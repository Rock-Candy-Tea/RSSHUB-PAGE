
---
title: 'Igalia可为老式Raspberry Pi单板计算机提供更快的2D渲染服务'
categories: 
 - 新媒体
 - cnBeta
 - 最新
headimg: 'https://static.cnbetacdn.com/article/2022/0716/5c5b24cf0dafcae.webp'
author: cnBeta
comments: false
date: Sat, 16 Jul 2022 11:31:40 GMT
thumbnail: 'https://static.cnbetacdn.com/article/2022/0716/5c5b24cf0dafcae.webp'
---

<div>   
Igalia开发人员Christopher Michael已经开始发表系列博文，概述了该公司在改善Raspberry Pi
1至Raspberry Pi 3单板计算机的加速2D渲染方面的进展。对于那些仍在使用目前Raspberry Pi 4之前的老式Raspberry
Pi硬件的人来说，X11下的2D渲染可能很慢而且有问题。<br>
 <p>目前，Raspberry Pi官方操作系统图像禁用了GLAMOR 2D加速，该加速使用OpenGL来加速X.Org服务器的2D渲染。之所以禁用GLAMOR是因为GPU的内存被限制在256Mb，如果（很容易）耗尽该内存，系统会反过来崩溃。因此，现在在这些老化的Arm SBC上，X11又回到了软件渲染的状态。</p><p><img src="https://static.cnbetacdn.com/article/2022/0716/5c5b24cf0dafcae.webp" title alt="image.webp" referrerpolicy="no-referrer"></p><p>在没有启用GLAMOR的情况下，X11的渲染在基于软件的渲染下性能会非常糟糕。Igalia正在努力克服这个问题，在使用xf86-video-modesetting驱动支持加速渲染的同时可以没有GLAMOR。</p><p>Christopher Michael在该系列的第一篇文章中总结了目前的情况，但没有透露他们在不耗尽Raspberry Pi 1-3硬件上有限的GPU内存的情况下克服X11加速渲染负担的解决方案，相信细节会在下一次披露中公布。</p><p>Igalia的工程师们一直在与Raspberry Pi基金会合作，为Raspberry Pi板使用的Broadcom显卡开发开源图形栈。</p><p>了解更多：</p><p><a href="https://blogs.igalia.com/cmichael/2022/05/30/modesetting-a-glamor-less-rpi-adventure/" _src="https://blogs.igalia.com/cmichael/2022/05/30/modesetting-a-glamor-less-rpi-adventure/" target="_blank">https://blogs.igalia.com/cmichael/2022/05/30/modesetting-a-glamor-less-rpi-adventure/</a><br></p>   
</div>
            