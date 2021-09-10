
---
title: 'Grafana 8.1.3 发布，系统指标监控与分析平台'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=3427'
author: 开源中国
comments: false
date: Fri, 10 Sep 2021 07:06:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=3427'
---

<div>   
<div class="content">
                                                                                            <div> 
 <p>Grafana 8.1.3 现已发布。Grafana 是一个功能丰富的指标标准仪表板和图形编辑器，用于分析和监控 Graphite、Elasticsearch、OpenTSDB、Prometheus 和 InfluxDB。</p> 
 <p style="color:#333333; text-align:left">具体更新内容如下：</p> 
 <h4>Bug fixes</h4> 
 <ul> 
  <li><strong>Alerting：</strong>修复内部警报管理器中的 alert flapping。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgrafana%2Fgrafana%2Fpull%2F38648" rel="nofollow" target="_blank">#38648</a></li> 
  <li><strong>Alerting：</strong>修复请求处理程序无法将数据帧“results”转换为 plugins.DataTimeSeriesSlice：输入帧未被识别为时间序列。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgrafana%2Fgrafana%2Fpull%2F38587" rel="nofollow" target="_blank">#38587</a></li> 
  <li><strong>Dashboard：</strong>通过导入 .json 文件，在导入/创建 dashboards 时，修复 UID 不被保留的问题。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgrafana%2Fgrafana%2Fpull%2F38659" rel="nofollow" target="_blank">#38659</a></li> 
  <li><strong>Dashboard：</strong>退出面板编辑时强制面板重新渲染。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgrafana%2Fgrafana%2Fpull%2F38913" rel="nofollow" target="_blank">#38913</a></li> 
  <li><strong>Dashboard：</strong>在导航到常规设置时防止文件夹更改。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgrafana%2Fgrafana%2Fpull%2F38103" rel="nofollow" target="_blank">#38103</a></li> 
  <li><strong>Docker：</strong>强制使用 libcrypto1.1 和 libssl1.1 版本来修复 CVE-2021-3711。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgrafana%2Fgrafana%2Fpull%2F38585" rel="nofollow" target="_blank">#38585</a></li> 
  <li><strong>Elasticsearch：</strong>修复警报查询的指标名称。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgrafana%2Fgrafana%2Fpull%2F38546" rel="nofollow" target="_blank">#38546</a></li> 
  <li><strong>Elasticsearch：</strong>将直方图字段参数限制为数值。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgrafana%2Fgrafana%2Fpull%2F38631" rel="nofollow" target="_blank">#38631</a></li> 
  <li><strong>Elasticsearch：</strong>防止管道聚合按选项顺序显示。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgrafana%2Fgrafana%2Fpull%2F38448" rel="nofollow" target="_blank">#38448</a></li> 
  <li><strong>LibraryPanels：</strong>防止创建重复的 repeated panels。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgrafana%2Fgrafana%2Fpull%2F38804" rel="nofollow" target="_blank">#38804</a></li> 
  <li><strong>Loki：</strong>在与解析器一起使用时修复 dashboard 中的临时过滤器。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgrafana%2Fgrafana%2Fpull%2F38542" rel="nofollow" target="_blank">#38542</a></li> 
  <li><strong>Plugins：</strong>跟踪签名文件+为未签名的 plugin assets 添加警告日志。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgrafana%2Fgrafana%2Fpull%2F38938" rel="nofollow" target="_blank">#38938</a></li> 
  <li><strong>Postgres/MySQL/MSSQL：</strong>修复未正确显示的区域注释。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgrafana%2Fgrafana%2Fpull%2F38936" rel="nofollow" target="_blank">#38936</a></li> 
  <li><strong>Prometheus：</strong>修复指标浏览器中的验证选择器。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgrafana%2Fgrafana%2Fpull%2F38921" rel="nofollow" target="_blank"># </a><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fivanahuckova" rel="nofollow" target="_blank">38921</a></li> 
 </ul> 
 <p>更新说明：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgrafana%2Fgrafana%2Freleases%2Ftag%2Fv8.1.3" rel="nofollow" target="_blank">https://github.com/grafana/grafana/releases/tag/v8.1.3</a></p> 
</div>
                                        </div>
                                      
</div>
            