
---
title: 'Android 13可按需关闭PhantomProcessKiller 告别疯狂杀后台'
categories: 
 - 新媒体
 - cnBeta
 - 最新
headimg: 'https://static.cnbetacdn.com/thumb/article/2021/1214/e567977e9870dc4.jpg'
author: cnBeta
comments: false
date: Tue, 14 Dec 2021 11:55:13 GMT
thumbnail: 'https://static.cnbetacdn.com/thumb/article/2021/1214/e567977e9870dc4.jpg'
---

<div>   
用上Android 12了吗？业内认为，从底层功能的角度，Android 12在隐私、省电、安全、通知等方面的改动甚至重构看成是Android
5.0后最大的一次升级。不过，可能是省电策略过于激进，安卓12中存在名为PhantomProcessKiller（幽灵进程杀手）的程序，造成了对部分网友很困扰的疯狂杀后台问题。<br>
 <p>简单来说，<strong>PhantomProcessKiller会检测使用CPU过多的程序，如果此时父进程在后台，会将其触发的子进程全部杀死。同时，PhantomProcessKiller也限制父进程最多可触发32个子进程。</strong></p><p>好在从谷歌向AOSP提交的新贡献显示，未来允许在开发者选项中按需关闭PhantomProcessKiller。</p><p>常年研究安卓代码的民间大神认为，该功能有望在Android 13上实现。</p><p><a href="https://img1.mydrivers.com/img/20211214/911add27c9c6437baf4d17047461d018.jpg" target="_blank"></a><a target="_blank" href="https://static.cnbetacdn.com/article/2021/1214/e567977e9870dc4.jpg"><img data-original="https://static.cnbetacdn.com/article/2021/1214/e567977e9870dc4.jpg" src="https://static.cnbetacdn.com/thumb/article/2021/1214/e567977e9870dc4.jpg" referrerpolicy="no-referrer"></a></p>   
</div>
            