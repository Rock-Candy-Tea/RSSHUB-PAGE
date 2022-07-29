
---
title: 'GNOME将在Secure Boot被禁用时向用户发出警告 并准备提供安全帮助'
categories: 
 - 新媒体
 - cnBeta
 - 最新
headimg: 'https://static.cnbetacdn.com/article/2022/0729/1fc7f49c499c9b6.webp'
author: cnBeta
comments: false
date: Fri, 29 Jul 2022 11:04:59 GMT
thumbnail: 'https://static.cnbetacdn.com/article/2022/0729/1fc7f49c499c9b6.webp'
---

<div>   
<strong>GNOME和Red
Hat的开发人员正在努力将固件安全提示和建议整合到桌面，以警告用户平台/固件安全问题，如UEFI安全启动是否被禁用，以及其他可能的系统被利用的途径。</strong>在GNOME控制中心中，有一个固件安全区域正在努力显示UEFI安全启动是否激活，各种安全保护细节，如TPM状态，Intel
BootGuard是否存在和启用，IOMMU保护状态等。<br>
 <p><img src="https://static.cnbetacdn.com/article/2022/0729/1fc7f49c499c9b6.webp" title alt="image.webp" referrerpolicy="no-referrer"></p><p>最终，有关人员希望在发现这些问题处于不太理想的状态时，允许在某些方面触发行动，以修复这些问题。</p><p>Plymouth启动界面也在准备一个警告图像，如果BIOS当中没有启用Secure Boot就会显示出来。红帽公司的最新公布的合并请求认为："当恶意软件试图感染系统的固件时，安全启动是用来对付几种安全威胁的。用户可能无意中禁用或软件可能有意禁用安全启动。因此，系统运行在一个不安全的平台上，配置不正确。如果Plymouth能向用户提供一个警告，用户可以重新启动并重新配置他们的系统，或者立即寻求帮助"。</p><p>GNOME正准备在Secure Boot被禁用的情况下向用户发出警告，以及其他试图确保系统状态至少在平台层面是安全的步骤。同样，在GDM显示管理器中，这个MR是开放的，用于添加安全启动检查和警告通知，以便用户在登录时被提醒他们的系统是否有漏洞。</p><p>在此基础上，红帽公司的Richard Hughes在博客中介绍了Fwupd正在进行的工作，以允许模拟主机配置文件。这种模拟支持是为了帮助测试任意配置下的固件安全状态，以测试拟议中的GNOME控制中心附加功能和其他工作。</p>   
</div>
            