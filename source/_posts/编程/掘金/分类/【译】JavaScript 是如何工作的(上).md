
---
title: '【译】JavaScript 是如何工作的(上)'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/9392a32893e14f1ea9cfacde67cc0e5d~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Wed, 11 Aug 2021 00:56:11 GMT
thumbnail: 'https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/9392a32893e14f1ea9cfacde67cc0e5d~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;color:#595959;font-size:15px;font-family:-apple-system,system-ui,BlinkMacSystemFont,Helvetica Neue,PingFang SC,Hiragino Sans GB,Microsoft YaHei,Arial,sans-serif;background-image:linear-gradient(90deg,rgba(60,10,30,.04) 3%,transparent 0),linear-gradient(1turn,rgba(60,10,30,.04) 3%,transparent 0);background-size:20px 20px;background-position:50%&#125;.markdown-body p&#123;color:#595959;font-size:15px;line-height:2;font-weight:400&#125;.markdown-body p+p&#123;margin-top:16px&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;padding:30px 0;margin:0;color:#135ce0&#125;.markdown-body h1&#123;position:relative;text-align:center;font-size:22px;margin:50px 0&#125;.markdown-body h1:before&#123;position:absolute;content:"";top:-10px;left:50%;width:32px;height:32px;transform:translateX(-50%);background-size:100% 100%;opacity:.36;background-repeat:no-repeat;background:url(data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACAAAAAgCAMAAABEpIrGAAAABGdBTUEAALGPC/xhBQAAACBjSFJNAAB6JgAAgIQAAPoAAACA6AAAdTAAAOpgAAA6mAAAF3CculE8AAABfVBMVEX///8Ad/8AgP8AgP8AgP8Aff8AgP8Af/8AgP8AVf8Af/8Af/8AgP8AgP8Af/8Afv8AAP8Afv8Afv8Aef8AgP8AdP8Afv8AgP8AgP8Acf8Ae/8AgP8Af/8AgP8Af/8Af/8AfP8Afv8AgP8Af/8Af/8Afv8Afv8AgP8Afv8AgP8Af/8Af/8AgP8AgP8Afv8AgP8Af/8AgP8AgP8AgP8Ae/8Afv8Af/8AgP8Af/8AgP8Af/8Af/8Aff8Af/8Abf8AgP8Af/8AgP8Af/8Af/8Afv8AgP8AgP8Afv8Afv8AgP8Af/8Aff8AgP8Afv8AgP8Aff8AgP8AfP8AgP8Ae/8AgP8Af/8AgP8AgP8AgP8Afv8AgP8AgP8AgP8Afv8AgP8AgP8AgP8AgP8AgP8Af/8AgP8Af/8Af/8Aev8Af/8AgP8Aff8Afv8AgP8AgP8AgP8Af/8AgP8Af/8Af/8AgP8Afv8AgP8AgP8AgP8AgP8Af/8AeP8Af/8Af/8Af//////rzEHnAAAAfXRSTlMAD7CCAivatxIDx5EMrP19AXdLEwgLR+6iCR/M0yLRzyFF7JupSXn8cw6v60Q0QeqzKtgeG237HMne850/6Qeq7QaZ+WdydHtj+OM3qENCMRYl1B3K2U7wnlWE/mhlirjkODa9FN/BF7/iNV/2kASNZpX1Wlf03C4stRGxgUPclqoAAAABYktHRACIBR1IAAAACXBIWXMAAAsTAAALEwEAmpwYAAAAB3RJTUUH4gEaBzgZ4yeM3AAAAT9JREFUOMvNUldbwkAQvCAqsSBoABE7asSOBRUVVBQNNuy9996789+9cMFAMHnVebmdm+/bmdtbQv4dOFOW2UjPzgFyLfo6nweKfIMOBYWwFtmMPGz2Yj2pJI0JDq3udJW6VVbmKa9I192VQFV1ktXUAl5NB0cd4KpnORqsEO2ZIRpF9gJfE9Dckqq0KuZt7UAH5+8EPF3spjsRpCeQNO/tA/qDwIDA+OCQbBoKA8NOdjMySgcZGVM6jwcgRuUiSs0nlPFNSrEpJfU0jTLD6llqbvKxei7OzvkFNQohi0vAsj81+MoqsCaoPOQFgus/1LyxichW+hS2JWCHZ7VlF9jb187pIAYcHiViHAMnp5mTjJ8B5xeEXF4B1ze/fTh/C0h398DDI9HB07O8ci+vRBdvdGnfP4gBuM8vw7X/G3wDmFhFZEdxzjMAAAAldEVYdGRhdGU6Y3JlYXRlADIwMTgtMDEtMjZUMDc6NTY6MjUrMDE6MDA67pVWAAAAJXRFWHRkYXRlOm1vZGlmeQAyMDE4LTAxLTI2VDA3OjU2OjI1KzAxOjAwS7Mt6gAAABl0RVh0U29mdHdhcmUAd3d3Lmlua3NjYXBlLm9yZ5vuPBoAAAAWdEVYdFRpdGxlAGp1ZWppbl9sb2dvIGNvcHlxapmKAAAAV3pUWHRSYXcgcHJvZmlsZSB0eXBlIGlwdGMAAHic4/IMCHFWKCjKT8vMSeVSAAMjCy5jCxMjE0uTFAMTIESANMNkAyOzVCDL2NTIxMzEHMQHy4BIoEouAOoXEXTyQjWVAAAAAElFTkSuQmCC)&#125;.markdown-body h2&#123;position:relative;font-size:20px;border-left:4px solid;padding:0 0 0 10px;margin:30px 0&#125;.markdown-body h3&#123;font-size:16px&#125;.markdown-body ul&#123;list-style:disc outside;margin-left:2em;margin-top:1em&#125;.markdown-body li&#123;line-height:2;color:#595959&#125;.markdown-body img.loaded&#123;margin:0 auto;display:block&#125;.markdown-body blockquote&#123;background:#fff9f9;margin:2em 0;padding:2px 20px;border-left:4px solid #b2aec5&#125;.markdown-body blockquote p&#123;color:#666;line-height:2&#125;.markdown-body a&#123;color:#036aca;border-bottom:1px solid rgba(3,106,202,.8);font-weight:400;text-decoration:none&#125;.markdown-body em strong,.markdown-body strong&#123;color:#036aca&#125;.markdown-body hr&#123;border-top:1px solid #135ce0&#125;.markdown-body pre&#123;overflow:auto&#125;.markdown-body code,.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body table&#123;border-collapse:collapse;margin:1rem 0;overflow-x:auto&#125;.markdown-body table td,.markdown-body table th&#123;border:1px solid #dfe2e5;padding:.6em 1em&#125;.markdown-body table tr&#123;border-top:1px solid #dfe2e5&#125;.markdown-body table tr:nth-child(2n)&#123;background-color:#f6f8fa&#125;</style><blockquote>
<p>原文地址：<a href="https://link.juejin.cn/?target=https%3A%2F%2Fbetterprogramming.pub%2Fhow-javascript-works-1706b9b66c4d" target="_blank" rel="nofollow noopener noreferrer" title="https://betterprogramming.pub/how-javascript-works-1706b9b66c4d" ref="nofollow noopener noreferrer">How JavaScript Works. Why understanding the fundamentals is… | by Ionel Hindorean | Better Programming</a></p>
</blockquote>
<p>为什么我们要理解基本原理</p>
<p>你可能想知道为什么有人会在 2019 年费心写一篇关于 JavaScript 核心的长文。</p>
<p>这是因为我相信，如果没有对基础知识的扎实了解，很容易在JS生态系统中迷失方向，而且几乎不可能探索更高级的内容。</p>
<p>了解 JavaScript 的工作原理可以使阅读和编写代码变得更容易，减少挫折感，让你专注于你的应用程序的逻辑，而不是与语言的语法作斗争。</p>
<h2 data-id="heading-0">它是如何工作的？</h2>
<p><strong>计算机不懂JavaScript，浏览器才懂。</strong></p>
<p>除了处理网络请求、监听鼠标点击、解释 HTML 和 CSS 以在屏幕上绘制像素外，浏览器还内置有一个 JavaScript 引擎。</p>
<p>JavaScript 引擎是一个用 C++ 编写的程序，它逐字逐句地查看所有的 JavaScript 代码，并将其 "转化 "为计算机 CPU 能够理解和执行的东西--<a href="https://link.juejin.cn/?target=https%3A%2F%2Fen.wikipedia.org%2Fwiki%2FMachine_code" target="_blank" rel="nofollow noopener noreferrer" title="https://en.wikipedia.org/wiki/Machine_code" ref="nofollow noopener noreferrer">机器代码</a>。</p>
<p>这个过程是同步进行的，也就是说，他们在一条时间线上，而且是按顺序进行。</p>
<p>他们这样做是因为机器代码很难，而且不同的 CPU 制造商的机器代码指令是不同的。所以，他们把所有这些麻烦从JavaScript 开发者那里抽象出来，否则，网络开发会更难，更不受欢迎，我们也不会有像 Medium 这样的东西，让我们可以写像这样的文章（而我现在就在睡觉）。</p>
<p>JavaScript 引擎可以机器的地浏览每一行 JavaScript，一遍又一遍（<a href="https://link.juejin.cn/?target=https%3A%2F%2Fen.wikipedia.org%2Fwiki%2FInterpreter_computing" target="_blank" rel="nofollow noopener noreferrer" title="https://en.wikipedia.org/wiki/Interpreter_computing" ref="nofollow noopener noreferrer">解释器</a>），或者它可以变得更聪明，检测出一些东西，比如经常被调用并且总是产生相同结果的函数。</p>
<p>然后，它可以把这些东西编译成机器代码，只需一次，这样下次遇到它时，它就会运行已经编译好的代码，这就快多了（<a href="https://link.juejin.cn/?target=https%3A%2F%2Fen.wikipedia.org%2Fwiki%2FJust-in-time_compilation" target="_blank" rel="nofollow noopener noreferrer" title="https://en.wikipedia.org/wiki/Just-in-time_compilation" ref="nofollow noopener noreferrer">及时编译</a>）。</p>
<p>或者，它可以提前将整个东西编译成机器代码，然后执行（见<a href="https://link.juejin.cn/?target=https%3A%2F%2Fen.wikipedia.org%2Fwiki%2FCompiler" target="_blank" rel="nofollow noopener noreferrer" title="https://en.wikipedia.org/wiki/Compiler" ref="nofollow noopener noreferrer">编译器</a>）。</p>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fv8%2Fv8" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/v8/v8" ref="nofollow noopener noreferrer">V8</a> 就是这样一个 JavaScript 引擎，谷歌在2008年将其开源。2009年，一个叫 Ryan Dahl 的人想到用 V8 来创建 <a href="https://link.juejin.cn/?target=https%3A%2F%2Fen.wikipedia.org%2Fwiki%2FNode.js" target="_blank" rel="nofollow noopener noreferrer" title="https://en.wikipedia.org/wiki/Node.js" ref="nofollow noopener noreferrer">Node.js</a>，这是一个在浏览器之外的 JavaScript 运行环境，这意味着该语言也可以用于服务器端应用。</p>
<h2 data-id="heading-1">函数执行上下文</h2>
<p>像其他语言一样，JavaScript 对于函数、变量、数据类型，以及这些数据类型可以存储的确切数值，在代码中哪些地方可以访问，哪些地方不可以，等等都有自己的规则。</p>
<p>这些规则由一个名为 <a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.ecma-international.org%2F" target="_blank" rel="nofollow noopener noreferrer" title="https://www.ecma-international.org/" ref="nofollow noopener noreferrer">Ecma International</a> 的组织定义标准，它们共同构成了语言规范文件（你可以在这里找到<a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.ecma-international.org%2Fpublications%2Fstandards%2FEcma-262.htm" target="_blank" rel="nofollow noopener noreferrer" title="https://www.ecma-international.org/publications/standards/Ecma-262.htm" ref="nofollow noopener noreferrer">最新版本</a>）。</p>
<p>因此，当引擎将 JavaScript 代码转换为机器代码时，它需要考虑这些规范。</p>
<p>如果代码中包含一个非法的赋值，或者它试图访问一个变量，而根据语言的规范，这个变量不应该从代码的特定部分被访问，怎么办？</p>
<p>每次函数被调用时，它都需要弄清所有这些事情。它通过创建一个被称为 "执行上下文 "的包装来实现这一目的。</p>
<p>为了更具体一些，避免将来出现混淆，我将把这个称为函数执行上下文，因为每次调用函数都会创建一个。不要被这个术语所吓倒，暂时不要想太多，后面会详细说明。</p>
<p>只要记住，它决定了一些事情，比如。"在那个特定的函数中，哪些变量是可以访问的，在它里面这个值是什么，哪些变量和函数在它里面被声明？"</p>
<h2 data-id="heading-2">全局执行上下文</h2>
<p>但是，并不是所有的 JavaScript 代码都在一个函数里面（尽管大部分代码都在里面）。</p>
<p>在任何函数之外，在全局层面上也可能有代码，因此，JavaScript 引擎首先要做的一件事就是创建一个全局执行上下文。</p>
<p>这就像一个函数执行上下文，在全局层面上起到同样的作用，但它有一些特殊性。</p>
<p>比如，有且只有一个全局执行上下文，在执行开始时创建，所有的 JavaScript 代码都在其中运行。</p>
<p>全局执行上下文创建了两个东西，这两个东西对它来说是特定的，即使没有代码要执行。</p>
<ul>
<li>
<p>一个全局对象。当 JavaScript 在浏览器内运行时，这个对象是窗口对象。当它在浏览器外运行时，就像在 Node.js 中那样，它将是类似 <code>global</code> 的对象。不过为了简单起见，我将在本文中使用 <code>window</code>。</p>
</li>
<li>
<p>一个特殊的变量 <code>this</code></p>
</li>
</ul>
<p>在全局执行上下文中，也只有 <code>this</code>，这实际上等于全局对象 <code>window</code>。它基本上是一个对 <code>window</code> 的引用。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-built_in">this</span> === <span class="hljs-built_in">window</span> <span class="hljs-comment">// logs true</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>全局执行上下文和函数执行上下文之间的另一个微妙区别是，任何在全局层面上声明的变量或函数（在任何函数之外），都会自动作为属性附加到窗口对象上，并隐含在特殊变量 <code>this</code> 上。</p>
<p>尽管函数也有特殊变量 <code>this</code>，但在函数执行环境中不会发生这种情况。</p>
<pre><code class="hljs language-js copyable" lang="js">foo; <span class="hljs-comment">// 'bar'</span>
<span class="hljs-built_in">window</span>.foo; <span class="hljs-comment">// 'bar'</span>
<span class="hljs-built_in">this</span>.foo; <span class="hljs-comment">// 'bar'</span>
(<span class="hljs-built_in">window</span>.foo === foo && <span class="hljs-built_in">this</span>.foo === foo && <span class="hljs-built_in">window</span>.foo === <span class="hljs-built_in">this</span>.foo) <span class="hljs-comment">// true</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>所有的 JavaScript 内置变量和函数都附着在全局窗口对象上： <code>setTimeout()</code>, <code>localStorage</code>, <code>scrollTo()</code>, <code>Math</code>, <code>fetch()</code>，等等。这就是为什么它们可以在代码的任何地方被访问。</p>
<h2 data-id="heading-3">执行栈</h2>
<p>我们知道，每次函数被调用时都会创建一个函数执行上下文。</p>
<p>由于即使是最简单的 JavaScript 程序也有相当多的函数调用，所有这些函数执行上下文都需要以某种方式进行管理。</p>
<p>请看下面的例子:</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">a</span>(<span class="hljs-params"></span>) </span>&#123;
  <span class="hljs-comment">// some code</span>
