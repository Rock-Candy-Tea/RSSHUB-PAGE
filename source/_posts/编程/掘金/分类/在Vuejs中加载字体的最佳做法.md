
---
title: '在Vue.js中加载字体的最佳做法'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/d2339f2082414514a69086b5e433565a~tplv-k3u1fbpfcp-zoom-1.image'
author: 掘金
comments: false
date: Sun, 11 Apr 2021 04:31:12 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/d2339f2082414514a69086b5e433565a~tplv-k3u1fbpfcp-zoom-1.image'
---

<div>   
<div class="markdown-body"><style>@charset "UTF-8";.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1:first-child,.markdown-body h2:first-child,.markdown-body h3:first-child,.markdown-body h4:first-child,.markdown-body h5:first-child,.markdown-body h6:first-child&#123;margin-top:-1.5rem;margin-bottom:1rem&#125;.markdown-body h1:before,.markdown-body h2:before,.markdown-body h3:before,.markdown-body h4:before,.markdown-body h5:before,.markdown-body h6:before&#123;content:"#";display:inline-block;color:#3eaf7c;padding-right:.23em&#125;.markdown-body h1&#123;position:relative;font-size:2.5rem;margin-bottom:5px&#125;.markdown-body h1:before&#123;font-size:2.5rem&#125;.markdown-body h2&#123;padding-bottom:.5rem;font-size:2.2rem;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:1.5rem;padding-bottom:0&#125;.markdown-body h4&#123;font-size:1.25rem&#125;.markdown-body h5&#123;font-size:1rem&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body strong&#123;color:#3eaf7c&#125;.markdown-body img&#123;max-width:100%;border-radius:2px;display:block;margin:auto;border:3px solid rgba(62,175,124,.2)&#125;.markdown-body hr&#123;border:none;border-top:1px solid #3eaf7c;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;overflow-x:auto;padding:.2rem .5rem;margin:0;color:#3eaf7c;font-weight:700;font-size:.85em;background-color:rgba(27,31,35,.05);border-radius:3px&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75;border-radius:6px;border:2px solid #3eaf7c&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;font-weight:500;text-decoration:none;color:#3eaf7c&#125;.markdown-body a:active,.markdown-body a:hover&#123;border-bottom:1.5px solid #3eaf7c&#125;.markdown-body a:before&#123;content:"⇲"&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #3eaf7c&#125;.markdown-body thead&#123;background:#3eaf7c;color:#fff;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:rgba(62,175,124,.2)&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:.5rem solid;border-color:#42b983;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body details&#123;outline:none;border:none;border-left:4px solid #3eaf7c;padding-left:10px;margin-left:4px&#125;.markdown-body details summary&#123;cursor:pointer;border:none;outline:none;background:#fff;margin:0 -17px&#125;.markdown-body details summary::-webkit-details-marker&#123;color:#3eaf7c&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body ol li::marker&#123;color:#3eaf7c&#125;.markdown-body ul li&#123;list-style:none&#125;.markdown-body ul li:before&#123;content:"•";margin-right:4px;color:#3eaf7c&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><blockquote>
<p><strong>博客原文</strong>：<a href="https://blog.zhangbing.site/2021/04/07/best-practices-for-loading-fonts-in-vue/" target="_blank" rel="nofollow noopener noreferrer">blog.zhangbing.site/2021/04/07/…</a></p>
</blockquote>
<p>添加字体不应该对性能产生负面影响。在本文中，我们将探讨在 Vue 应用程序中加载字体的最佳实践。</p>
<h2 data-id="heading-0">正确声明<code>font-face</code>的字体</h2>
<p>确保正确声明字体是加载字体的重要方面。这是通过使用 <code>font-face</code> 属性来声明你选择的字体来实现的。在你的Vue项目中，这个声明可以在你的根CSS文件中完成。在进入这个问题之前，我们先来看看Vue应用的结构。</p>
<pre><code class="copyable">/root
  public/
    fonts/
      Roboto/
        Roboto-Regular.woff2
        Roboto-Regular.woff
    index.html
  src/
    assets/
      main.css
    components/
    router/
    store/
    views/
    main.js
<span class="copy-code-btn">复制代码</span></code></pre>
<p>我们可以像这样在 <code>main.css</code> 中进行 <code>font-face</code> 声明：</p>
<pre><code class="hljs language-css copyable" lang="css">// <span class="hljs-attribute">src</span>/assets/<span class="hljs-selector-tag">main</span><span class="hljs-selector-class">.css</span>

