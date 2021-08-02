
---
title: '跟着来，你也可以手写VueRouter'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/dcc84f0fb8da436d811574d2f0bc9dee~tplv-k3u1fbpfcp-zoom-1.image'
author: 掘金
comments: false
date: Sun, 01 Aug 2021 17:37:05 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/dcc84f0fb8da436d811574d2f0bc9dee~tplv-k3u1fbpfcp-zoom-1.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><blockquote>
<p>声明：本文为掘金社区首发签约文章，未获授权禁止转载。</p>
</blockquote>
<h2 data-id="heading-0">写在前面</h2>
<p>VueRouter，无疑是每个 Vue 开发者时时刻刻都在使用的东西了，但对于它的源码，你了解多少呢？</p>
<p>相信大部分前端说起路由，都可以说出其核心有 <code>hash</code> 和 <code>history</code> 两种模式，<code>hash</code> 模式通过监听 <code>hashchange</code> 事件实现，<code>history</code> 模式通过监听 <code>popstate</code> 事件再使用 <code>pushstate</code> 修改 URL 来实现，你以为这就懂了？还是说你真的以为懂这些就算接触到 VueRouter 精髓了？No，far from it！！！</p>
<p>其实我和大多数人一样，之前根本没把 VueRouter 放在心上，认为这是一个很简单的东西。但当我开始读 VueRouter 源码时，并不是像我想的那样容易。VueRouter源码的整体架构其实很简单，但想读懂细节还是有难度的，各种谜一样的函数分离以及一些细节实现都让我想当无语，于是我就边读源码边照虎画猫，想通过这种方式深度学习，没成想直接淦了两个大夜才到预期目标。</p>
<h2 data-id="heading-1">本文重点</h2>
<p>话不多说，我们看下读完这篇文章你可以学到什么？</p>
<p>介绍了关于 Router 的一些常识，并手写了一个精简版的 VueRouter（大部分核心特性），和绝大多数手撸文章不同的是，这里的代码是完全以源码为标准一步一步实现的，包括整体架构、API等等都是一致的，跟着此文来一遍，除了能彻底搞懂核心源码之外，后期想看源码细节可无缝接入，看起真正的源码可以毫不夸张的说：纵享丝滑！</p>
<h2 data-id="heading-2">阅前提示</h2>
<p>本文基于最新最稳定的 VueRouter V3.5.2 版本，4.0+ 还是 next，所以不在本文讨论范围之内。</p>
<p>源码文章很枯燥也没有多少人看是因为难理解以及没有实践乐趣，So，建议拿出编辑器跟着手敲比较快乐。</p>
<p>关于本文对 VueRouter 的手写实现，主要包括：</p>
<ul>
<li>hash/history模式路由</li>
<li>嵌套路由</li>
<li>router-view/router-link组件</li>
<li><span class="math math-inline"><span class="katex"><span class="katex-mathml"><math xmlns="http://www.w3.org/1998/Math/MathML"><semantics><mrow><mi>r</mi><mi>o</mi><mi>u</mi><mi>t</mi><mi>e</mi><mi>r</mi><mi mathvariant="normal">/</mi></mrow><annotation encoding="application/x-tex">router/</annotation></semantics></math></span><span class="katex-html" aria-hidden="true"><span class="base"><span class="strut" style="height:1em;vertical-align:-0.25em;"></span><span class="mord mathnormal" style="margin-right:0.02778em;">r</span><span class="mord mathnormal">o</span><span class="mord mathnormal">u</span><span class="mord mathnormal">t</span><span class="mord mathnormal">e</span><span class="mord mathnormal" style="margin-right:0.02778em;">r</span><span class="mord">/</span></span></span></span></span>route</li>
<li>push/replace/go/back等方法</li>
<li>addRoute/addRoutes/getRouters</li>
<li>router hook</li>
</ul>
<p>没实现的部分，也会做大致介绍，并且我将一份刚 clone 下来的源码做好了注释，放到了手写源码项目的目录里（文末链接），大家手写完觉得不过瘾想磕细节就可以直接去看源码了，一套组合拳，不错，come on～</p>
<p>开始前，大家可以简单看下整个 VueRouter 对应的三个流程图解，看不懂也关系，有个大致印象即可，文末还会有此图。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/dcc84f0fb8da436d811574d2f0bc9dee~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-3">前端路由实现原理</h2>
<p>前端路由，指由前端监听 URL 改变从而控制页面中组件渲染做到无刷新式页面跳转，用户虽感觉是一组不同的页面，但其实都在一个页面内。想要实现前端路由，我们需要考虑两个点：</p>
<ul>
<li>URL 改变但页面不刷新？</li>
<li>监测 URL 改变？</li>
</ul>
<p>接下来我们分别看看 Hash 和 History 这两种模式是怎么解决的。</p>
<h3 data-id="heading-4">Hash路由简单实现</h3>
<p>Hash 模式其实就是通过改变 URL 中 # 号后面的 hash 值来切换路由，因为在 URL 中 hash 值的改变并不会引起页面刷新，再通过 hashchange 事件来监听 hash 的改变从而控制页面组件渲染，看一个小例子：</p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-meta"><!DOCTYPE <span class="hljs-meta-keyword">html</span>></span>
<span class="hljs-tag"><<span class="hljs-name">html</span> <span class="hljs-attr">lang</span>=<span class="hljs-string">"en"</span>></span>
<span class="hljs-tag"><<span class="hljs-name">body</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">a</span> <span class="hljs-attr">href</span>=<span class="hljs-string">"#/home"</span>></span>home<span class="hljs-tag"></<span class="hljs-name">a</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">a</span> <span class="hljs-attr">href</span>=<span class="hljs-string">"#/about"</span>></span>about<span class="hljs-tag"></<span class="hljs-name">a</span>></span>
  <span class="hljs-comment"><!-- 渲染路由模块 --></span>
  <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">id</span>=<span class="hljs-string">"view"</span>></span><span class="hljs-tag"></<span class="hljs-name">div</span>></span>
<span class="hljs-tag"></<span class="hljs-name">body</span>></span>
<span class="hljs-tag"><<span class="hljs-name">script</span>></span><span class="javascript">
  <span class="hljs-keyword">let</span> view = <span class="hljs-built_in">document</span>.querySelector(<span class="hljs-string">"#view"</span>)

  <span class="hljs-keyword">let</span> cb = <span class="hljs-function">() =></span> &#123;
    <span class="hljs-keyword">let</span> hash = location.hash || <span class="hljs-string">"#/home"</span>;

  &#125;
  <span class="hljs-built_in">window</span>.addEventListener(<span class="hljs-string">"hashchange"</span>, cb)
  <span class="hljs-built_in">window</span>.addEventListener(<span class="hljs-string">"load"</span>, cb)
</span><span class="hljs-tag"></<span class="hljs-name">script</span>></span>
<span class="hljs-tag"></<span class="hljs-name">html</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>如上，通过两个 a 标签来改变路由 hash 值，相当于 <code>router-link</code> 组件，页面中 <code>id=view</code> 的 div 我们可以把它理解为 <code>router-view</code> 组件，页面加载完毕先执行一下 cb 函数为 hash 和路由模块进行初始化赋值，点击 a 标签路由改变后，会被 hashchange 监听到从而触发路由模块更新。</p>
<h3 data-id="heading-5">History路由简单实现</h3>
<p>还有一种不带 # 号的方式，那就是 history，它提供了 pushState 和 replaceState 两个方法，使用这两个方法可以改变 URL 的路径还不会引起页面刷新，同时它也提供了一个 popstate 事件来监控路由改变，但是 popstate 事件并不像 hashchange 那样改变了就会触发。</p>
<ul>
<li>通过浏览器前进后退时改变了 URL 会触发 popstate 事件</li>
<li>js 调用 historyAPI 的 back、go、forward 等方法可以触发该事件</li>
</ul>
<p>来看它怎么实现路由监听：</p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-meta"><!DOCTYPE <span class="hljs-meta-keyword">html</span>></span>
<span class="hljs-tag"><<span class="hljs-name">html</span> <span class="hljs-attr">lang</span>=<span class="hljs-string">"en"</span>></span>
<span class="hljs-tag"><<span class="hljs-name">body</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">a</span> <span class="hljs-attr">href</span>=<span class="hljs-string">'/home'</span>></span>home<span class="hljs-tag"></<span class="hljs-name">a</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">a</span> <span class="hljs-attr">href</span>=<span class="hljs-string">'/about'</span>></span>about<span class="hljs-tag"></<span class="hljs-name">a</span>></span>
  <span class="hljs-comment"><!-- 渲染路由模块 --></span>
  <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">id</span>=<span class="hljs-string">"view"</span>></span><span class="hljs-tag"></<span class="hljs-name">div</span>></span>
