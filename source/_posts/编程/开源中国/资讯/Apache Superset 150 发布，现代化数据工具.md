
---
title: 'Apache Superset 1.5.0 发布，现代化数据工具'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://oscimg.oschina.net/oscnet/up-4973d1c961e4f2b135895f8d0428f88b53c.png'
author: 开源中国
comments: false
date: Fri, 29 Apr 2022 23:51:00 GMT
thumbnail: 'https://oscimg.oschina.net/oscnet/up-4973d1c961e4f2b135895f8d0428f88b53c.png'
---

<div>   
<div class="content">
                                                                                            <p><span style="background-color:#ffffff; color:#333333">Apache Superset 1.5.0 现已<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fapache%2Fsuperset%2Ftree%2Fmaster%2FRELEASING%2Frelease-notes-1-5" target="_blank">发布</a>。</span><span style="background-color:#ffffff; color:#333333">Apache Superset 是一款现代化的开源数据工具，用于数据探索和数据可视化。它提供了简单易用的无代码可视化构建器和声称是最先进的 SQL 编辑器，用户可以使用这些工具快速地构建数据仪表盘。</span></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><span style="background-color:#ffffff; color:#24292f">Superset 1.5 专注于完善仪表板原生过滤器体验，同时提高性能和稳定性。</span><span><span><span style="color:#24292f"><span><span><span><span><span><span><span><span><span><span><span><span style="background-color:#ffffff"><span><span><span>Superset 1.5 可能是 Superset 版本 1 的最后一个次要版本，并将由 Superset 2.0 接替。1.5 分支引入了 Superset 的长期支持 (LTS) 版本的概念，并且即使在 Superset 2.x 发布后也会收到安全性和其他关键修复。因此，用户可以选择留在 1.5 分支，或者在可用时升级到 2.x。</span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><strong><span><span><span><span><span style="color:#24292f"><span><span><span><span><span><span><span><span><span><span><span style="background-color:#ffffff"><span><span><span>面向用户的功能</span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></strong></p> 
<ul> 
 <li>具有大量 native filters 和图表的复杂仪表板将渲染得更快。可参阅显示复杂仪表板的渲染时间从 11 秒变为 3 秒的视频：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fapache%2Fsuperset%2Fpull%2F19064" target="_blank">#19064</a>。此外，应用过滤器和切换 tab 也更加顺畅。</li> 
 <li>Native Filter Bar 已经过重新设计，同时将“Apply”和“Clear all”按钮移至底部：</li> 
</ul> 
<p><img alt height="327" src="https://oscimg.oschina.net/oscnet/up-4973d1c961e4f2b135895f8d0428f88b53c.png" width="500" referrerpolicy="no-referrer"></p> 
<ul> 
 <li>现在可以使 Native filters 依赖于多个过滤器。这使得可以根据对其他过滤器的选择来限制过滤器中的可用值。</li> 
</ul> 
<p><img alt height="318" src="https://oscimg.oschina.net/oscnet/up-6dd52bc1c7ecf20ba080c561d166443b35a.png" width="500" referrerpolicy="no-referrer"></p> 
<ul> 
 <li>除了能够为 adhoc metrics 和 filters 编写自定义 SQL 之外，列控件现在还具有自定义 SQL 选项卡。这使得可以直接在图表中编写自定义表达式，而无需将它们作为保存的表达式添加到数据集中。</li> 
</ul> 
<p><img alt height="235" src="https://oscimg.oschina.net/oscnet/up-30f41221b80e6840cc08da0832098cbeab9.png" width="500" referrerpolicy="no-referrer"></p> 
<ul> 
 <li>添加了一个新<code>SupersetMetastoreCache</code>功能，可以在 Superset Metastore 中缓存数据，而无需运行像 Redis 或 Memcached 这样的专用缓存。新缓存将默认用于所需缓存，但也可用于缓存图表或其他数据。有关使用新缓存的详细信息，可参阅 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fsuperset.apache.org%2Fdocs%2Finstallation%2Fcache%23caching" target="_blank">文档</a>。</li> 
 <li>以前，具有大量过滤器的 Dashboard 可能会导致错误。Explore 中也存在类似问题。现在 Superset 将 Dashboard 和 Explore 状态存储在缓存中（而不是 URL），消除了臭名昭著的 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fapache%2Fsuperset%2Fissues%2F17086" target="_blank">长 URL 问题</a>。</li> 
 <li>以前指向 Dashboard 和 Explore 页面的永久链接实际上是缩短的 URL，它依赖于存储在 URL 中的状态（参阅上面的长 URL 问题）。此外，链接使用数字 id 并且不检查用户权限，从而可以轻松地遍历存储在元存储中的链接。现在永久链接状态作为 JSON 对象存储在元存储中，从而可以在永久链接中存储任意大的 Dashboard 和 Explore state。此外，使用<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fhashids.org%2F" target="_blank"><code>hashids</code></a>和检查权限对 id 进行编码，使永久链接状态更加安全。</li> 
