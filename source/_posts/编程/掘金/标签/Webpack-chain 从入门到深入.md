
---
title: 'Webpack-chain 从入门到深入'
categories: 
 - 编程
 - 掘金
 - 标签
headimg: 'https://picsum.photos/400/300?random=8436'
author: 掘金
comments: false
date: Mon, 05 Apr 2021 17:35:25 GMT
thumbnail: 'https://picsum.photos/400/300?random=8436'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h2 data-id="heading-0">一、前言</h2>
<p>webpack 的核心配置的创建和修改基于一个有潜在难于处理的 JavaScript 对象。虽然这对于配置单个项目来说是没有什么问题的，但当你团队中有比较多项目，并且尝试所有项目共享 webpack 配置文件时，你会觉难以入手，因为你需要考虑构建配置的可扩展性，比如某个子项目有自己独有的特征，需要进行一些个性化配置时，便会变得棘手。</p>
<p>webpack-chain 尝试通过提供可链式或顺流式的 API 创建和修改webpack 配置，API 的 Key 部分可以由用户指定的名称引用，这有助于跨项目修改配置方式的标准化。在 vue-cli3 以及一些开源的构建器中陆续采用了 webpack-chain 这种方式，所以本文我们会从入门到熟练上手，帮助大家熟悉 webpack-chain 的编写使用。</p>
<h2 data-id="heading-1">二、语法介绍</h2>
<h3 data-id="heading-2">1、webpack 实例创建</h3>
<p>我们可以使用 npm 或者 yarn 的方式安装 webpack-chain 包，如下所示</p>
<pre><code class="hljs language-javascript copyable" lang="javascript">npm i --save-dev webpack-chain
or
yarn add --dev webpack-chain
<span class="copy-code-btn">复制代码</span></code></pre>
<p>当你安装了webpack-chain， 你就可以开始创建一个 webpack 实例，如下所示</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">// 导入 webpack-chain 模块，该模块导出了一个用于创建一个 webpack 配置 API 的单一构造函数。</span>
<span class="hljs-keyword">const</span> Config = <span class="hljs-built_in">require</span>(<span class="hljs-string">'webpack-chain'</span>);

<span class="hljs-comment">// 对该单一构造函数创建一个新的配置实例</span>
<span class="hljs-keyword">const</span> config = <span class="hljs-keyword">new</span> Config();

<span class="hljs-comment">// ... 中间一系列 webpack 的配置，我们在后续的章节再陆续说明，这里暂且省略</span>

<span class="hljs-comment">// 导出这个修改完成的要被 webpack 使用的配置对象</span>
<span class="hljs-built_in">module</span>.exports = config.toConfig();
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-3">2、ChainedMap</h3>
<p>webpack-chain 中的核心 API 接口之一是 ChainedMap. 一个 ChainedMap 的操作类似于 JavaScript Map, 为链式和生成配置提供了一些便利， 如果一个属性被标记一个 ChainedMap, 则它将具有如下的 API 和方法:
<strong>除非另有说明，否则这些方法将返回 ChainedMap, 允许链式调用这些方法。</strong></p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">// 1、从 Map 移除所有 配置</span>
clear()

<span class="hljs-comment">// 2、通过键值从 Map 移除单个配置</span>
<span class="hljs-keyword">delete</span>(key)

<span class="hljs-comment">// 3、获取 Map 中相应键的值</span>
<span class="hljs-comment">// 注意：返回值是该 key 对应的值</span>
get(key)

<span class="hljs-comment">// 4、获取 Map 中相应键的值</span>
<span class="hljs-comment">// 如果键在 Map 中不存在，则 ChainedMap 中该键的值会被配置为 fn 的返回值.</span>
<span class="hljs-comment">// 注意：返回值是该 key 对应的值，或者 fn 返回的值</span>
getOrCompute(key, fn)

<span class="hljs-comment">// 5、配置 Map 中 已存在的键的值</span>
set(key, value)

<span class="hljs-comment">// 6、Map 中是否存在一个配置值的特定键，</span>
<span class="hljs-comment">// 注意：返回 boolean</span>
has(key)

<span class="hljs-comment">// 7、返回 Map 中已存储的所有值的数组</span>
<span class="hljs-comment">// 注意：返回 Array</span>
values()

<span class="hljs-comment">// 8、返回 Map 中全部配置的一个对象, 其中 键是这个对象属性，值是相应键的值，</span>
entries()

<span class="hljs-comment">// 9、 提供一个对象，这个对象的属性和值将 映射进 Map</span>
merge(obj, omit)

<span class="hljs-comment">// 10、对当前配置上下文执行函数 handler</span>
batch(handler)

