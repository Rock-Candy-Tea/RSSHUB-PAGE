
---
title: 'Linux提权手法实战 (blog.nsfocus.net)'
categories: 
 - 编程
 - 技术头条
 - 最新分享
headimg: 'https://picsum.photos/400/300?random=3094'
author: 技术头条
comments: false
date: 2022-09-06 09:10:01
thumbnail: 'https://picsum.photos/400/300?random=3094'
---

<div>   
Linux对不同角色的用户进行了权限管控，提权意味着用户获得不允许他使用的权限。  比如可以通过提权将用户的角色由普通用户变为管理员，从而获得更高的访问权限，执行相应的高危操作。提权是渗透流程中非常重要的一环，很大程度上决定本次渗透的最终成果。Linux提权的常见手法有以下几种：内核漏洞提权、定时任务提权、SUID提权、SUDO滥用提权、NFS提权、Docker组提权，下面逐一介绍。
    
</div>
            