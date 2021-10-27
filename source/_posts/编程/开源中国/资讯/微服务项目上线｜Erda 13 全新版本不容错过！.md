
---
title: '微服务项目上线｜Erda 1.3 全新版本不容错过！'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://oscimg.oschina.net/oscnet/5c060a8f-f12f-4a6b-96f6-98736d8d31b8.png'
author: 开源中国
comments: false
date: Wed, 27 Oct 2021 17:50:00 GMT
thumbnail: 'https://oscimg.oschina.net/oscnet/5c060a8f-f12f-4a6b-96f6-98736d8d31b8.png'
---

<div>   
<div class="content">
                                                                                            <p style="color:#333333; margin-left:0px; margin-right:0px"><img src="https://oscimg.oschina.net/oscnet/5c060a8f-f12f-4a6b-96f6-98736d8d31b8.png" referrerpolicy="no-referrer"></p> 
<p style="color:#333333; margin-left:0px; margin-right:0px"><span style="color:#474444">Erda V1.3 Changelog：</span></p> 
<p style="color:#333333; margin-left:0px; margin-right:0px"><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Ferda-project%2Ferda%2Fblob%2Fmaster%2FCHANGELOG%2FCHANGELOG-1.x.md" target="_blank"><em><span style="color:#7d71f1">https://github.com/erda-project/erda/blob/master/CHANGELOG/CHANGELOG-1.x.md</span></em></a></p> 
<p style="color:#333333; margin-left:8px; margin-right:8px"><span style="color:#474444">9 月底，Erda 1.3 版本正式发布。</span></p> 
<p style="color:#333333; margin-left:8px; margin-right:8px"><span style="color:#474444">本次重点发布了 Kubernetes 集群管理控制台、第三方应用接入微服务项目的新特性，总计 49 项新特性和改善事项。用户可以通过 Erda 1.3 版本在 Kubernetes 集群控制管理上做到更精细化的运维管理。同时，1.3 版本上线的微服务项目，可让外置应用也能接入使用微服务平台能力。</span></p> 
<p style="color:#333333; margin-left:8px; margin-right:8px"><span style="color:#474444">再次感谢为本次版本做出贡献的社区小伙伴，期待大家继续通过：</span><span style="color:#474444">https://github.com/erda-project/erda/issue </span><span style="color:#474444">提交建议，我们将会持续关注和采纳社区建议，推动 Erda 项目进一步发展，期待听到大家更多的反馈！</span></p> 
<p style="color:#333333; margin-left:8px; margin-right:8px"><span style="color:#474444">下面让我们一起看看 Erda 1.3 版本的重点更新内容。</span></p> 
<h3><span>Erda 1.3 版本核心亮点</span></h3> 
<p> <strong><span style="color:#7d71f1">Kubernetes 集群管理控制台发布</span><span style="color:#474444"> </span></strong></p> 
<p style="color:#333333; margin-left:8px; margin-right:8px"><span style="color:#474444">在 Erda 1.1 版本中，平台完善了支持用户已有 Kubernetes 集群（下文中统称 K8S 集群）导入的功能，虽然在 K8S 集群维护管理方面，平台有节点和节点上服务列表的管理，但是对于 K8S 集群全方位的维护管理方面还是有所欠缺的，比如：缺少以集群维度查看 Pods 信息、工作负载信息、集群在线 kubeclt 工具以及事件日志查看等功能。</span></p> 
<p style="color:#333333; margin-left:8px; margin-right:8px"><span style="color:#474444">本次 1.3 版本发布的 K8S 集群管理控制台，是为了弥补和完善 K8S 集群管理能力，从节点、Pod、工作负载、在线 Kubeclt 工具和事件日志全维度的覆盖，让 K8S 集群的管理维护人员能够真正在线白屏化操作。</span></p> 
<p> <strong><span style="color:#7d71f1">增加微服务治理项目类型</span></strong></p> 
<p style="color:#333333; margin-left:8px; margin-right:8px"><span style="color:#474444">微服务治理项目类型增加之前，Erda 微服务治理平台功能只能提供给自身流水线部署起来的项目使用，对于通过第三方工具构建部署的项目来说，不能很友好的支持第三方应用接入的能力，最终导致第三方项目应用对接 Erda 微服务治理平台时，需要双方进行点对点的开发配置，无形之中把对微服务治理有强烈需求的用户拒之门外。</span></p> 
<p style="color:#333333; margin-left:8px; margin-right:8px"><span style="color:#474444">为了解决上述问题，Erda 1.3 版本在创建项目时增加了微服务治理项目类型的选择，支持 opentracing 标准的接入，让在其他平台构建部署起来的应用也能够便捷对接使用微服务治理能力。</span></p> 
<h3 style="color:#333333; margin-left:8px; margin-right:8px"><span>更多特性</span></h3> 
<ul style="list-style-type:disc; margin-left:8px; margin-right:8px"> 
 <li> <p><span style="color:#474444">新增平台管理员和平台审计员角色。</span><span> </span><span style="color:#474444">#1031</span></p> </li> 
 <li> <p><span style="color:#474444">项目协同筛选条件支持保存<span> </span></span><span style="color:#474444">#1753</span></p> </li> 
</ul> 
<ul style="list-style-type:disc; margin-left:8px; margin-right:8px"> 
 <li> <p><span style="color:#474444">站内信支持一键标记已读。</span><span> </span><span style="color:#474444">#1593</span></p> </li> 
 <li> <p><span style="color:#474444">流水线构建镜像支持第三方 docker registry<span> </span></span><span style="color:#474444">#1628 </span><span> </span><span style="color:#474444">#175</span></p> </li> 
</ul> 
<ul style="list-style-type:disc; margin-left:8px; margin-right:8px"> 
 <li> <p><span style="color:#474444">项目协同「状态筛选项」优化为使用用户设定的状态名筛选<span> </span></span><span style="color:#474444">#1649</span></p> </li> 
 <li> <p><span style="color:#474444">代码仓库访问安全性增强。</span><span> </span><span style="color:#474444">#1607</span><span> </span><span style="color:#474444">#1663</span></p> </li> 
</ul> 
<ul style="list-style-type:disc; margin-left:8px; margin-right:8px"> 
 <li> <p><span style="color:#474444">优化链路追踪查询功能，改进链路查询操作体验，优化 trace 详情展示。</span><span> </span><span style="color:#474444">#1553</span></p> </li> 
 <li> <p><span style="color:#474444">优化事务分析功能，增加 MQ 调用分析。</span><span> </span><span style="color:#474444">#1676</span></p> </li> 
</ul> 
<p><span style="color:#474444">我们致力于决社区用户在实际生产环境中反馈的问题和需求，如果您有任何疑问或建议，欢迎添加小助手微信：</span><span> </span><strong><span style="color:#7d71f1">Erda202106</span></strong><span> </span><span style="color:#474444">，加入 Erda 用户群参与交流或在 Github 上与我们讨论！</span></p> 
<ul style="list-style-type:disc; margin-left:8px; margin-right:8px"> 
 <li> <p><span style="color:#474444">Erda Github 地址：</span><span> </span><span style="color:#474444">https://github.com/erda-project/erda</span></p> </li> 
 <li> <p><span style="color:#474444">Erda Cloud 官网：</span><span> </span><span style="color:#474444">https://www.erda.cloud/</span></p> </li> 
</ul> 
<p style="color:#333333; margin-left:0px; margin-right:0px"><img src="https://oscimg.oschina.net/oscnet/e5527e82-e45f-46f1-8978-efde6b71eafd.jpg" referrerpolicy="no-referrer"></p>
                                        </div>
                                      
</div>
            