
---
title: 'Raspberry Pi OS现上线64位镜像版本'
categories: 
 - 新媒体
 - cnBeta
 - 最新
headimg: 'https://static.cnbetacdn.com/thumb/article/2022/0203/66c9a8a5f39cf21.jpg'
author: cnBeta
comments: false
date: Thu, 03 Feb 2022 03:55:09 GMT
thumbnail: 'https://static.cnbetacdn.com/thumb/article/2022/0203/66c9a8a5f39cf21.jpg'
---

<div>   
<strong>树莓派基金会（RPF）宣布，专为迷你 DIY 电脑设计的树莓派系统（Raspberry Pi OS）现在有了 64 位版本。</strong>出于对旧硬件的兼容性和简单性的考虑，该操作系统只有 32 位，但现在用户有了更多选择。64位 的主要好处是，拥有 4GB 以上内存的系统可以充分利用其硬件。<br>
 <p>下载：<a href="https://www.raspberrypi.com/software/" target="_blank">https://www.raspberrypi.com/software/</a></p><p style="text-align:center"><a href="https://static.cnbetacdn.com/article/2022/0203/66c9a8a5f39cf21.jpg" target="_blank"><img src="https://static.cnbetacdn.com/thumb/article/2022/0203/66c9a8a5f39cf21.jpg" alt="7nqh0pjy.jpg" referrerpolicy="no-referrer"></a></p><p style="text-align:center"><a href="https://static.cnbetacdn.com/article/2022/0203/327b502789e6af6.jpg" target="_blank"><img src="https://static.cnbetacdn.com/thumb/article/2022/0203/327b502789e6af6.jpg" referrerpolicy="no-referrer"></a></p><p style="text-align: left;">在所有树莓派电脑中，树莓派 1、树莓派 2 和树莓派 Zero 支持 32 位操作系统，而树莓派 Zero 2、树莓派 3 和树莓派 4 都能运行 64 位操作系统。虽然 RPF 只提供一个 32 位的镜像比较简单，但它注意到一些闭源软件只为 arm64 硬件制作（那些前面列出的64位）。它还说 arm64 硬件在 64 位操作系统下应该运行得更好。</p><p style="text-align: left;">在评论 32 位操作系统下的内存限制时，RPF 说</p><blockquote style="text-align: left;"><p style="text-align: left;">一个更理论化的问题是，32 位指针只允许你寻址 4GB 的内存。在树莓派 4 上，我们使用 ARM 大型物理地址扩展（LPAE）来访问最高 8GB 的内存，但有一个限制条件，即任何进程只能访问 3GB 的内存（我们为内核保留了虚拟地址空间的前 1GB）。</p><p style="text-align: left;">很少有进程需要比这更多的内存：令人高兴的是，Chromium 可能是 Raspberry Pi OS 中最耗费内存的应用程序，它为每个标签生成了一个进程。但是，一些用例将受益于能够从一个单一进程中分配 8GB 树莓派4 的全部内存。</p></blockquote><p style="text-align: left;">Raspberry Pi OS 64 位用户可能遇到的一个问题是，默认安装的 64 位 Chromium 版本不包括 WidevineCDM 库，所以无法在 Netflix 等网站上观看 DRM 加密内容。</p><p style="text-align: left;">要观看这些内容，你需要使用以下命令安装 32 位版本的 Chromium</p><p style="text-align: left;">sudo apt install chromium-browser:armhf libwidevinecdm0</p><p style="text-align: left;">如果你想返回到 64 位版本，使用这个命令</p><p style="text-align: left;">sudo apt install chromium-browser:arm64 libwidevinecdm0-。</p><p style="text-align: center;"><a href="https://static.cnbetacdn.com/article/2022/0203/2c7a8b04ad7125b.png" target="_blank"><img src="https://static.cnbetacdn.com/thumb/article/2022/0203/2c7a8b04ad7125b.png" referrerpolicy="no-referrer"></a></p>   
</div>
            