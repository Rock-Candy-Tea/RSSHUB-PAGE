
---
title: '再谈HotSpot JVM GC机制中的写屏障'
categories: 
 - 社交媒体
 - 简书
 - 首页
headimg: 'https://upload-images.jianshu.io/upload_images/195230-645f12fb05723f18.png'
author: 简书
comments: false
date: Invalid Date
thumbnail: 'https://upload-images.jianshu.io/upload_images/195230-645f12fb05723f18.png'
---

<div>   
<h3>前言</h3>
<p>在比较久之前的一篇文章<a href="https://www.jianshu.com/p/da5717e5b5ad" target="_blank">《再谈JVM里的记忆集合》</a>中，笔者曾经写了这么一段话：</p>
<blockquote>
<p>HotSpot通过写屏障（write barrier）来维护卡表。<del>我们已经知道，内存屏障的主要作用是防止指令重排序，它也是volatile关键字的基础。有了写屏障，JVM就可以保证引用发生改变时，对卡表中的卡做标记与访问内存的顺序不发生变化。</del>在CardTableRS初始化时，所做的第一件事就是创建卡表需要的屏障集合（barrier set）……</p>
</blockquote>
<p>为什么划掉了呢？（原文也已经划掉了）</p>
<p>在上文中，笔者犯了一个原则性的低级错误，即把Java内存模型中的内存屏障/内存栅栏（memory barrier/fence）与HotSpot GC机制中的写屏障（write barrier）混为一谈了，但这两者实际上毫无关系。Doug Lea大佬也在<a href="https://links.jianshu.com/go?to=http%3A%2F%2Fgee.cs.oswego.edu%2Fdl%2Fjmm%2Fcookbook.html" target="_blank">《JSR-133 Cookbook for Compiler Writers》</a>一文中明确指出：</p>
<blockquote>
<p>Memory barriers are unrelated to the kinds of "write barriers" used in some garbage collectors.</p>
</blockquote>
<p>带来困扰，十分抱歉。</p>
<p>写屏障是个有些复杂的话题，准确来说，它在GC中的应用也有不止一处。下面先纠正错误，简单解释写屏障的概念，及其与卡表的关系。</p>
<h3>写屏障与卡表</h3>
<p>“写屏障”这个词虽然看起来高深，但是它的含义却相当naive——就是<strong>对一个对象引用进行写操作（即引用赋值）之前或之后附加执行的逻辑</strong>，相当于为引用赋值挂上的一小段钩子代码。</p>
<p>前文所述“HotSpot通过写屏障来维护卡表”，写屏障就是在将引用赋值写入内存之前，先做一步mark card——即将出现跨代引用的内存块对应的卡页置为dirty，如下图所示。</p>
<div class="image-package">
<div class="image-container">
<div class="image-container-fill"></div>
<div class="image-view" data-width="512" data-height="386"><img data-original-src="//upload-images.jianshu.io/upload_images/195230-645f12fb05723f18.png" data-original-width="512" data-original-height="386" data-original-format="image/png" data-original-filesize="131998" src="https://upload-images.jianshu.io/upload_images/195230-645f12fb05723f18.png" referrerpolicy="no-referrer"></div>
</div>
<div class="image-caption"></div>
</div>
<p>而之前提到过的JVM参数<code>-XX:+UseCondCardMark</code>，就是开启有条件的写屏障：在将卡页置为dirty之前，先检查它是否已经为dirty状态，如果已经是了，就不必再执行mark card动作，以避免虚共享。</p>
<p>写屏障除了用于维护卡表之外，在并行GC（如CMS、G1）中的并发标记阶段还有一个更重要的用途。下面以CMS垃圾收集器为例简单解说。</p>
<h3>并行GC中并发标记的漏标隐患</h3>
<p>我们已经知道，CMS垃圾收集器的执行分为以下6个阶段：</p>
<ol>
<li>初始标记</li>
<li>并发标记</li>
<li>并发预清理</li>
<li>重新标记</li>
<li>并发清理</li>
<li>并发重置</li>
</ol>
<p>其中，只有不带“并发”字眼的初始标记、重新标记两个阶段是stop-the-world的，其他4个阶段都是与用户线程（GC界的术语称作mutator）并行的，这符合CMS收集器追求最少STW时间与最高响应度的宗旨。</p>
<p>初始标记和并发标记阶段就是进行可达性分析。CMS的根搜索机制是深度优先的<a href="https://links.jianshu.com/go?to=https%3A%2F%2Fen.wikipedia.org%2Fwiki%2FTracing_garbage_collection%23Tri-color_marking" target="_blank">三色标记（tri-color marking）算法</a>，属于基础知识，不再展开讲了。</p>
<p>初始标记阶段会只遍历GC Roots直接可达的那些对象，并压入标记栈（mark stack）；并发标记阶段会逐一从标记栈中弹出对象，然后不断递归标记它们直接引用的对象，重复压入-弹出过程，直到标记栈为空。</p>
<p>在并发标记阶段，难点在于：用户线程并未停止，仍然在改变对象的引用关系。这有可能造成原本活动的对象被漏标，进而破坏GC的正确性。示例如下图所示。</p>
<div class="image-package">
<div class="image-container">
<div class="image-container-fill"></div>
<div class="image-view" data-width="1864" data-height="612"><img data-original-src="//upload-images.jianshu.io/upload_images/195230-4764bb7dd62e384d.png" data-original-width="1864" data-original-height="612" data-original-format="image/png" data-original-filesize="175028" src="https://upload-images.jianshu.io/upload_images/195230-4764bb7dd62e384d.png" referrerpolicy="no-referrer"></div>
</div>
<div class="image-caption"></div>
</div>
<p>(a) 搜索对象A的直接子对象，标记对象B为可达（灰色），并将B压入标记栈。此时A的直接子对象搜索完毕，标记为存活（黑色），将A弹出标记栈；</p>
<p>(b) (c) 与此同时，用户线程改变引用，让A引用C，并移除掉B对C的引用；</p>
<p>(c) 结果：无法再由B标记到C，但也无法由A标记到C（因为A已经出栈）。C虽然仍为活动对象，但被错判为非活动（白色）对象而被回收。显然这是无法容忍的。</p>
<p>事实上，不止是CMS，在其他任何并行的垃圾回收器中，都有对象漏标的隐患。Wilson指出，出现漏标的充要条件是以下两个情况同时发生：</p>
<ol>
<li>mutator使黑色对象直接引用了白色对象；</li>
<li>mutator删除了从灰色对象到白色对象之间的所有引用路径。</li>
</ol>
<h3>强三色不变式与增量更新写屏障</h3>
<p>为了解决漏标问题，需要破坏上文所述的两个情况，亦即强制回收器满足如下两个条件之一。</p>
<ul>
<li>
<strong>强三色不变式</strong>：保证永远不会存在黑色对象到白色对象的引用（破坏情况1）。</li>
<li>
<strong>弱三色不变式</strong>：所有被黑色对象引用的白色对象都处于灰色保护状态，即直接或间接从灰色对象可达（破坏情况2）。</li>
</ul>
<p>强/弱三色不变式都可以通过屏障技术来实现，并且在不同环境下有多种不同的屏障技术。CMS收集器采用增量更新（incremental update）写屏障实现强三色不变式，具体来讲，是Dijkstra等人提出的Dijkstra写屏障，其逻辑是：</p>
<blockquote>
<p><strong>拦截使黑色对象引用指向白色对象的mutate操作，强制被引用指向的白色对象置为灰色状态，并将其压入标记栈。</strong></p>
</blockquote>
<p>Dijkstra写屏障的逻辑用伪码表示如下。</p>
<pre><code class="js">write_barrier(obj, field, newobj) &#123;
  if(newobj.mark == FALSE) &#123;
    newobj.mark = TRUE
    push(newobj, $mark_stack)
  &#125;
  *field = newobj
