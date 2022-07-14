
---
title: '版本通告｜Apache Doris 1.1 Release 版本正式发布！'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/de4a669674ea45b685eff2a068685dbc~tplv-k3u1fbpfcp-zoom-1.image'
author: 开源中国
comments: false
date: Thu, 14 Jul 2022 14:59:00 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/de4a669674ea45b685eff2a068685dbc~tplv-k3u1fbpfcp-zoom-1.image'
---

<div>   
<div class="content">
                                                                    
                                                        <blockquote> 
 <p>以下内容源自 Apache Doris 官网（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdoris.apache.org%2F" target="_blank">https://doris.apache.org/</a> ），复制到浏览器打开。</p> 
</blockquote> 
<p>亲爱的社区小伙伴们，我们很高兴地宣布，Apache Doris 在 2022 年 7 月 14 日迎来 1.1 Release 版本的正式发布！<strong>这是 Apache Doris 正式从 Apache 孵化器毕业后并成为 Apache 顶级项目后发布的第一个 Release 版本。</strong></p> 
<p>在 1.1 版本中，有 <strong>90</strong> 位 Contributor 为 Apache Doris 提交了超过 <strong>450</strong> 项优化和修复，感谢每一个让 Apache Doris 变得更好的你！</p> 
<p>在 1.1 版本中，我们实现了计算层和存储层的全面向量化、正式将向量化执行引擎作为稳定功能进行全面启用，所有查询默认通过向量化执行引擎来执行，<strong>性能较之前版本有 3-5 倍的巨大提升。</strong></p> 
<p>在 1.1 版本中，增加了直接访问 Apache Iceberg 外部表的能力，支持对 Doris 和 Iceberg 中的数据进行联邦查询，扩展了 Apache Doris 在数据湖上的分析能力；在原有的 LZ4 基础上增加了 ZSTD 压缩算法，<strong>进一步提升了数据压缩率；修复了诸多之前版本存在的性能与稳定性问题，使系统稳定性得到大幅提升。</strong></p> 
<p>欢迎大家下载使用！</p> 
<p><strong>代码仓库：</strong></p> 
<p><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fapache%2Fincubator-doris" target="_blank">https://github.com/apache/incubator-doris</a></p> 
<p><strong>下载地址：</strong></p> 
<p><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdoris.apache.org%2Fdownloads%2Fdownloads.html" target="_blank">https://doris.apache.org/downloads/downloads.html</a></p> 
<p><strong>源码地址：</strong></p> 
<p><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fapache%2Fdoris%2Freleases%2Ftag%2F1.1.0-rc05" target="_blank">https://github.com/apache/doris/releases/tag/1.1.0-rc05</a></p> 
<h1>升级说明</h1> 
<h2>向量化执行引擎默认开启</h2> 
<p>在 Apache Doris 1.0 版本中，我们引入了向量化执行引擎作为实验性功能。用户需要在执行 SQL 查询手工开启，通过 set batch_size = 4096 和 <code>set enable_vectorized_engine = true</code> 配置 session 变量来开启向量化执行引擎。</p> 
<p>在 1.1 版本中，我们<strong>正式将向量化执行引擎作为稳定功能进行了全面启用</strong>，session 变量<code>enable_vectorized_engine</code>默认设置为 true，无需用户手工开启，所有查询默认通过向量化执行引擎来执行。</p> 
<h2>BE 二进制文件更名</h2> 
<p>BE 二进制文件从原有的 <strong>palo_be 更名为 doris_be</strong> ，如果您以前依赖进程名称进行集群管理和其他操作，请注意修改相关脚本。</p> 
<h2>Segment 存储格式升级</h2> 
<p>Apache Doris 早期版本的存储格式为 Segment V1，在 0.12 版本中我们实现了新的存储格式 Segment V2 ，引入了 Bitmap 索引、内存表、Page Cache、字典压缩以及延迟物化等诸多特性。从 0.13 版本开始，新建表的默认存储格式为 Segment V2，与此同时也保留了对 Segment V1 格式的兼容。</p> 
<p>为了保证代码结构的可维护性、降低冗余历史代码带来的额外学习及开发成本，我们决定从<strong>下一个版本起不再支持 Segment v1 存储格式</strong>，预计在 Apache Doris 1.2 版本中将删除这部分代码，还请所有仍在使用 Segment V1 存储格式的用户务必在 1.1 版本中完成数据格式的转换。</p> 
<p><strong>操作手册请参考：</strong></p> 
<p><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdoris.apache.org%2Fzh-CN%2F1.0%2Fadministrator-guide%2Fsegment-v2-usage.html" target="_blank">https://doris.apache.org/zh-CN/1.0/administrator-guide/segment-v2-usage.html</a></p> 
<h2>正常升级</h2> 
<p>按照官网上的<strong>集群升级文档</strong>进行滚动升级，可参考：</p> 
<p><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdoris.apache.org%2Fzh-CN%2Fdocs%2Fadmin-manual%2Fcluster-management%2Fupgrade.html" target="_blank">https://doris.apache.org/zh-CN/docs/admin-manual/cluster-management/upgrade.html</a></p> 
<h1>重要功能</h1> 
<h2><strong>支持数据随机分布 [实验性功能]</strong></h2> 
<p><strong>Issue/PR：</strong> #8259 #8041</p> 
<p>在某些场景中（例如日志分析类场景），用户可能无法找到一个合适的分桶键来避免数据倾斜，因此需要由系统提供额外的分布方式来解决数据倾斜的问题。</p> 
<p>因此通过在建表时可以不指定具体分桶键，<strong>选择使用随机分布对数据进行分桶</strong><code>DISTRIBUTED BY random BUCKET number</code>，数据导入时将会随机写入单个 Tablet ，以<strong>减少加载过程中的数据扇出，并减少资源开销、提升系统稳定性。</strong></p> 
<h2><strong>支持创建 Iceberg 外部表 [实验性功能]</strong></h2> 
<p><strong>Issue/PR：</strong> #7391 #7981 #8179</p> 
<p>Iceberg 外部表为 Apache Doris 提供了直接访问存储在 Iceberg 数据的能力。通过 Iceberg 外部表可以实现对本地存储和 Iceberg 存储的数据进行联邦查询，省去繁琐的数据加载工作、简化数据分析的系统架构，并进行更复杂的分析操作。</p> 
<p><strong>在 1.1 版本中，Apache Doris 支持了创建 Iceberg 外部表并查询数据，并支持通过 REFRESH 命令实现 Iceberg 数据库中所有表 Schema 的自动同步。</strong></p> 
<h2><strong>增加ZSTD压缩算法</strong></h2> 
<p><strong>Issue/PR：</strong> #8923 #9747</p> 
<p>目前 Apache Doris 中数据压缩方法是系统统一指定的，默认为 LZ4。针对部分对数据存储成本敏感的场景，例如日志类场景，原有的数据压缩率需求无法得到满足。</p> 
<p>在 1.1 版本中，用户建表时可以在表属性中设置<code>"compression"="zstd"</code> <strong>将压缩方法指定为 ZSTD。</strong> 在 25GB 1.1 亿行的文本日志测试数据中，最高获得了近 <strong>10</strong> 倍的压缩率、较原有压缩率提升了 <strong>53%</strong> ，从磁盘读取数据并进行解压缩的速度提升了 <strong>30%</strong> 。</p> 
<h1>功能优化</h1> 
<h2>更全面的向量化支持</h2> 
<p>在 1.1 版本中，我们实现了<strong>计算层和存储层的全面向量化</strong>，包括：</p> 
<ul> 
 <li>实现了所有内置函数的向量化。</li> 
 <li>存储层实现向量化，并支持了低基数字符串列的字典优化。</li> 
 <li>优化并解决了向量化引擎的大量性能和稳定性问题。</li> 
