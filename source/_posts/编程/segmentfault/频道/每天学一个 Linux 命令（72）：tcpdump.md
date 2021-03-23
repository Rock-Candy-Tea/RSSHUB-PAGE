
---
title: '每天学一个 Linux 命令（72）：tcpdump'
categories: 
 - 编程
 - segmentfault
 - 频道
headimg: '/images/404.gif'
author: segmentfault
comments: false
date: 2021-03-23 20:17:33
thumbnail: '/images/404.gif'
---

<div>   
<h2>命令简介</h2><p>tcpdump 命令是一款类 Unix/Linux 环境下的抓包工具。</p><p>tcpdump采用命令行方式对接口的数据包进行筛选抓取，如果不带任何选项的tcpdump，默认会抓取第一个网络接口，且只有将tcpdump进程终止才会停止抓包。</p><pre><code>[root@CentOS7-1 ~]# tcpdump
-bash: tcpdump: command not found
[root@CentOS7-1 ~]# yum install tcpdump -y
</code></pre><h2>语法格式</h2><pre><code>[root@CentOS7-1 ~]# tcpdump --help
tcpdump version 4.9.2
libpcap version 1.5.3
OpenSSL 1.0.2k-fips  26 Jan 2017
Usage: tcpdump [-aAbdDefhHIJKlLnNOpqStuUvxX#] [ -B size ] [ -c count ]
  [ -C file_size ] [ -E algo:secret ] [ -F file ] [ -G seconds ]
  [ -i interface ] [ -j tstamptype ] [ -M secret ] [ --number ]
  [ -Q|-P in|out|inout ]
  [ -r file ] [ -s snaplen ] [ --time-stamp-precision precision ]
  [ --immediate-mode ] [ -T type ] [ --version ] [ -V file ]
  [ -w file ] [ -W filecount ] [ -y datalinktype ] [ -z postrotate-command ]
  [ -Z user ] [ expression ]
</code></pre><h2>选项说明</h2><p>抓包选项</p><pre><code>-c            #指定要抓取的包数量
-i interface  #指定要监听的接口
-n   #对地址以数字方式显式
-n   #端口显示为数值
-N   #不打印出host的域名部分
-P   #指定要抓取的包是流入还是流出的包
-s len   #设置数据包抓取长度为len，默认将会是65535字节
</code></pre><p>输出选项</p><pre><code>-e   #输出的每行中都将包括数据链路层头部信息
-q   #快速打印输出
-X   #输出包的头部数据
-XX  #输出包的头部数据
-v   #详细的输出
-vv  #比-v更详细的输出
-vvv #比-vv更详细的输出
</code></pre><p>其他选项</p><pre><code>-D  #查询可以抓包的接口
-F  #从文件中读取抓包的表达式
-w  #将抓包的数据输出到文件
-r  #从指定的数据包文件中读取数据
</code></pre><p>推荐给你：<a href="http://mp.weixin.qq.com/s?__biz=MzI0MDQ4MTM5NQ==&mid=2247500085&idx=2&sn=5455a50a3ec0fc0a69a7cc910a316ebe&chksm=e918a429de6f2d3f4ba700653b387459cb16dd4bf34cd42b4b0ef53c2dd91a53ce40abf0f2a2&scene=21#wechat_redirect" rel="nofollow">值得收藏！Linux系统常用命令速查手册</a></p><p>所以常用的选项也就这几个：</p><pre><code>tcpdump -D
tcpdump -c num -i int -nn -XX -vvv
</code></pre><h2>应用举例</h2><p>实例</p><pre><code>[root@CentOS7-1 ~]# tcpdump -i ens33
tcpdump: verbose output suppressed, use -v or -vv for full protocol decode
listening on ens33, link-type EN10MB (Ethernet), capture size 262144 bytes
08:43:32.649405 IP CentOS7-1.ssh > 192.168.1.93.62148: Flags [P.], seq 1603116601:1603116813, ack 87129926, win 273, length 212
08:43:32.650284 IP CentOS7-1.54879 > public1.alidns.com.domain: 63951+ PTR? 93.1.168.192.in-addr.arpa. (43)
08:43:32.679205 IP public1.alidns.com.domain > CentOS7-1.54879: 63951 NXDomain 0/1/0 (120)
08:43:32.680996 IP CentOS7-1.50467 > public1.alidns.com.domain: 7677+ PTR? 100.1.168.192.in-addr.arpa. (44)
08:43:32.693832 IP 192.168.1.93.62148 > CentOS7-1.ssh: Flags [.], ack 212, win 4101, length 0
08:43:32.708977 IP public1.alidns.com.domain > CentOS7-1.50467: 7677 NXDomain 0/1/0 (121)
08:43:32.709897 IP CentOS7-1.54341 > public1.alidns.com.domain: 22823+ PTR? 5.5.5.223.in-addr.arpa. (40)
08:43:32.710391 IP CentOS7-1.ssh > 192.168.1.93.62148: Flags [P.], seq 212:392, ack 1, win 273, length 180
08:43:32.731500 IP public1.alidns.com.domain > CentOS7-1.54341: 22823 1/0/0 PTR public1.alidns.com. (72)
08:43:32.733069 IP CentOS7-1.ssh > 192.168.1.93.62148: Flags [P.], seq 392:1260, ack 1, win 273, length 868
08:43:32.733632 IP 192.168.1.93.62148 > CentOS7-1.ssh: Flags [.], ack 1260, win 4106, length 0
08:43:32.733936 IP CentOS7-1.ssh > 192.168.1.93.62148: Flags [P.], seq 1260:1520, ack 1, win 273, length 260
08:43:32.734278 IP CentOS7-1.ssh > 192.168.1.93.62148: Flags [P.], seq 1520:1684, ack 1, win 273, length 164
08:43:32.734619 IP 192.168.1.93.62148 > CentOS7-1.ssh: Flags [.], ack 1684, win 4104, length 0
</code></pre><p>抓取Ping数据包</p><pre><code>[root@CentOS7-1 ~]# tcpdump -c 5 -nn -i ens33 icmp
tcpdump: verbose output suppressed, use -v or -vv for full protocol decode
listening on ens33, link-type EN10MB (Ethernet), capture size 262144 bytes
08:53:52.652906 IP 192.168.1.199 > 192.168.1.100: ICMP echo request, id 1368, seq 1, length 64
08:53:52.654987 IP 192.168.1.100 > 192.168.1.199: ICMP echo reply, id 1368, seq 1, length 64
08:53:53.659034 IP 192.168.1.199 > 192.168.1.100: ICMP echo request, id 1368, seq 2, length 64
08:53:53.659095 IP 192.168.1.100 > 192.168.1.199: ICMP echo reply, id 1368, seq 2, length 64
08:53:54.667539 IP 192.168.1.199 > 192.168.1.100: ICMP echo request, id 1368, seq 3, length 64
5 packets captured
7 packets received by filter
0 packets dropped by kernel
</code></pre><p>分析数据包</p><pre><code>[root@CentOS7-1 ~]# tcpdump -c 2 -q -XX -vvv -nn -i ens33 tcp dst port 22
tcpdump: listening on ens33, link-type EN10MB (Ethernet), capture size 262144 bytes
08:55:43.606727 IP (tos 0x0, ttl 64, id 27235, offset 0, flags [DF], proto TCP (6), length 40)
    192.168.1.93.62148 > 192.168.1.100.22: tcp 0
 0x0000:  000c 2925 626f f875 a47d f4ec 0800 4500  ..)%bo.u.&#125;....E.
 0x0010:  0028 6a63 4000 4006 4c5b c0a8 015d c0a8  .(jc@.@.L[...]..
 0x0020:  0164 f2c4 0016 0531 cb7e 5f9f 9479 5010  .d.....1.~_..yP.
 0x0030:  1005 641a 0000 0000 0000 0000            ..d.........
08:55:43.651422 IP (tos 0x0, ttl 64, id 27236, offset 0, flags [DF], proto TCP (6), length 40)
    192.168.1.93.62148 > 192.168.1.100.22: tcp 0
 0x0000:  000c 2925 626f f875 a47d f4ec 0800 4500  ..)%bo.u.&#125;....E.
 0x0010:  0028 6a64 4000 4006 4c5a c0a8 015d c0a8  .(jd@.@.LZ...]..
 0x0020:  0164 f2c4 0016 0531 cb7e 5f9f 964d 5010  .d.....1.~_..MP.
 0x0030:  100a 6241 0000 0000 0000 0000            ..bA........
2 packets captured
3 packets received by filter
0 packets dropped by kernel
</code></pre><p><a href="http://mp.weixin.qq.com/s?__biz=MzI0MDQ4MTM5NQ==&mid=2247510302&idx=3&sn=0aeca994c0c995c7372fccd78b1a799e&chksm=e918cc02de6f45146ed734a56c3d999dc3021c7c7c54dc717de658813a63c18336233565a041&scene=21#wechat_redirect" rel="nofollow">每天学一个 Linux 命令（70）：dig</a></p><p><a href="http://mp.weixin.qq.com/s?__biz=MzI0MDQ4MTM5NQ==&mid=2247510344&idx=2&sn=5e160968cac5e504cd858de1396b01ca&chksm=e918cc54de6f4542080756783030918c2a44fc47d04d8e63abe4f83ce96a3de10cdfdfac87c1&scene=21#wechat_redirect" rel="nofollow">每天学一个 Linux 命令（71）：traceroute</a></p>  
</div>
            