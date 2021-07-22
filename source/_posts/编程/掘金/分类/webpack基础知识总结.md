
---
title: 'webpack基础知识总结'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/9512a732b5884b5eaa36e2e2825eafd2~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Thu, 22 Jul 2021 02:12:07 GMT
thumbnail: 'https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/9512a732b5884b5eaa36e2e2825eafd2~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h2 data-id="heading-0">什么是webpack？</h2>
<p>Webpack 是一个前端资源加载/打包工具。它将根据模块的依赖关系进行静态分析，然后将这些模块按照指定的规则生成对应的静态资源。
<img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/9512a732b5884b5eaa36e2e2825eafd2~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-1">为什么要使用webpack？</h2>
<p>现在很多网页都可以看做是功能丰富发应用，它们拥有复杂的JavaScript代码和一大堆依赖包。为了简化开发的复杂度，前端做了很多很好的尝试：</p>
<ul>
<li>模块化，把复杂的程序细化为小的模块；</li>
<li>在JavaScript基础上拓展的轻量级开发语言--TypeScript</li>
<li>Scss，less等CSS预处理器</li>
<li>...</li>
</ul>
<p>这些尝试都大大提高了前端的开发效率，但是这些文件往往需要进行额外的处理才能让浏览器识别，手动处理非常繁琐，而webpack类打包工具的出现正好可以解决上述问题。</p>
<h2 data-id="heading-2">开始使用webpack</h2>
<p>webpack可以在终端中使用，其基本的使用方法如下：</p>
<pre><code class="copyable">webpack &#123;entry file&#125; &#123;destination for bundled file&#125; 
//entry file:写入口文件的路径 
//destination for bundled file:填写打包文件的存放路径
<span class="copy-code-btn">复制代码</span></code></pre>
<p>Webpack拥有很多其它的比较高级的功能（比如<code>loaders</code>和<code>plugins</code>），这些功能其实都可以通过命令行模式实现，不过在终端中进行复杂的操作，其实不太方便且容易出错的，更好的办法就是定义一个配置文件，我们可以在跟目录下新建一个webpack.config.js的文件，我们可以把所有和打包相关的配置都放在这个文件里面。</p>
<pre><code class="copyable">var webpack=require('webpack'); 
    module.exports = &#123; entry: __dirname + "/app/main.js",//入口文件 
    output: &#123; 
        path: __dirname + "/public",//打包后的文件存放的地方 
        filename: "bundle.js"//打包后输出文件的文件名 
    &#125;, 
    mode: development, 
    module: &#123; 
        rules: [ &#123; test: /\.css$/, use: ["style-loader","css-loader"] &#125; ] 
    &#125;, 
    plugins:[ new webpack.BannerPlugin('webpack 实例')//版权声明插件 ] 
    &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>entry：用来指定webpack的依赖入口，entry可以是一个字符串（单入口文件），也可以是一个对象（多入口文件）</p>
<pre><code class="copyable">//单个入口 
const config = &#123; 
    entry: &#123; 
        main: './path/to/my/entry/file.js'
     &#125; 
&#125;;
//多个入口 
const config = &#123; 
    entry: &#123; 
        app: './src/app.js', 
        vendors: './src/vendors.js' 
    &#125;, 
    output: &#123; 
        filename: '[name].js', //使用name占位符 
        path: __dirname + '/dist' 
   &#125; 
&#125;;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>output：用来告诉webpack如何将编辑后的文件输出到磁盘。output中的path表示输出文件的存放路径，filename表示输出的文件名称。多个入口文件时，输出文件名可使用[name]占位符。</p>
<p>接下来我们在命令行输入webpack（非全局安装时使用 nodemodules/.bin/webpack）就可以了，这个命令会自动引用webpack.config.js文件里的配置。</p>
<h2 data-id="heading-3">babel</h2>
<p>webpack原始支持JavaScript的解析，但是对于ES6的语法，webpack原生并不支持，因此需要借助babel-loader来解析ES6语法。</p>
<p>babel-loader的使用：</p>
<pre><code class="copyable">module: &#123; 
    rules: [ 
        &#123; test: /\.js$/, loader: "babel-loader" &#125; 
    ]
&#125;,
<span class="copy-code-btn">复制代码</span></code></pre>
<p>babel-loader是依赖babel的，因此需要在项目中使用babel的配置文件.babelrc文件。Babel其实是一个编译JavaScript的平台，它可以编译代码帮我们达到一下目的：</p>
<ul>
<li>让我们能使用最新的JavaScript代码（ES6，ES7...），而不用管新标准是否被当前使用的浏览器完全支持；</li>
<li>让我们能使用基于JavaScript进行了拓展的语言，比如React的JSX</li>
</ul>
<p>babel中两个比较重要的概念：presets和plugins，可以理解为一个plugins对应一个功能，然后presets是一系列babel plugins的集合。这里我们需要支持ES6的语法，因此我们需要在.babelrc文件里增加babel的presets配置@babel/preset-env。(@babel/preset-env是一系列插件的集合，包含了我们在babel6中常用的es2015、es2016、es2017等最新的语法转化插件，允许我们使用最新的js语法，比如 let，const，箭头函数等等)。同理，如果需要支持react语法的解析，我们也需要在.babelrc文件里增加babel的presets配置@babel/preset-react。</p>
<pre><code class="copyable">&#123;
    "presets": [ 
        "@babel/preset-env",//解析ES6语法 
        "@babel/preset-react" //解析react JSX语法 
     ],
    "plugins":[
        "@babel/proposal-class-properties"//用来编译类 
    ] 
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-4">loaders</h2>
<p>webpack开箱即用只支持JS和JSON两种文件类型，通过loaders去支持其他文件类型并且把它们转化成有效的模块，并且可以添加到依赖中去。</p>
<p>loaders本身是一个函数，接受源文件作为参数，返回转换后的结果。</p>
<p>webpack中常用的loaders：
<img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/7cf97d17e2d04ebdb25681a3a783ba9c~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer">
loaders的用法：test用于指定匹配规则，use指定使用的loader名称</p>
<h3 data-id="heading-5">解析CSS</h3>
<p>在webpack中解析CSS，需要首先使用css-loader，勇于加载.css文件，并且转换成CommonJS对象，然后使用style-loader将样式通过<code><style></code>标签插入到head中。二者组合在一起使你能够把样式表嵌入webpack打包后的JS文件中。注意：loader的调用是链式调用，执行顺序是从右到左的，因此需要先写style-loader，然后写css-loader，这样执行的时候会先使用css-loader去解析CSS文件，然后将内容传递给style-loader。</p>
<pre><code class="copyable">module: &#123; 
    rules: [ 
        &#123; test: /\.less$/, use: ["style-loader","css-loader" &#125; 
    ]
&#125;,
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-6">解析less</h3>
<p>webpack想要解析less，只需在解析CSS的基础上首先使用less-loader将less转换成CSS。</p>
<pre><code class="copyable">module: &#123; 
    rules: [ 
        &#123; test: /\.less$/, use: ["style-loader","css-loader","less-loader"] &#125; 
    ]
&#125;,
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-7">解析图片和字体</h3>
<p>使用file-loader处理图片（png/jpeg/jpg/gif）和字体。url-loader也可以处理图片和字体，和file-loader相比，url-loader还可以设置较小资源自动做base64的转换</p>
<pre><code class="copyable">module: &#123; 
    rules: [ 
        &#123; test: /\.(png|jpeg|jpg|gif)$/, use: ["file-loader"] &#125;,//解析图片
        &#123; test: /\.(woff|woff2|eot|ttf|otf)$/, use: ["file-loader"] &#125;//解析字体
        &#123; 
            test: /\.(png|jpeg|jpg|gif)$/, //使用url-loader解析图片 
            use: [&#123;
                    loader: "file-loader",
                    options: &#123;
                        limit: 10240 // 图片大小小于10K时，webpack打包时会自动base64 
                        &#125;
                &#125;]
        &#125;
    ]
&#125;,
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-8">plugins</h2>
<p>插件是用来拓展Webpack功能的，它们会在整个构建过程中生效，执行相关的任务。Loaders和Plugins常常被弄混，但是他们其实是完全不同的东西，loaders是在打包构建过程中用来处理源文件的（JSX，Scss，Less..），一次处理一个，插件并不直接操作单个文件，它直接对整个构建过程其作用。插件主要是用于打包生成的bundle文件的优化、资源管理、环境变量注入等，作用于整个构建过程。任何loader无法做到的事情，都可以通过plugins去完成，比如每次构建前手动的去删除dist目录，这些都可以通过plugins去完成。</p>
<p>webpack常见的插件：
<img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/1242b3d4e33346cba9bb690a5fd341ab~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer">
plugins的用法：在webpack.config.js文件中的plugins数组中加入我们定义好的插件即可。</p>
<h3 data-id="heading-9">清除构建目录</h3>
<p>在webpack中每次构建都会产生一个构建的文件夹，在开发过程中可以使用命令 rm rf ./dist && webpack / dimraf ./dist && webpack来清除构建目录。更加优雅的解决办法是可以使用webpack的插件：clean webpack-plugin，默认会删除output指定的目录，避免构建前每次都需要手动删除dist</p>
<pre><code class="copyable">const CleanWebpackPlugin = require('clean webpack-plugin');
module.export = &#123; 
    plugin: [ 
            new CleanWebpackPlugin(), 
        ] 
&#125;,
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-10">CSS特性增强</h3>
<ul>
<li>使用PostCSS插件autoprefixer自动补齐CSS前缀</li>
</ul>
<p>由于浏览器的标准并没有完全统一，目前来看还是有四大内核：Trident（-ms)，Geko(-moz)，Webkit(-webkit)，Presto(-o)。</p>
<pre><code class="copyable">.box&#123;
    -moz-border-radius: 10px; 
    -webkit-border-radius: 10px; 
    -o-border-radius: 10px; 
    border-radius: 10px;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>如何在编写CSS不需要添加前缀？使用autoprefixer后置处理插件，可在css-loader前置处理完CSS文件后，给CSS属性添加前缀。</p>
<pre><code class="copyable">module: &#123; 
    rules: [ 
        &#123; 
            test: /\.less$/, 
            use: [
                'style-loader',
                'css-loader', 
                'less-loader',
                &#123;
                    loader: 'postcss-loader',
                    options: &#123;
                        plugins:()=>&#123; 
                            require('autoprefixer')(&#123; 
                                browsers: ['last 2 version','>1%','IOS 7'] 
                             &#125;) 
                          &#125;
                     &#125;
                &#125;
            ]
        &#125;
    ]
&#125;,
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>移动端CSS  px自动转换成rem</li>
</ul>
<p>rem: font zise of ths root element。rem是相对单位，px是绝对单位。使用px2rem-loader可以将CSS px自动转换成rem</p>
<pre><code class="copyable">module: &#123; 
    rules: [ 
        &#123; 
            test: /\.less$/, 
            use: [
                'style-loader',
                'css-loader', 
                'less-loader',
                &#123;
                    loader: 'px2rem-loader',
                    options: &#123;
                        remUnit: 75, 
                        remPrecision: 8,
                     &#125;
                &#125;
            ]
        &#125;
    ]
&#125;,
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-11">mode</h2>
<p>mode用来指定当前的构建环境是production、development还是none。不同构建环境下，webpack会默认开启一些内置的函数，mode默认值为production。
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/a132688f390d49db84dff9673b05850f~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-12">文件监听</h2>
<p>webpack每次修改源代码后都需要手动的执行构建命令，这在开发中比较低效且浪费时间，因此在webpack做文件的自动编译十分必要。文件监听是在发现源码发生变化时，自动重新构建出新的输出文件。</p>
<p>webpack开启监听模式，有两种方式</p>
<ul>
<li>启动webpack命令是，带上 --watch 参数。</li>
<li>在配置webpack.config.js中设置 watch: true。</li>
</ul>
<p>文件监听的原理是webpack会轮询判断文件的最后编译时间是否变化。某个文件发生了变化，并不会立刻告诉监听者，而是先缓存起来，等待aggregateTimeout时间结束之后再变化的文件一起去构建。</p>
<pre><code class="copyable">module.export = &#123; 
    //默认为false，也就是不开启 
    watch: true, 
    //只有开启监听模式，watchOptions才有意义 
    watchOptions: &#123; 
        ignored: /node_modules/, // 默认为空，不监听的文件或文件夹，支持正则匹配 
        aggregateTimeout: 300, //监听到变化发生后等300ms再去执行编译，默认300ms 
        poll: 10000, // 判断文件是否发生变化时通过不停询问系统指定文件有没有变化实现的，默认每秒询问1000次 
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>唯一缺陷：每次需要手动刷新浏览器。不用刷新浏览器的方法——另一种是基于<code>WDS (Webpack-dev-server)</code>的模块热更新HRM（Hot Module Replacement），只需要局部刷新页面上发生变化的模块，同时可以保留当前的页面状态，比如复选框的选中状态、输入框的输入等。</p>
<p>在webpack中实现HMR也很简单，只需要做两项配置</p>
<ol>
<li>在webpack配置文件中添加HMR插件；</li>
<li>在Webpack Dev Server中添加“hot”参数；</li>
</ol>
<pre><code class="copyable">module.export = &#123; 
    devServer: &#123; 
        contentBase: "./public", //本地服务器所加载的页面所在的目录 
        historyApiFallback: true, //不跳转 
        inline: true, 
        hot: true 
    &#125;,
    plugins: [
        new webpack.HotModuleReplacementPlugin() //热加载插件
    ]
&#125;,
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-13">代码压缩</h2>
<p>JavaScript压缩：webpack4内置了uglifyjs-webpack-plugin插件，打包过程中会自动进行JS代码的压缩。</p>
<p>CSS压缩：使用optimize-css-assets-webpack-plugin进行CSS代码压缩，同时需要使用CSS预处理器：cssnano。</p>
<p>HTML压缩：使用html-webpack-plugin插件，设置压缩参数。</p>
<pre><code class="copyable">const OptimizeCssAssetsWebpackPlugin = require('optimize-css-assets-webpack-plugin');//CSS压缩
const HtmlWebpackPlugin = require('html-webpack-plugin');//HTML压缩

module.export = &#123; 
    plugin: [ 
            new OptimizeCssAssetsWebpackPlugin(&#123; 
                assetNameRegExp: /\.css$/g, 
                cssProcessor: require("cssnano") 
            &#125;), 
            new HtmlWebpackPlugin(&#123;
                template: path.join(__dirname, 'src/search.html',//打包模板路径 
                filename: 'search.html',//打包出的文件名称 
                chunks:['search'],
                inject: true,
                minify: &#123;
                    html5: true, 
                    collapseWhitespace: true, 
                    preserveLineBreaks: false, 
                    minifyCSS: true, 
                    minifyJS: true, 
                    removeComments false,
                &#125;
            &#125;),
        ] 
&#125;,
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-14">提取公共资源</h2>
<p>在一个项目里面，有很多页面，这些页面使用的基础库都是一样的，每个页面之间可能还有一些公共的模块，如果在打包的时候把所有的依赖都打一份，这样其实比较浪费，而且打包出来的体积比较大。在页面之间怎么做公共资源的分离。</p>
<p>首先是基础库的分离。开发中以react为例，项目中会经常用到react、react-dom等基础库，我们可以通过将react、react-dom基础包通过CDN引入，不打包到bundle文件中，可以大大减少打包文件的体积。当然也可以利用SplitChunksPlugin插件进行公共脚本分离。SplitChunksPlugin是webpack4中提供的功能特别强大的插件，替代CommonsChunksPlugin插件。</p>
<pre><code class="copyable">new webpack.optimize.SplitChunksPlugin(&#123; 
    chunks: "all", 
    minSize: 20000, 
    minChunks: 1, 
    maxAsyncRequests: 5,
    maxInitialRequests: 3, 
    name: true, 
    cacheGroups:&#123;
        test: /(react|react.dom)/,//分离基react，react-dom础包 
        name:'vendors',//分离出基础包的文件名 
        chunks:'all',
     &#125; 
&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>可以看到SplitChunksPlugin插件的参数十分复杂，侧面也反应了该插件的功能十分强大。重点说明一下chunks参数的设置。chunks：async(异步进入的库进行分离-默认值)/initial（同步引入的库进行分离）/all（所以引入的库进行分离-推荐用法）。</p>
<p>还可以利用SplitChunksPlugin来提取页面的公共文件。minChunks设置最小引用次数，minuSize设置分离的包体积的大小.</p>
<pre><code class="copyable">new webpack.optimize.SplitChunksPlugin(&#123; 
    cacheGroups:&#123; 
        minSize: 0, 
        commons: &#123; 
            name: 'commons', 
            chunks: 'all', 
            minChunks: 2, 
        &#125; 
    &#125; 
&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-15">提高webpack打包速度</h2>
<ul>
<li>使用高版本的webpack和node.js。软件在迭代的过程中会不断的提升性能</li>
<li>使用thread-loader开启多进程多实例构建。原理：每次webpack解析一个模块，thread-loader都会将它及它的依赖分配给worker线程。</li>
<li>并行压缩。使用parallel-uglify-plugin插件、uglify-webpack-plugin插件、terser-webpack-plugin插件（支持ES6语法）来开启parallel参数</li>
<li>利用缓存提升二次打包速度：1、babel-loader开启缓存；2、terser-webpack-plugin开启缓存；3、使用cache-loader或者hard-source-webpack-plugin</li>
<li>...</li>
</ul>
<h2 data-id="heading-16">总结</h2>
<p>本次就前两周对于webpack的学习进行了一次简单的知识点整理，内容还不是很全面，也有理解不深入的地方，希望在后续的学习中能不断加深对于webpack的掌握，同时累积更多实战经历。</p></div>  
</div>
            