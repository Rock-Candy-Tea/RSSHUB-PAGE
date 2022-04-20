
---
title: 'Android 13将整合MGLRU：缓解杀后台问题'
categories: 
 - 新媒体
 - cnBeta
 - 最新
headimg: 'https://static.cnbetacdn.com/article/2022/0420/bf7c79c791d680a.webp'
author: cnBeta
comments: false
date: Wed, 20 Apr 2022 06:52:53 GMT
thumbnail: 'https://static.cnbetacdn.com/article/2022/0420/bf7c79c791d680a.webp'
---

<div>   
Android 系统最令人沮丧的体验之一就是杀后台。后台应用被杀后通知可能会停止推送，虽然部分厂商在后台应用优化方面做的比较好，但几乎所有手机都会出现这样的问题。<strong>不过在即将到来的 Android 13 系统中，有望缓解这个问题。</strong><br>
 <p style="text-align:center"><img src="https://static.cnbetacdn.com/article/2022/0420/bf7c79c791d680a.webp" alt="svcniwga.webp" referrerpolicy="no-referrer"></p><p style="text-align: left;">名为“Multi-Generational Least Recently Used”（MGLRU）的功能已经在 Chrome OS 上线，该公司在“4.14 和 5.15 之间的一些不同内核”上维护 MGLRU。现在看来，Google 计划将 MGLRU 整合到 Android 系统中。</p><p style="text-align: left;">Android Gerrit 上的一条 commit，Google 已经合并了 Android 13 的通用内核图像（GKI）的变化，另一个 commit 显示，很快甚至有可能通过 adb 启用它。</p><p style="text-align:center"><a href="https://static.cnbetacdn.com/article/2022/0420/b24d77a81dab2df.jpg" target="_blank"><img src="https://static.cnbetacdn.com/thumb/article/2022/0420/b24d77a81dab2df.jpg" referrerpolicy="no-referrer"></a></p><p style="text-align:center"><a href="https://static.cnbetacdn.com/article/2022/0420/14b9141c192a825.jpg" target="_blank"><img src="https://static.cnbetacdn.com/thumb/article/2022/0420/14b9141c192a825.jpg" referrerpolicy="no-referrer"></a></p><p style="text-align: left;">该功能实现了两个主要目标：第一个是Google发现 kswapd 的 CPU 使用量减少了 40%，第二个是Google发现 Android 上的内存不足（OOM）的应用杀戮减少了18%。</p><p style="text-align: left;">同一位Google工程师说，该公司在“一百万台” Android 设备上测试了 MGLRU，这似乎是指 Chrome OS 虚拟机上的 Android 运行时间（ARCVM），它为Chrome OS上的 Android 11提供动力。他们写道：“我们已经看到了CPU利用率和内存压力方面的实质性改进，从而减少了OOM杀戮，降低了UI延迟”。</p>   
</div>
            