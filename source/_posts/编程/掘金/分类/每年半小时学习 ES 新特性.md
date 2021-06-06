
---
title: '每年半小时学习 ES 新特性'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=811'
author: 掘金
comments: false
date: Fri, 04 Jun 2021 07:02:35 GMT
thumbnail: 'https://picsum.photos/400/300?random=811'
---

<div>   
<div class="markdown-body"><style>@charset "UTF-8";.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1:first-child,.markdown-body h2:first-child,.markdown-body h3:first-child,.markdown-body h4:first-child,.markdown-body h5:first-child,.markdown-body h6:first-child&#123;margin-top:-1.5rem;margin-bottom:1rem&#125;.markdown-body h1:before,.markdown-body h2:before,.markdown-body h3:before,.markdown-body h4:before,.markdown-body h5:before,.markdown-body h6:before&#123;content:"#";display:inline-block;color:#3eaf7c;padding-right:.23em&#125;.markdown-body h1&#123;position:relative;font-size:2.5rem;margin-bottom:5px&#125;.markdown-body h1:before&#123;font-size:2.5rem&#125;.markdown-body h2&#123;padding-bottom:.5rem;font-size:2.2rem;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:1.5rem;padding-bottom:0&#125;.markdown-body h4&#123;font-size:1.25rem&#125;.markdown-body h5&#123;font-size:1rem&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body strong&#123;color:#3eaf7c&#125;.markdown-body img&#123;max-width:100%;border-radius:2px;display:block;margin:auto;border:3px solid rgba(62,175,124,.2)&#125;.markdown-body hr&#123;border:none;border-top:1px solid #3eaf7c;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;overflow-x:auto;padding:.2rem .5rem;margin:0;color:#3eaf7c;font-weight:700;font-size:.85em;background-color:rgba(27,31,35,.05);border-radius:3px&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75;border-radius:6px;border:2px solid #3eaf7c&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;font-weight:500;text-decoration:none;color:#3eaf7c&#125;.markdown-body a:active,.markdown-body a:hover&#123;border-bottom:1.5px solid #3eaf7c&#125;.markdown-body a:before&#123;content:"⇲"&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #3eaf7c&#125;.markdown-body thead&#123;background:#3eaf7c;color:#fff;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:rgba(62,175,124,.2)&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:.5rem solid;border-color:#42b983;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body details&#123;outline:none;border:none;border-left:4px solid #3eaf7c;padding-left:10px;margin-left:4px&#125;.markdown-body details summary&#123;cursor:pointer;border:none;outline:none;background:#fff;margin:0 -17px&#125;.markdown-body details summary::-webkit-details-marker&#123;color:#3eaf7c&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body ol li::marker&#123;color:#3eaf7c&#125;.markdown-body ul li&#123;list-style:none&#125;.markdown-body ul li:before&#123;content:"•";margin-right:4px;color:#3eaf7c&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><blockquote>
<p>这是我参与更文挑战的第4天，活动详情查看：<a href="https://juejin.cn/post/6967194882926444557" target="_blank">更文挑战</a></p>
</blockquote>
<p>先简单了解一下 ECMAScript 跟 JavaScript 的关系。ECMAScript 是语言规范，JavaScript 是该规范的一种实现。我们通常认为 JavaScript 等价于 ECMAScript，但完整的 JavaScript 实现实际包含了三部分：核心（ECMAScript）、文档对象模型（DOM）、浏览器对象模型（BOM）。</p>
<p>我们在使用 JavaScript 开发项目时如果遇到问题，通常利用 Google 或者 stack overflow 都能获得解答。但当我们通过常规的方式无法获得想要的结果时，就应该查询规范了，不妨在 <a href="https://tc39.es/ecma262/" target="_blank" rel="nofollow noopener noreferrer">ECMA-262</a> 全局搜索一下试试~</p>
<p>ES6 有比较大的改动，建议翻阅阮一峰的 《ES6 入门教程》进行详细学习。在 ES6 之后，ECMAScript 每年都会有少量新特性增加。而对我们来说，只要每年花上半小时，足以充分学习并掌握这些新增特性。</p>
<p>ES7~ ES11相关内容可以参看<a href="https://coffe1891.gitbook.io/frontend-hard-mode-interview/1/1.1.1" target="_blank" rel="nofollow noopener noreferrer">前端内参</a>。</p>
<h2 data-id="heading-0">ES12</h2>
<h3 data-id="heading-1">String.prototype.replaceAll</h3>
<p>该方法将字符串内所有符合匹配规则的字符替换掉，返回一个全新的字符串。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">let</span> str = <span class="hljs-string">'Hello, world'</span>;
str.replaceAll(<span class="hljs-string">'l'</span>, <span class="hljs-string">''</span>); <span class="hljs-comment">// "Heo, word"</span>
<span class="hljs-comment">// 相当于</span>
str.replace(<span class="hljs-regexp">/l/g</span>, <span class="hljs-string">''</span>);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>需要注意的是如果该方法的匹配规则是正则表达式，需要有 g 标识符，不然会报错。</p>
<pre><code class="hljs language-js copyable" lang="js">str1.replaceAll(<span class="hljs-regexp">/l/</span>, <span class="hljs-string">''</span>);  <span class="hljs-comment">// TypeError: String.prototype.replaceAll called with a non-global RegExp argument</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-2">Promise.any</h3>
<p>接受一个项全为 promise 的数组，当其中任意一个 promise 成功 resolve 就返回第一个 resolve 的结果，如果所有都失败则抛出异常。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-built_in">Promise</span>.any([
  <span class="hljs-keyword">new</span> <span class="hljs-built_in">Promise</span>(<span class="hljs-function">(<span class="hljs-params">resolve, reject</span>) =></span> <span class="hljs-built_in">setTimeout</span>(reject, <span class="hljs-number">1000</span>, <span class="hljs-string">'我是第一个 promise'</span>)),
  <span class="hljs-keyword">new</span> <span class="hljs-built_in">Promise</span>(<span class="hljs-function">(<span class="hljs-params">resolve, reject</span>) =></span> <span class="hljs-built_in">setTimeout</span>(resolve, <span class="hljs-number">2000</span>, <span class="hljs-string">'我是第二个 promise'</span>)),
  <span class="hljs-keyword">new</span> <span class="hljs-built_in">Promise</span>(<span class="hljs-function">(<span class="hljs-params">resolve, reject</span>) =></span> <span class="hljs-built_in">setTimeout</span>(resolve, <span class="hljs-number">3000</span>, <span class="hljs-string">'我是第三个 promise'</span>)),
])
.then(<span class="hljs-function"><span class="hljs-params">value</span> =></span> <span class="hljs-built_in">console</span>.log(value)) <span class="hljs-comment">// 我是第二个 promise</span>
.catch (<span class="hljs-function"><span class="hljs-params">err</span> =></span> <span class="hljs-built_in">console</span>.log(err))

