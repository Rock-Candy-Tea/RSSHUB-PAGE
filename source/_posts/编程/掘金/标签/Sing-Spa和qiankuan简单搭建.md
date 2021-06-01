
---
title: 'Sing-Spa和qiankuan简单搭建'
categories: 
 - 编程
 - 掘金
 - 标签
headimg: 'https://picsum.photos/400/300?random=2300'
author: 掘金
comments: false
date: Mon, 31 May 2021 23:56:16 GMT
thumbnail: 'https://picsum.photos/400/300?random=2300'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h1 data-id="heading-0">微前端</h1>
<p>视频笔记：<a href="https://www.bilibili.com/video/BV1Dt4y1Q7KG?t=1821" target="_blank" rel="nofollow noopener noreferrer">www.bilibili.com/video/BV1Dt…</a>
参考链接： <a href="https://juejin.cn/post/6959447133766287374" target="_blank">juejin.cn/post/695944…</a></p>
<h2 data-id="heading-1">为什么要使用微前端</h2>
<ul>
<li>项目大打包慢</li>
<li>多人协作冲突</li>
<li>团队技术栈不同</li>
<li>每个团队可以独立开发、独立部署</li>
<li>项目中还需要老的应用代码，需要使用新的技术栈</li>
</ul>
<p>将一个应用划分成若干个子应用，将子应用打包成一个个的lib。当路径切换时加载不同的子应用。这样每个子应用都是独立的，技术栈也不用做限制。从而解决了前端协同开发问题。</p>
<h2 data-id="heading-2">应用通信</h2>
<ul>
<li>基于URL来进行数据传输，但是传输消息能力弱</li>
<li>基于CustomEvent实现通信</li>
<li>基于Props主子应用通信</li>
<li>使用权限变量、redux进行通信</li>
</ul>
<h2 data-id="heading-3">公共依赖</h2>
<ul>
<li>CDN - extends</li>
<li>webpack联邦模块</li>
</ul>
<h2 data-id="heading-4">为什么不是iframe？</h2>
<ul>
<li>如果不考虑体验问题，iframe几乎是最完美的微前端解决方案。</li>
<li>iframe最大的特性就是提供了浏览器原生的硬隔离方案，无论是样式隔离、JS隔离这些问题统统都能被完美解决。但他的最大问题也在于他的隔离性无法被突破，导致应用间上下文无法被共享，随之带来的开发体验、产品体验的问题。</li>
</ul>
<ol>
<li>
<p>url不同步，浏览器刷新iframe url状态丢失，后退前进按钮无法使用。</p>
</li>
<li></li>
</ol>
<h2 data-id="heading-5">single-SPA</h2>
<ul>
<li>问题：父子应用，平级应用样式、js冲突</li>
<li>实现了路由截止、路由加载</li>
<li>接入协议：子应用必须提供bootstrap、mount、unmount方法</li>
</ul>
<h3 data-id="heading-6">子应用</h3>
<ol>
<li>
<p>新建子应用</p>
<pre><code class="copyable">vue create child-vue

注意： 使用history路由
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
<li>
<p>安装single-spa-vue</p>
<pre><code class="copyable">npm install singe-spa-vue
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
<li>
<p>修改src目录下的main.js文件</p>
</li>
</ol>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">import</span> Vue <span class="hljs-keyword">from</span> <span class="hljs-string">'vue'</span>
<span class="hljs-keyword">import</span> App <span class="hljs-keyword">from</span> <span class="hljs-string">'./App.vue'</span>
<span class="hljs-keyword">import</span> router <span class="hljs-keyword">from</span> <span class="hljs-string">'./router'</span>
<span class="hljs-comment">//  1. 首先引入single-spa-vue</span>
<span class="hljs-keyword">import</span> singleSpaVue <span class="hljs-keyword">from</span> <span class="hljs-string">'single-spa-vue'</span>

Vue.config.productionTip = <span class="hljs-literal">false</span>

<span class="hljs-comment">// 2. 新建一个对象，而不是实例化Vue</span>
<span class="hljs-keyword">const</span> appOptions = &#123;
  <span class="hljs-attr">el</span>: <span class="hljs-string">'#vue'</span>, <span class="hljs-comment">//挂载父应用中的id为vue的标签中</span>
  router,
  <span class="hljs-attr">render</span>: <span class="hljs-function"><span class="hljs-params">h</span> =></span> h(App)
