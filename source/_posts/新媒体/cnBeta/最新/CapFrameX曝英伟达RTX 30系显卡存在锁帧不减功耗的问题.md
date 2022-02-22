
---
title: 'CapFrameX曝英伟达RTX 30系显卡存在锁帧不减功耗的问题'
categories: 
 - 新媒体
 - cnBeta
 - 最新
headimg: 'https://static.cnbetacdn.com/thumb/article/2022/0222/ddbe8410f835d76.jpg'
author: cnBeta
comments: false
date: Mon, 21 Feb 2022 23:58:15 GMT
thumbnail: 'https://static.cnbetacdn.com/thumb/article/2022/0222/ddbe8410f835d76.jpg'
---

<div>   
出于各种原因，玩家偶尔需要通过显卡驱动程序来锁定帧速率。<strong>在 CPU / GPU 或其它硬件可能遇到瓶颈的情况下，限制 fps 或有助于改善游戏体验。</strong>另外当输出帧率超过显示器所支持的刷新率时，此举也有助于节约能源。<br>
<p><a href="https://static.cnbetacdn.com/article/2022/0222/ddbe8410f835d76.jpg" target="_blank"><img src="https://static.cnbetacdn.com/thumb/article/2022/0222/ddbe8410f835d76.jpg" alt="0.jpg" referrerpolicy="no-referrer"></a></p><p style="text-align: center;">有时“少即是多”（来自：<a href="https://www.capframex.com/tests/Nvidia%20has%20an%20efficiency%20problem" target="_self">CapFrameX</a>）</p><p>A 卡老玩家们应该不会对 <a href="https://www.amd.com/en/technologies/radeon-software-chill" target="_self">Radeon Chill</a> 感到陌生，该功能可在用户远离屏幕时节约能源。与此同时，许多人也期待着 N 卡也有同样的锁帧表现。</p><p>尴尬的是，据性能监测工具制造商 CapFrameX 所述 —— 其通过实测发现所做的测试，基于 Ampere GPU 的 RTX 30 系列显卡未能顺利达成节能的目的。</p><p><a href="https://static.cnbetacdn.com/article/2022/0222/69a0452ec22fe21.png" target="_blank"><img src="https://static.cnbetacdn.com/thumb/article/2022/0222/69a0452ec22fe21.png" alt="1.png" referrerpolicy="no-referrer"></a></p><p style="text-align: center;">《毁灭战士：永恒》实测</p><p>CapFrameX 认为，英伟达当前的频率加速算法无法有效控制测试期间的 GPU 核心时钟和电压。因为即使帧速率限制启用到位，其仍被视作允许飙至最大值。</p><p><a href="https://static.cnbetacdn.com/article/2022/0222/3a5b5a3a6d305d1.png" target="_blank"><img src="https://static.cnbetacdn.com/thumb/article/2022/0222/3a5b5a3a6d305d1.png" alt="2.png" referrerpolicy="no-referrer"></a></p><p style="text-align: center;">《古墓丽影：暗影》</p><p>以 GeForce RTX 3090 旗舰显卡和《古墓丽影：暗影》游戏为例，CapFrameX 注意到 —— 在锁 60fps 帧率的情况下，GPU 能耗几乎是基础频率的两倍（约 195W）。</p><p>与此同时，手动配置的 RTX 3090，其消耗的功耗就要少很多（仅约 110W）。</p><p><a href="https://static.cnbetacdn.com/article/2022/0222/61a0cbb86f5e771.png" target="_blank"><img src="https://static.cnbetacdn.com/thumb/article/2022/0222/61a0cbb86f5e771.png" alt="3.png" referrerpolicy="no-referrer"></a></p><p style="text-align: center;">《战地 V》实测</p><p>CapFrameX 接着对 RTX 3070 Ti 展开了同样的 30 / 120 / 144 fps 锁帧测试，并且横跨了 1080p / 1440p 两档分辨率。</p><p>除了《古墓丽影：暗影》，参与测试的游戏中还包括《异域骑兵》、《毁灭战士：永恒》、以及《战地 V》。</p><p><a href="https://static.cnbetacdn.com/article/2022/0222/839c18d753af63c.png" target="_blank"><img src="https://static.cnbetacdn.com/thumb/article/2022/0222/839c18d753af63c.png" alt="4.png" referrerpolicy="no-referrer"></a></p><p style="text-align: center;">《异域骑兵》实测</p><p>庆幸的是，至少在 <a data-link="1" href="https://c.duomai.com/track.php?site_id=242986&euid=&t=https://amd-cpu.jd.com/" target="_blank">AMD</a> Radeon RX 6800 XT 显卡的实测中，CapFrameX 并未发现 Radeon Software 驱动程序有如此奇怪的问题。</p>   
</div>
            