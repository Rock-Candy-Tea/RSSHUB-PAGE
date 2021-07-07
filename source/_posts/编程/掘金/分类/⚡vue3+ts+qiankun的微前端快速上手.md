
---
title: '⚡vue3+ts+qiankun的微前端快速上手'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/e94f87c2252d4f15a10418e26666a3a1~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Mon, 05 Jul 2021 19:54:03 GMT
thumbnail: 'https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/e94f87c2252d4f15a10418e26666a3a1~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p><b>技术栈：vue3、typescript、qiankun(阿里的微前端框架)、vue-cli4</b></p>
<blockquote>
<p>PS： 一开始打算用<code>vite2</code>，但是调研后发现绝大多少微前端解决方案（包括<code>qiankun</code>）打包策略都是基于<code>webpack</code>的，vite2基本上除了官方文档，没有什么实战文章，更别说微前端的解决方案了（vite2这个工具不像<code>vue-cli4</code>，已经完全抛弃了webpack）。</p>
</blockquote>
<p>最近正在设计微前端项目，发现<a href="https://qiankun.umijs.org/zh/guide/tutorial#vue-%E5%BE%AE%E5%BA%94%E7%94%A8" target="_blank" rel="nofollow noopener noreferrer">qiankun</a>的官方文档只有vue2.x的写法，没有vue3.x的，刚好把踩完坑的demo分享出来</p>
<h2 data-id="heading-0">目录</h2>
<p>这里我会把主应用和微应用的目录贴出来，方便大家更直观清晰的理解后面的文件引入关系</p>
<p><em>PS： 我已经删掉了不涉及微前端功能的目录，看上去更简洁</em></p>
<h3 data-id="heading-1">主应用</h3>
<pre><code class="hljs language-json copyable" lang="json">parent
 ├── package.json
 └── src
     ├── App.vue
     ├── main.ts
     ├── modules
     │   ├── apps.ts
     │   └── index.ts
     ├── router
     │   └── index.ts
     └── views
         ├── About.vue
         └── Home.vue
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-2">微应用</h3>
<pre><code class="hljs language-json copyable" lang="json">children
 ├── package.json
 ├── vue.config.js
 └── src
     ├── App.vue
     ├── main.ts
     ├── public-path.ts
     ├── router
     │   └── index.ts
     └── views
         ├── About.vue
         └── Home.vue

<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-3">构建主应用</h2>
<h3 data-id="heading-4">安装<code>qiankun</code></h3>
<pre><code class="copyable">yarn add qiankun
或者
npm i qiankun -S
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-5">创建modules</h3>
<p>在src目录下新建modules目录，<code>modules目录</code>主要用于存放<code>qiankun</code>模块的相关代码</p>
<p>在modules目录下新建apps.ts文件</p>
<p>apps.ts文件用于统一存放微应用的信息</p>
<pre><code class="hljs language-typescript copyable" lang="typescript"><span class="hljs-comment">// src/modules/apps.ts</span>
<span class="hljs-keyword">const</span> apps: <span class="hljs-built_in">any</span>[] = [
  &#123;
    <span class="hljs-attr">name</span>: <span class="hljs-string">'children'</span>,
    <span class="hljs-attr">entry</span>: <span class="hljs-string">'//localhost:10001'</span>,
    <span class="hljs-attr">container</span>: <span class="hljs-string">'#frame'</span>,
    <span class="hljs-attr">activeRule</span>: <span class="hljs-string">'/children'</span>,
  &#125;,
];

<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> apps;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>在modules目录下新建index.ts</p>
<p>index.ts目录用于配置、注册主应用及微应用</p>
<pre><code class="hljs language-typescript copyable" lang="typescript"><span class="hljs-comment">// src/modules/index.ts</span>
<span class="hljs-keyword">import</span> &#123;
  registerMicroApps,
  addGlobalUncaughtErrorHandler,
  start,
&#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'qiankun'</span>;

<span class="hljs-comment">// 微应用的信息</span>
<span class="hljs-keyword">import</span> apps <span class="hljs-keyword">from</span> <span class="hljs-string">'./apps'</span>;

<span class="hljs-comment">/**
 * 注册微应用
 * 第一个参数 - 微应用的注册信息
 * 第二个参数 - 全局生命周期钩子
 */</span>
registerMicroApps(apps, &#123;
  <span class="hljs-comment">// qiankun 生命周期钩子 - 微应用加载前</span>
  <span class="hljs-attr">beforeLoad</span>: <span class="hljs-function">(<span class="hljs-params">app: <span class="hljs-built_in">any</span></span>) =></span> &#123;
    <span class="hljs-comment">// 加载微应用前，加载进度条</span>
    <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'before load'</span>, app.name);
    <span class="hljs-keyword">return</span> <span class="hljs-built_in">Promise</span>.resolve();
  &#125;,
  <span class="hljs-comment">// qiankun 生命周期钩子 - 微应用挂载后</span>
  <span class="hljs-attr">afterMount</span>: <span class="hljs-function">(<span class="hljs-params">app: <span class="hljs-built_in">any</span></span>) =></span> &#123;
    <span class="hljs-comment">// 加载微应用前，进度条加载完成</span>
    <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'after mount'</span>, app.name);
    <span class="hljs-keyword">return</span> <span class="hljs-built_in">Promise</span>.resolve();
  &#125;,
