
---
title: 'Vue3 + Vite2 项目实战复盘总结'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/450dcc225486460cb9e0a74740821db8~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Thu, 01 Jul 2021 03:58:15 GMT
thumbnail: 'https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/450dcc225486460cb9e0a74740821db8~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h3 data-id="heading-0">内容概要</h3>
<ul>
<li>背景</li>
<li>vue3 项目开发 get 到的知识</li>
<li>让我惊讶的 vite</li>
<li>项目中遇到的困难</li>
<li>总结</li>
<li>项目技术栈</li>
<li>资料推荐</li>
</ul>
<h2 data-id="heading-1">背景</h2>
<p>有一个新项目启动，移动端项目兼容安卓 6+，没有历史包袱，技术选型可以自由发挥。考虑到项目周期/团队技术/学习成本，最后选取还算比较新的 vue3。</p>
<p>不过等我的项目上线到写完这篇，有些东西已经不是最新的啦，<a href="https://mp.weixin.qq.com/s/1ycPAxnBq8b-hAHWwTgo1w" target="_blank" rel="nofollow noopener noreferrer">Vue 3.1.0 的 beta 版发布了</a>不得不感慨前端技术日新月异，变化的速度之快，我学不动了。</p>
<h2 data-id="heading-2">vue3 项目开发 get 到的知识</h2>
<p>刚开始用的时候，可怀念 vue2 了，我始终 get 不到 vue3 的精华，也理解不了网上说的组合式API 有多好。vue2 我是轻车熟路，vue3 我是面向文档开发。选择了用 vue3，就要去 get 他的精华，用着用着我发现真香，vue3 和 vite2 结合的项目惊讶到我了。</p>
<h4 data-id="heading-3">组合式 API 解决了什么问题？</h4>
<p>在开始写项目的时候，我一直没有 get 到组合 API 的有优点，还没有了全局的 this，我就有点不开心了，但是随着项目越来越复杂，页面越来越大的时候我就发现组合 API 真香。特别喜欢。</p>
<p>vue2 数据定义在 data，方法在 method，中间可能还有 watch，computed 等等别的东西，数据定义和方法处理逻辑之间差了十万八千里，当逻辑复杂达到一定长度的时候，追踪一个变量的变化是一件非常头痛的事情，鼠标需要来回滚动。</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/450dcc225486460cb9e0a74740821db8~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>有了组合 api，这个问题就解决了。所有相关的都可以写在一块。真好，它带来了一种全新的开发方式。如果你是 React 开发用户或者熟悉 React，那么 vue3 上手很快，你甚至都可以在页面中使用 hooks 的方式开发。由于这个项目使用场景比较小，所以在项目中并没有进行采用 hooks 的方式，后续有需要的时候可以考虑使用。了解更多关于组合式 API 请参考文档<a href="https://v3.cn.vuejs.org/guide/composition-api-introduction.html#%E4%BB%80%E4%B9%88%E6%98%AF%E7%BB%84%E5%90%88%E5%BC%8F-api" target="_blank" rel="nofollow noopener noreferrer">什么是组合式 API？</a></p>
<h4 data-id="heading-4">API的变化</h4>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/ca8d4e0f1573485b9c264bda51fa6072~tplv-k3u1fbpfcp-watermark.image" alt="nuxt api.png" loading="lazy" referrerpolicy="no-referrer">
由于在执行 setup 时，组件实例尚未被创建，因此在 setup 选项中没有 this。这意味着，除了 props 之外，你将无法访问组件中声明的任何属性——本地状态、计算属性或方法。setup 选项应该是一个接受 props 和 context 的函数。</p>
<p>因为 props 是响应式的，你不能使用 ES6 解构，因为它会消除 prop 的响应性。如果需要解构需要用 toRefs</p>
<p>执行 setup 时，组件实例尚未被创建。因此，你只能访问以下 property：</p>
<pre><code class="hljs language-plain copyable" lang="plain">props
attrs
slots
emit
<span class="copy-code-btn">复制代码</span></code></pre>
<p>换句话说，你将无法访问以下组件选项：</p>
<pre><code class="hljs language-plain copyable" lang="plain">data
computed
methods
<span class="copy-code-btn">复制代码</span></code></pre>
<p>整个项目下来与 vue2 只有语法的差别，思想啥的变化不大，不难。面向文档开发基本可以满足你的需求。</p>
<h4 data-id="heading-5">一个组件的思考</h4>
<p>如何写好一个组件，组件的规划/使用/维护，始终是一个值得深入思考的问题。Composition API 带了了一种全新的开发方式，甚至可以使用 hooks 的方式开发。每个模块各司其职，各自有自己的内部数据，公共的使用函数或者 hooks 抽象出来，整体上非常清爽，工程化越来越强，在项目中开发是否全部要使用 .vue 创建组件呢？</p>
<p>以前我觉得既然我选了 vue，就要用 .vue 的形式，但是在这次的项目开发过程中，我看到了我的小伙伴使用了原生 js 创建组件，我眼前一亮，在某些情况下用原生的 js 创建组件是一个非常不错的选择，那一刻我明白了，适合自己实际需求的才是最好的，混合式组件开发可以取长补短。</p>
<p>比如接口请求过程中，用户突然断网了，前端提示用户断网的页面，这代码就很简洁了。</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/32c3d5169dd44e359f5346334e2180c2~tplv-k3u1fbpfcp-watermark.image" alt="image-13.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>还有用 jsx 方式创建的组件，可定制化</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/6302bd5027f14093bb28077de8528dce~tplv-k3u1fbpfcp-watermark.image" alt="image (1).png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>适当的逻辑点分离: 埋点逻辑和业务逻辑分离更加有益于项目后期的维护（自定义指令实现声明式埋点）。</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/dbd0dad16bcc433bb4d10c455b2d66d1~tplv-k3u1fbpfcp-watermark.image" alt="image (2).png" loading="lazy" referrerpolicy="no-referrer"></p>
<h4 data-id="heading-6">路由逻辑的处理</h4>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/f1dce95e8f2a40938bcdf872f7249db9~tplv-k3u1fbpfcp-watermark.image" alt="640 (5).webp" loading="lazy" referrerpolicy="no-referrer">
视野中出现了焦点，也就出现了盲点。路由逻辑处理这块，我就坑到自己了，我焦点都在组合式API，在组合式 API 文档我找不到进入路由时候的生命周期函数。结果就导致我部分页面逻辑写在了 router.js 里面。</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">// 路由文件</span>
&#123;
  <span class="hljs-attr">path</span>: <span class="hljs-string">'/index'</span>,
  <span class="hljs-attr">component</span>: HOME,
  <span class="hljs-attr">beforeEnter</span>: <span class="hljs-function">(<span class="hljs-params">to, <span class="hljs-keyword">from</span></span>) =></span> &#123;
  <span class="hljs-comment">// 阅读页面回来的时候更新上次阅读记录,别的页面不做处理</span>
    <span class="hljs-keyword">if</span> (<span class="hljs-keyword">from</span>.path === <span class="hljs-string">"/read"</span>) &#123;
      to.meta = &#123;
        <span class="hljs-attr">updateHistory</span>: <span class="hljs-string">'read'</span>,
      &#125;
    &#125;
  &#125;
