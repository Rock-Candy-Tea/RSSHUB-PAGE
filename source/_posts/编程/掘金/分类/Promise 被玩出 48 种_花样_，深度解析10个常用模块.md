
---
title: 'Promise 被玩出 48 种_花样_，深度解析10个常用模块'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/a3f0aadad8dd4fedbaf9cff6dfd50e90~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Mon, 23 Aug 2021 17:37:20 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/a3f0aadad8dd4fedbaf9cff6dfd50e90~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body html cache"><style>.markdown-body&#123;position:relative;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#282d36&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px;color:#2f845e&#125;.markdown-body h2&#123;font-size:24px;display:inline-block;font-weight:700;background:#2f845e;color:#fff;padding:6px 8px 0 0;border-top-right-radius:6px;margin-right:2px;box-shadow:6px 3px 0 0 rgba(47,132,194,.2)&#125;.markdown-body h2:before&#123;content:" ";display:inline-block;width:8px&#125;.markdown-body h2:after&#123;content:" ";position:absolute;display:block;width:calc(100% - 40px);border-bottom:3px solid #2f845e&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%;box-shadow:6px 6px 6px #888&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75;border-top:6px solid #2f845e&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#262626;background:linear-gradient(180deg,rgba(66,185,131,.1),transparent)!important&#125;.markdown-body strong&#123;background-color:inherit;color:#2f845e&#125;.markdown-body em&#123;background-color:inherit;color:#949415&#125;.markdown-body a&#123;text-decoration:none;color:#2f8e54;border-bottom:1px solid #3f9e64&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#3f9e64&#125;.markdown-body a[class^=footnote]&#123;margin-left:4px&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:100%;max-width:100%;overflow:auto;border:2px solid #2f8e54&#125;.markdown-body thead&#123;background:#2f8e54;color:#fff;text-align:left;font-weight:700&#125;.markdown-body tr:nth-child(2n)&#123;background-color:rgba(153,255,188,.1)&#125;.markdown-body td,.markdown-body th&#123;width:100%;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;padding:1px 22px;margin:22px 0;border-left:6px solid #2f845e;background-color:rgba(66,185,131,.1);border-radius:4px&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body del&#123;color:#2f845e&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><blockquote>
<p>⚠️ 本文为掘金社区首发签约文章，未获授权禁止转载</p>
</blockquote>
<p>最近，阿宝哥在梳理 <a href="https://link.juejin.cn/?target=https%3A%2F%2Fzh.wikipedia.org%2Fwiki%2F%25E5%2591%25BD%25E4%25BB%25A4%25E8%25A1%258C%25E7%2595%258C%25E9%259D%25A2" target="_blank" rel="nofollow noopener noreferrer" title="https://zh.wikipedia.org/wiki/%E5%91%BD%E4%BB%A4%E8%A1%8C%E7%95%8C%E9%9D%A2" ref="nofollow noopener noreferrer">CLI</a>（Command Line Interface）的相关内容，就对优秀的 <a href="https://link.juejin.cn/?target=https%3A%2F%2Flerna.js.org%2F" target="_blank" rel="nofollow noopener noreferrer" title="https://lerna.js.org/" ref="nofollow noopener noreferrer">Lerna</a> 产生了兴趣，于是开始 “啃” 起了它的源码。在阅读开源项目时，阿宝哥习惯先阅读项目的 <strong>README.md</strong> 文档和 <strong>package.json</strong> 文件，而在 <strong>package.json</strong> 文件的 <strong>dependencies</strong> 字段中，阿宝哥见到了多个 <strong>p-</strong>* 的依赖包：</p>
<pre><code class="hljs language-json copyable" lang="json">&#123;
  <span class="hljs-attr">"name"</span>: <span class="hljs-string">"lerna-monorepo"</span>,
  <span class="hljs-attr">"version"</span>: <span class="hljs-string">"4.0.0-monorepo"</span>, 
  <span class="hljs-attr">"dependencies"</span>: &#123;
    <span class="hljs-attr">"p-map"</span>: <span class="hljs-string">"^4.0.0"</span>,
    <span class="hljs-attr">"p-map-series"</span>: <span class="hljs-string">"^2.1.0"</span>,
    <span class="hljs-attr">"p-pipe"</span>: <span class="hljs-string">"^3.1.0"</span>,
    <span class="hljs-attr">"p-queue"</span>: <span class="hljs-string">"^6.6.2"</span>,
    <span class="hljs-attr">"p-reduce"</span>: <span class="hljs-string">"^2.1.0"</span>,
    <span class="hljs-attr">"p-waterfall"</span>: <span class="hljs-string">"^2.1.1"</span>
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<blockquote>
<p>提示：如果你想知道阿宝哥如何阅读开源项目的话，可以阅读 <a href="https://juejin.cn/post/6887689159918485511" target="_blank" title="https://juejin.cn/post/6887689159918485511">使用这些思路与技巧，我读懂了多个优秀的开源项目</a> 这篇文章。</p>
</blockquote>
<p>之后，阿宝哥顺藤摸瓜找到了 <a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fsindresorhus%2Fpromise-fun" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/sindresorhus/promise-fun" ref="nofollow noopener noreferrer">promise-fun (3.5K)</a> 这个项目。该项目的作者 <strong><a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fsindresorhus" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/sindresorhus" ref="nofollow noopener noreferrer">sindresorhus</a></strong> 是一个全职做开源的大牛，Github 上拥有 <strong>43.9K</strong> 的关注者。同时，他还维护了多个优秀的开源项目，比如 <a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fsindresorhus%2Fawesome" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/sindresorhus/awesome" ref="nofollow noopener noreferrer">awesome (167K)</a>、<a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fsindresorhus%2Fawesome-nodejs" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/sindresorhus/awesome-nodejs" ref="nofollow noopener noreferrer">awesome-nodejs (42K)</a>、<a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fsindresorhus%2Fgot" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/sindresorhus/got" ref="nofollow noopener noreferrer">got (9.8K)</a>、<a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fsindresorhus%2Fora" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/sindresorhus/ora" ref="nofollow noopener noreferrer">ora (7.1K)</a> 和 <a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fsindresorhus%2Fscreenfull.js" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/sindresorhus/screenfull.js" ref="nofollow noopener noreferrer">screenfull.js (6.1K)</a> 等项目。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/a3f0aadad8dd4fedbaf9cff6dfd50e90~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>（图片来源 —— <a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fsindresorhus%25EF%25BC%2589" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/sindresorhus%EF%BC%89" ref="nofollow noopener noreferrer">github.com/sindresorhu…</a></p>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fsindresorhus%2Fpromise-fun" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/sindresorhus/promise-fun" ref="nofollow noopener noreferrer">promise-fun</a> 项目收录了 <strong><a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fsindresorhus" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/sindresorhus" ref="nofollow noopener noreferrer">sindresorhus</a></strong> 写过的 <strong>48</strong> 个与 <a href="https://link.juejin.cn/?target=https%3A%2F%2Fdeveloper.mozilla.org%2Fzh-CN%2Fdocs%2FWeb%2FJavaScript%2FReference%2FGlobal_Objects%2FPromise" target="_blank" rel="nofollow noopener noreferrer" title="https://developer.mozilla.org/zh-CN/docs/Web/JavaScript/Reference/Global_Objects/Promise" ref="nofollow noopener noreferrer">Promise</a> 相关的模块，比如前面见到的 <strong><a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fsindresorhus%2Fp-map" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/sindresorhus/p-map" ref="nofollow noopener noreferrer">p-map</a></strong>、<strong><a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fsindresorhus%2Fp-map-series" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/sindresorhus/p-map-series" ref="nofollow noopener noreferrer">p-map-series</a></strong>、<strong><a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fsindresorhus%2Fp-pipe" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/sindresorhus/p-pipe" ref="nofollow noopener noreferrer">p-pipe</a></strong> 和 <strong><a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fsindresorhus%2Fp-waterfall" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/sindresorhus/p-waterfall" ref="nofollow noopener noreferrer">p-waterfall</a></strong> 等模块。本文阿宝哥将筛选一些比较常用的模块，来详细分析每个模块的用法和具体的代码实现。</p>
<p>这些模块提供了很多有用的方法，利用这些方法，可以帮我们解决工作中一些很常见的问题，比如实现并发控制、异步任务处理等，特别是处理多种控制流，比如 <strong>series</strong>、<strong>waterfall</strong>、<strong>all</strong>、<strong>race</strong> 和 <strong>forever</strong> 等。</p>
<p>掘友们，准备好了没？让我们一起开启 <a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fsindresorhus%2Fpromise-fun" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/sindresorhus/promise-fun" ref="nofollow noopener noreferrer">promise-fun</a> 项目的 “探秘” 之旅。</p>
<h3 data-id="heading-0">初始化示例项目</h3>
<p>创建一个新的 <strong>learn-promise-fun</strong> 项目，然后在该项目的根目录下，执行 <code>npm init -y</code> 命令进行项目初始化操作。当该命令成功运行后，在项目根目录下将会生成 <strong>package.json</strong> 文件。由于 <a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fsindresorhus%2Fpromise-fun" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/sindresorhus/promise-fun" ref="nofollow noopener noreferrer">promise-fun</a> 项目中的很多模块使用了 ES Module，为了保证后续的示例代码能够正常运行，我们需要在 <strong>package.json</strong> 文件中，增加 <strong>type</strong> 字段并设置它的值为 <strong>"module"</strong>。</p>
<p>由于阿宝哥本地 <a href="https://link.juejin.cn/?target=https%3A%2F%2Fnodejs.org%2Fen%2F" target="_blank" rel="nofollow noopener noreferrer" title="https://nodejs.org/en/" ref="nofollow noopener noreferrer">Node.js</a> 的版本是 <strong>v12.16.2</strong>，要运行 ES Module 模块，还要添加 <strong>--experimental-modules</strong> 命令行选项。而如果你不想看到警告消息，还可以添加 <strong>--no-warnings</strong> 命令行选项。此外，为了避免每次运行示例代码时，都需要输入以上命令行选项，我们可以在 <strong>package.json</strong> 的 <strong>scripts</strong> 字段中定义相应的 <strong>npm script</strong> 命令，具体如下所示：</p>
<pre><code class="hljs language-json copyable" lang="json">&#123;
  <span class="hljs-attr">"name"</span>: <span class="hljs-string">"learn-promise-fun"</span>,
  <span class="hljs-attr">"type"</span>: <span class="hljs-string">"module"</span>,
  <span class="hljs-attr">"scripts"</span>: &#123;
    <span class="hljs-attr">"pall"</span>: <span class="hljs-string">"node --experimental-modules ./p-all/p-all.test.js"</span>,
    <span class="hljs-attr">"pfilter"</span>: <span class="hljs-string">"node --experimental-modules ./p-filter/p-filter.test.js"</span>,
    <span class="hljs-attr">"pforever"</span>: <span class="hljs-string">"node --experimental-modules ./p-forever/p-forever.test.js"</span>,
    <span class="hljs-attr">"preduce"</span>: <span class="hljs-string">"node --experimental-modules ./p-reduce/p-reduce.test.js"</span>,
    ...
  &#125;,
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>在完成项目初始化之后，我们先来回顾一下大家平时用得比较多的 <code>reduce</code>、<code>map</code> 和 <code>filter</code> 数组方法的特点：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/db8a77d6eb8e40dc92861826659fc1ba~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<blockquote>
<p>提示：上图通过👉  <strong><a href="https://link.juejin.cn/?target=https%3A%2F%2Fcarbon.now.sh%2F" target="_blank" rel="nofollow noopener noreferrer" title="https://carbon.now.sh/" ref="nofollow noopener noreferrer">carbon.now.sh/</a></strong> 在线网页制作生成。</p>
</blockquote>
<p>相信大家对图中的 <strong><a href="https://link.juejin.cn/?target=https%3A%2F%2Fdeveloper.mozilla.org%2Fzh-CN%2Fdocs%2FWeb%2FJavaScript%2FReference%2FGlobal_Objects%2FArray%2FReduce" target="_blank" rel="nofollow noopener noreferrer" title="https://developer.mozilla.org/zh-CN/docs/Web/JavaScript/Reference/Global_Objects/Array/Reduce" ref="nofollow noopener noreferrer">Array.prototype.reduce</a></strong> 方法不会陌生，该方法用于对数组中的每个元素执行一个 <strong>reducer</strong> 函数，并将结果汇总为单个返回值。对应的使用示例，如下所示：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">const</span> array1 = [<span class="hljs-number">1</span>, <span class="hljs-number">2</span>, <span class="hljs-number">3</span>, <span class="hljs-number">4</span>];
<span class="hljs-keyword">const</span> reducer = <span class="hljs-function">(<span class="hljs-params">accumulator, currentValue</span>) =></span> accumulator + currentValue;

