
---
title: 'Facebook介绍可对图像和视频进行细分的自我监督学习AI'
categories: 
 - 新媒体
 - cnBeta
 - 最新
headimg: 'https://static.cnbetacdn.com/thumb/article/2021/0501/458f13f864a8fcc.jpg'
author: cnBeta
comments: false
date: Sat, 01 May 2021 08:19:43 GMT
thumbnail: 'https://static.cnbetacdn.com/thumb/article/2021/0501/458f13f864a8fcc.jpg'
---

<div>   
<strong>Facebook 今日宣布了与 Inria 合作开发的 DINO 算法，特点是无需对数据进行标记，就能够对 transformers 机器学习模型进行训练。</strong>具体说来是，作为计算机视觉领域中最困难的挑战之一，其需要人工智能对图像中的内容进行理解。但 Facebook 介绍的这个新模型，能够在不指定特定目标的情况下，发现和分割图像 / 视频中的对象。<br>
<p><a href="https://static.cnbetacdn.com/article/2021/0501/458f13f864a8fcc.jpg" target="_blank"><img src="https://static.cnbetacdn.com/thumb/article/2021/0501/458f13f864a8fcc.jpg" alt="1.jpg" referrerpolicy="no-referrer"></a></p><p style="text-align: center;">FB DINO 系统能够以无监督的方式细分图像</p><p>传统上的细分（Segmentation）操作是在监督学习的情况下执行的，且需要投喂标注了大量注释的示例数据。</p><p>在有监督的学习中，算法会在为特定输出注释的输入数据上开展训练，直到它们可以检测到输入和输出结果之间的潜在关系为止。</p><p>但在可自我监督学习（DINO）的方案下，系统能够主动对未标记的数据进行分类和处理。</p><p>Transformers 使得 AI 模型能够选择性地专注于其输入的一部分，从而使它们能够更有效地进行推理。</p><p>而在应用于语音和自然语言处理之前，转换器就已经被用于解决计算机视觉问题、以及图像的分类和检测。</p><p>自我专注层（Self-Attention Layers）是所谓的 Vision Transformers 的核心部分，每个空间位置都通过参考其他位置来表示。</p><p>这样当查看其它距离可能较远的图像时，转换器就能对整个场景建立起丰富而高级的理解。</p><p><img src="https://static.cnbetacdn.com/article/2021/0501/4cbfb3ffad41932.gif" alt="2.gif" referrerpolicy="no-referrer"></p><p>通过在相同图像的不同视图上匹配模型输出，DINO 能够有效地发现目标对象和跨图像的共享特征。此外 DINO 可基于视觉属性来连接各种类型，以类似于生物分类的结构，来清楚地分辨不同动物物种。</p><p>Facebook 声称，即使不以此为目的而进行设计，DINO 也是识别图像副本的最佳工具之一。展望将来，基于 DINO 的模型，还可用于识别错误信息或版权侵犯行为。</p><blockquote><p>Facebook 在博客中写道：通过在转换器上进行自我监督学习，DINO 为打造创造性的机器学习应用而提供了一个机遇，使得机器能够更深入地理解图像和视频。</p><p>目前需要人工标注的数据，已经成为了计算机视觉系统发展的一个主要瓶颈。但通过 DINO 方案，注释的效率可以更高，并将模型用于更大的任务集，且有可能扩展其可识别的概念的数量。</p></blockquote><p>最后，Facebook 今天还详细介绍了一种被称作 PAWS 的新机器学习方案。与此前的半监督方案和新技术相比，该公司的半监督方法具有更好的分类准确度。</p><p>值得一提的是，其所需的训练也少了一个数量级（ 1/ 4~12），意味着 PAWS 可能也适合于没有太多标记的图像领域（比如医学分析）。</p>   
</div>
            