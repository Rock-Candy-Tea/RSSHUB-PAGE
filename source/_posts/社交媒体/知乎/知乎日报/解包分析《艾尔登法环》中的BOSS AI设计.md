
---
title: '解包分析《艾尔登法环》中的BOSS AI设计'
categories: 
 - 社交媒体
 - 知乎
 - 知乎日报
headimg: 'https://pic3.zhimg.com/v2-5d4b94821b59be71824541e835833af8_l.jpg?source=8673f162'
author: 知乎
comments: false
date: 2022-04-15 00:40:41
thumbnail: 'https://pic3.zhimg.com/v2-5d4b94821b59be71824541e835833af8_l.jpg?source=8673f162'
---

<div>   
<div class="main-wrap content-wrap">
<div class="headline">

<div class="img-place-holder">



</div>

<div class="content-inner">



<div class="question">
解包分析《艾尔登法环》中的BOSS AI设计（读指令篇）
<div class="answer">

<strong>
<img class="avatar" src="https://pic3.zhimg.com/v2-5d4b94821b59be71824541e835833af8_l.jpg?source=8673f162" referrerpolicy="no-referrer">
<span class="author">对面会更惨，</span><span class="bio">游戏策划</span>
</strong>

<div class="content">
<p>自从《艾尔登法环》发售以来，读指令这三个字一直都是玩家们争论的焦点之一。不少离谱的游戏实况表现和玩家群体中快速传播的动图让很多人对法环的一些 BOSS 行为充满了困惑。</p>
<p>事实上，魂系列 AI 读指令早已不是秘密，《黑暗之魂 1》在读、《血源诅咒》在读、《只狼》也在读。那么抛开大量新进魂系新人玩家涌入的因素，为什么《艾尔登法环》最为人所诟病呢？</p>
<p>本文将通过解包，以 AI 文件、动画文件、各类参数等内容为基础，尝试分析法环中的读指令问题究竟出在哪。</p>
<p>（PS：解包文件是工程逆向的结果，不代表 FS 社员工真的在用这种逆天脚本写 AI）</p>
<hr>
<p><strong>那么，《艾尔登法环》真的读指令了吗？</strong><strong><strong>真读了。</strong></strong></p>
<p class="ztext-empty-paragraph"> <br><br>随便打开一份 AI 的解包文件，我们就可以看到关于 Interrupt 的 Function<br><br></p>
<figure><img class="content-image" src="https://pic3.zhimg.com/v2-687a9c15c1fbb2e7423b5de69d1d61ea_1440w.jpg" alt referrerpolicy="no-referrer"></figure>
<hr>
<p><strong>废话不多说，先请出新人折磨王：熔炉骑士 AI</strong></p>
<figure><img class="content-image" src="https://pic4.zhimg.com/v2-81a23d9da82a3b0eebeba37327f208df_1440w.jpg" alt referrerpolicy="no-referrer"><figcaption>IsInterupt（）</figcaption></figure>
<p>我们从头来看</p>
<div class="highlight">
<pre><code class="language-lua"> <span class="kr">if</span> <span class="n">arg1</span><span class="p">:</span><span class="n">IsInterupt</span><span class="p">(</span><span class="n">INTERUPT_UseItem</span><span class="p">)</span> <span class="ow">and</span> <span class="n">arg1</span><span class="p">:</span><span class="n">HasSpecialEffectId</span><span class="p">(</span><span class="n">TARGET_SELF</span><span class="p">,</span> <span class="mi">5039</span><span class="p">)</span> <span class="o">==</span> <span class="kc">false</span> <span class="kr">then</span></code></pre>
</div>
<p>前边不需要太多的解释了，就是玩家使用道具。那这个 Effect Id 5039 是干什么的呢？</p>
<figure><img class="content-image" src="https://pic1.zhimg.com/v2-9bc2feabd8cc90fe04a8a922bdf4510c_1440w.jpg" alt referrerpolicy="no-referrer"><figcaption>熔炉骑士动作</figcaption></figure>
<p>我们打开熔炉骑士的动画文件后能看到大部分动作中有存在"AddSpEffect 5039”，这个东西其实是代表了熔炉骑士出招过程中自身 AI 不会去做打断的一个时长。</p>
<p>比如上图中这个挥砍的动作总时长是 2.5S，而「5039」占了前 1.5S，也就是说从 AI 的角度上，熔炉骑士一定会挥完这 1.5 S 的剑才能去做别的事情。这是非常合理的，总不能我在神龙摆尾摆一半，看到玩家在喝药，我就突然中断动作上去给他一刀吧？</p>
<p>老贼显然没这么离谱。</p>
<hr>
<p><strong>这里就可以看出「药检」的触发条件了</strong></p>
<ol>
<li>读到玩家喝药的输入指令</li>
<li>自身并没有在其他的招式硬直阶段</li>
</ol>
<p><strong>如果这两个条件都满足，就准备「药检」了：</strong></p>
<div class="highlight">
<pre><code class="language-lua"><span class="kr">if</span> <span class="n">arg1</span><span class="p">:</span><span class="n">IsInsideTargetCustom</span><span class="p">(</span><span class="n">TARGET_SELF</span><span class="p">,</span> <span class="n">TARGET_ENE_0</span><span class="p">,</span> <span class="n">AI_DIR_TYPE_F</span><span class="p">,</span> <span class="mi">120</span><span class="p">,</span> <span class="mi">180</span><span class="p">,</span> <span class="mi">5</span><span class="p">)</span> <span class="kr">then</span>
            <span class="kr">if</span> <span class="n">f23_local4</span> <span class="o"><=</span> <span class="mi">80</span> <span class="kr">then</span>
                <span class="n">arg2</span><span class="p">:</span><span class="n">ClearSubGoal</span><span class="p">()</span>
                <span class="n">arg2</span><span class="p">:</span><span class="n">AddSubGoal</span><span class="p">(</span><span class="n">GOAL_COMMON_ComboTunable_SuccessAngle180</span><span class="p">,</span> <span class="mi">10</span><span class="p">,</span> <span class="mi">3000</span><span class="p">,</span> <span class="n">TARGET_ENE_0</span><span class="p">,</span> <span class="mi">999</span><span class="p">,</span> <span class="n">f23_local2</span><span class="p">,</span> <span class="n">f23_local3</span><span class="p">,</span> <span class="mi">0</span><span class="p">,</span> <span class="mi">0</span><span class="p">)</span>
                <span class="kr">return</span> <span class="kc">true</span>
            <span class="kr">else</span>
                <span class="kr">return</span> <span class="kc">true</span></code></pre>
