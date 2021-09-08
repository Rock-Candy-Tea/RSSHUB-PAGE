
---
title: 'Firefox 94计划为卸载标签功能引入about_unloads页面'
categories: 
 - 新媒体
 - cnBeta
 - 最新
headimg: 'https://static.cnbetacdn.com/thumb/article/2021/0908/450d4154a13a2cf.jpg'
author: cnBeta
comments: false
date: Wed, 08 Sep 2021 03:28:12 GMT
thumbnail: 'https://static.cnbetacdn.com/thumb/article/2021/0908/450d4154a13a2cf.jpg'
---

<div>   
日前，本站曾报道 Firefox 93 中将恢复自动卸载标签（Tab Unloading）功能，也就是当系统内存不足的时候会自动卸载标签页。<strong>此外，Mozilla 也在准备类似于 chrome://discards 的页面，在 Firefox 94 版本中正测试 about:unloads 页面。</strong><br>
 <p style="text-align:center"><a href="https://static.cnbetacdn.com/article/2021/0908/450d4154a13a2cf.jpg" target="_blank"><img src="https://static.cnbetacdn.com/thumb/article/2021/0908/450d4154a13a2cf.jpg" referrerpolicy="no-referrer"></a></p><p style="text-align: left;">事实上早在 Firefox 67 版本中，Mozilla 就实施了一个节省内存的功能。该公司无法弄清用户设备上的低内存状况，因此该功能被撤消。</p><p style="text-align: left;">about:unloads 页面在 Firefox 地址栏中被访问时，给出了 Firefox 如何优先处理标签的基本概念，以及如果标签卸载变得活跃，哪个标签会被卸载。该页面还提供了卸载按钮来丢弃一个标签。</p><p style="text-align: left;">当用户点击一个被丢弃的标签时，它将再次被重新加载。该表包含7列。优先级，主机，最后访问，基本权重，第二权重，内存，和进程IDs。当该功能触发时，基于优先级的标签就会失去作用，资源就会被释放，从而使系统内存恢复正常，Firefox就会重新变得流畅和有反应。进程 ID 在标签页顶部框架中显示为粗体，当进程在不同标签页之间共享时显示为斜体。</p><p style="text-align:center"><a href="https://static.cnbetacdn.com/article/2021/0908/1829ac84655dd11.jpg" target="_blank"><img src="https://static.cnbetacdn.com/thumb/article/2021/0908/1829ac84655dd11.jpg" referrerpolicy="no-referrer"></a></p><p style="text-align: left;">这很可能类似于Firefox中的任务管理器或about:performance页面。它显示标签的标题、类型、能量影响和标签所消耗的内存。要在Firefox中打开TM，点击菜单>更多工具，选择任务管理器。</p><p style="text-align: left;">about:unloads 和 about:performance 的区别在于，前者允许你按需丢弃标签，而后者让你在发现标签占用系统内存和CPU的时候杀掉它们。</p>   
</div>
            