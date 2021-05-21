
---
title: 'Node系列 — v8引擎堆内存(二) 垃圾回收机制'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/f4a4d4d71a8348e0a8ea16f29a393668~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Thu, 20 May 2021 18:42:21 GMT
thumbnail: 'https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/f4a4d4d71a8348e0a8ea16f29a393668~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p><a href="https://juejin.cn/post/6963170647207837710" target="_blank">Node系列 — v8引擎堆内存详解（一）</a></p>
<h4 data-id="heading-0">看完本文你将学到什么</h4>
<ul class="contains-task-list">
<li class="task-list-item"><input type="checkbox" checked disabled> v8 堆内存分代机制</li>
<li class="task-list-item"><input type="checkbox" checked disabled> 分代晋升机制</li>
<li class="task-list-item"><input type="checkbox" checked disabled> 垃圾回收机制，涉及算法说明及其比较</li>
</ul>
<h4 data-id="heading-1">了解堆内存及垃圾回收的意义</h4>
<p>V8 对内存的限制对于浏览器而言，每个浏览器选项卡会实例化一个 V8 实例，用户选项卡使用周期也不长，内存一般绰绰有余，如果存在内存泄露问题，有一定的缓冲时间。但对于 Node 服务器端而言，生命周期很长，服务的稳定性及其重要，如果存在内存问题，会影响服务的正常运行。V8 的垃圾回收机制是会让 js 线程“全停顿”的，所以垃圾回收也是影响性能的重要因素之一。</p>
<h4 data-id="heading-2">v8的内存分代</h4>
<p>v8 中主要将内存分为两块空间：</p>
<ul>
<li><strong>新生代空间</strong>（存放生命周期短的对象）</li>
<li><strong>老生代空间</strong>（存放生命周期长的对象）</li>
</ul>
<p>如图：
<img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/f4a4d4d71a8348e0a8ea16f29a393668~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>前面我们提到的 <code>--max-old-space-size</code> 和<code>--max-new-space-size</code> 两个参数就是分别设置这两块空间的最大值。</p>
<blockquote>
<p>《深入浅出Nodejs》中指出：
<strong>老生代</strong> 内存空间最大值在64位系统和32位系统上分别为 1400MB 和 700MB,
<strong>新生代</strong> 内存空间最大值在64位系统和32位系统上分别为 32MB 和 16MB。</p>
</blockquote>
<p>由此可以解释 v8内存：
老生代 1.4G = (1400MB + 32MB) / 1024MB。
新生代 0.7G = (700MB + 16MB) /1024MB。
至于目前这块内存默认设置是多少，大家有兴趣可以去调查一下😊</p>
<h4 data-id="heading-3">垃圾回收机制</h4>
<p><code>Javascript</code> 具有自动垃圾回收机制，不像 <code>C</code> 和 <code>C++</code> 之类的语言，需要开发者手动跟踪内存情况并进行垃圾回收♻️，这也是很多 <code>javascript</code> 开发者没有关注这一块根本原因。
V8 中的垃圾回收策略重要是基于分代机制。因为在实际生产中，堆内存中对象的生命周期长短不一，如果定期的标记清除，会对生命周期比较长的对象重复处理，垃圾回收的过程 js 线程会暂停执行，导致程序运行性能大大降低。V8 设计者结合统计学对堆内的对象进行生命周期分类，在结合相应的算法处理，对新生代和老生代分别有一套处理机制。</p>
<h4 data-id="heading-4">新生代垃圾回收</h4>
<h5 data-id="heading-5">Scavenge 算法</h5>
<p>新生代中主要通过 <strong>Scavenge</strong> 算法进行垃圾回收，具体实现采用了 <strong>Cheney</strong> 算法。
<strong>Cheney</strong> 算法将一块内存一分为二，一块处于使用状态（称为 <strong>From</strong> 空间）,另一块处于闲置状态（称为 <strong>To</strong> 空间），当我们 js 线程执行要开始分配对象时，会首先在 <strong>From</strong> 空间分配。开始一轮垃圾回收时，先检查 <strong>From</strong> 中存活的对象然后复制到 <strong>To</strong> 中，接着释放 <strong>From</strong> 中的占用的空间，复制完成后，<strong>From</strong> 和 <strong>To</strong> 所代表的空间发生互换。</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/49cf98de488c47a696b44a81e351f7c8~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer">
<strong>Scavenge</strong> 算法</p>
<ul>
<li>缺点：内存空间只能使用一半</li>
<li>优点：效率特别高</li>
</ul>
<p>典型的拿空间换时间，这也就限制了该算法不能在全局的垃圾回收中使用。因为新生代生命周期短，该算法就很适合。</p>
<p>那这里有个问题，随着一轮又一轮回收，生命周期很长的对象就一直待在新生代空间🧐，新生代空间不就越来越小？？</p>
<h5 data-id="heading-6">晋升机制</h5>
<p>晋升的意义：就是将新生代中达到一定标准的对象移动到老生代空间中，给新生代腾出空间。
晋升的条件主要有两个：</p>
<ol>
<li><strong>对象是否经历过 Scavenge 回收</strong>；</li>
<li><strong>To 空间的占用大小是否超过 25%</strong>；</li>
</ol>
<p>晋升的过程：在执行一次新生代垃圾回收，将存活对象从 <strong>From</strong> 空间复制到 <strong>To</strong> 空间的时候，会检查该对象是否经历过一次 <strong>Scavenge</strong> 回收，如果经历过，则将该对象从 <strong>From</strong> 空间复制到老生代空间，如果没有，则复制到 <strong>To</strong> 空间。  另一个判断条件，当从 <strong>From</strong> 空间复制对象到 <strong>To</strong> 空间时，如果当前 <strong>To</strong> 空间的使用比例达到 25%，则直接将该对象复制到老生代空间。</p>
<h4 data-id="heading-7">老生代垃圾回收</h4>
<p>老生代中垃圾回收主要涉及两个算法 <strong>Mark-Sweep</strong> 和 <strong>Mark-Compact</strong>。
为什么不采用 <strong>Scavenge</strong> 算法呢🧐 ？主要有两点：</p>
<ol>
<li>老生代中大部分是活着的对象，复制大量活着的对象影响回收性能。</li>
<li>老生代中需要划分一半的空间实现 <strong>Scavenge</strong> 算法机制，浪费空间。</li>
</ol>
<h5 data-id="heading-8">Mark-sweep 算法</h5>
<p><strong>Mark-sweep</strong> 算法（标记-清除）会先标记内存中活着的对象，然后清除没有被标记的对象。</p>
<p>标记后如图所示：
<img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/4bd09d9970f34f648abb015eaf7e35d8~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>清除后如图所示：
<img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/00195c42a6594ab1a3b93606a3ce7416~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p><strong>Mark-sweep</strong> 算法存在一个问题，当清理完死对象后，会存在内存空隙，也就是说内存的状态是不连续的。这时如果分配一个比较大对象到内存，而且各空隙不足以分配，会导致提前触发垃圾回收，这样的垃圾回收是没有必要的。所以这种情况下，就需要 <strong>Mark-Compact</strong> 算法。</p>
<h5 data-id="heading-9">Mark-Compact 算法</h5>
<p><strong>Mark-Compact</strong> 算法（标记-整理）会先标记内存中死亡的对象，然后往一端移动活着的对象，移动完成后，清理掉边界外的内存。</p>
<p>标记移动如图所示：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/77e0bd77196442f7977fc9dfa659ed90~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>清理完如图所示：
移动完成后，清理掉边界外的内存</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/d906ee10df51431cafff5887db9a6763~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>在 v8 中，对于这两种算法是灵活使用的，当可用最大片段空间不足以分配晋升对象时才使用 Mark-Compact 算法。</p>
<h4 data-id="heading-10">算法比较</h4>





