</div>
<p>IsInsideTargetCustom 实际上是在检测熔炉骑士和玩家间的位置关系，AI_DIR_TYPE 一共有 4 种，分别是：</p>
<blockquote>AI_DIR_TYPE_F：自身前方<br>AI_DIR_TYPE_B：自身后方<br>AI_DIR_TYPE_L：自身左侧<br>AI_DIR_TYPE_R：自身右侧<br><br><br></blockquote>
<p>后边的参数则是角度和距离。</p>
<p>因此这里的前置条件就是【如果玩家在熔炉骑士前方 120°、半径 5 米的扇形区域内】</p>
<p>loacl4 是 Goal.Interrupt = function 中定义的变量，就不贴了。它是一个 1~100 间的随机数，所以<=80 就是「有 80% 的几率」</p>
<p>ClearSubGoal 是清空熔炉骑士 AI 中当前的行为列表，也就是说本来熔炉骑士本来寻思着准备上天了但还没上，一看到你喝药，马上急眼不上了。</p>
<p>AddSubGoal 就是给熔炉骑士 AI 的行为列表中添加行为，参数比较多我们只说重要的：</p>
<blockquote>10：所添加行为的寿命<br>3000：动作 Id<br>TARGET_ENE_0：目标<br>999：下一 combo 能否执行的目标距离判断<br><br><br></blockquote>
<p>（寿命和下一 combo 的距离判断其实是非常重要的参数，直接决定了 AI 的最终表现，但是和本篇内容无关，所以先不细说）</p>
<p>那动作 Id：3000 是啥？</p>
<figure><img class="content-image" src="https://pic4.zhimg.com/v2-bc09987dd46b57f15edcb7b54202ae27_1440w.jpg" alt referrerpolicy="no-referrer"><figcaption>给你一刀</figcaption></figure>
<p>归纳一下：</p>
<blockquote>触发「药检」后，如果玩家在熔炉骑士前方 120°、半径 5 米的扇形区域内，80%几率立刻给你一刀，20% 几率什么都不做</blockquote>
<hr>
<div class="highlight">
<pre><code class="language-lua"><span class="kr">elseif</span> <span class="n">arg1</span><span class="p">:</span><span class="n">IsInsideTargetCustom</span><span class="p">(</span><span class="n">TARGET_SELF</span><span class="p">,</span> <span class="n">TARGET_ENE_0</span><span class="p">,</span> <span class="n">AI_DIR_TYPE_F</span><span class="p">,</span> <span class="mi">120</span><span class="p">,</span> <span class="mi">180</span><span class="p">,</span> <span class="mi">10</span><span class="p">)</span> <span class="kr">then</span>
            <span class="kr">if</span> <span class="n">f23_local4</span> <span class="o"><=</span> <span class="mi">40</span> <span class="kr">then</span>
                <span class="n">arg2</span><span class="p">:</span><span class="n">ClearSubGoal</span><span class="p">()</span>
                <span class="n">arg2</span><span class="p">:</span><span class="n">AddSubGoal</span><span class="p">(</span><span class="n">GOAL_COMMON_ComboTunable_SuccessAngle180</span><span class="p">,</span> <span class="mi">10</span><span class="p">,</span> <span class="mi">3005</span><span class="p">,</span> <span class="n">TARGET_ENE_0</span><span class="p">,</span> <span class="mi">999</span><span class="p">,</span> <span class="n">f23_local2</span><span class="p">,</span> <span class="n">f23_local3</span><span class="p">,</span> <span class="mi">0</span><span class="p">,</span> <span class="mi">0</span><span class="p">)</span>
                <span class="kr">return</span> <span class="kc">true</span>
            <span class="kr">elseif</span> <span class="n">f23_local4</span> <span class="o"><=</span> <span class="mi">80</span> <span class="kr">then</span>
                <span class="n">arg2</span><span class="p">:</span><span class="n">ClearSubGoal</span><span class="p">()</span>
                <span class="n">arg2</span><span class="p">:</span><span class="n">AddSubGoal</span><span class="p">(</span><span class="n">GOAL_COMMON_ComboTunable_SuccessAngle180</span><span class="p">,</span> <span class="mi">10</span><span class="p">,</span> <span class="mi">3006</span><span class="p">,</span> <span class="n">TARGET_ENE_0</span><span class="p">,</span> <span class="mi">999</span><span class="p">,</span> <span class="n">f23_local2</span><span class="p">,</span> <span class="n">f23_local3</span><span class="p">,</span> <span class="mi">0</span><span class="p">,</span> <span class="mi">0</span><span class="p">)</span>
                <span class="kr">return</span> <span class="kc">true</span>
            <span class="kr">else</span>
                <span class="n">arg2</span><span class="p">:</span><span class="n">ClearSubGoal</span><span class="p">()</span>
                <span class="n">arg2</span><span class="p">:</span><span class="n">AddSubGoal</span><span class="p">(</span><span class="n">GOAL_COMMON_ApproachTarget</span><span class="p">,</span> <span class="mi">3</span><span class="p">,</span> <span class="n">TARGET_ENE_0</span><span class="p">,</span> <span class="mi">5</span><span class="p">,</span> <span class="n">TARGET_SELF</span><span class="p">,</span> <span class="kc">false</span><span class="p">,</span> <span class="mi">9910</span><span class="p">)</span>
                <span class="kr">return</span> <span class="kc">true</span>
            <span class="kr">end</span></code></pre>
