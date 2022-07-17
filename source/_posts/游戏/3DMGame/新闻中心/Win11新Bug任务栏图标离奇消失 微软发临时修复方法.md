
---
title: 'Win11新Bug任务栏图标离奇消失 微软发临时修复方法'
categories: 
 - 游戏
 - 3DMGame
 - 新闻中心
headimg: 'https://img.3dmgame.com/uploads/images/news/20220717/1658048253_634386.png'
author: 3DMGame
comments: false
date: Sun, 17 Jul 2022 08:58:00 GMT
thumbnail: 'https://img.3dmgame.com/uploads/images/news/20220717/1658048253_634386.png'
---

<div>   
<p style="text-indent:2em;">
Win11系统用的还算舒心么？近日有用户在微软反馈中心提交了新的Bug，表示自己的Win11系统任务栏图标因为不明原因“离奇消失”，并且找不到修复方法。
</p>
<p align="center">
<img src="https://img.3dmgame.com/uploads/images/news/20220717/1658048253_634386.png" alt="Win11新Bug任务栏图标离奇消失 微软发临时修复方法" referrerpolicy="no-referrer"> 
</p>
<p style="text-indent:2em;">
目前，微软已经对该Bug做出了回应，明确Bug原因的同时，给出了临时修复方法。
</p>
<p style="text-indent:2em;">
据悉，该Bug的罪魁祸首是Win11的IRIS服务，该服务疑似与Windows聚焦等功能有关，但微软从未明确承认过。
</p>
<p align="center">
<img src="https://img.3dmgame.com/uploads/images/news/20220717/1658048289_832274.png" alt="Win11新Bug任务栏图标离奇消失 微软发临时修复方法" referrerpolicy="no-referrer">
</p>
<p style="text-indent:2em;">
想要修复该Bug，需要用管理员模式打开命令符管理器（CMD），然后输入命令“reg delete HKCU\SOFTWARE\Microsoft\Windows\CurrentVersion\IrisService /f && shutdown -r -t 0”。
</p>
<p style="text-indent:2em;">
该命令会删除IRIS服务的注册表值，从而解决问题。
</p>
<p style="text-indent:2em;">
一般来说，在输入该命令后，系统会自动重启，在开机后问题就会得到解决。
</p>
<p align="center">
<img src="https://img.3dmgame.com/uploads/images/news/20220717/1658048296_878812.png" alt="Win11新Bug任务栏图标离奇消失 微软发临时修复方法" referrerpolicy="no-referrer"> 
</p>
<p style="text-indent:2em;">
值得一提的是，早在2020年，Win10就曾出现过任务栏不显示图标的Bug，不过当时出现问题的诱因是设备内存不足。
</p>          
</div>
            