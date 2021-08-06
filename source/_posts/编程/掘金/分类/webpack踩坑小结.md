
---
title: 'webpack踩坑小结'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/064ef2fb06c748f7ad98f873a1ee9caf~tplv-k3u1fbpfcp-zoom-in-crop-mark:1956:0:0:0.image'
author: 掘金
comments: false
date: Thu, 05 Aug 2021 05:54:47 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/064ef2fb06c748f7ad98f873a1ee9caf~tplv-k3u1fbpfcp-zoom-in-crop-mark:1956:0:0:0.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p><strong>这是我参与8月更文挑战的第6天，活动详情查看：<a href="https://juejin.cn/post/6987962113788493831" title="https://juejin.cn/post/6987962113788493831" target="_blank">8月更文挑战</a></strong></p>
<p>目录：</p>
<p>1、webpack概念</p>
<p>2、入口</p>
<ul>
<li>默认值、 对象、 字符串、数组、常见场景(实例演示)</li>
</ul>
<p>3、输出</p>
<ul>
<li>基本用法、 高级进阶（实例演示）</li>
</ul>
<p>4、模式</p>
<ul>
<li>模式概念、配置方式（实例演示）</li>
</ul>
<p>5、loader</p>
<ul>
<li>loader概念、 3种配置方式、loader特点、解析loader（实例演示）</li>
</ul>
<p>6、plugin</p>
<ul>
<li>概念、剖析、用法、（实例演示）</li>
</ul>
<h2 data-id="heading-0">webpack</h2>
<p>本质上，webpack是一个现代 JavaScript 应用程序的静态模块打包器(module bundler)。
当 webpack 处理应用程序时，它会递归地构建一个依赖关系图(dependency graph)，其中包含应用程序需要的每个模块，然后将所有这些模块打包成一个或多个 bundle。</p>
<h2 data-id="heading-1">webpack有哪些概念</h2>
<p>在配置使用webpack之前我们需要先理解四个核心概念</p>
<ul>
<li>入口(entry)</li>
<li>输出(output)</li>
<li>loader</li>
<li>插件(plugins)</li>
</ul>
<p>接下来会给出这些概念的高度概述，同时提供具体概念的详尽相关用例</p>
<h2 data-id="heading-2">入口</h2>
<p>入口起点(entry point)指示 webpack 应该使用哪个模块，来作为构建其内部依赖图的开始。进入入口起点后，webpack 会找出有哪些模块和库是入口起点（直接和间接）依赖的。</p>
<p>每个依赖项随即被处理，最后输出到称之为 bundles 的文件中，我们将在下一章节详细讨论这个过程。</p>
<p>可以通过在 webpack 配置中配置 entry 属性，来指定一个入口起点（或多个入口起点）。默认值为 ./src。</p>
<p>接下来我们看一个 entry 配置的最简单例子：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/064ef2fb06c748f7ad98f873a1ee9caf~tplv-k3u1fbpfcp-zoom-in-crop-mark:1956:0:0:0.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p><em><strong>根据应用程序的特定需求，可以以多种方式配置 entry 属性。从入口起点章节可以了解更多信息。</strong></em></p>
<h2 data-id="heading-3">出口</h2>
<p>output 属性告诉 webpack 在哪里输出它所创建的 bundles，以及如何命名这些文件，默认值为 ./dist。</p>
<p>基本上，整个应用程序结构，都会被编译到你指定的输出路径的文件夹中。</p>
<p>你可以通过在配置中指定一个 output 字段，来配置这些处理过程：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/3c13fc7220d14ba189256824c00aedf2~tplv-k3u1fbpfcp-zoom-in-crop-mark:1956:0:0:0.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>在上面的示例中，我们通过 output.filename 和 output.path 属性，来告诉 webpack bundle 的名称，以及我们想要 bundle 生成(emit)到哪里。</p>
<p>可能你想要了解在代码最上面导入的 path 模块是什么，它是一个 Node.js 核心模块，用于操作文件路径。</p>
<p><em><strong>你可能会发现术语生成(emitted 或 emit)贯穿了我们整个文档和插件 API。它是“生产(produced)”或“释放(discharged)”的特殊术语。</strong></em></p>
<p><em><strong>output 属性还有更多可配置的特性，如果你想要了解更多关于 output 属性的概念，你可以通过阅读概念章节来了解更多。</strong></em></p>
<h2 data-id="heading-4">loader</h2>
<p>loader 让 webpack 能够去处理那些非 JavaScript 文件（webpack 自身只理解 JavaScript）。loader 可以将所有类型的文件转换为 webpack 能够处理的有效模块，然后你就可以利用 webpack 的打包能力，对它们进行处理。</p>
<p>本质上，webpack loader 将所有类型的文件，转换为应用程序的依赖图（和最终的 bundle）可以直接引用的模块。</p>
<p><em><strong>注意，loader 能够 import 导入任何类型的模块（例如 .css 文件），这是 webpack 特有的功能，其他打包程序或任务执行器的可能并不支持。我们认为这种语言扩展是有很必要的，因为这可以使开发人员创建出更准确的依赖关系图。</strong></em></p>
<p>在更高层面，在 webpack 的配置中 loader 有两个目标：</p>
<p>1.test 属性，用于标识出应该被对应的 loader 进行转换的某个或某些文件。</p>
<p>2.use 属性，表示进行转换时，应该使用哪个 loader。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/1d546e2c2ccc49919d711463c60b4500~tplv-k3u1fbpfcp-zoom-in-crop-mark:1956:0:0:0.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>以上配置中，对一个单独的 module 对象定义了 rules 属性，里面包含两个必须属性：test 和 use。这告诉 webpack 编译器(compiler) 如下信息：</p>
<p>“嘿，webpack 编译器，当你碰到「在 require()/import 语句中被解析为 '.txt' 的路径」时，在你对它打包之前，先使用 raw-loader 转换一下。”</p>
<p><em><strong>重要的是要记得，在 webpack 配置中定义 loader 时，要定义在 module.rules 中，而不是 rules。然而，在定义错误时 webpack 会给出严重的警告。为了使你受益于此，如果没有按照正确方式去做，webpack 会“给出严重的警告”</strong></em></p>
<h2 data-id="heading-5">模式</h2>
<p>通过选择 development 或 production 之中的一个，来设置 mode 参数，你可以启用相应模式下的 webpack 内置的优化</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/ff557d46b8cc446fb688d5f8aa523052~tplv-k3u1fbpfcp-zoom-in-crop-mark:1956:0:0:0.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-6">插件</h2>
<p>loader 被用于转换某些类型的模块，而插件则可以用于执行范围更广的任务。插件的范围包括，从打包优化和压缩，一直到重新定义环境中的变量。插件接口功能极其强大，可以用来处理各种各样的任务。</p>
<p>想要使用一个插件，你只需要 require() 它，然后把它添加到 plugins 数组中。多数插件可以通过选项(option)自定义。你也可以在一个配置文件中因为不同目的而多次使用同一个插件，这时需要通过使用 new 操作符来创建它的一个实例。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/e1133bca75ee48b8aa787b980462b315~tplv-k3u1fbpfcp-zoom-in-crop-mark:1956:0:0:0.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p><em><strong>webpack 提供许多开箱可用的插件！查阅我们的插件列表获取更多信息。</strong></em></p>
<p><em><strong>在 webpack 配置中使用插件是简单直接的，然而也有很多值得我们进一步探讨的用例。</strong></em></p>
<h2 data-id="heading-7">入口 （依赖图的开始）</h2>
<p>正如我们在起步中提到的，在 webpack 配置中有多种方式定义 entry 属性。除了解释为什么它可能非常有用，我们还将向你展示如何去配置 entry 属性。</p>
<p>entry接受三种形式的值：对象，字符串，数组</p>
<h3 data-id="heading-8">默认值的形式</h3>
<p>在webpack中不配置entry选项</p>
<pre><code class="copyable">module.exports = &#123;
output: &#123;
filename: 'entry.js',

