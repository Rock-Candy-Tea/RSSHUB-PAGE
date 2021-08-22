
---
title: 'call、apply、bind这次真的可以学懂了'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/071d4df8c61a40038bf96d33d43cd13d~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Sat, 21 Aug 2021 04:24:46 GMT
thumbnail: 'https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/071d4df8c61a40038bf96d33d43cd13d~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>看过很多手写call、apply的文章总能让我从入门到放弃。 直到遇到<a href="https://juejin.cn/post/6844903476477034510#heading-0" target="_blank" title="https://juejin.cn/post/6844903476477034510#heading-0">冴羽</a>大佬的系列文章，反复看了好多遍，真上头，感觉自己又行了。本文是对<a href="https://juejin.cn/post/6844903476477034510#heading-0" target="_blank" title="https://juejin.cn/post/6844903476477034510#heading-0">[冴羽]</a>大佬这一篇文章中学习到的call原理的总结以及在《前端开发核心知识进阶》书中提到的apply和bind原理的总结。</p>
<h2 data-id="heading-0">call实现原理</h2>
<p>call()函数传入this和若干个参数。可以改变函数调用的this值。并且向函数中传入若干个参数。</p>
<blockquote>
<p>bar.call(obj); 执行这一句代码将bar的this手动指向为obj. <strong>根据this指向原理，谁调用this就指向谁</strong>。所以bar.call(obj)相当于obj.bar();</p>
</blockquote>
<h3 data-id="heading-1">谁调用，this就指向谁。</h3>
<ul>
<li><a href="https://juejin.cn/post/6844903476477034510#heading-0" target="_blank" title="https://juejin.cn/post/6844903476477034510#heading-0">冴羽</a>大佬文章中的思路真是妙呀。文章中多次巧妙的运用了this指向问题。</li>
</ul>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">let</span> obj = &#123;
<span class="hljs-attr">name</span>: <span class="hljs-string">'123'</span>,
<span class="hljs-comment">// bar: function () &#123;</span>
<span class="hljs-comment">// console.log(this.name)</span>
<span class="hljs-comment">// &#125;</span>
&#125;
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">bar</span>(<span class="hljs-params"></span>) </span>&#123;
<span class="hljs-built_in">console</span>.log(<span class="hljs-built_in">this</span>.name)
&#125;
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">call2</span>(<span class="hljs-params">context</span>) </span>&#123;
context.fn = <span class="hljs-built_in">this</span>;<span class="hljs-comment">//谁调用call2函数，this就指向谁</span>
context.fn();<span class="hljs-comment">//相当于正在执行bar函数，执行fn()相当于在执行bar(); 还是根据谁调用this指向谁。所以这里相当于bar()函数执行，其中this是context</span>
<span class="hljs-keyword">delete</span> context.fn
&#125;
<span class="hljs-built_in">Function</span>.prototype.call2 = call2;
bar.call2(obj);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>输出：
123</p>
<h3 data-id="heading-2">还有几点要完善的</h3>
<ul>
<li>call()函数允许传null,此时的this指向为window</li>
<li>call()函数除了传入this对象之外，还允许传入若干个参数</li>
<li>call()函数允许有返回值</li>
</ul>
<h4 data-id="heading-3">解决传入值为null的问题</h4>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">call2</span>(<span class="hljs-params">context</span>) </span>&#123;
<span class="hljs-keyword">var</span> context = context||<span class="hljs-built_in">window</span>;<span class="hljs-comment">//解决传入为空的问题</span>
context.fn = <span class="hljs-built_in">this</span>;<span class="hljs-comment">//谁调用call2函数，this就指向谁</span>
context.fn();<span class="hljs-comment">//相当于正在执行bar函数，执行fn()相当于在执行bar(); 还是根据谁调用this指向谁。所以这里相当于bar()函数执行，其中this是context</span>
<span class="hljs-keyword">delete</span> context.fn
&#125;
<span class="hljs-built_in">Function</span>.prototype.call2 = call2;
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-4">解决传入有参数问题</h4>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">call2</span>(<span class="hljs-params">context</span>) </span>&#123;
<span class="hljs-keyword">var</span> argsArr = <span class="hljs-built_in">Array</span>.prototype.slice.apply(<span class="hljs-built_in">arguments</span>);<span class="hljs-comment">//伪数组转化为数组</span>
<span class="hljs-keyword">var</span> context = context||<span class="hljs-built_in">window</span>;<span class="hljs-comment">//解决传入为空的问题</span>
context.fn = <span class="hljs-built_in">this</span>;<span class="hljs-comment">//谁调用call2函数，this就指向谁</span>
<span class="hljs-keyword">var</span> args = argsArr.slice(<span class="hljs-number">1</span>);
context.fn(...args);<span class="hljs-comment">//相当于正在执行bar函数，执行fn()相当于在执行bar(); 还是根据谁调用this指向谁。所以这里相当于bar()函数执行，其中this是context</span>
<span class="hljs-keyword">delete</span> context.fn
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-5">解决有返回值问题</h4>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">call2</span>(<span class="hljs-params">context</span>) </span>&#123;
<span class="hljs-keyword">var</span> argsArr = <span class="hljs-built_in">Array</span>.prototype.slice.apply(<span class="hljs-built_in">arguments</span>);
<span class="hljs-keyword">var</span> context = context || <span class="hljs-built_in">window</span>;<span class="hljs-comment">//解决传入为空的问题</span>
context.fn = <span class="hljs-built_in">this</span>;<span class="hljs-comment">//谁调用call2函数，this就指向谁</span>
<span class="hljs-keyword">var</span> args = argsArr.slice(<span class="hljs-number">1</span>);
<span class="hljs-keyword">var</span> result = context.fn(...args);<span class="hljs-comment">//相当于正在执行bar函数，执行fn()相当于在执行bar(); 还是根据谁调用this指向谁。所以这里相当于bar()函数执行，其中this是context</span>
<span class="hljs-keyword">delete</span> context.fn
<span class="hljs-keyword">return</span> result;
&#125;
<span class="hljs-built_in">Function</span>.prototype.call2 = call2;
<span class="hljs-keyword">let</span> res = bar.call2(obj, <span class="hljs-number">1</span>, <span class="hljs-number">2</span>, <span class="hljs-number">3</span>);
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-6">apply实现原理</h2>
<p>和call的原理类似，只是传的参数有区别</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">let</span> obj = &#123;
<span class="hljs-attr">name</span>: <span class="hljs-string">'123'</span>
&#125;
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">bar</span>(<span class="hljs-params">...args</span>) </span>&#123;
<span class="hljs-built_in">console</span>.log(<span class="hljs-built_in">this</span>.name, ...args, <span class="hljs-string">"aefffff"</span>)
<span class="hljs-keyword">return</span> <span class="hljs-number">1</span>
&#125;
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">apply2</span>(<span class="hljs-params">context, arr</span>) </span>&#123;
<span class="hljs-keyword">var</span> context = context || <span class="hljs-built_in">window</span>;<span class="hljs-comment">//解决传入为空的问题</span>
context.fn = <span class="hljs-built_in">this</span>;<span class="hljs-comment">//谁调用call2函数，this就指向谁</span>
<span class="hljs-keyword">var</span> result
<span class="hljs-keyword">if</span> (arr && arr.length) &#123;
result = context.fn(...arr);
&#125; <span class="hljs-keyword">else</span> &#123;
result = context.fn();
&#125;
<span class="hljs-keyword">delete</span> context.fn
<span class="hljs-keyword">return</span> result;
&#125;