<span class="hljs-comment">// 1 + 2 + 3 + 4</span>
<span class="hljs-built_in">console</span>.log(array1.reduce(reducer)); <span class="hljs-comment">// 10</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>其中 <strong>reducer</strong> 函数接收 4 个参数：</p>
<ul>
<li>acc（Accumulator）：累计器</li>
<li>cur（Current Value）： 当前值</li>
<li>idx（Current Index）：当前索引</li>
<li>src（Source Array）： 源数组</li>
</ul>
<p>而接下来，我们要介绍的 <a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fsindresorhus%2Fp-reduce" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/sindresorhus/p-reduce" ref="nofollow noopener noreferrer">p-reduce</a> 模块，就提供了跟 <strong><a href="https://link.juejin.cn/?target=https%3A%2F%2Fdeveloper.mozilla.org%2Fzh-CN%2Fdocs%2FWeb%2FJavaScript%2FReference%2FGlobal_Objects%2FArray%2FReduce" target="_blank" rel="nofollow noopener noreferrer" title="https://developer.mozilla.org/zh-CN/docs/Web/JavaScript/Reference/Global_Objects/Array/Reduce" ref="nofollow noopener noreferrer">Array.prototype.reduce</a></strong> 方法类似的功能。</p>
<h3 data-id="heading-1"><a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fsindresorhus%2Fp-reduce" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/sindresorhus/p-reduce" ref="nofollow noopener noreferrer">p-reduce</a></h3>
<blockquote>
<p>Reduce a list of values using promises into a promise for a value</p>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fsindresorhus%2Fp-reduce" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/sindresorhus/p-reduce" ref="nofollow noopener noreferrer">github.com/sindresorhu…</a></p>
</blockquote>
<h4 data-id="heading-2">使用说明</h4>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fsindresorhus%2Fp-reduce" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/sindresorhus/p-reduce" ref="nofollow noopener noreferrer">p-reduce</a> 适用于需要根据异步资源计算累加值的场景。该模块默认导出了一个 <strong>pReduce</strong> 函数，该函数的签名如下：</p>
<blockquote>
<p><strong><a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fsindresorhus%2Fp-reduce" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/sindresorhus/p-reduce" ref="nofollow noopener noreferrer">pReduce(input, reducer, initialValue): Promise</a></strong></p>
</blockquote>
<ul>
<li><code>input: Iterable<Promise|any></code></li>
<li><code>reducer(previousValue, currentValue, index): Function</code></li>
<li><code>initialValue: unknown</code></li>
</ul>
<p>了解完 <strong>pReduce</strong> 函数的签名之后，我们来看一下该函数如何使用。</p>
<h4 data-id="heading-3">使用示例</h4>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">// p-reduce/p-reduce.test.js</span>
<span class="hljs-keyword">import</span> delay <span class="hljs-keyword">from</span> <span class="hljs-string">"delay"</span>;
<span class="hljs-keyword">import</span> pReduce <span class="hljs-keyword">from</span> <span class="hljs-string">"p-reduce"</span>;

