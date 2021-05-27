
---
title: '记一次 Kubernetes 网络故障深度追踪'
categories: 
 - 编程
 - Dockone
 - 周报
headimg: 'https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210522/965f7da47cab1bce7c1985a3ece636bb.jpg'
author: Dockone
comments: false
date: 2021-05-27 04:46:39
thumbnail: 'https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210522/965f7da47cab1bce7c1985a3ece636bb.jpg'
---

<div>   
<br>某天晚上，客户碰到了 Kubernetes 集群一直扩容失败，所有的节点都无法正常加入集群。在经过多番折腾无解后，反馈到我们这里进行技术支持。这个问题的整个排查过程比较有意思，所以对其中的排查思路和用到的方法进行整理分享。<br>
<h3>问题现象</h3>运维同学在对客户的 Kubernetes 集群进行节点扩容时，发现新增的节点一直添加失败。该同学进行了初步的排查如下：<br>
<ul><li>在新增节点上，访问 Kubernetes master service vip 网络不通</li><li>在新增节点上，直接访问 Kubernetes master hostIP + 6443 网络正常</li><li>在新增节点上，访问其他节点的容器 IP 可以正常 ping 通</li><li>在新增节点上，访问 coredns service vip 网络正常</li></ul><br>
<br>该客户使用的 Kubernetes 版本是 1.13.10，宿主机的内核版本是 4.18（CentOS 8.2）。<br>
<h3>问题排查过程</h3>收到该一线同事的反馈，我们已经初步怀疑是 IPVS 的问题。根据以往网络问题排查的经验，先对现场做了些常规排查：<br>
<ul><li>确认内核模块 ip_tables 是否加载（正常）</li><li>确认 iptable forward 是否默认 accpet （正常）</li><li>确认宿主机网络是否正常（正常）</li><li>确认容器网络是否正常（正常）</li><li>……</li></ul><br>
<br>排除了常规的问题之后，基本可以缩小范围，再继续基于 IPVS 相关层面进行排查。<br>
<h3>通过 ipvsadm 命令排查</h3>10.96.0.1 是客户集群 Kubernetes master service vip。<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210522/965f7da47cab1bce7c1985a3ece636bb.jpg" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210522/965f7da47cab1bce7c1985a3ece636bb.jpg" class="img-polaroid" title="1.jpg" alt="1.jpg" referrerpolicy="no-referrer"></a>
</div>
<br>
可以发现有异常连接，处于 SYN_RECV 的状态，并且可以观察到，启动时 kubelet + kube-proxy 是有正常建连的，说明是在启动之后，Kubernetes service 网络出现异常。<br>
<h3>tcpdump 抓包分析</h3>两端进行抓包，并通过  <code class="prettyprint">telnet 10.96.0.1 443</code>  命令进行确认。<br>
<br>结论：发现 SYN 包在本机没有发送出去。<br>
<h3>初步总结</h3>通过上面的排查，可以再次缩小范围，问题基本就在 kube-proxy 身上。我们采用了 IPVS 模式，也会依赖了 iptables 配置实现一些网络的转发、SNAT、drop 等等。<br>
<br>根据上面的排查过程，我们又缩小了范围，开始分析怀疑对象 kube-proxy。<br>
<h3>查看 kube-proxy 日志</h3><div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210522/6761136e605a914749e834533d4012f3.jpeg" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210522/6761136e605a914749e834533d4012f3.jpeg" class="img-polaroid" title="2.jpeg" alt="2.jpeg" referrerpolicy="no-referrer"></a>
</div>
<br>
发现异常日志，iptables-restore 命令执行异常。通过 Google、社区查看，确认问题。<br>
<br>相关 issue 链接可以参考下：<br>
<ul><li><a href="https://github.com/kubernetes/kubernetes/issues/73360" rel="nofollow" target="_blank">https://github.com/kubernetes/ ... 73360</a></li><li><a href="https://github.com/kubernetes/kubernetes/pull/84422/files" rel="nofollow" target="_blank">https://github.com/kubernetes/ ... files</a></li><li><a href="https://github.com/kubernetes/kubernetes/pull/82214/files" rel="nofollow" target="_blank">https://github.com/kubernetes/ ... files</a></li></ul><br>
<br><h3>继续深入</h3>通过代码查看（1.13.10 版本 pkg/proxy/ipvs/proxier.go:1427），可以发现该版本确实没有判断 KUBE-MARK-DROP 是否存在并创建的逻辑。当出现该链不存在时，会出现逻辑缺陷，导致 iptable 命令执行失败。<br>
<br>Kubernetes master service vip 不通，但是实际容器相关的 IP 是通的原因，与下面这条 iptable 规则有关：<br>
<pre class="prettyprint">iptable -t nat -A KUBE-SERVICES ! -s 9.0.0.0/8 -m comment --comment "Kubernetes service cluster ip + port for masquerade purpose" -m set --match-set KUBE-CLUSTER-IP dst,dst -j KUBE-MARK-MASQ<br>
</pre><br>
<h3>根因探究</h3>前面我们已经知道了 kube-proxy 1.13.10 版本存在缺陷，在没有创建 KUBE-MARK-DROP 链的情况下，执行 iptables-restore 命令配置规则。但是为何 Kubernetes 1.13.10 版本跑在 CentOS 8.2 4.18 内核的操作系统上会报错，跑在 CentOS 7.6 3.10 内核的操作系统上却正常呢？<br>
<br>查看下 kube-proxy 的源码，可以发现 kube-proxy 其实也就是执行 iptables 命令进行规则配置。那既然 kube-proxy 报错 iptables-restore 命令失败，我们就找一台 4.18 内核的机器，进入 kube-proxy 容器看下情况。<br>
<br>到容器内执行下 iptables-save 命令，可以发现 kube-proxy 容器内确实没有创建 KUBE-MARK-DROP 链（符合代码预期）。继续在宿主机上执行下 iptables-save 命令，却发现是有 KUBE-MARK-DROP 链。<br>
<br>这里有两个疑问：<br>
<ul><li>为何 4.18 内核宿主机的 iptables 有 KUBE-MARK-DROP 链？</li><li>为何 4.18 内核宿主机的 iptables 规则和 kube-proxy 容器内的规则不一致？</li></ul><br>
<br>第一个疑惑，凭感觉怀疑除了 kube-proxy，还会有别的程序在操作 iptables，继续撸下 Kubernetes 代码。<br>
<br>结论：发现确实除了 kube-proxy，还有 kubelet 也会修改 iptables 规则。具体代码可以查看 pkg/kubelet/kubelet_network_linux.go<br>
<br>第二个疑惑，继续凭感觉吧。Google 一发捞一下为何 kube-proxy 容器挂载了宿主机 /run/xtables.lock 文件的情况下，宿主机和容器 iptables 查看的规则不一致。<br>
<br>结论：CentOS 8 在网络方面摒弃 iptables 采用 nftables 框架作为默认的网络包过滤工具。<br>
<br>至此，所有的谜团都解开了。<br>
<br>团队完成过大量的客户项目交付，还是有些问题可以再解答下：<br>
<h4>问题一：为何这么多客户环境第一次碰到该情况？因为需要 Kubernetes 1.13.10 + centos 8.2 的操作系统，这个组合罕见，且问题是必现。升级 Kubernetes 1.16.0+ 就不会有该问题。</h4><h4>问题二：为何使用 Kubernetes 1.13.10 + 5.5 内核却没有该问题？</h4>因为那是与 CentOS 8 操作系统有关，我们手动升级 5.5 版本后，默认还是使用的 iptables 框架。<br>
<br>可以通过  <code class="prettyprint">iptables -v</code>  命令来确认，是否使用了 nftables。<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210522/1af591c41350f9642f26e08f540ae9a6.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210522/1af591c41350f9642f26e08f540ae9a6.png" class="img-polaroid" title="3.png" alt="3.png" referrerpolicy="no-referrer"></a>
</div>
<br>
nftables 是何方神圣？比 iptables 好么？这是另一个值得进一步学习的点，这里就不再深入了。<br>
<h3>解决方法</h3>针对以上的排查问题，我们总结下解决方法：<br>
<ul><li>调整内核版本到 3.10（CentOS 7.6+），或者手动升级内核版本到 5.0 +；</li><li>升级 Kubernetes 版本，当前确认 1.16.10+ 版本没有该问题。</li></ul><br>
<br>原文链接：<a href="https://zhuanlan.zhihu.com/p/364382294" rel="nofollow" target="_blank">https://zhuanlan.zhihu.com/p/364382294</a>
                                                                <div class="aw-upload-img-list">
                                                                                                                                                                                                                                                                </div>
                                
                                                                <ul class="aw-upload-file-list">
                                                                                                                                                                                                                                                                                            </ul>
                                                              
</div>
            