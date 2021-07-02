
---
title: '一次有趣的 Docker 网络问题排查经历'
categories: 
 - 编程
 - Dockone
 - 周报
headimg: 'https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210628/8c70fcfe1dfa77dfd5541b8b0f5db067.jpg'
author: Dockone
comments: false
date: 2021-07-02 01:52:20
thumbnail: 'https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210628/8c70fcfe1dfa77dfd5541b8b0f5db067.jpg'
---

<div>   
<br>前段时间公司的安卓打包服务出现问题，现象是在上传 360 服务器进行加固的时候，非常大概率会卡在上传阶段，长时间重试最后失败。我对这个情况进行了一些排查分析，解决了这个问题，写了这篇长文复盘了排查的经历，会涉及到下面这些内容。<br>
<ul><li>Docker 桥接模式网络模型</li><li>Netfilter 与 NAT 原理</li><li>Systemtap 在内核探针中的用法</li></ul><br>
<br><h3>现象描述</h3>打包服务的部署结构这样的：安卓打包环境被打包为一个 Docker 镜像，部署在某台物理机上，这镜像会完成代码编译打包、加固、签名、生成渠道包的功能，如下图所示：<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210628/8c70fcfe1dfa77dfd5541b8b0f5db067.jpg" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210628/8c70fcfe1dfa77dfd5541b8b0f5db067.jpg" class="img-polaroid" title="1.jpg" alt="1.jpg" referrerpolicy="no-referrer"></a>
</div>
<br>
问题就出在上传 APK 这一步，传到一部分就卡住，360 的 SDK 提示超时等异常，如下图所示：<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210628/36cd31bfebc2764550c1950b28560d9c.jpg" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210628/36cd31bfebc2764550c1950b28560d9c.jpg" class="img-polaroid" title="2.jpg" alt="2.jpg" referrerpolicy="no-referrer"></a>
</div>
<br>
通过在宿主机和容器内分别抓包，我们发现了这样一些现象。<br>
<br>宿主机的抓包如下，序号为 881 的包是一个延迟的 ACK，它的 ACK 值为 530104，比这个 ACK 号更大的序列号在 875 的那个包已经确认过了（序列号为 532704，随后宿主机发送了一个 RST 包给远程的 360 加固服务器。<br>
<br>再后面就是不停重试发送数据，上传卡住也就对应这个不断重试发送数据的阶段，如下图所示：<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210628/273e4acd1180ce34b31199e1488a5d22.jpg" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210628/273e4acd1180ce34b31199e1488a5d22.jpg" class="img-polaroid" title="3.jpg" alt="3.jpg" referrerpolicy="no-referrer"></a>
</div>
<br>
在容器侧抓包，并没有出现这个 RST，其它的包一样，如下图所示：<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210628/7fe2a3eba3afa988cd6347221a6a144a.jpg" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210628/7fe2a3eba3afa988cd6347221a6a144a.jpg" class="img-polaroid" title="4.jpg" alt="4.jpg" referrerpolicy="no-referrer"></a>
</div>
<br>
因为容器侧没有感知到连接的异常，容器内的服务就一直在不停的重试上传，经过多次重试以后依然是失败的。<br>
<h3>初步的排查分析</h3>一开始的疑虑是，是不是因为收到了延迟到达的 ACK，所以回复 RST 呢？<br>
<br>这不应该，在 TCP 协议规范中，收到延迟到达的 ACK，忽略即可，不必回复 ACK，那到底为什么会发 RST 包呢？<br>
<br>那是不是这个包本来就不合法呢？经过仔细分析这个包的信息，没有发现什么异常。从已有的 TCP 原理知识，已经没法推断这个现象了。<br>
<br>黔驴技穷，没有什么思路，这个时候就该用上 systemtap，来看看 rst 包到底是哪里发出来。<br>
<br>通过查看内核的代码，发送 rst 包的函数主要是下面这两个：<br>
<pre class="prettyprint">tcp_v4_send_reset@net/ipv4/tcp_ipv4.c<br>
<br>
static void tcp_v4_send_reset(struct sock *sk, struct sk_buff *skb) &#123;<br>
&#125;<br>
<br>
tcp_send_active_reset@net/ipv4/tcp_output.c<br>
<br>
void tcp_send_active_reset(struct sock *sk, gfp_t priority) &#123;<br>
&#125; <br>
</pre><br>
接下来 systemtap 注入这两个函数即可。<br>
<pre class="prettyprint">probe kernel.function("tcp_send_active_reset@net/ipv4/tcp_output.c").call &#123;<br>
printf ("\n%-25s %s<-%s\n", ctime(gettimeofday_s()) ,execname(), ppfunc());<br>
if ($sk) &#123;<br>
    src_addr = tcp_src_addr($sk);<br>
    src_port = tcp_src_port($sk);<br>
    dst_addr = tcp_dst_addr($sk);<br>
    dst_port = tcp_dst_port($sk);<br>
    if (src_port == 443 || dst_port == 443) &#123;<br>
      printf (">>>>>>>>>[%s->%s] %s<-%s %d\n", str_addr(src_addr, src_port), str_addr(dst_addr, dst_port), execname(), ppfunc(), dst_port);<br>
      print_backtrace();<br>
    &#125;<br>
