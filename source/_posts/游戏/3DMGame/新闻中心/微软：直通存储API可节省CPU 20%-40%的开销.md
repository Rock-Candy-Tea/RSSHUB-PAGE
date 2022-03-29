
---
title: '微软：直通存储API可节省CPU 20%-40%的开销'
categories: 
 - 游戏
 - 3DMGame
 - 新闻中心
headimg: 'https://img.3dmgame.com/uploads/images/news/20220329/1648511190_502788.jpg'
author: 3DMGame
comments: false
date: Mon, 28 Mar 2022 23:47:00 GMT
thumbnail: 'https://img.3dmgame.com/uploads/images/news/20220329/1648511190_502788.jpg'
---

<div>   
<p style="text-indent:2em;">
本月早些时候，微软公开推出了直通存储API（DirectStorage API），该设计是为了克服Win32 
API在最近游戏上存在的输入/输出（IO）瓶颈。
</p>
<p align="center">
<img src="https://img.3dmgame.com/uploads/images/news/20220329/1648511190_502788.jpg" alt="微软：直通存储API可节省CPU 20%-40%的开销" referrerpolicy="no-referrer">
</p>
<p style="text-indent:2em;">
在GDC 2022上，微软软件工程师Cooper 
Partin讨论了优化直通存储在Windows上的IO性能。他说Windows版的直通存储API并不是Xbox Series 
S|X版本的直接移植，Windows版本已经被重新设计以满足PC系统的独特需求。
</p>
<p style="text-indent:2em;">
最令人兴奋的地方在于，Partin表示该API可以为CPU节省20%-40%的工作，前提是你是Windows11系统+NVMe 
SSD。游戏开发者可以使用这些CPU循环去做其他事情。
</p>
<p style="text-indent:2em;">
“DirectStorage的运行时间能为游戏开发者减少CPU占用率，同时减少他们游戏的加载时间。这项技术将与NVMe 
SSD以及串流架构结合使用，效果良好。
</p>
<p style="text-indent:2em;">
减少CPU的开销。这是我非常想强调的一个关键好处，你会听到我在这次演讲中多次提到它。为一个游戏释放的CPU周期越多，它们就越可以在该游戏的其他地方得到利用，改进后台处理工作。例如，人工智能工作负载或任何东西。
</p>
<p style="text-indent:2em;">
让我们来谈谈我刚提到的减少CPU占用问题。DirectStorage是为现代游戏系统设计的。它可以非常有效地处理较小的读取，你可以将这些数据批量处理，从而完成更多的工作。 
当DirectStorage与你的游戏完全整合时，Windows 11上带有NVMe 
SSD的DirectStorage可以减少20%到40%的游戏CPU开销，这归功于Windows 11上的文件IO栈以及该平台上的总体改进。”
</p>
<p align="center">
<img src="https://img.3dmgame.com/uploads/images/news/20220329/1648511199_216395.jpg" alt="微软：直通存储API可节省CPU 20%-40%的开销" referrerpolicy="no-referrer">
</p>
<p style="text-indent:2em;">
DirectStorage也支持Windows 10（19H1+），但在较旧的操作系统上，它是一个后备实现，使用了一个建立在Win32 
API之上的优化文件IO层。虽然它将利用异步IO和完成端口等模式来最大限度地提高Windows 10的吞吐量，但性能不会像Windows 11上那么好。
</p>          
</div>
            