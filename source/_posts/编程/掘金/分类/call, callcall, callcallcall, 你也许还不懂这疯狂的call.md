
---
title: 'call, call.call, call.call.call, 你也许还不懂这疯狂的call'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=9685'
author: 掘金
comments: false
date: Mon, 23 Aug 2021 16:08:58 GMT
thumbnail: 'https://picsum.photos/400/300?random=9685'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>这是我参与8月更文挑战的第24天，活动详情查看：<a href="https://juejin.cn/post/6987962113788493831" title="https://juejin.cn/post/6987962113788493831" target="_blank">8月更文挑战</a>。</p>
<h2 data-id="heading-0">前言</h2>
<p><code>Function.prototype.call</code> 我想大家都觉得自己很熟悉了，<strong>手写也没问题</strong>！！<br>
你确认这个问题之前， 首先看看 <strong><a href="https://juejin.cn/post/6978744007601946654" target="_blank" title="https://juejin.cn/post/6978744007601946654">三千文字，也没写好 Function.prototype.call</a></strong>,</p>
<p>看完，你感觉还OK，那么再看一道题：<br>
请问如下的输出结果</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">a</span>(<span class="hljs-params"></span>)</span>&#123; 
    <span class="hljs-built_in">console</span>.log(<span class="hljs-built_in">this</span>,<span class="hljs-string">'a'</span>)
&#125;;
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">b</span>(<span class="hljs-params"></span>)</span>&#123;
    <span class="hljs-built_in">console</span>.log(<span class="hljs-built_in">this</span>,<span class="hljs-string">'b'</span>)
&#125;
a.call.call(b,<span class="hljs-string">'b'</span>)  
<span class="copy-code-btn">复制代码</span></code></pre>
<p>如果，你也清晰的知道，结果，对不起，大佬， 打扰了，我错了！</p>
<p>本文起源:<br>
一个掘友加我微信，私聊问我这个问题，研究后，又请教了 <strong><a href="https://juejin.cn/user/764915822103079" target="_blank" title="https://juejin.cn/user/764915822103079">阿宝哥</a></strong>。<br>
觉得甚有意思，遂与大家分享！</p>
<h2 data-id="heading-1">结果</h2>
<p>结果如下： 惊喜还是意外，还是淡定呢？</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-built_in">String</span> &#123;<span class="hljs-string">"b"</span>&#125; <span class="hljs-string">"b"</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>再看看如下的代码：2个，3个，4个，更多个的call，输出都会是<code>String &#123;"b"&#125; "b"</code></p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">a</span>(<span class="hljs-params"></span>)</span>&#123; 
    <span class="hljs-built_in">console</span>.log(<span class="hljs-built_in">this</span>,<span class="hljs-string">'a'</span>)
&#125;;
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">b</span>(<span class="hljs-params"></span>)</span>&#123;
    <span class="hljs-built_in">console</span>.log(<span class="hljs-built_in">this</span>,<span class="hljs-string">'b'</span>)
