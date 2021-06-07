
---
title: 'NuxtJS 错误处理'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/822e96d64baa4c1d8fbe579f665983f4~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Sun, 06 Jun 2021 00:52:27 GMT
thumbnail: 'https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/822e96d64baa4c1d8fbe579f665983f4~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h2 data-id="heading-0">简介</h2>
<p>NuxtJS中的错误从产生到流经到最后的展示，有着一套既定的规则。本文通过对NuxtJS框架中错误流转的介绍，帮助读者准确的定位错误，并正确处理应用中的错误。</p>
<p>通过本文，你可以：</p>
<ol>
<li>了解NuxtJS错误的分类与流转机制</li>
<li>了解不同错误的捕获方式与处理技巧</li>
<li>了解NuxtJS错误页的展示原理，以及自定义错误页。</li>
</ol>
<h3 data-id="heading-1">错误来源</h3>
<p>NuxtJS框架中的错误来源有以下三种：</p>
<ol>
<li>事件处理函数</li>
<li>asyncData方法</li>
<li>组件模版渲染</li>
</ol>
<h3 data-id="heading-2">错误处理</h3>
<p>抛出的错误可以在以下四个位置进行捕获：</p>
<ol>
<li>errorCapture</li>
<li>Vue.js errorHandler</li>
<li>onunhandledrejection</li>
<li>render:errorMiddleware</li>
</ol>
<h3 data-id="heading-3">错误展示</h3>
<p>若不进行错误的处理，错误将最终被展示出来，有以下三种形式：</p>
<ol>
<li>浏览器Console</li>
<li><a href="https://nuxtjs.org/docs/2.x/concepts/views#error-page" target="_blank" rel="nofollow noopener noreferrer">NuxtJS错误页</a></li>
<li>静态错误页</li>
</ol>
<h2 data-id="heading-4">错误来源</h2>
<p>错误产生及传播可由下面的两张图表示：</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/822e96d64baa4c1d8fbe579f665983f4~tplv-k3u1fbpfcp-watermark.image" alt="【图1】事件处理函数中抛出的错误仅会出现在客户端(client-side)" loading="lazy" referrerpolicy="no-referrer">
【图1】事件处理函数中抛出的错误仅会出现在客户端(client-side)</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/88fb74c2c8a741cdadf241696fdadb63~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer">
【图2】asyncData方法中以及组件模版渲染中抛出的错误既可能出现在客户端(client-side)也可能出现在服务端(server-side)</p>
<h2 data-id="heading-5">错误处理</h2>
<h3 data-id="heading-6">errorCapture</h3>
<p><a href="https://vuejs.org/v2/api/#errorCaptured" target="_blank" rel="nofollow noopener noreferrer">errorCapture</a>是Vue组件的一个生命周期Hook，在NuxtJS中，同样可以为<a href="https://nuxtjs.org/docs/2.x/concepts/views#layouts" target="_blank" rel="nofollow noopener noreferrer">Layout</a>组件添加。在Layout组件中设置errorCapture，可以让你全局捕获和处理这些错误：</p>
<ol>
<li>事件处理函数（client-side）中的同步错误</li>
<li>组件模版渲染（client-side & server-side）中的错误</li>
</ol>
<p>DEMO in <a href="https://nuxtjs.org/guide/views/#default-layout" target="_blank" rel="nofollow noopener noreferrer">默认Layout - NuxtJS</a></p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">/**
 * <span class="hljs-doctag">@file </span>layouts/default.vue
 */</span>

<span class="hljs-keyword">import</span> Vue <span class="hljs-keyword">from</span> <span class="hljs-string">'vue'</span>
<span class="hljs-keyword">import</span> Component <span class="hljs-keyword">from</span> <span class="hljs-string">'vue-class-component'</span>

@Component(&#123;
  <span class="hljs-function"><span class="hljs-title">errorCaptured</span>(<span class="hljs-params">err, vm, info</span>)</span> &#123;
    <span class="hljs-keyword">if</span> (info === <span class="hljs-string">'render'</span>) &#123;
      <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'这是一个组件渲染的错误'</span>)
    &#125; <span class="hljs-keyword">else</span> &#123;
      <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'这是一个事件处理的错误'</span>)
    &#125;

    <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'[errorCaptured 错误处理]: '</span>, err, vm, info)

    <span class="hljs-comment">// 阻止错误继续向外传播</span>
    <span class="hljs-keyword">return</span> <span class="hljs-literal">false</span>
  &#125;,
