
---
title: '手写vue-router源码系列一： 实现 VueRouter｜8月更文挑战'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/ab050808495b4e8f93250ea70b25440c~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Sat, 31 Jul 2021 22:43:05 GMT
thumbnail: 'https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/ab050808495b4e8f93250ea70b25440c~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h2 data-id="heading-0">前言</h2>
<p>前端路由的原理在面试中会经常被问到，经常有些同学会在这里碰壁。本次我将通过几个系列文章的介绍并且手写代码实现来深挖 vue-router 的实现原理，一旦我们掌握了 vue-router 的实现原理，那么我们无论在平时的开发中还是出去面试都会更加游刃有余！</p>
<h2 data-id="heading-1">SPA(Single Page Application)的原理</h2>
<p>在单页应用 SPA(Single Page Application)中，路由其实描述的是 URL 与 UI 之间的映射关系，即 URL 变化引起 UI 更新，并且整个过程无需刷新页面（如德芙一样丝滑的体验）。</p>
<h2 data-id="heading-2">vue-router的使用及原理介绍</h2>
<p>首先我们回顾下 vue-router 的使用过程</p>
<ol>
<li>引入 vue-router 并使用 Vue.use()</li>
</ol>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">import</span> VueRouter <span class="hljs-keyword">from</span> <span class="hljs-string">'vue-router'</span>
Vue.use(VueRouter)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>Vue 是一套用于构建用户界面的渐进式框架，它的核心功能只是解决视图渲染。在 Vue.js 应用构建前端路由的功能就需要借助插件的方式来实现。Vue 的插件注册也很简单，如果插件是一个对象，必须提供 install 方法。如果插件是一个函数，它会被作为 install 方法。install 方法调用时，会将 Vue 作为参数传入。这样的好处就是开发插件的作者不需要再额外去 import Vue 了，节省了插件的文件体积。</p>
<ol start="2">
<li>创建 vueRouter 实例</li>
</ol>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> <span class="hljs-keyword">new</span> VueRouter(&#123;
  routes,
&#125;);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>VueRouter 是一个类，我们在 new Vue 的时候会把 routes 作为配置 的属性传⼊，这样在 VueRouter 中我们就可以获取到用户的前端路由配置表，进一步做我们想要做的事情。比如构建 URL 与 UI 之间的映射关系，方便我们以后切换路径的时候在页面上渲染不同的内容出来。</p>
<ol start="3">
<li>在根组件上添加路由实例</li>
</ol>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">import</span> router <span class="hljs-keyword">from</span> <span class="hljs-string">'./router'</span>

<span class="hljs-keyword">new</span> Vue(&#123;
 router,
&#125;).$mount(<span class="hljs-string">"#app"</span>);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>通过 router 配置参数注入路由，从而让整个应用都有路由功能。于是我们可以在任何组件内通过 this.$router 访问路由器，也可以通过 this.$route 访问当前路由。</p>
<ol start="4">
<li>添加路由视图</li>
</ol>
<pre><code class="hljs language-js copyable" lang="js"><router-view></router-view>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>RouterView 渲染路径匹配到的视图组件。RouterView还可以内嵌自己，根据嵌套路径，渲染嵌套组件。</p>
<p>以上介绍了 vue-router 的使用流程和简单的介绍了它的大概原理。接下来我们通过代码与图片的方式着手实现这个 Vue-router。</p>
<h2 data-id="heading-3">准备工作</h2>
<ol>
<li>使用 vue-cli 创建一个新的项目，我们选择Default vue2的模板。</li>
</ol>
<pre><code class="hljs language-js copyable" lang="js">vue create v-router
<span class="copy-code-btn">复制代码</span></code></pre>
<ol start="2">
<li>删除components文件夹。新增views文件夹，并且新建 Bar.vue 文件和 Foo.vue 文件</li>
</ol>
<p>Bar.vue</p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">template</span>></span>
<span class="hljs-tag"><<span class="hljs-name">div</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">h1</span>></span>bar<span class="hljs-tag"></<span class="hljs-name">h1</span>></span>
<span class="hljs-tag"></<span class="hljs-name">div</span>></span>
<span class="hljs-tag"></<span class="hljs-name">template</span>></span>

<span class="hljs-tag"><<span class="hljs-name">script</span>></span><span class="javascript">
<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> &#123;

&#125;
</span><span class="hljs-tag"></<span class="hljs-name">script</span>></span>

<span class="hljs-tag"><<span class="hljs-name">style</span>></span>

<span class="hljs-tag"></<span class="hljs-name">style</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>Foo.vue</p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">template</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">h1</span>></span>foo<span class="hljs-tag"></<span class="hljs-name">h1</span>></span>
<span class="hljs-tag"></<span class="hljs-name">template</span>></span>

<span class="hljs-tag"><<span class="hljs-name">script</span>></span><span class="javascript">
<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> &#123;

&#125;
</span><span class="hljs-tag"></<span class="hljs-name">script</span>></span>

<span class="hljs-tag"><<span class="hljs-name">style</span>></span>

<span class="hljs-tag"></<span class="hljs-name">style</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<ol start="3">
<li>修改App.vue文件</li>
</ol>
<pre><code class="hljs language-html copyable" lang="html">
<span class="hljs-tag"><<span class="hljs-name">template</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">id</span>=<span class="hljs-string">"app"</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">img</span> <span class="hljs-attr">alt</span>=<span class="hljs-string">"Vue logo"</span> <span class="hljs-attr">src</span>=<span class="hljs-string">"./assets/logo.png"</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">p</span>></span>
      <span class="hljs-tag"><<span class="hljs-name">router-link</span> <span class="hljs-attr">to</span>=<span class="hljs-string">"/foo"</span>></span>Go to Foo<span class="hljs-tag"></<span class="hljs-name">router-link</span>></span>
      <span class="hljs-tag"><<span class="hljs-name">router-link</span> <span class="hljs-attr">to</span>=<span class="hljs-string">"/bar"</span>></span>Go to Bar<span class="hljs-tag"></<span class="hljs-name">router-link</span>></span>
    <span class="hljs-tag"></<span class="hljs-name">p</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">router-view</span>></span><span class="hljs-tag"></<span class="hljs-name">router-view</span>></span>
  <span class="hljs-tag"></<span class="hljs-name">div</span>></span>
<span class="hljs-tag"></<span class="hljs-name">template</span>></span>

<span class="hljs-tag"><<span class="hljs-name">script</span>></span><span class="javascript">

<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> &#123;
  <span class="hljs-attr">name</span>: <span class="hljs-string">'App'</span>,
&#125;
</span><span class="hljs-tag"></<span class="hljs-name">script</span>></span>

<span class="hljs-tag"><<span class="hljs-name">style</span>></span><span class="css">
<span class="hljs-selector-id">#app</span> &#123;
  <span class="hljs-attribute">font-family</span>: Avenir, Helvetica, Arial, sans-serif;
  -webkit-<span class="hljs-attribute">font-smoothing</span>: antialiased;
  -moz-osx-<span class="hljs-attribute">font-smoothing</span>: grayscale;
  <span class="hljs-attribute">text-align</span>: center;
  <span class="hljs-attribute">color</span>: <span class="hljs-number">#2c3e50</span>;
  <span class="hljs-attribute">margin-top</span>: <span class="hljs-number">60px</span>;
&#125;
<span class="hljs-selector-tag">a</span> &#123;
  <span class="hljs-attribute">margin</span>:<span class="hljs-number">20px</span>;
&#125;
</span><span class="hljs-tag"></<span class="hljs-name">style</span>></span>

<span class="copy-code-btn">复制代码</span></code></pre>
<ol start="4">
<li>
<p>在src下面新增 vRouter 文件夹，这个文件夹主要用来放我们后续需要实 vue-router 的代码的相关文件。我们在 vRouter 文件夹下新建两个空白的文件：index.js、install.js</p>
</li>
<li>
<p>在src下面新增router文件夹，新建一个index.js</p>
</li>
</ol>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">import</span> Vue <span class="hljs-keyword">from</span> <span class="hljs-string">"vue"</span>;
<span class="hljs-comment">// 引入我们自己的vue-router</span>
<span class="hljs-keyword">import</span> VueRouter <span class="hljs-keyword">from</span> <span class="hljs-string">"@/vRouter/"</span>;
<span class="hljs-keyword">import</span> Foo <span class="hljs-keyword">from</span> <span class="hljs-string">"../views/Foo.vue"</span>;
<span class="hljs-keyword">import</span> Bar <span class="hljs-keyword">from</span> <span class="hljs-string">"../views/Bar.vue"</span>;
Vue.use(VueRouter);

<span class="hljs-keyword">const</span> routes = [
  &#123;
    <span class="hljs-attr">path</span>: <span class="hljs-string">"/foo"</span>,
    <span class="hljs-attr">name</span>: <span class="hljs-string">"foo"</span>,
    <span class="hljs-attr">component</span>: Foo,
  &#125;,
  &#123;
    <span class="hljs-attr">path</span>: <span class="hljs-string">"/bar"</span>,
    <span class="hljs-attr">name</span>: <span class="hljs-string">"bar"</span>,
    <span class="hljs-attr">component</span>: Bar,
  &#125;,
];
<span class="hljs-keyword">let</span> router = <span class="hljs-keyword">new</span> VueRouter(&#123;
  routes,
&#125;);

<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> router;

<span class="copy-code-btn">复制代码</span></code></pre>
<ol start="6">
<li>修改main.js文件</li>
</ol>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">import</span> Vue <span class="hljs-keyword">from</span> <span class="hljs-string">"vue"</span>;
<span class="hljs-keyword">import</span> router <span class="hljs-keyword">from</span> <span class="hljs-string">"./router/"</span>;
<span class="hljs-keyword">import</span> App <span class="hljs-keyword">from</span> <span class="hljs-string">"./App.vue"</span>;

Vue.config.productionTip = <span class="hljs-literal">false</span>;

<span class="hljs-keyword">new</span> Vue(&#123;
  router,
  <span class="hljs-attr">render</span>: <span class="hljs-function">(<span class="hljs-params">h</span>) =></span> h(App),
&#125;).$mount(<span class="hljs-string">"#app"</span>);

<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-4">实现 VueRouter.install</h2>
<p>前面的准备工作完成以后我们开始来一步步实现 vue-router。前面已经介绍过，Vue.use(VueRouter) 就是我们引入 vue-router 插件的方法。所以我们先来实现一个 install的方法。</p>
<p>我们在 beforeCreate 钩⼦函数执行的时候将 vue-router 注⼊到每⼀个组件中，这样我们在组件中就可以使用这个vue-router。这时候可能会有人问，我们只在根组件中注入了这个vue-router，但是为什么可以在他的子孙组件中获取到它呢？原因是在Vue内部实现initMixin的时候会把要混⼊的对象通过 mergeOption 合并到 Vue 的 options 中，由于每个组件的构造函数都会在 extend 阶段合并 Vue.options 到⾃⾝的 options 中，所以也就相当于每个组件都定义了 mixin 定义的选项。</p>
<p>相关代码在vue源码的 src/core/global-api/mixin.js 中定义：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">import</span> &#123; mergeOptions &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'../util/index'</span>

<span class="hljs-keyword">export</span> <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">initMixin</span> (<span class="hljs-params">Vue: GlobalAPI</span>) </span>&#123;
  Vue.mixin = <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params">mixin: <span class="hljs-built_in">Object</span></span>) </span>&#123;
    <span class="hljs-built_in">this</span>.options = mergeOptions(<span class="hljs-built_in">this</span>.options, mixin)
    <span class="hljs-keyword">return</span> <span class="hljs-built_in">this</span>
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>install.js</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">export</span> <span class="hljs-keyword">let</span> _Vue;

<span class="hljs-keyword">export</span> <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">install</span>(<span class="hljs-params">Vue</span>) </span>&#123;
  <span class="hljs-keyword">if</span> (install.installed && _Vue === Vue) <span class="hljs-keyword">return</span>;
  <span class="hljs-comment">//避免重复安装</span>
  install.installed = <span class="hljs-literal">true</span>;
  <span class="hljs-comment">//保存vue，因为后面需要使用Vue提供的api</span>
  _Vue = Vue;

  <span class="hljs-keyword">const</span> isDef = <span class="hljs-function">(<span class="hljs-params">v</span>) =></span> v !== <span class="hljs-literal">undefined</span>;


  Vue.mixin(&#123;
    <span class="hljs-function"><span class="hljs-title">beforeCreate</span>(<span class="hljs-params"></span>)</span> &#123;
      <span class="hljs-keyword">if</span> (isDef(<span class="hljs-built_in">this</span>.$options.router)) &#123;
        <span class="hljs-comment">//将 _routerRoot 设置为自己</span>
        <span class="hljs-built_in">this</span>._routerRoot = <span class="hljs-built_in">this</span>;
        <span class="hljs-comment">//将VueRouter实例挂载到Vue._router</span>
        <span class="hljs-built_in">this</span>._router = <span class="hljs-built_in">this</span>.$options.router;
        <span class="hljs-comment">//初始化VueRouter</span>
        <span class="hljs-built_in">this</span>._router.init(<span class="hljs-built_in">this</span>);
        <span class="hljs-comment">//把_route变成响应式</span>
        Vue.util.defineReactive(<span class="hljs-built_in">this</span>, <span class="hljs-string">"_route"</span>, <span class="hljs-built_in">this</span>._router.history.current);
      &#125; <span class="hljs-keyword">else</span> &#123;
        <span class="hljs-built_in">this</span>._routerRoot = (<span class="hljs-built_in">this</span>.$parent && <span class="hljs-built_in">this</span>.$parent._routerRoot) || <span class="hljs-built_in">this</span>;
      &#125;
    &#125;,
  &#125;);

  <span class="hljs-comment">/**
   * 注意：通过Object.defineProperty设置到Vue的原型上可以避免他人无意当中修改掉
   * 通过在Vue的原型上定义了$router、$route之后我们就可以在组件中调用 this.$router 和 this.$route 啦！
   */</span>
  <span class="hljs-built_in">Object</span>.defineProperty(Vue.prototype, <span class="hljs-string">"$router"</span>, &#123;
    <span class="hljs-function"><span class="hljs-title">get</span>(<span class="hljs-params"></span>)</span> &#123;
      <span class="hljs-keyword">return</span> <span class="hljs-built_in">this</span>._routerRoot._router;
    &#125;,
  &#125;);

  <span class="hljs-built_in">Object</span>.defineProperty(Vue.prototype, <span class="hljs-string">"$route"</span>, &#123;
    <span class="hljs-function"><span class="hljs-title">get</span>(<span class="hljs-params"></span>)</span> &#123;
      <span class="hljs-keyword">return</span> <span class="hljs-built_in">this</span>._routerRoot._route;
    &#125;,
  &#125;);
&#125;

<span class="copy-code-btn">复制代码</span></code></pre>
<p>然后通过将install方法引入并挂载到 VueRouter 这个类上，这样就实现了插件的 install 方法。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// index.js</span>
<span class="hljs-keyword">import</span> &#123; install &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">"./install"</span>;

<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> <span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">VueRouter</span> </span>&#123;
  <span class="hljs-function"><span class="hljs-title">constructor</span>(<span class="hljs-params">options = &#123;&#125;</span>)</span> &#123;

  &#125;
&#125;
VueRouter.install = install;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-5">实现 VueRouter</h2>
<ol>
<li>我们在 VueRouter中定义了一些属性，this.app 表⽰根 Vue 实例， this.apps 保存所有⼦组件的 Vue 实例， this.options 保存传⼊的路由配置。 this.mode 表⽰路由创建的模式， this.history 表⽰路由历史的具体的实现实例，它是根据 this.mode 实现不同的路由模式，它有 History 基类，然后不同的 history 实现都是继承 History。</li>
</ol>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// index.js</span>
<span class="hljs-keyword">import</span> &#123; install &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">"./install"</span>;
<span class="hljs-keyword">import</span> &#123; HashHistory &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">"./history/hash"</span>;

<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> <span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">VueRouter</span> </span>&#123;
  <span class="hljs-function"><span class="hljs-title">constructor</span>(<span class="hljs-params">options = &#123;&#125;</span>)</span> &#123;
    <span class="hljs-comment">//获取用户传入的配置</span>
    <span class="hljs-built_in">this</span>.options = options;
    <span class="hljs-comment">// this.app 表⽰根 Vue 实例</span>
    <span class="hljs-built_in">this</span>.app = <span class="hljs-literal">null</span>;
    <span class="hljs-comment">//this.apps 保存所有⼦组件的 Vue 实例</span>
    <span class="hljs-built_in">this</span>.apps = []; 
    <span class="hljs-built_in">this</span>.mode = options.mode || <span class="hljs-string">"hash"</span>;
    <span class="hljs-comment">//实现不同模式下的前端路由</span>
    <span class="hljs-keyword">switch</span> (<span class="hljs-built_in">this</span>.mode) &#123;
      <span class="hljs-keyword">case</span> <span class="hljs-string">"hash"</span>:
        <span class="hljs-built_in">this</span>.history = <span class="hljs-keyword">new</span> HashHistory(<span class="hljs-built_in">this</span>, options.base);
        <span class="hljs-keyword">break</span>;
      <span class="hljs-keyword">default</span>:
        <span class="hljs-keyword">return</span> <span class="hljs-keyword">new</span> <span class="hljs-built_in">Error</span>(<span class="hljs-string">`invalid mode: <span class="hljs-subst">$&#123;<span class="hljs-built_in">this</span>.mode&#125;</span>`</span>);
    &#125;
  &#125;
&#125;
VueRouter.install = install;
<span class="copy-code-btn">复制代码</span></code></pre>
<ol start="2">
<li>实例化 VueRouter 后会得到它的实例 router ，我们在使用 new Vue 的时候会把 router 作为 Vue.options.router 传入。我们在 install 方法添加一行代码用于初始化路由。这样每个组件在执⾏ beforeCreated 钩⼦函数的时候都会执⾏ router.init ⽅法。init方法中会用到history.transitionTo 做路由过渡，切换 URL 的时候也会执行它。并且我们还定义setupListeners 方法，如果用户使用的是hash模式的话，它会监听"popstate"、"hashchange"事件并且执行路由过渡。如果用户使用的是history模式的话，它会监听 URL 的变化并且执行路由过渡。</li>
</ol>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// install.js</span>

<span class="hljs-keyword">export</span> <span class="hljs-keyword">let</span> _Vue;

<span class="hljs-keyword">export</span> <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">install</span>(<span class="hljs-params">Vue</span>) </span>&#123;
  <span class="hljs-keyword">if</span> (install.installed && _Vue === Vue) <span class="hljs-keyword">return</span>;
  <span class="hljs-comment">//避免重复安装</span>
  install.installed = <span class="hljs-literal">true</span>;
  <span class="hljs-comment">//保存vue，因为后面需要使用Vue提供的api</span>
  _Vue = Vue;

  <span class="hljs-keyword">const</span> isDef = <span class="hljs-function">(<span class="hljs-params">v</span>) =></span> v !== <span class="hljs-literal">undefined</span>;

  Vue.mixin(&#123;
    <span class="hljs-function"><span class="hljs-title">beforeCreate</span>(<span class="hljs-params"></span>)</span> &#123;
      <span class="hljs-keyword">if</span> (isDef(<span class="hljs-built_in">this</span>.$options.router)) &#123;
        <span class="hljs-comment">//将 _routerRoot 设置为自己</span>
        <span class="hljs-built_in">this</span>._routerRoot = <span class="hljs-built_in">this</span>;
        <span class="hljs-comment">//将VueRouter实例挂载到Vue._router</span>
        <span class="hljs-built_in">this</span>._router = <span class="hljs-built_in">this</span>.$options.router;
        <span class="hljs-comment">//新增的代码</span>
        <span class="hljs-built_in">this</span>._router.init(<span class="hljs-built_in">this</span>);
      &#125; <span class="hljs-keyword">else</span> &#123;
        <span class="hljs-built_in">this</span>._routerRoot = (<span class="hljs-built_in">this</span>.$parent && <span class="hljs-built_in">this</span>.$parent._routerRoot) || <span class="hljs-built_in">this</span>;
      &#125;
    &#125;,
  &#125;);
  
  <span class="hljs-comment">/**
   * 注意：通过Object.defineProperty设置到Vue的原型上可以避免他人无意当中修改掉
   * 通过在Vue的原型上定义了$router、$route之后我们就可以在组件中调用 this.$router 和 this.$route 啦！
   */</span>
  <span class="hljs-built_in">Object</span>.defineProperty(Vue.prototype, <span class="hljs-string">"$router"</span>, &#123;
    <span class="hljs-function"><span class="hljs-title">get</span>(<span class="hljs-params"></span>)</span> &#123;
      <span class="hljs-keyword">return</span> <span class="hljs-built_in">this</span>._routerRoot._router;
    &#125;,
  &#125;);

  <span class="hljs-built_in">Object</span>.defineProperty(Vue.prototype, <span class="hljs-string">"$route"</span>, &#123;
    <span class="hljs-function"><span class="hljs-title">get</span>(<span class="hljs-params"></span>)</span> &#123;
      <span class="hljs-keyword">return</span> <span class="hljs-built_in">this</span>._routerRoot._route;
    &#125;,
  &#125;);
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>继续完善 VueRouter.init()</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// index.js</span>
<span class="hljs-keyword">import</span> &#123; install &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">"./install"</span>;

<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> <span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">VueRouter</span> </span>&#123;
  <span class="hljs-function"><span class="hljs-title">constructor</span>(<span class="hljs-params">options = &#123;&#125;</span>)</span> &#123;
    <span class="hljs-comment">//获取用户传入的配置</span>
    <span class="hljs-built_in">this</span>.options = options;
    <span class="hljs-comment">// this.app 表⽰根 Vue 实例</span>
    <span class="hljs-built_in">this</span>.app = <span class="hljs-literal">null</span>;
    <span class="hljs-comment">//this.apps 保存所有⼦组件的 Vue 实例</span>
    <span class="hljs-built_in">this</span>.apps = []; 
    <span class="hljs-built_in">this</span>.mode = options.mode || <span class="hljs-string">"hash"</span>;
    <span class="hljs-comment">//实现不同模式下的前端路由</span>
    <span class="hljs-keyword">switch</span> (<span class="hljs-built_in">this</span>.mode) &#123;
      <span class="hljs-keyword">case</span> <span class="hljs-string">"hash"</span>:
        <span class="hljs-built_in">this</span>.history = <span class="hljs-keyword">new</span> HashHistory(<span class="hljs-built_in">this</span>, options.base);
        <span class="hljs-keyword">break</span>;
      <span class="hljs-keyword">default</span>:
        <span class="hljs-keyword">return</span> <span class="hljs-keyword">new</span> <span class="hljs-built_in">Error</span>(<span class="hljs-string">`invalid mode: <span class="hljs-subst">$&#123;<span class="hljs-built_in">this</span>.mode&#125;</span>`</span>);
    &#125;
  &#125;

  <span class="hljs-function"><span class="hljs-title">init</span>(<span class="hljs-params">app</span>)</span> &#123;
    <span class="hljs-built_in">this</span>.apps.push(app);
    <span class="hljs-comment">// 只有根Vue实例会保存到this.app</span>
    <span class="hljs-keyword">if</span> (<span class="hljs-built_in">this</span>.app) &#123;
      <span class="hljs-keyword">return</span>;
    &#125;
    <span class="hljs-comment">//保存 Vue 实例</span>
    <span class="hljs-built_in">this</span>.app = app;

    <span class="hljs-keyword">const</span> history = <span class="hljs-built_in">this</span>.history;
    <span class="hljs-keyword">if</span> (history <span class="hljs-keyword">instanceof</span> HashHistory) &#123;
      <span class="hljs-comment">//添加路由事件监听函数</span>
      <span class="hljs-keyword">const</span> setupListeners = <span class="hljs-function">() =></span> &#123;
        history.setupListeners();
      &#125;;
      <span class="hljs-comment">//执行路由过渡</span>
      history.transitionTo(
        history.getCurrentLocation(),
        setupListeners
      );
    &#125;
  &#125;
&#125;
VueRouter.install = install;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-6">实现 hash 模式</h2>
<ol>
<li>我们在vRouter文件夹下新建history文件夹，然后新建hash.js。HashHistory 继承自 History。</li>
</ol>
<p>src/vRouter/history/hash.js</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">import</span> &#123; History &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">"./base"</span>;
<span class="hljs-keyword">import</span> &#123; pushState, replaceState, supportsPushState &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">"../util/push-state"</span>;

<span class="hljs-keyword">export</span> <span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">HashHistory</span> <span class="hljs-keyword">extends</span> <span class="hljs-title">History</span> </span>&#123;
  <span class="hljs-function"><span class="hljs-title">constructor</span>(<span class="hljs-params">router, base</span>)</span> &#123;
    <span class="hljs-built_in">super</span>(router, base);
  &#125;

  <span class="hljs-function"><span class="hljs-title">setupListeners</span>(<span class="hljs-params"></span>)</span> &#123;
    <span class="hljs-comment">/**
     * 监听浏览器前进、后退或者 hashchange 事件并且执行路由过渡
     */</span>
    <span class="hljs-keyword">const</span> handleRoutingEvent = <span class="hljs-function">() =></span> &#123;
      <span class="hljs-built_in">this</span>.transitionTo(
        getHash(), 
        <span class="hljs-function">(<span class="hljs-params">route</span>) =></span> &#123;
          <span class="hljs-keyword">if</span> (!supportsPushState) &#123;
            replaceHash(route.fullPath);
          &#125;
        &#125;
      );
    &#125;;
    <span class="hljs-keyword">const</span> eventType = supportsPushState ? <span class="hljs-string">"popstate"</span> : <span class="hljs-string">"hashchange"</span>;
    <span class="hljs-built_in">window</span>.addEventListener(eventType, handleRoutingEvent);
  &#125;
&#125;

<span class="hljs-keyword">export</span> <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">getHash</span>(<span class="hljs-params"></span>) </span>&#123;
  <span class="hljs-keyword">let</span> href = <span class="hljs-built_in">window</span>.location.href;
  <span class="hljs-keyword">const</span> index = href.indexOf(<span class="hljs-string">"#"</span>);
  <span class="hljs-keyword">if</span> (index < <span class="hljs-number">0</span>) <span class="hljs-keyword">return</span> <span class="hljs-string">""</span>;
  href = href.slice(index + <span class="hljs-number">1</span>);
  <span class="hljs-keyword">return</span> href;
&#125;

<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">replaceHash</span> (<span class="hljs-params">path</span>) </span>&#123;
  <span class="hljs-keyword">if</span> (supportsPushState) &#123;
    replaceState(getUrl(path))
  &#125; <span class="hljs-keyword">else</span> &#123;
    <span class="hljs-built_in">window</span>.location.replace(getUrl(path))
  &#125;
&#125;

<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">getUrl</span> (<span class="hljs-params">path</span>) </span>&#123;
  <span class="hljs-keyword">const</span> href = <span class="hljs-built_in">window</span>.location.href
  <span class="hljs-keyword">const</span> i = href.indexOf(<span class="hljs-string">'#'</span>)
  <span class="hljs-keyword">const</span> base = i >= <span class="hljs-number">0</span> ? href.slice(<span class="hljs-number">0</span>, i) : href
  <span class="hljs-keyword">return</span> <span class="hljs-string">`<span class="hljs-subst">$&#123;base&#125;</span>#<span class="hljs-subst">$&#123;path&#125;</span>`</span>
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<ol start="2">
<li>在vRouter中新建util文件夹，新建push-state.js</li>
</ol>
<p>src/vRouter/util/push-state.js</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">export</span> <span class="hljs-keyword">const</span> supportsPushState = <span class="hljs-built_in">window</span>.history && <span class="hljs-keyword">typeof</span> <span class="hljs-built_in">window</span>.history.pushState === <span class="hljs-string">"function"</span>;

<span class="hljs-keyword">export</span> <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">pushState</span>(<span class="hljs-params">url, replace</span>) </span>&#123;
  <span class="hljs-keyword">const</span> history = <span class="hljs-built_in">window</span>.history;
  <span class="hljs-keyword">try</span> &#123;
    <span class="hljs-keyword">if</span> (replace) &#123;
      history.replaceState(&#123;&#125;, <span class="hljs-string">""</span>, url);
    &#125; <span class="hljs-keyword">else</span> &#123;
      history.pushState(&#123;&#125;, <span class="hljs-string">""</span>, url);
    &#125;
  &#125; <span class="hljs-keyword">catch</span> (e) &#123;
    <span class="hljs-built_in">window</span>.location[replace ? <span class="hljs-string">"replace"</span> : <span class="hljs-string">"assign"</span>](url);
  &#125;
&#125;

<span class="hljs-keyword">export</span> <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">replaceState</span>(<span class="hljs-params">url</span>) </span>&#123;
  pushState(url, <span class="hljs-literal">true</span>);
&#125;

<span class="copy-code-btn">复制代码</span></code></pre>
<ol start="3">
<li>实现 History</li>
</ol>
<p>History 是 VueRouter 的基类。History 实现了：</p>
<ul>
<li>updateRoute (更新路由和视图)</li>
<li>transitionTo (路由切换)</li>
<li>listen （保存一些回调函数）</li>
</ul>
<p>src/vRouter/history/base.js</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">import</span> &#123; START &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">"../util/route"</span>;
<span class="hljs-keyword">import</span> &#123; inBrowser &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">"../util/dom"</span>;

<span class="hljs-keyword">export</span> <span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">History</span> </span>&#123;
  <span class="hljs-function"><span class="hljs-title">constructor</span>(<span class="hljs-params">router, base</span>)</span> &#123;
    <span class="hljs-comment">// 应用的基路径。例如，如果整个单页应用服务在 /app/ 下，然后 base 就应该设为 "/app/"。</span>
    <span class="hljs-built_in">this</span>.base = normalizeBase(base);
    <span class="hljs-built_in">this</span>.router = router; <span class="hljs-comment">//保存router实列</span>
    <span class="hljs-built_in">this</span>.current = START;
  &#125;

  <span class="hljs-function"><span class="hljs-title">listen</span>(<span class="hljs-params">cb</span>)</span> &#123;
    <span class="hljs-comment">//保存将来供 History 调用的方法</span>
    <span class="hljs-built_in">this</span>.cb = cb;
  &#125;

  <span class="hljs-function"><span class="hljs-title">updateRoute</span>(<span class="hljs-params">route</span>)</span> &#123;
    <span class="hljs-built_in">this</span>.current = route;
    <span class="hljs-built_in">this</span>.cb && <span class="hljs-built_in">this</span>.cb();
  &#125;

  <span class="hljs-function"><span class="hljs-title">transitionTo</span>(<span class="hljs-params">location, onComplete</span>)</span> &#123;
    <span class="hljs-keyword">let</span> route = location;
    onComplete && onComplete(route);
  &#125;
&#125;

<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">normalizeBase</span>(<span class="hljs-params">base</span>) </span>&#123;
  <span class="hljs-keyword">if</span> (!base) &#123;
    <span class="hljs-keyword">if</span> (inBrowser) &#123;
      <span class="hljs-comment">//如果在浏览器环境中会首先查找 <base href="" /> 中的href地址</span>
      <span class="hljs-keyword">const</span> baseEl = <span class="hljs-built_in">document</span>.querySelector(<span class="hljs-string">"base"</span>);
      base = (baseEl && baseEl.getAttribute(<span class="hljs-string">"href"</span>)) || <span class="hljs-string">"/"</span>;
      <span class="hljs-comment">//  "https://foo/" >> "/"</span>
      base = base.replace(<span class="hljs-regexp">/^https?:\/\/[^\/]+/</span>, <span class="hljs-string">""</span>);
    &#125; <span class="hljs-keyword">else</span> &#123;
      base = <span class="hljs-string">"/"</span>;
    &#125;
  &#125;
  <span class="hljs-comment">//确保 base 以 "/" 开头</span>
  <span class="hljs-keyword">if</span> (base.charAt(<span class="hljs-number">0</span>) !== <span class="hljs-string">"/"</span>) &#123;
    base = <span class="hljs-string">"/"</span> + base;
  &#125;
  <span class="hljs-comment">//去掉路径最后的 "/"</span>
  <span class="hljs-keyword">return</span> base.replace(<span class="hljs-regexp">/\/$/</span>, <span class="hljs-string">""</span>);
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>src/vRouter/util/route.js</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">/**
 * 此方法返回一个Route对象。
 * 表⽰的是路由中的⼀条线路，它除了描述了类似 Loctaion 的name、 path 、 query 、 hash 、meta这 些概念，
 * 还有 matched 表⽰匹配到的所有的 RouteRecord 。
 * <span class="hljs-doctag">@param <span class="hljs-type">&#123;*&#125;</span> <span class="hljs-variable">record</span></span>
 * <span class="hljs-doctag">@param <span class="hljs-type">&#123;*&#125;</span> <span class="hljs-variable">location</span></span>
 * <span class="hljs-doctag">@param <span class="hljs-type">&#123;*&#125;</span> <span class="hljs-variable">redirectedFrom</span></span>
 * <span class="hljs-doctag">@param <span class="hljs-type">&#123;*&#125;</span> <span class="hljs-variable">router</span></span>
 * <span class="hljs-doctag">@returns</span>
 */</span>
<span class="hljs-keyword">export</span> <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">createRoute</span>(<span class="hljs-params">record, location, redirectedFrom</span>) </span>&#123;
  <span class="hljs-comment">//路由记录</span>
  <span class="hljs-keyword">const</span> route = &#123;
    <span class="hljs-attr">name</span>: location.name || (record && record.name),
    <span class="hljs-attr">meta</span>: (record && record.meta) || &#123;&#125;,
    <span class="hljs-attr">path</span>: location.path || <span class="hljs-string">"/"</span>,
    <span class="hljs-attr">hash</span>: location.hash || <span class="hljs-string">""</span>,
    <span class="hljs-attr">fullPath</span>: getFullPath(location),
    <span class="hljs-attr">matched</span>: record ? formatMatch(record) : [],
  &#125;;
  <span class="hljs-keyword">if</span> (redirectedFrom) &#123;
    route.redirectedFrom = getFullPath(redirectedFrom);
  &#125;
  <span class="hljs-keyword">return</span> <span class="hljs-built_in">Object</span>.freeze(route);
&#125;

<span class="hljs-comment">// 初始化的route</span>
<span class="hljs-keyword">export</span> <span class="hljs-keyword">const</span> START = createRoute(<span class="hljs-literal">null</span>, &#123;
  <span class="hljs-attr">path</span>: <span class="hljs-string">"/"</span>,
&#125;);

<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">formatMatch</span>(<span class="hljs-params">record</span>) </span>&#123;
  <span class="hljs-keyword">const</span> res = [];
  <span class="hljs-keyword">while</span> (record) &#123;
    res.unshift(record);
    record = record.parent;
  &#125;
  <span class="hljs-keyword">return</span> res;
&#125;

<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">getFullPath</span>(<span class="hljs-params">&#123; path, hash = <span class="hljs-string">""</span> &#125;</span>) </span>&#123;
  <span class="hljs-keyword">return</span> (path || <span class="hljs-string">"/"</span>) + hash;
&#125;

<span class="copy-code-btn">复制代码</span></code></pre>
<p>v-router/src/vRouter/util/dom.js</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">export</span> <span class="hljs-keyword">const</span> inBrowser = <span class="hljs-keyword">typeof</span> <span class="hljs-built_in">window</span> !== <span class="hljs-string">'undefined'</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>通过以上步骤我们先运行下代码看看效果：</p>
<p>执行 npm run serve</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/ab050808495b4e8f93250ea70b25440c~tplv-k3u1fbpfcp-watermark.image" alt="demo1.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>通过页面我们看到 Vue 给我们报了警告：说我们没有注册过router-link、router-view这两个组件。</p>
<p>再检查页面中的元素可以看到，我们写的 router-link 和 router-view 并没有被浏览器识别出来。因为这个是我们自定义的标签。因此我们需要注册这两个全局组件。比如说让 router-link 渲染成 a 标签，router-view 渲染出我们想要的 UI。</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/767e6af09d18434aa5c395d966c7cf67~tplv-k3u1fbpfcp-watermark.image" alt="demo2.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-7">下期预告</h2>
<p>使用router-link可以实现跳转到指定路由界面,但是我们如何知道哪个 URL 对应的 View 的具体内容是什么呢? 换句话说就是如何将 URL 与 View 关联起来呢?即建立 URL 与 View 的映射关系。如果我们知道了这个对应关系，那么在 URL 变化的时候我们只需要更新对应的视图内容就可以了！这就是 matcher 的用途之一。另外 vue-router 的 matcher 还实现了addRoutes、addRoute、getRoutes等方法。那么下期我们将会介绍如何实现 matcher。敬请期待。。。</p></div>  
</div>
            