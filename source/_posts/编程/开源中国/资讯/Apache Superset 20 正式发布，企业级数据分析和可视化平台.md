
---
title: 'Apache Superset 2.0 正式发布，企业级数据分析和可视化平台'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://static.oschina.net/uploads/space/2021/0124/185022_RfO0_2720166.jpg'
author: 开源中国
comments: false
date: Mon, 25 Jul 2022 17:26:00 GMT
thumbnail: 'https://static.oschina.net/uploads/space/2021/0124/185022_RfO0_2720166.jpg'
---

<div>   
<div class="content">
                                                                                            <p>Apache Superset 是一款现代化的开源大数据工具，也是企业级商业智能 Web 应用，用于数据探索分析和数据可视化。它提供了简单易用的无代码可视化构建器和声称是最先进的 SQL 编辑器，用户可以使用这些工具快速地构建数据仪表盘。</p> 
<p>Superset 提供了源码、pypi、Docker 等多种安装方式，其文档称，Superset 目前在许多公司被大规模使用。例如，Superset 在 Airbnb 基于 Kubernetes 的生产环境中运行，为每天查看超过 10 万张图表的 600 多名活跃用户提供服务。</p> 
<p><img alt="185022_RfO0_2720166.jpg" src="https://static.oschina.net/uploads/space/2021/0124/185022_RfO0_2720166.jpg" referrerpolicy="no-referrer"></p> 
<p>Apache Superset 将 SQL IDE、数据浏览工具、拖拽式仪表板编辑器和插件组合使用，以构建自定义的可视化效果，支持从许多关系数据库和非关系数据库中创建仪表板，这些数据库包括 SQLite、MySQL，以及 Amazon Redshift、Google BigQuery、Snowflake、Oracle 数据库、IBM DB2 和<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fsuperset.apache.org%2Fdocs%2Fdatabases%2Finstalling-database-drivers" target="_blank">其他各种兼容的数据源</a>，并且可以连接到 Apache Drill 和 Apache Druid。此外，Superset 还适用于云原生场景和 Docker。</p> 
<p><img src="https://static.oschina.net/uploads/space/2022/0725/170702_KVVb_2720166.png" referrerpolicy="no-referrer"></p> 
<p>Apache Superset 2.0 已于近日正式发布。新版本针对用户体验和稳定性带来了重要提升：</p> 
<ul> 
 <li>通过弃用大量旧功能 flag 和代码路径，消除了许多此前积压的技术债</li> 
 <li>统一了产品中许多领域的用户体验</li> 
 <li>在 Explore 面板中添加了水平条形图 (horizontal bar chart) 和改进的可视化选择器等新功能</li> 
 <li>继续优化针对 Databricks、Trino、Pinot 等流行数据库的使用体验</li> 
 <li><em>……</em></li> 
</ul> 
<p><img src="https://static.oschina.net/uploads/space/2022/0725/161143_tZ7B_2720166.jpg" referrerpolicy="no-referrer"></p> 
<p><strong>增强 Visualization Switcher 功能</strong></p> 
<p>在 Explore 的无代码图表构建体验中，用户可以在最常用的可视化类型中快速切换，同时保留所选择的指标和维度。</p> 
<p><img alt src="https://oscimg.oschina.net/oscnet/up-6d04443b8a393ab98e1e60c88e21d855dd1.png" referrerpolicy="no-referrer"></p> 
<p><strong>支持水平条形图</strong></p> 
<p>支持将时间序列条形图的可视化方向从垂直切换到水平。</p> 
<p><img alt src="https://oscimg.oschina.net/oscnet/up-41d0ee258e21e91bbad4d0f22450bf2743d.png" referrerpolicy="no-referrer"></p> 
<p><strong><span style="background-color:#ffffff; color:#24292f">时间序列图表现在支持负值和正值的堆叠</span></strong></p> 
<p><img alt src="https://oscimg.oschina.net/oscnet/up-0e772bb4d19b58e1c64f869f85587c040a9.png" referrerpolicy="no-referrer"></p> 
<p><strong>支持在表格图表中拖放</strong></p> 
<p>表格可视化 (<span style="background-color:#ffffff; color:#333333">Table visualization</span>) 现在支持拖放以重新对列数据进行排列，从而更容易自定义此图表类型。</p> 
<p><img src="https://static.oschina.net/uploads/space/2022/0725/171856_b9cc_2720166.gif" referrerpolicy="no-referrer"></p> 
<p><strong>优化混合图表 (<span style="background-color:#ffffff; color:#333333">Mixed Chart</span>)</strong></p> 
<p>混合图表支持<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fpreset.io%2Fblog%2Fmixed-time-series-charts-tutorial%2F" target="_blank">在单个可视化容器中组合多个图表</a>。混合图表可视化 (<span style="background-color:#ffffff; color:#333333">Mixed Chart visualization</span>) 现在支持高级分析、非时间序列 x 轴等功能。</p> 
<p><img alt src="https://oscimg.oschina.net/oscnet/up-176d69e9ba29d90fb7c44e0fb47d91e9157.png" referrerpolicy="no-referrer"></p> 
<p><strong><span style="background-color:#ffffff; color:#24292f">支持在 </span>Edit Dashboard <span style="background-color:#ffffff; color:#24292f">模式下创建图表</span></strong></p> 
<p><img alt src="https://oscimg.oschina.net/oscnet/up-d0339598191328964a47c922b87c63e4a8c.png" referrerpolicy="no-referrer"></p> 
<p><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fapache%2Fsuperset%2Ftree%2Fmaster%2FRELEASING%2Frelease-notes-2-0" target="_blank">详情查看 release note</a> 和<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fpreset.io%2Fblog%2Fapache-superset-2-0-release-notes%2F" target="_blank">发布公告</a>。</p>
                                        </div>
                                      
</div>
            