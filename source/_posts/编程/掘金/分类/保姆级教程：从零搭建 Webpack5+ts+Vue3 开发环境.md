
---
title: '保姆级教程：从零搭建 Webpack5+ts+Vue3 开发环境'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=5324'
author: 掘金
comments: false
date: Tue, 29 Jun 2021 23:03:06 GMT
thumbnail: 'https://picsum.photos/400/300?random=5324'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>本文已参与好文召集令活动，点击查看：<a href="https://juejin.cn/post/6978685539985653767" target="_blank">后端、大前端双赛道投稿，2万元奖池等你挑战！</a></p>
<h1 data-id="heading-0">前言</h1>
<p>Hello，大家好，我是和光不同尘，一个你肯定还没有听说过的新人写手，大家可以叫我和光</p>
<p>最近我又在研究如何用 webpack 搭建 vue+ts 的前端项目了</p>
<p>什么，你说社区有太多类似的文章，你已经看麻了</p>
<p>我也很无奈啊，高深的东西我也整不明白，只能写点入门级的混个脸熟了...</p>
<p>什么，你说你用 vite 用 vue-cli</p>
<p>说实话我也喜欢用，还有 umi，都是很棒的工具，简洁优雅，省时省力，我从小用到大...</p>
<p>但总有人觉得自己亲手搭建的项目更强，更靠谱</p>
<p>虽然我没有这样的自信，大概这就是我这个菜鸡和人家高级前端的差距吧</p>
<p>废话不多说，我们这就操练起来</p>
<p>代码我放在了这个仓库：<a href="https://github.com/yyeexin/webpack5-ts-vue" target="_blank" rel="nofollow noopener noreferrer">webpack5-ts-vue</a></p>
<p>有需要的话可以自行取用</p>
<h1 data-id="heading-1">一、基础打包</h1>
<p>第一部分先带大家回忆一下 <code>webpack</code> 的基础打包流程，我知道这些大家肯定都会的，我只是带大家回忆一下</p>
<h2 data-id="heading-2">1. 新建项目</h2>
<p>找个地方新建名为 <code>webpack5-ts-vue</code> 的文件夹，打开终端进入此目录，安装 <code>webpack</code> 和 <code>ts</code> 相关依赖，初始化项目：</p>
<pre><code class="hljs language-cmd copyable" lang="cmd"><span class="hljs-built_in">mkdir</span> webpack5-ts-vue && <span class="hljs-built_in">cd</span> webpack5-ts-vue

npm install typescript webpack webpack-cli -D

git init
npm init -y
npx tsc --init
<span class="copy-code-btn">复制代码</span></code></pre>
<p>新建 <code>.gitignore</code> 文件，将 <code>node_modules</code> 文件夹添加进去，避免 <code>git</code> 必要的文件追踪</p>
<h2 data-id="heading-3">2. 新建入口文件</h2>
<p>在项目根目录下新建 <code>src</code> 文件夹，新建 <code>index.ts</code> 入口文件并添加内容：</p>
<pre><code class="hljs language-cmd copyable" lang="cmd"><span class="hljs-built_in">mkdir</span> src && <span class="hljs-built_in">cd</span> src && touch index.ts
<span class="hljs-built_in">echo</span> "const myName: string = \"和光不同尘\";" > index.ts
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-4">3. 运行打包命令</h2>
<p>在 <code>package.json</code> 文件中添加打包脚本：</p>
<pre><code class="hljs language-json copyable" lang="json">&#123;
  <span class="hljs-attr">"scripts"</span>: &#123;
    <span class="hljs-attr">"build"</span>: <span class="hljs-string">"webpack"</span>
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>在命令行中运行 <code>npm run build</code> ，发现报错了。阅读报错信息可知，<code>webpack</code> 没有找到正确的入口文件，并且告诉我们 <code>webpack</code> 查找入口文件的默认顺序是：</p>
<pre><code class="copyable">src.js
src.json
src.wasm
src/index.js
src/index.json
src/index.wasm
<span class="copy-code-btn">复制代码</span></code></pre>
<p>我们的 <code>index.ts</code> 文件并不在此列</p>
<h2 data-id="heading-5">4. 添加 ts 解析工具</h2>
<p><code>ts</code> 文件并不是 <code>webpack</code> 能直接解析的，所以我们需要使用 <code>ts-loader</code> 来专门处理</p>
<p>安装相关依赖：</p>
<pre><code class="hljs language-cmd copyable" lang="cmd">npm i ts-loader -D
<span class="copy-code-btn">复制代码</span></code></pre>
<p>在项目根目录新建 <code>webpack</code> 配置文件 <code>webpack.config.js</code>，写入如下内容：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-built_in">module</span>.exports = &#123;
  <span class="hljs-attr">entry</span>: <span class="hljs-string">"./src/index.ts"</span>,
  <span class="hljs-attr">module</span>: &#123;
    <span class="hljs-attr">rules</span>: [
      &#123;
        <span class="hljs-attr">test</span>: <span class="hljs-regexp">/\.ts$/</span>,
        exclude: <span class="hljs-regexp">/node_modules/</span>,
        use: <span class="hljs-string">"ts-loader"</span>,
      &#125;,
    ],
  &#125;,
&#125;;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>再次运行打包命令，丝般顺滑，终端没有报错</p>
<h2 data-id="heading-6">5. 修改配置文件</h2>
<p>在生成的 <code>dist</code> 目录中点开 <code>main.js</code> 文件，发现其中空空如也</p>
<p>这是因为 <code>webpack</code> 默认以 <code>production</code> 模式运行，会使用 <code>tree-shaking</code> 功能对文件内容进行优化。而我们在 <code>index.ts</code> 中只有一条声明语句，且并没有使用这个声明的变量，<code>webpack</code> 的树摇功能自动删去了这行无用的声明语句，结果就是打包的文件是空文件</p>
<p>我们可以手动声明以 <code>development</code> 模式运行：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-built_in">module</span>.exports = &#123;
  <span class="hljs-attr">mode</span>: <span class="hljs-string">"development"</span>,
&#125;;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>再次运行打包命令，现在生成的文件就有内容了</p>
<h2 data-id="heading-7">6. 生成 html 入口</h2>
<p>安装 <code>html-webpack-plugin</code> 插件处理 <code>index.html</code> 文件，此插件的功能是根据提供的模板文件，自动生成正确的项目入口文件，并把 <code>webpack</code> 打包的 <code>js</code> 文件自动插入其中</p>
<pre><code class="hljs language-cmd copyable" lang="cmd">npm i html-webpack-plugin -D
<span class="copy-code-btn">复制代码</span></code></pre>
<p>在项目根目录新建项目入口 <code>index.html</code> 模板文件：</p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-meta"><!DOCTYPE <span class="hljs-meta-keyword">html</span>></span>
<span class="hljs-tag"><<span class="hljs-name">html</span> <span class="hljs-attr">lang</span>=<span class="hljs-string">"en"</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">head</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">meta</span> <span class="hljs-attr">charset</span>=<span class="hljs-string">"UTF-8"</span> /></span>
    <span class="hljs-tag"><<span class="hljs-name">meta</span> <span class="hljs-attr">http-equiv</span>=<span class="hljs-string">"X-UA-Compatible"</span> <span class="hljs-attr">content</span>=<span class="hljs-string">"IE=edge"</span> /></span>
    <span class="hljs-tag"><<span class="hljs-name">meta</span> <span class="hljs-attr">name</span>=<span class="hljs-string">"viewport"</span> <span class="hljs-attr">content</span>=<span class="hljs-string">"width=device-width, initial-scale=1.0"</span> /></span>
    <span class="hljs-tag"><<span class="hljs-name">title</span>></span>Document<span class="hljs-tag"></<span class="hljs-name">title</span>></span>
  <span class="hljs-tag"></<span class="hljs-name">head</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">body</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">id</span>=<span class="hljs-string">"app"</span>></span><span class="hljs-tag"></<span class="hljs-name">div</span>></span>
  <span class="hljs-tag"></<span class="hljs-name">body</span>></span>
