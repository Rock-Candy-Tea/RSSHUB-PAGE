
---
title: '12代酷睿关闭小核获得性能提升 Intel果断出手封杀'
categories: 
 - 游戏
 - 3DMGame
 - 新闻中心
headimg: 'https://img.3dmgame.com/uploads/images/news/20220102/1641113778_752410.jpg'
author: 3DMGame
comments: false
date: Sun, 02 Jan 2022 08:56:00 GMT
thumbnail: 'https://img.3dmgame.com/uploads/images/news/20220102/1641113778_752410.jpg'
---

<div>   
<p style="text-indent:2em;">
Intel做出一个让人有些诧异的决定，彻底禁用12代酷睿对AVX-512指令集的支持。
</p>
<p style="text-indent:2em;">
据悉，AVX-512也就是AVX3，也就是“高级矢量扩展”，第一代AVX出现于Sandy 
Bridge二代酷睿，第二代AVX2诞生于2011年的四代酷睿(Haswell)，最新的第三代则发布于2013年，最早用于至强产品线，目前已经下放给11代酷睿Rocket 
Lake。
</p>
<p align="center">
<img src="https://img.3dmgame.com/uploads/images/news/20220102/1641113778_752410.jpg" alt="12代酷睿关闭小核获得性能提升 Intel果断出手封杀" referrerpolicy="no-referrer">
</p>
<p style="text-indent:2em;">
简单来说，AVX-512包含一系列可以加速工作负载的指令，包括科学模拟、金融分析、人工智能、深度学习、3D建模、音视频处理器、加密解密、数据压缩等。
</p>
<p style="text-indent:2em;">
虽然外界想当然地认为Alder 
Lake支持AVX-512，且用户发现可以在BIOS中禁用E核来启用AXV-512，但Intel却表示，这样会带来未知错误，将通过微码更新在BIOS中完全封杀掉AVX-512。
</p>
<p style="text-indent:2em;">
显而易见的原因是，12代酷睿Alder 
Lake采用混合架构，小核（E核）Gracemont并不支持AVX-512，为了这一指令集关闭E核的做法，Intel难以接受。
</p>
<p style="text-indent:2em;">
之所以说诡异是因为，IgorLabs测试发现，12代酷睿大核Golden 
Cove开启AVX-512后能效甚至比AVX2还高，这和11代酷睿大相径庭，后者的AVX-512简直电老虎。另外，PS3模拟器RPCS3官方前不久还在社交平台建议12代酷睿用户关闭E核开启P核AVX512指令集，这样可实现游戏帧数大幅提升。
</p>
<p style="text-indent:2em;">
合理的解释应该是，虽然AVX-512开启后的确在某些场景下有加成，可代价是牺牲E核，在Intel看来，还有更多的工作负载需要P核+E核共同参与，这样得不偿失。
</p>
<p style="text-indent:2em;">
显然，如果你当前的主板BIOS还能有开启AVX-512的可能且懂得如何驾驭，那还是暂缓升级BIOS了。
</p>          
</div>
            