
---
title: '能让你纵享丝滑的SSR技术，转转这样实践'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/f29db90fddb24b06b7f419ff034399e3~tplv-k3u1fbpfcp-zoom-1.image'
author: 掘金
comments: false
date: Thu, 22 Apr 2021 07:56:12 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/f29db90fddb24b06b7f419ff034399e3~tplv-k3u1fbpfcp-zoom-1.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><figure><img alt class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/f29db90fddb24b06b7f419ff034399e3~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></figure>
<h2 data-id="heading-0"><span class="prefix"></span><span class="content">SSR最佳实践</span><span class="suffix"></span></h2>
<p>秒开率对于用户的留存率有直接的影响,数据表明, 网页加载时间过长会直接导致用户流失.转转集团作为一家电商公司, 对于H5页面的秒开率有着更加严格的需求, 在主要的卖场侧页面(手机频道页、3c频道页、活动页)等重要流量入口我们都采用了SSR（服务端渲染）技术来构建页面,今天就带大家了解一下我们摸索出来的一些最佳实践.</p>
<h3 data-id="heading-1"><span class="prefix"></span><span class="content">网页的前世今生</span><span class="suffix"></span></h3>
<p>在早期的web应用中,实际上我们都是用的服务端渲染技术, 像jsp、asp、php等各种后台模板生成的页面,前端都是拿到整张页面,不用自己去拼接DOM.后来随着前后端分离开发模式,衍生出了最主要的两种渲染方式CSR以及SSR.</p>
<ul>
<li><p><strong>CSR : 客户端渲染</strong>,整个渲染流程是:  浏览器请求url --> 服务器返回index.html(空body、白屏) --> 再次请求bundle.js、路由分析 --> 浏览器渲染
<strong>bundle.js体积越大, 就会导致白屏的时间越长,给用户的体验就越差</strong>(当然，这可以借助打包构建工具来优化这部分)</p>
<p>交互流程图如下
<img alt class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/fa13446f9e8542eeb8de1b651bb33aff~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
</li></ul>
   图1-1客户端渲染流程图
<ul>
<li><p><strong>SSR</strong> <strong>: 服务端渲染</strong>,  服务端渲染分为两个步骤:</p>
</li><li><p>阶段一:  浏览器请求url --> 服务器路由分析、执行渲染 --> 服务器返回index.html(实时渲染的内容，字符串) --> 浏览器渲染  <strong>(此时是一个静态页面, 不可交互, 依赖于服务端的能力, 这就是快的原因)</strong></p>
</li><li><p>阶段二：浏览器请求bundle.js --> 服务器返回bundle.js --> 浏览器路由分析、生成虚拟DOM --> 比较DOM变化、绑定事件 --> 二次渲染 <strong>(用户可交互)</strong></p>
</li></ul>
<p>我们来看看整个交互流程图 :</p>
<div>
   <img alt="图片名称" width="45%" align="center" class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/177040fbbdc94f72b7f51b6f358d7100~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"> 
  <img alt="图片名称" align="center" width="45%" class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/1301285146d94e9d80f2380371627f76~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer">
</div> 
 图 1-2 服务端渲染交互流程图
<h3 data-id="heading-2"><span class="prefix"></span><span class="content">SSR构建逻辑</span><span class="suffix"></span></h3>
<p>理解了两种渲染模式的异同,我们来看看SSR整个构建逻辑(主要以Vue-SSR为例)</p>
<p>我们以官网的图片为例:</p>
<figure><img alt class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/c0a7268ab44f424bb790856840c1a351~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></figure>
图 2-1 SSR构建逻辑
<p>从图中我们可以知道 :</p>
<p>在整个构建过程中, 我们有两个入口, 一个是server-entry.js, 执行server端的逻辑, 一个是client.js, 执行client端的逻辑, 然后通过会将webpack打包分成两个Bundle: 服务端bundle; 客户端bundle. Node.js会处理服务端bundle用于SSR, 客户端bundle会在用户请求时和已经由SSR渲染出的页面一起返回给用户, 然后在浏览器执行”注水”(<code>hydrate</code>), 接管Vue接下来的业务逻辑.</p>
<p>理解了整个构建逻辑,接下来我们来看看我们是怎么运用SSR来服务我们的项目的.</p>
<h3 data-id="heading-3"><span class="prefix"></span><span class="content">SSR构建项目的背景</span><span class="suffix"></span></h3>
<p>卖场侧业务首页组成大同小异: 主要分首屏和第二屏, 首屏有多个模块组成, 第二屏是商品Feed流,便于读者理解, 我们抽象出了页面结构图:</p>
<div>
   <img alt="图片名称" width="45%" align="center" class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/f588559e3c524b82bf5c01681fcc26f1~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"> 
  <img alt="图片名称" align="center" width="45%" class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/13fa1aa457dd4d49b3486cbad7a08eda~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer">
