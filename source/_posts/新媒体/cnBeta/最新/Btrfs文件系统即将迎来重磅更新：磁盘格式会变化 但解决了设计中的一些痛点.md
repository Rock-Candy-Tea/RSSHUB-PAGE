
---
title: 'Btrfs文件系统即将迎来重磅更新：磁盘格式会变化 但解决了设计中的一些痛点'
categories: 
 - 新媒体
 - cnBeta
 - 最新
headimg: 'https://static.cnbetacdn.com/article/2021/1102/966afd99d60ef74.jpg'
author: cnBeta
comments: false
date: Fri, 12 Nov 2021 03:24:49 GMT
thumbnail: 'https://static.cnbetacdn.com/article/2021/1102/966afd99d60ef74.jpg'
---

<div>   
<strong>知名 Btrfs 文件系统开发者 Josef Bacik 正在筹备一个重磅更新。本次更新虽然会导致磁盘格式发生变化，但解决了文件系统设计中的一些“更糟糕的部分”。</strong>在接下来的一年里，Josef 希望通过这些改变来解决全局根文件系统中的锁争夺以及块组项目在整个范围树上的传播问题。<br>
 <p style="text-align:center"><img src="https://static.cnbetacdn.com/article/2021/1102/966afd99d60ef74.jpg" referrerpolicy="no-referrer"></p><p style="text-align: left;">Bacik 正在“extent-tree-v2”标签下开发这项工作，到目前为止已经有大约80个补丁，不过这才刚刚开始。他希望在接下来的 6~12 个月内，用户可以开始迁移到 Btrfs 的设计改进中。</p><p style="text-align:center"><a href="https://static.cnbetacdn.com/article/2021/1112/954e0256212564b.png" target="_blank"><img src="https://static.cnbetacdn.com/thumb/article/2021/1112/954e0256212564b.png" alt="Screenshot 2021-11-12 at 11-21-41 Extent-tree-v2 Global Roots and Block Group Root.png" referrerpolicy="no-referrer"></a></p><p style="text-align: left;">不过这项工作会对磁盘格式发生变化，用户将需要把他们的 Btrfs 文件系统转换为更新的格式，但这样会失去在在旧内核上安装文件系统的支持。一些用户一开始可能对改变磁盘格式有点紧张，这是可以理解的，但希望新版本将被证明是一个有用（和可靠）的改进。</p>   
</div>
            