
---
title: 'webpack全方位由浅到深讲解，做到简历上真正所谓的_熟悉_(系列一)'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/0818657a514542aaac2fdc5552a9f991~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Sat, 17 Apr 2021 06:50:38 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/0818657a514542aaac2fdc5552a9f991~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p><img alt="b840c72e59dd5b880ed68bb8d10b6c62.jpeg" class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/0818657a514542aaac2fdc5552a9f991~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<blockquote>
<p>注意：文章基于“webpack4”讲解</p>
</blockquote>
<h2 data-id="heading-0">1.为什么需要构建工具</h2>
<ul>
<li>
<ol>
<li>转换 ES6 语法</li>
</ol>
</li>
<li>
<ol start="2">
<li>转换 JSX</li>
</ol>
</li>
<li>
<ol start="3">
<li>CSS 前缀补全/预处理器</li>
</ol>
</li>
<li>
<ol start="4">
<li>压缩混淆</li>
</ol>
</li>
<li>
<ol start="5">
<li>图片压缩</li>
</ol>
</li>
</ul>
<p>...欢迎补充</p>
<h2 data-id="heading-1">2.初识webpack</h2>
<ul>
<li>
<p>1.默认配置文件：webpack.config.js。 可以通过 webpack --config 指定配置文件</p>
</li>
<li>
<p>2.配置组成</p>
<pre><code class="copyable">module.exports = &#123;
    //打包的入口文件
    entry: './src/index.js',
    // 打包的输出
    output: './dist/main.js,
    // 环境
    mode: 'production',
    module: &#123;
        // Loader 配置
        rules: [
            &#123;
                test:/\.txt$/,
                use: 'raw-loader'
            &#125;
        ]
    &#125;,
    plugins: [
        // 插件配置
        new HtmlWebpackPlugin(&#123;
            template: './src/index.html'
        &#125;)
    ]
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<blockquote>
<p>从webpack4后，webpack将内核和cli分离，所以需要安装webpack和webpack-cli</p>
</blockquote>
</li>
</ul>
<h2 data-id="heading-2">3. 通过 npm script 运行 webpack</h2>
<blockquote>
<p>原理： 模块局部安装会在 node_modules/.bin 目录创建软连接， package.json会默认读取./bin目录下的命名</p>
</blockquote>
<pre><code class="copyable">"scripts": &#123;
   "build": "webpack"
 &#125;,
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-3">4. entry 用法</h2>
<blockquote>
<p>指定打包入口</p>
</blockquote>
<ul>
<li>
<ol>
<li>单入口： entry是一个字符串(单页应用)</li>
</ol>
<pre><code class="copyable">module.exports = &#123;
   entry: './src/index.js'
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
<li>
<ol start="2">
<li>多入口： entry是一个对象（多页应用）</li>
</ol>
<pre><code class="copyable">module.exports = &#123;
   entry: &#123;
        index: './src/index.js'  
        app: './src/app.js'
   &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
</ul>
<h2 data-id="heading-4">5.output</h2>
<blockquote>
<p>告诉 webpack 如何将编译后的文件输出到磁盘</p>
</blockquote>
<ul>
<li>1.单入口配置
<pre><code class="copyable">module.exports = &#123;
    entry: &#123;
         index: './src/index.js'  
         app: './src/app.js'
    &#125;,
    output: &#123;
        filename: 'bundle.js',
        path: __dirname+'/dist'
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
<li>2.多入口配置
<pre><code class="copyable">module.exports = &#123;
    entry: './src/index.js',
    output: &#123;
        filename: '[name].js',
        path: __dirname+'/dist'
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
通过占位符确保文件名称的唯一</li>
</ul>
<h2 data-id="heading-5">6.loaders</h2>
<blockquote>
<p>webpack默认只支持JS 和 JSON 两种文件类型， 通过Loaders去支持其它文件类型并且把它们转化成有效的模块， 并且可以添加到依赖图中。本身是一个函数，接收源文件作为参数， 返回转换的结果。</p>
</blockquote>
<h4 data-id="heading-6">常见的Loaders</h4>
<ul>
<li>1.babel-loader: 转换ES6、ES7等JS新特性语法</li>
<li>2.css-loader: 支持css文件的加载和解析</li>
<li>3.less-loader: 将less文件转换成css</li>
<li>4.ts-loader: 将TS转换成JS</li>
<li>5.file-loader: 进行图片、字体等的打包</li>
<li>6.raw-loader: 将文件以字符串的形式导入</li>
<li>7.thread-loader: 多进程打包JS和CSS</li>
</ul>
<h4 data-id="heading-7">用法</h4>
<pre><code class="copyable">module.exports = &#123;
    output: &#123;
        filename: 'bundle.js'
    &#125;,
    module: &#123;
        rules: [
           &#123;
               test: /\.txt$/,   // test指定匹配规则
               use: 'raw-loader' // use指定使用的loader名称
           &#125; 
        ]
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-8">7.plugins</h2>
<blockquote>
<p>插件用于 bundle 文件的优化，资源管理和环境变量注入 ，作用于整个构建过程</p>
</blockquote>
<h4 data-id="heading-9">常见的Plugins</h4>
<ul>
<li>splitchunksplugin: 将chunks相同的模块代码提取成公共js</li>
<li>CleanWebpackPlugin: 清理构建目录</li>
<li>CopyWebpackPlugin: 将文件或者文件夹拷贝到构建的输出目录</li>
<li>HtmlWebpackPlugin: 创建html文件去承载输出的bundle</li>
<li>UglifyjsWebpackPlugin: 压缩JS</li>
<li>ZipWebpackPlugin: 将打包出的资源生成一个zip包</li>
<li>MiniCssExtractPlugin: 将CSS从bundle文件里提取成一个独立的CSS文件</li>
<li>OptimizeCssAssetsWebpackPlugin：CSS文件压缩</li>
<li>autoprefixer: PostCSS自动补齐CSS3前缀</li>
</ul>
<h4 data-id="heading-10">用法</h4>
<pre><code class="copyable">const path = require('path')
module.exports = &#123;
    output: &#123;
        filename: 'bundle.js'
    &#125;,
    plugins: [
        new HtmlWebpackPlugin(&#123;
            template: './src/index.html' // 放到plugins数组里
        &#125;)
    ]
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-11">8.mode</h2>
<blockquote>
<p>mode用来指定当前的构建环境是：production、development 还是 none, 设置mode可以使用 webpack内置的函数， 默认值为 production</p>
</blockquote>
<h4 data-id="heading-12">mode的内置函数功能</h4>
<ul>
<li>
<ol>
<li>development: 设置 process.env.NODE_ENV 的值为 development, 开启NamedChunksPlugin 和 NamedModulesPlugin.(模块热更新相关，会在控制台打印出哪个模块更改和对应路径)</li>
</ol>
</li>
<li>
<ol start="2">
<li>production: 设置 process.env.NODE_ENV 的值为 production， 开启FlagDependencyUsagePlugin, FlagIncludedChunksPlugin, OccurrenceOrderPlugin, SideEffectsFlagPlugin 和 TerserPlugin</li>
</ol>
</li>
<li>
<ol start="3">
<li>none: 不开启任何优化选项</li>
</ol>
</li>
</ul>
<h2 data-id="heading-13">9.解析ES6</h2>
<blockquote>
<p>使用 babel-loader。 babel的配置文件是： .babelrc</p>
</blockquote>
<pre><code class="copyable">modules: &#123;
    rules: [
        &#123;
            test: /\.js$/,
            use: 'babel-loader'
        &#125;
    ]
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="copyable">.babelrc文件
&#123;
    "presets": [
        "@babel/preset-env",
    ] 
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-14">10.解析css</h2>
<ul>
<li>
<ol>
<li>css-loader用于加载.css文件， 并且转换成 commonjs对象</li>
</ol>
</li>
<li>
<ol start="2">
<li>style-loader将样式通过 标签插入到head中
</li></ol>
</li>
</ul>
<pre><code class="copyable">&#123;
    test:/\.css$/,
    use: [
        'style-loader',
        'css-loader'
    ]
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<blockquote>
<p>loader是链式调用，执行顺序是从右到左。</p>
</blockquote>
<h2 data-id="heading-15">11.解析图片和字体</h2>
<ul>
<li>
<ol>
<li>file-loader 用于处理文件,也可用于处理字体</li>
</ol>
</li>
</ul>
<pre><code class="copyable">&#123;
    test: /\.(png|svg|jpg|gif)$/,
    use: [
        'file-loader'
    ]
&#125;

&#123;
    test: /\.(woff|woff2|eot|tff|otf)$/,
    use: [
        'file-loader'
    ]
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>
<ol start="2">
<li>url-loader也可以处理图片和字体， 可以设置较小资源自动base64</li>
</ol>
</li>
</ul>
<pre><code class="copyable">&#123;
    test: /\.(png|svg|jpg|gif)$/,
    use: [
       &#123;
            loader: 'url-loader',
            options: &#123;
                limit: 10240 //单位字节
            &#125;
       &#125;
    ] 
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-16">12. webpack中的文件监听</h2>
<p>开启监听模式，有两种方式</p>
<ul>
<li>
<ol>
<li>启动webpack命令时，带上 --watch 参数</li>
</ol>
</li>
<li>
<ol start="2">
<li>在配置 webpack.config.js中设置watch:true</li>
</ol>
</li>
</ul>
<pre><code class="copyable">module.export = &#123;
    // 默认false,也就是不开启
    watch:true,
    // 只有开启监听模式时，watchOptions才有意义
    watchOptions: &#123;
        // 默认为空， 不监听的文件 或 文件夹， 支持正则匹配
        ignored: /node_modules/,
        // 监听到变化发生后会等300ms再去执行， 默认300ms
        aggregateTimeout: 300,
        // 判断文件是否发生变化是通过不停询问系统指定文件有没有变化实现的，         // 默认每秒问1次
        poll: 1000
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-17">13. 热更新： webpack-dev-server</h2>
<ul>
<li>
<ol>
<li>不刷新浏览器</li>
</ol>
</li>
<li>
<ol start="2">
<li>不输出文件，而是放在内存中</li>
</ol>
</li>
</ul>
<p>使用HotModuleReplacementPlugin插件</p>
<pre><code class="copyable">// package.json
&#123;
    scripts: &#123;
        "dev": "webpack-dev-server --open"
    &#125;
&#125;

// webpack.config.js
module.export = &#123;
    plugins: [
        new webpack.HotModuleReplacementPlugin() // 配置了 hot: true 会自动引入这个 plugin
    ],
    devServer: &#123;
        contentBase: './dist',
        hot: true  // 会自动引入这个 HotModuleReplacementPlugin
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<blockquote>
<p>还有一种热更新： 使用 webpack-dev-middleware, 将webpack输出的文件传输给服务器，适用于灵活的定制场景。</p>
</blockquote>
<h4 data-id="heading-18">热更新的原理分析</h4>
<ul>
<li>
<ol>
<li>Webpack Compile: 将JS编译成 Bundle</li>
</ol>
</li>
<li>
<ol start="2">
<li>HMR Server: 将热更新的文件输出 HMR Runtime</li>
</ol>
</li>
<li>
<ol start="3">
<li>Bundle server: 提供文件在浏览器的访问</li>
</ol>
</li>
<li>
<ol start="4">
<li>HMR Runtime: 会被注入到浏览器，更新文件的变化</li>
</ol>
</li>
<li>
<ol start="5">
<li>bundle.js: 构建输出的文件</li>
</ol>
</li>
</ul>
<blockquote>
<p>热更新有最核心的是 HMR Server 和 HMR runtime。HMR Server 是服务端，用来将变化的 js 模块通过 websocket 的消息通知给浏览器端。HMR Runtime是浏览器端，用于接受 HMR Server 传递的模块数据，浏览器端可以看到 .hot-update.json 的文件过来。</p>
</blockquote>
<ul>
<li>
<p>HotModuleReplacementPlugin是做什么用的？</p>
<ul>
<li>webpack 构建出来的 bundle.js 本身是不具备热更新的能力的，HotModuleReplacementPlugin 的作用就是将 HMR runtime 注入到 bundle.js，使得bundle.js可以和HMR server建立websocket的通信连接</li>
</ul>
</li>
</ul>
<h2 data-id="heading-19">14.文件指纹</h2>
<ul>
<li>
<ol>
<li>Hash: 和整个项目的构建相关，只要项目文件有修改， 整个项目构建的hash值就会修改</li>
</ol>
</li>
<li>
<ol start="2">
<li>Chunkhash: 和webpack打包的chunk有关，不同的entry会生成不同的chunkhash值</li>
</ol>
<pre><code class="copyable">filename: '[name][chunkhash:8].js'
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
<li>
<ol start="3">
<li>Contenthash: 根据文件内容来定义hash, 文件内容不变，则contenthash不变(css文件一般设置这个hash)</li>
</ol>
<pre><code class="copyable">plugins: [
    new MiniCssExtractPlugin(&#123;
        filename: '[name][contenthash:8].css'
    &#125;)
]
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-20">图片的文件指纹设置</h4>
<p>设置file-loader的name,使用[hash]</p>
<ul>
<li>
<ol>
<li>[ext]: 资源后缀名</li>
</ol>
</li>
<li>
<ol start="2">
<li>[name]: 文件名称</li>
</ol>
</li>
<li>
<ol start="3">
<li>[path]: 文件的相对路径</li>
</ol>
</li>
<li>
<ol start="4">
<li>[folder]: 文件所在的文件夹</li>
</ol>
</li>
<li>
<ol start="5">
<li>[contenthash]: 文件的内容hash,默认是md5生成</li>
</ol>
</li>
<li>
<ol start="6">
<li>[hash]: 文件的内容hash,默认是md5生成</li>
</ol>
</li>
<li>
<ol start="7">
<li>[emoji]: 一个随机的指代文件内容的emoji</li>
</ol>
</li>
</ul>
<pre><code class="copyable">&#123;
    test: /\.(png|svg|jpg|gif)$/,
    use: [&#123;
        loader: 'file-loader',
        options: &#123;
            name: 'img/[name][hash:8].[ext]'
        &#125;
    &#125;]
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
</ul>
<h2 data-id="heading-21">15.代码压缩</h2>
<ul>
<li>
<ol>
<li>JS文件压缩： webpack内置了uglifyjs-webpack-plugin</li>
</ol>
</li>
<li>
<ol start="2">
<li>CSS文件压缩： 使用optimize-css-assets-webpack-plugin,同时使用 cssnano</li>
</ol>
</li>
</ul>
<pre><code class="copyable">plugins: [
    new OptimizeCSSAssetsPlugin(&#123;
        assetNameRegExp: /\.css$/g,
        cssProcessor: require('cssnano')
    &#125;)
]
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>
<ol start="3">
<li>HTML文件压缩：使用 html-webpack-plugin, 设置压缩参数</li>
</ol>
</li>
</ul>
<pre><code class="copyable">new HtmlWebpackPlugin(&#123;
    template: path.join(__dirname,'src/search.html'),
    filename: 'search.html',
    chunks: ['search'],
    inject: true,
    minify: &#123;
        html5: true,
        collapseWhitespace: true,
        preserveLineBreaks: false,
        minifyCSS: true,
        minifyJS: true,
        removeComments: false
    &#125;
&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-22">16. 自动清除构建目录</h2>
<p>避免构建前每次都需要手动删除 dist</p>
<p>使用 clean-webpack-plugin, 默认会删除output指定的输出目录</p>
<pre><code class="copyable">plugins:[
    new CleanWebpackPlugin()
]
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-23">17.PostCss插件autoprefixer自动补齐CSS3前缀</h2>
<p>配置：</p>
<pre><code class="copyable">&#123;
    test: /\.css$/,
    use: [
        MiniCssExtractPlugin.loader,
        'css-loader',
        'postcss-loader'
    ]
&#125;,

// .browserslistrc
# Browsers that we support

last 2 version 
>1%

//postcss.config.js
module.exports = &#123;
    plugins: [
        require('autoprefixer')
    ]
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<blockquote>
<p>loader顺序：less-loader -> postcss-loader -> css-loader -> style-loader 或者 MiniCssExtractPlugin.loader</p>
</blockquote>
<h2 data-id="heading-24">18.静态资源内联</h2>
<ul>
<li>
<ol>
<li>代码层面：</li>
</ol>
<ul>
<li>页面框架的初始化脚本</li>
<li>上报相关打点</li>
<li>css内联避免页面闪动</li>
</ul>
</li>
<li>2.请求层面：减少HTTP网络请求数
<ul>
<li>小图片或者字体内联（url-loader）</li>
</ul>
</li>
</ul>
<h4 data-id="heading-25">HTMl和JS内联</h4>
<blockquote>
<p>raw-loader(版本0.5.1)</p>
</blockquote>
<ul>
<li>
<p>raw-loader内联html</p>
<ul>
<li>require('raw-loader!./meta.html')</li>
</ul>
</li>
<li>
<p>raw-loader 内联JS</p>
<ul>
<li>require('raw-loader!babel-loader!../node_modules/lib-fixible')</li>
</ul>
</li>
</ul>
<h4 data-id="heading-26">CSS内联</h4>
<ul>
<li>1.html-inline-css-webpack-plugin</li>
</ul>
<h2 data-id="heading-27">19.多页面打包通用方案</h2>
<ul>
<li>
<p>动态获取entry和设置html-webpack-plugin数量</p>
<pre><code class="copyable">利用 glob.sync
entry: glob.sync(path.join(__dirname,'./src/*/index.js'))
<span class="copy-code-btn">复制代码</span></code></pre>
<p>具体配置：</p>
<pre><code class="copyable">const glob = require('glob');

const setMPA = () => &#123;
  const entry = &#123;&#125;;
  const htmlWebpackPlugins = [];
  const entryFiles = glob.sync(path.join(__dirname,     './src/*/index.js'));

Object.keys(entryFiles)
  .map((index) => &#123;
      const entryFile = entryFiles[index];

      const match = entryFile.match(/src\/(.*)\/index.js/);
      const pageName = match && match[1];

      entry[pageName] = entryFile;
      htmlWebpackPlugins.push(
          new HtmlWebpackPlugin(&#123;
              template: path.join(__dirname,`src/$&#123;pageName&#125;/index.html`),
              filename: `$&#123;pageName&#125;.html`,
              chunks: [`$&#123;pageName&#125;`],
              inject: true,
              minify: &#123;
                  html5: true,
                  collapseWhitespace: true,
                  preserveLineBreaks: false,
                  minifyCSS: true,
                  minifyJS: true,
                  removeComments: false
              &#125;
          &#125;)
      )
  &#125;)

  return &#123;
      entry, 
      htmlWebpackPlugins
  &#125;    
&#125;
const &#123;entry, htmlWebpackPlugins&#125; = setMPA();
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
</ul>
<h2 data-id="heading-28">20. source map</h2>
<p>作用： 通过 source map 定位到源代码</p>
<p>开发环境开启，线上环境关闭</p>
<ul>
<li>source map 关键字
<ul>
<li>
<ol>
<li>eval: 使用eval包裹模块代码</li>
</ol>
</li>
<li>
<ol start="2">
<li>source map: 产生.map文件</li>
</ol>
</li>
<li>
<ol start="3">
<li>cheap: 不包含列信息</li>
</ol>
</li>
<li>
<ol start="4">
<li>inline: 将.map作为DataURI嵌入， 不单独生成.map文件</li>
</ol>
</li>
<li>
<ol start="5">
<li>module: 包含loader的sourcemap</li>
</ol>
</li>
</ul>
</li>
</ul>
































































































<table><thead><tr><th>devtool</th><th>首次构建</th><th>二次构建</th><th>是否适合生产环境</th><th>可以定位的代码</th></tr></thead><tbody><tr><td>(none)</td><td>+++</td><td>+++</td><td>yes</td><td>最终输出的代码</td></tr><tr><td>eval</td><td>+++</td><td>+++</td><td>no</td><td>webpack生成的代码（一个个的模块）</td></tr><tr><td>cheap-eval-source-map</td><td>+</td><td>++</td><td>no</td><td>经过loader转换后的代码（只能看到行）</td></tr><tr><td>cheap-module-eval-source-map</td><td>0</td><td>++</td><td>no</td><td>源代码（只能看到行）</td></tr><tr><td>eval-source-map</td><td>-</td><td>+</td><td>no</td><td>源代码</td></tr><tr><td>cheap-source-map</td><td>+</td><td>0</td><td>yes</td><td>经过loader转换后的代码（只能看到行）</td></tr><tr><td>cheap-module-source-map</td><td>0</td><td>-</td><td>yes</td><td>源代码（只能看到行）</td></tr><tr><td>inline-cheap-source-map</td><td>+</td><td>0</td><td>no</td><td>经过loader转换后的代码（只能看到行）</td></tr><tr><td>inline-cheap-module-source-map</td><td>0</td><td>-</td><td>no</td><td>源代码（只能看到行）</td></tr><tr><td>source-map</td><td>--</td><td>--</td><td>yes</td><td>源代码</td></tr><tr><td>inline-source-map</td><td>--</td><td>--</td><td>no</td><td>源代码</td></tr><tr><td>hidden-source-map</td><td>--</td><td>--</td><td>yes</td><td>源代码</td></tr></tbody></table>
<blockquote>
<p>官网链接：<a href="https://webpack.docschina.org/configuration/devtool/" target="_blank" rel="nofollow noopener noreferrer">webpack.docschina.org/configurati…</a></p>
</blockquote>
<h2 data-id="heading-29">21.提取页面公共资源</h2>
<h4 data-id="heading-30">基础库分离</h4>
<p>方法一：</p>
<ul>
<li>
<ol>
<li>html-webpack-externals-plugin</li>
</ol>
</li>
</ul>
<pre><code class="copyable">new HtmlWebpackExternalsPlugin(&#123;
        externals: [
            &#123;
                module: 'react',
                entry: '//now8.gtimg.com/now/lib/16.8.6/react.min.js?_bid=4042',
                global: 'React'
            &#125;,
            &#123;
                module: 'react-dom',
                entry: '//now8.gtimg.com/now/lib/16.8.6/react-dom.min.js?_bid=4042',
                global: 'ReactDOM'
            &#125;
        ]
    &#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>方法二：</p>
<ul>
<li>
<ol start="2">
<li>SplitChunksPlugin</li>
</ol>
</li>
</ul>
<pre><code class="copyable">optimization: &#123;
    splitChunks: &#123;
        cacheGroups: &#123;
            commons: &#123;
                test: /(react|react-dom)/,
                name: 'vendors',
                chunks: 'all'
            &#125;
        &#125;
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-31">利用SplitChunksPlugin进行公共脚本分离</h4>
<pre><code class="copyable">optimization: &#123;
    splitChunks: &#123;
        minSize: 0,
        cacheGroups: &#123;
            commons: &#123;
                name: 'commons',
                chunks: 'all',
                minChunks: 2
            &#125;
        &#125;
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="copyable">module.exports = &#123;
    //...
    optimization: &#123;
      splitChunks: &#123;
        // async：异步引入的库进行分离（默认）， initial： 同步引入的库进行分离， all：所有引入的库进行分离（推荐）
        chunks: 'async',
        minSize: 30000, // 抽离的公共包最小的大小，单位字节
        maxSize: 0, // 最大的大小
        minChunks: 1, // 资源使用的次数(在多个页面使用到)， 大于1， 最小使用次数
        maxAsyncRequests: 5, // 并发请求的数量
        maxInitialRequests: 3, // 入口文件做代码分割最多能分成3个js文件
        automaticNameDelimiter: '~', // 文件生成时的连接符
        automaticNameMaxLength: 30, // 自动自动命名最大长度
        name: true, //让cacheGroups里设置的名字有效
        cacheGroups: &#123; //当打包同步代码时,上面的参数生效
          vendors: &#123;
            test: /[\\/]node_modules[\\/]/, //检测引入的库是否在node_modlues目录下的
            priority: -10, //值越大,优先级越高.模块先打包到优先级高的组里
            filename: 'vendors.js'//把所有的库都打包到一个叫vendors.js的文件里
          &#125;,
          default: &#123;
            minChunks: 2, // 上面有
            priority: -20, // 上面有
            reuseExistingChunk: true //如果一个模块已经被打包过了,那么再打包时就忽略这个上模块
          &#125;
        &#125;
      &#125;
    &#125;
  &#125;;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-32">22. Tree Shaking（摇树优化）的使用和原理分析</h2>
<p>概念： 1个模块可能有多个方法，只要其中的某个方法使用到了， 则整个文件都会被打到bundle里面去，tree shaking就是只把用到的方法打入bundle,没用到的方法会在uglify阶段被擦除掉。</p>
<p>使用： webpack默认支持， 在.babelrc里设置moudules:false即可， production mode的情况下默认开启</p>
<p>要求： 必须是ES6的语法， CJS的方式不支持</p>
<h4 data-id="heading-33">DCE(dead code elimination): 无用代码消除</h4>
<ul>
<li>
<ol>
<li>代码不会被执行</li>
</ol>
</li>
<li>
<ol start="2">
<li>代码执行的结果不会被用到</li>
</ol>
</li>
<li>
<ol start="3">
<li>代码只会影响死变量（只读不写）</li>
</ol>
</li>
</ul>
<p>例如：</p>
<pre><code class="copyable">if(false) &#123;
    console.log('这段代码永远不会执行')
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-34">Tree-shaking原理</h4>
<ul>
<li>1.利用ES6模块的特点：
<ul>
<li>
<ol>
<li>只能作为模块顶层的语句出现</li>
</ol>
</li>
<li>
<ol start="2">
<li>import的模块只能是字符串常量</li>
</ol>
</li>
<li>
<ol start="3">
<li>import binding是immutable的</li>
</ol>
</li>
</ul>
</li>
<li>
<ol start="2">
<li>代码擦除： uglify阶段删除无用代码</li>
</ol>
</li>
</ul>
<blockquote>
<p>编写的代码不能有副作用，不然tree-shaking会失效。副作用这个概念来源于函数式编程(FP)，纯函数是没有副作用的，也不依赖外界环境或者改变外界环境。纯函数的概念是：接受相同的输入，任何情况下输出都是一样的。非纯函数存在副作用，副作用就是：相同的输入，输出不一定相同。或者这个函数会影响到外部变量、外部环境。函数如果调用了全局对象或者改变函数外部变量，则说明这个函数有副作用。</p>
</blockquote>
<h2 data-id="heading-35">23. Scope Hoisting使用和原理分析</h2>
<p>现象： 构建后的代码存在大量闭包代码</p>
<p>导致：</p>
<ul>
<li>1.大量函数闭包包裹代码， 导致体积增大（模块越多越明显）</li>
<li>2.运行代码时创建的函数作用域变多，内存开销变大</li>
</ul>
<h4 data-id="heading-36">scope hoisting 原理</h4>
<p>原理： 将所有模块的代码按照引用顺序放在一个函数作用域里， 然后适当的重命名一些变量以防止变量名冲突</p>
<p>对比：通过scope hoisting可以减少函数申明代码和内存开销</p>
<blockquote>
<p>webapck mode 为 production默认开启，必须是ES6语法， CJS不支持</p>
</blockquote>
<pre><code class="copyable">plugins: [
    new webpack.optimize.ModuleConcatenationPlugin()
]
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-37">24. 代码分割和动态import</h2>
<ul>
<li>
<p>适用的场景：</p>
<ul>
<li>
<ol>
<li>抽离相同代码到一个共享块</li>
</ol>
</li>
<li>
<ol start="2">
<li>脚本懒加载，使得初始下载的代码更小</li>
</ol>
</li>
</ul>
</li>
<li>
<p>懒加载 JS 脚本的方式</p>
<ul>
<li>ES6: 动态 import (目前还没有原生支持， 需要babel转换)，安装babel插件： @babel/plugin-syntax-dynamic-import</li>
</ul>
<pre><code class="copyable">// .babelrc配置
&#123;
    "presets": [
        ["@babel/preset-env"],
    ],
    "plugins": [
        "@babel/plugin-syntax-dynamic-import"
    ]
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
</ul>
<h2 data-id="heading-38">25. 在webpack中使用ESLint</h2>
<pre><code class="copyable">&#123;
    test: /\.js$/,
    use: [
        'babel-loader',
        'eslint-loader'
    ]
&#125;
// .eslintrc.js
module.exports = &#123;
    "parser": "babel-eslint",
    "extends": "airbnb",
    "env": &#123;
        "browser": true,
        "node": true
    &#125;,
    "rules": &#123;
        "indent": ["error", 4]
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-39">26. webpack打包库和组件</h2>
<h4 data-id="heading-40">1.如何将库暴露出去</h4>
<ul>
<li>1.library: 指定库的全局变量</li>
<li>2.libraryTarget: 支持库引入的方式</li>
</ul>
<pre><code class="copyable">entry: &#123;
     "input": './src/components/input.js',
     "form": './src/components/form.js',
     "formItem": './src/components/form-item.js',
     "index": './src/components/index.js'
&#125;,
output: &#123;
    filename: '[name].js',
    library: 'soloForm',
    libraryExport: 'default',
    libraryTarget: 'umd'
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-41">27. 优化构建时命令行的显示日志</h2>
<ol>
<li></li>
</ol>



































<table><thead><tr><th>Preset</th><th>Alternative</th><th>Description</th></tr></thead><tbody><tr><td>"errors-only"</td><td>none</td><td>只在发生错误时输出</td></tr><tr><td>"minimal"</td><td>none</td><td>只在发生错误或有新的编译时输出</td></tr><tr><td>"none"</td><td>false</td><td>没有输出</td></tr><tr><td>"normal"</td><td>true</td><td>标准输出</td></tr><tr><td>"verbose"</td><td>none</td><td>全部输出</td></tr></tbody></table>
<pre><code class="copyable">// webpack.config.js
stats: 'errors-only'
<span class="copy-code-btn">复制代码</span></code></pre>
<ol start="2">
<li>优化命令行的构建日志</li>
</ol>
<ul>
<li>使用 friendly-errors-webpack-plugin
<ul>
<li>success: 构建成功的日志提示</li>
<li>warning：构建警告的日志提示</li>
<li>error: 构建报错的日志提示</li>
</ul>
</li>
<li>stats 设置成 errors-only</li>
</ul>
<pre><code class="copyable">plugins: [
  ...     
  new FriendlyErrorsWebpackPlugin(),
  ...
],
stats: 'errors-only'
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-42">28.构建异常和中断处理</h2>
<ul>
<li>
<p>compiler在每次构建结束后会触发 done 这个hook</p>
</li>
<li>
<p>process.exit 主动处理构建报错</p>
</li>
</ul>
<pre><code class="copyable">plugins: [
    new FriendlyErrorsWebpackPlugin(),
    function() &#123;
        this.hooks.done.tap('done', (stats) => &#123;
            if (stats.compilation.errors &&
                stats.compilation.errors.length &&
                process.argv.indexOf('--watch') == -1) &#123;
                    console.log('build error');
                    process.exit(1);
                &#125;
        &#125;)
    &#125;
]
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img alt="image.png" class="lazyload" src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/1b44bf8c973c4409860dce6713fd1a2c~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-43">最后</h2>
<h4 data-id="heading-44">其它系列文章链接</h4>
<ul>
<li><a href="https://juejin.cn/post/6952137026825093134" target="_blank">webpack全方位由浅到深讲解，做到简历上真正所谓的“熟悉”(系列一)</a></li>
<li><a href="https://juejin.cn/post/6952139288779685901" target="_blank">webpack全方位由浅到深讲解，做到简历上真正所谓的“熟悉”(系列二)</a></li>
<li><a href="https://juejin.cn/post/6952350211888906248" target="_blank">webpack全方位由浅到深讲解，做到简历上真正所谓的“熟悉”(系列三)</a></li>
</ul></div> <div class="image-viewer-box" data-v-78c9b824><!----></div>  
</div>
            