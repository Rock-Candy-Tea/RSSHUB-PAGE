
---
title: 'SuperEdge v0.6.0 版本正式发布'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://oscimg.oschina.net/oscnet/up-cb0cccf9b4d4ed2d5427b28f4c89cb0eb93.png'
author: 开源中国
comments: false
date: Thu, 14 Oct 2021 17:21:00 GMT
thumbnail: 'https://oscimg.oschina.net/oscnet/up-cb0cccf9b4d4ed2d5427b28f4c89cb0eb93.png'
---

<div>   
<div class="content">
                                                                    
                                                        <p>作者：SuperEdge 开发者团队</p> 
<p>SuperEdge 是基于原生 Kubernetes 的分布式边缘云容器管理系统，由腾讯云牵头，联合英特尔、VMware 威睿、虎牙、寒武纪、美团、首都在线等多家厂商在2020年12月共同发起的边缘计算开源项目，旨在将把 Kubernetes 强大的容器管理能力无缝的扩展到边缘计算和分布式资源管理的场景中，为边缘 IoT，边缘 AI，边缘智慧行业等赋能，推动物联网和数字化的落地。目前已经成为 CNCF Sandbox 项目，由 CNCF 基金会进行托管。</p> 
<h2>SuperEdge v0.6.0 版本正式发布</h2> 
<p>SuperEdge 在2021-09-28发布了 v0.6.0 版本，具体 changelog 见：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fsuperedge%2Fsuperedge%2Freleases%2Ftag%2Fv0.6.0" target="_blank">https://github.com/superedge/superedge/releases/tag/v0.6.0</a></p> 
<p>经过社区技术讨论，本次更新主要聚焦于生产集成，让 SuperEdge 真正在用户生产环境落地，添加了本地持久化存储的支持，边缘 IoT 设备的接入，ServiceGroup 的部署状态和事件的反馈，以及对微服务使用框架 Tars、边缘应用监控数据的采集、Tengine AI 框架在 SuperEdge 使用的 Demo，具体内容如下：</p> 
<h3>集成 TopoLVM，支持边缘本地持久化存储</h3> 
<ul> 
 <li>动态配置 PV：创建 PVC 对象时自动创建边缘节点 PV 资源；</li> 
 <li>动态扩容存储容量：可编辑 PVC 对象自动扩容 PV 的容量；</li> 
 <li>容量指标采集：可从 kubelet 中采集容量指标，进行存储容量和读写监控；</li> 
 <li>扩展调度器存储策略：TopoLVM 扩展了 Kube-scheduler，使用 CSI 拓扑功能将 Pod 调度到 LVM 卷所在节点，并且可设置存储容量调度策略；</li> 
 <li>统一管理本地存储资源：可把多个物理卷组加入 VolumeGroup 中，屏蔽了底层物理卷细节，对 Pod 统一进行存储资源分配；</li> 
</ul> 
<p>该功能使用文档见：</p> 
<p><img alt height="300" src="https://oscimg.oschina.net/oscnet/up-cb0cccf9b4d4ed2d5427b28f4c89cb0eb93.png" width="300" referrerpolicy="no-referrer"></p> 
<h3>集成 EdgeX Foundry，接入边缘 IoT 设备</h3> 
<ul> 
 <li>集成了原生的 EdgeX Foundry，可以一键在 SuperEdge 边缘集群 Addon EdgeX Foundry 组件，进行边缘 IoT 组件的接入；</li> 
 <li>EdgeX Foundry 各组件可选，用户可根据自己需求部署自己需要的组件，所有组件属性用户可自定义；</li> 
</ul> 
<p>该功能使用文档见：</p> 
<p><img alt height="300" src="https://oscimg.oschina.net/oscnet/up-c69001c5cf01ddf9d508c1b2d5f1a876a5b.png" width="300" referrerpolicy="no-referrer"></p> 
<h3>添加 ServiceGroup 部署的状态和事件反馈</h3> 
<ul> 
 <li>添加 ServiceGroup 部署的状态和失败事件的反馈，增加用户对边缘站点应用状态的掌握和运维的便利性；</li> 
 <li>DeploymentGrid 使用 templateHasher 修改后的模版作为创建对象，避免创建后的立即更新操作；</li> 
 <li>Fix ServiceGroup 中使用的 event scheme；</li> 
</ul> 
<h3>添加3个使用 Demo</h3> 
<ul> 
 <li>添加在 SuperEdge 部署 Tars 的示例，帮助用户在边缘站点上使用 Tars 开发框架；</li> 
 <li>添加采集边缘应用监控数据的示例，以便用户接入边缘应用的监控，更好的掌握边缘应用的状态；</li> 
 <li>添加用 Tengine + SuperEdge 一条指令跨平台部署边缘AI应用示例，帮助用户在 SuperEdge 使用 AI 相关框架；</li> 
</ul> 
<p>Demo 用例使用文档：</p> 
<p><img alt height="300" src="https://oscimg.oschina.net/oscnet/up-f7c813b5de7b8c6708430eeaa30bd515a73.png" width="300" referrerpolicy="no-referrer"></p> 
<p>项目链接：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fsuperedge%2Fsuperedge" target="_blank">https://github.com/superedge/superedge</a></p> 
<p>Release 链接：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fsuperedge%2Fsuperedge%2Freleases%2Ftag%2Fv0.6.0" target="_blank">https://github.com/superedge/superedge/releases/tag/v0.6.0</a></p> 
<p>变更记录：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fsuperedge%2Fsuperedge%2Fblob%2Fmain%2FCHANGELOG%2FCHANGELOG-0.6.md" target="_blank">https://github.com/superedge/superedge/blob/main/CHANGELOG/CHANGELOG-0.6.md</a></p> 
<p>项目文档：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fsuperedge%2Fsuperedge%2Ftree%2Fmain%2Fdocs" target="_blank">https://github.com/superedge/superedge/tree/main/docs</a><img alt src="https://www.oschina.net/img/bVbLtIB" referrerpolicy="no-referrer"></p>
                                        </div>
                                      
</div>
            