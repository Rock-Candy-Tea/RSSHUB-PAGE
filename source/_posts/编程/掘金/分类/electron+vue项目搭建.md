
---
title: 'electron+vue项目搭建'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=8984'
author: 掘金
comments: false
date: Wed, 01 Sep 2021 08:50:40 GMT
thumbnail: 'https://picsum.photos/400/300?random=8984'
---

<div>   
<div class="markdown-body html cache"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h2 data-id="heading-0">前言</h2>
<p>本文搭建基于vue cli提供的<a href="https://link.juejin.cn/?target=https%3A%2F%2Fnklayman.github.io%2Fvue-cli-plugin-electron-builder%2F" target="_blank" rel="nofollow noopener noreferrer" title="https://nklayman.github.io/vue-cli-plugin-electron-builder/" ref="nofollow noopener noreferrer">vue-cli-plugin-electron-builder</a>进行脚手架搭建。如果你是一个前端开发，想把现有页面转化成桌面软件，并且能有win，mac，linux的版本，那么electron不失为一个好的选择。</p>
<h2 data-id="heading-1">开发前的准备</h2>
<p>说到底electron本质上就是一个基于Chromium的应用，通俗点说，这个桌面软件就是一个浏览器，我们写的东西在浏览器中展示，在开发前你得知道前端三驾马车 HTML, CSS 和 JavaScript，涉及到一些文件等特殊的处理的话那么会有些许node的知识，electron能直接调用node，这是浏览器所不能做的。</p>
<h2 data-id="heading-2">安装</h2>
<pre><code class="hljs language-javascript copyable" lang="javascript"># 设置淘宝源
npm install --registry=https:<span class="hljs-comment">//registry.npm.taobao.org</span>
# 需要注意的是electron的本体下载并不是走这里所以还是要去设置一下
npm config edit
# 该命令会打开npm的配置文件，请在空白处添加
registry=https:<span class="hljs-comment">//registry.npm.taobao.org/</span>
electron_mirror=https:<span class="hljs-comment">//cdn.npm.taobao.org/dist/electron/ </span>
ELECTRON_BUILDER_BINARIES_MIRROR=http:<span class="hljs-comment">//npm.taobao.org/mirrors/electron-builder-binaries/</span>

# 安装vue-cli
npm install -g @vue/cli

# 创建vue项目
vue create electron-vue
# 自行选择vue版本，由于electron使用的是Chromium，那么我们可以不必考虑兼容性的问题
cd electron-vue
vue add electron-builder
# 选择electron版本号，这里我选择的是<span class="hljs-string">`11.0.0`</span>安装完成之后会有<span class="hljs-string">`src/background.js`</span>文件，<span class="hljs-string">`package.json`</span>中会多出几条electron的build及serve命令

