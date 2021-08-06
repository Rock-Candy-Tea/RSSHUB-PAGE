
---
title: '谈一谈Webpack 的SplitChunks'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/2e532dcfe618419e8295d4f86c66a42a~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Thu, 05 Aug 2021 02:17:38 GMT
thumbnail: 'https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/2e532dcfe618419e8295d4f86c66a42a~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>webpack官网中，有这么一句话，我不是很认同：</p>
<blockquote>
<p>开箱即用的 <code>SplitChunksPlugin</code> 对于大部分用户来说非常友好。</p>
</blockquote>
<p>可以说，性能优化最重要的部分就是懂得如何分包了。因此，就来谈谈webpack中的分包。</p>
<p>首先我们需要了解一个概念。</p>
<h2 data-id="heading-0">什么是chunks</h2>
<p>一个常考的面试题是 module、chunk、bundle是什么。对于初学者，这个是很迷惑的。我们首先要知道webpack一个简单的理解：</p>
<p>Webpack： 构建你的assets。左侧的资源通过webpack后，都能输出web浏览器能识别的资源！
归因于node构建了一个世界，让这个世界所有非js资源，都在js世界下的规则下处理：</p>
<p>css： 本质是style下的一个字符串，webpack处理css文本后，如果要直接作为style标签插入，再使用style-loader，如果要拿出来，则通过MiniCssExtractPlugin插件进行处理。
less： 本质最终要转化成css，因此通过less-loader，转化为css，再重复上面的操作。
typescript： 浏览器是没法直接识别的，通过ts-loader。来转化为浏览器能识别的js。</p>
<p>以上这些，都是为了做一件事：</p>
<p>以上图webpack为划分点，我们就可以区分module和bundle。即：左边是资源就是moudle，右边的资源就是bundle。</p>
<p>一个ts文件、图片、less、pug等都是一个module，而打包后的产物，总的称呼就是bundle。</p>
<p>那么chunk是什么呢？</p>
<p>对于打包产物bundle， 有些情况下，我们觉得太大了。 为了优化性能，比如快速打开首屏，利用缓存等，我们需要对bundle进行以下拆分，对于拆分出来的东西，我们叫它chunk。</p>
<p>我们试着打包一下！</p>
<h2 data-id="heading-1">默认配置</h2>
<p>现在我们创建src/index.js 和 src/a.js</p>













<table><thead><tr><th>index.js</th><th>a.js</th></tr></thead><tbody><tr><td><code>import lodash from "lodash";,import &#123; a &#125; from "./a";,console.log(lodash, a);</code></td><td><code>export const a = "i am aaaaaa";,console.log(a);,</code></td></tr></tbody></table>
<p>目录结构：</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/2e532dcfe618419e8295d4f86c66a42a~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>webpack.config.js 配置和打包结果为：</p>













<table><thead><tr><th>webpack.config.js</th><th></th></tr></thead><tbody><tr><td><code>&#123;,  mode: "production",,  entry: &#123;,    main: "./src/index.js",,  &#125;,,  output: &#123;,    path: path.resolve(__dirname, "dist"),,    filename: "[name].js", ,    clean: true,,  &#125;,,&#125;</code></td><td><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/4f7c5fb4788a4d02817563071ef6f1cb~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer">｜</td></tr></tbody></table>
<p>默认的，webpack没有进行分包，全部都打在一起了。</p>
<h2 data-id="heading-2">一些配置字段</h2>
<p>Webpack 的分包主要在optimization.splitChunks属性，现在我们来尝试使用不同的配置字段来看看效果。</p>
<h3 data-id="heading-3"></h3>
<h3 data-id="heading-4">optimization.splitChunks.chunks</h3>
<h3 data-id="heading-5"></h3>
<p>Chunks 有三个提供的值，分别是 async、initial、all</p>
<h4 data-id="heading-6">async</h4>
<p>此值是默认的chunks值，也就是说，我们的第一次打包实际上就是实行了async，该值的意思是：对于动态加载的模块，默认配置会将该模块单独打包。使用以下语法进行动态加载（还有其他写法）：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">import</span>(<span class="hljs-string">'lodash'</span>)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>修改index.js，然后运行build命令，为了文件更直观，我们将optimization.chunkIds的值设置为named</p>













