
---
title: '前端微周刊（第9期）：VueConf US 2021：Vue安装量提升51%，Vue 3在Q2将作为Vue的默认安装版本'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/2d2794d7940a41efb04935d9be9c6b83~tplv-k3u1fbpfcp-zoom-1.image'
author: 掘金
comments: false
date: Fri, 16 Apr 2021 00:01:01 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/2d2794d7940a41efb04935d9be9c6b83~tplv-k3u1fbpfcp-zoom-1.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><blockquote>
<p>“前端微周刊”每周五更新，为前端开发者提供技术相关资讯及文章</p>
<p>微信搜索订阅“前端微志”公众号</p>
</blockquote>
<h2 data-id="heading-0">🖼 趣图</h2>
<h3 data-id="heading-1"><a href="https://macos.vercel.app/" target="_blank" rel="nofollow noopener noreferrer">在浏览器中运行macOS</a></h3>
<p><img alt="浏览器中运行macOS" class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/2d2794d7940a41efb04935d9be9c6b83~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p>推上<code>@puruvjdev</code>使用<code>React</code>（现在是<code>Preact</code>）、<code>TypeScript</code>、<code>Vite</code>（最开始使用<code>snowpack</code>）制作了这个模拟macOS的页面，没有使用任何UI库，展示效果实现的非常高。</p>
<h2 data-id="heading-2">📰 资讯</h2>
<h3 data-id="heading-3"><a href="https://docs.google.com/presentation/d/1Lu1X6dyofyWqE6lpWsdUAkHMWm9pB6A9bs187iIUin4/mobilepresent?slide=id.p" target="_blank" rel="nofollow noopener noreferrer">VueConf US 2021：尤大分享<code>State of Vuenion 2021</code></a></h3>
<p>今年的<code>VueConf US</code>大会，尤大对Vue生态在今年的一些变化，如：</p>
<ul>
<li><code>Devtools</code>安装量提升43%（110万 -> 158万）</li>
<li><code>NPM</code>安装量提升51.6%（620万 -> 940万）</li>
<li><code>Vue Router</code> 4.0 及 <code>Vuex</code> 4.0 已稳定支持<code>Vue 3</code></li>
<li>新的构建工具：<code>Vite</code> 及 新的静态网站生成工具 <code>VitePress</code></li>
<li><code><script setup></code> 及 <code><style></code> 的<code>var</code>注入</li>
<li>更好的<code>TypeScript</code>和<code>IDE</code>支持</li>
<li><code>Vue 3</code>准备抛弃<code>IE11</code></li>
<li>在2021年第二季度<code>Vue 3</code>将作为npm安装<code>Vue</code>的默认版本，即应用tag：<code>latest</code></li>
</ul>
<h3 data-id="heading-4"><a href="https://deno.com/blog/v1.9" target="_blank" rel="nofollow noopener noreferrer">Deno 1.9发布</a></h3>
<p><code>Deno</code>发布1.9版本，带来了很多新特性、性能提升和bugfixs。新特性包括：</p>
<ul>
<li>原生的<code>HTTP/2</code> web服务器</li>
<li>在<code>Rust</code>和<code>serde_v8</code>中更快的调用</li>
<li>支持<code>Blob URL</code> & 对<code>fetch</code>的提升</li>
<li><code>LSP</code>中完成<code>import</code></li>
<li>交互式权限提示</li>
<li>在<code>TLS</code>服务器中支持<code>ALPN</code></li>
<li>......</li>
</ul>
<h3 data-id="heading-5"><a href="https://developer.chrome.com/blog/new-in-chrome-90/" target="_blank" rel="nofollow noopener noreferrer">Chrome 90上新</a></h3>
<p><code>Chrome 90</code>已经发布，带来了一些新的特性，主要有：</p>
<ul>
<li><code>overflow</code>新增一个特性：<code>clip</code>。该属性与<code>hidden</code>的效果很像，都是将超过边界的部分隐藏，且不能滚动。与<code>hidden</code>不同的是，<code>clip</code>也不能通过程序（如<code>el.scrollTop = 10</code>）的方式滚动。同时还有一个新属性<code>overflow-clip-margin</code>可以拓展标签剪切的范围；
<pre><code class="hljs language-css copyable" lang="css"><span class="hljs-selector-class">.overflow-clip</span> &#123;
  <span class="hljs-attribute">overflow</span>: clip;
  <span class="hljs-attribute">overflow</span>-<span class="hljs-attribute">clip</span>-<span class="hljs-attribute">margin</span>: <span class="hljs-number">25px</span>;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
