
---
title: 'Vue Router详解'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/1d71319672e64f39a122069ca6e5c82b~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Tue, 24 Aug 2021 02:17:40 GMT
thumbnail: 'https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/1d71319672e64f39a122069ca6e5c82b~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>Vue Router 是 vue.js 的官方插件，用来快速实现单页应用。</p>
<h1 data-id="heading-0">单页应用</h1>
<p>SPA（Single Page Application）单页面应用程序，简称单页应用。</p>
<p>单页，指的是网站的 “所有” 功能都在单个页面中进行呈现。</p>
<p>具有代表性的有后台管理系统、移动端、小程序等。</p>
<p>优点：</p>
<ul>
<li>前后端分离开发，提高了开发效率。</li>
<li>业务场景切换时，局部更新结构。</li>
<li>用户体验好，更加接近本地应用。</li>
</ul>
<p>缺点：</p>
<ul>
<li>不利于 SEO。</li>
<li>初次首屏加载速度较慢。</li>
<li>页面复杂度比较高。</li>
</ul>
<h1 data-id="heading-1">前端路由</h1>
<p>前端路由，指的是 URL 与内容间的映射关系。</p>
<p>设置前端路由必备的条件就是：URL、内容、映射关系。</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/1d71319672e64f39a122069ca6e5c82b~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>比如上面的单页每个内容对应一个URL的映射关系就是前端路由。</p>
<p>设置前端路由的两种方式：</p>
<ul>
<li>Hash方式</li>
<li>History方式</li>
</ul>
<h2 data-id="heading-2">Hash方式</h2>
<p>通过 hashchange 事件监听 hash 变化，并进行网页内容更新，就是设置前端路由的Hash方式。</p>
<p>Hash 是 URL 的组成部分，代表符号是<code>#</code>，一般用作锚点在页面内的跳转，当你在看本文时，点击文章目录的各个部分，你会发现地址栏中的 URL 是变化的。这样不会引起整个页面跳转的特性，很适合用作前端路由。</p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">div</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">a</span> <span class="hljs-attr">href</span>=<span class="hljs-string">"#/"</span>></span>首页<span class="hljs-tag"></<span class="hljs-name">a</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">a</span> <span class="hljs-attr">href</span>=<span class="hljs-string">"#/category"</span>></span>分类页<span class="hljs-tag"></<span class="hljs-name">a</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">a</span> <span class="hljs-attr">href</span>=<span class="hljs-string">"#/user"</span>></span>用户页<span class="hljs-tag"></<span class="hljs-name">a</span>></span>
<span class="hljs-tag"></<span class="hljs-name">div</span>></span>
<span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">id</span>=<span class="hljs-string">"container"</span>></span>
  这是首页功能