&#125;);

<span class="hljs-comment">/**
 * 添加全局的未捕获异常处理器
 */</span>
addGlobalUncaughtErrorHandler(<span class="hljs-function">(<span class="hljs-params">event: Event | <span class="hljs-built_in">string</span></span>) =></span> &#123;
  <span class="hljs-built_in">console</span>.error(event);
&#125;);

<span class="hljs-comment">// 导出 qiankun 的启动函数</span>
<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> start;

<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-6">改动main.ts</h3>
<p>将modules中的index.ts引入到main.ts中，并执行start</p>
<pre><code class="hljs language-typescript copyable" lang="typescript"><span class="hljs-keyword">import</span> &#123; createApp &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'vue'</span>;
<span class="hljs-keyword">import</span> App <span class="hljs-keyword">from</span> <span class="hljs-string">'./App.vue'</span>;
<span class="hljs-keyword">import</span> router <span class="hljs-keyword">from</span> <span class="hljs-string">'./router'</span>;
<span class="hljs-keyword">import</span> store <span class="hljs-keyword">from</span> <span class="hljs-string">'./store'</span>;
<span class="hljs-keyword">import</span> start <span class="hljs-keyword">from</span> <span class="hljs-string">'./modules'</span>;

<span class="hljs-keyword">const</span> app = createApp(App);

start();

app
  .use(store)
  .use(router)
  .mount(<span class="hljs-string">'#app'</span>);

<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-7">App.vue</h3>
<p>注意，<code>modules/apps</code>中的此处的微应用信息中，有个字段是<code>container</code>，是用于设定微应用挂载节点的，要注意与下方<code><div id="frame"></div></code>中的id保持一致（当然，你也可以根据自己需求自己写）</p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">template</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">id</span>=<span class="hljs-string">"app"</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">router-view</span>></span>
      <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">id</span>=<span class="hljs-string">"frame"</span>></span><span class="hljs-tag"></<span class="hljs-name">div</span>></span>
    <span class="hljs-tag"></<span class="hljs-name">router-view</span>></span>
  <span class="hljs-tag"></<span class="hljs-name">div</span>></span>
<span class="hljs-tag"></<span class="hljs-name">template</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>至此，主应用的项目代码已经修改完毕。</p>
<h2 data-id="heading-8">构建微应用</h2>
<h3 data-id="heading-9">新增public-path.ts</h3>
<p>在 <code>src</code> 目录下新增 <code>public-path.ts</code>：</p>
<pre><code class="hljs language-typescript copyable" lang="typescript"><span class="hljs-comment">// src/public-path.ts</span>
<span class="hljs-keyword">if</span> ((<span class="hljs-built_in">window</span> <span class="hljs-keyword">as</span> <span class="hljs-built_in">any</span>).__POWERED_BY_QIANKUN__) &#123;
  __webpack_public_path__ = (<span class="hljs-built_in">window</span> <span class="hljs-keyword">as</span> <span class="hljs-built_in">any</span>).__INJECTED_PUBLIC_PATH_BY_QIANKUN__;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-10">改写main.ts</h3>
<blockquote>
<p>本次主应用、微应用用的vue-router皆为4.0版本，与之前的3.x存在一定的差异</p>
</blockquote>
<blockquote>
<p>因qiankun是根据路由进行匹配微应用的，因此最好给微应用的路由配置加上<code>base: /微应用名称/</code>，而在<code>vue-router@4</code>中的写法则为<code>createWebHistory('/微应用名称/')</code>,</p>
</blockquote>
<pre><code class="hljs language-typescript copyable" lang="typescript"><span class="hljs-keyword">import</span> &#123; createApp &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'vue'</span>
<span class="hljs-keyword">import</span> &#123; createRouter, createWebHistory &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'vue-router'</span>
<span class="hljs-keyword">import</span> App <span class="hljs-keyword">from</span> <span class="hljs-string">'./App.vue'</span>
<span class="hljs-keyword">import</span> &#123; routes &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'./router'</span>
<span class="hljs-keyword">import</span> store <span class="hljs-keyword">from</span> <span class="hljs-string">'./store'</span>
<span class="hljs-keyword">import</span> <span class="hljs-string">'./public-path'</span>;
<span class="hljs-keyword">const</span> APP_NAME = <span class="hljs-built_in">require</span>(<span class="hljs-string">'../package.json'</span>).name;

<span class="hljs-keyword">const</span> app = createApp(App);

<span class="hljs-keyword">let</span> router = <span class="hljs-literal">null</span>;
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">render</span>(<span class="hljs-params">props: <span class="hljs-built_in">any</span></span>) </span>&#123;
  <span class="hljs-keyword">const</span> &#123; container &#125; = props;
  router = createRouter(&#123;
    <span class="hljs-attr">history</span>: createWebHistory(<span class="hljs-string">`/<span class="hljs-subst">$&#123;APP_NAME&#125;</span>/`</span>),
    routes
  &#125;)

  app.use(store)
  .use(router)
  .mount(container ? container.querySelector(<span class="hljs-string">'#app'</span>) : <span class="hljs-string">'#app'</span>)
&#125;

<span class="hljs-comment">// 独立运行时</span>
<span class="hljs-keyword">if</span> (!(<span class="hljs-built_in">window</span> <span class="hljs-keyword">as</span> <span class="hljs-built_in">any</span>).__POWERED_BY_QIANKUN__) &#123;
  render(&#123;&#125;);
&#125;


<span class="hljs-comment">/**
 * bootstrap ： 在微应用初始化的时候调用一次，之后的生命周期里不再调用
 */</span>
<span class="hljs-keyword">export</span> <span class="hljs-keyword">async</span> <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">bootstrap</span>(<span class="hljs-params"></span>) </span>&#123;
  <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'bootstrap'</span>);
&#125;

<span class="hljs-comment">/**
 * mount ： 在应用每次进入时调用 
 */</span>
<span class="hljs-keyword">export</span> <span class="hljs-keyword">async</span> <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">mount</span>(<span class="hljs-params">props: <span class="hljs-built_in">any</span></span>) </span>&#123;
  <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'mount'</span>, props);
  render(props);
&#125;

<span class="hljs-comment">/**
 * unmount ：应用每次 切出/卸载 均会调用
 */</span>
<span class="hljs-keyword">export</span> <span class="hljs-keyword">async</span> <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">unmount</span>(<span class="hljs-params"></span>) </span>&#123;
  <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'unmount'</span>);
  app.unmount();
