
---
title: 'Kubernetes Cluster API 1.0 版就绪：VMware 在 vSphere 之外，新增贡献 BYOH 基础设施提供程序'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://oscimg.oschina.net/oscnet/up-4053eb6260ad8f22119463a803df4ddb537.png'
author: 开源中国
comments: false
date: Tue, 07 Dec 2021 06:48:00 GMT
thumbnail: 'https://oscimg.oschina.net/oscnet/up-4053eb6260ad8f22119463a803df4ddb537.png'
---

<div>   
<div class="content">
                                                                    
                                                        <p style="color:#333333; margin-left:0; margin-right:0; text-align:left">2021年10月6日，云原生计算基金会（CNCF）宣布<strong>Cluster API v1.0</strong>已准备好投入生产并正式迁移到<strong>v1beta1</strong>API。从 Alpha项目的成熟度级别转变而来，Cluster API已经展现出了它越来越多的采用、成熟的功能以及对社区和包容性创新的坚定承诺。</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><img alt height="630" src="https://oscimg.oschina.net/oscnet/up-4053eb6260ad8f22119463a803df4ddb537.png" width="1200" referrerpolicy="no-referrer"></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">      Cluster API是一个Kubernetes项目，它为Kubernetes启用声明式管理，使用API轻松创建、配置和更新集群。它是一种端到端的方法，可以简化Kubernetes生命周期的重复性任务，同时在统一的基础架构中保持一致性和可重复性。</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">      从一开始，Cluster API就得到了众多公司的贡献，包括VMware、Microsoft、Weaveworks、Google、Mattermost、IBM、RedHat、D2iQ、Equinix、Apple、Talos Systems、Spectro Cloud、戴姆勒TSS、爱立信、Giant Swarm 、AppsCode、英特尔、Twilio、New Relic、亚马逊等。</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">      Cluster API的主要目标是让集群生命周期管理变得乏味，也就是简单易行。Cluster API和可扩展模型拥有经过验证的生产记录；随着时间的推移，它的目标是进一步巩固基础并构建抽象以简化最终用户的体验。</p> 
