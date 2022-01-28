
---
title: 'Valve改进Variable Rate Shading 让Steam Deck续航更持久'
categories: 
 - 新媒体
 - cnBeta
 - 最新
headimg: 'https://static.cnbetacdn.com/article/2022/0128/719391638107fd8.webp'
author: cnBeta
comments: false
date: Fri, 28 Jan 2022 03:41:44 GMT
thumbnail: 'https://static.cnbetacdn.com/article/2022/0128/719391638107fd8.webp'
---

<div>   
<strong>Valve 团队近日发布了一项更新，针对 Radeon 显卡优化了 Vulkan 对 VRS 的处理，以达到省电效果。</strong>虽然这项更新是针对 Steam Deck 的，但是传统 PC 也能从中受益。<br>
 <p style="text-align:center"><img src="https://static.cnbetacdn.com/article/2022/0128/719391638107fd8.webp" referrerpolicy="no-referrer"></p><p style="text-align: left;">Valve 的 Samuel Pitoiset 一直负责改善 Radeon Vulkan（RADV）驱动程序，以便对可变速率着色（VRS）的工作方式提供更多控制。Phoronix 指出，更高的控制程度可能与 Steam Deck 是用电池运行还是连接到交流电有关。</p><p style="text-align: left;">作为一项省电功能，<a data-link="1" href="https://c.duomai.com/track.php?site_id=242986&euid=&t=https://www.microsoftstore.com.cn/" target="_blank">微软</a>在 2019 年将 VRS 引入到 DirectX 12 中。从本质上说，它可以使游戏以不同的清晰度和精确度渲染屏幕的不同部分，这取决于它们的重要性。玩赛车游戏的人不一定在大部分时间都在看风景或天空，所以 VRS 可能会使游戏在这些区域的像素上花费的精力比汽车、驾驶舱或道路上的少。</p><p style="text-align:center"><img src="https://static.cnbetacdn.com/article/2022/0128/504951d17fdd240.webp" referrerpolicy="no-referrer"></p><p style="text-align: left;">在玩家不太容易注意到的区域，VRS 会减少渲染，比如被运动模糊覆盖的东西或阴影中的纯黑色像素。像这样的东西对于靠电池运行的便携式 PC 来说可能是至关重要的，比如 Steam Deck。</p><p style="text-align: left;">Pitoiset 的这项改进使 VRS 速率的动态缩放成为可能，现在该速率可以写入一个新的配置文件中。Steam Deck 的 <a data-link="1" href="https://c.duomai.com/track.php?site_id=242986&euid=&t=https://amd-cpu.jd.com/" target="_blank">AMD</a> Van Goh APU 将默认启用这一功能。虽然 Pitoiset 证实这一变化是为了节省电力，但 Phoronix 猜测这可能允许 VRS 速率在 Steam Deck 使用交流电或电池供电时在不同的设置之间变化。理论上，这也可能对其他运行 Vulkan 应用程序的 AMD 设备产生影响。</p>   
</div>
            