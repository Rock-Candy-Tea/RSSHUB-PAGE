
---
title: 'Grafana 9.1.3 发布，系统指标监控与分析平台'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=7519'
author: 开源中国
comments: false
date: Thu, 08 Sep 2022 07:01:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=7519'
---

<div>   
<div class="content">
                                                                                            <p style="margin-left:0"><span style="color:#333333">Grafana 是一个用于监控和可观察性的开源平台，可视化来自 Prometheus、Loki、Elasticsearch、InfluxDB、Postgres 等多个来源的指标、日志等。</span></p> 
<p style="margin-left:0"><span style="color:#000000">Grafana v9.1.3 现已发布</span><span style="color:#333333">，更新内容如下：</span></p> 
<h4 style="margin-left:0"><span style="color:#24292f"><strong>Features and enhancements</strong></span></h4> 
<ul> 
 <li><strong>API：</strong>不要在数据源错误响应中暴露 user input。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgrafana%2Fgrafana%2Fpull%2F53483" target="_blank">#53483</a></li> 
 <li><strong>Alerting：</strong>写入和删除多个警报实例。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgrafana%2Fgrafana%2Fpull%2F54072" target="_blank">#54072</a></li> 
 <li><strong>Library Panel：</strong>允许在弃用时删除它们。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgrafana%2Fgrafana%2Fpull%2F54662" target="_blank">#54662</a></li> 
 <li><strong>Plugins Catalog：</strong>允许使用特殊字符过滤插件。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgrafana%2Fgrafana%2Fpull%2F54474" target="_blank">#54474</a></li> 
</ul> 
<h4><span style="color:#24292f"><strong>Bug 修复</strong></span></h4> 
<ul> 
 <li><strong>Alerting：</strong>修复设置自定义通知 policy group 时的 UI 错误。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgrafana%2Fgrafana%2Fpull%2F54607" target="_blank">#54607</a></li> 
 <li><strong>AppRootPage：</strong>修复了在两个应用插件页面之间导航的问题。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgrafana%2Fgrafana%2Fpull%2F54519" target="_blank">#54519</a></li> 
 <li><strong>Correlations：</strong>使用正确的回退处理程序。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgrafana%2Fgrafana%2Fpull%2F54511" target="_blank">#54511</a></li> 
 <li><strong>修复：</strong> RBAC 防止删除空快照 ( <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgrafana%2Fgrafana%2Fpull%2F54385" target="_blank">#54385</a> )。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgrafana%2Fgrafana%2Fpull%2F54510" target="_blank">#54510</a></li> 
 <li><strong>LibraryElements：</strong>修复在 MySQL 下无法删除 library panels 的问题。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgrafana%2Fgrafana%2Fpull%2F54600" target="_blank">#54600</a></li> 
 <li><strong>Metrics：</strong>修复<code>grafana_database_conn_*</code>metrics，并添加新的<code>go_sql_stats_*</code>metrics 作为最终替换。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgrafana%2Fgrafana%2Fpull%2F54405" target="_blank">#54405</a></li> 
 <li><strong>TestData DB：</strong>修复数据类型字段设置为随机时不显示节点图的问题。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgrafana%2Fgrafana%2Fpull%2F54298" target="_blank">#54298</a></li> 
</ul> 
<h3><span style="color:#24292f">弃用</span></h3> 
<p><span style="color:#24292f"><code>grafana_database_conn_*</code>metrics 已弃用，并将在 Grafana 的未来版本中删除。需改用<code>go_sql_stats_*</code>metrics 来代替。Issue </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgrafana%2Fgrafana%2Fissues%2F54405" target="_blank"><span style="color:#24292f">#54405</span></a></p> 
<p><span style="color:#24292f">更新说明：</span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgrafana%2Fgrafana%2Freleases%2Ftag%2Fv9.1.3" target="_blank">https://github.com/grafana/grafana/releases/tag/v9.1.3</a></p>
                                        </div>
                                      
</div>
            