
---
title: '微软Outlook阅读Uber收据邮件时会崩溃'
categories: 
 - 新媒体
 - cnBeta
 - 最新
headimg: 'https://static.cnbetacdn.com/article/2022/0802/44c5af95ba7e3f2.webp'
author: cnBeta
comments: false
date: Tue, 02 Aug 2022 07:35:21 GMT
thumbnail: 'https://static.cnbetacdn.com/article/2022/0802/44c5af95ba7e3f2.webp'
---

<div>   
<strong>微软表示在打开和阅读包含复杂表格文件（例如 Uber 收据）的电子邮件时，Outlook 就会崩溃。</strong>在支持文档中，微软解释道：“在打开、回复和转发包含复杂表格的某些电子邮件，Outlook 可能会停止响应”。<br>
 <p style="text-align:center"><img src="https://static.cnbetacdn.com/article/2022/0802/44c5af95ba7e3f2.webp" alt="fa1l0tgm.webp" referrerpolicy="no-referrer"></p><p style="text-align: left;">而更糟糕的是，包含相同表格内容的电子邮件也会导致 Microsoft Word 应用停止响应。目前已经确认这个问题影响 Current Channel Version 2206 Build 15330.20196 及更高版本的 Microsoft 365 用户，目前 Beta 和 Current 频道的预览版中这个问题也会触发卡死。</p><p style="text-align: left;">微软 Word 团队表示已经开发了修复补丁，在经过内部认证之后即将会面向 Beta 频道用户开放。微软表示在本月的补丁星期二活动（8 月 9 日）中，目前 Current 频道的 Outlook 用户都会得到修复。</p><p style="text-align: left;">对于无法等待的用户，微软也提供了一个临时的解决方案</p><p style="text-align: left;">1. 以管理员权限打开命令提示符窗口</p><p style="text-align: left;">2. 在命令行窗口输入或者复制以下两条命令，输入完成之后分别按回车生效</p><p style="text-align: left;">cd %programfiles%\Common Files\Microsoft Shared\ClickToRun</p><p style="text-align: left;">officec2rclient.exe /update user updatetoversion=16.0.15225.20288</p>   
</div>
            