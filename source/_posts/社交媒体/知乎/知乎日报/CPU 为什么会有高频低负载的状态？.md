
---
title: 'CPU 为什么会有高频低负载的状态？'
categories: 
 - 社交媒体
 - 知乎
 - 知乎日报
headimg: 'https://pic2.zhimg.com/v2-86ea4b8b7df16d9c219613abc03b1ee5_l.jpg?source=8673f162'
author: 知乎
comments: false
date: 2022-01-13 05:12:08
thumbnail: 'https://pic2.zhimg.com/v2-86ea4b8b7df16d9c219613abc03b1ee5_l.jpg?source=8673f162'
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
<img class="avatar" src="https://pic2.zhimg.com/v2-86ea4b8b7df16d9c219613abc03b1ee5_l.jpg?source=8673f162" referrerpolicy="no-referrer">
<span class="author">老狼，</span><span class="bio">UEFI固件、服务器、嵌入式产品(公众号:UEFIblog)</span>
<a href="https://www.zhihu.com/question/305248464/answer/556858281" class="originUrl" hidden>查看知乎原文</a>
</strong>

<div class="content">
<p>先说结论，这样做是为了更加省电。现在 CPU 内核的频率控制由一个叫做 PCU（Package Control Unit）的微处理器来控制。PCU 从 Nehalem CPU 开始就嵌入在 CPU 的封装中。</p>
<p>PCU 控制内核频率本着省电和提高响应度来进行调节。完成一项工作，为了节省能耗，是不是就是低频慢慢干就好了呢？答案是否定的。我们排除浪费时间等因素，只从能耗上考量，如果我们衡量干完某件事需要消耗的整体能量，实际上有两种策略：</p>
<ol>
<li>保持固定频率，将事情干完，然后 CPU 进入休息状态。</li>
<li>加速干事情，忍受短时功耗上升，尽快干完事情，尽早让 CPU 休息。</li>
</ol>
<p>这和人一样，有些人是慢性子，徐徐图之；而有些人性子急，希望早干完早休息。很难判断哪种好，这就需要量化分析了，好在 Intel 的工程师已经为我们找到这个平衡点：</p>
<figure><img class="content-image" src="https://pica.zhimg.com/v2-d6d4ba4c81efcc37b68ed8649f92bb64_720w.jpg?source=8673f162" alt referrerpolicy="no-referrer"></figure>
<p>在这个平衡点附近，按照工作量（workload demand）被分成 Low Range 和 High Range，PCU 采取两种策略。</p>
<figure><img class="content-image" src="https://pic3.zhimg.com/v2-8c10f45a1221ed21273c3e75336b67c9_720w.jpg?source=8673f162" alt referrerpolicy="no-referrer"><figcaption>策略一</figcaption></figure>
<p>在 Low Range 的区间，CPU 的主频低于 Pe 就没有任何意义了，PCU 总是让内核工作在 Pe 频率上，尽快干完事，进入休眠状态（CState）。这就是有时计算机比较清闲，我们打开任务管理器时，会发现有些 CPU 既不是工作在最低主频上，也不是工作最高主频上的原因。</p>
<figure><img class="content-image" src="https://pic1.zhimg.com/v2-afafb3f0688e2f214980feaffbc4ad99_720w.jpg?source=8673f162" alt referrerpolicy="no-referrer"></figure>
<p>在 High Range 中，提高内核频率尽管可以让任务完成的更快，但是因为能耗和频率 f 是 3 次方的关系，对能耗比来说并不合算。这就需要操作系统来提示支持 Speed Shift 的 PCU，采取激进的高频高功耗模式，来提供更好的相应；还是保守的能耗优先模式。</p>
<p><strong>结论</strong></p>
<p>为什么低负载还高频呢，就是因为负载落在 low Range 中，内核会被加速到 Pe 来尽快完成，从而尽快进入省电的 Cstate，即省电，有快速响应，何乐而不为呢？</p>
</div>
</div>


<div class="view-more"><a href="https://www.zhihu.com/question/305248464">查看知乎讨论<span class="js-question-holder"></span></a></div>

</div>


</div>
</div></div>  
</div>
            