
---
title: 'Grafana 8 发布：统一告警、实时流和新的可视化等！'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://oscimg.oschina.net/oscnet/up-d89a4cc6ef75e6134bc22b9cd9f99235cdf.png'
author: 开源中国
comments: false
date: Fri, 11 Jun 2021 14:00:00 GMT
thumbnail: 'https://oscimg.oschina.net/oscnet/up-d89a4cc6ef75e6134bc22b9cd9f99235cdf.png'
---

<div>   
<div class="content">
                                                                    
                                                        <div> 
 <div> 
  <h2>前言</h2> 
  <p>Grafana v8.0 的<strong>重大变更</strong>包括对告警系统的重构；新的可视化改进，包括状态时间线、状态历史和直方图面板； <strong>实时流</strong>； 可以重用的<strong>库面板</strong>； 和<strong>细粒度的访问控制</strong>，允许企业客户确保其组织中的每个人都具有适当的<strong>访问级别</strong>。</p> 
  <p>我们还对 Grafana 的性能和功能进行了升级。 用户界面的改进带来了焕然一新的外观和感觉； Enterprise 中的数据源查询缓存用来<strong>加快仪表盘加载</strong>； 由于初始下载数据的大幅减少，<strong>更好的启动和加载性能</strong>，这意味着您可以更快地工作并享受与仪表盘的响应更快的交互。</p> 
  <p>要了解更多信息，请收听 6 月 9 日在 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgrafana.com%2Fgo%2Fgrafanaconline%2F2021%2Fgrafana-8%2F%3Fpg%3Dblog" target="_blank">GrafanaCONline 上举行的 Grafana 8.0 深入探讨会议</a>。在本次演讲中，Grafana 团队成员将演示此版本中的更多新功能。 您还可以在我们新的 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fplay.grafana.org%2Fd%2FYI95GyqMz%2F1-new-features-in-v8-0%3ForgId%3D1" target="_blank">Grafana Play 仪表盘</a>中查看 v8 中的新功能。 ​</p> 
  <p>最后，您可以通过 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgrafana.com%2Fproducts%2Fcloud%2F" target="_blank">Grafana Cloud</a> 在几分钟内开始使用 Grafana。 我们有免费和付费的 Grafana Cloud 计划来满足每个用例——<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgrafana.com%2Fauth%2Fsign-up%2Fcreate-user%3Fpg%3Dblog" target="_blank">立即免费注册</a>。</p> 
  <p>现在让我们来看看Grafana8.0中所有令人兴奋的新特性！</p> 
  <p><img alt src="https://oscimg.oschina.net/oscnet/up-d89a4cc6ef75e6134bc22b9cd9f99235cdf.png" referrerpolicy="no-referrer"></p> 
  <h2>一、告警</h2> 
  <p>多年来，Grafana 社区提出的最多需求都是警报相关的。去年9月，我们在 Grafana Cloud 中引入了 Prometheus 风格的告警，在 Grafana 实例中嵌入了一个简单的 UI 来管理警报。</p> 
  <p>在此基础上，我们在 8.0 对 Grafana 告警系统进行了全面的改进，将 Prometheus 告警和 Grafana 告警统一在同一个用户界面中，用于查看和编辑告警。这为所有 Grafana 用户和数据源提供了一种常见的告警体验——无论您使用的是开源版本还是企业和云堆栈。</p> 
  <p>Grafana 托管告警和来自 Prometheus 兼容数据源的告警都受支持，因此您可以为 Grafana 托管告警、Cortex 告警和 Loki 告警创建和编辑告警规则，还可以在单个可搜索视图中查看来自 Prometheus 兼容数据源的告警信息。这是 8.0 的一个选择加入功能。</p> 
  <p><img alt height="348" src="https://oscimg.oschina.net/oscnet/up-45bc7710487b666a5fcd1666ded95739d46.png" width="1080" referrerpolicy="no-referrer"></p> 
  <p>警报现在已与仪表盘解耦，我们还添加了对多维警报的支持、用于大规模管理通知的通知策略，以及功能齐全的API。</p> 
  <p><img alt height="348" src="https://oscimg.oschina.net/oscnet/up-b2e197bc7705c03dcca4f4fe5b5930cd36c.gif" width="1080" referrerpolicy="no-referrer"></p> 
  <p>有关我们新的警报功能的更多信息，请务必在6月16日的 GrafanaCONline 上观看“<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgrafana.com%2Fgo%2Fgrafanaconline%2F2021%2Falerting%2F" target="_blank">Grafana中告警的下一步</a>”课程。</p> 
  <h2>二、值映射</h2> 
  <p>使用新的值映射编辑器，可以将字符串和布尔状态直接映射到颜色和可选显示文本。这将在所有Grafana可视化中工作，包括新的状态时间表面板（见下文）。</p> 
  <p><img alt height="320" src="https://oscimg.oschina.net/oscnet/up-905c14a27bca0f4c26dd005061cb1e11c54.png" width="1080" referrerpolicy="no-referrer"></p> 
  <h2>三、状态时间轴面板</h2> 
  <p>“状态时间线”面板可以随时间显示字符串或布尔值状态。使用上述新的值映射功能，可以为每个值指定颜色。通过使用阈值，您还可以将时间序列可视化为随时间变化的离散状态，这样就可以很容易地一眼看到每个阈值括号中花费的持续时间。</p> 
  <p><img alt src="https://oscimg.oschina.net/oscnet/up-ee01e9cd6f1d296150ea16d3ce601caac3b.png" referrerpolicy="no-referrer"></p> 
  <h2>四、历史状态面板</h2> 
  <p>该面板旨在显示状态回顾，随着时间的推移可视化周期性数据。 您可以使用值映射为每个值添加颜色。 这适用于数字、字符串或布尔状态。</p> 
  <p><img alt src="https://oscimg.oschina.net/oscnet/up-e87dd21e4fac0bf480277a46f237dfa64c2.png" referrerpolicy="no-referrer"></p> 
  <h2>五、条形图面板</h2> 
  <p>新的条形图面板为 Grafana 增加了新的绘图功能，特别是对于非时间序列数据。它支持分类 x 或 y 字段、分组条以及水平和垂直布局。</p> 
  <p><img alt height="775" src="https://oscimg.oschina.net/oscnet/up-a28a23177d8eac017554189cd365b18f872.png" width="694" referrerpolicy="no-referrer"></p> 
  <h2>六、直方图面板</h2> 
  <p>曾经是旧图形面板的隐藏功能，此直方图面板现在是一个独立的可视化。 您可以使用此面板将计算数据分布中的桶的直方图转换与条形图可视化结合起来。 此外，我们还引入了可以与任何可视化配对的直方图转换。</p> 
  <p><img alt height="251" src="https://oscimg.oschina.net/oscnet/up-1a42a1e707e2deaf6d935fddd156f3ec3b0.png" width="1080" referrerpolicy="no-referrer"></p> 
  <h2>七、面板搜索和表格切换</h2> 
  <p>为了改进导航，我们添加了搜索功能，以便更轻松地在长长的面板选项和覆盖列表中找到您想要的内容。 它们现在也都列在面板编辑侧栏中，而不是在选项卡中分开。 此外，还有一个新的表视图切换，可让您快速查看传递给可视化的数据。</p> 
  <p><img alt height="447" src="https://oscimg.oschina.net/oscnet/up-cfee0f8e48cc50c8656340b7e5db498fa2d.png" width="1080" referrerpolicy="no-referrer"></p> 
  <h2>八、库面板</h2> 
  <p>我们添加了一个用于重用面板的新工作流程。 您现在可以构建可跨多个仪表盘共享的库面板。 对库面板所做的更改或更新将反映在使用该库面板的每个仪表盘上。</p> 
  <h2>九、实时流</h2> 
  <p>实时流自从在 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgrafana.com%2Fblog%2F2021%2F02%2F04%2Fgrafana-7.4-released-next-generation-graph-panel-with-30-fps-live-streaming-prometheus-exemplar-support-trace-to-logs-and-more%2F%23next-generation-graph-panel" target="_blank">7.4 版本的图形面板中实现预览版</a>，在 8.0 中获得了更多功能。 这是我们在 Grafana 中为支持工业/物联网用例所做的激动人心的改变的一部分。 实时更新现在可以通过与 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgrafana%2Fmqtt-datasource" target="_blank">MQTT</a> 数据源的 websocket 连接发送到仪表盘，也可以从 cURL 或 Telegraf 流式传输。 还可以通过将指标发布到新的实时端点 <code>/api/live/push</code> 来将事件发送到仪表盘。</p> 
  <p><img alt="Grafana 8 live streaming demo from Grafana Labs .gif" src="https://oscimg.oschina.net/oscnet/up-2b5a446f2056753ff04ac460a3ac8de06ff.gif" referrerpolicy="no-referrer"></p> 
  <p>它现在是 Grafana 的内置标准功能，可以开箱即用。 您所要做的就是推送到 API 并为您推送的数据连接面板。</p> 
  <h2>十、loki 日志的改进</h2> 
  <p>我们对探索中的日志导航进行了重大改进。 我们为日志添加了分页功能，因此您可以在达到行数限制时点击查看较旧或较新的日志。</p> 
  <p><img alt="image.png" height="372" src="https://oscimg.oschina.net/oscnet/up-b0b83e910179a49c71d3ba69e627b6d2c29.png" width="1080" referrerpolicy="no-referrer"></p> 
  <p>您还可以通过面板检查器中的 Data 选项卡和 Explore 的检查器将日志结果下载为文本文件。</p> 
  <h2>十一、更多的 traces 函数支持</h2> 
  <p>您现在可以通过直接从 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgrafana.com%2Foss%2Ftempo%2F" target="_blank">Grafana Tempo</a>（我们刚刚 GA 的分布式跟踪后端）查询 <a href="https://www.oschina.net/action/GoToLink?url=http%3A%2F%2Fgrafana.com%2Foss%2Floki%2F" target="_blank">Grafana Loki</a> 来搜索跟踪！</p> 
  <p>使用带有<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgrafana.com%2Fdocs%2Ftempo%2Flatest%2Fgrafana-agent%2Fautomatic-logging%2F" target="_blank">日志的附加 Loki 数据源</a>，您可以通过 Tempo 更轻松地发现跟踪并快速构建 Loki 查询。 更进一步，Tempo 查询面板现在可以帮助您从 Loki 数据源日志构建查询，因此您不必成为 LogQL 专家——同时提供更统一的跟踪发现体验。</p> 
  <p><img alt height="794" src="https://oscimg.oschina.net/oscnet/up-94f5ca856687c5e5fe51825ea3ca3675f4c.png" width="1080" referrerpolicy="no-referrer"></p> 
  <p>Explore 中还有更好的 Jaeger 搜索，以及支持 Jaeger、Zipkin 和 Tempo 的显示跟踪图。</p> 
  <h2>十二、获取更多信息</h2> 
  <p>查看 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgrafana.com%2Fdocs%2Fgrafana%2Flatest%2Fwhatsnew%2Fwhats-new-in-v8-0%2F" target="_blank">文档</a> 和 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgrafana.com%2Fdocs%2Fgrafana%2Flatest%2Frelease-notes%2F" target="_blank">版本说明</a> 以获取新功能、更改和错误修复的完整列表。</p> 
  <p>订阅我们即将举行的实时网络研讨会，了解有关仪表盘和 Grafana 8 用户界面的更多信息，同时为使用 Prometheus 和 Loki 存储指标和日志的 Web 服务设置监控。</p> 
  <p><strong>6月24日</strong> **: **<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgo.grafana.com%2FMzU2LVlGRy0zODkAAAF9kBOCjfpqa_qS7QruuPSU8FWcm4-vjofFJylmSBVVrG3rBrK1eSHL8efQRcTFMw6F-ZYAJQs%3D" target="_blank"><strong>Getting started with Grafana 8</strong></a></p> 
  <p><strong>6月29日</strong> <strong>:</strong> <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgo.grafana.com%2FMzU2LVlGRy0zODkAAAF9kBOCjaHybeVAihWzmGqsncRtdFEq7-eM9ShiEufhj-kgbInmkg8nqO3iy-KaLnD5BI66Opo%3D" target="_blank"><strong>Getting started with Grafana dashboard design</strong></a></p> 
  <h2>十二、升级 Grafana 8.0</h2> 
  <p>下载安装 Grafana 8.0 或尝试 Grafana 8.0 Cloud ：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgrafana.com%2Fget%2F" target="_blank">grafana.com/get/</a></p> 
  <p>有关升级安装 Grafana 的更多信息，请参阅：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgrafana.com%2Fdocs%2Fgrafana%2Flatest%2Finstallation%2Fupgrading%2F" target="_blank">grafana.com/docs/grafan…</a></p> 
  <h2>译者说</h2> 
  <p>我们一直在关注和使用 grafana 公司的一些产品，包括 Grafana、Prometheus、Loki 等。</p> 
  <p>mica-metrics 完善了对 druid 和 undertow 的指标收集，mica-logging 组件也添加了对 loki 的支持，欢迎关注和使用。</p> 
 </div> 
</div>
                                        </div>
                                      
</div>
            