
---
title: 'JuiceFS V1.0 RC1 发布，大幅优化 dump_load 命令性能， 深度用户不容错过'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://oscimg.oschina.net/oscnet/up-a2155d96e15c4d3bf25f7c26de73f3422e5.png'
author: 开源中国
comments: false
date: Fri, 17 Jun 2022 10:12:00 GMT
thumbnail: 'https://oscimg.oschina.net/oscnet/up-a2155d96e15c4d3bf25f7c26de73f3422e5.png'
---

<div>   
<div class="content">
                                                                    
                                                        <p style="color:#212529; text-align:start">JuiceFS v1.0 RC1 今天正式发布了！<strong>这个版本中，最值得关注的是对元数据迁移备份工具 dump/load 的优化。</strong></p> 
<p style="color:#212529; text-align:start">这个优化需求来自于某个社区重度用户，这个用户在将亿级数量文件的元数据从 Redis 迁移至 TiKV 时遇到了内存占用过高的问题，我们接到反馈后着手优化，<strong>最终使 dump 所需内存降低 95%，load 所需内存降低 80%。</strong></p> 
<p style="color:#212529; text-align:start">下面，我们来为你详细解读一下 JuiceFS v1.0 RC1 的主要变化。</p> 
<h3 style="margin-left:0; margin-right:0; text-align:start">元数据迁移备份工具 dump/load 命令的优化</h3> 
<p style="color:#212529; text-align:start">现有的<span> </span><code>dump</code><span> </span>命令实现中，会先将元数据引擎中的所有数据加载到客户端内存，形成一个类似只读快照的版本，再按照文件系统树型结构输出到指定文件。得益于 Redis 本身的高速随机读性能，<strong>v1.0 RC1 优化了 Redis 作为元数据引擎时的 dump 流程，不再做整个快照，而是一边预读一边输出，使其所需内存节省 95%，速度提升 100%。</strong>从 SQL 和 TiKV 备份元数据时，会使用单个事务来读数据以确保整个文件系统的一致性。</p> 
<p style="color:#212529; text-align:start">现有的<span> </span><code>load</code><span> </span>命令实现中，会先加载整个元数据集合，再并发导入到元数据引擎中。v1.0 RC1 对所有元数据引擎都做了优化，实现了流式加载功能，同样将其所需内存节省 80%，速度提高 25%。</p> 
<p style="color:#212529; text-align:start">以 Redis 元数据引擎 Dump & Load 一千万文件为例子，v1.0 Beta3 与 v1.0 RC1 的性能对比如下：</p> 
<p><img height="496" src="https://oscimg.oschina.net/oscnet/up-a2155d96e15c4d3bf25f7c26de73f3422e5.png" width="732" referrerpolicy="no-referrer"></p> 
<p><img height="605" src="https://oscimg.oschina.net/oscnet/up-b3a94a22e9d25f5aa9a4ca19cb7a296f6ca.png" width="732" referrerpolicy="no-referrer"></p> 
<p style="color:#212529; text-align:start">很多用户是一开始使用 Redis 作为元数据引擎，随着数据规模的增长，可能需要迁移到 TiKV 或者 SQL 引擎，<strong>这些优化可以保证用户在有上亿文件时仍然能够高效地完成元数据引擎的迁移。</strong></p> 
<p style="color:#212529; text-align:start">后续我们也会详细解析此次 dump/load 命令优化的技术细节，敬请期待。</p> 
<h3 style="margin-left:0; margin-right:0; text-align:start">新增对象存储测试工具 objbench</h3> 
<p style="color:#212529; text-align:start">对象存储是 JuiceFS 的底座，当用户在使用 JuiceFS 遇到问题时经常不确定是 JuiceFS 的问题还是对象存储的问题，所以我们在 v1.0 RC1 中新增<span> </span><code>objbench</code><span> </span>命令来帮助用户验证某个对象存储是否被 JuiceFS 支持以及测试与其共同使用时的性能表现。具体请参考<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Flink.segmentfault.com%2F%3Fenc%3DTz808reZXhnepW7w%252BySHUA%253D%253D.s3XKV%252B6uJS3KOvVH6IwterxK5DiDV04364uIQAKTm0QJLagz9PWs57oS7PXCYYqXjZ%252FMgjZtQHOuNx2L2rVLHIy3yP8%252BMdACeX1lsVik5wjSSrmkZnBzbbm%252FVVeuaDzp" target="_blank">JuiceFS Objbench 文档</a></p> 
<p><img height="461" src="https://oscimg.oschina.net/oscnet/up-52e8fdc56dbbec00086247b755f905bdda7.png" width="732" referrerpolicy="no-referrer"></p> 
<h3 style="margin-left:0; margin-right:0; text-align:start">新支持对接持续性能分析平台 Pyroscope</h3> 
<p style="color:#212529; text-align:start">受 Go 圈技术大牛「鸟窝」的一篇<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Flink.segmentfault.com%2F%3Fenc%3DTZdiP6UNjaI6gqPu2Uxmfw%253D%253D.1LHwITXJo57ARydd61AaWmPZC%252BQLkSesXyFDMSx51PlIGFpcTgJBS2Re9HhrK%252BAMBL833xdDC6O26Z%252BX3KY3HfrIFV8D79woH3jTKPzWYe0%253D" target="_blank">可观测性实践博客</a>的启发，我们想到了在 JuiceFS 中对接持续性能分析工具，一改 JuiceFS 过去只能通过 pprof 这个分析工具肉眼排查的窘境。于是在这个版本中，我们对接了<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Flink.segmentfault.com%2F%3Fenc%3DOOMnbv%252BtEix7Z1Zs8Aq2%252Bg%253D%253D.Qz6VGJYzVIceN0Lt8vkyWHqZRS5kSg742iJeGYi%252Bz0mKRHQn5U7MYe2U1pp%252B947U" target="_blank">Pyroscope</a>（一个开源的持续性能分析平台），通过这个工具，可以记录分析 JuiceFS 的运行状态，例如某段时间内 JuiceFS 代码中函数的 CPU 耗时、对象分配大小等细节数据。请参考<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Flink.segmentfault.com%2F%3Fenc%3D1ClmGBujlLytV4a1uSDEEQ%253D%253D.g%252F3w%252BlP72DndCGRw6W1aJEtVh2eIeOhJgU8XGSJAQn%252BvaVkP%252BnQ3jYL7n%252BO%252B07eJOCWcHgH1lJ1fqhhTxdhk09EvNIKU2aHQcE2w5BnBRX0%253D" target="_blank">使用 Pyroscope 文档</a>了解如何在 JuiceFS 中使用 Pyroscope。</p> 
<p><img height="378" src="https://oscimg.oschina.net/oscnet/up-23ec52f254036f69df5be4b00afaebd339f.png" width="732" referrerpolicy="no-referrer"></p> 
<h3 style="margin-left:0; margin-right:0; text-align:start">其它新增</h3> 
<p style="color:#212529; text-align:start">新支持 SQL 数据库、etcd 做数据存储，具体请参考<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Flink.segmentfault.com%2F%3Fenc%3D1Erww7%252Bs9vkmNKuH7LyUcw%253D%253D.DpqxWb9TnU9KEmABNXNIghVqVdzZJQC4fiJgW9EV8GbTa4dvYH9BHia1N7E1AKQSdCP7ZOidifOHtNlOcr67LGWy0lGE%252FVsKqADHfc7%252Bv3Q%253D" target="_blank">JuiceFS 设置对象存储文档</a>。<br> 新支持<span> </span><code>juicefs info</code><span> </span>命令中根据文件 inode 找到其完整路径</p> 
<blockquote>
 <strong>注意</strong>：查找在 v1.0 RC1 之前创建的文件时，可能出现路径查找不到或者路径不全的情况。
