
---
title: '_ Vue _ 通过使用 vue-loader 梳理通用知识点'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/3b8f4892dd1d4b07b8e7d920bd6985e2~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Sun, 18 Jul 2021 18:14:41 GMT
thumbnail: 'https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/3b8f4892dd1d4b07b8e7d920bd6985e2~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h2 data-id="heading-0">Vue Router 的作用</h2>
<h3 data-id="heading-1">实现基本的组件之间的路由</h3>
<p>vue 是 Vue Router 是 Vuejs 官方的路由器，他和 Vue.js 深度集成，是用于单页应用中组件之间的导航，本质上就是通过 components 和 router 进行映射绑定，使用 router-link 传入指定的组件地址，通过 router-view 渲染已经和组件地址绑定好的组件。</p>
<pre><code class="hljs language-vue copyable" lang="vue"><template>
  <div>
    <router-link to="/index/login">login</router-link>
    <router-link to="/index/search">search</router-link>
    <router-view></router-view>
  </div>
</template>
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/3b8f4892dd1d4b07b8e7d920bd6985e2~tplv-k3u1fbpfcp-watermark.image" alt="vue3-router-1.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-2">Vue Router 的开发要点</h2>
<h3 data-id="heading-3">多层级嵌套路由</h3>
<p>再实际的项目的开发中，肯定是有多层级的页面。配置多层级的路由就是给上一级路由增加 children 在参数，在 children 添加新的路由信息</p>
<pre><code class="hljs language-javascript copyable" lang="javascript">  routes: [
  &#123; 
    <span class="hljs-attr">path</span>: <span class="hljs-string">"/index"</span>, 
    <span class="hljs-attr">component</span>: renderView,
    <span class="hljs-attr">children</span>: [
      &#123;
        <span class="hljs-attr">path</span>: <span class="hljs-string">"index"</span>,
        <span class="hljs-attr">name</span>: <span class="hljs-string">"name"</span>,
        <span class="hljs-attr">component</span>: Index,
        <span class="hljs-attr">children</span>:[
          &#123; 
            <span class="hljs-attr">path</span>: <span class="hljs-string">"product"</span>,
          <span class="hljs-attr">name</span>: <span class="hljs-string">"product"</span>,
          <span class="hljs-attr">component</span>: Product,
          &#125;
        ]
      &#125;,
      &#123;
        <span class="hljs-attr">path</span>: <span class="hljs-string">"login/:user/comic/:age"</span>,
        <span class="hljs-attr">name</span>: <span class="hljs-string">"name"</span>,
        <span class="hljs-attr">component</span>: Login,
      &#125;,
      &#123;
        <span class="hljs-attr">path</span>: <span class="hljs-string">"search"</span>,
        <span class="hljs-attr">name</span>: <span class="hljs-string">"search"</span>,
        <span class="hljs-attr">component</span>: Search,
      &#125;,
      &#123;
        <span class="hljs-attr">path</span>: <span class="hljs-string">"*"</span>,
        <span class="hljs-attr">name</span>: <span class="hljs-string">"rank"</span>,
        <span class="hljs-attr">component</span>: Rank,
      &#125;,
    ],
  &#125;,
],
<span class="copy-code-btn">复制代码</span></code></pre>
<p>一个路由就是一个 Object ，如果有下一层级，就在里面加上一个 children 数组。</p>
<h3 data-id="heading-4">获取 URL 参数和配置默认路由地址</h3>
<p>获取 URL 的参数是 router 的 path 里面加上 ： 号，用来区分是一个动态的参数。在 render 组件的时候，执行 this.$route.params 就可以获取到动态传递的参数。</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">// router.js</span>
&#123;
  <span class="hljs-attr">path</span>: <span class="hljs-string">"comic/:id/chapter/:id"</span>,
  <span class="hljs-attr">name</span>: <span class="hljs-string">"name"</span>,
  <span class="hljs-attr">component</span>: Comic,
&#125;,

<span class="hljs-comment">// component.vue</span>
<span class="hljs-built_in">console</span>.log(<span class="hljs-built_in">this</span>.$route.params);
<span class="hljs-comment">//&#123; comic:123, chapter:456 &#125;</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>而默认路由地址，这个一般会是设置成主页或者 404 的情况，就是在找不到 URL 的地址是映射到什么组件的情况下，跳转到 404 页面或者是统一跳转到首页。一般情况下，是会跳转到 404 。然后把这个配置的映射放在了 router 的最后一项。</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">// router.js</span>
......
&#123;
  <span class="hljs-attr">path</span>: <span class="hljs-string">"search"</span>,
  <span class="hljs-attr">name</span>: <span class="hljs-string">"search"</span>,
  <span class="hljs-attr">component</span>: Search,
