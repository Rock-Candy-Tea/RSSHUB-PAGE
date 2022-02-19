
---
title: 'Grafana 8.4.0 发布，系统指标监控与分析平台'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=8679'
author: 开源中国
comments: false
date: Sat, 19 Feb 2022 07:35:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=8679'
---

<div>   
<div class="content">
                                                                                            <p>Grafana 8.4.0 现已发布。Grafana 是一个功能丰富的指标标准仪表板和图形编辑器，用于分析和监控 Graphite、Elasticsearch、OpenTSDB、Prometheus 和 InfluxDB。</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">该版本具体更新内容如下：</p> 
<h4><strong>Features and enhancements</strong></h4> 
<ul> 
 <li><strong>API：</strong>使用 go-swagger 从源代码中提取 OpenAPI 规范。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgrafana%2Fgrafana%2Fpull%2F40528" target="_blank">#40528</a></li> 
 <li><strong>AccessControl：</strong>当用户没有权限时，禁用用户删除和用户更新角色。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgrafana%2Fgrafana%2Fpull%2F43429" target="_blank">#43429</a></li> 
 <li><strong>AccessControl：</strong>为团队提供服务。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgrafana%2Fgrafana%2Fpull%2F43767" target="_blank">#43767</a></li> 
 <li><strong>API：</strong>添加使用情况统计预览端点。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgrafana%2Fgrafana%2Fpull%2F43899" target="_blank">#43899</a></li> 
 <li><strong>Alerting：</strong>将调度程序中的慢查询移动到另一个 goroutine。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgrafana%2Fgrafana%2Fpull%2F44423" target="_blank">#44423</a></li> 
 <li><strong>Alerting：</strong>使用 time.Ticker 代替 ngalert 中的 alerting.Ticker。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgrafana%2Fgrafana%2Fpull%2F44395" target="_blank">#44395</a></li> 
 <li><strong>Alerting：</strong>向警报面板添加自定义分组。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgrafana%2Fgrafana%2Fpull%2F44559" target="_blank">#44559</a></li> 
 <li><strong>Analytics：</strong>将用户 ID 跟踪添加到谷歌分析。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgrafana%2Fgrafana%2Fpull%2F42763" target="_blank">#</a> 42763</li> 
 <li><strong>Angular：</strong>将 AngularJS 插件支持弃用计划添加到文档站点。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgrafana%2Fgrafana%2Fpull%2F45149" target="_blank">#45149</a></li> 
 <li><strong>Auth：</strong>为 auth.jwt 实现 auto_sign_up。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgrafana%2Fgrafana%2Fpull%2F43502" target="_blank">#43502</a></li> 
 <li><strong>Azure Monitor Logs：</strong>在资源选择器中按名称对订阅进行排序。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgrafana%2Fgrafana%2Fpull%2F45228" target="_blank">#45228</a></li> 
 <li><strong>Chore：</strong>在 Grafana 中实现 OpenTelemetry。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgrafana%2Fgrafana%2Fpull%2F42674" target="_blank">#42674</a></li> 
 <li><strong>Cloud Monitoring：</strong>将指标类型添加到指标下拉选项中。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgrafana%2Fgrafana%2Fpull%2F43268" target="_blank">#43268</a></li> 
 <li><strong>CloudWatch：</strong>添加 Data Lifecycle Manager 指标和维度。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgrafana%2Fgrafana%2Fpull%2F43310" target="_blank">#43310</a></li> 
 <li><strong>CloudWatch：</strong>添加缺少的 Elasticache 主机级指标。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgrafana%2Fgrafana%2Fpull%2F43455" target="_blank">#43455</a></li> 
 <li><strong>CloudWatch：</strong>添加所有 ElastiCache Redis 指标。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgrafana%2Fgrafana%2Fpull%2F43336" target="_blank">#43336</a></li> 
 <li><strong>CloudWatch：</strong>添加新的 AWS/ES 指标。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgrafana%2Fgrafana%2Fpull%2F43034" target="_blank">#43034</a></li> 
 <li><strong>Cloudwatch：</strong>为“Metric Search”添加语法突出显示和自动完成功能。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgrafana%2Fgrafana%2Fpull%2F43985" target="_blank">#43985</a></li> 
 <li><strong>Explore：</strong>支持 Prometheus 数据源的示例链接的自定义显示标签。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgrafana%2Fgrafana%2Fpull%2F42732" target="_blank">#42732</a></li> 
 <li><strong>Playlists：</strong>启用共享播放列表的直接链接。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgrafana%2Fgrafana%2Fpull%2F44161" target="_blank">#44161</a></li> 
 <li><strong>SQLStore：</strong>防止并发迁移。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgrafana%2Fgrafana%2Fpull%2F44101" target="_blank">#44101</a></li> 
 <li><strong>Setting：</strong>支持使用 bool 来配置功能切换，而不仅仅是传递数组。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgrafana%2Fgrafana%2Fpull%2F43326" target="_blank">#43326</a></li> 
 <li><strong>TimeSeries：</strong>添加对负 Y 和恒定变换的支持。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgrafana%2Fgrafana%2Fpull%2F44774" target="_blank">#44774</a></li> 
 <li><strong>Transformations：</strong>将“JSON”字段类型添加到 ConvertFieldTypeTransformer。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgrafana%2Fgrafana%2Fpull%2F42624" target="_blank">#42624</a></li> 
