
---
title: '80行代码教你写一个Webpack插件并发布到npm'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/c5d45138dcf9445392ff2bffbfaffc4f~tplv-k3u1fbpfcp-zoom-1.image'
author: 掘金
comments: false
date: Sat, 22 May 2021 18:27:29 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/c5d45138dcf9445392ff2bffbfaffc4f~tplv-k3u1fbpfcp-zoom-1.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h2 data-id="heading-0">前言</h2>
<p>最近在学习 <code>Webpack</code> 相关的原理，以前只知道 Webpack 的配置方法，但并不知道其内部流程，经过一轮的学习，感觉获益良多，为了巩固学习的内容，我决定尝试自己动手写一个插件。</p>
<p>这个插件实现的功能比较简单：</p>
<ul>
<li>默认清除 <code>js</code> 代码中的 <code>console.log</code> 的打印输出；</li>
<li>可通过传入配置，实现移除 <code>console</code> 的其它方法，如 <code>console.warn</code>、<code>console.error</code> 等；</li>
</ul>
<h2 data-id="heading-1">Webpack 的构建流程以及 plugin 的原理</h2>
<h4 data-id="heading-2">Webpack 构建流程</h4>
<p><code>Webpack</code> 的主要构建流程，可以分为三个阶段:</p>
<ul>
<li><strong>初始化阶段</strong>：启动构建，读取与合并配置参数，加载 <code>Plugin</code>，实例化 <code>Compiler</code>。</li>
<li><strong>编译阶段</strong>：从 <code>Entry</code> 发出，针对每个 <code>Module</code> 串行调用对应的 <code>Loader</code> 去翻译文件内容，再找到该 <code>Module</code> 依赖的 <code>Module</code>，递归地进行编译处理。</li>
<li><strong>生成阶段</strong>：对编译后的 <code>Module</code> 组合成 <code>Chunk</code>，把 <code>Chunk</code> 转换成文件，输出到文件系统。</li>
</ul>
<p>如果 <code>Webpack</code> 打包生产环境文件时，只会执行一次构建，以上阶段会按顺序执行一遍。但是在开启监听模式时，如开发环境，Webpack 会持续的进行构建。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/c5d45138dcf9445392ff2bffbfaffc4f~tplv-k3u1fbpfcp-zoom-1.image" alt="webpack流程图.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h4 data-id="heading-3">plugin 原理</h4>
<p><code>Webpack</code> 插件通常是一个带有 <code>apply</code> 函数的类，其中 <code>constructor</code> 可以接收传入的配置项。插件被安装时，<code>apply</code> 函数会被调用一次，并接收 <code>Compiler</code> 对象，然后我们可以在 <code>Compiler</code> 对象上监听不同的事件钩子，从而进行插件功能的开发。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// 定义一个插件</span>
<span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">MyPlugin</span> </span>&#123;
  <span class="hljs-comment">// 构造函数，接收插件的配置项 options </span>
  <span class="hljs-function"><span class="hljs-title">constructor</span>(<span class="hljs-params">options</span>)</span> &#123;
    <span class="hljs-comment">// 获取配置项，初始化插件</span>
  &#125;

  <span class="hljs-comment">// 插件安装时会调用 apply，并传入 compiler</span>
  <span class="hljs-function"><span class="hljs-title">apply</span>(<span class="hljs-params">compiler</span>)</span> &#123;
    <span class="hljs-comment">// 获取 comolier 独享，可以监听事件钩子</span>
    <span class="hljs-comment">// 功能开发 ... </span>
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-4">compiler 和 compilation 对象</h4>
<p>在开发 <code>Plugin</code> 过程中最常用的两个对象就是 <code>Compiler</code> 和 <code>Compilation</code>：</p>
<ul>
<li><code>Compiler</code> 对象在 <code>Webpack</code> 启动时被实例化，该对象包含了 <code>Webpack</code> 环境所有的配置信息，包括 <code>options</code>、<code>loaders</code>、<code>plugins</code> 等。在整个 <code>Webpack</code> 构建过程中，<code>Compiler</code> 对象是全局唯一的， 它提供了很多事件钩子回调供插件使用。</li>
<li><code>Compilation</code> 对象包含了当前的模块资源、编译生成资源、变化的文件等。<code>Compilation</code> 对象在 <code>Webpack</code> 构建过程中并不是唯一的，如果在开发模式下 <code>Webpack</code> 开启了文件检测功能，每当文件变化时，<code>Webpack</code> 会重新构建，此时会生成一个新的 <code>Compilation</code> 对象。<code>Compilation</code> 对象也提供了很多事件回调供插件做扩展。</li>
</ul>
<h2 data-id="heading-5">插件开发</h2>
<h4 data-id="heading-6">项目目录</h4>
<p>该插件实现的功能比较简单，文件目录也不复杂。首先新建一个空文件夹 <code>remove-console-Webpack-plugin</code>，并在该文件夹目录下运行 <code>npm init</code>，根据提示来填写 <code>package.json</code> 相关信息。然后再新建一个 <code>src</code> 文件夹，插件主要代码就放在 <code>src/index.js</code> 里面。如果你需要把项目放到 <code>github</code> 上，最好也添加一下 <code>.gitignore</code>、<code>README.md</code> 等文件。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// remove-console-Webpack-plugin</span>
├─src
│  └─index.js  
├─.gitignore
├─package.json
└─README.md 
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-7">插件代码</h4>
<p>插件代码逻辑也并不复杂，主要有几点：</p>
<ol>
<li>在构造函数中接收配置参数，并对参数进行合并，得到需要清除的 <code>console </code> 函数, 存放在 <code>removed</code> 数组中；</li>
<li>在 <code>apply</code> 函数中监听 <code>compiler.hook.compilation</code> 钩子，该钩子触发后，拿到 <code>compilation</code> 后进一步监听它的钩子，这里 <code>Webpack4</code> 和 <code>Webpack5</code> 的钩子不一样，需要做兼容；</li>
<li>定义 <code>assetsHandler</code> 方法来处理 <code>js</code> 文件，利用正则表达式清除 <code>removed</code> 中包括的 <code>console</code> 函数；</li>
</ol>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">RemoveConsoleWebpackPlugin</span> </span>&#123;
  <span class="hljs-comment">// 构造函数接受配置参数</span>
  <span class="hljs-function"><span class="hljs-title">constructor</span>(<span class="hljs-params">options</span>)</span> &#123;
    <span class="hljs-keyword">let</span> include = options && options.include;
    <span class="hljs-keyword">let</span> removed = [<span class="hljs-string">'log'</span>]; <span class="hljs-comment">// 默认清除的方法</span>

    <span class="hljs-keyword">if</span> (include) &#123;
      <span class="hljs-keyword">if</span> (!<span class="hljs-built_in">Array</span>.isArray(include)) &#123;
        <span class="hljs-built_in">console</span>.error(<span class="hljs-string">'options.include must be an Array.'</span>);
      &#125; <span class="hljs-keyword">else</span> <span class="hljs-keyword">if</span> (include.includes(<span class="hljs-string">'*'</span>)) &#123;
        <span class="hljs-comment">// 传入 * 表示清除所有 console 的方法</span>
        removed = <span class="hljs-built_in">Object</span>.keys(<span class="hljs-built_in">console</span>).filter(<span class="hljs-function"><span class="hljs-params">fn</span> =></span> &#123;
          <span class="hljs-keyword">return</span> <span class="hljs-keyword">typeof</span> <span class="hljs-built_in">console</span>[fn] === <span class="hljs-string">'function'</span>;
        &#125;)
      &#125; <span class="hljs-keyword">else</span> &#123;
        removed = include; <span class="hljs-comment">// 根据传入配置覆盖</span>
      &#125;
    &#125;

    <span class="hljs-built_in">this</span>.removed = removed;
  &#125;

  <span class="hljs-comment">// Webpack 会调用插件实例的 apply 方法，并传入compiler 对象</span>
  <span class="hljs-function"><span class="hljs-title">apply</span>(<span class="hljs-params">compiler</span>)</span> &#123;
    <span class="hljs-comment">// js 资源代码处理函数</span>
    <span class="hljs-keyword">let</span> assetsHandler = <span class="hljs-function">(<span class="hljs-params">assets, compilation</span>) =></span> &#123;
      <span class="hljs-keyword">let</span> removedStr = <span class="hljs-built_in">this</span>.removed.reduce(<span class="hljs-function">(<span class="hljs-params">a, b</span>) =></span> (a + <span class="hljs-string">'|'</span> + b));

      <span class="hljs-keyword">let</span> reDict = &#123;
        <span class="hljs-number">1</span>: [<span class="hljs-built_in">RegExp</span>(<span class="hljs-string">`\\.console\\.(<span class="hljs-subst">$&#123;removedStr&#125;</span>)\\(\\)`</span>, <span class="hljs-string">'g'</span>), <span class="hljs-string">''</span>],
        <span class="hljs-number">2</span>: [<span class="hljs-built_in">RegExp</span>(<span class="hljs-string">`\\.console\\.(<span class="hljs-subst">$&#123;removedStr&#125;</span>)\\(`</span>, <span class="hljs-string">'g'</span>), <span class="hljs-string">';('</span>],
        <span class="hljs-number">3</span>: [<span class="hljs-built_in">RegExp</span>(<span class="hljs-string">`console\\.(<span class="hljs-subst">$&#123;removedStr&#125;</span>)\\(\\)`</span>, <span class="hljs-string">'g'</span>), <span class="hljs-string">''</span>],
        <span class="hljs-number">4</span>: [<span class="hljs-built_in">RegExp</span>(<span class="hljs-string">`console\\.(<span class="hljs-subst">$&#123;removedStr&#125;</span>)\\(`</span>, <span class="hljs-string">'g'</span>), <span class="hljs-string">'('</span>]
      &#125;

      <span class="hljs-built_in">Object</span>.entries(assets).forEach(<span class="hljs-function">(<span class="hljs-params">[filename, source]</span>) =></span> &#123;
        <span class="hljs-comment">// 匹配js文件</span>
        <span class="hljs-keyword">if</span> (<span class="hljs-regexp">/\.js$/</span>.test(filename)) &#123;
          <span class="hljs-comment">// 处理前文件内容</span>
          <span class="hljs-keyword">let</span> outputContent = source.source();

          <span class="hljs-built_in">Object</span>.keys(reDict).forEach(<span class="hljs-function"><span class="hljs-params">i</span> =></span> &#123;
            <span class="hljs-keyword">let</span> [re, s] = reDict[i];
            outputContent = outputContent.replace(re, s);
          &#125;)

          compilation.assets[filename] = &#123;
            <span class="hljs-comment">// 返回文件内容</span>
            <span class="hljs-attr">source</span>: <span class="hljs-function">() =></span> &#123;
              <span class="hljs-keyword">return</span> outputContent
            &#125;,
            <span class="hljs-comment">// 返回文件大小</span>
            <span class="hljs-attr">size</span>: <span class="hljs-function">() =></span> &#123;
              <span class="hljs-keyword">return</span> Buffer.byteLength(outputContent, <span class="hljs-string">'utf8'</span>)
            &#125;
          &#125;
        &#125;
      &#125;)
    &#125;

    <span class="hljs-comment">/**
     * 通过 compiler.hooks.compilation.tap 监听事件
     * 在回调方法中获取到 compilation 对象
     */</span>
    compiler.hooks.compilation.tap(<span class="hljs-string">'RemoveConsoleWebpackPlugin'</span>,
      <span class="hljs-function"><span class="hljs-params">compilation</span> =></span> &#123;
        <span class="hljs-comment">// Webpack 5</span>
        <span class="hljs-keyword">if</span> (compilation.hooks.processAssets) &#123;
          compilation.hooks.processAssets.tap(
            &#123; <span class="hljs-attr">name</span>: <span class="hljs-string">'RemoveConsoleWebpackPlugin'</span> &#125;,
            <span class="hljs-function"><span class="hljs-params">assets</span> =></span> assetsHandler(assets, compilation)
          );
        &#125; <span class="hljs-keyword">else</span> <span class="hljs-keyword">if</span> (compilation.hooks.optimizeAssets) &#123;
          <span class="hljs-comment">// Webpack 4</span>
          compilation.hooks.optimizeAssets.tap(
            <span class="hljs-string">'RemoveConsoleWebpackPlugin'</span>, 
            <span class="hljs-function"><span class="hljs-params">assets</span> =></span> assetsHandler(assets, compilation)
          );
        &#125;
      &#125;)
  &#125;
&#125;

<span class="hljs-comment">// export Plugin</span>
<span class="hljs-built_in">module</span>.exports = RemoveConsoleWebpackPlugin;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-8">发布到npm</h2>
<p>希望别人能使用到你的插件，就需要把插件发布到 <code>npm</code> 上，发布的主要流程：</p>
<ol>
<li>首先在 <code>npm</code> 官网上注册账号，然后打开命令行工具，在任意目录下输入 <code>npm login</code> 并按提示登录；</li>
</ol>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/8215cf8d96704809b04c8e89fbda78f8~tplv-k3u1fbpfcp-zoom-1.image" alt="npm login.png" loading="lazy" referrerpolicy="no-referrer"></p>
<ol start="2">
<li>登录后可用 <code>npm whoami</code> 查看是否登录成功；</li>
</ol>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/ee1861f5123c4889a3e52c3cabbfb4a9~tplv-k3u1fbpfcp-zoom-1.image" alt="npm whoami.png" loading="lazy" referrerpolicy="no-referrer"></p>
<ol start="3">
<li>发布前检查一下根目录下的 <code>package.json</code> 文件信息是否填写正确，主要字段：</li>
</ol>
<p><strong>name</strong>：决定用户下载你的插件时用的名称，不可与 <code>npm</code> 上已有的第三方包重名，否则无法发布；<br>
<strong>main</strong>：插件主文件入口，<code>Webpack</code> 引入插件时，就从该目录导入；<br>
<strong>version</strong>：每次更新发布时，需要与上一版本的版本号不一样，否则上传不成功；<br>
<strong>repository</strong>：如果你的插件代码放在 <code>github</code>、<code>gitee</code> 等网站，可以填一下；<br>
<strong>private</strong>：不能设置为 <code>true</code>，否则无法发布；</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/1587ac76cae24eb0ae1c8e827e2941e1~tplv-k3u1fbpfcp-zoom-1.image" alt="package_json.png" loading="lazy" referrerpolicy="no-referrer"></p>
<ol start="4">
<li>一切准备就绪后，切换到插件所在的目录下，运行 <code>npm publish</code> 即可上传插件；</li>
</ol>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/9ec61f460d42443a84918ca872d2ca4c~tplv-k3u1fbpfcp-zoom-1.image" alt="npm publish.png" loading="lazy" referrerpolicy="no-referrer"></p>
<ol start="5">
<li>上传成功后，到 <code>npm</code> 官网上搜索，看看是否能搜到插件；</li>
</ol>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/42dc716bc5e448779bf37431e1ee156b~tplv-k3u1fbpfcp-watermark.image" alt="npm search.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-9">结尾</h2>
<p>本文是我学习了 <code>Webpack</code> 原理并开发了一个小插件后的总结，由于 Webpack 的内容实在太多了，所以可能会有理解不到位的地方，还请大佬们多多指正。另外，如果这篇文章对你有帮助，可以给我点个赞，或者给<a target="_blank" href="https://github.com/Yuan-Yiming/remove-console-Webpack-plugin" rel="nofollow noopener noreferrer">我的插件项目</a>点个star，你的鼓励是我最大的动力哈~</p></div>  
</div>
            