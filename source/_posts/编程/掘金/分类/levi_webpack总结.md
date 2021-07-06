
---
title: 'levi_webpack总结'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=4239'
author: 掘金
comments: false
date: Sun, 04 Jul 2021 23:22:08 GMT
thumbnail: 'https://picsum.photos/400/300?random=4239'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><details>
  <summary>webpack 基本配置（可展开 && 收缩）</summary>
<pre><code class="copyable">
const os = require('os')
const &#123; resolve &#125; = require('path')
const webpack = require('webpack')
const HappyPack = require('happypack')
const WebpackBar = require('webpackbar')
const CopyPlugin = require('copy-webpack-plugin')
const HtmlWebpackPlugin = require('html-webpack-plugin')
const HardSourceWebpackPlugin = require('hard-source-webpack-plugin')
const CircularDependencyPlugin = require('circular-dependency-plugin')

const happyThreadPool = HappyPack.ThreadPool(&#123; size: os.cpus().length &#125;)
const source = resolve(__dirname, '..', 'src')

module.exports = &#123;
  context: source,
  entry: &#123;
    app: './index.tsx',
  &#125;,
  watchOptions: &#123;
    // 不监听的 node_modules 目录下的文件
    ignored: /node_modules/,
  &#125;,
  stats: &#123;
    assets: true,
    builtAt: true,
    colors: true,
    chunks: false,
    children: false,
    env: true,
    entrypoints: false,
    errors: true,
    errorDetails: true,
    hash: true,
    modules: false,
    moduleTrace: true,
    performance: true,
    publicPath: true,
    timings: true,
    version: true,
    warnings: true,
  &#125;,
  resolve: &#123;
    unsafeCache: true,
    mainFiles: ['index'],
    mainFields: ['main'],
    extensions: ['.ts', '.tsx', '.js'],
    modules: [source, 'node_modules'],
    alias: &#123;
      '@': source,
      'react-dom': '@hot-loader/react-dom',
      moment: 'dayjs',
      '@components': resolve(__dirname, '../src/components'),
      '@ant-design/icons/lib/dist$': resolve(__dirname, '../src/assets/icons.ts'),
    &#125;,
  &#125;,
  module: &#123;
    rules: [
      &#123;
        test: /\.((ts|js)(x?))$/,
        exclude: /node_modules/,
        include: [source],
        use: 'happypack/loader?id=babel',
      &#125;,
      &#123;
        test: /\.(jpe?g|png|gif|svg)$/,
        use: [
          &#123;
            loader: 'url-loader',
            options: &#123;
              limit: 8 * 1024,
              outputPath: 'images',
              name: '[path][name].[ext]',
            &#125;,
          &#125;,
        ],
      &#125;,
    ],
  &#125;,
  plugins: [
    new WebpackBar(),
    new CopyPlugin([
      &#123;
        from: resolve(__dirname, '../static'),
        ignore: ['dll/*'],
        to: resolve(__dirname, '../dist'),
      &#125;,
    ]),
    new HtmlWebpackPlugin(&#123;
      title: '新际通管理平台',
      filename: 'index.html',
      template: resolve(__dirname, '../public/index.html'),
      hash: true,
      minify: &#123;
        removeRedundantAttributes: true,
        collapseWhitespace: true,
        removeAttributeQuotes: true,
        removeComments: true,
        collapseBooleanAttributes: true,
      &#125;,
      // favicon: resolve(__dirname, '../public/favicon.ico'),
    &#125;),
    new HappyPack(&#123;
      id: 'babel',
      threadPool: happyThreadPool,
      loaders: [
        'cache-loader',
        &#123;
          loader: 'babel-loader',
          query: &#123;
            cacheDirectory: './node_modules/webpack_cache/',
          &#125;,
        &#125;,
        'eslint-loader',
      ],
    &#125;),
    new webpack.IgnorePlugin(/^\.\/locale$/, /dayjs$/),
    new HardSourceWebpackPlugin(),
    new CircularDependencyPlugin(&#123;
      exclude: /node_modules/,
      include: /src/,
      failOnError: true,
      allowAsyncCycles: false,
      cwd: process.cwd(),
    &#125;),
  ],
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
</details>
<h4 data-id="heading-0">webpack 模块打包原理</h4>
<ul>
<li><a href="https://juejin.cn/post/6844903802382860296#heading-5" target="_blank">webpack 模块打包原理</a></li>
</ul>
<p>下面谈谈我的理解<br>
javascript 万物皆对象，每个实例都有一个<strong>proto</strong>属性，指向了他构造函数的原型对象
每个构造函数都有一个 prototype 属性，指向了他的原型对象</p>
<blockquote>
<p>实例对象创建之间判断指向关系有 <strong>proto</strong> 代表指向关系 指向了原型对象</p>
</blockquote>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">A</span>(<span class="hljs-params"></span>) </span>&#123;&#125; <span class="hljs-comment">// A 构造函数</span>
<span class="hljs-keyword">var</span> a = <span class="hljs-keyword">new</span> A(); <span class="hljs-comment">// a 实例对象</span>

A.prototype; <span class="hljs-comment">// 原型对象</span>
a.__proto__ === A.prototype;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>所有函数都是由 Function 创建</p>
<pre><code class="hljs language-javascript copyable" lang="javascript">A.__proto__ === <span class="hljs-built_in">Function</span>.prototype; <span class="hljs-comment">// true</span>

<span class="hljs-built_in">Function</span>.__proto__ === <span class="hljs-built_in">Function</span>.prototype; <span class="hljs-comment">// true</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>Object 刚讲的是顶级函数，所以也是函数：（所有的鱼都归猫管哈哈哈哈哈）</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-built_in">Object</span>.__proto__ === <span class="hljs-built_in">Function</span>.prototype;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>所有的对象都是由 Object 构造函数创建的</strong>, 所以对象<strong>proto</strong>指向了 Object 的构造函数：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript">A.prototype.__proto__ === <span class="hljs-built_in">Object</span>.prototype;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>Object.prototype 也是对象，比较特殊，指向了 null</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-built_in">Object</span>.prototype.__proto__ === <span class="hljs-literal">null</span>;
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-1">webpack 热更新原理</h4>
<h4 data-id="heading-2">webpack 如何自定义loader，实现思路如何</h4>
<blockquote>
<p>带有副作用的内容转换器,函数, 从右到左执行，实质上是一个compose函数
将源文件经过转换输出新的结果，支持链式操作，其本质上就是一个函数</p>
</blockquote>
<pre><code class="hljs language-javascript copyable" lang="javascript">
<span class="hljs-built_in">module</span>.exports = <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">source, sourceMap?, data?</span>) </span>&#123;&#125;

<span class="hljs-comment">/** 同步loader */</span>
<span class="hljs-built_in">module</span>.exports = <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params">context</span>) </span>&#123;
  <span class="hljs-keyword">const</span> options = LeviLoaderUtils.getOptions(<span class="hljs-built_in">this</span>);

  <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'loader配置项:'</span>, options);

  <span class="hljs-keyword">const</span> result = context.concat(<span class="hljs-string">`console.log("<span class="hljs-subst">$&#123;options.message || <span class="hljs-string">'没有配置项'</span>&#125;</span>");`</span>);

  <span class="hljs-keyword">return</span> result;
&#125;;

<span class="hljs-comment">/** 异步loader */</span>
<span class="hljs-comment">// module.exports = function (context) &#123;</span>
<span class="hljs-comment">//   let count = 1;</span>
<span class="hljs-comment">//   const options = LeviLoaderUtils.getOptions(this);</span>
<span class="hljs-comment">//   const callback = this.async();</span>

<span class="hljs-comment">//   console.log(options);</span>
<span class="hljs-comment">//   const timer = setInterval(() => &#123;</span>
<span class="hljs-comment">//     count = count + 1;</span>
<span class="hljs-comment">//     console.log(count);</span>
<span class="hljs-comment">//   &#125;, 1000);</span>

<span class="hljs-comment">//   setTimeout(() => &#123;</span>
<span class="hljs-comment">//     callback(null, context);</span>
<span class="hljs-comment">//     clearInterval(timer);</span>
<span class="hljs-comment">//   &#125;, 4000);</span>
<span class="hljs-comment">// &#125;;</span>

    <span class="hljs-comment">// webpack callnack完整签名如下</span>
    <span class="hljs-built_in">this</span>.callback(
        <span class="hljs-comment">// 异常信息，Loader 正常运行时传递 null 值即可</span>
        err: <span class="hljs-built_in">Error</span> | <span class="hljs-literal">null</span>,
        <span class="hljs-comment">// 转译结果</span>
        <span class="hljs-attr">content</span>: string | Buffer,
        <span class="hljs-comment">// 源码的 sourcemap 信息</span>
        sourceMap?: SourceMap,
        <span class="hljs-comment">// 任意需要在 Loader 间传递的值</span>
        <span class="hljs-comment">// 经常用来传递 ast 对象，避免重复解析</span>
        data?: any
    );

<span class="copy-code-btn">复制代码</span></code></pre>
<p>参考文章: <a href="https://zhuanlan.zhihu.com/p/375626250" target="_blank" rel="nofollow noopener noreferrer">Webpack 原理系列七：如何编写loader</a></p>
<h4 data-id="heading-3">webpack 如何自定义plugin，实现思路是如何</h4>
<blockquote>
<p>plugin本质上就是拥有apply放的对象，在webpack初始化解读会执行apply方法
plugin 可以监听webpack各个生命周期广播出来的事件，在合适的实际，通过webpack释放的API来改变输出结果</p>
</blockquote>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Levi_Plugin</span> </span>&#123;
  <span class="hljs-function"><span class="hljs-title">apply</span>(<span class="hljs-params">compiler</span>)</span> &#123;
    <span class="hljs-comment">//不推荐使用，plugin函数被废弃了</span>
    <span class="hljs-comment">// compiler.plugin("compile", (compilation) => &#123;</span>
    <span class="hljs-comment">//   console.log("compile");</span>
    <span class="hljs-comment">// &#125;);</span>
    <span class="hljs-comment">//注册完成的钩子</span>
    compiler.hooks.done.tap(<span class="hljs-string">"MyPlugin"</span>, <span class="hljs-function">(<span class="hljs-params">compilation</span>) =></span> &#123;
      <span class="hljs-built_in">console</span>.log(<span class="hljs-string">"compilation done"</span>);
    &#125;);
  &#125;
&#125;

<span class="hljs-comment">// 注册异步狗子</span>
<span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Levi_Plugin</span> </span>&#123;
  <span class="hljs-function"><span class="hljs-title">apply</span>(<span class="hljs-params">compiler</span>)</span> &#123;
    compiler.hooks.run.tapAsync(<span class="hljs-string">"MyPlugin"</span>, <span class="hljs-function">(<span class="hljs-params">compilation, callback</span>) =></span> &#123;
      <span class="hljs-built_in">setTimeout</span>(<span class="hljs-function">()=></span>&#123;
        <span class="hljs-built_in">console</span>.log(<span class="hljs-string">"compilation run"</span>);
        callback()
      &#125;, <span class="hljs-number">1000</span>)
    &#125;);
    compiler.hooks.emit.tapPromise(<span class="hljs-string">"MyPlugin"</span>, <span class="hljs-function">(<span class="hljs-params">compilation</span>) =></span> &#123;
      <span class="hljs-keyword">return</span> <span class="hljs-keyword">new</span> <span class="hljs-built_in">Promise</span>(<span class="hljs-function">(<span class="hljs-params">resolve, reject</span>) =></span> &#123;
        <span class="hljs-built_in">setTimeout</span>(<span class="hljs-function">()=></span>&#123;
          <span class="hljs-built_in">console</span>.log(<span class="hljs-string">"compilation emit"</span>);
          resolve();
        &#125;, <span class="hljs-number">1000</span>)
      &#125;);
    &#125;);
  &#125;
&#125;

<span class="hljs-built_in">module</span>.exports = Levi_Plugin;
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>compiler对象包含了 Webpack 环境所有的的配置信息。这个对象在启动 webpack 时被一次性建立，并配置好所有可操作的设置，包括 options，loader 和 plugin。当在 webpack 环境中应用一个插件时，插件将收到此 compiler 对象的引用。可以使用它来访问 webpack 的主环境</li>
<li>compilation对象包含了当前的模块资源、编译生成资源、变化的文件等。</li>
</ul>
<h5 data-id="heading-4">参考文档</h5>
<ul>
<li><a href="https://www.webpackjs.com/api/compiler-hooks/" target="_blank" rel="nofollow noopener noreferrer">compiler构造</a></li>
<li><a href="https://zhuanlan.zhihu.com/p/40930680" target="_blank" rel="nofollow noopener noreferrer">手写一个webpack/plugin</a></li>
<li><a href="https://juejin.cn/post/6888936770692448270#heading-8" target="_blank">Webpack手写loader和plugin</a></li>
</ul>
<h4 data-id="heading-5">如何题提升webpack构建速度</h4>
<ul>
<li>
<p>使用高版本的webpack和nodejs</p>
</li>
<li>
<p>启用多进程构建（happypack/thead-loader）</p>
</li>
<li>
<p>压缩代码</p>
</li>
<li>
<p>使用mini-css-extract-plugin 提取公共css</p>
</li>
<li>
<p>terser-webpack-plugin 开启js多进程压缩</p>
</li>
<li>
<p>缩小打包作用域</p>
</li>
<li>
<p>exclude/include (确定 loader 规则范围)</p>
</li>
<li>
<p>resolve.modules 指定解析第三方包的目录位置 (减少不必要的查找)</p>
</li>
<li>
<p>resolve.extensions 尽可能减少后缀尝试的可能性</p>
</li>
<li>
<p>合理使用alias,简化导入</p>
</li>
<li>
<p>提取页面公共资源</p>
</li>
<li>
<p>使用 SplitChunksPlugin 进行(公共脚本、基础包、页面公共文件)分离(Webpack4内置) ，替代了 CommonsChunkPlugin 插件</p>
</li>
<li>
<p>提取公共js资源 => splitChunks</p>
<pre><code class="hljs language-javascrit copyable" lang="javascrit">module.exports = &#123;
    optimization: &#123;
        splitChunks: &#123;
            cacheGroups: &#123;
                utils: &#123;
                    chunks: 'initial',
                    minSize: 0,
                    minChunks: 2
                &#125;
            &#125;
        &#125;
    &#125;
&#125;;
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
<li>
<p>利用缓存提升二次加载速度</p>
</li>
<li>
<p>hard-source-webpack-plugin</p>
</li>
</ul>
<h4 data-id="heading-6">常见的loader有哪些，使用过哪些loader</h4>
<ul>
<li>file-loader</li>
<li>css-loader</li>
<li>image-loader</li>
<li>less-loader</li>
<li>babel-loader</li>
<li>ts-loader</li>
<li>eslint-loader</li>
</ul>
<h4 data-id="heading-7">有哪些常用插件， 使用过哪些</h4>
<ul>
<li>html-webpack-plugin 简化html创建</li>
<li>mini-css-extract-plugin 提取css文件</li>
<li>define-plugin 定义环境变量 (Webpack4 之后指定 mode 会自动配置)</li>
<li>hardsource-webpack-plugin 启用缓存</li>
<li>happypack 多进程构建</li>
<li>webpack-bundle-analyzer  可视化 Webpack 输出文件的体积 (业务组件、依赖第三方模块)</li>
<li>clean-webpack-plugin</li>
</ul>
<h4 data-id="heading-8">webpack中loader和plugin区别</h4>
<p>Loader 本质就是一个函数，在该函数中对接收到的内容进行转换，返回转换后的结果。 因为 Webpack 只认识 JavaScript，所以 Loader 就成了翻译官，对其他类型的资源进行转译的预处理工作</p>
<p>Plugin 就是插件，基于事件流框架 Tapable，插件可以扩展 Webpack 的功能，在 Webpack 运行的生命周期中会广播出许多事件，Plugin 可以监听这些事件，在合适的时机通过 Webpack 提供的 API 改变输出结果</p>
<p>Loader 在 module.rules 中配置，作为模块的解析规则，类型为数组。每一项都是一个 Object，内部包含了 test(类型文件)、loader、options (参数)等属性。</p>
<p>Plugin 在 plugins 中单独配置，类型为数组，每一项是一个 Plugin 的实例，参数都通过构造函数传入。</p>
<h4 data-id="heading-9">webpack构建流程简述下</h4>
<ul>
<li>初始化参数：从配置文件和 Shell 语句中读取与合并参数，得出最终的参数</li>
<li>开始编译：用上一步得到的参数初始化 Compiler 对象，加载所有配置的插件，执行对象的 run 方法开始执行编译</li>
<li>确定入口：根据配置中的 entry 找出所有的入口文件</li>
<li>编译模块：从入口文件出发，调用所有配置的 Loader 对模块进行翻译，再找出该模块依赖的模块，再递归本步骤直到所有入口依赖的文件都经过了本步骤的处理</li>
<li>完成模块编译：在经过第4步使用 Loader 翻译完所有模块后，得到了每个模块被翻译后的最终内容以及它们之间的依赖关系</li>
<li>输出资源：根据入口和模块之间的依赖关系，组装成一个个包含多个模块的 Chunk，再把每个 Chunk 转换成一个单独的文件加入到输出列表，这步是可以修改输出内容的最后机会</li>
<li>输出完成：在确定好输出内容后，根据配置确定输出的路径和文件名，把文件内容写入到文件系统</li>
</ul>
<p>在以上过程中，Webpack 会在特定的时间点广播出特定的事件，插件在监听到感兴趣的事件后会执行特定的逻辑，并且插件可以调用 Webpack 提供的 API 改变 Webpack 的运行结果。</p>
<p>简单说</p>
<ul>
<li>初始化：启动构建，读取与合并配置参数，加载 Plugin，实例化 Compiler</li>
<li>编译：从 Entry 出发，针对每个 Module 串行调用对应的 Loader 去翻译文件的内容，再找到该 Module 依赖的 Module，递归地进行编译处理</li>
<li>输出：将编译后的 Module 组合成 Chunk，将 Chunk 转换成文件，输出到文件系统中</li>
</ul>
<h4 data-id="heading-10">webpack如何文件监听</h4>
<p>webpack 开启监听有2种方式</p>
<ul>
<li>启动命令行添加 --watch</li>
<li>webpack 配置文件中 添加 watch: true</li>
</ul>
<h4 data-id="heading-11">babel编译原理</h4>
<ul>
<li>解析：将代码转换成 AST</li>
<li>转换：访问 AST 的节点进行变换操作生产新的 AST</li>
<li>生成：以新的 AST 为基础生成代码</li>
</ul>
<h4 data-id="heading-12">less-loader 源码</h4>
<pre><code class="hljs language-javascript copyable" lang="javascript">    <span class="hljs-keyword">import</span> less <span class="hljs-keyword">from</span> <span class="hljs-string">'less'</span>;
    <span class="hljs-keyword">import</span> &#123; getOptions &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'loader-utils'</span>;
    <span class="hljs-keyword">import</span> &#123; validate &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'schema-utils'</span>;
    <span class="hljs-keyword">import</span> schema <span class="hljs-keyword">from</span> <span class="hljs-string">'./options.json'</span>;
    <span class="hljs-keyword">async</span> <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">lessLoader</span>(<span class="hljs-params">source</span>) </span>&#123;
    <span class="hljs-keyword">const</span> options = getOptions(<span class="hljs-built_in">this</span>);
    <span class="hljs-comment">//校验参数</span>
    validate(schema, options, &#123;
        <span class="hljs-attr">name</span>: <span class="hljs-string">'Less Loader'</span>,
        <span class="hljs-attr">baseDataPath</span>: <span class="hljs-string">'options'</span>,
    &#125;);
    <span class="hljs-keyword">const</span> callback = <span class="hljs-built_in">this</span>.async();
    <span class="hljs-comment">//对options进一步处理，生成less渲染的参数</span>
    <span class="hljs-keyword">const</span> lessOptions = getLessOptions(<span class="hljs-built_in">this</span>, options);
    <span class="hljs-comment">//是否使用sourceMap，默认取options中的参数</span>
    <span class="hljs-keyword">const</span> useSourceMap =
        <span class="hljs-keyword">typeof</span> options.sourceMap === <span class="hljs-string">'boolean'</span> 
        ? options.sourceMap : <span class="hljs-built_in">this</span>.sourceMap;
    <span class="hljs-comment">//如果使用sourceMap，就在渲染参数加入</span>
    <span class="hljs-keyword">if</span> (useSourceMap) &#123;
        lessOptions.sourceMap = &#123;
        <span class="hljs-attr">outputSourceFiles</span>: <span class="hljs-literal">true</span>,
        &#125;;
    &#125;
    <span class="hljs-keyword">let</span> data = source;
    <span class="hljs-keyword">let</span> result;
    <span class="hljs-keyword">try</span> &#123;
        result = <span class="hljs-keyword">await</span> less.render(data, lessOptions);
    &#125; <span class="hljs-keyword">catch</span> (error) &#123;
    &#125;
    <span class="hljs-keyword">const</span> &#123; css, imports &#125; = result;
    <span class="hljs-comment">//有sourceMap就进行处理</span>
    <span class="hljs-keyword">let</span> map =
        <span class="hljs-keyword">typeof</span> result.map === <span class="hljs-string">'string'</span> 
        ? <span class="hljs-built_in">JSON</span>.parse(result.map) : result.map;
    
    callback(<span class="hljs-literal">null</span>, css, map);
    &#125;
    <span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> lessLoader;
<span class="copy-code-btn">复制代码</span></code></pre></div>  
</div>
            