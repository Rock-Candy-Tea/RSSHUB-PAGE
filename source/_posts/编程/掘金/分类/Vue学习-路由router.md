
---
title: 'Vue学习-路由router'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/e7c6e6853ff24840b8b643300f776c24~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Tue, 29 Jun 2021 09:03:26 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/e7c6e6853ff24840b8b643300f776c24~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h1 data-id="heading-0">Vue学习-路由router</h1>
<h2 data-id="heading-1">认识路由</h2>
<h3 data-id="heading-2">什么是前端渲染，什么是后端渲染？</h3>
<h4 data-id="heading-3">后端渲染阶段</h4>
<p>后端渲染： JSP - java server page</p>
<p>后台收到请求之后，html+css+java, java代码作用是从数据库中读取数据，并将它动态的放在页面中，页面在服务器端已经渲染好了，然后直接渲染好的页面返回给前端（html+css）</p>
<p>后端路由：后台处理URL和页面之间的映射关系</p>
<p>后端路由的缺点：</p>
<ul>
<li>整个页面的模块由后端人员来编写和维护的</li>
<li>前端开发人员如果开发页面，需要通过PHP，Java等语言来编写页面代码</li>
<li>通常情况下HTML代码和数据以及对应的逻辑会混在一起，编写和维护都是非常糟糕的事情</li>
</ul>
<h4 data-id="heading-4">前后端分离阶段</h4>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/e7c6e6853ff24840b8b643300f776c24~tplv-k3u1fbpfcp-watermark.image" alt="前后端分离.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>输入jd.com，先去静态资源浏览器请求静态资源（html+css+js），当浏览器引擎执行JS代码时，会触发API请求，会去后台的API服务器上请求数据。</p>
<p>前端渲染：浏览器中显示的网页中的大部分内容，都是由前端写的JS代码，在浏览器中执行，最终渲染出来的网页。</p>
<ul>
<li>随着Ajax的出现，由了前后端分离的开发模式</li>
<li>后端只提供API来返回数据，前端通过Ajax获取数据，并且可以通过JS将数据渲染到页面中</li>
<li>这样做最大的优点就是前后端责任的清晰，后端专注于数据上，前端专注于交互和可视化上</li>
<li>并且当移动端出现后，后端不需要进行任何处理，依然使用之前的一套API即可</li>
</ul>
<h4 data-id="heading-5">前端路由阶段（单页面富应用阶段）</h4>
<p>前后端分离的基础之上，加上前端路由</p>
<p>SPA应用：整个网站只有一个HTML页面，一套html+css+js</p>
<p>前端路由：页面与静态资源的映射关系由前端来管理，改变URL，页面不会整体刷新</p>
<h3 data-id="heading-6">url的hash和HTML5的history</h3>
<h4 data-id="heading-7">URL中的hash</h4>
<ul>
<li>URL中的hash也就是锚点(#)，本质上是改变window.location的href属性</li>
<li>可以通过直接赋值location.hash来改变href，但是页面不会发生刷新</li>
<li><code>location.hash = 'aaa'</code></li>
</ul>
<h4 data-id="heading-8">HTML5中的history</h4>
<ul>
<li><code>history.pushState(&#123;&#125;, '', 'home')</code>  压入</li>
<li><code>history.replaceState(&#123;&#125;, '', 'home')</code>  替换</li>
<li>replace不能返回之前的页面（替换了）, push可以返回到之前的页面</li>
<li><code>history.go()</code> 参数： -1： <code>history.back()</code> 1: <code>history.forward()</code></li>
</ul>
<h2 data-id="heading-9">Vue-router基本使用</h2>
<h3 data-id="heading-10">安装vue-router</h3>
<pre><code class="copyable">npm install vue-router --save
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-11">在模块化工程中使用vue-router(插件，可以用过Vue.use()来使用路由功能)</h3>
<ul>
<li>导入路由对象，并且调用Vue.use(VueRouter)</li>
<li>创建路由实例，并且传入路由映射配置</li>
<li>Vue实例中挂载创建的路由实例</li>
</ul>
<p>框架搭建</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">import</span> Vue <span class="hljs-keyword">from</span> <span class="hljs-string">'vue'</span>
<span class="hljs-comment">// 导入路由对象，并且调用Vue.use(VueRouter)</span>
<span class="hljs-keyword">import</span> VueRouter <span class="hljs-keyword">from</span> <span class="hljs-string">'vue-router'</span>
<span class="hljs-keyword">import</span> Home <span class="hljs-keyword">from</span> <span class="hljs-string">'../views/Home.vue'</span>

Vue.use(VueRouter)

<span class="hljs-comment">// 创建路由实例，并且传入路由映射配置</span>
<span class="hljs-keyword">const</span> routes = [
    &#123;
        <span class="hljs-attr">path</span>: <span class="hljs-string">'/'</span>,
        <span class="hljs-attr">name</span>: <span class="hljs-string">'Home'</span>,
        <span class="hljs-attr">component</span>: Home
    &#125;,
    &#123;
        <span class="hljs-attr">path</span>: <span class="hljs-string">'/about'</span>,
        <span class="hljs-attr">name</span>: <span class="hljs-string">'About'</span>,
        <span class="hljs-comment">// route level code-splitting</span>
        <span class="hljs-comment">// this generates a separate chunk (about.[hash].js) for this route</span>
        <span class="hljs-comment">// which is lazy-loaded when the route is visited.</span>
        <span class="hljs-attr">component</span>: <span class="hljs-function">() =></span> <span class="hljs-keyword">import</span>(<span class="hljs-comment">/* webpackChunkName: "about" */</span> <span class="hljs-string">'../views/About.vue'</span>)
    &#125;
]

<span class="hljs-keyword">const</span> router = <span class="hljs-keyword">new</span> VueRouter(&#123;
    <span class="hljs-attr">mode</span>: <span class="hljs-string">'history'</span>,
    <span class="hljs-attr">base</span>: process.env.BASE_URL,
    routes
&#125;)

<span class="hljs-comment">// 先导出，然后在main.js中，Vue实例中挂载创建的路由实例</span>
<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> router

<span class="copy-code-btn">复制代码</span></code></pre>
<p>配置路由</p>
<ul>
<li>创建路由组件</li>
<li>配置路由映射：组件和路径映射关系</li>
<li>使用路由：通过和</li>
</ul>
<pre><code class="hljs language-js copyable" lang="js">&#123;
    <span class="hljs-attr">path</span>: <span class="hljs-string">'/'</span>,
        <span class="hljs-attr">name</span>: <span class="hljs-string">'Home'</span>,
            <span class="hljs-attr">component</span>: Home
&#125;,
    &#123;
        <span class="hljs-attr">path</span>: <span class="hljs-string">'/about'</span>,
            <span class="hljs-attr">name</span>: <span class="hljs-string">'About'</span>,
                <span class="hljs-comment">// route level code-splitting</span>
                <span class="hljs-comment">// this generates a separate chunk (about.[hash].js) for this route</span>
                <span class="hljs-comment">// which is lazy-loaded when the route is visited.</span>
                <span class="hljs-comment">// 路由懒加载</span>
                <span class="hljs-attr">component</span>: <span class="hljs-function">() =></span> <span class="hljs-keyword">import</span>(<span class="hljs-comment">/* webpackChunkName: "about" */</span> <span class="hljs-string">'../views/About.vue'</span>)
    &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">router-link</span> <span class="hljs-attr">to</span>=<span class="hljs-string">"/home"</span>></span>首页<span class="hljs-tag"></<span class="hljs-name">router-link</span>></span>
<span class="hljs-tag"><<span class="hljs-name">router-link</span> <span class="hljs-attr">to</span>=<span class="hljs-string">"/about"</span>></span>关于<span class="hljs-tag"></<span class="hljs-name">router-link</span>></span>
<span class="hljs-tag"><<span class="hljs-name">router-view</span>></span><span class="hljs-tag"></<span class="hljs-name">router-view</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-12">路由的默认值和修改为history模式</h3>
<h4 data-id="heading-13">路由的默认值</h4>
<pre><code class="copyable">&#123; path: '/', redirect: 'home' &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-14">history模式</h4>
<p>mode: history</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> router = <span class="hljs-keyword">new</span> VueRouter(&#123;
    <span class="hljs-attr">mode</span>: <span class="hljs-string">'history'</span>,
    <span class="hljs-attr">base</span>: process.env.BASE_URL,
    routes
&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-15">router-link的其他属性</h3>
<h4 data-id="heading-16">tag属性</h4>
<p>默认渲染为a标签，想要渲染为其他元素，使用tag属性</p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">router-link</span> <span class="hljs-attr">to</span>=<span class="hljs-string">"/home"</span> <span class="hljs-attr">tag</span>=<span class="hljs-string">"button"</span>></span>首页<span class="hljs-tag"></<span class="hljs-name">router-link</span>></span>
<span class="hljs-tag"><<span class="hljs-name">router-link</span> <span class="hljs-attr">to</span>=<span class="hljs-string">"/about"</span> <span class="hljs-attr">tag</span>=<span class="hljs-string">"button"</span>></span>关于<span class="hljs-tag"></<span class="hljs-name">router-link</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-17">replace属性</h4>
<p>默认使用pushState，如果想使用replaceState,使用replace属性</p>
<pre><code class="copyable"><router-link to="/home" tag="button" replace>首页</router-link>
<router-link to="/about" tag="button" replace>关于</router-link>
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-18">.router-link-active</h4>
<p>选中的router-link会自动具有.router-link-active类，可以直接通过该类设置样式，比如选中的字体变为红色</p>
<pre><code class="copyable">.router-link-active &#123;
color: red;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>.router-link-active简写模式</p>
<pre><code class="copyable"><router-link to="/home" tag="button" replace active-class="acive">首页</router-link>
<router-link to="/about" tag="button" replace active-class="acive">关于</router-link>
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="copyable">.active &#123;
color: red;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>统一修改active-class</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">const</span> router = <span class="hljs-keyword">new</span> VueRouter(&#123;
    <span class="hljs-attr">mode</span>: <span class="hljs-string">'history'</span>,
    <span class="hljs-attr">base</span>: process.env.BASE_URL,
    routes,
    <span class="hljs-attr">linkActiveClass</span>: <span class="hljs-string">'active'</span>
&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-19">通过代码跳转路由</h3>
<pre><code class="copyable">this.$router.push('/home');
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="copyable">this.$router.replace('/home')
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-20">动态路由</h3>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">router-link</span> <span class="hljs-attr">to</span>=<span class="hljs-string">"/home"</span>></span>首页<span class="hljs-tag"></<span class="hljs-name">router-link</span>></span>
<span class="hljs-tag"><<span class="hljs-name">router-link</span> <span class="hljs-attr">to</span>=<span class="hljs-string">"/about"</span>></span>关于<span class="hljs-tag"></<span class="hljs-name">router-link</span>></span>
<span class="hljs-tag"><<span class="hljs-name">router-link</span> <span class="hljs-attr">to</span>=<span class="hljs-string">"/user/zhangsan"</span>></span>用户<span class="hljs-tag"></<span class="hljs-name">router-link</span>></span>
<span class="hljs-tag"><<span class="hljs-name">router-link</span> <span class="hljs-attr">:to</span>=<span class="hljs-string">"'/user/' + userId"</span>></span>用户<span class="hljs-tag"></<span class="hljs-name">router-link</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="hljs language-js copyable" lang="js">&#123; <span class="hljs-attr">path</span>: <span class="hljs-string">'/user/:userId'</span>, <span class="hljs-attr">component</span>: User &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>或者</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-built_in">this</span>.$router.push(<span class="hljs-string">'/user/'</span> + <span class="hljs-built_in">this</span>.userId)
<span class="copy-code-btn">复制代码</span></code></pre>
<p><code>User.vue</code>中获取到<code>userId</code></p>
<pre><code class="copyable">&#123;&#123; $route.params.userId &#125;&#125;
或者
this.$route.params.userId
// $route: 处于活跃中的路由
// $router: 整个路由对象
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-21">路由的懒加载</h3>
<ul>
<li>
<p>当打包构建应用时，Javascript包会变得非常大，影响页面加载</p>
</li>
<li>
<p>如果我们能把不同路由对应的组件分割成不同的代码块，然后当路由被访问的时候才加载对应组件，这样跟高效（一个路由打包一个JS文件）</p>
</li>
<li>
<p>懒加载：用到的时候再加载</p>
</li>
</ul>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// 推荐的方式</span>
<span class="hljs-keyword">const</span> routes = [
&#123; <span class="hljs-attr">path</span>: <span class="hljs-string">'/home'</span>, <span class="hljs-attr">component</span>: <span class="hljs-function">() =></span> <span class="hljs-keyword">import</span>(<span class="hljs-string">'../components/Home'</span>) &#125;,
    &#123; <span class="hljs-attr">path</span>: <span class="hljs-string">'/about'</span>, <span class="hljs-attr">component</span>: <span class="hljs-function">() =></span> <span class="hljs-keyword">import</span>(<span class="hljs-string">'../components/About'</span>) &#125;
]
<span class="copy-code-btn">复制代码</span></code></pre>
<p>或者</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> About = <span class="hljs-function"><span class="hljs-params">resolve</span> =></span> <span class="hljs-built_in">require</span>([<span class="hljs-string">'../components/About.vue'</span>], resolve);
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-22">Vue-router嵌套路由</h2>
<h3 data-id="heading-23">认识路由嵌套</h3>
<ul>
<li>比如在home页面中，我们希望通过/home/news和/home/message访问一些内容</li>
<li>一个路径映射一个组件，访问这两个路径也会分别渲染两个组件</li>
</ul>
<p>创建嵌套路由的步骤</p>
<ul>
<li>创建对应的子组件，并且在路由映射中配置对应的子路由</li>
<li>在组件内部使用标签</li>
</ul>
<pre><code class="hljs language-js copyable" lang="js">&#123; <span class="hljs-attr">path</span>:  <span class="hljs-string">'/home'</span>, <span class="hljs-attr">component</span>: Home, <span class="hljs-attr">children</span>: [
    &#123; <span class="hljs-attr">path</span>: <span class="hljs-string">'news'</span>, <span class="hljs-attr">component</span>: HomeNews &#125;,
    &#123; <span class="hljs-attr">path</span>: <span class="hljs-string">'message'</span>, <span class="hljs-attr">component</span>: HomeMessage &#125;,
    &#123; <span class="hljs-attr">path</span>: <span class="hljs-string">'/'</span>, <span class="hljs-attr">redirect</span>: <span class="hljs-string">'news'</span> &#125;
] &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">router-link</span> <span class="hljs-attr">to</span>=<span class="hljs-string">"/home/news"</span>></span>新闻<span class="hljs-tag"></<span class="hljs-name">router-link</span>></span>
<span class="hljs-tag"><<span class="hljs-name">router-link</span> <span class="hljs-attr">to</span>=<span class="hljs-string">"/home/message"</span>></span>消息<span class="hljs-tag"></<span class="hljs-name">router-link</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-24">Vue-router参数传递</h2>
<p>从一个页面跳转到另一个页面，希望传递一些消息</p>
<p>方法1： 动态路由中讲到的方法可以传递参数</p>
<ul>
<li>配置路由格式： /router/:id</li>
<li>传递的方式： 在path后面跟上对应的值</li>
<li>传递后形成的路径： /route/123, /route/abc</li>
</ul>
<p>方法2： query方式</p>
<ul>
<li>配置路由格式：/router，也就是普通配置</li>
<li>传递的方式：对象中使用query的key作为传递方式</li>
<li>传递后形成的路径: /router?id=123 , /router?id=abc</li>
</ul>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">router-link</span> <span class="hljs-attr">:to</span>=<span class="hljs-string">"&#123; path: '/profile', query: &#123; name: 'xx', age: 18, height: 1.88 &#125; &#125;"</span>></span><span class="hljs-tag"></<span class="hljs-name">router-link</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>或者</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-built_in">this</span>.$router.push(&#123;
<span class="hljs-attr">path</span>: <span class="hljs-string">'/profile'</span>,
    <span class="hljs-attr">query</span>: &#123;
        <span class="hljs-attr">name</span>: <span class="hljs-string">'xx'</span>,
        <span class="hljs-attr">age</span>: <span class="hljs-number">18</span>,
        <span class="hljs-attr">height</span>: <span class="hljs-number">1.88</span>
    &#125;
&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="copyable">&#123;&#123; $route.query.name &#125;&#125;
或者
this.$route.query.name
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-25">Vue-router: router和route的由来</h2>
<p>所有组件(.vue)都继承着vue的原型，vue原型上又挂载了<span class="math math-inline"><span class="katex"><span class="katex-mathml"><math xmlns="http://www.w3.org/1998/Math/MathML"><semantics><mrow><mi>r</mi><mi>o</mi><mi>u</mi><mi>t</mi><mi>e</mi><mi>r</mi><mi>g</mi><mtext>和</mtext></mrow><annotation encoding="application/x-tex">routerg和</annotation></semantics></math></span><span class="katex-html" aria-hidden="true"><span class="base"><span class="strut" style="height:0.8777699999999999em;vertical-align:-0.19444em;"></span><span class="mord mathnormal" style="margin-right:0.02778em;">r</span><span class="mord mathnormal">o</span><span class="mord mathnormal">u</span><span class="mord mathnormal">t</span><span class="mord mathnormal">e</span><span class="mord mathnormal" style="margin-right:0.02778em;">r</span><span class="mord mathnormal" style="margin-right:0.03588em;">g</span><span class="mord cjk_fallback">和</span></span></span></span></span>route</p>
<pre><code class="hljs language-js copyable" lang="js">Vue.prototype.$router = &#123;
...
&#125;
Vue.prototype.$route = &#123;
    ...
&#125;
或者
<span class="hljs-built_in">Object</span>.defineProperty(Vue.prototype, <span class="hljs-string">'$router'</span>, ...);
<span class="hljs-built_in">Object</span>.defineProperty(Vue.prototype, <span class="hljs-string">'$route'</span>, ...);
<span class="copy-code-btn">复制代码</span></code></pre>
<p><code>this.$router</code>就是vueRouter类的一个实例</p>
<p><code>this.$route</code>是处于活跃的路由</p>
<h2 data-id="heading-26">Vue-router导航守卫</h2>
<h3 data-id="heading-27">需求：</h3>
<p>在一个SPA应用中，如何改变网页的标题？</p>
<ul>
<li>网页标题是通过<code><title></code>来显示的，但是SPA只有一个固定的HTML,切换不同的页面时，标题并不会改变</li>
<li>可以通过Javascript来修改<code><title></code>的内容，<code>window.document.title="新的标题"</code></li>
<li>那么在VUE项目中，如何实现？</li>
</ul>
<p>方案1： 利用生命周期函数created实现</p>
<p>方案2：利用全局导航守卫 (前置钩子,前置守卫)</p>
<pre><code class="hljs language-js copyable" lang="js">router.beforeEach(<span class="hljs-function">(<span class="hljs-params">to, <span class="hljs-keyword">from</span>, next</span>) =></span> &#123;
<span class="hljs-comment">// 从from跳转到to</span>
<span class="hljs-built_in">document</span>.title = to.matched[<span class="hljs-number">0</span>].meta.title;
    next();
&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="hljs language-js copyable" lang="js">&#123; <span class="hljs-attr">path</span>: <span class="hljs-string">'/home'</span>, <span class="hljs-attr">component</span>: Home, <span class="hljs-attr">meta</span>: &#123; <span class="hljs-attr">title</span>: <span class="hljs-string">'首页'</span> &#125; &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-28">后置钩子：</h3>
<p>afterEach, 已经跳转完了</p>
<pre><code class="copyable">router.afterEach((to, from) => &#123;

&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-29">路由独享守卫</h3>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> router = <span class="hljs-keyword">new</span> VueRouter(&#123;
<span class="hljs-attr">routes</span>: [&#123;
        <span class="hljs-attr">path</span>: <span class="hljs-string">'/foo'</span>,
        <span class="hljs-attr">component</span>: Foo,
        <span class="hljs-attr">beforeEnter</span>: <span class="hljs-function">(<span class="hljs-params">to, <span class="hljs-keyword">from</span>, next</span>) =></span> &#123;
            
        &#125;
    &#125;]
&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-30">keep-alive</h2>
<ul>
<li>keep-alive是Vue内置的一个组件，可以使被包含的组件保留状态，或避免重新渲染</li>
<li>router-view也是一个组件，如果直接被包在keep-alive中，所有路径匹配的到的视图组件都会被缓存</li>
</ul>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">keep-alive</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">router-view</span>></span><span class="hljs-tag"></<span class="hljs-name">router-view</span>></span>
<span class="hljs-tag"></<span class="hljs-name">keep-alive</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>
<p><code>activated()</code>和<code>deactivated()</code>钩子函数只有在被keep-alive包裹的时候才会生效</p>
</li>
<li>
<p>如果希望组件中的某一个被频繁的创建和销毁</p>
<p>这里 Profile,User逗号后面不要加空格</p>
<pre><code class="copyable"><keep-alive exclude="Profile,User">
    <router-view></router-view>
</keep-alive>
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
</ul>
<h2 data-id="heading-31">路径别名</h2>
<p>vue-cli3中可以使用<code>@</code>代替<code>src</code></p>
<h2 data-id="heading-32">案例</h2>
<h3 data-id="heading-33">App.vue</h3>
<pre><code class="hljs language-vue copyable" lang="vue"><template>
  <div id="app">
    <router-view></router-view>
    <tab-bar>
      <tab-bar-item path="/home" activeColor="red">
        <img src="./assets/image/tabbar/首页.svg" alt="" slot="item-icon">
        <img src="./assets/image/tabbar/首页_active.svg" alt="" slot="item-icon-active">
        <div slot="item-text">首页</div>
      </tab-bar-item>
      <tab-bar-item path="/category" activeColor="skyblue">
        <img src="./assets/image/tabbar/分类.svg" alt="" slot="item-icon">
        <img src="./assets/image/tabbar/分类_active.svg" alt="" slot="item-icon-active">
        <div slot="item-text">分类</div>
      </tab-bar-item>
      <tab-bar-item path="/cart" activeColor="green">
        <img src="./assets/image/tabbar/购物车.svg" alt="" slot="item-icon">
        <img src="./assets/image/tabbar/购物车_active.svg" alt="" slot="item-icon-active">
        <div slot="item-text">购物车</div>
      </tab-bar-item>
      <tab-bar-item path="/profile">
        <img src="./assets/image/tabbar/我的.svg" alt="" slot="item-icon">
        <img src="./assets/image/tabbar/我的_active.svg" alt="" slot="item-icon-active">
        <div slot="item-text">我的</div>
      </tab-bar-item>
    </tab-bar>
  </div>
</template>

<script>
import TabBar from "./components/tabbar/TabBar";
import TabBarItem from "./components/tabbar/TabBarItem";

export default &#123;
  name: 'App',
  components: &#123;
    TabBar,
    TabBarItem
  &#125;
&#125;
</script>

<style lang="css">
@import './assets/css/base.css';
</style>
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-34">TabBar.vue</h3>
<pre><code class="hljs language-vue copyable" lang="vue"><!--  -->
<template>
   <div id="tab-bar">
       <slot></slot>
   </div>
</template>

<script>
    export default &#123;
        name: 'TabBar',
        data () &#123;
            return &#123;
            &#125;;
        &#125;
    &#125;
</script>
<style lang='css' scoped>
    #tab-bar &#123;
        display: flex;
        background-color: #f6f6f6;
        position: fixed;
        left: 0;
        right: 0;
        bottom: 0;
        /* 阴影 */
        box-shadow:  0px -1px 1px rgba(100, 100, 100, 0.2);
    &#125;
</style>
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-35">TabBarItem.vue</h3>
<pre><code class="hljs language-vue copyable" lang="vue"><!--  -->
<template>
<div class="tab-bar-item" @click="itemClick">
    <div v-if="!isActive"><slot name="item-icon"></slot></div>
    <div v-else><slot name="item-icon-active"></slot></div>
    <div :style="activeStyle">
        <slot name="item-text"></slot>
    </div>
</div>
</template>

<script>
    export default &#123;
        name: 'TabBarItem',
        props: &#123;
            path: String,
            activeColor: &#123;
                type: String,
                default: 'red'
            &#125;
        &#125;,
        data() &#123;
            return &#123;
            &#125;;
        &#125;,
        methods: &#123;
            itemClick() &#123;
                this.$router.push(this.path).catch(err => &#123;&#125;);
            &#125;
        &#125;,
        computed: &#123;
            isActive() &#123;
                return this.$route.path.indexOf(this.path) !== -1;
            &#125;,
            activeStyle() &#123;
                return this.isActive ? &#123; color: this.activeColor &#125; : &#123;&#125;;
            &#125;
        &#125;
    &#125;;
</script>
<style lang='css' scoped>
    .tab-bar-item &#123;
        flex: 1;
        text-align: center;
        height: 49px;
        font-size: 14px;
    &#125;

    .tab-bar-item img &#123;
        width: 24px;
        height: 24px;
        margin-top: 3px;
        vertical-align: middle;
    &#125;

</style>
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-36">效果图</h3>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/57bd3eec80794ecf964dff9e094e1851~tplv-k3u1fbpfcp-watermark.image" alt="案例.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-37"></h3></div>  
</div>
            