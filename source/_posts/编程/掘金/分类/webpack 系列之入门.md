
---
title: 'webpack 系列之入门'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/61b2b2b8743846479339caba2d93f798~tplv-k3u1fbpfcp-zoom-1.image'
author: 掘金
comments: false
date: Sun, 25 Apr 2021 01:50:16 GMT
thumbnail: 'https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/61b2b2b8743846479339caba2d93f798~tplv-k3u1fbpfcp-zoom-1.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/61b2b2b8743846479339caba2d93f798~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-0">前言</h3>
<p>看了很多webpack相关文章，一直读不进去(或者记不住)，无非将<a href="https://webpack.docschina.org/concepts/" target="_blank" rel="nofollow noopener noreferrer">webpack官文档</a>的配置说明，重新梳理下顺序或者翻译不好部分的再重新处理一下。很少以项目角度去讨论一个webpack工程项目如何从0到1搭建，搭建完成之后随着项目的复杂度提高又是如何一步步优化，达到最佳实践过程。</p>
<p>本系列是基于以下webpack版本来展开的讨论的</p>
<pre><code class="copyable">    "webpack": "^4.46.0",
    "webpack-dev-server": "^3.11.2"
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-1">【一】 项目初始化</h3>
<p>新建一个文件夹<code>webpack-demo</code>，执行下面命令。</p>
<pre><code class="hljs language-bash copyable" lang="bash">npm init -y
npm install webpack webpack-cli -D
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-2">【二】 配置打包的输入(entry)与输出(output)</h3>
<p>在<code>src/index.js</code>路径下写点代码，配置webpack.config.js</p>
<pre><code class="copyable">module.exports = &#123;
    entry:'./src/index.js', // 输入输出
    output: &#123;
        path: path.resolve(__dirname, "./dist"), // 打包后的目录
        filename:"bundle.js"
    &#125;
&#125;  
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-3">【三】 配置构建命令</h3>
<p>1、 在 package.json scripts 添加构建打包命令</p>
<pre><code class="hljs language-json copyable" lang="json">scripts:&#123;
  <span class="hljs-attr">"build"</span>: <span class="hljs-string">"webpack --config webpack.config.js"</span>
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>2、<code>验证：</code> 终端执行打包命令<code>npm run build</code> 将会在dist目录下生成一个bundle.js文件。</p>
<h3 data-id="heading-4">【四】自动引入打包生成的文件bundle.js</h3>
<ol>
<li>安装依赖: <code>html-webpack-plugin</code>和<code>clean-webpack-plugin</code></li>
</ol>
<pre><code class="hljs language-bash copyable" lang="bash">npm i -D html-webpack-plugin clean-webpack-plugin
<span class="copy-code-btn">复制代码</span></code></pre>
<ol start="2">
<li>配置 webpack.config.js，以插件形式引入</li>
</ol>
<pre><code class="copyable">const HtmlWebpackPlugin = require("html-webpack-plugin");
const &#123; CleanWebpackPlugin &#125; = require("clean-webpack-plugin");

