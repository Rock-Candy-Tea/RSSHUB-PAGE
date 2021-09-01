
---
title: '面试必备之JavaScript性能优化'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=6970'
author: 掘金
comments: false
date: Tue, 31 Aug 2021 05:08:08 GMT
thumbnail: 'https://picsum.photos/400/300?random=6970'
---

<div>   
<div class="markdown-body html cache"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p><strong>这是我参与8月更文挑战的第29天，活动详情查看：<a href="https://juejin.cn/post/6987962113788493831" title="https://juejin.cn/post/6987962113788493831" target="_blank">8月更文挑战</a></strong></p>
<h4 data-id="heading-0">性能优化</h4>
<ul>
<li>
<p>性能优化：</p>
<ul>
<li>性能优化是不可避免的</li>
<li>任何一个提高运行效率，降低运行成本的操作都是性能优化</li>
</ul>
</li>
<li>
<p>了解JavaScript语言本身上的优化</p>
<ul>
<li>内存管理</li>
<li>垃圾回收机制</li>
<li>从而编写高效的JavaScript代码</li>
</ul>
</li>
<li>
<p>从几个维度进行了解JavaScript本身的性能优化</p>
<ul>
<li>内存管理</li>
<li>垃圾回收与GC算法</li>
<li>v8引擎的垃圾回收</li>
<li>performance工具 查看监控内存</li>
<li>优化代码实例</li>
</ul>
</li>
<li>
<p>减少内存问题型代码</p>
</li>
</ul>
<h5 data-id="heading-1">内存管理介绍</h5>
<p>内存： 由可读写单元组成，表示一片可操作空间</p>
<p>管理：人为的去操作一片空间的申请、使用和释放</p>
<p>内存管理：开发者向内存申请空间、使用空间、释放空间</p>
<p>管理流程： 申请---使用---释放</p>
<ul>
<li>
<p>JavaScript中的内存管理</p>
<blockquote>
<p>找到垃圾，让js引擎去进行回收</p>
</blockquote>
</li>
</ul>
<p>由于JavaScript语言本身并没有提供相关申请内存空间、使用内存空间、释放内存空间的api，所以js不能向c/c++那样主动的去做内存相关的处理。</p>
<p>JavaScript中垃圾</p>
<ul>
<li>
<p>JavaScript中内存管理是自动的</p>
</li>
<li>
<p>对象不再引用时是垃圾</p>
</li>
<li>
<p>对象不能从根上访问到的是垃圾</p>
</li>
</ul>
<p>JavaScript中的可达对象</p>
<ul>
<li>
<p>可以访问到的对象就是可达对象（引用、作用域链）</p>
</li>
<li>
<p>可达的标准就是从根出发是否能够找到</p>
</li>
<li>
<p>JavaScript中的根就可以理解为是全局变量对象（全局执行上下文）</p>
</li>
</ul>
<p>GC定义与作用</p>
<ul>
<li>
<p>GC就是垃圾回收机制的简写</p>
<ul>
<li>
<p>gc里面的垃圾是什么？</p>
<ol>
<li>
<p>程序中不再需要使用的对象</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">fn</span>(<span class="hljs-params"></span>) </span>&#123;
  name = <span class="hljs-string">'lg'</span>
  <span class="hljs-keyword">return</span> name
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
<li>
<p>程序中不能再访问到的对象</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">fn</span>(<span class="hljs-params"></span>) </span>&#123;
<span class="hljs-keyword">const</span> name = <span class="hljs-string">'lg'</span>
  <span class="hljs-keyword">return</span> name
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
</ol>
</li>
</ul>
</li>
<li>
<p>GC可以找到内存中的垃圾、并释放和回收空间</p>
</li>
</ul>
<p>GC算法是什么</p>
<ul>
<li>Gc是一种机制，垃圾回收器完成具体的动作</li>
<li>工作的内容就是查找垃圾释放空间、回收空间</li>
<li>算法就是工作时查找和回收所遵循的工作</li>
</ul>
<p>如何去查找空间、释放空间的时候怎么去释放，回收空间的过程中如何去分配</p>
<p>常见的Gc算法</p>
<ul>
<li>引用计数</li>
<li>标记清除</li>
<li>标记整理   （与标记清除类似，但是回收的机制不同）</li>
<li>分代回收</li>
</ul>
<p>引用计数算法的实现</p>
<ul>
<li>核心思想：通过引用计数器维护活动对象的引用数，判断当前引用数是否为0，如果为0，则判断他是个垃圾，然后gc开始工作，开始回收垃圾。</li>
<li>引用关系发生改变时修改引用数字</li>
<li>引用数字为0时立即回收。</li>
</ul>
<p>引用计数算法的优点</p>
<ul>
<li>发现垃圾时立即回收</li>
<li>最大限度减少程序的暂停</li>
</ul>
<p>引用计数算法缺点</p>
<ul>
<li>
<p>无法回收引用循环引用的对象</p>
</li>
<li>
<p>时间开销大，速度相对不快</p>
<p>对象的循环引用</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">fn</span>(<span class="hljs-params"></span>) </span>&#123;
  <span class="hljs-keyword">const</span> obj1 = &#123;&#125;
  <span class="hljs-keyword">const</span> obj2 = &#123;&#125;
  obj1.name = obj2
  obj2.name = obj1
  
  <span class="hljs-keyword">return</span> <span class="hljs-string">'aa'</span>
