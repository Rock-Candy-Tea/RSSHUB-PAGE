
---
title: 'Microsoft Defender获得新功能以对抗Log4j高位漏洞'
categories: 
 - 新媒体
 - cnBeta
 - 最新
headimg: 'https://static.cnbetacdn.com/article/2021/1229/3a6344a5671e6bb.webp'
author: cnBeta
comments: false
date: Wed, 29 Dec 2021 12:53:28 GMT
thumbnail: 'https://static.cnbetacdn.com/article/2021/1229/3a6344a5671e6bb.webp'
---

<div>   
微软已经宣布对其安全软件Microsoft Defender的云端版本进行更新，以对抗Log4j漏洞。Log4j大部分已经打上了补丁，但仍然可以影响一些服务器，这些服务器可以使用微软防御者的帮助。<br>
 <p><img src="https://static.cnbetacdn.com/article/2021/1229/3a6344a5671e6bb.webp" title alt="2021-12-28-image-2-p_1100.webp" referrerpolicy="no-referrer"></p><p>微软透露，自12月中旬以来，它一直在为Microsoft Defender for 365发布更新，增加了检测和打击Log4j漏洞的自动方法。现在，Defender可以持续观察和识别漏洞。</p><p>最新版本可以发现有漏洞的Log4j库组件，以及使用Log4j库的有漏洞的已安装软件。微软增加了一个专门的Log4j仪表板，可以综合查看发现的漏洞。</p><p>DeviceTvmSoftwareEvidenceBeta是更新中引入的一个新模式，它从磁盘中调出文件级的发现，并让用户用增加的上下文对它们进行关联，以便进行高级搜索。用户现在还可以通过DeviceTvmSoftwareVulnerabilities与DeviceTvmSoftwareEvidenceBeta的组合来查找已安装程序中的漏洞。</p><p>这些更新适用于Microsoft Defender 365、Microsoft Defender for Endpoint和Microsoft Defender for Containers。除了<a data-link="1" href="https://microsoft.pvxt.net/x9Vg1" target="_blank">Windows</a> 10和11之外，这些更新还兼容Windows Server 2008、2012和2016。Linux用户如果将Defender for Linux更新到101.52.57（30.121092.15257.0）或更高版本，就可以得到最近更新。</p><p>Microsoft Defender for Containers是一个基于云的保护计划，于12月初首次亮相，专门为保护容器而设计。最近的更新让它检测到易受Log4j攻击的图像。当它们被推送到Azure容器注册中心，或从注册中心拉出，或在Kubernetes集群上运行时就会自动扫描它们。</p><p>在Azure门户中，"容器注册表图像应解决漏洞问题"的建议应出现在"Microsoft Defender for Cloud"下，Defender会显示有漏洞的镜像。用户还可以只显示当前在Kubernetes集群上运行的易受攻击的镜像，以及查看Azure资源图，以获得不同云中的漏洞信息。</p>   
</div>
            