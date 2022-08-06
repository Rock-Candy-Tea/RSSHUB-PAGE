
---
title: 'Artillect将80年代打字机变身为Linux终端和ASCII艺术打印机'
categories: 
 - 新媒体
 - cnBeta
 - 最新
headimg: 'https://static.cnbetacdn.com/article/2022/0806/298cb613b43f487.jpg'
author: cnBeta
comments: false
date: Sat, 06 Aug 2022 05:00:06 GMT
thumbnail: 'https://static.cnbetacdn.com/article/2022/0806/298cb613b43f487.jpg'
---

<div>   
近日，油管 Artillect 频道分享了一个相当有趣的老旧外设改造视频 —— <strong>展示了如何通过现代硬件，将上世纪 80 年代的 Brother AX-25 电子打字机，变身为一套 Linux 终端 + ASCII 码的艺术打印机。</strong>据悉，1980年代后期的原版兄弟 AX-25 使用了菊花字轮来打印文本。<br>
 <p><img src="https://static.cnbetacdn.com/article/2022/0806/298cb613b43f487.jpg" alt="1.jpg" referrerpolicy="no-referrer"></p><p>通过现代改造，这台 AX-25 被加装了一块能够显示 16 字符的 LCD 屏，并且可编辑存储在 8 kb 内存中的文档。</p><p>目前 Riley 仍在持续改进该项目，现阶段已将打字机连接到带有两块多路复用器的面板电路板上，并通过 Arduino Uno 来实现控制。</p><p style="text-align: center;"><iframe src="//tv.sohu.com/s/sohuplayer/iplay.html?bid=371714174&autoplay=false&disablePlaylist=true" width="720" height="480" frameborder="0"></iframe></p><p style="text-align: center;">My typewriter runs Linux - Artillect（<a href="https://tv.sohu.com/v/dXMvODIyMjQwNTMvMzcxNzE0MTc0LnNodG1s.html" target="_self">via</a>）</p><p>接着他通过串行方式，将 Arduino 连到了一台树莓派上 —— 中间配有一个分压器，以将前者的 5V 输出转换为 3.3V，以防伤害后者的硬件。</p><p>然后通过 USB 连接到一台笔记本电脑，使得 Riley 能够将打字机视作一款 Linux 终端。即使功能有些受限，但至少已能够用它来开展基于 ASCII 码的艺术创作。</p><p><img src="https://static.cnbetacdn.com/article/2022/0806/b07bf5df6d01646.jpg" alt="2.jpg" referrerpolicy="no-referrer"></p><p>在拿到兄弟 AX-25 电子打字机的耗材（替换用色带）之前，Reley 尚未做好开展更细致的艺术创作的打算，但视频中展示的小示例看起来已经相当不错。</p><p>感兴趣的朋友，也可移步至 <a href="https://github.com/artillect/serial-typewriter/" target="_self">GitHub</a> 查看其为这套独特系统编写的代码。此外如果你正在寻找同型号的打字机，eBay 等二手平台上还是挺好找到的。</p><p>最后，如果一切顺利，Riley 希望将这台机器变身为一台功能齐全的设备。下一步是将键盘连接到 Arduino 控制器，那样就无需另一台计算机来调用它了。</p>   
</div>
            