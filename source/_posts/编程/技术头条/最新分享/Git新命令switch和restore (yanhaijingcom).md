
---
title: 'Git新命令switch和restore (yanhaijing.com)'
categories: 
 - 编程
 - 技术头条
 - 最新分享
headimg: 'https://picsum.photos/400/300?random=9277'
author: 技术头条
comments: false
date: 2021-04-28 08:08:48
thumbnail: 'https://picsum.photos/400/300?random=9277'
---

<div>   
最近发现git在修改完文件后，提示恢复修改的命令是restore，如下所示，印象中应该是checkout，所以就研究了下，总结一下分享给大家。

git中的checkout命令承载了分支操作和文件恢复的部分功能，有点复杂，并且难以使用和学习，所以社区解决将这两部分功能拆分开，在git 2.23.0中引入了两个新的命令switch和restore用来取代checkout

下面分别来说说分支操作和文件恢复。

    
</div>
            