&#125;

<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-11">vue.config.js</h3>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> APP_NAME = <span class="hljs-built_in">require</span>(<span class="hljs-string">'./package.json'</span>).name;
<span class="hljs-keyword">const</span> path = <span class="hljs-built_in">require</span>(<span class="hljs-string">"path"</span>);

<span class="hljs-built_in">module</span>.exports = &#123;
  <span class="hljs-attr">devServer</span>: &#123;
    <span class="hljs-comment">// 监听端口</span>
    <span class="hljs-attr">port</span>: <span class="hljs-number">10001</span>,
    <span class="hljs-comment">// 关闭主机检查，使微应用可以被 fetch</span>
    <span class="hljs-attr">disableHostCheck</span>: <span class="hljs-literal">true</span>,
    <span class="hljs-comment">// 配置跨域请求头，解决开发环境的跨域问题</span>
    <span class="hljs-attr">headers</span>: &#123;
      <span class="hljs-string">"Access-Control-Allow-Origin"</span>: <span class="hljs-string">"*"</span>,
    &#125;,
  &#125;,
  <span class="hljs-attr">configureWebpack</span>: &#123;
    <span class="hljs-attr">resolve</span>: &#123;
      <span class="hljs-attr">alias</span>: &#123;
        <span class="hljs-string">"@"</span>: path.resolve(__dirname, <span class="hljs-string">"src"</span>),
      &#125;,
    &#125;,
    <span class="hljs-attr">output</span>: &#123;
      <span class="hljs-comment">// 微应用的包名，这里与主应用中注册的微应用名称一致</span>
      <span class="hljs-attr">library</span>: APP_NAME,
      <span class="hljs-comment">// 将你的 library 暴露为所有的模块定义下都可运行的方式</span>
      <span class="hljs-attr">libraryTarget</span>: <span class="hljs-string">"umd"</span>,
      <span class="hljs-comment">// 按需加载相关，设置为 webpackJsonp_微应用名称 即可</span>
      <span class="hljs-attr">jsonpFunction</span>: <span class="hljs-string">`webpackJsonp_<span class="hljs-subst">$&#123;APP_NAME&#125;</span>`</span>,
    &#125;,
  &#125;,
&#125;;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>至此微应用的代码部分也改造完成</p>
<h2 data-id="heading-12">运行</h2>
<p>在主应用、微应用的目录下，均运行<code>yarn serve</code> 启动项目</p>
<p>此时打开主应用的地址 <code>localhost:8080</code></p>
<p>在看到能正常显示后，将地址改为<code>localhost:8080/child</code>即可看到微应用被加载进来</p>
<h2 data-id="heading-13">结尾</h2>
<p>这次分享的内容仅仅是在vue3的版本下如何快速上手qiankun框架， 更细致或更深入的内容建议查阅文档。
如果关于这篇分享有什么疑问的话，可以在下面的评论区告诉我哦，我会尽量解答的（大概吧🙈）</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/e94f87c2252d4f15a10418e26666a3a1~tplv-k3u1fbpfcp-watermark.image" alt="QQ图片20210421150857.jpg" loading="lazy" referrerpolicy="no-referrer"></p></div>  
</div>
            