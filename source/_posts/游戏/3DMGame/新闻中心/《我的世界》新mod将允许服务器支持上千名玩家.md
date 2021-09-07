
---
title: '《我的世界》新mod将允许服务器支持上千名玩家'
categories: 
 - 游戏
 - 3DMGame
 - 新闻中心
headimg: 'https://img.3dmgame.com/uploads/images/news/20210907/1630985416_902497.png'
author: 3DMGame
comments: false
date: Tue, 07 Sep 2021 03:34:00 GMT
thumbnail: 'https://img.3dmgame.com/uploads/images/news/20210907/1630985416_902497.png'
---

<div>   
<p style="text-indent:2em;">
《<a target="_blank" href="https://www.3dmgame.com/games/minecraft/">我的世界</a>》目前情况下，仅在单个CPU上单线程处理有关服务器的所有信息。这意味着不论你有多强的电脑，一旦游戏中有数十甚至数百名玩家时，游戏的运行效率性能就一定会大打折扣，服务器的刷新率会降低到无法正常游玩的程度。目前，《我的世界》同一世界的最多玩家世界纪录数为 2622 名玩家，但是在这种情况下这些玩家什么事情都做不了。
</p>
<p align="center">
<img src="https://img.3dmgame.com/uploads/images/news/20210907/1630985416_902497.png" alt="《我的世界》新mod将允许服务器支持上千名玩家" referrerpolicy="no-referrer"> 
</p>
<p style="text-indent:2em;">
但是不用担心，一个由程序员 Jackson Roberts 开发的 mod 可能会改变这一切！
</p>
<p style="text-indent:2em;">
在 2020 年时他想要一个隔离期间能做的项目，因此决定创建一个超大的《我的世界》服务器，并且可以没有延迟地容纳数千名玩家。《我的世界》目前的单线程服务器软件显然无法胜任这项工作，因此 Roberts 和合作者 Harvey298 决定它们将研究如何构建自己的服务器软件，并将该项目称为 Mammoth（猛犸象）。
</p>
<p align="center">
<img src="https://img.3dmgame.com/uploads/images/news/20210907/1630985427_635412.jpg" alt="《我的世界》新mod将允许服务器支持上千名玩家" referrerpolicy="no-referrer"> 
</p>
<p style="text-indent:2em;">
Roberts 解释说，第一次尝试是一个概念证明系统，它将《我的世界》中的世界分成 1024 个块，每个块都由自己的服务器运行：边界区域将会被同步，服务器在彼此之间传输移动对象。但是，它有太多问题：玩家无法“跨”服务器看到彼此，一台服务器宕机导致该部分世界无法访问，而且如果许多玩家聚集在一个小区域内，该方案根本无法解决任何问题。
</p>
<p style="text-indent:2em;">
在这次经历之后，Roberts 为 Mammoth 设定了一系列目标，包括：玩家必须能够看到彼此，即使在不同的服务器进程中；当玩家放置方块或更新标志时，所有其他玩家都应该立即看到；如果一台服务器宕机，整个世界应该仍然可以访问；如果需要，可以随意添加或删除服务器以适应玩家数量。
</p>
<p align="center">
<img src="https://img.3dmgame.com/uploads/images/news/20210907/1630985437_105529.png" alt="《我的世界》新mod将允许服务器支持上千名玩家" referrerpolicy="no-referrer"> 
</p>
<p style="text-indent:2em;">
他提出的想法是一个集中的后端数据库，当《我的世界》服务器出现和消失时，它可以在它们之间进行通信，并不断传递有关例如玩家移动等信息。在尝试了一些现有软件（例如 redis 和 SpatialOS）后，Roberts 发现它不适合他的目的，因此决定构建自己的软件 WorldQL，他将其描述为“为多人游戏构建的实时、可编写脚本的空间数据库，它可以替代传统游戏服务器或用于平衡现有游戏服务器。”
</p>
<p style="text-indent:2em;">
所以，将于 9 月 8 日发布的新版 Mammoth mod 将建立在 World QL 上，它存储“所有永久的世界变化并在服务器之间传递实时玩家信息（例如位置）”。基本上，每个服务器都在不断地向 World QL 报告其数据，然后根据这些报告向其他服务器提问：如果它知道一个玩家在另一个玩家附近，并且第一个玩家的服务器说他们已经移动了，WorldQL 会询问另一个正在做什么。
</p>
<h3>
演示视频：<br>
</h3>
<p align="center">
<iframe src="https://player.youku.com/embed/XNTE5Nzc4MjM2MA?client_id=5a73c0df8eb0d91d" allowfullscreen width="640" height="480" frameborder="0">
</iframe>
</p>
<p style="text-indent:2em;">
“在 Mammoth 中，没有一个 Minecraft 服务器负责存储世界。来自基础种子的所有块更改都集中存储在 WorldQL 中。这些更改按块坐标和时间进行索引，因此《我的世界》服务器只能请求它需要的更新。”
</p>
<p style="text-indent:2em;">
Jackson Roberts 的帖子更详细的介绍了该 mod 其它的功能，例如“实时块同步”、消息代理以及在 World QL 脚本环境中创建的 Minecraft 迷你游戏的未来潜力。更多详情可以查看 Mammoth 项目的 github 页面。
</p>
<p style="text-indent:2em;">
<strong><span style="font-size:16px;"><span style="color:#E56600;">Github页面：</span><a href="https://github.com/WorldQL/mammoth" target="_blank">点击这里</a></span></strong>
</p>          
</div>
            