
---
title: '深入理解Webpack'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=7379'
author: 掘金
comments: false
date: Fri, 09 Apr 2021 23:13:34 GMT
thumbnail: 'https://picsum.photos/400/300?random=7379'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>Webpack 最初的目标是实现前端项目的模块化,解决的问题是如何在前端项目中更高效地管理和维护项目中的每一个资源</p>
<h3 data-id="heading-0">模块化的标准规范</h3>
<ul>
<li>在 Node.js 环境中，我们遵循 CommonJS 规范来组织模块。</li>
<li>在浏览器环境中，我们遵循 ES Modules 规范。</li>
</ul>
<blockquote>
<p>CommonJS 约定的是以同步的方式加载模块，因为 Node.js 执行机制是在启动时加载模块，执行过程中只是使用模块，所以这种方式不会有问题。但是如果要在浏览器端使用同步的加载模式，就会引起大量的同步模式请求，导致应用运行效率低下。</p>
</blockquote>
<blockquote>
<p>Webpack 以模块化思想为核心，帮助开发者更好的管理整个前端工程。</p>
</blockquote>
<blockquote>
<p>webpack 是 Webpack 的核心模块，webpack-cli 是 Webpack 的 CLI 程序，用来在命令行中调用 Webpack。</p>
</blockquote>
<blockquote>
<p>webpack.config.js 是一个运行在 Node.js 环境中的 JS 文件，需要按照 CommonJS 的方式编写代码</p>
</blockquote>
<h3 data-id="heading-1">配置文件支持智能提示</h3>
<p>VSCode 对于代码的自动提示是根据成员的类型推断出来的</p>
<p>默认 VSCode 不知道 Webpack 配置对象的类型，通过 import 的方式导入 Webpack 模块中的 Configuration 类型，根据类型注释的方式将变量标注为这个类型，这样在编写这个对象的内部结构时就有智能提示了，代码如下所示：</p>
<pre><code class="copyable">/** @type &#123;import('webpack').Configuration&#125; */
const config = &#123;
 entry: './src/index.js',
 output: &#123;
   filename: 'bundle.js'
 &#125;
&#125;
module.exports = config
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-2">Webpack 工作模式</h3>
<ul>
<li>
<p>production 模式下，启动内置优化插件，自动优化打包结果，打包速度偏慢；</p>
</li>
<li>
<p>development 模式下，自动优化打包速度，添加一些调试过程中的辅助插件；</p>
</li>
<li>
<p>none 模式下，运行最原始的打包，不做任何额外处理。</p>
<p>修改 Webpack 工作模式的方式有两种：</p>
<ul>
<li>
<p>通过 CLI --mode 参数传入；</p>
</li>
<li>
<p>通过配置文件设置 mode 属性。</p>
</li>
</ul>
</li>
</ul>
<h3 data-id="heading-3">Loader</h3>
<blockquote>
<p>Webpack 是用 Loader（加载器）来处理每个模块的，而内部默认的 Loader 只能处理 JS 模块，如果需要加载其他类型的模块就需要配置不同的 Loader</p>
</blockquote>
<pre><code class="copyable">// ./webpack.config.js
module.exports = &#123;
 entry: './src/main.css',
 output: &#123;
   filename: 'bundle.js'
 &#125;,
 module: &#123;
   rules: [
     &#123;
       test: /\.css$/, // 根据打包过程中所遇到文件路径匹配是否使用这个 loader
       use: 'css-loader' // 指定具体的 loader
     &#125;
   ]
 &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<blockquote>
<p>流程： css->css-loader->webpack->bundle.js</p>
</blockquote>
<blockquote>
<p>css-loader 只会把 CSS 模块加载到 JS 代码中，而并不会使用这个模块。所以这里我们还需要在 css-loader 的基础上再使用一个 style-loader，把 css-loader 转换后的结果通过 style 标签追加到页面上。</p>
</blockquote>
<pre><code class="copyable">// ./webpack.config.js
module.exports = &#123;
 entry: './src/main.css',
 output: &#123;
   filename: 'bundle.js'
 &#125;,
 module: &#123;
   rules: [
     &#123;
       test: /\.css$/,
       // 对同一个模块使用多个 loader，注意顺序
       use: [
         'style-loader',
         'css-loader'
       ]
     &#125;
   ]
 &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<blockquote>
