
---
title: 'K8S Event事件内容分析和告警 (www.ipcpu.com)'
categories: 
 - 编程
 - 技术头条
 - 最新分享
headimg: 'https://picsum.photos/400/300?random=160'
author: 技术头条
comments: false
date: 2022-08-18 15:18:58
thumbnail: 'https://picsum.photos/400/300?random=160'
---

<div>   
k8s的Event事件是一种资源对象，用于展示集群内发生的情况，k8s系统中的各个组件会将运行时发生的各种事件上报给apiserver 。可以通过kubectl get event 或 kubectl describe pod podName 命令显示事件，查看k8s集群中发生了哪些事件。 

    apiserver 会将Event事件存在etcd集群中，为避免磁盘空间被填满，故强制执行保留策略：在最后一次的事件发生后，删除1小时之前发生的事件。
    
</div>
            