&#125;,
&#123;
  <span class="hljs-attr">path</span>: <span class="hljs-string">"*"</span>,
  <span class="hljs-attr">name</span>: <span class="hljs-string">"rank"</span>,
  <span class="hljs-attr">component</span>: Rank,
&#125;,
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-5">JavaScript 执行路由跳转</h3>
<p>JavaScript 执行路由跳转这个是我自己的说法，官网给出的说法是叫作<strong>编程式路由</strong> 。一开始看到这个词逼格很高，但看完解释就是代码操作路由跳转。最后，还是按我自己的理解来把这个标题定为 JavaScript 执行路由跳转。在 Vue Router 中，有两种执行路由跳转的方式，第一种是声明式，第二种是编程式。</p>
<p>声明式：</p>
<pre><code class="hljs language-vue copyable" lang="vue"><router-link to="/index/login">login</router-link>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>通过 router-link 标签执行指定跳转。</p>
<p>编程式：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">// vue </span>
<span class="hljs-built_in">this</span>.$router.push()
<span class="hljs-built_in">this</span>.router.push(&#123; <span class="hljs-attr">name</span>: <span class="hljs-string">'user'</span>, <span class="hljs-attr">params</span>: &#123; userId &#125;&#125;) <span class="hljs-comment">// -> /user/123</span>
<span class="hljs-built_in">this</span>.router.push(&#123; <span class="hljs-attr">path</span>: <span class="hljs-string">`/user/<span class="hljs-subst">$&#123;userId&#125;</span>`</span> &#125;) <span class="hljs-comment">// -> /user/123</span>

<span class="hljs-comment">// router </span>
router.push(...);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>在 vue 实例中，可以通过 <span class="math math-inline"><span class="katex"><span class="katex-mathml"><math xmlns="http://www.w3.org/1998/Math/MathML"><semantics><mrow><mi>r</mi><mi>o</mi><mi>u</mi><mi>t</mi><mi>e</mi><mi>r</mi><mtext>访问路由，可以直接使用</mtext><mi>t</mi><mi>h</mi><mi>i</mi><mi>s</mi><mi mathvariant="normal">.</mi></mrow><annotation encoding="application/x-tex">router 访问路由，可以直接使用 this.</annotation></semantics></math></span><span class="katex-html" aria-hidden="true"><span class="base"><span class="strut" style="height:0.69444em;vertical-align:0em;"></span><span class="mord mathnormal" style="margin-right:0.02778em;">r</span><span class="mord mathnormal">o</span><span class="mord mathnormal">u</span><span class="mord mathnormal">t</span><span class="mord mathnormal">e</span><span class="mord mathnormal" style="margin-right:0.02778em;">r</span><span class="mord cjk_fallback">访</span><span class="mord cjk_fallback">问</span><span class="mord cjk_fallback">路</span><span class="mord cjk_fallback">由</span><span class="mord cjk_fallback">，</span><span class="mord cjk_fallback">可</span><span class="mord cjk_fallback">以</span><span class="mord cjk_fallback">直</span><span class="mord cjk_fallback">接</span><span class="mord cjk_fallback">使</span><span class="mord cjk_fallback">用</span><span class="mord mathnormal">t</span><span class="mord mathnormal">h</span><span class="mord mathnormal">i</span><span class="mord mathnormal">s</span><span class="mord">.</span></span></span></span></span>router.push() 进行操作。在使用的时候需要注意的一点就是，当有 path 的时候， params 会被忽略。所以需要像上面一样以字符串形式拼接 URL。</p>
<p>与 router.push 相似的还有 router.replace，他们之间唯一不同的地方就是， router.replace 会替换掉当前的历史记录。这个和 location.href 和 location.replace 是类似的。而官网最后也提到了，router.push、 router.replace 和 router.go 跟 window.history.pushState、 window.history.replaceState 和 window.history.go (opens new window)好像， 实际上它们确实是效仿 window.history API 的。</p>
<h3 data-id="heading-6">路由名称和多视图展示</h3>
<p>路由命名只需要在 router 中在 path 同级下增加一个 name，之后使用 router.path ( name: index ,..)
即可。</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">// set</span>
  <span class="hljs-attr">routes</span>: [
    &#123;
      <span class="hljs-attr">path</span>: <span class="hljs-string">'/index/:Id'</span>,
      <span class="hljs-attr">name</span>: <span class="hljs-string">'index'</span>,
      <span class="hljs-attr">component</span>: Index
    &#125;
  ]
  <span class="hljs-comment">// link</span>
  router.push(&#123; <span class="hljs-attr">name</span>: <span class="hljs-string">'index'</span>, <span class="hljs-attr">params</span>: &#123; <span class="hljs-attr">Id</span>: <span class="hljs-number">123</span> &#125; &#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>多视图展示 ，实质上就是增加 router-view 的标签，再通过 router 的 component 增加视图的名称。</p>
<pre><code class="hljs language-vue copyable" lang="vue"><div>
  <router-view class="one" name="one"></router-view>
  <router-view class="two" name="two"></router-view>
</div>
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="hljs language-javascript copyable" lang="javascript">  routes: [
    &#123;
      <span class="hljs-attr">path</span>: <span class="hljs-string">'/'</span>,
      <span class="hljs-attr">components</span>: &#123;
        <span class="hljs-attr">default</span>: Index,
        <span class="hljs-attr">one</span>: Search,
        <span class="hljs-attr">two</span>: Details,
      &#125;
    &#125;
  ]
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/b6a5d8e0f0304f3cb2fe8a8e9fdd713b~tplv-k3u1fbpfcp-watermark.image" alt="vue3-router-2.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-7">重定向 URL</h3>
<p>使用 redirect 参数，对 URL 进行替换 ， 重定向的场景一般适用于兼容的情况下，比如项目改造升级，原有的 URL 如果希望保持不变，那么就可以用重定向指向新的 URL 。</p>
<pre><code class="hljs language-javascript copyable" lang="javascript">  routes: [
    &#123; <span class="hljs-attr">path</span>: <span class="hljs-string">'/index'</span>, <span class="hljs-attr">redirect</span>: <span class="hljs-string">'/index/index'</span> &#125;
  ]
<span class="copy-code-btn">复制代码</span></code></pre>
<p>还有一个方法是叫别名，但是这个一般我没有使用，总感觉这样的方法会留下一些潜规则，所以一直不会使用这个方法，他的原理就是 URL 不变，但却走了另一个映射。</p>
<h3 data-id="heading-8">路由组件传参</h3>
<p>在组件中使用 $route 会使之与其对应路由形成高度耦合，从而使组件只能在某些特定的 URL 上使用，限制了其灵活性。</p>
<p>以对象模式通过 props 进行解耦</p>
<pre><code class="hljs language-javascript copyable" lang="javascript">  routes: [
    &#123; <span class="hljs-attr">path</span>: <span class="hljs-string">'/user/:id'</span>, <span class="hljs-attr">component</span>: User, <span class="hljs-attr">props</span>: <span class="hljs-literal">true</span> &#125;,
    &#123;
      <span class="hljs-attr">path</span>: <span class="hljs-string">'/user/:id'</span>,
      <span class="hljs-attr">components</span>: &#123; <span class="hljs-attr">default</span>: User, <span class="hljs-attr">sidebar</span>: Sidebar &#125;,
      <span class="hljs-attr">props</span>: &#123; <span class="hljs-attr">default</span>: <span class="hljs-literal">true</span>, <span class="hljs-attr">sidebar</span>: <span class="hljs-literal">false</span> &#125;
    &#125;
  ]
<span class="copy-code-btn">复制代码</span></code></pre>
<p>以函数模式</p>
<pre><code class="hljs language-javascript copyable" lang="javascript">routes: [
    &#123;
      <span class="hljs-attr">path</span>: <span class="hljs-string">'/search'</span>,
      <span class="hljs-attr">component</span>: Search,
      <span class="hljs-attr">props</span>: <span class="hljs-function"><span class="hljs-params">route</span> =></span> (&#123; <span class="hljs-attr">query</span>: route.query.name &#125;)
    &#125;
  ]
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-9">vue-router 钩子函数</h3>
<p>vue-router 的钩子函数也叫导航守卫。这里有三种守卫类型，第一种是全局前置守卫</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">const</span> router = <span class="hljs-keyword">new</span> VueRouter(&#123; ... &#125;)
router.beforeEach(<span class="hljs-function">(<span class="hljs-params">to, <span class="hljs-keyword">from</span>, next</span>) =></span> &#123;
  <span class="hljs-built_in">console</span>.log(to)
&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>导航在出发的时候它都会执行。这里有一点要注意是，确保 next 函数在任何给定的导航守卫中都被严格调用一次。它可以出现多于一次，但是只能在所有的逻辑路径都不重叠的情况下，否则钩子永远都不会被解析或报错。</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">// BAD</span>
router.beforeEach(<span class="hljs-function">(<span class="hljs-params">to, <span class="hljs-keyword">from</span>, next</span>) =></span> &#123;
  <span class="hljs-keyword">if</span> (to.name !== <span class="hljs-string">'Login'</span> && !isAuthenticated) next(&#123; <span class="hljs-attr">name</span>: <span class="hljs-string">'Login'</span> &#125;)
  <span class="hljs-comment">// 如果用户未能验证身份，则 `next` 会被调用两次</span>
  next()
&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">// GOOD</span>
router.beforeEach(<span class="hljs-function">(<span class="hljs-params">to, <span class="hljs-keyword">from</span>, next</span>) =></span> &#123;
  <span class="hljs-keyword">if</span> (to.name !== <span class="hljs-string">'Login'</span> && !isAuthenticated) next(&#123; <span class="hljs-attr">name</span>: <span class="hljs-string">'Login'</span> &#125;)
  <span class="hljs-keyword">else</span> next()
&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>第二种是全局解析守卫，这个和全局前置守卫差不多，唯一的区别就是在导航确认之前所有的守卫和异步路由组件被解析后执行。</p>
<p>最后一种是全局后置钩子，这个和前面不同的是，这个钩子没有 next 函数体。</p>
<pre><code class="hljs language-javascript copyable" lang="javascript">router.afterEach(<span class="hljs-function">(<span class="hljs-params">to, <span class="hljs-keyword">from</span></span>) =></span> &#123;
  <span class="hljs-built_in">console</span>.log(to)
&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>除了全局守卫之外还有路由独享的路由，他的用法就是在 routes 里面加上 beforeEnter。</p>
<pre><code class="hljs language-javascript copyable" lang="javascript">  routes: [
    &#123;
      <span class="hljs-attr">path</span>: <span class="hljs-string">'/index'</span>,
      <span class="hljs-attr">component</span>: Index,
      <span class="hljs-attr">beforeEnter</span>: <span class="hljs-function">(<span class="hljs-params">to, <span class="hljs-keyword">from</span>, next</span>) =></span> &#123;
        <span class="hljs-comment">// ...</span>
      &#125;
    &#125;
  ]
<span class="copy-code-btn">复制代码</span></code></pre>
<p>还有一个组件内的守卫，他的方法是写在组件里面的。他也有三个方法，后面会有一个具体例子。</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">const</span> Index = &#123;
  <span class="hljs-attr">template</span>: <span class="hljs-string">`...`</span>,
  <span class="hljs-function"><span class="hljs-title">beforeRouteEnter</span>(<span class="hljs-params">to, <span class="hljs-keyword">from</span>, next</span>)</span> &#123;
  &#125;,
  <span class="hljs-function"><span class="hljs-title">beforeRouteUpdate</span>(<span class="hljs-params">to, <span class="hljs-keyword">from</span>, next</span>)</span> &#123;
  &#125;,
  <span class="hljs-function"><span class="hljs-title">beforeRouteLeave</span>(<span class="hljs-params">to, <span class="hljs-keyword">from</span>, next</span>)</span> &#123;
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-10">在导航之前加载数据</h3>
<p>像以往获取数据的方法一般是写在了组件的函数里面，也就是导航完成后，执行数据的拉取。那么，还有另一种方法就是，在导航之前加载数据。</p>
<p>它的原理就是我们在组件的 beforeRouteEnter 守卫中获取数据，当数据获取成功后只调用 next 方法。</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">import</span> &#123; ajax &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'../../js/common/ajax-helper'</span>;
<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> &#123;
  <span class="hljs-function"><span class="hljs-title">data</span>(<span class="hljs-params"></span>)</span> &#123;
    <span class="hljs-keyword">return</span> &#123;
      <span class="hljs-attr">num</span>: <span class="hljs-number">1</span>
    &#125;
  &#125;,
  <span class="hljs-comment">// 方法一</span>
  <span class="hljs-function"><span class="hljs-title">beforeRouteEnter</span>(<span class="hljs-params">to, <span class="hljs-keyword">from</span>, next</span>)</span> &#123;
    <span class="hljs-built_in">console</span>.log(to)
    <span class="hljs-built_in">console</span>.log(<span class="hljs-built_in">window</span>.location.href)
    ajax(to.params.id, <span class="hljs-function">(<span class="hljs-params">err, post</span>) =></span> &#123;
      next(<span class="hljs-function"><span class="hljs-params">vm</span> =></span> vm.setData(err, post))
    &#125;)
  &#125;,
  <span class="hljs-comment">// 方法二</span>
  beforeRouteUpdate (to, <span class="hljs-keyword">from</span>, next) &#123;
    <span class="hljs-built_in">this</span>.post = <span class="hljs-literal">null</span>
    ajax(to.params.id, <span class="hljs-function">(<span class="hljs-params">err, post</span>) =></span> &#123;
    <span class="hljs-built_in">this</span>.setData(err, post)&#125;);
    next();
  &#125;,
  <span class="hljs-attr">methods</span>: &#123;
    <span class="hljs-function"><span class="hljs-title">setData</span>(<span class="hljs-params">err, num</span>)</span>&#123;
      <span class="hljs-built_in">this</span>.num = num;
      <span class="hljs-built_in">console</span>.log(<span class="hljs-built_in">this</span>.num)
    &#125;
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>vm 是当前实例，在进入这个路由之前获取 to.params.id ，发送请求拿到数据之后，通过 next 执行将数据挂载。</p>
<p>方法二是已经到了路由更新之前的阶段，可以直接通过 this 执行组件代码。执行完毕再执行下一步</p>
<h3 data-id="heading-11">路由器 lazyload</h3>
<p>我们需要将不同路由对应的组件分割成不同的模块，然后在路由在被访问的时候才加载对应的组件，这样能够大大降低页面性能的损耗。</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">const</span> Index = <span class="hljs-function">() =></span> 
<span class="hljs-keyword">import</span>(<span class="hljs-comment">/* webpackChunkName: "Index" */</span> <span class="hljs-string">'./Index.vue'</span>);
<span class="hljs-keyword">const</span> Search = <span class="hljs-function">() =></span>
<span class="hljs-keyword">import</span>(<span class="hljs-comment">/* webpackChunkName: "Search" */</span> <span class="hljs-string">'./Search.vue'</span>);
<span class="hljs-keyword">const</span> Details = <span class="hljs-function">() =></span> 
<span class="hljs-keyword">import</span>(<span class="hljs-comment">/* webpackChunkName: "Details" */</span> <span class="hljs-string">'./Details.vue'</span>)

<span class="hljs-keyword">const</span> router = <span class="hljs-keyword">new</span> VueRouter(&#123;
  <span class="hljs-attr">routes</span>: [&#123; <span class="hljs-attr">path</span>: <span class="hljs-string">'/Details'</span>, <span class="hljs-attr">component</span>: Details &#125;]
&#125;);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这里其实也是 vue 和 webpack 结合使用的功能，到了新的 vite 工具可能会使用新的一些方法可以后面再了解下。</p>
<h3 data-id="heading-12">导航报错</h3>
<p>这里引用一段 DEMO 的代码，也是比较简单。</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">import</span> VueRouter <span class="hljs-keyword">from</span> <span class="hljs-string">'vue-router'</span>
<span class="hljs-keyword">const</span> &#123; isNavigationFailure, NavigationFailureType &#125; = VueRouter

router.push(<span class="hljs-string">'/admin'</span>).catch(<span class="hljs-function"><span class="hljs-params">failure</span> =></span> &#123;
  <span class="hljs-keyword">if</span> (isNavigationFailure(failure, NavigationFailureType.redirected)) &#123;
    showToast(<span class="hljs-string">'Login in order to access the admin panel'</span>)
  &#125;
&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-13">结语</h2>
<p>使用 vue-router 最好的方法还是<strong>阅读文档</strong>，若换一个 React 又有属于它的插件，虽说，大致的逻辑不会相差太远，但肯定是另外一套写法。所以，在理解了一个插件的实现功能之后去理解下一个类似的插件就可以带着一些问题去了解它，理解起来就会更容易上手也能对插件之间进行对比和选型。
在下次接触 react 的路由插件可以从这几个点去思考</p>
<ol>
<li>实现基本的组件之间的路由</li>
<li>多层级嵌套路由</li>
<li>获取 URL 参数和配置默认路由地址</li>
<li>JavaScript 执行路由跳转</li>
<li>路由名称和多视图展示</li>
<li>重定向 URL</li>
<li>路由组件传参</li>
<li>钩子函数的使用</li>
</ol></div>  
</div>
            