
---
title: 'Rainbond V5.8 发布，提升 Kubernetes 管理体验，接管 Kubernetes 已有应用'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://grstatic.oss-cn-shanghai.aliyuncs.com/docs/5.8/community/change/import-region-resource.png'
author: 开源中国
comments: false
date: Wed, 10 Aug 2022 17:59:00 GMT
thumbnail: 'https://grstatic.oss-cn-shanghai.aliyuncs.com/docs/5.8/community/change/import-region-resource.png'
---

<div>   
<div class="content">
                                                                                            <p>Rainbond 是 <code>以应用为中心</code> 的云原生应用管理平台。相比于其他容器管理平台，提供了更易用的应用管理体验。这是一个优点，但是另一方面，由于应用级抽象与实际 Kubernetes 资源有所差异，对于许多已经熟悉 Kubernetes 的用户而言，使用 Rainbond 又会面临以下问题：</p> 
<ul> 
 <li> <p>Rainbond 对 Kubernetes 资源支持有限。在某些场景下，如环境变量引用某个 Secret 的值、调整 Pod 的调度策略、亲和性配置等场景难以实现。</p> </li> 
 <li> <p>在 Kubernetes 集群中已经部署的应用。如何迁移到 Rainbond 上，许多配置需要再次手动调整部署，迁移成本高。</p> </li> 
 <li> <p>已有的 Kubernetes Yaml 文件，在 Rainbond 上无法直接部署。</p> </li> 
</ul> 
<p>为了解决以上问题，我们在 5.8 版本中主要做了如下改进：</p> 
<ul> 
 <li> <p>支持一键导入 Kubernetes 集群中已存在的应用，我们可以将集群中已有应用直接导入到 Rainbond 进行管理。</p> </li> 
 <li> <p>兼容 Kubernetes 的资源和属性，支持在应用下通过 Yaml 文件创建各类资源，如 PVC、PV、Secret等。在应用下创建的资源，可以在组件里进行引用。同时支持了发布到应用模版。</p> </li> 
 <li> <p>支持通过 Yaml 文件部署组件，我们会将 Yaml 文件中识别到的资源转化为 Rainbond 的内置组件，实现 Yaml 文件的一键部署。</p> </li> 
