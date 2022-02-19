
---
title: 'CPU 能靠提高单核的规模去提高单核性能么？'
categories: 
 - 社交媒体
 - 知乎
 - 知乎日报
headimg: 'https://pic2.zhimg.com/v2-80542abccf998d3e28fb986c23875088_l.jpg?source=8673f162'
author: 知乎
comments: false
date: 2022-02-19 11:08:28
thumbnail: 'https://pic2.zhimg.com/v2-80542abccf998d3e28fb986c23875088_l.jpg?source=8673f162'
---

<div>   
<div class="main-wrap content-wrap">
<div class="headline">

<div class="img-place-holder">



</div>

<div class="content-inner">




<div class="question">
CPU 能靠增大单核的规模去提高单核性能么？

<div class="answer">

<strong>
<img class="avatar" src="https://pic2.zhimg.com/v2-80542abccf998d3e28fb986c23875088_l.jpg?source=8673f162" referrerpolicy="no-referrer">
<span class="author">ArchShineZ，</span><span class="bio">寻找CPU架构建模的工作机会</span>
<a href="https://www.zhihu.com/question/514191573/answer/2341328052" class="originUrl" hidden>查看知乎原文</a>
</strong>

<div class="content">
<p>难得遇到我读博的细分领域的问题，简略回答一下：</p>
<p>题主说的增大规模，我们一般称为“Scaling-up”。Scaling-up 是<strong>可以</strong>提升性能的，但是有几个基础性的<strong>挑战</strong>。</p>
<p><strong>可以</strong>是指：不考虑功耗、频率的前提下，增加晶体管的数量是可以提高同频性能的。</p>
<p>挑战是大头。</p>
<p>首先，有一个最常见的、最容易理解的答案。因为 Dennard scaling 不复存在，同频率下，粗暴地增加规模会增加功耗。当然，以多核的方法增加规模，全核跑起来功耗也吃不消，所以这<strong>不是单核特有的问题</strong>。</p>
<p><strong>均衡——存乎万物之间</strong></p>
<p>对 CPU 单核而言，一个最根本的问题是：CPU 流水级从头到尾、层次结构从内到外必须达到一个均衡的状态，才能发挥各部分的性能潜力。这导致 CPU 无法像 GPU 那样通过堆流处理器来提升性能。</p>
<p>我打一个比方，CPU 如果单纯地堆发射宽度和运算单元，就会像七龙珠里面特南克斯在超赛一阶段膨胀肌肉一样，纸面数值上去了，但是还是被沙鲁吊打，因为身体的敏捷性拉胯了。</p>
<p>其实香山处理器的第一代架构就存在这样的问题，雁栖湖架构的发射宽度非常夸张，但是性能一般（SPEC06 ~7/GHz）。而香山处理器的第二代南湖架构在没怎么增加发射宽度的前提下，性能获得了显著的提升。其实就是拓宽了瓶颈部分，使之与高发射宽度更加匹配了。</p>
<p>那么哪些部分需要平衡呢？</p>
<p>我习惯把 CPU 的功能分为三部分：指令流、寄存器数据流、访存数据流。这三部分都是需要平衡的，与此同时这些部分还存在无法暴力 Scaling-up 的因素。</p>
<p>首先是定义：</p>
<ul>
<li>指令流：从取指到重命名，包括 I-Cache</li>
<li>寄存器数据流：分发、发射、执行、写回、提交</li>
<li>访存数据流：访存推测、LSU、Cache</li>
</ul>
<p><strong>指令流</strong></p>
<p>指令流这部分 Scaling-up 的需求是<strong>准确的、高带宽的、连续的</strong>指令供应。<strong>准确</strong>是指分支预测的准确率，分支预测要是不准，1024 的窗口、32 发射也白搭，不多说了。而且规模越大、in-flight 的指令越多，对准确率要求越高。</p>
<p><strong>准确性带来的挑战</strong>。TAGE 和 Perceptron 这类分支预测器要用 RAM 装 TAGE Table 和 NN 的权重，一般 RAM 越大 Hash 冲突越少。但是 RAM 越大面积也就越大，面积大到一定程度延迟就上去了，如果你在这里打拍了就会影响指令供应的连续性。</p>
<p><strong>高带宽带来的挑战</strong>。x86 有个特有的问题：指令变长，后一条指令的起始位置依赖于前一条指令的类型，这导致译码是一个串行的组合逻辑。RISC 基本可以并行译码，但是重命名的时候 RISC 和 x86 一样：后一条指令重命名（可能）依赖于前一条指令重命名的结果，这也是一条串行依赖路径。这些串行依赖路径的存在，导致你不能暴力 Scaling-up 译码宽度或者重命名宽度。</p>
<p><strong>寄存器数据流</strong></p>
<p>寄存器数据流是我从入学到现在都在关注的问题。根据<sup>[1]</sup> 和<sup>[2]</sup> 这两篇文章的结果，物理寄存器堆和发射队列的线延迟在先进工艺下会贡献主要的时延。我和工业界的前辈交流时，大家也说这些是典型的频率瓶颈。结果就是“<strong>Clock rate versus IPC</strong>”：我们如果肆无忌惮地增加物理寄存器堆和发射队列的大小或者读写口数量，即使同频性能上去了，处理器的频率也做不上去。</p>
<p>当然，两篇经典论文的年代非常久远，他们观察到的现象在今天是否是关键瓶颈，我也不笃定。尤其是在 Apple 的指令窗口做到了 600+ 项时，我对此愈发感到怀疑：一般指令窗口和物理寄存器堆、发射队列需要一起 Scaling-up 才能获得较好的收益。一种猜测是 Apple 在架构设计或者物理设计方面发现了什么黑科技吗？另一个猜测是：M1 反正只跑 3GHz，不像 Intel 要跑 5GHz，而 600 是在目前 TSMC 的工艺和 Apple 的物理能力下的极限？</p>
<p><strong>访存数据流</strong></p>
<p>首先是访存推测，它的性质和分支预测是类似的：如果经常推测错，流水线就填不满，再宽也白搭。</p>
<p>然后是 LSQ，尤其是 Store Queue，它和发射队列有类似的问题。</p>
<p>最头疼的是 Cache，包括 L2、L3。大家最熟悉的是<strong>Memory Wall</strong>问题，我就不展开了。还有一个问题就是 L1 的<strong>带宽</strong>问题：Scaling-up 的时候，每周期的访存指令数量越来越多，L1 DCache 如何在同一个周期响应更多的请求？分 bank？SRAM 的读写口数量跟得上吗？</p>
<p><strong>要大幅提高核的规模你需要提高什么？</strong></p>
<p>总结一下：</p>
<ul>
<li>更高的分支预测准确率和访存推测，你的敌人是 RAM 的面积</li>
<li>更大的指令供应带宽，你的敌人重命名的串行时延（和译码的串行时延（x86））</li>
<li>更大的 PRF、发射队列和 LSQ，你的敌人是 PRF 和 CAM 的线延迟</li>
<li>更少的 Cache miss，你可以暴力堆容量，也可以改进替换、预取算法</li>
<li>更大的 DCache 的带宽，你的敌人是 DCache 的时延要求</li>
</ul>
<p>以我目前的知识，能看到的就是这些</p>
<p> </p>
<p>Update：昨晚上写的时候，主要考虑的是 CPU 设计的挑战，但是忽略了一个同样重要的问题是程序本身的特性：有的程序本身就是“<strong>不进油盐</strong>”，任由你 CPU 怎么 scaling-up 都无法获得显著性能提升。</p>
<p>在指令流方面，有的程序就是无法预测的：例如一个分支是 if (rand(0, 1) > 0.5)，那么这个分支本身就无法预测。更难预测的是随机的间接跳转，例如 Zoo = List(Animals)，你遍历 Zoo：for animal in Zoo: animal.eat()，每个动物有不同的 eat 的实现，而且每个动物在 Zoo 里面是随机序，那么这个 eat 的实现的 PC 就非常难预测。对于无法预测的程序，指令窗口再大、宽度再宽，也只是“徒增功耗”。</p>
<p>在寄存器数据流方面，Scaling-up 指令窗口大小是为了在窗口内容纳更大的数据流图、挖掘更多的 ILP 机会。极端情况下，如果一个程序的每一条指令都依赖于上一条指令，那么窗口 100 和窗口 1000 不会带来性能改进。嘛，我的一个研究工作就是研究怎么 scaling-up 窗口，发现窗口不敏感的程序也不少……</p>
<p>在访存数据流方面也有类似的问题，有的应用的局部性就是很差、footprint 很大、难以预测，除非你的 SRAM 堆到 4G+，否则就是放不下。例如 SPECCPU 里面的 mcf 就有一点这种意思，但是似乎最先进的商业处理器在 mcf 上已经捞到一点油水，也就是说 mcf 不属于完全“油盐不进”的。</p>
</div>
</div>


<div class="view-more"><a href="https://www.zhihu.com/question/514191573">查看知乎讨论<span class="js-question-holder"></span></a></div>

</div>


</div>
</div></div>  
</div>
            