</ul> 
<p>我们对 Apache Doris 1.1 版本与 0.15 版本分别在 <strong>SSB 和 TPC-H 标准测试数据集上进行了性能测试</strong>：</p> 
<ul> 
 <li>在SSB 测试数据集的全部 13 个 SQL 上，1.1 版本均优于 0.15 版本，整体性能约提升了 <strong>3</strong> 倍，解决了 1.0 版本中存在的部分场景性能劣化问题；</li> 
 <li>在 TPC-H 测试数据集的全部 22 个 SQL 上，1.1 版本均优于 0.15 版本，整体性能约提升了 <strong>4.5</strong> 倍，部分场景性能达到了<strong>10 余倍</strong>的提升；</li> 
</ul> 
<p><img alt="img" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/de4a669674ea45b685eff2a068685dbc~tplv-k3u1fbpfcp-zoom-1.image" referrerpolicy="no-referrer"></p> 
<p>图1 SSB 测试数据集</p> 
<p><img alt="img" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/1044edfbc62640d396238797c24fb28d~tplv-k3u1fbpfcp-zoom-1.image" referrerpolicy="no-referrer"></p> 
<p>图2 TPC-H 测试数据集</p> 
<p><strong>性能测试报告：</strong></p> 
<ul> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdoris.apache.org%2Fzh-CN%2Fdocs%2Fbenchmark%2Fssb.html" target="_blank">https://doris.apache.org/zh-CN/docs/benchmark/ssb.html</a></li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdoris.apache.org%2Fzh-CN%2Fdocs%2Fbenchmark%2Ftpch.html" target="_blank">https://doris.apache.org/zh-CN/docs/benchmark/tpch.html</a></li> 
</ul> 
<h2>Compaction 逻辑优化与实时性保证</h2> 
<p><strong>Issue/PR：</strong> #10153</p> 
<p>在 Apache Doris 中每次 Commit 都会产生一个数据版本，在高并发写入场景下，容易出现因数据版本过多且 Compaction 不及时而导致的 -235 错误，同时查询性能也会随之下降。</p> 
<p><strong>在 1.1 版本中我们引入了 QuickCompaction，</strong> 增加了主动触发式的 Compaction 检查，在数据版本增加的时候主动触发 Compaction，同时通过提升分片元信息扫描的能力，快速发现数据版本过多的分片并触发 Compaction。<strong>通过主动式触发加被动式扫描的方式，彻底解决数据合并的实时性问题。</strong></p> 
<p>同时，针对高频的小文件 Cumulative Compaction，<strong>实现了 Compaction 任务的调度隔离</strong>，防止重量级的 Base Compaction 对新增数据的合并造成影响。</p> 
<p>最后，针对小文件合并，<strong>优化了小文件合并的策略，采用梯度合并的方式</strong>，每次参与合并的文件都属于同一个数据量级，防止大小差别很大的版本进行合并，逐渐有层次的合并，减少单个文件参与合并的次数，能够大幅地节省系统的 CPU 消耗。</p> 
<p><img alt="img" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/3f87a68fc8f746f6a66cd312b7daa43e~tplv-k3u1fbpfcp-zoom-1.image" referrerpolicy="no-referrer"></p> 
<p>在数据上游维持每秒 10w 的写入频率时（20 个并发写入任务、每个作业 5000 行、 Checkpoint 间隔 1s），<strong>1.1 版本表现如下：</strong></p> 
<ul> 
 <li><strong>数据快速合并：</strong> Tablet 数据版本维持在 50 以下，Compaction Score 稳定。相较于之前版本高并发写入时频繁出现的 -235 问题，Compaction 合并效率有 <strong>10</strong> 倍以上的提升。</li> 
 <li><strong>CPU资源消耗显著降低</strong>* *：<strong>针对小文件 Compaction 进行了策略优化，在上述高并发写入场景下，CPU 资源消耗</strong>降低 25%**。</li> 
 <li><strong>查询耗时稳定：</strong> 提升了数据整体有序性，大幅降低查询耗时的波动性，高并发写入时的查询耗时与仅查询时持平，查询性能较之前版本有 <strong>3-4</strong> 倍提升。</li> 
