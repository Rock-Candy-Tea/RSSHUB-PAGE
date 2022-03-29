
---
title: 'CPU 的指令集存放在什么地方？'
categories: 
 - 社交媒体
 - 知乎
 - 知乎日报
headimg: 'https://pic1.zhimg.com/v2-c085855ea40ccfdb3e70ee7bad672171_l.jpg?source=8673f162'
author: 知乎
comments: false
date: 2022-03-29 00:43:13
thumbnail: 'https://pic1.zhimg.com/v2-c085855ea40ccfdb3e70ee7bad672171_l.jpg?source=8673f162'
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
<img class="avatar" src="https://pic1.zhimg.com/v2-c085855ea40ccfdb3e70ee7bad672171_l.jpg?source=8673f162" referrerpolicy="no-referrer">
<span class="author">温戈，</span><span class="bio">想当作家的 数字芯片设计工程师</span>
<a href="https://www.zhihu.com/question/20793038/answer/2411664069" class="originUrl" hidden>查看知乎原文</a>
</strong>

<div class="content">
<p>首先，指令集不是具象化物体，不会放在 CPU 物理结构的某个地方。也不是数据，可以存在缓存、存储器或者寄存器阵列中。</p>
<p>指令集是 CPU 中用来计算、存储、控制计算机系统的一套指令的集合。指令集可以认为是计算机软件和硬件之间的接口，是软件如何控制硬件的计算机抽象模型的一部分。在 CPU 架构设计的开始，就要进行指令集的设计，因为<strong>指令集决定了 CPU 能够做什么以及如何做。</strong></p>
<p>不仅如此，指令集也定义了 CPU 支持的数据类型、寄存器、硬件如何管理主内存、关键特性（如虚拟内存）等。</p>
<figure><img class="content-image" src="https://pic2.zhimg.com/v2-9e30c39a96e952d0284f834c85a59cda_720w.jpg?source=8673f162" alt referrerpolicy="no-referrer"></figure>
<p>举个不太恰当的例子，我想从上海去北京，可以把上海去北京的任务看成 CPU 中一个指令集或者多个指令集才能完成的任务，那么不同的指令集效率也不同。</p>
<p>X86 指令集在执行上海到北京的任务时，方式是坐飞机，ARM 指令集则是坐火车，不同任务在不同的指令集下执行效率是不一样的，此时 X86 可能更快些。但如果任务换成做一顿丰盛的大餐，可能 ARM 更快一些。</p>
<p>比如此时我设计了一套非常牛逼的指令集，就叫 NB 指令集吧，它执行上海到北京的任务的方式是「闪现」，那么效率就碾压 X86 和 ARM，我将走向人生巅峰。</p>
<p>与此同时，我的一位同事也设计了另一套指令集，简称 FW 指令集。但这套指令集从北京到上海采用的方式是“疾跑”，结果不仅效率差，还异常耗电，没有多久这个 CPU 就挂了，几个月后，我这个同事就被裁了。</p>
<p>还有，我的另一位同事也设计了一套指令集，简称 LJ 指令集，这套指令集非常失败，无法实现上海到北京的任务，因为他没去过北京也不知道北京怎么走，结果被老板边缘化，半年后就去投奔前一个被裁的同事去了。<strong>因为那个被裁的同事在新公司拿了 double 的薪资。</strong></p>
<p><strong>所以回过头来看，坐飞机、乘高铁、用闪现、疾跑，以及去不了北京这些方式存在什么地方吗？并没有，但是要实现这些方式，你得有飞机、机场、高铁、车站、飞毛腿等设施，而这些设施的本质，就是 CPU 的晶体管电路本身。</strong></p>
</div>
</div>


<div class="view-more"><a href="https://www.zhihu.com/question/20793038">查看知乎讨论<span class="js-question-holder"></span></a></div>

</div>


</div>
</div></div>  
</div>
            