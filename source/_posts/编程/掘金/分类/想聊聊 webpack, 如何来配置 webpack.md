
---
title: '想聊聊 webpack, 如何来配置 webpack'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/902fd719ecbf43ffac6d93a7ef59627e~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Sat, 14 Aug 2021 18:04:47 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/902fd719ecbf43ffac6d93a7ef59627e~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h1 data-id="heading-0">webpack 的基本使用</h1>
<h2 data-id="heading-1">1.什么是 webpack</h2>
<p>概念：webpack 是前端项目工程化的具体解决方案。</p>
<p>主要功能：它提供了友好的前端模块化开发支持，以及代码压缩混淆、处理浏览器端 JavaScript 的兼容性、性</p>
<p>能优化等强大的功能。</p>
<p>好处：让程序员把工作的重心放到具体功能的实现上，提高了前端开发效率和项目的可维护性。</p>
<blockquote>
<p>注意：目前 Vue，React 等前端项目，基本上都是基于 webpack 进行工程化开发的。</p>
</blockquote>
<h2 data-id="heading-2">2.在项目中安装 webpack</h2>
<p>在终端运行如下的命令，安装 webpack 相关的两个包：</p>
<pre><code class="hljs language-js copyable" lang="js">npm install webpack@<span class="hljs-number">5.42</span><span class="hljs-number">.1</span> webpack-cli@<span class="hljs-number">4.7</span><span class="hljs-number">.2</span> -D
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-3">3.在项目中配置 webpack</h2>
<ol>
<li>在项目根目录中，创建名为 webpack.config.js 的 webpack 配置文件，并初始化如下的基本配置：</li>
</ol>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-built_in">module</span>.export = &#123;
    <span class="hljs-attr">mode</span>: <span class="hljs-string">'development'</span> <span class="hljs-comment">// mode 用来指定构建模式。可选值有 development 和 production</span>
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<ol start="2">
<li>在 package.json 的 scripts 节点下，新增 dev 脚本如下：</li>
</ol>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-string">"scripts"</span>: &#123;
    <span class="hljs-string">"dev"</span>: <span class="hljs-string">"webpack"</span> <span class="hljs-comment">// script 节点下的脚本，可以通过 npm run 执行。例 npm run dev</span>
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<ol start="3">
<li>在终端中运行 npm run dev 命令，启动 webpack 进行项目的打包构建</li>
</ol>
<h3 data-id="heading-4">3.1 mode 的可选值</h3>
<p>mode 节点的可选值有两个，分别是：</p>
<p>① <strong>development</strong></p>
<p>开发环境</p>
<p>不会对打包生成的文件进行代码压缩和性能优化</p>
<p>打包速度快，适合在开发阶段使用</p>
<p>② <strong>production</strong></p>
<p>生产环境</p>
<p>会对打包生成的文件进行代码压缩和性能优化</p>
<p>打包速度很慢，仅适合在项目发布阶段使用</p>
<h3 data-id="heading-5">3.2 webpack.config.js 文件的作用</h3>
<p>webpack.config.js 是 webpack 的配置文件。webpack 在真正开始打包构建之前，会先读取这个配置文件，</p>
<p>从而基于给定的配置，对项目进行打包。</p>
<blockquote>
<p>注意：由于 webpack 是基于 node.js 开发出来的打包工具，因此在它的配置文件中，支持使用 node.js 相关的语法和模块进行 webpack 的个性化配置。</p>
</blockquote>
<h3 data-id="heading-6">3.3 webpack 中的默认约定</h3>
<p>在 webpack 4.x 和 5.x 的版本中，有如下的默认约定：</p>
<ol>
<li>
<p>默认的打包入口文件为 src -> index.js</p>
</li>
<li>
<p>默认的输出文件路径为 dist -> main.js</p>
</li>
</ol>
<blockquote>
<p>注意：可以在 webpack.config.js 中修改打包的默认约定</p>
</blockquote>
<h3 data-id="heading-7">3.4 自定义打包的入口与出口</h3>
<p>在 webpack.config.js 配置文件中，通过 entry 节点指定打包的入口。通过 output 节点指定打包的出口。</p>
<p>示例代码如下：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> path = requuire(<span class="hljs-string">'path'</span>) <span class="hljs-comment">// 导入 node.js 中专门操作路径的模块</span>

