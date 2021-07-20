
---
title: 'Vue路由'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/2abf9a5204ab42bdb2ec8aa1a6baf833~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Tue, 20 Jul 2021 01:02:26 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/2abf9a5204ab42bdb2ec8aa1a6baf833~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h3 data-id="heading-0">Hash模式</h3>
<p>vue-router默认使用是Hash模式，Hash模式主要是通过url中的hash值来变化的。<code>Hash（即#）是url的一个锚点，代表的是网页中的一个位置，当hash值变化时，浏览器就滚动到相应的位置，所以不会重新加载页面</code>。在hash值变化的同时url会被浏览器记录下来，这样既可以使用浏览器的后退了。</p>
<p><strong>总结：Hash模式就是通过改变url中#后面的值，实现浏览器渲染指定的组件</strong></p>
<h3 data-id="heading-1">History模式</h3>
<p>这种模式利用了HTML5 History新增的<strong>pushState()和replaceState()方法.</strong> 除了之前的back,forward,go方法,这两个新方法可以应用在浏览器历史记录的增加替换功能上.使用History模式,通过历史记录修改url,但它不会立即向后端发送请求. <strong><code>注意点:</code></strong> 虽然History模式可以丢掉不美观的#,也可以正常的前进后退,但是刷新f5后,此时浏览器就会访问服务器,在没有后台支持的情况下,此时就会得到一个404!官方文档给出的描述是:"不过这种模式要玩好,还需要后台配置支持.因为我们的应用是单个客户端应用,如果后台没有正确的配置,当用户直接访问时,就会返回404.所以呢,你要在服务端增加一个覆盖所有情况的的候选资源;如果url匹配不到任何静态资源,则应该返回同一个index.html页面."\</p>
<ul>
<li><code>history.pushState()</code>:跳转到页面，并且有记录</li>
<li><code>history.replaceState()</code>:跳转页面，没有记录</li>
<li><code>history.go()</code>:后退几步或者前进几步</li>
<li><code>history.back()</code>:移除当前页面，返回上一个页面</li>
</ul>
<p>history相当于一个栈结构每次pushState就相当一次入栈，每次back就相当一次出栈</p>
<p><strong>总结:History模式就是pushState()方法来对浏览器记录进行修改从而进行修改</strong></p>
<h3 data-id="heading-2">路由的配置实例 router.js文件</h3>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">//第一步：引入必要文件</span>
<span class="hljs-keyword">import</span> Vue <span class="hljs-keyword">from</span> <span class="hljs-string">'vue'</span>
<span class="hljs-keyword">import</span> VueRouter <span class="hljs-keyword">from</span> <span class="hljs-string">'vue-router'</span>
<span class="hljs-comment">//引入是路由需要的组件</span>
<span class="hljs-keyword">import</span> Home <span class="hljs-keyword">from</span> <span class="hljs-string">'../views/Home.vue'</span>

<span class="hljs-comment">//第二步:加载全局组件Router</span>
Vue.use(VueRouter)

