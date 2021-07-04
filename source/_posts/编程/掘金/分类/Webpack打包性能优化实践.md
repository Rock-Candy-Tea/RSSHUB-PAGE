
---
title: 'Webpack打包性能优化实践'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/d99cb4e9088d41588ad3cedfb1cfb4c5~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Fri, 02 Jul 2021 06:01:39 GMT
thumbnail: 'https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/d99cb4e9088d41588ad3cedfb1cfb4c5~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h2 data-id="heading-0">前言</h2>
<p>我觉得webpack的配置对于很多前端来说就是一个黑洞，首先是配置极多，其次项目大起来之后优化起来总是无从下手，后来自己通过看了众多的打包性能优化的配置之后总结下来其实就这么几点<code>预编译,做缓存,多线程,少检索</code>。</p>
<p>在聊到性能优化前，我们先得知道怎么去分析我们打包性能。</p>
<h2 data-id="heading-1">性能分析工具</h2>
<p>性能分析主要分为<code>打包大小分析</code>和<code>打包时间分析</code>。</p>
<h3 data-id="heading-2">打包大小分析</h3>
<p>打包的大小分析的插件是<code>webpack-bundle-analyzer</code>,这个插件可以将我们打包的各模块的大小可视化的展示出来了。</p>
<p>首先我们在package.json中写一个命令：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// package.json</span>
<span class="hljs-string">"scripts"</span>: &#123;
    <span class="hljs-string">"analyzer"</span>: <span class="hljs-string">"npm run build && webpack-bundle-analyzer --port 8888 ./dist/analyzer.json"</span>
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>webpack.prod.js代码：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// webpack.prod.js</span>
<span class="hljs-keyword">const</span> BundleAnalyzerPlugin = <span class="hljs-built_in">require</span>(<span class="hljs-string">'webpack-bundle-analyzer'</span>).BundleAnalyzerPlugin;
...

