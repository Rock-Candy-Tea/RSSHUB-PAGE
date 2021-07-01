
---
title: '每位 Web 开发者都应该知道的 7 个 JavaScript 基础知识'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=9141'
author: 掘金
comments: false
date: Wed, 30 Jun 2021 08:54:49 GMT
thumbnail: 'https://picsum.photos/400/300?random=9141'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><blockquote>
<ul>
<li>原文地址：<a href="https://betterprogramming.pub/7-javascript-fundamentals-every-web-developer-should-know-8c0f7e491167" target="_blank" rel="nofollow noopener noreferrer">7 JavaScript Fundamentals Every Web Developer Should Know</a></li>
<li>原文作者：<a href="https://cristiansalcescu.medium.com/" target="_blank" rel="nofollow noopener noreferrer">Cristian Salcescu</a></li>
<li>译文出自：<a href="https://github.com/xitu/gold-miner" target="_blank" rel="nofollow noopener noreferrer">掘金翻译计划</a></li>
<li>本文永久链接：<a href="https://github.com/xitu/gold-miner/blob/master/article/2021/7-JavaScript-Fundamentals-Every-Web-Developer-Should-Know.md" target="_blank" rel="nofollow noopener noreferrer">github.com/xitu/gold-m…</a></li>
<li>译者：<a href="https://github.com/HydeSong" target="_blank" rel="nofollow noopener noreferrer">Hyde Song</a></li>
<li>校对者：<a href="https://github.com/PassionPenguin" target="_blank" rel="nofollow noopener noreferrer">PassionPenguin</a>、<a href="https://github.com/greycodee" target="_blank" rel="nofollow noopener noreferrer">greycodee</a></li>
</ul>
</blockquote>
<p>在本文中，我们将讨论我认为 JavaScript 最重要、最独特的一些特性。</p>
<h2 data-id="heading-0">1、函数是独立的行为单元</h2>
<p>函数是基本单位，但这里重要的一点是，函数是独立的！在 Java 或 C# 等其他语言中，函数必须在类内声明，但在 JavaScript 中不是这样的。</p>
<p>函数可以在全局中被定义，也可以在模块里定义为可重用的单位。</p>
<h2 data-id="heading-1">2、对象是属性的动态集合</h2>
<p>对象实际上只是属性的集合。在其他语言中，它们被称为 Map、HashMap 或 HashTable。</p>
<p>对象是动态的，即一旦创建，就可以添加、编辑或删除属性。</p>
<p>下面是一个使用字面量语法定义的简单对象。它有两个属性：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> game = &#123;
  <span class="hljs-attr">title</span> : <span class="hljs-string">'Settlers'</span>,
  <span class="hljs-attr">developer</span>: <span class="hljs-string">'Ubisoft'</span>
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-2">3、对象继承自其他对象</h2>
<p>如果你曾经使用的语言是类似于 Java 或 C# 等基于 <code>class</code> 的语言，你可能习惯于从其他 <code>class</code> 继承 <code>class</code>。但是，JavaScript 不是这样的。</p>
<p>对象继承自称为 <code>prototypes</code> 的对象。</p>
<p>如前所述，在这种语言中，对象是属性的集合。当创建一个对象时，他有一个名为 <code>__proto__</code> 的隐藏属性，它引用其他对象。这个被引用的对象称为 <code>prototype</code>。</p>
<p>下面是一个创建空对象的例子（可以说，没有属性的对象）：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> obj = &#123;&#125;;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>即使 obj 看起来是空的没有任何属性，它实际上也是有一个隐藏属性 <code>__proto__</code> 的：</p>
<pre><code class="hljs language-js copyable" lang="js">obj.__proto__ === <span class="hljs-built_in">Object</span>.prototype;
<span class="hljs-comment">//true</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>在这类对象上，我们可以访问还没有定义的方法，例如 <code>toString</code> 方法，即使我们还没有定义这样的方法。这怎么可能呢？</p>
<p>此方法继承自 <code>Object.prototype</code>。当尝试访问该方法时，JS 引擎首先尝试在当前对象上查找该方法，然后再查找其原型上的属性。</p>
<p>不要被 <code>class</code> 关键字误导了。<code>class</code> 只是原型系统的语法糖，帮助来自基于 <code>class</code> 语言的开发者熟悉 JavaScript。</p>
<h2 data-id="heading-3">4、函数就是值</h2>
<p>在 JavaScript 中，函数就是值。就像其他值一样，函数可以赋值给变量：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> sum = <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">x,y</span>)</span>&#123; <span class="hljs-keyword">return</span> x + y &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这在其他编程语言中是做不到的。</p>
<p>与其他值一样，函数可以传递给不同的函数或被函数返回。下面是一个函数返回另一个函数的示例：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">startsWith</span>(<span class="hljs-params">text</span>)</span>&#123;
  <span class="hljs-keyword">return</span> <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">name</span>)</span>&#123;
    <span class="hljs-keyword">return</span> name.startsWith(text);
  &#125;
&#125;

