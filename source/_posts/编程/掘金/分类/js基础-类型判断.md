
---
title: 'js基础-类型判断'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=6377'
author: 掘金
comments: false
date: Mon, 05 Jul 2021 20:20:43 GMT
thumbnail: 'https://picsum.photos/400/300?random=6377'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h1 data-id="heading-0">类型判断</h1>
<p>数据类型应该算得上是 js 的基础第一课。在日常的开发中会遇到很多类型判断和类型转换的场景。</p>
<h2 data-id="heading-1">数据类型</h2>
<p>js中的数据类型分为基本类型和引用类型：</p>
<ul>
<li>基本类型
Number、Boolean、undefined、null、BigInt、String、Symbol</li>
<li>引用类型
Object、Function、Array、RegExp、Date</li>
</ul>
<h3 data-id="heading-2">基本类型和引用类型的不同</h3>
<p>基本类型的值是不可变的，引用类型的值是可变的。
在复制时：基本类型复制的是值，引用类型复制的是引用。
在比较时：基本类型只用比较值，引用类型需要同时比较引用地址和值。</p>
<h3 data-id="heading-3">数据存储</h3>
<p>在 js 中基本类型存储在栈内存中，引用类型存储在堆内存中。这是因为栈的存取速度相当快，仅次于 cpu 中寄存器的存取速度。</p>
<h2 data-id="heading-4">类型判断</h2>
<h3 data-id="heading-5">typeof - 基本类型的判断方法</h3>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">typeof</span> <span class="hljs-string">"s"</span>; <span class="hljs-comment">// "string"</span>
<span class="hljs-keyword">typeof</span> &#123; <span class="hljs-attr">x</span>: <span class="hljs-number">1</span> &#125;; <span class="hljs-comment">// "object"</span>
<span class="hljs-keyword">typeof</span> [<span class="hljs-number">1</span>, <span class="hljs-number">2</span>, <span class="hljs-number">3</span>]; <span class="hljs-comment">// "object"</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>tips: 关于 typeof 的一个历史 bug</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">typeof</span> <span class="hljs-literal">null</span>; <span class="hljs-comment">// 'object'</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>typeof 方法只能精确判断基本类型，对于引用类型的判断都为 “object”。</p>
<h3 data-id="heading-6">instanceof - 引用类型的判断方法</h3>
<p>instanceof 用于检测构造函数的 prototype 属性是否出现在某个实例对象的原型链上。
a instanceof b ,a 是否为 b 的实例。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">var</span> a = &#123; <span class="hljs-attr">x</span>: <span class="hljs-number">1</span> &#125;;
<span class="hljs-keyword">var</span> b = [<span class="hljs-number">1</span>, <span class="hljs-number">2</span>, <span class="hljs-number">3</span>];
<span class="hljs-keyword">var</span> c = <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params"></span>) </span>&#123;
  <span class="hljs-built_in">console</span>.log(<span class="hljs-string">"aa"</span>);
&#125;;
connsole.log(a <span class="hljs-keyword">instanceof</span> <span class="hljs-built_in">Object</span>); <span class="hljs-comment">// true</span>
<span class="hljs-built_in">console</span>.log(b <span class="hljs-keyword">instanceof</span> <span class="hljs-built_in">Array</span>); <span class="hljs-comment">// true</span>
<span class="hljs-built_in">console</span>.log(c <span class="hljs-keyword">instanceof</span> <span class="hljs-built_in">Function</span>); <span class="hljs-comment">// true</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>tips：不能检测 null 和 undefined。
instanceof 方法可以精确判断 引用类型 的数据类型；</p>
<h3 data-id="heading-7">constructor</h3>
<p>查询对象的构造函数</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">getConstructor</span>(<span class="hljs-params">obj</span>) </span>&#123;
  <span class="hljs-keyword">let</span> a = obj;
  <span class="hljs-keyword">return</span> a.constructor;
