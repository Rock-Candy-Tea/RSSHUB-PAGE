
---
title: 'Kubernetes 1.24 正式发布'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://oscimg.oschina.net/oscnet/up-9fea42a5a6e5f9584b494a0eac52bed926c.png'
author: 开源中国
comments: false
date: Wed, 04 May 2022 10:18:00 GMT
thumbnail: 'https://oscimg.oschina.net/oscnet/up-9fea42a5a6e5f9584b494a0eac52bed926c.png'
---

<div>   
<div class="content">
                                                                                            <p>Kubernetes 1.24 已正式发布，这也是 2022 年的首个大版本更新。</p> 
<p>1.24 总共有 46 项功能变化，其中包含：</p> 
<ul> 
 <li>14 项增强功能已升级为稳定状态</li> 
 <li>15 项增强功能正在进入测试阶段</li> 
 <li>13 项增强功能正在进入 alpha 阶段</li> 
 <li>两项功能已被标记为弃用状态</li> 
 <li>两项功能已被删除</li> 
</ul> 
<hr> 
<p><strong>主要变化</strong></p> 
<p><strong>从 kubelet 中删除 dockershim 组件</strong></p> 
<p>dockershim 组件在 1.20 中已被标记为弃用状态，最新的 1.24 版本则正式将其删除。从该版本开始，用户需要使用其他<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fkubernetes.io%2Fdocs%2Fsetup%2Fproduction-environment%2Fcontainer-runtimes%2F" target="_blank">受支持的运行时</a>（例如 containerd 或 CRI-O）。如果依赖 Docker Engine 作为运行时，则需要使用 cri-dockerd。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fkubernetes.io%2Fblog%2F2022%2F03%2F31%2Fready-for-dockershim-removal%2F" target="_blank">详情查看指南</a>。</p> 
<p><strong>默认关闭 Beta 状态的 API</strong></p> 
<p><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fkubernetes%2Fenhancements%2Fissues%2F3136" target="_blank">默认情况下，不会在集群中启用新的 beta API</a>。不过现有的 beta API 及其新版本将继续在 1.24 中启用。</p> 
<p><strong>提供的签名的发布工件 (Signing Release Artifacts)</strong></p> 
<p>在 1.24 中，发布工件会使用 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fsigstore%2Fcosign" target="_blank">cosign</a> <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fkubernetes%2Fenhancements%2Fissues%2F3031" target="_blank">进行签名，</a>同时提供实验性的镜像签名验证支持。发布工件的签名和验证是<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fkubernetes%2Fenhancements%2Fissues%2F3027" target="_blank">提升 Kubernetes 软件供应链安全性的一部分</a>。</p> 
<p><strong>OpenAPI v3</strong></p> 
<p>Kubernetes 1.24 为 API 的 OpenAPI v3 发布格式提供 beta 支持。</p> 
<p><strong>存储容量和存储卷扩展功能正式 GA</strong></p> 
<p style="text-align:left"><span><span><span><span style="color:#222222"><span><span><span><span><span><span><span><span><span><span><span style="background-color:#ffffff"><span><span><span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fkubernetes%2Fenhancements%2Fissues%2F1472" target="_blank">存储容量跟踪通过</a> <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fkubernetes.io%2Fdocs%2Fconcepts%2Fstorage%2Fstorage-capacity%2F%23api" target="_blank">CSIStorageCapacity 对象</a>公开当前可用的存储容量，并增强使用具有后期绑定的 CSI 存储卷的 pod 的调度。</span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></p> 
<p style="text-align:left"><span><span><span><span style="color:#222222"><span><span><span><span><span><span><span><span><span><span><span style="background-color:#ffffff"><span><span><span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fkubernetes%2Fenhancements%2Fissues%2F284" target="_blank">存储卷扩展</a>增加了对调整现有持久卷大小的支持。</span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></p> 
<p style="text-align:left"><strong>NonPreemptingPriority 正式进入稳定状态</strong></p> 
<p style="text-align:left"><span><span><span><span style="color:#222222"><span><span><span><span><span><span><span><span><span><span><span style="background-color:#ffffff"><span><span><span>此功能<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fkubernetes%2Fenhancements%2Fissues%2F902" target="_blank">为 PriorityClasses 添加了新选项</a>，可启用或禁用 pod 抢占机制</span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span><span><span><span><span style="color:#222222"><span><span><span><span><span><span><span><span><span><span><span style="background-color:#ffffff"><span><span><span>。</span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></p> 
<p style="text-align:left"><strong>迁移存储插件</strong></p> 
<p style="text-align:left">目前正在迁移树内存储插件，在实现 CSI 插件的同时，保持原有 API 的正常运行。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fkubernetes%2Fenhancements%2Fissues%2F1490" target="_blank">Azure Disk</a> 和 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fkubernetes%2Fenhancements%2Fissues%2F1489" target="_blank">OpenStack Cinder</a> 等插件已完成迁移。</p> 
<p style="text-align:left"><strong>gRPC 探针升级至 Beta 版本</strong></p> 
<p style="text-align:left">在 1.24 中，<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fkubernetes%2Fenhancements%2Fissues%2F2727" target="_blank">gRPC 探针功能</a>已进入 Beta 测试阶段，并默认启用。用户现在可以在 Kubernetes 中为 gRPC 应用程序进行<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fkubernetes.io%2Fdocs%2Ftasks%2Fconfigure-pod-container%2Fconfigure-liveness-readiness-startup-probes%2F%23configure-probes" target="_blank">本地配置启动、活跃度和就绪性探测，而无需公开 HTTP 端点或使用额外的可执行文件</a>。</p> 
<p style="text-align:left"><strong>Kubelet Credential Provider 升级至 Beta 版本</strong></p> 
<p style="text-align:left">该组件在 Kubernetes 1.20 中作为 Alpha 版本发布，kubelet 对其支持现已升级到 Beta 版本。这允许 kubelet 使用 exec 插件动态检索容器镜像注册表的凭据，而不是将凭据存储在节点的文件系统上。</p> 
<p><strong>Contextual Logging 进入 Alpha 阶段</strong></p> 
<p>此功能使函数的调用者能够控制日志记录的所有细节（输出格式、详细程度、附加值和名称等）。</p> 
<p><strong>避免为服务分配 IP 时发生冲突</strong></p> 
<p>这是新增的可选功能，允许用户为服务的静态 IP 地址分配预留范围。通过手动启用此项功能，集群将从指定的服务 IP 池中自动获取地址，从而降低冲突风险。</p> 
<p>因此服务的<code>ClusterIP</code><span style="background-color:#ffffff; color:#222222"><span>可通过以下方式被指定：</span></span></p> 
<ul> 
 <li>动态分配，这意味着集群将自动在配置的服务 IP 范围内选择空闲 IP</li> 
 <li>静态分配，这意味着用户将在已配置的服务 IP 范围内设置 IP</li> 
