
---
title: 'Windows Defender被曝影响英特尔CPU性能 涉及8到11代酷睿'
categories: 
 - 游戏
 - 3DMGame
 - 新闻中心
headimg: 'https://img.3dmgame.com/uploads/images/news/20220628/1656416335_940799.jpg'
author: 3DMGame
comments: false
date: Tue, 28 Jun 2022 11:39:00 GMT
thumbnail: 'https://img.3dmgame.com/uploads/images/news/20220628/1656416335_940799.jpg'
---

<div>   
<p style="text-indent:2em;">
近日，ThrottleStop和RealTemp等软件的开发者Kevin Glynn，在软件的开发过程中发现，微软Windows 
11/10上的Windows Defender会明显影响英特尔CPU的性能。虽然安全软件在实时保护期间必然会对性能有些许影响，但此次的影响要大得多。
</p>
<p align="center">
<img src="https://img.3dmgame.com/uploads/images/news/20220628/1656416335_940799.jpg" alt="Windows Defender被曝影响英特尔CPU性能 涉及8到11代酷睿" referrerpolicy="no-referrer">
</p>
<p style="text-indent:2em;">
据TechPowerup报道，Kevin Glynn发现当CPU满载的时候，HWiNFO会报告频率降低。更大的问题是，当Windows 
Defender受到影响时，性能就会明显下降，比如全核频率以5GHz运行的酷睿i9-10850K，会损失6%的性能。据了解，无论是桌面平台还是移动平台，英特尔第8、9、10和11代酷睿在Windows 
11/10都会如此，只是程度有所不同，AMD的处理器则不会受到影响。
</p>
<p align="center">
<img src="https://img.3dmgame.com/uploads/images/news/20220628/1656416273_902262.jpg" alt="Windows Defender被曝影响英特尔CPU性能 涉及8到11代酷睿" referrerpolicy="no-referrer">
</p>
<p align="center">
<img src="https://img.3dmgame.com/uploads/images/news/20220628/1656416280_701947.jpg" alt="Windows Defender被曝影响英特尔CPU性能 涉及8到11代酷睿" referrerpolicy="no-referrer">
</p>
<p style="text-indent:2em;">
消耗如此多性能，最根本原因是Windows 
Defender会随机使用英特尔CPU提供的所有7个硬件性能计数器，其中包括3个固定功能计数器。每个计数器都可以在四种模式中的其中一种模式下进行编程，以配置其计数的特权级别，包括Disabled、OS 
(ring-0)、User (ring>0)和All-Ring。由于这些计数器共享资源，因此多个程序可能希望同时访问这些计数器。
</p>
<p style="text-indent:2em;">
像HWiNFO或者ThrottleStop这些系统应用程序，都将这些计数器设置为“mode 
3”或“All-Ring”。设置了相同模式后，多个程序使用相同计数器是没有问题的，但Windows Defender设置的是“mode 
2”，导致程序之间会不断争抢，计数器控制寄存器会在0x222和0x332之间不断变化。
</p>
<p style="text-indent:2em;">
该问题的根源不在于英特尔的硬件，因为经过手动设置设置后，性能就会恢复正常，而且不影响Windows 
Defender对病毒的防护。临时方法是使用Counter Control工具中的Reset 
Counters按钮，一键重置计数器，或者使用ThrottleStop工具，在“选项”中选择“Windows Defender Boost”功能。
</p>
<p align="center">
<img src="https://img.3dmgame.com/uploads/images/news/20220628/1656416287_318811.jpg" alt="Windows Defender被曝影响英特尔CPU性能 涉及8到11代酷睿" referrerpolicy="no-referrer">
</p>          
</div>
            