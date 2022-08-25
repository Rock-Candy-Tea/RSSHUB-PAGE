
---
title: 'Kubernetes 1.25 正式发布'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://oscimg.oschina.net/oscnet/up-aa762e354a6d09085782af326b5fc055d9f.png'
author: 开源中国
comments: false
date: Thu, 25 Aug 2022 07:34:00 GMT
thumbnail: 'https://oscimg.oschina.net/oscnet/up-aa762e354a6d09085782af326b5fc055d9f.png'
---

<div>   
<div class="content">
                                                                                            <p>Kubernetes 1.25 已正式发布。</p> 
<p>1.25 总共包含 40 项功能变化，其中：</p> 
<ul> 
 <li>15 项增强功能正在进入 alpha 阶段</li> 
 <li>10 项增强功能正在升级到 beta 阶段</li> 
 <li>13 项增强功能正在升级到 stable 阶段</li> 
 <li>两项功能已被标记为弃用或删除</li> 
</ul> 
<hr> 
<p><strong>主要变化</strong></p> 
<p><strong>cgroup v2 支持正式 GA</strong></p> 
<p>cgroups 是在节点上组织和管理容器资源的关键 Linux 内核功能之一。在 Kubernetes 的早期，所有容器运行时都是使用 cgroup v1 构建的，现在 cgroups v2 支持已经升级到 GA 状态。使用 cgroups v2，容器工作负载将更安全地工作，包括无根容器，并且更可靠地使用最新的内核功能。</p> 
<p><strong>CronJob 中的时区支持升级到 beta</strong></p> 
<p>CronJob 实例由资源规范中提供的计划创建。但是，新创建资源的时区取决于控制器管理器的运行位置。使用新的增强功能，您将获得一个新字段 spec.timeZone，您可以在其中使用 tz 数据库中的有效时区。</p> 
<p><strong>删除 PodSecurityPolicy</strong></p> 
<p>在 Kubernetes 1.25 中，PodSecurityPolicy 在 1.21 版本弃用后被完全移除。PodSecurityPolicy 是定义 Pod 功能规则的解决方案，但随着时间的推移它变得复杂和混乱。相反，Kubernetes 现在已经实现了具有明确迁移路径的 Pod 安全准入控制器。</p> 
<p><strong>追溯默认 StorageClass 分配（alpha 版本）</strong></p> 
<p>默认存储类主要由集群管理员在集群创建期间配置。但是，当底层存储提供者或业务需求发生变化时，您还应该更改集群中的默认存储类。新的 alpha 功能侧重于将 Kubernetes 行为更改为对没有任何存储类的 PVC 具有追溯性。</p> 
<p><strong>自动刷新官方 CVE 源（alpha 版本）</strong></p> 
<p>Kubernetes 是最活跃的开源存储库之一，因此存在许多与 CVE 相关的问题和 PR，这些问题和 PR 是无法过滤的。新的alpha 功能可确保在自动化的帮助下标记问题和 PR。这种新方法将让你以最终用户、维护者或平台提供商的身份列出具有相关信息的 CVE。</p> 
<p><strong>默认为 seccomp（升级到 beta）</strong></p> 
<p>Kubernetes 允许通过定义seccomp配置文件来提高容器安全性；自 1.22 版本以来，它一直是 alpha 功能。默认情况下启用 Seccomp 会添加一个安全层来防止 CVE 和 0-days，现在此功能已在 1.25 版本中升级为 beta 。</p> 
<hr> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">Kubernetes 1.25 版本的主题是<strong>「Combiner」</strong>，团队希望通过此版本表达尊重协作和开放的精神，这种精神将大家从分散在全球的独立开发者、写作者和用户转化为能够改变世界的联合力量。</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><img alt src="https://oscimg.oschina.net/oscnet/up-aa762e354a6d09085782af326b5fc055d9f.png" referrerpolicy="no-referrer"></p> 
<p><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fkubernetes.io%2Fblog%2F2022%2F08%2F23%2Fkubernetes-v1-25-release%2F" target="_blank">Release Announcement</a><span> </span>|<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fkubernetes%2Fkubernetes%2Fblob%2Fmaster%2FCHANGELOG%2FCHANGELOG-1.25.md" target="_blank">Changelog</a></p>
                                        </div>
                                      
</div>
            