</ul> 
<p><img alt="img" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/16b7255e1aea4a62a995cbdb79a49946~tplv-k3u1fbpfcp-zoom-1.image" referrerpolicy="no-referrer"></p> 
<h2>Parquet 和 ORC 文件的读取效率优化</h2> 
<p><strong>Issue/PR：</strong> #9472</p> 
<p>通过调整 Arrow 参数，利用 Arrow 的多线程读取能力来加速 Arrow 对每个 row_group 的读取，并修改成 SPSC 模型，通过预取来降低等待网络的代价。优化前后对 Parquet 文件导入的性能有 <strong>4～5 倍</strong>的提升。</p> 
<h2>更安全的元数据 Checkpoint</h2> 
<h4>Issue/PR：#9180 #9192</h4> 
<p>通过对元数据检查点后生成的 image 文件进行双重检查和保留历史 image 文件的功能，<strong>解决了 image 文件错误导致的元数据损坏问题。</strong></p> 
<h2>BUG 修复</h2> 
<h2>修复由于缺少数据版本而无法查询数据的问题</h2> 
<p><strong>Issue/PR</strong>* *[严重]**：#9267 #9266</p> 
<p><strong>问题描述</strong>：failed to initialize storage reader. tablet=924991.xxxx, res=-214, backend=xxxx</p> 
<p>该问题是在版本 1.0 中引入的，可能会导致多个副本的数据版本丢失。</p> 
<h2>解决了资源隔离对加载任务的资源使用限制无效的问题</h2> 
<p><strong>Issue/PR[中等]</strong> ：#9492</p> 
<p>在 1.1 版本中， Broker Load 和 Routine Load 将使用具有指定资源标记的 BE 节点进行加载。</p> 
<h2><strong>修复使用</strong> <strong>HTTP BRPC 超过 2GB 传输网络数据包导致数据传输错误的问题</strong></h2> 
<p><strong>Issue/PR[中等]</strong> ：#9770</p> 
<p>在以前的版本中，当通过 BRPC 在后端之间传输的数据超过 2GB 时，可能会导致数据传输错误。</p> 
<h1>其他</h1> 
<h2>禁用 Mini Load</h2> 
<p>Mini Load 与 Stream Load 的导入实现方式完全一致，都是通过 HTTP 协议提交和传输数据，在导入功能支持上 Stream Load 更加完备。</p> 
<p>在 1.1 版本中，默认情况下 Mini Load 接口 /_load 将处于禁用状态，请<strong>统一使用 Stream Load 来替换 Mini Load</strong>。您也可以通过关闭 FE 配置项 disable_mini_load 来重新启用 Mini Load 接口。在版本 1.2 中，将彻底删除 Mini Load 。</p> 
<h2>完全禁用 SegmentV1 存储格式</h2> 
<p>在 1.1 版本中将不再允许新创建 SegmentV1 存储格式的数据，现有数据仍可以继续正常访问。</p> 
<p>您可以使用 ADMIN SHOW TABLET STORAGE FORMAT 语句检查集群中是否仍然存在 SegmentV1 格式的数据，如果存在<strong>请务必通过数据转换命令转换为 SegmentV2。</strong></p> 
<p>在 Apache Doris 1.2 版本中不再支持对 Segment V1 数据的访问，同时 Segment V1 代码将被彻底删除。</p> 
<h2>限制 String 类型的最大长度</h2> 
<p><strong>Issue/PR</strong>：#8567</p> 
<p>String 类型是 Apache Doris 在 0.15 版本中引入的新数据类型，在过去 String 类型的最大长度允许为 2GB。</p> 
<p>在 1.1 版本中，<strong>我们将 String 类型的最大长度限制为 1 MB</strong>，超过此长度的字符串无法再写入，同时不再支持将 String 类型用作表的 Key 列、分区列以及分桶列。已写入的字符串类型可以正常访问。</p> 
<h2>修复 fastjson 相关漏洞</h2> 
<p><strong>Issue/PR</strong>：#9763</p> 
<p>对 Canal 版本进行更新以修复 fastjson 安全漏洞</p> 
<h2>添加了 ADMIN DIAGNOSE TABLET 命令</h2> 
<p><strong>Issue/PR</strong>：#8839</p> 
<p>通过 ADMIN DIAGNOSE TABLET tablet_id 命令可以快速诊断指定 Tablet 的问题。</p> 
<h1>下载使用</h1> 
<h2>下载链接</h2> 
<p><a href="https://www.oschina.net/action/GoToLink?url=http%3A%2F%2Fdoris.apache.org%2Fzh-CN%2Fdownloads%2Fdownloads.html" target="_blank">http://doris.apache.org/zh-CN/downloads/downloads.html</a></p> 
<h2>升级说明</h2> 
<p>您可以从 Apache Doris 1.0 Release 版本和 1.0.x 发行版本升级到 1.1 Release 版本，<strong>升级过程请官网参考文档</strong>。如果您当前是 0.15 Release 版本或 0.15.x 发行版本，可跳过 1.0 版本直接升级至 1.1。</p> 
<p>升级文档：</p> 
<p><a href="https://www.oschina.net/action/GoToLink?url=http%3A%2F%2Fdoris.apache.org%2Fzh-CN%2Finstalling%2Fupgrade.html" target="_blank">http://doris.apache.org/zh-CN/installing/upgrade.html</a></p> 
<h2>更新日志</h2> 
<p>详细 <strong>Release Note</strong> 请查看链接：</p> 
<p><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fapache%2Fdoris%2Fissues%2F9949" target="_blank">https://github.com/apache/doris/issues/9949</a></p> 
<h2>意见反馈</h2> 
<p>如果您遇到任何使用上的问题，欢迎随时通过 GitHub Discussion 论坛或者 Dev 邮件组与我们取得联系。</p> 
<p><strong>GitHub 论坛：</strong></p> 
<p><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fapache%2Fincubator-doris%2Fdiscussions" target="_blank">https://github.com/apache/incubator-doris/discussions</a></p> 
<p><strong>Dev 邮件组：</strong></p> 
<p><a href="https://www.oschina.net/action/GoToLink?url=mailto%3Adev%40doris.apache.org" target="_blank">dev@doris.apache.org</a></p> 
<h1>致谢</h1> 
<p>Apache Doris 1.1 Release 版本的发布离不开所有社区用户的支持，在此<strong>向所有参与版本设计、开发、测试、讨论的社区贡献者们表示感谢</strong>，他们分别是：</p> 
<h2><strong>贡献者名单</strong></h2> 
<p>@adonis0147</p> 
<p>@airborne12</p> 
<p>@amosbird</p> 
<p>@aopangzi</p> 
<p>@arthuryangcs</p> 
<p>@awakeljw</p> 
<p>@BePPPower</p> 
<p>@BiteTheDDDDt</p> 
<p>@bridgeDream</p> 
<p>@caiconghui</p> 
<p>@cambyzju</p> 
<p>@ccoffline</p> 
<p>@chenlinzhong</p> 
<p>@daikon12</p> 
<p>@DarvenDuan</p> 
<p>@dataalive</p> 
<p>@dataroaring</p> 
<p>@deardeng</p> 
<p>@Doris-Extras</p> 
<p>@emerkfu</p> 
<p>@EmmyMiao87</p> 
<p>@englefly</p> 
<p>@Gabriel39</p> 
<p>@GoGoWen</p> 
<p>@gtchaos</p> 
<p>@HappenLee</p> 
<p>@hello-stephen</p> 
<p>@Henry2SS</p> 
<p>@hewei-nju</p> 
<p>@hf200012</p> 
<p>@jacktengg</p> 
<p>@jackwener</p> 
<p>@Jibing-Li</p> 
<p>@JNSimba</p> 
<p>@kangshisen</p> 
<p>@Kikyou1997</p> 
<p>@kylinmac</p> 
<p>@Lchangliang</p> 
<p>@leo65535</p> 
<p>@liaoxin01</p> 
<p>@liutang123</p> 
<p>@lovingfeel</p> 
<p>@luozenglin</p> 
<p>@luwei16</p> 
<p>@luzhijing</p> 
<p>@mklzl</p> 
<p>@morningman</p> 
<p>@morrySnow</p> 
<p>@nextdreamblue</p> 
<p>@Nivane</p> 
<p>@pengxiangyu</p> 
<p>@qidaye</p> 
<p>@qzsee</p> 
<p>@SaintBacchus</p> 
<p>@SleepyBear96</p> 
<p>@smallhibiscus</p> 
<p>@spaces-X</p> 
<p>@stalary</p> 
<p>@starocean999</p> 
<p>@steadyBoy</p> 
<p>@SWJTU-ZhangLei</p> 
<p>@Tanya-W</p> 
<p>@tarepanda1024</p> 
<p>@tianhui5</p> 
<p>@Userwhite</p> 
<p>@wangbo</p> 
<p>@wangyf0555</p> 
<p>@weizuo93</p> 
<p>@whutpencil</p> 
<p>@wsjz</p> 
<p>@wunan1210</p> 
<p>@xiaokang</p> 
<p>@xinyiZzz</p> 
<p>@xlwh</p> 
<p>@xy720</p> 
<p>@yangzhg</p> 
<p>@Yankee24</p> 
<p>@yiguolei</p> 
<p>@yinzhijian</p> 
<p>@yixiutt</p> 
<p>@zbtzbtzbt</p> 
<p>@zenoyang</p> 
<p>@zhangstar333</p> 
<p>@zhangyifan27</p> 
<p>@zhannngchen</p> 
<p>@zhengshengjun</p> 
<p>@zhengshiJ</p> 
<p>@zingdle</p> 
<p>@zuochunwei</p> 
<p>@zy-kkk</p> 
<p><img alt="img" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/de082aef6b10415593c64186af6f1b30~tplv-k3u1fbpfcp-zoom-1.image" referrerpolicy="no-referrer"></p> 
<p><img alt="img" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/94d4aeeaae0449d0949060569273001f~tplv-k3u1fbpfcp-zoom-1.image" referrerpolicy="no-referrer"></p> 
<p>SelectDB 是一家开源技术公司，致力于为 Apache Doris 社区提供一个由全职工程师、产品经理和支持工程师组成的团队，繁荣开源社区生态，打造实时分析型数据库领域的国际工业界标准。基于 Apache Doris 研发的新一代云原生实时数仓 SelectDB，运行于多家云上，为用户和客户提供开箱即用的能力。</p> 
<p><strong>相关链接：</strong></p> 
<p>SelectDB 官方网站：</p> 
<p><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fselectdb.com" target="_blank">https://selectdb.com</a></p> 
<p>Apache Doris 官方网站：</p> 
<p><a href="https://www.oschina.net/action/GoToLink?url=http%3A%2F%2Fdoris.apache.org" target="_blank">http://doris.apache.org</a></p> 
<p>Apache Doris Github：</p> 
<p><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fapache%2Fdoris" target="_blank">https://github.com/apache/doris</a></p> 
<p>Apache Doris 开发者邮件组：</p> 
<p><a href="https://www.oschina.net/action/GoToLink?url=mailto%3Adev%40doris.apache.org" target="_blank">dev@doris.apache.org</a></p>
                                        </div>
                                      
</div>
            