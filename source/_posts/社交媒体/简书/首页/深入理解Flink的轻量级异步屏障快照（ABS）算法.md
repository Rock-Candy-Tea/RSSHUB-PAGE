
---
title: '深入理解Flink的轻量级异步屏障快照（ABS）算法'
categories: 
 - 社交媒体
 - 简书
 - 首页
headimg: 'https://upload-images.jianshu.io/upload_images/195230-09206a9033c14d18.png'
author: 简书
comments: false
date: Invalid Date
thumbnail: 'https://upload-images.jianshu.io/upload_images/195230-09206a9033c14d18.png'
---

<div>   
<h3>Prologue</h3>
<p>在很久之前，笔者曾简单介绍了<a href="https://www.jianshu.com/p/06fff1ffe0a7" target="_blank">Chandy-Lamport</a>分布式快照算法，如果看官还未读过，建议作为前置知识补充一下。</p>
<p>用过Flink的人都会知道检查点机制有多重要，而Flink做checkpoint的过程正是依赖于Chandy-Lamport算法的变种——<strong>异步屏障快照（asynchronous barrier snapshotting, ABS）算法</strong>。该算法由五位大佬通过论文<a href="https://links.jianshu.com/go?to=https%3A%2F%2Farxiv.org%2Fpdf%2F1506.08603.pdf" target="_blank">《Lightweight Asynchronous Snapshots for Distributed Dataflows》</a>提出。可以说，理解了ABS，就真正理解了Flink检查点背后的原理。本文来谈谈它。</p>
<h3>Checkpoint & Snapshot</h3>
<p>检查点是Flink为流计算过程提供的容错和故障恢复机制。当程序出错时，Flink会重启受到影响的那部分算子及计算逻辑，并将它们重置到最后一次成功checkpoint时的状态。每次成功的checkpoint产生的“状态数据”其实就是这个流式计算任务在那一时刻的快照。</p>
<p>Flink作业可以抽象成有向图表示，图的顶点是算子（operator），边是数据流（data stream），与Chandy-Lamport算法提出的“进程-链路”图模型恰好对应。直接套用C-L算法的思路，我们可以得出如下推论：</p>
<blockquote>
<ul>
<li>Flink作业的快照要包含两部分，即算子所处的状态以及数据流承载的数据。算子每收到/发出一条数据，以及数据流每流入/流出一条数据，都会造成全局状态的改变。</li>
<li>算子可以感知到自己的状态，但数据流的状态不容易记录，主要是因为承载的数据量太大，并且总是在变化。</li>
<li>时间是无法静止的（即数据总是在流动的），并且快照不能stop-the-world，否则会造成延迟和数据堆积，降低吞吐量。</li>
</ul>
</blockquote>
<p>所以解决方案的要点有二：一是<strong>通过每个算子自己记录的状态合并出全局快照</strong>，二是<strong>引入一个标记把数据流从时域上切分成段</strong>。下面就可以了解ABS算法的基础——屏障。</p>
<h3>Barrier</h3>
<p>之前已经讲过，C-L算法引入了marker消息来作为快照的边界，即区分“当前快照的数据”和“下一个快照的数据”。ABS算法也有自己的marker消息，不过称为检查点屏障（checkpoint barrier），简称屏障。</p>
<p>屏障由Flink的JobManager周期性产生（周期长度由<code>StreamExecutionEnvironment.enableCheckpointing()</code>方法来指定），并广播给所有Source算子，沿着数据流流动下去。下图示出一条带有屏障的数据流。</p>
<div class="image-package">
<div class="image-container">
<div class="image-container-fill"></div>
<div class="image-view" data-width="667" data-height="261"><img data-original-src="//upload-images.jianshu.io/upload_images/195230-09206a9033c14d18.png" data-original-width="667" data-original-height="261" data-original-format="image/png" data-original-filesize="19448" src="https://upload-images.jianshu.io/upload_images/195230-09206a9033c14d18.png" referrerpolicy="no-referrer"></div>
</div>
<div class="image-caption"></div>
</div>
<p>可见，第n - 1个屏障之后、第n个屏障之前的所有数据都属于第n个检查点。下游算子如果检测到屏障的存在，就会触发快照动作，不必再关心时间无法静止的问题。下面继续了解快照阶段是如何执行的。</p>
<h3>Snapshotting & Barrier Alignment</h3>
<p>举例说明检查点流程。下图是论文中给出的并行度为2的Word Count示例，注意该作业的执行计划为有向无环图（DAG）。</p>
<div class="image-package">
<div class="image-container">
<div class="image-container-fill"></div>
<div class="image-view" data-width="1162" data-height="283"><img data-original-src="//upload-images.jianshu.io/upload_images/195230-47fbcee019af584b.png" data-original-width="1162" data-original-height="283" data-original-format="image/png" data-original-filesize="127021" src="https://upload-images.jianshu.io/upload_images/195230-47fbcee019af584b.png" referrerpolicy="no-referrer"></div>
</div>
<div class="image-caption"></div>
</div>
<p>快照算法的步骤如下：</p>
<p>a) Source算子接收到JobManager产生的屏障，生成自己状态的快照（其中包含数据源对应的offset/position信息），并将屏障广播给下游所有数据流；</p>
<p>b)、c) 下游非Source的算子从它的某个输入数据流接收到屏障后，会阻塞这个输入流，继续接收其他输入流，直到所有输入流的屏障都到达（图中的count-2算子接收的两个屏障就不是同时到达的）。一旦算子收齐了所有屏障，它就会生成自己状态的快照，并继续将屏障广播给下游所有数据流；</p>
<p>d) 快照生成后，算子解除对输入流的阻塞，继续进行计算。Sink算子接收到屏障之后会向JobManager确认，所有Sink都确认收到屏障标记着这一周期checkpoint过程结束，快照成功。</p>
<p>可见，如果算子只有一个输入流的话，问题就比较简单，只需要在收到屏障之后立即做快照。但是如果有多个输入流，就必须要等待收到所有屏障才能做快照，以避免将检查点n与检查点n + 1的数据混淆。这个等待的过程就叫做对齐（alignment），图来自官方文档。注意算子内部有个输入缓冲区，用来在对齐期间缓存数据。</p>
<div class="image-package">
<div class="image-container">
<div class="image-container-fill"></div>
<div class="image-view" data-width="1099" data-height="215"><img data-original-src="//upload-images.jianshu.io/upload_images/195230-92e8464723804bc6.png" data-original-width="1099" data-original-height="215" data-original-format="image/png" data-original-filesize="60442" src="https://upload-images.jianshu.io/upload_images/195230-92e8464723804bc6.png" referrerpolicy="no-referrer"></div>
</div>
<div class="image-caption"></div>
</div>
<p>下图是从Flink系统的角度示出整个checkpoint流程里屏障的流动，以及快照数据向状态后端的写入。注意Source记录的offset值以及Sink收到所有屏障后的ack信号。</p>
<div class="image-package">
<div class="image-container">
<div class="image-container-fill"></div>
<div class="image-view" data-width="1285" data-height="464"><img data-original-src="//upload-images.jianshu.io/upload_images/195230-281f4ec10fd1f5af.png" data-original-width="1285" data-original-height="464" data-original-format="image/png" data-original-filesize="162543" src="https://upload-images.jianshu.io/upload_images/195230-281f4ec10fd1f5af.png" referrerpolicy="no-referrer"></div>
</div>
<div class="image-caption"></div>
</div>
<h3>Exactly-Once vs At-Least-Once</h3>
<p>上面讲到的屏障对齐过程是Flink exactly-once语义的基础，因为屏障对齐能够保证多输入流的算子正常处理不同checkpoint区间的数据，避免它们发生交叉，即不会有数据被处理两次。</p>
<p>但是对齐过程需要时间，有一些对延迟特别敏感的应用可能对准确性的要求没有那么高。所以Flink也允许在<code>StreamExecutionEnvironment.enableCheckpointing()</code>方法里指定At-Least-Once语义，会取消屏障对齐，即算子收到第一个输入的屏障之后不会阻塞，而是触发快照。这样一来，部分属于检查点n + 1的数据也会包括进检查点n的数据里， 当恢复时，这部分交叉的数据就会被重复处理。</p>
<h3>Asynchronous</h3>
<p>“屏障”和“快照”都讲过了，“异步”呢？这个词实际上指的是快照数据写入的异步性：算子收齐屏障并触发快照之后，不会等待快照数据全部写入状态后端，而是一边后台写入，一边立刻继续处理数据流，并将屏障发送到下游，实现了最小化延迟。</p>
<p>当然，引入异步性之后，checkpoint成功的条件除了所有Sink都报告ack之外，还得加上一条：所有有状态的算子都报告ack，否则JobManager就无法确认异步写入到底完成没有。</p>
<h3>DCG？</h3>
<p>ABS的精华讲完了。最后看论文中提到的特殊情况，即作业的执行计划是个有向有环图（DCG）。很显然这种情况会造成死锁，环内的算子就会无限等待收齐屏障。面对该问题，ABS算法会单独处理回边（back edge）——即从下游流回上游的数据流，因为回边的存在会导致我们无法单纯地通过每个算子的状态合并出全局快照。</p>
<p>思路如下图所示，重点在于回边终点的那个算子。当该算子的非回边输入流的屏障都到达之后，它会生成一个本地的快照备份，并于此同时开始记录回边流入的数据，直到再次从回边收到相同的屏障。这样就靠算子的状态记录了回边的状态，当从快照恢复时，能够将回边的数据重新放回数据流传输。</p>
<div class="image-package">
<div class="image-container">
<div class="image-container-fill"></div>
<div class="image-view" data-width="1147" data-height="225"><img data-original-src="//upload-images.jianshu.io/upload_images/195230-36d1eef7ff7c1026.png" data-original-width="1147" data-original-height="225" data-original-format="image/png" data-original-filesize="78967" src="https://upload-images.jianshu.io/upload_images/195230-36d1eef7ff7c1026.png" referrerpolicy="no-referrer"></div>
</div>
<div class="image-caption"></div>
</div>
<h3>The End</h3>
<p>明天还有很多事，民那晚安晚安。</p>
  
</div>
            