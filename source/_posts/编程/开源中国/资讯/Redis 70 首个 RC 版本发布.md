
---
title: 'Redis 7.0 首个 RC 版本发布'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=3740'
author: 开源中国
comments: false
date: Fri, 11 Feb 2022 07:16:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=3740'
---

<div>   
<div class="content">
                                                                                            <p>Redis 7.0 首个 RC 版已发布了一段时间。新版本包含多个面向用户的新功能、显着的性能优化和许多其他改进。与此同时还引入了可能会破坏兼容性的变更，因此使用者在升级时需要确认是否受影响。</p> 
<p>需要特别注意以下变更：</p> 
<ol> 
 <li>Redis 7 将 AOF 作为多个文件存储在一个文件夹中</li> 
 <li>Redis 7 为 RDB 文件应用了新版本 (version 10) 格式，与旧版本不兼容</li> 
 <li>Redis 7 在加载较旧的 RDB 格式时会动态地将 ziplist 编码的 key 转换为 listpacks。此过程通常发生在从 RDB 加载文件或者主从复制之间，且会增加加载时间</li> 
</ol> 
<h3>新特性</h3> 
<ul> 
 <li><strong>Redis Functions</strong>：使用服务器脚本扩展 Redis 的新方法 (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fredis%2Fredis%2Fissues%2F8693" target="_blank">#8693</a>)<br> see<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fredis.io%2Ftopics%2Ffunctions-intro" target="_blank">https://redis.io/topics/functions-intro</a></li> 
 <li><strong>ACL</strong>：细粒度的基于 key 的权限控制，通过 selectors 支持多种权限规则 (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fredis%2Fredis%2Fpull%2F9974" target="_blank">#9974</a>)<br> see<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fredis.io%2Ftopics%2Facl%23key-permissions" target="_blank">https://redis.io/topics/acl#key-permissions</a><span> </span>and<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fredis.io%2Ftopics%2Facl%23selectors" target="_blank">https://redis.io/topics/acl#selectors</a></li> 
 <li><strong>Cluster</strong>：支持用于分片（特定节点）的发布/订阅功能 (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fredis%2Fredis%2Fpull%2F8621" target="_blank">#8621</a>)<br> see<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fredis.io%2Ftopics%2Fpubsub%23sharded-pubsub" target="_blank">https://redis.io/topics/pubsub#sharded-pubsub</a></li> 
 <li>在大多数情况下对子命令提供一流处理，这可能会对 ACL 类别、INFO 命令统计等造成影响 (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fredis%2Fredis%2Fpull%2F9504" target="_blank">#9504</a>,<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fredis%2Fredis%2Fpull%2F10147" target="_blank">#10147</a>)</li> 
 <li>命令元数据和文档更新 (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fredis%2Fredis%2Fpull%2F10104" target="_blank">#10104</a>)<br> <span>查看 </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fredis.io%2Fcommands%2Fcommand-docs" target="_blank">https://redis.io/commands/command-docs</a>,<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fredis.io%2Ftopics%2Fcommand-tips" target="_blank">https://redis.io/topics/command-tips</a></li> 
 <li><strong>Command key-specs</strong>：为 client 定位 key 参数和 read/write purpose 提供更好的方法<br>  (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fredis%2Fredis%2Fpull%2F8324" target="_blank">#8324</a>,<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fredis%2Fredis%2Fpull%2F10122" target="_blank">#10122</a>,<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fredis%2Fredis%2Fpull%2F10167" target="_blank">#10167</a>)<br> see<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fredis.io%2Ftopics%2Fkey-specs" target="_blank">https://redis.io/topics/key-specs</a></li> 
 <li>使用 Multi-Part AOF 机制避免 AOF 的重写开销 (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fredis%2Fredis%2Fpull%2F9788" target="_blank">#9788</a>)</li> 
 <li><strong>Cluster</strong>：支持主机名，不再是此前的仅支持 IP 地址 (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fredis%2Fredis%2Fpull%2F9530" target="_blank">#9530</a>)</li> 
 <li>优化网络缓冲区的内存开销管理，以及增加当总内存超过限制时删除客户端的选项 (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fredis%2Fredis%2Fpull%2F8687" target="_blank">#8687</a>)</li> 
 <li><strong>Cluster</strong>：增加断开集群总线连接的机制，以防止缓冲区不受控制的增长 (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fredis%2Fredis%2Fpull%2F9774" target="_blank">#9774</a>)</li> 
 <li><strong>AOF</strong>：增加时间戳注解和对基于时间点恢复的支持 (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fredis%2Fredis%2Fpull%2F9326" target="_blank">#9326</a>)</li> 
 <li><strong>Lua</strong>：支持 EVAL 脚本中的 Function flags (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fredis%2Fredis%2Fpull%2F10126" target="_blank">#10126</a>)<br> see<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fredis.io%2Ftopics%2Feval-intro%23eval-flags" target="_blank">https://redis.io/topics/eval-intro#eval-flags</a></li> 
 <li><strong>Lua</strong>：RESP3 协议响应 Verbatim 和 Big-Number 类型 (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fredis%2Fredis%2Fpull%2F9202" target="_blank">#9202</a>)</li> 
 <li><strong>Lua</strong>：可通过 redis.REDIS_VERSION, redis.REDIS_VERSION_NUM 命令获取 Redis 版本 (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fredis%2Fredis%2Fpull%2F10066" target="_blank">#10066</a>)</li> 
</ul> 
<h3>性能和资源利用改进</h3> 
<ul> 
 <li><span style="color:#4a4a4a">集群模式下显著优化延迟并降低内存开销 </span>(<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fredis%2Fredis%2Fpull%2F9356" target="_blank">#9356</a>)</li> 
 <li><span style="color:#4a4a4a">在具有很多 zset 或 hash key 的场景时降低内存开销 </span>(<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fredis%2Fredis%2Fpull%2F9228" target="_blank">#9228</a>)</li> 
 <li>复制积压缓冲区和主从复制缓冲区使用一个全局共享的缓冲区 (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fredis%2Fredis%2Fpull%2F9166" target="_blank">#9166</a>)</li> 
 <li>减少 copy-on-write 的内存开销 (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fredis%2Fredis%2Fpull%2F8974" target="_blank">#8974</a>)</li> 
 <li><span style="background-color:#ffffff; color:#24292f">释放集群发送缓冲区中未使用的容量 </span>(<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fredis%2Fredis%2Fpull%2F9255" target="_blank">#9255</a>)</li> 
 <li> <p style="margin-left:0; margin-right:0"><span style="color:#4a4a4a">优化内存效率，充分利用客户端结构内存用于回复缓冲区 </span>(<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fredis%2Fredis%2Fpull%2F8968" target="_blank">#8968</a>)</p> </li> 
 <li>在 Hash, List, Zset 中将 ziplist 替换为 listpack (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fredis%2Fredis%2Fpull%2F8887" target="_blank">#8887</a>,<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fredis%2Fredis%2Fpull%2F9366" target="_blank">#9366</a>,<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fredis%2Fredis%2Fpull%2F9740" target="_blank">#9740</a>)</li> 
 <li><span style="background-color:#ffffff; color:#24292f">添加对 list 类型的支持以存储大于 4GB 的元素 </span>(<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fredis%2Fredis%2Fpull%2F9357" target="_blank">#9357</a>)</li> 
 <li>为临时客户端对象添加了一个池，以便在模块操作中重复使用 (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fredis%2Fredis%2Fpull%2F9940" target="_blank">#9940</a>)</li> 
 <li>移除命令参数计数限制，动态增长 argv 缓冲区 (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fredis%2Fredis%2Fpull%2F9528" target="_blank">#9528</a>)</li> 
 <li>优化 list 操作，从更靠近元素的一侧开始查找 (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fredis%2Fredis%2Fpull%2F9454" target="_blank">#9454</a>)</li> 
 <li>改进 fsync 以避免大量写入磁盘 (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fredis%2Fredis%2Fpull%2F9409" target="_blank">#9409</a>)</li> 
 <li>BITSET 和 BITFIELD SET 仅在值实际更改时传播 (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fredis%2Fredis%2Fpull%2F9403" target="_blank">#9403</a>)</li> 
 <li><span style="color:#4a4a4a">降低客户端被模块解锁阻塞时的延时 </span>(<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fredis%2Fredis%2Fpull%2F9593" target="_blank">#9593</a>)</li> 
</ul> 
<p><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fredis%2Fredis%2Freleases%2Ftag%2F7.0-rc1" target="_blank">详情查看 release note</a>。</p>
                                        </div>
                                      
</div>
            