
---
title: 'JuiceFS v1.0 beta2 发布｜进一步提升稳定性'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=3129'
author: 开源中国
comments: false
date: Thu, 10 Mar 2022 15:26:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=3129'
---

<div>   
<div class="content">
                                                                                            <p>这是 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fjuicedata%2Fjuicefs" target="_blank">JuiceFS</a> v1.0 正式发布前的第二个 beta 版本，共有 16 位社区伙伴贡献了 150+ 次提交 🎉。本次更新以 Bug 修复和稳定性提升为主，辅以大量的文档更新和测试用例优化，并带来了以下新功能：</p> 
<h3>一、新增：BadgerDB 作为元数据引擎</h3> 
<p>由社区开发者秦牧羊（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fdiluga" target="_blank">@diluga</a>）发起贡献，在 JuiceFS 插件式元数据引擎架构上新增对 BadgerDB 数据库的支持，为 JuiceFS 元数据存储引擎家族再添新成员！</p> 
<p><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdgraph.io%2Fdocs%2Fbadger%2F" target="_blank">BadgerDB</a> 是一个 Go 语言开发的嵌入式、持久化的单机 Key-Value 数据库，它类似 SQLite 无需安装即可直接使用：</p> 
<pre><code># 创建文件系统
$ juicefs format badger://$HOME/badger-data test-volume
# 挂载文件系统
$ juicefs mount -d badger://$HOME/badger-data /mnt/jfs
</code></pre> 
<p>与 SQLite 不同之处在于，BadgerDB 的数据库不是单文件，而是一个目录。在上例中，BadgerDB 在<code>home</code>目录创建 <code>badger-data</code> 数据库目录，挂载文件系统时自然也要使用这个目录的路径。</p> 
<h3>二、一键启动 WebDAV 服务器</h3> 
<p>经过开源社区的共同努力，我们在稳定支持 FUSE-POSIX、S3-Gateway、HDFS、CSI Driver 等存储访问协议的基础上，新增了 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fen.wikipedia.org%2Fwiki%2FWebDAV" target="_blank">WebDAV</a> 访问协议，与 S3 网关的启用方式类似，使用新增的 <code>webdav</code> 子命令可以一键启动 WebDAV 服务器：</p> 
<pre><code>$ juicefs webdav redis://127.0.0.1:6379/1 localhost:9007
</code></pre> 
<p>使用任何支持 WebDAV 协议的客户端访问 <code>localhost:9007</code> 即可读写 JuiceFS 文件系统。</p> 
<h3>三、支持只读模式连接 Redis Replicas</h3> 
<p>对于 Redis 引擎读写压力较大的场景，现在支持让部分客户端以只读模式连接 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fredis.io%2Ftopics%2Fsentinel" target="_blank">Sentinel</a> 管理的 replicas，从而降低 master 节点的负载：</p> 
<pre><code>$ juicefs mount redis://mymaster,sentinel.local:26379?route-read=replica /mnt/jfs/ --read-only
</code></pre> 
<p>即在 URL 中添加参数 <code>route-read=replica</code> 指定该客户端自动从 Redis replicas 读取元数据。</p> 
<p>需要注意的是，由于 Redis replica 使用异步更新机制，设置了只读的客户端有时可能会读到较旧版本的元数据。</p> 
<h3>四、更清晰的客户端帮助信息</h3> 
<p>随着用户规模的不断扩大，我们发现想让各种经验背景的用户都能更好地使用 JuiceFS，一方面需要友好的文档，另一方面要增强 JuiceFS 客户端本身的命令帮助信息。特别是后者，如果问题可以在命令行里得到解决就能大大提升用户的使用体验。</p> 
<p>有鉴于此，在本次更新的版本中我们针对客户端的帮助信息做了以下改进：</p> 
<ol> 
 <li><strong>清晰的分类</strong> 
  <ul> 
   <li>ADMIN：用来管理 JuiceFS volumes，如 format、destroy、gc 等</li> 
   <li>INSPECTOR：用来检视 JuiceFS 的内部状态，如 stats、profile 等</li> 
   <li>SERVICE：用来启动特定的服务，如 mount、gateway 等</li> 
   <li>TOOL：用做特定需求的独立工具，如 bench、warmup 等</li> 
  </ul> </li> 
 <li><strong>详尽的说明</strong>：大部分命令增加了具体说明和使用示例</li> 
</ol> 
<h3>五、防止误操作</h3> 
<p>社区群组的讨论向我们证明了一件事：即便是经验丰富的老手，也不免会“做傻事”！特别是在创建和修改文件系统时，一些不经意的误操作可能会覆盖旧数据或导致错误的设置。</p> 
<p>针对这些可能涉及数据安全的操作，我们一直在完善相应的安全检查机制，本次新增的安全机制有：</p> 
<ol> 
 <li><strong>唯一性检查</strong>：检查并禁止在同一个 Bucket 上创建同名文件系统。</li> 
 <li><strong>防止非法参数</strong>：修改文件系统参数时，<code>config</code> 命令会尽量提前判断新参数是否合理，避免不合法的参数配置。</li> 
 <li><strong>隐藏敏感信息</strong>：当连接元数据引擎需要密码时，隐藏掉 <code>ps</code> 显示的进程密码参数。</li> 
</ol> 
<h2>修复的 Bug</h2> 
<ul> 
 <li>cmd: fix buffer-size in gc and fsck (#1316)</li> 
 <li>cmd/bench: convert PATH to absolute path (#1305)</li> 
 <li>meta: return EROFS as soon as possible (#1477)</li> 
 <li>meta/redis: fix leaked inodes in Redis (#1353)</li> 
 <li>meta/tkv: fix divide by zero error when dumping meta (#1369)</li> 
 <li>meta/tikv: fix scan of tikv, limiting the upperbound (#1455)</li> 
 <li>meta/memkv: fix scanKeys, returning a sorted list (#1381)</li> 
 <li>meta/sql: delete warning message for empty directory (#1442)</li> 
 <li>meta/sql: fix return value of mustInsert (#1429)</li> 
 <li>vfs: fixed deadlock when truncate a released file handle. (#1383)</li> 
 <li>vfs/trash: fix access to trash dir (#1356)</li> 
 <li>vfs/backup: skip dir objects when scanning meta backups (#1370)</li> 
 <li>vfs/backup: fix incorrect inode number when using subdir (#1385)</li> 
 <li>utils: fix the contention between progress bar and logger (#1436)</li> 
 <li>Windows: fix rename fails because the chunk file is still open (#1315)</li> 
 <li>Windows: fix mkdir on windows platform (#1327)</li> 
 <li>SDK: hadoop: fix umask apply (#1338, #1394)</li> 
 <li>SDK: hadoop: fix <a href="https://www.oschina.net/action/GoToLink?url=http%3A%2F%2Flibjfs.so" target="_blank">libjfs.so</a> load bug (#1458)</li> 
 <li>other: fix legend of "Operations" panel in Grafana template (#1321)</li> 
</ul>
                                        </div>
                                      
</div>
            