<span class="hljs-keyword">@font-face</span> &#123;
  <span class="hljs-attribute">font-family</span>: <span class="hljs-string">"Roboto"</span>;
  <span class="hljs-attribute">font-weight</span>: <span class="hljs-number">400</span>;
  <span class="hljs-attribute">font-style</span>: normal;
  <span class="hljs-attribute">font-display</span>: auto;
  unicode-range: U+<span class="hljs-number">000</span>-<span class="hljs-number">5</span>FF;
  <span class="hljs-attribute">src</span>: <span class="hljs-built_in">local</span>(<span class="hljs-string">"Roboto"</span>), <span class="hljs-built_in">url</span>(<span class="hljs-string">"/fonts/Roboto/Roboto-Regular.woff2"</span>) <span class="hljs-built_in">format</span>(<span class="hljs-string">"woff2"</span>), <span class="hljs-built_in">url</span>(<span class="hljs-string">"/fonts/Roboto/Roboto-Regular.woff"</span>) <span class="hljs-built_in">format</span>(<span class="hljs-string">"woff"</span>);
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>首先要注意的是 <code>font-display:auto</code>。使用 <code>auto</code> 作为值可以让浏览器使用最合适的策略来显示字体。这取决于一些因素，如网络速度、设备类型、闲置时间等。</p>
<p>要想更多地控制字体的加载方式，你应该使用 <code>font-display: block</code>，它指示浏览器短暂地隐藏文本，直到字体完全下载完毕。其他可能的值有 <code>swap</code>、<code>fallback</code> 和 <code>optional</code>。你可以在<a href="https://css-tricks.com/almanac/properties/f/font-display/" target="_blank" rel="nofollow noopener noreferrer">这里</a>阅读更多关于它们的信息。</p>
<p>需要注意的是 <code>unicode-range: U+000-5FF</code>，它指示浏览器只加载所需的字形范围（U+000 - U+5FF）。你还想使用<a href="https://css-tricks.com/understanding-web-fonts-getting/" target="_blank" rel="nofollow noopener noreferrer">woff和woff2</a>字体格式，它们是经过优化的格式，可以在大多数现代浏览器中使用。</p>
<p>另外需要注意的是 <code>src</code> 顺序。首先，我们检查字体的本地副本是否可用(<code>local("Roboto”)</code>)并使用它。很多Android设备都预装了Roboto，在这种情况下，我们将使用预装的副本。如果没有本地副本，则在浏览器支持的情况下继续下载woff2格式。否则，它会跳至支持的声明中的下一个字体。</p>
<h2 data-id="heading-1">预加载字体</h2>
<p>一旦你的自定义字体被声明，你可以使用 <code><link rel="preload"></code> 告诉浏览器提前预加载字体。在 <code>public/index.html</code> 中，添加以下内容：</p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">link</span> <span class="hljs-attr">rel</span>=<span class="hljs-string">"preload"</span> <span class="hljs-attr">as</span>=<span class="hljs-string">"font"</span> <span class="hljs-attr">href</span>=<span class="hljs-string">"./fonts/Roboto/Roboto-Regular.woff2"</span> <span class="hljs-attr">type</span>=<span class="hljs-string">"font/woff2"</span> <span class="hljs-attr">crossorigin</span>=<span class="hljs-string">"anonymous"</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p><code>rel = “preload”</code> 指示浏览器尽快开始获取资源，<code>as = “font”</code> 告诉浏览器这是一种字体，因此它优先处理请求。还要注意<code>crossorigin=“anonymous"</code>，因为如果没有这个属性，预加载的字体会被浏览器丢弃。这是因为浏览器是以匿名方式获取字体的，所以使用这个属性就可以匿名请求。</p>
<p>使用 <code>link=preload</code> 可以增加自定义字体在需要之前被下载的机会。这个小调整大大加快了字体的加载时间，从而加快了您的Web应用程序中的文本渲染。</p>
<h2 data-id="heading-2">使用link = preconnect托管字体</h2>
<p>当使用<a href="https://fonts.google.com/" target="_blank" rel="nofollow noopener noreferrer">Google fonts</a>等网站的托管字体时，你可以通过使用 <code>link=preconnect</code> 来获得更快的加载时间。它告诉浏览器提前建立与域名的连接。</p>
<p>如果您使用的是Google字体提供的Roboto字体，则可以在 <code>public/index.html</code> 中执行以下操作：</p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">link</span> <span class="hljs-attr">rel</span>=<span class="hljs-string">"preconnect"</span> <span class="hljs-attr">href</span>=<span class="hljs-string">"https://fonts.gstatic.com"</span>></span>
...
<span class="hljs-tag"><<span class="hljs-name">link</span> <span class="hljs-attr">href</span>=<span class="hljs-string">"https://fonts.googleapis.com/css2?family=Roboto&display=swap"</span> <span class="hljs-attr">rel</span>=<span class="hljs-string">"stylesheet"</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这样就可以建立与原点<a href="https://fonts.gstatic.com/" target="_blank" rel="nofollow noopener noreferrer">fonts.gstatic.com</a> 的初始连接，当浏览器需要从原点获取资源时，连接已经建立。从下图中可以看出两者的区别。</p>
<p><img alt class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/d2339f2082414514a69086b5e433565a~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p>当加载字体时没有使用 <code>link=preconnect</code> 时，你可以看到连接所需的时间（DNS查找、初始连接、SSL等）。当像这样使用<code>link=preconnect</code> 时，结果看起来非常不同。</p>
<p><img alt class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/afc6056fcfbf4d819f535a26e829897c~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p>在这里，你会发现DNS查找、初始连接和SSL所花费的时间已经不存在了，因为前面已经进行了连接。</p>
<p><img alt class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/91a1f68179774411a79eb3a05003fa34~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-3">使用service workers缓存字体</h2>
<p>字体是静态资源，变化不大，所以它们是缓存的好候选。理想情况下，您的Web服务器应该为字体设置一个较长的 <code>max-age expires</code> 头，这样浏览器缓存字体的时间就会更长。如果你正在构建一个渐进式网络应用（PWA），那么你可以使用<a href="https://developers.google.com/web/fundamentals/primers/service-workers" target="_blank" rel="nofollow noopener noreferrer">service workers</a>来缓存字体，并直接从缓存中为它们提供服务。</p>
<p>要开始使用Vue构建PWA，请使用vue-cli工具生成一个新项目：</p>
<pre><code class="hljs language-shell copyable" lang="shell">vue create pwa-app
<span class="copy-code-btn">复制代码</span></code></pre>
<p>选择<strong>Manually select features</strong>选项，然后选择<strong>Progressive Web App (PWA) Support</strong>：</p>
<p><img alt class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/04bbc7262e9648a9975e0a3cc9de43d4~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p>这些就是我们生成PWA模板所需要的唯一东西。完成后，你就可以把目录改为 <code>pwa-app</code>，然后为app服务。</p>
<pre><code class="hljs language-shell copyable" lang="shell">cd pwa-app
yarn serve
<span class="copy-code-btn">复制代码</span></code></pre>
<p>你会注意到在 <code>src</code> 目录下有一个文件 <code>registerServiceWorker</code>，其中包含了默认的配置。在项目的根目录下，如果<code>vue.config.js</code> 不存在，请创建它，如果存在，请添加以下内容：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// vue.config.js</span>
<span class="hljs-built_in">module</span>.exports = &#123;
  <span class="hljs-attr">pwa</span>: &#123;
    <span class="hljs-attr">workboxOptions</span>: &#123;
      <span class="hljs-attr">skipWaiting</span>: <span class="hljs-literal">true</span>,
      <span class="hljs-attr">clientsClaim</span>: <span class="hljs-literal">true</span>,
    &#125;
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>vue-cli工具使用<a href="https://cli.vuejs.org/core-plugins/pwa.html" target="_blank" rel="nofollow noopener noreferrer">PWA plugin</a>生成service worker。在底层，它使用<a href="https://developers.google.com/web/tools/workbox" target="_blank" rel="nofollow noopener noreferrer">Workbox</a>来配置service worker和它控制的元素、要使用的缓存策略以及其他必要的配置。</p>
<p>在上面的代码片段中，我们要确保我们的应用程序始终由service worker的最新版本控制。这是必要的，因为它确保我们的用户总是查看应用程序的最新版本。您可以签出Workbox配置文档，以获得对生成的service worker行为的更多控制。</p>
<p>接下来，我们将自定义字体添加到 <code>public</code> 目录。我有以下结构：</p>
<pre><code class="copyable">root/
  public/
    index.html
    fonts/
      Roboto/
        Roboto-Regular.woff
        Roboto-Regular.woff2
<span class="copy-code-btn">复制代码</span></code></pre>
<p>一旦完成了Vue应用程序的开发，就可以通过从终端运行以下命令来构建它：</p>
<pre><code class="copyable">yarn build
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这将结果输出到 <code>dist</code> 文件夹中。如果你检查文件夹的内容，你会注意到一个类似于 <code>precache-manifest.1234567890.js</code> 的文件。它包含了要缓存的资产列表，这只是一个包含修订版和URL的键值对的列表。</p>
<pre><code class="hljs language-js copyable" lang="js">self.__precacheManifest = (self.__precacheManifest || []).concat([
  &#123;
    <span class="hljs-string">"revision"</span>: <span class="hljs-string">"3628b4ee5b153071e725"</span>,
    <span class="hljs-string">"url"</span>: <span class="hljs-string">"/fonts/Roboto/Roboto-Regular.woff2"</span>
  &#125;,
  ...
]);
<span class="copy-code-btn">复制代码</span></code></pre>
<p><code>public/</code> 文件夹中的所有内容都是默认缓存的，其中包括自定义字体。有了这个地方，你可以用像service这样的包来<a href="https://www.npmjs.com/package/serve" target="_blank" rel="nofollow noopener noreferrer">serve</a>你的应用程序，或者把 <code>dist</code> 文件夹托管在web服务器上查看结果。你可以在下面找到一个应用程序的截图。</p>
<p><img alt class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/5347f7bc6a124b3c91d2aabfe64f056a~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p>在随后的访问中，字体是从缓存中加载的，这可以加快应用程序的加载时间。</p>
<h2 data-id="heading-4">结论</h2>
<p>在这篇文章中，我们研究了在Vue应用程序中加载字体时应用的一些最佳实践。使用这些实践将确保你提供的字体看起来不错，而不影响应用的性能。</p></div> <div class="image-viewer-box" data-v-78c9b824><!----></div>  
</div>
            