&#125;

<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">b</span>(<span class="hljs-params"></span>) </span>&#123;
  <span class="hljs-comment">// some code</span>
&#125;

a();
b();
<span class="copy-code-btn">复制代码</span></code></pre>
<p>当遇到函数 <code>a()</code> 的调用时，如上所述创建一个函数执行上下文，并执行该函数内的代码。</p>
<p>当代码的执行完成后<code>（</code>返回语句或到达函数的包围<code>&#125;</code>，函数 <code>a()</code> 的函数执行上下文被销毁。</p>
<p>然后，会遇到 <code>b()</code> 的调用，对函数 <code>b()</code> 重复同样的过程。</p>
<p>但这种情况很少发生，即使在非常简单的 JavaScript 程序中。大多数情况下，会有一些函数在其他函数中被调用:</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">a</span>(<span class="hljs-params"></span>) </span>&#123;
  <span class="hljs-comment">// some code</span>
  b();
  <span class="hljs-comment">// some more code</span>
&#125;

<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">b</span>(<span class="hljs-params"></span>) </span>&#123;
  <span class="hljs-comment">// some code</span>
&#125;

a();
<span class="copy-code-btn">复制代码</span></code></pre>
<p>在这种情况下，<code>a()</code> 的函数执行上下文被创建，但就在 <code>a()</code> 的执行过程中，遇到了 <code>b()</code> 的调用。</p>
<p>为 <code>b()</code> 创建了一个全新的函数执行上下文，但是没有破坏 <code>a()</code> 的执行上下文，因为它的代码还没有完全执行。</p>
<p>这意味着在同一时间有许多函数执行上下文。然而，在任何时候，它们中只有一个在实际运行。</p>
<p>为了跟踪当前正在运行的函数，我们使用了一个堆栈，其中当前正在运行的函数执行上下文位于栈的顶部。</p>
<p>一旦它执行完毕，它将被从堆栈中弹出，下一个执行上下文的执行将继续，以此类推，直到执行堆栈为空。</p>
<p>这个栈被称为执行栈，如下图所示:</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/9392a32893e14f1ea9cfacde67cc0e5d~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>当执行堆栈为空时，我们之前讨论过的、从未被销毁的全局执行上下文就成为当前运行的执行上下文。</p>
<h2 data-id="heading-4">事件队列</h2>
<p>还记得我说过，JavaScript 引擎只是浏览器的一个组件，与渲染引擎或网络层并列。</p>
<p>这些组件都有内置的 Hooks，引擎用这些 Hooks 来通信，以启动网络请求，在屏幕上绘制像素，或者监听鼠标点击。</p>
<p>当你在 JavaScript 中使用类似 fetch 的东西来做一个 HTTP 请求时，引擎实际上会将其传达给网络层。每当请求的响应到来时，网络层将把它传回给 JavaScript 引擎。</p>
<p>但这可能需要几秒钟的时间，当请求正在进行时，JavaScript 引擎会做什么？</p>
<p>简单地停止执行任何代码，直到响应到来？继续执行剩下的代码，每当响应到来时，就停止一切并执行其回调？当回调完成后，继续执行它离开的地方？</p>
<p>以上都不是，尽管第一个可以通过使用 await 来实现。</p>
<p>在多线程语言中，这可以通过一个线程在当前运行的执行环境中执行代码，另一个线程执行事件的回调来处理。但这在 JavaScript 中是不可能的，因为它是单线程的。</p>
<p>为了理解这实际上是如何工作的，让我们考虑一下我们之前看过的 <code>a()</code> 和 <code>b()</code> 函数，但是增加一个点击处理程序和一个 HTTP 请求处理程序。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">a</span>(<span class="hljs-params"></span>) </span>&#123;
  <span class="hljs-comment">// some code</span>
  b();
  <span class="hljs-comment">// some more code</span>
