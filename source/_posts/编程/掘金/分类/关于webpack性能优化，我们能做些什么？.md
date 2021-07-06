
---
title: '关于webpack性能优化，我们能做些什么？'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/0234702e819c4f1c94fce6869e0d88c6~tplv-k3u1fbpfcp-zoom-1.image'
author: 掘金
comments: false
date: Sun, 04 Jul 2021 23:13:05 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/0234702e819c4f1c94fce6869e0d88c6~tplv-k3u1fbpfcp-zoom-1.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/0234702e819c4f1c94fce6869e0d88c6~tplv-k3u1fbpfcp-zoom-1.image" alt="file" loading="lazy" referrerpolicy="no-referrer"></p>
<p>本文首发于：<a href="https://github.com/bigo-frontend/blog/" target="_blank" rel="nofollow noopener noreferrer">github.com/bigo-fronte…</a> 欢迎关注、转载。</p>
<h1 data-id="heading-0"><strong>我们做了啥</strong></h1>
<p>Bigo前端组计算平台前端组基于amis框架，参考之前的文章：<a href="https://github.com/bigo-frontend/blog/issues/17" target="_blank" rel="nofollow noopener noreferrer">github.com/bigo-fronte…</a> ，有很好的研发效率提升，但是构建速度却很慢，亟需进行优化。优化之后达到了将webpack构建速度提升80%左右的一个成绩，以下是优化前后的对比👇</p>
<p><strong>30965ms  ➡️      6545ms</strong></p>
<p>团队做了3件事情来达到这样的一个效果：</p>
<ol>
<li><code>split-chunks</code>进行公共模块优化👇
<pre><code class="copyable">optimization: &#123;
    splitChunks: &#123;
        chunks: "all",
        cacheGroups: &#123;
            vendorsa: &#123;
                chunks: 'all',
                test: /(mobx-state-tree|react-color|react-dom-router|sortablejs|mobx-react)/,
                priority: 100,
                name: 'vendors-react-mobx',
            &#125;,
            venodrb: &#123;
                test: /lodash/,
                priority: 100,
                name: 'vendor-lodash',
                chunks: 'all'
            &#125;,
        &#125;
    &#125;
&#125;,
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
<li><code>external</code>避免将比较大的第三方依赖打包到bundle中👇
<pre><code class="copyable">webpack.config.js:

externals: [
    &#123;
        'react': 'React',
        'react-dom': 'ReactDOM',
        'moment': 'moment',
        'mobx': 'mobx',
        'monaco-editor': 'monaco',
        'echarts': 'echarts',
        'jquery': 'jQuery',
        'hls.js': 'hls',
        'flv.js': 'flv',
    &#125;,
    function (context, request, callback) &#123;
        if (/^moment\/.+$/.test(request)) &#123;
            return callback(null, 'root ' + 'moment');
        &#125;
        if (/^tinymce\/.+$/.test(request))&#123;
            return callback(null, 'root ' + 'tinymce');
        &#125;
        if (/^froala-editor\/.+$/.test(request))&#123;
            return callback(null, 'root ' + 'froala');
        &#125;
        if (/^echarts\/.+$/.test(request))&#123;
            return callback(null, 'root ' + 'echarts');
        &#125;
        // 继续下一步且不外部化引用
        callback();
    &#125;,
]

index.html:
<script src="https://unpkg.com/react@16.8.6/umd/react.production.min.js"></script>
<script src="https://unpkg.com/react-dom@16.8.6/umd/react-dom.production.min.js"></script>
<script src="https://unpkg.com/moment@2.29.1/min/moment.min.js"></script>
<script src="https://unpkg.com/moment@2.29.1/min/locales.min.js"></script>
<script src="https://unpkg.com/mobx@4.5.2/lib/mobx.umd.min.js"></script>
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
<li>对<code>ts-loader</code>的优化：
<pre><code class="copyable">&#123;
    test: /\.tsx?$/,
    use: [
      &#123;
        loader: 'ts-loader',
        options: &#123;
          transpileOnly: true
        &#125;
      &#125;
    ],
    exclude: /node_modules/
&#125;,
  ...

