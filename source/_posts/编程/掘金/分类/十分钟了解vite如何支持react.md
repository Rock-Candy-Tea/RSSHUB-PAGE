
---
title: '十分钟了解vite如何支持react'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/0b69a520ed6c472d9ddce7ab39378ce7~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Wed, 28 Jul 2021 17:03:37 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/0b69a520ed6c472d9ddce7ab39378ce7~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>@charset "UTF-8";.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:14px;overflow-x:hidden;color:#353535&#125;.markdown-body h1&#123;padding-bottom:4px;font-size:30px&#125;.markdown-body h1,.markdown-body h2&#123;margin-top:36px;margin-bottom:10px;line-height:1.5;color:#005bb7&#125;.markdown-body h2&#123;position:relative;padding-left:16px;padding-right:10px;padding-bottom:10px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h2:before&#123;content:"「";position:absolute;top:-6px;left:-10px&#125;.markdown-body h2:after&#123;content:"」";position:absolute;top:6px;right:auto&#125;.markdown-body h3&#123;position:relative;padding-bottom:0;margin-top:30px;margin-bottom:10px;font-size:20px;line-height:1.5;color:#005bb7;padding-left:6px&#125;.markdown-body h3:before&#123;content:"»";padding-right:6px;color:#2196f3&#125;.markdown-body h4&#123;margin-top:24px;font-size:16px&#125;.markdown-body h4,.markdown-body h5&#123;padding-bottom:0;margin-bottom:10px;line-height:1.5;color:#005bb7;padding-left:6px&#125;.markdown-body h5&#123;margin-top:18px;font-size:14px&#125;.markdown-body h6&#123;padding-bottom:0;margin-top:12px;margin-bottom:10px;font-size:12px;line-height:1.5;color:#005bb7;padding-left:6px&#125;.markdown-body p&#123;line-height:inherit;margin-top:16px;margin-bottom:16px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;position:relative;width:98%;height:1px;margin-top:32px;margin-bottom:32px;background-image:linear-gradient(90deg,#007fff,rgba(255,0,0,.3),hsla(0,0%,100%,.1),rgba(255,0,0,.3),#007fff);border-width:0;overflow:visible&#125;.markdown-body hr:after&#123;content:"";position:absolute;margin:auto;left:0;right:0;bottom:0;top:0;display:inline-block;width:60px;height:20px;background:#fff;background-image:url(data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACgAAAAgCAYAAABgrToAAAADoklEQVRYR82XTYgcRRTHf2933Q1RjAa9eFO8JHoJ8RQVBQ2iBwXBET0YEUTXNVmNQtTpmeqaWV0XNRq/o4KoECSCEPSg4CF+BYUkIIiCoCJCPIhC/Ihh2Z0nVV27VnZnenumW9i6ddV7//frV69fVQurfMgq56NawFTPAU6QyomqXrw6wIZeyhCPebA5buNR+akKyGoAjd6BshthnYdSjqNcRVuOlIUsD2j0SuA94IwuMHdh5ZUykOUBXfSGbmKI54EtAeYIHSZoy5dl4JxvNYBOKdW1KE8BQ8AkVk6WhasWsAiN0TX9gveXQaPP+Aytpc4u+bMI06JNohsYYYYOR2lJWtS3OKDRfcAtQfgDoI6Vo4UCGb0OmAEuDvZvYmVbEd/igC3dzDz7gQu8sPA9kJDK27mBmjqBeLjTg90PDFOjWawFFQd06kZHEfaj3LAIpTRpSXsZ5E06zEYP9sDimnAApYaV2SLZG/wjMeqAkijwW4xQJ5Gf/ZzRC8OW3hiBTGGlURRswW55Bh/Ssxljrwew8l1PQaM14GngvGDzBUKdDsMeTtgU5o8B92PFlUf3YXUrHa7Fys6lBqcCGnX15YQ2A18FyPd7Crd1A3M8C1wdbH4DD3hWeP6IEXbQkG97ajR1HPFnuPP5jFFq1OWX7hl8WM9l1AO648uNfwLk7tytMeogty+xeQ4rO3r6bdcx1nuwOGsHmaXGtPzae4uzGnLH1kQkvpdZGrHjssBZJrL+pqS05KWc8tgITAPXRzYvYOXe/C2OV43eDcRBDtIhoS2f9wzc0Cv8Wls+zoFzUC5zF0U241h5uZtPfptp6OUM8wbK+cH5GEpCS17P3fJei0Z3+npTxryJ8CPzbKMtn/ZyWbkPGl0PuFPkmkjkcb4h4R2ZLwRq1H0ALmvjkf2HwK1Y+T1PY2XABe/sHJ6MxN5lnoSpnC/UGbsTaI5phK2R7x6s3Ffk5YoDOrWm3onwJHBmEP86bPmBrsGaenNoIdnxCH+gPEhLXi0Cl1VBvyPVLSh7gEuC62yAfOIUqabWEaaiucMIk6RyqJ+Q/QM69V26jjW86Gvov/EaoyT8zRCn+Xq7PVrbx0nuYUaO9wM3WAbjCE1NEUw09Um4UV+2OKfYfu5/S19gsAzGKqm6LE5FrShbdS0ku465DjDwKA/oQht19ejqbaEVuRbiLhuHByYLjtUAZpDutzP7cYdHsPJXWbjyNVgFwQoa1WXwf4Jd9YD/Ap80+yE7+u9aAAAAAElFTkSuQmCC);background-repeat:no-repeat;background-size:auto 100%;background-position-x:center&#125;.markdown-body code&#123;padding:.065em .4em;font-size:.87em;color:#c2185b;word-break:break-word;overflow-x:auto;background-color:#fff4f4;border-radius:2px&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;display:block;padding:16px 12px;margin:0;font-size:12px;color:#333;word-break:normal;overflow-x:auto;background:#f8f8f8&#125;.markdown-body pre>code::-webkit-scrollbar&#123;width:4px;height:4px&#125;.markdown-body pre>code::-webkit-scrollbar-track&#123;background-color:#bedcff&#125;.markdown-body pre>code::-webkit-scrollbar-thumb&#123;background-color:#2196f3;border-radius:10px&#125;.markdown-body a&#123;position:relative;text-decoration:none;color:#3da8f5;border-bottom:1px solid #bedcff&#125;.markdown-body a:hover&#123;color:#007fff;border-bottom-color:#007fff&#125;.markdown-body a:active&#123;color:#007fff&#125;.markdown-body a:after&#123;position:absolute;content:"";top:100%;left:0;width:100%;opacity:0;border-bottom:1px solid #bedcff;transition:top .3s,opacity .3s;transform:translateZ(0)&#125;.markdown-body a:hover:after&#123;top:0;opacity:1;border-bottom-color:#007fff&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #c3e0fd;border-spacing:0;border-collapse:collapse&#125;.markdown-body table thead&#123;color:#000;text-align:left;font-size:14px;background:#f6f6f6&#125;.markdown-body table tr:nth-child(2n)&#123;background-color:#f7fbff&#125;.markdown-body table tr:hover&#123;background-color:#e0edf7&#125;.markdown-body table td,.markdown-body table th&#123;padding:12px 8px;line-height:24px;border:1px solid #c3e0fd&#125;.markdown-body table th&#123;color:#005bb7;background-color:#dff0ff&#125;.markdown-body table td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#8c8c8c;border-left:4px solid #2196f3;background-color:#f0fdff;padding:1px 20px;margin:22px 0&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body b,.markdown-body blockquote>b,.markdown-body blockquote>strong,.markdown-body strong&#123;color:#2196f3&#125;.markdown-body em,.markdown-body i&#123;color:#4fc3f7&#125;.markdown-body del&#123;color:#ccc&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:4px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body details>summary&#123;outline:none;color:#005bb7;font-size:20px;font-weight:bolder;border-bottom:1px solid #bedcff;cursor:pointer&#125;.markdown-body details>p&#123;padding:10px 20px;margin:10px 0 0;color:#666;background-color:#f0fdff;border:2px dashed #2196f3&#125;.markdown-body h1::selection,.markdown-body h2::selection,.markdown-body h3::selection,.markdown-body h4::selection,.markdown-body h5::selection,.markdown-body h6::selection&#123;color:#005bb7;background-color:rgba(160,200,255,.15)&#125;.markdown-body p::selection&#123;color:#c80000&#125;.markdown-body a::selection,.markdown-body b::selection,.markdown-body del::selection,.markdown-body em::selection,.markdown-body i::selection,.markdown-body strong::selection&#123;background-color:transparent&#125;.markdown-body code::selection&#123;background-color:#ffeaeb&#125;.markdown-body pre>code::selection&#123;background-color:rgba(160,200,255,.25)&#125;.markdown-body ol ::selection,.markdown-body ul ::selection&#123;background-color:rgba(160,200,255,.15)&#125;.markdown-body .contains-task-list&#123;padding-left:14px;list-style:none&#125;.markdown-body .contains-task-list input[type=checkbox]&#123;position:relative&#125;.markdown-body .contains-task-list input[type=checkbox]:before&#123;content:"";position:absolute;top:0;left:0;right:0;bottom:0;width:inherit;height:inherit;background:#f0f8ff;border:1px solid #add6ff;border-radius:2px;box-sizing:border-box;z-index:1&#125;.markdown-body .contains-task-list input[type=checkbox]:checked:after&#123;content:"✓";position:absolute;top:-12px;left:0;right:0;bottom:0;width:0;height:0;color:#f55;font-size:20px;font-weight:700;z-index:2&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/0b69a520ed6c472d9ddce7ab39378ce7~tplv-k3u1fbpfcp-watermark.image" alt="掘金引流终版.gif" loading="lazy" referrerpolicy="no-referrer"></p>
<blockquote>
<p>丁楠:  微医前端技术部医疗支撑组  专业标题党，人菜瘾大的刀斯林</p>
</blockquote>
<h2 data-id="heading-0">前言</h2>
<p><code>vite</code> 是基于浏览器支持 ESM 模块，用以解决大型应用本地开发环境打包、热更新时间久的一套解决方案，目前已支持<code>vue</code>、<code>react</code>、<code>Svelte</code>、<code>Solid</code>等主流框架，相信不少同学已经开始使用 vite，并体验到“飞一般”的体验啦，下面我们来看看<code>vite</code>是如何支持<code>react</code>的吧<br>
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/28d699166b894f7d979d0f68e922f74d~tplv-k3u1fbpfcp-zoom-1.image" alt="u=2562422987,3798982828&fm=26&fmt=auto&gp=0.webp" loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-1">一、启动</h2>
<p>首先从 github 上拉下 vite 的源码，做好准备工作</p>
<pre><code class="hljs language-bash copyable" lang="bash">git <span class="hljs-built_in">clone</span> https://github.com/vitejs/vite.git
<span class="hljs-built_in">cd</span> vite
yarn
<span class="hljs-built_in">cd</span> packages/vite
yarn build
yarn link
<span class="copy-code-btn">复制代码</span></code></pre>
<p>用脚手架搭建好 vite-react 项目</p>
<pre><code class="hljs language-javascript copyable" lang="javascript">yarn create @vitejs/app my-react-app --template react
yarn link vite
yarn dev
<span class="copy-code-btn">复制代码</span></code></pre>
<p>加上 node 浏览器端调试 script</p>
<pre><code class="copyable">"debug": "node --inspect-brk node_modules/vite/dist/node/cli.js"
<span class="copy-code-btn">复制代码</span></code></pre>
<p>启动服务，可以看到
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/b82e7266db9747c38059dd3fc4c02273~tplv-k3u1fbpfcp-zoom-1.image" alt="企业微信截图_16260545748073.png" loading="lazy" referrerpolicy="no-referrer">
index.html 里比源码多了一块<code>vite/clinet</code>、<code>@react/refresh</code>的代码，另外 script 的 type 都是<code>module</code>类型，我们来根据源码分析下 vite 是如何做了这一层转化。</p>
<h2 data-id="heading-2">二、中间件（middleware）</h2>
<p>vite 2.x 之后放弃了原先 1.x 的 koa 模型，采用 node 原生 http 模块+connect 的中间件模型，在请求 localhost 过程中首先会被<code>connect-history-api-fallback</code>重定向到 index.html，随后会进入到下一个中间件<code>indexHtmlMiddleware</code>，这里实际是会执行<code>createDevHtmlTransformFn</code>函数</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">// packages\vite\src\node\server\middlewares\indexHtml.ts</span>
<span class="hljs-keyword">export</span> <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">createDevHtmlTransformFn</span>(<span class="hljs-params">
  server: ViteDevServer
