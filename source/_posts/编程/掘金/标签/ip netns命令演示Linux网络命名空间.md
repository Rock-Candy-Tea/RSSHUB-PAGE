
---
title: 'ip netns命令演示Linux网络命名空间'
categories: 
 - 编程
 - 掘金
 - 标签
headimg: 'https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/26db99ff3d6e491dbcaea772cc956992~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Tue, 13 Jul 2021 18:36:53 GMT
thumbnail: 'https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/26db99ff3d6e491dbcaea772cc956992~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>为了支持网络协议栈的多个实例，linux在网络栈中引入了网络命令空间。处于不同命名空间的网络栈是完全隔离的，彼此之间无法通信，通过对网络资源的隔离，就能在一个宿主机上虚拟出多个不同的网络环境，Docker就是利用了网络命名空间实现了不同容器之间的网络隔离。</p>
<h3 data-id="heading-0">网络命名空间操作</h3>
<pre><code class="copyable">查看网络命名空间
ip netns list

添加一个命名空间
ip netns add <name>

在命名空间执行命令
ip netns exec <name> <command>
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-1">演示命名空间</h3>
<p>添加test1，test2网络命名空间</p>
<pre><code class="copyable">ip netns add test1

ip netns add test2
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/26db99ff3d6e491dbcaea772cc956992~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>查看test1,test2网卡</p>
<pre><code class="copyable">[root@gundy ~]# ip netns exec test1 ip a
1: lo: <LOOPBACK> mtu 65536 qdisc noop state DOWN group default qlen 1000
    link/loopback 00:00:00:00:00:00 brd 00:00:00:00:00:00
[root@gundy ~]# ip netns exec test2 ip a
1: lo: <LOOPBACK> mtu 65536 qdisc noop state DOWN group default qlen 1000
    link/loopback 00:00:00:00:00:00 brd 00:00:00:00:00:00
<span class="copy-code-btn">复制代码</span></code></pre>
<p>只有lo本地回环口，状态是DOWN</p>
<p>通过Veth设备对将二个命名空间联系起来，Veth设备对都是成对出现的，很像一对以太网卡，并且中间有一根直连的网线, 将其中一端成为另一端的peer.
<img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/b83660c3687647f68745e87f0915d6c4~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-2">对Veth设备对的操作</h3>
<p>创建Veth设备对</p>
<pre><code class="copyable">[root@gundy ~]# ip link add veth-test1 type veth peer name veth-test2
<span class="copy-code-btn">复制代码</span></code></pre>
<p>创建后，可以查看Veth设备对的信息</p>
<pre><code class="copyable">[root@gundy ~]# ip link show
1: lo: <LOOPBACK,UP,LOWER_UP> mtu 65536 qdisc noqueue state UNKNOWN mode DEFAULT group default qlen 1000
   link/loopback 00:00:00:00:00:00 brd 00:00:00:00:00:00
2: eth0: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc fq_codel state UP mode DEFAULT group default qlen 1000
   link/ether 00:16:3e:0c:20:db brd ff:ff:ff:ff:ff:ff
3: veth-test2@veth-test1: <BROADCAST,MULTICAST,M-DOWN> mtu 1500 qdisc noop state DOWN mode DEFAULT group default qlen 1000
   link/ether 76:dd:e3:28:a2:46 brd ff:ff:ff:ff:ff:ff
4: veth-test1@veth-test2: <BROADCAST,MULTICAST,M-DOWN> mtu 1500 qdisc noop state DOWN mode DEFAULT group default qlen 1000
   link/ether 7a:42:dd:ee:76:46 brd ff:ff:ff:ff:ff:ff
<span class="copy-code-btn">复制代码</span></code></pre>
<p>将veth-test1添加到namespace test1里</p>
<pre><code class="copyable">ip link set veth-test1 netns test1
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="copyable">[root@gundy ~]# ip link show
1: lo: <LOOPBACK,UP,LOWER_UP> mtu 65536 qdisc noqueue state UNKNOWN mode DEFAULT group default qlen 1000
    link/loopback 00:00:00:00:00:00 brd 00:00:00:00:00:00
2: eth0: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc fq_codel state UP mode DEFAULT group default qlen 1000
    link/ether 00:16:3e:0c:20:db brd ff:ff:ff:ff:ff:ff
3: veth-test2@if4: <BROADCAST,MULTICAST> mtu 1500 qdisc noop state DOWN mode DEFAULT group default qlen 1000
    link/ether 76:dd:e3:28:a2:46 brd ff:ff:ff:ff:ff:ff link-netns test1
    
// test1里面多了一个veth-test1
[root@gundy ~]# ip  netns exec  test1 ip link
1: lo: <LOOPBACK,UP,LOWER_UP> mtu 65536 qdisc noqueue state UNKNOWN mode DEFAULT group default qlen 1000
    link/loopback 00:00:00:00:00:00 brd 00:00:00:00:00:00
4: veth-test1@if3: <BROADCAST,MULTICAST> mtu 1500 qdisc noop state DOWN mode DEFAULT group default qlen 1000
    link/ether 7a:42:dd:ee:76:46 brd ff:ff:ff:ff:ff:ff link-netnsid 0
