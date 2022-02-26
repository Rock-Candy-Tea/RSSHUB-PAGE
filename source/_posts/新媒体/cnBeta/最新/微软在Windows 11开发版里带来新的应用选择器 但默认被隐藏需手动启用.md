
---
title: '微软在Windows 11开发版里带来新的应用选择器 但默认被隐藏需手动启用'
categories: 
 - 新媒体
 - cnBeta
 - 最新
headimg: 'https://static.cnbetacdn.com/thumb/article/2022/0226/f89fb806677d8a3.png'
author: cnBeta
comments: false
date: Sat, 26 Feb 2022 05:32:37 GMT
thumbnail: 'https://static.cnbetacdn.com/thumb/article/2022/0226/f89fb806677d8a3.png'
---

<div>   
应用选择器指的是当我们打开某个文件时系统弹出的应用选择窗口，其实也就是我们右键点击文件然后选择打开方式时弹出的窗口。Windows 11正式版通道继续沿用此前的应用选择器，不过在最新开发版里微软已经使用 Mica 云母材料语言更换新设计。<br>
 新的应用选择器整体风格已经好看许多，尤其是背景已经换成半透明样式，同时原来硕大的滚动条也已经被替换。<p>要使用新版应用选择器我们需要更新至<a data-link="1" href="https://microsoft.pvxt.net/x9Vg1" target="_blank">Windows</a> 11 Dev Build 22563版 , 然后使用ViveTool工具开启配置选项。</p><p><strong>新版应用选择器这样：</strong></p><p><a href="https://img.lancdn.com/landian/2022/02/92749-1.png" target="_blank" rel="noopener"></a><a target="_blank" href="https://static.cnbetacdn.com/article/2022/0226/f89fb806677d8a3.png"><img data-original="https://static.cnbetacdn.com/article/2022/0226/f89fb806677d8a3.png" src="https://static.cnbetacdn.com/thumb/article/2022/0226/f89fb806677d8a3.png" referrerpolicy="no-referrer"></a><br></p><p><strong>当前稳定版的应用选择器：</strong></p><p><a href="https://img.lancdn.com/landian/2022/02/92749-2.png" target="_blank" rel="noopener"></a><a target="_blank" href="https://static.cnbetacdn.com/article/2022/0226/0826532537b68d4.png"><img data-original="https://static.cnbetacdn.com/article/2022/0226/0826532537b68d4.png" src="https://static.cnbetacdn.com/thumb/article/2022/0226/0826532537b68d4.png" referrerpolicy="no-referrer"></a><br></p><p><strong>开启方法：</strong></p><p>新版应用选择器默认并未开启且<a data-link="1" href="https://c.duomai.com/track.php?site_id=242986&euid=&t=https://www.microsoftstore.com.cn/" target="_blank">微软</a>在博客中也没提，不过我们可以使用ViveTool工具手动开启新版应用选择器。</p><p>如果你从未使用过ViveTool请先点击这里下载：<a href="https://www.landian.vip/archives/92272.html" target="_blank" rel="noopener">[图文</a><a data-link="1" href="https://c.duomai.com/track.php?k=iRyUSQzUycwRHdo1Ddm0DZpVXZmkDN2ITPklWYmYDO5IDNy0DZp9VZ0l2cmUmchdHdm92cGJTJjZkMl42Yu02bj5SZy9GdzRnZvN3byNWat5yd3dnRyU" target="_blank">教程</a>] Windows 11开发版必备神器 ViveTool 到底怎么用？</p><p>本次我们需要使用的命令如下，另外这里提下这些特性既然可以开启自然也可以关闭，如果你不喜欢可以改回去。</p><pre>#打开管理员模式的命令提示符(CMD) 注：因为某些问题使用PowerShell可能无法启用#开启新版应用选择器
.\vivetool addconfig 363020902#操作成功后立即生效无需重启系统
#关闭新版应用选择器
.\vivetool delconfig 363020902
#常用参数说明
addconfig #添加功能
delconfig #删除功能</pre><p><strong>操作配图：</strong></p><p><a href="https://img.lancdn.com/landian/2022/02/92749-3.png" target="_blank" rel="noopener"></a><a target="_blank" href="https://static.cnbetacdn.com/article/2022/0226/db88f22dd8b3582.png"><img data-original="https://static.cnbetacdn.com/article/2022/0226/db88f22dd8b3582.png" src="https://static.cnbetacdn.com/thumb/article/2022/0226/db88f22dd8b3582.png" referrerpolicy="no-referrer"></a><br></p>   
</div>
            