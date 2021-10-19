
---
title: '刚盈利的DeepMind收购MuJoCo：转手开源，所有人免费用'
categories: 
 - 新媒体
 - cnBeta
 - 最新
headimg: 'https://static.cnbetacdn.com/article/2021/1019/65d5baf0c585c77.jpg'
author: cnBeta
comments: false
date: Tue, 19 Oct 2021 06:26:38 GMT
thumbnail: 'https://static.cnbetacdn.com/article/2021/1019/65d5baf0c585c77.jpg'
---

<div>   
最新消息，首次实现盈利的 DeepMind 突然官宣：<strong>收购物理模拟引擎MuJoCo。</strong>但这还没完，他们同时宣布将对 <strong>MuJoCo开源</strong>！
这波买来给大家用的霸气操作让网友们直呼喜大普奔。<br>
 <p style="text-align:center"><img src="https://static.cnbetacdn.com/article/2021/1019/65d5baf0c585c77.jpg" referrerpolicy="no-referrer"></p><p style="text-align: left;">要知道，由于在动态多点接触（如灵活手指操作）的场景里有明显优势 ，MuJoCo 可以说是机器人研究人员的首选模拟器。</p><p style="text-align: left;">像这种人类肌腱、骨骼动态模拟，于它而言都是小 case。</p><p style="text-align:center"><img src="http://dingyue.ws.126.net/2021/1019/d9994e95g00r17i04024lc000hs00a0m.gif" referrerpolicy="no-referrer"></p><p style="text-align: left;">但它一直以来都需要<strong>付费使用</strong>，而且还很贵。</p><p style="text-align: left;">有人就表示在自己读大学时，曾因为 MuJoCo 太贵而没有继续学习 RL。</p><p style="text-align:center"><img src="https://static.cnbetacdn.com/article/2021/1019/e0d466511f8039e.jpg" referrerpolicy="no-referrer"></p><p style="text-align: left;">因此 ，DeepMind 这次开源可以说是为机器人开发者带来福音。</p><p style="text-align: left;">支持肌腱、布料仿真</p><p style="text-align: left;">MuJoCo 是多关节接触动力学 （Multi-Joint Dynamics with Contact） 的缩写，它由华盛顿大学 Emo Todorov 教授开发 ，2015 年由 Roboti LLC 作为付费产品推出。</p><p style="text-align: left;">MuJoCo 结合了广义坐标模拟和优化后的接触动力学，这使它能够模拟完整的物理运动。</p><p style="text-align: left;">要知道，许多模拟器都是把运动稳定性放在准确性之前考虑的，比如它们可能忽略陀螺效应，但这会偏离现实情况。</p><p style="text-align: left;">相比之下 ，MuJoCo 更加严格地还原现实世界中的物理运动。</p><p style="text-align: left;">像牛顿摆的现象，它都能很好模拟。</p><p style="text-align:center"><img src="https://static.cnbetacdn.com/article/2021/1019/68a4f20abb2b523.gif" referrerpolicy="no-referrer"></p><p style="text-align: left;">失重情况下的还原也非常真实：</p><p style="text-align:center"><img src="http://dingyue.ws.126.net/2021/1019/d3367887g00r17i0404cgc000hs00a0m.gif" referrerpolicy="no-referrer"></p><p style="text-align:center"><img src="https://static.cnbetacdn.com/article/2021/1019/0839fd8aea5c3f5.gif" referrerpolicy="no-referrer"></p><p style="text-align: left;">更让人惊艳的，还有 MuJoCo 对于人体关节、肌肉复杂运动的模拟。</p><p style="text-align: left;">许多机械手的研究，都是现在 MuJoCo 中模拟和验证的。</p><p style="text-align:center"><img src="https://static.cnbetacdn.com/article/2021/1019/fbdd4013433e8a1.jpg" referrerpolicy="no-referrer"></p><p style="text-align: left;">此外 ，MuJoCo 还能灵活将仿真步骤拆开执行，或者只执行仿真流程的一部分(如不计算逆动力学)。</p><p style="text-align: left;">而且支持软体材料，如绳子、布料的稳定性仿真。</p><p style="text-align: left;">为了提高仿真性能 ，MuJoCo 做了 AVX 指令等大量优化，是极少的选择 C 语言来实现的现代物理引擎之一。</p><p style="text-align: left;">而由 C 语言编写，能够让它很容易转化为其他架构。同时，独创的 MJCF 建模格式，相比 URDF 模型具有易读性、灵活配置等优点。</p><p style="text-align: left;">传送门</p><p style="text-align: left;">不过网友们发现，目前开源的还没有源代码。</p><p style="text-align: left;">DeepMind 表示，将努力在 2022 年发布代码库。</p><p style="text-align: left;">此外 ，MuJoCo 2.1 的相关信息也已经公布。</p><p style="text-align: left;">官网地址：</p><p style="text-align: left;">https://mujoco.org/</p>   
</div>
            