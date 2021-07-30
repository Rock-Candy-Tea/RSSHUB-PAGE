
---
title: 'JavaScript中的in运算符与数组'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/3fdafbe7ae7446168033fdab189f3ad4~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Thu, 29 Jul 2021 22:04:15 GMT
thumbnail: 'https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/3fdafbe7ae7446168033fdab189f3ad4~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h2 data-id="heading-0">前言</h2>
<p>JavaScript中有很多怪异点，这个in运算符后接数组就很奇特（虽然大家很少用到这个）。语义上讲in是个介词，词性prep，表示在什么什么里面。但在js中可能就不太一样了。</p>
<h2 data-id="heading-1">问题引出</h2>
<p>不慌，先来看看python中的效果。</p>
<pre><code class="hljs language-python copyable" lang="python"><span class="hljs-meta">>>> </span>array = [<span class="hljs-number">1</span>,<span class="hljs-number">2</span>,<span class="hljs-number">3</span>,<span class="hljs-number">4</span>]
<span class="hljs-meta">>>> </span><span class="hljs-number">0</span> <span class="hljs-keyword">in</span> array
<span class="hljs-literal">False</span>
<span class="hljs-meta">>>> </span><span class="hljs-number">4</span> <span class="hljs-keyword">in</span> array
<span class="hljs-literal">True</span>
<span class="hljs-meta">>>> </span><span class="hljs-number">4.0</span> <span class="hljs-keyword">in</span> array
<span class="hljs-literal">True</span>
<span class="hljs-meta">>>> </span>4n <span class="hljs-keyword">in</span> array
SyntaxError: invalid syntax

<span class="copy-code-btn">复制代码</span></code></pre>
<p>显然，此处in就是表示判断左边的元素是否存在与数组中。</p>
<pre><code class="hljs language-python copyable" lang="python"><span class="hljs-meta">>>> </span><span class="hljs-number">4</span>==<span class="hljs-number">4.0</span>
<span class="hljs-literal">True</span>
<span class="hljs-meta">>>> </span>array.append(<span class="hljs-string">'5'</span>)
<span class="hljs-meta">>>> </span><span class="hljs-number">5</span> <span class="hljs-keyword">in</span> array
<span class="hljs-literal">False</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>挨个匹配的，如果相等则返回True，显然字符串‘5’和数字5并不相等。非常合理是不是。</p>
<p>再来看看浏览器中的情况。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">let</span> a = [<span class="hljs-number">1</span>,<span class="hljs-number">2</span>,<span class="hljs-number">3</span>,<span class="hljs-number">4</span>];
<span class="hljs-number">1</span> <span class="hljs-keyword">in</span> a;<span class="hljs-comment">//true  合理</span>

<span class="hljs-number">1.0</span> <span class="hljs-keyword">in</span> a;<span class="hljs-comment">//true</span>
<span class="hljs-number">0</span> <span class="hljs-keyword">in</span> a;<span class="hljs-comment">//true  合理吗？</span>
<span class="hljs-string">'1'</span> <span class="hljs-keyword">in</span> a;<span class="hljs-comment">//true</span>

<span class="hljs-number">3n</span> <span class="hljs-keyword">in</span> a;<span class="hljs-comment">//true 离谱</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/3fdafbe7ae7446168033fdab189f3ad4~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer">
发生甚么事啦。</p>
<p>一起来研究下。</p>
<h2 data-id="heading-2">数组的本质</h2>
<p>数组Array 时按次序排列的一组值。每个值的位置都有编号（从0开始），整个数组用方括号表示。</p>
<p>任何类型的数组都可以放入数组。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">let</span> array = [a,<span class="hljs-number">2</span>,[<span class="hljs-number">3</span>,<span class="hljs-number">4</span>]];<span class="hljs-comment">// a 是[1,2,3,4]</span>
array
(<span class="hljs-number">3</span>) [<span class="hljs-built_in">Array</span>(<span class="hljs-number">4</span>), <span class="hljs-number">2</span>, <span class="hljs-built_in">Array</span>(<span class="hljs-number">2</span>)]
<span class="copy-code-btn">复制代码</span></code></pre>
<p>数组实际上一种的对象。<code>typeof</code>运算符会返回数组的类型是<code>object</code></p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">typeof</span> a ;<span class="hljs-comment">//"object"</span>
<span class="hljs-built_in">Object</span>.keys(a);<span class="hljs-comment">//(4) ["0", "1", "2", "3"]</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这里可以看出来，数组的键全是字符串数组，从0开始。</p>
<p>来看看对象的设定，js中的规定，对象的键都的是字符串。</p>
<p>当访问对象的值是，有点式object.key和括号式object[key]。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">let</span> ob = &#123;<span class="hljs-string">'0'</span>:<span class="hljs-number">0</span>,<span class="hljs-string">'1'</span>:<span class="hljs-number">1</span>,<span class="hljs-string">'k'</span>:<span class="hljs-string">'v'</span>&#125;;

