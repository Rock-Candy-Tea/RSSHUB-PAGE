
---
title: 'TypeScript进阶, 如何避免 any'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/9ce7ac2843f94248bc51d5253974dc69~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Thu, 13 May 2021 19:38:52 GMT
thumbnail: 'https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/9ce7ac2843f94248bc51d5253974dc69~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h2 data-id="heading-0">为什么会出现 <code>any</code></h2>
<ul>
<li>不知道如何准确的定义出类型，<code>TS</code> 报错了，用 <code>any</code> 能解决，便用 <code>any</code> 了</li>
<li>觉得定义类型浪费时间，项目经理催的紧，工期紧张，<code>any</code> 更方便</li>
</ul>
<h2 data-id="heading-1">频繁使用 <code>any</code> 的弊端</h2>
<ul>
<li>不利于良好的编码习惯</li>
<li>不利于项目的后续维护</li>
<li>会出现很多本可避免的 <code>bug</code></li>
</ul>

<h2 data-id="heading-2">非必要不使用 <code>any</code> 的好处</h2>
<ul>
<li>良好的代码提示</li>
<li>强大的静态类型检查</li>
<li>可读性和可维护性</li>
</ul>
<p><strong>所以，我们要对 AnyScript 说不！</strong></p>
<h2 data-id="heading-3">TS 容易出现 <code>any</code> 的场景梳理</h2>
<h3 data-id="heading-4">给 window 全局对象增加属性</h3>
<p>常常能见到这样的写法</p>
<pre><code class="hljs language-typescript copyable" lang="typescript">;(<<span class="hljs-built_in">any</span>><span class="hljs-built_in">window</span>).obj = &#123;&#125;(
  <span class="hljs-comment">// 或</span>
  <span class="hljs-built_in">window</span> <span class="hljs-keyword">as</span> <span class="hljs-built_in">any</span>
).obj = &#123;&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这样做，在使用时和赋值时都需要断言一次，非常麻烦，并且使用时也不能得到代码提示</p>
<p>正确的做法应该是</p>
<ol>
<li>在项目全局的 <code>xxx.d.ts</code> 文件中配置如下代码</li>
</ol>
<pre><code class="hljs language-typescript copyable" lang="typescript"><span class="hljs-keyword">interface</span> Window &#123;
  <span class="hljs-attr">obj</span>: &#123;&#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<ol start="2">
<li>在需要给 <code>window</code> 赋值的文件目录下级新建一个 <code>@types</code> 文件夹，并在其中新建 <code>index.d.ts</code> 文件，添加如下代码</li>
</ol>
<pre><code class="hljs language-typescript copyable" lang="typescript"><span class="hljs-keyword">interface</span> Window &#123;
  <span class="hljs-attr">obj</span>: &#123;&#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>方法 2 也会在全局的 <code>window</code> 上增加 <code>obj</code> 这一声明，如果新增属性使用的跨度比较大，则推荐放在项目的 <code>index.d.ts</code> 中更利于维护，两种方式都在全局给 <code>window</code> 添加了属性，但方法 1 能一眼看出项目中 <code>window</code> 中添加了什么属性</p>
<h3 data-id="heading-5">正确使用可选链、非空断言</h3>
<p>错误的理解 <code>typescript</code> 的可选参数，而使用断言导致隐患</p>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-keyword">const</span> a: &#123;
  <span class="hljs-attr">b</span>: <span class="hljs-built_in">string</span>
  c?: &#123;
    <span class="hljs-attr">d</span>: <span class="hljs-built_in">string</span>
  &#125;
&#125; = &#123;
  <span class="hljs-attr">b</span>: <span class="hljs-string">"123"</span>,
&#125;

<span class="hljs-built_in">console</span>.log((<<span class="hljs-built_in">any</span>>a).c.d) <span class="hljs-comment">// 错误，这样访问会报错，应使用可选链</span>
<span class="hljs-built_in">console</span>.log(a.c!.d) <span class="hljs-comment">// 错误，ts 不会将错误抛出，但实际访问也会报错</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p><code>!</code> 非空断言与 <code>as</code> 有相似之处，主要用于断言某个属性的值不为 <code>null</code> 和 <code>undefined</code>，它不会影响最终的代码产物，只会影响代码编译过程中的类型校验</p>
<p><code>?.</code> <a href="https://developer.mozilla.org/zh-CN/docs/Web/JavaScript/Reference/Operators/Optional_chaining" target="_blank" rel="nofollow noopener noreferrer">可选链操作符</a> 会影响编译后的代码产物，如：</p>
<p>这段 ts 代码</p>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-keyword">const</span> a = &#123;
  <span class="hljs-attr">c</span>: <span class="hljs-literal">undefined</span>,
&#125;

<span class="hljs-keyword">const</span> b = a?.c?.d
<span class="copy-code-btn">复制代码</span></code></pre>
<p>会被编译为如下 js 代码（ <a href="https://www.babeljs.cn/repl" target="_blank" rel="nofollow noopener noreferrer">babel 在线编译网站</a> ）</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-meta">"use strict"</span>

