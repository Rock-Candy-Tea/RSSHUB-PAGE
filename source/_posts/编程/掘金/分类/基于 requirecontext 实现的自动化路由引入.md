
---
title: '基于 require.context 实现的自动化路由引入'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=1842'
author: 掘金
comments: false
date: Wed, 30 Jun 2021 01:07:08 GMT
thumbnail: 'https://picsum.photos/400/300?random=1842'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h3 data-id="heading-0">初识</h3>
<p>前端时间在掘金上看到一篇文章了解到了 <code>require.context</code> 这个api。一番百度之后，对这个 API 有了一定的了解，这让我产生了一个想法，就是用 require.context 复刻 nuxtjs 的路由规则。对 nuxtjs 的路由相关代码做了简单阅读，发现是用 gulp 以及 global 监听 pages 文件夹下的文件变动，再编译成对应的路由(了解不深，有误请指正),而 require.context 则是将 XX 文件夹下的文件模块直接引入。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-built_in">require</span>.context(path: string, deep?: boolean, filter?: <span class="hljs-built_in">RegExp</span>, mode?: <span class="hljs-string">"sync"</span> | <span class="hljs-string">"eager"</span> | <span class="hljs-string">"weak"</span> | <span class="hljs-string">"lazy"</span> | <span class="hljs-string">"lazy-once"</span>)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>上面的话就是这个 API 的用法。假设项目的 pages 文件夹下有 @/pages/A/index.vue 以及 @/pages/B/B.vue 两个文件。那么用该方法引入的话就会得到以下结果。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> context = <span class="hljs-built_in">require</span>.context(<span class="hljs-string">"@/pages/"</span>, <span class="hljs-literal">true</span>, <span class="hljs-regexp">/\.vue/</span>)
===>
context = <span class="hljs-function"><span class="hljs-title">webpackContext</span>(<span class="hljs-params">req</span>)</span> &#123;
<span class="hljs-keyword">var</span> id = webpackContextResolve(req);
<span class="hljs-keyword">return</span> __webpack_require__(id);
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>如果调用 context 的 keys 方法的话就可以拿到对应的文件路径。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> pages = context.keys()
===>
pages = [<span class="hljs-string">"./A/A.vue"</span>, <span class="hljs-string">"./B/B.vue"</span>]
<span class="copy-code-btn">复制代码</span></code></pre>
<p>如果要引入这个页面模块的话只需要</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> pageModule = context(<span class="hljs-string">"./A/A.vue"</span>)
===>
pageModule = Module &#123;<span class="hljs-attr">default</span>: &#123;…&#125;, <span class="hljs-attr">__esModule</span>: <span class="hljs-literal">true</span>, <span class="hljs-built_in">Symbol</span>(<span class="hljs-built_in">Symbol</span>.toStringTag): <span class="hljs-string">"Module"</span>&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这个 pageModule 也就是这个页面模块把它写在 vue-router 路由对应的 component 就可以了。</p>
<h3 data-id="heading-1">脑洞</h3>
<p>根据这个思路，我就想到了 nuxtjs 的路由引入方式，但是自我感觉。把路由规则交给文件夹的嵌套关系，让整个文件关系非常的混乱。非常不简洁明了，如果每个文件都有一个 index.css 另外引入的话那维护项目的话 应该是非常头疼的事情。
所以我打算把页面的层级统一拉平为一层。这样的话简洁明了，把页面的路由关系全部都归结到一个 json 文件中。
这样子的话整个路由的关系在 json 文件中也显得非常明显。</p>
<h3 data-id="heading-2">实现</h3>
<p>有了想法就要付诸实践。
首先读取 vue 文件模块</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> context = <span class="hljs-built_in">require</span>.context(<span class="hljs-string">"@/pages/"</span>, <span class="hljs-literal">true</span>, <span class="hljs-regexp">/\.vue/</span>)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>创建好 json 文件。并且写好路由关系并引入。</p>
<pre><code class="hljs language-json copyable" lang="json"><span class="hljs-comment">// routeHierarchyMap.json</span>
&#123;
  <span class="hljs-attr">"/"</span>: &#123;&#125;,
  <span class="hljs-attr">"A"</span>: &#123;&#125;,
  <span class="hljs-attr">"B"</span>: &#123;&#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>然后解析这个路由，我的想法是一级一级的解析，因为路由可能有多个 children。
