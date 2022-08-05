
---
title: '刚刚，Google Cloud发布了其首款基于Arm的虚拟机'
categories: 
 - 编程
 - Dockone
 - 周报
headimg: 'https://picsum.photos/400/300?random=3082'
author: Dockone
comments: false
date: 2022-08-05 05:28:49
thumbnail: 'https://picsum.photos/400/300?random=3082'
---

<div>   
<br>前段时间，AWS凭借着Graviton实例实现了Arm虚拟机，微软Azure也紧随其后。如今Google Cloud终于有所行动，发布了自己首个基于Arm的虚拟机。而且不同于AWS自研定制芯片的思路，Google Cloud在这条道路上决定追随Azure的脚步，同样使用Ampere芯片。这些新虚拟机目前正处于预览阶段，后续将加入Google Cloud的Tau虚拟机家族，命名为“Tau T2A”。这是一条去年才正式推出的产品线，采用AMD Milan处理器，主要强调更高的性能价格比。<br>
<br>Google Cloud云基础设施副总裁兼总经理Sachin Gupta在新闻发布会上表示，“我们很高兴能够扩展除英特尔与AMD之外的计算架构选项，正式进军Arm生态系统，为我们的客户提供更多、更灵活的选项。我们已经能够支持由多种操作系统、数据库、编程语言及工具构成的广泛生态系统。”<br>
<br>新芯片将采用预定制SKU，最多可容纳48个vCPU，每vCPU相应配备最高4 GB内存。这些虚拟机将提供高达32 Gbps网络带宽，并支持Google Cloud生态系统中的各类常用存储选项。谷歌公司表示，强大且灵活的CPU配置使这些虚拟机能够从容应对各类工作负载，包括Web服务器、运行容器化微服务、数据记录等等。<br>
<br>与AMD驱动的Tau芯片一样，谷歌将此次公布的Arm新成员也视为高性价比的优化解决方案。例如，Google Cloud在us-central1区域内，为32核Tau T2A虚拟机开出的价格为每小时1.232美元。<br>
<br>用户可以在这些虚拟机上使用RHEL、CentOS、Ubuntu以及Rocky Linux，外加谷歌自家用于运行容器化应用程序的容器优化型操作系统。在这方面，Arm已经得到大部分操作系统和软件供应商的支持，这反过来又大大提高了这些虚拟机（当然也包括AWS和Azure两家竞争对手的虚拟机）的实用度。<br>
<br>新的虚拟机现已在少数区域上线，包括us-central（爱荷华州-A、B、F区）、europe-west4（荷兰-A、B、C区）及asia-southeast1（新加坡-B、C区），后续还将逐渐登陆更多其他数据中心。<br>
<br>Ampere Computing公司首席产品官Jeff Wittich表示，“Ampere Altra云原生处理器的设计初衷，就是为了满足现代云应用的需求。我们与Google Cloud的密切合作成就了高性价比Tau T2S优化型实例的推出，成功为要求苛刻的横向扩展应用程序找到了一条快速高效的部署之路。”<br>
<br>除了将这些虚拟机作为Google Cloud计算引擎的组成部分之外，谷歌现在还支持将它们作为Kubernetes引擎、Dataflow流与批处理服务，以及全新托管作业调度程序Batch中的一部分。Gupta解释称，“Batch这项新功能主要负责支持面向吞吐量的计算用例，包括天气预报与电子设计自动化。在其帮助之下，批处理作业将在时间、位置和成本方面获得前所未有的灵活性优势。”<br>
<br><strong>原文链接：<a href="https://techcrunch.com/2022/07/13/google-cloud-launches-its-first-arm-based-vms/">Google Cloud launches its first Arm-based VMs</a></strong>
                                
                                                              
</div>
            