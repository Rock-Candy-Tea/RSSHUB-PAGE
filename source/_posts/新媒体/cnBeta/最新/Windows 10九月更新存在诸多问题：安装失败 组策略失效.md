
---
title: 'Windows 10九月更新存在诸多问题：安装失败 组策略失效'
categories: 
 - 新媒体
 - cnBeta
 - 最新
headimg: 'https://static.cnbetacdn.com/article/2022/0916/d8274eead365f99.webp'
author: cnBeta
comments: false
date: Fri, 16 Sep 2022 09:03:23 GMT
thumbnail: 'https://static.cnbetacdn.com/article/2022/0916/d8274eead365f99.webp'
---

<div>   
在本月的补丁星期二活动日中，微软发布了适用于 Windows 10 的累积更新 KB5017308，引入了大量安全更新。<strong>不过部分用户在升级过程中出现了一些问题，其中一名用户反馈出现无法安装问题，出现 0x800f081f 错误。</strong><br>
<p><img src="https://static.cnbetacdn.com/article/2022/0916/d8274eead365f99.webp" alt="5esg629a.webp" referrerpolicy="no-referrer"></p><p>此外还有用户反馈在安装过程中出现了 0x8000ffff、0x8007007e 和 0x80073701 不同的错误，更糟糕的情况下，该更新会让系统进入无限重启循环中。目前尚不确定有多少用户受到影响。</p><p>微软从未真正承认 <a data-link="1" href="https://microsoft.pvxt.net/x9Vg1" target="_blank">Windows</a> 更新安装失败的报告，也没有官方修复。但是，一些用户反馈从 Microsoft Update Catalog 来离线安装更新确实可以解决那些受影响的问题。</p><p>此外，还有用户反馈本次更新破坏了 GPO 的“Files”组策略。根据 Reddit 网友反馈，在用户复制批处理文件到 public\documents 路径下，创建副本或桌面快捷方式时，图标不会被迁移，而且快捷方式会使用空白的默认图标。在某些情况下，批处理文件在复制时实际上是空的。</p><p>其中一名受影响的用户反馈道：“我的一些客户报告说 KB5017308 破坏了 Active Directory 组策略中的‘Replace’选项，尤其是在用户策略（在计算机策略中不使用）和选中‘在登录用户的安全情境中运行’复选框的情况下”。</p>   
</div>
            