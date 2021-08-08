
---
title: 'Zen3性能再提升15% AMD研究3D缓存多年：带宽超2TB_s'
categories: 
 - 游戏
 - 3DMGame
 - 新闻中心
headimg: 'https://img.3dmgame.com/uploads/images/news/20210808/1628393910_340771.jpg'
author: 3DMGame
comments: false
date: Sun, 08 Aug 2021 03:39:00 GMT
thumbnail: 'https://img.3dmgame.com/uploads/images/news/20210808/1628393910_340771.jpg'
---

<div>   
<p style="text-indent:2em;">
今年底AMD很有可能发布增强版的7nm Zen3处理器，为了对付Intel的12代酷睿Alder Lake，它将用上3D V-Cache缓存技术，额外增加了128MB缓存，总计192MB。
</p>
<p style="text-indent:2em;">
该技术今年6月份台北电脑展上首次公布，展示用的是一颗锐龙9 5900X 12核心处理器，原本内部集成两个CCD计算芯片、一个IO输入输出芯片。
</p>
<p style="text-indent:2em;">
经过改造后，<strong>它的每一个计算芯片上都堆叠了64MB SRAM，官方称之为“3D V-Cache”</strong>，可作为额外的三级缓存使用，这样加上处理器原本集成的64MB，总的三级缓存容量就达到了192MB。
</p>
<p align="center">
<img src="https://img.3dmgame.com/uploads/images/news/20210808/1628393910_340771.jpg" alt="Zen3性能再提升15% AMD研究3D缓存多年：带宽超2TB/s" referrerpolicy="no-referrer">
</p>
<p style="text-indent:2em;">
AMD在其中应用了直连铜间结合、硅片间TSV通信等技术，实现了这种混合式的缓存设计。
</p>
<p style="text-indent:2em;">
<strong><span style="color:#E53333;">根据AMD的数据，改进之后，对比标准的锐龙9 5900X处理器，频率都固定在4GHz，3D V-Cache缓存加入之后，游戏性能平均提升了多达15％。</span></strong>
</p>
<p style="text-indent:2em;">
对于该技术，Techinsights的研究员Yuzo Fukuzaki日前公布了更多细节，称AMD已经研究该技术多年，<strong>使用了TSV硅通孔技术将额外的128MB缓存集成到芯片上，面积6x6mm，带宽超过2TB/s。</strong>
</p>
<p style="text-indent:2em;">
他在文章中指出，为了应对memory_wall问题，缓存内存的设计很重要，这是缓存密度在工艺节点上的趋势，逻辑上的3D内存集成可以有助于获得更高的性能。
</p>
<p style="text-indent:2em;">
随着AMD开始实现Chiplet CPU整合，他们可以使用KGD（Known Good Die）来摆脱模具的低产量问题。在IRDS（International Roadmap Devices and Systems）中，这一创新预计将在2022年实现。
</p>
<p style="text-indent:2em;">
TechInsights以反向方式深入研究了3d V-Cache的连接方式，并提供了以下发现的结果：
</p>
<p style="text-indent:2em;">
TSV间距：17μm
</p>
<p style="text-indent:2em;">
KOZ尺寸：6.2 x 5.3μm
</p>
<p style="text-indent:2em;">
TSV数量：粗略估计大约23000个
</p>
<p style="text-indent:2em;">
TSV工艺位置：在M10-M11之间（共15种金属，从M0开始）
</p>
<p align="center">
<img src="https://img.3dmgame.com/uploads/images/news/20210808/1628393923_103412.png" alt="Zen3性能再提升15% AMD研究3D缓存多年：带宽超2TB/s" referrerpolicy="no-referrer">
</p>          
</div>
            