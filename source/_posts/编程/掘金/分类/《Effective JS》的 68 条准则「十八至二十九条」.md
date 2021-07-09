
---
title: '《Effective JS》的 68 条准则「十八至二十九条」'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=9015'
author: 掘金
comments: false
date: Thu, 08 Jul 2021 20:04:54 GMT
thumbnail: 'https://picsum.photos/400/300?random=9015'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;color:#595959;font-size:15px;font-family:-apple-system,system-ui,BlinkMacSystemFont,Helvetica Neue,PingFang SC,Hiragino Sans GB,Microsoft YaHei,Arial,sans-serif;background-image:linear-gradient(90deg,rgba(60,10,30,.04) 3%,transparent 0),linear-gradient(1turn,rgba(60,10,30,.04) 3%,transparent 0);background-size:20px 20px;background-position:50%&#125;.markdown-body p&#123;color:#595959;font-size:15px;line-height:2;font-weight:400&#125;.markdown-body p+p&#123;margin-top:16px&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;padding:30px 0;margin:0;color:#135ce0&#125;.markdown-body h1&#123;position:relative;text-align:center;font-size:22px;margin:50px 0&#125;.markdown-body h1:before&#123;position:absolute;content:"";top:-10px;left:50%;width:32px;height:32px;transform:translateX(-50%);background-size:100% 100%;opacity:.36;background-repeat:no-repeat;background:url(data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACAAAAAgCAMAAABEpIrGAAAABGdBTUEAALGPC/xhBQAAACBjSFJNAAB6JgAAgIQAAPoAAACA6AAAdTAAAOpgAAA6mAAAF3CculE8AAABfVBMVEX///8Ad/8AgP8AgP8AgP8Aff8AgP8Af/8AgP8AVf8Af/8Af/8AgP8AgP8Af/8Afv8AAP8Afv8Afv8Aef8AgP8AdP8Afv8AgP8AgP8Acf8Ae/8AgP8Af/8AgP8Af/8Af/8AfP8Afv8AgP8Af/8Af/8Afv8Afv8AgP8Afv8AgP8Af/8Af/8AgP8AgP8Afv8AgP8Af/8AgP8AgP8AgP8Ae/8Afv8Af/8AgP8Af/8AgP8Af/8Af/8Aff8Af/8Abf8AgP8Af/8AgP8Af/8Af/8Afv8AgP8AgP8Afv8Afv8AgP8Af/8Aff8AgP8Afv8AgP8Aff8AgP8AfP8AgP8Ae/8AgP8Af/8AgP8AgP8AgP8Afv8AgP8AgP8AgP8Afv8AgP8AgP8AgP8AgP8AgP8Af/8AgP8Af/8Af/8Aev8Af/8AgP8Aff8Afv8AgP8AgP8AgP8Af/8AgP8Af/8Af/8AgP8Afv8AgP8AgP8AgP8AgP8Af/8AeP8Af/8Af/8Af//////rzEHnAAAAfXRSTlMAD7CCAivatxIDx5EMrP19AXdLEwgLR+6iCR/M0yLRzyFF7JupSXn8cw6v60Q0QeqzKtgeG237HMne850/6Qeq7QaZ+WdydHtj+OM3qENCMRYl1B3K2U7wnlWE/mhlirjkODa9FN/BF7/iNV/2kASNZpX1Wlf03C4stRGxgUPclqoAAAABYktHRACIBR1IAAAACXBIWXMAAAsTAAALEwEAmpwYAAAAB3RJTUUH4gEaBzgZ4yeM3AAAAT9JREFUOMvNUldbwkAQvCAqsSBoABE7asSOBRUVVBQNNuy9996789+9cMFAMHnVebmdm+/bmdtbQv4dOFOW2UjPzgFyLfo6nweKfIMOBYWwFtmMPGz2Yj2pJI0JDq3udJW6VVbmKa9I192VQFV1ktXUAl5NB0cd4KpnORqsEO2ZIRpF9gJfE9Dckqq0KuZt7UAH5+8EPF3spjsRpCeQNO/tA/qDwIDA+OCQbBoKA8NOdjMySgcZGVM6jwcgRuUiSs0nlPFNSrEpJfU0jTLD6llqbvKxei7OzvkFNQohi0vAsj81+MoqsCaoPOQFgus/1LyxichW+hS2JWCHZ7VlF9jb187pIAYcHiViHAMnp5mTjJ8B5xeEXF4B1ze/fTh/C0h398DDI9HB07O8ci+vRBdvdGnfP4gBuM8vw7X/G3wDmFhFZEdxzjMAAAAldEVYdGRhdGU6Y3JlYXRlADIwMTgtMDEtMjZUMDc6NTY6MjUrMDE6MDA67pVWAAAAJXRFWHRkYXRlOm1vZGlmeQAyMDE4LTAxLTI2VDA3OjU2OjI1KzAxOjAwS7Mt6gAAABl0RVh0U29mdHdhcmUAd3d3Lmlua3NjYXBlLm9yZ5vuPBoAAAAWdEVYdFRpdGxlAGp1ZWppbl9sb2dvIGNvcHlxapmKAAAAV3pUWHRSYXcgcHJvZmlsZSB0eXBlIGlwdGMAAHic4/IMCHFWKCjKT8vMSeVSAAMjCy5jCxMjE0uTFAMTIESANMNkAyOzVCDL2NTIxMzEHMQHy4BIoEouAOoXEXTyQjWVAAAAAElFTkSuQmCC)&#125;.markdown-body h2&#123;position:relative;font-size:20px;border-left:4px solid;padding:0 0 0 10px;margin:30px 0&#125;.markdown-body h3&#123;font-size:16px&#125;.markdown-body ul&#123;list-style:disc outside;margin-left:2em;margin-top:1em&#125;.markdown-body li&#123;line-height:2;color:#595959&#125;.markdown-body img.loaded&#123;margin:0 auto;display:block&#125;.markdown-body blockquote&#123;background:#fff9f9;margin:2em 0;padding:2px 20px;border-left:4px solid #b2aec5&#125;.markdown-body blockquote p&#123;color:#666;line-height:2&#125;.markdown-body a&#123;color:#036aca;border-bottom:1px solid rgba(3,106,202,.8);font-weight:400;text-decoration:none&#125;.markdown-body em strong,.markdown-body strong&#123;color:#036aca&#125;.markdown-body hr&#123;border-top:1px solid #135ce0&#125;.markdown-body pre&#123;overflow:auto&#125;.markdown-body code,.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body table&#123;border-collapse:collapse;margin:1rem 0;overflow-x:auto&#125;.markdown-body table td,.markdown-body table th&#123;border:1px solid #dfe2e5;padding:.6em 1em&#125;.markdown-body table tr&#123;border-top:1px solid #dfe2e5&#125;.markdown-body table tr:nth-child(2n)&#123;background-color:#f6f8fa&#125;</style><h1 data-id="heading-0">起因</h1>
<p>阅读学习《Effective JavaScript》，以自身阅读和理解，<strong>着重记录内容精华部分以及对内容进行排版</strong>，便于日后自身回顾学习以及大家交流学习。</p>
<p>因内容居多，分为每个章节来进行编写文章，每章节的准条多少不一，故每篇学习笔记的文章以章节为准。</p>
<p><em>适合碎片化阅读，精简阅读的小友们。争取让小友们看完系列 === 看整本书的 85+%。</em></p>
<h1 data-id="heading-1">前言</h1>
<h2 data-id="heading-2">内容总览</h2>
<ul>
<li>第一章让初学者快速熟悉 JavaScript，了解 JavaScript 中的原始类型、隐式强制转换、编码类型等几本概念；</li>
<li>第二章着重讲解了有关 JavaScript 的变量作用域的建议，不仅介绍了怎么做，还介绍了操作背后的原因，帮助读者加深理解；</li>
<li>第三章和第四章的主题涵盖函数、对象及原型三大方面，这可是 JavaScript 区别于其他语言的核心；</li>
<li>第五章阐述了数组和字典这两种容易混淆的常用类型及具体使用时的建议，避免陷入一些陷阱；</li>
<li>第六章讲述了库和 API 设计；</li>
<li>第七章讲述了并行编程，这是晋升为 JavaScript 专家的必经之路</li>
</ul>
<h1 data-id="heading-3">第 3 章「使用函数」</h1>
<p>函数在 JavaScript 中既给程序员提供了主要的抽象功能，又提供了实现机制。函数也可以独自模拟实现出其他语言中的多个不同的特性，如过程、方法、构造函数、类和模块。因此在不同的环境中高效地使用函数是在所难免的。</p>
<h2 data-id="heading-4">第 18 条：理解函数调用、方法调用及构造函数调用之间的不同</h2>
<p>在 JavaScript 中，它们只是单个构造对象的三种不同的使用模式。</p>
<h3 data-id="heading-5">函数调用</h3>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">hello</span>(<span class="hljs-params">username</span>) </span>&#123;
  <span class="hljs-keyword">return</span> <span class="hljs-string">"hello"</span> + username;
