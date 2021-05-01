
---
title: '源码阅读-DoKit for Web'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=272'
author: 掘金
comments: false
date: Sat, 01 May 2021 02:28:59 GMT
thumbnail: 'https://picsum.photos/400/300?random=272'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h1 data-id="heading-0">源码阅读-DoKit for Web</h1>
<p>本文对应代码截止至2021.5.1</p>
<h2 data-id="heading-1">一些第一次接触的包</h2>
<h3 data-id="heading-2">npm-run-all</h3>
<p>一个<code>npm</code>的库，这个工具是为了解决官方的 <code>npm run</code> 命令无法同时运行多个脚本的问题</p>
<p>这个包提供三个命令，分别是 <code>npm-run-all</code> <code>run-s</code> <code>run-p</code>，其中后两个都是 <code>npm-run-all</code> 带参数的简写，分别对应串行和并行。</p>
<h3 data-id="heading-3">lerna</h3>
<p><code>Lerna</code> 是一个管理工具，用于管理包含多个软件包（<code>package</code>）的<code> JavaScript</code> 项目。</p>
<p><a href="https://github.com/lerna/lerna#getting-started" target="_blank" rel="nofollow noopener noreferrer">github 仓库</a></p>
<h4 data-id="heading-4">入门</h4>
<pre><code class="hljs language-shell copyable" lang="shell"><span class="hljs-meta">#</span><span class="bash"> 安装</span>
npm install --global lerna
<span class="hljs-meta">#</span><span class="bash"> 创建一个新的仓库代码</span>
git init lerna-repo && cd lerna-repo
<span class="hljs-meta">#</span><span class="bash"> 变为lerna仓库</span>
lerna init
<span class="copy-code-btn">复制代码</span></code></pre>
<p>你的代码仓库目前应该是如下结构：</p>
<pre><code class="copyable">my-lerna-repo/
  package.json
  packages/
    package-1/
      package.json
    package-2/
      package.json
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-5">常用指令</h4>
<blockquote>
<p>The two primary commands in Lerna are <code>lerna bootstrap</code> and <code>lerna publish</code>.</p>
<p><code>bootstrap</code> will link dependencies in the repo together. <code>publish</code> will help publish any updated packages.</p>
</blockquote>
<h3 data-id="heading-6">rollup.js</h3>
<blockquote>
<p>Rollup 是一个 JavaScript 模块打包器，可以将小块代码编译成大块复杂的代码，例如 library 或应用程序。</p>
</blockquote>
<p>待补充...</p>
<h2 data-id="heading-7">源码分析-组织结构</h2>
<p>目录结构是一个标准的<code>lerna</code>项目的结构，如上文介绍</p>
<h3 data-id="heading-8">package.json</h3>
<p>首先分析下根目录中的<code>package.json</code></p>
<pre><code class="hljs language-json copyable" lang="json">  <span class="hljs-string">"scripts"</span>: &#123;
    <span class="hljs-attr">"bootstrap"</span>: <span class="hljs-string">"run-s bootstrap:project bootstrap:package"</span>,
    <span class="hljs-attr">"bootstrap:project"</span>: <span class="hljs-string">"npm install"</span>,
    <span class="hljs-attr">"bootstrap:package"</span>: <span class="hljs-string">"lerna bootstrap"</span>,
    <span class="hljs-attr">"build"</span>: <span class="hljs-string">"lerna run build"</span>,
    <span class="hljs-attr">"dev"</span>: <span class="hljs-string">"lerna run dev --parallel"</span>,
    <span class="hljs-attr">"dev:playground"</span>: <span class="hljs-string">"run-p serve:playground dev"</span>,
    <span class="hljs-attr">"serve:playground"</span>: <span class="hljs-string">"node scripts/dev-playground.js"</span>,
    <span class="hljs-attr">"clean"</span>: <span class="hljs-string">"run-s clean:lerna clean:lock"</span>,
    <span class="hljs-attr">"clean:lerna"</span>: <span class="hljs-string">"lerna clean --yes"</span>,
    <span class="hljs-attr">"clean:lock"</span>: <span class="hljs-string">"run-s clean:lock-package clean:lock-subpackage"</span>,
    <span class="hljs-attr">"clean:lock-package"</span>: <span class="hljs-string">"rm -rf ./package-lock.json"</span>,
    <span class="hljs-attr">"clean:lock-subpackage"</span>: <span class="hljs-string">"rm -rf ./packages/**/package-lock.json"</span>
  &#125;,
<span class="copy-code-btn">复制代码</span></code></pre>
<p>运行的指令分别为<code>npm run bootstrap</code>,<code>npm run build</code>和<code>npm run dev:playground</code></p>
<p>前两者都是在安装依赖相关内容，主要运行的部分为</p>
<pre><code class="hljs language-shell copyable" lang="shell">node scripts/dev-playground.js
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-9">scripts/dev-playground.js</h3>
<p>可以看到入口在<code>dev-playground.js</code>文件中，其代码如下：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> http = <span class="hljs-built_in">require</span>(<span class="hljs-string">'http'</span>);
<span class="hljs-keyword">const</span> serveHandler = <span class="hljs-built_in">require</span>(<span class="hljs-string">'serve-handler'</span>);
<span class="hljs-keyword">const</span> open = <span class="hljs-built_in">require</span>(<span class="hljs-string">'open'</span>);

