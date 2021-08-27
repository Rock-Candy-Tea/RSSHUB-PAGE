
---
title: 'Intel XeSS技术确认支持AMD显卡：RX 6000可用'
categories: 
 - 新媒体
 - cnBeta
 - 最新
headimg: 'https://static.cnbetacdn.com/article/2021/0827/8d071c53b1b7e32.png'
author: cnBeta
comments: false
date: Fri, 27 Aug 2021 12:43:32 GMT
thumbnail: 'https://static.cnbetacdn.com/article/2021/0827/8d071c53b1b7e32.png'
---

<div>   
前不久Intel公布了自家的高性能桌面显卡ARC系列，中文名锐炫，除了升级Xe HPG架构之外，还支持DX12U、光追等等。甚至面对AMD的FSR、NVIDIA的DLSS游戏技术，Intel也有对应的XeSS超采样技术，实现流程有些类似NVIDIA DLSS 2.x版本，使用深度学习来合成非常接近原生高分辨率渲染质量的图像。<br>
 <p>结合空间数据(相邻像素)、时间数据(前一帧运动矢量)，然后反馈给预先训练的神经网络，重建子像素细节，对帧画面进行缩放优化。</p><p><strong>官方称，得益于升级的AI辅助放大功能，最高还可以将性能提高2倍之多。</strong></p><p><img src="https://static.cnbetacdn.com/article/2021/0827/8d071c53b1b7e32.png" referrerpolicy="no-referrer"></p><p><img src="https://static.cnbetacdn.com/article/2021/0827/067eb1874cca064.jpg" referrerpolicy="no-referrer"></p><p>对于XeSS技术，Intel这次也非常大方，保持了技术的开放性，不仅自家的ARC显卡支持，NVIDIA及AMD的显卡也能支持，不过实现方式不同，自家显卡有专用的XMX引擎加速XeSS，其他显卡则是通过DP4a指令实现的。</p><p>现在AMD公司已经确认了，<strong>RDNA2架构的显卡支持DP4a，所以RX 6000系列显卡是可以支持Intel的XeSS技术。</strong></p><p>至于更旧的显卡，虽然不支持DP4a指令集，但FP32、FP16的方式也能运行XeSS，就是性能会慢。</p><p>现在三家显卡厂商中，除了NVIDIA的DLSS限制于自家显卡，<strong>AMD及Intel各自在FSR、XeSS技术上倒是很开放，</strong>其他显卡也能用。</p>   
</div>
            