<span class="hljs-attr">plugins</span>:&#123;
    ...
    <span class="hljs-keyword">new</span> BundleAnalyzerPlugin(&#123;
      <span class="hljs-attr">analyzerMode</span>: <span class="hljs-string">'disabled'</span>,
      <span class="hljs-attr">generateStatsFile</span>: process.env.Analyzer === <span class="hljs-string">'on'</span>,
      <span class="hljs-attr">statsFilename</span>: path.join(__dirname, <span class="hljs-string">'../'</span>, <span class="hljs-string">'dist/analyzer.json'</span>)
    &#125;)
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>效果如图所示：</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/d99cb4e9088d41588ad3cedfb1cfb4c5~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer">
当然我们得到了我们项目模块的大小详情之后，我们可以优化打出来比较大的模块，比如lodash，我们并不需要把所有的方法都打进来的，可以通过只提取使用到的方法即可。</p>
<h3 data-id="heading-3">打包时间分析</h3>
<p>当然webpack打包我们除了要知道所有的打包出来的模块大小，还需要分析每个打包环节所花的时间，从而优化不同环节的耗时操作，对此我们要下载<code>speed-measure-webpack-plugin</code>插件。</p>
<p>其实配置很简单，只需要在我们的webpack配置包一层即可。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> SpeedMeasurePlugin = <span class="hljs-built_in">require</span>(<span class="hljs-string">"speed-measure-webpack-plugin"</span>);

<span class="hljs-keyword">const</span> smp = <span class="hljs-keyword">new</span> SpeedMeasurePlugin();

<span class="hljs-built_in">module</span>.exports = smp.wrap(webpackConfig) <span class="hljs-comment">// webpackConfig指打包配置</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>各个环节所消耗的时间如下：</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/50a0266640bf44c1b43fb426fd5a6294~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-4">多线程</h2>
<h3 data-id="heading-5">HappyPack</h3>
<p>由于构建需要对大量文件进行解析和处理，所以构建是文件读写和计算密集型操作。当文件增多的时候，webpack构建速度会越来越慢，因为webpack是运行在Node.js的单线程模型，所以webpack在构建时只能一个一个处理任务，无法一次性处理多个任务。</p>
<p>让webpack支持多线程的话有两个方式：<code>HappyPack</code>(不维护)和<code>thread-loader</code>。</p>
<p><strong>HappyPack配置</strong>：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> HappyPack = <span class="hljs-built_in">require</span>(<span class="hljs-string">'happypack'</span>);
<span class="hljs-keyword">const</span> happyThreadPool = HappyPack.ThreadPool(&#123; <span class="hljs-attr">size</span>: os.cpus().length &#125;);

<span class="hljs-built_in">module</span>.exports = &#123;
    <span class="hljs-attr">rules</span>: [
      &#123;
        <span class="hljs-attr">test</span>: <span class="hljs-regexp">/\.jsx?$/</span>,
        exclude: <span class="hljs-regexp">/node_modules/</span>,
        loader: <span class="hljs-string">'happypack/loader?id=jsx'</span>
      &#125;,
    ],
    <span class="hljs-attr">plugins</span>: [
      <span class="hljs-keyword">new</span> HappyPack(&#123;
        <span class="hljs-attr">id</span>: <span class="hljs-string">'jsx'</span>,
        <span class="hljs-attr">threadPool</span>: happyThreadPool,
        <span class="hljs-attr">loaders</span>: [
          &#123;
            <span class="hljs-attr">loader</span>: <span class="hljs-string">'babel-loader'</span>,
            <span class="hljs-attr">options</span>: &#123;
              <span class="hljs-attr">cacheDirectory</span>: <span class="hljs-string">'.webpack_cache'</span>
            &#125;
          &#125;
        ]
      &#125;)
    ]
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这边我们使用<code>babel-loader</code>时使用指定的目录将用来缓存<code> loader</code> 的执行结果。之后的 webpack 构建，将会尝试读取缓存，来避免在每次执行时，可能产生的、高性能消耗的 Babel 重新编译过程。</p>
<p>当然并不是所有的<code>loader</code>都需要用<code>happypack</code>开启多线程，因为多线程本身的启动也是需要时间的，项目不大或者不是耗时的<code>loader</code>可选择不开启。</p>
<h3 data-id="heading-6">thread-loader</h3>
<p><strong>thread-loader配置</strong>:
thread-loader配置相比于happypack会更加简单。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-built_in">module</span>.exports = &#123;
    <span class="hljs-attr">module</span>: &#123;
        <span class="hljs-attr">rules</span>: [
            &#123;
                <span class="hljs-attr">test</span>: <span class="hljs-regexp">/\.jsx?$/</span>,
                use: [<span class="hljs-string">'thread-loader'</span>, <span class="hljs-string">'babel-loader'</span>]
            &#125;
        ]
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-7">缓存</h2>
<h3 data-id="heading-8">cache-loader</h3>
<p>因为每次<code>webpack</code>打包编译会把所有的文件重新打包编译一遍，这也意味着很多文件没有修改也会重新编译，实际上这样也会导致构建时间的增多，在性能开销较大的<code>loader</code>，可以用<code>cache-loader</code>将结果缓存下来。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-built_in">module</span>.exports = &#123;
    <span class="hljs-attr">module</span>: &#123;
        <span class="hljs-attr">rules</span>: [
            &#123;
                <span class="hljs-attr">test</span>: <span class="hljs-regexp">/\.jsx?$/</span>,
                use: [<span class="hljs-string">'cache-loader'</span>, <span class="hljs-string">'babel-loader'</span>]
            &#125;
        ]
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>上文我们看到其实<code>babel-loader</code>自带了缓存功能，但是可能有些<code>loader</code>没有这种配置，可使用<code>cache-loader</code>缓存编译结果。</p>
<h2 data-id="heading-9">基础模块抽离</h2>
<h3 data-id="heading-10">webpack-dll-pllugin</h3>
<p>基础模块抽离主要就是将一些不会经常变更的第三方依赖，单独抽离出来。例如我们在项目里面常用的<code>react全家桶，lodash</code>等。</p>
<p>实际上我们每次打包都要去编译这些几乎不需要变更的第三方依赖库，这会导致我们浪费很多时间，我们可以使用<code>webpack-dll-plugin</code>库以一种<code>预编译</code>的方式，将这些基础模块提前<code>打包成一个个动态链接库</code>（一个链接库可包括多个模块），之后每次打包的时候就不用再去编译这些基础库，只要这些第三方依赖库的版本没有改变，我们就不需要重新去编译。</p>
<h3 data-id="heading-11">externals</h3>
<p>除了可以使用<code>webpack-dll-plugin</code>去将基础库进行预编译，还可以使用<code>CDN</code>引入这些库，并配合<code>webpack</code>的<code>externals</code>配置不将这些库打包进去以优化构建速度。</p>
<p><strong>index.html</strong>:</p>
<pre><code class="hljs language-js copyable" lang="js"><script
  src=<span class="hljs-string">"https://code.jquery.com/jquery-3.1.0.js"</span>
  crossorigin=<span class="hljs-string">"anonymous"</span>
></script>
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>webpack.config.js</strong>:</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-built_in">module</span>.exports = &#123;
    <span class="hljs-comment">//...</span>
    <span class="hljs-attr">externals</span>: &#123;
        <span class="hljs-string">'jquery'</span>: <span class="hljs-string">'jQuery'</span>
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这样通过<code>import $ from 'jquery';</code>依然可以使用jquery。</p>
<h2 data-id="heading-12">缩小文件搜索范围</h2>
<h3 data-id="heading-13">resolve.modules</h3>
<p>由于webpack搜索第三方依赖库，先会搜索<code>./node_modules</code>，然后没搜索到会继续往上一层<code>../node_modules</code>，以此内推。因此我们可以指定好第三方依赖库的路径，减少搜索时间。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> path = <span class="hljs-built_in">require</span>(<span class="hljs-string">'path'</span>);
<span class="hljs-built_in">module</span>.exports = &#123;
    <span class="hljs-comment">//...</span>
    <span class="hljs-attr">resolve</span>: &#123;
        <span class="hljs-attr">modules</span>: [path.resolve(__dirname, <span class="hljs-string">'node_modules'</span>)],
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-14">resolve.extensions</h3>
<p>当我们导入的文件没有后缀的时候，我们可以通过指定<code>resolve.extensions</code>来告诉webpack的后缀的搜索顺序，一般频率最高的放在最前面以此来减少搜索次数。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-built_in">module</span>.exports = &#123;
    <span class="hljs-comment">//...</span>
    <span class="hljs-attr">resolve</span>: &#123;
        <span class="hljs-attr">extensions</span>: [<span class="hljs-string">'jsx'</span>,<span class="hljs-string">'js'</span>,<span class="hljs-string">'json'</span>]
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-15">module.noParse</h3>
<p>由于一些如<code>jquery</code>和<code>chartjs</code>等库没有实现模块化标准，这样解析这些库会浪费时间而且没有意义。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-built_in">module</span>.exports = &#123;
    <span class="hljs-comment">//...</span>
    <span class="hljs-attr">module</span>: &#123;
        <span class="hljs-attr">noParse</span>: <span class="hljs-regexp">/jquery/</span>
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-16">loader下的exclude和include</h3>
<p>在<code>webpack</code>的<code>loader</code>编译模块时，我们可以指定<code>exclude和include</code>属性，<code>exclude</code>表示哪些文件夹下的模块不需要编译，<code>include</code>表示哪些文件夹下模块需要编译，两者同样使用的是绝对路径。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> path = <span class="hljs-built_in">require</span>(<span class="hljs-string">'path'</span>);
<span class="hljs-built_in">module</span>.exports = &#123;
    <span class="hljs-comment">//...</span>
    <span class="hljs-attr">module</span>: &#123;
        <span class="hljs-attr">rules</span>: [
            &#123;
                <span class="hljs-attr">test</span>: <span class="hljs-regexp">/\.js[x]?$/</span>,
                use: [<span class="hljs-string">'babel-loader'</span>],
                <span class="hljs-attr">exclude</span>: [path.resolve(__dirname, <span class="hljs-string">'node_modules'</span>)]
            &#125;
        ]
    &#125;,
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>参考：</p>
<p><a href="http://webpack.wuhaolin.cn/" target="_blank" rel="nofollow noopener noreferrer">深入浅出 Webpack</a></p></div>  
</div>
            