<span class="hljs-comment">//---------------------</span>
<span class="hljs-built_in">Promise</span>.any([
  <span class="hljs-built_in">Promise</span>.reject(),
  <span class="hljs-built_in">Promise</span>.reject(),
  <span class="hljs-built_in">Promise</span>.reject()
])
.then(<span class="hljs-function"><span class="hljs-params">value</span> =></span> <span class="hljs-built_in">console</span>.log(value))
.catch (<span class="hljs-function"><span class="hljs-params">err</span> =></span> <span class="hljs-built_in">console</span>.log(err)) <span class="hljs-comment">//AggregateError: All promises were rejected</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-3">WeakRefs</h3>
<p>这个提案主要包括两个主要的新功能：</p>
<ul>
<li>使用 WeakRef 类创建对象的弱引用</li>
<li>使用 FinalizationRegistry 类对对象进行垃圾回收后，运行用户定义的终结器</li>
</ul>
<p>它们可以分开使用，也可以一起使用。</p>
<p><code>WeakRef</code> 对象包含对对象的弱引用，这个弱引用被称为该 WeakRef 对象的 target 或者是 referent。对对象的弱引用是指当该对象应该被 GC 回收时不会阻止 GC 的回收行为。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">let</span> ref = <span class="hljs-keyword">new</span> WeakRef(obj)
<span class="hljs-keyword">let</span> isLive = ref.deref() <span class="hljs-comment">// 如果 obj 被垃圾回收了，那么 isLive 就是 undefined</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p><code>FinalizationRegistry</code> 能力：当一个在注册表中注册的对象被回收时，请求在某个时间点上调用一个清理回调。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> registry = <span class="hljs-keyword">new</span> FinalizationRegistry(<span class="hljs-function"><span class="hljs-params">heldValue</span> =></span> &#123;
  <span class="hljs-comment">// ....</span>
&#125;);

<span class="hljs-comment">// 通过 register 方法，注册任何你想要清理回调的对象，传入该对象和 heldValue</span>
registry.register(theObject, <span class="hljs-string">"some value"</span>);
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-4">Logical Assignment Operators（逻辑赋值操作符）</h3>
<p>新增了三个逻辑赋值操作符，如下所示：</p>
<pre><code class="hljs language-js copyable" lang="js">a ||= b;
<span class="hljs-comment">// 等价于</span>
a || (a = b);

a &&= b;
<span class="hljs-comment">// 等价于</span>
a && (a = b);

a ??= b;
<span class="hljs-comment">// 等价于</span>
a ?? (a = b);
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-5">Numeric separators（数字分割符）</h3>
<p>可以在数字之间增加可视化分隔符，通过下划线 <code>_</code> 来分割数字，增加可读性。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">let</span> budget = <span class="hljs-number">1_000_000_000_000</span>;
budget === <span class="hljs-number">10</span> ** <span class="hljs-number">12</span>; <span class="hljs-comment">// true</span>

<span class="hljs-keyword">let</span> nibbles = <span class="hljs-number">0b1010_0001_1000_0101</span>;
<span class="hljs-built_in">console</span>.log(!!(nibbles & (<span class="hljs-number">1</span> << <span class="hljs-number">7</span>))); <span class="hljs-comment">// true</span>
<span class="copy-code-btn">复制代码</span></code></pre></div>  
</div>
            