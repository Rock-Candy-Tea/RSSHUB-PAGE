
---
title: 'JS 垃圾回收机制解析 _ 8月更文挑战'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/329aef708e59432f8a35ad0914e3f4cc~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Thu, 19 Aug 2021 16:27:10 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/329aef708e59432f8a35ad0914e3f4cc~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><blockquote>
<p><strong>这是我参与8月更文挑战的第14天，活动详情查看：<a href="https://juejin.cn/post/6987962113788493831" title="https://juejin.cn/post/6987962113788493831" target="_blank">8月更文挑战</a></strong></p>
</blockquote>
<h1 data-id="heading-0">概述</h1>
<p>JS是一门具有自动垃圾回收机制的语言，开发人员不必关心内存分配和回收问题。</p>
<p>JS的垃圾回收机制是为了以防内存泄漏，内存泄漏的含义就是当已经不需要某块内存时这块内存还存在着，垃圾回收机制就是间歇的不定期的寻找到不再使用的变量，并释放掉它们所指向的内存。</p>
<h1 data-id="heading-1">JS 垃圾回收方式</h1>
<p>JS执行环境中的垃圾回收器怎样才能检测哪块内存可以被回收有两种方式：标记清除（mark and sweep）、引用计数(reference counting)。</p>
<h2 data-id="heading-2">标记清除</h2>
<p>大部分浏览器以此方式进行垃圾回收，当变量进入执行环境（函数中声明变量）的时候，垃圾回收器将其标记为“进入环境”，当变量离开环境的时候（函数执行结束）将其标记为“离开环境”，在离开环境之后还有的变量则是需要被删除的变量。标记方式不定，可以是某个特殊位的反转或维护一个列表等。</p>
<p>垃圾收集器给内存中的所有变量都加上标记，然后<strong>去掉环境中的变量以及被环境中的变量引用的变量的标记</strong>。在此之后再被加上的标记的变量即为需要回收的变量，因为环境中的变量已经无法访问到这些变量。</p>
<p><strong>核心思想：给当前不使用的值加上标记，然后再回收其内存。</strong></p>
<p>这样解释可能不容易理解，下面介绍一种简易理解的方法：</p>
<h3 data-id="heading-3">可达性</h3>
<p>JavaScript 中内存管理的主要概念是可达性。</p>
<p>简单地说，“可达性” 值就是那些以某种方式可访问或可用的值，它们被保证存储在内存中。</p>
<p><strong>1. 有一组基本的固有可达值，由于显而易见的原因无法删除。例如:</strong></p>
<ul>
<li>本地函数的局部变量和参数</li>
<li>当前嵌套调用链上的其他函数的变量和参数</li>
<li>全局变量</li>
<li>还有一些其他的，内部的</li>
</ul>
<p><strong>这些值称为根。</strong></p>
<p><strong>2. 如果引用或引用链可以从根访问任何其他值，则认为该值是可访问的。</strong></p>
<p>例如，如果局部变量中有对象，并且该对象具有引用另一个对象的属性，则该对象被视为<strong>可达性</strong>， 它引用的那些也是可以访问的，详细的例子如下。</p>
<p>JavaScript 引擎中有一个后台进程称为<strong>垃圾回收器</strong>，它监视所有对象，并删除那些不可访问的对象。</p>
<h3 data-id="heading-4">内部算法</h3>
<p>基本的垃圾回收算法称为**“标记-清除”**，定期执行以下“垃圾回收”步骤:</p>
<ul>
<li>垃圾回收器获取根并**“标记”**(记住)它们。</li>
<li>然后它访问并“标记”所有来自它们的引用。</li>
<li>然后它访问标记的对象并标记它们的引用。所有被访问的对象都被记住，以便以后不再访问同一个对象两次。</li>
<li>以此类推，直到有未访问的引用(可以从根访问)为止。</li>
<li>除标记的对象外，所有对象都被删除。</li>
</ul>
<p>例如，对象结构如下:</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/329aef708e59432f8a35ad0914e3f4cc~tplv-k3u1fbpfcp-watermark.image" alt="在这里插入图片描述" loading="lazy" referrerpolicy="no-referrer"></p>
<p>我们可以清楚地看到右边有一个“不可到达的块”。现在让我们看看“标记并清除”垃圾回收器如何处理它。</p>
<p><strong>第一步标记根</strong></p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/40372596e57c4ee596d7a21138b8cedd~tplv-k3u1fbpfcp-watermark.image" alt="<img src="/Users/mxj/百度云同步盘/学习笔记/前端全栈/js/js基础语法/img/image-20200629111020772.png" alt="image-20200629111020772" style="zoom:50%;" />" loading="lazy" referrerpolicy="no-referrer"></p>
<p><strong>然后标记他们的引用</strong></p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/b9ead9582b814c2d8b05748294f2c216~tplv-k3u1fbpfcp-watermark.image" alt="<img src="/Users/mxj/百度云同步盘/学习笔记/前端全栈/js/js基础语法/img/image-20200629111101448.png" alt="image-20200629111101448" style="zoom:50%;" />" loading="lazy" referrerpolicy="no-referrer"></p>
<p>以及子孙代的引用:</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/49c9a2cb39a04ed9b2e640f24ad4bebc~tplv-k3u1fbpfcp-watermark.image" alt="在这里插入图片描述" loading="lazy" referrerpolicy="no-referrer"></p>
<p>现在进程中不能访问的对象被认为是不可访问的，将被删除:</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/673040b17e22477b9625cc85083ff43c~tplv-k3u1fbpfcp-watermark.image" alt="<img src="/Users/mxj/百度云同步盘/学习笔记/前端全栈/js/js基础语法/img/image-20200629111231020.png" alt="image-20200629111231020" style="zoom:50%;" />" loading="lazy" referrerpolicy="no-referrer"></p>
<p>这就是垃圾收集的工作原理。JavaScript 引擎应用了许多优化，使其运行得更快，并且不影响执行。</p>
<h2 data-id="heading-5">引用计数</h2>
<p>这种方式常常会引起内存泄漏，低版本的IE使用这种方式。机制就是跟踪一个值的引用次数，当声明一个变量并将一个引用类型赋值给该变量时该值引用次数加1，当这个变量指向其他一个时该值的引用次数便减一。当该值引用次数为0时就会被回收。</p>
<p>该方式会引起内存泄漏的原因是它不能解决循环引用的问题：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">sample</span>(<span class="hljs-params"></span>)</span>&#123;
    <span class="hljs-keyword">var</span> a=&#123;&#125;;
    <span class="hljs-keyword">var</span> b=&#123;&#125;;
    a.prop = b;
    b.prop = a;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这种情况下每次调用sample()函数，a和b的引用计数都是2，会使这部分内存永远不会被释放，即内存泄漏。</p>
