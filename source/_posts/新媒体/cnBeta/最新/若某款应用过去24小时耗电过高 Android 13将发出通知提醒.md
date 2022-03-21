
---
title: '若某款应用过去24小时耗电过高 Android 13将发出通知提醒'
categories: 
 - 新媒体
 - cnBeta
 - 最新
headimg: 'https://static.cnbetacdn.com/article/2022/0321/43e058319c1df22.webp'
author: cnBeta
comments: false
date: Mon, 21 Mar 2022 04:13:26 GMT
thumbnail: 'https://static.cnbetacdn.com/article/2022/0321/43e058319c1df22.webp'
---

<div>   
<strong>在今天发布的 Android 13 第 2 个开发者预览版中，引入了一个新的系统通知。当你的应用程序在过去 24 小时内消耗了大量的设备电池时就会出现。</strong>这个新的通知会出现在所有运行在 Android 13 系统的设备上的应用程序，而不考虑目标 SDK 版本。<br>
 <p style="text-align:center"><img src="https://static.cnbetacdn.com/article/2022/0321/43e058319c1df22.webp" alt="ucnkgk56.webp" referrerpolicy="no-referrer"></p><p style="text-align: left;">在衡量你的应用程序对设备电池续航的影响时，系统会考虑到你的应用程序在几个不同地方所做的工作，包括以下内容。</p><p style="text-align: left;">● 前台服务，甚至那些有可见通知的服务</p><p style="text-align: left;">● Work 任务，包括加速的工作</p><p style="text-align: left;">● 广播接收者</p><p style="text-align: left;">● 后台服务</p><p style="text-align: left;">● 你的应用程序的缓存</p><p style="text-align: left;">如果你的应用程序出现这个通知，它不会再次出现在同一设备上，直到至少 24 小时后。如果系统检测到你的应用程序长时间运行一个前台服务--在 24 小时窗口内至少有 20 个小时--它会向用户发送一个通知，邀请他们与前台服务（FGS）任务管理器互动。</p><p style="text-align: left;">这可能都有点技术性，但一个过于简单的解释是，Android 13 现在监控一个应用程序的后台行为的越来越多的方面。不仅如此，还包括一些前台元素，如前台服务。这些是执行需要让用户注意到的操作的服务，并且有一个与之相关的通知，在服务停止或从前台移除之前不能被解除。这类行为的例子有：健身追踪应用程序，因为它们"正在锻炼"，并积极收集数据；或者一个多媒体播放器，与前台服务一起播放，并可能在通知中显示当前歌曲和多媒体控制等内容。</p>   
</div>
            