
---
title: '加亿点点灵魂？Live2d的灵动配方！'
categories: 
 - 游戏
 - GameRes 游资网
 - 热点推荐
headimg: 'https://di.gameres.com/attachment/forum/202109/09/095914om80k0jmse79v00v.png'
author: GameRes 游资网
comments: false
date: Thu, 09 Sep 2021 00:00:00 GMT
thumbnail: 'https://di.gameres.com/attachment/forum/202109/09/095914om80k0jmse79v00v.png'
---

<div>   
<table cellspacing="0" cellpadding="0"><tbody><tr><td class="t_f" id="postmessage_2513788">
<div class="quote"><blockquote><font color="#000000">大家好！</font><br>
<font color="#000000"><br>
</font><font color="#000000">这里是隆少（不是龙少哦~）</font><br>
<font color="#000000"><br>
</font><font color="#000000">因为希望自己绘制的人物能够朝自己开心挥挥手而奔向Live2d的动画设计师，</font><br>
<font color="#000000"><br>
</font><font color="#000000">那么今天我们就来看看令角色活过来的魔法配方吧！</font></blockquote></div><br>
<strong><font color="#de5650"><br>
</font></strong><br>
<strong><font color="#de5650">原画分析以及细节绑定思路</font></strong><br>
<br>
首先，Live2d是以原画为基础制作的2D骨骼模型，所以原画角色的外形和设定对之后的动画和制作方向有着至关重要的作用，所以在开始制作之前就需要对角色性格和衣着表现来有方向性地进行评估。<br>
<br>
举个例子：<br>
<br>
<div align="center"><font size="2">
<img id="aimg_1007230" aid="1007230" zoomfile="https://di.gameres.com/attachment/forum/202109/09/095914om80k0jmse79v00v.png" data-original="https://di.gameres.com/attachment/forum/202109/09/095914om80k0jmse79v00v.png" width="388" inpost="1" src="https://di.gameres.com/attachment/forum/202109/09/095914om80k0jmse79v00v.png" referrerpolicy="no-referrer">
</font></div><div align="center"><font size="2">图片来自游戏少女前线-小狮子</font></div><br>
首先，从上图我们看到人物为和风衣着手持团扇，有着一头蓬松金发的少女，衣着细节有蝴蝶型意面和披萨造型，可以考虑角色可能有吃货的属性。<br>
<br>
角色处于偏身朝向玩家的状态，表情腼腆且开心，搭配衣着可以考虑场景是夏日祭典中与有好感的人一起出游的状态。<br>
<br>
需善于联想，亦可观察角色的配饰或手持物以考虑细节方面的绑定思路。<br>
<br>
再来一个栗子~<br>
<br>
<div align="center"><font size="2">
<img id="aimg_1007232" aid="1007232" zoomfile="https://di.gameres.com/attachment/forum/202109/09/095917lgkgkmmmgnwnxkgc.png" data-original="https://di.gameres.com/attachment/forum/202109/09/095917lgkgkmmmgnwnxkgc.png" width="513" inpost="1" src="https://di.gameres.com/attachment/forum/202109/09/095917lgkgkmmmgnwnxkgc.png" referrerpolicy="no-referrer">
</font></div><div align="center"><font size="2">图片来自游戏少女前线-圣诞约定</font></div><br>
上图可见包含铃铛、花环以及写有圣诞快乐字样的帽子，红色的衣着打扮也充满圣诞节氛围。<br>
<br>
可以看出这是节日特征的立绘类型，制作时可以考虑表现在枪炮上的彩灯效果，以及在圣诞冬日时寒冷的气温下让角色在说话时呼出热气的表现都会与立绘的氛围颇为贴合。<br>
<br>
<strong><font color="#de5650">拆分原画路</font></strong><br>
<br>
原画在拆分前也需要考虑到角色之后在动画中的动态再进行，下面有请我们可爱的小黄人来举栗子：<br>
<br>
<div align="center">
<img id="aimg_1007233" aid="1007233" zoomfile="https://di.gameres.com/attachment/forum/202109/09/095918xnzlzrrfy3j2trfh.png" data-original="https://di.gameres.com/attachment/forum/202109/09/095918xnzlzrrfy3j2trfh.png" width="215" inpost="1" src="https://di.gameres.com/attachment/forum/202109/09/095918xnzlzrrfy3j2trfh.png" referrerpolicy="no-referrer">
</div><br>
图上的小黄人是张开手做出挥手状，那么便需要考虑在最终动画中小黄人是要单纯的挥挥手，还是会有握拳、V字手之类的额外手势动态。<br>
<br>
如果存在后者，需要在拆图的流程中就提前将小黄人的手指拆分出来以备在模型中绑定使用，以避免到了绑定阶段才突然发现手指难以进行动作而又折回现拆图的麻烦。<br>
<br>
所以考虑小黄人的帽子尖是否甩动、背带裤的肩带是否掉下来（bushi）也是同理~<br>
<br>
唯一比较不同的的大概就是小黄人只需要绑定三根手指就可以了（超省事儿，就很棒/w\）。<br>
<br>
<strong><font color="#de5650">拆分原画路</font></strong><br>
<br>
在模型绑定中除了正常所需要绑定包括头部XY，头发以及五官参数以外，依照角色的个性区别额外绑定或删减其专属的参数绑定。<br>
<br>
以下图的犬夜叉为例，他没有人类耳朵的绑定，转而需要增加兽耳的绑定参数，需要设置好所需的参数ID以及参数范围并调整合适的动态进行绑定，同头发一样需要注意兽耳的生长方向和运动方式（毕竟人耳可不太擅长自己摆动哒233）。<br>
<br>
<div align="center">
<img id="aimg_1007235" aid="1007235" zoomfile="https://di.gameres.com/attachment/forum/202109/09/095918hmd9jvyts99bxj9v.png" data-original="https://di.gameres.com/attachment/forum/202109/09/095918hmd9jvyts99bxj9v.png" width="554" inpost="1" src="https://di.gameres.com/attachment/forum/202109/09/095918hmd9jvyts99bxj9v.png" referrerpolicy="no-referrer">
</div><br>
关于角色的衣着需要有不同的绑定思路，例如犬夜叉比较宽大的衣袍所体现的飘动感和蓬松感，就需要和现代人较普遍收身的服装区别开来，以及脖子上的串珠，依原图并不是纯坠在胸前，而是略有飘动感（形态如路径所示），需要在动态上有所体现。<br>
<br>
<strong><font color="#de5650">动作设计</font></strong><br>
<br>
除了面部表情以外，肢体语言也是非常重要的！<br>
<br>
虽然很多人平时说话并不需要不停打手势，但在立绘角色中手势语言是能够加强个性以及提升互动效果的重要方式。<br>
<br>
<div align="center"><font size="2">
<img id="aimg_1007239" aid="1007239" zoomfile="https://di.gameres.com/attachment/forum/202109/09/095923nvvl11vyuwa85mvx.gif" data-original="https://di.gameres.com/attachment/forum/202109/09/095923nvvl11vyuwa85mvx.gif" width="243" inpost="1" src="https://di.gameres.com/attachment/forum/202109/09/095923nvvl11vyuwa85mvx.gif" referrerpolicy="no-referrer">
</font></div><div align="center"><font size="2">来自崩坏学院2-芙兰</font></div><br>
<strong><font color="#de5650">模型互动展示效果</font></strong><br>
<br>
最终输出的Live2d再搭配所要表达的文案，就可以正式向我们Say Hi啦！<br>
<br>
<div align="center"><font size="2">
<img id="aimg_1007241" aid="1007241" zoomfile="https://di.gameres.com/attachment/forum/202109/09/095926zutdjx77s84s893x.gif" data-original="https://di.gameres.com/attachment/forum/202109/09/095926zutdjx77s84s893x.gif" width="243" inpost="1" src="https://di.gameres.com/attachment/forum/202109/09/095926zutdjx77s84s893x.gif" referrerpolicy="no-referrer">
</font></div><div align="center"><font size="2">来自少女前线-64式</font></div><br>
<strong><font color="#de5650">结语</font></strong><br>
<br>
调制更精妙的药水还是要通过更多不懈的学习哒~<br>
<br>
而且我知道，<br>
<br>
其实游戏制作团队中的同学们都是伟大的魔法师,<br>
<br>
致力于创造一个快乐的世界，<br>
<br>
赋予角色生命和色彩，<br>
<br>
来讲述属于他们无比独特的故事。<br>
<br>
愿游戏人的未来，<br>
<br>
也一直会更加美丽多彩！<br>
<br>
最后<br>
<br>
希望大家每天都开心哦<br>
<br>
<font size="2"></font><br>
<font size="2">来源：隆少</font><br>
<font size="2">原文：https://mp.weixin.qq.com/s/p6EKP6fPbkHqI1wBx49Q_g</font><br>
<br>
<br>
</td></tr></tbody></table>



  
</div>
            