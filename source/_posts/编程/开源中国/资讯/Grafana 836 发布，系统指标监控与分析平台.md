
---
title: 'Grafana 8.3.6 发布，系统指标监控与分析平台'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=8194'
author: 开源中国
comments: false
date: Fri, 11 Feb 2022 07:03:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=8194'
---

<div>   
<div class="content">
                                                                                            <p style="margin-left:0px">Grafana 8.3.6 现已发布。Grafana 是一个功能丰富的指标标准仪表板和图形编辑器，用于分析和监控 Graphite、Elasticsearch、OpenTSDB、Prometheus 和 InfluxDB。</p> 
<p style="margin-left:0px">该版本具体更新内容如下：</p> 
<h3 style="margin-left:0px">新特性&改进</h3> 
<ul> 
 <li><strong>Cloud Monitoring：</strong>列出标签时减少请求大小。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgrafana%2Fgrafana%2Fpull%2F44365" target="_blank">#44365</a></li> 
 <li><strong>Explore:</strong> <span style="color:#24292f">在表格中显示标量数据结果（此前是在图标中）。</span> <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgrafana%2Fgrafana%2Fpull%2F44362" target="_blank">#44362</a></li> 
 <li><strong>Snapshots:</strong> <span style="color:#2e3033">更新外部快照服务器的默认 URL。</span> <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgrafana%2Fgrafana%2Fpull%2F44563" target="_blank">#44563</a></li> 
 <li><strong>Table:</strong> <span style="color:#2e3033">使页脚不重叠表内容。</span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgrafana%2Fgrafana%2Fpull%2F44210" target="_blank">#44210</a></li> 
 <li><strong>Tempo:</strong> <span style="color:#2e3033">向服务图数据链添加请求直方图。</span> <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgrafana%2Fgrafana%2Fpull%2F44671" target="_blank">#44671</a></li> 
 <li><strong>Tempo:</strong> <span style="color:#24292f">将时间范围添加到功能标志后面的速度搜索查询</span> <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgrafana%2Fgrafana%2Fpull%2F43811" target="_blank">#43811</a></li> 
 <li><strong>Tempo:</strong> <span style="color:#24292f">更改查询类型时，自动清除当前查询结果。</span> <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgrafana%2Fgrafana%2Fpull%2F44390" target="_blank">#44390</a></li> 
 <li><strong>Tempo:</strong> <span style="color:#24292f">将搜索结果中的“开始时间”显示为相对时间</span><span style="color:#2e3033">。</span> <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgrafana%2Fgrafana%2Fpull%2F44568" target="_blank">#44568</a></li> 
</ul> 
<h3><strong>Bug 修复</strong></h3> 
<ul> 
 <li><strong>Cloud Monitoring:</strong> <span style="color:#2e3033">修复查询编辑器中的资源标签</span>. <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgrafana%2Fgrafana%2Fpull%2F44550" target="_blank">#44550</a></li> 
 <li><strong>Cursor sync: </strong><span style="color:#2e3033">应用设置时不保存仪表板。</span> <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgrafana%2Fgrafana%2Fpull%2F44270" target="_blank">#44270</a></li> 
 <li><strong>LibraryPanels:</strong> <span style="color:#24292f">修复了清理库面板时出现的错误</span> <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgrafana%2Fgrafana%2Fpull%2F45033" target="_blank">#45033</a></li> 
 <li><strong>Logs Panel:</strong> <span style="color:#24292f">修复没有时区的字符串日期的时间戳解析</span> <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgrafana%2Fgrafana%2Fpull%2F44664" target="_blank">#44664</a></li> 
 <li><strong>Prometheus: </strong><span style="color:#24292f">修复一些使用 reduce/math 操作的警告查询</span>. <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgrafana%2Fgrafana%2Fpull%2F44380" target="_blank">#44380</a></li> 
 <li><strong>TablePanel:</strong> <span style="color:#2e3033">修复临时变量无法在默认数据源上工作的问题。</span> <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgrafana%2Fgrafana%2Fpull%2F44314" target="_blank">#44314</a></li> 
 <li><strong>Text Panel:</strong> <span style="color:#2e3033">修复元素的对齐方式。</span> <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgrafana%2Fgrafana%2Fpull%2F44313" target="_blank">#44313</a></li> 
 <li><strong>Variables:</strong> <span style="color:#2e3033">修复了自引用链接中常量变量的问题。</span> <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgrafana%2Fgrafana%2Fpull%2F44631" target="_blank">#44631</a></li> 
</ul> 
<p>更新公告：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgrafana%2Fgrafana%2Freleases%2Ftag%2Fv8.3.6" target="_blank">https://github.com/grafana/grafana/releases/tag/v8.3.6</a></p>
                                        </div>
                                      
</div>
            