<li><code>Feature Policy</code>重命名为<code>Permissions Policy</code>。<code>Feature Policy API</code>是从<code>Chrome 74</code>引入的功能，它可以让你有选择性地<code>启用</code>、<code>禁用</code>和<code>修改</code>特定的API和浏览器特性的行为，感兴趣的可以从<a href="https://developer.mozilla.org/zh-CN/docs/Web/HTTP/Headers/Feature-Policy" target="_blank" rel="nofollow noopener noreferrer">Feature-Policy的MDN文档</a>中了解详细的内容。如果你想在你的网站上使用这个特性，戳👉 <a href="https://developers.google.com/web/updates/2018/06/feature-policy" target="_blank" rel="nofollow noopener noreferrer">介绍Feature Policy</a>。</li>
<li><code>Declarative Shadow DOM</code>的支持。<code>Shadow DOM</code>是<code>Web Component</code>标准的一部分，它提供一种隔离<code>DOM</code>子树的<code>CSS</code>样式等能力。在此之前，要使用<code>Shadow DOM</code>，需要使用<code>JavaScript</code>构建一个<code>shadow root</code>。
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">const</span> host = <span class="hljs-built_in">document</span>.getElementById(<span class="hljs-string">'host'</span>);
<span class="hljs-keyword">const</span> opts = &#123;<span class="hljs-attr">mode</span>: <span class="hljs-string">'open'</span>&#125;;
<span class="hljs-keyword">const</span> shadowRoot = host.attachShadow(opts);
<span class="hljs-keyword">const</span> html = <span class="hljs-string">'<h1>Hello Shadow DOM</h1>'</span>;
shadowRoot.innerHTML = html;
<span class="copy-code-btn">复制代码</span></code></pre>
但是这种只能在客户端渲染时有效，不适用于服务端渲染。从<code>Chrome 90</code>的<code>Declarative Shadow DOM</code>，可以只使用<code>HTML</code>即可创建<code>shadow root</code>。
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">host-element</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">template</span> <span class="hljs-attr">shadowroot</span>=<span class="hljs-string">"open"</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">slot</span>></span><span class="hljs-tag"></<span class="hljs-name">slot</span>></span>
  <span class="hljs-tag"></<span class="hljs-name">template</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">h2</span>></span>Light content<span class="hljs-tag"></<span class="hljs-name">h2</span>></span>
