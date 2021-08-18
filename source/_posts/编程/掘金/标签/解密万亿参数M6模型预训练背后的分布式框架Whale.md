
---
title: '解密万亿参数M6模型预训练背后的分布式框架Whale'
categories: 
 - 编程
 - 掘金
 - 标签
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/d9376c90519c49ff924eeaa741314282~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Tue, 17 Aug 2021 23:37:56 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/d9376c90519c49ff924eeaa741314282~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>简介： 最近，阿里云PAI团队和达摩院智能计算实验室一起发布“低碳版”巨模型M6，大幅降低万亿参数超大模型训练能耗。借助我们自研的Whale框架仅使用480卡GPU，即训练出了规模达人类神经元10倍的万亿参数多模态大模型M6，与传统海外公司实现万亿参数规模相比，能耗降低超八成、效率提升近11倍。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/d9376c90519c49ff924eeaa741314282~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>作者 | 王林<br>
来源 | 阿里技术公众号</p>
<p>最近，阿里云PAI团队和达摩院智能计算实验室一起发布“低碳版”巨模型M6，大幅降低万亿参数超大模型训练能耗。借助我们自研的Whale框架仅使用480卡GPU，即训练出了规模达人类神经元10倍的万亿参数多模态大模型M6，与传统海外公司实现万亿参数规模相比，能耗降低超八成、效率提升近11倍。</p>
<p>M6是国内首个实现商业化落地的多模态大模型。M6拥有超越传统AI的认知和创造能力，擅长绘画、写作、问答，在电商、制造业、文学艺术等诸多领域拥有广泛应用前景。</p>
<p>这里来为大家介绍支持万亿参数模型训练的Whale框架设计。</p>
<h1 data-id="heading-0">一 模型发展趋势和挑战</h1>
<p><strong>1 模型发展趋势</strong></p>
<p>随着深度学习的火爆，模型的参数规模也增长迅速，OpenAI数据显示：</p>
<ul>
<li>2012年以前，模型计算耗时每2年增长一倍，和摩尔定律保持一致；</li>
<li>2012年后，模型计算耗时每3.4个月翻一倍，远超硬件发展速度；</li>
</ul>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/c079ed54717e4cd9a8245ca7b48d144f~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>近一年模型参数规模飞速增长，谷歌、英伟达、阿里、智源研究院都发布了万亿参数模型，有大厂也发布了百亿、千亿参数模型。同时，随着模型参数规模增大，模型效果也在逐步提高，Nvidia测试Bert模型不同参数规模，发现模型困惑度随模型参数规模增加而降低。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/07a72fdab9af4da7bbef2db6eabb0ae7~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>Google在GShard paper中也发现MoETransformer 模型参数规模越大，翻译质量越高。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/1b53e48eb1c94464a537bc5ea24838c7~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p><strong>2 大模型训练的挑战</strong></p>
<p>大模型带来模型效果提升的同时，也为训练框架带来更大的挑战，例如当我们要训练一个万亿规模的模型时会面临如下挑战：</p>
<ul>
<li>训练难：GPU显存已经不够存放模型副本，数据并行已经不能满足需求；需要框架提供新的并行策略，协同多GPU能力来存放和训练模型；如何给用户提供简洁、易用的接口，让用户能很容易实现分布式版模型；超大规模模型对计算效率、通信效率都带来很大挑战，如何提高计算和通信效率；下游任务如何对接，如何支持批量预测和在线推理需求；</li>
<li>成本高：以万亿模型为例，模型参数有4TB大小、梯度也有4TB，加上optimizer states和active tensor，显存需求巨大；业界训练同等规模模型需要的资源：英伟达 3072 A100、谷歌 2048 TPU v3，成本太高很难落地；如何降本增效，使用更少的资源，更快的训练收敛；</li>
</ul>
<p>当前已经有一些分布式训练框架，例如：Horovod、Tensorflow Estimator、PyTorch DDP等支持数据并行，Gpipe、PipeDream、PipeMare等支持流水并行，Mesh Tensorflow、FlexFlow、OneFlow、MindSpore等支持算子拆分，但这些框架还有一些不足：</p>
<ul>
<li>模式单一：很多框架只支持部分并行策略，不能完全支持各种混合并行；</li>
<li>接入门槛高：用户实现模型分布式版本难度大、成本高，需要有领域专家经验才能实现高效的分布式并行策略；</li>
<li>迁移代价大：不同分布式框架并行化实现割裂，不同框架有各自定义的DSL，当用户要切换并行策略时，需要学习各种接口，重新改写模型；</li>
<li>性能不理想：部分框架实现未考虑集群物理环境；</li>
</ul>
<p>为了应对当前分布式训练的挑战，我们研发了分布式训练框架Whale，主要目标是：</p>
<ul>
<li>统一多种并行策略：在一个框架中支持各种并行策略以及这些策略的各种组合；</li>
<li>简洁易用的接口：用户只需添加几行annotation即可完成并行策略的配置，模型代码不需要改动；</li>
<li>高效的训练框架：结合硬件资源、网络拓扑和模型进行协同优化，打造高效分布式训练框架；</li>
</ul>
<h1 data-id="heading-1">二 PAI自研Whale框架</h1>
<p><strong>1 Whale架构</strong></p>
<p>我们推出统一多种并行策略的高性能分布式训练框架Whale，从如下角度来应对分布式训练的挑战：</p>
<ul>
<li>将不同并行化策略进行统一抽象、封装，在一套分布式训练框架中支持多种并行策略；</li>
<li>基于Tensorflow设计一套分布式并行接口，完全兼容Tensorflow，用户仅仅只需添加几行annotation就可以实现丰富的分布式并行策略；</li>
<li>结合模型结构和网络拓扑进行调度和通信优化，提供高效的分布式训练能力。</li>
</ul>
<p>Whale框架如下图所示，主要分4个模块：</p>
<ul>
<li>API：提供简洁易用接口，让用户组合使用各种混合并行策略；</li>
<li>Whale IR：将并行策略转成内部表达，通过TaskGraph、Multi-Dimension、VirtualDevices抽象来表达各种并行策略；</li>
<li>Whale Engine：基于WhaleIR，通过图编辑工具来构建分布式执行图；</li>
<li>Runtime：将分布式执行图转成TFGraph，再调用TF 的Runtime来执行；</li>
</ul>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/8dcfe425affa4e17abcecdd08f8ad849~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p><strong>2 Whale简介易用接口</strong></p>
<p>Whale提供简洁易用的接口来描述各种并行策略，主要的原语：</p>
<ul>
<li>cluster：配置Virtual Device的划分方法</li>
<li>replica：数据并行</li>
<li>stage：划分TaskGraph</li>
<li>pipeline：流水并行</li>
<li>split：算子拆分</li>
</ul>
<p>用这些接口可以组合各种并行策略，例如：</p>
<ul>
<li>数据并行：</li>
</ul>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/7591a2cc2584405697b43f14c0271560~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<ul>
<li>流水并行：</li>
</ul>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/41819b74af944c9b959dcfac24c574cd~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<ul>
<li>流水并行+数据并行：</li>
</ul>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/2d8c332c00614b94bb76b13fe26a1e2f~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<ul>
<li>更多并行策略示例：</li>
</ul>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/e078e4b3777149d09d46986b1ab70e12~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p><strong>3 Whale训练流程</strong></p>
<p>使用Whale进行分布式训练流程：</p>
<ul>
<li>并行策略配置：使用Whale API来为模型配置并行策略，只需添加几行annotation，无需修改模型代码，方法如 2.2节 所示；可以将模型划分为多个TaskGraph，TaskGraph支持配置多个并行策略，每个TaskGraph可以配置不同的并行策略；</li>
<li>虚拟资源划分：按并行策略来划分Virtual Device，每个TaskGraph对应一个Virtual Device；按GPU资源和网络topo来为Virtual Device选择Physical Device；</li>
<li>分布式执行图：基于并行策略和资源分配信息，使用图编辑工具来编辑执行图（图拷贝、拆分、插入通信节点等），生成最终的分布式执行图；调用TF的runtime来执行分布式Graph；</li>
</ul>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/0f0084337fab4055be81e3ffba79e412~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p><strong>三 万亿M6模型预训练</strong></p>
<p>万亿模型的算力需求非常大，为了降低算力需求，Whale中实现了MoE(Mixture-of-Experts)结构，MoE的主要特点是稀疏激活，使用Gating(Router)来为输入选择Top k的expert进行计算（k常用取值1、2），从而大大减少算力需求。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/a42f03c0de564e15825bd77b192390eb~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>Whale中实现了MoE(Mixture-of-Experts) layer，并支持专家并行，将experts拆分到多个Devices上，降低单个Device的显存和算力需求。同时数据并行有利于提升训练的并发度，因此采用数据并行+专家并行组合的混合并行策略来训练M6模型：MoElayer采用专家并行，其他layer采用数据并行。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/e916c7b6f3814d188debaf92f64f3232~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>Whale中提供简洁易用的接口来进行模型的混合并行训练，只需要增加几行annotation来配置并行策略，模型本身不需要任何修改。M6模型采用数据并行+专家并行的策略，只需要增加如下图的annotation：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/e5b338fadb0048eb974b29c6044690ea~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>同时为了节约训练资源，提高训练效率，Whale中提供各种优化技术：</p>
<p>显存优化：</p>
<ul>
<li>Auto Gradient Checkpoint，自动选择最优checkpoint节点，节约activation的显存；</li>
<li>Group-wise Apply，优化Optimizer Apply阶段的显存；</li>
<li>CPU Offload技术，优化Optimizer status和Weight的显存；</li>
<li>通信池化，控制通信的数据块大小和并发，节约通信的显存；</li>
</ul>
<p>计算、通信加速：</p>
<ul>
<li>采用DP+EP混合并行策略，降低算力需求；</li>
<li>采用分组融合通信、半精度通信、拓扑感知的All2All通信算子等技术来提高通信效率；</li>
<li>结合混合精度、编译优化等技术提高训练效率；</li>
</ul>
<p>借助Whale框架，首次在480 V100 上，3天内完成万亿M6模型的预训练。相比此前英伟达使用3072 A100 GPU实现万亿参数、谷歌使用2048 TPU实现1.6万亿参数大模型，此次达摩院仅使用480卡V100 32G GPU就实现了万亿模型M6，节省算力资源超80%，且训练效率提升近11倍。</p>
<h1 data-id="heading-2">四 结语</h1>
<p>模型参数规模已越来越大，大模型已成为发展趋势，为解决超大模型训练的挑战，我们自研Whale框架，将不同并行化策略进行统一抽象、封装，在一套分布式训练框架中支持多种并行策略。Whale提供简洁易用的接口，用户只需添加几行annotation即可实现各种并行策略，不需要对模型本身进行修改。同时我们结合硬件资源、网络topo、模型进行软硬件协同优化，提供高效分布式训练框架。</p>
<p>通过Whale框架，我们用480 V100 GPU卡训练万亿规模模型，并在3天内完成模型训练收敛，为超大规模模型训练落地提供了可能，后续我们会进一步完善Whale框架，从更大规模、更快速度、更高性价比3个维度去扩展Whale框架的能力。同时也会推动Whale能力在更多业务场景落地，让技术能力到产品能力的转变。</p>
<p><a href="https://link.juejin.cn/?target=http%3A%2F%2Fclick.aliyun.com%2Fm%2F1000289935%2F" target="_blank" rel="nofollow noopener noreferrer" title="http://click.aliyun.com/m/1000289935/" ref="nofollow noopener noreferrer">原文链接</a></p>
<p>本文为阿里云原创内容，未经允许不得转载。</p></div>  
</div>
            