<table><thead><tr><th align="left">回收算法</th><th><strong>Mark-Sweep</strong></th><th><strong>Mark-Compact</strong></th><th><strong>Scavenge</strong></th></tr></thead><tbody><tr><td align="left">速度</td><td>中等</td><td>最慢</td><td>最快</td></tr><tr><td align="left">空间开销</td><td>少（有碎片空间）</td><td>少（无碎片）</td><td>双倍空间（无碎片）</td></tr><tr><td align="left">是否移动对象</td><td>否</td><td>是</td><td>是</td></tr></tbody></table>
<h4 data-id="heading-11">垃圾回收执行策略</h4>
<p>由于垃圾回收过程中 js 线程会暂停执行，必须等回收完再恢复执行，这种行为被称为“全停顿”。V8 回收过程中，新生代存活对象少，而且内存空间不大，回收基本不影响，而在老生代中存活对象多，而且内存空间大，标记、移动、清理过程将损耗较多时间。V8 在面临这种问题做出进步一改善，在标记阶段的动作从全局标记改为增量标记（<strong>incremental marking</strong>）,将标记动作分为很多小步，每完成一步清理，就恢复 js 应用执行，如此交替，直到标记完成。</p>
<h4 data-id="heading-12">总结</h4>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/d88ab2b515c34820958407fa05652891~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>内存泄露是前端开发工程师经常提到的，了解 V8 堆内存及垃圾回收，能让我们理解其内存大小的合理限制，以及内存状态对于我们日常开发的重要性，也能让我们在高性能的代码成长上迈出重要的一步。</p></div>  
</div>
            