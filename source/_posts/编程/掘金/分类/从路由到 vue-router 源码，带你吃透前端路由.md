
---
title: '从路由到 vue-router 源码，带你吃透前端路由'
categories: 
    - 编程
    - 掘金
    - 分类

author: 掘金
comments: false
date: Mon, 22 Mar 2021 08:55:12 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/e5c6e5719af241d4a1ba4f3d9fa0ec9b~tplv-k3u1fbpfcp-zoom-1.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>起因是因为我们团队内部在进行发布系统迁移的时候，遇到了规格路由相关的基础问题。当时隐约知道是为什么，但是对于路由 因为我们平时过于熟悉，以至于忘了其很多基础特性，并没有第一时间快速的排查问题。对此深感惭愧，于是就找个时间补一补路由相关的基础知识，并做一个整理~~~</p>
<h1 data-id="heading-0">路由</h1>
<p>我们既然是要聊一下前端路由，那么首先应该知道什么是路由。</p>
<p>路由这个概念本来是后端提出来的。很早的时候，都是服务端渲染，那时候前后端还没有分离，服务端将整个页面返回，响应过程基本都是这样的：</p>
<ol>
<li>浏览器发出请求</li>
<li>服务器的 80 或者 443 接口监听到浏览器发过来的请求，解析 URL 路径</li>
<li>服务端根据 URL 的内容，查询相应的资源，可能是 html 资源，可能是图片资源....，然后将对应的资源处理并返回给浏览器</li>
<li>浏览器接收到数据，然后根据 content-type 来判断如何解析资源</li>
</ol>
<p>那么什么是路由呢？我们可以简单理解为和服务器交互的一种方式，通过不同的路由我们去请求不同的资源（HTML 资源只是其中的一种方式）</p>
<h1 data-id="heading-1">后端路由</h1>
<p>我们上面介绍的其实就是后端路由。</p>
<p>后端路由又可称之为服务器端路由，因为对于服务器来说，当接收到客户端发来的HTTP请求，就会根据所请求的URL，来找到相应的映射函数，然后执行该函数，并将函数的返回值发送给客户端。</p>
<p>对于最简单的静态资源服务器，可以认为，所有URL的映射函数就是一个文件读取操作。
对于动态资源，映射函数可能是一个数据库读取操作，也可能是进行一些数据的处理，等等。</p>
<p>然后根据这些读取的数据，在服务器端就使用相应的模板来对页面进行渲染后，再返回渲染完毕的页面。</p>
<h1 data-id="heading-2">前端路由</h1>
<p>前端路由是由于 ajax 的崛起而诞生的，我们大家都知道 ajax 是浏览器为了实现异步加载的一种技术方案，刚刚也介绍了，在前后端没有分离的时候，服务端都是直接将整个 HTML 返回，用户每次一个很小的操作都会引起页面的整个刷新（再加上之前的网速还很慢，所以用户体验可想而知）</p>
<p>在 90年代末的时候，微软首先实现了 ajax（Asynchronous JavaScript And XML） 这个技术，这样用户每次的操作就可以不用刷新整个页面了，用户体验就大大提升了。</p>
<p>又随着技术的发展，慢慢三大框架称霸了前端圈，成为前端开发的主力军。前端也可以做更多的事情了，陆陆续续也有了模块化和组件化的概念。</p>
<p>当然还有单页应用、MVVM也陆陆续续出现在了前端er的视野。</p>
<p>至此，前端开发者能够开发出更加大型的应用，职能也变得更加强大了，那么这和前端路由有什么关系呢？</p>
<p>异步交互体验的更高级版本就是 SPA —— 单页应用。单页应用不仅仅是在页面交互是无刷新的，连页面跳转都是无刷新的。既然页面的跳转是无刷新的，也就是不再向后端请求返回 html。</p>
<p>那么，一个大型应用通常会有几十个页面（url 地址）相互跳转，怎么前端怎么知道 url 对应展示什么内容呢？</p>
<p>答案就是 —— 前端路由</p>
<p><strong>可以理解为，前端路由就是将之前服务端根据 url 的不同返回不同的页面的任务交给前端来做。</strong></p>
<p><img alt="image.png" class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/e5c6e5719af241d4a1ba4f3d9fa0ec9b~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer">
优点：用户体验好，不需要每次都从服务器全部获取，快速展现给用户
缺点：使用浏览器的前进，后退键的时候会重新发送请求，没有合理地利用缓存，单页面无法记住之前滚动的位置，无法在前进，后退的时候记住滚动的位置。</p>
<h2 data-id="heading-3"></h2>
<h1 data-id="heading-4">前端路由解决了什么问题</h1>
<ul>
<li>前端路由可以让前端自己维护路由和页面展示的逻辑。每次页面的改动不需要通知服务端。</li>
<li>更好的交互体验：不用每次都从服务端拉取资源，快速展现给用户</li>
</ul>
<h1 data-id="heading-5">前端路由有哪些缺点？</h1>
<ul>
<li>最让人诟病的就是不利于 SEO</li>
<li>使用浏览器的前进，后退键时会重新发送请求，来获取数据，没有合理地利用缓存。</li>
</ul>
<h1 data-id="heading-6">前端路由实现的原理是什么</h1>
<p>在了解了什么是前端路由和前端路由解决了什么问题之后，我们再来深入了解下前端路由实现的原理</p>
<p>前端路由的实现原理其实很简单，本质上就是检测 URL 的变化，通过拦截 URL然后解析匹配路由规则。</p>
<h2 data-id="heading-7">hash 路由</h2>
<p>之前，大家都是通过 hash 来实现实现路由的，hash 路由的方式就和 <code><a></code> 链接的锚点是一样的，在地址后面增加 <code>#</code> ，例如我的个人博客 <code> https://cherryblog.site/#/</code> <code> </code>
<code>#</code> 及后面的内容，我们称之为 location 的 hash
<img alt="image.png" class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/cd92708759534cb9af281b920e98db1f~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p>然后我们再点开其他的 tab 页面，发现虽然浏览器地址栏的 url 改变了，但是页面却没有刷新。打开控制台，我们可以看到切换 tab 只是向服务端发送了请求接口数据的接口，并没有重新请求 html 的资源。
<img alt="image.png" class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/d82a9dbf778640d0b5a93469d1511224~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer">
这是因为 hash 的变化不会导致浏览器向服务端发送请求，所以也就不会刷新页面。但是每次 hash 的变化，都会触发 <code>haschange</code> 事件。所以我们就可以通过监听 <code>haschange</code> 的变化来做出响应。</p>
<p>在我们现在（2021）的前端开发中，通常都是会有一个根节点 <code><div id="root"></div></code> ，然后将所要展示的内容插入到这个根节点之中。然后根据路由的不同，更换插入的内容组件。
<img alt="image.png" class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/5fed493816ef41af9c75af5acbb66e5c~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-8">history 路由</h2>
<p>hash 路由有一个问题就是因为有 <code>#</code>  所以不是那么“好看”</p>
<p>14年后，因为 HTML5 标准发布。多了两个 API， <code>pushState</code>  和 <code>replaceState</code> ，通过这两个 API 可以改变 url 地址且不会发送请求。同时还有 <code>onpopstate</code>  事件。通过这些就能用另一种方式来实现前端路由了，但原理都是跟 hash 实现相同的。</p>
<p>用了 HTML5 的实现，单页路由的 url 就不会多出一个 <code>#</code> ，变得更加美观。但因为没有 <code>#</code> 号，所以当用户刷新页面之类的操作时，浏览器还是会给服务器发送请求。为了避免出现这种情况，所以这个实现需要服务器的支持，需要把所有路由都重定向到根页面。具体可以见：[HTML5 histroy 模式](<a href="https://link.zhihu.com/?target=https%3A//router.vuejs.org/zh-cn/essentials/history-mode.html" target="_blank" rel="nofollow noopener noreferrer">HTML5 History 模式</a>)</p>
<p>注意，直接调用 <code>history.popState()</code> 和 <code>history.poshState()</code> 并不会触发 <code>popState</code> 。只有在做出浏览器的行为才会调用 <code>popState</code> ，比如点击浏览器的前进后退按钮或者JS调用 <code>history.back()</code> 或者 <code>history.forward()</code> 
<img alt="image.png" class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/1f87c67000744487b31813088aba5637~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<h1 data-id="heading-9">vue-router</h1>
<p>那我们来看一下 vue-router 是怎么结合 vue 一起实现前端路由的。</p>
<p><strong>总的来说就是使用 Vue.util.defineReactive 将实例的 _route 设置为响应式对象。而 push, replace 方法会主动更新属性 _route。而 go，back，或者点击前进后退的按钮则会在 onhashchange 或者 onpopstate 的回调中更新 _route。_route 的更新会触发 RoterView 的重新渲染。</strong></p>
<p>然后我们就在具体的看下是怎么实现的</p>
<h2 data-id="heading-10"></h2>
<h2 data-id="heading-11">如何在 vue 中注入 vueRouter（插件的安装）</h2>
<p>Vue提供了插件注册机制是，每个插件都需要实现一个静态的 <code>install</code>方法，当执行 <code>Vue.use</code> 注册插件的时候，就会执行 <code>install</code> 方法，该方法执行的时候第一个参数强制是 <code>Vue</code>对象。</p>
<p>在 vue-router 中，install 方法如下。</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">import</span> View <span class="hljs-keyword">from</span> <span class="hljs-string">'./components/view'</span>
<span class="hljs-keyword">import</span> Link <span class="hljs-keyword">from</span> <span class="hljs-string">'./components/link'</span>

