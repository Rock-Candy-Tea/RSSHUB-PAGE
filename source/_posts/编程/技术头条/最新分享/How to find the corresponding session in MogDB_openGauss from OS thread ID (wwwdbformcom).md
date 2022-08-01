
---
title: 'How to find the corresponding session in MogDB_openGauss from OS thread ID (www.dbform.com)'
categories: 
 - 编程
 - 技术头条
 - 最新分享
headimg: 'https://picsum.photos/400/300?random=2906'
author: 技术头条
comments: false
date: 2022-08-01 01:00:19
thumbnail: 'https://picsum.photos/400/300?random=2906'
---

<div>   
当MogDB数据库由于某种原因占用了较大的系统负载，比如CPU占用接近100%，那么如何知道到底是数据库里的哪个会话或者哪些会话占用了资源？
在Oracle数据库中，这样的问题诊断，通常都会关联 v$session, v$process, 以及操作系统top命令或者ps命令中查到的操作系统进程ID。
但是MogDB本身是线程模型，在操作系统上只能看到一个进程号，那么该如何定位问题？
    
</div>
            