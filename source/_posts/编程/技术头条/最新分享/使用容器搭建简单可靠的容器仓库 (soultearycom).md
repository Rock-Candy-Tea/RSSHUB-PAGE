
---
title: '使用容器搭建简单可靠的容器仓库 (soulteary.com)'
categories: 
 - 编程
 - 技术头条
 - 最新分享
headimg: 'https://picsum.photos/400/300?random=4217'
author: 技术头条
comments: false
date: 2021-05-28 00:26:09
thumbnail: 'https://picsum.photos/400/300?random=4217'
---

<div>   
提到容器仓库，我们一般会想到 Nexus、Harbor ，那么有没有更轻量可靠的方案呢。尤其是在频繁构建的 CI 流水线中、或是分布式的环境中需要高频拉取镜像的场景中。

《使用容器搭建 APT Cacher NG 缓存代理服务》一文提到了缓存，虽然可以使用文末中的 Nginx 的补充方式来提供容器镜像导出文件的缓存托管，但是这种方式相比较使用镜像仓库而言，不能够直接使用 Docker Client 与之交互，需要借助导出和导入命令，使用起来颇有不便。

本篇文章继续聊聊，如何使用容器搭建轻量可靠的镜像仓库：distribution。
    
</div>
            