&#125;
fn()
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
</ul>
<p>标记清除算法实现原理</p>
<ul>
<li>核心思想：将整个垃圾回收分为两个阶段
<ul>
<li>遍历所有对象找标记活动（可达）的对象</li>
<li>遍历所有对象清除没有标记的对象，将没有标记的对象进行清除</li>
<li>回收相应的空间</li>
</ul>
</li>
</ul>
<p>标记清除算法的优缺点</p>
<ul>
<li>解决了对象的回收操作</li>
<li>但是多了空间碎片化的问题，
<ul>
<li>空间碎片化：由于我们当前所回收的垃圾对象在地址上本身是不连续的，由于是不连续的，回收后分散在空间的各个位置，下一次需要使用内存空间的时候，如果是大了或者小了，将不能充分的利用内存空间。</li>
</ul>
</li>
</ul>
<p>标记整理算法原理</p>
<ul>
<li>标记整理可以看作是标记清除的增强</li>
<li>标记阶段的操作和标记清除一致</li>
<li>清除阶段先执行整理，移动对象位置， 让他们在地址上能够产生连续性。</li>
</ul>
<h5 data-id="heading-2">认识v8</h5>
<ul>
<li>v8是一款主流的JavaScript执行引擎</li>
<li>v8采用即时编译， 直接将源码可以编译为机器码直接执行。</li>
<li>v8内存设限 64位1.5g 32位800m</li>
</ul>
<p>v8垃圾回收的策略</p>
<p>​在程序的使用过程中，我们会使用到很多数据，有原始数据和引用数据，原始数据是由语言本身去控制的，而引用数据是在堆中的，所以需要内存管理</p>
<ul>
<li>采用分代回收的思想</li>
<li>内存分为新生代对象、老生代对象</li>
<li>针对不同代的对象(新生代、老生代)采用不同的算法， 更加高效。</li>
</ul>
<p>v8中常见的GC算法</p>
<ul>
<li>分代回收</li>
<li>空间复制</li>
<li>标记清除</li>
<li>标记整理</li>
<li>标记增量</li>
</ul>
<p>v8内存分配</p>
<ul>
<li>v8内存空间一分为二</li>
<li>小空间用于存储新生代对象（32M｜16M）</li>
<li>新生代指的是存活时间较短的对象。</li>
</ul>
<p>新生代对象回收实现</p>
<ul>
<li>
<p>回收过程采用复制算法+标记整理</p>
</li>
<li>
<p>新生代内存区分为两个等大小空间</p>
</li>
<li>
<p>使用空间为from， 空闲空间为to</p>
</li>
<li>
<p>活动对象存储于from 空间</p>
</li>
<li>
<p>标记整理后将活动对象拷贝至to</p>
</li>
<li>
<p>from 与 to交换空间完成释放</p>
</li>
</ul>
<p>回收细节说明</p>
<ul>
<li>拷贝过程中可能出现晋升</li>
<li>晋升就是将新生代对象移动至老生代</li>
<li>一轮GC还存活的新生代需要晋升</li>
<li>To空间的使用率超过25%</li>
</ul>
<p>老生代对象回收实现</p>
<ul>
<li>老生代对象存放在右侧老生代区域</li>
<li>64位1.4g 32位700M</li>
<li>老生代对象就是指的存活时间较长的对象， （闭包、全局）</li>
</ul>
<p>老年代对象回收实现</p>
<ul>
<li>主要采用标记清除、标记整理、增量标记算法</li>
<li>首先标记清除完成垃圾空间的回收</li>
<li>采用标记整理进行空间优化（老生代对象移动到新生代对象时）</li>
<li>采用增量标记进行效率优化</li>
</ul>
<p>细节对比</p>
<ul>
<li>新生代区域垃圾回收使用空间换时间</li>
<li>老生代区域垃圾回收不适合复制算法， 而且内存一分为二会造成浪费</li>
</ul>
<p>v8总结：</p>
<ul>
<li>v8是为浏览器而生的，是一款主流的JavaScript执行引擎</li>
<li>v8内存设置上限</li>
<li>v8采用基于分代回收思想实现垃圾回收</li>
<li>v8内存分为新生代和老生代</li>
<li>v8垃圾回收常见的GC算法</li>
</ul>
<h5 data-id="heading-3">Performance</h5>
<ul>
<li>GC的目的是为了实现内存空间的良性循环</li>
<li>良性循环的基石是合理使用</li>
<li>时刻关注才能确定是否合理</li>
<li>Performance提供多种监控方式</li>
</ul>
<p>Performance使用步骤</p>
<ul>
<li>打开浏览器输入目标网址</li>
<li>进入开发人员工具面板，选择性能</li>
<li>开启录制功能， 访问具体页面</li>
<li>执行用户行为，一段时间后停止录制</li>
<li>分析界面中记录的内存信息。</li>
</ul>
<p>内存问题的外在表现（在网络正常的情况下）</p>
<ul>
<li>页面出现延迟加载或经常性暂停（GC频繁的出现）</li>
<li>页面持续性出现糟糕的性能（内存膨胀，为了想有更好的体验，申请了过大的内存，超过了设备能提供的内存）</li>
<li>页面的性能随时间延长越来越差（内存产生了泄漏）</li>
</ul>
<p>界定内存问题的标准</p>
<ul>
<li>内存泄漏： 内存使用持续升高</li>
<li>内存膨胀：在多数设备上都存在性能问题</li>
<li>频繁的垃圾回收： 通过内存变化图进行分析</li>
</ul>
<p>监控内存的几种方式</p>
<ul>
<li>浏览器任务管理器</li>
<li>Timeline时序图记录</li>
<li>堆快照查找分离dom</li>
<li>判断是否存在频繁的垃圾回收</li>
</ul>
<p>什么是分离dom</p>
<p>堆快照功能的工作原理：对js进行堆快照的留存。</p>
<ul>
<li>界面元素存活在dom树上
<ul>
<li>垃圾对象时的dom阶段
<ul>
<li>dom节点从dom树上进行了脱离，而且js代码中没有对它的引用了</li>
</ul>
</li>
<li>分离状态的dom节点
<ul>
<li>dom节点从dom树上进行了脱离，js代码对它没有任何引用。</li>
</ul>
</li>
</ul>
</li>
</ul>
<h5 data-id="heading-4">代码优化</h5>
<ul>
<li>
<p>慎用全局变量</p>
<ul>
<li>全局的尽量变成局部的</li>
<li>将使用 中无法避免的全局变量缓存到局部
<ul>
<li>例如：缓存document</li>
</ul>
</li>
</ul>
</li>
<li>
<p>通过原型添加附加方法具有更快的执行速度</p>
</li>
<li>
<p>避免闭包陷阱</p>
<ul>
<li>闭包使用不当很容易产生内存泄漏</li>
</ul>
</li>
</ul>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">foo</span>(<span class="hljs-params"></span>) </span>&#123;
  <span class="hljs-keyword">var</span> name = <span class="hljs-string">'lg'</span>
  <span class="hljs-keyword">return</span> <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params"></span>) </span>&#123;
