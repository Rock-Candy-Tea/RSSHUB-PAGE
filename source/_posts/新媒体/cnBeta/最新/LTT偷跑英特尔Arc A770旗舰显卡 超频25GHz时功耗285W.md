
---
title: 'LTT偷跑英特尔Arc A770旗舰显卡 超频2.5GHz时功耗285W'
categories: 
 - 新媒体
 - cnBeta
 - 最新
headimg: 'https://static.cnbetacdn.com/article/2022/0721/12887526b7f06ac.jpg'
author: cnBeta
comments: false
date: Thu, 21 Jul 2022 02:57:46 GMT
thumbnail: 'https://static.cnbetacdn.com/article/2022/0721/12887526b7f06ac.jpg'
---

<div>   
<strong>Linus Tech Tips 刚刚在油管上分享了一支视频，主题是英特尔 Arc A770 显卡的游戏与超频性能预览。</strong>可知其能够在《赛博朋克 2077》上实现流畅的 1440p 游戏体验，辅以高达 2.5 GHz 的频率和 285W 的 TDP 功耗。<br>
 <p><img src="https://static.cnbetacdn.com/article/2022/0721/12887526b7f06ac.jpg" alt="1.jpg" referrerpolicy="no-referrer"></p><p style="text-align: center;">视频封面（来自：Linus Tech Tips / YouTube）</p><p>尽管距离<a data-link="1" href="https://c.duomai.com/track.php?site_id=242986&euid=&t=https://intel.jd.com/" target="_blank">英特尔</a>正式揭开 Arc Alchemist 旗舰台式显卡的神秘面纱已只有几天时间，但 LTT 还是在近日抢先放出了 Arc A770 的早期游戏基准与超频性能预览。</p><p>此外在 Linus Sebastian 和 Luke Lafreniere 主持的 WAN 秀直播期间，他们也与包括 Tom Petersen 和 Ryan Shrout 在内的嘉宾有过互动。</p><p style="text-align: center;"><iframe src="//tv.sohu.com/s/sohuplayer/iplay.html?bid=367147593&autoplay=false&disablePlaylist=true" width="720" height="480" frameborder="0"></iframe></p><p style="text-align: center;">I hope no one gets fired for this - Linus Tech Tips（<a href="https://tv.sohu.com/v/dXMvODIyMjQwNTMvMzY3MTQ3NTkzLnNodG1s.html" target="_self">via</a>）</p><p>鉴于 Arc A380 显卡评测没能给人留下深刻的印象，现在就看英特尔能否通过 Arc A770 扳回一局。</p><p>除了 Arc 7 台式旗舰显卡，ACM-G10 GPU 还有包括 Arc A770M / A730M 在内的移动衍生版本。</p><p>只不过 Arc A770 用上了满血版的 ACM-G10，拥有 4096 个 ALU / 32 个 Xe Core / 32 个光追单元。</p><p><img src="https://static.cnbetacdn.com/article/2022/0721/2c6dc9307feee58.jpg" alt="2.jpg" referrerpolicy="no-referrer"></p><p>频率方面，该 GPU 峰值可达 2.4 GHz（高于宣传规格），此时 FP32 性能接近 20 TFLOPs 。</p><p>Arc A770 还有 256-bit @ 16GB GDDR6 显存，外接 8+6 pin 供电（理论最大 300W），实际 TGP / TBP 功耗应该低于 250W（演示卡功率约 190W）。</p><p><img src="https://static.cnbetacdn.com/article/2022/0721/4bffd17342806a9.jpg" alt="3.jpg" referrerpolicy="no-referrer"></p><p>性能方面，预期 Arc A770 介于英伟达 RTX 3060 Ti 和 RTX 3070 之间 —— 毕竟 Arc A750 较 RTX 3060 有 17% 的跑分领先优势。</p><p>需要指出的是，Arc Alchemist GPU 更侧重于新近的 DirectX 12 和 Vulkan API 游戏表现，首发驱动对 DX11 老游戏的支持仍有较大改进空间。</p><p><img src="https://static.cnbetacdn.com/article/2022/0721/ec417b85bd95bcc.jpg" alt="4-1.jpg" referrerpolicy="no-referrer"></p><p>测试平台还选用了酷睿 i9-12900KS 处理器，可知 Arc A770 的 DX11 / DX12 成绩分别在 40 / 80 fps 左右。</p><blockquote><p>按照英特尔的“三层优化”策略，第 1 层是让 Arc GPU 提供一流的性能体验。</p><p>第 2 层是优化程度较低的游戏（现代游戏 API 上的表现略逊一筹）。</p><p>第 3 层则是未优化 / 在较旧的 API 运行的游戏（被竞争对手拉开较大的差距）。</p></blockquote><p><img src="https://static.cnbetacdn.com/article/2022/0721/514a078e78692ad.jpg" alt="4-2.jpg" referrerpolicy="no-referrer"></p><p>由《赛博朋克 2077》和《F1 2021》的广泛测试可知，其能够在 1440p 分辨率下提供相当不错的体验。</p><p>不过就算 LTT 没有披露更详尽的数据，Arc A770 的超频配置也是相当喜人的。</p><p>本例中，显卡被调教到了 +20% 的 GPU 性能加速状态。拉动电压曲线后，功率限制被解放到了 285W、温度限制也拉高到了 125℃ 。</p><p><img src="https://static.cnbetacdn.com/article/2022/0721/5a982c46755c6ac.png" alt="5.png" referrerpolicy="no-referrer"></p><p style="text-align: center;">（via <a href="https://wccftech.com/intel-flagship-arc-a770-graphics-card-performance-gaming-overclocking-preview-2-5-ghz-clocks-285w-tdp/" target="_self">WCCFTech</a>）</p><p>略为遗憾的是，尽管 Arc A770 在 2.5 GHz 的 GPU 加速频率下，能够以 76℃ 的最高温度达成 100% 的利用率。</p><p>但当配置文件被推到 +30% 时，游戏还是没能抵挡住崩溃，一种猜测是 LTT 测试用的 Arc A770 芯片体质拖了后腿。</p><p>最后，参照当前的市场状况和 Arc A770 显卡的性能表现，预计英特尔的定价会低于 400 美元、并于今夏晚些时候正式到来。</p>   
</div>
            