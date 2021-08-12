
---
title: 'Vue Router Next'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/a23e006b731c41d38585cabede928fc1~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Thu, 12 Aug 2021 01:52:20 GMT
thumbnail: 'https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/a23e006b731c41d38585cabede928fc1~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>这是我参与8月更文挑战的第5天，活动详情查看：<a href="https://juejin.cn/post/6987962113788493831" target="_blank" title="https://juejin.cn/post/6987962113788493831">8月更文挑战</a></p>
<hr>
<h2 data-id="heading-0">系列文章</h2>
<ul>
<li><a href="https://juejin.cn/post/6992194951492665374" target="_blank" title="https://juejin.cn/post/6992194951492665374">Vue 3 基础</a></li>
<li><a href="https://juejin.cn/post/6992476452721524750" target="_blank" title="https://juejin.cn/post/6992476452721524750">Vue 3 动效</a></li>
<li><a href="https://juejin.cn/post/6992765608240644109" target="_blank" title="https://juejin.cn/post/6992765608240644109">Vue 3 组件</a></li>
<li><a href="https://juejin.cn/post/6993197085474422797" target="_blank" title="https://juejin.cn/post/6993197085474422797">组合式 API</a></li>
<li><a href="https://juejin.cn/post/6995478754571059237" target="_blank" title="https://juejin.cn/post/6995478754571059237">Vue Router Next</a></li>
</ul>
<hr>
<p>通过 Vue.js 已经用组件组成了我们的应用，当加入 Vue Router 时，我们需要做的就是<strong>将（视图）组件映射到路由（URL）上</strong>，让 Vue Router 知道在哪里渲染它们，在单页面应用实现类似多页面切换的效果。</p>
<p>💡 Vue Router Next 是 Vue Router v4.x 版本，适配了 Vue 3，大部分 API 都得以保留，但仍有部分一些不可兼容的改变，从 Vue Router v3 <a href="https://link.juejin.cn/?target=https%3A%2F%2Fnext.router.vuejs.org%2Fzh%2Fguide%2Fmigration%2Findex.html" target="_blank" rel="nofollow noopener noreferrer" title="https://next.router.vuejs.org/zh/guide/migration/index.html" ref="nofollow noopener noreferrer">迁移指南</a>可以参考官方文档。本文介绍 Vue Router Next 的基础使用方法，主要针对 🎉 <em>与 Vue Router v3 的不同点</em>。</p>
<h2 data-id="heading-1">安装引入</h2>
<p>可以通过 CDN 引入最新版本的 Vue Router，该模块暴露 <code>VueRouter</code> 对象，通过 🎉 <em>调用其方法 <code>createRouter</code> 创建路由实例</em></p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">script</span> <span class="hljs-attr">src</span>=<span class="hljs-string">"https://unpkg.com/vue-router@4"</span>></span><span class="hljs-tag"></<span class="hljs-name">script</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>💡 也可以指定版本</p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">script</span> <span class="hljs-attr">src</span>=<span class="hljs-string">"https://unpkg.com/vue-router@4.0.11/dist/vue-router.global.js"</span>></span><span class="hljs-tag"></<span class="hljs-name">script</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>也可以通过 npm 安装，使用方法 <code>createRouter</code> 创建路由后，通过 <code>app.use(router)</code> 的方式安装插件（其中 <code>app</code> 是 Vue 应用实例，<code>router</code> 是路由实例），这样整个应用都支持路由（在其他子组件不需要再导入）</p>
<pre><code class="hljs language-bash copyable" lang="bash">npm install vue-router@4
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">import</span> &#123; createApp &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'vue'</span>;
<span class="hljs-keyword">import</span> &#123; createRouter &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'vue-router'</span>;

