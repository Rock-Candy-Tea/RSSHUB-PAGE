
---
title: 'UI控件+体验：如何从落地出发拆解微动效'
categories: 
 - 游戏
 - GameRes 游资网
 - 热点推荐
headimg: 'https://di.gameres.com/attachment/forum/202205/05/102259pv62kzevuuvd279u.gif'
author: GameRes 游资网
comments: false
date: Thu, 05 May 2022 00:00:00 GMT
thumbnail: 'https://di.gameres.com/attachment/forum/202205/05/102259pv62kzevuuvd279u.gif'
---

<div>   
<div align="center">
<img aid="1038403" zoomfile="https://di.gameres.com/attachment/forum/202205/05/102259pv62kzevuuvd279u.gif" data-original="https://di.gameres.com/attachment/forum/202205/05/102259pv62kzevuuvd279u.gif" width="600" id="aimg_1038403" inpost="1" src="https://di.gameres.com/attachment/forum/202205/05/102259pv62kzevuuvd279u.gif" referrerpolicy="no-referrer">
</div><br>
在游戏开发中，游戏策划往往更看重游戏流程的完整性，GUI设计师更加注重表现层的感受，动效设计师对于游戏中动效的设计也往往是更注重视觉上的表现，那么游戏交互设计师本就容易忽视的功能方面的“交互微动效”就更容易被忽略了。因此有时候会觉得自己团队做的游戏项目似乎哪里操作起来感觉很生硬，不够Q弹顺滑，但又说不上来哪里不对，那么我们就要考虑一下，是不是缺乏界面的过渡动效？<br>
<br>
<strong><font color="#de5650">前  言</font></strong><br>
<br>
由于是从游戏控件出发去拆解微动效，因此接下来的内容会比较干货，希望可以为大家带来一些指导意义。话不多说，下面先上一张脑暴图，接下来的内容也会围绕这几个方面去展开。<br>
<br>
<div align="center">
<img aid="1038404" zoomfile="https://di.gameres.com/attachment/forum/202205/05/102300y29vy5sls5g2lsk5.jpg" data-original="https://di.gameres.com/attachment/forum/202205/05/102300y29vy5sls5g2lsk5.jpg" width="600" id="aimg_1038404" inpost="1" src="https://di.gameres.com/attachment/forum/202205/05/102300y29vy5sls5g2lsk5.jpg" referrerpolicy="no-referrer">
</div><br>
<strong><font color="#de5650">一、微动效的分类</font></strong><br>
<br>
通常来说，在游戏中由于UI控件的位置、大小、透明度、光效、粒子等几种变化而产生的，且对提升玩家用户体验有所帮助的功能性动效，可以称之为微动效（本文讨论范围仅限于在游戏开发过程中可通用的微动效）<br>
<br>
<strong>反馈型动效</strong><br>
<br>
通常来说，玩家与UI控件进行交互后产生并表现在该控件本身的动效，且必须具备高效快速的反馈机制，比如缩放、闪烁等，可以称之为反馈型动效。这类动效适用于需要让玩家更好地了解操作结果与当前状态的UI控件。<br>
<br>
通过拆解游戏的UI控件，一般该类动效会出现在这些UI控件上，具体到控件可能出现的状态。<br>
<br>
<div align="center">
<img aid="1038405" zoomfile="https://di.gameres.com/attachment/forum/202205/05/102300p0mh5wm04jruiiks.jpg" data-original="https://di.gameres.com/attachment/forum/202205/05/102300p0mh5wm04jruiiks.jpg" width="600" id="aimg_1038405" inpost="1" src="https://di.gameres.com/attachment/forum/202205/05/102300p0mh5wm04jruiiks.jpg" referrerpolicy="no-referrer">
</div><br>
<strong>过渡型动效</strong><br>
<br>
通常来说，玩家主动与UI控件进行交互后，被交互控件所在界面的UI布局或表现发生变化且表现在控件与其他控件之间，用以补充玩家除反馈动效外的游戏体验所产生的动效，可以称之为过渡型动效。这类动效适用于需要保持过渡和切换流畅性的UI控件，该动效有但不仅限于组织UI元素在时间维度上的演进。<br>
<br>
通过拆解游戏的UI控件，一般该类动效会出现在这些UI控件上。<br>
<br>
<div align="center">
<img aid="1038406" zoomfile="https://di.gameres.com/attachment/forum/202205/05/102300syygfjgd8spzs2fm.jpg" data-original="https://di.gameres.com/attachment/forum/202205/05/102300syygfjgd8spzs2fm.jpg" width="600" id="aimg_1038406" inpost="1" src="https://di.gameres.com/attachment/forum/202205/05/102300syygfjgd8spzs2fm.jpg" referrerpolicy="no-referrer">
</div><br>
<strong>引导型动效</strong><br>
<br>
通常来说，玩家未与UI控件发生交互，由系统触发且UI控件自发展示引起玩家注意，能给玩家有效引导帮助的动效，可以称之为引导型动效。这类动效适用于隐藏起一部分功能或提醒玩家功能的UI控件。该类动效可再进行分类，从表现形式上，可分为流光型动效与闪光型动效。<br>
<br>
通过拆解游戏的UI控件，一般该类动效会出现在这些UI控件上。<br>
<br>
<div align="center">
<img aid="1038407" zoomfile="https://di.gameres.com/attachment/forum/202205/05/102300yousbpzbk2p2rrr2.jpg" data-original="https://di.gameres.com/attachment/forum/202205/05/102300yousbpzbk2p2rrr2.jpg" width="600" id="aimg_1038407" inpost="1" src="https://di.gameres.com/attachment/forum/202205/05/102300yousbpzbk2p2rrr2.jpg" referrerpolicy="no-referrer">
</div><br>
<strong><font color="#de5650">二、微动效的设计规范</font></strong><br>
<br>
纵观整个设计史，不仅一个设计师或者机构提到过动效设计原则，比如Google Material Design(2020) 提出的系统动效原则、Apple IOS （2021）提出的系统动效原则、Material Design(2017)提出的系统动效原则等等，因此在本文中提出的设计规范（原则）都是根据笔者自己的项目经验所归纳的。<br>
<br>
<strong>微动效的设计规范</strong><br>
<br>
先聊一下一般在设计交互微动效的时候需要注意哪些方面的规范细节（交互设计师在设计UI微动效的时候，可以根据自己项目的实际情况去调整以下的规范）。<br>
<br>
<ul><li>保持动效的一致性（控件出场顺序）</li><li>引导动效区分浅色界面/深色界面</li><li>不要加入过多的属性变化，以免影响动效流畅度</li><li>界面层级较深的控件动效避免过于繁复的动效设计<br>
</li></ul><br>
微动效的输出规范<br>
<br>
由于网易的游戏交互工作内容大多分为设计与输出，因此在聊到微动效的设计规范时，笔者简单整理了一下微动效的输出规范，方便大家参考落实。<br>
<br>
<ul><li>对于每一类游戏控件的动效建立一个模板，便于输出同学直接复用。</li><li>复用动效输出时注意面板的层级，节点层级需保持一致，不容易报错。</li><li>对于某些可变性较大的动效可以预留参数（关于参数接下来会聊到）修改的接口。<br>
</li></ul><br>
<strong><font color="#de5650">三、微动效的基本单元拆解</font></strong><br>
<br>
什么是微动效的基本单元呢？其实在这方面学术上一直没有比较明确的定义，以下拆解的基本单元也是笔者自己基于看一些设计网文和书籍，以及自己平时做交互的经验总结补充而来，本文将组成动效或者能够影响动效效果的因素称之为基本单元。<br>
<br>
<strong>微动效的基础变化类型</strong><br>
<br>
根据一开始本文对微动效的定义，将属性变化视为最基础的动效变化，做了以下分类，每个分类都以游戏控件为最小单位。<br>
<br>
<ul><li>Movement 移动<br>
</li></ul><br>
<div align="center">
<img aid="1038408" zoomfile="https://di.gameres.com/attachment/forum/202205/05/102301ennn2xo2vu8jeeun.gif" data-original="https://di.gameres.com/attachment/forum/202205/05/102301ennn2xo2vu8jeeun.gif" width="188" id="aimg_1038408" inpost="1" src="https://di.gameres.com/attachment/forum/202205/05/102301ennn2xo2vu8jeeun.gif" referrerpolicy="no-referrer">
</div><div align="center"><font size="2"><font color="#808080">游戏中游戏控件的微动效举例</font></font></div><br>
<ul><li>Scaling 缩放<br>
</li></ul><br>
<div align="center">
<img aid="1038410" zoomfile="https://di.gameres.com/attachment/forum/202205/05/102301l2hm1o4r05erm2ee.gif" data-original="https://di.gameres.com/attachment/forum/202205/05/102301l2hm1o4r05erm2ee.gif" width="224" id="aimg_1038410" inpost="1" src="https://di.gameres.com/attachment/forum/202205/05/102301l2hm1o4r05erm2ee.gif" referrerpolicy="no-referrer">
</div><br>
<div align="center"><font size="2"><font color="#808080">
<img aid="1038411" zoomfile="https://di.gameres.com/attachment/forum/202205/05/102301sf3thnntwmwwaoon.gif" data-original="https://di.gameres.com/attachment/forum/202205/05/102301sf3thnntwmwwaoon.gif" width="600" id="aimg_1038411" inpost="1" src="https://di.gameres.com/attachment/forum/202205/05/102301sf3thnntwmwwaoon.gif" referrerpolicy="no-referrer">
</font></font></div><div align="center"><font size="2"><font color="#808080">游戏中游戏控件的微动效举例</font></font></div><br>
<ul><li>Rotation 旋转<br>
</li></ul><br>
<div align="center">
<img aid="1038412" zoomfile="https://di.gameres.com/attachment/forum/202205/05/102302czq4f8lc8ml8qmsi.gif" data-original="https://di.gameres.com/attachment/forum/202205/05/102302czq4f8lc8ml8qmsi.gif" width="284" id="aimg_1038412" inpost="1" src="https://di.gameres.com/attachment/forum/202205/05/102302czq4f8lc8ml8qmsi.gif" referrerpolicy="no-referrer">
</div><br>
<div align="center"><font size="2"><font color="#808080">
<img aid="1038413" zoomfile="https://di.gameres.com/attachment/forum/202205/05/102302qp6blohxkobbrwlp.gif" data-original="https://di.gameres.com/attachment/forum/202205/05/102302qp6blohxkobbrwlp.gif" width="600" id="aimg_1038413" inpost="1" src="https://di.gameres.com/attachment/forum/202205/05/102302qp6blohxkobbrwlp.gif" referrerpolicy="no-referrer">
</font></font></div><div align="center"><font size="2"><font color="#808080">游戏中游戏控件的微动效举例</font></font></div><br>
<ul><li>Alpha 透明度<br>
</li></ul><br>
<div align="center">
<img aid="1038414" zoomfile="https://di.gameres.com/attachment/forum/202205/05/102303p6wbg4agrvra3h64.gif" data-original="https://di.gameres.com/attachment/forum/202205/05/102303p6wbg4agrvra3h64.gif" width="264" id="aimg_1038414" inpost="1" src="https://di.gameres.com/attachment/forum/202205/05/102303p6wbg4agrvra3h64.gif" referrerpolicy="no-referrer">
</div><br>
<div align="center"><font size="2"><font color="#808080">
<img aid="1038415" zoomfile="https://di.gameres.com/attachment/forum/202205/05/102306ib8jgjqq38hfjqgj.gif" data-original="https://di.gameres.com/attachment/forum/202205/05/102306ib8jgjqq38hfjqgj.gif" width="600" id="aimg_1038415" inpost="1" src="https://di.gameres.com/attachment/forum/202205/05/102306ib8jgjqq38hfjqgj.gif" referrerpolicy="no-referrer">
</font></font></div><div align="center"><font size="2"><font color="#808080">游戏中游戏控件的微动效举例</font></font></div><br>
<ul><li>Color 颜色<br>
</li></ul><br>
<div align="center">
<img aid="1038416" zoomfile="https://di.gameres.com/attachment/forum/202205/05/102310e6e7iojgmw0iimmi.gif" data-original="https://di.gameres.com/attachment/forum/202205/05/102310e6e7iojgmw0iimmi.gif" width="320" id="aimg_1038416" inpost="1" src="https://di.gameres.com/attachment/forum/202205/05/102310e6e7iojgmw0iimmi.gif" referrerpolicy="no-referrer">
</div><br>
<div align="center"><font size="2"><font color="#808080">
<img aid="1038417" zoomfile="https://di.gameres.com/attachment/forum/202205/05/102310fp8hhuwmkkrpw2rh.gif" data-original="https://di.gameres.com/attachment/forum/202205/05/102310fp8hhuwmkkrpw2rh.gif" width="600" id="aimg_1038417" inpost="1" src="https://di.gameres.com/attachment/forum/202205/05/102310fp8hhuwmkkrpw2rh.gif" referrerpolicy="no-referrer">
</font></font></div><div align="center"><font size="2"><font color="#808080">游戏中游戏控件的微动效举例</font></font></div><br>
<ul><li>Lighting Effect 光效<br>
</li></ul><br>
<div align="center"><font size="2"><font color="#808080">
<img aid="1038418" zoomfile="https://di.gameres.com/attachment/forum/202205/05/102311zk4skskzry74heks.gif" data-original="https://di.gameres.com/attachment/forum/202205/05/102311zk4skskzry74heks.gif" width="600" id="aimg_1038418" inpost="1" src="https://di.gameres.com/attachment/forum/202205/05/102311zk4skskzry74heks.gif" referrerpolicy="no-referrer">
</font></font></div><div align="center"><font size="2"><font color="#808080">游戏中游戏控件的微动效举例</font></font></div><br>
<strong>微动效的可调整参数</strong><br>
<br>
在制作通用微动效的模板时，可以预留一些参数接口，以便后续复用的时候便捷调整，可以快速预览或获得设计师想要的效果。以下是本文根据上述基础变化举例的一些可调整参数，具体情况请以项目组实际情况为准。<br>
<br>
<ul><li>微动效的响应时间</li><li>微动效光效变化的参数，比如光效的大小，光效持续时间、光效的颜色等等</li><li>微动效透明度的初始值与最终值</li><li>微动效缩放元素大小的初始值与最终值</li><li>微动效旋转元素的角度初始值与最终值<br>
</li></ul><br>
微动效的可调整参数数值变化一方面会受到微动效本身的复杂程度影响，一方面也会收到微动效的目标影响。以微动效的响应时间举例，响应时间指从用户执行操作到反馈出现的间隔时间。触发机制不同，响应时间的限制也不同。在微动效出入场的情况下，出场动效一般比入场动效更快，这是因为元素入场时用户一般需要阅读并处理新出现的信息，而元素出场时通常表明用户在此元素上的任务已完成，不需要再关注了，快速出场能够节省用户更多时间。再比如微动效的光效变化参数，在普通游戏场景中，由于界面本身的信息丰富，只需要给用户提高关注，但无需分散用户过多注意力，因此点击的光效强度会弱一些，具体参数表现为各项数值都会小一些；在新手引导场景中，由于此时希望用户强关注，提升学习力， 需要用户集中注意力，因此点击的光效强度也会强一些，具体参数表现为各项数值都会大一些。<br>
<br>
综上所述，微动效的参数调整是交互设计师在拆解微动效进行设计制作的时候必不可少的一环，如果在输出过程中交互设计师可以很好运用这些参数接口进行调整，对于平时的微动效制作效率将是大大提升的。<br>
<br>
<strong>微动效常用的速度变化模式</strong><br>
<br>
除上述基本因素之外，微动效还有一个可以拆解的基本单元即速度（时间—变化量），但由于速度的变化情况太多，以下仅从归纳总结的几种速度变化模式进行讨论。<br>
<br>
<strong>线性变化</strong><br>
<br>
线性变化具有匀速、骤停这两个特征。<br>
<br>
（1）匀速变化<br>
<br>
<div align="center">
<img aid="1038419" zoomfile="https://di.gameres.com/attachment/forum/202205/05/102322xedrrrmro4o8zokb.gif" data-original="https://di.gameres.com/attachment/forum/202205/05/102322xedrrrmro4o8zokb.gif" width="600" id="aimg_1038419" inpost="1" src="https://di.gameres.com/attachment/forum/202205/05/102322xedrrrmro4o8zokb.gif" referrerpolicy="no-referrer">
</div><br>
一般适用于与物理属性无关的过渡动效（如透明度属性的变化，包含渐隐渐现或颜色间的切换），或有规律的加载动效（如均匀的循环、数值变化或进度变化）。在与物理参数有关的变化中（如位置变化），尽量避免使用线性变化，否则很容易给人带来动效僵硬、不自然的感觉。<br>
<br>
<strong>曲线变化</strong><br>
<br>
曲线包含多种类型，在交互微动效设计中，缓动曲线的应用范围最广、效果最自然、对用户的干扰也较小，多用于与物理属性相关的属性变化中，简单展示两种比较典型的。<br>
<br>
（1）缓动 慢—快—慢<br>
<br>
<div align="center">
<img aid="1038420" zoomfile="https://di.gameres.com/attachment/forum/202205/05/102323gth4c0fociht0h05.gif" data-original="https://di.gameres.com/attachment/forum/202205/05/102323gth4c0fociht0h05.gif" width="600" id="aimg_1038420" inpost="1" src="https://di.gameres.com/attachment/forum/202205/05/102323gth4c0fociht0h05.gif" referrerpolicy="no-referrer">
</div><br>
一般适用于与物理属性相关的过渡动效（比如元素位置、大小等），比如获得奖励的动效，由慢到快，可以给用户一种惊喜感。<br>
<br>
（2）弹簧 正变化—负变化—正变化<br>
<br>
<div align="center">
<img aid="1038421" zoomfile="https://di.gameres.com/attachment/forum/202205/05/102323wnatzx7afxwaaok7.gif" data-original="https://di.gameres.com/attachment/forum/202205/05/102323wnatzx7afxwaaok7.gif" width="600" id="aimg_1038421" inpost="1" src="https://di.gameres.com/attachment/forum/202205/05/102323wnatzx7afxwaaok7.gif" referrerpolicy="no-referrer">
</div><br>
<strong>微动效的常用变化模式</strong><br>
<br>
该章节讨论的常用变化模式主要由上述3小节的元素组成的微动效展示的常用模式。如果说第二章的分类是从功能上区分动效类型，那该章节就是从动效展示方式的角度出发对动效的拆解。<br>
<br>
<ul><li>Container transform 容器转换<br>
</li></ul><br>
容器转换是指背景容器从一个UI元素形式被设计为另一个UI元素形式之间的过渡，此微动效变化模式在两个UI元素之间创建可见连接。通过将一个元素无缝转换为另一个元素，可以增强两个元素之间的关系。例如，当原神的按钮点击后转换为详细信息页面时，将玩家的焦点定向到该信息的扩展版本。<br>
<br>
<div align="center">
<img aid="1038422" zoomfile="https://di.gameres.com/attachment/forum/202205/05/102324h783tm7i3rikimaa.gif" data-original="https://di.gameres.com/attachment/forum/202205/05/102324h783tm7i3rikimaa.gif" width="600" id="aimg_1038422" inpost="1" src="https://di.gameres.com/attachment/forum/202205/05/102324h783tm7i3rikimaa.gif" referrerpolicy="no-referrer">
</div><br>
<ul><li>Shared axis 共享轴<br>
</li></ul><br>
共享轴线模式用于具有空间或导航关系UI元素之间的过渡。此模式使用共同的转变在x，y或z轴上增强元素之间的关系。在游戏微动效中比较典型的代表是游戏tab的切换，一般都是x,y轴上的变化。<br>
<br>
<div align="center">
<img aid="1038423" zoomfile="https://di.gameres.com/attachment/forum/202205/05/102324ixhrs5xc8vs778ni.gif" data-original="https://di.gameres.com/attachment/forum/202205/05/102324ixhrs5xc8vs778ni.gif" width="600" id="aimg_1038423" inpost="1" src="https://di.gameres.com/attachment/forum/202205/05/102324ixhrs5xc8vs778ni.gif" referrerpolicy="no-referrer">
</div><br>
<ul><li>Fade through 淡入淡出<br>
</li></ul><br>
淡入淡出模式是指通过褪色的方式过渡彼此不具有牢固关系UI元素，比如游戏中的弹窗，弹窗一般通过点击界面上的按钮弹出，弹窗界面与入口按钮所在界面一般属于两个交互层级，为了让玩家不会混淆这个概念，一般会采用淡入淡出的形式，且不会分散玩家太多注意力。<br>
<br>
<div align="center">
<img aid="1038424" zoomfile="https://di.gameres.com/attachment/forum/202205/05/102324nihairayfy43frbh.gif" data-original="https://di.gameres.com/attachment/forum/202205/05/102324nihairayfy43frbh.gif" width="600" id="aimg_1038424" inpost="1" src="https://di.gameres.com/attachment/forum/202205/05/102324nihairayfy43frbh.gif" referrerpolicy="no-referrer">
</div><br>
<strong><font color="#de5650">四、微动效的具体案例分析</font></strong><br>
<br>
笔者在服务《天谕》及海外版（目前日本畅销榜第一名）工作过程中，对《天谕》中的微动效进行了深入的探索和拆解。接下来以《天谕》为例，简单分析几个微动效。<br>
<br>
<div align="center">
<img aid="1038425" zoomfile="https://di.gameres.com/attachment/forum/202205/05/102326f4ju0dtad4s42ycd.jpg" data-original="https://di.gameres.com/attachment/forum/202205/05/102326f4ju0dtad4s42ycd.jpg" width="600" id="aimg_1038425" inpost="1" src="https://di.gameres.com/attachment/forum/202205/05/102326f4ju0dtad4s42ycd.jpg" referrerpolicy="no-referrer">
</div><br>
案例将从微动效的设计目标出发，评估设计的合理性，下面再上一张脑图。<br>
<br>
<div align="center"><font size="2"><font color="#808080">
<img aid="1038426" zoomfile="https://di.gameres.com/attachment/forum/202205/05/102329rlvl7t6kfkvfllv8.jpg" data-original="https://di.gameres.com/attachment/forum/202205/05/102329rlvl7t6kfkvfllv8.jpg" width="600" id="aimg_1038426" inpost="1" src="https://di.gameres.com/attachment/forum/202205/05/102329rlvl7t6kfkvfllv8.jpg" referrerpolicy="no-referrer">
</font></font></div><div align="center"><font size="2"><font color="#808080">某公司出品的微交互设计指南</font></font></div><br>
<ul><li>案例1<br>
</li></ul><br>
<div align="center">
<img aid="1038427" zoomfile="https://di.gameres.com/attachment/forum/202205/05/102330i2nhs9nlfh8b7znq.gif" data-original="https://di.gameres.com/attachment/forum/202205/05/102330i2nhs9nlfh8b7znq.gif" width="600" id="aimg_1038427" inpost="1" src="https://di.gameres.com/attachment/forum/202205/05/102330i2nhs9nlfh8b7znq.gif" referrerpolicy="no-referrer">
</div><br>
<strong>场景：</strong>《天谕》背包界面的四级导航tab<br>
<br>
<strong>目的：</strong>表明已经处于用户注意力范围内的不同元素间的层级关系<br>
<br>
<strong>制作：</strong>该微动效在制作时用到了缩放、光效这两种基础变化，通过点击来缩放tab的大小，吸引玩家的注意力，展示玩家目前所在的界面层级与界面信息。<br>
<br>
<strong>细节优化：</strong>下面的界面切换可以也增加一个微动效，让玩家感受到下面的内容也是跟着一起切换的。<br>
<br>
<strong>评估：</strong>基本符合设计目的，玩家的操作体验会变更好。<br>
<br>
<ul><li>案例2<br>
</li></ul><br>
<div align="center">
<img aid="1038428" zoomfile="https://di.gameres.com/attachment/forum/202205/05/102330qk8up6g6cphpuvcq.gif" data-original="https://di.gameres.com/attachment/forum/202205/05/102330qk8up6g6cphpuvcq.gif" width="480" id="aimg_1038428" inpost="1" src="https://di.gameres.com/attachment/forum/202205/05/102330qk8up6g6cphpuvcq.gif" referrerpolicy="no-referrer">
</div><br>
<strong>场景：</strong>《天谕》任务面板的提示<br>
<br>
<strong>目的：</strong>吸引用户注意，思考是否需要用户一下子就能注意到动效并立即采取行动<br>
<br>
<strong>制作：</strong>该微动效在制作时用到了光效、透明度这两种基础变化，通过闪烁，吸引玩家的注意力，提示目前任务流程的下一步操作，让玩家立马有下一步的目标感。<br>
<br>
<strong>细节优化：</strong>无<br>
<br>
<strong>评估：</strong>符合设计目的，玩家在任务流程中具有目标感。<br>
<br>
<strong><font color="#de5650">五、微动效的落地评判方案</font></strong><br>
<br>
那么如何判定一个微动效规范在实际项目中的可行性，是否真的有必要推行该规范呢？本文简单整理了一些规范评价方案，如下：<br>
<br>
<ul><li>考试：新人培训时，可以作为考察的标准</li><li>动效设计评审时加入规范匹配度，有专门对规范符合度打分</li><li>统计规范应用个数，并且给每个规范界定人天价值，预估降低的成本</li><li>量化带动效的UI控件个数统计：量化使用相关控件后的面板数量及整体感受的提升</li><li>可用性测试评分：对比规范上线前后分数<br>
</li></ul><br>
<strong><font color="#de5650">总  结</font></strong><br>
<br>
本文拆解了微动效的基本单元，从某种意义上还是延续自我们对于物理世界的认知，摩擦力和加速度在虚拟界面中以另外的方式续存着。模仿现实世界的界面让我们对于界面的秩序有更清晰的认知，允许我们更轻松的了解和访问界面的内容。当然，即使是遵循这么多规范，动效的设计依然是一门艺术，而非单纯的科学，多做测试多摸索总是有必要的。最后希望上述的规范与拆解可以帮助同学们在实际项目中如何高效且正确地运用微动效带来帮助。<br>
<br>
<font size="2"><font color="#808080">来源：雷火UX体验设计</font></font><br>
<br>
  
</div>
            