&#125;
</code></pre>
<p>可见，之所以名为“增量更新”，是指写屏障会持续hook引用的插入和变更。下图示出了加入增量更新写屏障后，并发标记阶段引用发生更改的情况，可见对象C可以安全地存活了。</p>
<div class="image-package">
<div class="image-container">
<div class="image-container-fill"></div>
<div class="image-view" data-width="2034" data-height="690"><img data-original-src="//upload-images.jianshu.io/upload_images/195230-d1901b96a71f7196.png" data-original-width="2034" data-original-height="690" data-original-format="image/png" data-original-filesize="216515" src="https://upload-images.jianshu.io/upload_images/195230-d1901b96a71f7196.png" referrerpolicy="no-referrer"></div>
</div>
<div class="image-caption"></div>
</div>
<p>但是，增量更新写屏障无法探知堆外（如栈上）GC Roots的引用变化，所以CMS收集器在并发标记和预清理完成后，还得做一次重新标记，即再做一次根搜索。</p>
<h3>The End</h3>
<p>G1的解决思路与CMS又有不同，是采用了初始快照（snapshot-at-the-beginning, SATB）写屏障实现了弱三色不变式。G1垃圾收集器非常复杂，应该择日好好总结一下，今天就不提了。</p>
<p>明天早起搬砖，民那晚安。</p>
  
</div>
            