<span class="hljs-keyword">const</span> games = [<span class="hljs-string">'Fornite'</span>, <span class="hljs-string">'Overwatch'</span>, <span class="hljs-string">'Valorant'</span>];
<span class="hljs-keyword">const</span> newGames = games.filter(startsWith(<span class="hljs-string">'Fo'</span>));
<span class="hljs-built_in">console</span>.log(newGames);
<span class="hljs-comment">//["Fornite"]</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>在同一个示例中，我们可以看到 <code>startsWith</code> 函数返回的函数是如何作为参数发送到 <code>filter</code> 数组方法的。</p>
<h2 data-id="heading-4">5、函数可以闭包</h2>
<p>函数内部可以定义函数。内部函数可以引用其他函数的变量。</p>
<p>而且，外部函数执行后，内部函数可以引用外部函数的变量。下面是关于这方面的例子；</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">createCounter</span>(<span class="hljs-params"></span>)</span>&#123;
  <span class="hljs-keyword">let</span> x = <span class="hljs-number">0</span>;
  <span class="hljs-keyword">return</span> <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params"></span>)</span>&#123;
    x = x + <span class="hljs-number">1</span>;
    <span class="hljs-keyword">return</span> x;
  &#125;
&#125;

<span class="hljs-keyword">const</span> count = createCounter();
<span class="hljs-built_in">console</span>.log(count());<span class="hljs-comment">//1</span>
<span class="hljs-built_in">console</span>.log(count());<span class="hljs-comment">//2</span>
<span class="hljs-built_in">console</span>.log(count());<span class="hljs-comment">//3</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p><code>count</code> 函数可以从 <code>createCounter</code> 父函数访问 <code>x</code> 变量，即使在执行之后也是如此。<code>count</code> 就是闭包函数。</p>
<h2 data-id="heading-5">6、基本数据类型被视为对象</h2>
<p>JavaScript 把基本类型当作对象，从而给人一种错觉。实际上，基本类型并不是对象. 基本类型不是属性的集合。</p>
<p>然而，我们可以在基本类型上调用方法。比如，我们可以在字符串上调用 <code>toUpperCase</code> 方法：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> upperText = <span class="hljs-string">'Minecraft'</span>.toUpperCase();
<span class="hljs-built_in">console</span>.log(upperText);
<span class="hljs-comment">//'MINECRAFT'</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>像 <code>Minecraft</code> 这样的简单文本是基本类型，自身没有任何方法。不过 JavaScript 会使用内置的 String 构造函数将其转换为对象，然后我们就能够对新创建的对象执行 <code>toUpperCase</code> 方法。</p>
<p>通过在底层把基本类型转换为包装对象，JavaScript 允许你调用方法，从而视它们为对象。</p>
<h2 data-id="heading-6">7、JavaScript 是一种单线程语言</h2>
<p>JavaScript 单线程的。这意味着在特定时间只执行一条语句。</p>
<p>在主线程中，两个函数不能同时执行。</p>
<p>你也许听说过像 <a href="https://developer.mozilla.org/en-US/docs/Web/Guide/Performance/Using_web_workers" target="_blank" rel="nofollow noopener noreferrer">web workers</a> 这种并行执行函数的方式，但是 workers 不会和主线程共享数据。它们只通过信息传递来通信 —— 什么都不是共享的。</p>
<p>这就容易理解了，我们只需要注意让函数执行更快就好了。耗费长时间去执行一个函数会让页面无响应。</p>
<p>谢谢阅读。编码快乐!</p>
<blockquote>
<p>如果发现译文存在错误或其他需要改进的地方，欢迎到 <a href="https://github.com/xitu/gold-miner" target="_blank" rel="nofollow noopener noreferrer">掘金翻译计划</a> 对译文进行修改并 PR，也可获得相应奖励积分。文章开头的 <strong>本文永久链接</strong> 即为本文在 GitHub 上的 MarkDown 链接。</p>
</blockquote>
<hr>
<blockquote>
<p><a href="https://github.com/xitu/gold-miner" target="_blank" rel="nofollow noopener noreferrer">掘金翻译计划</a> 是一个翻译优质互联网技术文章的社区，文章来源为 <a href="https://juejin.im/" target="_blank" rel="nofollow noopener noreferrer">掘金</a> 上的英文分享文章。内容覆盖 <a href="https://github.com/xitu/gold-miner#android" target="_blank" rel="nofollow noopener noreferrer">Android</a>、<a href="https://github.com/xitu/gold-miner#ios" target="_blank" rel="nofollow noopener noreferrer">iOS</a>、<a href="https://github.com/xitu/gold-miner#%E5%89%8D%E7%AB%AF" target="_blank" rel="nofollow noopener noreferrer">前端</a>、<a href="https://github.com/xitu/gold-miner#%E5%90%8E%E7%AB%AF" target="_blank" rel="nofollow noopener noreferrer">后端</a>、<a href="https://github.com/xitu/gold-miner#%E5%8C%BA%E5%9D%97%E9%93%BE" target="_blank" rel="nofollow noopener noreferrer">区块链</a>、<a href="https://github.com/xitu/gold-miner#%E4%BA%A7%E5%93%81" target="_blank" rel="nofollow noopener noreferrer">产品</a>、<a href="https://github.com/xitu/gold-miner#%E8%AE%BE%E8%AE%A1" target="_blank" rel="nofollow noopener noreferrer">设计</a>、<a href="https://github.com/xitu/gold-miner#%E4%BA%BA%E5%B7%A5%E6%99%BA%E8%83%BD" target="_blank" rel="nofollow noopener noreferrer">人工智能</a>等领域，想要查看更多优质译文请持续关注 <a href="https://github.com/xitu/gold-miner" target="_blank" rel="nofollow noopener noreferrer">掘金翻译计划</a>、<a href="http://weibo.com/juejinfanyi" target="_blank" rel="nofollow noopener noreferrer">官方微博</a>、<a href="https://zhuanlan.zhihu.com/juejinfanyi" target="_blank" rel="nofollow noopener noreferrer">知乎专栏</a>。</p>
</blockquote></div>  
</div>
            