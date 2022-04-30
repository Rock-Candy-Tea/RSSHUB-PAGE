
---
title: 'Grafana 8.5.1 发布，系统指标监控与分析平台'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=7880'
author: 开源中国
comments: false
date: Sat, 30 Apr 2022 07:35:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=7880'
---

<div>   
<div class="content">
                                                                                            <p>Grafana 是一个用于监控和可观察性的开源平台，可视化来自 Prometheus、Loki、Elasticsearch、InfluxDB、Postgres 等多个来源的指标、日志等。</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">Grafana 8.5.1 现已发布，更新内容如下：</p> 
<h4><span><span><span><span><span style="color:#24292f"><span><span><span><span><span><span><span><span><span><span><span style="background-color:#ffffff"><span><span><span>Bug 修复</span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></h4> 
<ul> 
 <li><strong>Azure Monitor：</strong>修复了 metrics query 链接到 Azure Portal 的 space character encoding。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgrafana%2Fgrafana%2Fpull%2F48139" target="_blank">#48139</a></li> 
 <li><strong>CloudWatch：</strong>防止在查询更改时删除日志组。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgrafana%2Fgrafana%2Fpull%2F47994" target="_blank">#47994</a></li> 
 <li><strong>Cloudwatch：</strong>修复变量查询中的模板变量。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgrafana%2Fgrafana%2Fpull%2F48140" target="_blank">#48140</a></li> 
 <li><strong>Explore：</strong>如果通过功能切换禁用，则阻止直接访问 explore。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgrafana%2Fgrafana%2Fpull%2F47714" target="_blank">#</a><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgrafana%2Fgrafana%2Fpull%2F47714" target="_blank">47714</a></li> 
 <li><strong>InfluxDB：</strong>修复无效的无数据警报。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgrafana%2Fgrafana%2Fpull%2F48295" target="_blank">#48295</a></li> 
 <li><strong>Navigation：</strong>防止导航栏在登录时短暂显示。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgrafana%2Fgrafana%2Fpull%2F47968" target="_blank">#47968</a></li> 
 <li><strong>Plugins Catalog：</strong>修复超链接的样式。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgrafana%2Fgrafana%2Fpull%2F48196" target="_blank">#48196</a></li> 
 <li><strong>Table：</strong>修复 filter crashes table。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgrafana%2Fgrafana%2Fpull%2F48258" target="_blank">#48258</a></li> 
 <li><strong>TimeSeries：</strong>正确堆叠缺少数据点的系列。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgrafana%2Fgrafana%2Fpull%2F48321" target="_blank">#48321</a></li> 
</ul> 
<p>更新说明：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgrafana%2Fgrafana%2Freleases%2Ftag%2Fv8.5.1" target="_blank">https://github.com/grafana/grafana/releases/tag/v8.5.1</a></p>
                                        </div>
                                      
</div>
            