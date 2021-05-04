
---
title: '【重拾落叶】深入浅出Webpack核心机制Loader、Plugin到彩蛋原理分析'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=1098'
author: 掘金
comments: false
date: Mon, 03 May 2021 07:06:30 GMT
thumbnail: 'https://picsum.photos/400/300?random=1098'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h1 data-id="heading-0">前言</h1>
<p>一起深入Wepcak , 尽管 Vite 非常火爆<code>确实很香</code>,但是 Webpack 依然在企业占据主导地位<code>以后我也不知道</code>, 学习深入非常有必要，主要介绍loader / plugin 和原理分析，而那些配置只介绍部分常用的，我希望您能学会看文档，中文 or 英文<code>我看不懂，以后必学</code></p>
<h1 data-id="heading-1">所以</h1>
<p>一位程序员的职业生涯大约十年，只有人寿命的十分之一。前端项目只是你生活工作的一部分，而你却是它的全部，你是他的灵魂。请放下长时间的游戏、工作时的摸鱼。多学习来以最完美的状态好好陪你项目！</p>
<h1 data-id="heading-2">正文</h1>
<p>文章底部小彩蛋，请你一步一步看过去！！</p>
<h2 data-id="heading-3">知识点</h2>
<ul>
<li>Webpack 前置基础</li>
<li>Loader 机制（手写一个）</li>
<li>Plugin 机制</li>
<li>小彩蛋（介绍部分Webpack原理分析）</li>
</ul>
<h3 data-id="heading-4">Webpack 前置基础（配置）</h3>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">const</span> path = <span class="hljs-built_in">require</span>(<span class="hljs-string">'path'</span>);

