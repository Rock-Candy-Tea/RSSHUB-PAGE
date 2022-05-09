
---
title: 'JuiceFS v1.0 beta3 发布，新增支持 etcd、Amazon MemoryDB 等'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://www.oschina.net/img/bVcZAzZ'
author: 开源中国
comments: false
date: Mon, 09 May 2022 10:30:00 GMT
thumbnail: 'https://www.oschina.net/img/bVcZAzZ'
---

<div>   
<div class="content">
                                                                    
                                                        <p>JuiceFS v1.0 beta3 在元数据引擎方面继续增强，新增 etcd 支持小于 200 万文件的使用场景，相比 Redis 可以提供更好的可用性和安全性。同时支持了 Amazon MemoryDB for Redis 和 Redis Cluster。至此，JuiceFS 支持的元数据引擎有：</p> 
<ol> 
 <li><strong>Redis</strong>：包括单机、Sentinel 和 Cluster 模式，适合小于 1 亿文件，同时追求高性能的场景。基于 AOF 的异步复制有少量数据丢失的风险，Amazon MemoryDB for Redis 使用同步数据复制，数据安全性更高；</li> 
 <li><strong>关系型数据库</strong>：包括 MySQL、MariaDB、PostgreSQL，适合数据安全要求高，性能要求不高的场景；</li> 
 <li><strong>TiKV</strong>：适合海量文件（1 亿以上），对性能与数据安全都有高要求的场景，但运维门槛比前面的方案高；</li> 
 <li><strong>etcd</strong>：适合小于 200 万文件并且可用性与数据安全要求高的场景；</li> 
 <li><strong>嵌入式数据库</strong>：包括 BadgerDB 和 SQLite，适合不需要多机访问的场景使用。</li> 
