
---
title: 'Reddit用户逆向工程苹果CSAM工具：发现算法早已存在'
categories: 
 - 新媒体
 - cnBeta
 - 最新
headimg: 'https://static.cnbetacdn.com/article/2021/08/f93062e988bc03f.jpg'
author: cnBeta
comments: false
date: Wed, 18 Aug 2021 07:55:54 GMT
thumbnail: 'https://static.cnbetacdn.com/article/2021/08/f93062e988bc03f.jpg'
---

<div>   
据外媒报道，本月早些时候，苹果宣布将为其整个生态系统引入新的儿童安全功能。作为这项努力的一部分，这家位于库比蒂诺的公司将通过使用设备上的机器学习来扫描iCloud和Messages应用上的内容以此来检测出可能存在的儿童性虐待材料(CSAM)。<br>
 尽管苹果澄清称，这款应用不会被用来侵犯隐私，也不会被利用来获取他人的信息和照片，但该声明还是在科技界和公众中引发了大量争议。<p style="text-align: left;">在受到批评后，苹果发布了一份六页的文件以概述其使用设备上的机器学习和一种名为NeuralHash的算法来对抗CSAM的方法。</p><p style="text-align: left;">苹果进一步表示，其CSAM检测模块正在开发中且只会扫描被标记为有问题的图像。</p><p style="text-align: left;">然而在最新的进展中，一位好奇的Reddit用户进入了苹果隐藏的API并对NeuralHash算法进行了逆向工程。令人惊讶的是，他们发现这种算法早在iOS 14.3就存在于苹果的生态系统中。这可能会引起一些人的惊讶，因为整个CSAM事件是一个最近才出现的东西，但这位用户却指出，有很好的理由相信这一发现是合法的。</p><p style="text-align: left;">首先，发现模型的文件都附加了NeuralHashv3b前缀。它遵循了苹果六页纸的命名规则。其次，还注意到，未公开的源代码使用了跟苹果文档中概述的相同的合成哈希的过程。第三，苹果称他们的哈希方案创建的哈希几乎独立于图像的大小和压缩，这也是该名Reddit用户在源代码中发现的，这进一步巩固了他们的信念，即确实发现了隐藏在源代码深处的NeuralHash。</p><p style="text-align:center"><a href="https://static.cnbetacdn.com/article/2021/08/f93062e988bc03f.jpg" target="_blank"><img src="https://static.cnbetacdn.com/article/2021/08/f93062e988bc03f.jpg" referrerpolicy="no-referrer"></a></p><p style="text-align: left;">Reddit用户在GitHub上发布了发现。虽然他没有公布导出的模型文件，但他概述了提取模型并将其转换为可部署的ONNX运行时格式的过程。在导出模型后，他测试运行了推断并给出了一个样本图像。</p><p style="text-align:center"><a href="https://static.cnbetacdn.com/article/2021/08/2be09a61d076a1a.jpg" target="_blank"><img src="https://static.cnbetacdn.com/article/2021/08/2be09a61d076a1a.jpg" referrerpolicy="no-referrer"></a></p><p style="text-align: left;">根据这位Reddit用户的说法，所有设备上的哈希都是一样的，除了几个bits之外，而这是意料之中的行为，因为NeuralHash负责处理浮点计算，其准确性在很大程度上取决于硬件。另外，他还补充称，苹果很可能会在随后的数据库匹配算法中适应这些相差几位的差异。</p><p style="text-align: left;">这位Reddit用户认为，现在是深入研究NeuralHash的工作原理及其对用户隐私的影响的好时机。</p>   
</div>
            