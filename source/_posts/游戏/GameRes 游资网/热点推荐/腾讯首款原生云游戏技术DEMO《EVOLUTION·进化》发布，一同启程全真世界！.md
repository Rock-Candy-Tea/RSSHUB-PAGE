
---
title: '腾讯首款原生云游戏技术DEMO《EVOLUTION·进化》发布，一同启程全真世界！'
categories: 
 - 游戏
 - GameRes 游资网
 - 热点推荐
headimg: 'https://di.gameres.com/attachment/forum/202206/29/100058pytpahjasojj2svs.jpg'
author: GameRes 游资网
comments: false
date: Wed, 29 Jun 2022 00:00:00 GMT
thumbnail: 'https://di.gameres.com/attachment/forum/202206/29/100058pytpahjasojj2svs.jpg'
---

<div>   
“原生云游戏，到底是什么样？”<br>
<br>
虽然，原生云游戏，自概念提出至今，该领域仍处于探索阶段。但是，腾讯原生云游戏技术解决方案研发团队，已取得了一定的进展和突破。<br>
<br>
<div align="center">
<img aid="1044389" zoomfile="https://di.gameres.com/attachment/forum/202206/29/100058pytpahjasojj2svs.jpg" data-original="https://di.gameres.com/attachment/forum/202206/29/100058pytpahjasojj2svs.jpg" width="600" id="aimg_1044389" inpost="1" src="https://di.gameres.com/attachment/forum/202206/29/100058pytpahjasojj2svs.jpg" referrerpolicy="no-referrer">
</div><br>
6月27日，“SPARK 2022”腾讯游戏发布会上，随着由START ENGINE制作的原生云游戏技术DEMO《EVOLUTION·进化》压轴全球首曝，原生云游戏的神秘面纱也首次被揭开。<br>
<br>
区别于过往只能观看不能体验的影视大片，在此次全球首曝的原生云游戏技术DEMO《EVOLUTION·进化》中，研发团队通过原生云游戏技术，为玩家打造了一个影视级别、实时交互的体验场景，超精细的恐龙渲染，茂密而真实的树林，让玩家仿佛亲临亿万年前的恐龙时代。<br>
<br>
除此之外，由原生云技术搭建的《EVOLUTION·进化》，天然具有千人同屏体验特性，且无需考虑传统网络游戏需要考虑的复杂同步问题。<br>
<br>
<strong>【实时高精度生物渲染】</strong><br>
<br>
<strong><font color="#de5650">任意距离零瑕疵 为游戏带来影视级的细节表达</font></strong><br>
<br>
由于传统游戏制作管线中没有或者缺少针对生物的细分技术，导致当前很多游戏，在生物渲染上，无法实现接近真实的肌肤质感、纹理、和色泽。<br>
<br>
而START ENGINE提出的实时细分处理方案——能够将影视中的模型细分技术运用到到实时渲染中，同时将这部分压力较大的工作转移到专属卡上执行。最终向玩家呈现出超3A级别的细节画面表现，达到影视级别的效果：<br>
<br>
<ul><li>直接导入影视级别的精细资产，渲染出超高精度的细节</li><li>无需任何预处理，对低精度模型进行实时表面细分</li><li>自适应网格LOD，支持达到原始模型1000倍以上的超高分辨率<br>
</li></ul><br>
<div align="center">
<img aid="1044390" zoomfile="https://di.gameres.com/attachment/forum/202206/29/100059x5ggotqkqfjtbntf.jpg" data-original="https://di.gameres.com/attachment/forum/202206/29/100059x5ggotqkqfjtbntf.jpg" width="600" id="aimg_1044390" inpost="1" src="https://di.gameres.com/attachment/forum/202206/29/100059x5ggotqkqfjtbntf.jpg" referrerpolicy="no-referrer">
</div><br>
<strong>【实时高密度高精度植物渲染】</strong><br>
<br>
<strong><font color="#de5650">“片片”分明   为实时游戏添加影视级真实树木场景</font></strong><br>
<br>
大规模超真实树木群的实时渲染，是目前在游戏制作及图形学研究中，一个重要但难以攻破的问题。究其原因，是高精度树木模型所需的数据量过大，极大地增加了渲染负荷。<br>
<br>
针对此难点，START ENGINE专门开发针对高精度树木群的实时渲染算法——BroadLeaf（实时高密度高精度植物渲染），在保证植物渲染品质的同时，保证其实时性。该算法可以以平均1000的帧率渲染上万颗树，效率远超现有渲染引擎。同时，由START ENGINE渲染的树木树叶，甚至可以实现单片交互。依托云计算平台，BroadLeaf使得实时游戏中添加大规模影视级别树木场景成为可能，极大地提高了游戏场景的丰富度及实时性。<br>
<br>
<div align="center">
<img aid="1044391" zoomfile="https://di.gameres.com/attachment/forum/202206/29/100059yc96yfi363i8lil9.jpg" data-original="https://di.gameres.com/attachment/forum/202206/29/100059yc96yfi363i8lil9.jpg" width="600" id="aimg_1044391" inpost="1" src="https://di.gameres.com/attachment/forum/202206/29/100059yc96yfi363i8lil9.jpg" referrerpolicy="no-referrer">
</div><br>
<strong>【实时动态树木仿真】</strong><br>
<br>
<strong><font color="#de5650">吹拂、弯折、碰撞 让树木也成为可交互内容</font></strong><br>
<br>
在传统制作上，由于算力限制，树木的物理仿真在实时领域，往往需要做非常多的简化才能降低计算量，以满足时效性需求。这也导致了实时领域，树木仿真结果不尽人意。<br>
<br>
START ENGINE利用云端多显卡算力优势，基于GPU加速技术，在原生云游戏中实现了实时的高精度树木仿真。其中，使用了硬件光线追踪技术，进行精确的物理碰撞检测，得到了非常好的效果：当树木与高精度模型进行碰撞时，可以实时、精确地得到物理反馈，进一步提升了实时领域的物理表现。<br>
<br>
<div align="center"><font size="2"><font color="#808080">
<img aid="1044392" zoomfile="https://di.gameres.com/attachment/forum/202206/29/100100m5fe7zif50pf0xet.jpg" data-original="https://di.gameres.com/attachment/forum/202206/29/100100m5fe7zif50pf0xet.jpg" width="600" id="aimg_1044392" inpost="1" src="https://di.gameres.com/attachment/forum/202206/29/100100m5fe7zif50pf0xet.jpg" referrerpolicy="no-referrer">
</font></font></div><div align="center"><font size="2"><font color="#808080"><br>
</font></font></div><div align="left"><strong>【GPU加速的实时流体仿真】</strong></div><br>
<strong><font color="#de5650">150万+水粒子  感受真实细腻的水体流动</font></strong><br>
<br>
高精度的流体模拟效果时常出现在各种影视作品中，但是由于流体的复杂度，在实时领域，只能用极少量的粒子数来进行近似，呈现效果也相对粗糙。<br>
<br>
而START ENGINE将150万+粒子放在云端上进行运算，使用GPU进行加速，并与渲染专用卡协同，实时将流体模拟结果通过SDF进行水体几何提取和渲染。<br>
<br>
最终，START ENGINE成功将高精度的流体模拟带到实时的游戏中，给玩家带来全新、真实的体验。<br>
<br>
<div align="center">
<img aid="1044393" zoomfile="https://di.gameres.com/attachment/forum/202206/29/100101ajcsaarjbxnpn7nn.jpg" data-original="https://di.gameres.com/attachment/forum/202206/29/100101ajcsaarjbxnpn7nn.jpg" width="600" id="aimg_1044393" inpost="1" src="https://di.gameres.com/attachment/forum/202206/29/100101ajcsaarjbxnpn7nn.jpg" referrerpolicy="no-referrer">
</div><br>
<strong><font color="#de5650">携手同行，启程全真世界</font></strong><br>
<br>
正如此次原生云游戏技术DEMO的取名《EVOLUTION·进化》，START ENGINE团队会进一步在原生云游戏领域专精技术发展，为传统游戏研发效率、流程带来根本性、变革性的提升，为终端的用户带来全新的游戏体验。<br>
<br>
这，仅仅只是开始。<br>
<br>
在可以预见的未来，原生云游戏技术，这样具有突破性力量的技术，除了游戏领域的全面应用，更为影视等多领域发展提供了全新的可能性。<br>
<br>
START ENGINE期待与全球游戏工作室、独立开发者和影视行业创作者一起，利用START ENGINE所提供的技术能力，探索更多可能，一同启程全真世界。<br>
<br>
更多START ENGINE技术应用、开发经验与最新活动分享，请关注START ENGINE官方公众号，或前往官网start.qq.com/startengine<br>
<br>
  
</div>
            