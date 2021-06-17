
---
title: 'windows server 2012 MySql 主从架构实现'
categories: 
 - 编程
 - 掘金
 - 标签
headimg: 'https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/56338abe2ec843e098bc1697affa9c2a~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Wed, 16 Jun 2021 18:06:10 GMT
thumbnail: 'https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/56338abe2ec843e098bc1697affa9c2a~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h1 data-id="heading-0">windows server 2012 MySql 主从架构实现</h1>
<h4 data-id="heading-1">一主一从</h4>
<ol>
<li>
<h5 data-id="heading-2">环境准备</h5>
<p>windows server 服务器一台（最好是准备两台），mysql 8.0.16 安装包（mysql-8.0.16-winx64.zip），配置好windows 环境，如果主从节点不在同一台服务器，注意防火墙、各个节点的时钟服务同步、各节点之间可以通过主机名相互通讯。</p>
</li>
<li>
<h5 data-id="heading-3">准备步骤</h5>
<ol>
<li>
<p>安装mysql, master 节点，解压安装包到指定目录：D:\soft\mysql-8.0.16-winx64，我是解压到这里，解压之后是缺少data目录和my.ini 配置文件的，所以我们自行创建。还要将解压后的 bin 路径添加到<code>环境变量 path</code> 里面</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/56338abe2ec843e098bc1697affa9c2a~tplv-k3u1fbpfcp-watermark.image" alt="image-20210615145842592.png" loading="lazy" referrerpolicy="no-referrer">
创建master 主节点 my.ini 文件，写入基本配置：</p>
<pre><code class="hljs language-ini copyable" lang="ini"><span class="hljs-section">[mysqld]</span>
<span class="hljs-comment"># 设置3306端口</span>
<span class="hljs-attr">port</span>=<span class="hljs-number">3306</span>
<span class="hljs-comment"># 设置mysql的安装目录</span>
<span class="hljs-comment"># 根据自己的地址更改</span>
<span class="hljs-attr">basedir</span>=D:\\soft\\mysql-<span class="hljs-number">8.0</span>.<span class="hljs-number">16</span>-winx64
<span class="hljs-comment"># 设置mysql数据库的数据的存放目录</span>
<span class="hljs-comment"># 根据自己的地址更改</span>
<span class="hljs-attr">datadir</span>=D:\\soft\\mysql-<span class="hljs-number">8.0</span>.<span class="hljs-number">16</span>-winx64\\data
<span class="hljs-comment"># 允许最大连接数</span>
<span class="hljs-attr">max_connections</span>=<span class="hljs-number">2000</span>
<span class="hljs-comment"># 允许连接失败的次数。这是为了防止有人从该主机试图攻击数据库系统</span>
<span class="hljs-attr">max_connect_errors</span>=<span class="hljs-number">10</span>
<span class="hljs-comment"># 服务端使用的字符集默认为UTF8</span>
<span class="hljs-attr">character-set-server</span>=UTF8MB4
<span class="hljs-comment"># 创建新表时将使用的默认存储引擎</span>
<span class="hljs-attr">default-storage-engine</span>=INNODB
<span class="hljs-comment"># 默认使用“mysql_native_password”插件认证</span>
<span class="hljs-attr">default_authentication_plugin</span>=mysql_native_password

<span class="hljs-section">[mysql]</span>
<span class="hljs-comment"># 设置mysql客户端默认字符集</span>
<span class="hljs-attr">default-character-set</span>=UTF8MB4