# 启动项目
npm run electron:serve
# 稍等一会儿（Vue Devtools首次安装问题）会有一个桌面窗口出现，ok安装就完成啦，接下来我们对其进行改造。
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-3">说明</h2>
<p>改造前说明一下：electron开发和我们普通的开发有所不同，它是有两种进程的：主进程和渲染进程</p>
<ul>
<li>主进程src/background.js：管理所有渲染进程（怎么配置桌面软件，怎么打开桌面软件，怎么相互通信等等）。</li>
<li>渲染进程：说得直白点就是网页（就是打开我们单页的网页）</li>
</ul>
<p><code>npm run electron:serve</code>做了什么，其实就是类似先运行npm run serve启动一个网页的端口并生成一个实时打包的js，然后通过electron的命令指定启动的js，用主进程载入网页的端口。
通俗点来说，你可以理解为我们开发的桌面软件是一个浏览器，主进程就是设置这个浏览器的样式（图标，大小等等），渲染进程就是浏览器打开的网页。</p>
<h2 data-id="heading-4">改造</h2>
<h3 data-id="heading-5">src目录改造</h3>
<p>首先我们在src目录下新建两个文件夹src/main、src/renderer，这两个分别放主进程及渲染进程的文件，然后把src/background.js放入src/main中，然后重命名为index.js，src下其他文件放入src/renderer中。
现在的结构如下：</p>
<pre><code class="copyable">├─src                          # 源码目录
│  ├─main                      # 主进程目录
│  │  └─index.js               # 主进程入口
│  └─renderer                  # 渲染进程文件夹
│      ├─assets
│      ├─components
│      ├─App.vue
│      └─main.js               # 渲染进程入口
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-6">添加vue.config.js</h3>
<p>由于我们修改了默认的入口文件位置，我们应该配置对应的参数，
在根目录新建vue.config.js，添加</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-built_in">module</span>.exports = &#123;
  <span class="hljs-attr">pluginOptions</span>: &#123;
    <span class="hljs-attr">electronBuilder</span>: &#123;
      <span class="hljs-attr">mainProcessFile</span>: <span class="hljs-string">'src/main/index.js'</span>, <span class="hljs-comment">// 主进程入口文件</span>
      <span class="hljs-attr">rendererProcessFile</span>: <span class="hljs-string">'src/renderer/main.js'</span>, <span class="hljs-comment">// 渲染进程入口文件</span>
      <span class="hljs-attr">mainProcessWatch</span>: [<span class="hljs-string">'src/main'</span>], <span class="hljs-comment">// 检测主进程文件在更改时将重新编译主进程并重新启动</span>
    &#125;
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>然后重新<code>npm run electron:serve</code>，看能否重新启动。</p>
<p>补充：如果是只打包单页electron的话这样配置没问题，但是这样的话想对web页面打包<code>npm run build</code>会有问题，因为我们把入口文件位置修改了。</p>
<p>这里我们可以通过设置pages来修改其入口文件，并且这样还可以打包多页</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-built_in">module</span>.exports = &#123;
   <span class="hljs-attr">pages</span>: &#123;
    <span class="hljs-attr">index</span>: &#123;
      <span class="hljs-attr">entry</span>: <span class="hljs-string">'src/renderer/main.js'</span>,
      <span class="hljs-attr">template</span>: <span class="hljs-string">'public/index.html'</span>,
      <span class="hljs-attr">filename</span>: <span class="hljs-string">'index.html'</span>,
      <span class="hljs-attr">title</span>: <span class="hljs-string">'electron-vue-cli'</span>,
      <span class="hljs-attr">chunks</span>: [<span class="hljs-string">'chunk-vendors'</span>, <span class="hljs-string">'chunk-common'</span>, <span class="hljs-string">'index'</span>]
    &#125;,
    <span class="hljs-comment">// loader: 'src/loader/main.js' // 多页loader页</span>
  &#125;,
  <span class="hljs-attr">pluginOptions</span>: &#123;
    <span class="hljs-attr">electronBuilder</span>: &#123;
      <span class="hljs-attr">mainProcessFile</span>: <span class="hljs-string">'src/main/index.js'</span>, <span class="hljs-comment">// 主进程入口文件</span>
      <span class="hljs-attr">mainProcessWatch</span>: [<span class="hljs-string">'src/main'</span>], <span class="hljs-comment">// 检测主进程文件在更改时将重新编译主进程并重新启动</span>
    &#125;
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>注：如果添加了pages，请把electronBuilder里的rendererProcessFile删除，两个都是web页面的入口，是互斥的，尝试分别运行web的serve、build及electron的serve、build，看是否能成功运行(打包可能会因为网络原因，下载electron包失败，请参考安装前几步，设置淘宝源和设置electron本体下载)。</p>
<h2 data-id="heading-7">环境变量配置</h2>
<p>vue cli可以通过--mode xx来读取.env.xx设置环境变量<a href="https://link.juejin.cn/?target=https%3A%2F%2Fcli.vuejs.org%2Fzh%2Fguide%2Fmode-and-env.html%23%25E6%25A8%25A1%25E5%25BC%258F" target="_blank" rel="nofollow noopener noreferrer" title="https://cli.vuejs.org/zh/guide/mode-and-env.html#%E6%A8%A1%E5%BC%8F" ref="nofollow noopener noreferrer">参考</a>，在根目录新建</p>
<pre><code class="hljs language-javascript copyable" lang="javascript">.env  # 本地开发
.env.dev  # 打包dev
.env.test  # 打包test
.env.prod  # 打包prod

