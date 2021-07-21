
---
title: 'Serverless 时代下大规模微服务应用运维的最佳实践'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/89e77ec93f8b4a5eab2030c2d5ceded9~tplv-k3u1fbpfcp-zoom-1.image'
author: 掘金
comments: false
date: Sun, 18 Jul 2021 18:45:06 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/89e77ec93f8b4a5eab2030c2d5ceded9~tplv-k3u1fbpfcp-zoom-1.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p><strong>简介：</strong> 原来的微服务用户需要自建非常多的组件，包括 PaaS 微服务一些技术框架，运维 IaaS、K8s，还包括可观测组件等。SAE 针对这些方面都做了整体的解决方案，使用户只需要关注自己的业务系统，这极大地降低了用户使用微服务技术的门槛。</p>
<p>作者 | 陈涛</p>
<h1 data-id="heading-0">微服务架构的优点和痛点</h1>
<p><strong>1、微服务架构的诞生背景</strong></p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/89e77ec93f8b4a5eab2030c2d5ceded9~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>回到互联网早期时代，也就是<strong>web1.0时代</strong>，当时主要是一些门户网站，单体应用是当时的主流应用，研发团队相对较小，这时候的挑战在于技术的复杂度，以及技术人员的匮乏。</p>
<p>到了<strong>新世纪互联网时代</strong>，出现了较大规模的一些应用，比如社交、电商等，流量和业务的复杂度也大幅增加，出现了几百甚至上千人的研发团队，研发团队扩大之后，协作问题成为困扰。SOA 解决方案是互联网的产物，其核心在于分布式、拆分等。但是因为 ESB 这样一些单点的组件，所以没有得到很好的推广。阿里巴巴在当时推出的 HSF、开源的Dubbo 等技术，其实是类似于分布式的一个解决方案，当时就已经有了微服务架构的理念。</p>
<p>微服务架构正式名称的诞生是在<strong>移动互联网时代</strong>，这时的生活已经实现全面互联网化，各种各样的生活类 APP 涌现，网民以及流量复杂度相对于新世纪互联网时代显著增强。另外，较大规模的研发团队也已成为主流。这时候，大家普遍都对效率有了更高的追求，而不只是原来只有几个巨头需要有这方面的技术。微服务架构以及微服务技术的推出，如 Spring Cloud、Dubbo 等框架的普及，极大地推广了微服务技术。</p>
<p>现在我们已经进入<strong>全面的数字化时代</strong>，社会全面互联网化，各种各样的单位（包括政企、相对传统的单位）都需要较强的研发能力。流量的挑战、业务复杂度的挑战、研发团队的扩大等，使得大家对效率有了更高的要求。这时候微服务架构得到了进一步的推广和普及。</p>
<p>微服务架构经过这么多年的发展，是经久不衰的一项技术，为什么它能够有这样持续的发展？</p>
<p><strong>2、微服务架构的优点</strong></p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/9c646ed9bcee46538da2814133a203e9~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>我们来回顾一下微服务架构和单体架构的区别，以及微服务架构的核心优势。</p>
<p>单体架构核心的问题在于冲突域太大，包括共享代码库。在研发过程中特别容易冲突；边界和模块的规模不清，使得团队效率也会降低。</p>
<p>而在微服务架构下，核心就在于拆分，包括解耦的研发态，解耦的部署态，极大地释放了团队的研发效率。大道至简，这也是微服务架构为什么能够持续发展的一个原因。</p>
<p><strong>3、微服务时代痛点</strong></p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/7051203e033b493e890117f27d55e4cb~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>根据复杂性守恒定律，我们解决了一个问题，问题会以另一种形式出现，我们又需要去解决。可以看到，微服务时代下会引入非常多的一些痛点，核心就是稳定性。因为从原来的一些本地调用改成远程调用以后，可能会发生稳定性的点激增，包括调度放大，即可能因为底层的一些远程调用问题，造成上层的一些不稳定，以及期间需要做的限流降级、调用链等。</p>
<p>在微服务时代定位一个问题的复杂度，也会成指数级的一个增长，这里面可能还需要服务治理。另外如果没有较好的设计和预先的一些设想，可能会出现微服务应用的爆炸，包括研发人员和测试人员之间的协作也都会成问题。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/b98b9e9d38c44025828c71ce05c67428~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>微服务技术经过这么多年的发展，业界其实已经有了一些解决方案。</p>
<p>如上图显示，如果要比较好地玩转微服务技术，除了开发自己的业务系统以外，可能还要配套地搭建多个系统，包括CI/CD、发布系统、研发流程、微服务组件相关的一些工具，以及可观测性相关的实时监控、告警系统、服务治理、调用链等等，还需要运维基础的 IaaS 资源。在这个时代，为了更好地运维 IaaS 资源，可能还需要自己维护一个K8s 集群。</p>
<p>所以说，在这样的背景下，很多企业会选择搭建一个运维团队，或者中间件团队，或者说由一些后端研发同学兼职。但是试想，有多少企业对自己内部搭建的这套系统是满意的？系统的迭代效率是多少，有没有踩到过一些开源的坑，这些坑现在有没有解决？这些应该是在企业的CTO、架构师心中一个持续的痛点。</p>
<h1 data-id="heading-1">Serverless时代下的解决方案</h1>
<p><strong>1、Serverless时代</strong></p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/48eacbce1d7a490e9a52123ddd329f0d~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>Serverless 从2012年第一次提出，到 2014年 推出了 Lambda 这样一个引爆性的产品后，短暂地达到了一个影响力的顶峰。但是这样一个新生事物，突然到真实的、复杂的生产环境中，其实有许多不适应，包括需要改善的地方，所以后续几年它可能要进入一个低谷。</p>
<p>但是，Serverless 的“<strong>将简单交给用户，复杂留给平台</strong>”的理念，其实是非常正确的一个方向。所以在开源界包括业界，其实都在持续性地进行 Serverless 方面的一些探索和发展。</p>
<p>阿里云在2017年推出了函数计算（Function Compute，FC），在2018年推出了Serverless应用引擎 SAE，在 2019年以及后续的这些年，阿里云持续地在 Serverless 领域进行投入，支持了包括镜像部署、预留实力、微服务场景等。</p>
<p><strong>2、Serverless 市场概况</strong></p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/bf606e09f49e4b1691e3666d6f238b4a~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>**在2021年最新的 Forrester 评测中，阿里云 Serverless 产品能力是中国第一、全球领先，阿里云的 Serverless 用户占比也是中国第一。**这侧面说明了阿里云 Serverless 是已经越来越多地进入到企业真实的生产环境中，越来越多的企业认可 Serverless 以及阿里云 Serverless 的能力和价值。</p>
<p><strong>3、SAE解决方案</strong></p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/836802b16c944596a51bdd39351e1454~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>可以看到，在传统的微服务架构下面，企业要用好微服务相关的技术需要自己研发非常多的解决方案，那么在 Serverless 时代下，在 SAE 这个产品里面是怎么解决的？</p>
<p>我们可以看到，SAE 将 Serverless 这个理念发扬到了极致，不仅仅托管了 IaaS 资源，包括上层的 K8s，另外还集成了白屏化的 PaaS 以及企业级微服务相关的套件和可观测相关的套件。在 SAE 整体解决方案里面，针对这些都进行了很好的集成，给用户提供了一个开箱即用的微服务解决方案，让企业和开发者能够很简单地使用微服务。</p>
<p><strong>1、0 门槛 PaaS</strong></p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/e4f0a1a98b9744a5a2376745dc845687~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>图中可以看到，SAE 在最上层给用户提供的是一个白屏化的操作系统，它的设计理念非常符合企业一般的 PaaS 系统，包括发布系统或者一些开源的 PaaS 系统，这样极大地降低了企业上手 SAE 的门槛，甚至可以说零门槛，包括它也集成了阿里巴巴最佳的一些发布，即发布三板斧——可观测、可灰度、可回滚。</p>
<p>另外它也提供了一些企业级能力的增强，包括命名空间环境隔离、细粒度的权限控制等等。从图中可以看到，在一个企业里面，如果有两个相互比较独立的模块，完全可以通过命名空间进程进行隔离。</p>
<p><strong>2、微服务治理增强</strong></p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/e1f10eb990cd49f88924e1bc6722778a~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>在微服务治理增强方面，特别是在 Java 语言，SAE 采用了一个 agent，对用户来说相当于是无侵入、无感知、零升级，而且 agent 的全面兼容开源，使用户几乎在无修改的情况下，就可以使用无损下限、API 管理、限流降级、链路追踪等等能力。</p>
<p><strong>3、前后端全链路灰度</strong></p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/e9aa10174aeb4c1bbdb3d4329d0fa983~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>这里展开两个能力，第一个能力是前后端全链路灰度。SAE 借助前面提到的 agent 技术，从 web请求到网关到 consumer 到 provide 进行了一个全链路的打通，使用户可以通过很简单的白屏化配置，就可以实现一个灰度发布场景。而这样的技术如果企业需要自建，这里面的复杂度大家应该是非常清楚的。</p>
<p><strong>4、CloudToolkit 端云联调</strong></p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/f222dfc176754e828dcdda4bbb7bc905~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>第二个能力就是 CloudToolkit 的端云联调。大家都知道微服务的场景下面应用数量是呈现一个爆炸的趋势，如果本地需要开发，需要启动那么多的应用，如何能够安全便捷地联调云上的一个服务？现在借助 CloudToolkit，用户可以很简单地在本地就打通云上的环境，进行一个端云联调，极大地降低开发测试的门槛。</p>
<p><strong>5、强大的应用监控 & 诊断</strong></p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/33e617e5fa784d59adfdaa64dd4d1342~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>在微服务的场景下，因为微服务的急剧发散、调用链路的极度增长，在有问题的场景下面定位问题是非常复杂的。而 SAE 集成了阿里云各种各样的可观测产品，包括Prometheus、IaaS、SLS、基础监控等，在 Tracing Logging Metrics 等方面都提供了丰富的解决方案，包括请求链路的查询，常用的诊断场景的指标分析，基础监控、实时日志、事件通知等等，这些都能极大地降低企业在微服务台运行场景下的一些日常定位问题。</p>
<h1 data-id="heading-2">SAE的技术原理和极致弹性建设</h1>
<p>前面已经针对三部分，也就是零门槛PaaS、企业级微服务套件、可观测进行了一个讲解。那么现在要介绍 Serverless 的一个核心模块，也就是 IaaS 层面上免运维以及弹性能力的建设。</p>
<p><strong>1、SAE 业务架构</strong></p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/cb62e23f3817466c84e3ce37f3935c98~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>通过这张 SAE 的业务架构图，大家就可以相对比较清晰地看出，在SAE里面 IaaS 资源包括存储、网络等是不需要用户关心的。另外 SAE 也托管了 K8s 这个 PaaS 层的一个组件，相当于用户也不需要自己去运维 K8s 。在 K8s 层之上，SAE 提供了微服务治理、应用生命周期管理等增强的能力。另外在弹性方面，SAE 的弹性能力达到了15秒，相信在很多企业级的场景下，这已经能帮助开发者较好地应对一些突发流量的情况。另外通过多套环境以及一些最佳实践，可以达到一个降本增效的效果。</p>
<p><strong>2、SAE 技术架构</strong></p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/4c9b79eee08f4e508938e3383193f3fa~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>那么 SAE 是怎么建设免运维，对用户来说，相当于不需要托管的一个 IaaS 资源以及 K8s 资源呢？</p>
<p>上图中可以看到，SAE 底层其实是采用了一种安全容器的技术，相比于Docker，安全容器相当于提供了虚拟机级别的一个安全解决方案。在 RunC 场景下，由于共享内核其实在公有云产品上，a用户有可能穿透到 b 用户的一个容器内，造成一些安全风险。采用安全容器的技术，也就是虚拟机相关的安全技术，达到了一个生产级别的安全隔离，包括安全容器也进入了 K8s 以及容器的生态。这样安全容器+容器生态的结合，就实现了较好的安全+效率的一个平衡。</p>
<p>另外在存储和网络的隔离方面，SAE 不仅仅需要考虑传统的 K8s 上的网络隔离，也需要考虑在公有云产品下，大部分用户已经在公有云上有非常多的一些存储资源、网络资源，这些也需要进行一个打通。</p>
<p>SAE 采用了云产品的 ENI网卡技术，将 ENI网卡直通到了安全沙箱内，这样相当于用户不仅仅实现了一个计算层的隔离，也实现了网络层的打通。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/339479372e1a4649933a4e2d1437df27~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>可以看到现在主流的安全容器技术有 Kata、Firecracker、gVisor 等等，在 SAE 里面是采用了最早也是最成熟的 Kata 技术来实现一个计算成安全的隔离。另外安全容器不仅实现了一个安全的隔离，也实现了一个性能隔离和故障隔离。</p>
<p>举一个比较好理解的例子，在 RunC 大家共享内核的场景下，一个用户的 Container 造成了一些内核的故障，是直接可能影响到物理机的。在 SAE 使用安全容器基础上就没有这方面的风险，最多只会影响到那一个安全容器。</p>
<p><strong>3、极致弹性 极致成本</strong></p>
<p>下图中可以看到，如果弹性效率达到了一个极致，用户的成本也可以达到一个极致。通过左右两边的图的对比，大家可以理解弹性对用户成本可以达到的一个效果。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/8856f403a2e74856bf7757637b9071f6~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p><strong>1、SAE 极致弹性建设：部署 & 重启</strong></p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/e196c52f5d624f00b362172750a452bd~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>SAE 在弹性方面做了哪些事情呢？可以看到传统的 K8s 的一个 Pod 的创建过程需要经过调度、init container的创建、拉取用户镜像、创建用户容器、启动用户容器、应用运行等等阶段，它虽然符合 K8s 的设计理念和规范，但是在生产环境下，对一些需要相对比较要求效率的场景，其实就不太满足企业级的要求。而 SAE 借助于阿里巴巴开源里面的 CloneSet 组件的原地升级策略，相当于不需要重建整个 Pod，而只需要重建里面的 container 省去了调度以及 innt containr 创建的一个过程，部署效率达到了 42% 的提升。</p>
<p><strong>2、SAE 极致弹性建设：弹性扩容</strong></p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/3f070994fc2744eb8a464be19bbaaa04~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>在镜像预热场景 SAE 也实现了一个并行的调度。可以看到，在标准的场景下，调度到用户拉取镜像是一个串行的过程。那么在此做了一个优化，就是在识别到 pod 即将调入到单个物理机的时候，它就会并行地开始拉取用户的镜像，这样也可以达到一个弹性效率 30% 的提升。</p>
<p><strong>3、SAE 极致弹性建设：Java启动加速</strong></p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/9bdf2122f0fe429184f551e398c60e39~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>那么在应用启动这个阶段，我们也做了一些弹性效率能力提升的事情。比如说 Java 的应用，在 Serverless 场景下其实一直有启动慢的痛点，核心在于 Java 需要一个个加载。而在一些企业级的应用里面，针对成千上万的 class 的加载，这肯定是一个相对较缓慢的过程。</p>
<p>SAE 结合阿里巴巴开源的 Dragonwell 实现了 App CDS 的技术，它会在应用第一次启动的时候，将 class 加载打到一个压缩包中，后续的应用加载，只需要加载压缩包即可，免去了大量 class 的一个串行化的加载，实现了部署效率 45% 的一个提升。</p>
<p><strong>4、SAE极致弹性建设</strong></p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/0bbcdebeddec4a57acc8625ccaea08be~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>最后在应用运行态，我们也做了一些弹性方面的增强。微服务的应用通常会需要配置非常多的一些线程，这些线程通常和 Linux 的底层线程是一一对应的。在高并发场景下，这里面就会有较大的线程切换的开销。SAE 结合阿里巴巴开源的 Dragonwell，WISP 线程的技术，将上层的几百个线程对应到了底层的十几个线程，极大的降低了线程切换的一个开销。</p>
<p>上图中是我们一个压测的数据。红线就是使用了 Dragonwell、WISP 的技术，可以看到运行效率有 20% 左右的提升。</p>
<p>以上就是 SAE 在 Serverless、IaaS 托管以及 K8s 托管方面，还有在弹性效率方面建设的一些技术原理和效果。</p>
<h1 data-id="heading-3">总结和展望</h1>
<p>原来的微服务用户需要自建非常多的组件，包括 PaaS 微服务一些技术框架，运维 IaaS、K8s，还包括可观测组件等。SAE 针对这些方面都做了整体的解决方案，使用户只需要关注自己的业务系统，这极大地降低了用户使用微服务技术的门槛。</p>
<p>后续 SAE 针对每个模块也会持续地的做能力的建设。包括：</p>
<ul>
<li>在零门槛 PaaS 方面，微服务会持续做一些云产品的集成，包括 CICD 工具链。另外也会做企业级的能力增强，比如审批流等。</li>
<li>在 Serverless 免运维、极致弹性方面，我们也会提供越来越多的弹性能力、弹性指标、弹性效率，这些也都会持续地建设。另外也会提供类似 AI 预测这样的弹性解决方案，降低用户设置弹性指标的时候的心智负担。</li>
<li>在微服务生态方面，我们也会和微服务的企业套件做更多的集成，进一步降低大家使用微服务技术的门槛，比如说混沌工程、远程调试能力增强等。</li>
</ul>
<p>最后在可观测方面，SAE 相当于运维了用户的应用。那么可观测对于 SAE 本身或者说对平台本身也是一个非常重要的能力，在这方面我们会持续地做相应的一些监控告警，包括预案和灰度建设等等。对用户来说，也需要在SAE上托管它的应用，这就要求产品能够降低用户在使用这方面的门槛，后续会建设应用大盘、事件中心等等。</p>
<p><a href="https://link.juejin.cn/?target=http%3A%2F%2Fclick.aliyun.com%2Fm%2F1000284237%2F" target="_blank" rel="nofollow noopener noreferrer" title="http://click.aliyun.com/m/1000284237/" ref="nofollow noopener noreferrer">原文链接</a></p>
<p>本文为阿里云原创内容，未经允许不得转载。</p></div>  
</div>
            