</span>): (<span class="hljs-params">url: string, html: string, originalUrl: string</span>) => <span class="hljs-title">Promise</span><<span class="hljs-title">string</span>> </span>&#123;
  <span class="hljs-keyword">const</span> [preHooks, postHooks] = resolveHtmlTransforms(server.config.plugins)

  <span class="hljs-keyword">return</span> (url: string, <span class="hljs-attr">html</span>: string, <span class="hljs-attr">originalUrl</span>: string): <span class="hljs-built_in">Promise</span><string> => &#123;
    <span class="hljs-keyword">return</span> applyHtmlTransforms(html, [...preHooks, devHtmlHook, ...postHooks], &#123;
      <span class="hljs-attr">path</span>: url,
      <span class="hljs-attr">filename</span>: getHtmlFilename(url, server),
      server,
      originalUrl
    &#125;)
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这里会导出两个 hook，作用分别是</p>
<ul>
<li>devHtmlHook， 将@/vite/client.js 插入头部</li>
<li>react-refresh， 将一堆 react-refresh 的代码插入头部</li>
</ul>
<p>这里就解释了截图中的两端 script 从哪里来的，@/vite/client.js 简单来讲就是支持<code>vite-hmr</code>热更新的一些代码，而<code>@react-refresh</code>是 vite 支持 react 的热更新插件代码</p>
<h2 data-id="heading-3">三、转换（transform）</h2>
<p>从入口文件（index.html）发起的资源请求都会进入<code>transformMiddleware</code></p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">// packages\vite\src\node\server\index.ts  文件转换的核心</span>
  middlewares.use(transformMiddleware(server))
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">// packages\vite\src\node\server\transformRequest.ts </span>
<span class="hljs-keyword">export</span> <span class="hljs-keyword">async</span> <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">transformRequest</span>(<span class="hljs-params">
  url
  &#123; config, pluginContainer, moduleGraph, watcher &#125;
  options
</span>) </span>&#123;

  ...
  <span class="hljs-keyword">const</span> loadResult = <span class="hljs-keyword">await</span> pluginContainer.load(id, ssr)
  
  code = loadResult.code
  map = loadResult.map

  <span class="hljs-comment">// 代码转换，调用一系列 plugin 做代码转换</span>
  <span class="hljs-keyword">const</span> transformStart = isDebug ? <span class="hljs-built_in">Date</span>.now() : <span class="hljs-number">0</span>
  <span class="hljs-keyword">const</span> transformResult = <span class="hljs-keyword">await</span> pluginContainer.transform(code, id, map, ssr)
  
  code = transformResult.code!
  map = transformResult.map

  <span class="hljs-keyword">return</span> (mod.transformResult = &#123;
    code,
    map,
    <span class="hljs-attr">etag</span>: getEtag(code, &#123; <span class="hljs-attr">weak</span>: <span class="hljs-literal">true</span> &#125;)
  &#125; <span class="hljs-keyword">as</span> TransformResult)
  
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>而 pluginContainer 的 transform 函数是会调用初始化时 vite 内置的一系列 plugin 对源码进行转换，以<code>src/main.jsx</code>文件为例，首先源码</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">import</span> React <span class="hljs-keyword">from</span> <span class="hljs-string">'react'</span>
<span class="hljs-keyword">import</span> ReactDOM <span class="hljs-keyword">from</span> <span class="hljs-string">'react-dom'</span>
<span class="hljs-keyword">import</span> <span class="hljs-string">'./index.css'</span>
<span class="hljs-keyword">import</span> App <span class="hljs-keyword">from</span> <span class="hljs-string">'./App'</span>

ReactDOM.render(
  <span class="xml"><span class="hljs-tag"><<span class="hljs-name">React.StrictMode</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">App</span> /></span>
  <span class="hljs-tag"></<span class="hljs-name">React.StrictMode</span>></span></span>,
  <span class="hljs-built_in">document</span>.getElementById(<span class="hljs-string">'root'</span>)
)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>会被标识名为 vite:esbuild 的 plugin 利用 esbuild 的内置 api<code>transform</code>，将<code>jsx</code>语法转译成<code>React.createElement</code>，算是替代了<code>babel</code>的一部分作用</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">import</span> React <span class="hljs-keyword">from</span> <span class="hljs-string">"react"</span>;
<span class="hljs-keyword">import</span> ReactDOM <span class="hljs-keyword">from</span> <span class="hljs-string">"react-dom"</span>;
<span class="hljs-keyword">import</span> <span class="hljs-string">"./index.css"</span>;
<span class="hljs-keyword">import</span> App <span class="hljs-keyword">from</span> <span class="hljs-string">"./App"</span>;
ReactDOM.render(<span class="hljs-comment">/* @__PURE__ */</span> React.createElement(React.StrictMode, <span class="hljs-literal">null</span>, <span class="hljs-comment">/* @__PURE__ */</span> React.createElement(App, <span class="hljs-literal">null</span>)), <span class="hljs-built_in">document</span>.getElementById(<span class="hljs-string">"root"</span>));
<span class="copy-code-btn">复制代码</span></code></pre>
<p>接着会进入标识名为 vite:import-analysis 的 plugin</p>
<blockquote>
<p>原生 ES 引入不支持裸模块导入，Vite 将在服务的所有源文件中检测此类裸模块导入，预构建和重写导入合法 url</p>
</blockquote>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">import</span> &#123; someMethod &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'my-dep'</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>由于浏览器不支持直接的裸模块导入，所以需要将模块地址改写成真实的资源文件地址，<code>import-analysis</code>使用了<code>es-module-lexer</code>这个包，去动态的分析当前代码中的<code>import</code>语法涉及的依赖，比如上面的<code>react</code>、<code>react-dom</code>，解析成依赖文件所在的本地地址（/node_modules/.vite 文件夹），然后再调用内置的<code>transformCjsImport</code>函数，转换 Commonjs 类型包的 import 语句，比如</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">import</span> React <span class="hljs-keyword">from</span> <span class="hljs-string">"react"</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>将会被转译成</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">import</span> __vite__cjsImport0_react <span class="hljs-keyword">from</span> <span class="hljs-string">"/node_modules/.vite/react.js?v=21227a2f"</span>; <span class="hljs-keyword">const</span> React = __vite__cjsImport0_react.__esModule ? __vite__cjsImport0_react.default : __vite__cjsImport0_react
<span class="copy-code-btn">复制代码</span></code></pre>
<p><em>总感觉这部分在 webpack 中也有类似的实现，感兴趣的朋友也可以找找看，同时多啰嗦几句，vue3 也是一样的转换逻辑，只是针对单文件需要@vitejs/plugin-vue 的支持</em>
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/1296d199c66a45678fa3678b3030a73e~tplv-k3u1fbpfcp-zoom-1.image" alt="u=933098548,4165838110&fm=26&fmt=auto&gp=0.webp" loading="lazy" referrerpolicy="no-referrer"></p>
<p>后续的加载逻辑形式也是类似的，就不赘述了。</p>
<h2 data-id="heading-4">四、@vitejs/plugin-react-refresh</h2>
<p>最后再讲下这个包，其实 vite 对 react 的支持主要还是用 esbuild 一部分得替代了原来<code>@babel/preset-react</code>的作用，另外一块就是封装了官方的 react-refresh，来支持 react 的热更新，下面，我们来看下它做了什么。</p>
<h3 data-id="heading-5">转码</h3>
<p>实际上所有的文件资源都会被@react-refresh 处理一遍，所有 jsx 文件会被<code>@react-refresh</code>通过<code>@babel/core</code>转译一遍，不过只有真正需要热更新的 react 组件才会被输出</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">const</span> result = transformSync(code, &#123;
    <span class="hljs-attr">babelrc</span>: <span class="hljs-literal">false</span>,
    <span class="hljs-attr">configFile</span>: <span class="hljs-literal">false</span>,
    <span class="hljs-attr">filename</span>: id,
    <span class="hljs-attr">parserOpts</span>: &#123;
      <span class="hljs-attr">sourceType</span>: <span class="hljs-string">'module'</span>,
      <span class="hljs-attr">allowAwaitOutsideFunction</span>: <span class="hljs-literal">true</span>,
      <span class="hljs-attr">plugins</span>: parserPlugins
    &#125;,
    <span class="hljs-attr">generatorOpts</span>: &#123;
      <span class="hljs-attr">decoratorsBeforeExport</span>: <span class="hljs-literal">true</span>
    &#125;,
    <span class="hljs-attr">plugins</span>: [
      <span class="hljs-built_in">require</span>(<span class="hljs-string">'@babel/plugin-transform-react-jsx-self'</span>),
      <span class="hljs-built_in">require</span>(<span class="hljs-string">'@babel/plugin-transform-react-jsx-source'</span>),
      [<span class="hljs-built_in">require</span>(<span class="hljs-string">'react-refresh/babel'</span>), &#123; <span class="hljs-attr">skipEnvCheck</span>: <span class="hljs-literal">true</span> &#125;]
    ],
    <span class="hljs-attr">ast</span>: !isReasonReact,
    <span class="hljs-attr">sourceMaps</span>: <span class="hljs-literal">true</span>,
    <span class="hljs-attr">sourceFileName</span>: id
  &#125;)

  <span class="hljs-keyword">if</span> (!<span class="hljs-regexp">/\$RefreshReg\$\(/</span>.test(result.code)) &#123;
    <span class="hljs-comment">// 这里会用正则去分析，代码块是否是个需要热更新支持的 react component，否则就返回源码</span>
    <span class="hljs-keyword">return</span> code
  &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-6">提供额外的运行时代码</h3>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">// index.html 被插入这一串初始化代码</span>
<span class="hljs-keyword">import</span> RefreshRuntime <span class="hljs-keyword">from</span> <span class="hljs-string">"/@react-refresh"</span>
RefreshRuntime.injectIntoGlobalHook(<span class="hljs-built_in">window</span>)
<span class="hljs-built_in">window</span>.$RefreshReg$ = <span class="hljs-function">() =></span> &#123;&#125;
<span class="hljs-built_in">window</span>.$RefreshSig$ = <span class="hljs-function">() =></span> <span class="hljs-function">(<span class="hljs-params">type</span>) =></span> type
<span class="hljs-built_in">window</span>.__vite_plugin_react_preamble_installed__ = <span class="hljs-literal">true</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">import</span> &#123; createHotContext <span class="hljs-keyword">as</span> __vite__createHotContext &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">"/@vite/client"</span>;
<span class="hljs-keyword">import</span>.meta.hot = __vite__createHotContext(<span class="hljs-string">"/src/App.jsx"</span>);
<span class="hljs-keyword">import</span> RefreshRuntime <span class="hljs-keyword">from</span> <span class="hljs-string">"/@react-refresh"</span>;
<span class="hljs-keyword">if</span> (<span class="hljs-keyword">import</span>.meta.hot) &#123;
  <span class="hljs-built_in">window</span>.$RefreshReg$ = <span class="hljs-function">(<span class="hljs-params">type, id</span>) =></span> &#123;
    RefreshRuntime.register(type, <span class="hljs-string">"D:/xxx/vite-react/src/App.jsx "</span> + id);
  &#125;;
  <span class="hljs-built_in">window</span>.$RefreshSig$ = RefreshRuntime.createSignatureFunctionForTransform;
&#125;

<span class="hljs-comment">// 这里插入组件转换后的代码</span>
<span class="hljs-keyword">if</span> (<span class="hljs-keyword">import</span>.meta.hot) &#123;
  <span class="hljs-keyword">import</span>.meta.hot.accept();
  <span class="hljs-keyword">if</span> (!<span class="hljs-built_in">window</span>.__vite_plugin_react_timeout) &#123;
    <span class="hljs-built_in">window</span>.__vite_plugin_react_timeout = <span class="hljs-built_in">setTimeout</span>(<span class="hljs-function">() =></span> &#123;
      <span class="hljs-built_in">window</span>.__vite_plugin_react_timeout = <span class="hljs-number">0</span>;
      RefreshRuntime.performReactRefresh();
    &#125;, <span class="hljs-number">30</span>);
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><code>importAnalysis</code>会在 jsx 文件上动态插入<code>createHotContext</code>的代码，<code>createHotContext</code>是<code>vite</code>提供的机制，用于缓存 context。</p>
<p><code>RefreshRuntime.register</code>是<code>react-refresh</code>提供的 api，用于注册组件，第二个参数是组件的文件路径加上 id，用于识别哪个组件需要被热替换。</p>
<p><code>RefreshRuntime.performReactRefresh</code>触发 react 渲染。</p>
<h2 data-id="heading-7">五、总结</h2>
<p>我们来个图归纳下 vite 在支持 react 上做了哪些事吧  <img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/811520897ea84100b8b1a58c05ac365b~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer">
其实在启动服务时，vite 会从入口文件起扫描一遍所有的依赖并进行预构建，并生成模块依赖 moduleGraph，类似于树状的形式，方便管理缓存，由于本文主要是对 react 方面的解读，就不一一深入了，后续也会有其他同学更深入的解读，感兴趣的同学欢迎继续跟踪，顺便路过的大哥、小姐姐们来个三连！
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/53ded54495664e088a9d72e267c2ef05~tplv-k3u1fbpfcp-zoom-1.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer">
​</p>
<h2 data-id="heading-8">小广告</h2>
<ul>
<li>微医集团 前端技术部医院支撑组</li>
<li>坐标：浙江杭州</li>
<li>社招 3 年+ 或者 22 届实习，待遇从优</li>
<li>简历邮箱： <a href="https://link.juejin.cn/?target=mailto%3A474038329%40qq.com" target="_blank" title="mailto:474038329@qq.com" ref="nofollow noopener noreferrer">474038329@qq.com</a></li>
</ul>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/9fb28f66c4064abb8bc62e7614126180~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p></div>  
</div>
            