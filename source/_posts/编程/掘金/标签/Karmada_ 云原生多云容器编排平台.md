
---
title: 'Karmada_ 云原生多云容器编排平台'
categories: 
 - 编程
 - 掘金
 - 标签
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/07a2b997a5d34e9e9444719d882baee1~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Wed, 11 Aug 2021 01:21:47 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/07a2b997a5d34e9e9444719d882baee1~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>7月17日，在Cloud Native Days China云原生多云多集群专场，华为云原生开源负责人王泽锋发表了《Karmada: 云原生多云容器编排平台》主题演讲，分享了在云原生多云多集群方面的思考与实践。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/07a2b997a5d34e9e9444719d882baee1~tplv-k3u1fbpfcp-watermark.image" alt="图片" loading="lazy" referrerpolicy="no-referrer"></p>
<p><strong>以下为演讲全文</strong></p>
<p>根据最新的调查报告显示，超过93%的企业正同时使用多个云厂商的服务。云原生技术和云市场不断成熟，多云、多集群部署已经成为常态，未来将是编程式多云管理服务的时代。<br>
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/b955e12e53d74f3abb2ca2bb2917a36c~tplv-k3u1fbpfcp-watermark.image" alt="图片" loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-0">云原生多云多集群的典型阶段</h2>
<p><strong>阶段一：一群孤岛</strong></p>
<ul>
<li>一致的集群运维</li>
<li>一致的应用交付</li>
<li>业务割裂，互不感知</li>
</ul>

