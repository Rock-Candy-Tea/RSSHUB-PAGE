
---
title: 'JavaScript 中的这些继承方式，你弄懂了吗？'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/141f4d9f90c84228bdb0320cca7fedc9~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Thu, 13 May 2021 18:58:57 GMT
thumbnail: 'https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/141f4d9f90c84228bdb0320cca7fedc9~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;color:#383838;font-size:15px;line-height:37.5px;letter-spacing:2px;word-break:break-word;font-family:-apple-system,BlinkMacSystemFont,Segoe UI,Roboto,Oxygen,Ubuntu,Cantarell,Open Sans,Helvetica Neue,sans-serif;scroll-behavior:smooth;background-image:linear-gradient(0deg,transparent 24%,rgba(201,195,195,.329) 25%,hsla(0,8%,80.4%,.05) 26%,transparent 27%,transparent 74%,hsla(0,5.2%,81%,.185) 75%,rgba(180,176,176,.05) 76%,transparent 77%,transparent),linear-gradient(90deg,transparent 24%,rgba(204,196,196,.226) 25%,hsla(0,4%,66.1%,.05) 26%,transparent 27%,transparent 74%,hsla(0,5.2%,81%,.185) 75%,rgba(180,176,176,.05) 76%,transparent 77%,transparent);background-color:#fff;background-size:50px 50px;padding-bottom:120px&#125;.markdown-body ::selection&#123;color:#fff;background-color:#a862ea&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;margin:30px 0 15px;color:#a862ea&#125;.markdown-body h1&#123;line-height:2;font-size:1.4em&#125;.markdown-body h1~p:first-of-type:first-letter&#123;color:#a862ea;float:left;font-size:2em;margin-right:.4em;font-weight:bolder&#125;.markdown-body h2&#123;font-size:1.2em&#125;.markdown-body h3&#123;font-size:1.1em&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:2em&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;padding-left:.2em&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:10px&#125;.markdown-body li::marker&#123;color:#a862ea&#125;.markdown-body li,.markdown-body p&#123;opacity:.9;vertical-align:baseline;transition:all .1s ease&#125;.markdown-body li:hover,.markdown-body p:hover&#123;opacity:1&#125;.markdown-body a&#123;display:inline-block;color:#a862ea;cursor:pointer;padding-bottom:2px;text-decoration:none;position:relative&#125;.markdown-body a:after&#123;content:"";position:absolute;width:98%;height:2px;bottom:0;left:0;transform:scaleX(0);background-color:#a862ea;transform-origin:bottom right;transition:transform .3s ease-in-out&#125;.markdown-body a:hover:after&#123;transform:scaleX(1);transform-origin:bottom left&#125;.markdown-body a:active,.markdown-body a:link&#123;color:#a862ea&#125;.markdown-body img&#123;max-width:100%;user-select:none;margin:1em 0;box-shadow:0 0 20px 0 #e7daff;transition:transform .2s ease 0s;background-color:#f8f5ff&#125;.markdown-body img:hover&#123;opacity:1;transform:translateY(-2px)&#125;.markdown-body blockquote&#123;padding:.5em 1em;margin:15px 0;border-top-left-radius:2px;border-bottom-left-radius:2px;border-left:4px solid #a862ea;background-color:#f8f5ff&#125;.markdown-body blockquote>p&#123;margin:0&#125;.markdown-body code&#123;padding:2px .4em;overflow-x:auto;color:#a862ea;font-weight:700;word-break:break-word;font-family:Operator Mono,Consolas,Monaco,Menlo,monospace;background-color:#f8f5ff&#125;.markdown-body pre&#123;margin:2em 0;box-shadow:0 0 20px #e7daff&#125;.markdown-body pre>code&#123;display:block;padding:1.5em;word-break:normal;font-size:.9em;font-style:normal;font-weight:400;font-family:Operator Mono,Consolas,Monaco,Menlo,monospace;line-height:22.5px;color:#383838;border-radius:3px;scroll-behavior:smooth&#125;.markdown-body pre>code::-webkit-scrollbar&#123;height:6px;background-color:#f8f5ff&#125;.markdown-body pre>code::-webkit-scrollbar-thumb&#123;background-color:#e7daff;border-bottom-left-radius:3px;border-bottom-right-radius:3px&#125;.markdown-body hr&#123;margin:2em 0;border-top:1px solid #a862ea&#125;.markdown-body table&#123;font-size:12px;max-width:100%;overflow:auto;border-collapse:collapse;border:1px solid #e7daff&#125;.markdown-body thead&#123;color:#a862ea;background:#f8f5ff&#125;.markdown-body td,.markdown-body th&#123;padding:1em .5em&#125;.markdown-body tr&#123;background-color:#fcfcfc&#125;@media (max-width:720px)&#123;.markdown-body&#123;font-size:12px&#125;&#125;</style><blockquote>
<p>面试中我们经常会被问到继承，希望通过此文，你能彻底搞懂 JavaScript 中的继承原理。</p>
</blockquote>
<h3 data-id="heading-0">前言</h3>
<p>ES6 以前，JavaScript 中的继承不像其它 oo 语言一样，用特定 class 去实现，它是由构造函数和原型去模拟，下面我们会介绍几种常见的继承方法以及对应的优点和不足。</p>
<h3 data-id="heading-1">原型链</h3>
<h5 data-id="heading-2">什么是原型链？</h5>
<p>比如我有一个构造函数，这个构造函数的实例有一个内部指针[[Prototype]]指向构造函数的原型，然后这个构造函数的原型又是另一个构造函数的实例，也就是说这个构造函数原型有一个内部指针[[Prototype]]指向另一个构造函数的原型，如此下去，就构成了一条原型链。那用原型链实现继承用代码表示出来就是这样：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">Parent</span> (<span class="hljs-params"></span>) </span>&#123;
    <span class="hljs-built_in">this</span>.name = <span class="hljs-string">'Twittytop'</span>;
