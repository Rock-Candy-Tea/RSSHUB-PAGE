
---
title: '仅需5分钟构建 Vue 3 桌面应用程序'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/be37a8d2100048c79184f90e41b2a922~tplv-k3u1fbpfcp-zoom-1.image'
author: 掘金
comments: false
date: Tue, 18 May 2021 02:06:15 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/be37a8d2100048c79184f90e41b2a922~tplv-k3u1fbpfcp-zoom-1.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>在本文中，我们将研究如何通过 Vite 开发 Vue 3 桌面项目。</p>
<p>在项目中会用到 <a href="https://www.electronjs.org/" target="_blank" rel="nofollow noopener noreferrer">Electron</a> ， 一种最流行的框架，可使用Javascript构建跨平台的桌面应用程序。 因此，许多受欢迎的应用程序都在使用Electron，例如VSCode，Slack，Twitch等。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/be37a8d2100048c79184f90e41b2a922~tplv-k3u1fbpfcp-zoom-1.image" alt="img" loading="lazy" referrerpolicy="no-referrer"></p>
<p>先看看要做什么：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/211b728cc59b4a738530ca674a270605~tplv-k3u1fbpfcp-zoom-1.image" alt="img" loading="lazy" referrerpolicy="no-referrer"></p>
<p>尽管这只是一个 Vite 的基本模板，但它跑在专用程序而不是浏览器中。 这是构建自己的桌面应用的必要步骤。</p>
<p>以下是开发过程。</p>
<h2 data-id="heading-0">创建的基本 Vite 程序</h2>
<p>首先创建 Vite 应用。 在这里不会过多介绍 Vite 的工作原理。</p>
<p>在终端下执行以下命令：</p>
<pre><code class="hljs language-bash copyable" lang="bash">npm init @vitejs/app
<span class="hljs-built_in">cd</span> [project-name]
npm install
<span class="copy-code-btn">复制代码</span></code></pre>
<p>完成了，先在浏览器中试一下。</p>
<p>在终端中简单的运行 <code>npm run dev</code> 命令。然后在浏览器中打开本机地址，可以看到是这样的：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/8c519c9bf27d4f758dbe85882541717a~tplv-k3u1fbpfcp-zoom-1.image" alt="img" loading="lazy" referrerpolicy="no-referrer"></p>
<p>没有问题，接着就该把 Electron 添加到它的设置中了。</p>
<h2 data-id="heading-1">在 Vite 项目中添加 Electron</h2>
<p>这里按照 <a href="https://www.electronjs.org/docs/tutorial/quick-start" target="_blank" rel="nofollow noopener noreferrer">Electron 官方的 quick start</a> 在我们的 Vite 应用中进行一些调整。</p>
<p>首先安装 Electron。在终端下输入以下命令：</p>
<pre><code class="hljs language-bash copyable" lang="bash">Install Electronnpm install --save-dev electron
<span class="copy-code-btn">复制代码</span></code></pre>
<p>接着再看一下 Electron 手册。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/01ed8bab1b114a2fa4119965388291c4~tplv-k3u1fbpfcp-zoom-1.image" alt="img" loading="lazy" referrerpolicy="no-referrer"></p>
<p>手册上说简单的 Electron 配置需要四个文件：</p>
<ol>
<li><code>package.json</code> —— 这个已经有了</li>
<li><code>main.js </code></li>
<li><code>preloader.js</code></li>
<li><code>index.html</code></li>
</ol>
<p>看上去项目中已经有了 <code>main.js</code>和<code>index.html</code>文件，但它们是 Vite 的文件，而不是 Electron 的文件。 Vite 的文件只能用于运行 Vite 程序，所以还需要提供单独的 Electron 文件。</p>
<p><code>main.js</code> 用于创建桌面程序并加载到 <code>index.html</code> 中，它还应该包括我们构建的 Vite 程序代码。</p>
<h2 data-id="heading-2">构建 Vite 程序</h2>
<p>所以首先必须构建 Vite 程序。 因为要把它与 Electron 进行整合，所以还需要做一些额外的配置。我们要确保在构建项目时，对最终 javascript 和 css 文件的所有引用都指向正确的路径。</p>
<p>要构建的 Vite 项目将会创建以下结构的 dist 目录。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/ba392c2e33e042d486870372c71c0009~tplv-k3u1fbpfcp-zoom-1.image" alt="img" loading="lazy" referrerpolicy="no-referrer"></p>
<p>但是由于我们的 Electron 代码位于项目的根目录中，所以应该将整个项目的基础设置为 dist 文件夹。 可以通过 <code>path</code> 库在 <code>vite.config.js</code> 文件中设置 <code>base</code> 属性来实现。</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">//vite.config.js</span>
<span class="hljs-keyword">import</span> &#123; defineConfig &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'vite'</span>
<span class="hljs-keyword">import</span> vue <span class="hljs-keyword">from</span> <span class="hljs-string">'@vitejs/plugin-vue'</span>
<span class="hljs-keyword">const</span> path = <span class="hljs-built_in">require</span>(<span class="hljs-string">'path'</span>)

