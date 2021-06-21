
---
title: 'Grafana 8.0.3 发布，系统指标监控与分析平台'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=3293'
author: 开源中国
comments: false
date: Mon, 21 Jun 2021 07:40:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=3293'
---

<div>   
<div class="content">
                                                                    
                                                        <p>Grafana 8.0.3 现已发布。Grafana 是一个功能丰富的指标标准仪表板和图形编辑器，用于分析和监控 Graphite、Elasticsearch、OpenTSDB、Prometheus 和 InfluxDB。</p> 
<p>具体更新内容如下：</p> 
<p><strong>Features and enhancements</strong></p> 
<ul> 
 <li><strong>Alerting：</strong>如果是 MySQL，则增加 alertmanager_conf 列。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgrafana%2Fgrafana%2Fpull%2F35657" target="_blank">#35657</a></li> 
 <li><strong>Time series/Bar chart panel：</strong>在转换为 plot array 时将无限数字处理为空值。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgrafana%2Fgrafana%2Fpull%2F35638" target="_blank">#35638</a></li> 
 <li><strong>TimeSeries：</strong>确保包含颜色的系列重写被迁移，并在改变面板类型时迁移之前的 fieldConfig。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgrafana%2Fgrafana%2Fpull%2F35676" target="_blank">#35676</a></li> 
 <li><strong>ValueMappings：</strong>改进 singlestat 值映射迁移。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgrafana%2Fgrafana%2Fpull%2F35578" target="_blank">#35578</a></li> 
</ul> 
<p><strong>Bug 修复</strong></p> 
<ul> 
 <li><strong>Annotations：</strong>修复 annotation line 和标记颜色。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgrafana%2Fgrafana%2Fpull%2F35608" target="_blank">#35608</a></li> 
 <li><strong>AzureMonitor：</strong>修复没有默认工作区的 KQL 模板变量查询。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgrafana%2Fgrafana%2Fpull%2F35836" target="_blank">#35836</a></li> 
 <li><strong>CloudWatch/Logs：</strong>修复丢失的日志查询响应数据。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgrafana%2Fgrafana%2Fpull%2F35724" target="_blank">#35724</a></li> 
 <li><strong>Elasticsearch：</strong>使用变量时恢复以前的字段命名策略。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgrafana%2Fgrafana%2Fpull%2F35624" target="_blank">#35624</a></li> 
 <li><strong>LibraryPanels：</strong>修复未找到面板插件时库面板列表中的崩溃。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgrafana%2Fgrafana%2Fpull%2F35907" target="_blank">#35907</a></li> 
 <li><strong>LogsPanel：</strong>修复在仪表板中移动日志面板时性能下降的问题。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgrafana%2Fgrafana%2Fpull%2F35379" target="_blank">#35379</a></li> 
 <li><strong>Loki：</strong>在启用 ANSI coloring 时解析 log levels。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgrafana%2Fgrafana%2Fpull%2F35607" target="_blank">#35607</a></li> 
 <li><strong>MSSQL：</strong>修复仍在执行隐藏查询的问题。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgrafana%2Fgrafana%2Fpull%2F35787" target="_blank">#35787</a></li> 
 <li><strong>PanelEdit：</strong>如果面板具有未知面板插件，则显示未显示的 VisualizationPicker。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgrafana%2Fgrafana%2Fpull%2F35831" target="_blank">#35831</a></li> 
 <li><strong>Plugins:：</strong>修复加载符号链接的插件。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgrafana%2Fgrafana%2Fpull%2F35635" target="_blank">#35635</a></li> 
 <li><strong>Prometheus：</strong>修复了在统计和仪表面板中用名称值替换图例名称的问题。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgrafana%2Fgrafana%2Fpull%2F35863" target="_blank">#35863</a></li> 
 <li><strong>State Timeline：</strong>修复悬停在面板上时的崩溃。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgrafana%2Fgrafana%2Fpull%2F35692" target="_blank">#35692</a></li> 
</ul> 
<p>更新说明：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgrafana%2Fgrafana%2Freleases%2Ftag%2Fv8.0.3" target="_blank">https://github.com/grafana/grafana/releases/tag/v8.0.3</a></p>
                                        </div>
                                      
</div>
            