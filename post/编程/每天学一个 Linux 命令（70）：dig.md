
---
title: 每天学一个 Linux 命令（70）：dig
categories: 
    - 编程
    - segmentfault - 频道
author: segmentfault - 频道
comments: false
date: 2021-03-21 16:40:59
thumbnail: https://segmentfault.com/img/bVbLc6v
---

<div>   
<p><strong>推荐阅读：</strong><a href="http://mp.weixin.qq.com/s?__biz=MzI0MDQ4MTM5NQ==&mid=2247510273&idx=2&sn=8a91565cf517d8630bb4d5aadad2ba8f&chksm=e918cc1dde6f450bfe93a212ae027356054f101b60cd15ab76736bda1a769eb8e65496b532cb&scene=21#wechat_redirect" rel="nofollow">每天学一个 Linux 命令（69）：nslookup</a></p><h2>命令简介</h2><p>dig 命令用于执行网络 DNS 查找。dig 是一个用于查询 DNS 名称服务器的灵活工具。它执行DNS查找并显示从查询的名称服务器返回的答案。</p><p>可使用 dig 来解决 DNS 问题，它具有灵活性，易用性和输出清晰度。相比其它工具功能更多、更强大。</p><h2>语法格式</h2><pre><code>dig [@server] [-b address] [-c class] [-f filename] [-k filename]
    [-m] [-p port#] [-q name] [-t type] [-x addr] [-y [hmac:]name:ke
</code></pre><h2>选项说明</h2><pre><code>@<服务器地址>   #指定进行域名解析的域名服务器
-b    #指定使用本机的哪个IP地址向域名服务器发送域名查询请求
-f<文件名称>   #指定dig以批处理的方式运行
-P  #指定域名服务器所使用端口号
-t<类型>  #指定要查询的DNS数据类型
-x  #执行逆向域名查询
-4  #使用IPv4
-6  #使用IPv6
-h  #显示帮助信息
</code></pre><h2>应用举例</h2><p>实例</p><pre><code>[root@CentOS7-1 ~]# dig www.baidu.com
; <<>> DiG 9.11.4-P2-RedHat-9.11.4-26.P2.el7_9.4 <<>> www.baidu.com
;; global options: +cmd
;; Got answer:
;; ->>HEADER<<- opcode: QUERY, status: NOERROR, id: 57747
;; flags: qr rd ra; QUERY: 1, ANSWER: 3, AUTHORITY: 0, ADDITIONAL: 0
;; QUESTION SECTION:
;www.baidu.com.   IN A
;; ANSWER SECTION:
www.baidu.com.  224 IN CNAME www.a.shifen.com.
www.a.shifen.com. 224 IN A 36.152.44.95
www.a.shifen.com. 224 IN A 36.152.44.96
;; Query time: 27 msec
;; SERVER: 223.5.5.5#53(223.5.5.5)
;; WHEN: Sat Mar 13 07:51:28 EST 2021
;; MSG SIZE  rcvd: 90
</code></pre><p>逆向查询</p><pre><code>[root@CentOS7-1 ~]# dig -x wwww.baidu.com
; <<>> DiG 9.11.4-P2-RedHat-9.11.4-26.P2.el7_9.4 <<>> -x wwww.baidu.com
;; global options: +cmd
;; Got answer:
;; ->>HEADER<<- opcode: QUERY, status: NXDOMAIN, id: 7825
;; flags: qr rd ra; QUERY: 1, ANSWER: 0, AUTHORITY: 1, ADDITIONAL: 0
;; QUESTION SECTION:
;com.baidu.wwww.in-addr.arpa. IN PTR
;; AUTHORITY SECTION:
in-addr.arpa.  600 IN SOA b.in-addr-servers.arpa. nstld.iana.org. 2021031279 1800 900 604800 3600
;; Query time: 151 msec
;; SERVER: 223.5.5.5#53(223.5.5.5)
;; WHEN: Sat Mar 13 07:52:54 EST 2021
;; MSG SIZE  rcvd: 113
</code></pre><p>向指定的DNS服务器查询</p><pre><code>[root@CentOS7-1 ~]# dig @8.8.8.8 baidu.com
; <<>> DiG 9.11.4-P2-RedHat-9.11.4-26.P2.el7_9.4 <<>> @8.8.8.8 baidu.com
; (1 server found)
;; global options: +cmd
;; Got answer:
;; ->>HEADER<<- opcode: QUERY, status: NOERROR, id: 20803
;; flags: qr rd ra; QUERY: 1, ANSWER: 2, AUTHORITY: 0, ADDITIONAL: 0
;; QUESTION SECTION:
;baidu.com.   IN A
;; ANSWER SECTION:
baidu.com.  329 IN A 39.156.69.79
baidu.com.  329 IN A 220.181.38.148
;; Query time: 4 msec
;; SERVER: 8.8.8.8#53(8.8.8.8)
;; WHEN: Sat Mar 13 07:55:26 EST 2021
;; MSG SIZE  rcvd: 59
</code></pre><p>一次查询多少域名，将域名写入文件，然后从文件读取信息。</p><pre><code>[root@CentOS7-1 ~]# cat domain_names_file
www.baidu.com
mail.163.com
www.qq.com
www.aliyun.com
www.amazon.com
[root@CentOS7-1 ~]# dig +noall +answer -f domain_names_file
www.baidu.com.  70 IN CNAME www.a.shifen.com.
www.a.shifen.com. 70 IN A 36.152.44.95
www.a.shifen.com. 70 IN A 36.152.44.96
mail.163.com.  117 IN CNAME ntes53.mail.163.com.
ntes53.mail.163.com. 117 IN A 123.126.97.202
www.qq.com.  71 IN CNAME ins-r23tsuuf.ias.tencent-cloud.net.
ins-r23tsuuf.ias.tencent-cloud.net. 71 IN A 183.194.238.19
ins-r23tsuuf.ias.tencent-cloud.net. 71 IN A 183.194.238.117
www.aliyun.com.  44 IN CNAME www-jp-de-intl-adns.aliyun.com.
www-jp-de-intl-adns.aliyun.com. 44 IN CNAME www-jp-de-intl-adns.aliyun.com.gds.alibabadns.com.
www-jp-de-intl-adns.aliyun.com.gds.alibabadns.com. 44 IN CNAME sh.wagbridge.aliyun.aliyun.com.
sh.wagbridge.aliyun.aliyun.com. 44 IN CNAME aliyun-adns.aliyun.com.
aliyun-adns.aliyun.com. 44 IN CNAME aliyun-adns.aliyun.com.gds.alibabadns.com.
aliyun-adns.aliyun.com.gds.alibabadns.com. 44 IN A 106.11.248.144
www.amazon.com.  15 IN CNAME tp.47cf2c8c9-frontier.amazon.com.
tp.47cf2c8c9-frontier.amazon.com. 15 IN CNAME d3ag4hukkh62yn.cloudfront.net.
d3ag4hukkh62yn.cloudfront.net. 15 IN A 13.225.100.223
#+noall（不显示所有内容）和 +answer（仅显示域名服务器的响应内容）
#不使用任何参数，对比一下输出的结果
[root@CentOS7-1 ~]# dig -f domain_names_file
; <<>> DiG 9.11.4-P2-RedHat-9.11.4-26.P2.el7_9.4 <<>> www.baidu.com
;; global options: +cmd
;; Got answer:
;; ->>HEADER<<- opcode: QUERY, status: NOERROR, id: 2834
;; flags: qr rd ra; QUERY: 1, ANSWER: 3, AUTHORITY: 0, ADDITIONAL: 0
;; QUESTION SECTION:
;www.baidu.com.   IN A
;; ANSWER SECTION:
www.baidu.com.  86 IN CNAME www.a.shifen.com.
www.a.shifen.com. 86 IN A 36.152.44.95
www.a.shifen.com. 86 IN A 36.152.44.96
;; Query time: 23 msec
;; SERVER: 223.5.5.5#53(223.5.5.5)
;; WHEN: Sat Mar 13 08:02:46 EST 2021
;; MSG SIZE  rcvd: 90
; <<>> DiG 9.11.4-P2-RedHat-9.11.4-26.P2.el7_9.4 <<>> mail.163.com
;; Got answer:
;; ->>HEADER<<- opcode: QUERY, status: NOERROR, id: 39346
;; flags: qr rd ra; QUERY: 1, ANSWER: 2, AUTHORITY: 0, ADDITIONAL: 0
;; QUESTION SECTION:
;mail.163.com.   IN A
;; ANSWER SECTION:
mail.163.com.  36 IN CNAME ntes53.mail.163.com.
ntes53.mail.163.com. 36 IN A 123.126.97.202
;; Query time: 19 msec
;; SERVER: 223.5.5.5#53(223.5.5.5)
;; WHEN: Sat Mar 13 08:02:46 EST 2021
;; MSG SIZE  rcvd: 67
; <<>> DiG 9.11.4-P2-RedHat-9.11.4-26.P2.el7_9.4 <<>> www.qq.com
;; Got answer:
;; ->>HEADER<<- opcode: QUERY, status: NOERROR, id: 51368
;; flags: qr rd ra; QUERY: 1, ANSWER: 3, AUTHORITY: 0, ADDITIONAL: 0
;; QUESTION SECTION:
;www.qq.com.   IN A
;; ANSWER SECTION:
www.qq.com.  78 IN CNAME ins-r23tsuuf.ias.tencent-cloud.net.
ins-r23tsuuf.ias.tencent-cloud.net. 78 IN A 183.194.238.19
ins-r23tsuuf.ias.tencent-cloud.net. 78 IN A 183.194.238.117
;; Query time: 22 msec
;; SERVER: 223.5.5.5#53(223.5.5.5)
;; WHEN: Sat Mar 13 08:02:46 EST 2021
;; MSG SIZE  rcvd: 108
; <<>> DiG 9.11.4-P2-RedHat-9.11.4-26.P2.el7_9.4 <<>> www.aliyun.com
;; Got answer:
;; ->>HEADER<<- opcode: QUERY, status: NOERROR, id: 5856
;; flags: qr rd ra; QUERY: 1, ANSWER: 6, AUTHORITY: 0, ADDITIONAL: 0
;; QUESTION SECTION:
;www.aliyun.com.   IN A
;; ANSWER SECTION:
www.aliyun.com.  22 IN CNAME www-jp-de-intl-adns.aliyun.com.
www-jp-de-intl-adns.aliyun.com. 22 IN CNAME www-jp-de-intl-adns.aliyun.com.gds.alibabadns.com.
www-jp-de-intl-adns.aliyun.com.gds.alibabadns.com. 22 IN CNAME sh.wagbridge.aliyun.aliyun.com.
sh.wagbridge.aliyun.aliyun.com. 22 IN CNAME aliyun-adns.aliyun.com.
aliyun-adns.aliyun.com. 22 IN CNAME aliyun-adns.aliyun.com.gds.alibabadns.com.
aliyun-adns.aliyun.com.gds.alibabadns.com. 22 IN A 106.11.172.51
;; Query time: 23 msec
;; SERVER: 223.5.5.5#53(223.5.5.5)
;; WHEN: Sat Mar 13 08:02:46 EST 2021
;; MSG SIZE  rcvd: 228
; <<>> DiG 9.11.4-P2-RedHat-9.11.4-26.P2.el7_9.4 <<>> www.amazon.com
;; Got answer:
;; ->>HEADER<<- opcode: QUERY, status: NOERROR, id: 36379
;; flags: qr rd ra; QUERY: 1, ANSWER: 4, AUTHORITY: 0, ADDITIONAL: 0
;; QUESTION SECTION:
;www.amazon.com.   IN A
;; ANSWER SECTION:
www.amazon.com.  26 IN CNAME tp.47cf2c8c9-frontier.amazon.com.
tp.47cf2c8c9-frontier.amazon.com. 26 IN CNAME www.amazon.com.edgekey.net.
www.amazon.com.edgekey.net. 26 IN CNAME e15316.e22.akamaiedge.net.
e15316.e22.akamaiedge.net. 26 IN A 223.119.142.58
;; Query time: 22 msec
;; SERVER: 223.5.5.5#53(223.5.5.5)
;; WHEN: Sat Mar 13 08:02:46 EST 2021
;; MSG SIZE  rcvd: 160</code></pre><p><span class="img-wrap"><img class="lazy" src="https://segmentfault.com/img/bVbLc6v" alt="image" title="image" referrerpolicy="no-referrer"></span></p>  
</div>
            