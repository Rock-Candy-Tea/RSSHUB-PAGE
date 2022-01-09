
---
title: '恶意软件可令iPhone假装关机并监控用户隐私'
categories: 
 - 新媒体
 - cnBeta
 - 最新
headimg: 'https://static.cnbetacdn.com/thumb/article/2022/0109/636a6003a5b8a7e.png'
author: cnBeta
comments: false
date: Sun, 09 Jan 2022 12:57:17 GMT
thumbnail: 'https://static.cnbetacdn.com/thumb/article/2022/0109/636a6003a5b8a7e.png'
---

<div>   
国外安全人员ZecOps近日开发了一项名为NoReboot的技术，可以让iPhone实现伪装关机，并且偷窃用户隐私。这项技术模拟了用户关机/重启的情景，来电铃声和信息通知、3D
Touch、震动、屏幕、相机指示灯等物理反馈也会被禁用，同时还会伪造Apple的经典开关机动画来误导用户以为已经完成了操作，但实际上还在联网状态中。<br>
 <p><strong>在“假关机”状态下，攻击者可悄悄远程访问用户<a data-link="1" href="https://c.duomai.com/track.php?site_id=242986&euid=&t=https://shouji.jd.com/" target="_blank">手机</a>的麦克风和摄像头，或者在不提醒用户的情况下做几乎任何他们想做的事情。</strong></p><p>通常情况下，重启<a data-link="1" href="https://apple.pvxt.net/c/1251234/435400/7639?u=https%3A%2F%2Fwww.apple.com%2Fcn%2Fiphone%2F" target="_blank">iPhone</a>可直接清除恶意软件的劫持代码。但是，NoReboot技术可在iPhone恢复开机状态时直接进行劫持，所以用户即便“真重启”也无济于事。</p><p>“NoReboot”的工作原理是将恶意代码注入InCallService、SpringBoard和backboardd这三个后台进程，它们负责iPhone的重新启动过程。</p><p>ZecOps表示，此问题无法通过补丁修复，并且可运行在任何iOS版本的iPhone上。</p><p><a href="https://img1.mydrivers.com/img/20220109/7cbb3ae5-be97-4786-8674-961f97366588.png" target="_blank"></a><a target="_blank" href="https://static.cnbetacdn.com/article/2022/0109/636a6003a5b8a7e.png"><img data-original="https://static.cnbetacdn.com/article/2022/0109/636a6003a5b8a7e.png" src="https://static.cnbetacdn.com/thumb/article/2022/0109/636a6003a5b8a7e.png" referrerpolicy="no-referrer"></a></p>   
</div>
            