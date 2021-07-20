
---
title: '深入理解JS闭包（请多多点赞收藏）'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/eeebfa306c6f460984743e5b118ffb50~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Mon, 19 Jul 2021 17:38:56 GMT
thumbnail: 'https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/eeebfa306c6f460984743e5b118ffb50~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h2 data-id="heading-0">前言</h2>
<p>JS<code>闭包</code>，对于每一个前端而言都是一个绕不开的概念。本人学习之初，因为闭包这个概念而花费了大量的时间以及精力去理解这个概念。所以在这里，我打算写一篇文章来分享一下本人的学习心得以及我眼中的<code>闭包</code>。</p>
<h2 data-id="heading-1">什么是闭包</h2>
<p>先来看看百度百科对<code>闭包</code>的定义：</p>
<blockquote>
<p><code>闭包</code>就是能够读取其他函数内部变量的函数。例如在javascript中，只有函数内部的子函数才能读取<a href="https://link.juejin.cn/?target=https%3A%2F%2Fbaike.baidu.com%2Fitem%2F%25E5%25B1%2580%25E9%2583%25A8%25E5%258F%2598%25E9%2587%258F%2F9844788" target="_blank" rel="nofollow noopener noreferrer" title="https://baike.baidu.com/item/%E5%B1%80%E9%83%A8%E5%8F%98%E9%87%8F/9844788" ref="nofollow noopener noreferrer">局部变量</a>，所以闭包可以理解成“定义在一个<a href="https://link.juejin.cn/?target=https%3A%2F%2Fbaike.baidu.com%2Fitem%2F%25E5%2587%25BD%25E6%2595%25B0%2F301912" target="_blank" rel="nofollow noopener noreferrer" title="https://baike.baidu.com/item/%E5%87%BD%E6%95%B0/301912" ref="nofollow noopener noreferrer">函数</a>内部的函数“。在本质上，闭包是将函数内部和函数外部连接起来的桥梁。</p>
</blockquote>
<p><strong>上面提到了<code>局部变量</code>，那什么又是<code>局部变量</code>呢？</strong> 在理解局部变量之前，我们需要先知道，一个函数的执行流程是什么样的。</p>
<h3 data-id="heading-2">执行上下文</h3>
<p><code>执行上下文</code>（execution context）是JavaScript中最重要的一个概念。<code>执行上下文</code>定义了<code>变量</code>或者<code>函数</code>有权访问的其他数据，决定了它们各自的行为。每个<code>执行上下文</code>都有一个与之关联的<code>变量对象</code>。</p>
<p><code>全局执行上下文</code>是最外围的一个执行上下文。根据ECMAScript所在的宿主环境的不同，该上下文也不同。在浏览器中，<code>全局执行上下文</code>是windows对象，在全局环境下声明的变量为<code>全局变量</code>，所有的全局变量和函数都是作为window对象的属性和方法创建的。某个<code>执行上下文</code>中的所有代码执行完毕后，该上下文被销毁，保存在其中的所有变量和函数也随之销毁（<code>全局执行上下文</code>知道应用程序退出——例如关闭浏览器或者网页时才会被销毁）</p>
<p>而每个<code>函数</code>也都有自己的<code>执行上下文</code>，当执行流进入一个函数时，函数的环境就会被推入一个环境栈当中。而在函数执行完毕后，栈将其环境弹出，把控制权返回给之前的执行环境。</p>
<blockquote>
<p>注意：<code>执行上下文</code>，顾名思义，是在某段代码执行时所定义的，所以它是动态的。某个<code>函数</code>在不同的环境调用时，可能会产生不同的<code>执行上下文</code>。</p>
</blockquote>
<p>我们来看个例子：</p>
<pre><code class="copyable">// 全局环境
var a = "全局环境";

function A() &#123;
  var a = "局部环境";
  B();
&#125;

function B() &#123;
  console.log(a);