.env:
NODE_ENV=development
VUE_APP_ENV=development
VUE_APP_APPID=com.electron.electronVueDEV
VUE_APP_PRODUCTNAME=electron开发
VUE_APP_VERSION=<span class="hljs-number">0.0</span><span class="hljs-number">.1</span>
BASE_URL=/

注：.env 的NODE_ENV设置development，其余打包的请设置production
<span class="hljs-attr">NODE_ENV</span>: webpack运行的模式
VUE_APP_ENV：我们自己使用的环境变量(通过这个判断我们是什么环境)，比如.env.test为VUE_APP_ENV=test，.env.prod为VUE_APP_ENV=production
VUE_APP_APPID：electron的appId配置，com.electron.electronVueDEV，com.electron.electronVueTEST，com.electron.electronVue
VUE_APP_PRODUCTNAME：electron的productName配置，electron开发，electron测试，···
VUE_APP_VERSION：electron的version配置
<span class="copy-code-btn">复制代码</span></code></pre>
<p>修改package.json的scripts，删除原来的打包命令，新增：</p>
<pre><code class="hljs language-json copyable" lang="json">web的打包：
<span class="hljs-string">"build:dev"</span>: <span class="hljs-string">"vue-cli-service build --mode dev"</span>,
<span class="hljs-string">"build:test"</span>: <span class="hljs-string">"vue-cli-service build --mode test"</span>,
<span class="hljs-string">"build:prod"</span>: <span class="hljs-string">"vue-cli-service build --mode prod"</span>,

electron的打包：
<span class="hljs-string">"build:dev:win32"</span>: <span class="hljs-string">"vue-cli-service electron:build --mode dev --win --ia32"</span>,
<span class="hljs-string">"build:dev:win64"</span>: <span class="hljs-string">"vue-cli-service electron:build --mode dev --win --x64"</span>,
<span class="hljs-string">"build:test:win32"</span>: <span class="hljs-string">"vue-cli-service electron:build --mode test --win --ia32"</span>,
<span class="hljs-string">"build:test:win64"</span>: <span class="hljs-string">"vue-cli-service electron:build --mode test --win --x64"</span>,
<span class="hljs-string">"build:prod:win32"</span>: <span class="hljs-string">"vue-cli-service electron:build --mode prod --win --ia32"</span>,
<span class="hljs-string">"build:prod:win64"</span>: <span class="hljs-string">"vue-cli-service electron:build --mode prod --win --x64"</span>,
<span class="hljs-string">"build:dev:mac"</span>: <span class="hljs-string">"vue-cli-service electron:build --mode dev --mac"</span>,
<span class="hljs-string">"build:test:mac"</span>: <span class="hljs-string">"vue-cli-service electron:build --mode test --mac"</span>,
<span class="hljs-string">"build:prod:mac"</span>: <span class="hljs-string">"vue-cli-service electron:build --mode prod --mac"</span>,
<span class="copy-code-btn">复制代码</span></code></pre>
<p>electron打包这里只配置了win32，win64，mac的打包，如果对其他模式的包有需求的请<a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.electron.build%2Fcli" target="_blank" rel="nofollow noopener noreferrer" title="https://www.electron.build/cli" ref="nofollow noopener noreferrer">参考</a>链接自行配置。</p>
<h2 data-id="heading-8">环境变量检测及打包配置</h2>
<h3 data-id="heading-9">添加config配置</h3>
<p>新增renderer/config/index.js</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">const</span> env = process.env

<span class="hljs-keyword">const</span> config = &#123;
  <span class="hljs-attr">host</span>: <span class="hljs-string">''</span>,
  <span class="hljs-attr">baseUrl</span>: <span class="hljs-string">''</span>
&#125;

<span class="hljs-built_in">Object</span>.assign(config, env)

<span class="hljs-comment">// if (env.NODE_ENV === 'development') &#123;</span>
<span class="hljs-comment">//   config.VUE_APP_ENV = 'test'</span>
<span class="hljs-comment">// &#125;</span>

