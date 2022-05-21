
---
title: '这只鼠标学会自己玩FPS游戏：准度竟不输职业选手'
categories: 
 - 新媒体
 - 快科技（原驱动之家）
 - 最新新闻
headimg: 'https://img1.mydrivers.com/img/20220521/64d58302910c49d1bf6f8537508245af.gif'
author: 快科技（原驱动之家）
comments: false
date: Sat, 21 May 2022 18:48:10 GMT
thumbnail: 'https://img1.mydrivers.com/img/20220521/64d58302910c49d1bf6f8537508245af.gif'
---

<div>   
<p>近日有一位CMU研究生小哥将自己的鼠标进行改装，<strong>使鼠标成为可以自动瞄准并“精准命中”，还不会被封号的FPS物理外挂。</strong></p>
<p align="center"><img alt="这只鼠标学会自己玩FPS游戏：准度竟不输职业选手" h="293" src="https://img1.mydrivers.com/img/20220521/64d58302910c49d1bf6f8537508245af.gif" style="border: black 1px solid;" w="600" referrerpolicy="no-referrer"></p>
<p>在这之前虽然也有一些物理外挂，但并不能完全让鼠标自己移动并完成射击。这位小哥开发的是一个能够自己独立进行瞄准与射击的FPS物理外挂，并且目前在训练场Aim Lab中的成绩已经超过了一些FPS专业玩家。</p>
<p style="text-align: center"><a href="https://img1.mydrivers.com/img/20220521/e355b9d2-c8d8-4529-80a9-ba6d6927b7c8.png" target="_blank"><img alt="这只鼠标学会自己玩FPS游戏：准度竟不输职业选手" h="287" src="https://img1.mydrivers.com/img/20220521/Se355b9d2-c8d8-4529-80a9-ba6d6927b7c8.png" style="border: black 1px solid" w="600" referrerpolicy="no-referrer"></a></p>
<p><strong>小哥表示为了让鼠标自己“学会”瞄准，他首先给鼠标设计了一个底盘</strong>。底盘用到了四个全向轮和对应的控制电机，能够让机器人朝向任意方向灵活运动，包括走直线等，而这些轮子分别由不同的电机控制。</p>
<p>基本的移动操作实现后，接下来是利用计算机视觉算法，来让它学会“自己寻找猎物”。小哥基于OpenCV写了一个Python目标检测算法，训练它能够根据目标的位置迅速瞄准对应的目标。</p>
<p>从视觉数据反馈到操作上，小哥采用了PID控制算法，让机器人学会自己去找距离最近的“射击点”，在规定时间内瞄中更多的物体。当瞄准物体后，这个机器人就会自行触发鼠标“点击”的动作，从而完成自动射击。</p>
<p align="center"><img alt="这只鼠标学会自己玩FPS游戏：准度竟不输职业选手" h="333" src="https://img1.mydrivers.com/img/20220521/759856d57fdf44928079f5ce272adfb2.gif" style="border: black 1px solid;" w="600" referrerpolicy="no-referrer"></p>
<p>为了加强这个机器人的能力，小哥在一个叫做Aim Lab的第一人称射击游戏模拟器中对它进行训练。<strong>小哥训练的这个“鼠标机器人”，主要还是针对的颜色球射击，其中视觉算法自动找到带颜色的球体，然后机器人跟上去瞄准射击。</strong></p>
<p>调测了两个月算法后，小哥终于训练出了比较满意的机器人，目前在Aim Lab中最高拿到了118494的分数，该得分已经超过了不少专业FPS玩家。</p>


           
           
<p class="end"><img src="https://icons.mydrivers.com/news/end_article.png" referrerpolicy="no-referrer"></p> 
<div style="overflow: hidden;font-size:14px;">
             
          <p class="url"><span style="color:#666">责任编辑：朝晖</span><a href="javascript:;" class="jiucuo" id="leftjiucuo">文章纠错</a></p>
        </div>
        <div class="page_article" id="bnext">
 
</div>
<p class="bqian">话题标签：<a href="https://news.mydrivers.com/tag/shubiao.htm">鼠标</a><a href="https://news.mydrivers.com/tag/gongzuozhiye.htm">工作职业</a><a href="https://news.mydrivers.com/tag/youxi.htm">游戏</a>  </p>
        
</div>
            