
---
title: '西数Cloud OS 3旧NAS平台亦曝出严重安全漏洞'
categories: 
 - 新媒体
 - cnBeta
 - 最新
headimg: 'https://static.cnbetacdn.com/thumb/article/2021/0703/621e70232971c75.jpg'
author: cnBeta
comments: false
date: Sat, 03 Jul 2021 06:21:15 GMT
thumbnail: 'https://static.cnbetacdn.com/thumb/article/2021/0703/621e70232971c75.jpg'
---

<div>   
在 6 月下旬曝出了 NAS 数据会被恶意攻击者抹除的猛料之后，KrebsOnSecurity 又介绍了在更多 WD 设备中发现的一个新漏洞。<strong>安全研究人员 Pedro Ribeiro 与 Radek Domanski 指出，问题似乎集中在 Cloud OS 3 平台、而不是新近发布的 Cloud OS 5 上。</strong>然而由于后者缺乏某些功能和特性，许多用户都宁可运行无补丁可打的旧版软件。<br>
<p><a href="https://static.cnbetacdn.com/article/2021/0703/621e70232971c75.jpg" target="_blank"><img src="https://static.cnbetacdn.com/thumb/article/2021/0703/621e70232971c75.jpg" alt="0.jpg" referrerpolicy="no-referrer"></a></p><p style="text-align: center;">（来自：Flashback Team / YouTube）</p><p>一方面，WD 表示不会为 Cloud OS 3 设备提供安全更新补丁。另一方面，一些用户也苦恼于无法升级至 Cloud OS 5 。</p><p>支持页面显示，<a href="https://www.westerndigital.com/support/productsecurity/wdc-21004-recommended-upgrade-to-mycloud-os-5" target="_self">Cloud OS 5</a> 并不适用于 MyCloud EX2 / EX4、或某些版本的 My Cloud 和 My Cloud Mirror 。</p><p><a href="https://static.cnbetacdn.com/article/2021/0703/8b06619fd1294e3.jpg" target="_blank"><img src="https://static.cnbetacdn.com/thumb/article/2021/0703/8b06619fd1294e3.jpg" alt="1.jpg" referrerpolicy="no-referrer"></a></p><p>对于这部分用户，WD 建议是换用支持新版软件的设备。或者参考去年致 Comparitech 的一份声明，直接在控制台中将远程访问功能给禁用掉。</p><p>安全研究人员指出，他们可以远程访问到一台 Cloud OS 3 设备，然后给它刷入修改后的新固件。</p><p><a href="https://static.cnbetacdn.com/article/2021/0703/5ddf684867b6279.jpg" target="_blank"><img src="https://static.cnbetacdn.com/thumb/article/2021/0703/5ddf684867b6279.jpg" alt="2.jpg" referrerpolicy="no-referrer"></a></p><p>按照惯例，固件更新功能仅面向经过身份验证的用户开放，但 Flashback Team 还是成功地绕过了这一限制，原因是 NAS 上似乎有一个密码为空的用户账户。</p><p>借助相关漏洞，攻击者可在 NAS 上执行任意命令。或者黑客也可以利用固件更新功能，让设备直接变砖。</p><p style="text-align: center;"><iframe width="640" height="480" src="//tv.sohu.com/s/sohuplayer/iplay.html?bid=269206114&autoplay=false&disablePlaylist=true" frameborder="0"></iframe></p><p style="text-align: center;">Exploiting & Patching a 0-Day RCE Vulnerability in a WD NAS（<a href="https://tv.sohu.com/v/dXMvODIyMjQwNTMvMjY5MjA2MTE0LnNodG1s.html" target="_self">via</a>）</p><p>尴尬的是，尽管研究人员设法编译了一个自定义的安全补丁，但在每次重启后，用户仍需手动将之应用于设备。</p>   
</div>
            