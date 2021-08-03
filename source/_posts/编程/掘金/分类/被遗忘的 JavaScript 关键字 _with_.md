
---
title: '被遗忘的 JavaScript 关键字 _with_'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=3979'
author: 掘金
comments: false
date: Sat, 31 Jul 2021 02:50:56 GMT
thumbnail: 'https://picsum.photos/400/300?random=3979'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><blockquote>
<p>本文为翻译</p>
<p>原文标题：JavaScript's Forgotten Keyword (with)</p>
<p>原文作者：Randall</p>
<p>原文地址：<a href="https://link.juejin.cn/?target=https%3A%2F%2Fdev.to%2Fmistval%2Fjavascript-s-forgotten-keyword-with-48id" target="_blank" rel="nofollow noopener noreferrer" title="https://dev.to/mistval/javascript-s-forgotten-keyword-with-48id" ref="nofollow noopener noreferrer">dev.to/mistval/jav…</a></p>
</blockquote>
<p>JavaScript 开发 可真是一份令人兴奋的工作。几乎每天你都能发现一些神秘又另类的东西。有时是惊喜，有时是惊吓。</p>
<p>在本文中，我会介绍 <a href="https://link.juejin.cn/?target=https%3A%2F%2Fdeveloper.mozilla.org%2Fzh-CN%2Fdocs%2FWeb%2FJavaScript%2FReference%2FStatements%2Fwith" target="_blank" rel="nofollow noopener noreferrer" title="https://developer.mozilla.org/zh-CN/docs/Web/JavaScript/Reference/Statements/with" ref="nofollow noopener noreferrer">“with”关键字</a>。它是 JavaScript 语言中的一个阴暗的角落，即便是那些资深开发者很少能注意到。</p>
<h2 data-id="heading-0">用法</h2>
<p>我们可以使用 <strong>with</strong> 关键字帮助我们打印一条消息到 console：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">with</span> (<span class="hljs-built_in">console</span>) &#123;
  log(<span class="hljs-string">'I dont need the "console." part anymore!'</span>);
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>我们还可以用它来将数组合并成字符串：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">with</span> (<span class="hljs-built_in">console</span>) &#123;
  <span class="hljs-keyword">with</span> ([<span class="hljs-string">'a'</span>, <span class="hljs-string">'b'</span>, <span class="hljs-string">'c'</span>]) &#123;
    log(join(<span class="hljs-string">''</span>)); <span class="hljs-comment">// writes "abc" to the console.</span>
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>是的，我的朋友，信不信由你，这就是 JavaScript。</p>
<h2 data-id="heading-1">"with" 做了什么？</h2>
<p>以下是 <a href="https://link.juejin.cn/?target=https%3A%2F%2Fdeveloper.mozilla.org%2Fzh-CN%2Fdocs%2FWeb%2FJavaScript%2FReference%2FStatements%2Fwith" target="_blank" rel="nofollow noopener noreferrer" title="https://developer.mozilla.org/zh-CN/docs/Web/JavaScript/Reference/Statements/with" ref="nofollow noopener noreferrer">来自 MDN 的解释</a>：</p>
<blockquote>
<p>JavaScript 查找某个未使用命名空间的变量时，会通过作用域链来查找，作用域链是跟执行代码的 context 或者包含这个变量的函数有关。“with” 语句将某个对象添加到作用域链的顶部，如果在 statement 中有某个未使用命名空间的变量，跟作用域链中的某个属性同名，则这个变量将指向这个属性值。如果沒有同名的属性，则将拋出 ReferenceError 异常。</p>
</blockquote>
<p>简单来说就是：当你在代码中写一个标识符的时候（就像前文中代码段里的 <code>log</code> 或者 <code>join</code> ），JavaScript 会查找 作用域链 上的对象，如果其中有对象的属性名 和 你在代码中写的这个标识符 一致，JavaScript 就会使用该对象的属性值。</p>
<p><code>with</code> 关键字允许你注入任何对象到 作用域链 顶部。这里我列了一个例子，应该能更清晰的解释这一点：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">with</span> (&#123; <span class="hljs-attr">myProperty</span>: <span class="hljs-string">'Hello world!'</span> &#125;) &#123;
  <span class="hljs-built_in">console</span>.log(myProperty); <span class="hljs-comment">// Logs "Hello world!"</span>
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-2">别用它</h2>
<p>看起来 “with” 棒极了，对吧？嗯，也许不是。</p>
<p>在大多数情况下，使用临时变量就能达到同样的效果，而且自从 <a href="https://link.juejin.cn/?target=https%3A%2F%2Fdeveloper.mozilla.org%2Fzh-CN%2Fdocs%2FWeb%2FJavaScript%2FReference%2FOperators%2FDestructuring_assignment" target="_blank" rel="nofollow noopener noreferrer" title="https://developer.mozilla.org/zh-CN/docs/Web/JavaScript/Reference/Operators/Destructuring_assignment" ref="nofollow noopener noreferrer">结构赋值</a> 出现后，这么做越来越方便了。</p>
<p>此外，MDN 列出了一些陷阱：</p>
<h3 data-id="heading-3">在严格模式下被禁用</h3>
<p>你不能在严格模式下使用 with 。考虑到 ES module 和 class 会自动启用严格模式，这种限制几乎消灭了任何 with 在现代开发中使用的可能性。</p>
<h3 data-id="heading-4">意外的变量遮蔽（Variable shadowing）</h3>
<p>思考下面的代码，我们将两个数求平均，然后将结果四舍五入：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">getAverage</span>(<span class="hljs-params">min, max</span>) </span>&#123;
  <span class="hljs-keyword">with</span> (<span class="hljs-built_in">Math</span>) &#123;
    <span class="hljs-keyword">return</span> round((min + max) / <span class="hljs-number">2</span>);
  &#125;
