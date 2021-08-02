
---
title: '学习笔记（一）简单实现 VueRouter'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=7961'
author: 掘金
comments: false
date: Sun, 01 Aug 2021 19:47:35 GMT
thumbnail: 'https://picsum.photos/400/300?random=7961'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h1 data-id="heading-0">学习笔记（一）简单实现 VueRouter</h1>
<p>交个朋友或进入前端交流群：<code>-GuanEr-</code></p>
<p><strong>本系列笔记来源，开课吧前端架构课程</strong></p>
<p>这个练习非常简单，只考虑 history 模式下路由和嵌套路由的实现。主要目的是理解路由的核心思想。至于更完善，更深入的内容，可以在学习完这些内容之后，阅读源码。</p>
<p>如果有问题，或者有更好的解决方案，欢迎大家分享和指教。</p>
<h2 data-id="heading-1">*最终效果</h2>
<p>我们在这个练习中需要实现的效果如下：</p>
<ul>
<li>考虑 hash 模式</li>
<li>实现 <code>router-link</code> 组件通过 <code>to</code> 属性切换路由</li>
<li>实现 <code>router-view</code> 渲染路由对应的组件</li>
<li>实现 在任意组件内通过 <code>this.$router.push(path)</code> 的方式，跳转路由</li>
<li>实现嵌套路由</li>
</ul>
<h2 data-id="heading-2">目录</h2>
<p>在 src 下新建以下文件和文件夹</p>
<pre><code class="copyable">my-router
  my-router.js  # 封装 VueRouter 类
  my-router-view.js # 封装 router-view
  index.js # 配置路由
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-3">main.js 中配置如下:</h3>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">import</span> Vue <span class="hljs-keyword">from</span> <span class="hljs-string">'vue'</span>
<span class="hljs-keyword">import</span> App <span class="hljs-keyword">from</span> <span class="hljs-string">'./App.vue'</span>
<span class="hljs-keyword">import</span> router <span class="hljs-keyword">from</span> <span class="hljs-string">'./my-router/index'</span>

Vue.config.productionTip = <span class="hljs-literal">false</span>