<span class="hljs-comment">//第三步:配置路由实例</span>
<span class="hljs-keyword">const</span> router = <span class="hljs-keyword">new</span> VueRouter(&#123;
  <span class="hljs-comment">//设置路由模式：默认是hash，在框架中改为history，配合后端使用</span>
  <span class="hljs-attr">mode</span>: <span class="hljs-string">'history'</span>,
  <span class="hljs-comment">//基路径:默认值为'/'.如果整个单页应用在/app/下,base就应该设为'/app/'.一般可以写成__dirname,在webpack中配置.</span>
  <span class="hljs-attr">base</span>: process.env.BASE_URL,
  <span class="hljs-comment">//注册路由</span>
  routes
&#125;)

<span class="hljs-keyword">const</span> routes = [
  &#123;
    <span class="hljs-comment">//路由的地址</span>
    <span class="hljs-attr">path</span>: <span class="hljs-string">'/'</span>,
    <span class="hljs-comment">//给路由命名，name必须是唯一的</span>
    <span class="hljs-attr">name</span>: <span class="hljs-string">'Home'</span>,
    <span class="hljs-comment">//需要显示的组件（这里是因为上面引入过了，应该写路径）</span>
    <span class="hljs-attr">component</span>: Home
  &#125;,
  &#123;
    <span class="hljs-attr">path</span>: <span class="hljs-string">'/about'</span>,
    <span class="hljs-attr">name</span>: <span class="hljs-string">'About'</span>,
    <span class="hljs-attr">component</span>: <span class="hljs-function">() =></span> <span class="hljs-keyword">import</span>(<span class="hljs-string">'../views/About.vue'</span>)
  &#125;,
  &#123;
    <span class="hljs-attr">path</span>: <span class="hljs-string">'/home'</span>,
    <span class="hljs-attr">name</span>: <span class="hljs-string">'Home'</span>,
    <span class="hljs-attr">component</span>: <span class="hljs-function">() =></span> <span class="hljs-keyword">import</span>(<span class="hljs-string">'../views/Home.vue'</span>)
  &#125;
]

<span class="hljs-comment">//第四步：将配置的路由实例抛出</span>
<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> router
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-3">将router.js文件挂载到vue实例中（main.js中）</h3>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/2abf9a5204ab42bdb2ec8aa1a6baf833~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-4"> router,routes,route的意思</h3>
<p>1.router:代表路由实例，如<code>$router</code>
2.routers:指router路由实例的routes API.用来配置多个route路由对象.
3.route:代表自身组件的路由对象，如<code>$route</code></p>
<h3 data-id="heading-5">页面标签</h3>
<p>1.router-link组件点击跳转到对应的页面
2.router-view组件，路由的出口（可以做路由嵌套）</p>
<pre><code class="hljs language-js copyable" lang="js">  <div <span class="hljs-class"><span class="hljs-keyword">class</span></span>=<span class="hljs-string">"home"</span>>
  
     <span class="hljs-comment">//router-link:跳转标签</span>
     <span class="hljs-comment">// to：跳转的地址</span>
    <span class="xml"><span class="hljs-tag"><<span class="hljs-name">router-link</span> <span class="hljs-attr">to</span>=<span class="hljs-string">"/about"</span>></span>111<span class="hljs-tag"></<span class="hljs-name">router-link</span>></span></span>
    
    <span class="hljs-comment">//路由匹配到的组件全部渲染到这里</span>
    <span class="xml"><span class="hljs-tag"><<span class="hljs-name">router-view</span>></span><span class="hljs-tag"></<span class="hljs-name">router-view</span>></span></span>
    
  </div>
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-6">JavaScript跳转</h3>
<p>1.this.$router.push(),有页面的记录</p>
<pre><code class="hljs language-js copyable" lang="js"> methods: &#123;
    <span class="hljs-function"><span class="hljs-title">toHome</span>(<span class="hljs-params"></span>)</span> &#123;
    
      <span class="hljs-comment">//单纯跳转</span>
      <span class="hljs-built_in">this</span>.$router.push(<span class="hljs-string">"/home"</span>);
      
      <span class="hljs-comment">//使用path跳转  query传参</span>
      <span class="hljs-built_in">this</span>.$router.push(&#123;<span class="hljs-attr">path</span>:<span class="hljs-string">"地址"</span>,<span class="hljs-attr">query</span>:参数&#125;)
      
      <span class="hljs-comment">//使用name跳转  params传参</span>
      <span class="hljs-built_in">this</span>.$router.push(&#123;<span class="hljs-attr">path</span>:<span class="hljs-string">"地址"</span>,<span class="hljs-attr">params</span>:参数&#125;)
     
    &#125;,
 &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="hljs language-js copyable" lang="js">  <span class="hljs-function"><span class="hljs-title">created</span>(<span class="hljs-params"></span>)</span> &#123;
    <span class="hljs-comment">// 用path跳转 使用this.$route.query获取</span>
    <span class="hljs-built_in">console</span>.log(<span class="hljs-built_in">this</span>.$route.query);
  
    <span class="hljs-comment">// 用name跳转 使用this.$route.params获取</span>
    <span class="hljs-built_in">console</span>.log(<span class="hljs-built_in">this</span>.$route.params);
  &#125;,
<span class="copy-code-btn">复制代码</span></code></pre>
<p>2.<code>this.$router.replace()</code>,没有页面的记录(其余的和<code>this.$router.push</code>一样)<br>
3.<code>this.$router.go()</code>这个方法的参数是一个整数，意思是在 history 记录中向前或者后退多少步，类似 <code>window.history.go(n)</code>。</p>
<pre><code class="hljs language-js copyable" lang="js">    <span class="hljs-comment">//前进2步</span>
    <span class="hljs-built_in">this</span>.$router.go(<span class="hljs-number">2</span>);
    
    <span class="hljs-comment">//后退2步</span>
    <span class="hljs-built_in">this</span>.$router.go(-<span class="hljs-number">2</span>);
    
    <span class="hljs-comment">// 如果 history 记录不够用，不会跳转</span>
    router.go(-<span class="hljs-number">100</span>)
    router.go(<span class="hljs-number">100</span>)
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-7">嵌套路由</h3>
<pre><code class="hljs language-js copyable" lang="js">routes: [
    <span class="hljs-comment">//嵌套路由就写在children配置中,写法和routes一样.</span>
   &#123; <span class="hljs-attr">path</span>: <span class="hljs-string">'/user'</span>, 
    <span class="hljs-attr">component</span>: User,<span class="hljs-attr">name</span>:<span class="hljs-string">'user'</span>, 
    <span class="hljs-comment">//children:[&#123;&#125;] 也可以继续添加children嵌套 </span>
    <span class="hljs-attr">children</span>: [
        <span class="hljs-comment">//如果/user下没有匹配到其他子路由时,User的<router-view>是什么都不会显示的,如果你想让它显示点什么.可以将path:''.设为空.此时UserDefault就是默认显示的组件.</span>
        &#123; <span class="hljs-attr">path</span>: <span class="hljs-string">''</span>, <span class="hljs-attr">component</span>: UserDefault ,<span class="hljs-attr">name</span>:<span class="hljs-string">'default'</span>, &#125;, 
        <span class="hljs-comment">//此时path等同于'/user/foo',子路由会继承父路由的路径.但是不能写成path:'/foo'.因为以 / 开头的嵌套路径会被当作根路径,也就是说此时foo成了根路径.而不是user. </span>
        &#123; <span class="hljs-attr">path</span>: <span class="hljs-string">'foo'</span>, <span class="hljs-attr">component</span>: UserFoo,<span class="hljs-attr">name</span>:<span class="hljs-string">'foo'</span>&#125;, 
        &#123; <span class="hljs-attr">path</span>: <span class="hljs-string">'bar'</span>, <span class="hljs-attr">component</span>: UserBar,<span class="hljs-attr">name</span>:<span class="hljs-string">'bar'</span> &#125; 
      ] 
   &#125; 
]


<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-8">重定向</h3>
<pre><code class="hljs language-js copyable" lang="js">routes:[ 
    &#123;
        <span class="hljs-attr">path</span>:<span class="hljs-string">'/a'</span>,
        <span class="hljs-comment">//从 /a 重定向到 /b </span>
        <span class="hljs-attr">redirect</span>:<span class="hljs-string">'/b'</span>
    &#125; 
]  /
<span class="hljs-comment">//从 /a 重定向到 命名为'foo'的路由 </span>
routes: [ &#123; <span class="hljs-attr">path</span>: <span class="hljs-string">'/a'</span>, <span class="hljs-attr">redirect</span>: &#123; <span class="hljs-attr">name</span>: <span class="hljs-string">'foo'</span> &#125;&#125; ]

<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-9">路由守卫</h3>
<ul>
<li>
<p><strong><code>to: Route</code></strong>: 即将要进入的目标 <a href="https://link.juejin.cn/?target=https%3A%2F%2Frouter.vuejs.org%2Fzh%2Fapi%2F%23%25E8%25B7%25AF%25E7%2594%25B1%25E5%25AF%25B9%25E8%25B1%25A1" title="https://link.juejin.cn/?target=https%3A%2F%2Frouter.vuejs.org%2Fzh%2Fapi%2F%23%25E8%25B7%25AF%25E7%2594%25B1%25E5%25AF%25B9%25E8%25B1%25A1" target="_blank">路由对象</a></p>
</li>
<li>
<p><strong><code>from: Route</code></strong>: 当前导航正要离开的路由对象</p>
</li>
<li>
<p><strong><code>next: Function</code></strong>: 一定要调用该方法来 <strong>resolve</strong> 这个钩子。执行效果依赖 <code>next</code> 方法的调用参数。</p>
<ul>
<li><strong><code>next()</code></strong> : 进行管道中的下一个钩子。如果全部钩子执行完了，则导航的状态就是 <strong>confirmed</strong> (确认的)。</li>
<li><strong><code>next(false)</code></strong> : 中断当前的导航。如果浏览器的 URL 改变了 (可能是用户手动或者浏览器后退按钮)，那么 URL 地址会重置到 <code>from</code> 路由对应的地址。</li>
<li><strong><code>next('/')</code> 或者 <code>next(&#123; path: '/' &#125;)</code></strong> : 跳转到一个不同的地址。当前的导航被中断，然后进行一个新的导航。你可以向 <code>next</code> 传递任意位置对象，且允许设置诸如 <code>replace: true</code>、<code>name: 'home'</code> 之类的选项以及任何用在 <a href="https://link.juejin.cn/?target=https%3A%2F%2Frouter.vuejs.org%2Fzh%2Fapi%2F%23to" title="https://link.juejin.cn/?target=https%3A%2F%2Frouter.vuejs.org%2Fzh%2Fapi%2F%23to" target="_blank"><code>router-link</code> 的 <code>to</code> prop</a> 或 <a href="https://link.juejin.cn/?target=https%3A%2F%2Frouter.vuejs.org%2Fzh%2Fapi%2F%23router-push" title="https://link.juejin.cn/?target=https%3A%2F%2Frouter.vuejs.org%2Fzh%2Fapi%2F%23router-push" target="_blank"><code>router.push</code></a> 中的选项。</li>
<li><strong><code>next(error)</code></strong> : (2.4.0+) 如果传入 <code>next</code> 的参数是一个 <code>Error</code> 实例，则导航会被终止且该错误会被传递给 <a href="https://link.juejin.cn/?target=https%3A%2F%2Frouter.vuejs.org%2Fzh%2Fapi%2F%23router-onerror" title="https://link.juejin.cn/?target=https%3A%2F%2Frouter.vuejs.org%2Fzh%2Fapi%2F%23router-onerror" target="_blank"><code>router.onError()</code></a> 注册过的回调。</li>
</ul>
</li>
</ul>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">//1,可以在main.js 或者在单独的路由配置文件router.js中进行设置</span>
router.beforeEach(<span class="hljs-function">(<span class="hljs-params">to, <span class="hljs-keyword">from</span>, next</span>) =></span> &#123; 

      next();
    &#125;);

<span class="hljs-comment">//2,也可以在组件内部设置</span>
<span class="hljs-built_in">this</span>.$router.beforeEach(<span class="hljs-function">(<span class="hljs-params">to, <span class="hljs-keyword">from</span>, next</span>) =></span> &#123; 

      next();
    &#125;);
<span class="copy-code-btn">复制代码</span></code></pre></div>  
</div>
            