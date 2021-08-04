
---
title: 'vue3 + vite 项目搭建 - 引入vue-router及实现权限控制'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=7892'
author: 掘金
comments: false
date: Wed, 04 Aug 2021 00:52:02 GMT
thumbnail: 'https://picsum.photos/400/300?random=7892'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h4 data-id="heading-0">一般后台管理系统都会有管理员和普通用户的区分，所以要做权限控制</h4>
<h3 data-id="heading-1">思路</h3>
<ol>
<li>创建公用页面login，可以让用户进行登录操作，根据用户信息对应的身份，匹配不同的权限模块</li>
<li>在路由前置钩子进行身份验证拦截，将拦截条件分为 白名单（不做拦截）、登录态未登录、登录态已登陆</li>
<li>路由注册分为两步，公用页面直接注册，权限路由根据登录用户的身份来注册</li>
<li>解决路由层级过深会导致keep-alive不缓存问题</li>
</ol>
<h3 data-id="heading-2">实现</h3>
<ol>
<li>安装依赖</li>
</ol>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-string">"dependencies"</span>: &#123;
<span class="hljs-string">"nprogress"</span>: <span class="hljs-string">"^0.2.0"</span>,
    <span class="hljs-string">"vue-router"</span>: <span class="hljs-string">"^4.0.6"</span>
  &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<ol start="2">
<li>在src目录下创建配置文件config，统一管理一些设置信息 新建setting.config.js</li>
</ol>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">/** src/config/setting.config.js */</span>
<span class="hljs-comment">// 项目名称</span>
<span class="hljs-keyword">export</span> <span class="hljs-keyword">const</span> title: string = <span class="hljs-string">'风控管理平台'</span>
<span class="hljs-comment">// 标题分隔符</span>
<span class="hljs-keyword">export</span> <span class="hljs-keyword">const</span> titleSeparator: string = <span class="hljs-string">' - '</span>
<span class="hljs-comment">// 标题是否反转</span>
<span class="hljs-comment">// 如果为false: "page - title"</span>
<span class="hljs-comment">// 如果为ture : "title - page"</span>
<span class="hljs-keyword">export</span> <span class="hljs-keyword">const</span> titleReverse: boolean = <span class="hljs-literal">true</span>
<span class="hljs-comment">// 缓存路由的最大数量</span>
<span class="hljs-keyword">export</span> <span class="hljs-keyword">const</span> keepAliveMaxNum: number = <span class="hljs-number">20</span>
<span class="hljs-comment">// 路由模式，可选值为 history 或 hash</span>
<span class="hljs-keyword">export</span> <span class="hljs-keyword">const</span> routerMode: <span class="hljs-string">'hash'</span> | <span class="hljs-string">'history'</span> = <span class="hljs-string">'hash'</span>
<span class="hljs-comment">// 不经过token校验的路由</span>
<span class="hljs-keyword">export</span> <span class="hljs-keyword">const</span> routesWhiteList: string[] = [
  <span class="hljs-string">'/login'</span>,
  <span class="hljs-string">'/login/vip'</span>,
  <span class="hljs-string">'/404'</span>,
  <span class="hljs-string">'/403'</span>
]
<span class="hljs-comment">// 是否开启登录拦截</span>
<span class="hljs-keyword">export</span> <span class="hljs-keyword">const</span> loginInterception: boolean = <span class="hljs-literal">true</span>

<span class="copy-code-btn">复制代码</span></code></pre>
<ol start="3">
<li>在src目录下创建router文件夹，新建index.ts  router.ts</li>
</ol>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">// src/router/index.ts</span>
<span class="hljs-keyword">import</span> &#123; createRouter, createWebHashHistory, createWebHistory, RouteRecordRaw &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'vue-router'</span>
<span class="hljs-keyword">import</span> &#123; loginInterception, routerMode, routesWhiteList, title, titleReverse &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'@/config/setting.config'</span>
<span class="hljs-keyword">import</span> Layout <span class="hljs-keyword">from</span> <span class="hljs-string">'@/views/layout/index.vue'</span>
<span class="hljs-keyword">import</span> VabProgress <span class="hljs-keyword">from</span> <span class="hljs-string">'nprogress'</span>
<span class="hljs-keyword">import</span> <span class="hljs-string">'nprogress/nprogress.css'</span>
<span class="hljs-keyword">import</span> &#123; store &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'@/store'</span>

