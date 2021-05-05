
---
title: '游戏UX交互框架规范'
categories: 
 - 游戏
 - GameRes 游资网
 - 热点推荐
headimg: 'https://di.gameres.com/attachment/forum/202104/30/104510kmk41mng5jmqaqz4.png'
author: GameRes 游资网
comments: false
date: Fri, 30 Apr 2021 00:00:00 GMT
thumbnail: 'https://di.gameres.com/attachment/forum/202104/30/104510kmk41mng5jmqaqz4.png'
---

<div>   
<table cellspacing="0" cellpadding="0"><tbody><tr><td class="t_f" id="postmessage_2495343">
游戏研发团队从几十人到上百人，规模越大出现的细节问题就越多，有时候版本已经完成了还要花很长时间去聚焦优化体验问题。<br>
<br>
所以，在游戏项目研发初期要制定以及维护交互框架。<br>
<br>
<strong><font color="#de5650">01什么是交互框架</font></strong><br>
<br>
<strong>框架来自建筑学概念，建立一个带约束性与支撑性的结构，用于解决复用的或复杂的问题，是一种标准体系。</strong><br>
<br>
假如我改造一座新房子，首先要考虑的就是其房间结构（<font color="#ff0000">框架</font>）；<br>
<br>
比如设计几个卧室，几个客厅，分别占多大面积，在什么位置等等（<font color="#ff0000">信息架构</font>）；<br>
<br>
然后还要考虑如何设计门和窗户，怎么能够在不同房间互通（<font color="#ff0000">导航方式</font>）；<br>
<br>
接着再思考每个房间里面分别需要怎么布局，分别需要哪些家居和电器，具体在什么位置（<font color="#ff0000">页面结构</font>）；<br>
<br>
<div align="center">
<img id="aimg_976011" aid="976011" zoomfile="https://di.gameres.com/attachment/forum/202104/30/104510kmk41mng5jmqaqz4.png" data-original="https://di.gameres.com/attachment/forum/202104/30/104510kmk41mng5jmqaqz4.png" width="580" inpost="1" src="https://di.gameres.com/attachment/forum/202104/30/104510kmk41mng5jmqaqz4.png" referrerpolicy="no-referrer">
</div><br>
产品框架相当于骨骼和经脉，如此细分下去，直到考虑全每个细节，这就是一个产品完整的交互框架。<br>
<br>
<strong><font color="#de5650">02要有哪些内容？</font></strong><br>
<br>
在为一款游戏产品构建交互框架时，应该从哪些内容入手呢？<br>
<br>
<strong>1. 画布规范</strong><br>
<br>
设计小组内部统一的画布尺寸，定义情景规避基础交互显示问题。<br>
<br>
<div align="center">
<img id="aimg_976012" aid="976012" zoomfile="https://di.gameres.com/attachment/forum/202104/30/104510qsgjmjzyjms0ymms.png" data-original="https://di.gameres.com/attachment/forum/202104/30/104510qsgjmjzyjms0ymms.png" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202104/30/104510qsgjmjzyjms0ymms.png" referrerpolicy="no-referrer">
</div><strong>2. 栅格化预演</strong><br>
<br>
建立栅格化对齐语言，以渠为度量单位，严格控制每个设计原子之间的间距。<br>
<br>
<div align="center">
<img id="aimg_976013" aid="976013" zoomfile="https://di.gameres.com/attachment/forum/202104/30/104511mnzip03ipisci6wc.png" data-original="https://di.gameres.com/attachment/forum/202104/30/104511mnzip03ipisci6wc.png" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202104/30/104511mnzip03ipisci6wc.png" referrerpolicy="no-referrer">
</div><br>
<strong>3. 适配方案</strong><br>
<br>
建议在做适配方案前，充分评估竞品界面布局规律，观察他们已解决和未解决的适配问题，思考原因后与技术沟通，共同制定。<br>
<br>
<div align="center">
<img id="aimg_976014" aid="976014" zoomfile="https://di.gameres.com/attachment/forum/202104/30/104511ibry9fspbbsf7s5z.png" data-original="https://di.gameres.com/attachment/forum/202104/30/104511ibry9fspbbsf7s5z.png" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202104/30/104511ibry9fspbbsf7s5z.png" referrerpolicy="no-referrer">
</div><br>
<strong>4. 对齐规则</strong><br>
<br>
常规游戏界面是由很多文本信息构成的，规范的对齐规则是可读性的关键。<br>
<br>
<div align="center">
<img id="aimg_976015" aid="976015" zoomfile="https://di.gameres.com/attachment/forum/202104/30/104512p2jppnni3feg3vvk.png" data-original="https://di.gameres.com/attachment/forum/202104/30/104512p2jppnni3feg3vvk.png" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202104/30/104512p2jppnni3feg3vvk.png" referrerpolicy="no-referrer">
</div><br>
<strong>5. 行文规则</strong><br>
<br>
避免符号或动态文本造成的阅读体验问题。<br>
<br>
<div align="center">
<img id="aimg_976016" aid="976016" zoomfile="https://di.gameres.com/attachment/forum/202104/30/104512sgmeme66zikufzie.png" data-original="https://di.gameres.com/attachment/forum/202104/30/104512sgmeme66zikufzie.png" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202104/30/104512sgmeme66zikufzie.png" referrerpolicy="no-referrer">
</div><br>
<strong>6. 导航规范</strong><br>
<br>
针对全屏、弹窗等不同的界面结构做导航规划，涉及位置、尺寸、扩展性考量等。<br>
<br>
<div align="center">
<img id="aimg_976017" aid="976017" zoomfile="https://di.gameres.com/attachment/forum/202104/30/104512xm300egmftc3ehjg.png" data-original="https://di.gameres.com/attachment/forum/202104/30/104512xm300egmftc3ehjg.png" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202104/30/104512xm300egmftc3ehjg.png" referrerpolicy="no-referrer">
</div><br>
<strong>7. 窗口规范</strong><br>
<br>
区分和定义不同功能窗口，对其进行应用规范。<br>
<br>
<div align="center">
<img id="aimg_976018" aid="976018" zoomfile="https://di.gameres.com/attachment/forum/202104/30/104513ip92w3rj71ajgpw2.png" data-original="https://di.gameres.com/attachment/forum/202104/30/104513ip92w3rj71ajgpw2.png" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202104/30/104513ip92w3rj71ajgpw2.png" referrerpolicy="no-referrer">
</div><br>
<strong><font color="#de5650">03交互框架的核心价值</font></strong><br>
<br>
我们为什么需要在前期花费大力气来建立与持续维护一套产品交互框。<br>
<br>
<div class="quote"><blockquote><strong>核心价值</strong><br>
<br>
向上约束<br>
提设计诉求不要天马行空，过度包装<br>
<br>
向下传递<br>
面对庞大的系统功能时避免出错<br>
<br>
作为指导手册<br>
规避后期的迭代优化成本<br>
<br>
作为检查工具<br>
当体验出现问题时全局判断和处理<br>
<br>
作为创新基石<br>
基于框架模块做更多设计思考</blockquote></div><br>
基于这个价值，我们其实还有很多内容去思考和补充。<br>
<br>
比如：<br>
<br>
<strong>更沉浸的界面体验</strong><br>
<br>
游戏产品更在意世界观中的沉浸感，所以会有很大一部分创意定制的界面设计（视游戏类型）。哪些系统需要包装，哪些系统又要避免过度包装？这方面需要投入交互体验上的思考。<br>
<br>
<div align="center">
<img id="aimg_976019" aid="976019" zoomfile="https://di.gameres.com/attachment/forum/202104/30/104513m8zvu1di8nn7pdvv.png" data-original="https://di.gameres.com/attachment/forum/202104/30/104513m8zvu1di8nn7pdvv.png" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202104/30/104513m8zvu1di8nn7pdvv.png" referrerpolicy="no-referrer">
</div><br>
<strong>更深的交互层级</strong><br>
<br>
游戏界面（非休闲）存在较深的窗口与信息显示层级，这些层级之间需要有清晰的互斥、跳转、快速跳转或关闭等规范。<br>
<br>
<div align="center">
<img id="aimg_976020" aid="976020" zoomfile="https://di.gameres.com/attachment/forum/202104/30/104513btddl2rivrg5aliw.png" data-original="https://di.gameres.com/attachment/forum/202104/30/104513btddl2rivrg5aliw.png" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202104/30/104513btddl2rivrg5aliw.png" referrerpolicy="no-referrer">
</div><br>
<strong>更复杂的体验引导</strong><br>
<br>
很多体验问题非单一设计样式就能解决，同一个设计方式会有不同的表现和应用情景，如果框架阶段缺少定义，后期就会有一系列体验问题出现。<br>
<br>
例如“对话气泡”，其设计样式会用在多个交互情景中（对话、对话气泡、按钮、红点提醒），合理的分级和定义就尤为重要。<br>
<br>
<div align="center">
<img id="aimg_976021" aid="976021" zoomfile="https://di.gameres.com/attachment/forum/202104/30/104514zptpxu56s6pqgytg.png" data-original="https://di.gameres.com/attachment/forum/202104/30/104514zptpxu56s6pqgytg.png" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202104/30/104514zptpxu56s6pqgytg.png" referrerpolicy="no-referrer">
</div><br>
<strong>更丰富的反馈行为</strong><br>
<br>
游戏中，反馈界面的效果需要按情景划分。<br>
<br>
当玩家获得普通物品，还是获得一个超级极品，表现是有区别的。<br>
<br>
以上，是这段时间我对游戏交互框架知识的结构化梳理，希望对你的工作有所帮助。<br>
<br>
篇幅关系不做更多展开了，后续可以加入我们的交流群一起聊聊。<br>
<br>
<font size="2"><font color="#708090">作者：杨曦UEDC</font></font><br>
<font size="2"><font color="#708090">来源：GameUE</font></font><br>
<font size="2"><font color="#708090">地址：https://mp.weixin.qq.com/s/BGPfVYM7TXF9b3OUu3wKhQ</font></font><br>
<br>
</td></tr></tbody></table>



  
</div>
            