<span class="hljs-keyword">var</span> _a$c

<span class="hljs-keyword">const</span> a = &#123;
  <span class="hljs-attr">c</span>: <span class="hljs-literal">undefined</span>,
&#125;
<span class="hljs-keyword">const</span> b =
  a === <span class="hljs-literal">null</span> || a === <span class="hljs-keyword">void</span> <span class="hljs-number">0</span>
    ? <span class="hljs-keyword">void</span> <span class="hljs-number">0</span>
    : (_a$c = a.c) === <span class="hljs-literal">null</span> || _a$c === <span class="hljs-keyword">void</span> <span class="hljs-number">0</span>
    ? <span class="hljs-keyword">void</span> <span class="hljs-number">0</span>
    : _a$c.d
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-6">将对象属性类型关联起来</h3>
<p>对象中有多个属性是联合类型，其中 <code>a</code> 属性和 <code>b</code> 属性是有关联的，<code>a</code> 为 <code>1</code> 时，<code>b</code> 为 <code>string</code>，<code>a</code> 为 <code>2</code> 时，<code>b</code> 为 <code>number</code>
我们通常是这样定义的</p>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-keyword">const</span> obj: &#123;
  <span class="hljs-attr">a</span>: <span class="hljs-number">1</span> | <span class="hljs-number">2</span>
  <span class="hljs-attr">b</span>: <span class="hljs-built_in">string</span> | <span class="hljs-built_in">number</span>
&#125; = &#123;
  <span class="hljs-attr">a</span>: <span class="hljs-number">1</span>,
  <span class="hljs-attr">b</span>: <span class="hljs-string">"1.2"</span>
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>那么使用时，会造成需要用断言来再次限定 <code>b</code> 的范围的情况，如下代码段所示</p>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-keyword">if</span> (obj.a === <span class="hljs-number">1</span>) &#123;
  <span class="hljs-keyword">const</span> [left, right] = (obj.b <span class="hljs-keyword">as</span> <span class="hljs-built_in">string</span>).split(<span class="hljs-string">"."</span>)
&#125;
<span class="hljs-comment">// 如果你偷懒，那可能又变成了这样的情况</span>
<span class="hljs-keyword">if</span> (obj.a === <span class="hljs-number">1</span>) &#123;
  <span class="hljs-keyword">const</span> [left, right] = (obj.b <span class="hljs-keyword">as</span> <span class="hljs-built_in">any</span>).split(<span class="hljs-string">"."</span>)
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>有没有什么办法能让我们不再 <code>as</code> 一次呢？有</p>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-keyword">const</span> obj: &#123;
  <span class="hljs-attr">a</span>: <span class="hljs-number">1</span>
  <span class="hljs-attr">b</span>: <span class="hljs-built_in">string</span>
&#125; | &#123;
  <span class="hljs-attr">a</span>: <span class="hljs-number">2</span>
  <span class="hljs-attr">b</span>: <span class="hljs-built_in">number</span>
&#125; = &#123;
  <span class="hljs-attr">a</span>: <span class="hljs-number">1</span>,
  <span class="hljs-attr">b</span>: <span class="hljs-string">"1.2"</span>