</ul> 
<p><img alt height="280" src="https://oscimg.oschina.net/oscnet/up-7217f914536d7ce67c2345dcfe177c3a091.png" width="500" referrerpolicy="no-referrer"></p> 
<p style="text-align:start"><strong><span><span><span><span><span style="color:#24292f"><span><span><span><span><span><span><span><span><span><span><span style="background-color:#ffffff"><span><span><span>功能标志</span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></strong></p> 
<ul> 
 <li>添加了一个新功能标志<code>GENERIC_CHART_AXES</code>，可以在 ECharts 时间序列图 ( <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fapache%2Fsuperset%2Fpull%2F17917" target="_blank">#17917</a> ) 上使用非时间 x 轴。启用后，在 ECharts 的折线图、面积图、条形图、阶梯图和散点图的控制面板中添加了一个新的控件“X 轴”，从而可以在这些图表上使用分类或数字的 x 轴。</li> 
</ul> 
<p><img alt height="291" src="https://oscimg.oschina.net/oscnet/up-39f9a4de935260f56879eed378feb632f97.png" width="500" referrerpolicy="no-referrer"></p> 
<p style="text-align:start"><strong>Database Experience</strong></p> 
<ul> 
 <li> <p><span>DuckDB：添加对数据库的支持： <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fapache%2Fsuperset%2Fpull%2F19317" target="_blank">#19317</a></span></p> </li> 
 <li> <p><span>Kusto：添加对 Azure Data Explorer (Kusto) 的支持： <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fapache%2Fsuperset%2Fpull%2F17898" target="_blank">#17898</a></span></p> </li> 
 <li> <p><span>Trino：添加服务器证书支持和新的认证方法： <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fapache%2Fsuperset%2Fpull%2F17593" target="_blank">#17593</a> 和 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fapache%2Fsuperset%2Fpull%2F16346" target="_blank">#16346</a></span></p> </li> 
 <li> <p><span>Microsoft SQL Server (MSSQL)：支持在虚拟表中使用 CTE： <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fapache%2Fsuperset%2Fpull%2F18567" target="_blank">#18567</a></span></p> </li> 
 <li> <p><span>Teradata 和 MSSQL：添加对 TOP 限制语法的支持： <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fapache%2Fsuperset%2Fpull%2F18746" target="_blank">#18746</a> 和 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fapache%2Fsuperset%2Fpull%2F18240" target="_blank">#18240</a></span></p> </li> 
 <li> <p><span>Apache Drill：User impersonation using drill+sadrill： <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fapache%2Fsuperset%2Fpull%2F19252" target="_blank">#19252</a></span></p> </li> 
</ul> 
<p style="text-align:start"><strong>Developer Experience</strong></p> 
<ul> 
 <li>superset-ui 现在已经集成到 Superset 代码库中，按照 SIP-58 的规定，被称为"Monorepo"。这使得与 Superset 一起发布的插件的开发变得相当简单。此外，它使 superset-ui 的发布与 Superset 的官方发布相一致成为可能。</li> 
</ul> 
<p style="text-align:start"><strong>Breaking Changes</strong></p> 
<ul> 
 <li><code>mysqlclient</code>从 v1 升级到 v2： <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fapache%2Fsuperset%2Fpull%2F17556" target="_blank">#17556</a></li> 
 <li>将不再从过滤器值中删除单引号和双引号： <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fapache%2Fsuperset%2Fpull%2F17881" target="_blank">#17881</a></li> 
 <li>以前<code>QUERY_COST_FORMATTERS_BY_ENGINE</code>、<code>SQL_VALIDATORS_BY_ENGINE</code>和 <code>SCHEDULED_QUERIES</code>预计会在<code>config.py</code>文件的 feature flag dictionary 中定义。 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fapache%2Fsuperset%2Fpull%2F15254" target="_blank">#15254</a></li> 
 <li>所有 Superset CLI 命令（init、load_examples 等）都需要设置<code>FLASK_APP</code>环境变量（加载<code>.flaskenv</code>时默认设置）： <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fapache%2Fsuperset%2Fpull%2F17539" target="_blank">#17539</a></li> 
</ul> 
<p> 完整变更日志可访问 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fapache%2Fsuperset%2Fblob%2F1.5%2FCHANGELOG.md" target="_blank">CHANGELOG.MD</a>。</p>
                                        </div>
                                      
</div>
            