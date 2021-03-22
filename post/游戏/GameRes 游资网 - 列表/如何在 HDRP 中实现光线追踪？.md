
---
title: '如何在 HDRP 中实现光线追踪？'
categories: 
    - 游戏
    - GameRes 游资网 - 列表
author: GameRes 游资网 - 列表
comments: false
date: Mon, 08 Feb 2021 00:00:00 GMT
thumbnail: 'https://di.gameres.com/attachment/forum/202102/08/140532zq80usj9tojuqtz4.jpg'
---

<div>   
<table cellspacing="0" cellpadding="0"><tbody><tr><td class="t_f" id="postmessage_2484804">
在光照中，“光线追踪”是指从摄影机或表面向其他表面或光照模型（尤其是摄像机视图外）射出光束来形成光照。该技术庞大的计算量使其仅在电影制片和高端可视化领域有广泛的应用，但是在实时内容创作上一直被帧数限制。数年来游戏使用了另一种方法替代光线追踪，即光栅化。简单来说，光栅化就是渲染屏幕像素受特定光照的影响，实际本身并不涉及光线追踪的概念，且由于其屏幕空间的本质而有一定的局限。<br>
<br>
幸而，随着主流GPU的更新迭代，由硬件支撑的光线追踪逐渐普及，光追可能很快就会成为生成光照的新标准（尤其是在高端平台上）。而高清渲染管线（HDRP）则推出了一种糅合传统光栅化与光线追踪技术的混合光线追踪管线，并用光线追踪重现了诸如环境光遮蔽（AO）、光反射、全局光照（GI）、次表面散射和阴影等常见光效。<br>
<br>
<div align="center">
<img id="aimg_959545" aid="959545" zoomfile="https://di.gameres.com/attachment/forum/202102/08/140532zq80usj9tojuqtz4.jpg" data-original="https://di.gameres.com/attachment/forum/202102/08/140532zq80usj9tojuqtz4.jpg" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202102/08/140532zq80usj9tojuqtz4.jpg" referrerpolicy="no-referrer">
</div><br>
<div align="center">
<img id="aimg_959546" aid="959546" zoomfile="https://di.gameres.com/attachment/forum/202102/08/140533bsqzgzfcpqp31rpf.jpg" data-original="https://di.gameres.com/attachment/forum/202102/08/140533bsqzgzfcpqp31rpf.jpg" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202102/08/140533bsqzgzfcpqp31rpf.jpg" referrerpolicy="no-referrer">
</div><br>
<div align="center">
<img id="aimg_959547" aid="959547" zoomfile="https://di.gameres.com/attachment/forum/202102/08/140533zluzhhd58nbnl5db.jpg" data-original="https://di.gameres.com/attachment/forum/202102/08/140533zluzhhd58nbnl5db.jpg" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202102/08/140533zluzhhd58nbnl5db.jpg" referrerpolicy="no-referrer">
</div><br>
以上图和视频为宝马2019款8系双门轿跑车展示，这是Unity、NVIDIA和宝马三方的合作成果。视频中，实景拍摄和光线追踪渲染的无缝融合产生了不可思议的效果，证明了实时光线跟踪技术在耗时、成本远低于离线渲染的前提下，也能制作出极度逼真的图像。<br>
<strong><font color="#de5650"><br>
</font></strong><br>
<strong><font color="#de5650">用全新的 HDRP 模板实现光线追踪</font></strong><br>
<br>
Unity 2020.2 推出了全新的 HDRP 模板，我们之前也介绍过该模板，感兴趣的朋友点击这里回顾。<br>
<br>
建议大家下载 Unity 2020.2，在 Unity Hub 中创建新项目，选择 HDRP 模板，然后点击Create。<br>
<br>
<div align="center">
<img id="aimg_959548" aid="959548" zoomfile="https://di.gameres.com/attachment/forum/202102/08/140534z7nkhv724lzzl6p6.jpg" data-original="https://di.gameres.com/attachment/forum/202102/08/140534z7nkhv724lzzl6p6.jpg" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202102/08/140534z7nkhv724lzzl6p6.jpg" referrerpolicy="no-referrer">
</div><br>
全新的 HDRP 模板借助了光栅化技术来渲染光照，使用了光照烘焙、光照探针组、反射探针、阴影贴图等功能。本文将介绍 HDRP 中 4 种主要的光线追踪效果，即光线追踪环境光遮挡（Ambient Occlusion）、光反射（Reflection）、全局光照（Global Illumination）和阴影（Shadow）。最后，介绍 HDRP 的路径追踪（Path Tracing）功能，路径追踪是更为简单粗暴的光追计算方法，通过延长渲染时间，来换取更高的图像保真度。 <br>
<br>
<strong><font color="#de5650">光线追踪环境光遮蔽（RTAO）</font></strong><br>
<br>
十多年来，屏幕空间环境光遮蔽（SSAO）一直是游戏实时渲染的主要内容，用于模拟环境的漫射光遮蔽，改善场景中物体接触区域的视觉效果，降低凹面区域的光照强度。但是效果如果强度过高，则会在几何体周围产生光晕，甚至产生卡通化外观。除此之外，它还继承了屏幕空间技术的主要缺点，即无法根据屏幕外对象生成遮蔽效果，仅能使用 z-buffer（z轴缓存）中出现的深度信息。但在优点上， SSAO 在处理摄像机内的小区域光遮挡时依然出色，并且成本相对较低。<br>
<br>
<div align="center">
<img id="aimg_959549" aid="959549" zoomfile="https://di.gameres.com/attachment/forum/202102/08/140535zsktcce8kfsnuns8.gif" data-original="https://di.gameres.com/attachment/forum/202102/08/140535zsktcce8kfsnuns8.gif" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202102/08/140535zsktcce8kfsnuns8.gif" referrerpolicy="no-referrer">
</div><div align="center"><font size="2"><font color="#708090">图例：三种情况下的环境光遮蔽对比</font></font></div><br>
在光线追踪的帮助下，位于摄像机视锥外的光线也能被拍摄进画面，让光线照射到画面外的物体，从而让摄像机内的大型物体<font color="#ff0000">生成出色的宏观遮挡效果。</font>尽管从技术上讲，AO只能勉强算作一种环境光照技术，但它能很好地补充光照贴图、光探针等其它光照，后者较低分辨率及效果强度并不足以生成微型光遮蔽。<br>
<br>
<strong><font color="#de5650">光线追踪光反射（RTR）</font></strong><br>
<br>
与 SSAO 类似，屏幕空间光反射（SSR）也只能反射画面中的物体，出于摄像机镜头外的表面并不能反射光。比方说，摄像机视角对着地面时，SSR技术将不能生成任何光照信息。因此，SSR 的效果多少会有偏差，且会受到多种因素干扰，甚至受你自己干扰：在大部分静态场景中，位置恰当的反射探针才能产生悦目的效果、减少干扰因素。不过 SSR 真正有用的地方在于视线平行方向上的镜面反射（如地板、墙壁和天花板）。SSR 最为理想的使用方法是用在视角固定的摄像机中，比如赛车游戏。<br>
<br>
<div align="center">
<img id="aimg_959550" aid="959550" zoomfile="https://di.gameres.com/attachment/forum/202102/08/140535ivt9wbjnmcrjiwj4.gif" data-original="https://di.gameres.com/attachment/forum/202102/08/140535ivt9wbjnmcrjiwj4.gif" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202102/08/140535ivt9wbjnmcrjiwj4.gif" referrerpolicy="no-referrer">
</div><div align="center"><font size="2"><font color="#708090">图例：光栅化与光线追踪的光反射对比</font></font></div><br>
但有了光线追踪后，我们就能<font color="#ff0000">获取屏幕外的光照信息</font>，并借此在整个世界上，或在镜头周围一定半径内生成更精确的光反射，根据 Light Cluster（光照集群）和光线照射距离来生成光照效果。<br>
<br>
<strong><font color="#de5650">光线追踪全局光照（RTGI）</font></strong><br>
<br>
光线跟踪最具代表性的功能之一是<font color="#ff0000">实时全局光照</font>，即用射出的光线生成间接光照，再简单点说，就是让光照在环境中弹射。<br>
<br>
通常在游戏引擎中，间接光照是使用提前计算或烘焙技术来处理的，包括光照探针、光照贴图，但技术的缺陷在于运算耗时会增加场景光照的迭代时间。<br>
<br>
<div align="center">
<img id="aimg_959551" aid="959551" zoomfile="https://di.gameres.com/attachment/forum/202102/08/140536e6bofaaftuelbhkh.gif" data-original="https://di.gameres.com/attachment/forum/202102/08/140536e6bofaaftuelbhkh.gif" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202102/08/140536e6bofaaftuelbhkh.gif" referrerpolicy="no-referrer">
</div><div align="center"><font size="2"><font color="#708090">图例：光栅化与光线追踪的全局光照对比</font></font></div><br>
HDRP 推出了两种 RTGI 技术：高性能和高质量。前者适用于在直射光下实现高帧率，而后者则能处理光线的多次反射和采样，可在复杂室内环境中生成精确的光效，当然运算成本也非常高。<br>
<br>
<strong><font color="#de5650">光线追踪阴影</font></strong><br>
<br>
HDRP 自带精美的阴影效果，在阴影过滤质量为高时（PCSS），管线生成的贴图可模拟自然的阴影柔顺感，保证阴影在投影物体周围的锐度，模仿真实阴影。然而当过滤质量为中等时，结果就不尽人意了，整张阴影贴图均会被无差别过滤，投影物体和接收物体间的距离将不能影响效果。<br>
<br>
<div align="center">
<img id="aimg_959552" aid="959552" zoomfile="https://di.gameres.com/attachment/forum/202102/08/140536d1e8xwpw8ugwxwaz.gif" data-original="https://di.gameres.com/attachment/forum/202102/08/140536d1e8xwpw8ugwxwaz.gif" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202102/08/140536d1e8xwpw8ugwxwaz.gif" referrerpolicy="no-referrer">
</div><div align="center"><font size="2"><font color="#708090">图例：光栅化与光线追踪的阴影对比</font></font></div><br>
光线追踪阴影可以显着改善阴影效果。通过从表面向光照投射射线，来计算出两者间的遮挡面积，由此生成的阴影非常逼近现实，而性能成本并不算高。此外，HDRP还支持透明表面的阴影！<br>
<br>
<strong><font color="#de5650">路径追踪</font></strong><br>
<br>
光线路径追踪功能较传统离线渲染可更快地生成精美图像。光线从摄像机射出，在碰撞到表面时，再向其他表面和光照投射光线（形成光照集群‘Light Cluster’结构）。光线从摄像机到灯光间的行程称为路径，功能由此得名路径追踪。<br>
<br>
<div align="center">
<img id="aimg_959553" aid="959553" zoomfile="https://di.gameres.com/attachment/forum/202102/08/140538vwjbfowwcrbzraxw.gif" data-original="https://di.gameres.com/attachment/forum/202102/08/140538vwjbfowwcrbzraxw.gif" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202102/08/140538vwjbfowwcrbzraxw.gif" referrerpolicy="no-referrer">
</div><br>
与其他光线追踪方法相比，路径追踪的优势在于能用<font color="#ff0000">统一的运算流程来生成所有光照</font>，包括阴影、反射、折射和全局光照。该技术的主要缺点在于渲染时间和图像噪波，后者可以通过累积采样多帧图像来推算出更为清晰的图像（类似时域化抗锯齿）。<br>
<br>
在此提醒一下各位朋友，目前 HDRP 中的光线追踪处于预览阶段，并不能满足商业制作要求，各位在创作的时候请务必做好备份。同时，也欢迎各位提出宝贵的建议。<br>
<br>
<font size="2"><font color="#708090">来源：Unity</font></font><br>
<font size="2"><font color="#708090">地址：https://mp.weixin.qq.com/s/vPKBGOA_vxcHVH5TP2Hoqg</font></font><br>
<br>
</td></tr></tbody></table>



  
</div>
            