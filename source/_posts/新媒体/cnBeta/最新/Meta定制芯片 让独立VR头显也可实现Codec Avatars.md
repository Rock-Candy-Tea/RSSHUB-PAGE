
---
title: 'Meta定制芯片 让独立VR头显也可实现Codec Avatars'
categories: 
 - 新媒体
 - cnBeta
 - 最新
headimg: 'https://static.cnbetacdn.com/article/2022/0505/4f5a6eeae710a50.webp'
author: cnBeta
comments: false
date: Thu, 05 May 2022 02:43:00 GMT
thumbnail: 'https://static.cnbetacdn.com/article/2022/0505/4f5a6eeae710a50.webp'
---

<div>   
Meta Reality Labs 科研人员近日研发出一款 VR 头显原型，内置了一个专门用于处理人工智能的定制加速器芯片，使在独立头盔上渲染该公司的逼真的 Codec Avatars 成为可能。<br>
<p style="text-align:center"><img src="https://static.cnbetacdn.com/article/2022/0505/4f5a6eeae710a50.webp" referrerpolicy="no-referrer"></p><p style="text-align: left;">在公司更名之前，Meta 公司就一直在推动 Codec Avatars 项目，该项目旨在使 VR 中近乎逼真的头像成为现实。利用设备上的传感器（如眼球追踪和嘴巴追踪）和人工智能处理的组合，该系统以逼真的方式实时为用户制作详细的动画。</p><p style="text-align: left;">Codec Avatars 项目的早期版本需要使用 NVIDIA 的 Titan X GPU 进行渲染支持，这使得像 Meta 最新 Quest 2 这样的移动独立头显无法驱动这些需求。</p><p style="text-align: left;">于是该公司已经开始研究如何在低功率的独立头显上实现 Codec Avatars，上个月召开的 2022 年 IEEE CICC 会议上发表的一篇论文证明了这一点。在这篇论文中，Meta 公司透露它创建了一个用 7 纳米工艺制造的定制芯片，作为专门用于 Codec Avatars 的加速器。</p><p style="text-align:center"><img src="https://static.cnbetacdn.com/article/2022/0505/a5f1f7dec8a73e8.webp" referrerpolicy="no-referrer"></p><p style="text-align: left;">根据研究人员的说法，该芯片远非现成的。该小组在设计它时，考虑到了 Codec Avatars 处理管道的一个重要部分，特别是分析传入的眼球追踪图像，并生成 Codec Avatars 模型所需的数据。该芯片的占地面积仅有 1.6mm²。</p><p style="text-align: left;">研究人员写道：“在7纳米技术节点制造的测试芯片具有一个神经网络（NN）加速器，由1024个乘积（MAC）阵列、2MB片上SRAM和一个32位RISC-V CPU组成”。反过来，他们也重建了Codec Avatars人工智能模型的部分，以利用该芯片的特定架构。</p><p style="text-align: left;">研究人员表示：“通过重新构建基于卷积[神经网络]的眼睛注视提取模型，并为硬件量身定做，整个模型适合在芯片上使用，以减轻系统级能量和片外内存访问的延迟成本。通过在电路层面有效地加速卷积操作，所提出的原型[芯片]在低外形尺寸下实现了每秒30帧的性能和低功耗”。</p><p style="text-align:center"><img src="https://static.cnbetacdn.com/article/2022/0505/47a9afaf024b059.webp" referrerpolicy="no-referrer"></p><p style="text-align: left;">通过加速 Codec Avatars 工作负载的密集部分，该芯片不仅加快了进程，而且还减少了所需的功率和热量。由于芯片的定制设计，它能够比通用CPU更有效地做到这一点，然后为Codec Avatars的眼球追踪组件的重新架构的软件设计提供参考。</p><p style="text-align: left;">但头显的通用CPU（在这种情况下，Quest 2的Snapdragon XR2芯片）也没有闲着。当定制芯片处理Codec Avatars的部分编码过程时，XR2管理解码过程和渲染化身的实际视觉效果。</p><p style="text-align:center"><img src="https://static.cnbetacdn.com/article/2022/0505/da8ac159e50abf1.webp" referrerpolicy="no-referrer"></p><p style="text-align: left;">这项工作一定是相当多学科的，因为论文中提到了12名研究人员，他们都来自Meta的现实实验室。H. Ekin Sumbul, Tony F. Wu, Yuecheng Li, Syed Shakib Sarwar, William Koven, Eli Murphy-Trotzky, Xingxing Cai, Elnaz Ansari, Daniel H. Morris, Huichu Liu, Doyun Kim, and Edith Beigne。</p><p style="text-align: left;">令人印象深刻的是，Meta的Codec Avatars可以在独立的耳机上运行，即使需要一个特殊的芯片。但我们不知道的一点是，头像的视觉渲染是如何处理的。用户的底层扫描是高度详细的，可能太复杂而无法在Quest 2上完全渲染。目前还不清楚在这种情况下，Codec Avatars的"逼真"部分被保留了多少，即使所有的基础部分都在那里以驱动动画。</p>   
</div>
            