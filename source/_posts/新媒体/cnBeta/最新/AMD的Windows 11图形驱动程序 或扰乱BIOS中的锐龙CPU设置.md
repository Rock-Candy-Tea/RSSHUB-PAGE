
---
title: 'AMD的Windows 11图形驱动程序 或扰乱BIOS中的锐龙CPU设置'
categories: 
 - 新媒体
 - cnBeta
 - 最新
headimg: 'https://static.cnbetacdn.com/thumb/article/2022/0401/0d34810e9877286.jpg'
author: cnBeta
comments: false
date: Fri, 01 Apr 2022 03:32:34 GMT
thumbnail: 'https://static.cnbetacdn.com/thumb/article/2022/0401/0d34810e9877286.jpg'
---

<div>   
在上月发布的 Radeon Adrenalin 22.3.1 WHQL 驱动程序中，AMD 更新了对 Radeon Super Resolution（简称 RSR）图像升级技术的支持。<strong>在内部测试期间，这项功能似乎运行良好。但在向用户普通推送之后，该公司才惊讶地发现，它或许引发了某个固件问题。</strong>在配备了锐龙处理器的设备上，其 BIOS 设置可能被扰乱或重置。<br>
 <p><a href="https://static.cnbetacdn.com/article/2022/0401/0d34810e9877286.jpg" target="_blank"><img src="https://static.cnbetacdn.com/thumb/article/2022/0401/0d34810e9877286.jpg" alt="1.jpg" referrerpolicy="no-referrer"></a></p><p style="text-align: center;">（via <a href="https://www.computerbase.de/forum/threads/adrenalin-22-3-1-mischt-sich-ins-bios-ein-und-verursacht-crashes.2077733/#post-26741015" target="_self">ComputerBase</a> / der-Kalli）</p><p>ComputerBase 论坛网友 der-Kalli 报告称，在更细了 22.3.1 驱动程序后，他留意到了这个奇怪的问题。</p><p>通过在网络上一番查找，我们发现早在今年 1 月份，就有一位名叫 gaojibao 的 Reddit 网友提到过类似的问题。</p><p>据推测，该问题可能是 <a data-link="1" href="https://c.duomai.com/track.php?site_id=242986&euid=&t=https://amd-cpu.jd.com/" target="_blank">AMD</a> 在去年 9 月的 21.9.1 版驱动程序中添加的“自动超频”（Auto Overclock）功能所致。</p><p><a href="https://static.cnbetacdn.com/article/2022/0401/e4b51a628cee5b2.png" target="_blank"><img src="https://static.cnbetacdn.com/thumb/article/2022/0401/e4b51a628cee5b2.png" alt="2.png" referrerpolicy="no-referrer"></a></p><p style="text-align: center;">（via <a href="https://www.reddit.com/r/Amd/comments/ruuqdv/amd_you_need_to_completely_remove_your_buggy_cpu/" target="_self">Reddit</a> / gaojibao）</p><p>这项改进旨在方便用户在一个地方实现 CPU 和 GPU 的 OC 频率调节，而无需借助 Ryzen Master 之类更复杂的实用工具。</p><p>但是出人意料的是，Radeon 驱动程序可能会在访问设备固件时，扰乱用户的原有 BIOS 设置，即便它也是启用 <a data-link="1" href="https://microsoft.pvxt.net/x9Vg1" target="_blank">Windows</a> 11 支持的同一 Radeon GPU 驱动程序。</p><p>最后，鉴于我们未能在上述两版 Radeon Adrenalin 驱动的“已知问题”列表中看到提及此错误的任何内容，AMD 或许真的一直就没有意识到该问题。</p>   
</div>
            