<span class="hljs-keyword">if</span> (config.VUE_APP_ENV === <span class="hljs-string">'development'</span>) &#123;
  config.host = <span class="hljs-string">'http://192.168.1.1:8080'</span>
&#125; <span class="hljs-keyword">else</span> <span class="hljs-keyword">if</span> (config.VUE_APP_ENV === <span class="hljs-string">'test'</span>) &#123;
  config.host = <span class="hljs-string">'http://192.168.1.1:8080'</span>
&#125; <span class="hljs-keyword">else</span> <span class="hljs-keyword">if</span> (config.VUE_APP_ENV === <span class="hljs-string">'production'</span>) &#123;
  config.host = <span class="hljs-string">'http://192.168.1.1:8080'</span>
&#125;

<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> config

<span class="copy-code-btn">复制代码</span></code></pre>
<p>本地开发切换环境，可以使用上面注释的方法修改，也可以直接修改.env文件的VUE_APP_ENV。</p>
<h2 data-id="heading-10">打包配置</h2>
<p>src/renderer/App.vue添加import cfg from '@/config'，打印cfg</p>
<p>vue.config.js添加</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">const</span> path = <span class="hljs-built_in">require</span>(<span class="hljs-string">'path'</span>)

<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">resolve</span>(<span class="hljs-params">dir</span>) </span>&#123;
  <span class="hljs-keyword">return</span> path.join(__dirname, dir)
&#125;

<span class="hljs-built_in">module</span>.exports = &#123;
  <span class="hljs-attr">chainWebpack</span>: <span class="hljs-function">(<span class="hljs-params">config</span>) =></span> &#123; <span class="hljs-comment">// 由于我们修改了渲染进程目录，修改'@'的alias</span>
    config.resolve.alias.set(<span class="hljs-string">'@'</span>, resolve(<span class="hljs-string">'src/renderer'</span>))
  &#125;,
  <span class="hljs-attr">builderOptions</span>: &#123;
    <span class="hljs-attr">appId</span>: process.env.VUE_APP_APPID,
    <span class="hljs-attr">productName</span>: process.env.VUE_APP_PRODUCTNAME,
    <span class="hljs-attr">extraMetadata</span>: &#123;
      <span class="hljs-attr">name</span>: process.env.VUE_APP_APPID.split(<span class="hljs-string">'.'</span>).pop(),
      <span class="hljs-attr">version</span>: process.env.VUE_APP_VERSION
    &#125;,
    <span class="hljs-attr">asar</span>: <span class="hljs-literal">true</span>,
    <span class="hljs-attr">directories</span>: &#123;
      <span class="hljs-attr">output</span>: <span class="hljs-string">"dist_electron"</span>,
      <span class="hljs-attr">buildResources</span>: <span class="hljs-string">"build"</span>,
      <span class="hljs-attr">app</span>: <span class="hljs-string">"dist_electron/bundled"</span>
    &#125;,
    <span class="hljs-attr">files</span>: [
      &#123;
        <span class="hljs-attr">filter</span>: [
          <span class="hljs-string">"**"</span>
        ]
      &#125;
    ],
    <span class="hljs-attr">extends</span>: <span class="hljs-literal">null</span>,
    <span class="hljs-attr">electronVersion</span>: <span class="hljs-string">"11.3.0"</span>,
    <span class="hljs-attr">extraResources</span>: [],
    <span class="hljs-attr">electronDownload</span>: &#123;
      <span class="hljs-attr">mirror</span>: <span class="hljs-string">"https://npm.taobao.org/mirrors/electron/"</span>
    &#125;,
    <span class="hljs-attr">dmg</span>: &#123;
      <span class="hljs-attr">contents</span>: [
        &#123;
          <span class="hljs-attr">type</span>: <span class="hljs-string">"link"</span>,
          <span class="hljs-attr">path</span>: <span class="hljs-string">"/Applications"</span>,
          <span class="hljs-attr">x</span>: <span class="hljs-number">410</span>,
          <span class="hljs-attr">y</span>: <span class="hljs-number">150</span>
        &#125;,
        &#123;
          <span class="hljs-attr">type</span>: <span class="hljs-string">"file"</span>,
          <span class="hljs-attr">x</span>: <span class="hljs-number">130</span>,
          <span class="hljs-attr">y</span>: <span class="hljs-number">150</span>
        &#125;
      ]
    &#125;,
    <span class="hljs-attr">mac</span>: &#123;
      <span class="hljs-attr">icon</span>: <span class="hljs-string">"public/icons/icon.icns"</span>
    &#125;,
    <span class="hljs-attr">nsis</span>: &#123;
      <span class="hljs-attr">oneClick</span>: <span class="hljs-literal">false</span>,
      <span class="hljs-attr">perMachine</span>: <span class="hljs-literal">true</span>,
      <span class="hljs-attr">allowToChangeInstallationDirectory</span>: <span class="hljs-literal">true</span>,
      <span class="hljs-attr">warningsAsErrors</span>: <span class="hljs-literal">false</span>,
      <span class="hljs-attr">allowElevation</span>: <span class="hljs-literal">false</span>,
      <span class="hljs-attr">createDesktopShortcut</span>: <span class="hljs-literal">true</span>,
      <span class="hljs-attr">createStartMenuShortcut</span>: <span class="hljs-literal">true</span>
    &#125;,
    <span class="hljs-attr">win</span>: &#123;
      <span class="hljs-attr">target</span>: <span class="hljs-string">"nsis"</span>,
      <span class="hljs-attr">icon</span>: <span class="hljs-string">"public/icons/icon.ico"</span>,
      <span class="hljs-attr">requestedExecutionLevel</span>: <span class="hljs-string">"highestAvailable"</span>
    &#125;,
    <span class="hljs-attr">linux</span>: &#123;
      <span class="hljs-string">"icon"</span>: <span class="hljs-string">"public/icons"</span>
    &#125;,
    <span class="hljs-attr">publish</span>: &#123;
      <span class="hljs-attr">provider</span>: <span class="hljs-string">"generic"</span>,
      <span class="hljs-attr">url</span>: <span class="hljs-string">"http://127.0.0.1"</span>
    &#125;
  &#125;
  ............
