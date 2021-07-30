
---
title: '在微信小程序中获取全局对象，并对他进行 polyfill'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/402484af56b74f4ea0999ecebe5ec51d~tplv-k3u1fbpfcp-zoom-1.image'
author: 掘金
comments: false
date: Wed, 28 Jul 2021 19:14:39 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/402484af56b74f4ea0999ecebe5ec51d~tplv-k3u1fbpfcp-zoom-1.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>微信小程序中的全局对象和其他环境中有所不同，通过 <code>global</code> 获取到的全局对象和 <code>V8 JavaScript</code> 引擎差距较大，很多时候需要兼容。</p>

<h2 data-id="heading-0">问题</h2>
<blockquote>
<p>小程序的主要开发语言是 JavaScript ，小程序的开发同普通的网页开发相比有很大的相似性。对于前端开发者而言，从网页开发迁移到小程序的开发成本并不高，但是二者还是有些许区别的。</p>
</blockquote>
<p>通过 <code>yarn add lodash.debounce</code> 添加到原生微信小程序项目中的防抖代码无法直接运行。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/402484af56b74f4ea0999ecebe5ec51d~tplv-k3u1fbpfcp-zoom-1.image" alt="TypeError" loading="lazy" referrerpolicy="no-referrer"></p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// => TypeError: Cannot read property 'now' of undefined</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这是因为，<code>lodash</code> 获取全局对象的方式在微信小程序中不适用</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">/** Detect free variable `global` from Node.js. */</span>
<span class="hljs-keyword">var</span> freeGlobal = <span class="hljs-keyword">typeof</span> <span class="hljs-built_in">global</span> == <span class="hljs-string">'object'</span> && <span class="hljs-built_in">global</span> && <span class="hljs-built_in">global</span>.Object === <span class="hljs-built_in">Object</span> && <span class="hljs-built_in">global</span>;
<span class="hljs-comment">// => global.Object is undefined </span>

<span class="hljs-comment">/** Detect free variable `self`. */</span>
<span class="hljs-keyword">var</span> freeSelf = <span class="hljs-keyword">typeof</span> self == <span class="hljs-string">'object'</span> && self && self.Object === <span class="hljs-built_in">Object</span> && self;
<span class="hljs-comment">// => freeSelf is undefined </span>

<span class="hljs-comment">/** Used as a reference to the global object. */</span>
<span class="hljs-keyword">var</span> root = freeGlobal || freeSelf || <span class="hljs-built_in">Function</span>(<span class="hljs-string">'return this'</span>)();
<span class="hljs-comment">// => root => &#123;&#125;</span>

<span class="hljs-keyword">var</span> now = <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params"></span>) </span>&#123;
  <span class="hljs-keyword">return</span> root.Date.now();
&#125;;
<span class="hljs-comment">// => root.Date is undefined</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-1">解决方案</h2>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// lodash-polyfill.js</span>
<span class="hljs-keyword">var</span> g = <span class="hljs-keyword">typeof</span> <span class="hljs-built_in">window</span> !== <span class="hljs-string">'undefined'</span> &&
<span class="hljs-built_in">window</span>.Math === <span class="hljs-built_in">Math</span> ? <span class="hljs-built_in">window</span> : <span class="hljs-keyword">typeof</span> <span class="hljs-built_in">global</span> === <span class="hljs-string">'object'</span> ? <span class="hljs-built_in">global</span> : <span class="hljs-built_in">this</span>

<span class="hljs-keyword">if</span> (!g.Object) &#123;
  g.Object = <span class="hljs-built_in">Object</span>
&#125;

<span class="hljs-keyword">if</span> (!g.Date) &#123;
  g.Date = <span class="hljs-built_in">Date</span>
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// app.js</span>
<span class="hljs-built_in">require</span>(<span class="hljs-string">'./lodash-polyfill.js'</span>)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这样，就可以开开心心地在项目中使用 <code>lodash.debounce</code> 啦(*^▽^*)。</p>
<hr>
<p>欢迎关注我的微信公众号：<em><strong>乘风破浪的Coder</strong></em></p></div>  
</div>
            