<span class="hljs-tag"></<span class="hljs-name">html</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>修改配置文件 <code>webpack.config.js</code>：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> HtmlWebpackPlugin = <span class="hljs-built_in">require</span>(<span class="hljs-string">"html-webpack-plugin"</span>);

<span class="hljs-built_in">module</span>.exports = &#123;
  <span class="hljs-comment">// ...</span>
  <span class="hljs-attr">plugins</span>: [
    <span class="hljs-keyword">new</span> HtmlWebpackPlugin(&#123;
      <span class="hljs-attr">title</span>: <span class="hljs-string">"webpack5-ts-vue"</span>,
      <span class="hljs-attr">template</span>: <span class="hljs-string">"./index.html"</span>,
    &#125;),
  ],
  <span class="hljs-comment">// ...</span>
&#125;;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>注意，只在配置文件中设置 <code>title</code> 并不起作用，<code>index.html</code> 文件需要做相应的修改：</p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">head</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">title</span>></span><%= htmlWebpackPlugin.options.title %><span class="hljs-tag"></<span class="hljs-name">title</span>></span>
<span class="hljs-tag"></<span class="hljs-name">head</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这其实是 <code>EJS</code> 模板语法，其中的变量会在打包过程中被某些值替换</p>
<h2 data-id="heading-8">7. 运行项目</h2>
<p>为了能更好的看到效果，我们将 <code>index.ts</code> 文件的内容修改的复杂些：</p>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-keyword">const</span> myName: <span class="hljs-built_in">string</span> = <span class="hljs-string">"和光不同尘"</span>;
<span class="hljs-built_in">console</span>.log(myName);

[<span class="hljs-number">1</span>, <span class="hljs-number">2</span>, <span class="hljs-number">3</span>].forEach(<span class="hljs-function">(<span class="hljs-params">item</span>) =></span> &#123;
  <span class="hljs-built_in">console</span>.log(item);
&#125;);

<span class="hljs-keyword">const</span> isInclude = [<span class="hljs-string">"a"</span>, <span class="hljs-string">"b"</span>, <span class="hljs-string">"c"</span>].includes(<span class="hljs-string">"a"</span>);
<span class="hljs-built_in">console</span>.log(isInclude);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>再次运行打包命令，<code>dist</code> 目录下生成了 <code>index.html</code> 和 <code>main.js</code> 两个文件，使用 <code>VSCode</code> 的 <code>live server</code> 插件或其他能够在本地开启静态资源服务器的工具打开 <code>index.html</code> 文件，打开控制台，可以看到在控制台成功输入了预期的结果：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-string">"和光不同尘"</span>;
<span class="hljs-number">1</span>;
<span class="hljs-number">2</span>;
<span class="hljs-number">3</span>;
<span class="hljs-literal">true</span>;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这样基础的打包流程就完成了，现在的项目结构如下：</p>
<pre><code class="copyable">webpack5-ts-vue
├── src
│   └── index.ts
├── index.html
├── package-lock.json
├── package.json
├── webpack.config.js
└── tsconfig.json
<span class="copy-code-btn">复制代码</span></code></pre>
<h1 data-id="heading-9">二、开发服务器</h1>
<p>为了能有更好的开发体验，我们引入 <code>webpack-dev-server</code> ，启动开发服务器</p>
<pre><code class="hljs language-cmd copyable" lang="cmd">npm i webpack-dev-server -D
<span class="copy-code-btn">复制代码</span></code></pre>
<p>在 <code>webpack.config.js</code> 添加配置：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-built_in">module</span>.exports = &#123;
  <span class="hljs-comment">// ...</span>
  <span class="hljs-comment">// webpack升级到5.0后，target默认值值会根据package.json中的browserslist改变，导致devServer的自动更新失效</span>
  <span class="hljs-comment">// 所以 development 环境下直接配置成 web</span>
  <span class="hljs-attr">target</span>: <span class="hljs-string">"web"</span>,
  <span class="hljs-attr">devServer</span>: &#123;
    <span class="hljs-attr">hot</span>: <span class="hljs-literal">true</span>, <span class="hljs-comment">// 启用热模块替换</span>
    <span class="hljs-attr">open</span>: <span class="hljs-literal">true</span>, <span class="hljs-comment">// 打开默认浏览器</span>
  &#125;,
  <span class="hljs-comment">// ...</span>
&#125;;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>在 <code>package.json</code> 中添加脚本：</p>
<pre><code class="hljs language-json copyable" lang="json">&#123;
  <span class="hljs-attr">"scripts"</span>: &#123;
    <span class="hljs-attr">"serve"</span>: <span class="hljs-string">"webpack serve"</span>
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这样我们运行 <code>npm run serve</code> 开发命令后，默认浏览器会自动打开，当我们修改了文件的内容时，浏览器也会自动刷新</p>
<p>这里我们详细解释一下在实际开发中非常常用的 <code>proxy</code> 配置项，它的作用是设置代理，解决开发环境中的跨域问题。其原理是将我们本地发出的请求通过一个中间代理服务器，转发到真正的接口服务器，服务器之间的通信是没有跨域问题的</p>
<p><code>proxy</code> 常用配置项如下：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-built_in">module</span>.exports = &#123;
  <span class="hljs-comment">// ...</span>
  <span class="hljs-attr">devServer</span>: &#123;
    <span class="hljs-attr">proxy</span>: &#123;
      <span class="hljs-string">"/api"</span>: &#123;
        <span class="hljs-comment">// 需要代理到的真实目标服务器，如/api/user会被代理到https://www.juejin.cn/api/user</span>
        <span class="hljs-attr">target</span>: <span class="hljs-string">"https://www.juejin.cn"</span>,
        <span class="hljs-comment">// 是否更改代理后请求的headers中host地址，某些安全级别较高的服务器会对此做校验</span>
        <span class="hljs-attr">changeOrigin</span>: <span class="hljs-literal">true</span>,
        <span class="hljs-comment">// 默认情况下不接受将请求转发到https的api服务器上，如果希望支持，可以设置为false</span>
        <span class="hljs-attr">secure</span>: <span class="hljs-literal">false</span>,
        <span class="hljs-comment">// 默认情况下/api也会写入到请求url中，通过这个配置可以将其删除</span>
        <span class="hljs-attr">pathRewrite</span>: &#123;
          <span class="hljs-string">"^/api"</span>: <span class="hljs-string">"/"</span>,
        &#125;,
      &#125;,
    &#125;,
  &#125;,
  <span class="hljs-comment">// ...</span>
&#125;;
<span class="copy-code-btn">复制代码</span></code></pre>
<h1 data-id="heading-10">三、配置文件拆分</h1>
<p>为了更能体现我们企业级项目开发环境搭建的目标，现在来对 <code>webpack</code> 的配置文件进行环境拆分</p>
<p>删除原来的 <code>webpack.config.js</code> 文件，新建 <code>config</code> 文件夹，新建 <code>webpack.base.js</code> 、 <code>webpack.dev.js</code> 和 <code>webpack.prod.js</code> 三个文件，并安装合并配置文件需要使用的依赖：</p>
<pre><code class="hljs language-cmd copyable" lang="cmd">npm i webpack-merge -D
<span class="copy-code-btn">复制代码</span></code></pre>
<p>在三个文件中分别写入以下内容：</p>
<h2 data-id="heading-11">1. 基础配置</h2>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> HtmlWebpackPlugin = <span class="hljs-built_in">require</span>(<span class="hljs-string">"html-webpack-plugin"</span>);

<span class="hljs-built_in">module</span>.exports = &#123;
  <span class="hljs-attr">entry</span>: <span class="hljs-string">"./src/index.ts"</span>,
  <span class="hljs-attr">module</span>: &#123;
    <span class="hljs-attr">rules</span>: [
      &#123;
        <span class="hljs-attr">test</span>: <span class="hljs-regexp">/\.ts$/</span>,
        exclude: <span class="hljs-regexp">/node_modules/</span>,
        use: <span class="hljs-string">"ts-loader"</span>,
      &#125;,
    ],
  &#125;,
  <span class="hljs-attr">plugins</span>: [
    <span class="hljs-keyword">new</span> HtmlWebpackPlugin(&#123;
      <span class="hljs-attr">title</span>: <span class="hljs-string">"webpack5-ts-vue"</span>,
      <span class="hljs-attr">template</span>: <span class="hljs-string">"./index.html"</span>,
    &#125;),
  ],
&#125;;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-12">2. 开发配置</h2>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> &#123; merge &#125; = <span class="hljs-built_in">require</span>(<span class="hljs-string">"webpack-merge"</span>);

<span class="hljs-keyword">const</span> baseConfig = <span class="hljs-built_in">require</span>(<span class="hljs-string">"./webpack.base.js"</span>);

<span class="hljs-built_in">module</span>.exports = merge(baseConfig, &#123;
  <span class="hljs-attr">mode</span>: <span class="hljs-string">"development"</span>,
  <span class="hljs-attr">target</span>: <span class="hljs-string">"web"</span>,
  <span class="hljs-attr">devServer</span>: &#123;
    <span class="hljs-attr">hot</span>: <span class="hljs-literal">true</span>,
    <span class="hljs-attr">open</span>: <span class="hljs-literal">true</span>,
  &#125;,
&#125;);
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-13">3. 生产配置</h2>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> &#123; merge &#125; = <span class="hljs-built_in">require</span>(<span class="hljs-string">"webpack-merge"</span>);

<span class="hljs-keyword">const</span> baseConfig = <span class="hljs-built_in">require</span>(<span class="hljs-string">"./webpack.base.js"</span>);

<span class="hljs-built_in">module</span>.exports = merge(baseConfig, &#123;
  <span class="hljs-attr">mode</span>: <span class="hljs-string">"production"</span>,
&#125;);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>修改 <code>npm</code> 脚本：</p>
<pre><code class="hljs language-json copyable" lang="json">&#123;
  <span class="hljs-attr">"scripts"</span>: &#123;
    <span class="hljs-attr">"build"</span>: <span class="hljs-string">"webpack --config ./config/webpack.prod.js"</span>,
    <span class="hljs-attr">"serve"</span>: <span class="hljs-string">"webpack serve --config ./config/webpack.dev.js"</span>
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这样就简单地对配置文件进行了环境上的区分，后续的各种工作只不过是根据不同的需求在不同的配置文件中添加配置而已，当然实际项目中的配置文件要比案例中复杂的多</p>
<p>需要注意的是，配置文件中的路径并没有因为将配置文件放进更深一层的 <code>config</code> 文件夹而修改，这是因在 <code>webpack</code> 配置中有一个 <code>context</code> 属性，该属性用来解析入口 <code>entry point</code> 和加载器 <code>loader</code> ，其默认值是 <code>webpack</code> 的启动目录，一般就是项目的根目录</p>
<h1 data-id="heading-14">四、打包各类文件</h1>
<p><code>webpack</code> 是一个 <code>js</code> 文件打包工具，其他类型的文件一般都需要通过额外的加载器 <code>loader</code> 来实现解析和打包，下面我们具体来看</p>
<h2 data-id="heading-15">1. vue</h2>
<p>安装 <code>vue3</code> ：</p>
<pre><code class="hljs language-cmd copyable" lang="cmd">npm i vue@next -S
<span class="copy-code-btn">复制代码</span></code></pre>
<p>安装 <code>vue-loader</code> ：</p>
<pre><code class="hljs language-cmd copyable" lang="cmd">npm install vue-loader -D
<span class="copy-code-btn">复制代码</span></code></pre>
<p>在 <code>src</code> 文件夹下新建 <code>App.vue</code> 文件：</p>
<pre><code class="hljs language-ts copyable" lang="ts"><template>
  <span class="xml"><span class="hljs-tag"><<span class="hljs-name">h1</span>></span>&#123;&#123; name &#125;&#125;<span class="hljs-tag"></<span class="hljs-name">h1</span>></span></span>
</template>
<span class="xml"><span class="hljs-tag"><<span class="hljs-name">script</span> <span class="hljs-attr">lang</span>=<span class="hljs-string">"ts"</span>></span><span class="javascript">
<span class="hljs-keyword">import</span> &#123; defineComponent &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">"vue"</span>;
<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> defineComponent(&#123;
  <span class="hljs-function"><span class="hljs-title">setup</span>(<span class="hljs-params"></span>)</span> &#123;
    <span class="hljs-keyword">const</span> name = <span class="hljs-string">"和光不同尘"</span>;
    <span class="hljs-keyword">return</span> &#123;
      name,
    &#125;;
  &#125;,
&#125;);
</span><span class="hljs-tag"></<span class="hljs-name">script</span>></span></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>修改 <code>index.ts</code> ：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">import</span> &#123; createApp &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">"vue"</span>;
<span class="hljs-keyword">import</span> App <span class="hljs-keyword">from</span> <span class="hljs-string">"./App.vue"</span>;

createApp(App).mount(<span class="hljs-string">"#app"</span>);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>修改 <code>webpack.base.js</code> ：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-built_in">module</span>.exports = &#123;
  <span class="hljs-attr">module</span>: &#123;
    <span class="hljs-attr">rules</span>: [
      &#123;
        <span class="hljs-attr">test</span>: <span class="hljs-regexp">/\.vue$/</span>,
        use: <span class="hljs-string">"vue-loader"</span>,
      &#125;,
    ],
  &#125;,
&#125;;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>现在对代码进行打包依然会报错，根据控制台的报错信息得知对 <code>.vue</code> 文件的解析还需要 <code>@vue/compoiler-sfc</code> 这个包：</p>
<pre><code class="hljs language-cmd copyable" lang="cmd">npm i @vue/compiler-sfc -D
<span class="copy-code-btn">复制代码</span></code></pre>
<p>另外，还需要配置对应的 <code>vue</code> 插件，它的作用是将你定义过的 <code>js</code>、 <code>css</code> 等规则应用到 <code>.vue</code> 文件中去：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> &#123; VueLoaderPlugin &#125; = <span class="hljs-built_in">require</span>(<span class="hljs-string">"vue-loader"</span>);

<span class="hljs-built_in">module</span>.exports = &#123;
  <span class="hljs-attr">plugins</span>: [<span class="hljs-keyword">new</span> VueLoaderPlugin()],
&#125;;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这样运行开发命令就已经不报错了，但是浏览器内还是一片空白，并且控制台还报错</p>
<p>这是因为单文件组件被 <code>vue-loader</code> 解析成了三个部分，<code>script</code> 部分最终交由 <code>ts-loader</code> 来处理，但是 <code>tsc</code> 并不知道如何处理 <code>.vue</code> 结尾的文件</p>
<p>为了解决这个问题，需要给 <code>ts-loader</code> 添加一个配置项：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-built_in">module</span>.exports = &#123;
  <span class="hljs-comment">// ...</span>
  <span class="hljs-attr">module</span>: &#123;
    <span class="hljs-attr">rules</span>: [
      &#123;
        <span class="hljs-attr">test</span>: <span class="hljs-regexp">/\.ts$/</span>,
        loader: <span class="hljs-string">"ts-loader"</span>,
        <span class="hljs-attr">exclude</span>: <span class="hljs-regexp">/node_modules/</span>,
        options: &#123;
          <span class="hljs-attr">appendTsSuffixTo</span>: [<span class="hljs-regexp">/\.vue$/</span>],
        &#125;,
      &#125;,
    ],
  &#125;,
  <span class="hljs-comment">// ...</span>
&#125;;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这样 <code>.vue</code> 文件就能完美解析了</p>
<p>注意，为了解决 <code>ts</code> 对 <code>.vue</code> 文件的报错问题，需要在 <code>src</code> 目录下添加一个 <code>shims-vue.d.ts</code> 类型申明文件</p>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-keyword">declare</span> <span class="hljs-built_in">module</span> <span class="hljs-string">"*.vue"</span> &#123;
  <span class="hljs-keyword">import</span> <span class="hljs-keyword">type</span> &#123; DefineComponent &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">"vue"</span>;
  <span class="hljs-keyword">const</span> component: DefineComponent<&#123;&#125;, &#123;&#125;, <span class="hljs-built_in">any</span>>;
  <span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> component;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-16">2. ts</h2>
<p>虽然在第一节我们已经介绍过使用 <code>ts-loader</code> 处理 <code>ts</code> 文件，但是这会存在一个问题：该 <code>loader</code> 是把 <code>typeScript</code> 转换成 <code>javaScript</code> , 只负责新语法的转换，新增的 API 不会自动添加 <code>polyfill</code></p>
<p>为了解决这个问题，我们还是要祭出 <code>babel</code>。<code>babel</code> 是一个工具链，主要用于旧浏览器或者环境中将 <code>ECMAScript 2015+</code> 代码转换为向后兼容版本的
<code>javaScript</code> ，包括语法转换、源代码转换等。关注社区的小伙伴可能知道，从 <code>babel7</code> 开始 <code>babel</code> 已经支持 <code>ts</code> 的编译，所以 <code>ts-loader</code> 可以弃用了</p>
<p>安装 <code>babel</code> 相关依赖：</p>
<pre><code class="hljs language-cmd copyable" lang="cmd">npm i babel-loader @babel/core @babel/preset-env @babel/preset-typescript -D
<span class="copy-code-btn">复制代码</span></code></pre>
<p>修改 <code>webpack.base.js</code> ：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-built_in">module</span>.epxorts = &#123;
  <span class="hljs-attr">module</span>: &#123;
    <span class="hljs-attr">rules</span>: [
      &#123;
        <span class="hljs-attr">test</span>: <span class="hljs-regexp">/\.(t|j)s$/</span>,
        exclude: <span class="hljs-regexp">/node_modules/</span>,
        use: &#123;
          <span class="hljs-attr">loader</span>: <span class="hljs-string">"babel-loader"</span>,
          <span class="hljs-attr">options</span>: &#123;
            <span class="hljs-attr">cacheDirectory</span>: <span class="hljs-literal">true</span>,
          &#125;,
        &#125;,
      &#125;,
    ],
  &#125;,
&#125;;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>在项目根目录添加 <code>babel.config.js</code> 文件：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-built_in">module</span>.exports = &#123;
  <span class="hljs-attr">presets</span>: [
    <span class="hljs-string">"@babel/preset-env"</span>,
    [
      <span class="hljs-string">"@babel/preset-typescript"</span>,
      &#123;
        <span class="hljs-attr">allExtensions</span>: <span class="hljs-literal">true</span>, <span class="hljs-comment">//支持所有文件扩展名</span>
      &#125;,
    ],
  ],
&#125;;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>现在可以安心的卸载 <code>ts-loader</code> 了</p>
<h2 data-id="heading-17">3. scss</h2>
<p>给 <code>App.vue</code> 文件添加样式，我使用了 <code>scss</code>，不出意外的报错了，因为缺少相应的 <code>loader</code></p>
<pre><code class="hljs language-cmd copyable" lang="cmd">npm i css-loader style-loader postcss-loader postcss-preset-env sass-loader sass -D
<span class="copy-code-btn">复制代码</span></code></pre>
<p>在 <code>webpack.base.js</code> 中添加配置：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-built_in">module</span>.exports = &#123;
  <span class="hljs-comment">// ...</span>
  <span class="hljs-attr">module</span>: &#123;
    <span class="hljs-attr">rules</span>: [
      &#123;
        <span class="hljs-attr">test</span>: <span class="hljs-regexp">/\.(sa|sc|c)ss$/</span>,
        use: [<span class="hljs-string">"style-loader"</span>, <span class="hljs-string">"css-loader"</span>, <span class="hljs-string">"postcss-loader"</span>, <span class="hljs-string">"sass-loader"</span>],
      &#125;,
    ],
  &#125;,
  <span class="hljs-comment">// ...</span>
&#125;;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这里需要强调一下 <code>loader</code> 的应用顺序是从右往左，从下往上的</p>
<p><code>postcss</code> 是一个加工样式文件的工具，可以提供自动添加样式前缀、修改单位等功能，具体使用了什么功能取决于你提供了哪些 <code>postcss</code> 插件，这些插件可以直接配置在 <code>loader</code> 中，更好的做法是在项目的根目录提供一份单独的配置文件</p>
<p>在一些陈旧的项目中可能会看到 <code>autoprefixer</code> 这个插件，现在我们可以直接使用 <code>postcss-preset-env</code> 这个插件，自动添加前缀的功能已经包含在了其中</p>
<p>在项目根目录下新增 <code>postcss.config.js</code> 配置文件：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-built_in">module</span>.exports = &#123;
  <span class="hljs-attr">plugins</span>: [<span class="hljs-string">"postcss-preset-env"</span>],
&#125;;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>如果在项目中你选择了 <code>less</code> ，只需安装 <code>less-loader</code> ，再修改少量的配置即可</p>
<h2 data-id="heading-18">4. img</h2>
<p>在 <code>webpack5</code> 之前，加载图片、字体等资源需要我们使用 <code>url-loader</code>、 <code>file-loader</code> 等来处理</p>
<p>从 <code>webpack5</code> 开始，我们可以使用内置的资源模块类型 <a href="https://webpack.js.org/guides/asset-modules/" target="_blank" rel="nofollow noopener noreferrer">Asset Modules type</a>，来替代这些 <code>loader</code> 的工作</p>
<p>资源模块类型 <code>Asset Modules type</code> 分为四种：</p>
<ul>
<li><code>asset/resource</code> 发送一个单独的文件并导出 URL，之前通过使用 <code>file-loader</code> 实现</li>
<li><code>asset/inline</code> 导出一个资源的 data URI，之前通过使用 <code>url-loader</code> 实现</li>
<li><code>asset/source</code> 导出资源的源代码，之前通过使用 <code>raw-loader</code> 实现</li>
<li><code>asset</code> 在导出一个 data URI 和发送一个单独的文件之间自动选择，之前通过使用 <code>url-loader</code> 实现，并且可以配置资源体积限制</li>
</ul>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-built_in">module</span>.epxorts = &#123;
  <span class="hljs-attr">module</span>: &#123;
    <span class="hljs-attr">rules</span>: [
      &#123;
        <span class="hljs-attr">test</span>: <span class="hljs-regexp">/\.(png|svg|jpe?g|gif)$/</span>,
        type: <span class="hljs-string">"asset"</span>,
        <span class="hljs-attr">generator</span>: &#123;
          <span class="hljs-attr">filename</span>: <span class="hljs-string">"images/[name]-[hash][ext]"</span>,
        &#125;,
      &#125;,
    ],
  &#125;,
&#125;;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>需要注意的是这里的 <code>[ext]</code> 扩展名通配符包含了 <code>.</code> ，我们不需要额外再写，跟之前的 <code>loader</code> 有所区别</p>
<h2 data-id="heading-19">5. font</h2>
<p>同上，这里不再赘述</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-built_in">module</span>.epxorts = &#123;
  <span class="hljs-attr">module</span>: &#123;
    <span class="hljs-attr">rules</span>: [
      &#123;
        <span class="hljs-attr">test</span>: <span class="hljs-regexp">/\.(eot|svg|ttf|woff2?|)$/</span>,
        type: <span class="hljs-string">"asset/resource"</span>,
        <span class="hljs-attr">generator</span>: &#123;
          <span class="hljs-attr">filename</span>: <span class="hljs-string">"fonts/[name]-[hash][ext]"</span>,
        &#125;,
      &#125;,
    ],
  &#125;,
&#125;;
<span class="copy-code-btn">复制代码</span></code></pre>
<h1 data-id="heading-20">五、其他配置</h1>
<p>接着再介绍一些让 <code>webpack</code> 更好用的配置和插件</p>
<h2 data-id="heading-21">1. 注入环境变量</h2>
<p>为了可以跨终端设置环境变量，我们使用 <code>cross-env</code> 这个工具</p>
<pre><code class="hljs language-cmd copyable" lang="cmd">npm i cross-env -D
<span class="copy-code-btn">复制代码</span></code></pre>
<p>修改 <code>npm</code> 脚本：</p>
<pre><code class="hljs language-json copyable" lang="json">&#123;
  <span class="hljs-attr">"scripts"</span>: &#123;
    <span class="hljs-attr">"build"</span>: <span class="hljs-string">"cross-env NODE_ENV=production webpack --config ./config/webpack.prod.js"</span>,
    <span class="hljs-attr">"serve"</span>: <span class="hljs-string">"cross-env NODE_ENV=development webpack serve --config ./config/webpack.dev.js"</span>
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这样在 <code>webpack</code> 的配置文件中，可以通过 <code>process.env.NODE_ENV</code> 读取到当前设置的环境变量，我们可以根据这个变量来做一些配置优化</p>
<h2 data-id="heading-22">2. 提取样式文件</h2>
<p><code>webpack</code> 官方文档中有这样一段描述：</p>
<blockquote>
<p>For production builds it's recommended to extract the CSS from your bundle being able to use parallel loading of CSS/JS resources later on.</p>
</blockquote>
<p>大意是建议我们在生产环境使用 <code>mini-css-extract-plugin</code> 这个工具来抽离样式文件，这样在浏览器中可以拥有更好的加载效率</p>
<p>安装相关依赖：</p>
<pre><code class="hljs language-cmd copyable" lang="cmd">npm i mini-css-extract-plugin -D
<span class="copy-code-btn">复制代码</span></code></pre>
<p>在 <code>webpack.base.js</code> 基础配置文件中做如下修改：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> MiniCssExtractPlugin = <span class="hljs-built_in">require</span>(<span class="hljs-string">"mini-css-extract-plugin"</span>);
<span class="hljs-keyword">const</span> devMode = process.env.NODE_ENV !== <span class="hljs-string">"production"</span>;

<span class="hljs-built_in">module</span>.exports = &#123;
  <span class="hljs-comment">// ...</span>
  <span class="hljs-attr">module</span>: &#123;
    <span class="hljs-attr">rules</span>: [
      &#123;
        <span class="hljs-attr">test</span>: <span class="hljs-regexp">/\.(sa|sc|c)ss$/</span>,
        use: [
          devMode ? <span class="hljs-string">"style-loader"</span> : MiniCssExtractPlugin.loader,
          <span class="hljs-string">"css-loader"</span>,
          <span class="hljs-string">"postcss-loader"</span>,
          <span class="hljs-string">"sass-loader"</span>,
        ],
      &#125;,
    ],
  &#125;,
  <span class="hljs-comment">// ...</span>
&#125;;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>在 <code>webpack.prod.js</code> 生产配置文件中添加插件：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> MiniCssExtractPlugin = <span class="hljs-built_in">require</span>(<span class="hljs-string">"mini-css-extract-plugin"</span>);

<span class="hljs-built_in">module</span>.exports = merge(baseConfig, &#123;
  <span class="hljs-comment">// ...</span>
  <span class="hljs-attr">plugins</span>: [<span class="hljs-keyword">new</span> MiniCssExtractPlugin()],
  <span class="hljs-comment">// ...</span>
&#125;);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这样在开发环境，我们依然使用 <code>style-loader</code> 有更高的开发效率，打包时，则能将样式抽离成单独的文件</p>
<h2 data-id="heading-23">3. 自动拷贝文件</h2>
<p>当某些文件不需要经过 <code>webpack</code> 打包而直接使用，如一些三方脚本 <code>js</code> 文件等等，我们可以使用 <code>copy-webpack-plugin</code> 这个插件直接进行文件的拷贝</p>
<p>例如我们有一个 <code>lodash.min.js</code> 文件放在了 <code>public</code> 文件夹下，现在我们想在项目中使用，有两个方案：</p>
<ul>
<li>方案一：在 <code>index.js</code> 入口文件中直接导入</li>
</ul>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">import</span> <span class="hljs-string">"../public/lodash.min.js"</span>;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这种方案可行，但是会经过 <code>webpack</code> 打包处理，完全没有必要，降低了打包效率</p>
<ul>
<li>方案二：在 <code>index.html</code> 中用 <code><script></script></code> 标签引入</li>
</ul>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">script</span> <span class="hljs-attr">src</span>=<span class="hljs-string">"./public/lodash.min.js"</span>></span><span class="hljs-tag"></<span class="hljs-name">script</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>在开发环境一切正常，但是当你打包后发布到服务器上你会发现，<code>lodash.min.js</code> 文件并不能成功加载，这是因为 <code>webpack</code> 并不会解析 <code>index.html</code> ，只会把它当做一个普通文本，所以需要我们手动处理其中引用的各个文件</p>
<pre><code class="hljs language-cmd copyable" lang="cmd">npm i <span class="hljs-built_in">copy</span>-webpack-plugin -D
<span class="copy-code-btn">复制代码</span></code></pre>
<p>修改 <code>webpack.prod.js</code>：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> CopyWebpackPlugin = <span class="hljs-built_in">require</span>(<span class="hljs-string">"copy-webpack-plugin"</span>);

<span class="hljs-built_in">module</span>.exports = merge(baseConfig, &#123;
  <span class="hljs-comment">// ...</span>
  <span class="hljs-attr">plugins</span>: [
    <span class="hljs-keyword">new</span> CopyWebpackPlugin(&#123;
      <span class="hljs-comment">// from后的路径是相对于项目的根目录，to后的路径是相对于打包后的dist目录</span>
      <span class="hljs-attr">patterns</span>: [&#123; <span class="hljs-attr">from</span>: <span class="hljs-string">"./public"</span>, <span class="hljs-attr">to</span>: <span class="hljs-string">"./public"</span> &#125;],
    &#125;),
  ],
  <span class="hljs-comment">// ...</span>
&#125;);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>那么为什么在开发环境可以正常运行，主要是因为 <code>webpack-dev-server</code> 有一个功能：浏览器请求的文件如果不是通过 <code>webpack</code> 提供，则默认到项目根目录中寻找</p>
<p>devServer 启动时会给出提示：</p>
<pre><code class="copyable">Content not from webpack is served from D:\github-workspaces\webapck-ts-vue
<span class="copy-code-btn">复制代码</span></code></pre>
<p>然后再根据我们在 <code>index.html</code> 配置的<code>./public/lodash.min.js</code>路径，就能正确找到静态资源的位置</p>
<h2 data-id="heading-24">4. 清理打包目录</h2>
<p>在 <code>webpack5</code> 之前，我们都习惯于使用一款名叫 <code>clean-webpack-plugin</code> 的插件清理 <code>dist</code> 目录，从 <code>webpack5</code> 开始自带了清理打包目录的功能，只需在生产环境的配置文件中增加一个配置即可</p>
<p>修改 <code>webpack.prod.js</code> 配置文件：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-built_in">module</span>.exports = merge(baseConfig, &#123;
  <span class="hljs-comment">// ...</span>
  <span class="hljs-attr">output</span>: &#123;
    <span class="hljs-attr">clean</span>: <span class="hljs-literal">true</span>,
  &#125;,
  <span class="hljs-comment">// ...</span>
&#125;);
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-25">5. 省略拓展名</h2>
<p><code>extensions</code> 配置项的功能是解析到文件时自动添加扩展名，其默认值为 <code>['.wasm', '.mjs', '.js', '.json']</code> ，我们可以根据需求将 <code>.vue</code> 也加入其中，虽然会带来一些便利，但实际上会在一定程度上影响 <code>webpack</code> 的运行效率，不推荐修改</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-built_in">module</span>.exports = &#123;
  <span class="hljs-comment">// ...</span>
  <span class="hljs-attr">resolve</span>: &#123;
    <span class="hljs-attr">extensions</span>: [<span class="hljs-string">".vue"</span>],
  &#125;,
  <span class="hljs-comment">// ...</span>
&#125;;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-26">6. 设置路径别名</h2>
<p><code>alias</code> 是一个非常和好用的配置项，当我们项目的目录结构比较深时，或者一个文件的路径可能需要 <code>../../</code> 这种路径片段才能访问到的时候，我们可以给一些常用的路径设置别名</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> path = <span class="hljs-built_in">require</span>(<span class="hljs-string">"path"</span>);

<span class="hljs-built_in">module</span>.exports = &#123;
  <span class="hljs-comment">// ...</span>
  <span class="hljs-attr">resolve</span>: &#123;
    <span class="hljs-attr">alias</span>: &#123;
      <span class="hljs-string">"@"</span>: path.resolve(__dirname, <span class="hljs-string">"../src"</span>),
    &#125;,
  &#125;,
  <span class="hljs-comment">// ...</span>
&#125;;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这样在代码中就能通过别名的方式引入文件：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">import</span> App <span class="hljs-keyword">from</span> <span class="hljs-string">"@/App.vue"</span>;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-27">7. 友好打包提示</h2>
<p>可装可不装的一个美化控制台输出的插件</p>
<pre><code class="hljs language-cmd copyable" lang="cmd">npm i friendly-errors-webpack-plugin -D
<span class="copy-code-btn">复制代码</span></code></pre>
<p>修改 <code>webpack.dev.js</code> 配置文件：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> FriendlyErrorsWebpackPlugin = <span class="hljs-built_in">require</span>(<span class="hljs-string">"friendly-errors-webpack-plugin"</span>);

modules.exports = &#123;
  <span class="hljs-comment">// ...</span>
  <span class="hljs-attr">plugins</span>: [<span class="hljs-keyword">new</span> FriendlyErrorsWebpackPlugin()],
  <span class="hljs-comment">// ...</span>
&#125;;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-28">8. 包文件分析</h2>
<p>如果你想对打包之后的文件进行分析和优化，可以安装这个插件</p>
<pre><code class="hljs language-cmd copyable" lang="cmd">npm i webpack-bundle-analyzer -D
<span class="copy-code-btn">复制代码</span></code></pre>
<p>修改 <code>webpack.prod.js</code> 配置文件：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> &#123; BundleAnalyzerPlugin &#125; = <span class="hljs-built_in">require</span>(<span class="hljs-string">"webpack-bundle-analyzer"</span>);

<span class="hljs-built_in">module</span>.exports = &#123;
  <span class="hljs-attr">plugins</span>: [
    <span class="hljs-comment">// ...</span>
    <span class="hljs-keyword">new</span> BundleAnalyzerPlugin(&#123;
      <span class="hljs-attr">analyzerMode</span>: <span class="hljs-string">"disabled"</span>,
      <span class="hljs-attr">generateStatsFile</span>: <span class="hljs-literal">true</span>,
    &#125;),
    <span class="hljs-comment">// ...</span>
  ],
&#125;;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这样每次打包完成之后，都会在打包文件目录中生成一个 <code>stats.json</code> 文件</p>
<p>在 <code>package.json</code> 中添加脚本：</p>
<pre><code class="hljs language-json copyable" lang="json">&#123;
  <span class="hljs-attr">"scripts"</span>: &#123;
    <span class="hljs-attr">"analyze"</span>: <span class="hljs-string">"webpack-bundle-analyzer --port 3000 ./dist/stats.json"</span>
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>运行 <code>npm run analyze</code> 即可自动打开包文件分析页面</p>
<h2 data-id="heading-29">9. 文件缓存</h2>
<p><code>webpack5</code> 之前我们常用 <code>cache-loader</code> 、<code>hard-source-webpack-plugin</code> 做文件缓存，加速二次构建， <code>webpack5</code> 现在内置了这种能力，默认会把编译的结果缓存到内存中，通过配置还可以缓存到文件系统中</p>
<p>修改 <code>webpack.base.js</code>：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-built_in">module</span>.exports = &#123;
  <span class="hljs-comment">// ...</span>
  <span class="hljs-attr">cache</span>: &#123;
    <span class="hljs-attr">type</span>: <span class="hljs-string">"filesystem"</span>,
  &#125;,
  <span class="hljs-comment">// ...</span>
&#125;;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-30">10. 代码分隔</h2>
<p><code>webpack</code> 默认会把所有的依赖打包到一个 <code>js</code> 文件当中，这个文件的大小会随着项目内容的增长而线性增大，导致浏览器加载变慢，可以使用代码分隔的方法来缓解这个问题</p>
<p>在 <code>webpack.prod.js</code> 中新增配置：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-built_in">module</span>.exports = &#123;
  <span class="hljs-comment">// ...</span>
  <span class="hljs-attr">optimization</span>: &#123;
    <span class="hljs-attr">splitChunks</span>: &#123;
      <span class="hljs-comment">// 选择对哪些文件进行拆分，默认是async，即只对动态导入的文件进行拆分</span>
      <span class="hljs-attr">chunks</span>: <span class="hljs-string">"all"</span>,
      <span class="hljs-comment">// 提取chunk的最小体积</span>
      <span class="hljs-attr">minSize</span>: <span class="hljs-number">20000</span>,
      <span class="hljs-comment">// 要提取的chunk最少被引用次数</span>
      <span class="hljs-attr">minChunks</span>: <span class="hljs-number">1</span>,
      <span class="hljs-comment">// 对要提取的trunk进行分组</span>
      <span class="hljs-attr">cacheGroups</span>: &#123;
        <span class="hljs-comment">// 匹配node_modules中的三方库，将其打包成一个trunk</span>
        <span class="hljs-attr">defaultVendors</span>: &#123;
          <span class="hljs-attr">test</span>: <span class="hljs-regexp">/[\\/]node_modules[\\/]/</span>,
          name: <span class="hljs-string">"vendors"</span>,
          <span class="hljs-attr">priority</span>: -<span class="hljs-number">10</span>,
        &#125;,
        <span class="hljs-attr">default</span>: &#123;
          <span class="hljs-comment">// 将至少被两个trunk引入的模块提取出来打包成单独trunk</span>
          <span class="hljs-attr">minChunks</span>: <span class="hljs-number">2</span>,
          <span class="hljs-attr">name</span>: <span class="hljs-string">"default"</span>,
          <span class="hljs-attr">priority</span>: -<span class="hljs-number">20</span>,
        &#125;,
      &#125;,
    &#125;,
  &#125;,
  <span class="hljs-comment">// ...</span>
&#125;;
<span class="copy-code-btn">复制代码</span></code></pre>
<h1 data-id="heading-31">六、代码规范</h1>
<p>啊，你不喜欢用 eslint？企业级项目，别人都用，你确定不要吗？你确定吗？</p>
<p>用吧用吧...</p>
<h2 data-id="heading-32">1. ESLint</h2>
<p><code>ESLint</code> 用于检查代码规则，在开发过程中根据你提供的规则做检验，并给出错误提示</p>
<p>在项目中安装 <code>eslint</code> 依赖：</p>
<pre><code class="hljs language-cmd copyable" lang="cmd">npm i eslint -D
<span class="copy-code-btn">复制代码</span></code></pre>
<p>运行<code>eslint</code> 初始化命令，根据提示进行选择，选择完毕后会自动安装相关依赖，并在项目根目录生成 <code>.eslintrc.js</code> 配置文件</p>
<pre><code class="hljs language-cmd copyable" lang="cmd">npx eslint --init
$ √ How would you like to use ESLint? · problems
$ √ What <span class="hljs-built_in">type</span> of modules does your project use? · esm
$ √ Which framework does your project use? · vue
$ √ Does your project use TypeScript? · No / Yes
$ √ Where does your code run? · browser
$ √ What <span class="hljs-built_in">format</span> <span class="hljs-keyword">do</span> you want your config file to be <span class="hljs-keyword">in</span>? · JavaScript
$ The config that you've selected requires the following dependencies:

@typescript-eslint/parser  @typescript-eslint/eslint-plugin eslint-plugin-vue
<span class="copy-code-btn">复制代码</span></code></pre>
<p><a href="https://github.com/typescript-eslint/typescript-eslint" target="_blank" rel="nofollow noopener noreferrer">typescript-eslint/eslint-plugin</a> 是 <code>ts</code> 官方提供的 <code>ESLint</code> 插件</p>
<p><a href="https://eslint.vuejs.org/" target="_blank" rel="nofollow noopener noreferrer">eslint-plugin-vue</a> 是 <code>vue</code> 官方提供的 <code>ESLint</code> 插件</p>
<p>结合两份文档对 <code>.eslintrc.js</code> 适当修改后内容如下：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-built_in">module</span>.exports = &#123;
  <span class="hljs-attr">env</span>: &#123;
    <span class="hljs-attr">browser</span>: <span class="hljs-literal">true</span>,
    <span class="hljs-attr">es2021</span>: <span class="hljs-literal">true</span>,
  &#125;,
  <span class="hljs-attr">parser</span>: <span class="hljs-string">"vue-eslint-parser"</span>,
  <span class="hljs-attr">parserOptions</span>: &#123;
    <span class="hljs-attr">ecmaVersion</span>: <span class="hljs-number">12</span>,
    <span class="hljs-attr">parser</span>: <span class="hljs-string">"@typescript-eslint/parser"</span>,
    <span class="hljs-attr">sourceType</span>: <span class="hljs-string">"module"</span>,
  &#125;,
  <span class="hljs-attr">plugins</span>: [<span class="hljs-string">"vue"</span>, <span class="hljs-string">"@typescript-eslint"</span>],
  <span class="hljs-comment">// extends的优先级也是从后往前的</span>
  <span class="hljs-attr">extends</span>: [
    <span class="hljs-string">"plugin:@typescript-eslint/recommended"</span>,
    <span class="hljs-string">"plugin:vue/vue3-recommended"</span>,
    <span class="hljs-string">"eslint:recommended"</span>,
  ],
  <span class="hljs-attr">rules</span>: &#123;
    <span class="hljs-string">"@typescript-eslint/no-explicit-any"</span>: <span class="hljs-string">"off"</span>,
    <span class="hljs-string">"@typescript-eslint/ban-types"</span>: <span class="hljs-string">"off"</span>,
  &#125;,
&#125;;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>查阅 <code>eslint-loader</code> 文档后得知这个 <code>loader</code> 已经被官方废弃，推荐使用新方案 <code>eslint-webpack-plugin</code></p>
<pre><code class="hljs language-cmd copyable" lang="cmd">npm i eslint-webpack-plugin -D
<span class="copy-code-btn">复制代码</span></code></pre>
<p>在 <code>webpack.dev.js</code> 中添加配置：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> ESLintPlugin = <span class="hljs-built_in">require</span>(<span class="hljs-string">"eslint-webpack-plugin"</span>);

<span class="hljs-built_in">module</span>.exports = &#123;
  <span class="hljs-comment">// ...</span>
  <span class="hljs-comment">// 注意如果不声明文件扩展名，eslint默认只会检查js结尾的文件</span>
  <span class="hljs-attr">plugins</span>: [<span class="hljs-keyword">new</span> ESLintPlugin(&#123; <span class="hljs-attr">extensions</span>: [<span class="hljs-string">"js"</span>, <span class="hljs-string">"ts"</span>, <span class="hljs-string">"vue"</span>] &#125;)],
  <span class="hljs-comment">// ...</span>
&#125;;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这样在运行开发命令后，在终端中就能拥有良好的代码规范提示</p>
<h2 data-id="heading-33">2. Prettier</h2>
<p>统一的编码风格有助于团队成员之间的高效协作</p>
<p>当你接到一个需求，打开别人的代码，发现从来没有进行过格式化，是一件相当恐怖的事情</p>
<p>可能你只需要改少量的代码，但因为你想要格式化整个文本让它变得美观好看，最终导致在代码仓库中显示更改了整个文件，难以追踪实际的代码变化</p>
<p>为了解决这个问题，我们在项目中加入 <code>prettier</code> 的支持</p>
<pre><code class="hljs language-cmd copyable" lang="cmd">npm i prittier eslint-config-prettier eslint-plugin-prettier -D
<span class="copy-code-btn">复制代码</span></code></pre>
<p>添加 <code>.prettierrc</code> 配置文件：</p>
<pre><code class="hljs language-json copyable" lang="json">&#123;
  <span class="hljs-attr">"printWidth"</span>: <span class="hljs-number">80</span>
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这里我们只指定一个行宽，其它配置全部使用 <code>prettier</code> 的默认值，这也符合 <code>prettier</code> 这个工具的设计理念，它本身提供的配置项非常少，目的就是不希望用户随意更改，这样才能在更大程度上保持统一</p>
<p>添加 <code>.prettierignore</code> 配置文件：</p>
<pre><code class="copyable">dist/
node_modules
<span class="copy-code-btn">复制代码</span></code></pre>
<p>修改 <code>.eslintrc.js</code>：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-built_in">module</span>.exports = &#123;
  <span class="hljs-comment">// ...</span>
  <span class="hljs-attr">plugins</span>: [<span class="hljs-string">"vue"</span>, <span class="hljs-string">"@typescript-eslint"</span>, <span class="hljs-string">"prettier"</span>],
  <span class="hljs-attr">extends</span>: [
    <span class="hljs-string">"plugin:@typescript-eslint/recommended"</span>,
    <span class="hljs-string">"plugin:vue/vue3-recommended"</span>,
    <span class="hljs-string">"eslint:recommended"</span>,
    <span class="hljs-string">"plugin:prettier/recommended"</span>,
  ],
  <span class="hljs-comment">// ...</span>
&#125;;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>注意一定要将 <code>prettier</code> 的插件放置在最后一个</p>
<p>这样就将 <code>eslint</code> 和 <code>prettier</code> 整合到了一起，每多写一个空格或少些一个分号，控制台都会有大红叉报错提醒，非常的赏心悦目</p>
<h2 data-id="heading-34">3. lint-staged</h2>
<p>如果在整个项目上运行 <code>lint</code> 效率会非常底下，更好的做法是只让进入暂存区的文件做代码校验，这会节约很多时间，我们需要使用的工具是 <code>lint-staged</code></p>
<pre><code class="hljs language-cmd copyable" lang="cmd">npm i lint-staged -D
<span class="copy-code-btn">复制代码</span></code></pre>
<p>添加 <code>lint-staged.config.js</code> 配置文件：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-built_in">module</span>.exports = &#123;
  <span class="hljs-string">"src/**/*.&#123;js,ts,vue&#125;"</span>: [
    <span class="hljs-string">"eslint --fix --ext .js,.ts,.vue"</span>,
    <span class="hljs-string">"prettier --write"</span>,
  ],
&#125;;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这样在命令行执行 <code>npx lint-staged</code> 就能手动在暂存区运行 <code>eslint+prettier</code> 做代码风格校验了</p>
<h2 data-id="heading-35">4. husky</h2>
<p>为了确保进入 <code>git</code> 仓库的代码都是符合代码规则且拥有统一风格，在代码提交之前，我们还需要强制进行一次代码校验，使用 <code>husky</code>（哈士奇），能够在我们做代码提交动作（commit）的时候自动运行代码校验命令</p>
<pre><code class="hljs language-cmd copyable" lang="cmd">npm i husky -D
<span class="copy-code-btn">复制代码</span></code></pre>
<p>我们安装的是 <code>6.0</code> 版本以上的 <code>husky</code> ，根据文档先在 <code>package.json</code> 中添加一条脚本：</p>
<pre><code class="hljs language-json copyable" lang="json">&#123;
  <span class="hljs-attr">"prepare"</span>: <span class="hljs-string">"husky install"</span>
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>运行 <code>husky</code> 安装脚本：</p>
<pre><code class="hljs language-cmd copyable" lang="cmd">npm run prepare
<span class="copy-code-btn">复制代码</span></code></pre>
<p>运行完此命令会在项目根目录下生成一个 <code>.husky</code> 文件夹</p>
<p>添加一个 <code>git hook</code>：</p>
<pre><code class="hljs language-cmd copyable" lang="cmd">npx husky add .husky/pre-commit "npx lint-staged"
<span class="copy-code-btn">复制代码</span></code></pre>
<p>执行完此命令后，会在 <code>.husky</code> 目录下自动生成一个 <code>pre-commit</code> 文件，但是经过我在公司 windows 电脑上的测试并没有成功生成，所以我们手动添加这个文件</p>
<p>在 <code>.husky</code> 目录下新建 <code>pre-commit</code> 文件，写入一下内容：</p>
<pre><code class="hljs language-sh copyable" lang="sh"><span class="hljs-meta">#!/bin/sh</span>
. <span class="hljs-string">"<span class="hljs-subst">$(dirname <span class="hljs-string">"<span class="hljs-variable">$0</span>"</span>)</span>/_/husky.sh"</span>

npx lint-staged
<span class="copy-code-btn">复制代码</span></code></pre>
<p>现在每当你执行 <code>commit</code> 操作时，都会自动执行 <code>lint-staged</code> 做规则校验，如果 <code>lint</code> 没有通过，则会 <code>abort</code> 当前的 <code>commit</code> 操作，直到你修复完了所有的 <code>error</code> 才能成功提交</p>
<h1 data-id="heading-36">写在最后</h1>
<p>到这里 webpack 基础的东西就写完了，囿于本人有限的技术水平，文章中肯定存在不少疏漏和没有讲清楚的地方，欢迎各位批评指正</p>
<p>尽管如此以上内容还是花费了我不少气力，原因还是 webpack 工具链流程太长，每个工具都包含大量的配置项，想把每个配置的具体作用都摸清楚实在不是一件容易的事，本文只介绍了其中一些最核心最常用的配置和插件，难怪有人调侃有 <code>webpack 配置工程师</code> 这么一说</p>
<p>我们也能大致预料到，自己配置出来的项目大概率是一个次优化的产物，肯定还存在大量改进的空间。<code>因此我更愿意相信社区的力量，在实际工作过程中使用社区里更成熟的工具</code>，它们有全职的开发者维护，投入的精力肯定比我个人甚至是绝大多数像我一样的普通开发者多得多，经过社区的检验后是相当靠谱的</p>
<p>写这篇文章主要是自己最近在复习，巩固基础，现在正好学到了 webpack 部分，就顺手做一些总结，为自己以后面试做准备。如果碰巧帮助到了你，那我万分欣喜</p>
<p>本人工作于杭州，活跃于长三角一带，如果想交个朋友或有进一步交流的需要的话，可以加我微信：imheguang</p>
<p>我是和光，让我们一起进步，变得更强</p></div>  
</div>
            