<span class="hljs-built_in">module</span>.export = &#123;
    <span class="hljs-attr">entry</span>: path.join(__dirname, <span class="hljs-string">'./src/index.js'</span>), <span class="hljs-comment">// 打包入口文件的路径</span>
    <span class="hljs-attr">output</span>: &#123;
        <span class="hljs-attr">path</span>: path.join(__dirname, <span class="hljs-string">'./dist'</span>), <span class="hljs-comment">// 输出文件的存放路径</span>
        <span class="hljs-attr">filename</span>: <span class="hljs-string">'bundle.js'</span> <span class="hljs-comment">// 输出文件的名称</span>
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h1 data-id="heading-8">webpack 中的插件</h1>
<h2 data-id="heading-9">1. webpack 插件的作用</h2>
<p>通过安装和配置第三方的插件，可以拓展 webpack 的能力，从而让 webpack 用起来更方便。最常用的</p>
<p>webpack 插件有如下两个：</p>
<ol>
<li>**webpack-dev-server **</li>
</ol>
<p>类似于 node.js 阶段用到的 nodemon 工具</p>
<p>每当修改了源代码，webpack 会自动进行项目的打包和构建</p>
<p>webpack-dev-server 可以让 webpack 监听项目源代码的变化，从而进行自动打包构建。</p>
<ol start="2">
<li><strong>html-webpack-plugin</strong></li>
</ol>
<p>webpack 中的 HTML 插件（类似于一个模板引擎插件）</p>
<p>可以通过此插件自定制 index.html 页面的内容</p>
<p>html-webpack-plugin 是 webpack 中的 HTML 插件，可以通过此插件自定制 index.html 页面的内容。</p>
<p>需求：通过 html-webpack-plugin 插件，将 src 目录下的 index.html 首页，复制到项目根目录中一份！</p>
<h2 data-id="heading-10">2.webpack-dev-server</h2>
<h3 data-id="heading-11">2.1 安装 webpack-dev-server</h3>
<pre><code class="hljs language-js copyable" lang="js">npm install webpack-dev-server@<span class="hljs-number">3.11</span><span class="hljs-number">.2</span> -D
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-12">2.2 配置 webpack-dev-server</h3>
<ol>
<li>修改 package.json -> scripts 中的 dev 命令如下：</li>
</ol>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-string">"scripts"</span>: &#123;
    <span class="hljs-string">"dev"</span>: <span class="hljs-string">"webpack serve"</span>, <span class="hljs-comment">// script 节点下的脚本，可以通过 npm run 执行</span>
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<ol start="2">
<li>
<p>再次运行 npm run dev 命令，重新进行项目的打包</p>
</li>
<li>
<p>在浏览器中访问 <a href="https://link.juejin.cn/?target=http%3A%2F%2Flocalhost%3A8080" target="_blank" rel="nofollow noopener noreferrer" title="http://localhost:8080" ref="nofollow noopener noreferrer">http://localhost:8080</a> 地址，查看自动打包效果</p>
</li>
</ol>
<blockquote>
<p>注意：webpack-dev-server 会启动一个实时打包的 http 服务器</p>
</blockquote>
<h3 data-id="heading-13">2.3 打包生成的文件哪儿去了？</h3>
<ol>
<li>不配置 webpack-dev-server 的情况下，webpack 打包生成的文件，会存放到实际的物理磁盘上</li>
</ol>
<p>​    严格遵守开发者在 webpack.config.js 中指定配置</p>
<p>​    根据 output 节点指定路径进行存放</p>
<ol start="2">
<li>配置了 webpack-dev-server 之后，打包生成的文件存放到了内存中</li>
</ol>
<p>​    不再根据 output 节点指定的路径，存放到实际的物理磁盘上</p>
<p>​    提高了实时打包输出的性能，因为内存比物理磁盘速度快很多</p>
<h3 data-id="heading-14">2.4 生成到内存中的文件该如何访问？</h3>
<p>webpack-dev-server 生成到内存中的文件，默认放到了项目的根目录中，而且是虚拟的、不可见的。</p>
<p>可以直接用 / 表示项目根目录，后面跟上要访问的文件名称，即可访问内存中的文件</p>
<p>例如 /bundle.js 就表示要访问 webpack-dev-server 生成到内存中的 bundle.js 文件</p>
<h2 data-id="heading-15">3.html-webpack-plugin</h2>
<h3 data-id="heading-16">3.1 安装 html-webpack-plugin</h3>
<pre><code class="hljs language-js copyable" lang="js">npm install html-webpack-plugin@<span class="hljs-number">5.3</span><span class="hljs-number">.2</span> -D
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-17">3.2 配置 html-webpack-plugin</h3>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// 1. 导入 HTML 插件，得到一个构造函数</span>
<span class="hljs-keyword">const</span> HtmlPlugin = <span class="hljs-built_in">require</span>(<span class="hljs-string">'html-webpack-plugin'</span>)