</ol> 
<p>除了元数据引擎的升级，JuiceFS S3 网关也提供了多租户、权限设置等高级功能，同时支持了非 UTF-8 编码的文件名。</p> 
<p>本次更新共有 <strong>22 位社区贡献者</strong>参与贡献了<strong>超过 240 次提交</strong>，感谢每一位的付出，也欢迎正在读文章的你参与到 JuiceFS 社区中来。</p> 
<p>下面，来为你解读一下 JuiceFS v1.0 beta3 的详细变化。</p> 
<h2>新增 etcd 元数据引擎</h2> 
<p><img alt src="https://www.oschina.net/img/bVcZAzZ" referrerpolicy="no-referrer"><img alt height="301" src="https://oscimg.oschina.net/oscnet/up-c37a6505edeee09180521595cd7f22cf709.png" width="600" referrerpolicy="no-referrer"></p> 
<p><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fetcd.io%2F" target="_blank">etcd</a> 是一个数据可靠的分布式 KV 存储系统，在 Kubernetes 中广泛使用，etcd 的数据修改会同步写到磁盘上，保证数据安全，通过 Raft 共识算法实现数据复制和故障切换，实现高可用。相比使用异步落盘和异步复制的 Redis 有更好的数据安全性和可用性。</p> 
<p>但 etcd 能够支撑的数据规模比较有限，从实际测试来看，小于 200 万文件时，是个不错的选择。</p> 
<p>使用方法与其他引擎类似，协议头为 <code>etcd://</code>，例如：</p> 
<pre><code class="language-bash"># 创建文件系统
$ juicefs format etcd://localhost:2379/myjfs jfs-etcd
# 挂载文件系统
$ juicefs mount -d etcd://localhost:2379/myjfs /mnt/jfs
</code></pre> 
<p>关于 etcd 的性能表现，请查看<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fjuicefs.com%2Fdocs%2Fzh%2Fcommunity%2Fmetadata_engines_benchmark" target="_blank">《元数据引擎性能测试文档》</a>。</p> 
<h2>支持 Redis Cluster 和 Amazon MemoryDB for Redis</h2> 
<p>由于 JuiceFS 依赖数据库事务保证数据强一致性，而 Redis Cluster 采用分片机制将数据分散在不同的分片上，但不支持跨分区的事务，导致不能使用 Redis Cluster 作为 JuiceFS 的元数据引擎。</p> 
<p><img alt src="https://www.oschina.net/img/bVcZAzU" referrerpolicy="no-referrer"><img alt height="450" src="https://oscimg.oschina.net/oscnet/up-1109abcb32c22414581229ba7c50b903ec9.jpg" width="800" referrerpolicy="no-referrer"></p> 
<p>v1.0 beta3 通过使用固定前缀的方式让所有的数据都分配到单一的 Redis 分区中，从而保证了 Redis 事务功能不受影响。这个方法不能充分享受 Redis 集群的数据分片能力，但可以获得数据复制和选举方面的便利（类似于哨兵模式）。另外，这种前缀方式类似于单机模式的多库功能，有无限的扩展能力，适用于有很多小规模文件系统的场景。</p> 
<p>AWS 最新发布的 MemoryDB for Redis 只提供集群模式，相比 ElastiCache 或者自己维护的 Redis，它的同步数据复制提供了更高的数据安全保证（但写入延迟更高），适用于对数据的安全性要求非常高，写少读多的场景。因为所有元数据都会集中在单个分片中，推荐使用一个分区加一份复制的部署模式（类似于主从模式），后续通过更换为更大内存的节点方式来扩容。</p> 
<h2>碎片延迟清理功能</h2> 
<p>JuiceFS 在读写文件时，如果该文件的数据碎片过多，就会自动触发碎片合并流程，将碎片聚合成大段数据并清理掉旧的碎片。</p> 
<p>然而，在元数据迁移、故障恢复等场景中，用户可能需要使用旧版本的元数据备份，此时如果数据碎片已被清理，就会导致相关文件读取失败。</p> 
<p>另外，当 Redis 丢失少量元数据时，也可能因为部分文件使用了已经被清理的碎片而损坏。</p> 
<p>为了解决上述问题，在 v1.0 beta3 中加入了<strong>碎片延迟清理功能</strong>，对于开启了回收站的文件系统，碎片会被延迟删除，超过设定的回收站时间后才被自动清理，也可以用 gc 命令手动清理。</p> 
<h2>增强 Sync 命令</h2> 
<p>v1.0 beta3 进一步调整了 Sync 命令的功能，使其在用法上与大家熟知的 rsync 工具尽量保持一致，减少上手成本。</p> 
<p>调整了用于过滤文件列表的 <code>--include</code> 和 <code>--exclude</code> 的用法，跟 rsync 保持一致，允许指定多个过滤规则，根据它们在命令行中的顺序和 Bash 通配符进行匹配，几乎可以实现任意集合的文件筛选需要，更具体的用法请参照 rsync 的文档。</p> 
<p>Sync 命令默认会拷贝符号链接的目标文件，可以通过 <code>--links</code> 参数调整为拷贝符号链接本身。</p> 
<p>另外，还加了一个 <code>--limit</code> 参数用于限制操作的文件个数，当设置为 1 时表示不进行递归遍历。</p> 
<h2>S3 网关功能升级</h2> 
<p>JuiceFS 的 S3 网关是基于 MinIO 的早期版本实现的，并且裁剪了一些非必要的功能。新版本的 MinIO 改用了 AGPL 协议，不能被 JuiceFS 直接升级使用。</p> 
<p>现在采取了反向集成的策略，在支持网关功能的最新版 MinIO 上集成 JuiceFS v1.0 beta3，整体基于 AGPL 协议开源，这样可以使用新版本的 MinIO 提供的多租户、权限设置等更多高级功能，详情请参考 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fjuicefs.com%2Fdocs%2Fzh%2Fcommunity%2Fs3_gateway" target="_blank">S3 网关文档</a>。</p> 
<p>JuiceFS 仍然内置了基础版的 S3 网关功能，而更完整的版本请使用这个反向集成的版本，<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fjuicedata%2Fminio%2Ftree%2Fgateway" target="_blank">代码请见</a>。</p> 
<h2>其它新功能</h2> 
<ol> 
 <li>支持 TLS 加密连接 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fjuicefs.com%2Fdocs%2Fzh%2Fcommunity%2Fdatabases_for_metadata%23%25E8%25AE%25BE%25E7%25BD%25AE-tls" target="_blank">TiKV 元数据引擎</a>。</li> 
 <li>创建文件系统时，可以通过 <code>--hash-prefix</code> 选项为数据写入对象存储时添加哈希前缀。很多对象存储有基于前缀的 QPS 限制或者系统瓶颈，通过该特性可以绕过这类限制以获得更好的性能。注意，已有数据写入的旧文件系统无法更改此选项。</li> 
 <li>挂载文件系统时，可以通过 <code>--heartbeat</code> 选项设置客户端的心跳间隔，这在一些关注故障切换时间的场景下能发挥作用。注意，默认的心跳过期时间已由 60s 调整为 12s。</li> 
 <li>数据存储增加 Oracle Object Storage 支持。</li> 
 <li>Java SDK 支持上报监控指标到 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fjuicefs.com%2Fdocs%2Fzh%2Fcommunity%2Fadministration%2Fmonitoring%2F%23graphite" target="_blank">Graphite 或者兼容的系统</a>。</li> 
 <li>SQL 引擎支持非 UTF-8 编码的文件名，已有的文件系统需要升级客户端后再修改数据库的表结构。</li> 
