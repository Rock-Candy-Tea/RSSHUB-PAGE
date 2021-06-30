
---
title: 'vite2.0 踩坑实录'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=4866'
author: 掘金
comments: false
date: Wed, 30 Jun 2021 01:44:03 GMT
thumbnail: 'https://picsum.photos/400/300?random=4866'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h1 data-id="heading-0">vite2.0 踩坑实录</h1>
<p>算是对上一篇的补充，记录了一些在配置项目中遇到的问题，希望对大家能有所帮助～</p>
<h2 data-id="heading-1">vite项目构建优化</h2>
<ul>
<li>
<p>路由动态导入 经过rollup的构建，动态导入的文件将会生成异步的chunk文件，在我们访问项目的时候按需加载，极大的提升应用的加载速度</p>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-keyword">import</span> Home <span class="hljs-keyword">from</span> <span class="hljs-string">'@/views/home/index.vue'</span>
<span class="hljs-keyword">import</span> Layout <span class="hljs-keyword">from</span> <span class="hljs-string">'@/components/Layout.vue'</span>

<span class="hljs-keyword">const</span> routes: <span class="hljs-built_in">Array</span><RouteRecordRaw> = [
  &#123;
    <span class="hljs-attr">path</span>: <span class="hljs-string">'/'</span>,
    <span class="hljs-attr">component</span>: Layout,
    <span class="hljs-attr">redirect</span>: <span class="hljs-string">'/home'</span>,
    <span class="hljs-attr">children</span>: [
      &#123;
        <span class="hljs-attr">path</span>: <span class="hljs-string">'/home'</span>,
        <span class="hljs-attr">name</span>: <span class="hljs-string">'Home'</span>,
        <span class="hljs-attr">component</span>: Home,
        <span class="hljs-attr">meta</span>: &#123; <span class="hljs-attr">title</span>: <span class="hljs-string">'首页'</span> &#125;
      &#125;,
      &#123;
        <span class="hljs-attr">path</span>: <span class="hljs-string">'/about'</span>,
        <span class="hljs-attr">name</span>: <span class="hljs-string">'About'</span>,
        <span class="hljs-attr">meta</span>: &#123; <span class="hljs-attr">title</span>: <span class="hljs-string">'关于'</span>, <span class="hljs-attr">keepAlive</span>: <span class="hljs-literal">true</span> &#125;,
        <span class="hljs-attr">component</span>: <span class="hljs-function">() =></span> <span class="hljs-keyword">import</span>(<span class="hljs-string">'@/views/about/index.vue'</span>)
      &#125;,
      &#123;
        <span class="hljs-attr">path</span>: <span class="hljs-string">'/square'</span>,
        <span class="hljs-attr">name</span>: <span class="hljs-string">'Square'</span>,
        <span class="hljs-attr">meta</span>: &#123; <span class="hljs-attr">title</span>: <span class="hljs-string">'组件广场'</span>, <span class="hljs-attr">keepAlive</span>: <span class="hljs-literal">true</span> &#125;,
        <span class="hljs-attr">component</span>: <span class="hljs-function">() =></span> <span class="hljs-keyword">import</span>(<span class="hljs-string">'@/views/square/index.vue'</span>)
      &#125;
    ]
  &#125;
]
<span class="hljs-keyword">const</span> router = createRouter(&#123;
  <span class="hljs-attr">history</span>: process.env.NODE_ENV === <span class="hljs-string">'development'</span>
    ? createWebHistory(process.env.BASE_URL)
    : createWebHashHistory(process.env.BASE_URL),
  routes,
    <span class="hljs-function"><span class="hljs-title">scrollBehavior</span>(<span class="hljs-params">to, <span class="hljs-keyword">from</span>, savedPosition</span>)</span> &#123;
      <span class="hljs-keyword">if</span> (savedPosition) &#123;
        <span class="hljs-comment">// 通过前进后台时才触发</span>
        <span class="hljs-keyword">return</span> savedPosition
      &#125; <span class="hljs-keyword">else</span> &#123;
        <span class="hljs-keyword">return</span> &#123; <span class="hljs-attr">top</span>: <span class="hljs-number">0</span>, <span class="hljs-attr">behavior</span>: <span class="hljs-string">'smooth'</span> &#125;
      &#125;
    &#125;
  &#125;)

router.beforeEach(<span class="hljs-function">(<span class="hljs-params">to, <span class="hljs-keyword">from</span>, next</span>) =></span> &#123;
  <span class="hljs-comment">// 可以对权限进行一些校验</span>
  <span class="hljs-keyword">if</span> (to.path !== <span class="hljs-keyword">from</span>.path) &#123;
    <span class="hljs-built_in">document</span>.title = <span class="hljs-string">`星乐圈 | <span class="hljs-subst">$&#123;to.meta.title&#125;</span>`</span>
  &#125;
  next()
&#125;)

router.onError(<span class="hljs-function">(<span class="hljs-params">error</span>) =></span> &#123;
  <span class="hljs-keyword">const</span> pattern = <span class="hljs-regexp">/Loading chunk (\d)+ failed/g</span>
  <span class="hljs-keyword">const</span> isChunkLoadFailed = error.message.match(pattern)
  <span class="hljs-keyword">if</span> (isChunkLoadFailed) &#123;
    location.reload()
  &#125;
&#125;)

<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> router
<span class="copy-code-btn">复制代码</span></code></pre>
<p>上述代码，是一个vite构建的vue项目的router文件，使用的<code>vue-router@4.0.6</code>,Vue Router支持开箱即用的动态导入，这意味着你可以用动态导入代替静态导入.在代码中可以看到：about页和square页都是动态导入的。
关于动态导入，MDN上有非常详细的介绍: <a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/import#dynamic_imports" target="_blank" rel="nofollow noopener noreferrer">传送门</a></p>
<p>经过rollup的构建，动态导入的文件将会生成异步的chunk文件，在我们访问项目的时候按需加载，极大的提升应用的加载速度。</p>
<p>在vite项目中的路由动态导入中我踩的坑：</p>
<p>构建时不支持<code>@/</code>别名。在构建的时候，rollup构建时并不能按照配置的别名找到对应的文件，因此在构建环节会有报错</p>
<p>解决方案：</p>
<ol>
<li>
<p>一开始感觉是引用路径的问题，所以尝试了几种引用方式,然后终于有一种成功了！<code>component: () => import('/src/views/about/index.vue')</code> 改成绝对路径以后，就可以正常启动</p>
</li>
<li>
<p>升级vite版本，一开始是<code>vite@2.0.0-beta.35</code>，不支持别名。在升级到<code>vite@2.3.8</code>之后就支持了。估计是2.0刚出，一下子没有写完善也是可以理解滴～</p>
</li>
<li>
<p>使用import.meta.glob方法</p>
<p>我配置使遇到的一些报错和警告</p>
<blockquote>
<p>warning: "import.meta" is not available in the configured target environment ("es2019") and will be empty</p>
</blockquote>
<p>当vite配置项esbuild.target 为 ‘es2019‘的时候，会有这个警告。表示这个情况下不支持使用import.meta api</p>
<blockquote>
<p>[vite] Internal server error: Invalid glob import syntax: pattern must start with "." or "/" (relative to project root)</p>
</blockquote>
<p>import.meta.glob() 中的参数必须以"." 或 "/" 开头，相对根目录进行匹配</p>
<p>最终的写法部分代码：</p>
<pre><code class="hljs language-ts copyable" lang="ts">  <span class="hljs-keyword">import</span> Layout <span class="hljs-keyword">from</span> <span class="hljs-string">'@/components/Layout.vue'</span>

  <span class="hljs-keyword">const</span> modules = <span class="hljs-keyword">import</span>.meta.glob(<span class="hljs-string">'/src/views/*/index.vue'</span>)

  <span class="hljs-keyword">const</span> routes: <span class="hljs-built_in">Array</span><RouteRecordRaw> = [
    &#123;
      <span class="hljs-attr">path</span>: <span class="hljs-string">'/'</span>,
      <span class="hljs-attr">component</span>: Layout,
      <span class="hljs-attr">redirect</span>: <span class="hljs-string">'/home'</span>,
      <span class="hljs-attr">children</span>: [
        &#123;
          <span class="hljs-attr">path</span>: <span class="hljs-string">'/home'</span>,
          <span class="hljs-attr">name</span>: <span class="hljs-string">'Home'</span>,
          <span class="hljs-attr">component</span>: modules[<span class="hljs-string">'/src/views/home/index.vue'</span>],
          <span class="hljs-attr">meta</span>: &#123; <span class="hljs-attr">title</span>: <span class="hljs-string">'首页'</span> &#125;
        &#125;,
        &#123;
          <span class="hljs-attr">path</span>: <span class="hljs-string">'/about'</span>,
          <span class="hljs-attr">name</span>: <span class="hljs-string">'About'</span>,
          <span class="hljs-attr">meta</span>: &#123; <span class="hljs-attr">title</span>: <span class="hljs-string">'关于'</span>, <span class="hljs-attr">keepAlive</span>: <span class="hljs-literal">true</span> &#125;,
          <span class="hljs-attr">component</span>: modules[<span class="hljs-string">'/src/views/about/index.vue'</span>]
        &#125;,
        &#123;
          <span class="hljs-attr">path</span>: <span class="hljs-string">'/square'</span>,
          <span class="hljs-attr">name</span>: <span class="hljs-string">'Square'</span>,
          <span class="hljs-attr">meta</span>: &#123; <span class="hljs-attr">title</span>: <span class="hljs-string">'组件广场'</span>, <span class="hljs-attr">keepAlive</span>: <span class="hljs-literal">true</span> &#125;,
          <span class="hljs-attr">component</span>: modules[<span class="hljs-string">'/src/views/square/index.vue'</span>]
        &#125;
      ]
    &#125;
  ]
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
</ol>
<p>通过使用import.meta.glob 方法，我们可以通过后台接口来配置路由，可控的进行权限控制。routes数据如果由接口返回，则不在权限范围内的组件根本不会生成路由项，这无疑增加了权限控制的力度。</p>
</li>
<li>
<p>配置build.rollupOptions.manualChunks，对node_modules文件进行分包加载</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-title">manualChunks</span>(<span class="hljs-params">id</span>)</span> &#123;
  <span class="hljs-keyword">if</span> (id.includes(<span class="hljs-string">'node_modules'</span>) && id.includes(<span class="hljs-string">'prime'</span>)) &#123;
    <span class="hljs-keyword">return</span> <span class="hljs-string">'prime'</span>
  &#125; <span class="hljs-keyword">else</span> <span class="hljs-keyword">if</span> (id.includes(<span class="hljs-string">'node_modules'</span>) && id.includes(<span class="hljs-string">'vue'</span>)) &#123;
    <span class="hljs-keyword">return</span> <span class="hljs-string">'vue'</span>
  &#125; <span class="hljs-keyword">else</span> <span class="hljs-keyword">if</span> (id.includes(<span class="hljs-string">'node_modules'</span>)) &#123;
    <span class="hljs-keyword">return</span> <span class="hljs-string">'vendor'</span>
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>如果不配置这项，vite会将node_modules包打包成一个大的异步vendor.js文件, 如果文件过大，这无疑增加了页面渲染时的阻塞时长。而且不利于页面缓存优化。
在上面的配置中，我将ui框架（primeVue）、vue相关的包分别打包成一个文件，这样做除了可以减少每个依赖文件的体积之外，还可以对项目的缓存进行优化。这些基础库之类的依赖包，更新的次数会比较少。
结合服务端的文件缓存策略配置，用户除了首次访问时需要加载这些依赖文件，后面再访问，都可以直接从缓存读取。将依赖文件代码进行一定的切割，可以极大的提升项目的性能。</p>
<p>而且，vite在构建的时候，会自动生成如下html文件</p>
<pre><code class="hljs language-html copyable" lang="html">  <span class="hljs-meta"><!DOCTYPE <span class="hljs-meta-keyword">html</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">html</span> <span class="hljs-attr">lang</span>=<span class="hljs-string">"en"</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">head</span>></span>
      <span class="hljs-tag"><<span class="hljs-name">meta</span> <span class="hljs-attr">charset</span>=<span class="hljs-string">"UTF-8"</span> /></span>
      <span class="hljs-tag"><<span class="hljs-name">link</span> <span class="hljs-attr">rel</span>=<span class="hljs-string">"icon"</span> <span class="hljs-attr">href</span>=<span class="hljs-string">"/favicon.ico"</span> /></span>
      <span class="hljs-tag"><<span class="hljs-name">meta</span> <span class="hljs-attr">name</span>=<span class="hljs-string">"viewport"</span> <span class="hljs-attr">content</span>=<span class="hljs-string">"width=device-width, initial-scale=1.0"</span> /></span>
      <span class="hljs-tag"><<span class="hljs-name">title</span>></span>我的项目<span class="hljs-tag"></<span class="hljs-name">title</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">script</span> <span class="hljs-attr">type</span>=<span class="hljs-string">"module"</span> <span class="hljs-attr">crossorigin</span> <span class="hljs-attr">src</span>=<span class="hljs-string">"/assets/index.e3627129.js"</span>></span><span class="hljs-tag"></<span class="hljs-name">script</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">link</span> <span class="hljs-attr">rel</span>=<span class="hljs-string">"modulepreload"</span> <span class="hljs-attr">href</span>=<span class="hljs-string">"/js/vue/vue.a1ee204f.js"</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">link</span> <span class="hljs-attr">rel</span>=<span class="hljs-string">"modulepreload"</span> <span class="hljs-attr">href</span>=<span class="hljs-string">"/js/prime/prime.eb4bfea6.js"</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">link</span> <span class="hljs-attr">rel</span>=<span class="hljs-string">"stylesheet"</span> <span class="hljs-attr">href</span>=<span class="hljs-string">"/assets/prime.296674d4.css"</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">link</span> <span class="hljs-attr">rel</span>=<span class="hljs-string">"stylesheet"</span> <span class="hljs-attr">href</span>=<span class="hljs-string">"/assets/index.289426b3.css"</span>></span>
  <span class="hljs-tag"></<span class="hljs-name">head</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">body</span>></span>
      <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">id</span>=<span class="hljs-string">"app"</span>></span><span class="hljs-tag"></<span class="hljs-name">div</span>></span>
      
    <span class="hljs-tag"></<span class="hljs-name">body</span>></span>
  <span class="hljs-tag"></<span class="hljs-name">html</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>其中加了<code>rel="modulepreload"</code>属性的link标签，可以预加载原生模块，保证某些文件可以不必等到执行时才加载，同样可以提升页面的性能</p>
</li>
<li>
<p>图片资源文件处理。资源体积小于 assetsInlineLimit 选项值 则会被内联为 base64 data URL，一起被打包至引用它的文件中。以此减少对文件的请求次数，提升项目性能</p>
</li>
</ul>
<h2 data-id="heading-2">其它</h2>
<ol>
<li>给动态导入文件生成的异步chunk，放置相对应的文件夹中，或者自定义给chunk命名。</li>
</ol>
<p>嘿嘿，查了rollup文档很久，又自己试了好一会儿，终于成功了。参考如下配置：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> defineConfig(&#123;
  <span class="hljs-attr">build</span>: &#123;
    <span class="hljs-attr">assetsDir</span>: <span class="hljs-string">'assets'</span>,
    <span class="hljs-attr">rollupOptions</span>: &#123;
      <span class="hljs-attr">output</span>: &#123;
        <span class="hljs-comment">// eslint-disable-next-line @typescript-eslint/no-explicit-any</span>
        <span class="hljs-attr">chunkFileNames</span>: <span class="hljs-function">(<span class="hljs-params">chunkInfo: any</span>) =></span> &#123;
          <span class="hljs-keyword">const</span> facadeModuleId = chunkInfo.facadeModuleId ? chunkInfo.facadeModuleId.split(<span class="hljs-string">'/'</span>) : []
          <span class="hljs-keyword">const</span> fileName = facadeModuleId[facadeModuleId.length - <span class="hljs-number">2</span>] || <span class="hljs-string">'[name]'</span>
          <span class="hljs-keyword">return</span> <span class="hljs-string">`js/<span class="hljs-subst">$&#123;fileName&#125;</span>/[name].[hash].js`</span>
        &#125;,
      &#125;
    &#125;
  &#125;
&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<ol start="2">
<li>
<p>vite配置传入全局的scss变量</p>
<p>配置如下</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> defineConfig(&#123;
  <span class="hljs-attr">css</span>: &#123;
    <span class="hljs-attr">preprocessorOptions</span>: &#123;
      <span class="hljs-attr">scss</span>: &#123;
        <span class="hljs-attr">additionalData</span>: <span class="hljs-string">'@import "./src/styles/variables";'</span>
      &#125;
    &#125;
  &#125;,
&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
<li>
<p>还需要注意的是，不同版本的vite之间，配置项会存在一些差异，所以在对项目进行配置的时候，如果你完全按照文档进行配置还是有问题，不妨看看是不是自己的版本与文档的版本不一样导致的。</p>
</li>
</ol>
<h2 data-id="heading-3">最后</h2>
<p>分享一下我配置好了的vite2.0+Vue3.0项目：<a href="https://gitee.com/someFutures/happy-study" target="_blank" rel="nofollow noopener noreferrer">传送门</a>, 用来试水的项目，如果有什么不对的地方，欢迎指正！</p>
<h2 data-id="heading-4">感谢阅读 mua~</h2></div>  
</div>
            