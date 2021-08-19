
---
title: '【前端--面试】常见面试题（四）—— JavaScript'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=4978'
author: 掘金
comments: false
date: Thu, 19 Aug 2021 01:56:12 GMT
thumbnail: 'https://picsum.photos/400/300?random=4978'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;color:#383838;font-size:15px;line-height:37.5px;letter-spacing:2px;word-break:break-word;font-family:-apple-system,BlinkMacSystemFont,Segoe UI,Roboto,Oxygen,Ubuntu,Cantarell,Open Sans,Helvetica Neue,sans-serif;scroll-behavior:smooth;background-image:linear-gradient(0deg,transparent 24%,rgba(201,195,195,.329) 25%,hsla(0,8%,80.4%,.05) 26%,transparent 27%,transparent 74%,hsla(0,5.2%,81%,.185) 75%,rgba(180,176,176,.05) 76%,transparent 77%,transparent),linear-gradient(90deg,transparent 24%,rgba(204,196,196,.226) 25%,hsla(0,4%,66.1%,.05) 26%,transparent 27%,transparent 74%,hsla(0,5.2%,81%,.185) 75%,rgba(180,176,176,.05) 76%,transparent 77%,transparent);background-color:#fff;background-size:50px 50px;padding-bottom:120px&#125;.markdown-body ::selection&#123;color:#fff;background-color:#a862ea&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;margin:30px 0 15px;color:#a862ea&#125;.markdown-body h1&#123;line-height:2;font-size:1.4em&#125;.markdown-body h1~p:first-of-type:first-letter&#123;color:#a862ea;float:left;font-size:2em;margin-right:.4em;font-weight:bolder&#125;.markdown-body h2&#123;font-size:1.2em&#125;.markdown-body h3&#123;font-size:1.1em&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:2em&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;padding-left:.2em&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:10px&#125;.markdown-body li::marker&#123;color:#a862ea&#125;.markdown-body li,.markdown-body p&#123;opacity:.9;vertical-align:baseline;transition:all .1s ease&#125;.markdown-body li:hover,.markdown-body p:hover&#123;opacity:1&#125;.markdown-body a&#123;display:inline-block;color:#a862ea;cursor:pointer;padding-bottom:2px;text-decoration:none;position:relative&#125;.markdown-body a:after&#123;content:"";position:absolute;width:98%;height:2px;bottom:0;left:0;transform:scaleX(0);background-color:#a862ea;transform-origin:bottom right;transition:transform .3s ease-in-out&#125;.markdown-body a:hover:after&#123;transform:scaleX(1);transform-origin:bottom left&#125;.markdown-body a:active,.markdown-body a:link&#123;color:#a862ea&#125;.markdown-body img&#123;max-width:100%;user-select:none;margin:1em 0;box-shadow:0 0 20px 0 #e7daff;transition:transform .2s ease 0s;background-color:#f8f5ff&#125;.markdown-body img:hover&#123;opacity:1;transform:translateY(-2px)&#125;.markdown-body blockquote&#123;padding:.5em 1em;margin:15px 0;border-top-left-radius:2px;border-bottom-left-radius:2px;border-left:4px solid #a862ea;background-color:#f8f5ff&#125;.markdown-body blockquote>p&#123;margin:0&#125;.markdown-body code&#123;padding:2px .4em;overflow-x:auto;color:#a862ea;font-weight:700;word-break:break-word;font-family:Operator Mono,Consolas,Monaco,Menlo,monospace;background-color:#f8f5ff&#125;.markdown-body pre&#123;margin:2em 0;box-shadow:0 0 20px #e7daff&#125;.markdown-body pre>code&#123;display:block;padding:1.5em;word-break:normal;font-size:.9em;font-style:normal;font-weight:400;font-family:Operator Mono,Consolas,Monaco,Menlo,monospace;line-height:22.5px;color:#383838;border-radius:3px;scroll-behavior:smooth&#125;.markdown-body pre>code::-webkit-scrollbar&#123;height:6px;background-color:#f8f5ff&#125;.markdown-body pre>code::-webkit-scrollbar-thumb&#123;background-color:#e7daff;border-bottom-left-radius:3px;border-bottom-right-radius:3px&#125;.markdown-body hr&#123;margin:2em 0;border-top:1px solid #a862ea&#125;.markdown-body table&#123;font-size:12px;max-width:100%;overflow:auto;border-collapse:collapse;border:1px solid #e7daff&#125;.markdown-body thead&#123;color:#a862ea;background:#f8f5ff&#125;.markdown-body td,.markdown-body th&#123;padding:1em .5em&#125;.markdown-body tr&#123;background-color:#fcfcfc&#125;@media (max-width:720px)&#123;.markdown-body&#123;font-size:12px&#125;&#125;</style><p>这是我参与8月更文挑战的第16天，活动详情查看：<a href="https://juejin.cn/post/6987962113788493831" title="https://juejin.cn/post/6987962113788493831" target="_blank">8月更文挑战</a></p>
<blockquote>
<p>做题啦，做题啦~~</p>
</blockquote>
<h3 data-id="heading-0">continue问题</h3>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">for</span> (<span class="hljs-keyword">let</span> i = <span class="hljs-number">1</span>; i < <span class="hljs-number">5</span>; i++) &#123;
  <span class="hljs-keyword">if</span> (i === <span class="hljs-number">3</span>) <span class="hljs-keyword">continue</span>;
  <span class="hljs-built_in">console</span>.log(i);
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>A: <code>1</code> <code>2</code></li>
<li>B: <code>1</code> <code>2</code> <code>3</code></li>
<li>C: <code>1</code> <code>2</code> <code>4</code></li>
<li>D: <code>1</code> <code>3</code> <code>4</code></li>
</ul>
<p><strong>答案: C</strong></p>
<p>这里<code>for</code>循环中，当i等于3的时候，<code>continue</code>就跳过迭代。</p>
<h3 data-id="heading-1">构造函数问题</h3>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-built_in">String</span>.prototype.giveMyFood = <span class="hljs-function">() =></span> &#123;
  <span class="hljs-keyword">return</span> <span class="hljs-string">"Please give weirui food!"</span>;
