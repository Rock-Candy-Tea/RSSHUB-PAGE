
---
title: 'Javascript 类型解读'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=1770'
author: 掘金
comments: false
date: Fri, 09 Jul 2021 23:50:56 GMT
thumbnail: 'https://picsum.photos/400/300?random=1770'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>大多数开发者认为，像JavaScript这样的动态语言是没有类型的</p>
<p>实则ECMAScript 类型细分为语言类型 和 规范类型</p>
<p>ECMAScript 语言中所有的值都有一个对应的语言类型</p>
<p><code>Undefined</code>
<code>Null</code>
<code>Boolean</code>
<code>String</code>
<code>Number</code>
<code>Object</code></p>
<p>对于JavaScript 来说，我们可以定义 “类型”:
对于语言引擎和开发人员来说，类型是值得内部特征，它定义了值得行为，以使其区别于其他值</p>
<p>全面掌握 JavaScript的类型之后，我们旨在改变对强制类型转换的成见，看到它的好处并且意识到它的缺点被过分夸大了</p>
<h3 data-id="heading-0">内置类型</h3>
<h5 data-id="heading-1">JavaScript 有 7 种内置类型：</h5>
<ul>
<li>空值 null</li>
<li>未定义 undefined</li>
<li>布尔值 boolean</li>
<li>数字 number</li>
<li>字符串 string</li>
<li>对象 object</li>
<li>符号 symbol</li>
</ul>
<p>除对象之外，其他统称为 基本类型</p>
<blockquote>
<p>typeof 运算符查看值得类型，它返回的是类型的字符串值</p>
</blockquote>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">typeof</span> <span class="hljs-literal">undefined</span> === <span class="hljs-string">"undefined"</span>
<span class="hljs-keyword">typeof</span> <span class="hljs-literal">true</span> === <span class="hljs-string">"boolean"</span>
<span class="hljs-keyword">typeof</span> <span class="hljs-number">42</span> === <span class="hljs-string">"number"</span>
<span class="hljs-keyword">typeof</span> <span class="hljs-string">"42"</span> === <span class="hljs-string">"string"</span>
<span class="hljs-keyword">typeof</span> &#123; <span class="hljs-attr">life</span>: <span class="hljs-number">42</span> &#125; === <span class="hljs-string">"object"</span>
<span class="hljs-keyword">typeof</span> <span class="hljs-built_in">Symbol</span>() ===  <span class="hljs-string">"symbol"</span>

<span class="hljs-keyword">typeof</span> <span class="hljs-literal">null</span> === <span class="hljs-string">"object"</span>

<span class="hljs-comment">// 我们需要使用复合条件来检测 null 值得类型</span>

<span class="hljs-keyword">var</span> a = <span class="hljs-literal">null</span>
(!a && <span class="hljs-keyword">typeof</span> a === <span class="hljs-string">"object"</span>)

<span class="hljs-keyword">typeof</span> funcrion <span class="hljs-function"><span class="hljs-title">a</span>(<span class="hljs-params"></span>)</span>&#123;&#125; === <span class="hljs-string">"function"</span>

<span class="hljs-keyword">typeof</span> [<span class="hljs-number">1</span>, <span class="hljs-number">2</span>, <span class="hljs-number">3</span>] === <span class="hljs-string">"object"</span> 
<span class="copy-code-btn">复制代码</span></code></pre>
<blockquote>
<p>function (函数) 实际上是 object 的一个 子类型, 具体来说， 函数是 可调用对象  它又一个内部属性[[Call]]，该属性使其可以被调用</p>
</blockquote>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">a</span> (<span class="hljs-params">b, c</span>) </span>&#123;

&#125;
<span class="hljs-comment">// 函数对象的length属性是其声明的参数的个数</span>
a.length === <span class="hljs-number">2</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<blockquote>
<p>数组也是 object 的一个子类型，数组的元素按数字顺序进行索引，而非普通对象那样通过字符串键值，其length 属性是元素的个数</p>
</blockquote>
<h3 data-id="heading-2">值和类型</h3>
<p>JavaScript 中的变量是没有类型的，只有值才有，变量可以随时持有任何类型的值</p>
<p>换个角度来理解就是，JavaScript不做类型强制，语言引擎不要求变量总是持有与其初始值同类型的值</p>
<p>所以，对变量执行 typeof 操作时，得到的结果并不是该变量的类型，而是该变量持有的值得类型，因为 JavaScript 中的变量没有类型</p>
<h5 data-id="heading-3">undefined 和 undeclared</h5>
<p>变量在未持有值的时候为 <code>undefined</code></p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">var</span> a
<span class="hljs-keyword">typeof</span> a <span class="hljs-comment">// undefined</span>

<span class="hljs-keyword">var</span> b = <span class="hljs-number">42</span>
<span class="hljs-keyword">var</span> c 

b = c

<span class="hljs-keyword">typeof</span> b <span class="hljs-comment">// undefined</span>
<span class="hljs-keyword">typeof</span> c <span class="hljs-comment">// undefined</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<blockquote>
<p>已在作用域中声明但还没有赋值的变量，是 <code>undefined</code> 的, 相反，还没有在作用域中声明过的变量，是 <code>undeclared</code>的</p>
</blockquote>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">var</span> a;
a; <span class="hljs-comment">// undefined</span>
b; <span class="hljs-comment">// ReferenceError: b is not defined</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<blockquote>
<p>对于 <code>undeclared</code> 变量，typeof 照样返回 <code>undefined</code>, 这是因为 typeof 又一个特殊的安全防范机制</p>
</blockquote>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">var</span> a;
<span class="hljs-keyword">typeof</span> a; <span class="hljs-comment">// "undefined"</span>
<span class="hljs-keyword">typeof</span> b; <span class="hljs-comment">// "undefined"</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">if</span> (DEBUG) &#123;
    <span class="hljs-built_in">console</span>.log(<span class="hljs-string">"Debugging is starting"</span>)
&#125;

<span class="hljs-keyword">if</span> (<span class="hljs-keyword">typeof</span> DEBUG !== <span class="hljs-string">"undefined"</span>) &#123;
    <span class="hljs-built_in">console</span>.log(<span class="hljs-string">"Debugging is starting"</span>)
&#125;
<span class="copy-code-btn">复制代码</span></code></pre></div>  
</div>
            