<span class="hljs-comment">// 11、条件执行一个函数去继续配置</span>
<span class="hljs-comment">// condition: Boolean</span>
<span class="hljs-comment">// whenTruthy: 当条件为真，调用把 ChainedMap 实例作为单一参数传入的函数</span>
<span class="hljs-comment">// whenFalsy: 当条件为假，调用把 ChainedMap 实例作为单一参数传入的函数</span>
when(condition, whenTruthy, whenFalsy)

<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-4">3、ChainedSet</h3>
<p>webpack-chain 中的核心 API 接口另一个是 ChainedSet，其操作类似于JavaScript Set, 为链式和生成配置提供了一些便利。 如果一个属性被标记一个 ChainedSet，则它将具有如下的 API 和方法：
<strong>除非另有说明，否则这些方法将返回 ChainedSet，允许链式调用这些方法。</strong></p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">// 1、添加/追加给 Set 末尾位置一个值</span>
add(value)

<span class="hljs-comment">// 2、添加给 Set 开始位置一个值</span>
prepend(value)

<span class="hljs-comment">// 3、移除Set中全部值</span>
clear()

<span class="hljs-comment">// 4、移除Set中一个指定的值</span>
<span class="hljs-keyword">delete</span>(value)

<span class="hljs-comment">// 5、检测 Set 中是否存在一个值</span>
<span class="hljs-comment">// 注意：返回 boolean</span>
has(value)

<span class="hljs-comment">// 6、返回 Set 中值的数组.</span>
<span class="hljs-comment">// 注意：返回 Array</span>
values()

<span class="hljs-comment">// 7、连接给定的数组到 Set 尾部。</span>
merge(arr)

<span class="hljs-comment">// 8、对当前配置上下文执行函数 handler</span>
batch(handler)

<span class="hljs-comment">// 8、条件执行一个函数去继续配置</span>
<span class="hljs-comment">// whenTruthy: 当条件为真，调用把 ChainedSet 实例作为单一参数传入的函数</span>
<span class="hljs-comment">// whenFalsy: 当条件为假，调用把 ChainedSet 实例作为单一参数传入的函数</span>
when(condition, whenTruthy, whenFalsy)
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-5">4、方法简写</h3>
<p>除了以上提到的使用 ChainedMap 和 ChainedSet 语法编写实现功能外，webpack-chain 还提供了许多简写方法，我们在这里不在一一列出，读者可以去 <a href="https://github.com/neutrinojs/webpack-chain" target="_blank" rel="nofollow noopener noreferrer">webpack-chain github 官方文档</a> 查阅。例如，devServer.hot 就是是一个简写方法，写法如下所示</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">// devServer 的简写方法如下</span>
devServer.hot(<span class="hljs-literal">true</span>);

