
---
title: 'ArangoDB 3.8 GA 发布，图遍历支持加权功能'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://oscimg.oschina.net/oscnet/up-90c9254787ce20c4178a0f7ac53fcd71ce4.png'
author: 开源中国
comments: false
date: Sun, 08 Aug 2021 23:57:00 GMT
thumbnail: 'https://oscimg.oschina.net/oscnet/up-90c9254787ce20c4178a0f7ac53fcd71ce4.png'
---

<div>   
<div class="content">
                                                                                            <p>ArangoDB 3.8 GA 已正式<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.arangodb.com%2F2021%2F07%2Fintroducing-arangodb-3-8-graph-analytics-at-scale%2F" target="_blank">发布</a>，其开发团队称他们在此版本改进了许多来自客户和开源用户的分析用例，增加了新功能，例如 AQL Window 操作、图和 GEO 分析，以及新的 ArangoSearch 功能。</p> 
<p><img alt src="https://oscimg.oschina.net/oscnet/up-90c9254787ce20c4178a0f7ac53fcd71ce4.png" referrerpolicy="no-referrer"></p> 
<p>下载地址：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.arangodb.com%2Fdownload-major%2F" target="_blank">https://www.arangodb.com/download-major/</a></p> 
<p style="text-align:start"><span style="color:#000000"><span style="background-color:#ffffff">下面将介绍部分更新亮点，包括 AQL Window 操作、管道分析器、加权的图遍历功能和 ArangoSearch 中的 Geo 支持。</span></span></p> 
<p><strong><span style="color:#000000"><span style="background-color:#ffffff">AQL Window 操作</span></span></strong></p> 
<p><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.arangodb.com%2Fdocs%2F3.8%2Faql%2Foperations-window.html" target="_blank"><code>WINDOW</code> 关键字</a>可用于相关行的聚合，通常是前一行和/或后一行。</p> 
<p><img alt src="https://oscimg.oschina.net/oscnet/up-0d5274da2117fefa3f664eb7cd359b309f0.png" referrerpolicy="no-referrer"></p> 
<p><span style="color:#333333"><span style="background-color:#ffffff"><strong>ArangoSearch</strong> </span></span><strong><span style="color:#000000"><span style="background-color:#ffffff">管道和 AQL 分析器</span></span></strong></p> 
<p><img alt src="https://oscimg.oschina.net/oscnet/up-45720b3ee616cc4faf8d8534b33628356f1.png" referrerpolicy="no-referrer"></p> 
<p style="text-align:start"><span style="color:#000000"><span style="background-color:#ffffff">ArangoSearch 添加了一种新的<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.arangodb.com%2Fdocs%2F3.8%2Fanalyzers.html%23pipeline" target="_blank">分析器类型<code>"pipeline"</code></a>，用于将多个分析器的效果链接为一个。例如，它可将不区分大小写的搜索的文本规范化与<em>n-</em> gram 标记化相结合，或者在多个临界字符处拆分文本，然后进行词干提取。</span></span></p> 
<p style="text-align:start"><span style="color:#000000"><span style="background-color:#ffffff">此外，新的<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.arangodb.com%2Fdocs%2F3.8%2Fanalyzers.html%23aql" target="_blank">分析器类型</a></span></span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.arangodb.com%2Fdocs%2F3.8%2Fanalyzers.html%23aql" target="_blank"><code>"aql"</code></a><span style="color:#000000"><span style="background-color:#ffffff">能够运行 AQL 查询（存在部分限制）以执行数据操作/过滤。例如，用户可以定义一个 soundex 分析器用于发音相似的术语搜索：</span></span></p> 
<pre><code class="language-sql">arangosh> var a = analyzers.save("soundex", "aql", &#123; queryString: "RETURN SOUNDEX(@param)" &#125;, ["frequency", "norm", "position"]);
</code></pre> 
<p style="text-align:start"><span style="color:#000000"><span style="background-color:#ffffff">请注意，查询不得访问存储引擎。这意味着不会在集合或视图上出现</span></span><code>FOR</code><span style="color:#000000"><span style="background-color:#ffffff">循环，不会使用 DOCUMENT() 函数，也不会使用图遍历。</span></span></p> 
<p><strong><span style="color:#000000"><span style="background-color:#ffffff">加权的图遍历</span></span></strong></p> 
<p>ArangoDB 3.8 中的<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.arangodb.com%2Fdocs%2F3.8%2Faql%2Fgraphs-traversals.html" target="_blank">图遍历</a>支持新的遍历类型<code>"weighted"</code>，它通过增加权重来枚举路径。</p> 
<pre><code class="language-sql">FOR x, v, p IN 0..10 OUTBOUND "places/York" GRAPH "kShortestPathsGraph"
  OPTIONS &#123;
    order: "weighted",
    weightAttribute: "travelTime",
    uniqueVertices: "path"
  &#125;</code></pre> 
<p><strong><span style="color:#333333"><span style="background-color:#ffffff">ArangoSearch 中增强的 Geo 支持</span></span></strong></p> 
<p>ArangoDB 3.8 通过 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.arangodb.com%2Fdocs%2F3.8%2Fanalyzers.html%23geojson" target="_blank">GeoJSON</a> 和 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.arangodb.com%2Fdocs%2F3.8%2Fanalyzers.html%23geopoint" target="_blank">GeoPoint</a> 分析器以及相应的 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.arangodb.com%2Fdocs%2F3.8%2Faql%2Ffunctions-arangosearch.html%23geo-functions" target="_blank">ArangoSearch Geo 功能</a>为 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.arangodb.com%2Fdocs%2F3.8%2Faql%2Ffunctions-arangosearch.html%23geo-functions" target="_blank">ArangoSearch</a> 添加了 Geo 支持：</p> 
<ul> 
 <li>Geo_Contains()</li> 
 <li>Geo_Distance()</li> 
 <li>Geo_In_Range()</li> 
 <li>Geo_Intersects()</li> 
</ul> 
<p><img alt src="https://oscimg.oschina.net/oscnet/up-568f1092c565b747c975f8a91b1cf072163.png" referrerpolicy="no-referrer"></p> 
<p>其他值得关注的变化：</p> 
<ul> 
 <li>优化 UI 和可视化工具</li> 
 <li>改进 Arangodump</li> 
 <li>改进排序性能</li> 
 <li>针对加密的硬件加速</li> 
 <li>……</li> 
</ul> 
<p><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.arangodb.com%2F2021%2F07%2Fintroducing-arangodb-3-8-graph-analytics-at-scale%2F" target="_blank">详情查看发布公告</a>。</p> 
<hr> 
<p>ArangoDB 是一个开源的分布式原生多模型数据库。</p> 
<p>ArangoDB 原生多模型数据库，指的是兼有图 (graph)、文档 (document)和键/值对 (key/value) 三种数据模型存储软件。其快捷灵活之处在于，它有适用于全部三种数据模型的统一内核和统一数据库查询语言——<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.arangodb.com%2Fwhy-arangodb%2Fsql-aql-comparison%2F" target="_blank">AQL </a>(ArangoDB Query Language)。其可以涵盖全部三种数据模型，还允许在单个查询中混合使用三种数据模型。</p> 
<p><strong>特性</strong></p> 
<ul> 
 <li> <p><strong>多数据模型：</strong>可以灵活的使用 document, graph, key-value 或者他们的组合作为你的数据模型</p> </li> 
 <li> <p><strong>方便的查询：</strong>支持类似 SQL 的查询语法 AQL，或者通过 REST 以及其他查询</p> </li> 
 <li> <p><strong>Ruby 和 JS 扩展：</strong>没有语言范围限制，你可以从前台到后台都使用同一种语言</p> </li> 
 <li> <p><strong>高性能以及低空间占用：</strong>ArangoDB 比其他 NoSQL 都要快，同时占用的空间更小</p> </li> 
 <li> <p><strong>简单易用：</strong>可以在几秒内启动并且使用，同时可以通过图形界面来管理你的 ArangoDB</p> </li> 
 <li> <p><strong>开源且免费：</strong>ArangoDB 遵守 Apache 协议</p> </li> 
</ul>
                                        </div>
                                      
</div>
            