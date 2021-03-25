
---
title: '每天学一个 Linux 命令（73）：curl'
categories: 
 - 编程
 - segmentfault
 - 频道
headimg: 'https://picsum.photos/400/300?random=6286'
author: segmentfault
comments: false
date: 2021-03-25 04:15:51
thumbnail: 'https://picsum.photos/400/300?random=6286'
---

<div>   
<h2>命令简介</h2><p>curl 命令使用 HTTP、HTTPS、FTP、FTPS、SCP、SFTP、TFTP、DICT、TELNET、LDAP或FILE支持的协议之一，将数据传输到网络服务器或从网络服务器传输数据。它非常适合在 Shell 脚本中使用。</p><p>curl 命令提供代理支持，用户身份验证，FTP 上传，HTTP 发布，SSL 连接，cookie，文件传输恢复，metalink 和其他功能。<a href="http://mp.weixin.qq.com/s?__biz=MzI0MDQ4MTM5NQ==&mid=2247502760&idx=2&sn=96f5850c8e33e93a6572602c573bad9a&chksm=e918aeb4de6f27a2a39ee24bb6c5c659a47bc8509493fdbff0e1b9f37b00726f154ee4877b7e&scene=21#wechat_redirect" rel="nofollow">非常值得一看的 Curl 用法指南</a></p><h2>语法格式</h2><pre><code>curl [options] [URL...]
</code></pre><h2>选项说明</h2><pre><code>-A  #用户代理
-b  #发送 Cookie 信息
-c  #将 Cookie 写入文件
-d  #发送 POST 请求的数据体
-e  #设置 HTTP 的标头 Referer 字段
-F  #向服务器上传文件
-G  #构造 URL 的查询字符串
-H  #添加 HTTP 请求的标头
-i  #打印服务器回应的 HTTP 标头
-I  打印服务器回应的 HEAD 标头
-k  #跳过 SSL 检测
-L  #跟随服务器的重定向
–limit-rate   #限制请求和回应的带宽
-o  #将服务器的回应保存成文件(下载文件，然后重新命名)
-O  #将服务器的回应保存成文件（下载多个文件）
-s  #不输出错误和进度信息
-S  #只输出错误信息
-u  #设置认证的用户名和密码
-v  #打印调试信息
-x  #设置请求代理
-X  #指定请求的方法
</code></pre><h2>应用举例</h2><p>打印版本信息</p><pre><code>[root@CentOS7-1 ~]# curl --version
curl 7.29.0 (x86_64-redhat-linux-gnu) libcurl/7.29.0 NSS/3.44 zlib/1.2.7 libidn/1.28 libssh2/1.8.0
Protocols: dict file ftp ftps gopher http https imap imaps ldap ldaps pop3 pop3s rtsp scp sftp smtp smtps telnet tftp 
Features: AsynchDNS GSS-Negotiate IDN IPv6 Largefile NTLM NTLM_WB SSL libz unix-sockets </code></pre><p>下载文件</p><pre><code>[root@CentOS7-1 download]# curl -O http://nginx.org/download/nginx-1.18.0.zip
  % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                 Dload  Upload   Total   Spent    Left  Speed
100 1671k  100 1671k    0     0   300k      0  0:00:05  0:00:05 --:--:--  414k
[root@CentOS7-1 download]# ll
total 1672
-rw-r--r-- 1 root root 1711619 Mar 13 09:29 nginx-1.18.0.zip
#将下载下来的文件重新改名成新的指定的文件名
[root@CentOS7-1 download]# curl -o $(date +%F)_download_nginx  http://nginx.org/download/nginx-1.18.0.zip
  % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                 Dload  Upload   Total   Spent    Left  Speed
100 1671k  100 1671k    0     0   480k      0  0:00:03  0:00:03 --:--:--  480k
[root@CentOS7-1 download]# ll
total 5016
-rw-r--r-- 1 root root 1711619 Mar 13 09:31 2021-03-13_download_nginx
-rw-r--r-- 1 root root 1711619 Mar 13 09:30 F_download_nginx
-rw-r--r-- 1 root root 1711619 Mar 13 09:29 nginx-1.18.0.zip
</code></pre><p>POST请求举例</p><pre><code>[root@CentOS7-1 ~]# curl http://192.168.1.199
this is a www web stie
#显示全部信息
[root@CentOS7-1 ~]# curl -i http://192.168.1.199
HTTP/1.1 200 OK
Date: Wed, 10 Mar 2021 17:05:04 GMT
Server: Apache/2.4.6 (CentOS)
Last-Modified: Wed, 10 Mar 2021 17:03:20 GMT
ETag: "17-5bd31a4e35769"
Accept-Ranges: bytes
Content-Length: 23
Content-Type: text/html; charset=UTF-8
this is a www web stie
#只显示头部信息
[root@CentOS7-1 ~]# curl -l http://192.168.1.199
this is a www web stie
#显示get请求全过程解析信息
[root@CentOS7-1 ~]# curl -v http://192.168.1.199
* About to connect() to 192.168.1.199 port 80 (#0)
*   Trying 192.168.1.199...
* Connected to 192.168.1.199 (192.168.1.199) port 80 (#0)
> GET / HTTP/1.1
> User-Agent: curl/7.29.0
> Host: 192.168.1.199
> Accept: */*
> 
< HTTP/1.1 200 OK
< Date: Wed, 10 Mar 2021 17:05:16 GMT
< Server: Apache/2.4.6 (CentOS)
< Last-Modified: Wed, 10 Mar 2021 17:03:20 GMT
< ETag: "17-5bd31a4e35769"
< Accept-Ranges: bytes
< Content-Length: 23
< Content-Type: text/html; charset=UTF-8
< 
this is a www web stie
* Connection #0 to host 192.168.1.199 left intact
</code></pre><p>登录服务器</p><pre><code>[root@CentOS7-1 ~]# curl -u mingongge:passwdPassWd  https://github.com/mingongge/
[root@CentOS7-1 ~]# curl -u mingongge  https://github.com/mingongge/
Enter host password for user 'mingongge':
</code></pre><p>上传文件（如上传文件到文件服务器）</p><pre><code>[root@CentOS7-1 ~]# curl -T user1.png ftp://username:password@ip:port/www/web/user_download/
</code></pre><p>打印下载进度条</p><pre><code>[root@CentOS7-1 ~]# curl -# -O http://nginx.org/download/nginx-1.18.0.zip
######################################################################## 100.0%
</code></pre><p><a href="http://mp.weixin.qq.com/s?__biz=MzI0MDQ4MTM5NQ==&mid=2247510344&idx=2&sn=5e160968cac5e504cd858de1396b01ca&chksm=e918cc54de6f4542080756783030918c2a44fc47d04d8e63abe4f83ce96a3de10cdfdfac87c1&scene=21#wechat_redirect" rel="nofollow">每天学一个 Linux 命令（71）：traceroute</a></p><p><a href="http://mp.weixin.qq.com/s?__biz=MzI0MDQ4MTM5NQ==&mid=2247510418&idx=2&sn=fea17a63f12102aa0b685f03fcc232b9&chksm=e918cc8ede6f459863bd6c826ea0ecddb89a83a8e9f5d6f67d597b4c00a9c14abb257b312825&scene=21#wechat_redirect" rel="nofollow">每天学一个 Linux 命令（72）：tcpdump</a></p>  
</div>
            