
---
title: '【面试说】怪异的 JavaScript'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=3289'
author: 掘金
comments: false
date: Sun, 04 Jul 2021 17:13:07 GMT
thumbnail: 'https://picsum.photos/400/300?random=3289'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h2 data-id="heading-0">前言</h2>
<p>在网上看到一个有趣的测试，<a href="https://jsisweird.com/" target="_blank" rel="nofollow noopener noreferrer">访问地址</a>。里面包含了 25 道选择题，每个都是一个简单的表达式，然后让你选择，都是一些 JavaScript 怪异行为的体现，最后网站生成答案和解析，帮助你更好的理解 JavaScript 怪异的行为。</p>
<p>这里我分享 10 道我认为有趣的，希望对大家有所帮助</p>
<h2 data-id="heading-1">测试</h2>
<ol>
<li>
<p><code>[,,,].length</code></p>
<p>a. 0
b. 3
c. 4
d. SyntaxError</p>
</li>
<li>
<p>10,2</p>
<p>a. 10.2
b. 10
c. 2
d. 20</p>
</li>
<li>
<p>true == "true"</p>
<p>a. true
b. false</p>
</li>
<li>
<p>010 - 03</p>
<p>a. 7
b. 5
c. 3
d. NaN</p>
</li>
<li>
<p><strong>1/0 > Math.pow(10, 1000)</strong></p>
<p>a. true
b. false
c. NaN
d. SyntaxError</p>
</li>
<li>
<p><strong>0/0</strong></p>
<p>a. 0
b. Infinity
c. NaN
d. SyntaxError</p>
</li>
<li>
<p><strong>true++</strong></p>
<p>a. 2
b. undefined
c. NaN
d. SyntaxError</p>
</li>
<li>
<p>true + ("true" - 0)</p>
<p>a. 1
b. 2
c. NaN
d. SyntaxError</p>
</li>
<li>
<p><strong>undefined + false</strong></p>
<p>a. "undefinedfalse"
b. 0
c. NaN
d. SyntaxError</p>
</li>
<li>
<p><strong>NaN++</strong></p>
<p>a. NaN
b. Undefined
c. TypeError
d. SyntaxError</p>
</li>
</ol>
<h2 data-id="heading-2">答案</h2>
<ol>
<li>
<p><code>[,,,].length</code></p>
<ol>
<li>0</li>
<li>3</li>
<li>4</li>
<li>SyntaxError</li>
</ol>
<p>解析：b。稀疏数组，<code>[,,]</code> 中间的元素为 <code>empty</code> ，这种我们就称为稀疏数组，我们也可以通过类似 new Array(2) 的方式创建稀疏数组。那为什么不是 4 而是 3 呢？这个跟 JavaScript 的<a href="https://developer.mozilla.org/zh-CN/docs/Web/JavaScript/Reference/Trailing_commas" target="_blank" rel="nofollow noopener noreferrer">尾后逗号</a> (Trailing commas) 有关。MDN 中的解析如下：</p>
<blockquote>
<p><strong>尾后逗号</strong> （有时叫做 “终止逗号”）在向 JavaScript 代码添加元素、参数、属性时十分有用。如果你想要添加新的属性，并且上一行已经使用了尾后逗号，你可以仅仅添加新的一行，而不需要修改上一行。这使得版本控制的代码比较（diff）更加清晰，代码编辑过程中遇到的麻烦更少。</p>
</blockquote>
<p>其实这个在我们平时写对象的时候用得比较多（假如 ESlint 允许的话）。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">var</span> object = &#123;
  <span class="hljs-attr">foo</span>: <span class="hljs-string">"bar"</span>,
  <span class="hljs-attr">baz</span>: <span class="hljs-string">"qwerty"</span>,
  <span class="hljs-attr">age</span>: <span class="hljs-number">42</span>, <span class="hljs-comment">// 注意</span>
&#125;;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>其实数组中也一样，这样就不难理解上面的输出了。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">var</span> arr = [
  <span class="hljs-number">1</span>,
  <span class="hljs-number">2</span>,
  <span class="hljs-number">3</span>,
];