<span class="hljs-tag"></<span class="hljs-name">body</span>></span>
<span class="hljs-tag"><<span class="hljs-name">script</span>></span><span class="javascript">
  <span class="hljs-keyword">let</span> view = <span class="hljs-built_in">document</span>.querySelector(<span class="hljs-string">"#view"</span>)

  <span class="hljs-comment">// 路由跳转</span>
  <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">push</span>(<span class="hljs-params">path = <span class="hljs-string">"/home"</span></span>)</span>&#123;
    <span class="hljs-built_in">window</span>.history.pushState(<span class="hljs-literal">null</span>, <span class="hljs-string">''</span>, path)
    update()
  &#125;
  <span class="hljs-comment">// 更新路由模块视图</span>
  <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">update</span>(<span class="hljs-params"></span>)</span>&#123;
    view.innerHTML = location.pathname
  &#125;

  <span class="hljs-built_in">window</span>.addEventListener(<span class="hljs-string">'popstate'</span>, <span class="hljs-function">()=></span>&#123;
    update()
  &#125;)
  <span class="hljs-built_in">window</span>.addEventListener(<span class="hljs-string">'load'</span>, <span class="hljs-function">()=></span>&#123;
    <span class="hljs-keyword">let</span> links = <span class="hljs-built_in">document</span>.querySelectorAll(<span class="hljs-string">'a[href]'</span>)
    links.forEach(<span class="hljs-function"><span class="hljs-params">el</span> =></span> el.addEventListener(<span class="hljs-string">'click'</span>, <span class="hljs-function">(<span class="hljs-params">e</span>) =></span> &#123;
      <span class="hljs-comment">// 阻止a标签默认行为</span>
      e.preventDefault()
      push(el.getAttribute(<span class="hljs-string">'href'</span>))
    &#125;))
    push()
  &#125;)
</span><span class="hljs-tag"></<span class="hljs-name">script</span>></span>
<span class="hljs-tag"></<span class="hljs-name">html</span>></span>

<span class="copy-code-btn">复制代码</span></code></pre>
<p>如上，a 标签为 <code>router-link</code> 组件，div 为 <code>router-view</code> 组件。</p>
<p>由于 popstate 事件只能监听浏览器前进回退和使用 history 前进后退 API，所以除了在事件监听中要做更新操作，还要在跳转时手动做路由模块更新。</p>
<p>这样就可以做到和 hash 一样的效果了，同时由于 a 标签存在默认点击跳转行为，所以我们阻止了此行为。同时我们可以直接在浏览器中改变URL刷新，但在这个例子是不支持的，因为这就需要后端来配合了。</p>
<p>上面就是 hash模式和 history 模式的精简原理了，知道这些基础我们就可以开始写 VueRouter 了</p>
<h2 data-id="heading-6">从使用分析VueRouter</h2>
<p>手写 VueRouter 之前，我们要从它的使用层面分析，看它都有什么，先回顾一下它的使用：</p>
<ul>
<li>路由配置文件中引入 VueRouter 并作为一个插件 use 一下</li>
<li>路由配置文件中配置路由对象生成路由实例并导出</li>
<li>将配置文件导出的 router 实例挂载到 Vue 的根实例上</li>
</ul>
<p>整个步骤如下所示：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// router/index.js</span>
<span class="hljs-keyword">import</span> Vue <span class="hljs-keyword">from</span> <span class="hljs-string">"vue"</span>;
<span class="hljs-keyword">import</span> VueRouter <span class="hljs-keyword">from</span> <span class="hljs-string">"vue-router"</span>;

Vue.use(VueRouter);

<span class="hljs-keyword">const</span> routes = [
  &#123;
    <span class="hljs-attr">path</span>: <span class="hljs-string">"/"</span>,
    <span class="hljs-attr">name</span>: <span class="hljs-string">"Home"</span>,
    component,
  &#125;,
  &#123;
    <span class="hljs-attr">path</span>: <span class="hljs-string">"/about"</span>,
    <span class="hljs-attr">name</span>: <span class="hljs-string">"About"</span>,
    component,
  &#125;
];

<span class="hljs-keyword">const</span> router = <span class="hljs-keyword">new</span> VueRouter(&#123;
  <span class="hljs-attr">mode</span>: <span class="hljs-string">"hash"</span>,
  <span class="hljs-attr">base</span>: process.env.BASE_URL,
  routes,
&#125;);

<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> router;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>在项目 main.js 文件中：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// main.js</span>
<span class="hljs-keyword">import</span> Vue <span class="hljs-keyword">from</span> <span class="hljs-string">"vue"</span>;
<span class="hljs-keyword">import</span> App <span class="hljs-keyword">from</span> <span class="hljs-string">"./App.vue"</span>;
<span class="hljs-keyword">import</span> router <span class="hljs-keyword">from</span> <span class="hljs-string">"./router"</span>;

<span class="hljs-keyword">new</span> Vue(&#123;
  router,
  <span class="hljs-attr">render</span>: <span class="hljs-function">(<span class="hljs-params">h</span>) =></span> h(App),
&#125;).$mount(<span class="hljs-string">"#app"</span>);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>可看出，VueRouter 作为一个类可以被实例化同时它也作为一个 Vue 插件被加载。</p>
<p>实例化好理解，但是为什么要加载插件呢？</p>
<p>我们在使用 VueRouter 时，经常会使用到 <code>router-link</code> 和 <code>router-view</code> 两个组件，这两个组件我们没有发现哪里引入了，有没有想过为什么可以全局使用？其实就是在 VueRouter 作为插件初始化时全局注册的。</p>
<p>在使用过程中，我们可以使用 <code>this.$router</code> 获取路由实例，同时实例上还会有一些像 <code>push/go/back</code> 等方法，还可以通过 <code>this.$route</code> 来获取一个只读的路由对象，其中包括我们当前的路由以及一些参数等。</p>
<h2 data-id="heading-7">手写前的准备</h2>
<h3 data-id="heading-8">项目搭建</h3>
<p>创建一个 Vue 项目，使用终端输入下面命令构建一个 Vue 项目：</p>
<pre><code class="hljs language-bash copyable" lang="bash">vue create hello-vue-router
<span class="copy-code-btn">复制代码</span></code></pre>
<p>注意构建时选上 VueRouter 哦！</p>
<p>构建完成直接 <code>yarn serve</code> 跑起来，如下，一个非常熟悉的界面：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/9c7072301bbd44c6a90e8c87bd4a856c~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>接着我们在 <code>src/</code> 下新建一个文件夹 <code>hello-vue-router/</code> ，此文件夹下就放我们自己写的 VueRouter 代码。</p>
<p>先新建一个 <code>index.js</code> 文件，导出一个空 VueRouter 类：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">/*
 * @path: src/hello-vue-router/index.js
 * @Description: 入口文件 VueRouter类
 */</span>

<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> <span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">VueRouter</span>()</span>&#123;
  <span class="hljs-function"><span class="hljs-title">constructor</span>(<span class="hljs-params">options</span>)</span>&#123;&#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>然后来到路由配置文件 <code>src/router/index.js</code> ，将引入的 VueRouter 换成我们自己的，并将路由模式改为 hash，因为我们要先实现 hash 模式，如下：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">import</span> Vue <span class="hljs-keyword">from</span> <span class="hljs-string">'vue'</span>
<span class="hljs-keyword">import</span> VueRouter <span class="hljs-keyword">from</span> <span class="hljs-string">'@/hello-vue-router/index'</span>
<span class="hljs-comment">// import VueRouter from 'vue-router'</span>
<span class="hljs-keyword">import</span> Home <span class="hljs-keyword">from</span> <span class="hljs-string">'../views/Home.vue'</span>

Vue.use(VueRouter)

<span class="hljs-keyword">const</span> routes = [...]

<span class="hljs-keyword">const</span> router = <span class="hljs-keyword">new</span> VueRouter(&#123;
  <span class="hljs-attr">mode</span>: <span class="hljs-string">'hash'</span>,
  <span class="hljs-attr">base</span>: process.env.BASE_URL,
  routes
&#125;)

<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> router
<span class="copy-code-btn">复制代码</span></code></pre>
<p>那现在页面就变成了空白，并且控制台报着下面的错：</p>
<pre><code class="hljs language-bash copyable" lang="bash">Cannot call a class as a <span class="hljs-keyword">function</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>控制台的错误说不能将 class 作为函数调用！！！</p>
<p>诶，哪里讲 class 作为函数调用了？</p>
<p>其实是 <code>Vue.use(VueRouter)</code> 这，说到这，我们就不得不介绍下这个 Vue 安装插件的 API 了</p>
<h3 data-id="heading-9">Vue.use()源码解析</h3>
<p>如下，其实说白了，这个方法接收一个类型为函数或对象的参数。如果参数是对象，那它就必须有一个 install 属性方法。不论参数是函数还是对象，在执行 install 方法或者函数本身的时候都会把构造函数 Vue 作为第一个参数传进去。</p>
<p>这样我们在写插件时，写一个函数或者一个有 install 函数属性的对象，都可以接收到构造函数 Vue，也就可以使用它来做一些事情了，很 easy 吧！</p>
<pre><code class="hljs language-js copyable" lang="js">Vue.use = <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params">plugin: <span class="hljs-built_in">Function</span> | <span class="hljs-built_in">Object</span></span>) </span>&#123;
  <span class="hljs-comment">// installedPlugins为已安装插件列表，若 Vue 构造函数不存在_installedPlugins属性，初始化</span>
  <span class="hljs-keyword">const</span> installedPlugins = (<span class="hljs-built_in">this</span>._installedPlugins || (<span class="hljs-built_in">this</span>._installedPlugins = []))
  <span class="hljs-comment">// 判断当前插件是否在已安装插件列表，存在直接返回，避免重复安装</span>
  <span class="hljs-keyword">if</span> (installedPlugins.indexOf(plugin) > -<span class="hljs-number">1</span>) &#123;
    <span class="hljs-keyword">return</span> <span class="hljs-built_in">this</span>
  &#125;

<span class="hljs-comment">// toArray方法将Use方法的参数转为数组并删除了第一个参数（第一个参数就是我们的插件）</span>
  <span class="hljs-keyword">const</span> args = toArray(<span class="hljs-built_in">arguments</span>, <span class="hljs-number">1</span>)
  <span class="hljs-comment">// use是构造函数Vue的静态方法，那这里的this就是构造函数Vue本身</span>
  <span class="hljs-comment">// 把this即构造函数Vue放到参数数组args的第一项</span>
  args.unshift(<span class="hljs-built_in">this</span>)
  <span class="hljs-keyword">if</span> (<span class="hljs-keyword">typeof</span> plugin.install === <span class="hljs-string">'function'</span>) &#123;
    <span class="hljs-comment">// 传入参数存在install属性且为函数</span>
    <span class="hljs-comment">// 将构造函数Vue和剩余参数组成的args数组作为参数传入install方法，将其this指向插件对象并执行install方法</span>
    plugin.install.apply(plugin, args)
  &#125; <span class="hljs-keyword">else</span> <span class="hljs-keyword">if</span> (<span class="hljs-keyword">typeof</span> plugin === <span class="hljs-string">'function'</span>) &#123;
    <span class="hljs-comment">// 传入参数是个函数</span>
    <span class="hljs-comment">// 将构造函数Vue和剩余参数组成的args数组作为参数传入插件函数并执行</span>
    plugin.apply(<span class="hljs-literal">null</span>, args)
  &#125;
  <span class="hljs-comment">// 像已安装插件列表中push当前插件</span>
  installedPlugins.push(plugin)
  <span class="hljs-keyword">return</span> <span class="hljs-built_in">this</span>
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-10">初步构建install方法</h2>
<p>接下来开始手写代码了！既然知道 Vue 如何加载插件，那就容易了，因为我们导出的是一个 VueRouter 类，也是一个对象，所以为其添加一个 install 方法就行。</p>
<p>稍微改变下 <code>index.js</code> ，为 VueRouter 类添加静态方法 install：</p>
<pre><code class="hljs language-JS copyable" lang="JS"><span class="hljs-comment">/*
 * @path: src/hello-vue-router/index.js
 * @Description: 入口文件 VueRouter类
 */</span>
<span class="hljs-keyword">import</span> &#123; install &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">"./install"</span>;

<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> <span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">VueRouter</span>()</span>&#123;
  <span class="hljs-function"><span class="hljs-title">constructor</span>(<span class="hljs-params">options</span>)</span>&#123;&#125;
&#125;
VueRouter.install = install;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>接着在 <code>src/hello-vue-router/</code> 目录下创建一个 <code>instal.js</code> ，导出一个 install 方法，我们看过 <code>Vue.use()</code> 方法源码了那肯定晓得这个方法的第一个参数是构造函数 Vue，如下：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">/*
 * @path: src/hello-vue-router/install.js
 * @Description: 插件安装方法install
 */</span>
<span class="hljs-keyword">export</span> <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">install</span>(<span class="hljs-params">Vue</span>)</span>&#123;&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>上面也分析过，插件安装时 install 方法会在 Vue 全局挂载两个组件，<code>router-view</code> 和 <code>router-link</code> 。</p>
<p>要知道，我们在 router 的配置文件中只做了初始化 VueRouter 插件和生成 VueRouter 实例 2 件事情，那我们平常在项目中直接使用的 <code>this.$router & this.$route</code> 是哪来的呢？</p>
<p>首先 <code>$router</code> 是 VueRouter 的实例对象，<code>$route</code> 是当前路由对象，<code>$route</code> 其实也是 <code>$router</code> 的一个属性，这两个对象在 Vue 所有的组件中都可以使用。</p>
<p>可能有小伙伴还记得在项目的入口文件 <code>main.js</code> 中，我们把导出的 router 实例挂载到了 Vue 根实例上，如下：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">import</span> Vue <span class="hljs-keyword">from</span> <span class="hljs-string">'vue'</span>
<span class="hljs-keyword">import</span> App <span class="hljs-keyword">from</span> <span class="hljs-string">'./App.vue'</span>
<span class="hljs-keyword">import</span> router <span class="hljs-keyword">from</span> <span class="hljs-string">'./router'</span>

Vue.config.productionTip = <span class="hljs-literal">false</span>

<span class="hljs-keyword">new</span> Vue(&#123;
  router,
  <span class="hljs-attr">render</span>: <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params">h</span>) </span>&#123; <span class="hljs-keyword">return</span> h(App) &#125;
&#125;).$mount(<span class="hljs-string">'#app'</span>)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>但问题又来了，我们只是挂载到了根实例上，并没有每个组件都挂，况且直接在 Vue 实例上挂载的对象，Vue 都会给我们放到当前实例的 <code>$options</code> 属性上，结合我们只挂载到了根实例上，那我们想要访问 router 实例对象只能采取 <code>this.$root.$options.router</code> 来获取，这里 <code>this.$root</code> 获取到的即根实例。</p>
<p>显然，外部并不是这样调用的。</p>
<p>所以，<code>$router & $route</code> 这两个属性只可能是在 VueRouter 组件内挂载的，并且还需要在 Vue 项目开发过程中能让所有组件都使用。</p>
<p>细品，VueRouter 组件里怎么获取它的实例对象（在这个类里怎么拿到new VueRouter对象）？</p>
<p>可能有小伙伴想到了，这个 router 实例在 Vue 根实例挂载了啊，没错，就是在 new Vue 的时候传入的那个 router 。想办法拿就可以了，怎么拿呢？</p>
<p>上面也说了，我们可以先获取到 Vue 根实例，接着可以用 <code>$options.router</code> 来获取实例上挂载的 router 属性，也就是说目前考虑的是如何在 VueRouter 中拿到 Vue 组件实例（有组件实例就可以拿到根组件实例从而访问它的 <code>$options</code> 属性）</p>
<p>诶，好像又想到了， VueRouter 的 install 方法会传进来一个 Vue 构造函数，它能搞事情吗？</p>
<p>构造函数就是构造函数，它当然不是实例，但是构造函数 Vue 有 <code>mixin</code> 方法啊，没错就是 <code>混入</code></p>
<blockquote>
<p><strong>小</strong> <strong>Tips：Vue.mixin</strong></p>
<p>估摸着很多人都知道这个方法，但还是有必要介绍一下。</p>
<p>混入分为全局混入和组件混入，我们直接使用构造函数 Vue.mixin 这种是全局混入，它接收一个对象参数，在这个对象参数里，我们可以写任何 Vue 组件里的东西，然后我们写的这堆东西会被混入（也可以理解为合并）到 Vue 每一个组件上。</p>
<p>比如写一个生命周期，里面写了个逻辑，那么在所有的 Vue 组件中这个生命周期开始前都会先执行我们混入的逻辑。还不懂？再比如，我们写了个 <code>methods</code> ，里面写了个函数，那这个函数会被混入到所有的 Vue 组件的 <code>methods</code> 中，所有组件都可直接调用。</p>
</blockquote>
<p>Vue.mixin 可以直接写组件那套，这就简单了，写一个生命周期全局混入到组件就 OK 了。</p>
<p>那么问题又又来了，在哪个生命周期里写呢？其实也简单，只要看在哪个生命周期 <code>$options</code> 可以构建好就行了，<code>beforeCreate</code> 这个周期 <code>$options</code> 就构建好了，也就是在这个生命周期后都可以使用 <code>$options</code>，还用问吗？肯定越早越好，就是 <code>beforeCreate</code> 这个生命周期了。</p>
<p>再捋一遍，install 方法可以传过来一个参数构造函数 Vue，使用构造函数 Vue 的静态方法 mixin 为我们所有组件的 <code>beforeCreate</code> 生命周期混入一段逻辑，这段逻辑就是为其挂载上 <code>$router & $route</code> 属性</p>
<p>根据我们上面的逻辑，先上完整代码再逐步解释：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">/*
 * @path: src/hello-vue-router/install.js
 * @Description: 插件安装方法install
 */</span>

<span class="hljs-keyword">export</span> <span class="hljs-keyword">let</span> _Vue;

<span class="hljs-keyword">export</span> <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">install</span>(<span class="hljs-params">Vue</span>)</span>&#123;
  <span class="hljs-keyword">if</span> (install.installed && _Vue === Vue) <span class="hljs-keyword">return</span>;
  install.installed = <span class="hljs-literal">true</span>;

  _Vue = Vue;

  Vue.mixin(&#123;
    <span class="hljs-function"><span class="hljs-title">beforeCreate</span>(<span class="hljs-params"></span>)</span> &#123;
      <span class="hljs-keyword">if</span> (<span class="hljs-built_in">this</span>.$options.router) &#123;
        <span class="hljs-built_in">this</span>._routerRoot = <span class="hljs-built_in">this</span>;
        <span class="hljs-built_in">this</span>._router = <span class="hljs-built_in">this</span>.$options.router;
        <span class="hljs-built_in">this</span>._route = &#123;&#125;;
      &#125; <span class="hljs-keyword">else</span> &#123;
        <span class="hljs-built_in">this</span>._routerRoot = (<span class="hljs-built_in">this</span>.$parent && <span class="hljs-built_in">this</span>.$parent._routerRoot) || <span class="hljs-built_in">this</span>
      &#125;
    &#125;,
  &#125;);

  <span class="hljs-built_in">Object</span>.defineProperty(Vue.prototype, <span class="hljs-string">"$router"</span>, &#123;
    <span class="hljs-function"><span class="hljs-title">get</span>(<span class="hljs-params"></span>)</span> &#123;
      <span class="hljs-keyword">return</span> <span class="hljs-built_in">this</span>._routerRoot._router;
    &#125;,
  &#125;);
  
  <span class="hljs-built_in">Object</span>.defineProperty(Vue.prototype, <span class="hljs-string">'$route'</span>, &#123;
    <span class="hljs-function"><span class="hljs-title">get</span>(<span class="hljs-params"></span>)</span> &#123;
      <span class="hljs-keyword">return</span> <span class="hljs-built_in">this</span>._routerRoot._route;
    &#125;
  &#125;);

  Vue.component(<span class="hljs-string">'RouterView'</span>, &#123;&#125;);
  Vue.component(<span class="hljs-string">'RouterLink'</span>, &#123;&#125;);  
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>来逐块解释：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">export</span> _Vue;

<span class="hljs-keyword">export</span> <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">install</span>(<span class="hljs-params">Vue</span>)</span>&#123;
  <span class="hljs-keyword">if</span> (install.installed && _Vue === Vue) <span class="hljs-keyword">return</span>;
  install.installed = <span class="hljs-literal">true</span>;

  _Vue = Vue;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>诶？ install 文件中不止导出了一个 install 方法，还导出了一个 _Vue 变量，它是什么？</p>
<p>在初始化插件的时候会执行 install 方法，在此方法里会把行参也就是 Vue 的构造函数赋值给变量 _Vue 并导出，其实这个 _Vue 它有两个作用：</p>
<p>第一就是通过它防止插件多次注册安装，因为插件安装方法 install 里我们给此方法添加了一个 installed 属性，当此属性存在且为 true 且 _Vue 已被赋值为构造函数 Vue 时 return，代表已经注册过该插件，无需重复注册。</p>
<p>第二个作用就是构造函数 Vue 上面挂载了很多实用 API 可供我们在 VueRouter 类里使用，当然也可以通过引入 Vue 来使用它的 API，但是一旦引入包使用，打包的时候也会将整个 Vue 打包进去，即然 install 里会把这个构造函数作为参数传过来，恰巧我们写 router 配置文件时，安装插件（Vue.use）是写在初始化 VueRouter 实例前面的，也就是 install 执行较早，这个时候我们把构造函数参数赋值给一个变量在 VueRouter 类里使用简直完美，还不理解就看图 ⬇️</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/9a75b16536864bd1b76d1f387fc1ecde~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>接着来看混入这块，其实说白了就是挂载 <code>$router & $route</code> ：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">export</span> <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">install</span>(<span class="hljs-params">Vue</span>)</span>&#123;  
  <span class="hljs-comment">// 全局注册混入，每个 Vue 实例都会被影响</span>
  Vue.mixin(&#123;
    <span class="hljs-comment">// Vue创建前钩子，此生命周期$options已挂载完成</span>
    <span class="hljs-function"><span class="hljs-title">beforeCreate</span>(<span class="hljs-params"></span>)</span> &#123;
      <span class="hljs-comment">// 通过判断组件实例this.$options有无router属性来判断是否为根实例</span>
      <span class="hljs-comment">// 只有根实例初始化时我们挂载了VueRouter实例router（main.js中New Vue(&#123;router&#125;)时）</span>
      <span class="hljs-keyword">if</span> (<span class="hljs-built_in">this</span>.$options.router) &#123;
        <span class="hljs-built_in">this</span>._routerRoot = <span class="hljs-built_in">this</span>;
        <span class="hljs-comment">// 在 Vue 根实例添加 _router 属性（ VueRouter 实例）</span>
        <span class="hljs-built_in">this</span>._router = <span class="hljs-built_in">this</span>.$options.router;
        <span class="hljs-built_in">this</span>._route = &#123;&#125;;
      &#125; <span class="hljs-keyword">else</span> &#123;
        <span class="hljs-comment">// 为每个组件实例定义_routerRoot，回溯查找_routerRoot</span>
        <span class="hljs-built_in">this</span>._routerRoot = (<span class="hljs-built_in">this</span>.$parent && <span class="hljs-built_in">this</span>.$parent._routerRoot) || <span class="hljs-built_in">this</span>
      &#125;
    &#125;,
  &#125;);

  <span class="hljs-comment">// 在 Vue 原型上添加 $router 属性( VueRouter )并代理到 this._routerRoot._router</span>
  <span class="hljs-built_in">Object</span>.defineProperty(Vue.prototype, <span class="hljs-string">"$router"</span>, &#123;
    <span class="hljs-function"><span class="hljs-title">get</span>(<span class="hljs-params"></span>)</span> &#123;
      <span class="hljs-keyword">return</span> <span class="hljs-built_in">this</span>._routerRoot._router;
    &#125;,
  &#125;);
  
  <span class="hljs-comment">// 在 Vue 原型上添加 $route 属性( 当前路由对象 )并代理到 this._routerRoot._route</span>
  <span class="hljs-built_in">Object</span>.defineProperty(Vue.prototype, <span class="hljs-string">'$route'</span>, &#123;
    <span class="hljs-function"><span class="hljs-title">get</span>(<span class="hljs-params"></span>)</span> &#123;
      <span class="hljs-keyword">return</span> <span class="hljs-built_in">this</span>._routerRoot._route;
    &#125;
  &#125;);
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>我们看看都做了什么：</p>
<p>首先写一个mixin，全局注册混入，让每个 Vue 实例都会被影响。混入里写一个 beforeCreate 钩子，因为此生命周期 <span class="math math-inline"><span class="katex"><span class="katex-mathml"><math xmlns="http://www.w3.org/1998/Math/MathML"><semantics><mrow><mi>o</mi><mi>p</mi><mi>t</mi><mi>i</mi><mi>o</mi><mi>n</mi><mi>s</mi><mtext>最早挂载完成。又因全局混入，所以</mtext><mi>b</mi><mi>e</mi><mi>f</mi><mi>o</mi><mi>r</mi><mi>e</mi><mi>C</mi><mi>r</mi><mi>e</mi><mi>a</mi><mi>t</mi><mi>e</mi><mtext>钩子里我们写了一个通过组件实例中的</mtext><mi>t</mi><mi>h</mi><mi>i</mi><mi>s</mi><mi mathvariant="normal">.</mi></mrow><annotation encoding="application/x-tex">options 最早挂载完成。又因全局混入，所以 beforeCreate 钩子里我们写了一个通过组件实例中的 this.</annotation></semantics></math></span><span class="katex-html" aria-hidden="true"><span class="base"><span class="strut" style="height:0.8888799999999999em;vertical-align:-0.19444em;"></span><span class="mord mathnormal">o</span><span class="mord mathnormal">p</span><span class="mord mathnormal">t</span><span class="mord mathnormal">i</span><span class="mord mathnormal">o</span><span class="mord mathnormal">n</span><span class="mord mathnormal">s</span><span class="mord cjk_fallback">最</span><span class="mord cjk_fallback">早</span><span class="mord cjk_fallback">挂</span><span class="mord cjk_fallback">载</span><span class="mord cjk_fallback">完</span><span class="mord cjk_fallback">成</span><span class="mord cjk_fallback">。</span><span class="mord cjk_fallback">又</span><span class="mord cjk_fallback">因</span><span class="mord cjk_fallback">全</span><span class="mord cjk_fallback">局</span><span class="mord cjk_fallback">混</span><span class="mord cjk_fallback">入</span><span class="mord cjk_fallback">，</span><span class="mord cjk_fallback">所</span><span class="mord cjk_fallback">以</span><span class="mord mathnormal">b</span><span class="mord mathnormal">e</span><span class="mord mathnormal" style="margin-right:0.10764em;">f</span><span class="mord mathnormal">o</span><span class="mord mathnormal" style="margin-right:0.02778em;">r</span><span class="mord mathnormal">e</span><span class="mord mathnormal" style="margin-right:0.07153em;">C</span><span class="mord mathnormal" style="margin-right:0.02778em;">r</span><span class="mord mathnormal">e</span><span class="mord mathnormal">a</span><span class="mord mathnormal">t</span><span class="mord mathnormal">e</span><span class="mord cjk_fallback">钩</span><span class="mord cjk_fallback">子</span><span class="mord cjk_fallback">里</span><span class="mord cjk_fallback">我</span><span class="mord cjk_fallback">们</span><span class="mord cjk_fallback">写</span><span class="mord cjk_fallback">了</span><span class="mord cjk_fallback">一</span><span class="mord cjk_fallback">个</span><span class="mord cjk_fallback">通</span><span class="mord cjk_fallback">过</span><span class="mord cjk_fallback">组</span><span class="mord cjk_fallback">件</span><span class="mord cjk_fallback">实</span><span class="mord cjk_fallback">例</span><span class="mord cjk_fallback">中</span><span class="mord cjk_fallback">的</span><span class="mord mathnormal">t</span><span class="mord mathnormal">h</span><span class="mord mathnormal">i</span><span class="mord mathnormal">s</span><span class="mord">.</span></span></span></span></span>​options 有无 router 属性来判断是否为根实例，只有根实例初始化时才挂载 VueRouter 实例 router（就是 main.js 中 New Vue(&#123;router&#125;) 时）。</p>
<blockquote>
<p><strong>是根实例：</strong></p>
<p>是根实例就为其添加 _router 属性，值为 VueRouter 实例，同时添加一个 _routerRoot 属性将 this 也就是根实例也挂载上去</p>
<p>上面分析过，这里还应有 route 对象，所以最后还为其添加了 _route 属性，暂且将它设置成空对象，后面再完善</p>
<p><strong>不是根实例：</strong></p>
<p>不是根实例，那就是子组件实例了，找它的父实例判断其父实例有没有 _routerRoot 属性，没有就为其加上引用，确保每一个组件实例都可以有 _routerRoot 属性，也就是让每个组件中都可以引用并访问到根实例，注意并不是反复赋值，对象间的引用而已</p>
</blockquote>
<p>最后为了让每个组件都可以访问到 <code>$router $ $route</code> 对象，我们在 Vue 原型上添加了 <span class="math math-inline"><span class="katex"><span class="katex-mathml"><math xmlns="http://www.w3.org/1998/Math/MathML"><semantics><mrow><mi>r</mi><mi>o</mi><mi>u</mi><mi>t</mi><mi>e</mi><mi>r</mi><mtext>属性并代理到</mtext><mi mathvariant="normal">‘</mi><mi>t</mi><mi>h</mi><mi>i</mi><mi>s</mi><msub><mi mathvariant="normal">.</mi><mi>r</mi></msub><mi>o</mi><mi>u</mi><mi>t</mi><mi>e</mi><mi>r</mi><mi>R</mi><mi>o</mi><mi>o</mi><mi>t</mi><msub><mi mathvariant="normal">.</mi><mi>r</mi></msub><mi>o</mi><mi>u</mi><mi>t</mi><mi>e</mi><mi>r</mi><mi mathvariant="normal">‘</mi><mtext>，也在</mtext><mi>V</mi><mi>u</mi><mi>e</mi><mtext>原型上添加了</mtext><mi mathvariant="normal">‘</mi></mrow><annotation encoding="application/x-tex">router 属性并代理到 `this._routerRoot._router`，也在 Vue 原型上添加了 `</annotation></semantics></math></span><span class="katex-html" aria-hidden="true"><span class="base"><span class="strut" style="height:0.84444em;vertical-align:-0.15em;"></span><span class="mord mathnormal" style="margin-right:0.02778em;">r</span><span class="mord mathnormal">o</span><span class="mord mathnormal">u</span><span class="mord mathnormal">t</span><span class="mord mathnormal">e</span><span class="mord mathnormal" style="margin-right:0.02778em;">r</span><span class="mord cjk_fallback">属</span><span class="mord cjk_fallback">性</span><span class="mord cjk_fallback">并</span><span class="mord cjk_fallback">代</span><span class="mord cjk_fallback">理</span><span class="mord cjk_fallback">到</span><span class="mord">‘</span><span class="mord mathnormal">t</span><span class="mord mathnormal">h</span><span class="mord mathnormal">i</span><span class="mord mathnormal">s</span><span class="mord"><span class="mord">.</span><span class="msupsub"><span class="vlist-t vlist-t2"><span class="vlist-r"><span class="vlist" style="height:0.151392em;"><span style="top:-2.5500000000000003em;margin-left:0em;margin-right:0.05em;"><span class="pstrut" style="height:2.7em;"></span><span class="sizing reset-size6 size3 mtight"><span class="mord mathnormal mtight" style="margin-right:0.02778em;">r</span></span></span></span><span class="vlist-s">​</span></span><span class="vlist-r"><span class="vlist" style="height:0.15em;"><span></span></span></span></span></span></span><span class="mord mathnormal">o</span><span class="mord mathnormal">u</span><span class="mord mathnormal">t</span><span class="mord mathnormal">e</span><span class="mord mathnormal" style="margin-right:0.02778em;">r</span><span class="mord mathnormal" style="margin-right:0.00773em;">R</span><span class="mord mathnormal">o</span><span class="mord mathnormal">o</span><span class="mord mathnormal">t</span><span class="mord"><span class="mord">.</span><span class="msupsub"><span class="vlist-t vlist-t2"><span class="vlist-r"><span class="vlist" style="height:0.151392em;"><span style="top:-2.5500000000000003em;margin-left:0em;margin-right:0.05em;"><span class="pstrut" style="height:2.7em;"></span><span class="sizing reset-size6 size3 mtight"><span class="mord mathnormal mtight" style="margin-right:0.02778em;">r</span></span></span></span><span class="vlist-s">​</span></span><span class="vlist-r"><span class="vlist" style="height:0.15em;"><span></span></span></span></span></span></span><span class="mord mathnormal">o</span><span class="mord mathnormal">u</span><span class="mord mathnormal">t</span><span class="mord mathnormal">e</span><span class="mord mathnormal" style="margin-right:0.02778em;">r</span><span class="mord">‘</span><span class="mord cjk_fallback">，</span><span class="mord cjk_fallback">也</span><span class="mord cjk_fallback">在</span><span class="mord mathnormal" style="margin-right:0.22222em;">V</span><span class="mord mathnormal">u</span><span class="mord mathnormal">e</span><span class="mord cjk_fallback">原</span><span class="mord cjk_fallback">型</span><span class="mord cjk_fallback">上</span><span class="mord cjk_fallback">添</span><span class="mord cjk_fallback">加</span><span class="mord cjk_fallback">了</span><span class="mord">‘</span></span></span></span></span>route<code>属性并代理到</code>this._routerRoot._route`，剩下就是创建全局组件了：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// 全局注册组件router-view</span>
Vue.component(<span class="hljs-string">'RouterView'</span>, &#123;&#125;);
<span class="hljs-comment">// 全局注册组件router-link</span>
Vue.component(<span class="hljs-string">'RouterLink'</span>, &#123;&#125;); 
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这块暂时比较简单，使用 Vue.component 全局注册了两个组件，配置对象都直接为空。下面简单的配置一下这两个全局组件，让项目跑起来，毕竟现在运行还在报错。</p>
<h2 data-id="heading-11">初步构建RouterView、RouterLink组件</h2>
<p>稍微分离一下，我们在 <code>src/hello-vue-router/</code> 目录下新建一个 <code>components/</code> 文件夹</p>
<p>在 <code>components</code> 文件夹下新建 <code>view.js</code> 和 <code>link.js</code> 两个文件，随后还是要先改变一下 install 方法：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">/*
 * @path: src/hello-vue-router/install.js
 * @Description: 插件安装方法install
 */</span>
<span class="hljs-keyword">import</span> View <span class="hljs-keyword">from</span> <span class="hljs-string">"./components/view"</span>;
<span class="hljs-keyword">import</span> Link <span class="hljs-keyword">from</span> <span class="hljs-string">"./components/link"</span>;

<span class="hljs-keyword">export</span> <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">install</span>(<span class="hljs-params">Vue</span>)</span>&#123;
  <span class="hljs-comment">// 全局注册组件router-view</span>
  Vue.component(<span class="hljs-string">'RouterView'</span>, view);

  <span class="hljs-comment">// 全局注册组件router-link</span>
  Vue.component(<span class="hljs-string">'RouterLink'</span>, link);  
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>可以看到我们把两个组件的配置对象单独拉出去了两个文件来写，其实就是每个文件导出一个组件配置对象。</p>
<p>先看 <code>link.js</code> ，link 组件类似 a 标签，其实它默认就会渲染一个 a 标签，组件接收一个 to 参数，可以为对象，也可以为字符串，用作跳转。</p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">router-link</span> <span class="hljs-attr">to</span>=<span class="hljs-string">"/home"</span>></span>
<span class="hljs-tag"><<span class="hljs-name">router-link</span> <span class="hljs-attr">:to</span>=<span class="hljs-string">"&#123;path: '/home'&#125;"</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>看实现：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">/*
 * @path: src/hello-vue-router/components/link.js
 * @Description: router-link
 */</span>
<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> &#123;
  <span class="hljs-attr">name</span>: <span class="hljs-string">"RouterLink"</span>,
  <span class="hljs-attr">props</span>: &#123;
    <span class="hljs-attr">to</span>: &#123;
      <span class="hljs-attr">type</span>: [<span class="hljs-built_in">String</span>, <span class="hljs-built_in">Object</span>],
      <span class="hljs-attr">require</span>: <span class="hljs-literal">true</span>
    &#125;
  &#125;,
  <span class="hljs-function"><span class="hljs-title">render</span>(<span class="hljs-params">h</span>)</span> &#123;
    <span class="hljs-keyword">const</span> href = <span class="hljs-keyword">typeof</span> <span class="hljs-built_in">this</span>.to === <span class="hljs-string">'string'</span> ? <span class="hljs-built_in">this</span>.to : <span class="hljs-built_in">this</span>.to.path
    <span class="hljs-keyword">const</span> router = <span class="hljs-built_in">this</span>.$router
    <span class="hljs-keyword">let</span> data = &#123;
      <span class="hljs-attr">attrs</span>: &#123;
        <span class="hljs-attr">href</span>: router.mode === <span class="hljs-string">"hash"</span> ? <span class="hljs-string">"#"</span> + href : href
      &#125;
    &#125;;
    <span class="hljs-keyword">return</span> h(<span class="hljs-string">"a"</span>, data, <span class="hljs-built_in">this</span>.$slots.default)
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>首先是 props 接收参数 to，必选项，可为对象或字符串类型，在 render 函数中首先判断了参数 to 的类型，并把它统一做成了对象。</p>
<p>接着访问了根实例中的 <code>$router</code>，这里的 this 其实是一个 Proxy，输出一下就会知道，这个 Proxy 代理到了 VueComponent 实例，而我们在 install 给每个组件实例都加上了指向根实例的属性 _routerRoot，这里其实想要访问 router 对象有好多种。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// this._self._routerRoot._router</span>
<span class="hljs-comment">// this._routerRoot._router</span>
<span class="hljs-comment">// this.$router</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<blockquote>
<p>用啥都可以，但是源码用的第三种，我们也就用这个了，可能是字符最少</p>
</blockquote>
<p>接着就是返回一个 VNode 了，其实 render 的 h 参数就是 createElement 函数，作用就是创建一个 VNode，它的参数看官网描述：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// @returns &#123;VNode&#125;</span>
createElement(
  <span class="hljs-comment">// &#123;String | Object | Function&#125;</span>
  <span class="hljs-comment">// 一个 HTML 标签名、组件选项对象，或者</span>
  <span class="hljs-comment">// resolve 了上述任何一种的一个 async 函数。必填项。</span>
  <span class="hljs-string">'div'</span>,

  <span class="hljs-comment">// &#123;Object&#125;</span>
  <span class="hljs-comment">// 一个与模板中 attribute 对应的数据对象。可选。</span>
  &#123;
    <span class="hljs-comment">// (详情见下一节)</span>
  &#125;,

  <span class="hljs-comment">// &#123;String | Array&#125;</span>
  <span class="hljs-comment">// 子级虚拟节点 (VNodes)，由 `createElement()` 构建而成，</span>
  <span class="hljs-comment">// 也可以使用字符串来生成“文本虚拟节点”。可选。</span>
  [
    <span class="hljs-string">'先写一些文字'</span>,
    createElement(<span class="hljs-string">'h1'</span>, <span class="hljs-string">'一则头条'</span>),
    createElement(MyComponent, &#123;
      <span class="hljs-attr">props</span>: &#123;
        <span class="hljs-attr">someProp</span>: <span class="hljs-string">'foobar'</span>
      &#125;
    &#125;)
  ]
)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这里我们想要返回一个 a 标签，所以第一个参数就是字符串 a，第二个参数就是标签 attribute 对应的数据对象，要给他带上 href 属性，属性值就是 to 参数，需要注意的是模式问题，hash 模式下要给所有的跳转路径前加上一个 # 号，所以需要 <code>router.mode</code> 判断一下模式，第三个参数就是子节点了，也就是 <code>router-link</code> 组件中包含的值，其实使用默认插槽即可拿到， <code>this.$slots.default</code> 获取默认插槽。</p>
<p>OK，到这 <code>router-link</code> 组件就差不多完成了，只是在 history 模式下还有问题，我们后面再说。</p>
<p>再来看 <code>view.js</code> ，其实我们并不需要 RouterView 组件渲染什么东西，它充其量就是一个占位符，用来替换我们的组件模块UI，所以一不需要生命周期，二不需要状态管理，三不需要各种监听，通俗点就是没必要创造一个实例，作为一个三无组件，函数式组件最符合了。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">/*
 * @path: src/hello-vue-router/components/view.js
 * @Description: router-view
 */</span>
<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> &#123;
  <span class="hljs-attr">name</span>: <span class="hljs-string">"RouterView"</span>,
  <span class="hljs-attr">functional</span>: <span class="hljs-literal">true</span>, <span class="hljs-comment">// 函数式组件</span>
  <span class="hljs-function"><span class="hljs-title">render</span>(<span class="hljs-params">h</span>)</span> &#123;
    <span class="hljs-keyword">return</span> h(<span class="hljs-string">'div'</span>, <span class="hljs-string">'This is RoutePage'</span>)
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>如上，直接先设置成函数式组件，然后 render 函数直接返回一个 div，内容为 <code>'This is RoutePage'</code>（h 函数即 createElement 函数没有无第二个参数可省略），这里只是初步搭建一下结构，逻辑后面再说，先让页面跑起来，现在你再打开浏览器会发现无报错了，导航也有了，还可以点击切换路由，就是路由模块组件即 <code>router-view</code> 永远都只显示 <code>This is RoutePage</code> ，如下：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/5f56470f44a84675ae47c1c00a6fccf0~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-12">初步构建VueRouter类</h2>
<p>install 方法我们暂时可以告一段落，思考一下 VueRouter 类里，我们需要做什么？</p>
<p>首先，接收到参数肯定要对参数进行一个分析，传进来的是一个对象，其中主要的就是两个属性：</p>
<ul>
<li>mode 路由模式</li>
<li>routes 路由配置数组</li>
</ul>
<p>其实 base 属性也比较重要，不过可以先不考虑这个，逻辑跑通后有时间再完善</p>
<p>思考 mode 配置，我们需要根据 mode 传入的路由模式来初始化对应模式的一些东西，从而实现对该模式下的路由监听。</p>
<p>那再思考一下关于 routes 数组，我们需要做什么？</p>
<p>其实，此数组中配置的最重要的就是路由 path 以及 path 对应的路由组件，当然还有一些重定向、动态路由、路由名称、路由别名的配置，这些也都暂时不考虑，后期逐步完善。</p>
<p>问题来了，监听到路由发生了变化我们需要做什么？</p>
<p>当然是拿到改变的路由 path ，在 routes 数组中找到匹配的 path 配置，获取它的组件，然后把拿到的组件渲染到对应的 <code>router-view</code> 中去。</p>
<p>对于 routes 配置，目的很明确了，因为这是一个树结构的数组对象，我们是基于 path 匹配的，很不放便，所以需要提前将此配置解析为 <code>&#123;key : value&#125;</code> 这种结构，当然 key 就是我们的 path ，而 value 则是此路由的配置项。分析完毕，开始敲代码：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">/*
 * @path: src/hello-vue-router/index.js
 * @Description: 入口文件 VueRouter类
 */</span>
<span class="hljs-keyword">import</span> &#123; install &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">"./install"</span>;
<span class="hljs-keyword">import</span> &#123; createMatcher &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">"./create-matcher"</span>;
<span class="hljs-keyword">import</span> &#123; HashHistory &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">"./history/hash"</span>;
<span class="hljs-keyword">import</span> &#123; HTML5History &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">"./history/html5"</span>;
<span class="hljs-keyword">import</span> &#123; AbstractHistory &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">"./history/abstract"</span>;
<span class="hljs-keyword">const</span> inBrowser = <span class="hljs-keyword">typeof</span> <span class="hljs-built_in">window</span> !== <span class="hljs-string">"undefined"</span>;

<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> <span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">VueRouter</span>()</span>&#123;
  <span class="hljs-function"><span class="hljs-title">constructor</span>(<span class="hljs-params">options</span>)</span> &#123;
    <span class="hljs-comment">// 路由配置</span>
    <span class="hljs-built_in">this</span>.options = options;
    <span class="hljs-comment">// 创建路由matcher对象，传入routes路由配置列表及VueRouter实例，主要负责url匹配</span>
    <span class="hljs-built_in">this</span>.matcher = createMatcher(options.routes);

    <span class="hljs-keyword">let</span> mode = options.mode || <span class="hljs-string">"hash"</span>;

    <span class="hljs-comment">// 支持所有 JavaScript 运行环境，非浏览器环境强制使用abstract模式，主要用于SSR</span>
    <span class="hljs-keyword">if</span> (!inBrowser) &#123;
      mode = <span class="hljs-string">"abstract"</span>;
    &#125;

    <span class="hljs-built_in">this</span>.mode = mode;

    <span class="hljs-comment">// 根据不同mode，实例化不同history实例</span>
    <span class="hljs-keyword">switch</span> (mode) &#123;
      <span class="hljs-keyword">case</span> <span class="hljs-string">"history"</span>:
        <span class="hljs-built_in">this</span>.history = <span class="hljs-keyword">new</span> HTML5History(<span class="hljs-built_in">this</span>);
        <span class="hljs-keyword">break</span>;
      <span class="hljs-keyword">case</span> <span class="hljs-string">"hash"</span>:
        <span class="hljs-built_in">this</span>.history = <span class="hljs-keyword">new</span> HashHistory(<span class="hljs-built_in">this</span>);
        <span class="hljs-keyword">break</span>;
      <span class="hljs-keyword">case</span> <span class="hljs-string">"abstract"</span>:
        <span class="hljs-built_in">this</span>.history = <span class="hljs-keyword">new</span> AbstractHistory(<span class="hljs-built_in">this</span>);
        <span class="hljs-keyword">break</span>;
      <span class="hljs-keyword">default</span>:
        <span class="hljs-keyword">if</span> (process.env.NODE_ENV !== <span class="hljs-string">"production"</span>) &#123;
          <span class="hljs-keyword">throw</span> <span class="hljs-keyword">new</span> <span class="hljs-built_in">Error</span>(<span class="hljs-string">`[vue-router] invalid mode: <span class="hljs-subst">$&#123;mode&#125;</span>`</span>);
        &#125;
    &#125;
  &#125;
&#125;
VueRouter.install = install;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>其实 VueRouter 这个类的 constructor 里的逻辑很简单，就是判断传入的 mode 模式随后初始化不同类实例，虽然实例化的是不同的类，但实例方法包括属性等都是一样的</p>
<p>完整的 VueRouter 有三种模式：</p>
<ul>
<li>hash 基本浏览器都支持，但是URL有 # 号，不好看</li>
<li>history URL好看，但是部分老版本浏览器不支持</li>
<li>abstract 支持所有环境，主要用于服务端 SSR</li>
</ul>
<p>我们不太清楚的可能是 abstract 模式了，其实在官方中把这种模式定义为支持任何环境的模式，因为这种模式是手动模拟一个路由环境，而源码中也有一个和上面一样的逻辑判断（<code>inBrowser</code>），就是在当前环境没有 window 对象也就是非浏览器环境情况下，直接强制切换为此模式，所以这种模式也主要用于 SSR，后面有精力就实现一下，相当简单。</p>
<p>整个 constructor 其实没有复杂逻辑。先判断当前环境有无 window 对象也就是否是浏览器环境，是的话继续走，不是则强制 mode 值为 abstract；然后就是判断一下 mode 属性值，匹配三个模式分别使用对应类来初始化该路由模式实例，匹配不到直接抛出错误，这里不论是哪个模式，在对应的类中我们都会实现一些相同的方法，并且将初始化的实例挂载到了 VueRouter 实例的 hisory 属性上。</p>
<p>其实在做 mode 参数校验前，还引入了一个 createMatcher 方法，这个方法的返回值挂载到了 VueRouter 实例的 matcher 属性上，它是做什么的呢？</p>
<p>你应该大致猜到了，上面也说过，大概就是构建 <code>&#123;key : value&#125;</code> 结构的对象（称之为 pathMap 对象）让我们更便捷的通过 path 路径匹配到对应路由模块。</p>
<p>那接下来我们就一步步推导下 createMatcher 这个方法是怎么封装的。</p>
<h2 data-id="heading-13">createMatcher方法推导</h2>
<p>你以为 createMatcher 这个方法只是单纯的构建一个 pathMap 映射对象？No，那样的话函数名应该叫 createRouterMap 才对，其实最开始确实是这个名字，但是一套推导下来发现它不仅可以构建出 pathMap 映射对象， <code>addRoutes/addRoute/getRoutes</code> 这几个方法也可以在这里实现。</p>
<p>构建出 pathMap 映射对象是做什么的？路由匹配啊！输入 path 的时候能够获取到对应的路由配置信息，pathMap 对象就相当于一个路由数据管家，写入的所有路由配置都在这里了，那动态添加路由的时候把新路由对象解析并添加到 pathMap 对象里就可以了，所以我们把路由匹配及动态路由添加的几个方法全放一块合成了 createMatcher 函数，我们叫它 <code>路由匹配器函数</code> 吧，主要作用就是生成一个路由匹配器对象，这个函数就返回了一个包含四个方法属性的对象：</p>
<ul>
<li>macth 路由匹配</li>
<li>addRoutes 动态添加路由（参数必须是一个符合 <code>routes</code> 选项要求的数组）</li>
<li>addRoute 动态添加路由（添加一条新路由规则）</li>
<li>getRoutes 获取所有活跃的路由记录列表</li>
</ul>
<h3 data-id="heading-14">createRouteMap生成路由映射</h3>
<p>首先我们要构建 pathMap 对象，单独拉出来一个文件写这个方法，在 <code>src/hello-vue-router/</code> 目录下新建一个 <code>create-route-map.js</code> 文件：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">/*
 * @path: src/hello-vue-router/create-route-map.js
 * @Description: 生成路由映射
 */</span>
<span class="hljs-comment">// 生成路由映射</span>
<span class="hljs-keyword">export</span> <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">createRouteMap</span>(<span class="hljs-params">routes</span>)</span>&#123;
  <span class="hljs-keyword">let</span> routeMap = &#123;&#125;
  routes.forEach(<span class="hljs-function"><span class="hljs-params">route</span> =></span> &#123;
    routeMap[route.path] = route
  &#125;)
  <span class="hljs-keyword">return</span> routeMap
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>如上，几行代码就生成了一个 pathMap 路由映射对象，有问题吗？没有问题，但我们上面只匹配了一层，路由配置里面可以有无限层子路由，比如下面这样的配置：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> routes = [
  &#123;
    <span class="hljs-attr">path</span>: <span class="hljs-string">"/about"</span>,
    <span class="hljs-attr">name</span>: <span class="hljs-string">"About"</span>,
    component,
  &#125;,
  &#123;
    <span class="hljs-attr">path</span>: <span class="hljs-string">"/parent"</span>,
    <span class="hljs-attr">name</span>: <span class="hljs-string">"Parent"</span>,
    component,
    <span class="hljs-attr">children</span>:[
      &#123;
        <span class="hljs-attr">path</span>: <span class="hljs-string">"child"</span>,
        <span class="hljs-attr">name</span>:<span class="hljs-string">"Child"</span>,
        component
      &#125;
    ]
  &#125;
];
<span class="copy-code-btn">复制代码</span></code></pre>
<p>我们想要生成的 pathMap 对象是什么，是下面这样：</p>
<pre><code class="hljs language-js copyable" lang="js">&#123;
  <span class="hljs-string">"/about"</span>: &#123;...&#125;,
  <span class="hljs-string">"/parent"</span>: &#123;...&#125;,
  <span class="hljs-string">"/parent/child"</span>: &#123;...&#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>可是现在的代码逻辑只生成了下面这种：</p>
<pre><code class="hljs language-js copyable" lang="js">&#123;
  <span class="hljs-string">"/about"</span>: &#123;...&#125;,
  <span class="hljs-string">"/parent"</span>: &#123;...&#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>有问题吗？有大问题，一层路由是 ok 的，多层级的嵌套路由直接 gameover。所以要递归处理解析，修改一下代码，还是老套路，先看完整代码再逐步解析。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">export</span> <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">createRouteMap</span>(<span class="hljs-params">routes</span>)</span>&#123;
  <span class="hljs-keyword">const</span> pathMap = <span class="hljs-built_in">Object</span>.create(<span class="hljs-literal">null</span>);
  <span class="hljs-comment">// 递归处理路由记录，最终生成路由映射</span>
  routes.forEach(<span class="hljs-function"><span class="hljs-params">route</span> =></span> &#123;
    <span class="hljs-comment">// 生成一个RouteRecord并更新pathMap</span>
    addRouteRecord(pathMap, route, <span class="hljs-literal">null</span>)
  &#125;)
  <span class="hljs-keyword">return</span> pathMap
&#125;

<span class="hljs-comment">// 添加路由记录</span>
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">addRouteRecord</span>(<span class="hljs-params">pathMap, route, parent</span>)</span>&#123;
  <span class="hljs-keyword">const</span> &#123; path, name &#125; = route

  <span class="hljs-comment">// 生成格式化后的path(子路由会拼接上父路由的path)</span>
  <span class="hljs-keyword">const</span> normalizedPath = normalizePath(path, parent)

  <span class="hljs-comment">// 生成一条路由记录</span>
  <span class="hljs-keyword">const</span> record = &#123;
    <span class="hljs-attr">path</span>: normalizedPath, <span class="hljs-comment">// 规范化后的路径</span>
    <span class="hljs-attr">regex</span>: <span class="hljs-string">""</span>, <span class="hljs-comment">// 利用path-to-regexp包生成用来匹配path的增强正则对象，用来匹配动态路由 （/a/:b）</span>
    <span class="hljs-attr">components</span>: route.component, <span class="hljs-comment">// 保存路由组件，省略了命名视图解析</span>
    name,
    parent, <span class="hljs-comment">// 父路由记录</span>
    <span class="hljs-attr">redirect</span>: route.redirect, <span class="hljs-comment">// 重定向的路由配置对象</span>
    <span class="hljs-attr">beforeEnter</span>: route.beforeEnter, <span class="hljs-comment">// 路由独享的守卫</span>
    <span class="hljs-attr">meta</span>: route.meta || &#123;&#125;, <span class="hljs-comment">// 元信息</span>
    <span class="hljs-attr">props</span>: route.props == <span class="hljs-literal">null</span> ? &#123;&#125; : route.props<span class="hljs-comment">// 动态路由传参</span>
  &#125;

  <span class="hljs-comment">// 处理有子路由情况，递归</span>
  <span class="hljs-keyword">if</span> (route.children) &#123;
    <span class="hljs-comment">// 遍历生成子路由记录</span>
    route.children.forEach(<span class="hljs-function"><span class="hljs-params">child</span> =></span> &#123;
      addRouteRecord(pathMap, child, record)
    &#125;)
  &#125;

  <span class="hljs-comment">// 若pathMap中不存在当前路径，则添加pathList和pathMap</span>
  <span class="hljs-keyword">if</span> (!pathMap[record.path]) &#123;
    pathMap[record.path] = record
  &#125;
&#125;

<span class="hljs-comment">// 规格化路径</span>
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">normalizePath</span>(<span class="hljs-params">
  path,
  parent
</span>) </span>&#123;
  <span class="hljs-comment">// 下标0为 / ，则是最外层path</span>
  <span class="hljs-keyword">if</span> (path[<span class="hljs-number">0</span>] === <span class="hljs-string">'/'</span>) <span class="hljs-keyword">return</span> path
  <span class="hljs-comment">// 无父级，则是最外层path</span>
  <span class="hljs-keyword">if</span> (!parent) <span class="hljs-keyword">return</span> path
  <span class="hljs-comment">// 清除path中双斜杆中的一个</span>
  <span class="hljs-keyword">return</span> <span class="hljs-string">`<span class="hljs-subst">$&#123;parent.path&#125;</span>/<span class="hljs-subst">$&#123;path&#125;</span>`</span>.replace(<span class="hljs-regexp">/\/\//g</span>, <span class="hljs-string">'/'</span>)
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>其实这块代码比较简单，也都带上了注释，简单说几个点吧。</p>
<p>我们在递归中其实把每一个路由配置对象都格式化了一下，生成了一个新的 record 对象，该对象的的 path 其实是完整 path，也就是如果原 path 是以 <code>/</code> 开头，说明自己是顶级路由，path 就是它本身，如果原 path 不是以 <code>/</code> 开头，说明它是子级路由，那我们就需要拼接上父级 path，为此我们单独写了一个 normalizePath 函数来生成完整 path，也就是将 path 规格化。</p>
<p>因为递归时传入了 parent ，除了顶级路由为 null 之外，子级路由都有父级，而我们子路由递归时是在 record 对象生成之后的，所以每个传入的父级都是格式化好的 record 对象，父级的 path 也是完整 path，这样不论多少子级，都可以拼出完整 path。</p>
<p>接着说 record 对象，我们还为其添加了一个 parent 属性指向它的父级对象，让父子之间有个联系，还有一些路由中可配置的参数像重定向 <code>redirect</code>、路由独享守卫 <code>beforeEnter</code>、元信息 <code>meta</code>、路由名称 <code>name</code> 这些我们也都接收并放到了 record 对象里。</p>
<p>单独说 <code>regex</code> 属性，相信大家都知道 VueRouter 里支持动态路由，其实主要是利用一个三方包 <code>path-to-regexp</code> 生成用来匹配path 的增强正则对象，用来匹配对应的动态路由，生成正则之后就放在 <code>regex</code> 属性里，这块对我们手写来说没有特别大的意义，所以我没写，直接置空了，如果有兴趣就直接看源码这里，主要还是 <code>path-to-regexp</code> 这个包的使用，也不复杂。另外最后的 <code>props</code> 属性是动态路由传参用的，暂不做这块可忽略。</p>
<p>最终一套下来，生成的 pathMap 对象就是 <code>[&#123;path: record&#125;...]</code> 这种格式了，key 是格式化后的完整 path，value是格式化好的路由配置对象 record。</p>
<p>到这里路由映射对象 pathMap 对象解析方法就差不多写完了。</p>
<h3 data-id="heading-15">createMatcher生成路由匹配器</h3>
<p>接着，我们在 <code>src/hello-vue-router/</code> 文件夹下创建一个 <code>create-matcher.js</code> 文件，按照我们上面分析大致结构如下：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">/*
 * @path: src/hello-vue-router/create-route-map.js
 * @Description: 路由匹配器Matcher对象生成方法
 */</span>
<span class="hljs-keyword">import</span> &#123; createRouteMap &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">"./create-route-map"</span>;

<span class="hljs-keyword">export</span> <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">createMatcher</span>(<span class="hljs-params">routes</span>)</span>&#123;
  <span class="hljs-comment">// 生成路由映射对象 pathMap</span>
  <span class="hljs-keyword">const</span> pathMap = createRouteMap(routes)

  <span class="hljs-comment">// 动态添加路由（添加一条新路由规则）</span>
  <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">addRoute</span>(<span class="hljs-params"></span>)</span>&#123; &#125;

  <span class="hljs-comment">// 动态添加路由（参数必须是一个符合 routes 选项要求的数组）</span>
  <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">addRoutes</span>(<span class="hljs-params"></span>)</span>&#123; &#125;

  <span class="hljs-comment">// 获取所有活跃的路由记录列表</span>
  <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">getRoutes</span>(<span class="hljs-params"></span>)</span>&#123; &#125;

  <span class="hljs-comment">// 路由匹配</span>
  <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">match</span>(<span class="hljs-params"></span>)</span>&#123; &#125;

  <span class="hljs-keyword">return</span> &#123;
    match,
    addRoute,
    getRoutes,
    addRoutes
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>路由匹配器 Matcher 对象生成方法即 createMatcher ，我们只需要一个参数，那就是生成路由映射对象 pathMap 所需的 routes 数组（就是 router 配置文件里的那个 routes）。</p>
<p>其实路由映射对象 pathMap 只有在匹配路由和动态添加路由的时候可以用到，而这些情况都包含在 <code>createMatcher</code> 函数内，所以在 <code>createMatcher</code> 函数内部直接使用刚写好的 <code>createRouteMap</code> 方法生成了 pathMap 对象，在函数调用时，内部一直维护着这个对象，因为 <code>createMatcher</code> 函数返回的几个方法里都有对 pathMap 对象的引用，就是一个典型闭包场景，所以整个 VueRouter 实例初始化过程中 <code>createMatcher</code> 函数只需调用一次就 OK，<code>createRouteMap</code> 方法也抛出了动态修改 pathMap 的方法。</p>
<h4 data-id="heading-16">addRoutes核心实现</h4>
<p>先来看 <code>addRoutes</code> 实现吧，比较简单，这个 API 的定义其实就是用来动态添加路由的，简单点就是把传入的新路由对象解析后加入到老 pathMap 对象里，使用时参数必须是一个符合 routes 选项要求的数组，作用就是可以让我们随时随地的添加几个路由配置，因为参数是数组并且和 routes 是一致的格式，所以完全可以复用 <code>createRouteMap</code> 方法。</p>
<p>先把 <code>createRouteMap</code> 方法简单修改一下，只需要加一个参数就 ok ，逻辑没问题。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// 新增 oldPathMap 参数</span>
<span class="hljs-keyword">export</span> <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">createRouteMap</span>(<span class="hljs-params">routes, oldPathMap</span>)</span>&#123;
  <span class="hljs-comment">// const pathMap = Object.create(null); old</span>
  <span class="hljs-keyword">const</span> pathMap = oldPathMap || <span class="hljs-built_in">Object</span>.create(<span class="hljs-literal">null</span>); <span class="hljs-comment">// new</span>
  
  <span class="hljs-comment">// ...</span>
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>如上，动态添加的时候，将旧的 pathMap 传进去即可，之前我们直接声明了一个空 pathMap 对象，这里可以判断一下 <code>oldPathMap</code> 参数是否存在，存在就给 pathMap 赋值，不存在默认还是空对象即可。这样就做到了把没有解析的配置，解析并添加到老映射对象里，是不是简单？ <code>addRoutes</code> 方法就更简单了：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// 动态添加路由（参数必须是一个符合 routes 选项要求的数组）</span>
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">addRoutes</span>(<span class="hljs-params">routes</span>)</span>&#123;
  createRouteMap(routes, pathMap)
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-17">getRoutes核心实现</h4>
<p>至于 <code>getRoutes</code> ，就更更简单了，直接返回 <code>pathMap</code> 对象即可</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// 获取所有活跃的路由记录列表</span>
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">getRoutes</span>(<span class="hljs-params"></span>)</span>&#123;
  <span class="hljs-keyword">return</span> pathMap
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-18">addRoute核心实现</h4>
<p><code>addRoute</code> 这个方法我们要稍微注意一下，因为这个方法将是未来 4.0+ 版本动态添加路由的主流，3.0+版本的 <code>addRoute & addRoutes</code> 两个方法并存，但 4.0+ 中看 <code>addRoutes</code> 方法已经被删除了，先看使用吧。</p>
<p><code>addRoute</code> 有两个参数，也是 2 种用法：</p>
<ul>
<li>添加一条新路由规则。如果该路由规则有 <code>name</code>，并且已经存在一个与之相同的名字，则会覆盖它。</li>
<li>添加一条新路由规则记录作为现有路由的子路由。如果该路由规则有 <code>name</code>，并且已经存在一个与之相同的名字，则会覆盖它。</li>
</ul>
<p>白话一下。第一种就是传入一个路由配置对象，注意，不是之前的 <code>routes</code> 数组了，是只有一个路由配置的对象，当然你可以在这个路由配置下写无数个子路由，但是添加的时候只能传入一个路由对象这种形式添加，一次只追加一条记录，如果当前的路由配置中存在 <code>name</code> 相同的记录，则会覆盖掉，如下：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-built_in">this</span>.$router.addRoute(&#123;
  <span class="hljs-attr">path</span>: <span class="hljs-string">"/parent"</span>,
  <span class="hljs-attr">name</span>: <span class="hljs-string">"Parent"</span>,
  component,
  <span class="hljs-attr">children</span>:[
    &#123;
      <span class="hljs-attr">path</span>: <span class="hljs-string">"child"</span>
      <span class="hljs-comment">// ...</span>
    &#125;,
    <span class="hljs-comment">// ...</span>
  ]
&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>第二种就是两个参数，第一个参数为一个已经存在的路由 <code>name</code> ，第二个参数为一个路由配置对象，就和上那种使用方式的路由配置对象一致，只是，这种方式会把这个路由配置对象当作第一个参数 <code>name</code> 对应的路由对象的子路由追加进去，简单说就是根据路由 <code>name</code> 定向添加子路由，添加过程中有重复路由 <code>name</code> 也是覆盖掉。</p>
<p>看着复杂，写起来其实很简单，再为 <code>createRouteMap</code> 加一个 <code>parent</code> 参数即可。修改 <code>createRouteMap</code> 函数：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// 新增 parentRoute 参数</span>
<span class="hljs-keyword">export</span> <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">createRouteMap</span>(<span class="hljs-params">routes, oldPathMap, parentRoute</span>)</span>&#123;  
  <span class="hljs-keyword">const</span> pathMap = oldPathMap || <span class="hljs-built_in">Object</span>.create(<span class="hljs-literal">null</span>);

  routes.forEach(<span class="hljs-function"><span class="hljs-params">route</span> =></span> &#123;
    <span class="hljs-comment">// addRouteRecord(pathMap, route, null) old</span>
    addRouteRecord(pathMap, route, parentRoute) <span class="hljs-comment">// new</span>
  &#125;)
  <span class="hljs-keyword">return</span> pathMap
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>如上所示，第三个参数代表父级路由，需要追加到一条记录上时，只需拿到这个父级路由传入即可，没有第三个参数时默认为 <code>undefined</code> 也不会影响下面逻辑。</p>
<p>接下来写 <code>addRoute</code> 方法：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// 动态添加路由（添加一条新路由规则）</span>
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">addRoute</span>(<span class="hljs-params">parentOrRoute, route</span>)</span>&#123;
  <span class="hljs-keyword">const</span> parent = (<span class="hljs-keyword">typeof</span> parentOrRoute !== <span class="hljs-string">'object'</span>) ? pathMap[parentOrRoute] : <span class="hljs-literal">undefined</span>
  createRouteMap([route || parentOrRoute], pathMap, parent)
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>如上，<code>addRoute</code> 方法第一个参数有可能是个字符串，也可能是个路由对象，而 <code>createRouteMap</code> 方法第一个参数是路由数组，所以我们调用时直接数组包裹，默认是第二个参数，第二个参数不存在拿第一个参数就是路由对象，然后传入旧的 pathMap 对象，最后的 parent 我们需要在函数开始就判断一下。</p>
<p>当第一个参数不是一个对象时，也就是输入的是一个路由 <code>name</code> 字符串，我们这里稍微改动一下，用路由 <code>path</code> 代替（明白意思就行），直接通过之前解析好的 pathMap 对象取出规格化路由赋值给 parent，如果是一个对象，那就肯定只有一个参数了，直接给 parent 赋值为 undefined，完美。</p>
<blockquote>
<p>解释下为什么不像官方那样用路由 <code>name</code> 匹配，源码中除了 pathMap 对象，还解析了一个 namePath 对象，我们写的是一个简化版，这些类似的东西包括对路由名称、路由别名、重定向参数、动态路由的处理我都省略了，做一个路由 path 的处理大家理解即可，其他处理大多一致，都很简单，不过瘾可以配合我打上注释的源码自行补全，整体架构都一致，无非是多加一些代码。</p>
</blockquote>
<h4 data-id="heading-19">match路由匹配核心实现</h4>
<p>最后是路由匹配函数 <code>match</code> 方法，也很简单：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// 路由匹配</span>
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">match</span>(<span class="hljs-params">location</span>)</span>&#123;
  location = <span class="hljs-keyword">typeof</span> location === <span class="hljs-string">'string'</span> ? &#123; <span class="hljs-attr">path</span>: location &#125; : location
  <span class="hljs-keyword">return</span> pathMap[location.path]
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><code>match</code> 方法我们给它一个参数，这个参数可以是字符串，也可以是个必须带有 path 属性的对象，因为必须要使用 path 才能匹配到配置的路由模块数据，使用如下：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// String | Object</span>

match(<span class="hljs-string">"/home"</span>)
match(&#123;<span class="hljs-attr">path</span>: <span class="hljs-string">"/home"</span>&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>在函数最开始校验了一下参数类型并统一转为对象，随后直接返回了 pathMap 的 path 映射，是不是很简单？别着急，这块后续还要优化。</p>
<h3 data-id="heading-20">createMatcher的使用及实例方法挂载</h3>
<p>回顾一下我们在 <code>createMatcher</code> 方法中做了哪些事情，其实主要是生成了一个路由映射对象 <code>pathMap</code>，返回了四个函数：</p>
<ul>
<li>addRoutes</li>
<li>getRoutes</li>
<li>addRoute</li>
<li>match</li>
</ul>
<p>对于这几个方法，其实最后都要挂载在 VueRouter 实例上，因为使用时是 <code>this.$router.addRoute()</code> 这种方式，这里只是核心实现，后续还要在实例挂载，其中  <code>match</code> 方法后续还有优化。</p>
<p>所以，来看看 <code>createMatcher</code> 函数的使用和这几个实例方法的挂载，再次回到 VueRouter 类这里：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> <span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">VueRouter</span>()</span>&#123;
  <span class="hljs-function"><span class="hljs-title">constructor</span>(<span class="hljs-params">options</span>)</span> &#123;
    <span class="hljs-built_in">this</span>.options = options;
    <span class="hljs-comment">// 创建路由matcher对象，传入routes路由配置列表及VueRouter实例，主要负责url匹配</span>
    <span class="hljs-built_in">this</span>.matcher = createMatcher(options.routes);
    
    <span class="hljs-comment">// ...</span>
  &#125;
  
  <span class="hljs-comment">// 匹配路由</span>
  <span class="hljs-function"><span class="hljs-title">match</span>(<span class="hljs-params">location</span>)</span> &#123;
    <span class="hljs-keyword">return</span> <span class="hljs-built_in">this</span>.matcher.match(location)
  &#125;
  
  <span class="hljs-comment">// 获取所有活跃的路由记录列表</span>
  <span class="hljs-function"><span class="hljs-title">getRoutes</span>(<span class="hljs-params"></span>)</span> &#123;
    <span class="hljs-keyword">return</span> <span class="hljs-built_in">this</span>.matcher.getRoutes()
  &#125;
  
  <span class="hljs-comment">// 动态添加路由（添加一条新路由规则）</span>
  <span class="hljs-function"><span class="hljs-title">addRoute</span>(<span class="hljs-params">parentOrRoute, route</span>)</span> &#123;
    <span class="hljs-built_in">this</span>.matcher.addRoute(parentOrRoute, route)
  &#125;
  
  <span class="hljs-comment">// 动态添加路由（参数必须是一个符合 routes 选项要求的数组）</span>
  <span class="hljs-function"><span class="hljs-title">addRoutes</span>(<span class="hljs-params">routes</span>)</span> &#123;
    <span class="hljs-built_in">this</span>.matcher.addRoutes(routes)
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>如上，我们直接在 VueRouter 类的 constructor 里调用了 <code>createMatcher</code> 函数，并将其返回值挂载到了实例的 matcher 属性上，其实这个对象就包含那四个方法，接着挂载这几个方法到实例上，不赘述了。</p>
<p>现在 VueRouter 实例上就有这些方法了，而 <code>this.$router</code> 在 install 中做了代理到 VueRouter 实例的操作，所以就可以使用这些方法了。</p>
<h2 data-id="heading-21">路由模式父类History实现</h2>
<p>路由匹配器实现告一段落，还记得在 VueRouter 类 constructor 中除了路由匹配器，还有什么吗？没错，校验了传入的 mode 参数，并且通过判断分别为三种模式创建了一个类并实例化后统一挂载到了 VueRouter 实例的 history 属性上。</p>
<p>那下面我们就逐一实现这几个类，分别是 <code>HTML5History | HashHistory | AbstractHistory</code>。首先在 <code>src/hello-vue-router/</code> 文件夹下新建 <code>history/</code> 的文件夹，在这此文件夹下新建三个文件，对应三种模式构建类：</p>
<ul>
<li>hash.js</li>
<li>html5.js</li>
<li>abstract.js</li>
</ul>
<p>接下来先给三个路由模式类定义一个父类。</p>
<p>思考：为什么要定义父类？</p>
<p>其实在初始化实例上 <code>this.history</code> 挂载的一些方法都是一致的，虽然实现方式上几种模式可能不太一致，但不能给用户增加负担，所以使用要统一，为了节省代码以及统一，我们可以定义一个父类，让三个子类都继承这个父类。</p>
<p>So，在刚刚新建子类的 <code>history/</code> 文件夹下，新建一个 <code>base.js</code> 文件并导出一个 History 类：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">/*
 * @path: src/hello-vue-router/history/base.js
 * @Description: 路由模式父类
 */</span>

<span class="hljs-keyword">export</span> <span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">History</span> </span>&#123;
  <span class="hljs-function"><span class="hljs-title">constructor</span>(<span class="hljs-params">router</span>)</span> &#123;
    <span class="hljs-built_in">this</span>.router = router;
    <span class="hljs-comment">// 当前路由route对象</span>
    <span class="hljs-built_in">this</span>.current = &#123;&#125;;
    <span class="hljs-comment">// 路由监听器数组，存放路由监听销毁方法</span>
    <span class="hljs-built_in">this</span>.listeners = [];
  &#125;
  
  <span class="hljs-comment">// 启动路由监听</span>
  <span class="hljs-function"><span class="hljs-title">setupListeners</span>(<span class="hljs-params"></span>)</span> &#123; &#125;

  <span class="hljs-comment">// 路由跳转</span>
  <span class="hljs-function"><span class="hljs-title">transitionTo</span>(<span class="hljs-params">location</span>)</span> &#123; &#125;

  <span class="hljs-comment">// 卸载</span>
  <span class="hljs-function"><span class="hljs-title">teardown</span>(<span class="hljs-params"></span>)</span> &#123;
    <span class="hljs-built_in">this</span>.listeners.forEach(<span class="hljs-function">(<span class="hljs-params">cleanupListener</span>) =></span> &#123;
      cleanupListener();
    &#125;);

    <span class="hljs-built_in">this</span>.listeners = [];
    <span class="hljs-built_in">this</span>.current = <span class="hljs-string">""</span>;
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>如上，History 类 constructor 中主要做了三件事：</p>
<ul>
<li>保存传入的路由实例 router</li>
<li>声明了一个当前路由对象 current</li>
<li>声明了一个路由监听器数组，存放路由监听销毁方法</li>
</ul>
<p>然后写了几个公共方法：</p>
<ul>
<li>setupListeners 启动路由监听的方法</li>
<li>transitionTo 路由跳转的方法</li>
<li>teardown 卸载 VueRouter 实例时卸载路由模式类中的监听并清空数据方法</li>
</ul>
<blockquote>
<p>暂时写了这 3 个方法，其实 <code>setupListeners</code> 方法这里只是声明一下，主要逻辑还会在子类中复写， 然后这里只把 <code>teardown</code> 这个卸载的方法完善了，<code>transitionTo</code> 这个路由跳转方法以及后面实现子类过程中需要添加的一些公共方法后续慢慢完善</p>
</blockquote>
<p>先看这个销毁方法，思考为什么要销毁？</p>
<p>其实不论是 hash 或 history 这两种模式在实现过程中肯定都会写一些监听，而当 VueRouter 实例卸载的时候，这些监听并不会被销毁，就会造成内存泄漏，所以我们手动写一个卸载销毁，代码十分简单</p>
<p>首先是维护了一个公共的路由监听器数组 <code>listeners</code> ，将来在子类中每写一个监听事件，直接就写一个卸载监听方法 <code>push</code> 到这个数组中来，当监听到 VueRouter 卸载时，手动调用卸载方法，方法里就是循环调用一下 <code>listeners</code> 数组中的方法从而销毁监听，可以看到卸载方法的最后把 <code>listeners</code> 数组以及当前路由对象 <code>current</code> 都清空了。</p>
<p>保存的 router 实例对象后面会用到，可能大家不了解的应该是 <code>current</code> 这个对象吧，接下来着重介绍。</p>
<p><strong>思考：我们怎么获取当前的路由对象？</strong></p>
<p>答：<code>$route</code></p>
<p><strong>思考：路由对象应该在哪里维护？有什么作用？</strong></p>
<p>先回顾下使用 <code>$route</code> 时，它都有什么属性？</p>
<p>其实它保存着当前路由的 <code>path、hash、meta、query、params</code> 等等一切与当前路由有关的东西其实都在这里存着，并且官方定义这个路由对象是只读的</p>
<p>而 <code>current</code> ，就是当前的意思，它其实就是这个路由对象，每当我们监听到路由 path 改变时，就要同步去修改这个路由对象，而当路由对象改变，<code>router-view</code> 组件需要渲染的视图也要改变，可以说这个路由对象就是整个 VueRouter 的中枢。</p>
<p>可能大家要问，刚刚不是说过这个对象是只读的吗？怎么还会改变？其实路由对象本身是被冻结的，我们只读的是对象中的属性，但是我们可以切换整个路由对象啊！</p>
<p>上面我们为 <code>current</code> 这个路由对象定义的初始值是空对象，其实因为路由对象是一个面向用户、具有固定格式的对象，所以应该由一个统一的方法来创建这个固定格式的路由对象，此方法我们叫它 <code>createRoute</code>。</p>
<h2 data-id="heading-22">createRoute方法</h2>
<p>还是单拿出来一个文件来实现这样一个方法。</p>
<p>在 <code>src/hello-vue-router/</code> 目录下新建一个 <code>utils/</code> 文件夹，在该文件夹下新建一个 <code>route.js</code> 文件，实现并导出一个 <code>createRoute</code> 方法。</p>
<p>先新建好文件，说 <code>createRoute</code> 方法之前，我们思考一下什么时候需要创建这个路由对象？</p>
<p>首先当然是我们的 <code>current</code> 属性初始化的时候需要创建一个空的路由对象，除此之外呢？</p>
<p>捋一下，要让 path 路径改变，有两种方式，一是直接改 URL，二是用 <code>push</code> 方法。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// No.1 oldURL => newURL</span>
<span class="hljs-keyword">let</span> oldURL = <span class="hljs-string">"http://localhost:8081/#/about"</span>
<span class="hljs-keyword">let</span> newURL = <span class="hljs-string">"http://localhost:8081/#/home?a=1"</span>

<span class="hljs-comment">// No.2</span>
<span class="hljs-built_in">this</span>.$router.push(&#123;
  <span class="hljs-attr">path</span>: <span class="hljs-string">"/home"</span>,
  <span class="hljs-attr">query</span>: &#123;<span class="hljs-attr">a</span>: <span class="hljs-number">1</span>&#125;
&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>可以看到，在改变路由时，可附带很多属性，就像官方文档中 <code>push</code> 方法支持的属性就有下面这些，具体作用看文档：</p>
<pre><code class="hljs language-js copyable" lang="js">name
path
hash
query
params
append
replace
<span class="copy-code-btn">复制代码</span></code></pre>
<p>路径改变，要去往一个新的 path，新的 path 加上这些可以携带的属性我们称之为 目标信息对象。而当前路由对象 route 要包含当前路由的所有信息，path 匹配的路由配置对象+目标信息信息对象=所有信息，所有信息格式化后就是当前路由对象 route。</p>
<p>所以更新当前路由对象就需要先通过 path 匹配到路由配置对象，然后路由配置对象和目标信息信息对象合并格式化为 route。在哪里做这样一个更新操作呢？</p>
<p>回顾下之前我们写的 <code>createMatcher</code> 函数，其中返回了一个 match 方法，如下：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// 路由匹配</span>
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">match</span>(<span class="hljs-params">location</span>)</span>&#123;
  location = <span class="hljs-keyword">typeof</span> location === <span class="hljs-string">'string'</span> ? &#123; <span class="hljs-attr">path</span>: location &#125; : location
  <span class="hljs-keyword">return</span> pathMap[location.path]
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这里我们当时返回的是路由配置对象，其实我们的最终目的就是让其匹配到当前路由对象，我们也分析了当前路由对象=路由配置对象+目标信息对象，所以直接匹配到路由对象的话就是最完整的数据，现在改写这个方法：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">/*
 * @path: src/hello-vue-router/create-route-map.js
 * @Description: 路由匹配器Matcher对象生成方法
 */</span>
<span class="hljs-keyword">import</span> &#123; createRouteMap &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">"./create-route-map"</span>;
<span class="hljs-comment">// 导入route对象创建方法</span>
<span class="hljs-keyword">import</span> &#123; createRoute &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">"./utils/route"</span>

<span class="hljs-keyword">export</span> <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">createMatcher</span>(<span class="hljs-params">routes</span>)</span>&#123;
  <span class="hljs-keyword">const</span> pathMap = createRouteMap(routes)
  
  <span class="hljs-comment">// 路由匹配</span>
  <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">match</span>(<span class="hljs-params">location</span>)</span>&#123;
    location = <span class="hljs-keyword">typeof</span> location === <span class="hljs-string">'string'</span> ? &#123; <span class="hljs-attr">path</span>: location &#125; : location
    <span class="hljs-keyword">return</span> createRoute(pathMap[location.path], location) <span class="hljs-comment">// 修改</span>
  &#125;
  
  <span class="hljs-comment">// ...</span>
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>如上，在 <code>createMatcher</code> 函数返回的 <code>match</code> 方法中，直接创建一个新路由对象返回。分析到这里我们就可以确定 <code>createRoute</code> 函数的参数了，就如同上面 <code>createRoute</code> 方法里有 2 个参数，第一个就是路由匹配对象 record，第二个就是目标信息对象 location（这也是为什么我们给 match 方法的参数起名为 location 并允许它有对象和字符串两种格式的原因）。</p>
<p>我们经常使用的 <code>push</code> 方法其实其中的参数就是 location 对象，既可以是字符串路径，也可以是对象，为对象时可传入的属性就和上面 push 方法可配置的那些属性是一致的</p>
<p>不过上面写的属性中 <code>append、replace</code> 是两个是附加功能，需要额外解析， <code>push</code> 方法支持，<code>router-link</code> 组件同样支持，作用看下面文档，我们暂时省略这两个参数的解析，因为不是核心逻辑。</p>
<ul>
<li><a href="https://link.juejin.cn/?target=https%3A%2F%2Frouter.vuejs.org%2Fzh%2Fapi%2F%23append" target="_blank" rel="nofollow noopener noreferrer" title="https://router.vuejs.org/zh/api/#append" ref="nofollow noopener noreferrer">router.vuejs.org/zh/api/#app…</a></li>
<li><a href="https://link.juejin.cn/?target=https%3A%2F%2Frouter.vuejs.org%2Fzh%2Fapi%2F%23replace" target="_blank" rel="nofollow noopener noreferrer" title="https://router.vuejs.org/zh/api/#replace" ref="nofollow noopener noreferrer">router.vuejs.org/zh/api/#rep…</a></li>
</ul>
<p>分析准备就绪，可以开始实现 <code>createRoute</code> 方法了，老规矩，先看整体代码，再逐步分析：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">/*
 * @path: src/hello-vue-router/utils/route.js
 * @Description: route对象相关方法
 */</span>
<span class="hljs-keyword">export</span> <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">createRoute</span>(<span class="hljs-params">record, location</span>) </span>&#123;
  <span class="hljs-keyword">let</span> route = &#123;
    <span class="hljs-attr">name</span>: location.name || (record && record.name),
    <span class="hljs-attr">meta</span>: (record && record.meta) || &#123;&#125;,
    <span class="hljs-attr">path</span>: location.path || <span class="hljs-string">"/"</span>,
    <span class="hljs-attr">hash</span>: location.hash || <span class="hljs-string">""</span>,
    <span class="hljs-attr">query</span>: location.query || &#123;&#125;,
    <span class="hljs-attr">params</span>: location.params || &#123;&#125;,
    <span class="hljs-attr">fullPath</span>: location.path || <span class="hljs-string">"/"</span>,
    <span class="hljs-attr">matched</span>: record && formatMatch(record),
  &#125;;
  <span class="hljs-keyword">return</span> <span class="hljs-built_in">Object</span>.freeze(route);
&#125;

<span class="hljs-comment">// 初始状态的起始路由</span>
<span class="hljs-keyword">export</span> <span class="hljs-keyword">const</span> START = createRoute(<span class="hljs-literal">null</span>, &#123;
  <span class="hljs-attr">path</span>: <span class="hljs-string">'/'</span>
&#125;)

<span class="hljs-comment">// 关联所有路由记录</span>
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">formatMatch</span>(<span class="hljs-params">record</span>) </span>&#123;
  <span class="hljs-keyword">const</span> res = []
  <span class="hljs-keyword">while</span> (record) &#123;
    <span class="hljs-comment">// 队列头添加，所以父record永远在前面，当前record永远在最后</span>
    <span class="hljs-comment">// 在router-view组件中获取匹配的route record时会用到</span>
    <span class="hljs-comment">// 精准匹配到路由记录是数组最后一个</span>
    res.unshift(record)
    record = record.parent
  &#125;
  <span class="hljs-keyword">return</span> res
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>如上，<code>createRoute</code> 方法里通过两个参数互相取一些值来构建 route 对象。这里需要注意的有两个地方，<code>fullPath</code> 参数其实是一个 path+qs+hash 的完整路径，但是这里我们只写了path，先不考虑参数的问题。</p>
<p>还有 <code>matched</code> 这个属性，我们直接写了一个 <code>formatMatch</code> 函数生成，函数中只做了一件事，拿到当前 path 关联的所有路由配置对象。</p>
<p>函数行参 <code>record</code> 就是路由配置对象，生成路由配置对象的时候，我们为其添加了 parent 属性，指向其父路由，不记得就回顾一下 <code>createRouteMap</code> 方法。 <code>formatMatch</code> 函数里就是递归找当前路径包括它的父级路由配置对象，组成一个数组即 <code>matched</code> 参数，举个例子，如下这个路由配置：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">let</span> routes = [
   &#123;
    <span class="hljs-attr">path</span>: <span class="hljs-string">"/parent"</span>,
    <span class="hljs-attr">name</span>: <span class="hljs-string">"Parent"</span>,
    component,
    <span class="hljs-attr">children</span>:[
      &#123;
        <span class="hljs-attr">path</span>: <span class="hljs-string">"child"</span>,
        <span class="hljs-attr">name</span>:<span class="hljs-string">"Child"</span>,
        component,
      &#125;
    ]
  &#125;
]
<span class="copy-code-btn">复制代码</span></code></pre>
<p>那么此路由配置解析成 pathMap 如下：</p>
<pre><code class="hljs language-js copyable" lang="js">pathMap = &#123;
  <span class="hljs-string">"/parent"</span>: &#123;<span class="hljs-attr">path</span>:<span class="hljs-string">"/parent"</span>, ...&#125;,
  <span class="hljs-string">"/parent/child"</span>: &#123;<span class="hljs-attr">path</span>:<span class="hljs-string">"/parent/child"</span>, ...&#125;,
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>假如要跳转的新 path 是 <code>/parent/child</code>，生成 route 时，经过 <code>formatMatch</code> 方法关联它的所有路由记录，最终该路由对象的 <code>matched</code> 属性就是下面这样：</p>
<pre><code class="hljs language-js copyable" lang="js">[
  &#123;<span class="hljs-attr">path</span>:<span class="hljs-string">"/parent"</span>, component, parent ...&#125;,
  &#123;<span class="hljs-attr">path</span>:<span class="hljs-string">"/parent/child"</span>, component, parent ...&#125;
]
<span class="copy-code-btn">复制代码</span></code></pre>
<p>注意，因为 <code>formatMatch</code> 函数递归查找父级时，我们使用的是 <code>unshift</code> 方法，所以最终的数组最后一项一定是当前 path 的模块。</p>
<p>这里其实是为嵌套路由做准备，因为当存在嵌套路由，子路由记录被匹配到时，其实代表着父路由记录也一定被匹配到了。例如匹配 /foo/bar， 当 /foo/bar 本身被匹配了，其父路由对象 /foo 肯定也匹配了，最终匹配结果如下：</p>
<pre><code class="hljs language-js copyable" lang="js">metched = [&#123;<span class="hljs-attr">path</span>:<span class="hljs-string">"/foo"</span>, ...&#125;,&#123;<span class="hljs-attr">path</span>:<span class="hljs-string">"/foo/bar"</span>&#125;] 
<span class="hljs-comment">// “/foo/bar” 本身匹配模块在数组最后，而第一项是顶级路由匹配项</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>总结来说，路由对象的 <code>matched</code> 属性是一个数组，数组项是匹配到的路由配置对象，数组项顺序依次是顶级路由匹配对象到当前子级路由本身匹配对象，到此一个简单的路由生成函数就 OK 了。</p>
<p>思路切回 History 类，<code>current</code> 对象我们还没为其赋初始路由值呢，所以，我们在 <code>route.js</code> 文件中还写了一个初始化路由对象并导出，调用了一下 <code>createRoute</code> 方法，参数一置空，参数二只写一个 path 属性值为 <code>"/"</code> 的对象：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// 初始状态的起始路由</span>
<span class="hljs-keyword">export</span> <span class="hljs-keyword">const</span> START = createRoute(<span class="hljs-literal">null</span>, &#123;
  <span class="hljs-attr">path</span>: <span class="hljs-string">'/'</span>
&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>最后修改一下 <code>base.js</code> 文件中的 History 类，将路由对象初始值 <code>START</code> 导入并赋值给 <code>current</code> ：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// 导入初始化route对象</span>
<span class="hljs-keyword">import</span> &#123; START &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">"../utils/route"</span>;

<span class="hljs-keyword">export</span> <span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">History</span> </span>&#123;
  <span class="hljs-function"><span class="hljs-title">constructor</span>(<span class="hljs-params">router</span>)</span> &#123;
    <span class="hljs-built_in">this</span>.router = router;
    
    <span class="hljs-comment">// 当前路由route对象</span>
    <span class="hljs-comment">//     this.current = &#123;&#125;;</span>
    <span class="hljs-comment">// =>  this.current = START;</span>
    <span class="hljs-built_in">this</span>.current = START;
    
    <span class="hljs-built_in">this</span>.listeners = [];
  &#125;
  
 <span class="hljs-comment">// ...</span>
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>到这里，父类中的 <code>transitionTo</code> 即路由跳转方法就可以继续补充了，调用路由跳转方法就会传入一个目标信息对象，这时应该做什么？</p>
<ul>
<li>
<p>更新路由对象 <code>current</code></p>
</li>
<li>
<p>更新 URL</p>
</li>
<li>
<p>更新视图</p>
</li>
</ul>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// 路由跳转</span>
<span class="hljs-function"><span class="hljs-title">transitionTo</span>(<span class="hljs-params">location, onComplete</span>)</span> &#123;
  <span class="hljs-comment">// 路由匹配，解析location匹配到其路由对应的数据对象</span>
  <span class="hljs-keyword">let</span> route = <span class="hljs-built_in">this</span>.router.match(location);

  <span class="hljs-comment">// 更新current</span>
  <span class="hljs-built_in">this</span>.current = route;

  <span class="hljs-comment">// 更新URL</span>
  <span class="hljs-built_in">this</span>.ensureURL()

  <span class="hljs-comment">// 跳转成功抛出回调</span>
  onComplete && onComplete(route)
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>如上，路由跳转方法 <code>transitionTo</code> 其实传入的就是 location 对象，<code>push</code> 方法也是基于此方法实现的。</p>
<p>那新的目标信息对象来了，我们首先就要构建一个新的路由对象，History 是一个父类，后面我们还会写子类，子类继承父类，子类在初始化实例的时候（index.js文件 mode 参数判断那块）其实传入了当前 VueRouter 实例，所以我们父类也可以接收到，也就是我们父类 constructor 中的 <code>router</code> 参数，我们将它直接挂在了父类实例属性 <code>router</code> 上，这样我们就可以通过 <code>this.router</code> 获取到 VueRouter 实例。</p>
<p>VueRouter 实例上我们挂载了 match 方法还记得吗？不记得回顾下代码。</p>
<p>我们使用 <code>this.router.match</code> 方法，传入 location 参数，就可以生成一个新的路由对象，最后将新的路由对象赋值给 <code>current</code> 属性。</p>
<p>OK，按照我们的逻辑，路由改变生成新的路由对象并赋值给 <code>current</code> 就完成了，还剩下更新URL以及更新视图。</p>
<p><strong>思考：为什么更新URL？</strong></p>
<p>其实直接修改 URL 来跳转，并不需要更新 URL，但如果使用 API 来做路由跳转，例如 <code>push</code> 方法，我们在代码中可以控制更新路由对象 <code>current</code> ，也可以更新视图，但是 URL 并没有改变，所以我们还需要更新 URL。</p>
<p>那么问题来了，怎么更新 URL？</p>
<p>可以看到上面代码中我们调用了 <code>ensureURL</code> 方法来更新，而且是 <code>this</code> 调用的，其实这个方法并不在父类上，而在子类。</p>
<p>为什么将 <code>ensureURL</code> 方法写在子类？</p>
<p>因为我们存在 3 种模式，不同模式替换 URL 的方式是不同的，所以各个子类上写自己的 URL 更新方法最好了。</p>
<p>为什么这里可以调用子类方法？</p>
<p>因为初始化实例的是子类，子类又继承父类，可以理解为父类的方法以及属性都被子类继承了，<code>transitionTo</code> 方法当然也被继承了，那在调用这个跳转方法时，内部的 <code>this</code> 指向就是子类，所以可直接调用子类方法。</p>
<p>至于视图更新，因为目前还没有完善 <code>router-view</code> 组件，子类也没写好，所以我们放到后面完善。</p>
<p>最后抛出跳转成功的回调，并传入当前 route 对象参数。</p>
<h2 data-id="heading-23">路由模式子类初步构建</h2>
<p>我们先把三种模式子类初步构建一下，其实就是在三个文件中创建不同的子类，并让他们都继承父类，后面我们一一实现。</p>
<p>hash.js</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">import</span> &#123; History &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'./base'</span>

<span class="hljs-keyword">export</span> <span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">HashHistory</span> <span class="hljs-keyword">extends</span> <span class="hljs-title">History</span> </span>&#123;
  <span class="hljs-function"><span class="hljs-title">constructor</span>(<span class="hljs-params">router</span>)</span>&#123;
    <span class="hljs-built_in">super</span>(router);
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>html5.js</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">import</span> &#123; History &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'./base'</span>

<span class="hljs-keyword">export</span> <span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">HTML5History</span> <span class="hljs-keyword">extends</span> <span class="hljs-title">History</span> </span>&#123;
  <span class="hljs-function"><span class="hljs-title">constructor</span>(<span class="hljs-params">router</span>)</span>&#123;
    <span class="hljs-built_in">super</span>(router);
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>abstract.js</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">import</span> &#123; History &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'./base'</span>

<span class="hljs-keyword">export</span> <span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">AbstractHistory</span> <span class="hljs-keyword">extends</span> <span class="hljs-title">History</span> </span>&#123;
  <span class="hljs-function"><span class="hljs-title">constructor</span>(<span class="hljs-params">router</span>)</span>&#123;
    <span class="hljs-built_in">super</span>(router);
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-24">HashHistory类实现</h2>
<p>来到 <code>history/</code> 的文件夹下的 <code>hash.js</code> 文件，我们先实现 HashHistory 类：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">/*
 * @path: src/hello-vue-router/index.js
 * @Description: 路由模式HashHistory子类
 */</span>
<span class="hljs-keyword">import</span> &#123; History &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'./base'</span>;

<span class="hljs-keyword">export</span> <span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">HashHistory</span> <span class="hljs-keyword">extends</span> <span class="hljs-title">History</span> </span>&#123;
  <span class="hljs-function"><span class="hljs-title">constructor</span>(<span class="hljs-params">router</span>)</span> &#123;
    <span class="hljs-comment">// 继承父类</span>
    <span class="hljs-built_in">super</span>(router);
  &#125;
  
  <span class="hljs-comment">// 启动路由监听</span>
  <span class="hljs-function"><span class="hljs-title">setupListeners</span>(<span class="hljs-params"></span>)</span> &#123;
    <span class="hljs-comment">// 路由监听回调</span>
    <span class="hljs-keyword">const</span> handleRoutingEvent = <span class="hljs-function">() =></span> &#123;
      <span class="hljs-keyword">let</span> location = getHash();
      <span class="hljs-built_in">this</span>.transitionTo(location, <span class="hljs-function">() =></span> &#123;
        <span class="hljs-built_in">console</span>.log(<span class="hljs-string">`Hash路由监听跳转成功！`</span>);
      &#125;);
    &#125;;

    <span class="hljs-built_in">window</span>.addEventListener(<span class="hljs-string">"hashchange"</span>, handleRoutingEvent);
    <span class="hljs-built_in">this</span>.listeners.push(<span class="hljs-function">() =></span> &#123;
      <span class="hljs-built_in">window</span>.removeEventListener(<span class="hljs-string">"hashchange"</span>, handleRoutingEvent);
    &#125;);
  &#125;
&#125;

<span class="hljs-comment">// 获取location hash路由</span>
<span class="hljs-keyword">export</span> <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">getHash</span>(<span class="hljs-params"></span>) </span>&#123;
  <span class="hljs-keyword">let</span> href = <span class="hljs-built_in">window</span>.location.href;
  <span class="hljs-keyword">const</span> index = href.indexOf(<span class="hljs-string">"#"</span>);
  <span class="hljs-keyword">if</span> (index < <span class="hljs-number">0</span>) <span class="hljs-keyword">return</span> <span class="hljs-string">"/"</span>;

  href = href.slice(index + <span class="hljs-number">1</span>);

  <span class="hljs-keyword">return</span> href;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>如上，我们让 HashHistory 类继承 History 类，子类也就继承了父类的一切。我们先实现了 hash 模式下的 <code>setupListeners</code> 方法，即启动路由监听方法。</p>
<p>来看一下其中的逻辑，主要就是监听了 <code>hashchange</code> 事件，也就是当 hash 路由改变，就会触发其回调。</p>
<p><strong>思考：监听到路由path改变了我们需要做什么？</strong></p>
<p>path 变了需要更新当前路由对象、更新视图等等，这个步骤我们前面做过，没错，就是 <code>transitionTo</code> 跳转方法里做的，所以我们直接在监听到路由改变时调用路由跳转方法即可。</p>
<p>所以回调中先是通过一个 <code>getHash</code> 的工具函数获取到当前 hash 值，返回 hash 路由 path，这个方法简单，不赘述。拿到 path 后接着调用 <code>transitionTo</code> 方法。</p>
<p>另外，在启动监听后，我们向 <code>listeners</code> 数组（继承父类）中 <code>push</code> 了一个销毁监听的方法，用于卸载时销毁监听事件，这点上面也说过了。</p>
<p>接下来补充一下子类的方法：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">export</span> <span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">HashHistory</span> <span class="hljs-keyword">extends</span> <span class="hljs-title">History</span> </span>&#123;
  <span class="hljs-function"><span class="hljs-title">constructor</span>(<span class="hljs-params">router</span>)</span> &#123;
    <span class="hljs-comment">// 继承父类</span>
    <span class="hljs-built_in">super</span>(router);
  &#125;
  
  <span class="hljs-comment">// 启动路由监听</span>
  <span class="hljs-function"><span class="hljs-title">setupListeners</span>(<span class="hljs-params"></span>)</span> &#123; <span class="hljs-comment">/** ... **/</span> &#125;
  
  <span class="hljs-comment">// 更新URL</span>
  <span class="hljs-function"><span class="hljs-title">ensureURL</span>(<span class="hljs-params"></span>)</span> &#123;
    <span class="hljs-built_in">window</span>.location.hash = <span class="hljs-built_in">this</span>.current.fullPath;
  &#125;
  
  <span class="hljs-comment">// 路由跳转方法</span>
  <span class="hljs-function"><span class="hljs-title">push</span>(<span class="hljs-params">location, onComplete</span>)</span> &#123;
    <span class="hljs-built_in">this</span>.transitionTo(location, onComplete)
  &#125;

  <span class="hljs-comment">// 路由前进后退</span>
  <span class="hljs-function"><span class="hljs-title">go</span>(<span class="hljs-params">n</span>)</span>&#123;
    <span class="hljs-built_in">window</span>.history.go(n)
  &#125;
  
  <span class="hljs-comment">// 跳转到指定URL，替换history栈中最后一个记录</span>
  <span class="hljs-function"><span class="hljs-title">replace</span>(<span class="hljs-params">location, onComplete</span>)</span> &#123;
    <span class="hljs-built_in">this</span>.transitionTo(location, <span class="hljs-function">(<span class="hljs-params">route</span>) =></span> &#123;
      <span class="hljs-built_in">window</span>.location.replace(getUrl(route.fullPath))
      onComplete && onComplete(route)
    &#125;)
  &#125;

  <span class="hljs-comment">// 获取当前路由</span>
  <span class="hljs-function"><span class="hljs-title">getCurrentLocation</span>(<span class="hljs-params"></span>)</span> &#123;
    <span class="hljs-keyword">return</span> getHash()
  &#125;
&#125;

<span class="hljs-comment">// 获取URL</span>
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">getUrl</span>(<span class="hljs-params">path</span>) </span>&#123;
  <span class="hljs-keyword">const</span> href = <span class="hljs-built_in">window</span>.location.href
  <span class="hljs-keyword">const</span> i = href.indexOf(<span class="hljs-string">'#'</span>)
  <span class="hljs-keyword">const</span> base = i >= <span class="hljs-number">0</span> ? href.slice(<span class="hljs-number">0</span>, i) : href
  <span class="hljs-keyword">return</span> <span class="hljs-string">`<span class="hljs-subst">$&#123;base&#125;</span>#<span class="hljs-subst">$&#123;path&#125;</span>`</span>
&#125;

<span class="hljs-comment">// 获取location hash路由</span>
<span class="hljs-keyword">export</span> <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">getHash</span>(<span class="hljs-params"></span>) </span>&#123; <span class="hljs-comment">/** ... **/</span> &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>我们补充了 5 个方法：</p>
<ul>
<li>
<p>ensureURL</p>
<ul>
<li>更新 URL ，它的实现其实很简单，更新导航栏 URL 的 hash，使用 <code>window.location.hash</code> API 就可以，在父类跳转方法里，更新当前路由对象之后才调用了 <code>ensureURL</code>，而更新后路由对象中的 <code>fullPath</code> 属性就是完整的hash path，所以直接赋值过去就可以了。</li>
</ul>
</li>
<li>
<p>push</p>
<ul>
<li>路由跳转方法，此方法我们在父类早已经实现好了，所以接在 <code>push</code> 中调用父类的 <code>transitionTo</code> 方法进行跳转就好，参数也都一致。</li>
</ul>
</li>
<li>
<p>go</p>
<ul>
<li>路由的前进后退，其实实现的不论是 hash 还是 history 模式跳转，每次跳转都改变了URL，跳转的记录都存放在浏览器的 <code>window.history</code> 栈中，而浏览器也提供了一个 <code>window.history.go</code> 的方法让用做前进后退路由，所以直接调用即可，参数都一致。</li>
</ul>
</li>
<li>
<p>getCurrentLocation</p>
<ul>
<li>获取当前 URL 路由地址，由于这是 hash 类，我们之前实现过一个 <code>getHash</code> 方法来获取 hash 模式下 URL 中的路由，所以返回此方法的调用值即可。</li>
</ul>
</li>
<li>
<p>replace</p>
<ul>
<li>跳转到指定URL，替换history栈中最后一个记录</li>
</ul>
</li>
</ul>
<p>我们重点说 <code>replace</code> 方法：</p>
<p>先说作用，其实也是跳转，只是使用 <code>replace</code> 跳转不会在 <code>window.history</code> 栈中产生记录，也就是当我们从 a 页面使用 <code>push</code> 跳转到 b 页面时，栈中是 <code>[a,b]</code>，再使用 <code>replace</code> 跳转从 b 页面到 c 页面时，栈中还是 <code>[a, b]</code> ，那这个时候我们返回上一个页面，就直接从 c 页面到了 a 页面。</p>
<p>其实我们大概也知道浏览器有 <code>window.location.replace</code> 方法就可以实现此功能，但 VueRouter 中跳转时需要考虑三块更新（路由对象、URL、视图）。</p>
<p>试想，假如我们要 <code>replace</code> 一个新的路由，我们需要怎么做？</p>
<p>先更新当前路由对象，再更新URL，这里的更新要使用 <code>window.location.replace</code> 更新才不会留记录，最后渲染视图。</p>
<p>诶？好像和 <code>transitionTo</code> 中差不多，那我们可以修改 <code>transitionTo</code> 方法，把它原来更新URL的 <code>ensureURL</code> 方法放到跳转成功回调的后面，这样我们调用 <code>transitionTo</code> 方法，在回调中使用 <code>window.location.replace</code> 更新URL就可以了。</p>
<p>你可能会疑问，将 <code>ensureURL</code> 方法放到最后，在回调中 <code>replace</code> 但回调执行完毕还是会调用 <code>ensureURL</code> 方法啊？</p>
<p>其实回调里使用 <code>window.location.replace</code> 更新URL后，URL已经是最新的了，这时再调用 <code>ensureURL</code> 更新URL，由于要更新的URL和当前URL是一致的，所以页面不会跳转。</p>
<p>因为 <code>ensureURL</code> 方法里其实调用的 <code>window.location.hash</code> ，假如当前页面地址为 <code>http://localhost:8080/#/about</code>，我们使用此 API 将其 hash 改为 <code>/about</code>，由于前后 hash 一致，其实等于啥也没做。。。</p>
<p>所以我们修改 <code>transitionTo</code> 方法只需修改其成功回调和更新URL的 <code>ensureURL</code> 方法调用顺序即可，如下：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-title">transitionTo</span>(<span class="hljs-params">location, onComplete</span>)</span> &#123;
  <span class="hljs-keyword">let</span> route = <span class="hljs-built_in">this</span>.router.match(location);
  <span class="hljs-built_in">this</span>.current = route;

  <span class="hljs-comment">// 跳转成功抛出回调 放上面</span>
  onComplete && onComplete(route)
  
  <span class="hljs-comment">// 更新URL 放下面</span>
  <span class="hljs-built_in">this</span>.ensureURL()
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>接着实现 <code>replace</code> 方法：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">export</span> <span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">HashHistory</span> <span class="hljs-keyword">extends</span> <span class="hljs-title">History</span> </span>&#123;

  <span class="hljs-comment">// 跳转到指定URL，替换history栈中最后一个记录</span>
  <span class="hljs-function"><span class="hljs-title">replace</span>(<span class="hljs-params">location, onComplete</span>)</span> &#123;
    <span class="hljs-built_in">this</span>.transitionTo(location, <span class="hljs-function">(<span class="hljs-params">route</span>) =></span> &#123;
      <span class="hljs-built_in">window</span>.location.replace(getUrl(route.fullPath))
      onComplete && onComplete(route)
    &#125;)
  &#125;
  
  <span class="hljs-comment">// ...</span>
&#125;

<span class="hljs-comment">// 获取URL</span>
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">getUrl</span>(<span class="hljs-params">path</span>) </span>&#123;
  <span class="hljs-keyword">const</span> href = <span class="hljs-built_in">window</span>.location.href
  <span class="hljs-keyword">const</span> i = href.indexOf(<span class="hljs-string">'#'</span>)
  <span class="hljs-keyword">const</span> base = i >= <span class="hljs-number">0</span> ? href.slice(<span class="hljs-number">0</span>, i) : href
  <span class="hljs-keyword">return</span> <span class="hljs-string">`<span class="hljs-subst">$&#123;base&#125;</span>#<span class="hljs-subst">$&#123;path&#125;</span>`</span>
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>如上，调用 <code>transitionTo</code> 方法，在其回调中 <code>window.location.replace</code> 一下就可以了</p>
<p>注意这里我们又写了一个工具方法，<code>getUrl</code> ，其实就是传入 hash path，返回完整的新 URL 路径，常规操作，不赘述。</p>
<p>到了这里，其实我们的 <code>HashHitory</code> 子类就差不多 OK 了。</p>
<p>接下来就是流程打通了。</p>
<p>之前在 VueRouter 类的实现中，我们只是初始化了各个路由模块子类，但是还没有开启路由监听，注意子类里启动监听的方法是 <code>setupListeners</code> ，再次回到 <code>src/hello-vue-router/index.js</code> 文件，即 VueRouter 类中，给它添加一个初始化方法。</p>
<h2 data-id="heading-25">VueRouter实例初始化</h2>
<h3 data-id="heading-26">初始化方法构建</h3>
<p>思考：VueRouter类初始化时应该做什么？</p>
<p>当然是启动路由模式类的监听，既然启动了监听，那必然要挂载一下销毁。</p>
<p>思考：什么时候销毁？</p>
<p>什么时候不需要监听什么时候销毁！！Vue根实例卸载后就不需要监听了，所以我们监听一下Vue根实例的卸载就可以了。</p>
<p>问题是我们在外部要怎么监听一个Vue实例的卸载？</p>
<p>诶！<code>hook:</code> 前缀的特殊事件监听就派上用场了，Vue官方支持。</p>
<p><strong>小 Tips：</strong><code>hook:</code> <strong>前缀的特殊事件监听</strong></p>
<p>源码中生命周期钩子函数是通过 <code>callHook</code> 函数去调用的， <code>callHook</code> 函数中有一个 <code>vm._hasHookEvent</code> 的判断，当它为 <code>true</code> 的情况下，有着 <code>hook:</code> 特殊前缀的事件，会在对应的生命周期当中执行。</p>
<p>组件中监听事件解析后会使用 <code>$on</code> 注册事件回调，使用 <code>$on</code> 或 <code>$once</code> 监听事件时，如事件名以 <code>hook:</code> 作为前缀，那这个事件会被当做 <code>hookEvent</code>，注册事件回调的同时，<code>vm._hasHookEvent</code> 会被置为 <code>true</code>，后当使用 <code>callHook</code> 调用生命周期函数时，由于 <code>_hasHookEvent</code> 为 <code>true</code>，会直接执行 <code>$emit('hook:xxx')</code>，所以注册的生命周期函数就会执行。</p>
<ul>
<li>在模板中通过 <code>@hook:created</code> 这种形式注册。</li>
<li>JS 中可通过<code>vm.$on('hook:created', cb)</code> 或者 <code>vm.$once('hook:created', cb)</code> 注册，vm 指当前组件实例。</li>
</ul>
<p>一道经典的面试题，<strong>如何在父组件中监听子组件生命周期</strong>，答案就是在父组件中获取到子组件实例（vm），然后通过注册<code>hook:</code> 前缀+生命周期钩子的特殊事件监听就可以了。</p>
<p>这里我们要监听根实例，所以要拿到根实例对象再注册监听，监听销毁事件我们没必要使用 <code>$on</code> ，用 <code>$once</code> 就可以，这样只触发一次，触发之后监听器就会被移除，如下：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// vm 为根实例对象</span>
vm.$once(<span class="hljs-string">"hook:destroyed"</span>, <span class="hljs-function">() =></span> &#123;&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>知道了这些问题，继续实现 init 方法，既然要拿到根实例对象，那 <code>init</code> 方法的参数就有了，分析完毕，开始写代码吧！</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> <span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">VueRouter</span></span>&#123;
  
<span class="hljs-function"><span class="hljs-title">init</span>(<span class="hljs-params">app</span>)</span> &#123;
    <span class="hljs-comment">// 绑定destroyed hook，避免内存泄露</span>
    app.$once(<span class="hljs-string">'hook:destroyed'</span>, <span class="hljs-function">() =></span> &#123;
      <span class="hljs-built_in">this</span>.app = <span class="hljs-literal">null</span>

      <span class="hljs-keyword">if</span> (!<span class="hljs-built_in">this</span>.app) <span class="hljs-built_in">this</span>.history.teardown()
    &#125;)

    <span class="hljs-comment">// 存在即不需要重复监听路由</span>
    <span class="hljs-keyword">if</span> (<span class="hljs-built_in">this</span>.app) <span class="hljs-keyword">return</span>;

    <span class="hljs-built_in">this</span>.app = app;

    <span class="hljs-comment">// 启动监听</span>
    <span class="hljs-built_in">this</span>.history.setupListeners();
  &#125;
  
  <span class="hljs-comment">// ...</span>
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>如上，其实很简单，<code>init</code> 方法传入了一个 app 参数，即 Vue 根实例，方法里判断了 <code>this.app</code> 是否存在，存在直接返回代表已经注册过监听，不存在则将实例赋值给了 VueRouter 类的 app 属性上，最后调用 VueRouter 实例 <code>history</code> 属性的 <code>setupListeners</code> 方法启动监听。</p>
<p><code>history</code> 就是我们在 <code>constructor</code> 里初始化的路由模式类实例，<code>constructor</code> 构造器在 <code>new VueRouter</code> 的时候就会执行，所以我们完全可以拿到 <code>history</code> 实例。</p>
<p>而注册的销毁监听也很简单，就是上面说过的使用根实例的 <code>$once</code> 注册一个 <code>hook:destroyed</code> 监听，回调中将 app 属性置空并调用 <code>history</code> 实例的卸载方法 <code>teardown</code> ，此方法是在路由模式父类中实现的，忘了的话可以回看一下。</p>
<p>OK，<code>init</code> 方法暂时写完了，我们要在什么时候调用它呢？</p>
<h3 data-id="heading-27">初始化方法调用</h3>
<p>因为 init 方法中还有启动监听，所以需要在一切都初始化好了再调用，并且这个时候还要能拿到 Vue 根实例。</p>
<p>回顾我们上面所有环节，能拿到根实例的地方只有插件安装 install 方法 <code>mixin</code> 混入的时候了。</p>
<p>所以，在 <code>src/hello-vue-router/install.js</code> 文件 install 方法的 <code>mixin</code> 中添加执行路由组件初始化方法：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">/*
 * @path: src/hello-vue-router/install.js
 * @Description: 入口文件 VueRouter类
 */</span>
<span class="hljs-keyword">export</span> <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">install</span>(<span class="hljs-params">Vue</span>)</span>&#123;
  
  Vue.mixin(&#123;
    <span class="hljs-function"><span class="hljs-title">beforeCreate</span>(<span class="hljs-params"></span>)</span> &#123;
      <span class="hljs-keyword">if</span> (<span class="hljs-built_in">this</span>.$options.router) &#123;
        <span class="hljs-built_in">this</span>._routerRoot = <span class="hljs-built_in">this</span>;
        <span class="hljs-built_in">this</span>._router = <span class="hljs-built_in">this</span>.$options.router;
        
        <span class="hljs-comment">// 调用VueRouter实例初始化方法</span>
        <span class="hljs-comment">// _router即VueRouter实，此处this即Vue根实例</span>
        <span class="hljs-built_in">this</span>._router.init(<span class="hljs-built_in">this</span>) <span class="hljs-comment">// 添加项 </span>
        
        <span class="hljs-built_in">this</span>._route = &#123;&#125;;
      &#125; <span class="hljs-keyword">else</span> &#123;
        <span class="hljs-built_in">this</span>._routerRoot = (<span class="hljs-built_in">this</span>.$parent && <span class="hljs-built_in">this</span>.$parent._routerRoot) || <span class="hljs-built_in">this</span>
      &#125;
    &#125;,
  &#125;);
  
  <span class="hljs-comment">// ...</span>
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这时你会发现，<code>mixin</code> 中 <code>_route</code> 对象还是空对象，我们已经实现了当前路由对象即路由模式类的 <code>current</code> 属性，所以这里可以为其赋值了，再次修改代码如下：</p>
<pre><code class="hljs language-js copyable" lang="js">Vue.mixin(&#123;
  <span class="hljs-function"><span class="hljs-title">beforeCreate</span>(<span class="hljs-params"></span>)</span> &#123;
    <span class="hljs-keyword">if</span> (<span class="hljs-built_in">this</span>.$options.router) &#123;
      <span class="hljs-built_in">this</span>._routerRoot = <span class="hljs-built_in">this</span>;
      <span class="hljs-built_in">this</span>._router = <span class="hljs-built_in">this</span>.$options.router;
      <span class="hljs-built_in">this</span>._router.init(<span class="hljs-built_in">this</span>)

      <span class="hljs-comment">// this._route = &#123;&#125;; old</span>
      <span class="hljs-built_in">this</span>._route =  <span class="hljs-built_in">this</span>._router.history.current; <span class="hljs-comment">// new</span>
    &#125; <span class="hljs-keyword">else</span> &#123;
      <span class="hljs-built_in">this</span>._routerRoot = (<span class="hljs-built_in">this</span>.$parent && <span class="hljs-built_in">this</span>.$parent._routerRoot) || <span class="hljs-built_in">this</span>
    &#125;
  &#125;,
&#125;);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>到了这里其实我们 hash 模式的整个流程基本通了，可以打开项目链接看看，没有报错并且可以点击导航切换路由，有报错那肯定是你写错了，不是我。。虽无报错，但页面中路由模块没有渲染，因为 <code>router-view</code> 组件还没完善。</p>
<h2 data-id="heading-28">RouterView组件完善</h2>
<p>目前我们的 RouterView 组件是这样的：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">/*
 * @path: src/hello-vue-router/components/view.js
 * @Description: router-view
 */</span>
<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> &#123;
  <span class="hljs-attr">name</span>: <span class="hljs-string">"RouterView"</span>,
  <span class="hljs-attr">functional</span>: <span class="hljs-literal">true</span>,
  <span class="hljs-function"><span class="hljs-title">render</span>(<span class="hljs-params">h</span>)</span> &#123;
    <span class="hljs-keyword">return</span> h(<span class="hljs-string">'div'</span>, <span class="hljs-string">'This is RoutePage'</span>)
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>如上，组件渲染的永远是固定的 div，现在就可以开始完善它了。</p>
<h3 data-id="heading-29">路由组件动态渲染</h3>
<p>思路很简单，先拿到当前路由对象，因为当前路由对象的 <code>matched</code> 数组存着当前 path 所有有关联的路由匹配对象，数组最后一项即当前path本身的路由匹配对象，所以我们只需要取出数组最后一项，然后拿它的 components 属性（即当前 path 对应的路由模块），直接将它给到渲染函数即可。</p>
<p>开始修改 RouterView 组件：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> &#123;
  <span class="hljs-attr">name</span>: <span class="hljs-string">"RouterView"</span>,
  <span class="hljs-attr">functional</span>: <span class="hljs-literal">true</span>, <span class="hljs-comment">// 函数式组件</span>
  <span class="hljs-function"><span class="hljs-title">render</span>(<span class="hljs-params">h,  &#123; parent, data&#125;</span>)</span> &#123;
    <span class="hljs-comment">// parent：对父组件的引用</span>
    <span class="hljs-comment">// data：传递给组件的整个数据对象，作为 createElement 的第二个参数传入组件</span>
    
    <span class="hljs-comment">// 标识当前渲染组件为router-view</span>
    data.routerView = <span class="hljs-literal">true</span>

    <span class="hljs-keyword">let</span> route = parent.$route
    <span class="hljs-keyword">let</span> matched;
    <span class="hljs-keyword">if</span>(route.matched)&#123;
      matched = route.matched[route.matched.length - <span class="hljs-number">1</span>]
    &#125;

    <span class="hljs-keyword">if</span> (!matched) <span class="hljs-keyword">return</span> h();
  
    <span class="hljs-keyword">return</span> h(matched.components, data)
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>对函数式组件不了解的请看文档 <a href="https://link.juejin.cn/?target=https%3A%2F%2Fcn.vuejs.org%2Fv2%2Fguide%2Frender-function.html%23%25E5%2587%25BD%25E6%2595%25B0%25E5%25BC%258F%25E7%25BB%2584%25E4%25BB%25B6" target="_blank" rel="nofollow noopener noreferrer" title="https://cn.vuejs.org/v2/guide/render-function.html#%E5%87%BD%E6%95%B0%E5%BC%8F%E7%BB%84%E4%BB%B6" ref="nofollow noopener noreferrer">函数式组件文档</a> 。</p>
<p>其实代码很简单，先标识了一下当前渲染的是 RouterView 组件，代码中给 data 添加了一个属性，这个 data 最后会被作为 createElement 的第二个参数传入组件，当我们想要知道一个组件是不是 RouterView 渲染出来的，就可以通过这个属性来判断，这个属性存放在组件实例下 <code>$vnode</code> 属性的 data 对象中。</p>
<p>由于我们已经挂载了 <code>$route</code> 所以通过任何一个实例都可以访问此路由对象，拿到路由对象，取其 <code>matched</code> 属性数组的最后一项，即当前 path 对应的路由组件。</p>
<p>最后直接在 h（createElement）函数中返回组件即可。</p>
<p>貌似已经 OK 了，打开项目页面看一下。</p>
<p>页面中除了导航一片空白，也没报错，点击导航也确实触发跳转监听了（控制台有输出），但是并无任何组件渲染，如下：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/4ee77e9e0d334c65ab487fa5968363cb~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>怎么回事？捋一遍流程。</p>
<p>首先，点击导航跳转，监听到 hash 路由改变，走 <code>transitionTo</code> 方法，方法中做三件事：</p>
<ul>
<li>更新当前路由对象</li>
<li>更新URL</li>
<li>更新组件渲染</li>
</ul>
<p>诶！更新组件渲染，这一步我们好像到现在还没做，找到问题所在了！</p>
<p>RouterView 组件我们已经初步完善了，但是当路由 path 更新，我们怎么通知 RouterView 组件更新渲染呢？？</p>
<p>想一下，Vue最核心的是什么？当然是数据响应式，RouterView 的核心数据是 <code>$route</code>，如果我们将它做成一个响应式的数据，那当它改变时岂不就可以直接自动重新渲染！</p>
<p>说干就干，之前写的 <code>$route</code>，它其实是被代理到了 Vue 根实例的 <code>_route</code> 对象，所以只要将 <code>_route</code> 对象搞成响应式的就可以了，做响应式当然还是借助 Vue 提供的方法，不然我们在手写一个数据响应式太费劲了，况且 Vue 本身构造函数就有提供这样的 API，即 <code>Vue.util.defineReactive</code> 函数，使用也很简单，修改一下 install 方法：</p>
<pre><code class="hljs language-js copyable" lang="js">Vue.mixin(&#123;
  <span class="hljs-function"><span class="hljs-title">beforeCreate</span>(<span class="hljs-params"></span>)</span> &#123;
    <span class="hljs-keyword">if</span> (<span class="hljs-built_in">this</span>.$options.router) &#123;
      <span class="hljs-built_in">this</span>._routerRoot = <span class="hljs-built_in">this</span>;
      <span class="hljs-built_in">this</span>._router = <span class="hljs-built_in">this</span>.$options.router;
      <span class="hljs-built_in">this</span>._router.init(<span class="hljs-built_in">this</span>) 

      <span class="hljs-comment">// this._route =  this._router.history.current;  old</span>
      Vue.util.defineReactive(<span class="hljs-built_in">this</span>, <span class="hljs-string">'_route'</span>, <span class="hljs-built_in">this</span>._router.history.current); <span class="hljs-comment">// new</span>
    &#125; <span class="hljs-keyword">else</span> &#123;
      <span class="hljs-built_in">this</span>._routerRoot = (<span class="hljs-built_in">this</span>.$parent && <span class="hljs-built_in">this</span>.$parent._routerRoot) || <span class="hljs-built_in">this</span>
    &#125;
  &#125;,
&#125;);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>如上所示，我们使用 <code>Vue.util.defineReactive</code> API，为根实例（this）添加一个响应式属性 <code>_route</code> 并为其赋值为路由对象，这里能够直接使用 Vue 构造函数是因为 <code>install</code> 方法参数传入了 Vue。</p>
<p>如此，每当 <code>_route</code> 这个对象更改的时候 RouterView 组件就可以自动渲染了，我们再看下页面，点一点导航：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/1493a3ba65f64fdda99e29934dbe1452~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>fuck，还是老样子，这是为什么呢？再捋捋。</p>
<p>首先，点击导航跳转，监听到 hash 路由改变，走 <code>transitionTo</code> 方法，方法中做三件事：</p>
<ul>
<li>更新当前路由对象</li>
<li>更新URL</li>
<li>更新组件渲染</li>
</ul>
<p>好像没毛病啊，诶！等等，好像又发现了问题，更新当前路由对象的时候，好像只更新了 <code>current</code>，并没有更新 <code>_route</code>，<code>_route</code> 对象只在初始化的时候赋了一次值。。改它！！</p>
<p>首先为 <code>History</code> 类增加一个 <code>listen</code> 方法，并接收一个回调，<code>listen</code> 函数内部则直接将此回调函数保存到了 <code>History</code> 类的 <code>cb</code> 属性上，在 <code>transitionTo</code> 函数里 <code>current</code> 更新后面调用 <code>cb</code> 回调并传出了要更新的 <code>route</code> 对象，而 <code>_route</code> 更新的这一步操作，放在了 VueRouter 类的 init 方法里，如下：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// History父类中新增listen方法 保存赋值回调</span>
<span class="hljs-function"><span class="hljs-title">listen</span>(<span class="hljs-params">cb</span>)</span>&#123;
  <span class="hljs-built_in">this</span>.cb = cb
&#125;

<span class="hljs-function"><span class="hljs-title">transitionTo</span>(<span class="hljs-params">location, onComplete</span>)</span> &#123;
  <span class="hljs-keyword">let</span> route = <span class="hljs-built_in">this</span>.router.match(location);
  <span class="hljs-built_in">this</span>.current = route;

  <span class="hljs-comment">// 修改</span>
  <span class="hljs-comment">// 调用赋值回调，传出新路由对象，用于更新 _route</span>
  <span class="hljs-built_in">this</span>.cb && <span class="hljs-built_in">this</span>.cb(route)

  onComplete && onComplete(route)
  <span class="hljs-built_in">this</span>.ensureURL()
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>接着是 VueRouter 类的 init 方法：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-title">init</span>(<span class="hljs-params">app</span>)</span> &#123;
  app.$once(<span class="hljs-string">'hook:destroyed'</span>, <span class="hljs-function">() =></span> &#123;
    <span class="hljs-built_in">this</span>.app = <span class="hljs-literal">null</span>

    <span class="hljs-keyword">if</span> (!<span class="hljs-built_in">this</span>.app) <span class="hljs-built_in">this</span>.history.teardown()
  &#125;)

  <span class="hljs-keyword">if</span> (<span class="hljs-built_in">this</span>.app) <span class="hljs-keyword">return</span>;

  <span class="hljs-built_in">this</span>.app = app;

  <span class="hljs-built_in">this</span>.history.setupListeners();

  <span class="hljs-comment">// 新增 </span>
  <span class="hljs-comment">// 传入赋值回调，为_route赋值，进而触发router-view的重新渲染 </span>
  <span class="hljs-comment">// 当前路由对象改变时调用</span>
  <span class="hljs-built_in">this</span>.history.listen(<span class="hljs-function">(<span class="hljs-params">route</span>) =></span> &#123;
    app._route = route
  &#125;)
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>可能有小伙伴会懵，其实也很好理解，就是在 init 方法中调用了 <code>history</code> 实例继承于父类的 <code>listen</code> 方法，传入一个更新 <code>_route</code> 的回调，<code>listen</code> 函数会将这个回调一直保存，每次更新路由对象的时候，传入新的路由对象调用一次即可更新 <code>_route</code>。</p>
<p>现在打开页面再看一下，刷新页面，没有渲染，点击导航又渲染了。</p>
<p><strong>思考：为什么刷新时没有渲染组件？</strong></p>
<p>其实是因为路由 path 改变时，我们能够监听到，进而都做了操作，但当页面初始化时我们没有对初始的 path 进行解析。</p>
<p>知道了问题就解决！其实也简单，直接在 init 方法中获取当前路由path，然后调用 <code>transitionTo</code> 方法解析path渲染一下就行了，再次修改 VueRouter 类的 init 方法：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-title">init</span>(<span class="hljs-params">app</span>)</span> &#123;
  app.$once(<span class="hljs-string">'hook:destroyed'</span>, <span class="hljs-function">() =></span> &#123;
    <span class="hljs-built_in">this</span>.app = <span class="hljs-literal">null</span>

    <span class="hljs-keyword">if</span> (!<span class="hljs-built_in">this</span>.app) <span class="hljs-built_in">this</span>.history.teardown()
  &#125;)

  <span class="hljs-keyword">if</span> (<span class="hljs-built_in">this</span>.app) <span class="hljs-keyword">return</span>;

  <span class="hljs-built_in">this</span>.app = app;

  <span class="hljs-comment">// 新增</span>
  <span class="hljs-comment">// 跳转当前路由path匹配渲染 用于页面初始化</span>
  <span class="hljs-built_in">this</span>.history.transitionTo(
    <span class="hljs-comment">// 获取当前页面 path</span>
    <span class="hljs-built_in">this</span>.history.getCurrentLocation(),
    <span class="hljs-function">() =></span> &#123;
      <span class="hljs-comment">// 启动监听放在跳转后回调中即可</span>
      <span class="hljs-built_in">this</span>.history.setupListeners();
    &#125;
  )

  <span class="hljs-built_in">this</span>.history.listen(<span class="hljs-function">(<span class="hljs-params">route</span>) =></span> &#123;
    app._route = route
  &#125;)
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>如上，还记得路由模式子类中写的 <code>getCurrentLocation</code> 方法吗？其实就是获取当前路由path，使用 <code>history</code> 实例的 <code>transitionTo</code> 方法传入当前路由path，由于这里是 init 方法，所以相当于是在页面初始化时执行的，也就是刷新时会获取到当前页面的 path 进行解析渲染一次，我们把启动监听 <code>setupListeners</code> 函数放在了跳转回调中监听，这都无碍。</p>
<p>那再来看看页面：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/49393cca0a9d4d479e94c42d114c5d84~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>不论是刷新还是跳转都没有问题，都可以正常显示，nice！</p>
<h3 data-id="heading-30">嵌套路由组件渲染</h3>
<p>再测试一下嵌套路由吧！</p>
<p>做下准备，先写一个父级页面，在 <code>src/views/</code> 文件夹下新建 <code>Parent.vue</code> 文件，写入在代码：</p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">template</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">div</span>></span>
    parent page
    <span class="hljs-tag"><<span class="hljs-name">router-view</span>></span><span class="hljs-tag"></<span class="hljs-name">router-view</span>></span>
  <span class="hljs-tag"></<span class="hljs-name">div</span>></span>
<span class="hljs-tag"></<span class="hljs-name">template</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>接着写一个子级页面，在 <code>src/views/</code> 文件夹下新建 <code>Child.vue</code> 文件，写入代码：</p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">template</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">div</span>></span>
    child page
  <span class="hljs-tag"></<span class="hljs-name">div</span>></span>
<span class="hljs-tag"></<span class="hljs-name">template</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>修改 <code>src/router/index.js</code> 文件的路由配置数组如下：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> routes = [
  <span class="hljs-comment">// ...</span>
  
  <span class="hljs-comment">//新增路由配置</span>
  &#123;
    <span class="hljs-attr">path</span>: <span class="hljs-string">"/parent"</span>,
    <span class="hljs-attr">name</span>: <span class="hljs-string">"Parent"</span>,
    <span class="hljs-attr">component</span>: <span class="hljs-function">()=></span><span class="hljs-keyword">import</span>(<span class="hljs-string">"./../views/Parent.vue"</span>),
    <span class="hljs-attr">children</span>:[
      &#123;
        <span class="hljs-attr">path</span>: <span class="hljs-string">"child"</span>,
        <span class="hljs-attr">name</span>:<span class="hljs-string">"Child"</span>,
        <span class="hljs-attr">component</span>:<span class="hljs-function">()=></span><span class="hljs-keyword">import</span>(<span class="hljs-string">"./../views/Child.vue"</span>)
      &#125;
    ]
  &#125;
];
<span class="copy-code-btn">复制代码</span></code></pre>
<p>接着修改 <code>src/App.vue</code> 文件中的路由导航，新增 <code>Parent & Child</code> 两个导航如下：</p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">template</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">id</span>=<span class="hljs-string">"app"</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">id</span>=<span class="hljs-string">"nav"</span>></span>
      <span class="hljs-tag"><<span class="hljs-name">router-link</span> <span class="hljs-attr">to</span>=<span class="hljs-string">"/"</span>></span>Home<span class="hljs-tag"></<span class="hljs-name">router-link</span>></span> |
      <span class="hljs-tag"><<span class="hljs-name">router-link</span> <span class="hljs-attr">to</span>=<span class="hljs-string">"/about"</span>></span>About<span class="hljs-tag"></<span class="hljs-name">router-link</span>></span> ｜
      <span class="hljs-comment"><!-- 新增 --></span>
      <span class="hljs-tag"><<span class="hljs-name">router-link</span> <span class="hljs-attr">:to</span>=<span class="hljs-string">"&#123; path: '/parent' &#125;"</span>></span>Parent<span class="hljs-tag"></<span class="hljs-name">router-link</span>></span> |
      <span class="hljs-tag"><<span class="hljs-name">router-link</span> <span class="hljs-attr">:to</span>=<span class="hljs-string">"&#123; path: '/parent/child' &#125;"</span>></span>Parent Child<span class="hljs-tag"></<span class="hljs-name">router-link</span>></span>
    <span class="hljs-tag"></<span class="hljs-name">div</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">router-view</span>/></span>
  <span class="hljs-tag"></<span class="hljs-name">div</span>></span>
<span class="hljs-tag"></<span class="hljs-name">template</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>OK，这是一个非常简单的嵌套路由，来看看页面效果吧！</p>
<p>前两个页面正常，<code>parent</code> 页面组件没有渲染，控制台直接爆栈了：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/7ffbce3307be4b9d8ff945d88f497db9~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p><code>child</code> 页面显示如下：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/6858eb0724af40bbad7de6f572a4311c~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p><code>child</code> 页面因为只渲染出了子页面的内容，这是一个嵌套路由，子页页面内容是在父页面写的 <code>router-view</code> 中渲染，所以点击子页面正常应该父页面的内容也会显示。</p>
<p>其实，所有的问题都由于我们在写 RouterView 组件时，没有考虑嵌套的情况，回顾下 RouterView 组件代码：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> &#123;
  <span class="hljs-attr">name</span>: <span class="hljs-string">"RouterView"</span>,
  <span class="hljs-attr">functional</span>: <span class="hljs-literal">true</span>,
  <span class="hljs-function"><span class="hljs-title">render</span>(<span class="hljs-params">h,  &#123; parent, data&#125;</span>)</span> &#123;
    data.routerView = <span class="hljs-literal">true</span>

    <span class="hljs-keyword">let</span> route = parent.$route
    <span class="hljs-keyword">let</span> matched;
    <span class="hljs-keyword">if</span>(route.matched)&#123;
      matched = route.matched[route.matched.length - <span class="hljs-number">1</span>]
    &#125;

    <span class="hljs-keyword">if</span> (!matched) <span class="hljs-keyword">return</span> h();
  
    <span class="hljs-keyword">return</span> h(matched.components, data)
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>分析一下，以目前的 RouterView 组件代码，假如当前 path 为 <code>/parent/child</code> ，拿到当前路由对象 <code>route</code>，我们知道 <code>route.matched</code>  这里存放的是路径解析后所有相关的路由配置对象，它应该是这样的：</p>
<pre><code class="hljs language-js copyable" lang="js">[
  &#123;<span class="hljs-attr">path</span>: <span class="hljs-string">"/parent"</span>, components, ...&#125;,
  &#123;<span class="hljs-attr">path</span>: <span class="hljs-string">"/parent/child"</span>, components, ...&#125;
]
<span class="copy-code-btn">复制代码</span></code></pre>
<p>而我们取最后一项，只取了子路由模块，所以也就只渲染出了子路由组件。</p>
<p>再假如当前 path 为 <code>/parent</code> ，当前路由对象解析后拿到的 <code>route.matched</code> 数组是下面这样的：</p>
<pre><code class="hljs language-js copyable" lang="js">[
  &#123;<span class="hljs-attr">path</span>: <span class="hljs-string">"/parent"</span>, components, ...&#125;
]
<span class="copy-code-btn">复制代码</span></code></pre>
<p>取最后一项，只渲染了父路由组件，由于父路由组件中还有 <code>router-view</code> 组件，继续走组件逻辑，接着渲染父组件。。。一直循环下去，所以就爆栈了。。</p>
<p>修改一下 RouterView 组件，如下，先看完整代码再解释。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> &#123;
  <span class="hljs-attr">name</span>: <span class="hljs-string">"RouterView"</span>,
  <span class="hljs-attr">functional</span>: <span class="hljs-literal">true</span>, <span class="hljs-comment">// 函数式组件</span>
  <span class="hljs-function"><span class="hljs-title">render</span>(<span class="hljs-params">h,  &#123; parent, data&#125;</span>)</span> &#123;
    <span class="hljs-comment">// parent：对父组件的引用</span>
    <span class="hljs-comment">// data：传递给组件的整个数据对象，作为 createElement 的第二个参数传入组件</span>
    
    <span class="hljs-comment">// 标识当前组件为router-view</span>
    data.routerView = <span class="hljs-literal">true</span>

    <span class="hljs-keyword">let</span> depth = <span class="hljs-number">0</span>;
    <span class="hljs-comment">// 逐级向上查找组件，当parent指向Vue根实例结束循环</span>
    <span class="hljs-keyword">while</span>(parent && parent._routerRoot !== parent)&#123;
      <span class="hljs-keyword">const</span> vnodeData = parent.$vnode ? parent.$vnode.data : &#123;&#125;;
      <span class="hljs-comment">// routerView属性存在即路由组件深度+1，depth+1</span>
      <span class="hljs-keyword">if</span>(vnodeData.routerView)&#123;
        depth++
      &#125;

      parent = parent.$parent
    &#125;


    <span class="hljs-keyword">let</span> route = parent.$route
    
    <span class="hljs-keyword">if</span> (!route.matched) <span class="hljs-keyword">return</span> h();
    
    <span class="hljs-comment">// route.matched还是当前path全部关联的路由配置数组</span>
    <span class="hljs-comment">// 渲染的哪个组件，走上面逻辑时就会找到depth个RouterView组件</span>
    <span class="hljs-comment">// 由于逐级向上时是从父级组件开始找，所以depth数量并没有包含当前路由组件</span>
    <span class="hljs-comment">// 假如depth=2，则route.matched数组前两项都是父级，第三项则是当前组件，所以depth=索引</span>
    <span class="hljs-keyword">let</span> matched = route.matched[depth]

    <span class="hljs-keyword">if</span> (!matched) <span class="hljs-keyword">return</span> h();

    <span class="hljs-keyword">return</span> h(matched.components, data)
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这块可能不太容易理解。</p>
<p>首先还是给所有的 RouterView 组件做了一个标识。</p>
<p>接着开始从 <code>parent</code> 父级实例逐级向上遍历组件，从当前父实例找到顶部根实例，也就是当 <code>parent._routerRoot !== parent</code> 成立时，跳出循环。</p>
<p>在遍历的逻辑里，判断实例的 <code>$vnode</code> 属性下 data 属性中有无 <code>routerView</code> 属性，有则 <code>depth + 1</code>，遍历的最后让 <code>parent = parent.$parent</code> ，<code>$parent</code> 拿到的是父组件实例，以此开启递归。</p>
<p>要知道不论怎么搞，当前 path 对应的路由对象 route 对象始终是不变的，而 <code>route.matched</code> 是当前 path 全部关联的路由配置数组。</p>
<p>假如当前 path 是 <code>/a/b/c</code> ，三级嵌套路由，那它的 <code>route.matched</code> 应如下：</p>
<pre><code class="hljs language-js copyable" lang="js">[
  &#123;<span class="hljs-attr">path</span>: <span class="hljs-string">"/a"</span>, ...&#125;,
  &#123;<span class="hljs-attr">path</span>: <span class="hljs-string">"/a/b"</span>, ...&#125;,
  &#123;<span class="hljs-attr">path</span>: <span class="hljs-string">"/a/b/c"</span>, ...&#125;,
]
<span class="copy-code-btn">复制代码</span></code></pre>
<p>嵌套了三层，也就有三个 RouterView 组件， <code>App.vue、a.vue、b.vue</code> 中各一个，所以当渲染 <code>/a/b/c</code> 时，页面应该是下面这样的：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// /a/b/c</span>
a
 b
  c
<span class="copy-code-btn">复制代码</span></code></pre>
<p>当 <code>App.vue</code> 页面 RouterView 组件开始渲染，走组件逻辑查找 <code>depth</code> 层级，<strong>从父实例</strong>向上迭代到根实例查找带有 <code>routerView</code> 属性的组件，有 0 个，所以 <code>depth = 0</code> ，<code>route.matched[0]</code> 即 <code>/a</code> 路由组件。</p>
<p>当 <code>a.vue</code> 页面 RouterView 组件开始渲染，走组件逻辑查找 <code>depth</code> 层级，<strong>从父实例</strong>向上迭代到根实例查找带有 <code>routerView</code> 属性的组件，有 1 个，所以 <code>depth = 1</code> ，<code>route.matched[1]</code> 即 <code>/a</code> 路由组件。</p>
<p>当 <code>b.vue</code> 页面 RouterView 组件开始渲染，走组件逻辑查找 <code>depth</code> 层级，<strong>从父实例</strong>向上迭代到根实例查找带有 <code>routerView</code> 属性的组件，有 2 个，所以 <code>depth = 2</code> ，<code>route.matched[2]</code> 即 <code>/a</code> 路由组件。</p>
<p>再来看看页面，我们发现嵌套路由两个页面都正常了。</p>
<p>/parent：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/43d5c5e87d1843488f519dccd1f03267~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>/parent/child：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/066a1463ba354211a86d834d8f365e68~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>所以，看懂了吗？我觉得够详细了，不懂再看几遍配合断点或打印。</p>
<h2 data-id="heading-31">VueRouter实例方法挂载完善</h2>
<p>路由模式类上面我们实现了几个路由跳转相关的方法，还没有挂载到 VueRouter 类上，我们一块来挂载下，还有之前挂载的 <code>addRoute & addRoutes</code> 两个方法，还需要完善一下。</p>
<p>回到 <code>src/hello-vue-router/index.js</code> 文件：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> <span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">VueRouter</span> </span>&#123;
  
  <span class="hljs-comment">// 导航到新url，向 history栈添加一条新访问记录</span>
  <span class="hljs-function"><span class="hljs-title">push</span>(<span class="hljs-params">location</span>)</span> &#123;
    <span class="hljs-built_in">this</span>.history.push(location)
  &#125;

  <span class="hljs-comment">// 在 history 记录中向前或者后退多少步</span>
  <span class="hljs-function"><span class="hljs-title">go</span>(<span class="hljs-params">n</span>)</span> &#123;
    <span class="hljs-built_in">this</span>.history.go(n);
  &#125;

  <span class="hljs-comment">// 导航到新url，替换 history 栈中当前记录</span>
  <span class="hljs-function"><span class="hljs-title">replace</span>(<span class="hljs-params">location, onComplete</span>)</span> &#123;
    <span class="hljs-built_in">this</span>.history.replace(location, onComplete)
  &#125;

  <span class="hljs-comment">// 导航回退一步</span>
  <span class="hljs-function"><span class="hljs-title">back</span>(<span class="hljs-params"></span>)</span> &#123;
    <span class="hljs-built_in">this</span>.history.go(-<span class="hljs-number">1</span>)
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>如上，添加几个路由跳转相关的方法，其实就是调用已经实现好的 history 实例上的方法就 OK 了，不赘述了。</p>
<p>接着我们看之前挂载的 <code>addRoute & addRoutes</code> 两个方法。</p>
<p>目前这两个方法调用时，确实进行追加了，普通情况下也是没问题的，但是有一种特殊情况，即在当前页面 path 初始化前，动态添加当前页面的路由组件，这时我们如果使用目前的API加载后，其实只是解析并添加了内部 pathMap， 但由于当前路由对象并没有更新，页面直接就会报错。</p>
<p>所以需要在动态添加后进行一次路由更新操作，其实还是调用一下 <code>transitionTo</code> 方法跳转当前页面 path 即可，当然还需避免路由初始化时即当前路由等于 <code>START</code> （之前写的路由 current 对象初始值）的情况。</p>
<p>So，修改这两个函数，如下：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// 新增START对象导入</span>
<span class="hljs-keyword">import</span> &#123; START &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">"./utils/route"</span>;

<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> <span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">VueRouter</span> </span>&#123;
  
 <span class="hljs-comment">// 动态添加路由（添加一条新路由规则）</span>
  <span class="hljs-function"><span class="hljs-title">addRoute</span>(<span class="hljs-params">parentOrRoute, route</span>)</span> &#123;
    <span class="hljs-built_in">this</span>.matcher.addRoute(parentOrRoute, route)
    <span class="hljs-comment">// 新增</span>
    <span class="hljs-keyword">if</span> (<span class="hljs-built_in">this</span>.history.current !== START) &#123;
      <span class="hljs-built_in">this</span>.history.transitionTo(<span class="hljs-built_in">this</span>.history.getCurrentLocation())
    &#125;
  &#125;

  <span class="hljs-comment">// 动态添加路由（参数必须是一个符合 routes 选项要求的数组）</span>
  <span class="hljs-function"><span class="hljs-title">addRoutes</span>(<span class="hljs-params">routes</span>)</span> &#123;
    <span class="hljs-built_in">this</span>.matcher.addRoutes(routes)
    <span class="hljs-comment">// 新增</span>
    <span class="hljs-keyword">if</span> (<span class="hljs-built_in">this</span>.history.current !== START) &#123;
      <span class="hljs-built_in">this</span>.history.transitionTo(<span class="hljs-built_in">this</span>.history.getCurrentLocation())
    &#125;
  &#125;
  
  <span class="hljs-comment">// ...</span>
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>比较简单，不赘述了。</p>
<p>至此，hash 模式的流程完整了。</p>
<p>接下来就是按部就班的实现 history 模式也就是填充 HTML5History 类了。</p>
<h2 data-id="heading-32">HTML5History类实现</h2>
<p>HTML5History 类虽然和 HashHistory 类实现细节上略有不同，但是我们要写的 API 都是一致的，这样才能完全契合外部的统一调用。</p>
<p>来到 <code>history/</code> 文件夹下的 <code>html5.js</code> 文件，有了上面 HashHistory 类的经验我们这里就直接贴代码了，因为没有什么困难的地方。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">/*
 * @path: src/hello-vue-router/history/html5.js
 * @Description: 路由模式HTML5History子类
 */</span>
<span class="hljs-keyword">import</span> &#123; History &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'./base'</span>

<span class="hljs-keyword">export</span> <span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">HTML5History</span> <span class="hljs-keyword">extends</span> <span class="hljs-title">History</span> </span>&#123;
  <span class="hljs-function"><span class="hljs-title">constructor</span>(<span class="hljs-params">router</span>)</span> &#123;
    <span class="hljs-comment">// 继承父类</span>
    <span class="hljs-built_in">super</span>(router);
  &#125;

  <span class="hljs-comment">// 启动路由监听</span>
  <span class="hljs-function"><span class="hljs-title">setupListeners</span>(<span class="hljs-params"></span>)</span> &#123;
    <span class="hljs-comment">// 路由监听回调</span>
    <span class="hljs-keyword">const</span> handleRoutingEvent = <span class="hljs-function">() =></span> &#123;

      <span class="hljs-built_in">this</span>.transitionTo(getLocation(), <span class="hljs-function">() =></span> &#123;
        <span class="hljs-built_in">console</span>.log(<span class="hljs-string">`HTML5路由监听跳转成功！`</span>);
      &#125;);
    &#125;;

    <span class="hljs-built_in">window</span>.addEventListener(<span class="hljs-string">"popstate"</span>, handleRoutingEvent);
    <span class="hljs-built_in">this</span>.listeners.push(<span class="hljs-function">() =></span> &#123;
      <span class="hljs-built_in">window</span>.removeEventListener(<span class="hljs-string">"popstate"</span>, handleRoutingEvent);
    &#125;);
  &#125;

  <span class="hljs-comment">// 更新URL</span>
  <span class="hljs-function"><span class="hljs-title">ensureURL</span>(<span class="hljs-params"></span>)</span> &#123;
    <span class="hljs-keyword">if</span> (getLocation() !== <span class="hljs-built_in">this</span>.current.fullPath) &#123;
      <span class="hljs-built_in">window</span>.history.pushState(
        &#123; <span class="hljs-attr">key</span>: <span class="hljs-built_in">Date</span>.now().toFixed(<span class="hljs-number">3</span>) &#125;, 
        <span class="hljs-string">""</span>, 
        <span class="hljs-built_in">this</span>.current.fullPath
      );
    &#125;
  &#125;

  <span class="hljs-comment">// 路由跳转方法</span>
  <span class="hljs-function"><span class="hljs-title">push</span>(<span class="hljs-params">location, onComplete</span>)</span> &#123;
    <span class="hljs-built_in">this</span>.transitionTo(location, onComplete)
  &#125;

  <span class="hljs-comment">// 路由前进后退</span>
  <span class="hljs-function"><span class="hljs-title">go</span>(<span class="hljs-params">n</span>)</span>&#123;
    <span class="hljs-built_in">window</span>.history.go(n)
  &#125;

  <span class="hljs-comment">// 跳转到指定URL，替换history栈中最后一个记录</span>
  <span class="hljs-function"><span class="hljs-title">replace</span>(<span class="hljs-params">location, onComplete</span>)</span> &#123;
    <span class="hljs-built_in">this</span>.transitionTo(location, <span class="hljs-function">(<span class="hljs-params">route</span>) =></span> &#123;
      <span class="hljs-built_in">window</span>.history.replaceState(<span class="hljs-built_in">window</span>.history.state, <span class="hljs-string">''</span>, route.fullPath)
      onComplete && onComplete(route)
    &#125;)
  &#125;

  <span class="hljs-comment">// 获取当前路由</span>
  <span class="hljs-function"><span class="hljs-title">getCurrentLocation</span>(<span class="hljs-params"></span>)</span> &#123;
    <span class="hljs-keyword">return</span> getLocation()
  &#125;
&#125;

<span class="hljs-comment">// 获取location HTML5 路由</span>
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">getLocation</span>(<span class="hljs-params"></span>) </span>&#123;
  <span class="hljs-keyword">let</span> path = <span class="hljs-built_in">window</span>.location.pathname;
  <span class="hljs-keyword">return</span> path;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>如上我们很轻松就实现了 HTML5Histoy 类，但是有一个问题，在使用 <code>history</code> ，不断点击 <code>router-link</code> 生成的同一个导航时，每次点击都会刷新页面，这其实就是我们之前说的， <code>router-link</code> 最终生成的是 a 标签，<code>history</code> 模式点击 a 标签，默认会触发页面的跳转，所以需要拦截 a 标签点击事件默认行为，<code>hash</code> 就不会，因为 hash 模式下 a 标签中解析后的 href 属性中是以 <code>#</code> 号开头的。</p>
<p>在哪里拦截？当然是 <code>router-link</code> 组件。</p>
<h2 data-id="heading-33">RouterLink组件完善</h2>
<p>也比较简单，统一给 RouterLink 组件返回的 a 标签加了阻止默认跳转，然后又加了手动跳转：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> &#123;
  <span class="hljs-attr">name</span>: <span class="hljs-string">"RouterLink"</span>,
  <span class="hljs-attr">props</span>: &#123;
    <span class="hljs-attr">to</span>: &#123;
      <span class="hljs-attr">type</span>: [<span class="hljs-built_in">String</span>, <span class="hljs-built_in">Object</span>],
      <span class="hljs-attr">require</span>: <span class="hljs-literal">true</span>
    &#125;
  &#125;,
  <span class="hljs-function"><span class="hljs-title">render</span>(<span class="hljs-params">h</span>)</span> &#123;
    <span class="hljs-keyword">const</span> href = <span class="hljs-keyword">typeof</span> <span class="hljs-built_in">this</span>.to === <span class="hljs-string">'string'</span> ? <span class="hljs-built_in">this</span>.to : <span class="hljs-built_in">this</span>.to.path
    <span class="hljs-keyword">const</span> router = <span class="hljs-built_in">this</span>.$router
    <span class="hljs-keyword">let</span> data = &#123;
      <span class="hljs-attr">attrs</span>: &#123;
        <span class="hljs-attr">href</span>: router.mode === <span class="hljs-string">"hash"</span> ? <span class="hljs-string">"#"</span> + href : href
      &#125;,
      <span class="hljs-comment">//新增</span>
      <span class="hljs-attr">on</span>: &#123;
        <span class="hljs-attr">click</span>: <span class="hljs-function"><span class="hljs-params">e</span> =></span> &#123;
          e.preventDefault()
          router.push(href)
        &#125;
      &#125;
    &#125;;
    <span class="hljs-keyword">return</span> h(<span class="hljs-string">"a"</span>, data, <span class="hljs-built_in">this</span>.$slots.default)
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>如上，我们在 createElement（h）函数的第二个参数中，对点击事件加入了阻止默认跳转事件，没有了默认跳转，我们进行了一次手动跳转，即直接调用 <code>router</code> 实例的 <code>push</code> 方法进行跳转。</p>
<h2 data-id="heading-34">AbstractHistory类实现</h2>
<p>没有了，其实实现起来很简单，就是用数组模拟了一个历史调用栈，找源码看一眼几分钟就写完了，完全是由一个数组和各种数组操作API组成的类，篇幅问题，不赘述了。</p>
<h2 data-id="heading-35">植入router hook</h2>
<p>如果你跟着实现，到了这其实 VueRouter 的核心内容都差不多搞定了，接下来可以疯狂发散下思路，再自己动手找源码中相关实现来参考，最后完善出来 <code>router hook</code>，因为路由钩子是余下功能里实现起来有一定难度的一个，这是一个非常好的锻炼机会。</p>
<p><strong>Tips：</strong> 路由钩子有三种：</p>
<ul>
<li>全局路由钩子</li>
<li>组件路由钩子</li>
<li>路由独享beforeEnter守卫</li>
</ul>
<h2 data-id="heading-36">写在最后</h2>
<p>如果看到这里依然对其流程不太清楚，再来看这张图，说不定可以直接打通任督二脉哦！</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/6aae2f62cb504a58b0097829958a4dc1~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>整个实现的核心逻辑还算 OK，细节上还存在很多问题，因为我们忽略了一些校验及小功能的实现，但对理解 VueRouter 源码还是有很大帮助。建议跟着手敲一遍，搞完后直接去完整的看一遍 VueRouter 源码，加油吧！欢迎刊误！原创烧脑，写作不易，如果对你有帮助，点个赞吧！！</p>
<p>项目代码地址：<a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fisboyjc%2Fhello-vue-router" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/isboyjc/hello-vue-router" ref="nofollow noopener noreferrer">hello-vue-router</a></p>
<p>根目录下 <code>src/hello-vue-router</code> 文件夹即手写 VueRouter 完整代码，已作注释</p>
<p>根目录下 <code>vue-router-source</code> 文件夹即带有注释的 VueRouter V3.5.2 源码</p></div>  
</div>
            