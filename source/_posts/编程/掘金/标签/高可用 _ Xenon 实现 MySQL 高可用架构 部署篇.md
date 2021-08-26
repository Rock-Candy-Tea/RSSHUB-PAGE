
---
title: '高可用 _ Xenon 实现 MySQL 高可用架构 部署篇'
categories: 
 - 编程
 - 掘金
 - 标签
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/daca1e83f3a74e37a7905d7fa2777cff~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Wed, 25 Aug 2021 19:58:11 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/daca1e83f3a74e37a7905d7fa2777cff~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>在《<a href="https://juejin.cn/post/6970878746882490404" target="_blank" title="https://juejin.cn/post/6970878746882490404">高可用 | Xenon：后 MHA 时代的选择</a>》一文中，我们对 Xenon 的实现原理、应用场景等做了简要介绍。文章发布后，社区小伙伴都在咨询 <em><strong>Xenon 如何与 MySQL 配合使用？</strong></em></p>
<p>本文来自知数堂投稿，是一篇基于 Xenon 架构原理，部署 <strong>一主两从</strong> 架构的 MySQL 高可用集群的实操文档。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/daca1e83f3a74e37a7905d7fa2777cff~tplv-k3u1fbpfcp-watermark.image" alt="Xenon 架构图" loading="lazy" referrerpolicy="no-referrer"></p>
Xenon 架构图 
<p>环境信息：</p>
<ul>
<li>Redhat 7</li>
<li>MySQL 5.7</li>
<li>Xenon 1.0.7</li>
<li>XtraBackup 24</li>
</ul>
<p>*<em>另：Xenon 支持 MySQL 5.6/5.7/8.0 内核，本文以 5.7 为例</em>。</p>
<h1 data-id="heading-0">1. 搭建 MySQL 增强半同步复制架构</h1>
<h2 data-id="heading-1">1.1 准备单机 MySQL</h2>
<p>准备三台单机 MySQL，安装步骤（略）。</p>
<ul>
<li>db1 (10.10.10.10)</li>
<li>db2 (10.10.10.11)</li>
<li>db3 (10.10.10.18)</li>
</ul>
<h2 data-id="heading-2">1.2 配置主从复制</h2>
<p>配置三台单机 MySQL 主从 复制关系，配置步骤（略）。</p>
<h2 data-id="heading-3">1.3 配置增强半同步复制</h2>
<p>在 db1 服务器上，开启 <code>semi_sync</code>插件。</p>
<pre><code class="copyable">set global super_read_only=0;   ---默认
set global read_only=0;         ---默认
INSTALL PLUGIN rpl_semi_sync_slave SONAME 'semisync_slave.so';
INSTALL PLUGIN rpl_semi_sync_master SONAME 'semisync_master.so';
show plugins;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>在 db2 和 db3 服务器上执行并查看结果。</p>
<pre><code class="copyable">stop  slave io_thread;
start slave io_thread;
2020-01-05T12:16:01.269943Z 20 [Note] Aborted connection 20 to db: 'unconnected' user: 'root' host: 'localhost' (Got timeout reading communication packets)
2020-01-05T12:25:57.193720Z 13 [Note] Slave I/O thread killed while reading event for channel ''
2020-01-05T12:25:57.193804Z 13 [Note] Slave I/O thread exiting for channel '', read up to log 'mysql-bin.000002', position 2310
2020-01-05T12:25:57.227685Z 22 [Note] Slave I/O thread: Start semi-sync replication to master 'repl@10.10.10.10:3306' in log 'mysql-bin.000002' at position 2310
2020-01-05T12:25:57.227782Z 22 [Warning] Storing MySQL user name or password information in the master info repository is not secure and is therefore not recommended. Please consider using the USER and PASSWORD connection options for START SLAVE; see the 'START SLAVE Syntax' in the MySQL Manual for more information.
2020-01-05T12:25:57.230523Z 22 [Note] Slave I/O thread for channel '': connected to master 'repl@10.10.10.10:3306',replication started in log 'mysql-bin.000002' at position 2310
<span class="copy-code-btn">复制代码</span></code></pre>
<p>至此，<strong>一主两从</strong> 增强半同步复制就配置好了，接下来即可使用 Xenon 搭建高可用架构。</p>
<h1 data-id="heading-4">2. 使用 Xenon 搭建高可用架构</h1>
<h2 data-id="heading-5">2.1 环境准备</h2>
<h3 data-id="heading-6">2.1.1 配置帐号</h3>
<p>修改 MySQL 的路径和帐号密码，由 <code>/sbin/nologin</code> 修改为 <code>/bin/bash</code>，并修改 MySQL 帐号的密码。</p>
<p>说明：MySQL 默认路径为 <code>/bin/bash</code>。</p>
<pre><code class="copyable">chsh mysql
Changing shell for mysql.
New shell [/sbin/nologin]: /bin/bash
passwd mysql
<span class="copy-code-btn">复制代码</span></code></pre>
<p>为 Xenon 的帐号添加 <code>sudo /usr/ip</code> 权限。</p>
<pre><code class="copyable">visudo 
mysql   ALL=(ALL)       NOPASSWD: /usr/sbin/ip
# 添加权限前
[mysql@db1 ~]$ sudo /sbin/ip a a 10.10.10.30/16 dev enp0s3 && arping -c 3 -A  172.18.0.100  -I enp0s3
bind: Cannot assign requested address 
# 添加权限后
[mysql@db1 ~]$ ping 10.10.10.30
PING 10.10.10.30 (10.10.10.30) 56(84) bytes of data.
64 bytes from 10.10.10.30: icmp_seq=1 ttl=64 time=0.021 ms
[1]+  Stopped                 ping 10.10.10.30
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-7">2.1.2 建立互信关系</h3>
<p>建立三台服务器之间互信关系。</p>
<pre><code class="copyable">ssh-copy-id -i /home/mysql/.ssh/id_rsa.pub 10.10.10.18
ssh-copy-id -i /home/mysql/.ssh/id_rsa.pub 10.10.10.10
ssh-copy-id -i /home/mysql/.ssh/id_rsa.pub 10.10.10.11
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-8">2.1.3 安装 XtraBackup</h3>
<pre><code class="copyable">yum install -y perl-DBD-MySQL
rpm -ivh libev-4.15-1.el6.rf.x86_64.rpm 
rpm -ivh percona-xtrabackup-24-2.4.15-1.el7.x86_64.rpm

