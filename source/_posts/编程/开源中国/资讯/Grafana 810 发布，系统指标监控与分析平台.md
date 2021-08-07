
---
title: 'Grafana 8.1.0 发布，系统指标监控与分析平台'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=1597'
author: 开源中国
comments: false
date: Sat, 07 Aug 2021 07:27:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=1597'
---

<div>   
<div class="content">
                                                                    
                                                        <p>Grafana 8.1.0 现已发布。Grafana 是一个功能丰富的指标标准仪表板和图形编辑器，用于分析和监控 Graphite、Elasticsearch、OpenTSDB、Prometheus 和 InfluxDB。</p> 
<p>具体更新内容如下：</p> 
<h4><strong>Features and enhancements</strong></h4> 
<ul> 
 <li><strong>Alerting：</strong>在迁移期间 deduplicate receivers 。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgrafana%2Fgrafana%2Fpull%2F36812" target="_blank">#36812</a></li> 
 <li><strong>ColorPicker：</strong>将颜色显示为 RGBA。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgrafana%2Fgrafana%2Fpull%2F37231" target="_blank">#37231</a></li> 
 <li><strong>Select：</strong>让移植菜单 opt-in，但在任何地方都 opt-in。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgrafana%2Fgrafana%2Fpull%2F37501" target="_blank">#37501</a></li> 
 <li><strong>TimeRangePicker：</strong>提高可访问性。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgrafana%2Fgrafana%2Fpull%2F36912" target="_blank">#36912</a></li> 
</ul> 
<h4>Bug 修复</h4> 
<ul> 
 <li><strong>Annotations：</strong>更正页面刷新时显示的注释。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgrafana%2Fgrafana%2Fpull%2F37496" target="_blank">#37496</a></li> 
 <li><strong>Annotations：</strong>修复从 Grafana v8.0.6 中消失的启用按钮。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgrafana%2Fgrafana%2Fpull%2F37454" target="_blank">#37454</a></li> 
 <li><strong>Annotations：</strong>修复不可用于注释的数据源模板变量。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgrafana%2Fgrafana%2Fpull%2F37506" target="_blank">#37506</a></li> 
 <li><strong>AzureMonitor：</strong>修复未加载的注释查询编辑器。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgrafana%2Fgrafana%2Fpull%2F37476" target="_blank">#37476</a></li> 
 <li><strong>Geomap：</strong>修复比例计算。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgrafana%2Fgrafana%2Fpull%2F37375" target="_blank">#37375</a></li> 
 <li><strong>GraphNG：</strong>修复 y 轴自动调整大小。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgrafana%2Fgrafana%2Fpull%2F37464" target="_blank">#37464</a></li> 
 <li><strong>Live：</strong>显示流率并修复列表响应中的重复频道。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgrafana%2Fgrafana%2Fpull%2F37365" target="_blank">#37365</a></li> 
 <li><strong>Loki：</strong>当时间范围改变时更新日志浏览器中的标签。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgrafana%2Fgrafana%2Fpull%2F37520" target="_blank">#37520</a></li> 
 <li><strong>Loki：</strong>当仪表板中的时间范围发生变化时，更新日志浏览器中的标签。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgrafana%2Fgrafana%2Fpull%2F37541" target="_blank">#37541</a></li> 
 <li><strong>NGAlert：</strong>在 alerting -> Normal 时向 alertmanager 发送解决信号。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgrafana%2Fgrafana%2Fpull%2F37363" target="_blank">#37363</a></li> 
 <li><strong>PasswordField：</strong>防止在单击 Enter 按钮时显示密码。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgrafana%2Fgrafana%2Fpull%2F37444" target="_blank">#37444</a></li> 
 <li><strong>Renderer：</strong>当 Grafana 停止时删除 debug.log 文件。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgrafana%2Fgrafana%2Fpull%2F37367" target="_blank">#37367</a></li> 
 <li><strong>Security：</strong>更新依赖项以修复 CVE-2021-36222。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgrafana%2Fgrafana%2Fpull%2F37546" target="_blank">#37546</a></li> 
</ul> 
<p>更新说明：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgrafana%2Fgrafana%2Freleases%2Ftag%2Fv8.1.0" target="_blank">https://github.com/grafana/grafana/releases/tag/v8.1.0</a></p>
                                        </div>
                                      
</div>
            