&#125;
hello(<span class="hljs-string">"Ling Mu"</span>);<span class="hljs-comment">// "hello Ling Mu"</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>简单调用 hello 函数并将给定的实参绑定到 name 形参</p>
<h3 data-id="heading-6">方法调用</h3>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> obj = &#123;
  <span class="hljs-attr">username</span>: <span class="hljs-string">"Ling Mu"</span>,
  <span class="hljs-attr">hello</span>: <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params"></span>) </span>&#123;
    <span class="hljs-keyword">return</span> <span class="hljs-string">"hello"</span> + <span class="hljs-built_in">this</span>.username;
  &#125;
&#125;;
obj.hello();<span class="hljs-comment">// "hello Ling Mu"</span>

<span class="copy-code-btn">复制代码</span></code></pre>
<p>表达式 obj.hello() 在 obj 对象中查找名为 hello 的属性恰巧是 obj.hello 函数，也就是方法调用。</p>
<p>而 <code>this</code> 变量的绑定是由表达式自身来确定，绑定到 this 变量的对象称为调用接收者。如下例子</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> obj2 = &#123;
  <span class="hljs-attr">username</span>: <span class="hljs-string">"Ling Mu2"</span>,
  <span class="hljs-attr">hello</span>: obj.hello
&#125;;
obj2.hello();<span class="hljs-comment">// "hello Ling Mu2"</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>表达式 obj2.hello() 在 obj2 对象中查找名为 hello 的属性，恰巧正是 obj.hello 函数，但是接收者是 obj2 对象。通常，通过某个对象调用方法将查找该方法并将该对象作为该方法的接收者。</p>
<p>若是非方法函数调用则会将全局对象作为接收者：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">hello</span>(<span class="hljs-params"></span>) </span>&#123;
  <span class="hljs-keyword">return</span> <span class="hljs-string">"hello"</span> + <span class="hljs-built_in">this</span>.username;
&#125;
hello();<span class="hljs-comment">// "hello undefined"</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>全局对象中没有 name 的属性，则产生 undefined。而在全局作用域下将 this 变量绑定到全局对象也是有问题的，所以 ES5 严格模式将 this 变量的默认绑定值设置为 undefined</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">hello</span>(<span class="hljs-params"></span>) </span>&#123;
<span class="hljs-meta">  "use strict"</span>;
  <span class="hljs-keyword">return</span> <span class="hljs-string">"hello"</span> + <span class="hljs-built_in">this</span>.username;
&#125;
hello();<span class="hljs-comment">// error: cannnot read property "usename" of undefined</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-7">构造函数调用</h3>
<p>函数通过构造函数使用，就像方法和纯函数一样，也是 function 运算符定义。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">User</span>(<span class="hljs-params">name, password</span>) </span>&#123;
  <span class="hljs-built_in">this</span>.name = name;
  <span class="hljs-built_in">this</span>.password = password;
&#125;
<span class="hljs-keyword">const</span> u = <span class="hljs-keyword">new</span> User(<span class="hljs-string">"Ling Mu"</span>, <span class="hljs-string">"123456"</span>);
u.name; <span class="hljs-comment">// "Ling Mu"</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>与函数调用和方法调用不同的是，构造函数调用将一个全新的对象作为 this 变量的值，并隐式返回这个新对象作为调用结果。构造函数的主要职责是初始化该新对象。</p>
<h3 data-id="heading-8">总结</h3>
<ul>
<li>方法调用将被查找方法属性的对象作为调用接收者。</li>
<li>函数调用将全局对象（处于严格模式下则为 undefined）作为其接收者，一般很少使用函数调用语法来调用方法。</li>
<li>构造函数需要通过 new 运算符调用，并产生一个新的对象作为其接收者。</li>
</ul>
<h2 data-id="heading-9">第 19 条：熟练掌握高阶函数</h2>
<h3 data-id="heading-10">高阶函数</h3>
<p>开发简洁优雅的函数通常可以使代码更加简单明了，高阶函数则是将函数作为参数或返回值的函数，是一种强大且富有表现力的惯用法，也在 JavaScript程序中被大量使用。</p>
<p>如简单的转换字符串数组的操作，使用循环：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> names = [<span class="hljs-string">"Lin"</span>, <span class="hljs-string">"Mu"</span>, <span class="hljs-string">"Qiqiu"</span>];
<span class="hljs-keyword">const</span> upper = [];
<span class="hljs-keyword">for</span> (<span class="hljs-keyword">let</span> i = <span class="hljs-number">0</span>, n = names.length; i < n; i++) &#123;
  upper[i] = names[i].toUpperCase();
&#125;
upper;<span class="hljs-comment">// ["LIN", "MU", "QIQIU"];</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>高阶函数与之实现为：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> names = [<span class="hljs-string">"Lin"</span>, <span class="hljs-string">"Mu"</span>, <span class="hljs-string">"Qiqiu"</span>];
<span class="hljs-keyword">const</span> upper = names.map(<span class="hljs-function">() =></span> name.toUpperCase(););
upper;<span class="hljs-comment">// ["LIN", "MU", "QIQIU"];</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>使用数组遍历的 map 方法，可以完全消除循环，仅仅使用一个局部函数就可以实现对元素的逐个转换。</p>
<h3 data-id="heading-11">例子</h3>
<blockquote>
<p>需要引入高阶函数抽象的信号是出现重复或相似的代码。</p>
</blockquote>
<p>例如，假设我们发现程序的部分代码段使用英文字母构造一个字符串。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> aIndex = <span class="hljs-string">'a'</span>.charCodeAt(<span class="hljs-number">0</span>);<span class="hljs-comment">// 97</span>
<span class="hljs-keyword">let</span> alphabet = <span class="hljs-string">''</span>;
<span class="hljs-keyword">for</span> (<span class="hljs-keyword">let</span> i = <span class="hljs-number">0</span>; i < <span class="hljs-number">26</span>; i++) &#123;
  alphabet += <span class="hljs-built_in">String</span>.fromCharCode(aIndex + i);
