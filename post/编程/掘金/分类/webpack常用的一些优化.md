
---
title: 'webpack常用的一些优化'
categories: 
    - 编程
    - 掘金
    - 分类

author: 掘金
comments: false
date: Sun, 21 Mar 2021 23:48:01 GMT
thumbnail: ''
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><blockquote>
<p>Webpack是现在主流的功能强大的模块化打包工具，在使用Webpack时，如果不注意性能优化，有非常大的可能会产生性能问题，性能问题主要分为开发时打包构建速度慢、开发调试时的重复性工作、以及输出文件质量不高等，因此性能优化也主要从这些方面来分析。</p>
</blockquote>
<h2 data-id="heading-0">1.开发环境优化</h2>
<h3 data-id="heading-1">1.1 resolve.modules</h3>
<p>告诉webpack在那个文件夹下面去找第三方模块，避免了层层的查找</p>
<pre><code class="copyable">resolve:&#123;
    modules:[path.resolve(__dirname,'node_modules')]
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-2">1.2 resolve.alias</h3>
<p>对一些第三方比较打的库，指定其文件夹位置，避免了层层的查找</p>
<pre><code class="copyable">resolve:&#123;
    alias:&#123;
       'vue':patch.resolve(__dirname, './node_modules/vue/dist/vue.min.js'),
       'react':patch.resolve(__dirname, './node_modules/react/dist/react.min.js') 
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-3">1.3 配置loader时，通过test、exclude、include缩小搜索范围</h3>
<h3 data-id="heading-4">1.4 开启happypack多线程解析</h3>
<p>我一般在解析js文件的时候会使用</p>
<pre><code class="copyable">module:&#123;
    rules:[
        &#123;
            test: /(\.js|\.jsx)$/,
            exclude: resolve(__dirname, 'node_modules'),
            use: ['happypack/loader?id=babel'],
        &#125;,
    ]
&#125;,
plugins:[
    new happypack(&#123;
        id:"babel",
        loaders:[
            &#123;loader:'babel-loader?cacheDirectory=true'&#125;
        ]
    &#125;)
]
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-5">1.5 开启paralleUgilifyPlugin多线程压缩js文件</h3>
<pre><code class="copyable">new ParallelUglifyPlugin(&#123;
            uglifyJS: &#123;
                output: &#123;
                    //去除空格
                    beautify: false,
                    //去除注释
                    comments: false
                &#125;,
                compress: &#123;
                    //删除所有的console
                    drop_console: false
                &#125;
            &#125;
&#125;),
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-6">1.6 开启热模块替换HMR</h3>
<p>模块热替换不刷新整个网页而只重新编译发生变化的模块，并用新模块替换老模块</p>
<pre><code class="copyable">/**
* 启用webpack内置的webpack插件(开启HMR)
*/
 new webpack.HotModuleReplacementPlugin(),
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="copyable">devServer:&#123;
    hot:true
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-7">2.生产环境优化</h2>
<h3 data-id="heading-8">2.1 单独提取css代码MiniCssExtractPlugin</h3>
<pre><code class="copyable">&#123;
    test:/\.css$/,
    use:[MiniCssExtractPlugin.loader,css-loader]
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="copyable">new MiniCssExtractPlugin(&#123;
    filename:'css/[name].[hash:10].css'
&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-9">2.2压缩css OptimizeCssAssetsWebpackPlugin</h3>
<pre><code class="copyable">new OptimizeCssAssetsWebpackPlugin()
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-10">2.3 代码分割 optimization</h3>
<pre><code class="copyable">optimization: &#123;
        splitChunks: &#123;
            chunks: 'all',
            minSize: 30000, //块的最小大小,只有超过30k,才会进行代码分割
            maxSize: 0,
            minChunks: 1, //模块至少需要被引用1次
            maxAsyncRequests: 5, //最大打包数量
            maxInitialRequests: 3, //entry入口最大数量
            automaticNameDelimiter: '~',
            name: true,
            cacheGroups: &#123;
                vendors: &#123;
                    test: /[\\/]node_modules[\\/]/,
                    priority: -10,
                    reuseExistingChunk: true
                &#125;,
                default: &#123;
                    minChunks: 2,
                    priority: -20,
                    reuseExistingChunk: true
                &#125;
            &#125;
        &#125;,
        runtimeChunk: &#123;
            name: entrypoint => `manifest.$&#123;entrypoint.name&#125;`
        &#125;
    &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-11">2.4 按需加载</h3>
<pre><code class="copyable">import(/*webpackChunkName:"one*/'./one.js').then(data=>&#123;
    console.log(data);
&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-12">2.5 CDN引入第三方包</h3>
<pre><code class="copyable"><body>
    <div id="app"></div>
    <script src="https://cdn.bootcss.com/jquery/3.4.1/jquery.min.js"></script>
</body>
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="copyable">externals:&#123;
    jquery:"jQuery",//告诉webpack哪些第三方包不参与打包，优化首屏加载速度
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-13">2.6 source-map</h3>
<p>我的用法：</p>
<pre><code class="copyable">devtool: process.env.NODE_ENV == 'development' ? 'eval-source-map' : 'cheap-module-source-map',
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-14">2.7 Tree Shaking剔除无用代码</h3></div> <div class="image-viewer-box" data-v-78c9b824><!----></div>  
</div>
            