<span class="hljs-comment">// 2. 创建 HTML 插件的实例对象</span>
<span class="hljs-keyword">const</span> htmlPlugin = <span class="hljs-keyword">new</span> HtmlPlugin(&#123;
    <span class="hljs-attr">template</span>: <span class="hljs-string">'./src/index.html'</span>, <span class="hljs-comment">// 指定原文件的存放路径</span>
    <span class="hljs-attr">filename</span>: <span class="hljs-string">'./index.html'</span> <span class="hljs-comment">// 指定生成的文件的存放路径</span>
&#125;)

<span class="hljs-built_in">module</span>.export = &#123;
    <span class="hljs-attr">mode</span>: <span class="hljs-string">'development'</span>,
    <span class="hljs-attr">plugins</span>: [htmlPlugin], <span class="hljs-comment">// 3. 通过 plugin 节点，使 htmlPlugin 插件生效</span>
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-18">3.3 解惑 html-webpack-plugin</h3>
<p>通过 HTML 插件复制到项目根目录中的 index.html 页面，也被放到了内存中</p>
<p>HTML 插件在生成的 index.html 页面，自动注入了打包的 bundle.js 文件</p>
<h2 data-id="heading-19">4. devServer 节点</h2>
<p>在 webpack.config.js 配置文件中，可以通过 devServer 节点对 webpack-dev-server 插件进行更多的配置，</p>
<p>示例代码如下：</p>
<pre><code class="hljs language-js copyable" lang="js">devServer: &#123;
    <span class="hljs-attr">open</span>: <span class="hljs-literal">true</span>, <span class="hljs-comment">// 初次打包完成后，自动打开浏览器</span>
    <span class="hljs-attr">host</span>: <span class="hljs-string">'127.0.0.1'</span>, <span class="hljs-comment">// 实时打包所使用的主机地址</span>
    <span class="hljs-attr">port</span>: <span class="hljs-number">80</span>, <span class="hljs-comment">// 实时打扮所使用的端口号</span>
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<blockquote>
<p>注意：凡是修改了 webpack.config.js 配置文件，或修改了 package.json 配置文件，必须重启实时打包的服</p>
<p>务器，否则最新的配置文件无法生效！</p>
</blockquote>
<h1 data-id="heading-20">webpack 中的 loader</h1>
<h2 data-id="heading-21">1. loader 概述</h2>
<p>在实际开发过程中，webpack 默认只能打包处理以 .js 后缀名结尾的模块。其他非 .js 后缀名结尾的模块，</p>
<p>webpack 默认处理不了，需要调用 loader 加载器才可以正常打包，否则会报错！</p>
<p>loader 加载器的作用：协助 webpack 打包处理特定的文件模块。比如：</p>
<blockquote>
<p>css-loader 可以打包处理 .css 相关的文件</p>
</blockquote>
<blockquote>
<p>less-loader 可以打包处理 .less 相关的文件</p>
</blockquote>
<blockquote>
<p>babel-loader 可以打包处理 webpack 无法处理的高级 JS 语法</p>
</blockquote>
<h2 data-id="heading-22">2. loader 的调用过程</h2>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/902fd719ecbf43ffac6d93a7ef59627e~tplv-k3u1fbpfcp-watermark.image" alt="在这里插入图片描述" loading="lazy" referrerpolicy="no-referrer">
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/b09478de2dd64c24880c499a8347c9a2~tplv-k3u1fbpfcp-watermark.image" alt="在这里插入图片描述" loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-23">3. 打包处理 css 文件</h2>
<ol>
<li>
<p>运行 npm i <a href="https://link.juejin.cn/?target=mailto%3Astyle-loader%403.0.0" target="_blank" title="mailto:style-loader@3.0.0" ref="nofollow noopener noreferrer">style-loader@3.0.0</a> <a href="https://link.juejin.cn/?target=mailto%3Acss-loader%405.2.6" target="_blank" title="mailto:css-loader@5.2.6" ref="nofollow noopener noreferrer">css-loader@5.2.6</a> -D 命令，安装处理 css 文件的 loader</p>
</li>
<li>
<p>在 webpack.config.js 的 module -> rules 数组中，添加 loader 规则如下：</p>
</li>
</ol>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-built_in">module</span>: &#123;
    <span class="hljs-attr">rules</span>: [
        &#123;<span class="hljs-attr">test</span>: <span class="hljs-regexp">/\.css$/</span>, use: [<span class="hljs-string">'style-loader'</span>, <span class="hljs-string">'css-loader'</span>]&#125;
    ]
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>其中，test 表示匹配的文件类型， use 表示对应要调用的 loader</p>
<blockquote>
<p>注意：</p>
<p>use 数组中指定的 loader 顺序是固定的</p>
<p>多个 loader 的调用顺序是：从后往前调用</p>
</blockquote>
<h2 data-id="heading-24">4. 打包处理 less 文件</h2>
<ol>
<li>
<p>运行 npm i <a href="https://link.juejin.cn/?target=mailto%3Aless-loader%4010.0.1" target="_blank" title="mailto:less-loader@10.0.1" ref="nofollow noopener noreferrer">less-loader@10.0.1</a> <a href="https://link.juejin.cn/?target=mailto%3Aless%404.1.1" target="_blank" title="mailto:less@4.1.1" ref="nofollow noopener noreferrer">less@4.1.1</a> -D 命令</p>
</li>
<li>
<p>在 webpack.config.js 的 module -> rules 数组中，添加 loader 规则如下：</p>
</li>
</ol>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-built_in">module</span>: &#123;
    <span class="hljs-attr">rules</span>: [
        &#123;<span class="hljs-attr">test</span>: <span class="hljs-regexp">/\.less$/</span>, use: [<span class="hljs-string">'style-loader'</span>, <span class="hljs-string">'css-loader'</span>, <span class="hljs-string">'less-loader'</span>]&#125;
    ]
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-25">5. 打包处理样式表中与url 路径相关的文件</h2>
<ol>
<li>
<p>运行 npm i <a href="https://link.juejin.cn/?target=mailto%3Aless-loader%4010.0.1" target="_blank" title="mailto:less-loader@10.0.1" ref="nofollow noopener noreferrer">less-loader@10.0.1</a> <a href="https://link.juejin.cn/?target=mailto%3Aless%404.1.1" target="_blank" title="mailto:less@4.1.1" ref="nofollow noopener noreferrer">less@4.1.1</a> -D 命令</p>
</li>
<li>
<p>在 webpack.config.js 的 module -> rules 数组中，添加 loader 规则如下：</p>
</li>
</ol>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-built_in">module</span>: &#123;
    <span class="hljs-attr">rules</span>: [
        &#123;<span class="hljs-attr">test</span>: <span class="hljs-regexp">/\.jpg|png|gif$/</span>, use: <span class="hljs-string">'url-loader?limit=22229'</span>&#125;
    ]
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<blockquote>
<p>其中 ? 之后的是 loader 的参数项：</p>
<p>limit 用来指定图片的大小，单位是字节（byte）</p>
<p>只有 ≤ limit 大小的图片，才会被转为 base64 格式的图片</p>
</blockquote>
<h2 data-id="heading-26">6. 打包处理 js 文件中的高级语法</h2>
<p>webpack 只能打包处理一部分高级的 JavaScript 语法。对于那些 webpack 无法处理的高级 js 语法，需要借</p>
<p>助于 babel-loader 进行打包处理。例如 webpack 无法处理下面的 JavaScript 代码：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// 1. 定义了名为 info 的装饰器</span>
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">info</span>(<span class="hljs-params">target</span>) </span>&#123;
    <span class="hljs-comment">// 2. 为咪表添加静态属性 info</span>
    target.info = <span class="hljs-string">'Person info'</span>
&#125;

<span class="hljs-comment">// 3. 为 Person 类应用 info 装饰器</span>
@info
<span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Person</span> </span>&#123;&#125;

<span class="hljs-comment">// 4. 打印 Person 的静态属性 info</span>
<span class="hljs-built_in">console</span>.log(Persion.info)
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-27">6.1 安装 babel-loader 相关的包</h3>
<pre><code class="hljs language-js copyable" lang="js">npm i babel-loader@<span class="hljs-number">8.2</span><span class="hljs-number">.2</span> @babel/core@<span class="hljs-number">7.14</span><span class="hljs-number">.6</span> @babel/plugin-proposal-decorators@<span class="hljs-number">7.14</span><span class="hljs-number">.5</span> -D
<span class="copy-code-btn">复制代码</span></code></pre>
<p>在 webpack.config.js 的 module -> rules 数组中，添加 loader 规则如下：</p>
<pre><code class="hljs language-js copyable" lang="js">&#123; <span class="hljs-attr">test</span>: <span class="hljs-regexp">/\.js$/</span>, use: <span class="hljs-string">'babel=loader'</span>, <span class="hljs-attr">exclude</span>: <span class="hljs-regexp">/node_modules/</span> &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-28">6.2 配置 babel-loader</h3>
<p>在项目根目录下，创建名为 babel.config.js 的配置文件，定义 Babel 的配置项如下：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-built_in">module</span>.exports = &#123;
    <span class="hljs-attr">plugins</span>: [[<span class="hljs-string">'@babel/pligin-proposal=decorators'</span>, &#123;<span class="hljs-attr">legacy</span>: <span class="hljs-literal">true</span>&#125;]]
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h1 data-id="heading-29">打包发布</h1>
<h2 data-id="heading-30">1. 为什么要打包发布</h2>
<p>项目开发完成之后，需要使用 webpack 对项目进行打包发布，主要原因有以下两点：</p>
<ol>
<li>
<p>开发环境下，打包生成的文件存放于内存中，无法获取到最终打包生成的文件</p>
</li>
<li>
<p>开发环境下，打包生成的文件不会进行代码压缩和性能优化</p>
</li>
</ol>
<p>为了让项目能够在生产环境中高性能的运行，因此需要对项目进行打包发布。</p>
<h2 data-id="heading-31">2. 配置 webpack 的打包发布</h2>
<p>在 package.json 文件的 scripts 节点下，新增 build 命令如下：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-string">"scripts"</span>: &#123;
    <span class="hljs-string">"dev"</span>: <span class="hljs-string">"webpack serve"</span>, <span class="hljs-comment">// 开发环境中，运行 dev 命令</span>
    <span class="hljs-string">"build"</span>: <span class="hljs-string">"webpack --mode production"</span> <span class="hljs-comment">// 项目发布时，运行 build 命令</span>
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>--model 是一个参数项，用来指定 webpack 的运行模式。production 代表生产环境，会对打包生成的文件</p>
<p>进行代码压缩和性能优化。</p>
<blockquote>
<p>注意：通过 --model 指定的参数项，会覆盖 webpack.config.js 中的 model 选项。</p>
</blockquote>
<h2 data-id="heading-32">3. 把 JavaScript 文件统一生成到 js 目录中</h2>
<p>在 webpack.config.js 配置文件的 output 节点中，进行如下的配置：</p>
<pre><code class="hljs language-js copyable" lang="js">output: &#123;
    <span class="hljs-attr">path</span>: path.join(__dirname, <span class="hljs-string">'dist'</span>),
    <span class="hljs-attr">filename</span>: <span class="hljs-string">'js/bundle.js'</span>
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-33">4. 把图片文件统一生成到 image 目录中</h2>
<p>修改 webpack.config.js 中的 url-loader 配置项，新增 outputPath 选项即可指定图片文件的输出路径：</p>
<pre><code class="hljs language-js copyable" lang="js">&#123;
    <span class="hljs-attr">test</span>: <span class="hljs-regexp">/\.jpg|png|gif$/</span>,
    use: &#123;
        <span class="hljs-attr">loader</span>: <span class="hljs-string">'url-loader'</span>,
            <span class="hljs-attr">options</span>: &#123;
                <span class="hljs-attr">limit</span>: <span class="hljs-number">22228</span>,
                    <span class="hljs-attr">outputPath</span>: <span class="hljs-string">'image'</span>
            &#125;
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-34">5. 自动清理 dist 目录下的旧文件</h2>
<p>为了在每次打包发布时自动清理掉 dist 目录中的旧文件，可以安装并配置 clean-webpack-plugin 插件：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// 1. 安装清理 dist 目录的 webpack 插件</span>
npm install clean-webpack=plugin@<span class="hljs-number">3.0</span><span class="hljs-number">.0</span> -D

<span class="hljs-comment">// 2. 按需导入插件、得到插件的构造函数之后， 创建插件的实例对象</span>
<span class="hljs-keyword">const</span> &#123; CleanWebpackPlugin &#125; = <span class="hljs-built_in">require</span>(<span class="hljs-string">'clean-webpack=plugin'</span>)
<span class="hljs-keyword">const</span> cleanPlugin = <span class="hljs-keyword">new</span> CleanWebpackPlugin()

<span class="hljs-comment">// 3. 把创建 cleanPlugin 插件的实例对象，挂载到 plugins 节点中</span>
<span class="hljs-attr">plugins</span>: [htmlPlugin, cleanPlugin]
<span class="copy-code-btn">复制代码</span></code></pre>
<h1 data-id="heading-35">Source Map</h1>
<h2 data-id="heading-36">1. 生产环境遇到的问题</h2>
<p>前端项目在投入生产环境之前，都需要对 JavaScript 源代码进行压缩混淆，从而减小文件的体积，提高文件的</p>
<p>加载效率。此时就不可避免的产生了另一个问题：</p>
<p>对压缩混淆之后的代码除错（debug）是一件极其困难的事情</p>
<blockquote>
<p>变量被替换成没有任何语义的名称</p>
<p>空行和注释被剔除</p>
</blockquote>
<h2 data-id="heading-37">2. 什么是 Source Map</h2>
<p>Source Map 就是一个信息文件，里面储存着位置信息。也就是说，Source Map 文件中存储着压缩混淆后的</p>
<p>代码，所对应的转换前的位置。</p>
<p>有了它，出错的时候，除错工具将直接显示原始代码，而不是转换后的代码，能够极大的方便后期的调试</p>
<h2 data-id="heading-38">3. <strong>webpack</strong> <strong>开发环境下的</strong> <strong>Source Map</strong></h2>
<p>在开发环境下，webpack 默认启用了 Source Map 功能。当程序运行出错时，可以直接在控制台提示错误行</p>
<p>的位置，并定位到具体的源代码</p>
<h3 data-id="heading-39">3.1 默认 Source Map 的问题</h3>
<p>开发环境下默认生成的 Source Map，记录的是生成后的代码的位置。会导致运行时报错的行数与源代码的行</p>
<p>数不一致的问题。</p>
<h3 data-id="heading-40">3.2 解决默认 Source Map 的问题</h3>
<p>开发环境下，推荐在 webpack.config.js 中添加如下的配置，即可保证运行时报错的行数与源代码的行数</p>
<p>保持一致：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-built_in">module</span>.exports = &#123;
    <span class="hljs-attr">mode</span>: <span class="hljs-string">'development'</span>,
    <span class="hljs-attr">devtool</span>: <span class="hljs-string">'eval-source-map'</span>
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-41">4. <strong>webpack</strong> <strong>生产环境下的</strong> <strong>Source Map</strong></h2>
<p>在生产环境下，如果省略了 devtool 选项，则最终生成的文件中不包含 Source Map。这能够防止原始代码通</p>
<p>过 Source Map 的形式暴露给别有所图之人</p>
<h3 data-id="heading-42">4.1 只定位行数不暴露源码</h3>
<p>在生产环境下，如果只想定位报错的具体行数，且不想暴露源码。此时可以将 devtool 的值设置为</p>
<p>nosources-source-map</p>
<h3 data-id="heading-43">4.2 定位行数且暴露源码</h3>
<p>在生产环境下，如果想在定位报错行数的同时，展示具体报错的源码。此时可以将 devtool 的值设置为</p>
<p>source-map</p>
<h2 data-id="heading-44">5. Source Map 的最佳实践</h2>
<h4 data-id="heading-45">1. 开发环境下：</h4>
<pre><code class="copyable">建议把 devtool 的值设置为 eval-source-map

好处：可以精准定位到具体的错误行
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-46">2. 生产环境下：</h4>
<pre><code class="copyable">建议关闭 Source Map 或将 devtool 的值设置为 nosources-source-map

好处：防止源码泄露，提高网站的安全性
<span class="copy-code-btn">复制代码</span></code></pre></div>  
</div>
            