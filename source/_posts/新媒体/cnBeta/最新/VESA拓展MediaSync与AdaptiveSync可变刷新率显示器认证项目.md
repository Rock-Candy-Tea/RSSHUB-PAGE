
---
title: 'VESA拓展MediaSync与AdaptiveSync可变刷新率显示器认证项目'
categories: 
 - 新媒体
 - cnBeta
 - 最新
headimg: 'https://static.cnbetacdn.com/article/2022/0503/ed5569b17e500d9.jpg'
author: cnBeta
comments: false
date: Tue, 03 May 2022 08:22:42 GMT
thumbnail: 'https://static.cnbetacdn.com/article/2022/0503/ed5569b17e500d9.jpg'
---

<div>   
<strong>视频电子标准协会（VESA）刚刚拓展了针对“可变刷新率”（VRR）显示器的认证计划，旨在帮助广大消费者轻松选购此类产品。</strong>与之前衡量峰值亮度等指标的“高动态范围”（HDR）认证项目不同，新增的“自适应同步”（Adaptive-Sync Display CTS）认证项目专注于可变刷新率显示器，特点是能够防止画面出现闪烁、撕裂、丢帧等现象。<br>
<p style="text-align: center;"><img src="https://static.cnbetacdn.com/article/2022/0503/ed5569b17e500d9.jpg" alt="1.jpg" referrerpolicy="no-referrer"></p><p style="text-align: center;">（图 via <a href="https://www.msi.com/blog/nvidia-g-sync-and-amd-freesync" target="_self">MSI</a>）</p><p>对于广大 PC 游戏玩家来说，首次接触 VRR 技术是在特定的显卡 / 显示器产品上 —— 其中包括英伟达（Nvidia）主导的闭源型 G-Sync、以及 <a data-link="1" href="https://c.duomai.com/track.php?site_id=242986&euid=&t=https://amd-cpu.jd.com/" target="_blank">AMD</a> 主推的开源性 FreeSync 方案。</p><p>2014 年的时候，VESA 携手 AMD 在 DisplayPort 1.2a 标准中，原生提供了对“自适应同步”（Adaptive-Sync）的支持。现在，该标准现已被红（AMD）、绿（Nvidia）、蓝（Intel）三家全面接纳。</p><p>与此同时，A / N 长期争相推广自家的“可变刷新率”（VRR）认证方案，但影响力相对有限。比如当 Nvidia 于 2019 年开测“G-Sync 兼容性”认证项目时，通过率仅 5.56% 。</p><p>被刷下来的产品，要么是没有提供足够宽广的刷新率范围，要么就是存在其它图像质量问题（比如闪烁）。</p><p><img src="https://static.cnbetacdn.com/article/2022/0503/8087dc7a39153d5.png" alt="4.png" referrerpolicy="no-referrer"></p><p style="text-align: center;">VESA AdaptiveSync Display CTS 成员名单</p><p>最新消息是，VESA 正在测试“自适应同步”（Adaptive-Sync）的原型性能。其最大的特点，就是不像 FreeSync 或 G-Sync 那样特定于 GPU 支持，因而有望拉拢到更多的 OEM 厂商加入。</p><p>更重要的是，VESA 的自适应同步技术基于 DisplayPort 标准实现 —— 适用于计算机、显示器、以及 USB-C 视频输出 —— 而不像基于 HDMI 2.1 标准的 VRR 方案那样特定于<a data-link="1" href="https://c.duomai.com/track.php?site_id=242986&euid=&t=https%3A%2F%2Flist.jd.com%2Flist.html%3Fcat%3D737%2C794%2C798%26ev%3D4155_76344%26sort%3Dsort_rank_asc%26trans%3D1%26JL%3D2_1_0%23J_crumbsBar" target="_blank">电视</a>设备。</p><p>英特尔工程师兼 VESA 任务工作组主席 Roland Wooster 指出：除了更加开放，VESA 的新认证项目还有助于推动显示设备厂商向广大消费者交付更高规格的产品。</p><p>尽管他们已经见到某些显示器通过了闪烁、抖动等子项目的测试，但预计市面上仅有不到一半的自适应同步显示器可符合 VESA 的标准（与 Nvidia G-Sync 推广初期的情况类似）。</p><p style="text-align: center;"><img src="https://static.cnbetacdn.com/article/2022/0503/ac7c1f2ce2e79be.png" alt="3.png" referrerpolicy="no-referrer"></p><p style="text-align: center;">（来自：AdaptiveSync.org <a href="https://www.adaptivesync.org/" target="_self">官网</a>）</p><p>言归正传，VESA 新认证包含了 AdaptiveSync 与 MediaSync 两档。后者适用于内容创作与视频观看，而前者更适用于电竞游戏。</p><p>通过认证的厂商，可在设备包装、网站、以及可能吸引潜在消费者的其它任何地方使用相关标识。而未通过认证的产品，将不被允许使用。（为了留点面子，失败机型并不会被公开披露）</p><p>具体说来是，MediaSync 认证旨在确保显示器符合 10 种主要的国际帧速率标准 —— 包括 23.976（美国地区 / 电影内容上常见）、24、25、29.97、30、47.952、48、50、 59.94、以及 60 fps 。</p><p>虽然看似简单，但在 60Hz 显示器上播放时，非整数倍率的 24 fps 内容可能遇到一些问题。常用的“3:2 下拉”方案（依次让某一帧显示两次），但这么做会产生让人不悦的抖动，而 MediaSync 就可轻松化解。</p><p style="text-align: center;"><img src="https://static.cnbetacdn.com/article/2022/0503/a9e4d9defe888be.png" alt="2.png" referrerpolicy="no-referrer"></p><p>然后是主要面向高刷屏电竞显示器的 AdaptiveSync 认证，VESA 要求产品必须默认支持原始分辨率下 @ 至少 144Hz 的高刷新率。</p><p>至于下限，则相对宽松地保持在 60Hz 。Wooster 解释称，若帧速率掉到更低（比如 58 fps），显示器有望翻倍至整数的（116 fps）的自适应同步状态。</p><p>此外以标称 144Hz 的显示器为例，通过认证的机型可在认证徽标右侧加上“Display 144”的小方框，以反映其在原始分辨率状态下支持的最大刷新率（无论是 144、240、还是 360 Hz）。</p>   
</div>
            