&#125;
getConstructor(<span class="hljs-number">1</span>);
<span class="hljs-comment">// ƒ Number() &#123; [native code] &#125;</span>
getConstructor(<span class="hljs-string">""</span>);
<span class="hljs-comment">// ƒ String() &#123; [native code] &#125;</span>
getConstructor(<span class="hljs-literal">false</span>);
<span class="hljs-comment">// ƒ Boolean() &#123; [native code] &#125;</span>
getConstructor(<span class="hljs-built_in">Symbol</span>(<span class="hljs-number">1</span>));
<span class="hljs-comment">// ƒ Symbol() &#123; [native code] &#125;</span>
getConstructor(<span class="hljs-built_in">BigInt</span>(<span class="hljs-number">1</span>));
<span class="hljs-comment">// ƒ BigInt() &#123; [native code] &#125;</span>
getConstructor(<span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params"></span>) </span>&#123;&#125;);
<span class="hljs-comment">// ƒ Function() &#123; [native code] &#125;</span>
getConstructor(<span class="hljs-keyword">new</span> <span class="hljs-built_in">Date</span>());
<span class="hljs-comment">// ƒ Date() &#123; [native code] &#125;</span>
getConstructor(<span class="hljs-regexp">/a/</span>);
<span class="hljs-comment">// ƒ RegExp() &#123; [native code] &#125;</span>
getConstructor(&#123;&#125;);
<span class="hljs-comment">// ƒ Object() &#123; [native code] &#125;</span>
getConstructor([]);
<span class="hljs-comment">// ƒ Array() &#123; [native code] &#125;</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-8">原型方法</h3>
<p>Object.prototype.toString.call()</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-built_in">Object</span>.prototype.toString.call(<span class="hljs-string">"xx"</span>); <span class="hljs-comment">// "[object String]"</span>
<span class="hljs-built_in">Object</span>.prototype.toString.call([<span class="hljs-number">12</span>, <span class="hljs-number">3</span>]); <span class="hljs-comment">// "[object Array]"</span>
<span class="hljs-built_in">Object</span>.prototype.toString.call(&#123; <span class="hljs-attr">x</span>: <span class="hljs-number">1</span> &#125;); <span class="hljs-comment">// "[object Object]"</span>
<span class="hljs-built_in">Object</span>.prototype.toString.call(<span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params"></span>) </span>&#123;&#125;); <span class="hljs-comment">//"[object Function]"</span>
<span class="hljs-built_in">Object</span>.prototype.toString.call(<span class="hljs-literal">true</span>); <span class="hljs-comment">// "[object Boolean]"</span>
<span class="hljs-built_in">Object</span>.prototype.toString.call(<span class="hljs-literal">null</span>); <span class="hljs-comment">// "[object Null]"</span>
<span class="hljs-built_in">Object</span>.prototype.toString.call(<span class="hljs-number">1</span>); <span class="hljs-comment">// "[object Number]"</span>
<span class="hljs-built_in">Object</span>.prototype.toString.call(<span class="hljs-literal">undefined</span>); <span class="hljs-comment">// "[object Undefined]"</span>
<span class="hljs-built_in">Object</span>.prototype.toString.call(<span class="hljs-keyword">new</span> <span class="hljs-built_in">Date</span>()); <span class="hljs-comment">// "[object Date]"</span>
<span class="hljs-built_in">Object</span>.prototype.toString.call(<span class="hljs-keyword">new</span> <span class="hljs-built_in">RegExp</span>()); <span class="hljs-comment">// "[object RegExp]"</span>
<span class="hljs-built_in">Object</span>.prototype.toString.call(<span class="hljs-built_in">BigInt</span>(<span class="hljs-number">2</span>)); <span class="hljs-comment">// "[object BigInt]"</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>总结
js 中数据类型的判断方法，typeof 常被用于检测基本类型，instanceof 常被用于检测引用类型， Object.prototype.toString 这种方法算是通用方法，实际开发中也是我最喜欢使用的。</li>
</ul>
<h2 data-id="heading-9">类型转换</h2>
<p>以下场景会触发类型转换：</p>
<ul>
<li>if 条件语句</li>
<li>三目表达式等逻辑语句</li>
<li>==、+、-、*等运算算符</li>
</ul>
<h2 data-id="heading-10">开发中值得注意的点</h2>
<ol>
<li>Number有最大限制:</li>
</ol>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// 通过Number.MAX_VALUE访问，超过此值计算时会丢失精度</span>
<span class="hljs-built_in">Number</span>.MAX_VALUE <span class="hljs-comment">// 1.7976931348623157e+308</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<ol start="2">
<li>二进制转十进制：</li>
</ol>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-built_in">parseInt</span>(<span class="hljs-string">'1010'</span>, <span class="hljs-number">2</span>) <span class="hljs-comment">// 10</span>
<span class="hljs-built_in">parseInt</span>(<span class="hljs-string">'a'</span>, <span class="hljs-number">12</span>) <span class="hljs-comment">// 10</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<ol start="3">
<li>十进制转二进制：</li>
</ol>
<pre><code class="hljs language-js copyable" lang="js">(<span class="hljs-number">10</span>).toString(<span class="hljs-number">2</span>)  <span class="hljs-comment">// "1010"</span>
(<span class="hljs-number">10</span>).toString(<span class="hljs-number">12</span>) <span class="hljs-comment">// "a"</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>哇哦，奇妙的知识又增加了！姐妹们get起来吧！</p></div>  
</div>
            