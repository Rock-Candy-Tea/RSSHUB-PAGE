
---
title: 'Facebook宣布开源Droidlet机器人开发平台'
categories: 
 - 新媒体
 - cnBeta
 - 最新
headimg: 'https://static.cnbetacdn.com/article/2021/0805/9286ea5fbea0735.jpg'
author: cnBeta
comments: false
date: Thu, 05 Aug 2021 03:48:51 GMT
thumbnail: 'https://static.cnbetacdn.com/article/2021/0805/9286ea5fbea0735.jpg'
---

<div>   
<strong>Facebook 于今日宣布开源旗下 Droidlet 机器人开发平台，特点是能够利用自然语言处理（NLP）和计算机视觉（CV）技术来感知周围世界。</strong>其宣称能够简化机器学习算法在机器人项目中的集成，并促进快速的软件原型设计。尽管当前机器人已能够通过编程来执行舞蹈等特定应用，但还是缺乏可在更深层次上处理信息的能力。<br>
<p><img src="https://static.cnbetacdn.com/article/2021/0805/9286ea5fbea0735.jpg" alt="1.jpg" referrerpolicy="no-referrer"></p><p style="text-align: center;">Droidlet 项目 - GitHub <a href="https://github.com/facebookresearch/droidlet" target="_self">传送门</a></p><p>当然，Droidlet 并不是所有问题的万能解决方案，而是一种测试不同 NLP 和 CV 处理模型的方法。</p><p>其允许开发者构建能够在现实世界中、或《我的世界》和 Facebook 的 Habitat 等模拟环境里完成相关任务的系统。开发者可按需更换组件，来支持可在不同机器人上使用的相同系统。</p><p>此外 Droidlet 平台提供了一个仪表板，方便开发者添加调试与可视化小部件和相关工具，以及一个用于纠错和注释的界面。</p><p>除了用于测试针对机器人设置进行微调的视觉模型的环境之外，Droidlet 还附带了用于将机器学习模型连接到机器人的封包器。</p><p><img src="https://static.cnbetacdn.com/article/2021/0805/c54d038738dfd18.jpg" alt="3.jpg" referrerpolicy="no-referrer"></p><p>Droidlet 有一系列组件构成，其中某些为启发式的、另一些则是学习向的，开发者可在方便时调用静态数据、然后适当调用动态数据开展训练。其设计由以下几个模块到模块的接口组成：</p><blockquote><p>● 一个存储系统，用于跨各种模块的信息存储。</p><p>● 一组能够处理来自外界信息、并将之存储与内存中的感知模块。</p><p>● 可让机器人适应环境变化的一组较低级别的任务支持，比如‘向前移动三英尺’和‘将物品放在给定坐标处’。</p><p>● 一个控制器，可决定执行哪些基于存储系统状态的任务。</p></blockquote><p><img src="https://static.cnbetacdn.com/article/2021/0805/016d37a87008631.gif" alt="2.gif" referrerpolicy="no-referrer"></p><p>Facebook 指出，这些模块中的每一个，都可进一步分解为可训练或启发式的组件，且相关模块与仪表板支持在 Droidlet 之外的生态系统中使用。</p><p>对于研究人员和爱好者，Droidlet 还提供了对“内置电池”系统的支持，可通过预训练的物体检测和姿态预估模型来感知环境，并将观察结果存储在机器人的内存中。</p><p>通过这种表示，系统可响应诸如“前往红椅子处”之类的语音命令，利用预训练的神经语义解析器，将自然语言转换为可由机器人执行的程序。</p>   
</div>
            