&#125;

<span class="hljs-comment">// 3. singleSpaVue包裹</span>
<span class="hljs-keyword">const</span> vueLifeCycle = singleSpaVue(&#123;
  Vue,
  appOptions
&#125;)

<span class="hljs-comment">// 5. 父应用引用我, 不加这个，默认跳转父应用的理由</span>
<span class="hljs-keyword">if</span>(<span class="hljs-built_in">window</span>.singleSpaNavigate)&#123;
  __webpack_public_path__ = <span class="hljs-string">'http://localhost:10002/'</span>
&#125;

<span class="hljs-comment">// 6. 子应用独立运行，当前不是作为子应用的情况</span>
<span class="hljs-keyword">if</span>(!<span class="hljs-built_in">window</span>.singleSpaNavigate)&#123;
  <span class="hljs-keyword">delete</span> appOptions.el
  <span class="hljs-keyword">new</span> Vue(appOptions).$mount(<span class="hljs-string">'#app'</span>)
&#125;

<span class="hljs-comment">//4. 协议接入，父应用会调用这些方法</span>
<span class="hljs-keyword">export</span> <span class="hljs-keyword">const</span> bootstrap = vueLifeCycle.bootstrap
<span class="hljs-keyword">export</span> <span class="hljs-keyword">const</span> mount = vueLifeCycle.mount
<span class="hljs-keyword">export</span> <span class="hljs-keyword">const</span> unmount = vueLifeCycle.unmount

<span class="copy-code-btn">复制代码</span></code></pre>
<ol start="4">
<li>
<p>将子应用打包成一个lib</p>
<p>首先需要在根目录下创建一个vue.config.js文件</p>
</li>
</ol>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-built_in">module</span>.exports = &#123;
    <span class="hljs-attr">configureWebpack</span>: &#123;
        <span class="hljs-attr">output</span>: &#123;
            <span class="hljs-attr">library</span>: <span class="hljs-string">'singleVue'</span>,
            <span class="hljs-attr">library</span>: <span class="hljs-string">'umd'</span> <span class="hljs-comment">// 最后将数学挂载到window上</span>
        &#125;,
        <span class="hljs-attr">devServer</span>: &#123;
            <span class="hljs-attr">port</span>: <span class="hljs-number">10000</span>
        &#125;
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-7">父应用</h3>
<ol>
<li>
<p>创建父应用</p>
<p>vue create parent-vue</p>
<p>注意：使用history路由</p>
</li>
<li>
<p>安装single-spa</p>
<p>npm install single-spa</p>
</li>
<li>
<p>修改src目录下的app.vue文件</p>
</li>
</ol>
<pre><code class="hljs language-js copyable" lang="js"><template>
  <span class="xml"><span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">id</span>=<span class="hljs-string">"app"</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">id</span>=<span class="hljs-string">"nav"</span>></span>
      <span class="hljs-tag"><<span class="hljs-name">router-link</span> <span class="hljs-attr">to</span>=<span class="hljs-string">"/vue"</span>></span>加载Vue应用<span class="hljs-tag"></<span class="hljs-name">router-link</span>></span> |
    <span class="hljs-tag"></<span class="hljs-name">div</span>></span>
    <span class="hljs-comment"><!--子应用挂载的位置--></span>
    <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">id</span>=<span class="hljs-string">"vue"</span>></span><span class="hljs-tag"></<span class="hljs-name">div</span>></span>
  <span class="hljs-tag"></<span class="hljs-name">div</span>></span></span>
</template>
<span class="copy-code-btn">复制代码</span></code></pre>
<ol start="4">
<li>修改src目录下的main.js文件</li>
</ol>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">import</span> Vue <span class="hljs-keyword">from</span> <span class="hljs-string">'vue'</span>
<span class="hljs-keyword">import</span> App <span class="hljs-keyword">from</span> <span class="hljs-string">'./App.vue'</span>
<span class="hljs-keyword">import</span> router <span class="hljs-keyword">from</span> <span class="hljs-string">'./router'</span>
<span class="hljs-comment">// 1. 引入注册子应用方法和启动方法</span>
<span class="hljs-keyword">import</span> &#123; registerApplication, start&#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'single-spa'</span>

Vue.config.productionTip = <span class="hljs-literal">false</span>


<span class="hljs-keyword">async</span> <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">loadScript</span>(<span class="hljs-params">url</span>)</span>&#123;
  <span class="hljs-keyword">return</span> <span class="hljs-keyword">new</span> <span class="hljs-built_in">Promise</span>(<span class="hljs-function">(<span class="hljs-params">resolve, reject</span>)=></span>&#123;
    <span class="hljs-keyword">let</span> script = <span class="hljs-built_in">document</span>.createElement(<span class="hljs-string">'script'</span>)
    script.src = url
    script.onload = resolve;
    script.onerror = reject;
    <span class="hljs-built_in">document</span>.head.appendChild(script)
  &#125;)
&#125;

<span class="hljs-comment">// 2.注册子应用</span>
registerApplication(<span class="hljs-string">'myVueApp'</span>,
  <span class="hljs-keyword">async</span> ()=>&#123;
      <span class="hljs-keyword">await</span> loadScript(<span class="hljs-string">'http://localhost:10002/js/chunk-vendors.js'</span>) 
      <span class="hljs-keyword">await</span> loadScript(<span class="hljs-string">'http://localhost:10002/js/app.js'</span>)
      <span class="hljs-keyword">return</span> <span class="hljs-built_in">window</span>.singleVue
  &#125;,
  <span class="hljs-function"><span class="hljs-params">location</span> =></span> location.pathname.startsWith(<span class="hljs-string">'/vue'</span>),
)

<span class="hljs-comment">// 3. 启动</span>
start();

<span class="hljs-keyword">new</span> Vue(&#123;
  router,
  <span class="hljs-attr">render</span>: <span class="hljs-function"><span class="hljs-params">h</span> =></span> h(App)
&#125;).$mount(<span class="hljs-string">'#app'</span>)

<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-8">single-spa的缺点</h3>
<ul>
<li>不能动态加载js</li>
<li>样式不隔离</li>
<li>全局变量没有js沙箱机制</li>
</ul>
<h4 data-id="heading-9">子应用之间的样式隔离</h4>
<h4 data-id="heading-10">主应用和子应用之间的样式隔离</h4>
<ul>
<li>约定项目前缀</li>
<li>css-modules 打包时生成不冲突的选择器名</li>
<li>Shadow DOM 样子dom 真正意义上的隔离（<a href="https://developer.mozilla.org/zh-CN/docs/Web/Web_Components/Using_shadow_DOM%EF%BC%89" target="_blank" rel="nofollow noopener noreferrer">developer.mozilla.org/zh-CN/docs/…</a></li>
<li>css-in-js</li>
</ul>
<h4 data-id="heading-11">JS的隔离</h4>
<p>A应用给window加属性window.a, B应用也可以访问window
单应用切换，沙箱 创建一个干净的环境，切换时可以删除属性和恢复属性</p>
<p>js沙箱</p>
<ol>
<li>快照沙箱  1年前拍一张，再拍一张，作对比，将区别保存起来
<a href="https://blog.csdn.net/qq_33226029/article/details/112511772" target="_blank" rel="nofollow noopener noreferrer">blog.csdn.net/qq_33226029…</a>
多个子应用不能使用这种方式</li>
<li>代理沙箱 es6 proxy</li>
</ol>
<ul>
<li>把不同的应用用不同的代理实现</li>
<li>qiankuan源码实现js隔离的方式</li>
</ul>
<h2 data-id="heading-12">qiankun</h2>
<p>官网：<a href="https://qiankun.umijs.org/zh/guide" target="_blank" rel="nofollow noopener noreferrer">qiankun.umijs.org/zh/guide</a></p>
<ul>
<li>技术栈无关，任意技术栈的应用均可使用/接入，不论是React/Vue/Angular/Jquery还是其他框架；</li>
<li>HTML Entry接入方式，让你接入微应用像使用iframe一样简单；</li>
<li>样式隔离， 确保微应用之间样式互相不干扰；</li>
<li>JS沙箱， 确保微应用之间[全局变量/事件]不冲突；</li>
<li>资源预加载， 在浏览器空闲时间预加载未打开的微应用资源，加速微应用打开速度；</li>
<li>umi插件， 提供了@umijs/plugin-qiankun供umi应用一键切换成微前端系统。</li>
</ul>
<h3 data-id="heading-13">项目实施</h3>
<h4 data-id="heading-14">新建基座qiankuan-base</h4>
<ol>
<li>安装qiankuan</li>
</ol>
<p>npm install qiankuan
2. 修改src目录下的main.js文件</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">import</span> Vue <span class="hljs-keyword">from</span> <span class="hljs-string">'vue'</span>
<span class="hljs-keyword">import</span> App <span class="hljs-keyword">from</span> <span class="hljs-string">'./App.vue'</span>
<span class="hljs-keyword">import</span> router <span class="hljs-keyword">from</span> <span class="hljs-string">'./router'</span>

<span class="hljs-keyword">import</span> ElementUI <span class="hljs-keyword">from</span> <span class="hljs-string">'element-ui'</span>
<span class="hljs-keyword">import</span> <span class="hljs-string">'element-ui/lib/theme-chalk/index.css'</span>

Vue.use(ElementUI)

Vue.config.productionTip = <span class="hljs-literal">false</span>
<span class="hljs-comment">// 1. 引入qiankun</span>
<span class="hljs-keyword">import</span> &#123;registerMicroApps, start&#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'qiankun'</span>
<span class="hljs-comment">// 2. 创建路由数组</span>
<span class="hljs-keyword">const</span> apps = [
&#123;
  <span class="hljs-attr">name</span> : <span class="hljs-string">'vueApp'</span>, <span class="hljs-comment">//应用的名字</span>
  <span class="hljs-attr">entry</span>: <span class="hljs-string">'http://localhost:20000'</span>, <span class="hljs-comment">//子应用支持跨域</span>
  <span class="hljs-attr">container</span>: <span class="hljs-string">'#vue'</span>, <span class="hljs-comment">//挂载容器</span>
  <span class="hljs-attr">activeRule</span>: <span class="hljs-string">'/vue'</span>, <span class="hljs-comment">//激活的路径</span>
  <span class="hljs-attr">props</span>: &#123;<span class="hljs-attr">a</span>: <span class="hljs-number">1</span>&#125;
&#125;,
&#123;
  <span class="hljs-attr">name</span> : <span class="hljs-string">'reactApp'</span>,
  <span class="hljs-attr">entry</span>: <span class="hljs-string">'http://localhost:30000'</span>, <span class="hljs-comment">//子应用支持跨域</span>
  <span class="hljs-attr">container</span>: <span class="hljs-string">'#react'</span>,
  <span class="hljs-attr">activeRule</span>: <span class="hljs-string">'/react'</span>,
 
&#125;
]
<span class="hljs-comment">// 3. 注册子应用路由</span>
registerMicroApps(apps) <span class="hljs-comment">//注册应用</span>
<span class="hljs-comment">// 4. 启动</span>
start(&#123;
<span class="hljs-attr">prefetch</span>: <span class="hljs-literal">false</span> <span class="hljs-comment">//取消预加载</span>
&#125;) <span class="hljs-comment">//启动</span>

<span class="hljs-keyword">new</span> Vue(&#123;
router,
<span class="hljs-attr">render</span>: <span class="hljs-function"><span class="hljs-params">h</span> =></span> h(App)
&#125;).$mount(<span class="hljs-string">'#app'</span>)

<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-15">新建子应用qiankuan-vue</h4>
<h4 data-id="heading-16">新建子应用qiankuan-react</h4>
<ol>
<li>安装react-app-rewired</li>
</ol>
<p>npm install react-app-rewired</p>
<ol start="2">
<li>修改根目录下的package.json文件</li>
</ol>
<pre><code class="hljs language-js copyable" lang="js"> <span class="hljs-string">"scripts"</span>: &#123;
    <span class="hljs-string">"start"</span>: <span class="hljs-string">"react-app-rewired start"</span>,
    <span class="hljs-string">"build"</span>: <span class="hljs-string">"react-app-rewired build"</span>,
    <span class="hljs-string">"test"</span>: <span class="hljs-string">"react-app-rewired test"</span>,
    <span class="hljs-string">"eject"</span>: <span class="hljs-string">"react-app-rewired eject"</span>
  &#125;,
<span class="copy-code-btn">复制代码</span></code></pre>
<ol start="3">
<li>在根目录新建config-overrides.js文件</li>
</ol>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-built_in">module</span>.exports = &#123;
    <span class="hljs-attr">webpack</span>: <span class="hljs-function">(<span class="hljs-params">config</span>) =></span> &#123;
        config.output.library = <span class="hljs-string">'reactApp'</span>;
        config.output.libraryTarget = <span class="hljs-string">'umd'</span>
        config.output.publicPath = <span class="hljs-string">"http://localhost:30000"</span>
        <span class="hljs-keyword">return</span> config
    &#125;,
    <span class="hljs-attr">devServer</span>: <span class="hljs-function">(<span class="hljs-params">configFunction</span>) =></span> &#123;
        <span class="hljs-keyword">return</span> <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">proxy, allowedHost</span>)</span>&#123;
            <span class="hljs-keyword">const</span> config = configFunction(proxy, allowedHost);
            config.headers = &#123;
                <span class="hljs-string">'Access-Control-Allow-Origin'</span>: <span class="hljs-string">'*'</span>
            &#125;
            <span class="hljs-keyword">return</span> config;
        &#125;
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<ol start="4">
<li>修改src目录下的index.js文件</li>
</ol>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">import</span> React <span class="hljs-keyword">from</span> <span class="hljs-string">'react'</span>;
<span class="hljs-keyword">import</span> ReactDOM <span class="hljs-keyword">from</span> <span class="hljs-string">'react-dom'</span>;
<span class="hljs-keyword">import</span> <span class="hljs-string">'./index.css'</span>;
<span class="hljs-keyword">import</span> App <span class="hljs-keyword">from</span> <span class="hljs-string">'./App'</span>;


<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">render</span>(<span class="hljs-params"></span>)</span>&#123;
  ReactDOM.render(
    <span class="xml"><span class="hljs-tag"><<span class="hljs-name">React.StrictMode</span>></span>
      <span class="hljs-tag"><<span class="hljs-name">App</span> /></span>
    <span class="hljs-tag"></<span class="hljs-name">React.StrictMode</span>></span></span>,
    <span class="hljs-built_in">document</span>.getElementById(<span class="hljs-string">'root'</span>)
  );
&#125;

<span class="hljs-keyword">if</span>(!<span class="hljs-built_in">window</span>.__POWERED_BY_QIANKUN__)&#123;
  render()
&#125;

<span class="hljs-keyword">export</span> <span class="hljs-keyword">async</span> <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">bootstrap</span>(<span class="hljs-params"></span>)</span>&#123;&#125;
<span class="hljs-keyword">export</span> <span class="hljs-keyword">async</span> <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">mount</span>(<span class="hljs-params"></span>)</span>&#123;
  render()
&#125;
<span class="hljs-keyword">export</span> <span class="hljs-keyword">async</span> <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">unmount</span>(<span class="hljs-params"></span>)</span>&#123;
  ReactDOM.unmountComponentAtNode(<span class="hljs-built_in">document</span>.getElementById(<span class="hljs-string">'root'</span>))
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<ol start="5">
<li>启动qiankun-react子应用</li>
</ol>
<p>npm run start</p>
<h3 data-id="heading-17">从零实现一个微前端框架</h3>
<h4 data-id="heading-18">初始化开发环境</h4>
<ol>
<li>新建一个文件夹my-single-spa</li>
<li>初始化： 执行命令npm init -y
会生成一个package.json文件</li>
</ol>
<pre><code class="hljs language-js copyable" lang="js">&#123;
  <span class="hljs-string">"name"</span>: <span class="hljs-string">"my-single-spa"</span>,
  <span class="hljs-string">"version"</span>: <span class="hljs-string">"1.0.0"</span>,
  <span class="hljs-string">"description"</span>: <span class="hljs-string">""</span>,
  <span class="hljs-string">"main"</span>: <span class="hljs-string">"index.js"</span>,
  <span class="hljs-string">"scripts"</span>: &#123;
    <span class="hljs-string">"test"</span>: <span class="hljs-string">"echo \"Error: no test specified\" && exit 1"</span>
  &#125;,
  <span class="hljs-string">"keywords"</span>: [],
  <span class="hljs-string">"author"</span>: <span class="hljs-string">""</span>,
  <span class="hljs-string">"license"</span>: <span class="hljs-string">"ISC"</span>
&#125;

<span class="copy-code-btn">复制代码</span></code></pre>
<ol start="3">
<li>安装打包工具rollup</li>
</ol>
<ul>
<li>npm install rollup</li>
<li>rollup相对于webpack的好处是：打包出来的代码比较简洁</li>
</ul>
<ol start="4">
<li>安装rollup-plugin-serve</li>
</ol>
<ul>
<li>npm install rollup-plugin-serve</li>
<li>该工具可以启动应用</li>
</ul>
<ol start="5">
<li>根目录下新建配置文件rollup.config.js</li>
</ol>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">import</span> serve <span class="hljs-keyword">from</span> <span class="hljs-string">'rollup-plugin-serve'</span>

<span class="hljs-comment">//rollup可以帮我们打包 es6模块化语法</span>
<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> &#123;
 <span class="hljs-attr">input</span> : <span class="hljs-string">'./src/single-spa.js'</span>, <span class="hljs-comment">//指定入口文件</span>
 <span class="hljs-attr">output</span>: &#123;
     <span class="hljs-attr">file</span>: <span class="hljs-string">'./lib/umd/single-spa.js'</span>, <span class="hljs-comment">//指定出口文件</span>
     <span class="hljs-attr">format</span>: <span class="hljs-string">'umd'</span>,  <span class="hljs-comment">//指定挂载到window</span>
     <span class="hljs-attr">name</span>: <span class="hljs-string">'singleSpa'</span>,
     <span class="hljs-attr">sourcemap</span>: <span class="hljs-literal">true</span>
 &#125;,
 <span class="hljs-attr">plugins</span>: [
    serve(&#123; <span class="hljs-comment">//服务</span>
        <span class="hljs-attr">openPage</span>: <span class="hljs-string">'/index.html'</span>, <span class="hljs-comment">//默认打开的页面</span>
        <span class="hljs-attr">contentBase</span>: <span class="hljs-string">''</span>,
        <span class="hljs-attr">port</span>: <span class="hljs-number">3000</span>
    &#125;)
 ]
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<ol start="6">
<li>根目录下新建入口文件夹src</li>
<li>根目录下新建index.html文件</li>
<li>修改根目录下的配置文件package.json</li>
</ol>
<pre><code class="hljs language-js copyable" lang="js"> <span class="hljs-string">"scripts"</span>: &#123;
    <span class="hljs-string">"dev"</span>: <span class="hljs-string">"rollup -c -w"</span>
  &#125;,
<span class="copy-code-btn">复制代码</span></code></pre>
<p>以上完成rollup环境的搭建</p>
<h4 data-id="heading-19">应用加载状态-生命周期</h4>
<pre><code class="hljs language-mermaid" lang="mermaid">stateDiagram-v2
[*] --> not_load
not_load --> loading_source_code
loading_source_code --> load_err
loading_source_code --> not_bootstrap
not_bootstrap --> bootstraping
bootstraping --> not_mount
not_mount --> mounting
mounting --> mounted
mounted --> updating
updating --> mounted
mounted --> [*]

</code></pre>
<h2 data-id="heading-20">技术原理</h2>
<h3 data-id="heading-21">样式隔离</h3>
<ol>
<li>qiankun为每个微应用的容器包裹上一个shadow dom节点，从而确保微应用的样式不会对全局造成影响。</li>
<li>qiankun还提供了一个实验性的样式隔离特性，qiankun会改写子应用所添加的样式，为所有样式规则添加一个特殊的选择器规则来限定其影响范围。</li>
</ol>
<h3 data-id="heading-22">JS沙箱</h3></div>  
</div>
            