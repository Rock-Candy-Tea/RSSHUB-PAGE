
---
title: 'WebAssembly会是下一个Kubernetes吗？'
categories: 
 - 编程
 - Dockone
 - 周报
headimg: 'https://picsum.photos/400/300?random=9481'
author: Dockone
comments: false
date: 2022-02-20 04:10:24
thumbnail: 'https://picsum.photos/400/300?random=9481'
---

<div>   
<br>几周前我有一个“哦，啊哈，当然”的时刻，我想分享一下：WebAssembly是下一个Kubernetes吗？<br>
<h3>Kubernetes来了</h3>Kubernetes承诺提供一个软件虚拟化基础，可以让你同时解决许多问题：<br>
<ul><li>与在裸机上运行服务相比，Kubernetes可以让你更有效地使用硬件。Kubernetes允许你在一台硬件服务器上运行多个容器，并允许你根据需要向集群中添加更多服务器。</li><li>“容器云”架构有效地划分了构建服务器端应用程序的工作。数据库团队可以发布数据库容器，后端团队可以发布Java容器，产品经理使用网络作为通用中间层将它们连接在一起。它符合康威定律：软件看起来像组织结构图。</li><li>容器抽象足够通用，可以支持许多不同类型的服务。Go、Java、C++等等——它不是特定于语言的。开发团队可以使用他们喜欢的东西。</li><li>负责运行容器的Kubernetes服务器的运维团队不必信任他们运行的容器，他们内置了一些沙盒和保护措施。</li></ul><br>
<br>Kubernetes本身是对先前架构OpenStack的演变。OpenStack让每个容器都是一个完整的虚拟机，具有完整的内核和操作系统以及一切。相反，Kubernetes通常使用容器，容器中通常不需要内核。它们更轻量级——想想Docker与VirtualBox。<br>
<br>在Kubernetes部署中，内核仍然位于软件架构的中心位置。容器化的基本机制是具有私有命名空间的Linux内核进程。然后这些容器通过TCP和UDP套接字粘合在一起。然而，虽然每个容器有一个或多个内核进程确实比完整的虚拟机扩展得更好，但它通常不会扩展到数百万个容器。并且进程确实有一些启动时间——你不能为每个对高性能Web服务的请求启动一个容器。这些技术限制导致某些类型的系统架构，通常具有保持某种状态的长期组件。<br>
<h3>k8s会演化到w9y吗</h3>服务器端WebAssembly与Kubernetes处于类似的空间——或者更确切地说，WebAssembly类似于进程和私有命名空间。WebAssembly为你提供了良好的抽象屏障和（可以提供）高度安全隔离。在某些方面它甚至更好，因为WebAssembly提供了“允许列表”安全性——它没有一开始的功能，要求运行WebAssembly的“主机”将自己的一些功能显式委托给客体WebAssembly模块。与默认情况下从每个功能开始然后必须受到限制的进程进行比较。<br>
<br>与Kubernetes一样，WebAssembly也为你提供康威定律系统。你无需传送容器，而是传送WebAssembly模块——以及一些关于他们需要从环境中获得哪些类型的东西的元数据（“导入”）。WebAssembly是通用的——它是一个低级的虚拟机，任何东西都可以编译成。<br>
<br>但是，在WebAssembly中你会得到更多的东西。一是快速启动，因为内存就是数据，所以你可以安排创建一个WebAssembly模块，该模块的状态从内存中预初始化的状态开始。这样的模块可以在几微秒内启动——速度足够快，可以在每个请求上创建一个，在某些情况下，只是在之后丢弃状态。你可以在WebAssembly上比在容器上更有效地运行功能即服务架构。另一个是虚拟化完全在用户空间中提供。一个进程可以在许多不同的WebAssembly模块之间多路复用。这让一台服务器可以做更多事情。而且，你不需要使用网络来连接WebAssembly组件；它们可以在内存中传输数据，有时甚至无需复制。<br>
<br><em>题外话：WebAssembly的这种轻量级进程特色使得其他架构也成为可能，例如这个有趣的<a href="https://hacks.mozilla.org/2021/12/webassembly-and-back-again-fine-grained-sandboxing-in-firefox-95/">hack将链接到Firefox</a>的库沙箱化，他们实际上已经发布了！</em><br>
<br>我将WebAssembly与Kubernetes进行比较，但实际上它更像是进程和私有命名空间。所以对最初提出的问题的一个答案是，不，WebAssembly不是下一个 Kubernetes。下一个项目正在等待建立，尽管我知道一些已经开始的团队。<br>
<br>不过，我似乎很清楚一件事：WebAssembly将处于新事物的底部，因此WebAssembly的近期轨迹很可能会跟随Kubernetes的轨迹，这意味着……<br>
<ul><li>分析师的庆祝时间！</li><li>Gartner魔力象限再次出现</li><li>IBM推出了一个新的WebAssembly部门</li><li>埃森哲开始向公司询问他们的WebAssembly迁移计划</li><li>Linux基金会尝鲜</li></ul><br>
<br>等等。我会在不久的将来看到动荡的水域。所以从这个意义上说，Kubernetes本质上不是一个技术软件，而是一个泡沫商业竞争的纽带，当然：我们还有5年左右的时间，我们会很开心。<br>
<br>读者评论：2021年12月的WebAssembly让我想起了2014年容器/Kubernetes的情况——业界已经意识到当前的技术状态并不能解决当今所有的问题。跨边缘/服务器/浏览器的可移植性、可移植的安全模型以及业务逻辑和库之间的紧密耦合意味着企业构建/管理/操作应用程序的多个版本。像wasmCloud这样的技术是未来，在我看来，未来几年将会有一个更好的故事。<br>
<br><strong>原文链接：<a href="https://wingolog.org/archives/2021/12/13/webassembly-the-new-kubernetes">webassembly: the new kubernetes?</a></strong>
                                
                                                              
</div>
            