<span class="hljs-built_in">console</span>.log(name)
  &#125;
&#125;
<span class="hljs-keyword">var</span> a = foo()
a()
<span class="hljs-comment">// 闭包的特点</span>
<span class="hljs-comment">// 1. 对产生闭包的foo函数而言， 它的外部具有指向它的内部的引用</span>
<span class="hljs-comment">// 2. 在外部作用域（a函数）可以访问内部作用域（foo函数）的数据（foo函数作用域内的name）</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>
<p>避免属性访问方法</p>
<p>JavaScript中的面向对象</p>
<ul>
<li>
<p>js不需要属性的访问方法，所有属性都是外部可见的</p>
</li>
<li>
<p>使用属性访问方法只会增加一层重定义，没有访问的控制力。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">Person</span>(<span class="hljs-params"></span>) </span>&#123;
  <span class="hljs-built_in">this</span>.name = <span class="hljs-string">'icoder'</span>
  <span class="hljs-built_in">this</span>.age = <span class="hljs-number">18</span> <span class="hljs-comment">// 假如被私有化</span>
  <span class="hljs-built_in">this</span>.getAge = <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params"></span>) </span>&#123;
    <span class="hljs-keyword">return</span> <span class="hljs-built_in">this</span>.age
&#125;
&#125;
<span class="hljs-keyword">new</span> Person().getAge() <span class="hljs-comment">// slower</span>
<span class="hljs-keyword">new</span> Person().age  <span class="hljs-comment">// faster</span>
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
</ul>
</li>
<li>
<p>文档碎片优化节点添加</p>
<ul>
<li>
<p>节点的添加操作必然会有回流和重绘</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// 定义文档碎片容器</span>
<span class="hljs-keyword">const</span> fragEle = <span class="hljs-built_in">document</span>.createDocumentFragment()
<span class="hljs-keyword">for</span>(<span class="hljs-keyword">var</span> i =<span class="hljs-number">0</span>;i<<span class="hljs-number">10</span>;i++) &#123;
  <span class="hljs-keyword">var</span> op = <span class="hljs-built_in">document</span>.createElement(<span class="hljs-string">'p'</span>)
  op.innerHTML = i
  fragEle.appendChild(op)
&#125;
<span class="hljs-comment">// 想body中添加文档碎片容器</span>
<span class="hljs-built_in">document</span>.body.appendChild(op)
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
</ul>
</li>
</ul></div>  
</div>
            