<p>注意的是，一旦配置多个 Loader，执行顺序是从后往前执行的，所以这里一定要将 css-loader 放在最后，因为必须要 css-loader 先把 CSS 代码转换为 JS 模块，才可以正常打包</p>
</blockquote>
<blockquote>
<p>style-loader 的作用总结一句话就是，将 css-loader 中所加载到的所有样式模块，通过创建 style 标签的方式添加到页面上。</p>
</blockquote>
<h4 data-id="heading-4">经常用到的loader</h4>
<pre><code class="copyable">名称链接
file-loaderhttps://webpack.js.org/loaders/file-loader
url-loaderhttps://webpack.js.org/loaders/url-loader
babel-loaderhttps://webpack.js.org/loaders/babel-loader
style-loaderhttps://webpack.js.org/loaders/style-loader
css-loaderhttps://webpack.js.org/loaders/css-loader
sass-loaderhttps://webpack.js.org/loaders/sass-loader
postcss-loaderhttps://webpack.js.org/loaders/postcss-loader
eslint-loaderhttps://github.com/webpack-contrib/eslint-loader
vue-loaderhttps://github.com/vuejs/vue-loader
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-5">开发一个 Loader</h3>
<blockquote>
<p>每个 Webpack 的 Loader 都需要导出一个函数，这个函数就是我们这个 Loader 对资源的处理过程，它的输入就是加载到的资源文件内容，输出就是我们加工后的结果。我们通过 source 参数接收输入，通过返回值输出</p>
</blockquote>
<pre><code class="copyable">// ./markdown-loader.js
module.exports = source => &#123;
 // 加载到的模块内容 => '# About\n\nthis is a markdown file.'
 console.log(source)
 // 返回值就是最终被打包的内容
 return 'hello loader ~'
&#125;

// ./webpack.config.js
module.exports = &#123;
 entry: './src/main.js',
 output: &#123;
   filename: 'bundle.js'
 &#125;,
 module: &#123;
   rules: [
     &#123;
       test: /\.md$/,
       // 直接使用相对路径
       use: './markdown-loader'
     &#125;
   ]
 &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<blockquote>