<span class="hljs-built_in">module</span>.exports = &#123;
  <span class="hljs-attr">mode</span>: <span class="hljs-string">"production"</span>, <span class="hljs-comment">// "production" | "development" | "none"</span>
  <span class="hljs-comment">// Chosen mode tells webpack to use its built-in optimizations accordingly.</span>

  <span class="hljs-attr">entry</span>: <span class="hljs-string">"./app/entry"</span>, <span class="hljs-comment">// string | object | array</span>
  <span class="hljs-comment">// 这里应用程序开始执行</span>
  <span class="hljs-comment">// webpack 开始打包</span>

  <span class="hljs-attr">output</span>: &#123;
    <span class="hljs-comment">// webpack 如何输出结果的相关选项</span>

    <span class="hljs-attr">path</span>: path.resolve(__dirname, <span class="hljs-string">"dist"</span>), <span class="hljs-comment">// string</span>
    <span class="hljs-comment">// 所有输出文件的目标路径</span>
    <span class="hljs-comment">// 必须是绝对路径（使用 Node.js 的 path 模块）</span>

    <span class="hljs-attr">filename</span>: <span class="hljs-string">"bundle.js"</span>, <span class="hljs-comment">// string</span>
    <span class="hljs-comment">// 「入口分块(entry chunk)」的文件名模板（出口分块？）</span>

    <span class="hljs-attr">publicPath</span>: <span class="hljs-string">"/assets/"</span>, <span class="hljs-comment">// string</span>
    <span class="hljs-comment">// 输出解析文件的目录，url 相对于 HTML 页面</span>

    <span class="hljs-attr">library</span>: <span class="hljs-string">"MyLibrary"</span>, <span class="hljs-comment">// string,</span>
    <span class="hljs-comment">// 导出库(exported library)的名称</span>

    <span class="hljs-attr">libraryTarget</span>: <span class="hljs-string">"umd"</span>, <span class="hljs-comment">// 通用模块定义</span>
    <span class="hljs-comment">// 导出库(exported library)的类型</span>

    <span class="hljs-comment">/* 高级输出配置（点击显示） */</span>
  &#125;,

  <span class="hljs-attr">module</span>: &#123;
    <span class="hljs-comment">// 关于模块配置</span>

    <span class="hljs-attr">rules</span>: [
      <span class="hljs-comment">// 模块规则（配置 loader、解析器等选项）</span>

      &#123;
        <span class="hljs-attr">test</span>: <span class="hljs-regexp">/\.jsx?$/</span>,
        include: [
          path.resolve(__dirname, <span class="hljs-string">"app"</span>)
        ],
        <span class="hljs-attr">exclude</span>: [
          path.resolve(__dirname, <span class="hljs-string">"app/demo-files"</span>)
        ],
        <span class="hljs-comment">// 这里是匹配条件，每个选项都接收一个正则表达式或字符串</span>
        <span class="hljs-comment">// test 和 include 具有相同的作用，都是必须匹配选项</span>
        <span class="hljs-comment">// exclude 是必不匹配选项（优先于 test 和 include）</span>
        <span class="hljs-comment">// 最佳实践：</span>
        <span class="hljs-comment">// - 只在 test 和 文件名匹配 中使用正则表达式</span>
        <span class="hljs-comment">// - 在 include 和 exclude 中使用绝对路径数组</span>
        <span class="hljs-comment">// - 尽量避免 exclude，更倾向于使用 include</span>

        <span class="hljs-attr">issuer</span>: &#123; test, include, exclude &#125;,
        <span class="hljs-comment">// issuer 条件（导入源）</span>

        <span class="hljs-attr">enforce</span>: <span class="hljs-string">"pre"</span>,
        <span class="hljs-attr">enforce</span>: <span class="hljs-string">"post"</span>,
        <span class="hljs-comment">// 标识应用这些规则，即使规则覆盖（高级选项）</span>

        <span class="hljs-attr">loader</span>: <span class="hljs-string">"babel-loader"</span>,
        <span class="hljs-comment">// 应该应用的 loader，它相对上下文解析</span>
        <span class="hljs-comment">// 为了更清晰，`-loader` 后缀在 webpack 2 中不再是可选的</span>
        <span class="hljs-comment">// 查看 webpack 1 升级指南。</span>

        <span class="hljs-attr">options</span>: &#123;
          <span class="hljs-attr">presets</span>: [<span class="hljs-string">"es2015"</span>]
        &#125;,
        <span class="hljs-comment">// loader 的可选项</span>
      &#125;,

      &#123;
        <span class="hljs-attr">test</span>: <span class="hljs-regexp">/\.html$/</span>,
        test: <span class="hljs-string">"\.html$"</span>

        <span class="hljs-attr">use</span>: [
          <span class="hljs-comment">// 应用多个 loader 和选项</span>
          <span class="hljs-string">"htmllint-loader"</span>,
          &#123;
            <span class="hljs-attr">loader</span>: <span class="hljs-string">"html-loader"</span>,
            <span class="hljs-attr">options</span>: &#123;
              <span class="hljs-comment">/* ... */</span>
            &#125;
          &#125;
        ]
      &#125;,

      &#123; <span class="hljs-attr">oneOf</span>: [ <span class="hljs-comment">/* rules */</span> ] &#125;,
      <span class="hljs-comment">// 只使用这些嵌套规则之一</span>

      &#123; <span class="hljs-attr">rules</span>: [ <span class="hljs-comment">/* rules */</span> ] &#125;,
      <span class="hljs-comment">// 使用所有这些嵌套规则（合并可用条件）</span>

      &#123; <span class="hljs-attr">resource</span>: &#123; <span class="hljs-attr">and</span>: [ <span class="hljs-comment">/* 条件 */</span> ] &#125; &#125;,
      <span class="hljs-comment">// 仅当所有条件都匹配时才匹配</span>

      &#123; <span class="hljs-attr">resource</span>: &#123; <span class="hljs-attr">or</span>: [ <span class="hljs-comment">/* 条件 */</span> ] &#125; &#125;,
      &#123; <span class="hljs-attr">resource</span>: [ <span class="hljs-comment">/* 条件 */</span> ] &#125;,
      <span class="hljs-comment">// 任意条件匹配时匹配（默认为数组）</span>

      &#123; <span class="hljs-attr">resource</span>: &#123; <span class="hljs-attr">not</span>: <span class="hljs-comment">/* 条件 */</span> &#125; &#125;
      <span class="hljs-comment">// 条件不匹配时匹配</span>
    ],

    <span class="hljs-comment">/* 高级模块配置（点击展示） */</span>
  &#125;,

  <span class="hljs-attr">resolve</span>: &#123;
    <span class="hljs-comment">// 解析模块请求的选项</span>
    <span class="hljs-comment">// （不适用于对 loader 解析）</span>

    <span class="hljs-attr">modules</span>: [
      <span class="hljs-string">"node_modules"</span>,
      path.resolve(__dirname, <span class="hljs-string">"app"</span>)
    ],
    <span class="hljs-comment">// 用于查找模块的目录</span>

    <span class="hljs-attr">extensions</span>: [<span class="hljs-string">".js"</span>, <span class="hljs-string">".json"</span>, <span class="hljs-string">".jsx"</span>, <span class="hljs-string">".css"</span>],
    <span class="hljs-comment">// 使用的扩展名</span>

    <span class="hljs-attr">alias</span>: &#123;
      <span class="hljs-comment">// 模块别名列表</span>

      <span class="hljs-string">"module"</span>: <span class="hljs-string">"new-module"</span>,
      <span class="hljs-comment">// 起别名："module" -> "new-module" 和 "module/path/file" -> "new-module/path/file"</span>

      <span class="hljs-string">"only-module$"</span>: <span class="hljs-string">"new-module"</span>,
      <span class="hljs-comment">// 起别名 "only-module" -> "new-module"，但不匹配 "only-module/path/file" -> "new-module/path/file"</span>

      <span class="hljs-string">"module"</span>: path.resolve(__dirname, <span class="hljs-string">"app/third/module.js"</span>),
      <span class="hljs-comment">// 起别名 "module" -> "./app/third/module.js" 和 "module/file" 会导致错误</span>
      <span class="hljs-comment">// 模块别名相对于当前上下文导入</span>
    &#125;,
  &#125;,

  <span class="hljs-attr">devtool</span>: <span class="hljs-string">"source-map"</span>, <span class="hljs-comment">// enum</span>
  <span class="hljs-comment">// 通过在浏览器调试工具(browser devtools)中添加元信息(meta info)增强调试</span>
  <span class="hljs-comment">// 牺牲了构建速度的 `source-map' 是最详细的。</span>

  <span class="hljs-attr">devServer</span>: &#123;
    <span class="hljs-attr">proxy</span>: &#123; <span class="hljs-comment">// proxy URLs to backend development server</span>
      <span class="hljs-string">'/api'</span>: <span class="hljs-string">'http://localhost:3000'</span>
    &#125;,
    <span class="hljs-attr">contentBase</span>: path.join(__dirname, <span class="hljs-string">'public'</span>), <span class="hljs-comment">// boolean | string | array, static file location</span>
    <span class="hljs-attr">compress</span>: <span class="hljs-literal">true</span>, <span class="hljs-comment">// enable gzip compression</span>
    <span class="hljs-attr">historyApiFallback</span>: <span class="hljs-literal">true</span>, <span class="hljs-comment">// true for index.html upon 404, object for multiple paths</span>
    <span class="hljs-attr">hot</span>: <span class="hljs-literal">true</span>, <span class="hljs-comment">// hot module replacement. Depends on HotModuleReplacementPlugin</span>
    <span class="hljs-attr">https</span>: <span class="hljs-literal">false</span>, <span class="hljs-comment">// true for self-signed, object for cert authority</span>
    <span class="hljs-attr">noInfo</span>: <span class="hljs-literal">true</span>, <span class="hljs-comment">// only errors & warns on hot reload</span>
    <span class="hljs-comment">// ...</span>
  &#125;,

  <span class="hljs-attr">plugins</span>: [
    <span class="hljs-comment">// ...</span>
  ],
  <span class="hljs-comment">// 附加插件列表</span>


  <span class="hljs-comment">/* 高级配置（点击展示） */</span>
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>上面内容高级 CV 操作来自<a href="https://www.webpackjs.com/configuration/" target="_blank" rel="nofollow noopener noreferrer">Webpack官网</a>仅贴出常用配置！这个不是主体，进入写一个环节</p>
<ul>
<li>entry：入口，Webpack 执行构建的第一步将从 entry 开始，可抽象成输入。</li>
<li>module：模块，在 Webpack 里一切皆模块，一个模块对应着一个文件。Webpack 会从配置的 entry 开始递归找出所有依赖的模块。</li>
<li>chunk：代码块，一个 chunk 由多个模块组合而成，用于代码合并与分割。</li>
<li>loader：模块转换器，用于把模块原内容按照需求转换成新内容。</li>
<li>plugin：扩展插件，在 Webpack 构建流程中的特定时机会广播出对应的事件，插件可以监听这些事件的发生，在特定时机做对应的事情。</li>
</ul>
<p>你得了解上面基本信息后，才可以进入下一步</p>
<h4 data-id="heading-5">Loader 机制（手写一个）</h4>
<p>简单来说 loader 是一个 可以获取你入口文件源代码的一个函数，函数本身参数就是源代码。</p>
<p>实现一个读取图片的 loader 并没有你想象的那么难</p>
<ol>
<li>获取图片的buffer</li>
<li>转base64 / 写入 buffer 生成图片</li>
</ol>
<p>动手试试</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">// webpack.config.js</span>
 <span class="hljs-attr">module</span>: &#123;
        <span class="hljs-attr">rules</span>: [
            &#123;
                <span class="hljs-attr">test</span>: <span class="hljs-regexp">/\.(png)|(jpg)|(gif)$/</span>, use: [&#123;
                    <span class="hljs-attr">loader</span>: <span class="hljs-string">"./loaders/img-loader.js"</span>,
                    <span class="hljs-attr">options</span>: &#123;
                        <span class="hljs-attr">limit</span>: <span class="hljs-number">3000</span>, <span class="hljs-comment">//3000字节以上使用图片，3000字节以内使用base64</span>
                        <span class="hljs-attr">filename</span>: <span class="hljs-string">"img-[contenthash:5].[ext]"</span>
                    &#125;
                &#125;]
            &#125;
        ]
    &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>获取模块配置项</strong></p>
<p>在 Loader 中获取用户传入的 options，通过 loader-utils 的 getOptions 方法获取：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">var</span> loaderUtil = <span class="hljs-built_in">require</span>(<span class="hljs-string">"loader-utils"</span>)

<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">loader</span>(<span class="hljs-params">buffer</span>) </span>&#123; <span class="hljs-comment">//给的是buffer</span>
    <span class="hljs-built_in">console</span>.log(<span class="hljs-string">"文件数据大小：(字节)"</span>, buffer.byteLength);
    <span class="hljs-keyword">var</span> &#123; limit = <span class="hljs-number">1000</span>, filename = <span class="hljs-string">"[contenthash].[ext]"</span> &#125; = loaderUtil.getOptions(<span class="hljs-built_in">this</span>);
    <span class="hljs-keyword">if</span> (buffer.byteLength >= limit) &#123;
        <span class="hljs-keyword">var</span> content = getFilePath.call(<span class="hljs-built_in">this</span>, buffer, filename);
    &#125;
    <span class="hljs-keyword">else</span>&#123;
        <span class="hljs-keyword">var</span> content = getBase64(buffer)
    &#125;
    <span class="hljs-keyword">return</span> <span class="hljs-string">`module.exports = \`<span class="hljs-subst">$&#123;content&#125;</span>\``</span>;
&#125;

loader.raw = <span class="hljs-literal">true</span>; 
<span class="hljs-comment">// 通过 exports.raw 属性告诉 Webpack 该 Loader 是否需要二进制数据</span>

<span class="hljs-built_in">module</span>.exports = loader;

<span class="hljs-comment">// 获取base 64 格式</span>
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">getBase64</span>(<span class="hljs-params">buffer</span>) </span>&#123;
    <span class="hljs-keyword">return</span> <span class="hljs-string">"data:image/png;base64,"</span> + buffer.toString(<span class="hljs-string">"base64"</span>);
&#125;
<span class="hljs-comment">// 构建图片 生成路径</span>
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">getFilePath</span>(<span class="hljs-params">buffer, name</span>) </span>&#123;
    <span class="hljs-keyword">var</span> filename = loaderUtil.interpolateName(<span class="hljs-built_in">this</span>, name, &#123;
        <span class="hljs-attr">content</span>: buffer
    &#125;);
    <span class="hljs-built_in">this</span>.emitFile(filename, buffer);
    <span class="hljs-keyword">return</span> filename;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>上面通过 this.emitFile 进行文件写入</p>
<p><strong>同步与异步</strong></p>
<p>Loader 有同步和异步之分，上面的 Loader 都是同步的 Loader，因为它们的转换流程都是同步的，转换完成后再返回结果。但有些场景下转换的步骤只能是异步完成的，例如你需要通过网络请求才能得出结果，如果采用同步的方式 网络请求 就会阻塞整个构建，导致构建非常缓慢。</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-built_in">module</span>.exports = <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">source</span>) </span>&#123;
  <span class="hljs-comment">// 告诉 Webpack 本次转换是异步的，Loader 会在 callback 中回调结果</span>
  <span class="hljs-keyword">var</span> callback = <span class="hljs-built_in">this</span>.async();
  someAsyncOperation(source, <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">err, result, sourceMaps, ast</span>) </span>&#123;
    <span class="hljs-comment">// 通过 callback 返回异步执行后的结果</span>
    callback(err, result, sourceMaps, ast);
  &#125;);
&#125;;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>缓存加速</strong></p>
<p>在有些情况下，有些转换操作需要大量计算非常耗时，如果每次构建都重新执行重复的转换操作，构建将会变得非常缓慢。为此，Webpack 会默认缓存所有 Loader 的处理结果，也就是说在需要被处理的文件或者其他依赖的文件没有发生变化时，是不会重新调用对应的 Loader 去执行转换操作的。</p>
<p>如果你想让 Webpack 不缓存该 Loader 的处理结果，可以这样：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-built_in">module</span>.exports = <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">source</span>) </span>&#123;
  <span class="hljs-comment">// 关闭该 Loader 的缓存功能</span>
  <span class="hljs-built_in">this</span>.cacheable(<span class="hljs-literal">false</span>);
  <span class="hljs-keyword">return</span> source;
&#125;;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>知道了 Webpack 核心loader 再来介绍一下 plugin</p>
<h4 data-id="heading-6">Plugin 机制</h4>
<p>Plugin 可以干的活比Loader更多，更复杂，其本质是一个Class类</p>
<p>插件的基本结构
plugins 是可以用自身原型方法 apply 来实例化的对象。apply 只在安装插件被 Webpack 的 compiler 执行一次。apply 方法传入一个 webpck compiler 的引用，来访问编译器回调。</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">HelloPlugin</span> </span>&#123;
  <span class="hljs-comment">// 在构造函数中获取用户给该插件传入的配置</span>
  <span class="hljs-function"><span class="hljs-title">constructor</span>(<span class="hljs-params">options</span>)</span> &#123;
    <span class="hljs-comment">// ...</span>
  &#125;
  <span class="hljs-comment">// Webpack 会调用 HelloPlugin 实例的 apply 方法给插件实例传入 compiler 对象</span>
  <span class="hljs-function"><span class="hljs-title">apply</span>(<span class="hljs-params">compiler</span>)</span> &#123;
    <span class="hljs-comment">// 在 emit 阶段插入钩子函数，用于特定时机处理额外的逻辑</span>
    compiler.hooks.emit.tap(<span class="hljs-string">'HelloPlugin'</span>, <span class="hljs-function"><span class="hljs-params">compilation</span> =></span> &#123;
      <span class="hljs-comment">// 在功能流程完成后可以调用 Webpack 提供的回调函数</span>
    &#125;);
    <span class="hljs-comment">// 如果事件是异步的，会带两个参数，第二个参数为回调函数，在插件处理完成任务时需要调用回调函数通知 Webpack，才会进入下一个处理流程</span>
    compiler.plugin(<span class="hljs-string">'emit'</span>, <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">compilation, callback</span>) </span>&#123;
      <span class="hljs-comment">// 支持处理逻辑</span>
      <span class="hljs-comment">// 处理完毕后执行 callback 以通知 Webpack</span>
      <span class="hljs-comment">// 如果不执行 callback，运行流程将会一致卡在这不往下执行</span>
      callback();
    &#125;);
  &#125;
&#125;
<span class="hljs-built_in">module</span>.exports = HelloPlugin;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>使用插件时，只需要将它的实例放到 Webpack 的 Plugins 数组配置中：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">const</span> HelloPlugin = <span class="hljs-built_in">require</span>(<span class="hljs-string">'./hello-plugin.js'</span>);
<span class="hljs-built_in">module</span>.exports = &#123;
  <span class="hljs-attr">plugins</span>: [<span class="hljs-keyword">new</span> HelloPlugin(&#123; <span class="hljs-attr">options</span>: <span class="hljs-literal">true</span> &#125;)],
&#125;;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>先来分析以下 Webpack Plugin 的工作原理：</p>
<ol>
<li>读取配置的过程中会先执行 new HelloPlugin(options) 初始化一个 HelloPlugin 获得其实例</li>
<li>初始化 compiler 对象后调用 HelloPlugin.apply(compiler) 给插件实例传入 compiler 对象</li>
<li>插件实例在获取到 compiler 对象后，就可以通过 compiler.plugin(事件名称, 回调函数) 监听到 Webpack 广播出来的事件，并且可以通过 compiler 对象去操作 Webpack</li>
</ol>
<p>在<code>apply</code>的阶段你可以调用 <a href="https://www.webpackjs.com/api/compiler-hooks/" target="_blank" rel="nofollow noopener noreferrer">compiler钩子</a></p>
<p>webpack的hoosk钩子其实是使用tapable直接注册在不同的阶段的，所以我们进行下一步分析</p>
<h4 data-id="heading-7">小彩蛋（介绍部分Webpack原理分析）</h4>
<p>Webpack 本质是一个打包构建工具，我们不妨思考一下，它为我们做了什么。</p>
<ol>
<li>读取<code>webpack.config.js</code>配置文件，找到入口</li>
<li>获取入口文件中的源代码 分析抽象语法树（babel实现）</li>
<li>分析过程 静态分析代码执行上下文和使用情况, 标记是否<code>Tree Shaking</code></li>
<li>核心的loader 和 plugin 在读取配置过程中执行函数，<code>tapable</code>注入钩子函数</li>
<li>最后输出在配置文件中的出口目录中</li>
</ol>
<p>其实我们简易分析一下，也是非常好理解的</p>
<pre><code class="hljs language-javacript copyable" lang="javacript">// 首先定义 Compiler
class Compiler &#123;
  constructor(options) &#123;
    // Webpack 配置
    const &#123; entry, output &#125; = options;
    // 入口
    this.entry = entry;
    // 出口
    this.output = output;
    // 模块
    this.modules = [];
  &#125;
  // 构建启动
  run() &#123;
    // ...
  &#125;
  // 重写 require 函数，输出 bundle
  generate() &#123;
    // ...
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>使用 <code>@babel/parser</code>和<code>@babel/traverse</code>两个库分析源代码抽象语法树，找出所用模板依赖</p>
<p>而<code>tapable</code>本质是一个javascript小型库, 内部是发布订阅模式。类似Node的EventEmitter。</p>
<p>Webpack 本质上是一种事件流的机制，它的工作流程就是将各个插件串联起来，而实现这一切的核心就是 Tapable，Webpack 中最核心的负责编译的 Compiler 和负责创建 bundles 的 Compilation 都是 Tapable 的子类，并且实例内部的生命周期也是通过 Tapable 库提供的钩子类实现的。</p>
<h1 data-id="heading-8">总结</h1>
<p>Webpack 本质是一个事件流机制的打包构建工具，从读取配置到分析语法树注册事件流输出文件的一个过程。其核心的<code>loader</code> 本质也是一个可以获取到源代码的一个函数，<code>plugin</code>则是一个可以获取到整个事件生命周期的一个类~ 至此你应该对webpack有了更加深刻的认识，本文跳过了许多的细节问题，介绍核心知识，所以你还是得多看看配置的文档！</p>
<h2 data-id="heading-9">往期文章</h2>
<p><a href="https://juejin.cn/post/6910837207632707592" target="_blank">【重拾落叶】Javascript执行期上下文、预编译</a></p>
<p><a href="https://juejin.cn/post/6926124727324901383" target="_blank">【重拾落叶】浏览器如何完整获取一个页面？（加载篇）</a></p></div>  
</div>
            