ob.k ;<span class="hljs-comment">//"v"</span>
ob[<span class="hljs-string">"k"</span>];  
<span class="hljs-string">"v"</span>  <span class="hljs-comment">// 两种都能取值</span>
ob<span class="hljs-number">.0</span>  <span class="hljs-comment">// 报错啦！数字加点，还以为是小数</span>
Uncaught <span class="hljs-built_in">SyntaxError</span>: Unexpected number
ob[<span class="hljs-string">'0'</span>] <span class="hljs-comment">//数字字符串没毛病</span>
<span class="hljs-number">0</span>
ob[<span class="hljs-number">0</span>]  <span class="hljs-comment">//[]内为数字时，也能访问</span>
<span class="hljs-number">0</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>规定</strong>：</p>
<ul>
<li>
<p>点式不能使用数字，否则识别为小数，报错。</p>
</li>
<li>
<p>键名传入非字符串时，会被转为字符串</p>
</li>
</ul>
<p>正因此,数组才能使用数字索引访问。而数组中的键都是字符串。</p>
<h2 data-id="heading-3">in 运算符 与包含</h2>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fdeveloper.mozilla.org%2Fzh-CN%2Fdocs%2FWeb%2FJavaScript%2FReference%2FOperators%2Fin" target="_blank" rel="nofollow noopener noreferrer" title="https://developer.mozilla.org/zh-CN/docs/Web/JavaScript/Reference/Operators/in" ref="nofollow noopener noreferrer">MDN</a>上的解释是这样的:</p>
<p>如果指定的属性在指定的对象或其<strong>原型链</strong>中，则**<code>in</code> 运算符**返回<code>true</code>。</p>
<p>显然这个in并不是包含关系，而是包含该属性。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-string">"toString"</span> <span class="hljs-keyword">in</span> &#123;&#125;; <span class="hljs-comment">//true</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p><code>in</code>右操作数必须是一个对象值，不能是字符串。而左侧需要一个字符串，</p>
<p>当左侧传入不是字符串时，则调用tostring()，转为字符串.</p>
<p>顺带一提，要表达包含关系，可以使用<a href="https://link.juejin.cn/?target=https%3A%2F%2Fdeveloper.mozilla.org%2Fzh-CN%2Fdocs%2FWeb%2FJavaScript%2FReference%2FGlobal_Objects%2FArray%2Fincludes" target="_blank" rel="nofollow noopener noreferrer" title="https://developer.mozilla.org/zh-CN/docs/Web/JavaScript/Reference/Global_Objects/Array/includes" ref="nofollow noopener noreferrer">Array.prototype.includes()</a> ,例如：</p>
<pre><code class="hljs language-js copyable" lang="js">[<span class="hljs-number">1</span>, <span class="hljs-number">2</span>, <span class="hljs-literal">NaN</span>].includes(<span class="hljs-string">'1'</span>);<span class="hljs-comment">//false</span>
[<span class="hljs-number">1</span>, <span class="hljs-number">2</span>, <span class="hljs-literal">NaN</span>].includes(<span class="hljs-number">1.0</span>);<span class="hljs-comment">//true</span>
[<span class="hljs-number">1</span>, <span class="hljs-number">2</span>, <span class="hljs-literal">NaN</span>].includes(<span class="hljs-literal">NaN</span>);<span class="hljs-comment">//true  </span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-4">1.0.toString ()与(1).toString()</h2>
<p>这个问题也是个笔试常考题目。首先是不能写1.toString()，因为有歧义，不知道这个.是小数点，还是调用方法。只要能规避歧义的，都能得到正确的结果。比如:</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-number">1</span> .toString;<span class="hljs-comment">//'1'</span>
(<span class="hljs-number">1</span>).toString();<span class="hljs-comment">//'1'</span>
<span class="hljs-number">1.0</span>.toString();<span class="hljs-comment">//'1'</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>现在的问题是为什么1.0.toString()得到的是字符串'1'，而不是字符串’1.0‘呢？</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-number">1.0</span> === <span class="hljs-number">1</span>;<span class="hljs-comment">//true</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>从存储上来讲，JavaScript数字全部是浮点数。 根据 IEEE 754标准中的64位二进制(binary64), 也称作双精度规范(double precision)来储存。那么1.0===1也合情合理。</p>
<p>在toString ()的实现算法中，是根据数字的大小来将数字解码成字符串的。具体太复杂了，可以看<a href="https://link.juejin.cn/?target=https%3A%2F%2F262.ecma-international.org%2F6.0%2F%23sec-tostring-applied-to-the-number-type" target="_blank" rel="nofollow noopener noreferrer" title="https://262.ecma-international.org/6.0/#sec-tostring-applied-to-the-number-type" ref="nofollow noopener noreferrer">这个</a></p>
<p>因此1.0 或是1.00，乃至是1.0000000000000001.toString() 都是’1‘ （精度不够了）。</p>
<p>那么问题来了，有没有数tostring()可以得到1.0呢？</p>
<p>俺也不知道</p>
<h2 data-id="heading-5">3n是什么？</h2>
<p>前文的内容完全解释了1.0 in a 和’1‘ in a得到true的问题，但是最后一个3n 是什么呢。</p>
<p>答案是ES2020新特性：一个用于处理任意精度整数的新数字基元--n</p>
<p>为了更精确地表示没有位数限制的整数，ES2020引入了<code>不同于Number</code>数字类型的<code>BigInt</code>数字类型， 只用来表示整数（大整数），<code>没有位数的限制</code>，任何位数的整数都可以精确表示。为了与 Number 类型区别，BigInt 类型的数据必须添加后缀<code>n</code>。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">typeof</span> <span class="hljs-number">3n</span> <span class="hljs-comment">//"bigint"</span>
<span class="hljs-number">3n</span> ==<span class="hljs-number">3</span>;<span class="hljs-comment">//true</span>
<span class="hljs-number">3n</span> === <span class="hljs-number">3</span>;<span class="hljs-comment">//false</span>
<span class="hljs-number">3n</span>+<span class="hljs-number">4n</span>;<span class="hljs-comment">//7n</span>
<span class="hljs-number">3n</span>.toString();<span class="hljs-comment">//"3"</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>所以3n in [1,2,3,4] ===true非常合理。</p>
<p>那么1.0n.tostring() 能得到1.0吗？当然，报错了。bigInt只能用于整数。</p>
<p>坐等ES2035修复小数的精度问题。</p>
<h2 data-id="heading-6">最后说下for in</h2>
<p>for in 可以用与遍历，跟in差不多意思，用于遍历得到的是索引。</p>
<p>遍历数组时，当然得到的是字符串而不是数字。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">for</span> (<span class="hljs-keyword">let</span> i <span class="hljs-keyword">in</span> [<span class="hljs-number">1</span>,<span class="hljs-number">2</span>,<span class="hljs-number">3</span>])&#123;<span class="hljs-built_in">console</span>.log(<span class="hljs-number">2</span>+i)&#125;;
<span class="hljs-comment">//20</span>
<span class="hljs-comment">//21</span>
<span class="hljs-comment">//22</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>也能遍历到原型链上的属性。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">let</span> a = [<span class="hljs-number">1</span>,<span class="hljs-number">2</span>,<span class="hljs-number">3</span>,<span class="hljs-number">4</span>];
a.k=<span class="hljs-string">'v'</span>;
<span class="hljs-built_in">Array</span>.prototype.key=<span class="hljs-string">'val'</span>;
<span class="hljs-keyword">for</span> (<span class="hljs-keyword">let</span> i <span class="hljs-keyword">in</span> a)&#123;<span class="hljs-built_in">console</span>.log(i)&#125;;
<span class="hljs-number">0</span>
<span class="hljs-number">1</span>
<span class="hljs-number">2</span>
<span class="hljs-number">3</span>
k
key
<span class="copy-code-btn">复制代码</span></code></pre>
<p>ES6的for of，用于遍历数组。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">for</span> (<span class="hljs-keyword">let</span> i <span class="hljs-keyword">of</span> a)&#123;<span class="hljs-built_in">console</span>.log(i)&#125;
<span class="hljs-number">1</span>
<span class="hljs-number">2</span>
<span class="hljs-number">3</span>
<span class="hljs-number">4</span> <span class="hljs-comment">//到4就结束了，拿不到属性k</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>for of 遍历对象或类数组会报错。</p>
<p>综上：for in 适合遍历对象</p>
<p>for of 遍历数组</p>
<h2 data-id="heading-7">总结</h2>
<p>js中的in不是表示包含关系，而且表示属性存在与否</p>
<p>数组中的属性均为字符串，in运算符判断是存在类型转换</p></div>  
</div>
            