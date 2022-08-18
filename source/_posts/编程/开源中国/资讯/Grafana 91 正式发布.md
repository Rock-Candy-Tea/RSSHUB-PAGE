
---
title: 'Grafana 9.1 正式发布'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://oscimg.oschina.net/oscnet/up-6de77ab8c2260c0b017e39fb274c919cb49.png'
author: 开源中国
comments: false
date: Thu, 18 Aug 2022 07:31:00 GMT
thumbnail: 'https://oscimg.oschina.net/oscnet/up-6de77ab8c2260c0b017e39fb274c919cb49.png'
---

<div>   
<div class="content">
                                                                                            <p><span style="color:#000000">Grafana v9.1 现已<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgrafana.com%2Fdocs%2Fgrafana%2Flatest%2Fwhatsnew%2Fwhats-new-in-v9-1" target="_blank">发布</a>，此版本进行了多项改进，重点关注 Grafana 的可用性、性能和安全性。还包括共享和嵌入仪表板的新选项、搜索和导航增强功能、新面板选项以及其他身份验证功能，以及有关 Grafana Enterprise 中新的单点登录和基于角色的访问控制选项等的更多信息。</span></p> 
<p><strong><span style="color:#000000">Grafana 服务帐户普遍可用</span></strong></p> 
<p><span style="color:#000000">自 Grafana v8.5 以来，服务帐户一直处于测试阶段。在此期间，开发团队改进了 API 密钥的 UI 和迁移路径，可以将服务帐户添加到团队，并继承团队权限。要了解有关服务帐户的更多信息，可参阅</span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgrafana.com%2Fdocs%2Fgrafana%2Flatest%2Fadministration%2Fservice-accounts%2F" target="_blank">文档</a><span style="color:#000000">。</span></p> 
<p><span style="color:#000000">服务帐户是 Grafana 中机器访问的演变。用户可以为每个服务帐户创建多个具有独立到期日期的 API 令牌，并暂时禁用服务帐户而不将其删除。这些优势使服务帐户成为 Terraform 和其他应用程序向 Grafana 进行身份验证的更灵活的方式。服务帐户还可以在 Grafana Enterprise 中使用基于角色的访问控制。你可以通过授予服务帐户特定角色来限制它们可以执行的功能来提高安全性。</span></p> 
<p><span style="color:#000000"><img alt height="234" src="https://oscimg.oschina.net/oscnet/up-6de77ab8c2260c0b017e39fb274c919cb49.png" width="500" referrerpolicy="no-referrer"></span></p> 
<p style="text-align:start"><strong><span><span><span><span><span><span><span style="color:#000000"><span><span><span><span><span><span><span><span><span><span><span>JWT URL 嵌入</span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></strong></p> 
<p style="margin-left:0; margin-right:0; text-align:start"><span><span><span><span><span style="color:#393946"><span><span><span><span><span><span><span><span><span><span><span><span><span><span>现在可以通过直接在 Grafana 的 URL 中添加 JWT 令牌轻松地将 Grafana 嵌入到其他应用程序中，例如<code>https://example.grafana.net/dashboard/uuid?aut_token=<jwt_token></code>。当 JWT 令牌通过 request URL 传递到 Grafana 时，Grafana 会验证并验证链接到特定用户的令牌，从而允许访问该用户可以查看的仪表板。要查看 JWT URL 嵌入的实际效果，可参阅<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgrafana%2Fgrafana-iframe-oauth-sample" target="_blank">示例项目</a>。</span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></p> 
<p style="margin-left:0; margin-right:0; text-align:start"><span><span><span><span><span style="color:#393946"><span><span><span><span><span><span><span><span><span><span><span><span><span><span><img alt height="359" src="https://oscimg.oschina.net/oscnet/up-edc202f1bbf63d0b7f4a51e9b6cc86ef25b.png" width="500" referrerpolicy="no-referrer"></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></p> 
<p style="margin-left:0; margin-right:0; text-align:start"><strong><span><span><span><span><span style="color:#393946"><span><span><span><span><span><span><span><span><span><span><span><span><span><span>GitHub OAuth2 认证的组织角色映射</span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></strong></p> 
<p style="margin-left:0; margin-right:0; text-align:start">现在可以使用 GitHub OAuth2 通过<code>role_attribute_path</code>配置选项将用户或团队映射到特定的 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgrafana.com%2Fdocs%2Fgrafana%2Flatest%2Fadministration%2Froles-and-permissions%2F%23organization-roles" target="_blank">Grafana 组织角色。</a>Grafana 将使用 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fjmespath.org%2Fexamples.html" target="_blank">JMESPath</a> 进行路径查找和角色映射。有关详细信息，可参阅<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgrafana.com%2Fdocs%2Fgrafana%2Flatest%2Fsetup-grafana%2Fconfigure-security%2Fconfigure-authentication%2Fgithub%2F%23map-roles" target="_blank">文档</a>。</p> 
<p style="margin-left:0; margin-right:0; text-align:start"><img alt height="220" src="https://oscimg.oschina.net/oscnet/up-689284c4700f34b7c3ecdca5d2444679d24.png" width="500" referrerpolicy="no-referrer"></p> 
<p style="text-align:start"><strong><span><span><span><span><span><span><span style="color:#000000"><span><span><span><span><span><span><span><span><span><span><span>（Beta）面板标题搜索和搜索改进</span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></strong></p> 
<p style="margin-left:0; margin-right:0; text-align:start"><span style="color:#000000">改进了按面板标题搜索的性能。如果面板的标题与你的搜索查询匹配，它将显示在搜索结果中。此功能将在几周内向 Grafana Cloud 用户推出，或者可以通过启用<code>panelTitleSearch</code>功能切换来访问。</span></p> 
<p style="margin-left:0; margin-right:0; text-align:start"><span style="color:#000000">面板标题搜索使用更新的仪表板搜索方法。以前，Grafana 使用 SQL 数据库查询按标题查找仪表板。启用功能切换后，Grafana 可以构建所有仪表板的内存索引。要了解有关 Grafana 中搜索的更多信息，可参阅</span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgrafana.com%2Fdocs%2Fgrafana%2Flatest%2Fdashboards%2Fuse-dashboards%2F%23dashboard-search" target="_blank">文档</a>。</p> 
<p style="margin-left:0; margin-right:0; text-align:start"><img alt height="261" src="https://oscimg.oschina.net/oscnet/up-daa3ef583a3f1ad438d06a20acb8a8b9e15.png" width="500" referrerpolicy="no-referrer"></p> 
<p style="text-align:start"><strong><span><span><span><span><span><span><span style="color:#000000"><span><span><span><span><span><span><span><span><span><span><span>导航栏中加星标的仪表板</span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></strong></p> 
<p style="margin-left:0; margin-right:0; text-align:start"><span style="color:#000000">作为即将对 Grafana 导航进行改进的一部分，用户现在可以从导航栏中直接访问已加</span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgrafana.com%2Fdocs%2Fgrafana%2Flatest%2Fdashboards%2Fuse-dashboards%2F" target="_blank">星标的仪表板。</a></p> 
<p style="margin-left:0; margin-right:0; text-align:start"><img alt height="287" src="https://oscimg.oschina.net/oscnet/up-93b94a7cf7d980b99e776f2f647851654b7.png" width="500" referrerpolicy="no-referrer"></p> 
<p style="text-align:start"><strong><span><span><span><span><span><span><span style="color:#000000"><span><span><span><span><span><span><span><span><span><span><span>热图改进</span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></strong></p> 
<p style="margin-left:0; margin-right:0; text-align:start"><span style="color:#000000">9.0 版中宣布的 beta 热图现在在整个 Grafana 中使用。它的性能得到了改进，现在支持 </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgrafana.com%2Fdocs%2Fgrafana%2Flatest%2Fbasics%2Fexemplars%2F" target="_blank">exemplars</a>。要了解有关热图面板的更多信息，可参阅<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgrafana.com%2Fdocs%2Fgrafana%2Flatest%2Fvisualizations%2Fheatmap%2F" target="_blank">文档</a>。</p> 
<p style="margin-left:0; margin-right:0; text-align:start"><img alt height="255" src="https://oscimg.oschina.net/oscnet/up-157c334ddce17eeb74a1d88ad5f1a93a169.png" width="500" referrerpolicy="no-referrer"></p> 
<p style="text-align:start"><strong><span><span><span><span><span><span><span style="color:#000000"><span><span><span><span><span><span><span><span><span><span><span>Geomap</span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></strong></p> 
<p style="margin-left:0; margin-right:0; text-align:start"><span><span><span><span><span style="color:#393946"><span><span><span><span><span><span><span><span><span><span><span><span><span><span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgrafana.com%2Fdocs%2Fgrafana%2Flatest%2Fvisualizations%2Fgeomap%2Fcontrols%2F%23show-measure-tools" target="_blank">现在可以使用面板的新测量工具</a>来测量 Geomap 可视化上的距离和面积。要了解有关 Geomap 面板的更多信息，可参阅<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgrafana.com%2Fdocs%2Fgrafana%2Flatest%2Fvisualizations%2Fgeomap%2F" target="_blank">文档</a>。</span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></p> 
<p style="margin-left:0; margin-right:0; text-align:start"><span><span><span><span><span style="color:#393946"><span><span><span><span><span><span><span><span><span><span><span><span><span><span><img alt height="383" src="https://oscimg.oschina.net/oscnet/up-b1bc8b1c0669f704714dfc2c5344e82d5bb.png" width="500" referrerpolicy="no-referrer"></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></p> 
<p style="text-align:start"><strong><span><span><span><span><span><span><span style="color:#000000"><span><span><span><span><span><span><span><span><span><span><span>(Alpha) 公共仪表板</span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></strong></p> 
<p style="margin-left:0; margin-right:0; text-align:start"><span><span><span><span><span style="color:#393946"><span><span><span><span><span><span><span><span><span><span><span><span><span><span>公共仪表板可作为 Alpha 功能使用，可通过<code>publicDashboards</code>功能切换启用。</span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span><span><span><span><span><span style="color:#393946"><span><span><span><span><span><span><span><span><span><span><span><span><span><span>可以为要公开共享的仪表板生成链接。知道该链接的任何人都可以访问该仪表板，而不能访问其他任何内容。</span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></p> 
<p style="margin-left:0; margin-right:0; text-align:start"><span><span><span><span><span style="color:#393946"><span><span><span><span><span><span><span><span><span><span><span><span><span><span>仪表板的公共视图有一些限制：</span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></p> 
<ul> 
 <li>不能通过公共仪表板对你的数据源运行任意查询。公共仪表板只能执行存储在原始仪表板上的查询。</li> 
 <li>公共仪表板是以 read-only kiosk view 显示的。</li> 
 <li>时间范围固定为仪表板默认时间范围。</li> 