root@db2 tmp]# rpm -ivh percona-xtrabackup-24-2.4.15-1.el7.x86_64.rpm 
warning: percona-xtrabackup-24-2.4.15-1.el7.x86_64.rpm: Header V4 RSA/SHA256 Signature, key ID 8507efa5: NOKEY
Preparing...                          ################################# [100%]
Updating / installing...
   1:percona-xtrabackup-24-2.4.15-1.el################################# [100%]
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-9">2.1.4 安装 Go</h3>
<pre><code class="copyable">wget https://golang.org/doc/install?download=go1.13.4.linux-amd64.tar.gz
tar -C /usr/local -xzf go1.13.4.linux-amd64.tar.gz
echo "export PATH=\$PATH:/usr/local/go/bin" >> /etc/profile

[root@db1 tmp]# source /etc/profile
[root@db1 tmp]# which go
/usr/local/go/bin/go
[root@db1 tmp]# go version
go version go1.13.4 linux/amd64
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-10">2.2 安装 Xenon</h2>
<p>在 <a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fradondb%2Fxenon%2Freleases" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/radondb/xenon/releases" ref="nofollow noopener noreferrer">github.com/radondb/xen…</a> 下载 1.0.7 版本的安装包至服务器。</p>
<pre><code class="copyable">[root@db1 local]# tar -xvf xenon-1.0.7.tar.gz
[root@db1 local]# mv xenon-1.0.7 xenon
[root@db1 local]# cd /usr/local/xenon
[root@db1 xenon]# make build
fatal: Not a git repository (or any of the parent directories): .git
fatal: Not a git repository (or any of the parent directories): .git
fatal: Not a git repository (or any of the parent directories): .git
fatal: Not a git repository (or any of the parent directories): .git
--> Building...
# 省略……
[root@db1 xenon]# make
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-11">2.3 配置 Xenon</h2>
<h3 data-id="heading-12">2.3.1 添加配置文件</h3>
<p>添加 db1 的配置文件。</p>
<pre><code class="copyable">[mysql@db1 conf]$ cat xenon.json 
&#123;
"server":
&#123;
   "endpoint":"10.10.10.10:8801"