</ul> 
<h4><strong><span><span><span><span><span style="color:#24292f"><span><span><span><span><span><span><span><span><span><span><span style="background-color:#ffffff"><span><span><span>Bug 修复</span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></strong></h4> 
<ul> 
 <li><strong>Auth：</strong>保证签名 SigV4 headers 的一致性。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgrafana%2Fgrafana%2Fpull%2F45054" target="_blank">#45054</a></li> 
 <li><strong>CloudWatch：</strong>修复 Namespace 变化时 MetricName resetting。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgrafana%2Fgrafana%2Fpull%2F44165" target="_blank">#44165</a></li> 
 <li><strong>Cloudwatch：</strong>修复了在 Metric Query 中更改 namespace 时重置 metric name 的问题。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgrafana%2Fgrafana%2Fpull%2F44612" target="_blank">#44612</a></li> 
 <li><strong>Instrumentation：</strong>修复验证失败的 HTTP 请求检测。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgrafana%2Fgrafana%2Fpull%2F44234" target="_blank">#44234</a></li> 
 <li><strong>LibraryPanels：</strong>防止长描述和名称遮挡删除按钮。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgrafana%2Fgrafana%2Fpull%2F45190" target="_blank">#45190</a></li> 
 <li><strong>OAuth：</strong>如果 header 包含非字符串值，则修复 ID token 的解析。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgrafana%2Fgrafana%2Fpull%2F44159" target="_blank">#44159</a></li> 
 <li><strong>Panel Edit：</strong>可视化搜索现在可以正确使用特殊字符。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgrafana%2Fgrafana%2Fpull%2F45137" target="_blank">#45137</a></li> 
 <li><strong>Provisioning：</strong>在配置多个组织时修复重复验证。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgrafana%2Fgrafana%2Fpull%2F44151" target="_blank">#44151</a></li> 
 <li><strong>QueryField：</strong>修复插入建议时撤消历史记录的问题（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgrafana%2Fgrafana%2Fissues%2F28656" target="_blank">#28656</a>）。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgrafana%2Fgrafana%2Fpull%2F39114" target="_blank">#39114</a></li> 
 <li><strong>TablePanel：</strong>如果有多个框架和 override active，不要在列前加上框架名称。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgrafana%2Fgrafana%2Fpull%2F45174" target="_blank">#45174</a></li> 
</ul> 
<h4><strong>Deprecations</strong></h4> 
<p style="text-align:start"><span><span><span style="color:#24292f"><span><span><span><span><span><span><span><span><span><span><span><span style="background-color:#ffffff"><span><span><span>AngularJS 插件支持现在处于弃用状态，计划版本 10（2023 年）中进行删除。更多详细信息可查看<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgrafana.com%2Fdocs%2Fgrafana%2Fnext%2Fdevelopers%2Fangular_deprecation%2F" target="_blank">文章</a>。</span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span><span style="background-color:#ffffff; color:#24292f">Issue </span><span><span><span style="color:#24292f"><span><span><span><span><span><span><span><span><span><span><span><span style="background-color:#ffffff"><span><span><span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgrafana%2Fgrafana%2Fissues%2F45149" target="_blank">#45149</a></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></p> 
<p style="text-align:start"><span><span><span style="color:#24292f"><span><span><span><span><span><span><span><span><span><span><span><span style="background-color:#ffffff"><span><span><span>详情可查看更新说明：</span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgrafana%2Fgrafana%2Freleases%2Ftag%2Fv8.4.0" target="_blank">https://github.com/grafana/grafana/releases/tag/v8.4.0</a></p>
                                        </div>
                                      
</div>
            