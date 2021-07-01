
---
title: 'Vue3知识点，vue.config.js配置和组合式api的使用。'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/1bd101840df446c78d52e9c14711aae7~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Wed, 30 Jun 2021 01:01:27 GMT
thumbnail: 'https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/1bd101840df446c78d52e9c14711aae7~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h3 data-id="heading-0">Vue3知识点</h3>
<h4 data-id="heading-1">1、vue.config.js配置</h4>
<h5 data-id="heading-2"><strong>创建vue.config.js</strong></h5>
<p><code>vue.config.js</code> 是一个可选的配置文件，如果项目的 (和 <code>package.json</code> 同级的) 根目录中存在这个文件，那么它会被 <code>@vue/cli-service</code> 自动加载。</p>
<p>这个文件应该导出一个包含了选项的对象：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// vue.config.js</span>
<span class="hljs-built_in">module</span>.exports = &#123;
  <span class="hljs-comment">// 选项...</span>
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h5 data-id="heading-3"><strong>配置选项</strong></h5>
<h6 data-id="heading-4">publicPath</h6>
<ul>
<li>Type: <code>string</code></li>
<li>Default: <code>'/'</code></li>
</ul>
<p>这个值也可以被设置为空字符串 ('') 或是相对路径 ('./')，这样所有的资源都会被链接为相对路径，这样打出来的包可以被部署在任意路径。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// 这里的webpack配置会和公共的webpack.config.js进行合并</span>
<span class="hljs-built_in">module</span>.exports = &#123;
  <span class="hljs-comment">// 执行 npm run build 统一配置文件路径（本地访问dist/index.html需'./'）</span>
  <span class="hljs-attr">publicPath</span>: <span class="hljs-string">'./'</span>,
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h6 data-id="heading-5">outputDir</h6>
<ul>
<li>
<p>Type: <code>string</code></p>
</li>
<li>
<p>Default: <code>'dist'</code></p>
<p>当运行 <code>vue-cli-service build</code> 时生成的生产环境构建文件的目录。注意目标目录在构建之前会被清除 (构建时传入 <code>--no-clean</code> 可关闭该行为)。</p>
</li>
</ul>
<pre><code class="hljs language-js copyable" lang="js">outputDir:<span class="hljs-string">'dist'</span>, <span class="hljs-comment">// 打包文件输出目录, 默认打包到dist文件下</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h6 data-id="heading-6">assetsDir</h6>
<ul>
<li>
<p>Type: <code>string</code></p>
</li>
<li>
<p>Default: <code>''</code></p>
<p>放置生成的静态资源 (js、css、img、fonts) 的 (相对于 <code>outputDir</code> 的) 目录。</p>
</li>
</ul>
<pre><code class="hljs language-js copyable" lang="js">assetsDir:<span class="hljs-string">'static'</span>, <span class="hljs-comment">// 放置静态资源</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h6 data-id="heading-7">pages</h6>
<ul>
<li>
<p>Type: <code>Object</code></p>
</li>
<li>
<p>Default: <code>undefined</code></p>
<p>在 multi-page 模式下构建应用。每个“page”应该有一个对应的 JavaScript 入口文件。其值应该是一个对象，对象的 key 是入口的名字，value 是：</p>
<ul>
<li>一个指定了 <code>entry</code>, <code>template</code>, <code>filename</code>, <code>title</code> 和 <code>chunks</code> 的对象 (除了 <code>entry</code> 之外都是可选的)；</li>
<li>或一个指定其 <code>entry</code> 的字符串。</li>
</ul>
</li>
</ul>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-built_in">module</span>.exports = &#123;
  <span class="hljs-attr">pages</span>:&#123;
    <span class="hljs-attr">index</span>:&#123;
      <span class="hljs-comment">// page 的入口</span>
      <span class="hljs-attr">entry</span>: <span class="hljs-string">'src/main.js'</span>,
      <span class="hljs-comment">// 模板来源</span>
      <span class="hljs-attr">template</span>: <span class="hljs-string">'public/index.html'</span>,
      <span class="hljs-comment">// 修改模板引擎title</span>
      <span class="hljs-attr">title</span>:<span class="hljs-string">"Vue3 学习"</span>,
      <span class="hljs-comment">// 在 dist/index.html 的输出</span>
      <span class="hljs-attr">filename</span>: <span class="hljs-string">'index.html'</span>,
    &#125;
  &#125;,
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h6 data-id="heading-8">lintOnSave</h6>
<ul>
<li>
<p>Type: <code>boolean</code> | <code>'warning'</code> | <code>'default'</code> | <code>'error'</code></p>
</li>
<li>
<p>Default: <code>'default'</code></p>
</li>
<li>
<p>是否在保存的时候使用 <code>eslint-loader</code> 进行检查。 有效的值：<code>ture</code> | <code>false</code> | <code>"error"</code>  当设置为 <code>"error"</code> 时，检查出的错误会触发编译失败。</p>
</li>
</ul>
<pre><code class="hljs language-js copyable" lang="js">lintOnSave: <span class="hljs-literal">false</span>, <span class="hljs-comment">// 设置是否在开发环境下每次保存代码时都启用 eslint验证</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h6 data-id="heading-9">chainWebpack</h6>
<ul>
<li>
<p>Type: <code>Function</code></p>
<p>是一个函数，会接收一个基于 <a href="https://github.com/mozilla-neutrino/webpack-chain" target="_blank" rel="nofollow noopener noreferrer">webpack-chain</a> 的 <code>ChainableConfig</code> 实例。允许对内部的 webpack 配置进行更细粒度的修改。</p>
<p>更多细节可查阅：<a href="https://cli.vuejs.org/zh/guide/webpack.html#%E9%93%BE%E5%BC%8F%E6%93%8D%E4%BD%9C-%E9%AB%98%E7%BA%A7" target="_blank" rel="nofollow noopener noreferrer">配合 webpack > 链式操作</a></p>
</li>
</ul>
<pre><code class="hljs language-js copyable" lang="js">chainWebpack:<span class="hljs-function"><span class="hljs-params">config</span> =></span> &#123; <span class="hljs-comment">// 允许对内部的 webpack 配置进行更细粒度的修改。</span>
    config.module
    .rule(<span class="hljs-string">'images'</span>)
      .use(<span class="hljs-string">'url-loader'</span>)
        .loader(<span class="hljs-string">'url-loader'</span>)
        .tap(<span class="hljs-function"><span class="hljs-params">options</span> =></span> <span class="hljs-built_in">Object</span>.assign(options, &#123; <span class="hljs-attr">limit</span>: <span class="hljs-number">10240</span> &#125;))
  &#125;,
<span class="copy-code-btn">复制代码</span></code></pre>
<h6 data-id="heading-10">devServer</h6>
<ul>
<li>
<p>Type: <code>Object</code></p>
<p><a href="https://webpack.js.org/configuration/dev-server/" target="_blank" rel="nofollow noopener noreferrer">所有 <code>webpack-dev-server</code> 的选项</a>都支持。注意：</p>
<ul>
<li>有些值像 <code>host</code>、<code>port</code> 和 <code>https</code> 可能会被命令行参数覆写。</li>
<li>有些值像 <code>publicPath</code> 和 <code>historyApiFallback</code> 不应该被修改，因为它们需要和开发服务器的 <a href="https://cli.vuejs.org/zh/config/#publicpath" target="_blank" rel="nofollow noopener noreferrer">publicPath</a> 同步以保障正常的工作。</li>
</ul>
</li>
</ul>
<pre><code class="hljs language-js copyable" lang="js">devServer:&#123;
    <span class="hljs-attr">host</span>: <span class="hljs-string">'localhost'</span>,
    <span class="hljs-attr">port</span>: <span class="hljs-number">8090</span>, <span class="hljs-comment">// 端口号</span>
    <span class="hljs-attr">hotOnly</span>: <span class="hljs-literal">false</span>, <span class="hljs-comment">// 热更新</span>
    <span class="hljs-attr">https</span>: <span class="hljs-literal">false</span>,<span class="hljs-comment">// https:&#123;type:Boolean&#125;配置前缀</span>
    <span class="hljs-attr">open</span>: <span class="hljs-literal">false</span>,<span class="hljs-comment">//配置自动启动浏览器</span>
    <span class="hljs-attr">proxy</span>: &#123;
      <span class="hljs-string">'/api'</span>: &#123;
        <span class="hljs-attr">target</span>: <span class="hljs-string">'url'</span>,
        <span class="hljs-comment">// 是否允许跨域</span>
        <span class="hljs-attr">changeOrigin</span>: <span class="hljs-literal">true</span>,
        <span class="hljs-attr">secure</span>: <span class="hljs-literal">false</span>, <span class="hljs-comment">// 如果是https接口，需要配置这个参数</span>
        <span class="hljs-attr">ws</span>: <span class="hljs-literal">true</span>, <span class="hljs-comment">//如果要代理 websockets，配置这个参数</span>
        <span class="hljs-attr">pathRewrite</span>: &#123;
          <span class="hljs-string">'^/api'</span>: <span class="hljs-string">''</span>
        &#125;
      &#125;
    &#125;
  &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h6 data-id="heading-11">完整配置</h6>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-built_in">module</span>.exports = &#123;
  <span class="hljs-comment">// 选项...</span>
  <span class="hljs-attr">publicPath</span>: process.env.NODE_ENV === <span class="hljs-string">'production'</span>? <span class="hljs-string">''</span>: <span class="hljs-string">'/'</span>, <span class="hljs-comment">// 通常用于确定在开发环境还是生产环境</span>
  <span class="hljs-attr">outputDir</span>:<span class="hljs-string">'dist'</span>, <span class="hljs-comment">// 打包文件输出目录, 默认打包到dist文件下</span>
  <span class="hljs-attr">assetsDir</span>:<span class="hljs-string">'static'</span>, <span class="hljs-comment">// 放置静态资源</span>
  <span class="hljs-attr">pages</span>:&#123;
    <span class="hljs-attr">index</span>:&#123;
      <span class="hljs-comment">// page 的入口</span>
      <span class="hljs-attr">entry</span>: <span class="hljs-string">'src/main.js'</span>,
      <span class="hljs-comment">// 模板来源</span>
      <span class="hljs-attr">template</span>: <span class="hljs-string">'public/index.html'</span>,
      <span class="hljs-comment">// 修改模板引擎title</span>
      <span class="hljs-attr">title</span>:<span class="hljs-string">"Vue3 学习"</span>,
      <span class="hljs-comment">// 在 dist/index.html 的输出</span>
      <span class="hljs-attr">filename</span>: <span class="hljs-string">'index.html'</span>,
    &#125;
  &#125;,
  <span class="hljs-attr">lintOnSave</span>: <span class="hljs-literal">false</span>, <span class="hljs-comment">// 设置是否在开发环境下每次保存代码时都启用 eslint验证</span>
  <span class="hljs-attr">runtimeCompiler</span>:<span class="hljs-literal">false</span>, <span class="hljs-comment">// 是否使用带有浏览器内编译器的完整构建版本</span>
  <span class="hljs-attr">configureWebpack</span>: &#123; <span class="hljs-comment">// 别名配置</span>
    <span class="hljs-attr">resolve</span>: &#123;
      <span class="hljs-attr">alias</span>: &#123;
        <span class="hljs-string">'src'</span>: <span class="hljs-string">'@'</span>, <span class="hljs-comment">// 默认已配置</span>
        <span class="hljs-string">'assets'</span>: <span class="hljs-string">'@/assets'</span>,
        <span class="hljs-string">'common'</span>: <span class="hljs-string">'@/common'</span>,
        <span class="hljs-string">'components'</span>: <span class="hljs-string">'@/components'</span>,
        <span class="hljs-string">'api'</span>: <span class="hljs-string">'@/api'</span>,
        <span class="hljs-string">'views'</span>: <span class="hljs-string">'@/views'</span>,
        <span class="hljs-string">'plugins'</span>: <span class="hljs-string">'@/plugins'</span>,
        <span class="hljs-string">'utils'</span>: <span class="hljs-string">'@/utils'</span>,
      &#125;
    &#125;
  &#125;,
  <span class="hljs-comment">//打包的css路径及命名</span>
  <span class="hljs-attr">css</span>: &#123;
    <span class="hljs-attr">modules</span>: <span class="hljs-literal">false</span>,
    <span class="hljs-comment">//vue 文件中修改css 不生效 注释掉  extract:true</span>
    <span class="hljs-attr">extract</span>: &#123;
      <span class="hljs-attr">filename</span>: <span class="hljs-string">"style/[name].[hash:8].css"</span>,
      <span class="hljs-attr">chunkFilename</span>: <span class="hljs-string">"style/[name].[hash:8].css"</span>
    &#125;
  &#125;,
  <span class="hljs-attr">chainWebpack</span>:<span class="hljs-function"><span class="hljs-params">config</span> =></span> &#123; <span class="hljs-comment">// 允许对内部的 webpack 配置进行更细粒度的修改。</span>
    config.module
    .rule(<span class="hljs-string">'images'</span>)
      .use(<span class="hljs-string">'url-loader'</span>)
        .loader(<span class="hljs-string">'url-loader'</span>)
        .tap(<span class="hljs-function"><span class="hljs-params">options</span> =></span> <span class="hljs-built_in">Object</span>.assign(options, &#123; <span class="hljs-attr">limit</span>: <span class="hljs-number">10240</span> &#125;))
  &#125;,
  <span class="hljs-attr">devServer</span>:&#123;
    <span class="hljs-attr">host</span>: <span class="hljs-string">'localhost'</span>,
    <span class="hljs-attr">port</span>: <span class="hljs-number">8090</span>, <span class="hljs-comment">// 端口号</span>
    <span class="hljs-attr">hotOnly</span>: <span class="hljs-literal">false</span>, <span class="hljs-comment">// 热更新</span>
    <span class="hljs-attr">https</span>: <span class="hljs-literal">false</span>,<span class="hljs-comment">// https:&#123;type:Boolean&#125;配置前缀</span>
    <span class="hljs-attr">open</span>: <span class="hljs-literal">false</span>,<span class="hljs-comment">//配置自动启动浏览器</span>
    <span class="hljs-attr">proxy</span>: &#123;
      <span class="hljs-string">'/api'</span>: &#123;
        <span class="hljs-attr">target</span>: <span class="hljs-string">'url'</span>,
        <span class="hljs-comment">// 是否允许跨域</span>
        <span class="hljs-attr">changeOrigin</span>: <span class="hljs-literal">true</span>,
        <span class="hljs-attr">secure</span>: <span class="hljs-literal">false</span>, <span class="hljs-comment">// 如果是https接口，需要配置这个参数</span>
        <span class="hljs-attr">ws</span>: <span class="hljs-literal">true</span>, <span class="hljs-comment">//如果要代理 websockets，配置这个参数</span>
        <span class="hljs-attr">pathRewrite</span>: &#123;
          <span class="hljs-string">'^/api'</span>: <span class="hljs-string">''</span>
        &#125;
      &#125;
    &#125;
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-12">2、Vue3核心语法</h4>
<p>关于<code>Composition API</code>这里有大佬做的动画演示，极力推荐。</p>
<p><a href="https://juejin.cn/post/6891640356543627278" target="_blank">那个忙了一夜的Vue3动画很好，就是太短了</a></p>
<p><strong>Option的缺陷--反复横跳</strong></p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// options API</span>
<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> &#123;
  <span class="hljs-attr">components</span>: &#123; RepositoriesFilters, RepositoriesSortBy, RepositoriesList &#125;,
  <span class="hljs-attr">props</span>: &#123;
    <span class="hljs-attr">user</span>: &#123; 
      <span class="hljs-attr">type</span>: <span class="hljs-built_in">String</span>,
      <span class="hljs-attr">required</span>: <span class="hljs-literal">true</span>
    &#125;
  &#125;,
  data () &#123;
    <span class="hljs-keyword">return</span> &#123;
      <span class="hljs-attr">repositories</span>: [], <span class="hljs-comment">// 1</span>
      <span class="hljs-attr">filters</span>: &#123; ... &#125;, <span class="hljs-comment">// 3</span>
      <span class="hljs-attr">searchQuery</span>: <span class="hljs-string">''</span> <span class="hljs-comment">// 2</span>
    &#125;
  &#125;,
  <span class="hljs-attr">computed</span>: &#123;
    filteredRepositories () &#123; ... &#125;, <span class="hljs-comment">// 3</span>
    repositoriesMatchingSearchQuery () &#123; ... &#125;, <span class="hljs-comment">// 2</span>
  &#125;,
  <span class="hljs-attr">watch</span>: &#123;
    <span class="hljs-attr">user</span>: <span class="hljs-string">'getUserRepositories'</span> <span class="hljs-comment">// 1</span>
  &#125;,
  <span class="hljs-attr">methods</span>: &#123;
    getUserRepositories () &#123;
      <span class="hljs-comment">// 使用 `this.user` 获取用户仓库</span>
    &#125;, <span class="hljs-comment">// 1</span>
    updateFilters () &#123; ... &#125;, <span class="hljs-comment">// 3</span>
  &#125;,
  mounted () &#123;
    <span class="hljs-built_in">this</span>.getUserRepositories() <span class="hljs-comment">// 1</span>
  &#125;
&#125;

<span class="copy-code-btn">复制代码</span></code></pre>
<p>这种碎片化使得理解和维护复杂组件变得困难。选项的分离掩盖了潜在的逻辑问题。此外，在处理单个逻辑关注点时，我们必须不断地**“反复跳转”**相关代码的选项块。</p>
<p>需求复杂之后，就会多出watch，computed，inject，provide等配置，这个.vue文件也会逐渐增大。</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/1bd101840df446c78d52e9c14711aae7~tplv-k3u1fbpfcp-watermark.image" alt="img" loading="lazy" referrerpolicy="no-referrer"></p>
<h5 data-id="heading-13">Composition API</h5>
<ul>
<li>
<p>composition就是为了解决这个问题存在的，通过组合的方式，把零散在各个data，methods的代码，重新组合，一个功能的代码都放在一起维护，并且这些代码可以单独拆分成函数</p>
</li>
<li>
<p><code>Vue3</code>兼容大部分<code>Vue2</code>语法，所以在<code>Vue3</code>中书写<code>Vue2</code>语法是没有问题的（废除的除外）</p>
</li>
</ul>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/d05799744a6341fd908ec03e5916d7b6~tplv-k3u1fbpfcp-watermark.image" alt="img" loading="lazy" referrerpolicy="no-referrer"></p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/4146605abc9c4b638863e9a3f2f1b001~tplv-k3u1fbpfcp-watermark.image" alt="img" loading="lazy" referrerpolicy="no-referrer"></p>
<h6 data-id="heading-14">setup</h6>
<p>作为组合式 API 的入口。 <code>setup</code> 返回的所有内容都暴露给组件的其余部分 (计算属性、方法、生命周期钩子等等) 以及组件的模板。</p>
<p><code>setup</code>只在初始化时执行一次，类似<code>created()</code>一样。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-title">beforeCreate</span>(<span class="hljs-params"></span>)</span>&#123;
  <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'beforeCreate'</span>)
&#125;,
<span class="hljs-function"><span class="hljs-title">created</span>(<span class="hljs-params"></span>)</span> &#123;
   <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'created'</span>)
&#125;,
<span class="hljs-function"><span class="hljs-title">setup</span>(<span class="hljs-params">props</span>)</span> &#123;
   <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'setup'</span>) 
&#125;
<span class="hljs-comment">// setup</span>
<span class="hljs-comment">// beforeCreate</span>
<span class="hljs-comment">// created</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>根据控制台打印循序可以看到<code>setup</code>是在<code>beforeCreate</code>生命周期之前执行的。<code>setup</code> 的调用发生在 <code>data</code> property、<code>computed</code> property 或 <code>methods</code> 被解析之前，所以它们无法在 <code>setup</code> 中被获取。由此可以推断出<code>setup</code>执行的时候,组件对象还没有创建,组件实例对象<code>this</code>还不可用,此时<code>this</code>是<code>undefined</code>, 不能通过<code>this</code>来访问<code>data/computed/methods/props</code>。</p>
<p><strong>setup的使用</strong></p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// html</span>
<button @click=<span class="hljs-string">"handelClick"</span>>&#123;&#123;name&#125;&#125;</button>
<span class="hljs-comment">// js</span>
<span class="hljs-keyword">import</span> &#123; defineComponent, reactive, toRefs, onMounted &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'vue'</span>
<span class="hljs-function"><span class="hljs-title">setup</span>(<span class="hljs-params">props</span>)</span> &#123;
    <span class="hljs-keyword">const</span> state = reactive(&#123;
      <span class="hljs-attr">name</span>:<span class="hljs-string">'点击'</span>
    &#125;)
     <span class="hljs-keyword">const</span> handelClick =<span class="hljs-function">() =></span> &#123;
      <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'handelClick'</span>)
    &#125;
     <span class="hljs-comment">// 这里返回的任何内容都可以用于组件的其余部分</span>
    <span class="hljs-keyword">return</span> &#123;
        ...toRefs(state),
        handelClick
    &#125;
  &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h6 data-id="heading-15">ref 响应式变量</h6>
<p>在 Vue 3.0 中，我们可以通过一个新的 <code>ref</code> 函数使任何响应式变量在任何地方起作用，如下所示：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">import</span> &#123; ref &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'vue'</span>
<span class="hljs-keyword">const</span> counter = ref(<span class="hljs-number">0</span>)
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/764a90724aef4f9d815d2c5e3a0418de~tplv-k3u1fbpfcp-watermark.image" alt="1624957698322.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p><code>ref</code> 接收参数并将其包裹在一个带有 <code>value</code> property 的对象中返回，然后可以使用该 property 访问或更改响应式变量的值：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">import</span> &#123; ref &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'vue'</span>
<span class="hljs-keyword">const</span> count = ref(<span class="hljs-number">0</span>)
<span class="hljs-keyword">const</span> handelClick =<span class="hljs-function">() =></span> &#123;
    <span class="hljs-comment">// 需要使用xxx.value的形式，而模板中不需要添加.value</span>
<span class="hljs-built_in">console</span>.log(count.value)
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>举个栗子：点击事件触发count增加</p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">template</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">div</span>></span>&#123;&#123;count&#125;&#125;<span class="hljs-tag"></<span class="hljs-name">div</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">button</span> @<span class="hljs-attr">click</span>=<span class="hljs-string">'handelClick'</span>></span>点击<span class="hljs-tag"></<span class="hljs-name">button</span>></span>
<span class="hljs-tag"></<span class="hljs-name">template</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>在vue2中</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-title">data</span>(<span class="hljs-params"></span>)</span> &#123;
  <span class="hljs-keyword">return</span> &#123;
    <span class="hljs-attr">conunt</span>: <span class="hljs-number">0</span>,
  &#125;;
&#125;,
<span class="hljs-attr">methods</span>: &#123;
  <span class="hljs-function"><span class="hljs-title">handelClick</span>(<span class="hljs-params"></span>)</span> &#123;
    <span class="hljs-comment">// 需要使用xxx.value的形式，而模板中不需要添加.value</span>
    <span class="hljs-built_in">this</span>.conunt++;
  &#125;,
&#125;,
<span class="copy-code-btn">复制代码</span></code></pre>
<p>在vue3中</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">import</span> &#123; ref &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'vue'</span>
<span class="hljs-function"><span class="hljs-title">setup</span>(<span class="hljs-params"></span>)</span> &#123;
    <span class="hljs-keyword">const</span> count = ref(<span class="hljs-number">0</span>)
    <span class="hljs-keyword">const</span> handelClick =<span class="hljs-function">() =></span> &#123;
      count.value++
    &#125;
    <span class="hljs-keyword">return</span> &#123;
        count,
        handelClick
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h6 data-id="heading-16">reactive</h6>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> obj = reactive(obj)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>响应式转换是“深层”的——它影响所有嵌套 property。在基于 <a href="https://developer.mozilla.org/zh-CN/docs/Web/JavaScript/Reference/Global_Objects/Proxy" target="_blank" rel="nofollow noopener noreferrer">ES2015 Proxy</a> 的实现中，返回的 proxy 是<strong>不</strong>等于原始对象的。建议只使用响应式 proxy，避免依赖原始对象。<strong>处理更复杂的数据，通常用于对象和数组</strong></p>
<p>模拟ajax请求返回一段数组</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// html</span>
<banner :bannerList=<span class="hljs-string">"bannerList"</span>></banner>
<span class="hljs-comment">// js</span>
<span class="hljs-keyword">import</span> &#123; defineComponent, reactive, toRefs, ref &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'vue'</span>
<span class="hljs-keyword">import</span> api <span class="hljs-keyword">from</span> <span class="hljs-string">'@/api/api.js'</span>
<span class="hljs-function"><span class="hljs-title">setup</span>(<span class="hljs-params"></span>)</span> &#123;
    <span class="hljs-keyword">const</span> state = reactive(&#123;
      <span class="hljs-attr">bannerList</span>: [], <span class="hljs-comment">// 轮播图</span>
    &#125;)
    <span class="hljs-keyword">const</span> getBanners = <span class="hljs-keyword">async</span> () => &#123;
      <span class="hljs-keyword">const</span> &#123;code,data&#125; = <span class="hljs-keyword">await</span> api.queryBannersByPosition(&#123;<span class="hljs-attr">position</span>:<span class="hljs-number">1</span>&#125;)
      <span class="hljs-keyword">if</span>(code == <span class="hljs-number">1</span>) &#123;
        state.bannerList = data;
      &#125;
    &#125;
    getBanners();
    <span class="hljs-keyword">return</span> &#123;
      ...toRefs(state),
    &#125;
  &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h6 data-id="heading-17">toRefs</h6>
<p>将响应式对象转换为普通对象，其中结果对象的每个 property 都是指向原始对象相应 property 的 <a href="https://v3.cn.vuejs.org/api/refs-api.html#ref" target="_blank" rel="nofollow noopener noreferrer"><code>ref</code></a>`</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">useFeatureX</span>(<span class="hljs-params"></span>) </span>&#123;
  <span class="hljs-keyword">const</span> state = reactive(&#123;
    <span class="hljs-attr">foo</span>: <span class="hljs-number">1</span>,
    <span class="hljs-attr">bar</span>: <span class="hljs-number">2</span>
  &#125;)
  <span class="hljs-comment">// 操作 state 的逻辑</span>

  <span class="hljs-comment">// 返回时转换为ref</span>
  <span class="hljs-keyword">return</span> &#123;
      <span class="hljs-comment">//通过toRefs返回的对象,解构出来的属性也是响应式的</span>
      ...toRefs(state)
  &#125;
&#125;
<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> &#123;
  <span class="hljs-function"><span class="hljs-title">setup</span>(<span class="hljs-params"></span>)</span> &#123;
    <span class="hljs-comment">// 可以在不失去响应性的情况下解构</span>
    <span class="hljs-keyword">const</span> &#123; foo, bar &#125; = useFeatureX()

    <span class="hljs-keyword">return</span> &#123;
      foo,
      bar
    &#125;
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h6 data-id="heading-18">computed计算属性</h6>
<p>与<code>Vue2</code>中的<code>computed</code>配置功能一致，返回的是一个<code>ref</code>类型的对象，计算属性的函数中如果只传入一个回调函数 表示的是<code>get</code>操作</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// html</span>
<div>&#123;&#123;user&#125;&#125;</div>
<span class="hljs-comment">// js</span>
<span class="hljs-keyword">import</span> &#123; defineComponent, reactive,  computed &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'vue'</span>
<span class="hljs-comment">// 计算属性computed</span>
<span class="hljs-function"><span class="hljs-title">setup</span>(<span class="hljs-params"></span>)</span> &#123;
    <span class="hljs-keyword">const</span> objname = reactive(&#123;<span class="hljs-attr">name</span>:<span class="hljs-string">'我的对象'</span>&#125;)
    <span class="hljs-keyword">const</span> user = computed(<span class="hljs-function">() =></span> &#123;
        <span class="hljs-keyword">return</span> objname.name + <span class="hljs-string">'是谁'</span>
    &#125;)
    <span class="hljs-keyword">return</span> &#123;
        user
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>计算属性默认只有 getter，不过在需要时你也可以提供一个 setter：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> user2 = computed(&#123;
    <span class="hljs-function"><span class="hljs-title">get</span>(<span class="hljs-params"></span>)</span> &#123;
        <span class="hljs-keyword">return</span> objname2.name+ <span class="hljs-string">'_'</span>+ objname2.age
    &#125;,
    <span class="hljs-function"><span class="hljs-title">set</span>(<span class="hljs-params">val</span>)</span> &#123;
        <span class="hljs-keyword">const</span> age = val.split(<span class="hljs-string">"_"</span>)
        objname2.name = objname2.name + age[<span class="hljs-number">1</span>]
    &#125;
&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<h6 data-id="heading-19">watch侦听器</h6>
<p>和vue2用法一致，默认情况下，它也是惰性的，即只有当被侦听的源发生变化时才执行回调。</p>
<ul>
<li>参数1:要监听的数据源</li>
<li>参数2:回调函数</li>
<li>参数3:配置</li>
</ul>
<p><strong>侦听单个数据源</strong></p>
<p>侦听器数据源可以是返回值的 getter 函数，也可以直接是 <code>ref</code>：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// 侦听一个 getter</span>
<span class="hljs-keyword">const</span> state = reactive(&#123;
    <span class="hljs-attr">bannerList</span>: [], <span class="hljs-comment">// 轮播图</span>
    <span class="hljs-attr">name</span>:<span class="hljs-string">'点击2'</span>,
    <span class="hljs-attr">count</span>: <span class="hljs-number">0</span>
&#125;)
<span class="hljs-keyword">const</span> handelClick2 =<span class="hljs-function">() =></span> &#123;
      state.count++
    &#125;
watch(
  <span class="hljs-function">() =></span> state.count,
  <span class="hljs-function">(<span class="hljs-params">count, prevCount</span>) =></span> &#123;
   <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'我被监听了'</span>,count, prevCount); <span class="hljs-comment">//logs: 1, 0</span>
  &#125;
)
<span class="hljs-keyword">return</span> &#123;
    ...toRefs(state),
    handelClick2
&#125;
<span class="hljs-comment">// 直接侦听ref</span>
<span class="hljs-keyword">const</span> count = ref(<span class="hljs-number">0</span>)
watch(count, <span class="hljs-function">(<span class="hljs-params">count, prevCount</span>) =></span> &#123;
  <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'我被监听了'</span>,count, prevCount); <span class="hljs-comment">//logs: 1, 0</span>
&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>侦听多个数据源</strong></p>
<p><code>watch</code>监听多个数据,使用数组</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> firstName = ref(<span class="hljs-string">''</span>);
<span class="hljs-keyword">const</span> lastName = ref(<span class="hljs-string">''</span>);

watch([firstName, lastName], <span class="hljs-function">(<span class="hljs-params">newValues, prevValues</span>) =></span> &#123;
  <span class="hljs-built_in">console</span>.log(newValues, prevValues);
&#125;)

firstName.value = <span class="hljs-string">"John"</span>; <span class="hljs-comment">// logs: ["John",""] ["", ""]</span>
lastName.value = <span class="hljs-string">"Smith"</span>; <span class="hljs-comment">// logs: ["John", "Smith"] ["John", ""]</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>侦听响应式对象</strong></p>
<p>使用侦听器来比较一个数组或对象的值，这些值是响应式的，要求它有一个由值构成的副本。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> numbers = reactive([<span class="hljs-number">1</span>, <span class="hljs-number">2</span>, <span class="hljs-number">3</span>, <span class="hljs-number">4</span>])

watch(
  <span class="hljs-function">() =></span> [...numbers],
  <span class="hljs-function">(<span class="hljs-params">numbers, prevNumbers</span>) =></span> &#123;
    <span class="hljs-built_in">console</span>.log(numbers, prevNumbers);
  &#125;)

numbers.push(<span class="hljs-number">5</span>) <span class="hljs-comment">// logs: [1,2,3,4,5] [1,2,3,4]</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h6 data-id="heading-20">watchEffect</h6>
<p>为了根据响应式状态<em>自动应用</em>和<em>重新应用</em>副作用，我们可以使用 <code>watchEffect</code> 方法。它立即执行传入的一个函数，同时响应式追踪其依赖，并在其依赖变更时重新运行该函数。</p>
<p>对比：</p>
<p><code>watch</code>当值监听到变化的时候才执行，但可以通过配置<code>immediate</code>为<code>true</code>, 来指定初始时立即执行第一次。</p>
<p><code>watchEffect</code>可以立即执行第一次。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> count = ref(<span class="hljs-number">0</span>)
watchEffect(<span class="hljs-function">() =></span> &#123;
<span class="hljs-built_in">console</span>.log(<span class="hljs-string">'我被监听了'</span>,count.value); <span class="hljs-comment">// logs: 我被监听了 0</span>
&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>停止侦听</strong></p>
<p>当 <code>watchEffect</code> 在组件的 <a href="https://v3.cn.vuejs.org/guide/composition-api-setup.html" target="_blank" rel="nofollow noopener noreferrer">setup()</a> 函数或<a href="https://v3.cn.vuejs.org/guide/composition-api-lifecycle-hooks.html" target="_blank" rel="nofollow noopener noreferrer">生命周期钩子</a>被调用时，侦听器会被链接到该组件的生命周期，并在组件卸载时自动停止。</p>
<p>在一些情况下，也可以显式调用返回值以停止侦听：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> stop = watchEffect(<span class="hljs-function">() =></span> &#123;
  <span class="hljs-comment">/* ... */</span>
&#125;)

<span class="hljs-comment">// later</span>
stop()
<span class="copy-code-btn">复制代码</span></code></pre>
<h6 data-id="heading-21">生命周期钩子</h6>
<p>你可以通过在生命周期钩子前面加上 “on” 来访问组件的生命周期钩子。</p>
<p>下表包含如何在 <a href="https://v3.cn.vuejs.org/guide/composition-api-setup.html" target="_blank" rel="nofollow noopener noreferrer">setup ()</a> 内部调用生命周期钩子：</p>





























































<table><thead><tr><th>选项式 API</th><th>Hook inside <code>setup</code></th></tr></thead><tbody><tr><td><code>beforeCreate</code></td><td>Not needed*</td></tr><tr><td><code>created</code></td><td>Not needed*</td></tr><tr><td><code>beforeMount</code></td><td><code>onBeforeMount</code></td></tr><tr><td><code>mounted</code></td><td><code>onMounted</code></td></tr><tr><td><code>beforeUpdate</code></td><td><code>onBeforeUpdate</code></td></tr><tr><td><code>updated</code></td><td><code>onUpdated</code></td></tr><tr><td><code>beforeUnmount</code></td><td><code>onBeforeUnmount</code></td></tr><tr><td><code>unmounted</code></td><td><code>onUnmounted</code></td></tr><tr><td><code>errorCaptured</code></td><td><code>onErrorCaptured</code></td></tr><tr><td><code>renderTracked</code></td><td><code>onRenderTracked</code></td></tr><tr><td><code>renderTriggered</code></td><td><code>onRenderTriggered</code></td></tr><tr><td><code>activated</code></td><td><code>onActivated</code></td></tr><tr><td><code>deactivated</code></td><td><code>onDeactivated</code></td></tr></tbody></table>
<p>TIP</p>
<p>因为 <code>setup</code> 是围绕 <code>beforeCreate</code> 和 <code>created</code> 生命周期钩子运行的，所以不需要显式地定义它们。换句话说，在这些钩子中编写的任何代码都应该直接在 <code>setup</code> 函数中编写。</p>
<p><strong>新的生命周期</strong></p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-title">setup</span>(<span class="hljs-params">props,context</span>)</span> &#123;
    onBeforeMount(<span class="hljs-function">() =></span> &#123;
        <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'onBeforeMount'</span>)
    &#125;)
    onMounted(<span class="hljs-function">() =></span> &#123;
        <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'onMounted'</span>)
    &#125;)
    onBeforeUpdate(<span class="hljs-function">() =></span> &#123;
        <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'onBeforeUpdate'</span>);
    &#125;)
    <span class="hljs-comment">// 视图更新时渲染</span>
    onUpdated(<span class="hljs-function">() =></span> &#123;
        <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'onUpdated'</span>);
    &#125;)
    onUnmounted(<span class="hljs-function">() =></span> &#123;
        <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'onUnmounted'</span>)
    &#125;)
    <span class="hljs-comment">// 首次渲染执行</span>
    onRenderTracked(<span class="hljs-function">() =></span> &#123;
        <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'onRenderTracked'</span>)
    &#125;)
    <span class="hljs-comment">// 页面重新渲染</span>
    onRenderTriggered(<span class="hljs-function">() =></span> &#123;
        <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'onRenderTriggered'</span>)
    &#125;)
    <span class="hljs-keyword">const</span> name = ref(<span class="hljs-string">'张三'</span>)
    <span class="hljs-keyword">const</span> handelClick = <span class="hljs-function">() =></span> &#123;
        name.value = <span class="hljs-string">'wujf'</span>
    &#125;
    <span class="hljs-keyword">return</span> &#123;
        name,
        handelClick
    &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h6 data-id="heading-22">provide 与 inject</h6>
<p>我们也可以在组合式 API 中使用 <a href="https://v3.cn.vuejs.org/guide/component-provide-inject.html" target="_blank" rel="nofollow noopener noreferrer">provide/inject</a>。两者都只能在当前活动实例的 <a href="https://v3.cn.vuejs.org/guide/composition-api-setup.html" target="_blank" rel="nofollow noopener noreferrer"><code>setup()</code></a> 期间调用。</p>
<p>作用：实现跨层级组件间通信</p>
<p><code>provide</code> 函数允许你通过两个参数定义 property：</p>
<ol>
<li>name (<code><String></code> 类型)</li>
<li>value</li>
</ol>
<pre><code class="hljs language-js copyable" lang="js">provide(name,value)
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// 父组件</span>
<template>
  <span class="xml"><span class="hljs-tag"><<span class="hljs-name">div</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">My-Map</span>></span><span class="hljs-tag"></<span class="hljs-name">My-Map</span>></span>
  <span class="hljs-tag"></<span class="hljs-name">div</span>></span></span>
</template>
<span class="xml"><span class="hljs-tag"><<span class="hljs-name">script</span>></span><span class="javascript">
<span class="hljs-keyword">import</span> &#123; defineComponent, reactive, toRefs, ref, computed, watch,watchEffect, provide &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'vue'</span>
<span class="hljs-keyword">import</span> MyMap <span class="hljs-keyword">from</span> <span class="hljs-string">'@/components/my-map/my-map.vue'</span>
<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> defineComponent(&#123;
  <span class="hljs-attr">components</span>:&#123;
    MyMap
  &#125;,
  <span class="hljs-comment">// provide 与 inject的用法</span>
  <span class="hljs-function"><span class="hljs-title">setup</span>(<span class="hljs-params"></span>)</span> &#123;
    <span class="hljs-keyword">const</span> msg = ref(<span class="hljs-string">'子组件传递信息'</span>)
    <span class="hljs-keyword">const</span> state = reactive(&#123;
      <span class="hljs-attr">obj</span>:&#123;
        <span class="hljs-attr">name</span>: <span class="hljs-string">'网校账'</span>,
        <span class="hljs-attr">age</span>: <span class="hljs-number">19</span>
      &#125;
    &#125;)
    provide(<span class="hljs-string">'msg'</span>,msg)
    provide(<span class="hljs-string">'obj'</span>,state.obj)
  &#125;
&#125;)
</span><span class="hljs-tag"></<span class="hljs-name">script</span>></span></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p><code>inject</code> 函数有两个参数：</p>
<ol>
<li>要 inject 的 property 的 name</li>
<li>默认值 (<strong>可选</strong>)</li>
</ol>
<pre><code class="hljs language-js copyable" lang="js">inject(name)
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="hljs language-js copyable" lang="js"><template>
<!-- 子组件 my-map.vue -->
  <span class="xml"><span class="hljs-tag"><<span class="hljs-name">div</span>></span>
    &#123;&#123;msgF&#125;&#125;
    <span class="hljs-tag"><<span class="hljs-name">div</span>></span>
      名字：&#123;&#123;obj.name&#125;&#125; / 年龄：&#123;&#123;obj.age&#125;&#125;
    <span class="hljs-tag"></<span class="hljs-name">div</span>></span>
  <span class="hljs-tag"></<span class="hljs-name">div</span>></span></span>
</template>
<span class="xml"><span class="hljs-tag"><<span class="hljs-name">script</span>></span><span class="javascript">
<span class="hljs-keyword">import</span> &#123; defineComponent, inject &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'vue'</span>
<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> defineComponent(&#123;
  <span class="hljs-comment">// inject的用法</span>
  <span class="hljs-function"><span class="hljs-title">setup</span>(<span class="hljs-params"></span>)</span> &#123;
    <span class="hljs-keyword">const</span> msgF = inject(<span class="hljs-string">'msg'</span>)
    <span class="hljs-keyword">const</span> obj = inject(<span class="hljs-string">'obj'</span>)
    <span class="hljs-keyword">return</span> &#123;
      msgF,
      obj
    &#125;
  &#125;
&#125;)
</span><span class="hljs-tag"></<span class="hljs-name">script</span>></span></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>传给子孙组件</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// 父组件</span>
provide(<span class="hljs-string">'my-map-son'</span>,state.obj)
<template>
<!-- 子孙组件 my-map-son.vue -->
  <span class="xml"><span class="hljs-tag"><<span class="hljs-name">div</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">div</span>></span>
      名字：&#123;&#123;obj.name&#125;&#125; / 年龄：&#123;&#123;obj.age&#125;&#125;
    <span class="hljs-tag"></<span class="hljs-name">div</span>></span>
  <span class="hljs-tag"></<span class="hljs-name">div</span>></span></span>
</template>
<span class="xml"><span class="hljs-tag"><<span class="hljs-name">script</span>></span><span class="javascript">
<span class="hljs-keyword">import</span> &#123; defineComponent, inject &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'vue'</span>
<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> defineComponent(&#123;
  <span class="hljs-comment">// provide 与 inject的用法</span>
  <span class="hljs-function"><span class="hljs-title">setup</span>(<span class="hljs-params"></span>)</span> &#123;
    <span class="hljs-keyword">const</span> obj = inject(<span class="hljs-string">'my-map-son'</span>)
    <span class="hljs-keyword">return</span> &#123;
      obj
    &#125;
  &#125;
&#125;)
</span><span class="hljs-tag"></<span class="hljs-name">script</span>></span></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h6 data-id="heading-23">setup参数的使用</h6>
<p>使用 <code>setup</code> 函数时，它将接收两个参数：</p>
<ol>
<li><code>props</code></li>
<li><code>context</code></li>
</ol>
<p><strong>props</strong>: 是一个对象,里面有父级组件向子级组件传递的数据,并且是在子级组件中使用<code>props</code>接收到的所有的属性</p>
<pre><code class="hljs language-js copyable" lang="js"><!-- 父组件 -->
<span class="xml"><span class="hljs-tag"><<span class="hljs-name">template</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">div</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">My-Map</span> <span class="hljs-attr">:list</span>=<span class="hljs-string">"list"</span>></span><span class="hljs-tag"></<span class="hljs-name">My-Map</span>></span>
  <span class="hljs-tag"></<span class="hljs-name">div</span>></span>
<span class="hljs-tag"></<span class="hljs-name">template</span>></span></span>
<span class="xml"><span class="hljs-tag"><<span class="hljs-name">script</span>></span><span class="javascript">
<span class="hljs-keyword">import</span> &#123; defineComponent &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'vue'</span>
<span class="hljs-keyword">import</span> MyMap <span class="hljs-keyword">from</span> <span class="hljs-string">'@/components/my-map/my-map.vue'</span>
<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> defineComponent(&#123;
  <span class="hljs-attr">components</span>:&#123;
    MyMap
  &#125;,
  <span class="hljs-comment">// provide 与 inject的用法</span>
  <span class="hljs-function"><span class="hljs-title">setup</span>(<span class="hljs-params"></span>)</span> &#123;
    <span class="hljs-keyword">const</span> list = [<span class="hljs-number">1</span>,<span class="hljs-number">2</span>,<span class="hljs-number">3</span>,<span class="hljs-number">4</span>]
    <span class="hljs-keyword">return</span> &#123;
      list
    &#125;
  &#125;
&#125;)
</span><span class="hljs-tag"></<span class="hljs-name">script</span>></span></span>
<span class="hljs-comment">// 子组件</span>
<span class="xml"><span class="hljs-tag"><<span class="hljs-name">template</span>></span>
<span class="hljs-comment"><!-- 子组件 my-map.vue --></span>
  <span class="hljs-tag"><<span class="hljs-name">div</span>></span>
  <span class="hljs-tag"></<span class="hljs-name">div</span>></span>
<span class="hljs-tag"></<span class="hljs-name">template</span>></span></span>
<span class="xml"><span class="hljs-tag"><<span class="hljs-name">script</span>></span><span class="javascript">
<span class="hljs-keyword">import</span> &#123; defineComponent &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'vue'</span>
<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> defineComponent(&#123;
  <span class="hljs-attr">props</span>:&#123;
    <span class="hljs-attr">list</span>:&#123;
      <span class="hljs-attr">type</span>: <span class="hljs-built_in">Array</span>,
      <span class="hljs-attr">default</span>: <span class="hljs-function">() =></span> []
    &#125;
  &#125;,
  <span class="hljs-attr">components</span>:&#123;
    MyMapSon
  &#125;,
  <span class="hljs-function"><span class="hljs-title">setup</span>(<span class="hljs-params">props</span>)</span> &#123;
    <span class="hljs-built_in">console</span>.log(props.list) <span class="hljs-comment">// [1, 2, 3, 4]</span>
  &#125;
&#125;)
</span><span class="hljs-tag"></<span class="hljs-name">script</span>></span></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>注意的一点</strong>：因为 <code>props</code> 是响应式的，你<strong>不能使用 ES6 解构</strong>，它会消除 prop 的响应性。</p>
<p>如果需要解构 prop，可以在 <code>setup</code> 函数中使用 <a href="https://v3.cn.vuejs.org/guide/reactivity-fundamentals.html#%E5%93%8D%E5%BA%94%E5%BC%8F%E7%8A%B6%E6%80%81%E8%A7%A3%E6%9E%84" target="_blank" rel="nofollow noopener noreferrer"><code>toRefs</code></a> 函数来完成此操作：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">import</span> &#123; toRefs &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'vue'</span>
<span class="hljs-function"><span class="hljs-title">setup</span>(<span class="hljs-params">props</span>)</span> &#123;
  <span class="hljs-keyword">const</span> &#123; title &#125; = toRefs(props)
  <span class="hljs-built_in">console</span>.log(title.value)
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>Context</strong>：传递给 <code>setup</code> 函数的第二个参数是 <code>context</code>。<code>context</code> 是一个普通的 <code>JavaScript</code> 对象，它暴露组件的三个 <code>property</code>：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> &#123;
  <span class="hljs-function"><span class="hljs-title">setup</span>(<span class="hljs-params">props, context</span>)</span> &#123;
    <span class="hljs-comment">// Attribute (非响应式对象),获取当前组件标签上所有没有通过props接收的属性的对象, 相当于 this.$attrs</span>
    <span class="hljs-built_in">console</span>.log(context.attrs)

    <span class="hljs-comment">// 插槽 (非响应式对象),包含所有传入的插槽内容的对象, 相当于 this.$slots</span>
    <span class="hljs-built_in">console</span>.log(context.slots)

    <span class="hljs-comment">// 触发事件 (方法),用来分发自定义事件的函数, 相当于 this.$emit</span>
    <span class="hljs-built_in">console</span>.log(context.emit)
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><code>context</code> 是一个普通的 <code>JavaScript</code> 对象，也就是说，它不是响应式的，这意味着你可以安全地对 <code>context</code> 使用 ES6 解构。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// MyBook.vue</span>
<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> &#123;
  <span class="hljs-function"><span class="hljs-title">setup</span>(<span class="hljs-params">props, &#123; attrs, slots, emit &#125;</span>)</span> &#123;
    ...
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><code>attrs</code>使用：获取子组件自定义的数据</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// 父组件</span>
<template>
  <span class="xml"><span class="hljs-tag"><<span class="hljs-name">div</span>></span>
      <span class="hljs-tag"><<span class="hljs-name">my-son</span> <span class="hljs-attr">msg</span>=<span class="hljs-string">"打得你叫爸爸"</span>></span><span class="hljs-tag"></<span class="hljs-name">my-son</span>></span>
  <span class="hljs-tag"></<span class="hljs-name">div</span>></span></span>
</template>
<span class="hljs-comment">// 子组件</span>
<span class="xml"><span class="hljs-tag"><<span class="hljs-name">template</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">div</span>></span>
    子组件
  <span class="hljs-tag"></<span class="hljs-name">div</span>></span>
<span class="hljs-tag"></<span class="hljs-name">template</span>></span></span>
<span class="xml"><span class="hljs-tag"><<span class="hljs-name">script</span>></span><span class="javascript">
<span class="hljs-keyword">import</span> &#123; defineComponent &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'vue'</span>
<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> defineComponent(&#123;
  <span class="hljs-function"><span class="hljs-title">setup</span>(<span class="hljs-params">props,&#123;attrs, slots, emit&#125;</span>)</span> &#123;
    <span class="hljs-built_in">console</span>.log(attrs.msg) <span class="hljs-comment">// 打得你叫爸爸</span>
  &#125;,
&#125;)
</span><span class="hljs-tag"></<span class="hljs-name">script</span>></span></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p><code>slots</code>使用</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// 父组件</span>
<template>
  <span class="xml"><span class="hljs-tag"><<span class="hljs-name">div</span>></span>
      <span class="hljs-tag"><<span class="hljs-name">my-son</span> <span class="hljs-attr">msg</span>=<span class="hljs-string">"打得你叫爸爸"</span>></span>
          获取插槽的内容
  <span class="hljs-tag"></<span class="hljs-name">my-son</span>></span>
  <span class="hljs-tag"></<span class="hljs-name">div</span>></span></span>
</template>
<span class="hljs-comment">// 子组件</span>
<span class="xml"><span class="hljs-tag"><<span class="hljs-name">template</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">div</span>></span>
    子组件
  <span class="hljs-tag"></<span class="hljs-name">div</span>></span>
<span class="hljs-tag"></<span class="hljs-name">template</span>></span></span>
<span class="xml"><span class="hljs-tag"><<span class="hljs-name">script</span>></span><span class="javascript">
<span class="hljs-keyword">import</span> &#123; defineComponent,h &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'vue'</span>

<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> defineComponent(&#123;
  <span class="hljs-function"><span class="hljs-title">setup</span>(<span class="hljs-params">props,&#123;attrs, slots, emit&#125;</span>)</span> &#123;
    <span class="hljs-built_in">console</span>.log(attrs.msg) <span class="hljs-comment">// 打得你叫爸爸</span>
    <span class="hljs-built_in">console</span>.log(slots.default()) <span class="hljs-comment">// </span>
    <span class="hljs-keyword">return</span> <span class="hljs-function">()=></span> h(<span class="hljs-string">'div'</span>,&#123;&#125;,slots.default()) <span class="hljs-comment">// 输出自定义组件插槽的内容</span>
  &#125;,
&#125;)
</span><span class="hljs-tag"></<span class="hljs-name">script</span>></span></span>

<span class="copy-code-btn">复制代码</span></code></pre>
<p>输出自定义组件插槽内容：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/a851d3d590ef4167ac02442494bd21d3~tplv-k3u1fbpfcp-watermark.image" alt="1625043016074.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p><code>emit</code>使用：向父组件派发事件</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// 父组件</span>
<my-son  @change=<span class="hljs-string">"handelChange"</span>>
</my-son>
<span class="hljs-function"><span class="hljs-title">setup</span>(<span class="hljs-params"></span>)</span> &#123;
    <span class="hljs-keyword">const</span> handelChange =<span class="hljs-function">() =></span> &#123;
      <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'23456'</span>)
    &#125;
    <span class="hljs-keyword">return</span> &#123;
      handelChange,
    &#125;
  &#125;,
<span class="hljs-comment">// 子组件</span>
<span class="xml"><span class="hljs-tag"><<span class="hljs-name">template</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">div</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">button</span> @<span class="hljs-attr">click</span>=<span class="hljs-string">"handelClick"</span>></span> 子组件<span class="hljs-tag"></<span class="hljs-name">button</span>></span>
  <span class="hljs-tag"></<span class="hljs-name">div</span>></span>
<span class="hljs-tag"></<span class="hljs-name">template</span>></span></span>
<span class="xml"><span class="hljs-tag"><<span class="hljs-name">script</span>></span><span class="javascript">
<span class="hljs-keyword">import</span> &#123; defineComponent,h &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'vue'</span>

<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> defineComponent(&#123;
  <span class="hljs-function"><span class="hljs-title">setup</span>(<span class="hljs-params">props,&#123;attrs, slots, emit&#125;</span>)</span> &#123;
    <span class="hljs-keyword">const</span> handelClick =<span class="hljs-function">() =></span> &#123;
      emit(<span class="hljs-string">'change'</span>)
    &#125;
    <span class="hljs-keyword">return</span> &#123;
      handelClick
    &#125;
  &#125;,
&#125;)
</span><span class="hljs-tag"></<span class="hljs-name">script</span>></span></span>

<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/4e2245a2647b4e92a3b1978d216bf18f~tplv-k3u1fbpfcp-watermark.image" alt="1625043416118.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h6 data-id="heading-24">Teleport传送门</h6>
<p>可以选择挂载到指定的dom节点</p>
<p>语法：</p>
<pre><code class="hljs language-html copyable" lang="html">// to 指定的节点位置 如：.box  , #warp 对的
<span class="hljs-tag"><<span class="hljs-name">teleport</span> <span class="hljs-attr">to</span>=<span class="hljs-string">"body"</span>></span>
    // html
<span class="hljs-tag"></<span class="hljs-name">teleport</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>举个栗子：把一个阴影层覆盖整个<code>body</code></p>
<pre><code class="hljs language-js copyable" lang="js"><template>
  <span class="xml"><span class="hljs-tag"><<span class="hljs-name">div</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"box"</span>></span>
      <span class="hljs-tag"><<span class="hljs-name">button</span>  @<span class="hljs-attr">click</span>=<span class="hljs-string">'clickBtn'</span>></span>点击<span class="hljs-tag"></<span class="hljs-name">button</span>></span>
      // to 指定挂在的元素位置
      <span class="hljs-tag"><<span class="hljs-name">teleport</span> <span class="hljs-attr">to</span>=<span class="hljs-string">"body"</span>></span>
        <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">v-show</span>=<span class="hljs-string">"show"</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"mask"</span>></span>
        
        <span class="hljs-tag"></<span class="hljs-name">div</span>></span>
      <span class="hljs-tag"></<span class="hljs-name">teleport</span>></span>
    <span class="hljs-tag"></<span class="hljs-name">div</span>></span>
  <span class="hljs-tag"></<span class="hljs-name">div</span>></span></span>
</template>
<span class="xml"><span class="hljs-tag"><<span class="hljs-name">script</span>></span><span class="javascript">
<span class="hljs-keyword">import</span> &#123; defineComponent, ref &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'vue'</span>

<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> defineComponent(&#123;
  <span class="hljs-function"><span class="hljs-title">setup</span>(<span class="hljs-params"></span>)</span> &#123;
    <span class="hljs-keyword">const</span> show = ref(<span class="hljs-literal">false</span>)
    <span class="hljs-keyword">const</span> clickBtn =<span class="hljs-function">() =></span> &#123;
      show.value = !show.value
    &#125;
    <span class="hljs-keyword">return</span> &#123;
      clickBtn,
      show
    &#125;
  &#125;,
&#125;)
</span><span class="hljs-tag"></<span class="hljs-name">script</span>></span></span>

<span class="xml"><span class="hljs-tag"><<span class="hljs-name">style</span>></span><span class="css">
    <span class="hljs-selector-class">.box</span> &#123;
      <span class="hljs-attribute">position</span>: absolute;
      <span class="hljs-attribute">top</span>: <span class="hljs-number">50%</span>;
      <span class="hljs-attribute">left</span>: <span class="hljs-number">50%</span>;
      <span class="hljs-attribute">transform</span>: <span class="hljs-built_in">translate</span>(-<span class="hljs-number">50%</span>, -<span class="hljs-number">50%</span>);
      <span class="hljs-attribute">width</span>: <span class="hljs-number">300px</span>;
      <span class="hljs-attribute">height</span>: <span class="hljs-number">300px</span>;
      <span class="hljs-attribute">background-color</span>: aqua;
      <span class="hljs-attribute">z-index</span>: <span class="hljs-number">10</span>;
    &#125;

    <span class="hljs-selector-class">.mask</span> &#123;
      <span class="hljs-attribute">position</span>: absolute;
      <span class="hljs-attribute">top</span>: <span class="hljs-number">0</span>;
      <span class="hljs-attribute">left</span>: <span class="hljs-number">0</span>;
      <span class="hljs-attribute">right</span>: <span class="hljs-number">0</span>;
      <span class="hljs-attribute">bottom</span>: <span class="hljs-number">0</span>;
      <span class="hljs-attribute">background-color</span>: <span class="hljs-number">#000</span>;
      <span class="hljs-attribute">opacity</span>: .<span class="hljs-number">5</span>;
    &#125;
  </span><span class="hljs-tag"></<span class="hljs-name">style</span>></span></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>效果：</p>
<p>初始位置：</p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">v-show</span>=<span class="hljs-string">"show"</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"mask"</span>></span>

<span class="hljs-tag"></<span class="hljs-name">div</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/cbbf432b12bc4589bd0075ece72e2d44~tplv-k3u1fbpfcp-watermark.image" alt="1625037369006.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>使用<code>teleport</code>后，mask阴影层已挂在body下面了。</p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">teleport</span> <span class="hljs-attr">to</span>=<span class="hljs-string">"body"</span>></span>
<span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">v-show</span>=<span class="hljs-string">"show"</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"mask"</span>></span>

<span class="hljs-tag"></<span class="hljs-name">div</span>></span>
<span class="hljs-tag"></<span class="hljs-name">teleport</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/f54ac670cf9a4375b108057c5b8cbfc3~tplv-k3u1fbpfcp-watermark.image" alt="1625037369006.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/8ee577207b4a488d953c985dba7bc9a2~tplv-k3u1fbpfcp-watermark.image" alt="img" loading="lazy" referrerpolicy="no-referrer"></p></div>  
</div>
            