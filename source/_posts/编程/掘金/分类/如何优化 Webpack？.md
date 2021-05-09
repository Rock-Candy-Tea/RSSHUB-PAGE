
---
title: '如何优化 Webpack？'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=148'
author: 掘金
comments: false
date: Sat, 08 May 2021 22:50:35 GMT
thumbnail: 'https://picsum.photos/400/300?random=148'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h4 data-id="heading-0">1）优化 Webpack 的构建速度</h4>
<ul>
<li>使用高版本的 Webpack（使用 webpack4）</li>
<li>多线程/多实例构建：happypack（不维护了）、thread-loader</li>
<li>缩小打包作用域：
<ul>
<li>exclude/include （确定 loader 规则范围）</li>
<li>resolve.modules 指明第三方模块的绝对路径（减少不必要的查找）</li>
<li>resolve.extensions 尽可能减少后缀尝试的可能性</li>
<li>noParse 对完全不需要解析的库进行忽略（不去解析但仍会打包到 bundle 中，注意被忽略掉的文件里不应该包含 import、require、define 等模块化语句）</li>
<li>IgnorePlugin（完全排除模块）</li>
<li>合理使用 alias</li>
</ul>
</li>
<li>充分利用缓存提升二次构建速度：
<ul>
<li>babel-loader 开启缓存</li>
<li>terser-webpack-plugin 开启换成</li>
<li>使用 cache-loader 或者 hard-source-webpack-plugin</li>
</ul>
<em>注：thread-loader 和 cache-loader 两个一起使用的话，请先放 cache-loader，接着是thread-loader，最后才是 heavy-loader。</em></li>
<li>DLL：
<ul>
<li>使用 DllPlugin 进行分包，使用 DllReferencePlugin（索引链接）对 manifest.json 引用，让一些基本不会改动的代码先打包成静态资源，避免反复编译浪费时间。</li>
</ul>
</li>
</ul>
<h4 data-id="heading-1">2）优化 Webpack 的打包体积</h4>
<ul>
<li>压缩代码
<ul>
<li>webpack-paralle-uglify-plugin</li>
<li>uglifyjs-webpack-plugin 开启 parallel 参数</li>
<li>terser-webpack-plugin 开启 parallel 参数</li>
<li>多线程并行压缩</li>
<li>通过 mini-css-extract-plugin 提取 Chunk 中的 CSS 代码到单独文件，通过对 optimize-css-asstes-webpack-plugin 插件，开启 cssnano 压缩 CSS</li>
</ul>
</li>
<li>提取页面公共资源
<ul>
<li>使用 html-webpack-externals-plugin，将基础包通过 CDN 引入，不打入 bundle 中</li>
<li>使用 SplitChunksPlugin 进行（公共脚本、基础包、也没公共文件）分离（Webpack4 内置），替代 CommonsChunkPlugin 插件</li>
</ul>
</li>
<li>Tree-shaking
<ul>
<li>purgecss-webpack-plugin 和 mini-css-extract-plugin 配合使用</li>
<li>打包过程中检测工程中没用引用过的模块并进行标记，在资源压缩时将他们从最终的 bundle 中去掉。该功能只能对 ES6 Modlue 生效，所以开发中尽可能使用 ES6 Modlue 的模块，提高 Tree-shaking 效率</li>
<li>禁用 babel-loader 的模块依赖解析，否则 Webpack 接收到的就是转换过的 CommonJs 形式的模块，无法进行 Tree-shaking</li>
<li>使用 PurifyCSS（不维护了）或者 uncss 去除无用 CSS 代码</li>
</ul>
</li>
<li>Scope hoisting
<ul>
<li>构建后的代码会存在大量闭包，造成体积增大，运行代码时创建的函数作用域变多，内存开销变大。Scope hoisting 将所有模块的代码按照引用顺序放在一个函数作用域里，然后适当的重命名一些变量以防止变量名冲突</li>
<li>必须是 ES6 的语法，因为很多第三方库仍采用 CommonJS 语法，为了充分发挥 Scope hoisting 的作用，需要配置 mainFields 对第三方模块优先采用 jsnext:main 中指向的 ES6 模块化语法</li>
</ul>
</li>
<li>图片压缩
<ul>
<li>使用基于 Node 库的 imagemin（很多定制选项、可以处理多种图片格式）</li>
<li>配置 image-webpack-loader</li>
</ul>
</li>
<li>动态 Polyfill
<ul>
<li>建议采用 polyfill-service 只给用户返回需要的 polyfill（部分国内奇葩浏览器UA可能无法识别，可以降级返回所需全部 polyfill）</li>
<li>@babel/preset-env 中通过 useBuiltlns:usage 参数来动态加载 polyfill</li>
</ul>
</li>
</ul>
<h4 data-id="heading-2">3)speed-measure-webpack-plugin</h4>
<p>简称 SMP，分析出 Webpack 打包过程中 Loader 和 Plugin 的耗时，有助于找到构建过程中的性能瓶颈。</p>
<h3 data-id="heading-3">webpack4 的优化</h3>
<ul>
<li>
<p>V8 带来的优化（for of 替代 forEach、map，Set 替代 Object，includes 替代 indexOf）</p>
</li>
<li>
<p>默认使用更快的 md4 hash 算法</p>
</li>
<li>
<p>webpacks AST 可以直接从 loader 传递给 AST，减少解析时间</p>
</li>
<li>
<p>使用字符串方法替代正则表达式</p>
<h5 data-id="heading-4">1. noParse</h5>
<p>不去解析某个库内部依赖关系，比如 jquery 这个库是独立的，则不去解析这个库内部以来的其他东西。在独立库的时候可以使用：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-built_in">module</span>.exports = &#123;
    <span class="hljs-attr">module</span>: &#123;
        <span class="hljs-attr">noParse</span>: <span class="hljs-regexp">/jquery/</span>,
        rules: []
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h5 data-id="heading-5">2.IgnorePlugin</h5>
<p>忽略掉某些内容，不去解析依赖库内部引用的某些内容。比如用 IgnorePlugin  来忽略 moment 的语言包 ：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-built_in">module</span>.exports = &#123;
    <span class="hljs-attr">plugins</span>: [
        <span class="hljs-keyword">new</span> Webpack.IgnorePlugin(<span class="hljs-regexp">/^\.\/locale$/</span>, <span class="hljs-regexp">/moment$/</span>)
    ]
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h5 data-id="heading-6">3.dllPlugin</h5>
<p><em>Webpack.DllPlugin、Webpack.DllReferencePlugin</em></p>
<ul>
<li>不会多次打包，优化打包时间</li>
<li>先把依赖的不变的库打包</li>
<li>生成 mainfest.json 文件</li>
<li>然后在 webpack.config 中引入</li>
</ul>
<h5 data-id="heading-7">4.happypack -> thread-loader</h5>
<ul>
<li>在大项目的时候开启多线程打包</li>
<li>影响前段发布速度的有两个方面，一个是构建，一个就是压缩，把这两个东西优化起来，可以减少很多发布的时间。</li>
</ul>
<h5 data-id="heading-8">5.thread-loader</h5>
<p>thread-loader 会将你的 loader 放置在一个 worker 池里面运行，以达到多线程构建。把这个 loader 放置在其他 loader 之前（如下图 example 的位置），放置在thread-loader 之后的 loader 就会在一个单独的 worker 池中运行。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// webpack.config.js</span>
<span class="hljs-built_in">module</span>.exports = &#123;
    <span class="hljs-attr">module</span>: &#123;
        <span class="hljs-attr">rules</span>: [
            &#123;
                <span class="hljs-attr">test</span>: <span class="hljs-regexp">/\.js$/</span>,
                include: path.resolve(<span class="hljs-string">"src"</span>),
                <span class="hljs-attr">use</span>: [
                    <span class="hljs-string">"thread-loader"</span>,
                    <span class="hljs-comment">// 你的高开销的 loader 放置在这里（e.g babel-loader）</span>
                ]
            &#125;
        ]
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>每个 worker 都是一个单独的有600ms限制的 node.js 进程，同时跨进程的数据交互也会被限制。请在高开销的 loader 中使用，否则效果不会很好。</p>
<h5 data-id="heading-9">6.压缩加速--开启多线程压缩</h5>
<p>推荐使用 terser-webpack-plugin</p>
<pre><code class="hljs language-js copyable" lang="js">modeule.exports = &#123;
    <span class="hljs-attr">optimization</span>: &#123;
        <span class="hljs-attr">minimizer</span>: [
            <span class="hljs-keyword">new</span> TerserPlugin(&#123; <span class="hljs-attr">parallel</span>: <span class="hljs-literal">true</span> &#125;) <span class="hljs-comment">// 多线程</span>
        ]
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
</ul></div>  
</div>
            