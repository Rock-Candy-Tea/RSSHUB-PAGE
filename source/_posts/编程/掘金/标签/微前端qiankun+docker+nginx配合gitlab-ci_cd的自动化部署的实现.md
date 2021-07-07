
---
title: '微前端qiankun+docker+nginx配合gitlab-ci_cd的自动化部署的实现'
categories: 
 - 编程
 - 掘金
 - 标签
headimg: 'https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/99bde409c3234317bc129b0707af92f4~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Sun, 04 Jul 2021 23:24:31 GMT
thumbnail: 'https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/99bde409c3234317bc129b0707af92f4~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h2 data-id="heading-0">往期文章推荐</h2>
<p><a href="https://juejin.cn/post/6976222927742042119" target="_blank">一篇文章教你搭建一个前后端分离（gitlab-cicd+docker+vue+django）的自动化部署的网站，干货满满！</a></p>
<p><a href="https://juejin.cn/post/6964289384845672478" target="_blank">Docker入门，这一篇就够了</a></p>
<h2 data-id="heading-1">技术栈简介</h2>
<ul>
<li>微前端</li>
<li>qiankun</li>
<li><a href="https://juejin.cn/post/6976222927742042119#heading-2" target="_blank">docker</a> 不了解的建议先看一下我之前的介绍，一看就明白</li>
<li><a href="https://juejin.cn/post/6976222927742042119#heading-4" target="_blank">gitlab-ci/cd</a> 这里是自动化部署的知识，可以了解一下</li>
<li>nginx</li>
</ul>
<h3 data-id="heading-2">什么是微前端</h3>
<p>微前端是一种多个团队通过独立发布功能的方式来共同构建现代化 web 应用的技术手段及方法策略。</p>
<p>微前端架构具备以下几个核心价值：</p>
<ul>
<li>
<p>技术栈无关
主框架不限制接入应用的技术栈，微应用具备完全自主权</p>
</li>
<li>
<p>独立开发、独立部署
微应用仓库独立，前后端可独立开发，部署完成后主框架自动完成同步更新</p>
</li>
<li>
<p>增量升级</p>
<p>在面对各种复杂场景时，我们通常很难对一个已经存在的系统做全量的技术栈升级或重构，而微前端是一种非常好的实施渐进式重构的手段和策略</p>
</li>
<li>
<p>独立运行时
每个微应用之间状态隔离，运行时状态不共享</p>
</li>
</ul>
<h3 data-id="heading-3">什么是qiankun</h3>
<p>qiankun 是一个生产可用的微前端框架，它基于 single-spa，具备 js 沙箱、样式隔离、HTML Loader、预加载 等微前端系统所需的能力。qiankun 可以用于任意 js 框架，微应用接入像嵌入一个 iframe 系统一样简单。</p>
<h3 data-id="heading-4">qiankun 的核心设计理念</h3>
<p>引用地址：<a href="https://qiankun.umijs.org/zh/guide" target="_blank" rel="nofollow noopener noreferrer">qiankun.umijs.org/zh/guide</a></p>
<ul>
<li>
<p>简单</p>
<p>由于主应用微应用都能做到技术栈无关，qiankun 对于用户而言只是一个类似 jQuery 的库，你需要调用几个 qiankun 的 API 即可完成应用的微前端改造。同时由于 qiankun 的 HTML entry 及沙箱的设计，使得微应用的接入像使用 iframe 一样简单。</p>
</li>
<li>
<p>解耦/技术栈无关</p>
<p>微前端的核心目标是将巨石应用拆解成若干可以自治的松耦合微应用，而 qiankun 的诸多设计均是秉持这一原则，如 HTML entry、沙箱、应用间通信等。这样才能确保微应用真正具备 独立开发、独立运行 的能力。</p>
</li>
</ul>
<h3 data-id="heading-5">为什么不用Iframe</h3>
<p>引用地址：<a href="https://www.yuque.com/kuitos/gky7yw/gesexv" target="_blank" rel="nofollow noopener noreferrer">www.yuque.com/kuitos/gky7…</a></p>
<p><em>如果不考虑体验问题，iframe 几乎是最完美的微前端解决方案了。</em></p>
<p>iframe 最大的特性就是提供了浏览器原生的硬隔离方案，不论是样式隔离、js 隔离这类问题统统都能被完美解决。但他的最大问题也在于他的隔离性无法被突破，导致应用间上下文无法被共享，随之带来的开发体验、产品体验的问题。</p>
<ol>
<li>url 不同步。浏览器刷新 iframe url 状态丢失、后退前进按钮无法使用。</li>
<li>UI 不同步，DOM 结构不共享。想象一下屏幕右下角 1/4 的 iframe 里来一个带遮罩层的弹框，同时我们要求这个弹框要浏览器居中显示，还要浏览器 resize 时自动居中。</li>
<li>全局上下文完全隔离，内存变量不共享。iframe 内外系统的通信、数据同步等需求，主应用的 cookie 要透传到根域名都不同的子应用中实现免登效果。</li>
<li>慢。每次子应用进入都是一次浏览器上下文重建、资源重新加载的过程。</li>
</ol>
<p>其中有的问题比较好解决(问题1)，有的问题我们可以睁一只眼闭一只眼(问题4)，但有的问题我们则很难解决(问题3)甚至无法解决(问题2)，而这些无法解决的问题恰恰又会给产品带来非常严重的体验问题， 最终导致我们舍弃了 iframe 方案。</p>
<h3 data-id="heading-6">微前端的核心价值</h3>
<p><a href="https://www.yuque.com/kuitos/gky7yw/rhduwc" target="_blank" rel="nofollow noopener noreferrer">www.yuque.com/kuitos/gky7…</a></p>
<h2 data-id="heading-7">项目的构想</h2>
<p>在说具体技术实现前，我们先来看下我们想要实现个什么东西。</p>
<h3 data-id="heading-8">微前端示意图</h3>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/99bde409c3234317bc129b0707af92f4~tplv-k3u1fbpfcp-watermark.image" alt="image-20210705141310079.png" loading="lazy" referrerpolicy="no-referrer">
主应用负责登录状态的管理和导航的显示</p>
<p>子应用会根据主应用导航的点击而动态加载</p>
<h3 data-id="heading-9">部署逻辑</h3>
<p>部署的思路有很多，我这里说说我尝试过的方式：</p>
<ul>
<li>
<p>只使用一个nginx容器，通过监听不同端口，部署多个应用，再在主应用的端口里面添加对应路由代理到子应用</p>
<p>这种方式最简单但是不适合 gitlab-ci/cd 的自动化部署，所以我只是最初测试一下nginx部署微前端的实现</p>
</li>
<li>
<p>使用多个nginx容器，每个容器暴露一个端口，再通过主应用添加对应路由代理到子应用</p>
<p>这种方式可以实现，但是会在服务器暴露多个端口，安全性会降低，而且外部也可以通过端口直接访问子应用</p>
</li>
<li>
<p>使用多个nginx容器，只暴露主应用的端口，主应用去连通子应用，然后通过nginx代理访问</p>
<p>这种方式最理想，只需要暴露一个端口，所有代理都在容器间，对外是无感的，下面是实现的图示</p>
</li>
</ul>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/bf4f65e0e844466893c86514ccbaec0b~tplv-k3u1fbpfcp-watermark.image" alt="image-20210705142948593.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-10">qiankun</h2>
<h3 data-id="heading-11">安装qiankun</h3>
<pre><code class="hljs language-bash copyable" lang="bash">$ yarn add qiankun <span class="hljs-comment"># 或者 npm i qiankun -S</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-12">在主应用中注册微应用</h3>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-keyword">import</span> &#123; registerMicroApps, addGlobalUncaughtErrorHandler, start &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'qiankun'</span>;

