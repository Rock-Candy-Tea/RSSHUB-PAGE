
---
title: '回味那些年我们一起用过的JQuery'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/761095a300d34dbbb89c7e610953786a~tplv-k3u1fbpfcp-zoom-1.image'
author: 掘金
comments: false
date: Fri, 23 Jul 2021 20:07:45 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/761095a300d34dbbb89c7e610953786a~tplv-k3u1fbpfcp-zoom-1.image'
---

<div>   
<div class="markdown-body"><style>@charset "UTF-8";.markdown-body&#123;line-height:1.75;font-family:Menlo,Monaco,Consolas,Courier New,monospace;letter-spacing:2px;background-image:linear-gradient(90deg,rgba(50,0,0,.05) 3%,transparent 0),linear-gradient(1turn,rgba(50,0,0,.05) 3%,transparent 0);background-size:20px 20px;background-position:50%;word-break:break-word;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1&#123;font-size:25px;margin-bottom:5px;border-left:5px solid #773098&#125;.markdown-body h1,.markdown-body h2&#123;display:inline-block;font-weight:700;padding-left:10px&#125;.markdown-body h2&#123;font-size:18px;border-left:5px solid #916dd5&#125;.markdown-body h3&#123;font-size:16px;font-weight:700;padding-left:10px;border-left:5px solid #d89cf6&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;border-radius:6px;display:block;margin:20px auto;object-fit:contain;box-shadow:2px 4px 7px #999&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;padding:.2em .5em;font-weight:700;font-size:1em;color:#916dd5;word-break:break-word;overflow-x:auto;background-color:none;border-radius:2px&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;display:block;font-size:12px;padding:16px 12px;margin:0;color:#333;word-break:normal;overflow-x:auto;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#916dd5;font-weight:700;border-bottom:1px solid #916dd5&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#773098&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #916dd5&#125;.markdown-body thead&#123;background-color:#916dd5;color:#fff;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#d89cf6&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #d89cf6;background-color:#f4eeff&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0;line-height:26px&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px;list-style-type:circle&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body b,.markdown-body strong&#123;color:#916dd5;font-weight:700&#125;.markdown-body b:before,.markdown-body strong:before&#123;content:"「"&#125;.markdown-body b:after,.markdown-body strong:after&#123;content:"」"&#125;.markdown-body em,.markdown-body i&#123;color:#916dd5&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h2 data-id="heading-0">jQuery的状态如何？</h2>
<p>经历过许多项目，直到今天笔者仍使用jQuery。这个库出现在2006年，比<code>React</code>、<code>Vue</code>甚至<code>Angular</code>早了许多年。</p>
<p>jQuery 曾经是 JavaScript 世界的关键。它使我们更容易开发Web应用程序。尤其是涉及到 <code>DOM</code> 操作和网络请求时，jQuery更加直接。</p>
<p>但是现在，发生了什么变化，谁还在使用它，它的受欢迎程度如何？</p>
<h2 data-id="heading-1">jQuery更新了什么东西？</h2>
<p>打开jQuery官方博客页面，看看有什么变化。老实说，并没有发生太多事情。jQuery3有很多变化，但没有一个是真正值得注意的。过去几年没有像 <code>React</code>中的<code>hooks</code>或者<code>Vue</code>的<code>composition API</code>这样的更新。</p>
<p>小的变化是支持 <code>for-of</code> 循环，所以它现在可以被用于<code>jQuery</code>对象。在底层、使用 <code>requestAnimationFrame</code> 来执行动画。</p>
<p>然而，没有更显著的变化。原因很简单：jQuery已经把它应该做的事情做到了足够的程度。</p>
<h2 data-id="heading-2">你们公司还在使用jQuery吗？</h2>
<p>当谈到选择一项技术时，市场上的大公司发挥着重要作用。当有能力的开发者团队选择一项技术时，它的分量很重。即使<code>jQuery</code>正在失去人气，它仍然在网络上发挥着巨大的作用。</p>
<p>据 Wappalyzer 称，在所有使用 <code>JavaScript</code> 库的网站中，<code>jQuery</code> 仍占超过 <code>34%</code> 的巨大份额。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/761095a300d34dbbb89c7e610953786a~tplv-k3u1fbpfcp-zoom-1.image" alt="那些年我们一起用过的JQuery" loading="lazy" referrerpolicy="no-referrer"></p>
<p>当然，对此类数据应该持保留态度：仅仅因为仍有数千或数百万个网站仍在使用这项技术，并不意味着这是一个好的决定。 <code>jQuery</code> 也已成为其他库必不可少的工具。</p>
<p>其中一个伟大的用途是Bootstrap，这个CSS框架使用jQuery进行所有的DOM操作，只有在Bootstrap5中，才取消了包含jQuery。</p>
<p>事实上，Stack Overflow 仍然使用 jQuery。其他使用 jQuery 的公司包括：</p>
<ul>
<li>Wellsfargo.com</li>
<li>Microsoft.com</li>
<li>Salesforce.com</li>
</ul>
<p>即时微软这样的大公司。尽管如此，我不会将公司的技术栈视为唯一的真理。甚至他们的网站也有犯错误或没有时间优化的人。</p>
<h2 data-id="heading-3">jQuery已经过时吗？</h2>
<p><code>没有过时的技术、只有适合自己项目的技术</code>。不过，不得不承认 jQuery 已经失去了极大的人气，尤其是在过去的五年里：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/408a05120aa74d698b504318c605b555~tplv-k3u1fbpfcp-zoom-1.image" alt="那些年我们一起用过的JQuery" loading="lazy" referrerpolicy="no-referrer"></p>
<p>许多人认为因为像 <code>React</code>、<code>Vue</code> 和 <code>Angular</code> 这样的框架和库变得越来越流行。但这并不是令jQuery过时的原因，尽管都是让我们很容易地构建Web应用程序，它们之间还是有很大的不同。</p>
<p>这些框架都是关于可重用组件、数据绑定、状态和单页应用程序的，jQuery应该永远像纯JavaScript的方言，更应该理解成是JavaScript的工具库。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">//js</span>
<span class="hljs-keyword">let</span> el = <span class="hljs-built_in">document</span>.getElementById(<span class="hljs-string">'contents'</span>);