</ol> 
<h2>其它变化</h2> 
<ol> 
 <li>在新建文件系统时，会自动在数据存储中写入一个记录了 UUID 的占位对象，避免其他文件系统重复使用相同的数据存储造成混淆。</li> 
 <li><code>juicefs dump</code> 命令会自动隐藏对象存储的 <strong>secret key</strong> 防止泄漏敏感信息。</li> 
 <li>改用加密形式存储对象存储访问密钥，减小安全隐患；已有的文件系统可通过 <code>juicefs config META-URL --encrypt-secret</code> 命令调整加密模式。注意，修改后旧版客户端将无法挂载。</li> 
 <li>调整元数据默认备份机制，当文件数多于一百万时，需要用户显式指定备份周期。</li> 
 <li>在 Linux 下使用非 root 用户挂载时，将默认的缓存和日志目录改为此用户的家目录，避免因权限不足而失败。</li> 
 <li>改进了往 Redis 和 SQL 数据库导入大型目录（超过一百万文件）的能力。</li> 
 <li>为关系型数据库所有表结构增加主键，提升日志复制性能，<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fvettabase.com%2Fblog%2Fwhy-tables-need-a-primary-key-in-mariadb-and-mysql%2F" target="_blank">详情参考</a>。</li> 
</ol> 
<h2>升级建议</h2> 
<p>请在升级新版前注意评估以下几个变化：</p> 
<h3>会话管理格式调整</h3> 
<p>自 v1.0 beta3 开始，会话管理使用了新的格式，旧版本客户端通过 <code>juicefs status</code> 或者 <code>juicefs destroy</code> 无法看到 v1.0 beta3 的会话，新版客户端可以看到所有会话。</p> 
<h3>SQL 表结构调整，支持非 UTF-8 编码文件名</h3> 
<p>为了更好地支持非 UTF-8 编码的文件名，在 JuiceFS v1.0 beta3 中修改了关系型数据库的表结构。</p> 
<p>对于正在使用 MySQL、MariaDB、PostgreSQL 的用户，如果需要让已有的文件系统支持非 UTF-8 编码的文件名，需要手动修改表结构，详情请<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fjuicefs.com%2Fdocs%2Fzh%2Fcommunity%2Frelease_notes" target="_blank">参考文档</a>。</p> 
<h2>修复的 Bug</h2> 
<ol> 
 <li>修复了元数据备份失败时可能导致部分内存未及时释放问题。</li> 
 <li>修复了使用 SQL 作为元数据引擎时，扫描函数返回结果可能不正确问题。</li> 
 <li>修复了使用 <code>juicefs load</code> 命令加载元数据时部分计数器可能统计不准确问题。</li> 
 <li>修复了对象存储开启多 buckets 时，扫描对象列表结果不正确问题。</li> 
 <li>修复了使用 Ceph RADOS 做对象存储时，对象数过多时扫描卡住问题。</li> 
</ol> 
<p>详细的 Bug 修复列表请看 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fjuicedata%2Fjuicefs%2Freleases%2Ftag%2Fv1.0.0-beta3" target="_blank">https://github.com/juicedata/juicefs/releases/tag/v1.0.0-beta3</a></p> 
<p>快去下载体验吧，<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fjuicedata%2Fjuicefs%2Freleases%2Ftag%2Fv1.0.0-beta3" target="_blank">Juicedata/JuiceFS</a></p>
                                        </div>
                                      
</div>
            