<span class="hljs-section">[client]</span>
<span class="hljs-comment"># 设置mysql客户端连接服务端时默认使用的端口</span>
<span class="hljs-attr">port</span>=<span class="hljs-number">3306</span>
<span class="hljs-attr">default-character-set</span>=utf8
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
<li>
<p>安装mysql</p>
<p>在mysql的安装目录：D:\soft\mysql-8.0.16-winx64\bin下，以管理员身份运行cmd，执行下面的命令：</p>
<pre><code class="hljs language-sh copyable" lang="sh">mysqld --defaults-file=D:\soft\mysql-8.0.16-winx64\my.ini --initialize --console
<span class="copy-code-btn">复制代码</span></code></pre>
<p>执行完成后，会打印 root 用户的初始默认密码,复制并保存它。</p>
<img loading="lazy" src="https://juejin.cn/post/undefined" referrerpolicy="no-referrer">
<p>再行下面的命令安装mysql服务：</p>
<pre><code class="hljs language-sh copyable" lang="sh">mysqld --install 服务名 --defaults-file=D:\soft\mysql-8.0.16-winx64\my.ini
<span class="copy-code-btn">复制代码</span></code></pre>
<p>安装成功后，使用命令 ：net start  服务名，启动mysql 服务，使用之前root 账号的默认密码，登录mysql ，修改密码。</p>
<p>修改密码的sql:</p>
<pre><code class="hljs language-sql copyable" lang="sql"><span class="hljs-keyword">ALTER</span> <span class="hljs-keyword">USER</span> <span class="hljs-string">'root'</span>@<span class="hljs-string">'localhost'</span> IDENTIFIED <span class="hljs-keyword">WITH</span> mysql_native_password <span class="hljs-keyword">BY</span> <span class="hljs-string">'新密码'</span>;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/9c31d5db5a0c46f093ba63e5e8dbefb3~tplv-k3u1fbpfcp-watermark.image" alt="uTools_1623742626184.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>安装mysql 就完成了。其他从节点安装，请参考以上步骤。</p>
</li>
</ol>
</li>
<li>
<h5 data-id="heading-4">实现步骤</h5>
<ul>
<li>
<p><strong>架构图</strong></p>
<ul>
<li><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/7958209f60d64f998ba4f1909bd158e7~tplv-k3u1fbpfcp-watermark.image" alt="image-20210615153900561.png" loading="lazy" referrerpolicy="no-referrer"></li>
</ul>
</li>
<li>
<p><strong>配置master主服务器</strong></p>
<ul>
<li>
<p>找到mysql 安装目录中的 my.ini 文件,进行一些配置，报过二进制日志文件，唯一server-id的指定。如：</p>
<pre><code class="hljs language-ini copyable" lang="ini"><span class="hljs-section">[mysqld]</span>
.....
<span class="hljs-comment">#### 主从配置 ####</span>
<span class="hljs-attr">server-id</span>=<span class="hljs-number">1</span>
<span class="hljs-comment">#打开Mysql日志，日志格式为二进制</span>
<span class="hljs-attr">log-bin</span>=master-bin
<span class="hljs-comment">#每次执行写入就与硬盘同步, 根据业务需求进行相应调整</span>
<span class="hljs-attr">sync-binlog</span>=<span class="hljs-number">1</span>
<span class="hljs-comment">#需要同步的二进制数据库名</span>
<span class="hljs-attr">binlog-do-db</span>=xxxx
<span class="hljs-comment">#只保留7天的二进制日志，以防磁盘被日志占满，根据业务需求进行相应调整</span>
<span class="hljs-attr">expire-logs-days</span>=<span class="hljs-number">7</span>
<span class="hljs-comment">#不备份的数据库</span>
<span class="hljs-attr">binlog-ignore-db</span>=information_schema
<span class="hljs-attr">binlog-ignore-db</span>=performation_schema
<span class="hljs-attr">binlog-ignore-db</span>=sys
<span class="hljs-attr">binlog-ignore-db</span>=mysql

<span class="hljs-comment">#mysql复制主要有三种方式:</span>
<span class="hljs-comment"># 根据业务需求进行相应调整</span>
<span class="hljs-attr">binlog_format</span>=ROW
<span class="copy-code-btn">复制代码</span></code></pre>
<p>修改完后，重启mysqL 服务。</p>
</li>
</ul>
</li>
<li>
<p><strong>创建复制账号</strong></p>
<ul>
<li>
<p>在master 节点上创建一个专门的主从同步的账号，每个 slave 使用标准的 MySQL 用户名和密码连接 master 。进行复制操作的用户会授予 REPLICATION SLAVE 权限。</p>
<pre><code class="hljs language-sql copyable" lang="sql"># 创建账户
<span class="hljs-keyword">CREATE</span> <span class="hljs-keyword">USER</span> `m<span class="hljs-operator">-</span>slave`@`<span class="hljs-operator">%</span>` IDENTIFIED <span class="hljs-keyword">WITH</span> mysql_native_password <span class="hljs-keyword">BY</span> <span class="hljs-string">'密码'</span> PASSWORD EXPIRE NEVER;
# 授权
<span class="hljs-keyword">GRANT</span> Replication Client, Replication Slave <span class="hljs-keyword">ON</span> <span class="hljs-operator">*</span>.<span class="hljs-operator">*</span> <span class="hljs-keyword">TO</span> `m<span class="hljs-operator">-</span>slave`@`<span class="hljs-operator">%</span>`;
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
</ul>
</li>
<li>
<p><strong>查看master状态</strong></p>
<ul>
<li>
<p>在 Master 的数据库执行 <code>show master status</code>，查看主服务器二进制日志状态及位置号。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/93c294b58c67415390b58a9ad5df3e3e~tplv-k3u1fbpfcp-watermark.image" alt="image-20210615155643785.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>后面，同步时会用到。</p>
</li>
</ul>
</li>
<li>
<p><strong>配置slave从服务器</strong></p>
<ul>
<li>
<p>找到从节点的mysql 安装目录的my.ini 文件，打开中继日志，指定唯一的 servr ID，设置只读权限。在配置文件加入如下值：</p>
<pre><code class="hljs language-ini copyable" lang="ini"><span class="hljs-comment">#### 主从配置 #####</span>
<span class="hljs-comment"># 配置server-id，让从服务器有唯一ID号</span>
<span class="hljs-attr">server-id</span>=<span class="hljs-number">2</span>
<span class="hljs-comment"># 打开Mysql中继日志，日志格式为二进制</span>
<span class="hljs-attr">relay_log</span>=mysql-relay-bin
<span class="hljs-comment"># 设置只读权限</span>
<span class="hljs-attr">read_only</span>=<span class="hljs-number">1</span>
<span class="hljs-comment"># 开启从服务器二进制日志</span>
<span class="hljs-attr">log_bin</span>=slave-bin
<span class="hljs-comment"># 使得更新的数据写进二进制日志中</span>
<span class="hljs-attr">log_slave_updates</span>=<span class="hljs-number">1</span>

