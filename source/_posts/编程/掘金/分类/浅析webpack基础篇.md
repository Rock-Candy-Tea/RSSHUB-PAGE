
---
title: '浅析webpack基础篇'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=6218'
author: 掘金
comments: false
date: Fri, 09 Jul 2021 22:59:37 GMT
thumbnail: 'https://picsum.photos/400/300?random=6218'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h2 data-id="heading-0">为什么需要构建工具？</h2>
<p>转换ES6语法 <br>
转换JSX  <br>
CSS前缀补全/预处理器  <br>
压缩混淆  <br>
图片压缩</p>
<h2 data-id="heading-1">为什么选择webpack？</h2>
<p>社区生态丰富 <br>
配置灵活和插件化拓展  <br>
官方更新迭代速度快</p>
<h2 data-id="heading-2">初识webpack：配置文件名称</h2>
<p>webpack默认配置文件：webpack.config.js  <br>
可以通过webpack --config指定配置文件</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">// 初始webpack：webpack配置组成</span>
<span class="hljs-built_in">module</span>.exports = &#123;
    <span class="hljs-attr">entry</span>: <span class="hljs-string">'./src/index.js'</span>,  <span class="hljs-comment">// 打包的入口文件</span>
    output：<span class="hljs-string">'./dist/main.js'</span>,  <span class="hljs-comment">// 打包的输出</span>
    <span class="hljs-attr">mode</span>: <span class="hljs-string">'production'</span>,  <span class="hljs-comment">// 环境</span>
    <span class="hljs-attr">module</span>: &#123;
        <span class="hljs-attr">rules</span>: [&#123;  <span class="hljs-comment">// Loader配置</span>
            <span class="hljs-attr">test</span>: <span class="hljs-regexp">/\.txt$/</span>, use: <span class="hljs-string">'raw-loader'</span>
        &#125;]
    &#125;,
    <span class="hljs-attr">plugins</span>: [  <span class="hljs-comment">// 插件配置</span>
        <span class="hljs-keyword">new</span> HtmlwebpackPlugin(&#123;
            <span class="hljs-attr">template</span>: <span class="hljs-string">'./src/index.html'</span>,
        &#125;)
    ]
&#125;

<span class="hljs-comment">// 零配置webpack包含那些内容？</span>
<span class="hljs-built_in">module</span>.exports = &#123;
    <span class="hljs-attr">entry</span>: <span class="hljs-string">'./src/index.js'</span>,  <span class="hljs-comment">// 指定默认的entry为： ./src/index.js</span>
    output：<span class="hljs-string">'./dist/main.js'</span>,  <span class="hljs-comment">// 指定默认的output为： ./dist/main.js</span>
    <span class="hljs-attr">mode</span>: <span class="hljs-string">'production'</span>,
    <span class="hljs-attr">module</span>: &#123;
        <span class="hljs-attr">rules</span>: [&#123;
            <span class="hljs-attr">test</span>: <span class="hljs-regexp">/\.txt$/</span>, use: <span class="hljs-string">'raw-loader'</span>
        &#125;]
    &#125;,
    <span class="hljs-attr">plugins</span>: [
        <span class="hljs-keyword">new</span> HtmlwebpackPlugin(&#123;
            <span class="hljs-attr">template</span>: <span class="hljs-string">'./src/index.html'</span>,
        &#125;)
    ]
&#125;

<span class="hljs-comment">// 通过npm script 运行webpack</span>
&#123;
  <span class="hljs-string">"name"</span>: <span class="hljs-string">"webpack-study"</span>,
  <span class="hljs-string">"version"</span>: <span class="hljs-string">"1.0.0"</span>,
  <span class="hljs-string">"description"</span>: <span class="hljs-string">""</span>,
  <span class="hljs-string">"main"</span>: <span class="hljs-string">"index.js"</span>,
  <span class="hljs-string">"scripts"</span>: &#123;
    <span class="hljs-string">"test"</span>: <span class="hljs-string">"echo \"Error: no test specified\" && exit 1"</span>,
    <span class="hljs-comment">//  通过npm run build 运行构建</span>
    <span class="hljs-string">"build"</span>: <span class="hljs-string">"webpack"</span> <span class="hljs-comment">// 原理：模块局部安装会在node_modules/.bin目录创建软链接</span>
  &#125;,
  <span class="hljs-string">"keywords"</span>: [],
  <span class="hljs-string">"author"</span>: <span class="hljs-string">""</span>,
  <span class="hljs-string">"license"</span>: <span class="hljs-string">"ISC"</span>,
  <span class="hljs-string">"dependencies"</span>: &#123;&#125;,
  <span class="hljs-string">"devDependencies"</span>: &#123;
    <span class="hljs-string">"webpack"</span>: <span class="hljs-string">"^4.31.0"</span>,
    <span class="hljs-string">"webpack-cli"</span>: <span class="hljs-string">"^3.3.2"</span>
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-3">webpack核心概念</h2>
<h3 data-id="heading-4">Entry</h3>
<p>Entry 用来制定webpack的打包入口 <br>
依赖图的入口是entry <br>
对于非代码比如图片、字体以来也会不断加入到依赖图中</p>
<p>用法：
单入口：entry是一个字符串
单界面应用</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-built_in">module</span>.exports = &#123;
    <span class="hljs-attr">entry</span>: <span class="hljs-string">'xxxxx'</span>,
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>多入口：entry是一个对象
多界面应用</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-built_in">module</span>.exports = &#123;
    <span class="hljs-attr">entry</span>: &#123;
        <span class="hljs-attr">app</span>: <span class="hljs-string">'xxx'</span>,
        <span class="hljs-attr">adminApp</span>: <span class="hljs-string">'xxxx'</span>,
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-5">Output</h3>
<p>Output用来告诉webpack如何将编译后的文件输出到磁盘。</p>
<p>Output 的用法：单入口配置</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-built_in">module</span>.exports = &#123;
    <span class="hljs-attr">entry</span>: <span class="hljs-string">'xxxx'</span>,
    <span class="hljs-attr">output</span>: &#123;
        <span class="hljs-attr">filename</span>: <span class="hljs-string">'bundle.js'</span>,
        <span class="hljs-attr">path</span>: __dirname + <span class="hljs-string">'/dist'</span>
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>Output 的用法：多入口配置</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-built_in">module</span>.exports = &#123;
    <span class="hljs-attr">entry</span>: &#123;
        <span class="hljs-attr">app</span>: <span class="hljs-string">'xxx'</span>,
        <span class="hljs-attr">adminApp</span>: <span class="hljs-string">'xxx'</span>,
    &#125;,
    <span class="hljs-comment">// 没有多出口的说法</span>
    <span class="hljs-attr">output</span>: &#123;
        <span class="hljs-comment">// 通过占位符确保文件名称的唯一</span>
        <span class="hljs-attr">filename</span>: <span class="hljs-string">'[name].js'</span>,   <span class="hljs-comment">// name 指定打包的名称</span>
        <span class="hljs-attr">path</span>: __dirname + <span class="hljs-string">'/dist'</span>,
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-6">Loaders</h3>
<p>webpack开箱即用只支持JS和JSON两种文件类型，通过Loaders去支持其它文件类型并且把它们转化为有效的模块，并且可以添加到依赖图中。  <br>
本身是一个函数，接受源文件作为参数，返回转换的结果。</p>
<p><strong>常见的Loaders有那些？</strong></p>





































<table><thead><tr><th>名称</th><th>描述</th></tr></thead><tbody><tr><td>babel-loader</td><td>转换ES6、ES7等JS新特性语法</td></tr><tr><td>css-loader</td><td>支持.css文件的加载和解析</td></tr><tr><td>less-loader</td><td>将less文件转换为css</td></tr><tr><td>ts-loader</td><td>将TS转换为JS</td></tr><tr><td>file-loader</td><td>进行图片、字体等的打包</td></tr><tr><td>raw-loader</td><td>将文件以字符串的形式导入</td></tr><tr><td>thread-loader</td><td>多进程打包JS和CSS（正常是一个进程）</td></tr></tbody></table>
<p><strong>Loaders 的用法</strong></p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">const</span> path = <span class="hljs-built_in">require</span>(<span class="hljs-string">'path'</span>);

<span class="hljs-built_in">module</span>.exports = &#123;
    <span class="hljs-attr">entry</span>: <span class="hljs-string">'./src/index.js'</span>,
    output：<span class="hljs-string">'./dist/main.js'</span>,
    <span class="hljs-attr">mode</span>: <span class="hljs-string">'production'</span>,
    <span class="hljs-attr">module</span>: &#123;
        <span class="hljs-attr">rules</span>: [&#123;
            <span class="hljs-comment">// test 指定匹配规则</span>
            <span class="hljs-comment">// use 指定使用的loader名称</span>
            <span class="hljs-attr">test</span>: <span class="hljs-regexp">/\.txt$/</span>, use: <span class="hljs-string">'raw-loader'</span>
        &#125;]
    &#125;,
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-7">Plugins</h3>
<p>插件用于bundle文件的优化，资源管理和环境变量注入，Loader没办法做到事情Plugins都可以做到。 <br>
作用于整个构建过程</p>
<p><strong>常见的Plugins有哪些？</strong></p>





































<table><thead><tr><th>名称</th><th>描述</th></tr></thead><tbody><tr><td>CommonsChunkPlugin</td><td>将chunks相同的模块代码提取成公共js</td></tr><tr><td>CleanWebpackPlgin</td><td>清理构建目录</td></tr><tr><td>ExtractTextWebpackPlugin</td><td>将css从bunlde文件里提取成一个独立的css</td></tr><tr><td>CopyWebpackPlugin</td><td>将文件或者文件夹拷贝到构建的输出目录</td></tr><tr><td>HtmlWebpackPlugin</td><td>创建html文件去承载输出的bundle</td></tr><tr><td>UglifyjsWebpackPlugin</td><td>压缩JS</td></tr><tr><td>ZipWebpackPlugin</td><td>将打包出的资源生成一个zip包</td></tr></tbody></table>
<p><strong>Plugins的用法</strong></p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-built_in">module</span>.exports = &#123;
    <span class="hljs-attr">entry</span>: <span class="hljs-string">'./src/index.js'</span>, 
    output：<span class="hljs-string">'./dist/main.js'</span>,  
    <span class="hljs-attr">mode</span>: <span class="hljs-string">'production'</span>,
    <span class="hljs-attr">module</span>: &#123;
        <span class="hljs-attr">rules</span>: [&#123;
            <span class="hljs-attr">test</span>: <span class="hljs-regexp">/\.txt$/</span>, use: <span class="hljs-string">'raw-loader'</span>
        &#125;]
    &#125;,
    <span class="hljs-attr">plugins</span>: [
        <span class="hljs-comment">// 放到plugin数组</span>
        <span class="hljs-keyword">new</span> HtmlwebpackPlugin(&#123;
            <span class="hljs-attr">template</span>: <span class="hljs-string">'./src/index.html'</span>,
        &#125;)
    ]
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-8">mode</h3>
<p>Mode用来指定当前构建环境是：production、development还是none，webpack 4以前是没有这个概念的。</p>
<p>设置mode可以使用webpack内置的函数，默认值为production。</p>
<p><strong>Mode的内置函数功能</strong></p>





















<table><thead><tr><th>选项</th><th>描述</th></tr></thead><tbody><tr><td>development</td><td>设置process.env.NODE_ENV 的值为development<br>开启NameChunkPlugin 和 NameModulesPlugiin</td></tr><tr><td>production</td><td>设置process.env.NODE_ENV的值为production<br>开启FlagDependencyUsagePlugin，<br>FlagIncludeChunksPlugin，ModuleConcatenationPlugin， <br>NoEmitOnErrorsPlugin，OccurrenceOrderPlugin，<br>SideEffectsFlagPlugin，TerserPlugin</td></tr><tr><td>none</td><td>不开始任何优化选项</td></tr></tbody></table>
<h2 data-id="heading-9">资源解析</h2>
<h3 data-id="heading-10">解析ES6</h3>
<p>使用babel-loader  <br>
babel的配置文件是：.babelrc</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-built_in">module</span>.exports = &#123;
    <span class="hljs-attr">entry</span>: <span class="hljs-string">'./src/index.js'</span>, 
    output：<span class="hljs-string">'./dist/main.js'</span>,  
    <span class="hljs-attr">mode</span>: <span class="hljs-string">'production'</span>,
    <span class="hljs-attr">module</span>: &#123;
        <span class="hljs-attr">rules</span>: [&#123;
            <span class="hljs-attr">test</span>: <span class="hljs-regexp">/\.js$/</span>, use: <span class="hljs-string">'babel-loader'</span>
        &#125;]
    &#125;,
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>增加ES6的babel preset配置</p>
<pre><code class="hljs language-javascript copyable" lang="javascript">&#123;
    <span class="hljs-string">"presets"</span>: [
        <span class="hljs-comment">// 增加ES6的babel preset配置</span>
        <span class="hljs-string">"@babel/preset-env"</span>
    ],
    <span class="hljs-string">"plugins"</span>: [
        <span class="hljs-string">"@babel/proposal-class-properties"</span>
    ]
&#125;

<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-11">解析React JSX</h3>
<pre><code class="hljs language-javascript copyable" lang="javascript">&#123;
    <span class="hljs-string">"presets"</span>: [
        <span class="hljs-comment">// 增加ES6的babel preset配置</span>
        <span class="hljs-string">"@babel/preset-env"</span>,
        <span class="hljs-comment">// 增加React的babel preset配置</span>
        <span class="hljs-string">"@babel/preset-react"</span>
    ],
    <span class="hljs-string">"plugins"</span>: [
        <span class="hljs-string">"@babel/proposal-class-properties"</span>
    ]
&#125;

<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-12">解析CSS</h3>
<p>css-loader用于加载.css文件，并且转换成commonjs对象。 <br>
style-loader将样式通过标签插入到head中。
</p><pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-built_in">module</span>.exports = &#123;
    <span class="hljs-attr">entry</span>: <span class="hljs-string">'./src/index.js'</span>, 
    output：<span class="hljs-string">'./dist/main.js'</span>,  
    <span class="hljs-attr">mode</span>: <span class="hljs-string">'production'</span>,
    <span class="hljs-attr">module</span>: &#123;
        <span class="hljs-attr">rules</span>: [&#123;
            <span class="hljs-attr">test</span>: <span class="hljs-regexp">/\.css$/</span>, use: [
                <span class="hljs-string">'style-loader'</span>,
                <span class="hljs-string">'css-loader'</span>
            ]
        &#125;]
    &#125;,
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-13">解析less 和 sass</h3>
<p>less-loader用于将less转换成css</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-built_in">module</span>.exports = &#123;
    <span class="hljs-attr">entry</span>: <span class="hljs-string">'./src/index.js'</span>, 
    output：<span class="hljs-string">'./dist/main.js'</span>,  
    <span class="hljs-attr">mode</span>: <span class="hljs-string">'production'</span>,
    <span class="hljs-attr">module</span>: &#123;
        <span class="hljs-attr">rules</span>: [&#123;
            <span class="hljs-attr">test</span>: <span class="hljs-regexp">/\.css$/</span>, use: [
                <span class="hljs-string">'style-loader'</span>,
                <span class="hljs-string">'css-loader'</span>,
                <span class="hljs-string">'less-loader'</span>
            ]
        &#125;]
    &#125;,
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-14">解析图片和字体</h3>
<p>解析图片/字体 <br>
file-loader</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-built_in">module</span>.exports = &#123;
    <span class="hljs-attr">entry</span>: <span class="hljs-string">'./src/index.js'</span>, 
    output：<span class="hljs-string">'./dist/main.js'</span>,  
    <span class="hljs-attr">mode</span>: <span class="hljs-string">'production'</span>,
    <span class="hljs-attr">module</span>: &#123;
        <span class="hljs-attr">rules</span>: [&#123;
            <span class="hljs-attr">test</span>: <span class="hljs-regexp">/\.(png|svg|jpg|gif)$/</span>, use: [
                <span class="hljs-string">'file-loader'</span>,  <span class="hljs-comment">//用于处理文件</span>
            ]
        &#125;,&#123;
            <span class="hljs-attr">test</span>: <span class="hljs-regexp">/\.(woff|woff2|eot|tff)$/</span>, use: [
                <span class="hljs-string">'file-loader'</span>,  <span class="hljs-comment">//用于处理字体</span>
            ]
        &#125;]
    &#125;,
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>url-loader也可以处理图片和字体,内部也是file-loader  <br>
可以设置较小资源自动base64</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-built_in">module</span>.exports = &#123;
    <span class="hljs-attr">entry</span>: <span class="hljs-string">'./src/index.js'</span>, 
    output：<span class="hljs-string">'./dist/main.js'</span>,  
    <span class="hljs-attr">mode</span>: <span class="hljs-string">'production'</span>,
    <span class="hljs-attr">module</span>: &#123;
        <span class="hljs-attr">rules</span>: [&#123;
            <span class="hljs-attr">test</span>: <span class="hljs-regexp">/\.(png|svg|jpg|gif)$/</span>, use: [&#123;
                <span class="hljs-attr">loader</span>: <span class="hljs-string">'url-loader'</span>,  <span class="hljs-comment">//用于处理文件</span>
                <span class="hljs-attr">optins</span>: &#123;
                    <span class="hljs-attr">limit</span>: <span class="hljs-number">10240</span>  <span class="hljs-comment">// 单位：字节</span>
                &#125;
            &#125;]
        &#125;]
    &#125;,
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-15">webpack 中的文件监听</h2>
<p>文件监听是在发现源码发生变化时，自动重新构建出新的输出文件。 <br></p>
<p><strong>webpack 开启监听模式，有两种方式：</strong></p>
<ul>
<li>启动webpack命令时，带上--watch参数</li>
<li>在配置webpack.config.js中设置watch：true</li>
</ul>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">// 监听使用</span>
&#123;
  <span class="hljs-string">"name"</span>: <span class="hljs-string">"webpack-study"</span>,
  <span class="hljs-string">"version"</span>: <span class="hljs-string">"1.0.0"</span>,
  <span class="hljs-string">"description"</span>: <span class="hljs-string">""</span>,
  <span class="hljs-string">"main"</span>: <span class="hljs-string">"index.js"</span>,
  <span class="hljs-string">"scripts"</span>: &#123;
    <span class="hljs-string">"test"</span>: <span class="hljs-string">"echo \"Error: no test specified\" && exit 1"</span>,
    <span class="hljs-comment">//  通过npm run build 运行构建</span>
    <span class="hljs-string">"build"</span>: <span class="hljs-string">"webpack"</span>, <span class="hljs-comment">// 原理：模块局部安装会在node_modules/.bin目录创建软链接</span>
    <span class="hljs-string">"watch"</span>: <span class="hljs-string">'webpack --watch'</span>  <span class="hljs-comment">//唯一缺陷：每次需要手动刷新浏览器</span>
  &#125;,
  <span class="hljs-string">"keywords"</span>: [],
  <span class="hljs-string">"author"</span>: <span class="hljs-string">""</span>,
  <span class="hljs-string">"license"</span>: <span class="hljs-string">"ISC"</span>,
  <span class="hljs-string">"dependencies"</span>: &#123;&#125;,
  <span class="hljs-string">"devDependencies"</span>: &#123;
    <span class="hljs-string">"webpack"</span>: <span class="hljs-string">"^4.31.0"</span>,
    <span class="hljs-string">"webpack-cli"</span>: <span class="hljs-string">"^3.3.2"</span>
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>文件监听原理分析</strong> <br>
轮询判断文件的最后编辑时间是否变化</p>
<p>某个文件发生了变化，并不会立刻告诉监听者,而是先缓存起来，等aggregateTimeout</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-built_in">module</span>.export = &#123;
    <span class="hljs-comment">// 默认false，也就是不开启</span>
    <span class="hljs-attr">watch</span>: <span class="hljs-literal">true</span>,
    <span class="hljs-comment">// 只有开启监听模式时，watchOptions才有意义</span>
    <span class="hljs-attr">watchOptions</span>: &#123;
        <span class="hljs-comment">// 默认为空，不监听的文件或者文件夹，支持正则匹配</span>
        <span class="hljs-attr">ignored</span>: <span class="hljs-regexp">/node_modules/</span>,
        <span class="hljs-comment">// 监听到变化发生后等300ms再去执行，默认300ms</span>
        aggregateTimeout: <span class="hljs-number">300</span>,
        <span class="hljs-comment">// 判断文件是否发生变化时通过不停询问系统指定文件有没有变化实现的，默认每秒问1000次</span>
        <span class="hljs-attr">poll</span>: <span class="hljs-number">1000</span>
    &#125;
&#125;

<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-16">webpack 热更新</h2>
<p><strong>使用webpack-dev-server</strong> <br></p>
<p>WDS 不刷新浏览器  <br>
WDS 不输出文件，没有磁盘IO，而是放在内存中  <br>
使用HotModuleReplacementPlugin插件</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">// 热更新</span>
&#123;
  <span class="hljs-string">"name"</span>: <span class="hljs-string">"webpack-study"</span>,
  <span class="hljs-string">"version"</span>: <span class="hljs-string">"1.0.0"</span>,
  <span class="hljs-string">"description"</span>: <span class="hljs-string">""</span>,
  <span class="hljs-string">"main"</span>: <span class="hljs-string">"index.js"</span>,
  <span class="hljs-string">"scripts"</span>: &#123;
    <span class="hljs-string">"test"</span>: <span class="hljs-string">"echo \"Error: no test specified\" && exit 1"</span>,
    <span class="hljs-comment">//  通过npm run build 运行构建</span>
    <span class="hljs-string">"build"</span>: <span class="hljs-string">"webpack"</span>, <span class="hljs-comment">// 原理：模块局部安装会在node_modules/.bin目录创建软链接</span>
    <span class="hljs-string">"watch"</span>: <span class="hljs-string">"webpack --watch"</span>, <span class="hljs-comment">//唯一缺陷：每次需要手动刷新浏览器</span>
    <span class="hljs-string">"dev"</span>: <span class="hljs-string">"webpack-dev-server --open"</span>
  &#125;,
  <span class="hljs-string">"keywords"</span>: [],
  <span class="hljs-string">"author"</span>: <span class="hljs-string">""</span>,
  <span class="hljs-string">"license"</span>: <span class="hljs-string">"ISC"</span>,
  <span class="hljs-string">"dependencies"</span>: &#123;&#125;,
  <span class="hljs-string">"devDependencies"</span>: &#123;
    <span class="hljs-string">"webpack"</span>: <span class="hljs-string">"^4.31.0"</span>,
    <span class="hljs-string">"webpack-cli"</span>: <span class="hljs-string">"^3.3.2"</span>
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>使用webpack-dev-middleware</strong></p>
<p>WDM将webpack输出的文件传输给服务器  <br>
适用于灵活的定制场景</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">const</span> express = <span class="hljs-built_in">require</span>(<span class="hljs-string">'express'</span>);
<span class="hljs-keyword">const</span> webpack = <span class="hljs-built_in">require</span>(<span class="hljs-string">'webpack'</span>);
<span class="hljs-keyword">const</span> webpackDevMiddleware = <span class="hljs-built_in">require</span>(<span class="hljs-string">'webpack-dev-middleware'</span>);

<span class="hljs-keyword">const</span> app = express();
<span class="hljs-keyword">const</span> config = <span class="hljs-built_in">require</span>(<span class="hljs-string">'./webpack.config.js'</span>);
<span class="hljs-keyword">const</span> compiler = webpack(<span class="hljs-string">'config'</span>);

app.use(webpackDevMiddleware(compiler, &#123;
    <span class="hljs-attr">publicPath</span>:config.output.publicPath
&#125;));

app.listen(<span class="hljs-number">3000</span>, <span class="hljs-function">() =></span> &#123;
   <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'监听'</span>); 
&#125;);

<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>热更新的原理分析</strong>  <br>
Webpack Compile：将JS编译成Bundle  <br>
HMR Server: 将热更新的文件输出给HMR Runtime  <br>
Bundle server： 提供文件在浏览器访问  <br>
HMR Runtime：会被注入到浏览器，更新文件的变化  <br>
bundle.js: 构建输出的文件</p>
<h2 data-id="heading-17">文件指纹</h2>
<p><strong>什么是文件指纹？</strong>  <br>
打包后输出文件名的后缀。</p>
<p><strong>文件指纹如何生成?</strong>  <br>
Hash: 和整个项目的构建相关，只要项目文件有修改，整个项目构建的hash值就会更改  <br>
Chunkhash: 和webpack打包的chunk有关，不同的entry会生成不同的chunkhash值  <br>
Contenthash: 根据文件内容来定义hash，文件内容不变，则contenthash不变</p>
<p><strong>JS的文件指纹设置</strong>  <br>
设置output的filename,使用[chunkhash]</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-built_in">module</span>.exports = &#123;
    <span class="hljs-attr">entry</span>: <span class="hljs-string">'./src/index.js'</span>, 
    <span class="hljs-attr">output</span>: &#123;
        <span class="hljs-attr">path</span>: path.join(__dirname, <span class="hljs-string">'dist'</span>),
        <span class="hljs-attr">filename</span>: <span class="hljs-string">'[name][chunkhash:8].js'</span>,
    &#125;,
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>CSS的文件指纹设置</strong>  <br>
设置MiniCssExtractPlugin的filename,使用[contenthash]</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-built_in">module</span>.exports = &#123;
    <span class="hljs-attr">entry</span>: <span class="hljs-string">'./src/index.js'</span>, 
    <span class="hljs-attr">output</span>: &#123;
        <span class="hljs-attr">path</span>: path.join(__dirname, <span class="hljs-string">'dist'</span>),
        <span class="hljs-attr">filename</span>: <span class="hljs-string">'[name][chunkhash:8].js'</span>,
    &#125;,
    <span class="hljs-attr">plugins</span>: [
        <span class="hljs-keyword">new</span> MiniCssExtractPlugin(
            &#123;
                <span class="hljs-attr">filename</span>: <span class="hljs-string">`[name][contenthash:8].css`</span>
            &#125;
        )
    ]
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>图片的文件指纹设置</strong>  <br>
设置file-loader的name,使用[hash]</p>





































<table><thead><tr><th>占位符名称</th><th>含义</th></tr></thead><tbody><tr><td>[ext]</td><td>资源后缀名</td></tr><tr><td>[name]</td><td>文件名称</td></tr><tr><td>[path]</td><td>文件的相对路径</td></tr><tr><td>[folder]</td><td>文件所在的文件夹</td></tr><tr><td>[contenthash]</td><td>文件的内容hash,默认是md5生成</td></tr><tr><td>[hash]</td><td>文件内容的hash,默认是md5生成</td></tr><tr><td>[emoji]</td><td>一个随机的指代文件内容的emoj</td></tr></tbody></table>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-built_in">module</span>.exports = &#123;
    <span class="hljs-attr">entry</span>: <span class="hljs-string">'./src/index.js'</span>, 
    output：<span class="hljs-string">'./dist/main.js'</span>,  
    <span class="hljs-attr">mode</span>: <span class="hljs-string">'production'</span>,
    <span class="hljs-attr">module</span>: &#123;
        <span class="hljs-attr">rules</span>: [&#123;
            <span class="hljs-attr">test</span>: <span class="hljs-regexp">/\.(png|svg|jpg|gif)$/</span>, 
            use: [&#123;
                <span class="hljs-attr">loader</span>: <span class="hljs-string">'file-loader'</span>,  <span class="hljs-comment">//用于处理文件</span>
                <span class="hljs-attr">options</span>: &#123;
                    <span class="hljs-attr">name</span>: <span class="hljs-string">'img/[name][hash:8].[ext]'</span>,  <span class="hljs-comment">//8: hash前8位</span>
                &#125;
            &#125;]
        &#125;]
    &#125;,
&#125;

<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-18">代码压缩</h3>
<p>HTML压缩  <br>
CSS压缩  <br>
JS压缩  <br></p>
<p><strong>JS 文件的压缩</strong></p>
<p>内置了 uglifyjs-webpack-plugin</p>
<p><strong>CSS压缩</strong></p>
<p>使用optimize-css-assets-webpack-plugin  <br>
同时使用cssnano</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-built_in">module</span>.exports = &#123;
    <span class="hljs-attr">entry</span>: <span class="hljs-string">'./src/index.js'</span>, 
    output：<span class="hljs-string">'./dist/main.js'</span>,  
    <span class="hljs-attr">mode</span>: <span class="hljs-string">'production'</span>,
    <span class="hljs-attr">module</span>: &#123;
        <span class="hljs-attr">rules</span>: [&#123;
            <span class="hljs-attr">test</span>: <span class="hljs-regexp">/\.(png|svg|jpg|gif)$/</span>, 
            use: [&#123;
                <span class="hljs-attr">loader</span>: <span class="hljs-string">'file-loader'</span>,  <span class="hljs-comment">//用于处理文件</span>
                <span class="hljs-attr">options</span>: &#123;
                    <span class="hljs-attr">name</span>: <span class="hljs-string">'img/[name][hash:8].[ext]'</span>,  <span class="hljs-comment">//8: hash前8位</span>
                &#125;
            &#125;]
        &#125;]
    &#125;,
    <span class="hljs-attr">plugins</span>: [
        <span class="hljs-keyword">new</span> OptimizeCSSAssetsPlugin(&#123;
            <span class="hljs-attr">assetNameRegExp</span>: <span class="hljs-regexp">/\.css$/g</span>,
            cssProcessor: <span class="hljs-built_in">require</span>(<span class="hljs-string">'cssnano'</span>),
        &#125;)
    ],
&#125;

<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>HTML 文件的压缩</strong>  <br>
修改html-webpack-plugin,设置压缩参数</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-built_in">module</span>.exports = &#123;
    <span class="hljs-attr">entry</span>: <span class="hljs-string">'./src/index.js'</span>, 
    output：<span class="hljs-string">'./dist/main.js'</span>,  
    <span class="hljs-attr">mode</span>: <span class="hljs-string">'production'</span>,
    <span class="hljs-attr">module</span>: &#123;
        <span class="hljs-attr">rules</span>: [&#123;
            <span class="hljs-attr">test</span>: <span class="hljs-regexp">/\.(png|svg|jpg|gif)$/</span>, 
            use: [&#123;
                <span class="hljs-attr">loader</span>: <span class="hljs-string">'file-loader'</span>,  <span class="hljs-comment">//用于处理文件</span>
                <span class="hljs-attr">options</span>: &#123;
                    <span class="hljs-attr">name</span>: <span class="hljs-string">'img/[name][hash:8].[ext]'</span>,  <span class="hljs-comment">//8: hash前8位</span>
                &#125;
            &#125;]
        &#125;]
    &#125;,
    <span class="hljs-attr">plugins</span>: [
        <span class="hljs-keyword">new</span> HtmlWebpackPlugin(&#123;
            <span class="hljs-attr">template</span>: path.join(__dirname, <span class="hljs-string">'src/search.html'</span>),
            <span class="hljs-attr">fileanme</span>: <span class="hljs-string">'search.html'</span>,
            <span class="hljs-attr">chunks</span>: [<span class="hljs-string">'search'</span>],
            <span class="hljs-attr">inject</span>: <span class="hljs-literal">true</span>,
            <span class="hljs-attr">minify</span>: &#123;
                <span class="hljs-attr">html5</span>: <span class="hljs-literal">true</span>,
                <span class="hljs-attr">collapseWhitespace</span>: <span class="hljs-literal">true</span>,
                <span class="hljs-attr">preserveLineBreaks</span>: <span class="hljs-literal">false</span>,
                <span class="hljs-attr">minifyCSS</span>: <span class="hljs-literal">true</span>,
                <span class="hljs-attr">minifyJS</span>: <span class="hljs-literal">true</span>,
                <span class="hljs-attr">removeComments</span>: <span class="hljs-literal">false</span>,
            &#125;
        &#125;)
    ],
&#125;

<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-19">自动清理构建目录产物</h3>
<p><strong>通过npm scripts 清理构建目录</strong></p>
<p>rm -rf ./dist && webpack  <br>
rimraf ./dist && webpack</p>
<p><strong>自动清理构建目录</strong></p>
<p>避免构建前每次都需要手动删除dist</p>
<p>使用clean-webpack-plugin,默认会删除output指定的输出目录</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-built_in">module</span>.exports = &#123;
    <span class="hljs-attr">entry</span>: <span class="hljs-string">'./src/index.js'</span>, 
    output：<span class="hljs-string">'./dist/main.js'</span>,  
    <span class="hljs-attr">mode</span>: <span class="hljs-string">'production'</span>,
    <span class="hljs-attr">module</span>: &#123;
        <span class="hljs-attr">rules</span>: [&#123;
            <span class="hljs-attr">test</span>: <span class="hljs-regexp">/\.(png|svg|jpg|gif)$/</span>, 
            use: [&#123;
                <span class="hljs-attr">loader</span>: <span class="hljs-string">'file-loader'</span>,  <span class="hljs-comment">//用于处理文件</span>
                <span class="hljs-attr">options</span>: &#123;
                    <span class="hljs-attr">name</span>: <span class="hljs-string">'img/[name][hash:8].[ext]'</span>,  <span class="hljs-comment">//8: hash前8位</span>
                &#125;
            &#125;]
        &#125;]
    &#125;,
    <span class="hljs-attr">plugins</span>: [
        <span class="hljs-keyword">new</span> CleanWebpackPlugin()
    ],
&#125;

<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-20">PostCSS插件autoprefixer自动补齐css3前缀</h3>
<p>CSS3的属性为什么要添加前缀？
浏览器标准不统一</p>
<p>IE  Trident（-ms）  <br>
...</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-built_in">module</span>.exports = &#123;
    <span class="hljs-attr">entry</span>: <span class="hljs-string">'./src/index.js'</span>, 
    output：<span class="hljs-string">'./dist/main.js'</span>,  
    <span class="hljs-attr">mode</span>: <span class="hljs-string">'production'</span>,
    <span class="hljs-attr">module</span>: &#123;
        
        <span class="hljs-attr">rules</span>: [
            &#123;
                <span class="hljs-attr">test</span>: <span class="hljs-regexp">/.js$/</span>,
                use: <span class="hljs-string">'babel-loader'</span>
            &#125;, 
            &#123;
                <span class="hljs-comment">// 调用顺序从右到左</span>
                <span class="hljs-attr">test</span>: <span class="hljs-regexp">/.css$/</span>,
                use: [
                    <span class="hljs-string">'style-loader'</span>,
                    <span class="hljs-string">'css-loader'</span>
                ]
            &#125;, 
            &#123;
                <span class="hljs-comment">// 调用顺序从右到左</span>
                <span class="hljs-attr">test</span>: <span class="hljs-regexp">/.less$/</span>,
                use: [
                    <span class="hljs-string">'style-loader'</span>,
                    <span class="hljs-string">'css-loader'</span>,
                    <span class="hljs-string">'less-loader'</span>, 
                    &#123;
                        <span class="hljs-attr">loader</span>: <span class="hljs-string">'postcss-loader'</span>,
                        <span class="hljs-attr">options</span>: &#123;
                            <span class="hljs-attr">plugins</span>: <span class="hljs-function">() =></span> &#123;
                                <span class="hljs-built_in">require</span>(<span class="hljs-string">'autoprefixer'</span>) (&#123;
                                    <span class="hljs-attr">browsers</span>: [<span class="hljs-string">'last 2 version'</span>, <span class="hljs-string">'>1%'</span>, <span class="hljs-string">'iOS 7'</span>]
                                &#125;)
                            &#125;
                        &#125;
                    &#125;
                ]
            &#125;,
            &#123;
                <span class="hljs-attr">test</span>: <span class="hljs-regexp">/\.(png|svg|jpg|gif)$/</span>, use: [
                    <span class="hljs-string">'file-loader'</span>,  <span class="hljs-comment">//用于处理文件</span>
                ]
            &#125;,
            <span class="hljs-comment">// &#123;</span>
            <span class="hljs-comment">//     test: /\.(png|svg|jpg|gif)$/, use: [&#123;</span>
            <span class="hljs-comment">//         loader: 'url-loader',  //用于处理文件</span>
            <span class="hljs-comment">//         optins: &#123;</span>
            <span class="hljs-comment">//             limit: 10240  // 单位：字节</span>
            <span class="hljs-comment">//         &#125;</span>
            <span class="hljs-comment">//     &#125;]</span>
            <span class="hljs-comment">// &#125;,</span>
        ]
    &#125;,
    <span class="hljs-attr">plugins</span>: [
        <span class="hljs-keyword">new</span> CleanWebpackPlugin()
    ],
&#125;

<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-21">移动端px自动转换成rem</h3>
<p>css 媒体查询实现响应式布局</p>
<p>W3C对rem定义： font-size of the root element</p>
<p><strong>rem和px对比</strong>  <br>
.rem 是相对单位  <br>
.px 是绝对单位</p>
<p>使用px2rem-loaders</p>
<pre><code class="hljs language-javascript copyable" lang="javascript">&#123;
    <span class="hljs-comment">// 调用顺序从右到左</span>
    <span class="hljs-attr">test</span>: <span class="hljs-regexp">/.less$/</span>,
    use: [
        <span class="hljs-string">'style-loader'</span>,
        <span class="hljs-string">'css-loader'</span>,
        <span class="hljs-string">'less-loader'</span>,
        &#123;
            <span class="hljs-attr">loader</span>: <span class="hljs-string">'postcss-loader'</span>,
            <span class="hljs-attr">options</span>: &#123;
                <span class="hljs-attr">plugins</span>: <span class="hljs-function">() =></span> &#123;
                    <span class="hljs-built_in">require</span>(<span class="hljs-string">'autoprefixer'</span>) (&#123;
                        <span class="hljs-attr">browsers</span>: [<span class="hljs-string">'last 2 version'</span>, <span class="hljs-string">'>1%'</span>, <span class="hljs-string">'iOS 7'</span>]
                    &#125;)
                &#125;
            &#125;
        &#125;
    ]
&#125;,
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-22">资源内联</h3>
<p><strong>意义</strong></p>
<p>代码层面：</p>
<ul>
<li>页面框架的初始化脚本</li>
<li>上报相关打点</li>
<li>css内联避免页面闪动</li>
</ul>
<p>请求层面：减少http网络请求数</p>
<ul>
<li>小图片或者字体内联（url-loader）</li>
</ul>
<p><strong>hmtl和js内联</strong></p>
<p>raw-loader内联html  <br></p>
  <br>
<p>raw-loader内联js  <br></p>

<p><strong>css内联</strong></p>
<p>方案一： 借助style-loader  <br>
方案二：html-inline-css-webpack-plugin</p>
<h4 data-id="heading-23">多页面应用（MPA）概念</h4>
<p>每一次页面跳转的时候，后台服务器都会返回一个新的HTML文档，这种类型的网站也就是多页网站，也叫做多页应用。</p>
<p><strong>方案</strong>  <br>
动态获取entry和设置html-webpack-plugin数量</p>
<p>利用glob.sync</p>
<h4 data-id="heading-24">使用source map</h4>
<p>作用：通过source map定位到源代码  <br>
开发环境开启、线上环境关闭</p>
<h4 data-id="heading-25">提取公共资源</h4>
<p>思路：将React、React-Dom基础包通过cdn引入，不打入bundle中</p>
<p>方法： 使用html-webpack-externals-plugin</p>
<p>webpack 4内置：利用SplitChunksPlugin进行公共脚本分离</p>
<h4 data-id="heading-26">Tree Shaking（摇树优化）</h4>
<p>概念：1个模块可能有很多方法，只要其中的某个方法使用到了，则整个文件都会被打到bundle里面去，tree shaking就是只把用到的方法打入bundle，没用到的方法会在uglify阶段被擦除掉。</p>
<p>使⽤：webpack 默认⽀持，在 .babelrc ⾥设置 modules: false 即可
· production mode的情况下默认开启</p>
<p>要求：必须是 ES6 的语法，CJS 的⽅式不⽀持</p>
<p>DCE (Dead code elimination)   <br>
代码执⾏的结果不会被⽤到  <br>
代码不会被执⾏，不可到达  <br>
代码只会影响死变量（只写不读）</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">if</span> (<span class="hljs-literal">false</span>) &#123;
    <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'这段代码永远不会执行’);
&#125;
</span><span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>Tree-shaking 原理</strong></p>
<p>利⽤ ES6 模块的特点:</p>
<ul>
<li>只能作为模块顶层的语句出现</li>
<li>import 的模块名只能是字符串常量</li>
<li>import binding 是 immutable的</li>
</ul>
<p>代码擦除： uglify 阶段删除⽆⽤代码</p>
<h4 data-id="heading-27">代码分割的意义</h4>
<p>对于⼤的 Web 应⽤来讲，将所有的代码都放在⼀个⽂件中显然是不够有效的，特别是当你的
某些代码块是在某些特殊的时候才会被使⽤到。webpack 有⼀个功能就是将你的代码库分割成
chunks（语块），当代码运⾏到需要它们的时候再进⾏加载。</p>
<p><strong>适⽤的场景</strong></p>
<ul>
<li>抽离相同代码到⼀个共享块</li>
<li>脚本懒加载，使得初始下载的代码更⼩</li>
</ul>
<p><strong>懒加载 JS 脚本的⽅式</strong></p>
<ul>
<li>CommonJS：require.ensure</li>
<li>ES6：动态 import（⽬前还没有原⽣⽀持，需要 babel 转换）</li>
</ul>
<p><strong>如何使⽤动态 import?</strong>
安装 babel 插件 <br>
npm install @babel/plugin-syntax-dynamic-import --save-dev <br>
ES6：动态 import（⽬前还没有原⽣⽀持，需要 babel 转换） <br></p>
<pre><code class="hljs language-javascript copyable" lang="javascript">&#123;
    <span class="hljs-string">"plugins"</span>: [<span class="hljs-string">"@babel/plugin-syntax-dynamic-import"</span>],
    ...
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-28">ESLint 的必要性</h4>
<p><strong>⾏业⾥⾯优秀的 ESLint 规范实践</strong></p>
<p>Airbnb: eslint-config-airbnb、 eslint-config-airbnb-base</p>
<p>腾讯：</p>
<ul>
<li>alloyteam团队 eslint-config-alloy(<a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2FAlloyTeam%2Feslint-config-alloy" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/AlloyTeam/eslint-config-alloy" ref="nofollow noopener noreferrer">github.com/AlloyTeam/e…</a>)</li>
<li>ivweb 团队：eslint-config-ivweb(<a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Ffeflow%2Feslint-config-ivweb" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/feflow/eslint-config-ivweb" ref="nofollow noopener noreferrer">github.com/feflow/esli…</a>)</li>
</ul>
<p><strong>制定团队的 ESLint 规范</strong></p>
<p>不重复造轮⼦，基于 eslint:recommend 配置并
改进</p>
<ul>
<li>能够帮助发现代码错误的规则，全部开启</li>
<li>帮助保持团队的代码⻛格统⼀，⽽不是限制开发体验</li>
</ul>
<h3 data-id="heading-29">小结</h3>
<p>上述为我们学习webpack过程中的基础，在webpack的基础上，优化是一个亘古不变的话题，我们接下来会对常用优化手段进行总结学习。</p></div>  
</div>
            