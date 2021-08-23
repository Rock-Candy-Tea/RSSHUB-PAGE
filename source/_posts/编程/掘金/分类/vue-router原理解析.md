
---
title: 'vue-router原理解析'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=5910'
author: 掘金
comments: false
date: Sun, 22 Aug 2021 05:54:08 GMT
thumbnail: 'https://picsum.photos/400/300?random=5910'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h1 data-id="heading-0">一、vue-router原理解析</h1>
<p>整体内容较长，需要一定的耐心，可以先理解大概思想再进行一个内容一个内容的突破。我们先从vue-router的基本使用开始讲起。</p>
<h5 data-id="heading-1">1.1 定义一个路由文件</h5>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// router.js</span>
<span class="hljs-keyword">import</span> Router <span class="hljs-keyword">from</span> <span class="hljs-string">'vue-router'</span>
Vue.use(Router)
<span class="hljs-keyword">const</span> routes = [
  &#123;
    <span class="hljs-attr">path</span>: <span class="hljs-string">'/'</span>,
    <span class="hljs-attr">name</span>: <span class="hljs-string">'Home'</span>,
    <span class="hljs-attr">component</span>: Home
  &#125;,
  &#123;
    <span class="hljs-attr">path</span>: <span class="hljs-string">'/about'</span>,
    <span class="hljs-attr">name</span>: <span class="hljs-string">'About'</span>,
    <span class="hljs-attr">component</span>: <span class="hljs-function">() =></span> <span class="hljs-keyword">import</span>(<span class="hljs-comment">/* webpackChunkName: "about" */</span> <span class="hljs-string">'../views/About.vue'</span>),
    <span class="hljs-attr">children</span>:[
      &#123;
        <span class="hljs-attr">path</span>: <span class="hljs-string">'a'</span>,
        <span class="hljs-attr">name</span>: <span class="hljs-string">'a'</span>,
        <span class="hljs-attr">component</span>: <span class="hljs-function">()=></span><span class="hljs-keyword">import</span>(<span class="hljs-comment">/* webpackChunkName: "aboutA" */</span> <span class="hljs-string">'../views/AboutA.vue'</span>)
      &#125;,
      &#123;
        <span class="hljs-attr">path</span>: <span class="hljs-string">'b'</span>,
        <span class="hljs-attr">name</span>: <span class="hljs-string">'b'</span>,
        <span class="hljs-attr">component</span>: <span class="hljs-function">()=></span><span class="hljs-keyword">import</span>(<span class="hljs-comment">/* webpackChunkName: "aboutA" */</span> <span class="hljs-string">'../views/AboutB.vue'</span>)
      &#125;
    ]
  &#125;
]

