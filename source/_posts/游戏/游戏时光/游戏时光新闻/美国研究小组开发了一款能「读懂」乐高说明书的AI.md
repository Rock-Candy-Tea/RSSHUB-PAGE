
---
title: '美国研究小组开发了一款能「读懂」乐高说明书的AI'
categories: 
 - 游戏
 - 游戏时光
 - 游戏时光新闻
headimg: 'https://img01.vgtime.com/web/topic/2022/08/10/220810115108468_u24074.jpg'
author: 游戏时光
comments: false
date: Wed, 10 Aug 2022 06:15:16 GMT
thumbnail: 'https://img01.vgtime.com/web/topic/2022/08/10/220810115108468_u24074.jpg'
---

<div>   
<input type="hidden" id="topicId" value="1175965">
<input type="hidden" value id="puid">


<div class="abstract">
<p>还能用于家具组装和在《我的世界》中搭建物品。</p>
</div>

                
<div class="topicContent front_content"><p><span style="background-color: initial; letter-spacing: 1.3px;">由美国斯坦福大学、麻省理工学院和 Autodesk 人工智能实验室组成的研究团队开发了一项 「可以将乐高说明书内容转化为机械语言」的技术。通过这项技术，人们可以用机器人来组装乐高积木了。</span></p><p><span style="background-color: initial; letter-spacing: 1.3px;">买过拼装玩具的朋友可能会比较熟悉，厂商一般会随商品附赠一本组装说明书。为了尽可能地让用户理解，说明书一般会用图解的方式进行说明。</span></p><div class="vg_insert_img"><figure contenteditable="false"><img src="https://img01.vgtime.com/web/topic/2022/08/10/220810115108468_u24074.jpg" class="vg_insert_img_onfocus" style="width: 600px;" referrerpolicy="no-referrer"><figcaption class="vg_insert_img_notice" contenteditable="true"></figcaption></figure></div><p>但对于 AI 来说，图解就不是那么友善了。所以研究小组决定构建一个模型，将一个个组装步骤转换为机器可理解的指令，以便机器人能够根据组装指令来拼装乐高。</p><p><span style="background-color: initial; letter-spacing: 1.3px;">为了实现这个目标，设计者必须将说明书中平面的图解理解透彻，然后为每个部件确定一个三维空间中的位置（坐标）和方向，在某些特定场合下，还要考虑部分零件位置出现重叠的情况。 此外，由于乐高有大量的零件，一些数据库中没有的零件也需要重新录入。</span></p><div class="vg_insert_img"><figure contenteditable="false"><img src="https://img01.vgtime.com/web/topic/2022/08/10/220810122309298_u24074.jpg" class="vg_insert_img_onfocus" style="width: 600px;" referrerpolicy="no-referrer"><figcaption class="vg_insert_img_notice" contenteditable="true"></figcaption></figure></div><p><span style="background-color: initial; letter-spacing: 1.3px;">而为了更好地解决上述问题，研究小组提出了一个新的基于学习的框架 — MEPNet（Manual-to-Executable-Plan Network）。他们表示，这项技术能够更好地帮助他们将说明书上的内容转换成机械语言。</span><br></p><p><span style="background-color: initial; letter-spacing: 1.3px;">MEPNet 由两个阶段组成。在第一阶段，系统将提取说明书中所有零部件的形状、大小等构成要素，</span><span style="background-color: initial; letter-spacing: 1.3px;">并通过一个积卷的神经网络来预测组装的关键点和一些零件可能重合的部分</span><span style="background-color: initial; letter-spacing: 1.3px;">。在第二阶段，系统则会通过从第一阶段收集/预测的信息推测出完整模型的外观，并且判断各部件之间可以通过哪些方式连接在一起，从而预估每个部件的位置和方向。</span></p><div class="vg_insert_img"><figure contenteditable="false"><img src="https://img01.vgtime.com/web/topic/2022/08/10/220810122324518_u24074.jpg" class="vg_insert_img_onfocus" style="width: 600px;" referrerpolicy="no-referrer"><figcaption class="vg_insert_img_notice" style="display: none;" contenteditable="true"></figcaption></figure></div><p><span style="background-color: initial; letter-spacing: 1.3px;">此外，研究小组还表示 MEPNet 并不是一项仅限于乐高的技术，它还可以应用在一些其他场景中，比如组装家具或是在《我的世界》中搭建一些物品等。</span></p><div class="vg_insert_img"><figure contenteditable="false"><img src="https://img01.vgtime.com/web/topic/2022/08/10/220810131403330_u24074.jpg" class="vg_insert_img_onfocus" style="width: 600px;" referrerpolicy="no-referrer"><figcaption class="vg_insert_img_notice" contenteditable="true"></figcaption></figure></div><p style="text-align: right;"><span style="background-color: initial; letter-spacing: 1.3px;">来源：</span><a href="https://www.itmedia.co.jp/news/articles/2208/10/news060.html" style="background-color: initial; letter-spacing: 1.3px;">ITmedia</a><br></p></div>
                
                
  
</div>
            