
---
title: 'Sentry 安装到 React_Web 项目并支持 source-map_trace'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/bffd9b88c041459c8f9afe37bf6e00e1~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Tue, 24 Aug 2021 00:55:29 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/bffd9b88c041459c8f9afe37bf6e00e1~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><blockquote>
<ul>
<li>性能监控(trace)</li>
<li>错误定位(source-map)</li>
</ul>
</blockquote>
<h2 data-id="heading-0">1. 安装并配置命令行工具</h2>
<h3 data-id="heading-1">安装  sentry-cli</h3>
<pre><code class="hljs language-bash copyable" lang="bash"><span class="hljs-comment"># 安装 命令行工具</span>
$ npm install @sentry/cli
<span class="copy-code-btn">复制代码</span></code></pre>
<p>如果安装比较慢可以查看</p>
<h3 data-id="heading-2">新建配置文件  <code>.sentryclirc</code></h3>
<p>在工程根目录下新建 <code>.sentryclirc</code> 文件, sentry_cli 会默认读取文件，配置如下：</p>
<pre><code class="copyable">[defaults]
url=http://sentry.demo-domain.com
org='组织名'
project='项目名称'

[auth]
token=AccountApiToken
<span class="copy-code-btn">复制代码</span></code></pre>
<p>Token 的获取地址 <code>Account > API> Create New Token</code>
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/bffd9b88c041459c8f9afe37bf6e00e1~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer">
如果这里上传 source-map , 则需要 <code>project:releases</code>权限</p>
<h3 data-id="heading-3">获取项目Dsn</h3>
<p>dsn 是项目上报错误的地址, <strong>该 dsn（数据源）告诉 SDK 将事件发送到哪里。如果未提供此值，SDK 将尝试从 SENTRY_DSN 环境变量中读取它。如果该变量也不存在，则 SDK 将不会发送任何事件。请在 sentry.io 中查看“设置”->“项目”->“客户端密钥（DSN）”</strong>
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/8ef415758c7345859a0c20ba34cc71d8~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-4">2. 使用 Webpack 组件包配置</h2>
<h3 data-id="heading-5">2.1 Umi/React 示例</h3>
<h4 data-id="heading-6">1) 项目安装</h4>
<p>Sentry 通过在应用程序的运行时中使用 SDK 捕获数据。使用 yarn 或 npm 将 Sentry SDK 添加为依赖项</p>
<pre><code class="hljs language-bash copyable" lang="bash">$ npm install --save-dev @sentry/webpack-plugin
$ npm install --save @sentry/react
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-7">2) 项目对接 Dsn</h4>
<p>在项目的根 layout 文件中引入并初始化 Sentry React SDK 和 ErrorBoundary</p>
<pre><code class="hljs language-jsx copyable" lang="jsx"><span class="hljs-keyword">import</span> React <span class="hljs-keyword">from</span> <span class="hljs-string">'react'</span>;
<span class="hljs-keyword">import</span> * <span class="hljs-keyword">as</span> Sentry <span class="hljs-keyword">from</span> <span class="hljs-string">'@sentry/react'</span>;

