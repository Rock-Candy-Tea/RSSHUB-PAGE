
---
title: 'JavaScript 性能优化'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=6863'
author: 掘金
comments: false
date: Sat, 17 Jul 2021 22:39:56 GMT
thumbnail: 'https://picsum.photos/400/300?random=6863'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h3 data-id="heading-0">1. 内存管理</h3>
<h4 data-id="heading-1">1.1、什么是内存</h4>
<pre><code class="copyable"> 由可读写单元组成，表示一篇可操作空间。 
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-2">1.2、 管理</h4>
<pre><code class="copyable"> 人为的去操作一片内存的申请、使用和释放。 
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-3">1.3、内存管理</h4>
<pre><code class="copyable"> 开发者主动申请空间、使用空间和释放空间。 
 
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-4">2. GC</h3>
<h4 data-id="heading-5">2.1 GC 的定义与作用</h4>
<ol>
<li>GC 就是垃圾回收机制的简写</li>
<li>GC 可以找到内存中的垃圾，并释放和回收空间</li>
</ol>
<h4 data-id="heading-6">2.2 GC 里的垃圾是什么</h4>
<ol>
<li>程序中不再需要使用的对象</li>
<li>程序中不再能访问到的对象</li>
</ol>
<h4 data-id="heading-7">3. GC 算法是什么</h4>
<ol>
<li>GC 是一种机制，垃圾回收器完成具体的工作</li>
<li>工作内容就是查找垃圾释放空间，回收空间</li>
<li>算法就是工作时查找和回收所遵循的规则</li>
</ol>
<h4 data-id="heading-8">4. 常见的 GC 算法</h4>
<h5 data-id="heading-9">1. 引用计数</h5>
<p><strong>核心思想：</strong></p>
<p>-设置引用数，判断当前引用数是否为 0
-引用关系改变时修改引用数字
-引用数字为 0 时立即回收</p>
<p><strong>引用计数算法的优点：</strong></p>
<ol>
<li>发现垃圾时立即回收</li>
<li>最大程度减少程序暂停</li>
</ol>
<p><strong>引用计数算法的缺点：</strong></p>
<ol>
<li>无法回收循环引用的对象</li>
<li>时间开销大</li>
</ol>
<h5 data-id="heading-10">2. 标记清除</h5>
<p><strong>核心思想：</strong></p>
<ul>
<li>分标记和清除两个阶段完成</li>
<li>遍历所有对象找标记活动对象</li>
<li>遍历所有对象清除没有标记对象</li>
<li>回收相应空间</li>
</ul>
<p><strong>标记清除算法的优点：</strong></p>
<ol>
<li>可以解决循环引用的对象的回收</li>
</ol>
<p><strong>标记清除算法的缺点：</strong></p>
<ol>
<li>会导致回收的空间的碎片化</li>
<li>不会立即回收垃圾对象</li>
</ol>
<h5 data-id="heading-11">3. 标记整理</h5>
<p>标记整理可以看作是标记清除的增强</p>
<p>标记阶段的操作和标记清除一致</p>
<p>清除阶段会先执行整理，移动对象位置</p>
<p><strong>标记清除算法的优点：</strong></p>
<ol>
<li>减少碎片化空间</li>
</ol>
<p><strong>标记清除算法的缺点：</strong></p>
<ol>
<li>不会立即回收垃圾对象</li>
<li>移动对象位置，回收效率慢</li>
</ol>
<h5 data-id="heading-12">4. 分代回收</h5>
<h3 data-id="heading-13">5.认识 V8</h3>
<p>V8 是一款主流的 JavaScript 执行引擎，目前常见的 Chrome 浏览器和 NodeJs 平台都在使用。</p>
<p>V8 采用即时编译，之前的 JavaScript 执行引擎先把 JavaScript 源代码转为字节码然后再执行，而 V8 把代码转为可以直接执行的机器码，所以速度是非常快的。</p>
<p>V8 内存设有上线，在 64 位操作系统上，这个上限不超过 1.5G, 在 32 位操作系统上，这个上限不超过 800MB,该大小对于网页应用来说足够使用了，而且对于垃圾回收机制 1.5G 的垃圾，V8 引擎采用增量标记的算法去处理需要消耗50ms， 如果采用非增量标记的方式去回收需要 1s， 1s 对用户体验来说已经是很长的时间了。</p>
<h4 data-id="heading-14">V8 垃圾回收策略</h4>
<p>采用分代回收的思想：内存分为新生代、老生代，再分别对其采用不同的垃圾回收算法。</p>
<p>V8 中常用的 GC 算法：</p>
<ul>
<li>分代回收</li>
<li>空间复制</li>
<li>标记清除</li>
<li>标记整理</li>
<li>标记增量</li>
</ul>
<p><strong>分代回收算法详解：</strong></p>
<p>V8 内存空间一分为二，小空间用于存储新生代对象（64 位操作系统分配 32M，32 位操作系统分配 16M），大空间用于存储老生代对象（64 位操作系统分配 1.4G，32 位操作系统分配 700G）。</p>
<p><strong>新生代对象回收实现</strong>：（新生代指的是存活时间较短的对象 ）</p>
<p>回收过程采用复制算法、标记整理。
新生代内存区分为两个等大小空间，使用空间位 From，空闲空间位 To。活动对象储存于 From 空间，标记整理后将活动对象拷贝至 To，From 与 To 交换空间完成释放。</p>
<p><em>回收细节说明：</em>
<em>拷贝过程中可能出现晋升，将新生代对象移动至老生代。</em>
<em>一轮 GC 还存活的新生代需要晋升，</em>
<em>To 空间的使用率超过 25%</em></p>
<p><strong>老生代对象回收实现：</strong></p>
<p>主要采用标记清除、标记整理、标记增量算法。
首先使用标记清除算法完成垃圾空间回收
当需要将新生代对象移动至老生代存储区的时候，并且老生代存储区不足以存储新生代对象的时候，将采用标记整理进行空间优化。
标记增量算法把一次垃圾回收操作分成多次去执行，每次循环并标记不能的层级，全部标记完成后再进行清除，减少了程序等待的时间。</p>
<p>新生代垃圾回收算法与老生代垃圾回收算法比较：
新生代区域垃圾回收使用空间换时间。
老生区域垃圾回收不适合复制算法。因为空间较大，会导致大量空间浪费。</p></div>  
</div>
            