&#125;<br>
&#125;<br>
<br>
probe kernel.function("tcp_v4_send_reset@net/ipv4/tcp_ipv4.c").call &#123;<br>
printf ("\n%-25s %s<-%s\n", ctime(gettimeofday_s()) ,execname(), ppfunc());<br>
if ($sk) &#123;<br>
    src_addr = tcp_src_addr($sk);<br>
    src_port = tcp_src_port($sk);<br>
    dst_addr = tcp_dst_addr($sk);<br>
    dst_port = tcp_dst_port($sk);<br>
    if (src_port == 443 || dst_port == 443) &#123;<br>
      printf (">>>>>>>>>[%s->%s] %s<-%s %d\n", str_addr(src_addr, src_port), str_addr(dst_addr, dst_port), execname(), ppfunc(), dst_port);<br>
      print_backtrace();<br>
    &#125;<br>
&#125; else if ($skb) &#123;<br>
    header = __get_skb_tcphdr($skb);<br>
    src_port = __tcp_skb_sport(header)<br>
    dst_port = __tcp_skb_dport(header)<br>
    if (src_port == 443 || dst_port == 443) &#123;<br>
        try &#123;<br>
            iphdr = __get_skb_iphdr($skb)<br>
            src_addr_str = format_ipaddr(__ip_skb_saddr(iphdr), @const("AF_INET"))<br>
            dst_addr_str = format_ipaddr(__ip_skb_daddr(iphdr), @const("AF_INET"))<br>
<br>
            tcphdr = __get_skb_tcphdr($skb)<br>
            urg = __tcp_skb_urg(tcphdr)<br>
            ack = __tcp_skb_ack(tcphdr)<br>
            psh = __tcp_skb_psh(tcphdr)<br>
            rst = __tcp_skb_rst(tcphdr)<br>
            syn = __tcp_skb_syn(tcphdr)<br>
            fin = __tcp_skb_fin(tcphdr)<br>
<br>
            printf ("skb [%s:%d->%s:%d] ack:%d, psh:%d, rst:%d, syn:%d fin:%d %s<-%s %d\n",<br>
                    src_addr_str, src_port, dst_addr_str, dst_port, ack, psh, rst, syn, fin, execname(), ppfunc(), dst_port);<br>
            print_backtrace();<br>
        &#125; <br>
        catch &#123; &#125;<br>
&#125;<br>
&#125; else &#123;<br>
      printf ("tcp_v4_send_reset else\n");<br>
      print_backtrace();<br>