&#125;

<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">b</span>(<span class="hljs-params"></span>) </span>&#123;
  <span class="hljs-comment">// some code</span>
&#125;

<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">httpHandler</span>(<span class="hljs-params"></span>) </span>&#123;
  <span class="hljs-comment">// some code here</span>
&#125;

<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">clickHandler</span>(<span class="hljs-params"></span>) </span>&#123;
  <span class="hljs-comment">// some more code here</span>
&#125;

a();
<span class="copy-code-btn">复制代码</span></code></pre>
<p>JavaScript 引擎从浏览器的其他组件收到的任何事件，如鼠标点击或网络响应，都不会被立即处理。</p>
<p>在这一点上，JavaScript 引擎可能正忙于执行代码，所以它将把事件放在一个队列中，称为事件队列。</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/e4cd6cf9cd0e4a68816085c3301b108d~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>我们已经谈过了执行栈，以及一旦相应函数中的代码执行完毕，当前运行的函数执行上下文是如何从堆栈中弹出的。</p>
<p>然后，下一个执行上下文恢复执行，直到它完成，以此类推，直到堆栈为空，全局执行上下文成为当前运行的执行上下文。</p>
<p>当执行栈中有代码要执行时，事件队列中的事件被忽略，因为引擎正忙于执行栈中的代码。</p>
<p>只有当它完成了，并且执行栈是空的，JavaScript 引擎才会处理事件队列中的下一个事件（当然，如果有的话），并且会调用它的处理程序。</p>
<p>由于这个处理程序是一个 JavaScrip t函数，它的处理就像 <code>a()</code> 和 <code>b()</code> 的处理一样，也就是说，一个函数的执行上下文被创建并推到执行栈中。</p>
<p>如果该处理程序反过来调用另一个函数，那么另一个函数的执行上下文就会被创建并推到堆栈的顶部，以此类推。
只有当执行栈再次为空时，JavaScript 引擎才会再次检查事件队列中的新事件。</p>
<p>这同样适用于键盘和鼠标事件。当鼠标被点击时，JavaScript 引擎会得到一个点击事件，把它放在事件队列中，只有当执行栈为空时才会执行它的处理程序。</p>
<p>你可以通过把下面的代码复制到你的浏览器控制台，轻松地看到这个过程：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">documentClickHandler</span>(<span class="hljs-params"></span>) </span>&#123;
  <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'CLICK!!!'</span>);
