
---
title: '【日志分析】Linux日志分析'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/ad3a8a052cda42658652406aa96a4778~tplv-k3u1fbpfcp-zoom-1.image'
author: 掘金
comments: false
date: Sun, 04 Jul 2021 23:52:48 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/ad3a8a052cda42658652406aa96a4778~tplv-k3u1fbpfcp-zoom-1.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h1 data-id="heading-0">0x00 前言</h1>
<p>Linux系统拥有非常灵活和强大的日志功能，可以保存几乎所有的操作记录，并可以从中检索出我们需要的信息。 本文简介一下Linux系统日志及日志分析技巧。</p>
<h1 data-id="heading-1">0x01 日志简介</h1>
<p>日志默认存放位置：/var/log/</p>
<p>查看日志配置情况：more /etc/rsyslog.conf</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/ad3a8a052cda42658652406aa96a4778~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>比较重要的几个日志： 登录失败记录：/var/log/btmp //lastb 最后一次登录：/var/log/lastlog //lastlog 登录成功记录: /var/log/wtmp //last 登录日志记录：/var/log/secure</p>
<p>目前登录用户信息：/var/run/utmp //w、who、users</p>
<p>历史命令记录：history ​ 仅清理当前用户： history -c</p>
<h1 data-id="heading-2">0x02 日志分析技巧</h1>
<h1 data-id="heading-3">A、常用的shell命令</h1>
<p>Linux下常用的shell命令如：find、grep 、egrep、awk、sed</p>
<p>小技巧：</p>
<p>1、grep显示前后几行信息:</p>
<pre><code class="copyable">​标准unix/linux下的grep通过下面參数控制上下文：
​grep -C 5 foo file 显示file文件里匹配foo字串那行以及上下5行
​grep -B 5 foo file 显示foo及前5行
​grep -A 5 foo file 显示foo及后5行
​查看grep版本号的方法是
​grep -V
<span class="copy-code-btn">复制代码</span></code></pre>
<p>2、grep 查找含有某字符串的所有文件</p>
<pre><code class="copyable">grep -rn "hello,world!" 
* : 表示当前目录所有文件，也可以是某个文件名
-r 是递归查找
-n 是显示行号
-R 查找所有文件包含子目录
-i 忽略大小写
<span class="copy-code-btn">复制代码</span></code></pre>
<p>3、如何显示一个文件的某几行：</p>
<pre><code class="copyable">cat input_file | tail -n +1000 | head -n 2000
#从第1000行开始，显示2000行。即显示1000~2999行
<span class="copy-code-btn">复制代码</span></code></pre>
<p>4、find /etc -name init</p>
<pre><code class="copyable">//在目录/etc中查找文件init
<span class="copy-code-btn">复制代码</span></code></pre>
<p>5、只是显示/etc/passwd的账户</p>
<pre><code class="copyable">`cat /etc/passwd |awk  -F ':'  '&#123;print $1&#125;'`  
//awk -F指定域分隔符为':'，将记录按指定的域分隔符划分域，填充域，​$0则表示所有域,$1表示第一个域,​$n表示第n个域。
<span class="copy-code-btn">复制代码</span></code></pre>
<p>6、sed -i '153,$d' .bash_history</p>
<pre><code class="copyable">删除历史操作记录，只保留前153行
<span class="copy-code-btn">复制代码</span></code></pre>
<h1 data-id="heading-4">B、日志分析技巧</h1>
<p><strong>A、/var/log/secure</strong></p>
<pre><code class="copyable">1、定位有多少IP在爆破主机的root帐号：    
grep "Failed password for root" /var/log/secure | awk '&#123;print $11&#125;' | sort | uniq -c | sort -nr | more

定位有哪些IP在爆破：
grep "Failed password" /var/log/secure|grep -E -o "(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)"|uniq -c

爆破用户名字典是什么？
 grep "Failed password" /var/log/secure|perl -e 'while($_=<>)&#123; /for(.*?) from/; print "$1\n";&#125;'|uniq -c|sort -nr
 
2、登录成功的IP有哪些： 
grep "Accepted " /var/log/secure | awk '&#123;print $11&#125;' | sort | uniq -c | sort -nr | more

登录成功的日期、用户名、IP：
grep "Accepted " /var/log/secure | awk '&#123;print $1,$2,$3,$9,$11&#125;' 

3、增加一个用户kali日志：
Jul 10 00:12:15 localhost useradd[2382]: new group: name=kali, GID=1001
Jul 10 00:12:15 localhost useradd[2382]: new user: name=kali, UID=1001, GID=1001, home=/home/kali
, shell=/bin/bash
Jul 10 00:12:58 localhost passwd: pam_unix(passwd:chauthtok): password changed for kali
#grep "useradd" /var/log/secure 

4、删除用户kali日志：
Jul 10 00:14:17 localhost userdel[2393]: delete user 'kali'
Jul 10 00:14:17 localhost userdel[2393]: removed group 'kali' owned by 'kali'
Jul 10 00:14:17 localhost userdel[2393]: removed shadow group 'kali' owned by 'kali'
# grep "userdel" /var/log/secure

5、su切换用户：
Jul 10 00:38:13 localhost su: pam_unix(su-l:session): session opened for user good by root(uid=0)

sudo授权执行:
sudo -l
Jul 10 00:43:09 localhost sudo:    good : TTY=pts/4 ; PWD=/home/good ; USER=root ; COMMAND=/sbin/shutdown -r now
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>2、/var/log/yum.log</strong></p>
<p>软件安装升级卸载日志：</p>
<pre><code class="copyable">yum install gcc

[root@bogon ~]# more /var/log/yum.log

Jul 10 00:18:23 Updated: cpp-4.8.5-28.el7_5.1.x86_64
Jul 10 00:18:24 Updated: libgcc-4.8.5-28.el7_5.1.x86_64
Jul 10 00:18:24 Updated: libgomp-4.8.5-28.el7_5.1.x86_64
Jul 10 00:18:28 Updated: gcc-4.8.5-28.el7_5.1.x86_64
Jul 10 00:18:28 Updated: libgcc-4.8.5-28.el7_5.1.i686
<span class="copy-code-btn">复制代码</span></code></pre></div>  
</div>
            