module.exports = &#123;
    // ... 省略其它配置项目
    plugins:[
        new CleanWebpackPlugin(&#123; // 每次打包前清空打包输出目录
            // cleanOnceBeforeBuildPatterns:['**/*', '!dll', '!dll/**'] // 不删除dll目录下的文件
        &#125;), // 清空打包输出目录
        new HtmlWebpackPlugin(&#123;
            template: './index.html' // 源模板文件
            // filename: './index.html' // 指定输出文件
        &#125;)
    ]
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<ol start="3">
<li><code>验证：</code> 终端执行命令<code>npm run build</code>将打包dist生成文件除了bundle.js，还有index.html 。这样打包之后bundle.js自动注入到<code>index.html</code></li>
</ol>
<h3 data-id="heading-5">【五】搭建本地服务器</h3>
<ol>
<li>安装依赖 <code>webpack-dev-server</code></li>
</ol>
<pre><code class="hljs language-bash copyable" lang="bash">npm i -D webpack-dev-server
<span class="copy-code-btn">复制代码</span></code></pre>
<p>2、配合服务启动目录、端口</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-built_in">module</span>.exports = &#123;
    <span class="hljs-comment">// ... 省略其它配置项目</span>
  <span class="hljs-attr">devServer</span>: &#123;
    <span class="hljs-attr">port</span>: <span class="hljs-number">3001</span>,
    <span class="hljs-attr">hot</span>: <span class="hljs-literal">true</span>,
    <span class="hljs-attr">contentBase</span>: <span class="hljs-string">"./dist"</span>,
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<ol start="3">
<li>在 package.json scripts 配置本地服务启动命令</li>
</ol>
<pre><code class="hljs language-json copyable" lang="json">   scripts:&#123;
    <span class="hljs-attr">"serve"</span>: <span class="hljs-string">"webpack-dev-server --config webpack.config.js --open"</span>
   &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>4、<code>验证：</code> 在终端执行<code>npm run serve</code>，会自动开口浏览器启动本地服务</p>
<h3 data-id="heading-6">【六】 配置解析和转换文件的策略 module</h3>
<p><strong>常见loader</strong></p>













































<table><thead><tr><th>loder</th><th>功能</th></tr></thead><tbody><tr><td>babel-loader</td><td>解析 .js 和 .jsx 文件</td></tr><tr><td>tsx-loader</td><td>处理 ts 文件</td></tr><tr><td>less-loader</td><td>处理 less 文件，并将其编译为 css</td></tr><tr><td>sass-loader</td><td>处理 sass、scss 文件，并将其编译为 css</td></tr><tr><td>css-loader</td><td>处理 css 文件</td></tr><tr><td>style-loader</td><td>将 css 注入到 DOM</td></tr><tr><td>file-loader</td><td>将文件上的import  /  require 解析为 url，并将该文件输出到输出目录中</td></tr><tr><td>url-loader</td><td>用于将文件转换成 base64 uri 的 webpack 加载程序</td></tr><tr><td>html-loader</td><td>将 HTML 导出为字符串， 当编译器要求时，将 HTML 最小化</td></tr></tbody></table>
<h4 data-id="heading-7">6.1 处理js(引入babel-loader)</h4>
<p>由于不同浏览器对高级语法的支持性并不是非常好，为了向下兼容考虑将他们转换为ES5标准</p>
<ol>
<li>安装依赖 <code>babel-loader</code>()、<code>@babel/core</code> 和<code>@babel/preset-env</code></li>
</ol>
<pre><code class="copyable">npm install -D babel-loader @babel/core @babel/preset-env
<span class="copy-code-btn">复制代码</span></code></pre>
<ol start="2">
<li>配置<code>webpack.config.js</code></li>
</ol>
<pre><code class="copyable">module.exports=&#123;
    module:&#123;
        &#123;
            test: /\.js$/,
            loader: 'babel-loader',
            exclude: /node_modules/ // 
        &#125;
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<ol start="3">
<li>根目录新建.babelrc</li>
</ol>
<pre><code class="copyable">&#123;
  "presets": [
    "@babel/preset-env" // 官方推荐使用，包含了所有现代js（es2015 es2016等）的所有新特性
  ]
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<ol start="4">
<li>如果你希望 加入懒加载 TODO</li>
</ol>
<pre><code class="hljs language-bash copyable" lang="bash">npm i -D @babel/plugin-syntax-dynamic-import
<span class="copy-code-btn">复制代码</span></code></pre>
<p>同时更新 .babelrc 文件，加入plugins配置</p>
<pre><code class="hljs language-json copyable" lang="json">&#123;
  <span class="hljs-attr">"presets"</span>: [
    <span class="hljs-string">"@babel/preset-env"</span> 
  ],
  <span class="hljs-attr">"plugins"</span>: [
    <span class="hljs-string">"syntax-dynamic-import"</span>
  ]
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<ol start="5">
<li><code>验证：</code>在index.js 加入箭头函数，执行构建命令查看<code>bundle.js</code>是否将ES6箭头函数转换为普通函数</li>
</ol>
<pre><code class="copyable">// Babel Input: ES2015 arrow function
[1, 2, 3].map((n) => n + 1);

// Babel Output: ES5 equivalent
[1, 2, 3].map(function(n) &#123;
  return n + 1;
&#125;);
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-8">6.2 处理css(scss less)，这里以scss举例</h4>
<ol>
<li>为支持css import，安装依赖<code>style-loader css-loader</code></li>
</ol>
<pre><code class="hljs language-bash copyable" lang="bash">npm i -D style-loader css-loader
<span class="copy-code-btn">复制代码</span></code></pre>
<ol start="2">
<li>如果我们使用sass来构建样式，则需要多安装两个node-sass sass-loader</li>
</ol>
<pre><code class="hljs language-bash copyable" lang="bash">npm i -D node-sass sass-loader
<span class="copy-code-btn">复制代码</span></code></pre>
<p>3、为css增加浏览器前缀</p>
<pre><code class="copyable">npm i -D postcss-loader autoprefixer  
<span class="copy-code-btn">复制代码</span></code></pre>
<p>3、配置 webpack.config.js，通过loader形式让webpack 知道以何种loader加载对应后缀名(<code>.css</code>和<code>scss</code>)的文件，从而打包进bundle.js</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-built_in">module</span>.exports = &#123;
    <span class="hljs-comment">// ... 省略其它配置项目</span>
   <span class="hljs-attr">module</span>:&#123;
        <span class="hljs-attr">rules</span>:[
            &#123;
              <span class="hljs-attr">test</span>:<span class="hljs-regexp">/\.css$/</span>,
              use:[<span class="hljs-string">'style-loader'</span>,<span class="hljs-string">'css-loader'</span>] <span class="hljs-comment">// 从右向左解析原则</span>
            &#125;,
            &#123;
              <span class="hljs-attr">test</span>:<span class="hljs-regexp">/\.scss$/</span>,
              use:[<span class="hljs-string">'style-loader'</span>,<span class="hljs-string">'css-loader'</span>,<span class="hljs-string">'postcss-loader'</span>,<span class="hljs-string">'sass-loader'</span>] <span class="hljs-comment">// 从右向左解析原则</span>
            &#125;
          ]

    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>4、<code>验证：</code> 新建一个.sccs文件，写一些sass 语法样式，以及css3语法，查看实际输出结果</p>
<pre><code class="hljs language-scss copyable" lang="scss"><span class="hljs-comment">// 变量定义</span>
<span class="hljs-variable">$color</span>: blue;

<span class="hljs-selector-tag">body</span> &#123;
    <span class="hljs-comment">/*嵌套*/</span>
  <span class="hljs-selector-class">.test</span> &#123;
    <span class="hljs-attribute">height</span>: <span class="hljs-number">100px</span>;
    <span class="hljs-attribute">display</span>: flex;
    <span class="hljs-attribute">align-items</span>: center;
    <span class="hljs-attribute">justify-content</span>: center;
    <span class="hljs-attribute">background-color</span>: <span class="hljs-variable">$color</span>;
    <span class="hljs-attribute">color</span>: <span class="hljs-number">#fff</span>;
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-9">6.3 处理图片/字体等多媒体文件</h4>
<ol>
<li>为支持import 字体、图片等其它多媒体格式文件，安装依赖<code>url-loader file-loader</code></li>
</ol>
<pre><code class="hljs language-bash copyable" lang="bash">npm i -D url-loader file-loader
<span class="copy-code-btn">复制代码</span></code></pre>
<ol start="2">
<li>配置 webpack.config.js,通过loader形式让webpack知道以何种loader加载这些多媒体格式文件的</li>
</ol>
<p>注意：<code>url-loader</code> 一般与<code>file-loader</code>搭配使用，功能与<code>file-loader</code>类似，如果文件小于限制的大小。则会返回<code>base64</code>编码，否则使用 <code>file-loader</code> 将文件移动到输出的目录中</p>
<pre><code class="copyable">module.exports = &#123;
    // ... 省略其它配置
    module:&#123;
        rules:&#123;
              &#123;
                test: /\.(jpe?g|png|gif)$/i, //图片文件
                use: [
                  &#123;
                    loader: 'url-loader',
                    options: &#123;
                      limit: 10240,
                      fallback: &#123;
                        loader: 'file-loader',
                        options: &#123;
                            name: 'img/[name].[hash:8].[ext]'
                        &#125;
                      &#125;
                    &#125;
                  &#125;
                ]
              &#125;,
              &#123;
                test: /\.(mp4|webm|ogg|mp3|wav|flac|aac)(\?.*)?$/, //媒体文件
                use: [
                  &#123;
                    loader: 'url-loader',
                    options: &#123;
                      limit: 10240,
                      fallback: &#123;
                        loader: 'file-loader',
                        options: &#123;
                          name: 'media/[name].[hash:8].[ext]'
                        &#125;
                      &#125;
                    &#125;
                  &#125;
                ]
              &#125;,
              &#123;
                test: /\.(woff2?|eot|ttf|otf)(\?.*)?$/i, // 字体
                use: [
                  &#123;
                    loader: 'url-loader',
                    options: &#123;
                      limit: 10240,
                      fallback: &#123;
                        loader: 'file-loader',
                        options: &#123;
                          name: 'fonts/[name].[hash:8].[ext]'
                        &#125;
                      &#125;
                    &#125;
                  &#125;
                ]
              &#125;,
            ]
        &#125;
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-10">【七】】其它</h3>
<h4 data-id="heading-11">7.1 mode</h4>
<p>mode 配置选项告用于告诉webpack相应地使用其内置的优化。可选配置有 <code>development</code> 、<code>production</code>或 <code>none</code>，具体可查看<a href="https://webpack.js.org/configuration/mode/" target="_blank" rel="nofollow noopener noreferrer">官方文档</a></p>
<h4 data-id="heading-12">7.2 devtool</h4>
<p>在了解Source Map用处之后，你就会容易理解通过devtool的配置 webpack 如何生成 Source Map，用来增强调试过程。不同的值会明显影响到构建(build)和重新构建(rebuild)的速度。</p>
<ul>
<li><code>生产环境(mode=production)</code>：默认为 null ，一般不设置（ none ）或 nosources-source-map</li>
<li><code>开发环境(mode=development)</code>：默认为 eval ，一般设置为 eval、cheap-eval-source-map 、cheap-module-eval-source-map</li>
</ul>
<p><strong>sourcemap 生成几个策略：</strong></p>



































<table><thead><tr><th>值</th><th>原理</th><th>优缺点</th></tr></thead><tbody><tr><td>eval</td><td>通过eval包裹每一个module模块，编译后不会生成<code>sourcemap</code>文件，仅仅是在每一个模块后，增加sourceURL来关联模块处理前后对应的关系</td><td>优点是：打包速度非常快，因为不需要生成sourcemap文件。缺点是：由于会映射到转换后的代码，而不是映射到原始代码，所以不能正确的显示行数。</td></tr><tr><td>source-map</td><td>为每一个打包后的模块生成独立的sourcemap文件，打包后的代码最后面一句代码是 <code>// #sourceMappingURL=bundle.js.map</code> ，同时在dist目录下会针对每一个模块生成响应的 .map文件</td><td>拥有完整的源代码信息，便于调试，但影响持续构建</td></tr><tr><td>inline</td><td>不会生成独立的 .map文件，而是将<code>.map</code>文件以dataURL的形式插入</td><td>缺点：打包输出文件变大</td></tr><tr><td>cheap</td><td>打包后同样会为每一个文件模块生成 <code>.map</code>文件，但是与<code>source-map</code>的区别在于<code>cheap-source-map</code>生成的 map文件会忽略原始代码中的列信息</td><td>可以大幅提高<code>souremap</code>生成的效率，但没有列信息（会映射到转换后的代码，而不是映射到原始代码），通常我们调试并不关心列信息</td></tr><tr><td>module</td><td>同样生成一个没有列的信息的sourcemap文件，同时loader的sourcemap也被简化成为只包含对应行</td><td>支持<code>babel</code>这种预编译工具，找到最初源码信息</td></tr></tbody></table>
<p><strong>如何根据不同环境选择相应sourceMap 生成策略？</strong></p>
<ul>
<li>
<ol>
<li>源代码中的列信息是没有任何作用，因此我们打包后的文件不希望包含列相关信息，只有行信息能建立打包前后的依赖关系。因此不管是开发环境或生产环境，我们都希望添加<code>cheap</code>的基本类型来忽略打包前后的列信息。</li>
</ol>
</li>
<li>
<ol start="2">
<li>不管是开发环境还是正式环境，我们都希望能定位到bug的源代码具体的位置，比如说某个vue文件报错了，我们希望能定位到具体的vue文件，因此我们也需要module配置。</li>
</ol>
</li>
<li>
<ol start="3">
<li>我们需要生成map文件的形式，因此我们需要增加<code>source-map</code>属性。</li>
</ol>
</li>
<li>
<ol start="4">
<li>我们介绍了eval打包代码的时候，知道eval打包后的速度非常快，因为它不生成map文件，但是可以对eval组合使用<code>eval-source-map</code>使用会将map文件以DataURL的形式存在打包后的js文件中</li>
</ol>
</li>
</ul>
<p>因此建议：</p>
<pre><code class="copyable">// 在开发环境中我们可以使用 , eval加快打包效率
module.exports = &#123;
  devtool: 'cheap-module-eval-source-map'
&#125;

// 在正式环境中我们可以使用  
module.exports = &#123; 
  devtool: 'cheap-module-source-map';
&#125;
<span class="copy-code-btn">复制代码</span></code></pre></div>  
</div>
            