<span class="hljs-tag"></<span class="hljs-name">div</span>></span>
<span class="hljs-tag"><<span class="hljs-name">script</span>></span><span class="javascript">
  <span class="hljs-comment">// 准备对象，用于封装 hash 功能。</span>
  <span class="hljs-keyword">var</span> router = &#123;
    <span class="hljs-comment">// 路由存储位置： 保存了 url 与 内容处理函数的对应关系</span>
    <span class="hljs-attr">routes</span>: &#123;&#125;,
    <span class="hljs-comment">// 定义路由规则的方法</span>
    <span class="hljs-attr">route</span>: <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params">path, callback</span>) </span>&#123;
      <span class="hljs-built_in">this</span>.routes[path] = callback;
    &#125;,
    <span class="hljs-comment">// 初始化路由的方法</span>
    <span class="hljs-attr">init</span>: <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params"></span>) </span>&#123;
      <span class="hljs-keyword">var</span> that = <span class="hljs-built_in">this</span>;
      <span class="hljs-built_in">window</span>.onhashchange = <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params"></span>) </span>&#123;
        <span class="hljs-comment">// 当 hash 改变，我们需要得到当前新的 hash</span>
        <span class="hljs-keyword">var</span> hash = location.hash.replace(<span class="hljs-string">'#'</span>, <span class="hljs-string">''</span>);
        <span class="hljs-comment">// 根据 hash 触发 routes 中的对应 callback</span>
        that.routes[hash] && that.routes[hash]();
      &#125;;
    &#125;
  &#125;;
  <span class="hljs-keyword">var</span> container = <span class="hljs-built_in">document</span>.getElementById(<span class="hljs-string">'container'</span>);
  <span class="hljs-comment">// 定义路由规则</span>
  router.route(<span class="hljs-string">'/'</span>, <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params"></span>) </span>&#123;
    container.innerHTML = <span class="hljs-string">'这是首页功能'</span>;
  &#125;);
  router.route(<span class="hljs-string">'/category'</span>, <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params"></span>) </span>&#123;
    container.innerHTML = <span class="hljs-string">'这是分类功能'</span>;
  &#125;);
  router.route(<span class="hljs-string">'/user'</span>, <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params"></span>) </span>&#123;
    container.innerHTML = <span class="hljs-string">'这是用户功能'</span>;
  &#125;);
  <span class="hljs-comment">// 初始化路由</span>
  router.init();
</span><span class="hljs-tag"></<span class="hljs-name">script</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>特点总结：</p>
<ul>
<li>Hash 方式兼容性好</li>
<li>地址中具有 <code>#</code> 符号，不太美观</li>
<li>前进后退功能较为繁琐</li>
</ul>
<p>要解决地址不美观、前进后退的问题，则可使用前端路由的另一种方式，History方式。</p>
<h2 data-id="heading-3">History方式</h2>
<p>History 方式采用 HTML5 提供的新功能实现前端路由。</p>
<p>在操作时需要通过 history.pushState() 变更 URL并执行对应操作。</p>
<p>前进后退功能，首先需要在更改 url 时保存路由标记。通过 popstate 事件监听前进后退按钮操作，并检测 state。调用初始化方法监听前进后退操作并处理。</p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">div</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">a</span> <span class="hljs-attr">href</span>=<span class="hljs-string">"/"</span>></span>首页<span class="hljs-tag"></<span class="hljs-name">a</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">a</span> <span class="hljs-attr">href</span>=<span class="hljs-string">"/category"</span>></span>分类<span class="hljs-tag"></<span class="hljs-name">a</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">a</span> <span class="hljs-attr">href</span>=<span class="hljs-string">"/user"</span>></span>用户<span class="hljs-tag"></<span class="hljs-name">a</span>></span>
<span class="hljs-tag"></<span class="hljs-name">div</span>></span>
<span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">id</span>=<span class="hljs-string">"container"</span>></span>
  这是首页功能
<span class="hljs-tag"></<span class="hljs-name">div</span>></span>
<span class="hljs-tag"><<span class="hljs-name">script</span>></span><span class="javascript">
  <span class="hljs-keyword">var</span> router = &#123;
    <span class="hljs-comment">// 存储路由的对象</span>
    <span class="hljs-attr">routes</span>: &#123;&#125;,
    <span class="hljs-comment">// 定义路由的方法</span>
    route (path, callback) &#123;
      <span class="hljs-built_in">this</span>.routes[path] = callback;
    &#125;,
    <span class="hljs-comment">// 用于触发指定的路由操作</span>
    go (path) &#123;
      <span class="hljs-comment">// 更改 url</span>
      history.pushState(&#123; <span class="hljs-attr">path</span>: path &#125;, <span class="hljs-literal">null</span>, path);
      <span class="hljs-comment">// 触发路由对应的回调函数</span>
      <span class="hljs-built_in">this</span>.routes[path] && <span class="hljs-built_in">this</span>.routes[path]();
    &#125;,
    <span class="hljs-comment">// 设置初始化方法，用来检测前进后退按钮的功能</span>
    init () &#123;
      <span class="hljs-keyword">var</span> that = <span class="hljs-built_in">this</span>;
      <span class="hljs-built_in">window</span>.addEventListener(<span class="hljs-string">'popstate'</span>, <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params">e</span>) </span>&#123;
        <span class="hljs-keyword">var</span> path = e.state ? e.state.path : <span class="hljs-string">'/'</span>;
        that.routes[path] && that.routes[path]();
      &#125;);
    &#125;
  &#125;;
  router.init();
  <span class="hljs-comment">// 设置 a 标签的功能</span>
  <span class="hljs-keyword">var</span> links = <span class="hljs-built_in">document</span>.querySelectorAll(<span class="hljs-string">'a'</span>);
  <span class="hljs-keyword">var</span> container = <span class="hljs-built_in">document</span>.querySelector(<span class="hljs-string">'#container'</span>);
  links.forEach(<span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params">ele</span>) </span>&#123;
    ele.addEventListener(<span class="hljs-string">'click'</span>, <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params">event</span>) </span>&#123;
      router.go(<span class="hljs-built_in">this</span>.getAttribute(<span class="hljs-string">'href'</span>));
      event.preventDefault();
    &#125;);
  &#125;);
  <span class="hljs-comment">// 路由规则</span>
  router.route(<span class="hljs-string">'/'</span>, <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params"></span>) </span>&#123;
    container.innerHTML = <span class="hljs-string">'首页功能'</span>;
  &#125;);
  router.route(<span class="hljs-string">'/category'</span>, <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params"></span>) </span>&#123;
    container.innerHTML = <span class="hljs-string">'分类功能'</span>;
  &#125;);
  router.route(<span class="hljs-string">'/user'</span>, <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params"></span>) </span>&#123;
    container.innerHTML = <span class="hljs-string">'用户功能'</span>;
  &#125;);
</span><span class="hljs-tag"></<span class="hljs-name">script</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>优点：</p>
<ul>
<li>地址格式比hash方法美观</li>
<li>实现前进后退比较方便</li>
</ul>
<p>缺点：</p>
<ul>
<li>因为是HTML5功能，兼容性稍差</li>
<li>刷新时需要后端配合处理，防止刷新访问不到路径</li>
</ul>
<h1 data-id="heading-4">Vue Router使用</h1>
<p>Vue Router是 Vue.js 官方的路由管理器，让构建单页面应用变得易如反掌。</p>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Frouter.vuejs.org%2Fzh%2Finstallation.html" target="_blank" rel="nofollow noopener noreferrer" title="https://router.vuejs.org/zh/installation.html" ref="nofollow noopener noreferrer">官方文档</a></p>
<h2 data-id="heading-5">基本使用</h2>
<h3 data-id="heading-6">安装</h3>
<p>方式一、直接下载 / CDN</p>
<ul>
<li>最新版本：<code>https://unpkg.com/vue-router/dist/vue-router.js</code></li>
<li>指定版本：<code>https://unpkg.com/vue-router@3.4.9/dist/vue-router.js</code></li>
</ul>
<p>方式二、npm 方式</p>
<pre><code class="hljs language-shell copyable" lang="shell">npm install vue-router
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-7">引入</h3>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-comment"><!-- 因为vue-router.js是vue.js的插件，所以必须先引入vue.js --></span>
<span class="hljs-tag"><<span class="hljs-name">script</span> <span class="hljs-attr">src</span>=<span class="hljs-string">"lib/vue.js"</span>></span><span class="hljs-tag"></<span class="hljs-name">script</span>></span>
<span class="hljs-tag"><<span class="hljs-name">script</span> <span class="hljs-attr">src</span>=<span class="hljs-string">"lib/vue-router.js"</span>></span><span class="hljs-tag"></<span class="hljs-name">script</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-8">使用</h3>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">id</span>=<span class="hljs-string">"app"</span>></span>
  <span class="hljs-comment"><!-- 设置用于进行路由操作的组件 --></span>
  <span class="hljs-tag"><<span class="hljs-name">router-link</span> <span class="hljs-attr">to</span>=<span class="hljs-string">"/"</span>></span>首页<span class="hljs-tag"></<span class="hljs-name">router-link</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">router-link</span> <span class="hljs-attr">to</span>=<span class="hljs-string">"/user"</span>></span>用户<span class="hljs-tag"></<span class="hljs-name">router-link</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">router-link</span> <span class="hljs-attr">to</span>=<span class="hljs-string">"/category"</span>></span>分类<span class="hljs-tag"></<span class="hljs-name">router-link</span>></span>
  <span class="hljs-comment"><!-- 路由显示区域 --></span>
  <span class="hljs-tag"><<span class="hljs-name">router-view</span>></span><span class="hljs-tag"></<span class="hljs-name">router-view</span>></span>
<span class="hljs-tag"></<span class="hljs-name">div</span>></span>
<span class="hljs-comment"><!-- 因为vue-router.js是vue.js的插件，所以必须先引入vue.js --></span>
<span class="hljs-tag"><<span class="hljs-name">script</span> <span class="hljs-attr">src</span>=<span class="hljs-string">"lib/vue.js"</span>></span><span class="hljs-tag"></<span class="hljs-name">script</span>></span>
<span class="hljs-tag"><<span class="hljs-name">script</span> <span class="hljs-attr">src</span>=<span class="hljs-string">"lib/vue-router.js"</span>></span><span class="hljs-tag"></<span class="hljs-name">script</span>></span>
<span class="hljs-tag"><<span class="hljs-name">script</span>></span><span class="javascript">
  <span class="hljs-comment">// 定义组件</span>
  <span class="hljs-keyword">var</span> Index = &#123;
    <span class="hljs-attr">template</span>: <span class="hljs-string">`<div>首页功能</div>`</span>
  &#125;;
  <span class="hljs-keyword">var</span> User = &#123;
    <span class="hljs-attr">template</span>: <span class="hljs-string">`<div>用户功能</div>`</span>
  &#125;;
  <span class="hljs-keyword">var</span> Category = &#123;
    <span class="hljs-attr">template</span>: <span class="hljs-string">`<div>分类功能</div>`</span>
  &#125;;
  <span class="hljs-comment">// 定义路由规则</span>
  <span class="hljs-keyword">var</span> routes = [
    &#123; <span class="hljs-attr">path</span>: <span class="hljs-string">'/'</span>, <span class="hljs-attr">component</span>: Index &#125;,
    &#123; <span class="hljs-attr">path</span>: <span class="hljs-string">'/user'</span>, <span class="hljs-attr">component</span>: User &#125;,
    &#123; <span class="hljs-attr">path</span>: <span class="hljs-string">'/category'</span>, <span class="hljs-attr">component</span>: Category &#125;
  ];
  <span class="hljs-comment">// 创建 Vue Router 实例</span>
  <span class="hljs-keyword">var</span> router = <span class="hljs-keyword">new</span> VueRouter(&#123;
    routes
  &#125;);
  <span class="hljs-comment">// 创建 Vue 实例，注入 router</span>
  <span class="hljs-keyword">var</span> vm = <span class="hljs-keyword">new</span> Vue(&#123;
    <span class="hljs-attr">el</span>: <span class="hljs-string">'#app'</span>,
    <span class="hljs-comment">// router</span>
  &#125;);
</span><span class="hljs-tag"></<span class="hljs-name">script</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-9">命名视图</h2>
<p>如果导航后，希望同时在同级展示多个视图（组件），这时就需要进行命名视图。</p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">id</span>=<span class="hljs-string">"app"</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">router-link</span> <span class="hljs-attr">to</span>=<span class="hljs-string">"/"</span>></span>首页<span class="hljs-tag"></<span class="hljs-name">router-link</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">router-link</span> <span class="hljs-attr">to</span>=<span class="hljs-string">"/user"</span>></span>用户<span class="hljs-tag"></<span class="hljs-name">router-link</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">router-view</span> <span class="hljs-attr">name</span>=<span class="hljs-string">"sidebar"</span>></span><span class="hljs-tag"></<span class="hljs-name">router-view</span>></span>
  <span class="hljs-comment"><!-- 没有设置 name 的 router-view 默认 name 为 default--></span>
  <span class="hljs-tag"><<span class="hljs-name">router-view</span>></span><span class="hljs-tag"></<span class="hljs-name">router-view</span>></span>
<span class="hljs-tag"></<span class="hljs-name">div</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>需要在路由规则中进行设置</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">// 定义路由规则</span>
<span class="hljs-keyword">var</span> routes = [
  &#123;
    <span class="hljs-attr">path</span>: <span class="hljs-string">'/'</span>,
    <span class="hljs-attr">components</span>: &#123;
      <span class="hljs-comment">// router-view 的 name : 组件配置对象</span>
      <span class="hljs-attr">default</span>: Index,
      <span class="hljs-attr">sidebar</span>: SideBar1
    &#125;
  &#125;,
  &#123;
    <span class="hljs-attr">path</span>: <span class="hljs-string">'/user'</span>,
    <span class="hljs-attr">components</span>: &#123;
      <span class="hljs-attr">default</span>: User,
      <span class="hljs-attr">sidebar</span>: SideBar2
    &#125;
  &#125;
];
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-10">动态路由</h2>
<p>当我们需要将某一类 URL 都映射到同一个组件，就需要使用动态路由。</p>
<p>定义路由规则时，将路径中的某个部分使用 <code>:</code> 进行标记，即可设置为动态路由。</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">// 设置路由规则</span>
<span class="hljs-keyword">var</span> routes = [
  &#123; 
    <span class="hljs-comment">// 表示'/user/1'，'/user/2'，'/user/3'等都指向该路由</span>
    <span class="hljs-attr">path</span>: <span class="hljs-string">'/user/:id'</span>, <span class="hljs-attr">component</span>: User
  &#125;
];
<span class="copy-code-btn">复制代码</span></code></pre>
<p><code>:</code>部分对应的信息称为路径参数，存储在 vm.$route.params 中。</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">// 设置组件 </span>
<span class="hljs-keyword">var</span> User = &#123;
  <span class="hljs-attr">template</span>: <span class="hljs-string">`<div>这是用户 &#123;&#123; $route.params.id &#125;&#125; 的功能</div>`</span>
&#125;;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-11">侦听路由参数</h3>
<p>如果要响应路由的参数变化，可以通过 watch 监听 $route。</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">// 设置组件 </span>
<span class="hljs-keyword">var</span> User = &#123;
  <span class="hljs-attr">template</span>: <span class="hljs-string">`
    <div>
      这是用户 &#123;&#123; $route.params.id &#125;&#125; 的功能
      <input type="text">
    </div>`</span>,
  <span class="hljs-attr">watch</span>: &#123;
    $route (route) &#123;
      <span class="hljs-comment">// console.log(route);</span>
      <span class="hljs-built_in">console</span>.log(route.params.id)
    &#125;
  &#125;
&#125;;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-12">路由传参</h3>
<p>数据可以通过 <code>$route.params</code> 进行接收，但这样会导致组件和数据高度耦合，如果以后组件复用在其他位置、使用父组件或其他组件传递数据，就不好处理。</p>
<p>这时我们需要通过路由的 <code>props</code> 设置数据，并通过组件的 <code>props</code> 接收数据。</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">// 设置路由规则</span>
<span class="hljs-keyword">var</span> routes = [
  &#123;
    <span class="hljs-attr">path</span>: <span class="hljs-string">'/user/:id'</span>,
    <span class="hljs-attr">component</span>: User
  &#125;,
  &#123;
    <span class="hljs-attr">path</span>: <span class="hljs-string">'/category/:id'</span>
    <span class="hljs-attr">component</span>: Category,
    <span class="hljs-attr">props</span>: <span class="hljs-literal">true</span>
  &#125;
];
<span class="copy-code-btn">复制代码</span></code></pre>
<p>定义组件</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">var</span> User = &#123;
  <span class="hljs-attr">template</span>: <span class="hljs-string">`<div>这是用户 &#123;&#123; $route.params.id &#125;&#125; 功能</div>`</span>
&#125;;
<span class="hljs-keyword">var</span> Category = &#123;
  <span class="hljs-attr">props</span>: [<span class="hljs-string">'id'</span>],
  <span class="hljs-attr">template</span>: <span class="hljs-string">`<div>这是分类 &#123;&#123; id &#125;&#125; 功能</div>`</span>
&#125;;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>当包含多个命名视图时，需要将路由的 props 设置为对象。</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">// 设置路由规则</span>
<span class="hljs-keyword">var</span> routes = [
  &#123;
    <span class="hljs-attr">path</span>: <span class="hljs-string">'/user/:id'</span>,
    <span class="hljs-attr">component</span>: User
  &#125;,
  &#123;
    <span class="hljs-attr">path</span>: <span class="hljs-string">'/category/:id'</span>,
    <span class="hljs-attr">components</span>: &#123;
      <span class="hljs-attr">default</span>: Category,
      <span class="hljs-attr">sidebar</span>: SideBar,
      <span class="hljs-attr">sidebar2</span>: SideBar2
    &#125;,
    <span class="hljs-attr">props</span>: &#123;
      <span class="hljs-attr">default</span>: <span class="hljs-literal">true</span>,
      <span class="hljs-attr">sidebar</span>: <span class="hljs-literal">false</span>,
      <span class="hljs-attr">sidebar2</span>: &#123;
        <span class="hljs-comment">// 如果希望设置静态数据，可将 props 中的某个组件对应的选项设置为对象，</span>
        <span class="hljs-comment">// 内部属性会绑定给组件的 props。</span>
        <span class="hljs-attr">a</span>: <span class="hljs-string">'状态1'</span>,
        <span class="hljs-attr">b</span>: <span class="hljs-string">'状态2'</span>
      &#125;
    &#125;
  &#125;
];
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-13">嵌套路由</h2>
<p>实际场景中，路由通常由多层嵌套的组件组合而成，这时需要使用嵌套路由配置。</p>
<p>方法是使用 children 来进行嵌套路由中的子路由设置。</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">var</span> routes = [
  &#123;
    <span class="hljs-attr">path</span>: <span class="hljs-string">'/user'</span>,
    <span class="hljs-attr">component</span>: User,
    <span class="hljs-attr">children</span>: [
      &#123; <span class="hljs-comment">// 表明/user/hobby，path属性值不需要加斜杠/</span>
        <span class="hljs-attr">path</span>: <span class="hljs-string">'hobby'</span>,
        <span class="hljs-attr">component</span>: UserHobby
      &#125;,
      &#123; <span class="hljs-comment">// 表明/user/info</span>
        <span class="hljs-attr">path</span>: <span class="hljs-string">'info'</span>,
        <span class="hljs-attr">component</span>: UserInfo,
        <span class="hljs-attr">children</span>: [
          &#123; <span class="hljs-comment">// 表明/user/info/school</span>
            <span class="hljs-attr">path</span>: <span class="hljs-string">'school'</span>,
            <span class="hljs-attr">component</span>: UserInfoSchool
          &#125;,
        ]
      &#125;
    ]
  &#125;
]
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-14">编程式导航</h2>
<p>编程式导航，指的是通过方法设置导航。</p>
<p><code>router.push()</code> 用来导航到一个新 URL。</p>
<pre><code class="hljs language-javascript copyable" lang="javascript">vm.$router.push(<span class="hljs-string">'/user'</span>)
<span class="hljs-comment">// 对象结构参数</span>
vm.$router.push(&#123;<span class="hljs-attr">path</span>: <span class="hljs-string">'/user'</span>&#125;)
vm.$router.push(&#123;<span class="hljs-attr">path</span>: <span class="hljs-string">'/user/123'</span>&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<p><code><router-link></code> 的 <code>to</code> 属性使用绑定方式时也可使用属性对象结构。Vue在解析的时候会调用<code>router.push()</code>来处理。</p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">router-link</span> <span class="hljs-attr">:to</span>=<span class="hljs-string">"&#123; path: '/user/700' &#125;"</span>></span>用户700<span class="hljs-tag"></<span class="hljs-name">router-link</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-15">命名路由</h3>
<p>通过设置路由时添加 <code>name</code> 属性，来使我们更方便地对路由进行处理。</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">var</span> routes = [
  &#123;
    <span class="hljs-attr">path</span>: <span class="hljs-string">'/user/:id/info/school'</span>,
    <span class="hljs-attr">name</span>: <span class="hljs-string">'school'</span>,
    <span class="hljs-attr">component</span>: School
  &#125;
];
<span class="copy-code-btn">复制代码</span></code></pre>
<p>在 <code>router.push()</code> 中通过 <code>name</code> 导航到对应路由，参数通过 params 设置。</p>
<pre><code class="hljs language-javascript copyable" lang="javascript">vm.$router.push(&#123; <span class="hljs-attr">name</span>: <span class="hljs-string">'school'</span>, <span class="hljs-attr">params</span>: &#123; <span class="hljs-attr">id</span>: <span class="hljs-number">10</span> &#125; &#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>也可以在 <code><router-link></code> 中使用。</p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">router-link</span> <span class="hljs-attr">:to</span>=<span class="hljs-string">"&#123; name: 'school', params: &#123; id: 10 &#125; &#125;"</span>></span>学校10<span class="hljs-tag"></<span class="hljs-name">router-link</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<blockquote>
<p>注意，path 方式和 name 方式不能混用。</p>
</blockquote>
<h2 data-id="heading-16">重定向</h2>
<p>使用 redirect 属性可以对路由进行重定向，用于防止意料之外的情况。</p>
<pre><code class="hljs language-javscript copyable" lang="javscript">var routes = [
  &#123;
    path: '/',
    component: Index
  &#125;,
  &#123;
    path: '/category/:id',
    component: Category
  &#125;,
  //  对不合理的路由访问，进行redirect重定向到根目录
  &#123;
    path: '/category',
    redirect: '/'
  &#125;
];
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-17">别名</h2>
<p>别名是一种路径美化的方式。使用 <code>alias</code> 属性对路径进行美化，使用户看到的地址栏路径简短美观。</p>
<pre><code class="hljs language-html copyable" lang="html">var routes = [
  &#123;
    path: '/user/:id/info/school/:date',
    name: 'school',
    component: School,
    alias: '/:id/:date'
  &#125;
]
<span class="copy-code-btn">复制代码</span></code></pre>
<p>使用</p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">router-link</span> <span class="hljs-attr">:to</span>=<span class="hljs-string">"&#123; name: 'school', params: &#123; id: 10, date: '0612'&#125; &#125;"</span>></span>学校信息<span class="hljs-tag"></<span class="hljs-name">router-link</span>></span>
<span class="hljs-tag"><<span class="hljs-name">router-link</span> <span class="hljs-attr">to</span>=<span class="hljs-string">"/20/1234"</span>></span>学校信息2<span class="hljs-tag"></<span class="hljs-name">router-link</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-18">导航守卫</h2>
<p>用于在每条路由执行之前，进行的操作。实际应用在未登录用户，跳转登录等场景。</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">// 设置导航守卫</span>
router.beforeEach(<span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params">to, <span class="hljs-keyword">from</span>, next</span>) </span>&#123;
  <span class="hljs-comment">// console.log(to, from);</span>
  <span class="hljs-comment">// next() 导航守卫结束，继续下一步导航</span>
  <span class="hljs-comment">// next(false) 终止下一步导航</span>
  <span class="hljs-keyword">if</span> (to.path === <span class="hljs-string">'/user'</span>) &#123;
    <span class="hljs-comment">// 路由跳转</span>
    next(<span class="hljs-string">'/category'</span>);
  &#125; <span class="hljs-keyword">else</span> &#123;
    next();
  &#125;
&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>每个导航守卫需要执行一次<code>next()</code>，相当于导航守卫操作结束，否则无法进入导航路由。</p>
<h2 data-id="heading-19">History模式</h2>
<p>Vue Router 默认使用 Hash 模式，因为兼容性更好，但是也提供了History 模式的设置。</p>
<p>需要通过 Vue Router 实例的 <code>mode</code> 选项来设置，这样 URL 会更加美观，但同样需要后端支持避免问题，防止刷新访问不到路径。</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">var</span> router = <span class="hljs-keyword">new</span> VueRouter(&#123;
  <span class="hljs-attr">mode</span>: <span class="hljs-string">'history'</span>,
  <span class="hljs-attr">routes</span>: [
    &#123; <span class="hljs-attr">path</span>: <span class="hljs-string">'/'</span>, <span class="hljs-attr">component</span>: Index &#125;,
    &#123; <span class="hljs-attr">path</span>: <span class="hljs-string">'/user'</span>, <span class="hljs-attr">component</span>: User &#125;,
    &#123; <span class="hljs-attr">path</span>: <span class="hljs-string">'/category'</span>, <span class="hljs-attr">component</span>: Category &#125;,
  ]
&#125;)
<span class="copy-code-btn">复制代码</span></code></pre></div>  
</div>
            