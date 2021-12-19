
---
title: 'Evolution Gym：一套能让机器人进化的设计系统'
categories: 
 - 新媒体
 - cnBeta
 - 最新
headimg: 'https://static.cnbetacdn.com/article/2021/12/9a8877a26c09921.webp'
author: cnBeta
comments: false
date: Sun, 19 Dec 2021 05:02:18 GMT
thumbnail: 'https://static.cnbetacdn.com/article/2021/12/9a8877a26c09921.webp'
---

<div>   
想象一下，你正在跑一场比赛。为了完成它，你的身体需要强壮，你的大脑需要跟踪路线以控制你的步伐并防止你绊倒。机器人的情况也是如此。为了完成任务，它们既需要一个精心设计的身体也需要一个“大脑”或控制器。<br>
 <p style="text-align:center"><a href="https://static.cnbetacdn.com/article/2021/12/9a8877a26c09921.webp" target="_blank"><img src="https://static.cnbetacdn.com/article/2021/12/9a8877a26c09921.webp" referrerpolicy="no-referrer"></a></p><p style="text-align: left;">工程师们可以使用各种模拟来改善机器人的控制，从而使其更加智能。但很少有办法能够同时优化机器人的设计。</p><p style="text-align: left;">除非设计者是一个算法。</p><p style="text-align: left;">得益于计算技术的进步，现在终于有可能编写同时优化设计和控制的软件，这种方法被称为协同设计。虽然有既定的平台来优化控制或设计，但大多数协同设计研究人员不得不设计自己的测试平台，而这些平台通常是非常密集的计算且耗时。</p><p style="text-align: left;">为了帮助解决这个问题，麻省理工学院的一名本科生研究员Jagdeep Bhatia和其他研究人员创建了一个名为Evolution Gym的2D协同设计软体机器人模拟系统。他们在今年的神经信息处理系统会议上展示了该系统。现在，他们还在一篇新论文中详细介绍了该系统。</p><p style="text-align: left;">“基本上，我们试图做一个非常简单和快速的模拟器，”该论文的第一作者Bhatia说说道，“在此基础上，我们为这些机器人建立了一系列的任务。”</p><p style="text-align: left;">在Evolution Gym中，2D软体机器人是由彩色单元或体素组成。不同的颜色代表不同类型的简单组件--要么是软性材料，要么是刚性材料，要么是水平或垂直的执行器。其结果是机器人由彩色方块拼凑而成，在视频游戏般的环境中移动。因为它是2D的、程序设计简单，所以不需要太多的计算能力。</p><p style="text-align: left;">顾名思义，研究人员将该系统结构化以模仿生物的进化过程。它不是生成单个机器人，而是生成具有轻微不同设计的机器人种群。该系统有一个双级优化系统--一个外循环和一个内循环。外循环是设计优化。该系统为一个给定的任务生成若干不同的设计，如行走、跳跃、攀爬或抓取东西；内环则用于控制优化。</p><p style="text-align: left;">Bhatia指出，系统将采取这些设计中的每一个，它将在Evolution Gym中为它优化特定任务的控制器，然后，它将会为每一个设计返回一个分数以回到设计优化算法并说“这是机器人使用最佳控制器的表现”。</p><p style="text-align: left;">通过这种方式，该系统根据特定任务的“奖励”分数生成多代机器人并保留维持和增加这种奖励的元素。研究人员开发出了30多个任务供机器人尝试执行，它们有简单、中等或困难分级。</p><p style="text-align: left;">“如果你的任务是行走，在这种情况下，你希望机器人在规定的时间内尽可能快地移动，”MIT电气工程和计算机科学教授、该论文的第一作者Wojciech Matusik说道。</p><p style="text-align: left;">研究人员发现，该系统对许多任务都非常有效且算法设计的机器人比人类设计的机器人效果更好。该系统想出了人类永远无法做到的设计，其能产生复杂的材料和非常有效的执行器。尽管该系统之前对动物或生物学没有任何了解，但它还独立地想出了一些类似动物的设计。</p><p style="text-align: left;">另一方面，没有一个机器人设计能够有效地完成最困难的任务，如举起和抓起物品。来自亚利桑那大学的工程系副教授、没有参加这项研究的Wolfgang Fink指出，这可能有很多原因，包括程序选择的进化群体不够多样化。</p><p style="text-align: left;">另外，Evolution Gym的简单化、2D设计还不适合改编成现实生活中的机器人。尽管如此，Bhatia希望Evolution Gym能成为研究人员的资源并能使他们开发新的和令人兴奋的共同设计算法。目前，该程序是开源的，人们可以免费使用。</p>   
</div>
            