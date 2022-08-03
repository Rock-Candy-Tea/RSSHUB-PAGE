
---
title: '_视频_乐高不会拼了？这款AI能帮你根据手册拼搭出成品'
categories: 
 - 新媒体
 - cnBeta
 - 最新
headimg: 'https://static.cnbetacdn.com/article/2022/0803/c51636f313203e2.webp'
author: cnBeta
comments: false
date: Wed, 03 Aug 2022 02:42:49 GMT
thumbnail: 'https://static.cnbetacdn.com/article/2022/0803/c51636f313203e2.webp'
---

<div>   
被乐高套装难住了？最新开发的机器学习框架能够引导你拼接完成。<strong>来自斯坦福大学、麻省理工大学加速季科学和人工智能实验室、Autodeck AI 实验室的科研团队联合开发了一种基于机器学习的框架，能够根据 2D 拼搭指导手册来展示 3D 效果。</strong><br>
 <p style="text-align:center"><img src="https://static.cnbetacdn.com/article/2022/0803/c51636f313203e2.webp" referrerpolicy="no-referrer"></p><p style="text-align: left;">该框架叫做 Manual-to-Executable-Plan Network（简称 MEPNet），目前已经在多款计算机生成的乐高套装、真实的乐高套装指南和 Minecraft 风格的立体建筑上成功测试，科研人员表示其性能已经超过现有其他版本。</p><p style="text-align: left;">对于人工智能来说，理解 2D 指导手册并不容易。研究人员表示，视觉指令有几个关键问题，就像乐高套装一样，完全由图像组成：识别 2D 和 3D 对象之间的对应关系，以及处理许多基本部件都非常困难。</p><p style="text-align: left;"><iframe src="//player.bilibili.com/player.html?bvid=BV1jd4y1T7Fc&page=1" width="750" height="480" frameborder="0"></iframe></p><p style="text-align: left;">研究人员表示在，任何复杂的乐高套装都是建立在基础的乐高砖块上。研究人员表示这增加了机器对乐高手册的理解难度，它需要推断由可见图元组成的不可见物体的 3D 姿势。</p><p style="text-align: left;">研究人员表示，现有的将手动步骤解析为机器可执行计划的方法主要包括两种形式：基于搜索的方法，简单准确但计算成本高；以及基于学习的模型，这些模型速度很快，但不太擅长处理看不见的 3D 形状。</p><p style="text-align: left;">研究人员说，MEPNet 结合了两者。研究人员写道，从组件的 3D 模型、乐高集的当前状态和 2D 手动图像开始，MEPNet “预测每个组件的一组 2D 关键点和掩码”。</p><p style="text-align: left;">完成后，2D 关键点“通过找到基本形状和新组件之间的可能连接，反向投影到 3D”。该团队写道，这种组合“保持了基于学习的模型的效率，并更好地推广到看不见的 3D 组件”。在论文中，研究人员表示，他们的目标是创造帮助人们组装复杂物体的机器，他们的应用列表中包括家具、乐高积木和像素世界。</p><p style="text-align:center"><img src="https://static.cnbetacdn.com/article/2022/0803/2c8c35b6823d32f.webp" referrerpolicy="no-referrer"></p><p style="text-align:center"><img src="https://static.cnbetacdn.com/article/2022/0803/8e1ca1e16cb5816.webp" referrerpolicy="no-referrer"></p><p style="text-align: center;"><img src="https://static.cnbetacdn.com/article/2022/0803/8632dcbbf7889a5.webp" referrerpolicy="no-referrer"></p>   
</div>
            