
---
title: 'Reddit用户发现CSAM检测中使用的苹果NeuralHash算法隐藏在iOS 14.3中'
categories: 
 - 新媒体
 - cnBeta
 - 最新
headimg: 'https://static.cnbetacdn.com/thumb/article/2021/0819/79b9b3dd484793c.jpg'
author: cnBeta
comments: false
date: Wed, 18 Aug 2021 23:48:13 GMT
thumbnail: 'https://static.cnbetacdn.com/thumb/article/2021/0819/79b9b3dd484793c.jpg'
---

<div>   
据外媒AppleInsider报道，<strong>Reddit上的一个用户称，他发现了iOS 14.3中儿童性虐待材料(CSAM)检测中使用的苹果NeuralHash算法的一个版本。</strong>苹果在发给Motherboard 的一份声明中表示，在 iOS 14.3 中发现的 NeuralHash 版本并不是与 iOS 15 一起发布的最终版本。<br>
 <p style="text-align:center"><a href="https://static.cnbetacdn.com/article/2021/0819/79b9b3dd484793c.jpg" target="_blank"><img src="https://static.cnbetacdn.com/thumb/article/2021/0819/79b9b3dd484793c.jpg" alt="43838-85276-B5B0EACF-C6DA-432D-BBAE-1650992B21E5-xl.jpg" referrerpolicy="no-referrer"></a></p><p style="text-align: left;">Reddit用户u/AsuharietYgvar说，NerualHash代码被发现隐藏在iOS 14.3中。该用户说，他们已经对代码进行了逆向工程，并在Python中重建了一个工作模型，可以通过传递图像进行测试。</p><p style="text-align: left;">该算法是在隐藏的API中发现的，NeuralHash的容器被称为MobileNetV3。有兴趣查看代码的人可以在<a href="https://github.com/AsuharietYgvar/AppleNeuralHash2ONNX" target="_self">GitHub</a>中找到。</p><p style="text-align: left;">这位Reddit用户声称这一定是正确的算法，原因有二。首先，模型文件的前缀与苹果文档中发现的相同，其次，代码的可验证部分与苹果对NeuralHash的描述工作相同。</p><p style="text-align: left;">利用这个工作的Python脚本，GitHub用户已经开始研究这个算法是如何工作的，以及它是否可以被滥用。例如，一位名叫dxoigmn的用户发现，如果知道CSAM数据库中发现的结果哈希值，人们可以创建一个产生相同哈希值的假图像。如果是真的，有人可以制造出类似于任何东西的假图像，但产生所需的CSAM哈希值匹配。从理论上讲，一个用户可以将这些图片发送给苹果用户，以试图触发该算法。</p><p style="text-align: left;">尽管有这些发现，这个版本的NerualHash所提供的所有信息可能并不代表最终版本。苹果公司多年来一直在构建CSAM检测算法，因此可以认为存在一些版本的代码用于测试。如果u/AsuharietYgvar发现的确实是CSAM检测算法的某个版本，它可能不是最终版本。</p><p style="text-align: left;">如果dxoigmn 建议的攻击向量是可能的，只需将其生成的图像发送给用户，就有几个故障保护措施可以防止用户禁用 iCloud 帐户，并报告给执法部门。。有许多方法可以在一个人的设备上获得图像，如电子邮件、AirDrop或iMessage，但用户必须手动添加照片到照片库中。没有一个直接的攻击载体，不需要物理设备，或用户的iCloud凭证来直接向照片应用程序注入图像。</p><p style="text-align: left;">苹果也有一个人工审查程序。攻击图像不是人类可以解析的东西，而是一个位域，而且显然伪造的文件中不涉及 CSAM。</p><p style="text-align: left;">不是最终版本</p><p style="text-align: left;">Reddit用户声称他们发现了这些代码，但并不是ML专家。带有Python脚本的GitHub资源库暂时可供公众检查。</p><p style="text-align: left;">目前还没有人发现iOS 15测试版中存在CSAM数据库或匹配算法。一旦它出现，有理由相信一些用户将能够提取该算法进行测试和比较。</p><p style="text-align: left;">目前，用户可以探究这个潜在的NerualHash版本，并试图找到任何潜在的问题。然而，这项工作可能被证明是没有结果的，因为这只是用于CSAM检测的复杂过程的一部分，并没有考虑到凭证系统或服务器端发生的事情。</p><p style="text-align: left;">苹果还没有提供CSAM检测功能的确切发布时间表。</p>   
</div>
            