&#125;

getAverage(<span class="hljs-number">1</span>, <span class="hljs-number">5</span>);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>最终返回是 <code>NaN</code> 。为什么？因为 <code>Math.min()</code> 和 <code>Math.max()</code> <strong>遮蔽</strong>  了函数接收的参数，所以我们最终是在将两个函数相加，当然就是 <code>NaN</code> 了。</p>
<p>基本上，你如果用了 <code>with</code> , 你就不得不小心翼翼的选择标识符的命名了。你必须检查你往 <code>with</code> 里传了什么东西，确认其中的属性不会导致 高层作用域的 <strong>变量遮蔽</strong> 。</p>
<p>使用 <code>with</code> 还可能引发安全漏洞。如果 传入 <code>with</code> 的对象 被 攻击者添加一些属性，那么就可能会遮蔽你的标识符，并会通过各种你意想不到的方式影响你程序的行为。</p>
<p>例如，从一个未经过验证的  JSON HTTP 请求体 中解析得到 JS对象 后，直接传给 <code>with</code>，这么做是极其危险的行为。</p>
<h3 data-id="heading-5">性能</h3>
<p>把东西添加到 作用域链，你会降低代码的运行速度，因为你增加了 在解析标识符到实际值时 所需要搜索的对象数量。</p>
<h3 data-id="heading-6">被排斥</h3>
<p>如果你用 <code>with</code> 关键字，所有人都会认为你疯了，然后在吃午饭的时候远离你。也有可能，他们会用滑稽的表情看着你。</p>
<p>无论如何，使用这种没人知道的神奇语言特性只会让你的代码更难维护，而且其实它也没给你带来多少好处。</p>
<h2 data-id="heading-7">结论</h2>
<p><code>with</code> 关键字为 JavaScript 增添了一些有趣的能力，但是到头来 弊大于利，我个人不推荐使用。</p>
<p>当然，不要只听我的一家之言。似乎 <a href="https://link.juejin.cn/?target=https%3A%2F%2Fdeveloper.mozilla.org%2Fzh-CN%2Fdocs%2FWeb%2FJavaScript%2FReference%2FStatements%2Fwith" target="_blank" rel="nofollow noopener noreferrer" title="https://developer.mozilla.org/zh-CN/docs/Web/JavaScript/Reference/Statements/with" ref="nofollow noopener noreferrer">MDN</a> 也对 <code>with</code> 恨之入骨，在严格模式中禁用它是有原因的。</p>
<p>我写 JavaScript 超过 5 年了，令我惊讶的是，直到今天我还在学习语言的关键字，这些关键字甚至都不是最近才出现的。到底还有什么知识点在潜藏着呢？</p>
<p><code>with</code> 源于什么？谁设计的？为什么？是想实现类似于 C++ 命名空间的东西吗？是 通灵板 告诉他们怎么做的吗？</p>
<p>不管是什么情况，看起来被长期遗忘的 <code>with</code> 要被永远的扔进历史的垃圾箱了。</p>
<p>就像黑魔法一样，有趣 又 混乱！</p></div>  
</div>
            