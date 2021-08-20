
---
title: 'Intel XeSS超采样技术揭秘：性能提升最高2倍、完全开源'
categories: 
 - 新媒体
 - 快科技（原驱动之家）
 - 最新新闻
headimg: 'https://img1.mydrivers.com/img/20210820/s_a97cd5387b904786b2c8b69ebf610c73.png'
author: 快科技（原驱动之家）
comments: false
date: Fri, 20 Aug 2021 18:58:09 GMT
thumbnail: 'https://img1.mydrivers.com/img/20210820/s_a97cd5387b904786b2c8b69ebf610c73.png'
---

<div>   
<p>Intel终于向高性能游戏显卡市场宣战了！</p>
<p><a class="f14_link" href="https://news.mydrivers.com/1/777/777617.htm" target="_blank">全新的Xe HPG微架构来势汹汹</a>，各种该有的技术特性都不缺，尤其是也支持硬件光追，而且一如NVIDIA DLSS、AMD FSR，也有自己的超采样技术，命名为XeSS，虽是后来者，却颇有博采众长的架势。</p>
<p>超采样技术诞生的初衷是弥补开启光追之后带来的性能大幅下滑，从而兼顾高帧率、高画质，当然它也可以脱离光追单独存在，让中低端显卡也能在画质、性能上媲美高端显卡，不用再为了速度而过于牺牲画面。</p>
<p align="center"><a href="https://img1.mydrivers.com/img/20210820/a97cd5387b904786b2c8b69ebf610c73.png" target="_blank"><img alt="Intel XeSS超采样技术揭秘：性能提升最高2倍、完全开源" h="337" src="https://img1.mydrivers.com/img/20210820/s_a97cd5387b904786b2c8b69ebf610c73.png" style="border: black 1px solid;" w="600" referrerpolicy="no-referrer"></a></p>
<p><strong>Intel XeSS的实现流程有些类似NVIDIA DLSS 2.x版本，使用深度学习来合成非常接近原生高分辨率渲染质量的图像，结合空间数据(相邻像素)、时间数据(前一帧运动矢量)，然后反馈给预先训练的神经网络，重建子像素细节，对帧画面进行缩放优化。</strong></p>
<p>官方称，<strong><span style="color:#ff0000;">得益于升级的AI辅助放大功能，最高还可以将性能提高2倍之多。</span></strong></p>
<p style="text-align: center;"><a href="https://img1.mydrivers.com/img/20210820/c06b14ff30ae4ff098e184ebe17fe9d7.png" style="text-align: -webkit-center;" target="_blank"><img alt="Intel XeSS超采样技术揭秘：性能提升最高2倍、完全开源" h="337" src="https://img1.mydrivers.com/img/20210820/s_c06b14ff30ae4ff098e184ebe17fe9d7.png" style="border: 1px solid black;" w="600" referrerpolicy="no-referrer"></a></p>
<p>XeSS有两种实现途径，<strong>一是基于Xe HPG架构新增的XMX矩阵引擎，或者叫矩阵数学单元</strong>，它们是专门用来处理矩阵、张量操作的，每个每时钟周期可处理1024位，可以是64个FP16操作，也可以是128个INT8操作。</p>
<p><strong>另一种则不依赖特定硬件，而是使用DP4a指令</strong>(4元素矢量点积)，Intel、AMD、NVIDIA基本所有的GPU都支持它，包括集成显卡，因此在竞品平台上也能用。</p>
<p>当然，这种软性操作的画面质量肯定不如基于XMX硬件的，但官方称依然明显强于传统缩放算法。</p>
<p style="text-align: center;"><a href="https://img1.mydrivers.com/img/20210820/116b6e96676a4bf9a2a6d66217ed3c06.jpg" style="text-align: -webkit-center;" target="_blank"><img alt="Intel XeSS超采样技术揭秘：性能提升最高2倍、完全开源" h="337" src="https://img1.mydrivers.com/img/20210820/s_116b6e96676a4bf9a2a6d66217ed3c06.jpg" style="border: 1px solid black;" w="600" referrerpolicy="no-referrer"></a></p>
<p>这是Intel放出的XeSS效果对比图，使用尚未发布的Xe HPG DG2 Alchemist独立显卡完成，基于XMX硬件加速。</p>
<p>可以看到，<strong>XeSS 4K画面在2倍放大后依然可圈可点，虽然不如原生4K那么惊喜，但也非常接近了，同时远超1080p画质，尤其是注意中间的文字部分，1080p下完全不可见，XeSS则已经可以完全分辨出来。</strong></p>
<p style="text-align: center;"><a href="https://img1.mydrivers.com/img/20210820/6241bcfb8b124dc9929870b421d0b3d1.png" style="text-align: -webkit-center;" target="_blank"><img alt="Intel XeSS超采样技术揭秘：性能提升最高2倍、完全开源" h="337" src="https://img1.mydrivers.com/img/20210820/s_6241bcfb8b124dc9929870b421d0b3d1.png" style="border: 1px solid black;" w="600" referrerpolicy="no-referrer"></a></p>
<p>一如AMD FSR，<strong><span style="color:#ff0000;">Intel XeSS也将开源开放</span></strong>，更能吸引开发者。</p>
<p><strong>XeSS SDK开发包将在本月内提供，初期是XMX版本，今年晚些时候推出DP4a版本。</strong></p>
<p align="center"><a href="https://img1.mydrivers.com/img/20210820/efb36155868f40b1942db160a3a5e470.jpg" target="_blank"><img alt="Intel XeSS超采样技术揭秘：性能提升最高2倍、完全开源" h="400" src="https://img1.mydrivers.com/img/20210820/s_efb36155868f40b1942db160a3a5e470.jpg" style="border: black 1px solid;" w="600" referrerpolicy="no-referrer"></a></p>

           
           
<p class="end"> - THE END -</p> 
          <p class="zhuanzai">转载请注明出处：快科技</p>  
 <p class="bqian"><a href="https://news.mydrivers.com/tag/intel.htm"><i>#</i>Intel</a><a href="https://news.mydrivers.com/tag/xianka.htm"><i>#</i>显卡</a></p>
<p class="url">
     
<span>责任编辑：上方文Q</span>
</p>
        
</div>
            