&#125;,
"raft":
&#123;
   "meta-datadir":"raft.meta",
   "heartbeat-timeout":1000,
   "election-timeout":3000,
   "admit-defeat-hearbeat-count": 5,
   "purge-binlog-disabled": true,
   "leader-start-command":"sudo /sbin/ip a a 10.10.10.20/24 dev enp0s3 && arping -c 3 -A 10.10.10.20 -I enp0s3",
   "leader-stop-command":"sudo /sbin/ip a d 10.10.10.20/24 dev enp0s3"
&#125;,
"mysql":
&#123;
   "admin":"root",                
   "passwd":"123456",            
   "host":"127.0.0.1",              
   "port":3306,                    
   "basedir":"/usr/local/mysql",    
   "defaults-file":"/etc/my.cnf"
&#125;,
"replication":
&#123;
   "user":"repl",                
   "passwd":"123456"        
&#125;,
"backup":
&#123;
   "ssh-host":"10.10.10.10",                    
   "ssh-user":"mysql",                            
   "ssh-passwd":"123456",                        
   "basedir":"/usr/local/mysql",                 
   "backup-dir":"/backup",
   "mysqld-monitor-interval": 5000,
   "backup-use-memory": "3072M",
   "ssh-port": 22,
   "backup-parallel": 2,         
   "backup-iops-limits": 100000,                 
   "xtrabackup-bindir":"/usr/bin"       
&#125;,
"rpc":
&#123;
   "request-timeout":500
&#125;,
"log":
&#123;
   "level":"INFO"
&#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>添加 db2 和 db3 的配置文件。以 db2 配置文件为示例。</p>
<pre><code class="copyable">[mysql@db2 ~]$ cd /usr/local/xenon/conf
[mysql@db2 conf]$ cat xenon.json 
&#123;
"server":
&#123;
   "endpoint":"10.10.10.11:8801"  #添加 db3 配置文件时，需设置为 10.10.10.18
&#125;,
"raft":
&#123;
   "meta-datadir":"raft.meta",
   "heartbeat-timeout":1000,
   "election-timeout":3000,
   "admit-defeat-hearbeat-count": 5,
   "purge-binlog-disabled": true,
   "leader-start-command":"sudo /sbin/ip a a 10.10.10.20/24 dev enp0s3 && arping -c 3 -A 10.10.10.20 -I enp0s3",
   "leader-stop-command":"sudo /sbin/ip a d 10.10.10.20/24 dev enp0s3"
&#125;,
"mysql":
&#123;
   "admin":"root",                
   "passwd":"123456",            
   "host":"127.0.0.1",              
   "port":3306,                    
   "basedir":"/usr/local/mysql",    
   "defaults-file":"/etc/my.cnf"
&#125;,
"replication":
&#123;
   "user":"repl",                
   "passwd":"123456"        
&#125;,
"backup":
&#123;
   "ssh-host":"10.10.10.11",                    
   "ssh-user":"mysql",                            
   "ssh-passwd":"123456",                        
   "basedir":"/usr/local/mysql",                 
   "backup-dir":"/backup",
   "mysqld-monitor-interval": 5000,
   "backup-use-memory": "3072M",
   "ssh-port": 22,
   "backup-parallel": 2,         
   "backup-iops-limits": 100000,                 
   "xtrabackup-bindir":"/usr/bin"       
