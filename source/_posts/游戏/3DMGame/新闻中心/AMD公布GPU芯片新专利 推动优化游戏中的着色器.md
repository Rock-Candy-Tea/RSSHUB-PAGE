
---
title: 'AMD公布GPU芯片新专利 推动优化游戏中的着色器'
categories: 
 - 游戏
 - 3DMGame
 - 新闻中心
headimg: 'https://img.3dmgame.com/uploads/images/news/20220710/1657400576_757712.jpg'
author: 3DMGame
comments: false
date: Sat, 09 Jul 2022 21:05:00 GMT
thumbnail: 'https://img.3dmgame.com/uploads/images/news/20220710/1657400576_757712.jpg'
---

<div>   
<p style="text-indent:2em;">
AMD最近公布了一项专利，将渲染的负载分散到多个GPU芯片组中。这样一来，一个游戏场景将被划分为单独的块，并分配给小芯片，以优化游戏中着色器的利用率。AMD公司公布的新专利为该公司计划在未来几年内利用下一代GPU和CPU技术的用途开拓了更多思路。
</p>
<p align="center">
<img src="https://img.3dmgame.com/uploads/images/news/20220710/1657400576_757712.jpg" alt="AMD公布GPU芯片新专利 推动优化游戏中的着色器" referrerpolicy="no-referrer">
</p>
<p style="text-indent:2em;">
在六月底，AMD有五十四项专利申请被披露。目前还不知道在公布的五十多项专利中，哪些将在AMD的计划中得到利用。专利中讨论的应用详细说明了该公司在接下来几年的做法。
</p>
<p style="text-indent:2em;">
社区成员@ETI1120在ComputerBase网站上注意到的一项申请，专利号为US20220207827，讨论了关键的图像数据分两个阶段，将来自GPU的渲染负载有效地传递到许多小芯片上。CPU方面技术最初是在去年年底向美国专利局申请的。
</p>
<p align="center">
<img src="https://img.3dmgame.com/uploads/images/news/20220710/1657400706_509415.jpg" alt="AMD公布GPU芯片新专利 推动优化游戏中的着色器" referrerpolicy="no-referrer">
</p>
<p style="text-indent:2em;">
当GPU上的图像数据通过标准手段被光栅化时，着色器单元，也被称为ALU会执行相同的任务，并为单个像素分配一个颜色名称。反过来，在特定游戏场景中的特定像素处发现的纹理多边形被直接映射到像素上。最后，制定的任务将保持非典型的原则，只通过位于不同像素的其他纹理进行区别。这种方法被称为SIMD，即单指令-多数据。
</p>
<p style="text-indent:2em;">
对于目前的大多数游戏来说，着色并不是GPU所承担的唯一任务。相反，在最初的着色之后，还包括几个后续的处理步骤。例如，GPU将添加的动作是抗锯齿、阴影和游戏环境的遮挡。然而，光线追踪是与着色同时进行的，创造了一种新的计算方法。
</p>
<p align="center">
<img src="https://img.3dmgame.com/uploads/images/news/20220710/1657400715_374184.jpg" alt="AMD公布GPU芯片新专利 推动优化游戏中的着色器" referrerpolicy="no-referrer">
</p>
<p style="text-indent:2em;">
当GPU控制并处理当前游戏中的图形时，计算机所产生的负载被成倍地增加到成千上万的计算单元。
</p>
<p style="text-indent:2em;">
在GPU处理的游戏中，这种计算负荷以相对理想的方式被扩展到几千个计算单元。这与处理器的不同之处在于，应用程序必须专门编写以增加更多的核心处理。CPU调度器创造了这个动作，将来自GPU的工作分割成更容易分解的任务，供应给计算单元处理，这被称为分档。游戏中的图像被渲染，然后被分成独立的块，这些块包含设定的像素数量。该块由图形处理器的一个子单元计算，然后在那里同步和创建。在这个动作之后，等待计算的像素被包含在一个块中，直到最终使用显卡的子单元。AMD在设计过程中对着色器的计算能力、内存带宽和高速缓存的大小都进行了全盘考虑。
</p>
<p style="text-indent:2em;">
AMD在专利中解释说，在GPU的不同步骤之间分割和连接要求进行彻底和完整的数据连接，这就带来了一个问题。不处于芯片上的数据链接具有较高的延迟水平，导致该过程较慢。
</p>
<p style="text-indent:2em;">
CPU已经毫不费力地实现了向芯片的这种过渡，因为它能够同时几个核心上发送任务，使其可用于芯片。GPU没有提供同样的灵活性，其调度器还只能与入门的双核处理器相提并论。
</p>
<p align="center">
<img src="https://img.3dmgame.com/uploads/images/news/20220710/1657400735_244526.jpg" alt="AMD公布GPU芯片新专利 推动优化游戏中的着色器" referrerpolicy="no-referrer">
</p>
<p align="center">
<img src="https://img.3dmgame.com/uploads/images/news/20220710/1657400735_495192.jpg" alt="AMD公布GPU芯片新专利 推动优化游戏中的着色器" referrerpolicy="no-referrer">
</p>
<p style="text-indent:2em;">
AMD认识到了这一需求，并试图通过改变光栅化的管道，在几个GPU小芯片之间发送任务，类似于CPU，来对这些问题做出处理。这需要先进的分层技术，该公司正在引入"两级分层"，也被称为"混合分层"。分层被处理成两个独立的阶段，而不是直接处理成逐个像素块。第一步是计算方程，取对应三维环境，从原始图像中创建一个二维图像。这个阶段被称为顶点着色，在光栅化之前完成，这个过程在GPU的第一个芯片上相对简短的。一旦完成，游戏场景开始被分档，并交由不同的芯片处理，然后，栅格化和后期处理等常规任务就可以开始了。
</p>          
</div>
            