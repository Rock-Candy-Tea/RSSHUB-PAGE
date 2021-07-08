
---
title: '剖析 Webpack SplitChunksPlugin 源码_ 学完你也能写一个'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/ef02460089204bcf94af0683e5e074f4~tplv-k3u1fbpfcp-zoom-1.image'
author: 掘金
comments: false
date: Wed, 07 Jul 2021 04:18:15 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/ef02460089204bcf94af0683e5e074f4~tplv-k3u1fbpfcp-zoom-1.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h1 data-id="heading-0">研究背景</h1>
<p>上个月团队很多人都在反馈有个项目打包速度越来越慢，打包发布一次至少要半个小时，这个速度不仅我们接受不了，测试那边也多次反馈发布进度卡在前端，因此对该项目进行了打包优化。</p>
<h2 data-id="heading-1">对项目进行 bundle 分析</h2>
<h3 data-id="heading-2">优化前</h3>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/ef02460089204bcf94af0683e5e074f4~tplv-k3u1fbpfcp-zoom-1.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer">
目前线上splitChunks.cacheGroups配置如下：</p>
<pre><code class="hljs language-ts copyable" lang="ts">&#123; 
        <span class="hljs-attr">styles</span>: &#123; 
            <span class="hljs-attr">name</span>: <span class="hljs-string">'style'</span>, 
            <span class="hljs-attr">test</span>: <span class="hljs-function"><span class="hljs-params">m</span> =></span> m.constructor.name === <span class="hljs-string">'CssModule'</span>, 
            <span class="hljs-attr">chunks</span>: <span class="hljs-string">'all'</span>, 
            <span class="hljs-attr">enforce</span>: <span class="hljs-literal">true</span>, 
            <span class="hljs-attr">priority</span>: <span class="hljs-number">40</span>, 
        &#125;, 
        <span class="hljs-attr">emcommon</span>: &#123; 
            <span class="hljs-attr">name</span>: <span class="hljs-string">'emcommon'</span>, 
            <span class="hljs-attr">test</span>: <span class="hljs-function"><span class="hljs-params">module</span> =></span> &#123; 
                <span class="hljs-keyword">const</span> regs = [<span class="hljs-regexp">/@ant-design/</span>, <span class="hljs-regexp">/@em/</span>, <span class="hljs-regexp">/@bytedesign/</span>]; 
                <span class="hljs-keyword">return</span> regs.some(<span class="hljs-function"><span class="hljs-params">reg</span> =></span> reg.test(<span class="hljs-built_in">module</span>.context)); 
            &#125;, 
            <span class="hljs-attr">chunks</span>: <span class="hljs-string">'all'</span>, 
            <span class="hljs-attr">enforce</span>: <span class="hljs-literal">true</span>, 
            <span class="hljs-attr">priority</span>: <span class="hljs-number">30</span>, 
        &#125;, 
        <span class="hljs-attr">byteedu</span>: &#123; 
            <span class="hljs-attr">name</span>: <span class="hljs-string">'byteedu'</span>, 
            <span class="hljs-attr">test</span>: <span class="hljs-function"><span class="hljs-params">module</span> =></span> &#123; 
                <span class="hljs-keyword">const</span> regs = [ 
                    <span class="hljs-regexp">/@ax/</span>, 
                    <span class="hljs-regexp">/@bridge/</span>, 
                    <span class="hljs-regexp">/axios/</span>, 
                    <span class="hljs-regexp">/lodash/</span>, 
                    <span class="hljs-regexp">/@byted-edu/</span>, 
                    <span class="hljs-regexp">/codemirror/</span>, 
                    <span class="hljs-regexp">/@syl-editor/</span>, 
                    <span class="hljs-regexp">/prosemirror/</span>, 
                ]; 
                <span class="hljs-keyword">return</span> regs.some(<span class="hljs-function"><span class="hljs-params">reg</span> =></span> reg.test(<span class="hljs-built_in">module</span>.context)); 
            &#125;, 
            <span class="hljs-attr">chunks</span>: <span class="hljs-string">'all'</span>, 
            <span class="hljs-attr">enforce</span>: <span class="hljs-literal">true</span>, 
            <span class="hljs-attr">priority</span>: <span class="hljs-number">20</span>, 
        &#125;, 
        <span class="hljs-attr">default</span>: &#123; 
            <span class="hljs-attr">minChunks</span>: <span class="hljs-number">2</span>, 
            <span class="hljs-attr">priority</span>: <span class="hljs-number">1</span>, 
            <span class="hljs-attr">chunks</span>: <span class="hljs-string">'all'</span>, 
            <span class="hljs-attr">reuseExistingChunk</span>: <span class="hljs-literal">true</span>, 
        &#125;, 
    &#125;; 