<span class="hljs-keyword">const</span> app = Vue.createApp(&#123;&#125;)
<span class="hljs-comment">// 路由配置</span>
<span class="hljs-keyword">const</span> routes = [...]
<span class="hljs-keyword">const</span> router = VueRouter.createRouter(&#123;
  <span class="hljs-comment">// 使用 hash 模式</span>
  <span class="hljs-attr">history</span>: VueRouter.createWebHashHistory(),
  routes, <span class="hljs-comment">// 路由配置</span>
&#125;)
<span class="hljs-comment">// 整个应用支持路由</span>
app.use(router)
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-2">初始化</h2>
<p>🎉 <em>通过方法 <code>createRouter()</code> 创建路由实例</em>，并配置组件和路由的映射关系</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">import</span> &#123; createApp &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'vue'</span>;
<span class="hljs-keyword">import</span> VueRouter <span class="hljs-keyword">from</span> <span class="hljs-string">'vue-router'</span>;

<span class="hljs-comment">// 路由配置</span>
<span class="hljs-comment">// 路由和组件的映射规则，一般每个路由 path 对应一个组件 component</span>
<span class="hljs-keyword">const</span> routes = [
  &#123; 
    <span class="hljs-comment">// 路由网址（url）</span>
    <span class="hljs-attr">path</span>: <span class="hljs-string">'/'</span>,
    <span class="hljs-comment">// 对应的组件（视图）</span>
    <span class="hljs-attr">component</span>: Home
  &#125;,
  &#123; <span class="hljs-attr">path</span>: <span class="hljs-string">'/about'</span>, <span class="hljs-attr">component</span>: About &#125;,
]

<span class="hljs-comment">// 创建 router 实例，</span>
<span class="hljs-keyword">const</span> router = VueRouter.createRouter(&#123;
  <span class="hljs-comment">// 使用 hash 模式</span>
  <span class="hljs-attr">history</span>: VueRouter.createWebHashHistory(),
  <span class="hljs-comment">// 传入路由配置</span>
  routes,
&#125;)

<span class="hljs-comment">// 创建和挂载根实例</span>
<span class="hljs-comment">// 通过选项 router 注入路由，让整个应用都可以使用路由功能</span>
createApp(&#123;&#125;).use(router).mount(<span class="hljs-string">'#app'</span>);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>通过调用 <code>app.use(router)</code> 注入路由后，在应用中常用到两个概念（其中 <code>this</code> 表示组件实例）：</p>
<ul>
<li><code>router</code> 是指路由器，它由 Vue Router 插件提供的多种控制路由的方法，在任何组件内都可以通过 <code>this.$router</code> 访问路由器</li>
<li><code>route</code> 是指一个包含当前路由信息的对象，可以通过 <code>this.$route</code> 访问当前路由</li>
</ul>
<p>💡 如果 🎉 <em>在选项 <code>setup</code> 函数则分别通过函数 <code>useRouter()</code> 访问路由实例，通过函数 <code>useRoute()</code> 访问当前路由</em></p>
<p>最后别忘了在 Vue 实例（组件）的模板中使用 Vue Router 的<strong>内置组件 <code><router-view></code></strong> ，这样才可以将当前路由匹配的组件渲染在到页面上。</p>
<p>可以使用 Vue Router 的<strong>内置组件 <code><router-link></code></strong> 为在页面中添加一个导航的 UI 组件，它默认渲染为一个 <code><a></code> 标签</p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">id</span>=<span class="hljs-string">"app"</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">div</span>></span>
    <span class="hljs-comment"><!--使用 router-link 组件进行导航 --></span>
    <span class="hljs-comment"><!--通过传递 `to` 来指定链接 --></span>
    <span class="hljs-comment"><!--`<router-link>` 将呈现一个带有正确 `href` 属性的 `<a>` 标签--></span>
    <span class="hljs-tag"><<span class="hljs-name">router-link</span> <span class="hljs-attr">to</span>=<span class="hljs-string">"/"</span>></span>Go to Home<span class="hljs-tag"></<span class="hljs-name">router-link</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">router-link</span> <span class="hljs-attr">to</span>=<span class="hljs-string">"/about"</span>></span>Go to About<span class="hljs-tag"></<span class="hljs-name">router-link</span>></span>
  <span class="hljs-tag"></<span class="hljs-name">div</span>></span>

  <span class="hljs-comment"><!-- 路由匹配到的组件将渲染在这里 --></span>
  <span class="hljs-tag"><<span class="hljs-name">router-view</span>></span><span class="hljs-tag"></<span class="hljs-name">router-view</span>></span>
<span class="hljs-tag"></<span class="hljs-name">div</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-3">历史模式</h2>
<p>传递给方法 <code>VueRouter.createRouter(&#123;&#125;)</code> 的参数是一个对象，在 Vue Route Next 中抛弃了属性 <code>mode</code> ，需要显式使用 🎉 <em>属性<code>history</code> 来设置项目使用何种历史模式</em></p>
<h3 data-id="heading-4">Hash 模式</h3>
<p>🎉 <em>通过 <code>createWebHashHistory()</code> 创建</em></p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">import</span> &#123; createRouter, createWebHashHistory &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'vue-router'</span>

<span class="hljs-keyword">const</span> router = createRouter(&#123;
  <span class="hljs-attr">history</span>: createWebHashHistory(),
  <span class="hljs-attr">routes</span>: [
    <span class="hljs-comment">//...</span>
  ],
&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>在该模式下项目内部<strong>传递的实际 URL 之前使用了一个哈希字符 <code>#</code></strong> ，由于这部分 URL 从未被发送到服务器，所以它不需要在服务器层面上进行任何特殊处理，不会引起页面重载。不过<strong>它在 SEO 中确实有不好的影响</strong>。</p>
<h3 data-id="heading-5">HTML5 模式</h3>
<p>🎉 <em>通过 <code>createWebHistory()</code> 创建</em>，需要<a href="https://link.juejin.cn/?target=https%3A%2F%2Fnext.router.vuejs.org%2Fguide%2Fessentials%2Fhistory-mode.html%23example-server-configurations" target="_blank" rel="nofollow noopener noreferrer" title="https://next.router.vuejs.org/guide/essentials/history-mode.html#example-server-configurations" ref="nofollow noopener noreferrer">后端服务器配合</a></p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">import</span> &#123; createRouter, createWebHistory &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'vue-router'</span>

<span class="hljs-keyword">const</span> router = createRouter(&#123;
  <span class="hljs-attr">history</span>: createWebHistory(),
  <span class="hljs-attr">routes</span>: [
    <span class="hljs-comment">//...</span>
  ],
&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>当使用这种历史模式时，URL 会看起来和「正常」的路径一样，不过需要同时在服务器上添加一个回退路由，让 URL 不匹配任何静态资源时，它也提供与你的应用程序中的 <code>index.html</code> 相同的页面。关于 Vue Router 采用 HTML5 模式时，服务器的配置示例可以参考<a href="https://link.juejin.cn/?target=https%3A%2F%2Fnext.router.vuejs.org%2Fguide%2Fessentials%2Fhistory-mode.html%23example-server-configurations" target="_blank" rel="nofollow noopener noreferrer" title="https://next.router.vuejs.org/guide/essentials/history-mode.html#example-server-configurations" ref="nofollow noopener noreferrer">官方文档</a>。</p>
<h2 data-id="heading-6">路由配置</h2>
<p>传递给方法 <code>VueRouter.createRouter(&#123;&#125;)</code> 的参数是一个对象，其中属性 <code>routes</code> 是一个数组，每一个元素表示一个路由，包含相应的配置信息</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> router = createRouter(&#123;
  <span class="hljs-attr">history</span>: createWebHistory(),
  <span class="hljs-attr">routes</span>: [
    &#123;
      <span class="hljs-attr">path</span>: <span class="hljs-string">'/user/:username'</span>,
      <span class="hljs-attr">component</span>: User
    &#125;
  ],
&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>最基本的一个路由是由路径 <code>path</code> 和相应的视图组件 <code>component</code> 构成</p>
<h3 data-id="heading-7">路由元信息</h3>
<p>在定义路由规则时，可以设置选项 <code>meta</code> 元信息，传递一个对象，以键值对的形式<strong>存储关于该路由的相关信息</strong>，相当于为路由增添一些除了路径以为的附加信息，这些额外的信息可以用在路由守卫上，例如在导航守卫中基于 <code>meta</code> 的信息判断访问的路径是否需要登录验证等。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// 路由配置</span>
<span class="hljs-keyword">const</span> routes = [
  &#123;
    <span class="hljs-attr">path</span>: <span class="hljs-string">'/posts'</span>,
    <span class="hljs-attr">component</span>: PostsLayout,
    <span class="hljs-attr">children</span>: [
      &#123;
        <span class="hljs-attr">path</span>: <span class="hljs-string">'new'</span>,
        <span class="hljs-attr">component</span>: PostsNew,
        <span class="hljs-comment">// 只有经过身份验证的用户才能创建帖子</span>
        <span class="hljs-attr">meta</span>: &#123; <span class="hljs-attr">requiresAuth</span>: <span class="hljs-literal">true</span> &#125;
      &#125;,
      &#123;
        <span class="hljs-attr">path</span>: <span class="hljs-string">':id'</span>,
        <span class="hljs-attr">component</span>: PostsDetail
        <span class="hljs-comment">// 任何人都可以阅读文章</span>
        <span class="hljs-attr">meta</span>: &#123; <span class="hljs-attr">requiresAuth</span>: <span class="hljs-literal">false</span> &#125;
      &#125;
    ]
  &#125;
]
<span class="copy-code-btn">复制代码</span></code></pre>
<p>对于以上示例，如果希望基于路由的 <code>meta</code> 信息判断是否需要进行授权验证，可以使用组件内守卫</p>
<p>💡 一个路由可以匹配到多个路由（所有匹配到的路由记录会暴露为 <code>$route.matched</code> 数组，一般需要通过遍历数组各元素，来检查特性的属性），Vue Router 为我们提供了一个 <strong><code>$route.meta</code> 对象</strong>，它是一个<strong>非递归合并所有 <code>meta</code> 字段的对象</strong>（从父字段到子字段），可以更方便地访问路由的元信息。</p>
<pre><code class="hljs language-js copyable" lang="js">router.beforeEach(<span class="hljs-function">(<span class="hljs-params">to, <span class="hljs-keyword">from</span></span>) =></span> &#123;
  <span class="hljs-comment">// 基于路由的 `meta` 信息，判断当前导航是否需要进行授权验证</span>
  <span class="hljs-comment">// 默认是需要通过遍历 to.matched 数组，检查每条路由记录中的 meta 对象</span>
  <span class="hljs-comment">// to.matched.some(record => record.meta.requiresAuth)</span>
  <span class="hljs-comment">// 现在可以直接通过所有元信息合并后得到的 to.meta 对象进行检查</span>
  <span class="hljs-keyword">if</span> (to.meta.requiresAuth && !auth.isLoggedIn()) &#123;
    <span class="hljs-comment">// 如果此路由需要授权，请检查是否已登录</span>
    <span class="hljs-comment">// 如果没有，则重定向到登录页面</span>
    <span class="hljs-keyword">return</span> &#123;
      <span class="hljs-attr">path</span>: <span class="hljs-string">'/login'</span>,
      <span class="hljs-comment">// 保存我们所在的位置，以便以后再来</span>
      <span class="hljs-attr">query</span>: &#123; <span class="hljs-attr">redirect</span>: to.fullPath &#125;,
    &#125;
  &#125;
&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>💡 如果使用 TypeScript 编写代码，可以通过<strong>扩展 <code>RouteMeta</code> 接口来输入 meta 字段</strong></p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// typings.d.ts or router.ts</span>
<span class="hljs-keyword">import</span> <span class="hljs-string">'vue-router'</span>

declare <span class="hljs-built_in">module</span> <span class="hljs-string">'vue-router'</span> &#123;
  interface RouteMeta &#123;
    <span class="hljs-comment">// 是可选的</span>
    isAdmin?: boolean
    <span class="hljs-comment">// 每个路由都必须声明</span>
    <span class="hljs-attr">requiresAuth</span>: boolean
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-8">页面滚动</h3>
<p>在创建路由实例时，可以通过<strong>选项 <code>scrollBehavior</code> 设置切换页面时如何滚动</strong>。</p>
<p>该选项是一个方法，前两个参数接收 <code>to</code> 和 <code>from</code> 路由对象，第三个参数 <code>savedPosition</code> 它是记录当前页面位置；返回一个 <a href="https://link.juejin.cn/?target=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FScrollToOptions" target="_blank" rel="nofollow noopener noreferrer" title="https://developer.mozilla.org/en-US/docs/Web/API/ScrollToOptions" ref="nofollow noopener noreferrer"><code>ScrollToOptions</code></a> 位置对象（告诉浏览器该如何滚动页面）或 <code>savedPosition</code>（告诉浏览器将页面滚动到之前的位置）</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> router = <span class="hljs-keyword">new</span> VueRouter(&#123;
  <span class="hljs-attr">routes</span>: [...],
  scrollBehavior (to, <span class="hljs-keyword">from</span>, savedPosition) &#123;
    <span class="hljs-keyword">if</span> (savedPosition) &#123;
      <span class="hljs-comment">// 如果通过上一页/下一页按钮进行导航</span>
      <span class="hljs-comment">// 则页面会通过 savedPosition 保留之前的位置</span>
      <span class="hljs-keyword">return</span> savedPosition
    &#125; <span class="hljs-keyword">else</span> &#123;
      <span class="hljs-comment">// 如果没有位置记录，默认就是滚动到页面顶部</span>
      <span class="hljs-keyword">return</span>&#123; <span class="hljs-attr">left</span>: <span class="hljs-number">0</span>, <span class="hljs-attr">top</span>: <span class="hljs-number">0</span> &#125;
    &#125;
  &#125;
&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>返回滚动位置的对象信息可以有多种格式：</p>
<ul>
<li>
<p>🎉 <em>滚动到指定的坐标轴 <code>return &#123; left: number, top: number &#125;</code></em>，一般对于所有路由导航，简单地让页面滚动到顶部 <code>return &#123; left: 0, top: 0 &#125;</code></p>
</li>
<li>
<p>🎉 <em>在返回对象中通过属性 <code>el</code> 指定一个元素（通过 CSS 选择器或直接传递一个 DOM）</em>，这样滚动的位移就是相对于该元素的</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> router = createRouter(&#123;
  <span class="hljs-function"><span class="hljs-title">scrollBehavior</span>(<span class="hljs-params">to, <span class="hljs-keyword">from</span>, savedPosition</span>)</span> &#123;
    <span class="hljs-comment">// 始终在元素 #main 上方滚动 10px</span>
    <span class="hljs-keyword">return</span> &#123;
      <span class="hljs-comment">// 通过 el 传递一个 CSS 选择器或一个 DOM 元素</span>
      <span class="hljs-attr">el</span>: <span class="hljs-string">'#main'</span>,
      <span class="hljs-comment">// 也可以这么写</span>
      <span class="hljs-comment">// el: document.getElementById('main'),</span>
      <span class="hljs-attr">top</span>: -<span class="hljs-number">10</span>,
    &#125;
  &#125;,
&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
<li>
<p>滚动到指定锚点</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> router = createRouter(&#123;
  <span class="hljs-function"><span class="hljs-title">scrollBehavior</span>(<span class="hljs-params">to, <span class="hljs-keyword">from</span>, savedPosition</span>)</span> &#123;
    <span class="hljs-keyword">if</span> (to.hash) &#123;
      <span class="hljs-keyword">return</span> &#123;
        <span class="hljs-attr">el</span>: to.hash,
      &#125;
    &#125;
  &#125;,
&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
<li>
<p>滚动到原来位置 <code>return savedPosition</code> 该值当且仅当通过浏览器的 <strong>前进/后退</strong> 按钮触发（popstate 导航）时才可用</p>
</li>
<li>
<p>返回一个 falsy 值或一个空对象，不发生滚动</p>
</li>
</ul>
<p>💡 还可以在返回的对象中添加 <code>behavior</code> 选项，并将值设置为 <code>smooth</code>，就可以启用原生的平滑滚动效果</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// ...</span>
scrollBehavior (to, <span class="hljs-keyword">from</span>, savedPosition) &#123;
  <span class="hljs-keyword">if</span> (to.hash) &#123;
    <span class="hljs-keyword">return</span> &#123;
      <span class="hljs-attr">el</span>: to.hash,
      <span class="hljs-attr">behavior</span>: <span class="hljs-string">'smooth'</span>,
    &#125;
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>💡 该方法支持返回一个 Promise，通过 <code>resolve</code> 一个对象来表示预期的位置，这样就可以在页面滚动之前稍作等待，实现<strong>异步滚动/延迟滚动</strong>。通过这个方法可以让滚动行为和页面过渡更好地配合，实现更优雅的动效。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> router = createRouter(&#123;
  scrollBehavior (to, <span class="hljs-keyword">from</span>, savedPosition) &#123;
    <span class="hljs-keyword">return</span> <span class="hljs-keyword">new</span> <span class="hljs-built_in">Promise</span>(<span class="hljs-function">(<span class="hljs-params">resolve, reject</span>) =></span> &#123;
      <span class="hljs-built_in">setTimeout</span>(<span class="hljs-function">() =></span> &#123;
        resolve(&#123; <span class="hljs-attr">left</span>: <span class="hljs-number">0</span>, <span class="hljs-attr">top</span>: <span class="hljs-number">0</span> &#125;)
      &#125;, <span class="hljs-number">500</span>) <span class="hljs-comment">// 延迟 500ms 后才进行页面滚动</span>
    &#125;)
  &#125;，
&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-9">命名路由</h3>
<p>可以在配置路由时，通过选项 <code>name</code> 给某个路由设置名称（名称需要唯一），这样在使用路径较长的路由进行导航时，可以通过该名称来指代该路由（如果是动态路由，还会配合路由参数使用）。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// 路由规则</span>
<span class="hljs-keyword">const</span> routes = [
  &#123;
    <span class="hljs-attr">path</span>: <span class="hljs-string">'/user/:username'</span>,
    <span class="hljs-attr">name</span>: <span class="hljs-string">'user'</span>
    <span class="hljs-attr">component</span>: User
  &#125;,
]
<span class="copy-code-btn">复制代码</span></code></pre>
<p>声明式导航，使用路由名称，并传递路由参数，由 Vue Router 拼接得到相应的 url</p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">router-link</span> <span class="hljs-attr">:to</span>=<span class="hljs-string">"&#123; name: 'user', params: &#123; username: 'ben' &#125;&#125;"</span>></span>
  User
<span class="hljs-tag"></<span class="hljs-name">router-link</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>编程式导航</p>
<pre><code class="hljs language-js copyable" lang="js">router.push(&#123; <span class="hljs-attr">name</span>: <span class="hljs-string">'user'</span>, <span class="hljs-attr">params</span>: &#123; <span class="hljs-attr">username</span>: <span class="hljs-string">'ben'</span> &#125; &#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>以上两个导航指向的路径都是 <code>/user/ben</code></p>
<h3 data-id="heading-10">别名</h3>
<p>可以在配置路由时，通过选项 <code>alias</code> 为路由设置<strong>别名</strong>，该功能可以让你自由地将同一个 <strong>UI 结构映射到任意的 URL</strong>，而不是受限于嵌套路由结构，例如实现类似短链接的功能方便用户访问。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// 路由配置</span>
<span class="hljs-keyword">const</span> routes = [
  &#123; 
    <span class="hljs-attr">path</span>: <span class="hljs-string">'/'</span>,
    <span class="hljs-attr">component</span>: Homepage,
    <span class="hljs-attr">alias</span>: <span class="hljs-string">'/home'</span>
  &#125;
]
<span class="copy-code-btn">复制代码</span></code></pre>
<p>💡 路由别名和路由重定向是不同的，虽然两者都可以实现将一个路径映射到另一个视图组件的效果，但是如果路径 <code>/a</code> 的路由别名是 <code>/b</code>，这意味着当用户访问 <code>/b</code> 时，<strong>URL 会保持为 <code>/b</code>，而不是跳转到 <code>/a</code></strong>，但是使用的路由匹配是 <code>/a</code> 路由的，就像用户访问 <code>/a</code> 一样。</p>
<p>该选项的值可以是一个数组，提供多个别名，即实现<strong>多个网址指向同一个页面</strong>。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> routes = [
  &#123;
    <span class="hljs-attr">path</span>: <span class="hljs-string">'/users/:id'</span>,
    <span class="hljs-attr">component</span>: UsersByIdLayout,
    <span class="hljs-attr">children</span>: [
      <span class="hljs-comment">// 为这 3 个 URL 呈现 UserDetails</span>
      <span class="hljs-comment">// - /users/24</span>
      <span class="hljs-comment">// - /users/24/profile</span>
      <span class="hljs-comment">// - /24</span>
      &#123; 
        <span class="hljs-attr">path</span>: <span class="hljs-string">'profile'</span>,
        <span class="hljs-attr">component</span>: UserDetails,
        <span class="hljs-attr">alias</span>: [<span class="hljs-string">'/:id'</span>, <span class="hljs-string">''</span>] &#125;,
    ],
  &#125;,
]
<span class="copy-code-btn">复制代码</span></code></pre>
<p>💡 如果原路径有参数，为了 SEO 规范，<strong>请在别名中耶包含相应的参数</strong></p>
<h3 data-id="heading-11">命名视图</h3>
<p>可以在页面模板中<strong>同时设置多个 <code><router-view></code></strong> （平行关系，而不是通过嵌套路由和嵌套的 <code><router-view></code> 的映射实现），不过得为每个视图设置名称 <code><router-view name="viewName></code>（没有设置名字则默认为 <code>default</code>），这样就可以<strong>在一个路由下「平行」渲染出多个组件</strong>。</p>
<p>这时应该在路由的配置中，相应地<strong>对于同一个路由要设置多个组件</strong>（如果组件数量少于平行的 <code><router-view></code> 数量，则相应的多余的视图组件将不会渲染），即选项 <code>components</code>（此时选项<strong>不</strong>是 <code>component</code>）变成一个对象，设置多个组件，每一个属性都是一个组件，键为视图 <code><router-view></code> 的的命名 <code>name</code>，值为组件名</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> router = createRouter(&#123;
  <span class="hljs-attr">history</span>: createWebHashHistory(),
  <span class="hljs-attr">routes</span>: [
    &#123;
      <span class="hljs-attr">path</span>: <span class="hljs-string">'/'</span>,
      <span class="hljs-comment">// 对应于多个组件</span>
      <span class="hljs-attr">components</span>: &#123;
        <span class="hljs-comment">// 默认 `<router-view>` 对应的组件</span>
        <span class="hljs-attr">default</span>: Home,
        <span class="hljs-comment">// 这时 ES6 对象属性的缩写，相当于 LeftSidebar: LeftSidebar</span>
        <span class="hljs-comment">// 属性名与 `<router-view>` 上的 `name` 属性匹配</span>
        LeftSidebar,
        RightSidebar,
      &#125;,
    &#125;,
  ],
&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">router-view</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"view left-sidebar"</span> <span class="hljs-attr">name</span>=<span class="hljs-string">"LeftSidebar"</span>></span><span class="hljs-tag"></<span class="hljs-name">router-view</span>></span>
<span class="hljs-tag"><<span class="hljs-name">router-view</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"view main-content"</span>></span><span class="hljs-tag"></<span class="hljs-name">router-view</span>></span>
<span class="hljs-tag"><<span class="hljs-name">router-view</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"view right-sidebar"</span> <span class="hljs-attr">name</span>=<span class="hljs-string">"RightSidebar"</span>></span><span class="hljs-tag"></<span class="hljs-name">router-view</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>💡 命名视图和嵌套路由都可以在一个页面设置多个视图 <code><router-view></code> 组件，但作用不同</p>
<ul>
<li>命名视图同一个页面设置多个 <code><router-view></code>，它们渲染出来的节点可以是「平行」关系，实现不同路由复用同一个布局模板</li>
<li>嵌套路由设置多个 <code><couter-view></code>，渲染出来的节点是父子嵌套关系，一般用于局部的布局更改</li>
</ul>
<p>💡 可以混用命名视图和嵌套视图，实现更复杂的布局</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/a23e006b731c41d38585cabede928fc1~tplv-k3u1fbpfcp-watermark.image" alt="命名视图 VS 嵌套视图" loading="lazy" referrerpolicy="no-referrer"></p>
<p>以上示例中父组件 <code>UserSettings</code> 中有一个常规组件 <code>Nav</code>，还有基于路由的三个嵌套组件<code>UserEmailsSubscriptions</code>、<code>UserProfile</code>、<code>UserProfilePreview</code>，其中组件 <code>UserProfile</code>、<code>UserProfilePreview</code> 是属于「平行」关系的。</p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-comment"><!-- UserSettings.vue --></span>
<span class="hljs-tag"><<span class="hljs-name">div</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">h1</span>></span>User Settings<span class="hljs-tag"></<span class="hljs-name">h1</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">NavBar</span> /></span>
  <span class="hljs-tag"><<span class="hljs-name">router-view</span> /></span>
  <span class="hljs-tag"><<span class="hljs-name">router-view</span> <span class="hljs-attr">name</span>=<span class="hljs-string">"helper"</span> /></span>
<span class="hljs-tag"></<span class="hljs-name">div</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// 相应的路由配置</span>
&#123;
  <span class="hljs-attr">path</span>: <span class="hljs-string">'/settings'</span>,
  <span class="hljs-attr">component</span>: UserSettings,
  <span class="hljs-comment">// 嵌套路由</span>
  <span class="hljs-attr">children</span>: [
    &#123;
      <span class="hljs-attr">path</span>: <span class="hljs-string">'emails'</span>,
      <span class="hljs-attr">component</span>: UserEmailsSubscriptions
    &#125;, 
    &#123;
      <span class="hljs-attr">path</span>: <span class="hljs-string">'profile'</span>,
      <span class="hljs-comment">// 命名视图</span>
      <span class="hljs-attr">components</span>: &#123;
        <span class="hljs-attr">default</span>: UserProfile,
        <span class="hljs-attr">helper</span>: UserProfilePreview
      &#125;
  &#125;]
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>💡 其实命名视图可以看作是更一般路由-组件映射规则，如果页面只需要一个 <code><router-view></code> 也可以在设置路由时使用 <code>components</code> 选项，只是里面只设置 <code>default: componentName</code> 一个组件。</p>
<h3 data-id="heading-12">重定向</h3>
<p>在路由的配置中通过选项 <code>redirect</code> 来实现重定向，实现用户访问 <code>/a</code> 路径时，导航转向路径 <code>/b</code> 的效果。</p>
<p>该选项的属性值可以是表示路径的字符串，或表示另一个路由的名称，或一个包含路由信息的对象，或一个方法（其返回值是前面三种表示路由的形式之一）</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// 路由配置</span>
<span class="hljs-keyword">const</span> routes = [
  &#123;
    <span class="hljs-attr">path</span>: <span class="hljs-string">'/home'</span>,
    <span class="hljs-attr">redirect</span>: <span class="hljs-string">'/'</span>
  &#125;,
  <span class="hljs-comment">// 重定向的目标也可以是一个命名的路由</span>
  &#123;
    <span class="hljs-attr">path</span>: <span class="hljs-string">'/home'</span>,
    <span class="hljs-attr">redirect</span>: &#123; <span class="hljs-attr">name</span>: <span class="hljs-string">'homepage'</span> &#125; 
  &#125;，
  &#123;
    <span class="hljs-comment">// 该动态路由可以实现重定向</span>
    <span class="hljs-comment">// 例如从路由 /home/hello 重定向到 /home?q=hello</span>
    <span class="hljs-attr">path</span>: <span class="hljs-string">'/home/:searchText'</span>,
    <span class="hljs-attr">redirect</span>: <span class="hljs-function"><span class="hljs-params">route</span> =></span> &#123;
      <span class="hljs-comment">// 方法接收当前的路由作为参数</span>
      <span class="hljs-comment">// return 重定向的字符串路径/路径对象</span>
      <span class="hljs-keyword">return</span> &#123; <span class="hljs-attr">path</span>: <span class="hljs-string">'/home'</span>, <span class="hljs-attr">query</span>: &#123; <span class="hljs-attr">q</span>: route.params.searchText &#125; &#125;
  &#125;,
]
<span class="copy-code-btn">复制代码</span></code></pre>
<p>💡 该选项的值也支持是相对路径（例如不以 <code>/</code> 开头的字符串路径就是相对路径），实现相对重定向</p>
<p>⚠️ 导航守卫并<strong>不</strong>应用在跳转路由上，而应用在其指向的路由上，因此以上例子如果针对 <code>/home</code> 路由添加一个 <code>beforeEnter</code> 守卫并不会起作用。</p>
<p>💡 如果路由配置了选项 <code>redirect</code> 时，可以省略 <code>component</code> 配置，因为该路由从来没有被直接访问过，所以没有组件要渲染。唯一的例外是嵌套路由，如果一个路由有 <code>children</code> 和 <code>redirect</code> 属性，它也应该有 <code>component</code> 属性。</p>
<h3 data-id="heading-13">路由懒加载</h3>
<p>Vue Router 支持动态导入，把不同路由对应的组件分割成不同的代码块，然后<strong>当路由被访问的时候才加载对应组件</strong>，这样就会更加高效。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// 将 import UserDetails from './views/UserDetails'</span>
<span class="hljs-comment">// 替换成</span>
<span class="hljs-keyword">const</span> UserDetails = <span class="hljs-function">() =></span> <span class="hljs-keyword">import</span>(<span class="hljs-string">'./views/UserDetails'</span>)

<span class="hljs-keyword">const</span> router = createRouter(&#123;
  <span class="hljs-comment">// ...</span>
  <span class="hljs-attr">routes</span>: [&#123; <span class="hljs-attr">path</span>: <span class="hljs-string">'/users/:id'</span>, <span class="hljs-attr">component</span>: UserDetails &#125;],
&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>💡 一般来说，对所有的路由<strong>都使用动态导入</strong>是个好主意。但<strong>不要</strong>在路由中使用<a href="https://link.juejin.cn/?target=https%3A%2F%2Fv3.vuejs.org%2Fguide%2Fcomponent-dynamic-async.html%23async-components" target="_blank" rel="nofollow noopener noreferrer" title="https://v3.vuejs.org/guide/component-dynamic-async.html#async-components" ref="nofollow noopener noreferrer">异步组件</a>，虽然异步组件仍然可以在路由组件中使用，但路由组件本身就是动态导入的。</p>
<p>💡 在路由配置中，选项 <code>component</code> 或 <code>components</code> 可以接收一个<strong>返回 Promise</strong> 的函数，该 Promise 最后需要 <code>resolve</code> 一个组件，那么 Vue Router <strong>只会在第一次进入页面时才会获取该组件</strong>，之后就会使用缓存数据，还可以在 Promise 中执行更复杂的操作</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> UserDetails = <span class="hljs-function">() =></span>
  <span class="hljs-built_in">Promise</span>.resolve(&#123;
    <span class="hljs-comment">/* 组件定义 */</span>
  &#125;)

<span class="hljs-keyword">const</span> router = createRouter(&#123;
  <span class="hljs-comment">// ...</span>
  <span class="hljs-attr">routes</span>: [&#123; <span class="hljs-attr">path</span>: <span class="hljs-string">'/users/:id'</span>, <span class="hljs-attr">component</span>: UserDetails &#125;],
&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>💡 如果使用 Webpack 打包，还可以把组件按组分块，具体配置参考<a href="https://link.juejin.cn/?target=https%3A%2F%2Fnext.router.vuejs.org%2Fguide%2Fadvanced%2Flazy-loading.html%23grouping-components-in-the-same-chunk" target="_blank" rel="nofollow noopener noreferrer" title="https://next.router.vuejs.org/guide/advanced/lazy-loading.html#grouping-components-in-the-same-chunk" ref="nofollow noopener noreferrer">官方文档</a>。</p>
<h2 data-id="heading-14">查看现有路由</h2>
<p>Vue Router 在路由实例中提供两种方法来查看现有的路由：</p>
<ul>
<li>🎉 <em><code>router.hasRoute(name)</code> 检查给定名称的路由是否存在。</em></li>
<li><code>router.getRoutes()</code> 返回一个包含<strong>所有路由</strong>记录的数组。</li>
</ul>
<h2 data-id="heading-15">增删路由</h2>
<p>一般路由的设置都是在实例化路由时完成的，通过传递给方法 <code>VueRouter.createRouter()</code> 的对象中，在该对象的属性 <code>routes</code> 中完成配置，该属性值是一个数组，每一个元素就是一个路由。</p>
<p>但是在某些情况下，你可能想在应用程序已经运行的时候再添加或删除路由，Vue Router 提供了方法 <code>addRoute()</code> 和 <code>removeRoute()</code> 实现增删路由的功能。</p>
<h3 data-id="heading-16">添加路由</h3>
<p>通过路由实例的方法 <code>router.addRoute()</code> 注册一个新的路由</p>
<p>💡 如果<strong>新增加的路由与当前页面所在的路径位置相匹配</strong>（可能当前路径被一个动态路由匹配，因为它可以基于一个模式匹配大量的路径，而新增的路由可能是一个静态路由，更「精准」地匹配当前的路径），需要<strong>手动导航</strong> <code>router.push()</code> 或 <code>router.replace()</code> 才可以应用新的路由（渲染新的视图组件）</p>
<p>如果一个应用只有一个动态路由，则进入任何页面，例如 <code>/about</code>，最终都会呈现 <code>Article</code> 组件</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> router = createRouter(&#123;
  <span class="hljs-attr">history</span>: createWebHistory(),
  <span class="hljs-attr">routes</span>: [&#123; <span class="hljs-attr">path</span>: <span class="hljs-string">'/:articleName'</span>, <span class="hljs-attr">component</span>: Article &#125;],
&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>如果我们在前面添加一个新的静态路由</p>
<pre><code class="hljs language-js copyable" lang="js">router.addRoute(&#123; <span class="hljs-attr">path</span>: <span class="hljs-string">'/about'</span>, <span class="hljs-attr">component</span>: About &#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>虽然当前页面会优先匹配到新增的路由，但是仍然会显示 <code>Article</code> 组件，我们需要<strong>手动调用 <code>router.replace()</code> 来导航</strong>以载入 <code>About</code> 组件</p>
<pre><code class="hljs language-js copyable" lang="js">router.replace(router.currentRoute.value.fullPath)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>💡 如果是在导航守卫中同时添加路由，则<strong>不</strong>应该调用 <code>router.replace()</code> 而应该<strong>直接返回一个路由</strong>，触发 Vue Router 执行重定向</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// 在导航守卫中新增一个路由</span>
<span class="hljs-comment">// 新增的路由的路径与导航目标的路径相同，所以最后返回的路径是 to.fullPath</span>
router.beforeEach(<span class="hljs-function"><span class="hljs-params">to</span> =></span> &#123;
  <span class="hljs-keyword">if</span> (!hasNecessaryRoute(to)) &#123;
    router.addRoute(generateRoute(to))
    <span class="hljs-comment">// 触发重定向</span>
    <span class="hljs-keyword">return</span> to.fullPath
  &#125;
&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>⚠️ 以上示例要满足两个假设：</p>
<ul>
<li>新添加的路由记录将与 <code>to</code> 位置相匹配，实际上导致与我们试图访问的位置不同。</li>
<li><strong>在添加新的路由后 <code>hasNecessaryRoute()</code> 返回 <code>false</code></strong><em>？</em>，以避免无限重定向。</li>
</ul>
<p>要将<strong>嵌套路由</strong>添加到现有的路由中，可以将路由的 <code>name</code> 作为第一个参数传递给 <code>router.addRoute()</code>，然后第二个参数就是嵌套路由的配置</p>
<pre><code class="hljs language-js copyable" lang="js">router.addRoute(<span class="hljs-string">'admin'</span>, &#123; <span class="hljs-attr">path</span>: <span class="hljs-string">'settings'</span>, <span class="hljs-attr">component</span>: AdminSettings &#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>等效于</p>
<pre><code class="hljs language-js copyable" lang="js">router.addRoute(&#123;
  <span class="hljs-attr">name</span>: <span class="hljs-string">'admin'</span>,
  <span class="hljs-attr">path</span>: <span class="hljs-string">'/admin'</span>,
  <span class="hljs-attr">component</span>: Admin,
  <span class="hljs-attr">children</span>: [&#123; <span class="hljs-attr">path</span>: <span class="hljs-string">'settings'</span>, <span class="hljs-attr">component</span>: AdminSettings &#125;],
&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-17">删除路由</h3>
<p>有几个不同的方法来删除现有的路由，当路由被删除时，<strong>所有的别名和子路由也会被同时删除</strong>：</p>
<ul>
<li>
<p>通过添加一个<strong>名称冲突的路由</strong>。如果添加与现有途径名称相同的途径，会先删除路由，再添加路由</p>
<pre><code class="hljs language-js copyable" lang="js">router.addRoute(&#123; <span class="hljs-attr">path</span>: <span class="hljs-string">'/about'</span>, <span class="hljs-attr">name</span>: <span class="hljs-string">'about'</span>, <span class="hljs-attr">component</span>: About &#125;)
<span class="hljs-comment">// 这将会删除之前已经添加的路由，因为他们具有相同的名字且名字必须是唯一的</span>
router.addRoute(&#123; <span class="hljs-attr">path</span>: <span class="hljs-string">'/other'</span>, <span class="hljs-attr">name</span>: <span class="hljs-string">'about'</span>, <span class="hljs-attr">component</span>: Other &#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
<li>
<p>通过调用 <code>router.addRoute()</code> 返回的回调，这对于没有命名的路由很有用</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> removeRoute = router.addRoute(routeRecord)
removeRoute() <span class="hljs-comment">// 删除路由如果存在的话</span>
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
<li>
<p>通过使用 <code>router.removeRoute()</code> <strong>按名称</strong>删除路由</p>
<pre><code class="hljs language-js copyable" lang="js">router.addRoute(&#123; <span class="hljs-attr">path</span>: <span class="hljs-string">'/about'</span>, <span class="hljs-attr">name</span>: <span class="hljs-string">'about'</span>, <span class="hljs-attr">component</span>: About &#125;)
<span class="hljs-comment">// 删除路由</span>
router.removeRoute(<span class="hljs-string">'about'</span>)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>💡 如果你想使用这个功能，但又想避免名字的冲突，可以在路由中<strong>使用 <code>Symbol</code> 作为名字</strong>。</p>
</li>
</ul>
<h2 data-id="heading-18">路由匹配</h2>
<p>Vue Router 支持多种路由匹配模式：</p>
<ul>
<li>大部分的路由是由字符串构成的<strong>静态路由</strong>，它只能匹配一个不可变的路径，例如 <code>/about</code></li>
<li>进一步根据某种模式匹配一系列路径的<strong>动态路由</strong>，例如 <code>/users/:userId</code></li>
<li>再进一步还可以使用正则表达式自定义匹配模式，以匹配需要满足复杂条件的路径，🎉 <em>正则表达式在路径参数后的<strong>括号</strong>里</em>，例如 <code>/:orderId(\d+)</code> 匹配仅由数字组成的路径，💡 由于需要转义反斜杠``，所以使用了 <code>\d+</code> 表示匹配多个（至少一个）数字</li>
</ul>
<h3 data-id="heading-19">动态路由</h3>
<p>动态路由是指把某种模式（正则表达式）匹配到的所有路由，全都映射到同个组件。</p>
<p>动态路径的参数<strong>以冒号 <code>:</code> 开头</strong></p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// 路由配置，传递给 `createRouter`</span>
<span class="hljs-keyword">const</span> routes = [
  <span class="hljs-comment">// 组件 User 对所有用户进行渲染</span>
  <span class="hljs-comment">// 但用户 username 不同，动态段以冒号开始，作为路径参数</span>
  &#123;
    <span class="hljs-attr">path</span>: <span class="hljs-string">'/user/:username'</span>, 
    <span class="hljs-attr">component</span>: User
  &#125;,
  &#123;
    <span class="hljs-attr">path</span>: <span class="hljs-string">'/user/:username/posts/:postId'</span>
    <span class="hljs-attr">component</span>: Post
  &#125;
]
<span class="copy-code-btn">复制代码</span></code></pre>
<p>匹配到的参数值（路径的的动态段，称之为<strong>路径参数</strong>）会被添加到 <code>this.$route.params</code> 对象中。而且在同一个路由中设置有<strong>多个路径参数</strong>，它们会映射到 <code>this.$route.params</code> 上的相应字段。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// User 组件</span>
<span class="hljs-keyword">const</span> User = &#123;
  <span class="hljs-attr">template</span>: <span class="hljs-string">'<p>User &#123;&#123; $route.params.username &#125;&#125;</p>'</span>,
&#125;

<span class="hljs-comment">// Post 组件</span>
<span class="hljs-keyword">const</span> Post = &#123;
  <span class="hljs-attr">template</span>: <span class="hljs-string">`
    <p>User &#123;&#123; $route.params.username &#125;&#125;</p>
    <p>Post &#123;&#123; $route.params.postId &#125;&#125;</p>
  `</span>
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>💡 实际动态路由在内部使用的默认正则表达式是 <code>[^/]+</code> 匹配 URL 中至少有一个字符不是斜杠 <code>/</code>，用以提取路径中相应的参数。</p>
<p>⚠️ 当使用动态路由匹配同一个组件时，如果只有动态路径参数改变，并<strong>不</strong>会触发组件重新渲染，而是<strong>复用原来的组件</strong>，因此<strong>组件的生命周期钩子不会再被调用</strong>。如果希望路由匹配的参数改变时，同时触发组件更新，可以设置一个侦听器 <code>watch</code> 监测 <code>$route.params</code> 的变化，或使用 Vue Router 提供的 <code>beforeRouteUpdate</code> 钩子函数进行路由守卫，然后在相应的回调函数中手动触发原来需要在生命周期钩子函数中执行的操作。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> User = &#123;
  <span class="hljs-attr">template</span>: <span class="hljs-string">'...'</span>,
  <span class="hljs-function"><span class="hljs-title">created</span>(<span class="hljs-params"></span>)</span> &#123;
    <span class="hljs-built_in">this</span>.$watch(
      <span class="hljs-function">() =></span> <span class="hljs-built_in">this</span>.$route.params,
      <span class="hljs-function">(<span class="hljs-params">toParams, previousParams</span>) =></span> &#123;
        <span class="hljs-comment">// 对路由变化做出响应...</span>
      &#125;
    )
  &#125;,
&#125;

<span class="hljs-keyword">const</span> User = &#123;
  <span class="hljs-attr">template</span>: <span class="hljs-string">'...'</span>,
  <span class="hljs-keyword">async</span> <span class="hljs-function"><span class="hljs-title">beforeRouteUpdate</span>(<span class="hljs-params">to, <span class="hljs-keyword">from</span></span>)</span> &#123;
    <span class="hljs-comment">// 对路由变化做出响应...</span>
  &#125;,
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-20">可重复的参数</h4>
<p>如果需要匹配路径中多个结构相似的部分，可以<strong>直接在路径参数后添加修饰符 <code>*</code> 或 <code>+</code></strong> （其作用和正则表达式常用的量词一样），将参数标记为可重复，而不必手动设置多个路径参数。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> routes = [
  <span class="hljs-comment">// /:chapters ->  匹配 /one, /one/two, /one/two/three, 等</span>
  &#123; <span class="hljs-attr">path</span>: <span class="hljs-string">'/:chapters+'</span> &#125;,
  <span class="hljs-comment">// /:chapters -> 匹配 /, /one, /one/two, /one/two/three, 等</span>
  &#123; <span class="hljs-attr">path</span>: <span class="hljs-string">'/:chapters*'</span> &#125;,
]
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这样路径参数得到的是一个数组，例如使用 <code>/:chapters+</code> 动态路径，去匹配路径 <code>/a/b</code>，得到的路径参数的值如下</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-built_in">console</span>.log(<span class="hljs-built_in">this</span>.$route.params.chapters) <span class="hljs-comment">// ['a', 'b']</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-21">可选的参数</h4>
<p>如果动态路由中路径参数的部分是可选的，可以<strong>在路径参数后添加 <code>?</code></strong> （其作用和正则表达式常用的量词一样，表示 0 个或 1 个）</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> routes = [
  <span class="hljs-comment">// 匹配 /users 和 /users/posva</span>
  &#123; <span class="hljs-attr">path</span>: <span class="hljs-string">'/users/:userId?'</span> &#125;,
  <span class="hljs-comment">// 匹配 /users 和 /users/42</span>
  &#123; <span class="hljs-attr">path</span>: <span class="hljs-string">'/users/:userId(\d+)?'</span> &#125;,
]
<span class="copy-code-btn">复制代码</span></code></pre>
<p>💡 <code>*</code> 在技术上也标志着一个参数是可选的，但 <code>?</code> 参数是不能重复，最多只能匹配 1 个</p>
<h3 data-id="heading-22">404 Not Found 路由</h3>
<p>动态路由的路径参数<strong>只能匹配 url 片段（用 <code>/</code> 分隔）之间的字符</strong>。🎉 <em>由于 Vue Router Next 删除了通配符 <code>*</code> 路由器，如果希望匹配任意路径（最常见的场景是用于捕获用户访问未定义的路由，再转向 404 画面），可以使用<strong>自定义的路径参数正则表达式</strong>，它写在路径参数后面的括号 <code>()</code> 中</em></p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> routes = [
  <span class="hljs-comment">// 匹配以 `/user-` 开头之后的所有内容，并将其放在路径参数 afterUser 中</span>
  <span class="hljs-comment">// 即可以通过 `$route.params.afterUser` 进行访问</span>
  &#123; 
    <span class="hljs-attr">path</span>: <span class="hljs-string">'/user-:afterUser(.*)'</span>, 
    <span class="hljs-attr">component</span>: UserGeneric 
  &#125;,
  <span class="hljs-comment">// 匹配路径的所有内容，将并将其放在路径参数 pathMatch 中</span>
  <span class="hljs-comment">// 即可以通过 `$route.params.pathMatch` 进行访问</span>
  &#123; 
    <span class="hljs-attr">path</span>: <span class="hljs-string">'/:pathMatch(.*)*'</span>, 
    <span class="hljs-attr">name</span>: <span class="hljs-string">'NotFound'</span>,
    <span class="hljs-attr">component</span>: NotFound
  &#125;,
]
<span class="copy-code-btn">复制代码</span></code></pre>
<p>以上的示例路由参数都是匹配一整段的路径，但由于正则表达式的不同，解析得到的内容也不一样</p>
<ul>
<li>路径参数 <code>afterUser</code> 的自定义正则表达式是 <code>.*</code>，它匹配到的是以 <code>/user-</code> 开头之后的所有内容，路径参数得到的是一个<strong>字符串</strong>，其中如果剩余路径内容中包括 <code>/</code> 分隔符，就会进行<strong>转译</strong>为 <code>%2F</code>，例如路径 <code>/user-ben/posts</code>，则路径参数匹配得到的字符串就是 <code>ben%2Fposts</code></li>
<li>路径参数 <code>pathMatch</code> 的自定义正则表达式一样是 <code>.*</code>，但之后还使用了修饰符 <code>*</code> 以标注路径参数是**<a href="https://juejin.cn/post/6995478754571059237#%E5%8F%AF%E9%87%8D%E5%A4%8D%E7%9A%84%E5%8F%82%E6%95%B0" target="_blank" title="#%E5%8F%AF%E9%87%8D%E5%A4%8D%E7%9A%84%E5%8F%82%E6%95%B0">重复的参数</a><strong>，因此路径参数得到的是一个</strong>数组**，其中路径中的 <code>/</code> 就是匹配解析时的分隔标志，得到数组各元素，例如路径 <code>/not/found</code>，则路径参数是 <code>['not', 'found']</code></li>
</ul>
<p>以上两种方式都可以匹配捕获整段路径，但是<strong>推荐第二种</strong>，因为当需要使用路由的名称，例如 <code>NotFound</code>，<strong>手动 push 跳转到 404 路由时</strong>，基于传递的参数，拼接出来的路径中分隔符 <code>/</code> 才不会被转译</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-built_in">this</span>.$router.push(&#123;
  <span class="hljs-attr">name</span>: <span class="hljs-string">'NotFound'</span>,
  <span class="hljs-attr">params</span>: &#123; <span class="hljs-attr">pathMatch</span>: [<span class="hljs-string">'not'</span>, <span class="hljs-string">'found'</span>] &#125;,
&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>💡 如果不是基于路由名称 push 跳转到 404 路由，而是基于路径字符串就不会出现拼接时 <code>/</code> 转译的问题。则以上两种方式都可以</p>
<p>有时候一个 url 可以匹配多个路由，此时<strong>匹配的优先级就按照路由的定义顺序</strong>：即在路由配置中，先定义的路由优先级更高；<strong>匹配顺序由上到下，直到有符合的规则为止</strong>。所以<strong>404 Not Found 路由一般放在最后</strong>，它作为「兜底」捕获一些未定义的路径。</p>
<h2 data-id="heading-23">嵌套路由</h2>
<p>当网页中一个界面有<strong>多层嵌套的组件</strong>组合而成，可以使用嵌套路由，将这些嵌套的组件与 URL 中相应的<strong>某段路径相映射</strong>，而且支持多层深度嵌套的路由-组件映射。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/0a9adb4d8275471ebeb35d47101b3ec9~tplv-k3u1fbpfcp-watermark.image" alt="嵌套路由" loading="lazy" referrerpolicy="no-referrer"></p>
<p>即在父组件中可以嵌套有自己的 <code><router-view></code>，而在配置路由时，要在该组件对应的路由（父路由）中使用<strong>选项 <code>children</code></strong> 设置内嵌的路由-子组件映射规则。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// 父组件</span>
<span class="hljs-keyword">const</span> User = &#123;
  <span class="hljs-attr">template</span>: <span class="hljs-string">`<div class="page">
    <p>User</p>
      // 基于路由将嵌套的子组件渲染在此
      <router-view></router-view>
    </div>`</span>
&#125;;

<span class="hljs-comment">// 子组件</span>
<span class="hljs-keyword">const</span> Profile = &#123;
  <span class="hljs-attr">template</span>: <span class="hljs-string">`<div class="page">Profile</div>`</span>
&#125;;
<span class="hljs-keyword">const</span> Posts = &#123;
  <span class="hljs-attr">template</span>: <span class="hljs-string">`<div class="page">Posts</div>`</span>
&#125;

<span class="hljs-keyword">const</span> router = <span class="hljs-keyword">new</span> VueRouter(&#123;
  <span class="hljs-comment">// 路由规则</span>
  <span class="hljs-attr">routes</span>: [
  <span class="hljs-comment">// ...</span>
    &#123;
      <span class="hljs-attr">path</span>: <span class="hljs-string">'/user/:id'</span>,
      <span class="hljs-attr">component</span>: User,
      <span class="hljs-comment">// 嵌套路由</span>
      <span class="hljs-attr">children</span>: [
        &#123;
          <span class="hljs-comment">// UserProfile will be rendered inside User's <router-view></span>
          <span class="hljs-comment">// when /user/:id/profile is matched</span>
          <span class="hljs-attr">path</span>: <span class="hljs-string">'profile'</span>,
          <span class="hljs-attr">component</span>: UserProfile
        &#125;,
        &#123;
          <span class="hljs-comment">// UserPosts will be rendered inside User's <router-view></span>
          <span class="hljs-comment">// when /user/:id/posts is matched</span>
          <span class="hljs-attr">path</span>: <span class="hljs-string">'posts'</span>,
          <span class="hljs-attr">component</span>: UserPosts
        &#125;
      ]
    &#125;,
  ]
&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>其实路由的选项 <code>children</code> 只是另一个路由数组，就像 <code>routes</code> 本身一样，因此可以根据自己的需要，不断地嵌套视图。</p>
<p>⚠️ 一般路由 <code>path</code> 会以 <code>/</code> 开头，<strong>但嵌套路径不会使用</strong>，因为 <code>/</code> 会被当作根路径（绝对路径），使用相对路径可以使用嵌套组件而无须设置嵌套的路径，<strong>迁移更方便</strong>。</p>
<p>💡 如果希望嵌套路由可以支持访问上一级的路由时，父组件的 <code><router-view></code> 也渲染出页面，可以在使用<strong>选项 <code>children</code></strong> 设置内嵌的路由-子组件映射规则时，<strong>添加一个 <code>path</code> 为空字串 <code>""</code> 的规则</strong>。即路径的嵌套部分为空时，也可以渲染出一个默认的嵌套组件。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> router = <span class="hljs-keyword">new</span> VueRouter(&#123;
  <span class="hljs-attr">routes</span>: [
    &#123;
      <span class="hljs-attr">path</span>: <span class="hljs-string">'/user/:id'</span>,
      <span class="hljs-attr">component</span>: User,
      <span class="hljs-attr">children</span>: [
        <span class="hljs-comment">// UserHome will be rendered inside User's <router-view></span>
        <span class="hljs-comment">// when /user/:id is matched</span>
        &#123; <span class="hljs-attr">path</span>: <span class="hljs-string">''</span>, <span class="hljs-attr">component</span>: UserHome &#125;
        <span class="hljs-comment">// ...other sub routes</span>
      ]
    &#125;
  ]
&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-24">路由导航</h2>
<p>Vue Router 有两种方式切换 url 路径</p>
<ul>
<li>使用组件 <code><router-link></code> 组件进行导航，该组件会在页面上渲染为 <code><a></code> 标签。</li>
<li>使用 Vue Router 提供的方法通过 JS 手动切换 url 路径，称为<strong>编程式导航</strong>。</li>
</ul>
<p>💡 🎉 在 Vue Router Next 中所有的导航，包括第一个导航，现在都是<strong>异步</strong>的，即编程式导航的各种方法都<strong>返回一个 Promise</strong>*，如果要基于导航完成后再执行操作，需要使用异步编程 <code>await</code> 或 <code>then</code></p>
<p>例如页面有一个弹出的导航菜单，我们<strong>希望在导航到新页面后</strong>隐藏菜单，因为<strong>导航是异步的</strong>，我们需要 <code>await</code> 等到 <code>router.push</code> 返回的 promise 解析 <code>resovle</code> 或 <code>reject</code> 后才执行菜单隐藏</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">await</span> router.push(<span class="hljs-string">'/my-profile'</span>)
<span class="hljs-built_in">this</span>.isMenuOpen = <span class="hljs-literal">false</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-25">router-link</h3>
<p>使用 <code><router-link></code> 组件来导航，通过属性 <code>to</code> 指定路径，它默认渲染为 <code><a></code> 标签，并将组件标签中的内容包裹在其中（插槽，支持 HTML），实现类似 url 切换的功能</p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">router-link</span> <span class="hljs-attr">to</span>=<span class="hljs-string">"/home"</span>></span>Home Page<span class="hljs-tag"></<span class="hljs-name">router-link</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>🔨 渲染结果</p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">a</span> <span class="hljs-attr">href</span>=<span class="hljs-string">"/home"</span>></span>Home Page<span class="hljs-tag"></<span class="hljs-name">a</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>💡 如果希望点击链接后，导航是以<strong>替换当前路由</strong>的形式进行（即导航后不会留下历史记录），可以为组件 <code><router-link></code> 设置<strong>属性 <code>replace</code></strong>，这样用户点击链接时会调用 <code>router.replace()</code>，而不是 <code>router.push()</code></p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">router-link</span> <span class="hljs-attr">to</span>=<span class="hljs-string">"/abc"</span> <span class="hljs-attr">replace</span>></span><span class="hljs-tag"></<span class="hljs-name">router-link</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-26">to 属性</h4>
<p>组件 <code><router-link></code> 的属性 <code>to</code> 是用以描述该链接要导航到哪个目标路由，它的属性值可以是一个表示路径的<strong>字符串</strong>，或一个描述路径的<strong>对象</strong></p>
<p>💡 由于当被点击后，内部会立刻把 <code>to</code> 的值传到 <code>router.push()</code> 实现导航，所以属性 <code>to</code> 与 <code>router.push</code> <a href="https://juejin.cn/post/6995478754571059237#%E7%BC%96%E7%A8%8B%E5%BC%8F%E5%AF%BC%E8%88%AA" target="_blank" title="#%E7%BC%96%E7%A8%8B%E5%BC%8F%E5%AF%BC%E8%88%AA">接受的值的规则完全相同</a>。</p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-comment"><!-- 字符串 --></span>
<span class="hljs-tag"><<span class="hljs-name">router-link</span> <span class="hljs-attr">to</span>=<span class="hljs-string">"/home"</span>></span>Home<span class="hljs-tag"></<span class="hljs-name">router-link</span>></span>
<span class="hljs-comment"><!-- 渲染结果 --></span>
<span class="hljs-comment"><!-- <a href="/home">Home</a> --></span>

<span class="hljs-comment"><!-- 使用 v-bind 的 JS 表达式 --></span>
<span class="hljs-tag"><<span class="hljs-name">router-link</span> <span class="hljs-attr">:to</span>=<span class="hljs-string">"'/home'"</span>></span>Home<span class="hljs-tag"></<span class="hljs-name">router-link</span>></span>
<span class="hljs-comment"><!-- 渲染结果同上 --></span>

<span class="hljs-comment"><!-- 传递一个带有路径属性 path 的对象  --></span>
<span class="hljs-tag"><<span class="hljs-name">router-link</span> <span class="hljs-attr">:to</span>=<span class="hljs-string">"&#123; path: '/home' &#125;"</span>></span>Home<span class="hljs-tag"></<span class="hljs-name">router-link</span>></span>
<span class="hljs-comment"><!-- 渲染结果同上 --></span>

<span class="hljs-comment"><!-- 命名路由，带有路径参数 --></span>
<span class="hljs-tag"><<span class="hljs-name">router-link</span> <span class="hljs-attr">:to</span>=<span class="hljs-string">"&#123; name: 'user', params: &#123; userId: '123' &#125;&#125;"</span>></span>User<span class="hljs-tag"></<span class="hljs-name">router-link</span>></span>

<span class="hljs-comment"><!-- 带查询参数 --></span>
<span class="hljs-tag"><<span class="hljs-name">router-link</span> <span class="hljs-attr">:to</span>=<span class="hljs-string">"&#123; path: '/register', query: &#123; plan: 'private' &#125;&#125;"</span>></span>Register<span class="hljs-tag"></<span class="hljs-name">router-link</span>></span>
<span class="hljs-comment"><!-- 渲染结果 --></span>
<span class="hljs-comment"><!-- <a href="/register?plan=private">Register</a> --></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-27">自定义标签</h4>
<p>🎉 <em>Vue Router Next 中删除了 <code><router-link></code> 的属性 <code>tag</code></em>，如果希望<strong>定制该组件渲染为另一种标签</strong>，<em>可以<a href="https://link.juejin.cn/?target=https%3A%2F%2Fnext.router.vuejs.org%2Fzh%2Fapi%2F%23router-link-props" target="_blank" rel="nofollow noopener noreferrer" title="https://next.router.vuejs.org/zh/api/#router-link-props" ref="nofollow noopener noreferrer">需要添加属性 <code>custom</code></a></em>（默认是 <code>false</code>，将该属性添加到组件 <code><router-link></code> 时其值就是 <code>true</code>），表示使用自定义的方式（直接基于插槽内容渲染组件），而不需要将插槽内容包裹在 <code><a></code> 元素中。</p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">router-link</span> <span class="hljs-attr">to</span>=<span class="hljs-string">"/home"</span> <span class="hljs-attr">custom</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">span</span>></span>Home Page<span class="hljs-tag"></<span class="hljs-name">span</span>></span>
<span class="hljs-tag"></<span class="hljs-name">router-link</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>🔨 渲染结果</p>
<pre><code class="hljs language-html copyable" lang="html"> <span class="hljs-tag"><<span class="hljs-name">span</span>></span>Home Page<span class="hljs-tag"></<span class="hljs-name">span</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-28">作用域插槽</h4>
<p>组件 <code><router-link></code> 的<strong>作用域插槽 <code>v-slot</code> 暴露了<a href="https://link.juejin.cn/?target=https%3A%2F%2Fnext.router.vuejs.org%2Fapi%2Findex.html%23router-link-s-v-slot" target="_blank" rel="nofollow noopener noreferrer" title="https://next.router.vuejs.org/api/index.html#router-link-s-v-slot" ref="nofollow noopener noreferrer">一些关于相应路由（属性 <code>to</code> 指向的路由）的参数</a></strong>，然后可以用在插槽中，定制组件渲染的内容。</p>
<p>⚠️ 如果要定制化组件的渲染内容，记得为组件 <code><router-link></code> 添加属性 <code>custom</code> 以防止插槽的内容默认包裹在 <code><a></code> 元素内，导致渲染定制内容时出现问题。</p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">router-link</span>
  <span class="hljs-attr">to</span>=<span class="hljs-string">"/about"</span>
  <span class="hljs-attr">custom</span>
  <span class="hljs-attr">v-slot</span>=<span class="hljs-string">"&#123; href, route, navigate, isActive, isExactActive &#125;"</span>
></span>
  <span class="hljs-comment"><!-- 一个自定义的「链接」组件，接收路由的相关信息作为 props --></span>
  <span class="hljs-tag"><<span class="hljs-name">NavLink</span> <span class="hljs-attr">:active</span>=<span class="hljs-string">"isActive"</span> <span class="hljs-attr">:href</span>=<span class="hljs-string">"href"</span> @<span class="hljs-attr">click</span>=<span class="hljs-string">"navigate"</span>></span>
    &#123;&#123; route.fullPath &#125;&#125;
  <span class="hljs-tag"></<span class="hljs-name">NavLink</span>></span>
<span class="hljs-tag"></<span class="hljs-name">router-link</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li><code>href</code>：解析属性 <code>to</code> 后得到的 URL，将会作为默认 <code><a></code> 元素的 <code>href</code> 属性。如果什么都没提供，则它会包含 <code>base</code></li>
<li><code>route</code>：解析属性 <code>to</code> 后的规范化的地址</li>
<li><code>navigate</code>：触发导航的函数。 <strong>会在必要时自动阻止事件</strong>，和 <code>router-link</code> 一样。例如：<code>ctrl</code> 或者 <code>cmd</code> + click 仍然会被 <code>navigate</code> 忽略</li>
<li><code>isActive</code>：如果需要应用 <a href="https://link.juejin.cn/?target=https%3A%2F%2Fnext.router.vuejs.org%2Fzh%2Fapi%2F%23active-class" target="_blank" rel="nofollow noopener noreferrer" title="https://next.router.vuejs.org/zh/api/#active-class" ref="nofollow noopener noreferrer">active class</a>，则为 <code>true</code>（在组件上设置了属性 <code>active-class</code>）</li>
<li><code>isExactActive</code>：如果需要应用 <a href="https://link.juejin.cn/?target=https%3A%2F%2Fnext.router.vuejs.org%2Fzh%2Fapi%2F%23exact-active-class" target="_blank" rel="nofollow noopener noreferrer" title="https://next.router.vuejs.org/zh/api/#exact-active-class" ref="nofollow noopener noreferrer">exact active class</a>，则为 <code>true</code>（在组件上设置了属性 <code>exact-active-class</code>）</li>
</ul>
<p>💡 路由激活时，是指组件 <code><router-link></code> 的属性 <code>to</code> 与当前 url 路径匹配上），该组件的根元素会添加上类名 <code>.router-link-active</code>；而路由准确匹配上的元素则会再加上类名 <code>.router-link-exact-active</code>，可以使用这两个 <code>class</code> 类属性设置样式</p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">router-link</span> <span class="hljs-attr">to</span>=<span class="hljs-string">"/"</span>></span>Index<span class="hljs-tag"></<span class="hljs-name">router-link</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-29">编程式导航</h3>
<p>使用 Vue Router 提供的方法通过 JS 手动切换 url 路径，称为<strong>编程式导航</strong></p>
<p>💡 这些方法是效仿浏览器提供的 API <code>window.history</code>，以下路由方法分别类似于 <code>window.history.pushState</code>、<code>window.history.replaceState</code> 和 <code>window.history.go</code></p>
<p>💡 如果路由导航的目的地和当前路由<strong>映射的组件是相同</strong>，如（动态路由）只有参数发生了改变，为了优化效率，组件会复用，即在组件生命周期钩子函数中执行的操作并不会再次执行，需要使用 <code>beforeRouteUpdate</code> 钩子函数进行路由守卫，或 <code>watch</code> 监听路由的变化然后在相应的回调函数中手动触发原来所需的操作。</p>
<h4 data-id="heading-30">常规导航</h4>
<p>最常见的导航方式是使用方法 <code>$router.push(location)</code> 将页面导航到指定的 <code>location</code>，并向 history 栈添加一个新的记录</p>
<p>💡 相应的声明式导航是 <code><router-link to="location"></code></p>
<p>该方法的参数可以是一个表示路径的字符串，或一个描述路径的对象</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// 字符串路径</span>
router.push(<span class="hljs-string">'/users/ben'</span>)

<span class="hljs-comment">// 带有路径属性 path 的对象</span>
router.push(&#123; <span class="hljs-attr">path</span>: <span class="hljs-string">'/users/ben'</span> &#125;)

<span class="hljs-comment">// 使用命名路由（假设路由对应的路径是 /users/:username），并加上路径参数（让路由建立 url，将参数「填入」相应动态路径的路径参数）</span>
<span class="hljs-comment">// 结果是 /users/ben</span>
router.push(&#123; <span class="hljs-attr">name</span>: <span class="hljs-string">'user'</span>, <span class="hljs-attr">params</span>: &#123; <span class="hljs-attr">username</span>: <span class="hljs-string">'ben'</span> &#125; &#125;)

<span class="hljs-comment">// 带有路径属性 path 的对象，并带查询参数（让路由建立 url）</span>
<span class="hljs-comment">// 结果是 /register?plan=private</span>
router.push(&#123; <span class="hljs-attr">path</span>: <span class="hljs-string">'/register'</span>, <span class="hljs-attr">query</span>: &#123; <span class="hljs-attr">plan</span>: <span class="hljs-string">'private'</span> &#125; &#125;)

<span class="hljs-comment">// 带有路径属性 path 的对象，并带 hash</span>
<span class="hljs-comment">// 结果是 /about#team</span>
router.push(&#123; <span class="hljs-attr">path</span>: <span class="hljs-string">'/about'</span>, <span class="hljs-attr">hash</span>: <span class="hljs-string">'#team'</span> &#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>💡 如果方法 <code>$router.push()</code> 传入的描述路径的对象中，即提供了 <code>path</code> 属性，也提供了 <code>params</code> 属性，那么 <code>params</code> 就会被忽略。因此传递对象时，要么是将参数手动进行拼接，要么是以 <code>name</code> 和 <code>params</code> 的方式来提供参数</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> username = <span class="hljs-string">'ben'</span>
<span class="hljs-comment">// 我们可以手动建立 url，但我们必须自己处理编码</span>
router.push(<span class="hljs-string">`/user/<span class="hljs-subst">$&#123;username&#125;</span>`</span>) <span class="hljs-comment">// -> /user/ben</span>
<span class="hljs-comment">// 同样</span>
router.push(&#123; <span class="hljs-attr">path</span>: <span class="hljs-string">`/user/<span class="hljs-subst">$&#123;username&#125;</span>`</span> &#125;) <span class="hljs-comment">// -> /user/ben</span>
<span class="hljs-comment">// 如果可能的话，使用 `name` 和 `params` 从自动 URL 编码中获益</span>
router.push(&#123; <span class="hljs-attr">name</span>: <span class="hljs-string">'user'</span>, <span class="hljs-attr">params</span>: &#123; username &#125; &#125;) <span class="hljs-comment">// -> /user/ben</span>
<span class="hljs-comment">// `params` 不能与 `path` 一起使用</span>
router.push(&#123; <span class="hljs-attr">path</span>: <span class="hljs-string">'/user'</span>, <span class="hljs-attr">params</span>: &#123; username &#125; &#125;) <span class="hljs-comment">// -> /user</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-31">替换式导航</h4>
<p>使用方法 <code>$router.push(&#123;path: location, replace: true&#125;)</code>（增加要给属性 <code>repalce</code>）或 <code>$router.replace(location)</code> 导航到指定的 <code>location</code>，它<strong>不</strong>会向 history 添加新记录，而是替换掉当前的 history 记录</p>
<p>💡 相应的声明式导航是 <code><router-link to="location" replace></code></p>
<h4 data-id="heading-32">历史记录导航</h4>
<p>使用方法 <code>$router.go(n)</code> 在 history 记录中向前或者后退 <code>n</code> 步，类似 <code>window.history.go(n)</code>，如果输入的数值过大或过小，而 history 记录不够用，跳转就会<strong>失败</strong></p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// 向前移动一条记录，与 router.forward() 相同</span>
router.go(<span class="hljs-number">1</span>)

<span class="hljs-comment">// 返回一条记录，与router.back() 相同</span>
router.go(-<span class="hljs-number">1</span>)

<span class="hljs-comment">// 前进 3 条记录</span>
router.go(<span class="hljs-number">3</span>)

<span class="hljs-comment">// 如果没有那么多记录，静默失败</span>
router.go(-<span class="hljs-number">100</span>)
router.go(<span class="hljs-number">100</span>)
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-33">导航故障</h3>
<p>导航故障/导航失败 navigation failures，表示一次失败的导航，所期待的导航被阻止，用户仍<strong>留在同一页面上</strong>：</p>
<ul>
<li>用户已经位于他们正在尝试导航到的页面</li>
<li>导航守卫 <code>return false</code> 或调用 <code>next(false)</code> 中断了这次导航</li>
<li>当前的导航守卫还没有完成时，一个新的导航守卫会出现了</li>
<li>导航守卫通过返回一个路由，重定向到其他地方（例如对于未登录的用户一直重定向到 <code>/login</code> 页面）</li>
<li>导航守卫抛出了一个错误 <code>Error</code></li>
</ul>
<p>导航故障时，导航返回的 <code>Promise</code> 被解析为 <strong>Navigation Failure</strong>，它是一个带有一些额外属性的 <code>Error</code> 实例（而正常情况下，导航成功 Promise 被解析为一个 <em>falsy</em> 值，通常是 <code>undefined</code>），这样我们就可以区分我们导航是否离开了当前位置：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> navigationResult = <span class="hljs-keyword">await</span> router.push(<span class="hljs-string">'/home'</span>)

<span class="hljs-keyword">if</span> (navigationResult) &#123;
  <span class="hljs-comment">// 导航被阻止</span>
&#125; <span class="hljs-keyword">else</span> &#123;
  <span class="hljs-comment">// 导航成功 (包括重新导航的情况)</span>
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-34">鉴别导航故障</h4>
<p>要检查一个错误是否来自于路由器，可以使用 <code>isNavigationFailure</code> 函数，它接收第一个参数是导航的 Promise，以判断导航解析的类型，（可选）第二个参数是 <code>NavigationFailureType</code> 区分不同类型的<em>导航故障</em></p>
<p>💡 如果只传递第一个参数 <code>isNavigationFailure(failure)</code> 忽略第二个参数，那么就只会检查这个 <code>failure</code> 是不是一个 <em>Navigation Failure</em></p>
<p>🎉 <code>NavigationFailureType</code> 有<strong>三种</strong>不同的类型*，对应于不同的情况下导致导航的中止：</p>
<ul>
<li><code>aborted</code>：在导航守卫中返回 <code>false</code> 或调用了 <code>next(false)</code> 中断了本次导航。</li>
<li><code>cancelled</code>：在当前导航还没有完成之前又有了一个新的导航。比如在等待导航守卫的过程中，又调用了 <code>router.push</code>。</li>
<li><code>duplicated</code>：导航被阻止，因为我们已经在目标位置了。</li>
</ul>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">import</span> &#123; isNavigationFailure, NavigationFailureType &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'vue-router'</span>

<span class="hljs-comment">// 试图离开未保存的编辑文本界面</span>
<span class="hljs-keyword">const</span> failure = <span class="hljs-keyword">await</span> router.push(<span class="hljs-string">'/articles/2'</span>)
<span class="hljs-comment">// 如果导航故障，且故障类型是 aborted</span>
<span class="hljs-keyword">if</span> (isNavigationFailure(failure, NavigationFailureType.aborted)) &#123;
  <span class="hljs-comment">// 给用户显示一个小通知</span>
  showToast(<span class="hljs-string">'You have unsaved changes, discard and leave anyway?'</span>)
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>💡 所有的导航故障都会有 <code>to</code> 和 <code>from</code> 属性，分别用来表达这次失败的导航的<strong>目标位置</strong>和<strong>当前位置</strong></p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// 正在尝试访问 admin 页面</span>
router.push(<span class="hljs-string">'/admin'</span>).then(<span class="hljs-function"><span class="hljs-params">failure</span> =></span> &#123;
  <span class="hljs-keyword">if</span> (isNavigationFailure(failure, NavigationFailureType.redirected)) &#123;
    failure.to.path <span class="hljs-comment">// '/admin'</span>
    failure.from.path <span class="hljs-comment">// '/'</span>
  &#125;
&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-35">检测重定向</h4>
<p>还有一种导航故障是导航守卫通过返回一个路由，重定向到其他地方，它会触发一个新的导航，覆盖正在进行的导航。</p>
<p>与其他导航守卫的返回值不同的是，重定向<strong>不会阻止导航，而是创建一个新的导航</strong>，可以通过读取当前路由地址中的 <strong><code>redirectedFrom</code> 属性</strong>，对其进行检查</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">await</span> router.push(<span class="hljs-string">'/my-profile'</span>)
<span class="hljs-keyword">if</span> (router.currentRoute.value.redirectedFrom) &#123;
  <span class="hljs-comment">// redirectedFrom 是解析出的路由地址</span>
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-36">导航守卫</h2>
<p>导航守卫是在指用户访问特定的路径时，<strong>基于条件执行跳转或取消的操作</strong>，从而在前端对特定页面和数据进行「保护」。有多种机会植入导航守卫，可以设置全局的、单个路由独享的、或者组件级的路由守卫。</p>
<p>💡 守卫是<strong>异步</strong>解析执行，因此导航在所有守卫 resolve 完之前一直处于<strong>等待中</strong></p>
<p>完整的路由导航解析流程：</p>
<ol start="0">
<li>导航被触发</li>
<li>在失活的组件里调用 <strong><code>beforeRouteLeave</code> 守卫</strong>（组件内的守卫）</li>
<li>调用全局的 <strong><code>beforeEach</code> 守卫</strong>（全局前置守卫）</li>
<li>在重用的组件里调用 <strong><code>beforeRouteUpdate</code> 守卫</strong>（组件内的守卫，路由更新，但组件复用）</li>
<li>在路由配置里调用 <strong><code>beforeEnter</code> 守卫</strong>（路由独享的守卫）</li>
<li>解析异步路由组件</li>
<li>在被激活的组件里调用 <strong><code>beforeRouteEnter</code> 守卫</strong>（组件内的守卫）</li>
<li>调用全局的 <strong><code>beforeResolve</code> 守卫</strong>（全局解析守卫）</li>
<li>导航被确认</li>
<li>调用全局的 <strong><code>afterEach</code> 钩子</strong>（全局后置守卫）</li>
<li>触发 DOM 更新</li>
<li>调用 <code>beforeRouteEnter</code> 守卫中传给 <strong><code>next</code> 的回调函数</strong>，创建好的组件实例会作为回调函数的参数传入</li>
</ol>
<p>💡 路由的参数 <code>params</code> 或查询 <code>query</code> 的改变并<strong>不</strong>会触发进入/离开类型的导航守卫。可以通过 <code>watch</code> 观察 <code>$route</code> 路由对象来应对这些变化，或使用 <a href="https://juejin.cn/post/6995478754571059237#%E7%BB%84%E4%BB%B6%E5%86%85%E5%AE%88%E5%8D%AB" target="_blank" title="#%E7%BB%84%E4%BB%B6%E5%86%85%E5%AE%88%E5%8D%AB"><code>beforeRouteUpdate</code> 组件内守卫</a>来响应这些变化。</p>
<h3 data-id="heading-37">回调函数</h3>
<h4 data-id="heading-38">入参</h4>
<p>路由守卫回调函数一般接收两个参数：</p>
<ul>
<li><code>to</code> 即将要进入的目标（路由对象 route）</li>
<li><code>from</code> 当前导航正要离开的路由对象 route</li>
</ul>
<p>💡 🎉 <em>由守卫的回调函数还可以接收第三个（可选）参数 <code>next</code>，它是一个函数，通过调用它以验证导航。但是如果守卫的回调函数中有<a href="https://juejin.cn/post/6995478754571059237#%E8%BF%94%E5%9B%9E%E5%80%BC" target="_blank" title="#%E8%BF%94%E5%9B%9E%E5%80%BC">返回值</a>，则可以省略 <code>next</code>，并且鼓励这么做。</em></p>
<p>⚠️ <strong>如果传递了该参数，请确保它被严格调用一次</strong>，这样守卫才可以 <code>resolve</code> Promise 以「放行」，否则页面将会「卡住」，无法顺利跳转或展示数据。它的执行效果依赖调用时传递的参数：</p>
<ul>
<li>
<p><code>next()</code> 不传递参数时，会进行管道中的下一个钩子</p>
</li>
<li>
<p><code>next(false)</code> 中断当前的导航</p>
</li>
<li>
<p><code>next('/otherPath')</code> 或者 <code>next(&#123; path: '/otherPath' &#125;)</code> 当前的导航被中断，然后进行一个新的导航。跳转到一个不同的地址</p>
<p>💡 传递对象可以定制跳转的方式，如 <code>next(&#123; replace: true、name: 'home' &#125;)</code> 以取代历史记录的方式，跳转导航到首页。</p>
</li>
<li>
<p><code>next(error)</code> 传入 next 的参数是一个 Error 实例，则导航会被终止。</p>
</li>
</ul>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// 在用户未能验证身份时，重定向到 /login 页面</span>
router.beforeEach(<span class="hljs-function">(<span class="hljs-params">to, <span class="hljs-keyword">from</span>, next</span>) =></span> &#123;
  <span class="hljs-keyword">if</span> (to.name !== <span class="hljs-string">'Login'</span> && !isAuthenticated) next(&#123; <span class="hljs-attr">name</span>: <span class="hljs-string">'Login'</span> &#125;)
  <span class="hljs-keyword">else</span> next()
&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-39">返回值</h4>
<p>路由守卫回调函数有多种返回值，相应执行不同的导航行为</p>
<ul>
<li>
<p>无返回（即返回 <code>undefined</code>）或返回 <code>true</code>：执行预期的导航</p>
</li>
<li>
<p>返回 <code>false</code>：取消当前的导航</p>
<pre><code class="hljs language-js copyable" lang="js">router.beforeEach(<span class="hljs-function">(<span class="hljs-params">to, <span class="hljs-keyword">from</span></span>) =></span> &#123;
  <span class="hljs-comment">// ...</span>
  <span class="hljs-comment">// 返回 false 以取消导航</span>
  <span class="hljs-keyword">return</span> <span class="hljs-literal">false</span>
&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>如果浏览器的 URL 改变了（可能是用户手动或者浏览器后退按钮），那么 URL 地址会重置到 <code>from</code> 路由对应的地址</p>
</li>
<li>
<p>返回一个路由地址：执行导航到另外的地址</p>
<p>路由地址可以是一个表示路径的字符串，也可以是一个描述路由信息的对象，可以设置如 <code>replace: true</code> 或 <code>name: 'home'</code> 等选项。这时候类似于调用 <code>router.push()</code> 一样，手动执行导航，跳转到返回的地址（与用户原来期待的导航路径不同）</p>
</li>
<li>
<p>抛出一个 <code>Error</code>：取消导航并且调用执行 <code>router.onError()</code> 注册过的回调</p>
<p>一般是遇到意料之外的情况</p>
</li>
</ul>
<p>以下是常用的路由守卫钩子函数，根据实际情况选择合适的钩子函数进行路由守卫：</p>
<h3 data-id="heading-40">全局前置守卫</h3>
<p>全局路由守卫 <code>beforeEach</code> 在进入任何路由<strong>前</strong>都会调用。可以使用路由实例的方法 <code>beforeEach()</code> 定义一个全局路由守卫，当一个导航触发时，全局前置守卫<strong>按照创建顺序依此调用</strong>。</p>
<pre><code class="hljs language-js copyable" lang="js">router.beforeEach(<span class="hljs-function">(<span class="hljs-params">to, <span class="hljs-keyword">from</span></span>) =></span> &#123;
  ...
&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-41">全局解析守卫</h3>
<p>全局解析守卫 <code>beforeResolve</code> 和全局前置守卫 <code>beforeEach</code> 类似，也是在每次导航都会调用，但它会在<strong>所有组件内守卫和异步路由组件被解析之后，在确认导航之前</strong>被调用。</p>
<p>全局解析守卫执行时，<strong>用户还未进入页面</strong>，一般会在该守卫的回调函数中 fetch 数据，可以访问路由的元信息，或者执行一些预判操作，如权限询问获取，尽早阻止用户访问相应的页面（以便避免用户即使进入了页面，却因为不符合条件，而无法执行一些操作）。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// 通过全局解析守卫，获取目的路由的 meta 元信息</span>
<span class="hljs-comment">// 该路由的元信息有 requiresCamera 选项（布尔值）表示跳转的页面需要使用设备摄像机</span>
router.beforeResolve(<span class="hljs-keyword">async</span> to => &#123;
  <span class="hljs-keyword">if</span> (to.meta.requiresCamera) &#123;
    <span class="hljs-keyword">try</span> &#123;
      <span class="hljs-comment">// 可以在路由守卫中先尝试获取访问设备摄像机的权限</span>
      <span class="hljs-keyword">await</span> askForCameraPermission()
    &#125; <span class="hljs-keyword">catch</span> (error) &#123;
      <span class="hljs-comment">// 如果无法获取权限就取消导航</span>
      <span class="hljs-keyword">if</span> (error <span class="hljs-keyword">instanceof</span> NotAllowedError) &#123;
        <span class="hljs-comment">// ...</span>
        <span class="hljs-keyword">return</span> <span class="hljs-literal">false</span>
      &#125; <span class="hljs-keyword">else</span> &#123;
        <span class="hljs-comment">// 意料之外的错误，取消导航并把错误传给全局处理器</span>
        <span class="hljs-keyword">throw</span> error
      &#125;
    &#125;
  &#125;
&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-42">全局后置钩子</h3>
<p>全局后置钩子 <code>afterEach</code> 在<strong>导航被确认时</strong>调用，这个钩子<strong>不</strong>会接受 <code>next</code> 函数，也<strong>不会改变导航本身</strong>。</p>
<p>可以在这个路由守卫中对所有导航成功所进入的页面进行操作，例如可以实现分析、更改页面标题，声明页面等辅助功能。</p>
<pre><code class="hljs language-js copyable" lang="js">router.afterEach(<span class="hljs-function">(<span class="hljs-params">to, <span class="hljs-keyword">from</span></span>) =></span> &#123;
  sendToAnalytics(to.fullPath)
&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>💡 导航失败的信息 <a href="https://link.juejin.cn/?target=https%3A%2F%2Fnext.router.vuejs.org%2Fguide%2Fadvanced%2Fnavigation-failures.html" target="_blank" rel="nofollow noopener noreferrer" title="https://next.router.vuejs.org/guide/advanced/navigation-failures.html" ref="nofollow noopener noreferrer">navigation failures</a> 可以作为（可选）第三个参数</p>
<pre><code class="hljs language-js copyable" lang="js">router.afterEach(<span class="hljs-function">(<span class="hljs-params">to, <span class="hljs-keyword">from</span>, failure</span>) =></span> &#123;
  <span class="hljs-keyword">if</span> (!failure) sendToAnalytics(to.fullPath)
&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-43">路由独享守卫</h3>
<p>路由独享的守卫 <code>beforeEnter</code> 只有在进入特定路径前调用。可以在路由配置时，使用选项 <code>beforeEnter</code> 针对特定的路由进行定义。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// 路由配置</span>
<span class="hljs-keyword">const</span> routes = [
  &#123;
    <span class="hljs-attr">path</span>: <span class="hljs-string">'/users/:id'</span>,
    <span class="hljs-attr">component</span>: UserDetails,
    <span class="hljs-attr">beforeEnter</span>: <span class="hljs-function">(<span class="hljs-params">to, <span class="hljs-keyword">from</span></span>) =></span> &#123;
      <span class="hljs-comment">// reject the navigation</span>
      <span class="hljs-keyword">return</span> <span class="hljs-literal">false</span>
    &#125;,
  &#125;,
]
<span class="copy-code-btn">复制代码</span></code></pre>
<p>💡 可以 🎉 <em>将一个组函数数组传递给 <code>beforeEnter</code></em>，它们会被依此执行，这在为不同的路由重用守卫时很有用</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">removeQueryParams</span>(<span class="hljs-params">to</span>) </span>&#123;
  <span class="hljs-keyword">if</span> (<span class="hljs-built_in">Object</span>.keys(to.query).length)
    <span class="hljs-keyword">return</span> &#123; <span class="hljs-attr">path</span>: to.path, <span class="hljs-attr">query</span>: &#123;&#125;, <span class="hljs-attr">hash</span>: to.hash &#125;
&#125;

<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">removeHash</span>(<span class="hljs-params">to</span>) </span>&#123;
  <span class="hljs-keyword">if</span> (to.hash) <span class="hljs-keyword">return</span> &#123; <span class="hljs-attr">path</span>: to.path, <span class="hljs-attr">query</span>: to.query, <span class="hljs-attr">hash</span>: <span class="hljs-string">''</span> &#125;
&#125;

<span class="hljs-comment">// 路由配置</span>
<span class="hljs-keyword">const</span> routes = [
  &#123;
    <span class="hljs-attr">path</span>: <span class="hljs-string">'/users/:id'</span>,
    <span class="hljs-attr">component</span>: UserDetails,
    <span class="hljs-attr">beforeEnter</span>: [removeQueryParams, removeHash], <span class="hljs-comment">// 函数数组</span>
  &#125;,
]
<span class="copy-code-btn">复制代码</span></code></pre>
<p>💡 路由独享守卫 <code>beforeEnter</code> 只在进入路由时触发，<strong>不</strong>会在 <code>params</code>、<code>query</code> 或 <code>hash</code> 改变时触发。</p>
<h3 data-id="heading-44">组件内守卫</h3>
<p>可以在<strong>组件内</strong>定义路由守卫，这些路由守卫会在该组件相应的路由修改时作出反应。</p>
<h4 data-id="heading-45">选项式 API</h4>
<p>可以在组件中使用以下选项，为路由组件添加组件内守卫</p>
<ul>
<li>
<p><code>beforeRouteEnter(to, from) &#123;...&#125;</code> 在渲染该组件的对应路由被 confirm <strong>前</strong>调用</p>
<p>⚠️ 守卫的钩子函数内<strong>不</strong>能访问组件实例 <code>this</code>，因为该守卫在导航确认前被调用，此时即将登场的新组件还没被创建。不过可以通过（可选）第三个参数，传一个回调给其中的 <code>next</code> 函数来访问组件实例</p>
<pre><code class="hljs language-js copyable" lang="js">beforeRouteEnter (to, <span class="hljs-keyword">from</span>, next) &#123;
  <span class="hljs-comment">// 在导航被确认的时候执行 next 的回调，并且把组件实例作为回调方法的参数</span>
  next(<span class="hljs-function"><span class="hljs-params">vm</span> =></span> &#123;
    <span class="hljs-comment">// 通过 `vm` 访问组件实例</span>
  &#125;)
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
<li>
<p><code>beforeRouteUpdate(to, from) &#123;...&#125;</code> 在当前路由改变但是该<strong>组件被复用时</strong>调用，一般用于在路由的路径参数 <code>params</code> 或查询参数 <code>query</code> 改变时做出响应。</p>
<p>例如对于动态路径 <code>/users/:id</code>，当用户在 <code>/users/1</code> 和 <code>/users/2</code> 之间跳转的时候，这个钩子会被调用，由于在这种情况下组件已经挂载好了，导航守卫<strong>可以</strong>访问组件实例 <code>this</code></p>
</li>
<li>
<p><code>beforeRouteLeave(to, from) &#123;...&#125;</code> 导航离开该组件的对应路由时调用。</p>
<p>离开守卫通常用来<strong>禁止用户在还未保存修改前突然离开</strong>，可以通过返回 <code>false</code> 来取消导航。</p>
<pre><code class="hljs language-js copyable" lang="js">beforeRouteLeave (to, <span class="hljs-keyword">from</span>) &#123;
  <span class="hljs-keyword">const</span> answer = <span class="hljs-built_in">window</span>.confirm(<span class="hljs-string">'Really want to leave? you have unsaved changes!'</span>)
  <span class="hljs-keyword">if</span> (!answer) <span class="hljs-keyword">return</span> <span class="hljs-literal">false</span>
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
</ul>
<h4 data-id="heading-46">组合式 API</h4>
<p>🎉 <em>Vue Router 将<strong>更新</strong>和<strong>离开</strong>守卫作为组合式 API 函数公开</em>，可以在组件的选项 <code>setup</code> 函数中使用以下方法定义组件内守卫：</p>
<ul>
<li><code>onBeforeTouteUpdata</code></li>
<li><code>onBeforeRouteLeave</code></li>
</ul>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">import</span> &#123; onBeforeRouteLeave, onBeforeRouteUpdate &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'vue-router'</span>

<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> &#123;
  <span class="hljs-function"><span class="hljs-title">setup</span>(<span class="hljs-params"></span>)</span> &#123;
    <span class="hljs-comment">// 与 beforeRouteLeave 相同，无法访问 `this`</span>
    onBeforeRouteLeave(<span class="hljs-function">(<span class="hljs-params">to, <span class="hljs-keyword">from</span></span>) =></span> &#123;
      <span class="hljs-keyword">const</span> answer = <span class="hljs-built_in">window</span>.confirm(
        <span class="hljs-string">'Do you really want to leave? you have unsaved changes!'</span>
      )
      <span class="hljs-comment">// 取消导航并停留在同一页面上</span>
      <span class="hljs-keyword">if</span> (!answer) <span class="hljs-keyword">return</span> <span class="hljs-literal">false</span>
    &#125;)

    <span class="hljs-keyword">const</span> userData = ref()

    <span class="hljs-comment">// 与 beforeRouteLeave 相同，无法访问 `this`</span>
    onBeforeRouteUpdate(<span class="hljs-keyword">async</span> (to, <span class="hljs-keyword">from</span>) => &#123;
      <span class="hljs-comment">//仅当 id 更改时才获取用户，例如仅 query 或 hash 值已更改</span>
      <span class="hljs-keyword">if</span> (to.params.id !== <span class="hljs-keyword">from</span>.params.id) &#123;
        userData.value = <span class="hljs-keyword">await</span> fetchUser(to.params.id)
      &#125;
    &#125;)
  &#125;,
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>💡 组件内守卫的组合式 API 可以用在任何由 <code><router-view></code> 渲染的组件中，它们不必像选项式 API 那样直接用在路由组件上。</p>
<h3 data-id="heading-47">数据获取</h3>
<p>在访问网页需要从服务器获取数据，一般有两种时机可以选择：</p>
<ul>
<li>在导航完成之后：先完成导航，然后在接下来的<strong>组件生命周期钩子函数中</strong>，如 <code>created</code> 钩子，获取数据。在数据获取期间显示 Loading 之类的指示。这个时机一般是获取页面数据。</li>
<li>在导航完成之前：导航完成前，在路由进入的<strong>守卫钩子函数中</strong>获取数据，在数据获取成功后执行导航。在获取数据时会停止跳转，<strong>用户会停留在当前的界面，有种「卡住」的感觉</strong>，因此建议在数据获取期间，显示一些进度条或者别的指示。这个时机一般是<strong>基于验证、会员</strong>内容的数据获取。</li>
</ul>
<p>⚠️ 使用组件的生命周期的 hook 或路由守卫时应该考虑 Vue 对于<strong>组件的复用</strong>，如果使用组件的生命周期钩子函数获取数据时，应该添加 <code>watch</code> 侦听路由 <code>$route</code> 的变换，手动触发重新获取数据；如果使用路由守卫的钩子函数，则可以在组件内守卫的 <code>beforeRouteUpdate</code> 钩子函数中获取数据，这样即使组件复用也可以顺利更新数据。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> &#123;
  <span class="hljs-function"><span class="hljs-title">data</span>(<span class="hljs-params"></span>)</span> &#123;
    <span class="hljs-keyword">return</span> &#123;
      <span class="hljs-comment">// ...</span>
    &#125;
  &#125;,
  <span class="hljs-function"><span class="hljs-title">created</span>(<span class="hljs-params"></span>)</span> &#123;
    <span class="hljs-comment">// watch 路由的参数，以便再次获取数据</span>
    <span class="hljs-built_in">this</span>.$watch(
      <span class="hljs-function">() =></span> <span class="hljs-built_in">this</span>.$route.params,
      <span class="hljs-function">() =></span> &#123;
        <span class="hljs-built_in">this</span>.fetchData()
      &#125;,
      <span class="hljs-comment">// 组件创建完后获取数据，</span>
      &#123; <span class="hljs-attr">immediate</span>: <span class="hljs-literal">true</span> &#125;
    )
  &#125;,
  <span class="hljs-attr">methods</span>: &#123;
    <span class="hljs-function"><span class="hljs-title">fetchData</span>(<span class="hljs-params"></span>)</span> &#123;
      <span class="hljs-comment">// ...</span>
    &#125;,
  &#125;,
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> &#123;
  <span class="hljs-function"><span class="hljs-title">data</span>(<span class="hljs-params"></span>)</span> &#123;
    <span class="hljs-keyword">return</span> &#123;
      <span class="hljs-comment">// ...</span>
    &#125;
  &#125;,
  <span class="hljs-comment">// 在导航转入新的路由前获取数据</span>
  <span class="hljs-comment">// 通过调用 next 方法访问组件实例，将获取的数据放到 data 选项中，使数据具有响应性</span>
  <span class="hljs-function"><span class="hljs-title">beforeRouteEnter</span>(<span class="hljs-params">to, <span class="hljs-keyword">from</span>, next</span>)</span> &#123;
    getPost(to.params.id, <span class="hljs-function">(<span class="hljs-params">err, post</span>) =></span> &#123;
      next(<span class="hljs-function"><span class="hljs-params">vm</span> =></span> vm.setData(err, post))
    &#125;)
  &#125;,
  <span class="hljs-comment">// 通过 beforeRouteUpdate 守卫可以响应路由的路径参数或查询参数的变化</span>
  <span class="hljs-keyword">async</span> <span class="hljs-function"><span class="hljs-title">beforeRouteUpdate</span>(<span class="hljs-params">to, <span class="hljs-keyword">from</span></span>)</span> &#123;
    <span class="hljs-built_in">this</span>.post = <span class="hljs-literal">null</span>
    <span class="hljs-keyword">try</span> &#123;
      <span class="hljs-built_in">this</span>.post = <span class="hljs-keyword">await</span> getPost(to.params.id)
    &#125; <span class="hljs-keyword">catch</span> (error) &#123;
      <span class="hljs-built_in">this</span>.error = error.toString()
    &#125;
  &#125;,
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-48">过渡效果</h2>
<p>可以用 <code><transition></code> 组件给所有路由组件 <code><router-view></code> 添加过渡效果，这样在路由切换时，组件就可以有相应的进入/离开的动效，</p>
<p>🎉 <em>但在 Vue Router Next 中 <code><transition></code> 组件需要在 <code><router-view></code> 的插槽中，配合 <code><router-view></code> 的作用域插槽 <a href="https://link.juejin.cn/?target=https%3A%2F%2Fnext.router.vuejs.org%2Fapi%2Findex.html%23route" target="_blank" rel="nofollow noopener noreferrer" title="https://next.router.vuejs.org/api/index.html#route" ref="nofollow noopener noreferrer"><code>v-slot</code> 暴露的参数</a>使用：</em></p>
<ul>
<li><code>Component</code>: VNodes 一般用以传递给组件 <code><component></code> 的 <code>is</code> 属性，用以动态切换路由组件</li>
<li><code>route</code>: 解析出的路由地址</li>
</ul>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">router-view</span> <span class="hljs-attr">v-slot</span>=<span class="hljs-string">"&#123; Component, route &#125;"</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">transition</span> <span class="hljs-attr">:name</span>=<span class="hljs-string">"route.meta.transition || 'fade'"</span> <span class="hljs-attr">mode</span>=<span class="hljs-string">"out-in"</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">keep-alive</span>></span>
      <span class="hljs-tag"><<span class="hljs-name">component</span>
        <span class="hljs-attr">:is</span>=<span class="hljs-string">"Component"</span>
        <span class="hljs-attr">:key</span>=<span class="hljs-string">"route.meta.usePathKey ? route.path : undefined"</span>
      /></span>
    <span class="hljs-tag"></<span class="hljs-name">keep-alive</span>></span>
   <span class="hljs-tag"></<span class="hljs-name">transition</span>></span>
<span class="hljs-tag"></<span class="hljs-name">router-view</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>💡 如果你想让每个路由的组件有不同的过渡，可以在路由的元信息中添加一些与过渡相关的字段，然后通过 <code><router-view></code> 的作用域插槽 <code>v-slot</code> 暴露的对象的属性 <code>route.meta</code> 获取，并在 <code><transition></code> 组件的属性 <code>name</code> 绑定</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> routes = [
  &#123;
    <span class="hljs-attr">path</span>: <span class="hljs-string">'/custom-transition'</span>,
    <span class="hljs-attr">component</span>: PanelLeft,
    <span class="hljs-attr">meta</span>: &#123; <span class="hljs-attr">transition</span>: <span class="hljs-string">'slide-left'</span> &#125;,
  &#125;,
  &#123;
    <span class="hljs-attr">path</span>: <span class="hljs-string">'/other-transition'</span>,
    <span class="hljs-attr">component</span>: PanelRight,
    <span class="hljs-attr">meta</span>: &#123; <span class="hljs-attr">transition</span>: <span class="hljs-string">'slide-right'</span> &#125;,
  &#125;,
]
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">router-view</span> <span class="hljs-attr">v-slot</span>=<span class="hljs-string">"&#123; Component, route &#125;"</span>></span>
  <span class="hljs-comment"><!-- 使用任何自定义过渡和回退到 `fade` --></span>
  <span class="hljs-tag"><<span class="hljs-name">transition</span> <span class="hljs-attr">:name</span>=<span class="hljs-string">"route.meta.transition || 'fade'"</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">component</span> <span class="hljs-attr">:is</span>=<span class="hljs-string">"Component"</span> /></span>
  <span class="hljs-tag"></<span class="hljs-name">transition</span>></span>
<span class="hljs-tag"></<span class="hljs-name">router-view</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>也可以基于路由层级关系采用不同的过渡效果</p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-comment"><!-- 使用动态过渡名称 --></span>
<span class="hljs-tag"><<span class="hljs-name">router-view</span> <span class="hljs-attr">v-slot</span>=<span class="hljs-string">"&#123; Component, route &#125;"</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">transition</span> <span class="hljs-attr">:name</span>=<span class="hljs-string">"route.meta.transition"</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">component</span> <span class="hljs-attr">:is</span>=<span class="hljs-string">"Component"</span> /></span>
  <span class="hljs-tag"></<span class="hljs-name">transition</span>></span>
<span class="hljs-tag"></<span class="hljs-name">router-view</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// 使用全局后置钩子，根据路径的深度动态添加信息到 meta 字段</span>
router.afterEach(<span class="hljs-function">(<span class="hljs-params">to, <span class="hljs-keyword">from</span></span>) =></span> &#123;
  <span class="hljs-keyword">const</span> toDepth = to.path.split(<span class="hljs-string">'/'</span>).length
  <span class="hljs-keyword">const</span> fromDepth = <span class="hljs-keyword">from</span>.path.split(<span class="hljs-string">'/'</span>).length
  to.meta.transitionName = toDepth < fromDepth ? <span class="hljs-string">'slide-right'</span> : <span class="hljs-string">'slide-left'</span>
&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>💡 如果动画效果不生效，一般是由于 Vue 对<strong>组件进行复用</strong>，可以将 <code>$route</code> 相关信息，如 <code>$route.path</code> 或 <code>$route.fullPath</code> 作为 <code><router-view></code> 组件的 <code>key</code> 属性值</p>
<h2 data-id="heading-49">组合式 API</h2>
<h3 data-id="heading-50">访问路由和当前路由</h3>
<p>使用组合式 API 开发时，在组件的选项 <code>setup</code> 函数中无法访问组件实例 <code>this</code>，🎉 <em>因此 Vue Router 提供 <code>useRouter()</code> 函数和 <code>useRoute()</code> 函数</em>，以分别替代 <code>this.$router</code> 和 <code>this.$route</code>，访问路由实例和当前路由对象</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">import</span> &#123; useRouter, useRoute &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'vue-router'</span>

<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> &#123;
  <span class="hljs-function"><span class="hljs-title">setup</span>(<span class="hljs-params"></span>)</span> &#123;
    <span class="hljs-keyword">const</span> router = useRouter()
    <span class="hljs-keyword">const</span> route = useRoute()

    <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">pushWithQuery</span>(<span class="hljs-params">query</span>) </span>&#123;
      router.push(&#123;
        <span class="hljs-attr">name</span>: <span class="hljs-string">'search'</span>,
        <span class="hljs-attr">query</span>: &#123;
          ...route.query,
        &#125;,
      &#125;)
    &#125;
  &#125;,
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>💡 在模板中仍然可以访问 <code>$router</code> 和 <code>$route</code>，不需要在 <code>setup</code> 中返回 <code>router</code> 或 <code>route</code>。</p>
<p>路由对象是一个响应式对象，所以它的任何属性都可以被监听，但应该<strong>避免</strong>监听整个 <code>route</code> 对象</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">import</span> &#123; useRoute &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'vue-router'</span>

<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> &#123;
  <span class="hljs-function"><span class="hljs-title">setup</span>(<span class="hljs-params"></span>)</span> &#123;
    <span class="hljs-keyword">const</span> route = useRoute()
    <span class="hljs-keyword">const</span> userData = ref()

    <span class="hljs-comment">// 监听路径参数，更改时获取用户信息</span>
    watch(
      <span class="hljs-function">() =></span> route.params,
      <span class="hljs-keyword">async</span> newParams => &#123;
        userData.value = <span class="hljs-keyword">await</span> fetchUser(newParams.id)
      &#125;
    )
  &#125;,
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-51">导航守卫</h3>
<p>此外为了可以在组合式 API 中设置组件内守卫，🎉 <em>Vue Router 将更新守卫 <code>onBeforeTouteUpdata</code> 和离开守卫 <code>onBeforeRouteLeave</code> 作为组合式 API 函数公开</em></p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">import</span> &#123; onBeforeRouteLeave, onBeforeRouteUpdate &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'vue-router'</span>

<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> &#123;
  <span class="hljs-function"><span class="hljs-title">setup</span>(<span class="hljs-params"></span>)</span> &#123;
    <span class="hljs-comment">// 与 beforeRouteLeave 相同，但无法访问 `this`</span>
    onBeforeRouteLeave(<span class="hljs-function">(<span class="hljs-params">to, <span class="hljs-keyword">from</span></span>) =></span> &#123;
      <span class="hljs-keyword">const</span> answer = <span class="hljs-built_in">window</span>.confirm(
        <span class="hljs-string">'Do you really want to leave? you have unsaved changes!'</span>
      )
      <span class="hljs-comment">// 取消导航并停留在同一页面上</span>
      <span class="hljs-keyword">if</span> (!answer) <span class="hljs-keyword">return</span> <span class="hljs-literal">false</span>
    &#125;)

    <span class="hljs-keyword">const</span> userData = ref()

    <span class="hljs-comment">// 与 onBeforeRouteUpdate 相同，但无法访问 `this`</span>
    onBeforeRouteUpdate(<span class="hljs-keyword">async</span> (to, <span class="hljs-keyword">from</span>) => &#123;
      <span class="hljs-comment">//仅当 id 更改时才获取用户，例如仅 query 或 hash 值已更改</span>
      <span class="hljs-keyword">if</span> (to.params.id !== <span class="hljs-keyword">from</span>.params.id) &#123;
        userData.value = <span class="hljs-keyword">await</span> fetchUser(to.params.id)
      &#125;
    &#125;)
  &#125;,
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>💡 组合式 API 守卫也可以用在任何由 <code><router-view></code> 渲染的组件中，它们不必像组件内守卫那样直接用在路由组件上。</p>
<h3 data-id="heading-52">扩展 RouterLink</h3>
<p>Vue Router 提供的组件 <code><router-link></code> 通过<a href="https://link.juejin.cn/?target=https%3A%2F%2Fnext.router.vuejs.org%2Fapi%2Findex.html%23router-link-s-v-slot" target="_blank" rel="nofollow noopener noreferrer" title="https://next.router.vuejs.org/api/index.html#router-link-s-v-slot" ref="nofollow noopener noreferrer">作用域插槽 <code>v-slot</code> 提供了大量的 API</a>（<code>route</code>、<code>href</code>、<code>isActive</code>、<code>isExactActive</code>、<code>navigate</code>），但未能涵盖所有的需求，我们能够借助组合式 API <code>useLink</code> （RouterLink 的内部行为作为一个组合式 API 函数公开）来扩展定制一个 <code><cutom-router-link></code> 组件</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">import</span> &#123; RouterLink, useLink &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'vue-router'</span>

<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> &#123;
  <span class="hljs-attr">name</span>: <span class="hljs-string">'AppLink'</span>,

  <span class="hljs-attr">props</span>: &#123;
    <span class="hljs-comment">// 如果使用 TypeScript，请添加 @ts-ignore</span>
    ...RouterLink.props,
    <span class="hljs-attr">inactiveClass</span>: <span class="hljs-built_in">String</span>,
  &#125;,

  <span class="hljs-function"><span class="hljs-title">setup</span>(<span class="hljs-params">props</span>)</span> &#123;
    <span class="hljs-keyword">const</span> &#123; route, href, isActive, isExactActive, navigate &#125; = useLink(props)
    <span class="hljs-comment">// 添加 isExternalLink 属性，以判断链接是否指向外部，结合 CSS 可以在页面实现外部链接和内部链接的的不同样式显式</span>
    <span class="hljs-keyword">const</span> isExternalLink = computed(
      <span class="hljs-function">() =></span> <span class="hljs-keyword">typeof</span> props.to === <span class="hljs-string">'string'</span> && props.to.startsWith(<span class="hljs-string">'http'</span>)
    )

    <span class="hljs-keyword">return</span> &#123; isExternalLink, href, navigate, isActive &#125;
  &#125;,
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>💡 在大多数中型到大型应用程序中，值得创建一个自定义 RouterLink 组件，以在整个应用程序中重用它们，例如导航菜单中的链接，添加外部链接提示和 <code>inactive-class</code> 等，具体例子可以参考<a href="https://link.juejin.cn/?target=https%3A%2F%2Fnext.router.vuejs.org%2Fzh%2Fguide%2Fadvanced%2Fextending-router-link.html" target="_blank" rel="nofollow noopener noreferrer" title="https://next.router.vuejs.org/zh/guide/advanced/extending-router-link.html" ref="nofollow noopener noreferrer">官方文档</a>。</p>
<h2 data-id="heading-53">路由组件传参</h2>
<p>以 props 方式将路由信息传递给组件，<strong>将组件与路由解耦合</strong>，让组件可以更通用。</p>
<p>为了组件更通用，不应该在组件的模板中使用 <code>$route</code> 直接读取当前路由信息，但是组件中又确实需要使用路由相关的数据时，可以<strong>将路由信息作为 props 传递给组件，记得在组件内要设置相应的 props 接收传进来的数据</strong>。</p>
<p>有三种方法将路由信息（或其他数据）作为 props 传递给组件</p>
<ul>
<li>布尔模式</li>
<li>对象模式</li>
<li>函数模式</li>
</ul>
<h3 data-id="heading-54">布尔模式</h3>
<p>在设置路由时，如果将选项 <code>props</code> 设置为 <code>true</code>，则动态路由的<strong>路径参数 <code>route.params</code> 将会被设置为组件 props 属性</strong></p>
<p>⚠️ 通过选项 <code>props</code> 简单地开启传参，并不能传递路径的完整信息，如查询参数 <code>route.query</code></p>
<p>💡 对于包含多个组件的路由（对应多个命名视图），如果希望这些组件都与路由解耦，而在组件中还可以使用路由相关信息，必须<strong>分别为每个命名视图「开启」属性 <code>props</code></strong></p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> User = &#123;
  <span class="hljs-comment">// 组件设置 props 接收路由传递进来的数据</span>
  <span class="hljs-attr">props</span>: [<span class="hljs-string">'id'</span>],
  <span class="hljs-attr">template</span>: <span class="hljs-string">'<div>User &#123;&#123; id &#125;&#125;</div>'</span>
&#125;

<span class="hljs-keyword">const</span> router = <span class="hljs-keyword">new</span> VueRouter(&#123;
  <span class="hljs-attr">routes</span>: [
    &#123; 
      <span class="hljs-attr">path</span>: <span class="hljs-string">'/user/:id'</span>,
      <span class="hljs-attr">component</span>: User, 
      <span class="hljs-attr">props</span>: <span class="hljs-literal">true</span>
    &#125;,
    <span class="hljs-comment">// 对于包含命名视图的路由，你必须分别为每个命名视图添加 `props` 选项</span>
    &#123;
      <span class="hljs-attr">path</span>: <span class="hljs-string">'/user/:id'</span>,
      <span class="hljs-attr">components</span>: &#123; 
        <span class="hljs-attr">default</span>: User,
        <span class="hljs-attr">sidebar</span>: Sidebar
      &#125;,
      <span class="hljs-attr">props</span>: &#123; 
        <span class="hljs-attr">default</span>: <span class="hljs-literal">true</span>,
        <span class="hljs-attr">sidebar</span>: <span class="hljs-literal">false</span>
      &#125;
    &#125;
  ]
&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-55">对象模式</h3>
<p>在设置路由时，如果将选项 <code>props</code> 设置为一个对象，它会被作为<strong>静态值</strong>，按原样传递给组件。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// 路由设置</span>
<span class="hljs-keyword">const</span> routes = [
  &#123;
    <span class="hljs-attr">path</span>: <span class="hljs-string">'/promotion/from-newsletter'</span>,
    <span class="hljs-attr">component</span>: Promotion,
    <span class="hljs-comment">// 对象模式</span>
    <span class="hljs-attr">props</span>: &#123; <span class="hljs-attr">newsletterPopup</span>: <span class="hljs-literal">false</span> &#125;
  &#125;
]
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-56">函数模式</h3>
<p>在设置路由时，如果将选项 <code>props</code> 设置为一个函数，则<strong>传递给组件的数据就是函数的返回值</strong>。该函数可以接收路由对象 <code>route</code> 作为参数，这样就可以<strong>获取相应路由的数据</strong></p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// 路由设置</span>
<span class="hljs-keyword">const</span> routes = [
  &#123;
    <span class="hljs-attr">path</span>: <span class="hljs-string">'/search'</span>,
    <span class="hljs-attr">component</span>: SearchUser,
    <span class="hljs-attr">props</span>: <span class="hljs-function"><span class="hljs-params">route</span> =></span> (&#123; <span class="hljs-attr">query</span>: route.query.q &#125;)
  &#125;
]
<span class="copy-code-btn">复制代码</span></code></pre>
<p>以上示例在用户访问路由 <code>/search?q=ben</code> 时，则相关的数据就会传递给组件 <code>SearchUser</code> ，该组件获得的 prop 就是 <code>&#123;query: 'ben'&#125;</code>，因此在组件中需要先预设 prop <code>query</code> 以接收数据。</p></div>  
</div>
            