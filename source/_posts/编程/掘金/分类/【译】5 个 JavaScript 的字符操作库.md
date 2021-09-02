
---
title: '【译】5 个 JavaScript 的字符操作库'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://cdn-images-1.medium.com/max/2560/1*pdPTFvogzT9vzmc7k-qY2Q.jpeg'
author: 掘金
comments: false
date: Wed, 01 Sep 2021 03:13:57 GMT
thumbnail: 'https://cdn-images-1.medium.com/max/2560/1*pdPTFvogzT9vzmc7k-qY2Q.jpeg'
---

<div>   
<div class="markdown-body html cache"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><blockquote>
<ul>
<li>原文地址：<a href="https://link.juejin.cn/?target=https%3A%2F%2Fblog.bitsrc.io%2F5-string-manipulation-libraries-for-javascript-9ca5da8b4eb8" target="_blank" rel="nofollow noopener noreferrer" title="https://blog.bitsrc.io/5-string-manipulation-libraries-for-javascript-9ca5da8b4eb8" ref="nofollow noopener noreferrer">5 String Manipulation Libraries for JavaScript</a></li>
<li>原文作者：<a href="https://link.juejin.cn/?target=https%3A%2F%2Fmedium.com%2F%40gitgit6" target="_blank" rel="nofollow noopener noreferrer" title="https://medium.com/@gitgit6" ref="nofollow noopener noreferrer">Mike Chen</a></li>
<li>译文出自：<a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fxitu%2Fgold-miner" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/xitu/gold-miner" ref="nofollow noopener noreferrer">掘金翻译计划</a></li>
<li>本文永久链接：<a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fxitu%2Fgold-miner%2Fblob%2Fmaster%2Farticle%2F2021%2F5-string-manipulation-libraries-for-javascript.md" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/xitu/gold-miner/blob/master/article/2021/5-string-manipulation-libraries-for-javascript.md" ref="nofollow noopener noreferrer">github.com/xitu/gold-m…</a></li>
<li>译者：<a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fjaredliw" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/jaredliw" ref="nofollow noopener noreferrer">jaredliw</a></li>
<li>校对者：<a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2FKimYangOfCat" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/KimYangOfCat" ref="nofollow noopener noreferrer">KimYangOfCat</a></li>
</ul>
</blockquote>
<h1 data-id="heading-0">5 个 JavaScript 的字符操作库</h1>
<p><img src="https://cdn-images-1.medium.com/max/2560/1*pdPTFvogzT9vzmc7k-qY2Q.jpeg" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>处理字符串可能是一项繁琐的任务，因为我们需要考虑许多不同的用例。举例来说，像将字符串转为驼峰格式这样简单的任务就需要好几行代码来实现。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">camelize</span>(<span class="hljs-params">str</span>) </span>&#123;
  <span class="hljs-keyword">return</span> str.replace(<span class="hljs-regexp">/(?:^\w|[A-Z]|\b\w|\s+)/g</span>, <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">match, index</span>) </span>&#123;
    <span class="hljs-keyword">if</span> (+match === <span class="hljs-number">0</span>) <span class="hljs-keyword">return</span> <span class="hljs-string">""</span>; <span class="hljs-comment">// 或 if (/\s+/.test(match)) 来匹配空白字符</span>
    <span class="hljs-keyword">return</span> index === <span class="hljs-number">0</span> ? match.toLowerCase() : match.toUpperCase();
  &#125;);
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>上方的代码片段是在 Stack Overflow 中最受好评的答案。然而，它无法解决字符串中包含 <code>---Foo---bAr---</code> 的用例。</p>
<p><img src="https://cdn-images-1.medium.com/max/2000/1*B2BkvkI5nmrksHi8UpLHIQ.png" alt="运行结果" loading="lazy" referrerpolicy="no-referrer"></p>
<p>这时字符串处理库就派上用场了。这些库考虑了给定问题的每一种可能的用例，使得复杂字符串操作的实现变得简单。这对你很有帮助，因为你只需要调用一个函数就能得到有效的解决方案。</p>
<p>让我们看看几个 JavaScript 中的几个字符串处理库。</p>
<h2 data-id="heading-1">1. String.js</h2>
<p>String.js（简称为 <code>S</code>）是一个为浏览器或 Node.js 提供额外字符串操作方法的轻量级（压缩后大小小于 5 kB）JavaScript 库。</p>
<h3 data-id="heading-2">安装方式</h3>
<pre><code class="hljs language-bash copyable" lang="bash">npm i string
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-3">值得注意的方法</h3>
<ul>
<li><code>between(left, right)</code> —— 提取 <code>left</code> 和 <code>right</code> 字符串之间的所有字符。</li>
</ul>
<p>这个方法可以用于提取 HTML 标签之间的元素。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">var</span> S = <span class="hljs-built_in">require</span>(<span class="hljs-string">'string'</span>);
S(<span class="hljs-string">'<a>This is a link</a>'</span>).between(<span class="hljs-string">'<a>'</span>, <span class="hljs-string">'</a>'</span>).s 
<span class="hljs-comment">// => 'This is a link'</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li><code>camelize()</code> —— 去除所有的下划线和破折号，并将字符串转为驼峰格式。</li>
</ul>
<p>这个方法可以用来解决这篇文章开头时的问题。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">var</span> S = <span class="hljs-built_in">require</span>(<span class="hljs-string">'string'</span>);
S(<span class="hljs-string">'---Foo---bAr---'</span>).camelize().s; 
<span class="hljs-comment">// => 'fooBar'</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li><code>humanize()</code> —— 将输入转为人性化的形式。</li>
</ul>
<p>从无到有地实现这个函数必定需要相当多行的代码。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">var</span> S = <span class="hljs-built_in">require</span>(<span class="hljs-string">'string'</span>);
S(<span class="hljs-string">'   capitalize dash-CamelCase_underscore trim  '</span>).humanize().s
<span class="hljs-comment">// => 'Capitalize dash camel case underscore trim'</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li><code>stripPunctuation()</code> —— 去除给定字符串的所有标点符号。</li>
</ul>
<p>如果你从头开始实现这个函数，那么你很可能会错过某个标点符号。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">var</span> S = <span class="hljs-built_in">require</span>(<span class="hljs-string">'string'</span>);
S(<span class="hljs-string">'My, st[ring] *full* of %punct)'</span>).stripPunctuation().s; 
<span class="hljs-comment">// => 'My string full of punct'</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>你可以在<a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fjprichardson%2Fstring.js" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/jprichardson/string.js" ref="nofollow noopener noreferrer">这里</a>查看更多的方法。</p>
<h2 data-id="heading-4">2. Voca</h2>
<p>Voca 是一个 JavaScript 字符串操作库。这个库包含了<strong>更改大小写</strong>，<strong>修剪</strong>，<strong>填充</strong>，<strong>生成 slug</strong>，<strong>拉丁化</strong>，<strong>sprintf 格式化</strong>，<strong>截断</strong>，<strong>转义</strong>和其他有用的字符串操作方法。为了减少应用程序的构建，Voca 的模块化构建允许你只载入特定的功能。该库已经过<strong>全面的测试</strong>，<strong>文档完整</strong>，且<strong>提供长期的支持</strong>。</p>
<h3 data-id="heading-5">安装方式</h3>
<pre><code class="hljs language-bash copyable" lang="bash">npm i voca
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-6">值得注意的方法</h3>
<ul>
<li><code>camelCase(String data)</code></li>
</ul>
<p>将 <code>data</code> 转为驼峰格式。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">var</span> v = <span class="hljs-built_in">require</span>(<span class="hljs-string">'voca'</span>);
v.camelCase(<span class="hljs-string">'foo Bar'</span>);
<span class="hljs-comment">// => 'fooBar'</span>

v.camelCase(<span class="hljs-string">'FooBar'</span>);
<span class="hljs-comment">// => 'fooBar'</span>

v.camelCase(<span class="hljs-string">'---Foo---bAr---'</span>);
<span class="hljs-comment">// => 'fooBar'</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li><code>latinise(String data)</code></li>
</ul>
<p>通过删除变音符号来拉丁化 <code>data</code>。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">var</span> v = <span class="hljs-built_in">require</span>(<span class="hljs-string">'voca'</span>);
v.latinise(<span class="hljs-string">'cafe\u0301'</span>); <span class="hljs-comment">// or 'café'</span>
<span class="hljs-comment">// => 'cafe'</span>

v.latinise(<span class="hljs-string">'août décembre'</span>);
<span class="hljs-comment">// => 'aout decembre'</span>

v.latinise(<span class="hljs-string">'как прекрасен этот мир'</span>);
<span class="hljs-comment">// => 'kak prekrasen etot mir'</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li><code>isAlphaDigit(String data)</code></li>
</ul>
<p>检查 <code>data</code> 是否只包含字母和数字字符（文数字字符串）。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">var</span> v = <span class="hljs-built_in">require</span>(<span class="hljs-string">'voca'</span>);
v.isAlphaDigit(<span class="hljs-string">'year2020'</span>);
<span class="hljs-comment">// => true</span>

v.isAlphaDigit(<span class="hljs-string">'1448'</span>);
<span class="hljs-comment">// => true</span>

v.isAlphaDigit(<span class="hljs-string">'40-20'</span>);
<span class="hljs-comment">// => false</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li><code>countWords(String data)</code></li>
</ul>
<p>计算 <code>data</code> 中的单词数。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">var</span> v = <span class="hljs-built_in">require</span>(<span class="hljs-string">'voca'</span>);
v.countWords(<span class="hljs-string">'gravity can cross dimensions'</span>);
<span class="hljs-comment">// => 4</span>

v.countWords(<span class="hljs-string">'GravityCanCrossDimensions'</span>);
<span class="hljs-comment">// => 4</span>

v.countWords(<span class="hljs-string">'Gravity - can cross dimensions!'</span>);
<span class="hljs-comment">// => 4</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li><code>escapeRegExp(String data)</code></li>
</ul>
<p>转义正则表达式中的特殊字符 —— <code>- [ ] / &#123; &#125; ( ) * + ? . \ ^ $ |</code>。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">var</span> v = <span class="hljs-built_in">require</span>(<span class="hljs-string">'voca'</span>);
v.escapeRegExp(<span class="hljs-string">'(hours)[minutes]&#123;seconds&#125;'</span>);
<span class="hljs-comment">// => '(hours)[minutes]&#123;seconds&#125;'</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>你可以在<a href="https://link.juejin.cn/?target=https%3A%2F%2Fvocajs.com%2F%23" target="_blank" rel="nofollow noopener noreferrer" title="https://vocajs.com/#" ref="nofollow noopener noreferrer">此处</a>查看更多的信息。</p>
<h2 data-id="heading-7">3. Anchorme.js</h2>
<p>这是一个小巧且快速的 JavaScript 库。它能帮助你检测链接、URL、电邮地址等，并将它们转为可点击的 HTML 锚链接。</p>
<ul>
<li>高敏感度，低误报率。</li>
<li>根据完整的 IANA（互联网号码分配局）列表验证 URL 和电邮地址。</li>
<li>验证端口号（如有）。</li>
<li>验证 IP 地址（如有）。</li>
<li>可检测非拉丁字母的 URL。</li>
</ul>
<h3 data-id="heading-8">安装方式</h3>
<pre><code class="hljs language-bash copyable" lang="bash">npm i anchorme
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-9">用法</h3>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">import</span> anchorme <span class="hljs-keyword">from</span> <span class="hljs-string">"anchorme"</span>; 
<span class="hljs-comment">// 或 </span>
<span class="hljs-comment">// var anchorme = require("anchorme").default;</span>

<span class="hljs-keyword">const</span> input = <span class="hljs-string">"some text with a link.com"</span>; 
<span class="hljs-keyword">const</span> resultA = anchorme(input);
<span class="hljs-comment">// => 'some text with a <a href="http://link.com">link.com</a>'</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>你可以传入额外的扩展来进一步地自定义这个功能。</p>
<h2 data-id="heading-10">4. Underscore.string</h2>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fepeli%2Funderscore.string" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/epeli/underscore.string" ref="nofollow noopener noreferrer">Underscore.string</a> 是 JavaScript 字符串操作扩展，你可以将它与 Underscore.js 配合使用。Underscore.string 是 Underscore.js 的扩展，受 <a href="https://link.juejin.cn/?target=http%3A%2F%2Fapi.prototypejs.org%2Flanguage%2FString%2F" target="_blank" rel="nofollow noopener noreferrer" title="http://api.prototypejs.org/language/String/" ref="nofollow noopener noreferrer">Prototype.js</a>，<a href="https://link.juejin.cn/?target=http%3A%2F%2Frightjs.org%2Fdocs%2Fstring" target="_blank" rel="nofollow noopener noreferrer" title="http://rightjs.org/docs/string" ref="nofollow noopener noreferrer">Right.js</a> 和 <a href="https://link.juejin.cn/?target=http%3A%2F%2Fdocumentcloud.github.com%2Funderscore%2F" target="_blank" rel="nofollow noopener noreferrer" title="http://documentcloud.github.com/underscore/" ref="nofollow noopener noreferrer">Underscore</a> 所启发。这个 JavaScript 库能让你「惬意的」操作字符串。</p>
<p>Underscore.string 为你提供了几个有用的功能，例如：<code>capitalize</code>，<code>clean</code>，<code>includes</code>，<code>count</code>，<code>escapeHTML</code>，<code>unescapeHTML</code>，<code>insert</code>，<code>splice</code>，<code>startsWith</code>，<code>endsWith</code>，<code>titleize</code>，<code>trim</code>，<code>truncate</code> 等等。</p>
<h3 data-id="heading-11">安装方式</h3>
<pre><code class="hljs language-bash copyable" lang="bash">npm install underscore.string
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-12">值得注意的方法</h3>
<ul>
<li><code>numberFormat(number)</code> —— 格式化数字。</li>
</ul>
<p>将数字格式化为带有小数点和万位分隔符的字符串。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">var</span> _ = <span class="hljs-built_in">require</span>(<span class="hljs-string">"underscore.string"</span>);

_.numberFormat(<span class="hljs-number">1000</span>, <span class="hljs-number">3</span>)
<span class="hljs-comment">// => "1,000.000"</span>

_.numberFormat(<span class="hljs-number">123456789.123</span>, <span class="hljs-number">5</span>, <span class="hljs-string">'.'</span>, <span class="hljs-string">','</span>);
<span class="hljs-comment">// => "123,456,789.12300"</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li><code>levenshtein(string1, string2)</code> —— 计算两个字符串的莱文斯坦距离。</li>
</ul>
<p>你可以在<a href="https://link.juejin.cn/?target=https%3A%2F%2Fdzone.com%2Farticles%2Fthe-levenshtein-algorithm-1" target="_blank" rel="nofollow noopener noreferrer" title="https://dzone.com/articles/the-levenshtein-algorithm-1" ref="nofollow noopener noreferrer">此处</a>了解更多有关莱文斯坦距离算法的信息。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">var</span> _ = <span class="hljs-built_in">require</span>(<span class="hljs-string">"underscore.string"</span>);

_.levenshtein(<span class="hljs-string">'kitten'</span>, <span class="hljs-string">'kittah'</span>);
<span class="hljs-comment">// => 2</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li><code>chop(string, step)</code> —— 将指定字符串切成多段。</li>
</ul>
<pre><code class="hljs language-js copyable" lang="js">_.chop(<span class="hljs-string">'whitespace'</span>, <span class="hljs-number">3</span>);
<span class="hljs-comment">// => ['whi','tes','pac','e']</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>你可以在<a href="https://link.juejin.cn/?target=http%3A%2F%2Fgabceb.github.io%2Funderscore.string.site" target="_blank" rel="nofollow noopener noreferrer" title="http://gabceb.github.io/underscore.string.site" ref="nofollow noopener noreferrer">此处</a>了解更多有关 Underscore String 的信息。</p>
<h2 data-id="heading-13">5. Stringz</h2>
<p>这个库的主要亮点在于它可以识别 Unicode。如果你运行以下的代码，输出会是 2。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-string">"🤔"</span>.length;
<span class="hljs-comment">// => 2</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这是因为 <code>String.length()</code> 回传的是字符串中的代码单元数，而不是字符数。实际上，在 <strong>010000 至 03FFFF</strong> 和 <strong>040000 至 10FFFF</strong> 区间中的字符需要 4 个字节（32 位），1 个码位来表示。这对结果毫无影响。然而，有些字符需要超过 2 个字节来表示，一次他们需要 1 个以上的码位。</p>
<p>你可以在<a href="https://link.juejin.cn/?target=https%3A%2F%2Fmathiasbynens.be%2Fnotes%2Fjavascript-unicode" target="_blank" rel="nofollow noopener noreferrer" title="https://mathiasbynens.be/notes/javascript-unicode" ref="nofollow noopener noreferrer">此处</a>阅读更多有关 JavaScript Unicode 的问题。</p>
<h3 data-id="heading-14">安装方式</h3>
<pre><code class="hljs language-bash copyable" lang="bash">npm install stringz
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-15">值得注意的方法</h3>
<ul>
<li><code>limit(string, limit, padString, padPosition)</code></li>
</ul>
<p>将字符串长度限制在给定长度内。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> stringz = <span class="hljs-built_in">require</span>(<span class="hljs-string">'stringz'</span>);

<span class="hljs-comment">// 截断：</span>
stringz.limit(<span class="hljs-string">'Life’s like a box of chocolates.'</span>, <span class="hljs-number">20</span>); 
<span class="hljs-comment">// => "Life's like a box of"</span>

<span class="hljs-comment">// 填充：</span>
stringz.limit(<span class="hljs-string">'Everybody loves emojis!'</span>, <span class="hljs-number">26</span>, <span class="hljs-string">'💩'</span>); 
<span class="hljs-comment">// => "Everybody loves emojis!💩💩💩"</span>
stringz.limit(<span class="hljs-string">'What are you looking at?'</span>, <span class="hljs-number">30</span>, <span class="hljs-string">'+'</span>, <span class="hljs-string">'left'</span>); 
<span class="hljs-comment">// => "++++++What are you looking at?"</span>

<span class="hljs-comment">// 可识别 unicode</span>
stringz.limit(<span class="hljs-string">'🤔🤔🤔'</span>, <span class="hljs-number">2</span>); 
<span class="hljs-comment">// => "🤔🤔"</span>
stringz.limit(<span class="hljs-string">'👍🏽👍🏽'</span>, <span class="hljs-number">4</span>, <span class="hljs-string">'👍🏽'</span>); 
<span class="hljs-comment">// => "👍🏽👍🏽👍🏽👍🏽"</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li><code>toArray(string)</code></li>
</ul>
<p>将字符串转为数组：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> stringz = <span class="hljs-built_in">require</span>(<span class="hljs-string">'stringz'</span>);

stringz.toArray(<span class="hljs-string">'abc'</span>);
<span class="hljs-comment">// ['a','b','c']</span>

<span class="hljs-comment">// 可识别 unicode</span>
stringz.toArray(<span class="hljs-string">'👍🏽🍆🌮'</span>);
<span class="hljs-comment">// ['👍🏽', '🍆', '🌮']</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>欲了解更多关于 Stringz 的信息，请访问 <a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fsallar%2Fstringz" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/sallar/stringz" ref="nofollow noopener noreferrer">Stringz 的 Github 仓库</a>。</p>
<blockquote>
<p>如果发现译文存在错误或其他需要改进的地方，欢迎到 <a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fxitu%2Fgold-miner" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/xitu/gold-miner" ref="nofollow noopener noreferrer">掘金翻译计划</a> 对译文进行修改并 PR，也可获得相应奖励积分。文章开头的 <strong>本文永久链接</strong> 即为本文在 GitHub 上的 MarkDown 链接。</p>
</blockquote>
<hr>
<blockquote>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fxitu%2Fgold-miner" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/xitu/gold-miner" ref="nofollow noopener noreferrer">掘金翻译计划</a> 是一个翻译优质互联网技术文章的社区，文章来源为 <a href="https://juejin.im/" target="_blank" title="https://juejin.im">掘金</a> 上的英文分享文章。内容覆盖 <a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fxitu%2Fgold-miner%23android" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/xitu/gold-miner#android" ref="nofollow noopener noreferrer">Android</a>、<a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fxitu%2Fgold-miner%23ios" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/xitu/gold-miner#ios" ref="nofollow noopener noreferrer">iOS</a>、<a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fxitu%2Fgold-miner%23%25E5%2589%258D%25E7%25AB%25AF" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/xitu/gold-miner#%E5%89%8D%E7%AB%AF" ref="nofollow noopener noreferrer">前端</a>、<a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fxitu%2Fgold-miner%23%25E5%2590%258E%25E7%25AB%25AF" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/xitu/gold-miner#%E5%90%8E%E7%AB%AF" ref="nofollow noopener noreferrer">后端</a>、<a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fxitu%2Fgold-miner%23%25E5%258C%25BA%25E5%259D%2597%25E9%2593%25BE" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/xitu/gold-miner#%E5%8C%BA%E5%9D%97%E9%93%BE" ref="nofollow noopener noreferrer">区块链</a>、<a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fxitu%2Fgold-miner%23%25E4%25BA%25A7%25E5%2593%2581" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/xitu/gold-miner#%E4%BA%A7%E5%93%81" ref="nofollow noopener noreferrer">产品</a>、<a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fxitu%2Fgold-miner%23%25E8%25AE%25BE%25E8%25AE%25A1" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/xitu/gold-miner#%E8%AE%BE%E8%AE%A1" ref="nofollow noopener noreferrer">设计</a>、<a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fxitu%2Fgold-miner%23%25E4%25BA%25BA%25E5%25B7%25A5%25E6%2599%25BA%25E8%2583%25BD" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/xitu/gold-miner#%E4%BA%BA%E5%B7%A5%E6%99%BA%E8%83%BD" ref="nofollow noopener noreferrer">人工智能</a>等领域，想要查看更多优质译文请持续关注 <a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fxitu%2Fgold-miner" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/xitu/gold-miner" ref="nofollow noopener noreferrer">掘金翻译计划</a>、<a href="https://link.juejin.cn/?target=http%3A%2F%2Fweibo.com%2Fjuejinfanyi" target="_blank" rel="nofollow noopener noreferrer" title="http://weibo.com/juejinfanyi" ref="nofollow noopener noreferrer">官方微博</a>、<a href="https://link.juejin.cn/?target=https%3A%2F%2Fzhuanlan.zhihu.com%2Fjuejinfanyi" target="_blank" rel="nofollow noopener noreferrer" title="https://zhuanlan.zhihu.com/juejinfanyi" ref="nofollow noopener noreferrer">知乎专栏</a>。</p>
</blockquote></div>  
</div>
            