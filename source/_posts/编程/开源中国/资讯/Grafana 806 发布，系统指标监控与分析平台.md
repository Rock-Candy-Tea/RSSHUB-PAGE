
---
title: 'Grafana 8.0.6 发布，系统指标监控与分析平台'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=1472'
author: 开源中国
comments: false
date: Fri, 16 Jul 2021 07:26:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=1472'
---

<div>   
<div class="content">
                                                                    
                                                        <p>Grafana 8.0.6 现已发布。Grafana 是一个功能丰富的指标标准仪表板和图形编辑器，用于分析和监控 Graphite、Elasticsearch、OpenTSDB、Prometheus 和 InfluxDB。</p> 
<p>具体更新内容如下：</p> 
<h4><strong>Features and enhancements</strong></h4> 
<ul> 
 <li><strong>Alerting：</strong>在警报状态更改时添加注释。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgrafana%2Fgrafana%2Fpull%2F36535" target="_blank">#36535</a></li> 
 <li><strong>Alerting：</strong>在标签和注释名称中允许空格。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgrafana%2Fgrafana%2Fpull%2F36549" target="_blank">#36549</a></li> 
 <li><strong>InfluxDB：</strong>改进 InfluxDB 查询结果的图例标签。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgrafana%2Fgrafana%2Fpull%2F36603" target="_blank">#36603</a></li> 
</ul> 
<h4>Bug 修复</h4> 
<ul> 
 <li> <p><strong>Alerting：</strong>通过更改空标签的处理来修复不正确的警报。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgrafana%2Fgrafana%2Fpull%2F36679" target="_blank">#36679</a></p> </li> 
 <li><strong>CloudWatch/Logs：</strong>重新建立 Cloud Watch 警报行为。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgrafana%2Fgrafana%2Fpull%2F36558" target="_blank">#36558</a></li> 
 <li><strong>Dashboard：</strong>避免在 folded panel 中没有 defaults 字段的 fieldConfig 上的迁移中断。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgrafana%2Fgrafana%2Fpull%2F36666" target="_blank">#36666</a></li> 
 <li><strong>DashboardList：</strong>修复了在变量更改后不重新获取 dashboard list 的问题。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgrafana%2Fgrafana%2Fpull%2F36591" target="_blank">#36591</a></li> 
 <li><strong>Database：</strong>修复 MySQL 的隔离级别配置参数格式不正确。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgrafana%2Fgrafana%2Fpull%2F36565" target="_blank">#36565</a></li> 
 <li><strong>InfluxDB：</strong>对 InfluxDB 数据进行正确的标签过滤。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgrafana%2Fgrafana%2Fpull%2F36570" target="_blank">#36570</a></li> 
 <li><strong>Links：</strong>修复导致整个页面重新加载的链接。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgrafana%2Fgrafana%2Fpull%2F36631" target="_blank">#36631</a></li> 
 <li><strong>Live：</strong>修复 InfluxDB metrics 具有不完整或不对称字段集时的 HTTP 错误。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgrafana%2Fgrafana%2Fpull%2F36664" target="_blank">#36664</a></li> 
 <li><strong>Postgres/MySQL/MSSQL：</strong>将时间字段更改为“Time”以进行时间序列查询。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgrafana%2Fgrafana%2Fpull%2F36720" target="_blank">#36720</a></li> 
 <li><strong>Postgres：</strong>修复查询结果中空返回值的处理。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgrafana%2Fgrafana%2Fpull%2F36648" target="_blank">#36648</a></li> 
 <li><strong>Tempo</strong><strong>：</strong>显示十六进制字符串而不是 ID 的 uint。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgrafana%2Fgrafana%2Fpull%2F36471" target="_blank">#3647</a></li> 
 <li><strong>TimeSeries：</strong>改进在工具提示溢出时的工具提示定位。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgrafana%2Fgrafana%2Fpull%2F36440" target="_blank">#36440</a></li> 
 <li><strong>Transformations：</strong>添加“prepare time series”转换器。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgrafana%2Fgrafana%2Fpull%2F36737" target="_blank">#36737</a></li> 
</ul> 
<p>更新说明：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgrafana%2Fgrafana%2Freleases%2Ftag%2Fv8.0.6" target="_blank">https://github.com/grafana/grafana/releases/tag/v8.0.6</a></p>
                                        </div>
                                      
</div>
            