&#125;

<span class="copy-code-btn">复制代码</span></code></pre>
<p>builderOptions是electron的打包配置，参考<a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.electron.build%2Fconfiguration%2Fconfiguration" target="_blank" rel="nofollow noopener noreferrer" title="https://www.electron.build/configuration/configuration" ref="nofollow noopener noreferrer">链接</a>，之前打包的话由于网络原因，下载electron包可能会下载失败或特慢，这里配置electronDownload为淘宝源，本来electron的name及version是读取package.json里面的值的，这里使用extraMetadata把这两个值注入进package.json，其他配置可自行修改。</p>
<h3 data-id="heading-11">icons</h3>
<p>打包是需要icons的，windows呢需要.ico，mac需要icns，你可以使用icofx进行生成(后续有时间的话会补充)，这里呢我使用的是一个插件直接生成的</p>
<pre><code class="copyable">yarn add -D electron-icon-builder
package.json添加
"icons": "electron-icon-builder --input=./public/icons/icon.png --output=public --flatten",
<span class="copy-code-btn">复制代码</span></code></pre>
<p>在public下新建icons文件夹，再把你的icon.png(512*512)放在里面，运行npm run icons就会在icons里面生成对应的图片了。</p>
<p>最后：运行打包命令，分别打dev，test，prod包安装，打开软件查看打印的cfg是否正确。</p>
<h3 data-id="heading-12">补充</h3>
<p>如果使用npm install或yarn install出现错误时，一般来说是网络问题，先删除node_modules，严格按照安装步骤来，重新npm install</p>
<p>本文源码gitee地址：<a href="https://link.juejin.cn/?target=https%3A%2F%2Fgitee.com%2Fldlw%2Felectron-vue-cli" target="_blank" rel="nofollow noopener noreferrer" title="https://gitee.com/ldlw/electron-vue-cli" ref="nofollow noopener noreferrer">gitee.com/ldlw/electr…</a></p>
<p>关注作者： 微信搜【学好前端】公众号，即可以获取作者微信，加技术交流群</p></div>  
</div>
            