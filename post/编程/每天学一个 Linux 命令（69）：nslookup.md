
---
title: 每天学一个 Linux 命令（69）：nslookup
categories: 
    - 编程
    - segmentfault - 频道
author: segmentfault - 频道
comments: false
date: 2021-03-21 16:40:59
thumbnail: https://segmentfault.com/a/undefined
---

<div>   
<p><strong>推荐阅读：</strong><a href="http://mp.weixin.qq.com/s?__biz=MzI0MDQ4MTM5NQ==&mid=2247510238&idx=3&sn=5136ed2456f87590747b9fa76abfb73b&chksm=e918cdc2de6f44d448fea91350d186c39f4dde6a723390c66572a315d1c8f59981194d5c8e6e&scene=21#wechat_redirect" rel="nofollow">每天学一个 Linux 命令（68）：lsof</a></p><h2>命令简介</h2><p>nslookup（name server lookup）命令用于查询域名 DNS 信息的工具。nslookup 有两种工作模式，即“交互模式”和“非交互模式”。</p><pre><code>[root@CentOS7-1 ~]# nslookup
-bash: nslookup: command not found
[root@CentOS7-1 ~]# yum install -y bind-utils
</code></pre><h2>语法格式</h2><pre><code>nslookup [-option] [name | -] [server]
</code></pre><h2>选项说明</h2><pre><code>-query=TYPE      #设置查询类型
-timeout=NUMBER  #设置等待响应的超时时间，单位秒
-sil             #不显示任何警告信息。
</code></pre><p>还有一些交互的命令，有兴趣的读者可以查看帮助信息阅读。<img alt="图片" title="图片" src="https://segmentfault.com/a/undefined" referrerpolicy="no-referrer"></p><h2>应用举例</h2><p>实例</p><pre><code>非交互式模式
[root@CentOS7-1 ~]# nslookup www.baidu.com
Server:  223.5.5.5
Address: 223.5.5.5#53
Non-authoritative answer:
www.baidu.com canonical name = www.a.shifen.com.
Name: www.a.shifen.com
Address: 36.152.44.96
Name: www.a.shifen.com
Address: 36.152.44.95
#交互式模式
[root@CentOS7-1 ~]# nslookup
> baidu.com
Server:  223.5.5.5
Address: 223.5.5.5#53
Non-authoritative answer:
Name: baidu.com
Address: 39.156.69.79
Name: baidu.com
Address: 220.181.38.148
> 163.com
Server:  223.5.5.5
Address: 223.5.5.5#53
Non-authoritative answer:
Name: 163.com
Address: 123.58.180.7
Name: 163.com
Address: 123.58.180.8
</code></pre><p>google.com 相关的信息</p><pre><code>#在您的 DNS 中查询与域名 google.com 相关的所有可用信息。
[root@CentOS7-1 ~]# nslookup -type=any google.com
Server:  223.5.5.5
Address: 223.5.5.5#53
Non-authoritative answer:
Name: google.com
Address: 93.46.8.90
google.com nameserver = ns1.google.com.
google.com nameserver = ns2.google.com.
google.com nameserver = ns4.google.com.
google.com nameserver = ns3.google.com.
Authoritative answers can be found from:
#在您的 DNS 中查询与域名 google.com 相关邮件交换服务器的信息
[root@CentOS7-1 ~]# nslookup -type=mx google.com
Server:  223.5.5.5
Address: 223.5.5.5#53
Non-authoritative answer:
google.com mail exchanger = 10 aspmx.l.google.com.
google.com mail exchanger = 50 alt4.aspmx.l.google.com.
google.com mail exchanger = 20 alt1.aspmx.l.google.com.
google.com mail exchanger = 30 alt2.aspmx.l.google.com.
google.com mail exchanger = 40 alt3.aspmx.l.google.com.
Authoritative answers can be found from:
</code></pre><p>反向查找一个地址(文中地址作了处理哈)</p><pre><code>[root@CentOS7-1 ~]# nslookup 200.208.150.3
 
Server:         103.240.22.111
Address:        103.240.22.111#53
 
Non-authoritative answer:
3.150.208.200.in-addr.arpa      name = 200.208.150.3.xmission.com.
 
Authoritative answers can be found from:
150.208.200.in-addr.arpa        nameserver = ns1.xmission.com.
150.208.200.in-addr.arpa        nameserver = ns2.xmission.com.
150.208.200.in-addr.arpa        nameserver = ns.xmission.com.
</code></pre><p><a href="http://mp.weixin.qq.com/s?__biz=MzI0MDQ4MTM5NQ==&mid=2247510011&idx=3&sn=ac31bc4049d0c97ffe7b6efb78884740&chksm=e918c2e7de6f4bf190a8eb41a7700aa22b67a3178a9e96122241c30ade2652783bdb3dc60fe9&scene=21#wechat_redirect" rel="nofollow">每天学一个 Linux 命令（66）：ss</a></p><p><a href="http://mp.weixin.qq.com/s?__biz=MzI0MDQ4MTM5NQ==&mid=2247510087&idx=3&sn=43c42eed6776a283b278d873fdb5441a&chksm=e918cd5bde6f444dfc84a5e14b650eab4d1d5eff75499df9ba15cccd1e35c9e2154ec39f0cd9&scene=21#wechat_redirect" rel="nofollow">每天学一个 Linux 命令（67）：nmap</a></p>  
</div>
            