
---
title: '浏览器下的JS执行机制'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/f2a5a9eec1b249ac8cbc4f28e994c32e~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Fri, 07 May 2021 20:41:50 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/f2a5a9eec1b249ac8cbc4f28e994c32e~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h1 data-id="heading-0">1.变量提升</h1>
<ul>
<li>在执行过程中，若使用了未声明的变量，那么 JavaScript 执行会报错。</li>
<li>在一个变量定义之前使用它，不会出错，但是该变量的值会为 undefined，而不是定义时的值。</li>
<li>在一个函数定义之前使用它，不会出错，且函数能正确执行。</li>
</ul>
<p>所谓的变量提升，是指在 JavaScript 代码执行过程中，JavaScript 引擎把变量的声明部分和函数的声明部分提升到代码开头的“行为”。变量被提升后，会给变量设置默认值，这个默认值就是我们熟悉的 undefined。</p>
<h1 data-id="heading-1">2.JavaScript 代码的执行流程</h1>
<p>实际上变量和函数声明在代码里的位置是不会改变的，而且是在编译阶段被 JavaScript 引擎放入内存中。</p>
<p>一段 JavaScript 代码在执行之前需要被 JavaScript 引擎编译，编译完成之后，才会进入执行阶段。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/f2a5a9eec1b249ac8cbc4f28e994c32e~tplv-k3u1fbpfcp-watermark.image" alt="649c6e3b5509ffd40e13ce9c91b3d91e.png" loading="lazy" referrerpolicy="no-referrer">
JavaScript 的执行流程图</p>
<ol>
<li>编译阶段</li>
</ol>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/0ec9e854dfac43c3958957f0cb9add2b~tplv-k3u1fbpfcp-watermark.image" alt="0655d18ec347a95dfbf843969a921a13.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>输入一段代码，经过编译后，会生成两部分内容：<code>执行上下文（Execution context）和可执行代码</code></p>
<p><code>执行上下文是 JavaScript 执行一段代码时的运行环境</code>，比如调用一个函数，就会进入这个函数的执行上下文，确定该函数在执行期间用到的诸如 this、变量、对象以及函数等。</p>
<p>在执行上下文中存在一个<code>变量环境的对象</code>（Viriable Environment），该对象中保存了变量提升的内容，比如上面代码中的变量 myname 和函数 showName，都保存在该对象中。</p>
<ol start="2">
<li>执行阶段</li>
</ol>
<ul>
<li>当执行到 showName 函数时，JavaScript 引擎便开始在变量环境对象中查找该函数，由于变量环境对象中存在该函数的引用，所以 JavaScript 引擎便开始执行该函数，并输出“函数 showName 被执行”结果。</li>
<li>接下来打印“myname”信息，JavaScript 引擎继续在变量环境对象中查找该对象，由于变量环境存在 myname 变量，并且其值为 undefined，所以这时候就输出 undefined。</li>
<li>接下来执行第 3 行，把“极客时间”赋给 myname 变量，赋值后变量环境中的 myname 属性值改变为“极客时间”，变量环境如下所示：</li>
</ul>
<pre><code class="hljs language-js copyable" lang="js">VariableEnvironment: 
    myname -> <span class="hljs-string">"极客时间"</span>, 
    showName -><span class="hljs-function"><span class="hljs-keyword">function</span> : </span>&#123;<span class="hljs-built_in">console</span>.log(myname)
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>代码中出现相同的变量或者函数怎么办？
<ul>
<li>一段代码如果定义了两个相同名字的函数，那么最终生效的是最后一个函数。</li>
</ul>
</li>
</ul>
<p>总结</p>
<ul>
<li>JavaScript 代码执行过程中，需要先做变量提升，而之所以需要实现变量提升，是因为 JavaScript 代码在执行之前需要先编译。</li>
<li>在编译阶段，变量和函数会被存放到变量环境中，变量的默认值会被设置为 undefined；在代码执行阶段，JavaScript 引擎会从变量环境中去查找自定义的变量和函数。</li>
<li>如果在编译阶段，存在两个相同的函数，那么最终存放在变量环境中的是最后定义的那个，这是因为后定义的会覆盖掉之前定义的。</li>
</ul>
<blockquote>
<p>JavaScript 的执行机制：先编译，再执行</p>
</blockquote>
<blockquote>
<p>函数提升要比变量提升的优先级要高一些，且不会被变量声明覆盖，但是会被变量赋值之后覆盖。</p>
</blockquote>
<h1 data-id="heading-2">3.调用栈：为什么JavaScript代码会出现栈溢出？</h1>
<p>哪些情况下代码才算是“一段”代码，才会在执行之前就进行编译并创建执行上下文。一般说来，有这么三种情况：</p>
<ul>
<li>当 JavaScript 执行全局代码的时候，会编译全局代码并创建全局执行上下文，而且在整个页面的生存周期内，全局执行上下文只有一份。</li>
<li>当调用一个函数的时候，函数体内的代码会被编译，并创建函数执行上下文，一般情况下，函数执行结束之后，创建的函数执行上下文会被销毁。</li>
<li>当使用 eval 函数的时候，eval 的代码也会被编译，并创建执行上下文。</li>
</ul>
<p>调用栈就是用来管理函数调用关系的一种数据结构。</p>
<p>JavaScript 引擎正是利用栈的这种结构来管理执行上下文的。在执行上下文创建好后，JavaScript 引擎会将执行上下文压入栈中，通常把这种用来管理执行上下文的栈称为执行上下文栈，又称调用栈。</p>
<p>调用栈是一种用来管理执行上下文的数据结构，符合后进先出的规则。<code>调用栈是有大小的</code>，当入栈的执行上下文超过一定数目，JavaScript 引擎就会报错，我们把这种错误叫做<code>栈溢出</code>。</p>
<p>总结</p>
<ul>
<li>每调用一个函数，JavaScript 引擎会为其创建执行上下文，并把该执行上下文压入调用栈，然后 JavaScript 引擎开始执行函数代码。</li>
<li>如果在一个函数 A 中调用了另外一个函数 B，那么 JavaScript 引擎会为 B 函数创建执行上下文，并将 B 函数的执行上下文压入栈顶。</li>
<li>当前函数执行完毕后，JavaScript 引擎会将该函数的执行上下文弹出栈。</li>
<li>当分配的调用栈空间被占满时，会引发“堆栈溢出”问题。</li>
</ul>
<p>题目：
// 优化下这段代码，以解决栈溢出的问题</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">runStack</span> (<span class="hljs-params">n</span>) </span>&#123; 
    <span class="hljs-keyword">if</span> (n === <span class="hljs-number">0</span>) <span class="hljs-keyword">return</span> <span class="hljs-number">100</span>; 
    <span class="hljs-keyword">return</span> runStack( n- <span class="hljs-number">2</span>);
