
---
title: 'Grafana 8.3.4 发布，系统指标监控与分析平台'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=2691'
author: 开源中国
comments: false
date: Thu, 20 Jan 2022 07:08:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=2691'
---

<div>   
<div class="content">
                                                                                            <p style="margin-left:0px">Grafana 8.3.4 现已发布。Grafana 是一个功能丰富的指标标准仪表板和图形编辑器，用于分析和监控 Graphite、Elasticsearch、OpenTSDB、Prometheus 和 InfluxDB。</p> 
<p style="margin-left:0px">具体更新内容如下：</p> 
<h3><strong>Features and enhancements（特性与增强）</strong></h3> 
<ul> 
 <li><strong>Alerting:</strong> <span style="color:#2e3033">允许配置未就绪的警报管理器</span> <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgrafana%2Fgrafana%2Fpull%2F43063" target="_blank">#43063</a></li> 
 <li><strong>Alerting:</strong> <span style="color:#2e3033">允许自定义谷歌聊天消息 </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgrafana%2Fgrafana%2Fpull%2F43568" target="_blank">#43568</a></li> 
 <li><strong>Alerting:</strong> <span style="color:#2e3033">允许自定义谷歌聊天消息</span> (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgrafana%2Fgrafana%2Fpull%2F43568" target="_blank">#43568</a> 手动反向移植) <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgrafana%2Fgrafana%2Fpull%2F43723" target="_blank">#43723</a></li> 
 <li><strong>AppPlugins:</strong> <span style="color:#2e3033">支持只有默认导航的应用插件 </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgrafana%2Fgrafana%2Fpull%2F43016" target="_blank">#43016</a></li> 
 <li><strong>InfluxDB:</strong> <span style="color:#2e3033">nfluxQL：查询编辑器：跳过元数据查询中的字段</span>. <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgrafana%2Fgrafana%2Fpull%2F42543" target="_blank">#42543</a>, <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgabor" target="_blank">@gabor</a></li> 
 <li><strong>Postgres/MySQL/MSSQL:</strong> 如果用户在 grafana 中取消查询，则取消正在进行的 SQL 查询。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgrafana%2Fgrafana%2Fpull%2F43890" target="_blank">#43890</a></li> 
 <li><strong>Prometheus:</strong> prometheus 数据源迁移后转发 oauth 令牌。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgrafana%2Fgrafana%2Fpull%2F43686" target="_blank">#43686</a></li> 
</ul> 
<h3><strong>Bug fixes（Bug 修复）</strong></h3> 
<ul> 
 <li><strong>Azure Monitor:</strong> 修复了指标下拉列表中的变量插值。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgrafana%2Fgrafana%2Fpull%2F43251" target="_blank">#43251</a></li> 
 <li><strong>Azure Monitor:</strong> 改进了变量查询的错误消息。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgrafana%2Fgrafana%2Fpull%2F43213" target="_blank">#43213</a></li> 
 <li><strong>CloudMonitoring:</strong> 修复了使用 group bys 的损坏的变量查询。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgrafana%2Fgrafana%2Fpull%2F43914" target="_blank">#43914 </a></li> 
 <li><strong>Configuration:</strong> 如果没有活动的 API 密钥，则可以查看过期的 API 密钥。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgrafana%2Fgrafana%2Fpull%2F42452" target="_blank">#42452</a></li> 
 <li><strong>Elasticsearch:</strong> 修复处理单个字段的多个数据链路。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgrafana%2Fgrafana%2Fpull%2F44029" target="_blank">#44029</a></li> 
 <li><strong>ImportDashboard:</strong> 修复了导入仪表板和名称以 uid 结尾的问题。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgrafana%2Fgrafana%2Fpull%2F43451" target="_blank">#43451</a></li> 
 <li><strong>Login:</strong> 页面不再在移动设备上溢出。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgrafana%2Fgrafana%2Fpull%2F43739" target="_blank">#43739</a></li> 
 <li><strong>Plugins:</strong> <span style="color:#2e3033">为核心插件设置后端元数据属性。</span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgrafana%2Fgrafana%2Fpull%2F43349" target="_blank">#43349</a></li> 
 <li><strong>Prometheus:</strong> 用空值填充缺失的步骤。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgrafana%2Fgrafana%2Fpull%2F43622" target="_blank">#43622</a></li> 
 <li><strong>Prometheus:</strong> 修复 $__rate_interval 变量的插值。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgrafana%2Fgrafana%2Fpull%2F44035" target="_blank">#44035</a></li> 
 <li><strong>Prometheus:</strong> 用大括号语法插入变量。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgrafana%2Fgrafana%2Fpull%2F42927" target="_blank">#42927</a></li> 
 <li><strong>Prometheus:</strong> 尊重 http-method 数据源设置。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgrafana%2Fgrafana%2Fpull%2F42753" target="_blank">#42753</a></li> 
 <li><strong>Table:</strong> 修复了隐藏列时，将字段配置应用在错误字段的问题。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgrafana%2Fgrafana%2Fpull%2F43376" target="_blank">#43376</a></li> 
 <li><strong>Toolkit:</strong> 修复在签署私有插件时未正确解析 rootUrls 的错误。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgrafana%2Fgrafana%2Fpull%2F43014" target="_blank">#43014</a></li> 
 <li><strong>Variables:</strong> 修复 Variables 以便将数据源变量添加到临时配置中。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgrafana%2Fgrafana%2Fpull%2F43881" target="_blank">#43881</a></li> 
</ul> 
<h3><strong>Plugin development fixes & changes（插件修复/变更）</strong></h3> 
<ul> 
 <li><strong>Toolkit:</strong> 恢复构建配置，将 tslib 与插件捆绑在一起，以防止插件崩溃。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgrafana%2Fgrafana%2Fpull%2F43556" target="_blank">#43556</a></li> 
</ul> 
<p>更新公告：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgrafana%2Fgrafana%2Freleases%2Ftag%2Fv8.3.4" target="_blank">https://github.com/grafana/grafana/releases/tag/v8.3.4</a></p>
                                        </div>
                                      
</div>
            