
---
title: 'React history 路由模式webpack配置不生效'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/fd7e70ee3d7f4b8c86e65620310cff47~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Mon, 30 Aug 2021 00:24:54 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/fd7e70ee3d7f4b8c86e65620310cff47~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body html cache"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h3 data-id="heading-0">React history 路由模式webpack配置不生效</h3>
<blockquote>
<p>摘要：在做一个react学习项目的时候，一开始使用的是hash路由模式进行开发，后来想要切换成history路由模式。遂修改路由模式为BrowserRouter，当然如果配置不做任何修改，直接进行访问肯定是不成功的。因为hash路由模式进行前端资源访问的时候，路由改变只是hash在变化，不会向后端发送请求，而history路由模式则是整个浏览器地址栏地址都变化了，会向服务端发送请求。此时我们又没有进行类似代理的配置，请求肯定是不成功的。</p>
</blockquote>
<h3 data-id="heading-1">修改路由模式</h3>
<p>把 HashRouter 替换为 BrowserRouter</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">// 注释掉 HashRouter 路由引入方式。替换为 BrowserRouter</span>
<span class="hljs-comment">// import &#123; HashRouter &#125; from "react-router-dom";</span>
<span class="hljs-keyword">import</span> &#123; BrowserRouter &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">"react-router-dom"</span>;
<span class="hljs-comment">// 使用react-router-config来进行路由的配置</span>
<span class="hljs-keyword">import</span> &#123; renderRoutes &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">"react-router-config"</span>;
<span class="hljs-comment">// 自定义的路由配置</span>
<span class="hljs-keyword">import</span> routes <span class="hljs-keyword">from</span> <span class="hljs-string">"./router"</span>;

