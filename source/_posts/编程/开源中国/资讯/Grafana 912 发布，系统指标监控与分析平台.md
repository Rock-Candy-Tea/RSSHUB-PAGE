
---
title: 'Grafana 9.1.2 发布，系统指标监控与分析平台'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=8977'
author: 开源中国
comments: false
date: Thu, 01 Sep 2022 07:03:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=8977'
---

<div>   
<div class="content">
                                                                                            <p><span style="background-color:#ffffff; color:#333333">Grafana 是一个用于监控和可观察性的开源平台，可视化来自 Prometheus、Loki、Elasticsearch、InfluxDB、Postgres 等多个来源的指标、日志等。</span></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><span style="background-color:#ffffff; color:#000000">Grafana v9.1.2 现已发布</span><span style="background-color:#ffffff; color:#333333">，更新内容如下：</span></p> 
<h4><strong><span><span><span><span><span style="color:#24292f"><span><span><span><span><span><span><span><span><span><span><span style="background-color:#ffffff"><span><span><span>Features and enhancements</span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></strong></h4> 
<ul> 
 <li><strong>AdHoc variable：</strong>配置时正确预选数据源。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgrafana%2Fgrafana%2Fpull%2F54088" target="_blank">#54088</a></li> 
 <li><strong>AzureMonitor：</strong>为模板变量添加了 ARG 查询功能。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgrafana%2Fgrafana%2Fpull%2F53059" target="_blank">#53059</a></li> 
 <li><strong>Dashboard save：</strong>浏览仪表板保存 drawer 的选项卡时保留详细信息消息。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgrafana%2Fgrafana%2Fpull%2F54084" target="_blank">#54084</a></li> 
 <li><strong>Dashboard：</strong>正确迁移混合数据源目标。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgrafana%2Fgrafana%2Fpull%2F54152" target="_blank">#54152</a></li> 
 <li><strong>Elasticsearch：</strong>使用毫秒间隔进行警报。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgrafana%2Fgrafana%2Fpull%2F54157" target="_blank">#54157</a></li> 
 <li><strong>Elasticsearch：</strong>在前端使用毫秒间隔。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgrafana%2Fgrafana%2Fpull%2F54202" target="_blank">#54202</a></li> 
 <li><strong>Geomap：</strong>Local 颜色范围。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgrafana%2Fgrafana%2Fpull%2F54348" target="_blank">#54348</a></li> 
 <li><strong>Plugins Catalog：</strong>使用 appSubUrl 生成插件目录 url。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgrafana%2Fgrafana%2Fpull%2F54426" target="_blank">#54426</a></li> 
 <li><strong>Rendering：</strong>添加对渲染器令牌的支持。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgrafana%2Fgrafana%2Fpull%2F54425" target="_blank">#54425</a></li> 
</ul> 
<h4><strong><span><span><span><span><span style="color:#24292f"><span><span><span><span><span><span><span><span><span><span><span style="background-color:#ffffff"><span><span><span>Bug 修复</span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></strong></h4> 
<ul> 
 <li><strong>Alerting：</strong>修复了使用签名 URL 上传的屏幕截图的保存问题。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgrafana%2Fgrafana%2Fpull%2F53933" target="_blank">#53933</a></li> 
 <li><strong>AngularPanels：</strong>修复了从面板编辑返回时更改的角度面板选项不生效的问题。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgrafana%2Fgrafana%2Fpull%2F54087" target="_blank">#54087</a></li> 
 <li><strong>Explore：</strong>改进查询行折叠按钮的 a11y。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgrafana%2Fgrafana%2Fpull%2F53827" target="_blank">#53827</a></li> 
 <li><strong>Geomap：</strong>修复工具提示显示。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgrafana%2Fgrafana%2Fpull%2F54245" target="_blank">#54245</a></li> 
 <li><strong>QueryEditorRow：</strong>在装载时过滤数据。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgrafana%2Fgrafana%2Fpull%2F54260" target="_blank">#54260</a></li> 
 <li><strong>Search：</strong>在文件夹视图中显示所有仪表板。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgrafana%2Fgrafana%2Fpull%2F54163" target="_blank">#54163</a></li> 
 <li><strong>Tracing：</strong>修复 opentelemetry tracing 中的事件属性。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgrafana%2Fgrafana%2Fpull%2F54117" target="_blank">#54117</a></li> 
</ul> 
<h4><strong><span><span><span><span><span style="color:#24292f"><span><span><span><span><span><span><span><span><span><span><span style="background-color:#ffffff"><span><span><span>插件开发修复和更改</span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></strong></h4> 
<ul> 
 <li><strong>GrafanaUI：</strong>修复无效选择和 DataSourcePicker 的样式。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgrafana%2Fgrafana%2Fpull%2F53476" target="_blank">#53476</a></li> 
</ul> 
<p>更新说明：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgrafana%2Fgrafana%2Freleases%2Ftag%2Fv9.1.2" target="_blank">https://github.com/grafana/grafana/releases/tag/v9.1.2</a></p>
                                        </div>
                                      
</div>
            