<span class="hljs-built_in">Function</span>.prototype.apply2 = apply2;
<span class="hljs-keyword">let</span> res = bar.apply2(obj, [<span class="hljs-number">1</span>, <span class="hljs-number">2</span>, <span class="hljs-number">3</span>]);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>但是这里需要注意，如果apply上本来就存在fn函数。在使用apply函数时，原有的 属性值会被覆盖，之后会被删除，为了保证键的唯一性，可以使用ES6 的<a href="https://link.juejin.cn/?target=https%3A%2F%2Fes6.ruanyifeng.com%2F%23docs%2Fsymbol" target="_blank" rel="nofollow noopener noreferrer" title="https://es6.ruanyifeng.com/#docs/symbol" ref="nofollow noopener noreferrer">Symbol</a>。</p>
<p>参考代码如下</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">apply2</span>(<span class="hljs-params">context, arr</span>) </span>&#123;
<span class="hljs-keyword">var</span> context = context || <span class="hljs-built_in">window</span>;<span class="hljs-comment">//解决传入为空的问题</span>
context.fn = <span class="hljs-built_in">this</span>;<span class="hljs-comment">//谁调用call2函数，this就指向谁</span>
<span class="hljs-keyword">var</span> fn = <span class="hljs-built_in">Symbol</span>();
<span class="hljs-keyword">var</span> result
<span class="hljs-keyword">if</span> (arr && arr.length) &#123;
result = context[fn](...arr);
&#125; <span class="hljs-keyword">else</span> &#123;
result = context[fn]();
&#125;
<span class="hljs-keyword">delete</span> context[fn]
<span class="hljs-keyword">return</span> result;
&#125;

