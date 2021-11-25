
---
title: 'Grafana 8.3.0-beta1 发布，系统指标监控与分析平台'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=3879'
author: 开源中国
comments: false
date: Thu, 25 Nov 2021 06:17:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=3879'
---

<div>   
<div class="content">
                                                                    
                                                        <p style="color:#000000; margin-left:0; margin-right:0; text-align:start">Grafana 8.3.0-beta1 现已发布。Grafana 是一个功能丰富的指标标准仪表板和图形编辑器，用于分析和监控 Graphite、Elasticsearch、OpenTSDB、Prometheus 和 InfluxDB。</p> 
<p style="color:#000000; margin-left:0; margin-right:0; text-align:start">具体更新内容如下：</p> 
<p style="color:#000000; margin-left:0; margin-right:0; text-align:start"><strong>Features and enhancement</strong></p> 
<ul style="margin-left:0; margin-right:0"> 
 <li><strong>AccessControl：</strong>将细粒度的访问控制应用于许可。（Enterprise）</li> 
 <li><strong>Alerting：</strong>使面板标题中的警报状态指示器与 Grafana 8 警报一起使用。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgrafana%2Fgrafana%2Fpull%2F38713" target="_blank">#38713</a></li> 
 <li><strong>Alerting：</strong> Discord 通知程序可选择使用 webhook name。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgrafana%2Fgrafana%2Fpull%2F40463" target="_blank">#40463</a></li> 
 <li><strong>Annotations：</strong>弃用 AnnotationsSrv。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgrafana%2Fgrafana%2Fpull%2F39631" target="_blank">#39631</a>，<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fhugohaggmark" target="_blank">@hugohaggmark</a></li> 
 <li><strong>Auditing：</strong>为统一警报端点添加审计日志。（Enterprise）</li> 
 <li><strong>Auth：</strong>省略 JWT auth 的 JWT tokens 中的所有 base64 paddings。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgrafana%2Fgrafana%2Fpull%2F35602" target="_blank">#35602</a></li> 
 <li><strong>Azure Monitor：</strong>编辑指标时清理字段。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgrafana%2Fgrafana%2Fpull%2F41762" target="_blank">#41762</a></li> 
 <li><strong>AzureMonitor：</strong>添加新的 starter dashboards。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgrafana%2Fgrafana%2Fpull%2F39876" target="_blank">#39876</a></li> 
 <li><strong>Barchart/Time series：</strong>允许 x 轴标签。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgrafana%2Fgrafana%2Fpull%2F41142" target="_blank">#41142</a></li> 
 <li><strong>CLI：</strong>改进安装插件的错误处理。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgrafana%2Fgrafana%2Fpull%2F41257" target="_blank">#41257</a></li> 
 <li><strong>CloudMonitoring：</strong>迁移到使用后端插件 SDK 合同。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgrafana%2Fgrafana%2Fpull%2F38650" target="_blank">#38650</a></li> 
 <li><strong>Elasticsearch：</strong>添加对 Elasticsearch 8.0<span> </span><span style="color:#24292f">(Beta) </span>的支持。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgrafana%2Fgrafana%2Fpull%2F41729" target="_blank">#41729</a></li> 
 <li><strong>Explore：</strong>允许更改<span> </span><span style="color:#24292f">graph type</span>。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgrafana%2Fgrafana%2Fpull%2F40522" target="_blank"># </a><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgabor" target="_blank">40522</a></li> 
 <li><strong>OAuth：</strong>支持 PKCE。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgrafana%2Fgrafana%2Fpull%2F39948" target="_blank">#39948</a></li> 
 <li>......<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgabor" target="_blank">​​​​</a></li> 
</ul> 
<h4 style="margin-left:.6em; margin-right:0; text-align:start"><span style="color:#24292f">Bug 修复</span></h4> 
<ul style="margin-left:0; margin-right:0"> 
 <li><strong>API：</strong>修复仪表盘上的 imports 配额限制。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgrafana%2Fgrafana%2Fpull%2F41495" target="_blank">#41495</a></li> 
 <li><strong>Alerting：</strong>修复 Azure Monitor 数据源的规则编辑器问题。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgrafana%2Fgrafana%2Fpull%2F41317" target="_blank">#41317</a></li> 
 <li><strong>Azure monitor：</strong>确保在使用模板变量时未启用警报规则编辑器。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgrafana%2Fgrafana%2Fpull%2F41335" target="_blank">#41335</a></li> 
 <li><strong>CloudMonitoring：</strong>修复注释查询。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgrafana%2Fgrafana%2Fpull%2F41529" target="_blank">#41529</a></li> 
 <li><strong>CodeEditor：</strong>触发传递给 CodeEditor 的最新 getSuggestions()。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgrafana%2Fgrafana%2Fpull%2F40544" target="_blank">#40544</a></li> 
 <li><strong>Dashboard：</strong>从 Dashboard 数据源的选项列表中删除当前面板。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgrafana%2Fgrafana%2Fpull%2F41826" target="_blank">#41826</a></li> 
 <li><strong>Encryption：</strong>修复警报迁移中的 decrypting secrets 。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgrafana%2Fgrafana%2Fpull%2F41061" target="_blank">#41061</a></li> 
 <li><strong>InfluxDB：</strong>修复 ALIAS 字段中索引太大的极端情况。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgrafana%2Fgrafana%2Fpull%2F41562" target="_blank">#41562</a></li> 
 <li><strong>NavBar：</strong>按字母顺序排列应用程序插件。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgrafana%2Fgrafana%2Fpull%2F40078" target="_blank">#40078</a></li> 
 <li><strong>NodeGraph：</strong>修复触摸板上的缩放灵敏度。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgrafana%2Fgrafana%2Fpull%2F40718" target="_blank">#40718</a></li> 
 <li><strong>Plugins：</strong>将 OAuth pass-through 逻辑添加到 api/ds/query 端点。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgrafana%2Fgrafana%2Fpull%2F41352" target="_blank">#41352</a></li> 
 <li><strong>Snapshots：</strong>修复快照数据的面板检查器。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgrafana%2Fgrafana%2Fpull%2F41530" target="_blank">#41530</a></li> 
 <li><strong>Tempo：</strong>修复添加标签时的基本身份验证密码重置。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgrafana%2Fgrafana%2Fpull%2F41808" target="_blank">#41808</a></li> 
 <li><strong>ValueMapping：</strong>修复了 regex mappings 问题。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgrafana%2Fgrafana%2Fpull%2F41515" target="_blank">#41515</a></li> 
</ul> 
<h4 style="margin-left:.6em; margin-right:0; text-align:start"><span style="color:#24292f"><strong>插件开发修复和更改</strong></span></h4> 
<ul style="margin-left:0; margin-right:0"> 
 <li><strong>grafana/ui：</strong>启用滑块标记显示。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgrafana%2Fgrafana%2Fpull%2F41275" target="_blank">#41275</a></li> 
</ul> 
<p style="color:#000000; margin-left:0; margin-right:0; text-align:start">更新说明：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgrafana%2Fgrafana%2Freleases%2Ftag%2Fv8.3.0-beta1" target="_blank">https://github.com/grafana/grafana/releases/tag/v8.3.0-beta1</a></p> 
<p> </p>
                                        </div>
                                      
</div>
            