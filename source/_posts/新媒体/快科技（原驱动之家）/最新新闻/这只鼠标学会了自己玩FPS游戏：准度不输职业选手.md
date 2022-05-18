
---
title: '这只鼠标学会了自己玩FPS游戏：准度不输职业选手'
categories: 
 - 新媒体
 - 快科技（原驱动之家）
 - 最新新闻
headimg: 'https://img1.mydrivers.com/img/20220518/51b7cac88dfa4463acf984d9ef47b4cc.gif'
author: 快科技（原驱动之家）
comments: false
date: Wed, 18 May 2022 15:07:26 GMT
thumbnail: 'https://img1.mydrivers.com/img/20220518/51b7cac88dfa4463acf984d9ef47b4cc.gif'
---

<div>   
<p>能自动瞄准并“精准命中”，还不会被封号的FPS外挂，你见过吗？</p>
<p>现在，真的有一位CMU研究生小哥，将自己的鼠标变成了FPS游戏里的“神狙手”！</p>
<p>给它安上四个轮子后，鼠标便能根据CV算法反馈，自动瞄准并实现一枪狙击。</p>
<p align="center"><img alt="这只鼠标学会了自己玩FPS游戏：准度不输职业选手" h="234" src="https://img1.mydrivers.com/img/20220518/51b7cac88dfa4463acf984d9ef47b4cc.gif" style="border: black 1px solid;" w="480" referrerpolicy="no-referrer"></p>
<p>在这之前，虽然也有一些物理外挂，但还不至于自动化到让鼠标自己移动并完成射击。</p>
<p>如果选择第三方软件修改等外挂，又极容易被直接封号。</p>
<p>思索一番，这位小哥便开发了一个能自己瞄准目标的FPS物理外挂，目前在训练场Aim Lab中的成绩已经超过了一些FPS专业玩家——</p>
<p>人类FPS专家平均在80000~90000分左右，而它拿到了110000+分。</p>
<p>有网友看完后表示“绝不简单”：对于写过代码的人来说，这可没听上去那么轻松。</p>
<p style="text-align: center"><a href="https://img1.mydrivers.com/img/20220518/01a05ade-dff6-4282-9a04-c21919f2bcf1.png" target="_blank"><img alt="这只鼠标学会了自己玩FPS游戏 在训练场中准度不输职业选手" h="82" src="https://img1.mydrivers.com/img/20220518/S01a05ade-dff6-4282-9a04-c21919f2bcf1.png" style="border: black 1px solid" w="600" referrerpolicy="no-referrer"></a></p>
<p>所以，他究竟是怎么做到的呢？</p>
<p><span style="color:#0000ff;"><strong>将鼠标变成“神狙手”</strong></span></p>
<p>为了让鼠标自己“学会”瞄准，这名小哥首先给鼠标设计了一个底盘。</p>
<p>在他的设想中，这个底盘要能带着鼠标灵活移动，原理大概像这样：</p>
<p align="center"><img alt="这只鼠标学会了自己玩FPS游戏：准度不输职业选手" h="266" src="https://img1.mydrivers.com/img/20220518/8329296bba0745aab1367dc3babea77b.gif" style="border: black 1px solid;" w="480" referrerpolicy="no-referrer"></p>
<p>思路有了后，最终底盘用到了四个全向轮和对应的控制电机。</p>
<p align="center"><img alt="这只鼠标学会了自己玩FPS游戏：准度不输职业选手" h="266" src="https://img1.mydrivers.com/img/20220518/5e37941be5f740108c6997660c39c4d1.gif" style="border: black 1px solid;" w="480" referrerpolicy="no-referrer"></p>
<p>简单来说，各个方向的全向轮（omni wheels），能够让机器人朝向任意方向灵活运动，包括直接走直线等，而这些轮子分别由不同的电机控制。</p>
<p style="text-align: center"><a href="https://img1.mydrivers.com/img/20220518/76c5975a-dfd2-486e-9485-07f477479111.png" target="_blank"><img alt="这只鼠标学会了自己玩FPS游戏 在训练场中准度不输职业选手" h="328" src="https://img1.mydrivers.com/img/20220518/S76c5975a-dfd2-486e-9485-07f477479111.png" style="border: black 1px solid" w="600" referrerpolicy="no-referrer"></a></p>
<p>基本的移动操作实现后，就是利用计算机视觉算法，来让它学会“自己寻找猎物”了。</p>
<p>小哥基于OpenCV写了一个Python目标检测算法，训练它能够根据目标的位置迅速瞄准对应的目标：</p>
<p align="center"><img alt="这只鼠标学会了自己玩FPS游戏：准度不输职业选手" h="266" src="https://img1.mydrivers.com/img/20220518/cc42ccd8f7284537ae4521383968acf3.gif" style="border: black 1px solid;" w="480" referrerpolicy="no-referrer"></p>
<p>从视觉数据反馈到操作上，小哥采用了PID控制算法，让机器人学会自己去找距离最近的“射击点”，来在规定时间内瞄中更多的物体：</p>
<p align="center"><img alt="这只鼠标学会了自己玩FPS游戏：准度不输职业选手" h="266" src="https://img1.mydrivers.com/img/20220518/383ca730070f4caab80e6e408d1925f8.gif" style="border: black 1px solid;" w="480" referrerpolicy="no-referrer"></p>
<p>当瞄准物体后，这个机器人就会自行触发鼠标“点击”的动作，从而完成自动射击。</p>
<p><span style="color:#0000ff;"><strong>在测试中超过部分专业玩家</strong></span></p>
<p>为了加强这个机器人的能力，小哥在一个叫做Aim Lab的第一人称射击游戏模拟器中对它进行训练。</p>
<p>目前，有不少专业FPS玩家都会在Aim Lab中训练，里面也包含了各种不同类型的射击任务，例如人形移动靶、飞靶等。</p>
<p align="center"><img alt="这只鼠标学会了自己玩FPS游戏：准度不输职业选手" h="266" src="https://img1.mydrivers.com/img/20220518/161abba9881c4c4084240f3170f99809.gif" style="border: black 1px solid;" w="480" referrerpolicy="no-referrer"></p>
<p>小哥训练的这个“鼠标机器人”，主要针对的还是颜色球射击，其中视觉算法自动找到带颜色的球体，然后机器人跟上去瞄准射击。</p>
<p>调测了两个月算法后，小哥终于训练出了比较满意的机器人，目前在Aim Lab中最高拿到了118494的分数，超过了不少专业FPS玩家。</p>
<p style="text-align: center"><a href="https://img1.mydrivers.com/img/20220518/ee2def29-657b-4892-bc84-1eefb5d331f7.png" target="_blank"><img alt="这只鼠标学会了自己玩FPS游戏 在训练场中准度不输职业选手" h="298" src="https://img1.mydrivers.com/img/20220518/See2def29-657b-4892-bc84-1eefb5d331f7.png" style="border: black 1px solid" w="600" referrerpolicy="no-referrer"></a><br>
△一名职业选手公开分数</p>
<p>不过目前它还没有打破Aim Lab的最高纪录（146902分）。</p>
<p>也有一个原因是在挑战最高分数的过程中，它的底盘因转速过快烧毁了一个电机，无法再度挑战最高分（手动狗头）。</p>
<p>开发这个物理外挂的小哥名叫Kamal Carter，本科毕业于CMU，目前在CMU读硕士研究生，同时也在Howie Choset教授创立的HEBI Robotics公司工作。</p>
<p style="text-align: center"><img alt="这只鼠标学会了自己玩FPS游戏 在训练场中准度不输职业选手" h="368" src="https://img1.mydrivers.com/img/20220518/6aac9aa6-31d0-4622-b26f-1e596a6f8fc7.png" style="border: black 1px solid" w="372" referrerpolicy="no-referrer"></p>
<p>据小哥自己介绍，他高中的时候就开始玩机器人了，目前研究兴趣也是机械设计和CAD等。</p>
<p>对此有网友调侃，这个机器人值得一个更好的鼠标：</p>
<p style="text-align: center"><a href="https://img1.mydrivers.com/img/20220518/e68e67e9-6193-41f5-834b-7f15f933b6a0.png" target="_blank"><img alt="这只鼠标学会了自己玩FPS游戏 在训练场中准度不输职业选手" h="81" src="https://img1.mydrivers.com/img/20220518/Se68e67e9-6193-41f5-834b-7f15f933b6a0.png" style="border: black 1px solid" w="600" referrerpolicy="no-referrer"></a></p>
<p>但也有网友认为，小哥具有这般能力，更应该做点有用的东西，而不是搞这些物理外挂。</p>
<p style="text-align: center"><a href="https://img1.mydrivers.com/img/20220518/1f24e157-9d07-4e46-aa5b-06b3c7abf71c.png" target="_blank"><img alt="这只鼠标学会了自己玩FPS游戏 在训练场中准度不输职业选手" h="73" src="https://img1.mydrivers.com/img/20220518/S1f24e157-9d07-4e46-aa5b-06b3c7abf71c.png" style="border: black 1px solid" w="600" referrerpolicy="no-referrer"></a></p>
<p>那么，你觉得呢？</p>
<p>OpenCV视觉算法教程：</p>
<p>https://docs.opencv.org/4.x/df/d9d/tutorial_py_colorspaces.html</p>
<p>参考链接：</p>
<p>[1]https://www.youtube.com/watch?v=ne9bmMX82iY</p>
<p>[2]https://www.pcgamer.com/a-roboticist-built-a-hardware-aimbot-that-could-outperform-the-pros-until-it-aimed-so-hard-it-died/</p>
<p>[3]https://hackaday.com/2022/04/30/aimbot-does-it-in-hardware/</p>
<p>[4]https://krcarter.github.io/</p>

           
           
<p class="end"><img src="https://icons.mydrivers.com/news/end_article.png" referrerpolicy="no-referrer"></p> 
<div style="overflow: hidden;font-size:14px;">
             
          <p class="url"><span style="color:#666">责任编辑：随心</span><a href="javascript:;" class="jiucuo" id="leftjiucuo">文章纠错</a></p>
        </div>
        <div class="page_article" id="bnext">
 
</div>
<p class="bqian">话题标签：<a href="https://news.mydrivers.com/tag/shubiao.htm">鼠标</a><a href="https://news.mydrivers.com/tag/diyirenchensheji.htm">第一人称射击</a><a href="https://news.mydrivers.com/tag/youxi.htm">游戏</a>  </p>
        
</div>
            