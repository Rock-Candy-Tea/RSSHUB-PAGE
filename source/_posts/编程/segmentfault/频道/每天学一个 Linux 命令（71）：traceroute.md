
---
title: '每天学一个 Linux 命令（71）：traceroute'
categories: 
 - 编程
 - segmentfault
 - 频道
headimg: 'https://segmentfault.com/img/bVbLc6v'
author: segmentfault
comments: false
date: 2021-03-24 00:02:30
thumbnail: 'https://segmentfault.com/img/bVbLc6v'
---

<div>   
<h2>命令简介</h2><p>traceroute 命令用于显示数据包到主机间的路径信息。traceroute 命令利用 IP 协议的“生存时间”字段，并尝试从每个网关到某个主机的路径引发 ICMP TIME_EXCEEDED 响应。</p><pre><code>[root@CentOS7-1 ~]# traceroute
-bash: traceroute: command not found
[root@CentOS7-1 ~]# yum install traceroute -y
</code></pre><h2>语法格式</h2><pre><code>traceroute [-46dFITUnreAV] [-f first_ttl] [-g gate,...] [-i device] 
           [-m max_ttl] [-p port] [-s src_addr] [-q nqueries] 
           [-N squeries] [-t tos] [-l flow_label] [-w waittime] 
           [-z sendwait] [-UL] [-D] [-P proto] [--sport=port] [-M method] 
           [-O mod_options] [--mtu] [--back] host [packet_len] </code></pre><h2>选项说明</h2><pre><code>-d            #使用Socket级的功能
-f<存活数值>   #设置第一个检测数据包的存活数值TTL的大小
-g<网关>      #设置来源路由网关，最多可设置8个
-i<网络界面>  #使用指定的网络界面送出数据包
-I   #使用ICMP回应取代UDP
-m<存活数值>  #设置检测数据包的最大存活数值TTL的大小
-n    #使用IP地址
-p<通信端口>  #设置UDP传输协议的通信端口
-r   #忽略Routing Table，直接将数据包送到远端主机上
-s<来源地址>  #设置本地主机送出数据包的IP地址
-t<服务类型>  #设置检测数据包的TOS数值
-v  #详细显示执行过程
-w<超时秒数>  #设置等待远端主机返回的时间
-x  #开启或关闭数据包的正确性检验
</code></pre><h2>应用举例</h2><p>实例</p><pre><code>[root@CentOS7-1 ~]# traceroute  www.bai.com
traceroute to www.bai.com (39.105.137.64), 30 hops max, 60 byte packets
 1  gateway (192.168.1.1)  1.362 ms  2.077 ms  1.252 ms
 2  100.106.0.1 (100.106.0.1)  6.903 ms  6.256 ms  4.887 ms
 3  112.26.21.65 (112.26.21.65)  5.686 ms  4.540 ms  5.581 ms
 4  221.183.48.53 (221.183.48.53)  5.430 ms  5.964 ms  5.573 ms
 5  221.183.40.33 (221.183.40.33)  25.211 ms  24.256 ms  23.582 ms
 6  * * *
 7  111.13.0.173 (111.13.0.173)  26.907 ms 111.13.188.37 (111.13.188.37)  30.360 ms 39.156.0.37 (39.156.0.37)  24.476 ms
 8  39.156.7.41 (39.156.7.41)  27.161 ms 39.156.1.225 (39.156.1.225)  28.306 ms 39.156.7.41 (39.156.7.41)  26.763 ms
 9  39.156.1.225 (39.156.1.225)  28.571 ms 39.156.7.41 (39.156.7.41)  26.401 ms  26.422 ms
10  * 116.251.105.78 (116.251.105.78)  27.443 ms 123.56.34.14 (123.56.34.14)  28.939 ms
11  119.38.212.89 (119.38.212.89)  28.758 ms 116.251.94.101 (116.251.94.101)  28.575 ms *
12  * * *
13  * * *
14  * * *
15  * * *
16  * * *
17  * * *
18  * * *
19  * * *
20  * * *
21  * * *
22  * * *
23  * * *
24  * * *
25  * * *
26  * * *
27  * * *
28  * * *
29  * * *
30  * * *
#每一行纪录就是一跳 ，每一跳表示一个网关，如果出现*可能是防火墙禁止了ICMP数据包
设置指定的跳数
</code></pre><pre><code>[root@CentOS7-1 ~]# traceroute -m 5  www.bai.com
traceroute to www.bai.com (39.105.137.64), 5 hops max, 60 byte packets
 1  gateway (192.168.1.1)  0.891 ms  0.987 ms  1.232 ms
 2  100.106.0.1 (100.106.0.1)  5.577 ms  4.535 ms  4.726 ms
 3  112.26.21.65 (112.26.21.65)  4.923 ms  5.276 ms  5.243 ms
 4  221.183.48.53 (221.183.48.53)  7.336 ms  5.865 ms  5.836 ms
 5  221.183.40.33 (221.183.40.33)  25.271 ms  24.109 ms  24.157 ms