&#125;
a.call.call(b,<span class="hljs-string">'b'</span>)  <span class="hljs-comment">// String &#123;"b"&#125; "b"</span>
a.call.call.call(b,<span class="hljs-string">'b'</span>)   <span class="hljs-comment">// String &#123;"b"&#125; "b"</span>
a.call.call.call.call(b,<span class="hljs-string">'b'</span>)  <span class="hljs-comment">// String &#123;"b"&#125; "b"</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>看完上面，应该有三个疑问？</p>
<ol>
<li>为什么被调用的是<code>b</code>函数</li>
<li>为什么<code>this</code>是 <code>String &#123;"b"&#125;</code></li>
<li>为什么 2, 3, 4个<code>call</code>的结果一样</li>
</ol>
<p>结论：<br>
两个以上的call，比如<code>call.call(b, 'b')</code>，你就简单理解为用 <code>b.call('b')</code></p>
<h2 data-id="heading-2">分析</h2>
<h3 data-id="heading-3">为什么 2, 3, 4个<code>call</code>的结果一样</h3>
<p><code>a.call(b)</code> 最终被调用的是<code>a</code>,<br>
<code>a.call.call(b)</code>， 最终被调用的 <code>a.call</code><br>
<code>a.call.call.call(b)</code>， 最终被执行的 <code>a.call.call</code></p>
<p>看一下引用关系</p>
<pre><code class="hljs language-js copyable" lang="js">a.call === <span class="hljs-built_in">Function</span>.protype.call  <span class="hljs-comment">// true</span>
a.call === a.call.call  <span class="hljs-comment">// true</span>
a.call === a.call.call.call  <span class="hljs-comment">// true</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>基于上述<strong>执行</strong>分析:<br>
<code>a.call</code> 被调用的是<code>a</code><br>
<code>a.call.call</code> 和 <code>a.call.call.call</code> 本质没啥区别， 被调用的都是<code>Function.prototype.call</code>。</p>
<p>为什么 2, 3, 4个<code>call</code>的结果一样，到此已经<strong>真相</strong>了</p>
<h3 data-id="heading-4">为什么被调用的是<code>b</code>函数</h3>
<p>看本质就要返璞归真，ES 标准对 <strong><a href="https://link.juejin.cn/?target=https%3A%2F%2F262.ecma-international.org%2F6.0%2F%23sec-function.prototype.call" target="_blank" rel="nofollow noopener noreferrer" title="https://262.ecma-international.org/6.0/#sec-function.prototype.call" ref="nofollow noopener noreferrer">Funtion.prototye.call</a></strong> 的描述</p>
<blockquote>
<h1 data-id="heading-5">Function.prototype.call (thisArg , ...args)</h1>
<p>When the <code>call</code> method is called on an object <code>func</code> with argument, <code>thisArg</code> and zero or more <code>args</code>, the following steps are taken:</p>
<ol>
<li>If <a href="https://link.juejin.cn/?target=https%3A%2F%2F262.ecma-international.org%2F6.0%2F%23sec-iscallable" target="_blank" rel="nofollow noopener noreferrer" title="https://262.ecma-international.org/6.0/#sec-iscallable" ref="nofollow noopener noreferrer">IsCallable</a>(<em>func</em>) is <strong>false</strong>, throw a <strong>TypeError</strong> exception.</li>
<li>Let <em>argList</em> be an empty <a href="https://link.juejin.cn/?target=https%3A%2F%2F262.ecma-international.org%2F6.0%2F%23sec-list-and-record-specification-type" target="_blank" rel="nofollow noopener noreferrer" title="https://262.ecma-international.org/6.0/#sec-list-and-record-specification-type" ref="nofollow noopener noreferrer">List</a>.</li>
<li>If this method was called with more than one argument then in left to right order, starting with the second argument, append each argument as the last element of <em>argList</em>.</li>
<li>Perform <a href="https://link.juejin.cn/?target=https%3A%2F%2F262.ecma-international.org%2F6.0%2F%23sec-preparefortailcall" target="_blank" rel="nofollow noopener noreferrer" title="https://262.ecma-international.org/6.0/#sec-preparefortailcall" ref="nofollow noopener noreferrer">PrepareForTailCall</a>().</li>
<li>Return <a href="https://link.juejin.cn/?target=https%3A%2F%2F262.ecma-international.org%2F6.0%2F%23sec-call" target="_blank" rel="nofollow noopener noreferrer" title="https://262.ecma-international.org/6.0/#sec-call" ref="nofollow noopener noreferrer">Call</a>(<em>func</em>, <em>thisArg</em>, <em>argList</em>).</li>
</ol>
</blockquote>
<p>中文翻译一下</p>
<ol>
<li>如果不可调用，抛出异常</li>
<li>准备一个argList空数组变量</li>
<li>把第一个之后的变量按照顺序添加到argList</li>
<li>返回 <a href="https://link.juejin.cn/?target=https%3A%2F%2F262.ecma-international.org%2F6.0%2F%23sec-call" target="_blank" rel="nofollow noopener noreferrer" title="https://262.ecma-international.org/6.0/#sec-call" ref="nofollow noopener noreferrer">Call</a>(<em>func</em>, <em>thisArg</em>, <em>argList</em>)的结果</li>
</ol>
<p>这里的<code>Call</code>只不是是一个抽象的定义， 实际上是调用函数内部 <strong><a href="https://link.juejin.cn/?target=https%3A%2F%2F262.ecma-international.org%2F6.0%2F%23sec-call" target="_blank" rel="nofollow noopener noreferrer" title="https://262.ecma-international.org/6.0/#sec-call" ref="nofollow noopener noreferrer">[[Call]]</a></strong> 的方法, 其也没有暴露更多的有用的信息。</p>
<p>实际上在这里，我已经停止了思考:</p>
<p><strong><a href="https://link.juejin.cn/?target=https%3A%2F%2Fstackoverflow.com%2Fquestions%2F34916477%2Fa-is-a-function-then-what-a-call-call-really-do" target="_blank" rel="nofollow noopener noreferrer" title="https://stackoverflow.com/questions/34916477/a-is-a-function-then-what-a-call-call-really-do" ref="nofollow noopener noreferrer">a is a function, then what <code>a.call.call</code> really do?</a></strong> 一文的解释，有提到 <strong><a href="https://link.juejin.cn/?target=https%3A%2F%2F262.ecma-international.org%2F6.0%2F%23sec-bound-function-exotic-objects" target="_blank" rel="nofollow noopener noreferrer" title="https://262.ecma-international.org/6.0/#sec-bound-function-exotic-objects" ref="nofollow noopener noreferrer">Bound Function Exotic Objects</a></strong> ， MDN的  <strong><a href="https://link.juejin.cn/?target=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FJavaScript%2FReference%2FGlobal_Objects%2FFunction%2Fbind" target="_blank" rel="nofollow noopener noreferrer" title="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Function/bind" ref="nofollow noopener noreferrer">Function.prototype.bind</a></strong> 也有提到：</p>
<blockquote>
<p>The <code>bind()</code> function creates a new <strong>bound function</strong>, which is an <em>exotic function object</em> (a term from ECMAScript 2015) that wraps the original function object. Calling the bound function generally results in the execution of its wrapped function.</p>
</blockquote>
<p><strong><a href="https://link.juejin.cn/?target=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FJavaScript%2FReference%2FGlobal_Objects%2FFunction%2Fcall" target="_blank" rel="nofollow noopener noreferrer" title="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Function/call" ref="nofollow noopener noreferrer">Function.prototype.call</a></strong> 相反，并没有提及！！！ 但不排查在调用过程中有生成。</p>
<p><strong><a href="https://link.juejin.cn/?target=https%3A%2F%2Fstackoverflow.com%2Fquestions%2F43424141%2Fdifference-between-function-call-function-prototype-call-function-prototype-ca" target="_blank" rel="nofollow noopener noreferrer" title="https://stackoverflow.com/questions/43424141/difference-between-function-call-function-prototype-call-function-prototype-ca" ref="nofollow noopener noreferrer">Difference between Function.call, Function.prototype.call, Function.prototype.call.call and Function.prototype.call.call.call</a></strong> 一文的解释，我觉得是比较合理的</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">my</span>(<span class="hljs-params">p</span>) </span>&#123; <span class="hljs-built_in">console</span>.log(p) &#125;
<span class="hljs-built_in">Function</span>.prototype.call.call(my, <span class="hljs-built_in">this</span>, <span class="hljs-string">"Hello"</span>); <span class="hljs-comment">// output 'Hello'</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<blockquote>
<p><code>Function.prototype.call.call(my, this, "Hello");</code> means:</p>
<p>Use <code>my</code> as <code>this</code> argument (the function context) for the function that was <code>call</code>ed. In this case <code>Function.prototype.call</code> was called.</p>
<p>So, <code>Function.prototype.call</code> would be called with <code>my</code> as its context. Which basically means - it would be the function to be invoked.</p>
<p>It would be called with the following arguments: <code>(this, "Hello")</code>, where <code>this</code> is the context to be set inside the function to be called (in this case it's <code>my</code>), and the only argument to be passed is <code>"Hello"</code> string.</p>
</blockquote>
<p>重点标出：<br>
<strong>So, <code>Function.prototype.call</code> would be called with <code>my</code> as its context. Which basically means - it would be the function to be invoked.</strong></p>
<p><strong>It would be called with the following arguments: <code>(this, "Hello")</code>, where <code>this</code> is the context to be set inside the function to be called (in this case it's <code>my</code>), and the only argument to be passed is <code>"Hello"</code> string</strong></p>
<p>翻译一下：<br>
<code>Function.prototype.call.call(my, this, "Hello")</code>表示： 用<code>my</code>作为上下文调用<code>Function.prototype.call</code>，也就是说<code>my</code>是最终被调用的函数。</p>
<p><code>my</code>带着这些 <strong><code>(this, "Hello")</code></strong> 被调用， <code>this</code> 作为被调用函数的上下文，此处是作为<code>my</code>函数的上下文， 唯一被传递的参数是 "hello"字符串。</p>
<p>基于这个理解， 我们简单验证一下, 确实是这样的表象</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// case 1:</span>
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">my</span>(<span class="hljs-params">p</span>) </span>&#123; <span class="hljs-built_in">console</span>.log(p) &#125;
<span class="hljs-built_in">Function</span>.prototype.call.call(my, <span class="hljs-built_in">this</span>, <span class="hljs-string">"Hello"</span>); <span class="hljs-comment">// output 'Hello'</span>

<span class="hljs-comment">// case 2:</span>
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">a</span>(<span class="hljs-params"></span>)</span>&#123; 
    <span class="hljs-built_in">console</span>.log(<span class="hljs-built_in">this</span>,<span class="hljs-string">'a'</span>)
&#125;;
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">b</span>(<span class="hljs-params"></span>)</span>&#123;
    <span class="hljs-built_in">console</span>.log(<span class="hljs-built_in">this</span>,<span class="hljs-string">'b'</span>)
&#125;
a.call.call(b,<span class="hljs-string">'b'</span>)  <span class="hljs-comment">// String &#123;"b"&#125; "b"</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>为什么被调用的是<code>b</code>函数， 到此也真相了。</strong></p>
<p>其实我依旧不能太释怀， 但是这个解释可以接受，表象也是正确的， 期望掘友们有更合理，更详细的解答。</p>
<h3 data-id="heading-6">为什么<code>this</code>是 <code>String &#123;"b"&#125;</code></h3>
<p>在上一节的分析中，我故意遗漏了<code>Function.prototype.call</code>的两个<code>note</code></p>
<blockquote>
<p><strong>NOTE 1</strong>:  The thisArg value is passed without modification as the <strong>this</strong> value. This is a change from Edition 3, where an <strong>undefined</strong> or <strong>null</strong> thisArg is replaced with the global object and <a href="https://link.juejin.cn/?target=https%3A%2F%2F262.ecma-international.org%2F6.0%2F%23sec-toobject" target="_blank" rel="nofollow noopener noreferrer" title="https://262.ecma-international.org/6.0/#sec-toobject" ref="nofollow noopener noreferrer">ToObject</a> is applied to all other values and that result is passed as the <strong>this</strong> value. Even though the thisArg is passed without modification, non-strict functions still perform these transformations upon entry to the function.</p>
</blockquote>
<blockquote>
<p><strong>NOTE 2</strong>: If <code>func</code> is an arrow function or a <a href="https://link.juejin.cn/?target=https%3A%2F%2F262.ecma-international.org%2F6.0%2F%23sec-bound-function-exotic-objects" target="_blank" rel="nofollow noopener noreferrer" title="https://262.ecma-international.org/6.0/#sec-bound-function-exotic-objects" ref="nofollow noopener noreferrer">bound function</a> then the <code>thisArg</code> will be ignored by the function [[Call]] in step 5.</p>
</blockquote>
<p>注意这一句：</p>
<blockquote>
<p>This is a change from Edition 3, where an <strong>undefined</strong> or <strong>null</strong> thisArg is replaced with the global object and <a href="https://link.juejin.cn/?target=https%3A%2F%2F262.ecma-international.org%2F6.0%2F%23sec-toobject" target="_blank" rel="nofollow noopener noreferrer" title="https://262.ecma-international.org/6.0/#sec-toobject" ref="nofollow noopener noreferrer">ToObject</a> is applied to all other values and that result is passed as the <strong>this</strong> value</p>
</blockquote>
<p>两点：</p>
<ol>
<li>如果<code>thisArg</code>是<code>undefined</code> 或者<code>null</code>, 会用global object替换</li>
</ol>
<p>这里的前提是 <strong>非严格模式</strong></p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-meta">"use strict"</span>

<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">a</span>(<span class="hljs-params">m</span>)</span>&#123;
    <span class="hljs-built_in">console</span>.log(<span class="hljs-built_in">this</span>, m);  <span class="hljs-comment">// undefined, 1</span>
&#125;

a.call(<span class="hljs-literal">undefined</span>, <span class="hljs-number">1</span>)
<span class="copy-code-btn">复制代码</span></code></pre>
<ol start="2">
<li>其他的所有类型，都会调用 <a href="https://link.juejin.cn/?target=https%3A%2F%2F262.ecma-international.org%2F6.0%2F%23sec-toobject" target="_blank" rel="nofollow noopener noreferrer" title="https://262.ecma-international.org/6.0/#sec-toobject" ref="nofollow noopener noreferrer">ToObject</a>进行转换</li>
</ol>
<p>所以<strong>非严格模式</strong>下， <code>this</code>肯定是个对象, 看下面的代码：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-built_in">Object</span>(<span class="hljs-string">'b'</span>) <span class="hljs-comment">// String &#123;"b"&#125;</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>note2的 <strong><a href="https://link.juejin.cn/?target=https%3A%2F%2F262.ecma-international.org%2F6.0%2F%23sec-toobject" target="_blank" rel="nofollow noopener noreferrer" title="https://262.ecma-international.org/6.0/#sec-toobject" ref="nofollow noopener noreferrer">ToObject</a></strong> 就是答案</p>
<p><strong>到此， 为什么<code>this</code>是 <code>Sting(b)</code> 这个也真相了</strong></p>
<h3 data-id="heading-7">万能的函数调用方法</h3>
<p>基于<code>Function.prototype.call.call</code>的特性，我们可以封装一个万能函数调用方法</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">var</span> call = <span class="hljs-built_in">Function</span>.prototype.call.call.bind(<span class="hljs-built_in">Function</span>.prototype.call);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>示例</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">var</span> person = &#123;
    <span class="hljs-function"><span class="hljs-title">hello</span>(<span class="hljs-params"></span>)</span> &#123; 
        <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'hello'</span>, <span class="hljs-built_in">this</span>.name) 
    &#125;
&#125;

call(person.hello, &#123;<span class="hljs-string">"name"</span>: <span class="hljs-string">"tom"</span>&#125;)  <span class="hljs-comment">// hello tom</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-8">写在最后</h2>
<p>如果你觉得不错，你的一赞一评就是我前行的最大动力。</p>
<p>技术交流群请到 <a href="https://juejin.cn/pin/6994350401550024741" title="https://juejin.cn/pin/6994350401550024741" target="_blank">这里来</a>。
或者添加我的微信 dirge-cloud，一起学习。</p>
<h2 data-id="heading-9">引用</h2>
<blockquote>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Ftc39.es%2Fecma262%2F%23sec-function.prototype.call" target="_blank" rel="nofollow noopener noreferrer" title="https://tc39.es/ecma262/#sec-function.prototype.call" ref="nofollow noopener noreferrer">sec-function.prototype.call</a><br>
<a href="https://link.juejin.cn/?target=https%3A%2F%2F262.ecma-international.org%2F6.0%2F%23sec-bound-function-exotic-objects" target="_blank" rel="nofollow noopener noreferrer" title="https://262.ecma-international.org/6.0/#sec-bound-function-exotic-objects" ref="nofollow noopener noreferrer">Bound Function Exotic Objects</a><br>
<a href="https://link.juejin.cn/?target=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FJavaScript%2FReference%2FGlobal_Objects%2FFunction%2Fbind" target="_blank" rel="nofollow noopener noreferrer" title="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Function/bind" ref="nofollow noopener noreferrer">Function.prototype.bind</a>
<a href="https://link.juejin.cn/?target=https%3A%2F%2Fstackoverflow.com%2Fquestions%2F34916477%2Fa-is-a-function-then-what-a-call-call-really-do" target="_blank" rel="nofollow noopener noreferrer" title="https://stackoverflow.com/questions/34916477/a-is-a-function-then-what-a-call-call-really-do" ref="nofollow noopener noreferrer">a is a function, then what <code>a.call.call</code> really do?</a><br>
<a href="https://link.juejin.cn/?target=https%3A%2F%2Fstackoverflow.com%2Fquestions%2F43424141%2Fdifference-between-function-call-function-prototype-call-function-prototype-ca" target="_blank" rel="nofollow noopener noreferrer" title="https://stackoverflow.com/questions/43424141/difference-between-function-call-function-prototype-call-function-prototype-ca" ref="nofollow noopener noreferrer">Difference between Function.call, Function.prototype.call, Function.prototype.call.call and Function.prototype.call.call.call</a><br>
<a href="https://link.juejin.cn/?target=https%3A%2F%2Fstackoverflow.com%2Fquestions%2F31074664%2Fjavascript-function-prototype-call" target="_blank" rel="nofollow noopener noreferrer" title="https://stackoverflow.com/questions/31074664/javascript-function-prototype-call" ref="nofollow noopener noreferrer">Javascript Function.prototype.call()</a><br>
<a href="https://link.juejin.cn/?target=https%3A%2F%2Fstackoverflow.com%2Fquestions%2F44490211%2Fcant-use-function-prototype-call-directly" target="_blank" rel="nofollow noopener noreferrer" title="https://stackoverflow.com/questions/44490211/cant-use-function-prototype-call-directly" ref="nofollow noopener noreferrer">Can't use Function.prototype.call directly</a></p>
</blockquote></div>  
</div>
            