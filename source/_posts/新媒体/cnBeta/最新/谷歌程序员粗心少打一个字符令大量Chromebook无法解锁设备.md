
---
title: '谷歌程序员粗心少打一个字符令大量Chromebook无法解锁设备'
categories: 
 - 新媒体
 - cnBeta
 - 最新
headimg: 'https://static.cnbetacdn.com/article/2021/0724/bf81a011228e3a6.png'
author: cnBeta
comments: false
date: Sat, 24 Jul 2021 09:07:05 GMT
thumbnail: 'https://static.cnbetacdn.com/article/2021/0724/bf81a011228e3a6.png'
---

<div>   
近日，谷歌为Chromebook推送了ChromeOS
91，具体版本号为91.0.4772.165。但是，这次更新出现重大Bug，导致用户的ChromeBook无法正常解锁，官方已经紧急撤销更新。多数用户反馈，在更新到此版本后，在登录时即便输入了正确的密码，但还是卡在了锁屏界面，无法正常进入桌面，有的设备甚至会循环重启。<br>
<p>而开发者从谷歌官网的源码中发现，这个问题是由一个低级错误引发的。</p><p>从下图可以看出，判断两个条件之间“&&”，但是程序员漏打了一个“&”，导致系统无法正常对设备解密登陆。</p><p><img src="https://static.cnbetacdn.com/article/2021/0724/bf81a011228e3a6.png" referrerpolicy="no-referrer"></p><p>现在谷歌已经紧急发布修复补丁，解决了这个低级错误。</p><p><img src="https://static.cnbetacdn.com/article/2021/0724/22d79dac1680ef8.png" referrerpolicy="no-referrer"></p>   
</div>
            