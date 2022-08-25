
---
title: 'Grafana 9.1.1 发布，系统指标监控与分析平台'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=6498'
author: 开源中国
comments: false
date: Thu, 25 Aug 2022 07:02:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=6498'
---

<div>   
<div class="content">
                                                                                            <p><span style="background-color:#ffffff; color:#333333">Grafana 是一个用于监控和可观察性的开源平台，可视化来自 Prometheus、Loki、Elasticsearch、InfluxDB、Postgres 等多个来源的指标、日志等。</span></p> 
<p><span style="background-color:#ffffff; color:#000000">Grafana v9.1.1 现已发布</span><span style="background-color:#ffffff; color:#333333">，更新内容如下：</span></p> 
<h4><strong><span><span><span><span><span style="color:#24292f"><span><span><span><span><span><span><span><span><span><span><span style="background-color:#ffffff"><span><span><span>Features and enhancements</span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></strong></h4> 
<ul> 
 <li><strong>Cloud Monitoring：</strong>支持 SLO burn rate。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgrafana%2Fgrafana%2Fpull%2F53710" target="_blank">#53710</a></li> 
 <li><strong>Schema：</strong>在 LegendDisplayMode 中恢复“hidde”。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgrafana%2Fgrafana%2Fpull%2F53925" target="_blank">#53925</a></li> 
 <li><strong>Timeseries：</strong>将时区属性名称更改回单数。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgrafana%2Fgrafana%2Fpull%2F53926" target="_blank">#53926</a></li> 
</ul> 
<h4><strong><span><span><span><span><span style="color:#24292f"><span><span><span><span><span><span><span><span><span><span><span style="background-color:#ffffff"><span><span><span>Bug 修复</span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></strong></h4> 
<ul> 
 <li><strong>Alerting：</strong>修复 Microsoft Teams 通知中的链接。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgrafana%2Fgrafana%2Fpull%2F54003" target="_blank">#54003</a></li> 
 <li><strong>Alerting：</strong>修复 Microsoft Teams 的通知。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgrafana%2Fgrafana%2Fpull%2F53810" target="_blank">#53810</a></li> 
 <li><strong>Alerting：</strong>修复 Teams 通知中自适应卡片的宽度。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgrafana%2Fgrafana%2Fpull%2F53996" target="_blank">#53996</a></li> 
 <li><strong>ColorPickerInput：</strong>修复禁用状态下的弹出框。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgrafana%2Fgrafana%2Fpull%2F54000" target="_blank">#54000</a></li> 
 <li><strong>Decimals：</strong>修复 auto decimals，使其对正负值的行为相同。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgrafana%2Fgrafana%2Fpull%2F53960" target="_blank">#53960</a></li> 
 <li><strong>Loki：</strong>修复唯一日志行 ID 生成。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgrafana%2Fgrafana%2Fpull%2F53932" target="_blank">#53932</a></li> 
 <li><strong>Plugins：</strong>修复开发认证指南中的文件扩展名。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgrafana%2Fgrafana%2Fpull%2F53838" target="_blank">#53838</a></li> 
 <li><strong>TimeSeries：</strong>修复 jumping legend 问题。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgrafana%2Fgrafana%2Fpull%2F53671" target="_blank">#53671</a></li> 
 <li><strong>TimeSeries：</strong>修复由 KeyboardPlugin 引起的 viz re-init 时的内存泄漏。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgrafana%2Fgrafana%2Fpull%2F53872" target="_blank">#53872</a> </li> 
</ul> 
<h4><strong><span><span><span><span><span style="color:#24292f"><span><span><span><span><span><span><span><span><span><span><span style="background-color:#ffffff"><span><span><span>Plugin development fixes & changes</span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></strong></h4> 
<ul> 
 <li><strong>TimePicker：</strong>修复了不到一天不显示的相对时间范围。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgrafana%2Fgrafana%2Fpull%2F53975" target="_blank">#53975</a></li> 
 <li><strong>GrafanaUI：</strong>修复 ClipboardButton 以始终保留多行内容。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgrafana%2Fgrafana%2Fpull%2F53903" target="_blank">#53903</a></li> 
</ul> 
<p>更新说明：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgrafana%2Fgrafana%2Freleases%2Ftag%2Fv9.1.1" target="_blank">https://github.com/grafana/grafana/releases/tag/v9.1.1</a> </p> 
<p> </p>
                                        </div>
                                      
</div>
            