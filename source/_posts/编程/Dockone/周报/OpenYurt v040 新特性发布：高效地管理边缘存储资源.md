
---
title: 'OpenYurt v0.4.0 新特性发布：高效地管理边缘存储资源'
categories: 
 - 编程
 - Dockone
 - 周报
headimg: 'https://ucc.alicdn.com/pic/developer-ecology/9a4c8b1cec3249ed9745f1272d3d828e.png'
author: Dockone
comments: false
date: 2021-06-07 12:37:51
thumbnail: 'https://ucc.alicdn.com/pic/developer-ecology/9a4c8b1cec3249ed9745f1272d3d828e.png'
---

<div>   
<br>作者 | 高文俊<br>
来源｜<a href="https://mp.weixin.qq.com/s/9xhnJNN2fWPUqz3MPlP1SQ">阿里巴巴云原生公众号</a><br>
​<br>
<h1>简介</h1>OpenYurt 是由阿里云开源的<strong>基于原生 Kubernetes 构建的、业内首个对于 Kubernetes 非侵入式的边缘计算项目</strong>，目标是扩展 Kubernetes 以无缝支持边缘计算场景。它提供了完整的 Kubernetes API 兼容性；支持所有 Kubernetes 工作负载、服务、运营商、CNI 插件和 CSI 插件；提供良好的节点自治能力和云边协同能力。OpenYurt 可以轻松部署在任何 Kubernetes 集群服务中，让强大的云原生能力扩展到边缘。<br>
​<br>
<h1>边缘本地存储</h1>​<br>
OpenYurt v0.4.0 版本推出全新特性：边缘本地存储管理，用于高效地管理边缘节点的存储资源，用户可以通过 ConfigMap 来动态配置集群内节点的本地资源，并能无缝对接 CSI 存储插件，通过原生的 PV/PVC 方式使用本地存储。<br>
​<br>
该项目组件主要包含两个部分， 一个是定义在集群中 kube-system namespace 的 node-resource-topo ConfigMap, 一个是部署在集群中 kube-system namespace 下面的 node-resource-manager Daemonset, 每个 Node 节点上的 node-resource-manager 通过挂载 node-resource-topo ConfigMap 的方式生产并管理用户定义的本地资源。架构如下：<br>
​<br>
<img src="https://ucc.alicdn.com/pic/developer-ecology/9a4c8b1cec3249ed9745f1272d3d828e.png" alt="1.png" referrerpolicy="no-referrer"><br>
<br>主要优点：<br>
<ul><li>简单易用：node-resource-manager 可以仅通过定义 ConfigMap 就完成对集群中的本地资源的初始化和更新。</li><li>易于集成：node-resource-manager 可以与 csi 插件集成来完成 kubernetes 集群中的相关本地资源的生命周期管理。</li><li>与云平台无关：node-resource-manager 可以轻松部署在任何完全兼容 Kubernetes API 的集群中。</li></ul><br>
<br>关于边缘本地存储设备管理的详情和使用方法，请参考 configmap.md：<br>
<a href="https://github.com/openyurtio/node-resource-manager/blob/main/docs/configmap.md">_</a><a href="https://github.com/openyurtio/node-resource-manager/blob/main/docs/configmap.md_" rel="nofollow" target="_blank">https://github.com/openyurtio/ ... p.md_</a>_。_<br>
​<br>
<h1>IOT 设备管理 API</h1>阿里联合 VMware 在 OpenYurt 社区推出了 IOT 边缘设备管理的 API 标准定义，API 基于 Kubernetes 的 CRD（custom resource definitions）模型实现。任何边缘平台只需实现对应 CRD Controller，即能通过这些 API 接入 OpenYurt 集群，完成面向终态的设备管理。<br>
​<br>
未来我们将继续基于 OpenYurt + EdgeX Foundry 来进行 IOT 等边缘场景下的探索，共建统一 API 下的多场景设备接入、使能和融合能力，打造云原生 IOT 领域标准。<br>
<br>关于 API 定义，请参考《Proposal: managing edge devices by integraing Edgex Foundry into OpenYurt》：<br>
<a href="https://github.com/openyurtio/openyurt/pull/236">_</a><a href="https://github.com/openyurtio/openyurt/pull/236_" rel="nofollow" target="_blank">https://github.com/openyurtio/openyurt/pull/236_</a><br>
_​_<br>
<br><h1>支持 Kubernetes 1.18 版本</h1>​<br>
OpenYurt 正式支持 Kubernetes 1.18 版本，用户可无缝转换 Kubernetes 1.18 集群至 OpenYurt 集群，并使用 1.18 版本的 API 和新特性。<br>
​<br>
<h1>更多特性</h1><ul><li><br><strong>YurtHub 支持 CRD 缓存</strong>，边缘应用可在云边断网情况下，使用 CRD 的扩展能力，如 Calico、各类自定义 Operator 等，请参见《Proposal: enhance the caching ability of YurtHub》：<a href="https://github.com/openyurtio/openyurt/pull/244">_</a><a href="https://github.com/openyurtio/openyurt/pull/244_" rel="nofollow" target="_blank">https://github.com/openyurtio/openyurt/pull/244_</a></li><li><br><strong>UnitedDeployment 支持 Patch 特性</strong>，UnitedDeployment controller 支持 在不同 nodepool 内进行 workload 的差异化配置，如 images、resources 等，请参见《Feature: UnitedDeployment support patch for pool》：<a href="https://github.com/openyurtio/yurt-app-manager/pull/12">_</a><a href="https://github.com/openyurtio/yurt-app-manager/pull/12_" rel="nofollow" target="_blank">https://github.com/openyurtio/ ... l/12_</a></li><li><br><strong>支持 Prometheus 和 Yurt-Tunnel-Server 跨节点部署</strong>，请参见《Feature: add dns controller to sync cluster node dns records》：<a href="https://github.com/openyurtio/openyurt/pull/270">_</a><a href="https://github.com/openyurtio/openyurt/pull/270_" rel="nofollow" target="_blank">https://github.com/openyurtio/openyurt/pull/270_</a> </li><li><br><strong>Yurtctl 支持 Kind 集群一键转换</strong>，请参见《Add support for the conversion between kind and OpenYurt cluster》：<a href="https://github.com/openyurtio/openyurt/pull/234">_</a><a href="https://github.com/openyurtio/openyurt/pull/234_" rel="nofollow" target="_blank">https://github.com/openyurtio/openyurt/pull/234_</a></li><li><br><strong>新增边缘容器网络特性说明</strong>，针对边缘弱网场景，提供边缘网络插件的定制化特性，如 MAC 地址保持，IP 地址保持，并提供相应代码参考和使用说明，请参见《add edge-pod-network doc》：<a href="https://github.com/openyurtio/openyurt/pull/302">_</a><a href="https://github.com/openyurtio/openyurt/pull/302_" rel="nofollow" target="_blank">https://github.com/openyurtio/openyurt/pull/302_</a></li><li><br><strong>制定社区治理规则</strong>，基于社区反馈，设立 Member，Reviewer，Approver，Maintainer 等角色，明确成员职责和准入、提升条件，规范化社区治理，鼓励社区同学参与共建，请参见：<a href="https://github.com/openyurtio/community/blob/main/community-membership.md">_</a><a href="https://github.com/openyurtio/community/blob/main/community-membership.md_" rel="nofollow" target="_blank">https://github.com/openyurtio/ ... p.md_</a></li></ul><br>
<br><h1>未来计划​</h1>OpenYurt V0.4.0 版本发布，提供了边缘本地存储管理，边缘 IOT 设备管理等全新能力，并发布了 Kubernetes 1.18 版本的支持，以及一系列扩展能力和优化。未来 OpenYurt 社区会在本地存储项目提供存储调度能力，在 IOT 设备管理领域持续投入和探索演进，在社区治理和贡献者体验方面加大建设力度，同时也非常欢迎有兴趣的同学加入参与共建，共同打造一个稳定、可靠的云原生边缘计算平台。<br>
​<br>
更多社区详情请关注：<a href="https://github.com/openyurtio/openyurt">_</a><a href="https://github.com/openyurtio/openyurt_" rel="nofollow" target="_blank">https://github.com/openyurtio/openyurt_</a>。<br>
<br><strong>相关链接</strong>：<br>
​<br>
- OpenYurt v0.4.0 CHANGELOG：<a href="https://github.com/openyurtio/openyurt/blob/master/CHANGELOG.md#v040">_</a><a href="https://github.com/openyurtio/openyurt/blob/master/CHANGELOG.md#v040_" rel="nofollow" target="_blank">https://github.com/openyurtio/ ... v040_</a><br>
- OpenYurt 使用教程：<a href="https://github.com/openyurtio/openyurt/tree/master/docs/tutorial">_</a><a href="https://github.com/openyurtio/openyurt/tree/master/docs/tutorial_" rel="nofollow" target="_blank">https://github.com/openyurtio/ ... rial_</a><br>
- OpenYurt 官网：<a href="https://openyurt.io/">_</a><a href="https://openyurt.io/_" rel="nofollow" target="_blank">https://openyurt.io/_</a>
                                
                                                              
</div>
            