&#125;
runStack(<span class="hljs-number">1000000</span>)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>解题：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">runStack</span> (<span class="hljs-params">n</span>) </span>&#123;
  <span class="hljs-keyword">if</span> (n === <span class="hljs-number">0</span>) <span class="hljs-keyword">return</span> <span class="hljs-number">100</span>;
  <span class="hljs-keyword">return</span> runStack.bind(<span class="hljs-literal">null</span>, n- <span class="hljs-number">2</span>); <span class="hljs-comment">// 返回自身的一个版本</span>
&#125;
<span class="hljs-comment">// 蹦床函数，避免递归</span>
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">trampoline</span>(<span class="hljs-params">f</span>) </span>&#123;
  <span class="hljs-keyword">while</span> (f && f <span class="hljs-keyword">instanceof</span> <span class="hljs-built_in">Function</span>) &#123;
    f = f();
  &#125;
  <span class="hljs-keyword">return</span> f;
&#125;
trampoline(runStack(<span class="hljs-number">1000000</span>))
<span class="copy-code-btn">复制代码</span></code></pre>
<h1 data-id="heading-3">4.块级作用域：var缺陷以及为什么要引入let和const？</h1>
<p>作用域是指在程序中定义变量的区域，该位置决定了变量的生命周期。通俗地理解，作用域就是变量与函数的可访问范围，即作用域控制着变量和函数的可见性和生命周期。</p>
<p>在 ES6 之前，ES 的作用域只有两种：全局作用域和函数作用域。</p>
<ul>
<li>全局作用域中的对象在代码中的任何地方都能访问，其生命周期伴随着页面的生命周期。</li>
<li>函数作用域就是在函数内部定义的变量或者函数，并且定义的变量或者函数只能在函数内部被访问。函数执行结束之后，函数内部定义的变量会被销毁。</li>
</ul>
<p>ES6 是如何解决变量提升带来的缺陷</p>
<ul>
<li>ES6 引入了 let 和 const 关键字，从而使 JavaScript 也能像其他语言一样拥有了块级作用域。</li>
</ul>
<p>块级作用域就是通过词法环境的栈结构来实现的，而变量提升是通过变量环境来实现，通过这两者的结合，JavaScript 引擎也就同时支持了变量提升和块级作用域了。</p>
<p>问题：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">let</span> myname= <span class="hljs-string">'极客时间'</span>
&#123; 
<span class="hljs-built_in">console</span>.log(myname) 
<span class="hljs-keyword">let</span> myname= <span class="hljs-string">'极客邦'</span>
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>题解</p>
<pre><code class="copyable">【最终打印结果】：VM6277:3 Uncaught ReferenceError: Cannot access 'myname' before initialization
【分析原因】：在块作用域内，let声明的变量被提升，但变量只是创建被提升，初始化并没有被提升，在初始化之前使用变量，就会形成一个暂时性死区。
【拓展】
var的创建和初始化被提升，赋值不会被提升。
let的创建被提升，初始化和赋值不会被提升。
function的创建、初始化和赋值均会被提升。
<span class="copy-code-btn">复制代码</span></code></pre>
<h1 data-id="heading-4">5. 作用域链和闭包 ：代码中出现相同的变量，JavaScript引擎是如何选择的？</h1>
<p>JavaScript 执行过程中，其作用域链是由词法作用域决定的。</p>
<p>词法作用域就是指作用域是由代码中函数声明的位置来决定的，所以词法作用域是静态的作用域，通过它就能够预测代码在执行过程中如何查找标识符。</p>
<p>词法作用域是代码编译阶段就决定好的，和函数是怎么调用的没有关系。</p>
<p>根据词法作用域的规则，内部函数总是可以访问它们的外部函数中的变量</p>
<p>在 JavaScript 中，根据词法作用域的规则，内部函数总是可以访问其外部函数中声明的变量，当通过调用一个外部函数返回一个内部函数后，即使该外部函数已经执行结束了，但是内部函数引用外部函数的变量依然保存在内存中，我们就把这些变量的集合称为闭包。</p>
<p>所以在使用闭包的时候，你要尽量注意一个原则：<code>如果该闭包会一直使用，那么它可以作为全局变量而存在；但如果使用频率不高，而且占用内存又比较大的话，那就尽量让它成为一个局部变量。</code></p>
<h1 data-id="heading-5">6.this：从JavaScript执行上下文的视角讲清楚this</h1>
<p>作用域链和 this 是两套不同的系统，它们之间基本没太多联系。</p>
<p>全局执行上下文中的 this:指向 window 对象。</p>
<p>函数执行上下文中的 this:</p>
<p>有下面几种方式来设置函数执行上下文中的 this 值.</p>
<ul>
<li>call</li>
<li>bind</li>
<li>apply</li>
<li>通过对象调用方法设置（使用对象来调用其内部的一个方法，该方法的 this 是指向对象本身的。）
<ul>
<li>在全局环境中调用一个函数，函数内部的 this 指向的是全局变量 window。通过一个对象来调用其内部的一个方法，该方法的执行上下文中的 this 指向对象本身。</li>
</ul>
</li>
</ul>
<p>ES6 中的箭头函数并不会创建其自身的执行上下文，所以箭头函数中的 this 取决于它的外部函数。</p>
<h1 data-id="heading-6">最后：分享下自己整理的部分知识点文章链接</h1>
<ul>
<li>
<p><a href="https://juejin.cn/post/6954906499353149471" target="_blank">记录一下3月底到4月的前端开发工程师面经</a></p>
</li>
<li>
<p><a href="https://juejin.cn/post/6947117720903090206" target="_blank">面试高频的手写JS代码</a></p>
</li>
<li>
<p><a href="https://juejin.cn/post/6948629158809960479" target="_blank"> 某大厂面经 </a></p>
</li>
<li>
<p><a href="https://juejin.cn/post/6952137026825093134" target="_blank">webpack全方位由浅到深讲解，做到简历上真正所谓的“熟悉”(系列一)</a></p>
</li>
<li>
<p><a href="https://juejin.cn/post/6952139288779685901" target="_blank">webpack全方位由浅到深讲解，做到简历上真正所谓的“熟悉”(系列二)</a></p>
</li>
<li>
<p><a href="https://juejin.cn/post/6952350211888906248" target="_blank">webpack全方位由浅到深讲解，做到简历上真正所谓的“熟悉”(系列三)</a></p>
</li>
<li>
<p><a href="https://juejin.cn/post/6952694999733501988" target="_blank">webpack全方位由浅到深讲解，做到简历上真正所谓的“熟悉”(系列四)</a></p>
</li>
<li>
<p><a href="https://juejin.cn/post/6952807822203551752" target="_blank">webpack全方位由浅到深讲解，做到简历上真正所谓的“熟悉”(系列五)</a></p>
</li>
</ul></div>  
</div>
            