</ul> 
<p>服务的<code>ClusterIP</code>具有唯一性，因此当尝试使用已被分配的<code>ClusterIP</code>进行服务创建，则会返回错误结果。</p> 
<p><strong><span><span><span><span><span style="color:#222222"><span><span><span><span><span><span><span><span><span><span><span style="background-color:#ffffff"><span><span><span>从 Kubelet 中删除动态 kubelet 配置</span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></strong></p> 
<p style="text-align:left"><span><span><span><span style="color:#222222"><span><span><span><span><span><span><span><span><span><span><span style="background-color:#ffffff"><span><span><span>动态 Kubelet 配置在 1.22 中被标记为弃用状态，现已被正式删除。该功能还将从 Kubernetes 1.26 的 API 服务器中删除。</span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></p> 
<hr> 
<p>Kubernetes 1.24 版本以「Stargazer」命名，logo 是一架<span style="background-color:#ffffff; color:#333333">望远镜在遥望空中的昴宿星团 —— 在希腊神话中被称为“七仙女星”。“7”是 Kubernetes 的幸运数，毕竟它曾经的项目名称为</span>“Project Seven”。</p> 
<p><img alt height="300" src="https://oscimg.oschina.net/oscnet/up-9fea42a5a6e5f9584b494a0eac52bed926c.png" width="300" referrerpolicy="no-referrer"></p> 
<p><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fkubernetes.io%2Fblog%2F2022%2F05%2F03%2Fkubernetes-1-24-release-announcement%2F" target="_blank">Release Announcement</a> | <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fkubernetes%2Fkubernetes%2Fblob%2Fmaster%2FCHANGELOG%2FCHANGELOG-1.24.md" target="_blank">Changelog</a></p>
                                        </div>
                                      
</div>
            