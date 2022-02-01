
---
title: '研究人员利用GPU指纹技术追踪在线用户'
categories: 
 - 新媒体
 - cnBeta
 - 最新
headimg: 'https://static.cnbetacdn.com/thumb/article/2022/0201/feb4a9ee42344e7.jpg'
author: cnBeta
comments: false
date: Tue, 01 Feb 2022 09:10:51 GMT
thumbnail: 'https://static.cnbetacdn.com/thumb/article/2022/0201/feb4a9ee42344e7.jpg'
---

<div>   
当第三方服务收集各种人的信息，并利用这些信息帮助在其他在线用户的海洋中识别他们时，就会发生对用户的在线追踪。这种对特定信息的收集通常被称为"指纹"，攻击者通常利用它来获取用户的信息。今天，研究人员宣布，他们成功地利用WebGL（网络图形库）的优势，为每一颗GPU创建了一个独特的指纹，以此追踪在线用户。<br><br>
 <p>这个漏洞之所以有效，是因为每块硅片在制造时都有自己的变化和独特的特征，就像每个人都有一个独特的指纹一样。即使在确切的处理器型号中，硅料的差异也使每个产品与众不同，这就是为什么你不能将每一枚处理器超频到相同的频率，所谓芯片“体质”存在差异的原因。</p><p><a href="https://static.cnbetacdn.com/article/2022/0201/feb4a9ee42344e7.jpg" target="_blank"><img src="https://static.cnbetacdn.com/thumb/article/2022/0201/feb4a9ee42344e7.jpg" title alt="IPUMe69IaDQgMaCe.jpg" referrerpolicy="no-referrer"></a></p><p>如果有人能精确地探索GPU的差异，并利用这些差异通过这些特征来识别在线用户，会发生什么？这正是创建DrawnApart的研究人员所想到的。使用WebGL，他们运行了一个GPU工作负载，在16个数据收集处识别了超过176个测量值。这是在GLSL（OpenGL着色语言）中使用顶点操作完成的，工作负载被阻止在处理单元的网络上随机分布。</p><p>DrawnApart可以测量和记录完成顶点渲染的时间，记录渲染的确切路线，处理停滞功能，以及更多。这使得该框架能够发出独特的数据组合，变成GPU的指纹，可以在线利用。在下面的图中你可以看到两个GPU（相同型号）的数据跟踪记录，从中可以显示出变化。</p><p><a href="https://static.cnbetacdn.com/article/2022/0201/725ed3817138e69.jpg" target="_blank"><img src="https://static.cnbetacdn.com/thumb/article/2022/0201/725ed3817138e69.jpg" title alt="lkbw2ums0Ko9jT6N.jpg" referrerpolicy="no-referrer"></a></p><p>WebGL API的创造者Khronos Group已经成立了一个工作小组来处理这种情况，并防止API泄露过多的信息来在线追踪用户。如果你想了解更多关于这项技术的信息，你可以在ArXiv上阅读更多细节：</p><p><a href="https://arxiv.org/pdf/2201.09956.pdf" _src="https://arxiv.org/pdf/2201.09956.pdf" target="_blank">https://arxiv.org/pdf/2201.09956.pdf</a><br></p>   
</div>
            