</ul> 
<p>总体来说，在本次版本中，Rainbond 在与 Kubernetes 底层的资源兼容性上又进了一步，许多以往不支持的资源也可以直接创建和使用。下面简单介绍下本次版本的主要功能。</p> 
<h2>主要功能点解读：</h2> 
<h3>1. 支持一键导入已有集群应用</h3> 
<p>对于在Kubernetes集群中已经运行的应用，我们支持了一键导入命名空间下的所有应用。当选择好要导入的命名空间时，我们可以看到该命名空间下的资源。我们会根据 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fkubernetes.io%2Fzh-cn%2Fdocs%2Fconcepts%2Foverview%2Fworking-with-objects%2Fcommon-labels%2F" target="_blank">Kubernetes 推荐标签</a> 来区分应用，将资源按应用区分出来。如下图所示: <img alt src="https://grstatic.oss-cn-shanghai.aliyuncs.com/docs/5.8/community/change/import-region-resource.png" referrerpolicy="no-referrer"></p> 
<p>这些资源中，Deployment/Statefulset/Job/CronJob 将会转化为内置组件，其他资源如果无法与 Rainbond 抽象模型对应，则会转化为应用下的 K8s 资源。在点击下一步后，你可以看到之前的资源与 Rainbond 模型的关系。如下图所示</p> 
<p><img alt src="https://grstatic.oss-cn-shanghai.aliyuncs.com/docs/5.8/docs/use-manual/team-manage/ns-to-team/advanced_resources.jpg" referrerpolicy="no-referrer"></p> 
<p>最终导入后，你就可以在 Rainbond 的团队中管理你的应用了。请参阅文档 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.rainbond.com%2Fdocs%2Fuse-manual%2Fteam-manage%2Fns-to-team%2F" target="_blank">Kubernetes 资源导入</a></p> 
<h3>2. 支持通过Yaml文件部署组件</h3> 
<p>许多用户自己编写 Yaml 部署应用，为了便于用户使用，我们同样支持了通过 Yaml 部署应用。与其他容器管理平台不同的是，在使用 Yaml 文件部署应用时，我们不是直接让 Yaml 文件在集群中生效，而是转化为我们的组件类型。以便于用户在部署后，还能使用到我们应用级的管理功能，如组件的全生命周期、组件编排、发布安装等。</p> 
<p>在添加组件时，选择 Yaml 部署后，上传你的文件。我们会在识别后转化为对应的组件模型和应用资源，如下图所示：</p> 
<p>请参阅文档 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.rainbond.com%2Fdocs%2Fuse-manual%2Fcomponent-create%2Fpackage-support%2Fyaml" target="_blank">基于 Yaml 部署组件</a></p> 
<p><img alt="yaml_team_handle.jpg" src="https://grstatic.oss-cn-shanghai.aliyuncs.com/docs/5.8/docs/use-manual/component-create/package-support/yaml_team_handle.jpg" referrerpolicy="no-referrer"></p> 
<h3>3. 兼容 Kubernetes 资源和属性</h3> 
<p>为了扩展应用和组件的能力，以及更好的兼容 Kubernetes 的资源。我们在应用下，新增了 <code>K8s 资源</code> 的入口，在这里可以通过 Yaml 部署集群中的各类资源。如 PV、PVC、Service、Ingress 等。在这里部署的资源均会直接被部署到集群中。这里我们定义的是，它应该是你应用运行所需要的基础环境。即这里提供的资源，应该是供当前应用下的组件进行使用的。在发布时，这里的资源也会和组件一起发布。</p> 
<p><img alt="k8s_resources_add.jpg" src="https://grstatic.oss-cn-shanghai.aliyuncs.com/docs/5.8/docs/use-manual/app-manage/k8s-resource/k8s_resources_add.jpg" referrerpolicy="no-referrer"></p> 
<p>同样在组件的其他设置下，有 Kubernetes 属性这一项。我们可以在这里定义该组件使用到的一些属性，如 volumes、volumeMounts 等。这里可以挂载应用下创建的 <code>K8s 资源</code>，用于扩展组件能力。</p> 
<ul> 
 <li>请参阅文档 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.rainbond.com%2Fdocs%2Fuse-manual%2Fapp-manage%2Fk8s-resource%2F" target="_blank">应用下 K8s 资源管理</a></li> 
 <li>请参阅文档 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.rainbond.com%2Fdocs%2Fuse-manual%2Fcomponent-manage%2Fother%2F" target="_blank">组件 Kubernetes 属性</a></li> 
</ul> 
<p><img alt="k8s_attr.jpg" src="https://grstatic.oss-cn-shanghai.aliyuncs.com/docs/5.8/community/change/k8s_attr.jpg" referrerpolicy="no-referrer"></p> 
<h3>4. 支持直接上传 Jar/War 包构建组件</h3> 
<p>在之前的版本中，当用户使用 Jar 包进行交付时，我们需要先创建一个 git 仓库，并将 Jar 包推上去才可以构建。这会带来几个问题：</p> 
<ul> 
 <li>创建新仓库操作繁琐，离线环境难以部署</li> 
 <li>git 仓库会限制单个文件大小，Jar 包过大时，无法上传</li> 
