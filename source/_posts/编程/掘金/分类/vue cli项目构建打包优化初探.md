
---
title: 'vue cli项目构建打包优化初探'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/dbedc66bbafc46ecbf24566346569527~tplv-k3u1fbpfcp-zoom-1.image'
author: 掘金
comments: false
date: Sun, 02 May 2021 00:01:45 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/dbedc66bbafc46ecbf24566346569527~tplv-k3u1fbpfcp-zoom-1.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h2 data-id="heading-0">背景</h2>
<p>因为公司的前端项目在打包构建方面时间属实长得离谱，冷启动大约5min，本地构建打包也大约5min,到线上腾讯云docker构建打包全过程需要16~20min。因此不仅极大影响开发效率，也大大延迟了给测试交付的时间。</p>
<h2 data-id="heading-1">优化思路</h2>
<ul>
<li>了解项目当前webpack配置</li>
<li>构建相关优化</li>
<li>打包体积相关优化</li>
<li>docker相关优化</li>
</ul>
<h2 data-id="heading-2">量化工具</h2>
<h3 data-id="heading-3">speed-measure-webpack-plugin</h3>
<h4 data-id="heading-4">介绍：</h4>
<p><a href="https://www.npmjs.com/package/speed-measure-webpack-plugin" target="_blank" rel="nofollow noopener noreferrer">speed-measure-webpack-plugin npm</a></p>
<blockquote>
<p>The first step to optimising your webpack build speed, is to know where to focus your attention.
This plugin measures your webpack build speed, giving an output like this:</p>
</blockquote>
<p>通过smp输出的分析可以清楚的了解到webpack构建过程中，每一阶段的loader以及plugin的工作花费的时间。</p>
<h4 data-id="heading-5">使用方式：</h4>
<pre><code class="hljs language-javascript copyable" lang="javascript"># Yarn
yarn add -D speed-measure-webpack-plugin

<span class="hljs-keyword">const</span> SpeedMeasurePlugin = <span class="hljs-built_in">require</span>(<span class="hljs-string">'speed-measure-webpack-plugin'</span>)
<span class="hljs-built_in">module</span>.exports = &#123;
  <span class="hljs-attr">chainWebpack</span>: <span class="hljs-function"><span class="hljs-params">config</span> =></span> &#123;
    config
      .plugin(<span class="hljs-string">'speed-measure-webpack-plugin'</span>)
      .use(SpeedMeasurePlugin)
      .end()
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>在本项目中使用其他的使用都会报error，但是以上的用法似乎不会区分plugin与loader的使用，甚至没有其他plugin的使用情况信息，迷惑~。</p>
<h3 data-id="heading-6">webpack-bundle-analyzer</h3>
<h4 data-id="heading-7">介绍：</h4>
<p><a href="https://www.npmjs.com/package/webpack-bundle-analyzer" target="_blank" rel="nofollow noopener noreferrer">webpack-bundle-analyzer npm</a>
用来分析webapck构建打包后的文件，如分包情况，占用体积等参数的分析。</p>
<h4 data-id="heading-8">使用方式：</h4>
<pre><code class="hljs language-javascript copyable" lang="javascript"># Yarn
yarn add -D webpack-bundle-analyzer

