
---
title: '深入理解js数据类型与堆栈内存'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/1d7f2dbf817a411b86cf484764bfe844~tplv-k3u1fbpfcp-zoom-1.image'
author: 掘金
comments: false
date: Tue, 23 Mar 2021 08:03:57 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/1d7f2dbf817a411b86cf484764bfe844~tplv-k3u1fbpfcp-zoom-1.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h2 data-id="heading-0">前言</h2>
<p>在JavaScript中，它的内存分为三种类型：代码空间、栈空间、堆空间，其中代码空间用于存放可执行代码。</p>
<p>本文带大家来深入理解下栈空间与堆空间（堆内存与栈内存），欢迎各位感兴趣的开发者阅读本文。</p>
<h2 data-id="heading-1">理解数据类型</h2>
<p>最新的 ECMAScript 标准定义了 9 种数据类型:</p>
<ul>
<li>6 种<a href="https://developer.mozilla.org/en-US/docs/Glossary/Primitive" target="_blank" rel="nofollow noopener noreferrer">原始类型</a>，使用 <a href="https://developer.mozilla.org/en-US/docs/Glossary/typeof" target="_blank" rel="nofollow noopener noreferrer">typeof</a> 运算符检查
<ul>
<li><a href="https://developer.mozilla.org/en-US/docs/Glossary/undefined" target="_blank" rel="nofollow noopener noreferrer">undefined</a>：<code>typeof instance === "undefined"</code></li>
<li><a href="https://developer.mozilla.org/en-US/docs/Glossary/Boolean" target="_blank" rel="nofollow noopener noreferrer">Boolean</a>：<code>typeof instance === "boolean"</code></li>
<li><a href="https://developer.mozilla.org/en-US/docs/Glossary/Number" target="_blank" rel="nofollow noopener noreferrer">Number</a>：<code>typeof instance === "number"</code></li>
<li><a href="https://developer.mozilla.org/en-US/docs/Glossary/String" target="_blank" rel="nofollow noopener noreferrer">String</a>：<code>typeof instance === "string</code></li>
<li><a href="https://developer.mozilla.org/en-US/docs/Glossary/BigInt" target="_blank" rel="nofollow noopener noreferrer">BigInt</a>：<code>typeof instance === "bigint"</code></li>
<li><a href="https://developer.mozilla.org/en-US/docs/Glossary/Symbol" target="_blank" rel="nofollow noopener noreferrer">Symbol</a> ：<code>typeof instance === "symbol"</code></li>
</ul>
</li>
<li><a href="https://developer.mozilla.org/en-US/docs/Glossary/Null" target="_blank" rel="nofollow noopener noreferrer">null</a>：<code>typeof instance === "object"</code></li>
<li><a href="https://developer.mozilla.org/en-US/docs/Glossary/Object" target="_blank" rel="nofollow noopener noreferrer">Object</a>：<code>typeof instance === "object"</code>，任何构造函数对象实例的特殊非数据结构类型，也用做数据结构：new <a href="https://developer.mozilla.org/en-US/docs/Glossary/Object" target="_blank" rel="nofollow noopener noreferrer">Object</a>，new <a href="https://developer.mozilla.org/en-US/docs/Glossary/array" target="_blank" rel="nofollow noopener noreferrer">Array</a>，new <a href="https://developer.mozilla.org/en-US/docs/Glossary/Map" target="_blank" rel="nofollow noopener noreferrer">Map</a>，new <a href="https://developer.mozilla.org/en-US/docs/Glossary/Set" target="_blank" rel="nofollow noopener noreferrer">Set</a>，new <a href="https://developer.mozilla.org/en-US/docs/Glossary/WeakMap" target="_blank" rel="nofollow noopener noreferrer">WeakMap</a>，new <a href="https://developer.mozilla.org/en-US/docs/Glossary/WeakSet" target="_blank" rel="nofollow noopener noreferrer">WeakSet</a>，new <a href="https://developer.mozilla.org/en-US/docs/Glossary/Date" target="_blank" rel="nofollow noopener noreferrer">Date</a>，和几乎所有通过<code>new</code>关键词创建的东西。</li>
<li><a href="https://developer.mozilla.org/en-US/docs/Glossary/Function" target="_blank" rel="nofollow noopener noreferrer">Function</a>：非数据结构，尽管 typeof 操作的结果是：<code>typeof instance === "function"</code>。这个结果是为 Function 的一个特殊缩写，尽管每个 Function 构造器都由 Object 构造器派生。</li>
</ul>
<blockquote>
<p><code>typeof</code> 操作符的唯一目的就是检查数据类型，如果我们希望检查任何从 Object 派生出来的结构类型，使用 <code>typeof</code> 是不起作用的，因为总是会得到 <code>"object"</code>。检查 Object 种类的合适方式是使用 <a href="https://developer.mozilla.org/en-US/docs/Glossary/instanceof" target="_blank" rel="nofollow noopener noreferrer">instanceof</a> 关键字。但即使这样也存在误差。</p>
</blockquote>
<h3 data-id="heading-2">动态类型</h3>
<p>JavaScript 是一种<strong>弱类型</strong>或者说<strong>动态</strong>语言。我们不需要提前声明变量的类型，在程序运行过程中，类型会被自动确定。这也意味着我们可以使用同一个变量保存不同类型的数据：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">var</span> info = <span class="hljs-string">"字符串类型"</span>; <span class="hljs-comment">// string类型</span>
info = <span class="hljs-number">20</span>; <span class="hljs-comment">// number类型</span>
info = <span class="hljs-literal">true</span>; <span class="hljs-comment">// boolean类型</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-3">隐式转换</h3>
<ul>
<li><code>+</code>和<code>-</code>运算符转换</li>
</ul>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-built_in">console</span>.log(<span class="hljs-string">"20"</span> + <span class="hljs-number">6</span>) <span class="hljs-comment">// "106" 字符串拼接 string + number = string</span>
<span class="hljs-built_in">console</span>.log(<span class="hljs-string">"16"</span> - <span class="hljs-number">6</span>) <span class="hljs-comment">// 10 减法运算 string - number = number</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>比较运算符</li>
</ul>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">// ==（等于），会自动转换数据类型再比较</span>
<span class="hljs-comment">// ===（严格等于），不会自动转换数据类型，如果数据类型不一致，返回false；如果一致，再比较。</span>
<span class="hljs-literal">false</span> == <span class="hljs-number">0</span>; <span class="hljs-comment">// true</span>
<span class="hljs-literal">false</span> === <span class="hljs-number">0</span>; <span class="hljs-comment">// false</span>
<span class="hljs-literal">undefined</span> == <span class="hljs-literal">null</span>; <span class="hljs-comment">// true，（undefined是null的子集）</span>