<p>这里的 use 中不仅可以使用模块名称，还可以使用模块文件路径，这点与 Node 中的 require 函数是一样的。</p>
</blockquote>
<blockquote>
<p>Webpack 加载资源文件的过程类似于一个工作管道，你可以在这个过程中依次使用多个 Loader，但是最终这个管道结束过后的结果必须是一段标准的 JS 代码字符串。</p>
</blockquote>
<blockquote>
<p>Any Source -> Loader1->Loader2->Loader3->JavaScript Code</p>
</blockquote>
<ul>
<li>
<p>直接在这个 Loader 的最后返回一段 JS 代码字符串；</p>
</li>
<li>
<p>再找一个合适的加载器，在后面接着处理我们这里得到的结果。</p>
</li>
</ul>
<h3 data-id="heading-6">插件 plugin</h3>
<blockquote>
<p>Loader 是负责完成项目中各种各样资源模块的加载，从而实现整体项目的模块化，而 Plugin 则是用来解决项目中除了资源模块打包以外的其他自动化工作，所以说 Plugin 的能力范围更广，用途自然也就更多</p>
</blockquote>
<p>我在这里先介绍几个插件最常见的应用场景：</p>
<ul>
<li>
<p>实现自动在打包之前清除 dist 目录（上次的打包结果）；</p>
</li>
<li>
<p>自动生成应用所需要的 HTML 文件；(clean-webpack-plugin)</p>
</li>
<li>
<p>根据不同环境为代码注入类似 API 地址这种可能变化的部分；(html-webpack-plugin)</p>
</li>
<li>
<p>拷贝不需要参与打包的资源文件到输出目录；(copy-webpack-plugin)</p>
</li>
<li>
<p>压缩 Webpack 打包完成后输出的文件；</p>
</li>
<li>
<p>自动发布打包结果到服务器实现自动部署。</p>
</li>
</ul>
<h3 data-id="heading-7">开发一个插件</h3>
<blockquote>
<p>Webpack 的插件机制就是我们在软件开发中最常见的钩子机制</p>
</blockquote>
<blockquote>
<p>Webpack 要求我们的插件必须是一个函数或者是一个包含 apply 方法的对象，一般我们都会定义一个类型，在这个类型中定义 apply 方法。然后在使用时，再通过这个类型来创建一个实例对象去使用这个插件。然后在这个类型中定义一个 apply 方法，这个方法会在 Webpack 启动时被调用，它接收一个 compiler 对象参数，这个对象是 Webpack 工作过程中最核心的对象，里面包含了我们此次构建的所有配置信息，我们就是通过这个对象去注册钩子函数</p>
</blockquote>
<pre><code class="copyable">// ./remove-comments-plugin.js
class RemoveCommentsPlugin &#123;
  apply (compiler) &#123;
    compiler.hooks.emit.tap('RemoveCommentsPlugin', compilation => &#123;
      // compilation => 可以理解为此次打包的上下文
      for (const name in compilation.assets) &#123;
        console.log(name) // 输出文件名称
      &#125;
    &#125;)
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>那根据 API 文档中的介绍，我们找到一个叫作 emit 的钩子，这个钩子会在 Webpack 即将向输出目录输出文件时执行。</p>
<p>我们回到代码中，通过 compiler 对象的 hooks 属性访问到 emit 钩子，再通过 tap 方法注册一个钩子函数，这个方法接收两个参数：</p>
<ul>
<li>
<p>第一个是插件的名称，我们这里的插件名称是 RemoveCommentsPlugin；</p>
</li>
<li>
<p>第二个是要挂载到这个钩子上的函数；</p>
</li>
</ul>
<p>根据 API 文档中的提示，这里我们在这个函数中接收一个 compilation 对象参数，这个对象可以理解为此次运行打包的上下文，所有打包过程中产生的结果，都会放到这个对象中。</p>
<h3 data-id="heading-8">Webpack 核心工作过程中的关键环节</h3>
<ul>
<li>1.Webpack CLI 启动打包流程；</li>
<li>2.载入 Webpack 核心模块，创建 Compiler 对象；</li>
<li>3.使用 Compiler 对象开始编译整个项目；</li>
<li>4.从入口文件开始，解析模块依赖，形成依赖关系树；</li>
<li>5.递归依赖树，将每个模块交给对应的 Loader 处理；</li>
<li>6.合并 Loader 处理完的结果，将打包结果输出到 dist 目录</li>
</ul>
<h4 data-id="heading-9">1.Webpack CLI</h4>
<p>Webpack CLI将CLI参数和Webpack配置文件中的配置整合，得到一个完整的配置对象。</p>
<p>具体流程：</p>
<blockquote>
<p>Webpack CLI 会通过 yargs 模块解析 CLI 参数;紧接着后面，调用了 bin/utils/convert-argv.js 模块，将得到的命令行参数转换为 Webpack 的配置选项对象;在 convert-argv.js 工作过程中，首先为传递过来的命令行参数设置了默认值，然后判断了命令行参数中是否指定了一个具体的配置文件路径，如果指定了就加载指定配置文件，反之则需要根据默认配置文件加载规则找到配置文件;找到配置文件过后，将配置文件中的配置和 CLI 参数中的配置合并，如果出现重复的情况，会优先使用 CLI 参数，最终得到一个完整的配置选项。有了配置选项过后，开始载入 Webpack 核心模块，传入配置选项，创建 Compiler 对象，这个 Compiler 对象就是整个 Webpack 工作过程中最核心的对象了，负责完成整个项目的构建工作。</p>
</blockquote>
<h4 data-id="heading-10">2.创建 Compiler 对象</h4>
<p>随着 Webpack CLI 载入 Webpack 核心模块，整个执行过程就到了 Webpack 模块中;导出的是一个用于创建 Compiler 的函数</p>
<blockquote>
<p>在这个函数中，首先校验了外部传递过来的 options 参数是否符合要求，紧接着判断了 options 的类型。根据这个函数中的代码，我们发现 options 不仅仅可以是一个对象，还可以是一个数组。如果我们传入的是一个数组，那么 Webpack 内部创建的就是一个 MultiCompiler，也就是说 Webpack 应该支持同时开启多路打包，配置数组中的每一个成员就是一个独立的配置选项。而如果我们传入的是普通的对象，就会按照我们最熟悉的方式创建一个 Compiler 对象，进行单线打包。在创建了 Compiler 对象过后，Webpack 就开始注册我们配置中的每一个插件了，因为再往后 Webpack 工作过程的生命周期就要开始了，所以必须先注册，这样才能确保插件中的每一个钩子都能被命中。</p>
</blockquote>
<h4 data-id="heading-11">3、开始构建</h4>
<blockquote>
<p>完成 Compiler 对象的创建过后，紧接着这里的代码开始判断配置选项中是否启用了监视模式;</p>
</blockquote>
<ul>
<li>如果是监视模式就调用 Compiler 对象的 watch 方法，以监视模式启动构建。</li>
<li>如果不是监视模式就调用 Compiler 对象的 run 方法，开始构建整个应用。</li>
</ul>
<blockquote>
<p>这个 run 方法定义在 Compiler 类型中，具体文件在 webpack 模块下的 lib/Compiler.js 中;这个方法内部就是先触发了beforeRun 和 run 两个钩子，然后最关键的是调用了当前对象的 compile 方法，真正开始编译整个项目;</p>
</blockquote>
<p>compile 方法内部主要就是创建了一个 Compilation 对象，Compilation 字面意思是“合集”，实际上，你就可以理解为一次构建过程中的上下文对象，里面包含了这次构建中全部的资源和信息。创建完 Compilation 对象过后，紧接着触发了一个叫作 make 的钩子，进入整个构建过程最核心的 make 阶段。</p>
<h4 data-id="heading-12">4、make 阶段</h4>
<blockquote>
<p>make 阶段主体的目标就是：根据 entry 配置找到入口模块，开始依次递归出所有依赖，形成依赖关系树，然后将递归到的每个模块交给不同的 Loader 处理。由于这个阶段的调用过程并不像之前一样，直接调用某个对象的某个方法，而是采用事件触发机制，让外部监听这个 make 事件的地方开始执行;找到六个插件中都注册了 make 事件，这些插件实际上是前面创建 Compiler 对象的时候创建的；因为我们默认使用的就是单一入口打包的方式，所以这里最终会执行其中的 SingleEntryPlugin；这个插件中调用了 Compilation 对象的 addEntry 方法，开始解析我们源代码中的入口文件，以此开始“顺藤摸瓜”式的寻找。</p>
</blockquote>
<p>对于 make 阶段后续的流程，这里我们概括一下：</p>
<ul>
<li>1.SingleEntryPlugin 中调用了 Compilation 对象的 addEntry 方法，开始解析入口；</li>
<li>2.addEntry 方法中又调用了 _addModuleChain 方法，将入口模块添加到模块依赖列表中；</li>
<li>3.紧接着通过 Compilation 对象的 buildModule 方法进行模块构建；</li>
<li>4.buildModule 方法中执行具体的 Loader，处理特殊资源加载；</li>
<li>5.build 完成过后，通过 acorn 库生成模块代码的 AST 语法树；</li>
<li>6.根据语法树分析这个模块是否还有依赖的模块，如果有则继续循环 build 每个依赖；</li>
<li>7.所有依赖解析完成，build 阶段结束；</li>
<li>8.最后合并生成需要输出的 bundle.js 写入 dist 目录。</li>
</ul>
<blockquote>
<p>注意： Webpack 的插件系统是基于官方自己的 Tapable 库实现的</p>
</blockquote>
<h3 data-id="heading-13">使用 Dev Server 提高本地开发效率</h3>
<p>webpack-dev-server</p>
<p>流程：</p>
<ul>
<li>1.开始</li>
<li>2.启动HTTP服务</li>
<li>3.Webpack构建</li>
<li>4.监视文件变化</li>
<li>回到第3步</li>
</ul>
<blockquote>
<p>webpack-dev-server 为了提高工作速率，它并没有将打包结果写入到磁盘中，而是暂时存放在内存中，内部的 HTTP Server 也是从内存中读取这些文件的。这样一来，就会减少很多不必要的磁盘读写操作，大大提高了整体的构建效率。</p>
</blockquote>
<h4 data-id="heading-14">静态资源访问</h4>
<p>如果有一些没有参与打包的静态文件也需要作为开发服务器的资源被访问,配置如下：</p>
<p>通过这个 devServer 对象的 contentBase 属性指定额外的静态资源路径。这个 contentBase 属性可以是一个字符串或者数组，也就是说你可以配置一个或者多个路径</p>
<pre><code class="copyable">// ./webpack.config.js
module.exports = &#123;
  // ...
  devServer: &#123;
    contentBase: 'public'
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-15">Proxy 代理</h4>
<pre><code class="copyable">// ./webpack.config.js
module.exports = &#123;
  // ...
  devServer: &#123;
    proxy: &#123;
      '/api': &#123;
        target: 'https://api.github.com',
        pathRewrite: &#123;
          '^/api': '' // 替换掉代理地址中的 /api
        &#125;,
        changeOrigin: true // 确保请求 GitHub 的主机名就是：api.github.com
      &#125;
    &#125;
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-16">配置 Webpack SourceMap</h3>
<p>Source Map（源代码地图）从它的名字就能够看出它的作用：映射转换后的代码与源代码之间的关系。一段转换后的代码，通过转换过程中生成的 Source Map 文件就可以逆向解析得到对应的源代码。</p>
<pre><code class="copyable">// ./webpack.config.js
module.exports = &#123;
  devtool: 'source-map' // source map 设置
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<blockquote>
<p>Source Map 并不是 Webpack 特有的功能，它们两者的关系只是：Webpack 支持 Source Map。大多数的构建或者编译工具也都支持 Source Map。</p>
</blockquote>
<h3 data-id="heading-17">热替换（HMR）机制</h3>
<p>Webpack 中的模块热替换，指的是我们可以在应用运行过程中，实时的去替换掉应用中的某个模块，而应用的运行状态不会因此而改变。例如，我们在应用运行过程中修改了某个模块，通过自动刷新会导致整个应用的整体刷新，那页面中的状态信息都会丢失；而如果使用的是 HMR，就可以实现只将修改的模块实时替换至应用中，不必完全刷新整个应用。</p>
<h4 data-id="heading-18">开启 HMR</h4>
<p>HMR 已经集成在了 webpack 模块中了，所以不需要再单独安装什么模块。</p>
<p>使用这个特性最简单的方式就是，在运行 webpack-dev-server 命令时，通过 --hot 参数去开启这个特性。</p>
<p>或者也可以在配置文件中通过添加对应的配置来开启这个功能。那我们这里打开配置文件，这里需要配置两个地方：</p>
<ul>
<li>首先需要将 devServer 对象中的 hot 属性设置为 true；</li>
<li>然后需要载入一个插件，这个插件是 webpack 内置的一个插件，所以我们先导入 webpack 模块，有了这个模块过后，这里使用的是一个叫作 HotModuleReplacementPlugin 的插件。</li>
</ul>
<pre><code class="copyable">// ./webpack.config.js
const webpack = require('webpack')

module.exports = &#123;
  // ...
  devServer: &#123;
    // 开启 HMR 特性，如果资源不支持 HMR 会 fallback 到 live reloading
    hot: true
    // 只使用 HMR，不会 fallback 到 live reloading
    // hotOnly: true
  &#125;,
  plugins: [
    // ...
    // HMR 特性所需要的插件
    new webpack.HotModuleReplacementPlugin()
  ]
&#125;

<span class="copy-code-btn">复制代码</span></code></pre>
<p>我们回到开发工具中，这里我们先来尝试修改一下 CSS 文件。样式文件修改保存过后，确实能够以不刷新的形式更新到页面中。</p>
<p>然后我们再来尝试一下修改 JS 文件。保存过后你会发现，这里的页面依然自动刷新了，好像并没有之前所说 HMR 的体验。</p>
<p>很明显：HMR 并不像 Webpack 的其他特性一样可以开箱即用，需要有一些额外的操作。</p>
<p>具体来说，Webpack 中的 HMR 需要我们手动通过代码去处理，当模块更新过后该，如何把更新后的模块替换到页面中。</p>
<blockquote>
<p>因为样式文件是经过 Loader 处理的，在 style-loader 中就已经自动处理了样式文件的热更新，所以就不需要我们额外手动去处理了。样式模块更新过后，只需要把更新后的 CSS 及时替换到页面中，它就可以覆盖掉之前的样式，从而实现更新。而我们所编写的 JavaScript 模块是没有任何规律的，你可能导出的是一个对象，也可能导出的是一个字符串，还可能导出的是一个函数，使用时也各不相同。所以 Webpack 面对这些毫无规律的 JS 模块，根本不知道该怎么处理更新后的模块，也就无法直接实现一个可以通用所有情况的模块替换方案。</p>
</blockquote>
<blockquote>
<p>使用框架开发时，我们项目中的每个文件就有了规律，例如 React 中要求每个模块导出的必须是一个函数或者类，那这样就可以有通用的替换办法，所以这些工具内部都已经帮你实现了通用的替换操作，自然就不需要手动处理了</p>
</blockquote>
<h4 data-id="heading-19">HMR APIs</h4>
<p>HotModuleReplacementPlugin 为我们的 JavaScript 提供了一套用于处理 HMR 的 API，我们需要在我们自己的代码中，使用这套 API 将更新后的模块替换到正在运行的页面中。</p>
<p>对于开启 HMR 特性的环境中，我们可以访问到全局的 module 对象中的 hot 成员，这个成员是一个对象，这个对象就是 HMR API 的核心对象，它提供了一个 accept 方法，用于注册当某个模块更新后的处理函数。accept 方法第一个参数接收的就是所监视的依赖模块路径，第二个参数就是依赖模块更新后的处理函数。</p>
<pre><code class="copyable">// ./main.js

// ... 原本的业务代码

module.hot.accept('./editor', () => &#123;
  // 当 ./editor.js 更新，自动执行此函数
  console.log('editor 更新了～～')
&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="copyable">// HMR -----------------------------------
if (module.hot) &#123; // 确保有 HMR API 对象
  module.hot.accept('./editor', () => &#123;
    // ...
  &#125;)
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<blockquote>
<p>除此之外，可能你还有一个问题：我们在代码中写了很多与业务功能本身无关的代码，会不会对生产环境有影响？---- 你会发现之前我们编写的处理热替换的代码都被移除掉了，只剩下一个 if (false) 的空判断，这种没有意义的判断，在压缩过后也会自动去掉，所以根本不会对生产环境有任何影响。</p>
</blockquote>
<h3 data-id="heading-20">Webpack 高级特性应对项目优化需求</h3>
<h4 data-id="heading-21">Tree Shaking 和 sideEffects</h4>
<h5 data-id="heading-22">Tree Shaking</h5>
<p>Tree Shaking 翻译过来的意思就是“摇树”。伴随着摇树的动作，树上的枯树枝和树叶就会掉落下来。</p>
<p>我们这里要介绍的 Tree-shaking 也是同样的道理，不过通过 Tree-shaking “摇掉”的是代码中那些没有用到的部分，这部分没有用的代码更专业的说法应该叫作未引用代码（dead-code）。</p>
<p>使用 Webpack 生产模式打包的优化过程中，就使用自动开启这个功能，以此来检测我们代码中的未引用代码，然后自动移除它们。</p>
<blockquote>
<p>Tree-shaking 并不是指 Webpack 中的某一个配置选项，而是一组功能搭配使用过后实现的效果，这组功能在生产模式下都会自动启用，所以使用生产模式打包就会有 Tree-shaking 的效果</p>
</blockquote>
<h4 data-id="heading-23">开启 Tree Shaking</h4>
<p>不再使用 production 模式，而是使用 none，也就是不开启任何内置功能和插件</p>
<p>在配置对象中添加一个 optimization 属性，这个属性用来集中配置 Webpack 内置优化功能，它的值也是一个对象</p>
<pre><code class="copyable">// ./webpack.config.js
module.exports = &#123;
  // ... 其他配置项
  optimization: &#123;
    // 模块只导出被使用的成员
    usedExports: true,
    // 压缩输出结果
    minimize: true
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这就是 Tree-shaking 的实现，整个过程用到了 Webpack 的两个优化功能：</p>
<ul>
<li>usedExports - 打包结果中只导出外部用到的成员；</li>
<li>minimize - 压缩打包结果。</li>
</ul>
<p>如果把我们的代码看成一棵大树，那你可以这样理解：</p>
<ul>
<li>usedExports 的作用就是标记树上哪些是枯树枝、枯树叶；</li>
<li>minimize 的作用就是负责把枯树枝、枯树叶摇下来。</li>
</ul>
<h4 data-id="heading-24">合并模块（扩展）</h4>
<p>除了 usedExports 选项之外，我们还可以使用一个 concatenateModules 选项继续优化输出。</p>
<p>普通打包只是将一个模块最终放入一个单独的函数中，如果我们的模块很多，就意味着在输出结果中会有很多的模块函数。</p>
<p>concatenateModules 配置的作用就是尽可能将所有模块合并到一起输出到一个函数中，这样既提升了运行效率，又减少了代码的体积。</p>
<p>在 optimization 属性中开启 concatenateModules</p>
<pre><code class="copyable">// ./webpack.config.js
module.exports = &#123;
  // ... 其他配置项
  optimization: &#123;
    // 模块只导出被使用的成员
    usedExports: true,
    // 尽可能合并每一个模块到一个函数中
    concatenateModules: true,
    // 压缩输出结果
    minimize: true
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这个特性又被称为 Scope Hoisting，也就是作用域提升，它是 Webpack 3.0 中添加的一个特性。</p>
<p>如果再配合 minimize 选项，打包结果的体积又会减小很多。</p>
<h4 data-id="heading-25">结合 babel-loader 的问题</h4>
<blockquote>
<p>Tree-shaking 实现的前提是 ES Modules，也就是说：最终交给 Webpack 打包的代码，必须是使用 ES Modules 的方式来组织的模块化。</p>
</blockquote>
<blockquote>
<p>最新版本的 babel-loader 并不会导致 Tree-shaking 失效。如果你不确定现在使用的 babel-loader 会不会导致这个问题，最简单的办法就是在配置中将 @babel/preset-env 的 modules 属性设置为 false，确保不会转换 ES Modules，也就确保了 Tree-shaking 的前提</p>
</blockquote>
<h4 data-id="heading-26">sideEffects</h4>
<p>Webpack 4 中新增了一个 sideEffects 特性，它允许我们通过配置标识我们的代码是否有副作用，从而提供更大的压缩空间。</p>
<blockquote>
<p>TIPS：模块的副作用指的就是模块执行的时候除了导出成员，是否还做了其他的事情。</p>
</blockquote>
<p>在 optimization 中开启 sideEffects 特性</p>
<pre><code class="copyable">// ./webpack.config.js
module.exports = &#123;
  mode: 'none',
  entry: './src/main.js',
  output: &#123;
    filename: 'bundle.js'
  &#125;,
  optimization: &#123;
    sideEffects: true
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<blockquote>
<p>TIPS：注意这个特性在 production 模式下同样会自动开启。</p>
</blockquote>
<p>那此时 Webpack 在打包某个模块之前，会先检查这个模块所属的 package.json 中的 sideEffects 标识，以此来判断这个模块是否有副作用，如果没有副作用的话，这些没用到的模块就不再被打包。换句话说，即便这些没有用到的模块中存在一些副作用代码，我们也可以通过 package.json 中的 sideEffects 去强制声明没有副作用。</p>
<p>那我们打开项目 package.json 添加一个 sideEffects 字段，把它设置为 false，</p>
<pre><code class="copyable">&#123;
  "name": "01-side-effects",
  "version": "0.1.0",
  "author": "",
  "license": "MIT",
  "scripts": &#123;
    "build": "webpack"
  &#125;,
  "devDependencies": &#123;
    "webpack": "^4.43.0",
    "webpack-cli": "^3.3.11"
  &#125;,
  "sideEffects": false
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这样就表示我们这个项目中的所有代码都没有副作用，让 Webpack 放心大胆地去“干”。</p>
<p>这里设置了两个地方：</p>
<ul>
<li>webpack.config.js 中的 sideEffects 用来开启这个功能；</li>
<li>package.json 中的 sideEffects 用来标识我们的代码没有副作用。</li>
</ul>
<p>目前很多第三方的库或者框架都已经使用了 sideEffects 标识，所以我们再也不用担心为了一个小功能引入一个很大体积的库了。例如，某个 UI 组件库中只有一两个组件会用到，那只要它支持 sideEffects，你就可以放心大胆的直接用了。</p>
<h4 data-id="heading-27">sideEffects 注意</h4>
<p>使用 sideEffects 这个功能的前提是确定你的代码没有副作用，或者副作用代码没有全局影响，否则打包时就会误删掉你那些有意义的副作用代码。</p>
<p>最好的办法就是在 package.json 中的 sideEffects 字段中标识需要保留副作用的模块路径（可以使用通配符</p>
<pre><code class="copyable">&#123;
  "name": "01-side-effects",
  "version": "0.1.0",
  "author": "",
  "license": "MIT",
  "scripts": &#123;
    "build": "webpack"
  &#125;,
  "devDependencies": &#123;
    "webpack": "^4.43.0",
    "webpack-cli": "^3.3.11"
  &#125;,
  "sideEffects": [
    "./src/extend.js",
    "*.css"
  ]
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这样 Webpack 的 sideEffects 就不会忽略确实有必要的副作用模块了。</p>
<h4 data-id="heading-28">Code Splitting（代码分割）</h4>
<p>Webpack 实现分包的方式主要有两种：</p>
<ul>
<li>根据业务不同配置多个打包入口，输出多个打包结果；</li>
<li>结合 ES Modules 的动态导入（Dynamic Imports）特性，按需加载模块。</li>
</ul>
<p>多入口打包</p>
<pre><code class="copyable">// ./webpack.config.js
const HtmlWebpackPlugin = require('html-webpack-plugin')
module.exports = &#123;
  entry: &#123;
    index: './src/index.js',
    album: './src/album.js'
  &#125;,
  output: &#123;
    filename: '[name].bundle.js' // [name] 是入口名称
  &#125;,
  // ... 其他配置
  plugins: [
    new HtmlWebpackPlugin(&#123;
      title: 'Multi Entry',
      template: './src/index.html',
      filename: 'index.html',
      chunks: ['index'] // 指定使用 index.bundle.js
    &#125;),
    new HtmlWebpackPlugin(&#123;
      title: 'Multi Entry',
      template: './src/album.html',
      filename: 'album.html',
      chunks: ['album'] // 指定使用 album.bundle.js
    &#125;)
  ]
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>提取公共模块</p>
<pre><code class="copyable">// ./webpack.config.js
module.exports = &#123;
  entry: &#123;
    index: './src/index.js',
    album: './src/album.js'
  &#125;,
  output: &#123;
    filename: '[name].bundle.js' // [name] 是入口名称
  &#125;,
  optimization: &#123;
    splitChunks: &#123;
      // 自动提取所有公共模块到单独 bundle
      chunks: 'all'
    &#125;
  &#125;
  // ... 其他配置
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-29">动态导入</h4>
<p>除了多入口打包的方式，Code Splitting 更常见的实现方式还是结合 ES Modules 的动态导入特性，从而实现按需加载。</p>
<pre><code class="copyable">// ./src/index.js
// import posts from './posts/posts'
// import album from './album/album'
const update = () => &#123;
  const hash = window.location.hash || '#posts'
  const mainElement = document.querySelector('.main')
  mainElement.innerHTML = ''
  if (hash === '#posts') &#123;
    // mainElement.appendChild(posts())
    import('./posts/posts').then((&#123; default: posts &#125;) => &#123;
      mainElement.appendChild(posts())
    &#125;)
  &#125; else if (hash === '#album') &#123;
    // mainElement.appendChild(album())
    import('./album/album').then((&#123; default: album &#125;) => &#123;
      mainElement.appendChild(album())
    &#125;)
  &#125;
&#125;
window.addEventListener('hashchange', update)
update()
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-30">魔法注释</h4>
<p>默认通过动态导入产生的 bundle 文件，它的 name 就是一个序号，这并没有什么不好，因为大多数时候，在生产环境中我们根本不用关心资源文件的名称。</p>
<p>但是如果你还是需要给这些 bundle 命名的话，就可以使用 Webpack 所特有的魔法注释去实现</p>
<pre><code class="copyable">// 魔法注释
import(/* webpackChunkName: 'posts' */'./posts/posts')
  .then((&#123; default: posts &#125;) => &#123;
    mainElement.appendChild(posts())
  &#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>所谓魔法注释，就是在 import 函数的形式参数位置，添加一个行内注释，这个注释有一个特定的格式：webpackChunkName: ''，这样就可以给分包的 chunk 起名字了。</p>
<p>除此之外，魔法注释还有个特殊用途：如果你的 chunkName 相同的话，那相同的 chunkName 最终就会被打包到一起，例如我们这里可以把这两个 chunkName 都设置为 components，然后再次运行打包，那此时这两个模块都会被打包到一个文件中</p>
<h3 data-id="heading-31">优化 Webpack 的构建速度和打包结果</h3>
<h5 data-id="heading-32">生产模式下的优化插件</h5>
<p>1.Define Plugin</p>
<p>首先是 DefinePlugin，DefinePlugin 是用来为我们代码中注入全局成员的。在 production 模式下，默认通过这个插件往代码中注入了一个 process.env.NODE_ENV。很多第三方模块都是通过这个成员去判断运行环境，从而决定是否执行例如打印日志之类的操作。</p>
<pre><code class="copyable">// ./webpack.config.js
const webpack = require('webpack')
module.exports = &#123;
/  // ... 其他配置
  plugins: [
    new webpack.DefinePlugin(&#123;
      API_BASE_URL:  '"https://api.example.com"'
    &#125;)
  ]
&#125;

<span class="copy-code-btn">复制代码</span></code></pre>
<p>2.Mini CSS Extract Plugin</p>
<p>对于 CSS 文件的打包，一般我们会使用 style-loader 进行处理，这种处理方式最终的打包结果就是 CSS 代码会内嵌到 JS 代码中。</p>
<p>mini-css-extract-plugin 是一个可以将 CSS 代码从打包结果中提取出来的插件</p>
<pre><code class="copyable">// ./webpack.config.js
const MiniCssExtractPlugin = require('mini-css-extract-plugin')
module.exports = &#123;
  mode: 'none',
  entry: &#123;
    main: './src/index.js'
  &#125;,
  output: &#123;
    filename: '[name].bundle.js'
  &#125;,
  module: &#123;
    rules: [
      &#123;
        test: /\.css$/,
        use: [
          // 'style-loader', // 将样式通过 style 标签注入
          MiniCssExtractPlugin.loader,
          'css-loader'
        ]
      &#125;
    ]
  &#125;,
  plugins: [
    new MiniCssExtractPlugin()
  ]
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>我们这里先导入这个插件模块，导入过后我们就可以将这个插件添加到配置对象的 plugins 数组中了。这样 Mini CSS Extract Plugin 在工作时就会自动提取代码中的 CSS 了。</p>
<p>除此以外，Mini CSS Extract Plugin 还需要我们使用 MiniCssExtractPlugin 中提供的 loader 去替换掉 style-loader，以此来捕获到所有的样式。</p>
<p>这样的话，打包过后，样式就会存放在独立的文件中，直接通过 link 标签引入页面。</p>
<p>不过这里需要注意的是，如果你的 CSS 体积不是很大的话，提取到单个文件中，效果可能适得其反，因为单独的文件就需要单独请求一次。个人经验是如果 CSS 超过 200KB 才需要考虑是否提取出来，作为单独的文件。</p>
<h4 data-id="heading-33">Optimize CSS Assets Webpack Plugin</h4>
<p>Webpack 内置的压缩插件仅仅是针对 JS 文件的压缩，其他资源文件的压缩都需要额外的插件</p>
<p>Webpack 官方推荐了一个 Optimize CSS Assets Webpack Plugin 插件。我们可以使用这个插件来压缩我们的样式文件。</p>
<pre><code class="copyable">// ./webpack.config.js
const MiniCssExtractPlugin = require('mini-css-extract-plugin')
const OptimizeCssAssetsWebpackPlugin = require('optimize-css-assets-webpack-plugin')
const TerserWebpackPlugin = require('terser-webpack-plugin')
module.exports = &#123;
  mode: 'none',
  entry: &#123;
    main: './src/index.js'
  &#125;,
  output: &#123;
    filename: '[name].bundle.js'
  &#125;,
  optimization: &#123;
    minimizer: [
      new TerserWebpackPlugin(),
      new OptimizeCssAssetsWebpackPlugin()
    ]
  &#125;,
  module: &#123;
    rules: [
      &#123;
        test: /\.css$/,
        use: [
          MiniCssExtractPlugin.loader,
          'css-loader'
        ]
      &#125;
    ]
  &#125;,
  plugins: [
    new MiniCssExtractPlugin()
  ]
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<blockquote>
<p>因为我们设置了 minimizer，Webpack 认为我们需要使用自定义压缩器插件，那内部的 JS 压缩器就会被覆盖掉。我们必须手动再添加回来。内置的 JS 压缩插件叫作 terser-webpack-plugin</p>
</blockquote></div> <div class="image-viewer-box" data-v-78c9b824><!----></div>  
</div>
            