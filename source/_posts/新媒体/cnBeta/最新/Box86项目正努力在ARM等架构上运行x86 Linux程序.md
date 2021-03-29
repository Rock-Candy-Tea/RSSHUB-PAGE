
---
title: 'Box86项目正努力在ARM等架构上运行x86 Linux程序'
categories: 
 - 新媒体
 - cnBeta
 - 最新
headimg: 'https://static.cnbetacdn.com/article/2021/0329/bd62929146b62c7.jpg'
author: cnBeta
comments: false
date: Mon, 29 Mar 2021 03:34:39 GMT
thumbnail: 'https://static.cnbetacdn.com/article/2021/0329/bd62929146b62c7.jpg'
---

<div>   
<strong>作为一个有趣的开源项目，Box86 允许用户在未经修改的 x86 Linux 系统（比如 ARM 平台）上运行 32-bit x86 程序。</strong>与利用 QEMU 在其它 CPU 架构上运行的 x86 程序相比，其特点是利用了系统的某些原生库，因而性能表现上也更加出色。<br>
 <p><img src="https://static.cnbetacdn.com/article/2021/0329/bd62929146b62c7.jpg" referrerpolicy="no-referrer"></p><p>此外 Box86 的设计也很容易实现 x86 OpenGL 游戏和其它图形软件的运行，通过某些解决方案，你甚至可在 Box86 中体验 Steam / Wine 游戏。</p><p>至于 Box86 的 ARM 平台支持，这里还不得不提到一款动态重编译器。与基于解释器的方案相比，其能够显著提升性能。</p><p>在早些时候的自由及开源软件开发者欧洲会议（FOSDEM 2021）上，我们就见到过一个 Box86 虚拟展台。</p><p style="text-align: center;"><iframe src="//tv.sohu.com/s/sohuplayer/iplay.html?bid=247549196&autoplay=false&disablePlaylist=true" width="640" height="480" frameborder="0"></iframe></p><p style="text-align: center;">Freedom Planet on Raspberry Pi 4 _ using Box86（<a href="https://tv.sohu.com/v/dXMvODIyMjQwNTMvMjQ3NTQ5MTk2LnNodG1s.html" target="_self">via</a>）</p><p>在共享性能指标（受 CPU 限制）的基准测试项目中，Box86 只能发挥大约一半的本机系统性能。但在 glmark2 图形测试项目中，其已接近于完整的性能发挥。</p><p>然而 Phoronix 指出，Box86 的一大短板，就是对于主机 / 本机系统的 32-bit 库支持要求，导致某些情况下的部署变得有些复杂（Box86 暂不支持 x86_64 Linux 程序）。</p><p>感兴趣的朋友，可移步至 <a href="https://github.com/ptitSeb/box86" target="_self">GitHub</a> 主页，查看有关该项目的更多细节。</p>   
</div>
            