<span class="hljs-comment">// 导出 vue 实例</span>
<span class="hljs-keyword">export</span> <span class="hljs-keyword">let</span> _Vue

<span class="hljs-comment">// install 方法 当 Vue.use(vueRouter)时 相当于 Vue.use(vueRouter.install())</span>
<span class="hljs-keyword">export</span> <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">install</span> (<span class="hljs-params">Vue</span>) </span>&#123;
  <span class="hljs-comment">// 如果已经注册过了并且已经有了 vue 实例，那么直接返回</span>
  <span class="hljs-keyword">if</span> (install.installed && _Vue === Vue) <span class="hljs-keyword">return</span>
  install.installed = <span class="hljs-literal">true</span>

  <span class="hljs-comment">// 保存Vue实例，方便其它插件文件使用</span>
  _Vue = Vue

  <span class="hljs-keyword">const</span> isDef = <span class="hljs-function"><span class="hljs-params">v</span> =></span> v !== <span class="hljs-literal">undefined</span>

  <span class="hljs-comment">// 递归注册实例的方法</span>
  <span class="hljs-keyword">const</span> registerInstance = <span class="hljs-function">(<span class="hljs-params">vm, callVal</span>) =></span> &#123;
    <span class="hljs-keyword">let</span> i = vm.$options._parentVnode
    <span class="hljs-keyword">if</span> (isDef(i) && isDef(i = i.data) && isDef(i = i.registerRouteInstance)) &#123;
      i(vm, callVal)
    &#125;
  &#125;

  <span class="hljs-comment">/**
   * 递归的将所有的 vue 组件混入两个生命周期 beforeCreate 和 destroyed
   * 在 beforeCreated 中初始化 vue-router，并将_route响应式
   */</span>
  Vue.mixin(&#123;
    beforeCreate () &#123;
      <span class="hljs-comment">// 初始化 vue-router</span>
      <span class="hljs-keyword">if</span> (isDef(<span class="hljs-built_in">this</span>.$options.router)) &#123;
        <span class="hljs-built_in">this</span>._routerRoot = <span class="hljs-built_in">this</span>
        <span class="hljs-built_in">this</span>._router = <span class="hljs-built_in">this</span>.$options.router
        <span class="hljs-built_in">this</span>._router.init(<span class="hljs-built_in">this</span>)
        Vue.util.defineReactive(<span class="hljs-built_in">this</span>, <span class="hljs-string">'_route'</span>, <span class="hljs-built_in">this</span>._router.history.current)
      &#125; <span class="hljs-keyword">else</span> &#123;
        <span class="hljs-comment">// 将 _route 变成响应式对象</span>
        <span class="hljs-built_in">this</span>._routerRoot = (<span class="hljs-built_in">this</span>.$parent && <span class="hljs-built_in">this</span>.$parent._routerRoot) || <span class="hljs-built_in">this</span>
      &#125;
      registerInstance(<span class="hljs-built_in">this</span>, <span class="hljs-built_in">this</span>)
    &#125;,
    destroyed () &#123;
      registerInstance(<span class="hljs-built_in">this</span>)
    &#125;
  &#125;)
  
  <span class="hljs-comment">/**
   * 给Vue添加实例对象 $router 和 $route
   * $router为router实例
   * $route为当前的route
   */</span>
  <span class="hljs-built_in">Object</span>.defineProperty(Vue.prototype, <span class="hljs-string">'$router'</span>, &#123;
    get () &#123; <span class="hljs-keyword">return</span> <span class="hljs-built_in">this</span>._routerRoot._router &#125;
  &#125;)

  <span class="hljs-built_in">Object</span>.defineProperty(Vue.prototype, <span class="hljs-string">'$route'</span>, &#123;
    get () &#123; <span class="hljs-keyword">return</span> <span class="hljs-built_in">this</span>._routerRoot._route &#125;
  &#125;)

  <span class="hljs-comment">/**
   * 注入两个全局组件
   * <router-view>
   * <router-link>
   */</span>
  Vue.component(<span class="hljs-string">'RouterView'</span>, View)
  Vue.component(<span class="hljs-string">'RouterLink'</span>, Link)

  <span class="hljs-comment">/**
   * Vue.config 是一个对象，包含了Vue的全局配置
   * 将vue-router的hook进行Vue的合并策略
   */</span>
  <span class="hljs-keyword">const</span> strats = Vue.config.optionMergeStrategies
  <span class="hljs-comment">// use the same hook merging strategy for route hooks</span>
  strats.beforeRouteEnter = strats.beforeRouteLeave = strats.beforeRouteUpdate = strats.created
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>为了保证 <code>VueRouter</code> 只执行一次，当执行 <code>install</code> 逻辑的时候添加一个标识 <code>installed</code>。用一个全局变量保存 Vue，方便插件对 Vue 的使用。</p>
<p>VueRouter 安装的核心是通过 <code>mixin</code>，向 Vue app 的所有组件混入 <code>beforeCreate</code> 和 <code>destroyed</code>钩子函数。</p>
<p>并且还在 Vue 添加实例对象</p>
<ul>
<li>_routerRoot: 指向 vue 实例</li>
<li>_router：指向 vueRouter 实例</li>
</ul>
<p>在 Vue 的 prototype 上初始化了一些 getter</p>
<ul>
<li>$router, 当前Router的实例</li>
<li>$route, 当前Router的信息</li>
</ul>
<p>Vue.util.defineReactive, 这是Vue里面观察者劫持数据的方法，劫持 _route，当 _route 触发 setter 方法的时候，则会通知到依赖的组件。</p>
<p>后面通过 <code>Vue.component</code> 方法定义了全局的 <code><router-link></code> 和 <code><router-view></code> 两个组件。<code><router-link></code>类似于a标签，<code><router-view></code> 是路由出口，在 <code><router-view></code> 切换路由渲染不同Vue组件。
最后定义了路由守卫的合并策略，采用了Vue的合并策略。</p>
<h2 data-id="heading-12">init VueRouter</h2>
<p>刚刚我们提到了在 install 的时候会执行 VueRouter 的 init 方法（ <code>this._router.init(this)</code> ），那么接下来我们就来看一下 init 方法做了什么。简单来说就是将 Vue 实例挂载到当前 router 的实例上。</p>
<p>然后 install 的时候会执行执行 VueRouter 的 init 方法（ <code>this._router.init(this)</code> ）。init 执行的时候通过 <code>history.transitionTo</code> 做路由过渡。<code>matcher</code> 路由匹配器是后面路由切换，路由和组件匹配的核心函数。</p>
<pre><code class="hljs language-javascript copyable" lang="javascript">
  init (app: any <span class="hljs-comment">/* Vue component instance */</span>) &#123;
    <span class="hljs-built_in">this</span>.apps.push(app)

    <span class="hljs-comment">// main app previously initialized</span>
    <span class="hljs-comment">// return as we don't need to set up new history listener </span>
    <span class="hljs-keyword">if</span> (<span class="hljs-built_in">this</span>.app) &#123;
      <span class="hljs-keyword">return</span>
    &#125;

    <span class="hljs-comment">// 在 VueRouter 上挂载 Vue 实例</span>
    <span class="hljs-built_in">this</span>.app = app

    <span class="hljs-keyword">const</span> history = <span class="hljs-built_in">this</span>.history

    <span class="hljs-comment">// setupListeners 里会对 hashchange 事件进行监听</span>
    <span class="hljs-comment">// transitionTo 是进行路由导航的函数</span>
    <span class="hljs-keyword">if</span> (history <span class="hljs-keyword">instanceof</span> HTML5History || history <span class="hljs-keyword">instanceof</span> HashHistory) &#123;
      <span class="hljs-keyword">const</span> setupListeners = <span class="hljs-function"><span class="hljs-params">routeOrError</span> =></span> &#123;
        history.setupListeners()
      &#125;
      history.transitionTo(
        history.getCurrentLocation(),
        setupListeners,
        setupListeners
      )
    &#125;

    <span class="hljs-comment">// 路由全局监听，维护当前的route</span>
    <span class="hljs-comment">// 因为 _route 在 install 执行时定义为响应式属性，</span>
    <span class="hljs-comment">// 当 route 变更时 _route 更新，后面的视图更新渲染就是依赖于 _route</span>
    history.listen(<span class="hljs-function"><span class="hljs-params">route</span> =></span> &#123;
      <span class="hljs-built_in">this</span>.apps.forEach(<span class="hljs-function"><span class="hljs-params">app</span> =></span> &#123;
        app._route = route
      &#125;)
    &#125;)
  &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-13">VueRouter 的 constructor</h2>
<p>VueRouter 的 constructor 相对而言比较简单</p>
<ul>
<li>定义了一些属性和方法。</li>
<li>创建 matcher 匹配函数，这个函数函数很重要，可以查找 route</li>
<li>设置默认值和做不支持 H5 history 的降级处理</li>
<li>根据不同的 mode 实例化不同的 History 对象</li>
</ul>
<pre><code class="hljs language-javascript copyable" lang="javascript">  <span class="hljs-title">constructor</span> (<span class="hljs-params">options: RouterOptions = &#123;&#125;</span>) &#123;
    <span class="hljs-built_in">this</span>.app = <span class="hljs-literal">null</span>
    <span class="hljs-built_in">this</span>.apps = []
    <span class="hljs-built_in">this</span>.options = options
    <span class="hljs-built_in">this</span>.beforeHooks = []
    <span class="hljs-built_in">this</span>.resolveHooks = []
    <span class="hljs-built_in">this</span>.afterHooks = []
    <span class="hljs-comment">// 创建 matcher 匹配函数</span>
    <span class="hljs-built_in">this</span>.matcher = createMatcher(options.routes || [], <span class="hljs-built_in">this</span>)

    <span class="hljs-comment">// 默认使用 哈希路由</span>
    <span class="hljs-keyword">let</span> mode = options.mode || <span class="hljs-string">'hash'</span>
    
    <span class="hljs-comment">// h5的history有兼容性 对history做降级处理</span>
    <span class="hljs-built_in">this</span>.fallback =
      mode === <span class="hljs-string">'history'</span> && !supportsPushState && options.fallback !== <span class="hljs-literal">false</span>
    <span class="hljs-keyword">if</span> (<span class="hljs-built_in">this</span>.fallback) &#123;
      mode = <span class="hljs-string">'hash'</span>
    &#125;
    
    <span class="hljs-keyword">if</span> (!inBrowser) &#123;
      mode = <span class="hljs-string">'abstract'</span>
    &#125;
   
    <span class="hljs-built_in">this</span>.mode = mode

    <span class="hljs-comment">// 分发处理</span>
    <span class="hljs-keyword">switch</span> (mode) &#123;
      <span class="hljs-keyword">case</span> <span class="hljs-string">'history'</span>:
        <span class="hljs-built_in">this</span>.history = <span class="hljs-keyword">new</span> HTML5History(<span class="hljs-built_in">this</span>, options.base)
        <span class="hljs-keyword">break</span>
      <span class="hljs-keyword">case</span> <span class="hljs-string">'hash'</span>:
        <span class="hljs-built_in">this</span>.history = <span class="hljs-keyword">new</span> HashHistory(<span class="hljs-built_in">this</span>, options.base, <span class="hljs-built_in">this</span>.fallback)
        <span class="hljs-keyword">break</span>
      <span class="hljs-keyword">case</span> <span class="hljs-string">'abstract'</span>:
        <span class="hljs-built_in">this</span>.history = <span class="hljs-keyword">new</span> AbstractHistory(<span class="hljs-built_in">this</span>, options.base)
        <span class="hljs-keyword">break</span>
      <span class="hljs-attr">default</span>:
        <span class="hljs-keyword">if</span> (process.env.NODE_ENV !== <span class="hljs-string">'production'</span>) &#123;
          assert(<span class="hljs-literal">false</span>, <span class="hljs-string">`invalid mode: <span class="hljs-subst">$&#123;mode&#125;</span>`</span>)
        &#125;
    &#125;
  &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>在实例化 vueRouter 的时候，vueRouter 仿照 history 定义了一些api：<code>push</code>、<code>replace</code>、<code>back</code>、<code>go</code>、<code>forward</code>，还定义了路由匹配器、添加router动态更新方法等。</p>
<h2 data-id="heading-14">如何更改 url</h2>
<p>那么 VueRouter 是如何做路由的跳转的呢？也就是说我们在使用 <code>_this_.$router.push('/foo', increment)</code> 的时候，怎么让渲染的视图展示 Foo 组件。</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">const</span> router = <span class="hljs-keyword">new</span> VueRouter(&#123;
  <span class="hljs-attr">mode</span>: <span class="hljs-string">'history'</span>,
  <span class="hljs-attr">base</span>: __dirname,
  <span class="hljs-attr">routes</span>: [
    &#123; <span class="hljs-attr">path</span>: <span class="hljs-string">'/'</span>, <span class="hljs-attr">component</span>: Home &#125;,
    &#123; <span class="hljs-attr">path</span>: <span class="hljs-string">'/foo'</span>, <span class="hljs-attr">component</span>: Foo &#125;,
    &#123; <span class="hljs-attr">path</span>: <span class="hljs-string">'/bar'</span>, <span class="hljs-attr">component</span>: Bar &#125;,
    &#123; <span class="hljs-attr">path</span>: <span class="hljs-built_in">encodeURI</span>(<span class="hljs-string">'/é'</span>), <span class="hljs-attr">component</span>: Unicode &#125;,
    &#123; <span class="hljs-attr">path</span>: <span class="hljs-string">'/query/:q'</span>, <span class="hljs-attr">component</span>: Query &#125;
  ]
&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>还记得我们刚刚在 vue-router 的 constructor 中做了什么吗？我来帮大家回忆一下。在 constructor 中，我们根据不同的 mode 选择不同类型的 history 进行实例化（h5 history 还是 hash history 还是 abstract ），然后在 init 的时候调用 history.transitionTo 进行路由初始化匹配，也就是完成第一次路由导航。</p>
<p>我们在 <code>history/base.js</code> 文件中可以找到 <code>transitionTo</code> 方法。<code>transitionTo</code> 可以接收三个参数 <code>location</code>、<code>onComplete</code>、<code>onAbort</code>，分别是目标路径、路经切换成功的回调、路径切换失败的回调。</p>
<p>首先在 router 中找到传入的 location ，然后更新当前的 route，接着就执行路经切换成功的回调函数（在这个函数中，不同模式的 history 的实现是不一样的）。</p>
<p>回调中会调用 replaceHash 或者 pushHash 方法。它们会更新 location 的 hash 值。如果兼容 historyAPI，会使用 history.replaceState 或者 history.pushState。如果不兼容 historyAPI 会使用 window.location.replace 或者window.location.hash。</p>
<p>而handleScroll方法则是会更新我们的滚动条的位置。</p>
<pre><code class="hljs language-javascript copyable" lang="javascript">transitionTo (
    location: RawLocation,
    onComplete?: <span class="hljs-built_in">Function</span>,
    onAbort?: <span class="hljs-built_in">Function</span>
) &#123;
    <span class="hljs-comment">// 调用 match方法得到匹配的 route对象</span>
    <span class="hljs-keyword">const</span> route = <span class="hljs-built_in">this</span>.router.match(location, <span class="hljs-built_in">this</span>.current)
    
    <span class="hljs-comment">// 过渡处理</span>
    <span class="hljs-built_in">this</span>.confirmTransition(
        route,
        <span class="hljs-function">() =></span> &#123;
            <span class="hljs-comment">// 更新当前的 route 对象</span>
            <span class="hljs-built_in">this</span>.updateRoute(route)
          
            <span class="hljs-comment">// 更新url地址 hash模式更新hash值 history模式通过pushState/replaceState来更新</span>
            onComplete && onComplete(route)
           
            <span class="hljs-built_in">this</span>.ensureURL()
    
            <span class="hljs-comment">// fire ready cbs once</span>
            <span class="hljs-keyword">if</span> (!<span class="hljs-built_in">this</span>.ready) &#123;
                <span class="hljs-built_in">this</span>.ready = <span class="hljs-literal">true</span>
                <span class="hljs-built_in">this</span>.readyCbs.forEach(<span class="hljs-function"><span class="hljs-params">cb</span> =></span> &#123;
                  cb(route)
                &#125;)
            &#125;
        &#125;,
        <span class="hljs-function"><span class="hljs-params">err</span> =></span> &#123;
            <span class="hljs-keyword">if</span> (onAbort) &#123;
                onAbort(err)
            &#125;
            <span class="hljs-keyword">if</span> (err && !<span class="hljs-built_in">this</span>.ready) &#123;
                <span class="hljs-built_in">this</span>.ready = <span class="hljs-literal">true</span>
                <span class="hljs-built_in">this</span>.readyErrorCbs.forEach(<span class="hljs-function"><span class="hljs-params">cb</span> =></span> &#123;
                cb(err)
                &#125;)
            &#125;
        &#125;
    )
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-15">url 更改后怎么进行组件的渲染</h2>
<p>到此为止，已经可以让不同模式下的 history 对象拥有了表现相同的 <code>push</code>  <code>replace</code> 功能（详细可以看下面的实现部分）</p>
<p>那么路由更换之后怎么进行正确的渲染呢。</p>
<p>记得我们前面说过的 vue 的响应式原理了吗？我们在 install 的时候已经将 _router 设置为响应式的了。只要 _router 进行了改变，那么就会触发 RouterView 的渲染。（我们在 transitionTo 的回调中更新了 _route）</p>
<h2 data-id="heading-16">go, forward, back</h2>
<p>在 VueRouter 上定义的 go，forward，back方法都是调用 history 的属性的 go 方法。</p>
<p>而hash上go方法调用的是history.go，它是如何更新RouteView的呢？答案是hash对象在setupListeners方法中添加了对popstate或者hashchange事件的监听。在事件的回调中会触发RoterView的更新</p>
<h3 data-id="heading-17">setupListeners</h3>
<p>我们在通过点击后退, 前进按钮或者调用 back, forward, go 方法的时候。我们没有主动更新 _app.route 和current。我们该如何触发 RouterView 的更新呢？通过在 window 上监听 popstate，或者 hashchange 事件。在事件的回调中，调用 transitionTo 方法完成对 _route 和 current 的更新。</p>
<p>或者可以这样说，在使用 push，replace 方法的时候，hash的更新在 _route 更新的后面。而使用 go, back 时，hash 的更新在 _route 更新的前面。</p>
<pre><code class="copyable">setupListeners () &#123;
  const router = this.router
  const expectScroll = router.options.scrollBehavior
  const supportsScroll = supportsPushState && expectScroll
  if (supportsScroll) &#123;
    setupScroll()
  &#125;
  window.addEventListener(supportsPushState ? 'popstate' : 'hashchange', () => &#123;
    const current = this.current
    if (!ensureSlash()) &#123;
      return
    &#125;
    this.transitionTo(getHash(), route => &#123;
      if (supportsScroll) &#123;
        handleScroll(this.router, route, current, true)
      &#125;
      if (!supportsPushState) &#123;
        replaceHash(route.fullPath)
      &#125;
    &#125;)
  &#125;)
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-18">hash 路由</h2>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">export</span> <span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">HashHistory</span> <span class="hljs-keyword">extends</span> <span class="hljs-title">History</span> </span>&#123;
  <span class="hljs-title">constructor</span> (<span class="hljs-params">router: Router, base: ?string, fallback: boolean</span>) &#123;
    <span class="hljs-built_in">super</span>(router, base)
    <span class="hljs-comment">// check history fallback deeplinking</span>
    <span class="hljs-keyword">if</span> (fallback && checkFallback(<span class="hljs-built_in">this</span>.base)) &#123;
      <span class="hljs-keyword">return</span>
    &#125;
    ensureSlash()
  &#125;

  <span class="hljs-comment">// this is delayed until the app mounts</span>
  <span class="hljs-comment">// to avoid the hashchange listener being fired too early</span>
  setupListeners () &#123;
    <span class="hljs-keyword">if</span> (<span class="hljs-built_in">this</span>.listeners.length > <span class="hljs-number">0</span>) &#123;
      <span class="hljs-keyword">return</span>
    &#125;

    <span class="hljs-keyword">const</span> router = <span class="hljs-built_in">this</span>.router
    <span class="hljs-keyword">const</span> expectScroll = router.options.scrollBehavior
    <span class="hljs-keyword">const</span> supportsScroll = supportsPushState && expectScroll

    <span class="hljs-keyword">if</span> (supportsScroll) &#123;
      <span class="hljs-built_in">this</span>.listeners.push(setupScroll())
    &#125;

    <span class="hljs-comment">// 添加 hashchange 事件监听</span>
    <span class="hljs-built_in">window</span>.addEventListener(
      hashchange,
      <span class="hljs-function">() =></span> &#123;
        <span class="hljs-keyword">const</span> current = <span class="hljs-built_in">this</span>.current
        <span class="hljs-comment">// 获取 hash 的内容并通过路由配置，把新的页面 render 到 ui-view 的节点</span>
        <span class="hljs-built_in">this</span>.transitionTo(getHash(), <span class="hljs-function"><span class="hljs-params">route</span> =></span> &#123;
          <span class="hljs-keyword">if</span> (supportsScroll) &#123;
            handleScroll(<span class="hljs-built_in">this</span>.router, route, current, <span class="hljs-literal">true</span>)
          &#125;
          <span class="hljs-keyword">if</span> (!supportsPushState) &#123;
            replaceHash(route.fullPath)
          &#125;
        &#125;)
      &#125;
    )
    <span class="hljs-built_in">this</span>.listeners.push(<span class="hljs-function">() =></span> &#123;
      <span class="hljs-built_in">window</span>.removeEventListener(eventType, handleRoutingEvent)
    &#125;)
  &#125;
    push (location: RawLocation, onComplete?: <span class="hljs-built_in">Function</span>, onAbort?: <span class="hljs-built_in">Function</span>) &#123;
    <span class="hljs-keyword">const</span> &#123; <span class="hljs-attr">current</span>: fromRoute &#125; = <span class="hljs-built_in">this</span>
    <span class="hljs-built_in">this</span>.transitionTo(
      location,
      <span class="hljs-function"><span class="hljs-params">route</span> =></span> &#123;
        pushHash(route.fullPath)
        handleScroll(<span class="hljs-built_in">this</span>.router, route, fromRoute, <span class="hljs-literal">false</span>)
        onComplete && onComplete(route)
      &#125;,
      onAbort
    )
  &#125;

  replace (location: RawLocation, onComplete?: <span class="hljs-built_in">Function</span>, onAbort?: <span class="hljs-built_in">Function</span>) &#123;
    <span class="hljs-keyword">const</span> &#123; <span class="hljs-attr">current</span>: fromRoute &#125; = <span class="hljs-built_in">this</span>
    <span class="hljs-built_in">this</span>.transitionTo(
      location,
      <span class="hljs-function"><span class="hljs-params">route</span> =></span> &#123;
        replaceHash(route.fullPath)
        handleScroll(<span class="hljs-built_in">this</span>.router, route, fromRoute, <span class="hljs-literal">false</span>)
        onComplete && onComplete(route)
      &#125;,
      onAbort
    )
  &#125;

  go (n: number) &#123;
    <span class="hljs-built_in">window</span>.history.go(n)
  &#125;
&#125;

<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">pushHash</span> (<span class="hljs-params">path</span>) </span>&#123;
  <span class="hljs-keyword">if</span> (supportsPushState) &#123;
    pushState(getUrl(path))
  &#125; <span class="hljs-keyword">else</span> &#123;
    <span class="hljs-built_in">window</span>.location.hash = path
  &#125;
&#125;

<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">replaceHash</span> (<span class="hljs-params">path</span>) </span>&#123;
  <span class="hljs-keyword">if</span> (supportsPushState) &#123;
    replaceState(getUrl(path))
  &#125; <span class="hljs-keyword">else</span> &#123;
    <span class="hljs-built_in">window</span>.location.replace(getUrl(path))
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-19"></h2>
<h2 data-id="heading-20">H5 history 路由</h2>
<p>其实和 hash 的实现方式是基本类似的，区别点主要在于</p>
<ul>
<li>监听的事件不一样</li>
<li>push 和 replace 方法的实现不一样</li>
</ul>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">export</span> <span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">HTML5History</span> <span class="hljs-keyword">extends</span> <span class="hljs-title">History</span> </span>&#123;
  <span class="hljs-attr">_startLocation</span>: string

  <span class="hljs-title">constructor</span> (<span class="hljs-params">router: Router, base: ?string</span>) &#123;
    <span class="hljs-built_in">super</span>(router, base)

    <span class="hljs-built_in">this</span>._startLocation = getLocation(<span class="hljs-built_in">this</span>.base)
  &#125;

  setupListeners () &#123;
    <span class="hljs-keyword">if</span> (<span class="hljs-built_in">this</span>.listeners.length > <span class="hljs-number">0</span>) &#123;
      <span class="hljs-keyword">return</span>
    &#125;

    <span class="hljs-keyword">const</span> router = <span class="hljs-built_in">this</span>.router
    <span class="hljs-keyword">const</span> expectScroll = router.options.scrollBehavior
    <span class="hljs-keyword">const</span> supportsScroll = supportsPushState && expectScroll

    <span class="hljs-keyword">if</span> (supportsScroll) &#123;
      <span class="hljs-built_in">this</span>.listeners.push(setupScroll())
    &#125;

    <span class="hljs-comment">// 通过监听 popstate 事件</span>
    <span class="hljs-built_in">window</span>.addEventListener(<span class="hljs-string">'popstate'</span>, <span class="hljs-function">() =></span> &#123;
      <span class="hljs-keyword">const</span> current = <span class="hljs-built_in">this</span>.current

      <span class="hljs-comment">// Avoiding first `popstate` event dispatched in some browsers but first</span>
      <span class="hljs-comment">// history route not updated since async guard at the same time.</span>
      <span class="hljs-keyword">const</span> location = getLocation(<span class="hljs-built_in">this</span>.base)
      <span class="hljs-keyword">if</span> (<span class="hljs-built_in">this</span>.current === START && location === <span class="hljs-built_in">this</span>._startLocation) &#123;
        <span class="hljs-keyword">return</span>
      &#125;

      <span class="hljs-built_in">this</span>.transitionTo(location, <span class="hljs-function"><span class="hljs-params">route</span> =></span> &#123;
        <span class="hljs-keyword">if</span> (supportsScroll) &#123;
          handleScroll(router, route, current, <span class="hljs-literal">true</span>)
        &#125;
      &#125;)
    &#125;)
    <span class="hljs-built_in">this</span>.listeners.push(<span class="hljs-function">() =></span> &#123;
      <span class="hljs-built_in">window</span>.removeEventListener(<span class="hljs-string">'popstate'</span>, handleRoutingEvent)
    &#125;)
  &#125;

  go (n: number) &#123;
    <span class="hljs-built_in">window</span>.history.go(n)
  &#125;

  push (location: RawLocation, onComplete?: <span class="hljs-built_in">Function</span>, onAbort?: <span class="hljs-built_in">Function</span>) &#123;
    <span class="hljs-keyword">const</span> &#123; <span class="hljs-attr">current</span>: fromRoute &#125; = <span class="hljs-built_in">this</span>
    <span class="hljs-built_in">this</span>.transitionTo(location, <span class="hljs-function"><span class="hljs-params">route</span> =></span> &#123;
      <span class="hljs-comment">// 使用 pushState 更新 url，不会导致浏览器发送请求，从而不会刷新页面</span>
      pushState(cleanPath(<span class="hljs-built_in">this</span>.base + route.fullPath))
      handleScroll(<span class="hljs-built_in">this</span>.router, route, fromRoute, <span class="hljs-literal">false</span>)
      onComplete && onComplete(route)
    &#125;, onAbort)
  &#125;

  replace (location: RawLocation, onComplete?: <span class="hljs-built_in">Function</span>, onAbort?: <span class="hljs-built_in">Function</span>) &#123;
    <span class="hljs-keyword">const</span> &#123; <span class="hljs-attr">current</span>: fromRoute &#125; = <span class="hljs-built_in">this</span>
    <span class="hljs-built_in">this</span>.transitionTo(location, <span class="hljs-function"><span class="hljs-params">route</span> =></span> &#123;
      <span class="hljs-comment">// replaceState 跟 pushState 的区别在于，不会记录到历史栈</span>
      replaceState(cleanPath(<span class="hljs-built_in">this</span>.base + route.fullPath))
      handleScroll(<span class="hljs-built_in">this</span>.router, route, fromRoute, <span class="hljs-literal">false</span>)
      onComplete && onComplete(route)
    &#125;, onAbort)
  &#125;

  ensureURL (push?: boolean) &#123;
    <span class="hljs-keyword">if</span> (getLocation(<span class="hljs-built_in">this</span>.base) !== <span class="hljs-built_in">this</span>.current.fullPath) &#123;
      <span class="hljs-keyword">const</span> current = cleanPath(<span class="hljs-built_in">this</span>.base + <span class="hljs-built_in">this</span>.current.fullPath)
      push ? pushState(current) : replaceState(current)
    &#125;
  &#125;

  getCurrentLocation (): string &#123;
    <span class="hljs-keyword">return</span> getLocation(<span class="hljs-built_in">this</span>.base)
  &#125;
&#125;

<span class="copy-code-btn">复制代码</span></code></pre>
<hr>
<p>能读到这里的同学真的很感谢大家~~ 这是我第一次写源码相关的内容，还没有研究的很透彻，其中不免会有一些错误的地方，希望大家多多指正~~~</p></div> <div class="image-viewer-box" data-v-78c9b824><!----></div>  
</div>
            