<span class="hljs-keyword">const</span> BundleAnalyzerPlugin = <span class="hljs-built_in">require</span>(<span class="hljs-string">'webpack-bundle-analyzer'</span>).BundleAnalyzerPlugin;
<span class="hljs-built_in">module</span>.exports = &#123;
  <span class="hljs-attr">plugins</span>: [
    <span class="hljs-keyword">new</span> BundleAnalyzerPlugin()
  ]
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>但是在vue-cli中有report命令可以直接调用，然后去dist打包目录打开report.html。</p>
<pre><code class="hljs language-javascript copyable" lang="javascript">vue-cli-service build --report
or
vue-cli-service build --report-json
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-9">查看vue-cli当前webpack配置</h2>
<h3 data-id="heading-10">介绍</h3>
<p>vue-cli脚手架会有webpack的很多默认行为，因此我们得知道基于vue-cli的项目，当前的webpack都配置了啥，然后才能做针对性的分析与优化。</p>
<blockquote>
<p><code>vue-cli-service</code> 暴露了 <code>inspect</code> 命令用于审查解析好的 webpack 配置。那个全局的 <code>vue</code> 可执行程序同样提供了 <code>inspect</code> 命令，这个命令只是简单的把 <code>vue-cli-service inspect</code> 代理到了你的项目中。</p>
</blockquote>
<h3 data-id="heading-11">使用方式：</h3>
<pre><code class="hljs language-javascript copyable" lang="javascript">#根据mode，分别生成开发环境、生产环境的配置
vue inspect --mode production > output.js
#输入命令后，在根目录会生产一个output.js文件
<span class="copy-code-btn">复制代码</span></code></pre>
<p>如果<code>vue command not found</code>的错可以全局安装注册一下vue命令<code>npm install -g vue-cli</code></p>
<h2 data-id="heading-12">构建相关优化</h2>
<h3 data-id="heading-13">hard-source-webpack-plugin</h3>
<h4 data-id="heading-14">介绍</h4>
<p><a href="https://www.npmjs.com/package/hard-source-webpack-plugin" target="_blank" rel="nofollow noopener noreferrer">hard-source-webpack-plugin npm</a></p>
<blockquote>
<p>HardSourceWebpackPlugin is a plugin for webpack to provide an intermediate caching step for modules. In order to see results, you'll need to run webpack twice with this plugin: the first build will take the normal amount of time. The second build will be signficantly faster.</p>
</blockquote>
<p>在启动项目时会针对项目生成缓存，若是项目无package或其他变化，下次就不用花费时间重新构建，直接复用缓存。</p>
<h4 data-id="heading-15">使用方式：</h4>
<pre><code class="hljs language-javascript copyable" lang="javascript">#yarn
yarn add -D hard-source-webpack-plugin

