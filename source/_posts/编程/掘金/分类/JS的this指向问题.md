
---
title: 'JS的this指向问题'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=7530'
author: 掘金
comments: false
date: Tue, 24 Aug 2021 00:43:47 GMT
thumbnail: 'https://picsum.photos/400/300?random=7530'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p><strong>这是我参与8月更文挑战的第24天，活动详情查看：<a href="https://juejin.cn/post/6987962113788493831" title="https://juejin.cn/post/6987962113788493831" target="_blank">8月更文挑战</a></strong></p>
<h2 data-id="heading-0">写在前面</h2>
<blockquote>
<p>在绝大多数情况下，函数的调用方式决定了 this 的值（运行时绑定）。this 不能在执行期间被赋值，并且在每次函数被调用时 this 的值也可能会不同。ES5 引入了 bind 方法来设置函数的 this 值，而不用考虑函数如何被调用的。ES2015 引入了箭头函数，箭头函数不提供自身的 this 绑定（this 的值将保持为闭合词法上下文的值）</p>
</blockquote>
<pre><code class="hljs language-js copyable" lang="js">
<span class="hljs-keyword">var</span> person = &#123;
  <span class="hljs-attr">firstName</span>: <span class="hljs-string">"LiMing"</span>,
  <span class="hljs-attr">lastName</span> : <span class="hljs-string">"Li"</span>,
  <span class="hljs-attr">id</span>       : <span class="hljs-number">123</span>,
  <span class="hljs-attr">fullName</span> : <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params"></span>) </span>&#123;
    <span class="hljs-keyword">return</span> <span class="hljs-built_in">this</span>.firstName + <span class="hljs-string">" "</span> + <span class="hljs-built_in">this</span>.lastName;
  &#125;
&#125;;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-1">this 是什么？</h2>
<blockquote>
<p>this是当前执行上下文（global、function 或 eval）的一个属性，在非严格模式下，总是指向一个对象，在严格模式下可以是任意值。</p>
<p>JavaScript this 关键词指的是它所属的对象。</p>
<p>它拥有不同的值，具体取决于它的使用位置：</p>
<ul>
<li>在方法中，<code>this</code> 指的是所有者对象。</li>
<li>单独的情况下，<code>this</code> 指的是全局对象。</li>
<li>在函数中，<code>this</code> 指的是全局对象。</li>
<li>在函数中，严格模式下，<code>this</code> 是 <code>undefined。</code></li>
<li>在事件中，<code>this</code> 指的是接收事件的元素。</li>
<li>像 call() 和 apply() 这样的方法可以将 <code>this</code> 引用到任何对象。</li>
</ul>
</blockquote>
<h2 data-id="heading-2">方法中的 this</h2>
<p>在对象方法中，<code>this</code> 指的是此方法的“拥有者”。
在本页最上面的例子中，<code>this</code> 指的是 <code>person</code> 对象。
<code>person</code> 对象是 <code>fullName</code> 方法的拥有者。</p>
<pre><code class="copyable">fullName : function() &#123;
  return this.firstName + " " + this.lastName;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-3">单独的 this</h2>
<p>在单独使用时，拥有者是全局对象，因此 this 指的是全局对象。</p>
<p>在浏览器窗口中，全局对象是 <code>[object Window]</code>：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">var</span> x = <span class="hljs-built_in">this</span>;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>在严格模式中，如果单独使用，那么 this 指的是全局对象 <code>[object Window]</code>：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-meta">"use strict"</span>;
<span class="hljs-keyword">var</span> x = <span class="hljs-built_in">this</span>;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-4">函数中的 this（默认）</h2>
<p>在 JavaScript 函数中，函数的拥有者默认绑定 <code>this</code></p>
<p>因此，在函数中，<code>this</code> 指的是全局对象 <code>[object Window]</code>。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">myFunction</span>(<span class="hljs-params"></span>) </span>&#123;
  <span class="hljs-keyword">return</span> <span class="hljs-built_in">this</span>;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-5">派生类</h2>
<p>不像基类的构造函数，派生类的构造函数没有初始的 this 绑定。在构造函数中调用 super() 会生成一个 this 绑定，并相当于执行如下代码，Base为基类：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-built_in">this</span> = <span class="hljs-keyword">new</span> Base();
<span class="copy-code-btn">复制代码</span></code></pre>
<blockquote>
<p>注意：在调用 super() 之前引用 this 会抛出错误。</p>
</blockquote>
<p>派生类不能在调用 super() 之前返回，除非其构造函数返回的是一个对象，或者根本没有构造函数。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">A</span> </span>&#123;&#125;
<span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">B</span> <span class="hljs-keyword">extends</span> <span class="hljs-title">A</span> </span>&#123;&#125;
<span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">C</span> <span class="hljs-keyword">extends</span> <span class="hljs-title">A</span> </span>&#123;
  <span class="hljs-function"><span class="hljs-title">constructor</span>(<span class="hljs-params"></span>)</span> &#123;
    <span class="hljs-keyword">return</span> &#123;<span class="hljs-attr">X</span>: <span class="hljs-number">12</span>&#125;;
  &#125;
&#125;
<span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">D</span> <span class="hljs-keyword">extends</span> <span class="hljs-title">A</span> </span>&#123;
  <span class="hljs-function"><span class="hljs-title">constructor</span>(<span class="hljs-params"></span>)</span> &#123;&#125;
&#125;

<span class="hljs-keyword">new</span> B();
<span class="hljs-keyword">new</span> C();
<span class="hljs-keyword">new</span> D(); <span class="hljs-comment">// ReferenceError</span>

<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-6">bind方法</h2>
<blockquote>
<p>ECMAScript 5 引入了 Function.prototype.bind()。调用f.bind(someObject)会创建一个与f具有相同函数体和作用域的函数，但是在这个新函数中，this将永久地被绑定到了<code>bind</code>的第一个参数，无论这个函数是如何被调用的。</p>
</blockquote>
<h2 data-id="heading-7">箭头函数</h2>
<blockquote>
<p>在箭头函数中，this与封闭词法环境的this保持一致。在全局代码中，它将被设置为全局对象</p>
<p>注意：如果将this传递给call、bind、或者apply来调用箭头函数，它将被忽略。不过你仍然可以为调用添加参数，不过第一个参数（thisArg）应该设置为null。</p>
</blockquote></div>  
</div>
            