&#125;
A();
<span class="copy-code-btn">复制代码</span></code></pre>
<p>我们来模拟一下浏览器执行上述代码时的流程。</p>
<ol>
<li><code>执行栈</code>中推入全局执行上下文，全局执行上下文中存在<code>全局变量a</code>和函数A与函数B。</li>
</ol>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/eeebfa306c6f460984743e5b118ffb50~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<ol start="2">
<li>执行流进入A函数，在<code>执行栈</code>顶推入函数A的执行上下文，函数A的执行上下文存在<code>局部变量a</code>。</li>
</ol>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/1bafcd2d281643e9a333920b6180f025~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<ol start="3">
<li>执行函数A代码块中的函数B调用指令，<code>执行栈</code>顶推入函数B的执行上下文，函数B打印<code>变量a</code>。</li>
</ol>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/f21262459d164d43aac2a5e6d96f34af~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p><strong>此时，控制台打印出了<code>全局变量</code>。</strong></p>
<p>讲到这里，我们不禁发出了疑问，根据执行栈的情况来说，理应是函数B逐层向下查找到函数A的执行上下文，并且打印出<code>局部变量</code>才对呀，为什么反而打印出了<code>全局变量</code>呢？</p>
<p><strong>这里就引出了<code>作用域</code>这个概念</strong></p>
<h3 data-id="heading-3">作用域</h3>
<p>作用域：指的是一个变量的作用范围。<br>
在ES6之前，JS的作用域只有<code>全局作用域</code>以及<code>函数作用域</code>两种，在ES6引入了<code>块级作用域</code>（本文暂且先不讨论块级作用域）。</p>
<p>一个变量如果是在全局环境下定义的，那么这个变量就存在于<code>全局作用域</code>下。以此类推，在函数内部定义的变量，则存在于<code>函数作用域</code>下。</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/52788cf136d64233b13d8a0ca9f7835c~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p><strong>在各自作用域下声明的变量只在各自作用域下有效。</strong></p>
<h3 data-id="heading-4">作用域链</h3>
<p>而JS的函数在声明时，会创建一个<code>作用域链</code>。它的用途是保证对<code>执行上下文</code>有权访问的所有变量和函数的有序访问。<code>作用域链</code>的前端，始终都是当前执行的代码所在的上下文的变量对象。如果这个上下文是函数，其变量对象为其内部声明的变量以及入参的arguments对象。<code>作用域链</code>中的下一个变量来自包含（外部）上下文，这样一直延续到全局执行上下文。<strong>而JS的函数在声明时，采用的是<code>词法作用域</code>，即在声明时就确定好了<code>作用域链</code>。作用域链的定义是静态的！</strong></p>
<p>在上面的例子里，函数A和函数B在定义时，外部执行上下文只有全局执行上下文，所以其作用域链都为：</p>
<p><code>函数A/B作用域</code> -> <code>全局作用域</code>。</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/d107d886fdba4d1da73fa159cce5f883~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>所以，上文中的例子，函数B内部通过其<code>作用域链</code>先找其内部的变量对象，发现没有变量a，便向上通过<code>作用域链</code>找到了全局作用域下的<code>全局变量</code>，并最终打印出结果。</p>
<blockquote>
<p>个人理解：<code>执行上下文</code>所构成的<code>执行栈</code>，归并出了所有变量或函数。但是，并不是在栈顶的执行上下文就一定能向下获取所有的变量或函数，因为<code>作用域</code>的存在，规定了每个<code>作用域</code>内，只能通过<code>作用域链</code>去向下正确的访问各个变量或者函数。<strong><code>执行上下文</code>是动态的，会根据调用函数环境的不同，存在不同的<code>执行栈</code>。而<code>作用域链</code>是静态的，是每个函数在创建之初根据<code>词法作用域</code>就生成的，它规定了在<code>执行栈</code>中，有权访问哪些变量或函数</strong>（纯个人总结，如有不对的地方，欢迎在评论区指出）</p>
</blockquote>
<p>那么，怎么才能在全局作用域中获取函数作用域中的值呢？</p>
<h3 data-id="heading-5">闭包</h3>
<p>说了这么多，<code>闭包</code>它终于来了。<code>闭包</code>是指有权访问另一个<code>函数作用域</code>中的变量的<code>函数</code>。创建<code>闭包</code>的方式，就是在一个函数内部返回一个匿名函数。我们来改造一下上面的那个例子：</p>
<pre><code class="copyable">var a = "全局环境";