arr; <span class="hljs-comment">// [1, 2, 3]</span>
arr.length; <span class="hljs-comment">// 3</span>
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
<li>
<p>10,2</p>
<ol>
<li>10.2</li>
<li>10</li>
<li>2</li>
<li>20</li>
</ol>
<p>解析：c。逗号操作符只返回最后一个操作符的值。这允许你创建一个复合表达式，在其中计算多个表达式，复合表达式为最后一个表达式的值。在 for  循环中可能会用到。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">for</span> (<span class="hljs-keyword">var</span> i = <span class="hljs-number">0</span>, j = <span class="hljs-number">9</span>; i <= <span class="hljs-number">9</span>; i++, j--)
  <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'a['</span> + i + <span class="hljs-string">']['</span> + j + <span class="hljs-string">'] = '</span> + a[i][j]);
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">myFunc</span>(<span class="hljs-params"></span>) </span>&#123;
  <span class="hljs-keyword">var</span> x = <span class="hljs-number">0</span>;

  <span class="hljs-keyword">return</span> (x += <span class="hljs-number">1</span>, x); <span class="hljs-comment">// the same as return ++x;</span>
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
<li>
<p>true == "true"</p>
<ol>
<li>true</li>
<li>false</li>
</ol>
<p>解析：b。根据隐式类型转换的规则。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-built_in">Number</span>(<span class="hljs-literal">true</span>); <span class="hljs-comment">// -> 1</span>
<span class="hljs-built_in">Number</span>(<span class="hljs-string">"true"</span>); <span class="hljs-comment">// -> NaN</span>
<span class="hljs-number">1</span> == <span class="hljs-literal">NaN</span>; <span class="hljs-comment">// -> false</span>
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
<li>
<p>010 - 03</p>
<ol>
<li>7</li>
<li>5</li>
<li>3</li>
<li>NaN</li>
</ol>
<p>解析：b。010 被 JavaScript 视为八进制数。因此，它的值是以8为基数的。010 被解析成 8，减 3 得 5。</p>
</li>
<li>
<p><strong>1/0 > Math.pow(10, 1000)</strong></p>
<ol>
<li>true</li>
<li>false</li>
<li>NaN</li>
<li>SyntaxError</li>
</ol>
<p>解析：b。两个表达式都是 Infinity。Infinity 两者相等。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-number">1</span>/<span class="hljs-number">0</span>; <span class="hljs-comment">// -> Infinity</span>
<span class="hljs-built_in">Math</span>.pow(<span class="hljs-number">10</span>, <span class="hljs-number">1000</span>); <span class="hljs-comment">// -> Infinity</span>
<span class="hljs-literal">Infinity</span> > <span class="hljs-literal">Infinity</span>; <span class="hljs-comment">// -> false</span>
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
<li>
<p><strong>0/0</strong></p>
<ol>
<li>0</li>
<li>Infinity</li>
<li>NaN</li>
<li>SyntaxError</li>
</ol>
<p>解析：由于等式 <code>0/0</code> 是没有有意义的数值答案，输出简单地是 <code>NaN</code>。</p>
</li>
<li>
<p><strong>true++</strong></p>
<ol>
<li>2</li>
<li>undefined</li>
<li>NaN</li>
<li>SyntaxError</li>
</ol>
<p>解析：d。会存在以下的怪异行为，undefined 不会报错。【这里我也找不到合适的理由去解释】。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-number">1</span>++; <span class="hljs-comment">// -> SyntaxError</span>
<span class="hljs-string">"x"</span>++; <span class="hljs-comment">// -> SyntaxError</span>
<span class="hljs-literal">undefined</span>++; <span class="hljs-comment">// -> NaN</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>假如要使它不报错的话，就得：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">let</span> x = <span class="hljs-literal">true</span>;
x++;
x; <span class="hljs-comment">// -> 2</span>
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
<li>
<p>true + ("true" - 0)</p>
<ol>
<li>1</li>
<li>2</li>
<li>NaN</li>
<li>SyntaxError</li>
</ol>
<p>解析：同 3。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-built_in">Number</span>(<span class="hljs-string">"true"</span>); <span class="hljs-comment">// -> NaN</span>
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
<li>
<p><strong>undefined + false</strong></p>
<ol>
<li>"undefinedfalse"</li>
<li>0</li>
<li>NaN</li>
<li>SyntaxError</li>
</ol>
<p>解析：<code>false</code> 可以转换为数字，<code>undefined</code> 不能。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-built_in">Number</span>(<span class="hljs-literal">false</span>); <span class="hljs-comment">// -> 0</span>
<span class="hljs-built_in">Number</span>(<span class="hljs-literal">undefined</span>); <span class="hljs-comment">// -> NaN</span>
<span class="hljs-literal">NaN</span> + <span class="hljs-number">0</span>; <span class="hljs-comment">// -> NaN</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>但是 undefined 又可以转换成 false。</p>
<pre><code class="hljs language-js copyable" lang="js">!!<span class="hljs-literal">undefined</span> === <span class="hljs-literal">false</span>; <span class="hljs-comment">// -> true</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>所以要以上为 0。应该：</p>
<pre><code class="hljs language-js copyable" lang="js">!!<span class="hljs-literal">undefined</span> + <span class="hljs-literal">false</span>; <span class="hljs-comment">// -> 0</span>
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
<li>
<p><strong>NaN++</strong></p>
<ol>
<li>NaN</li>
<li>Undefined</li>
<li>TypeError</li>
<li>SyntaxError</li>
</ol>
<p>答案：a。<code>NaN</code> 不是一个数字，所以它不能递增。这也意味着 <code>NaN</code> 和 <code>NaN++</code> 表示相同的值。</p>
</li>
</ol>
<h2 data-id="heading-3">结语</h2>
<p>Javascript 之所以有以上怪异表现，主要是初期设计过于匆忙，1995 年仅用用了 10 天来完成的。可能上面的行为我们用得不多，但了解它们对于我们更加深入了解 JavaScript 也是有所帮助。所以强烈建议大家去做一些这 <a href="https://jsisweird.com/" target="_blank" rel="nofollow noopener noreferrer">25 道题目</a>，感受一下。</p></div>  
</div>
            