<table><thead><tr><th>index.js</th><th></th></tr></thead><tbody><tr><td><code>import &#123; a &#125; from "./a";,import('lodash').then(lodash => &#123;,    const res = lodash.default.add(3,4),    console.log(a, res);,&#125;)</code></td><td><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/8e8e2f0615964338a5cf0ff25fff2af8~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></td></tr></tbody></table>
<p>可以看到lodash被分出一个单独的包了。</p>
<p>以下是webpack对于默认配置的说法：</p>
<blockquote>
<p>webpack 将根据以下条件自动拆分 chunks：
新的 chunk 可以被共享，或者模块来自于 <code>node_modules</code> 文件夹
新的 chunk 体积大于 20kb（在进行 min+gz 之前的体积）
当按需加载 chunks 时，并行请求的最大数量小于或等于 30
当加载初始化页面时，并发请求的最大数量小于或等于 30
当尝试满足最后两个条件时，最好使用较大的 chunks。</p>
</blockquote>
<p>进行实验后，发现并不准确，比如两个入口引入lodash，lodash并未被抽出来</p>













<table><thead><tr><th>index.js</th><th>other.js</th></tr></thead><tbody><tr><td><code>import lodash from "lodash";,import &#123; a &#125; from "./a";,console.log(lodash, a);</code></td><td><code>import lodash from "lodash";,,console.log("lodash", lodash);</code></td></tr></tbody></table>
<p>配置与打包</p>





















<table><thead><tr><th>配置</th><th>打包</th></tr></thead><tbody><tr><td><code>&#123;,  entry: &#123;,    main: "./src/index.js",,    other: "./src/other.js",,  &#125;,,  optimization: &#123;,    chunkIds: "named",,  &#125;,,&#125;</code></td><td><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/7ca559eeae5d43c0a546bd6d978bdb64~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer">｜</td></tr><tr><td>默认配置只会抽出动态加载的模块，通常情况下，不是立即需要的包，可以考虑动态加载，比如导出excel的包，echarts，monaco-editor等。</td><td></td></tr><tr><td>#### initial</td><td></td></tr></tbody></table>
<p>当chunk为initial或者为alll时，webpack打包遵循以下配置（取名default）：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-built_in">module</span>.exports = &#123;
  <span class="hljs-comment">//...</span>
  <span class="hljs-attr">optimization</span>: &#123;
    <span class="hljs-attr">splitChunks</span>: &#123;
      <span class="hljs-attr">chunks</span>: <span class="hljs-string">'initial'</span>,
      <span class="hljs-attr">minSize</span>: <span class="hljs-number">20000</span>,
      <span class="hljs-attr">minRemainingSize</span>: <span class="hljs-number">0</span>,
      <span class="hljs-attr">minChunks</span>: <span class="hljs-number">1</span>,
      <span class="hljs-attr">maxAsyncRequests</span>: <span class="hljs-number">30</span>,
      <span class="hljs-attr">maxInitialRequests</span>: <span class="hljs-number">30</span>,
      <span class="hljs-attr">enforceSizeThreshold</span>: <span class="hljs-number">50000</span>,
      <span class="hljs-attr">cacheGroups</span>: &#123;
        <span class="hljs-attr">defaultVendors</span>: &#123;
          <span class="hljs-attr">test</span>: <span class="hljs-regexp">/[\\/]node_modules[\\/]/</span>,
          priority: -<span class="hljs-number">10</span>,
          <span class="hljs-attr">reuseExistingChunk</span>: <span class="hljs-literal">true</span>,
        &#125;,
        <span class="hljs-attr">default</span>: &#123;
          <span class="hljs-attr">minChunks</span>: <span class="hljs-number">2</span>,
          <span class="hljs-attr">priority</span>: -<span class="hljs-number">20</span>,
          <span class="hljs-attr">reuseExistingChunk</span>: <span class="hljs-literal">true</span>,
        &#125;,
      &#125;,
    &#125;,
  &#125;,
&#125;;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>尽管你的配置可能是这样：</p>