<span class="hljs-comment">// https://vitejs.dev/config/</span>
<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> defineConfig(&#123;
  <span class="hljs-attr">base</span>: path.resolve(__dirname, <span class="hljs-string">'./dist/'</span>),
  <span class="hljs-attr">plugins</span>: [vue()]
&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>现在可以在终端中运行 <code>npm run build</code> 来创建 dist 目录了。</p>
<h2 data-id="heading-3">设置 Electron 的 main.js</h2>
<p>下一步是在项目的根目录中创建 <code>main.js</code> 文件。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/711d66c9bb3f4400abb0820a56dfb29b~tplv-k3u1fbpfcp-zoom-1.image" alt="img" loading="lazy" referrerpolicy="no-referrer"></p>
<p>创建完毕后我们只需要从 <a href="https://www.electronjs.org/docs/tutorial/quick-start#create-the-main-script-file" target="_blank" rel="nofollow noopener noreferrer">Electron quick start guide</a> 中复制粘贴代码就行了。</p>
<p>在我们加载 <code>index.html</code> 的地方，要将其改为 <code>dist/index.html</code>，以便在 dist 目录中使用该文件。</p>
<p>所以 <code>main.js</code> 中的最终代码是这样：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">//main.js</span>
<span class="hljs-keyword">const</span> &#123; app, BrowserWindow &#125; = <span class="hljs-built_in">require</span>(<span class="hljs-string">'electron'</span>)
<span class="hljs-keyword">const</span> path = <span class="hljs-built_in">require</span>(<span class="hljs-string">'path'</span>)

<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">createWindow</span> (<span class="hljs-params"></span>) </span>&#123;
  <span class="hljs-keyword">const</span> win = <span class="hljs-keyword">new</span> BrowserWindow(&#123;
    <span class="hljs-attr">width</span>: <span class="hljs-number">800</span>,
    <span class="hljs-attr">height</span>: <span class="hljs-number">600</span>,
    <span class="hljs-attr">webPreferences</span>: &#123;
      <span class="hljs-attr">preload</span>: path.join(__dirname, <span class="hljs-string">'preload.js'</span>)
    &#125;
  &#125;)

  win.loadFile(<span class="hljs-string">'dist/index.html'</span>)
&#125;

app.whenReady().then(<span class="hljs-function">() =></span> &#123;
  createWindow()

  app.on(<span class="hljs-string">'activate'</span>, <span class="hljs-function">() =></span> &#123;
    <span class="hljs-keyword">if</span> (BrowserWindow.getAllWindows().length === <span class="hljs-number">0</span>) &#123;
      createWindow()
    &#125;
  &#125;)
&#125;)

app.on(<span class="hljs-string">'window-all-closed'</span>, <span class="hljs-function">() =></span> &#123;
  <span class="hljs-keyword">if</span> (process.platform !== <span class="hljs-string">'darwin'</span>) &#123;
    app.quit()
  &#125;
&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-4">创建并编写 preload.js.</h2>
<p>接下来让在项目根目录中创建 <code>preload.js</code> 文件，然后再次使用<a href="https://www.electronjs.org/docs/tutorial/quick-start#define-a-preload-script" target="_blank" rel="nofollow noopener noreferrer">quick start code</a>，这次不必修改任何内容。</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">//preload.js</span>
<span class="hljs-built_in">window</span>.addEventListener(<span class="hljs-string">'DOMContentLoaded'</span>, <span class="hljs-function">() =></span> &#123;
    <span class="hljs-keyword">const</span> replaceText = <span class="hljs-function">(<span class="hljs-params">selector, text</span>) =></span> &#123;
      <span class="hljs-keyword">const</span> element = <span class="hljs-built_in">document</span>.getElementById(selector)
      <span class="hljs-keyword">if</span> (element) element.innerText = text
    &#125;
  
    <span class="hljs-keyword">for</span> (<span class="hljs-keyword">const</span> type <span class="hljs-keyword">of</span> [<span class="hljs-string">'chrome'</span>, <span class="hljs-string">'node'</span>, <span class="hljs-string">'electron'</span>]) &#123;
      replaceText(<span class="hljs-string">`<span class="hljs-subst">$&#123;type&#125;</span>-version`</span>, process.versions[type])
    &#125;
&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-5">修改 package.json</h2>
<p>差不多快要完成了，最后还需要对 package.json文件进行一些修改，以便运行 Electron 命令。</p>
<p>首先要设置 <code>main</code> 属性，在默认情况下，Electron 会在根目录中查找 <code>index.js</code> 文件并执行，但是由于我们的文件名为 <code>main.js</code>，所以需要在 <code>package.json</code> 中定义。</p>
<pre><code class="hljs language-json copyable" lang="json"><span class="hljs-comment">//package.json</span>
&#123;
  <span class="hljs-attr">"name"</span>: <span class="hljs-string">"vite-electron"</span>,
  <span class="hljs-attr">"version"</span>: <span class="hljs-string">"0.0.0"</span>,
  <span class="hljs-attr">"main"</span>: <span class="hljs-string">"main.js"</span>, <span class="hljs-comment">// 这一行</span>
  ...
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>然后设置运行 Electron 的方式，在 <code>scripts</code> 部分中新创建一个名为<code>electron:start</code>  的脚本，内容是<code>electron . </code>。</p>
<pre><code class="hljs language-json copyable" lang="json"><span class="hljs-comment">//package.json</span>
&#123;
  <span class="hljs-attr">"name"</span>: <span class="hljs-string">"vite-electron"</span>,
  <span class="hljs-attr">"version"</span>: <span class="hljs-string">"0.0.0"</span>,
  <span class="hljs-attr">"main"</span>: <span class="hljs-string">"main.js"</span>,
  <span class="hljs-attr">"scripts"</span>: &#123;
    <span class="hljs-attr">"dev"</span>: <span class="hljs-string">"vite"</span>,
    <span class="hljs-attr">"build"</span>: <span class="hljs-string">"vite build"</span>,
    <span class="hljs-attr">"serve"</span>: <span class="hljs-string">"vite preview"</span>,
    <span class="hljs-attr">"electron:start"</span>: <span class="hljs-string">"electron ."</span> <span class="hljs-comment">// 这里</span>
  &#125;,
  ...
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>以上就是所有的代码了。</p>
<p>最后在终端中执行： <code>npm run electron:start</code> 命令，然后就能看到：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/2a7a0b1ff8c2484d9e9fc7d9f9aa4d7e~tplv-k3u1fbpfcp-zoom-1.image" alt="img" loading="lazy" referrerpolicy="no-referrer"></p>
<p>桌面程序终于完成了，很简单吧～</p>
<h2 data-id="heading-6">写在最后</h2>
<p>近期在提升 Vue 的过程中，发现一个高逼格的 Vue3+TS 教程。
无偿分享给掘仔们，<a href="https://www.bilibili.com/video/BV1gf4y1W783" target="_blank" rel="nofollow noopener noreferrer">戳我看教程</a></p></div>  
</div>
            