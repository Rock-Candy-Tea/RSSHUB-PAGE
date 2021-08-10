
---
title: '1张GPU就能让静态图片变gif'
categories: 
 - 新媒体
 - 快科技（原驱动之家）
 - 最新新闻
headimg: 'https://img1.mydrivers.com/img/20210810/b7ad6b318cb041f2acfb60e0e3c434d7.gif'
author: 快科技（原驱动之家）
comments: false
date: Tue, 10 Aug 2021 14:03:46 GMT
thumbnail: 'https://img1.mydrivers.com/img/20210810/b7ad6b318cb041f2acfb60e0e3c434d7.gif'
---

<div>   
<p>自打伯克利和谷歌联合打造的NeRF横空出世，江湖上静态图变动图的魔法就风靡开来。</p>
<p align="center"><img alt="1张GPU就能让静态图片变gif" h="320" src="https://img1.mydrivers.com/img/20210810/b7ad6b318cb041f2acfb60e0e3c434d7.gif" style="border: black 1px solid;" w="320" referrerpolicy="no-referrer"></p>
<p>不过，想要像这样依靠AI来简化3D动态效果的制作，算力开销可不小：</p>
<p>以NeRF为例，想要在1440 x 1600像素、90Hz的VR头盔中实现实时渲染，需要37 petaFLOPS（每秒10^15次浮点运算）的算力——这在目前的GPU上根本不可能实现。</p>
<p>怎么降低点计算复杂度？</p>
<p>现在，来自奥地利格拉兹科技大学和Facebook的研究人员，就想出一招：引入真实深度信息。</p>
<p>就这一下，很快的，推理成本最高能降低48倍，并且只用1个GPU，就能以每秒20帧的速度实现交互式渲染。</p>
<p>画质什么的，也没啥影响，甚至还能有所提升：</p>
<p align="center"><img alt="1张GPU就能让静态图片变gif" h="405" src="https://img1.mydrivers.com/img/20210810/95f04ab633994a40aee418b77f03fa32.gif" style="border: 1px solid black; width: 600px;" w="720" referrerpolicy="no-referrer"></p>
<p>具体是怎样一招，咱们往下接着聊。</p>
<p>基于深度预言网络的NeRF</p>
<p>首先需要说明的是，NeRF，即神经辐射场（neural radiance field）方法，是沿相机射线采样5D坐标，来实现图像合成的。</p>
<p align="center"><img alt="1张GPU就能让静态图片变gif" h="324" src="https://img1.mydrivers.com/img/20210810/f0f64341f25c422ab9d02ca964fc51b9.gif" style="border: 1px solid black; width: 600px;" w="639" referrerpolicy="no-referrer"></p>
<p>也就是说，在NeRF的渲染过程中，需要对每条射线都进行网络评估，以输出对应的颜色和体积密度值等信息。</p>
<p>这正是造成NeRF在实时渲染应用中开销过大的主要原因。</p>
<p>而现在，格拉兹科技大学和Facebook的研究人员发现，引入真实深度信息，只考虑物体表面周围的重要样本，每条视图射线（view ray）所需的样本数量能够大大减少，并且不会影响到图像质量。</p>
<p>基于此，他们提出了DONeRF。</p>
<p style="text-align: center"><a href="https://img1.mydrivers.com/img/20210810/20502e6d-53da-419f-9d58-d9cea969e2f0.png" target="_blank"><img alt="1张GPU就能让静态图片变gif" h="135" src="https://img1.mydrivers.com/img/20210810/S20502e6d-53da-419f-9d58-d9cea969e2f0.png" style="border: black 1px solid" w="600" referrerpolicy="no-referrer"></a></p>
<p>DONeRF由两个网络组成，其一，是Sampling Oracle Network，使用分类法来预测沿视图射线的最佳采样位置。</p>
<p>具体来说，这个深度预言网络通过将空间沿射线离散化，并预测沿射线的采样概率，来预测每条射线上的多个潜在采样对象。</p>
<p>如下图所示，3个颜色通道编码了沿射线的3种最高采样概率，灰度值表明其中可能只有一个表面需要被采样，而彩色数值则表明这些样本需要在深度上展开。</p>
<p style="text-align: center"><a href="https://img1.mydrivers.com/img/20210810/6d81ce33-6e7e-4685-8bf0-93d28d82d1c2.png" target="_blank"><img alt="1张GPU就能让静态图片变gif" h="204" src="https://img1.mydrivers.com/img/20210810/S6d81ce33-6e7e-4685-8bf0-93d28d82d1c2.png" style="border: black 1px solid" w="600" referrerpolicy="no-referrer"></a></p>
<p>其二，是一个着色网络，使用类似于NeRF的射线行进累积法来提供RGBA输出。</p>
<p>为了消除输入的模糊性，研究人员还将射线转换到了一个统一的空间，并使用非线性采样来追踪接近的区域。</p>
<p>另外，在两个网络之间，研究人员对局部采样进行扭曲，以使着色网络的高频预测被引导到前景上。</p>
<p style="text-align: center"><a href="https://img1.mydrivers.com/img/20210810/032f32dd-6acf-4ecd-b0c3-e7ba45b61946.png" target="_blank"><img alt="1张GPU就能让静态图片变gif" h="289" src="https://img1.mydrivers.com/img/20210810/S032f32dd-6acf-4ecd-b0c3-e7ba45b61946.png" style="border: black 1px solid" w="600" referrerpolicy="no-referrer"></a></p>
<p>本文还引入了视图单元（view cell）的概念。一个视图单元被定义为一个具有主要方向和最大视角的边界框。</p>
<p>简单来说，这个边界框能够捕捉到所有源于框内、并且在一定旋转范围内的视图射线。</p>
<p>利用这样的方法，就可以对大场景进行分割，解决NeRF没有办法应用于大场景的问题。</p>
<p>此外，较小的视图单元减少了场景中的可见内容，因此可能会进一步提高成像质量。</p>
<p>对比结果</p>
<p>所以，DONeRF相较于前辈NeRF，到底能快多少?</p>
<p>不妨直接来看对比结果。</p>
<p align="center"><img alt="1张GPU就能让静态图片变gif" h="360" src="https://img1.mydrivers.com/img/20210810/7077551a6f2947f5bf1f2421b607a93e.gif" style="border: 1px solid black; height: 338px; width: 600px;" w="640" referrerpolicy="no-referrer"></p>
<p>在相似的质量下，NeRF总共使用了256个样本。而DONeRF只用到了4个样本，在速度上可以实现20-48倍的提升。</p>
<p>并且在成像细节方面，DONeRF的图像边缘更为清晰。</p>
<p style="text-align: center"><a href="https://img1.mydrivers.com/img/20210810/24abb3b4-7a9a-4826-9524-2ab7c85f5e3d.png" target="_blank"><img alt="1张GPU就能让静态图片变gif" h="385" src="https://img1.mydrivers.com/img/20210810/S24abb3b4-7a9a-4826-9524-2ab7c85f5e3d.png" style="border: black 1px solid" w="600" referrerpolicy="no-referrer"></a></p>
<p>研究人员还指出，在16个样本的情况下，从峰值信噪比（PSNR）来看，几乎所有场景中DONeRF都超越了NeRF。</p>
<p style="text-align: center"><a href="https://img1.mydrivers.com/img/20210810/0b2d100c-17c9-4e89-823c-32222288620d.png" target="_blank"><img alt="1张GPU就能让静态图片变gif" h="321" src="https://img1.mydrivers.com/img/20210810/S0b2d100c-17c9-4e89-823c-32222288620d.png" style="border: black 1px solid" w="600" referrerpolicy="no-referrer"></a></p>
<p>传送门</p>
<p>论文地址：https://arxiv.org/abs/2103.03231</p>
<p>项目地址：https://depthoraclenerf.github.io/</p>

           
           
<p class="end"> - THE END -</p> 
            
 <p class="bqian"><a href="https://news.mydrivers.com/tag/tupian.htm"><i>#</i>图片</a><a href="https://news.mydrivers.com/tag/gpu.htm"><i>#</i>GPU</a></p>
<p class="url">
     <span>原文链接：<a href="https://mp.weixin.qq.com/s/S0CgyNLo4Lvej9CKTj1b_g">量子位</a></span>
<span>责任编辑：随心</span>
</p>
        
</div>
            