<span class="hljs-built_in">Function</span>.prototype.apply2 = apply2;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-7">bind</h2>
<blockquote>
<p><code>bind() </code> 方法创建一个新的函数，在 <code>bind()</code> 被调用时，这个新函数的 <code>this</code> 被指定为 <code>bind()</code> 的第一个参数，而其余参数将作为新函数的参数，供调用时使用。</p>
</blockquote>
<h3 data-id="heading-8">bind方法与call,apply的区别</h3>
<ul>
<li>bind()返回的是函数</li>
<li>调用bind返回的函数的时候可以向该函数传递参数(柯里化)</li>
</ul>
<h3 data-id="heading-9">第一版 利用apply实现bind函数</h3>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">bind2</span>(<span class="hljs-params">context</span>) </span>&#123;
<span class="hljs-keyword">var</span> currentThis = <span class="hljs-built_in">this</span>;<span class="hljs-comment">//谁调用bind1 this就指向谁, 此时this指向bar</span>
<span class="hljs-keyword">var</span> arrayArgs = <span class="hljs-built_in">Array</span>.prototype.slice.call(<span class="hljs-built_in">arguments</span>);
<span class="hljs-keyword">return</span> <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params"></span>) </span>&#123;
<span class="hljs-keyword">return</span> currentThis.apply(context, arrayArgs.slice(<span class="hljs-number">1</span>));<span class="hljs-comment">//闭包 利用apply再改变bar函数的指向</span>
&#125;
&#125;
<span class="hljs-built_in">Function</span>.prototype.bind2 = bind2;
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">bar</span>(<span class="hljs-params"></span>) </span>&#123;
<span class="hljs-keyword">return</span> <span class="hljs-built_in">this</span>.name;
&#125;
<span class="hljs-keyword">let</span> obj = &#123;
<span class="hljs-attr">name</span>: <span class="hljs-string">'xxxxxx'</span>
&#125;
<span class="hljs-keyword">let</span> bindFn = bar.bind2(obj);
<span class="hljs-built_in">console</span>.log(bindFn());<span class="hljs-comment">//输出'xxxxxx'</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>第一版函数中借用闭包和apply函数实现了一个初级版bind()函数。但是别忘了bind()返回的函数是可以接收参数的。</p>
<h3 data-id="heading-10">第二版 让bind返回的函数可以接收参数</h3>
<p>这里需要利用柯里化将上面向bindFn()的参数和调用bind()函数的参数做个拼接，如下面所示。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">bind2</span>(<span class="hljs-params">context</span>) </span>&#123;
<span class="hljs-keyword">var</span> currentThis = <span class="hljs-built_in">this</span>;<span class="hljs-comment">//谁调用bind1 this就指向谁, 此时this指向bar</span>
<span class="hljs-keyword">var</span> arrayArgs = <span class="hljs-built_in">Array</span>.prototype.slice.call(<span class="hljs-built_in">arguments</span>);
<span class="hljs-keyword">return</span> <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params"></span>) </span>&#123;
<span class="hljs-keyword">var</span> bindFnArgs = <span class="hljs-built_in">Array</span>.prototype.slice.call(<span class="hljs-built_in">arguments</span>);
<span class="hljs-keyword">var</span> args =arrayArgs.slice(<span class="hljs-number">1</span>).concat(bindFnArgs);
<span class="hljs-keyword">return</span> currentThis.apply(context, args);<span class="hljs-comment">//闭包 利用apply再改变bar函数的指向</span>
&#125;
&#125;
<span class="hljs-built_in">Function</span>.prototype.bind2 = bind2;
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">bar</span>(<span class="hljs-params">...arg</span>) </span>&#123;
<span class="hljs-keyword">return</span> <span class="hljs-built_in">this</span>.name;
&#125;
<span class="hljs-keyword">let</span> obj = &#123;
<span class="hljs-attr">name</span>: <span class="hljs-string">'xxxxxx'</span>
&#125;
<span class="hljs-keyword">let</span> bindFn = bar.bind2(obj);
<span class="hljs-built_in">console</span>.log(bindFn(<span class="hljs-number">11</span>));<span class="hljs-comment">//输出'xxxxxx'</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>但是试着用<strong>new bindFn()</strong>，将bind()返回的函数作为构造器使用，如下面代码所示;</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">let</span> obj = &#123;
<span class="hljs-attr">name</span>: <span class="hljs-string">"小花"</span>
&#125;
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">bar</span>(<span class="hljs-params"></span>) </span>&#123;
<span class="hljs-built_in">console</span>.log(<span class="hljs-built_in">this</span>.name, <span class="hljs-string">"this"</span>)<span class="hljs-comment">//bar实例</span>
&#125;
<span class="hljs-keyword">let</span> barFun = bar.bind(obj);
<span class="hljs-keyword">let</span> barInstance = <span class="hljs-keyword">new</span> barFun();
<span class="copy-code-btn">复制代码</span></code></pre>
<p>输出：此时输出undefined, 明明我传的obj对象进去，却找不到obj.name说明此时this指向已经发生了改变，其实此时的this已经指向barInstance实例对象了。</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/071d4df8c61a40038bf96d33d43cd13d~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>用第二版的bind2方法执行同样的代码，此时的this一样指向obj对象，说明第二版的bind函数还存在问题。</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/4ac43d5a16814fb19b1de1829407f223~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-11">第三版 像"bind()"函数一样，解决new关键字调用问题。</h3>
<p>先看看new 操作符调用构造函数的时候做了哪些事情</p>
<ul>
<li>创建一个新的对象</li>
<li>将构造函数的this指向这个新的对象</li>
<li>为这个对象添加属性、方法。</li>
<li>最终返回一个新对象</li>
</ul>
<p>伪代码如下</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">var</span> obj = &#123;&#125;;
obj._proto_=Foo.prototype
Foo.call(obj)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>看看new 构造函数的实例到底指向谁</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">let</span> obj = &#123;
<span class="hljs-attr">name</span>: <span class="hljs-string">"小花"</span>
&#125;
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">bar</span>(<span class="hljs-params"></span>) </span>&#123;
<span class="hljs-built_in">console</span>.log(<span class="hljs-built_in">this</span>.name, <span class="hljs-string">"this"</span>)<span class="hljs-comment">//bar实例</span>
&#125;
bar.prototype.name=<span class="hljs-string">'bar上的小花'</span>
<span class="hljs-keyword">let</span> barFun = bar.bind(obj);
<span class="hljs-keyword">let</span> barInstance = <span class="hljs-keyword">new</span> barFun();
<span class="hljs-built_in">console</span>.log(barInstance)
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/83587f9c40194644b65a465ce127dca8~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>好家伙，barInstance的constructor竟然是bar函数，那如果是new 调用的情况将bind.prototype==bar.prototype不就可以了</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-built_in">Function</span>.prototype.bind2 = <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params">context</span>) </span>&#123;
<span class="hljs-keyword">var</span> me = <span class="hljs-built_in">this</span>;
<span class="hljs-keyword">var</span> args = <span class="hljs-built_in">Array</span>.prototype.slice.call(<span class="hljs-built_in">arguments</span>, <span class="hljs-number">1</span>);
<span class="hljs-keyword">var</span> bound = <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params"></span>) </span>&#123;
<span class="hljs-keyword">var</span> innerArgs = <span class="hljs-built_in">Array</span>.prototype.slice.call(<span class="hljs-built_in">arguments</span>);
<span class="hljs-keyword">var</span> finalArgs = args.concat(innerArgs);
<span class="hljs-keyword">return</span> me.apply(<span class="hljs-built_in">this</span> <span class="hljs-keyword">instanceof</span> me ? <span class="hljs-built_in">this</span> : context || <span class="hljs-built_in">this</span>, finalArgs);<span class="hljs-comment">//</span>
&#125;
bound.prototype = <span class="hljs-built_in">this</span>.prototype; <span class="hljs-comment">// // 修改返回函数的 prototype 为绑定函数的 prototype，实例就可以继承绑定函数的原型中的值</span>
<span class="hljs-keyword">return</span> bound;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>然后用这一版的函数执行上面相同的代码，和上面输出的结果一样</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/f4a72d5053764281a73c4989e2de0d09~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>我们在看看这样改变bind2原型实例上的name属性值</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">let</span> obj = &#123;
<span class="hljs-attr">name</span>: <span class="hljs-string">"小花"</span>
&#125;
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">bar</span>(<span class="hljs-params"></span>) </span>&#123;
<span class="hljs-built_in">console</span>.log(<span class="hljs-built_in">this</span>.name, <span class="hljs-string">"this"</span>)<span class="hljs-comment">//bar实例</span>
&#125;
bar.prototype.name = <span class="hljs-string">'bar上的小花'</span>
<span class="hljs-keyword">let</span> barFun = bar.bind2(obj);
barFun.prototype.name = <span class="hljs-string">"我修改了bind原型上的name值"</span>;
<span class="hljs-built_in">console</span>.log(barFun.prototype,<span class="hljs-string">'baFunnnnnnnnnnnnnnn'</span>);
<span class="hljs-built_in">console</span>.log(bar.prototype,<span class="hljs-string">'bar'</span>)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>输出结果如下：上面我们只修改了barFun.prototype.name,却发现bar.prototype上面的name也被修改了。
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/2009470d8e19463a9e170933559dfac9~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>用一个空的F构造函数缓存this原型链，代码如下面所示</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-built_in">Function</span>.prototype.bind2 = <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params">context</span>) </span>&#123;
<span class="hljs-keyword">var</span> me = <span class="hljs-built_in">this</span>;
<span class="hljs-keyword">var</span> args = <span class="hljs-built_in">Array</span>.prototype.slice.call(<span class="hljs-built_in">arguments</span>, <span class="hljs-number">1</span>);
<span class="hljs-keyword">var</span> F = <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params"></span>)</span>&#123;&#125;
F.prototype=<span class="hljs-built_in">this</span>.prototype
<span class="hljs-keyword">var</span> bound = <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params"></span>) </span>&#123;
<span class="hljs-built_in">console</span>.log(<span class="hljs-built_in">this</span>, <span class="hljs-string">"this"</span>)
<span class="hljs-keyword">var</span> innerArgs = <span class="hljs-built_in">Array</span>.prototype.slice.call(<span class="hljs-built_in">arguments</span>);
<span class="hljs-keyword">var</span> finalArgs = args.concat(innerArgs);
<span class="hljs-keyword">return</span> me.apply(<span class="hljs-built_in">this</span> <span class="hljs-keyword">instanceof</span> me ? <span class="hljs-built_in">this</span> : context || <span class="hljs-built_in">this</span>, finalArgs);
&#125;
bound.prototype = <span class="hljs-keyword">new</span> F(); <span class="hljs-comment">// // 修改返回函数的 prototype 为绑定函数的 prototype，实例就可以继承绑定函数的原型中的值</span>
<span class="hljs-keyword">return</span> bound;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>输出如下:bar的原型链没有被污染
<img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/ca6ae3b105ca40029c437e0d9248d360~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>上面call,apply,bind函数实现得差不多了，感谢<a href="https://juejin.cn/post/6844903476477034510#heading-0" target="_blank" title="https://juejin.cn/post/6844903476477034510#heading-0">[冴羽]</a>大佬的文章。</p></div>  
</div>
            