<span class="hljs-tag"></<span class="hljs-name">host-element</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
</ul>
<h3 data-id="heading-6"><a href="https://blog.tailwindcss.com/tailwind-ui-now-with-react-and-vue-support" target="_blank" rel="nofollow noopener noreferrer">Tailwind UI现已支持React和Vue</a></h3>
<p><code>Tailwind UI</code>是基于<code>Tailwind CSS</code>的一套组件库，并提供超过400个经过设计的响应式示例网页，可以直接将这些示例页面的内容丢到你的<code>Tailwind CSS</code>项目中去，改造成本很低。现在这些组件已经支持<code>React</code>和<code>Vue 3</code>，使得在这些框架的项目中使用<code>Tailwind UI</code>更加地简单。</p>
<p>从<a href="https://tailwindui.com/" target="_blank" rel="nofollow noopener noreferrer"><code>Tailwind UI</code>官网</a>上我们可以看出，它提供了付费查看更多示例模板的服务，从中我们可以学习到一种技术工具和框架的一种商业化途径。如果你也有比较好的开源工具或框架，也可以参考这种方式，提供上层封装的API、组件或功能，达到商业化变现的目的。</p>
<h2 data-id="heading-7">📖 文章</h2>
<h3 data-id="heading-8"><a href="https://dev.to/dabit3/the-complete-guide-to-full-stack-ethereum-development-3j13" target="_blank" rel="nofollow noopener noreferrer">The Complete Guide to Full Stack Ethereum Development</a></h3>
<p>本文较详细地介绍了如何做全栈的以太坊开发，涉及到的内容还是比较全面的。使用的主要技术架构是：</p>
<ul>
<li>前端框架 - React</li>
<li>以太坊开发环境 - <a href="https://hardhat.org/" target="_blank" rel="nofollow noopener noreferrer">Hardhat</a></li>
<li>以太坊Web端类库 - <a href="https://docs.ethers.io/v5/" target="_blank" rel="nofollow noopener noreferrer">Ethers.js</a></li>
<li>API层 - <a href="https://thegraph.com/" target="_blank" rel="nofollow noopener noreferrer">Graph Protocal</a></li>
</ul>
<p>本文是一个端到端的指南，讲述如何使用最新的资源、类库和工具来构建一个全栈以太坊应用，大致包括：</p>
<ul>
<li>如何创建、部署和测试以太坊智能合约到本地、测试和主网</li>
<li>如何在本地、测试和生产环境/网络之间切换</li>
<li>如何使用一个如React、Vue、Svelte或Angular等的环境，与合约进行连接和交互</li>
</ul>
<h3 data-id="heading-9"><a href="https://blog.sentry.io/2021/04/12/slow-and-steady-converting-sentrys-entire-frontend-to-typescript" target="_blank" rel="nofollow noopener noreferrer">Slow and Steady: Converting Sentry’s Entire Frontend to TypeScript</a></h3>
<p><img alt="转换成TypeScript" class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/b9458b4dd2f143a2ace1e747672d0abf~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p>越来越多的前端开发者开始使用<code>TypeScript</code>作为主要开发语言，很多之前对<code>TypeScript</code>比较抗拒的开发者身上也在上演“真香定律”。</p>
<p><code>Sentry</code>网站的前端团队，将自身网站由<code>JavaScript</code>100%迁移到<code>TypeScript</code>的过程做了一次详细的介绍，分享其中的进度节奏、技术、挑战和最终学到的东西。</p>
<p>整体的节奏是<code>缓慢且稳定</code>的，整个过程有超过12个人的团队，1100个文件，95000行代码。</p>
<p>整个迁移的策略大致分为三个阶段：</p>
<ul>
<li><strong>教育培训</strong>。这个阶段，需要让团队内所有的开发者了解<code>TypeScript</code>即将到来，并提供有用的资源帮助他们“上车”；</li>
<li><strong>新代码使用TypeScript</strong>。这个阶段，需要将开发模式转为<code>TypeScript</code>；</li>
<li><strong>转换</strong>。这个阶段，所有的新工作都转为<code>TypeScript</code>。</li>
</ul>
<p>如果你手边也有老项目想要迁移到<code>TypeScript</code>，可以详细地阅读原文，文中介绍的阶段性任务拆分和分析工具的使用，会有所帮助。</p>
<h2 data-id="heading-10">🛠 工具、插件</h2>
<h3 data-id="heading-11"><a href="https://github.com/preactjs/wmr" target="_blank" rel="nofollow noopener noreferrer">WMR</a></h3>
<p><code>WMR</code>是一个轻量的现代web应用开发的一站式开发工具。整个npm包的安装大小为2MB，且没有任何依赖。</p>
<p>现代web应用开发所需要的特性，从开发环境到生产环境，包括且不限于：</p>
<ul>
<li>🔨   No entry points or pages to configure - just HTML files with <code><script type=module></code></li>
<li>🦦   Safely import "packages" from npm without installation</li>
<li>📦   Smart bundling and caching for npm dependencies</li>
<li>↻   Hot reloading for modules, Preact components and CSS</li>
<li>⚡️   Lightning-fast JSX support that you can debug in the browser</li>
<li>💄   Import CSS files and CSS Modules (*.module.css)</li>
<li>🔩   Out-of-the-box support for TypeScript</li>
<li>📂   Static file serving with hot reloading of CSS and images</li>
<li>🗜   Highly optimized Rollup-based production output (wmr build)</li>
<li>📑   Crawls and pre-renders your app's pages to static HTML at build time</li>
<li>🏎   Built-in HTTP2 in dev and prod (wmr serve --http2)</li>
<li>🔧   Supports Rollup plugins, even in development where Rollup isn't used</li>
</ul>
<h3 data-id="heading-12"><a href="https://github.com/pmndrs/react-spring" target="_blank" rel="nofollow noopener noreferrer">React弹簧物理动画库：react-spring</a></h3>
<p><img alt="类似现实生活中的弹簧动效" class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/22950614c58f4fbc85d864b443a56c77~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p><code>react-spring</code>是一个基于<strong>弹簧物理</strong>的动画库，它可以满足大部分UI相关动画的需求，且提供足够灵活的工具将你的创意想法变成现实。</p>
<h3 data-id="heading-13"><a href="https://draculatheme.com/ui" target="_blank" rel="nofollow noopener noreferrer">Dracula UI</a></h3>
<p><img alt="Dracula UI暗色系组件" class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/c2712c00810b4293b86efac03ba2c580~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p><code>Dracula</code>是一个配色主题，主打的是暗色系的主题配色，支持各种常用的IDE。这一套UI组件，正是基于原有的配色体系，提供一套暗色优先的前端组件及响应的设计稿模板。</p>
<p>不得不说，确实很漂亮。</p>
<h3 data-id="heading-14"><a href="https://www.drawkit.io/" target="_blank" rel="nofollow noopener noreferrer">Drawit</a></h3>
<p><img alt="不带插图的网页 VS 带插图的网页" class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/88430180e314468db46cbda452cbbfb3~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p>该网站提供了大量手绘的矢量插图和图标资源，大部分是免费的。</p>
<p>近几年，插图已经成为大多网站的标配，手绘的插图可以给网页带来视觉上的新的体验，为网页枯燥的文案描述添加更加形象的描述，增色不少。</p>
<h2 data-id="heading-15">🥅 代码片段</h2>
<h3 data-id="heading-16">如何在<code>Node.js</code>中使用<code>ES6</code>中的<code>import</code>语法</h3>
<p>要在<code>Node.js</code>中使用<code>import</code>语法，有多种方式。下面介绍两种简单的方法：</p>
<ol>
<li>在<code>package.json</code>中添加字段<code>"type": "module"</code></li>
</ol>
<p>这是一种很简单的方法，只需要添加一个类型标识：</p>
<pre><code class="hljs language-json copyable" lang="json">&#123;
  <span class="hljs-attr">"type"</span>: <span class="hljs-string">"module"</span>
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这种方法，有一个前置条件，需要<code>Node.js</code>的版本至少在<code>14.x.x</code>以上。
2. 使用<code>Babel</code>做语法转换
如果你想在<code>Node.js</code>版本小于14的环境下使用<code>import</code>，可以借助于<code>Babel</code>的预发转换能力，将<code>import</code>语法转换成<code>CommonJS</code>的语法。
安装相关依赖：</p>
<pre><code class="hljs language-bash copyable" lang="bash">npm i -D @babel/core @babel/preset-env @babel/node
<span class="copy-code-btn">复制代码</span></code></pre>
<p>在项目根目录下创建<code>babel.config.json</code>的配置文件：</p>
<pre><code class="hljs language-json copyable" lang="json">&#123;
  <span class="hljs-attr">"presets"</span>: [<span class="hljs-string">"@babel/preset-env"</span>]
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>最后使用<code>nodemon</code>来启动服务：</p>
<pre><code class="hljs language-json copyable" lang="json">&#123;
  <span class="hljs-attr">"scripts"</span>: &#123;
    <span class="hljs-attr">"dev"</span>: <span class="hljs-string">"nodemon --exec babel-node server.js"</span>
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-17">使用<code>useReducer</code>实现状态切换</h3>
<p>业务开发中，经常需要来回切换两种状态，下面介绍一种使用<code>React.useReducer</code>创建一个状态切换机的方法，示例代码如下：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">const</span> useToggle = <span class="hljs-function">(<span class="hljs-params">initialValue = <span class="hljs-literal">false</span></span>) =></span> &#123;
  <span class="hljs-keyword">return</span> React.useReducer(
    <span class="hljs-function">(<span class="hljs-params">previousValue</span>) =></span> !previousValue&#125;,
    initialValue
  )
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>业务代码中即可使用<code>useToggle</code>使用这个状态切换机：</p>
<pre><code class="hljs language-jsx copyable" lang="jsx"><span class="hljs-keyword">const</span> [value, toggleValue] = useToggle();