function A() &#123;
  var a = "局部环境";
  return &#123;
    B: function () &#123;
      console.log(a);
    &#125;,
  &#125;;
&#125;

var obj = A();
obj.B(); // "局部环境"
<span class="copy-code-btn">复制代码</span></code></pre>
<p>现在，我们在函数A的内部返回了一个对象，该对象内部有一个函数B。我们在全局环境下调用了这个函数B，结果打印出了<code>局部环境</code>。这就是一个<code>闭包</code>，我们成功的在全局作用域下调用到了函数A作用域中的变量。究竟是怎么回事呢？让我们再来执行一下这段代码：</p>
<ol>
<li>全局执行上下文推入执行栈中，该上下文中存在一个全局变量a，一个函数A和一个对象obj。</li>
</ol>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/1883ec438d3e4904a31dc783e6087bf9~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<ol start="2">
<li>调用函数A，执行栈中推入函数A执行上下文。该上下文中存在一个局部变量a。</li>
</ol>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/d34957406a374eeba372b29b89c44bae~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<ol start="3">
<li>执行<code>obj.B()</code>，将函数B执行上下文推入执行栈中。</li>
</ol>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/7ebc08b559f94dd789b56f9cbcaca7b5~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<ol start="4">
<li>打印变量a，此时根据<code>词法作用域</code>，我们画出<code>作用域链</code>。函数A是在全局环境下声明的，所以其<code>作用域链</code>的下一部分指向了全局作用域，而函数B是在函数A中声明的，所以其<code>作用域链</code>的下一部分指向了函数A的函数作用域。</li>
</ol>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/ff80e205fefb4444a2e0e2db4dd5b291~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>此时，函数B的<code>作用域链</code>指向了函数A的作用域，因此打印出了<code>局部变量</code>。现在，我们通过<code>闭包</code>，可以在全局环境中使用函数作用域下的变量了，是不是感觉很棒。</p>
<p>抽象点来理解<code>闭包</code>：当一个函数内部返回了一个<code>匿名函数</code>，该<code>匿名函数</code>除了自身携带的物品外（内部的变量对象），还背着一个背包（通过<code>作用域链</code>引用的外部函数的变量对象）。在该函数外部就可以通过这个背包来访问这个函数内部的变量了。</p>
<blockquote>
<p>注意点：因为<code>闭包</code>返回出来的匿名函数有对其外部函数变量对象的引用，原本外部函数执行完后其变量对象等都会被内存回收，但由于<code>闭包</code>的存在，其外部函数的变量对象还在被引用，所以不会内存回收。我们在使用<code>闭包</code>的同时，还要注意它所带来的副作用。</p>
</blockquote>
<h2 data-id="heading-6">结语</h2>
<p><code>闭包</code>其实这个概念并不难以理解，只要了解了<code>执行上下文</code>，<code>作用域</code>，<code>作用域链</code>等概念，就能掌握<code>闭包</code>这个概念。而<code>闭包</code>在JS中的使用是非常广泛的，了解了<code>闭包</code>，相信你的JS功底会更加的扎实。由于本人也是在学习阶段，以上的文章如有不对的地方，欢迎在评论区里指出！</p>
<p>最后，码字不易，如果觉得我写的还不错的，烦请各位大佬点下宝贵的赞，你的支持是我创作的最大动力。QAQ</p></div>  
</div>
            