<span class="hljs-keyword">new</span> Vue(&#123;
  router,
  <span class="hljs-attr">render</span>: <span class="hljs-function"><span class="hljs-params">h</span> =></span> h(App)
&#125;).$mount(<span class="hljs-string">'#app'</span>)
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-4">my-router/index.js</h3>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">import</span> Vue <span class="hljs-keyword">from</span> <span class="hljs-string">'vue'</span>
<span class="hljs-keyword">import</span> Router <span class="hljs-keyword">from</span> <span class="hljs-string">'./my-router'</span>
<span class="hljs-keyword">import</span> Home <span class="hljs-keyword">from</span> <span class="hljs-string">'../views/Home.vue'</span>

Vue.use(Router)

<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> <span class="hljs-keyword">new</span> Router(&#123;
  <span class="hljs-attr">mode</span>: <span class="hljs-string">'history'</span>,
  <span class="hljs-attr">base</span>: process.env.BASE_URL,
  <span class="hljs-attr">routes</span>: [
    &#123;
      <span class="hljs-attr">path</span>: <span class="hljs-string">'/'</span>,
      <span class="hljs-attr">name</span>: <span class="hljs-string">'home'</span>,
      <span class="hljs-attr">component</span>: Home
    &#125;,
    &#123;
      <span class="hljs-attr">path</span>: <span class="hljs-string">'/about'</span>,
      <span class="hljs-attr">name</span>: <span class="hljs-string">'about'</span>,
      <span class="hljs-attr">component</span>: <span class="hljs-function">() =></span> <span class="hljs-keyword">import</span>(<span class="hljs-string">'../views/About.vue'</span>),
      <span class="hljs-attr">children</span>: [
        &#123;
          <span class="hljs-attr">path</span>: <span class="hljs-string">'/about/about-1'</span>,
          <span class="hljs-attr">name</span>: <span class="hljs-string">'about1'</span>,
          <span class="hljs-attr">component</span>: <span class="hljs-function">() =></span> <span class="hljs-keyword">import</span>(<span class="hljs-string">'../views/about/About-1'</span>)
        &#125;, &#123;
          <span class="hljs-attr">path</span>: <span class="hljs-string">'/about/about-2'</span>,
          <span class="hljs-attr">name</span>: <span class="hljs-string">'about2'</span>,
          <span class="hljs-attr">component</span>: <span class="hljs-function">() =></span> <span class="hljs-keyword">import</span>(<span class="hljs-string">'../views/about/About-2'</span>)
        &#125;
      ]
    &#125;
  ]
&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-5">一、暂不考虑嵌套路由</h2>
<h3 data-id="heading-6">不考虑嵌套路由</h3>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// 1. 插件</span>
<span class="hljs-comment">// 2. 两个组件 router-link router-view</span>


<span class="hljs-comment">/* vue 插件
*  function or object
*
*  要求有一个 install 方法，将来会被 Vue.use 调用
* */</span>
<span class="hljs-keyword">let</span> Vue; <span class="hljs-comment">// 保存 Vue 的 构造函数，插件中要使用</span>

<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> <span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">VueRouter</span> </span>&#123;
  <span class="hljs-function"><span class="hljs-title">constructor</span>(<span class="hljs-params">props</span>)</span> &#123;
    <span class="hljs-built_in">this</span>.$options = props;

    <span class="hljs-comment">/* 将 current 作为响应式数据，router-view 的函数能够再次执行 */</span>
    <span class="hljs-keyword">const</span> hash = <span class="hljs-built_in">window</span>.location.hash.slice(<span class="hljs-number">1</span>);
    <span class="hljs-keyword">const</span> initial = hash || <span class="hljs-string">'/'</span>
    Vue.util.defineReactive(<span class="hljs-built_in">this</span>, <span class="hljs-string">'current'</span>, initial);

    <span class="hljs-comment">// 监听 hash 的变化</span>
    <span class="hljs-built_in">window</span>.addEventListener(<span class="hljs-string">'hashchange'</span>, <span class="hljs-function">() =></span> &#123;
      <span class="hljs-built_in">this</span>.current = <span class="hljs-built_in">window</span>.location.hash.slice(<span class="hljs-number">1</span>);
    &#125;);
  &#125;
  <span class="hljs-comment">/* *
    任务一： 保证组件内 $router 能正常使用
  * install 函数，为 VueRouter 的静态方法
  * 此处 Vue 不使用 import 原因如下：
  *  1. Vue.use() 调用插件 install 函数时，会将 Vue 的构造函数传入
  *  2. 如果要单独打包该插件，会将 import 的 Vue 也打包在一起，会让插件的体积变大
  * */</span>
  <span class="hljs-keyword">static</span> <span class="hljs-function"><span class="hljs-title">install</span>(<span class="hljs-params">_Vue</span>)</span> &#123;
    Vue = _Vue;
    <span class="hljs-comment">/* 全局混入
    *  目的：延迟逻辑，保证使用 router 时，router 已经创建
    * */</span>
    Vue.mixin(&#123;
      <span class="hljs-comment">/* 此钩子在每个组件创建实例时都会调用 */</span>
      <span class="hljs-function"><span class="hljs-title">beforeCreate</span>(<span class="hljs-params"></span>)</span> &#123;
        <span class="hljs-comment">/* 因为 router 被挂载在根实例上，所以根实例会有 router */</span>
        <span class="hljs-keyword">const</span> &#123; router &#125; = <span class="hljs-built_in">this</span>.$options;
        <span class="hljs-keyword">if</span>(router) &#123;
          <span class="hljs-comment">/*
          *  将挂载在根实例上的 router 挂在 Vue 原型上，也是为了延迟执行，当该方法执行的时候，router 已经被创建了
          * */</span>
          Vue.prototype.$router = router;
        &#125;
      &#125;
    &#125;);

    <span class="hljs-comment">/* 任务二：注册 router-view 和 router-link 组件 */</span>
    Vue.component(
      <span class="hljs-string">'router-link'</span>,
      &#123;
        <span class="hljs-attr">props</span>: &#123;
          <span class="hljs-attr">to</span>: &#123;
            <span class="hljs-attr">type</span>: <span class="hljs-built_in">String</span>,
            <span class="hljs-attr">required</span>: <span class="hljs-literal">true</span>
          &#125;
        &#125;,
        <span class="hljs-function"><span class="hljs-title">render</span>(<span class="hljs-params">h</span>)</span>&#123;
          <span class="hljs-comment">/* 方式一(不推荐，兼容性比较差) */</span>
          <span class="hljs-comment">/* return <a href=&#123;'#' + this.to&#125;>&#123;this.$slots.default&#125;</a> */</span>

          <span class="hljs-comment">/* 方式二 */</span>
          <span class="hljs-keyword">return</span> h(<span class="hljs-string">'a'</span>, &#123;
            <span class="hljs-attr">attrs</span>: &#123;
              <span class="hljs-attr">href</span>: <span class="hljs-string">'#'</span> + <span class="hljs-built_in">this</span>.to
            &#125;
          &#125;, <span class="hljs-built_in">this</span>.$slots.default)
        &#125;
      &#125;
    );

    Vue.component(<span class="hljs-string">'router-view'</span>, &#123;
      <span class="hljs-function"><span class="hljs-title">render</span>(<span class="hljs-params">h</span>)</span> &#123;
        <span class="hljs-comment">/* 获取并渲染当前路由对应的组件 */</span>
        <span class="hljs-keyword">let</span> component = <span class="hljs-literal">null</span>;
        <span class="hljs-keyword">const</span> route = <span class="hljs-built_in">this</span>.$router.$options.routes.find(
          <span class="hljs-function"><span class="hljs-params">route</span> =></span> route.path === <span class="hljs-built_in">this</span>.$router.current
        );
        <span class="hljs-keyword">if</span> (route) &#123;
          component = route.component;
        &#125;
        <span class="hljs-keyword">return</span> h(component);
      &#125;
    &#125;);
  &#125;
  <span class="hljs-function"><span class="hljs-title">push</span>(<span class="hljs-params">path</span>)</span> &#123;
    <span class="hljs-built_in">window</span>.location.hash = path;
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-7">二、嵌套路由</h2>
<p>上面的写法会在出现嵌套路由时报错，要考虑嵌套循环，做以下改进：</p>
<ul>
<li>声明一个新响应式数据：matched 数组，当其发生改变时，就会执行对应操作</li>
<li>使用 match 方法将要渲染的一级、二级...路由匹配成一个 mathced 数组</li>
<li>为每个要被 router-view 渲染的组件打上 routerView 的标记，便于遍历时确定层级</li>
<li>用 depth 标记当前被路由组件的路由层级，便于在 mathced 数组中直接定位并防止循环渲染 router-view</li>
</ul>
<h3 data-id="heading-8">分析如下</h3>
<pre><code class="copyable">假设有一个符合项目路由配置的 hash 为: /about/about-1/about-1-1

那么在配置路由时，routes 一定包含这样一个路由配置:
routes: [
  ...
  &#123;
    path: '/about',
    component: AboutComponet,
    children: [
      &#123;
        path: '/about/about-1',
        component: About1Component,
        chilren: [
          &#123;
            path: '/about/about-1/about1-1',
            component: About11Component
          &#125;
        ]
      &#125;, &#123;
        path: '/about/about-2'
        component: About2Component
      &#125;
    ]
  &#125;
  ...
]

当路由改变为： /about/about-1/about-1-1 时，希望 match 函数能在 routes 数组中做匹配，匹配之后，matched 数组包含以下内容：

[
  &#123;
    path: '/about',
    component: AboutComponet,
    children: [...]
  &#125;, &#123;
    path: '/about/about-1',
    component: About1Component,
    chilren: [...]
  &#125;, &#123;
    path: '/about/about-1/about1-1',
    component: About11Component
  &#125;
]

当一级路由 '/about' 的 router-view 渲染时，会有一个 depth，值为 0，代表该router-view 要渲染 mathced[0].component

当二级路由 '/about/about-1' 的 router-view 渲染时，会有一个 depth，值为 1，代表该router-view 要渲染 mathced[1].component

当三级路由 '/about/about-1-1' 的 router-view 渲染时，会有一个 depth，值为 2，代表该router-view 要渲染 mathced[2].component
<span class="copy-code-btn">复制代码</span></code></pre>
<p>按照以上规律，我们可以将 router-view 的配置和渲染单独封装，并且改变 VueRouter 类的部分内容：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">import</span> RouterView <span class="hljs-keyword">from</span> <span class="hljs-string">'./my-router-view'</span>

<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> <span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">VueRouter</span> </span>&#123;
  <span class="hljs-keyword">static</span> <span class="hljs-function"><span class="hljs-title">install</span>(<span class="hljs-params">_Vue</span>)</span> &#123;
    Vue = _Vue;
    Vue.mixin(&#123;
      <span class="hljs-function"><span class="hljs-title">beforeCreate</span>(<span class="hljs-params"></span>)</span> &#123;
        <span class="hljs-keyword">const</span> &#123; router &#125; = <span class="hljs-built_in">this</span>.$options;
        <span class="hljs-keyword">if</span>(router) &#123;
          Vue.prototype.$router = router;
        &#125;
      &#125;
    &#125;);

    Vue.component(
      <span class="hljs-string">'router-link'</span>,
      &#123;
        <span class="hljs-attr">props</span>: &#123;
          <span class="hljs-attr">to</span>: &#123;
            <span class="hljs-attr">type</span>: <span class="hljs-built_in">String</span>,
            <span class="hljs-attr">required</span>: <span class="hljs-literal">true</span>
          &#125;
        &#125;,
        <span class="hljs-function"><span class="hljs-title">render</span>(<span class="hljs-params">h</span>)</span>&#123;
          <span class="hljs-keyword">return</span> h(<span class="hljs-string">'a'</span>, &#123;
            <span class="hljs-attr">attrs</span>: &#123;
              <span class="hljs-attr">href</span>: <span class="hljs-string">'#'</span> + <span class="hljs-built_in">this</span>.to
            &#125;
          &#125;, <span class="hljs-built_in">this</span>.$slots.default)
        &#125;
      &#125;
    );

    Vue.component(<span class="hljs-string">'router-view'</span>, RouterView);
  &#125;

  matched = [];
  <span class="hljs-function"><span class="hljs-title">constructor</span>(<span class="hljs-params">props</span>)</span> &#123;
    <span class="hljs-built_in">this</span>.$options = props;
    <span class="hljs-built_in">this</span>.current = <span class="hljs-built_in">window</span>.location.hash.slice(<span class="hljs-number">1</span>) || <span class="hljs-string">'/'</span>;
    Vue.util.defineReactive(<span class="hljs-built_in">this</span>, <span class="hljs-string">'matched'</span>, []);

    <span class="hljs-comment">// match 方法可以递归的遍历路由表，获得匹配关系数组</span>
    <span class="hljs-built_in">this</span>.match();

    <span class="hljs-comment">// 监听 hash 的变化</span>
    <span class="hljs-built_in">window</span>.addEventListener(<span class="hljs-string">'hashchange'</span>, <span class="hljs-built_in">this</span>.onHashChange.bind(<span class="hljs-built_in">this</span>));
  &#125;

  <span class="hljs-function"><span class="hljs-title">onHashChange</span>(<span class="hljs-params"></span>)</span> &#123;
    <span class="hljs-built_in">this</span>.current = <span class="hljs-built_in">window</span>.location.hash.slice(<span class="hljs-number">1</span>);
    <span class="hljs-built_in">this</span>.matched = []; <span class="hljs-comment">// 清空 matched 数组，重新匹配</span>
    <span class="hljs-built_in">this</span>.match();
  &#125;

  <span class="hljs-function"><span class="hljs-title">match</span>(<span class="hljs-params">routes</span>)</span> &#123;
    routes = routes || <span class="hljs-built_in">this</span>.$options.routes;

    <span class="hljs-comment">// 递归遍历</span>
    <span class="hljs-keyword">for</span>(<span class="hljs-keyword">const</span> route <span class="hljs-keyword">of</span> routes) &#123;
      <span class="hljs-keyword">if</span> (route.path === <span class="hljs-string">'/'</span> && <span class="hljs-built_in">this</span>.current === <span class="hljs-string">'/'</span>) &#123;
        <span class="hljs-built_in">this</span>.matched.push(route);
        <span class="hljs-keyword">return</span>;
      &#125;
      <span class="hljs-keyword">if</span>(route.path !== <span class="hljs-string">'/'</span> && <span class="hljs-built_in">this</span>.current.indexOf(route.path) !== -<span class="hljs-number">1</span>) &#123;
        <span class="hljs-built_in">this</span>.matched.push(route);
        <span class="hljs-comment">// 如果存在 children，继续判断</span>
        <span class="hljs-keyword">if</span>(route.children) &#123;
          <span class="hljs-built_in">this</span>.match(route.children);
          <span class="hljs-comment">/* 递归遍历完成时，matched 数组中就会承接此次跳转的所有路由列表 */</span>
        &#125;
        <span class="hljs-keyword">return</span>;
      &#125;
    &#125;
  &#125;
  <span class="hljs-function"><span class="hljs-title">push</span>(<span class="hljs-params">path</span>)</span> &#123;
    <span class="hljs-built_in">window</span>.location.hash = path;
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>view封装</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> &#123;
  <span class="hljs-function"><span class="hljs-title">render</span>(<span class="hljs-params">h</span>)</span> &#123;
    <span class="hljs-comment">/* 在当前 router-view  的虚拟节点上，标记其深度 */</span>
    <span class="hljs-built_in">this</span>.$vnode.data.routerView = <span class="hljs-literal">true</span>;

    <span class="hljs-comment">/* 深度值，一级路由为 0 */</span>
    <span class="hljs-keyword">let</span> depth = <span class="hljs-number">0</span>;
    <span class="hljs-comment">/* 当前 router-view 所在的父级 vNode  */</span>
    <span class="hljs-keyword">let</span> parent = <span class="hljs-built_in">this</span>.$parent;

    <span class="hljs-keyword">while</span>(parent) &#123;
      <span class="hljs-keyword">const</span> vnodeData = parent.$vnode && parent.$vnode.data;
      <span class="hljs-keyword">if</span>(vnodeData && vnodeData.routerView) &#123;
        <span class="hljs-comment">/*
          每次 router-view 被 render 时，都会在其 data 上添加 routerView 属性，
          所以如果这里的routerView存在，即证明该 parent 为一个 routerView，
          那么当前 router-view 的深度就应该 +1
        */</span>
        depth++;
      &#125;
      <span class="hljs-comment">// 当前 parent 判断完毕，再获取上层 parent，继续判断，直至无 parent，遍历完毕</span>
      parent = parent.$parent;
    &#125;

    <span class="hljs-comment">/* 获取并渲染当前路由对应的组件 */</span>
    <span class="hljs-keyword">let</span> component = <span class="hljs-literal">null</span>;
    <span class="hljs-keyword">const</span> route = <span class="hljs-built_in">this</span>.$router.matched[depth];
    <span class="hljs-keyword">if</span>(route) &#123;
      component = route.component;
    &#125;
    <span class="hljs-keyword">return</span> h(component);
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre></div>  
</div>
            