
---
title: 'Grafana 8.1.0-beta1 发布，系统指标监控与分析平台'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=6418'
author: 开源中国
comments: false
date: Sat, 24 Jul 2021 07:18:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=6418'
---

<div>   
<div class="content">
                                                                                            <p>Grafana 8.1.0-beta1 现已发布。Grafana 是一个功能丰富的指标标准仪表板和图形编辑器，用于分析和监控 Graphite、Elasticsearch、OpenTSDB、Prometheus 和 InfluxDB。</p> 
<p>具体更新内容如下：</p> 
<h4><strong>Features and enhancements</strong></h4> 
<ul> 
 <li><strong>Alerting：</strong>添加 Alertmanager 的通知标签</li> 
 <li><strong>Alerting：</strong>添加按钮以停用当前的 Alertmanager 配置</li> 
 <li><strong>Annotation panel：</strong>发布<strong> </strong>annotation panel</li> 
 <li><strong>Annotations：</strong>为内置注释中的标签添加 typeahead 支持</li> 
 <li><strong>AzureMonitor：</strong>为 Azure 服务添加 curated dashboards</li> 
 <li><strong>Elasticsearch：</strong>添加速率聚合</li> 
 <li><strong>Email：</strong>允许配置电子邮件通知的内容类型</li> 
 <li><strong>Explore：</strong>当达到行限制时添加更多元信息</li> 
 <li><strong>Explore：</strong>跟踪视图的 UI 改进</li> 
 <li><strong>Loki：</strong>添加 $__range 变量</li> 
 <li><strong>Loki：</strong>在模板中添加对“label_values(log stream selector, label)”的支持</li> 
 <li><strong>Loki：</strong>在仪表板中添加对临时过滤的支持</li> 
 <li><strong>MySQL Datasource：</strong>添加时区参数</li> 
 <li>......</li> 
</ul> 
<h4>Bug 修复</h4> 
<ul> 
 <li><strong>Alerting：</strong>处理 marshaling Inf 值</li> 
 <li><strong>AzureMonitor：</strong>修复模板变量的宏解析</li> 
 <li><strong>AzureMonitor：</strong>修复对 Microsoft.NetApp/../../volumes 资源的查询</li> 
 <li><strong>AzureMonitor：</strong>请求并连接后续资源页面</li> 
 <li><strong>Datasources：</strong>改进错误消息的错误处理</li> 
 <li><strong>Explore：</strong>更正所有用途的 shift-enter 快捷方式的功能</li> 
 <li><strong>GraphNG：</strong>修复 XYChart 的 Tooltip 模式“All”</li> 
 <li><strong>Plugins：</strong>验证插件签名时忽略符号链接文件夹</li> 
 <li>......</li> 
</ul> 
<h4>Breaking changes</h4> 
<ul> 
 <li>当使用模板变量解析 Elasticsearch 查询响应时，每个字段都会以变量值命名，而不是名称。</li> 
 <li>Azure Monitor 数据源不再支持现有数据源中的指标和日志的不同凭证。要对 Azure Monitor 日志使用不同的凭证，需创建另一个数据源。</li> 
 <li>Log Analytics 工作区的现有 Azure Metrics Logs 查询应向后兼容此更改，不应受到影响。当你第一次编辑和保存面板时，面板将被迁移到使用新的以资源为中心的后端。</li> 
 <li>Application Insights 和 Insights Analytics 查询现在是只读的，不能修改。要更新 Application Insights 查询，用户可以手动将它们重新创建为指标查询，并使用日志重新创建 Insights Analytics。</li> 
</ul> 
<h4>插件开发修复和更改</h4> 
<ul> 
 <li><strong>Toolkit：</strong>改进任务失败时的错误消息。</li> 
</ul> 
<p>详情可查看：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgrafana%2Fgrafana%2Freleases%2Ftag%2Fv8.1.0-beta1" target="_blank">https://github.com/grafana/grafana/releases/tag/v8.1.0-beta1</a></p>
                                        </div>
                                      
</div>
            