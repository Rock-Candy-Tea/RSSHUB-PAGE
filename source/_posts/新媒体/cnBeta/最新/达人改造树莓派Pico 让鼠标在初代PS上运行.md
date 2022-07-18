
---
title: '达人改造树莓派Pico 让鼠标在初代PS上运行'
categories: 
 - 新媒体
 - cnBeta
 - 最新
headimg: 'https://static.cnbetacdn.com/article/2022/0718/8218a5c1db9c528.webp'
author: cnBeta
comments: false
date: Mon, 18 Jul 2022 00:34:02 GMT
thumbnail: 'https://static.cnbetacdn.com/article/2022/0718/8218a5c1db9c528.webp'
---

<div>   
<strong>开发者使用 Vojtěch Salajka 使用树莓派 Pico 创建了一个全新的适配器，可以让鼠标在初代 PlayStation 上运行。</strong>Salajka 是一位微型电路的资深玩家，在其 <a href="https://www.franticware.com/" target="_blank">Franticware</a> 网站上分享了他创作的大量作品。<br>
 <p style="text-align:center"><img src="https://static.cnbetacdn.com/article/2022/0718/8218a5c1db9c528.webp" referrerpolicy="no-referrer"></p><p style="text-align: left;">这个项目并不需要对 PS1 进行内部改造，但需要一条兼容 PS1 主机端口的线缆。因此适合 PS1 的第三方游戏手柄是不错的选择，用户只需剪断手柄的线缆，然后将电线剥离出来。</p><p style="text-align: left;">然后 Salajka 提供了将线焊接到 Pico 的示意图，通过 Pico 上的迷你 PFM 控制 DC-DC USB 0.9V-5V to 5V DC 来提供电源。虽然目前并没有太多 PS1 游戏支持鼠标方式来玩，但至少可以通过鼠标来玩《Broken Sword》系列、《Command & Conquer》、《Doom》和《Quake 2》等游戏。</p><p style="text-align:center"><img src="https://static.cnbetacdn.com/article/2022/0718/b500f569fffab6c.webp" referrerpolicy="no-referrer"></p><p style="text-align: left;">这个项目的软件是开源的，并已经托管到 <a href="https://github.com/Franticware/usb-to-playstation-mouse" target="_blank">Github</a> 上开放下载。刷机过程也非常简单，只需要将下载后的 uf2 文件拖拽到 Pico 就可以了。不过需要注意的是这个项目也存在一些限制，并非所有的鼠标都兼容。</p><p style="text-align: center;"><img src="https://static.cnbetacdn.com/article/2022/0718/e63c121c7a3b9ee.webp" referrerpolicy="no-referrer"></p>   
</div>
            