<table><thead><tr><th><code>&#123;,  entry: &#123;,    main: "./src/index.js",,    other: "./src/other.js",,  &#125;,,  optimization: &#123;,    chunkIds: "named",,    splitChunks: &#123;,      chunks: "initial",,    &#125;,,  &#125;,,&#125;</code></th><th><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/3da3f1ac36ad4250b9a3a197ae35de15~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></th></tr></thead></table>
<p>只有当chunks 不为async时，webpack打包的默认配置才会是default配置</p>
<blockquote>
<p>新的 chunk 可以被共享，或者模块来自于 <code>node_modules</code> 文件夹
新的 chunk 体积大于 20kb（在进行 min+gz 之前的体积）
当按需加载 chunks 时，并行请求的最大数量小于或等于 30
当加载初始化页面时，并发请求的最大数量小于或等于 30</p>
</blockquote>
<h4 data-id="heading-7">all</h4>
<p>当chunks值为all时，基本跟initial值相同，我们来实验一下它的不同点；</p>
<p>我们将在other.js对lodash动态引用：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">import</span>(<span class="hljs-string">'lodash'</span>).then(<span class="hljs-function"><span class="hljs-params">lodash</span> =></span> &#123;
    <span class="hljs-keyword">const</span> res = lodash.default.add(<span class="hljs-number">3</span>,<span class="hljs-number">4</span>)
    <span class="hljs-built_in">console</span>.log(res);
&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>然后分别使用chunks为all 和initial的值，看看效果：</p>













<table><thead><tr><th>all</th><th>initial</th></tr></thead><tbody><tr><td><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/a4c59a84a50c432ba740b0720eaff136~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></td><td><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/5cd89b8ce5b34d14a2d2cdc45297fbc9~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></td></tr></tbody></table>
<p>可以看到，对于两个入口文件引用lodash， 如果一个是正常引入，一个是动态引入，initial会打包成两份，而all的话，只会有一份，因此，通常情况下，all的优于initial的。</p>
<h3 data-id="heading-8">optimization.splitChunks的其他默认配置</h3>
<pre><code class="hljs language-yaml copyable" lang="yaml">&#123;
      <span class="hljs-attr">minSize:</span> <span class="hljs-number">20000</span>,
      <span class="hljs-attr">minRemainingSize:</span> <span class="hljs-number">0</span>,
      <span class="hljs-attr">minChunks:</span> <span class="hljs-number">1</span>,
      <span class="hljs-attr">maxAsyncRequests:</span> <span class="hljs-number">30</span>,
      <span class="hljs-attr">maxInitialRequests:</span> <span class="hljs-number">30</span>,
      <span class="hljs-attr">enforceSizeThreshold:</span> <span class="hljs-number">50000</span>,
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>minSize：此配置是指，将要被分包的chunks，如果压缩前体积不足20k，将不会被拆包。
minChunks：某个chunks被多次引用，如果这个引用次数小于某个值，将不会被拆包。
...
以上条件满足一个将会被分包。
enforceSizeThreshold：如果某个chunks的大小超过了50k，以上限制将不会生效。</p>
<h3 data-id="heading-9">optimization.splitChunks. cacheGroups</h3>
<p>cacheGroups有两个默认缓存策略，也就是chunks为all和initail时的默认配置：</p>
<pre><code class="hljs language-yaml copyable" lang="yaml"><span class="hljs-attr">cacheGroups:</span> &#123;
        <span class="hljs-attr">defaultVendors:</span> &#123;
          <span class="hljs-attr">test:</span> <span class="hljs-string">/</span>[<span class="hljs-string">\\/</span>]<span class="hljs-string">node_modules</span>[<span class="hljs-string">\\/</span>]<span class="hljs-string">/</span>,
          <span class="hljs-attr">priority:</span> <span class="hljs-number">-10</span>,
          <span class="hljs-attr">reuseExistingChunk:</span> <span class="hljs-literal">true</span>,
        &#125;,
        <span class="hljs-attr">default:</span> &#123;
          <span class="hljs-attr">minChunks:</span> <span class="hljs-number">2</span>,
          <span class="hljs-attr">priority:</span> <span class="hljs-number">-20</span>,
          <span class="hljs-attr">reuseExistingChunk:</span> <span class="hljs-literal">true</span>,
        &#125;,
 &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>defaultVendors 会将源代码中所有引入node_modules的文件打包成为一个大的chunks。