path: path.resolve(__dirname, 'dist')
&#125;,
module: &#123;
rules: [&#123;
test: /\.css$/,
use: [
'style-loader',
'css-loader'
]
&#125;]
&#125;,
plugins: [
new CleanWebpackPlugin(['dist']),
new HtmlWebpackPlugin(&#123;
title: 'Output Management'
&#125;)
]
&#125;;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>以上配置打包后的目录是这样的（dist是打包后的目录，src是打包前资源目录）</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/b900eb38bb1b4768a2e507f3d9bbcd1e~tplv-k3u1fbpfcp-zoom-in-crop-mark:1956:0:0:0.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>默认去找src目录下的index.js去打包</p>
<h3 data-id="heading-9">entry入口的对象形式</h3>
<p>对象语法会比较繁琐。但是这也是应用程序中定义入口的<strong>最可扩展</strong>的方式。</p>
<p>“可扩展的 webpack 配置”是指，可重用并且可以与其他配置组合使用。这是一种流行的技术，用于将关注点(concern)从环境(environment)、构建目标(build target)、运行时(runtime)中分离。然后使用专门的工具（如 webpack-merge）将它们合并。</p>
<p><strong>key</strong></p>
<p>对象形式中对于key可以是简单的字符串，比如：'app', 'vebdors', 'entry-1'等。</p>
<pre><code class="copyable">entry: &#123;
'entryTest': './src/entry-1.js'
&#125;,
output: &#123;
filename: '[name].js',
path: path.resolve(__dirname, 'dist')
&#125;,
<span class="copy-code-btn">复制代码</span></code></pre>
<p>上面的配置打包后生成</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/a784536102294d38aa8e1b41ca1e64c8~tplv-k3u1fbpfcp-zoom-in-crop-mark:1956:0:0:0.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p><strong>value</strong></p>
<p>value可以是字符串，这个字符串可以是文件路径，也可以是一个npm模块</p>
<pre><code class="copyable">entry: &#123;
'my-lodash': 'lodash'
&#125;,
output: &#123;
filename: '[name].js',
path: path.resolve(__dirname, 'dist')
&#125;,
<span class="copy-code-btn">复制代码</span></code></pre>
<p>上面的配置打包之后会生成</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/149e8586b5314850ac7c66994218d849~tplv-k3u1fbpfcp-zoom-in-crop-mark:1956:0:0:0.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>value也可以是数组，数组中元素需要是合理字符串值。</p>
<pre><code class="copyable">entry: &#123;
    main: ['./src/index.js', 'lodash']
&#125;,
output: &#123;
filename: '[name].js',
path: path.resolve(__dirname, 'dist')
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>上面的配置打包生成</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/8b3e19639f4f4625a91445fadd91172e~tplv-k3u1fbpfcp-zoom-in-crop-mark:1956:0:0:0.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-10">字符串形式entry</h3>
<pre><code class="copyable">const config = &#123;
  entry: './path/to/my/entry/file.js'
&#125;;

module.exports = config;

<span class="copy-code-btn">复制代码</span></code></pre>
<p>字符串形式等于是下面这种形式的简写</p>
<pre><code class="copyable">const config = &#123;
  entry: &#123;
    main: './path/to/my/entry/file.js'
  &#125;
&#125;;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-11">数组形式entry</h3>
<pre><code class="copyable">const config = &#123;
entry: ['./app.js', 'lodash']
&#125;;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>等价于下面的对象形式</p>
<pre><code class="copyable">const config = &#123;
entry: &#123;
main: ['./app.js', 'lodash']
&#125;
&#125;;
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="copyable">entry: ['./src/print.js', './src/index.js'],
output: &#123;
filename: '[name].js',
path: path.resolve(__dirname, 'dist')
&#125;,
<span class="copy-code-btn">复制代码</span></code></pre>
<p>上面的配置打包后生成</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/930443491ad346b5b42290dc3787cb0e~tplv-k3u1fbpfcp-zoom-in-crop-mark:1956:0:0:0.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>"当你向 entry 传入一个数组时会发生什么？向 entry 属性传入「文件路径(file path)数组」将创建“多个主入口(multi-main entry)”。在你想要多个依赖文件一起注入，并且将它们的依赖导向(graph)到一个“chunk”时，传入数组的方式就很有用。"</p>
<h3 data-id="heading-12">常见场景</h3>
<p><strong>1.分离 应用程序(app) 和 第三方库(vendor) 入口</strong></p>
<pre><code class="copyable">const config = &#123;
  entry: &#123;
    app: './src/app.js',
    vendors: './src/vendors.js'
  &#125;
&#125;;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这是什么？从表面上看，这告诉我们 webpack 从 app.js 和 vendors.js 开始创建依赖图(dependency graph)。这些依赖图是彼此完全分离、互相独立的（每个 bundle 中都有一个 webpack 引导(bootstrap)）。这种方式比较常见于，只有一个入口起点（不包括 vendor）的单页应用程序(single page application)中。</p>
<p>为什么？此设置允许你使用 CommonsChunkPlugin 从「应用程序 bundle」中提取 vendor 引用(vendor reference) 到 vendor bundle，并把引用 vendor 的部分替换为 <em><strong>webpack_require</strong></em>() 调用。如果应用程序 bundle 中没有 vendor 代码，那么你可以在 webpack 中实现被称为长效缓存的通用模式。</p>
<p><strong>2.多页面应用程序</strong></p>
<pre><code class="copyable">const config = &#123;
  entry: &#123;
    pageOne: './src/pageOne/index.js',
    pageTwo: './src/pageTwo/index.js',
    pageThree: './src/pageThree/index.js'
  &#125;
&#125;;

<span class="copy-code-btn">复制代码</span></code></pre>
<p>这是什么？我们告诉 webpack 需要 3 个独立分离的依赖图（如上面的示例）。</p>
<p>为什么？在多页应用中，服务器将为你获取一个新的 HTML 文档。页面重新加载新文档，并且资源被重新下载。然而，这给了我们特殊的机会去做很多事：</p>
<ul>
<li>使用 CommonsChunkPlugin 为每个页面间的应用程序共享代码创建 bundle。由于入口起点增多，多页应用能够复用入口起点之间的大量代码/模块，从而可以极大地从这些技术中受益。</li>
</ul>
<p><em><strong>根据经验：每个 HTML 文档只使用一个入口起点。</strong></em></p>
<h2 data-id="heading-13">输出（output）</h2>
<p>配置 output 选项可以控制 webpack 如何向硬盘写入编译文件。注意，即使可以存在多个入口起点，但只指定一个输出配置</p>
<p>在 webpack 中配置 output 属性的最低要求是，将它的值设置为一个对象，包括以下两点：</p>
<ul>
<li>filename 用于输出文件的文件名。</li>
<li>目标输出目录 path 的绝对路径。</li>
</ul>
<p><strong>用法</strong></p>
<pre><code class="copyable">const config = &#123;
  output: &#123;
    filename: 'bundle.js',
    path: '/home/proj/public/assets'
  &#125;
&#125;;

module.exports = config;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>此配置将一个单独的 bundle.js 文件输出到 /home/proj/public/assets 目录中。</p>
<p><strong>多个入口起点</strong></p>
<p>如果配置创建了多个单独的 "chunk"（例如，使用多个入口起点或使用像 CommonsChunkPlugin 这样的插件），则应该使用占位符(substitutions)来确保每个文件具有唯一的名称</p>
<pre><code class="copyable">&#123;
  entry: &#123;
    app: './src/app.js',
    search: './src/search.js'
  &#125;,
  output: &#123;
    filename: '[name].js',
    path: __dirname + '/dist'
  &#125;
&#125;
// 写入到硬盘：./dist/app.js, ./dist/search.js
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>高级进阶</strong></p>
<p>以下是使用 CDN 和资源 hash 的复杂示例：</p>
<pre><code class="copyable">output: &#123;
  path: "/home/proj/cdn/assets/[hash]",
  publicPath: "http://cdn.example.com/assets/[hash]/"
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="copyable">entry: &#123;
index: './src/index.js',
print: './src/print.js'
&#125;,
output: &#123;
filename: '[name].js',
path: path.resolve(__dirname, 'dist/[hash]'),
publicPath: "http://cdn.example.com/assets/[hash]"
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>以上配置输出目录为</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/5c0221026a364fcf9e7311bba1a8f7ec~tplv-k3u1fbpfcp-zoom-in-crop-mark:1956:0:0:0.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>在html中引用的文件路径变为</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/14e7d5c2d2a04614bc1a911e0bfad7d0~tplv-k3u1fbpfcp-zoom-in-crop-mark:1956:0:0:0.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>publicPath指定的是构建后在html里的路径，一般也是用这个来指定上线后的cdn域名
在编译时不知道最终输出文件的 publicPath 的情况下，publicPath 可以留空，并且在入口起点文件运行时动态设置。可以在入口起点设置</p>
<pre><code class="copyable">__webpack_public_path__ = myRuntimePublicPath
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-14">模式[mode]</h2>
<p>提供 mode 配置选项，告知 webpack 使用相应模式的内置优化。他的值是string类型。分别为'none', 'development', 'production'(默认).</p>
<p><strong>development</strong></p>
<p>会将 process.env.NODE_ENV 的值设为 development。启用 NamedChunksPlugin 和 NamedModulesPlugin。</p>
<p><strong>production</strong></p>
<p>会将 process.env.NODE_ENV 的值设为 production。启用 FlagDependencyUsagePlugin, FlagIncludedChunksPlugin, ModuleConcatenationPlugin, NoEmitOnErrorsPlugin, OccurrenceOrderPlugin, SideEffectsFlagPlugin 和 UglifyJsPlugin.</p>
<p><strong>none</strong></p>
<p>Opts out of any default optimization options</p>
<p>如果未设置，webpack将production设置为mode的默认值</p>
<p>###两种配置形式</p>
<p>1.在配置文件中</p>
<pre><code class="copyable">module.exports = &#123;
  mode: 'production'
&#125;;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>2.从 CLI 参数中传递</p>
<pre><code class="copyable">webpack --mode=production
<span class="copy-code-btn">复制代码</span></code></pre>
<p>如果要根据webpack.config.js中的mode变量更改行为，则必须导出函数而不是对象</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/d7ce6861e2a74b5e86821827cbf3bb06~tplv-k3u1fbpfcp-zoom-in-crop-mark:1956:0:0:0.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p><em><strong>记住，只设置 NODE_ENV，则不会自动设置 mode。</strong></em></p>
<p>打包信息如下</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/a6388dcd02ef419c822b5050c6756db2~tplv-k3u1fbpfcp-zoom-in-crop-mark:1956:0:0:0.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-15">loader</h2>
<p>loader 用于对模块的源代码进行转换。loader 可以使你在 import 或"加载"模块时预处理文件。因此，loader 类似于其他构建工具中“任务(task)”，并提供了处理前端构建步骤的强大方法。</p>
<ul>
<li>loader 可以将文件从不同的语言（如 TypeScript）转换为 JavaScript。</li>
<li>将内联图像转换为 data URL。</li>
<li>允许你直接在 JavaScript 模块中 import CSS文件</li>
</ul>
<p>你可以使用 loader 告诉 webpack 加载 CSS 文件，或者将 TypeScript 转为 JavaScript。为此，首先安装相对应的 loader</p>
<pre><code class="copyable">npm install --save-dev css-loader
npm install --save-dev ts-loader
<span class="copy-code-btn">复制代码</span></code></pre>
<p>然后指示 webpack 对每个 .css 使用 css-loader，以及对所有 .ts 文件使用 ts-loader</p>
<pre><code class="copyable">module.exports = &#123;
  module: &#123;
    rules: [
      &#123; test: /\.css$/, use: 'css-loader' &#125;,
      &#123; test: /\.ts$/, use: 'ts-loader' &#125;
    ]
  &#125;
&#125;;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>使用loader</strong></p>
<ul>
<li>配置（推荐）：在 webpack.config.js 文件中指定 loader。</li>
<li>内联：在每个 import 语句中显式指定 loader。</li>
<li>CLI：在 shell 命令中指定它们。</li>
</ul>
<p>1、配置（推荐）：在 webpack.config.js 文件中指定 loader。</p>
<p>module.rules 允许你在 webpack 配置中指定多个 loader。 这是展示 loader 的一种简明方式，并且有助于使代码变得简洁。同时让你对各个 loader 有个全局概览：</p>
<pre><code class="copyable">module: &#123;
rules: [
  &#123;
    test: /\.css$/,
    use: [
      &#123; loader: 'style-loader' &#125;,
      &#123;
        loader: 'css-loader',
        options: &#123;
          modules: true
        &#125;
      &#125;
    ]
  &#125;
]
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>经过以上配置我们在js里引入的css就如下图所示添加到html文件中。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/298eee3e41aa4adfbd74d8f2f4192948~tplv-k3u1fbpfcp-zoom-in-crop-mark:1956:0:0:0.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>2、内联：在每个 import 语句中显式指定 loader。</p>
<pre><code class="copyable">import Styles from 'style-loader!css-loader?modules!./styles.css';
<span class="copy-code-btn">复制代码</span></code></pre>
<p>可以在 import 语句或任何等效于 "import" 的方式中指定 loader。使用 ! 将资源中的 loader 分开。分开的每个部分都相对于当前目录解析。</p>
<p>选项可以传递查询参数，例如 ?key=value&foo=bar，或者一个 JSON 对象，例如 ?&#123;"key":"value","foo":"bar"&#125;。</p>
<p>eg:在config.js去除关于css-loader和style-loader的配置,然后在引入css的文件中配置如下：</p>
<pre><code class="copyable">import _ from 'lodash';
// import './style.css';
import 'style-loader!css-loader?modules!./loader-inline.css';
<span class="copy-code-btn">复制代码</span></code></pre>
<p>生成的效果</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/cddb73230e9842da90afa14b8b1426b6~tplv-k3u1fbpfcp-zoom-in-crop-mark:1956:0:0:0.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>尽可能使用 module.rules，因为这样可以减少源码中的代码量，并且可以在出错时，更快地调试和定位 loader 中的问题。</p>
<p>3、CLI：在 shell 命令中指定它们。</p>
<pre><code class="copyable">webpack --module-bind jade-loader --module-bind 'css=style-loader!css-loader'
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这会对 .jade 文件使用 jade-loader，对 .css 文件使用 style-loader 和 css-loader。</p>
<p><strong>loader 特性</strong></p>
<ul>
<li>loader 支持链式传递。能够对资源使用流水线(pipeline)。一组链式的 loader 将按照相反的顺序执行。loader 链中的第一个 loader 返回值给下一个 loader。在最后一个 loader，返回 webpack 所预期的 JavaScript。</li>
<li>loader 可以是同步的，也可以是异步的。</li>
<li>loader 运行在 Node.js 中，并且能够执行任何可能的操作。</li>
<li>loader 接收查询参数。用于对 loader 传递配置。</li>
<li>loader 也能够使用 options 对象进行配置。</li>
<li>除了使用 package.json 常见的 main 属性，还可以将普通的 npm 模块导出为 loader，做法是在 package.json 里定义一个 loader 字段。</li>
<li>插件(plugin)可以为 loader 带来更多特性。</li>
<li>loader 能够产生额外的任意文件。</li>
</ul>
<p>loader 通过（loader）预处理函数，为 JavaScript 生态系统提供了更多能力。 用户现在可以更加灵活地引入细粒度逻辑，例如压缩、打包、语言翻译和其他更多。</p>
<p><strong>解析 loader</strong></p>
<p>loader 遵循标准的模块解析。多数情况下，loader 将从模块路径（通常将模块路径认为是 npm install, node_modules）解析。</p>
<p>loader 模块需要导出为一个函数，并且使用 Node.js 兼容的 JavaScript 编写。通常使用 npm 进行管理，但是也可以将自定义 loader 作为应用程序中的文件。按照约定，loader 通常被命名为 xxx-loader（例如 json-loader）。有关详细信息，请查看如何编写 loader？。</p>
<h2 data-id="heading-16">plugin</h2>
<p>插件是 webpack 的支柱功能。webpack 自身也是构建于，你在 webpack 配置中用到的相同的插件系统之上！</p>
<p>插件目的在于解决 loader 无法实现的其他事。</p>
<p><strong>剖析</strong></p>
<p>webpack 插件是一个具有 apply 属性的 JavaScript 对象。apply 属性会被 webpack compiler 调用，并且 compiler 对象可在整个编译生命周期访问。</p>
<p>ConsoleLogOnBuildWebpackPlugin.js</p>
<pre><code class="copyable">const pluginName = 'ConsoleLogOnBuildWebpackPlugin';

class ConsoleLogOnBuildWebpackPlugin &#123;
    apply(compiler) &#123;
        compiler.hooks.run.tap(pluginName, compilation => &#123;
            console.log("webpack 构建过程开始！");
        &#125;);
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>compiler hook 的 tap 方法的第一个参数，应该是驼峰式命名的插件名称。建议为此使用一个常量，以便它可以在所有 hook 中复用。</p>
<p><strong>用法</strong></p>
<p>由于插件可以携带参数/选项，你必须在 webpack 配置中，向 plugins 属性传入 new 实例。</p>
<p>webpack.config.js</p>
<pre><code class="copyable">const HtmlWebpackPlugin = require('html-webpack-plugin'); //通过 npm 安装
const webpack = require('webpack'); //访问内置的插件
const path = require('path');

const config = &#123;
  entry: './path/to/my/entry/file.js',
  output: &#123;
    filename: 'my-first-webpack.bundle.js',
    path: path.resolve(__dirname, 'dist')
  &#125;,
  module: &#123;
    rules: [
      &#123;
        test: /\.(js|jsx)$/,
        use: 'babel-loader'
      &#125;
    ]
  &#125;,
  plugins: [
    new webpack.optimize.UglifyJsPlugin(),
    new HtmlWebpackPlugin(&#123;template: './src/index.html'&#125;)
  ]
&#125;;

module.exports = config;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>Node API</strong></p>
<p><em><strong>即便使用 Node API，用户也应该在配置中传入 plugins 属性。compiler.apply 并不是推荐的使用方式。</strong></em></p>
<p>some-node-script.js</p>
<pre><code class="copyable">  const webpack = require('webpack'); //访问 webpack 运行时(runtime)
  const configuration = require('./webpack.config.js');

  let compiler = webpack(configuration);
  compiler.apply(new webpack.ProgressPlugin());

  compiler.run(function(err, stats) &#123;
    // ...
  &#125;);
<span class="copy-code-btn">复制代码</span></code></pre>
<p><em><strong>你知道吗：以上看到的示例和 webpack 自身运行时(runtime) 极其类似。wepback 源码中隐藏有大量使用示例，你可以用在自己的配置和脚本中。</strong></em></p></div>  
</div>
            