<span class="xml"><span class="hljs-tag"><<span class="hljs-name">button</span> <span class="hljs-attr">onClick</span>=<span class="hljs-string">&#123;toggleValue&#125;</span>></span>
  Click me
<span class="hljs-tag"></<span class="hljs-name">button</span>></span></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-18">伪类 <code>:out-of-range</code> 和 <code>:in-range</code></h3>
<p><img alt="输入框使用该伪类的效果" class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/c4aed0911f014db6a52fd3d2a731f7f8~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p>可以对输入框设置范围的伪类，设置一些特殊的样式。如：</p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">input</span> <span class="hljs-attr">type</span>=<span class="hljs-string">"number"</span> <span class="hljs-attr">min</span>=<span class="hljs-string">10</span> <span class="hljs-attr">max</span>=<span class="hljs-string">15</span> /></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>样式：</p>
<pre><code class="hljs language-css copyable" lang="css"><span class="hljs-selector-pseudo">:in-range</span> &#123;
  <span class="hljs-attribute">background</span>: green;
&#125;

<span class="hljs-selector-pseudo">:out-of-range</span> &#123;
  <span class="hljs-attribute">background</span>: red;
&#125;

<span class="hljs-selector-tag">input</span> &#123;
  <span class="hljs-attribute">font-size</span>: <span class="hljs-number">15rem</span>;
  <span class="hljs-attribute">color</span>: white;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<blockquote>
<p>文章首发于微信公众号：前端微志。</p>
<p>想要第一时间收到文章推送，更有前端前瞻性技术分享，请微信搜索关注“前端微志”，</p>
</blockquote></div> <div class="image-viewer-box" data-v-78c9b824><!----></div>  
</div>
            