default 则是对于多入口引入的相同模块超过两次后，进行拆包操作，需要注意的是，我们通常操作的单页面应用，默认只有一个入口文件，如果有如下代码：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">// index.js</span>
<span class="hljs-keyword">import</span> lodash <span class="hljs-keyword">from</span> <span class="hljs-string">"lodash"</span>;
<span class="hljs-keyword">import</span> &#123; a &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">"./a"</span>;
<span class="hljs-keyword">import</span> &#123; b &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">"./b"</span>;
<span class="hljs-built_in">console</span>.log(lodash, a, b);

<span class="hljs-comment">// a.js</span>
<span class="hljs-keyword">export</span> <span class="hljs-keyword">const</span> a = <span class="hljs-string">"i am aaaaaa"</span>;
<span class="hljs-built_in">console</span>.log(a);
<span class="hljs-keyword">import</span> <span class="hljs-string">"./c"</span>;

<span class="hljs-comment">// b.js</span>
<span class="hljs-keyword">export</span> <span class="hljs-keyword">const</span> b = <span class="hljs-string">"i am bbbbbbbbb"</span>;
<span class="hljs-built_in">console</span>.log(b);
<span class="hljs-keyword">import</span> <span class="hljs-string">"./c"</span>;

<span class="hljs-comment">// c.js</span>
<span class="hljs-built_in">console</span>.log(<span class="hljs-string">"ccccccccc"</span>);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>a.js 和 b.js 共同引用了c.js。此时a、b、c都从属于index.js入口，虽然c.js被引用了两次，但c.js并不会分成单独的包，如果要将c.js单独打包，考虑动态加载。</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/c558d4d570754e51bf631b8d8dd110be~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>通常，我们只需要默认的配置即可满足大部分需求，有的时候我们可能想单独抽出react相关代码，那么这需要以下配置。</p>
<pre><code class="hljs language-css copyable" lang="css">react: &#123;
  name: <span class="hljs-string">"ReactAbout"</span>,
  test: /react/,
  priority: <span class="hljs-number">1</span>,
&#125;,
<span class="copy-code-btn">复制代码</span></code></pre>
<p>打包效果</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/566403250ba848b6986085e6843a587b~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<pre><code class="hljs language-haskell copyable" lang="haskell">// other.js

<span class="hljs-keyword">import</span>('<span class="hljs-title">lodash'</span>).then(<span class="hljs-title">lodash</span> => &#123;
    <span class="hljs-title">const</span> <span class="hljs-title">res</span> = <span class="hljs-title">lodash</span>.<span class="hljs-title">default</span>.<span class="hljs-title">add</span>(3,4)
    console.log(res);
&#125;)

<span class="hljs-keyword">import</span>('./<span class="hljs-title">style</span>/<span class="hljs-title">a</span>.<span class="hljs-title">css'</span>)
<span class="hljs-keyword">import</span>('./<span class="hljs-title">style</span>/<span class="hljs-title">b</span>.<span class="hljs-title">css'</span>)
<span class="hljs-keyword">import</span>('./<span class="hljs-title">style</span>/<span class="hljs-title">c</span>.<span class="hljs-title">css'</span>)
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="hljs language-css copyable" lang="css">&#123;
    test: /\.css$/,
    use: [<span class="hljs-string">"style-loader"</span>, <span class="hljs-string">"css-loader"</span>],
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-10">css</h4>
<p>css也是性能优化的一部分，有一种方式是通过style- loader将css以style标签的形式插入到文档，这种方式正常引用无法进行分包。但可以通过动态引入的方式分包。</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/338a9e27727f419c922256469562dc1b~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>另外有一个MiniCssExtractPlugin插件进行css的分包。此插件默认为每个入口单独抽出css，也可以进行cacheGroups的配置，满足条件时，会将多个入口的css打包在一起。</p>
<pre><code class="hljs language-yaml copyable" lang="yaml"><span class="hljs-attr">css:</span> &#123;
  <span class="hljs-attr">name:</span> <span class="hljs-string">"css"</span>,
  <span class="hljs-attr">test:</span> <span class="hljs-string">/\.css$/</span>,
  <span class="hljs-attr">minChunks:</span> <span class="hljs-number">1</span>,
  <span class="hljs-attr">enforce:</span> <span class="hljs-literal">true</span>,
&#125;
<span class="copy-code-btn">复制代码</span></code></pre></div>  
</div>
            