&#125;

<span class="hljs-built_in">document</span>.addEventListener(<span class="hljs-string">'click'</span>, documentClickHandler);

<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">a</span>(<span class="hljs-params"></span>) </span>&#123;
  <span class="hljs-keyword">const</span> fiveSecondsLater = <span class="hljs-keyword">new</span> <span class="hljs-built_in">Date</span>().getTime() + <span class="hljs-number">5000</span>;
  <span class="hljs-keyword">while</span> (<span class="hljs-keyword">new</span> <span class="hljs-built_in">Date</span>().getTime() < fiveSecondsLater) &#123;&#125;
&#125;

a();
<span class="copy-code-btn">复制代码</span></code></pre>
<p><code>while</code> 循环只是让引擎忙碌五秒钟，不用太担心。在这五秒钟内开始点击文档上的任何地方，你会看到没有任何东西被记录到控制台。</p>
<p>当五秒钟过去，执行栈为空时，第一次点击的处理程序被调用。</p>
<p>由于这是一个函数，一个函数执行上下文被创建，推送到堆栈，执行，并从堆栈中弹出。然后，第二次点击的处理程序被调用，以此类推。</p>
<p>实际上，<code>setTimeout()</code>（和 <code>setInterval()</code> ）的情况也是如此。你提供给 <code>setTimeout()</code> 的处理程序实际上被放在事件队列中。</p>
<p>这意味着，如果你将超时设置为 0，但执行堆栈上还有代码要执行，那么 <code>setTimeout()</code> 的处理程序只有在堆栈为空时才会被调用，这可能是许多毫秒之后。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-built_in">setTimeout</span>(<span class="hljs-function">() =></span> &#123;
  <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'TIMEOUT HANDLER!!!'</span>);
