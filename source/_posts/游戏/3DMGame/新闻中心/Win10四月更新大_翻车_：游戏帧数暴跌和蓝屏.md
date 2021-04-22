
---
title: 'Win10四月更新大_翻车_：游戏帧数暴跌和蓝屏'
categories: 
 - 游戏
 - 3DMGame
 - 新闻中心
headimg: 'https://img.3dmgame.com/uploads/images/news/20210422/1619061898_349584.jpg'
author: 3DMGame
comments: false
date: Thu, 22 Apr 2021 03:25:00 GMT
thumbnail: 'https://img.3dmgame.com/uploads/images/news/20210422/1619061898_349584.jpg'
---

<div>   
<p style="text-indent:2em;">
不久前，微软向Win10推送了今年的四月累积更新，其代号为KB5001330。该更新旨在修复之前的多个安全漏洞以及其他问题，例如打印机驱动的兼容问题等等。
</p>
<p style="text-indent:2em;">
然而，这次的更新似乎又引发了不少新问题，每次更新在修复Bug的同时引入新故障，俨然成为了Win10系统的新常态。
</p>
<p align="center">
<img src="https://img.3dmgame.com/uploads/images/news/20210422/1619061898_349584.jpg" alt="Win10四月更新大“翻车”：游戏帧数暴跌和蓝屏" referrerpolicy="no-referrer">
</p>
<p style="text-indent:2em;">
根据Windows Lastest的报道，Win10四月累积更新KB5001330在推送后，从多个社交媒体以及反馈中心上，都可以观察到有为数不少用户提交的问题报告。
</p>
<h3 style="text-indent:2em;">
安装错误Bug
</h3>
<p style="text-indent:2em;">
这是本次升级更新用户反馈的问题，这会导致KB5001330补丁安装失败、系统无法更新到四月累积更新。这些错误会伴随着以下代码。
</p>
<p style="text-indent:2em;">
·0x800f081f
</p>
<p style="text-indent:2em;">
·0x800f0984
</p>
<p style="text-indent:2em;">
·0x800f0922
</p>
<p style="text-indent:2em;">
其中，0x800f081f错误出现在下载KB5001330补丁的时候，用户反馈称，在尝试下载安装KB5001330时，遇到了该错误代码，并提示“已执行标准DISM和SFC命令，进行了Windows Update的基本重置。”
</p>
<p style="text-indent:2em;">
而0x800f0984错误代码则出现在Suface Studio和Surface Pro 7上，用户反馈称安装四月更新无法顺利完成，会在安装进度20%的时候暂停，接着进度跳转到73%，接而安装进度为100%，但最后会安装失败。
</p>
<h3 style="text-indent:2em;">
临时用户配置文件Bug
</h3>
<p style="text-indent:2em;">
在某些情况下，KB5001330补丁还会导致重现之前就臭名昭著的用户档案Bug。在去年12月，这个问题就已经被发现，具体表现为当安装了累积更新后，系统会创建全新的用户配置文件，这导致用户之前的文件和设置（例如壁纸）会消失不见。
</p>
<p style="text-indent:2em;">
有用户反馈称，更新后甚至无法登录进电脑，因为系统提示成用户配置文件服务失败，无法加载配置文件。有用户则表示，由于这个Bug导致无法使用管理员账户，因此无法对电脑进行操作，不得不将电脑重新返厂重置才得以解决。
</p>
<p style="text-indent:2em;">
所幸该问题并非完全无法解决，用户可以重新回滚更新或者手动备份用户文件，来避免问题。
</p>
<h3 style="text-indent:2em;">
游戏帧数暴跌和蓝屏死机
</h3>
<p style="text-indent:2em;">
对于游戏玩家来说，四月更新也会带来问题。有用户在社区中反馈，本次更新会导致某些游戏渲染异常。
</p>
<p style="text-indent:2em;">
例如，某些游戏可能会崩溃，或者存在卡顿和帧率下降的问题，而卸载了本次四月累积更新后就再也没有出现过。不过这些问题只有少数用户反馈，似乎并没有像其他故障一样广泛存在。
</p>
<p style="text-indent:2em;">
而就如以往每次更新一样，Win10四月累积更新也会导致蓝屏死机。用户反馈称，升级后电脑在几个小时内就出现了两次蓝屏死机，这并非是孤例。
</p>
<h3 style="text-indent:2em;">
DNS问题
</h3>
<p style="text-indent:2em;">
媒体还发现有用户出现了DNS和共享文件夹相关的故障。在支持文档中，有人找到了解决该问题的方案。
</p>
<p style="text-indent:2em;">
如果想要修正DNS和共享文件夹的故障，可以尝试以下步骤：
</p>
<p style="text-indent:2em;">
·开启组策略编辑器，并进入“计算机配置-管理模版-网络-DNS客户端”；
</p>
<p style="text-indent:2em;">
·双击“关闭多播名称解析”；
</p>
<p style="text-indent:2em;">
·将其设定为“已禁用”；
</p>
<p style="text-indent:2em;">
·点击“确定”
</p>
<p style="text-indent:2em;">
随后，开启CMD并使用以下命令刷新DNS。
</p>
<p style="text-indent:2em;">
ipconfig /flushdns
</p>
<p style="text-indent:2em;">
简单来说，Win10四月累积更新的确存在一些Bug，如果你不幸遇到，可以使用以下方法回滚系统。
</p>
<p style="text-indent:2em;">
·开启设置面板
</p>
<p style="text-indent:2em;">
·点击“更新和安全”
</p>
<p style="text-indent:2em;">
·点击“Windows Update”
</p>
<p style="text-indent:2em;">
·点击“查看更新历史”
</p>
<p style="text-indent:2em;">
·选中KB5001330更新并卸载它，随后重启系统。
</p>
<p style="text-indent:2em;">
总的来说，Win10的每次更新似乎都会带来新问题。微软将会在今年下半年推出Win10近年最大的更新21H2，它的稳定性表现会如何？希望不会令人失望吧。
</p>
<p align="center">
<img src="https://img.3dmgame.com/uploads/images/news/20210422/1619061918_311272.jpg" alt="Win10四月更新大“翻车”：游戏帧数暴跌和蓝屏" referrerpolicy="no-referrer">
</p>          
</div>
            