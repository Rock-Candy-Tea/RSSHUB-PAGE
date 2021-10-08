
---
title: 'Grafana 8.2.0 发布，系统指标监控与分析平台'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=3634'
author: 开源中国
comments: false
date: Fri, 08 Oct 2021 07:44:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=3634'
---

<div>   
<div class="content">
                                                                    
                                                        <p>Grafana 8.2.0 现已发布。Grafana 是一个功能丰富的指标标准仪表板和图形编辑器，用于分析和监控 Graphite、Elasticsearch、OpenTSDB、Prometheus 和 InfluxDB。</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">具体更新内容如下：</p> 
<h4 style="text-align:start">Features and enhancements</h4> 
<ul> 
 <li><strong>AWS：</strong>更新了 AWS 认证文档。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgrafana%2Fgrafana%2Fpull%2F39236" target="_blank"># </a><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fsunker" target="_blank">39236</a></li> 
 <li><strong>Alerting：</strong>为上游 Prometheus AM 实现添加了对 Alertmanager 数据源的支持。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgrafana%2Fgrafana%2Fpull%2F39775" target="_blank">#39775</a></li> 
 <li><strong>Alerting：</strong>允许标签名称中有更多字符，以便发送通知。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgrafana%2Fgrafana%2Fpull%2F38629" target="_blank">#38629</a></li> 
 <li><strong>Alerting：</strong>使用 /api/v1/rules 端点获取仪表板或面板的警报规则。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgrafana%2Fgrafana%2Fpull%2F39476" target="_blank">#39476</a></li> 
 <li><strong>Annotations：</strong>改进了事件标记的渲染性能。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgrafana%2Fgrafana%2Fpull%2F39984" target="_blank">#39984</a></li> 
 <li><strong>CloudWatch Logs：</strong>跳过日志查询的缓存。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgrafana%2Fgrafana%2Fpull%2F39860" target="_blank">#39860</a></li> 
 <li><strong>Explore：</strong>在 Jaeger、Zipkin 和 Tempo 中的 Node Graph 添加了一个 opt-in 配置。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgrafana%2Fgrafana%2Fpull%2F39958" target="_blank">#39958</a></li> 
 <li><strong>Prometheus：</strong>Metrics browser 现在可以处理带有特殊字符的标签值。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgrafana%2Fgrafana%2Fpull%2F39713" target="_blank">#39713</a></li> 
</ul> 
<h4 style="margin-left:0; margin-right:0; text-align:left">Bug fixes</h4> 
<ul> 
 <li><strong>CodeEditor：</strong>确保触发了提供给组件的最新 onSave 回调。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgrafana%2Fgrafana%2Fpull%2F39835" target="_blank">#39835</a></li> 
 <li><strong>DashboardList/AlertList：</strong>修复缺少的所有文件夹值的问题。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgrafana%2Fgrafana%2Fpull%2F39772" target="_blank">#3977</a></li> 
</ul> 
<h4 style="text-align:start"><span><span><span><span><span style="color:#24292f"><span><span><span><span><span><span><span><span><span><span><span style="background-color:#ffffff"><span><span><span>Plugin development fixes & changes</span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></h4> 
<ul> 
 <li><strong>Plugins：</strong>创建模拟图标组件以防止控制台错误。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgrafana%2Fgrafana%2Fpull%2F39901" target="_blank">#39901</a></li> 
</ul> 
<p>更新说明：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgrafana%2Fgrafana%2Freleases%2Ftag%2Fv8.2.0" target="_blank">https://github.com/grafana/grafana/releases/tag/v8.2.0</a></p>
                                        </div>
                                      
</div>
            