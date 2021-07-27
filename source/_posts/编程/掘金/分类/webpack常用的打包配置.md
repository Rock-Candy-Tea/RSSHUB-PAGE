
---
title: 'webpack常用的打包配置'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=2570'
author: 掘金
comments: false
date: Sun, 25 Jul 2021 23:12:15 GMT
thumbnail: 'https://picsum.photos/400/300?random=2570'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>webpack打包</p>
<p>webpack在项目根目录创建一个webpack.config.js文件</p>
<h3 data-id="heading-0">webpack.config.js</h3>
<p>主要有五个属性</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-built_in">module</span>.exports = &#123;
    <span class="hljs-attr">entry</span>:<span class="hljs-string">""</span>,
    <span class="hljs-attr">output</span>:&#123;
        <span class="hljs-attr">filename</span>:<span class="hljs-string">""</span>, <span class="hljs-comment">// 输出的文件名</span>
        <span class="hljs-attr">path</span>:<span class="hljs-string">""</span> <span class="hljs-comment">// 文件输出的位置</span>
    &#125;,
    <span class="hljs-attr">module</span>:&#123;
        <span class="hljs-attr">rules</span>:&#123;
            <span class="hljs-attr">text</span>:<span class="hljs-string">'正则表达式'</span>, <span class="hljs-comment">// 处理匹配到的文件</span>
            <span class="hljs-attr">exclude</span>:<span class="hljs-string">""</span>, <span class="hljs-comment">// 处理没有匹配到的文件</span>
            <span class="hljs-attr">exclude</span>: <span class="hljs-regexp">/node_modules/</span>, <span class="hljs-comment">// 排除node_modules文件下的文件</span>
            use:[ <span class="hljs-comment">// 执行顺序从下到上 从右到左</span>
                <span class="hljs-string">'css-loader'</span>,
                &#123; <span class="hljs-comment">// 要对某一个loader进行详情配置时</span>
                   <span class="hljs-attr">loader</span>:<span class="hljs-string">"postcss-loader"</span>,
                   <span class="hljs-attr">options</span>:&#123; 
                     
                   &#125;
                &#125;
            ], <span class="hljs-comment">// 使用个loader时使用这个属性</span>
            <span class="hljs-attr">loader</span>:<span class="hljs-string">""</span>, <span class="hljs-comment">// 假如只用到一个loader时可以用这个</span>
            <span class="hljs-attr">enforce</span>:<span class="hljs-string">"pre"</span>, <span class="hljs-comment">// 如果有多个loader同时处理这个表示先执行这个loader</span>
            <span class="hljs-comment">// 只有一个loader时就可以直接使用options对其进行配置</span>
            <span class="hljs-attr">options</span>:&#123;
            &#125;
            
        &#125;
    &#125;, <span class="hljs-comment">// 加载不同格式文件的方式</span>
    <span class="hljs-attr">plugins</span>:[], <span class="hljs-comment">// 加载不同的插件</span>
    <span class="hljs-attr">mode</span>:<span class="hljs-string">""</span>, <span class="hljs-comment">// 环境 (development || production)</span>
    <span class="hljs-comment">// 这个是用来生成临时文件的服务</span>
    <span class="hljs-comment">// 需要安装webpack-dev-server</span>
    <span class="hljs-comment">// 命令：npm i webpack-dev-server -D</span>
    <span class="hljs-comment">// 开发服务器devserver：用来自动化</span>
    <span class="hljs-comment">// 特点：只会在内存中编译打包 不会有任何输出</span>
    <span class="hljs-comment">// 启动devServer指令为：npx webpack-dev-server</span>
    <span class="hljs-attr">devServer</span>:&#123;
        <span class="hljs-attr">contentBase</span>:resolve(__dirname, <span class="hljs-string">'built'</span>),
        <span class="hljs-comment">// 启动GZIP压缩</span>
        <span class="hljs-attr">compress</span>:<span class="hljs-literal">true</span>,
        <span class="hljs-comment">// 端口号</span>
        <span class="hljs-attr">port</span>:<span class="hljs-number">3000</span>,
        <span class="hljs-comment">// 自动打开浏览器</span>
        <span class="hljs-attr">open</span>:<span class="hljs-literal">true</span>
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>下面有打包<code>css</code> <code>less</code> <code>html</code> <code>字体文件</code> <code>图片</code></p>
<h4 data-id="heading-1">css所需loader</h4>
<p>style-loader、css-loader</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-built_in">module</span>: &#123;
    <span class="hljs-attr">rules</span>: [&#123;
        <span class="hljs-attr">test</span>: <span class="hljs-regexp">/\.css$/</span>,
        use: [
            <span class="hljs-string">'style-loader'</span>,
            <span class="hljs-string">'css-loader'</span>,
        ],
    &#125;,]
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-2">less所需loader</h4>
<p>要先安装less插件
style-loader、css-loader、less-loader</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-built_in">module</span>: &#123;
    <span class="hljs-attr">rules</span>: [&#123;
        <span class="hljs-attr">test</span>: <span class="hljs-regexp">/\.css$/</span>,
        use: [
            <span class="hljs-string">'style-loader'</span>,
            <span class="hljs-string">'css-loader'</span>,
            <span class="hljs-string">'less-loader'</span>,
        ],
    &#125;,]
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-3">字体文件和图片所需loader</h4>
<p>file-loader、url-loader</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-built_in">module</span>: &#123;
    <span class="hljs-attr">rules</span>: [
            &#123;
                <span class="hljs-attr">test</span>: <span class="hljs-regexp">/\.(jpg|png|gif|jpe1g)$/</span>,
                use: [&#123;
                    <span class="hljs-attr">loader</span>: <span class="hljs-string">"file-loader"</span>,
                    <span class="hljs-attr">options</span>: &#123;
                    <span class="hljs-comment">// 图片小于8kb 就会被base64处理</span>
                    <span class="hljs-comment">// 优点：能减少请求数量</span>
                    <span class="hljs-comment">// 确定：图片体积会更大</span>
                    <span class="hljs-attr">limit</span>:<span class="hljs-number">102400</span>,
                    <span class="hljs-comment">//  解析时出现[object Module]时配置esModule: false</span>
                    <span class="hljs-comment">// name: utils.assetsPath('img/[name].[hash:7].[ext]'),</span>
                    <span class="hljs-comment">// outputPath: "media/" 可以将文件输出到某个固定的目录</span>
                &#125;
            &#125;,
            &#123;
                <span class="hljs-comment">// exclude:/\.(css|js|html|jpg|png|gif|jpeg)$/, 这里是指排除这几种格式的文件</span>
                <span class="hljs-attr">test</span>: <span class="hljs-regexp">/\.ttf$/</span>,
                use: [&#123;
                    <span class="hljs-attr">loader</span>: <span class="hljs-string">"file-loader"</span>,
                    <span class="hljs-attr">options</span>: &#123;
                        <span class="hljs-attr">name</span>: <span class="hljs-string">"[hash:4].[ext]"</span>,
                        <span class="hljs-attr">outputPath</span>: <span class="hljs-string">"media/"</span>
                    &#125;
                &#125;]

            &#125;
        ],
   &#125;,]
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-4">html所需loader</h4>
<p>html-loader</p>
<h3 data-id="heading-5">以某个html文件为模板输出</h3>
<p><code>html-webpack-plugin</code></p>
<pre><code class="hljs language-js copyable" lang="js">npm i html-webpack-plugin -D
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> HtmlWebpackPlugin = <span class="hljs-built_in">require</span>(<span class="hljs-string">"html-webpack-plugin"</span>)
<span class="hljs-attr">plugins</span>:[
  <span class="hljs-keyword">new</span> HtmlWebpackPlugin(&#123;
            <span class="hljs-attr">template</span>: <span class="hljs-string">"./index.html"</span>,
            <span class="hljs-attr">minify</span>:&#123;
                <span class="hljs-comment">// 移除空格</span>
                <span class="hljs-attr">collapseWhitespace</span>:<span class="hljs-literal">true</span>,
                <span class="hljs-comment">// 移除注释</span>
                <span class="hljs-attr">removeComment</span>:<span class="hljs-literal">true</span>
            &#125;
        &#125;),
]
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-6">提取css成单独文件</h3>
<p>一般在打包之后css会被直接混入js文件通过这个插件可以让css单独输出出来
<code>mini-css-extract-plugin</code></p>
<pre><code class="hljs language-js copyable" lang="js">npm i mini-css-extract-plugin -D
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> MiniCssExtractPlugin = <span class="hljs-built_in">require</span>(<span class="hljs-string">"mini-css-extract-plugin"</span>)
<span class="hljs-keyword">const</span> commonCssLoader = [
    MiniCssExtractPlugin.loader,
    <span class="hljs-string">'css-loader'</span>,
]
<span class="hljs-attr">module</span>: &#123;
    <span class="hljs-attr">rules</span>: [&#123;
            <span class="hljs-attr">test</span>: <span class="hljs-regexp">/\.css$/</span>,
            use: [
                ...commonCssLoader,
            ]
        &#125;,
        &#123;
            <span class="hljs-attr">test</span>: <span class="hljs-regexp">/\.less$/</span>,
            use: [
                ...commonCssLoader,
                <span class="hljs-string">'less-loader'</span>,

            ]
        &#125;,
    &#125;
&#125;,
<span class="hljs-attr">plugins</span>:[
    <span class="hljs-keyword">new</span> MiniCssExtractPlugin(&#123;
        <span class="hljs-comment">// 对输出的文件重命名</span>
        <span class="hljs-attr">filename</span>:<span class="hljs-string">"css/built.css"</span>,
    &#125;)
]
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-7">css兼容</h3>
<p><code>npm i postcss-loader postcss-preset-env -D</code></p>
<p>帮 postcss找到package.json中browserslist里面的配置，通过配置加载指定的css兼容性样式</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> commonCssLoader = [
    MiniCssExtractPlugin.loader,
    <span class="hljs-string">'css-loader'</span>,
    <span class="hljs-comment">// css兼容性 需要在package.json中定义browserslist</span>
    <span class="hljs-comment">/*
    "browserslist": &#123;
        "development": [
          "last 1 chrome vesion",
          "last 1 firefox vesion",
          "last 1 safari vesion"
        ],
        "production": [
          ">0.2%",
          "not dead",
          "not op_mini all"
        ]
      &#125;*/</span>
    &#123;
        <span class="hljs-attr">loader</span>: <span class="hljs-string">"postcss-loader"</span>,
        <span class="hljs-attr">options</span>: &#123;
            <span class="hljs-attr">postcssOptions</span>: &#123;
                <span class="hljs-attr">plugins</span>: [
                    [
                        <span class="hljs-string">'postcss-preset-env'</span>,
                        &#123;
                            <span class="hljs-attr">ident</span>: <span class="hljs-string">"postcss"</span>
                        &#125;,
                    ],
                ],
            &#125;
        &#125;
    &#125;
]
<span class="hljs-attr">rules</span>: [&#123;
    <span class="hljs-attr">test</span>: <span class="hljs-regexp">/\.css$/</span>,
    use: [
        ...commonCssLoader,
    ]
&#125;,
&#123;
    <span class="hljs-attr">test</span>: <span class="hljs-regexp">/\.less$/</span>,
    use: [
        ...commonCssLoader,
        <span class="hljs-string">'less-loader'</span>,

    ]
&#125;,]
<span class="copy-code-btn">复制代码</span></code></pre>
<h5 data-id="heading-8">package.json</h5>
<pre><code class="hljs language-json copyable" lang="json"><span class="hljs-string">"browserslist"</span>:&#123;
    <span class="hljs-comment">// 设置nodejs环境变量;</span>
    <span class="hljs-comment">// process.env.NODE_ENV = 'devlopment';</span>
    <span class="hljs-comment">// 开发环境 =》 设置node环境变量： process.env.NODE_ENV = devlopment</span>
    <span class="hljs-attr">"development"</span>:[
        <span class="hljs-string">"last 1 chrome vesion"</span>, <span class="hljs-comment">//兼容最近的一个chrome</span>
        <span class="hljs-string">"last 1 firefox vesion"</span>, <span class="hljs-comment">//兼容最近的一个firefox</span>
        <span class="hljs-string">"last 1 safari vesion"</span>, <span class="hljs-comment">//兼容最近的一个safari</span>
    ],
    <span class="hljs-attr">"production"</span>:[
        <span class="hljs-string">">0.2%"</span>,
        <span class="hljs-string">"not dead"</span>,
        <span class="hljs-string">"not op_mini all"</span>
    ]
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-9">压缩css</h3>
<p><code>optimize-css-assets-webpack-plugin</code></p>
<pre><code class="hljs language-js copyable" lang="js">npm i optimize-css-assets-webpack-plugin -D
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> optimizeCssAssetsWebpackPlugin = <span class="hljs-built_in">require</span>(<span class="hljs-string">"optimize-css-assets-webpack-plugin"</span>)
<span class="hljs-attr">plugins</span>:[
  <span class="hljs-keyword">new</span> optimizeCssAssetsWebpackPlugin()
]
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-10">js兼容性处理</h3>
<p>1、 js兼容性处理：babel-loader @babel/preset-env @babel/core
还是不支持 promise</p>
<p>2、 全部js兼容性处理 -->  @babel/polyfill
使用方式 import "@babel/polyfill"</p>
<p>3、 需求做兼容性处理的就做 ： 按需处理 --》 core-js</p>
<p>使用之后就可以把上面import "@babel/polyfill"删掉了
一般是1和3结合使用
<code>babel-loader @babel/preset-env @babel/core @babel/polyfill</code></p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-built_in">module</span>:&#123;
        <span class="hljs-attr">rules</span>:[
            &#123;
                <span class="hljs-attr">test</span>:<span class="hljs-regexp">/\.js$/</span>,
                exclude:<span class="hljs-regexp">/node_modules/</span>,
                loader:<span class="hljs-string">"babel-loader"</span>,
                options：&#123;
                    <span class="hljs-comment">// 预设：指示babel做怎么样的兼容性处理</span>
                    <span class="hljs-comment">// presets:['@babel/preset-env']</span>
                    <span class="hljs-attr">presets</span>:[
                       [
                            <span class="hljs-string">'@babel/preset-env'</span>,
                            &#123;
                                <span class="hljs-comment">// 按需加载</span>
                                <span class="hljs-attr">useBuiltIns</span>: <span class="hljs-string">'usage'</span>,
                                <span class="hljs-comment">// 指定core-js版本</span>
                                <span class="hljs-attr">corejs</span>: &#123;
                                    <span class="hljs-attr">version</span>: <span class="hljs-number">3</span>
                                &#125;,
                                <span class="hljs-attr">targets</span>: &#123;
                                    <span class="hljs-attr">chrome</span>: <span class="hljs-string">"60"</span>,
                                    <span class="hljs-attr">firebox</span>: <span class="hljs-string">"60"</span>,
                                    <span class="hljs-attr">ie</span>:<span class="hljs-string">'9'</span>,
                                    <span class="hljs-attr">safari</span>: <span class="hljs-string">'10'</span>
                                &#125;
                            &#125;
                        ]
                    ]
                &#125;
            &#125;
        ]
    &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-11">js 设置 eslint语法校验 使用 airbnb</h4>
<p>所需插件
<code>eslint eslint-config-airbnb-base eslint-loader eslint-plugin-import</code></p>
<pre><code class="hljs language-js copyable" lang="js">&#123;
    <span class="hljs-attr">test</span>: <span class="hljs-regexp">/\.js$/</span>,
    exclude: <span class="hljs-regexp">/node_modules/</span>,
    <span class="hljs-comment">// 优先执行</span>
    enforce: <span class="hljs-string">"pre"</span>,
    <span class="hljs-attr">loader</span>: <span class="hljs-string">"eslint-loader"</span>,
    <span class="hljs-attr">options</span>: &#123;
        <span class="hljs-comment">// 对js语法规范自动修复</span>
        <span class="hljs-attr">fix</span>: <span class="hljs-literal">true</span>
    &#125;
&#125;,
<span class="copy-code-btn">复制代码</span></code></pre>
<p>在package.json中添加</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-string">"eslintConfig"</span>: &#123;
    <span class="hljs-string">"extends"</span>: <span class="hljs-string">"airbnb-base"</span>
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-12">完整文件</h3>
<pre><code class="hljs language-js copyable" lang="js">&#123;
    <span class="hljs-attr">test</span>: <span class="hljs-regexp">/\.html$/</span>,
    <span class="hljs-comment">// 处理html文件中img图片</span>
    loader: <span class="hljs-string">"html-loader"</span>
&#125;,
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> &#123;
    resolve
&#125; = <span class="hljs-built_in">require</span>(<span class="hljs-string">"path"</span>);

process.env.NODE_ENV = <span class="hljs-string">'production'</span>; <span class="hljs-comment">// 打包的环境</span>


<span class="hljs-keyword">const</span> MiniCssExtractPlugin = <span class="hljs-built_in">require</span>(<span class="hljs-string">'mini-css-extract-plugin'</span>); <span class="hljs-comment">// 压缩css</span>

<span class="hljs-keyword">const</span> OptimizeCssAssetsWebpackPlugin = <span class="hljs-built_in">require</span>(<span class="hljs-string">"optimize-css-assets-webpack-plugin"</span>); <span class="hljs-comment">// css兼容性</span>

<span class="hljs-keyword">const</span> HtmlWebpackPlugin = <span class="hljs-built_in">require</span>(<span class="hljs-string">"html-webpack-plugin"</span>); <span class="hljs-comment">// html插件</span>

<span class="hljs-keyword">const</span> commonCssLoader = [
    MiniCssExtractPlugin.loader,
    <span class="hljs-string">'css-loader'</span>,
    <span class="hljs-comment">// css兼容性 需要在package.json中定义browserslist</span>
    <span class="hljs-comment">/*
    "browserslist": &#123;
        "development": [
          "last 1 chrome vesion",
          "last 1 firefox vesion",
          "last 1 safari vesion"
        ],
        "production": [
          ">0.2%",
          "not dead",
          "not op_mini all"
        ]
      &#125;*/</span>
    &#123;
        <span class="hljs-attr">loader</span>: <span class="hljs-string">"postcss-loader"</span>,
        <span class="hljs-attr">options</span>: &#123;
            <span class="hljs-attr">postcssOptions</span>: &#123;
                <span class="hljs-attr">plugins</span>: [
                    [
                        <span class="hljs-string">'postcss-preset-env'</span>,
                        &#123;
                            <span class="hljs-attr">ident</span>: <span class="hljs-string">"postcss"</span>
                        &#125;,
                    ],
                ],
            &#125;
        &#125;
    &#125;
]
<span class="hljs-built_in">module</span>.exports = &#123;
    <span class="hljs-attr">entry</span>: <span class="hljs-string">'./index.js'</span>,
    <span class="hljs-attr">output</span>: &#123;
        <span class="hljs-attr">filename</span>: <span class="hljs-string">'js/built.js'</span>,
        <span class="hljs-attr">path</span>: resolve(__dirname, <span class="hljs-string">'built'</span>)
    &#125;,
    <span class="hljs-attr">module</span>: &#123;
        <span class="hljs-attr">rules</span>: [&#123;
                <span class="hljs-attr">test</span>: <span class="hljs-regexp">/\.css$/</span>,
                use: [
                    ...commonCssLoader,
                ]
            &#125;,
            &#123;
                <span class="hljs-attr">test</span>: <span class="hljs-regexp">/\.less$/</span>,
                use: [
                    ...commonCssLoader,
                    <span class="hljs-string">'less-loader'</span>,

                ]
            &#125;,
            <span class="hljs-comment">/*
                正常来说 一个文件只能被一个loader处理
                当一个文件要被多个loader处理,那么一定要制定loader执行的先后顺序
                先执行eslint 再执行babel
                可以对其中一个loader添加一个属性 enforce:"pre"
            */</span>
            <span class="hljs-comment">// js 设置 eslint语法校验 使用 airbnb</span>
            <span class="hljs-comment">/*
            在package.json中添加
            "eslintConfig": &#123;
                "extends": "airbnb-base"
            &#125;
            */</span>
            <span class="hljs-comment">// &#123;</span>
            <span class="hljs-comment">//     test: /\.js$/,</span>
            <span class="hljs-comment">//     exclude: /node_modules/,</span>
            <span class="hljs-comment">//     // 优先执行</span>
            <span class="hljs-comment">//     enforce: "pre",</span>
            <span class="hljs-comment">//     loader: "eslint-loader",</span>
            <span class="hljs-comment">//     options: &#123;</span>
            <span class="hljs-comment">//         // 对js语法规范自动修复</span>
            <span class="hljs-comment">//         fix: true</span>
            <span class="hljs-comment">//     &#125;</span>
            <span class="hljs-comment">// &#125;,</span>
            <span class="hljs-comment">// js兼容性处理</span>
            &#123;
                <span class="hljs-attr">test</span>: <span class="hljs-regexp">/\.js$/</span>,
                exclude: <span class="hljs-regexp">/node_modules/</span>,
                loader: <span class="hljs-string">"babel-loader"</span>,
                <span class="hljs-attr">options</span>: &#123;
                    <span class="hljs-attr">presets</span>: [
                        [
                            <span class="hljs-string">'@babel/preset-env'</span>,
                            <span class="hljs-comment">// 1、兼容部分语法 不包括promise</span>
                            <span class="hljs-comment">// 2、全部js兼容性处理 -->  @babel/polyfill  使用方式 import "@babel/polyfill"</span>
                            <span class="hljs-comment">// 3、 需求做兼容性处理的就做 ： 按需处理 --》 core-js 使用之后就可以把上面import "@babel/polyfill"删掉了</span>
                            <span class="hljs-comment">// 这里用的是1和3</span>
                            &#123;
                                <span class="hljs-comment">// 按需加载</span>
                                <span class="hljs-attr">useBuiltIns</span>: <span class="hljs-string">'usage'</span>,
                                <span class="hljs-comment">// 指定core-js版本</span>
                                <span class="hljs-attr">corejs</span>: &#123;
                                    <span class="hljs-attr">version</span>: <span class="hljs-number">3</span>
                                &#125;,
                                <span class="hljs-attr">targets</span>: &#123;
                                    <span class="hljs-attr">chrome</span>: <span class="hljs-string">"60"</span>,
                                    <span class="hljs-attr">firefox</span>: <span class="hljs-string">"60"</span>,
                                    <span class="hljs-attr">ie</span>: <span class="hljs-string">'9'</span>,
                                    <span class="hljs-attr">safari</span>: <span class="hljs-string">'10'</span>,
                                    <span class="hljs-attr">edge</span>: <span class="hljs-string">'17'</span>
                                &#125;
                            &#125;
                        ]

                    ]

                &#125;
            &#125;,
            <span class="hljs-comment">// &#123;</span>
            <span class="hljs-comment">//     test: /\.(jpg|png|gif|jpeg)$/,</span>
            <span class="hljs-comment">//     loader: 'url-loader',</span>
            <span class="hljs-comment">//     options: &#123;</span>
            <span class="hljs-comment">//         limit: 8 * 1024,</span>
            <span class="hljs-comment">//         name: "[hash:10].[ext]", // 图片名称</span>
            <span class="hljs-comment">//         outputPath: 'imgs', // 图片输出的目录</span>
            <span class="hljs-comment">//         esModule: false, // 防止html中直接引用的图片链接错误</span>
            <span class="hljs-comment">//     &#125;</span>
            <span class="hljs-comment">// &#125;,</span>
            &#123;
                <span class="hljs-attr">test</span>: <span class="hljs-regexp">/\.html$/</span>,
                loader: <span class="hljs-string">"html-loader"</span>,
            &#125;,
            <span class="hljs-comment">// &#123;</span>
            <span class="hljs-comment">//     exclude: /\.(jpg|png|gif|jpeg|html|js|less|css)$/,</span>
            <span class="hljs-comment">//     loader: 'file-loader',</span>
            <span class="hljs-comment">//     options: &#123;</span>
            <span class="hljs-comment">//         outputPath: 'media', // 这些文件的输出目录</span>
            <span class="hljs-comment">//     &#125;</span>
            <span class="hljs-comment">// &#125;</span>
        ]
    &#125;,
    <span class="hljs-attr">plugins</span>: [
        <span class="hljs-keyword">new</span> MiniCssExtractPlugin(&#123;
            <span class="hljs-attr">filename</span>: <span class="hljs-string">"css/built.css"</span>, <span class="hljs-comment">// 将css从js中抽离出来</span>
        &#125;),
        <span class="hljs-keyword">new</span> OptimizeCssAssetsWebpackPlugin(), <span class="hljs-comment">// 压缩css</span>
        <span class="hljs-keyword">new</span> HtmlWebpackPlugin(&#123;
            <span class="hljs-attr">template</span>: <span class="hljs-string">"./index.html"</span>, <span class="hljs-comment">// 输出的模板文件</span>
            <span class="hljs-attr">minify</span>: &#123;
                <span class="hljs-comment">// 压缩html</span>
                <span class="hljs-attr">collapseBooleanAttributes</span>: <span class="hljs-literal">true</span>,
                <span class="hljs-comment">// 去除注释</span>
                <span class="hljs-attr">removeComments</span>: <span class="hljs-literal">true</span>,
            &#125;
        &#125;)
    ],
    <span class="hljs-attr">mode</span>: <span class="hljs-string">"production"</span>
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-13">package.json</h3>
<pre><code class="hljs language-json copyable" lang="json">&#123;
  <span class="hljs-attr">"name"</span>: <span class="hljs-string">"webpackcs"</span>,
  <span class="hljs-attr">"version"</span>: <span class="hljs-string">"1.0.0"</span>,
  <span class="hljs-attr">"description"</span>: <span class="hljs-string">""</span>,
  <span class="hljs-attr">"main"</span>: <span class="hljs-string">"index.js"</span>,
  <span class="hljs-attr">"scripts"</span>: &#123;
    <span class="hljs-attr">"test"</span>: <span class="hljs-string">"echo \"Error: no test specified\" && exit 1"</span>
  &#125;,
  <span class="hljs-attr">"keywords"</span>: [],
  <span class="hljs-attr">"author"</span>: <span class="hljs-string">""</span>,
  <span class="hljs-attr">"license"</span>: <span class="hljs-string">"ISC"</span>,
  <span class="hljs-attr">"dependencies"</span>: &#123;
    <span class="hljs-attr">"jquery"</span>: <span class="hljs-string">"^3.6.0"</span>
  &#125;,
  <span class="hljs-attr">"devDependencies"</span>: &#123;
    <span class="hljs-attr">"@babel/core"</span>: <span class="hljs-string">"^7.14.8"</span>,
    <span class="hljs-attr">"@babel/preset-env"</span>: <span class="hljs-string">"^7.14.8"</span>,
    <span class="hljs-attr">"babel-loader"</span>: <span class="hljs-string">"^8.2.2"</span>,
    <span class="hljs-attr">"css-loader"</span>: <span class="hljs-string">"^6.0.0"</span>,
    <span class="hljs-attr">"eslint"</span>: <span class="hljs-string">"^7.31.0"</span>,
    <span class="hljs-attr">"eslint-config-airbnb-base"</span>: <span class="hljs-string">"^14.2.1"</span>,
    <span class="hljs-attr">"eslint-loader"</span>: <span class="hljs-string">"^4.0.2"</span>,
    <span class="hljs-attr">"eslint-plugin-import"</span>: <span class="hljs-string">"^2.23.4"</span>,
    <span class="hljs-attr">"file-loader"</span>: <span class="hljs-string">"^6.2.0"</span>,
    <span class="hljs-attr">"html-loader"</span>: <span class="hljs-string">"^2.1.2"</span>,
    <span class="hljs-attr">"html-webpack-plugin"</span>: <span class="hljs-string">"^5.3.2"</span>,
    <span class="hljs-attr">"less"</span>: <span class="hljs-string">"^4.1.1"</span>,
    <span class="hljs-attr">"less-loader"</span>: <span class="hljs-string">"^10.0.1"</span>,
    <span class="hljs-attr">"mini-css-extract-plugin"</span>: <span class="hljs-string">"^2.1.0"</span>,
    <span class="hljs-attr">"optimize-css-assets-webpack-plugin"</span>: <span class="hljs-string">"^6.0.1"</span>,
    <span class="hljs-attr">"postcss-loader"</span>: <span class="hljs-string">"^6.1.1"</span>,
    <span class="hljs-attr">"postcss-preset-env"</span>: <span class="hljs-string">"^6.7.0"</span>,
    <span class="hljs-attr">"style-loader"</span>: <span class="hljs-string">"^3.1.0"</span>,
    <span class="hljs-attr">"webpack"</span>: <span class="hljs-string">"^5.44.0"</span>,
    <span class="hljs-attr">"webpack-cli"</span>: <span class="hljs-string">"^3.3.12"</span>,
    <span class="hljs-attr">"webpack-dev-server"</span>: <span class="hljs-string">"^3.11.2"</span>
  &#125;,
  <span class="hljs-attr">"browserslist"</span>: &#123;
    <span class="hljs-attr">"development"</span>: [
      <span class="hljs-string">"last 1 chrome vesion"</span>,
      <span class="hljs-string">"last 1 firefox vesion"</span>,
      <span class="hljs-string">"last 1 safari vesion"</span>
    ],
    <span class="hljs-attr">"production"</span>: [
      <span class="hljs-string">">0.2%"</span>,
      <span class="hljs-string">"not dead"</span>,
      <span class="hljs-string">"not op_mini all"</span>
    ]
  &#125;
&#125;,
<span class="hljs-string">"eslintConfig"</span>: &#123;
    <span class="hljs-attr">"extends"</span>: <span class="hljs-string">"airbnb-base"</span>
&#125;

<span class="copy-code-btn">复制代码</span></code></pre></div>  
</div>
            