&#125;
Parent.prototype.getName = <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params"></span>) </span>&#123;
    <span class="hljs-keyword">return</span> <span class="hljs-built_in">this</span>.name;
&#125;
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">Child</span> (<span class="hljs-params"></span>) </span>&#123;
    <span class="hljs-built_in">this</span>.age = <span class="hljs-number">29</span>;
&#125;
<span class="hljs-comment">// 继承</span>
Child.prototype = <span class="hljs-keyword">new</span> Parent();
<span class="hljs-keyword">var</span> ins = <span class="hljs-keyword">new</span> Child();
<span class="hljs-built_in">console</span>.log(ins.getName()); <span class="hljs-comment">// Twittytop</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这样原来在 Parent 上的属性都变成了 Child.prototype 上的属性。</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/141f4d9f90c84228bdb0320cca7fedc9~tplv-k3u1fbpfcp-watermark.image" alt="inherit1.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h5 data-id="heading-3">问题</h5>
<p>第一：共享问题</p>
<p>当 Parent 上包含有引用属性时，就出出现问题，比如：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">Parent</span> (<span class="hljs-params"></span>) </span>&#123;
    <span class="hljs-built_in">this</span>.friends = [<span class="hljs-string">'Jack'</span>, <span class="hljs-string">'Tom'</span>];
&#125;
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">Child</span> (<span class="hljs-params"></span>) </span>&#123;
    <span class="hljs-built_in">this</span>.age = <span class="hljs-number">29</span>;
&#125;
<span class="hljs-comment">// 继承</span>
Child.prototype = <span class="hljs-keyword">new</span> Parent();
<span class="hljs-keyword">var</span> ins1 = <span class="hljs-keyword">new</span> Child();
ins1.friends.push(<span class="hljs-string">'Bob'</span>);
<span class="hljs-keyword">var</span> ins2 = <span class="hljs-keyword">new</span> Child();
<span class="hljs-built_in">console</span>.log(ins2.friends); <span class="hljs-comment">// ["Jack", "Tom", "Bob"]</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>因为继承之后变成了 Child 的原型属性，所以所有 Child 的实例都指向的是同一个 friends，当其中一个实例修改了这个值之后，变化就会反映到所有实例上。</p>
<p>第二： 传参问题</p>
<p>Child 在实例化是没法向 Parent 传参，当 Parent 依赖外部传参时，就会导致问题。</p>
<h3 data-id="heading-4">盗用构造函数</h3>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">Parent</span> (<span class="hljs-params">name</span>) </span>&#123;
    <span class="hljs-built_in">this</span>.name = name;
&#125;
Parent.prototype.getName = <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params"></span>) </span>&#123;
    <span class="hljs-keyword">return</span> <span class="hljs-built_in">this</span>.name;
&#125;
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">Child</span> (<span class="hljs-params">name, age</span>) </span>&#123;
    <span class="hljs-comment">// 继承</span>
    Parent.call(<span class="hljs-built_in">this</span>, name);
    <span class="hljs-built_in">this</span>.age = age;
&#125;
<span class="hljs-keyword">var</span> ins = <span class="hljs-keyword">new</span> Child(<span class="hljs-string">'Twittytop'</span>, <span class="hljs-number">29</span>);
<span class="hljs-built_in">console</span>.log(ins.name); <span class="hljs-comment">// Twittytop</span>
<span class="hljs-built_in">console</span>.log(ins.getName); <span class="hljs-comment">// undefined</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>可以看到，盗用构造函数的优点是能传递参数，问题是它只能继承实例属性，不能继承原型属性。</p>
<h3 data-id="heading-5">组合继承</h3>
<p>既然原型链和盗用构造函数继承都有各自的缺点，那我们能不能把这两者结合起来呢？这就是组合继承。</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">Parent</span> (<span class="hljs-params">name</span>) </span>&#123;
    <span class="hljs-built_in">this</span>.name = name;
&#125;
Parent.prototype.getName = <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params"></span>) </span>&#123;
    <span class="hljs-keyword">return</span> <span class="hljs-built_in">this</span>.name;
&#125;
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">Child</span> (<span class="hljs-params">name, age</span>) </span>&#123;
    <span class="hljs-comment">// 继承实例属性</span>
    Parent.call(<span class="hljs-built_in">this</span>, name);
    <span class="hljs-built_in">this</span>.age = age;
