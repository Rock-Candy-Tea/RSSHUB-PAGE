
---
title: 'AMD FSR画质技术正式开源：NVIDIA_Intel都能用'
categories: 
 - 新媒体
 - 快科技（原驱动之家）
 - 最新新闻
headimg: 'https://img1.mydrivers.com/img/20210716/s_0b4531aaa38c49c7becc21206b53ffa4.png'
author: 快科技（原驱动之家）
comments: false
date: Fri, 16 Jul 2021 02:31:11 GMT
thumbnail: 'https://img1.mydrivers.com/img/20210716/s_0b4531aaa38c49c7becc21206b53ffa4.png'
---

<div>   
<p>6月底，AMD正式发布了FSR画质缩放技术，中文称为超分辨率锐画，走了一条和NVIDIA DLSS不同的技术路线，而且承诺会在7月中旬开源。</p>
<p>现在，<strong><span style="color:#ff0000;">AMD兑现承诺，FSR技术的源代码、开发文档、实例都已经放在了AMD GPUOpen网站上</span></strong>，开发者可以直接用于他们的游戏。</p>
<p>AMD目前提供的实例支持DX12、Vulkan，但保证说编译着色器也兼容DX11。</p>
<p align="center"><a href="https://img1.mydrivers.com/img/20210716/0b4531aaa38c49c7becc21206b53ffa4.png" target="_blank"><img alt="AMD FSR画质技术正式开源：NVIDIA/Intel都能用" h="399" src="https://img1.mydrivers.com/img/20210716/s_0b4531aaa38c49c7becc21206b53ffa4.png" style="border: black 1px solid;" w="600" referrerpolicy="no-referrer"></a></p>
<p>AMD还表示，FSR技术不像NVIDIA DLSS那样依赖于运动向量(Motion Vector)或者历史缓冲区(History Buffer)，因此不需要专门的Tensor核心来加速，但<strong>同样也能使用时间数</strong>据，只是现阶段FSR的重心是简化开发、快速推向市场，技术上会逐步深入增强。</p>
<p style="text-align: center;"><a href="https://img1.mydrivers.com/img/20210716/98bf6adb114c4338afaac680c085e8c0.jpg" style="text-align: -webkit-center;" target="_blank"><img alt="AMD FSR画质技术正式开源：NVIDIA/Intel都能用" h="337" src="https://img1.mydrivers.com/img/20210716/s_98bf6adb114c4338afaac680c085e8c0.jpg" style="border: 1px solid black;" w="600" referrerpolicy="no-referrer"></a></p>
<p>AMD在开发文档中详细列举了<strong>FSR的画质/性能模式、缩放比例、输入分辨率、输出分辨率、驱动过载时间</strong>(0.2-1.0ms/显卡越高端越短)。</p>
<p align="center"><a href="https://img1.mydrivers.com/img/20210716/ec24c26870e44356be04a28f606487cd.jpg" target="_blank"><img alt="AMD FSR画质技术正式开源：NVIDIA/Intel都能用" h="337" src="https://img1.mydrivers.com/img/20210716/s_ec24c26870e44356be04a28f606487cd.jpg" style="border: 1px solid black;" w="600" referrerpolicy="no-referrer"></a></p>
<p align="center"><a href="https://img1.mydrivers.com/img/20210716/1d11f4105ca343a5a96454a8a9694d40.jpg" target="_blank"><img alt="AMD FSR画质技术正式开源：NVIDIA/Intel都能用" h="337" src="https://img1.mydrivers.com/img/20210716/s_1d11f4105ca343a5a96454a8a9694d40.jpg" style="border: 1px solid black;" w="600" referrerpolicy="no-referrer"></a></p>
<p>支持设备方面，<strong><span style="color:#ff0000;">FSR的兼容性非常好，AMD RX 6000、RX 5000、RX Vega、RX 500、RX 400系列全都可以，而且支持NVIDIA RTX 30、RTX 20、GTX 10、GTX 9系列，Intel UHD系列。</span></strong></p>
<p>但注意在显卡上走的是半精度FP16浮点模式，RX 500、RX 400、GTX 9系列则回退到单精度FP32。</p>
<p style="text-align: center;"><a href="https://img1.mydrivers.com/img/20210716/34e911f4b23d4be5937174aa9d2ce312.jpg" style="text-align: -webkit-center;" target="_blank"><img alt="AMD FSR画质技术正式开源：NVIDIA/Intel都能用" h="337" src="https://img1.mydrivers.com/img/20210716/s_34e911f4b23d4be5937174aa9d2ce312.jpg" style="border: 1px solid black;" w="600" referrerpolicy="no-referrer"></a></p>
<p>FSR技术首发支持<a class="f14_link" href="https://news.mydrivers.com/1/764/764034.htm" target="_blank">19款游戏、44家开发商</a>，现在又新增加了4款游戏，分别是<strong>《生化危机：村庄》、《街机末日》(Arcadegeddon)、《涅克罗蒙达：赏金猎人》(Necromunda Hired Gun)、《永恒边缘》(Edge of Eternity)。</strong></p>
<p>Unity引擎已将发布的2021.2b版本也会支持FSR。</p>
<p>希望后续能有越来越多的大作加入。</p>
<p align="center"><a href="https://img1.mydrivers.com/img/20210716/7cd0fc36b3c44ea29b56f6c0792fd977.jpg" target="_blank"><img alt="AMD FSR画质技术正式开源：NVIDIA/Intel都能用" h="313" src="https://img1.mydrivers.com/img/20210716/s_7cd0fc36b3c44ea29b56f6c0792fd977.jpg" style="border: black 1px solid;" w="600" referrerpolicy="no-referrer"></a></p>
<p align="center"><a href="https://img1.mydrivers.com/img/20210716/38d1f20d8ef74bb99fa22798a5ef2a1f.jpg" target="_blank"><img alt="AMD FSR画质技术正式开源：NVIDIA/Intel都能用" h="337" src="https://img1.mydrivers.com/img/20210716/s_38d1f20d8ef74bb99fa22798a5ef2a1f.jpg" style="border: black 1px solid;" w="600" referrerpolicy="no-referrer"></a></p>

           
           
<p class="end"> - THE END -</p> 
          <p class="zhuanzai">转载请注明出处：快科技</p>  
 <p class="bqian"><a href="https://news.mydrivers.com/tag/amd.htm"><i>#</i>AMD</a><a href="https://news.mydrivers.com/tag/amd_fsr.htm"><i>#</i>AMD FSR</a></p>
<p class="url">
     
<span>责任编辑：上方文Q</span>
</p>
        
</div>
            