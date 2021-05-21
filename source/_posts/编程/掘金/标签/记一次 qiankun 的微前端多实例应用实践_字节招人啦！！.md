
---
title: '记一次 qiankun 的微前端多实例应用实践_字节招人啦！！'
categories: 
 - 编程
 - 掘金
 - 标签
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/cfd5ad7fd98044fca506c19e8578aa29~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Wed, 19 May 2021 09:07:13 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/cfd5ad7fd98044fca506c19e8578aa29~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h1 data-id="heading-0">业务背景</h1>
<blockquote>
<p>先看成果，完整的项目在线演示地址 <a href="http://182.48.115.108:8887/microFE-dapeng-base//#/home" target="_blank" rel="nofollow noopener noreferrer">点我查看</a></p>
</blockquote>
<p>大鹏地图可视化大屏项目是一个集<strong>地图应用</strong>和<strong>视图应用</strong>为一体的大屏应用，通过<strong>头部菜单</strong>可切换视图应用，视图应用包括左右两边的内容展示区域，视图应用可以和地图应用通信和交互。项目采用<strong>Vue3搭建</strong>，核心问题在于，3D地图如果使用<strong>iframe方式</strong>集成，那么<strong>性能和用户体验会大幅降低</strong>，为了解决这个问题，我们采用微前端服务框架 <code>qiankun</code> 成功将<strong>地图h5应用和Vue3视图应用</strong>以DOM的方式<strong>嵌入同一个页面</strong>中，这些嵌入的应用就称为<strong>微应用</strong>，下图中的地图应用和视图应用均为微应用。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/cfd5ad7fd98044fca506c19e8578aa29~tplv-k3u1fbpfcp-watermark.image" alt="架构图1.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-1">为什么采用微前端方案</h3>
<ul>
<li>
<p><strong>1.技术栈无关</strong> - 支持接入任意技术栈的应用，支持未来任何技术栈</p>
<ul>
<li>
<p>试想一下，5年前的Angular.js在当时也是非常火的技术栈，许多大型项目都在用，然而技术每年都会迭代更新，每年前端都只会学习使用最新的技术栈，如今的Angular.js已经几乎无人问津，而当初用这在当时很热门的技术栈搭建的项目，现在却已是没人想去改、去优化、去移植、甚至没人会修改的地步。</p>
</li>
</ul>
</li>
<li>
<p><strong>2.可独立开发、测试、部署</strong> - 不同团队或人员维护对应应用，职责拆分，从巨石解耦，加快构建和开发</p>
<ul>
<li>你能想象把百度和谷歌放在一个页面里同时运行吗？甚至是把qq音乐、网易云音乐、酷狗音乐放在一个页面里运行？没错，微前端他实现了，你可以随时把一个应用单独拿出来开发、部署，同时也能在一个基座中将这些单独的应用集成进来组合成新的应用。</li>
</ul>
</li>
<li>
<p><strong>3.增量升级</strong> - 不用打包全部代码更新升级，快速且更有针对性</p>
<ul>
<li>
<p>抛开以前传统应用的整体打包升级方式，微前端方案是将细粒度更小的应用组合成一个大的应用，因此只需要小应用升级即可，好比你有一套房，只需要对其中一个房间进行升级改造，其余房间丝毫不用动。</p>
</li>
</ul>
</li>
<li>
<p><strong>4.独立运行时</strong></p>
<ul>
<li>每个微小应用都拥有自己的独立运行时上下文，也就是说他们的js、css环境是互相不受影响的，比如 <code>A</code> 应用修改了 <code>window.a</code>，<code>B</code> 应用也修改了 <code>window.a</code>，但他们的 <code>window</code> 不是同一个 <code>window</code>对象，故不会造成变量污染。</li>
</ul>
</li>
</ul>
<h1 data-id="heading-2">方案实践</h1>
<h2 data-id="heading-3">基座应用改造</h2>
<p>基座采用vue-cli搭建，子应用也一样用vue-cli搭建，技术栈统一为Vue3，后续接入子应用可以接入其他技术栈的应用。</p>
<h3 data-id="heading-4">安装 qiankun</h3>
<pre><code class="copyable">npm install qiankun -P
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-5">路由配置</h3>
<p>让 <code>/home</code> 作为整个基座和子应用的共同主路由</p>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-comment">// router/index.ts</span>
<span class="hljs-keyword">const</span> Login = <span class="hljs-function">() =></span> <span class="hljs-keyword">import</span>(<span class="hljs-string">'../views/login.vue'</span>);
<span class="hljs-keyword">const</span> Home = <span class="hljs-function">() =></span> <span class="hljs-keyword">import</span>(<span class="hljs-string">'../views/home.vue'</span>);
<span class="hljs-keyword">const</span> NotFound = <span class="hljs-function">() =></span> <span class="hljs-keyword">import</span>(<span class="hljs-string">'@/components/exception/not-found.vue'</span>);

<span class="hljs-comment">// 首次必然要加载的路由</span>
<span class="hljs-keyword">const</span> routes: <span class="hljs-built_in">Array</span><<span class="hljs-built_in">any</span>> = [
  <span class="hljs-comment">// 默认进入首页</span>
  &#123;
    <span class="hljs-attr">path</span>: <span class="hljs-string">''</span>,
    <span class="hljs-attr">redirect</span>: &#123;
      <span class="hljs-attr">name</span>: <span class="hljs-string">'home'</span>,
    &#125;,
  &#125;,
  &#123;
    <span class="hljs-attr">path</span>: <span class="hljs-string">'/'</span>,
    <span class="hljs-attr">redirect</span>: &#123;
      <span class="hljs-attr">name</span>: <span class="hljs-string">'home'</span>,
    &#125;,
  &#125;,
  &#123;
    <span class="hljs-attr">path</span>: <span class="hljs-string">'/home'</span>,
    <span class="hljs-attr">name</span>: <span class="hljs-string">'home'</span>,
    <span class="hljs-attr">component</span>: Home,
  &#125;,
  <span class="hljs-comment">// 全不匹配的情况下，返回404</span>
  &#123;
    <span class="hljs-attr">path</span>: <span class="hljs-string">'/:catchAll(.*)'</span>,
    <span class="hljs-attr">component</span>: NotFound,
  &#125;,
];

<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> routes;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>基座通过 <code>createWebHashHistory</code> 创建 <code>hash</code> 路由，使用 <code>history</code> 和 <code>memory</code> 路由也可以</p>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-comment">// main.ts</span>
<span class="hljs-keyword">import</span> routes <span class="hljs-keyword">from</span> <span class="hljs-string">'./router'</span>;