</div>
<p>有了前边的经验，这里看起来就方便很多了：</p>
<p>【当玩家位于熔炉骑士前方 120°，5~10 米间的扇环时】</p>
<ul>
<li>有 40% 的几率使用，3005，即冲刺挥砍</li>
</ul>
<figure><img class="content-image" src="https://pic3.zhimg.com/v2-7c7f15da94a255bf75511793e011a57e_1440w.jpg" alt referrerpolicy="no-referrer"><figcaption>冲刺挥砍</figcaption></figure>
<ul>
<li>有 40% 概率使用，3006，即咸鱼突刺</li>
</ul>
<figure><img class="content-image" src="https://pic4.zhimg.com/v2-87408495966ff90550fd47a98af7113b_1440w.jpg" alt referrerpolicy="no-referrer"><figcaption>咸鱼突刺</figcaption></figure>
<ul>
<li>剩下 20% 的概率，GOAL_COMMON_ApproachTarget，会接近玩家。3 则是熔炉骑士走路的最大速度系数，大概这样</li>
</ul>
<figure><img class="content-image" src="https://pic3.zhimg.com/v2-a446827ae5008430ab3e1a7de297e4aa_1440w.jpg" alt referrerpolicy="no-referrer"><figcaption>脑门上纹了个「急」</figcaption></figure>
<hr>
<div class="highlight">
<pre><code class="language-lua"><span class="kr">elseif</span> <span class="n">arg1</span><span class="p">:</span><span class="n">IsInsideTargetCustom</span><span class="p">(</span><span class="n">TARGET_SELF</span><span class="p">,</span> <span class="n">TARGET_ENE_0</span><span class="p">,</span> <span class="n">AI_DIR_TYPE_F</span><span class="p">,</span> <span class="mi">120</span><span class="p">,</span> <span class="mi">180</span><span class="p">,</span> <span class="mi">15</span><span class="p">)</span> <span class="kr">then</span>
            <span class="kr">if</span> <span class="n">f23_local4</span> <span class="o"><=</span> <span class="mi">80</span> <span class="kr">then</span>
                <span class="n">arg2</span><span class="p">:</span><span class="n">ClearSubGoal</span><span class="p">()</span>
                <span class="n">arg2</span><span class="p">:</span><span class="n">AddSubGoal</span><span class="p">(</span><span class="n">GOAL_COMMON_ApproachTarget</span><span class="p">,</span> <span class="mi">3</span><span class="p">,</span> <span class="n">TARGET_ENE_0</span><span class="p">,</span> <span class="mi">5</span><span class="p">,</span> <span class="n">TARGET_SELF</span><span class="p">,</span> <span class="kc">false</span><span class="p">,</span> <span class="mi">9910</span><span class="p">)</span>
                <span class="kr">return</span> <span class="kc">true</span>
            <span class="kr">else</span>
                <span class="kr">return</span> <span class="kc">true</span>
            <span class="kr">end</span>
        <span class="kr">end</span></code></pre>
