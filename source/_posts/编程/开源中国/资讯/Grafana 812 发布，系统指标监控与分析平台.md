
---
title: 'Grafana 8.1.2 发布，系统指标监控与分析平台'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=7874'
author: 开源中国
comments: false
date: Sat, 21 Aug 2021 07:16:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=7874'
---

<div>   
<div class="content">
                                                                                            <p>Grafana 8.1.2 现已发布。Grafana 是一个功能丰富的指标标准仪表板和图形编辑器，用于分析和监控 Graphite、Elasticsearch、OpenTSDB、Prometheus 和 InfluxDB。</p> 
<p>具体更新内容如下：</p> 
<h4><strong>Features and enhancements</strong></h4> 
<ul> 
 <li><strong>AzureMonitor：</strong>添加对 PostgreSQL 和 MySQL 灵活服务器的支持。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgrafana%2Fgrafana%2Fpull%2F38075" target="_blank">#38075</a></li> 
 <li><strong>Datasource：</strong>将 datasource health check 失败的 HTTP 状态代码更改为 400。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgrafana%2Fgrafana%2Fpull%2F37895" target="_blank">#37895</a></li> 
 <li><strong>Explore：</strong>将 span duration 添加到 trace viewer 的左侧面板。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgrafana%2Fgrafana%2Fpull%2F37806" target="_blank">#37806</a></li> 
 <li><strong>Plugins：</strong>在提供插件资产时使用文件扩展名 allowlist，而不是检查 UNIX 可执行文件。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgrafana%2Fgrafana%2Fpull%2F37688" target="_blank">#37688</a></li> 
 <li><strong>Profiling：</strong>支持将 pprof 服务器绑定到自定义网络接口。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgrafana%2Fgrafana%2Fpull%2F36580" target="_blank">#36580</a></li> 
 <li><strong>Search：</strong>使搜索图标键盘可导航。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgrafana%2Fgrafana%2Fpull%2F37865" target="_blank">#37865</a></li> 
 <li><strong>Template variables：</strong>键盘导航改进。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgrafana%2Fgrafana%2Fpull%2F38001" target="_blank">#38001</a></li> 
 <li><strong>Tooltip：</strong>在分钟时间范围内显示毫秒 (ms)。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgrafana%2Fgrafana%2Fpull%2F37569" target="_blank"># </a><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fnikki-kiga" target="_blank">37569</a></li> 
</ul> 
<h4>Bug 修复</h4> 
<ul> 
 <li><strong>Alerting：</strong>修复保存 LINE contact point。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgrafana%2Fgrafana%2Fpull%2F37744" target="_blank">#37744</a></li> 
 <li><strong>Alerting：</strong>修复保存 LINE contact point。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgrafana%2Fgrafana%2Fpull%2F37718" target="_blank">#37718</a></li> 
 <li><strong>Annotations：</strong>修复 alerting annotation coloring。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgrafana%2Fgrafana%2Fpull%2F37412" target="_blank">#37412</a></li> 
 <li><strong>Annotations：</strong>修复了 alerting annotation 在正确面板中的可见性。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgrafana%2Fgrafana%2Fpull%2F37959" target="_blank">#37959</a></li> 
 <li><strong>Auth：</strong>隐藏 SigV4 配置 UI 并在禁用其配置标志时禁用中间件。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgrafana%2Fgrafana%2Fpull%2F37293" target="_blank">#37293</a></li> 
 <li><strong>Dashboard：</strong>通过将窗口宽度与主题断点进行比较来防止不正确的面板布局。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgrafana%2Fgrafana%2Fpull%2F37868" target="_blank">#37868</a></li> 
 <li><strong>Elasticsearch：</strong>修复警报查询的指标名称。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgrafana%2Fgrafana%2Fpull%2F37871" target="_blank">#37871</a></li> 
 <li><strong>Explore：</strong>修复完整日志上下文的显示。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgrafana%2Fgrafana%2Fpull%2F37442" target="_blank">#37442</a></li> 
 <li><strong>PanelEdit：</strong>通过将正确的面板大小传递给 Das…. 来修复“Actual”大小。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgrafana%2Fgrafana%2Fpull%2F37885" target="_blank">#37885</a></li> 
 <li><strong>Plugins：</strong>修复 TLS 数据源设置。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgrafana%2Fgrafana%2Fpull%2F37797" target="_blank">#37797</a></li> 
 <li><strong>Variables：</strong>修复导航空白下拉的问题。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgrafana%2Fgrafana%2Fpull%2F37776" target="_blank">#37776</a></li> 
 <li><strong>Variables：</strong>修复 URL util 转换<code>false</code>为<code>true</code>. <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgrafana%2Fgrafana%2Fpull%2F37402" target="_blank"># </a><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FsimPod" target="_blank">37402</a></li> 
</ul> 
<h4>Plugin development fixes & changes</h4> 
<ul> 
 <li><strong>Toolkit：</strong>修复 matchMedia 未找到的错误。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgrafana%2Fgrafana%2Fpull%2F37643" target="_blank">#37643</a></li> 
</ul> 
<p>详情可查看：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgrafana%2Fgrafana%2Freleases%2Ftag%2Fv8.1.2" target="_blank">https://github.com/grafana/grafana/releases/tag/v8.1.2</a></p>
                                        </div>
                                      
</div>
            