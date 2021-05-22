
---
title: '五分钟教学妹学会redis实战-这篇文章让我轻松拿下阿里offer，建议收藏'
categories: 
 - 编程
 - 掘金
 - 标签
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/20482891a8d14e6f98b18c7a1a757d17~tplv-k3u1fbpfcp-zoom-1.image'
author: 掘金
comments: false
date: Sat, 22 May 2021 02:03:32 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/20482891a8d14e6f98b18c7a1a757d17~tplv-k3u1fbpfcp-zoom-1.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p><strong>注：</strong></p>
<p>正在找工作的小伙伴可以看我的《<a href="https://blog.csdn.net/xinshuzhan/category_9553853.html?spm=1001.2014.3001.5482" target="_blank" rel="nofollow noopener noreferrer">运维面试宝典专栏</a>》（持续更新中）</p>
<p>对职业发展比较困惑的小伙伴可以看 《<a href="https://blog.csdn.net/xinshuzhan/category_9446052.html?spm=1001.2014.3001.5482" target="_blank" rel="nofollow noopener noreferrer">IT学子成长指南</a>》（更新中）</p>
<p>想要系统学习云计算运维的小伙伴可以看《<a href="https://blog.csdn.net/xinshuzhan/article/details/116108930?spm=1001.2014.3001.5502" target="_blank" rel="nofollow noopener noreferrer">循序渐进学运维专栏</a>》 （持续更新中）</p>
<p>想要改变思维打造自己的副业的小伙伴可以看《<a href="https://blog.csdn.net/xinshuzhan/category_10484268.html?spm=1001.2014.3001.5482" target="_blank" rel="nofollow noopener noreferrer">年薪300W的随笔</a>》 （持续更新中）</p>
<h2 data-id="heading-0">作者简介</h2>
<p>作者名： 互联网老辛</p>
<p>简介： CSDN博客专家，一线互联网从业人员，架构师，云计算运维讲师，互联网连续创业者，从16年开始做直播教学，几年来，陆续帮助近3000+小伙伴高薪就业。欢迎各位小伙伴加我咨询相关问题，带你走出迷茫；</p>
<p><strong>座右铭： 我不认为自己是最优秀的，但我可以是最努力的</strong></p>
<h2 data-id="heading-1">正文</h2>
<h3 data-id="heading-2">redis概述和安装Redis</h3>
<h4 data-id="heading-3">1. redis的介绍</h4>
<p>Redis 是完全开源的，遵守 BSD 协议，是一个高性能的 key-value 数据库。</p>
<p>Redis 与其他 key - value 缓存产品有以下三个特点：</p>
<ul>
<li>Redis支持数据的持久化，可以将内存中的数据保存在磁盘中，重启的时候可以再次加载进行使用。</li>
<li>Redis不仅仅支持简单的key-value类型的数据，同时还提供list，set，zset，hash等数据结构的存储。</li>
<li>Redis支持数据的备份，即master-slave模式的数据备份。</li>
</ul>
<p>目前官网上推荐下载的版本是：6.2.3</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/20482891a8d14e6f98b18c7a1a757d17~tplv-k3u1fbpfcp-zoom-1.image" alt="在这里插入图片描述" loading="lazy" referrerpolicy="no-referrer"></p>
<h4 data-id="heading-4">2 .redis 能够支持的数据类型</h4>
<p>支持存储的数据类型有：
String（字符串，包含整数）,
List（列表）,
Hash（关联数组）,
Sets（集合）,
Sorted Sets（有序集合）
Bitmaps（位图）, HyperLoglog。</p>
<h4 data-id="heading-5">3. redis性能评估</h4>
<ul>
<li>100万较小的键存储字符串，大概消耗100M内存</li>
<li>由于Redis是单线程，如果服务器主机上有多个CPU，只有一个能够使用，但并不意味着CPU会成为瓶颈，因为Redis是一个比较简单的K-V数据存储，CPU通常不会成为瓶颈的</li>
<li>在常见的linux服务器上，500K（50万）的并发，只需要一秒钟处理，如果主机硬件较好的情况下，每秒钟可以达到上百万的并发</li>
</ul>
<p><strong>面试题： redis和memcache的区别</strong>
关于reids和memcache的区别，我在专栏《运维面试宝典》里有些可以跳转阅读。</p>
<p>这里可以列举两条：</p>
<ul>
<li>(1）【持久化能力】Redis支持持久化，memcache也支持但一般不做持久化（重启丢失数据）</li>
<li>（2）【数据类型支持】Redis类型较多（5种数据类型，string、list、hash、set、sorted set），memcache只能是字符串</li>
</ul>
<h4 data-id="heading-6">4. 安装redis</h4>
<ol>
<li>在安装Remi repository源时，需要依赖epel源，因此先安装epel源</li>
</ol>
<pre><code class="hljs language-bash copyable" lang="bash">[root@itlaoxin17 ~]<span class="hljs-comment"># yum -y install epel-release</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<ol start="2">
<li>安装remi repository源</li>
</ol>
<pre><code class="hljs language-bash copyable" lang="bash">[root@itlaoxin~]<span class="hljs-comment"># yum -y install http://rpms.remirepo.net/enterprise/remi-release-7.rpm</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<ol start="3">
<li>使用remi repository源安装Redis</li>
</ol>
<pre><code class="hljs language-cpp copyable" lang="cpp">[root@itlaoxin ~]<span class="hljs-meta"># yum --enablerepo=remi install -y redis#选用remi源进行安装redis</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<ol start="4">
<li>启动Redis</li>
</ol>
<pre><code class="hljs language-bash copyable" lang="bash">[root@itlaoxin ~]<span class="hljs-comment"># systemctl start redis </span>
[root@itlaoxin-17 ~]<span class="hljs-comment"># netstat  -antup | grep redis</span>
tcp        0      0 127.0.0.1:6379          0.0.0.0:*               LISTEN      68199/redis-server  
tcp6       0      0 ::1:6379                :::*                    LISTEN      68199/redis-server  
注：redis默认监听6379端口

<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-7">redis基本操作</h2>
<h3 data-id="heading-8">基本操作</h3>
<pre><code class="hljs language-bash copyable" lang="bash">[root@itlaoxin ~]<span class="hljs-comment"># redis-cli </span>
选项：
-h <hostname> 指定主机IP  
-p <port>指定端口socket文件进行通信。
[root@itlaoxin ~]<span class="hljs-comment"># redis-cli -h 127.0.0.1#连接redis，默认不启用密码认证。</span>
127.0.0.1:6379> <span class="hljs-built_in">exit</span> <span class="hljs-comment">#退出连接。</span>
或：
[root@itlaoxin ~]<span class="hljs-comment"># redis-cli #使用redis-cli直接连接，默认连接是127.0.0.1 IP。</span>

<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-9">举例1：设置键system的值为centos</h3>
<pre><code class="hljs language-bash copyable" lang="bash">
[root@itlaoxin ~]<span class="hljs-comment">#  redis-cli -h 127.0.0.1</span>
127.0.0.1:6379> <span class="hljs-built_in">set</span> system centos   <span class="hljs-comment">#set用于创建键值</span>
OK
127.0.0.1:6379> get system   <span class="hljs-comment">#get 后加键，可以查看键中的值</span>
<span class="hljs-string">"centos"</span>

<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-10">举例2： 定义一个键name值为zhangsan，并设置过期时间为60秒。</h3>
<pre><code class="hljs language-bash copyable" lang="bash">
127.0.0.1:6379> <span class="hljs-built_in">set</span> name itlaoxin EX 60
OK
127.0.0.1:6379> get name
<span class="hljs-string">"itlaoxin"</span>

<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-11">举例3，开启redis用户认证服务</h3>
<pre><code class="hljs language-bash copyable" lang="bash">[root@itlaoxin ~]<span class="hljs-comment"># vim /etc/redis.conf</span>
改：901  <span class="hljs-comment"># requirepass foobared#启用此项，并指定密码即可。</span>
为：901requirepass jfvip123<span class="hljs-comment">#指定密码为jfvip123</span>
[root@itlaoxin ~]<span class="hljs-comment"># systemctl restart redis  #重启服务</span>
[root@itlaoxin ~]<span class="hljs-comment"># iptables -F   #关闭防火墙</span>

测试用户认证功能：
[root@itlaoxin ~]<span class="hljs-comment"># redis-cli    #登陆测试</span>
127.0.0.1:6379> get system    
(error) NOAUTH Authentication required.    <span class="hljs-comment">#发现报错， 需要用户密码认证</span>
127.0.0.1:6379> auth jfvip123 <span class="hljs-comment">#输入密码</span>
OK
127.0.0.1:6379> get system
<span class="hljs-string">"centos"</span>

<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-12">配置reids持久化</h2>
<h3 data-id="heading-13">1. redis持久化介绍</h3>
<p>redis持久化概述</p>
<p>redis持久化主要有两种 ROD和AOF，也可以把两种混合起来，从reids4.0后引入的方式。</p>
<p>RDB实现原理：
RDB类似于快照，在某个时间点，将 Redis 在内存中的数据库状态（数据库的键值对等信息）保存到磁盘里面。RDB 持久化功能生成的 RDB 文件是经过压缩的二进制文件。</p>
<p>AOF：
保存 Redis 服务器所执行的所有写操作命令来记录数据库状态，并在服务器启动时，通过重新执行这些命令来还原数据集。
AOF默认是关闭的，可以通过appendonley yes 开启
AOF 持久化功能的实现可以分为三个步骤：命令追加、文件写入、文件同步。</p>
<h3 data-id="heading-14">2. 配置文件中配置与RDB相关的参数</h3>
<pre><code class="hljs language-bash copyable" lang="bash">[root@itlaoxin ~]<span class="hljs-comment"># vim /etc/redis.conf     #默认参数就够用了</span>
235  stop-writes-on-bgsave-error yes<span class="hljs-comment">#在进行快照备份时，一旦发生错误的话是否停止。</span>
241  rdbcompression yes     <span class="hljs-comment">#RDB文件是否使用压缩，压缩会消耗CPU。</span>
250  rdbchecksum yes<span class="hljs-comment">#是否对RDB文件做校验码检测，此项定义在redis启动时加载RDB文件是否对文件检查校验码，在redis生成RDB文件是会生成校验信息，在redis再次启动或装载RDB文件时，是否检测校验信息。</span>
253  dbfilename dump.rdb <span class="hljs-comment">#定义RDB文件的名称。</span>
263  dir /var/lib/redis <span class="hljs-comment">#定义RDB文件存放的目录路径。</span>

<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-15">实战 搭建redis主从架构</h2>
<ol>
<li>原理：</li>
</ol>
<p>Redis的主从复制是自动进行的，并不需要用户的介入，slave端会自动连接master并进行数据同步。如果同步连接时slave端短暂的与master端断开了连接，那连接恢复后slave端会与master端进行一次同步。从而保证数据一致。</p>
<ol start="2">
<li>拓扑图：</li>
</ol>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/facd086634074dc3b2278efe0a0f6f7e~tplv-k3u1fbpfcp-zoom-1.image" alt="在这里插入图片描述" loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-16">配置itlaoxin17为redis主</h3>
<h4 data-id="heading-17">1. 在itlaoxin17主机上安装Redis</h4>
<pre><code class="hljs language-bash copyable" lang="bash">[root@itlaoxin-17 ~]<span class="hljs-comment"># rm -rf  /var/run/yum.pid</span>
[root@itlaoxin ~]<span class="hljs-comment"># yum -y install epel-release#安装epel源。</span>
[root@itlaoxin ~]<span class="hljs-comment"># yum -y install http://rpms.remirepo.net/enterprise/remi-release-7.rpm#安装remi源。</span>
[root@itlaoxin ~]<span class="hljs-comment"># yum --enablerepo=remi install -y redis#安装Redis。</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-18">2、修改itlaoxin17主机上的Redis配置文件</h4>
<pre><code class="hljs language-bash copyable" lang="bash">[root@itlaoxin-17 ~]<span class="hljs-comment"># vim /etc/redis.conf：</span>
改：75 <span class="hljs-built_in">bind</span> 127.0.0.1
为：75 <span class="hljs-built_in">bind</span> 0.0.0.0<span class="hljs-comment">#redis监听的地址，默认监听在127.0.0.1地址上，改为0.0.0.0地址或192.168.1.17</span>
改：507  <span class="hljs-comment"># requirepass foobared#启用此项，并指定密码即可。</span>
为：507requirepass jfxinvip123<span class="hljs-comment">#指定密码为jfxinvip123</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>重启服务</p>
<pre><code class="hljs language-bash copyable" lang="bash">[root@itlaoxin ~]<span class="hljs-comment"># systemctl restart redis  #重启服务</span>
[root@itlaoxin ~]<span class="hljs-comment"># iptables -F</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-19">3、配置itlaoxin18为redis从， 在itlaoxin18主机上安装Redis</h4>
<pre><code class="hljs language-bash copyable" lang="bash">[root@itlaoxin ~]<span class="hljs-comment"># yum -y install epel-release#安装epel源。</span>
[root@itlaoxin ~]<span class="hljs-comment"># yum -y install http://rpms.remirepo.net/enterprise/remi-release-7.rpm#安装remi源。</span>
[root@itlaoxin ~]<span class="hljs-comment"># yum --enablerepo=remi install -y redis#安装Redis。</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-20">4、修改itlaoxin18主机上的Redis配置文件</h4>
<pre><code class="hljs language-bash copyable" lang="bash">[root@itlaoxin ~]<span class="hljs-comment"># vim /etc/redis.conf#修改第286行。</span>
改： 478<span class="hljs-comment"># replicaof <masterip> <masterport>#修改此项如下。</span>
为：478  replicaof 192.168.1.17 6379
改：486 <span class="hljs-comment"># masterauth <master-password></span>
为：486  masterauth jfxinvip123   <span class="hljs-comment">#写上redis主的密码。如果redis主没有密码，这里可不写</span>
[root@itlaoxin ~]<span class="hljs-comment"># systemctl start redis#启动redis。</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-21">5、登录itlaoxin18主机上查看主从复制状态</h4>
<pre><code class="hljs language-bash copyable" lang="bash">[root@itlaoxin ~]<span class="hljs-comment"># redis-cli#登录redis。</span>

127.0.0.1:6379> info replication
<span class="hljs-comment"># Replication</span>
role:slave       <span class="hljs-comment">#角色： slave</span>
master_host:192.168.1.17  <span class="hljs-comment">#主服务器IP。</span>
master_port:6379   <span class="hljs-comment">#主服务器端口</span>
master_link_status:up    <span class="hljs-comment">##主服务器连接状态为up，说明已经主从同步上了</span>
master_last_io_seconds_ago:8
master_sync_in_progress:0
slave_repl_offset:112
slave_priority:100
slave_read_only:1          <span class="hljs-comment">#成为从服务以后，1表示该服务器为只读。</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-22">6、登录itlaoxin17主机上查看主从复制信息</h4>
<p>[</p>
<pre><code class="hljs language-bash copyable" lang="bash">root@itlaoxin ~]<span class="hljs-comment"># redis-cli#登录Redis。</span>
127.0.0.1:6379>AUTH jfxinvip123
</pre>OK
127.0.0.1:6379> info replication
<span class="hljs-comment"># Replication</span>
role:master<span class="hljs-comment">#角色：master。</span>
connected_slaves:1<span class="hljs-comment">#从服务器数量。</span>
slave0:ip=192.168.1.18,port=6379,state=online,offset=476,lag=0   <span class="hljs-comment">#从服务器信息。</span>
...
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-23">7、在itlaoxin17上验证主从复制：</h4>
<pre><code class="hljs language-bash copyable" lang="bash">登录Redis主服务，并创建一个user键。

[root@itlaoxin-17 ~]<span class="hljs-comment"># redis-cli </span>
127.0.0.1:6379> AUTH jfxinvip123
OK
127.0.0.1:6379> <span class="hljs-built_in">set</span> user itlaoxin
OK
8、登录Redis从服务，获取在主服务上创建的user键。
[root@itlaoxin ~]<span class="hljs-comment">#  redis-cli</span>
127.0.0.1:6379> get user      <span class="hljs-comment">#可以查看到键值，说明主从数据同步成功。</span>
<span class="hljs-string">"itlaoxin"</span> 
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-24">实战二： 使用sentinel实现redis集群高可用</h2>
<p>实验拓扑：
重新开启3台全新服务器，一定是全新的3台服务器，如果之前的实验环境上做，会出现配置混乱。每台服务器上分别配置redis和sentinel。其中1个master和2个slave。如下图所示：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/0f656b1504e241b5be5304f275dd6aa3~tplv-k3u1fbpfcp-zoom-1.image" alt="在这里插入图片描述" loading="lazy" referrerpolicy="no-referrer"></p>
<h4 data-id="heading-25">1、在三台机器上安装redis</h4>
<pre><code class="hljs language-bash copyable" lang="bash">[root@itlaoxin ~]<span class="hljs-comment"># yum -y install epel-release</span>
[root@itlaoxin ~]<span class="hljs-comment"># yum -y install http://rpms.remirepo.net/enterprise/remi-release-7.rpm</span>
[root@itlaoxin ~]<span class="hljs-comment"># yum --enablerepo=remi install -y redis#安装Redis</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-26">2、修改itlaoxin17主机上的Redis配置文件</h4>
<pre><code class="hljs language-bash copyable" lang="bash">[root@itlaoxin17 ~]<span class="hljs-comment"># vim /etc/redis.conf</span>
改：675 <span class="hljs-built_in">bind</span> 127.0.0.1
为：75  <span class="hljs-built_in">bind</span> 0.0.0.0<span class="hljs-comment">#redis监听的地址，改为0.0.0.0表示在所有网卡接口上进行监听 </span>
改：94 protected-mode yes  
为：94 protected-mode no   <span class="hljs-comment">#关闭允protected-mode，许外网访问redis服务器</span>
[root@itlaoxin17 ~]<span class="hljs-comment"># systemctl restart redis  #重启服务</span>
[root@itlaoxin17 ~]<span class="hljs-comment"># iptables -F</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-27">3、配置itlaoxin18/19主机为redis从服务器</h4>
<pre><code class="hljs language-bash copyable" lang="bash">[root@itlaoxin18 ~]<span class="hljs-comment"># vim /etc/redis.conf#修改第286行。</span>
改：75 <span class="hljs-built_in">bind</span> 127.0.0.1
为：75  <span class="hljs-built_in">bind</span> 0.0.0.0<span class="hljs-comment">#redis监听的地址，改为0.0.0.0表示在所有网卡接口上进行监听 </span>
改：94 protected-mode yes
为： 94 protected-mode no
改： 477 <span class="hljs-comment"># replicaof <masterip> <masterport></span>
为： 478 replicaof 192.168.1.17 6379
[root@itlaoxin18 ~]<span class="hljs-comment"># systemctl start redis#启动redis。</span>
[root@itlaoxin18 ~]<span class="hljs-comment"># iptables -F</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-28">4、登录itlaoxin19主机上查看主从复制状态</h4>
<pre><code class="hljs language-bash copyable" lang="bash">[root@itlaoxin19 ~]<span class="hljs-comment"># redis-cli#登录redis。</span>
127.0.0.1:6379> info replication
<span class="hljs-comment"># Replication</span>
role:slave               <span class="hljs-comment">#角色：slave。</span>
master_host:192.168.1.17<span class="hljs-comment">#主服务器IP。</span>
master_port:6379<span class="hljs-comment">#主服务端口。</span>
master_link_status:up<span class="hljs-comment">#主服务器连接状态为up，说明已经主从同步上了</span>
到此，1主2从的redis主从复制架构已经搭建成功，下面开始配置sentinel架构构。
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-29">5、在itlaoxin17上配置sentinel1</h4>
<pre><code class="hljs language-bash copyable" lang="bash">[root@itlaoxin17 ~]<span class="hljs-comment">#  vim /etc/redis-sentinel.conf</span>
改：17 <span class="hljs-comment"># protected-mode no</span>
为：17 protected-mode no
改：26 daemonize no
：26 daemonize yes
改：84 sentinel monitor mymaster 127.0.0.1 6379 2
为：84 sentinel monitor mymaster 192.168.1.17 6379 2

改：113 sentinel down-after-milliseconds mymaster 30000 <span class="hljs-comment">#默认单位是毫秒，配成10秒</span>
为：113 sentinel down-after-milliseconds mymaster 10000

改：146 sentinel failover-timeout mymaster 180000 
为：146 sentinel failover-timeout mymaster 60000    
如果在该时间（ms）内未能完成failover操作，则认为该failover失败
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-30">6、把redis-sentinel.conf发给itlaoxin18和itlaoxin19</h4>
<pre><code class="hljs language-bash copyable" lang="bash">[root@itlaoxin17 ~]<span class="hljs-comment"># scp  /etc/redis-sentinel.conf  192.168.1.18:/etc/redis-sentinel.conf</span>
[root@itlaoxin17 ~]<span class="hljs-comment"># scp  /etc/redis-sentinel.conf  192.168.1.19:/etc/redis-sentinel.conf</span>
11111111111111111111111111111
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-31">7、启动Redis 和sentinel服务器</h4>
<pre><code class="hljs language-bash copyable" lang="bash">[root@itlaoxin17 ~]<span class="hljs-comment">#  systemctl start redis && systemctl start redis-sentinel </span>
[root@itlaoxin18 ~]<span class="hljs-comment">#  systemctl start redis && systemctl start redis-sentinel </span>
[root@itlaoxin19 ~]<span class="hljs-comment">#  systemctl start redis && systemctl start redis-sentinel </span>
一定要关闭selinux
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-32">8. 模拟故障</h4>
<pre><code class="hljs language-bash copyable" lang="bash">查看当前主从状态
[root@itlaoxin17 ~]<span class="hljs-comment"># redis-cli -h 192.168.1.18</span>
192.168.1.18:6379> info replication
<span class="hljs-comment"># Replication</span>
role:slave
master_host:192.168.1.17
master_port:6379
[root@itlaoxin17 ~]<span class="hljs-comment"># systemctl stop redis    #在itlaoxin17上关闭master</span>

[root@itlaoxin-17 ~]<span class="hljs-comment"># redis-cli -h 192.168.1.19</span>
192.168.1.19:6379>info replication
<span class="hljs-comment"># Replication</span>
role:slave
master_host:192.168.1.8   <span class="hljs-comment">#master已经转移到itlaoxin18上了</span>
master_port:6379
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-33">9. 恢复itlaoxin17</h4>
<pre><code class="hljs language-bash copyable" lang="bash">[root@itlaoxin17 ~]<span class="hljs-comment"># systemctl start redis</span>
[root@itlaoxin17 ~]<span class="hljs-comment"># redis-cli -h 192.168.1.17</span>
192.168.1.17:6379> info replication
<span class="hljs-comment"># Replication</span>
role:slave
master_host:192.168.1.18   <span class="hljs-comment">#主redis还是itlaoxin18，并不会因为itlaoxin17恢复成功后，就主动让出权限。 这样可以避免再次回切时，发生服务中断。</span>
  <span class="hljs-comment">#登录主redis上查看从节点信息</span>
[root@itlaoxin-19 etc]<span class="hljs-comment"># redis-cli </span>
127.0.0.1:6379> info replication
<span class="hljs-comment"># Replication</span>
role:slave
master_host:192.168.1.18
master_port:6379
master_link_status:up
master_last_io_seconds_ago:1
master_sync_in_progress:0
slave_repl_offset:33537
slave_priority:100
slave_read_only:1
replica_announced:1
connected_slaves:0
master_failover_state:no-failover
master_replid:49a65486e84936ed563d6796f253945b492660a8
master_replid2:7514fbacc143345f567dd8e93a081592b24e0c9a
master_repl_offset:33537
second_repl_offset:2702
repl_backlog_active:1
repl_backlog_size:1048576 
repl_backlog_first_byte_offset:163
repl_backlog_histlen:33375
127.0.0.1:6379>
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-34">10、查看Sentinel信息</h4>
<pre><code class="hljs language-bash copyable" lang="bash">[root@itlaoxin17 ~]<span class="hljs-comment"># redis-cli -h 192.168.1.17 -p 26379  #查看Sentinel信息。</span>
[root@itlaoxin18 ~]<span class="hljs-comment"># redis-cli -h 192.168.1.17 -p 26379 </span>
192.168.1.17:26379> info sentinel
<span class="hljs-comment"># Sentinel</span>
sentinel_masters:1
sentinel_tilt:0
sentinel_running_scripts:0
sentinel_scripts_queue_length:0
sentinel_simulate_failure_flags:0
master0:name=mymaster,status=sdown,address=192.168.1.17:6379,slaves=0,sentinels=1
192.168.1.17:26379> <span class="hljs-built_in">exit</span>
14

<span class="copy-code-btn">复制代码</span></code></pre>
<p>互联网老辛，2021年立下个flag，每天直播分享技术5小时，持续10000小时，也就是2000天</p>
<blockquote>
<p>今天是持续直播教学的第 110 / 2000天。
求点赞、求评论、求收藏。
有任何疑问都可以在评论区询问，有问必答~</p>
</blockquote>
<p>收藏本文，以后没准能用到哦~</p></div>  
</div>
            