</div>
<p>同理，玩家处于半径 10~15 范围的扇环时</p>
<ul>
<li>80% 几率以最大速度接近玩家</li>
<li>20% 几率什么都不做</li>
</ul>
<p>至此，熔炉骑士的药检部分就全部结束了。</p>
<figure><img class="content-image" src="https://pic3.zhimg.com/v2-acdb05d68c0ebcc4be19684abfc2cada_1440w.jpg" alt referrerpolicy="no-referrer"><figcaption>熔炉骑士读指令简单框图</figcaption></figure>
<p><strong>有两点需要说明一下：</strong></p>
<p><strong>1. 看起来熔炉骑士只有玩家在其前方时才会「药检」，那我站在他背后是不是就安全了？</strong></p>
<p>这是理论存在但<strong>实际不太存在</strong>的情况，除了部分招式的硬直状态，熔炉骑士调整朝向面向玩家是较高优先级的事情，而且根据玩家的相对位置（侧前、后方）不同，转向速度还会大幅度加快。</p>
<figure><img class="content-image" src="https://pic1.zhimg.com/v2-8e9d8674937a6bae2a170c6c325199dc_1440w.jpg" alt referrerpolicy="no-referrer"><figcaption>跟得上我的思必得吗？</figcaption></figure>
<p>更不用说，几乎所有招式中，都包含转向调整的窗口时长这种事了。</p>
<figure><img class="content-image" src="https://pic2.zhimg.com/v2-bafeabf2e22c410d3bf8dab85433c991_1440w.jpg" alt referrerpolicy="no-referrer"><figcaption>闪电五连转</figcaption></figure>
<p>就像这张图，是盾牌猛击的攻击行为，1.12S 的时间内，熔炉骑士可以做到依次以 30、240、120、240、360 的转身速度调整 5 次朝向（只要他需要），所以转身 180°给你一下都属于是牛刀小试了。</p>
<p>因此，在「药检」的设计上，只考虑前方的情况是非常合理的。</p>
<p><strong>2.这是不是意味着我站在熔炉骑士 15 米开外喝药就绝对安全了？</strong></p>
<p>理论上是的，至少熔炉骑士的「药检」AI 部分不会对你的行为做出反馈了。但这不意味着他本身的行为模块不会想办法搞你。</p>
<p><strong>结论：</strong></p>
<p>熔炉骑士的「药检」AI，通过玩家距离的不同分成了近、中、远 3 种。其中近距离（5 米）基本就是站在脸上了，很少有人会这样喝药；而远距离则需要玩家通过 BOSS 硬直、自身体力跑位去达成（15 米），因此熔炉骑士也不会做出即刻的攻击行为。中距离是玩家与熔炉骑士战斗中最常触发的情况，所以 FS 的设计师给中距离预备了 3 种不同的反馈，透过概率来决定。</p>
<p>这套设计我觉得本质上是没有问题的，针对玩家的特殊行为进行反馈；在常见情况中准备了多种行为，增加战斗多样性的同时也强化了对玩家反应维度、操作维度的考察，可圈可点。</p>
<p><strong>而我认为可以优化的地方则是：</strong></p>
<ul>
<li>「药检」模块直接清空原先的行为列表过于武断，必要性不强</li>
</ul>
<p>喝药作为玩家的特殊行为，可以给反馈，但不需要<strong>每次立刻</strong>都要给反馈，行为列表本身有「寿命」，结束后自身就会清掉，不需要强制清空执行药检（或者加个概率清空）</p>
<ul>
<li>近、远距离均有 20% 的行为留白，但中距离却没有，3 种行为均是强压迫性，可以考虑 20% 留白</li>
</ul>
<p>熔炉骑士在 idle 状态下基本常驻举盾，玩家本就难以对其造成伤害，留白并不会降低难度；留白也并不代表原地待着不动，而是在小概率的前提下给予战斗节奏的变化</p>
<div class="highlight">
<pre><code class="language-lua"><span class="kr">if</span> <span class="n">arg1</span><span class="p">:</span><span class="n">IsInterupt</span><span class="p">(</span><span class="n">INTERUPT_Shoot</span><span class="p">)</span> <span class="kr">then</span>
        <span class="kr">if</span> <span class="n">arg1</span><span class="p">:</span><span class="n">HasSpecialEffectId</span><span class="p">(</span><span class="n">TARGET_SELF</span><span class="p">,</span> <span class="mi">5039</span><span class="p">)</span> <span class="o">==</span> <span class="kc">false</span> <span class="kr">then</span>
            <span class="kr">if</span> <span class="n">arg1</span><span class="p">:</span><span class="n">IsInsideTargetCustom</span><span class="p">(</span><span class="n">TARGET_SELF</span><span class="p">,</span> <span class="n">TARGET_ENE_0</span><span class="p">,</span> <span class="n">AI_DIR_TYPE_F</span><span class="p">,</span> <span class="mi">120</span><span class="p">,</span> <span class="mi">180</span><span class="p">,</span> <span class="mi">5</span><span class="p">)</span> <span class="kr">then</span>
                <span class="kr">return</span> <span class="kc">true</span>
            <span class="kr">end</span>
        <span class="kr">elseif</span> <span class="n">arg1</span><span class="p">:</span><span class="n">IsInsideTargetCustom</span><span class="p">(</span><span class="n">TARGET_SELF</span><span class="p">,</span> <span class="n">TARGET_ENE_0</span><span class="p">,</span> <span class="n">AI_DIR_TYPE_F</span><span class="p">,</span> <span class="mi">120</span><span class="p">,</span> <span class="mi">180</span><span class="p">,</span> <span class="mf">7.5</span><span class="p">)</span> <span class="kr">then</span>
            <span class="kr">if</span> <span class="n">arg1</span><span class="p">:</span><span class="n">HasSpecialEffectId</span><span class="p">(</span><span class="n">TARGET_SELF</span><span class="p">,</span> <span class="mi">14606</span><span class="p">)</span> <span class="o">==</span> <span class="kc">true</span> <span class="kr">then</span>
                <span class="n">arg2</span><span class="p">:</span><span class="n">ClearSubGoal</span><span class="p">()</span>
                <span class="n">arg2</span><span class="p">:</span><span class="n">AddSubGoal</span><span class="p">(</span><span class="n">GOAL_COMMON_ComboRepeat_SuccessAngle180</span><span class="p">,</span> <span class="mi">10</span><span class="p">,</span> <span class="mi">3003</span><span class="p">,</span> <span class="n">TARGET_ENE_0</span><span class="p">,</span> <span class="mi">999</span><span class="p">,</span> <span class="mi">0</span><span class="p">,</span> <span class="mi">0</span><span class="p">)</span>
                <span class="kr">return</span> <span class="kc">true</span>
            <span class="kr">end</span>
        <span class="kr">elseif</span> <span class="n">arg1</span><span class="p">:</span><span class="n">IsInsideTargetCustom</span><span class="p">(</span><span class="n">TARGET_SELF</span><span class="p">,</span> <span class="n">TARGET_ENE_0</span><span class="p">,</span> <span class="n">AI_DIR_TYPE_F</span><span class="p">,</span> <span class="mi">120</span><span class="p">,</span> <span class="mi">180</span><span class="p">,</span> <span class="mi">10</span><span class="p">)</span> <span class="kr">then</span>
            <span class="kr">if</span> <span class="n">f23_local4</span> <span class="o"><=</span> <span class="mi">30</span> <span class="kr">then</span>
                <span class="n">arg2</span><span class="p">:</span><span class="n">ClearSubGoal</span><span class="p">()</span>
                <span class="n">arg2</span><span class="p">:</span><span class="n">AddSubGoal</span><span class="p">(</span><span class="n">GOAL_COMMON_ComboTunable_SuccessAngle180</span><span class="p">,</span> <span class="mi">10</span><span class="p">,</span> <span class="mi">3005</span><span class="p">,</span> <span class="n">TARGET_ENE_0</span><span class="p">,</span> <span class="mi">999</span><span class="p">,</span> <span class="n">f23_local2</span><span class="p">,</span> <span class="n">f23_local3</span><span class="p">,</span> <span class="mi">0</span><span class="p">,</span> <span class="mi">0</span><span class="p">)</span>
                <span class="kr">return</span> <span class="kc">true</span>
            <span class="kr">elseif</span> <span class="n">f23_local4</span> <span class="o"><=</span> <span class="mi">60</span> <span class="kr">then</span>
                <span class="n">arg2</span><span class="p">:</span><span class="n">ClearSubGoal</span><span class="p">()</span>
                <span class="n">arg2</span><span class="p">:</span><span class="n">AddSubGoal</span><span class="p">(</span><span class="n">GOAL_COMMON_ComboTunable_SuccessAngle180</span><span class="p">,</span> <span class="mi">10</span><span class="p">,</span> <span class="mi">3006</span><span class="p">,</span> <span class="n">TARGET_ENE_0</span><span class="p">,</span> <span class="mi">999</span><span class="p">,</span> <span class="n">f23_local2</span><span class="p">,</span> <span class="n">f23_local3</span><span class="p">,</span> <span class="mi">0</span><span class="p">,</span> <span class="mi">0</span><span class="p">)</span>
                <span class="kr">return</span> <span class="kc">true</span>
            <span class="kr">else</span>
                <span class="n">arg2</span><span class="p">:</span><span class="n">ClearSubGoal</span><span class="p">()</span>
                <span class="n">arg2</span><span class="p">:</span><span class="n">AddSubGoal</span><span class="p">(</span><span class="n">GOAL_COMMON_ApproachTarget</span><span class="p">,</span> <span class="mi">3</span><span class="p">,</span> <span class="n">TARGET_ENE_0</span><span class="p">,</span> <span class="mi">5</span><span class="p">,</span> <span class="n">TARGET_SELF</span><span class="p">,</span> <span class="kc">false</span><span class="p">,</span> <span class="mi">9910</span><span class="p">)</span>
                <span class="kr">return</span> <span class="kc">true</span>
            <span class="kr">end</span>
        <span class="kr">elseif</span> <span class="n">arg1</span><span class="p">:</span><span class="n">IsInsideTargetCustom</span><span class="p">(</span><span class="n">TARGET_SELF</span><span class="p">,</span> <span class="n">TARGET_ENE_0</span><span class="p">,</span> <span class="n">AI_DIR_TYPE_F</span><span class="p">,</span> <span class="mi">120</span><span class="p">,</span> <span class="mi">180</span><span class="p">,</span> <span class="mi">15</span><span class="p">)</span> <span class="kr">then</span>
            <span class="kr">if</span> <span class="n">f23_local4</span> <span class="o"><=</span> <span class="mi">80</span> <span class="kr">then</span>
                <span class="n">arg2</span><span class="p">:</span><span class="n">ClearSubGoal</span><span class="p">()</span>
                <span class="n">arg2</span><span class="p">:</span><span class="n">AddSubGoal</span><span class="p">(</span><span class="n">GOAL_COMMON_ApproachTarget</span><span class="p">,</span> <span class="mi">3</span><span class="p">,</span> <span class="n">TARGET_ENE_0</span><span class="p">,</span> <span class="mi">5</span><span class="p">,</span> <span class="n">TARGET_SELF</span><span class="p">,</span> <span class="kc">false</span><span class="p">,</span> <span class="mi">9910</span><span class="p">)</span>
                <span class="kr">return</span> <span class="kc">true</span>
            <span class="kr">else</span>
                <span class="kr">return</span> <span class="kc">true</span>
            <span class="kr">end</span>
        <span class="kr">end</span>
    <span class="kr">end</span></code></pre>