</blockquote> 
<p style="color:#212529; text-align:start">新增<span> </span><code>juicefs rmr</code><span> </span>和<span> </span><code>juicefs warmup</code><span> </span>命令的进度条，并允许中断操作。</p> 
<blockquote>
 <strong>注意</strong>：使用 v1.0 RC1 的 JuiceFS 客户端操作 v1.0 RC1 之前的挂载点时，会显示一直没有进度，但实际命令能够正常执行。
</blockquote> 
<h3 style="margin-left:0; margin-right:0; text-align:start">其它调整</h3> 
<ol> 
 <li>大幅提升 SQL 元数据引擎的稳定性。我们在对 JuiceFS S3 网关进行压力测试的过程中发现了 SQL 元数据引擎在高负载下的一些问题，其中包括所使用的 ORM 框架的几个 bug，都进行了修复并反馈给上游。</li> 
 <li>限制了单次清理回收站和文件缓存的数量，提高了在大规模应用下的稳定性。</li> 
 <li>支持在容器内使用<span> </span><code>juicefs warmup</code><span> </span>命令</li> 
 <li>提升<span> </span><code>juicefs rmr</code><span> </span>命令的性能并减低内存使用</li> 
 <li><code>juicefs sync</code><span> </span>命令也进行了增强，改进了使用免密登录 SSH 拷贝数据的情况，修复了几个 bug。</li> 
 <li>支持通过<span> </span><code>juicefs config</code><span> </span>命令动态修改数据存储的 Access Key 和 Secret Key</li> 
 <li>大量的错误日志描述优化</li> 
</ol> 
<p style="color:#212529; text-align:start">支持通过<span> </span><code>juicefs config</code><span> </span>命令动态修改数据存储的 Access Key 和 Secret Key</p> 
<h3 style="margin-left:0; margin-right:0; text-align:start">Bug 修复</h3> 
<ul> 
 <li>修复了<span> </span><code>juicefs sync</code><span> </span>读取源端文件失败时未打印错误日志的问题</li> 
 <li>修复了只读客户端无法执行<span> </span><code>warmup</code><span> </span>的问题</li> 
 <li>修复了大量删除文件时因 0 号 Slice 导致事务频繁冲突的问题</li> 
 <li>修复了 SQL 类数据库作元数据引擎时，操作事务性未完全保证的问题</li> 
 <li>修复了使用 TiKV 作元数据引擎时，可能因空连接导致 JuiceFS 客户端 panic 的问题</li> 
 <li>修复了 List 元数据备份失败时，可能导致 JuiceFS 客户端 panic 的问题</li> 
</ul> 
<h3 style="margin-left:0; margin-right:0; text-align:start">升级建议</h3> 
<ul> 
 <li>使用 SQL 类数据库作元数据引擎的文件系统：<strong>请务必升级</strong></li> 
 <li>使用其它元数据引擎的文件系统：建议升级</li> 
</ul> 
<p style="color:#212529; text-align:start">介绍了这么多，大家赶紧<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Flink.segmentfault.com%2F%3Fenc%3D2TAM3cE5Gyql0h5CjKGgTw%253D%253D.iAG9PVBV0CICgJTMXVucOFNPj1o51Js5pP4RPF1u1a5NGeDvsgO4Dcz6801gGSw5mPItScoGWoK5unyJEO3%252BRg%253D%253D" target="_blank">点此</a>上手试试吧～</p>
                                        </div>
                                      
</div>
            