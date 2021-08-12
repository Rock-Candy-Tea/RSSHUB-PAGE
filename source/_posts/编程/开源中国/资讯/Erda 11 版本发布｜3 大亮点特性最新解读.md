
---
title: 'Erda 1.1 版本发布｜3 大亮点特性最新解读'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://oscimg.oschina.net/oscnet/up-073e01349b63716f93fea11502ba7e9c66c.png'
author: 开源中国
comments: false
date: Thu, 12 Aug 2021 13:25:00 GMT
thumbnail: 'https://oscimg.oschina.net/oscnet/up-073e01349b63716f93fea11502ba7e9c66c.png'
---

<div>   
<div class="content">
                                                                                            <p><img alt src="https://oscimg.oschina.net/oscnet/up-073e01349b63716f93fea11502ba7e9c66c.png" referrerpolicy="no-referrer"></p> 
<p><strong>Erda v1.1 Changelog</strong>： <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Ferda-project%2Ferda%2Fblob%2Fmaster%2FCHANGELOG%2FCHANGELOG-1.x.md" target="_blank"><em>https://github.com/erda-project/erda/blob/master/CHANGELOG/CHANGELOG-1.x.md</em></a> ​</p> 
<p>Erda 是由端点开源的一站式云原生 PaaS 平台，项目自开源发布以来，吸引了众多相关领域的专家和开发者们的关注，在大家的积极反馈下，社区的开发工作发展迅速。2021 年 7 月 27 日晚，Erda 1.1 版本正式发布，主要新增了 3 项重要功能，分别是：</p> 
<ul> 
 <li>支持项目级应用</li> 
 <li>项目协同事项变更消息订阅</li> 
 <li>支持导入用户已有 K8s 集群</li> 
</ul> 
<p>​以上 3 项重要功能的开发需求来自社区众多用户的实际反馈。此外，Erda v1.1 还新增了一些 bug 的修复和文档的更新，欢迎使用体验 Erda v1.1！感谢为本次版本做出贡献的社区小伙伴，我们将会继续广泛关注和采纳社区的建议，推动 Erda 项目的进一步发展，期待听到大家更多的反馈！ ​</p> 
<p>下文是本次版本发布功能的进一步介绍。 ​</p> 
<h1>Erda v1.1 亮点特性</h1> 
<h2>1. 支持项目级应用</h2> 
<p>​目前，Erda 平台中所有的 CI/CD 都是在最小单元应用层进行的，但是实际产品或者解决方案开发过程中构建部署的场景往往是复杂多样性的，项目级的构建部署、自动化测试和制品发布也是实际场景中经常遇到的需求。在只有应用层构建部署的情况下，没有一个很优雅的方案来解决以上问题。 ​</p> 
<p>为了能够优雅解决上述问题，Erda 技术团队基于现有产品以应用为中心和 IaC 的理念，在 Erda 1.1 版本中支持了项目级应用。项目级应用本质上还是一个应用，仍通过 pipeline.yml 管理 CI/CD 的流水线过程，不同的是该 pipeline 流水线不仅仅是本应用代码构建、部署等 Action 能力的调用，还能对项目下其他应用的流水线进行编排和调用执行，从而实现项目级的应用部署功能。 ​</p> 
<p>具体的使用方法也非常简单，只要在 pipeline.yml 编排中选择应用构建、其他应用 pipeline 执行的 Action 即可。 ​</p> 
<p><strong>功能部分演示视频链接：</strong><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.bilibili.com%2Fvideo%2FBV12y4y1j7zW%2F" target="_blank"><strong>https://www.bilibili.com/video/BV12y4y1j7zW/</strong></a> ​</p> 
<h2>2. 项目协同事项变更消息订阅</h2> 
<p>如何在一个平台让不同的研发角色进行高效协作，一直是项目管理的难点。Erda 平台也在始终致力于打造一个这样的协作平台，目前已经具备 milestone、backlog、sprint、requirement、task、bug 等管理功能，但是在事项订阅通知方面做的还不够好，不能及时接收到自己关注事项的变更通知，这在很大程度上阻碍了异步协同的高效性。 ​</p> 
<p>为此，在 Erda 1.1 版本中，我们增加了事项订阅的功能，让用户能够自定义关注自身的相关事项、当事项内容、状态、备注等发生变动时，都能够接收到站内信和邮件通知。 ​</p> 
<h1>支持导入已有集群</h1> 
<p>当前，在 K8s 盛行的背景下，平台用户往往已经搭建一个或多个 K8s 集群，那么如何导入用户已构建集群进行复用呢？我们在 1.1 版本中提供了白屏化的集群导入方式，方便用户有效合理复用已有资源。 ​</p> 
<p>集群导入的方式支持原生的 Kuberconfig、Account 和平台 Agent 三种模式，多元化的集群导入管理方式更方便用户便捷导入。 ​</p> 
<h1>更多特性</h1> 
<ul> 
 <li>手工测试用例支持异步导入导出</li> 
 <li>缺陷新增关闭日期的查看和筛选</li> 
 <li>事项协同-待处理页面支持翻页</li> 
 <li>代码仓库克隆地址优化</li> 
 <li>事项编辑滑窗及描述区块大小优化</li> 
 <li>事项协同表格支持调整分页大小</li> 
 <li>容器日志下载文件名和后缀格式优化：服务名_时间戳.log</li> 
</ul> 
<p><strong>Erda v1.1 Changelog</strong>： <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Ferda-project%2Ferda%2Fblob%2Fmaster%2FCHANGELOG%2FCHANGELOG-1.x.md" target="_blank"><em>https://github.com/erda-project/erda/blob/master/CHANGELOG/CHANGELOG-1.x.md</em></a> <strong>​</strong></p> 
<h1>总结</h1> 
<p>本次 Erda 1.1 版本的发布，主要增强了平台 SaaS 化能力，解决社区用户使用 Erda 过程中反馈的问题。主要表现在以下三个方面： ​</p> 
<ul> 
 <li>支持项目级应用</li> 
 <li>项目协同事项变更消息订阅</li> 
 <li>支持导入用户已有 K8s 集群</li> 
</ul> 
<p><strong>如果你有任何疑问，欢迎添加小助手微信（Erda202106）加入交流群，参与交流和讨论！</strong> <strong>​</strong></p> 
<ul> 
 <li>Erda Github 地址：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Ferda-project%2Ferda" target="_blank">https://github.com/erda-project/erda</a></li> 
 <li>Erda Cloud 官网：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.erda.cloud%2F" target="_blank">https://www.erda.cloud/</a></li> 
</ul>
                                        </div>
                                      
</div>
            