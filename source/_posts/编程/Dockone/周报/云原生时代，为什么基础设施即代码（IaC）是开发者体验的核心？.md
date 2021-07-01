
---
title: '云原生时代，为什么基础设施即代码（IaC）是开发者体验的核心？'
categories: 
 - 编程
 - Dockone
 - 周报
headimg: 'https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210629/d96eab9dcf7f980511cd98c08559c065.png'
author: Dockone
comments: false
date: 2021-07-01 06:08:22
thumbnail: 'https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210629/d96eab9dcf7f980511cd98c08559c065.png'
---

<div>   
<br><h3>从一个小故事开始</h3>你是一个高级开发工程师。<br>
<br>某天，你自信地写好了 <code class="prettyprint">自动煮咖啡</code>  功能的代码，并在本地调试通过。代码合并入主干分支后，你准备把服务发布到测试环境，进入提测流程。<br>
<br>你熟练地打开项目协同，新建了一个发布工单给运维同学，详细备注了需要发布的代码分支，并特别强调这次需要专门新增一个开关 <code class="prettyprint">AUTO_MAKE_COFFIE_``ENABLED``=true</code>。<br>
<br>过了一段时间，工单处理完成，测试同学开始测试。<br>
<br>突然，噩耗传来：你的项目协同里出现了几个 Bug。<br>
<br>你很疑惑，为什么本地完美运行的代码，在测试环境被提了这么多 Bug ？<br>
<br>你开始怀疑代码中某个地方的逻辑有问题。可仔细排查后却仍然定位不到问题。<br>
<br>最后，你终于发现，是运维同学复制环境变量时少复制了一个字母：<br>
<br>关 <code class="prettyprint">AUTO_MAKE_COFFIE_``ENABLE``=true</code>，<code class="prettyprint">ENABLED</code> 少了一个 <code class="prettyprint">D</code>。<br>
<br>上面这种情况是不是很熟悉？虽然不是你的锅，却拖慢了你成为十倍程序员的进度。<br>
<br>那么，该怎么避免呢？  <br>
<br>你一定在想：要是没有手工复制操作就好了。那就要有个地方来保存你的配置，但是你没有权限、也不想登录到运维操作平台自己粘贴配置。<br>
<br>你灵光一现：要是和运维同学约定好一个配置文件，把部署配置也提交进代码里，运维同学从文件里读取应用环境配置，问题就迎刃而解了。<br>
<h3>IaC 是什么</h3>在上面的故事里，这个特殊约定好的配置文件就是这个应用基础设施的一部分（IaC 中的 I）。<br>
<br>我们该怎么理解基础设施呢？一个稍微复杂点的应用，只有代码是无法运行起来的，因为它还有很多环境依赖需要被准确描述，比如需要运行环境有 make、git 等指定的命令行工具，依赖了哪些中间件等。<br>
<br>因此，产品团队在实施持续交付的过程中，必须考虑将基础设施的维护纳入进来，作为支持产品运行的一部分。<br>
<br>同时，技术的快速进步和演化，也使得基础设施的配置不得不频繁变化。在这种快速变化的过程中，要求基础设施既要灵活，也要安全、可靠。<br>
<br>参考 Wikipedia 上的定义，IaC 里的 Infrastructure 广义上是指 IaaS 层的基础设施，包括物理服务器、虚拟机以及相关的资源定义等。As Code 是指这些配置都应该被放到 VCS 上管理起来。<br>
<br>As Code 的好处是，你可以享受版本管理天然的福利，很方便地做一些回滚操作等。<br>
<br><blockquote><br>当你把 Code 维护在 Git 里，就成了 GitOps。感兴趣的同学可以自行搜索 GitOps 相关文章进行学习。</blockquote>那么，As Code 里的 Code 应该长什么样？这个格式由具体的自动化平台来定。至于 Code 的类型，指令式和声明式都可以。例如，常见的 Ansible 一般来说是指令式的，而 Terraform 是声明式的。当然，声明式定义更为推荐，因为这是一种面向终态的定义，对开发者屏蔽了具体实现细节，更加友好。<br>
<h3>云原生时代，以应用为中心的 IaC 有什么不同？</h3>时间快进到云原生时代。<br>
<br>在服务上云的大趋势下，基础设施的概念已经不再局限于 IaaS 层。云原生时代，开发者的焦点逐渐聚集到了应用上。即：以应用为中心。<br>
<br>持续集成、持续部署和 DevOps 这些概念的广泛推行和接受，要求产品团队对部署和运维要有更高的自主性。<br>
<br>首先，在 DevOps 概念深入人心的今天，一个高级开发工程师如果仅仅是把代码写好，是远远不够的，那只是做好了 Dev。真正的软件交付的生命周期，是从 Ops 开始的，运维同学早已不再负责应用的部署和运维，这都是开发者的事情。<br>
<br>Docker 的出现使得镜像交付成为大多数应用软件事实上的交付标准。所以，应用里需要有一个文件来定义怎么样把你的代码制作成镜像，这个文件通常是 Dockerfile。  <br>
<br>与此同时，PaaS 平台的普及，使得开发者甚至不需要关心 Dockerfile。因为 PaaS 平台可以通过你的应用目录结构和特征文件，自动探测和选择合适的构建方式，这个代码编译和镜像构建的过程被称为 BuildPack。当然，在编译之前，你可能还需要做一些代码质量检查、合规性检查等，这些流程化的配置，需要有一个流程描述文件来声明。在不同的 PaaS 平台上，会有不同的声明方式。<br>
<br>Erda DOP 里怎么样把 IaC 做得更好<br>
<br>Erda 是一个以应用为中心的企业级一站式数字化 PaaS 平台。<br>
<br>DOP，即 DevOps Platform，是一个以应用为中心的一站式的 DevOps 平台。<br>
<br>一个 Erda 应用支持代码质量扫描、代码安全扫描、单元测试执行等，镜像制作好之后，还有镜像安全扫描、持续部署、接口自动化测试等。通过这些流程对应用的全生命周期进行管理。<br>
<br>在这个平台上，你可以使用 pipeline.yaml 来定义应用的 CI/CD 全流程。很显然，这个 pipeline.yaml 就是这个应用基础设施的一部分。<br>
<br>同时，你需要用一个声明式的 erda.yaml 来描述你的应用微服务架构，包括微服务之间的依赖关系、对中间件的依赖等等。<br>
<br>在平台设计之初，我们就对应用做了抽象，使得它可以被部署到任意平台，包括 Kubernetes、DC/OS 等，对开发者屏蔽了具体实现细节。<br>
<br>因此，当应用部署在 Erda PaaS 平台上时，这两个文件是必不可少的。<br>
<br><blockquote><br>值得一提的是，在平台最早期的时候，我们只有一个 erda.yaml 文件，里面把微服务架构和构建过程写在一起。在实践过程中，我们逐渐意识到这样的方式扩展性不够，很难进行流程定制。并且命令式和声明式的两种形态耦合在同一个文件中，使用者的心智切换成本也更高。</blockquote>除此之外，我们还支持在 .erda 目录下定义 API 描述文件来对 API 全生命周期进行管理。<br>
<br>当这些 Infrastructure 都被作为 Code 提交之后，Erda 平台就可以根据这些配置，进行持续集成和持续交付，最终自动把应用完整地部署起来。<br>
<br>以 Erda 自身举例，Erda 本身的持续集成、自动版本发布等，都是在 Erda 平台上自举的。<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210629/d96eab9dcf7f980511cd98c08559c065.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210629/d96eab9dcf7f980511cd98c08559c065.png" class="img-polaroid" title="1.png" alt="1.png" referrerpolicy="no-referrer"></a>
</div>
<br>
<em>erda.yaml 部分截图</em><br>
<br><div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210629/0d2bfd08c14fd338fcbd9156d9513d11.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210629/0d2bfd08c14fd338fcbd9156d9513d11.png" class="img-polaroid" title="2.png" alt="2.png" referrerpolicy="no-referrer"></a>
</div>
<br>
<em>用于 CI 的 pipeline.yaml 部分截图</em><br>
<br>当你的应用是一个标品时，有了 IaC，给客户交付这个应用就变得非常简单。你要做的，只是把代码仓库完整地推送到新的应用代码仓库里，然后执行流水线。执行完毕后，一个完整的应用就被交付到了新的客户环境里。之后，开发者在这个新应用进行定制化开发，在应用基础设施变更时，把变更提交到代码里进行版本控制管理。<br>
<h3>总结</h3>> You build it, you run it.<br>
<br>所以我们说，<strong>基础设施即代码（IaC）是云原生时代开发者体验的核心</strong>。<br>
<br>有了 IaC，作为开发者的你，终于可以更好地掌握应用的全生命周期了。<br>
<br>原文链接：<a href="https://mp.weixin.qq.com/s/kAvxNJi3fKWu6Cd0ePTTaA" rel="nofollow" target="_blank">https://mp.weixin.qq.com/s/kAvxNJi3fKWu6Cd0ePTTaA</a>
                                                                <div class="aw-upload-img-list">
                                                                                                                                                                                                </div>
                                
                                                                <ul class="aw-upload-file-list">
                                                                                                                                                                                                                    </ul>
                                                              
</div>
            