<span class="hljs-comment">// 这里的版本号使用 env+version 方式, 更方便定位问题</span>
Sentry.init(&#123;
  <span class="hljs-attr">dsn</span>: <span class="hljs-string">'数据源'</span>,
  <span class="hljs-attr">release</span>: <span class="hljs-string">'版本号'</span>,
  <span class="hljs-attr">environment</span>: <span class="hljs-string">'环境，比如生产或者测试'</span>,
&#125;);

<span class="hljs-keyword">const</span> Base = <span class="hljs-function">(<span class="hljs-params">props:any</span>) =></span> &#123;
  <span class="hljs-keyword">const</span> children = props.children;
  <span class="hljs-keyword">return</span> <span class="xml"><span class="hljs-tag"><<span class="hljs-name">Sentry.ErrorBoundary</span> <span class="hljs-attr">fallback</span>=<span class="hljs-string">&#123;()</span> =></span> console.log("An error has occurred")&#125;>
      &#123;children&#125;
    <span class="hljs-tag"></<span class="hljs-name">Sentry.ErrorBoundary</span>></span></span>
&#125;;

<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> Base;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>注: ErrorBoundary 是定义遇到错误时应用程序行为的必要工具。该@sentry/react 软件包公开了一个 ErrorBoundary 组件，该组件自动将 JavaScript 错误从 React 组件树内部发送到 Sentry。像常规 React 组件一样使用 ErrorBoundary . 完成此操作后，Sentry 会自动捕获所有未处理的异常</p>
<p>可以通过在应用程序内的某个地方引发异常来触发开发环境中的第一个事件。例如，呈现一个按钮：</p>
<pre><code class="hljs language-jsx copyable" lang="jsx"><span class="hljs-keyword">return</span> <span class="xml"><span class="hljs-tag"><<span class="hljs-name">button</span> <span class="hljs-attr">onClick</span>=<span class="hljs-string">&#123;methodDoesNotExist&#125;</span>></span>Break the world<span class="hljs-tag"></<span class="hljs-name">button</span>></span></span>;
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-8">3) 部署  source-map</h4>
<p>构建项目时，我们会将代码进行压缩混淆，为了在进行日志分析的时候更清楚看到错误发生的原因，我们要对代码进行还原，因此需要 sourcemap 文件，使用 Sentry 的 Webpack 插件在项目构建时会自动上传 sourcemap 文件. 此操作需要身份认证, 这里会使用到之前配置的 sentry-cli 以及其 Token
​</p>
<p><strong>在 umirc.ts 配置文件中引入并使用</strong></p>
<p>配置文件中增加 SentryWebpackPlugin 和 devtool 配置项, devtool 值设置为"source-map".</p>
<blockquote>
<p>注意 : 这里的版本号使用的是 env + version 的方式, 更方便定位问题</p>
</blockquote>
<pre><code class="hljs language-javascript copyable" lang="javascript">&#123;
    <span class="hljs-attr">devtool</span>: <span class="hljs-string">"source-map"</span>,
    <span class="hljs-function"><span class="hljs-title">chainWebpack</span>(<span class="hljs-params">config : any, &#123; webpack &#125;: &#123; webpack: any &#125;</span>)</span> &#123;
        config.plugin(<span class="hljs-string">'sentry'</span>).use(SentryWebpackPlugin, [
            &#123;
                <span class="hljs-attr">include</span>: <span class="hljs-string">'./dist'</span>,
                <span class="hljs-attr">release</span>: <span class="hljs-string">`<span class="hljs-subst">$&#123;env&#125;</span>-<span class="hljs-subst">$&#123;version&#125;</span>`</span>,
                <span class="hljs-attr">ignore</span>: [<span class="hljs-string">'node_modules'</span>],
                <span class="hljs-attr">org</span>: <span class="hljs-string">'org'</span>,
                <span class="hljs-attr">sourceMapReference</span>: <span class="hljs-literal">true</span>,
            &#125;,
        ]);
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-9">2.2) Vite 安装</h3>
<h4 data-id="heading-10">1) 安装组件</h4>
<p>安装组件, 因为官方没有提供 对 vite 的对接, 所以使用三方插件</p>
<pre><code class="hljs language-bash copyable" lang="bash">$ yarn add vite-plugin-sentry
$ yarn add @sentry/vue
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-11">2) 项目对接 dsn</h4>
<p>在主项目入口引入并配置</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">import</span> * <span class="hljs-keyword">as</span> Sentry <span class="hljs-keyword">from</span> <span class="hljs-string">'@sentry/vue'</span>;
<span class="hljs-keyword">import</span> &#123; appMode, appVersion, sentryDsnUrl &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'@/utils/conf'</span>;

<span class="hljs-keyword">const</span> app = createApp(App)

Sentry.init(&#123;
    app,
    <span class="hljs-attr">dsn</span>: sentryDsnUrl,
    <span class="hljs-attr">release</span>: <span class="hljs-string">`<span class="hljs-subst">$&#123;appMode&#125;</span>-<span class="hljs-subst">$&#123;appVersion&#125;</span>`</span>,
    <span class="hljs-attr">environment</span>: appMode
&#125;);
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-12">3) 部署 source-map</h4>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">// vite.config.ts</span>
<span class="hljs-comment">// https://vitejs.dev/config/</span>
<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> defineConfig(<span class="hljs-function">(<span class="hljs-params">&#123; mode &#125;</span>) =></span> &#123;
    <span class="hljs-keyword">return</span> &#123;
        ...
        <span class="hljs-attr">plugins</span>: [
            ...
            <span class="hljs-comment">// 使用 NODE_ENV, production 时候才会执行错误搜集</span>
            viteSentry(&#123;
                <span class="hljs-attr">debug</span>: <span class="hljs-literal">true</span>,
                <span class="hljs-attr">url</span>: process.env.VITE_SENTRY_URL,
                <span class="hljs-attr">authToken</span>: process.env.VITE_SENTRY_TOKEN,
                <span class="hljs-attr">org</span>: <span class="hljs-string">'dadi'</span>,
                <span class="hljs-attr">project</span>: <span class="hljs-string">'proj'</span>,
                <span class="hljs-attr">release</span>: <span class="hljs-string">`<span class="hljs-subst">$&#123;mode&#125;</span>-<span class="hljs-subst">$&#123;pkgJson.version&#125;</span>`</span>,
                <span class="hljs-attr">deploy</span>: &#123;
                    <span class="hljs-attr">env</span>: <span class="hljs-string">`<span class="hljs-subst">$&#123;mode&#125;</span>`</span>
                &#125;,
                <span class="hljs-attr">setCommits</span>: &#123;
                    <span class="hljs-attr">auto</span>: <span class="hljs-literal">false</span>
                &#125;,
                <span class="hljs-attr">sourceMaps</span>: &#123;
                    <span class="hljs-attr">include</span>: [
                        <span class="hljs-string">`build/proj-<span class="hljs-subst">$&#123;mode&#125;</span>/assets`</span>
                    ],
                    <span class="hljs-attr">ignore</span>: [<span class="hljs-string">'node_modules'</span>],
                    <span class="hljs-attr">urlPrefix</span>: <span class="hljs-string">'~/assets'</span>
                &#125;
            &#125;)
        ],
        <span class="hljs-attr">build</span>: &#123;
            <span class="hljs-attr">outDir</span>: <span class="hljs-string">`build/proj-<span class="hljs-subst">$&#123;mode&#125;</span>`</span>,
            <span class="hljs-attr">sourcemap</span>: (mode === <span class="hljs-string">'prod'</span> || mode === <span class="hljs-string">'dev'</span>),
            ...
        &#125;,
        ...
    &#125;
&#125;);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这样在执行打包的时候即可进行 source-map的上传</p>
<pre><code class="hljs language-javascript copyable" lang="javascript">...
    ~<span class="hljs-regexp">/assets/u</span>seGoodsGames.d954199a.js (sourcemap at useGoodsGames.d954199a.js.map)
    ~<span class="hljs-regexp">/assets/u</span>seGoodsProperty.26f6354d.js (sourcemap at useGoodsProperty.26f6354d.js.map)
    ~<span class="hljs-regexp">/assets/</span>vant.31618c38.js (sourcemap at vant.31618c38.js.map)
    ~<span class="hljs-regexp">/assets/</span>vue3-clipboard-es.f4fdbc1a.js (sourcemap at vue3-clipboard-es.f4fdbc1a.js.map)
  Source Maps
    ~<span class="hljs-regexp">/assets/</span>Auto.f5325f0e.js.map
    ~<span class="hljs-regexp">/assets/</span>Buy.cca58b67.js.map
    ~<span class="hljs-regexp">/assets/</span>Chat.3d9466bf.js.map
...
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-13">3 Sentry 性能监控</h2>
<p>性能监控是搜集当前项目性能的一个组件工具,  可选安装, 这里简要介绍</p>
<h3 data-id="heading-14">3.1 安装跟踪软件包</h3>
<pre><code class="hljs language-bash copyable" lang="bash">$ yarn add @sentry/tracing
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-15">3.2 配置</h3>
<p>通过以下两种方式在应用中启用性能监控：</p>
<ul>
<li>tracesSampleRate 统一采样率,设置为 0 和之间的数字 1。（例如，20% 的 transactions 抽样率，设置 tracesSampleRate 为 0.2。）</li>
<li>tracesSampler 基于 transactions 本身及其捕获的上下文动态控制采样率(两者同时配置时,优先级高)</li>
</ul>
<h4 data-id="heading-16">1) 自动检测</h4>
<p>@sentry/tracing 提供了 BrowserTracing 集成,该 BrowserTracing 集成会为每个页面加载和导航事件生成一个新的事务(transactions)，并为每一个 XMLHttpRequest 或 fetch 创建一个 child span(子跨度)。
要启用此自动跟踪，需要在 SDK 配置选项中添加 BrowserTracing integrations 配置.</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">import</span> * <span class="hljs-keyword">as</span> Sentry <span class="hljs-keyword">from</span> <span class="hljs-string">"@sentry/browser"</span>;
<span class="hljs-keyword">import</span> &#123; Integrations &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">"@sentry/tracing"</span>; <span class="hljs-comment">// Must import second</span>
Sentry.init(&#123;
    app,
    <span class="hljs-attr">dsn</span>: sentryDsnUrl,
    <span class="hljs-attr">release</span>: <span class="hljs-string">`<span class="hljs-subst">$&#123;appMode&#125;</span>-<span class="hljs-subst">$&#123;appVersion&#125;</span>`</span>,
    <span class="hljs-attr">environment</span>: appMode,
    <span class="hljs-attr">integrations</span>: [
        <span class="hljs-keyword">new</span> Integrations.BrowserTracing(&#123;
            <span class="hljs-attr">routingInstrumentation</span>: Sentry.vueRouterInstrumentation(router),
            <span class="hljs-attr">tracingOrigins</span>: [<span class="hljs-string">'kejinshou.com'</span>, <span class="hljs-string">'dev.kejinshou.iliexiang.com'</span>, <span class="hljs-regexp">/^\//</span>]
        &#125;)
    ],
    <span class="hljs-comment">/**
     * 线上环境捕捉 1%, 开发环境捕捉完整
     * https://docs.sentry.io/platforms/javascript/guides/vue/configuration/sampling/#setting-a-sampling-function
     * <span class="hljs-doctag">@param <span class="hljs-variable">samplingContext</span></span>
     */</span>
    <span class="hljs-attr">tracesSampler</span>: <span class="hljs-function"><span class="hljs-params">samplingContext</span> =></span> &#123;
        <span class="hljs-keyword">if</span> (appMode === <span class="hljs-string">'prod'</span>) &#123;
            <span class="hljs-keyword">return</span> <span class="hljs-number">0.01</span>;
        &#125; <span class="hljs-keyword">else</span> &#123;
            <span class="hljs-keyword">return</span> <span class="hljs-number">1</span>;
        &#125;
    &#125;
&#125;);
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>配置选项</strong></p>
<ul>
<li>tracingOrigins</li>
</ul>
<p>tracingOrigins 默认值是['localhost', /^//]。
JavaScript SDK 将 sentry-trace 标头附加到所有输出 XHR / fetch 请求中，这些请求的目的地在列表中包含字符串或与列表中的正则表达式匹配。如果您的前端向其他域发出请求，则需要在其中添加它，
以将 sentry-trace 标头传播到后端服务，这是将事务链接在一起作为单个跟踪的一部分所必需的。该 tracingOrigins 选项与整个请求 URL 匹配，而不仅仅是域。使用更严格的正则表达式来匹配 URL 的某些部分，可以确保请求不必 sentry-trace 附加标头。
例如
前端应用程序 example.com
后端服务 api.example.com
前端应用程序对后端进行 API 调用
因此，该选项需要这样配置： new Integrations.BrowserTracing(&#123;tracingOrigins: ['api.example.com']&#125;)
现在发出的 XHR / fetch 请求 api.example.com 将 sentry-trace 附加标头
您将需要配置 Web 服务器 CORS 以允许 sentry-trace 标头。该配置看起来像"Access-Control-Allow-Headers: sentry-trace"，但是该配置取决于您的设置。如果您不允许 sentry-trace 标题，则该请求可能会被阻止。</p>
<ul>
<li>beforeNavigate</li>
</ul>
<p>对于 pageload 和 navigation 事务，BrowserTracing 集成使用浏览器的 window.locationAPI 生成事务名称。需要自定义名称可以提供一个 beforeNavigate 选项，使用此选项可以修改事务名称以使其更通用，例如，命名为 GET /users/12312012 的事务和 GET /users/11212012 都可以重命名 GET /users/:userid，以便它们可以组合在一起。</p>
<ul>
<li>shouldCreateSpanForRequest</li>
</ul>
<p>此功能可用于过滤掉不需要的跨度，例如 XHR 的运行状况检查或类似的检查。默认情况下，shouldCreateSpanForRequest 已经过滤掉了除 tracingOrigins 之外的所有.</p>
<h4 data-id="heading-17">2) 手动检测</h4>
<p>要手动检测代码的某些区域，可以创建事务来捕获它们。
这是适用于所有的 JavaScript 的 SDK（包括后端和前端）和独立工作的的 Express，Http 和 BrowserTracing 集成。</p>
<pre><code class="copyable">const transaction = Sentry.startTransaction(&#123; name: "test-transaction" &#125;);
const span = transaction.startChild(&#123; op: "functionX" &#125;); // This function returns a Span
// functionCallX
span.finish(); // Remember that only finished spans will be sent with the transaction
transaction.finish(); // Finishing the transaction will send it to Sentry
<span class="copy-code-btn">复制代码</span></code></pre>
<p>例如，如果要为页面上的用户交互创建事务，请执行以下操作：</p>
<pre><code class="copyable">// Let's say this function is invoked when a user clicks on the checkout button of your shop
shopCheckout() &#123;
  // This will create a new Transaction for you
  const transaction = Sentry.startTransaction('shopCheckout');
  // set the transaction on the scope so it picks up any errors
  hub.configureScope(scope => scope.setSpan(transaction));

  // Assume this function makes an xhr/fetch call
  const result = validateShoppingCartOnServer();

  const span = transaction.startChild(&#123;
    data: &#123;
      result
    &#125;,
    op: 'task',
    description: `processing shopping cart result`,
  &#125;);
  processAndValidateShoppingCart(result);
  span.finish();

  transaction.finish();
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>此示例将向 shopCheckoutSentry 发送事务。交易将包含一个 task 跨度，用于衡量 processAndValidateShoppingCart 花费了多长时间。最后，调用 transaction.finish()完成交易并将其发送给 Sentry。
在为异步操作创建跨度时，还可以利用 Promise。但是跨度必须在 transaction.finish()调用之前完成。</p>
<pre><code class="hljs language-bash copyable" lang="bash"><span class="hljs-keyword">function</span> processItem(item, transaction) &#123;
  const span = transaction.startChild(&#123;
    op: <span class="hljs-string">"http"</span>,
    description: `GET /items/:item-id`,
  &#125;);

  <span class="hljs-built_in">return</span> new Promise((resolve, reject) => &#123;
    http.get(`/items/<span class="hljs-variable">$&#123;item.id&#125;</span>`, response => &#123;
      response.on(<span class="hljs-string">"data"</span>, () => &#123;&#125;);
      response.on(<span class="hljs-string">"end"</span>, () => &#123;
        span.setTag(<span class="hljs-string">"http.status_code"</span>, response.statusCode);
        span.setData(<span class="hljs-string">"http.foobarsessionid"</span>, getFoobarSessionid(response));
        span.finish();
        resolve(response);
      &#125;);
    &#125;);
  &#125;);
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-18">4. QA</h2>
<h3 data-id="heading-19">1. 出现错误  (http status: 413)</h3>
<blockquote>
<p>error: API request failed
caused by: sentry reported an error: unknown error (http status: 413)</p>
</blockquote>
<p>上传的sourceMap太多，有可能会导致413 Request Entity Too Large错误, 这里需要更改后端对上传的大小限制即可, 如果是nginx, 需要在指定的配置段中增加</p>
<pre><code class="hljs language-nginx copyable" lang="nginx"><span class="hljs-attribute">client_max_body_size</span> <span class="hljs-number">20m</span>;
<span class="copy-code-btn">复制代码</span></code></pre>
<blockquote>
<p>参考来源:</p>
</blockquote>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fdocs.sentry.io%2Fplatforms%2Fjavascript%2Fguides%2Freact%2F%23monitor-performance" target="_blank" rel="nofollow noopener noreferrer" title="https://docs.sentry.io/platforms/javascript/guides/react/#monitor-performance" ref="nofollow noopener noreferrer">docs.sentry.io/platforms/j…</a>
<a href="https://link.juejin.cn/?target=https%3A%2F%2Fdocs.sentry.io%2Fplatforms%2Fjavascript%2Fguides%2Freact%2Fperformance%2Fcapturing%2Fautomatic%2F" target="_blank" rel="nofollow noopener noreferrer" title="https://docs.sentry.io/platforms/javascript/guides/react/performance/capturing/automatic/" ref="nofollow noopener noreferrer">docs.sentry.io/platforms/j…</a></p></div>  
</div>
            