
---
title: 'Win11正式版累积更新又惹祸了 微软正在解决BUG'
categories: 
 - 游戏
 - 3DMGame
 - 新闻中心
headimg: 'https://img.3dmgame.com/uploads/images/news/20211031/1635664947_726280.jpg'
author: 3DMGame
comments: false
date: Sun, 31 Oct 2021 07:22:00 GMT
thumbnail: 'https://img.3dmgame.com/uploads/images/news/20211031/1635664947_726280.jpg'
---

<div>   
<p style="text-indent:2em;">
Win11系统正式版发布近一个月，11月份即将大规模推送，微软表示可用性基本没有问题。但每次更新总得弄点错误出来，本月的本月的Win11累积更新KB5006674又惹出了打印问题。微软表示已经在努力解决。
</p>
<p style="text-indent:2em;">
微软的Windows系统更新似乎跟打印相关的服务杠上了，上周才解决了Win10 21H2更新导致的网络打印机失效的问题，现在Win11正式版的首次累积更新 
KB5006674也出现了网络服务器的问题。
</p>
<p align="center">
<img src="https://img.3dmgame.com/uploads/images/news/20211031/1635664947_726280.jpg" alt="Win11正式版累积更新又惹祸了 微软正在解决BUG" referrerpolicy="no-referrer">
</p>
<p style="text-indent:2em;">
根据微软的介绍，升级累积更新 KB5006674之后，Win11用户使用网络打印服务器时会提示以下错误：
</p>
<p style="text-indent:2em;">
0x000006e4 (RPC_S_CANNOT_SUPPORT)
</p>
<p style="text-indent:2em;">
0x0000007c (ERROR_INVALID_LEVEL)
</p>
<p style="text-indent:2em;">
0x00000709 (ERROR_INVALID_PRINTER_NAME)
</p>
<p style="text-indent:2em;">
微软表示已经在调查问题，正在寻求解决方案，在此之前网络管理员可以通过允许打印客户端通过以下端口范围建立 RPC over TCP 
连接来缓解此问题：
</p>
<p style="text-indent:2em;">
默认启动端口：49152
</p>
<p style="text-indent:2em;">
默认结束端口：65535
</p>
<p style="text-indent:2em;">
端口范围：16384 端口
</p>          
</div>
            