ReactDOM.render(
  <span class="xml"><span class="hljs-tag"><<span class="hljs-name">BrowserRouter</span> <span class="hljs-attr">basename</span>=<span class="hljs-string">"/"</span>></span>&#123;renderRoutes(routes)&#125;<span class="hljs-tag"></<span class="hljs-name">BrowserRouter</span>></span></span>,
  <span class="hljs-built_in">document</span>.getElementById(<span class="hljs-string">"app"</span>)
);
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-2">修改webpack配置</h3>
<p>秉着快速了解配置并解决问题的思路(拿来主义🐶)，直接百度了下相关的配置，拿到相关的搜索结果进行配置文件的修改。
此处只提供涉及到修改的配置信息。
可在devServer中配置historyApiFallback配置项，具体修改如下：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">// webpack.dev.js</span>
<span class="hljs-built_in">module</span>.exports = merge(common, &#123;
  <span class="hljs-attr">mode</span>: <span class="hljs-string">"development"</span>,
  <span class="hljs-attr">devtool</span>: <span class="hljs-string">"cheap-module-eval-source-map"</span>,
  <span class="hljs-attr">output</span>: &#123;
    <span class="hljs-attr">path</span>: path.resolve(__dirname, <span class="hljs-string">'../release'</span>),
    <span class="hljs-attr">publicPath</span>: path.resolve(__dirname, <span class="hljs-string">'../release'</span>)
  &#125;,
  <span class="hljs-attr">devServer</span>: &#123;
    <span class="hljs-attr">historyApiFallback</span>: <span class="hljs-literal">true</span>, <span class="hljs-comment">// 添加这一行代码，当使用 HTML5 History API 时，任意的 404 响应都可能需要被替代为 index.html</span>
    <span class="hljs-attr">stats</span>: <span class="hljs-string">"errors-only"</span>,
    <span class="hljs-attr">compress</span>: <span class="hljs-literal">true</span>,
    <span class="hljs-attr">port</span>: <span class="hljs-number">8081</span>,
    <span class="hljs-attr">hot</span>: <span class="hljs-literal">true</span>,
    <span class="hljs-attr">open</span>: <span class="hljs-literal">true</span>,
    <span class="hljs-attr">proxy</span>: &#123;
      <span class="hljs-string">"/api"</span>: &#123;
        <span class="hljs-attr">target</span>: <span class="hljs-string">"http://proxy.test.cn"</span>,
        <span class="hljs-attr">changeOrigin</span>: <span class="hljs-literal">true</span>,
      &#125;,
    &#125;,
  &#125;
&#125;);

<span class="copy-code-btn">复制代码</span></code></pre>
<p>涉及的修改：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-built_in">module</span>.exports = merge(common, &#123;
  <span class="hljs-comment">// 新增</span>
  <span class="hljs-attr">output</span>: &#123;
    <span class="hljs-attr">path</span>: path.resolve(__dirname, <span class="hljs-string">'../release'</span>),
    <span class="hljs-attr">publicPath</span>: path.resolve(__dirname, <span class="hljs-string">'../release'</span>)
  &#125;,
  <span class="hljs-attr">devServer</span>: &#123;
    <span class="hljs-comment">// 新增</span>
    <span class="hljs-attr">historyApiFallback</span>: <span class="hljs-literal">true</span>, <span class="hljs-comment">// 添加这一行代码，当使用 HTML5 History API 时，任意的 404 响应都可能需要被替代为 index.html</span>
  &#125;
&#125;);
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-3">运行调试</h3>
<p>由于没有先去官网查看相关的配置（<a href="https://link.juejin.cn/?target=https%3A%2F%2Fv4.webpack.docschina.org%2Fconfiguration%2Fdev-server%2F%23devserver-historyapifallback" target="_blank" rel="nofollow noopener noreferrer" title="https://v4.webpack.docschina.org/configuration/dev-server/#devserver-historyapifallback" ref="nofollow noopener noreferrer">官网链接</a>）。所以修改完就运行验证下配置是否正确。心想应该能成功的。可是当运行起来后发现，当访问 <a href="https://link.juejin.cn/?target=http%3A%2F%2Flocalhost%3A8081%2F" target="_blank" rel="nofollow noopener noreferrer" title="http://localhost:8081/" ref="nofollow noopener noreferrer">http://localhost:8081/</a> 或者其他路由 <a href="https://link.juejin.cn/?target=http%3A%2F%2Flocalhost%3A8081%2Flogin" target="_blank" rel="nofollow noopener noreferrer" title="http://localhost:8081/login" ref="nofollow noopener noreferrer">http://localhost:8081/login</a> 的时候得到如下的结果。</p>
<p>不成功，得到的结果总是 <code>Cannot GET /</code>。习惯性的思维是继续去进行搜索，不管是百度还是stackoverflow。其实忽略了最重要的资源官网。官网上有每一个配置字段的说明。我们只要细心一点，关注下每个字段配置的功能，一定能避免很多问题。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/fd7e70ee3d7f4b8c86e65620310cff47~tplv-k3u1fbpfcp-watermark.image" alt="image1.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fv4.webpack.docschina.org%2Fconfiguration%2Fdev-server%2F%23devserver-publicpath-" target="_blank" rel="nofollow noopener noreferrer" title="https://v4.webpack.docschina.org/configuration/dev-server/#devserver-publicpath-" ref="nofollow noopener noreferrer">publicPath 说明</a>。</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/fabc1a7d7c504e568c7a3581e3b3d164~tplv-k3u1fbpfcp-watermark.image" alt="image2.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>如果我们配置了publicPath， devServer会从publicPath下加载静态资源，并且这个路径除了配置一个完整URL之外，需要确保 <code>devServer.publicPath</code> 总是以斜杠(/)开头和结尾。我们做如下的调整：</p>
<pre><code class="hljs language-js copyable" lang="js">    publicPath: <span class="hljs-string">'/release/'</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>那此时我们的访问路径应该是 <code>http://localhost:8081/release/</code>。我们发现资源找到了！说明html模板加载没有问题了。不过，像<code>http://localhost:8081/login</code>这样的路径访问还是不行。因为我们的静态资源是在release路径下。所以<code>http://localhost:8081/login</code>这样的访问方式，肯定获取不到模板html，那路由渲染也肯定是不成功的。</p>
<h3 data-id="heading-4">解决方案</h3>
<p>我们有两种解决方式：</p>
<ol>
<li>走默认配置</li>
</ol>
<p>删掉 publicPath 配置，默认为<code>/</code>。此时访问 <code>http://localhost:8081/</code> 或者 <code>http://localhost:8081/login</code> 都能获取模板。然后路由跳转再由react-router来进行控制。</p>
<pre><code class="hljs language-js copyable" lang="js">output: &#123;
    <span class="hljs-attr">path</span>: path.resolve(__dirname, <span class="hljs-string">'../release'</span>),
&#125;,
<span class="hljs-attr">historyApiFallback</span>: <span class="hljs-literal">true</span>,
<span class="copy-code-btn">复制代码</span></code></pre>
<ol start="2">
<li>重写访问路由</li>
</ol>
<pre><code class="hljs language-js copyable" lang="js">output: &#123;
    <span class="hljs-attr">path</span>: path.resolve(__dirname, <span class="hljs-string">'../release'</span>),
    <span class="hljs-attr">publicPath</span>: <span class="hljs-string">'/release/'</span>
&#125;,
<span class="hljs-attr">historyApiFallback</span>: &#123;
    <span class="hljs-attr">rewrites</span>: [
    &#123;
        <span class="hljs-attr">from</span>: <span class="hljs-regexp">/.*/</span>,
        to: <span class="hljs-string">'/release/'</span>
    &#125;
    ]
&#125;,
<span class="copy-code-btn">复制代码</span></code></pre>
<p>我们把 <code>historyApiFallback:true</code> 修改为一个对象，并且重写请求路径。任何请求过来的路径，默认都走<code>/release/</code>，这样就能够跟我们设置的publicPath一致，就能获取到html模板文件了。</p></div>  
</div>
            