<span class="hljs-keyword">const</span> HardSourceWebpackPlugin = <span class="hljs-built_in">require</span>(<span class="hljs-string">'hard-source-webpack-plugin'</span>)
<span class="hljs-built_in">module</span>.exports = &#123;
<span class="hljs-attr">configureWebpack</span>: <span class="hljs-function"><span class="hljs-params">config</span> =></span> &#123;
  config.plugin.push(
    <span class="hljs-comment">// 为模块提供中间缓存，缓存路径是：node_modules/.cache/hard-source</span>
      <span class="hljs-comment">// solve Configuration changes are not being detected</span>
      <span class="hljs-keyword">new</span> HardSourceWebpackPlugin(&#123;
        <span class="hljs-attr">root</span>: process.cwd(),
        <span class="hljs-attr">directories</span>: [],
        <span class="hljs-attr">environmentHash</span>: &#123;
          <span class="hljs-attr">root</span>: process.cwd(),
          <span class="hljs-attr">directories</span>: [],
          <span class="hljs-attr">files</span>: [<span class="hljs-string">'package.json'</span>, <span class="hljs-string">'yarn.lock'</span>, <span class="hljs-string">'vue.config.js'</span>]
        &#125;
      &#125;)
      <span class="hljs-comment">// 配置了files的主要原因是解决配置更新，cache不生效了的问题，配置后有包的变化，plugin会重新构建一部分cache</span>
    )
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-16">注意：</h4>
<p><code>Could not freeze : Cannot read property 'hash' of undefined</code> 删除node_modules/.cache后，重新启动项目，产生这个问题的原因可能是异步加载模块时编译产生的错误，可参考：</p>
<h3 data-id="heading-17">缩小文件检索解析范围</h3>
<p>为避免无用的检索与递归遍历，可以使用alias指定引用时候的模块，noParse，对不依赖本地代码的第三方依赖不进行解析。</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">// 定义getAliasPath方法，把相对路径转换成绝对路径</span>
<span class="hljs-keyword">const</span> getAliasPath = <span class="hljs-function"><span class="hljs-params">dir</span> =></span> join(__dirname, dir)
<span class="hljs-built_in">module</span>.exports = &#123;
<span class="hljs-attr">configureWebpack</span>: <span class="hljs-function"><span class="hljs-params">config</span> =></span> &#123;
    config.module.noParse = <span class="hljs-regexp">/^(vu|vue-router|vuex|vuex-router-sync|lodash|echarts|axios|element-ui)$/</span>
  &#125;
  <span class="hljs-attr">chainWebpack</span>: <span class="hljs-function"><span class="hljs-params">config</span> =></span> &#123;
    <span class="hljs-comment">// 添加别名</span>
    config.resolve.alias
      .set(<span class="hljs-string">'@'</span>, getAliasPath(<span class="hljs-string">'src'</span>))
      .set(<span class="hljs-string">'assets'</span>, getAliasPath(<span class="hljs-string">'src/assets'</span>))
      .set(<span class="hljs-string">'utils'</span>, getAliasPath(<span class="hljs-string">'src/utils'</span>))
      .set(<span class="hljs-string">'views'</span>, getAliasPath(<span class="hljs-string">'src/views'</span>))
      .set(<span class="hljs-string">'components'</span>, getAliasPath(<span class="hljs-string">'src/components'</span>))
&#125;
  <span class="hljs-comment">// 生产环境禁用eslint</span>
  <span class="hljs-attr">lintOnSave</span>: !process.env.NODE_ENV !== <span class="hljs-string">'production'</span>,
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-18">减少打包体积</h3>
<h4 data-id="heading-19">image-webpack-plugin 图片压缩</h4>
<p>对图片像素要求没很极致的，这个压缩还是可以使用的，压缩率肉眼看起来感觉是没太大区别。
这里注意一下，我没有对svg进行压缩，原因是压缩的svg,再通过构建时被打包成base64时，生成的base64会有问题，无法访问。</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-built_in">module</span>.exports = &#123;
  <span class="hljs-attr">chainWebpack</span>: <span class="hljs-function"><span class="hljs-params">config</span> =></span> &#123;
   <span class="hljs-comment">// 对图片进行压缩</span>
    config.module
      .rule(<span class="hljs-string">'images'</span>)
      .test(<span class="hljs-regexp">/\.(png|jpe?g|gif)(\?.*)?$/</span>)
      .use(<span class="hljs-string">'image-webpack-loader'</span>)
      .loader(<span class="hljs-string">'image-webpack-loader'</span>)
      .options(&#123; <span class="hljs-attr">bypassOnDebug</span>: <span class="hljs-literal">true</span> &#125;)
      .end()
&#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-20">UglifyJsPlugin删除console 注释</h4>
<p>uglifyJsPlugin 用来对js文件进行压缩，减小js文件的大小。其会拖慢webpack的编译速度，建议开发环境时关闭，生产环境再将其打开。
更建议规范团队成员的代码上去解决。</p>
<pre><code class="hljs language-javascript copyable" lang="javascript">#yarn
yarn add -D uglifyjs-webpack-plugin

<span class="hljs-keyword">const</span> UglifyJsPlugin = <span class="hljs-built_in">require</span>(<span class="hljs-string">'uglifyjs-webpack-plugin'</span>)

<span class="hljs-built_in">module</span>.exports = &#123;
<span class="hljs-attr">configureWebpack</span>: <span class="hljs-function"><span class="hljs-params">config</span> =></span> &#123;
  config.plugin.push(
    <span class="hljs-keyword">new</span> UglifyJsPlugin(&#123;
        <span class="hljs-attr">uglifyOptions</span>: &#123;
          <span class="hljs-comment">// 删除注释</span>
          <span class="hljs-attr">output</span>: &#123;
            <span class="hljs-attr">comments</span>: <span class="hljs-literal">false</span>
          &#125;,
          <span class="hljs-comment">// 删除console debugger 删除警告</span>
          <span class="hljs-attr">compress</span>: &#123;
            <span class="hljs-attr">warnings</span>: <span class="hljs-literal">false</span>,
            <span class="hljs-attr">drop_console</span>: <span class="hljs-literal">true</span>, <span class="hljs-comment">//console</span>
            <span class="hljs-attr">drop_debugger</span>: <span class="hljs-literal">false</span>,
            <span class="hljs-attr">pure_funcs</span>: [<span class="hljs-string">'console.log'</span>] <span class="hljs-comment">//移除console</span>
          &#125;
        &#125;,
        <span class="hljs-attr">sourceMap</span>: <span class="hljs-literal">false</span>,
        <span class="hljs-attr">parallel</span>: <span class="hljs-literal">true</span> <span class="hljs-comment">//使用多进程并行运行来提高构建速度。默认并发运行数：os.cpus().length - 1。</span>
      &#125;)
    )
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-21">DLL动态链接库</h3>
<p>这个插件是在一个额外的独立的 webpack 设置中创建一个只有 dll 的 bundle(dll-only-bundle)。 这个插件会生成一个名为 manifest.json 的文件，这个文件是用来让 DLLReferencePlugin 映射到相关的依赖上去的。</p>
<blockquote>
<p>可以简单理解为把一些依赖从项目的bundle中拆分出去，通过映射关系用请求来加载。我认为拆分出去之后不会再在项目里被解析，因此对构建，体积都是有所帮助的。</p>
</blockquote>
<p>配置DllPlugin,可以分为下面几个步骤：</p>
<ol>
<li>新建webpack.dll.config.js文件(其他命名都可以)，配置需要拆分的插件；</li>
<li>在package.json文件中新建一条命令来专门打包，<code>"build:dll":"webpack --config webpack.dll.config.js"</code>; 运行该命令；</li>
<li>在vue.config.js 文件中配置<code>DllReferencePlugin</code>,主要把dll引用到需要预编译的依赖；</li>
<li>在index.html手动引入拆分的bundle包（放到cdn的话会更好）</li>
</ol>
<p>安装：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript">#yarn 
yarn add webpack-cli@^<span class="hljs-number">3.2</span><span class="hljs-number">.3</span> add-asset-html-webpack-plugin@^<span class="hljs-number">3.1</span><span class="hljs-number">.3</span> clean-webpack-plugin@^<span class="hljs-number">1.0</span><span class="hljs-number">.1</span> --dev
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">// webpack.dll.config.js</span>
<span class="hljs-comment">/* eslint-disable @typescript-eslint/no-var-requires */</span>
<span class="hljs-keyword">const</span> path = <span class="hljs-built_in">require</span>(<span class="hljs-string">'path'</span>)
<span class="hljs-keyword">const</span> webpack = <span class="hljs-built_in">require</span>(<span class="hljs-string">'webpack'</span>)
<span class="hljs-keyword">const</span> CleanWebpackPlugin = <span class="hljs-built_in">require</span>(<span class="hljs-string">'clean-webpack-plugin'</span>)
<span class="hljs-comment">// dll文件存放的目录</span>
<span class="hljs-keyword">const</span> dllPath = <span class="hljs-string">'public/vendor'</span>

<span class="hljs-built_in">module</span>.exports = &#123;
  <span class="hljs-attr">entry</span>: &#123;
    <span class="hljs-comment">// 需要提取的库文件</span>
    <span class="hljs-attr">vendor</span>: [<span class="hljs-string">'vue'</span>, <span class="hljs-string">'vue-router'</span>, <span class="hljs-string">'vuex'</span>],
    <span class="hljs-attr">utils</span>: [<span class="hljs-string">'axios'</span>, <span class="hljs-string">'lodash'</span>]
  &#125;,
  <span class="hljs-attr">output</span>: &#123;
    <span class="hljs-attr">path</span>: path.join(__dirname, dllPath),
    <span class="hljs-attr">filename</span>: <span class="hljs-string">'[name].dll.js'</span>,
    <span class="hljs-comment">// vendor.dll.js中暴露出的全局变量名</span>
    <span class="hljs-comment">// 保持与 webpack.DllPlugin 中名称一致</span>
    <span class="hljs-attr">library</span>: <span class="hljs-string">'[name]_[hash]'</span>
  &#125;,
  <span class="hljs-attr">plugins</span>: [
    <span class="hljs-comment">// 清除之前的dll文件</span>
    <span class="hljs-keyword">new</span> CleanWebpackPlugin([<span class="hljs-string">'*.*'</span>], &#123;
      <span class="hljs-attr">root</span>: path.join(__dirname, dllPath)
    &#125;),
    <span class="hljs-comment">// manifest.json 描述动态链接库包含了哪些内容</span>
    <span class="hljs-keyword">new</span> webpack.DllPlugin(&#123;
      <span class="hljs-attr">path</span>: path.join(__dirname, dllPath, <span class="hljs-string">'[name]-manifest.json'</span>),
      <span class="hljs-comment">// 保持与 output.library 中名称一致</span>
      <span class="hljs-attr">name</span>: <span class="hljs-string">'[name]_[hash]'</span>,
      <span class="hljs-attr">context</span>: process.cwd()
    &#125;)
  ]
<span class="hljs-number">12</span>

<span class="copy-code-btn">复制代码</span></code></pre>
<p>在<code>vue.config.js plugin</code>中使用</p>
<pre><code class="hljs language-javascript copyable" lang="javascript">config.plugin.push(
  <span class="hljs-keyword">new</span> DllReferencePlugin(&#123;
    <span class="hljs-attr">context</span>: process.cwd(),
    <span class="hljs-attr">manifest</span>: <span class="hljs-built_in">require</span>(<span class="hljs-string">'./public/vendor/vendor-manifest.json'</span>)
  &#125;),
    <span class="hljs-keyword">new</span> DllReferencePlugin(&#123;
    <span class="hljs-attr">context</span>: process.cwd(),
    <span class="hljs-attr">manifest</span>: <span class="hljs-built_in">require</span>(<span class="hljs-string">'./public/vendor/utils-manifest.json'</span>)
  &#125;),
    <span class="hljs-comment">// 将 dll 注入到 生成的 html 模板中</span>
    <span class="hljs-keyword">new</span> AddAssetHtmlPlugin(&#123;
    <span class="hljs-comment">// dll文件位置</span>
    <span class="hljs-attr">filepath</span>: getPath(<span class="hljs-string">'./public/vendor/*.js'</span>),
    <span class="hljs-comment">// dll 引用路径</span>
    <span class="hljs-attr">publicPath</span>: <span class="hljs-string">'./vendor'</span>,
    <span class="hljs-comment">// dll最终输出的目录</span>
    <span class="hljs-attr">outputPath</span>: <span class="hljs-string">'./vendor'</span>
  &#125;)
)
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-22">splitChunks 分割代码</h3>
<p><a href="https://webpack.docschina.org/plugins/split-chunks-plugin/" target="_blank" rel="nofollow noopener noreferrer">split-chunks-plugin webpack</a></p>
<ul>
<li>chunks: 表示哪些代码需要优化，有三个可选值：initial(初始块)、async(按需加载块)、all(全部块)，默认为async</li>
<li>minSize: 表示在压缩前的最小模块大小，默认为30000</li>
<li>minChunks: 表示被引用次数，默认为1</li>
<li>maxAsyncRequests: 按需加载时候最大的并行请求数，默认为5</li>
<li>maxInitialRequests: 一个入口最大的并行请求数，默认为3</li>
<li>automaticNameDelimiter: 命名连接符</li>
<li>name: 拆分出来块的名字，默认由块名和hash值自动生成</li>
<li>cacheGroups: 缓存组。缓存组的属性除上面所有属性外，还有test, priority, reuseExistingChunk
<ul>
<li>test: 用于控制哪些模块被这个缓存组匹配到</li>
<li>priority: 缓存组打包的先后优先级</li>
<li>reuseExistingChunk: 如果当前代码块包含的模块已经有了，就不在产生一个新的代码块</li>
</ul>
</li>
</ul>
<pre><code class="hljs language-javascript copyable" lang="javascript">config.optimization = &#123;
  <span class="hljs-attr">runtimeChunk</span>: <span class="hljs-string">'single'</span>,
  <span class="hljs-attr">splitChunks</span>: &#123;
    <span class="hljs-attr">chunks</span>: <span class="hljs-string">'all'</span>, <span class="hljs-comment">// 表示哪些代码需要优化，有三个可选值：initial(初始块)、async(按需加载块)、all(全部块)，默认为async</span>
    <span class="hljs-attr">maxInitialRequests</span>: <span class="hljs-literal">Infinity</span>, <span class="hljs-comment">// 按需加载时候最大的并行请求数，默认为5</span>
    <span class="hljs-attr">minSize</span>: <span class="hljs-number">30000</span>, <span class="hljs-comment">// 依赖包超过300000bit将被单独打包</span>
    <span class="hljs-comment">// 缓存组</span>
    <span class="hljs-comment">// priority: 缓存组打包的先后优先级</span>
    <span class="hljs-comment">// minChunks: 表示被引用次数，默认为1</span>
    <span class="hljs-attr">cacheGroups</span>: &#123;
      <span class="hljs-comment">//公共模块</span>
      <span class="hljs-attr">commons</span>: &#123;
        <span class="hljs-attr">name</span>: <span class="hljs-string">'chunk-commons'</span>,
        <span class="hljs-attr">test</span>: resolve(<span class="hljs-string">'src'</span>), <span class="hljs-comment">// can customize your rules</span>
        <span class="hljs-attr">minSize</span>: <span class="hljs-number">100</span>, <span class="hljs-comment">//大小超过100个字节</span>
        <span class="hljs-attr">minChunks</span>: <span class="hljs-number">3</span>, <span class="hljs-comment">//  minimum common number</span>
        <span class="hljs-attr">priority</span>: <span class="hljs-number">5</span>,
        <span class="hljs-attr">reuseExistingChunk</span>: <span class="hljs-literal">true</span>
      &#125;,
      <span class="hljs-comment">// 第三方库</span>
      <span class="hljs-attr">libs</span>: &#123;
        <span class="hljs-attr">name</span>: <span class="hljs-string">'chunk-libs'</span>,
        <span class="hljs-attr">test</span>: <span class="hljs-regexp">/[\\/]node_modules[\\/]/</span>,
        priority: <span class="hljs-number">10</span>,
        <span class="hljs-attr">chunks</span>: <span class="hljs-string">'initial'</span>, <span class="hljs-comment">// only package third parties that are initially dependent</span>
        <span class="hljs-attr">reuseExistingChunk</span>: <span class="hljs-literal">true</span>,
        <span class="hljs-attr">enforce</span>: <span class="hljs-literal">true</span>
      &#125;,
      <span class="hljs-attr">echarts</span>: &#123;
        <span class="hljs-attr">name</span>: <span class="hljs-string">'chunk-echarts'</span>,
        <span class="hljs-attr">test</span>: <span class="hljs-regexp">/[\\/]node_modules[\\/]echarts[\\/]/</span>,
        chunks: <span class="hljs-string">'all'</span>,
        <span class="hljs-attr">priority</span>: <span class="hljs-number">12</span>,
        <span class="hljs-attr">reuseExistingChunk</span>: <span class="hljs-literal">true</span>,
        <span class="hljs-attr">enforce</span>: <span class="hljs-literal">true</span>
      &#125;
    &#125;
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-23">总结</h2>
<p>以上是我在公司项目做的一些小优化，对其他项目不一定适用，甚至使用上也不是最优，但目前对本项目很大程度上还是有帮助的。更多webpack优化的思路，我附上个思维导图吧。(仅供学习，记录📝)
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/dbedc66bbafc46ecbf24566346569527~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-24">其他</h2>
<p><a href="https://cli.vuejs.org/zh/" target="_blank" rel="nofollow noopener noreferrer">Vue CLI</a></p>
<p><a href="https://github.com/fncheng/blog/issues/26" target="_blank" rel="nofollow noopener noreferrer">vue-cli中的configureWebpack设置</a></p>
<p><a href="https://shanyue.tech/frontend-engineering/docker.html#" target="_blank" rel="nofollow noopener noreferrer">如何使用 docker 部署前端项目</a></p></div>  
</div>
            