</ul> 
<p style="margin-left:0; margin-right:0; text-align:start"><span><span><span><span><span style="color:#393946"><span><span><span><span><span><span><span><span><span><span><span><span><span><span>要了解更多信息，可参阅<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgrafana.com%2Fdocs%2Fgrafana%2Flatest%2Fdashboards%2Fdashboard-public%2F" target="_blank">文档</a>。</span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></p> 
<p style="text-align:start"><span style="color:#000000"><strong>Grafana Alerting 的配置改进</strong></span></p> 
<p style="margin-left:0; margin-right:0; text-align:start"><span style="color:#000000">可以直接从磁盘配置 Grafana Alerting 资源。Grafana Alerting 的配置当前支持以下资源：</span></p> 
<ul> 
 <li><span style="color:#000000">Alert rules</span></li> 
 <li><span style="color:#000000">Contact points</span></li> 
 <li><span style="color:#000000">Notification policies</span></li> 
 <li><span style="color:#000000">Mute timings</span></li> 
 <li><span style="color:#000000">Text templates</span></li> 
</ul> 
<p style="margin-left:0; margin-right:0; text-align:start"><span style="color:#000000">有关详细信息，可参阅</span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgrafana.com%2Fdocs%2Fgrafana%2Flatest%2Fadministration%2Fprovisioning%2F" target="_blank">文档</a>。</p> 
<p style="margin-left:0; margin-right:0; text-align:start"><span style="color:#000000">更多版本更新内容，可参阅完整的</span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgrafana%2Fgrafana%2Fblob%2Fmaster%2FCHANGELOG.md" target="_blank">变更日志</a>。</p>
                                        </div>
                                      
</div>
            