&#125;)
<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> <span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Layout</span> <span class="hljs-keyword">extends</span> <span class="hljs-title">Vue</span> </span>&#123;
  ...
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-7">errorHandler</h3>
<p><a href="https://vuejs.org/v2/api/#errorHandler" target="_blank" rel="nofollow noopener noreferrer">errorHandler</a> 是Vue全局配置的一项，你可以使用它去捕获和处理这些错误：</p>
<ol>
<li>事件处理函数（client-side）中的同步错误且未被errorCapture处理掉</li>
<li>组件模版渲染（client-side）的错误且未被errorCapture处理掉</li>
</ol>
<p>DEMO in <a href="https://www.nuxtjs.cn/guides/directory-structure/plugins" target="_blank" rel="nofollow noopener noreferrer">plugins - NuxtJS</a></p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">/**
 * <span class="hljs-doctag">@file </span>plugins/monitor.client.js
 */</span>
<span class="hljs-keyword">import</span> Vue <span class="hljs-keyword">from</span> <span class="hljs-string">'vue'</span>

<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params">ctx</span>) </span>&#123;
  Vue.config.errorHandler = <span class="hljs-function">(<span class="hljs-params">error, vm, info</span>) =></span> &#123;
    <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'[errorHandler 错误处理]: '</span>, err, vm, info)
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-8">onunhandledrejection</h3>
<p><a href="https://developer.mozilla.org/en-US/docs/Web/API/WindowEventHandlers/onunhandledrejection" target="_blank" rel="nofollow noopener noreferrer">onunhandledrejection</a>是浏览器事件，可以捕获异步的代码错误，包括：</p>
<ol>
<li>事件处理函数（client-side）中的异步错误</li>
<li>asyncData（server-side）中的错误</li>
</ol>
<p>DEMO in <a href="https://www.nuxtjs.cn/guides/directory-structure/plugins" target="_blank" rel="nofollow noopener noreferrer">plugins - NuxtJS</a></p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">/**
 * <span class="hljs-doctag">@file </span>plugins/monitor.client.js
 */</span>

<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params">ctx</span>) </span>&#123;
  <span class="hljs-built_in">window</span>.onunhandledrejection = <span class="hljs-function">(<span class="hljs-params">event</span>) =></span> &#123;
    <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'[onunhandledrejection 错误处理]: '</span>, event, event.reason)
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-9">render:errorMiddleware</h3>
<p><a href="https://www.nuxtjs.cn/guides/internals-glossary/internals-renderer" target="_blank" rel="nofollow noopener noreferrer">render:errorMiddleware</a>是NuxtJS内部向外暴露的一个<a href="https://zh.nuxtjs.org/docs/2.x/configuration-glossary/configuration-hooks/" target="_blank" rel="nofollow noopener noreferrer">hook</a>，他本质上是添加一个<a href="https://github.com/senchalabs/connect#error-middleware" target="_blank" rel="nofollow noopener noreferrer">connect的错误中间件</a>，而<a href="https://github.com/senchalabs/connect" target="_blank" rel="nofollow noopener noreferrer">connect</a>是NuxtJS底层用于实现HTTP Server的框架。</p>
<p>值得关注的是，在<code>render:errorMiddleware</code>中你并不能阻止错误继续传播下去，也就是说你不能阻止 静态错误页 的展示。如果想避免静态错误页的展示，你需要在<code>asyncData</code>中捕获并处理掉这些错误。</p>
<p>DEMO in <a href="https://zh.nuxtjs.org/docs/2.x/configuration-glossary/configuration-hooks/" target="_blank" rel="nofollow noopener noreferrer">The hooks Property - NuxtJS</a></p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">/**
 * <span class="hljs-doctag">@file </span>hooks/render.js
 */</span>