&#125;, <span class="hljs-number">0</span>);

<span class="hljs-keyword">const</span> fiveSecondsLater = <span class="hljs-keyword">new</span> <span class="hljs-built_in">Date</span>().getTime() + <span class="hljs-number">5000</span>;
<span class="hljs-keyword">while</span> (<span class="hljs-keyword">new</span> <span class="hljs-built_in">Date</span>().getTime() < fiveSecondsLater) &#123;&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>注意：被放入事件队列的代码被称为异步的。这是否是一个好的术语是另一个话题，但人们就是这样称呼它的，所以我想你必须习惯于它。</p>
<h2 data-id="heading-5">函数执行上下文步骤</h2>
<p>现在我们已经熟悉了JavaScript程序的执行周期，让我们再深入了解一下函数执行上下文到底是如何创建的。</p>
<p>它发生在两个步骤中：创建步骤和执行步骤。</p>
<p>创建步骤 "设置了一些东西"，以便代码可以被执行，而执行步骤实际上是执行它。</p>
<p>在创建步骤中发生的两件事非常重要：</p>
<ul>
<li>确定 <code>scope</code>.</li>
<li>确定值。（我将假设你已经熟悉 JavaScript 中的 <code>this</code> 关键字）。</li>
</ul>
<p>在接下来的两个相应章节中，将分别详细介绍这些内容。</p></div>  
</div>
            