&#125;
<span class="hljs-comment">// 继承原型属性</span>
Child.prototype = <span class="hljs-keyword">new</span> Parent();
<span class="hljs-keyword">var</span> ins = <span class="hljs-keyword">new</span> Child(<span class="hljs-string">'Twittytop'</span>, <span class="hljs-number">29</span>);
<span class="hljs-built_in">console</span>.log(ins.name); <span class="hljs-comment">// Twittytop</span>
<span class="hljs-built_in">console</span>.log(ins.getName()); <span class="hljs-comment">// Twittytop</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>组合继承弥补了原型链和盗用构造函数的不足，能同时继承实例属性和原型属性，但它的缺点是会调用两次父类构造函数。一次是在 Child 构造函数中执行 Parent.call，一次是在实例化 Parent 时。这样就会导致 Child 的不仅自身实例上有 name 属性，原型上也有 name 属性，导致了不必要的多余继承。用图表示如下：</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/6587360d39de4a728c6ea32ce8b46f24~tplv-k3u1fbpfcp-watermark.image" alt="inherit2.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-6">原型式继承</h3>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">Parent</span> (<span class="hljs-params">name</span>) </span>&#123;
    <span class="hljs-built_in">this</span>.name = <span class="hljs-string">'Twittytop'</span>;
&#125;
Parent.prototype.getName = <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params"></span>) </span>&#123;
    <span class="hljs-keyword">return</span> <span class="hljs-built_in">this</span>.name;
&#125;
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">Child</span> (<span class="hljs-params">age</span>) </span>&#123;
    <span class="hljs-built_in">this</span>.age = age;
&#125;
<span class="hljs-comment">// 继承原型属性</span>
Child.prototype = <span class="hljs-built_in">Object</span>.create(Parent.prototype);
<span class="hljs-keyword">var</span> ins = <span class="hljs-keyword">new</span> Child(<span class="hljs-number">29</span>);
<span class="hljs-built_in">console</span>.log(ins.getName);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>原型式继承只继承了原型上的属性，没有继承实例属性，相比原型链继承更干净，它没有把父类的实例属性继承到自身的原型上面，当然，它和原型链一样，也会有引用属性的共享问题。</p>
<h3 data-id="heading-7">寄生式继承</h3>
<p>寄生式继承是建立在原型式继承基础上的，寄生式继承用代码表达出来是这样：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">inherit</span> (<span class="hljs-params">Parent</span>) </span>&#123;
    <span class="hljs-keyword">let</span> pro = <span class="hljs-built_in">Object</span>.create(Parent.prototype);
    pro.myMethod = <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params"></span>) </span>&#123;&#125;;
    <span class="hljs-keyword">return</span> pro;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>它相比原型式继承多了添加一些自己的属性和方法。</p>
<h3 data-id="heading-8">寄生式组合继承</h3>
<p>寄生式组合继承综合了盗用构造函数和寄生式继承，它使用盗用构造函数继承实例属性，使用寄生式继承继承原型属性。</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">inherit</span> (<span class="hljs-params">Child, Parent</span>) </span>&#123;
    <span class="hljs-keyword">let</span> pro = <span class="hljs-built_in">Object</span>.create(Parent.prototype);
    pro.constructor = Child; <span class="hljs-comment">// 将constructor重新指回Child</span>
    Child.prototype = pro;
&#125;
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">Parent</span> (<span class="hljs-params">name</span>) </span>&#123;
    <span class="hljs-built_in">this</span>.name = name;
&#125;
Parent.prototype.getName = <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params"></span>) </span>&#123;
    <span class="hljs-keyword">return</span> <span class="hljs-built_in">this</span>.name;
&#125;
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">Child</span> (<span class="hljs-params">name, age</span>) </span>&#123;
    <span class="hljs-comment">// 继承实例属性</span>
    Parent.call(<span class="hljs-built_in">this</span>, name);
    <span class="hljs-built_in">this</span>.age = age;
&#125;
<span class="hljs-comment">// 继承原型属性</span>
inherit(Child, Parent)
<span class="hljs-keyword">var</span> ins = <span class="hljs-keyword">new</span> Child(<span class="hljs-string">'Twittytop'</span>, <span class="hljs-number">29</span>);
<span class="hljs-built_in">console</span>.log(ins.name); <span class="hljs-comment">// Twittytop</span>
<span class="hljs-built_in">console</span>.log(ins.getName()); <span class="hljs-comment">// Twittytop</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>寄生式组合继承吸取了盗用构造函数和寄生式继承的优点，又没有组合继承中调用父类构造函数两次的不足，是ES5 实现继承的最佳模式。</p>
<p>关于 ES6 的继承，这里就不介绍了，它本质是上述继承的语法糖而已。</p>
<h3 data-id="heading-9">写在后面</h3>
<p>JavaScript 继承独特的地方就是它的原型，如果这篇文章能让你对 JavaScript 继承有进一步的了解，那将是我最大的欣慰。如果你觉得能学到一点东西的话，还请动动你可爱的小指让更多人看到。如果有错误或者有疑问的地方，也欢迎交流讨论。</p></div>  
</div>
            