首先先将路由引入放如一个对象中，该对象的 key - value 结果如下所示：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> pageObj = &#123;
  <span class="hljs-string">"/"</span>: Module,
  <span class="hljs-string">"A"</span>: Module,
  <span class="hljs-string">"B"</span>: Module
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// routes 为json文件的路由映射</span>
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">getRouteFromObj</span>(<span class="hljs-params">routes, parentsRoute</span>) </span>&#123;
  <span class="hljs-keyword">const</span> routesMap = <span class="hljs-built_in">Object</span>.keys(routes);
  <span class="hljs-keyword">return</span> routesMap.map(<span class="hljs-function">(<span class="hljs-params">item</span>) =></span> &#123;
    <span class="hljs-keyword">const</span> path = <span class="hljs-string">`<span class="hljs-subst">$&#123;parentsRoute.replace(<span class="hljs-regexp">/\/$/</span>, <span class="hljs-string">""</span>)&#125;</span>/<span class="hljs-subst">$&#123;item.replace(<span class="hljs-regexp">/\/$/</span>, <span class="hljs-string">""</span>)&#125;</span>`</span>;
    <span class="hljs-keyword">return</span> &#123;
      path,
      <span class="hljs-attr">component</span>: <span class="hljs-function">() =></span> pageObj[item].component,
      <span class="hljs-attr">children</span>: getRouteFromObj(routes[item], path),
      <span class="hljs-attr">name</span>: <span class="hljs-string">""</span>,
    &#125;
  &#125;);
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>调用</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">import</span> routeMapData <span class="hljs-keyword">from</span> <span class="hljs-string">"routeHierarchyMap.json"</span>
getRouteFromObj(routeMapData, <span class="hljs-string">""</span>)
<span class="hljs-comment">// 得到路由如下</span>
===>
[
  &#123;
    <span class="hljs-attr">path</span>: <span class="hljs-string">"/A"</span>,
    <span class="hljs-attr">component</span>: <span class="hljs-function">() =></span> Module,
    <span class="hljs-attr">children</span>: [],
    <span class="hljs-attr">name</span>: <span class="hljs-string">""</span>
  &#125;,
  &#123;
    <span class="hljs-attr">path</span>: <span class="hljs-string">"/B"</span>,
    <span class="hljs-attr">component</span>: <span class="hljs-function">() =></span> Module,
    <span class="hljs-attr">children</span>: [],
    <span class="hljs-attr">name</span>: <span class="hljs-string">""</span>
  &#125;
]
<span class="copy-code-btn">复制代码</span></code></pre>
<p>如果有嵌套关系的话，如：</p>
<pre><code class="hljs language-json copyable" lang="json"><span class="hljs-comment">// routeHierarchyMap.json</span>
&#123;
  <span class="hljs-attr">"/"</span>: &#123;
    <span class="hljs-attr">"A"</span>: &#123;
      <span class="hljs-attr">"B"</span>: &#123;&#125;
    &#125;
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// 得到路由如下</span>
[
  &#123;
    <span class="hljs-attr">path</span>: <span class="hljs-string">"/"</span>,
    <span class="hljs-attr">name</span>: <span class="hljs-string">"Home"</span>,
    <span class="hljs-attr">component</span>: <span class="hljs-function">() =></span> Module,
    <span class="hljs-attr">children</span>: [
      &#123;
        <span class="hljs-attr">path</span>: <span class="hljs-string">"/A"</span>,
        <span class="hljs-attr">component</span>: <span class="hljs-function">() =></span> Module,
        <span class="hljs-attr">children</span>: [
          &#123;
            <span class="hljs-attr">path</span>: <span class="hljs-string">"/B"</span>,
            <span class="hljs-attr">component</span>: <span class="hljs-function">() =></span> Module,
            <span class="hljs-attr">children</span>: [],
            <span class="hljs-attr">name</span>: <span class="hljs-string">""</span>
          &#125;
        ],
        <span class="hljs-attr">name</span>: <span class="hljs-string">""</span>
      &#125;
    ]
  &#125;
]
<span class="copy-code-btn">复制代码</span></code></pre>
<p>再加上可能有一些个性化的路由规则，例如再 mate 中写 needLogin 或者 name值等等。所以就在路由映射的 json 中加入一个 __meta 用来存在个性化的配置，如下:</p>
<pre><code class="hljs language-json copyable" lang="json"><span class="hljs-comment">// routeHierarchyMap.json</span>
&#123;
  <span class="hljs-attr">"/"</span>: &#123;
    <span class="hljs-attr">"__meta"</span>: &#123;
      <span class="hljs-attr">"name"</span>: <span class="hljs-string">"home"</span>
    &#125;
  &#125;,
  <span class="hljs-attr">"A"</span>: &#123;
    <span class="hljs-attr">"__meta"</span>: &#123;
      <span class="hljs-attr">"name"</span>: <span class="hljs-string">"a"</span>,
      <span class="hljs-attr">"meta"</span>: &#123;
        <span class="hljs-attr">"needLogin"</span>: <span class="hljs-literal">true</span>
      &#125;
    &#125;
  &#125;,
  <span class="hljs-attr">"B"</span>: &#123;
    <span class="hljs-attr">"__meta"</span>: &#123;
      <span class="hljs-attr">"name"</span>: <span class="hljs-string">"b"</span>
    &#125;
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>那么解析路由的函数就需要进一步的优化</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// routes 为json文件的路由映射</span>
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">getRouteFromObj</span>(<span class="hljs-params">routes, parentsRoute</span>) </span>&#123;
  <span class="hljs-comment">// 剔除 "__meta" 的 key</span>
  <span class="hljs-keyword">const</span> routesMap = <span class="hljs-built_in">Object</span>.keys(routes).filter(<span class="hljs-function">(<span class="hljs-params">item</span>) =></span> item !== <span class="hljs-string">"__meta"</span>);
  <span class="hljs-keyword">return</span> routesMap.map(<span class="hljs-function">(<span class="hljs-params">item</span>) =></span> &#123;
    <span class="hljs-keyword">const</span> path = <span class="hljs-string">`<span class="hljs-subst">$&#123;parentsRoute.replace(<span class="hljs-regexp">/\/$/</span>, <span class="hljs-string">""</span>)&#125;</span>/<span class="hljs-subst">$&#123;item.replace(<span class="hljs-regexp">/\/$/</span>, <span class="hljs-string">""</span>)&#125;</span>`</span>;
    <span class="hljs-keyword">return</span> &#123;
      path,
      <span class="hljs-attr">component</span>: <span class="hljs-function">() =></span> pageObj[item].component,
      <span class="hljs-attr">children</span>: getRouteFromObj(routes[item], path),
      <span class="hljs-comment">// 放入其他属性</span>
      ...routes[item].__meta,
    &#125;
  &#125;);
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>好的这样子的话已经实现了根据 json 的路由映射进行引入了，但是到此为止，只是对 routes 写法的一种改造，简化了引入这一步，那么如何将这些都变成自动的呢？如果依赖于以上完成的东西进行的话，我能够想到的就是依赖脚本进行自动化的生产页面以及自动化的写入路由映射。就像 hexo 一样，创建一个文章我只需要 <code>hexo create <postname></code> 就可以了。那这样子的话，当创建页面的时候通过 fs 在 pages 文件夹下写入一个模板。在 <code>routeHierarchyMap.json</code> 映射文件中写入对应路由。可以说使用起来没有很方便而且相当的麻烦了。</p>
<h3 data-id="heading-3">改版</h3>
<p>之前的依赖路由映射文件的方式的缺点就是太繁琐，将原本的步骤简化了一小步，但是加大了其使用成本，对开发者来说并不是一个友好的措施。所以参考 nuxt.js 的路由构建规则，通过文件路由的关系来反映真实路由的关系。</p>
<p>解析路由, 同样呢入参都需要提前使用 <code>require.context</code> 来引入模块，下文的参数 <code>modules</code> 就是引入的模块。由于该方式完全依赖于文件路径的解析，所有无法进行个性化的 meta 处理。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">createRoutes</span>(<span class="hljs-params">routeConfig</span>) </span>&#123;
  <span class="hljs-keyword">const</span> &#123; modules, redirect = <span class="hljs-string">"/"</span> &#125; = routeConfig;
  <span class="hljs-comment">// 最后的 routes</span>
  <span class="hljs-keyword">const</span> routes = [];

  <span class="hljs-keyword">const</span> pages = modules.keys();
  <span class="hljs-keyword">for</span> (<span class="hljs-keyword">const</span> page <span class="hljs-keyword">of</span> pages) &#123;
    <span class="hljs-comment">// 解析每一个 vue 文件的路由</span>
    addRoute(routes, page, modules);
  &#125;
  <span class="hljs-comment">// 兜底</span>
  routes.push(&#123;
    <span class="hljs-attr">path</span>: <span class="hljs-string">"/:pathMatch(.*)*"</span>,
    redirect,
  &#125;);

  <span class="hljs-keyword">return</span> routes;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>解析路由的函数</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">addRoute</span>(<span class="hljs-params">routes, route, modules</span>) </span>&#123;
  <span class="hljs-comment">// 当前文件路径</span>
  <span class="hljs-keyword">const</span> routeStr = route
    .replace(<span class="hljs-regexp">/^\.\//</span>, <span class="hljs-string">""</span>)
    .replace(<span class="hljs-regexp">/(\.\w+)$/</span>, <span class="hljs-string">""</span>)
    .replace(<span class="hljs-regexp">/^index/</span>, <span class="hljs-string">"home"</span>)
    .replace(<span class="hljs-regexp">/\/index$/</span>, <span class="hljs-string">""</span>);
  <span class="hljs-comment">// 路由名称</span>
  <span class="hljs-keyword">const</span> name = routeStr.split(<span class="hljs-string">"/"</span>).join(<span class="hljs-string">"-"</span>).replace(<span class="hljs-regexp">/_/g</span>, <span class="hljs-string">""</span>);
  <span class="hljs-keyword">const</span> path = routeStr.startsWith(<span class="hljs-string">"home"</span>)
    ? routeStr.replace(<span class="hljs-regexp">/^(home\/|home)/</span>, <span class="hljs-string">"/"</span>)
    : <span class="hljs-string">"/"</span> + routeStr;
  <span class="hljs-comment">// 父级路由 - findParent 为寻找父级路由的函数</span>
  <span class="hljs-keyword">const</span> target = findParent(<span class="hljs-string">"/"</span> + routeStr, name, routes);
  <span class="hljs-comment">// 父级路由路径</span>
  <span class="hljs-keyword">const</span> targetFullPath = target?.meta?.fullPath || <span class="hljs-string">""</span>;
  <span class="hljs-comment">// 路由路径</span>
  <span class="hljs-keyword">const</span> finalPath = targetFullPath
    ? path.replace(<span class="hljs-built_in">String</span>(targetFullPath), <span class="hljs-string">""</span>)
    : path;
  <span class="hljs-comment">// toProxy 是将路由对象转为 proxy 删除当存在 children 时删除 name 字段</span>
  <span class="hljs-keyword">const</span> targetRoute = toProxy(&#123;
    name,
    <span class="hljs-attr">path</span>: finalPath.replace(<span class="hljs-regexp">/_/g</span>, <span class="hljs-string">":"</span>),
    <span class="hljs-comment">// moduleResolve 路由解析函数</span>
    <span class="hljs-attr">component</span>: moduleResolve(modules(route)),
    <span class="hljs-attr">meta</span>: &#123;
      <span class="hljs-attr">originName</span>: name,
      <span class="hljs-attr">fullPath</span>: path,
    &#125;,
  &#125;);
  <span class="hljs-keyword">if</span> (target) &#123;
    <span class="hljs-keyword">const</span> children = target?.children ?? [];
    target.children = [...children, targetRoute];
    <span class="hljs-keyword">return</span>;
  &#125;
  routes.push(targetRoute);
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<blockquote>
<p>路由解析</p>
</blockquote>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">moduleResolve</span>(<span class="hljs-params"><span class="hljs-built_in">module</span></span>) </span>&#123;
  <span class="hljs-keyword">if</span> (!<span class="hljs-built_in">module</span>.default && <span class="hljs-built_in">module</span> <span class="hljs-keyword">instanceof</span> <span class="hljs-built_in">Promise</span>) <span class="hljs-keyword">return</span> <span class="hljs-function">() =></span> <span class="hljs-built_in">module</span>;
  <span class="hljs-keyword">if</span> (<span class="hljs-built_in">module</span>.default && <span class="hljs-built_in">module</span>.__esModule) <span class="hljs-keyword">return</span> <span class="hljs-built_in">module</span>.default;
  <span class="hljs-keyword">throw</span> <span class="hljs-built_in">Error</span>(<span class="hljs-string">"Routing module resolution failed!"</span>);
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<blockquote>
<p>转为 Proxy</p>
</blockquote>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">toProxy</span>(<span class="hljs-params">target</span>) </span>&#123;
  <span class="hljs-keyword">return</span> <span class="hljs-keyword">new</span> <span class="hljs-built_in">Proxy</span>(target, &#123;
    <span class="hljs-function"><span class="hljs-title">set</span>(<span class="hljs-params">target, p, value</span>)</span> &#123;
      <span class="hljs-keyword">if</span> (p === <span class="hljs-string">"children"</span>) <span class="hljs-keyword">delete</span> target.name;
      <span class="hljs-keyword">return</span> (target[p.toString()] = value);
    &#125;,
  &#125;);
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<blockquote>
<p>寻找父级路由</p>
</blockquote>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">findParent</span>(<span class="hljs-params">route, name, routes, beforeTarget</span>) </span>&#123;
  <span class="hljs-keyword">const</span> target = routes.find(
    <span class="hljs-function">(<span class="hljs-params">item</span>) =></span>
      route.startsWith(item.path) &&
      name.startsWith(<span class="hljs-built_in">String</span>(item?.meta?.originName || <span class="hljs-string">""</span>))
  );
  <span class="hljs-keyword">const</span> routeRest = route.replace(target?.path ?? <span class="hljs-string">""</span>, <span class="hljs-string">""</span>);
  <span class="hljs-keyword">if</span> (target && routeRest.split(<span class="hljs-string">"/"</span>).length === <span class="hljs-number">2</span>) <span class="hljs-keyword">return</span> target;
  <span class="hljs-keyword">if</span> (target && routeRest)
    <span class="hljs-keyword">return</span> findParent(routeRest, name, target.children || [], target);
  <span class="hljs-keyword">if</span> (beforeTarget && routeRest) <span class="hljs-keyword">return</span> beforeTarget;
  <span class="hljs-keyword">return</span> target;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这种方式可以解析出来的路由如下:
<strong>路由方式参考 <a href="https://zh.nuxtjs.org/docs/2.x/features/file-system-routing" target="_blank" rel="nofollow noopener noreferrer">Nuxtjs</a></strong></p>
<blockquote>
<p>基本路由</p>
</blockquote>
<pre><code class="hljs language-js copyable" lang="js">pages/
--| user/
-----| index.vue
-----| one.vue
--| index.vue
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="hljs language-js copyable" lang="js">router: &#123;
  <span class="hljs-attr">routes</span>: [
    &#123;
      <span class="hljs-attr">name</span>: <span class="hljs-string">'index'</span>,
      <span class="hljs-attr">path</span>: <span class="hljs-string">'/'</span>,
      <span class="hljs-attr">component</span>: <span class="hljs-string">'pages/index.vue'</span>
    &#125;,
    &#123;
      <span class="hljs-attr">name</span>: <span class="hljs-string">'user'</span>,
      <span class="hljs-attr">path</span>: <span class="hljs-string">'/user'</span>,
      <span class="hljs-attr">component</span>: <span class="hljs-string">'pages/user/index.vue'</span>
    &#125;,
    &#123;
      <span class="hljs-attr">name</span>: <span class="hljs-string">'user-one'</span>,
      <span class="hljs-attr">path</span>: <span class="hljs-string">'/user/one'</span>,
      <span class="hljs-attr">component</span>: <span class="hljs-string">'pages/user/one.vue'</span>
    &#125;
  ]
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<blockquote>
<p>动态路由</p>
</blockquote>
<p>详见 <a href="https://zh.nuxtjs.org/docs/2.x/features/file-system-routing" target="_blank" rel="nofollow noopener noreferrer">Nuxtjs</a></p>
<blockquote>
<p>嵌套路由</p>
</blockquote>
<p>详见 <a href="https://zh.nuxtjs.org/docs/2.x/features/file-system-routing" target="_blank" rel="nofollow noopener noreferrer">Nuxtjs</a></p>
<blockquote>
<p>动态嵌套路由</p>
</blockquote>
<p>详见 <a href="https://zh.nuxtjs.org/docs/2.x/features/file-system-routing" target="_blank" rel="nofollow noopener noreferrer">Nuxtjs</a></p>
<h3 data-id="heading-4">总结</h3>
<p>以上就是我对 require.context API 的学习以及一些思考，前者是对路由映射对象的遍历、递归生成路由，后者是对文件路径的解析生成路由。二者都是在运行时执行生成路由，可能会对性能上有一定的影响，并且并不适用于所有场景。</p>
<p>初识文章:<br>
<a href="https://juejin.cn/post/6974287967573671966" target="_blank">自动化注册组件，自动化注册路由--懒人福利（vue，react皆适用）</a><br>
参考资料:<br>
<a href="https://zh.nuxtjs.org/" target="_blank" rel="nofollow noopener noreferrer">Nuxtjs</a></p>
<p><a href="https://zhuanlan.zhihu.com/p/59564277" target="_blank" rel="nofollow noopener noreferrer">webpack中require.context的作用</a></p></div>  
</div>
            