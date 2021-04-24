
---
title: '没人想要再管理 Kubernetes 了 ！'
categories: 
 - 编程
 - Dockone
 - 周报
headimg: 'https://picsum.photos/400/300?random=9706'
author: Dockone
comments: false
date: 2021-04-24 04:09:56
thumbnail: 'https://picsum.photos/400/300?random=9706'
---

<div>   
<br>市面上有众多成熟可靠、种类繁多的托管Kubernetes方案，越来越多的公司避免管理自己的集群。本文解释了个中原委。<br>
<br>管理Kubernetes很难，许多组织开始意识到：如果将容器编排方面的大部分重任交给托管服务提供商，自己可以更好地专注于其他尚未解决的工程技术问题。<br>
<br>如今，最受欢迎的托管Kubernetes方案（有时称为Kubernetes即服务，KaaS）包括：Amazon Elastic Kubernetes Service（EKS）、Azure Kubernetes Service（AKS）和Google Kubernetes Engine（GKE）。自2018年前后首次推出以来，每家云提供商越来越多地提供这些服务的托管版本，比如独具一格的GKE Autopilot和无服务器EKS Fargate。还有其他选择，比如Rancher、Red Hat OpenShift和VMware Tanzu，但基本上三大云供应商称霸这个领域。<br>
<br>云供应商竭力在以下两者之间寻求适当的平衡：允许客户控制和集成他们所需的服务，以及抽取棘手的自动扩展、升级、配置和集群管理任务。这些托管服务趋于成熟，许多组织由此认识到：管理自己的Kubernetes集群是不会带来差异化优势的繁重工作，越来越没有必要。<br>
<br>Kubernetes的联合创始人兼VMware Tanzu的首席工程师Joe Bea说：“有人深入钻研到开源二进制代码，编写自己的工具，这是相当极端的例子，除非您在以一种真正独特的方式使用Kubernetes，否则今天真没理由要这么做。”<br>
<br>AWS的计算服务副总裁Deepak Singh说：“对于拥有强大的工程和运营实力、自己运行Kubernetes的组织而言，总是存在例外情况，但是对于大多数客户而言，管理Kubernetes显然是一项艰巨的任务。扩展Kubernetes面临挑战，管理控制平面、API层和数据库很复杂，这不是胆小的人搞得了的。”<br>
<br>Azure Compute企业副总裁Brendan Burns之前曾是谷歌的Kubernetes首席工程师，他认为，两个因素促使市场对托管Kubernetes服务有了这种新的需求：更好的企业功能（尤其是专用网络支持和一致的策略管理等功能），以及更普遍的业务形势要求提高敏捷性和速度。<br>
<h3>托管服务发生了什么变化？</h3>关注开发者的调研公司RedMonk的联合创始人Stephen O’Grady认为，今天Kubernetes方面出现了一种类似的模式，与以前数据库和CRM方面的情况如出一辙，即没有管理员肯将其最重要的部分交给托管提供商，除非大势所趋。<br>
<br>他说：“企业认为某个方面具有战略意义时，最初倾向于自己运营。然后随着不断适应，它们逐渐意识到，这不仅没有给自己带来任何竞争优势，供应商更有可能比自己运营得更好。每家企业都在走这条路吗？还没有，但是走这条路的愿望和方向似乎很明确。”<br>
<br>云原生计算基金会（CNCF）的开发人员倡导者Ihor Dvoretskyi看到了这个潮流正在一大批的Kubernetes用户当中涌现。他说：“如今，我们可以看到受监管行业的更大客户比以前更频繁大量地使用托管服务。”<br>
<br>以金融数据巨头彭博（Bloomberg）为例。早在2019年，计算基础架构负责人Andrey Rybka告诉IT外媒《InfoWorld》：“你其实得有一支专家团队，与上游Kubernetes、CNCF和整个生态系统保持联系，才拥有那种内部知识。你不能光依赖供应商，需要了解这方面的种种复杂情况。”<br>
<br>快进到今天。彭博如今使用三大托管Kubernetes服务来处理生产环境中的工作负载。出现了什么变化？<br>
<br>Rybka说：“云提供商一直在努力改善其Kubernetes产品方面的服务质量。到目前为止，托管服务成熟度方面的趋势线表现良好。”<br>
<br>这还归结为针对特定的任务使用合适的工具。彭博仍然在本地运行约80%的Kubernetes工作负载，已投入大量资金来开发内部技能，以便可靠地管理该环境以及基于该环境的内部开发者平台。然而，针对适合云的工作负载，“我们依赖托管Kubernetes产品，因为我们无法做得更好。”<br>
<h3>对托管Kubernetes的需求不断增长</h3>许多来源的数字都反映了从自我管理的开源Kubernetes到托管发行版的这种转变。<br>
<br>在最新的CNCF云原生调查中，26%的受访者使用托管Kubernetes服务，高于一年前的23%，正迅速逼近本地安装的比例（31%）。属于CNCF成员的那些受访者可能会使这个数字偏向传统上捣鼓自己的Kubernetes集群的自我管理型组织。因此，托管Kubernetes的实际使用率可能高于CNCF调查表明的情况。<br>
<br>Flexera的《2021年云状态》报告显示，51%的受访者使用AWS托管容器方案，这包括Amazon EKS和亚马逊的非Kubernetes ECS服务。自我管理的Kubernetes达到48%，略高于Azure的Kubernetes托管服务（AKS）的43%和谷歌（GKE）的31%。<br>
<br>据Datadog的最新《容器报告》显示，在谷歌云上运行Kubernetes的组织中大约90%依赖GKE，AKS正迅速成为基于Azure平台上的Kubernetes用户的标准，三分之二的受访者已采用它。与此同时，亚马逊的EKS年同比增长10%，并且继续稳步攀升。<br>
<br>Singh说：“现在从AWS开始的客户很少不是从EKS开始的，而确实运行自己的Kubernetes的大量客户如今在EKS上运行，因为自己运行根本不值得。”比如说，机票元搜索引擎Skyscanner最近从自我管理Kubernetes改而青睐EKS。<br>
<h3>为什么使用托管的Kubernetes服务？</h3>缺乏内部专业知识、确保安全以及实际管理容器化环境，这些是Flexera调查受访者当中最常提及的几个Kubernetes挑战。<br>
<br>Flexera调查显示，在员工不到1000人、比较难获得云原生专业知识的组织中，托管Kubernetes更受欢迎。AWS托管方案无疑是管理容器的最普遍方式，占52%，自己管理的Kubernetes占37%，Azure管理的Kubernetes占35%，GKE管理的Kubernetes占23%。<br>
<br>CNCF的Dvoretskyi提到管理开销以及时间和资源消耗是采用托管Kubernetes的两大驱动因素。他说：“如果托管服务可以让组织满意，不重新发明轮子是显而易见的选择。”<br>
<br>对于全球旅行技术公司Amadeus而言，托管Kubernetes服务实现了简化管理的承诺。自2017年以来，Amadeus一直稳步转向Kubernetes作为其底层基础设施。<br>
<br>该公司的技术平台和工程技术高级副总裁Sylvain Roy说：“有一点要弄清楚，托管Kubernetes很省力。它为我们运营，这点很重要，因为做到确保自己拥有运行[Kubernetes]所需的所有人并非易事。”如今，Amadeus主要借助Red Hat的OpenShift平台，在本地环境或者私有云或公共云上的Kubernetes集群上运行约四分之一的工作负载。<br>
<br>Roy在提到考虑适合托管Kubernetes的工作负载时说：“首要因素是总体拥有成本：与我们自建架构相比，这需要多少成本？我们需要多少人来运营它？”<br>
<br>Amadeus尚未将任何工作负载迁移到托管服务，但是与微软达成新协议之后，它正在“必要时在适当地方”测试AKS及其他托管服务。<br>
<br>目前，这不包括核心应用软件。但是针对“对于我们的业务并非核心的工具和应用软件，以及小规模的特定使用场景，使用AKS之类的方法很明智，”Roy说。<br>
<h3>信任Kubernetes服务供应商的问题</h3>正如供应商们承认的那样，对于许多组织而言，决定使用托管Kubernetes服务归结于信任。<br>
<br>谷歌云的首席工程师Kelsey Hightower说：“Kubernetes出现时，有人担心这是挂羊头卖狗肉，是供应商在抢地盘。五六年后才反驳了这一点。”<br>
<br>同样，AWS的Singh表示，对于一些客户来说，EKS与Kubernetes的开源发行版保持关系密切很重要。AWS最近在GitHub上开源了其EKS发行版，即可证明这一点。<br>
<br>VMware的Beda承认，“谈到这个话题不得不提及锁定问题”，并敦促做出这些购买决定的任何人应适当地评估风险。他说：“你离开服务供应商的可能性有多大？如果你离开，这么做的成本会是多少？你需要重写多少代码以及需要多少再培训工作？任何做出这些投入的人需要了解需求、风险和缺点或不足。”<br>
<br>CNCF设有Kubernetes认证合格项目，确保安装的两套系统可实现互操作性，不管认证供应商是谁。<br>
<h3>为什么不是每个人都搭上托管Kubernetes这趟车？</h3>在像彭博和Amadeus这么庞大而复杂的公司，一些遗留或高度敏感的工作负载完全不得不留在本地，而运行它们的Kubernetes集群可能仍将保持一段时间的自我管理。<br>
<br>谷歌的Hightower说：“那些想要自我管理系统的人会担心数据平面；他们需要在某些领域进行定制或专门化。他们不介意托管的控制平面。”<br>
<br>AWS的Singh认为两类客户尚未搭上托管Kubernetes这趟车：一类是“构建者”，还有一类有着错综复杂的依赖关系。对于构建者这类客户，“我们的重点是识别它们，并花时间在AWS上提供核心Kubernetes”，开源Karpenter自动扩展系统之类的项目就是个例子。<br>
<br>他说：“第二类客户并不运行纯粹的Kubernetes，他们进行了分叉和变更，在无法访问的托管控制平面成为问题的地方采用依赖项。他们建立了自建版Kubernetes，要花一些时间才能回到普通版Kubernetes。”<br>
<br>CNCF的Dvoretskyi表示，如果组织已经投入了大量的资金来开发和招聘微调自己的Kubernetes集群所需的技能，这些技能不会就因为在适当的地方采用一些托管服务而会浪费。<br>
<br>Dvoretskyi说：“那些技能绝对并非毫无用处。即使你使用完全托管的Kubernetes，只是在现有集群上编写一些应用软件，了解底层工作机制也有助于更高效地构建这些应用软件。”<br>
<br>在Kubernetes这项企业核心技术的生命周期的现阶段，所有迹象表明，深入到自建Kubernetes系统的底层的理由越来越少。<br>
<br>O’Grady说：“也许你将其视为一项现有投入，没人想把它作为沉没成本一笔勾销，或者偏保守的组织对于一系列工作负载或业务存在担忧。或者有人担心基础设施中被认为具有战略意义的某部分不归自己控制。但是当你看到同行这么做时，这种担心就消失了，你会看到更多的人获得好处。”<br>
<br>原文链接：<a href="https://mp.weixin.qq.com/s/NuCCglhmHD2eyGtHfDoDgw" rel="nofollow" target="_blank">https://mp.weixin.qq.com/s/NuCCglhmHD2eyGtHfDoDgw</a>
                                
                                                              
</div>
            