
---
title: '前端工程化和webpack'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=4508'
author: 掘金
comments: false
date: Sat, 14 Aug 2021 01:51:42 GMT
thumbnail: 'https://picsum.photos/400/300?random=4508'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h1 data-id="heading-0">前言</h1>
<p>首先我们先了解什么是前端工程化，再来看前端工程化的有哪些解决方案解决方案，其次了解webpack的基本使用及其常用插件。最后看看webpack是如何实现打包发布的，以及如何通过Source Map来帮助我们排错。</p>
<hr color="#000000" size="1"">
<h1 data-id="heading-1">前端工程化</h1>
<h2 data-id="heading-2">一、小白眼中的前端VS实际的前端开发</h2>
<ol>
<li>小白眼中的前端</li>
</ol>
<p>只要会HTML、CSS、JavaScript就可以开发
想快速实现布局结构，layUI拿过来就成
想要操作DOM或者向服务器发送Ajax请求，拽个jQuery过来</p>
<ol start="2">
<li>实际上的前端开发</li>
</ol>
<p><code>模块化</code>(js的模块化、css的模块化、资源的模块化)
<code>组件化</code>(复用现有的UI结构、样式、行为)
<code>规范化</code>(目录结构的划分、编码规范化、接口规范化、文档规范化、Git分支管理)
<code>自动化</code>(自动化构建、自动部署、自动化测试)</p>
<h2 data-id="heading-3">二、什么是前端工程化</h2>
<p>    在企业级的前端项目开发中，把前端开发所需的<strong>工具、技术、流程、经验</strong>等进行规范化、标准化。</p>
<h2 data-id="heading-4">三、前端工程化的好处</h2>
<p>    前端开发<code>自成体系</code>，有一套标准的开发方案和流程。</p>
<h2 data-id="heading-5">四、前端工程化的解决方案</h2>
<ol>
<li>早期的前端工程化解决方案</li>
</ol>
<p>grunt(<code>https://www.gruntjs.net/</code>)
gulp(<code>https://www.gulpjs.com.cn/</code>)
2. 目前主流的前端工程化解决方案
webpack(<code>https://www.webpackjs.com/</code>)
parcel(<code>https://zh.parceljs.org/</code>)</p>

<h1 data-id="heading-6">webpack</h1>
<h2 data-id="heading-7">一、什么是webpack</h2>
<h3 data-id="heading-8">1、概念</h3>
<p>    前端项目工程化的具体解决方案</p>
<h3 data-id="heading-9">2、 主要功能</h3>
<p>    能提供友好的前端模块化开发支持，以及<code>代码压缩混淆</code>、<code>处理浏览器端JavaScript的兼容性</code>、<code>性能优化</code>等强大的功能</p>
<h3 data-id="heading-10">3、好处</h3>
<p>    让程序员把工作的重心放到具体功能的实现上，提高了前端<code>开发效率</code>和项目的<code>可维护性</code>。·</p>
<h2 data-id="heading-11">二、webpack基本使用</h2>
<h3 data-id="heading-12">1、在项目中安装webpack</h3>
<p><code>npm install webpack@5.42.1 webpack-cli@4.7.2 -D</code></p>
<h3 data-id="heading-13">2、在项目中配置webpack</h3>
<p>在文件根目录下新建 <code>webpack.config.js</code>文件，在文件中书写以下代码</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-built_in">module</span>.exports = &#123;
    <span class="hljs-comment">// 指定构建模式，有两个参数可选</span>
    <span class="hljs-comment">// 开发阶段使用development,因为打包速度快</span>
    <span class="hljs-comment">// 上线阶段使用production,因为项目上线需要文件体积小</span>
    <span class="hljs-attr">mode</span>:<span class="hljs-string">'development'</span>
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<ol>
<li>mode节点可选值</li>
</ol>
<ul>
<li>development</li>
</ul>
<p><code>开发环境</code>
不会对打包生成的文件进行代码压缩和性能优化
打包速度快，适合开发阶段使用</p>
<ul>
<li>production</li>
</ul>
<p><code>生产环境</code>
会对打包生成的文件进行代码压缩和性能优化
打包速度慢，仅适合项目发布阶段使用</p>
<ol start="2">
<li>webpack.config.js文件的作用</li>
</ol>
<p>webpack.config.js是webpack的配置文件。webpack在真正开始打包构建之前，<strong>会先读取这个配置文件</strong>，从而基于给定的配置，对项目进行打包。
<code>注</code>：由于webpack是基于node.js开发出来的打包工具,因此在它的配置文件中，支持使用node.js相关的语法和模块进行webpack的个性化配置。</p>
<p>在<code>package.json</code>的scripts节点下，新增 dev 脚本如下</p>
<pre><code class="hljs language-json copyable" lang="json"><span class="hljs-string">"scripts"</span>:&#123;
    <span class="hljs-comment">// npm run dev</span>
    <span class="hljs-attr">"dev"</span>:<span class="hljs-string">"webpack"</span>
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>在cmd终端中运行<code>npm run dev</code>,启动webpack进行项目的打包构建</p>
<h3 data-id="heading-14">3、webpack打包入口、出口</h3>
<ol>
<li>默认约定</li>
</ol>
<p>在webpack 4.x 和 5.x 版本中，有如下的默认约定
①默认的打包<strong>入口文件</strong>为 src -> index.js
②默认的<strong>输出文件</strong>路径为 dist -> main.js
2. 自定义打包的入口与出口
在<code>webpack.config.js</code>配置文件中，通过<code>entry</code>节点指定打包的入口。通过<code>output </code>节点指定打包的出口</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> path = <span class="hljs-built_in">require</span>(<span class="hljs-string">'path'</span>)

<span class="hljs-built_in">module</span>.exports = &#123;
    <span class="hljs-attr">mode</span>:<span class="hljs-string">'development'</span>,
    <span class="hljs-comment">//entry:'指定要处理哪个文件'</span>
    <span class="hljs-attr">entry</span>:path.join(__dirname,<span class="hljs-string">'src/xxx.js'</span>),
    <span class="hljs-comment">//指定生成的文件要存放到哪里</span>
    <span class="hljs-attr">output</span>:&#123;
        <span class="hljs-comment">//存放的目录</span>
        <span class="hljs-attr">path</span>: path.join(__dirname,<span class="hljs-string">'dist'</span>),
        <span class="hljs-comment">//生成的文件名</span>
        <span class="hljs-attr">filename</span>: <span class="hljs-string">'bundle.js'</span>
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<ol start="3">
<li>问题：每次修改源代码，都需要在终端执行 <code>npm run dev </code>命令。十分的麻烦!</li>
</ol>
<h2 data-id="heading-15">三、webpack中的插件</h2>
<h3 data-id="heading-16">1、webpack插件的作用</h3>
<p>通过安装和配置第三方的插件，可以<strong>拓展webpack的能力</strong>，从而让webpack用起来更方便。</p>
<h3 data-id="heading-17">2、常用的插件</h3>
<ol>
<li>webpack-dev-server</li>
</ol>
<ul>
<li><strong>作用</strong></li>
</ul>
<p>类似于node.js阶段用到的nodemon工具
每当修改了源代码，webpack会自动进行项目的打包和构建</p>
<ul>
<li><strong>npm命令</strong></li>
</ul>
<p>终端中运行如下命令 <code>npm install webpack-dev-server@3.11.2 -D</code></p>
<ul>
<li><strong>配置</strong></li>
</ul>
<p>修改 <code>package.json </code>-> scripts中的 dev 命令中如下
再次运行 <code>npm run dev</code>命令，重新进行项目的打包
在浏览器中访问 <code>http://localhost:8080</code> 查看打包效果</p>
<pre><code class="hljs language-json copyable" lang="json"><span class="hljs-string">"scripts"</span>: &#123;
   <span class="hljs-attr">"dev"</span>:<span class="hljs-string">"webpack serve"</span>
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><code>注</code>：生成的出口文件在根目录中，是保存在<code>内存</code>中的</p>
<ol start="2">
<li>html-webpack-plugin</li>
</ol>
<ul>
<li><strong>作用</strong></li>
</ul>
<p>webpack中的HTML插件
可以通过此插件自定制index.html页面的内容</p>
<ul>
<li><strong>npm命令</strong></li>
</ul>
<p>终端中运行如下命令 <code>npm install html-webpack-plugin@5.3.2 -D</code></p>
<ul>
<li><strong>配置</strong></li>
</ul>
<p>在 webpack.config.js 文件中配置</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">//导入 html-webpack-plugin 这个插件，得到插件的构造函数</span>
<span class="hljs-keyword">const</span> HtmlPlugin = <span class="hljs-built_in">require</span>(<span class="hljs-string">'html-webpack-plugin'</span>)

<span class="hljs-comment">//创建 html 插件的实例对象</span>
<span class="hljs-keyword">const</span> htmlPlugin = <span class="hljs-keyword">new</span> HtmlPlugin(&#123;
    <span class="hljs-comment">//指定原文件的存放路径</span>
    <span class="hljs-attr">template</span>:<span class="hljs-string">'./src/index.html'</span>,
    <span class="hljs-comment">//指定生成的文件的存放路径</span>
    <span class="hljs-attr">filename</span>:<span class="hljs-string">'./index.html'</span>
&#125;)

<span class="hljs-built_in">module</span>.exports = &#123;
    <span class="hljs-attr">mode</span>:<span class="hljs-string">'development'</span>,
    <span class="hljs-comment">//通过 plugins 节点，是 htmlPlugin 生效</span>
    <span class="hljs-comment">//插件的数组，将来 webpack 在运行时，会加载调用这些插件</span>
    <span class="hljs-attr">plugins</span>:[htmlPlugin]
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><code>注</code>：会在 index.html 中自动注入一个script脚本
        复制的index.html页面同样保存在<code>内存</code>中</p>
<h3 data-id="heading-18">3、devServer节点</h3>
<p>在<code>webpack.config.js</code>中添加如下</p>
<pre><code class="hljs language-js copyable" lang="js">devServer : &#123;
    <span class="hljs-comment">//初次打包后自动打开浏览器</span>
    <span class="hljs-attr">open</span>:<span class="hljs-literal">true</span>，
    <span class="hljs-comment">//修改端口号</span>
    <span class="hljs-comment">//在http协议中，如果端口号是80,则可以被省略</span>
    <span class="hljs-attr">port</span>:<span class="hljs-number">80</span>,
    <span class="hljs-comment">//指定运行的主机地址</span>
    <span class="hljs-attr">host</span>:<span class="hljs-string">'127.0.0.1'</span>
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><code>注</code>：凡是修改了webpack.config.js配置文件，或修改了package.json配置文件，<strong>必须重启实时打包的服务器</strong>，否则最新的配置文件无法生效!</p>
<h2 data-id="heading-19">四、webpack中的loader(加载器)</h2>
<p>在实际开发过程中，webpack默认只能打包处理以 .js 后缀名结尾的模块。其他非 .js 后缀名结尾的模块，webpack默认处理不了,<strong>需要调用loader加载器才可以正常打包</strong>，否则会报错!</p>
<h3 data-id="heading-20">1、loader加载器的作用</h3>
<p>协助webpack打包处理特定的文件模块。</p>
<h3 data-id="heading-21">2、常用的loader加载器</h3>
<ul>
<li>打包处理css 文件(css-loader)</li>
<li>npm命令</li>
</ul>
<p>运行 <code>npm i style-loader@3.0.0 css-loader@5.2.6 -D</code></p>
<ul>
<li>配置</li>
</ul>
<p>在 <code>webpack.config.js</code> 的module -> rules 数组中，添加 loader 规则如下</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-built_in">module</span>:&#123;
    <span class="hljs-attr">rules</span>:[
        <span class="hljs-comment">//test是文件类型</span>
        <span class="hljs-comment">//use表示对应要调用的loader</span>
        &#123;<span class="hljs-attr">test</span>:<span class="hljs-regexp">/\.css$/</span>,use:[<span class="hljs-string">'style-loader'</span>,<span class="hljs-string">'css-loader'</span>]&#125;
    ]
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><code>注</code>：use中的loader顺序是<strong>固定的</strong>，调用顺序<strong>从后往前调用</strong>。</p>
<ul>
<li>打包处理less文件(less-loader)</li>
<li>npm命令</li>
</ul>
<p>运行<code>npm i less-loader@10.0.1 less@4.1.1 -D</code>命令</p>
<ul>
<li>配置</li>
</ul>
<p>在 <code>webpack.config.js </code>的module -> rules 数组中，添加 loader 规则如下</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-built_in">module</span>:&#123;
    <span class="hljs-attr">rules</span>:[
        <span class="hljs-comment">//文件后缀名的匹配规则</span>
        &#123;<span class="hljs-attr">test</span>:<span class="hljs-regexp">/\.less$/</span>,use:[<span class="hljs-string">'style-loader'</span>,<span class="hljs-string">'css-loader'</span>,<span class="hljs-string">'less-loader'</span>]&#125;
    ]
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>打包处理样式表中与url路径相关的文件（file-loader）</li>
<li>npm命令</li>
</ul>
<p>运行<code>npm i url-loader@4.1.1 file-loader@6.2.0 -D</code></p>
<ul>
<li>配置</li>
</ul>
<p>在 <code>webpack.config.js</code> 的module -> rules 数组中，添加 loader 规则如下</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-built_in">module</span>:&#123;
    <span class="hljs-attr">rules</span>:[
        <span class="hljs-comment">//处理图片文件的loader</span>
        <span class="hljs-comment">//如果需要调用的 loader 只有一个，则值传递一个字符串也行，如有多个loader</span>
        &#123;<span class="hljs-attr">test</span>:<span class="hljs-regexp">/\.jpg|png|gif$/</span>,use:<span class="hljs-string">'url-loader?limit-22229'</span>&#125;
    ]
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>其中 <code>?</code> 之后的是loader的参数项：</p>
<pre><code class="copyable">limit用来指定**图片的大小**，单位是字节(byte)
只有 ≤ limit 大小的图片，才会被转为base64格式的图片
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>打包处理js文件中的高级语法(babel-loader)</li>
<li>npm命令</li>
</ul>
<p>运行<code>npm i babel-loader@8.2.2 @babel/core@7.14.6 @babel/plugin-proposal-decorators@7.14.5 -D</code></p>
<ul>
<li>配置</li>
</ul>
<p>在 webpack.config.js 的module -> rules 数组中，添加 loader 规则如下</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-built_in">module</span>:&#123;
    <span class="hljs-attr">rules</span>:[
        <span class="hljs-comment">//在配置babel-loader的时候，程序员只需要把自己的代码进行转换即可；一定要排除 node_modules目录中的js文件</span>
        &#123;<span class="hljs-attr">test</span>:<span class="hljs-regexp">/\.js$/</span>,use:<span class="hljs-string">'babel-loader'</span>,<span class="hljs-attr">exclude</span>:<span class="hljs-regexp">/node_modules/</span>&#125;
    ]
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>        根目录新建<code>babel.config.js</code>,定义Babel的配置项如下:</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-built_in">module</span>.exports = &#123;
    <span class="hljs-comment">//声明babel可用的插件</span>
    <span class="hljs-attr">plugins</span>:[[<span class="hljs-string">'@babel/plugin-proposal-decorators'</span>,&#123;<span class="hljs-attr">legacy</span>:<span class="hljs-literal">true</span>&#125;]]
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h1 data-id="heading-22">打包发布</h1>
<h2 data-id="heading-23">一、为什么要打包发布？</h2>
<ul>
<li>开发环境下，打包生成的文件存放于内存中，无法获取到最终打包生成的文件</li>
<li>开发环境下，打包生成的文件不会进行代码压缩和性能优化</li>
</ul>
<h2 data-id="heading-24">二、配置 webpack的打包发布</h2>
<p>在 <code>package.json </code>文件的 scripts 节点下，新增build 命令如下：</p>
<pre><code class="hljs language-json copyable" lang="json"><span class="hljs-string">"scripts"</span>:&#123;
    <span class="hljs-comment">//开发环境中，运行 dev 命令</span>
    <span class="hljs-attr">"dev"</span>:<span class="hljs-string">"webpack serve"</span>,
     <span class="hljs-comment">//项目发布时，运行build命令</span>
    <span class="hljs-attr">"build"</span>:<span class="hljs-string">"webpack --mode production"</span>
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>--model 是一个参数项，用来指定 webpack 的运行模式。production代表生产环境，会对打包生成的文件进行代码压缩和性能优化。</p>
<p><code>注</code>：通过--model指定的参数项，会覆盖 <code>webpack.config.js</code>中的model选项</p>
<h3 data-id="heading-25">1、把JavaScript文件统一生成到js目录中</h3>
<p>在<code>webpack.config.js</code>配置文件的<code>output</code>节点中，进行如下配置：</p>
<pre><code class="hljs language-js copyable" lang="js">output: &#123;
<span class="hljs-attr">path</span>: path.join(__dirname,<span class="hljs-string">'dist'</span>),
<span class="hljs-comment">// 明确告诉 webpack 把生成的 bundle.js 文件放到 dist 目录下的 js 子目录中</span>
<span class="hljs-attr">filename</span>: <span class="hljs-string">'js/bundle.js'</span>
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-26">2、把图片文件统一生成到image目录中</h3>
<p>修改 <code>webpack.config.js</code>中的 <code>url-loader</code>配置项，新增<code>outputPath</code>选项即可指定图片文件的输出路径：</p>
<pre><code class="hljs language-js copyable" lang="js">&#123;
<span class="hljs-attr">test</span>: <span class="hljs-regexp">/\.jpg|png|gif$/</span>,
use: &#123;
<span class="hljs-attr">loader</span>: <span class="hljs-string">'url-loader'</span>,
<span class="hljs-attr">options</span>: &#123;
<span class="hljs-attr">limit</span>: <span class="hljs-number">22228</span>,
<span class="hljs-comment">// 明确指定把打包生成的图片文件，存储到 dist 目录下的image 文件夹中</span>
<span class="hljs-attr">outputPath</span>: <span class="hljs-string">'image'</span>
&#125;
&#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-27">3、自动清理dist目录下的旧文件</h3>
<p>参考网址：<code>https://www.npmjs.com/package/clean-webpack-plugin</code></p>
<h1 data-id="heading-28">Source Map</h1>
<h2 data-id="heading-29">一、Source Map是什么?</h2>
<p>就是一个信息文件，里面存储这位置信息。也就是说， Source Map文件中存储着压缩混淆后的代码，所对应的转换前的位置。</p>
<h2 data-id="heading-30">二、 如何使用？</h2>
<ol>
<li>开发环境下</li>
</ol>
<p>推荐在 <code>webpack.config.js</code> 中添加如下的配置，即可保证<code>运行时报错的行数</code>与<code>源代码的行数</code>保持一致</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-built_in">module</span>.exports = &#123;
    <span class="hljs-attr">mode</span>:<span class="hljs-string">'development'</span>,
    <span class="hljs-attr">devtool</span>:<span class="hljs-string">'eval-source-map'</span>
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<ol start="2">
<li>生产环境下</li>
</ol>
<p>如果省略了 devtool 选项，则最终生成的文件中不包含 Source Map。这能够防止原始代码通过 Source Map的形式暴露给别有所图之人。
或者将 <code>devtool</code>的值设置为<code>nosources-source-map</code>,这样只会定位出错行数，而不暴露源码。</p>
<h1 data-id="heading-31">补充</h1>
<h1 data-id="heading-32">一、npm命令补充</h1>
<ol>
<li>-S 是<code>--save</code>的简写</li>
</ol>
<p>明确告诉npm将第三方模块名称和版本号写在dependencies中
2. -D是<code>--save-dev</code>的简写
-D  明确告诉npm 将该文件放到devDependencies中
只在开发阶段需要用到,就使用 -D 将文件放到devDependencies中</p>
<h1 data-id="heading-33">二、使用 @ 表示src源代码目录</h1>
<p>在 <code>webpack.config.js</code>中新增一个  <code>resolve</code>节点</p>
<pre><code class="hljs language-js copyable" lang="js">resolve:&#123;
    <span class="hljs-attr">alias</span>:&#123;
        <span class="hljs-comment">//告诉 webpack ,程序员写的代码中，@符号表示 src 这一层目录</span>
        <span class="hljs-string">'@'</span>:path.join(__dirname,<span class="hljs-string">'/src/'</span>)
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<hr color="#000000" size="1"">
<h1 data-id="heading-34">总结</h1>
<p>关于前端工程化的解决方案，Vue为我们提供了 Vue CLI脚手架工具，其基于 webpack 构建，并带有合理的默认配置。可以让我们更专注撰写应用上，而不用花费好几天的时间纠结配置的问题。最后给大家奉上Vue CLI官网地址<code>https://cli.vuejs.org/zh/</code>，今天就到这里，拜拜~</p></div>  
</div>
            