<ul>
<li>数据孤岛、资源孤岛、流量孤岛</li>
</ul>
<p><strong>阶段二：威尼斯水城</strong></p>
<ul>
<li>统一应用交付（部署运维）</li>
<li>统一应用访问（流量分发）</li>
<li>统一资源分配（编排调度）</li>
<li>少量、小压力的跨集群业务访问</li>
</ul>
<p><strong>阶段3：大航海时代</strong></p>
<p>实例、数据、流量：</p>
<ul>
<li>自动调度</li>
<li>自由伸缩</li>
<li>自由迁移</li>
</ul>
<p>目前，从业界的产品和一些用户二次开发使用的进度来看，还处于从一群孤岛到威尼斯水城的过渡阶段，一些开源的软件和厂商的产品，大部分还是在做统一的集群生命周期管理与集群的目录，以方便快速的选择切换集群，外加集群的外部流量打通进行全局流量的分配等等。但像跨集群自动分配以及应用的跨集群等这些能力是缺失的。</p>
<p><strong>现阶段，云原生多云多集群业务的编排也面临着诸多挑战：</strong></p>
<p>1）集群繁多的重复劳动：运维工程师需要应对繁琐的集群配置、不同云厂商集群间的管理差异以及碎片化的API访问入口等问题；</p>
<p>2）业务过度分散的维护难题：应用在各集群的差异化配置繁琐；业务跨云访问以及集群间的应用同步难以管理。</p>
<p>3）集群的边界限制：应用的可用性受限于集群；资源调度、弹性伸缩受限于集群。</p>
<p>4）厂商绑定：业务部署的黏性问题，缺少自动化故障迁移；缺少中立的开源多云容器编排项目。</p>
<h2 data-id="heading-1">多集群容器编排的前世今生</h2>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/0fe56ebfb5b94660bae7a5a9e4d3e9b8~tplv-k3u1fbpfcp-watermark.image" alt="图片" loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-2">Karmada：开源的云原生多云容器编排平台</h2>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/977917aea61849cea66aa72cc04e1868~tplv-k3u1fbpfcp-watermark.image" alt="图片" loading="lazy" referrerpolicy="no-referrer"></p>
<p>上图为Karmada在开源社区技术全景图，Karmada将以模块化的方式提供应用多集群部署、高可用调度、故障迁移、多集群服务发现和流量治理、多云集群生命周期管理等能力集，并面向多种典型的用户场景预置策略集，让用户可以结合企业实际情况自由定制适合自身的多云平台。</p>
<p>Karmada重点会基于Kubernetes的原生API提供多集群应用管理的能力，帮助用户实现零代码改造甚至零yaml改造到多集群架构的迁移。在能力方面，我们主要帮助用户解决全网统一管理以及全网集群的统一管理，另外我们会内置典型的应用部署模型，包括两地三中心等。</p>
<h2 data-id="heading-3">Karmada 架构</h2>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/123d0c3935ef466382b0f2266f4301dd~tplv-k3u1fbpfcp-watermark.image" alt="图片" loading="lazy" referrerpolicy="no-referrer"></p>
<p>Karmada通过独立的API 服务器（Karmada API Server）提供与其他组件进行通信的 REST 接口，包含Kubernetes原生API及Karmada扩展API，而Karmada 控制管理器根据用户创建的 API 对象执行操作, Karmada 调度器则实现应用在多集群中的调度。</p>
<h2 data-id="heading-4">Karmada核心概念</h2>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/beba75c6b7e54f82af5b55084ecb72f1~tplv-k3u1fbpfcp-watermark.image" alt="图片" loading="lazy" referrerpolicy="no-referrer"></p>
<p><strong>Resource Template</strong></p>
<ul>
<li>K8s原生API定义，包括CRD</li>
<li>无需修改即可创建多集群应用</li>
</ul>
<p><strong>Propagation Policy</strong></p>
<ul>
<li>可重用的应用多集群调度策略</li>
</ul>
<p><strong>Resource Binding</strong></p>
<ul>
<li>通用类型，驱动内部流程</li>
</ul>
<p><strong>Override Policy</strong></p>
<ul>
<li>跨集群可重用的差异化配置策略</li>
</ul>
<p><strong>Work</strong></p>
<ul>
<li>子集群最终资源在联邦层的映射</li>
</ul>
<p>Karmada API workflow</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/8bf18ceec1234b469ae4809ef56bb50b~tplv-k3u1fbpfcp-watermark.image" alt="图片" loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-5">Karmada内部工作流程</h2>
<p><strong>多集群应用部署</strong></p>
<p><strong>1）零改造 — 使用K8s原生API部署一个多集群应用</strong></p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/ccc5505e37324c8386ec7c30f97c96ab~tplv-k3u1fbpfcp-watermark.image" alt="图片" loading="lazy" referrerpolicy="no-referrer"></p>
<ul>
<li>示例策略：为所有deployment配置多AZ的HA部署方案</li>
</ul>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/12792d1759014cfe961110247ff8169a~tplv-k3u1fbpfcp-watermark.image" alt="图片" loading="lazy" referrerpolicy="no-referrer"></p>
<ul>
<li>使用标准的K8s API定义部署应用</li>
<li>kubectl create -f nginx-deployment.yaml</li>
</ul>
<p><strong>2）Propagation Policy: 可重用的应用多集群调度策略</strong></p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/f56afc0c419149cd9f4e11abe8dab763~tplv-k3u1fbpfcp-watermark.image" alt="图片" loading="lazy" referrerpolicy="no-referrer"></p>
<p><strong>resourceSelector</strong></p>
<ul>
<li>支持关联多种资源类型</li>
<li>支持使用 name 或 labelSelector 进行对象筛选</li>
</ul>
<p><strong>placement</strong></p>
<p>clusterAffinity:</p>
<ul>
<li>定义倾向调度的目标集群</li>
<li>支持通过 names 或 labelselector 筛选</li>
</ul>
<p>clusterTolerations:</p>
<ul>
<li>类似单集群中Pod tolerations和 node taints</li>
</ul>
<p>spreadConstraints:</p>
<ul>
<li>定义应用分发的HA策略</li>
<li>支持对集群动态分组：按Region、AZ、特性label分组，实现不同层级的HA</li>
</ul>
<p><strong>3）Override Policy: 跨集群可重用的差异化配置策略</strong></p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/580b792eef0e4dfdbba341387c7274a8~tplv-k3u1fbpfcp-watermark.image" alt="图片" loading="lazy" referrerpolicy="no-referrer"></p>
<p><strong>resourceSelector</strong></p>
<ul>
<li>支持使用 name 或 labelSelector 进行对象筛选</li>
</ul>
<p><strong>overriders</strong></p>
<ul>
<li>支持多种override插件类型</li>
<li>plainTextOverrider :基础插件，纯文本操作替换</li>
<li>imageOverrider:针对容器镜像的差异化配置插件</li>
</ul>
<p><strong>4）Member Cluster API: 用户自助可查的资源池基本单元</strong></p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/a513ed7d4a2a4524aa1ae9bfad834758~tplv-k3u1fbpfcp-watermark.image" alt="图片" loading="lazy" referrerpolicy="no-referrer"></p>
<p><strong>syncMode</strong></p>
<ul>
<li>支持使用 Push 或 Pull 模式与集群进行同步</li>
</ul>
<p><strong>secretRef</strong></p>
<ul>
<li>分离Push模式下集群访问凭据，便于开放 clusters API 供用户自助查询</li>
</ul>
<p><strong>taints</strong></p>
<ul>
<li>集群级别taint - toleration机制，支持集群级资源预留及驱逐</li>
</ul>
<p><strong>kubernetesVersion, apiEnablements</strong></p>
<ul>
<li>K8s版本，集群开启的API列表，支持基于API依赖的调度</li>
</ul>
<p><strong>resourceSummary</strong></p>
<ul>
<li>集群资源信息（容量、使用量、调度中）</li>
</ul>
<h2 data-id="heading-6">Karmada 社区路标</h2>
<p>目前，我们已经实现了Q1与Q2规划的特性，最新发布的0.7版本提供了多集群东西向服务发现，多集群外部流量接入目前在研发当中。版本的发布我们是保持一个月一个版本的频率，以让用户快速使用。在Q4，我们计划重点集成业界已有的一些周边项目，并在今年完成整体技术栈的能力开发。\</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/f35ca73bec3b41d19b801f4a459739d6~tplv-k3u1fbpfcp-watermark.image" alt="图片" loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-7">附：Karmada社区技术交流地址</h2>
<p><strong>项目地址：</strong></p>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fkarmada-io%2Fkarmada" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/karmada-io/karmada" ref="nofollow noopener noreferrer">github.com/karmada-io/…</a></p>
<p><strong>Slack地址：</strong></p>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fkarmada-io.slack.com" target="_blank" rel="nofollow noopener noreferrer" title="https://karmada-io.slack.com" ref="nofollow noopener noreferrer">karmada-io.slack.com</a></p></div>  
</div>
            