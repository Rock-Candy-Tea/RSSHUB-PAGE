
---
title: 'Grafana 8.3.3 发布，系统指标监控与分析平台'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=7994'
author: 开源中国
comments: false
date: Tue, 14 Dec 2021 23:28:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=7994'
---

<div>   
<div class="content">
                                                                    
                                                        <p>Grafana 8.3.3 现已发布。Grafana 是一个功能丰富的指标标准仪表板和图形编辑器，用于分析和监控 Graphite、Elasticsearch、OpenTSDB、Prometheus 和 InfluxDB。</p> 
<p style="color:#000000; margin-left:0; margin-right:0; text-align:start">具体更新内容如下：</p> 
<h4 style="margin-left:0px; margin-right:0px; text-align:start"><strong>Features and enhancement</strong></h4> 
<ul> 
 <li><strong>BarChart：</strong>使用新的数据错误视图组件在面板编辑中显示操作。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgrafana%2Fgrafana%2Fpull%2F42474" target="_blank">#42474</a></li> 
 <li><strong>CloudMonitor：</strong>对资源的 pageToken 进行遍历。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgrafana%2Fgrafana%2Fpull%2F42546" target="_blank">#42546</a></li> 
 <li><strong>Macaron：</strong>防止 WriteHeader 无效的 HTTP status code panic。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgrafana%2Fgrafana%2Fpull%2F42973" target="_blank">#42973</a></li> 
</ul> 
<h4 style="text-align:start"><span style="color:#24292f">Bug 修复</span></h4> 
<ul> 
 <li><strong>AnnoListPanel：</strong>修复标签中变量的插值。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgrafana%2Fgrafana%2Fpull%2F42318" target="_blank"># </a><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Ffrancoisdtm" target="_blank">42318</a></li> 
 <li><strong>CloudWatch：</strong>允许查询没有指定维度。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgrafana%2Fgrafana%2Fpull%2F42800" target="_blank">#42800</a></li> 
 <li><strong>CloudWatch：</strong>修复了从 8.2.4/8.2.5 迁移到 8.3.0 的用户的损坏查询。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgrafana%2Fgrafana%2Fpull%2F42611" target="_blank">#42611</a></li> 
 <li><strong>CloudWatch：</strong>确保 MatchExact 标志获得正确的值。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgrafana%2Fgrafana%2Fpull%2F42621" target="_blank">#42621</a></li> 
 <li><strong>Dashboards：</strong>修复以便可以从管理仪表板/文件夹页面中删除空文件夹。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgrafana%2Fgrafana%2Fpull%2F42527" target="_blank">#42527</a></li> 
 <li><strong>InfluxDB：</strong>改进对 InfluxQL 中元数据查询错误的处理。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgrafana%2Fgrafana%2Fpull%2F42500" target="_blank">#42500</a></li> 
 <li><strong>Loki：</strong>修复为带有解析器和 line_format 表达式的查询添加临时过滤器的问题。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgrafana%2Fgrafana%2Fpull%2F42590" target="_blank">#42590</a></li> 
 <li><strong>Prometheus：</strong>修复对非直方图指标的示例查询的运行。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgrafana%2Fgrafana%2Fpull%2F42749" target="_blank">#42749</a></li> 
 <li><strong>Prometheus：</strong>在区间内插入模板变量。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgrafana%2Fgrafana%2Fpull%2F42637" target="_blank"># </a><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fivanahuckova" target="_blank">42637</a> </li> 
 <li><strong>StateTimeline：</strong>修复 toolitp 在具有多个字段的帧时不显示的问题。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgrafana%2Fgrafana%2Fpull%2F42741" target="_blank">#42741</a></li> 
 <li><strong>TraceView：</strong>修复在浏览器的右窗格中打开跟踪视图时虚拟化滚动。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgrafana%2Fgrafana%2Fpull%2F42480" target="_blank">#42480</a></li> 
 <li><strong>Variables：</strong>修复时间范围更改变量的重复面板。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgrafana%2Fgrafana%2Fpull%2F42828" target="_blank">#42828</a></li> 
 <li><strong>Variables：</strong>修复 queryparam 选项对范围内变量的作用。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgrafana%2Fgrafana%2Fpull%2F42742" target="_blank">#42742</a></li> 
</ul> 
<p>更新说明：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgrafana%2Fgrafana%2Freleases%2Ftag%2Fv8.3.3" target="_blank">https://github.com/grafana/grafana/releases/tag/v8.3.3</a></p>
                                        </div>
                                      
</div>
            