<span class="hljs-comment"># 需要同步的库,库名称相同</span>
<span class="hljs-comment">#replicate-do-db=xxx</span>
<span class="hljs-comment">#replicate-do-db=shop_ds_master</span>

<span class="hljs-comment">#如果需要同步的数据库名不同</span>
<span class="hljs-comment"># master 上的数据库名为 shop_ds_master ， slave 上的库名为 shop_ds_slave</span>
<span class="hljs-attr">replicate-rewrite-db</span>=test->test


<span class="hljs-comment">#跳过所有的错误错误，继续执行复制操作,适合大数据量同步</span>
<span class="hljs-comment">#slave-skip-errors=all</span>

<span class="hljs-comment">#不同步mysql系统数据库</span>
<span class="hljs-attr">replicate-ignore-db</span>=mysql
<span class="copy-code-btn">复制代码</span></code></pre>
<p>修改完，记得重启mysql 服务。</p>
</li>
</ul>
</li>
<li>
<p><strong>启动从服务器复制线程</strong></p>
<ul>
<li>
<pre><code class="hljs language-sql copyable" lang="sql">MariaDB [(<span class="hljs-keyword">none</span>)]<span class="hljs-operator">></span> change master <span class="hljs-keyword">to</span> master_host<span class="hljs-operator">=</span><span class="hljs-string">'192.168.37.111'</span>, <span class="hljs-operator">/</span><span class="hljs-operator">/</span> 主节点的ip
   <span class="hljs-operator">></span>master_user<span class="hljs-operator">=</span><span class="hljs-string">'slave'</span>,  <span class="hljs-operator">/</span><span class="hljs-operator">/</span> 同步账户
   <span class="hljs-operator">></span>master_password<span class="hljs-operator">=</span><span class="hljs-string">'keer'</span>,  <span class="hljs-operator">/</span><span class="hljs-operator">/</span> 密码
   <span class="hljs-operator">></span>master_port<span class="hljs-operator">=</span><span class="hljs-string">'3306'</span>,  <span class="hljs-operator">/</span><span class="hljs-operator">/</span> 端口
   <span class="hljs-operator">></span>master_log_file<span class="hljs-operator">=</span><span class="hljs-string">'master-bin.000001'</span>,  <span class="hljs-operator">/</span><span class="hljs-operator">/</span> master对应的bin<span class="hljs-operator">-</span>log文件
   <span class="hljs-operator">></span>master_log_pos<span class="hljs-operator">=</span><span class="hljs-number">1496</span>; <span class="hljs-operator">/</span><span class="hljs-operator">/</span> 同步位置号
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
<li>
<p>启动复制线程：</p>
<pre><code class="hljs language-sql copyable" lang="sql"><span class="hljs-operator">></span> <span class="hljs-keyword">start</span> slave;
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
</ul>
</li>
<li>
<p><strong>查看从服务器状态</strong></p>
<ul>
<li>
<p>可使用<code>SHOW SLAVE STATUS\G;</code>查看从服务器状态，如下所示，也可用<code>show processlist \G;</code>查看当前复制状态：</p>
</li>
<li>
<pre><code class="hljs language-java copyable" lang="java">    Slave_IO_Running: Yes<span class="hljs-comment">//IO线程正常运行</span>
Slave_SQL_Running: Yes<span class="hljs-comment">//SQL线程正常运行</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img alt loading="lazy" src="https://juejin.cn/post/undefined" referrerpolicy="no-referrer"></p>
</li>
</ul>
</li>
<li>
<p><strong>测试</strong></p>
<p>主从同步测试：</p>
<p>​我们在 master 服务器上创建一个数据库，再使用该数据库创建一个表，添加一条记录，来看一看 slave 服务器有没有同步成功。
　　首先，我们先来查看一下两个服务器上有什么数据库：</p>
<p>​master:</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/2b06c48471ac4859979a708204b1d119~tplv-k3u1fbpfcp-watermark.image" alt="image-20210615162140974.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>slave:</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/f86ebadf1f8f417d99d33ecc3dcb1427~tplv-k3u1fbpfcp-watermark.image" alt="image-20210615162150425.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>在master 服务器中 test库中创建一个表“t_user”,看从服务器中是否有这张表：</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/cc5235ce284c40088057e7133b06eb37~tplv-k3u1fbpfcp-watermark.image" alt="image-20210615162721592.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>从服务器上也有这张表：t_user</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/6c733ad7a7df4f778a9d24fe4745d0cb~tplv-k3u1fbpfcp-watermark.image" alt="image-20210615162844470.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>说明主从同步成功了！</p>
</li>
</ul>
</li>
</ol></div>  
</div>
            