run();
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">run</span>(<span class="hljs-params"></span>)</span>&#123;
  <span class="hljs-keyword">const</span> server = http.createServer(<span class="hljs-function">(<span class="hljs-params">request, response</span>) =></span> &#123;
    <span class="hljs-keyword">return</span> serveHandler(request, response);
  &#125;)   
  server.listen(<span class="hljs-number">3000</span>, <span class="hljs-function">() =></span> &#123;
    <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'Dev Server Running at http://localhost:3000'</span>);
    open(<span class="hljs-string">'http://localhost:3000/playground'</span>);
  &#125;)
&#125;

<span class="copy-code-btn">复制代码</span></code></pre>
<p>这一部分是运行了一个<code>server</code>，并指向了<code>./playground/index.html</code>文件</p>
<h3 data-id="heading-10">/playground/index.html</h3>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-meta"><!DOCTYPE <span class="hljs-meta-keyword">html</span>></span>
<span class="hljs-tag"><<span class="hljs-name">html</span> <span class="hljs-attr">lang</span>=<span class="hljs-string">"en"</span>></span>

<span class="hljs-tag"><<span class="hljs-name">head</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">meta</span> <span class="hljs-attr">charset</span>=<span class="hljs-string">"UTF-8"</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">meta</span> <span class="hljs-attr">http-equiv</span>=<span class="hljs-string">"X-UA-Compatible"</span> <span class="hljs-attr">content</span>=<span class="hljs-string">"IE=edge"</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">meta</span> <span class="hljs-attr">name</span>=<span class="hljs-string">"viewport"</span> <span class="hljs-attr">content</span>=<span class="hljs-string">"width=device-width, initial-scale=1.0"</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">title</span>></span>Dokit For Web<span class="hljs-tag"></<span class="hljs-name">title</span>></span>
<span class="hljs-tag"></<span class="hljs-name">head</span>></span>

<span class="hljs-tag"><<span class="hljs-name">body</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">h1</span>></span>Dokit For Web<span class="hljs-tag"></<span class="hljs-name">h1</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">h2</span>></span>Playground<span class="hljs-tag"></<span class="hljs-name">h2</span>></span>
<span class="hljs-tag"></<span class="hljs-name">body</span>></span>
<span class="hljs-tag"><<span class="hljs-name">script</span> <span class="hljs-attr">src</span>=<span class="hljs-string">"https://unpkg.com/vue@next"</span>></span><span class="hljs-tag"></<span class="hljs-name">script</span>></span>
<span class="hljs-tag"><<span class="hljs-name">script</span> <span class="hljs-attr">src</span>=<span class="hljs-string">"../packages/web/dist/dokit.js"</span>></span><span class="hljs-tag"></<span class="hljs-name">script</span>></span>
<span class="hljs-tag"></<span class="hljs-name">html</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这边是主要的网页入口了，其引入的内容都在<code>web/dist/dokit.js</code>中</p>
<h3 data-id="heading-11">packages/web/</h3>
<p>该目录下是一个利用<code>rollup</code>打包的模块，查看<code>rollup.config.js</code>可以看到，上文所引用的<code>dokit.js</code>便是打包的输出文件，输入文件为<code>src/index.js</code></p>
<h4 data-id="heading-12">src/index.js</h4>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">import</span> &#123;Dokit&#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'@dokit/web-core'</span>
<span class="hljs-keyword">import</span> &#123;Features&#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'./feature'</span>
<span class="hljs-comment">/*
* TODO 全局注册 Dokit
*/</span>
<span class="hljs-built_in">window</span>.Dokit = <span class="hljs-keyword">new</span> Dokit(&#123;
  <span class="hljs-attr">features</span>: Features,
&#125;);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>根据<code>js</code>内容，继续找到<code>feature.js</code>和<code>@dokit/web-core</code></p>
<h4 data-id="heading-13">src/feature.js</h4>
<p>在这个文件中，可以看到，一共引入了4个插件</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">import</span> Console <span class="hljs-keyword">from</span> <span class="hljs-string">'./plugins/console/index'</span>
<span class="hljs-keyword">import</span> AppInfo <span class="hljs-keyword">from</span> <span class="hljs-string">'./plugins/app-info/index'</span>
<span class="hljs-keyword">import</span> DemoPlugin <span class="hljs-keyword">from</span> <span class="hljs-string">'./plugins/demo-plugin/index'</span>
<span class="hljs-keyword">import</span> HelloWorld <span class="hljs-keyword">from</span> <span class="hljs-string">'./components/ToolHelloWorld'</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>然而网页中显示的有很多个插件，继续向下看</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">export</span> <span class="hljs-keyword">const</span> BasicFeatures = &#123;
  <span class="hljs-attr">title</span>: <span class="hljs-string">'常用工具'</span>,
  <span class="hljs-attr">list</span>: [Console, AppInfo, DemoPlugin, &#123;
    <span class="hljs-attr">nameZh</span>: <span class="hljs-string">'H5任意门a '</span>,
    <span class="hljs-attr">name</span>: <span class="hljs-string">'h5-door'</span>,
    <span class="hljs-attr">icon</span>: <span class="hljs-string">'https://pt-starimg.didistatic.com/static/starimg/img/FHqpI3InaS1618997548865.png'</span>,
    <span class="hljs-attr">component</span>: AppInfo
  &#125;]
&#125;

<span class="hljs-keyword">export</span> <span class="hljs-keyword">const</span> DokitFeatures = &#123;
  <span class="hljs-attr">title</span>: <span class="hljs-string">'平台功能'</span>,
  <span class="hljs-attr">list</span>: [&#123;
    <span class="hljs-attr">nameZh</span>: <span class="hljs-string">'Mock数据'</span>,
    <span class="hljs-attr">name</span>: <span class="hljs-string">'mock'</span>,
    <span class="hljs-attr">icon</span>: <span class="hljs-string">'https://pt-starimg.didistatic.com/static/starimg/img/aDn77poRDB1618997545078.png'</span>,
    <span class="hljs-attr">component</span>: HelloWorld
  &#125;]
&#125;

<span class="hljs-keyword">export</span> <span class="hljs-keyword">const</span> UIFeatures = &#123;
  <span class="hljs-attr">title</span>: <span class="hljs-string">'视觉功能'</span>,
  <span class="hljs-attr">list</span>: [&#123;
    <span class="hljs-attr">nameZh</span>: <span class="hljs-string">'取色器'</span>,
    <span class="hljs-attr">name</span>: <span class="hljs-string">'color-selector'</span>,
    <span class="hljs-attr">icon</span>: <span class="hljs-string">'https://pt-starimg.didistatic.com/static/starimg/img/QYUvEE8FnN1618997536890.png'</span>,
    <span class="hljs-attr">component</span>: HelloWorld
  &#125;, &#123;
    <span class="hljs-attr">nameZh</span>: <span class="hljs-string">'对齐标尺'</span>,
    <span class="hljs-attr">name</span>: <span class="hljs-string">'align-ruler'</span>,
    <span class="hljs-attr">icon</span>: <span class="hljs-string">'https://pt-starimg.didistatic.com/static/starimg/img/a5UTjMn6lO1618997535798.png'</span>,
    <span class="hljs-attr">component</span>: HelloWorld
  &#125;, &#123;
    <span class="hljs-attr">nameZh</span>: <span class="hljs-string">'UI结构'</span>,
    <span class="hljs-attr">name</span>: <span class="hljs-string">'view-selector'</span>,
    <span class="hljs-attr">icon</span>: <span class="hljs-string">'https://pt-starimg.didistatic.com/static/starimg/img/XNViIWzG7N1618997548483.png'</span>,
    <span class="hljs-attr">component</span>: HelloWorld
  &#125;]
&#125;
<span class="hljs-keyword">export</span> <span class="hljs-keyword">const</span> Features = [BasicFeatures, DokitFeatures, UIFeatures]
<span class="copy-code-btn">复制代码</span></code></pre>
<p>可以看到，<code>DokitFeatures</code>和<code>UIFeatures</code>中只是占了位置，实际对应的插件还是<code>HelloWorld</code>的<code>demo</code>，最后将这些全部<code>export</code>出去即可。</p>
<h3 data-id="heading-14">packages/core</h3>
<p>在上面看到，声明了一个全局组件<code>Dokit</code>，这个来自于<code>@dokit/web-core</code>，继续寻找其定义位置。既然是<code>web-core</code>，那就在<code>core/</code>文件夹下寻找试试。查看<code>package.json</code>，该目录下文件的<code>name</code>就是<code>@dokit/web-core</code>，其<code>main</code>文件为<code>dist/index.js</code>。不难猜出，这个文件仍是<code>rollup</code>打包出来的文件，查看<code>rollup.config.js</code>，源文件为<code>src/index.js</code>。在这里，找到了<code>Dokit</code>的定义：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">import</span> &#123;createApp&#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'vue'</span>
<span class="hljs-keyword">import</span> App <span class="hljs-keyword">from</span> <span class="hljs-string">'./components/app'</span>
<span class="hljs-keyword">import</span> Store <span class="hljs-keyword">from</span> <span class="hljs-string">'./store'</span>
<span class="hljs-keyword">import</span> &#123;applyLifecyle, LifecycleHooks&#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'./common/js/lifecycle'</span> 
<span class="hljs-keyword">import</span> &#123;getRouter&#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'./router'</span>
<span class="hljs-keyword">export</span> <span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Dokit</span></span>&#123;
  options = <span class="hljs-literal">null</span>
  <span class="hljs-function"><span class="hljs-title">constructor</span>(<span class="hljs-params">options</span>)</span>&#123;
    <span class="hljs-built_in">this</span>.options = options
    <span class="hljs-keyword">let</span> app = createApp(App);
    <span class="hljs-keyword">let</span> &#123;features&#125; = options; 
    app.use(getRouter(features));
    app.use(Store);
    Store.state.features = features;
    <span class="hljs-built_in">this</span>.app = app;
    <span class="hljs-built_in">this</span>.init();
    <span class="hljs-built_in">this</span>.onLoad();
  &#125;

  <span class="hljs-function"><span class="hljs-title">onLoad</span>(<span class="hljs-params"></span>)</span>&#123;
    <span class="hljs-comment">// Lifecycle Load</span>
    applyLifecyle(<span class="hljs-built_in">this</span>.options.features, LifecycleHooks.LOAD)
  &#125;

  <span class="hljs-function"><span class="hljs-title">onUnload</span>(<span class="hljs-params"></span>)</span>&#123;
    <span class="hljs-comment">// Lifecycle UnLoad</span>
    applyLifecyle(<span class="hljs-built_in">this</span>.options.features, LifecycleHooks.UNLOAD)
  &#125;

  <span class="hljs-function"><span class="hljs-title">init</span>(<span class="hljs-params"></span>)</span>&#123;
    <span class="hljs-keyword">let</span> dokitRoot = <span class="hljs-built_in">document</span>.createElement(<span class="hljs-string">'div'</span>)
    dokitRoot.id = <span class="hljs-string">"dokit-root"</span>
    <span class="hljs-built_in">document</span>.documentElement.appendChild(dokitRoot);
    <span class="hljs-comment">// dokit 容器</span>
    <span class="hljs-keyword">let</span> el = <span class="hljs-built_in">document</span>.createElement(<span class="hljs-string">'div'</span>)
    el.id = <span class="hljs-string">"dokit-container"</span>
    <span class="hljs-built_in">this</span>.app.mount(el)
    dokitRoot.appendChild(el)
  &#125;
&#125;

<span class="hljs-keyword">export</span> * <span class="hljs-keyword">from</span> <span class="hljs-string">'./store'</span>
<span class="hljs-keyword">export</span> * <span class="hljs-keyword">from</span> <span class="hljs-string">'./common/js/feature'</span>

<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> &#123;
  Dokit
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><code>Dokit</code>的初始化过程中现根据<code>App</code>创建一个实例，然后加载了两个模板<code>getRouter</code>和<code>Store</code>，并把插件<code>Features</code>传给了<code>Store</code>。<code>init()</code>函数中将<code>dokit</code>插件插入到了文档流中。</p>
<p>按顺序依次查看源码。</p>
<h4 data-id="heading-15">components/app.vue</h4>
<pre><code class="hljs language-js copyable" lang="js"><template>
  <span class="xml"><span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"dokit-app"</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"dokit-entry-btn"</span> <span class="hljs-attr">v-dragable</span> @<span class="hljs-attr">click</span>=<span class="hljs-string">"toggleContainer"</span>></span><span class="hljs-tag"></<span class="hljs-name">div</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"mask"</span> <span class="hljs-attr">v-show</span>=<span class="hljs-string">"showContainer"</span> @<span class="hljs-attr">click</span>=<span class="hljs-string">"toggleContainer"</span>></span><span class="hljs-tag"></<span class="hljs-name">div</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">router-container</span> <span class="hljs-attr">v-show</span>=<span class="hljs-string">"showContainer"</span>></span><span class="hljs-tag"></<span class="hljs-name">router-container</span>></span>
  <span class="hljs-tag"></<span class="hljs-name">div</span>></span></span>
</template>

<span class="xml"><span class="hljs-tag"><<span class="hljs-name">script</span>></span><span class="javascript">
<span class="hljs-keyword">import</span> dragable <span class="hljs-keyword">from</span> <span class="hljs-string">"../common/directives/dragable"</span>;
<span class="hljs-keyword">import</span> RouterContainer <span class="hljs-keyword">from</span> <span class="hljs-string">'./container'</span>;

<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> &#123;
  <span class="hljs-attr">components</span>: &#123;
    RouterContainer
  &#125;,
  <span class="hljs-attr">directives</span>: &#123;
    dragable,
  &#125;,
  <span class="hljs-function"><span class="hljs-title">data</span>(<span class="hljs-params"></span>)</span> &#123;
    <span class="hljs-keyword">return</span> &#123;
      <span class="hljs-attr">showContainer</span>: <span class="hljs-literal">false</span>,
    &#125;;
  &#125;,
  <span class="hljs-attr">methods</span>: &#123;
    <span class="hljs-function"><span class="hljs-title">toggleContainer</span>(<span class="hljs-params"></span>)</span> &#123;
      <span class="hljs-built_in">this</span>.showContainer = !<span class="hljs-built_in">this</span>.showContainer;
    &#125;,
  &#125;,
&#125;;
</span><span class="hljs-tag"></<span class="hljs-name">script</span>></span></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p><code>app.vue</code>里声明了一个组件，其对应的应该是<code>Dokit</code>的按钮，通过<code>showContainer</code>来控制是否展示插件容器。这里面又使用了<code>RouterContainer</code></p>
<h4 data-id="heading-16">components/container.vue</h4>
<pre><code class="hljs language-js copyable" lang="js"><template>  <span class="xml"><span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"container"</span>></span>    <span class="hljs-tag"><<span class="hljs-name">top-bar</span> <span class="hljs-attr">:title</span>=<span class="hljs-string">"title"</span> <span class="hljs-attr">:canBack</span>=<span class="hljs-string">"canBack"</span>></span><span class="hljs-tag"></<span class="hljs-name">top-bar</span>></span>    <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"router-container"</span>></span>      <span class="hljs-tag"><<span class="hljs-name">router-view</span> <span class="hljs-attr">v-slot</span>=<span class="hljs-string">"&#123; Component &#125;"</span>></span>        <span class="hljs-tag"><<span class="hljs-name">keep-alive</span>></span>          <span class="hljs-tag"><<span class="hljs-name">component</span> <span class="hljs-attr">:is</span>=<span class="hljs-string">"Component"</span> /></span>        <span class="hljs-tag"></<span class="hljs-name">keep-alive</span>></span>      <span class="hljs-tag"></<span class="hljs-name">router-view</span>></span>    <span class="hljs-tag"></<span class="hljs-name">div</span>></span>  <span class="hljs-tag"></<span class="hljs-name">div</span>></span></span><<span class="hljs-regexp">/template><script>import TopBar from "../</span>common/components/top-bar<span class="hljs-string">";export default &#123;  components: &#123;   TopBar   &#125;,  data()&#123;    return &#123;&#125;  &#125;,  computed:&#123;    curRoute()&#123;      return this.$router.currentRoute.value    &#125;,    title()&#123;      return this.curRoute.meta.title || 'Dokit'    &#125;,    canBack()&#123;      return this.curRoute.name !== 'index'    &#125;  &#125;,  created()&#123;  &#125;&#125;</script>
</span><span class="copy-code-btn">复制代码</span></code></pre>
<p>可以看到，这里便是<code>Dokit</code>的菜单栏组件</p>
<h4 data-id="heading-17">store/index.js</h4>
<p>接下来继续看<code>Store</code>的源码</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">import</span> &#123; Store &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">"../common/js/store"</span>;<span class="hljs-keyword">const</span> store = <span class="hljs-keyword">new</span> Store(&#123;  <span class="hljs-attr">state</span>: &#123;    <span class="hljs-attr">features</span>: []  &#125;&#125;)<span class="hljs-comment">// 更新全局 Store 数据export function updateGlobalData(key, value)&#123;  store.state[key] = value&#125;// 获取当前 Store 数据的状态export function getGlobalData()&#123;  return store.state&#125;export default store</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>看起来这个类使用来进行数据存储</p>
<p>继续看一下<code>Store</code>的定义</p>
<h4 data-id="heading-18">common/js/store.js</h4>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">import</span> &#123;reactive&#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'vue'</span><span class="hljs-keyword">const</span> storeKey = <span class="hljs-string">'store'</span><span class="hljs-comment">/** * 简易版 Store 实现 * 支持直接修改 Store 数据 */</span><span class="hljs-keyword">export</span> <span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Store</span></span>&#123;  <span class="hljs-function"><span class="hljs-title">constructor</span>(<span class="hljs-params">options</span>)</span>&#123;    <span class="hljs-keyword">let</span> &#123;state&#125; = options    <span class="hljs-built_in">this</span>.initData(state)  &#125;  <span class="hljs-function"><span class="hljs-title">initData</span>(<span class="hljs-params">data = &#123;&#125;</span>)</span>&#123;    <span class="hljs-built_in">this</span>._state = reactive(&#123;      <span class="hljs-attr">data</span>: data    &#125;)  &#125;  <span class="hljs-keyword">get</span> <span class="hljs-title">state</span>()&#123;    <span class="hljs-keyword">return</span> <span class="hljs-built_in">this</span>._state.data  &#125;  <span class="hljs-function"><span class="hljs-title">install</span>(<span class="hljs-params">app</span>)</span>&#123;    app.provide(storeKey, <span class="hljs-built_in">this</span>)    app.config.globalProperties.$store = <span class="hljs-built_in">this</span>  &#125;&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>源码里展现出的也的确是存取数据的功能。</p>
<h4 data-id="heading-19">router/index.js</h4>
<p>继续分析<code>Dokit</code>引入的组件，下一个是<code>getRouter</code>组件:</p>
<pre><code class="hljs language-js copyable" lang="js">app.use(getRouter(features));
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这里将<code>features</code>都传给了<code>getRouter</code></p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">import</span> &#123; createRouter, createMemoryHistory &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'vue-router'</span><span class="hljs-keyword">import</span> &#123;routes, getRoutes&#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'./routes'</span><span class="hljs-keyword">export</span> <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">getRouter</span>(<span class="hljs-params">features</span>)</span>&#123;  <span class="hljs-keyword">return</span> createRouter(&#123;    <span class="hljs-attr">routes</span>: [...routes, ...getRoutes(features)],    <span class="hljs-attr">history</span>: createMemoryHistory()  &#125;)&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><code>getRouter</code>接收到<code>features</code>参数之后，调用<code>getRoutes</code>函数并进一步创建路由</p>
<h4 data-id="heading-20">router/routers.js</h4>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">import</span> Index <span class="hljs-keyword">from</span> <span class="hljs-string">'../components/index'</span><span class="hljs-keyword">export</span> <span class="hljs-keyword">const</span> routes = [&#123;  <span class="hljs-attr">path</span>: <span class="hljs-string">'/'</span>,  <span class="hljs-attr">name</span>: <span class="hljs-string">'index'</span>,  <span class="hljs-attr">component</span>: Index&#125;]<span class="hljs-keyword">export</span> <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">getRoutes</span>(<span class="hljs-params">features</span>)</span>&#123;  <span class="hljs-keyword">let</span> routes = []  features.forEach(<span class="hljs-function"><span class="hljs-params">feature</span> =></span> &#123;    <span class="hljs-keyword">let</span> &#123;list, <span class="hljs-attr">title</span>:featureTitle&#125; = feature    list.forEach(<span class="hljs-function"><span class="hljs-params">item</span> =></span> &#123;      <span class="hljs-comment">// TODO 暂时只支持路由方式的插件      let &#123;name, title, component&#125; = item      routes.push(&#123;        path: `/$&#123;name&#125;`,        name: name,        component: component.component || component,        meta: &#123;          title: title,          feature: featureTitle        &#125;      &#125;)    &#125;)  &#125;)  return routes&#125;</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这部分的内容也很容易理解，即对<code>features</code>里的内容依次生成路由，从而完成不同插件页面的跳转。</p>
<p>可以看到，在头部还引入了一个根目录路由<code>Index</code>，继续深入分析</p>
<h4 data-id="heading-21">components/index.vue</h4>
<pre><code class="hljs language-js copyable" lang="js"><template>  <span class="xml"><span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"index-container"</span>></span>    <span class="hljs-tag"><<span class="hljs-name">card</span>      <span class="hljs-attr">v-for</span>=<span class="hljs-string">"(item, index) in features"</span>      <span class="hljs-attr">:key</span>=<span class="hljs-string">"index"</span>      <span class="hljs-attr">:title</span>=<span class="hljs-string">"item.title"</span>      <span class="hljs-attr">:list</span>=<span class="hljs-string">"item.list"</span>    ></span><span class="hljs-tag"></<span class="hljs-name">card</span>></span>    <span class="hljs-tag"><<span class="hljs-name">version-card</span> <span class="hljs-attr">:version</span>=<span class="hljs-string">"version"</span>></span><span class="hljs-tag"></<span class="hljs-name">version-card</span>></span>  <span class="hljs-tag"></<span class="hljs-name">div</span>></span></span><<span class="hljs-regexp">/template><script>import TopBar from "../</span>common/components/top-bar<span class="hljs-string">";import Card from "</span>../common/components/card<span class="hljs-string">";import VersionCard from "</span>../common/components/version<span class="hljs-string">";export default &#123;  components: &#123;    TopBar,    Card,    VersionCard  &#125;,  data()&#123;    return &#123;      version: '1.3.0'    &#125;  &#125;,  mounted()&#123;  &#125;,  computed: &#123;    features()&#123;      return this.$store.state.features    &#125;  &#125;&#125;;</script>
</span><span class="copy-code-btn">复制代码</span></code></pre>
<p>该组件便是<code>Dokit</code>的菜单页面了，将<code>features</code>的内容分别生成一个<code><card></code>。在<code>web/src/features.js</code>中可以看到，<code>features</code>中还对不同插件进行了功能分类，每种功能下有若干个插件，那么可以猜想<code><card></code>中会再次遍历<code>list</code>，然后生成不同插件的按钮。</p>
<p>找到<code>card.vue</code>:</p>
<h4 data-id="heading-22">comon/components/card.vue</h4>
<pre><code class="hljs language-js copyable" lang="js"><template>  <span class="xml"><span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"card"</span>></span>    <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"card-title"</span>></span>      <span class="hljs-tag"><<span class="hljs-name">span</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"card-title-text"</span>></span> &#123;&#123;title&#125;&#125; <span class="hljs-tag"></<span class="hljs-name">span</span>></span>    <span class="hljs-tag"></<span class="hljs-name">div</span>></span>    <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"item-list"</span>></span>      <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"item"</span> <span class="hljs-attr">v-for</span>=<span class="hljs-string">"(item,index) in list"</span> <span class="hljs-attr">:key</span>=<span class="hljs-string">"index"</span> @<span class="hljs-attr">click</span>=<span class="hljs-string">"handleClickItem(item)"</span>></span>        <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"item-icon"</span>></span>          <span class="hljs-tag"><<span class="hljs-name">img</span>            <span class="hljs-attr">class</span>=<span class="hljs-string">"item-icon-image"</span>            <span class="hljs-attr">:src</span>=<span class="hljs-string">"item.icon || defaultIcon"</span>          /></span>        <span class="hljs-tag"></<span class="hljs-name">div</span>></span>        <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"item-title"</span>></span>&#123;&#123;item.nameZh || '默认功能'&#125;&#125;<span class="hljs-tag"></<span class="hljs-name">div</span>></span>      <span class="hljs-tag"></<span class="hljs-name">div</span>></span>    <span class="hljs-tag"></<span class="hljs-name">div</span>></span>  <span class="hljs-tag"></<span class="hljs-name">div</span>></span></span><<span class="hljs-regexp">/template><script>import &#123;DefaultItemIcon&#125; from '../</span>js/icon<span class="hljs-string">'export default &#123;  props: &#123;    title: &#123;      default: '</span>专区<span class="hljs-string">'    &#125;,    list: &#123;      default: []    &#125;  &#125;,  data()&#123;    return &#123;      defaultIcon: DefaultItemIcon    &#125;  &#125;,  methods: &#123;    handleClickItem(item)&#123;      this.$router.push(&#123;        name: item.name      &#125;)    &#125;  &#125;&#125;;</script>
</span><span class="copy-code-btn">复制代码</span></code></pre>
<p>的确，代码中对<code>list</code>进行遍历，然后对每个插件生成一个按钮，与猜想一样。</p>
<h2 data-id="heading-23">源码分析-功能实现</h2>
<p>目前<code>web</code>端仅实现了<code>日志</code>和<code>应用信息</code>两个功能，其他功能只有<code>demo</code>模板。</p>
<h3 data-id="heading-24">app-info</h3>
<p><strong>ToolAppInfo.vue</strong></p>
<pre><code class="hljs language-js copyable" lang="js"><template>  <span class="xml"><span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"app-info-container"</span>></span>    <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"info-wrapper"</span>></span>      <span class="hljs-tag"><<span class="hljs-name">Card</span> <span class="hljs-attr">title</span>=<span class="hljs-string">"Page Info"</span>></span>        <span class="hljs-tag"><<span class="hljs-name">table</span> <span class="hljs-attr">border</span>=<span class="hljs-string">"1"</span>></span>          <span class="hljs-tag"><<span class="hljs-name">tr</span>></span>            <span class="hljs-tag"><<span class="hljs-name">td</span>></span>UA<span class="hljs-tag"></<span class="hljs-name">td</span>></span>            <span class="hljs-tag"><<span class="hljs-name">td</span>></span>&#123;&#123;ua&#125;&#125;<span class="hljs-tag"></<span class="hljs-name">td</span>></span>          <span class="hljs-tag"></<span class="hljs-name">tr</span>></span>          <span class="hljs-tag"><<span class="hljs-name">tr</span>></span>            <span class="hljs-tag"><<span class="hljs-name">td</span>></span>URL<span class="hljs-tag"></<span class="hljs-name">td</span>></span>            <span class="hljs-tag"><<span class="hljs-name">td</span>></span>&#123;&#123;url&#125;&#125;<span class="hljs-tag"></<span class="hljs-name">td</span>></span>          <span class="hljs-tag"></<span class="hljs-name">tr</span>></span>        <span class="hljs-tag"></<span class="hljs-name">table</span>></span>      <span class="hljs-tag"></<span class="hljs-name">Card</span>></span>    <span class="hljs-tag"></<span class="hljs-name">div</span>></span>    <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"info-wrapper"</span>></span>      <span class="hljs-tag"><<span class="hljs-name">Card</span> <span class="hljs-attr">title</span>=<span class="hljs-string">"Device Info"</span>></span>        <span class="hljs-tag"><<span class="hljs-name">table</span> <span class="hljs-attr">border</span>=<span class="hljs-string">"1"</span>></span>          <span class="hljs-tag"><<span class="hljs-name">tr</span>></span>            <span class="hljs-tag"><<span class="hljs-name">td</span>></span>设备缩放比<span class="hljs-tag"></<span class="hljs-name">td</span>></span>            <span class="hljs-tag"><<span class="hljs-name">td</span>></span>&#123;&#123;ratio&#125;&#125;<span class="hljs-tag"></<span class="hljs-name">td</span>></span>          <span class="hljs-tag"></<span class="hljs-name">tr</span>></span>          <span class="hljs-tag"><<span class="hljs-name">tr</span>></span>            <span class="hljs-tag"><<span class="hljs-name">td</span>></span>screen<span class="hljs-tag"></<span class="hljs-name">td</span>></span>            <span class="hljs-tag"><<span class="hljs-name">td</span>></span>&#123;&#123;screen.width&#125;&#125;X&#123;&#123;screen.height&#125;&#125;<span class="hljs-tag"></<span class="hljs-name">td</span>></span>          <span class="hljs-tag"></<span class="hljs-name">tr</span>></span>          <span class="hljs-tag"><<span class="hljs-name">tr</span>></span>            <span class="hljs-tag"><<span class="hljs-name">td</span>></span>viewport<span class="hljs-tag"></<span class="hljs-name">td</span>></span>            <span class="hljs-tag"><<span class="hljs-name">td</span>></span>&#123;&#123;viewport.width&#125;&#125;X&#123;&#123;viewport.height&#125;&#125;<span class="hljs-tag"></<span class="hljs-name">td</span>></span>          <span class="hljs-tag"></<span class="hljs-name">tr</span>></span>        <span class="hljs-tag"></<span class="hljs-name">table</span>></span>      <span class="hljs-tag"></<span class="hljs-name">Card</span>></span>    <span class="hljs-tag"></<span class="hljs-name">div</span>></span>  <span class="hljs-tag"></<span class="hljs-name">div</span>></span></span><<span class="hljs-regexp">/template><script>import Card from '../</span>../common/Card<span class="hljs-string">'export default &#123;  components: &#123;    Card  &#125;,  data() &#123;    return &#123;      ua: window.navigator.userAgent,      url: window.location.href,      ratio: window.devicePixelRatio,      screen: window.screen,      viewport: &#123;        width: document.documentElement.clientWidth,        height: document.documentElement.clientHeight      &#125;    &#125;  &#125;,&#125;
</span><span class="copy-code-btn">复制代码</span></code></pre>
<p>这一部分内容比较简单，都是调用了<code>js</code>中<code>window</code>和<code>document</code>中的内置函数来获取设备信息，通过<code>vue</code>的数据绑定显示出来</p>
<h3 data-id="heading-25">console</h3>
<p>该插件功能实现略微复杂，从目录结构就可以看出，分了很多个小模块</p>
<pre><code class="copyable">console/- css/- js/--- console.js- console-tap.vue- index.js- log-container.vue- log-detail,vue- log-item.vue- main.vue- op-command.vue
<span class="copy-code-btn">复制代码</span></code></pre>
<p>从<code>index.js</code>中可以看到:</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">import</span> Console <span class="hljs-keyword">from</span> <span class="hljs-string">'./main.vue'</span><span class="hljs-keyword">import</span> &#123;overrideConsole,restoreConsole&#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'./js/console'</span><span class="hljs-keyword">import</span> &#123;getGlobalData, RouterPlugin&#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'@dokit/web-core'</span><span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> <span class="hljs-keyword">new</span> RouterPlugin(&#123;  <span class="hljs-attr">name</span>: <span class="hljs-string">'console'</span>,  <span class="hljs-attr">nameZh</span>: <span class="hljs-string">'日志'</span>,  <span class="hljs-attr">component</span>: Console,  <span class="hljs-attr">icon</span>: <span class="hljs-string">'https://pt-starimg.didistatic.com/static/starimg/img/PbNXVyzTbq1618997544543.png'</span>,  <span class="hljs-function"><span class="hljs-title">onLoad</span>(<span class="hljs-params"></span>)</span>&#123;    <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'Load'</span>)    overrideConsole(<span class="hljs-function">(<span class="hljs-params">&#123;name, type, value&#125;</span>) =></span> &#123;      <span class="hljs-keyword">let</span> state = getGlobalData();      state.logList = state.logList || [];      state.logList.push(&#123;        <span class="hljs-attr">type</span>: type,        <span class="hljs-attr">name</span>: name,        <span class="hljs-attr">value</span>: value      &#125;);    &#125;);  &#125;,  <span class="hljs-function"><span class="hljs-title">onUnload</span>(<span class="hljs-params"></span>)</span>&#123;    restoreConsole()  &#125;&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>主要插件为从<code>main.vue</code>中引入的<code>Console</code></p>
<h4 data-id="heading-26">main.vue</h4>
<pre><code class="hljs language-js copyable" lang="js"><template>  <span class="xml"><span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"console-container"</span>></span>    <span class="hljs-tag"><<span class="hljs-name">console-tap</span> <span class="hljs-attr">:tabs</span>=<span class="hljs-string">"logTabs"</span> @<span class="hljs-attr">changeTap</span>=<span class="hljs-string">"handleChangeTab"</span>></span><span class="hljs-tag"></<span class="hljs-name">console-tap</span>></span>    <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"log-container"</span>></span>      <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"info-container"</span>></span>        <span class="hljs-tag"><<span class="hljs-name">log-container</span> <span class="hljs-attr">:logList</span>=<span class="hljs-string">"curLogList"</span>></span><span class="hljs-tag"></<span class="hljs-name">log-container</span>></span>      <span class="hljs-tag"></<span class="hljs-name">div</span>></span>      <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"operation-container"</span>></span>        <span class="hljs-tag"><<span class="hljs-name">operation-command</span>></span><span class="hljs-tag"></<span class="hljs-name">operation-command</span>></span>      <span class="hljs-tag"></<span class="hljs-name">div</span>></span>    <span class="hljs-tag"></<span class="hljs-name">div</span>></span>  <span class="hljs-tag"></<span class="hljs-name">div</span>></span></span><<span class="hljs-regexp">/template><script>import ConsoleTap from './</span><span class="hljs-built_in">console</span>-tap<span class="hljs-string">';import LogContainer from '</span>./log-container<span class="hljs-string">';import OperationCommand from '</span>./op-command<span class="hljs-string">';import &#123;LogTabs, LogEnum&#125; from '</span>./js/<span class="hljs-built_in">console</span><span class="hljs-string">'export default &#123;  components: &#123;    ConsoleTap,    LogContainer,    OperationCommand  &#125;,  data() &#123;    return &#123;      logTabs: LogTabs,      curTab: LogEnum.ALL    &#125;  &#125;,  computed:&#123;    logList()&#123;      return this.$store.state.logList || []    &#125;,    curLogList()&#123;      if(this.curTab == LogEnum.ALL)&#123;        return this.logList      &#125;      return this.logList.filter(log => &#123;        return log.type == this.curTab      &#125;)    &#125;  &#125;,  created () &#123;&#125;,  methods: &#123;    handleChangeTab(type)&#123;      this.curTab = type    &#125;  &#125;&#125;</script>
</span><span class="copy-code-btn">复制代码</span></code></pre>
<p>在这里一下次又引入了四个组件，接下来继续依次进行分析</p>
<h4 data-id="heading-27">console-tab.vue</h4>
<pre><code class="hljs language-js copyable" lang="js"><template>  <span class="xml"><span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"tab-container"</span>></span>    <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"tab-list"</span>></span>      <span class="hljs-tag"><<span class="hljs-name">div</span>        <span class="hljs-attr">class</span>=<span class="hljs-string">"tab-item"</span>        <span class="hljs-attr">:class</span>=<span class="hljs-string">"curIndex === index? 'tab-active': 'tab-default'"</span>        <span class="hljs-attr">v-for</span>=<span class="hljs-string">"(item, index) in tabs"</span>        <span class="hljs-attr">:key</span>=<span class="hljs-string">"index"</span>        @<span class="hljs-attr">click</span>=<span class="hljs-string">"handleClickTab(item, index)"</span>      ></span>        <span class="hljs-tag"><<span class="hljs-name">span</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"tab-item-text"</span>></span>&#123;&#123; item.name &#125;&#125;<span class="hljs-tag"></<span class="hljs-name">span</span>></span>      <span class="hljs-tag"></<span class="hljs-name">div</span>></span>    <span class="hljs-tag"></<span class="hljs-name">div</span>></span>  <span class="hljs-tag"></<span class="hljs-name">div</span>></span></span></template>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这一部分为<code>console</code>上方的<code>tab</code>栏，根据传进来的<code>tabs</code>生成所有的<code>tab</code></p>
<h4 data-id="heading-28">log-container.vue</h4>
<pre><code class="hljs language-js copyable" lang="js"><template>  <span class="xml"><span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"log-container"</span>></span>    <span class="hljs-tag"><<span class="hljs-name">log-item</span>      <span class="hljs-attr">v-for</span>=<span class="hljs-string">"(log, index) in logList"</span>      <span class="hljs-attr">:key</span>=<span class="hljs-string">"index"</span>      <span class="hljs-attr">:value</span>=<span class="hljs-string">"log.value"</span>      <span class="hljs-attr">:type</span>=<span class="hljs-string">"log.type"</span>    ></span><span class="hljs-tag"></<span class="hljs-name">log-item</span>></span>  <span class="hljs-tag"></<span class="hljs-name">div</span>></span></span></template>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>该组件为<code>cosole</code>的<code>log</code>部分，根据<code>logList</code>把所有的<code>log</code>显示出来。显示的方式为<code>log-item</code>，引用于<code>log-item.vue</code></p>
<h4 data-id="heading-29">log-item.vue</h4>
<pre><code class="hljs language-js copyable" lang="js"><template>  <span class="xml"><span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"log-ltem"</span>></span>    <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"log-preview"</span> <span class="hljs-attr">v-html</span>=<span class="hljs-string">"logPreview"</span> @<span class="hljs-attr">click</span>=<span class="hljs-string">"toggleDetail"</span>></span><span class="hljs-tag"></<span class="hljs-name">div</span>></span>    <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">v-if</span>=<span class="hljs-string">"showDetail && typeof value === 'object'"</span>></span>      <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"list-item"</span> <span class="hljs-attr">v-for</span>=<span class="hljs-string">"(key, index) in value"</span> <span class="hljs-attr">:key</span>=<span class="hljs-string">"index"</span>></span>        <span class="hljs-tag"><<span class="hljs-name">Detail</span> <span class="hljs-attr">:detailValue</span>=<span class="hljs-string">"key"</span> <span class="hljs-attr">:detailIndex</span>=<span class="hljs-string">"index"</span>></span><span class="hljs-tag"></<span class="hljs-name">Detail</span>></span>      <span class="hljs-tag"></<span class="hljs-name">div</span>></span>    <span class="hljs-tag"></<span class="hljs-name">div</span>></span>  <span class="hljs-tag"></<span class="hljs-name">div</span>></span></span></template>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>每个<code>log-item</code>都按照<code>Detail</code>的方式显示了出来，</p>
<h4 data-id="heading-30">log-detail.vue</h4>
<pre><code class="hljs language-js copyable" lang="js"><template>  <span class="xml"><span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"detail-container"</span> <span class="hljs-attr">:class</span>=<span class="hljs-string">"[canFold ? 'can-unfold':'', unfold ? 'unfolded' : '']"</span> ></span>    <span class="hljs-tag"><<span class="hljs-name">div</span> @<span class="hljs-attr">click</span>=<span class="hljs-string">"unfoldDetail"</span> <span class="hljs-attr">v-html</span>=<span class="hljs-string">"displayDetailValue"</span>></span><span class="hljs-tag"></<span class="hljs-name">div</span>></span>    <span class="hljs-tag"><<span class="hljs-name">template</span> <span class="hljs-attr">v-if</span>=<span class="hljs-string">"canFold"</span>></span>      <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">v-show</span>=<span class="hljs-string">"unfold"</span> <span class="hljs-attr">v-for</span>=<span class="hljs-string">"(key, index) in detailValue"</span> <span class="hljs-attr">:key</span>=<span class="hljs-string">"index"</span>></span>        <span class="hljs-tag"><<span class="hljs-name">Detail</span> <span class="hljs-attr">:detailValue</span>=<span class="hljs-string">"key"</span> <span class="hljs-attr">:detailIndex</span>=<span class="hljs-string">"index"</span>></span><span class="hljs-tag"></<span class="hljs-name">Detail</span>></span>      <span class="hljs-tag"></<span class="hljs-name">div</span>></span>    <span class="hljs-tag"></<span class="hljs-name">template</span>></span>  <span class="hljs-tag"></<span class="hljs-name">div</span>></span></span></template>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>主要还是用来显示数据用的组件，下面的<code>script</code>部分根据不同的内容还会改变样式，这里不具体分析了。</p>
<h4 data-id="heading-31">op-command.vue</h4>
<pre><code class="hljs language-js copyable" lang="js"><template>  <span class="xml"><span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"operation"</span>></span>    <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"input-wrapper"</span>></span>      <span class="hljs-tag"><<span class="hljs-name">input</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"input"</span> <span class="hljs-attr">placeholder</span>=<span class="hljs-string">"Command……"</span> <span class="hljs-attr">v-model</span>=<span class="hljs-string">"command"</span> /></span>    <span class="hljs-tag"></<span class="hljs-name">div</span>></span>    <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"button-wrapper"</span> @<span class="hljs-attr">click</span>=<span class="hljs-string">"excuteCommand"</span>></span>      <span class="hljs-tag"><<span class="hljs-name">span</span>></span>Excute<span class="hljs-tag"></<span class="hljs-name">span</span>></span>    <span class="hljs-tag"></<span class="hljs-name">div</span>></span>  <span class="hljs-tag"></<span class="hljs-name">div</span>></span></span><<span class="hljs-regexp">/template><script>import &#123;excuteScript&#125; from './</span>js/<span class="hljs-built_in">console</span><span class="hljs-string">'export default &#123;  data()&#123;    return &#123;      command: ""    &#125;  &#125;,  methods: &#123;    excuteCommand()&#123;      if(!this.command)&#123;        return      &#125;      let ret = excuteScript(this.command)      console.log(ret)    &#125;  &#125;&#125;;</script>
</span><span class="copy-code-btn">复制代码</span></code></pre>
<p>这里是<code>console</code>中输入/执行指令的部分，每一个指令都会传给<code>excuteScript</code>并执行。</p>
<p>以上便是控制<code>console</code>UI部分的代码，剩下的部分均来自于<code>js/console</code>，为具体的逻辑实现部分</p>
<h4 data-id="heading-32">js/console.js</h4>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">export</span> <span class="hljs-keyword">const</span> LogMap = &#123;  <span class="hljs-number">0</span>: <span class="hljs-string">'All'</span>,  <span class="hljs-number">1</span>: <span class="hljs-string">'Log'</span>,  <span class="hljs-number">2</span>: <span class="hljs-string">'Info'</span>,  <span class="hljs-number">3</span>: <span class="hljs-string">'Warn'</span>,  <span class="hljs-number">4</span>: <span class="hljs-string">'Error'</span>&#125;<span class="hljs-keyword">export</span> <span class="hljs-keyword">const</span> LogEnum = &#123;  <span class="hljs-attr">ALL</span>: <span class="hljs-number">0</span>,  <span class="hljs-attr">LOG</span>: <span class="hljs-number">1</span>,  <span class="hljs-attr">INFO</span>: <span class="hljs-number">2</span>,  <span class="hljs-attr">WARN</span>: <span class="hljs-number">3</span>,  <span class="hljs-attr">ERROR</span>: <span class="hljs-number">4</span>&#125;<span class="hljs-keyword">export</span> <span class="hljs-keyword">const</span> ConsoleLogMap = &#123;  <span class="hljs-string">'log'</span>: LogEnum.LOG,  <span class="hljs-string">'info'</span>: LogEnum.INFO,  <span class="hljs-string">'warn'</span>: LogEnum.WARN,  <span class="hljs-string">'error'</span>: LogEnum.ERROR&#125;<span class="hljs-keyword">export</span> <span class="hljs-keyword">const</span> CONSOLE_METHODS = [<span class="hljs-string">"log"</span>, <span class="hljs-string">"info"</span>, <span class="hljs-string">'warn'</span>, <span class="hljs-string">'error'</span>]  &#125;)&#125;<span class="hljs-keyword">export</span> <span class="hljs-keyword">const</span> LogTabs = <span class="hljs-built_in">Object</span>.keys(LogMap).map(<span class="hljs-function"><span class="hljs-params">key</span> =></span> &#123;  <span class="hljs-keyword">return</span> &#123;    <span class="hljs-attr">type</span>: <span class="hljs-built_in">parseInt</span>(key),    <span class="hljs-attr">name</span>: LogMap[key]  &#125;&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>该文件上来先定义了几个常量，<code>LogMap</code>为<code>console</code>中展示出来的<code>tab</code>，<code>LogNum</code>和<code>ConsoleLogMap</code>为类型和对应下标之间的映射，<code>CONSOLE_METHODS</code>为<code>console</code>中不同的方法类型。<code>LogTabs</code>则是生成一个<code>tab</code>列表，生成<code>console-tab</code>时使用。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">export</span> <span class="hljs-keyword">const</span> excuteScript = <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">command</span>)</span>&#123;  <span class="hljs-keyword">let</span> ret   <span class="hljs-keyword">try</span>&#123;    ret = <span class="hljs-built_in">eval</span>.call(<span class="hljs-built_in">window</span>, <span class="hljs-string">`(<span class="hljs-subst">$&#123;command&#125;</span>)`</span>)  &#125;<span class="hljs-keyword">catch</span>(e)&#123;    ret = <span class="hljs-built_in">eval</span>.call(<span class="hljs-built_in">window</span>, command)  &#125;  <span class="hljs-keyword">return</span> ret&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这个函数很容易理解，就是将输入的指令执行。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">export</span> <span class="hljs-keyword">const</span> origConsole = &#123;&#125;<span class="hljs-keyword">export</span> <span class="hljs-keyword">const</span> noop = <span class="hljs-function">() =></span> &#123;&#125;<span class="hljs-keyword">export</span> <span class="hljs-keyword">const</span> overrideConsole = <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">callback</span>) </span>&#123;  <span class="hljs-keyword">const</span> winConsole = <span class="hljs-built_in">window</span>.console  CONSOLE_METHODS.forEach(<span class="hljs-function">(<span class="hljs-params">name</span>) =></span> &#123;    <span class="hljs-keyword">let</span> origin = (origConsole[name] = noop)    <span class="hljs-keyword">if</span> (winConsole[name]) &#123;      origin = origConsole[name] = winConsole[name].bind(winConsole)    &#125;    winConsole[name] = <span class="hljs-function">(<span class="hljs-params">...args</span>) =></span> &#123;      callback(&#123;        <span class="hljs-attr">name</span>: name,        <span class="hljs-attr">type</span>: ConsoleLogMap[name],        <span class="hljs-attr">value</span>: args      &#125;)      origin(...args)    &#125;  &#125;)&#125;<span class="hljs-keyword">export</span> <span class="hljs-keyword">const</span> restoreConsole = <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params"></span>)</span>&#123;  <span class="hljs-keyword">const</span> winConsole = <span class="hljs-built_in">window</span>.console  CONSOLE_METHODS.forEach(<span class="hljs-function">(<span class="hljs-params">name</span>) =></span> &#123;    winConsole[name] = origConsole[name]  &#125;)&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>最后一部分则是将浏览器中的<code>console</code>进行重载，在<code>console</code>执行的过程中会先调用传入的<code>callback</code>，然后才执行原函数。原函数保存在了<code>origConsole</code>中，在<code>restoreConsole</code>中便是将原始的<code>console</code>还原的过程。</p>
<p>在<code>index.js</code>中有一段:</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-title">onLoad</span>(<span class="hljs-params"></span>)</span>&#123;    <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'Load'</span>)    overrideConsole(<span class="hljs-function">(<span class="hljs-params">&#123;name, type, value&#125;</span>) =></span> &#123;      <span class="hljs-keyword">let</span> state = getGlobalData();      state.logList = state.logList || [];      state.logList.push(&#123;        <span class="hljs-attr">type</span>: type,        <span class="hljs-attr">name</span>: name,        <span class="hljs-attr">value</span>: value      &#125;);    &#125;);  &#125;,
<span class="copy-code-btn">复制代码</span></code></pre>
<p>可以看到，传给<code>overrideCOnsole</code>的<code>callback</code>便是将每个指令都存到<code>state</code>中，从而能够将其在<code>log-container</code>中展示出来。</p></div>  
</div>
            