</div>
<p>像玩家 Shoot 类指令当然也是有读的，大同小异就不赘述了，感兴趣的可以自己看下。</p>
<p>除此以外，熔炉骑士还会读很多其他形式的玩家输入，<strong>整个读指令模块有 1000 行，约占其全部 AI 的 1/3</strong>。</p>
<hr>
<p><strong>说到读指令，我们不得不提的重量级人物自然少不了这位：</strong></p>
<figure><img class="content-image" src="https://pic3.zhimg.com/v2-61f400a9662a43880717129e6d2151e2_1440w.jpg" alt referrerpolicy="no-referrer"><figcaption>马戏团双雄</figcaption></figure>
<p>直接来吧！</p>
<figure><img class="content-image" src="https://pic3.zhimg.com/v2-ad9941c589462bff201fe1afbfac91a6_1440w.jpg" alt referrerpolicy="no-referrer"><figcaption>这东西内部命名叫「OldLion」，老~狮~子~</figcaption></figure>
<p>说实话，打开文件前我还想会不会是 BUG 或者是逻辑卡死了什么的，没想到打开后发现有点离谱，特别是在看完熔炉骑士之后。</p>
<p>老狮子的 AI 写法上明显和熔炉骑士习惯不同，99% 是不同的设计师制作的，但原理一样，所以我们也不多解释了：</p>
<div class="highlight">
<pre><code class="language-lua"><span class="kr">if</span> <span class="n">arg1</span><span class="p">:</span><span class="n">IsInterupt</span><span class="p">(</span><span class="n">INTERUPT_Shoot</span><span class="p">)</span> <span class="ow">and</span> <span class="n">arg1</span><span class="p">:</span><span class="n">HasSpecialEffectId</span><span class="p">(</span><span class="n">TARGET_SELF</span><span class="p">,</span> <span class="mi">5025</span><span class="p">)</span> <span class="ow">and</span> <span class="n">f36_local3</span> <span class="o">></span> <span class="mi">6</span> <span class="kr">then</span>
        <span class="n">arg2</span><span class="p">:</span><span class="n">ClearSubGoal</span><span class="p">()</span>
        <span class="kr">if</span> <span class="n">arg1</span><span class="p">:</span><span class="n">IsInsideTarget</span><span class="p">(</span><span class="n">TARGET_ENE_0</span><span class="p">,</span> <span class="n">AI_DIR_TYPE_L</span><span class="p">,</span> <span class="mi">180</span><span class="p">)</span> <span class="kr">then</span>
            <span class="kd">local</span> <span class="n">f36_local5</span> <span class="o">=</span> <span class="mf">0.5</span>
            <span class="kd">local</span> <span class="n">f36_local6</span> <span class="o">=</span> <span class="mi">6003</span>
            <span class="kd">local</span> <span class="n">f36_local7</span> <span class="o">=</span> <span class="n">TARGET_ENE_0</span>
            <span class="kd">local</span> <span class="n">f36_local8</span> <span class="o">=</span> <span class="mi">0</span>
            <span class="kd">local</span> <span class="n">f36_local9</span> <span class="o">=</span> <span class="n">AI_DIR_TYPE_R</span>
            <span class="kd">local</span> <span class="n">f36_local10</span> <span class="o">=</span> <span class="mi">0</span>
            <span class="n">arg2</span><span class="p">:</span><span class="n">AddSubGoal</span><span class="p">(</span><span class="n">GOAL_COMMON_SpinStep</span><span class="p">,</span> <span class="n">f36_local5</span><span class="p">,</span> <span class="n">f36_local6</span><span class="p">,</span> <span class="n">f36_local7</span><span class="p">,</span> <span class="n">f36_local8</span><span class="p">,</span> <span class="n">f36_local9</span><span class="p">,</span> <span class="n">f36_local10</span><span class="p">)</span></code></pre>
