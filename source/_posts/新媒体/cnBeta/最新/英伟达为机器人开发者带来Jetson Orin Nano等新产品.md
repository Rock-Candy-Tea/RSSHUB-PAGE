
---
title: '英伟达为机器人开发者带来Jetson Orin Nano等新产品'
categories: 
 - 新媒体
 - cnBeta
 - 最新
headimg: 'https://static.cnbetacdn.com/article/2022/0921/4f0ee0fee13db14.jpg'
author: cnBeta
comments: false
date: Wed, 21 Sep 2022 09:42:00 GMT
thumbnail: 'https://static.cnbetacdn.com/article/2022/0921/4f0ee0fee13db14.jpg'
---

<div>   
<strong>在 GTC 2022 会议期间，英伟达介绍了面向机器人开发领域的新硬件和配套服务，旨在为行业开发和机器测试而提供帮助。</strong>首先，英伟达的 Isaac Sim 机器人模拟平台将很快提供云端访问。其次，系统级模块的阵容也在快速扩展，包括专为低功率机器人设计的 Jetson Orin Nano、以及一个名为 IGX 的新平台。<br>
<p><img src="https://static.cnbetacdn.com/article/2022/0921/4f0ee0fee13db14.jpg" referrerpolicy="no-referrer"></p><p><strong>早在去年 6 月，Isaac Sim 就已经以公测形式推出。</strong>特点是允许设计师模拟机器人和现实世界的模型交互，比如仓库和工厂车间的数字重建。</p><p>用户可借助模拟传感器生成数据集，在现实世界中的机器人上训练模型，并且利用来自批量并行、以及独特的模拟合成数据，来提升模型的性能。</p><p><img src="https://static.cnbetacdn.com/article/2022/0921/bb45ac95139be69.jpg" referrerpolicy="no-referrer"></p><p>这样的表述，并非营销层面的噱头。有研究指出，合成数据可以帮助试图实施 AI 解决方案、但又遇到诸多发展挑战的企业纾困。</p><p>麻省理工学院（MIT）的研究人员，最近还找到了一种使用合成数据对图像进行分类的方法。</p><p>更何况各大自动驾驶汽车公司都在积极使用模拟数据，来填补其从道路上收集真实数据的短板。</p><p><img src="https://static.cnbetacdn.com/article/2022/0921/12289e11c6523bb.jpg" referrerpolicy="no-referrer"></p><p>英伟达表示，即将发布的 Isaac Sim 可在 AWS RoboMaker 和 NVIDIA NGC 上使用，并支持部署到任何公共云、且很快会登陆该公司的 Omniverse Cloud 平台。</p><p>企业客户能够将在云平台上使用实时车队任务分配和路线规划引擎，并借助 NVIDIA cuOpt 来优化机器人的路径规划性能。</p><p><strong>英伟达高级产品营销经理 Gerard Andrews 在一篇博客文章中写道：</strong></p><blockquote><p>云端 Isaac Sim 能够汇聚分布在世界各地的开发团队，让他们同享一个虚拟世界，并在其中模拟和训练机器人。</p><p>与此同时，在云端运行的 Isaac Sim，意味着开发人员不再依赖于强大的工作站来运行模拟，并可在任何设备上配置、管理和查看模拟的结果。</p></blockquote><p><img src="https://static.cnbetacdn.com/article/2022/0921/1600f52e537bbe1.webp" referrerpolicy="no-referrer"></p><p><strong>接着来聊聊 Jetson Orin Nano：</strong>英伟达在 3 月推出了 Jetson Orin，这是该公司用于边缘计算的下一代 ARM 单板机。</p><p>该系列首位成员是 Jetson AGX Orin，但我们现又迎来了 Orin Nano —— 它以更实惠的配置，拓展了 Jetson Orin 家族的产品阵容。</p><blockquote><p>Orin Nano 具有该系列迄今为止最小的外形尺寸，全速运行时可执行高达每秒 40 万亿次的操作（TOPS）。</p><p>作为 Jetson 家族的最入门 SKU，英伟达还提供了六款基于 Orin 的生产模块 —— 适用于一系列机器人和本地离线计算应用程序。</p></blockquote><p>值得一提的是，Orin Nano 采用了与英伟达先前宣布的 Orin NX 兼容的模块，支持 2020 年问世的 Ampere GPU 架构的 AI 应用程序管道。</p><p>感兴趣的开发者可于明年 1 月入手两个版本，其售价为 199 美元。其中 Orin Nano 8GB 具有 7~15W 的可配置功率，性能为 40 TOPS；而 Orin Nano 4GB 具有 5~10W 的较低功率，性能为 20 TOPS 。</p><p><strong>英伟达嵌入式与边缘计算副总裁 Deepu Talla 在一份声明中称：</strong></p><blockquote><p>自六个月前宣布推出 Jetson AGX Orin 以来，其已得到超过 1000 名客户和 150 家合作伙伴的采用。而随着 Orin Nano 的到来，这一趋势还将显著扩大。</p><p>此外在价格方面，Jetson AGX Orin 的成本远超 1000 美元，而 Orin Nano 要实惠得多 —— 它为入门级边缘 AI 和机器人技术设立了新的标准。</p></blockquote><p><img src="https://static.cnbetacdn.com/article/2022/0921/218f8905dac07c6.webp" referrerpolicy="no-referrer"></p><p><strong>最后，英伟达悄然放出了 IGX 的一瞥</strong> —— 作为一套适用于“高精度”边缘 AI 的平台（尤其是制造业和物流等应用场景），该公司称其可为工厂、仓库、诊所、医院等需要高度监管的环境，提供了额外的安全层和低延迟的 AI 性能体验。</p><blockquote><p>作为 IGX 平台的一部分，IGX Orin 是一款用于资助工业机器和医疗设备的 AI 芯片。</p><p>英伟达称，适用于原型和产品测试的开发工具包，将于明年初向企业提供。</p><p>每个工具包都具有集成的 GPU / GPU，以及具有安全特性的软件堆栈，可针对不同的用例进行配置和编程。</p></blockquote><p>英伟达补充道，目前其正在与 Canonical、Red Hat 和 SUSE 等 Linux 发行版的开发商合作，以期为 IGX 提供长期且全栈的支持。首席执行官黄仁勋在一份声明中表示：</p><blockquote><p>随着人类越来越多地与机器人合作，各行业正在为人工智能和计算制定新的功能安全标准。</p><p>而 IGX 将帮助公司构建下一代软件定义的工业和医疗设备，以使之能够在与人类相同的环境中安全运行。</p></blockquote>   
</div>
            