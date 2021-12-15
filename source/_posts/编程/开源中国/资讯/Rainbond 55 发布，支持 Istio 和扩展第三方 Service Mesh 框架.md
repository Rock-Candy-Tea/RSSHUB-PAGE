
---
title: 'Rainbond 5.5 发布，支持 Istio 和扩展第三方 Service Mesh 框架'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://grstatic.oss-cn-shanghai.aliyuncs.com/docs/5.5/community/change/goverance-change-example1.png'
author: 开源中国
comments: false
date: Wed, 15 Dec 2021 14:13:00 GMT
thumbnail: 'https://grstatic.oss-cn-shanghai.aliyuncs.com/docs/5.5/community/change/goverance-change-example1.png'
---

<div>   
<div class="content">
                                                                    
                                                        <p>Rainbond 5.5 版本主要优化扩展性。服务治理模式可以扩展第三方 ServiceMesh 架构，兼容kubernetes 管理命令和第三方管理平台。</p> 
<h3>主要功能点解读：</h3> 
<h4>1. 支持 Istio，并支持扩展第三方 ServiceMesh 框架</h4> 
<p>Rainbond 专注于无侵入，松耦合的设计理念。在当前版本中，Rainbond 引入了应用级治理模式的切换功能，实现了服务治理能力的动态切换，无需业务逻辑变更，为业务提供了不同的治理能力。可以通过应用级插件的形式扩展第三方 ServcieMesh 框架，比如 Istio、Linkerd、Dapr 等，本次我们优先支持了Istio，用户可以通过 helm 安装 Istio 相关组件，实现应用治理模式的切换。从而享受到Istio相关的治理能力。如下图所示：</p> 
<p><img alt="image" src="https://grstatic.oss-cn-shanghai.aliyuncs.com/docs/5.5/community/change/goverance-change-example1.png" referrerpolicy="no-referrer"></p> 
<p><img alt="image" src="https://grstatic.oss-cn-shanghai.aliyuncs.com/docs/5.5/community/change/goverance-change-example2.png" referrerpolicy="no-referrer"></p> 
<p>我们希望用户最终使用时，服务治理能力与业务逻辑是完全解耦的，用户可以根据不同的业务使用不同的治理能力。可以根据自己的需要扩展不同的治理模式，后续我们会有专门的文章来详细介绍如何扩展第三方 ServiceMesh 框架。</p> 
<h4>2. 兼容 kubernetes 管理命令和第三方管理平台</h4> 
<p>在之前的版本中，我们以应用为中心，使用户可以便捷的管理自己的业务。但通过Rainbond生成的名字空间、应用名和服务名使用 UUID，对熟悉 Kubernetes 的人非常不友好，在 Kubernetes 展示的 ID 无法跟业务关联，就无法使用 Kubernetes 命令或 Kubernetes 的第三方工具管理。因此我们现在支持了集群内各类资源的重命名。用户可以自定义团队、应用、服务、组件、镜像的英文名，在Kubernetes 中会以英文名展示。</p> 
<p>用户设置了应用的英文名为 rbd，分别设置了组件的英文名后，在集群生成的资源如下图所示。</p> 
<p><img alt="images" src="https://grstatic.oss-cn-shanghai.aliyuncs.com/docs/5.5/community/change/english-name-example1.png" referrerpolicy="no-referrer"></p> 
<p><img alt="images" src="https://grstatic.oss-cn-shanghai.aliyuncs.com/docs/5.5/community/change/english-name-example2.png" referrerpolicy="no-referrer"></p> 
<h3>详细变更点：</h3> 
<h3>新增功能</h3> 
<ul> 
 <li>【应用管理】<strong>支持Istio治理模式的切换；</strong></li> 
 <li>【应用管理】<strong>支持修改应用和组件的集群资源名；</strong></li> 
</ul> 
<h3>优化功能</h3> 
<ul> 
 <li>【组件管理】<strong>优化组件构建的镜像名称；</strong></li> 
 <li>【数据库】<strong>新版本集群数据库使用utf8mb4编码；</strong></li> 
 <li>【升级】<strong>优化应用升级时无变更组件不进行更新操作</strong>；</li> 
 <li>【组件管理】<strong>优化组件首次设置健康检测的提示</strong>；</li> 
</ul> 
<h3>BUG 修复</h3> 
<ul> 
 <li>【组件管理】<strong>修复实例运行内存为0的问题；</strong></li> 
 <li>【网关】<strong>修复网关策略跳转页面错误的问题；</strong></li> 
 <li>【应用管理】<strong>修复应用运行组件数展示错误的问题；</strong></li> 
 <li>【应用管理】<strong>修复应用无法正常回滚的问题；</strong></li> 
 <li>【插件管理】<strong>修复默认插件构建失败的问题；</strong></li> 
 <li>【应用管理】<strong>修复发布应用时，插件分享事件同步发生错误的问题；</strong></li> 
 <li>【插件管理】<strong>修复安装插件不生效的问题；</strong></li> 
 <li>【组件管理】<strong>修复域名创建的第三方组件无法通过内部依赖访问的问题；</strong></li> 
 <li>【应用管理】<strong>修复TCP策略网关端口可以随意设置的问题；</strong></li> 
 <li>【升级】<strong>修复应用升级失败重试无响应的问题</strong>；</li> 
 <li>【应用管理】<strong>修复helm应用状态展示错误的问题；</strong></li> 
 <li>【升级】<strong>修复回滚功能不可用的问题；</strong></li> 
 <li>【组件管理】<strong>修复内部域名可以重复的问题；</strong></li> 
 <li>【插件】<strong>修复插件内存不限制时报错的问题；</strong></li> 
 <li>【升级】<strong>修复配置文件升级后无法修改的问题；</strong></li> 
 <li>【组件管理】<strong>修复创建中组件无法继续部署的问题；</strong></li> 
</ul> 
<h3>References Link</h3> 
<p>[1] Rainbond 5.5安装: <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.rainbond.com%2Fdocs%2Fquick-start%2Fquick-install%3Fchannel%3Doschina" target="_blank">https://www.rainbond.com/docs/quick-start/quick-install?channel=oschina</a></p> 
<p>[2] Rainbond 5.4升级到5.5: <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.rainbond.com%2Fdocs%2Fupgrade%2F5.5.0-upgrade%3Fchannel%3Doschina" target="_blank">https://www.rainbond.com/docs/upgrade/5.5.0-upgrade?channel=oschina</a></p> 
<p>[3] Istio控制平面安装: <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.rainbond.com%2Fdocs%2Fuser-manual%2Fapp-manage%2Fdeploy-istio%3Fchannel%3Doschina" target="_blank">https://www.rainbond.com/docs/user-manual/app-manage/deploy-istio?channel=oschina</a></p> 
<hr> 
<p>Rainbond 是一个开源的云原生应用管理平台，使用简单，不需要懂容器和Kubernetes，支持管理多个Kubernetes集群，提供企业级应用的全生命周期管理，功能包括应用开发环境、应用市场、微服务架构、应用持续交付、应用运维、应用级多云管理等。</p> 
<p>Github：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgoodrain%2Frainbond" target="_blank">https://github.com/goodrain/rainbond</a></p> 
<p>官网：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.rainbond.com%3Fchannel%3Doschina" target="_blank">https://www.rainbond.com?channel=oschina</a></p> 
<p>微信群：请搜索添加群助手微信号 wylhzmyj</p>
                                        </div>
                                      
</div>
            