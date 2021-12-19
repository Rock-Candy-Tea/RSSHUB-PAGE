
---
title: '传统架构 vs 云原生架构，谈谈为什么我们需要云原生架构？'
categories: 
 - 编程
 - Dockone
 - 周报
headimg: 'https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20211214/3d88b78f16e01c1a757fbbc1ca38c2da.png'
author: Dockone
comments: false
date: 2021-12-19 03:08:38
thumbnail: 'https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20211214/3d88b78f16e01c1a757fbbc1ca38c2da.png'
---

<div>   
<br><h3>云原生架构是什么</h3>回顾过去十年，数字化转型驱动着技术创新和商业元素的不断融合和重构，可以说，现在已经不是由商业模式决定采用何种技术架构，而是由技术架构决定企业的商业模式。所以无论是行业巨头还是中小微企业都面临着数字化转型带来的未知机遇和挑战。机遇是商业模式的创新，挑战来自对整体技术架构的变革。<br>
<br>新一代的技术架构是什么？如何变革？是很多互联网企业面临的问题。而云原生架构则是这个问题最好的答案，因为<strong>云原生架构对云计算服务方式与互联网架构进行整体性升级，深刻改变着整个商业世界的 IT 根基</strong>。<br>
<br>虽然云原生的概念由来已久，很多人并不理解什么是云原生。从技术的角度来讲，云原生架构是基于云原生技术的一组架构原则和设计模式的集合，旨在将云应用中的非业务代码部分进行最大化的剥离，从而让云设施接管应用中原有的大量非功能特性（如弹性、韧性、安全、 可观测性、灰度等），使业务不再受非功能性业务中断困扰的同时，具备轻量、敏捷、高度自动化的特点。<strong>简单的说，就是帮助企业的业务功能迭代更快、系统能承受住各种量级的流量冲击的同时，构建系统的成本更低。</strong><br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20211214/3d88b78f16e01c1a757fbbc1ca38c2da.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20211214/3d88b78f16e01c1a757fbbc1ca38c2da.png" class="img-polaroid" title="1.png" alt="1.png" referrerpolicy="no-referrer"></a>
</div>
<br>
<em>传统架构与云原生架构的区别</em><br>
<br>上图展示了在代码中通常包括的三部分内容，即业务代码、第三方软件、处理非功能特性的代码。其中“业务代码”指实现业务逻辑的代码。“三方软件”是业务代码中依赖的所有三方库，包括业务库和基础库。“处理非功能性的代码”指实现高可用、安全、可观测性等非功能性能力的代码。<br>
<br>这三部分中只有业务代码是对业务真正带来价值的，另外两个部分都只算附属物，但随着软件规模的增大、业务模块规模变大、部署环境增多、分布式复杂性增强，使得今天的软件构建变得越来越复杂，对开发人员的技能要求也越来越高。云原生架构相比较传统架构前进了一大步，即<strong>从业务代码中剥离了大量非功能性特性到 IaaS 和 PaaS 中</strong>，从而减少业务代码开发人员的技术关注范围，通过云服务的专业性提升应用的非功能性能力。<br>
<br>这便是云原生架构的核心思路。<br>
<h3>为什么需要云原生架构</h3>解释完什么是云原生架构后，大家可能会有进一步的思考，即当今互联网企业为什么需要云原生架构。分析下 SaaS 的市场规模可以发现，2019 年 SaaS 市场规模为 360 亿元，2020 年仍保持可观上涨趋势，2022 年 SaaS 市场规模预计破千亿。<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20211214/b33f6a9cb615b91eeca43971b76cae0f.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20211214/b33f6a9cb615b91eeca43971b76cae0f.png" class="img-polaroid" title="2.png" alt="2.png" referrerpolicy="no-referrer"></a>
</div>
<br>
纵观中国企业级 SaaS 行业发展历程，大体分为四个阶段：2015 年之前，中国市场和绝大多数中国企业对“什么是 SaaS”缺乏基本认知，基于私有部署的传统软件形式仍为主流，企业级 SaaS 市场方兴未艾。到了 2015 年，随着云计算技术的进一步成熟，中国企业级 SaaS 行业进入快速成长阶段，这个慢赛道逐渐为公众所知。<br>
<br>时至今日，在疫情、经济、社会环境的大背景下。互联网企业开始寻求新的商业模式，一些抓住机会的 SaaS 企业实现了快速响应，结果是其业务呈现成倍增长，比如：<br>
<ul><li>餐饮 SaaS 厂商帮助线下餐饮门店开发小程序点餐系统，实现无接触点餐。</li><li>电商零售领域的 ERP 厂商帮助企业建立会员管理系统。</li><li>营销 SaaS 厂商通过流量平台帮助企业在线营销，远程触达客户。</li></ul><br>
<br>所以，在“如何活下去”成为热门议题的背景下，快速响应能力成为企业之间的核心竞争优势，SaaS 企业需要及时满足市场的新需求。而这正是前几年中国 SaaS 企业为了快速占领市场、盲目跟风、一味借鉴国外产品所产生的天生缺陷。为弥补这些缺陷，SaaS 厂商需要根据市场的需求快速调整产品服务方向，业务功能要多元化，业务体系需要新的枝杈，在技术上也有更大的挑战。<br>
<br>除了市场带来的压力，SaaS 企业自身也有诸多痛点：<br>
<ul><li>大多 SaaS 产品只做所谓的通用能力，或者只是一味模仿国外产品，一旦深入到行业属性比较重的场景时便无法满足需求，所以被贴上了“半成品”的标签，导致市场接受程度不如预期。</li><li>产品模块单一、功能相似的 SaaS 产品很容易陷入价格竞争，最后只能以亏损获得网络效应，但会终食恶果。</li><li>市场对 SaaS 产品的定制化需求过多，使得 SaaS 企业缺乏对产品打磨的精力，把一个 SaaS 型公司做成了项目型公司。</li></ul><br>
<br>SaaS 企业解决以上的外忧内患的核心就是<strong>专注在业务</strong>。要做好一款 SaaS 产品，对于业务渠道、竞争格局、用户体验等诸多方面都有更加严苛的要求，甚至从市场运营、产品经理到研发、运维都要专注在业务，所有这些角色的本职工作都应该为行业业务服务，行业的深度分析，快速响应市场，稳定的产品质量这些是必须要具备的。<br>
<br>但这就要求技术具备<strong>更快的迭代速度</strong>，业务推出速度从按周提升到按小时，每月上线业务量从“几十/月”提升到“几百/天”，并且不可接受业务中断。<br>
<br>另一个互联网企业需要云原生转型的原因是中国的刘易斯拐点已经到来。刘易斯拐点，即劳动力过剩向短缺的转折点，是指在工业化进程中，随着农村富余劳动力向非农产业的逐步转移，农村富余劳动力逐渐减少，最终达到瓶颈状态。用大白话说就是中国的人口红利已经逐渐消退，企业劳动力成本不断增加，加上 2020 年疫情的影响，成本因素越来越成为企业的重要考量。<br>
<br>而 SaaS 产品订阅制付费、通用性强、低部署成本的特点，便成了<strong>企业降本增效</strong>的新选择。这是 SaaS 企业在市场中的机会，而且对于 SaaS 企业本身来说，同样有降本增效的需求，而且内部降本增效做得越好，SaaS 产品在市场上的竞争力会更加明显。<br>
<br>以上这些现状的解法和云原生架构和核心能力不谋而合：<br>
<ul><li>云原生将三方软件和非功能性能力的完全兜底，可以极大程度解放企业研发、运维人员的精力，并使其可以专注在业务上。</li><li>系统的横向扩展性、高可用性、健壮性、SLA 由云原生架构兜底，解决了 SaaS 产品最忌讳的稳定性问题。</li><li>将一些自建的组件迁移至云原生架构中，对传统的部署方式和资源进行云原生化，GitOps 的落地，在资源成本和人力成本方面都有进一步的优化。</li></ul><br>
<br><h3>如何落地云原生架构</h3>在聊如何落地云原生架构之前，我们先来看一看云原生架构成熟度模型（SESORA）：<br><br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20211214/c0a7933c9f213829ce816096f9e86094.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20211214/c0a7933c9f213829ce816096f9e86094.png" class="img-polaroid" title="3.png" alt="3.png" referrerpolicy="no-referrer"></a>
</div>
<br>
<em>云原生架构成熟度模型</em><br>
<br>云原生架构成熟度模型有六个评判维度，可以将成熟度划分为 4 个级别。我会从自动化能力、无服务化能力、弹性能力、可观测性、韧性能力这五个维度，贯穿说明如何落地云原生架构。<br>
<h4>传统架构</h4><div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20211214/f5d1272c40bfea57db95ad939dc42910.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20211214/f5d1272c40bfea57db95ad939dc42910.png" class="img-polaroid" title="4.png" alt="4.png" referrerpolicy="no-referrer"></a>
</div>
<br>
上图展示的是一个较传统的 Java+Spring Cloud 架构应用服务侧的部署架构。除了 SLB，基本上所有的组件都部署在 ECS 上。下面我们来一起看看如何将这个架构转型为云原生架构。<br>
<h4>无服务化（Serverless）</h4>Serverless 的概念是什么在这篇文章不再赘述，可以参阅<a href="https://mp.weixin.qq.com/s?__biz=MzU4NzU0MDIzOQ==&mid=2247491052&idx=3&sn=0238428fd6ef0f812722c4af0736b7ea&scene=21#wechat_redirect">这篇文章</a>进行了解。使用 ECS 集群部署服务的架构有两个显著的短板：<br>
<ul><li>运维成本高：ECS 的各项状态、高可用都需要运维同学维护。</li><li>弹性能力不足：每次有大促活动时，都需要提前购买 ECS，扩展服务的节点数，然后再释放，并且这种情况只适用于定时定点的活动，如果是不定时的流量脉冲则无法应对。</li></ul><br>
<br>所以首先我们要将服务的部署方式 Serverless 化，我们可以选择 Serverless App Engine（SAE）作为服务应用的发布、部署平台。SAE 是面向应用的 Serverless PaaS 平台，能够帮助用户免运维 IaaS、按需使用、按量计费，做到低门槛服务应用云原生化，并且支持多种语言和高弹性能力。<br>
<br><strong>1、命名空间</strong><br>
<br>打开 SAE 控制台，我们首先创建命名空间，SAE 的命名空间可以将其下的应用进行网络和资源的逻辑隔离，通常我们可使用命名空间来区分开发环境、测试环境、预发环境、生产环境。<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20211214/193e238f359fef03a1a00ec100aa7361.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20211214/193e238f359fef03a1a00ec100aa7361.png" class="img-polaroid" title="5.png" alt="5.png" referrerpolicy="no-referrer"></a>
</div>
<br>
<strong>2、创建应用</strong><br>
<br>创建好命名空间后，我们进入应用列表，即可选择不同的命名空间，看到其下的应用或者创建应用：<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20211214/c81f62f970c4ae10b31c681f72f4087d.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20211214/c81f62f970c4ae10b31c681f72f4087d.png" class="img-polaroid" title="6.png" alt="6.png" referrerpolicy="no-referrer"></a>
</div>
<br>
选择对应的命名空间，然后创建应用：<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20211214/45b823c9576b1542ac5af983782008a8.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20211214/45b823c9576b1542ac5af983782008a8.png" class="img-polaroid" title="7.png" alt="7.png" referrerpolicy="no-referrer"></a>
</div>
<br>
<ul><li>应用名称：服务名称，用户自行输入。</li><li><br>专有网络配置：<br>
<ul><li>自动配置：自动帮用户配置 VPC、Vswitch、安全组。这些组件都会新创建。</li><li>自定义配置：用户选择命名空间，VPC，VSwitch 以及安全组。一般选择自定义配置，因为咱们的服务所属的VPC肯定要和其他云资源的 VPC 是相同的，这样才能保证网络畅通。这里需要注意的一点是，当在新的命名空间下第一次创建好应用后，该命名空间就会和所选的 VPC 进行绑定，之后再创建应用时，该命名空间对应的 VPC 不可更改。如果需要更改，可以进入命名空间详情进行更改。</li></ul></li><li><br>应用实例数：应用（服务）节点数量，这里的节点数量按需设置，而且不是最终设定，因为后续可以手动或者自动的扩缩节点数。</li><li>VCPU/ 内存：该应用在运行过程中需要的CPU和内存的规格。这里的规格是单个实例数的规格。既如果选择了 2C4G，那么有 2 个实例的话，就是 4C8G。</li></ul><br>
<br>配置完基本信息后，下一步进入应用部署配置：<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20211214/029697aabc35c69ba0c97e5071ecf1ee.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20211214/029697aabc35c69ba0c97e5071ecf1ee.png" class="img-polaroid" title="8.png" alt="8.png" referrerpolicy="no-referrer"></a>
</div>
<br>
<ul><li><br>技术栈语言：Java 语言支持镜像、War 包、Jar 包三种部署方式，其他语言支持镜像部署方式。以 Java Jar 包方式为例：<br>
<ul><li>应用运行环境：默认标准 Java 应用运行环境即可。</li><li>Java 环境：目前支持 JDK7 和 JDK8。</li><li>文件上传方式：支持手动上传 Jar 包或者配置可以下载 Jar 包的地址。</li></ul></li><li><br>版本：支持时间戳和手动输入。</li><li>启动命令设置：配置 JVM 参数。</li><li>环境变量设置：设置容器环境中的一些变量，便于应用部署后灵活的变更容器配置。</li><li>Host 绑定设置：设置 Host 绑定，便于通过域名访问应用。</li><li>应用健康检查设置：用于判断容器和用户业务是否正常运行。</li><li>应用生命周期管理设置：容器侧的生命周期脚本定义，管理应用在容器在运行前和关闭前的一些动作，比如环境准备、优雅下线等。</li><li>日志收集服务：和 SLS 日志服务集成，统一管理日志。</li><li>持久化存储：绑定 NAS。</li><li>配置管理：通过挂载配置文件的方式向容器中注入配置信息。</li></ul><br>
<br>我使用 Jar 包的方式部署完应用后，在对应命名空间下就可以看到刚刚创建的应用了：<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20211214/44d80a73374b818a390975d4a0164a21.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20211214/44d80a73374b818a390975d4a0164a21.png" class="img-polaroid" title="9.png" alt="9.png" referrerpolicy="no-referrer"></a>
</div>
<br>
点击应用名称可以查看应用详情：<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20211214/a95fcceb9c04939b674edcc7ab9ee5f1.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20211214/a95fcceb9c04939b674edcc7ab9ee5f1.png" class="img-polaroid" title="10.png" alt="10.png" referrerpolicy="no-referrer"></a>
</div>
<br>
<strong>3、绑定 SLB</strong><br>
<br>因为 ServiceA 在架构中是对外提供接口的服务，所以需要对该服务绑定公网 SLB 暴露 IP 和做负载均衡，在 SAE 中，绑定 SLB 非常简单，在详情页中，即可看到应用访问设置：<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20211214/f3385ca44f83a8c51b9532764989404d.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20211214/f3385ca44f83a8c51b9532764989404d.png" class="img-polaroid" title="11.png" alt="11.png" referrerpolicy="no-referrer"></a>
</div>
<br>
添加 SLB 时可以选择新建也可以选择已经创建好的 SLB：<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20211214/060cf9dd7892940f3436de11e244ad2f.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20211214/060cf9dd7892940f3436de11e244ad2f.png" class="img-polaroid" title="12.png" alt="12.png" referrerpolicy="no-referrer"></a>
</div>
<br>
<strong>4、服务/配置中心</strong><br>
<br>对于微服务架构，服务中心和配置中心是必不可少的，大家常用到一般是 Nacos、Eureka、ZooKeeper 三种。对于云原生架构来讲，根据不同的场景，服务/配置中心可以有以下几种选择：<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20211214/c28ce8567d8134838a1d6fc3c7cea94d.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20211214/c28ce8567d8134838a1d6fc3c7cea94d.png" class="img-polaroid" title="13.png" alt="13.png" referrerpolicy="no-referrer"></a>
</div>
<br>
对于现状就是使用 Nacos 的客户而言，转型云原生架构，服务/配置中心如上面表格所示有两种选择：<br>
<ul><li>需要快速转型，对服务/配置中心高可用要求不是特别极致的情况下，建议直接使用 SAE 自带的 Nacos 即可，代码不需要做改动，直接在 SAE 中创建应用即可。SAE 控制台提供的配置管理在界面操作和功能上和开源 Nacos 的控制台基本一致。<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20211214/406f0c9dc6f2f94b539b92580313e7d4.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20211214/406f0c9dc6f2f94b539b92580313e7d4.png" class="img-polaroid" title="14.png" alt="14.png" referrerpolicy="no-referrer"></a>
</div>
</li><li>对服务/配置中心高可用要求比较高的情况下，建议使用 MSE Nacos，它的优势是独享集群，并且节点规格和节点数量可以根据实际情况动态的进行调整。唯一不足的一点就是需要修改 Nacos 的接入点，算是有一点代码侵入。</li></ul><br>
<br>对于现状是使用 Eureka 和 ZooKeeper 的客户而言，建议直接使用 MSE Eureka 和 MSE ZooKeeper。<br>
<br>这里我简单介绍一下 MSE。微服务引擎 MSE（Microservice Engine）是一个面向业界主流开源微服务框架 Spring Cloud 和 Dubbo 一站式微服务平台，提供治理中心、托管的注册中心和托管的配置中心。这里我们用到的是 MSE 的托管注册中心和托管配置中心。<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20211214/d8f402d3088352e1c0e44cc84cf2a118.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20211214/d8f402d3088352e1c0e44cc84cf2a118.png" class="img-polaroid" title="15.png" alt="15.png" referrerpolicy="no-referrer"></a>
</div>
<br>
MSE 有三块核心的功能点：<br><br>
<ul><li>支持三大主流服务中心，节点规格和数量灵活搭配，可在运行时动态调整节点规格/数量。<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20211214/7efc2d7d70c873ef51a9e03a32233b50.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20211214/7efc2d7d70c873ef51a9e03a32233b50.png" class="img-polaroid" title="16.png" alt="16.png" referrerpolicy="no-referrer"></a>
</div>
</li><li>通过命名空间逻辑隔离不同环境。<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20211214/4aeb44a8239f10e493a1375d1805c2a3.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20211214/4aeb44a8239f10e493a1375d1805c2a3.png" class="img-polaroid" title="17.png" alt="17.png" referrerpolicy="no-referrer"></a>
</div>
</li><li>配置变更实时推送并且可追踪。<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20211214/c0e5224bd5ad45fadd16d02ddcbf6cc4.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20211214/c0e5224bd5ad45fadd16d02ddcbf6cc4.png" class="img-polaroid" title="18.png" alt="18.png" referrerpolicy="no-referrer"></a>
</div>
</li></ul><br>
<br><h4>弹性能力（Elasticity）</h4>云原生架构成熟度模型中的弹性能力同样依托于 SAE 来实现，因为 Serverless 的底层实现原理，所以在 SAE 中的应用实例数（节点数）扩缩速度非常快，可达到秒级。<br>
<br>进入应用详情页的实例部署信息，可以看到应用的具体实例：<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20211214/8eed283e851ab0ebbc639d2503b7d258.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20211214/8eed283e851ab0ebbc639d2503b7d258.png" class="img-polaroid" title="19.png" alt="19.png" referrerpolicy="no-referrer"></a>
</div>
<br>
SAE 提供了两种扩缩应用实例数的方式，手动方式和自动方式。<br>
<br><strong>1、手动扩缩</strong><br>
<br>在控制台右上方有手动扩缩操作按钮，然后选择要扩缩到的实例数即可：<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20211214/2624824e555f1b34e44c0f0ed7279f75.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20211214/2624824e555f1b34e44c0f0ed7279f75.png" class="img-polaroid" title="20.png" alt="20.png" referrerpolicy="no-referrer"></a>
</div>
<br>
当进行扩缩时，我们可以看到具体实例的变更状态：<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20211214/f21e65b953bf9d6125d50881d16d2f4a.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20211214/f21e65b953bf9d6125d50881d16d2f4a.png" class="img-polaroid" title="21.png" alt="21.png" referrerpolicy="no-referrer"></a>
</div>
<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20211214/53b2fa07abe6dbe0bb8ea4b6967904bf.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20211214/53b2fa07abe6dbe0bb8ea4b6967904bf.png" class="img-polaroid" title="22.png" alt="22.png" referrerpolicy="no-referrer"></a>
</div>
<br>
<strong>2、自动扩缩</strong><br>
<br>在控制台右上角有自动扩缩操作按钮，然后可以看到创建扩缩规则的界面。SAE 自动扩缩提供时间策略和指标策略两种。<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20211214/24ad27afc65853d8784d675da8553718.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20211214/24ad27afc65853d8784d675da8553718.png" class="img-polaroid" title="23.png" alt="23.png" referrerpolicy="no-referrer"></a>
</div>
<br>
上图是时间策略，即设置好具体的时间节点，在这个时间节点要将应用的实例数扩到几个或者缩到几个。这种策略适合流量高峰期有相对明确时间节点的场景，比如在线教育的客户，通常流量高峰在晚上 8 点开始，11 点逐渐结束，这种情况下，通过定时策略在 7 点半左右把应用的实例数扩起来，然后 11 点之后逐渐把应用实例数缩回正常。<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20211214/12a452b7c7e408fd0d3d8003d72943a4.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20211214/12a452b7c7e408fd0d3d8003d72943a4.png" class="img-polaroid" title="24.png" alt="24.png" referrerpolicy="no-referrer"></a>
</div>
<br>
上图是指标策略，目前提供 CPU 使用率、内存使用率、应用的 QPS 阈值、应用接口平均响应时间（RT）阈值四种指标，这四种指标可以配合使用。当这四种指标其中有一种达到阈值后就会触发扩容，会对应用实例进行逐渐扩容。当指标小于阈值后触发缩容。这种策略适合流量高峰时间不固定的场景，比如市场营销，游戏运营。<br>
<br><strong>3、成本优化</strong><br>
<br>对于弹性能力，大家可能更多的是关注它能让系统快速支撑流量脉冲，增加系统横向扩展的能力。其实因为SAE有极致的弹性能力，再加上<strong>按分钟、按量计费的</strong>模式，对整体的资源成本是有一定优化的。<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20211214/eb8e8207c6537c97af3410d454215f82.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20211214/eb8e8207c6537c97af3410d454215f82.png" class="img-polaroid" title="25.png" alt="25.png" referrerpolicy="no-referrer"></a>
</div>
<br>
<h4>可观测性（Observability）</h4>应用侧的可观测性分两个维度，一是纵向的 Metrics 指标，比如主机的 CPU、内存、磁盘各项指标，Pod 的 CPU、内存各项指标，JVM 的 Full GC、堆内存、非堆内存各项指标。另一个维度是横向的请求调用链路监测，上游服务到下游服务的调用、上游接口到下游接口的调用。<br>
<br>在监控微服务架构时，通常需要从三个角度来看：<br>
<ul><li>应用的整体健康状况。</li><li>应用每个实例的健康状况。</li><li>应用每个接口的健康状况。</li></ul><br>
<br>而 SAE 对应用的监控也都覆盖了上述这两个维度和三个角度。<br>
<br><strong>1、应用整体健康状况</strong><br>
<br>进入应用详情页，点击左侧菜单中的应用监控/应用总览，便可以看到应用的整体状况：<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20211214/7e209192ce63ed396d6c4435b4c9a53c.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20211214/7e209192ce63ed396d6c4435b4c9a53c.png" class="img-polaroid" title="26.png" alt="26.png" referrerpolicy="no-referrer"></a>
</div>
<br>
<ul><li>总请求量：可以一目了然的看到请求量是否明显的异常，比如骤降或者陡升。</li><li>平均响应时间：应用整体接口的平均响应时间，这个指标直接反映最真实的应用健康状况。</li><li>Full GC：JVM 里比较重要的指标，也是会直接影响系统性能的因素。</li><li>慢 SQL：智能抓取执行时间大于 500ms 的 SQL。</li><li>一些曲线视图：帮助我们掌握不同时段的应用情况。</li></ul><br>
<br><strong>2、应用实例节点健康状况</strong><br>
<br>进入应用详情页，点击左侧菜单中的应用监控/应用详情，便可以看到应用每个节点的信息：<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20211214/ec6839c0fff6bb3f1299c487751c7321.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20211214/ec6839c0fff6bb3f1299c487751c7321.png" class="img-polaroid" title="27.png" alt="27.png" referrerpolicy="no-referrer"></a>
</div>
<br>
从上图可以看到，左侧会列出当前应用的所有实例节点，包括该节点的平均响应时间、请求次数、错误数、异常数。如果我们按照影响时间降序排序，比较靠上的节点就是响应时间较慢的节点，然后我们就需要分析是什么原因导致这些节点的响应时间较慢。所以，右侧会提供了一些检查维度来帮助我们分析排查问题。<br>
<br>比如查看 JVM 指标：<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20211214/580ec775014308b50f44b6c82f0b78fe.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20211214/580ec775014308b50f44b6c82f0b78fe.png" class="img-polaroid" title="28.png" alt="28.png" referrerpolicy="no-referrer"></a>
</div>
<br>
<strong>3、应用接口健康状况</strong><br>
<br>进入应用详情页，点击左侧菜单中的应用监控/接口调用，便可以看到应用每个接口的信息：<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20211214/8607d179da62fa6048429b3ec85c7454.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20211214/8607d179da62fa6048429b3ec85c7454.png" class="img-polaroid" title="29.png" alt="29.png" referrerpolicy="no-referrer"></a>
</div>
<br>
接口监控和应用实例节点监控的思路一致，左侧会列出所有请求过的接口，同样显示了响应时间、请求数、错误数，右侧同样提供了一些检查维度来帮助我们分析接口 RT 高的原因。<br>
<br>比如查看 SQL 调用分析：<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20211214/05c8ad70daa1738d4485974aedd1afc9.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20211214/05c8ad70daa1738d4485974aedd1afc9.png" class="img-polaroid" title="30.png" alt="30.png" referrerpolicy="no-referrer"></a>
</div>
<br>
<strong>4、纵向 Metrics 指标</strong><br>
<br>在上述三个角度中，其实已经涵盖了绝大多数 Metrics 指标，比如有应用健康状态的指标、JVM 的指标、SQL 指标、NoSQL 指标等。<br>
<br><strong>5、横向调用链路</strong><br>
<br>在很多时候，我们单纯的看 Metrics 指标是无法确定问题的根本原因的，因为会涉及到不同服务之间的调用，不同接口之间的调用，所以需要查看服务和服务之间、接口和接口之间的调用关系以及具体的代码信息。在这个维度上，SAE 集成的 ARMS 的监控能力便可以实现。我们在应用监控/接口调用/接口快照中可以看到有请求的接口快照，通过 TraceID 便可以查看该接口的整体调用链路：<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20211214/8d528e27d66a1bd4786f0530a524b382.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20211214/8d528e27d66a1bd4786f0530a524b382.png" class="img-polaroid" title="31.png" alt="31.png" referrerpolicy="no-referrer"></a>
</div>
<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20211214/3045f01bc799cb17922e2b999fb9e121.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20211214/3045f01bc799cb17922e2b999fb9e121.png" class="img-polaroid" title="32.png" alt="32.png" referrerpolicy="no-referrer"></a>
</div>
<br>
从上面这个图我们可以看出很多信息：<br>
<ul><li>该接口在服务级别的完整请求链路，比如 ikf（前端）-> ikf-web（Java 服务）-> ikf-blog（Java 服务）-> ikf-blog（Java 服务）。</li><li>每个服务的状态情况，比如状态一列是红点，说明在这个环节是有异常出现的。</li><li>在每个服务中请求的接口名称。</li><li>每个服务的请求耗时。</li></ul><br>
<br>除了上述这些显性的信息以外，还有一些隐性的信息：<br>
<ul><li>上游服务 ikf-web 的总耗时是 2008ms，但下游服务 ikf-blog 的总耗时是 5052ms，而且耗时起点是一样的，说明 ikf-web 到 ikf-blog 是一个异步调用。</li><li>既然 ikf-web 到 ikf-blog 是异步调用，然而 ikf-web 的耗时有 2s 之多，说明 ikf-web 服务中的接口也有问题。</li><li>在 ikf-blog 服务中，又有内部接口被调用，因为从调用链上出现了两个 ikf-blog，并且这个内部调用是同步调用，而且问题出现在最后一个接口调用上。</li></ul><br>
<br>从以上这些信息可以帮我们缩小和圈定问题根因出现在哪个环节的范围，然后我们可以点击方法栈一列的放大镜，查看具体的方法栈代码信息：<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20211214/15855d094fae3095d0cb81153b4eab9d.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20211214/15855d094fae3095d0cb81153b4eab9d.png" class="img-polaroid" title="33.png" alt="33.png" referrerpolicy="no-referrer"></a>
</div>
<br>
从方法栈这里我们又可以得到很多显性信息：<br>
<ul><li>具体的方法。</li><li>每个方法的耗时。</li><li>方法产生的具体异常信息。</li><li>数据库操作的具体 SQL 语句，甚至 SQL 上的 Binding Value。</li></ul><br>
<br>当然除了显性信息外，还有一个比较重要的隐性信息，比如我们可以看到<code class="prettyprint">BlogController.findBlogByIsSelection(int isSelection)</code>这个方法的耗时是 5s，但是该方法内部的数据库操作的耗时很少，只有 1ms，说明耗时是属于业务代码的，毕竟业务代码我们是抓不到也不会去抓取信息的。这时我们可以有两种方式去定位具体问题：<br>
<ul><li>从方法栈信息中已经知道了具体的服务和具体的方法，那么直接打开 IDE 查看、分析代码。</li><li>查看方法栈页签旁边的线程剖析，也基本可以确定问题所在。比如上图这个情况，我们查看线程剖析后会发现他的耗时是因为<code class="prettyprint">java.lang.Thread.sleep( ):-2 [3000ms]</code>。</li></ul><br>
<br><div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20211214/9f62c78d56eff30a685a83fd89b3225c.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20211214/9f62c78d56eff30a685a83fd89b3225c.png" class="img-polaroid" title="34.png" alt="34.png" referrerpolicy="no-referrer"></a>
</div>
<br>
<h4>韧性能力（Resilience）</h4>对于云原生架构的韧性能力，我会从<strong>优雅上下线、多AZ部署、限流降级</strong>三个方面来聊一聊。<br>
<br><strong>1、优雅上下线</strong><br>
<br>一个好的产品，要能快速应对用户对产品功能、能力具有普适性的反馈和意见，能快速响应市场需求的变化。那么产品的功能就需要快速的做迭代和优化，从 IT 层面来看，就是要有快速、高效、高质量的发布变更流程，能够随时进行生产环境的服务发布。<br>
<br>但是这会带来一个核心问题，即频繁的服务发布，并且不能影响用户体验，用户的请求不能断流。所以这就要求我们的系统部署架构中有优雅上下线的能力。<br>
<br>以微服务架构来说明，虽然开源的产品有能力和方案做到近似优雅上下线，但也是近似做到，当发布服务节点较多的情况下依然会有断流的情况。所以开源方案有诸多问题：<br>
<ul><li>注册中心不可靠、通知不及时。</li><li>客户端轮训不实时、客户端缓存。</li><li>自定义镜像非1号进程，Sigterm 信号无法传递。</li><li>无默认优雅下线方案，需要添加 actuator 组建。</li></ul><br>
<br>在无服务化/服务配置中心章节中，我阐述了 SAE 自带的服务中心和 MSE 的服务中心，无论使用那种方案，我们都对优雅上下线做了进一步的优化。<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20211214/61c6b3ed4756f4371b475df249e56689.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20211214/61c6b3ed4756f4371b475df249e56689.png" class="img-polaroid" title="35.png" alt="35.png" referrerpolicy="no-referrer"></a>
</div>
<br>
从上图可以看到，部署在 SAE 的应用具有主动通知服务中心和服务消费者的能力，再结合 Liveness 应用实例探活和 Readiness 应用业务探活的机制，能让我们的服务在进行部署和因为其他原因挂掉时不会影响用户的正常访问。<br>
<br><strong>2、多 AZ 部署</strong><br>
<br>本着鸡蛋不能放在一个篮子里的原则，一个应用的多个节点，应该分布在不同的可用区，这样整体应用的高可用和健壮性才是足够好的。SAE 支持设置多个交换机（VSwitch），每个交换机可以在不同的可用区，这样在部署、扩容应用的节点时会随机从可选的可用区拉起实例：<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20211214/bee384b9644d9f9b029244d94e6cd95c.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20211214/bee384b9644d9f9b029244d94e6cd95c.png" class="img-polaroid" title="36.png" alt="36.png" referrerpolicy="no-referrer"></a>
</div>
<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20211214/3523be9e48d5ef8f400b03e042340941.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20211214/3523be9e48d5ef8f400b03e042340941.png" class="img-polaroid" title="37.png" alt="37.png" referrerpolicy="no-referrer"></a>
</div>
<br>
这就避免了当某个可用区出现问题挂掉时，整体系统因为在一个可用区而挂掉，这也是最基本的同城多活的实践。<br>
<br><strong>3、限流降级</strong><br>
<br>限流降级是系统断臂求生的能力，在遇到突发的流量脉冲时，可以及时限制流量，避免整个系统被击穿，或者当流量超出预期时，及时切断非核心业务，释放资源来支撑核心业务。<br>
<br>目前对于 Java 应用，SAE 也支持限流降级的能力，首先对应用的所有接口的请求指标进行抓取和监控：<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20211214/40ef8e2256af6e57326ec750947a80e1.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20211214/40ef8e2256af6e57326ec750947a80e1.png" class="img-polaroid" title="38.png" alt="38.png" referrerpolicy="no-referrer"></a>
</div>
<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20211214/37179bf327fe576f3def62ac9d0d680d.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20211214/37179bf327fe576f3def62ac9d0d680d.png" class="img-polaroid" title="39.png" alt="39.png" referrerpolicy="no-referrer"></a>
</div>
<br>
然后我们可以针对每一个接口设置流控、隔离、熔断的规则，比如我对 /checkHealth 接口设置一条流控规则：<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20211214/0b7528b56e36644cc33a711005c30f90.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20211214/0b7528b56e36644cc33a711005c30f90.png" class="img-polaroid" title="40.png" alt="40.png" referrerpolicy="no-referrer"></a>
</div>
<br>
当该接口的 QPS 达到 50 后，单个机器超过 50 的请求将快速失败。比如我们对一个有 6 个节点的应用进行压测时，可以看到每个节点的 QPS 情况：<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20211214/42b2201dd100756e7d962ce959c3af12.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20211214/42b2201dd100756e7d962ce959c3af12.png" class="img-polaroid" title="41.png" alt="41.png" referrerpolicy="no-referrer"></a>
</div>
<br>
当开启流控规则后，可以立即看到限流的效果：<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20211214/5e2b174faec09dcd3031c5890a396ce3.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20211214/5e2b174faec09dcd3031c5890a396ce3.png" class="img-polaroid" title="42.png" alt="42.png" referrerpolicy="no-referrer"></a>
</div>
<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20211214/a5f91cbb22c18335248254948fd90ccd.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20211214/a5f91cbb22c18335248254948fd90ccd.png" class="img-polaroid" title="43.png" alt="43.png" referrerpolicy="no-referrer"></a>
</div>
<br>
可以看到 QPS 被精准的控制到 50，超过 50 的请求直接返回失败。<br>
<h4>自动化能力（Automation）</h4>在自动化能力方面，我主要从 CICD 流程这个维度来聊一聊。大家从上面章节的截图可以看到，有很多是 SAE 控制台的截图，在实际应用中肯定不会通过控制台来一个一个发布应用，必然都是通过 CICD 流程来做自动化的应用打包和发布流程。<br>
<br>SAE 在这个方面提供两种实现<strong>自动化运维</strong>的方式。<br>
<br><strong>1、基于 GitLab 和 Jenkins</strong><br>
<br>目前很多企业的 CICD 流程都是基于 GitLab 和 Jenkins 来做的，那么 SAE 也支持将发布的操作集成到这种方案里。这个方案的核心是 SAE 会提供一个 Maven 插件，同时对应有三个配置文件，Maven 插件通过这三个配置文件中的信息将打包好的 Jar/War 或者镜像发布到对应的 SAE 应用中。<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20211214/869edd5b3cbc41feaafc2921bb7352bd.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20211214/869edd5b3cbc41feaafc2921bb7352bd.png" class="img-polaroid" title="44.png" alt="44.png" referrerpolicy="no-referrer"></a>
</div>
<br>
<ul><li>toolkit_profile.yaml：配置 RegionID、AccessKey ID、AccessKey Secret。</li><li>toolkit_package.yaml：配置比如应用部署包类型、部署包地址、镜像地址。</li><li>toolkit_deploy.yaml：配置比如 SAE 应用的 ID、应用所属命名空间 ID、应用名称、发布方式等。</li></ul><br>
<br>更详细的配置信息可以参阅该文档。<br>
<br>然后在 Jenkins 的任务中，对 Maven 设置如下的命令即可：<br>
<pre class="prettyprint">clean package toolkit:deploy -Dtoolkit_profile=toolkit_profile.yaml -Dtoolkit_package=toolkit_package.yaml -Dtoolkit_deploy=toolkit_deploy.yaml <br>
</pre><br>
这样就可以很容易的将 SAE 的部署流程集成到基于 Gitlab 和 Jenkins 的 CICD 方案里了。<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20211214/49e4b7adbdb44b8807d6e368c99b8788.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20211214/49e4b7adbdb44b8807d6e368c99b8788.png" class="img-polaroid" title="45.png" alt="45.png" referrerpolicy="no-referrer"></a>
</div>
<br>
<strong>2、基于 Open API</strong><br>
<br>还有一些企业会自己研发运维平台，运维赋能研发，由研发同学在运维平台上进行运维操作。面对这种场景，SAE 提供了丰富的 Open API，可以将 SAE 控制台上 90% 的能力通过 Open API 集成到客户自己的运维平台中。详细的 OpenAPI 说明可以参与该文档。<br>
<h3>总结</h3>基于 SAE 武装过系统后，整体的部署架构会变成这样：<br><br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20211214/f2502173155cc95fc961053067ff0cb3.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20211214/f2502173155cc95fc961053067ff0cb3.png" class="img-polaroid" title="46.png" alt="46.png" referrerpolicy="no-referrer"></a>
</div>
<br>
云原生架构成熟度模型（SESORA）在我阐述的这五个维度一共是 15 分，基于 SAE 的云原生架构在这五个维度会达到 12 分：<br>
<ul><li>无服务化：3分</li><li>弹性能力：3分</li><li>可观测性：2分</li><li>韧性能力：2分</li><li>自动化能力：2分</li></ul><br>
<br>原文链接：<a href="https://mp.weixin.qq.com/s/zOlQ07dCLRy_cHTTai6V1g" rel="nofollow" target="_blank">https://mp.weixin.qq.com/s/zOlQ07dCLRy_cHTTai6V1g</a>
                                                                <div class="aw-upload-img-list">
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                </div>
                                
                                                                <ul class="aw-upload-file-list">
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    </ul>
                                                              
</div>
            