&#125; 
<span class="copy-code-btn">复制代码</span></code></pre>
<p>优化前，我们项目在生产环境打包需要14min，通过bundle分析不难发现，并且多个页面都重复打包了arco-design等，很多应该抽离的chunk并没有抽取，导致最终产物极大。这也是打包时间缓慢的重要原因。究其根本原因：default配置没有起作用；按照我们的期望当一个modules被两个或两个以上的chunk共用时，应该就会被提取成独立的chunk，但是结果事与愿违，从bundle分析结果图可以看出arco-design明明被多个chunk共用，却并没有触发该配置。</p>
<h3 data-id="heading-3">优化后</h3>
<p>定位到问题是default配置没有生效后，我们就针对default进行了一系列的修改，发现当我们将maxAsyncRequests设置为30的时候，default配置起作用了，最终抽离公用chunk，将打包大小降为30M左右，足足缩小了90%。线上打包时间更是缩短到了2.5min左右。
为什么配置maxAsyncRequests才能按照我们的期望进行分包？maxAsyncRequests又是什么？webpack的分包逻辑到底是如何运行的？一系列的问题就需要从webpack的源码出发进行解答了。</p>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-keyword">default</span>: &#123; 
            <span class="hljs-attr">maxAsyncRequests</span>: <span class="hljs-number">30</span>,  
            <span class="hljs-attr">minChunks</span>: <span class="hljs-number">2</span>, 
            <span class="hljs-attr">priority</span>: <span class="hljs-number">1</span>, 
            <span class="hljs-attr">chunks</span>: <span class="hljs-string">'all'</span>, 
            <span class="hljs-attr">reuseExistingChunk</span>: <span class="hljs-literal">true</span>, 
        &#125; 
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/2945f4e0d87c4e4182d3bba2475edc83~tplv-k3u1fbpfcp-zoom-1.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h1 data-id="heading-4">Module和Chunk的关系</h1>
<p>由于下文会频繁的出现module和chunk，所以首先单独介绍一下Module和Chunk的关系以及这两者是什么？首先通过一个关系图来理解：</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/155b0b9641e946f1b48cdcb9e8fb587d~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<ol>
<li>对于一份同逻辑的代码，当我们手写下一个一个的文件，它们无论是 ESM 还是 commonJS 或是 AMD，他们都是 <strong>module</strong></li>
<li>当我们写的 module 源文件传到 webpack 进行打包时，webpack 会根据文件引用关系生成 <strong>chunk</strong> 文件，webpack 会对这个 chunk 文件进行一些操作</li>
</ol>
<h1 data-id="heading-5">SplitChunksPlugin</h1>
<p>我们项目的webpack版本为4.44.2，因此选择这个版本的webpack进行源码解析，进一步了解SplitChunksPlugin如何进行打包的。</p>
<p>SplitChunksPlugin 引入缓存组（cacheGroups）对模块（module）进行分组，每个缓存组根据规则将匹配到的模块分配到代码块（chunk）中，每个缓存组的打包结果可以是单一 chunk，也可以是多个 chunk。webpack 的默认优化就是通过 SplitChunksPlugin 配置实现的，具体可参考<a href="https://link.juejin.cn/?target=https%3A%2F%2Fv4.webpack.js.org%2Fplugins%2Fsplit-chunks-plugin%2F%23root" target="_blank" rel="nofollow noopener noreferrer" title="https://v4.webpack.js.org/plugins/split-chunks-plugin/#root" ref="nofollow noopener noreferrer">官方文档</a>。</p>
<h2 data-id="heading-6">默认配置</h2>
<p>实际开发会发现哪怕SplitChunksPlugin什么也没有配置，生产环境下还是会按照一些规则进行打包，为什么会这样？这就需要从源码找答案，webpack4有一个文件叫做WebpackOptionsDefaulter.js，在这个文件中有一系列的默认配置。文件的第226行-256行：</p>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-built_in">this</span>.set(<span class="hljs-string">"optimization.splitChunks"</span>, &#123;&#125;); 
<span class="hljs-built_in">this</span>.set(<span class="hljs-string">"optimization.splitChunks.hidePathInfo"</span>, <span class="hljs-string">"make"</span>, <span class="hljs-function"><span class="hljs-params">options</span> =></span> &#123; 
  <span class="hljs-keyword">return</span> isProductionLikeMode(options); 
&#125;); 
<span class="hljs-built_in">this</span>.set(<span class="hljs-string">"optimization.splitChunks.chunks"</span>, <span class="hljs-string">"async"</span>); 
<span class="hljs-built_in">this</span>.set(<span class="hljs-string">"optimization.splitChunks.minSize"</span>, <span class="hljs-string">"make"</span>, <span class="hljs-function"><span class="hljs-params">options</span> =></span> &#123; 
  <span class="hljs-keyword">return</span> isProductionLikeMode(options) ? <span class="hljs-number">30000</span> : <span class="hljs-number">10000</span>; 
&#125;); 
<span class="hljs-built_in">this</span>.set(<span class="hljs-string">"optimization.splitChunks.minChunks"</span>, <span class="hljs-number">1</span>); 
<span class="hljs-built_in">this</span>.set(<span class="hljs-string">"optimization.splitChunks.maxAsyncRequests"</span>, <span class="hljs-string">"make"</span>, <span class="hljs-function"><span class="hljs-params">options</span> =></span> &#123; 
  <span class="hljs-keyword">return</span> isProductionLikeMode(options) ? <span class="hljs-number">5</span> : <span class="hljs-literal">Infinity</span>; 
&#125;); 
<span class="hljs-built_in">this</span>.set(<span class="hljs-string">"optimization.splitChunks.automaticNameDelimiter"</span>, <span class="hljs-string">"~"</span>); 
<span class="hljs-built_in">this</span>.set(<span class="hljs-string">"optimization.splitChunks.automaticNameMaxLength"</span>, <span class="hljs-number">109</span>); 
<span class="hljs-built_in">this</span>.set(<span class="hljs-string">"optimization.splitChunks.maxInitialRequests"</span>, <span class="hljs-string">"make"</span>, <span class="hljs-function"><span class="hljs-params">options</span> =></span> &#123; 
  <span class="hljs-keyword">return</span> isProductionLikeMode(options) ? <span class="hljs-number">3</span> : <span class="hljs-literal">Infinity</span>; 
&#125;); 
<span class="hljs-built_in">this</span>.set(<span class="hljs-string">"optimization.splitChunks.name"</span>, <span class="hljs-literal">true</span>); 
<span class="hljs-built_in">this</span>.set(<span class="hljs-string">"optimization.splitChunks.cacheGroups"</span>, &#123;&#125;); 
<span class="hljs-built_in">this</span>.set(<span class="hljs-string">"optimization.splitChunks.cacheGroups.default"</span>, &#123; 
  <span class="hljs-attr">automaticNamePrefix</span>: <span class="hljs-string">""</span>, 
  <span class="hljs-attr">reuseExistingChunk</span>: <span class="hljs-literal">true</span>, 
  <span class="hljs-attr">minChunks</span>: <span class="hljs-number">2</span>, 
  <span class="hljs-attr">priority</span>: -<span class="hljs-number">20</span> 
&#125;); 
<span class="hljs-built_in">this</span>.set(<span class="hljs-string">"optimization.splitChunks.cacheGroups.vendors"</span>, &#123; 
  <span class="hljs-attr">automaticNamePrefix</span>: <span class="hljs-string">"vendors"</span>, 
  <span class="hljs-attr">test</span>: <span class="hljs-regexp">/[\\/]node_modules[\\/]/</span>, 
  priority: -<span class="hljs-number">10</span> 
&#125;); 
<span class="copy-code-btn">复制代码</span></code></pre>
<p>从源码可以看出，SplitChunksPlugin的默认配置在不同的环境下也有变化，比如minSize在生产环境是30000字节，而非生产环境是10000字节。但是官方文档并没有展示这些细节，估计是默认我们最终都会将代码打包到生产环境，但是实际中，我们会在不同模式下切换，因此还是需要注意到这些细节，毕竟开发环境的打包速度也是我们需要关心的。</p>
<h2 data-id="heading-7">基本属性</h2>
<p>结合前面提到的默认配置的源码，可以确定生产模式下，SplitChunksPlugin的默认配置如下：</p>
<pre><code class="hljs language-ts copyable" lang="ts">splitChunks: &#123; 
    <span class="hljs-attr">chunks</span>: <span class="hljs-string">"async"</span>, 
    <span class="hljs-attr">minSize</span>: <span class="hljs-number">30000</span>, 
    <span class="hljs-attr">minChunks</span>: <span class="hljs-number">1</span>, 
    <span class="hljs-attr">maxAsyncRequests</span>: <span class="hljs-number">5</span>, 
    <span class="hljs-attr">maxInitialRequests</span>: <span class="hljs-number">3</span>, 
    <span class="hljs-attr">automaticNameDelimiter</span>: <span class="hljs-string">'~'</span>, 
    <span class="hljs-attr">name</span>: <span class="hljs-literal">true</span>, 
    <span class="hljs-attr">cacheGroups</span>: &#123; 
        <span class="hljs-attr">vendors</span>: &#123; 
            <span class="hljs-attr">test</span>: <span class="hljs-regexp">/[\\/]node_modules[\\/]/</span>, 
            priority: -<span class="hljs-number">10</span> 
        &#125;, 
            <span class="hljs-attr">default</span>: &#123; 
            <span class="hljs-attr">minChunks</span>: <span class="hljs-number">2</span>, 
            <span class="hljs-attr">priority</span>: -<span class="hljs-number">20</span>, 
            <span class="hljs-attr">reuseExistingChunk</span>: <span class="hljs-literal">true</span> 
        &#125; 
    &#125; 
&#125; 
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这些配置都是什么意义和作用的？一个一个来看：</p>
<ul>
<li><strong>chunks</strong>: 指的的那些chunks需要进行优化，是一个字符串类型，有效值是：all，async和initial。
<ul>
<li><code>async</code>这个值表示按需引入的模块将会被用于优化。</li>
<li><code>initial</code>表示项目中被直接引入的模块将会被用于优化。</li>
<li><code>all</code>顾名思义，表明直接引入和按需引入的模块都会被用于优化。</li>
</ul>
</li>
<li><strong>minSize</strong>: 打包优化完生成的新chunk大小要> 30000字节，否则不生成新chunk。</li>
<li><strong>minChunks</strong>: 共享该module的最小chunk数</li>
<li><strong>maxAsyncRequests</strong>：最多有N个异步加载请求该module</li>
<li><strong>maxInitialRequests</strong>： 一个入口文件可以并行加载的最大文件数量</li>
<li><strong>automaticNameDelimiter</strong>：名字中间的间隔符</li>
<li><strong>name</strong>：chunk的名字，
<ul>
<li>如果设成true，会根据被提取的chunk自动生成。</li>
<li>值为 false 时，适合生产模式使用，webpack 会避免对 chunk 进行不必要的命名，以减小打包体积，除了入口 chunk 外，其他 chunk 的名称都由 id 决定，所以最终看到的打包结果是一排数字命名的 js，这也是为啥我们看线上网页请求的资源，总会掺杂一些 0.js，1.js 之类的文件(当然，使资源名为数字 id 的方式不止这一种，懒加载也能轻松办到)。</li>
<li>值为 string 时，缓存组最终会打包成一个 chunk，名称就是该 string。此外，当两个缓存组 name 一样，最终会打包在一个 chunk 中。你甚至可以把它设为一个入口的名称，从而将这个入口会移除。</li>
</ul>
</li>
<li><strong>cacheGroups</strong>： 这个就是重点了，我们要切割成的每一个新chunk就是一个cache group。
<ul>
<li><strong>test</strong>：用来决定提取哪些module，可以接受字符串，正则表达式，或者函数，函数的一个参数为module，第二个参数为引用这个module的chunk(数组)。</li>
<li><strong>priority</strong>：优先级高的chunk为被优先选择(说出来感觉好蠢),优先级一样的话，size大的优先被选择。</li>
<li><strong>reuseExistingChunk</strong>: 当module未变时，是否可以使用之前的chunk。</li>
<li>要禁用任何默认缓存组，请将它们设置为<code>false</code>。例如 default:false</li>
</ul>
</li>
</ul>
<p>这些规则一旦制定，只有全部满足的模块才会被提取，所以需要根据项目情况合理配置才能达到满意的优化结果。</p>
<h2 data-id="heading-8">执行流程</h2>
<p>首先看一下wbepack的主题流程：
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/4864200ef70647089fd74448c9d40f12~tplv-k3u1fbpfcp-zoom-1.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer">
流程图中展示了些核心任务点，简要说明下：</p>
<ul>
<li>通过yargs解析config和shell的配置项</li>
<li>webpack 初始化过程，首先会根据第一步的 options 生成 compiler 对象，然后初始化 webpack 的内置插件及 options 配置</li>
<li>run 代表编译的开始，会构建 compilation 对象，用于存储这一次编译过程的所有数据</li>
<li>make 执行真正的编译构建过程，从入口文件开始，构建模块，直到所有模块创建结束</li>
<li>seal 生成 chunks，对 chunks 进行一系列的优化操作，并生成要输出的代码</li>
<li>seal 结束后，Compilation 实例的所有工作到此也全部结束，意味着一次构建过程已经结束</li>
</ul>
<p>Webpack 插件统一以 <code>apply</code> 方法为入口，然后注册优化事件，<code>apply</code>方法接收一个参数，该参数是webpack初始化过程中生成的<code>compiler</code> 对象的引用，从而可以在回调函数中访问到 <code>compiler</code> 对象。</p>
<p>SplitChunksPlugin逻辑都在 SplitChunksPlugin.js 中：</p>
<p>从源码中可以看到两个重要的对象<code>compiler</code>和<code>compilation</code>，这两个对象是连接plugin和webpack的重要桥梁。<a href="https://link.juejin.cn/?target=https%3A%2F%2Fv4.webpack.js.org%2Fapi%2Fcompilation-hooks%2F%23unseal" target="_blank" rel="nofollow noopener noreferrer" title="https://v4.webpack.js.org/api/compilation-hooks/#unseal" ref="nofollow noopener noreferrer">官方API</a></p>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-function"><span class="hljs-title">apply</span>(<span class="hljs-params">compiler</span>)</span> &#123; 
    <span class="hljs-comment">//Compiler 对象包含了 Webpack 环境的所有配置信息，包含options、loaders、plugins等信息。这个对象在 Webpack 启动时被实例化，它是全局唯一的，可以简单地将它理解为 Webpack 实例。 </span>
    compiler.hooks.thisCompilation.tap(<span class="hljs-string">"SplitChunksPlugin"</span>, <span class="hljs-function"><span class="hljs-params">compilation</span> =></span> &#123; 
    <span class="hljs-comment">//Compilation 对象包含了当前的模块资源、编译生成资源、变化的文件等。当 Webpack 以开发模式运行时，每当检测到一个文件变化，一次新的 Compilation 将被创建。Compilation 对象也提供了很多事件回调供插件做扩展。通过 Compilation 也能读取到 Compiler 对象。 </span>
      <span class="hljs-keyword">let</span> alreadyOptimized = <span class="hljs-literal">false</span>; 
      <span class="hljs-comment">//当编译开始接受新模块时触发 </span>
      compilation.hooks.unseal.tap(<span class="hljs-string">"SplitChunksPlugin"</span>, <span class="hljs-function">() =></span> &#123; 
        alreadyOptimized = <span class="hljs-literal">false</span>; 
      &#125;); 
      <span class="hljs-comment">//在块优化阶段的开始时调用。插件可以利用此钩子来执行块优化。 </span>
      compilation.hooks.optimizeChunksAdvanced.tap( 
        <span class="hljs-string">"SplitChunksPlugin"</span>, 
        <span class="hljs-function"><span class="hljs-params">chunks</span> =></span> &#123; 
            <span class="hljs-comment">//核心代码 </span>
        &#125; 
      ); 
    &#125;); 
  &#125; 
<span class="copy-code-btn">复制代码</span></code></pre>
<p>在编译过程中，SplitChunksPlugin监听了<code>optimizeChunksAdvanced</code>钩子；在块优化阶段的开始时，触发 <code>optimizeChunksAdvanced</code> 事件并传入 <code>chunks</code>，开始代码分割优化过程，所有优化都在 <code>optimizeChunksAdvanced</code> 事件的回调函数中完成。</p>
<h2 data-id="heading-9">分块策略执行步骤</h2>
<p>回调事件注册好后，接下来是核心的分块策略执行流程，这一块的代码较多，因此根据每块代码的作用，将执行过程分为三步：1、优化前准备阶段；2、模块分组阶段；3、依次检查阶段。</p>
<h3 data-id="heading-10">优化前准备阶段</h3>
<p>在进行块优化前，首先要定义一些必要的方法和数据结构，在优化过程的每个阶段中都可能使用到这些方法和数据结构，具体流程如图：</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/558f68db86874da0ae5111255e0a7f5f~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>接下来看具体代码，着重是流程图中红色部分：</p>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-comment">// 给每个选定的块一个索引（从块中创建字符串）index从1开始递增 </span>
<span class="hljs-keyword">const</span> indexMap = <span class="hljs-keyword">new</span> <span class="hljs-built_in">Map</span>(); 
<span class="hljs-keyword">let</span> index = <span class="hljs-number">1</span>; 
<span class="hljs-keyword">for</span> (<span class="hljs-keyword">const</span> chunk <span class="hljs-keyword">of</span> chunks) &#123; 
    indexMap.set(chunk, index++); 
&#125; 
 
<span class="hljs-comment">// 获取chunks的唯一key，通过上一步的index索引拼接而成，索引数组按从小到大排序。compareNumbers = (a, b) => a - b; </span>
<span class="hljs-keyword">const</span> getKey = <span class="hljs-function"><span class="hljs-params">chunks</span> =></span> &#123; 
    <span class="hljs-keyword">return</span> <span class="hljs-built_in">Array</span>.from(chunks, <span class="hljs-function"><span class="hljs-params">c</span> =></span> indexMap.get(c)) 
      .sort(compareNumbers) 
      .join(); 
&#125;; 
 
<span class="hljs-comment">/** 
* 块优化的核心就是提取公共的module。所以要为包含某一module的chunks生成一个key值 
* 每个module都能找到包含该module的chunks集合（module.chunksIterable），根据chunks集合就可以生成有chunk索引拼接而成的key 
* 这样我们就知道每个module在哪些chunk中重复了，这对优化起了关键作用。 
* 这里将该key值和这些chunks建立映射关系，存在chunkSetsInGraph中，便于之后通过key值取出这些chunks集合，进行优化。 
*/</span> 
<span class="hljs-keyword">const</span> chunkSetsInGraph = <span class="hljs-keyword">new</span> <span class="hljs-built_in">Map</span>(); 
<span class="hljs-keyword">for</span> (<span class="hljs-keyword">const</span> <span class="hljs-built_in">module</span> <span class="hljs-keyword">of</span> compilation.modules) &#123; 
    <span class="hljs-keyword">const</span> chunksKey = getKey(<span class="hljs-built_in">module</span>.chunksIterable); 
    <span class="hljs-keyword">if</span> (!chunkSetsInGraph.has(chunksKey)) &#123; 
      chunkSetsInGraph.set(chunksKey, <span class="hljs-keyword">new</span> <span class="hljs-built_in">Set</span>(<span class="hljs-built_in">module</span>.chunksIterable)); 
    &#125; 
&#125; 
 
 
<span class="hljs-comment">/**  
* 在上一步的代码中，我们知道了每个module在哪些chunks中重复，并存在了chunkSetsInGraph中。这一步统计每个module重复的次数，并将重复次数存在chunkSetsByCount中。  
* 这一步是为了匹配minChunks属性，可以根据minChunks（module的最小重复次数）直接找到对应的chunksSet的集合，  
* 不符合minChunks的chunks集合会直接排除在优化之外，即该module不会被提取。  
* 注意，一个module对应一个chunksSet，一个count对应多个chunksSet，也就对应多个module */</span> 
<span class="hljs-keyword">const</span> chunkSetsByCount = <span class="hljs-keyword">new</span> <span class="hljs-built_in">Map</span>(); 
<span class="hljs-keyword">for</span> (<span class="hljs-keyword">const</span> chunksSet <span class="hljs-keyword">of</span> chunkSetsInGraph.values()) &#123; 
<span class="hljs-comment">// 遍历chunkSetsInGraph，统计每个chunks集合的chunk数量，即每个module的重复次数，建立数量和chunks集合的映射 </span>
    <span class="hljs-keyword">const</span> count = chunksSet.size; 
    <span class="hljs-keyword">let</span> array = chunkSetsByCount.get(count); 
    <span class="hljs-keyword">if</span> (array === <span class="hljs-literal">undefined</span>) &#123; 
      array = []; 
      chunkSetsByCount.set(count, array); 
    &#125; 
    array.push(chunksSet); 
&#125; 
 
<span class="hljs-keyword">const</span> combinationsCache = <span class="hljs-keyword">new</span> <span class="hljs-built_in">Map</span>(); <span class="hljs-comment">// Map<string, Set<Chunk>[]> </span>
<span class="hljs-comment">// 获得可能满足minChunks条件chunks集合，用于后续和minChunks条件比对 </span>
<span class="hljs-keyword">const</span> getCombinations = <span class="hljs-function"><span class="hljs-params">key</span> =></span> &#123; 
    <span class="hljs-comment">// 首先通过传入的key拿到chunks集合 </span>
    <span class="hljs-keyword">const</span> chunksSet = chunkSetsInGraph.get(key); 
    <span class="hljs-keyword">var</span> array = [chunksSet]; 
    <span class="hljs-keyword">if</span> (chunksSet.size > <span class="hljs-number">1</span>) &#123; 
      <span class="hljs-keyword">for</span> (<span class="hljs-keyword">const</span> [count, setArray] <span class="hljs-keyword">of</span> chunkSetsByCount) &#123; 
        <span class="hljs-comment">//遍历chunkSetsByCount，当chunk集合小于传入key对应的chunk集合时，进入是否时子集的判断。如果是子集则和通过key拿到的集合存在一个数组中，最后返回 </span>
        <span class="hljs-keyword">if</span> (count < chunksSet.size) &#123; 
          <span class="hljs-keyword">for</span> (<span class="hljs-keyword">const</span> set <span class="hljs-keyword">of</span> setArray) &#123; 
            <span class="hljs-keyword">if</span> (isSubset(chunksSet, set)) &#123; 
              array.push(set); 
            &#125; 
          &#125; 
        &#125; 
      &#125; 
    &#125; 
    <span class="hljs-keyword">return</span> array; 
&#125;; 
<span class="hljs-comment">// 判断两个chunk集合，后者是否时前者的子集 </span>
<span class="hljs-keyword">const</span> isSubset = <span class="hljs-function">(<span class="hljs-params">bigSet, smallSet</span>) =></span> &#123; 
  <span class="hljs-keyword">if</span> (bigSet.size < smallSet.size) <span class="hljs-keyword">return</span> <span class="hljs-literal">false</span>; 
  <span class="hljs-keyword">for</span> (<span class="hljs-keyword">const</span> item <span class="hljs-keyword">of</span> smallSet) &#123; 
    <span class="hljs-keyword">if</span> (!bigSet.has(item)) <span class="hljs-keyword">return</span> <span class="hljs-literal">false</span>; 
  &#125; 
  <span class="hljs-keyword">return</span> <span class="hljs-literal">true</span>; 
&#125;; 
 
<span class="hljs-keyword">const</span> selectedChunksCacheByChunksSet = <span class="hljs-keyword">new</span> <span class="hljs-built_in">WeakMap</span>(); 
<span class="hljs-comment">/** 
* 传入chunks和chunks过滤方法，最终返回满足条件的chunk集合和集合key 
* 从性能方面考虑，会将通过过滤条件产生的结果与过滤条件、传入的chunk集合一起缓存起来 
**/</span> 
<span class="hljs-keyword">const</span> getSelectedChunks = <span class="hljs-function">(<span class="hljs-params">chunks, chunkFilter</span>) =></span> &#123; 
    <span class="hljs-comment">// 通过传入的chunks集合，判断是否缓存过，如果没有缓存过则创建缓存 </span>
    <span class="hljs-keyword">let</span> entry = selectedChunksCacheByChunksSet.get(chunks); 
    <span class="hljs-keyword">if</span> (entry === <span class="hljs-literal">undefined</span>) &#123; 
      entry = <span class="hljs-keyword">new</span> <span class="hljs-built_in">WeakMap</span>(); 
      selectedChunksCacheByChunksSet.set(chunks, entry); 
    &#125; 
    <span class="hljs-comment">/** <span class="hljs-doctag">@type <span class="hljs-type">&#123;SelectedChunksResult&#125;</span> </span>*/</span> 
    <span class="hljs-comment">// 通过缓存条件判断是否有筛选结果，有则直接返回，没有则生成选择结果并缓存 </span>
    <span class="hljs-keyword">let</span> entry2 = entry.get(chunkFilter); 
    <span class="hljs-keyword">if</span> (entry2 === <span class="hljs-literal">undefined</span>) &#123; 
      <span class="hljs-comment">/** <span class="hljs-doctag">@type <span class="hljs-type">&#123;Chunk[]&#125;</span> </span>*/</span> 
      <span class="hljs-keyword">const</span> selectedChunks = []; 
      <span class="hljs-keyword">for</span> (<span class="hljs-keyword">const</span> chunk <span class="hljs-keyword">of</span> chunks) &#123; 
        <span class="hljs-keyword">if</span> (chunkFilter(chunk)) selectedChunks.push(chunk); 
      &#125; 
      entry2 = &#123; 
        <span class="hljs-attr">chunks</span>: selectedChunks, 
        <span class="hljs-attr">key</span>: getKey(selectedChunks) 
      &#125;; 
      entry.set(chunkFilter, entry2); 
    &#125; 
    <span class="hljs-keyword">return</span> entry2; 
&#125;; 
 
<span class="hljs-keyword">const</span> chunksInfoMap = <span class="hljs-keyword">new</span> <span class="hljs-built_in">Map</span>(); 
<span class="hljs-comment">// 关键的Map结构，每一项对应一个分割出来的缓存组，键名为根据name属性生成的key值，键值为该key值对应的modules、chunks和cacheGroup信息对象 </span>
<span class="hljs-keyword">const</span> addModuleToChunksInfoMap = <span class="hljs-function">(<span class="hljs-params"> 
    cacheGroup, 
    cacheGroupIndex, 
    selectedChunks, 
    selectedChunksKey, 
    <span class="hljs-built_in">module</span> 
  </span>) =></span> &#123; 
    <span class="hljs-comment">// Break if minimum number of chunks is not reached </span>
    <span class="hljs-comment">// 如果选择的chunk集合小于设置的**minChunks，直接返回** </span>
    <span class="hljs-keyword">if</span> (selectedChunks.length < cacheGroup.minChunks) <span class="hljs-keyword">return</span>; 
    <span class="hljs-comment">// 确定拆分块的名称 </span>
    <span class="hljs-keyword">const</span> name = cacheGroup.getName( 
      <span class="hljs-built_in">module</span>, 
      selectedChunks, 
      cacheGroup.key 
    ); 
     
    <span class="hljs-comment">// 创建map的key，如果有传入名称，就会以名称作为key，否则用chunk集合生成的key做key </span>
    <span class="hljs-keyword">const</span> key = 
      cacheGroup.key + 
      (name ? <span class="hljs-string">` name:<span class="hljs-subst">$&#123;name&#125;</span>`</span> : <span class="hljs-string">` chunks:<span class="hljs-subst">$&#123;selectedChunksKey&#125;</span>`</span>); 
    <span class="hljs-comment">// 将模块添加到map中 </span>
    <span class="hljs-keyword">let</span> info = chunksInfoMap.get(key); 
    <span class="hljs-keyword">if</span> (info === <span class="hljs-literal">undefined</span>) &#123; 
      chunksInfoMap.set( 
        key, 
        (info = &#123; 
          <span class="hljs-attr">modules</span>: <span class="hljs-keyword">new</span> SortableSet(<span class="hljs-literal">undefined</span>, sortByIdentifier), 
          cacheGroup, 
          cacheGroupIndex, 
          name, 
          <span class="hljs-attr">size</span>: <span class="hljs-number">0</span>, 
          <span class="hljs-attr">chunks</span>: <span class="hljs-keyword">new</span> <span class="hljs-built_in">Set</span>(), 
          <span class="hljs-attr">reuseableChunks</span>: <span class="hljs-keyword">new</span> <span class="hljs-built_in">Set</span>(), 
          <span class="hljs-attr">chunksKeys</span>: <span class="hljs-keyword">new</span> <span class="hljs-built_in">Set</span>() 
        &#125;) 
      ); 
    &#125; 
    <span class="hljs-comment">// info.modules是一个set，通过oldSize和添加module之后大size比较，确定要不要更新info的size </span>
    <span class="hljs-keyword">const</span> oldSize = info.modules.size; 
    info.modules.add(<span class="hljs-built_in">module</span>); 
    <span class="hljs-keyword">if</span> (info.modules.size !== oldSize) &#123; 
      info.size += <span class="hljs-built_in">module</span>.size(); 
    &#125; 
    <span class="hljs-comment">// 同上，info.chunks是一个set,根据chunksKeys的size判断要不要加选中的chunk集合加入info.chunks </span>
    <span class="hljs-keyword">const</span> oldChunksKeysSize = info.chunksKeys.size; 
    info.chunksKeys.add(selectedChunksKey); 
    <span class="hljs-keyword">if</span> (oldChunksKeysSize !== info.chunksKeys.size) &#123; 
      <span class="hljs-keyword">for</span> (<span class="hljs-keyword">const</span> chunk <span class="hljs-keyword">of</span> selectedChunks) &#123; 
        info.chunks.add(chunk); 
      &#125; 
    &#125; 
  &#125;; 
<span class="copy-code-btn">复制代码</span></code></pre>
<p>前面这一块代码都是优化前的准备阶段，这个阶段最关键的点就是<code>chunksInfoMap</code>和<code>addModuleToChunksInfoMap</code>。</p>
<ul>
<li><code>chunksInfoMap</code> 存储着代码分割信息，每一项都是一个缓存组，对应于最终要分割出哪些额外代码块，会不断迭代，最终将代码分割结果加入 <code>results</code> 中，而 <code>results</code> 最终会生成我们见到的打包文件。这些缓存组还附带一些额外信息，比如 cacheGroup，就是我们配置的 cacheGroup 代码分割规则，用于后续校验；再比如 sizes，记录了缓存组中模块的总体积，用于之后判断是否符合我们配置的 minSize 条件。</li>
<li><code>addModuleToChunksInfoMap</code> 这个方法就是向 <code>chunksInfoMap</code> 中添加新的代码分割信息（选中的chunk集合），在方法中会通过key去更新缓存组或者添加新的缓存组。</li>
</ul>
<h3 data-id="heading-11">模块分组阶段</h3>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/43e30d4f9c54422ab2b55638586a8c58~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>准备工作做好之后，开始核心的分组优化工作，遍历所有的models，将符合条件的module 通过 <code>addModuleToChunksInfoMap</code> 方法存到 <code>chunksInfoMap</code> 中。该代码在SplitChunksPlugin.js的565-670行：</p>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-comment">// Walk through all modules </span>
<span class="hljs-comment">// 遍历所有modules </span>
<span class="hljs-keyword">for</span> (<span class="hljs-keyword">const</span> <span class="hljs-built_in">module</span> <span class="hljs-keyword">of</span> compilation.modules) &#123; 
    <span class="hljs-comment">// Get cache group </span>
    <span class="hljs-comment">// 通过getCacheGroups得到module从属的cacheGroup，一个module可能符合多个cacheGroup的条件 </span>
    <span class="hljs-keyword">let</span> cacheGroups = <span class="hljs-built_in">this</span>.options.getCacheGroups(<span class="hljs-built_in">module</span>); 
    <span class="hljs-keyword">if</span> (!<span class="hljs-built_in">Array</span>.isArray(cacheGroups) || cacheGroups.length === <span class="hljs-number">0</span>) &#123; 
      <span class="hljs-keyword">continue</span>; 
    &#125; 
     
    <span class="hljs-comment">// Prepare some values </span>
    <span class="hljs-comment">// 包含同一个module的chunk会对应唯一的key值，通过前期准备阶段的各种方法，获取唯一的key，通过chunksKey拿到 包含同一个module的chunk的全部子集，并存入combinationsCache做缓存 </span>
    <span class="hljs-keyword">const</span> chunksKey = getKey(<span class="hljs-built_in">module</span>.chunksIterable); 
    <span class="hljs-keyword">let</span> combs = combinationsCache.get(chunksKey); 
    <span class="hljs-keyword">if</span> (combs === <span class="hljs-literal">undefined</span>) &#123; 
      combs = getCombinations(chunksKey); 
      combinationsCache.set(chunksKey, combs); 
    &#125; 
     
    <span class="hljs-keyword">let</span> cacheGroupIndex = <span class="hljs-number">0</span>; 
    <span class="hljs-keyword">for</span> (<span class="hljs-keyword">const</span> cacheGroupSource <span class="hljs-keyword">of</span> cacheGroups) &#123; 
      <span class="hljs-comment">// 遍历将的cacheGroup配置都取出来，如果值不存在，则会从splitChunks全局配置继承 </span>
      <span class="hljs-keyword">const</span> minSize = 
        cacheGroupSource.minSize !== <span class="hljs-literal">undefined</span> 
          ? cacheGroupSource.minSize 
          : cacheGroupSource.enforce 
            ? <span class="hljs-number">0</span> 
            : <span class="hljs-built_in">this</span>.options.minSize; 
      <span class="hljs-keyword">const</span> enforceSizeThreshold = 
        cacheGroupSource.enforceSizeThreshold !== <span class="hljs-literal">undefined</span> 
          ? cacheGroupSource.enforceSizeThreshold 
          : cacheGroupSource.enforce 
            ? <span class="hljs-number">0</span> 
            : <span class="hljs-built_in">this</span>.options.enforceSizeThreshold; 
      <span class="hljs-comment">// 按照配置创建cacheGroup    </span>
      <span class="hljs-keyword">const</span> cacheGroup = &#123; 
        <span class="hljs-attr">key</span>: cacheGroupSource.key, 
        <span class="hljs-attr">priority</span>: cacheGroupSource.priority || <span class="hljs-number">0</span>, 
        <span class="hljs-attr">chunksFilter</span>: 
          cacheGroupSource.chunksFilter || <span class="hljs-built_in">this</span>.options.chunksFilter, 
        minSize, 
        <span class="hljs-attr">minSizeForMaxSize</span>: 
          cacheGroupSource.minSize !== <span class="hljs-literal">undefined</span> 
            ? cacheGroupSource.minSize 
            : <span class="hljs-built_in">this</span>.options.minSize, 
        enforceSizeThreshold, 
        <span class="hljs-attr">maxSize</span>: 
          cacheGroupSource.maxSize !== <span class="hljs-literal">undefined</span> 
            ? cacheGroupSource.maxSize 
            : cacheGroupSource.enforce 
              ? <span class="hljs-number">0</span> 
              : <span class="hljs-built_in">this</span>.options.maxSize, 
        <span class="hljs-attr">minChunks</span>: 
          cacheGroupSource.minChunks !== <span class="hljs-literal">undefined</span> 
            ? cacheGroupSource.minChunks 
            : cacheGroupSource.enforce 
              ? <span class="hljs-number">1</span> 
              : <span class="hljs-built_in">this</span>.options.minChunks, 
        <span class="hljs-attr">maxAsyncRequests</span>: 
          cacheGroupSource.maxAsyncRequests !== <span class="hljs-literal">undefined</span> 
            ? cacheGroupSource.maxAsyncRequests 
            : cacheGroupSource.enforce 
              ? <span class="hljs-literal">Infinity</span> 
              : <span class="hljs-built_in">this</span>.options.maxAsyncRequests, 
        <span class="hljs-attr">maxInitialRequests</span>: 
          cacheGroupSource.maxInitialRequests !== <span class="hljs-literal">undefined</span> 
            ? cacheGroupSource.maxInitialRequests 
            : cacheGroupSource.enforce 
              ? <span class="hljs-literal">Infinity</span> 
              : <span class="hljs-built_in">this</span>.options.maxInitialRequests, 
        <span class="hljs-attr">getName</span>: 
          cacheGroupSource.getName !== <span class="hljs-literal">undefined</span> 
            ? cacheGroupSource.getName 
            : <span class="hljs-built_in">this</span>.options.getName, 
        <span class="hljs-attr">filename</span>: 
          cacheGroupSource.filename !== <span class="hljs-literal">undefined</span> 
            ? cacheGroupSource.filename 
            : <span class="hljs-built_in">this</span>.options.filename, 
        <span class="hljs-attr">automaticNameDelimiter</span>: 
          cacheGroupSource.automaticNameDelimiter !== <span class="hljs-literal">undefined</span> 
            ? cacheGroupSource.automaticNameDelimiter 
            : <span class="hljs-built_in">this</span>.options.automaticNameDelimiter, 
        <span class="hljs-attr">reuseExistingChunk</span>: cacheGroupSource.reuseExistingChunk, 
        <span class="hljs-attr">_validateSize</span>: minSize > <span class="hljs-number">0</span>, 
        <span class="hljs-attr">_conditionalEnforce</span>: enforceSizeThreshold > <span class="hljs-number">0</span> 
      &#125;; 
      <span class="hljs-comment">// For all combination of chunk selection </span>
      <span class="hljs-comment">// 遍历选择chunk的所有组合 </span>
      <span class="hljs-keyword">for</span> (<span class="hljs-keyword">const</span> chunkCombination <span class="hljs-keyword">of</span> combs) &#123; 
        <span class="hljs-comment">// Break if minimum number of chunks is not reached </span>
        <span class="hljs-comment">// 首先判断是否满足minChunks，如果不满足，就直接跳过，不建立这个缓存组，也就不会分割相应代码 </span>
        <span class="hljs-keyword">if</span> (chunkCombination.size < cacheGroup.minChunks) <span class="hljs-keyword">continue</span>; 
        <span class="hljs-comment">// Select chunks by configuration </span>
        <span class="hljs-comment">// 利用准备阶段的方法，从chunk集合中，选择出满足过滤条件的chunks，并解构为selectedChunks，selectedChunksKey </span>
        <span class="hljs-keyword">const</span> &#123; 
          <span class="hljs-attr">chunks</span>: selectedChunks, 
          <span class="hljs-attr">key</span>: selectedChunksKey 
        &#125; = getSelectedChunks( 
          chunkCombination, 
          cacheGroup.chunksFilter 
        ); 
        <span class="hljs-comment">// 利用准备阶段的addModuleToChunksInfoMap方法，将上一步产生的符合条件的selectedChunks、selectedChunksKey，结合modules、chunks、cacheGroupIndex和cacheGroup信息存到chunksInfoMap中，cacheGroupIndex每次都会+1 </span>
        addModuleToChunksInfoMap( 
          cacheGroup, 
          cacheGroupIndex, 
          selectedChunks, 
          selectedChunksKey, 
          <span class="hljs-built_in">module</span> 
        ); 
      &#125; 
      cacheGroupIndex++; 
    &#125; 
&#125; 
<span class="copy-code-btn">复制代码</span></code></pre>
<p>chunksFilter是<code>chunks</code>属性的过滤，即判断chunk是满足<code>all</code>、<code>async</code>还是<code>initial</code>。因此在分组阶段，除了将 cacheGroup 的配置全部取出，还检查配置中的 <code>minChunks</code> 和 <code>chunks</code> 规则，满足条件的分组才会被创建出来。其他各种需要校验的配置会在下一个阶段做处理。</p>
<h3 data-id="heading-12">依次检查阶段</h3>
<p>在上一个阶段，我们将模块按照按照一定条件分组，并存入了<code>chunksInfoMap</code>中。本阶段就是优化的最后一步，判断<code>chunksInfoMap</code>的每一个缓存组是不是符合用户的<code>cacheGroup</code>配置，不满足就剔除。还是流程图出发：</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/a0b99eafedd54f2fbceb2779a29ec38f~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-comment">// Filter items were size < minSize </span>
<span class="hljs-comment">// 第一步，去除chunksInfoMap不满足minSize的缓存组（chunsInfoItem） </span>
<span class="hljs-keyword">for</span> (<span class="hljs-keyword">const</span> pair <span class="hljs-keyword">of</span> chunksInfoMap) &#123; 
    <span class="hljs-keyword">const</span> info = pair[<span class="hljs-number">1</span>]; 
    <span class="hljs-keyword">if</span> ( 
      info.cacheGroup._validateSize && 
      info.size < info.cacheGroup.minSize 
    ) &#123; 
      chunksInfoMap.delete(pair[<span class="hljs-number">0</span>]); 
    &#125; 
&#125; 
 
<span class="hljs-keyword">const</span> maxSizeQueueMap = <span class="hljs-keyword">new</span> <span class="hljs-built_in">Map</span>(); 
<span class="hljs-comment">// 第二步，while 循环，直到chunksInfoMap的缓存组全部分配好 </span>
<span class="hljs-keyword">while</span> (chunksInfoMap.size > <span class="hljs-number">0</span>) &#123; 
    <span class="hljs-comment">// Find best matching entry </span>
    <span class="hljs-comment">// 寻找最匹配的cacheGroup分组信息，优先进行分割，优先产生打包结果 </span>
    <span class="hljs-keyword">let</span> bestEntryKey; 
    <span class="hljs-keyword">let</span> bestEntry; 
    <span class="hljs-keyword">for</span> (<span class="hljs-keyword">const</span> pair <span class="hljs-keyword">of</span> chunksInfoMap) &#123; 
      <span class="hljs-keyword">const</span> key = pair[<span class="hljs-number">0</span>]; 
      <span class="hljs-keyword">const</span> info = pair[<span class="hljs-number">1</span>]; 
      <span class="hljs-keyword">if</span> (bestEntry === <span class="hljs-literal">undefined</span>) &#123; 
        bestEntry = info; 
        bestEntryKey = key; 
      &#125; <span class="hljs-keyword">else</span> <span class="hljs-keyword">if</span> (compareEntries(bestEntry, info) < <span class="hljs-number">0</span>) &#123; 
        <span class="hljs-comment">// 比较那个cacheGroup更需要有限分割 </span>
        bestEntry = info; 
        bestEntryKey = key; 
      &#125; 
    &#125; 
     
    <span class="hljs-keyword">const</span> item = bestEntry; 
    chunksInfoMap.delete(bestEntryKey); 
     
    <span class="hljs-keyword">let</span> chunkName = item.name; 
    <span class="hljs-comment">// Variable for the new chunk (lazy created) </span>
    <span class="hljs-comment">// 由缓存组生成的新chunk </span>
    <span class="hljs-comment">/** <span class="hljs-doctag">@type <span class="hljs-type">&#123;Chunk&#125;</span> </span>*/</span> 
    <span class="hljs-keyword">let</span> newChunk; 
    <span class="hljs-comment">// When no chunk name, check if we can reuse a chunk instead of creating a new one </span>
    <span class="hljs-keyword">let</span> isReused = <span class="hljs-literal">false</span>; 
    <span class="hljs-comment">// 从这里开始真正的分割代码 </span>
    <span class="hljs-comment">// 如果没有设定name，则寻找是否能复用已有的chunk </span>
    <span class="hljs-keyword">if</span> (item.cacheGroup.reuseExistingChunk) &#123; 
      <span class="hljs-attr">outer</span>: <span class="hljs-keyword">for</span> (<span class="hljs-keyword">const</span> chunk <span class="hljs-keyword">of</span> item.chunks) &#123; 
        <span class="hljs-keyword">if</span> (chunk.getNumberOfModules() !== item.modules.size) <span class="hljs-keyword">continue</span>; 
        <span class="hljs-keyword">if</span> (chunk.hasEntryModule()) <span class="hljs-keyword">continue</span>; 
        <span class="hljs-keyword">for</span> (<span class="hljs-keyword">const</span> <span class="hljs-built_in">module</span> <span class="hljs-keyword">of</span> item.modules) &#123; 
          <span class="hljs-comment">// 结束最外层for循环 </span>
          <span class="hljs-keyword">if</span> (!chunk.containsModule(<span class="hljs-built_in">module</span>)) <span class="hljs-keyword">continue</span> outer; 
        &#125; 
        <span class="hljs-keyword">if</span> (!newChunk || !newChunk.name) &#123; 
          newChunk = chunk; 
        &#125; <span class="hljs-keyword">else</span> <span class="hljs-keyword">if</span> ( 
          chunk.name && 
          chunk.name.length < newChunk.name.length 
        ) &#123; 
          newChunk = chunk; 
        &#125; <span class="hljs-keyword">else</span> <span class="hljs-keyword">if</span> ( 
          chunk.name && 
          chunk.name.length === newChunk.name.length && 
          chunk.name < newChunk.name 
        ) &#123; 
          newChunk = chunk; 
        &#125; 
        chunkName = <span class="hljs-literal">undefined</span>; 
        isReused = <span class="hljs-literal">true</span>; 
      &#125; 
    &#125; 
     
    <span class="hljs-comment">// 过滤chunks，过滤chunk自身 </span>
    <span class="hljs-keyword">const</span> selectedChunks = <span class="hljs-built_in">Array</span>.from(item.chunks).filter(<span class="hljs-function"><span class="hljs-params">chunk</span> =></span> &#123; 
      <span class="hljs-keyword">return</span> ( 
        (!chunkName || chunk.name !== chunkName) && chunk !== newChunk 
      ); 
    &#125;); 
     
    <span class="hljs-comment">// 获取enforced </span>
    <span class="hljs-keyword">const</span> enforced = 
      item.cacheGroup._conditionalEnforce && 
      item.size >= item.cacheGroup.enforceSizeThreshold; 
     
    <span class="hljs-comment">// selectedChunks长度为0直接跳过 </span>
    <span class="hljs-keyword">if</span> (selectedChunks.length === <span class="hljs-number">0</span>) <span class="hljs-keyword">continue</span>; 
     
    <span class="hljs-comment">// chunks 去重 </span>
    <span class="hljs-keyword">const</span> usedChunks = <span class="hljs-keyword">new</span> <span class="hljs-built_in">Set</span>(selectedChunks); 
     
    <span class="hljs-comment">// Check if maxRequests condition can be fulfilled </span>
    <span class="hljs-comment">// 检测缓存组中的代码块是否满足maxInitialRequests和maxAsyncRequests条件，如果它们都是无穷大，就跳过检测 </span>
    <span class="hljs-keyword">if</span> ( 
      !enforced && 
      (<span class="hljs-built_in">Number</span>.isFinite(item.cacheGroup.maxInitialRequests) || 
        <span class="hljs-built_in">Number</span>.isFinite(item.cacheGroup.maxAsyncRequests)) 
    ) &#123; 
      <span class="hljs-keyword">for</span> (<span class="hljs-keyword">const</span> chunk <span class="hljs-keyword">of</span> usedChunks) &#123; 
        <span class="hljs-comment">// 如果chunk是初始代码块，只需判断maxInitialRequests条件是否满足；  </span>
        <span class="hljs-comment">// 如果chunk不是初始代码块，只需判断maxAsyncRequests条件是否满足；  </span>
        <span class="hljs-comment">// 如果chunk可以作为初始代码块，就取两者最小值；不过目前这个分支条件是走不到的，因为目前版本代码块只有初始（作为入口）或者非初始（懒加载） </span>
        <span class="hljs-keyword">const</span> maxRequests = chunk.isOnlyInitial() 
          ? item.cacheGroup.maxInitialRequests 
          : chunk.canBeInitial() 
            ? <span class="hljs-built_in">Math</span>.min( 
              item.cacheGroup.maxInitialRequests, 
              item.cacheGroup.maxAsyncRequests 
            ) 
            : item.cacheGroup.maxAsyncRequests; 
        <span class="hljs-comment">// 如果不满足最大请求数的条件，则从validChunks中去除 </span>
        <span class="hljs-keyword">if</span> ( 
          <span class="hljs-built_in">isFinite</span>(maxRequests) && 
          getRequests(chunk) >= maxRequests 
        ) &#123; 
          usedChunks.delete(chunk); 
        &#125; 
      &#125; 
    &#125; 
     
    <span class="hljs-attr">outer</span>: <span class="hljs-keyword">for</span> (<span class="hljs-keyword">const</span> chunk <span class="hljs-keyword">of</span> usedChunks) &#123; 
      <span class="hljs-keyword">for</span> (<span class="hljs-keyword">const</span> <span class="hljs-built_in">module</span> <span class="hljs-keyword">of</span> item.modules) &#123; 
       <span class="hljs-comment">//结束外层for循环 </span>
        <span class="hljs-keyword">if</span> (chunk.containsModule(<span class="hljs-built_in">module</span>)) <span class="hljs-keyword">continue</span> outer; 
      &#125; 
      <span class="hljs-comment">// 包含item.modules中任意module的chunk要剔除 </span>
      usedChunks.delete(chunk); 
    &#125; 
     
    <span class="hljs-comment">// Were some (invalid) chunks removed from usedChunks? </span>
    <span class="hljs-comment">// => readd all modules to the queue, as things could have been changed </span>
    <span class="hljs-comment">// 将去除不符合条件的chunk之后的新缓存组加入chunksInfoMap，不断迭代，更新代码分割结果 </span>
    <span class="hljs-keyword">if</span> (usedChunks.size < selectedChunks.length) &#123; 
      <span class="hljs-comment">// 剩余chunk大于minChunks，则加入chunksInfoMap，迭代分割 </span>
      <span class="hljs-keyword">if</span> (usedChunks.size >= item.cacheGroup.minChunks) &#123; 
        <span class="hljs-keyword">const</span> chunksArr = <span class="hljs-built_in">Array</span>.from(usedChunks); 
        <span class="hljs-keyword">for</span> (<span class="hljs-keyword">const</span> <span class="hljs-built_in">module</span> <span class="hljs-keyword">of</span> item.modules) &#123; 
          addModuleToChunksInfoMap( 
            item.cacheGroup, 
            item.cacheGroupIndex, 
            chunksArr, 
            getKey(usedChunks), 
            <span class="hljs-built_in">module</span> 
          ); 
        &#125; 
      &#125; 
      <span class="hljs-keyword">continue</span>; 
    &#125; 
     
    <span class="hljs-comment">// Create the new chunk if not reusing one </span>
    <span class="hljs-comment">// 如果不重用一个，则compilation创建新的块 </span>
    <span class="hljs-keyword">if</span> (!isReused) &#123; 
      newChunk = compilation.addChunk(chunkName); 
    &#125; 
    <span class="hljs-comment">// Walk through all chunks </span>
    <span class="hljs-keyword">for</span> (<span class="hljs-keyword">const</span> chunk <span class="hljs-keyword">of</span> usedChunks) &#123; 
      <span class="hljs-comment">// Add graph connections for splitted chunk </span>
      <span class="hljs-comment">// 创建了新代码块还不够，还需要建立chunk和chunkGroup之间的关系 </span>
      chunk.split(newChunk); 
    &#125; 
     
    <span class="hljs-comment">// Add a note to the chunk </span>
    <span class="hljs-comment">// 提供输出信息：根据是否复用输出不同信息 </span>
    newChunk.chunkReason = isReused 
      ? <span class="hljs-string">"reused as split chunk"</span> 
      : <span class="hljs-string">"split chunk"</span>; 
    <span class="hljs-comment">// 提供输出信息便于我们debug </span>
    <span class="hljs-keyword">if</span> (item.cacheGroup.key) &#123; 
      newChunk.chunkReason += <span class="hljs-string">` (cache group: <span class="hljs-subst">$&#123;item.cacheGroup.key&#125;</span>)`</span>; 
    &#125; 
    <span class="hljs-keyword">if</span> (chunkName) &#123; 
      <span class="hljs-built_in">console</span>.log(chunkName) 
      newChunk.chunkReason += <span class="hljs-string">` (name: <span class="hljs-subst">$&#123;chunkName&#125;</span>)`</span>; 
      <span class="hljs-comment">// If the chosen name is already an entry point we remove the entry point 如果所选名称已经是入口点，我们将删除该入口点 </span>
      <span class="hljs-keyword">const</span> entrypoint = compilation.entrypoints.get(chunkName); 
      <span class="hljs-keyword">if</span> (entrypoint) &#123; 
        compilation.entrypoints.delete(chunkName); 
        entrypoint.remove(); 
        newChunk.entryModule = <span class="hljs-literal">undefined</span>; 
      &#125; 
    &#125; 
    <span class="hljs-keyword">if</span> (item.cacheGroup.filename) &#123; 
      <span class="hljs-keyword">if</span> (!newChunk.isOnlyInitial()) &#123; 
        <span class="hljs-keyword">throw</span> <span class="hljs-keyword">new</span> <span class="hljs-built_in">Error</span>( 
          <span class="hljs-string">"SplitChunksPlugin: You are trying to set a filename for a chunk which is (also) loaded on demand. "</span> + 
          <span class="hljs-string">"The runtime can only handle loading of chunks which match the chunkFilename schema. "</span> + 
          <span class="hljs-string">"Using a custom filename would fail at runtime. "</span> + 
          <span class="hljs-string">`(cache group: <span class="hljs-subst">$&#123;item.cacheGroup.key&#125;</span>)`</span> 
        ); 
      &#125; 
      newChunk.filenameTemplate = item.cacheGroup.filename; 
    &#125; 
    <span class="hljs-keyword">if</span> (!isReused) &#123; 
      <span class="hljs-comment">// Add all modules to the new chunk 将所有的modules添加到新chunk </span>
      <span class="hljs-keyword">for</span> (<span class="hljs-keyword">const</span> <span class="hljs-built_in">module</span> <span class="hljs-keyword">of</span> item.modules) &#123; 
        <span class="hljs-keyword">if</span> (<span class="hljs-keyword">typeof</span> <span class="hljs-built_in">module</span>.chunkCondition === <span class="hljs-string">"function"</span>) &#123; 
          <span class="hljs-comment">// 这个版本永远是true </span>
          <span class="hljs-keyword">if</span> (!<span class="hljs-built_in">module</span>.chunkCondition(newChunk)) <span class="hljs-keyword">continue</span>; 
        &#125; 
        <span class="hljs-comment">// Add module to new chunk </span>
        <span class="hljs-comment">// 建立module和新chunk的关系 关键代码，通过这里变更chunk图 </span>
        GraphHelpers.connectChunkAndModule(newChunk, <span class="hljs-built_in">module</span>); 
        <span class="hljs-comment">// Remove module from used chunks 从使用的chunk移除module </span>
        <span class="hljs-keyword">for</span> (<span class="hljs-keyword">const</span> chunk <span class="hljs-keyword">of</span> usedChunks) &#123; 
          chunk.removeModule(<span class="hljs-built_in">module</span>); 
          <span class="hljs-built_in">module</span>.rewriteChunkInReasons(chunk, [newChunk]); 
        &#125; 
      &#125; 
    &#125; <span class="hljs-keyword">else</span> &#123; 
      <span class="hljs-comment">// Remove all modules from used chunks </span>
      <span class="hljs-comment">// 如果是复用的，则从usedChunks中删除所有的module </span>
      <span class="hljs-keyword">for</span> (<span class="hljs-keyword">const</span> <span class="hljs-built_in">module</span> <span class="hljs-keyword">of</span> item.modules) &#123; 
        <span class="hljs-keyword">for</span> (<span class="hljs-keyword">const</span> chunk <span class="hljs-keyword">of</span> usedChunks) &#123; 
          chunk.removeModule(<span class="hljs-built_in">module</span>); 
          <span class="hljs-built_in">module</span>.rewriteChunkInReasons(chunk, [newChunk]); 
        &#125; 
      &#125; 
    &#125; 
     
    <span class="hljs-keyword">if</span> (item.cacheGroup.maxSize > <span class="hljs-number">0</span>) &#123; 
    <span class="hljs-comment">// 如果cacheGroup.maxSize > 0，则更新maxSizeQueueMap，更新newChunk的minSize，maxSize等 </span>
      <span class="hljs-keyword">const</span> oldMaxSizeSettings = maxSizeQueueMap.get(newChunk); 
      maxSizeQueueMap.set(newChunk, &#123; 
        <span class="hljs-attr">minSize</span>: <span class="hljs-built_in">Math</span>.max( 
          oldMaxSizeSettings ? oldMaxSizeSettings.minSize : <span class="hljs-number">0</span>, 
          item.cacheGroup.minSizeForMaxSize 
        ), 
        <span class="hljs-attr">maxSize</span>: <span class="hljs-built_in">Math</span>.min( 
          oldMaxSizeSettings ? oldMaxSizeSettings.maxSize : <span class="hljs-literal">Infinity</span>, 
          item.cacheGroup.maxSize 
        ), 
        <span class="hljs-attr">automaticNameDelimiter</span>: item.cacheGroup.automaticNameDelimiter, 
        <span class="hljs-attr">keys</span>: oldMaxSizeSettings 
          ? oldMaxSizeSettings.keys.concat(item.cacheGroup.key) 
          : [item.cacheGroup.key] 
      &#125;); 
    &#125; 
     
    <span class="hljs-comment">// remove all modules from other entries and update size </span>
    <span class="hljs-comment">// 从其他入口中删除所有模块并更新大小 </span>
    <span class="hljs-keyword">for</span> (<span class="hljs-keyword">const</span> [key, info] <span class="hljs-keyword">of</span> chunksInfoMap) &#123; 
      <span class="hljs-keyword">if</span> (isOverlap(info.chunks, usedChunks)) &#123; 
        <span class="hljs-comment">// 判断info的chunk是有有在usedChunks中 </span>
        <span class="hljs-comment">// update modules and total size </span>
        <span class="hljs-comment">// may remove it from the map when < minSize </span>
        <span class="hljs-comment">// </span>
        <span class="hljs-keyword">const</span> oldSize = info.modules.size; 
        <span class="hljs-keyword">for</span> (<span class="hljs-keyword">const</span> <span class="hljs-built_in">module</span> <span class="hljs-keyword">of</span> item.modules) &#123; 
          <span class="hljs-comment">// 将info.modules中的item.modules的module都删除 </span>
          info.modules.delete(<span class="hljs-built_in">module</span>); 
        &#125; 
        <span class="hljs-keyword">if</span> (info.modules.size !== oldSize) &#123; 
          <span class="hljs-keyword">if</span> (info.modules.size === <span class="hljs-number">0</span>) &#123; 
            chunksInfoMap.delete(key); 
            <span class="hljs-keyword">continue</span>; 
          &#125; 
          info.size = getModulesSize(info.modules); 
          <span class="hljs-keyword">if</span> ( 
            info.cacheGroup._validateSize && 
            info.size < info.cacheGroup.minSize 
          ) &#123; 
            chunksInfoMap.delete(key); 
          &#125; 
          <span class="hljs-keyword">if</span> (info.modules.size === <span class="hljs-number">0</span>) &#123; 
            chunksInfoMap.delete(key); 
          &#125; 
        &#125; 
      &#125; 
    &#125; 
&#125; 
compareEntries、isOverlap代码 
<span class="hljs-keyword">const</span> compareEntries = <span class="hljs-function">(<span class="hljs-params">a, b</span>) =></span> &#123; 
  <span class="hljs-comment">// 1. by priority 通过cacheGroup的priority比较 </span>
  <span class="hljs-keyword">const</span> diffPriority = a.cacheGroup.priority - b.cacheGroup.priority; 
  <span class="hljs-keyword">if</span> (diffPriority) <span class="hljs-keyword">return</span> diffPriority; 
  <span class="hljs-comment">// 2. by number of chunks，比较两个cacheGroyp的chunks的大小 </span>
  <span class="hljs-keyword">const</span> diffCount = a.chunks.size - b.chunks.size; 
  <span class="hljs-keyword">if</span> (diffCount) <span class="hljs-keyword">return</span> diffCount; 
  <span class="hljs-comment">// 3. by size reduction 比较两个cacheGroyp的大小 </span>
  <span class="hljs-keyword">const</span> aSizeReduce = a.size * (a.chunks.size - <span class="hljs-number">1</span>); 
  <span class="hljs-keyword">const</span> bSizeReduce = b.size * (b.chunks.size - <span class="hljs-number">1</span>); 
  <span class="hljs-keyword">const</span> diffSizeReduce = aSizeReduce - bSizeReduce; 
  <span class="hljs-keyword">if</span> (diffSizeReduce) <span class="hljs-keyword">return</span> diffSizeReduce; 
  <span class="hljs-comment">// 4. by cache group index 比较cacheGroupIndex </span>
  <span class="hljs-keyword">const</span> indexDiff = b.cacheGroupIndex - a.cacheGroupIndex; 
  <span class="hljs-keyword">if</span> (indexDiff) <span class="hljs-keyword">return</span> indexDiff; 
  <span class="hljs-comment">// 5. by number of modules (to be able to compare by identifier) 比较cacheGroup的modules数量 </span>
  <span class="hljs-keyword">const</span> modulesA = a.modules; 
  <span class="hljs-keyword">const</span> modulesB = b.modules; 
  <span class="hljs-keyword">const</span> diff = modulesA.size - modulesB.size; 
  <span class="hljs-keyword">if</span> (diff) <span class="hljs-keyword">return</span> diff; 
  <span class="hljs-comment">// 6. by module identifiers比较modules的identifiers </span>
  modulesA.sort(); 
  modulesB.sort(); 
  <span class="hljs-keyword">const</span> aI = modulesA[<span class="hljs-built_in">Symbol</span>.iterator](); 
  <span class="hljs-keyword">const</span> bI = modulesB[<span class="hljs-built_in">Symbol</span>.iterator](); 
  <span class="hljs-comment">// eslint-disable-next-line no-constant-condition </span>
  <span class="hljs-keyword">while</span> (<span class="hljs-literal">true</span>) &#123; 
    <span class="hljs-keyword">const</span> aItem = aI.next(); 
    <span class="hljs-keyword">const</span> bItem = bI.next(); 
    <span class="hljs-keyword">if</span> (aItem.done) <span class="hljs-keyword">return</span> <span class="hljs-number">0</span>; 
    <span class="hljs-keyword">const</span> aModuleIdentifier = aItem.value.identifier(); 
    <span class="hljs-keyword">const</span> bModuleIdentifier = bItem.value.identifier(); 
    <span class="hljs-keyword">if</span> (aModuleIdentifier > bModuleIdentifier) <span class="hljs-keyword">return</span> -<span class="hljs-number">1</span>; 
    <span class="hljs-keyword">if</span> (aModuleIdentifier < bModuleIdentifier) <span class="hljs-keyword">return</span> <span class="hljs-number">1</span>; 
  &#125; 
&#125;; 
 
<span class="hljs-keyword">const</span> isOverlap = <span class="hljs-function">(<span class="hljs-params">a, b</span>) =></span> &#123; 
  <span class="hljs-keyword">for</span> (<span class="hljs-keyword">const</span> item <span class="hljs-keyword">of</span> a) &#123; 
    <span class="hljs-keyword">if</span> (b.has(item)) <span class="hljs-keyword">return</span> <span class="hljs-literal">true</span>; 
  &#125; 
  <span class="hljs-keyword">return</span> <span class="hljs-literal">false</span>; 
&#125;; 
<span class="copy-code-btn">复制代码</span></code></pre>
<p>经过本阶段的筛选，chunksInfoMap 中符合配置规则的缓存组会被全部打包成新代码块，完成代码分割的工作。</p>
<h1 data-id="heading-13">总结</h1>
<p>以上就是SplitChunksPlugin的整个工作流程，从优化前准备到模块分组，最终依次检查，输出最终打包文件。不管是哪一个步骤都有着关键的作用。SplitChunksPlugin的源码我们不能修改，但是cacheGroups是交给我们配置的，合适cacheGroups配置，就能产出合适的chunksInfoMap，从而输出合适的分包结果。</p>
<p>分析源码的过程，可以看到整个过程并没有复杂的算法逻辑，而是合理的安排每一个步骤，在合适的时间做合适的事情，最终将一个庞大的项目分割成能够预测的结果。我们自己在开发过程中也应该学习这样的思想，不要过度设计，而是把复杂的设计简单化。当然简化流程的代价可能就是复杂的数据结构，这两者如何抉择还是因项目而异了。</p></div>  
</div>
            