</ul> 
<p>因此为了解决以上问题，我们支持直接上传 Jar/War 包构建组件。如下图所示，我们可以在组件总览页查看到文件名，以及文件的 MD5 值。以便于在反复上传文件时区分版本。</p> 
<p>请参阅文档 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.rainbond.com%2Fdocs%2Fuse-manual%2Fcomponent-create%2Fpackage-support%2Fjar-war" target="_blank">基于 Jar / War 部署组件</a></p> 
<p><img alt="Pasted%20Graphic%204.pn" src="https://grstatic.oss-cn-shanghai.aliyuncs.com/docs/5.8/docs/use-manual/component-create/package-support/Pasted%20Graphic%204.png" referrerpolicy="no-referrer"></p> 
<h3>5. 支持切换组件构建源</h3> 
<p>当我们从应用市场安装一个完整应用，但应用中的部分组件需要从源码和镜像替换，这时就需要修改构建源。也就是说，如果我安装下来一个应用，想要替换其中的某个组件时，往往只能新建一个组件，重新编排依赖关系。操作较繁琐。尤其是在离线环境，发现安装的组件有问题时，调整后再发布，往往还需要再次刻盘。因此为了解决这种问题。在新版本中，我们支持直接将应用商店的组件构建源更改为镜像或者源码。以便于快速自测和交付。</p> 
<p><img alt="change_build_source.png" src="https://grstatic.oss-cn-shanghai.aliyuncs.com/docs/5.8/community/change/change_build_source.png" referrerpolicy="no-referrer"></p> 
<h3>6. 支持创建任务类型(Job/CronJob)的组件</h3> 
<p>在新版本中，我们的组件部署类型，在无状态组件和有状态组件的基础上，又扩展了两种类型，任务(Job)和周期性任务(CronJob), 现在如果需要创建一次性任务，可以通过更改组件部署类型修改。</p> 
<p>请参阅文档 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.rainbond.com%2Fdocs%2Fuse-manual%2Fcomponent-create%2Ftask-support%2Fjob-cronjob" target="_blank">部署Job \ CronJob类型组件</a></p> 
<h2>详细变更点</h2> 
<h3>新增功能</h3> 
<ul> 
 <li>【集群管理】 支持一键导入已有集群应用</li> 
 <li>【团队管理】 支持直接通过 Jar、War 包或 Yaml 文件部署组件</li> 
 <li>【组件管理】 支持创建 Job/CronJob 类型任务</li> 
 <li>【组件管理】 支持应用商店安装的组件修改构建源</li> 
 <li>【应用管理】 支持扩展应用和组件支持的属性</li> 
 <li>【组件管理】 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgoodrain%2Frainbond%2Fissues%2F1172" target="_blank">支持 Dockerfile 使用私有镜像构建</a></li> 
</ul> 
<h3>优化功能</h3> 
<ul> 
 <li>【组件管理】 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgoodrain%2Frainbond%2Fpull%2F1244" target="_blank">组件内存不限制时，内存展示实际使用量</a></li> 
</ul> 
<h3>BUG 修复</h3> 
<ul> 
 <li>【日志】 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgoodrain%2Frainbond%2Fpull%2F1211" target="_blank">修复组件构建日志缺失的问题</a></li> 
 <li>【应用管理】 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgoodrain%2Frainbond%2Fissues%2F1203" target="_blank">修复组件备份恢复失败的问题</a></li> 
 <li>【团队管理】 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgoodrain%2Frainbond%2Fissues%2F1279" target="_blank">修复团队列表内存和CPU数据错误的问题</a></li> 
 <li>【企业管理】 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgoodrain%2Frainbond%2Fissues%2F1254" target="_blank">修复非管理员用户登陆提示没有权限的问题</a></li> 
 <li>【组件管理】 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgoodrain%2Frainbond%2Fissues%2F1220" target="_blank">修复组件访问信息展示错乱的问题</a></li> 
 <li>【组件管理】 修复更换构建源后，源码构建参数未改变的问题</li> 
</ul> 
<h2>升级方式</h2> 
<p>支持从 5.7.1版本升级，<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.rainbond.com%2Fdocs%2Fupgrade%2F5.8.0-upgrade%2F" target="_blank">升级参考文档</a></p> 
<p>其他版本用户请依次版本升级请先升级到 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.rainbond.com%2Fdocs%2Fupgrade%2F5.7.1-upgrade%2F" target="_blank">5.7.1</a></p>
                                        </div>
                                      
</div>
            