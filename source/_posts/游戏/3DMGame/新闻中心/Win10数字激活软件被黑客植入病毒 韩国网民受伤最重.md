
---
title: 'Win10数字激活软件被黑客植入病毒 韩国网民受伤最重'
categories: 
 - 游戏
 - 3DMGame
 - 新闻中心
headimg: 'https://img.3dmgame.com/uploads/images/news/20220322/1647941783_150391.jpg'
author: 3DMGame
comments: false
date: Tue, 22 Mar 2022 10:05:00 GMT
thumbnail: 'https://img.3dmgame.com/uploads/images/news/20220322/1647941783_150391.jpg'
---

<div>   
<p style="text-indent:2em;">
近日安全研究公司ASEC发现网上出现一种新的恶意软件大肆传播，它会伪装成以Windows激活工具的形式，但实际上是BitRAT远程访问木马。
</p>
<p align="center">
<img src="https://img.3dmgame.com/uploads/images/news/20220322/1647941783_150391.jpg" alt="Win10数字激活软件被黑客植入病毒 韩国网民受伤最重" referrerpolicy="no-referrer"> 
</p>
<p style="text-indent:2em;">
ASEC发现这种木马主要是通过Webhards分发(Webhards是韩国的在线文件共享服务)，但也会有通过其他渠道传播的风险。ASEC认为目前受害者主要是韩国网民，其他地区传播的不大。
</p>
<p align="center">
<img src="https://img.3dmgame.com/uploads/images/news/20220322/1647941784_526912.jpg" alt="Win10数字激活软件被黑客植入病毒 韩国网民受伤最重" referrerpolicy="no-referrer"> 
</p>
<p style="text-indent:2em;">
值得一提的是，虽然破解和盗版软件通常被报毒，但许多人往往不会认真对待此类警告，而且部分用户需要Windows激活工具，可能在某些情况下就导致了这一问题。
</p>
<p style="text-indent:2em;">
ASEC解释说，下载的zip文件“W10DigitalActivation.exe”虽然带有正版 Windows 
激活文件，但也确实包含恶意文件。“W10DigitalActivation”msi 
文件显然是真实的，而另一个“W10DigitalActivation_Temp”文件却是恶意软件。当毫无戒心的用户运行压缩包中的文件时，真正的激活工具和恶意软件会同时执行，从而让用户误以为 
Windows 激活工具是真的，所以这个文件没有威胁。
</p>
<p align="center">
<img src="https://img.3dmgame.com/uploads/images/news/20220322/1647941784_480552.jpg" alt="Win10数字激活软件被黑客植入病毒 韩国网民受伤最重" referrerpolicy="no-referrer"> 
</p>
<p style="text-indent:2em;">
当你运行木马后，W10DigitalActivation_Temp.exe会通过命令和控制 (C&C) 
服务器下载其他恶意文件，并通过PowerShell将它们传递到Windows启动程序文件夹中。
</p>
<p align="center">
<img src="https://img.3dmgame.com/uploads/images/news/20220322/1647941784_522284.jpg" alt="Win10数字激活软件被黑客植入病毒 韩国网民受伤最重" referrerpolicy="no-referrer"> 
</p>
<p style="text-indent:2em;">
最后，BitRAT 会为你在% temp%文件夹内安装“Software_Reporter_Tool.exe”文件，从而实现在Windows 
Defender中添加Startup文件夹的排除路径和BitRAT的排除过程。
</p>          
</div>
            