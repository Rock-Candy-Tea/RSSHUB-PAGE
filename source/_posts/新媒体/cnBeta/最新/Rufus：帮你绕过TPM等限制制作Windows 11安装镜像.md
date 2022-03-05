
---
title: 'Rufus：帮你绕过TPM等限制制作Windows 11安装镜像'
categories: 
 - 新媒体
 - cnBeta
 - 最新
headimg: 'https://static.cnbetacdn.com/article/2022/0305/1436c611709008c.webp'
author: cnBeta
comments: false
date: Sat, 05 Mar 2022 02:38:16 GMT
thumbnail: 'https://static.cnbetacdn.com/article/2022/0305/1436c611709008c.webp'
---

<div>   
因严苛的硬件要求，Windows 11 系统在推出之后遭到了很多用户的吐槽和批评。Windows 11 系统要求英特尔第 8 代及更新的处理器，至少 4GB 的内存和 64GB 的存储空间，并要求启用 TPM 2.0 UEFI 和 Secure Boot 功能。<br>
 <p style="text-align:center"><img src="https://static.cnbetacdn.com/article/2022/0305/1436c611709008c.webp" alt="Windows-11-Rufus.webp" referrerpolicy="no-referrer"></p><p style="text-align: left;">虽然 TPM 2.0 对大多数用户来说不是一个大问题，但 Windows 11 的 CPU 要求使许多机器无法接受升级到新的操作系统。<a data-link="1" href="https://c.duomai.com/track.php?site_id=242986&euid=&t=https://www.microsoftstore.com.cn/" target="_blank">微软</a>官方给出的理由是提高最新操作系统的性能和安全性。</p><p style="text-align: left;">自然，也有很多绕过这些限制安装 Windows 11 的方法。甚至于微软官方还发布了一份指南，详细介绍了如何绕过要求，将不符合升级条件的 Windows 10 系统升级到 Windows 11。官方程序要求用户手动修改注册表。如果你不想自己对注册表进行修改，现在你可以使用 Rufus 来执行原地升级到 Windows 11。</p><p style="text-align: left;">从 Rufus 3.18 版本开始，你可以创建一个可启动的 Windows 11 媒体，并轻松绕过 TPM 2.0 或 TPM 本身。要开始使用，从 <a href="https://github.com/pbatard/rufus/releases" target="_blank">Github</a> 安装 Rufus 3.18 测试版，下载 <a href="https://www.windowslatest.com/2021/10/05/download-windows-11-iso-images/" target="_blank">Windows 11 ISO</a>，插入一个 USB 设备，如果你的配置中包含 TPM，可以选择"标准Windows 11安装（TPM 2.0 + 安全启动）"选项，或者在没有TPM的设备上选择第二个选项。</p><p style="text-align: left;">如果你想绕过这些要求而不使用 Rufus 等第三方应用程序，注册表黑客程序也很简单。</p><blockquote style="text-align: left;"><p style="text-align: left;">执行 Win+r 并输入 regedit。</p><p style="text-align: left;">导航到 HKEY_LOCAL_MACHINE\SYSTEM\Setup\MoSetup</p><p style="text-align: left;">右键单击左侧并创建一个新的DWORD（32位）值。</p><p style="text-align: left;">将其名称设为 AllowUpgradesWithUnsupportedTPMOrCPU。</p><p style="text-align: left;">将值切换为1。</p></blockquote>   
</div>
            