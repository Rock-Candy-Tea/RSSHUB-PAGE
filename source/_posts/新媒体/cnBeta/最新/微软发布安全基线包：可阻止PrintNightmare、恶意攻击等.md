
---
title: '微软发布安全基线包：可阻止PrintNightmare、恶意攻击等'
categories: 
 - 新媒体
 - cnBeta
 - 最新
headimg: 'https://static.cnbetacdn.com/article/2021/1222/55973b8a936f711.webp'
author: cnBeta
comments: false
date: Wed, 22 Dec 2021 02:39:17 GMT
thumbnail: 'https://static.cnbetacdn.com/article/2021/1222/55973b8a936f711.webp'
---

<div>   
<strong>以 Microsoft Security Configuration Toolkit 的形式，微软今天发布了适用于 Windows 10 21H2 November 2021 功能更新的安全基线（Security Baseline）包。</strong>该工具包提供了一个微软推荐的安全基线，以帮助管理员在不影响安全的前提下更好地管理各种企业组策略对象（GPO）等。<br>
 <p style="text-align:center"><img src="https://static.cnbetacdn.com/article/2021/1222/55973b8a936f711.webp" alt="zv947ujf.webp" referrerpolicy="no-referrer"></p><p style="text-align: left;">对于 Security Configuration Toolkit，微软官方的介绍如下</p><blockquote style="text-align: left;"><p style="text-align: left;">微软 Security Configuration Toolkit 使企业安全管理员能够有效地管理其企业的组策略对象（GPO）。使用该工具包，管理员可以将他们当前的 GPO 与微软推荐的 GPO 基线或其他基线进行比较，编辑它们，以 GPO 备份文件格式存储它们，并通过域控制器应用它们或直接注入测试平台主机以测试它们的效果。</p></blockquote><p style="text-align: left;">新的基线引入了几个新的策略设置，如打印机驱动程序安装限制，以防止像臭名昭著的 PrintNightmare 场景，以及“篡改保护”，这可能有助于防止“人为操作的勒索软件”以及其他威胁。除了这两个，在这个新的基线下，经典版 Edge 设置也被取消了。</p><p style="text-align: left;">就新的打印机驱动程序安装限制而言，微软表示：</p><blockquote style="text-align: left;"><p style="text-align: left;">我们已经在MS安全指南中添加了一个新的设置（Administrative Templates\Printers\Limits print driver installation to Administrators），并强制启用了。注意这个设置以前是SecGuide.admx/l中的一个自定义设置，后来移到了box中。</p></blockquote><p style="text-align: left;">而在谈到篡改保护时，微软表示，该功能可以防止恶意软件。</p><blockquote style="text-align: left;"><p style="text-align: left;">● 禁用病毒和威胁保护</p><p style="text-align: left;">● 禁用实时保护</p><p style="text-align: left;">● 关闭行为监控</p><p style="text-align: left;">● 禁用防病毒软件（如I<a data-link="1" href="https://microsoft.pvxt.net/P0JMe" target="_blank">Office</a>Antivirus（IOAV））。</p><p style="text-align: left;">● 禁用云交付的保护</p><p style="text-align: left;">● 删除安全情报更新</p><p style="text-align: left;">● 禁用对检测到的威胁的自动行动</p></blockquote><p>Source: Microsoft (<a href="https://techcommunity.microsoft.com/t5/microsoft-security-baselines/security-baseline-for-windows-10-version-21h2/ba-p/3042703">1</a>), (<a href="https://techcommunity.microsoft.com/t5/microsoft-security-baselines/windows-11-security-baseline/ba-p/2810772">2</a>)</p>   
</div>
            