<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">render</span>(<span class="hljs-params"></span>) </span>&#123;
  router = createRouter(&#123;
    <span class="hljs-attr">history</span>: createWebHashHistory(),
    routes,
  &#125;);
  
  instance.use(router);
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-6">配置导航菜单</h3>
<p>点击菜单要切换视图子应用，因此菜单每个选项都应该包含一个应用信息，包括目录id，名称、入口、挂载容器id，用于切换视图微应用。</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/20354f7441fd48d7b166590eeb379921~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer">
导航目录的数据结构如下，真实场景是通过接口获取的，便于动态修改</p>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-comment">// menu.ts</span>
<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> [&#123;
<span class="hljs-string">"id"</span>: <span class="hljs-number">1</span>, <span class="hljs-comment">// 目录id</span>
<span class="hljs-string">"name"</span>: <span class="hljs-string">"蓝天"</span>, <span class="hljs-comment">// 目录名称</span>
<span class="hljs-string">"app"</span>: &#123;
<span class="hljs-string">"name"</span>: <span class="hljs-string">"vue3-air-app"</span>, <span class="hljs-comment">// 应用名称</span>
<span class="hljs-string">"entry"</span>: &#123;
<span class="hljs-string">"dev"</span>: <span class="hljs-string">"//localhost:8081/"</span>, <span class="hljs-comment">// 开发版应用入口</span>
<span class="hljs-string">"product"</span>: <span class="hljs-string">"http://182.48.115.108:8887/vue3-air-app/"</span> <span class="hljs-comment">// 线上版应用入口</span>
&#125;,
<span class="hljs-string">"container"</span>: <span class="hljs-string">"#microapp"</span> <span class="hljs-comment">// 挂载容器id</span>
&#125;,
<span class="hljs-string">"active"</span>: <span class="hljs-literal">false</span>
&#125;, &#123;
<span class="hljs-string">"id"</span>: <span class="hljs-number">2</span>,
<span class="hljs-string">"name"</span>: <span class="hljs-string">"碧水"</span>,
<span class="hljs-string">"app"</span>: &#123;
<span class="hljs-string">"name"</span>: <span class="hljs-string">"vue3-water-app"</span>,
<span class="hljs-string">"entry"</span>: &#123;
<span class="hljs-string">"dev"</span>: <span class="hljs-string">"//localhost:8082/"</span>,
<span class="hljs-string">"product"</span>: <span class="hljs-string">"http://182.48.115.108:8887/vue3-water-app/"</span>
&#125;,
<span class="hljs-string">"container"</span>: <span class="hljs-string">"#microapp"</span>
&#125;,
<span class="hljs-string">"active"</span>: <span class="hljs-literal">false</span>
&#125;,
……
]
<span class="copy-code-btn">复制代码</span></code></pre>
<p>当菜单切换时，通过 <code>loadMicroApp</code> 加载菜单中的应用信息即可完成视图应用的切换，例如</p>
<pre><code class="hljs language-ts copyable" lang="ts"> <span class="hljs-keyword">import</span> &#123; loadMicroApp &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'qiankun'</span>;
 <span class="hljs-keyword">import</span> MENU <span class="hljs-keyword">from</span> <span class="hljs-string">'./menu'</span>;
 <span class="hljs-keyword">const</span> isProd = process.env.NODE_ENV === <span class="hljs-string">'production'</span>; <span class="hljs-comment">// 是否开发环境</span>
 
 <span class="hljs-comment">// 菜单切换</span>
 <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">onChangeMenu</span>(<span class="hljs-params">id</span>) </span>&#123;
   <span class="hljs-keyword">const</span> currentApp = MENU.find(<span class="hljs-function"><span class="hljs-params">menu</span> =></span> menu.id === id).app;
   loadMicroApp(&#123;
      <span class="hljs-attr">name</span>: currentApp.name,
      <span class="hljs-attr">entry</span>: currentApp.entry[isProd ? <span class="hljs-string">'dev'</span> : <span class="hljs-string">'product'</span>],
      <span class="hljs-attr">container</span>: currentApp.container,
      <span class="hljs-attr">props</span>: &#123;&#125;
   &#125;);
 &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-7">加载微应用</h3>
<p>基座加载微应用有两种方式，一种是通过 <code>registerMicroApps</code> 注册子应用信息包括子应用的<strong>名称(name)、入口(entry)、挂载容器id(container)、路由匹配规则(activeRule)</strong>，注册后的应用会根据浏览器<strong>url的变化来匹配</strong>对应的子应用并加载，第二种是通过 <code>loadMicroApp</code> 来手动加载子应用，也是需要传入子应用的名称、入口、挂载容器id，不过是少了路由匹配规则，他能让你的子应用<strong>立即挂载</strong>，无须匹配任何路由规则，本项目采用的是 <code>loadMicroApp</code>，因为要<strong>同时加载地图应用和视图应用</strong>。</p>
<ul>
<li>loadMicroApp 使用说明
<ul>
<li>作用：通过 <code>qiankun</code> 的<code>loadMicroApp</code> 函数实现在基座中挂载/卸载子应用。</li>
<li>优点：在一个页面中可以同时挂载多个微应用，比如可以同时挂载地图应用和视图应用。</li>
<li>缺点：无法根据路由匹配规则来挂载应用，因为一个路由只能匹配一个应用。</li>
<li>适用场景：当需要在一个页面中同时挂载2个以上子应用，并且子应用的挂载不需要通过路由匹配来实现。</li>
</ul>
</li>
<li>demo演示</li>
</ul>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/7bc7731e920d4bba9a9f2e27fb597e19~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<ul>
<li>代码实现</li>
</ul>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-comment"><!-- template --></span>
<span class="hljs-tag"><<span class="hljs-name">template</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"container"</span>></span>
        <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">id</span>=<span class="hljs-string">"micro-app1"</span>></span><span class="hljs-tag"></<span class="hljs-name">div</span>></span>
        <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">id</span>=<span class="hljs-string">"micro-app2"</span>></span><span class="hljs-tag"></<span class="hljs-name">div</span>></span>
    <span class="hljs-tag"></<span class="hljs-name">div</span>></span>
<span class="hljs-tag"></<span class="hljs-name">template</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="hljs language-ts copyable" lang="ts"> <span class="hljs-comment">// main.ts</span>
 <span class="hljs-keyword">import</span> &#123; loadMicroApp &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'qiankun'</span>;
 loadMicroApp(&#123;
    <span class="hljs-attr">name</span>: <span class="hljs-string">'app1'</span>, <span class="hljs-comment">// 应用唯一名称</span>
    <span class="hljs-attr">entry</span>: <span class="hljs-string">'//localhost:8088/'</span>, <span class="hljs-comment">// 应用唯一HTML入口，可以省略index.html</span>
    <span class="hljs-attr">container</span>: <span class="hljs-string">'#micro-app1'</span>, <span class="hljs-comment">// 基座挂载该应用的容器DOM的id</span>
    <span class="hljs-attr">props</span>: &#123;&#125; <span class="hljs-comment">// 基座传递给微应用的参数，微应用通过mount生命周期函数的参数props获取</span>
 &#125;);
 
 loadMicroApp(&#123;
    <span class="hljs-attr">name</span>: <span class="hljs-string">'app2'</span>,
    <span class="hljs-attr">entry</span>: <span class="hljs-string">'//localhost:8089/'</span>,
    <span class="hljs-attr">container</span>: <span class="hljs-string">'#micro-app2'</span>,
    <span class="hljs-attr">props</span>: &#123;&#125;
 &#125;);
<span class="copy-code-btn">复制代码</span></code></pre>
<blockquote>
<p>注意：loadMicroApp重复挂载name和container一样的应用是会出错的，比如下面操作</p>
</blockquote>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/58ae87139f3941d6ad7b5bde0eaafcb4~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<pre><code class="hljs language-ts copyable" lang="ts"> <span class="hljs-comment">// main.ts</span>
 <span class="hljs-keyword">import</span> &#123; loadMicroApp &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'qiankun'</span>;
 loadMicroApp(&#123;
    <span class="hljs-attr">name</span>: <span class="hljs-string">'app1'</span>, <span class="hljs-comment">// 应用唯一名称</span>
    <span class="hljs-attr">entry</span>: <span class="hljs-string">'//localhost:8088/'</span>, <span class="hljs-comment">// 应用唯一HTML入口，可以省略index.html</span>
    <span class="hljs-attr">container</span>: <span class="hljs-string">'#micro-app1'</span>, <span class="hljs-comment">// 基座挂载该应用的容器DOM的id</span>
    <span class="hljs-attr">props</span>: &#123;&#125; <span class="hljs-comment">// 基座传递给微应用的参数，微应用通过mount生命周期函数的参数props获取</span>
 &#125;);
 
 loadMicroApp(&#123;
    <span class="hljs-attr">name</span>: <span class="hljs-string">'app2'</span>,
    <span class="hljs-attr">entry</span>: <span class="hljs-string">'//localhost:8088/'</span>,
    <span class="hljs-attr">container</span>: <span class="hljs-string">'#micro-app2'</span>,
    <span class="hljs-attr">props</span>: &#123;&#125;
 &#125;);
 
 <span class="hljs-comment">// 这里重复挂载上面的应用后，页面会变成空白</span>
 loadMicroApp(&#123;
    <span class="hljs-attr">name</span>: <span class="hljs-string">'app2'</span>,
    <span class="hljs-attr">entry</span>: <span class="hljs-string">'//localhost:8089/'</span>,
    <span class="hljs-attr">container</span>: <span class="hljs-string">'#micro-app2'</span>,
    <span class="hljs-attr">props</span>: &#123;&#125;
 &#125;);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>解决方案：通过 <code>loadMicroApp</code> 进一步封装了 <code>switchMicroApp</code> 函数，实现根据应用的挂载情况来决定如何切换应用，<strong>首次挂载应用时</strong>直接调用 <code>loadMicroApp</code> 加载应用，<strong>非首次挂载应用时</strong>，则需要先卸载之前挂载的应用后才挂载新的应用。</p>
<pre><code class="hljs language-ts copyable" lang="ts">  <span class="hljs-keyword">import</span> &#123; LoadableApp, loadMicroApp &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'qiankun'</span>;
  
  <span class="hljs-comment">// loadMicroApp的实例对象</span>
  <span class="hljs-keyword">const</span> contentApp: <span class="hljs-built_in">any</span> = ref(<span class="hljs-literal">null</span>);

  <span class="hljs-comment">/**
   * 切换微应用
   * <span class="hljs-doctag">@param </span>runningMicroApp qiankun规定的微应用配置对象
   */</span>
  <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">switchMicroApp</span>(<span class="hljs-params">runningMicroApp: LoadableApp<<span class="hljs-built_in">any</span>></span>) </span>&#123;
    <span class="hljs-keyword">const</span> microApp = runningMicroApp;

    <span class="hljs-comment">// 切换微应用时，先卸载前一个微应用</span>
    <span class="hljs-keyword">if</span> (microApp && contentApp?.value?.getStatus() === <span class="hljs-string">'MOUNTED'</span>) &#123;
      <span class="hljs-comment">// 卸载前一个应用</span>
      contentApp.value.unmount();
      <span class="hljs-comment">// 卸载完前一个应用后紧接着加载新的应用，这里用qiankun的loadMicroApp来加载微应用，返回一个实例，可以通过实例上的unmount方法卸载自身。</span>
      contentApp.value = loadMicroApp(microApp);

      <span class="hljs-keyword">return</span>;
    &#125;

    <span class="hljs-comment">// 如果微应用是初次加载，那么不用先卸载之前挂载的应用直接加载</span>
    contentApp.value = loadMicroApp(microApp);
  &#125;
  
 switchMicroApp(&#123;
    <span class="hljs-attr">name</span>: <span class="hljs-string">'app2'</span>,
    <span class="hljs-attr">entry</span>: <span class="hljs-string">'//localhost:8088/'</span>,
    <span class="hljs-attr">container</span>: <span class="hljs-string">'#micro-app2'</span>,
    <span class="hljs-attr">props</span>: &#123;&#125;
 &#125;);
 
 <span class="hljs-comment">// 这里重复挂载上面的应用，正常加载</span>
 switchMicroApp(&#123;
    <span class="hljs-attr">name</span>: <span class="hljs-string">'app2'</span>,
    <span class="hljs-attr">entry</span>: <span class="hljs-string">'//localhost:8089/'</span>,
    <span class="hljs-attr">container</span>: <span class="hljs-string">'#micro-app2'</span>,
    <span class="hljs-attr">props</span>: &#123;&#125;
 &#125;);
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-8">Layout 组件</h3>
<pre><code class="hljs language-ts copyable" lang="ts"><template>
  <span class="xml"><span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"ths-main"</span>></span>
    <span class="hljs-comment"><!--  导航菜单  --></span>
    <span class="hljs-tag"><<span class="hljs-name">t-header</span> <span class="hljs-attr">:data</span>=<span class="hljs-string">"headerNavs"</span> @<span class="hljs-attr">click</span>=<span class="hljs-string">"onClickHeader"</span>></span><span class="hljs-tag"></<span class="hljs-name">t-header</span>></span>
    
    <span class="hljs-comment"><!--  视图微应用容器  --></span>
    <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"content"</span> <span class="hljs-attr">id</span>=<span class="hljs-string">"microapp"</span>></span><span class="hljs-tag"></<span class="hljs-name">div</span>></span>

    <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"map"</span>></span>
      <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"map-mask"</span>></span><span class="hljs-tag"></<span class="hljs-name">div</span>></span>
      <span class="hljs-comment"><!--  地图微应用容器  --></span>
      <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">id</span>=<span class="hljs-string">"map-app"</span>></span><span class="hljs-tag"></<span class="hljs-name">div</span>></span>
    <span class="hljs-tag"></<span class="hljs-name">div</span>></span>
  <span class="hljs-tag"></<span class="hljs-name">div</span>></span></span>
</template>
<script lang="ts">
export default defineComponent(&#123;
  name: 'Home',
  setup() &#123;
    // 当前头部菜单配置
    const headerNavs = ref<HeaderNavItems>([]);
    // 当前选中的应用id
    const curAppId = ref<number>(0);
    
    // 默认要加载的子应用，地图+首页
    const BASE_MICRO_APPS: BaseMicroApps = &#123;
      map: &#123;
        id: 99,
        name: 'h5-map-app',
        entry: !isProd ? '//localhost:8088/' : `$&#123;webUrl&#125;h5-map-app/`,
        container: '#map-app',
        props: &#123;
          baseUrl,
          experimentalStyleIsolation: true,
        &#125;,
      &#125;,
      home: &#123;
        id: 0,
        name: 'vue3-home-app',
        entry: !isProd ? '//localhost:8090/' : `$&#123;webUrl&#125;vue3-home-app/`,
        container: '#microapp',
        props: &#123;
          baseUrl,
          experimentalStyleIsolation: false,
        &#125;,
      &#125;,
    &#125;;

    /**
     * 点击菜单切换子应用
     * @param id 应用id
     */
    onClickHeader(id: number) &#123;
      // 点击的是当前选中的则返回
      if (curAppId.value === id) &#123;
        return;
      &#125;

      // 当前选中的应用id
      curAppId.value = id;
      // 根据点击的应用id，选中加载哪个应用
      headerNavs.value.forEach((item) => &#123;
        if (item.id === id) &#123;
          switchMicroApp(item.id, &#123;
            ...item.app,
            entry: item.app.entry[isProd ? 'product' : 'dev'],
          &#125;);
        &#125;
      &#125;);
    &#125;
  
    onBeforeMount(() => &#123;
      // 默认加载地图应用
      loadMicroApp(BASE_MICRO_APPS.map);
      // 默认加载首页应用
      loadMicroApp(BASE_MICRO_APPS.home);
    &#125;);
  
    onMounted(() => &#123;
      // 请求导航菜单数据，返回上面‘配置导航菜单’中的MENU对象
      getHeaderMenu('dapeng-header-menu').then((data: HeaderNavItems) => &#123;
        if (isEmpty(data)) &#123;
          headerNavs.value = [];
          return false;
        &#125;
        headerNavs.value = data;
        return true;
      &#125;);
    &#125;);
    
    return &#123;
      onClickHeader,
    &#125;;
  &#125;,
&#125;);
</script>
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-9">刷新路由保存应用状态</h3>
<p>由于通过 <code>loadMicroApp</code> 方式加载的应用<strong>无法匹配路由</strong>，所以当路由变化时就<strong>无法刷新或保持状态</strong>，一旦刷新路由，那么基座中加载的应用都会<strong>重置成首次加载的应用</strong>，例如大气、水环境的应用刷新后都会重新渲染成首页应用。</p>
<ul>
<li>解决方案
<ul>
<li>每个应用对应菜单的一个id，所以通过 <code>localStorage</code> 的方式缓存切换的菜单id，路由刷新后再根据 <code>localStorage</code> 中的id切换对应应用即可。</li>
</ul>
</li>
</ul>
<h3 data-id="heading-10">预加载微应用</h3>
<p>在获取到包含所有子应用信息的菜单数据后，可以<strong>预先请求</strong>其余子应用的<strong>html、js、css</strong>等静态资源，等切换子应用时，可以直接从<strong>缓存</strong>中读取这些静态资源，从而<strong>加快渲染</strong>子应用。</p>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-keyword">import</span> &#123; prefetchApps &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'qiankun'</span>;

getHeaderMenu(<span class="hljs-string">'dapeng-header-menu'</span>).then(<span class="hljs-function">(<span class="hljs-params">data: HeaderNavItems</span>) =></span> &#123;
  <span class="hljs-keyword">if</span> (isEmpty(data)) &#123;
    headerNavs.value = [];
    <span class="hljs-keyword">return</span> <span class="hljs-literal">false</span>;
  &#125;
  headerNavs.value = data;
  <span class="hljs-comment">// 预加载其余微应用</span>
  prefetchApps(headerNavs.value.map(<span class="hljs-function"><span class="hljs-params">nav</span> =></span> (&#123;
    <span class="hljs-attr">name</span>: nav.app.name,
    <span class="hljs-attr">entry</span>: nav.app.entry[isProd ? <span class="hljs-string">'product'</span> : <span class="hljs-string">'dev'</span>],
  &#125;)));
  <span class="hljs-keyword">return</span> <span class="hljs-literal">true</span>;
&#125;);
<span class="copy-code-btn">复制代码</span></code></pre>
<h1 data-id="heading-11">打造qiankun子应用</h1>
<p>我们基于公司 <a href="https://docs.qq.com/doc/DWHVienZQUGZ3QUt3?tdsourcetag=s_macqq_aiomsg&jumpuin=1762696383" target="_blank" rel="nofollow noopener noreferrer">fe-cli</a>  创建一个 Vue3 项目应用，由上述的流程描述，我们知道子应用得向外暴露一系列<strong>生命周期函数</strong>供 qiankun 调用，在 index.js 文件中进行改造：</p>
<h3 data-id="heading-12">增加 public-path.ts 文件</h3>
<p>目录外层添加 <code>public-path.ts</code> 文件，当子应用挂载在主应用下时，如果我们的一些静态资源沿用了 publicPath=/ 的配置，我们拿到的域名将会是主应用域名，这个时候就会造成资源加载出错，好在 Webpack 提供了 <code>__webpack_public_path__</code> 动态更改 <code>publicPath</code> 的修改方式，<code>window.__INJECTED_PUBLIC_PATH_BY_QIANKUN__</code> 等同于 <code>location.host + location.pathname</code> 如 <a href="http://localhost:8081/" target="_blank" rel="nofollow noopener noreferrer">http://localhost:8081/</a> 或 <a href="http://182.48.115.108:8887/vue3-air-home/" target="_blank" rel="nofollow noopener noreferrer">http://182.48.115.108:8887/vue3-air-home/</a> ，如下：</p>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-comment">// public-path.ts</span>
<span class="hljs-keyword">if</span> ((<span class="hljs-built_in">window</span> <span class="hljs-keyword">as</span> <span class="hljs-built_in">any</span>).__POWERED_BY_QIANKUN__) &#123;
  __webpack_public_path__ = (<span class="hljs-built_in">window</span> <span class="hljs-keyword">as</span> <span class="hljs-built_in">any</span>).__INJECTED_PUBLIC_PATH_BY_QIANKUN__;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-13">路由 base 设置</h3>
<p>试想一下，当<strong>基座的路由base</strong>不再是本地的 <code>'/'</code>，而是线上的 <code>'/microFE-dapeng-base/'</code> ，而<strong>子应用的路由base</strong>设置还是'/'，会发生什么，没错，答案是无法匹配到 <code>'/microFE-dapeng-base/'</code> 路由，导致本地子应用路由无法匹配，资源无法加载。注意 <code>createWebHistory</code> 的第一个参数就是设置的路由base，那么通过如下配置即可解决子应用 <code>base</code> 设置问题：</p>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-keyword">const</span> isProd = process.env.NODE_ENV === <span class="hljs-string">'production'</span>; <span class="hljs-comment">// 是否开发环境</span>
<span class="hljs-keyword">const</span> BASE_PREFIX = isProd ? <span class="hljs-string">'/microFE-dapeng-base/'</span> : <span class="hljs-string">'/'</span>; <span class="hljs-comment">// 根据环境设置base</span>
router = createRouter(&#123;
  <span class="hljs-comment">// 根据是否qiankun环境设置base</span>
  <span class="hljs-attr">history</span>: createWebHistory((<span class="hljs-built_in">window</span> <span class="hljs-keyword">as</span> <span class="hljs-built_in">any</span>).__POWERED_BY_QIANKUN__ ? BASE_PREFIX : <span class="hljs-string">'/'</span>),
  routes,
&#125;);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>可见，只要是开发环境，不管子应用是 <code>qiankun</code> 环境下或者独立运行，<code>base</code> 始终都是 <code>'/'</code>，因为本地开发基座应用都不会设置域名二级目录；而线上环境的话，如果子应用是独立运行，那么 <code>base</code> 就是 <code>'/'</code>，相对于当前根路径；如果是 <code>qiankun</code> 环境下，那么 <code>base</code> 就是 <code>'/microFE-dapeng-base/'</code> 相对于基座路由。</p>
<h3 data-id="heading-14">增加生命周期函数</h3>
<p>子应用的入口文件加入生命周期函数初始化，方便主应用调用资源完成后按应用名称调用子应用的生命周期</p>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-comment">/**
 * bootstrap 只会在微应用初始化的时候调用一次，下次微应用重新进入时会直接调用 mount 钩子，不会再重复触发 bootstrap。
 * 通常我们可以在这里做一些全局变量的初始化，比如不会在 unmount 阶段被销毁的应用级别的缓存等。
 */</span>
<span class="hljs-keyword">export</span> <span class="hljs-keyword">async</span> <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">bootstrap</span>(<span class="hljs-params"></span>) </span>&#123;
  <span class="hljs-built_in">console</span>.log(<span class="hljs-string">"bootstraped"</span>);
&#125;

<span class="hljs-comment">/**
 * 应用每次进入都会调用 mount 方法，通常我们在这里触发应用的渲染方法
 */</span>
<span class="hljs-keyword">export</span> <span class="hljs-keyword">async</span> <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">mount</span>(<span class="hljs-params">props</span>) </span>&#123;
  <span class="hljs-built_in">console</span>.log(<span class="hljs-string">"mount"</span>, props);
  render(props); <span class="hljs-comment">// 执行createApp创建instance并挂载子应用DOM</span>
&#125;

<span class="hljs-comment">/**
 * 应用每次切出/卸载 会调用的方法，通常在这里我们会卸载微应用的应用实例
 */</span>
<span class="hljs-keyword">export</span> <span class="hljs-keyword">async</span> <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">unmount</span>(<span class="hljs-params"></span>) </span>&#123;
  <span class="hljs-built_in">console</span>.log(<span class="hljs-string">"unmount"</span>);
  instance.unmount();
  instance._container.innerHTML = <span class="hljs-string">''</span>;
  instance = <span class="hljs-literal">null</span>;
  router = <span class="hljs-literal">null</span>;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<blockquote>
<p>注意：所有的生明周期函数都必须是 Promise</p>
</blockquote>
<h3 data-id="heading-15">子应用独立运行配置</h3>
<p>在上述的生命周期mount钩子中挂载了子应用的实例的DOM，那么当子应用要单独运行，是不是也要挂载一次实例的DOM呢？通过 <code>!window.__POWERED_BY_QIANKUN__</code> 判断如果不是qiankun环境的话，就立即挂载实例的DOM。</p>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">render</span>(<span class="hljs-params">props</span>) </span>&#123;
    <span class="hljs-keyword">const</span> container = props.container || <span class="hljs-literal">null</span>;
    <span class="hljs-keyword">const</span> isProd = process.env.NODE_ENV === <span class="hljs-string">'production'</span>; <span class="hljs-comment">// 是否开发环境</span>
    <span class="hljs-keyword">const</span> BASE_PREFIX = isProd ? <span class="hljs-string">'/microFE-dapeng-base/'</span> : <span class="hljs-string">'/'</span>; <span class="hljs-comment">// 根据环境设置base</span>
    router = createRouter(&#123;
      <span class="hljs-attr">history</span>: createWebHistory(<span class="hljs-built_in">window</span>.__POWERED_BY_QIANKUN__ ? BASE_PREFIX : <span class="hljs-string">'/'</span>),
      routes,
    &#125;);
    instance = createApp(App);
    instance.use(router);
    instance.mount(container ? container.querySelector(<span class="hljs-string">'#app'</span>) : <span class="hljs-string">'#app'</span>);
&#125;

<span class="hljs-comment">// 当不是qiankun环境时候，立即执行render挂载DOM</span>
<span class="hljs-keyword">if</span> (!<span class="hljs-built_in">window</span>.__POWERED_BY_QIANKUN__) &#123;
  render();
&#125;

<span class="hljs-comment">// 生命周期钩子函数</span>
<span class="hljs-keyword">export</span> <span class="hljs-keyword">async</span> <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">bootstrap</span>(<span class="hljs-params"></span>) </span>&#123;...&#125;
<span class="hljs-comment">// 当是qiankun环境时候，才会在父容器挂载完成后执行mount钩子，然后执行render挂载DOM</span>
<span class="hljs-keyword">export</span> <span class="hljs-keyword">async</span> <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">mount</span>(<span class="hljs-params">props</span>) </span>&#123; render(props) &#125;
<span class="hljs-keyword">export</span> <span class="hljs-keyword">async</span> <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">unmount</span>(<span class="hljs-params"></span>) </span>&#123;...&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-16"><span id="user-content-package">修改打包配置</span></h3>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">isProd</span>(<span class="hljs-params"></span>) </span>&#123;
  <span class="hljs-keyword">return</span> process.env.NODE_ENV === <span class="hljs-string">'production'</span>;
&#125;
<span class="hljs-comment">// 图片公用地址前缀，请配置成微应用部署在三方服务器的完整根地址</span>
<span class="hljs-keyword">const</span> publicPath = isProd() ? <span class="hljs-string">`http://182.48.115.108:8887/<span class="hljs-subst">$&#123;name&#125;</span>/`</span> : <span class="hljs-string">`http://localhost:<span class="hljs-subst">$&#123;port&#125;</span>`</span>;

<span class="hljs-built_in">module</span>.exports = &#123;
  <span class="hljs-comment">// 本地服务配置</span>
  <span class="hljs-attr">devServer</span>: &#123;
    <span class="hljs-attr">host</span>: <span class="hljs-string">'localhost'</span>,
    <span class="hljs-attr">hot</span>: <span class="hljs-literal">true</span>,
    <span class="hljs-attr">disableHostCheck</span>: <span class="hljs-literal">true</span>,
    port,
    <span class="hljs-attr">overlay</span>: &#123;
      <span class="hljs-attr">warnings</span>: <span class="hljs-literal">false</span>,
      <span class="hljs-attr">errors</span>: <span class="hljs-literal">true</span>,
    &#125;,
    <span class="hljs-attr">headers</span>: &#123;
       <span class="hljs-comment">// 设置本地资源允许跨域，部署后服务端也需要设置允许跨域，因为基座是通过 fetch 来拉取子应用资源的，跨域才能拉</span>
      <span class="hljs-string">'Access-Control-Allow-Origin'</span>: <span class="hljs-string">'*'</span>,
    &#125;,
  &#125;,
  publicPath, <span class="hljs-comment">// 注意这里很重要，设置所有静态资源的加载路径为绝对路径</span>
  <span class="hljs-attr">configureWebpack</span>: <span class="hljs-function">(<span class="hljs-params">config</span>) =></span> &#123;
      <span class="hljs-keyword">return</span> &#123;
          <span class="hljs-attr">output</span>: &#123;
            <span class="hljs-comment">// 微应用的包名，这里与主应用中注册的微应用名称一致，比如name = 'vue3-home-app'</span>
            <span class="hljs-attr">library</span>: <span class="hljs-string">`<span class="hljs-subst">$&#123;name&#125;</span>-[name]`</span>,
            <span class="hljs-comment">// 将你的 library 暴露为所有的模块定义下都可运行的方式</span>
            <span class="hljs-attr">libraryTarget</span>: <span class="hljs-string">'umd'</span>,
            <span class="hljs-comment">// 按需加载相关，设置为 webpackJsonp_VueMicroApp 即可</span>
            <span class="hljs-attr">jsonpFunction</span>: <span class="hljs-string">'webpackJsonp_VueMicroApp'</span>,
          &#125;,
      &#125;
  &#125;,
  <span class="hljs-attr">chainWebpack</span>: <span class="hljs-function">(<span class="hljs-params">config</span>) =></span> &#123;
    <span class="hljs-comment">// 替换打包后的字体资源地址为绝对地址或压缩成base64</span>
    config.module.rule(<span class="hljs-string">'fonts'</span>)
      .use(<span class="hljs-string">'url-loader'</span>)
      .loader(<span class="hljs-string">'url-loader'</span>)
      .options(&#123;
        <span class="hljs-attr">limit</span>: <span class="hljs-number">4096</span>, <span class="hljs-comment">// 小于4kb将会被打包成 base64</span>
        <span class="hljs-attr">fallback</span>: &#123;
          <span class="hljs-attr">loader</span>: <span class="hljs-string">'file-loader'</span>,
          <span class="hljs-attr">options</span>: &#123;
            <span class="hljs-attr">name</span>: <span class="hljs-string">'fonts/[name].[hash:8].[ext]'</span>,
            <span class="hljs-comment">// 将图片相对地址替换为本地或线上完整地址，防止相对地址会相对于基座地址来查找静态资源</span>
            <span class="hljs-comment">// 如 'http://localhost:8082/'或'http://182.48.115.108:8887/vue3-air-app/'</span>
            publicPath,
          &#125;,
        &#125;,
      &#125;)
      .end();
    <span class="hljs-comment">// 替换打包后的图片资源地址为绝对地址或压缩成base64</span>
    config.module.rule(<span class="hljs-string">'images'</span>)
      .use(<span class="hljs-string">'url-loader'</span>)
      .loader(<span class="hljs-string">'url-loader'</span>)
      .options(&#123;
        <span class="hljs-attr">limit</span>: <span class="hljs-number">4096</span>, <span class="hljs-comment">// 小于4kb将会被打包成 base64</span>
        <span class="hljs-attr">fallback</span>: &#123;
          <span class="hljs-attr">loader</span>: <span class="hljs-string">'file-loader'</span>,
          <span class="hljs-attr">options</span>: &#123;
            <span class="hljs-attr">name</span>: <span class="hljs-string">'img/[name].[hash:8].[ext]'</span>,
            <span class="hljs-comment">// 同上</span>
            publicPath,
          &#125;,
        &#125;,
      &#125;);
  &#125;,
&#125;;
<span class="copy-code-btn">复制代码</span></code></pre>
<blockquote>
<p>注意：配置的修改为了达到三个目的，一个是暴露生命周期函数给主应用调用，第二点是允许跨域访问，第三点是将图片等静态资源的相对路径地址修改为绝对路径从而解决资源相对于基座路径的问题，修改的注意点可以参考代码的注释。</p>
</blockquote>
<ul>
<li><strong>暴露生命周期</strong>： UMD 可以让 qiankun 按应用名称匹配到生命周期函数</li>
<li><strong>跨域配置</strong>： 主应用是通过 Fetch 获取资源，所以为了解决跨域问题，必须设置允许跨域访问</li>
</ul>
<h1 data-id="heading-17">项目中遇到的问题</h1>
<h3 data-id="heading-18"><strong>1、子应用未成功加载</strong></h3>
<p>如果项目启动完成后，发现子应用系统没有加载，我们应该打开控制台分析原因：</p>
<ul>
<li><strong>控制台无报错</strong>：子应用未加载，检查子应用导出的生命周期mount中是否调用了render挂载DOM</li>
<li><strong><a href="https://qiankun.umijs.org/faq#application-died-in-status-not_mounted-target-container-with-container-not-existed-after-xxx-mounted" target="_blank" rel="nofollow noopener noreferrer">挂载容器未找到</a></strong>：检查容器 DIV 是否在 <code>loadMicroApp</code> 时一定存在，如不能保证需设法在 DOM 挂载后执行。</li>
</ul>
<h3 data-id="heading-19"><strong>2、基座应用路由模式</strong></h3>
<p>基座路由配置</p>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-built_in">exports</span> routes = [&#123;
    <span class="hljs-attr">path</span>: <span class="hljs-string">'/home'</span>,
    <span class="hljs-attr">name</span>: <span class="hljs-string">'home'</span>,
    <span class="hljs-attr">component</span>: Home,
  &#125;];
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>基座应用项目是 hash 模式路由，子路由是 history 模式</li>
</ul>
<p>子应用配置路由</p>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-comment">// routes.ts</span>
<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> [
  &#123;
    <span class="hljs-attr">path</span>: <span class="hljs-string">'/'</span>, <span class="hljs-comment">// 这里必须是 '/'，不能变更pathname</span>
    <span class="hljs-attr">name</span>: <span class="hljs-string">'Home'</span>,
    <span class="hljs-attr">component</span>: <span class="hljs-function">() =></span> <span class="hljs-keyword">import</span>(<span class="hljs-string">'@/views/home.vue'</span>),
  &#125;,
];

<span class="hljs-comment">// main.ts</span>
router = createRouter(&#123;
    <span class="hljs-comment">// history 模式</span>
    <span class="hljs-attr">history</span>: createWebHistory(<span class="hljs-built_in">window</span>.__POWERED_BY_QIANKUN__ ? BASE_PREFIX : <span class="hljs-string">'/'</span>),
    routes,
  &#125;);
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>基座应用项目是 hash 模式路由，子路由是 hash 模式</li>
</ul>
<p>子应用配置路由</p>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-comment">// routes.ts</span>
<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> [
  &#123;
    <span class="hljs-attr">path</span>: <span class="hljs-string">'/home'</span>, <span class="hljs-comment">// 这里必须跟基座保持一致</span>
    <span class="hljs-attr">name</span>: <span class="hljs-string">'Home'</span>,
    <span class="hljs-attr">component</span>: <span class="hljs-function">() =></span> <span class="hljs-keyword">import</span>(<span class="hljs-string">'@/views/home.vue'</span>),
  &#125;,
];

<span class="hljs-comment">// main.ts</span>
router = createRouter(&#123;
    <span class="hljs-comment">// hash 模式</span>
    <span class="hljs-attr">history</span>: createWebHashHistory(<span class="hljs-built_in">window</span>.__POWERED_BY_QIANKUN__ ? BASE_PREFIX : <span class="hljs-string">'/'</span>),
    routes,
  &#125;);
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-20"><strong>3、CSS 样式错乱</strong></h3>
<p>由于默认情况下 <code>qiankun</code> 并不会开启 <code>CSS</code> 沙箱进行样式隔离，当主应用和子应用产生样式错乱时，有两种样式隔离配置：</p>
<ul>
<li>strictStyleIsolation - boolean
<ul>
<li>这个时候会用 <code>Shadow Dom</code> 节点包裹子应用，相信大家看到这个也很熟悉，和 <code>Ionic</code> 中组件的样式隔离方案一致。</li>
</ul>
<pre><code class="hljs language-ts copyable" lang="ts">loadMicroApp(microApp, &#123;
  <span class="hljs-attr">sandbox</span>: &#123;
    <span class="hljs-attr">strictStyleIsolation</span>: <span class="hljs-literal">true</span>,
  &#125;,
&#125;);
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>优点
<ul>
<li>完全隔离CSS样式</li>
</ul>
</li>
<li>缺点
<ul>
<li>在使用一些弹窗组件的时候（弹窗很多情况下都是默认添加到了 document.body ）这个时候它就跳过了阴影边界，跑到了主应用里面，样式就丢了</li>
</ul>
</li>
</ul>
</li>
<li>experimentalStyleIsolation - boolean
<ul>
<li>会在运行时劫持应用style的规则，并且添加前缀来控制隔离，比如 <code>.title</code>，劫持后输出 <code>div[data-qiankun-app] .title</code></li>
</ul>
<pre><code class="hljs language-ts copyable" lang="ts">loadMicroApp(microApp, &#123;
  <span class="hljs-attr">sandbox</span>: &#123;
    <span class="hljs-attr">experimentalStyleIsolation</span>: <span class="hljs-literal">true</span>,
  &#125;,
&#125;);
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>优点
<ul>
<li>支持大部分样式隔离需求</li>
<li>解决了 Shadow DOM 方案导致的丢失根节点问题</li>
</ul>
</li>
<li>缺点
<ul>
<li>运行时重新加载样式，会有一定性能损耗</li>
</ul>
</li>
</ul>
</li>
</ul>
<p>具体如何样式隔离的原理可以参考 <a href="https://juejin.cn/post/6919068660233895944#heading-14" target="_blank">这篇文章</a></p>
<h3 data-id="heading-21"><strong>4、H5 微应用静态资源404</strong></h3>
<p>h5子应用如果没有通过webpack等工具打包，没有在打包的时候将静态资源相对地址<a href="https://juejin.cn/post/6964047353128943630#package">替换成publicPath</a>，那么还是那个问题，应用被转换成DOM后append到基座html中，相对路径其实已经从原来应用的url变为了当前页面也就是基座的url，通过设置 <code>head</code> 中的 <code>base</code> 标签 <code>href</code> 属性解决相对路径问题：</p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-comment"><!-- 本地 --></span>
<span class="hljs-tag"><<span class="hljs-name">base</span> <span class="hljs-attr">href</span>=<span class="hljs-string">"http://localhost:8088/"</span>></span>
<span class="hljs-comment"><!-- 线上 --></span>
<span class="hljs-tag"><<span class="hljs-name">base</span> <span class="hljs-attr">href</span>=<span class="hljs-string">"http://182.48.115.108:8887/h5-map-app/"</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-22"><strong>5、异步加载的js中再异步加载了其他js，loadMicroApp加载的应用全局作用域会错乱</strong></h3>
<p><code>qiankun</code> 在加载 <code>js</code> 时，会根据加载的 <code>js</code> 来匹配对应所属的微应用，并<strong>开启对应沙箱隔离</strong> <code>js</code>，如果异步加载的 <code>js</code> 中再次异步加载了 <code>js</code>，那么最后异步加载的 <code>js</code> 对应的应用就<strong>无法正确匹配到属于哪个微应用</strong>，就会造成<strong>无法开启正确的沙箱进行隔离</strong>，导致 <code>js</code> 全局作用域污染。</p>
<ul>
<li>解决方案
<ul>
<li>先只加载有多重异步引入 <code>js</code> 的应用，让所有异步的 <code>js</code> 只能匹配该应用的沙箱，加载完后再通知基座开始加载其余正常应用。</li>
</ul>
</li>
</ul>
<h3 data-id="heading-23"><strong>6、配置线上和本地环境的publicPath设置资源加载的默认路径</strong></h3>
<p>微应用不能使用相对路径的资源，因此需设置资源加载路径为绝对路径，并且区分线上和本地环境。</p>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-keyword">const</span> isProd = process.env.NODE_ENV === <span class="hljs-string">'production'</span>;
<span class="hljs-keyword">const</span> publicPath = isProd ? <span class="hljs-string">`http://182.48.115.108:8887/<span class="hljs-subst">$&#123;name&#125;</span>/`</span> : <span class="hljs-string">`http://localhost:<span class="hljs-subst">$&#123;port&#125;</span>`</span>;
 
 <span class="hljs-comment">// vue.config.js</span>
 <span class="hljs-built_in">module</span>.exports = &#123;
  <span class="hljs-comment">// ...</span>
  publicPath,
&#125;

<span class="hljs-comment">// webpack</span>
<span class="hljs-built_in">module</span>.exports = &#123;
  <span class="hljs-comment">// ...</span>
  <span class="hljs-attr">assetsPublicPath</span>: publicPath,
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>如果需要本地打包后能正常访问应用，需将 <code>isProd</code> 手动改为 <code>false</code></p>
<h3 data-id="heading-24"><strong>7.线上子应用单独运行需修改路由path</strong></h3>
<p>子应用打包部署后，为了能让子应用独立运行，则需要根据子应用部署地址的 <code>path</code> 来设置路由 <code>path</code>，比如子应用部署地址是 <code>http://182.48.115.108:8887/vue3-air-app/</code>，那么子应用路由的 <code>path</code> 就应该变成 <code>'/vue3-air-app' + '/'</code> 而不是 <code>'/'</code>，为了统一，访问地址的 <code>path</code> 就是应用的名称 <code>packageName</code></p>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-keyword">const</span> packageName = <span class="hljs-built_in">require</span>(<span class="hljs-string">'../../package.json'</span>).name;
<span class="hljs-keyword">const</span> basePath = <span class="hljs-string">'/'</span>;
<span class="hljs-comment">// routes.ts</span>
<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> [
  &#123;
    <span class="hljs-comment">// 非qiankun环境即独立运行并且是正式版本的应用的 path 要加上应用名称，否则无法独立运行</span>
    <span class="hljs-attr">path</span>: !(<span class="hljs-built_in">window</span> <span class="hljs-keyword">as</span> <span class="hljs-built_in">any</span>).__POWERED_BY_QIANKUN__ && process.env.NODE_ENV === <span class="hljs-string">'production'</span> ? <span class="hljs-string">`/<span class="hljs-subst">$&#123;packageName&#125;</span><span class="hljs-subst">$&#123;basePath&#125;</span>`</span> : basePath;,
    name: <span class="hljs-string">'Home'</span>,
    <span class="hljs-attr">component</span>: <span class="hljs-function">() =></span> <span class="hljs-keyword">import</span>(<span class="hljs-string">'@/views/home.vue'</span>),
  &#125;,
];
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-25"><strong>8、 另外，在接入过程中，总结了几个需要注意的点</strong></h3>
<ul>
<li>虽然 <code>qiankun</code> 支持 <code>jQuery</code>，但对多页应用的老项目接入不是很友好，需要每个页面都修改，成本也很高，这类老项目接入还是比较推荐 <code>iframe</code> ；</li>
<li>因为 <code>qiankun</code> 的方式，是通过 <code>HTML-Entry</code> 抽取 <code>JS</code> 文件和 <code>DOM</code> 结构的，实际上和主应用共用的是同一个 <code>Document</code>，如果子应用和主应用同时定义了相同事件，会互相影响，如，用 <code>onClick</code> 或 <code>addEventListener</code> 给 <code><body></code> 添加了一个点击事件，<code>JS</code> 沙箱并不能消除它的影响，还得靠平时的代码规范</li>
<li>部署上有点繁琐，需要手动解决跨域问题</li>
<li>在 <code>vue</code> 中使用图片得用 <strong>require(相对/绝对路径).default</strong> 获取图片路径</li>
<li>在子应用 <code>js</code> 中通过 <code>function</code> 或者 <code>var</code> 声明在 <code>window</code> 上的全局变量无法识别，原因在于 <code>Proxy</code> 沙箱将 <code>window</code> 替换成 <code>Proxy</code> 实例了，所以声明的变量无法保存在 <code>proxy</code> 对象上，如果要使用全局变量，可以用 <code>(function(global)&#123;global.obj = &#123;&#125;, global.fn = function() &#123;&#125;&#125;(window))</code></li>
<li>像地图依赖的的三方js有很多不确定性，比如引入了 <code>CesiumJs</code> 和其他 <code>qiankun</code> 无法完美支持的js库等，以及其中引入了很多静态资源相对地址都无法在打包时替换为绝对地址，所以为了让这些三方js库能顺利集成，最好的方式是将他们在基座的 <code>index.html</code> 中加载，这样 <code>qiankun</code> 就不会劫持三方引入的js从而发生错误了。</li>
<li>切换子应用前需要先卸载前一个子应用，否则会报错</li>
</ul>
<pre><code class="hljs language-ts copyable" lang="ts">app1 = loadMicroApp();
app1.unmount;
app2 = loadMicroApp();
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>无法兼容 IE，在基座的 main.ts 中引入如下依赖解决</li>
</ul>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-keyword">import</span> <span class="hljs-string">'whatwg-fetch'</span>;
<span class="hljs-keyword">import</span> <span class="hljs-string">'custom-event-polyfill'</span>;
<span class="hljs-keyword">import</span> <span class="hljs-string">'core-js/stable/promise'</span>;
<span class="hljs-keyword">import</span> <span class="hljs-string">'core-js/stable/symbol'</span>;
<span class="hljs-keyword">import</span> <span class="hljs-string">'core-js/stable/string/starts-with'</span>;
<span class="hljs-keyword">import</span> <span class="hljs-string">'core-js/web/url'</span>;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-26"><strong>8、未来可能需要考虑一些问题</strong></h3>
<ul>
<li>自动化注入：每一个子应用改造的过程其实也是挺麻烦的事情，但是其实大多的工作都是标准化流程，在考虑通过脚本自动注册子应用，实现自动化</li>
</ul>
<h1 data-id="heading-27">总结</h1>
<p>其实写下来整个项目，最大的感受 qiankun 的开箱可用性非常强，需要更改的项目配置基本很少，当然遇到的一些坑点也肯定是踩过才能更清晰。</p>
<p>如果文章有什么问题或者错误，欢迎指正交流，谢谢！</p>
<h1 data-id="heading-28">彩蛋：字节跳动内推-成都-2021.05</h1>
<h3 data-id="heading-29">字节跳动抖音社交团队招人拉！！！</h3>
<h3 data-id="heading-30">为什么来字节？只要NB，干完活随时可以下班！只要你想，你可以干你喜欢的有挑战的事！只要有意见，各种反馈群，值班号，onCall随时找人提！</h3>
<p><strong>职位介绍</strong></p>
<ul>
<li>前端开发工程师 - 抖音 - <strong>经验不限</strong>只要够<strong>NB</strong></li>
</ul>
<ol>
<li>负责抖音社交、本地生活前端开发工作，包括产品端核心功能、活动等开发；</li>
<li>落实和推进产品规划及需求，保障产品功能高效高质迭代；</li>
<li>关注产品流程和产品体验，创造极致的用户体验；</li>
<li>参与制定技术规划，并保障开发体验、研发效率、系统性能和安全。</li>
</ol>
<p><strong>职位要求</strong></p>
<p>1.本科及以上学历，计算机、通信和电子信息科学、数学等相关专业优先；
2.具备扎实的计算机和前端基础，具有良好的逻辑理解能力和学习能力；
3.熟练前端基础技术以及常用的开发框架；
4.拥有较好的交互设计及用户体验意识；
5.积极乐观，责任心强，具备良好的服务意识及沟通协作能力；</p>
<p>有意者简历发邮箱：<a href="mailto:lilin.verygood@bytedance.com">lilin.verygood@bytedance.com</a></p>
<p>简历名称为：<strong>简历-抖音社交前端-姓名-微信号.pdf</strong></p>
<p>每个发送简历的人我都会提供<strong>面试准备建议</strong>和<strong>简历修改建议</strong>，简历通过者我会直接找到你发送<strong>内推码</strong>，没通过会给予<strong>修改建议</strong>，内推好处是每个<strong>面试环节进度都清清楚楚</strong>，能找到直接对接人跟进进度，还在等什么，机会永远不会等人，投了简历没过也能进入<strong>人才库</strong>，增大下次面试的机会！我就是这样进入字节的，不要怂干就完事！！</p></div>  
</div>
            