<span class="hljs-comment">// 上述方法等效于</span>
devServer.set(<span class="hljs-string">'hot'</span>, <span class="hljs-literal">true</span>);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>跟 ChainedMap 和 ChainedSet 语法一样，简写方法在没有特别说明的情况，返回的也是原实例，因此简写方法也是支持链式语法的。</p>
<h3 data-id="heading-6">5、合并配置</h3>
<p>webpack-chain 支持将对象合并到配置实例，但是要注意，这不是 webpack 配置对象，如果我们需要合并 webpack-chain 对象，需要在合并前对其进行转换。</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">// 合并</span>
config.merge(&#123; <span class="hljs-attr">devtool</span>: <span class="hljs-string">'source-map'</span> &#125;);
<span class="hljs-comment">// 获取 "source-map"</span>
config.get(<span class="hljs-string">'devtool'</span>)
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-7">6、检查生成的配置</h3>
<p>我们可以使用语法 config.toString() 方法将 webpack 对象转换成字符串，转换后的字符串包含命名规则、用法和插件的注释提示，如下所示</p>
<pre><code class="hljs language-javascript copyable" lang="javascript">config
  .module
    .rule(<span class="hljs-string">'compile'</span>)
      .test(<span class="hljs-regexp">/\.js$/</span>)
      .use(<span class="hljs-string">'babel'</span>)
        .loader(<span class="hljs-string">'babel-loader'</span>);

config.toString();

<span class="hljs-comment">// 转换后的输出</span>
&#123;
  <span class="hljs-attr">module</span>: &#123;
    <span class="hljs-attr">rules</span>: [
      <span class="hljs-comment">/* config.module.rule('compile') */</span>
      &#123;
        <span class="hljs-attr">test</span>: <span class="hljs-regexp">/\.js$/</span>,
        use: [
          <span class="hljs-comment">/* config.module.rule('compile').use('babel') */</span>
          &#123;
            <span class="hljs-attr">loader</span>: <span class="hljs-string">'babel-loader'</span>
          &#125;
        ]
      &#125;
    ]
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-8">三、常用实例编写</h2>
<h3 data-id="heading-9">1、entry 入口配置</h3>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">// 配置编译入口文件</span>
config.entry(<span class="hljs-string">'main'</span>).add(<span class="hljs-string">'./src/main.js'</span>) 

<span class="hljs-comment">// 等同于以下 webpack 配置</span>
<span class="hljs-attr">entry</span>: &#123;
  <span class="hljs-attr">main</span>: [
    <span class="hljs-string">'./src/main.js'</span>
  ]
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-10">2、output 出口配置</h3>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">// 配置出口文件</span>
config.output
  .path(path.resolve(__dirname, <span class="hljs-string">'./dist'</span>))
  .filename(<span class="hljs-string">'[name].[chunkhash].js'</span>)
  .chunkFilename(<span class="hljs-string">'chunks/[name].[chunkhash].js'</span>)
  .libraryTarget(<span class="hljs-string">'umd'</span>);

<span class="hljs-comment">// 等同于以下 webpack 配置</span>
output: &#123;
  <span class="hljs-attr">path</span>: path.resolve(__dirname, <span class="hljs-string">'./dist'</span>),
  <span class="hljs-attr">filename</span>: <span class="hljs-string">'[name].[chunkhash].js'</span>,
  <span class="hljs-attr">chunkFilename</span>: <span class="hljs-string">'chunks/[name].[chunkhash].js'</span>,
  <span class="hljs-attr">libraryTarget</span>: <span class="hljs-string">'umd'</span>
&#125;,
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-11">3、alias 别名配置</h3>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">// 配置目录别名</span>
config.resolve.alias
  .set(<span class="hljs-string">'@'</span>, path.resolve(__dirname, <span class="hljs-string">'src'</span>))
  .set(<span class="hljs-string">'assets'</span>, path.resolve(__dirname, <span class="hljs-string">'src/assets'</span>))

<span class="hljs-comment">// 等同于以下 webpack 配置</span>
<span class="hljs-attr">resolve</span>: &#123;
  <span class="hljs-attr">alias</span>: &#123;
    <span class="hljs-string">'@'</span>: path.resolve(__dirname, <span class="hljs-string">'src'</span>),
     <span class="hljs-attr">assets</span>: path.resolve(__dirname, <span class="hljs-string">'src/assets'</span>)）
  &#125;
&#125;,
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-12">4、loader 配置新增</h3>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">// 配置一个新的 loader</span>
config.module
.rule(<span class="hljs-string">'babel'</span>)
.test(<span class="hljs-regexp">/\.(js|jsx|mjs|ts|tsx)$/</span>)
.include
  .add(path.resolve(__dirname,  <span class="hljs-string">'src'</span>))
  .end()
.use(<span class="hljs-string">'babel-loader'</span>)
  .loader(<span class="hljs-string">'babel-loader'</span>)
  .options(&#123;
    <span class="hljs-string">'presets'</span>:[<span class="hljs-string">'@babel/preset-env'</span>]
  &#125;)

<span class="hljs-comment">// 等同于以下 webpack 配置</span>
<span class="hljs-attr">module</span>: &#123;
  <span class="hljs-attr">rules</span>: [
    &#123;
      <span class="hljs-attr">test</span>: <span class="hljs-regexp">/\.(js|jsx|mjs|ts|tsx)$/</span>,
      include: [
        path.resolve(__dirname,  <span class="hljs-string">'src'</span>)
      ],
      <span class="hljs-attr">use</span>: [
        &#123;
          <span class="hljs-attr">loader</span>: <span class="hljs-string">'babel-loader'</span>,
          <span class="hljs-attr">options</span>: &#123;
              <span class="hljs-attr">presets</span>: [
                <span class="hljs-string">'@babel/preset-env'</span>
              ]
            &#125;
        &#125;
      ]
    &#125;
  ]
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-13">5、loader 配置修改</h3>
<p>跟新增 loader 不同的是，使用了 tap 方法，该方法的回调参数为 options 即该 loader 的配置选项对象，从而我们可以通过更改 options 对象，从而去更改 loader 配置。</p>
<pre><code class="hljs language-javascript copyable" lang="javascript">config.module
.rule(<span class="hljs-string">'babel'</span>)
.use(<span class="hljs-string">'babel-loader'</span>)
  .tap(<span class="hljs-function"><span class="hljs-params">options</span> =></span> &#123;
    <span class="hljs-comment">// 修改它的选项...</span>
    options.include = path.resolve(__dirname,  <span class="hljs-string">'test'</span>)
    <span class="hljs-keyword">return</span> options
  &#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-14">6、loader 配置移除</h3>
<pre><code class="hljs language-javascript copyable" lang="javascript">config.module.rules.clear(); <span class="hljs-comment">// 添加的 loader 都删掉.</span>

config.module.rule(<span class="hljs-string">'babel'</span>).uses.clear();  删除指定 rule 用 use 添加的
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-15">7、plugin 配置新增</h3>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">// 配置一个新的 plugin</span>
config.plugin(<span class="hljs-string">'HtmlWebpackPlugin'</span>).use(HtmlWebpackPlugin, [
  &#123;
    <span class="hljs-attr">template</span>: path.resolve(__dirname, <span class="hljs-string">'./src/index.html'</span>),
    <span class="hljs-attr">minify</span>: &#123;
      <span class="hljs-attr">collapseWhitespace</span>: <span class="hljs-literal">true</span>,
      <span class="hljs-attr">minifyJS</span>: <span class="hljs-literal">true</span>,
      <span class="hljs-attr">minifyCSS</span>: <span class="hljs-literal">true</span>,
      <span class="hljs-attr">removeComments</span>: <span class="hljs-literal">true</span>,
      <span class="hljs-attr">removeEmptyAttributes</span>: <span class="hljs-literal">true</span>,
      <span class="hljs-attr">removeRedundantAttributes</span>: <span class="hljs-literal">true</span>,
      <span class="hljs-attr">useShortDoctype</span>: <span class="hljs-literal">true</span>
    &#125; 
  &#125;
]);

<span class="hljs-comment">// 等同于以下 webpack 配置</span>
  plugins: [
    <span class="hljs-keyword">new</span> HtmlWebpackPlugin(
      &#123;
        <span class="hljs-attr">template</span>: path.resolve(__dirname, <span class="hljs-string">'./src/index.html'</span>),
        <span class="hljs-attr">minify</span>: &#123;
          <span class="hljs-attr">collapseWhitespace</span>: <span class="hljs-literal">true</span>,
          <span class="hljs-attr">minifyJS</span>: <span class="hljs-literal">true</span>,
          <span class="hljs-attr">minifyCSS</span>: <span class="hljs-literal">true</span>,
          <span class="hljs-attr">removeComments</span>: <span class="hljs-literal">true</span>,
          <span class="hljs-attr">removeEmptyAttributes</span>: <span class="hljs-literal">true</span>,
          <span class="hljs-attr">removeRedundantAttributes</span>: <span class="hljs-literal">true</span>,
          <span class="hljs-attr">useShortDoctype</span>: <span class="hljs-literal">true</span>
        &#125;
      &#125;
    )
  ],
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-16">8、plugin 配置修改</h3>
<p>跟新增 loader/plugin 不同的是，使用了 tap 方法，且保留了之前配置的选项，更改的选项被覆盖。</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">// 修改插件 HtmlWebpackPlugin</span>
config.plugin(<span class="hljs-string">'HtmlWebpackPlugin'</span>).tap(<span class="hljs-function">(<span class="hljs-params">args</span>) =></span> [
  &#123;
    ...(args[<span class="hljs-number">0</span>] || &#123;&#125;),
    <span class="hljs-attr">template</span>: path.resolve(__dirname, <span class="hljs-string">'./main.html'</span>),
  &#125;
]);
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-17">9、使用 when 条件进行配置</h3>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">// 1、示例：仅在生产期间添加minify插件</span>
config
  .when(process.env.NODE_ENV === <span class="hljs-string">'production'</span>, <span class="hljs-function"><span class="hljs-params">config</span> =></span> &#123;
    config
      .plugin(<span class="hljs-string">'minify'</span>)
      .use(BabiliWebpackPlugin);
  &#125;);

<span class="hljs-comment">// 2、示例：只有在生产过程中添加缩小插件，否则设置 devtool 到源映射</span>
config
  .when(process.env.NODE_ENV === <span class="hljs-string">'production'</span>,
    <span class="hljs-function"><span class="hljs-params">config</span> =></span> config.plugin(<span class="hljs-string">'minify'</span>).use(BabiliWebpackPlugin),
    <span class="hljs-function"><span class="hljs-params">config</span> =></span> config.devtool(<span class="hljs-string">'source-map'</span>)
  );
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-18">10、插件移除配置</h3>
<pre><code class="hljs language-javascript copyable" lang="javascript">config.plugins.delete(<span class="hljs-string">'HtmlWebpackPlugin'</span>);
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-19">四、总结</h2>
<p>本文我们会从入门到熟练上手，通过介绍 webpack-chain 的语法到手动编写 webpack 的常见配置和操作，帮助大家熟悉 webpack-chain 的编写使用，希望对你有帮助。</p>
<p>辛苦整理良久，还望手动点赞鼓励~ 博客 github地址为：<a href="https://github.com/fengshi123/blog" target="_blank" rel="nofollow noopener noreferrer">github.com/fengshi123/…</a> ，汇总了作者的所有博客，欢迎关注及 star ~</p></div> <div class="image-viewer-box" data-v-78c9b824><!----></div>  
</div>
            