&#125;
alphabet;<span class="hljs-comment">// "abcdefghijklmnopqrstuvwxyz"</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>同时，程序的另一部分代码段生成一个包含数字的字符串。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">let</span> digits = <span class="hljs-string">''</span>;
<span class="hljs-keyword">for</span> (<span class="hljs-keyword">let</span> i = <span class="hljs-number">0</span>; i < <span class="hljs-number">10</span>; i++) &#123;
digits += i;
&#125;
digits;<span class="hljs-comment">// "0123456789"</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>此外，程序的其他地方还存在创建一个随机字符串。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> aIndex = <span class="hljs-string">'a'</span>.charCodeAt(<span class="hljs-number">0</span>);<span class="hljs-comment">// 97</span>
<span class="hljs-keyword">let</span> random = <span class="hljs-string">''</span>;
<span class="hljs-keyword">for</span> (<span class="hljs-keyword">let</span> i = <span class="hljs-number">0</span>; i < <span class="hljs-number">8</span>; i++) &#123;
random += <span class="hljs-built_in">String</span>.fromCharCode(<span class="hljs-built_in">Math</span>.floor(<span class="hljs-built_in">Math</span>.random() * <span class="hljs-number">26</span>) + aIndex);
&#125;
random;<span class="hljs-comment">// 随机字符串</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>每个例子创建了一个不同的字符串，但它们都有着共同的逻辑。<strong>每个循环通过链接每个独立部分的计算结果来创建一个字符串</strong>。我们可以提取出公用的部分，移到单个工具函数里。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">buildString</span>(<span class="hljs-params">n, callback</span>) </span>&#123;
  <span class="hljs-keyword">let</span> result = <span class="hljs-string">''</span>;
  <span class="hljs-keyword">for</span> (<span class="hljs-keyword">let</span> i = <span class="hljs-number">0</span>; i < n; i++) &#123;
result += callback(i);
&#125;
  <span class="hljs-keyword">return</span> result;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>buildString 函数实现包含了每个循环的所有共用部分，并使用参数来替代变化部分。如循环迭代次数由变量 <code>n</code> 替代，每个字符串片段的构造由 <code>callback</code> 函数替代。因此我们可以使用如下高阶函数：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> alphabet = buildString(<span class="hljs-number">26</span>, <span class="hljs-function">(<span class="hljs-params">i</span>) =></span> <span class="hljs-built_in">String</span>.fromCharCode(aIndex + i););
alphabet;<span class="hljs-comment">// "abcdefghijklmnopqrstuvwxyz"</span>

<span class="hljs-keyword">const</span> digits = buildString(<span class="hljs-number">10</span>, <span class="hljs-function">(<span class="hljs-params">i</span>) =></span> i);
digits;<span class="hljs-comment">// "0123456789"</span>

