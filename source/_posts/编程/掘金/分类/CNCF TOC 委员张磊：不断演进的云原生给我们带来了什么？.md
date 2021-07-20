
---
title: 'CNCF TOC 委员张磊：不断演进的云原生给我们带来了什么？'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/1cbedc057d5d4c7d81cd0d32871b1cfb~tplv-k3u1fbpfcp-zoom-1.image'
author: 掘金
comments: false
date: Mon, 19 Jul 2021 21:56:21 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/1cbedc057d5d4c7d81cd0d32871b1cfb~tplv-k3u1fbpfcp-zoom-1.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>简介： 任何一种云原生技术，它不再是某种能力的弥补，而是更多地将云的能力以某种方式更简单、更高效地透出给我的应用去使用。无论是容器、K8s 还是 Service Mesh，他们都是在不同的环节帮助应用本身能够更好地去使用云服务。</p>
<p>作者｜张磊</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/1cbedc057d5d4c7d81cd0d32871b1cfb~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<h1 data-id="heading-0">云原生是什么？</h1>
<p>即使“云原生”的提出已经有一段时间，但不少人还是会有这样一个问题：究竟什么是云原生？或者说云原生的确切定义是什么？</p>
<p>实际上，当我们接触到很多云原生的开源技术和产品之后，会逐渐发现一个现象——云原生本质上其实并不是一个非常确切的物体。也就是说，云原生其实不存在什么具体定义，它指的是一个不断演进的过程。与其谈云原生的本质，不如我们将它理解为一套愿景。</p>
<p>那么这套愿景的内容又是什么呢？</p>
<p>在未来云的时代，我们的软件或者应用是天然的生于云上，长于云上。之所以会出现这样一种现象或这样一个事实，正是因为云计算能够最大程度地去帮助这些软件降本提效，释放软件本身最大的业务价值。这才是云原生真正想要去做的一件事情，所以它并不是某一项具体的技术，也不是某一个方法，更不是某一个具体的科研项目。</p>
<h1 data-id="heading-1">不断演进的云原生</h1>
<p>下图能够直观地阐明云原生整体的形态到底是怎么去演进和发展的。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/4b59f0ec28544c6c98f2ff4b54824ae7~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>云原生非常强调利用云的特性，所以它的核心方法论和核心概念都是围绕如何让我们的软件和应用去利用云的特性。那么云的特性是什么呢？比如说云是能够无限弹性的、云的资源是可以快速交付的、云的使用方法是可以按量付费的，这些都是云非常本质的特性。</p>
<p>围绕这些云的特性，云原生才有了一套最基础的方法论和概念。比如大家可能听说过不可变基础设施，当我的应用部署在云上，假设这个应用载体是不可变的，我就可以随时把它删掉或替换掉，那么要更新我的应用会非常容易。如果要升级应用，可以直接采用删掉旧的、上线新的方式去做，而不是说需要去动态变更应用里面的某项配置，甚至动态更改代码去实现。所以，不可变基础设施就是一套非常典型的、基于利用云的快速资源交付能力而形成的方法论。</p>
<p>再比如说，云原生强调要高度的自动化，实现自运维甚至自愈，其实也是希望软件本身能够去更好地利用云的特性。因为云的能力是非常强大的，云能够提供各种各样的运维能力，所以应用或者软件可能从开发的时候，就要考虑到云其实能够提供很多能力到应用层，而不是说先开发完应用，再去思考怎么借助云的能力去运维，这样是构建不出来云原生应用的。</p>
<p>再比如说，云原生应用无所谓用什么语言写，用什么框架写，这也是很明显的一个特点。因为云本身是一个基础设施能力，那么就不应该也不会去用某种语言或者框架去锁定。同样也是希望这个世界上所有的软件都能够去利用云的能力，而不是说云只能服务于某种语言。</p>
<p>以上这些都是在云的背景下，云原生提出的一些非常重要的概念。而这些概念本身在我们的技术研究当中就会被映射成为一系列的系统，或者说架构思想。比如说前面提到不可变基础设施，可以把一个应用旧的实例删掉换成新的实例，像这样的一套方法怎么去实现？就要靠容器技术。容器技术本质上提供容器镜像，一个容器镜像是自包含一个应用的运行环境，包括应用本身，可以随时把这个镜像版本替掉，上线一个新的版本就可以了。这其实代表着容器是不可变基础设施的一个非常良好的实现。</p>
<p>那么这是不是意味着未来会有某一种技术，能够更好地去实现不可变基础设施呢？这是很有可能的，并且这项技术当然也是云原生的。当未来可能有一个新的技术去实现不可变基础设施，或者更好地实现不可变基础设施，那么这样一个技术也一定是属于云原生的核心范畴。与之类似的，像我们云原生今天强调的 Sidecar 架构，就是把中间件能力通过一个叫 Sidecar 容器的方式去对接到业务容器里去，而不是说在业务本身上去做定制，集成中间件去解决问题。这其实是希望能够去实践我们强调的与语言无关、与框架无关的这样一套方法论所提出的一个架构。而这个架构的特点就是，中间件能力不再需要以语言或者框架的方式嵌到业务代码本身里去，所以说 Sidecar 加上容器都能够去实现这样的一套方法。</p>
<p>这就是云原生方法论背后不断推演出来的一系列技术和架构，而这些技术架构最终在云原生生态里面，往往是以开源的技术项目来给大家去使用的。比如说前面提到的容器就会有 Docker 上的项目，我们提到的 Sidecar 和自运维的这套思想，最终会通过 Kubernetes 去帮你去实现。</p>
<p>再比如说最近比较火热的 Service Mesh，它本质上在帮你去做中间件的能力，只不过是通过 Sidecar 这种与语言无关的方式去做；再比如说我们未来或者说现在就已经比较火的 eBPF、WASM，他们其实都是在实践云原生这套体系背后的某项思想和某种架构，以开源的方式去满足让用户使用的场景。而正是因为有了这一系列的开源项目，我们才能做到说当我的用户拿到这样的开源项目，拿到这样的技术，他能够去真正实践云原生理念，从而达到我们前面讲到的这两种云带来的本质效果：</p>
<p>第一个是提升效率，比如说研发效率、交付效率、运营效率。例如我的应用本身通过容器实现了不可变基础设施的这样一套理念，那么它的交付就可以非常简单，我只需要做镜像，交付镜像后它就可以运行在每一个地方；再比如说我们的运维，当你的软件本身已经实现了自运维，那么它的运维的难度和成本一定是降低的，所以我们一定能够借助云的能力去提效。</p>
<p>第二个是降低成本，这里包括了资源成本，也包括了人力成本。比如说通过 Kubernetes 或者说通过容器这样的项目，我的应用可以更好地、更多地去集成云服务，通过云服务来减少运维成本和人力投入，这些都是很明显的成本降低。再比如说我的应用通过云原生实现了上云，又通过云原生架构，可以很快速地进行资源交付和更新的模式，让整个应用的资源成本也变得很低，这同样也是通过云原生技术，让应用能够更好地使用到云的本质能力的一种非常好的体现和实践。</p>
<p>总体而言，你会发现这一套云原生的方法其实是一个很完善的闭环，先不断去地看、不断地去探索如何利用云的特性帮助用户去提效降本，然后把这一系列的方法或者这一系列的思想，总结沉淀成为云原生的概念和方法论，再通过一系列相应的架构和对应的开源项目将其实现，最后再让用户能够去使用这些技术，从而达到释放云计算红利的本质目的。</p>
<p><strong>所以说云原生它没有一个具体的定义，它实际上是一套不断自我演进的理论体系加上最佳实践的组合。</strong></p>
<h1 data-id="heading-2">今天的云原生</h1>
<p>今天的云原生可能是围绕着容器和 Kubernetes 来构建的，而这样的项目实际上在帮助我们去实践很多云原生背后的本质思想，包括不可变基础设施、自动化等。今天 Kubernetes 被认为是一个云时代的通用控制平面，也有人把它叫做操作系统，就是说你的所有操作都可以借助 Kubernetes 在云上统一去完成。</p>
<p><strong>1、Kubernetes 项目的“安卓化”</strong></p>
<p>Kubernetes 项目的角色可能会越来越像一个安卓。举一个例子，比如说今天的 Kubernetes 其实正在做到无处不在，每个地方每个云层都有 Kubernetes，甚至部署在端的用户、或者部署在边缘的环境下都是非常正常的，就跟安卓一样，车上也有，我们电视里也有，甚至空调也会有可能有一个安卓。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/618cfa22dc34424fb3619766e959bfbb~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>那么更重要的是，用户使用 Kubernetes 的本质目的是什么？是交付和管理它的软件。比如说我用 Kubernetes 一定是在上面部署了某一个东西，比如说 AI 的服务或者淘宝，用户的本质目的是使用这套东西来管理软件。而 Kubernetes 本身其实对上暴露的是一系列格式化的抽象，比如说 Deployment、Service、Ingress，让我能够去管理和交付我的应用；而对下它启动了一套标准化的接口，比如说通过 CNI 就可以对接阿里云网络，对接自研网络插件，所以它本质上是一个中间层，即一个控制平面，接入了大量的基础设施，而他们暴露的东西成为了我的应用所需要的一些能力，让我能够去用这些能力去管理应用。</p>
<p>那么这样的一个趋势往后面不断去研究的话，就会发现这个跟安卓特别相似。比如说安卓在手机本身其实是不付钱，但是应用市场里的应用是要付钱的。安卓的价值在于它把用户的手机抽象、包装、封装成一系列应用可以使用的 API，所以说安卓的价值和今天 Kubernetes 是完全一样的。</p>
<p>未来我们会看到，Kubernetes 它不仅会出现在各种不一样的地方，更重要的是它会为应用软件的研发、运维、交付的全生命周期提供一系列完整的能力，让用户可以使用它。与此同时，为了能够更好地把软件交付出去，我们会发现未来还会有很多这样的项目专门帮助你去解决软件在 K8s 上交付的问题。与此同时，我们以前的传统 PaaS 会不复存在，因为它的能力已经全部被 Kubernetes 接管了，而未来会出现更多的这种开放的可扩展的 PaaS，他们的作用是让你能够去更好地更简单地交付和管理软件，就像安卓上的豌豆荚，可以很容易地去管理软件。对于这样一个趋势，我把它叫做 Kubernetes 的“安卓化”。</p>
<p><strong>2、应用与能力的“Operator化”</strong></p>
<p>而另一个趋势就是，在今天云原生的生态里面，不论是我的应用还是我的能力，它都会往一个非常能够自动化的方向去演进，我把它叫做 “Operator 化”。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/1fe64dabcec14ed8ab32fcabc53fc7f9~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>Operator 是 Kubernetes 里面的一个核心思想，它代表着我的任何一个应用和它所需要的能力都可以定义成为一个 Kubernetes 的 API 对象，通过一个叫做 Controller 的机制让你去使用云的能力，再让你接入到各种各样的基础设施里面。这个 Operator 化带来的一个直接结果就是，我的应用本身是高度自动化的，包括自愈、健壮性、可靠性、运行的确定性，这些在今天都可以交给 Kubernetes去解决。我的用户或者说我应用的 owner，不需要再关心这些问题。<br>
​</p>
<p>那么这也是我们今天在 K8s 安卓化的背景下看到的另外一个趋势，就是我的应用本身和业务所需要的能力会不断地往自动化方向去演进。这也非常符合云原生的理念，因为你的应用自动化和自愈能力越强，你就越能够去跟云去对接，人工需要去记录的成本会更低，时间也会更少，更多的是把我的自动化能力跟云去对接好，让云帮助我去解决所有问题。<br>
​</p>
<p><strong>3、应用中间件能力进一步“下沉”</strong><br>
​</p>
<p>还有一个趋势是，我们应用本身所需要的中间件能力下沉。即以前的中心化的中间件其实在过去几年中，已经演进到了微服务架构。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/54ea5ef3d3c94a918f01f84def27d818~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>微服务架构本质上是把以前的中心化中间件的这一套东西拆开，放在了业务代码里面，而你需要去把它引入进来使用。一般来说，会提供一个比较重的客户端或者一个库让你去使用，这是我们的微服务时代典型的中间件的一个使用方式。但是在今天，在我们云原生的越来越普及的这样一个现状下，有没有像 Sidecar 这样一个机制的存在？</p>
<p>今天的中间件实际上是大量的通过 Sidecar 方式去被使用到的，所以我的应用本身不需要再去引入一个库，或者引入一个特定的框架来去做很多事情，我甚至都不需要感知。比如说我今天要去做流量的切分，我不需要说在应用里面去引入这么一个库去做，而是完全交给我的基础设施，交给云去做。</p>
<p>那么应用跟云的交互，就通过一个叫 Sidecar 的一个旁路容器，让这个容器去代理应用本身所需要的进出流量，所以云就可以非常容易地通过这样一个代理，调节流量、做流量切分，这就是非常简单的 Service Mesh 的原理。</p>
<p>今天，中间件能力不断通过这样一个方式在下沉，它会带来一个非常明显的趋势，即中间件不再与业务相关了，不再与程序的编写语言相关了，也不需要对框架有什么依赖。它的实现跟 K8s 容器化这套体系会非常的紧密结合。另外，我对 Sidecar 的依赖也会更多，所以说相应的对 Sidecar 的管理能力也在逐步去提高要求。我们可以把它总结为应用中间件能力的进一步下沉。</p>
<h1 data-id="heading-3">层出不穷的云原生服务</h1>
<p>除此之外，伴随着云原生整套体系的不断发展，我们会看到，云服务在大量的、频繁地向云原生生态去靠拢，甚至说带来一些革命性的影响。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/f9d0667e068c40cbb1812e50428bd6a0~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>比如说，今天阿里云的云原生数据库，它实际上就是基于云原生提到的核心的思想理念，比如说无限弹性、高度可扩展，提出了一个全新的数据库架构，使得数据库的本身非常容易去扩展，能够去应付极高的、极为苛刻的流量和海量的数据处理需求，满足今天现代互联网应用的数据库使用的诉求。</p>
<p>再比如说阿里云基础设施，它能够给我们带来极致的资源使用效率，减少了很多层的虚拟化的性能损耗，让容器本身具有弹性，非常容易地去运维部署和管理，并且通过安全容器，通过更强的安全边界，保证容器之间的隔离，使隔离性是足够的。它能够为容器带来极致的物理级别的网络存储和计算性能，这是非常重要的，也是我们的应用通过云原生的理念去使用云计算服务的一个非常典型的例子。</p>
<p>再比如说像亚马逊云科技，它让我们的芯片本身能够去更容易或者说更直接的去适配容器化应用的使用方式。因为一个容器可能只有一个非常独立或者说非常模块化的一个进程在跑，那我就可以用芯片的核心去适配这样的一个业务，把我的基础设施的能力发挥得更强，把能力发挥到极致，同时保证像这样的核心之间的干扰是非常少的，更适应容器化微服务的应用的使用方式。</p>
<p>比如亚马逊云科技最近推出一个云原生应用部署引擎，它可以用我们这种完全一致的方式去部署任何的这种云服务或者是容器服务，这都是能够去帮助我们利用云的能力去提升应用管理交付运维效率的一个非常典型的产品。</p>
<p>所以我们看这些产品也好，去看所谓开源项目也好，当我们想要去思考这样一个问题，说我这个云产品是不是所谓的云原生，是不是云原生的技术，其实非常简单。只要判断一下它能不能帮助我的应用最大程度地去利用云计算降本提效，能不能通过这样的方式释放最大的业务价值，这个是判断一项技术，或者说一个产品是不是去把它定位为云原生的一个非常核心的一个标准，而不是说去看这个产品是容器与否。</p>
<h1 data-id="heading-4">阿里巴巴云原生化</h1>
<p>回到我们阿里巴巴本身的例子来讲，我们可以看到这么一个事实，今天阿里巴巴的基础设施已经基于像 Kubernetes 容器这样整套技术，完成了我们所谓的云原生化。而真正我们回过头来看这样一件事情，我们会发现其实云原生本身给阿里巴巴自己带来了非常重要的一些变革。</p>
<p>第一个我们对业务研发，通过前面讲到的云原生的思想，很好地做到了关注点分离，研发更专注于业务。通过云原生的这种标准的交付方式，我们还提出了像云原生标准交付的规范，去标准化地、模块化地进行可持续交付，兼顾用户体验和灵活度，从而大幅提升业务的研发效能，让他们完全关注于自己的业务，不需要再去接触到复杂的基础设施，这个是云原生给业务研发带来一个最大的价值。</p>
<p>再比如说对大量的业务运维和 SRE 来说，云原生体系所提供的这种敏捷运维高效运营的这套理念，以及它的技术实现，包括前面讲的轻量级的容器不可变、基础设施、高度自动化的应用本身和运维方式，都能够让我们今天的软件运维变得极其简单、极其高效，尤其相比于之前的传统方式，基于容器的基于自动化的一个方式，能够极高地提高我们的运维自动化程度，大量减少人工介入，提升我们操作的并发度，真正意义上的实现所谓的把复杂留给系统，把简单留给用户，这就是我们今天云原生的体系。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/8c5745d99616467f90fefd0e215f2dda~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>那么更不用说今天容器化之后，比如淘宝这类的应用，去做水平扩容和升级都是非常快捷、非常高效的，而不是说升级一下淘宝，你的手机应用就挂了，在云原生时代这事不再会发生了。</p>
<p>另外一个例子是对基础设施来说，通过阿里今天使用的神龙裸金属的实力，加上我们的安全容器，能够去帮助我们极大地提升今天数据中心的使用资源效率，我们叫提升资源效能。尤其是它能够去支持我们极高密度地去部署安全容器，利用规模效应，降低资源碎片。可以去根据你的工作负载的不同形态，去放心地填资源的碎片，因为有神龙金属所以我们能够确保这样做，依然有极高的业务的运行效率，同时不会互相之间有任何干扰。这些都是在今天云原生的环境下，这项基础设施所能够给我们带来的一个非常重要的一套变革，甚至说对于阿里巴巴的这样一个组织，随着云原生技术的引入和发展，也带来了一个非常好的变化，让阿里巴巴的技术栈标准化开放，能够跟生态无缝集成，也能够降低研发成本，让整个体系的可靠性和研发效率都有一个很好的提高。</p>
<p>而另一方面，随着自身基础设施的标准化，阿里巴巴的技术正在飞快地进入到开源社区当中。今天阿里巴巴是 CNCF 里面开源项目最多的一个公司，远远领先于任何一个厂商和其他一些组织。这里一个关键原因就在于，今天阿里巴巴的技术是跟生态无缝对接的，所以我们才能够积极去参与这样的一个更广泛的开源生态，把阿里的开源技术输出出去，甚至说这引领和影响了整个业界生态的发展过程，这个都是阿里巴巴的云原生化之后，我们看到的实实在在的一个变化。</p>
<h1 data-id="heading-5">总结</h1>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/0cf5d5c635f64fd99219f8da8601aafa~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>如果我们回顾一下今天讲的云原生这套理念，可以发现它实际上是一套架构到技术到产品的不断演进的过程。从架构上来讲，云原生认为软件天然生于云上、长于云上，能够最大化的利用云的能力；另外一方面区别于传统的模式，云原生能够让开发者享受到红利，能够去引领它的软件和应用本身去不断的现代化。</p>
<p>而围绕这种架构和理念，我们有一系列的技术，这里面有开源的，有自研的，但是它背后的逻辑和思想是高度一致的。围绕着基础设施、应用架构、开发运维交付的场景，通过云原生技术让系统更加可靠，具有弹性，有更好的容错性，并且组件之间松耦合易管理，可观测性做得更好，从而充分地去把云的能力透出来。云原生能够释放云的最大潜力，其实它的背后往往离不开云原生本质的这套理念和技术的支持，以这些理念和架构为代表的，像容器、不可变基础设施等等，他们其实是我们去落地云原生里面的一个高效的手段。</p>
<p>而围绕这些手段本身，我们才有了这样各种各样的云原生理念加持下的产品，包括云原生数据库、云原生服务产品、中间件、函数计算、容器等等一系列的开放标准，能够去弹性，能够去利用云的价值的，能够去让用通过云本身更好的服务的应用研发运维和应用交付人员的这样一系列的产品，那么他们都是能够非常明显地区别于传统的云计算服务提供的形态。</p>
<p>所以我们会看到未来的云会更多地向 Service 化、SaaS 化、服务化的方式去演进，而较少地去专注在基础设施这一层，因为我们真正的用户关注点，其实在它的应用能否发挥最大的业务价值这个问题上面的。</p>
<p>未来的整个演进趋势，它其实都伴随着一个非常重要的点，就是说云的能力在不断地越变越丰富，这是非常重要的。之所以在过去，我们的整个软件架构本身它会需要大量的，比如说传统中间件，甚至一些微服务框架或者是 PaaS，去帮助我们更好地的管理软件，它的背后非常重要的原因在于云或者说基础设施能力不够强。比如说我今天就想要一个蓝绿发布的能力，而很多云在很长一段时间内是不具备这个能力的，所以必须通过某种中间件或者某种框架来帮你去解决，但今天不是这样。今天我们的云几乎能做到你想象到的任何一种应用所需要的管理能力，甚至应该说云的能力其实已经几乎要超出了我们今天软件架构的大部分需求。所以在这种情况下，我必然不再需要一个额外的层，无论是传统中间件，还是传统的这种微服务框架或者 PaaS，去帮助弥补软件的诉求跟基础设施之间的鸿沟。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/b3e6682fa02f42f7b88cfce023671d1c~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>当这个鸿沟越来越窄，各种各样的云原生技术开始出现。所以任何一种云原生技术，它不再是某种能力的弥补，而是更多地将云的能力以某种方式更简单、更高效地透出给我的应用去使用。无论是容器、K8s 还是 Service Mesh，他们都是在不同的环节帮助应用本身能够更好地去使用云服务。或者说使用到云背后的基础设施能力，比如说 K8s 它可以让应用非常无感地极简地进入到我的云的存储和网络当中，使用云计算能力；Service Mesh 通过 Sidecar 这样完全无侵入的方式，让你能够使用云的流量控制的能力来去作为微服务治理。</p>
<p>未来我们的整个云计算发展，包括云原生背后的关注点一定也是这样，不断地、持续地、充分地去释放云计算的基础设施能力，到软件的研发交付乃至整个生命周期当中，这是非常重要的一点。因为未来云的能力一定是越来越强，伴随这样一个趋势我们才会看到，云原生一定是在逐步引领整个云计算生态。</p>
<p><a href="https://link.juejin.cn/?target=http%3A%2F%2Fclick.aliyun.com%2Fm%2F1000284516%2F" target="_blank" rel="nofollow noopener noreferrer" title="http://click.aliyun.com/m/1000284516/" ref="nofollow noopener noreferrer">原文链接</a></p>
<p>本文为阿里云原创内容，未经允许不得转载。</p></div>  
</div>
            