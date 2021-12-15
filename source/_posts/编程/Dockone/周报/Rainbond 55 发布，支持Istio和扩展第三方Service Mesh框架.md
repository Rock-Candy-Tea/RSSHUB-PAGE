
---
title: 'Rainbond 5.5 发布，支持Istio和扩展第三方Service Mesh框架'
categories: 
 - 编程
 - Dockone
 - 周报
headimg: 'https://grstatic.oss-cn-shanghai.aliyuncs.com/docs/5.5/community/change/goverance-change-example1.png'
author: Dockone
comments: false
date: 2021-12-15 10:08:33
thumbnail: 'https://grstatic.oss-cn-shanghai.aliyuncs.com/docs/5.5/community/change/goverance-change-example1.png'
---

<div>   
<br>Rainbond 5.5 版本主要优化扩展性。服务治理模式可以扩展第三方 ServiceMesh 架构，兼容kubernetes 管理命令和第三方管理平台。<br>
<br><h2>主要功能点解读：</h2><h3>1. 支持 Istio，并支持扩展第三方 ServiceMesh 框架</h3>Rainbond 专注于无侵入，松耦合的设计理念。在当前版本中，Rainbond 引入了应用级治理模式的切换功能，实现了服务治理能力的动态切换，无需业务逻辑变更，为业务提供了不同的治理能力。可以通过应用级插件的形式扩展第三方 ServcieMesh 框架，比如 Istio、Linkerd、Dapr 等，本次我们优先支持了Istio，用户可以通过 helm 安装 Istio 相关组件，实现应用治理模式的切换。从而享受到Istio相关的治理能力。如下图所示：<br>
<br><img src="https://grstatic.oss-cn-shanghai.aliyuncs.com/docs/5.5/community/change/goverance-change-example1.png" alt="image" referrerpolicy="no-referrer"><br>
<br><img src="https://grstatic.oss-cn-shanghai.aliyuncs.com/docs/5.5/community/change/goverance-change-example2.png" alt="image" referrerpolicy="no-referrer"><br>
<br>我们希望用户最终使用时，服务治理能力与业务逻辑是完全解耦的，用户可以根据不同的业务使用不同的治理能力。可以根据自己的需要扩展不同的治理模式，后续我们会有专门的文章来详细介绍如何扩展第三方 ServiceMesh 框架。<br>
<br><h3>2. 兼容 kubernetes 管理命令和第三方管理平台</h3>在之前的版本中，我们以应用为中心，使用户可以便捷的管理自己的业务。但通过Rainbond生成的名字空间、应用名和服务名使用 UUID，对熟悉 Kubernetes 的人非常不友好，在 Kubernetes 展示的 ID 无法跟业务关联，就无法使用 Kubernetes 命令或 Kubernetes 的第三方工具管理。因此我们现在支持了集群内各类资源的重命名。用户可以自定义团队、应用、服务、组件、镜像的英文名，在Kubernetes 中会以英文名展示。<br>
<br>用户设置了应用的英文名为 rbd，分别设置了组件的英文名后，在集群生成的资源如下图所示。<br>
<br><img src="https://grstatic.oss-cn-shanghai.aliyuncs.com/docs/5.5/community/change/english-name-example1.png" alt="images" referrerpolicy="no-referrer"><br>
<br><img src="https://grstatic.oss-cn-shanghai.aliyuncs.com/docs/5.5/community/change/english-name-example2.png" alt="images" referrerpolicy="no-referrer"><br>
<br><h2>详细变更点：</h2><h3>新增功能</h3><ul><li>【应用管理】支持Istio治理模式的切换；</li><li>【应用管理】支持修改应用和组件的集群资源名；</li></ul><br>
<br><h3>优化功能</h3><ul><li>【组件管理】优化组件构建的镜像名称；</li><li>【数据库】新版本集群数据库使用utf8mb4编码；</li><li>【升级】优化应用升级时无变更组件不进行更新操作；</li><li>【组件管理】优化组件首次设置健康检测的提示；</li></ul><br>
<br><h3>BUG 修复</h3><ul><li>【组件管理】修复实例运行内存为0的问题；</li><li>【网关】修复网关策略跳转页面错误的问题；</li><li>【应用管理】修复应用运行组件数展示错误的问题；</li><li>【应用管理】修复应用无法正常回滚的问题；</li><li>【插件管理】修复默认插件构建失败的问题；</li><li>【应用管理】修复发布应用时，插件分享事件同步发生错误的问题；</li><li>【插件管理】修复安装插件不生效的问题；</li><li>【组件管理】修复域名创建的第三方组件无法通过内部依赖访问的问题；</li><li>【应用管理】修复TCP策略网关端口可以随意设置的问题；</li><li>【升级】修复应用升级失败重试无响应的问题；</li><li>【应用管理】修复helm应用状态展示错误的问题；</li><li>【升级】修复回滚功能不可用的问题；</li><li>【组件管理】修复内部域名可以重复的问题；</li><li>【插件】修复插件内存不限制时报错的问题；</li><li>【升级】修复配置文件升级后无法修改的问题；</li><li>【组件管理】修复创建中组件无法继续部署的问题；</li></ul><br>
<br><h2>References Link</h2>[1] <a href="https://www.rainbond.com/docs/quick-start/quick-install?channel=dockone">Rainbond 5.5安装</a><br>
[2] <a href="https://www.rainbond.com/docs/upgrade/5.5.0-upgrade?channel=dockone">Rainbond 5.4升级到5.5</a><br>
[3] <a href="https://www.rainbond.com/docs/user-manual/app-manage/deploy-istio?channel=dockone">Istio控制平面安装</a><br>
<br>----<br>
<br><a href="https://www.rainbond.com/?channel=dockone">Rainbond</a> 是一个开源的云原生应用管理平台，使用简单，不需要懂容器和Kubernetes，支持管理多个Kubernetes集群，提供企业级应用的全生命周期管理，功能包括应用开发环境、应用市场、微服务架构、应用持续交付、应用运维、应用级多云管理等。<br>
<br>Github：<a href="https://github.com/goodrain/rainbond" rel="nofollow" target="_blank">https://github.com/goodrain/rainbond</a><br>
<br>官网：<a href="https://www.rainbond.com/?channel=dockone" rel="nofollow" target="_blank">https://www.rainbond.com?channel=dockone</a><br>
<br>微信群：请搜索添加群助手微信号 <strong>wylhzmyj</strong><br>
<br>钉钉群：请搜索群号 <strong>31096419</strong>
                                
                                                              
</div>
            