&#125;
<span class="hljs-comment">// 你会发现这样定义了以后，不需要再次进行断言限定 obj.b 的范围</span>
<span class="hljs-keyword">if</span> (obj.a === <span class="hljs-number">1</span>) &#123;
  <span class="hljs-keyword">const</span> [left, right] = obj.b.split(<span class="hljs-string">"."</span>) <span class="hljs-comment">// 校验通过</span>
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>如果我们把这样的方法应用到函数（也可以用重载实现）传参或组件传参，有意思的是它还能限定传参的范围，
函数组件实现：</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/9ce7ac2843f94248bc51d5253974dc69~tplv-k3u1fbpfcp-watermark.image" alt="function-components-params-1.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>错误的传参，<code>a</code> 与 <code>b</code> 的类型不匹配，校验不通过</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/3e13fe03be2547d3bc1d4357c9f0c29b~tplv-k3u1fbpfcp-watermark.image" alt="function-components-params-2.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>正确的传参，校验能通过</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/1ddfa0986d724c85bb7d2f42643d9d67~tplv-k3u1fbpfcp-watermark.image" alt="function-components-params-3.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>注意：你不能将 <code>props</code> 解构出来，会导致两者的关系丢失</p>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-keyword">const</span> &#123; a, b &#125; = props <span class="hljs-comment">// 错误，a 和 b 的类型关系丢失</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>是否使用联合类型需要辩证的看待，在任何时候都用上述方法定义可能会造成一些臃肿</p>
<h3 data-id="heading-7">巧用类型保护避免断言</h3>
<p>在 <code>typescript</code> 中，常用的类型保护为 <code>typeof</code> 、<code>instanceof</code>、和 <code>in</code> 关键字
掌握上述关键字较为容易，可通过文档了解
还有一个关键字 <code>is</code> （类型谓词）是 <code>typescript</code> 提供的，是另一种“类型保护”（这种说法助于理解）</p>
<p>类型谓词能让我们通过函数的形式做出复杂的类型检验的逻辑，一个使用类型谓词的函数的声明往往是如下形式：</p>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-keyword">type</span> X = xxxx <span class="hljs-comment">// 某种类型</span>
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">check</span>(<span class="hljs-params">params</span>): <span class="hljs-title">params</span> <span class="hljs-title">is</span> <span class="hljs-title">X</span>
</span><span class="copy-code-btn">复制代码</span></code></pre>
<p>理解起来就是如果 <code>check</code> 函数返回了真值，则参数 <code>params</code> 是 <code>X</code> 类型，否则不一定是 <code>X</code> 类型</p>
<p>设想一下如下场景，某个项目，既可能运行在微信网页中，也可能运行在其他 <code>webview</code> 中</p>
<p>在微信网页中，微信客户端向 window 对象中注入了各种 native 方法，使用它的方式就是 <code>window.wx.xxxx()</code></p>
<p>在其他 <code>webview</code> 中，我们假设也有这样的 native 方法，并且使用它的方式为 <code>window.webviewnative.xxxx()</code></p>
<p>在 typescript 项目中，<code>window</code> 对象上并不会默认存在 <code>wx</code> 和 <code>webviewnative</code> 两个属性，参考 <a href="https://juejin.cn/post/6961985123923263525#%E7%BB%99-window-%E5%85%A8%E5%B1%80%E5%AF%B9%E8%B1%A1%E5%A2%9E%E5%8A%A0%E5%B1%9E%E6%80%A7">给 window 全局对象增加属性</a>，我们能显示地为 <code>wx</code> 和 <code>webviewnative</code> 两个属性定义类型：</p>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-keyword">interface</span> Window &#123;
    wx?: &#123;
        <span class="hljs-attr">xxxx</span>: <span class="hljs-built_in">Function</span>
    &#125;
    webviewnative?: &#123;
        <span class="hljs-attr">xxxx</span>: <span class="hljs-built_in">Function</span>
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>如果你不会这样做，那可能又会写成断言为 <code>any</code> ：<code>(window as any).wx.xxxx()</code></p>
<p>可以看到在上面的代码段中两个属性都被我定义为了可选属性，目的是为了在后续维护（迭代）中，防止不做判断直接链式调用</p>
<p>在微信环境中 <code>window.wx</code> 一定存在，但 webviewnative 一定不存在，反之在其他的 <code>webview</code> 中，（见前文假设）<code>window.webviewnative</code> 一定存在</p>
<p>在接口 <code>interface</code> 中，我们并不能动态的知晓和定义到底哪个存在</p>
<p>你可以这样写</p>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-keyword">if</span> (<span class="hljs-keyword">typeof</span> <span class="hljs-built_in">window</span>.wx !== <span class="hljs-string">'undefined'</span>) &#123;
    <span class="hljs-built_in">window</span>.wx.xxxx()
&#125; <span class="hljs-keyword">else</span> &#123;
    <span class="hljs-comment">// not in wx</span>
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>但是直接在 <code>if</code> 中写这样的表达式太过局限，或者 有很多方式都能判断是在微信环境中，会导致项目中充斥着五花八门的判断，类型谓词的好处就出来了</p>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">checkIsWxNativeAPICanUse</span>(<span class="hljs-params">win: Window</span>): <span class="hljs-title">win</span> <span class="hljs-title">is</span> </span>&#123; wx: Exclude<Window[<span class="hljs-string">'wx'</span>], <span class="hljs-literal">undefined</span>> &#125; & Window &#123;
    <span class="hljs-keyword">return</span> <span class="hljs-keyword">typeof</span> <span class="hljs-built_in">window</span>.wx !== <span class="hljs-string">'undefined'</span>
&#125;
<span class="hljs-comment">// 使用</span>
<span class="hljs-keyword">if</span> (checkIsWxNativeAPICanUse(<span class="hljs-built_in">window</span>)) &#123;
    <span class="hljs-built_in">window</span>.wx.xxxx()
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-8">总结</h2>
<p>非必要少使用 <code>any</code> 既是良好的 <code>ts</code> 代码习惯的养成，也是对自己代码质量的较真</p>
<p>你还有什么 ts 技巧呢</p>
<blockquote>
<p>原文：<a href="https://yzl.xyz/lin/2021/05/TypeScript%E8%BF%9B%E9%98%B6-%E5%A6%82%E4%BD%95%E9%81%BF%E5%85%8D-any/ff7f28f9eb29.html" target="_blank" rel="nofollow noopener noreferrer">yzl.xyz/lin/2021/05…</a></p>
</blockquote></div>  
</div>
            