<span class="hljs-keyword">const</span> inputs = [<span class="hljs-built_in">Promise</span>.resolve(<span class="hljs-number">1</span>), delay(<span class="hljs-number">50</span>, &#123; <span class="hljs-attr">value</span>: <span class="hljs-number">6</span> &#125;), <span class="hljs-number">8</span>];

<span class="hljs-keyword">async</span> <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">main</span>(<span class="hljs-params"></span>) </span>&#123;
  <span class="hljs-keyword">const</span> result = <span class="hljs-keyword">await</span> pReduce(inputs, <span class="hljs-keyword">async</span> (a, b) => a + b, <span class="hljs-number">0</span>);
  <span class="hljs-built_in">console</span>.dir(result); <span class="hljs-comment">// 输出结果：15</span>
&#125;

main();
<span class="copy-code-btn">复制代码</span></code></pre>
<p>在以上示例中，我们导入了 <strong><a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fsindresorhus%2Fdelay" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/sindresorhus/delay" ref="nofollow noopener noreferrer">delay</a></strong> 模块默认导出的 <code>delay</code> 方法，该方法可用于按照给定的时间，延迟一个 Promise 对象。即在给定的时间之后，Promise 状态才会变成 <strong>resolved</strong>。默认情况下，<strong><a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fsindresorhus%2Fdelay" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/sindresorhus/delay" ref="nofollow noopener noreferrer">delay</a></strong> 模块内部是通过 <a href="https://link.juejin.cn/?target=https%3A%2F%2Fdeveloper.mozilla.org%2Fzh-CN%2Fdocs%2FWeb%2FAPI%2FWindowOrWorkerGlobalScope%2FsetTimeout" target="_blank" rel="nofollow noopener noreferrer" title="https://developer.mozilla.org/zh-CN/docs/Web/API/WindowOrWorkerGlobalScope/setTimeout" ref="nofollow noopener noreferrer">setTimeout</a> API 来实现延迟功能的。示例中 <code>delay(50, &#123; value: 6 &#125;)</code> 表示延迟 50ms 后，Promise 对象的返回值为 <strong>6</strong>。而在 <code>main</code> 函数内部，我们使用了 <code>pReduce</code> 函数来计算 <code>inputs</code> 数组元素的累加值。当以上代码成功运行之后，命令行会输出 <strong>15</strong>。</p>
<p>下面我们来分析一下 <code>pReduce</code> 函数内部是如何实现的。</p>
<h4 data-id="heading-4">源码分析</h4>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">// https://github.com/sindresorhus/p-reduce/blob/main/index.js</span>
<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> <span class="hljs-keyword">async</span> <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">pReduce</span>(<span class="hljs-params">iterable, reducer, initialValue</span>) </span>&#123;
  <span class="hljs-keyword">return</span> <span class="hljs-keyword">new</span> <span class="hljs-built_in">Promise</span>(<span class="hljs-function">(<span class="hljs-params">resolve, reject</span>) =></span> &#123;
    <span class="hljs-keyword">const</span> iterator = iterable[<span class="hljs-built_in">Symbol</span>.iterator](); <span class="hljs-comment">// 获取迭代器</span>
    <span class="hljs-keyword">let</span> index = <span class="hljs-number">0</span>; <span class="hljs-comment">// 索引值</span>

    <span class="hljs-keyword">const</span> next = <span class="hljs-keyword">async</span> (total) => &#123;
      <span class="hljs-keyword">const</span> element = iterator.next(); <span class="hljs-comment">// 获取下一项</span>

      <span class="hljs-keyword">if</span> (element.done) &#123; <span class="hljs-comment">// 判断迭代器是否迭代完成</span>
        resolve(total);
        <span class="hljs-keyword">return</span>;
      &#125;

      <span class="hljs-keyword">try</span> &#123;
        <span class="hljs-keyword">const</span> [resolvedTotal, resolvedValue] = <span class="hljs-keyword">await</span> <span class="hljs-built_in">Promise</span>.all([
          total,
          element.value,
        ]);
        <span class="hljs-comment">// 迭代下一项</span>
        <span class="hljs-comment">// reducer(previousValue, currentValue, index): Function</span>
        next(reducer(resolvedTotal, resolvedValue, index++));
      &#125; <span class="hljs-keyword">catch</span> (error) &#123;
        reject(error);
      &#125;
    &#125;;

    <span class="hljs-comment">// 使用初始值，开始迭代</span>
    next(initialValue);
  &#125;);
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>在以上代码中，核心的流程就是通过获取 <code>iterable</code> 对象内部的迭代器，来不断地进行迭代。此外，在 <code>pReduce</code> 函数中，使用了 <a href="https://link.juejin.cn/?target=https%3A%2F%2Fdeveloper.mozilla.org%2Fzh-CN%2Fdocs%2FWeb%2FJavaScript%2FReference%2FGlobal_Objects%2FPromise%2Fall" target="_blank" rel="nofollow noopener noreferrer" title="https://developer.mozilla.org/zh-CN/docs/Web/JavaScript/Reference/Global_Objects/Promise/all" ref="nofollow noopener noreferrer"><strong>Promise.all</strong></a> 方法，该方法会返回一个 promise 对象，当输入的所有 promise 对象的状态都变成 <code>resolved</code> 时，返回的 promise 对象就会以数组的形式，返回每个 promise 对象 resolve 后的结果。当输入的任何一个 promise 对象状态变成 <code>rejected</code> 时，则返回的 promise 对象会 reject 对应的错误信息。</p>
<p>不过，需要注意的是，<a href="https://link.juejin.cn/?target=https%3A%2F%2Fdeveloper.mozilla.org%2Fzh-CN%2Fdocs%2FWeb%2FJavaScript%2FReference%2FGlobal_Objects%2FPromise%2Fall" target="_blank" rel="nofollow noopener noreferrer" title="https://developer.mozilla.org/zh-CN/docs/Web/JavaScript/Reference/Global_Objects/Promise/all" ref="nofollow noopener noreferrer"><strong>Promise.all</strong></a> 方法存在兼容性问题，具体的兼容性如下图所示：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/622880e18e4149fcbb1fccff73634df6~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>（图片来源 —— <a href="https://link.juejin.cn/?target=https%3A%2F%2Fcaniuse.com%2F%3Fsearch%3DPromise.all%25EF%25BC%2589" target="_blank" rel="nofollow noopener noreferrer" title="https://caniuse.com/?search=Promise.all%EF%BC%89" ref="nofollow noopener noreferrer">caniuse.com/?search=Pro…</a></p>
<p>可能有一些小伙伴对 <a href="https://link.juejin.cn/?target=https%3A%2F%2Fdeveloper.mozilla.org%2Fzh-CN%2Fdocs%2FWeb%2FJavaScript%2FReference%2FGlobal_Objects%2FPromise%2Fall" target="_blank" rel="nofollow noopener noreferrer" title="https://developer.mozilla.org/zh-CN/docs/Web/JavaScript/Reference/Global_Objects/Promise/all" ref="nofollow noopener noreferrer"><strong>Promise.all</strong></a> 还不熟悉，它又是一道比较高频的手写题。所以，接下来我们来手写一个简易版的 <a href="https://link.juejin.cn/?target=https%3A%2F%2Fdeveloper.mozilla.org%2Fzh-CN%2Fdocs%2FWeb%2FJavaScript%2FReference%2FGlobal_Objects%2FPromise%2Fall" target="_blank" rel="nofollow noopener noreferrer" title="https://developer.mozilla.org/zh-CN/docs/Web/JavaScript/Reference/Global_Objects/Promise/all" ref="nofollow noopener noreferrer"><strong>Promise.all</strong></a>：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-built_in">Promise</span>.all = <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params">iterators</span>) </span>&#123;
  <span class="hljs-keyword">return</span> <span class="hljs-keyword">new</span> <span class="hljs-built_in">Promise</span>(<span class="hljs-function">(<span class="hljs-params">resolve, reject</span>) =></span> &#123;
    <span class="hljs-keyword">if</span> (!iterators || iterators.length === <span class="hljs-number">0</span>) &#123;
      resolve([]);
    &#125; <span class="hljs-keyword">else</span> &#123;
      <span class="hljs-keyword">let</span> count = <span class="hljs-number">0</span>; <span class="hljs-comment">// 计数器，用于判断所有任务是否执行完成</span>
      <span class="hljs-keyword">let</span> result = []; <span class="hljs-comment">// 结果数组</span>
      <span class="hljs-keyword">for</span> (<span class="hljs-keyword">let</span> i = <span class="hljs-number">0</span>; i < iterators.length; i++) &#123;
        <span class="hljs-comment">// 考虑到iterators[i]可能是普通对象，则统一包装为Promise对象</span>
        <span class="hljs-built_in">Promise</span>.resolve(iterators[i]).then(
          <span class="hljs-function">(<span class="hljs-params">data</span>) =></span> &#123;
            result[i] = data; <span class="hljs-comment">// 按顺序保存对应的结果</span>
            <span class="hljs-comment">// 当所有任务都执行完成后，再统一返回结果</span>
            <span class="hljs-keyword">if</span> (++count === iterators.length) &#123;
              resolve(result);
            &#125;
          &#125;,
          <span class="hljs-function">(<span class="hljs-params">err</span>) =></span> &#123;
            reject(err); <span class="hljs-comment">// 任何一个Promise对象执行失败，则调用reject()方法</span>
            <span class="hljs-keyword">return</span>;
          &#125;
        );
      &#125;
    &#125;
  &#125;);
&#125;;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-5"><a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fsindresorhus%2Fp-map" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/sindresorhus/p-map" ref="nofollow noopener noreferrer">p-map</a></h3>
<blockquote>
<p>Map over promises concurrently</p>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fsindresorhus%2Fp-map" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/sindresorhus/p-map" ref="nofollow noopener noreferrer">github.com/sindresorhu…</a></p>
</blockquote>
<h4 data-id="heading-6">使用说明</h4>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fsindresorhus%2Fp-map" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/sindresorhus/p-map" ref="nofollow noopener noreferrer">p-map</a> 适用于使用不同的输入多次运行 <strong>promise-returning</strong> 或 <strong>async</strong> 函数的场景。与前面介绍的 <a href="https://link.juejin.cn/?target=https%3A%2F%2Fdeveloper.mozilla.org%2Fzh-CN%2Fdocs%2FWeb%2FJavaScript%2FReference%2FGlobal_Objects%2FPromise%2Fall" target="_blank" rel="nofollow noopener noreferrer" title="https://developer.mozilla.org/zh-CN/docs/Web/JavaScript/Reference/Global_Objects/Promise/all" ref="nofollow noopener noreferrer">Promise.all</a> 方法的区别是，你可以控制并发，也可以决定是否在出现错误时停止迭代。该模块默认导出了一个 <strong>pMap</strong> 函数，该函数的签名如下：</p>
<blockquote>
<p><strong><a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fsindresorhus%2Fp-map" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/sindresorhus/p-map" ref="nofollow noopener noreferrer">pMap(input, mapper, options): Promise</a></strong></p>
</blockquote>
<ul>
<li><code>input: Iterable<Promise | unknown></code></li>
<li><code>mapper(element, index): Function</code></li>
<li><code>options: object</code>
<ul>
<li><code>concurrency: number</code> —— 并发数，默认值 <code>Infinity</code>，最小值为 <code>1</code>；</li>
<li><code>stopOnError: boolean</code> —— 出现异常时，是否终止，默认值为 <code>true</code>。</li>
</ul>
</li>
</ul>
<p>了解完 <strong>pMap</strong> 函数的签名之后，我们来看一下该函数如何使用。</p>
<h4 data-id="heading-7">使用示例</h4>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">// p-map/p-map.test.js</span>
<span class="hljs-keyword">import</span> delay <span class="hljs-keyword">from</span> <span class="hljs-string">"delay"</span>;
<span class="hljs-keyword">import</span> pMap <span class="hljs-keyword">from</span> <span class="hljs-string">"p-map"</span>;

<span class="hljs-keyword">const</span> inputs = [<span class="hljs-number">200</span>, <span class="hljs-number">100</span>, <span class="hljs-number">50</span>];
<span class="hljs-keyword">const</span> mapper = <span class="hljs-function">(<span class="hljs-params">value</span>) =></span> delay(value, &#123; value &#125;);

<span class="hljs-keyword">async</span> <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">main</span>(<span class="hljs-params"></span>) </span>&#123;
  <span class="hljs-built_in">console</span>.time(<span class="hljs-string">"start"</span>);
  <span class="hljs-keyword">const</span> result = <span class="hljs-keyword">await</span> pMap(inputs, mapper, &#123; <span class="hljs-attr">concurrency</span>: <span class="hljs-number">1</span> &#125;);
  <span class="hljs-built_in">console</span>.dir(result); <span class="hljs-comment">// 输出结果：[ 200, 100, 50 ]</span>
  <span class="hljs-built_in">console</span>.timeEnd(<span class="hljs-string">"start"</span>);
&#125;

main();
<span class="copy-code-btn">复制代码</span></code></pre>
<p>在以上示例中，我们也使用了 <strong><a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fsindresorhus%2Fdelay" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/sindresorhus/delay" ref="nofollow noopener noreferrer">delay</a></strong> 模块导出的 <code>delay</code> 函数，用于实现延迟功能。当成功执行以上代码后，命令行会输出以下信息：</p>
<pre><code class="hljs language-shell copyable" lang="shell">[ 200, 100, 50 ]
start: 368.708ms
<span class="copy-code-btn">复制代码</span></code></pre>
<p>而当把 <code>concurrency</code> 属性的值更改为 <code>2</code> 之后，再次执行以上代码。那么命令行将会输出以下信息：</p>
<pre><code class="hljs language-shell copyable" lang="shell">[ 200, 100, 50 ]
start: 210.322ms
<span class="copy-code-btn">复制代码</span></code></pre>
<p>观察以上的输出结果，我们可以看出并发数为 <code>1</code> 时，程序的运行时间大于 350ms。而如果并发数为 <code>2</code> 时，多个任务是并行执行的，所以程序的运行时间只需 210 多毫秒。那么 <code>pMap</code> 函数，内部是如何实现并发控制的呢？下面来分析一下 <code>pMap</code> 函数的源码。</p>
<h4 data-id="heading-8">源码分析</h4>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">// https://github.com/sindresorhus/p-map/blob/main/index.js</span>
<span class="hljs-keyword">import</span> AggregateError <span class="hljs-keyword">from</span> <span class="hljs-string">"aggregate-error"</span>;

<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> <span class="hljs-keyword">async</span> <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">pMap</span>(<span class="hljs-params">
  iterable,
  mapper,
  &#123; concurrency = <span class="hljs-built_in">Number</span>.POSITIVE_INFINITY, stopOnError = <span class="hljs-literal">true</span> &#125; = &#123;&#125;
</span>) </span>&#123;
  <span class="hljs-keyword">return</span> <span class="hljs-keyword">new</span> <span class="hljs-built_in">Promise</span>(<span class="hljs-function">(<span class="hljs-params">resolve, reject</span>) =></span> &#123;
    <span class="hljs-comment">// 省略参数校验代码</span>
    <span class="hljs-keyword">const</span> result = []; <span class="hljs-comment">// 存储返回结果</span>
    <span class="hljs-keyword">const</span> errors = []; <span class="hljs-comment">// 存储异常对象</span>
    <span class="hljs-keyword">const</span> skippedIndexes = []; <span class="hljs-comment">// 保存跳过项索引值的数组</span>
    <span class="hljs-keyword">const</span> iterator = iterable[<span class="hljs-built_in">Symbol</span>.iterator](); <span class="hljs-comment">// 获取迭代器</span>
    <span class="hljs-keyword">let</span> isRejected = <span class="hljs-literal">false</span>; <span class="hljs-comment">// 标识是否出现异常</span>
    <span class="hljs-keyword">let</span> isIterableDone = <span class="hljs-literal">false</span>; <span class="hljs-comment">// 标识是否已迭代完成</span>
    <span class="hljs-keyword">let</span> resolvingCount = <span class="hljs-number">0</span>; <span class="hljs-comment">// 正在处理的任务个数</span>
    <span class="hljs-keyword">let</span> currentIndex = <span class="hljs-number">0</span>; <span class="hljs-comment">// 当前索引</span>

    <span class="hljs-keyword">const</span> next = <span class="hljs-function">() =></span> &#123;
      <span class="hljs-keyword">if</span> (isRejected) &#123; <span class="hljs-comment">// 若出现异常，则直接返回</span>
        <span class="hljs-keyword">return</span>;
      &#125;

      <span class="hljs-keyword">const</span> nextItem = iterator.next(); <span class="hljs-comment">// 获取下一项</span>
      <span class="hljs-keyword">const</span> index = currentIndex; <span class="hljs-comment">// 记录当前的索引值</span>
      currentIndex++;

      <span class="hljs-keyword">if</span> (nextItem.done) &#123; <span class="hljs-comment">// 判断迭代器是否迭代完成</span>
        isIterableDone = <span class="hljs-literal">true</span>;

        <span class="hljs-comment">// 判断是否所有的任务都已经完成了</span>
        <span class="hljs-keyword">if</span> (resolvingCount === <span class="hljs-number">0</span>) &#123; 
          <span class="hljs-keyword">if</span> (!stopOnError && errors.length > <span class="hljs-number">0</span>) &#123; <span class="hljs-comment">// 异常处理</span>
            reject(<span class="hljs-keyword">new</span> AggregateError(errors));
          &#125; <span class="hljs-keyword">else</span> &#123;
            <span class="hljs-keyword">for</span> (<span class="hljs-keyword">const</span> skippedIndex <span class="hljs-keyword">of</span> skippedIndexes) &#123;
              <span class="hljs-comment">// 删除跳过的值，不然会存在空的占位</span>
              result.splice(skippedIndex, <span class="hljs-number">1</span>); 
            &#125;
            resolve(result); <span class="hljs-comment">// 返回最终的处理结果</span>
          &#125;
        &#125;
        <span class="hljs-keyword">return</span>;
      &#125;

      resolvingCount++; <span class="hljs-comment">// 正在处理的任务数加1</span>

      (<span class="hljs-keyword">async</span> () => &#123;
        <span class="hljs-keyword">try</span> &#123;
          <span class="hljs-keyword">const</span> element = <span class="hljs-keyword">await</span> nextItem.value;

          <span class="hljs-keyword">if</span> (isRejected) &#123;
            <span class="hljs-keyword">return</span>;
          &#125;

          <span class="hljs-comment">// 调用mapper函数，进行值进行处理</span>
          <span class="hljs-keyword">const</span> value = <span class="hljs-keyword">await</span> mapper(element, index);
          <span class="hljs-comment">// 处理跳过的情形，可以在mapper函数中返回pMapSkip，来跳过当前项</span>
          <span class="hljs-comment">// 比如在异常捕获的catch语句中，返回pMapSkip值</span>
          <span class="hljs-keyword">if</span> (value === pMapSkip) &#123; <span class="hljs-comment">// pMapSkip = Symbol("skip")</span>
            skippedIndexes.push(index);
          &#125; <span class="hljs-keyword">else</span> &#123;
            result[index] = value; <span class="hljs-comment">// 把返回值按照索引进行保存</span>
          &#125;

          resolvingCount--;
          next(); <span class="hljs-comment">// 迭代下一项</span>
        &#125; <span class="hljs-keyword">catch</span> (error) &#123;
          <span class="hljs-keyword">if</span> (stopOnError) &#123; <span class="hljs-comment">// 出现异常时，是否终止，默认值为true</span>
            isRejected = <span class="hljs-literal">true</span>;
            reject(error);
          &#125; <span class="hljs-keyword">else</span> &#123;
            errors.push(error);
            resolvingCount--;
            next();
          &#125;
        &#125;
      &#125;)();
    &#125;;

    <span class="hljs-comment">// 根据配置的concurrency值，并发执行任务</span>
    <span class="hljs-keyword">for</span> (<span class="hljs-keyword">let</span> index = <span class="hljs-number">0</span>; index < concurrency; index++) &#123;
      next();
      <span class="hljs-keyword">if</span> (isIterableDone) &#123;
        <span class="hljs-keyword">break</span>;
      &#125;
    &#125;
  &#125;);
&#125;

<span class="hljs-keyword">export</span> <span class="hljs-keyword">const</span> pMapSkip = <span class="hljs-built_in">Symbol</span>(<span class="hljs-string">"skip"</span>);
<span class="copy-code-btn">复制代码</span></code></pre>
<p><code>pMap</code> 函数内部的处理逻辑还是蛮清晰的，把核心的处理逻辑都封装在 <code>next</code> 函数中。在调用 <code>pMap</code> 函数之后，内部会根据配置的<code>concurrency</code> 值，并发调用 <code>next</code> 函数。而在 <code>next</code> 函数内部，会通过 <strong>async/await</strong> 来控制任务的执行过程。</p>
<p>在 <code>pMap</code> 函数中，作者巧妙设计了 <strong>pMapSkip</strong>。当我们在 <code>mapper</code> 函数中返回了 <strong>pMapSkip</strong> 之后，将会从返回的结果数组中移除对应索引项的值。了解完 <strong>pMapSkip</strong> 的作用之后，我们来举个简单的例子：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">import</span> pMap, &#123; pMapSkip &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">"p-map"</span>;

<span class="hljs-keyword">const</span> inputs = [<span class="hljs-number">200</span>, pMapSkip, <span class="hljs-number">50</span>];
<span class="hljs-keyword">const</span> mapper = <span class="hljs-keyword">async</span> (value) => value;

<span class="hljs-keyword">async</span> <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">main</span>(<span class="hljs-params"></span>) </span>&#123;
  <span class="hljs-built_in">console</span>.time(<span class="hljs-string">"start"</span>);
  <span class="hljs-keyword">const</span> result = <span class="hljs-keyword">await</span> pMap(inputs, mapper, &#123; <span class="hljs-attr">concurrency</span>: <span class="hljs-number">2</span> &#125;);
  <span class="hljs-built_in">console</span>.dir(result); <span class="hljs-comment">// [ 200, 50 ]</span>
  <span class="hljs-built_in">console</span>.timeEnd(<span class="hljs-string">"start"</span>);
&#125;

main();
<span class="copy-code-btn">复制代码</span></code></pre>
<p>在以上代码中，我们的 <code>inputs</code> 数组中包含了 <code>pMapSkip</code> 值，当使用 <code>pMap</code> 函数对 <code>inputs</code> 数组进行处理后，<code>pMapSkip</code> 值将会被过滤掉，所以最终 <code>result</code> 的结果为 <strong>[200 , 50]</strong>。</p>
<h3 data-id="heading-9"><a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fsindresorhus%2Fp-filter" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/sindresorhus/p-filter" ref="nofollow noopener noreferrer">p-filter</a></h3>
<blockquote>
<p>Filter promises concurrently</p>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fsindresorhus%2Fp-filter" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/sindresorhus/p-filter" ref="nofollow noopener noreferrer">github.com/sindresorhu…</a></p>
</blockquote>
<h4 data-id="heading-10">使用说明</h4>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fsindresorhus%2Fp-filter" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/sindresorhus/p-filter" ref="nofollow noopener noreferrer">p-filter</a> 适用于使用不同的输入多次运行 <strong>promise-returning</strong> 或 <strong>async</strong> 函数，并对返回的结果进行过滤的场景。该模块默认导出了一个 <strong>pFilter</strong> 函数，该函数的签名如下：</p>
<blockquote>
<p><strong><a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fsindresorhus%2Fp-filter" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/sindresorhus/p-filter" ref="nofollow noopener noreferrer">pFilter(input, filterer, options): Promise</a></strong></p>
</blockquote>
<ul>
<li><code>input: Iterable<Promise | any></code></li>
<li><code>filterer(element, index): Function</code></li>
<li><code>options: object</code>
<ul>
<li><code>concurrency: number</code> —— 并发数，默认值 <code>Infinity</code>，最小值为 <code>1</code>。</li>
</ul>
</li>
</ul>
<p>了解完 <strong>pFilter</strong> 函数的签名之后，我们来看一下该函数如何使用。</p>
<h4 data-id="heading-11">使用示例</h4>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">// p-filter/p-filter.test.js</span>
<span class="hljs-keyword">import</span> pFilter <span class="hljs-keyword">from</span> <span class="hljs-string">"p-filter"</span>;

<span class="hljs-keyword">const</span> inputs = [<span class="hljs-built_in">Promise</span>.resolve(<span class="hljs-number">1</span>), <span class="hljs-number">2</span>, <span class="hljs-number">3</span>];
<span class="hljs-keyword">const</span> filterer = <span class="hljs-function">(<span class="hljs-params">x</span>) =></span> x % <span class="hljs-number">2</span>;

<span class="hljs-keyword">async</span> <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">main</span>(<span class="hljs-params"></span>) </span>&#123;
  <span class="hljs-keyword">const</span> result = <span class="hljs-keyword">await</span> pFilter(inputs, filterer, &#123; <span class="hljs-attr">concurrency</span>: <span class="hljs-number">1</span> &#125;);
  <span class="hljs-built_in">console</span>.dir(result); <span class="hljs-comment">// 输出结果：[ 1, 3 ]</span>
&#125;

main();
<span class="copy-code-btn">复制代码</span></code></pre>
<p>在以上示例中，我们使用 <code>pFilter</code> 函数对包含 <code>Promise</code> 对象的 <code>inputs</code> 数组，应用了 <code>(x) => x % 2</code> 过滤器。当以上代码成功运行后，命令行会输出 <strong>[1, 3]</strong>。</p>
<h4 data-id="heading-12">源码分析</h4>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">// https://github.com/sindresorhus/p-filter/blob/main/index.js</span>
<span class="hljs-keyword">const</span> pMap = <span class="hljs-built_in">require</span>(<span class="hljs-string">'p-map'</span>);

<span class="hljs-keyword">const</span> pFilter = <span class="hljs-keyword">async</span> (iterable, filterer, options) => &#123;
<span class="hljs-keyword">const</span> values = <span class="hljs-keyword">await</span> pMap(
iterable,
<span class="hljs-function">(<span class="hljs-params">element, index</span>) =></span> <span class="hljs-built_in">Promise</span>.all([filterer(element, index), element]),
options
);
<span class="hljs-keyword">return</span> values.filter(<span class="hljs-function"><span class="hljs-params">value</span> =></span> <span class="hljs-built_in">Boolean</span>(value[<span class="hljs-number">0</span>])).map(<span class="hljs-function"><span class="hljs-params">value</span> =></span> value[<span class="hljs-number">1</span>]);
&#125;;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>由以上代码可知，在 <code>pFilter</code> 函数内部，使用了我们前面已经介绍过的 <code>pMap</code> 和 <code>Promise.all</code> 函数。要理解以上代码，我们还需要来回顾一下 <code>pMap</code> 函数的关键代码：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">// https://github.com/sindresorhus/p-map/blob/main/index.js</span>
<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> <span class="hljs-keyword">async</span> <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">pMap</span>(<span class="hljs-params">
  iterable, mapper,
  &#123; concurrency = <span class="hljs-built_in">Number</span>.POSITIVE_INFINITY, stopOnError = <span class="hljs-literal">true</span> &#125; = &#123;&#125;
</span>) </span>&#123;
  <span class="hljs-keyword">const</span> iterator = iterable[<span class="hljs-built_in">Symbol</span>.iterator](); <span class="hljs-comment">// 获取迭代器</span>
  <span class="hljs-keyword">let</span> currentIndex = <span class="hljs-number">0</span>; <span class="hljs-comment">// 当前索引</span>
  
  <span class="hljs-keyword">const</span> next = <span class="hljs-function">() =></span> &#123;
    <span class="hljs-keyword">const</span> nextItem = iterator.next(); <span class="hljs-comment">// 获取下一项</span>
    <span class="hljs-keyword">const</span> index = currentIndex;
    currentIndex++;
    (<span class="hljs-keyword">async</span> () => &#123;
        <span class="hljs-keyword">try</span> &#123;
          <span class="hljs-comment">// element => await Promise.resolve(1);</span>
          <span class="hljs-keyword">const</span> element = <span class="hljs-keyword">await</span> nextItem.value;
          <span class="hljs-comment">// mapper => (element, index) => Promise.all([filterer(element, index), element])</span>
          <span class="hljs-keyword">const</span> value = <span class="hljs-keyword">await</span> mapper(element, index);
          <span class="hljs-keyword">if</span> (value === pMapSkip) &#123;
            skippedIndexes.push(index);
          &#125; <span class="hljs-keyword">else</span> &#123;
            result[index] = value; <span class="hljs-comment">// 把返回值按照索引进行保存</span>
          &#125;
          resolvingCount--;
          next(); <span class="hljs-comment">// 迭代下一项</span>
        &#125; <span class="hljs-keyword">catch</span> (error) &#123;
          <span class="hljs-comment">// 省略异常处理代码</span>
        &#125;
    &#125;)();
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>因为 <code>pFilter</code> 函数中所用的 <code>mapper</code> 函数是 <code>(element, index) => Promise.all([filterer(element, index), element])</code>，所以 <code>await mapper(element, index)</code> 表达式的返回值是一个数组。数组的第 1 项是 <code>filterer</code> 过滤器的处理结果，而数组的第 2 项是当前元素的值。因此在调用 <code>pMap</code> 函数后，它的返回值是一个二维数组。所以在获取 <code>pMap</code> 函数的返回值之后， 会使用以下语句对返回值进行处理：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript">values.filter(<span class="hljs-function"><span class="hljs-params">value</span> =></span> <span class="hljs-built_in">Boolean</span>(value[<span class="hljs-number">0</span>])).map(<span class="hljs-function"><span class="hljs-params">value</span> =></span> value[<span class="hljs-number">1</span>])
<span class="copy-code-btn">复制代码</span></code></pre>
<p>其实，对于前面的 <code>pFilter</code> 示例来说，除了 <code>inputs</code> 可以含有 Promise 对象，我们的 <code>filterer</code> 过滤器也可以返回 Promise 对象：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">import</span> pFilter <span class="hljs-keyword">from</span> <span class="hljs-string">"p-filter"</span>;

<span class="hljs-keyword">const</span> inputs = [<span class="hljs-built_in">Promise</span>.resolve(<span class="hljs-number">1</span>), <span class="hljs-number">2</span>, <span class="hljs-number">3</span>];
<span class="hljs-keyword">const</span> filterer = <span class="hljs-function">(<span class="hljs-params">x</span>) =></span> <span class="hljs-built_in">Promise</span>.resolve(x % <span class="hljs-number">2</span>);

<span class="hljs-keyword">async</span> <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">main</span>(<span class="hljs-params"></span>) </span>&#123;
  <span class="hljs-keyword">const</span> result = <span class="hljs-keyword">await</span> pFilter(inputs, filterer);
  <span class="hljs-built_in">console</span>.dir(result); <span class="hljs-comment">// [ 1, 3 ]</span>
&#125;

main();
<span class="copy-code-btn">复制代码</span></code></pre>
<p>以上代码成功执行后，命令行的输出结果也是 <strong>[1, 3]</strong>。好的，现在我们已经介绍了 <a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fsindresorhus%2Fp-reduce" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/sindresorhus/p-reduce" ref="nofollow noopener noreferrer">p-reduce</a>、<a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fsindresorhus%2Fp-map" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/sindresorhus/p-map" ref="nofollow noopener noreferrer">p-map</a> 和 <a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fsindresorhus%2Fp-filter" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/sindresorhus/p-filter" ref="nofollow noopener noreferrer">p-filter</a> 3 个模块。下面我们来继续介绍另一个模块 —— <a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fsindresorhus%2Fp-waterfall" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/sindresorhus/p-waterfall" ref="nofollow noopener noreferrer">p-waterfall</a>。</p>
<h3 data-id="heading-13"><a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fsindresorhus%2Fp-waterfall" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/sindresorhus/p-waterfall" ref="nofollow noopener noreferrer">p-waterfall</a></h3>
<blockquote>
<p>Run promise-returning & async functions in series, each passing its result to the next</p>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fsindresorhus%2Fp-waterfall" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/sindresorhus/p-waterfall" ref="nofollow noopener noreferrer">github.com/sindresorhu…</a></p>
</blockquote>
<h4 data-id="heading-14">使用说明</h4>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fsindresorhus%2Fp-waterfall" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/sindresorhus/p-waterfall" ref="nofollow noopener noreferrer">p-waterfall</a> 适用于串行执行 <strong>promise-returning</strong> 或 <strong>async</strong> 函数，并把前一个函数的返回结果自动传给下一个函数的场景。该模块默认导出了一个 <strong>pWaterfall</strong> 函数，该函数的签名如下：</p>
<blockquote>
<p><strong><a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fsindresorhus%2Fp-waterfall" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/sindresorhus/p-waterfall" ref="nofollow noopener noreferrer">pWaterfall(tasks, initialValue): Promise</a></strong></p>
</blockquote>
<ul>
<li><code>tasks: Iterable<Function></code></li>
<li><code>initialValue: unknown</code>：将作为第一个任务的 <code>previousValue</code></li>
</ul>
<p>了解完 <strong>pWaterfall</strong> 函数的签名之后，我们来看一下该函数如何使用。</p>
<h4 data-id="heading-15">使用示例</h4>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">// p-waterfall/p-waterfall.test.js</span>
<span class="hljs-keyword">import</span> pWaterfall <span class="hljs-keyword">from</span> <span class="hljs-string">"p-waterfall"</span>;

<span class="hljs-keyword">const</span> tasks = [
  <span class="hljs-keyword">async</span> (val) => val + <span class="hljs-number">1</span>,
  <span class="hljs-function">(<span class="hljs-params">val</span>) =></span> val + <span class="hljs-number">2</span>,
  <span class="hljs-keyword">async</span> (val) => val + <span class="hljs-number">3</span>,
];

<span class="hljs-keyword">async</span> <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">main</span>(<span class="hljs-params"></span>) </span>&#123;
  <span class="hljs-keyword">const</span> result = <span class="hljs-keyword">await</span> pWaterfall(tasks, <span class="hljs-number">0</span>);
  <span class="hljs-built_in">console</span>.dir(result); <span class="hljs-comment">// 输出结果：6</span>
&#125;

main();
<span class="copy-code-btn">复制代码</span></code></pre>
<p>在以上示例中，我们创建了 3 个任务，然后使用 <code>pWaterfall</code> 函数来执行这 3 个任务。当以上代码成功执行后，命令行会输出 <strong>6</strong>。对应的执行流程如下图所示：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/23640c8512e346df8b2325b0df11df6e~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<h4 data-id="heading-16">源码分析</h4>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">// https://github.com/sindresorhus/p-waterfall/blob/main/index.js</span>
<span class="hljs-keyword">import</span> pReduce <span class="hljs-keyword">from</span> <span class="hljs-string">'p-reduce'</span>;

<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> <span class="hljs-keyword">async</span> <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">pWaterfall</span>(<span class="hljs-params">iterable, initialValue</span>) </span>&#123;
<span class="hljs-keyword">return</span> pReduce(iterable, <span class="hljs-function">(<span class="hljs-params">previousValue, function_</span>) =></span> function_(previousValue), initialValue);
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>在 <code>pWaterfall</code> 函数内部，会利用前面已经介绍的 <code>pReduce</code> 函数来实现 <strong>waterfall</strong> 流程控制。同样，要搞清楚内部的控制流程，我们需要来回顾一下 <code>pReduce</code> 函数的具体实现：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> <span class="hljs-keyword">async</span> <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">pReduce</span>(<span class="hljs-params">iterable, reducer, initialValue</span>) </span>&#123;
  <span class="hljs-keyword">return</span> <span class="hljs-keyword">new</span> <span class="hljs-built_in">Promise</span>(<span class="hljs-function">(<span class="hljs-params">resolve, reject</span>) =></span> &#123;
    <span class="hljs-keyword">const</span> iterator = iterable[<span class="hljs-built_in">Symbol</span>.iterator](); <span class="hljs-comment">// 获取迭代器</span>
    <span class="hljs-keyword">let</span> index = <span class="hljs-number">0</span>; <span class="hljs-comment">// 索引值</span>

    <span class="hljs-keyword">const</span> next = <span class="hljs-keyword">async</span> (total) => &#123;
      <span class="hljs-keyword">const</span> element = iterator.next(); <span class="hljs-comment">// 获取下一项</span>

      <span class="hljs-keyword">if</span> (element.done) &#123;
        <span class="hljs-comment">// 判断迭代器是否迭代完成</span>
        resolve(total);
        <span class="hljs-keyword">return</span>;
      &#125;

      <span class="hljs-keyword">try</span> &#123;
        <span class="hljs-comment">// 首次调用next函数的状态：</span>
        <span class="hljs-comment">// resolvedTotal => 0</span>
        <span class="hljs-comment">// element.value => async (val) => val + 1</span>
        <span class="hljs-keyword">const</span> [resolvedTotal, resolvedValue] = <span class="hljs-keyword">await</span> <span class="hljs-built_in">Promise</span>.all([
          total,
          element.value,
        ]);
        <span class="hljs-comment">// reducer => (previousValue, function_) => function_(previousValue)</span>
        next(reducer(resolvedTotal, resolvedValue, index++));
      &#125; <span class="hljs-keyword">catch</span> (error) &#123;
        reject(error);
      &#125;
    &#125;;

    <span class="hljs-comment">// 使用初始值，开始迭代</span>
    next(initialValue);
  &#125;);
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>现在我们已经知道 <strong>pWaterfall</strong> 函数会把前一个任务的输出结果，作为输入传给下一个任务。但有些时候，在串行执行每个任务时，我们并不关心每个任务的返回值。针对这种场合，我们可以考虑使用 <a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fsindresorhus%2Fp-series" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/sindresorhus/p-series" ref="nofollow noopener noreferrer">p-series</a> 模块提供的 <code>pSeries</code> 函数。</p>
<h3 data-id="heading-17"><a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fsindresorhus%2Fp-series" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/sindresorhus/p-series" ref="nofollow noopener noreferrer">p-series</a></h3>
<blockquote>
<p>Run promise-returning & async functions in series</p>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fsindresorhus%2Fp-series" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/sindresorhus/p-series" ref="nofollow noopener noreferrer">github.com/sindresorhu…</a></p>
</blockquote>
<h4 data-id="heading-18">使用说明</h4>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fsindresorhus%2Fp-series" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/sindresorhus/p-series" ref="nofollow noopener noreferrer">p-series</a> 适用于串行执行 <strong>promise-returning</strong> 或 <strong>async</strong> 函数的场景。</p>
<h4 data-id="heading-19">使用示例</h4>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">// p-series/p-series.test.js</span>
<span class="hljs-keyword">import</span> pSeries <span class="hljs-keyword">from</span> <span class="hljs-string">"p-series"</span>;

<span class="hljs-keyword">const</span> tasks = [<span class="hljs-keyword">async</span> () => <span class="hljs-number">1</span> + <span class="hljs-number">1</span>, <span class="hljs-function">() =></span> <span class="hljs-number">2</span> + <span class="hljs-number">2</span>, <span class="hljs-keyword">async</span> () => <span class="hljs-number">3</span> + <span class="hljs-number">3</span>];

<span class="hljs-keyword">async</span> <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">main</span>(<span class="hljs-params"></span>) </span>&#123;
  <span class="hljs-keyword">const</span> result = <span class="hljs-keyword">await</span> pSeries(tasks);
  <span class="hljs-built_in">console</span>.dir(result); <span class="hljs-comment">// 输出结果：[2, 4, 6]</span>
&#125;

main();
<span class="copy-code-btn">复制代码</span></code></pre>
<p>在以上示例中，我们创建了 3 个任务，然后使用 <code>pSeries</code> 函数来执行这 3 个任务。当以上代码成功执行后，命令行会输出 <strong>[ 2, 4, 6 ]</strong>。对应的执行流程如下图所示：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/eba0f1a8c2fb47d4a0f01536197ff7a1~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<h4 data-id="heading-20">源码分析</h4>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">// https://github.com/sindresorhus/p-series/blob/main/index.js</span>
<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> <span class="hljs-keyword">async</span> <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">pSeries</span>(<span class="hljs-params">tasks</span>) </span>&#123;
<span class="hljs-keyword">for</span> (<span class="hljs-keyword">const</span> task <span class="hljs-keyword">of</span> tasks) &#123;
<span class="hljs-keyword">if</span> (<span class="hljs-keyword">typeof</span> task !== <span class="hljs-string">'function'</span>) &#123;
<span class="hljs-keyword">throw</span> <span class="hljs-keyword">new</span> <span class="hljs-built_in">TypeError</span>(<span class="hljs-string">`Expected task to be a \`Function\`, received \`<span class="hljs-subst">$&#123;<span class="hljs-keyword">typeof</span> task&#125;</span>\``</span>);
&#125;
&#125;

<span class="hljs-keyword">const</span> results = [];

<span class="hljs-keyword">for</span> (<span class="hljs-keyword">const</span> task <span class="hljs-keyword">of</span> tasks) &#123;
results.push(<span class="hljs-keyword">await</span> task()); <span class="hljs-comment">// eslint-disable-line no-await-in-loop</span>
&#125;

<span class="hljs-keyword">return</span> results;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>由以上代码可知，在 <code>pSeries</code> 函数内部是利用 <strong><a href="https://link.juejin.cn/?target=https%3A%2F%2Fdeveloper.mozilla.org%2Fzh-CN%2Fdocs%2FWeb%2FJavaScript%2FReference%2FStatements%2Ffor...of" target="_blank" rel="nofollow noopener noreferrer" title="https://developer.mozilla.org/zh-CN/docs/Web/JavaScript/Reference/Statements/for...of" ref="nofollow noopener noreferrer">for...of</a></strong> 语句和 <strong><a href="https://link.juejin.cn/?target=https%3A%2F%2Fdeveloper.mozilla.org%2Fzh-CN%2Fdocs%2FLearn%2FJavaScript%2FAsynchronous%2FAsync_await" target="_blank" rel="nofollow noopener noreferrer" title="https://developer.mozilla.org/zh-CN/docs/Learn/JavaScript/Asynchronous/Async_await" ref="nofollow noopener noreferrer">async/await</a></strong> 特性来实现串行任务流控制。因此在实际的项目中，你也可以无需使用该模块，就可以轻松的实现串行任务流控制。</p>
<h3 data-id="heading-21"><a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fsindresorhus%2Fp-all" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/sindresorhus/p-all" ref="nofollow noopener noreferrer">p-all</a></h3>
<blockquote>
<p>Run promise-returning & async functions concurrently with optional limited concurrency</p>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fsindresorhus%2Fp-all" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/sindresorhus/p-all" ref="nofollow noopener noreferrer">github.com/sindresorhu…</a></p>
</blockquote>
<h4 data-id="heading-22">使用说明</h4>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fsindresorhus%2Fp-all" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/sindresorhus/p-all" ref="nofollow noopener noreferrer">p-all</a> 适用于并发执行 <strong>promise-returning</strong> 或 <strong>async</strong> 函数的场景。该模块提供的功能，与 <a href="https://link.juejin.cn/?target=https%3A%2F%2Fdeveloper.mozilla.org%2Fzh-CN%2Fdocs%2FWeb%2FJavaScript%2FReference%2FGlobal_Objects%2FPromise%2Fall" target="_blank" rel="nofollow noopener noreferrer" title="https://developer.mozilla.org/zh-CN/docs/Web/JavaScript/Reference/Global_Objects/Promise/all" ref="nofollow noopener noreferrer"><strong>Promise.all</strong></a> API 类似，主要的区别是该模块允许你限制任务的并发数。在日常开发过程中，一个比较常见的场景就是控制 HTTP 请求的并发数，这时你也可以考虑使用 <a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Frxaviers%2Fasync-pool" target="_blank" title="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Frxaviers%2Fasync-pool">async-pool</a> 这个库来解决并发控制的问题，如果你对该库的内部实现原理感兴趣的话，可以阅读 <a href="https://juejin.cn/post/6976028030770610213" target="_blank" title="https://juejin.cn/post/6976028030770610213">JavaScript 中如何实现并发控制？</a> 这篇文章。</p>
<p>下面我们来继续介绍 <a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fsindresorhus%2Fp-all" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/sindresorhus/p-all" ref="nofollow noopener noreferrer">p-all</a> 模块，该模块默认导出了一个 <strong>pAll</strong> 函数，该函数的签名如下：</p>
<blockquote>
<p><strong><a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fsindresorhus%2Fp-all" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/sindresorhus/p-all" ref="nofollow noopener noreferrer">pAll(tasks, options)</a></strong></p>
</blockquote>
<ul>
<li><code>tasks: Iterable<Function></code></li>
<li><code>options: object</code>
<ul>
<li><code>concurrency: number</code> —— 并发数，默认值 <code>Infinity</code>，最小值为 <code>1</code>；</li>
<li><code>stopOnError: boolean</code> —— 出现异常时，是否终止，默认值为 <code>true</code>。</li>
</ul>
</li>
</ul>
<h4 data-id="heading-23">使用示例</h4>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">// p-all/p-all.test.js</span>
<span class="hljs-keyword">import</span> delay <span class="hljs-keyword">from</span> <span class="hljs-string">"delay"</span>;
<span class="hljs-keyword">import</span> pAll <span class="hljs-keyword">from</span> <span class="hljs-string">"p-all"</span>;

<span class="hljs-keyword">const</span> inputs = [
  <span class="hljs-function">() =></span> delay(<span class="hljs-number">200</span>, &#123; <span class="hljs-attr">value</span>: <span class="hljs-number">1</span> &#125;),
  <span class="hljs-keyword">async</span> () => &#123;
    <span class="hljs-keyword">await</span> delay(<span class="hljs-number">100</span>);
    <span class="hljs-keyword">return</span> <span class="hljs-number">2</span>;
  &#125;,
  <span class="hljs-keyword">async</span> () => <span class="hljs-number">8</span>,
];

<span class="hljs-keyword">async</span> <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">main</span>(<span class="hljs-params"></span>) </span>&#123;
  <span class="hljs-built_in">console</span>.time(<span class="hljs-string">"start"</span>);
  <span class="hljs-keyword">const</span> result = <span class="hljs-keyword">await</span> pAll(inputs, &#123; <span class="hljs-attr">concurrency</span>: <span class="hljs-number">1</span> &#125;);
  <span class="hljs-built_in">console</span>.dir(result); <span class="hljs-comment">// 输出结果：[ 1, 2, 8 ]</span>
  <span class="hljs-built_in">console</span>.timeEnd(<span class="hljs-string">"start"</span>);
&#125;

main();
<span class="copy-code-btn">复制代码</span></code></pre>
<p>在以上示例中，我们创建了 3 个异步任务，然后通过 <code>pAll</code> 函数来执行已创建的任务。当成功执行以上代码后，命令行会输出以下信息：</p>
<pre><code class="hljs language-shell copyable" lang="shell">[ 1, 2, 8 ]
start: 312.561ms
<span class="copy-code-btn">复制代码</span></code></pre>
<p>而当把 <code>concurrency</code> 属性的值更改为 <code>2</code> 之后，再次执行以上代码。那么命令行将会输出以下信息：</p>
<pre><code class="hljs language-shell copyable" lang="shell">[ 1, 2, 8 ]
start: 209.469ms
<span class="copy-code-btn">复制代码</span></code></pre>
<p>可以看出并发数为 <code>1</code> 时，程序的运行时间大于 300ms。而如果并发数为 <code>2</code> 时，前面两个任务是并行的，所以程序的运行时间只需 200 多毫秒。</p>
<h4 data-id="heading-24">源码分析</h4>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">// https://github.com/sindresorhus/p-all/blob/main/index.js</span>
<span class="hljs-keyword">import</span> pMap <span class="hljs-keyword">from</span> <span class="hljs-string">'p-map'</span>;

<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> <span class="hljs-keyword">async</span> <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">pAll</span>(<span class="hljs-params">iterable, options</span>) </span>&#123;
<span class="hljs-keyword">return</span> pMap(iterable, <span class="hljs-function"><span class="hljs-params">element</span> =></span> element(), options);
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>很明显在 <code>pAll</code> 函数内部，是通过 <a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fsindresorhus%2Fp-map" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/sindresorhus/p-map" ref="nofollow noopener noreferrer">p-map</a> 模块提供的 <code>pMap</code> 函数来实现并发控制的。如果你对 <code>pMap</code> 函数的内部实现方式，还不清楚的话，可以回过头再次阅读 <a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fsindresorhus%2Fp-map" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/sindresorhus/p-map" ref="nofollow noopener noreferrer">p-map</a> 模块的相关内容。接下来，我们来继续介绍另一个模块 —— <a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fsindresorhus%2Fp-race" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/sindresorhus/p-race" ref="nofollow noopener noreferrer">p-race</a>。</p>
<h3 data-id="heading-25"><a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fsindresorhus%2Fp-race" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/sindresorhus/p-race" ref="nofollow noopener noreferrer">p-race</a></h3>
<blockquote>
<p>A better <code>Promise.race()</code></p>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fsindresorhus%2Fp-race" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/sindresorhus/p-race" ref="nofollow noopener noreferrer">github.com/sindresorhu…</a></p>
</blockquote>
<h4 data-id="heading-26">使用说明</h4>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fsindresorhus%2Fp-race" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/sindresorhus/p-race" ref="nofollow noopener noreferrer">p-race</a> 这个模块修复了 <a href="https://link.juejin.cn/?target=https%3A%2F%2Fdeveloper.mozilla.org%2Fzh-CN%2Fdocs%2FWeb%2FJavaScript%2FReference%2FGlobal_Objects%2FPromise%2Frace" target="_blank" rel="nofollow noopener noreferrer" title="https://developer.mozilla.org/zh-CN/docs/Web/JavaScript/Reference/Global_Objects/Promise/race" ref="nofollow noopener noreferrer">Promise.race</a> API 一个 “愚蠢” 的行为。当使用空的可迭代对象，调用 <a href="https://link.juejin.cn/?target=https%3A%2F%2Fdeveloper.mozilla.org%2Fzh-CN%2Fdocs%2FWeb%2FJavaScript%2FReference%2FGlobal_Objects%2FPromise%2Frace" target="_blank" rel="nofollow noopener noreferrer" title="https://developer.mozilla.org/zh-CN/docs/Web/JavaScript/Reference/Global_Objects/Promise/race" ref="nofollow noopener noreferrer">Promise.race</a> API 时，将会返回一个永远处于 <strong>pending</strong> 状态的 Promise 对象，这可能会产生一些非常难以调试的问题。而如果往 <a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fsindresorhus%2Fp-race" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/sindresorhus/p-race" ref="nofollow noopener noreferrer">p-race</a> 模块提供的 <code>pRace</code> 函数中传入一个空的可迭代对象时，该函数将会立即抛出 <strong>RangeError: Expected the iterable to contain at least one item</strong> 的异常信息。</p>
<p><strong><code>pRace(iterable)</code></strong> 方法会返回一个 promise 对象，一旦迭代器中的某个 promise 对象 <strong>resolved</strong> 或 <strong>rejected</strong>，返回的 promise 对象就会 resolve 或 reject 相应的值。</p>
<h4 data-id="heading-27">使用示例</h4>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">// p-race/p-race.test.js</span>
<span class="hljs-keyword">import</span> delay <span class="hljs-keyword">from</span> <span class="hljs-string">"delay"</span>;
<span class="hljs-keyword">import</span> pRace <span class="hljs-keyword">from</span> <span class="hljs-string">"p-race"</span>;

<span class="hljs-keyword">const</span> inputs = [delay(<span class="hljs-number">50</span>, &#123; <span class="hljs-attr">value</span>: <span class="hljs-number">1</span> &#125;), delay(<span class="hljs-number">100</span>, &#123; <span class="hljs-attr">value</span>: <span class="hljs-number">2</span> &#125;)];

<span class="hljs-keyword">async</span> <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">main</span>(<span class="hljs-params"></span>) </span>&#123;
  <span class="hljs-keyword">const</span> result = <span class="hljs-keyword">await</span> pRace(inputs);
  <span class="hljs-built_in">console</span>.dir(result); <span class="hljs-comment">// 输出结果：1</span>
&#125;

main();
<span class="copy-code-btn">复制代码</span></code></pre>
<p>在以上示例中，我们导入了 <strong><a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fsindresorhus%2Fdelay" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/sindresorhus/delay" ref="nofollow noopener noreferrer">delay</a></strong> 模块默认导出的 <code>delay</code> 方法，该方法可用于按照给定的时间，延迟一个 Promise 对象。利用 <code>delay</code> 函数，我们创建了 2 个 Promise 对象，然后使用 <code>pRace</code> 函数来处理这两个 Promise 对象。以上代码成功运行后，命令行始终会输出 <strong>1</strong>。那么为什么会这样呢？下面我们来分析一下 <code>pRace</code> 函数的源码。</p>
<h4 data-id="heading-28">源码分析</h4>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">// https://github.com/sindresorhus/p-race/blob/main/index.js</span>
<span class="hljs-keyword">import</span> isEmptyIterable <span class="hljs-keyword">from</span> <span class="hljs-string">'is-empty-iterable'</span>;

<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> <span class="hljs-keyword">async</span> <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">pRace</span>(<span class="hljs-params">iterable</span>) </span>&#123;
<span class="hljs-keyword">if</span> (isEmptyIterable(iterable)) &#123;
<span class="hljs-keyword">throw</span> <span class="hljs-keyword">new</span> <span class="hljs-built_in">RangeError</span>(<span class="hljs-string">'Expected the iterable to contain at least one item'</span>);
&#125;

<span class="hljs-keyword">return</span> <span class="hljs-built_in">Promise</span>.race(iterable);
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>观察以上源码可知，在 <code>pRace</code> 函数内部会先判断传入的 <code>iterable</code> 参数是否为空的可迭代对象。检测参数是否为空的可迭代对象，是通过 <code>isEmptyIterable</code> 函数来实现，该函数的具体代码如下所示：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">// https://github.com/sindresorhus/is-empty-iterable/blob/main/index.js</span>
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">isEmptyIterable</span>(<span class="hljs-params">iterable</span>) </span>&#123;
<span class="hljs-keyword">for</span> (<span class="hljs-keyword">const</span> _ <span class="hljs-keyword">of</span> iterable) &#123;
<span class="hljs-keyword">return</span> <span class="hljs-literal">false</span>;
&#125;

<span class="hljs-keyword">return</span> <span class="hljs-literal">true</span>;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>当发现是空的可迭代对象时，<code>pRace</code> 函数会直接抛出 <code>RangeError</code> 异常。否则，会利用 <code>Promise.race</code> API 来实现具体的功能。需要注意的是，<a href="https://link.juejin.cn/?target=https%3A%2F%2Fdeveloper.mozilla.org%2Fzh-CN%2Fdocs%2FWeb%2FJavaScript%2FReference%2FGlobal_Objects%2FPromise%2Frace" target="_blank" rel="nofollow noopener noreferrer" title="https://developer.mozilla.org/zh-CN/docs/Web/JavaScript/Reference/Global_Objects/Promise/race" ref="nofollow noopener noreferrer"><strong>Promise.race</strong></a> 方法也存在兼容性问题，具体如下图所示：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/431968918a034a2c8597bc8bfcb48a46~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>（图片来源 —— <a href="https://link.juejin.cn/?target=https%3A%2F%2Fcaniuse.com%2F%3Fsearch%3DPromise.race%25EF%25BC%2589" target="_blank" rel="nofollow noopener noreferrer" title="https://caniuse.com/?search=Promise.race%EF%BC%89" ref="nofollow noopener noreferrer">caniuse.com/?search=Pro…</a></p>
<p>同样，可能有一些小伙伴对 <a href="https://link.juejin.cn/?target=https%3A%2F%2Fdeveloper.mozilla.org%2Fzh-CN%2Fdocs%2FWeb%2FJavaScript%2FReference%2FGlobal_Objects%2FPromise%2Frace" target="_blank" rel="nofollow noopener noreferrer" title="https://developer.mozilla.org/zh-CN/docs/Web/JavaScript/Reference/Global_Objects/Promise/race" ref="nofollow noopener noreferrer"><strong>Promise.race</strong></a> 还不熟悉，它也是一道挺高频的手写题。所以，接下来我们来手写一个简易版的 <a href="https://link.juejin.cn/?target=https%3A%2F%2Fdeveloper.mozilla.org%2Fzh-CN%2Fdocs%2FWeb%2FJavaScript%2FReference%2FGlobal_Objects%2FPromise%2Frace" target="_blank" rel="nofollow noopener noreferrer" title="https://developer.mozilla.org/zh-CN/docs/Web/JavaScript/Reference/Global_Objects/Promise/race" ref="nofollow noopener noreferrer"><strong>Promise.race</strong></a>：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-built_in">Promise</span>.race = <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params">iterators</span>) </span>&#123;
  <span class="hljs-keyword">return</span> <span class="hljs-keyword">new</span> <span class="hljs-built_in">Promise</span>(<span class="hljs-function">(<span class="hljs-params">resolve, reject</span>) =></span> &#123;
    <span class="hljs-keyword">for</span> (<span class="hljs-keyword">const</span> iter <span class="hljs-keyword">of</span> iterators) &#123;
      <span class="hljs-built_in">Promise</span>.resolve(iter)
        .then(<span class="hljs-function">(<span class="hljs-params">res</span>) =></span> &#123;
          resolve(res);
        &#125;)
        .catch(<span class="hljs-function">(<span class="hljs-params">e</span>) =></span> &#123;
          reject(e);
        &#125;);
    &#125;
  &#125;);
&#125;;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-29"><a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fsindresorhus%2Fp-forever" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/sindresorhus/p-forever" ref="nofollow noopener noreferrer">p-forever</a></h3>
<blockquote>
<p>Run promise-returning & async functions repeatedly until you end it</p>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fsindresorhus%2Fp-forever" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/sindresorhus/p-forever" ref="nofollow noopener noreferrer">github.com/sindresorhu…</a></p>
</blockquote>
<h4 data-id="heading-30">使用说明</h4>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fsindresorhus%2Fp-forever" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/sindresorhus/p-forever" ref="nofollow noopener noreferrer">p-forever</a> 适用于需要重复不断执行 <strong>promise-returning</strong> 或 <strong>async</strong> 函数，直到用户终止的场景。该模块默认导出了一个 <strong>pForever</strong> 函数，该函数的签名如下：</p>
<blockquote>
<p><strong><a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fsindresorhus%2Fp-forever" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/sindresorhus/p-forever" ref="nofollow noopener noreferrer">pForever(fn, initialValue)</a></strong></p>
</blockquote>
<ul>
<li><code>fn: Function</code>：重复执行的函数；</li>
<li><code>initialValue</code>：传递给 <code>fn</code> 函数的初始值。</li>
</ul>
<p>了解完 <strong>pForever</strong> 函数的签名之后，我们来看一下该函数如何使用。</p>
<h4 data-id="heading-31">使用示例</h4>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">// p-forever/p-forever.test.js</span>
<span class="hljs-keyword">import</span> delay <span class="hljs-keyword">from</span> <span class="hljs-string">"delay"</span>;
<span class="hljs-keyword">import</span> pForever <span class="hljs-keyword">from</span> <span class="hljs-string">"p-forever"</span>;

<span class="hljs-keyword">async</span> <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">main</span>(<span class="hljs-params"></span>) </span>&#123;
  <span class="hljs-keyword">let</span> index = <span class="hljs-number">0</span>;
  <span class="hljs-keyword">await</span> pForever(<span class="hljs-keyword">async</span> () => (++index === <span class="hljs-number">10</span> ? pForever.end : delay(<span class="hljs-number">50</span>)));
  <span class="hljs-built_in">console</span>.log(<span class="hljs-string">"当前index的值: "</span>, index); <span class="hljs-comment">// 输出结果：当前index的值: 10</span>
&#125;

main();
<span class="copy-code-btn">复制代码</span></code></pre>
<p>在以上示例中，传入 <code>pForever</code> 函数的 <code>fn</code> 函数会一直重复执行，直到该 <code>fn</code> 函数返回 <code>pForever.end</code> 的值，才会终止执行。因此以上代码成功执行后，命令行的输出结果是：<strong>当前index的值:  10</strong>。</p>
<h4 data-id="heading-32">源码分析</h4>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">// https://github.com/sindresorhus/p-forever/blob/main/index.js</span>
<span class="hljs-keyword">const</span> endSymbol = <span class="hljs-built_in">Symbol</span>(<span class="hljs-string">'pForever.end'</span>);

<span class="hljs-keyword">const</span> pForever = <span class="hljs-keyword">async</span> (function_, previousValue) => &#123;
<span class="hljs-keyword">const</span> newValue = <span class="hljs-keyword">await</span> function_(<span class="hljs-keyword">await</span> previousValue);
<span class="hljs-keyword">if</span> (newValue === endSymbol) &#123;
<span class="hljs-keyword">return</span>;
&#125;
<span class="hljs-keyword">return</span> pForever(function_, newValue);
&#125;;

pForever.end = endSymbol;
<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> pForever;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>由以上源码可知，<code>pForever</code> 函数的内部实现并不复杂。当判断 <code>newValue</code> 的值为 <code>endSymbol</code> 时，就直接返回了。否则，就会继续调用 <code>pForever</code> 函数。除了一直重复执行任务之外，有时候我们会希望显式指定任务的执行次数，针对这种场景，我们就可以使用 <a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fsindresorhus%2Fp-times" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/sindresorhus/p-times" ref="nofollow noopener noreferrer">p-times</a> 模块。</p>
<h3 data-id="heading-33"><a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fsindresorhus%2Fp-times" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/sindresorhus/p-times" ref="nofollow noopener noreferrer">p-times</a></h3>
<blockquote>
<p>Run promise-returning & async functions a specific number of times concurrently</p>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fsindresorhus%2Fp-times" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/sindresorhus/p-times" ref="nofollow noopener noreferrer">github.com/sindresorhu…</a></p>
</blockquote>
<h4 data-id="heading-34">使用说明</h4>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fsindresorhus%2Fp-times" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/sindresorhus/p-times" ref="nofollow noopener noreferrer">p-times</a> 适用于显式指定 <strong>promise-returning</strong> 或 <strong>async</strong> 函数执行次数的场景。该模块默认导出了一个 <strong>pTimes</strong> 函数，该函数的签名如下：</p>
<blockquote>
<p><strong><a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fsindresorhus%2Fp-times" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/sindresorhus/p-times" ref="nofollow noopener noreferrer">pTimes(count, mapper, options): Promise</a></strong></p>
</blockquote>
<ul>
<li><code>count: number</code>：调用次数；</li>
<li><code>mapper(index): Function</code>：mapper 函数，调用该函数后会返回 Promise 对象或某个具体的值；</li>
<li><code>options: object</code>
<ul>
<li><code>concurrency: number</code> —— 并发数，默认值 <code>Infinity</code>，最小值为 <code>1</code>；</li>
<li><code>stopOnError: boolean</code> —— 出现异常时，是否终止，默认值为 <code>true</code>。</li>
</ul>
</li>
</ul>
<p>了解完 <strong>pTimes</strong> 函数的签名之后，我们来看一下该函数如何使用。</p>
<h4 data-id="heading-35">使用示例</h4>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">// p-times/p-times.test.js</span>
<span class="hljs-keyword">import</span> delay <span class="hljs-keyword">from</span> <span class="hljs-string">"delay"</span>;
<span class="hljs-keyword">import</span> pTimes <span class="hljs-keyword">from</span> <span class="hljs-string">"p-times"</span>;

<span class="hljs-keyword">async</span> <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">main</span>(<span class="hljs-params"></span>) </span>&#123;
  <span class="hljs-built_in">console</span>.time(<span class="hljs-string">"start"</span>);
  <span class="hljs-keyword">const</span> result = <span class="hljs-keyword">await</span> pTimes(<span class="hljs-number">5</span>, <span class="hljs-keyword">async</span> (i) => delay(<span class="hljs-number">50</span>, &#123; <span class="hljs-attr">value</span>: i * <span class="hljs-number">10</span> &#125;), &#123;
    <span class="hljs-attr">concurrency</span>: <span class="hljs-number">3</span>,
  &#125;);
  <span class="hljs-built_in">console</span>.dir(result);
  <span class="hljs-built_in">console</span>.timeEnd(<span class="hljs-string">"start"</span>);
&#125;

main();
<span class="copy-code-btn">复制代码</span></code></pre>
<p>在以上示例中，我们通过 <code>pTimes</code> 函数配置 <strong>mapper</strong> 函数的执行次数为 <strong>5</strong> 次，同时设置任务的并发数为 <strong>3</strong>。当以上代码成功运行后，命令行会输出以下结果：</p>
<pre><code class="hljs language-shell copyable" lang="shell">[ 0, 10, 20, 30, 40 ]
start: 116.090ms
<span class="copy-code-btn">复制代码</span></code></pre>
<p>对于以上示例，你可以通过改变 <code>concurrency</code> 的值，来对比输出的程序运行时间。那么 <code>pTimes</code> 函数内部是如何实现并发控制的呢？其实该函数内部也是利用 <code>pMap</code> 函数来实现并发控制。</p>
<h4 data-id="heading-36">源码分析</h4>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">// https://github.com/sindresorhus/p-times/blob/main/index.js</span>
<span class="hljs-keyword">import</span> pMap <span class="hljs-keyword">from</span> <span class="hljs-string">"p-map"</span>;

<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">pTimes</span>(<span class="hljs-params">count, mapper, options</span>) </span>&#123;
  <span class="hljs-keyword">return</span> pMap(
    <span class="hljs-built_in">Array</span>.from(&#123; <span class="hljs-attr">length</span>: count &#125;).fill(),
    <span class="hljs-function">(<span class="hljs-params">_, index</span>) =></span> mapper(index),
    options
  );
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>在 <code>pTimes</code> 函数中，会通过 <a href="https://link.juejin.cn/?target=https%3A%2F%2Fdeveloper.mozilla.org%2Fzh-CN%2Fdocs%2FWeb%2FJavaScript%2FReference%2FGlobal_Objects%2FArray%2Ffrom" target="_blank" rel="nofollow noopener noreferrer" title="https://developer.mozilla.org/zh-CN/docs/Web/JavaScript/Reference/Global_Objects/Array/from" ref="nofollow noopener noreferrer">Array.from</a> 方法创建指定长度的数组，然后通过 <code>fill</code> 方法进行填充。最后再把该数组、<code>mapper</code> 函数和 <code>options</code> 配置对象，作为输入参数调用 <code>pMap</code> 函数。写到这里，阿宝哥觉得 <code>pMap</code> 函数提供的功能还是蛮强大的，很多模块的内部都使用了 <code>pMap</code> 函数。</p>
<h3 data-id="heading-37"><a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fsindresorhus%2Fp-pipe" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/sindresorhus/p-pipe" ref="nofollow noopener noreferrer">p-pipe</a></h3>
<blockquote>
<p>Compose promise-returning & async functions into a reusable pipeline</p>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fsindresorhus%2Fp-pipe" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/sindresorhus/p-pipe" ref="nofollow noopener noreferrer">github.com/sindresorhu…</a></p>
</blockquote>
<h4 data-id="heading-38">使用说明</h4>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fsindresorhus%2Fp-pipe" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/sindresorhus/p-pipe" ref="nofollow noopener noreferrer">p-pipe</a> 适用于把 <strong>promise-returning</strong> 或 <strong>async</strong> 函数组合成可复用的管道。该模块默认导出了一个 <strong>pPipe</strong> 函数，该函数的签名如下：</p>
<blockquote>
<p><strong><a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fsindresorhus%2Fp-pipe" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/sindresorhus/p-pipe" ref="nofollow noopener noreferrer">pPipe(input...)</a></strong></p>
</blockquote>
<ul>
<li><code>input: Function</code>：期望调用后会返回 Promise 或任何值的函数。</li>
</ul>
<p>了解完 <strong>pPipe</strong> 函数的签名之后，我们来看一下该函数如何使用。</p>
<h4 data-id="heading-39">使用示例</h4>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">// p-pipe/p-pipe.test.js</span>
<span class="hljs-keyword">import</span> pPipe <span class="hljs-keyword">from</span> <span class="hljs-string">"p-pipe"</span>;

<span class="hljs-keyword">const</span> addUnicorn = <span class="hljs-keyword">async</span> (string) => <span class="hljs-string">`<span class="hljs-subst">$&#123;string&#125;</span> Unicorn`</span>;
<span class="hljs-keyword">const</span> addRainbow = <span class="hljs-keyword">async</span> (string) => <span class="hljs-string">`<span class="hljs-subst">$&#123;string&#125;</span> Rainbow`</span>;

<span class="hljs-keyword">const</span> pipeline = pPipe(addUnicorn, addRainbow);

(<span class="hljs-keyword">async</span> () => &#123;
  <span class="hljs-built_in">console</span>.log(<span class="hljs-keyword">await</span> pipeline(<span class="hljs-string">"❤️"</span>)); <span class="hljs-comment">// 输出结果：❤️ Unicorn Rainbow</span>
&#125;)();
<span class="copy-code-btn">复制代码</span></code></pre>
<p>在以上示例中，我们通过 <code>pPipe</code> 函数把 <code>addUnicorn</code> 和 <code>addRainbow</code> 这两个函数组合成一个新的可复用的管道。被组合函数的执行顺序是从左到右，所以以上代码成功运行后，命令行会输出 <strong>❤️ Unicorn Rainbow</strong>。</p>
<h4 data-id="heading-40">源码分析</h4>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">// https://github.com/sindresorhus/p-pipe/blob/main/index.js</span>
<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">pPipe</span>(<span class="hljs-params">...functions</span>) </span>&#123;
<span class="hljs-keyword">if</span> (functions.length === <span class="hljs-number">0</span>) &#123;
<span class="hljs-keyword">throw</span> <span class="hljs-keyword">new</span> <span class="hljs-built_in">Error</span>(<span class="hljs-string">'Expected at least one argument'</span>);
&#125;

<span class="hljs-keyword">return</span> <span class="hljs-keyword">async</span> input => &#123;
<span class="hljs-keyword">let</span> currentValue = input;

<span class="hljs-keyword">for</span> (<span class="hljs-keyword">const</span> function_ <span class="hljs-keyword">of</span> functions) &#123;
currentValue = <span class="hljs-keyword">await</span> function_(currentValue); <span class="hljs-comment">// eslint-disable-line no-await-in-loop</span>
&#125;
<span class="hljs-keyword">return</span> currentValue;
&#125;;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>由以上代码可知，在 <code>pPipe</code> 函数内部是利用 <strong><a href="https://link.juejin.cn/?target=https%3A%2F%2Fdeveloper.mozilla.org%2Fzh-CN%2Fdocs%2FWeb%2FJavaScript%2FReference%2FStatements%2Ffor...of" target="_blank" rel="nofollow noopener noreferrer" title="https://developer.mozilla.org/zh-CN/docs/Web/JavaScript/Reference/Statements/for...of" ref="nofollow noopener noreferrer">for...of</a></strong> 语句和 <strong><a href="https://link.juejin.cn/?target=https%3A%2F%2Fdeveloper.mozilla.org%2Fzh-CN%2Fdocs%2FLearn%2FJavaScript%2FAsynchronous%2FAsync_await" target="_blank" rel="nofollow noopener noreferrer" title="https://developer.mozilla.org/zh-CN/docs/Learn/JavaScript/Asynchronous/Async_await" ref="nofollow noopener noreferrer">async/await</a></strong> 特性来实现管道的功能。分析完 <a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fsindresorhus%2Fpromise-fun" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/sindresorhus/promise-fun" ref="nofollow noopener noreferrer">promise-fun</a> 项目中的 10 个模块之后，再次感受到 <strong><a href="https://link.juejin.cn/?target=https%3A%2F%2Fdeveloper.mozilla.org%2Fzh-CN%2Fdocs%2FLearn%2FJavaScript%2FAsynchronous%2FAsync_await" target="_blank" rel="nofollow noopener noreferrer" title="https://developer.mozilla.org/zh-CN/docs/Learn/JavaScript/Asynchronous/Async_await" ref="nofollow noopener noreferrer">async/await</a></strong> 特性给前端异步编程带来的巨大便利。其实对于异步的场景来说，除了可以使用 <a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fsindresorhus%2Fpromise-fun" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/sindresorhus/promise-fun" ref="nofollow noopener noreferrer">promise-fun</a> 项目中收录的模块之外，还可以使用 <a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fcaolan%2Fasync" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/caolan/async" ref="nofollow noopener noreferrer">async</a> 或 <a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fsuguru03%2Fneo-async" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/suguru03/neo-async" ref="nofollow noopener noreferrer">neo-async</a> 这两个异步处理模块提供的工具函数。在 Webpack 项目中，就用到了 <a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fsuguru03%2Fneo-async" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/suguru03/neo-async" ref="nofollow noopener noreferrer">neo-async</a> 这个模块，该模块的作者是希望用来替换 <a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fcaolan%2Fasync" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/caolan/async" ref="nofollow noopener noreferrer">async</a> 模块，以提供更好的性能。建议需要经常处理异步场景的小伙伴，抽空浏览一下 <a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fsuguru03%2Fneo-async" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/suguru03/neo-async" ref="nofollow noopener noreferrer">neo-async</a> 这个模块的 <strong><a href="https://link.juejin.cn/?target=http%3A%2F%2Fsuguru03.github.io%2Fneo-async%2Fdoc%2Findex.html" target="_blank" rel="nofollow noopener noreferrer" title="http://suguru03.github.io/neo-async/doc/index.html" ref="nofollow noopener noreferrer">官方文档</a></strong>。</p>
<h3 data-id="heading-41">总结</h3>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fsindresorhus%2Fpromise-fun" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/sindresorhus/promise-fun" ref="nofollow noopener noreferrer">promise-fun</a> 项目共收录了 <strong>50</strong> 个与 Promise 有关的模块，该项目的作者 <strong><a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fsindresorhus" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/sindresorhus" ref="nofollow noopener noreferrer">sindresorhus</a></strong> 个人就开发了 <strong>48</strong> 个模块，不愧是全职做开源的大牛。由于篇幅有限，阿宝哥只介绍了其中 <strong>10</strong> 个比较常用的模块。其实该项目还包含一些挺不错的模块，比如 <strong><a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fsindresorhus%2Fp-queue" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/sindresorhus/p-queue" ref="nofollow noopener noreferrer">p-queue</a></strong>、<strong><a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fsindresorhus%2Fp-any" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/sindresorhus/p-any" ref="nofollow noopener noreferrer">p-any</a></strong>、<strong><a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fsindresorhus%2Fp-some" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/sindresorhus/p-some" ref="nofollow noopener noreferrer">p-some</a></strong>、<strong><a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fsindresorhus%2Fp-debounce" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/sindresorhus/p-debounce" ref="nofollow noopener noreferrer">p-debounce</a></strong>、<strong><a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fsindresorhus%2Fp-throttle" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/sindresorhus/p-throttle" ref="nofollow noopener noreferrer">p-throttle</a></strong> 和 <strong><a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fsindresorhus%2Fp-timeout" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/sindresorhus/p-timeout" ref="nofollow noopener noreferrer">p-timeout</a></strong> 等。感兴趣的小伙伴，可以自行了解一下其他的模块。</p>
<h3 data-id="heading-42">参考资源</h3>
<ul>
<li><a href="https://link.juejin.cn/?target=https%3A%2F%2Fdeveloper.mozilla.org%2Fzh-CN%2Fdocs%2FWeb%2FJavaScript%2FReference%2FGlobal_Objects%2FArray%2FReduce" target="_blank" rel="nofollow noopener noreferrer" title="https://developer.mozilla.org/zh-CN/docs/Web/JavaScript/Reference/Global_Objects/Array/Reduce" ref="nofollow noopener noreferrer">MDN — Array.prototype.reduce()</a></li>
<li><a href="https://link.juejin.cn/?target=https%3A%2F%2Fdeveloper.mozilla.org%2Fzh-CN%2Fdocs%2FWeb%2FJavaScript%2FReference%2FGlobal_Objects%2FArray%2Ffrom" target="_blank" rel="nofollow noopener noreferrer" title="https://developer.mozilla.org/zh-CN/docs/Web/JavaScript/Reference/Global_Objects/Array/from" ref="nofollow noopener noreferrer">MDN — Array.from</a></li>
<li><a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fdomenic%2Fpromises-unwrapping%2Fissues%2F75" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/domenic/promises-unwrapping/issues/75" ref="nofollow noopener noreferrer">Promise.race with empty lists</a></li>
<li><a href="https://link.juejin.cn/?target=http%3A%2F%2Fsuguru03.github.io%2Fneo-async%2Fdoc%2Findex.html" target="_blank" rel="nofollow noopener noreferrer" title="http://suguru03.github.io/neo-async/doc/index.html" ref="nofollow noopener noreferrer">neo-async 官方文档</a></li>
</ul></div>  
</div>
            