
---
title: '通过 MicroK8s 搭建你的 K8s 环境 (soulteary.com)'
categories: 
 - 编程
 - 技术头条
 - 最新分享
headimg: 'https://picsum.photos/400/300?random=3351'
author: 技术头条
comments: false
date: 2022-06-19 15:08:42
thumbnail: 'https://picsum.photos/400/300?random=3351'
---

<div>   
去年的时候，我曾经写过如何[简单搭建 Kubernetes 集群]，当时使用的是官方的工具箱：Kubeadm，这个方案对于只是想试试的同学来说，还是过于复杂。这里介绍一款简单的工具：MicroK8s。官方给这款工具的人设是“无需运维的 Kubernetes ，服务于工作站、物联网。”最大的价值在于可以快速搭建单节点的容器编排系统，用于生产试验。[官方网站]里的文档有简单介绍如何安装使用，但是却未曾考虑安装过程存在网络问题的神州大陆的同学们，本文将结合这种情况聊聊。
    
</div>
            