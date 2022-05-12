
---
title: '惠普推送BIOS更新 解决影响200多个计算机型号的高危漏洞'
categories: 
 - 新媒体
 - cnBeta
 - 最新
headimg: 'https://static.cnbetacdn.com/article/2022/0512/cfb1dacc821b781.webp'
author: cnBeta
comments: false
date: Thu, 12 May 2022 12:13:00 GMT
thumbnail: 'https://static.cnbetacdn.com/article/2022/0512/cfb1dacc821b781.webp'
---

<div>   
<strong>你是否拥有一台惠普笔记本电脑、台式机或PoS
PC？那么你可能需要确保其BIOS是最新的。该公司刚刚为200多个设备型号发布了更新，修复了UEFI固件中的两个高严重级别漏洞。</strong>据Bleeping
Computer报道，惠普已经就潜在的安全漏洞发出警告，这些漏洞可能允许以内核权限执行任意代码，这将使黑客能够进入设备的BIOS并植入恶意软件，而这些恶意软件无法通过传统的杀毒软件或重新安装操作系统来清除。<br>
 <p><img src="https://static.cnbetacdn.com/article/2022/0512/cfb1dacc821b781.webp" title alt="2021-11-25-image-23-j_1100.webp" referrerpolicy="no-referrer"></p><p>这两个漏洞--CVE-2021-3808和CVE-2021-3809--的CVSS 3.1基本得分都是8.8分的高严重程度。</p><p>惠普公司没有透露关于这些漏洞的任何技术细节。这一点留给了安全研究员尼古拉斯-斯塔克，他发现了这些漏洞。</p><p>斯塔克写道："这个漏洞可能允许攻击者以内核级权限（CPL==0）执行，将权限提升到系统管理模式（SMM）。在SMM模式下执行操作，攻击者就可以获得对主机的全部权限，从而进一步实施攻击。"</p><p><img src="https://static.cnbetacdn.com/article/2022/0512/ed218a50d86f8f8.png" title alt="图片.png" referrerpolicy="no-referrer"></p><p>Starke补充说，在一些惠普机型中，有一些缓解措施需要被绕过才能使漏洞发挥作用，包括惠普的Sure Start系统，该系统可以检测到固件运行时间被篡改的情况。</p><p>受该漏洞影响的设备相当广泛，包括商务笔记本电脑，如Elite Dragonfly、EliteBooks和ProBooks；商务台式电脑，包括EliteDesk和EliteOne；零售点专用电脑，如Engage；台式工作站电脑（Z1、Z2系列）；还有四个瘦客户端电脑。</p><p>你可以在这里看到受影响的惠普设备和相应的SoftPaqs的完整列表，并非所有的设备都已收到更新：</p><p><a href="https://support.hp.com/us-en/document/ish_6184733-6184761-16/hpsbhf03788" _src="https://support.hp.com/us-en/document/ish_6184733-6184761-16/hpsbhf03788" target="_blank">https://support.hp.com/us-en/document/ish_6184733-6184761-16/hpsbhf03788</a><br></p>   
</div>
            