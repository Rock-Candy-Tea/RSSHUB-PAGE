
---
title: '《赛博朋克2077》1.3版AVX Mod修复旧CPU问题'
categories: 
 - 游戏
 - 3DMGame
 - 新闻中心
headimg: 'https://img.3dmgame.com/uploads/images/news/20210831/1630370166_948141.jpg'
author: 3DMGame
comments: false
date: Tue, 31 Aug 2021 00:41:00 GMT
thumbnail: 'https://img.3dmgame.com/uploads/images/news/20210831/1630370166_948141.jpg'
---

<div>   
<p style="text-indent:2em;">
之前CDPR发布了《<a target="_blank" href="https://www.3dmgame.com/games/cyberpunk2077/">赛博朋克2077</a>》1.3版更新，然而该补丁让游戏无法在不支持AVX指令集的CPU上运行了。值得庆幸的是，国外大神Jens 
Andree发布了一个Mod，让玩家能继续用旧CPU运行《<a target="_blank" href="https://www.3dmgame.com/tag/saibopengke_1/">赛博朋克</a>2077》。
</p>
<p align="center">
<img src="https://img.3dmgame.com/uploads/images/news/20210831/1630370166_948141.jpg" alt="《赛博朋克2077》1.3版AVX Mod修复旧CPU问题" referrerpolicy="no-referrer"> 
</p>
<p style="text-indent:2em;">
当玩家试图用不支持AVX指令集的CPU运行《赛博朋克2077》1.3版时，会弹出 “EXCEPTION_ILLEGAL_INSTRUCTION 
(0xC000001D) crash”框，Jens 
Andree指出，这是因为AudioKinetic声音引擎崩溃了。因此他费心更新了33条AVX指令，才得以让游戏重新正常运行。
</p>
<p style="text-indent:2em;">
<strong><span style="color:#E56600;font-size:16px;">Mod下载地址：<a href="https://www.nexusmods.com/cyberpunk2077/mods/3084?tab=files" target="_blank"><strong><span style="color:#337FE5;"><u>点击进入</u></span></strong></a></span></strong> 
</p>
<p align="center">
<img src="https://img.3dmgame.com/uploads/images/news/20210831/1630370166_900392.jpg" alt="《赛博朋克2077》1.3版AVX Mod修复旧CPU问题" referrerpolicy="no-referrer"> 
</p>
<p style="text-indent:2em;">
Jens 
Andree表示用该解决方案有些无奈，因为无法在内存中找到关键点以阻止这些调用，他只能简单搜索每一条指令，并用nop把它们修补了。因为他保留了所有的寄存器值，所以被修补的指令不会影响代码运行。如果它在支持AVX指令集的CPU上运行时，只是检查一些数据指令，与AVX 
CPU上的堆栈跟踪相比，修补后的执行方式没有任何不同。
</p>          
</div>
            