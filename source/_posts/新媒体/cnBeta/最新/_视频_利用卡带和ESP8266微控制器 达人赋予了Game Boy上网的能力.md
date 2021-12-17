
---
title: '_视频_利用卡带和ESP8266微控制器 达人赋予了Game Boy上网的能力'
categories: 
 - 新媒体
 - cnBeta
 - 最新
headimg: 'https://static.cnbetacdn.com/article/2021/1217/dd6d1d8fc21ae1e.webp'
author: cnBeta
comments: false
date: Fri, 17 Dec 2021 00:20:12 GMT
thumbnail: 'https://static.cnbetacdn.com/article/2021/1217/dd6d1d8fc21ae1e.webp'
---

<div>   
<strong>硬件改造达人 Sebastian Staacks 完成了看似不可能的事情：他使用一个基础款 32 千兆字节的 Game Boy 卡带和一个 ESP8266 微型控制器，<a href="https://there.oughta.be/a/wifi-game-boy-cartridge" target="_blank">赋予了 Game Boy 上网冲浪的能力</a>。</strong>谈及这个改造项目的初衷，他只是表示这是他的兴趣，并有足够的能力可以做到。<br>
 <p style="text-align:center"><img src="https://static.cnbetacdn.com/article/2021/1217/dd6d1d8fc21ae1e.webp" referrerpolicy="no-referrer"></p><p style="text-align:center"><img src="https://static.cnbetacdn.com/article/2021/1217/fb4e6954b9b5b80.webp" referrerpolicy="no-referrer"></p><p style="text-align: left;">在一篇<a data-link="1" href="https://c.duomai.com/track.php?k=iRyUSQzUycwRHdo1Ddm0DZpVXZmkDN2ITPklWYmYDO5IDNy0DZp9VZ0l2cmUmchdHdm92cGJTJjZkMl42Yu02bj5SZy9GdzRnZvN3byNWat5yd3dnRyU" target="_blank">教程</a>中，Staacks 详细介绍了设计和建造该项目所需的步骤，这有点让人眼花缭乱。整个教程非常长，有两件事推动了这个项目；用于与ESP8266微控制器连接的 Z80 汇编代码，以及将网站重新格式化以在 Game Boy 屏幕上显示的微控制器代码。值得注意的是，微控制器具有 160Mhz 的时钟速度，所以比 Game Boy 的 4Mhz 升级是令人难以置信的。</p><p><iframe src="//player.bilibili.com/player.html?bvid=BV1ar4y1U7zP&page=1" width="750" height="480" frameborder="0"></iframe></p><p style="text-align: left;">以下是该帖子的摘录。</p><p style="text-align: left;">花了一些时间，但我终于成功地创建了我自己的 Game Boy 卡带。有 WiFi! 在这一点上，它只能演示简单的 telnet 式通信和访问维基百科的文章，但我相信我在未来会展示更多的东西。现在，有趣的和令人惊讶的棘手部分是这个东西到底是如何工作的。</p><p style="text-align:center"><img src="https://static.cnbetacdn.com/article/2021/1217/f2fee801611a4e8.webp" referrerpolicy="no-referrer"></p><p style="text-align:center"><img src="https://static.cnbetacdn.com/article/2021/1217/0e63b2e2a285e9f.webp" referrerpolicy="no-referrer"></p><p style="text-align:center"><img src="https://static.cnbetacdn.com/article/2021/1217/f1e2d085290ae76.webp" referrerpolicy="no-referrer"></p><p style="text-align:center"><img src="https://static.cnbetacdn.com/article/2021/1217/d521c1739b5c852.webp" referrerpolicy="no-referrer"></p><p style="text-align:center"><img src="https://static.cnbetacdn.com/article/2021/1217/b961cf2b742a3ec.webp" referrerpolicy="no-referrer"></p><p style="text-align:center"><img src="https://static.cnbetacdn.com/article/2021/1217/93260681130c330.webp" referrerpolicy="no-referrer"></p><p style="text-align:center"><img src="https://static.cnbetacdn.com/article/2021/1217/052c21816ecef48.webp" referrerpolicy="no-referrer"></p><p style="text-align:center"><img src="https://static.cnbetacdn.com/article/2021/1217/a902bf38f63d1a6.webp" referrerpolicy="no-referrer"></p><p style="text-align: left;">在你浪费你的时间在这篇文章上之前，我也许应该清楚地说明这个盒子能做什么，也许更重要的是，它不能做什么。这是一个基本的 32kiB 游戏机卡带，有一个 ESP8266 微控制器来增加 Wifi 功能。有了它，你可以从互联网或本地网络上访问 Game Boy 的数据，或从它那里发送数据。由于 ESP8266 可以为 Game Boy 做很多预处理，所以 Twitter 客户端和 Reddit 浏览器一样是可以想象的。</p><p style="text-align: left;">根据 Staacks 的说法，用于连接Wi-Fi控制器的Z80代码是使用开源开发工具包GBDK开发的，它也与世嘉游戏机兼容。Game Boy和Game Gear都是Zilog Z80的变种，所以这是否意味着我们可能会看到Game Gear墨盒在未来能够渲染彩色JPG？我不会屏住呼吸。</p>   
</div>
            