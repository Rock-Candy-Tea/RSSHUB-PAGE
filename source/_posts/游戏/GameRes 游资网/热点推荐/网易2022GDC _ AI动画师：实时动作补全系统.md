
---
title: '网易2022GDC _ AI动画师：实时动作补全系统'
categories: 
 - 游戏
 - GameRes 游资网
 - 热点推荐
headimg: 'https://di.gameres.com/attachment/forum/202207/19/090159chzjajfffcnzfkjn.gif'
author: GameRes 游资网
comments: false
date: Tue, 19 Jul 2022 00:00:00 GMT
thumbnail: 'https://di.gameres.com/attachment/forum/202207/19/090159chzjajfffcnzfkjn.gif'
---

<div>   
<div align="center">
<img aid="1046633" zoomfile="https://di.gameres.com/attachment/forum/202207/19/090159chzjajfffcnzfkjn.gif" data-original="https://di.gameres.com/attachment/forum/202207/19/090159chzjajfffcnzfkjn.gif" width="600" id="aimg_1046633" inpost="1" src="https://di.gameres.com/attachment/forum/202207/19/090159chzjajfffcnzfkjn.gif" referrerpolicy="no-referrer">
</div><br>
<i><font color="#808080">本文首发网易游学APP（原网易游戏学院）</font></i><br>
<br>
GDC是在全球范围内享有最高影响力的游戏开发者会议，已举办35届，今年于3月21至25日在旧金山举行。网易互娱今年有12位大咖的9个提案入围GDC非赞助类演讲，包括1项核心演讲和8项主题峰会演讲，让我们一起围观入围的提案和大神风采！<br>
<br>
<strong><font color="#de5650">一、技术概述</font></strong><br>
<br>
为了减少动画制作流程中的工作，也为非专业人士提供动画制作的可能，我们的研究尝试实现一个简单但是有效的基于深度学习的解决方案，即可一键生成的实时动作补全系统。<br>
<br>
<i><font color="#808080">目前已经被GDC2022 ML submit接收：</font></i><br>
<i><font color="#808080">https://schedule.gdconf.com/session/machine-learning-summit-ai-animator-a-real-time-motion-completion-system/883186</font></i><br>
<br>
同时论文A Unified Framework for Real Time Motion Completion已被AAAI 2022 以oral收录，详细算法内容请查看论文。<br>
<br>
我们的设计和使用：<br>
<br>
<ul><li>基于传统动画制作流程，其交互简单且可以直接嵌入。</li><li>AI基于目标关键帧一键生成，无需设置运动轨迹和中间关键帧</li><li>可嵌入任何平台之中，实时生成动作<br>
</li></ul><br>
<strong><font color="#de5650">二、问题背景</font></strong><br>
<br>
在动画制作流程中，通常由动画师手K动画关键帧，然后再进一步就细节微调；此外，Maya，Max等提供了一些线性插值、混合等的解决方案。在这些方案中，手K动画工作比较繁琐，即使是较为简单的或是重复的动作，也需要我们动画师设计每一帧动画关键帧。每一次的动作调整都有可能需要动画师重复大量动作绘制过程，这给动画师增加了很大负担。Maya、Max等自带的插值很难处理长距离的动画生成，而且它们提供的动作曲线等调整工具则依旧需要动画师绘制每一个关键帧。<br>
<br>
对于没有动画师的项目而言，网络上下载的动画直接使用会有一些细节不符，而自己制作简单的自然的动画比较复杂。<br>
<br>
因此，动作补全一直是图形学和多媒体研究的热点。长久以来，有很多深度学习的方法致力于通过算法生成多个关键帧中间的动画。<br>
<br>
<strong><font color="#de5650">三、技术实现</font></strong><br>
<br>
<strong>（1）我们的方法能够解决不同的动作补全场景问题：</strong><br>
<br>
<div align="center">
<img aid="1046634" zoomfile="https://di.gameres.com/attachment/forum/202207/19/090200lc4coh6oa1k1o4k4.png" data-original="https://di.gameres.com/attachment/forum/202207/19/090200lc4coh6oa1k1o4k4.png" width="600" id="aimg_1046634" inpost="1" src="https://di.gameres.com/attachment/forum/202207/19/090200lc4coh6oa1k1o4k4.png" referrerpolicy="no-referrer">
</div><br>
<strong>（2） 动作补全 In-betweening结果展示</strong><br>
<br>
输入骨骼动画：蓝色部分<br>
<br>
AI算法生成结果：白色部分<br>
<br>
<strong>（3）动作上采样 In-filling</strong><br>
<br>
我们的动作上采样算法，选择了比较难的舞蹈动作来展示其效果。<br>
<br>
如下gif所示，我们随意选取了4个人类姿态，放入模型之后生成了一段128帧长的舞蹈（30fps）<br>
<br>
图中，左侧为我们生成的算法，中间为（目前通用的）线性插帧算法，右侧为四个pose展示<br>
<br>
红色为生成结果，黑色为输入pose<br>
<br>
<strong>（4）动作衔接 Blending</strong><br>
<br>
输入骨骼动画：蓝色部分<br>
<br>
AI算法生成结果：白色部分<br>
<br>
动作衔接我们同样采用了比较复杂的舞蹈动作来进行测试。<br>
<br>
<strong><font color="#de5650">四、应用介绍</font></strong><br>
<br>
我们针对动作补全部分In-betweening实现了一个Maya插件<br>
<br>
我们在maya上测试的速度表现如下：<br>
<br>
<div align="center">
<img aid="1046635" zoomfile="https://di.gameres.com/attachment/forum/202207/19/090200zk5kh1hs50n50505.png" data-original="https://di.gameres.com/attachment/forum/202207/19/090200zk5kh1hs50n50505.png" width="600" id="aimg_1046635" inpost="1" src="https://di.gameres.com/attachment/forum/202207/19/090200zk5kh1hs50n50505.png" referrerpolicy="no-referrer">
</div><br>
实际使用中，我们首先需要导入一段动画：<br>
<br>
重定向到我们的模型<br>
<br>
即可调整参数实时生成动画<br>
<br>
同时，对于同一段动画，我们可以选择生成不同的长度。<br>
<br>
  
</div>
            