<span class="copy-code-btn">复制代码</span></code></pre>
<p>而常见高阶函数抽象的实现中存在一些棘手的部分，如正确地获取循环边界条件，它们可以被正确地放置在高阶函数的实现中。</p>
<p>记得给高阶函数抽象一个清晰的名称，这样能使读者更清晰地了解该代码能做什么，而无须深入实现细节。</p>
<p>当发现自己在重复地写一些相同的模式时，学会借助于一个高阶函数可以使代码更简洁、更高效、更可读。留意一些常见的模式并将它们移到高阶的工具函数中是一个重要的开发习惯。</p>
<h3 data-id="heading-12">总结</h3>
<ul>
<li>高阶函数时那些将函数作为参数或返回值的函数。</li>
<li>熟悉掌握现有库中的高阶函数。</li>
<li>学会发现可以被高阶函数所取代的常用的编码模式。</li>
</ul>
<h2 data-id="heading-13">第 20 条：使用 call 方法自定义接收者来调用方法</h2>
<h3 data-id="heading-14">接收者</h3>
<p>通常情况下，函数或方法的接收者（即绑定到特殊关键字 this 的值）是由调用者的语法决定的。如方法调用语法将方法被查找的对象绑定到 <code>this</code> 变量，有时需要使用自定义接收者来调用函数。</p>
<p>因为该函数可能并不是期望的接收者对象的属性，我们可以将方法作为一个新的属性添加到接收者对象中。</p>
<pre><code class="hljs language-js copyable" lang="js">obj.temp = f;
<span class="hljs-keyword">const</span> res = obj.temp(arg1, arg2);
<span class="hljs-keyword">delete</span> obj.temp;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>修改 obj 对象往往是不可取的，甚至有时不可能修改。当使用自定义属性时，都可能与 obj 中已由的属性重名。</p>
<p>此外，某些对象可能被冻结或密封以防止添加任何属性。因此对于不是自己常见的对象，随意给对象添加属性是一种不好的实践。</p>
<h3 data-id="heading-15">call 方法</h3>
<p>函数对象具有一个内置的方法 <code>call</code> 来自定义接收者。可能通过函数对象的 <code>call</code> 方法来调用其自身。</p>
<pre><code class="hljs language-js copyable" lang="js">f(arg1, arg2);
<span class="hljs-comment">// 类似等价于</span>
f.call(obj, arg1, arg2)
<span class="copy-code-btn">复制代码</span></code></pre>
<p><code>call</code> 方法第一个参数提供了一个显式的接收者对象。当调用的方法已经被删除、修改或者覆盖时，<code>call</code> 方法也可以派上用场了。</p>
<p>如 <code>hasOwnProperty</code> 方法可被任意的对象调用，甚至该对象是一个字典对象。在字典对象中，查找 <code>hasOwnProperty</code> 属性会得到该字典对象的属性值，而不是继承过来的方法。</p>
<pre><code class="hljs language-js copyable" lang="js">dict.hasOwnProperty = <span class="hljs-number">1</span>;
dict.hasOwnProperty(<span class="hljs-string">"foo"</span>);<span class="hljs-comment">// error: 1 is not a function</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>使用 <code>hasOwnProperty</code> 方法的 call 方法使调用字典对象中的方法成为可能。即便我们手动删除了该对象。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> hasOwnProperty = &#123;&#125;.hasOwnProperty;
<span class="hljs-keyword">const</span> dict.foo = <span class="hljs-number">1</span>;
<span class="hljs-keyword">delete</span> dict.hasOwnProperty;
<span class="hljs-comment">// 调用 dict 中的属性</span>
hasOwnProperty.call(dict, <span class="hljs-string">"foo"</span>);<span class="hljs-comment">// true</span>
<span class="hljs-comment">// 无该属性</span>
hasOwnProperty.call(dict, <span class="hljs-string">"hasOwnProperty"</span>);<span class="hljs-comment">// false</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-16">高阶函数</h3>
<p>高阶函数的一个惯用法是接收一个可选的参数作为调用该函数的接收者。例如，表示键值对列表的对象可能提供名为 <code>forEach</code> 的方法。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> table = &#123;
  <span class="hljs-attr">entries</span>: [],
  <span class="hljs-attr">addEntry</span>: <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">key, value</span>) </span>&#123;
    <span class="hljs-built_in">this</span>.entries.push(&#123; key, value &#125;);
  &#125;,
  <span class="hljs-attr">forEach</span>: <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">f, thisArg</span>) </span>&#123;
    <span class="hljs-keyword">const</span> entries = <span class="hljs-built_in">this</span>.entries;
    <span class="hljs-keyword">for</span> (<span class="hljs-keyword">let</span> i = <span class="hljs-number">0</span>, n = entries.length; i < n; i++) &#123;
      <span class="hljs-keyword">const</span> entry = entries[i];
      f.call(thisArg, entry.key, entry.value, i);
    &#125;
  &#125;
&#125;;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>上述例子允许 <code>table</code> 对象的使用者将一个方法作为 <code>table.forEach</code> 的回调函数 <code>f</code>，并未该方法提供一个合理的接收者。例如，可以方便地将一个 <code>table</code> 的内容复制到另一个中。</p>
<p><code>table1.forEach(table2.addEntry, table2);</code></p>
<p>这段代码从 <code>table2</code> 中提取 <code>addEntry</code> 方法（甚至可以从 Table.prototype 或者 table1 中提取），<code>forEach</code> 方法将 <code>table2</code> 作为接收者，并反复调用该 <code>addEntry</code> 方法。</p>
<p>虽然 <code>addEntry</code> 方法只期望两个参数，但 <code>forEach</code> 方法调用它时却传递给它按个参数。多余的索引参数将被 <code>addEntry</code> 方法简单地忽略掉。</p>
<h3 data-id="heading-17">总结</h3>
<ul>
<li>使用 call 方法自定义接收者来调用函数。</li>
<li>使用 call 方法可以调用在给定的对象中不存在的方法。</li>
<li>使用 call 方法定义高阶函数允许使用者给回调函数指定接收者。</li>
</ul>
<h2 data-id="heading-18">第 21 条：使用 apply 方法通过不同数量的参数调用函数</h2>
<h3 data-id="heading-19">apply 方法</h3>
<p>在调用 <code>call</code> 方法中，当回调函数可以接收任意数量的参数，被称为可变参数或可变元的函数，但需让调用者预先明确地知道提供了多少个参数。</p>
<p>倘若我们传递的是一个数组参数，那么将使用函数对象内置的 <code>apply</code> 方法，它与 <code>call</code> 方法非常类似，并且是为了固定元数传递数组参数而设计的。</p>
<p>apply  方法指定第一个参数绑定到被调用函数的 this 变量，若调用函数中没有引用 this 变量，我们可以简单地传递 null 值。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> scores = [<span class="hljs-number">1</span>, <span class="hljs-number">2</span>, <span class="hljs-number">3</span>];
average.apply(<span class="hljs-literal">null</span>, scores);

<span class="hljs-comment">// 以上代码的行为等效于</span>
average.apply(scores[<span class="hljs-number">0</span>], scores[<span class="hljs-number">1</span>], scores[<span class="hljs-number">2</span>]);
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-20">可变参数方法</h3>
<p>apply 方法也可用于可变参数方法。例如 buffer 对象包含一个可变参数的 append 方法，该方法添加元素到函数内部的 state 数组中。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> buffer = &#123;
  <span class="hljs-attr">state</span>: [],
  <span class="hljs-attr">append</span>: <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params"></span>) </span>&#123;
    <span class="hljs-keyword">for</span> (<span class="hljs-keyword">let</span> i = <span class="hljs-number">0</span>, n = <span class="hljs-built_in">arguments</span>.length; i < n; i++) &#123;
      <span class="hljs-built_in">this</span>.state.push(<span class="hljs-built_in">arguments</span>[i]);
    &#125;
  &#125;
&#125;

<span class="hljs-comment">// 可变参数调用</span>
buffer.append(<span class="hljs-string">"hello, "</span>);
buffer.append(firstName, <span class="hljs-string">""</span>, lastName, <span class="hljs-string">"!"</span>);

<span class="copy-code-btn">复制代码</span></code></pre>
<p>借助于 apply 方法的 this 参数，我们也可以指定一个可计算的数组调用 append 方法：</p>
<p><code>buffer.append.apply(buffer, getInputStrings());</code></p>
<blockquote>
<p>apply 第一个参数，如果我们传递一个不同的对象，那么 append 方法将尝试修改该错误独享的 state 属性。</p>
</blockquote>
<h3 data-id="heading-21">总结</h3>
<ul>
<li>使用 apply  方法指定一个可计算的参数数组来调用可变参数的函数。</li>
<li>使用 apply  方法的第一个参数给可变参数的方法提供一个接收者。</li>
<li>利用函数内置的 arguments 局部变量来调用 apply 方法用于可变参数方法中。</li>
</ul>
<h2 data-id="heading-22">第 22 条：使用 arguments 创建可变参数的函数</h2>
<h3 data-id="heading-23">arguments</h3>
<p>可变参数没有定义任何显式的形参。它利用了 JavaScript 给每个函数都隐式地提供了一个名为 <code>arguments</code> 的局部变量对象，给实参提供了一个类似数组的接口。它为每个实参提供了一个索引属性，还包含一个 <code>length</code> 属性用来指示参数的个数。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">average</span>(<span class="hljs-params"></span>) </span>&#123;
  <span class="hljs-keyword">for</span> (<span class="hljs-keyword">let</span> i = <span class="hljs-number">0</span>, sum = <span class="hljs-number">0</span>, n = <span class="hljs-built_in">arguments</span>.length; i < n; i++) &#123;
    sum += <span class="hljs-built_in">arguments</span>[i];
  &#125;
  <span class="hljs-keyword">return</span> sum / n;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-24">便利固定元数方法</h3>
<p>可变参数函数提供了灵活的接口，不同的调用者可使用不同数量的参数来调用它们。如果使用者想使用计算的数组参数来调用可变参数的函数，只能使用在第 21 条中描述的 apply 方法。</p>
<p>而我们可以提供一个便利的可变参数的函数，也最好提供一个需要显示指定数组的固定元数的版本。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">average</span>(<span class="hljs-params"></span>) </span>&#123;
  <span class="hljs-keyword">return</span> averageOfArray(<span class="hljs-built_in">arguments</span>);
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>编写一个轻量级的封装，并委托给固定元数的版本实现可变参数的函数。这样一来，函数的使用者就无需借助 <code>apply</code> 方法。</p>
<blockquote>
<p>apply 方法会降低可读性而且经常导致性能损失。</p>
</blockquote>
<h3 data-id="heading-25">总结</h3>
<ul>
<li>使用隐式的 arguments 对象实现可变参数的函数。</li>
<li>考虑对可变参数的函数提供一个额外的固定元数的版本，从而使使用者无需借助 apply 方法，避免其缺陷。</li>
</ul>
<h2 data-id="heading-26">第 23 条：永远不要修改 arguments 对象</h2>
<h3 data-id="heading-27">arguments 别名</h3>
<p>arguments 是一个类数组而非数组。例如，当我们想在 arguments 对象上调用 <code>shift()</code> 方法来删除数组的第一个元素并逐个移动所有后续的元素。因为 arguments 对象上没有 <code>shift()</code> 方法，我们不能直接调用。</p>
<p>可以通过 apply 尝试从数组中提取出 shift 方法，来调用 arguments 对象。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">callMethod</span>(<span class="hljs-params">obj, method</span>) </span>&#123;
<span class="hljs-keyword">const</span> shift = [].shift;
  shift.call(<span class="hljs-built_in">arguments</span>);
  shift.call(<span class="hljs-built_in">arguments</span>);
  <span class="hljs-keyword">return</span> obj[method].apply(obj, <span class="hljs-built_in">arguments</span>);
&#125;

<span class="hljs-keyword">const</span> obj = &#123;
  <span class="hljs-attr">add</span>: <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">x, y</span>) </span>&#123; <span class="hljs-keyword">return</span> x + y; &#125;
&#125;;
callMethod(obj, <span class="hljs-string">"add"</span>, <span class="hljs-number">17</span>, <span class="hljs-number">25</span>);<span class="hljs-comment">// error: cannot read property "apply" of undefined</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>上述方法出错的原因是 arguments 对象并不是函数参数的副本，所有命名参数都是 arguments 对象中对应索引的别名。因此，即使通过 shift 方法移除 arguments 对象中的元素之后，<code>obj</code> 仍然是 arguments[0] 的别名，<code>method</code> 仍然是 argument[1] 的别名，均已被 <code>shift()</code> 删除掉。</p>
<p>因此我们提取的 <code>obj["add"]</code>，实际上是在提取 <code>17[25]</code>。由于 JavaScript 的自动强制转换规则，引擎将 <code>17</code> 转换为 <code>Number</code> 对象并提取 <code>25</code> 属性，产生 undefined。最后试图提取 undefined 的 <code>apply</code> 属性调用，则报错。</p>
<h3 data-id="heading-28">严格模式</h3>
<p>而在严格模式下，函数参数不支持对其 arguments 对象取别名。下列例子通过编写一个更新 arguments 对象某个元素的函数来说明这个差异。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">strict</span>(<span class="hljs-params">x</span>) </span>&#123;
<span class="hljs-meta">  "use strict"</span>;
  <span class="hljs-built_in">arguments</span>[<span class="hljs-number">0</span>] = <span class="hljs-string">"modified"</span>;
  <span class="hljs-built_in">console</span>.log(<span class="hljs-built_in">arguments</span>[<span class="hljs-number">0</span>], x);
  <span class="hljs-keyword">return</span> x === <span class="hljs-built_in">arguments</span>[<span class="hljs-number">0</span>];
&#125;

<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">nonstrict</span>(<span class="hljs-params">x</span>) </span>&#123;
  <span class="hljs-built_in">arguments</span>[<span class="hljs-number">0</span>] = <span class="hljs-string">"modified"</span>;
  <span class="hljs-built_in">console</span>.log(<span class="hljs-built_in">arguments</span>[<span class="hljs-number">0</span>], x);
  <span class="hljs-keyword">return</span> x === <span class="hljs-built_in">arguments</span>[<span class="hljs-number">0</span>];
&#125;

strict(<span class="hljs-string">"unmodified"</span>);<span class="hljs-comment">// false</span>
nonstrict(<span class="hljs-string">"unmodified"</span>);<span class="hljs-comment">// true</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p><code>strict</code> 中，严格模式下，arguments 不是函数参数别名，因此 <code>modified === unmodified</code> 为 false。<code>nonstrict</code> 中，通过别名改变了参数，<code>modified === modified</code> 为 true。</p>
<h3 data-id="heading-29">复制 arguments 对象</h3>
<p>因此，永远不要直接修改 <code>arguments</code> 对象。可以通过一开始复制参数重的元素到一个真正数组的方法，来避免这个意外。如浅拷贝：<code>const args = [...arguments];</code>。</p>
<p>因此通过 <code>slice</code> 方法来获取 <code>callMethod</code> 的第三、四个参数，进而调用我们第一个例子方法：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">callMethod</span>(<span class="hljs-params">obj, method</span>) </span>&#123;
<span class="hljs-keyword">const</span> shift = [].shift;
  <span class="hljs-keyword">const</span> arg = [...arguments].slice(<span class="hljs-number">2</span>);
  <span class="hljs-keyword">return</span> obj[method].apply(obj, arg);
&#125;

<span class="hljs-keyword">const</span> obj = &#123;
  <span class="hljs-attr">add</span>: <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">x, y</span>) </span>&#123; <span class="hljs-keyword">return</span> x + y; &#125;
&#125;;
callMethod(obj, <span class="hljs-string">"add"</span>, <span class="hljs-number">17</span>, <span class="hljs-number">25</span>);<span class="hljs-comment">// 42</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-30">总结</h3>
<ul>
<li>永远不要修改 arguments 对象。</li>
<li>将 arguments 对象复制到一个真正的数组中再进行函数参数的操作。</li>
</ul>
<h2 data-id="heading-31">第 24 条：使用变量保存 arguments 的引用</h2>
<h3 data-id="heading-32">迭代器</h3>
<p>迭代器是一个可以顺序存取数据集合的一些，其中 <code>next</code> 方法可以获取序列中的下一个值。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> it = values(<span class="hljs-number">1</span>, <span class="hljs-number">4</span>, <span class="hljs-number">1</span>, <span class="hljs-number">4</span>, <span class="hljs-number">2</span>, <span class="hljs-number">1</span>, <span class="hljs-number">3</span>, <span class="hljs-number">5</span>, <span class="hljs-number">6</span>);
it.next();<span class="hljs-comment">// 1</span>
it.next();<span class="hljs-comment">// 4</span>
it.next();<span class="hljs-comment">// 1</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>我们希望写一个便利的函数，可以接收任意数量的参数，并为这些值建立一个迭代器。由于 values 函数必须能够接收任意数量的参数，所以我们可以构造迭代器对象来遍历 arguments 对象的元素。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">values</span>(<span class="hljs-params"></span>) </span>&#123;
  <span class="hljs-keyword">let</span> i = <span class="hljs-number">0</span>;
  <span class="hljs-keyword">const</span> = <span class="hljs-built_in">arguments</span>.length;
  <span class="hljs-keyword">return</span> &#123;
    <span class="hljs-attr">hasNext</span>: <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params"></span>) </span>&#123;
      <span class="hljs-keyword">return</span> i < n;
    &#125;,
    <span class="hljs-attr">next</span>: <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params"></span>) </span>&#123;
      <span class="hljs-keyword">if</span> (i >= n) &#123;
        <span class="hljs-keyword">throw</span> <span class="hljs-keyword">new</span> <span class="hljs-built_in">Error</span>(<span class="hljs-string">"end of iteration"</span>);
      &#125;
      <span class="hljs-keyword">return</span> <span class="hljs-built_in">arguments</span>[i++];<span class="hljs-comment">// wrong arguments</span>
    &#125;;
  &#125;;
&#125;;

<span class="hljs-keyword">const</span> it = values(<span class="hljs-number">1</span>, <span class="hljs-number">4</span>, <span class="hljs-number">1</span>, <span class="hljs-number">4</span>, <span class="hljs-number">2</span>, <span class="hljs-number">1</span>, <span class="hljs-number">3</span>, <span class="hljs-number">5</span>, <span class="hljs-number">6</span>);
it.next();<span class="hljs-comment">// undefined</span>
it.next();<span class="hljs-comment">// undefined</span>
it.next();<span class="hljs-comment">// undefined</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这段代码中，<strong>一个新的 arguments 变量被隐式地绑定到每个函数体内</strong>。迭代器的 <code>next</code> 方法含有自己的 arguments 变量，而非 <code>values </code> 函数的变量，故返回的 arguments[i++] 均为 undefined。</p>
<h3 data-id="heading-33">局部保存</h3>
<p>我们只需简单地在我们感兴趣的 arguments 对象作用域内绑定一个新的局部变量，并确保嵌套函数只能引用这个显示命名的变量。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">values</span>(<span class="hljs-params"></span>) </span>&#123;
  <span class="hljs-keyword">let</span> i = <span class="hljs-number">0</span>;
  <span class="hljs-keyword">const</span> n = <span class="hljs-built_in">arguments</span>.length, arr = <span class="hljs-built_in">arguments</span>;
  <span class="hljs-keyword">return</span> &#123;
    <span class="hljs-attr">hasNext</span>: <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params"></span>) </span>&#123;
      <span class="hljs-keyword">return</span> i < n;
    &#125;,
    <span class="hljs-attr">next</span>: <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params"></span>) </span>&#123;
      <span class="hljs-keyword">if</span> (i >= n) &#123;
        <span class="hljs-keyword">throw</span> <span class="hljs-keyword">new</span> <span class="hljs-built_in">Error</span>(<span class="hljs-string">"end of iteration"</span>);
      &#125;
      <span class="hljs-keyword">return</span> arr[i++];<span class="hljs-comment">// wrong arguments</span>
    &#125;;
  &#125;;
&#125;;

<span class="hljs-keyword">const</span> it = values(<span class="hljs-number">1</span>, <span class="hljs-number">4</span>, <span class="hljs-number">1</span>, <span class="hljs-number">4</span>, <span class="hljs-number">2</span>, <span class="hljs-number">1</span>, <span class="hljs-number">3</span>, <span class="hljs-number">5</span>, <span class="hljs-number">6</span>);
it.next();<span class="hljs-comment">// 1</span>
it.next();<span class="hljs-comment">// 4</span>
it.next();<span class="hljs-comment">// 1</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-34">总结</h3>
<ul>
<li>当引用 arguments 时，当心函数嵌套层级。</li>
<li>绑定一个明确作用域的引用到 arguments 变量，从而可以在嵌套的函数中引用它。</li>
</ul>
<h2 data-id="heading-35">第 25 条：使用 bind 方法提取具有确定接收者的方法</h2>
<h3 data-id="heading-36">函数接收者</h3>
<p>由于方法与对象值为函数的属性没有区别，因此很容易提取对象的方法并将提取出的函数作为回调函数直接传递给高阶函数。这样很容易<strong>忘记将提取出的函数的接收者绑定到该函数被提取出的对象上。</strong></p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> buffer = &#123;
  <span class="hljs-attr">entries</span>: [],
  <span class="hljs-attr">add</span>: <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">s</span>) </span>&#123;
    <span class="hljs-built_in">this</span>.entries.push(s);
  &#125;
&#125;
<span class="hljs-keyword">const</span> source = [<span class="hljs-string">"867"</span>, <span class="hljs-string">"-"</span>, <span class="hljs-string">"5309"</span>];
source.forEach(buffer.add);<span class="hljs-comment">// error: entries is undefined</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>在 forEach 调用的 <code>buffer.add</code> 中的接收者并不是 buffer 对象。函数的接收者取决于它是如何被调用的，而我们将它传递给了 <code>forEach</code> 方法。<code>forEach</code> 方法的实现使用全局对象作为默认的接收者，全局对象没有 <code>entries</code> 属性，因此抛出 <code>undefined</code> 错误。</p>
<p>而 <code>forEach</code> 方法允许调用者提供一个可选的参数作为回调函数的接收者：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> buffer = &#123;
  <span class="hljs-attr">entries</span>: [],
  <span class="hljs-attr">add</span>: <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">s</span>) </span>&#123;
    <span class="hljs-built_in">this</span>.entries.push(s);
  &#125;
&#125;
<span class="hljs-keyword">const</span> source = [<span class="hljs-string">"867"</span>, <span class="hljs-string">"-"</span>, <span class="hljs-string">"5309"</span>];
source.forEach(buffer.add, buffer);
buffer.join();<span class="hljs-comment">// "867-5309"</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-37">显示调用</h3>
<p>若是高阶函数没有为使用者提供其回调函数的接收者，另一个好的解决方法是创建使用适当的方法调用语法来调用 <code>buffer.add</code> 的一个局部函数。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> source = [<span class="hljs-string">"867"</span>, <span class="hljs-string">"-"</span>, <span class="hljs-string">"5309"</span>];
source.forEach(<span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">s</span>) </span>&#123;
  buffer.add(s);
&#125;)
buffer.join();<span class="hljs-comment">// "867-5309"</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这里创建一个显式地以 <code>buffer</code> 对象方法的方式调用 <code>add</code> 的封装函数。不管封装函数如何被调用，它总能确保其参数推送到接收者中。</p>
<h3 data-id="heading-38">bind</h3>
<p>创建一个函数用来实现绑定其接收者到一个指定对象是非常常见的，因此 ES5 标准库采用函数对象的 <code>bind</code> 方法。该方法需要接受一个接收者对象，并产生一个以该接收者对象方法调用的方式调用原来的函数的封装函数。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> source = [<span class="hljs-string">"867"</span>, <span class="hljs-string">"-"</span>, <span class="hljs-string">"5309"</span>];
source.forEach(buffer.add.bind(buffer));
buffer.join();<span class="hljs-comment">// "867-5309"</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>**<code>buffer.add.bind(buffer)</code> 创建了一个新函数而不是修改了 <code>buffer.add</code> 函数。**新函数的行为就像原来函数的行为，但它的接收者绑定到了 <code>buffer</code> 对象，而原有函数的接收者保持不变。</p>
<p><code>buffer.add === buffer.add.bind(buffer);// false</code></p>
<p>因此这意味着调用 <code>bind</code> 方法是安全的，即使是一个可能在程序的其他部分被共享的函数，这对于原型对象上的共享方法尤其重要。<strong>当在任何的原型后代中调用共享方法时，该方法仍能正常工作。</strong></p>
<h3 data-id="heading-39">总结</h3>
<ul>
<li>要注意，提取一个方法不会将方法的接收者绑定到该方法的对象上。</li>
<li>当给高阶函数传递对象方法时，使用匿名函数在适当的接收者上调用该方法。</li>
<li>使用 bind 方法创建绑定到适当接收者的函数。</li>
</ul>
<h2 data-id="heading-40">第 26 条：使用 bind 方法实现函数柯里化</h2>
<h3 data-id="heading-41">函数柯里化</h3>
<p><strong>将函数与其参数的一个子集绑定的技术称为函数柯里化</strong>，以逻辑学家 <strong>Haskell Curry</strong> 的名字命名。比起显式地封装函数，函数柯里化是一种简洁的、使用更少引用来实现函数委托的方式。</p>
<p>而函数对象的 bind 方法除了具有将方法绑定到接收者的用途外，还可以自动构造匿名函数。如有一个装配 URL 字符串的简单函数：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">simpleURL</span>(<span class="hljs-params">protocol, domain, path</span>) </span>&#123;
  <span class="hljs-keyword">return</span> protocol + <span class="hljs-string">"://"</span> + domain + <span class="hljs-string">"/"</span> + path;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>程序可能需要将特定站点的路径字符串构建为绝对路径 URL，一种自然的方式是对数组使用 ES5 提供的 map 方法来实现：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> urls = paths.map(<span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">path</span>) </span>&#123;
  <span class="hljs-keyword">return</span> simpleURL(<span class="hljs-string">"http"</span>, siteDomain, path);
&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>上述列子中的匿名函数对 map 方法的每次迭代使用相同的协议字符串和网站域名字符串。传给 aimpleURL 函数的前两个参数对于每次迭代都是固定的，仅第三个参数是变化的。<strong>我们可以通过调用 simpleURL 函数的 bind 方法来自动构造该匿名函数</strong></p>
<p><code>const urls = paths.map(simpleURL.bind(null, "http", siteDomain));</code></p>
<p>simpleURL.bind 的调用产生了一个委托到 simpleURL 的新函数，bind 方法的第一个参数提供了接收者的值。由于 simpleURL 不需要引用 this 变量，所以可以使用 null 来替代。</p>
<p>simpleURL.bind 的其余参数和提供给新函数的所有参数共同组成了传递给 simpleURL 的参数。<strong>使用单个参数 path 调用 <code>simpleURL.bind</code>，则该执行结果是一个委托到 <code>simpleURL("http", siteDomain, path)</code> 的函数</strong></p>
<h3 data-id="heading-42">总结</h3>
<ul>
<li>使用 bind 方法实现函数柯里化，即创建一个固定需求参数子集的委托函数。</li>
<li>传入 null 或 undefined 作为接收者的参数来实现函数柯里化，从而忽略其接收者。</li>
</ul>
<h2 data-id="heading-43">第 27 条：使用闭包而不是字符串来封装代码</h2>
<h3 data-id="heading-44">字符串封装</h3>
<p>函数是一种将代码作为数据结构存储的便利方式，这些代码可以随后被执行，也是 JavaScript 异步 I/O 方法的核心。与此同时，也可以将代码表示为字符串的形式传递给 <code>eval</code> 函数以达到同样的功能。</p>
<p>而我们应该将代码表示为函数而非字符串，其不够灵活的一个重要原因是：<strong>它们不是闭包</strong>。假设有一个简单的多次重复用户提供的动作的函数：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">repeat</span>(<span class="hljs-params">n, action</span>) </span>&#123;
  <span class="hljs-keyword">for</span> (<span class="hljs-keyword">let</span> i = <span class="hljs-number">0</span>; i < n; i++) &#123;
    <span class="hljs-built_in">eval</span>(action);
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>该函数在全局作用域会工作得很好，因为 <code>eval</code> 函数会将出现在字符串中的所有变量引用作为全局变量来解释。而若简单地将代码移到函数中来调用，那么其变量期望为局部变量，而非全局变量。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">benchmark</span>(<span class="hljs-params"></span>) </span>&#123;
  <span class="hljs-keyword">const</span> start = [], end = [], timings = [];
  repeat(<span class="hljs-number">1000</span>, <span class="hljs-string">"start.push(Date.now()); f(); end.push(Date.now());"</span>);
  <span class="hljs-keyword">for</span> (<span class="hljs-keyword">let</span> i = <span class="hljs-number">0</span>, n = start.length; i < n; i++) &#123;
    timings[i] = end[i] - start[i];
  &#125;
  <span class="hljs-keyword">return</span> timings;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>该函数会导致 repeat 函数引用全局的 start 和 end 变量。将会发生意料不到的情况，全局变量未定义，抛出 ReferenceError 异常。代码恰好绑定到 start 和 end 全局对象的 push 方法，程序将变得无法预测。</p>
<h3 data-id="heading-45">闭包封装</h3>
<p>因此我们应该接受闭包封装而非字符串。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">repeat</span>(<span class="hljs-params">n, action</span>) </span>&#123;
  <span class="hljs-keyword">for</span> (<span class="hljs-keyword">let</span> i = <span class="hljs-number">0</span>; i < n; i++) &#123;
    <span class="hljs-built_in">eval</span>(action);
  &#125;
&#125;

<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">benchmark</span>(<span class="hljs-params"></span>) </span>&#123;
  <span class="hljs-keyword">const</span> start = [], end = [], timings = [];
  repeat(<span class="hljs-number">1000</span>, <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params"></span>) </span>&#123;
   start.push(<span class="hljs-built_in">Date</span>.now()); 
    f(); 
    end.push(<span class="hljs-built_in">Date</span>.now());
  &#125;);
  <span class="hljs-keyword">for</span> (<span class="hljs-keyword">let</span> i = <span class="hljs-number">0</span>, n = start.length; i < n; i++) &#123;
    timings[i] = end[i] - start[i];
  &#125;
  <span class="hljs-keyword">return</span> timings;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>相较于 eval 的另一个问题是，通常一些高性能的引擎很难优化字符串中的代码，因为编译器不能尽可能早地获得源代码来及时优化代码。而函数表达式在其代码出现的同时就能被编译，更适合标准化编译和优化。</p>
<h3 data-id="heading-46">总结</h3>
<ul>
<li>当将字符串传递给 eval 函数以执行它们的 API 时，绝不要在字符串中包含局部变量引用。</li>
<li>接受闭包优于使用 eval 函数执行字符串。</li>
</ul>
<h2 data-id="heading-47">第 28 条：不要信赖函数对象的 toString 方法</h2>
<p>JavaScript 函数可以将其源代码重现为字符串的能力，聪明的黑客偶然会通过巧妙的方法用到它：</p>
<pre><code class="hljs language-js copyable" lang="js">(<span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">x</span>)</span>&#123;
  <span class="hljs-keyword">return</span> x + <span class="hljs-number">1</span>;
&#125;).toString();<span class="hljs-comment">// "function(x) &#123;\n return x + 1;\n&#125;"</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>然而 ECMAScript 标准对函数对象的 toString 方法的返回结果并没有任何要求，这意味这不同的 JavaScript 引擎将产生不同的字符串，甚至与该函数并不相关。</p>
<pre><code class="hljs language-js copyable" lang="js">(<span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">x</span>) </span>&#123;
  <span class="hljs-keyword">return</span> x + <span class="hljs-number">1</span>;
&#125;).bind(<span class="hljs-number">16</span>).toString();<span class="hljs-comment">// "function(x) &#123;\n[native code]\n&#125;"</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>该例子失败的原因是使用了由宿主环境的内置库提供的函数，而非纯 JavaScript 实现。在许多宿主环境中，bind 函数是由其他编译语言实现的，宿主环境提供的是一个编译后的函数，在此环境下啊函数没有 JavaScript 源代码供 toString 显示。</p>
<p>其次，由于标准允许浏览器引擎改变 toString 方法的输出，这很容易使编写的程序在一个 JavaScript 系统中正确运行，在其他 JavaScript 中却无法正确运行。</p>
<p>程序对函数的源代码字符串的具体细节也很敏感，即使 JavaScript 的实现有一点细微的变化（如空格格式化）都可能破坏代码。</p>
<pre><code class="hljs language-js copyable" lang="js">(<span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">x</span>) </span>&#123;
  <span class="hljs-keyword">return</span> <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params">y</span>) </span>&#123;
    <span class="hljs-keyword">return</span> x + y;
  &#125;
&#125;)(<span class="hljs-number">42</span>).toString();<span class="hljs-comment">// "function(y) &#123;\n return x + y;\n&#125;"</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>而且由 toString 方法生产的源代码并不展示闭包中保存的与内部变量引用相关的值。尽管函数实际上是一个绑定 x 为 42 的闭包，但结果字符串仍然包含一个引用了 x 的变量。</p>
<p>因此 toString 方法的这些局限使其用来提取函数源代码并不是特别有用和值得信赖，应该避免使用它。对提取函数源代码相当复杂的使用应当采用精心制作的 JavaScript 解释器和处理库。</p>
<blockquote>
<p>最后，将 JavaScript 函数看作一个不该违背抽象是最稳妥的。</p>
</blockquote>
<h3 data-id="heading-48">总结</h3>
<ul>
<li>当调用函数的 toString 方法时，并没有要求 JavaScript 引擎能够精确地获取到函数的源代码。</li>
<li>在不同的引擎下调用 toString 方法的结果可能不同。</li>
<li>toString 方法的执行结果并不会暴露存储在闭包中的局部变量值。</li>
<li>避免使用函数对象的 toString 方法。</li>
</ul>
<h2 data-id="heading-49">第 29 条：避免使用非标准的栈检查属性</h2>
<h3 data-id="heading-50">栈检查属性</h3>
<p>调用栈是指当前正在执行的活动函数链，曾经许多 JavaScript 环境都提供检查调用栈的功能。在某些旧的宿主环境中，每个 arguments 对象都含有两个额外的属性：<code>arguments.callee</code> 和 <code>arguments.caller</code>。前者指向使用该 arguments 对象被调用的函数，后者指向调用该 arguments 对象的函数。</p>
<p><code>arguments.callee</code> 除了允许匿名函数递归地引用其自身之外，就没有更多的用途了。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> factorial = (<span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">n</span>) </span>&#123;
  <span class="hljs-keyword">return</span> (n <= <span class="hljs-number">1</span>) ? <span class="hljs-number">1</span> : (n * <span class="hljs-built_in">arguments</span>.callee(n-<span class="hljs-number">1</span>));
&#125;) 
<span class="hljs-comment">// 等价于</span>
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">factorial</span>(<span class="hljs-params">n</span>) </span>&#123;
  <span class="hljs-keyword">return</span> (n <= <span class="hljs-number">1</span>) ? <span class="hljs-number">1</span> : (n * factorial(n - <span class="hljs-number">1</span>));
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><code>arguments.caller</code> 属性指向的是使用该 arguments 对象调用函数的函数，处于安全考虑，大多数环境已经移除了此特性。许多 JavaScript 环境也提供了一个相似的函数对象属性 <code>caller</code> 属性，指向函数最近调用者。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">revealCaller</span>(<span class="hljs-params"></span>) </span>&#123;
  <span class="hljs-keyword">return</span> revealCaller.caller;
&#125;
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">start</span>(<span class="hljs-params"></span>) </span>&#123;
  <span class="hljs-keyword">return</span> revealCaller();
&#125;
start() === start;<span class="hljs-comment">// true</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-51">栈跟踪</h3>
<p>栈跟踪是一个题哦那个当前调用栈快照的数据结构，使用该属性来获取栈跟踪是很有诱惑力。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">getCallStack</span>(<span class="hljs-params"></span>) </span>&#123;
  <span class="hljs-keyword">const</span> stack = [];
  <span class="hljs-keyword">for</span> (<span class="hljs-keyword">let</span> f = getCallStack.caller; f; f = f.caller) &#123;
    stack.push(f);
  &#125;
  <span class="hljs-keyword">return</span> stack;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>对于简单的调用栈，getCallStack 函数可以很好地工作。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">f1</span>(<span class="hljs-params"></span>) </span>&#123;
  <span class="hljs-keyword">return</span> getCallStack();
&#125;
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">f2</span>(<span class="hljs-params"></span>) </span>&#123;
  <span class="hljs-keyword">return</span> f1();
&#125;
<span class="hljs-keyword">const</span> trace = f2();
trace;<span class="hljs-comment">// [f1, f2]</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>如果某个函数在调用栈中出现了不止一次，那么栈检查逻辑将会陷入循环。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">f</span>(<span class="hljs-params">n</span>) </span>&#123;
  <span class="hljs-keyword">return</span> n === <span class="hljs-number">0</span> ? getCallStack() : f(n - <span class="hljs-number">1</span>);
&#125;
<span class="hljs-keyword">const</span> trace = f(<span class="hljs-number">1</span>);<span class="hljs-comment">// infinite loop</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>由于函数 f 递归地调用其自身，因此其 caller 属性会自动更新，指回到函数 f。所以函数 getCallStack 会陷入无限地查找函数 f 的循环之中，因此该栈跟踪出错。</p>
<p>这些栈检查属性都是非标准的，在移植性或适用性上很受限制，并且在 ES5 的严格函数中，是被禁止使用的。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">f</span>(<span class="hljs-params"></span>) </span>&#123;
<span class="hljs-meta">  "use strict"</span>;
  <span class="hljs-keyword">return</span> f.caller;
&#125;
f();<span class="hljs-comment">// error: caller may not be accessed on strict functions</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>最好的策略是避免栈检查，如果为了调试而检查栈，那么更为可能的方式是使用交互式的调试器。</p>
<h3 data-id="heading-52">总结</h3>
<ul>
<li>避免使用非标准的 arguments.caller 和 arguments.callee 栈检查属性，因为它们不具备良好的移植性。</li>
<li>避免使用非标准的函数对象 caller 属性，在包含全部栈信息方面，它是不可能靠的。</li>
<li>在严格模式下禁用栈检查属性。</li>
</ul>
<h1 data-id="heading-53">后言</h1>
<p>以上为 <strong>第三章内容</strong> 学习了 18~29 条规则 <code>着重于熟悉 JavaScript 函数的具体细节规则</code></p>
<blockquote>
<p>系列如下：</p>
<ul>
<li><a href="https://juejin.cn/post/6978290455834263565" target="_blank" title="https://juejin.cn/post/6978290455834263565">《Effective JS》的 68 条准则「一至七条」</a></li>
<li><a href="https://juejin.cn/post/6979219927907450911" target="_blank" title="https://juejin.cn/post/6979219927907450911">《Effective JS》的 68 条准则「八至十七条」</a></li>
<li>《Effective JS》的 68 条准则「十八至二十九条」</li>
<li>《Effective JS》的 68 条准则「三十至四十二条」</li>
<li>《Effective JS》的 68 条准则「四十三至五十二条」</li>
<li>《Effective JS》的 68 条准则「五十三至六十条」</li>
<li>《Effective JS》的 68 条准则「六十一至六十八条」</li>
</ul>
<p><em>若无链接，则是正在学习当中...</em></p>
</blockquote></div>  
</div>
            