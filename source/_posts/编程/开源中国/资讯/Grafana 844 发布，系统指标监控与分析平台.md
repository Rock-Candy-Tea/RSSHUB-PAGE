
---
title: 'Grafana 8.4.4 发布，系统指标监控与分析平台'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=78'
author: 开源中国
comments: false
date: Sun, 20 Mar 2022 07:41:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=78'
---

<div>   
<div class="content">
                                                                                            <p>Grafana 是一个用于监控和可观察性的开源平台，可视化来自 Prometheus、Loki、Elasticsearch、InfluxDB、Postgres 等多个来源的指标、日志等。</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">Grafana 8.4.4 正式发布，更新内容如下：</p> 
<h4>功能和改进</h4> 
<ul> 
 <li><strong>Loki：</strong>将 unpack 添加到自动完成建议 ( <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgrafana%2Fgrafana%2Fissues%2F44623" target="_blank">#44623</a> )。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgrafana%2Fgrafana%2Fpull%2F46573" target="_blank">#46573</a></li> 
 <li><strong>Plugins：</strong>允许将函数和类组件用于应用程序插件。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgrafana%2Fgrafana%2Fpull%2F46148" target="_blank">#46148</a></li> 
 <li><strong>TimeSeries：</strong>为图形面板的 transform series override 添加迁移。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgrafana%2Fgrafana%2Fpull%2F46577" target="_blank">#46577</a></li> 
 <li><strong>TimeSeries：</strong>在进行负 Y 转换时保留空值/未定义值。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgrafana%2Fgrafana%2Fpull%2F46584" target="_blank">#46584</a></li> 
</ul> 
<h4><span><span><span><span><span style="color:#24292f"><span><span><span><span><span><span><span><span><span><span><span style="background-color:#ffffff"><span><span><span>Bug 修复</span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></h4> 
<ul> 
 <li><strong>CloudWatch：</strong>使用 aws-sdk-go 的默认 http 客户端。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgrafana%2Fgrafana%2Fpull%2F46370" target="_blank">#46370</a></li> 
 <li><strong>Dashboards：</strong>修复了按行重复且不刷新的问题。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgrafana%2Fgrafana%2Fpull%2F46565" target="_blank">#46565</a></li> 
 <li><strong>Gauge：</strong>当数据链接存在且方向为水平时修复了 blank viz。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgrafana%2Fgrafana%2Fpull%2F46335" target="_blank">#46335</a></li> 
 <li><strong>Search：</strong>使用 postgres 时正确排序结果。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgrafana%2Fgrafana%2Fpull%2F46466" target="_blank">#46466</a></li> 
 <li><strong>TagsInput：</strong>修复标签删除按钮的可访问性问题。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgrafana%2Fgrafana%2Fpull%2F46254" target="_blank">#46254</a></li> 
 <li><strong>TextPanel：</strong>在 markdown 被渲染成 html 后进行清理。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgrafana%2Fgrafana%2Fpull%2F46166" target="_blank">#46166</a></li> 
</ul> 
<p>更新说明：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgrafana%2Fgrafana%2Freleases%2Ftag%2Fv8.4.4" target="_blank">https://github.com/grafana/grafana/releases/tag/v8.4.4</a></p>
                                        </div>
                                      
</div>
            