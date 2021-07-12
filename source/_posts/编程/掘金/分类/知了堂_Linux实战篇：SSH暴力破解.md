
---
title: '知了堂_Linux实战篇：SSH暴力破解'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/31b7676447f540419478eda4e44c9d92~tplv-k3u1fbpfcp-zoom-1.image'
author: 掘金
comments: false
date: Mon, 12 Jul 2021 00:21:46 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/31b7676447f540419478eda4e44c9d92~tplv-k3u1fbpfcp-zoom-1.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h1 data-id="heading-0">0x00 前言</h1>
<p>SSH 是目前较可靠，专为远程登录会话和其他网络服务提供安全性的协议，主要用于给远程登录会话数据进行加密，保证数据传输的安全。SSH口令长度太短或者复杂度不够，如仅包含数字，或仅包含字母等，容易被攻击者破解，一旦被攻击者获取，可用来直接登录系统，控制服务器所有权限。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/31b7676447f540419478eda4e44c9d92~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<h1 data-id="heading-1">0x01 应急场景</h1>
<p>某天，网站管理员登录服务器进行巡检时，发现端口连接里存在两条可疑的连接记录，如下图：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/56f3551ad62742969ec7a3e7f5d44e41~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<ol>
<li>TCP初始化连接三次握手吧：发SYN包，然后返回SYN/ACK包，再发ACK包，连接正式建立。但是这里有点出入，当请求者收到SYS/ACK包后，就开始建立连接了，而被请求者第三次握手结束后才建立连接。</li>
<li>客户端TCP状态迁移：<br>
CLOSED->SYN_SENT->ESTABLISHED->FIN_WAIT_1->FIN_WAIT_2->TIME_WAIT->CLOSED<br>
服务器TCP状态迁移：<br>
CLOSED->LISTEN->SYN recv->ESTABLISHED->CLOSE_WAIT->LAST_ACK->CLOSED</li>
<li>当客户端开始连接时，服务器还处于LISTENING，客户端发一个SYN包后，服务端接收到了客户端的SYN并且发送了ACK时，服务器处于SYN_RECV状态，然后并没有再次收到客户端的ACK进入ESTABLISHED状态，一直停留在SYN_RECV状态。<br>
在这里，SSH（22）端口，两条外网IP的SYN_RECV状态连接，直觉告诉了管理员，这里一定有什么异常。</li>
</ol>
<h1 data-id="heading-2">0x02 日志分析</h1>
<p>SSH端口异常，我们首先有必要先来了解一下系统账号情况：</p>
<p><strong>A、系统账号情况</strong></p>
<pre><code class="copyable">1、除root之外，是否还有其它特权用户(uid 为0)
[root@localhost ~]# awk -F: '$3==0&#123;print $1&#125;' /etc/passwd
root

2、可以远程登录的帐号信息
[root@localhost ~]# awk '/\$1|\$6/&#123;print $1&#125;' /etc/shadow
root:$6$38cKfZDjsTiUe58V$FP.UHWMObqeUQS1Z2KRj/4EEcOPi.6d1XmKHgK3j3GY9EGvwwBei7nUbbqJC./qK12HN8jFuXOfEYIKLID6hq0::0:99999:7:::
<span class="copy-code-btn">复制代码</span></code></pre>
<p>我们可以确认目前系统只有一个管理用户root。</p>
<p>接下来，我们想到的是/var/log/secure，这个日志文件记录了验证和授权方面的信息，只要涉及账号和密码的程序都会记录下来。</p>
<p><strong>B、确认攻击情况：</strong></p>
<pre><code class="copyable">1、统计了下日志，发现大约有126254次登录失败的记录，确认服务器遭受暴力破解
[root@localhost ~]# grep -o "Failed password" /var/log/secure|uniq -c
     126254 Failed password
     
2、输出登录爆破的第一行和最后一行，确认爆破时间范围：
[root@localhost ~]# grep "Failed password" /var/log/secure|head -1
Jul  8 20:14:59 localhost sshd[14323]: Failed password for invalid user qwe from 111.13.xxx.xxx port 1503 ssh2
[root@localhost ~]# grep "Failed password" /var/log/secure|tail -1
Jul 10 12:37:21 localhost sshd[2654]: Failed password for root from 111.13.xxx.xxx port 13068 ssh2

3、进一步定位有哪些IP在爆破？
[root@localhost ~]# grep "Failed password" /var/log/secure|grep -E -o "(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)"|uniq -c | sort -nr 
    12622 23.91.xxx.xxx
     8942 114.104.xxx.xxx
     8122 111.13.xxx.xxx
     7525 123.59.xxx.xxx
     ...................
    
4、爆破用户名字典都有哪些？
[root@localhost ~]# grep "Failed password" /var/log/secure|perl -e 'while($_=<>)&#123; /for(.*?) from/; print "$1\n";&#125;'|uniq -c|sort -nr
      9402  root
      3265  invalid user oracle
      1245  invalid user admin
      1025  invalid user user
      .....................
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>C、管理员最近登录情况：</strong></p>
<pre><code class="copyable">1、登录成功的日期、用户名、IP：
[root@localhost ~]# grep "Accepted " /var/log/secure | awk '&#123;print $1,$2,$3,$9,$11&#125;' 
Jul 9 09:38:09 root 192.168.143.100
Jul 9 14:55:51 root 192.168.143.100
Jul 10 08:54:26 root 192.168.143.100
Jul 10 16:25:59 root 192.168.143.100
............................
通过登录日志分析，并未发现异常登录时间和登录IP。

2、顺便统计一下登录成功的IP有哪些：
[root@localhost ~]# grep "Accepted " /var/log/secure | awk '&#123;print $11&#125;' | sort | uniq -c | sort -nr | more
     27 192.168.204.1
<span class="copy-code-btn">复制代码</span></code></pre>
<p>通过日志分析，发现攻击者使用了大量的用户名进行暴力破解，但从近段时间的系统管理员登录记录来看，并未发现异常登录的情况，需要进一步对网站服务器进行入侵排查，这里就不再阐述。</p>
<h1 data-id="heading-3">0x04 处理措施</h1>
<p>SSH暴力破解依然十分普遍，如何保护服务器不受暴力破解攻击，总结了几种措施：</p>
<pre><code class="copyable">1、禁止向公网开放管理端口，若必须开放应限定管理IP地址并加强口令安全审计（口令长度不低于8位，由数字、大小写字母、特殊字符等至少两种以上组合构成）。
2、更改服务器ssh默认端口。
3、部署入侵检测设备，增强安全防护。
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>知了姐今天先分享到这儿了，明天为大家分享《第2篇：捕捉短连接》</strong></p></div>  
</div>
            