</div>
<p>老狮子执行躲避弹道的行为执行有 3 个前置条件：</p>
<ol>
<li>检测到玩家输入弹道操作（投掷物、法术、弓箭等）</li>
<li>狮子自己身上有 5025 的状态（可以看出，这里逻辑和熔炉骑士是反的，狮子在少数过渡动作上添加了 5025，而在处于这些状态下时，去执行闪避；最终结果还是不打断常规出招）</li>
<li>与玩家间的直线距离大于 6</li>
</ol>
<p>条件均满足后分为两种情况</p>
<ul>
<li>IsInsideTarget 检测了与玩家间的位置关系，玩家位于其左侧 180°扇形时，执行 6003 行为</li>
</ul>
<figure><img class="content-image" src="https://pic3.zhimg.com/v2-b9eae48bd5baebe07ffd5a0c8cace4aa_1440w.jpg" alt referrerpolicy="no-referrer"><figcaption>简单右跳</figcaption></figure>
<div class="highlight">
<pre><code class="language-lua"> <span class="kr">else</span>
            <span class="kd">local</span> <span class="n">f36_local5</span> <span class="o">=</span> <span class="mf">0.5</span>
            <span class="kd">local</span> <span class="n">f36_local6</span> <span class="o">=</span> <span class="mi">6002</span>
            <span class="kd">local</span> <span class="n">f36_local7</span> <span class="o">=</span> <span class="n">TARGET_ENE_0</span>
            <span class="kd">local</span> <span class="n">f36_local8</span> <span class="o">=</span> <span class="mi">0</span>
            <span class="kd">local</span> <span class="n">f36_local9</span> <span class="o">=</span> <span class="n">AI_DIR_TYPE_L</span>
            <span class="kd">local</span> <span class="n">f36_local10</span> <span class="o">=</span> <span class="mi">0</span>
            <span class="n">arg2</span><span class="p">:</span><span class="n">AddSubGoal</span><span class="p">(</span><span class="n">GOAL_COMMON_SpinStep</span><span class="p">,</span> <span class="n">f36_local5</span><span class="p">,</span> <span class="n">f36_local6</span><span class="p">,</span> <span class="n">f36_local7</span><span class="p">,</span> <span class="n">f36_local8</span><span class="p">,</span> <span class="n">f36_local9</span><span class="p">,</span> <span class="n">f36_local10</span><span class="p">)</span>
        <span class="kr">end</span>
        <span class="kr">return</span> <span class="kc">true</span></code></pre>
