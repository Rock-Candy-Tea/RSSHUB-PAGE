
---
title: 'vue-router详解'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/65197b100b464336bb1fcd6ebf5c46c3~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Tue, 10 Aug 2021 01:44:41 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/65197b100b464336bb1fcd6ebf5c46c3~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>官方文档：
<a href="https://link.juejin.cn/?target=https%3A%2F%2Frouter.vuejs.org%2Fzh%2Finstallation.html" target="_blank" rel="nofollow noopener noreferrer" title="https://router.vuejs.org/zh/installation.html" ref="nofollow noopener noreferrer">router.vuejs.org/zh/installa…</a></p>
<h1 data-id="heading-0">一、路由规则（基础）</h1>
<p>所谓前端路由，即改变URL，但是页面不进行整体的刷新。实现方式主要有下面两种方式</p>
<h3 data-id="heading-1">1. URL的hash</h3>
<p>URL 的 <code>hash</code> 也就是锚点 (<code>#</code>), 本质上是改变 <code>window.location</code> 的 <code>href</code> 属性。可以通过直接赋值 <code>location.hash</code> 来改变 <code>href</code>，但是页面不发生刷新</p>
<p>直接在浏览器的命令行测试：</p>
<pre><code class="hljs language-js copyable" lang="js">> location.href
<span class="hljs-string">"http://localhost:8080"</span>
> location.hash=<span class="hljs-string">'/foo'</span>
<span class="hljs-string">"/foo"</span>
> location.href
<span class="hljs-string">"http://localhost:8080/#/foo"</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>查看 Network，可以看到页面并没有刷新</p>
<h3 data-id="heading-2">2. HTML5的history模式</h3>
<p><code>history</code> 接口是 HTML5 新增的, 它有五种模式改变 URL 而不刷新页面</p>
<ol>
<li>
<p><code>history.pushState(data: any, title: string, url?: string | null)</code>
可以理解为压栈，将新的 url 压入栈中，浏览器的 地址栏只显示栈中最上面的 url</p>
<pre><code class="hljs language-js copyable" lang="js">> location.href
<span class="hljs-string">"http://localhost:8080/"</span>
> history.pushState(&#123;&#125;,<span class="hljs-string">''</span>,<span class="hljs-string">"/app"</span>)
<span class="hljs-literal">undefined</span>
> location.href
<span class="hljs-string">"http://localhost:8080/app"</span>
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
<li>
<p><code>history.replaceState(data: any, title: string, url?: string | null)</code>
不保留当前 url，直接替换。</p>
</li>
<li>
<p><code>history.go(delta?: number)</code>
传入一个数字，正数表示向前跳转几次，负数表示向后跳转几次，</p>
<pre><code class="hljs language-js copyable" lang="js">> location.href
<span class="hljs-string">"http://localhost:8080/"</span>
> history.pushState(&#123;&#125;,<span class="hljs-string">''</span>,<span class="hljs-string">"/app"</span>)
<span class="hljs-literal">undefined</span>
> location.href
<span class="hljs-string">"http://localhost:8080/app"</span>
> history.replaceState(&#123;&#125;,<span class="hljs-string">''</span>,<span class="hljs-string">'/demo'</span>)
<span class="hljs-literal">undefined</span>
> location.href
<span class="hljs-string">"http://localhost:8080/demo"</span>
> history.go(-<span class="hljs-number">1</span>)
<span class="hljs-literal">undefined</span>
> location.href
<span class="hljs-string">"http://localhost:8080/"</span>
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
<li>
<p><code>history.back()</code>
等价于：history.go(-1)</p>
</li>
<li>
<p><code>history.forward()</code>
等价于：history.go(1)</p>
</li>
</ol>
<h1 data-id="heading-3">二、安装与使用vue-router</h1>
<h3 data-id="heading-4">1. 安装</h3>
<p>在使用脚手架创建项目的时候直接添加 <code>Router</code>，也可以使用命令在项目中添加：</p>
<pre><code class="hljs language-bash copyable" lang="bash">npm install vue-router --save
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-5">2. vue-router 使用步骤：</h3>
<p>大体步骤：</p>
<ol>
<li>导入路由对象，并且调用 Vue.use(VueRouter)</li>
<li>创建路由实例，并且传入路由映射配置</li>
<li>在Vue实例中挂载创建的路由实例</li>
</ol>
<p>例子：</p>
<ul>
<li>
<p><code>src/router/index.js</code>：一般的，router 相关的配置信息，都放在 <code>src/router/index.js</code> 中</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">import</span> Vue <span class="hljs-keyword">from</span> <span class="hljs-string">"vue"</span>
<span class="hljs-comment">// 1. 导入 VueRouter 插件</span>
<span class="hljs-keyword">import</span> VueRouter <span class="hljs-keyword">from</span> <span class="hljs-string">"vue-router"</span>;

<span class="hljs-comment">// 2.通过 Vue.use(VueRouter)，安装插件</span>
Vue.use(VueRouter);

<span class="hljs-comment">// 3. 创建 VueRouter 对象并配置映射关系</span>
<span class="hljs-keyword">const</span> router = <span class="hljs-keyword">new</span> VueRouter(&#123;
  <span class="hljs-comment">// 配置路由和组件之间的应用关系</span>
  <span class="hljs-attr">routes</span>: [

  ]
&#125;)

<span class="hljs-comment">// 4. 将 router 对象传入到 Vue 实例中</span>
<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> router;
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
<li>
<p><code>main.js</code> 中</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">import</span> Vue <span class="hljs-keyword">from</span> <span class="hljs-string">'vue'</span>
<span class="hljs-keyword">import</span> App <span class="hljs-keyword">from</span> <span class="hljs-string">'./App.vue'</span>
<span class="hljs-comment">// 5. 导入，如果导入的是一个文件夹，会自动找到文件夹中 index.js 文件</span>
<span class="hljs-keyword">import</span> router <span class="hljs-keyword">from</span> <span class="hljs-string">"./router"</span>;

Vue.config.productionTip = <span class="hljs-literal">false</span>

<span class="hljs-keyword">new</span> Vue(&#123;
  <span class="hljs-comment">// 6. 挂载创建的路由实例</span>
  router,
  <span class="hljs-attr">render</span>: <span class="hljs-function"><span class="hljs-params">h</span> =></span> h(App),
&#125;).$mount(<span class="hljs-string">'#app'</span>)
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
</ul>
<h3 data-id="heading-6">3. 路由与组件映射</h3>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">const</span> router = <span class="hljs-keyword">new</span> VueRouter(&#123;
  <span class="hljs-comment">// 配置路由和组件之间的应用关系</span>
  <span class="hljs-attr">routes</span>: [
    &#123;
      <span class="hljs-comment">// 路由的默认路径（指定刚进入页面时，选择哪个路由）</span>
      <span class="hljs-attr">path</span>: <span class="hljs-string">'/'</span>,
      <span class="hljs-attr">redirect</span>: <span class="hljs-string">'/home'</span>
    &#125;,
    &#123;
      <span class="hljs-attr">path</span>: <span class="hljs-string">'/home'</span>,
      <span class="hljs-attr">component</span>: <span class="hljs-function">() =></span> <span class="hljs-keyword">import</span>(<span class="hljs-string">"../components/Home"</span>)
    &#125;,
    &#123;
      <span class="hljs-attr">path</span>: <span class="hljs-string">'/about'</span>,
      <span class="hljs-attr">component</span>: <span class="hljs-function">() =></span> <span class="hljs-keyword">import</span>(<span class="hljs-string">"../components/About"</span>)
    &#125;
  ]
&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-7">4. 使用路由（ router-link 和 router-view 标签）</h3>
<p><code><router-link></code> 与 <code><router-view></code> 标签都是 <code>vue-router</code> 中已经内置的组件。</p>
<ul>
<li>
<p><code><router-link></code>：用来改变地址栏中的地址</p>
<ul>
<li>
<p><code>to</code>：用来指定路径，默认使用的是锚点。</p>
</li>
<li>
<p><code>tag</code>：tag可以指定 <code><router-link></code> 之后渲染成什么组件，默认会被渲染成一个 <code><a></code> 标签</p>
</li>
<li>
<p><code>replace</code>：使用该参数后不会留下 history 记录，所以指定 replace 的情况下，后退键返回不能返回到上一个页面中</p>
<blockquote>
<p>（可想而知，默认底层使用 history.pushState() 改变 url，加上 replace 后，就使用的是 history.replaceState() 来改变url ）</p>
</blockquote>
</li>
<li>
<p>active-class：当 <code><router-link></code> 对应的路由匹配成功时, 会自动给当前元素设置一个 <code>router-link-active</code> 的 class，可以通过设置 <code>active-class</code> 来修改这个默认的 class 名称。（全部修改请查看第三章第2节）</p>
</li>
</ul>
</li>
<li>
<p><code><router-view></code>：该标签会根据当前的路径，动态渲染出不同的组件.</p>
<p>网页的其他内容，比如顶部的标题/导航，或者底部的一些版权信息等会和<code><router-view></code>处于同一个等级。在路由切换时，切换的是 <code><router-view></code> 挂载的组件，其他内容不会发生改变.</p>
<ul>
<li><code>key</code>：标识当前组件，默认使用的是==路由==，当路由中存在参数时，可以使用全路径。（详见 八-1）</li>
</ul>
</li>
</ul>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">template</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">id</span>=<span class="hljs-string">"app"</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">router-link</span> <span class="hljs-attr">to</span>=<span class="hljs-string">"/home"</span>></span>首页<span class="hljs-tag"></<span class="hljs-name">router-link</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">router-link</span> <span class="hljs-attr">to</span>=<span class="hljs-string">"/about"</span> <span class="hljs-attr">tag</span>=<span class="hljs-string">"li"</span> <span class="hljs-attr">replace</span>></span>关于<span class="hljs-tag"></<span class="hljs-name">router-link</span>></span>

    <span class="hljs-tag"><<span class="hljs-name">router-view</span>></span><span class="hljs-tag"></<span class="hljs-name">router-view</span>></span>
<span class="hljs-comment"><!-- 使用全路径作为标识 --></span>
<span class="hljs-tag"><<span class="hljs-name">router-view</span> <span class="hljs-attr">:key</span>=<span class="hljs-string">"$route.fullPath"</span>></span><span class="hljs-tag"></<span class="hljs-name">router-view</span>></span>
  <span class="hljs-tag"></<span class="hljs-name">div</span>></span>
<span class="hljs-tag"></<span class="hljs-name">template</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-8">5. 事件中使用路由（$router）</h3>
<p>可以不使用 <code><router-link></code> 而是直接使用按钮等其它标签，然后绑定事件，通过事件来改变 url：</p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-comment"><!-- push 与 replace 的区别就是会不会留下 history 记录 --></span>
<span class="hljs-tag"><<span class="hljs-name">button</span> @<span class="hljs-attr">click</span>=<span class="hljs-string">"$router.push('/home')"</span>></span>Home<span class="hljs-tag"></<span class="hljs-name">button</span>></span>
<span class="hljs-tag"><<span class="hljs-name">button</span> @<span class="hljs-attr">click</span>=<span class="hljs-string">"$router.replace('/about')"</span>></span>About<span class="hljs-tag"></<span class="hljs-name">button</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>vue 中通过 this 来访问 <code>$router</code> 属性</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> &#123;
  <span class="hljs-attr">name</span>: <span class="hljs-string">'App'</span>,
  <span class="hljs-attr">method</span>:&#123;
    <span class="hljs-function"><span class="hljs-title">clickFunc</span>(<span class="hljs-params"></span>)</span> &#123;
      <span class="hljs-built_in">this</span>.$router.replace(<span class="hljs-string">"/home"</span>);
    &#125;
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>==注意==：不要使用 <code>history.pushState()</code> 、<code>history.replaceState()</code> 等方法来直接修改 url，这样会绕过 <code>vue-router</code>。</li>
</ul>
<h1 data-id="heading-9">三、创建 VueRouter 对象时的其它配置</h1>
<h2 data-id="heading-10">1. mode（指定路由模式）</h2>
<p>默认情况下，路径的改变使用的 URL 的 hash。使用如下方式，在创建 VueRouter 对象时，更改 mode 属性，设置路由模式为 HTML5 的 History 模式</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">const</span> router = <span class="hljs-keyword">new</span> VueRouter(&#123;
  <span class="hljs-comment">// 配置路由和组件之间的应用关系</span>
  <span class="hljs-attr">routes</span>: [
  ],
  <span class="hljs-comment">// 指定路由模式</span>
  <span class="hljs-attr">mode</span>: <span class="hljs-string">'history'</span>
&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-11">2. linkActiveClass（路由匹配成功时添加 class）</h2>
<p>当 <code><router-link></code> 对应的路由匹配成功时, 会自动给当前元素设置一个 <code>router-link-active</code> 的 class。</p>
<p>一般在进行高亮显示的导航菜单或者底部 tabbar 时, 会使用到该类。但是通常不会修改类的属性, 会直接使用默认的 <code>router-link-active</code> 即可</p>
<p>也可以使用 linkActiveClass 来修改这个默认的 class。</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">const</span> router = <span class="hljs-keyword">new</span> VueRouter(&#123;
  <span class="hljs-comment">// 配置路由和组件之间的应用关系</span>
  <span class="hljs-attr">routes</span>: [
  ],
  <span class="hljs-comment">// 指定路由模式</span>
  <span class="hljs-attr">linkActiveClass</span>: <span class="hljs-string">"active"</span>
&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<h1 data-id="heading-12">四、传递参数（$route）</h1>
<h2 data-id="heading-13">1. 动态路由（params的类型）</h2>
<p>要给 User 组件传入一个 ID，那么，我们可以在 vue-router 的路由路径中使用“<strong>动态路径参数</strong>”(dynamic segment) 来达到这个效果
一个“<strong>路径参数</strong>”使用冒号 <code>:</code> 标记。当匹配到一个路由时，参数值会被设置到 <code>this.$route.params $route</code></p>
<ul>
<li>
<p><code>$route</code>：当前哪个路由处于活跃状态，拿到的就是哪个路由。即 <code>routes</code> 数组中对应的路由对象</p>
<blockquote>
<p>注意与 <code>$router</code> 的区别，<code>$router</code> 是指 new 出来的 VueRouter 对象，也就是下面的的常量 <code>router</code>，而 <code>$route</code> 是 <code>VueRouter</code> 对象中的 <code>routers</code> 数组中的一个对象，即 <code>$router.routes[0]</code> 的路由是处于活跃状态时就是 <code>$route</code></p>
</blockquote>
</li>
</ul>
<ol>
<li>在 vue-router 映射关系的 path 中，增加一个 idProp 参数，来接收上面传入的 id，这个参数传递进来后会保存在 <code>$route.idProp</code> 中</li>
</ol>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">const</span> router = <span class="hljs-keyword">new</span> VueRouter(&#123;
  <span class="hljs-comment">// 配置路由和组件之间的应用关系</span>
  <span class="hljs-attr">routes</span>: [
    &#123;
      <span class="hljs-attr">path</span>: <span class="hljs-string">'/user/:idProp'</span>,
      <span class="hljs-attr">component</span>: <span class="hljs-function">() =></span> <span class="hljs-keyword">import</span>(<span class="hljs-string">"../components/User"</span>)
    &#125;
  ],
  <span class="hljs-attr">mode</span>: <span class="hljs-string">'history'</span>
&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<ol start="2">
<li>url 中加入的用户的 id 参数：</li>
</ol>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-comment"><!-- 使用 router-link 的方式 --></span>
<span class="hljs-tag"><<span class="hljs-name">router-link</span> <span class="hljs-attr">:to</span>=<span class="hljs-string">"'/user/' + id"</span> <span class="hljs-attr">tag</span>=<span class="hljs-string">"button"</span>></span>用户<span class="hljs-tag"></<span class="hljs-name">router-link</span>></span>

<span class="hljs-comment"><!-- 使用 JavsScript 的方式 --></span>
<span class="hljs-tag"><<span class="hljs-name">button</span> @<span class="hljs-attr">click</span>=<span class="hljs-string">"$router.push('/user/' + id)"</span>></span>用户<span class="hljs-tag"></<span class="hljs-name">button</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<ol start="3">
<li>使用 <code>$route.params</code> 获取到传入的 idProp 参数</li>
</ol>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">template</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">div</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">h3</span>></span>这是直接获取的用户id：&#123;&#123;$route.params.idProp&#125;&#125;<span class="hljs-tag"></<span class="hljs-name">h3</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">li</span>></span>这是从方法中获取的id：&#123;&#123;id2&#125;&#125;<span class="hljs-tag"></<span class="hljs-name">li</span>></span>
  <span class="hljs-tag"></<span class="hljs-name">div</span>></span>
<span class="hljs-tag"></<span class="hljs-name">template</span>></span>

<span class="hljs-tag"><<span class="hljs-name">script</span>></span><span class="javascript">
  <span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> &#123;
    <span class="hljs-attr">name</span>: <span class="hljs-string">"User"</span>,
    <span class="hljs-attr">computed</span>: &#123;
      <span class="hljs-function"><span class="hljs-title">id2</span>(<span class="hljs-params"></span>)</span> &#123;
        <span class="hljs-keyword">return</span> <span class="hljs-built_in">this</span>.$route.params.idProp;
      &#125;
    &#125;
  &#125;
</span><span class="hljs-tag"></<span class="hljs-name">script</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-14">2. query的类型</h2>
<p>配置路由格式：<code>/router</code>，也就是普通配置
传递的方式：直接传递对象，对象中用 <code>path</code> 来指定路由，用 <code>query</code> 对象来传递参数
传递后形成的路径：<code>/router?id=123</code>、<code>/router?id=abc</code></p>
<ol>
<li>
<p>==传递参数==：直接传递一个对象，对象的 path 用来指定路由，query 用来指定参数</p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-comment"><!-- 使用 router-link 的方式 --></span>
<span class="hljs-comment"><!-- 请求地址：http://localhost:8080/profile?name=%E6%9D%8E%E5%9B%9B&age=24&heigth=1.88 --></span>
<span class="hljs-tag"><<span class="hljs-name">router-link</span> <span class="hljs-attr">:to</span>=<span class="hljs-string">"&#123;path: '/profile', query: &#123;name: '张三', age: 34&#125;&#125;"</span>></span>张三档案<span class="hljs-tag"></<span class="hljs-name">router-link</span>></span>

<span class="hljs-comment"><!-- 使用 JavsScript 的方式 --></span>
<span class="hljs-tag"><<span class="hljs-name">button</span> @<span class="hljs-attr">click</span>=<span class="hljs-string">"$router.push(&#123;path: '/profile', query: &#123;name: '李四', age : 24, heigth: 1.88&#125;&#125;)"</span>></span>李四档案<span class="hljs-tag"></<span class="hljs-name">button</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
<li>
<p>==接收参数==：Profile.vue 中使用 <code>$route.query</code> 来获取传入的 <code>query</code> 对象</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><template>
  <span class="xml"><span class="hljs-tag"><<span class="hljs-name">div</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">li</span> <span class="hljs-attr">v-for</span>=<span class="hljs-string">"(val, key) in $route.query"</span>></span>&#123;&#123;key&#125;&#125;: &#123;&#123;val&#125;&#125;<span class="hljs-tag"></<span class="hljs-name">li</span>></span>
  <span class="hljs-tag"></<span class="hljs-name">div</span>></span></span>
</template>
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
</ol>
<blockquote>
<p><strong>扩展</strong>：</p>
<ul>
<li>URL的完整路径各个部分的叫法，这也解释了上面为什么使用 query 来字义参数：</li>
</ul>
<pre><code class="hljs language-html copyable" lang="html">scheme:[//[user:password@]host[:port]][/]path[?query][#fragment] 
<span class="copy-code-btn">复制代码</span></code></pre>
</blockquote>
<h1 data-id="heading-15">五、嵌套路由</h1>
<p>嵌套路由是一个很常见的功能，比如在 home 页面中，我们希望通过 <code>/home/news</code> 或者 <code>/home/message</code> 访问一些内容。一个路径映射一个组件，访问这两个路径也会分别渲染两个组件。比如说，当访问 <code>/home/news</code> 时，先渲染 <code>Home</code> 组件，再在 Home 组件中渲染 News 组件。</p>
<p>路径和组件的关系如下:</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/65197b100b464336bb1fcd6ebf5c46c3~tplv-k3u1fbpfcp-watermark.image" alt="在这里插入图片描述" loading="lazy" referrerpolicy="no-referrer"></p>
<p>实现嵌套路由主要是两个步骤：</p>
<ol>
<li>创建对应的子组件，并且在路由映射的 <code>children</code> 中配置对应的子路由.</li>
</ol>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> <span class="hljs-keyword">new</span> VueRouter(&#123;
  <span class="hljs-comment">// 配置路由和组件之间的应用关系</span>
  <span class="hljs-attr">routes</span>: [
    &#123;
      <span class="hljs-attr">path</span>: <span class="hljs-string">'/home'</span>,
      <span class="hljs-attr">component</span>: <span class="hljs-function">() =></span> <span class="hljs-keyword">import</span>(<span class="hljs-string">"../components/Home"</span>),
      <span class="hljs-attr">children</span>:[
        &#123;
          <span class="hljs-attr">path</span>: <span class="hljs-string">''</span>,
          <span class="hljs-attr">redirect</span>: <span class="hljs-string">'news'</span>
        &#125;,
        &#123;
          <span class="hljs-comment">// 注意路径前的 /，加上表示绝对路径，不加表示相对路径</span>
          <span class="hljs-comment">// 下面的配置匹配的路径为：/home/news</span>
          <span class="hljs-attr">path</span>: <span class="hljs-string">'news'</span>,
          <span class="hljs-attr">component</span>: <span class="hljs-function">() =></span> <span class="hljs-keyword">import</span>(<span class="hljs-string">"../components/HomeNews"</span>)
        &#125;,
        &#123;
          <span class="hljs-attr">path</span>: <span class="hljs-string">'messages'</span>,
          <span class="hljs-attr">component</span>: <span class="hljs-function">() =></span> <span class="hljs-keyword">import</span>(<span class="hljs-string">"../components/HomeMessages"</span>)
        &#125;
      ]
    &#125;
  ]
&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<ol start="2">
<li>在组件内部使用 <code><router-view></code> 标签.</li>
</ol>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">template</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">div</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">h2</span>></span>我是Home<span class="hljs-tag"></<span class="hljs-name">h2</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">p</span>></span>我是Home的内容<span class="hljs-tag"></<span class="hljs-name">p</span>></span>

    <span class="hljs-tag"><<span class="hljs-name">button</span> @<span class="hljs-attr">click</span>=<span class="hljs-string">"$router.replace('/home/news')"</span>></span>首页新闻<span class="hljs-tag"></<span class="hljs-name">button</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">button</span> @<span class="hljs-attr">click</span>=<span class="hljs-string">"$router.replace('/home/messages')"</span>></span>首页消息<span class="hljs-tag"></<span class="hljs-name">button</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">router-view</span>></span><span class="hljs-tag"></<span class="hljs-name">router-view</span>></span>
  <span class="hljs-tag"></<span class="hljs-name">div</span>></span>
<span class="hljs-tag"></<span class="hljs-name">template</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h1 data-id="heading-16">六、导航守卫</h1>
<p>vue-router 提供的导航守卫主要用来<strong>监听路由的进入和离开</strong>的。导航守卫这块官网也说的比较清楚了，这块直接看官网就好（官方网址：<a href="https://link.juejin.cn/?target=https%3A%2F%2Frouter.vuejs.org%2Fzh%2Fguide%2Fadvanced%2Fnavigation-guards.html%23%25E7%25BB%2584%25E4%25BB%25B6%25E5%2586%2585%25E7%259A%2584%25E5%25AE%2588%25E5%258D%25AB" target="_blank" rel="nofollow noopener noreferrer" title="https://router.vuejs.org/zh/guide/advanced/navigation-guards.html#%E7%BB%84%E4%BB%B6%E5%86%85%E7%9A%84%E5%AE%88%E5%8D%AB" ref="nofollow noopener noreferrer">戳这里</a>）</p>
<p>这里就给全局守卫举个例子，其它的用法也基本相同。</p>
<h2 data-id="heading-17">全局前置守卫</h2>
<p>vue-router 提供了 <code>beforeEach</code> 和 <code>afterEach</code> 的全局钩子函数，它们会在路由即将改变前和改变后触发。</p>
<p>使用 <code>router.beforeEach</code> 注册一个全局前置守卫：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">const</span> router = <span class="hljs-keyword">new</span> VueRouter(&#123; ... &#125;)

router.beforeEach(<span class="hljs-function">(<span class="hljs-params">to, <span class="hljs-keyword">from</span>, next</span>) =></span> &#123;
  <span class="hljs-comment">// ...</span>
  next();
&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>当一个导航触发时，全局前置守卫按照创建顺序调用。守卫是异步解析执行，此时导航在所有守卫 resolve 完之前一直处于 等待中。</p>
<p>每个守卫方法接收三个参数：</p>
<ul>
<li>
<p><code>to: Route</code>: 即将要进入的目标 路由对象</p>
</li>
<li>
<p><code>from: Route</code>: 当前导航正要离开的路由</p>
</li>
<li>
<p><code>next: Function</code>: ==一定要调用该方法来 resolve 这个钩子==。执行效果依赖 next 方法的调用参数。</p>
<ul>
<li>
<p><code>next()</code>: 进行管道中的下一个钩子。如果全部钩子执行完了，则导航的状态就是 confirmed (确认的)。</p>
</li>
<li>
<p><code>next(false)</code>: 中断当前的导航。如果浏览器的 URL 改变了 (可能是用户手动或者浏览器后退按钮)，那么 URL 地址会重置到 from 路由对应的地址。</p>
</li>
<li>
<p><code>next('/')</code> 或者 <code>next(&#123; path: '/' &#125;)</code>: 跳转到一个不同的地址。当前的导航被中断，然后进行一个新的导航。你可以向 next 传递任意位置对象，且允许设置诸如 replace: true、name: 'home' 之类的选项以及任何用在 router-link 的 to prop 或 router.push 中的选项。</p>
</li>
<li>
<p><code>next(error)</code>: (2.4.0+) 如果传入 next 的参数是一个 Error 实例，则导航会被终止且该错误会被传递给 router.onError() 注册过的回调。</p>
</li>
</ul>
</li>
<li>
<p>举个小例子：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">const</span> router = <span class="hljs-keyword">new</span> VueRouter(&#123;
  <span class="hljs-attr">routes</span>: [
    &#123;
      <span class="hljs-attr">path</span>: <span class="hljs-string">'/home'</span>,
      <span class="hljs-attr">component</span>: <span class="hljs-function">() =></span> <span class="hljs-keyword">import</span>(<span class="hljs-string">"../components/Home"</span>),
      <span class="hljs-comment">// 使用 meta 属性来添加数据</span>
      <span class="hljs-attr">meta</span>: &#123;
        <span class="hljs-attr">title</span>: <span class="hljs-string">'首页'</span>
      &#125;
    &#125;,
    &#123;
      <span class="hljs-attr">path</span>: <span class="hljs-string">'/about'</span>,
      <span class="hljs-attr">component</span>: <span class="hljs-function">() =></span> <span class="hljs-keyword">import</span>(<span class="hljs-string">"../components/About"</span>),
      <span class="hljs-attr">meta</span>: &#123;
        <span class="hljs-attr">title</span>: <span class="hljs-string">'关于'</span>
      &#125;,
    &#125;
  ],
  <span class="hljs-attr">mode</span>: <span class="hljs-string">'history'</span>
&#125;)

router.beforeEach(<span class="hljs-function">(<span class="hljs-params">to, <span class="hljs-keyword">from</span>, next</span>) =></span> &#123;
  <span class="hljs-comment">// 路由改变时，修改标题</span>
  <span class="hljs-built_in">document</span>.title = to.meta.title;

  <span class="hljs-comment">// 如果是子组件的话，要这么取 meta 中的值：(to.matched是个数组，包含所有子组件)</span>
  <span class="hljs-built_in">document</span>.title = to.matched[<span class="hljs-number">0</span>].meta.title;
  next();
&#125;);
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
</ul>
<h1 data-id="heading-18">七、路由懒加载</h1>
<p>当打包构建应用时，JavaScript 包会变得非常大，影响页面加载。</p>
<p>路由懒加载的主要作用就是将路由对应的组件打包成一个个的 <code>js</code> 代码块。只有在这个路由被访问到的时候，才加载对应的组件。</p>
<p>结合 Vue 的异步组件和 Webpack 的代码分割功能，轻松实现路由组件的懒加载（之前的案例都是这种写法，这里就是再说明一下）：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">const</span> router = <span class="hljs-keyword">new</span> VueRouter(&#123;
  <span class="hljs-comment">// 配置路由和组件之间的应用关系</span>
  <span class="hljs-attr">routes</span>: [
    &#123;
      <span class="hljs-attr">path</span>: <span class="hljs-string">'/home'</span>,
      <span class="hljs-comment">// 下面的写法就是路由懒加载写法</span>
      <span class="hljs-attr">component</span>: <span class="hljs-function">() =></span> <span class="hljs-keyword">import</span>(<span class="hljs-string">"../components/Home"</span>)
    &#125;,
    &#123;
      <span class="hljs-attr">path</span>: <span class="hljs-string">'/about'</span>,
      <span class="hljs-attr">component</span>: <span class="hljs-function">() =></span> <span class="hljs-keyword">import</span>(<span class="hljs-string">"../components/About"</span>)
    &#125;
  ]
&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<h1 data-id="heading-19">八、遇到的问题</h1>
<h2 data-id="heading-20">1. 多路由共用同一组件，相互干扰问题</h2>
<ul>
<li>
<p>问题描述：一个组件，要根据传入的参数不同，显示不同的数据，同时这个组件的状态还要保留（<code><keep-alive></code>）。这个时候就出现了一个问题，当一个组件的数据改变时，其它组件的数据也会跟着改。</p>
</li>
<li>
<p>解决办法：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><router-view :key=<span class="hljs-string">"$route.fullPath"</span>/>
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
</ul></div>  
</div>
            