<span class="hljs-comment">//jQuery </span>
<span class="hljs-keyword">let</span> el = $(<span class="hljs-string">'#contents'</span>);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>你不应该对所有东西都使用<code>React</code>、<code>Vue</code>或<code>Angular</code>。对于没有jQuery的站点来说，jQuery仍然是一个很大的帮助。</p>
<p><code>框架并没有杀死jQuery，杀死jQuery的是现代 JavaScript</code>。
尤其是方法 <code>querySelector</code> 许多 jQuery 粉丝引用作为他们切换的原因。</p>
<p>JavaScript 的发展使我们更容易访问 DOM。即使是 jQuery 处理得非常好的网络请求，在 JavaScript 中也变得更加简单比如新增<code>fetch</code>。</p>
<h2 data-id="heading-4">jQuery 影响性能吗?</h2>
<p>当然，库对你的网站的性能来说并不是那么好。特别是如果它们很大，加载时间就会增加。但是，jQuery只有30kb，并不是那么大。作为比较，看看Vue、React.js和Angular的压缩和最小化的NPM包。</p>
<ul>
<li>vue: 22 kb</li>
<li>react-dom + react: 41 kb</li>
<li>angular: 62 kb</li>
</ul>
<p>重要提示：这只是包的大小。应用程序的生产包的大小要大得多！因此，在加载时间方面，jQuery 做得很好。</p>
<p><strong>但是渲染性能呢？</strong></p>
<p>大型框架喜欢争夺谁的性能最好。基准测试通常是同时渲染巨大的表或数千个状态更新。你已经可以在这样的实验中看到不同之处，当然如果要追求极致性能，原生JavaScript 击败了他们。</p>
<p>但老实说，基准通常没有那么有意义。特别是对于只显示内容而不是“应用程序”的网站，库的渲染性能几乎不重要。用户不会注意到下拉列表使用了“慢速”库。</p>
<h2 data-id="heading-5">最后</h2>
<p>jQuery过去和现在都更适合于那些以内容为主的网站，而不是以功能为主。在更复杂的网络应用中，前端三大框架是更好的选择。笔者认为仍然使用 jQuery 并没有错。该库在许多情况下仍然非常有用，特别是如果您已经掌握了它。当然现代JavaScript也有很多新特性，我们也要了解并运用，时刻保持着学习新技术的态度。</p></div>  
</div>
            