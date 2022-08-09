
---
title: 'HttpClient设置不当引发的一次雪崩，整个项目组慌了！ (mp.weixin.qq.com)'
categories: 
 - 编程
 - 技术头条
 - 最新分享
headimg: 'https://picsum.photos/400/300?random=2388'
author: 技术头条
comments: false
date: 2022-08-09 05:19:38
thumbnail: 'https://picsum.photos/400/300?random=2388'
---

<div>   
我最近运维了一个网上的实时接口服务，最近经常出现Address already in use (Bind failed)的问题。



很明显是一个端口绑定冲突的问题，于是大概排查了一下当前系统的网络连接情况和端口使用情况，发现是有大量time_wait的连接一直占用着端口没释放，导致端口被占满（最高的时候6w+个），因此HttpClient建立连接的时候会出现申请端口冲突的情况。
    
</div>
            