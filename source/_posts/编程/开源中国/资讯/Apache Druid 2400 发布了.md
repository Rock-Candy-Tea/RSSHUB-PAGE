
---
title: 'Apache Druid 24.0.0 发布了'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=6730'
author: 开源中国
comments: false
date: Mon, 19 Sep 2022 07:21:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=6730'
---

<div>   
<div class="content">
                                                                                            <p>Apache Druid <span style="color:#1a1a1a"> 是一个分布式的、支持实时多维 OLAP 分析的数据处理系统。它既支持高速的数据实时摄入处理，也支持实时且灵活的多维数据分析查询。因此 Druid 最常用的场景就是大数据背景下、灵活快速的多维 OLAP 分析。</span></p> 
<p><span style="color:#1a1a1a">另外，Druid 还有一个关键的特点：它支持根据时间戳对数据进行预聚合摄入和聚合分析，因此也有用户经常在有时序数据处理分析的场景中用到它。</span></p> 
<p><span style="color:#1a1a1a">目前 </span>Apache Druid 24.0.0 发布了，此版本<span style="color:#24292f">包含来自 67 个贡献者的 300 多个新功能、错误修复、性能增强、文档改进和额外的测试。以下是部分新功能：</span></p> 
<h3><strong>多阶段查询任务引擎</strong></h3> 
<p>Apache Druid 的基于 SQL 的摄取（<span style="color:#24292f">ingestion</span>）使用分布式多阶段查询架构，其中包括一个称名为多阶段查询任务引擎（MSQ 任务引擎）的查询引擎。 MSQ 任务引擎扩展了 Druid 的查询功能，因此可以编写引用外部数据的查询以及使用 SQL INSERT 和 REPLACE 执行摄取。</p> 
<p>从 Druid 24.0.0 开始，使用多阶段查询任务引擎的基于 SQL 的摄取是最推荐的解决方案，同时也仍支持替代摄取解决方案，例如本机批处理和基于 Hadoop 的摄取系统。</p> 
<p>参考：</p> 
<p><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fapache%2Fdruid%2Fpull%2F12524" target="_blank">#12524</a><br> <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fapache%2Fdruid%2Fpull%2F12386" target="_blank">#12386</a><br> <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fapache%2Fdruid%2Fpull%2F12523" target="_blank">#12523</a><br> <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fapache%2Fdruid%2Fpull%2F12589" target="_blank">#12589</a></p> 
<h3><strong>嵌套列</strong></h3> 
<p>Druid 现在支持将嵌套数据结构直接存储在新添加的 COMPLEX<json> 列类型中。 COMPLEX<json> 列以 JSON 格式存储结构化数据的副本，以及用于嵌套文字值（STRING、LONG 和 DOUBLE 类型）的专用内部列和索引。</p> 
<p>参考：</p> 
<p><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fapache%2Fdruid%2Fpull%2F12753" target="_blank">#12753</a><br> <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fapache%2Fdruid%2Fpull%2F12714" target="_blank">#12714</a><br> <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fapache%2Fdruid%2Fpull%2F12753" target="_blank">#12753</a><br> <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fapache%2Fdruid%2Fpull%2F12920" target="_blank">#12920</a></p> 
<h3><strong>更新 Java 支持</strong></h3> 
<p>完全支持 Java 11 ，Java 17 支持得到改进。</p> 
<p><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fapache%2Fdruid%2Fpull%2F12839" target="_blank">#12839</a></p> 
<h2 style="margin-left:0px"><strong>查询引擎更新</strong></h2> 
<h3><strong>更新了列索引和过滤器的查询处理</strong></h3> 
<p>重新设计的列索引非常灵活，允许对各种索引类型进行建模。添加了构建使用更新索引的过滤器的机制，同时还允许其他列实现实现内置索引类型以提供适配器，以在 Druid 提供的当前集合过滤器中使用索引。</p> 
<p><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fapache%2Fdruid%2Fpull%2F12388" target="_blank">#12388</a></p> 
<p><strong>时间过滤运算符</strong></p> 
<p>现在可以使用 Druid SQL 运算符 TIME_IN_INTERVAL 根据时间过滤查询结果。优先使用 TIME_IN_INTERVAL 而不是 SQL BETWEEN 运算符以按时间过滤。详细信息请参阅<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fapache%2Fdruid%2Fblob%2Fdruid-24.0.0%2Fdocs%2Fquerying%2Fsql-scalar.md%23date-and-time-functions" target="_blank">日期和时间函数</a>。</p> 
<p><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fapache%2Fdruid%2Fpull%2F12662" target="_blank">#12662</a></p> 
<h3><strong>Null 值和“in”过滤器</strong></h3> 
<p>如果<code>values</code>数组包含<code>null</code>，则“in”过滤器匹配空值。与不匹配空值的 SQL IN 过滤器不同。</p> 
<p>有关详细信息，请参阅<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fapache%2Fdruid%2Fblob%2Fdruid-24.0.0%2Fdocs%2Fquerying%2Ffilters.md" target="_blank"> 询过滤器</a>和 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fapache%2Fdruid%2Fblob%2Fdruid-24.0.0%2Fdocs%2Fquerying%2Fsql-data-types.md" target="_blank">SQL 数据类型</a>。<br> <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fapache%2Fdruid%2Fpull%2F12863" target="_blank">#12863</a></p> 
<h3><strong>搜索查询中的虚拟列</strong></h3> 
<p>以前，<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fapache%2Fdruid%2Fblob%2Fdruid-24.0.0%2Fdocs%2Fquerying%2Fsearchquery.md" target="_blank">搜索查询</a>只能搜索数据源中存在的维度，现在支持将<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fapache%2Fdruid%2Fblob%2Fdruid-24.0.0%2Fdocs%2Fquerying%2Fvirtual-columns.md" target="_blank">虚拟列</a>作为查询中的参数。</p> 
<p><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fapache%2Fdruid%2Fpull%2F12720" target="_blank">#12720</a></p> 
<h3><strong>在 __time 上优化简单的 MIN / MAX SQL 查询</strong></h3> 
<p>像现在这样的简单查询<code>select max(__time) from ds</code>作为<code>timeBoundary</code>查询运行，以利用段中的时间维度排序。可以设置功能标志来启用此功能。</p> 
<p><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fapache%2Fdruid%2Fpull%2F12472" target="_blank">#12472</a><br> <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fapache%2Fdruid%2Fpull%2F12491" target="_blank">#12491</a></p> 
<h3><strong>字符串聚合结果</strong></h3> 
<p>第一个/最后一个字符串聚合器现在仅根据值进行比较。以前，第一个/最后一个字符串聚合器的值首先根据<code>_time</code>列进行比较，然后再根据值进行比较。</p> 
<p>如果有现有查询并希望继续使用<code>_time</code>列和值，请更新查询，以使用 ORDER BY MAX(timeCol)。</p> 
<p><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fapache%2Fdruid%2Fpull%2F12773" target="_blank">#12773</a></p> 
<h3><strong>Jackson 序列化</strong></h3> 
<p>引入并实现了新的辅助函数<code>JacksonUtils</code>以实现 <code>SerializerProvider</code>对象的重用。</p> 
<p>此外，默认情况下禁用了对 <code>GroupByQueryToolChest</code> 基于映射的行的向后兼容性 ，这消除了复制重量级<code>ObjectMapper</code>. 引入了一个配置选项，允许管理员显式启用向后兼容性。</p> 
<p><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fapache%2Fdruid%2Fpull%2F12468" target="_blank">#12468</a></p> 
<h3><strong>更新了 IPAddress Java 库</strong></h3> 
<p>添加了一个新的 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fseancfoley%2FIPAddress" target="_blank">IPAddress</a> Java 库依赖项来处理 IP 地址，该库包括 IPv6 支持，此外迁移了 IPv4 函数以使用新库。</p> 
<p><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fapache%2Fdruid%2Fpull%2F11634" target="_blank">#11634</a></p> 
<p> </p> 
<p>其他还包括大量性能改进，这是一个大型版本，更多详情请查看<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fapache%2Fdruid%2Freleases" target="_blank">更新公告</a>。</p> 
<p> </p>
                                        </div>
                                      
</div>
            