<span class="hljs-keyword">const</span> router = <span class="hljs-keyword">new</span> VueRouter(&#123;
  routes
&#125;)

router.beforeEach(<span class="hljs-function">(<span class="hljs-params">to, <span class="hljs-keyword">from</span>, next</span>) =></span> &#123;
    <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'beforeEach'</span>)
    next()
&#125;)

<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> router
<span class="copy-code-btn">复制代码</span></code></pre>
<h5 data-id="heading-2">1.2 在main.js中引入</h5>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// main.js</span>
<span class="hljs-keyword">import</span> Vue <span class="hljs-keyword">from</span> <span class="hljs-string">'vue'</span>
<span class="hljs-keyword">import</span> App <span class="hljs-keyword">from</span> <span class="hljs-string">'./App.vue'</span>
<span class="hljs-keyword">import</span> router <span class="hljs-keyword">from</span> <span class="hljs-string">'./router'</span>

Vue.config.productionTip = <span class="hljs-literal">false</span>

<span class="hljs-keyword">new</span> Vue(&#123;
  router,
  <span class="hljs-attr">name</span>: <span class="hljs-string">'main'</span>,
  <span class="hljs-attr">render</span>: <span class="hljs-function"><span class="hljs-params">h</span> =></span> h(App)
&#125;).$mount(<span class="hljs-string">'#app'</span>)
<span class="copy-code-btn">复制代码</span></code></pre>
<h5 data-id="heading-3">1.3 在app.vue中添加router-view与router-link组件</h5>
<pre><code class="hljs language-js copyable" lang="js"><template>
  <span class="xml"><span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">id</span>=<span class="hljs-string">"app"</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">id</span>=<span class="hljs-string">"nav"</span>></span>
      <span class="hljs-tag"><<span class="hljs-name">router-link</span> <span class="hljs-attr">to</span>=<span class="hljs-string">"/"</span>></span>Home<span class="hljs-tag"></<span class="hljs-name">router-link</span>></span> |
      <span class="hljs-tag"><<span class="hljs-name">router-link</span> <span class="hljs-attr">to</span>=<span class="hljs-string">"/about"</span>></span>About<span class="hljs-tag"></<span class="hljs-name">router-link</span>></span> |
    <span class="hljs-tag"></<span class="hljs-name">div</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">router-view</span>/></span>
  <span class="hljs-tag"></<span class="hljs-name">div</span>></span></span>
</template>
<span class="xml"><span class="hljs-tag"><<span class="hljs-name">script</span>></span><span class="javascript">
<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> &#123;
  <span class="hljs-attr">name</span>: <span class="hljs-string">'app'</span>
&#125;
</span><span class="hljs-tag"></<span class="hljs-name">script</span>></span></span>

<span class="xml"><span class="hljs-tag"><<span class="hljs-name">style</span>></span>
    ...
<span class="hljs-tag"></<span class="hljs-name">style</span>></span></span>

<span class="copy-code-btn">复制代码</span></code></pre>
<p>以上就完成了我们的vue-router基本使用，启动服务以后进入home首页，点击router-link可以进行路由跳转，router-view组件将会替换成定义的routes的component内容。官方说法是<strong>将组件 (components) 映射到路由 (routes)，然后告诉 Vue Router 在哪里渲染它们</strong>。说完用法，那我们来思考一下它的实现原理吧。</p>
<h1 data-id="heading-4">二、从用法思考原理</h1>
<h3 data-id="heading-5">1.引入与挂载</h3>
<p>从调用顺序上来看，首先是引入vue-router模块，然后使用了<code>Vue.use(Router)</code>进行了插件安装,翻阅vue.js官方文档：<a href="https://link.juejin.cn/?target=https%3A%2F%2Fcn.vuejs.org%2Fv2%2Fguide%2Fplugins.html" target="_blank" rel="nofollow noopener noreferrer" title="https://cn.vuejs.org/v2/guide/plugins.html" ref="nofollow noopener noreferrer">cn.vuejs.org/v2/guide/pl…</a></p>
<p>Vue.js 的插件应该暴露一个 <code>install</code> 方法。这个方法的第一个参数是 <code>Vue</code> 构造器，第二个参数是一个可选的选项对象。</p>
<p>因此我们还原出以下代码,新建一个vue-router文件夹，文件夹下新建index.js,声明一个class VueRouter，关于js类的说明参考：<a href="https://link.juejin.cn/?target=https%3A%2F%2Fdeveloper.mozilla.org%2Fzh-CN%2Fdocs%2FWeb%2FJavaScript%2FReference%2FClasses" target="_blank" rel="nofollow noopener noreferrer" title="https://developer.mozilla.org/zh-CN/docs/Web/JavaScript/Reference/Classes" ref="nofollow noopener noreferrer">developer.mozilla.org/zh-CN/docs/…</a></p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// index.js</span>
<span class="hljs-keyword">import</span> install <span class="hljs-keyword">from</span> <span class="hljs-string">'./install'</span>
<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> <span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">VueRouter</span></span>&#123;&#125;
<span class="hljs-comment">// 实例的属性必须定义在类的方法里</span>
<span class="hljs-comment">// install有以下两种定义方法</span>
<span class="hljs-comment">// 1.类的属性可以使用static在class内进行定义</span>
<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> <span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">VueRouter</span></span>&#123;
    <span class="hljs-keyword">static</span> install = install
&#125;
<span class="hljs-comment">// 2.或者定义在class外</span>
VueRouter.install = install;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>那么基础结构我们就已经完成了，在install的时候做了一些什么事情呢？同级目录下新建install.js</p>
<p>一般插件在安装时会做哪些事情呢？有以下几点。</p>
<ol>
<li>添加全局方法或 property</li>
<li>添加全局资源</li>
<li>注入组件选项</li>
<li>添加实例方法</li>
</ol>
<p>那么在<code>Vue.use(Router)</code>完成后，</p>
<ol>
<li>添加全局方法或property，具体表现为添加了<code>$route</code>与<code>$router</code>;</li>
<li>添加全局资源，具体表现为添加了组件<code>router-view</code>和<code>router-link</code>;</li>
<li>注入组件选项，使用Vue.mixin混入beforeCreate处理函数，在组件初始化时提供路由相关操作。</li>
</ol>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// install.js</span>
<span class="hljs-keyword">import</span> View <span class="hljs-keyword">from</span> <span class="hljs-string">'./components/view'</span>
<span class="hljs-keyword">import</span> Link <span class="hljs-keyword">from</span> <span class="hljs-string">'./components/link'</span>
<span class="hljs-keyword">export</span> <span class="hljs-keyword">let</span> _Vue;
<span class="hljs-keyword">export</span> <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">install</span> (<span class="hljs-params">Vue</span>) </span>&#123;
<span class="hljs-comment">// Vue是在use的时候传入，将Vue构造函数存起来，需要的地方进行引用</span>
  _Vue = Vue;
  <span class="hljs-comment">// 注入组件选项</span>
  Vue.mixin(&#123; <span class="hljs-comment">// 给所有组件的生命周期都增加beforeCreate方法,挂载在vue原型上，加载每个Vue组件时都会执行到</span>
    <span class="hljs-function"><span class="hljs-title">beforeCreate</span>(<span class="hljs-params"></span>)</span> &#123;
      <span class="hljs-keyword">if</span> (<span class="hljs-built_in">this</span>.$options.router) &#123; <span class="hljs-comment">// 如果有router属性说明是根实例</span>
        <span class="hljs-built_in">this</span>._routerRoot = <span class="hljs-built_in">this</span>; <span class="hljs-comment">// 将根实例挂载在_routerRoot属性上</span>
        <span class="hljs-built_in">this</span>._router = <span class="hljs-built_in">this</span>.$options.router; <span class="hljs-comment">// 将当前router实例挂载在_router上</span>
        <span class="hljs-built_in">this</span>._router.init(<span class="hljs-built_in">this</span>); <span class="hljs-comment">// 根实例上进行路由初始化，这里的this指向的是根实例router实例</span>
        Vue.util.defineReactive(<span class="hljs-built_in">this</span>,<span class="hljs-string">'_route'</span>,<span class="hljs-built_in">this</span>._router.history.current);
      &#125; <span class="hljs-keyword">else</span> &#123; <span class="hljs-comment">// 父组件渲染后会渲染子组件</span>
        <span class="hljs-built_in">this</span>._routerRoot = <span class="hljs-built_in">this</span>.$parent && <span class="hljs-built_in">this</span>.$parent._routerRoot;
      &#125;
    &#125;,
  &#125;);
  
  <span class="hljs-comment">// 添加两个属性</span>
  <span class="hljs-comment">// 在use之后还只是单纯的增加了这两个属性，this._routerRoot值是在执行beforeCreate之后才有，也就是new Vue之后才会有真正的值</span>
  <span class="hljs-comment">// 为什么要这么做呢，因为之后我们要使用this.$route获取current路由对象</span>
  <span class="hljs-built_in">Object</span>.defineProperty(Vue.prototype,<span class="hljs-string">'$route'</span>,&#123;
    <span class="hljs-function"><span class="hljs-title">get</span>(<span class="hljs-params"></span>)</span>&#123;
      <span class="hljs-keyword">return</span> <span class="hljs-built_in">this</span>._routerRoot._route;
    &#125;
  &#125;);
  <span class="hljs-comment">// 使用this.$router获取router的实例，也就是之前new Router()得到的实例</span>
  <span class="hljs-built_in">Object</span>.defineProperty(Vue.prototype,<span class="hljs-string">'$router'</span>,&#123;
    <span class="hljs-function"><span class="hljs-title">get</span>(<span class="hljs-params"></span>)</span>&#123;
      <span class="hljs-keyword">return</span> <span class="hljs-built_in">this</span>._routerRoot._router;
    &#125;
  &#125;)
  
  <span class="hljs-comment">// 增加了两个全局资源组件</span>
  Vue.component(<span class="hljs-string">'RouterView'</span>,View);
  Vue.component(<span class="hljs-string">'RouterLink'</span>,Link);
&#125; 
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-6">2.new vueRouter解析用户配置文件</h3>
<p>说完install完成的事情之后我们来看看vueRouter实例化的时候干了什么</p>
<ul>
<li>(1)建立一个匹配器进行关系匹配，提供match与addroutes方法</li>
<li>(2)根据mode创建一个history类型，用来执行路径监听与匹配（这里我们用hash做演示）</li>
<li>(3)注册钩子函数（勾子函数有好几种，拿出一个进行演示）</li>
</ul>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// index.js</span>
<span class="hljs-keyword">import</span> &#123;install&#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'./install'</span>
<span class="hljs-keyword">import</span> createMatcher <span class="hljs-keyword">from</span> <span class="hljs-string">'./create-matcher'</span>
<span class="hljs-keyword">import</span> HashHistory <span class="hljs-keyword">from</span> <span class="hljs-string">'./history/hash'</span>
<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> <span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">VueRouter</span></span>&#123;
  <span class="hljs-title">constructor</span> (<span class="hljs-params">options</span>) &#123;
    <span class="hljs-comment">// 根据用户传递的routes创建匹配关系，this.matcher需要两个方法</span>
    <span class="hljs-comment">// match： match方法用来匹配规则</span>
    <span class="hljs-comment">// addRoutes:用来动态添加路由</span>
    <span class="hljs-built_in">this</span>.matcher = createMatcher(options.routes || []);
    <span class="hljs-comment">// 根据mode创建一个history类型，默认为hash</span>
    <span class="hljs-built_in">this</span>.history = <span class="hljs-keyword">new</span> HashHistory(<span class="hljs-built_in">this</span>);
    <span class="hljs-comment">// 注册before勾子函数</span>
    <span class="hljs-built_in">this</span>.beforeHooks = [];
  &#125;
  <span class="hljs-comment">// 在组件初始化时才调用,这里功能可以先放着</span>
  <span class="hljs-function"><span class="hljs-title">init</span>(<span class="hljs-params">app</span>)</span>&#123;
    ...
  &#125;
  <span class="hljs-function"><span class="hljs-title">beforeEach</span>(<span class="hljs-params">fn</span>)</span>&#123;
    <span class="hljs-built_in">this</span>.beforeHooks.push(fn);
  &#125;
&#125;
VueRouter.install = install;

<span class="copy-code-btn">复制代码</span></code></pre>
<p>（1）因为功能比较复杂，将createMatcher分离出来，同级目录新建create-matcher文件夹，文件夹下新建index.js</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// create-matcher/index.js</span>
<span class="hljs-keyword">import</span> createRouteMap <span class="hljs-keyword">from</span> <span class="hljs-string">'./create-route-map'</span>
<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">createMatcher</span>(<span class="hljs-params">routes</span>)</span>&#123;
  <span class="hljs-comment">// 收集所有的路由路径，收集路径的对应渲染关系</span>
  <span class="hljs-comment">// pathList = ['/','/about','/about/a','/about/b']</span>
  <span class="hljs-comment">// pathMap = ['/':'/的记录','/about':'/about的记录'...]</span>
  <span class="hljs-keyword">let</span> &#123;pathList, pathMap&#125; = createRouteMap(routes);
  <span class="hljs-built_in">console</span>.log(pathList, pathMap)

  <span class="hljs-comment">// 这个方法就是动态加载路由的方法</span>
  <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">addRoutes</span>(<span class="hljs-params">routes</span>)</span>&#123;
    createRouteMap(routes,pathList,pathMap)
  &#125;
  <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">match</span>(<span class="hljs-params">location</span>)</span>&#123;
    ...
  &#125;
  <span class="hljs-keyword">return</span> &#123;
    addRoutes,
    match
  &#125;
&#125;

<span class="copy-code-btn">复制代码</span></code></pre>
<p>在目录create-matcher文件夹下新建create-route-map.js</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// create-matcher/create-route-map.js</span>
<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">createRouteMap</span>(<span class="hljs-params">routes,oldPathList,oldPathMap</span>)</span>&#123;
  <span class="hljs-comment">// 当第一次加载时没有pathList 和 pathMap</span>
  <span class="hljs-keyword">let</span> pathList = oldPathList || [];
  <span class="hljs-keyword">let</span> pathMap = oldPathMap || <span class="hljs-built_in">Object</span>.create(<span class="hljs-literal">null</span>);
  routes.forEach(<span class="hljs-function"><span class="hljs-params">route</span> =></span> &#123;
    addRouteRecord(route,pathList,pathMap);
  &#125;);
  <span class="hljs-keyword">return</span> &#123;
    pathList,
    pathMap
  &#125;
&#125;

<span class="hljs-comment">// pathList = ['/','/about','/about/a','/about/b']</span>
<span class="hljs-comment">// pathMap = ['/':'/的记录','/about':'/about的记录'...]</span>
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">addRouteRecord</span>(<span class="hljs-params">route,pathList,pathMap,parent</span>)</span>&#123;
  <span class="hljs-keyword">let</span> path = parent?<span class="hljs-string">`<span class="hljs-subst">$&#123;parent.path&#125;</span>/<span class="hljs-subst">$&#123;route.path&#125;</span>`</span>:route.path;
  <span class="hljs-keyword">let</span> record = &#123;
    path,
    <span class="hljs-attr">component</span>:route.component,
    parent
  &#125;
  <span class="hljs-keyword">if</span>(!pathMap[path])&#123;
    pathList.push(path);
    pathMap[path] = record;
  &#125;
  <span class="hljs-comment">// 处理子路由</span>
  <span class="hljs-keyword">if</span>(route.children)&#123;
    route.children.forEach(<span class="hljs-function"><span class="hljs-params">r</span>=></span>&#123;
      addRouteRecord(r,pathList,pathMap,route);
    &#125;)
  &#125;
&#125;

<span class="copy-code-btn">复制代码</span></code></pre>
<p>（2）执行路径监听与匹配，同级目录新建history文件夹，文件夹下新建base.js,因为模式有很多种，history，hash,抽象，所以将基本方法放在基础History类里,那我们思考一下哪些是基础的功能，哪些是模式特有的功能。基础功能有跳转，更新，监听；特有的有路径的监听，hash模式还会在项目启动后将<code>/</code>路径变更为<code>/#/</code></p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// history/base.js</span>
<span class="hljs-keyword">import</span> &#123;runQueue&#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'../util/async'</span>
<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> <span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">History</span></span>&#123;
  <span class="hljs-function"><span class="hljs-title">constructor</span>(<span class="hljs-params">router</span>)</span>&#123;
    <span class="hljs-built_in">this</span>.router = router;
    <span class="hljs-built_in">this</span>.current = createRoute(<span class="hljs-literal">null</span>,&#123;<span class="hljs-attr">path</span>:<span class="hljs-string">'/'</span>&#125;);
    <span class="hljs-built_in">this</span>.cb = <span class="hljs-literal">null</span>;
  &#125;
  <span class="hljs-comment">// 跳转功能</span>
  <span class="hljs-function"><span class="hljs-title">transitionTo</span>(<span class="hljs-params">location,onComplete</span>)</span>&#123;
    <span class="hljs-keyword">let</span> route = <span class="hljs-built_in">this</span>.router.match(location);
    <span class="hljs-keyword">if</span>(location === route.path && route.matched.length === <span class="hljs-built_in">this</span>.current.matched.length)&#123;
      <span class="hljs-keyword">return</span>
    &#125;
    <span class="hljs-comment">// 预留勾子函数执行逻辑，可以先只看this.updateRoute(route);onComplete && onComplete();</span>
    <span class="hljs-keyword">let</span> queue = [].concat(<span class="hljs-built_in">this</span>.router.beforeHooks);
    <span class="hljs-keyword">const</span> iterator = <span class="hljs-function">(<span class="hljs-params">hook,next</span>)=></span>&#123;
      hook(route,<span class="hljs-built_in">this</span>.current,<span class="hljs-function">()=></span>&#123;
        next();
      &#125;)
    &#125;
    runQueue(queue,iterator,<span class="hljs-function">()=></span>&#123;
      <span class="hljs-built_in">this</span>.updateRoute(route);
      onComplete && onComplete();
    &#125;)
  &#125;
  <span class="hljs-function"><span class="hljs-title">updateRoute</span>(<span class="hljs-params">route</span>)</span>&#123;
    <span class="hljs-built_in">this</span>.current = route;
    <span class="hljs-built_in">this</span>.cb && <span class="hljs-built_in">this</span>.cb(route);
  &#125;
  <span class="hljs-function"><span class="hljs-title">listen</span>(<span class="hljs-params">cb</span>)</span>&#123;
    <span class="hljs-built_in">this</span>.cb = cb;
  &#125;
&#125;

<span class="hljs-keyword">export</span> <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">createRoute</span>(<span class="hljs-params">record,location</span>)</span>&#123;
  <span class="hljs-keyword">let</span> res = [];
  <span class="hljs-keyword">if</span>(record)&#123;
    <span class="hljs-keyword">while</span>(record)&#123;
      res.unshift(record);
      record = record.parent
    &#125;
  &#125;
  <span class="hljs-keyword">return</span> &#123;
    ...location,
    <span class="hljs-attr">matched</span>: res
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>新建hash.js,继承Histoty</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// history/hash.js</span>
<span class="hljs-keyword">import</span> History <span class="hljs-keyword">from</span> <span class="hljs-string">"./base"</span>;
<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> <span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">HashHistory</span> <span class="hljs-keyword">extends</span> <span class="hljs-title">History</span></span>&#123;
  <span class="hljs-function"><span class="hljs-title">constructor</span>(<span class="hljs-params">router</span>)</span>&#123;
    <span class="hljs-built_in">super</span>(router);
    ensureSlash();
  &#125;
  <span class="hljs-function"><span class="hljs-title">getCurrentLocation</span>(<span class="hljs-params"></span>)</span>&#123;
    <span class="hljs-keyword">return</span> getHash();
  &#125;
  <span class="hljs-function"><span class="hljs-title">setupListener</span>(<span class="hljs-params"></span>)</span>&#123;
    <span class="hljs-built_in">window</span>.addEventListener(<span class="hljs-string">'hashchange'</span>,<span class="hljs-function">()=></span>&#123;
      <span class="hljs-built_in">this</span>.transitionTo(getHash());
    &#125;)
  &#125;
  <span class="hljs-function"><span class="hljs-title">push</span>(<span class="hljs-params">location</span>)</span>&#123;
    <span class="hljs-built_in">this</span>.transitionTo(location)
  &#125;
&#125;
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">ensureSlash</span>(<span class="hljs-params"></span>)</span>&#123;
  <span class="hljs-keyword">if</span>(<span class="hljs-built_in">window</span>.location.hash)&#123;
    <span class="hljs-keyword">return</span>
  &#125;
  <span class="hljs-built_in">window</span>.location.hash = <span class="hljs-string">'/'</span>
&#125;
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">getHash</span>(<span class="hljs-params"></span>)</span>&#123;
  <span class="hljs-keyword">return</span> <span class="hljs-built_in">window</span>.location.hash.slice(<span class="hljs-number">1</span>);
&#125;

<span class="copy-code-btn">复制代码</span></code></pre>
<p>(3)注册钩子函数</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// index.js</span>
<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> <span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">VueRouter</span></span>&#123;
  <span class="hljs-title">constructor</span> (<span class="hljs-params">options</span>) &#123;
    ...
    <span class="hljs-built_in">this</span>.beforeHooks = [];
  &#125;
  ...
  <span class="hljs-function"><span class="hljs-title">init</span>(<span class="hljs-params">app</span>)</span>&#123;
    ...
  &#125;
  <span class="hljs-function"><span class="hljs-title">beforeEach</span>(<span class="hljs-params">fn</span>)</span>&#123;
    <span class="hljs-built_in">this</span>.beforeHooks.push(fn);
  &#125;
  ...
&#125;
VueRouter.install = install;

<span class="copy-code-btn">复制代码</span></code></pre>
<p>新建一个util方法，用来执行勾子函数</p>
<pre><code class="copyable">// util/async.js
export function runQueue (queue, iterator, cb) &#123;
  function step (index) &#123;
    if(index >= queue.length)&#123;
      cb();
    &#125; else &#123;
      let hook = queue[index];
      iterator(hook,()=>&#123;
        step(index+1)
      &#125;)
    &#125;
  &#125;
  step(0)
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>将History中transitionTo方法中的runQueue结合起来看会更清楚。</p>
<h3 data-id="heading-7">3.提供init方法，监听变化，跳转路由</h3>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// index.js</span>
<span class="hljs-function"><span class="hljs-title">init</span>(<span class="hljs-params">app</span>)</span>&#123;
    <span class="hljs-keyword">const</span> history = <span class="hljs-built_in">this</span>.history;
    <span class="hljs-comment">// 设置路径变化监听</span>
    <span class="hljs-keyword">const</span> setupHashListener = <span class="hljs-function">()=></span>&#123;
      history.setupListener();
    &#125;
    <span class="hljs-comment">// 注册路由变化函数</span>
    history.listen(<span class="hljs-function">(<span class="hljs-params">route</span>)=></span>&#123;
      app._route = route
    &#125;)
    <span class="hljs-comment">// 跳转路由</span>
    history.transitionTo(
      history.getCurrentLocation(),
      setupHashListener
    )
  &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-8">4.然后提供别的push等等方法进行路由操作</h3>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// index.js</span>
<span class="hljs-function"><span class="hljs-title">push</span>(<span class="hljs-params">location</span>)</span>&#123;
    <span class="hljs-built_in">this</span>.history.push(location)
  &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-9">5.实现router-view组件</h3>
<p>新建components文件夹</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// components/view.js</span>
<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> &#123;
  <span class="hljs-attr">functional</span>: <span class="hljs-literal">true</span>,
  <span class="hljs-function"><span class="hljs-title">render</span>(<span class="hljs-params">h,&#123;parent,data&#125;</span>)</span>&#123;  <span class="hljs-comment">//动态渲染 </span>
    <span class="hljs-keyword">let</span> route = parent.$route;
    <span class="hljs-keyword">let</span> depth = <span class="hljs-number">0</span>;
    data.routerView = <span class="hljs-literal">true</span>;
    <span class="hljs-keyword">while</span>(parent)&#123;
      <span class="hljs-keyword">if</span>(parent.$vnode && parent.$vnode.data.routerView)&#123;
        depth++;
      &#125;
      parent = parent.$parent;
    &#125;
    <span class="hljs-keyword">let</span> record = route.matched[depth];
    <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'record:'</span>,record);
    <span class="hljs-keyword">if</span>(!record)&#123;
      <span class="hljs-keyword">return</span> h();
    &#125;
    <span class="hljs-keyword">return</span> h(record.component,data);
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-10">实现router-link组件</h3>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// components/link.js</span>
<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> &#123;
  <span class="hljs-attr">props</span>:&#123;
      <span class="hljs-attr">to</span>:&#123;
          <span class="hljs-attr">type</span>:<span class="hljs-built_in">String</span>,
          <span class="hljs-attr">required</span>:<span class="hljs-literal">true</span>
      &#125;,
      <span class="hljs-attr">tag</span>:&#123;
          <span class="hljs-attr">type</span>:<span class="hljs-built_in">String</span>
      &#125;
  &#125;,
  <span class="hljs-function"><span class="hljs-title">render</span>(<span class="hljs-params"></span>)</span>&#123;
    <span class="hljs-keyword">let</span> tag = <span class="hljs-built_in">this</span>.tag || <span class="hljs-string">'a'</span>;
    <span class="hljs-keyword">let</span> handler = <span class="hljs-function">()=></span>&#123;
        <span class="hljs-built_in">this</span>.$router.push(<span class="hljs-built_in">this</span>.to);
    &#125;
    <span class="hljs-keyword">return</span> <span class="xml"><span class="hljs-tag"><<span class="hljs-name">tag</span> <span class="hljs-attr">onClick</span>=<span class="hljs-string">&#123;handler&#125;</span>></span>&#123;this.$slots.default&#125;<span class="hljs-tag"></<span class="hljs-name">tag</span>></span></span>
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre></div>  
</div>
            