<span class="hljs-comment">// 每次刷新都重新加载权限路由</span>
<span class="hljs-keyword">let</span> routerLoad = <span class="hljs-literal">false</span>

VabProgress.configure(&#123;
  <span class="hljs-attr">easing</span>: <span class="hljs-string">'ease'</span>,
  <span class="hljs-attr">speed</span>: <span class="hljs-number">500</span>,
  <span class="hljs-attr">trickleSpeed</span>: <span class="hljs-number">200</span>,
  <span class="hljs-attr">showSpinner</span>: <span class="hljs-literal">false</span>
&#125;)

<span class="hljs-keyword">const</span> routes: <span class="hljs-built_in">Array</span><RouteRecordRaw> = [
  &#123;
    <span class="hljs-attr">path</span>: <span class="hljs-string">'/'</span>,
    <span class="hljs-attr">component</span>: Layout,
    <span class="hljs-attr">redirect</span>: <span class="hljs-string">'/home'</span>
  &#125;,
  &#123;
    <span class="hljs-attr">path</span>: <span class="hljs-string">'/home'</span>,
    <span class="hljs-attr">name</span>: <span class="hljs-string">'Home'</span>,
    <span class="hljs-attr">component</span>: <span class="hljs-function">() =></span> <span class="hljs-keyword">import</span>(<span class="hljs-string">'@/views/index/index.vue'</span>),
    <span class="hljs-attr">meta</span>: &#123;
      <span class="hljs-attr">noKeepAlive</span>: <span class="hljs-literal">true</span>
    &#125;
  &#125;,
  &#123;
    <span class="hljs-attr">path</span>: <span class="hljs-string">'/login'</span>,
    <span class="hljs-attr">name</span>: <span class="hljs-string">'Login'</span>,
    <span class="hljs-attr">component</span>: <span class="hljs-function">() =></span> <span class="hljs-keyword">import</span>(<span class="hljs-string">'@/views/login/index.vue'</span>)
  &#125;,
  &#123;
    <span class="hljs-attr">path</span>: <span class="hljs-string">'/403'</span>,
    <span class="hljs-attr">name</span>: <span class="hljs-string">'403'</span>,
    <span class="hljs-attr">component</span>: <span class="hljs-function">() =></span> <span class="hljs-keyword">import</span>(<span class="hljs-string">'@/views/403.vue'</span>)
  &#125;,
  &#123;
    <span class="hljs-attr">path</span>: <span class="hljs-string">'/:pathMatch(.*)*'</span>,
    <span class="hljs-attr">name</span>: <span class="hljs-string">'404'</span>,
    <span class="hljs-attr">component</span>: <span class="hljs-function">() =></span> <span class="hljs-keyword">import</span>(<span class="hljs-string">'@/views/404.vue'</span>)
  &#125;
]

<span class="hljs-keyword">const</span> router = createRouter(&#123;
  <span class="hljs-attr">history</span>: routerMode === <span class="hljs-string">'hash'</span>
    ? createWebHashHistory(<span class="hljs-keyword">import</span>.meta.env.BASE_URL)
    : createWebHistory(<span class="hljs-keyword">import</span>.meta.env.BASE_URL),
  routes
&#125;)

<span class="hljs-keyword">export</span> <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">resetRoute</span> (<span class="hljs-params">routes: any</span>): <span class="hljs-title">void</span> </span>&#123;
  router.addRoute(&#123;
    <span class="hljs-attr">path</span>: <span class="hljs-string">'/'</span>,
    <span class="hljs-attr">component</span>: Layout,
    <span class="hljs-attr">redirect</span>: <span class="hljs-string">'/home'</span>,
    <span class="hljs-attr">children</span>: getAllFirstRoute(routes)
  &#125;)
&#125;

<span class="hljs-comment">/**
 * 解构成一级路由，解决多级嵌套的keep-alive问题
 * <span class="hljs-doctag">@param <span class="hljs-variable">routes</span></span>
 * <span class="hljs-doctag">@param <span class="hljs-variable">result</span></span>
 */</span>
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">getAllFirstRoute</span> (<span class="hljs-params">routes: any, result: any = []</span>): <span class="hljs-title">any</span> </span>&#123;
  routes.forEach(<span class="hljs-function">(<span class="hljs-params">route: any</span>) =></span> &#123;
    result.push(&#123;
      ...route,
      <span class="hljs-attr">children</span>: [],
      <span class="hljs-attr">path</span>: route.meta.realPath
    &#125;)
    <span class="hljs-keyword">if</span> (route.children && route.children.length > <span class="hljs-number">0</span>) &#123;
      result = getAllFirstRoute(route.children, result)
    &#125;
  &#125;)
  <span class="hljs-keyword">return</span> result
&#125;

router.beforeEach(<span class="hljs-keyword">async</span> (to, <span class="hljs-keyword">from</span>, next) => &#123;
  VabProgress.start()
  <span class="hljs-keyword">let</span> hasToken = store.getters[<span class="hljs-string">'user/token'</span>]
  <span class="hljs-keyword">if</span> (!loginInterception) hasToken = <span class="hljs-literal">true</span>
  <span class="hljs-keyword">if</span> (routesWhiteList.includes(to.path)) &#123;
    <span class="hljs-comment">// 白名单内的不做验证</span>
    next()
  &#125; <span class="hljs-keyword">else</span> <span class="hljs-keyword">if</span> (hasToken) &#123;
    <span class="hljs-comment">// 已登录</span>
    <span class="hljs-keyword">if</span> (routerLoad) &#123;
      next()
    &#125; <span class="hljs-keyword">else</span> &#123;
      <span class="hljs-keyword">await</span> store.dispatch(<span class="hljs-string">'router/setRoutes'</span>)
      routerLoad = <span class="hljs-literal">true</span>
      next(to.path)
    &#125;
  &#125; <span class="hljs-keyword">else</span> &#123;
    <span class="hljs-comment">// 未登录</span>
    next(store.getters[<span class="hljs-string">'router/logoutUrl'</span>])
  &#125;
  VabProgress.done()
&#125;)

router.afterEach(<span class="hljs-function"><span class="hljs-params">route</span> =></span> &#123;
  <span class="hljs-keyword">if</span> (route.meta && route.meta.title) &#123;
    <span class="hljs-keyword">if</span> (titleReverse) &#123;
      <span class="hljs-built_in">document</span>.title = <span class="hljs-string">`<span class="hljs-subst">$&#123;route.meta.title&#125;</span> - <span class="hljs-subst">$&#123;title&#125;</span>`</span>
    &#125; <span class="hljs-keyword">else</span> &#123;
      <span class="hljs-built_in">document</span>.title = <span class="hljs-string">`<span class="hljs-subst">$&#123;title&#125;</span> - <span class="hljs-subst">$&#123;route.meta.title&#125;</span>`</span>
    &#125;
  &#125;
&#125;)

<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> router

<span class="copy-code-btn">复制代码</span></code></pre>
<ol start="4">
<li>状态管理新增router模块，更新state.d.ts ，新建 router.ts</li>
</ol>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">// src/state/state.d.ts</span>
declare namespace MyStore &#123;
  type language = <span class="hljs-string">'zh-cn'</span> | <span class="hljs-string">'en'</span>
  type RouterRoleType = <span class="hljs-string">'administrators'</span> | <span class="hljs-string">'headquarters'</span> | <span class="hljs-string">'subsidiary'</span>
  interface RouteMeta &#123;
    <span class="hljs-attr">title</span>: string,
    <span class="hljs-attr">icon</span>: string,
    <span class="hljs-attr">hidden</span>: boolean,
    <span class="hljs-attr">noKeepAlive</span>: boolean,
    <span class="hljs-attr">fullPath</span>: string,
    <span class="hljs-attr">realPath</span>: string
  &#125;
  interface Route &#123;
    <span class="hljs-attr">path</span>: string,
    <span class="hljs-attr">component</span>: any,
    <span class="hljs-attr">redirect</span>: string,
    <span class="hljs-attr">name</span>: string,
    <span class="hljs-attr">meta</span>: RouteMeta,
    <span class="hljs-attr">children</span>: <span class="hljs-built_in">Array</span><Route>
  &#125;
  interface State &#123;
    <span class="hljs-attr">count</span>: number
  &#125;
  interface SettingState &#123;
    <span class="hljs-attr">language</span>: language
  &#125;
  interface RouterState &#123;
    <span class="hljs-attr">roleType</span>: RouterRoleType,
    <span class="hljs-attr">routes</span>: Route,
    <span class="hljs-attr">cachedRoutes</span>: <span class="hljs-built_in">Array</span><Route>
  &#125;
&#125;

<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">// src/state/modules/router.ts</span>
<span class="hljs-comment">// import routers from '@/router/router.json'</span>
<span class="hljs-keyword">import</span> routers <span class="hljs-keyword">from</span> <span class="hljs-string">'@/router/router'</span>
<span class="hljs-keyword">import</span> &#123; convertRouter &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'@/utils/routes'</span>
<span class="hljs-keyword">import</span> &#123; resetRoute &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'@/router'</span>
<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> &#123;
  <span class="hljs-attr">name</span>: <span class="hljs-string">'router'</span>,
  <span class="hljs-attr">namespaced</span>: <span class="hljs-literal">true</span>,
  <span class="hljs-attr">state</span>: <span class="hljs-function">() =></span> &#123;
    <span class="hljs-keyword">const</span> state: MyStore.RouterState = &#123;
      <span class="hljs-attr">roleType</span>: <span class="hljs-string">'headquarters'</span>, <span class="hljs-comment">// 角色类型</span>
      <span class="hljs-attr">routes</span>: &#123;
        <span class="hljs-attr">children</span>: []
      &#125;,
      <span class="hljs-attr">cachedRoutes</span>: []
    &#125;
    <span class="hljs-keyword">return</span> state
  &#125;,
  <span class="hljs-attr">getters</span>: &#123;
    logoutUrl () &#123;
      <span class="hljs-keyword">return</span> <span class="hljs-string">'/login'</span>
    &#125;
  &#125;,
  <span class="hljs-attr">mutations</span>: &#123;
    setRoutes (state: MyStore.RouterState, <span class="hljs-attr">routes</span>: MyStore.Route) &#123;
      state.routes = routes
    &#125;,
    setRoleType (state: MyStore.RouterState, <span class="hljs-attr">type</span>: MyStore.RouterRoleType) &#123;
      state.roleType = type
    &#125;,
    setCachedRoutes (state: MyStore.RouterState, <span class="hljs-attr">routes</span>: <span class="hljs-built_in">Array</span><MyStore.Route>) &#123;
      state.cachedRoutes = routes
    &#125;
  &#125;,
  <span class="hljs-attr">actions</span>: &#123;
    <span class="hljs-keyword">async</span> setRoutes (&#123; commit, state &#125;: any) &#123;
      <span class="hljs-comment">// @ts-ignore</span>
      <span class="hljs-keyword">const</span> routes = routers[state.roleType]
      commit(<span class="hljs-string">'setRoutes'</span>, routes)
      <span class="hljs-keyword">const</span> syncRoutes = convertRouter([routes])
      resetRoute(syncRoutes)
    &#125;,
    <span class="hljs-keyword">async</span> setCachedRoutes (&#123; commit &#125;: any, <span class="hljs-attr">routes</span>: any) &#123;
      commit(<span class="hljs-string">'setCachedRoutes'</span>, routes)
    &#125;
  &#125;
&#125;

<span class="copy-code-btn">复制代码</span></code></pre>
<ol start="5">
<li>创建工具方法，解析路由</li>
</ol>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">// src/utils/router.ts</span>
<span class="hljs-keyword">export</span> <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">convertRouter</span> (<span class="hljs-params">asyncRoutes: <span class="hljs-built_in">Array</span><any>, parentUrl: string = <span class="hljs-string">''</span></span>): <span class="hljs-title">any</span> </span>&#123;
  <span class="hljs-keyword">return</span> asyncRoutes.map(<span class="hljs-function"><span class="hljs-params">route</span> =></span> &#123;
    <span class="hljs-comment">// 动态拼接组件，但是发布到线上后失效，暂时搁置</span>
    <span class="hljs-comment">// if (route.component) &#123;</span>
    <span class="hljs-comment">//   if (route.component === 'Layout') &#123;</span>
    <span class="hljs-comment">//     route.component = () => import('../views/layout/index.vue')</span>
    <span class="hljs-comment">//   &#125; else &#123;</span>
    <span class="hljs-comment">//     const index = route.component.indexOf('views')</span>
    <span class="hljs-comment">//     const path =</span>
    <span class="hljs-comment">//         index > 0 ? route.component.slice(index) : `views/$&#123;route.component&#125;`</span>
    <span class="hljs-comment">//     // route.component = () => import(`../$&#123;path&#125;/index.vue`)</span>
    <span class="hljs-comment">//     route.component = defineAsyncComponent(() => import(`../$&#123;path&#125;/index.vue`))</span>
    <span class="hljs-comment">//   &#125;</span>
    <span class="hljs-comment">// &#125;</span>
    <span class="hljs-comment">// 检测meta</span>
    <span class="hljs-comment">// fullPath 左侧menu使用，用来激活</span>
    <span class="hljs-comment">// realPath 组件全路径，用来注册路由</span>
    <span class="hljs-keyword">if</span> (!route.meta) route.meta = &#123; <span class="hljs-attr">hidden</span>: <span class="hljs-literal">false</span>, <span class="hljs-attr">fullPath</span>: <span class="hljs-string">''</span>, <span class="hljs-attr">realPath</span>: <span class="hljs-string">''</span> &#125;
    <span class="hljs-keyword">if</span> (!parentUrl) &#123;
      <span class="hljs-comment">// 第一级没有传入 parentUrl</span>
      route.meta.fullPath = route.path
      route.meta.realPath = route.path
    &#125; <span class="hljs-keyword">else</span> <span class="hljs-keyword">if</span> (route.meta.hidden) &#123;
      <span class="hljs-comment">// 如果隐藏当前，不在menu展示，则fullPath设置为上一级路由</span>
      route.meta.fullPath = parentUrl
      route.meta.realPath = <span class="hljs-string">`<span class="hljs-subst">$&#123;parentUrl&#125;</span>/<span class="hljs-subst">$&#123;route.path&#125;</span>`</span>
    &#125; <span class="hljs-keyword">else</span> &#123;
      route.meta.fullPath = <span class="hljs-string">`<span class="hljs-subst">$&#123;parentUrl&#125;</span>/<span class="hljs-subst">$&#123;route.path&#125;</span>`</span>
      route.meta.realPath = <span class="hljs-string">`<span class="hljs-subst">$&#123;parentUrl&#125;</span>/<span class="hljs-subst">$&#123;route.path&#125;</span>`</span>
    &#125;

    <span class="hljs-keyword">if</span> (route.children && route.children.length) &#123; route.children = convertRouter(route.children, route.meta.fullPath) &#125;
    <span class="hljs-keyword">if</span> (route.children && route.children.length === <span class="hljs-number">0</span>) <span class="hljs-keyword">delete</span> route.children
    <span class="hljs-keyword">return</span> route
  &#125;)
&#125;

<span class="copy-code-btn">复制代码</span></code></pre>
<ol start="6">
<li>在登录页更新状态管理器 router/roleType，再进行页面跳转，在前置钩子处就会自动匹配并注册当前权限下的路由了。</li>
</ol></div>  
</div>
            