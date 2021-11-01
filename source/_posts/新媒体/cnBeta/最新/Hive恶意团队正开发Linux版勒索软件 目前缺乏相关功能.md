
---
title: 'Hive恶意团队正开发Linux版勒索软件 目前缺乏相关功能'
categories: 
 - 新媒体
 - cnBeta
 - 最新
headimg: 'https://static.cnbetacdn.com/thumb/article/2021/1101/ac63431b99a25dd.jpg'
author: cnBeta
comments: false
date: Sun, 31 Oct 2021 23:55:39 GMT
thumbnail: 'https://static.cnbetacdn.com/thumb/article/2021/1101/ac63431b99a25dd.jpg'
---

<div>   
利用专门针对 Linux 和 FreeBSD 等发行版本开发的恶意程序变种，Hive 勒索软件团队正对这些平台发起攻击。<strong>正如斯洛伐克互联网安全公司 ESET 所发现的，Hive 的新加密器仍在开发中，不过缺乏相关功能。</strong><br>
 <p style="text-align:center"><a href="https://static.cnbetacdn.com/article/2021/1101/ac63431b99a25dd.jpg" target="_blank"><img src="https://static.cnbetacdn.com/thumb/article/2021/1101/ac63431b99a25dd.jpg" referrerpolicy="no-referrer"></a></p><p style="text-align: left;">根据 ESET 分析的样本中，针对 Linux 平台的恶意程序仍存在不少问题。当这些恶意软件以绝对路径执行的时候，加密会完全失效。</p><p style="text-align:center"><a href="https://static.cnbetacdn.com/article/2021/1101/7bf8c698a439293.jpg" target="_blank"><img src="https://static.cnbetacdn.com/thumb/article/2021/1101/7bf8c698a439293.jpg" referrerpolicy="no-referrer"></a></p><p style="text-align: left;">它支持的命令行参数只有一个（-no-wipe）。相比之下，Hive 的 <a data-link="1" href="https://microsoft.pvxt.net/x9Vg1" target="_blank">Windows</a> 勒索软件有多达 5 个执行选项，包括杀死进程和跳过磁盘清理、不感兴趣的文件和旧文件。</p><p style="text-align: left;">该勒索软件的 Linux 版本如果在没有 root 权限的情况下执行，也无法触发加密，因为它试图在被攻击设备的根文件系统上要求支付赎金。</p><p style="text-align:center"><img src="https://static.cnbetacdn.com/article/2021/1101/7886649c34549f5.jpg" referrerpolicy="no-referrer"></p><p style="text-align: left;">ESET 研究实验室说：“就像 Windows 版本一样，这些变种是用 Golang 编写的，但字符串、包名和函数名已经被混淆，可能是用 gobfuscate 编写的”。</p><p style="text-align: left;">Hive 是一个至少从 2021 年 6 月开始活跃的勒索软件集团，已经袭击了 30 多个组织，只计算拒绝支付赎金的受害者。他们只是许多勒索软件团伙中的一个，在他们的企业目标慢慢迁移到虚拟机以方便设备管理和更有效地利用资源之后，他们开始瞄准 Linux 服务器。</p>   
</div>
            