</div> 
图 2-2 页面结构图
<p>(欢迎大家下载转转app体验)</p>
<p>而且这些页面都有一个共同的特点:</p>
<ul>
<li>只用于展示, 和用户的状态不强绑定(不需要用户登录)</li><li>页面状态稳定,内容不会经常变更</li><li>都是重要流量的第一个入口(首页)</li></ul>
<p>由于对于秒开率有着极高的要求,又承载了主要流量入口,结合以上页面特点,所以我们使用了SSR来提升用户体验.</p>
<p>经过一系列的探索和探究, 我们最终使用Nuxt.js来作为我们的技术选型.</p>
<p>这里提下为啥使用Nuxt.js作为我们的技术选型, 主要原因有以下几点:</p>
<ol>
<li>集团内部C端业务是以Vue技术栈为主,B端技术栈是以React为主, 所以不考虑React服务端渲染技术栈;</li><li>Nuxt.js是开箱即用的服务端渲染框架,不用开发人员自己去搭建Vue+ Vue-server-renderer + vuex来集成服务端渲染框架, 接入成本比较低.</li></ol>
<h3 data-id="heading-4"><span class="prefix"></span><span class="content">SSR运用的最佳实践</span><span class="suffix"></span></h3>
<p>目前我们使用SSR实现的主要能力有:</p>
<ul>
<li>首屏使用服务端渲染,第二屏使用客户端渲染,首屏模块数据可调整,即优化了性能, 又丰富了页面配置.</li><li>合理化使用缓存, 进一步提升用户体验.</li><li>实现css注入,达到按需换肤的效果.</li><li>使用ErrorBoundary拦截错误,使得组件错误不会影响整个页面白屏.</li><li>按需加载第二屏数据,只有滑动到可见范围, 才加载第二屏数据</li><li>针对大促场景, 结合服务端能力, 以及各种监控,docker扩容,保证页面稳定.</li></ul>
<p>接下来就和大家探索其中几种能力的主要思路:</p>
<h4 data-id="heading-5"><span class="prefix"></span><span class="content">怎样实现首屏使用服务端渲染,第二屏使用客户端渲染</span><span class="suffix"></span></h4>
<p>这种实现方式主要是结合asyncData在服务端异步获取数据,使用vue动态组件component的特性,来调整模块的渲染顺序; mounted生命钩子只会在客户端执行, 使用仅在客户端渲染组件的特性来实现的.</p>
<p>示例代码:</p>
<pre class="custom"><span></span><code class="hljs copyable"><template><br>  <!--服务端渲染,动态获取首屏模块并且加载对应模块的数据, 使用error-boundary来拦截错误--><br>  <template v-for=<span class="hljs-string">"(e, i) in structureOrder"</span>><br>    <error-boundary><br>      <component :info=<span class="hljs-string">"activityState.structure[e]"</span><br>                 :is=<span class="hljs-string">"Mutations.name2Component(e)"</span><br>                 class=<span class="hljs-string">"anchor"</span><br>                 :id=<span class="hljs-string">"e"</span><br>                 :key=<span class="hljs-string">"i"</span> :name=<span class="hljs-string">"e"</span> v-if=<span class="hljs-string">"activityState.structure[e] || e === 'bar' "</span>/><br>    </error-boundary><br>  </template><br>  <!--客户端渲染--><br>  <client-only><br>    <!--滑动到可见范围加载对应的数据--><br>    <div :is=<span class="hljs-string">"listComponent"</span> :tab=<span class="hljs-string">"labelFilter"</span>/><br>  </client-only><br></template><br><span class="copy-code-btn">复制代码</span></code></pre>
<p>获取数据:</p>
<pre class="custom"><span></span><code class="hljs copyable">//服务端渲染数据<br>async asyncData(&#123;app, route, req&#125;) &#123;<br>  const initData = await app.<span class="hljs-variable">$axios</span>.<span class="hljs-variable">$get</span>(host, &#123;<br>    params: &#123;<br>      name: key, from, smark, keys: `structure,base,labelFilter,navigate,redPack,<span class="hljs-variable">$&#123;elements&#125;</span>`<br>    &#125;, headers<br>  &#125;)<br>  const &#123;structureInfo, structureOrder, restStructure, anchors&#125; = Mutations.initStructure(initData)<br>  <span class="hljs-built_in">return</span> &#123;<br>    structureInfo,<br>    restStructure,<br>    structureOrder, //动态返回对应模块的名称<br>    useVideo: Mutations.checkUseVideo(req),<br>    theme,<br>    pageFrom: route.query.from,<br>    isPOP,<br>    anchors,<br>    ...formInfo<br>  &#125;<br>&#125;,<br>async <span class="hljs-function"><span class="hljs-title">mounted</span></span>() &#123;<br>    //获取客户端渲染的数据<br>   const res = await this.initData()<br>&#125;,<br><span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-6"><span class="prefix"></span><span class="content">怎样使用ErrorBoundary捕获组件级别错误,避免整个页面白屏</span><span class="suffix"></span></h4>
<p>关于ErrorBoundary这个捕获错误的组件,这个组件的主要功能是使得组件级的错误不会蔓延到页面级,不会造成整个页面的白屏,考虑到服务端渲染可能会发生偶发性错误,状态容易变的不可控, 所以使用这个能力还是很有必要的, 这个组件主要使用vue提供的 errorCaptured 来捕获组件级的错误, 想详细了解这个api的作用可以去看官方文档,具体的实现如下:</p>
<pre class="custom"><span></span><code class="hljs copyable">const errorBoundary = Vue => &#123;<br>  Vue.component(<span class="hljs-string">'ErrorBoundary'</span>, &#123;<br>    data: () => (&#123; error: null &#125;),<br>    errorCaptured(err, vm, info) &#123;<br>      this.error = `<span class="hljs-variable">$&#123;err.stack&#125;</span>\n\nfound <span class="hljs-keyword">in</span> <span class="hljs-variable">$&#123;info&#125;</span> of component`<br>      SentryCapture(err, 1) //异常上报到sentry<br>      <span class="hljs-built_in">return</span> <span class="hljs-literal">false</span><br>    &#125;,<br>    <span class="hljs-function"><span class="hljs-title">render</span></span>() &#123;<br>      <span class="hljs-built_in">return</span> (this.<span class="hljs-variable">$slots</span>.default || [null])[0] || null<br>    &#125;<br>  &#125;)<br>&#125;<br><br>// 全局注册errorBoundary<br>Vue.use(errorBoundary)<br><span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-7"><span class="prefix"></span><span class="content">怎样实现css注入,实现页面换肤</span><span class="suffix"></span></h4>
<p>这个功能的主要作用是 : 可以根据配置json文件定制化活动页面的样式, 做到"千人千面" (一个会场的key可以配置一种样式, 但是底层代码是一套),使得元素多样化,在视觉上给用户体验带来很大提升.</p>
<p>我们先来看看效果示意图:
<img alt="图片名称" align="center" width="100%" class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/b9aa9a96ba834964802c661adabf1038~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p>以上就是展示效果, 借住CSS注入, 我们可以根据不同的json文件来定制化页面的样式, 只需要维护一套代码, 简单高效.</p>
<p>实现逻辑也很简单,主要是运用了Nuxt.js框架提供的head方法:</p>
<pre class="custom"><span></span><code class="hljs copyable"><span class="hljs-function"><span class="hljs-title">head</span></span>() &#123;<br>            //this.baseInfo.additionStyle是从json文件拿到的样式<br>      //通过css权重, 可以实现样式覆盖<br>      <span class="hljs-built_in">return</span> &#123;<br>        style: [<br>          &#123;cssText: this.baseInfo?.additionStyle || <span class="hljs-string">''</span>, <span class="hljs-built_in">type</span>: <span class="hljs-string">'text/css'</span>&#125;<br>        ],<br>        __dangerouslyDisableSanitizers: [<span class="hljs-string">'style'</span>]  // 防止对一些选择器的特殊字符进行转义<br>      &#125;<br>    &#125;,<br><span class="copy-code-btn">复制代码</span></code></pre>
<p>不仅如此, 还可以实现js注入, 感兴趣的小伙伴可以自己去了解,底层原理可以了解下 <strong>vue-meta</strong> 这个库</p>
<p>但是, 随着业务的不断迭代, 这种注入方式还是存在很多可优化的点:</p>
<ul>
<li>每个活动页运营同学都要维护一份json文件,里面包含冗长的css配置字段, 活动规则等等, 特别是css配置字段,就是一段冗长的css, 给运营和开发同学带来很大的不便;</li><li>运营同学维护成本高,学习成本高,操作成本高;</li><li>对于UI同学成本也大, 每次都需要UI同学来设计活动页面样式;</li></ul>
<p>目前, 集团内部正在使用 <strong>魔方</strong> 一步一步去替代这种方式, <strong>魔方</strong> 只需要运营同学拖拖拽拽, 就能生成一个活动页, 简单高效, 想要了解魔方的同学, 可以<strong>继续关注我们的公众号</strong></p>
<h4 data-id="heading-8"><span class="prefix"></span><span class="content">怎样实现组件滑动到可见范围,才加载数据</span><span class="suffix"></span></h4>
<p>其实这种优化页面的方法并不是说只适用于SSR, 其他非SSR页面也可以使用这种方式来优化;</p>
<p>看看我们的实现方式 :</p>
<pre class="custom"><span></span><code class="hljs copyable"><span class="hljs-keyword">function</span> asyncComponent(&#123;componentFactory, loading = <span class="hljs-string">'div'</span>, loadingData = <span class="hljs-string">'loading'</span>, errorComponent, rootMargin = <span class="hljs-string">'0px'</span>,retry= 2&#125;) &#123;<br>  <span class="hljs-built_in">let</span> resolveComponent;<br>  <span class="hljs-built_in">return</span> () => (&#123;<br>    component: new Promise(resolve => resolveComponent = resolve),<br>    loading: &#123;<br>      <span class="hljs-function"><span class="hljs-title">mounted</span></span>() &#123;<br>        const observer = new IntersectionObserver(([entries]) => &#123;<br>          <span class="hljs-keyword">if</span> (!entries.isIntersecting) <span class="hljs-built_in">return</span>;<br>          observer.unobserve(this.<span class="hljs-variable">$el</span>);<br><br>          <span class="hljs-built_in">let</span> p = Promise.reject();<br>          <span class="hljs-keyword">for</span> (<span class="hljs-built_in">let</span> i = 0; i < retry; i++) &#123;<br>            p = p.catch(componentFactory);<br>          &#125;<br>          p.then(resolveComponent).catch(e => console.error(e));<br>        &#125;, &#123;<br>          root: null,<br>          rootMargin,<br>          threshold: [0]<br>        &#125;);<br>        observer.observe(this.<span class="hljs-variable">$el</span>);<br>      &#125;,<br>      render(h) &#123;<br>        <span class="hljs-built_in">return</span> h(loading, loadingData);<br>      &#125;,<br>    &#125;,<br>    error: errorComponent,<br>    delay: 200<br>  &#125;);<br>&#125;<br><br><span class="hljs-built_in">export</span> default &#123;<br>  install: (Vue, option) => &#123;<br>    Vue.prototype.<span class="hljs-variable">$loadComponent</span> = componentFactory => &#123;<br>      <span class="hljs-built_in">return</span> asyncComponent(Object.assign(option, &#123;<br>        componentFactory<br>      &#125;))<br>    &#125;<br>  &#125;<br>&#125;<br><span class="copy-code-btn">复制代码</span></code></pre>
<p>实现原理主要是使用vue高阶组件, 元素到达可见范围内, 延迟加载组件;</p>
<p>看看效果图:</p>
   <img alt="图片名称" align="center" width="100%" class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/04fcefb3ea514a7ea487725ebbcdeb9a~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer">
<p>我们可以看到,只有到底部商品Feed流出现在可视范围,才去请求对应的接口</p>
<h4 data-id="heading-9"><span class="prefix"></span><span class="content">针对大促场景怎样保证页面稳定</span><span class="suffix"></span></h4>
<p>所谓大促场景,是指像 6.18, 双11,这种场景下, 面对大流量, 如何保证页面稳定? SSR是CPU密集型任务, 意味着很耗费服务器资源,集团目前主要采取的策略是:</p>
<ul>
<li>对接口进行压测, 模拟高并发场景下页面性能, 接口响应速度;</li><li>集团内部实现了一套监控系统, 可以实时监控CPU,内存的消耗情况;</li><li>需要有服务器扩容方案, 比如接入docker, 可以实现服务器实时扩容</li></ul>
<h4 data-id="heading-10"><span class="prefix"></span><span class="content">怎样利用缓存</span><span class="suffix"></span></h4>
<p>请大家移步集团一位前端大佬写的公众号文章: <a href="https://mp.weixin.qq.com/s/XmIcE4kWN1fzHD_DoqeFFw?st=44750C9EB200D36504EB6D425B420DBB6B15C56ACA80A204C54C8323EDC1801EA5A5F3B820B554A82F62E4033B31A51709D75E975D62F9DF6D44CAE16D1789B8AD72E2CD5F9B783F67AD99F4F2798CF2C68E30FA529A9493650C4F2DBC668A6BDF60C19EBD53E8095436171B77B43F8379F0786B6B7CC24FF5D8D3F7E9234CB1AAF8E432ACBF7660C8D5A46943940625F334223CFD292F52C622C9D71CA23109&vid=1688853671357556&cst=84C66BDBB38DB9209F2CBE20568358526FE0CB352D65E68D84CDC8560959A5D0CF245948AFF68C1B51377FEEFF49EFA4&deviceid=28ea5b9c-c888-47c9-a3cf-e19b1d9eaf5c&version=3.0.40.6184&platform=mac" target="_blank" rel="nofollow noopener noreferrer">Nuxt实现的SSR页面性能优化的进一步探索与实践</a></p>
<p>最终,看看我们最终的实现效果:</p>
<img alt="图片名称" align="center" width="100%" class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/66fe644575794e92a2aae5a90b89490d~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer">
<p>可以看到, 首屏渲染时间在<strong>594ms</strong>, 秒开率在<strong>百分之87</strong>左右;</p>
<h3 data-id="heading-11"><span class="prefix"></span><span class="content">SSR的不足</span><span class="suffix"></span></h3>
<p>ssr的使用过程并不是一帆风顺的, 在使用的过程中, 也总结几点不足之处:</p>
<ul>
<li>对于开发人员的要求更高, 要学习其他的额外知识,例如: Linux , node相关知识, 需要具备一定的后端思维;</li><li>服务端渲染接口抓包不方便, 我们在客户端抓取不到服务端的接口请求, 不过对于使用Mac电脑开发的同学,可以使用 proxychains-ng 来抓取服务端请求的接口</li><li>冗长的配置环境过程, 每次开发联调需要配置后端host</li><li>对于服务器资源有要求,并发量越大, 资源消耗的越多</li><li>服务端渲染可能会发生偶发性错误, 需要有一套降级方案</li></ul>
<p>至于如何取舍, 看各位同学的项目需求,以及运用场景;</p>
<h3 data-id="heading-12"><span class="prefix"></span><span class="content">总结</span><span class="suffix"></span></h3>
<p>SSR的使用有利有弊, 我们应该结合自己的业务特性去制定合适的方案, 它的优点就是快, 有利于SEO, 缺点也很明显, 比较耗费服务器资源, 对于亿级流量的超巨app来说, 理论上是不太合适的, 集团内部也有自己的一套方案来优化客户端渲染, 使得用户体验尽量向SSR靠齐.每一种技术的运用只有实践了才知道利弊,才能产生碰撞. 本文只是简单的带大家了解一条业务线上对SSR的运用, 所阐述的方面也只是冰山一角, 希望给广大开发者带来一定的启发, 前人栽树, 后人乘凉, 感谢转转FE前辈们留下的宝贵财富.</p>
<h3 data-id="heading-13"><span class="prefix"></span><span class="content">最后</span><span class="suffix"></span></h3>
最后，感谢您的阅读，有任何问题，欢迎评论区留言讨论，互相学习~ 本月我们将推出更多实践相关文章及有奖留言活动，也欢迎扫描下方二维码关注我们的微信公众号及时获取
<img alt="图片名称" align="center" width="40%" class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/c219df58fbce4cb09a87c4e942e7e48d~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer">
<p>参考资料</p>
<p>nuxt官网:  https://www.baidu.com/link?url=xy0d8KPUgTmiVoGge6g-FgdeqjJSTjxdpT0tpxZzBG_&wd=&eqid=db50cacf00052e5e000000066081587d</p>
<p>Vue SSR指南: https://ssr.vuejs.org/zh/guide/</p>
<h1 data-id="heading-14"></h1>
</div> <div class="image-viewer-box" data-v-78c9b824><!----></div>  
</div>
            