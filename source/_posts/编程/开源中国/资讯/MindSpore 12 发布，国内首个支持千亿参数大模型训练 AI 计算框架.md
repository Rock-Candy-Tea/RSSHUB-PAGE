
---
title: 'MindSpore 1.2 发布，国内首个支持千亿参数大模型训练 AI 计算框架'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://oscimg.oschina.net/oscnet/up-f84ebb156c9d00cf76e8bb5579e58424703.png'
author: 开源中国
comments: false
date: Thu, 29 Apr 2021 14:14:00 GMT
thumbnail: 'https://oscimg.oschina.net/oscnet/up-f84ebb156c9d00cf76e8bb5579e58424703.png'
---

<div>   
<div class="content">
                                                                    
                                                        <p>4月26日，华为开发者大会2021（Cloud）期间（简称HDC. Cloud 2021），国内首个支持千亿参数大模型训练的AI计算框架MindSpore 1.2正式发布。最新1.2版本带来了AI框架领域 “全自动并行、全场景AI、可解释推荐模型” 三大创新，让开发者尽享AI开发。</p> 
<p><img alt src="https://oscimg.oschina.net/oscnet/up-f84ebb156c9d00cf76e8bb5579e58424703.png" referrerpolicy="no-referrer"></p> 
<h1 style="text-align:justify"><strong><span style="color:#222222"><span style="background-color:#ffffff">全自动并行</span></span></strong></h1> 
<p style="text-align:justify"><span style="color:#222222"><span style="background-color:#ffffff">MindSpore是业界首个基于网络拓扑和集群资源自动感知的全自动并行框架，且基于全自动并行能力已开发业界首个2000亿参数的中文预训练模型。</span></span></p> 
<p style="text-align:justify"><span style="color:#222222"><span style="background-color:#ffffff">在静态图模式下，MindSpore融合了流水线并行、模型并行和数据并行三种并行技术，开发者只需编写单机算法代码，添加少量并行标签，即可实现训练过程的自动切分，使得并行算法性能调优时间从月级降为小时级，同时训练性能相比业界标杆提升40%。</span></span></p> 
<p style="text-align:justify"><span style="color:#222222"><span style="background-color:#ffffff">在动态图模式下，MindSpore独特的函数式微分设计，能从一阶微分轻易地扩展到高阶微分，并进行整图性能优化，大幅提升动态图性能；结合创新的通讯算子融合和多流并行机制，较其它AI框架，MindSpore动态图性能提升60%。</span></span></p> 
<h1 style="text-align:justify"><strong><span style="color:#222222"><span style="background-color:#ffffff">全场景AI</span></span></strong></h1> 
<p style="text-align:justify"><span style="color:#222222"><span style="background-color:#ffffff">MindSpore实现了在云、边、端不同场景下硬件设备的快速应用、高效运行与有效协同。通过全场景AI的能力，Huawei Watch GT的抬腕识别率提升了80%，时延小于5ms，模型小于1KB，大幅提升了用户体验。</span></span></p> 
<ul> 
 <li style="text-align: justify;"><span style="color:#222222"><span style="background-color:#ffffff">在云端：通过自适应模型切分和服务内分布式并行调度技术，可支持超大模型在多张加速卡上的推理部署，且推理性能较目前业界领先的serving服务方式提升30%；</span></span></li> 
 <li style="text-align: justify;"><span style="color:#222222"><span style="background-color:#ffffff">在边缘侧：通过自适应模型压缩技术，将CV类（Computer Vision 计算机视觉）模型压缩2/3，推理时间缩短50%，用户侧实测精度损失<1%，能有效解决边缘侧算力瓶颈；</span></span></li> 
 <li style="text-align: justify;"><span style="color:#222222"><span style="background-color:#ffffff">在端侧：模型即代码，将模型编译到代码里，实现了极小的ROM（Read-Only Memory储存内存）占用。同时，通过算子数据重排技术提升端侧Cache命中率，可降低推理时延，解决在超轻量IOT设备进行部署时受设备类型、内存等所限制的难题。</span></span></li> 
</ul> 
<h1 style="text-align:justify"><strong><span style="color:#222222"><span style="background-color:#ffffff">可解释推荐模型</span></span></strong></h1> 
<p style="text-align:justify"><span style="color:#222222"><span style="background-color:#ffffff"><span style="color:#000000">MindSpore内置业界首个语义级可解释推荐模型TB-Net，基于原创知识图谱双向传导技术，从知识图谱的海量关系路径中，精准识别影响用户行为的核心特征和关键路径，提供个性化推荐和语义级的解释，可解释性评估指标相比业界模型提升63%。</span></span></span></p> 
<p style="text-align:justify"><span style="color:#222222"><span style="background-color:#ffffff">自2020年3月开源以来，MindSpore社区拥有逾17万名开发者，软件下载量超过24万，在超过10个行业规模使用。此外，在码云（Gitee）上MindSpore的代码活跃度、影响力、社区活跃度、团队构建、流行趋势综合排名第一。目前，MindSpore已是发展最快的AI开源社区。</span></span></p>
                                        </div>
                                      
</div>
            