&#125;,
<span class="hljs-comment">// 页面文件</span>
watch(<span class="hljs-function">() =></span> route.meta,<span class="hljs-function">(<span class="hljs-params">val</span>) =></span> &#123;
  <span class="hljs-keyword">if</span> (val.updateHistory) &#123;
    <span class="hljs-comment">// 更新上次阅读的记录</span>
    getHistoryHandler()
  &#125;
&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这是一个非常非常不好的写法，页面逻辑和路由逻辑耦合在一起，后期维护带来了很大的问题，后来同事指点，纠正了这个问题。我竟然忽略了它原来的语法，去执着与他的新语法。</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/96a3551339e7498b8e8f6b463cd87105~tplv-k3u1fbpfcp-watermark.image" alt="640 (6).webp" loading="lazy" referrerpolicy="no-referrer"></p>
<p>所有页面需要统一的动态的一级路由前缀，即路由的一级域名不是由前端控制的，但是在实际开发中，前端路由规则是要关注一级路由的。按照一贯的逻辑是所有的路由配置动态路由即<code>path: '/:flag/index', path: '/:flag/listen'....</code>只要是有路由就需要在前面加上<code>/:flag</code>,某些情况下还需要处理在业务逻辑里面单独处理，这个逻辑混在比较多，不利于后期的维护。</p>
<p>想偷懒，思考有没有简单的解决方法，同事一番研究花了不少时间，不断试错不断研究，终于发现可在路由上面做文章，一句代码解决了大量重复的劳力。简直开心的不能再开心，分分钟搞定了<a href="https://next.router.vuejs.org/zh/api/#createwebhistory?fileGuid=t3GvJVRGxRkXgypy" target="_blank" rel="nofollow noopener noreferrer">createWebHistory 支持设置base文件目录</a></p>
<p><code>createWebHistory(location.pathname.split('/')[1])</code></p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/88907ebb92f8482a9583699279037d5d~tplv-k3u1fbpfcp-watermark.image" alt="image (3).png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>原来打包的时候还能动态的指定路由方式，真棒。</p>
<h2 data-id="heading-7">让我惊讶的 vite</h2>
<h4 data-id="heading-8">开发体验对比</h4>
<p>项目启动&&项目打包&&项目体积。</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/8b5ca095ba934d9caeb7c90976d98d15~tplv-k3u1fbpfcp-watermark.image" alt="640 (8).webp" loading="lazy" referrerpolicy="no-referrer"></p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/6cc920c0238d4bedb1415870b25d8be5~tplv-k3u1fbpfcp-watermark.image" alt="640 (9).webp" loading="lazy" referrerpolicy="no-referrer"></p>
<blockquote>
<p>ps：由于 vue-cli 和 vite 的环境变量读取方式和某一些 css 的引入方式不一样，在 vue-cli 里面我就注释了相关的代码。确保项目能够跑去来。除此之外别的几乎是一模一样</p>
</blockquote>
<p>通过数据对比可见：</p>
<p>vite 创建的项目，在项目启动和打包后的体积方面都远远胜过 vue-cli 创建的项目。</p>
<p>vue-cli 创建的项目，打包速度优于vite一点，但是在我们开发过程中，经常打包频率并不高，而且慢的也没有很夸张离谱。</p>
<p>就我个人而言，我更加倾向于 vite 去搭建项目。</p>
<h4 data-id="heading-9">vite 是如何吸引我的？</h4>
<p>1.无边界 => 纯 html 项目，react 项目都可以，项目中可以使用较新的语法，兼容性交给工具。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/21427005737a40ba9bac6ca95a97bf4c~tplv-k3u1fbpfcp-watermark.image" alt="640 (10).webp" loading="lazy" referrerpolicy="no-referrer"></p>
<ol start="2">
<li>紧跟时代的语法潮流支持。</li>
</ol>
<blockquote>
<p>module 形式引入js脚本 </p>
<blockquote>
<p>在js里面，可以通过这种形式引入css </p>
</blockquote>

<blockquote>
<p>支持css模块化写法
纯html项目也可以做到实时更新</p>
</blockquote>
</blockquote>
<p>让我们可以只需要关注业务开发，而无需去关注语法层面的兼容性以及打包配置，我喜欢这样的开发体验。</p>
<p><a href="https://github.com/sunseekers/vite/blob/main/index.html" target="_blank" rel="nofollow noopener noreferrer">vite demo 代码地址</a></p>
<h2 data-id="heading-10">项目遇到的困难</h2>
<p>困难总比办法多，再多的问题都会慢慢被解决，项目会如期上线。项目的开发，磕磕碰碰，才有成长，学到东西才有意义。</p>
<h4 data-id="heading-11">轮播组件</h4>
<p>应产品需求，轮播组件最终使用第三方插件，最初选用 vue-awesome-swiper ，但是 vue3 不支持，虽然官方有 vue3 的 demo，但是需要 vue2与 vue3 混用。</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/3a3c1a2390af45b5b2fd81ae5aa6d792~tplv-k3u1fbpfcp-watermark.image" alt="640 (11).webp" loading="lazy" referrerpolicy="no-referrer"></p>
<p>一番查找最后选用 swiper 插件，本身就支持了 vue3 ，而且他只支持 vue3，救了我</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/54f3764331594c2f92e7d53818a80b3d~tplv-k3u1fbpfcp-watermark.image" alt="640 (12).webp" loading="lazy" referrerpolicy="no-referrer"></p>
<p>就是文档写的不太好，很多并没有明确的暴露出来，需要去 swiper.js 文档查找， swiper 本身支持现在主流的框架这是一个很棒的体验，就是文档这一块需要加油</p>
<h4 data-id="heading-12">虚拟滚动</h4>
<p>页面列表加载上百千条数据时，白屏时间长，滚动有卡顿。最开始考虑采用前端页面分页，只要数据够多页面 dom 节点还是很多，达到一定量卡顿依旧存在。后来使用 vue-virtual-scroller 解决问题，但在网上看到大部分都是vue2版本的，vue3 版本都是在 issues 里面找到的</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/f8fb1436a17b420fb8504354fc1a9e73~tplv-k3u1fbpfcp-watermark.image" alt="640 (13).webp" loading="lazy" referrerpolicy="no-referrer"></p>
<p>在使用过程中又遇到，缺少某些方法导致无法满足产品需求，最后源码查找到满足需求的方法。vue3 本身的文档也不够完善，如果能够暴露更多的方法，而不是源码找，体验会更好</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/b2bd9509ff1f4c70ac30fa49c778b4a1~tplv-k3u1fbpfcp-watermark.image" alt="640 (14).webp" loading="lazy" referrerpolicy="no-referrer"></p>
<p>但是这个项目在 github 上面的 star 很不错，应该是靠谱的，只是人家还没来得及做吧，哈哈</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/501abdf5284445dfb79921434f711da4~tplv-k3u1fbpfcp-watermark.image" alt="640 (15).webp" loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-13">总结</h2>
<p>以上就我个人这次项目实战的经验而言，在用新的 API 的时候，需要思考一个问题，逻辑点聚合，同时也要注意转变代码组织思维。这不仅是 vue2 和 vue3 的区别，而是一直以来我们应该思考的一个问题，每次开发都应该思考，如何能让这个项目/组件能够长期稳定的发展。框架的更新于用户而言不仅仅是语法的更新，而应该去思考，框架在发展中遇到了什么问题？他是如何解决的？为了我们开发的项目长期稳定可持续的发展，是否可以借鉴他们的经验？</p>
<h2 data-id="heading-14">项目中使用到的技术栈及文档</h2>
<p><a href="https://cn.vitejs.dev/config/#mode" target="_blank" rel="nofollow noopener noreferrer">vite.config 的配置文档 </a></p>
<p><a href="https://next.router.vuejs.org/introduction.html" target="_blank" rel="nofollow noopener noreferrer">路由 router</a></p>
<p><a href="https://v3.cn.vuejs.org/guide/installation.html#%E5%91%BD%E4%BB%A4%E8%A1%8C%E5%B7%A5%E5%85%B7-cli" target="_blank" rel="nofollow noopener noreferrer">vue3</a></p>
<p><a href="https://swiperjs.com/vue" target="_blank" rel="nofollow noopener noreferrer">轮播插件swiper</a></p>
<p><a href="https://github.com/Akryum/vue-virtual-scroller/blob/next/packages/vue-virtual-scroller/README.md" target="_blank" rel="nofollow noopener noreferrer">虚拟滚动vue3 版本</a></p>
<h2 data-id="heading-15">vue3/vite资料推荐</h2>
<p><a href="https://juejin.cn/post/6960506633839443981#comment" target="_blank">昨晚尤大的连麦直播，我学到了很多！！！</a></p>
<p><a href="https://cn.vitejs.dev/guide/why.html" target="_blank" rel="nofollow noopener noreferrer">vite 文档</a></p>
<p><a href="https://juejin.cn/post/6910014283707318279" target="_blank">备战2021：vite工程化实践，建议收藏</a></p>
<p><a href="https://juejin.cn/post/6960110425438421006" target="_blank">手撸Vite，揭开Vite神秘面纱</a></p>
<p><a href="https://juejin.cn/post/6924912613750996999" target="_blank">备战2021：Vite2项目最佳实践</a></p>
<p><a href="https://juejin.cn/post/6937176680251424775" target="_blank">【译】下一代前端构建工具 ViteJS 中英双语字幕 ｜ 技术点评</a></p>
<p><a href="https://www.bilibili.com/video/BV1kh411Q7WN" target="_blank" rel="nofollow noopener noreferrer">【译】下一代前端工具 ViteJS 中英双语字幕 - Open Source Friday</a></p>
<p><a href="https://juejin.cn/post/6891885484524437518" target="_blank">忙了一夜用CompositionAPI征服产品妹子花里胡哨的需求</a></p>
<p><a href="https://juejin.cn/post/6894993303486332941" target="_blank">闪电五连鞭：Composition API原理深度剖析</a></p>
<p><a href="https://mp.weixin.qq.com/s/w4n_WhbDqK4kgzxEHUWWfw" target="_blank" rel="nofollow noopener noreferrer">不要再用Vue 2的思维写Vue 3了</a></p>
<p><a href="https://vue3js.cn/reactivity/reactive.spec.html" target="_blank" rel="nofollow noopener noreferrer">vue3 源码解析</a></p></div>  
</div>
            