<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>NaN（Not a Number）这个特殊的Number与所有其他值都不相等，包括它自己：</li>
</ul>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-literal">NaN</span> === <span class="hljs-literal">NaN</span>; <span class="hljs-comment">// false</span>
<span class="hljs-built_in">isNaN</span>(<span class="hljs-literal">NaN</span>);  <span class="hljs-comment">// true (isNaN() 函数用于判断NaN)</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>浮点数相等比较</li>
</ul>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-number">1</span> / <span class="hljs-number">3</span> === (<span class="hljs-number">1</span> - <span class="hljs-number">2</span> / <span class="hljs-number">3</span>); <span class="hljs-comment">// false</span>
<span class="hljs-comment">// 浮点数在运算过程中会产生误差，因为计算机无法精确表示无限循环小数。要比较两个浮点数是否相等，只能计算它们之差的绝对值，看是否小于某个阈值</span>
<span class="hljs-built_in">Math</span>.abs(<span class="hljs-number">1</span> / <span class="hljs-number">3</span> - (<span class="hljs-number">1</span> - <span class="hljs-number">2</span> / <span class="hljs-number">3</span>)) < <span class="hljs-number">0.0000001</span>; <span class="hljs-comment">// true</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-4">包装对象</h3>
<p>在JavaScript中，<strong>一切皆对象</strong>。
<code>Array</code>（数组）和 <code>Function</code>（函数）本质上都是对象，就连三种原始类型的值 — — <code>Number</code>（数值）、<code>String</code>（字符串）、<code>Boolean</code>（布尔值） — — 在一定条件下，也会自动转为对象，也就是原始类型的 <strong>包装对象</strong>。</p>
<p>一般来说，只有对象是可以对属性进行读写操作的，但是我们平常用的很多的字符串方法和属性，都是通过<code>.</code>操作符访问的，例如：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-built_in">console</span>.log(<span class="hljs-string">"神奇的程序员"</span>.length);
<span class="hljs-built_in">console</span>.log(<span class="hljs-string">"我是大白"</span>.indexOf(<span class="hljs-string">"白"</span>));
<span class="copy-code-btn">复制代码</span></code></pre>
<p>如上述代码所示，在我们调用这些方法和属性时，<strong>JS内部已经隐式地帮我们帮创建了一个包装对象</strong>了，上述代码JS在运行时会处理成这样：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-built_in">console</span>.log(<span class="hljs-keyword">new</span> <span class="hljs-built_in">String</span>(<span class="hljs-string">"神奇的程序员"</span>).length);
<span class="hljs-built_in">console</span>.log(<span class="hljs-keyword">new</span> <span class="hljs-built_in">String</span>(<span class="hljs-string">"我是大白"</span>).indexOf(<span class="hljs-string">"白"</span>));
<span class="copy-code-btn">复制代码</span></code></pre>
<p>浏览器自己隐式创建的包装对象和我们显式创建的包装对象不严格相等，我们举个例子说明下：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">var</span> name =  <span class="hljs-string">"神奇的程序员"</span>;
<span class="hljs-keyword">var</span> info = <span class="hljs-keyword">new</span> <span class="hljs-built_in">String</span>(<span class="hljs-string">"神奇的程序员"</span>);
<span class="hljs-built_in">console</span>.log(name == info);    <span class="hljs-comment">// true</span>
<span class="hljs-built_in">console</span>.log(name === info);   <span class="hljs-comment">// false</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>运行结果如下：</p>
<p><img alt="image-20210323224807378" class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/1d7f2dbf817a411b86cf484764bfe844~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-5">类型检测</h3>
<p>接下来我们来学习下js中几个常用的类型检测方法。</p>
<h4 data-id="heading-6">typeof运算符</h4>
<p><code>typeof</code>可以检测变量的数据类型，返回如下6种字符串<code>number</code>、<code>string</code>、<code>boolean</code>、<code>object</code>、<code>undefined</code>、<code>function</code></p>
<p>我们举个例子说明下：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">var</span> age = <span class="hljs-number">1</span>;
<span class="hljs-built_in">console</span>.log(<span class="hljs-keyword">typeof</span> age);  <span class="hljs-comment">// number</span>

