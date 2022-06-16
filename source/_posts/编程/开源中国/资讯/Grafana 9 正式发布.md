
---
title: 'Grafana 9 正式发布'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://static.oschina.net/uploads/space/2022/0616/075715_0cYh_4937141.png'
author: 开源中国
comments: false
date: Thu, 16 Jun 2022 07:59:00 GMT
thumbnail: 'https://static.oschina.net/uploads/space/2022/0616/075715_0cYh_4937141.png'
---

<div>   
<div class="content">
                                                                    
                                                        <p>Grafana 9.0 的主要重点是改善 Grafana 的用户体验，使可观察性和数据可视化更易用也更容易获得。无论是通过 Prometheus 和 Loki 可视化查询生成器还是面板和仪表板搜索功能，Grafana 9.0 都引入了更新的工作流程，使发现和调查数据变得更加容易和直观。</p> 
<p>要深入了解所有最新功能，可以加入<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgrafana.com%2Fgo%2Fgrafanaconline%2F2022%2Fgrafana-9-deep-dive%2F%3Fpg%3Dblog%26plcmt%3Dbody-txt" target="_blank">在 GrafanaCONline 举行的 Grafana 9.0 会议</a>。</p> 
<p><img alt height="394" src="https://static.oschina.net/uploads/space/2022/0616/075715_0cYh_4937141.png" width="700" referrerpolicy="no-referrer"></p> 
<h3>Visual Prometheus 查询生成器</h3> 
<p><img alt height="390" src="https://static.oschina.net/uploads/space/2022/0616/075726_tyPU_4937141.png" width="700" referrerpolicy="no-referrer"></p> 
<p>尽管 PromQL 是一种强大的查询语言，但当涉及到编写查询时，它并不是最简单的，也不容易理解它们。对于 Prometheus 新手来说，开始编写查询可能是令人生畏的。</p> 
<p>Prometheus 的新查询生成器正是为了解决这个问题而建立的。在 Grafana 9.0 中，你将在 Explore 中看到一个全新的可视化查询生成器界面，允许任何人编写、编辑和理解一个查询的作用。</p> 
<h3>多种方式来编写查询</h3> 
<p>你已经熟悉的 Explore 界面现在增加了切换字段，可以选择在文本编辑模式（Code）或可视化生成器模式（Builder）中编写 PromQL 查询。当你选择 Builder 模式时，一个新的可视化界面允许你通过多词搜索下拉菜单选择感兴趣的指标来制作你的查询。你可以在这些模式之间进行切换，同时保留你的文字修改。</p> 
<h3>用指标和标签过滤器生成你的查询</h3> 
<p>这个新的查询生成器允许你通过多词搜索来搜索和选择一个指标。你可以从选择一个指标或一个标签过滤器开始。</p> 
<h3>对指标进行数学运算</h3> 
<p>Operations 字段用于通过各种函数、聚合和二进制操作对感兴趣的指标进行数学操作。你可以通过 <code>+ Operation</code> 按钮将这些操作分层。由于 Operations 是按照执行的顺序呈现的，而不是按照文本查询中的倒序排列，这使得阅读和编辑查询变得更加容易。</p> 
<h3>通过应用内指南持续学习</h3> 
<p>如果你是 PromQL 的新手，你可以使用第三种模式，即 Explain，通过应用内指南了解已经写好的查询。你可以在 Builder 模式和 Explain 模式之间切换，同时保留查询，以了解更多关于被查询的指标和执行的操作。</p> 
<p><img alt height="200" src="https://static.oschina.net/uploads/space/2022/0616/075738_pdXJ_4937141.png" width="700" referrerpolicy="no-referrer"></p> 
<p><em>上图：切换到 Explain 模式获取应用内指南以了解查询。</em></p> 
<p><img alt height="176" src="https://static.oschina.net/uploads/space/2022/0616/075747_e3JD_4937141.png" width="700" referrerpolicy="no-referrer"></p> 
<p><em>上图：查看查询的不同参数代表什么的详细说明。</em></p> 
<p>新的可视化生成器也有被称为 "hints" 的建议，会适时提供正确操作的建议</p> 
<p><img alt height="201" src="https://static.oschina.net/uploads/space/2022/0616/075756_seX3_4937141.png" width="700" referrerpolicy="no-referrer"></p> 
<p><em>上图：Hints 指导你为要查询的指标选择最适合的操作。</em></p> 
<h3>Visual Grafana Loki 查询生成器</h3> 
<p>在 Grafana 9.0 中，编写 LogQL 查询也得到了一个可视化查询生成界面的帮助。在许多方面 LogQL 比 PromQL 更复杂，有更多的语法需要记忆。新的查询生成器将帮助你编写和理解 Loki 查询，而不需要记住任何语法。</p> 
<p>在下图所示的 Loki 查询生成器中，你可以添加和编辑标签过滤器、解析器和函数等。Loki 查询生成器支持上面列出的 Prometheus 查询生成器的所有功能，包括 Explain 模式，以及在 Code 模式和 Builder 模式之间切换的功能。</p> 
<p><img alt height="204" src="https://static.oschina.net/uploads/space/2022/0616/075813_tNaM_4937141.png" width="700" referrerpolicy="no-referrer"></p> 
<h3>Explore-to-dashboard 工作流程</h3> 
<p>虽然 Grafana 一直支持从仪表盘移动到 Explore 而不丢失上下文的功能，但反过来却不行。</p> 
<p>Grafana 9.0 公布了一个新的 Explore 到仪表盘的工作流程，允许你直接从 Explore 模式中创建面板或仪表盘。当一个复杂的查询起作用时，你不再需要费力地复制它或重写它到一个新的仪表板。相反只需指示 Grafana，通过点击一个按钮（见下图），就可以直接从 Explore 创建一个新的面板/仪表盘或添加到一个现有的面板中。</p> 
<p><img alt height="363" src="https://static.oschina.net/uploads/space/2022/0616/075823_c20t_4937141.png" width="700" referrerpolicy="no-referrer"></p> 
<h3>新的 heatmap 面板</h3> 
<p>新的和修订的 heatmap 面板经历了架构上的变化，使其具有更高的性能（能够在超过 20 万个数据点上呈现时间序列），速度也提高了几个数量级。除了性能，heatmap 面板上的分辨率也更高，你现在可以对色谱进行自定义和精细控制。</p> 
<p><img alt height="478" src="https://static.oschina.net/uploads/space/2022/0616/075834_5qpn_4937141.png" width="700" referrerpolicy="no-referrer"></p> 
<h3>命令面板</h3> 
<p>命令面板对于那些常用键盘快捷键的用户来说是一次很大的生产力提升。使用 cmd+K（macOS）或ctrl+K（Linux/Windows），你可以调出一个命令面板，使导航和仪表盘搜索更加容易。根据你在 Grafana 用户界面中的位置，你可以快速运行一个查询、切换到分割视图、在仪表盘之间导航，或改变主题偏好。</p> 
<p><img alt height="435" src="https://static.oschina.net/uploads/space/2022/0616/075844_THBI_4937141.png" width="700" referrerpolicy="no-referrer"></p> 
<h3>面板搜索</h3> 
<p>如果你管理多个仪表盘和每个仪表盘下的许多不同的面板，搜索面板标题可以节省滚动仪表盘或在仪表盘之间切换以找到正确面板的时间。随着搜索功能的最新更新，你现在可以按标题搜索面板。</p> 
<p><img alt height="495" src="https://static.oschina.net/uploads/space/2022/0616/075855_6Ju5_4937141.png" width="700" referrerpolicy="no-referrer"></p> 
<h3>仪表盘中的 Trace 面板</h3> 
<p>在 Grafana 9.0 中，你现在可以在仪表盘中添加 Trace 面板，通过 Trace 视图来可视化，而不是在 Explore 模式中查看它们。这项功能目前在 Grafana 9.0 中处于测试阶段。</p> 
<h3>仪表盘预览</h3> 
<p>这个测试版功能提供了所有可用仪表盘的摘要概述，当名称不足时，可以帮助你快速找到你需要的仪表盘。</p> 
<p><img alt height="438" src="https://static.oschina.net/uploads/space/2022/0616/075908_iEzl_4937141.png" width="700" referrerpolicy="no-referrer"></p> 
<h3>新的导航</h3> 
<p>扩大导航栏，以便更好地了解 Grafana 的功能和你安装的集成。Grafana 9 还将引入一种方法，让你把你的仪表盘加注星标，并从导航菜单中轻松访问它们。你可以通过打开 <code>savedItems</code> 功能来选择访问被标记的仪表盘。</p> 
<h3>Grafana Alerting 的改进</h3> 
<p>在 v8.0 中，Grafana 引入了一种新的告警用户体验，以简化跨多个数据源和 Grafana 部署的告警创建和管理。在 Grafana 9.0 中，这是现在的默认设置，随着这一变化，Grafana 还进一步改善了告警体验 —— 特别是 UI 和文档。</p> 
<h3>下载</h3> 
<p>链接：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgrafana.com%2Fgrafana%2Fdownload" target="_blank">https://grafana.com/grafana/download</a></p> 
<p>更多详情可查看：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgrafana%2Fgrafana%2Freleases%2Ftag%2Fv9.0.0" target="_blank">https://github.com/grafana/grafana/releases/tag/v9.0.0</a></p>
                                        </div>
                                      
</div>
            