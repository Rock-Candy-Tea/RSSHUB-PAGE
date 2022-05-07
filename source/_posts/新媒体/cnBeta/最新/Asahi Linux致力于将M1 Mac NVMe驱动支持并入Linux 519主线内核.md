
---
title: 'Asahi Linux致力于将M1 Mac NVMe驱动支持并入Linux 5.19主线内核'
categories: 
 - 新媒体
 - cnBeta
 - 最新
headimg: 'https://static.cnbetacdn.com/article/2022/0507/477f1176d5974c0.jpg'
author: cnBeta
comments: false
date: Sat, 07 May 2022 03:49:43 GMT
thumbnail: 'https://static.cnbetacdn.com/article/2022/0507/477f1176d5974c0.jpg'
---

<div>   
尽管非易失性内存主机控制器（NVMe）接口规范已经成为行业标准多年，但想要让运行 Linux 内核的 Apple Silicon 设备支持它，仍需付出相当大的努力。<strong>好消息是，负责该驱动程序的 Asahi Linux 已在邮件公告列表中进行了披露，并致力于让它在即将到来的 Linux 5.19 合并窗口中被引入。</strong><br>
<p><img src="https://static.cnbetacdn.com/article/2022/0507/477f1176d5974c0.jpg" referrerpolicy="no-referrer"></p><p style="text-align: center;">如果一切顺利，Linux 5.19 有望于 7 月正式发布。</p><p><a href="https://www.phoronix.com/scan.php?page=news_item&px=Apple-M1-NVMe-Linux-5.19" target="_self">Phoronix</a> 指出，Apple M1 的 NVMe 支持，并非由<a data-link="1" href="https://apple.pvxt.net/c/1251234/435400/7639?u=https%3A%2F%2Fwww.apple.com%2Fcn%2Fmusic%2F" target="_blank">苹果</a>官方提供，而是逆向工程开源社区的一个项目。</p><p>问题在于，M1 Mac 的 NVMe 控制器并非直接挂载到 PCI Express 总线上，意味着 Linux 内核驱动程序开发者需要对各种基础组件进行魔改，才能让苹果硬件顺利地跑起来。</p><p>此外 M1 Mac 的 NVMe 控制器还依赖于一个专有的 RTOS（RTKit）协处理器，作为支持的一部分，Linux 内核需要与之交互。</p><p><img src="https://static.cnbetacdn.com/article/2022/0507/4662a574a2ddbff.png" referrerpolicy="no-referrer"></p><p style="text-align: center;">截图（来自：Asahi Linux <a href="https://asahilinux.org/about/" target="_self">官网</a>）</p><p>M1 Mac 平台 NVMe 驱动程序和所有其它必要更改，总计需要大约 3500 行新代码。赶在本月晚些时候的 Linux 5.19 合并窗口开启之前，这部分 SoC 驱动程序将被并入主线。</p><p>综上所述，Apple M1 Mac 上的 Linux 支持将逐渐成熟。后续开发团队将致力于搞定音频 / 麦克风等连接选项，不过横亘在他们面前的一个最大阻碍，还是缺乏对图形加速的适当支持。</p>   
</div>
            