plugins: [
    new ForkTsCheckerWebpackPlugin(),
]
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
</ol>
<p>基于这次优化做了功课，看了一些资料，看看还有哪些可以优化的地方。</p>
<h1 data-id="heading-1"><strong>webpack是什么</strong></h1>
<p>官网的定义：</p>
<p><em>webpack is a static module bundler for modern JavaScript applications. When webpack processes your application, it internally builds a dependency graph which maps every module your project needs and generates one or more bundles.</em></p>
<p>也就是说 webpack 是一个用于现代 JavaScript 应用程序的静态模块打包工具，从入口出发，找到入口文件所有的依赖，生成浏览器可以用的bundle文件。webpack的出现使得前端的工程化更加地丰富。从webpack在2013的第一次release(v1.0.0-beta2)开始，至今已经有8、9年的历史了，是一个相当成熟的工具，其生态也比较完善，所以前端圈用webpack也是非常地广泛。</p>
<h1 data-id="heading-2"><strong>版本</strong></h1>
<p>尽量用较新的版本，新版本想较之前都会有一定的性能提升和优化，包括Node和Webpack。要注意的是<code>Node.js v8.9.10 - v9.11.1</code>ES6的<code>Set</code>和<code>Map</code>会有性能回退问题，现在LTS的node已经是<code>v14.16.0</code>，所以假设<code>Node</code>版本已经较新，并且用的是<code>WP4</code>(<code>webpack4</code>)。目前还不建议对求稳的或者已经很庞大的项目立即升级到<code>WP5</code>，其一是因为webpack生态里面并不一定所有的插件都能跟的上最新的版本，可能会出现兼容性的问题；其二由于webpack5还并未被广泛地应用，到新版本的稳定和成熟还是需要一定的时间，为避免不必要的bug，建议暂时使用<code>webpack4</code>。</p>
<h1 data-id="heading-3"><strong>为什么要优化</strong></h1>
<p>对于开发者来说，每次在build的时候不希望花费较长的时间，优化构建速度能够减少开发成本；对于用户而言，优化bundle文件的数量和大小能减少用户的流失率，提升用户体验。所以webpack的性能优化是一个非常关键的技术手段。</p>
<h1 data-id="heading-4"><strong>优化手段</strong></h1>
<h3 data-id="heading-5"><ins>两个测量工具</ins></h3>
<ul>
<li><code>speed-measure-webpack-plugin</code>(<strong>SMP</strong>)，要对webpack的构建速度进行优化，得知道要优化的重点在哪里，而该插件则是帮助检查哪些地方需要进一步优化的工具。</li>
<li><code>webpack-bundle-analyzer</code>，虽然webpack也有官方的<a href="https://github.com/webpack/analyse" target="_blank" rel="nofollow noopener noreferrer">分析工具</a>，社区也有许多其他的工具可以参考，但是通过资料、技术分享以及项目经验，<code>webpack-bundle-analyzer</code>用的还是不错的，它可以将bundle展示为交互式、可缩放的树状图形式，使用起来非常便捷。</li>
</ul>
<h3 data-id="heading-6"><ins>三个可优化阶段<ins></ins></ins></h3>
<p>webpack构建大概可分为<strong>loader解析</strong> -> <strong>依赖搜索</strong> -> <strong>打包</strong>等三个阶段，就这三个阶段我们分别展开阐述如何去优化。</p>
<p><strong>loader解析：</strong></p>
<ul>
<li>
<p><code>include/exclude</code>，对于loader而言，不需要对项目中所有的文件进行文件转换，应将loader应用于最少数量的必要模块，常见的配置：</p>
<pre><code class="copyable">&#123;
    ...,
    exclude: /node_modules/
&#125;,
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
<li>
<p>如果项目中用到了<code>ts-loader</code>，那就要小心了，因为如果不做额外的配置，会发现构建速度是非常耗时的。原因是因为<code>ts-loader</code>在每次构建的时候都会对所有文件进行类型检查，当项目越来越庞大，会发现构建速度越来越慢。这个时候需要设置<code>transpileOnly: true</code>来提高构建速度，该配置只处理编译而不做类型检查；然而类型检查是使用<code>TypeScript</code>的初衷，可以使用<code>fork-ts-checker-webpack-plugin</code>插件来在<strong>单独的进程</strong>中做类型检查。那性能和类型检查都能cover到。</p>
</li>
<li>
<p>如果使用的是<code>babel-loader</code>，可以设置其cache相关的选项，比如<code>cacheDirectory</code>、<code>cacheCompression</code>等；</p>
</li>
<li>
<p><code>cache-loader</code>: 利用文件的modifier time来检查文件是否更新，如果没有更新则利用缓存的内容，是一个轻量级的比较。特点是在第一次构建的时候比较慢，后面的构建会快很多。但是用它也要特别注意，最好用在性能消耗比较昂贵的地方，否则基本没有什么效果。该loader已经被作者<strong>Archive</strong>了，因为webpack5内置了cache的相关配置，将来如果升级就不需要它了。使用cache-loader时要放在其他loader的前面。</p>
</li>
<li>
<p><code>thread-loader</code>：也是应用于比较昂贵的地方，可以将打包任务划分多个node进程，把模块一次分配给这些进程，实现多进程构建。跟<code>cache-loader</code>一样也需要放到其他loader的前面。</p>
<pre><code class="copyable">&#123;
    ...,
    use: [
        'thread-loader',
        // 昂贵的loader (e.g babel-loader)
    ],