<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> (nuxtConfig) => (&#123;
  <span class="hljs-function"><span class="hljs-title">errorMiddleware</span>(<span class="hljs-params">app</span>)</span> &#123;
    app.use(<span class="hljs-function">(<span class="hljs-params">error, _req, _res, next</span>) =></span> &#123;
      <span class="hljs-keyword">if</span> (error) &#123;
        <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'[errorMiddleware 错误处理]: '</span>, error)
      &#125;

      <span class="hljs-comment">// 将传递给后面的错误中间件继续处理</span>
      next(error)
    &#125;)
  &#125;,
&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-10">错误页面</h2>
<p>当错误没有被正常处理掉，会最终展示在前端界面上，共有三种形式。</p>
<h3 data-id="heading-11">浏览器Console</h3>
<p>事件处理函数中的错误会仅会展示到浏览器的Console（控制台）上，不会导致页面的崩溃（即我们常说的白屏）。</p>
<h3 data-id="heading-12">NuxtJS错误页</h3>
<p>客户端的asyncData错误和模版渲染错误会展示<a href="https://nuxtjs.org/docs/2.x/concepts/views#error-page" target="_blank" rel="nofollow noopener noreferrer">NuxtJS错误页</a>。使用 <a href="https://nuxtjs.org/docs/2.x/internals-glossary/context#error" target="_blank" rel="nofollow noopener noreferrer">context.error</a>方法也会导向该页面。</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/cc01a1906ece48cfa8cbe704cffcc13b~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>你可以通过添加<code>layouts/error.vue</code>文件来覆盖默认的NuxtJS错误页。</p>
<p>DEMO in <code>layouts/error.vue</code></p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">/**
 * <span class="hljs-doctag">@file </span>layouts/error.vue
 */</span>

@Component(&#123;
  <span class="hljs-attr">props</span>: &#123;
    <span class="hljs-attr">error</span>: &#123;
      <span class="hljs-attr">type</span>: <span class="hljs-built_in">Object</span>,
      <span class="hljs-attr">default</span>: <span class="hljs-function">() =></span> (&#123;&#125;),
    &#125;,
  &#125;,
&#125;)
<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> <span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">ErrorPage</span> <span class="hljs-keyword">extends</span> <span class="hljs-title">Vue</span> </span>&#123;
  <span class="hljs-function"><span class="hljs-title">mounted</span>(<span class="hljs-params"></span>)</span> &#123;
    <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'[layouts/error 错误展示]: '</span>, error)
  &#125;
&#125;

<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-13">静态错误页</h3>
<p>服务端的asyncData错误和模版渲染错误会展示静态错误页：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/57ced02ea55e4198ae9b40ee35c3ae53~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>但是在开发环境下，你不会看见如上页面，会改为展示 <a href="https://github.com/poppinss/youch" target="_blank" rel="nofollow noopener noreferrer">youch 错误页面</a>：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/9018a474b2954b5e9eb9edd0b1c08d26~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>你可以通过添加<code>app/views/error.html</code>文件来覆盖默认的静态错误页。</p>
<p>DEMO in <code>app/views/error.html</code></p>
<pre><code class="hljs language-html copyable" lang="html">/**
 * @file app/views/error.html
 */

<span class="hljs-meta"><!DOCTYPE <span class="hljs-meta-keyword">html</span>></span>
<span class="hljs-tag"><<span class="hljs-name">html</span> <span class="hljs-attr">lang</span>=<span class="hljs-string">"en"</span>></span>
<span class="hljs-tag"><<span class="hljs-name">head</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">meta</span> <span class="hljs-attr">charset</span>=<span class="hljs-string">"UTF-8"</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">meta</span> <span class="hljs-attr">http-equiv</span>=<span class="hljs-string">"X-UA-Compatible"</span> <span class="hljs-attr">content</span>=<span class="hljs-string">"IE=edge"</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">meta</span> <span class="hljs-attr">name</span>=<span class="hljs-string">"viewport"</span> <span class="hljs-attr">content</span>=<span class="hljs-string">"width=device-width, initial-scale=1.0"</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">title</span>></span>错误页<span class="hljs-tag"></<span class="hljs-name">title</span>></span>
<span class="hljs-tag"></<span class="hljs-name">head</span>></span>
<span class="hljs-tag"><<span class="hljs-name">body</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">h1</span>></span>服务器崩溃了，嘤嘤嘤～<span class="hljs-tag"></<span class="hljs-name">h1</span>></span>
<span class="hljs-tag"></<span class="hljs-name">body</span>></span>
<span class="hljs-tag"></<span class="hljs-name">html</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre></div>  
</div>
            