<span class="hljs-keyword">var</span> info = <span class="hljs-literal">undefined</span>;
<span class="hljs-built_in">console</span>.log(<span class="hljs-keyword">typeof</span> info);  <span class="hljs-comment">// undefined</span>

<span class="hljs-keyword">var</span> title = <span class="hljs-literal">null</span>;
<span class="hljs-built_in">console</span>.log(<span class="hljs-keyword">typeof</span> title);  <span class="hljs-comment">// object，（null是空对象引用/或者说指针）。</span>

<span class="hljs-keyword">var</span> obj = <span class="hljs-keyword">new</span> <span class="hljs-built_in">Object</span>();
<span class="hljs-built_in">console</span>.log(<span class="hljs-keyword">typeof</span> obj);  <span class="hljs-comment">// object</span>

<span class="hljs-keyword">var</span> arr = [<span class="hljs-number">1</span>,<span class="hljs-number">2</span>,<span class="hljs-number">3</span>];
<span class="hljs-built_in">console</span>.log(<span class="hljs-keyword">typeof</span> arr);  <span class="hljs-comment">// object </span>

<span class="hljs-keyword">var</span> fn = <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params"></span>)</span>&#123;&#125;
<span class="hljs-built_in">console</span>.log(<span class="hljs-keyword">typeof</span> fn);  <span class="hljs-comment">// function</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>运行结果如下：</p>
<p><img alt="image-20210323224959529" class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/a4b082306c0b409c8efb320edd27f7e6~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<h4 data-id="heading-7">instanceof运算符</h4>
<ul>
<li>
<p><code>instanceof</code>，用于检测某个对象的原型链是否包含某个构造函数的 <code>prototype</code> 属性。</p>
</li>
<li>
<p><code>instanceof</code> 适用于检测对象，它是基于原型链运作的。</p>
</li>
</ul>
<ul>
<li><code>instanceof</code> 除了适用于任何 <code>object</code> 的类型检查之外，也可以用来检测内置对象，比如：<code>Array</code>、<code>RegExp</code>、<code>Object</code>、<code>Function</code></li>
<li><code>instanceof</code> 对基本数据类型检测不起作用，主要是因为基本数据类型没有原型链。</li>
</ul>
<p>我们举个例子来说明下：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-built_in">console</span>.log([<span class="hljs-number">1</span>, <span class="hljs-number">2</span>, <span class="hljs-number">3</span>] <span class="hljs-keyword">instanceof</span> <span class="hljs-built_in">Array</span>); <span class="hljs-comment">// true</span>
<span class="hljs-built_in">console</span>.log(<span class="hljs-regexp">/abc/</span> <span class="hljs-keyword">instanceof</span> <span class="hljs-built_in">RegExp</span>); <span class="hljs-comment">// true</span>
<span class="hljs-built_in">console</span>.log(&#123;&#125; <span class="hljs-keyword">instanceof</span> <span class="hljs-built_in">Object</span>); <span class="hljs-comment">// true</span>
<span class="hljs-built_in">console</span>.log(<span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params"></span>) </span>&#123;&#125; <span class="hljs-keyword">instanceof</span> <span class="hljs-built_in">Function</span>); <span class="hljs-comment">// true</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>运行结果如下：</p>
<p><img alt="image-20210323225421217" class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/ba3878100af244feabf3c9d35e40ea82~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<h4 data-id="heading-8">constructor属性</h4>
<p>构造函数属性,可确定当前对象的构造函数，我们举个例子说明下：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">var</span> o = <span class="hljs-keyword">new</span> <span class="hljs-built_in">Object</span>();
<span class="hljs-built_in">console</span>.log(o.constructor == <span class="hljs-built_in">Object</span>); <span class="hljs-comment">// true</span>
<span class="hljs-keyword">var</span> arr = <span class="hljs-keyword">new</span> <span class="hljs-built_in">Array</span>();
<span class="hljs-built_in">console</span>.log(arr.constructor == <span class="hljs-built_in">Array</span>); <span class="hljs-comment">// true</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>运行结果如下：</p>
<p><img alt="image-20210323225557196" class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/7c7badd068914067a9aa8545086cd476~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<h4 data-id="heading-9">hasOwnProperty属性</h4>
<p>判断属性是否存在于当前对象实例中（而不是原型对象中），我们举个例子来说明下：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">const</span> info = &#123; <span class="hljs-attr">title</span>: <span class="hljs-string">"书"</span>, <span class="hljs-attr">name</span>: <span class="hljs-string">"大白"</span> &#125;;
<span class="hljs-built_in">console</span>.log(info.hasOwnProperty(<span class="hljs-string">"title"</span>)); <span class="hljs-comment">// true</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>运行结果如下：</p>
<p><img alt="image-20210323225809992" class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/a25f6d1556004b70900e4adb56f0bbca~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-10">堆栈内存空间</h2>
<p>接下来，我们看下什么是堆、栈内存空间。</p>
<h3 data-id="heading-11">栈内存空间</h3>
<p>见名知意，<strong>栈内存空间</strong> 就是用栈作为数据结构在内存中所申请的空间。</p>
<p>对栈这种数据结构不了解的开发者，请移步我的另一篇文章：<a href="https://juejin.cn/post/6844904069102829581" target="_blank">数据结构:栈与队列</a>。</p>
<p>我们来回顾下<strong>栈</strong>的特点：</p>
<ul>
<li>后进先出，最后添加进栈的元素最先出。</li>
<li>访问栈底元素，必须拿掉它上面的元素。</li>
</ul>
<p>我们画个图来描述下栈，如下所示：</p>
<p><img alt="image-20210323113726313" class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/5631876df7b34b1cbe19f10ff5fe7b1a~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-12">堆内存空间</h3>
<p>同样的，见名知意，<strong>堆内存空间</strong>就是用堆作为数据结构在内存中所申请的空间。</p>
<p>对堆这种数据结构不了解的开发者，请移步我的另外两篇文章：<a href="https://juejin.cn/post/6844904070969294856" target="_blank">数据结构:堆</a>、<a href="https://juejin.cn/post/6854573211197046791" target="_blank">实现二叉堆</a></p>
<p>通常情况下，我们所说的 <strong>堆</strong> 数据结构指的是 <strong>二叉堆</strong> ，我们来回顾下二叉堆的特点：</p>
<ul>
<li>它是一颗完全二叉树</li>
<li>二叉堆不是最小堆就是最大堆</li>
</ul>
<p>我们画个图来描述下 <strong>最大堆</strong> 与 <strong>最小堆</strong> ，如下所示：</p>
<p><img alt="image-20210323134717994" class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/0ec50917e0fa48bcbd75544575160814~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-13">变量类型与堆栈内存的关系</h2>
<h3 data-id="heading-14">基本数据类型</h3>
<p>我们知道JS的基本数据类型有7种：</p>
<ul>
<li><code>string</code></li>
<li><code>number</code></li>
<li><code>boolean</code></li>
<li><code>null</code></li>
<li><code>undefined</code></li>
<li><code>symbol</code></li>
<li><code>bigInt</code></li>
</ul>
<p>基本数据类型变量保存在栈内存中，因为基本数据类型占用空间小、大小固定，通过值来访问，属于被频繁使用的数据。</p>
<p>接下来，我们通过一个例子来讲解下，基本数据类型在栈内存中的存储：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">let</span> name = <span class="hljs-string">"大白"</span>;
<span class="hljs-keyword">let</span> age = <span class="hljs-number">20</span>;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>上述代码中，我们定义了2个变量：</p>
<ul>
<li>name为<code>string</code>类型</li>
<li>age为<code>number</code>类型</li>
</ul>
<p>我们画个图来描述下它在栈内存的存储：</p>
<p><img alt="image-20210323152445985" class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/5dbc0fe6fefb4b838cd22ea0a9f48e36~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<blockquote>
<p>注意⚠️：闭包中的基本数据类型变量是保存在堆内存里的，当函数执行完弹出调用栈后，返回一个内部函数的一个引用，这时候函数的变量就会转移到堆上，因此内部函数依然能访问到上一层函数的变量。</p>
</blockquote>
<h3 data-id="heading-15">引用数据类型</h3>
<p>除了上个章节提到的基本数据类型外，其他的都属于引用数据类型，例如：<code>Array</code>、<code>Function</code>、<code>Object</code>等。</p>
<p>引用数据类型存储在堆内存中，引用数据类型占据空间大、大小不固定，如果存储在栈中，将影响程序的运行性能。</p>
<p>引用数据类型会在栈中存储一个指针，这个指针指向堆内存空间中该实体的起始地址。</p>
<p>当解释器寻找引用值时，会先检索其在栈中的地址，取得地址后，从堆中获得实体。</p>
<p>我们举个例子来描述下上述话语：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">// 基本数据类型-栈内存</span>
<span class="hljs-keyword">let</span> name = <span class="hljs-string">"大白"</span>;
<span class="hljs-comment">// 基本数据类型-栈内存</span>
<span class="hljs-keyword">let</span> age = <span class="hljs-number">20</span>;
<span class="hljs-comment">// 基本数据类型-栈内存</span>
<span class="hljs-keyword">let</span> info = <span class="hljs-literal">null</span>;
<span class="hljs-comment">// 对象指针存放在栈内存中，指针指向的对象放在堆内存中</span>
<span class="hljs-keyword">let</span> msgObj = &#123;<span class="hljs-attr">msg</span>: <span class="hljs-string">"测试"</span>, <span class="hljs-attr">id</span>: <span class="hljs-number">5</span>&#125;;
<span class="hljs-comment">// 数组的指针存放在栈内存中，指针指向的数组存放在堆内存中</span>
<span class="hljs-keyword">let</span> ages = [<span class="hljs-number">19</span>, <span class="hljs-number">22</span>, <span class="hljs-number">57</span>]
<span class="copy-code-btn">复制代码</span></code></pre>
<p>上述代码中：</p>
<ul>
<li>我们创建了两个变量<code>msgObj</code>、<code>ages</code>，他们的值都是引用类型(object、array)</li>
<li>堆内存空间采用<code>二叉堆</code>作为数据结构，<code>msgObj</code>与<code>ages</code>的具体值会存在堆内存空间中</li>
<li>存储完成后，堆内存空间会返回这两个值的引用地址(指针)</li>
<li>拿到引用地址后，这个引用地址会和它的变量名对应起来，存放在栈内存空间中</li>
<li>在查找变量<code>msgObj</code>与<code>ages</code>的具体值时，会先从栈内存空间中获取它的引用地址</li>
<li>获取到引用地址后，通过引用地址在堆内存空间的二叉堆中查找到对应的值。</li>
</ul>
<p>我们画个图来描述下上述话语，如下所示：</p>
<p>堆内存空间中的<code>Object</code>，表示的是存储在空间中的其他对象的引用值。</p>
<p><img alt="image-20210323170843691" class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/18fbd5bf395a42e5b6757c84a4768be7~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<blockquote>
<p>我们来理解下堆内存空间与堆内存的区别：</p>
<p>堆内存空间：相当于一个采用二叉堆作为数据结构的容器。</p>
<p>堆内存：指的是一个引用类型的具体值。</p>
<p>堆内存存在于堆内存空间中。</p>
</blockquote>
<h2 data-id="heading-16">变量复制</h2>
<p>接下来，我们从内存角度来看下变量复制。</p>
<h3 data-id="heading-17">基本数据类型的复制</h3>
<p>我们通过一个例子来看下基本类型的复制，代码如下所示：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">let</span> name = <span class="hljs-string">"神奇的程序员"</span>;
<span class="hljs-keyword">let</span> alias = name;
alias = <span class="hljs-string">"大白"</span>;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>上述代码中：</p>
<ul>
<li><code>name</code>、<code>alias</code>都是基本类型，它们的值存储在栈内存。</li>
<li>它们分别有各自独立的栈空间</li>
<li>因此，修改<code>alias</code>的值，<code>name</code>不受影响</li>
</ul>
<p>我们画个图来描述下：</p>
<p><img alt="image-20210323203531067" class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/a62044e6cc31425b997800b3df2a559f~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-18">引用数据类型的复制</h3>
<p>接下来，我们通过一个例子来看下引用类型的复制，代码如下所示：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">let</span> book = &#123;<span class="hljs-attr">title</span>:<span class="hljs-string">"书"</span>, <span class="hljs-attr">id</span>: <span class="hljs-number">12</span>&#125;
<span class="hljs-keyword">let</span> info = book;
info.title = <span class="hljs-string">"故事书"</span>;
<span class="hljs-built_in">console</span>.log(book.title); <span class="hljs-comment">// 故事书</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>上述代码中：</p>
<ul>
<li><code>info</code>、<code>book</code>都是引用类型，它们的引用存在栈内存，值存在堆内存</li>
<li>它们的值指向同一块堆内存，栈内存中会复制一份相同的引用</li>
</ul>
<p>我们画个图来描述下：</p>
<p><img alt="image-20210323213720148" class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/2eb62499c51742e7a13b1ea6a51aa517~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-19">深拷贝与浅拷贝</h2>
<p>通过上述章节的学习，我们了解到引用数据类型在复制时，改了其中一个数据的值，另一个数据的值也会跟着改变，这种拷贝方式我们称为<strong>浅拷贝</strong>。</p>
<p>在实际开发中，我们希望引用类型复制到新的变量后，二者是独立的，不会因为一个的改变而影响到另一个。这种拷贝方式就称为<strong>深拷贝</strong>。</p>
<p>深拷贝，实际上就是重新在堆内存中开辟一块新的空间，把原对象的数据拷贝到这个新地址空间里来，通常来说，我们有两种方法：</p>
<ul>
<li>转一遍JSON再转回来 ,但是这个办法有一个问题，这只能转化一般常见数据，function，undefined等类型都无法通过这种变回来</li>
<li>手动去写循环遍历</li>
</ul>
<p>我们来看下第一种方法，代码如下所示：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">const</span> data = &#123; <span class="hljs-attr">name</span>: <span class="hljs-string">"大白"</span> &#125;;
<span class="hljs-keyword">const</span> obj = <span class="hljs-built_in">JSON</span>.parse(<span class="hljs-built_in">JSON</span>.stringify(data));
obj.age = <span class="hljs-number">20</span>;
<span class="hljs-built_in">console</span>.log(<span class="hljs-string">"data = "</span>, data);
<span class="hljs-built_in">console</span>.log(<span class="hljs-string">"obj = "</span>, obj);

<span class="copy-code-btn">复制代码</span></code></pre>
<p>运行结果如下：</p>
<p><img alt="image-20210323233500632" class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/c17c86de9bc344c7a27b925ad60c3da0~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p>最后，我们来看下第二种写法，代码如下所示：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">const</span> data = [&#123; <span class="hljs-attr">name</span>: <span class="hljs-string">"大白"</span> &#125;];
<span class="hljs-keyword">let</span> obj = data.map(<span class="hljs-function"><span class="hljs-params">item</span> =></span> item);
obj.push(&#123; <span class="hljs-attr">name</span>: <span class="hljs-string">"神奇的程序员"</span> &#125;);
<span class="hljs-built_in">console</span>.log(<span class="hljs-string">"data = "</span>, data);
<span class="hljs-built_in">console</span>.log(<span class="hljs-string">"obj = "</span>, obj);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>运行结果如下：</p>
<p><img alt="image-20210323234043404" class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/f02821520c204054890dc517c5e0d011~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-20">代码地址</h2>
<p>本文为《JS原理学习》系列的第4篇文章，本系列的完整路线请移步：<a href="https://juejin.cn/post/6937688619503058974" target="_blank">JS原理学习 (1) 》学习路线规划</a></p>
<p>本系列文章的所有示例代码，请移步：<a href="https://github.com/likaia/js-learning" target="_blank" rel="nofollow noopener noreferrer">js-learning</a></p>
<h2 data-id="heading-21">写在最后</h2>
<p>至此，文章就分享完毕了。</p>
<p>我是<strong>神奇的程序员</strong>，一位前端开发工程师。</p>
<p>如果你对我感兴趣，请移步我的<a href="https://www.kaisir.cn/" target="_blank" rel="nofollow noopener noreferrer">个人网站</a>，进一步了解。</p>
<ul>
<li>文中如有错误，欢迎在评论区指正，如果这篇文章帮到了你，欢迎点赞和关注😊</li>
<li>本文首发于掘金，未经许可禁止转载💌</li>
</ul></div> <div class="image-viewer-box" data-v-78c9b824><!----></div>  
</div>
            