&#125;;

<span class="hljs-keyword">const</span> name = <span class="hljs-string">"weirui"</span>;

name.giveMyFood();
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>A: <code>"Please give weirui food!"</code></li>
<li>B: <code>TypeError: not a function</code></li>
<li>C: <code>SyntaxError</code></li>
<li>D: <code>undefined</code></li>
</ul>
<p><strong>答案: A</strong></p>
<p><code>String</code>是一个内置的构造函数，我们可以为它添加一些属性。 在这里给它的原型添加了一个方法。 原始类型的字符串自动转换为字符串对象，由字符串原型函数生成。 因此，所有字符串（字符串对象）都可以访问该方法！</p>
<p>当使用基本类型的字符串调用<code>giveMyFood</code>时，实际上发生了下面的过程：</p>
<ul>
<li>创建一个<code>String</code>的包装类型实例</li>
<li>在实例上调用<code>substring</code>方法</li>
<li>销毁实例</li>
</ul>
<h3 data-id="heading-2">类型转换</h3>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> a = &#123;&#125;;
<span class="hljs-keyword">const</span> b = &#123; <span class="hljs-attr">key</span>: <span class="hljs-string">"b"</span> &#125;;
<span class="hljs-keyword">const</span> c = &#123; <span class="hljs-attr">key</span>: <span class="hljs-string">"c"</span> &#125;;

a[b] = <span class="hljs-number">123</span>;
a[c] = <span class="hljs-number">456</span>;