&#125;,
"rpc":
&#123;
   "request-timeout":500
&#125;,
"log":
&#123;
   "level":"INFO"
&#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>注意：主机配置文件中<code>leader-start-command</code> 和  <code>leader-stop-command</code> 参数的值，10.10.10.20/24 和 enp0s3 需要根据实际情况填写。</p>
<h3 data-id="heading-13">2.3.2 配置备份环境</h3>
<pre><code class="copyable">mkdir /backup & chown -R mysql.mysql /backup
<span class="copy-code-btn">复制代码</span></code></pre>
<p>在复制环境中创建管理员帐号。</p>
<pre><code class="copyable">create user 'root'@'127.0.0.1' identified by '123456';
grant all privileges on *.* to 'root'@'127.0.0.1';
flush privileges;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-14">2.3.3 修改权限</h3>
<pre><code class="copyable">mkdir /etc/xenon/
ln -s /usr/local/xenon/conf/xenon.json /etc/xenon/
chown mysql.mysql -R /usr/local/xenon
chown mysql.mysql -R /etc/xenon/
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-15">2.3.4 修改日志目录</h3>
<pre><code class="copyable">mkdir /etc/xenon/log
chown mysql.mysql /etc/xenon/log
cd /usr/local/xenon/bin/
echo "/etc/xenon/xenon.json" > /usr/local/xenon/bin/config.path
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-16">2.4 启用 Xenon</h2>
<h3 data-id="heading-17">2.4.1 登录</h3>
<p>通过 MySQL 帐号登录并启动 Xenon。</p>
<pre><code class="copyable"># db1
su - mysql
/usr/local/xenon/bin/xenon -c /etc/xenon/xenon.json > /etc/xenon/log/xenon.log 2>&1 &
 
# db2
su - mysql
/usr/local/xenon/bin/xenon -c /etc/xenon/xenon.json > /etc/xenon/log/xenon.log 2>&1 &
 
# db3
su - mysql
/usr/local/xenon/bin/xenon -c /etc/xenon/xenon.json > /etc/xenon/log/xenon.log 2>&1 &
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-18">2.4.2 添加成员</h3>
<pre><code class="copyable">/usr/local/xenon/bin/xenoncli cluster add \
10.10.10.10:8801,10.10.10.11:8801,10.10.10.18:8801
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-19">2.4.3 查看集群状态</h3>
<p>查看集群状态。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/cf61e6734c064c539108d8f07550fb3c~tplv-k3u1fbpfcp-watermark.image" alt="file" loading="lazy" referrerpolicy="no-referrer"></p>
<p>查看 MySQL 状态。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/63c2ebc536104bf79054a79c3d9024ff~tplv-k3u1fbpfcp-watermark.image" alt="file" loading="lazy" referrerpolicy="no-referrer"></p>
<p><strong>MySQL 高可用部署成功！</strong></p>
<h1 data-id="heading-20">总结</h1>
<p>在使用 Xenon 搭建高可用集群时，需要注意以下几点：</p>
<ol>
<li>MySQL 5.7+ GTID 复制结构为基础</li>
<li>必须有增强半同步复制插件</li>
<li>MySQL 帐号必须是 <code>/bin/bash</code></li>
<li>Xenon 和 MySQL 必须运行在同一帐号下，一般就是 MySQL</li>
<li>MySQL 帐号在节点之前必须有 SSH 信任</li>
<li>节点必须安装 Xtrabackup</li>
<li>必须使用 mysqld_safe 启用 mysql</li>
</ol>
<h1 data-id="heading-21">下期预告</h1>
<p>下一期我们将介绍 Xenon 常见操作。</p></div>  
</div>
            