
---
title: '迄今为止最好的Webview远程调试神器：devtools-pro'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/5daf535405cd4bfebc26a711ecc3b611~tplv-k3u1fbpfcp-zoom-1.image'
author: 掘金
comments: false
date: Sat, 15 May 2021 03:09:21 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/5daf535405cd4bfebc26a711ecc3b611~tplv-k3u1fbpfcp-zoom-1.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h1 align="center" data-id="heading-0">Devtools-Pro</h1>
<div align="center">
A web remote debugging tools, based on Chrome DevTools.
</div>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/5daf535405cd4bfebc26a711ecc3b611~tplv-k3u1fbpfcp-zoom-1.image" alt="image" loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-1">🎉 Features</h2>
<ul>
<li>基于 Chrome DevTools</li>
<li>基于 WebSocket 远程调试</li>
<li>可扩展，支持自定义插件</li>
</ul>
<h2 data-id="heading-2">📦 Installation</h2>
<pre><code class="hljs language-shell copyable" lang="shell">npm i -g devtools-pro
<span class="hljs-meta">#</span><span class="bash"> OR</span>
yarn global add devtools-pro
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-3">命令行配置项</h2>
<pre><code class="hljs language-bash copyable" lang="bash">devtools-pro -h
<span class="hljs-comment"># or</span>
dp -h
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="copyable">Options:
  -h, --help      Show help                                            [boolean]
      --plugins   Add plugins                                            [array]
      --config    Provide path to a devtools configuration file e.g.
                  ./devtools.config.js     [string] [default: "devtools.config"]
  -o, --open      Open browser when server start       [boolean] [default: true]
      --https     Use HTTPS protocol.                                  [boolean]
  -p, --port      Port to use [8899]                                    [number]
      --verbose   Displays verbose logging            [boolean] [default: false]
      --hostname  Address to use [0.0.0.0]                              [string]
  -v, --version   Show version number                                  [boolean]
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-4">配置文件<code>devtools.config.js</code></h2>
<p>为了方便项目统一配置，DevTools-pro 支持配置文件，可以在项目中创建一个名为<code>devtools.config.js</code>的文件，支持的配置项如下：</p>
<ul>
<li>logLevel：日志级别，支持<code>silent</code> <code>verbose</code></li>
<li>port：server 端口号，默认 <code>8899</code></li>
<li>hostname：默认 <code>0.0.0.0</code></li>
<li>plugins：配置插件，<a href="https://juejin.cn/post/6962472321948844040#%E6%8F%92%E4%BB%B6%E5%BC%80%E5%8F%91">下面介绍</a></li>
<li>https：server 默认是 http 的，如果要启用 https，可以设置<code>https=true</code>，或者使用此字段配置<a href="https://nodejs.org/api/https.html" target="_blank" rel="nofollow noopener noreferrer">nodejs/https 模块</a>相关配置，例如：</li>
</ul>
<pre><code class="hljs language-js copyable" lang="js">https:&#123;
    <span class="hljs-attr">key</span>: fs.readFileSync(<span class="hljs-string">'/path/to/server.key'</span>),
    <span class="hljs-attr">cert</span>: fs.readFileSync(<span class="hljs-string">'/path/to/server.crt'</span>),
    <span class="hljs-attr">ca</span>: fs.readFileSync(<span class="hljs-string">'/path/to/ca.pem'</span>),
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-5">开发</h2>
<ol>
<li>clone</li>
</ol>
<pre><code class="hljs language-bash copyable" lang="bash">mkdir devtools-pro
git <span class="hljs-built_in">clone</span> git@github.com:ksky521/devtools-pro.git devtools-pro
<span class="copy-code-btn">复制代码</span></code></pre>
<ol start="2">
<li>安装依赖 & 初始化</li>
</ol>
<pre><code class="hljs language-bash copyable" lang="bash">yarn
<span class="hljs-comment"># 初始化：将chrome-devtools-frontend/front_end复制出来</span>
sh init.sh
<span class="copy-code-btn">复制代码</span></code></pre>
<ol start="3">
<li>开始开发</li>
</ol>
<pre><code class="hljs language-bash copyable" lang="bash">yarn dev
<span class="copy-code-btn">复制代码</span></code></pre>
<p>访问：</p>
<ul>
<li>home：localhost:8080/home.html</li>
<li>调试页面 demo：localhost:8080/demo.html</li>
<li>inspector：localhost:8989/inspector.html</li>
<li>backend.js: localhost:8080/backend.js</li>
</ul>
<h2 data-id="heading-6">原理</h2>
<p>DevTools-pro 是基于<a href="https://github.com/ChromeDevTools/devtools-frontend" target="_blank" rel="nofollow noopener noreferrer">chrome-devtools-frontend</a>进行开发的，通过自建 WebSocket 通道实现 Frontend 和 Backend 的通信。</p>
<p>DevTools 主要由四部分组成：</p>
<ul>
<li>Frontend：调试器前端，默认由 Chromium 内核层集成，DevTools Frontend 是一个 Web 应用程序；</li>
<li>Backend：调试器后端，Chromium、V8 或 Node.js；在这里我们主要是引入的 backend.js</li>
<li>Protocol：调试协议，调试器前端和后端使用此协议通信。 它分为代表被检查实体的语义方面的域。 每个域定义类型、命令（从前端发送到后端的消息）和事件（从后端发送到前端的消息）。该协议基于 json rpc 2.0 运行；</li>
<li>Message Channels：消息通道，消息通道是在后端和前端之间发送协议消息的一种方式。包括：Embedder Channel、WebSocket Channel、Chrome Extensions Channel、USB/ADB Channel。</li>
</ul>
<p>这四部分的交互逻辑如下图所示：</p>
<p><img src="https://juejin.cn/post/docs/imgs/devtools-flow.png" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>简单来说：被调试页面引入 Backend 后，会跟 Frontend 建立连接；在 backend 中，对于一些 JavaScript API 或者 DOM 操作等进行了监听和 mock，从而页面执行对应操作时，会发送消息到 Frontend。同时 Backend 也会监听来自于 Frontend 的消息，收到消息后进行对应处理。</p>
<h2 data-id="heading-7">插件开发</h2>
<p>DevTools-pro 是可以通过插件增加功能的，比如：</p>
<ul>
<li>增加 devtools 面板，例如集成 san-devtools、vue-devtools、react-devtools 等到 devtools-pro 中</li>
<li>主动在页面触发 <a href="https://chromedevtools.github.io/devtools-protocol/" target="_blank" rel="nofollow noopener noreferrer">Chrome DevTools Protocol（CDP）</a>，接收/发送数据，例如将一些特殊的请求或者信息通过 CDP 发送到 devtools frontend 中展示</li>
<li>其他脑洞大开的想法</li>
</ul>
<p>插件可以发布一个 NPM 包，然后在项目下的<code>devtools.config.js</code>中通过<code>plugins</code>进行添加，一个 plugins 是一个 NPM 包，由以下三部分组成：</p>
<ul>
<li>frontend：调试器前端，即 Chrome DevTools 的 module，按照 Chrome-Devtools-Frontend 写法进行定义，也可以使用 iframe 进行嵌入</li>
<li>backend：调试器后端，即被调试页面的引入的 js 实现</li>
<li>middleware：即 Koa 的中间件，用于增强 server 实现</li>
</ul>
<p>这三部分根据自己插件的实际功能进行开发，并非都包含。三部分的定义是在 NPM 包的<code>package.json</code>中<code>devtools</code>字段，类似：</p>
<pre><code class="hljs language-json5 copyable" lang="json5">&#123;
    name: 'js-native-monitor',
    version: '1.0.0',
    main: 'index.js',
    // ....
    devtools: &#123;
        // middleware
        frontend: &#123;
            name: 'jsna_monitor',
            type: '', // remote/autostart
            dir: 'frontend'
        &#125;,
        // backend字段，该文件内容会被merge到backend.js中
        backend: 'index.js',
        // middleware
        middleware: 'middleware.js'
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-8">Frontend</h3>
<p>Frontend 是完全符合的<a href="https://github.com/ChromeDevTools/devtools-frontend/tree/master/front_end/panels" target="_blank" rel="nofollow noopener noreferrer">chrome-devtools-frontend</a>的模块，<code>package.json</code>中的<code>devtools.frontend</code>包含配置有：</p>
<ul>
<li>name：名字，访问<code>hostname:port/devtools/$&#123;name&#125;/**</code> 则自动转发到这里，优先级高于内置和 chrome-devtools-frontend/front_end 文件，<strong>如果 name 是 chrome-devtools-frontend/front_end 已经存在的则优先级高于 chrome-devtools-frontend</strong>；</li>
<li>type：可选值：<code>autostart</code>和<code>remote</code>，含义参考 Chrome DevTools 具体实现；</li>
<li>dir：指定文件夹目录</li>
</ul>
<p>dir 文件夹中的重要文件是模块描述文件<code>module.json</code>，通过文件夹下的 <code>module.json</code> 配置文件进行定义，配置文件有以下几个属性：</p>
<ul>
<li><code>scripts</code>：模块中包含的 JavaScript 文件数组，这里的路径名称是相对于 module.json 的位置；</li>
<li><code>skip_compilation</code>：类似于脚本，但是 Closure Compiler 不会对这些文件进行类型检查；</li>
<li><code>resources</code>：模块使用的非 JavaScript 文件数组；</li>
<li><code>dependencies</code>：模块使用的其他模块的数组；</li>
<li><code>extensions</code>：具有 type 属性的对象数组。 扩展可以通过运行时系统查询，并可以通过任何模块中的代码进行访问。类型包括 "setting"、"view"，"context-menu-item"。例如可以按如下方式注册出现在设置屏幕中的设置：</li>
</ul>
<pre><code class="hljs language-json5 copyable" lang="json5">&#123;
  "extensions": [
    &#123;
      "type": "setting",
      "settingName": "interdimensionalWarpEnabled",
      "settingType": "boolean",
      "defaultValue": false,
      "storageType": "session",
      "title": "Show web pages from other dimensions"
    &#125;,
    ...
  ]
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>DevTools Frontend 通过 Module 和 Extension 机制为 Application 增加了“插件化”的能力，然后通过配置进行灵活的组装。</p>
<h4 data-id="heading-9">应用举例</h4>
<p>我们应用做多的可能是添加一个面板，例如我要添加一个<code>js-native</code>的面板，则<code>module.json</code>内容如下：</p>
<pre><code class="hljs language-json5 copyable" lang="json5">&#123;
    extensions: [
        &#123;
            // 类型
            type: 'view',
            // 位置
            location: 'panel',
            id: 'jsna_monitor',
            // 面板显示文字
            title: 'jsNative monitor',
            order: 110,
            // 启动className
            className: 'JSNAMonitor.JSNAMonitor'
        &#125;
    ],
    // 依赖
    dependencies: ['platform', 'ui', 'host', 'components', 'data_grid', 'source_frame', 'sdk'],
    scripts: [],
    // 资源
    modules: ['jsna_monitor.js', 'jsna_monitor-legacy.js', 'JSNAMonitor.js'],
    resources: ['jsna.css']
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>此部分可以参考<a href="https://github.com/ksky521/js-native-monitor" target="_blank" rel="nofollow noopener noreferrer">@ksky521/js-native-monitor</a>实现。</p>
<h3 data-id="heading-10">Backend</h3>
<p>当被调试的页面引入<code>hostname:port/backend.js</code>时，backend 的文件会被合并到<code>backend.js</code>中输出。这里提供了全局命名空间<code>$devtools</code>，它的定义在<a href="https://juejin.cn/post/src/runtime.js">./src/runtime.js</a>中。后面<a href="https://juejin.cn/post/6962472321948844040#%E9%80%9A%E4%BF%A1">通信</a>部分会详细介绍</p>
<h3 data-id="heading-11">通信</h3>
<p>在原来的 CDP 基础上，为了方便开发插件开发，DevTools-pro 提供了两种 Backend 和 Frontend 插件的通信方式：<strong>CDP 事件</strong>和<strong>自建 WebSocket</strong>。</p>
<h4 data-id="heading-12">CDP 事件</h4>
<p>在 Backend 中，提供了一个全局命名空间<code>$devtools</code>，可以通过下面方法进行事件注册。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// backend中代码</span>
$devtools.registerEvent(<span class="hljs-string">'PluginName.method'</span>, <span class="hljs-function"><span class="hljs-params">data</span> =></span> &#123;
    <span class="hljs-keyword">const</span> result = <span class="hljs-string">'处理完的返回数据'</span>;
    <span class="hljs-built_in">console</span>.log(data);
    <span class="hljs-comment">//...</span>
    <span class="hljs-keyword">return</span> result;
&#125;);
<span class="hljs-comment">// frontend插件中，发送命令给backend</span>
runtime.bridge.sendCommand(<span class="hljs-string">'PluginName.method'</span>, &#123;&#125;).then(<span class="hljs-function"><span class="hljs-params">a</span> =></span> <span class="hljs-built_in">console</span>.log(<span class="hljs-number">111</span>, a));
<span class="hljs-comment">// 输出：111，处理完的返回数据</span>
<span class="hljs-comment">// -> frontend发送数据之后，会得到一个Promise，得到的数据是backend的事件处理函数直接返回的数据。</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>注意</strong>：推荐事件命名上采用跟 CDP 一致的方式，即以<code>.</code>间隔，以此来防止命名冲突，造成事件相互覆盖。</p>
<h4 data-id="heading-13">自建 WebSocket</h4>
<p>DevTools-pro 本身自带 WebSocket 服务，所以可以在 Backend 中使用<code>$devtools.createWebsocketConnection(wsUrl)</code>创建一个 WebSocket 链接：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// backend代码</span>
<span class="hljs-keyword">const</span> channelId = $devtools.nanoid();
<span class="hljs-comment">// -> 这里注意路径必须是/backend/开头</span>
<span class="hljs-keyword">const</span> wsUrl = $devtools.createWebsocketUrl(<span class="hljs-string">`/backend/<span class="hljs-subst">$&#123;channelId&#125;</span>`</span>);
<span class="hljs-keyword">const</span> ws = $devtools.createWebsocketConnection(wsUrl);
ws.on(<span class="hljs-string">'message'</span>, <span class="hljs-function"><span class="hljs-params">event</span> =></span> &#123;
    <span class="hljs-comment">// message</span>
&#125;);
<span class="hljs-comment">// 发送数据</span>
ws.send(<span class="hljs-string">'hi~'</span>);
<span class="hljs-comment">// ws链接建立成功</span>
ws.on(<span class="hljs-string">'open'</span>, onOpen);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>在 Frontend 插件中，需要利用 ChannelId 建立一条相同的 MessageChannel，这时候应该通过 CDP 事件将 channelId 由 Backend，发送的 Frontend：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// backend</span>
$devtools.sendCommand(<span class="hljs-string">'PluginName.channelId'</span>, channelId);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>然后在 Frontend 插件中：</p>
<pre><code class="hljs language-js copyable" lang="js">runtime.bridge.registerEvent(<span class="hljs-string">'PluginName.channelId'</span>, <span class="hljs-function"><span class="hljs-params">channelId</span> =></span> &#123;
    <span class="hljs-keyword">const</span> wsUrl = <span class="hljs-string">`/frontend/<span class="hljs-subst">$&#123;channelId&#125;</span>`</span>;
    <span class="hljs-keyword">const</span> ws = <span class="hljs-keyword">new</span> WebSocket(wsUrl);
    ws.onmessage = <span class="hljs-function"><span class="hljs-params">event</span> =></span> &#123;
        <span class="hljs-built_in">console</span>.log(event.data);
    &#125;;
    ws.send(<span class="hljs-string">'i am ready'</span>);
&#125;);
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-14">Middleware</h3>
<p>middleware 的定义是在<a href="https://juejin.cn/post/server/Server.js#L50">server/Server.js</a>，接受 3 个参数<code>middleware(router, logger, serverInstance)</code>：</p>
<ul>
<li><code>router</code>是<a href="https://www.npmjs.com/package/koa-router" target="_blank" rel="nofollow noopener noreferrer">koa-router</a>的实例；</li>
<li><code>logger</code>是<a href="https://www.npmjs.com/package/consola" target="_blank" rel="nofollow noopener noreferrer">consola</a>对象，有<code>logger.log</code>、<code>logger.info</code>、<code>logger.debug</code>等方法；</li>
<li><code>serverInstance</code>是 Server 类实例</li>
</ul>
<h4 data-id="heading-15">应用举例</h4>
<p>给 server 添加 router：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// middleware.js</span>
<span class="hljs-built_in">module</span>.exports = <span class="hljs-function"><span class="hljs-params">router</span> =></span> &#123;
    router.get(<span class="hljs-string">'/hi'</span>, <span class="hljs-function"><span class="hljs-params">ctx</span> =></span> &#123;
        ctx.body = <span class="hljs-string">'world'</span>;
    &#125;);
&#125;;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-16">其他脑洞</h2>
<h3 data-id="heading-17">自动化测试</h3>
<p>我们可以启动 DevTools-pro 之后，通过<a href="https://github.com/cyrus-and/chrome-remote-interface" target="_blank" rel="nofollow noopener noreferrer">chrome-remote-interface</a>链接 WebSocket，然后通过发送 CDP 命令，进行自动化测试。</p>
<p><img src="https://juejin.cn/post/docs/imgs/devtools-test.png" alt loading="lazy" referrerpolicy="no-referrer"></p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> CDP = <span class="hljs-built_in">require</span>(<span class="hljs-string">'chrome-remote-interface'</span>);

CDP(
    &#123;
        <span class="hljs-attr">target</span>: <span class="hljs-string">'ws://localhost:8899/frontend/TDBmn-IDKkaIV98iW20Qh'</span>
    &#125;,
    <span class="hljs-keyword">async</span> client => &#123;
        <span class="hljs-keyword">const</span> &#123;Page, Runtime&#125; = client;
        <span class="hljs-keyword">await</span> Page.enable();
        <span class="hljs-keyword">const</span> result = Runtime.evaluate(&#123;<span class="hljs-attr">expression</span>: <span class="hljs-string">'window.location.toString()'</span>&#125;);
        <span class="hljs-built_in">console</span>.log(result);
    &#125;
);
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-18">Vue-DevTools、San-DevTools 等集成</h3>
<p>我们可以在 frontend 的 module 中，添加一个 iframe 面板：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">export</span> <span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">SanDevtoolsPanel</span> <span class="hljs-keyword">extends</span> <span class="hljs-title">UI</span>.<span class="hljs-title">VBox</span> </span>&#123;
    <span class="hljs-function"><span class="hljs-title">constructor</span>(<span class="hljs-params"></span>)</span> &#123;
        <span class="hljs-built_in">super</span>(<span class="hljs-string">'san_devtools'</span>);
        <span class="hljs-built_in">this</span>.registerRequiredCSS(<span class="hljs-string">'san_devtools/san_devtools.css'</span>, &#123;<span class="hljs-attr">enableLegacyPatching</span>: <span class="hljs-literal">false</span>&#125;);
        <span class="hljs-built_in">this</span>.contentElement.classList.add(<span class="hljs-string">'html'</span>, <span class="hljs-string">'san-devtools'</span>);
    &#125;
    <span class="hljs-function"><span class="hljs-title">wasShown</span>(<span class="hljs-params"></span>)</span> &#123;
        <span class="hljs-built_in">this</span>._createIFrame();
    &#125;
    <span class="hljs-function"><span class="hljs-title">willHide</span>(<span class="hljs-params"></span>)</span> &#123;
        <span class="hljs-built_in">this</span>.contentElement.removeChildren();
    &#125;
    <span class="hljs-function"><span class="hljs-title">_createIFrame</span>(<span class="hljs-params"></span>)</span> &#123;
        <span class="hljs-built_in">this</span>.contentElement.removeChildren();
        <span class="hljs-keyword">const</span> iframe = <span class="hljs-built_in">document</span>.createElement(<span class="hljs-string">'iframe'</span>);
        iframe.className = <span class="hljs-string">'san-devtools-frame'</span>;
        iframe.setAttribute(<span class="hljs-string">'src'</span>, <span class="hljs-string">'/san-devtools.html'</span>);
        iframe.tabIndex = -<span class="hljs-number">1</span>;
        UI.ARIAUtils.markAsPresentation(iframe);
        <span class="hljs-built_in">this</span>.contentElement.appendChild(iframe);
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>然后在 Frontend 嵌入的页面中，可以直接建立自己的 WebSocket 链接直接跟 Backend 进行通信。</p>
<h2 data-id="heading-19">开发插件相关资料</h2>
<ul>
<li><a href="https://zhaomenghuan.js.org/blog/chrome-devtools.html" target="_blank" rel="nofollow noopener noreferrer">深入理解 Chrome DevTools</a></li>
<li><a href="https://zhaomenghuan.js.org/blog/chrome-devtools-frontend-analysis-of-principle.html" target="_blank" rel="nofollow noopener noreferrer">Chrome DevTools Frontend 运行原理浅析</a></li>
</ul></div>  
</div>
            