</div>
<p>反之，自然就是玩家位于其右侧 180°扇形时，执行 6002 行为</p>
<figure><img class="content-image" src="https://pic2.zhimg.com/v2-feaeb68f59d4fe06dbc5e1bee6e6ff1d_1440w.jpg" alt referrerpolicy="no-referrer"><figcaption>简单左跳</figcaption></figure>
<p>没了。</p>
<p><strong>这里有几个问题，都很严重：</strong></p>
<p><strong>1.单纯将与玩家的相对方位分成左右两个扇形基本没有实际意义</strong></p>
<p>由于魂系游戏中怪物基本都会随时调整方位来保证时刻朝向目标，因此在玩家不动的情况下，这个判断结果只取决于横跳动作后的朝向调整中的细微误差。最终导致的就是上面马戏团双雄的图里，左右横跳看起来完全是随机的。给人一种只写了 50% 左跳、50%右跳 的逻辑，廉价感很强</p>
<p><strong>2.没有设置读指令的距离上限</strong></p>
<p>老狮子这里躲避的判断前提只有距离大于 6，却没有上限，熔炉骑士的 AI 中上限是 15。如果我没记错的话，15 应该是大部分法术技能打不到的距离了，卡这个距离是非常合理的设计。大于这个距离，即便你放法术，我也只会常规逼近而不会<strong>虚空闪避</strong>。</p>
<p><strong>3.完全没有做 SpaceCheck</strong></p>
<div class="highlight">
<pre><code class="language-lua"><span class="kr">if</span> <span class="n">f40_local0</span> <span class="o">>=</span> <span class="mi">5</span> <span class="ow">and</span> <span class="n">SpaceCheck</span><span class="p">(</span><span class="n">arg0</span><span class="p">,</span> <span class="n">arg1</span><span class="p">,</span> <span class="mi">0</span><span class="p">,</span> <span class="mi">5</span><span class="p">)</span> <span class="o">==</span> <span class="kc">true</span> <span class="kr">then</span>
        <span class="n">f40_local10</span> <span class="o">=</span> <span class="n">f40_local13</span>
    <span class="kr">elseif</span> <span class="n">SpaceCheck</span><span class="p">(</span><span class="n">arg0</span><span class="p">,</span> <span class="n">arg1</span><span class="p">,</span> <span class="o">-</span><span class="mi">45</span><span class="p">,</span> <span class="mi">5</span><span class="p">)</span> <span class="o">==</span> <span class="kc">true</span> <span class="kr">then</span>
        <span class="kr">if</span> <span class="n">SpaceCheck</span><span class="p">(</span><span class="n">arg0</span><span class="p">,</span> <span class="n">arg1</span><span class="p">,</span> <span class="mi">45</span><span class="p">,</span> <span class="mi">5</span><span class="p">)</span> <span class="o">==</span> <span class="kc">true</span> <span class="kr">then</span>
            <span class="kr">if</span> <span class="n">f40_local1</span> <span class="o"><=</span> <span class="mi">50</span> <span class="kr">then</span>
                <span class="n">f40_local10</span> <span class="o">=</span> <span class="n">f40_local11</span>
            <span class="kr">else</span>
                <span class="n">f40_local10</span> <span class="o">=</span> <span class="n">f40_local12</span>
            <span class="kr">end</span>
        <span class="kr">else</span>
            <span class="n">f40_local10</span> <span class="o">=</span> <span class="n">f40_local12</span>
        <span class="kr">end</span>
    <span class="kr">elseif</span> <span class="n">SpaceCheck</span><span class="p">(</span><span class="n">arg0</span><span class="p">,</span> <span class="n">arg1</span><span class="p">,</span> <span class="mi">45</span><span class="p">,</span> <span class="mi">5</span><span class="p">)</span> <span class="o">==</span> <span class="kc">true</span> <span class="kr">then</span>
        <span class="n">f40_local10</span> <span class="o">=</span> <span class="n">f40_local12</span>
    <span class="kr">else</span></code></pre>
