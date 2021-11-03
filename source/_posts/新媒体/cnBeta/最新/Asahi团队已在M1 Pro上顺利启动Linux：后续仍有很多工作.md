
---
title: 'Asahi团队已在M1 Pro上顺利启动Linux：后续仍有很多工作'
categories: 
 - 新媒体
 - cnBeta
 - 最新
headimg: 'https://static.cnbetacdn.com/article/2021/1103/94be1af79d3e697.png'
author: cnBeta
comments: false
date: Wed, 03 Nov 2021 06:52:15 GMT
thumbnail: 'https://static.cnbetacdn.com/article/2021/1103/94be1af79d3e697.png'
---

<div>   
在苹果于上月发布了采用 M1 Pro / M1 Max 芯片组的 2021 款 14 / 16 英寸 MacBook Pro 之后，Asahi 团队也在努力实现在新硬件上运行 Linux 开源操作系统的目标。在去年搞定了 M1 平台之后，<strong>Asahi Linux 项目组的 Hector Martin，现又在 Twitter 上宣布其已抵达一个新的里程碑 —— 通过可用的 USB 端口，成功地在 M1 Pro 设备上启动到了一个 Shell 界面。</strong><br>
 <p><img src="https://static.cnbetacdn.com/article/2021/1103/94be1af79d3e697.png" referrerpolicy="no-referrer"></p><p>据悉，Asahi Linux 项目组的 Hector Martin，一直致力于通过众包的方式，让 Linux 在<a data-link="1" href="https://apple.pvxt.net/c/1251234/435400/7639?u=https%3A%2F%2Fwww.apple.com%2Fcn%2Fmusic%2F" target="_blank">苹果</a>最新硬件平台上运行。</p><p>过去一年，他还和许多热心开发者携手，为在 M1 <a data-link="1" href="https://apple.pvxt.net/c/1251234/435400/7639?u=https%3A%2F%2Fwww.apple.com%2Fcn%2Fmac%2F" target="_blank">MacBook</a> 上运行 Linux 开源操作系统而付出了大量的心力。</p><p>在此前经验的基础上，这次 M1 Pro / M1 Max MacBook 的 Linux 引导工作已变得轻车熟路。</p><p>虽然距离最终目标还有很长一段路，但可以确定的是，SMP 对称多处理、IRQ / IPI 中断、Framebuffer Console 帧缓冲控制台、DART、USB（包括供电）、I2C、以及 GPIO，现都已能够在 M1 Pro 平台上配合使用。</p><p>接下来，Asahi Linux 团队将把更多精力放到 PCI Express 总线上，尤其是搞定 SD 读卡器和 Wi-Fi 无线网络支持（但愿后续的存储支持也能够很快完善）。至于键盘 / 触摸板支持，还是依赖于概念验证的 SPI 驱动程序。</p><p>最后，与去年的 Apple M1 一样，Asahi Linux 团队仍面临着 DRM 内核驱动、以及基于 OpenGL / Vulkan 的图形支持等难题。只有完善了这些功能，Linux 用户才能充分发挥苹果新硬件的性能。</p>   
</div>
            