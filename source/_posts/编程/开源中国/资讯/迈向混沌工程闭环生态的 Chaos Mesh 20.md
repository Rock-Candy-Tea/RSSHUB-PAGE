
---
title: '迈向混沌工程闭环生态的 Chaos Mesh 2.0'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://pic3.zhimg.com/80/v2-7a6b97113ff64a6b71e5fe90a45ff2da_1440w.jpg'
author: 开源中国
comments: false
date: Thu, 05 Aug 2021 06:15:00 GMT
thumbnail: 'https://pic3.zhimg.com/80/v2-7a6b97113ff64a6b71e5fe90a45ff2da_1440w.jpg'
---

<div>   
<div class="content">
                                                                    
                                                        <p><strong>2021 年 7 月 23 日，我们发布了 Chaos Mesh 2.0 GA 版本。Chaos Mesh 2.0 是一个让人兴奋版本，朝着混沌工程闭环生态迈出了坚实的一步。</strong></p> 
<p>让混沌工程变得更简单一直是 Chaos Mesh 坚定不移的目标，构建混沌工程闭环生态是帮助我们达成目的的关键步骤。在近一年的不屑努力下，我们主要在三个方面作出了非常大的改进：易用性，实验的编排与调度以及故障类型的丰富度。</p> 
<h2><strong>易用性</strong></h2> 
<p>我们一直致力于提升产品的易用性，在 Chaos Mesh 1.0 GA 时我们便发布了 Chaos Dashboard，方便用户通过图形化的界面进行混沌实验。在 Chaos Mesh 2.0 中，<strong>Chaos Dashboard 带来了较大的改进</strong>：</p> 
<ul> 
 <li>Chaos Dashboard 支持 AWSChaos GCPChaos 的创建、查看与更新，使云上环境的混沌实验与 kubernetes 环境的混沌实验体验一致；</li> 
 <li>对于每个混沌实验，Chaos Dashboard 现在能够展示每个实验的更多详细事件，让实验的可见性更进一步！</li> 
</ul> 
<h2><strong>原生的实验编排与调度</strong></h2> 
<p>在进行混沌实验时，单个混沌实验往往不能满足对故障场景的模拟，而手动控制实验的启停是一件繁琐且危险的事情。之前我们可以通过 Argo 配合 Chaos Mesh 来自动地控制实验的注入与结束。在 Chaos Mesh 2.0 版本中，我们<strong>原生加入了 Workflow</strong>，支持了场景编排的能力，可以方便地将多个实验串行/并行地执行，并能够织入通知与健康检查，形成复杂的实验场景。</p> 
<p><img alt src="https://pic3.zhimg.com/80/v2-7a6b97113ff64a6b71e5fe90a45ff2da_1440w.jpg" referrerpolicy="no-referrer"></p> 
<p>之前在定义定期执行的混沌时，仅使用 “cron: <a href="https://my.oschina.net/u/2609610">@every</a> 10s” 与 “duration: 5s” 描述行为并不能满足大家的需求。例如单次执行时常大于执行周期，这种定义是合法的，但是对于预期行为研究没有合适的描述。我们参考了 CronJob 的定义引入了新的自定义对象 Schedule，为定期执行的任务加入了更多明确的属性，例如同一时间内是否允许多个实验同时执行，进而约束行为。</p> 
<p><img alt src="https://pic2.zhimg.com/80/v2-55083fae19f031b2ebc4f7d8e4794539_1440w.jpg" referrerpolicy="no-referrer"></p> 
<p>对于定义的更新我们提供了迁移工具，帮助用户迁移升级，也会随 release 发布。可以参考<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fchaos-mesh.org%2Fwebsite-zh%2Fdocs%2Fupgrade-to-2.0" target="_blank">升级至 Chaos Mesh 2.0</a> 完成从 1.x 到 2.0 版本的升级。</p> 
<h2><strong>更多的故障类型</strong></h2> 
<p>Chaos Mesh 已经支持了如 NetworkChaos，IOChaos，StressChaos 等系统层面的故障注入，也支持了如 AWSChaos，GCPChaos 这种云服务类型的故障注入。我们在 Chaos Mesh 2.0 中也加入了应用层的故障注入功能。</p> 
<p><strong>JVMChaos</strong></p> 
<p>Java 及 Kotlin 等基于 JVM 的语言是在业界中有非常广泛的引用，通过 JVM 字节码增强以及 javaagent 等技术可以较为轻松的实现 JVMChaos. 目前 Chaos Mesh 借助 chaos-exec-jvm 实现了 JVMChaos，能够进行例如方法延迟，返回值修改，内存溢出，抛出异常等应用级别故障注入。可以参考文档<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fchaos-mesh.org%2Fwebsite-zh%2Fdocs%2Fsimulate-jvm-application-chaos" target="_blank">模拟 JVM 应用故障</a>了解更多信息。</p> 
<p><strong>HTTPChaos</strong></p> 
<p>HTTPChaos 是在 2.0 中新支持的 Chaos 类型，它能够在服务侧劫持 HTTP 服务请求与响应，中断链接、注入延迟或修改 Header/Body，适用于任何使用 HTTP 作为通信协议的场景。可以参考文档<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fchaos-mesh.org%2Fwebsite-zh%2Fdocs%2Fsimulate-http-chaos-on-kubernetes" target="_blank">模拟 HTTP 故障</a>了解更多信息。</p> 
<h2><strong>物理机注入工具 Chaosd</strong></h2> 
<p>Chaos Mesh 专为 kubernetes 设计，而在物理机环境上，我们提供了 Chaosd，Chaosd 由 chaos-daemon 演化而来，并针对物理机的特点增加了一些专门的混沌实验功能。支持在物理机上进行进程，网络，JVM，压力，磁盘等不同类型的故障注入。</p> 
<h2><strong>展望未来</strong></h2> 
<p>Chaos Mesh 仍在活跃地开发中，在接下来的几个月里，我们已经为 Chaos Mesh<strong>规划了更多强大的功能</strong>，包括：</p> 
<ul> 
 <li>运行时注入 JVMChaos，让 JVMChaos 的成本更低，更加方便。</li> 
 <li>插件机制，允许用户构建自定义的混沌实验，同时能够享受 Chaos Mesh 的调度功能。</li> 
</ul> 
<p>另外，我们也发现用户的混沌实验的使用场景是非常宝贵的资源，而且好的混沌实验场景能够复用到很多地方。我们在未来会推出一个平台，允许用户分享自己使用过的混沌实验场景。</p> 
<h2><strong>快速体验</strong></h2> 
<p>你可以在浏览器中打开<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Flink.zhihu.com%2F%3Ftarget%3Dhttps%253A%2F%2Fchaos-mesh.org%2Finteractive-tutorial" target="_blank">https://chaos-mesh.org/interactive-tutorial</a>，使用云上的资源快速体验 Chaos Mesh 2.0！</p> 
<h2><strong>致谢</strong></h2> 
<p>感谢所有 Chaos Mesh 的贡献者 （<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Flink.zhihu.com%2F%3Ftarget%3Dhttps%253A%2F%2Fgithub.com%2Fchaos-mesh%2Fchaos-mesh%2Fgraphs%2Fcontributors" target="_blank">https://github.com/chaos-mesh/chaos-mesh/graphs/contributors</a>)，Chaos Mesh 从 1.0 到 2.0 的过程中离不开每一位贡献者的努力！</p> 
<p><strong>最后欢迎大家为 Chaos Mesh 提交 issue 或者参考文档开始提交代码，Chaos Mesh 期待大家的参与和反馈！</strong></p>
                                        </div>
                                      
</div>
            