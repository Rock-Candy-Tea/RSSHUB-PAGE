
---
title: '为什么电池容量一般用安时（Ah）作为单位，这不科学呀，为什么不用瓦时（Wh）？'
categories: 
 - 社交媒体
 - 知乎
 - 知乎日报
headimg: 'https://pic3.zhimg.com/v2-b8c4992b61b3435c653f23af24846efb_l.jpg?source=8673f162'
author: 知乎
comments: false
date: 2022-06-16 07:10:02
thumbnail: 'https://pic3.zhimg.com/v2-b8c4992b61b3435c653f23af24846efb_l.jpg?source=8673f162'
---

<div>   
<div class="main-wrap content-wrap">
<div class="headline">

<div class="img-place-holder">



</div>

<div class="content-inner">




<div class="question">


<div class="answer">

<strong>
<img class="avatar" src="https://pic3.zhimg.com/v2-b8c4992b61b3435c653f23af24846efb_l.jpg?source=8673f162" referrerpolicy="no-referrer">
<span class="author">张抗抗，</span><span class="bio">电动汽车</span>
<a href="https://www.zhihu.com/question/22029368/answer/2528240871" class="originUrl" hidden>查看知乎原文</a>
</strong>

<div class="content">
<p>安时 Ah 从名字就可以看出，它是电流×时间。考虑到电流 = 电量（电子的数目）/ 时间。所以 Ah 就是可移动电子的数量。<strong>根据电荷守衡，安时 Ah 也就是锂电池可用于充放电的锂离子数量</strong>。</p>
<p>请注意，这是一个“物质的量”。根据物质守恒定律，锂离子作为一种物质，无论是快充还是慢充，无论在什么温度下放电，它的量是不会发生变化的。除非发生电池衰减或低温放不出电，那也只是可用于充放电的锂离子变少了，而不是湮灭了。</p>
<p>Wh 则不同，它是 Ah × V，表示的是能量。能量具体是多少，与锂离子移动时那一瞬间的电压有关。<strong>打个比方，你拿一盆水往下波，水的量相同时，从高处泼的杀伤力会更大一些。</strong></p>
<p>根据锂电池的电化学特性，它的电压是 SOC 的稳定函数，可以说是开路电压稳定。<strong>但锂电池有内阻，在快放与慢放时的端电压是不同的；温度也会影响内阻，导致端电压不同；因此放出的能量也不同。能量的差值，就变成了锂电池的内部生热</strong>。</p>
<p>如此以来，Wh 就是一个依赖充放电条件的量，而<strong>Ah 相对 Wh 来说并不那么</strong>依赖充放电条件（并不是完全不依赖)。</p>
<p>所以，用 Ah 来做单位的时候，就可以省略一句话“在 0.01C 的放电条件下，此电池的容量是 xx Wh”，相对来说更简便一些。</p>
<p><strong>但是在组成电动汽车电池包之后，每家公司的电池包电压不同，用 Ah 来表示的话，就难以区分真实大小。 </strong>比如 800V 100Ah 的电池，看起来比 400V 150Ah 的电池小，但实际上的储存能量大啊！</p>
<p>所以 ，在电动汽车或其它电压不同的应用场合，大家就用 kWh 作为通用单位。</p>
<p><strong>这有一个前提，这个 kWh 的值必须是按照国标来测出来 —— 因为国标的存在，它规定了测试 Wh 的放电条件 ，从而使得 Wh 也和 Ah 一样，也成为了一个“不需要表述放电条件”的物理量了，一样很方便。</strong></p>
<p><strong>补充：</strong>有人疑惑，不同测试条件下，Ah 数也不一定相同。确实如此，但咱们为了区别 Ah 与 Wh，只需要找到一个 Ah 相同而 Wh 不同的标准试验，例如：</p>
<p><strong>设计一个试验 1</strong>，相同温度下，以 x C 的倍率放电，在后段逐渐降低到电流至 0.01C，然后到相同的截止电压 Vmin 截止。 <strong>设 x = 1、2、3，做三次试验会发现：Ah 数相同，Wh 数不同</strong>。</p>
<p>还有人质疑：既然你可以设计一个试验让 Ah 相同而 Wh 不同，那我也可以设计一个试验让 Wh 相同，而 Ah 不同啊？例如：</p>
<p><strong>设计一个试验 2</strong>，相同温度下，以 xC 的倍率放电，在后段逐渐降低到电流至 0.01C，然后到 Vmin 的电压截止。 设 x = 1、2、3，做三次试验，然后精巧地选择截止电压 Vmin1、Vmin2、Vmin3，总能找到，Ah 数不同，而 Wh 数相同。</p>
<p><strong>是的，的确如此，但你应该可以轻易看出来，试验 1 是一个标准试验，而试验 2 是一个精挑细选参数 Vmin 才能成立的偶然试验。</strong>这两个试验的说服力是不一样的，从中你应该可以感受到 Ah 与 Wh 对充放电条件依赖程度的不同。</p>
</div>
</div>


<div class="view-more"><a href="https://www.zhihu.com/question/22029368">查看知乎讨论<span class="js-question-holder"></span></a></div>

</div>


</div>
</div></div>  
</div>
            