&#125;,
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
<li>
<p>最后一点是，尽量少用工具，因为每个loader/plugin都有其启动时间，不用就不会有性能问题啦。</p>
</li>
</ul>
<p><strong>依赖搜索：</strong></p>
<ul>
<li>
<p>减少 <code>resolve.modules</code>, <code>resolve.extensions</code>等 中条目数量，因为IO操作比较消耗性能；</p>
</li>
<li>
<p>基本上webpack对这些配置有默认值，比如<code>resolve.modules</code>为<code>node_modules</code>，告诉webpack解析模块时应该搜索<code>node_modules</code>目录；<code>resolve.extensions</code>默认值为<code>['.wasm', '.mjs', '.js', '.json']</code>，如果用了<code>TypeScript</code>还是要配置一下的，<code>extensions</code>是说在引入模块时可以不需要带扩展:</p>
<pre><code class="copyable">import File from '../path/to/file';
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
</ul>
<p><strong>打包: Smaller = Faster</strong></p>
<ul>
<li>
<p><code>splitChunks</code>，本着“小即是快”的原则，尽量使chunk包越小越好。在webpack4之前，可以使用<code>CommonsChunkPlugin</code>来避免模块与模块之间的重复依赖，webpack4内置了<code>optimization.splitChunks</code>，可开箱即用。<code>splitChunks</code>有它默认的行为，不同的项目根据需求做不同的调整。可以设置不同的cacheGroup，拆分前必须共享模块的最小chunk数量等等，能最大程度地优化重复依赖的问题。一个简单的🌰 ：</p>
<pre><code class="copyable">splitChunks: &#123;
  chunks: "all",
  cacheGroups: &#123;
    lodash: &#123;
      test: /lodash/,
      priority: 1,
    &#125;,
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
<li>
<p><code>externals</code>，防止将某些 import 的包打包到 bundle 中，而是在运行时再去从外部获取这些扩展依赖。例如：</p>
<pre><code class="copyable">externals: [
    &#123;
        'moment': 'moment',
    &#125;
    ...
]
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
</ul>
<p>当然需要在<code>index.html</code>里面引入cdn依赖，否则在runtime无法找到相应的模块：<code><script src="https://unpkg.com/moment@2.29.1/min/moment.min.js"></script></code>。</p>
<h1 data-id="heading-7"><strong>多环境</strong></h1>
<p><ins><strong>生产环境</strong></ins><strong>：</strong> 生产环境关注与压缩bundle、更轻量的source map等，建议不同环境写不同的配置，当然可以有共用的配置，利用<code>webpack-merge</code>可以实现配置共用；对于devTools，推荐使用<code>source-Map</code>，相对于<code>inline-source-map</code>和<code>eval-cheap-module-source-map</code>性能好一点；代码压缩，在WP5中内置了<code>terser-webpack-plugin</code>，现在使用WP4的话，需要安装插件，这个插件功能非常强大，除了基本的压缩功能以外，还可以使用多进程并发构建，以及去除注释等功能；不带路径的配置，<code>path-info</code>会在bundle中包含模块信息的注释，但在庞大的项目中，会导致GC性能很差，应该关闭；</p>
<p><ins><strong>开发环境</strong></ins><strong>：</strong> 同样地，生产环境有些配置也不适用于开发环境，比如<code>TerserPlugin</code>就不需要，因为在开发环境中压缩代码是没有意义的；devTools的最佳实践是<code>eval-cheap-module-source-map</code>，我现在的项目比较轻量，但是也能看出对比：</p>
<pre><code class="copyable">`inline-source-map`：5205ms

VS

`eval-cheap-module-source-map`： 4744ms
<span class="copy-code-btn">复制代码</span></code></pre>
<p>虽然是不到1000ms的差距，苍蝇肉也是肉不是？而且将来代码量越来越庞大的时候，差距就更明显了。</p>
<p>当然还有其他的可以优化的方法，比如使用ES module，能更好地利用webpack的tree shaking功能；Dll，为更改不频繁的代码生成单独的编译结果，但却是一个配置比较复杂的过程；还有对图片的压缩等等。以上是对于webpack4性能优化基本的配置，期待webpack5成熟稳定的那一天。</p>
<h3 data-id="heading-8"><ins>参考</ins>：</h3>
<ul>
<li><a href="https://webpack.docschina.org/guides/build-performance/" target="_blank" rel="nofollow noopener noreferrer">webpack.docschina.org/guides/buil…</a></li>
<li><a href="https://developers.google.com/web/fundamentals/performance/webpack" target="_blank" rel="nofollow noopener noreferrer">developers.google.com/web/fundame…</a></li>
</ul>
<p>欢迎大家留言讨论，祝工作顺利、生活愉快！</p>
<p>我是bigo前端，下期见。</p></div>  
</div>
            