</div>
<p>这是我从《艾尔登法环》中红灵 NPC 的 AI 里截取的，可以看到里边大量使用了 SpaceCheck 进行判断，这其实是在判断自身周围一定范围内有没有障碍物。《只狼》中的大部分 NPC 会在执行侧闪行为前进行类似的判断，这非常合理：右边有障碍物，你还非得往右边闪吗？而这老狮子，从图上可以看出，右边已经是墙了，自己还在往墙里怼，带给玩家的表现就很差，直白来说就是显得傻。</p>
<p><strong>4.没有提供多种反馈形式、没有留白</strong></p>
<p>熔炉骑士的反馈根据距离远近分为了 3 类，每种距离内又分别分成了 2、3、2 小类。老狮子的反馈有且仅有一种（左右横跳不算两种），并且在没有检测距离上限的情况下，没有留白就意味着<strong>逢 Shoot 必跳</strong>，势必是要被批判一番的。</p>
<p>实际上，老狮子的现有资源就已经可以支持多种反馈形式：</p>
<figure><img class="content-image" src="https://pic4.zhimg.com/v2-7cf8248ee0e4a4d0ce8efe9d2e241e7b_1440w.jpg" alt referrerpolicy="no-referrer"><figcaption>强扑</figcaption></figure>
<p>如果玩家在 6~10 米范围内发射投射物，我是不是可以给予 20% 的概率前扑攻击，增加压迫性？</p>
<figure><img class="content-image" src="https://pic4.zhimg.com/v2-dcbd4658729012aa6876e577696bf1c7_1440w.jpg" alt referrerpolicy="no-referrer"><figcaption>后跳</figcaption></figure>
<p>是不是可以把后跳加入躲闪序列中？横跳下怪物与玩家距离不变，后跳改变了距离，就会有新的 AI 模块被激活，产生变数。</p>
<p>最后就是留白，不一定每次玩家 shoot 都一定要有反馈。</p>
<p><strong>这样一来，可能谈不上多好，起码不会被送到马戏团里了。</strong></p>
<hr>
<p>结合熔炉骑士来看，老狮子的设计师我感觉是资历较浅亦或是新人 / 应届生：</p>
<ul>
<li>老狮子的 AI 里，函数中所使用的参数都使用了已经定义好默认值的变量，而熔炉骑士的制作者直接在函数的传参里填了值。虽然前者很规范，但做多了在保证没问题的前提下，____________吧？</li>
<li>一般来说，操作不可打断的窗口条件时，标签肯定是【不可打断】，而不是反过来把可以打断的地方全都贴上能打断的标签。</li>
<li>同样执行玩家方位检测时，熔炉骑士的制作者使用了 IsInsideTargetCustom，而老狮子的制作者使用的是 IsInsideTarget，它们功能基本一致，区别是前者拥有额外的两个参数输入，用来判断玩家的距离。简单来说就是该严谨的地方严谨了。</li>
</ul>
<p><strong>总结：</strong></p>
<p>正如文章开头所说，读指令在某些使用情景下是完全没有问题的，它不仅可以动态的改变战斗的节奏，还可以让玩家更好的感知到自己行为所产生的反馈，显得 AI 更加「聪明」。这也是该设计方向能够在 FS 的游戏当中传承至今的重要原因。《黑暗之魂 1》里 A 大就已经能对玩家的远程攻击产生 3 种不同形式的反馈了，《只狼》里人人都知道「药检」的存在，却很少有人去喷它是不合理的。而《艾尔登法环》中被玩家截出的种种啼笑皆非的读指令事件，除了少数是因为 BUG，绝大部分还是因为实际制作者层面出现了问题：</p>
<blockquote>至少在读指令这一块，有些怪物的 AI 甚至不如《黑暗之魂 1》考虑的周到</blockquote>
<p>这并不是老狮子制作者的问题，我更倾向于认为由于制作周期、开放世界制作量指数级爆炸等因素，导致资深员工疲于生产内容，不能去做太细致的指导，也没有时间去 review 这种「细枝末节」的东西。</p>
<p>最后，希望小高拿了今年的 GOTY，多招点人，让我早点玩到 DLC 和新作。</p>
<figure><img class="content-image" src="https://pic1.zhimg.com/v2-b1fb8b44f6500d7044237b4be4040978_1440w.jpg" alt referrerpolicy="no-referrer"></figure>

<div class="view-more"><a href="https://zhuanlan.zhihu.com/p/492629716">查看知乎讨论</a></div>

</div>
</div>
</div>


</div>
</div></div>  
</div>
            