&#125;<br>
&#125; <br>
</pre><br>
一运行就发现，出问题时，进入的是 tcp_v4_send_reset 这个函数，调用堆栈是：<br>
<pre class="prettyprint">Tue Jun 15 11:23:04 2021  swapper/6<-tcp_v4_send_reset<br>
skb [36.110.213.207:443->10.21.17.99:39700] ack:1, psh:0, rst:0, syn:0 fin:0 swapper/6<-tcp_v4_send_reset 39700<br>
0xffffffff99e5bc50 : tcp_v4_send_reset+0x0/0x460 [kernel]<br>
0xffffffff99e5d756 : tcp_v4_rcv+0x596/0x9c0 [kernel]<br>
0xffffffff99e3685d : ip_local_deliver_finish+0xbd/0x200 [kernel]<br>
0xffffffff99e36b49 : ip_local_deliver+0x59/0xd0 [kernel]<br>
0xffffffff99e364c0 : ip_rcv_finish+0x90/0x370 [kernel]<br>
0xffffffff99e36e79 : ip_rcv+0x2b9/0x410 [kernel]<br>
0xffffffff99df0b79 : __netif_receive_skb_core+0x729/0xa20 [kernel]<br>
0xffffffff99df0e88 : __netif_receive_skb+0x18/0x60 [kernel]<br>
0xffffffff99df0f10 : netif_receive_skb_internal+0x40/0xc0 [kernel]<br>
...<br>
</pre><br>
可以看到是在收到 ACK 包以后，调用 tcp_v4_rcv 来处理时发送的 RST，那到底是哪一行呢？<br>
<br>这就需要用到一个很厉害的工具 faddr2line，把堆栈中的信息还原为源码对应的行数。<br>
<pre class="prettyprint">wget https://raw.githubusercontent.com/torvalds/linux/master/scripts/faddr2line<br>
<br>
bash faddr2line /usr/lib/debug/lib/modules/`uname -r`/vmlinux tcp_v4_rcv+0x536/0x9c0<br>
<br>
tcp_v4_rcv+0x596/0x9c0:<br>
tcp_v4_rcv in net/ipv4/tcp_ipv4.c:1740<br>
</pre><br>
可以看到是在 tcp_ipv4.c 的 1740 行调用了 tcp_v4_send_reset 函数。<br>
<pre class="prettyprint">int tcp_v4_rcv(struct sk_buff *skb)<br>
&#123;<br>
struct sock *sk;<br>
<br>
sk = __inet_lookup_skb(&tcp_hashinfo, skb, th->source, th->dest);<br>
if (!sk)<br>
    goto no_tcp_socket;<br>
<br>
...<br>
<br>
no_tcp_socket:<br>
if (!xfrm4_policy_check(NULL, XFRM_POLICY_IN, skb))<br>
    goto discard_it;<br>
<br>
if (skb->len < (th->doff << 2) || tcp_checksum_complete(skb)) &#123;<br>
csum_error:<br>
    TCP_INC_STATS_BH(net, TCP_MIB_CSUMERRORS);<br>
bad_packet:<br>
    TCP_INC_STATS_BH(net, TCP_MIB_INERRS);<br>
&#125; else &#123;<br>
    tcp_v4_send_reset(NULL, skb);  // 1739 行<br>
&#125;<br>
&#125; <br>
</pre><br>
唯一可能调用到的逻辑就是找不到这个包对应的套接字信息，sk 为 NULL，然后走到 no_tcp_socket 标签处，然后走到 else 的流程，才有可能。<br>
<br>这怎么可能呢？连接好好的存在，怎么可能收到一个延迟到达的 ack 包处理的时候找不到这个连接套接字了呢？接下来我们来看 __inet_lookup_skb 函数的底层实现，最终走到了 __inet_lookup_established 这个函数。<br>
<pre class="prettyprint">struct sock *__inet_lookup_established(struct net *net,<br>
              struct inet_hashinfo *hashinfo,<br>
              const __be32 saddr, const __be16 sport,<br>
              const __be32 daddr, const u16 hnum,<br>
              const int dif) <br>