<span class="copy-code-btn">复制代码</span></code></pre>
<p>将veth-test2添加到namespace test2里</p>
<pre><code class="copyable">ip link set veth-test2 netns test2
<span class="copy-code-btn">复制代码</span></code></pre>
<p>目前只有mac地址，没有ip地址 状态都是down, 现在给他们分配ip地址</p>
<p>ip netns exec test1  ip addr add 192.168.1.1/24 dev veth-test1
ip netns exec test2  ip addr add 192.168.1.2/24 dev veth-test2</p>
<p>启动他们</p>
<pre><code class="copyable">ip netns exec test1 ip link set dev veth-test1 up
ip netns exec test2 ip link set dev veth-test2 up
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="copyable">[root@gundy ~]# ip netns exec test1 ip link set dev veth-test1 up
[root@gundy ~]# ip netns exec test2 ip link set dev veth-test2 up


[root@gundy ~]# ip netns exec test1 ip link
1: lo: <LOOPBACK,UP,LOWER_UP> mtu 65536 qdisc noqueue state UNKNOWN mode DEFAULT group default qlen 1000
    link/loopback 00:00:00:00:00:00 brd 00:00:00:00:00:00
4: veth-test1@if3: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc noqueue state UP mode DEFAULT group default qlen 1000
    link/ether 7a:42:dd:ee:76:46 brd ff:ff:ff:ff:ff:ff link-netns test2
[root@gundy ~]# ip netns exec test2 ip link
1: lo: <LOOPBACK> mtu 65536 qdisc noop state DOWN mode DEFAULT group default qlen 1000
    link/loopback 00:00:00:00:00:00 brd 00:00:00:00:00:00
3: veth-test2@if4: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc noqueue state UP mode DEFAULT group default qlen 1000
    link/ether 76:dd:e3:28:a2:46 brd ff:ff:ff:ff:ff:ff link-netns test1
<span class="copy-code-btn">复制代码</span></code></pre>
<p>目前状态都是up的了， 查看ip地址</p>
<pre><code class="copyable">[root@gundy ~]# ip netns exec test1 ip a
1: lo: <LOOPBACK,UP,LOWER_UP> mtu 65536 qdisc noqueue state UNKNOWN group default qlen 1000
    link/loopback 00:00:00:00:00:00 brd 00:00:00:00:00:00
    inet 127.0.0.1/8 scope host lo
       valid_lft forever preferred_lft forever
    inet6 ::1/128 scope host
       valid_lft forever preferred_lft forever
4: veth-test1@if3: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc noqueue state UP group default qlen 1000
    link/ether 7a:42:dd:ee:76:46 brd ff:ff:ff:ff:ff:ff link-netns test2
    inet 192.168.1.1/24 scope global veth-test1
       valid_lft forever preferred_lft forever
    inet6 fe80::7842:ddff:feee:7646/64 scope link
       valid_lft forever preferred_lft forever
       
[root@gundy ~]# ip netns exec test2 ip a
1: lo: <LOOPBACK> mtu 65536 qdisc noop state DOWN group default qlen 1000
    link/loopback 00:00:00:00:00:00 brd 00:00:00:00:00:00
3: veth-test2@if4: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc noqueue state UP group default qlen 1000
    link/ether 76:dd:e3:28:a2:46 brd ff:ff:ff:ff:ff:ff link-netns test1
    inet 192.168.1.2/24 scope global veth-test2
       valid_lft forever preferred_lft forever
    inet6 fe80::74dd:e3ff:fe28:a246/64 scope link
       valid_lft forever preferred_lft forever

<span class="copy-code-btn">复制代码</span></code></pre>
<p>这样test1、test2二个网络命名空间就通了，通过ping测试</p>
<pre><code class="copyable">[root@gundy ~]# ip netns exec test1 ping 192.168.1.2
PING 192.168.1.2 (192.168.1.2) 56(84) bytes of data.
64 bytes from 192.168.1.2: icmp_seq=1 ttl=64 time=0.041 ms
64 bytes from 192.168.1.2: icmp_seq=2 ttl=64 time=0.043 ms
64 bytes from 192.168.1.2: icmp_seq=3 ttl=64 time=0.033 ms
64 bytes from 192.168.1.2: icmp_seq=4 ttl=64 time=0.030 ms
--- 192.168.1.2 ping statistics ---
4 packets transmitted, 4 received, 0% packet loss, time 63ms
rtt min/avg/max/mdev = 0.030/0.036/0.043/0.009 ms


[root@gundy ~]# ip netns exec test2 ping 192.168.1.1
PING 192.168.1.1 (192.168.1.1) 56(84) bytes of data.
64 bytes from 192.168.1.1: icmp_seq=1 ttl=64 time=0.020 ms
64 bytes from 192.168.1.1: icmp_seq=2 ttl=64 time=0.037 ms
64 bytes from 192.168.1.1: icmp_seq=3 ttl=64 time=0.033 ms
64 bytes from 192.168.1.1: icmp_seq=4 ttl=64 time=0.036 ms
64 bytes from 192.168.1.1: icmp_seq=5 ttl=64 time=0.046 ms
--- 192.168.1.1 ping statistics ---
5 packets transmitted, 5 received, 0% packet loss, time 104ms
rtt min/avg/max/mdev = 0.020/0.034/0.046/0.009 ms
<span class="copy-code-btn">复制代码</span></code></pre>
<p>现在的状态如下图所示：
<img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/d5c6630e1aca4522ad9cff38df5467ac~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p></div>  
</div>
            