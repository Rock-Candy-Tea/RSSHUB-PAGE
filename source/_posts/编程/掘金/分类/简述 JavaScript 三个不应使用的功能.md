
---
title: '简述 JavaScript 三个不应使用的功能'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://cdn-images-1.medium.com/max/3840/1*kSqZcIr9JLkFQgqwe4LEOQ.jpeg'
author: 掘金
comments: false
date: Thu, 22 Jul 2021 03:38:45 GMT
thumbnail: 'https://cdn-images-1.medium.com/max/3840/1*kSqZcIr9JLkFQgqwe4LEOQ.jpeg'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;color:#595959;font-size:15px;font-family:-apple-system,system-ui,BlinkMacSystemFont,Helvetica Neue,PingFang SC,Hiragino Sans GB,Microsoft YaHei,Arial,sans-serif;background-image:linear-gradient(90deg,rgba(60,10,30,.04) 3%,transparent 0),linear-gradient(1turn,rgba(60,10,30,.04) 3%,transparent 0);background-size:20px 20px;background-position:50%&#125;.markdown-body p&#123;color:#595959;font-size:15px;line-height:2;font-weight:400&#125;.markdown-body p+p&#123;margin-top:16px&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;padding:30px 0;margin:0;color:#135ce0&#125;.markdown-body h1&#123;position:relative;text-align:center;font-size:22px;margin:50px 0&#125;.markdown-body h1:before&#123;position:absolute;content:"";top:-10px;left:50%;width:32px;height:32px;transform:translateX(-50%);background-size:100% 100%;opacity:.36;background-repeat:no-repeat;background:url(data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACAAAAAgCAMAAABEpIrGAAAABGdBTUEAALGPC/xhBQAAACBjSFJNAAB6JgAAgIQAAPoAAACA6AAAdTAAAOpgAAA6mAAAF3CculE8AAABfVBMVEX///8Ad/8AgP8AgP8AgP8Aff8AgP8Af/8AgP8AVf8Af/8Af/8AgP8AgP8Af/8Afv8AAP8Afv8Afv8Aef8AgP8AdP8Afv8AgP8AgP8Acf8Ae/8AgP8Af/8AgP8Af/8Af/8AfP8Afv8AgP8Af/8Af/8Afv8Afv8AgP8Afv8AgP8Af/8Af/8AgP8AgP8Afv8AgP8Af/8AgP8AgP8AgP8Ae/8Afv8Af/8AgP8Af/8AgP8Af/8Af/8Aff8Af/8Abf8AgP8Af/8AgP8Af/8Af/8Afv8AgP8AgP8Afv8Afv8AgP8Af/8Aff8AgP8Afv8AgP8Aff8AgP8AfP8AgP8Ae/8AgP8Af/8AgP8AgP8AgP8Afv8AgP8AgP8AgP8Afv8AgP8AgP8AgP8AgP8AgP8Af/8AgP8Af/8Af/8Aev8Af/8AgP8Aff8Afv8AgP8AgP8AgP8Af/8AgP8Af/8Af/8AgP8Afv8AgP8AgP8AgP8AgP8Af/8AeP8Af/8Af/8Af//////rzEHnAAAAfXRSTlMAD7CCAivatxIDx5EMrP19AXdLEwgLR+6iCR/M0yLRzyFF7JupSXn8cw6v60Q0QeqzKtgeG237HMne850/6Qeq7QaZ+WdydHtj+OM3qENCMRYl1B3K2U7wnlWE/mhlirjkODa9FN/BF7/iNV/2kASNZpX1Wlf03C4stRGxgUPclqoAAAABYktHRACIBR1IAAAACXBIWXMAAAsTAAALEwEAmpwYAAAAB3RJTUUH4gEaBzgZ4yeM3AAAAT9JREFUOMvNUldbwkAQvCAqsSBoABE7asSOBRUVVBQNNuy9996789+9cMFAMHnVebmdm+/bmdtbQv4dOFOW2UjPzgFyLfo6nweKfIMOBYWwFtmMPGz2Yj2pJI0JDq3udJW6VVbmKa9I192VQFV1ktXUAl5NB0cd4KpnORqsEO2ZIRpF9gJfE9Dckqq0KuZt7UAH5+8EPF3spjsRpCeQNO/tA/qDwIDA+OCQbBoKA8NOdjMySgcZGVM6jwcgRuUiSs0nlPFNSrEpJfU0jTLD6llqbvKxei7OzvkFNQohi0vAsj81+MoqsCaoPOQFgus/1LyxichW+hS2JWCHZ7VlF9jb187pIAYcHiViHAMnp5mTjJ8B5xeEXF4B1ze/fTh/C0h398DDI9HB07O8ci+vRBdvdGnfP4gBuM8vw7X/G3wDmFhFZEdxzjMAAAAldEVYdGRhdGU6Y3JlYXRlADIwMTgtMDEtMjZUMDc6NTY6MjUrMDE6MDA67pVWAAAAJXRFWHRkYXRlOm1vZGlmeQAyMDE4LTAxLTI2VDA3OjU2OjI1KzAxOjAwS7Mt6gAAABl0RVh0U29mdHdhcmUAd3d3Lmlua3NjYXBlLm9yZ5vuPBoAAAAWdEVYdFRpdGxlAGp1ZWppbl9sb2dvIGNvcHlxapmKAAAAV3pUWHRSYXcgcHJvZmlsZSB0eXBlIGlwdGMAAHic4/IMCHFWKCjKT8vMSeVSAAMjCy5jCxMjE0uTFAMTIESANMNkAyOzVCDL2NTIxMzEHMQHy4BIoEouAOoXEXTyQjWVAAAAAElFTkSuQmCC)&#125;.markdown-body h2&#123;position:relative;font-size:20px;border-left:4px solid;padding:0 0 0 10px;margin:30px 0&#125;.markdown-body h3&#123;font-size:16px&#125;.markdown-body ul&#123;list-style:disc outside;margin-left:2em;margin-top:1em&#125;.markdown-body li&#123;line-height:2;color:#595959&#125;.markdown-body img.loaded&#123;margin:0 auto;display:block&#125;.markdown-body blockquote&#123;background:#fff9f9;margin:2em 0;padding:2px 20px;border-left:4px solid #b2aec5&#125;.markdown-body blockquote p&#123;color:#666;line-height:2&#125;.markdown-body a&#123;color:#036aca;border-bottom:1px solid rgba(3,106,202,.8);font-weight:400;text-decoration:none&#125;.markdown-body em strong,.markdown-body strong&#123;color:#036aca&#125;.markdown-body hr&#123;border-top:1px solid #135ce0&#125;.markdown-body pre&#123;overflow:auto&#125;.markdown-body code,.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body table&#123;border-collapse:collapse;margin:1rem 0;overflow-x:auto&#125;.markdown-body table td,.markdown-body table th&#123;border:1px solid #dfe2e5;padding:.6em 1em&#125;.markdown-body table tr&#123;border-top:1px solid #dfe2e5&#125;.markdown-body table tr:nth-child(2n)&#123;background-color:#f6f8fa&#125;</style><blockquote>
<ul>
<li>原文地址：<a href="https://link.juejin.cn/?target=https%3A%2F%2Fblog.bitsrc.io%2Fthe-dark-side-of-javascript-a-look-at-3-features-you-never-want-to-use-83b6f0b3804b" target="_blank" rel="nofollow noopener noreferrer" title="https://blog.bitsrc.io/the-dark-side-of-javascript-a-look-at-3-features-you-never-want-to-use-83b6f0b3804b" ref="nofollow noopener noreferrer">The Dark Side of Javascript: A Look at 3 Features You Never Want to Use</a></li>
<li>原文作者：<a href="https://link.juejin.cn/?target=https%3A%2F%2Fmedium.com%2F%40deleteman123" target="_blank" rel="nofollow noopener noreferrer" title="https://medium.com/@deleteman123" ref="nofollow noopener noreferrer">Fernando Doglio</a></li>
<li>译文出自：<a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fxitu%2Fgold-miner" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/xitu/gold-miner" ref="nofollow noopener noreferrer">掘金翻译计划</a></li>
<li>本文永久链接：<a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fxitu%2Fgold-miner%2Fblob%2Fmaster%2Farticle%2F2021%2Fthe-dark-side-of-javascript-a-look-at-3-features-you-never-want-to-use.md" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/xitu/gold-miner/blob/master/article/2021/the-dark-side-of-javascript-a-look-at-3-features-you-never-want-to-use.md" ref="nofollow noopener noreferrer">github.com/xitu/gold-m…</a></li>
<li>译者：<a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fzenblofe" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/zenblofe" ref="nofollow noopener noreferrer">Z招锦</a></li>
<li>校对者：<a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2FCarlosChenN" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/CarlosChenN" ref="nofollow noopener noreferrer">CarlosChen</a>、<a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Ffinalwhy" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/finalwhy" ref="nofollow noopener noreferrer">finalwhy</a></li>
</ul>
</blockquote>
<h1 data-id="heading-0">简述 JavaScript 三个不应使用的功能</h1>
<p><img src="https://cdn-images-1.medium.com/max/3840/1*kSqZcIr9JLkFQgqwe4LEOQ.jpeg" alt="Image by Free-Photos from Pixabay" loading="lazy" referrerpolicy="no-referrer"></p>
<p>JavaScript 已经存在了相当长的一段时间（大约 26 年），在这段时间里，该语言已经有了很大的发展。</p>
<p>这种演变大多是有目的，特别是在最新的迭代中，开发者社区已经设法影响了其中的一些变化，使 JavaScript 成为一种非常灵活和好用的语言。</p>
<p>然而，在这些年的演变过程中，可以说仍有一些残余的过时功能，这些功能还没有被拿掉，但确实没有任何用途（或者更确切地说，在原本的用途方面效率不高）。</p>
<p>以下三个 JavaScript 特性，即使它们在运行时仍然可用，但你应避免去使用它们。</p>
<h2 data-id="heading-1">void 操作符</h2>
<p>你可能在某一时刻看到过 void 操作符的存在。在过去，每当你点击一个链接，而这个链接将触发一个 JavaScript 函数时，你会添加 <code>href="javascript:void(0)"</code> 以确保默认行为（即页面跳转）不会触发。</p>
<p>但这究竟是什么意思呢？</p>
<p><code>void</code> 操作符是一种在 JavaScript 中生成 <code>undefined</code> 值的方法。没错，它能接受任何表达式，并且每次都返回 <code>undefined</code>。</p>
<p>我知道你在想什么：为什么不直接使用已经存在的 <code>undefined</code> 关键字呢？嗯，正如你看到的，在 ECMAScript 5 之前，<code>undefined</code> 关键字并不是一个常量值。是的，你可以定义 <code>undefined</code>，如果你再想一想，这不就是我们曾经想做的事情吗？</p>
<p>当然，这样做是没有意义的，这就是为什么最终它被重新定义为一个常量值，且不可更改。然而，因为早前你是可以改变它的，所以 <code>void</code> 会允许你访问 <code>undefined</code>，即使这个常量不再起作用。</p>
<p>事实上，一个很好的方法是通过创建你自己的 IIFEs 来重新定义只属于你的命名空间的常量，避免与第三方库的任何问题，其中一个参数确实是 <code>undefined</code>，像这样：</p>
<pre><code class="hljs language-JavaScript copyable" lang="JavaScript">(<span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params"><span class="hljs-built_in">window</span>, <span class="hljs-literal">undefined</span></span>) </span>&#123;
  <span class="hljs-comment">// 你这里的逻辑，可以把 undefined 当作预期</span>
&#125;)(<span class="hljs-built_in">window</span>, <span class="hljs-keyword">void</span>(<span class="hljs-number">0</span>))
<span class="copy-code-btn">复制代码</span></code></pre>
<p>当然，今天的 <code>void</code> 操作符仍然有它的用途，但它是非必要的。例如，在现在的 JavaScript 中，最好的用例是帮助避免单行箭头函数的非预期返回。</p>
<p>你可能知道，一个单行箭头函数将返回该行的结果，即使你没有显式使用 <code>return</code> 语句。</p>
<pre><code class="hljs language-JavaScript copyable" lang="JavaScript"><span class="hljs-keyword">const</span> double = <span class="hljs-function"><span class="hljs-params">x</span> =></span> x * <span class="hljs-number">2</span>; <span class="hljs-comment">// 返回 X 乘以 2 的结果</span>

<span class="hljs-keyword">const</span> callAfunction = <span class="hljs-function">() =></span> myFunction(); <span class="hljs-comment">// 返回 myFunction 所返回的结果，即使我不想这样做</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这两个函数都会返回一些东西。显然，对于 <code>double</code> 函数来说，你希望它返回一个值，但另一个可能不是，你可能只是想用它调用另一个函数（即 <code>myFunction()</code>），但你对其结果值不感兴趣。因此你可以这样做：</p>
<pre><code class="hljs language-JavaScript copyable" lang="JavaScript"><span class="hljs-keyword">const</span> callAfunction = <span class="hljs-function">() =></span> <span class="hljs-keyword">void</span> myFunction(); <span class="hljs-comment">// 返回 myFunction 所返回的结果，即使我不想这样做</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>而这将立即覆盖返回值，并确保你的调用只返回 <code>undefined</code>。</p>
<p>对我来说，这种行为提供了一个最小的好处，使 <code>void</code> 在这个时代的 JavaScript 中毫无用处。</p>
<p>我建议你避免使用它，让它保持一个废弃的状态。</p>
<h2 data-id="heading-2">With 语句</h2>
<p>这个是 JavaScript 自带的结构之一，但你可能从未听说过它，因为它并没有被真正推广。事实上，即使是 MDN 官方文档也不鼓励你使用它，因为它可能导致非常混乱的代码。</p>
<p><code>with</code> 语句允许扩展给定语句的作用域链。换句话说，它允许你将一个表达式注入到给定语句的作用域，理想情况下，可以简化所述语句。</p>
<p>下面是一个示例，这样你就会明白我想说什么：</p>
<pre><code class="hljs language-JavaScript copyable" lang="JavaScript"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">greet</span>(<span class="hljs-params">user</span>) </span>&#123;
  
  <span class="hljs-function"><span class="hljs-title">with</span>(<span class="hljs-params">user</span>)</span> &#123;
    <span class="hljs-built_in">console</span>.log(<span class="hljs-string">`Hello there <span class="hljs-subst">$&#123;name&#125;</span>, how are you and your <span class="hljs-subst">$&#123;kids.length&#125;</span> kids today?`</span>)
  &#125;
&#125;

greet(&#123;
  <span class="hljs-attr">name</span>: <span class="hljs-string">"Fernando"</span>,
  <span class="hljs-attr">kids</span>: [<span class="hljs-string">"Brian"</span>, <span class="hljs-string">"Andrew"</span>]
&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>注意 <code>greet</code> 函数中 <code>with</code> 语句的魔力。这是一个基本的示例，表明了表达式的 <code>happy path</code>。但是，让我们看另一个情况，事情变得有点复杂：</p>
<pre><code class="hljs language-JavaScript copyable" lang="JavaScript"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">greet</span>(<span class="hljs-params">user, message</span>) </span>&#123;
  <span class="hljs-function"><span class="hljs-title">with</span>(<span class="hljs-params">user</span>)</span> &#123;
    <span class="hljs-built_in">console</span>.log(<span class="hljs-string">`Hey <span class="hljs-subst">$&#123;name&#125;</span>, here is a message for you: <span class="hljs-subst">$&#123;message&#125;</span>`</span>)
  &#125;
&#125;

<span class="hljs-comment">// happy path</span>
greet(&#123;
  <span class="hljs-attr">name</span>: <span class="hljs-string">"Fernando"</span>
&#125;, <span class="hljs-string">"You got 2 emails"</span>)

<span class="hljs-comment">// kinda sad path</span>
greet(&#123;
  <span class="hljs-attr">name</span>: <span class="hljs-string">"Fernando"</span>,
  <span class="hljs-attr">message</span>: <span class="hljs-string">"Unrelated message"</span>
&#125;, <span class="hljs-string">"you got email"</span>)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>你认为这种执行方式的输出结果会是什么？</p>
<pre><code class="copyable">Hey Fernando, here is a message for you: You got 2 emails
Hey Fernando, here is a message for you: Unrelated message
<span class="copy-code-btn">复制代码</span></code></pre>
<p>由于你在传入的对象中添加了一个同名属性，你无意间覆盖了函数的第二个参数。我想补充的是，这完全是正常的，因为人们永远不会期望两者处于同一个作用域级别。然而，多亏了 <code>with</code>，我们把这两个作用域都混在了一起，但结果并不理想。</p>
<p>这都是为了说明要避免使用 <code>with</code>，虽然它可能看起来是节省代码量的好方法，但你的代码很快会变得非常复杂，这会对别人（或两周后的你）去理解你的代码造成心智负担。</p>
<h2 data-id="heading-3">Labels 标签</h2>
<p>如果你学习编程足够早（像我一样），你就经历过其他语言（如 C 语言）中对 <code>go-to</code> 语句的憎恨。那太糟糕了，那是一个在当年很有意义的功能，但最终随着同一问题的更新的解决方案，这种功能变得如此过时和糟糕，以至于变成了一种反模式。</p>
<p>因此 JavaScript 不得不去实现它。</p>
<p><code>Go-to</code> 语句是一种方式，让你在代码的任何地方放置一个标记，然后从其他地方跳到那里。你可以跳到一个函数的中间，或者跳到一个 <code>IF</code> 语句里面，它就像一个神奇的入口，可以跳到你代码中的任何地方。我相信你可以看到这可能是一个问题，它的力量太大，灵活性太强，我们当然会错过使用它的机会。</p>
<p>然而，JavaScript 实现了一个类似的，但不完全相同的结构：<code>labels</code> 标签。</p>
<p>JavaScript 中的标签语句是一个你放在语句前的标记，然后你可以 <code>break</code> 或 <code>continue</code>。请注意，没有更多的 <code>go-to</code>，这是一个很好的优势。</p>
<p>你可以这样写：</p>
<pre><code class="hljs language-JavaScript copyable" lang="JavaScript">label1: &#123;
  <span class="hljs-built_in">console</span>.log(<span class="hljs-number">1</span>)
  <span class="hljs-keyword">let</span> condition = <span class="hljs-literal">true</span>
  <span class="hljs-keyword">if</span>(condition) &#123;
  <span class="hljs-keyword">break</span> label1
  &#125;
  <span class="hljs-built_in">console</span>.log(<span class="hljs-number">2</span>)
&#125;
<span class="hljs-built_in">console</span>.log(<span class="hljs-string">"end"</span>)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>而输出结果将是：</p>
<pre><code class="copyable">1
end
<span class="copy-code-btn">复制代码</span></code></pre>
<p>当然，这个例子看起来非常像一个 <code>if..else</code> 语句。而且你完全可以说，它看起来并不那么糟糕。然而，你打破了代码的正常流程，跳过了语句。如果你就是希望如此，那么使用 <code>if..else</code> 带来的心智负担会小很多。</p>
<p>当我们把标签与循环和 <code>continue</code> 语句的相互作用包括在内时，<code>labels</code> 标签的问题就变得更明显了。</p>
<pre><code class="hljs language-JavaScript copyable" lang="JavaScript"><span class="hljs-keyword">let</span> i, j;

loop1:
<span class="hljs-keyword">for</span>(i = <span class="hljs-number">0</span>; i < <span class="hljs-number">10</span>; i++) &#123;
  <span class="hljs-attr">loop2</span>:
  <span class="hljs-keyword">for</span>(j = <span class="hljs-number">0</span>; j < <span class="hljs-number">10</span>; j++) &#123;

    <span class="hljs-keyword">if</span>(j == <span class="hljs-number">3</span> && i == <span class="hljs-number">2</span>) &#123;
      <span class="hljs-keyword">continue</span> loop2;
    &#125;
    <span class="hljs-built_in">console</span>.log(&#123;i, j&#125;)
    <span class="hljs-keyword">if</span>(j % <span class="hljs-number">2</span> == <span class="hljs-number">0</span>) &#123;
      <span class="hljs-keyword">continue</span> loop1;
    &#125;
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>你能在头脑中运行上述代码并告诉我具体的输出结果吗？这并非不可能，但要花点时间。上面的脚本会打印：</p>
<pre><code class="copyable">&#123; i: 0, j: 0 &#125;
&#123; i: 1, j: 0 &#125;
&#123; i: 2, j: 0 &#125;
&#123; i: 3, j: 0 &#125;
&#123; i: 4, j: 0 &#125;
&#123; i: 5, j: 0 &#125;
&#123; i: 6, j: 0 &#125;
&#123; i: 7, j: 0 &#125;
&#123; i: 8, j: 0 &#125;
&#123; i: 9, j: 0 &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>从本质上讲，第二个 <code>if</code> 在 <code>0</code> 的时候评估为 <code>true</code>，所以 <code>continue</code> 语句影响了外循环，导致它移动到下一个索引值，这反过来又重置了内循环，导致它回到 <code>0</code>，同样的事情不断发生，重复了 <code>10</code> 次。第一个 <code>if</code>，如果你想知道的话，从来没有评估为 <code>true</code>，因为 <code>j</code> 从来没有达到 <code>0</code> 以外的任何值。</p>
<p><code>labels</code> 标签可能是棘手的小家伙，即使你能正确地使用它们，并且从解释器的角度来看，它们也很有意义，但你应该为人类而不是为机器写代码。别人会来读它（甚至是三周后的你），当他们看到标签的那一刻，他们会永远恨你。当然，他们会花更多的时间来理解你代码的基本流程，但这在目前是次要问题。</p>
<h2 data-id="heading-4">本文总结</h2>
<p>请不要误会，我喜欢 JavaScript 这门语言，自从 <code>18</code> 年前我开始从事网络开发工作以来，我一直在以不同的方式与它互动。我见证了这门语言的发展，就像一坛好酒，随着时间的推移而变得更好。然而，如果我说这门语言中没有一些我不喜欢的黑暗角落，那是假的。而这三个功能恰好表明了这一点。</p>
<p>好消息是，在我多年的经验中，我还没有看到 <code>with</code> 或标签（<code>Label</code>）被实施并部署到生产中。这并不是说没有这样的情况，只是我从未见过，这让我觉得没有多少代码审查会让它们通过。</p>
<p>你有没有看到这些功能在现代 JavaScript 中被使用？</p>
<blockquote>
<p>如果发现译文存在错误或其他需要改进的地方，欢迎到 <a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fxitu%2Fgold-miner" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/xitu/gold-miner" ref="nofollow noopener noreferrer">掘金翻译计划</a> 对译文进行修改并 PR，也可获得相应奖励积分。文章开头的 <strong>本文永久链接</strong> 即为本文在 GitHub 上的 MarkDown 链接。</p>
</blockquote>
<hr>
<blockquote>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fxitu%2Fgold-miner" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/xitu/gold-miner" ref="nofollow noopener noreferrer">掘金翻译计划</a> 是一个翻译优质互联网技术文章的社区，文章来源为 <a href="https://juejin.im/" target="_blank" title="https://juejin.im">掘金</a> 上的英文分享文章。内容覆盖 <a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fxitu%2Fgold-miner%23android" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/xitu/gold-miner#android" ref="nofollow noopener noreferrer">Android</a>、<a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fxitu%2Fgold-miner%23ios" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/xitu/gold-miner#ios" ref="nofollow noopener noreferrer">iOS</a>、<a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fxitu%2Fgold-miner%23%25E5%2589%258D%25E7%25AB%25AF" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/xitu/gold-miner#%E5%89%8D%E7%AB%AF" ref="nofollow noopener noreferrer">前端</a>、<a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fxitu%2Fgold-miner%23%25E5%2590%258E%25E7%25AB%25AF" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/xitu/gold-miner#%E5%90%8E%E7%AB%AF" ref="nofollow noopener noreferrer">后端</a>、<a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fxitu%2Fgold-miner%23%25E5%258C%25BA%25E5%259D%2597%25E9%2593%25BE" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/xitu/gold-miner#%E5%8C%BA%E5%9D%97%E9%93%BE" ref="nofollow noopener noreferrer">区块链</a>、<a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fxitu%2Fgold-miner%23%25E4%25BA%25A7%25E5%2593%2581" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/xitu/gold-miner#%E4%BA%A7%E5%93%81" ref="nofollow noopener noreferrer">产品</a>、<a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fxitu%2Fgold-miner%23%25E8%25AE%25BE%25E8%25AE%25A1" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/xitu/gold-miner#%E8%AE%BE%E8%AE%A1" ref="nofollow noopener noreferrer">设计</a>、<a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fxitu%2Fgold-miner%23%25E4%25BA%25BA%25E5%25B7%25A5%25E6%2599%25BA%25E8%2583%25BD" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/xitu/gold-miner#%E4%BA%BA%E5%B7%A5%E6%99%BA%E8%83%BD" ref="nofollow noopener noreferrer">人工智能</a>等领域，想要查看更多优质译文请持续关注 <a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fxitu%2Fgold-miner" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/xitu/gold-miner" ref="nofollow noopener noreferrer">掘金翻译计划</a>、<a href="https://link.juejin.cn/?target=http%3A%2F%2Fweibo.com%2Fjuejinfanyi" target="_blank" rel="nofollow noopener noreferrer" title="http://weibo.com/juejinfanyi" ref="nofollow noopener noreferrer">官方微博</a>、<a href="https://link.juejin.cn/?target=https%3A%2F%2Fzhuanlan.zhihu.com%2Fjuejinfanyi" target="_blank" rel="nofollow noopener noreferrer" title="https://zhuanlan.zhihu.com/juejinfanyi" ref="nofollow noopener noreferrer">知乎专栏</a>。</p>
</blockquote></div>  
</div>
            