</pre><br>
刨去现有的现象，有一个很类似的 RST 的场景是，往一个没有监听某端口的服务发送包。这个包没有对应的连接，内核就会回复 RST，告知发送端无法处理这个包。<br>
<br>到这里，排查陷入了僵局。为什么明明连接还在，内核协议栈就是找不到呢？<br>
<h3>Docker 桥接模式网络包流通方式</h3>Docker 进程启动时，会在主机上创建一个名为 docker0 的虚拟网桥，这个主机上的 docker 容器会连接到这个虚拟网桥上。<br>
<br>容器启动后，Docker 会生成一对 veth 接口（veth pair），本质相当于软件实现的以太网连接，Docker 通过 veth 把容器内的 eth0 连接到 docker0 网桥。外部的连接可以通过 IP 伪装（IP masquerading）的方式提供，IP 伪装是网络地址转换（NAT）的一种方式，以 IP 转发（IP forwarding）和 iptables 规则建立。<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210628/efd0ffadc34f1d7272e841c020326d78.jpg" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210628/efd0ffadc34f1d7272e841c020326d78.jpg" class="img-polaroid" title="5.jpg" alt="5.jpg" referrerpolicy="no-referrer"></a>
</div>
<br>
<h3>深入 Netfilter 与 NAT</h3>Netfilter 是一个 Linux 内核框架，它在内核协议栈中设置了若干hook 点，以此对数据包进行拦截、过滤或其他处理。从简单的防火墙，到对网络通信数据的详细分析，到复杂的、依赖于状态的分组过滤器，它都可以实现。<br>
<br>Docker 利用了它的 NAT（network address translation，网络地址转换）特性，根据某些规则来转换源地址和目标地址。iptables 正是一个用户态用于管理这些 Netfilter 的工具。<br>
<br>对于这个场景中的部署结构，它的原理如下图所示：<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210628/68d02fce4cf37dfb443ee9c974ade0bd.jpg" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210628/68d02fce4cf37dfb443ee9c974ade0bd.jpg" class="img-polaroid" title="6.jpg" alt="6.jpg" referrerpolicy="no-referrer"></a>
</div>
<br>
经过查看 netfilter 的代码，发现它会把 out of window 的包标记为 INVALID 状态，源码见  <code class="prettyprint">net/netfilter/nf_conntrack_proto_tcp.c</code>：<br>
<pre class="prettyprint">/* Returns verdict for packet, or -1 for invalid. */<br>
static int tcp_packet(struct nf_conn *ct,<br>
          const struct sk_buff *skb,<br>
          unsigned int dataoff,<br>
          enum ip_conntrack_info ctinfo,<br>
          u_int8_t pf,<br>
          unsigned int hooknum,<br>
          unsigned int *timeouts) &#123;<br>
<br>
// ...  <br>
<br>
if (!tcp_in_window(ct, &ct->proto.tcp, dir, index,<br>
           skb, dataoff, th, pf)) &#123;<br>
    spin_unlock_bh(&ct->lock);<br>
    return -NF_ACCEPT;<br>
