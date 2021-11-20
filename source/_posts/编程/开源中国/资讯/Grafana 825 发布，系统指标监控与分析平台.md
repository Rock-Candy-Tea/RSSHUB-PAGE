
---
title: 'Grafana 8.2.5 发布，系统指标监控与分析平台'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=2660'
author: 开源中国
comments: false
date: Sat, 20 Nov 2021 07:35:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=2660'
---

<div>   
<div class="content">
                                                                    
                                                        <p>Grafana 8.2.5 现已发布。Grafana 是一个功能丰富的指标标准仪表板和图形编辑器，用于分析和监控 Graphite、Elasticsearch、OpenTSDB、Prometheus 和 InfluxDB。</p> 
<p style="color:#000000; margin-left:0; margin-right:0; text-align:start">具体更新内容如下：</p> 
<h4>Bug fixes</h4> 
<ul> 
 <li><strong>Alerting：</strong>修复 Legacy Alerting 中使用 AND 运算符的警报规则的 <span style="background-color:#ffffff; color:#24292f">no data behaviour</span>。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgrafana%2Fgrafana%2Fpull%2F41305" target="_blank">#41305</a></li> 
 <li><strong>Alerting：</strong>修复评估字符串中的指标未正确填充的错误。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgrafana%2Fgrafana%2Fpull%2F41731" target="_blank">#41731</a></li> 
 <li><strong>CloudMonitoring：</strong>忽略 MQL 查询中的最小和最大聚合。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgrafana%2Fgrafana%2Fpull%2F41302" target="_blank">#41302</a></li> 
 <li><strong>Dashboards：</strong> “Copy”不再添加到新的 dashboard titles 中。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgrafana%2Fgrafana%2Fpull%2F41344" target="_blank">#41344</a></li> 
 <li><strong>DataProxy：</strong>修复了当响应是 WebSocket upgrade 时覆盖响应主体的问题。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgrafana%2Fgrafana%2Fpull%2F41364" target="_blank">#41364</a></li> 
 <li><strong>Elasticsearch：</strong>使用在查询编辑器中配置的字段作为 date_histogram 聚合的字段。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgrafana%2Fgrafana%2Fpull%2F41258" target="_blank">#41258</a></li> 
 <li><strong>Explore：</strong>修复在没有 datasource property set 的情况下运行查询。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgrafana%2Fgrafana%2Fpull%2F40805" target="_blank">#40805</a></li> 
 <li><strong>InfluxDB：</strong>修复查询中的数字别名。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgrafana%2Fgrafana%2Fpull%2F41531" target="_blank">#41531</a></li> 
 <li><strong>Plugins：</strong>确保插件设置列表响应一致。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgrafana%2Fgrafana%2Fpull%2F41346" target="_blank">#41346</a></li> 
 <li><strong>Tempo：</strong>修复对 float durations 的验证。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgrafana%2Fgrafana%2Fpull%2F41400" target="_blank"># </a><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fivanahuckova" target="_blank">41400</a></li> 
 <li><strong>Tracing：</strong>显示每个跨度的正确标签。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgrafana%2Fgrafana%2Fpull%2F41473" target="_blank">#41473</a></li> 
</ul> 
<h4>Breaking changes</h4> 
<p style="text-align:start"><strong><span><span><span><span><span style="color:#24292f"><span><span><span><span><span><span><span><span><span><span><span style="background-color:#ffffff"><span><span><span>Fix No Data behaviour in Legacy Alerting</span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></strong></p> 
<ul> 
 <li>Grafana 8.2.5 及更高版本中，此更改修复了在使用 AND 操作符比较两个或多个条件时评估警报规则的一个错误。在 Grafana 8.2.4 及更早的版本中，如果至少有一个（而非全部）条件没有返回数据，此类警报规则将评估为 OK。此更改修复了该错误，因此在 Grafana 8.2.5 中，这些警报规则现在评估为<code>No Data</code>。如果当一个或所有条件返回<code>No Data</code>时，警报应该评估为 OK，那么这可以通过改变<code>If no data or all values are null</code>来实现。然而，这不会保留 8.2.4 中的  old behaviour；即如果至少有一个（但不是全部）条件返回<code>No Data</code>，警报将是 OK；如果所有条件返回<code>No Data</code>，则是<code>No Data</code>。</li> 
</ul> 
<p>更新说明：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgrafana%2Fgrafana%2Freleases%2Ftag%2Fv8.2.5" target="_blank">https://github.com/grafana/grafana/releases/tag/v8.2.5</a></p>
                                        </div>
                                      
</div>
            