<hr> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">“Cluster API项目是VMware努力将云原生工具带给更广泛受众的核心。VMware在其转型之旅中为其企业客户提供支持，而Cluster API在多云世界中提供跨基础架构提供商的一致体验。通过与社区中的众多其他人合作，我们可以轻松地以社区一致的方式跨各种基础架构部署和管理Kubernetes集群——从vSphere到公有云再到裸机。新发布的Cluster Class特性通过提供一个更简单的界面来定义和共享Cluster模式，进一步简化了工作。通过为平台团队创建更好的工具集，他们可以反过来为应用程序团队提供更加自动化、快速和简单的内部产品。最终结果是应用程序团队交付得更快、更安全。”</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><strong>——</strong><em><strong>VMware Tanzu产品家族首席工程师Joe Beda</strong></em></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">“在VMware，我们相信竞争让我们每个人都变得更好，而协作让世界变得更美好。我们很自豪能够与Kubernetes社区一起走过从Cluster API成立到目前的生产就绪状态的旅程。作为一个系统，它从根本上重新定义了用于部署和维护Kubernetes集群的模型，将Kubernetes控制模式的强大功能带入了大规模的基础设施管理领域。衷心祝贺社区发布 v1.0。我们期待这个项目的未来，不仅是我们Tanzu产品线的一个基本部分，而且是充满活力的Kubernetes生态系统的一个日益重要的部分。”</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><em><strong>——VMware现代应用和管理事业群副总裁Craig McLuckie</strong></em></p> 
<hr> 
<h1 style="margin-left:0; margin-right:0; text-align:left"><strong>自带主机基础设施提供程序（Bring Your Own Host Infrastructure Provider）</strong></h1> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><u><em><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fvmware-tanzu%2Fcluster-api-provider-bringyourownhost" target="_blank">https://github.com/vmware-tanzu/cluster-api-provider-bringyourownhost</a></em></u></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><strong>      BYOH项目是VMware中国研发中心边缘计算实验室共同发起和参与的开源项目。</strong>该项目于2021年初启动，由来自全球五个时区/国家的同事共同推进，并于2021年10月在VMware Tanzu下开源。自带主机（BYOH）项目是符合Cluster API v1beta1定义的基础设施提供程序，用于已经安装Linux的物理机/虚拟机。</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">      近几年随着大规模应用上云的趋势，越来越多的企业应用迁移到云基础设施上。但是在选择哪家云提供商的问题上，由于技术演进、商业模式和成本回报等方面的考虑，企业自然而然地期望能够拥有在多个云上选择、同时使用和未来迁移的灵活性。另一方面，随着边缘计算的快速发展和云边协同越来越紧密化的演进，边缘侧应用越来越多地期望以云原生的方式运维、以边原生的方式运行。基于Kubernetes以及各种针对以上需求的衍生项目和技术架构方案在近几年层出不穷。</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">      在此类架构设计中，我们发现的一个普遍存在的共同问题是：<strong>边缘侧的某架构通常和特定云的实现有较强的耦合</strong>。这可能既是厂商技术演进便利性的结果，也有某些商业因素考虑。但技术提供商各自设计并实现相互不完全兼容的架构，对于企业用户的采用灵活性就产生了不必要的困扰。</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">      我们期望能够利用Cluster API这样可能跨云、统一接口实现的Kubernetes集群和舰队管理方式，向下延伸到边缘计算领域，实现云边协同方案的、真正的中立性。</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><strong>      BYOH的愿景是：</strong>用户可以在任何主流的公有云、混合云或私有云上建立Kubernetes管理集群、实现舰队管理，可以Kubernetes原生的方式、上游社区API的接口方便地管理任何地点、异构CPU平台、支持容器的任何OS、虚拟或物理机上的边缘节点及其上的边缘应用。</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">      从技术上讲，BYOH也可以应用在非边缘的场景里。</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><img alt src="https://oscimg.oschina.net/oscnet/up-3ee59ca93d81504fac8ccb9463d74cb534c.png" referrerpolicy="no-referrer"></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:center"><strong>架构图</strong></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">BYOH现在还是处于Alpha阶段的初创项目，当下仅提供符合Cluster API定义的<strong>基础功能</strong>：</p> 
<ul style="list-style-type:disc; margin-left:0; margin-right:0"> 
 <li> <p style="margin-left:0; margin-right:0">支持原生Kubernetes manifest和API</p> </li> 
 <li> <p style="margin-left:0; margin-right:0">支持单节点和多节点控制面集群</p> </li> 
 <li> <p style="margin-left:0; margin-right:0">支持已部署的Ubuntu 20.04虚拟机和物理机</p> </li> 
</ul> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">这是将BYOH项目与VMware Tanzu开源社区版（Tanzu Community Edition，TCE）集成，并部署管理多节点、异构平台集群的<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fmp.weixin.qq.com%2Fs%2FVRqYsSuJ2cNS1y6_Dl6fKQ" target="_blank"><strong>演示视频</strong></a>。</p> 
<hr> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:justify"><strong>尝试BYOH提供程序：</strong></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:justify"><span style="color:#3498db"><em><u>https://github.com/vmware-tanzu/cluster-api-provider-bringyourownhost/blob/main/docs/getting_started.md</u></em></span></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:justify"><strong>如何在本地测试BYOH提供程序： </strong></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:justify"><span style="color:#3498db"><em><u>https://github.com/vmware-tanzu/cluster-api-provider-bringyourownhost/blob/main/docs/local_dev.md</u></em></span></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:justify">欢迎感兴趣的业内同行与我们交流、跟踪BYOH项目的后续更新、或提供直接代码贡献。</p>
                                        </div>
                                      
</div>
            