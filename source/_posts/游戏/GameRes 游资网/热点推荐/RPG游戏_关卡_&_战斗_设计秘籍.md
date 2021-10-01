
---
title: 'RPG游戏_关卡_&_战斗_设计秘籍'
categories: 
 - 游戏
 - GameRes 游资网
 - 热点推荐
headimg: 'https://di.gameres.com/attachment/forum/202109/30/095232qnnlnnjlnuozm9ql.jpg'
author: GameRes 游资网
comments: false
date: Thu, 30 Sep 2021 00:00:00 GMT
thumbnail: 'https://di.gameres.com/attachment/forum/202109/30/095232qnnlnnjlnuozm9ql.jpg'
---

<div>   
<table cellspacing="0" cellpadding="0"><tbody><tr><td class="t_f" id="postmessage_2515944">
<div align="center">
<img id="aimg_1012366" aid="1012366" zoomfile="https://di.gameres.com/attachment/forum/202109/30/095232qnnlnnjlnuozm9ql.jpg" data-original="https://di.gameres.com/attachment/forum/202109/30/095232qnnlnnjlnuozm9ql.jpg" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202109/30/095232qnnlnnjlnuozm9ql.jpg" referrerpolicy="no-referrer">
</div>
<br><font color="#808080">首发知乎“游戏设计师的自我修养”</font><br><font color="#808080">https://zhuanlan.zhihu.com/p/414222813</font><br><br><strong><font color="#de5650">前言</font></strong><br><br>
在很多游戏项目中，关卡与战斗的内容制作分工较为清晰，会有对应的关卡与战斗策划进行合作。<br><br>
但很多时候，这两部分内容的知识点具备许多共性，需要策划都能够了解、掌握……<br><br>
个人在近两年的时间参与并负责了诸多战斗、副本从0到1的实现，总结个人经验的同时，结合许多前人经验、书籍资料、网络资源……整理出了一份RPG游戏中关卡&战斗设计脑图，把设计的关键点尽量展开呈现了出来。<br><br>
这些点并不能给关卡&战斗设计提供一份标准答案，它最大的作用是帮助新人战斗&关卡策划对于一些设计方向迅速建立概念并学习。<br><br>
对于OG策划而言，这些内容已是烂熟于心，但网络上确实提供给关卡&战斗策划学到的知识匮乏，整理出来，希望能有所帮助，读后若无价值，还望理解。<br><br>
友情提醒，文章内容不包含任何配置的基础概念或技能，若对于关卡&战斗实现不太了解的同学，可以先收藏本文，日后再消化。<br><br><strong><font color="#de5650">关卡设计</font></strong><br><br>
关卡设计的整个脑图长度过长，下图先进行总览，具体细节会分图进行展示。<br><br><div align="center"><img id="aimg_FS70R" data-original="https://pic1.zhimg.com/v2-7c682f4e737cca159de1b614b3197adc_r.jpg" onmouseover="img_onmouseoverfunc(this)" lazyloadthumb="1" style="width:100%;max-width:600px;" border="0" alt src="https://pic1.zhimg.com/v2-7c682f4e737cca159de1b614b3197adc_r.jpg" referrerpolicy="no-referrer"></div>
<div align="center"><font size="2"><font color="#808080">关卡设计总览</font></font></div>
<br><strong><font color="#de5650">战斗节奏的控制</font></strong><br><br><strong>战斗系统层面节奏的控制</strong><br><br><div align="center"><img id="aimg_gsp8e" data-original="https://pic4.zhimg.com/v2-39719e1ff02b9144e76df6c43140d97b_r.jpg" onmouseover="img_onmouseoverfunc(this)" lazyloadthumb="1" style="width:100%;max-width:600px;" border="0" alt src="https://pic4.zhimg.com/v2-39719e1ff02b9144e76df6c43140d97b_r.jpg" referrerpolicy="no-referrer"></div>
<div align="center"><font size="2"><font color="#808080">战斗系统层面节奏的控制</font></font></div>
<br><strong>关卡层面战斗节奏的控制</strong><br><br><div align="center"><img id="aimg_fdEPb" width="600" height="800" data-original="https://pic2.zhimg.com/v2-55a039b9ab23e8d8d99564b4d39e99bd_r.jpg" onmouseover="img_onmouseoverfunc(this)" style="cursor:pointer" border="0" alt src="https://pic2.zhimg.com/v2-55a039b9ab23e8d8d99564b4d39e99bd_r.jpg" referrerpolicy="no-referrer"></div>
<div align="center"><font size="2"><font color="#808080">关卡层面战斗节奏的控制</font></font></div>
<br><strong>场景设计</strong><br><br><div align="center"><img id="aimg_yNPmP" width="600" height="1736" data-original="https://pic3.zhimg.com/v2-c4275ca91d987dd8bfc2ccb1db917cfe_r.jpg" onmouseover="img_onmouseoverfunc(this)" style="cursor:pointer" border="0" alt src="https://pic3.zhimg.com/v2-c4275ca91d987dd8bfc2ccb1db917cfe_r.jpg" referrerpolicy="no-referrer"></div>
<div align="center"><font size="2"><font color="#808080">场景设计</font></font></div>
<br><strong>怪物设计</strong><br><br><div align="center"><img id="aimg_I8BEZ" width="600" height="1971" data-original="https://pic4.zhimg.com/v2-b34f8f87eecd9cc4ee83a92bba5ea383_r.jpg" onmouseover="img_onmouseoverfunc(this)" style="cursor:pointer" border="0" alt src="https://pic4.zhimg.com/v2-b34f8f87eecd9cc4ee83a92bba5ea383_r.jpg" referrerpolicy="no-referrer"></div>
<div align="center"><font size="2"><font color="#808080">怪物设计</font></font></div>
<br><strong>关卡战斗外的一些点</strong><br><br><div align="center"><img id="aimg_c28EB" width="600" height="251" data-original="https://pic1.zhimg.com/v2-419317d215d90445f9d3f28e0fc940c0_r.jpg" onmouseover="img_onmouseoverfunc(this)" style="cursor:pointer" border="0" alt src="https://pic1.zhimg.com/v2-419317d215d90445f9d3f28e0fc940c0_r.jpg" referrerpolicy="no-referrer"></div>
<div align="center"><font size="2"><font color="#808080">关卡战斗外的一些点</font></font></div>
<br>
最后，希望以上的知识点能够有所帮助，辅助建立属于你的详尽关卡&战斗设计理念！<br><br><font size="2"><font color="#808080"></font></font><br><font size="2"><font color="#808080">原文：https://zhuanlan.zhihu.com/p/414222813</font></font><br>
</td></tr></tbody></table>


  
</div>
            