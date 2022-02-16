
---
title: 'Win11承诺的支持安卓App终于更新了 教你如何在国区使用'
categories: 
 - 新媒体
 - 快科技（原驱动之家）
 - 最新新闻
headimg: 'https://img1.mydrivers.com/img/20220216/S128b2e4d-3437-4492-8a53-7486b359a2d6.png'
author: 快科技（原驱动之家）
comments: false
date: Wed, 16 Feb 2022 15:24:09 GMT
thumbnail: 'https://img1.mydrivers.com/img/20220216/S128b2e4d-3437-4492-8a53-7486b359a2d6.png'
---

<div>   
<p>今天可能是操作系统历史上最神奇的一天，因为Windows和Android在同一天实现了互相套娃。</p>
<p>微软承诺的“Windows 11支持Android应用”今天终于发布更新。</p>
<p style="text-align: center"><a href="https://img1.mydrivers.com/img/20220216/128b2e4d-3437-4492-8a53-7486b359a2d6.png" target="_blank"><img alt="Win11承诺的支持安卓App终于更新了 教你如何在国区使用" h="450" src="https://img1.mydrivers.com/img/20220216/S128b2e4d-3437-4492-8a53-7486b359a2d6.png" style="border: black 1px solid" w="600" referrerpolicy="no-referrer"></a></p>
<p>你终于可以在自己的工作电脑上刷抖音了。</p>
<p>而就在微软攻入谷歌“基地”的同时，谷歌方面也没闲着。</p>
<p>首先是官方宣布将开放Chrome OS安装到PC上。</p>
<p style="text-align: center"><a href="https://img1.mydrivers.com/img/20220216/70c34653-eab8-4927-8238-6b0502b44c65.png" target="_blank"><img alt="Win11承诺的支持安卓App终于更新了 教你如何在国区使用" h="289" src="https://img1.mydrivers.com/img/20220216/S70c34653-eab8-4927-8238-6b0502b44c65.png" style="border: black 1px solid" w="600" referrerpolicy="no-referrer"></a></p>
<p>还有黑客在Pixel 6手机里装上了Windows虚拟机。</p>
<p>这两家科技巨头是如何“相爱相杀”的，我们且往下看。</p>
<p><span style="color:#0000ff;"><strong>Windows的Android子系统</strong></span></p>
<p>早在Windows11发布前，微软就承诺加入Android子系统，今天这项更新终于到来。</p>
<p>用户无需加入Insider计划，即可享用到这项新功能。</p>
<p>但是Windows 11限制用户只可以从亚马逊应用商店安装App，我们中国区用户怎么办呢？别急。</p>
<p style="text-align: center"><a href="https://img1.mydrivers.com/img/20220216/1674c117-a2a4-4c3b-9805-b6ffe9ebd4af.png" target="_blank"><img alt="Win11承诺的支持安卓App终于更新了 教你如何在国区使用" h="400" src="https://img1.mydrivers.com/img/20220216/S1674c117-a2a4-4c3b-9805-b6ffe9ebd4af.png" style="border: black 1px solid" w="600" referrerpolicy="no-referrer"></a></p>
<p>虽然非美区用户还无法在微软商店下载Amazon Appstore，不过已经有大神可以绕过这一限制，实现安装任意apk。</p>
<p>首先进入网站https://store.rg-adguard.net，分别选择ProductID、Slow，在搜索框中输入9P3395VX91NR，点击确定。</p>
<p>选择下载最后一个msibundle文件。</p>
<p style="text-align: center"><a href="https://img1.mydrivers.com/img/20220216/2eaa8535-1b81-4008-930f-1c886c1cd732.png" target="_blank"><img alt="Win11承诺的支持安卓App终于更新了 教你如何在国区使用" h="279" src="https://img1.mydrivers.com/img/20220216/S2eaa8535-1b81-4008-930f-1c886c1cd732.png" style="border: black 1px solid" w="600" referrerpolicy="no-referrer"></a></p>
<p>比如你希望将Android子系统安装在C:\WSA\文件夹下，那么就把msibundle文件移到该文件夹中，并在PowerShell中运行以下命令：</p>
<p><strong>cd C:\WSA\</strong></p>
<p>再输入以下命令完成Android子系统的安装：</p>
<p><strong>Add-AppxPackage MicrosoftCorporationII.WindowsSubsystemForAndroid1.8.32837.0_neutral~_8wekyb3d8bbwe.msixbundle</strong></p>
<p>这样Android子系统和Amazon Appstore就安装成功了。</p>
<p>如果我们不想限制在Amazon Appstore里，想安装任意apk怎么办呢？</p>
<p>点击“开始”菜单，选择所有应用，找到Windows Subsystem for Android?? Settings，启用开发者模式，并找到子系统的IP地址。</p>
<p style="text-align: center"><a href="https://img1.mydrivers.com/img/20220216/bb998e0a-a135-45d5-a629-49d7683b4a0a.png" target="_blank"><img alt="Win11承诺的支持安卓App终于更新了 教你如何在国区使用" h="400" src="https://img1.mydrivers.com/img/20220216/Sbb998e0a-a135-45d5-a629-49d7683b4a0a.png" style="border: black 1px solid" w="600" referrerpolicy="no-referrer"></a></p>
<p>比如设置中显示IP地址为172.22.137.166，则通过以下命令连接到子系统：（需要先安装adb调试工具）</p>
<p><strong>adb connect 172.22.137.166</strong></p>
<p>最后再通过以下命令安装apk文件：</p>
<p><strong>adb install app-debug.apk</strong></p>
<p><span style="color:#0000ff;"><strong>谷歌背刺Windows</strong></span></p>
<p>另一边，谷歌于今日推出了Chrome OS Flex，可以让用户在旧的PC或Mac上安装Chrome OS，而以前Chrome OS几乎只有预装这一种形式。</p>
<p style="text-align: center"><a href="https://img1.mydrivers.com/img/20220216/f701f513-528a-47a3-a6a6-1e4271d93c93.png" target="_blank"><img alt="Win11承诺的支持安卓App终于更新了 教你如何在国区使用" h="400" src="https://img1.mydrivers.com/img/20220216/Sf701f513-528a-47a3-a6a6-1e4271d93c93.png" style="border: black 1px solid" w="600" referrerpolicy="no-referrer"></a></p>
<p>除了官方“整活”外，还有技术大神kdrag0n利用Android 13具有的“全KVM功能”，在Pixel 6手机上运行了Windows 11 ARM版。</p>
<p align="center"><img alt="Win11承诺的支持安卓App终于更新了 教你如何在国区使用" h="960" src="https://img1.mydrivers.com/img/20220216/d4e7b24034cf4489bb66b8bb635b06a1.gif" style="border: black 1px solid;" w="432" referrerpolicy="no-referrer"></p>
<p>他还顺带在这个虚拟机中玩了一把Doom。</p>
<p align="center"><img alt="Win11承诺的支持安卓App终于更新了 教你如何在国区使用" h="400" src="https://img1.mydrivers.com/img/20220216/0d3b16030f324a0baf2f8bd491fcb681.gif" style="border: 1px solid black; width: 600px;" w="640" referrerpolicy="no-referrer"></p>
<p>这位大神之所以能成功，是因为谷歌正在开展标准化Android设备Linux内核的工作，这项计划称为“通用内核映像”（GKI）。只有统一内核后，Android手机的虚拟机才能方便实现。</p>
<p>而Pixel 6是目前唯一部使用GKI的Android手机。</p>
<p>那么多问题来了：</p>
<p>既然Windows能安装Android，Android能安装Windows，我们可以这样无限套娃吗？</p>
<p>其实是不可以的，因为Android 13并不支持嵌套虚拟化技术。</p>
<p>参考链接：</p>
<p>[1]https://www.theverge.com/2022/2/15/22934562/microsoft-windows-11-february-2022-update-android-apps-taskbar-improvements</p>
<p>[2]https://docs.microsoft.com/en-us/windows/android/wsa/</p>
<p>[3]https://github.com/WSA-Community/WSAGAScript</p>
<p>[4]https://pureinfotech.com/install-windows-subsystem-android-wsa-windows-11/</p>
<p>[5]https://www.theverge.com/2022/2/15/22934810/google-chrome-os-chromebooks-flex-operating-system-enterprise-schools</p>
<p>[6]https://arstechnica.com/gadgets/2022/02/android-13-virtualization-hack-runs-windows-and-doom-in-a-vm-on-android/</p>
<p>[7]https://twitter.com/kdrag0n/status/1493089098944237568</p>

           
           
<p class="end"> - THE END -</p> 
            
 <p class="bqian"><a href="https://news.mydrivers.com/tag/anzhuo.htm"><i>#</i>安卓</a><a href="https://news.mydrivers.com/tag/windows_11.htm"><i>#</i>Windows 11</a></p>
<p class="url">
     <span>原文链接：<a href="https://mp.weixin.qq.com/s/4jg5vFJ0A-gLdBlHuSKbyg">量子位</a></span>
<span>责任编辑：随心</span>
</p>
        
</div>
            