</code></pre><p>显示IP地址，不查主机名</p><pre><code>[root@CentOS7-1 ~]# traceroute -n www.bai.com
traceroute to www.bai.com (39.105.137.64), 30 hops max, 60 byte packets
 1  192.168.1.1  0.814 ms  0.553 ms  0.578 ms
 2  100.106.0.1  6.032 ms  6.508 ms  6.238 ms
 3  112.26.21.65  4.854 ms  4.691 ms  9.640 ms
 4  221.183.48.53  7.241 ms  7.086 ms  6.928 ms
 5  221.183.40.33  25.174 ms  25.030 ms  25.194 ms
 6  * * *
 7  111.13.188.37  27.009 ms 111.13.0.173  25.983 ms 39.156.0.46  25.386 ms
 8  39.156.1.225  27.632 ms * 39.156.0.37  25.082 ms
 9  * 116.251.112.186  28.673 ms 39.156.7.41  26.949 ms
10  123.56.34.25  27.917 ms 116.251.94.113  27.853 ms 119.38.212.97  27.568 ms
11  116.251.105.78  30.888 ms 119.38.212.85  28.531 ms *
12  * * *
13  * * *
14  * * *
15  * * *
16  * * *
17  * * *
18  * * *
19  * * *
20  * * *
21  * * *
22  * * *
23  * * *
24  * * *
25  * * *
26  * * *
27  * * *
28  * * *
29  * * *
30  * * *
</code></pre><p>把探测包的个数设置为值5</p><pre><code>[root@CentOS7-1 ~]# traceroute -q 5 www.bai.com
traceroute to www.bai.com (39.105.137.64), 30 hops max, 60 byte packets
 1  gateway (192.168.1.1)  0.795 ms  0.568 ms  0.537 ms  0.474 ms  0.541 ms
 2  100.106.0.1 (100.106.0.1)  4.805 ms  4.414 ms  4.843 ms  4.588 ms  4.957 ms
 3  112.26.21.65 (112.26.21.65)  4.506 ms  4.574 ms  4.917 ms  4.877 ms  4.880 ms
 4  221.183.48.53 (221.183.48.53)  6.155 ms  5.354 ms  5.462 ms  5.264 ms  4.733 ms
 5  221.183.40.33 (221.183.40.33)  45.558 ms  24.936 ms  24.420 ms  24.374 ms  24.974 ms
 6  * * * * *
 7  39.156.0.46 (39.156.0.46)  25.993 ms 39.156.0.37 (39.156.0.37)  25.967 ms 111.13.0.173 (111.13.0.173)  26.491 ms 111.13.188.37 (111.13.188.37)  25.742 ms  26.645 ms
 8  * 39.156.0.37 (39.156.0.37)  25.074 ms 39.156.0.46 (39.156.0.46)  25.646 ms  25.533 ms 39.156.0.37 (39.156.0.37)  27.975 ms
 9  39.156.7.41 (39.156.7.41)  30.148 ms 39.156.1.225 (39.156.1.225)  27.671 ms  27.640 ms 39.156.7.41 (39.156.7.41)  27.215 ms  26.626 ms
10  116.251.112.206 (116.251.112.206)  28.230 ms 116.251.112.214 (116.251.112.214)  28.362 ms * 119.38.212.85 (119.38.212.85)  27.916 ms 119.38.212.89 (119.38.212.89)  28.332 ms
11  * * * * *
12  * * * * *
13  * * * * *
14  * * * * *
15  * * * * *
16  * * * * *
17  * * * * *
18  * * * * *
19  * * * * *
20  * * * * *
21  * * * * *
22  * * * * *
23  * * * * *
24  * * * * *
25  * * * * *
26  * * * * *
27  * * * * *
28  * * * * *
29  * * * * *
30  * * * * *
</code></pre><p>绕过正常的路由表，直接发送到网络相连的主机</p><pre><code>[root@CentOS7-1 ~]# traceroute -r www.bai.com
traceroute to www.bai.com (39.105.137.64), 30 hops max, 60 byte packets
connect: Network is unreachable
[root@CentOS7-1 ~]# traceroute -r 192.168.1.100
traceroute to 192.168.1.100 (192.168.1.100), 30 hops max, 60 byte packets
 1  CentOS7-1 (192.168.1.100)  0.193 ms  0.004 ms  0.003 ms
</code></pre><p><a href="https://segmentfault.com/a/1190000039681414">每天学一个 Linux 命令（70）：dig</a></p><p><span class="img-wrap"><img class="lazy" src="https://segmentfault.com/img/bVbLc6v" alt="image" title="image" referrerpolicy="no-referrer"></span></p>  
</div>
            