<span class="hljs-keyword">const</span> apps = [
  &#123;
    <span class="hljs-attr">name</span>: <span class="hljs-string">'ManageMicroApp'</span>,
    <span class="hljs-attr">entry</span>: <span class="hljs-string">'/system/'</span>, <span class="hljs-comment">// 本地开发的时候使用 //localhost:子应用端口</span>
    <span class="hljs-attr">container</span>: <span class="hljs-string">'#frame'</span>,
    <span class="hljs-attr">activeRule</span>: <span class="hljs-string">'/manage'</span>,
  &#125;,
]

<span class="hljs-comment">/**
 * 注册微应用
 * 第一个参数 - 微应用的注册信息
 * 第二个参数 - 全局生命周期钩子
 */</span>
registerMicroApps(apps,&#123;
  <span class="hljs-comment">// qiankun 生命周期钩子 - 微应用加载前</span>
  <span class="hljs-attr">beforeLoad</span>: <span class="hljs-function">(<span class="hljs-params">app: <span class="hljs-built_in">any</span></span>) =></span> &#123;
    <span class="hljs-built_in">console</span>.log(<span class="hljs-string">"before load"</span>, app.name);
    <span class="hljs-keyword">return</span> <span class="hljs-built_in">Promise</span>.resolve();
  &#125;,
  <span class="hljs-comment">// qiankun 生命周期钩子 - 微应用挂载后</span>
  <span class="hljs-attr">afterMount</span>: <span class="hljs-function">(<span class="hljs-params">app: <span class="hljs-built_in">any</span></span>) =></span> &#123;
    <span class="hljs-built_in">console</span>.log(<span class="hljs-string">"after mount"</span>, app.name);
    <span class="hljs-keyword">return</span> <span class="hljs-built_in">Promise</span>.resolve();
  &#125;,
&#125;);

<span class="hljs-comment">/**
 * 添加全局的未捕获异常处理器
 */</span>
addGlobalUncaughtErrorHandler(<span class="hljs-function">(<span class="hljs-params">event: Event | <span class="hljs-built_in">string</span></span>) =></span> &#123;
  <span class="hljs-built_in">console</span>.error(event);
  <span class="hljs-keyword">const</span> &#123; <span class="hljs-attr">message</span>: msg &#125; = event <span class="hljs-keyword">as</span> <span class="hljs-built_in">any</span>;
  <span class="hljs-comment">// 加载失败时提示</span>
  <span class="hljs-keyword">if</span> (msg && msg.includes(<span class="hljs-string">"died in status LOADING_SOURCE_CODE"</span>)) &#123;
    <span class="hljs-built_in">console</span>.error(<span class="hljs-string">"微应用加载失败，请检查应用是否可运行"</span>);
  &#125;
&#125;);

start();
<span class="copy-code-btn">复制代码</span></code></pre>
<p>当微应用信息注册完之后，一旦浏览器的 url 发生变化，便会自动触发 qiankun 的匹配逻辑，所有 activeRule 规则匹配上的微应用就会被插入到指定的 container 中，同时依次调用微应用暴露出的生命周期钩子。</p>
<p>如果微应用不是直接跟路由关联的时候，你也可以选择手动加载微应用的方式：</p>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-keyword">import</span> &#123; loadMicroApp &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'qiankun'</span>;


loadMicroApp(&#123;
  <span class="hljs-attr">name</span>: <span class="hljs-string">'app'</span>,
  <span class="hljs-attr">entry</span>: <span class="hljs-string">'//localhost:7100'</span>,
  <span class="hljs-attr">container</span>: <span class="hljs-string">'#yourContainer'</span>,
&#125;);
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-13">微应用</h3>
<p>微应用不需要额外安装任何其他依赖即可接入 qiankun 主应用。</p>
<h4 data-id="heading-14">1. 导出相应的生命周期钩子</h4>
<p>微应用需要在自己的入口 js (通常就是你配置的 webpack 的 entry js) 导出 <code>bootstrap</code>、<code>mount</code>、<code>unmount</code> 三个生命周期钩子，以供主应用在适当的时机调用。</p>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-keyword">import</span> Vue <span class="hljs-keyword">from</span> <span class="hljs-string">'vue'</span>;
<span class="hljs-keyword">import</span> VueRouter <span class="hljs-keyword">from</span> <span class="hljs-string">'vue-router'</span>;

<span class="hljs-keyword">import</span> <span class="hljs-string">'./public-path'</span>;
<span class="hljs-keyword">import</span> App <span class="hljs-keyword">from</span> <span class="hljs-string">'./App.vue'</span>;
<span class="hljs-keyword">import</span> routes <span class="hljs-keyword">from</span> <span class="hljs-string">'./routes'</span>;
<span class="hljs-keyword">import</span> SharedModule <span class="hljs-keyword">from</span> <span class="hljs-string">'@/shared'</span>; 

Vue.config.productionTip = <span class="hljs-literal">false</span>;

<span class="hljs-keyword">let</span> instance = <span class="hljs-literal">null</span>;
<span class="hljs-keyword">let</span> router = <span class="hljs-literal">null</span>;
<span class="hljs-comment">// 如果子应用独立运行则直接执行render</span>
<span class="hljs-keyword">if</span> (!<span class="hljs-built_in">window</span>.__POWERED_BY_QIANKUN__) &#123;
  render();
&#125;

<span class="hljs-comment">/**
 * 渲染函数
 * 主应用生命周期钩子中运行/子应用单独启动时运行
 */</span>
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">render</span>(<span class="hljs-params">props = &#123;&#125;</span>) </span>&#123;
  <span class="hljs-comment">// SharedModule用于主应用于子应用的通讯</span>
  <span class="hljs-comment">// 当传入的 shared 为空时，使用子应用自身的 shared</span>
  <span class="hljs-comment">// 当传入的 shared 不为空时，主应用传入的 shared 将会重载子应用的 shared</span>
  <span class="hljs-keyword">const</span> &#123; shared = SharedModule.getShared() &#125; = props;
  SharedModule.overloadShared(shared);

  router = <span class="hljs-keyword">new</span> VueRouter(&#123;
    <span class="hljs-attr">base</span>: <span class="hljs-built_in">window</span>.__POWERED_BY_QIANKUN__ ? <span class="hljs-string">'/manage/'</span> : <span class="hljs-string">'/'</span>,
    <span class="hljs-attr">mode</span>: <span class="hljs-string">'history'</span>,
    routes
  &#125;);

  <span class="hljs-comment">// 挂载应用</span>
  instance = <span class="hljs-keyword">new</span> Vue(&#123;
    router,
    <span class="hljs-attr">render</span>: <span class="hljs-function">(<span class="hljs-params">h</span>) =></span> h(App)
  &#125;).$mount(<span class="hljs-string">'#app'</span>);
&#125;

<span class="hljs-comment">/**
 * bootstrap 只会在微应用初始化的时候调用一次，下次微应用重新进入时会直接调用 mount 钩子，不会再重复触发 bootstrap。
 * 通常我们可以在这里做一些全局变量的初始化，比如不会在 unmount 阶段被销毁的应用级别的缓存等。
 */</span>
<span class="hljs-keyword">export</span> <span class="hljs-keyword">async</span> <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">bootstrap</span>(<span class="hljs-params"></span>) </span>&#123;
  <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'vue app bootstraped'</span>);
&#125;
<span class="hljs-comment">/**
 * 应用每次进入都会调用 mount 方法，通常我们在这里触发应用的渲染方法
 */</span>
<span class="hljs-keyword">export</span> <span class="hljs-keyword">async</span> <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">mount</span>(<span class="hljs-params">props</span>) </span>&#123;
  <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'vue mount'</span>, props);
  render(props);
&#125;
<span class="hljs-comment">/**
 * 应用每次 切出/卸载 会调用的方法，通常在这里我们会卸载微应用的应用实例
 */</span>
<span class="hljs-keyword">export</span> <span class="hljs-keyword">async</span> <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">unmount</span>(<span class="hljs-params"></span>) </span>&#123;
  <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'vue unmount'</span>);
  instance.$destroy();
  instance = <span class="hljs-literal">null</span>;
  router = <span class="hljs-literal">null</span>;
&#125;
<span class="hljs-comment">/**
 * 可选生命周期钩子，仅使用 loadMicroApp 方式加载微应用时生效
 */</span>
<span class="hljs-keyword">export</span> <span class="hljs-keyword">async</span> <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">update</span>(<span class="hljs-params">props</span>) </span>&#123;
  <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'update props'</span>, props);
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>上述代码中还引用了一个<code>public-path</code>的文件：</p>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-keyword">if</span> (<span class="hljs-built_in">window</span>.__POWERED_BY_QIANKUN__) &#123;
  <span class="hljs-comment">// eslint-disable-next-line no-undef</span>
  __webpack_public_path__ = <span class="hljs-built_in">window</span>.__INJECTED_PUBLIC_PATH_BY_QIANKUN__;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这个主要解决的是微应用动态载入的 脚本、样式、图片 等地址不正确的问题。</p>
<h4 data-id="heading-15">2. 配置微应用的打包工具</h4>
<p>除了代码中暴露出相应的生命周期钩子之外，为了让主应用能正确识别微应用暴露出来的一些信息，微应用的打包工具需要增加如下配置：</p>
<p><strong>webpack：</strong></p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> packageName = <span class="hljs-built_in">require</span>(<span class="hljs-string">'./package.json'</span>).name;


<span class="hljs-built_in">module</span>.exports = &#123;
  <span class="hljs-attr">publicPath</span>: <span class="hljs-string">'/system/'</span>, <span class="hljs-comment">//这里打包地址都要基于主应用的中注册的entry值</span>
  <span class="hljs-attr">output</span>: &#123;
    <span class="hljs-attr">library</span>: <span class="hljs-string">'ManageMicroApp'</span>, <span class="hljs-comment">// 库名，与主应用注册的微应用的name一致</span>
    <span class="hljs-attr">libraryTarget</span>: <span class="hljs-string">'umd'</span>, <span class="hljs-comment">// 这个选项会尝试把库暴露给前使用的模块定义系统，这使其和CommonJS、AMD兼容或者暴露为全局变量。</span>
    <span class="hljs-attr">jsonpFunction</span>: <span class="hljs-string">`webpackJsonp_<span class="hljs-subst">$&#123;packageName&#125;</span>`</span>,
  &#125;,
&#125;;
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-16">关键点总结</h4>
<ul>
<li>
<p>主应用注册时的配置</p>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-keyword">const</span> apps = [
  &#123;
    <span class="hljs-attr">name</span>: <span class="hljs-string">'ManageMicroApp'</span>,
    <span class="hljs-attr">entry</span>: <span class="hljs-string">'/system/'</span>,  <span class="hljs-comment">// http://localhost/system/ 这里会通过nginx代理指向对应的子应用地址</span>
    <span class="hljs-attr">container</span>: <span class="hljs-string">'#frame'</span>,
    <span class="hljs-attr">activeRule</span>: <span class="hljs-string">'/manage'</span>,
  &#125;,
]
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>主应用注册微应用时，<code>entry</code> 可以为相对路径，<code>activeRule</code> 不可以和 <code>entry</code> 一样（否则主应用页面刷新就变成微应用）</strong></p>
</li>
<li>
<p>vue路由的base</p>
<pre><code class="hljs language-js copyable" lang="js">router = <span class="hljs-keyword">new</span> VueRouter(&#123;
  <span class="hljs-attr">base</span>: <span class="hljs-built_in">window</span>.__POWERED_BY_QIANKUN__ ? <span class="hljs-string">'/manage/'</span> : <span class="hljs-string">'/'</span>,
  <span class="hljs-attr">mode</span>: <span class="hljs-string">'history'</span>,
  routes
&#125;);
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>如果是主应用调用的那么路由的base为<code>/manage/</code></strong></p>
</li>
<li>
<p>webpack打包配置</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-built_in">module</span>.exports = &#123;
  <span class="hljs-attr">publicPath</span>: <span class="hljs-string">'/system/'</span>,
&#125;;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>对于 <code>webpack</code> 构建的微应用，微应用的 <code>webpack</code> 打包的 <code>publicPath</code> 需要配置成 <code>/system/</code>，否则微应用的 <code>index.html</code> 能正确请求，但是微应用 <code>index.html</code> 里面的 <code>js/css</code> 路径不会带上 <code>/system/</code>。</strong></p>
</li>
</ul>
<p>到这里我们把微前端的配置做好了，接下来就是nginx的配置。</p>
<h2 data-id="heading-17">生产环境Nginx配置</h2>
<p>先把主应用的nginx配置挂一下</p>
<pre><code class="hljs language-nginx copyable" lang="nginx">    <span class="hljs-section">server</span> &#123;
        <span class="hljs-attribute">listen</span>       <span class="hljs-number">80</span>;
        <span class="hljs-attribute">listen</span>       [::]:<span class="hljs-number">80</span> default_server;
        <span class="hljs-attribute">server_name</span>  localhost;
        <span class="hljs-attribute">root</span>         /usr/share/nginx/html;

        <span class="hljs-attribute">location</span> / &#123;
            <span class="hljs-attribute">try_files</span> $uri $uri/ /index.html;
            <span class="hljs-attribute">index</span> index.html;
        &#125;
<span class="hljs-comment"># 前面我们配置的子应用entry是/system/，所以会触发这里的代理，代理到对应的子应用</span>
        <span class="hljs-attribute">location</span> /system/ &#123;
     <span class="hljs-comment"># -e表示只要filename存在，则为真，不管filename是什么类型，当然这里加了!就取反</span>
             <span class="hljs-attribute">if</span> (!-e $request_filename) &#123;
                <span class="hljs-attribute">proxy_pass</span> http://192.168.1.2; <span class="hljs-comment"># 这里的ip是子应用docker容器的ip</span>
             &#125;
     <span class="hljs-comment"># -f filename 如果 filename为常规文件，则为真</span>
             <span class="hljs-attribute">if</span> (!-f $request_filename) &#123;
                <span class="hljs-attribute">proxy_pass</span> http://192.168.1.2;
             &#125;
             <span class="hljs-comment"># docker运行的nginx不识别localhost的 所以这种写法会报502</span>
             <span class="hljs-comment"># proxy_pass  http://localhost:10200/;</span>
             <span class="hljs-attribute">proxy_set_header</span> Host $host;
         &#125;

        <span class="hljs-attribute">location</span> /api/ &#123;
            <span class="hljs-attribute">proxy_pass</span> http://后台地址IP/;
            <span class="hljs-attribute">proxy_set_header</span> Host $host;
            <span class="hljs-attribute">proxy_set_header</span> X-Real-IP $remote_addr;
            <span class="hljs-attribute">proxy_set_header</span> REMOTE-HOST $remote_addr;
            <span class="hljs-attribute">proxy_set_header</span> X-Forwarded-For $proxy_add_x_forwarded_for;
        &#125;

        <span class="hljs-attribute">error_page</span> <span class="hljs-number">404</span> /<span class="hljs-number">404</span>.html;
            <span class="hljs-attribute">location</span> = /40x.html &#123;
        &#125;

        <span class="hljs-attribute">error_page</span> <span class="hljs-number">500</span> <span class="hljs-number">502</span> <span class="hljs-number">503</span> <span class="hljs-number">504</span> /50x.html;
            <span class="hljs-attribute">location</span> = /50x.html &#123;
        &#125;
    &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>再看一下子应用的</p>
<pre><code class="hljs language-nginx copyable" lang="nginx"><span class="hljs-section">server</span> &#123;
    <span class="hljs-attribute">listen</span>       <span class="hljs-number">80</span>;
    <span class="hljs-attribute">listen</span>       [::]:<span class="hljs-number">80</span> default_server;
    <span class="hljs-attribute">server_name</span>  _2;
    <span class="hljs-attribute">root</span>         /usr/share/nginx/html;

    <span class="hljs-comment"># 这里必须加上允许跨域，否则主应用无法访问</span>
    <span class="hljs-attribute">add_header</span> Access-Control-Allow-Origin *;
    <span class="hljs-attribute">add_header</span> Access-Control-Allow-Methods <span class="hljs-string">'GET, POST, OPTIONS'</span>;
    <span class="hljs-attribute">add_header</span> Access-Control-Allow-Headers <span class="hljs-string">'DNT,X-Mx-ReqToken,Keep-Alive,User-Agent,X-Requested-With,If-Modified-Since,Cache-Control,Content-Type,Authorization'</span>;

    <span class="hljs-attribute">location</span> / &#123;
        <span class="hljs-attribute">try_files</span> $uri $uri/ /index.html;
        <span class="hljs-attribute">index</span> index.html;
    &#125;

    <span class="hljs-attribute">location</span> /api/ &#123;
        <span class="hljs-attribute">proxy_pass</span> http://后台地址IP/;
        <span class="hljs-attribute">proxy_set_header</span> Host $host;
        <span class="hljs-attribute">proxy_set_header</span> X-Real-IP $remote_addr;
        <span class="hljs-attribute">proxy_set_header</span> REMOTE-HOST $remote_addr;
        <span class="hljs-attribute">proxy_set_header</span> X-Forwarded-For $proxy_add_x_forwarded_for;
    &#125;

    <span class="hljs-attribute">error_page</span> <span class="hljs-number">404</span> /<span class="hljs-number">404</span>.html;
        <span class="hljs-attribute">location</span> = /40x.html &#123;
    &#125;

    <span class="hljs-attribute">error_page</span> <span class="hljs-number">500</span> <span class="hljs-number">502</span> <span class="hljs-number">503</span> <span class="hljs-number">504</span> /50x.html;
        <span class="hljs-attribute">location</span> = /50x.html &#123;
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-18">dockerfile配置</h2>
<p>这里先看一下子应用的</p>
<pre><code class="hljs language-dockerfile copyable" lang="dockerfile"><span class="hljs-comment"># 直接使用nginx镜像</span>
<span class="hljs-keyword">FROM</span> nginx
<span class="hljs-comment"># 把上面配置的conf文件替换一下默认的</span>
<span class="hljs-keyword">COPY</span><span class="bash"> nginx.conf /etc/nginx/nginx.conf</span>
<span class="hljs-comment"># nginx默认目录下需要能看见index.html文件</span>
<span class="hljs-keyword">COPY</span><span class="bash"> dist/index.html /usr/share/nginx/html/index.html</span>
<span class="hljs-comment"># 再回头看一下部署逻辑图和qiankun注意点，必须要把所有的资源文件放到system文件下index.html才能正确加载</span>
<span class="hljs-keyword">COPY</span><span class="bash"> dist /usr/share/nginx/html/system</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>再看一下主应用的</p>
<pre><code class="hljs language-dockerfile copyable" lang="dockerfile"><span class="hljs-comment"># 这里主应用没有直接使用nginx，因为nginx反向代理的/api/会出现404的问题，原因未知！</span>
<span class="hljs-keyword">FROM</span> centos
<span class="hljs-comment"># 安装nginx</span>
<span class="hljs-keyword">RUN</span><span class="bash"> yum install -y nginx</span>
<span class="hljs-comment"># 跳转到/etc/nginx</span>
<span class="hljs-keyword">WORKDIR</span><span class="bash"> /etc/nginx</span>
<span class="hljs-comment"># 替换配置文件</span>
<span class="hljs-keyword">COPY</span><span class="bash"> nginx.conf nginx.conf</span>
<span class="hljs-comment"># 跳转到/usr/share/nginx/html</span>
<span class="hljs-keyword">WORKDIR</span><span class="bash"> /usr/share/nginx/html</span>
<span class="hljs-comment"># 主应用正常打包，所以直接把包放进去就行</span>
<span class="hljs-keyword">COPY</span><span class="bash"> dist .</span>
<span class="hljs-comment"># 暴露80端口</span>
<span class="hljs-keyword">EXPOSE</span> <span class="hljs-number">80</span>
<span class="hljs-comment"># 运行nginx</span>
<span class="hljs-keyword">CMD</span><span class="bash"> nginx -g <span class="hljs-string">"daemon off;"</span></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-19">gitlab-ci/cd配置</h2>
<p>先看一下子应用的，<strong>只说重点的</strong></p>
<pre><code class="hljs language-yaml copyable" lang="yaml"><span class="hljs-attr">image:</span> <span class="hljs-string">node</span>

<span class="hljs-attr">stages:</span>
  <span class="hljs-bullet">-</span> <span class="hljs-string">install</span>
  <span class="hljs-bullet">-</span> <span class="hljs-string">build</span>
  <span class="hljs-bullet">-</span> <span class="hljs-string">deploy</span>
  <span class="hljs-bullet">-</span> <span class="hljs-string">clear</span>

<span class="hljs-attr">cache:</span>
  <span class="hljs-attr">key:</span> <span class="hljs-string">modules-cache</span>
  <span class="hljs-attr">paths:</span>
    <span class="hljs-bullet">-</span> <span class="hljs-string">node_modules</span>
    <span class="hljs-bullet">-</span> <span class="hljs-string">dist</span>

<span class="hljs-string">安装环境:</span>
  <span class="hljs-attr">stage:</span> <span class="hljs-string">install</span>
  <span class="hljs-attr">tags:</span>
    <span class="hljs-bullet">-</span> <span class="hljs-string">vue</span>
  <span class="hljs-attr">script:</span>
    <span class="hljs-bullet">-</span> <span class="hljs-string">npm</span> <span class="hljs-string">install</span> <span class="hljs-string">yarn</span>
    <span class="hljs-bullet">-</span> <span class="hljs-string">yarn</span> <span class="hljs-string">install</span>

<span class="hljs-string">打包项目:</span>
  <span class="hljs-attr">stage:</span> <span class="hljs-string">build</span>
  <span class="hljs-attr">tags:</span>
    <span class="hljs-bullet">-</span> <span class="hljs-string">vue</span>
  <span class="hljs-attr">script:</span>
    <span class="hljs-bullet">-</span> <span class="hljs-string">yarn</span> <span class="hljs-string">build</span>

<span class="hljs-string">部署项目:</span>
  <span class="hljs-attr">stage:</span> <span class="hljs-string">deploy</span>
  <span class="hljs-attr">image:</span> <span class="hljs-string">docker</span>
  <span class="hljs-attr">tags:</span>
    <span class="hljs-bullet">-</span> <span class="hljs-string">vue</span>
  <span class="hljs-attr">script:</span>
  <span class="hljs-comment"># 通过dockerfile构建项目的镜像</span>
    <span class="hljs-bullet">-</span> <span class="hljs-string">docker</span> <span class="hljs-string">build</span> <span class="hljs-string">-t</span> <span class="hljs-string">rainbow-system</span> <span class="hljs-string">.</span>
    <span class="hljs-comment"># 如果存在之前创建的容器先删除</span>
    <span class="hljs-bullet">-</span> <span class="hljs-string">if</span> [ <span class="hljs-string">$(docker</span> <span class="hljs-string">ps</span> <span class="hljs-string">-aq</span> <span class="hljs-string">--filter</span> <span class="hljs-string">name=rainbow-admin-system)</span> ]<span class="hljs-string">;then</span> <span class="hljs-string">docker</span> <span class="hljs-string">rm</span> <span class="hljs-string">-f</span> <span class="hljs-string">rainbow-admin-system;fi</span>
    <span class="hljs-comment"># 通过刚刚的镜像创建一个容器 给容器指定一个网卡rainbow-net，这个网卡是我们自定义，创建方式后面会说，然后给定一个ip</span>
    <span class="hljs-bullet">-</span> <span class="hljs-string">docker</span> <span class="hljs-string">run</span> <span class="hljs-string">-d</span> <span class="hljs-string">--net</span> <span class="hljs-string">rainbow-net</span> <span class="hljs-string">--ip</span> <span class="hljs-number">192.168</span><span class="hljs-number">.1</span><span class="hljs-number">.2</span> <span class="hljs-string">--name</span> <span class="hljs-string">rainbow-admin-system</span> <span class="hljs-string">rainbow-system</span>

<span class="hljs-string">清理docker:</span>
  <span class="hljs-attr">stage:</span> <span class="hljs-string">clear</span>
  <span class="hljs-attr">image:</span> <span class="hljs-string">docker</span>
  <span class="hljs-attr">tags:</span>
    <span class="hljs-bullet">-</span> <span class="hljs-string">vue</span>
  <span class="hljs-attr">script:</span>
    <span class="hljs-bullet">-</span> <span class="hljs-string">if</span> [ <span class="hljs-string">$(docker</span> <span class="hljs-string">ps</span> <span class="hljs-string">-aq</span> <span class="hljs-string">|</span> <span class="hljs-string">grep</span> <span class="hljs-string">"Exited"</span> <span class="hljs-string">|</span> <span class="hljs-string">awk</span> <span class="hljs-string">'&#123;print $1 &#125;'</span><span class="hljs-string">)</span> ]<span class="hljs-string">;</span> <span class="hljs-string">then</span> <span class="hljs-string">docker</span> <span class="hljs-string">stop</span> <span class="hljs-string">$(docker</span> <span class="hljs-string">ps</span> <span class="hljs-string">-a</span> <span class="hljs-string">|</span> <span class="hljs-string">grep</span> <span class="hljs-string">"Exited"</span> <span class="hljs-string">|</span> <span class="hljs-string">awk</span> <span class="hljs-string">'&#123;print $1 &#125;'</span><span class="hljs-string">);fi</span>
    <span class="hljs-bullet">-</span> <span class="hljs-string">if</span> [ <span class="hljs-string">$(docker</span> <span class="hljs-string">ps</span> <span class="hljs-string">-aq</span> <span class="hljs-string">|</span> <span class="hljs-string">grep</span> <span class="hljs-string">"Exited"</span> <span class="hljs-string">|</span> <span class="hljs-string">awk</span> <span class="hljs-string">'&#123;print $1 &#125;'</span><span class="hljs-string">)</span> ]<span class="hljs-string">;</span> <span class="hljs-string">then</span> <span class="hljs-string">docker</span> <span class="hljs-string">rm</span> <span class="hljs-string">$(docker</span> <span class="hljs-string">ps</span> <span class="hljs-string">-a</span> <span class="hljs-string">|</span> <span class="hljs-string">grep</span> <span class="hljs-string">"Exited"</span> <span class="hljs-string">|</span> <span class="hljs-string">awk</span> <span class="hljs-string">'&#123;print $1 &#125;'</span><span class="hljs-string">);fi</span>
    <span class="hljs-bullet">-</span> <span class="hljs-string">if</span> [ <span class="hljs-string">$(docker</span> <span class="hljs-string">images</span> <span class="hljs-string">|</span> <span class="hljs-string">grep</span> <span class="hljs-string">"none"</span> <span class="hljs-string">|</span> <span class="hljs-string">awk</span> <span class="hljs-string">'&#123;print $3&#125;'</span><span class="hljs-string">)</span> ]<span class="hljs-string">;</span> <span class="hljs-string">then</span> <span class="hljs-string">docker</span> <span class="hljs-string">rmi</span> <span class="hljs-string">$(docker</span> <span class="hljs-string">images</span> <span class="hljs-string">|</span> <span class="hljs-string">grep</span> <span class="hljs-string">"none"</span> <span class="hljs-string">|</span> <span class="hljs-string">awk</span> <span class="hljs-string">'&#123;print $3&#125;'</span><span class="hljs-string">);fi</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>再看一下主应用的，省略重复的，直接看重点</p>
<pre><code class="hljs language-yaml copyable" lang="yaml"><span class="hljs-string">部署项目:</span>
  <span class="hljs-attr">stage:</span> <span class="hljs-string">deploy</span>
  <span class="hljs-attr">image:</span> <span class="hljs-string">docker</span>
  <span class="hljs-attr">tags:</span>
    <span class="hljs-bullet">-</span> <span class="hljs-string">vue3</span>
  <span class="hljs-attr">script:</span>
    <span class="hljs-bullet">-</span> <span class="hljs-string">docker</span> <span class="hljs-string">build</span> <span class="hljs-string">-t</span> <span class="hljs-string">rainbow-admin</span> <span class="hljs-string">.</span>
    <span class="hljs-bullet">-</span> <span class="hljs-string">if</span> [ <span class="hljs-string">$(docker</span> <span class="hljs-string">ps</span> <span class="hljs-string">-aq</span> <span class="hljs-string">--filter</span> <span class="hljs-string">name=rainbow-admin-main)</span> ]<span class="hljs-string">;then</span> <span class="hljs-string">docker</span> <span class="hljs-string">rm</span> <span class="hljs-string">-f</span> <span class="hljs-string">rainbow-admin-main;fi</span>
    <span class="hljs-comment"># 给容器指定一个网卡rainbow-net，然后给定一个ip，然后通过--link与之前创建的子应用连通，重点！</span>
    <span class="hljs-bullet">-</span> <span class="hljs-string">docker</span> <span class="hljs-string">run</span> <span class="hljs-string">-d</span> <span class="hljs-string">-p</span> <span class="hljs-number">80</span><span class="hljs-string">:80</span> <span class="hljs-string">--net</span> <span class="hljs-string">rainbow-net</span> <span class="hljs-string">--ip</span> <span class="hljs-number">192.168</span><span class="hljs-number">.1</span><span class="hljs-number">.1</span> <span class="hljs-string">--link</span> <span class="hljs-number">192.168</span><span class="hljs-number">.1</span><span class="hljs-number">.2</span> <span class="hljs-string">--name</span> <span class="hljs-string">rainbow-admin-main</span> <span class="hljs-string">rainbow-admin</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>上面说到了docker的自定义网卡，生成的命令如下：</p>
<pre><code class="hljs language-bash copyable" lang="bash">$ docker network create --driver bridge --subnet 192.168.0.0/16 --gateway 192.168.0.1 rainbow-net
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-20">总结</h2>
<p>到这里我们已经实现了qiankun+docker配合gitlab-ci/cd的自动化部署，中间遇到很多坑，然后走出了一条相对合理的解决方案，有问题欢迎讨论。</p></div>  
</div>
            