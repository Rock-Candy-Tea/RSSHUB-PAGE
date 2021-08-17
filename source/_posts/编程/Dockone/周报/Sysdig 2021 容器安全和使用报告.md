
---
title: 'Sysdig 2021 容器安全和使用报告'
categories: 
 - 编程
 - Dockone
 - 周报
headimg: 'https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210814/f16d16d3fe08d5aa7c397c38d00f88d1.png'
author: Dockone
comments: false
date: 2021-08-17 10:08:07
thumbnail: 'https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210814/f16d16d3fe08d5aa7c397c38d00f88d1.png'
---

<div>   
<br>在过去的四年中，我们实时地对客户真实数据进行分析，对容器有了更深入的了解。随着我们安全和监控能力的提高，我们独特的优势使我们能明晰企业处理安全性和合规性的细节，随着时间的推移，我们对如何使用基础设施、应用和容器有了更多的了解，对此，我们为您带来了Sysdig 2021年容器安全和使用报告。<br>
<br>我们的企业客户用数据告诉我们，容器普遍寿命较短，对于容器环境安全性和合规性的问题研究是很重要的。今年的调研结果与去年的报告一致，大约有一半的容器寿命在5分钟以内。报告突出显示了用于故障响应、故障定位和故障解决的详细记录。对此，我们对容器安全状况进行了更深入的研究，以明确我们的客户面临的挑战。在我们的分析报告中显示出对于部分公司，“向左移”的趋势触及了Kubernetes的安全性，四分之三的团队在CI/CD流程中将扫描容器镜像阶段放在部署之前。<br>
<br>尽管许多团队对识别漏洞有很强的意识，但他们错误的配置为攻击者敞开了大门。事实上，报告显示，大多数容器镜像配置过于随意，其中58%的容器使用root权限运行，这伴有严重的安全隐患。随着容器环境的完善，团队意识到只扫描镜像是不满足安全要求的。它们还需要确保容器运行时的安全性以应对持续的威胁。作为处理这些问题的一种方式，我们看到了Cloud Native Computing Foundation（CNCF）Falco项目的飞速增长，以帮助团队在容器运行时、主机和Kubernetes环境中检测威胁。<br>
<br>虽然Kubernetes在容器编排方面的使用方式在2020年没有改动，但在容器运行时的工具选型中有了明显转变，各个团队从Docker转向了containd和CRI-O，事实上，Kubernetes项目官方宣布将在2021年末正式弃用Docker。随着今年容器密度的再次增长，团队正在转向使用Prometheus作为监测这些环境的标准方法 。<br>
<br>根据GitHub的统计数据，在我们的客户中使用Prometheus指标的占比相较于去年增长了35%，Exporters 排名前三的是：node-exporter，blackbox-exporter和jmx-exporter。Quay仓库今年得到了更多的使用，云原生开发人员首选的编程语言Golang，也在团队中得到了更多的使用。<br>
<br>这份报告中的数据来自于我们对一个客户子公司每天运行着数百万个容器的分析，以及我们的客户在过去一年中运行的近10亿个不同容器数据。在此报告中，您将发现关于安全性、合规性、服务、告警和Kubernetes使用模式的更多细节。这些信息将对于来自全世界各行各业的公司掌握容器环境的真实安全状态和使用情况非常有用。<br>
<h3>2021 趋势关键字</h3><div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210814/f16d16d3fe08d5aa7c397c38d00f88d1.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210814/f16d16d3fe08d5aa7c397c38d00f88d1.png" class="img-polaroid" title="1.png" alt="1.png" referrerpolicy="no-referrer"></a>
</div>
<br>
<h3>统计数据和数据来源</h3>该报告中的数据来自于对近200万个容器的分析，这还是我们的客 户每天运行容器的一部分。<br>
<br>我们又从GitHub、Docker Hub和CNCF等公共数据源中提取容器 数据。这些数据来自于全球各行各业的容器使用情况，团队的规模 从中型企业到大型企业不等。<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210814/0d062f00cfd2b855fdfec5d98bb8b1c6.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210814/0d062f00cfd2b855fdfec5d98bb8b1c6.png" class="img-polaroid" title="2.png" alt="2.png" referrerpolicy="no-referrer"></a>
</div>
<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210814/b2a88d3d0954d9655e26fc85676505dc.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210814/b2a88d3d0954d9655e26fc85676505dc.png" class="img-polaroid" title="3.png" alt="3.png" referrerpolicy="no-referrer"></a>
</div>
<br>
<h3>使用哪些容器运行时部署？</h3><h4>Container runtime</h4>在过去的一年里，我们看到containerd和CRI-O的使用率有了显著增长(相比去年上升了18%和4%)，而Docker相比于去年的79%下降到今年的50%。值得注意的是，Kubernetes项目官方宣布将在2021年底正式弃用Docker。确切地说，containerd是Docker公司过去一直在使用的底层工具。Docker引擎先前已经具备了高级运行时和低级运行时的特性。它们现在被分解成独立的containerd和runc项目。然而更多的工具选型也会让用户选择时更纠结。<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210814/39bceb0273ef45ae4f80460b9578b3d8.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210814/39bceb0273ef45ae4f80460b9578b3d8.png" class="img-polaroid" title="4.png" alt="4.png" referrerpolicy="no-referrer"></a>
</div>
<br>
不同的解决方案都期望这些工具在减少资源开销、更强的稳定性、可扩展性和容器镜像仓库兼容性等方面做的更好。然而，由于现在有了开放标准，对于那些做出错误选择并且只能使用某个工具的担忧已经不复存在了。为了使得用户在进行工具选型时更加简单，像OpenShift、GKE和IKS这样的主流平台，通常支持选择容器运行时并使用多种类型的容器运行时并发执行任务，这样就不需要花费太多时间决定使用哪个容器运行时了。<br>
<h4>容器编排平台</h4>相比于其他平台，Kubernetes一直处于领导地位，仅仅比去年有轻微的变化。下面图表中展示了当前主流平台的分类占比，令人惊奇的是，与去年相比，Swarm和Mesos的占比大致相同，分别为2.5%和1.3%。<br>
<br>OpenShift的增幅最大，从9%上升到15%，越来越多的用户似乎依赖于OpenShift，因为它能够在混合云中运行。Docker Compose仅用于在单个主机上管理多个容器，尽管它不被认为能像Kubernetes那样管理多种主机环境，但今年已经添加了这部分功能。<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210814/11acbcf5a7c29e36f8f77ef8dd2867ec.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210814/11acbcf5a7c29e36f8f77ef8dd2867ec.png" class="img-polaroid" title="5.png" alt="5.png" referrerpolicy="no-referrer"></a>
</div>
<br>
<h3>安全性和合规性</h3>随着团队将容器工作负载转移到生产环境中，他们意识到需要将安全性和合规性集成到DevOps工作流程中。“左移安全”已经成为一个热门词汇，它通常指扫描容器漏洞。因为大多数从公共镜像仓库拉取的容器镜像，扫描失败率较高，所以扫描镜像是十分重要的。这些数据也强调了合规检查和严格运行时策略的必要性，需要借此降低风险。为了深入了解Kubernetes和云原生环境中的安全性和合规性状态，我们分析了包括漏洞扫描、运行时安全性和合规性在内的数据。<br>
<h4>镜像扫描</h4>无论容器镜像的来自哪里，在部署到生产环境之前，执行镜像扫描并识别已知漏洞是非常重要的。为了量化漏洞风险的范围，我们对7天内扫描的镜像进行了采样。超过一半的镜像失败了，这意味着它们可能存在严重程度较高或更高的已知漏洞。<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210814/05b8090a13f563b909f552422e1a58c2.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210814/05b8090a13f563b909f552422e1a58c2.png" class="img-polaroid" title="6.png" alt="6.png" referrerpolicy="no-referrer"></a>
</div>
<br>
<strong>操作系统漏洞</strong><br>
<br>我们注意到4%的操作系统漏洞是高危或严重的。虽然看起来概率很低，但如果一个操作系统漏洞被利用，它可能会损害整个镜像并导致应用程序崩溃。这也是为什么对操作系统漏洞的扫描非常关注的原因，特别是那些提供一部分镜像扫描功能的仓库（即ECR、GCR等）。<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210814/e6ef7cf9118620fe4a0b2df25b2cf3c5.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210814/e6ef7cf9118620fe4a0b2df25b2cf3c5.png" class="img-polaroid" title="7.png" alt="7.png" referrerpolicy="no-referrer"></a>
</div>
<br>
<strong>非操作系统漏洞</strong><br>
<br>很多团队并没有检查第三方库中的漏洞。我们发现53%的非操作系统软件包具有高危或极其严重的漏洞。开发人员可能会在不知情的情况下从这些非操作系统开源包（如Python PIP、Ruby Gem等）中引入漏洞，并引入安全风险。<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210814/ff3c170b2ca1f7d7a31bab36ed08d1e8.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210814/ff3c170b2ca1f7d7a31bab36ed08d1e8.png" class="img-polaroid" title="8.png" alt="8.png" referrerpolicy="no-referrer"></a>
</div>
<br>
<strong>在构建阶段扫描镜像</strong><br>
<br>DevOps团队开始思考在开发生命周期早期阶段扫描镜像的重要性，因为在这些所有问题中安全是最重要的一环，带着这个思考，他们正在“向左移动”。在我们的部分分析报告中，我们查看了在CI/CD流水线中构建阶段扫描镜像以及那些没有在构建阶段扫描镜像的企业数量。74%的客户实际上在部署前扫描。这种信号实际上是一个好消息，因为在构建阶段扫描可以帮助团队在将镜像投入生产之前解决潜在的安全问题。<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210814/6f03aed230fa558bd7e9dbf335d6a3a7.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210814/6f03aed230fa558bd7e9dbf335d6a3a7.png" class="img-polaroid" title="9.png" alt="9.png" referrerpolicy="no-referrer"></a>
</div>
<br>
<strong>在哪里扫描：内嵌扫描 vs. 后台扫描</strong><br>
<br>用户可以有两种方法来扫描镜像：<br>
<ul><li>后台扫描-当使用后台扫描时（即直接在UI中或通过使用sdc-cli集成相关工具），Sysdig后台将从镜像仓库提取整个镜像，并执行镜像分析（提取镜像元数据，如安装的软件包、版本、文件属性、Dockerfile指令）和评估（检测OS/非OS漏洞、错误配置和错误的安全实践）。许多团队利用后台扫描。虽然内嵌扫描提供了更好的安全性，但是后台扫描的步骤更靠前。</li><li>内嵌扫描-当使用内嵌扫描时，镜像分析阶段直接在CI/CD流水线、镜像仓库或容器运行时进行。扫描结果元数据被发送到Sysdig后台进行评估，评估结果将被发送回工作人员（评估报告为PDF或JSON格式）。您将对镜像数据有充分的了解，而无需共享镜像或对外公开镜像仓库凭据。扫描结果可以在Sysdig中直接看到。</li></ul><br>
<br><div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210814/2a9ea15840124c82920c664a109d87d7.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210814/2a9ea15840124c82920c664a109d87d7.png" class="img-polaroid" title="10.png" alt="10.png" referrerpolicy="no-referrer"></a>
</div>
<br>
<strong>私有和托管镜像仓库</strong><br>
<br>镜像仓库为托管和管理容器镜像提供存储库。在我们34%的客户中经常使用Docker仓库。它提供包括私有托管库和公共存储库。由云提供商托管的镜像仓库解决方案越来越受欢迎。和过去几年一样，谷歌云镜像仓库再次成为排名第一的公有云存储库，在我们客户中有26%的团队使用它。不过，Quay较去年也有所增长，从14%增长到了24%。<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210814/62d394f5bc4ad2d84af5b55c472bc252.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210814/62d394f5bc4ad2d84af5b55c472bc252.png" class="img-polaroid" title="11.png" alt="11.png" referrerpolicy="no-referrer"></a>
</div>
<br>
在这些不同的产品中，我们调查了从公共镜像仓库和私有镜像仓库中拉取镜像的占比。我们发现大家对公共镜像资源的信任程度越来越强，从去年的40%上升到今年的47%。使用来自公共镜像仓库的镜像会有很大的风险，因为大家很少会验证或检查安全漏洞。然而，随着越来越多的公司在Kubernetes环境中改进他们的安全程序和流程，使用公共镜像仓库的便利性可能掩盖了风险。我们的客户正在创建策略来定义哪些容器镜像仓库被批准在他们的团队中使用。<br><br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210814/103c4a30f1218b286a44fb47d68c89aa.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210814/103c4a30f1218b286a44fb47d68c89aa.png" class="img-polaroid" title="12.png" alt="12.png" referrerpolicy="no-referrer"></a>
</div>
<br>
<h3>容器运行时的威胁</h3>一旦在容器生命周期的构建阶段解决了已知的漏洞，团队则需要设置策略以检测异常行为并及时触发安全警报。Kubernetes运行时的安全是一些组织正在着手解决的问题。由Sysdig贡献的CNCF开源项目Falco正在迅速获得关注和推进力，如下图所示。该项目目前在DockerHub拥有超过2000万的拉取数量，比去年的252%增长了300%。Falco支持定义运行时策略以检测安全问题并生成告警通知。<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210814/eaaaea15723dacf387229d263a535052.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210814/eaaaea15723dacf387229d263a535052.png" class="img-polaroid" title="13.png" alt="13.png" referrerpolicy="no-referrer"></a>
</div>
<br>
<strong>使用管理员权限运行容器</strong><br>
<br>虽然团队清楚必须扫描漏洞，但可能不会扫描常见的配置错误。我们所看到58%的镜像以root权限运行，这将允许专属特权容器可以被破坏。有些容器应该以root权限运行(例如，安全和系统守护进程)，但这只是整个容器的一小部分。从我们与客户的沟通来看，在实践中，即使在容器运行时检测到有风险的配置，团队为了快速部署不会停止容器。取而代之的是他们会在一个宽限期内继续运行，然后再考虑补救步骤。<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210814/93b848682240175475caa773c4d1ef93.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210814/93b848682240175475caa773c4d1ef93.png" class="img-polaroid" title="14.png" alt="14.png" referrerpolicy="no-referrer"></a>
</div>
<br>
<h3>容器运行时违规策略排行</h3>我们通过客户报告的警报数量来衡量策略违规情况。这份报告也表明了用户经常未覆盖容器运行时安全风险的类型。在今年我们看到了可疑文件系统和可疑容器违规问题数量的上升。<br>
<br>在SysdigSecure中默认启用的Falco安全策略可以检测到每一项违规。在下面我们按出现频率列出了前7个违规事项，并对每个违规事项进行了描述以诠释可能存在的威胁。<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210814/546ecebdcd8648435454950729b1adb6.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210814/546ecebdcd8648435454950729b1adb6.png" class="img-polaroid" title="15.png" alt="15.png" referrerpolicy="no-referrer"></a>
</div>
<br>
<h3>合规性</h3>包括PCI-DSS、HIPAA和GDPR在内的一些企业都有许多平台治理和策略合规性的需求，他们便开始采取行动以践行最佳实践。Sysdig平台也在一系列的最佳实践中去使用相关规范来监控集群、监控主机、容器和环境等。这些规范包括互联网安全中心(CIS)标准测试规范、Kubernetes的CIS标准测试规范和Docker的CIS标准测试规范。我们从CIS标准测试规范的80多个规则中选取了一个样本，以表明Sysdig用户对这些最佳实践的遵从情况。这八个基准测试将评估每个主机上容器镜像的配置问题，这些配置问题可能与容器权限、使用的安全工具和可能使组织暴露于风险的某些配置有关。本次测试内容是每个宿主机上的所有容器测试失败的情况和没有按照推荐的最佳实践去降低风险的情况。在这种测试方法下，分数的确是最好的量化方式，我们获取了这八次容器检查中每一次测试分数的中位数。<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210814/bd8d8a04f6ff49150e127e85878aa136.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210814/bd8d8a04f6ff49150e127e85878aa136.png" class="img-polaroid" title="16.png" alt="16.png" referrerpolicy="no-referrer"></a>
</div>
<br>
<h3>客户正在运行哪些服务？</h3><h4>在容器中运行的十大开源解决方案</h4>开源改变了企业在云计算领域的面貌。它不仅推动了基础设施的创新，也推动了应用研发的创新。Sysdig能够自动发现容器内的进程，这让我们能够即时了解客户在生产中，运行云原生服务的解决方案。以下是Sysdig客户部署的十大开源技术：<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210814/230bacaa77fd00696427229fcc9039c6.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210814/230bacaa77fd00696427229fcc9039c6.png" class="img-polaroid" title="17.png" alt="17.png" referrerpolicy="no-referrer"></a>
</div>
<br>
2021年的榜单包括了各种各样的服务——每一种服务都对应用程序的功能至关重要，包括：<br>
<ul><li>HTTP服务器和反向代理解决方案——Nginx</li><li>NoSQL，关系和内存数据库解决方案——MongoDB，Postgres和Redis</li><li>日志和数据分析——Elasticsearch</li><li>编程语言和框架——node. js，Go，Java/JVMs</li><li>消息队列代理软件——RabbitMQ</li></ul><br>
<br>开源社区中可供选择的范围尽管很广，但在我们记录列表中的服务在过去三年中保持了惊人的一致。我们有意省略了Kubernetes组件，如etcd、fluentd以及Falco。由于这些都是默认部署的，所以对于每个Kubernetes用户来说，它们都位于列表的顶部。去年，Node.js和Go（又名Golang）的使用量都超过了Java。今年，Go的使用率从14%飙升至66%，增长了470%。由谷歌工程师创建的Go语言正在迅速成为开发云原生应用程序的首选语言。列表中前10的解决方案是用户普遍部署的可信服务。如果您正在市场上寻找类似的服务，那么您应该充分利用这些开源解决方案。<br>
<h4>自定义指标</h4>自定义指标解决方案为开发人员和DevOps团队提供了一种方法来收集独一无二的数据。这种方法已经成为在生产环境中监控应用程序的主流方法。三个主要解决方案是JMX、StatsD和Prometheus，其中Prometheus连续第二年获得了胜利。<br>
<br>与去年同期相比，我们的客户使用Prometheus指标的比例上升到了62%，而去年为46%。随着新编程框架的广泛使用，JMX指标（用于Java应用程序）和StatsD等替代指标继续下降，同比分别下降了35%和15%。<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210814/8adc5aa1b0a8265ed53881c095e48ee9.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210814/8adc5aa1b0a8265ed53881c095e48ee9.png" class="img-polaroid" title="18.png" alt="18.png" referrerpolicy="no-referrer"></a>
</div>
<br>
<h4>Prometheus exporters 排名</h4>作为CNCF最成功的开源项目之一，Prometheus已经成为云原生服务监控的代名词。它现在被Kubernetes、OpenShift和Istio等项目作为监控指标广泛使用。此外，越来越多的“exporters”可以为大量的第三方解决方案提供详细的数据指标。在Sysdig为大规模环境提供完全兼容Prometheus的情况下，我们预计Prometheus的受欢迎程度将在我们的客户基础中持续增长。<br>
<br>对于当前的排名情况，我们查看了在prometheus.io上列出的每个GitHub项目。并统计了每个项目的问题、星标数和forks的数量，并将结果与Dockerhub或其他仓库拉取数量相关联。<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210814/177098d09027330488eef5670c48854f.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210814/177098d09027330488eef5670c48854f.png" class="img-polaroid" title="19.png" alt="19.png" referrerpolicy="no-referrer"></a>
</div>
<br>
<h3>容器</h3>每年，我们都要详细统计一下容器的数量和活动，还包括容器的密度和寿命。通过对容器的采样和研究，也验证了企业正在实现的规模和效率。<br>
<h4>在每个团队中容器的运行数量</h4>为了解企业当前的规模，我们调研了每个客户在其基础设施上运行的容器数量。超过一半的客户使用250个或更少的容器。在高端市场，只有4%的客户管理着超过5000个容器。大多数客户是从小规模开始慢慢累积的，也有一些是开发人员为推动容器化加速软件交付主动增加了规模。据DevOps和云计算团队报告称，一旦容器的优势得到证明，越来越多的业务部门会关注新的平台，这些平台普及的速度将会加快。然而，企业应该应该考虑运行容器的原始数量，以及这些容器的大小（见下图）。<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210814/9835b8d6f8e9fab2e9c7cf68e206a884.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210814/9835b8d6f8e9fab2e9c7cf68e206a884.png" class="img-polaroid" title="20.png" alt="20.png" referrerpolicy="no-referrer"></a>
</div>
<br>
<h4>镜像到底有多大？</h4>尽管镜像的大小取决于应用程序，但根据我们的数据，镜像的平均值是376 MB。较大的10GB 镜像是一个极端值，除非有使用该镜像的场景，否则使用较大的镜像并不是最佳实践。大型镜像不仅需要更长的部署时间，还会降低发布速度，更可能会暴露更多的漏洞。<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210814/9cca17ece076b5b2210b614295ca17fd.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210814/9cca17ece076b5b2210b614295ca17fd.png" class="img-polaroid" title="21.png" alt="21.png" referrerpolicy="no-referrer"></a>
</div>
<br>
<h4>容器密度</h4>每个主机的容器密度增加了33%！<br>
<br>在过去四年中，每一份报告中都显示容器数量中位数有所增加。然而，今年同比增幅仅为33%，而去年的增幅为100%。在将来这个数字可能会继续小幅增加，但这种密度的增加可能会以牺牲整体镜像大小为代价。尽管容器的主要目标是加速开发和部署，但在容器执行效率一定的前提下，许多团队正在提高硬件资源利用率以获取更好的效益。<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210814/00eb7e65f4acbffd72cbe062c5d5a86c.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210814/00eb7e65f4acbffd72cbe062c5d5a86c.png" class="img-polaroid" title="22.png" alt="22.png" referrerpolicy="no-referrer"></a>
</div>
<br>
<h4>容器，镜像和服务的生命周期</h4>在我们2019年的报告中，容器、容器镜像和服务的寿命长短是最受欢迎的数据报告之一。它从开发和容器运行时的角度反映了现代应用程序的活跃状态。<br>
<br><strong>容器寿命短</strong><br>
<br>通过比较容器每年的寿命，我们可以看到相似的数据，大多数容器的寿命都不到一周。事实上，我们最新的数据样本显示，与去年的22%相比，存活10秒的容器数量仍然保持在21%。<br>
<br>许多容器需要在整个生命周期中执行某个功能，功能完成时则终止容器。几秒钟可能看起来很短，但对于某些过程来说，这是必要的。容器的短暂性仍然是该技术的独特优势之一，但会对容器的监控、安全性和合规性方面提出了新的挑战。随着采用Serverless（无服务器架构）云技术的增长，较短寿命的进程和服务可能会从容器移向托管云。但是，这并不代表环境中工作负载总体架构会发生变化。相反，它可以代表寿命较短的工作负载从一种技术到另一种技术的转变。<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210814/05fc66b43e3fc7ed5355344c1fd99dd3.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210814/05fc66b43e3fc7ed5355344c1fd99dd3.png" class="img-polaroid" title="23.png" alt="23.png" referrerpolicy="no-referrer"></a>
</div>
<br>
<strong>Continuous development and image lifespans</strong><br>
<br>容器是敏捷开发的完美伴侣，它通常作为容器化的微服务加速代码开发进程和应用发布进度。据我们调研的镜像生命周期数据显示，代码发布和CI/CD流水线正在帮助开发团队更快的交付，超过一半的容器镜像在一周或更短的时间内被更替或删除。对于大多数企业来说, 进入市场的速度在保持竞争力方面起着至关重要的作用。随着代码频繁地被编译构建部署，这意味着不断产生着新的容器镜像，企业中不断涌现的灵感和想法将迅速转化为真实的容器运行在企业中。<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210814/f4fe65b954613b91dd1c9d3d688934ec.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210814/f4fe65b954613b91dd1c9d3d688934ec.png" class="img-polaroid" title="24.png" alt="24.png" referrerpolicy="no-referrer"></a>
</div>
<br>
<strong>Service lifespan</strong><br>
<br>在关乎寿命这个话题中我们最后检查了有关服务和运行时间的数据。服务是什么呢?它是我们软件的重要组成部分，比如数据库软件、负载平衡器和客户的代码，这些服务可能会不断的优化改进。然而，保持服务24小时运行是十分重要的（至少对大多数7*24 提供服务的企业来说确是如此）。与过去几年不同的是，我们有超过一半的客户服务持续两周或更长时间，今年我们在服务运行时间上看到了更多的变化，尤其是在不到5分钟范围内变化很大。<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210814/8f57e79e638ae274a0acd65fa4bda5c9.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210814/8f57e79e638ae274a0acd65fa4bda5c9.png" class="img-polaroid" title="25.png" alt="25.png" referrerpolicy="no-referrer"></a>
</div>
<br>
<h3>告警</h3>对客户设置的告警类型进行趋势分析，有助于我们了解用户认为对其容器操作最有可能造成破坏的情况。<br>
<h4>The top 10 告警策略</h4>我们的客户使用了800多种独特的告警策略。下图表示最常用的告警策略，以及每种告警的占比。与上次报告相比，这些告警的组成已经发生了变化，大多转向了支持Kubernetes节点可用性，而略微减少了对资源利用率和正常运行时间的关注。<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210814/bfcf1b998da64ad4b4b2e06698c593dd.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210814/bfcf1b998da64ad4b4b2e06698c593dd.png" class="img-polaroid" title="26.png" alt="26.png" referrerpolicy="no-referrer"></a>
</div>
<br>
<h4>告警范围</h4>Sysdig告警支持通过“限定”特定标签或Kubernetes / cloud标签进行定制。例如，使用上文中告警的一个例子，您可以为单个名称空间（如“isio -system”）或该名称空间中的特定Pod名称（如“envoy”）指定memory.used.percent字段。标签在云原生环境中扮演着关键角色，它是为团队提供隔离项目的唯一标识。<br>
<br>在本示例中，标签指定了一组“待观察的资源”。用Kubernetes标签指定告警现在是最常见的做法之一，前五名包括命名空间、集群、Deployment和host。代理标签——部署时附加到Sysdig代理上的元数据——成为了Sysdig用户中最流行的告警范围。<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210814/d18f2df97529e6ce05301a92cb654627.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210814/d18f2df97529e6ce05301a92cb654627.png" class="img-polaroid" title="27.png" alt="27.png" referrerpolicy="no-referrer"></a>
</div>
<br>
在下面的图片中显示了一些我们的客户正在使用的告警范围标签：<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210814/665a123e355685ee9e146920ef271d46.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210814/665a123e355685ee9e146920ef271d46.png" class="img-polaroid" title="28.png" alt="28.png" referrerpolicy="no-referrer"></a>
</div>
<br>
<h4>告警渠道</h4>我们通过专门的通信通道查看了用户的告警信息。发现Slack位居榜首，超过了专用事件响应平台，甚至超过了电子邮件。这些结果更有趣的是与PagerDuty和Opsgenie不同，Slack并不被认为是一个事件响应平台。Slack大多用于处理工作时间内的非关键性警报，而像PagerDuty这样的解决方案被用于关键性警报，提供类似“把人们从床上叫醒”的服务。<br>
<br>今年，我们决定为未配置通知通道的告警添加一个类别。这种情形的出现是因为告警仅仅用于提供相关信息，也可能是因为Sysdig平台本身提供了足够的信息已经满足了告警的需求。<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210814/07871836322cf02dd7ab0630651375e7.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210814/07871836322cf02dd7ab0630651375e7.png" class="img-polaroid" title="29.png" alt="29.png" referrerpolicy="no-referrer"></a>
</div>
<br>
<h3>Kubernetes使用模式</h3>客户正在运行多少个集群？每个节点运行多少Pod？在本节中，我们将回答这些问题以及更多内容。我们从集群维度到ReplicaSets维度调研了关于客户使用Kubernetes做了什么。由于Sysdig可以自动收集Kubernetes标签和元数据，我们能从性能指标、告警到安全事件中为我们发现的所有数据提供上下文。同理，我们可以通过简单的查询，从集群一直捕获到Pod和容器的使用数据。<br><br>
<h4>Kubernetes集群和节点</h4>一些客户维护几个集群，他们的集群大小不一，而另一些客户则拥有许多不同规模的集群。下方的图表提供了Sysdig平台用户的集群数量和每个集群节点的分布。大多数客户只拥有单个集群，并且节点数量相对较少，这表明许多企业仍处于使用Kubernetes的早期阶段。我们还认识到，在公共云中使用托管Kubernetes服务是影响这 些数据点的另一个因素。这些服务提供商如：Amazon Elastic Kubernetes Service（EKS）、谷歌Kubernetes Engine（GKE）、Azure Kubernetes Service（AKS）和IBM Cloud Kubernetes Service（IKS），用户可以根据需求快速启动和删除集群。<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210814/c40431a8bf5ad698e6d2f5252d17edc7.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210814/c40431a8bf5ad698e6d2f5252d17edc7.png" class="img-polaroid" title="30.png" alt="30.png" referrerpolicy="no-referrer"></a>
</div>
<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210814/905714b9f7a44c2e2bf1f5202be6def7.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210814/905714b9f7a44c2e2bf1f5202be6def7.png" class="img-polaroid" title="31.png" alt="31.png" referrerpolicy="no-referrer"></a>
</div>
<br>
<h4>Kubernetes命名空间、Deployments和Pod</h4><strong>每个集群上的命名空间</strong><br>
<br>Kubernetes使用命名空间来帮助多个用户、团队或应用进行资源隔离。Kubernetes有三个初始命名空间：default、kube-system和kubepublic。命名空间的使用方式因人而异，但云原生团队通常为每个应用使用单独的命名空间。<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210814/f34209ee6fe0f2a7ef7836306ae8a352.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210814/f34209ee6fe0f2a7ef7836306ae8a352.png" class="img-polaroid" title="32.png" alt="32.png" referrerpolicy="no-referrer"></a>
</div>
<br>
<strong>每个命名空间下的Deployments</strong><br>
<br>Deployments描述了Pods和ReplicasSets所需的状态，并有助于确保应用的一个或多个实例来正常应对用户请求。Deployments包含一组多个相同的Pod，它没有唯一的身份定义，比如Nginx、Redis或Tomcat都可以是Deployments。每个命名空间下的Deployments构成了用户微服务应用。<br>
<br>我们看到今年出现了轻微的变化，每个命名空间的Deployments数量减少了。通过命名空间对环境进行访问是简单有效的，因此，在每个命名空间中Deployments数量越少，越可以为团队更好地分工，让他们只能访问自己负责的应用。<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210814/4f40d1dfe0b2052226ca9fd8409be836.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210814/4f40d1dfe0b2052226ca9fd8409be836.png" class="img-polaroid" title="33.png" alt="33.png" referrerpolicy="no-referrer"></a>
</div>
<br>
<strong>每个集群中od 的数量</strong><br>
<br>Pod是Kubernetes中最小的可操作对象。它们包含一个或多个具有共享存储和网络的容器，以及如何运行这些容器的定义。<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210814/8d4dcf61e299e948d00c873d036cfb12.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210814/8d4dcf61e299e948d00c873d036cfb12.png" class="img-polaroid" title="34.png" alt="34.png" referrerpolicy="no-referrer"></a>
</div>
<br>
**每个节点中Pod的数量<br>
<br>每个Pod的整个生命周期都在将节点上完成，有时会因为节点资源不足或节点故障被驱逐至其他节点。<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210814/b007706154b6111473677f0b8c9bb257.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210814/b007706154b6111473677f0b8c9bb257.png" class="img-polaroid" title="35.png" alt="35.png" referrerpolicy="no-referrer"></a>
</div>
<br>
<h3>统计数据和数据来源</h3>该报告中的数据来自于对近200万个容器的分析，这还是我们的客户每天运行容器的一部分。<br>
<br>我们又从GitHub、Docker Hub和CNCF等公共数据源中提取容器数据。这些数据来自于全球各行各业的容器使用情况，团队的规模从中型企业到大型企业不等。<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210814/d33acd2f0db1984dbb14a2ecba7d3a3a.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210814/d33acd2f0db1984dbb14a2ecba7d3a3a.png" class="img-polaroid" title="36.png" alt="36.png" referrerpolicy="no-referrer"></a>
</div>
<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210814/526e1c8fa8ecc1cb6b33ebe754f7abd8.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210814/526e1c8fa8ecc1cb6b33ebe754f7abd8.png" class="img-polaroid" title="37.png" alt="37.png" referrerpolicy="no-referrer"></a>
</div>
<br>
<h3>结论</h3>容器技术在应用交付中的作用日益显著。随着DevOps团队对Kubernetes关注度的提高，我们非常欣喜地看到团队在构建过程中贯彻和落实安全规范。但是，仍需要更多的保障来确保容器的安全，以防止可能出现的漏洞进入生产。在我们第四份年度报告中突出表明了容器环境趋势的持续增长，和对开源解决方案依赖的增强：<br>
<ul><li>各个团队在Kubernetes环境中不断“向左移动”，通过在构建阶段利用内嵌扫描来扫描镜像，漏洞也不断地增多，仍需要有保障的安全工具来识别、审计和验证合规性。</li><li>尽管Kubernetes仍然是容器编排的最佳选择，但容器运行时的选择也在随着containd和CRI-O的快速增长而变化。随着容器密度的增加，团队应该在Kubernetes-native工具中多做贡献来简化大规模的操作。</li><li>一些开源的产品正在成为Kubernetes环境中的核心组件。Falco、Prometheus和Go的发展表明了人们对高质量开源解决方案的渴望，希望以此帮我们解决对于生命周期较短的容器安全和监控问题。</li></ul><br>
<br>原文链接：<br>
<ul><li><a href="https://mp.weixin.qq.com/s/KVJg8Mk6PUk2G_AGyg1qFQ" rel="nofollow" target="_blank">https://mp.weixin.qq.com/s/KVJg8Mk6PUk2G_AGyg1qFQ</a></li><li><a href="https://mp.weixin.qq.com/s/KC4BqUffmItfhZGPL3HgSw" rel="nofollow" target="_blank">https://mp.weixin.qq.com/s/KC4BqUffmItfhZGPL3HgSw</a></li></ul>
                                                                <div class="aw-upload-img-list">
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                </div>
                                
                                                                <ul class="aw-upload-file-list">
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            </ul>
                                                              
</div>
            