&#125;<br>
&#125; <br>
</pre><br>
口说无凭，上面只是理论分析，你怎么就能说是一个 ACK 导致的 invalid 包呢？<br>
<br>我们可以通过 iptables 的规则，把 invalid 的包打印出来。<br>
<pre class="prettyprint">iptables -A INPUT -m conntrack --ctstate INVALID -m limit --limit 1/sec   -j LOG --log-prefix "invalid: " --log-level 7<br>
</pre><br>
添加上面的规则以后，再次运行加固上传的脚本，同时开始抓包，现象重现。<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210628/a1bcd8c890d4c19ae74b5f4e5fb3542a.jpg" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210628/a1bcd8c890d4c19ae74b5f4e5fb3542a.jpg" class="img-polaroid" title="7.jpg" alt="7.jpg" referrerpolicy="no-referrer"></a>
</div>
<br>
然后在 dmesg 中查看对应的日志。<br><br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210628/583e96239b7298a934425bb2274cb45d.jpg" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210628/583e96239b7298a934425bb2274cb45d.jpg" class="img-polaroid" title="8.jpg" alt="8.jpg" referrerpolicy="no-referrer"></a>
</div>
<br>
以第一行为例，它的 LEN=40，也就是 20 IP 头 + 20 字节 TCP 头，ACK 位被置位，表示这是一个没有任何内容的 ACK 包，对应于上图中 RST 包的前一个 ACK 包。这个包的详情如下图，Window 等于 187 也是对的上的。<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210628/9262e05f8424c7d61de99815335e91ee.jpg" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210628/9262e05f8424c7d61de99815335e91ee.jpg" class="img-polaroid" title="9.jpg" alt="9.jpg" referrerpolicy="no-referrer"></a>
</div>
<br>
如果是 INVALID 状态的包，netfilter 不会对其做 IP 和端口的 NAT 转换，这样协议栈再去根据 IP + 端口去找这个包的连接时，就会找不到，这个时候就会回复一个 RST，过程如下图所示。<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210628/72693e91bb665b5e94024ce39d4509a9.jpg" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210628/72693e91bb665b5e94024ce39d4509a9.jpg" class="img-polaroid" title="10.jpg" alt="10.jpg" referrerpolicy="no-referrer"></a>
</div>
<br>
这也印证了我们前面 __inet_lookup_skb 为 null，然后发送 RST 的代码逻辑。<br>
<h3>如何修改</h3>知道了原因，修改起来就很简单了，有两个改法。第一个改法有点粗暴，使用 iptables 把 invalid 包 drop 掉，不让它产生 RST。<br>
<pre class="prettyprint">iptables -A INPUT -m conntrack --ctstate INVALID -j DROP<br>
</pre><br>
这样修改以后，问题瞬间解决了，经过几十次的测试，一次都没有出现过上传超时和失败的情况。<br>
<br>这样修改有一个小问题，可能会误伤 FIN 包和一些其它真正 invalid 的包。有一个更加优雅的改法是修改 把内核选项  <code class="prettyprint">net.netfilter.nf_conntrack_tcp_be_liberal</code> 设置为 1：<br>
<pre class="prettyprint">sysctl -w "net.netfilter.nf_conntrack_tcp_be_liberal=1"<br>
net.netfilter.nf_conntrack_tcp_be_liberal = 1<br>
</pre><br>
把这个参数值设置为 1 以后，对于窗口外的包，将不会被标记为 INVALID，源码见 <code class="prettyprint">net/netfilter/nf_conntrack_proto_tcp.c</code>：<br>
<pre class="prettyprint">static bool tcp_in_window(const struct nf_conn *ct,<br>
          struct ip_ct_tcp *state,<br>
          enum ip_conntrack_dir dir,<br>
          unsigned int index,<br>
          const struct sk_buff *skb,<br>
          unsigned int dataoff,<br>
          const struct tcphdr *tcph,<br>
          u_int8_t pf) &#123;<br>
    ...<br>
<br>
    res = false;<br>
    if (sender->flags & IP_CT_TCP_FLAG_BE_LIBERAL ||<br>
        tn->tcp_be_liberal)<br>
        res = true;<br>
    ...<br>
return res;<br>
&#125; <br>
</pre><br>
最后来一个如丝般顺滑的上传截图结束本篇文章。<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210628/b041a7f9c00d5785f470ed14314f699c.jpg" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210628/b041a7f9c00d5785f470ed14314f699c.jpg" class="img-polaroid" title="11.jpg" alt="11.jpg" referrerpolicy="no-referrer"></a>
</div>
<br>
<h3>后记</h3>多看代码，怀疑一些不可能的现象。以上可能说的都是错误，看看方法就好。<br>
<br>原文链接：<a href="https://juejin.cn/post/6976101827179708453" rel="nofollow" target="_blank">https://juejin.cn/post/6976101827179708453</a>，作者：挖坑的张师傅
                                                                <div class="aw-upload-img-list">
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                </div>
                                
                                                                <ul class="aw-upload-file-list">
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            </ul>
                                                              
</div>
            