<span class="hljs-built_in">console</span>.log(a[b]);
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>A: <code>123</code></li>
<li>B: <code>456</code></li>
<li>C: <code>undefined</code></li>
<li>D: <code>ReferenceError</code></li>
</ul>
<p><strong>答案: B</strong>
对象键自动转换成了字符串，开始将一个对象设置为对象a的键，值为123，当对象自动转换为字符串时候，就变成了[Object object]，所以说是<code>a["Object object"] = 123</code>。<code>c</code>对象同样也发生了隐式类型转换。那么，<code>a["Object object"] = 456</code>。这时候我们打印<code>a[b]</code>，它实际上是<code>a["Object object"]</code>，因此返回<code>456</code>。</p>
<h3 data-id="heading-3">call bind问题</h3>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> person = &#123; <span class="hljs-attr">name</span>: <span class="hljs-string">"weirui"</span> &#125;;

<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">sayHi</span>(<span class="hljs-params">age</span>) </span>&#123;
  <span class="hljs-built_in">console</span>.log(<span class="hljs-string">`<span class="hljs-subst">$&#123;<span class="hljs-built_in">this</span>.name&#125;</span> is <span class="hljs-subst">$&#123;age&#125;</span>`</span>);
&#125;

sayHi.call(person, <span class="hljs-number">24</span>);
sayHi.bind(person, <span class="hljs-number">24</span>);
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>A: <code>undefined is 21</code>  <code>Lydia is 21</code></li>
<li>B: <code>function</code>  <code>function</code></li>
<li>C: <code>Lydia is 21</code>  <code>Lydia is 21</code></li>
<li>D: <code>Lydia is 21</code>  <code>function</code></li>
</ul>
<p><strong>答案: D</strong></p>
<p>我们传递<code>this</code>关键字引用的对象， 但是，<code>.call</code>方法会立即执行，</p>
<p><code>.bind</code>方法会返回函数的拷贝值，但带有绑定的上下文，不会立即执行。</p>
<h3 data-id="heading-4">类型判断</h3>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">sayHi</span>(<span class="hljs-params"></span>) </span>&#123;
  <span class="hljs-keyword">return</span> (<span class="hljs-function">() =></span> <span class="hljs-number">0</span>)();
&#125;

<span class="hljs-keyword">typeof</span> sayHi();
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>A: <code>"object"</code></li>
<li>B: <code>"number"</code></li>
<li>C: <code>"function"</code></li>
<li>D: <code>"undefined"</code></li>
</ul>
<p><strong>答案: B</strong></p>
<p><code>sayHi</code>函数返回立即调用的函数的返回值。 该函数返回<code>0</code>，类型为<code>number</code>。</p>
<blockquote>
<p>JavaScript有7种内置类型：<code>null</code>，<code>undefined</code>，<code>boolean</code>，<code>number</code>，<code>string</code>，<code>object</code>和<code>symbol</code>。 <code>function</code>不是一个类型，因为函数是对象，它的类型是<code>object</code>。</p>
</blockquote>
<p>再来看一个类型判断的问题：</p>
<p><strong>哪些值是假值？</strong></p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-number">0</span>;
<span class="hljs-keyword">new</span> <span class="hljs-built_in">Number</span>(<span class="hljs-number">0</span>);
(<span class="hljs-string">""</span>);
(<span class="hljs-string">" "</span>);
<span class="hljs-keyword">new</span> <span class="hljs-built_in">Boolean</span>(<span class="hljs-literal">false</span>);
<span class="hljs-literal">undefined</span>;
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>A: <code>0</code>, <code>''</code>, <code>undefined</code></li>
<li>B: <code>0</code>, <code>new Number(0)</code>, <code>''</code>, <code>new Boolean(false)</code>, <code>undefined</code></li>
<li>C: <code>0</code>, <code>''</code>, <code>new Boolean(false)</code>, <code>undefined</code></li>
<li>D: 所有都是假值</li>
</ul>
<p><strong>答案: A</strong></p>
<p><code>JavaScript</code>中只有6个假值：</p>
<ul>
<li><code>undefined</code></li>
<li><code>null</code></li>
<li><code>NaN</code></li>
<li><code>0</code></li>
<li><code>''</code> (empty string)</li>
<li><code>false</code></li>
</ul>
<p>函数构造函数，如<code>new Number</code>和<code>new Boolean</code>都是真值。</p></div>  
</div>
            