<blockquote>
<p>低版本IE中有一部分对象并不是原生JS对象。例如，其BOM和DOM中的对象就是使用C++以COM(Component Object Model)对象的形式实现的，而COM对象的垃圾收集机制采用的就是引用计数策略。</p>
<p><strong>因此即使IE的js引擎是用的标记清除来实现的，但是js访问COM对象如BOM,DOM还是基于引用计数的策略的</strong>，也就是说只要在IE中设计到COM对象，也就会存在循环引用的问题。</p>
</blockquote>
<h1 data-id="heading-6">总结</h1>
<ul>
<li>离开作用域的值将被自动标记为可回收，因此将在垃圾回收期间被删除</li>
<li>“标记清除”是目前主流的垃圾回收算法，这种算法的思想是给当前不使用的值加上标记，然后再回收其内存</li>
<li>而“引用计数”，这种算法的思想是跟踪记录所有值被引用的次数。JS引擎目前都不再使用这种算法；IE9以前有这种算法</li>
<li>当代码中存在循环引用现象时，“引用计数”算法会导致问题</li>
<li>解除变量的引用不仅有助于消除循环引用现象，而且对垃圾收集也有好处。为了确保有效的回收内存，应该及时解除不再使用的全局对象，全局对象属性以及循环引用变量的引用</li>
</ul>
<p><strong>优化</strong></p>
<ul>
<li><strong>分代回收</strong>——对象分为两组:“新对象”和“旧对象”。许多对象出现，完成它们的工作并迅速结 ，它们很快就会被清理干净。那些活得足够久的对象，会变“老”，并且很少接受检查。</li>
<li><strong>增量回收</strong>——如果有很多对象，并且我们试图一次遍历并标记整个对象集，那么可能会花费一些时间，并在执行中会有一定的延迟。因此，引擎试图将垃圾回收分解为多个部分。然后，各个部分分别执行。这需要额外的标记来跟踪变化，这样有很多微小的延迟，而不是很大的延迟。</li>
<li><strong>空闲时间收集</strong>——垃圾回收器只在 CPU 空闲时运行，以减少对执行的可能影响。</li>
</ul></div>  
</div>
            