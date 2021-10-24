
---
title: 'Grafana 8.2.2 发布，系统指标监控平台'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=6570'
author: 开源中国
comments: false
date: Sun, 24 Oct 2021 00:13:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=6570'
---

<div>   
<div class="content">
                                                                    
                                                        <p><span style="color:#000000">Grafana 8.2.1 现已发布。Grafana 是一个功能丰富的指标标准仪表板和图形编辑器，用于分析和监控 Graphite、Elasticsearch、OpenTSDB、Prometheus 和 InfluxDB。</span></p> 
<h3><strong>功能和增强功能</strong></h3> 
<ul> 
 <li><strong>Annotations：</strong>改进了标签搜索性能。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgrafana%2Fgrafana%2Fpull%2F40567" target="_blank">#40567</a></li> 
 <li><strong>Application： </strong>现在可以配置错误模板的标题。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgrafana%2Fgrafana%2Fpull%2F40310" target="_blank">#40310</a></li> 
 <li><strong>AzureMonitor：</strong>我们从资源过滤器查询中删除了一个限制。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgrafana%2Fgrafana%2Fpull%2F40690" target="_blank">#40690</a></li> 
 <li><strong>Caching：</strong>现在可选缓存大小的指标收集（企业版）。</li> 
 <li><strong>Packaging：</strong>删除了 systemd 中的 ProcSubset 选项，此选项会阻止 Grafana 在 LXC 环境中启动。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgrafana%2Fgrafana%2Fpull%2F40339" target="_blank">#40339</a></li> 
 <li><strong>Prometheus：</strong>删除了指标自动完成限制。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgrafana%2Fgrafana%2Fpull%2F39363" target="_blank">#39363</a></li> 
 <li><strong>Request interceptor：</strong>允许 MSSQL 的命名实例。（企业）</li> 
 <li><strong>Table：</strong>改进了类型图标的样式，使它们与列/字段名称更加不同。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgrafana%2Fgrafana%2Fpull%2F40596" target="_blank">#40596</a></li> 
 <li><strong>ValueMappings：</strong>您现在可以在统计、仪表、条形仪表和饼图可视化中使用值映射。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgrafana%2Fgrafana%2Fpull%2F40612" target="_blank">#40612</a></li> 
</ul> 
<h3><strong>Bug修复</strong></h3> 
<ul> 
 <li><strong>Alerting：</strong>修复 Slack 的 API 发送意外响应时产生的 <span style="color:#24292f"><code>panic</code> </span>。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgrafana%2Fgrafana%2Fpull%2F40721" target="_blank">#40721</a>，</li> 
 <li><strong>Alerting：</strong>使用默认数据源时，“创建警报”按钮现在会出现在仪表面板上。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgrafana%2Fgrafana%2Fpull%2F40334" target="_blank">#40334</a></li> 
 <li><span style="color:#24292f"><strong>Explore</strong></span><strong>：</strong>修复了当 Elasticsearch 日志查询没有返回结果时，<span style="color:#24292f">Explore </span>日志面板消失的问题。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgrafana%2Fgrafana%2Fpull%2F40217" target="_blank">#40217</a></li> 
 <li><strong>Graph：</strong>现在可以在指针悬停时看到注释说明。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgrafana%2Fgrafana%2Fpull%2F40581" target="_blank">#40581</a></li> 
 <li><strong>Logs：</strong>系统现在只有在将行解析为对象时才会使用 JSON 解析器。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgrafana%2Fgrafana%2Fpull%2F40507" target="_blank">#40507</a> </li> 
 <li><strong>Prometheus：</strong>修复了从 Grafana 警报查询时，系统没有重用 TCP 连接的问题。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgrafana%2Fgrafana%2Fpull%2F40349" target="_blank">#40349</a></li> 
 <li><strong>Prometheus：</strong>修复了当用户使用 $__interval min 步长创建查询时导致错误的问题。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgrafana%2Fgrafana%2Fpull%2F40525" target="_blank">#40525</a></li> 
 <li><strong>RowsToFields：</strong>我们修复了系统无法正确解释数值的问题。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgrafana%2Fgrafana%2Fpull%2F40580" target="_blank">#40580</a></li> 
 <li><strong>Scale：</strong>修复了当数据最小值 = 数据最大值时,系统如何处理 NaN 百分比。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgrafana%2Fgrafana%2Fpull%2F40622" target="_blank">#40622</a></li> 
 <li><strong>Table panel：</strong>现在可以创建包含特殊字符的过滤器。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgrafana%2Fgrafana%2Fpull%2F40458" target="_blank"># </a><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fdprokop" target="_blank">40458</a></li> 
</ul> 
<p>更新公告：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgrafana%2Fgrafana%2Freleases%2Ftag%2Fv8.2.2" target="_blank">https://github.com/grafana/grafana/releases/tag/v8.2.2</a></p>
                                        </div>
                                      
</div>
            