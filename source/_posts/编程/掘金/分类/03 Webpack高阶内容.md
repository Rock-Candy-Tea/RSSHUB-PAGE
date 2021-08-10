
---
title: '03. Webpack高阶内容'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/c77e04a2ce46489587130c752cbd92eb~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Mon, 09 Aug 2021 04:56:41 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/c77e04a2ce46489587130c752cbd92eb~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h2 data-id="heading-0">Dev Server</h2>
<h3 data-id="heading-1">较为理想的开发环境</h3>
<ol>
<li>首先，它必须能够使用 HTTP 服务运行而不是文件形式预览。这样的话，一来更接近生产环境状态，二来我们的项目可能需要使用 AJAX 之类的 API，以文件形式访问会产生诸多问题。</li>
<li>其次，在我们修改完代码过后，Webpack 能够自动完成构建，然后浏览器可以即时显示最新的运行结果，这样就大大减少了开发过程中额外的重复操作，同时也会让我们更加专注，效率自然得到提升。</li>
<li>最后，它还需要能提供 Source Map 支持。这样一来，运行过程中出现的错误就可以快速定位到源代码中的位置，而不是打包后结果中的位置，更便于我们快速定位错误、调试应用。</li>
</ol>
<p>“编写源代码 → Webpack 打包 → 运行应用 → 浏览器查看”这种周而复始的开发方式过于原始</p>
<h3 data-id="heading-2">Webpack自动编译</h3>
<p>Webpack CLI 提供 watch 工作模式</p>
<p>在这种模式下，Webpack 完成初次构建过后，项目中的源文件会被监视，一旦发生任何改动，Webpack 都会自动重新运行打包任务。
启动 Webpack 时，添加一个 --watch 的 CLI 参数，这样的话，Webpack 就会以监视模式启动运行。
在打包完成过后，CLI 不会立即退出，它会等待文件变化再次工作，直到我们手动结束它或是出现不可控的异常。</p>
<p>那此时我们的开发体验就是：修改代码 → Webpack 自动打包 → 手动刷新浏览器 → 预览运行结果。</p>
<p>P.S. 这里我使用的静态文件服务器是一个 npm 模块，叫作 <a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fvercel%2Fserve" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/vercel/serve" ref="nofollow noopener noreferrer">serve</a>。</p>
<p>编码变化后, 浏览器能够在Webpack打包后自动刷新</p>
<p>如果你已经了解过一个叫作 <a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.browsersync.io%2F" target="_blank" rel="nofollow noopener noreferrer" title="https://www.browsersync.io/" ref="nofollow noopener noreferrer">BrowserSync</a> 的工具，你应该知道 BrowserSync 就可以帮我们实现文件变化过后浏览器自动刷新的功能。</p>
<p>所以，我们就可以使用 BrowserSync 工具替换 serve 工具，启动 HTTP 服务，这里还需要同时监听 dist 目录下文件的变化，具体命令如下：</p>
<pre><code class="hljs language-bash copyable" lang="bash"><span class="hljs-comment"># 可以先通过 npm 全局安装 browser-sync 模块，然后再使用这个模块</span>
npm install browser-sync --global
browser-sync dist --watch

<span class="hljs-comment"># 或者也可以使用 npx 直接使用远端模块</span>
npx browser-sync dist --watch
<span class="copy-code-btn">复制代码</span></code></pre>
<p>BrowserSync它的原理就是 Webpack 监视源代码变化，自动打包源代码到 dist 中，而 dist 中文件的变化又被 BrowserSync 监听了，从而实现自动编译并且自动刷新浏览器的功能，整个过程由两个工具分别监视不同的内容。</p>
<p>这种 watch 模式 + BrowserSync 虽然也实现了我们的需求，但是这种方法有很多弊端：</p>
<ol>
<li>操作烦琐，我们需要同时使用两个工具，那么需要了解的内容就会更多，学习成本大大提高；</li>
<li>效率低下，因为整个过程中， Webpack 会将文件写入磁盘，BrowserSync 再进行读取。过程中涉及大量磁盘读写操作，必然会导致效率低下。</li>
</ol>
<h3 data-id="heading-3">Webpack Dev Server</h3>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fwebpack%2Fwebpack-dev-server" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/webpack/webpack-dev-server" ref="nofollow noopener noreferrer">webpack-dev-server</a> 是 Webpack 官方推出的一款开发工具，它提供了一个开发服务器，并且将自动编译和自动刷新浏览器等一系列对开发友好的功能全部集成在了一起。</p>
<p>webpack-dev-server 同样也是一个独立的 npm 模块，所以我们需要通过 npm 将 webpack-dev-server 作为项目的开发依赖安装。安装完成过后，这个模块为我们提供了一个叫作 webpack-dev-server 的 CLI 程序，我们同样可以直接通过 npx 直接去运行这个 CLI，或者把它定义到 npm scripts 中，具体操作如下：</p>
<pre><code class="hljs language-bash copyable" lang="bash"><span class="hljs-comment"># 安装 webpack-dev-server</span>
npm install webpack-dev-server --save-dev
<span class="hljs-comment"># 运行 webpack-dev-server</span>
npx webpack-dev-server
<span class="copy-code-btn">复制代码</span></code></pre>
<p>运行 webpack-dev-server 这个命令时，它内部会启动一个 HTTP Server，为打包的结果提供静态文件服务，并且自动使用 Webpack 打包我们的应用，然后监听源代码的变化，一旦文件发生变化，它会立即重新打包，大致流程如下：</p>
<h2 data-id="heading-4"><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/c77e04a2ce46489587130c752cbd92eb~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></h2>
<p>webpack-dev-server 为了提高工作速率，它并没有将打包结果写入到磁盘中，而是暂时存放在内存中，内部的 HTTP Server 也是从内存中读取这些文件的。这样一来，就会减少很多不必要的磁盘读写操作，大大提高了整体的构建效率。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/8ad86745c8404c578688aefdaec09513~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>我们还可以为 webpack-dev-server 命令传入一个 --open 的参数，用于自动唤起浏览器打开我们的应用。打开浏览器过后，此时如果你有两块屏幕，就可以把浏览器放到另外一块屏幕上，然后体验一边编码，一边即时预览的开发环境了。</p>
<h4 data-id="heading-5">Webpack Dev Server配置</h4>
<p>Webpack 配置对象中可以有一个叫作 devServer 的属性，专门用来为 webpack-dev-server 提供配置，具体如下：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">// ./webpack.config.js</span>
<span class="hljs-keyword">const</span> path = <span class="hljs-built_in">require</span>(<span class="hljs-string">'path'</span>)

<span class="hljs-built_in">module</span>.exports = &#123;
  <span class="hljs-comment">// ...</span>
  <span class="hljs-attr">devServer</span>: &#123;
    <span class="hljs-attr">contentBase</span>: path.join(__dirname, <span class="hljs-string">'dist'</span>),
    <span class="hljs-attr">compress</span>: <span class="hljs-literal">true</span>,
    <span class="hljs-attr">port</span>: <span class="hljs-number">9000</span>
    <span class="hljs-comment">// ...</span>
    <span class="hljs-comment">// 详细配置文档：https://webpack.js.org/configuration/dev-server/</span>
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-6">Webpack Dev Server静态资源访问</h4>
<p>webpack-dev-server 默认会将构建结果和输出文件全部作为开发服务器的资源文件，也就是说，只要通过 Webpack 打包能够输出的文件都可以直接被访问到。但是如果你还有一些没有参与打包的静态文件也需要作为开发服务器的资源被访问，那你就需要额外通过配置“告诉” webpack-dev-server。</p>
<p>具体的方法就是在 webpack-dev-server 的配置对象中添加一个对应的配置。
我们回到配置文件中，找到 devServer 属性，它的类型是一个对象，我们可以通过这个 devServer 对象的 contentBase 属性指定额外的静态资源路径。这个 contentBase 属性可以是一个字符串或者数组，也就是说你可以配置一个或者多个路径。具体配置如下：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">// ./webpack.config.js</span>
<span class="hljs-built_in">module</span>.exports = &#123;
  <span class="hljs-comment">// ...</span>
  <span class="hljs-attr">devServer</span>: &#123;
    <span class="hljs-attr">contentBase</span>: <span class="hljs-string">'public'</span>
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-7">Proxy代理</h4>
<p>webpack-dev-server 是一个本地开发服务器, 与后端服务通信会产生跨域</p>
<p>webpack-dev-server 支持直接通过配置的方式，添加代理服务。</p>
<p>那解决这种开发阶段跨域请求问题最好的办法，就是在开发服务器中配置一个后端 API 的代理服务，也就是把后端接口服务代理到本地的开发服务地址。</p>
<p>pathRewrite 属性来实现代理路径重写，重写规则就是把路径中开头的 /api 替换为空，pathRewrite 最终会以正则的方式来替换请求路径。</p>
<p>将代理规则配置的 changeOrigin 属性设置为 true，就会以实际代理请求地址中的主机名去请求，也就是我们正常请求这个地址的主机名是什么，实际请求时就会设置成什么。</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">// ./webpack.config.js</span>
<span class="hljs-built_in">module</span>.exports = &#123;
  <span class="hljs-comment">// ...</span>
  <span class="hljs-attr">devServer</span>: &#123;
    <span class="hljs-attr">proxy</span>: &#123;
      <span class="hljs-string">'/api'</span>: &#123;
        <span class="hljs-attr">target</span>: <span class="hljs-string">'https://api.github.com'</span>,
        <span class="hljs-attr">pathRewrite</span>: &#123;
          <span class="hljs-string">'^/api'</span>: <span class="hljs-string">''</span> <span class="hljs-comment">// 替换掉代理地址中的 /api</span>
        &#125;,
        <span class="hljs-attr">changeOrigin</span>: <span class="hljs-literal">true</span> <span class="hljs-comment">// 确保请求 GitHub 的主机名就是：api.github.com</span>
      &#125;
    &#125;
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>那此时我们请求 <a href="https://link.juejin.cn/?target=http%3A%2F%2Flocalhost%3A8080%2Fapi%2Fusers" target="_blank" rel="nofollow noopener noreferrer" title="http://localhost:8080/api/users" ref="nofollow noopener noreferrer">http://localhost:8080/api/users</a> ，就相当于请求了 <a href="https://link.juejin.cn/?target=https%3A%2F%2Fapi.github.com%2Fapi%2Fusers" target="_blank" rel="nofollow noopener noreferrer" title="https://api.github.com/api/users" ref="nofollow noopener noreferrer">api.github.com/users</a>。
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/4bff587b15554b1f8fefab27809c2f90~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-8">Source Map</h2>
<p>通过构建或者编译之类的操作，我们将开发阶段编写的源代码转换为能够在生产环境中运行的代码，这种进步同时也意味着我们实际运行的代码和我们真正编写的代码之间存在很大的差异。</p>
<p>在这种情况下，如果需要调试我们的应用，或是应用运行的过程中出现意料之外的错误，那我们将无从下手。
因为无论是调试还是报错，都是基于构建后的代码进行的，我们只能看到错误信息在构建后代码中具体的位置，却很难直接定位到源代码中对应的位置。</p>
<h3 data-id="heading-9">Source Map 简介</h3>
<p>Source Map（源代码地图）就是解决此类问题最好的办法，从它的名字就能够看出它的作用：映射转换后的代码与源代码之间的关系。一段转换后的代码，通过转换过程中生成的 Source Map 文件就可以逆向解析得到对应的源代码。
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/cc71ee41b65544c0860213fde2dcf5b4~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>目前很多第三方库在发布的文件中都会同时提供一个 .map 后缀的 Source Map 文件。例如 jQuery。我们可以打开它的 Source Map 文件看一下，如下图所示：
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/88eb72d0413446cdb4cebadd0454ddd1~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer">
这是一个 JSON 格式的文件。这个 JSON 里面记录的就是转换后和转换前代码之间的映射关系，主要存在以下几个属性：</p>
<ol>
<li>version 是指定所使用的 Source Map 标准版本；</li>
<li>sources 中记录的是转换前的源文件名称，因为有可能出现多个文件打包转换为一个文件的情况，所以这里是一个数组；</li>
<li>names 是源代码中使用的一些成员名称，我们都知道一般压缩代码时会将我们开发阶段编写的有意义的变量名替换为一些简短的字符，这个属性中记录的就是原始的名称；</li>
<li>mappings 属性，这个属性最为关键，它是一个叫作 base64-VLQ 编码的字符串，里面记录的信息就是转换后代码中的字符与转换前代码中的字符之间的映射关系，具体如下图所示：</li>
</ol>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/5af66902cc90453586305d82aac5d84d~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer">
一般我们会在转换后的代码中通过添加一行注释的方式来去引入 Source Map 文件。
不过这个特性只是用于开发调试的，所以最新版本的 jQuery 已经去除了引入 Source Map 的注释，我们需要手动添加回来，这里我们在最后一行添加 //# sourceMappingURL=jquery-3.4.1.min.map，具体效果如下：
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/78fa8e9756c54cf9ba37841712dda158~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>这样我们在 Chrome 浏览器中如果打开了开发人员工具，它就会自动请求这个文件，然后根据这个文件的内容逆向解析出来源代码，以便于调试。
同时因为有了映射关系，所以代码中如果出现了错误，也就能自动定位找到源代码中的位置了。</p>
<p>打开开发人员工具，找到 Source 面板，这里我们就能看到转换前的 jQuery 源代码了，具体效果如下图所示：
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/44065f725c834a6dbb9f28907db40bb8~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-10">Webpack中配置Source Map</h3>
<p>我们回到配置文件中，这里我们要使用的配置属性叫作 devtool。这个属性就是用来配置开发过程中的辅助工具，也就是与 Source Map 相关的一些功能。我们可以先将这个属性设置为 source-map，具体代码如下：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">// ./webpack.config.js</span>
<span class="hljs-built_in">module</span>.exports = &#123;
  <span class="hljs-attr">devtool</span>: <span class="hljs-string">'source-map'</span> <span class="hljs-comment">// source map 设置</span>
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>然后打开命令行终端，运行 Webpack 打包。打包完成过后，我们打开 dist 目录，此时这个目录中就会生成我们 bundle.js 的 Source Map 文件，与此同时 bundle.js 中也会通过注释引入这个 Source Map 文件，具体如下图所示：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/0598a55118824256b17bdd18a8ed6dce~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer">
Webpack 中的 devtool 配置，除了可以使用 source-map 这个值，它还支持很多其他的选项，具体的我们可以参考文档中的不同模式的对比表。
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/c6a8146a780b4463981ccad76ec8e542~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-11">Eval模式</h3>
<p>eval 其实指的是 JavaScript 中的一个函数，可以用来运行字符串中的 JavaScript 代码。例如下面这段代码，字符串中的 console.log("foo~") 就会作为一段 JavaScript 代码被执行：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">const</span> code = <span class="hljs-string">'console.log("foo~")'</span>
<span class="hljs-built_in">eval</span>(code) <span class="hljs-comment">// 将 code 中的字符串作为 JS 代码执行</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>在默认情况下，这段代码运行在一个临时的虚拟机环境中，我们在控制台中就能够看到：
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/c6db8a3412bd4a81a59825002c7914f4~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>在 eval 函数执行的字符串代码中添加一个注释，注释的格式：# sourceURL=./path/to/file.js，这样的话这段代码就会执行在指定路径下。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/af1e491888fa44dab4da51d8df352dee~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p> eval 函数可以通过 sourceURL 指定代码所属文件路径</p>
<p> Webpack 的配置文件中，将 devtool 属性设置为 eval，具体如下：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">// ./webpack.config.js</span>
<span class="hljs-built_in">module</span>.exports = &#123;
  <span class="hljs-attr">devtool</span>: <span class="hljs-string">'eval'</span>
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>成的 bundle.js 文件，你会发现每个模块中的代码都被包裹到了一个 eval 函数中，而且每段模块代码的最后都会通过 sourceURL 的方式声明这个模块对应的源文件路径，具体如下：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/253231c56b654ad2b250010028a999f6~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer">
那此时如果我们回到浏览器运行这里的 bundle.js，一旦出现错误，浏览器的控制台就可以定位到具体是哪个模块中的代码，具体效果如下：
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/03525066efd0455eb2bc3c198d6a4af9~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer">
但是当你点击控制台中的文件名打开这个文件后，看到的却是打包后的模块代码，而并非我们真正的源代码，具体如下：</p>
<h2 data-id="heading-12"><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/654c0a979e574b9bb320ade1409ac7c8~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></h2>
<p>综上所述，在 eval 模式下，Webpack 会将每个模块转换后的代码都放到 eval 函数中执行，并且通过 sourceURL 声明对应的文件路径，这样浏览器就能知道某一行代码到底是在源代码的哪个文件中。</p>
<p>因为在 eval 模式下并不会生成 Source Map 文件，所以它的构建速度最快，但是缺点同样明显：它只能定位源代码的文件路径，无法知道具体的行列信息。</p>
<h3 data-id="heading-13">eval-source-map</h3>
<p>eval-source-map 模式除了定位文件，还可以定位具体的行列信息。
相比于 eval 模式，它能够生成 Source Map 文件，可以反推出源代码</p>
<h3 data-id="heading-14">cheap-eval-source-map</h3>
<p>阉割版的 eval-source-map，因为它虽然也生成了 Source Map 文件，但是这种模式下的 Source Map 只能定位到行，而定位不到列，所以在效果上差了一点点，但是构建速度会提升很多</p>
<h3 data-id="heading-15">cheap-module-eval-source-map</h3>
<p>cheap-module-eval-source-map 中定位的源代码与我们编写的源代码是一模一样的，而 cheap-eval-source-map 模式中定位的源代码是经过 ES6 转换后的结果，具体对比如下（左图是 cheap-eval-source-map）：
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/0b89baa2577b4f6fa517d10e639a0159~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer">
因为这种名字中带有 module 的模式，解析出来的源代码是没有经过 Loader 加工的，而名字中不带 module 的模式，解析出来的源代码是经过 Loader 加工后的结果。也就是说如果我们想要还原一模一样的源代码，就需要选择 cheap-module-eval-source-map 模式。</p>
<h3 data-id="heading-16">cheap-source-map</h3>
<p>这个模式的名字中没有 eval，意味着它没用 eval 执行代码，而名字中没有 module，意味着 Source Map 反推出来的是 Loader 处理后的代码，有 cheap 表示只能定位源代码的行号。</p>
<h3 data-id="heading-17">inline-source-map</h3>
<p>它跟普通的 source-map 效果相同，只不过这种模式下 Source Map 文件不是以物理文件存在，而是以 data URLs 的方式出现在代码中。我们前面遇到的 eval-source-map 也是这种 inline 的方式。</p>
<h3 data-id="heading-18">hidden-source-map</h3>
<p>我们在开发工具中看不到 Source Map 的效果，但是它也确实生成了 Source Map 文件，这就跟 jQuery 一样，虽然生成了 Source Map 文件，但是代码中并没有引用对应的 Source Map 文件，开发者可以自己选择使用。</p>
<h3 data-id="heading-19">nosources-source-map</h3>
<p>在这个模式下，我们能看到错误出现的位置（包含行列位置），但是点进去却看不到源代码。这是为了保护源代码在生产环境中不暴露。</p>
<h3 data-id="heading-20">真实情况</h3>
<h4 data-id="heading-21">开发环境</h4>
<p>首先开发过程中（开发环境），会选择 cheap-module-eval-source-map，原因有以下三点：</p>
<ol>
<li>以 React 和 Vue.js 为例，无论是 JSX 还是 vue 单文件组件，Loader 转换后差别都很大，我需要调试 Loader 转换前的源代码。</li>
<li>一般情况下，编写的代码每行不会超过 80 个字符，对我而言能够定位到行到位置就够了，而且省略列信息还可以提升构建速度。</li>
<li>虽然在这种模式下启动打包会比较慢，但大多数时间内我使用的 webpack-dev-server 都是在监视模式下重新打包，它重新打包的速度非常快。</li>
</ol>
<h4 data-id="heading-22">生产环境</h4>
<p>至于发布前的打包，也就是生产环境的打包，选择 none，它不会生成 Source Map。原因很简单：</p>
<ol>
<li>首先，Source Map 会暴露我的源代码到生产环境。如果没有控制 Source Map 文件访问权限的话，但凡是有点技术的人都可以很容易的复原项目中涉及的绝大多数源代码，这非常不合理也不安全，我想很多人可能都忽略了这个问题。</li>
<li>其次，调试应该是开发阶段的事情，你应该在开发阶段就尽可能找到所有问题和隐患，而不是到了生产环境中再去全民公测。如果你对自己的代码实在没有信心，我建议你选择 nosources-source-map 模式，这样出现错误可以定位到源码位置，也不至于暴露源码</li>
</ol>
<h2 data-id="heading-23">HMR机制</h2>
<h3 data-id="heading-24">自动刷新的问题</h3>
<p>我们每次修改完代码，Webpack 都可以监视到变化，然后自动打包，再通知浏览器自动刷新，一旦页面整体刷新，那页面中的任何操作状态都将会丢失</p>
<h3 data-id="heading-25">模块热替换（HMR）</h3>
<p>HMR 全称 Hot Module Replacement，翻译过来叫作“模块热替换”或“模块热更新”。</p>
<p>Webpack 中的模块热替换，指的是我们可以在应用运行过程中，实时的去替换掉应用中的某个模块，而应用的运行状态不会因此而改变。</p>
<h3 data-id="heading-26">开启HMR</h3>
<p>使用这个特性最简单的方式就是，在运行 webpack-dev-server 命令时，通过 --hot 参数去开启这个特性。</p>
<p>或者也可以在配置文件中通过添加对应的配置来开启这个功能。那我们这里打开配置文件，这里需要配置两个地方：</p>
<ol>
<li>首先需要将 devServer 对象中的 hot 属性设置为 true；</li>
<li>然后需要载入一个插件，这个插件是 webpack 内置的一个插件，所以我们先导入 webpack 模块，有了这个模块过后，这里使用的是一个叫作 HotModuleReplacementPlugin 的插件。</li>
</ol>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">// ./webpack.config.js</span>
<span class="hljs-keyword">const</span> webpack = <span class="hljs-built_in">require</span>(<span class="hljs-string">'webpack'</span>)

<span class="hljs-built_in">module</span>.exports = &#123;
  <span class="hljs-comment">// ...</span>
  <span class="hljs-attr">devServer</span>: &#123;
    <span class="hljs-comment">// 开启 HMR 特性，如果资源不支持 HMR 会 fallback 到 live reloading</span>
    <span class="hljs-attr">hot</span>: <span class="hljs-literal">true</span>
    <span class="hljs-comment">// 只使用 HMR，不会 fallback 到 live reloading</span>
    <span class="hljs-comment">// hotOnly: true</span>
  &#125;,
  <span class="hljs-attr">plugins</span>: [
    <span class="hljs-comment">// ...</span>
    <span class="hljs-comment">// HMR 特性所需要的插件</span>
    <span class="hljs-keyword">new</span> webpack.HotModuleReplacementPlugin()
  ]
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-27">HMR 的疑问</h3>
<p>Webpack 中的 HMR 需要我们手动通过代码去处理，当模块更新过后该，如何把更新后的模块替换到页面中。</p>
<p>Q1：可能你会问，为什么我们开启 HMR 过后，样式文件的修改就可以直接热更新呢？我们好像也没有手动处理样式模块的更新啊？</p>
<p>A1：这是因为样式文件是经过 Loader 处理的，在 style-loader 中就已经自动处理了样式文件的热更新，所以就不需要我们额外手动去处理了。</p>
<p>Q2：那你可能会想，凭什么样式就可以自动处理，而我们的脚本就需要自己手动处理呢？</p>
<p>A2：这个原因也很简单，因为样式模块更新过后，只需要把更新后的 CSS 及时替换到页面中，它就可以覆盖掉之前的样式，从而实现更新。</p>
<p>而我们所编写的 JavaScript 模块是没有任何规律的，你可能导出的是一个对象，也可能导出的是一个字符串，还可能导出的是一个函数，使用时也各不相同。
所以 Webpack 面对这些毫无规律的 JS 模块，根本不知道该怎么处理更新后的模块，也就无法直接实现一个可以通用所有情况的模块替换方案。</p>
<p>那这就是为什么样式文件可以直接热更新，而 JS 文件更新后页面还是回退到自动刷新的原因。</p>
<p>Q3：那可能还有一些平时使用 vue-cli 或者 create-react-app 这种框架脚手架工具的人会说，“我的项目就没有手动处理，JavaScript 代码照样可以热替换，也没你说的那么麻烦”。</p>
<p>A3：这是因为你使用的是框架，使用框架开发时，我们项目中的每个文件就有了规律，例如 React 中要求每个模块导出的必须是一个函数或者类，那这样就可以有通用的替换办法，所以这些工具内部都已经帮你实现了通用的替换操作，自然就不需要手动处理了。</p>
<h3 data-id="heading-28">HRM APIs</h3>
<p>当 JavaScript 模块更新过后，该如何将更新后的模块替换到页面中。</p>
<p>HotModuleReplacementPlugin 为我们的 JavaScript 提供了一套用于处理 HMR 的 API，我们需要在我们自己的代码中，使用这套 API 将更新后的模块替换到正在运行的页面中。</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">// ./src/main.js</span>
<span class="hljs-keyword">import</span> createEditor <span class="hljs-keyword">from</span> <span class="hljs-string">'./editor'</span>
<span class="hljs-keyword">import</span> logo <span class="hljs-keyword">from</span> <span class="hljs-string">'./icon.png'</span>
<span class="hljs-keyword">import</span> <span class="hljs-string">'./global.css'</span>

<span class="hljs-keyword">const</span> img = <span class="hljs-keyword">new</span> Image()
img.src = logo
<span class="hljs-built_in">document</span>.body.appendChild(img)

<span class="hljs-keyword">const</span> editor = createEditor()
<span class="hljs-built_in">document</span>.body.appendChild(editor)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>Webpack 打包的入口文件，在这个文件中会加载一些其他模块。
正是因为在 main.js 中使用了这些模块，所以一旦这些模块更新了过后，我们在 main.js 中就必须重新使用更新后的模块。</p>
<p>我们需要在这个文件中添加一些额外的代码，去处理它所依赖的这些模块更新后的热替换逻辑。</p>
<p>对于开启 HMR 特性的环境中，我们可以访问到全局的 module 对象中的 hot 成员，这个成员是一个对象，这个对象就是 HMR API 的核心对象，它提供了一个 accept 方法，用于注册当某个模块更新后的处理函数。
accept 方法第一个参数接收的就是所监视的依赖模块路径，第二个参数就是依赖模块更新后的处理函数。</p>
<p>那我们这里先尝试注册 ./editor 模块更新过后的处理函数，第一个参数就是 editor 模块的路径，第二个参数则需要我们传入一个函数，然后在这个函数中打印一个消息，具体代码如下：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">// ./main.js</span>

<span class="hljs-comment">// ... 原本的业务代码</span>

<span class="hljs-built_in">module</span>.hot.accept(<span class="hljs-string">'./editor'</span>, <span class="hljs-function">() =></span> &#123;
  <span class="hljs-comment">// 当 ./editor.js 更新，自动执行此函数</span>
  <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'editor 更新了～～'</span>)
&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>如果我们修改了 editor 模块，保存过后，浏览器的控制台中就会自动打印我们上面在代码中添加的消息，而且浏览器也不会自动刷新了。</p>
<p>一旦这个模块的更新被我们手动处理了，就不会触发自动刷新；反之，如果没有手动处理，热替换会自动 fallback（回退）到自动刷新。</p>
<h3 data-id="heading-29">JS模块热替换</h3>
<p>这个模块导出的是一个 createEditor 函数，我们先正常把它打印到控制台，然后在模块更新后的处理函数中再打印一次，具体代码如下：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">// ./main.js</span>
<span class="hljs-keyword">import</span> createEditor <span class="hljs-keyword">from</span> <span class="hljs-string">'./editor'</span>

<span class="hljs-comment">// ... 原本的业务代码</span>

<span class="hljs-built_in">console</span>.log(createEditor)
<span class="hljs-built_in">module</span>.hot.accept(<span class="hljs-string">'./editor'</span>, <span class="hljs-function">() =></span> &#123;
  <span class="hljs-built_in">console</span>.log(createEditor)
&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>如果再次修改 editor 模块，保存过后，就会发现当模块更新后，这里拿到的 createEditor 函数也就更新为了最新的结果，具体结果如下图所示：
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/ca4c141369844a58b406b801f04187f2~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer">
模块文件更新后 createEditor 函数可以自动更新。
我们这里使用 createEditor 函数是用来创建一个界面元素的，那模块一旦更新了，这个元素也就需要重新创建，所以我们这里先移除原来的元素，然后再调用更新后的 createEditor 函数，创建一个新的元素追加到页面中，具体代码如下：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">// ./main.js</span>
<span class="hljs-keyword">import</span> createEditor <span class="hljs-keyword">from</span> <span class="hljs-string">'./editor'</span>

<span class="hljs-keyword">const</span> editor = createEditor()
<span class="hljs-built_in">document</span>.body.appendChild(editor)

<span class="hljs-comment">// ... 原本的业务代码</span>

<span class="hljs-comment">// HMR -----------------------------------</span>
<span class="hljs-built_in">module</span>.hot.accept(<span class="hljs-string">'./editor'</span>, <span class="hljs-function">() =></span> &#123;
  <span class="hljs-built_in">document</span>.body.removeChild(editor) <span class="hljs-comment">// 移除之前创建的元素</span>
  <span class="hljs-keyword">const</span> newEditor = createEditor() <span class="hljs-comment">// 用新模块创建新元素</span>
  <span class="hljs-built_in">document</span>.body.appendChild(newEditor)
&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>但如果只是这样实现的话，一次热替换结束后，第二次就没法再实现热替换了。因为第二次执行这个函数的时候，editor 变量指向的元素已经在上一次执行时被移除了，所以我们这里还应该记录下来每次热替换创建的新元素，以便于下一次热替换时的操作，具体代码如下：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">// ./main.js</span>
<span class="hljs-keyword">import</span> createEditor <span class="hljs-keyword">from</span> <span class="hljs-string">'./editor'</span>

<span class="hljs-keyword">const</span> editor = createEditor()
<span class="hljs-built_in">document</span>.body.appendChild(editor)

<span class="hljs-comment">// ... 原本的业务代码</span>

<span class="hljs-comment">// HMR -----------------------------------</span>
<span class="hljs-keyword">let</span> lastEditor = editor
<span class="hljs-built_in">module</span>.hot.accept(<span class="hljs-string">'./editor'</span>, <span class="hljs-function">() =></span> &#123;
  <span class="hljs-built_in">document</span>.body.removeChild(lastEditor) <span class="hljs-comment">// 移除之前创建的元素</span>
  lastEditor = createEditor() <span class="hljs-comment">// 用新模块创建新元素</span>
  <span class="hljs-built_in">document</span>.body.appendChild(lastEditor)
&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>此时就应该是正常的热替换效果了</p>
<h3 data-id="heading-30">热替换的状态保持</h3>
<p>热替换操作必须在替换时把状态保留下来。</p>
<p>在替换前先拿到编辑器中的内容，然后替换后在放回去就行了。那因为我这里使用的是可编辑元素，而不是文本框，所以我们需要通过 innerHTML 拿到之前编辑的内容，然后设置到更新后创建的新元素中，具体代码如下：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">// ./main.js</span>
<span class="hljs-keyword">import</span> createEditor <span class="hljs-keyword">from</span> <span class="hljs-string">'./editor'</span>

<span class="hljs-keyword">const</span> editor = createEditor()
<span class="hljs-built_in">document</span>.body.appendChild(editor)

<span class="hljs-comment">// ... 原本的业务代码</span>

<span class="hljs-comment">// HMR --------------------------------</span>
<span class="hljs-keyword">let</span> lastEditor = editor
<span class="hljs-built_in">module</span>.hot.accept(<span class="hljs-string">'./editor'</span>, <span class="hljs-function">() =></span> &#123;
  <span class="hljs-comment">// 当 editor.js 更新，自动执行此函数</span>
  <span class="hljs-comment">// 临时记录更新前编辑器内容</span>
  <span class="hljs-keyword">const</span> value = lastEditor.innerHTML
  <span class="hljs-comment">// 移除更新前的元素</span>
  <span class="hljs-built_in">document</span>.body.removeChild(lastEditor)
  <span class="hljs-comment">// 创建新的编辑器</span>
  <span class="hljs-comment">// 此时 createEditor 已经是更新过后的函数了</span>
  lastEditor = createEditor()
  <span class="hljs-comment">// 还原编辑器内容</span>
  lastEditor.innerHTML = value
  <span class="hljs-comment">// 追加到页面</span>
  <span class="hljs-built_in">document</span>.body.appendChild(lastEditor)
&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>为什么 Webpack 需要我们自己处理 JS 模块的热更新了：
因为不同的模块有不同的情况，不同的情况，在这里处理时肯定也是不同的。
就好像，我们这里是一个文本编辑器应用，所以需要保留状态，如果不是这种类型那就不需要这样做。
所以说 Webpack 没法提供一个通用的 JS 模块替换方案。</p>
<h3 data-id="heading-31">图片热模块替换</h3>
<p>我们同样通过 module.hot.accept 注册这个图片模块的热替换处理函数，在这个函数中，我们只需要重新给图片元素的 src 设置更新后的图片路径就可以了。
因为图片修改过后图片的文件名会发生变化，而这里我们就可以直接得到更新后的路径，所以重新设置图片的 src 就能实现图片热替换，具体代码如下：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">// ./src/main.js</span>
<span class="hljs-keyword">import</span> logo <span class="hljs-keyword">from</span> <span class="hljs-string">'./icon.png'</span>
<span class="hljs-comment">// ... 其他代码</span>
<span class="hljs-built_in">module</span>.hot.accept(<span class="hljs-string">'./icon.png'</span>, <span class="hljs-function">() =></span> &#123;
  <span class="hljs-comment">// 当 icon.png 更新后执行</span>
  <span class="hljs-comment">// 重写设置 src 会触发图片元素重新加载，从而局部更新图片</span>
  img.src = logo
&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-32">常见问题</h3>
<h4 data-id="heading-33">1. 热替换代码中有错误</h4>
<p>如果处理热替换的代码（处理函数）中有错误，结果也会导致自动刷新。例如我们这里在处理函数中故意加入一个运行时错误，代码如下：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">// ./src/main.js</span>
<span class="hljs-comment">// ... 其他代码</span>
<span class="hljs-built_in">module</span>.hot.accept(<span class="hljs-string">'./editor'</span>, <span class="hljs-function">() =></span> &#123;
  <span class="hljs-comment">// 刻意造成运行异常</span>
  <span class="hljs-literal">undefined</span>.foo()
&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这是因为 HMR 过程报错导致 HMR 失败，HMR 失败过后，会自动回退到自动刷新，页面一旦自动刷新，控制台中的错误信息就会被清除，这样的话，如果不是很明显的错误，就很难被发现。</p>
<p>在这种情况下，我们可以使用 hotOnly 的方式来解决，因为现在使用的 hot 方式，如果热替换失败就会自动回退使用自动刷新，而 hotOnly 的情况下并不会使用自动刷新。</p>
<p>我们回到配置文件中，这里我们将 devServer 中的 hot 等于 true 修改为 hotOnly 等于 true，具体代码如下：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">// ./webpack.config.js</span>
<span class="hljs-keyword">const</span> webpack = <span class="hljs-built_in">require</span>(<span class="hljs-string">'webpack'</span>)

<span class="hljs-built_in">module</span>.exports = &#123;
  <span class="hljs-comment">// ...</span>
  <span class="hljs-attr">devServer</span>: &#123;
    <span class="hljs-comment">// 只使用 HMR，不会 fallback 到 live reloading</span>
    <span class="hljs-attr">hotOnly</span>: <span class="hljs-literal">true</span>
  &#125;,
  <span class="hljs-attr">plugins</span>: [
    <span class="hljs-comment">// ...</span>
    <span class="hljs-comment">// HMR 特性所需要的插件</span>
    <span class="hljs-keyword">new</span> webpack.HotModuleReplacementPlugin()
  ]
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-34">2. 使用了HRM API, 但是未开启HMR功能</h4>
<p>对于使用了 HMR API 的代码，如果我们在没有开启 HMR 功能的情况下运行 Webpack 打包，此时运行环境中就会报出 Cannot read property 'accept' of undefined 的错误，具体错误信息如下：
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/2d721adac4e84330a8ba3bac8fc22869~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>原因是 module.hot 是 HMR 插件提供的成员，没有开启这个插件，自然也就没有这个对象。</p>
<p>解决办法也很简单，与我们在业务代码中判断 API 兼容一样，我们先判断是否存在这个对象，然后再去使用就可以了，具体代码如下：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">// HMR -----------------------------------</span>
<span class="hljs-keyword">if</span> (<span class="hljs-built_in">module</span>.hot) &#123; <span class="hljs-comment">// 确保有 HMR API 对象</span>
  <span class="hljs-built_in">module</span>.hot.accept(<span class="hljs-string">'./editor'</span>, <span class="hljs-function">() =></span> &#123;
    <span class="hljs-comment">// ...</span>
  &#125;)
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>我们回到配置文件中，确保已经将热替换特性关闭，并且移除掉了 HotModuleReplacementPlugin 插件，然后打开命令行终端，正常运行一下 Webpack 打包，打包过后，我们找到打包生成的 bundle.js 文件，然后找到里面 main.js 对应的模块，具体结果如下图：
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/6811eed134b5446691cbaf7205747244~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer">
你会发现之前我们编写的处理热替换的代码都被移除掉了，只剩下一个 if (false) 的空判断，这种没有意义的判断，在压缩过后也会自动去掉，所以根本不会对生产环境有任何影响。</p>
<h3 data-id="heading-35">关于框架的 HMR</h3>
<p>关于框架的 HMR，因为在大多数情况下是开箱即用的，所以这里不做过多介绍，详细可以参考：</p>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fgaearon%2Freact-hot-loader" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/gaearon/react-hot-loader" ref="nofollow noopener noreferrer">React HMR</a>
<a href="https://link.juejin.cn/?target=https%3A%2F%2Fvue-loader.vuejs.org%2Fguide%2Fhot-reload.html" target="_blank" rel="nofollow noopener noreferrer" title="https://vue-loader.vuejs.org/guide/hot-reload.html" ref="nofollow noopener noreferrer">Vue HMR</a></p>
<h2 data-id="heading-36">Tree-shaking</h2>
<h3 data-id="heading-37">Tree-shaking介绍</h3>
<p>Tree Shaking 翻译过来的意思就是“摇树”。伴随着摇树的动作，树上的枯树枝和树叶就会掉落下来。</p>
<p>我们这里要介绍的 Tree-shaking 也是同样的道理，不过通过 Tree-shaking “摇掉”的是代码中那些没有用到的部分，这部分没有用的代码更专业的说法应该叫作未引用代码（dead-code）。</p>
<p>Tree-shaking 最早是 Rollup 中推出的一个特性，Webpack 从 2.0 过后开始支持这个特性。</p>
<p>我们使用 Webpack 生产模式打包的优化过程中，就使用自动开启这个功能，以此来检测我们代码中的未引用代码，然后自动移除它们。</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">// ./src/components.js</span>
<span class="hljs-keyword">export</span> <span class="hljs-keyword">const</span> Button = <span class="hljs-function">() =></span> &#123;
  <span class="hljs-keyword">return</span> <span class="hljs-built_in">document</span>.createElement(<span class="hljs-string">'button'</span>)
  <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'dead-code'</span>)
&#125;

<span class="hljs-keyword">export</span> <span class="hljs-keyword">const</span> Link = <span class="hljs-function">() =></span> &#123;
  <span class="hljs-keyword">return</span> <span class="hljs-built_in">document</span>.createElement(<span class="hljs-string">'a'</span>)
&#125;

<span class="hljs-keyword">export</span> <span class="hljs-keyword">const</span> Heading = <span class="hljs-function"><span class="hljs-params">level</span> =></span> &#123;
  <span class="hljs-keyword">return</span> <span class="hljs-built_in">document</span>.createElement(<span class="hljs-string">'h'</span> + level)
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>其中 Button 组件函数中，在 return 过后还有一个 console.log() 语句，很明显这句代码永远都不会被执行，所以这个 console.log() 就属于未引用代码。</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">// ./src/main.js</span>
<span class="hljs-keyword">import</span> &#123; Button &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'./components'</span>
<span class="hljs-built_in">document</span>.body.appendChild(Button())
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这里导入 components 模块时，我们只提取了模块中的 Button 成员，那这就导致components 模块中很多地方都不会被用到，那这些地方就是冗余的，具体冗余部分如下：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">// ./src/components.js</span>
<span class="hljs-keyword">export</span> <span class="hljs-keyword">const</span> Button = <span class="hljs-function">() =></span> &#123;
  <span class="hljs-keyword">return</span> <span class="hljs-built_in">document</span>.createElement(<span class="hljs-string">'button'</span>)
  <span class="hljs-comment">// 未引用代码</span>
  <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'dead-code'</span>)
&#125;
<span class="hljs-comment">// 未引用代码</span>
<span class="hljs-keyword">export</span> <span class="hljs-keyword">const</span> Link = <span class="hljs-function">() =></span> &#123;
  <span class="hljs-keyword">return</span> <span class="hljs-built_in">document</span>.createElement(<span class="hljs-string">'a'</span>)
&#125;
<span class="hljs-comment">// 未引用代码</span>
<span class="hljs-keyword">export</span> <span class="hljs-keyword">const</span> Heading = <span class="hljs-function"><span class="hljs-params">level</span> =></span> &#123;
  <span class="hljs-keyword">return</span> <span class="hljs-built_in">document</span>.createElement(<span class="hljs-string">'h'</span> + level)
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>去除冗余代码是生产环境优化中一个很重要的工作，Webpack 的 Tree-shaking 功能就很好地实现了这一点。</p>
<p>我们打开命令行终端，这里我们尝试以 production 模式运行打包，具体命令如下：</p>
<pre><code class="hljs language-bash copyable" lang="bash">npx webpack --mode=production
<span class="copy-code-btn">复制代码</span></code></pre>
<p>Webpack 的 Tree-shaking 特性在生产模式下会自动开启。打包完成以后我们打开输出的 bundle.js，具体结果如下：
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/d221aa311e3e4a57be8a96f642dc2f76~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer">
通过搜索你会发现，components 模块中冗余的代码根本没有输出。这就是经过 Tree-shaking 处理过后的效果。</p>
<p>试想一下，如果我们在项目中引入 Lodash 这种工具库，大部分情况下我们只会使用其中的某几个工具函数，而其他没有用到的部分就是冗余代码。通过 Tree-shaking 就可以极大地减少最终打包后 bundle 的体积。</p>
<p>需要注意的是，Tree-shaking 并不是指 Webpack 中的某一个配置选项，而是一组功能搭配使用过后实现的效果，这组功能在生产模式下都会自动启用，所以使用生产模式打包就会有 Tree-shaking 的效果。</p>
<h3 data-id="heading-38">开启 Tree shaking</h3>
<p>这里还是上述的案例结构，我们再次运行 Webpack 打包，不过这一次我们不再使用 production 模式，而是使用 none，也就是不开启任何内置功能和插件，具体命令如下：</p>
<pre><code class="hljs language-bash copyable" lang="bash">npx webpack --mode=none
<span class="copy-code-btn">复制代码</span></code></pre>
<p>打包完成过后，我们再次找到输出的 bundle.js 文件，具体结果如下：
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/07cff003217346bf8b83922871ccedf9~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer">
我们这里注意一下 components 对应的这个模块，虽然外部没有使用这里的 Link 函数和 Heading 函数，但是仍然导出了它们，具体如下图所示：
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/91e14bfc160943eebca230af0faaba69~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer">
这种导出是没有任何意义的。</p>
<p>明确目前打包结果的状态过后，我们打开 Webpack 的配置文件，在配置对象中添加一个 optimization 属性，这个属性用来集中配置 Webpack 内置优化功能，它的值也是一个对象。</p>
<p>在 optimization 对象中我们可以先开启一个 usedExports 选项，表示在输出结果中只导出外部使用了的成员，具体配置代码如下：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">// ./webpack.config.js</span>
<span class="hljs-built_in">module</span>.exports = &#123;
  <span class="hljs-comment">// ... 其他配置项</span>
  <span class="hljs-attr">optimization</span>: &#123;
    <span class="hljs-comment">// 模块只导出被使用的成员</span>
    <span class="hljs-attr">usedExports</span>: <span class="hljs-literal">true</span>
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>配置完成后，重新打包，然后我们再来看一下输出的 bundle.js，具体结果如下图：
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/bd1e6b1d436240c0920e6c03924f7db8~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer">
此时你会发现 components 模块所对应的函数，就不再导出 Link 和 Heading 这两个函数了，那它们对应的代码就变成了未引用代码。而且如果你使用的是 VS Code，会发现 VS Code 将这两个函数名的颜色变淡了，这是为了表示它们未被引用。</p>
<p>对于这种未引用代码，如果我们开启压缩代码功能，就可以自动压缩掉这些没有用到的代码。</p>
<p>我们可以回到配置文件中，尝试在 optimization 配置中开启 minimize，具体配置如下：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">// ./webpack.config.js</span>
<span class="hljs-built_in">module</span>.exports = &#123;
  <span class="hljs-comment">// ... 其他配置项</span>
  <span class="hljs-attr">optimization</span>: &#123;
    <span class="hljs-comment">// 模块只导出被使用的成员</span>
    <span class="hljs-attr">usedExports</span>: <span class="hljs-literal">true</span>,
    <span class="hljs-comment">// 压缩输出结果</span>
    <span class="hljs-attr">minimize</span>: <span class="hljs-literal">true</span>
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>然后再次回到命令行重新运行打包，具体结果如下图所示：
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/7abcbb6015ee4427b266029dbfe98ae5~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>仔细查看打包结果，你会发现，Link 和 Heading 这些未引用代码都被自动移除了。</p>
<p>这就是 Tree-shaking 的实现，整个过程用到了 Webpack 的两个优化功能：</p>
<ol>
<li>usedExports - 打包结果中只导出外部用到的成员；</li>
<li>minimize - 压缩打包结果。</li>
</ol>
<p>如果把我们的代码看成一棵大树，那你可以这样理解：</p>
<ol>
<li>usedExports 的作用就是标记树上哪些是枯树枝、枯树叶；</li>
<li>minimize 的作用就是负责把枯树枝、枯树叶摇下来。</li>
</ol>
<h3 data-id="heading-39">合并模块(扩展)</h3>
<p>除了 usedExports 选项之外，我们还可以使用一个 concatenateModules 选项继续优化输出。</p>
<p>普通打包只是将一个模块最终放入一个单独的函数中，如果我们的模块很多，就意味着在输出结果中会有很多的模块函数。</p>
<p>concatenateModules 配置的作用就是尽可能将所有模块合并到一起输出到一个函数中，这样既提升了运行效率，又减少了代码的体积。</p>
<p>我们回到配置文件中，这里我们在 optimization 属性中开启 concatenateModules。同时，为了更好地看到效果，我们先关闭 minimize，具体配置如下：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">// ./webpack.config.js</span>
<span class="hljs-built_in">module</span>.exports = &#123;
  <span class="hljs-comment">// ... 其他配置项</span>
  <span class="hljs-attr">optimization</span>: &#123;
    <span class="hljs-comment">// 模块只导出被使用的成员</span>
    <span class="hljs-attr">usedExports</span>: <span class="hljs-literal">true</span>,
    <span class="hljs-comment">// 尽可能合并每一个模块到一个函数中</span>
    <span class="hljs-attr">concatenateModules</span>: <span class="hljs-literal">true</span>,
    <span class="hljs-comment">// 压缩输出结果</span>
    <span class="hljs-attr">minimize</span>: <span class="hljs-literal">false</span>
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>然后回到命令行终端再次运行打包。那此时 bundle.js 中就不再是一个模块对应一个函数了，而是把所有的模块都放到了一个函数中，具体结果如下：
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/40303850dc834529b65d09037feb4f09~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer">
这个特性又被称为 Scope Hoisting，也就是作用域提升，它是 Webpack 3.0 中添加的一个特性。</p>
<p>如果再配合 minimize 选项，打包结果的体积又会减小很多。</p>
<h3 data-id="heading-40">结合babel-loader的问题</h3>
<p>因为早期的 Webpack 发展非常快，那变化也就比较多，所以当我们去找资料时，得到的结果不一定适用于当前我们所使用的版本。而 Tree-shaking 的资料更是如此，很多资料中都表示“为 JS 模块配置 babel-loader，会导致 Tree-shaking 失效”。</p>
<p>Tree-shaking 实现的前提是 ES Modules，也就是说：最终交给 Webpack 打包的代码，必须是使用 ES Modules 的方式来组织的模块化。</p>
<p>我们都知道 Webpack 在打包所有的模块代码之前，先是将模块根据配置交给不同的 Loader 处理，最后再将 Loader 处理的结果打包到一起。</p>
<p>很多时候，我们为了更好的兼容性，会选择使用 babel-loader 去转换我们源代码中的一些 ECMAScript 的新特性。而 Babel 在转换 JS 代码时，很有可能处理掉我们代码中的 ES Modules 部分，把它们转换成 CommonJS 的方式，如下图所示：
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/b5f9232d8ac942ab8ed4a28f9aaf1d52~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>Babel 具体会不会处理 ES Modules 代码，取决于我们有没有为它配置使用转换 ES Modules 的插件。</p>
<p>很多时候，我们为 Babel 配置的都是一个 preset（预设插件集合），而不是某些具体的插件。例如，目前市面上使用最多的 @babel/preset-env，这个预设里面就有转换 ES Modules 的插件。所以当我们使用这个预设时，代码中的 ES Modules 部分就会被转换成 CommonJS 方式。那 Webpack 再去打包时，拿到的就是以 CommonJS 方式组织的代码了，所以 Tree-shaking 不能生效。</p>
<p>为了可以更容易分辨结果，我们只开启 usedExports，完整配置如下：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">// ./webpack.config.js</span>
<span class="hljs-built_in">module</span>.exports = &#123;
  <span class="hljs-attr">mode</span>: <span class="hljs-string">'none'</span>,
  <span class="hljs-attr">entry</span>: <span class="hljs-string">'./src/main.js'</span>,
  <span class="hljs-attr">output</span>: &#123;
    <span class="hljs-attr">filename</span>: <span class="hljs-string">'bundle.js'</span>
  &#125;,
  <span class="hljs-attr">module</span>: &#123;
    <span class="hljs-attr">rules</span>: [
      &#123;
        <span class="hljs-attr">test</span>: <span class="hljs-regexp">/\.js$/</span>,
        use: &#123;
          <span class="hljs-attr">loader</span>: <span class="hljs-string">'babel-loader'</span>,
          <span class="hljs-attr">options</span>: &#123;
            <span class="hljs-attr">presets</span>: [
              [<span class="hljs-string">'@babel/preset-env'</span>]
            ]
          &#125;
        &#125;
      &#125;
    ]
  &#125;,
  <span class="hljs-attr">optimization</span>: &#123;
    <span class="hljs-attr">usedExports</span>: <span class="hljs-literal">true</span>
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>配置完成过后，我们打开命令行终端，运行 Webpack 打包命令，然后再找到 bundle.js，具体结果如下：
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/34992f51e2b5487aa8a6874526438d5a~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer">
仔细查看你会发现，结果并不是像刚刚说的那样，这里 usedExports 功能仍然正常工作了，此时，如果我们压缩代码，这些未引用的代码依然会被移除。这也就说明 Tree-shaking 并没有失效。</p>
<p>那到底是怎么回事呢？为什么很多资料都说 babel-loader 会导致 Tree-shaking 失效，但当我们实际尝试后又发现并没有失效？</p>
<p>其实，这是因为在最新版本（8.x）的 babel-loader 中，已经自动帮我们关闭了对 ES Modules 转换的插件，你可以参考对应版本 babel-loader 的源码，核心代码如下：
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/2fc0631ff5a64d83bb6dc7f08851b3f9~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer">
通过查阅 babel-loader 模块的源码，我们发现它已经在 injectCaller 函数中标识了当前环境支持 ES Modules。</p>
<p>然后再找到我们所使用的 @babal/preset-env 模块源码，部分核心代码如下：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/dbce547e94fa46d8a0a507f56bb44ee3~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer">
在这个模块中，根据环境标识自动禁用了对 ES Modules 的转换插件，所以经过 babel-loader 处理后的代码默认仍然是 ES Modules，那 Webpack 最终打包得到的还是 ES Modules 代码，Tree-shaking 自然也就可以正常工作了。</p>
<p>我们也可以在 babel-loader 的配置中强制开启 ES Modules 转换插件来试一下，具体配置如下：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">// ./webpack.config.js</span>
<span class="hljs-built_in">module</span>.exports = &#123;
  <span class="hljs-attr">mode</span>: <span class="hljs-string">'none'</span>,
  <span class="hljs-attr">entry</span>: <span class="hljs-string">'./src/main.js'</span>,
  <span class="hljs-attr">output</span>: &#123;
    <span class="hljs-attr">filename</span>: <span class="hljs-string">'bundle.js'</span>
  &#125;,
  <span class="hljs-attr">module</span>: &#123;
    <span class="hljs-attr">rules</span>: [
      &#123;
        <span class="hljs-attr">test</span>: <span class="hljs-regexp">/\.js$/</span>,
        use: &#123;
          <span class="hljs-attr">loader</span>: <span class="hljs-string">'babel-loader'</span>,
          <span class="hljs-attr">options</span>: &#123;
            <span class="hljs-attr">presets</span>: [
              [<span class="hljs-string">'@babel/preset-env'</span>, &#123; <span class="hljs-attr">modules</span>: <span class="hljs-string">'commonjs'</span> &#125;]
            ]
          &#125;
        &#125;
      &#125;
    ]
  &#125;,
  <span class="hljs-attr">optimization</span>: &#123;
    <span class="hljs-attr">usedExports</span>: <span class="hljs-literal">true</span>
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>给 Babel preset 添加配置的方式比较特别，这里很多人都会配错，一定要注意。它需要把预设数组中的成员定义成一个数组，然后这个数组中的第一个成员就是所使用的 preset 的名称，第二个成员就是给这个 preset 定义的配置对象。</p>
<p>我们在这个对象中将 modules 属性设置为 "commonjs"，默认这个属性是 auto，也就是根据环境判断是否开启 ES Modules 插件，我们设置为 commonjs 就表示我们强制使用 Babel 的 ES Modules 插件把代码中的 ES Modules 转换为 CommonJS。</p>
<p>完成以后，我们再次打开命令行终端，运行 Webpack 打包。然后找到 bundle.js，结果如下：
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/1f04b979fa7344139002fea791c30f1f~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer">
此时，你就会发现 usedExports 没法生效了。即便我们开启压缩代码，Tree-shaking 也会失效。</p>
<p>总结一下，这里通过实验发现，最新版本的 babel-loader 并不会导致 Tree-shaking 失效。如果你不确定现在使用的 babel-loader 会不会导致这个问题，最简单的办法就是在配置中将 @babel/preset-env 的 modules 属性设置为 false，确保不会转换 ES Modules，也就确保了 Tree-shaking 的前提。</p>
<h2 data-id="heading-41">SideEffects</h2>
<h3 data-id="heading-42">SideEffects简介</h3>
<p>Webpack 4 中新增了一个 sideEffects 特性，它允许我们通过配置标识我们的代码是否有副作用，从而提供更大的压缩空间。</p>
<blockquote>
<p>TIPS：模块的副作用指的就是模块执行的时候除了导出成员，是否还做了其他的事情。</p>
</blockquote>
<p>这个特性一般只有我们去开发一个 npm 模块时才会用到。因为官网把对 sideEffects 特性的介绍跟 Tree-shaking 混到了一起，所以很多人误认为它们之间是因果关系，其实它们没有什么太大的关系。</p>
<p>我们先把 sideEffects 特性本身的作用弄明白，你就更容易理解为什么说它跟 Tree-shaking 没什么关系了。</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">// ./src/components/index.js</span>
<span class="hljs-keyword">export</span> &#123; <span class="hljs-keyword">default</span> <span class="hljs-keyword">as</span> Button &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'./button'</span>
<span class="hljs-keyword">export</span> &#123; <span class="hljs-keyword">default</span> <span class="hljs-keyword">as</span> Link &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'./link'</span>
<span class="hljs-keyword">export</span> &#123; <span class="hljs-keyword">default</span> <span class="hljs-keyword">as</span> Heading &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'./heading'</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>另外，在每个组件中，我们都添加了一个 console 操作（副作用代码），具体代码如下：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">// ./src/components/button.js</span>
<span class="hljs-built_in">console</span>.log(<span class="hljs-string">'Button component~'</span>) <span class="hljs-comment">// 副作用代码</span>

<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> () => &#123;
  <span class="hljs-keyword">return</span> <span class="hljs-built_in">document</span>.createElement(<span class="hljs-string">'button'</span>)
&#125;

我们再到打包入口文件（main.js）中去载入 components 中的 Button 成员，具体代码如下：

<span class="hljs-comment">// ./src/main.js</span>
<span class="hljs-keyword">import</span> &#123; Button &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'./components'</span>

<span class="hljs-built_in">document</span>.body.appendChild(Button())
<span class="copy-code-btn">复制代码</span></code></pre>
<p>那这样就会出现一个问题，虽然我们在这里只是希望载入 Button 模块，但实际上载入的是 components/index.js，而 index.js 中又载入了这个目录中全部的组件模块，这就会导致所有组件模块都会被加载执行。</p>
<p>我们打开命令行终端，尝试运行打包，打包完成过后找到打包结果，具体结果如下：
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/e6870493c2da414bad050aca407cd56e~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer">
此时如果我们开启 Tree-shaking 特性（只设置 useExports），这里没有用到的导出成员其实最终也可以被移除，打包效果如下：
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/877208fd93f54ca1af7bacbb6ed34657~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer">
但是由于这些成员所属的模块中有副作用代码，所以就导致最终 Tree-shaking 过后，这些模块并不会被完全移除。</p>
<p>可能你会认为这些代码应该保留下来，而实际情况是，这些模块内的副作用代码一般都是为这个模块服务的，例如这里我添加的 console.log，就是希望表示一下当前这个模块被加载了。但是最终整个模块都没用到，也就没必要留下这些副作用代码了。</p>
<p>Tree-shaking 只能移除没有用到的代码成员，而想要完整移除没有用到的模块，那就需要开启 sideEffects 特性了。</p>
<h3 data-id="heading-43">sideEffects作用</h3>
<p>打开 Webpack 的配置文件，在 optimization 中开启 sideEffects 特性，具体配置如下：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">// ./webpack.config.js</span>
<span class="hljs-built_in">module</span>.exports = &#123;
  <span class="hljs-attr">mode</span>: <span class="hljs-string">'none'</span>,
  <span class="hljs-attr">entry</span>: <span class="hljs-string">'./src/main.js'</span>,
  <span class="hljs-attr">output</span>: &#123;
    <span class="hljs-attr">filename</span>: <span class="hljs-string">'bundle.js'</span>
  &#125;,
  <span class="hljs-attr">optimization</span>: &#123;
    <span class="hljs-attr">sideEffects</span>: <span class="hljs-literal">true</span>
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<blockquote>
<p>TIPS：注意这个特性在 production 模式下同样会自动开启。</p>
</blockquote>
<p>那此时 Webpack 在打包某个模块之前，会先检查这个模块所属的 package.json 中的 sideEffects 标识，以此来判断这个模块是否有副作用，如果没有副作用的话，这些没用到的模块就不再被打包。
换句话说，即便这些没有用到的模块中存在一些副作用代码，我们也可以通过 package.json 中的 sideEffects 去强制声明没有副作用。</p>
<p>那我们打开项目 package.json 添加一个 sideEffects 字段，把它设置为 false，具体代码如下：</p>
<pre><code class="hljs language-json copyable" lang="json">&#123;
  <span class="hljs-attr">"name"</span>: <span class="hljs-string">"09-side-effects"</span>,
  <span class="hljs-attr">"version"</span>: <span class="hljs-string">"0.1.0"</span>,
  <span class="hljs-attr">"author"</span>: <span class="hljs-string">"zce <w@zce.me> (https://zce.me)"</span>,
  <span class="hljs-attr">"license"</span>: <span class="hljs-string">"MIT"</span>,
  <span class="hljs-attr">"scripts"</span>: &#123;
    <span class="hljs-attr">"build"</span>: <span class="hljs-string">"webpack"</span>
  &#125;,
  <span class="hljs-attr">"devDependencies"</span>: &#123;
    <span class="hljs-attr">"webpack"</span>: <span class="hljs-string">"^4.43.0"</span>,
    <span class="hljs-attr">"webpack-cli"</span>: <span class="hljs-string">"^3.3.11"</span>
  &#125;,
  <span class="hljs-attr">"sideEffects"</span>: <span class="hljs-literal">false</span>
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这样就表示我们这个项目中的所有代码都没有副作用，让 Webpack 放心大胆地去“干”。</p>
<p>完成以后我们再次运行打包，然后同样找到打包输出的 bundle.js 文件，结果如下：
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/f080306213ba4e76bc7bd03264662880~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer">
此时那些没有用到的模块就彻底不会被打包进来了。那这就是 sideEffects 的作用。</p>
<p>这里设置了两个地方：</p>
<ol>
<li>webpack.config.js 中的 sideEffects 用来开启这个功能；</li>
<li>package.json 中的 sideEffects 用来标识我们的代码没有副作用。</li>
</ol>
<h3 data-id="heading-44">SideEffects注意点</h3>
<p>对全局有影响的副作用代码不能移除，而只是对模块有影响的副作用代码就可以移除。</p>
<p>使用 sideEffects 这个功能的前提是确定你的代码没有副作用，或者副作用代码没有全局影响，否则打包时就会误删掉你那些有意义的副作用代码。</p>
<p>例如，我这里准备的 extend.js 模块：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">// ./src/extend.js</span>
<span class="hljs-comment">// 为 Number 的原型添加一个扩展方法</span>
<span class="hljs-built_in">Number</span>.prototype.pad = <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params">size</span>) </span>&#123;
  <span class="hljs-keyword">const</span> leadingZeros = <span class="hljs-built_in">Array</span>(size + <span class="hljs-number">1</span>).join(<span class="hljs-number">0</span>)
  <span class="hljs-keyword">return</span> leadingZeros + <span class="hljs-built_in">this</span>
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>在这个模块中并没有导出任何成员，仅仅是在 Number 的原型上挂载了一个 pad 方法，用来为数字添加前面的导零，这是一种很早以前常见的基于原型的扩展方法。</p>
<p>我们回到 main.js 中去导入 extend 模块，具体代码如下：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">// ./src/main.js</span>
<span class="hljs-keyword">import</span> <span class="hljs-string">'./extend'</span> <span class="hljs-comment">// 内部包含影响全局的副作用</span>

<span class="hljs-built_in">console</span>.log((<span class="hljs-number">8</span>).pad(<span class="hljs-number">3</span>)) <span class="hljs-comment">// => '0008'</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>因为这个模块确实没有导出任何成员，所以这里也就不需要提取任何成员。导入过后就可以使用它为 Number 提供扩展方法了。</p>
<p>这里为 Number 类型做扩展的操作就是 extend 模块对全局产生的副作用。</p>
<p>此时如果我们还是通过 package.json 标识我们代码没有副作用，那么再次打包过后，就会出现问题。我们可以找到打包结果，如下图所示：
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/f6c3464e8b414da0969556e5a4b5652a~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer">
我们看到，对 Number 的扩展模块并不会打包进来。</p>
<p>缺少了对 Number 的扩展操作，我们的代码再去运行的时候，就会出现错误。这种扩展的操作属于对全局产生的副作用。</p>
<p>这种基于原型的扩展方式，在很多 Polyfill 库中都会大量出现，比较常见的有 es6-promise，这种模块都属于典型的副作用模块。
除此之外，我们在 JS 中直接载入的 CSS 模块，也都属于副作用模块，同样会面临这种问题。
所以说不是所有的副作用都应该被移除，有一些必要的副作用需要保留下来。</p>
<p>最好的办法就是在 package.json 中的 sideEffects 字段中标识需要保留副作用的模块路径（可以使用通配符），具体配置如下：</p>
<pre><code class="hljs language-json copyable" lang="json">&#123;
  <span class="hljs-attr">"name"</span>: <span class="hljs-string">"09-side-effects"</span>,
  <span class="hljs-attr">"version"</span>: <span class="hljs-string">"0.1.0"</span>,
  <span class="hljs-attr">"author"</span>: <span class="hljs-string">"zce <w@zce.me> (https://zce.me)"</span>,
  <span class="hljs-attr">"license"</span>: <span class="hljs-string">"MIT"</span>,
  <span class="hljs-attr">"scripts"</span>: &#123;
    <span class="hljs-attr">"build"</span>: <span class="hljs-string">"webpack"</span>
  &#125;,
  <span class="hljs-attr">"devDependencies"</span>: &#123;
    <span class="hljs-attr">"webpack"</span>: <span class="hljs-string">"^4.43.0"</span>,
    <span class="hljs-attr">"webpack-cli"</span>: <span class="hljs-string">"^3.3.11"</span>
  &#125;,
  <span class="hljs-attr">"sideEffects"</span>: [
    <span class="hljs-string">"./src/extend.js"</span>,
    <span class="hljs-string">"*.css"</span>
  ]
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>总之不管是 Tree-shaking 还是 sideEffects，它们都是为了弥补 JavaScript 早期在模块系统设计上的不足。随着 Webpack 这类技术的发展，JavaScript 的模块化确实越来越好用，也越来越合理。</p>
<h2 data-id="heading-45">Code Spliting(分块打包)</h2>
<h3 data-id="heading-46">All in One 的弊端</h3>
<p>通过 Webpack 实现前端项目整体模块化的优势固然明显，但是它也会存在一些弊端：它最终会将我们所有的代码打包到一起。试想一下，如果我们的应用非常复杂，模块非常多，那么这种 All in One 的方式就会导致打包的结果过大，甚至超过 4～5M。</p>
<p>在绝大多数的情况下，应用刚开始工作时，并不是所有的模块都是必需的。如果这些模块全部被打包到一起，即便应用只需要一两个模块工作，也必须先把 bundle.js 整体加载进来，而且前端应用一般都是运行在浏览器端，这也就意味着应用的响应速度会受到影响，也会浪费大量的流量和带宽。</p>
<p>所以这种 All in One 的方式并不合理，更为合理的方案是把打包的结果按照一定的规则分离到多个 bundle 中，然后根据应用的运行需要按需加载。这样就可以降低启动成本，提高响应速度。</p>
<p>Webpack 就是通过把项目中散落的模块打包到一起，从而提高加载效率，那么为什么这里又要分离？这不是自相矛盾吗？</p>
<p>Web 应用中的资源受环境所限，太大不行，太碎更不行。因为我们开发过程中划分模块的颗粒度一般都会非常的细，很多时候一个模块只是提供了一个小工具函数，并不能形成一个完整的功能单元。</p>
<p>如果我们不将这些资源模块打包，直接按照开发过程中划分的模块颗粒度进行加载，那么运行一个小小的功能，就需要加载非常多的资源模块。</p>
<p>HTTP1.1本身存在缺陷</p>
<ol>
<li>同一个域名下的并行请求是有限制的；</li>
<li>每次请求本身都会有一定的延迟；</li>
<li>每次请求除了传输内容，还有额外的请求头，大量请求的情况下，这些请求头加在一起也会浪费流量和带宽。</li>
</ol>
<h3 data-id="heading-47">Code Splitting</h3>
<p>为了解决打包结果过大导致的问题，Webpack 设计了一种分包功能：Code Splitting（代码分割）。</p>
<p>Code Splitting 通过把项目中的资源模块按照我们设计的规则打包到不同的 bundle 中，从而降低应用的启动成本，提高响应速度。</p>
<p>Webpack 实现分包的方式主要有两种：</p>
<ol>
<li>根据业务不同配置多个打包入口，输出多个打包结果；</li>
<li>结合 ES Modules 的动态导入（Dynamic Imports）特性，按需加载模块。</li>
</ol>
<h3 data-id="heading-48">多入口打包</h3>
<p>多入口打包一般适用于传统的多页应用程序，最常见的划分规则就是一个页面对应一个打包入口，对于不同页面间公用的部分，再提取到公共的结果中。</p>
<p>示例源码</p>
<p>GitHub：<a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fzce%2Fwebpack-multi-entry" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/zce/webpack-multi-entry" ref="nofollow noopener noreferrer">github.com/zce/webpack…</a>
CodeSandbox：<a href="https://link.juejin.cn/?target=https%3A%2F%2Fcodesandbox.io%2Fs%2Fgithub%2Fzce%2Fwebpack-multi-entry" target="_blank" rel="nofollow noopener noreferrer" title="https://codesandbox.io/s/github/zce/webpack-multi-entry" ref="nofollow noopener noreferrer">codesandbox.io/s/github/zc…</a></p>
<pre><code class="hljs language-bash copyable" lang="bash">.
├── dist
├── src
│   ├── common
│   │   ├── fetch.js
│   │   └── global.css
│   ├── album.css
│   ├── album.html
│   ├── album.js
│   ├── index.css
│   ├── index.html
│   └── index.js
├── package.json
└── webpack.config.js
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这个示例中有两个页面，分别是 index 和 album。代码组织的逻辑也很简单：</p>
<ul>
<li>index.js 负责实现 index 页面功能逻辑；</li>
<li>album.js 负责实现 album 页面功能逻辑；</li>
<li>global.css 是公用的样式文件；</li>
<li>fetch.js 是一个公用的模块，负责请求 API。</li>
</ul>
<p>为这个案例配置多入口打包，具体配置如下：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">// ./webpack.config.js</span>
<span class="hljs-keyword">const</span> HtmlWebpackPlugin = <span class="hljs-built_in">require</span>(<span class="hljs-string">'html-webpack-plugin'</span>)
<span class="hljs-built_in">module</span>.exports = &#123;
  <span class="hljs-attr">entry</span>: &#123;
    <span class="hljs-attr">index</span>: <span class="hljs-string">'./src/index.js'</span>,
    <span class="hljs-attr">album</span>: <span class="hljs-string">'./src/album.js'</span>
  &#125;,
  <span class="hljs-attr">output</span>: &#123;
    <span class="hljs-attr">filename</span>: <span class="hljs-string">'[name].bundle.js'</span> <span class="hljs-comment">// [name] 是入口名称</span>
  &#125;,
  <span class="hljs-comment">// ... 其他配置</span>
  <span class="hljs-attr">plugins</span>: [
    <span class="hljs-keyword">new</span> HtmlWebpackPlugin(&#123;
      <span class="hljs-attr">title</span>: <span class="hljs-string">'Multi Entry'</span>,
      <span class="hljs-attr">template</span>: <span class="hljs-string">'./src/index.html'</span>,
      <span class="hljs-attr">filename</span>: <span class="hljs-string">'index.html'</span>,
      <span class="hljs-attr">chunks</span>: [<span class="hljs-string">'index'</span>] <span class="hljs-comment">// 指定使用 index.bundle.js</span>
    &#125;),
    <span class="hljs-keyword">new</span> HtmlWebpackPlugin(&#123;
      <span class="hljs-attr">title</span>: <span class="hljs-string">'Multi Entry'</span>,
      <span class="hljs-attr">template</span>: <span class="hljs-string">'./src/album.html'</span>,
      <span class="hljs-attr">filename</span>: <span class="hljs-string">'album.html'</span>,
      <span class="hljs-attr">chunks</span>: [<span class="hljs-string">'album'</span>] <span class="hljs-comment">// 指定使用 album.bundle.js</span>
    &#125;)
  ]
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>一般 entry 属性中只会配置一个打包入口，如果我们需要配置多个入口，可以把 entry 定义成一个对象。</p>
<p>这里 entry 是定义为对象而不是数组，如果是数组的话就是把多个文件打包到一起，还是一个入口。</p>
<p>在这个对象中一个属性就是一个入口，属性名称就是这个入口的名称，值就是这个入口对应的文件路径。那我们这里配置的就是 index 和 album 页面所对应的 JS 文件路径。</p>
<p>一旦我们的入口配置为多入口形式，那输出文件名也需要修改，因为两个入口就有两个打包结果，不能都叫 bundle.js。我们可以在这里使用 [name] 这种占位符来输出动态的文件名，[name] 最终会被替换为入口的名称。</p>
<p>除此之外，在配置中还通过 html-webpack-plugin 分别为 index 和 album 页面生成了对应的 HTML 文件。</p>
<p>找到输出 HTML 的插件，默认这个插件会自动注入所有的打包结果，如果需要指定所使用的 bundle，我们可以通过 HtmlWebpackPlugin 的 chunks 属性来设置。我们分别为两个页面配置使用不同的 chunk, 让每个打包入口都会形成一个独立的 chunk（块）。</p>
<p>完成配置之后，我们就可以打开命令行终端，运行 Webpack 打包，那此次打包会有两个入口。打包完成后，我们找到输出目录，这里就能看到两个入口文件各自的打包结果了，如下图所示：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/ee3e8ff63f3441ababfb4ac676712a53~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/6f3b2d07057346a8b0a8d9e72d788c3e~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-49">提取公共模块</h3>
<p>我们还需要把这些公共的模块提取到一个单独的 bundle 中。Webpack 中实现公共模块提取非常简单，我们只需要在优化配置中开启 splitChunks 功能就可以了，具体配置如下：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">// ./webpack.config.js</span>
<span class="hljs-built_in">module</span>.exports = &#123;
  <span class="hljs-attr">entry</span>: &#123;
    <span class="hljs-attr">index</span>: <span class="hljs-string">'./src/index.js'</span>,
    <span class="hljs-attr">album</span>: <span class="hljs-string">'./src/album.js'</span>
  &#125;,
  <span class="hljs-attr">output</span>: &#123;
    <span class="hljs-attr">filename</span>: <span class="hljs-string">'[name].bundle.js'</span> <span class="hljs-comment">// [name] 是入口名称</span>
  &#125;,
  <span class="hljs-attr">optimization</span>: &#123;
    <span class="hljs-attr">splitChunks</span>: &#123;
      <span class="hljs-comment">// 自动提取所有公共模块到单独 bundle</span>
      <span class="hljs-attr">chunks</span>: <span class="hljs-string">'all'</span>
    &#125;
  &#125;
  <span class="hljs-comment">// ... 其他配置</span>
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这里在 optimization 属性中添加 splitChunks 属性，那这个属性的值是一个对象，这个对象需要配置一个 chunks 属性，我们这里将它设置为 all，表示所有公共模块都可以被提取。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/9b2cb476c78142a4a3975cb82bad1ea3~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer">
<a href="https://link.juejin.cn/?target=https%3A%2F%2Fwebpack.js.org%2Fplugins%2Fsplit-chunks-plugin%2F" target="_blank" rel="nofollow noopener noreferrer" title="https://webpack.js.org/plugins/split-chunks-plugin/" ref="nofollow noopener noreferrer">splitChunks的其它用法</a></p>
<h3 data-id="heading-50">动态导入</h3>
<p>Code Splitting 更常见的实现方式还是结合 ES Modules 的动态导入特性，从而实现按需加载。</p>
<p>Webpack 中支持使用动态导入的方式实现模块的按需加载，而且所有动态导入的模块都会被自动提取到单独的 bundle 中，从而实现分包。</p>
<p>相比于多入口的方式，动态导入更为灵活，因为我们可以通过代码中的逻辑去控制需不需要加载某个模块，或者什么时候加载某个模块。而且我们分包的目的中，很重要的一点就是让模块实现按需加载，从而提高应用的响应速度。</p>
<pre><code class="hljs language-javascript copyable" lang="javascript">.
├── src
│   ├── album
│   │   ├── album.css
│   │   └── album.js
│   ├── common
│   │   ├── fetch.js
│   │   └── <span class="hljs-built_in">global</span>.css
│   ├── posts
│   │   ├── posts.css
│   │   └── posts.js
│   ├── index.html
│   └── index.js
├── package.json
└── webpack.config.js
<span class="copy-code-btn">复制代码</span></code></pre>
<p>文章列表对应的是这里的 posts 组件，而相册列表对应的是 album 组件。我在打包入口（index.js）中同时导入了这两个模块，然后根据页面锚点的变化决定显示哪个组件，核心代码如下：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">// ./src/index.js</span>
<span class="hljs-keyword">import</span> posts <span class="hljs-keyword">from</span> <span class="hljs-string">'./posts/posts'</span>
<span class="hljs-keyword">import</span> album <span class="hljs-keyword">from</span> <span class="hljs-string">'./album/album'</span>
<span class="hljs-keyword">const</span> update = <span class="hljs-function">() =></span> &#123;
  <span class="hljs-keyword">const</span> hash = <span class="hljs-built_in">window</span>.location.hash || <span class="hljs-string">'#posts'</span>
  <span class="hljs-keyword">const</span> mainElement = <span class="hljs-built_in">document</span>.querySelector(<span class="hljs-string">'.main'</span>)
  mainElement.innerHTML = <span class="hljs-string">''</span>
  <span class="hljs-keyword">if</span> (hash === <span class="hljs-string">'#posts'</span>) &#123;
    mainElement.appendChild(posts())
  &#125; <span class="hljs-keyword">else</span> <span class="hljs-keyword">if</span> (hash === <span class="hljs-string">'#album'</span>) &#123;
    mainElement.appendChild(album())
  &#125;
&#125;
<span class="hljs-built_in">window</span>.addEventListener(<span class="hljs-string">'hashchange'</span>, update)
update()
<span class="copy-code-btn">复制代码</span></code></pre>
<p>为了动态导入模块，可以将 import 关键字作为函数调用。当以这种方式使用时，import 函数返回一个 Promise 对象。这就是 ES Modules 标准中的 Dynamic Imports。</p>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FJavaScript%2FReference%2FStatements%2Fimport%23Dynamic_Imports" target="_blank" rel="nofollow noopener noreferrer" title="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/import#Dynamic_Imports" ref="nofollow noopener noreferrer">Dynamic Imports</a></p>
<p>采用动态导入的方式，就不会产生浪费的问题了，因为所有的组件都是惰性加载，只有用到的时候才会去加载。具体实现代码如下：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">// ./src/index.js</span>
<span class="hljs-comment">// import posts from './posts/posts'</span>
<span class="hljs-comment">// import album from './album/album'</span>
<span class="hljs-keyword">const</span> update = <span class="hljs-function">() =></span> &#123;
  <span class="hljs-keyword">const</span> hash = <span class="hljs-built_in">window</span>.location.hash || <span class="hljs-string">'#posts'</span>
  <span class="hljs-keyword">const</span> mainElement = <span class="hljs-built_in">document</span>.querySelector(<span class="hljs-string">'.main'</span>)
  mainElement.innerHTML = <span class="hljs-string">''</span>
  <span class="hljs-keyword">if</span> (hash === <span class="hljs-string">'#posts'</span>) &#123;
    <span class="hljs-comment">// mainElement.appendChild(posts())</span>
    <span class="hljs-keyword">import</span>(<span class="hljs-string">'./posts/posts'</span>).then(<span class="hljs-function">(<span class="hljs-params">&#123; <span class="hljs-keyword">default</span>: posts &#125;</span>) =></span> &#123;
      mainElement.appendChild(posts())
    &#125;)
  &#125; <span class="hljs-keyword">else</span> <span class="hljs-keyword">if</span> (hash === <span class="hljs-string">'#album'</span>) &#123;
    <span class="hljs-comment">// mainElement.appendChild(album())</span>
    <span class="hljs-keyword">import</span>(<span class="hljs-string">'./album/album'</span>).then(<span class="hljs-function">(<span class="hljs-params">&#123; <span class="hljs-keyword">default</span>: album &#125;</span>) =></span> &#123;
      mainElement.appendChild(album())
    &#125;)
  &#125;
&#125;
<span class="hljs-built_in">window</span>.addEventListener(<span class="hljs-string">'hashchange'</span>, update)
update()
<span class="copy-code-btn">复制代码</span></code></pre>
<p>在需要使用组件的地方通过 import 函数导入指定路径，那这个方法返回的是一个 Promise。
在这个 Promise 的 then 方法中我们能够拿到模块对象。
由于我们这里的 posts 和 album 模块是以默认成员导出，所以我们需要解构模块对象中的 default，先拿到导出成员，然后再正常使用这个导出成员。</p>
<p>打包结果具体结果:
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/af464fed683646e6a3f37684e85c392a~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer">
此时 dist 目录下就会额外多出三个 JS 文件，其中有两个文件是动态导入的模块，另外一个文件是动态导入模块中公共的模块，这三个文件就是由动态导入自动分包产生的。</p>
<p>动态导入在 Webpack 中的使用。整个过程我们无需额外配置任何地方，只需要按照 ES Modules 动态导入的方式去导入模块就可以了，Webpack 内部会自动处理分包和按需加载。</p>
<p>如果使用的是 Vue.js 之类的 SPA 开发框架的话，那你项目中路由映射的组件就可以通过这种动态导入的方式实现按需加载，从而实现分包。</p>
<h3 data-id="heading-51">魔法注释</h3>
<p>默认通过动态导入产生的 bundle 文件，它的 name 就是一个序号，这并没有什么不好，因为大多数时候，在生产环境中我们根本不用关心资源文件的名称。</p>
<p>但是如果你还是需要给这些 bundle 命名的话，就可以使用 Webpack 所特有的魔法注释去实现。具体方式如下：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">// 魔法注释</span>
<span class="hljs-keyword">import</span>(<span class="hljs-comment">/* webpackChunkName: 'posts' */</span><span class="hljs-string">'./posts/posts'</span>)
  .then(<span class="hljs-function">(<span class="hljs-params">&#123; <span class="hljs-keyword">default</span>: posts &#125;</span>) =></span> &#123;
    mainElement.appendChild(posts())
  &#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>所谓魔法注释，就是在 import 函数的形式参数位置，添加一个行内注释，这个注释有一个特定的格式：webpackChunkName: ''，这样就可以给分包的 chunk 起名字了。</p>
<p>完成过后，我们再次打开命令行终端，运行 Webpack 打包，那此时我们生成 bundle 的 name 就会使用刚刚注释中提供的名称了，具体结果如下：
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/88e9139781864c8a9c125642036a2f04~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer">
魔法注释还有个特殊用途：如果你的 chunkName 相同的话，那相同的 chunkName 最终就会被打包到一起，例如我们这里可以把这两个 chunkName 都设置为 components，然后再次运行打包，那此时这两个模块都会被打包到一个文件中，具体操作如下图所示：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/875a22ac1b1046dd8763494bfef4efe5~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-52">构建速度与打包结果</h2>
<p>生产环境和开发环境有很大的差异，在生产环境中我们强调的是以更少量、更高效的代码完成业务功能，也就是注重运行效率。而开发环境中我们注重的只是开发效率。</p>
<p>Webpack 4 推出了 mode 的用法，为我们提供了不同模式下的一些预设配置，其中生产模式下就已经包括了很多优化配置。</p>
<h3 data-id="heading-53">不同环境下的配置</h3>
<p>为不同的工作环境创建不同的 Webpack 配置。创建不同环境配置的方式主要有两种：</p>
<ol>
<li>在配置文件中添加相应的判断条件，根据环境不同导出不同配置；</li>
<li>为不同环境单独添加一个配置文件，一个环境对应一个配置文件。</li>
</ol>
<p>们回到配置文件中，Webpack 配置文件还支持导出一个函数，然后在函数中返回所需要的配置对象。这个函数可以接收两个参数，第一个是 env，是我们通过 CLI 传递的环境名参数，第二个是 argv，是运行 CLI 过程中的所有参数。具体代码如下：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">// ./webpack.config.js</span>
<span class="hljs-built_in">module</span>.exports = <span class="hljs-function">(<span class="hljs-params">env, argv</span>) =></span> &#123;
  <span class="hljs-keyword">return</span> &#123;
    <span class="hljs-comment">// ... webpack 配置</span>
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>那我们就可以借助这个特点，为开发环境和生产环境创建不同配置。我先将不同模式下公共的配置定义为一个 config 对象，通过判断，再为 config 对象添加不同环境下的特殊配置。具体代码如下：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">// ./webpack.config.js</span>
<span class="hljs-built_in">module</span>.exports = <span class="hljs-function">(<span class="hljs-params">env, argv</span>) =></span> &#123;
  <span class="hljs-keyword">const</span> config = &#123;
    <span class="hljs-comment">// ... 不同模式下的公共配置</span>
  &#125;

  <span class="hljs-keyword">if</span> (env === <span class="hljs-string">'development'</span>) &#123;
    <span class="hljs-comment">// 为 config 添加开发模式下的特殊配置</span>
    config.mode = <span class="hljs-string">'development'</span>
    config.devtool = <span class="hljs-string">'cheap-eval-module-source-map'</span>
  &#125; <span class="hljs-keyword">else</span> <span class="hljs-keyword">if</span> (env === <span class="hljs-string">'production'</span>) &#123;
    <span class="hljs-comment">// 为 config 添加生产模式下的特殊配置</span>
    config.mode = <span class="hljs-string">'production'</span>
    config.devtool = <span class="hljs-string">'nosources-source-map'</span>
  &#125;

  <span class="hljs-keyword">return</span> config
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-54">不同环境的配置文件</h3>
<p>通过判断环境名参数返回不同配置对象的方式只适用于中小型项目，因为一旦项目变得复杂，我们的配置也会一起变得复杂起来。所以对于大型的项目来说，还是建议使用不同环境对应不同配置文件的方式来实现。</p>
<p>一般在这种方式下，项目中最少会有三个 webpack 的配置文件。其中两个用来分别适配开发环境和生产环境，另外一个则是公共配置。因为开发环境和生产环境的配置并不是完全不同的，所以需要一个公共文件来抽象两者相同的配置。具体配置文件结构如下：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript">.
├── webpack.common.js ···························· 公共配置
├── webpack.dev.js ······························· 开发模式配置
└── webpack.prod.js ······························ 生产模式配置
<span class="copy-code-btn">复制代码</span></code></pre>
<p>在不同环境的具体配置中我们先导入公共配置对象，然后这里可以使用 Object.assign 方法把公共配置对象复制到具体环境的配置对象中，并且同时去覆盖其中的一些配置。具体如下：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">// ./webpack.common.js</span>
<span class="hljs-built_in">module</span>.exports = &#123;
  <span class="hljs-comment">// ... 公共配置</span>
&#125;
<span class="hljs-comment">// ./webpack.prod.js</span>
<span class="hljs-keyword">const</span> common = <span class="hljs-built_in">require</span>(<span class="hljs-string">'./webpack.common'</span>)
<span class="hljs-built_in">module</span>.exports = <span class="hljs-built_in">Object</span>.assign(common, &#123;
  <span class="hljs-comment">// 生产模式配置</span>
&#125;)
<span class="hljs-comment">// ./webpack.dev.js</span>
<span class="hljs-keyword">const</span> common = <span class="hljs-built_in">require</span>(<span class="hljs-string">'./webpack.common'</span>)
<span class="hljs-built_in">module</span>.exports = <span class="hljs-built_in">Object</span>.assign(common, &#123;
  <span class="hljs-comment">// 开发模式配置</span>
&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>Object.assign 这个方法会完全覆盖掉前一个对象中的同名属性。
这个特点对于普通值类型属性的覆盖都没有什么问题。但是像配置中的 plugins 这种数组，我们只是希望在原有公共配置的插件基础上添加一些插件，那 Object.assign 就做不到了。</p>
<p>可以使用 Lodash 提供的 merge 函数来实现, 社区提供了更为专业的模块 webpack-merge，它专门用来满足我们这里合并 Webpack 配置的需求。</p>
<pre><code class="hljs language-bash copyable" lang="bash">npm i webpack-merge --save-dev 
<span class="hljs-comment"># or yarn add webpack-merge --dev</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>那这个模块导出的就是一个 merge 函数，我们使用这个函数来合并这里的配置与公共的配置。具体代码如下：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">// ./webpack.common.js</span>
<span class="hljs-built_in">module</span>.exports = &#123;
  <span class="hljs-comment">// ... 公共配置</span>
&#125;
<span class="hljs-comment">// ./webpack.prod.js</span>
<span class="hljs-keyword">const</span> merge = <span class="hljs-built_in">require</span>(<span class="hljs-string">'webpack-merge'</span>)
<span class="hljs-keyword">const</span> common = <span class="hljs-built_in">require</span>(<span class="hljs-string">'./webpack.common'</span>)
<span class="hljs-built_in">module</span>.exports = merge(common, &#123;
  <span class="hljs-comment">// 生产模式配置</span>
&#125;)
<span class="hljs-comment">// ./webpack.dev.jss</span>
<span class="hljs-keyword">const</span> merge = <span class="hljs-built_in">require</span>(<span class="hljs-string">'webpack-merge'</span>)
<span class="hljs-keyword">const</span> common = <span class="hljs-built_in">require</span>(<span class="hljs-string">'./webpack.common'</span>)
<span class="hljs-built_in">module</span>.exports = merge(common, &#123;
  <span class="hljs-comment">// 开发模式配置</span>
&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>使用 webpack-merge 过后，我们这里的配置对象就可以跟普通的 webpack 配置一样，需要什么就配置什么，merge 函数内部会自动处理合并的逻辑。</p>
<p>分别配置完成过后，我们再次回到命令行终端，然后尝试运行 webpack 打包。不过因为这里已经没有默认的配置文件了，所以我们需要通过 --config 参数来指定我们所使用的配置文件路径。例如：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript">webpack --config webpack.prod.js
<span class="copy-code-btn">复制代码</span></code></pre>
<p>也可以把这个构建命令定义到 npm scripts 中，方便使用。</p>
<h3 data-id="heading-55">生产模式下的优化插件</h3>
<p>在 Webpack 4 中新增的 production 模式下，内部就自动开启了很多通用的优化功能。对于使用者而言，开箱即用是非常方便的，但是对于学习者而言，这种开箱即用会导致我们忽略掉很多需要了解的东西。以至于出现问题无从下手。</p>
<p>这里我们先一起学习 production 模式下几个主要的优化功能，顺便了解一下 Webpack 如何优化打包结果。</p>
<h4 data-id="heading-56">Define Plugin</h4>
<p>DefinePlugin 是用来为我们代码中注入全局成员的。
在 production 模式下，默认通过这个插件往代码中注入了一个 process.env.NODE_ENV。很多第三方模块都是通过这个成员去判断运行环境，从而决定是否执行例如打印日志之类的操作。</p>
<p>DefinePlugin 是一个内置的插件，所以我们先导入 webpack 模块，然后再到 plugins 中添加这个插件。这个插件的构造函数接收一个对象参数，对象中的成员都可以被注入到代码中。具体代码如下：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">// ./webpack.config.js</span>
<span class="hljs-keyword">const</span> webpack = <span class="hljs-built_in">require</span>(<span class="hljs-string">'webpack'</span>)
<span class="hljs-built_in">module</span>.exports = &#123;
<span class="hljs-regexp">/  /</span><span class="hljs-regexp">/ ... 其他配置
  plugins: [
    new webpack.DefinePlugin(&#123;
      API_BASE_URL: 'https://api.example.com'
    &#125;)
  ]
&#125;
</span><span class="copy-code-btn">复制代码</span></code></pre>
<p>通过 DefinePlugin 定义一个 API_BASE_URL，用来为我们的代码注入 API 服务地址，它的值是一个字符串。</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">// ./src/main.js</span>
<span class="hljs-built_in">console</span>.log(API_BASE_URL)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>完成以后我们打开控制台，然后运行 webpack 打包。打包完成过后我们找到打包的结果，然后找到 main.js 对应的模块。具体结果如下：
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/3b8095059c0d441bb3230c6be9e6d7ca~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer">
这里我们发现 DefinePlugin 其实就是把我们配置的字符串内容直接替换到了代码中，而目前这个字符串的内容为 <a href="https://link.juejin.cn/?target=https%3A%2F%2Fapi.example.com" target="_blank" rel="nofollow noopener noreferrer" title="https://api.example.com" ref="nofollow noopener noreferrer">api.example.com</a>，字符串中并没有包含引号，所以替换进来语法自然有问题。</p>
<p>正确的做法是传入一个字符串字面量语句。具体实现如下：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">// ./webpack.config.js</span>
<span class="hljs-keyword">const</span> webpack = <span class="hljs-built_in">require</span>(<span class="hljs-string">'webpack'</span>)
<span class="hljs-built_in">module</span>.exports = &#123;
  <span class="hljs-comment">// ... 其他配置</span>
  <span class="hljs-attr">plugins</span>: [
    <span class="hljs-keyword">new</span> webpack.DefinePlugin(&#123;
      <span class="hljs-comment">// 值要求的是一个代码片段</span>
      <span class="hljs-attr">API_BASE_URL</span>: <span class="hljs-string">'"https://api.example.com"'</span>
    &#125;)
  ]
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/9d758ecb32654ff789490e22b1022115~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer">
如果我们需要注入的是一个值，就可以通过 JSON.stringify 的方式来得到表示这个值的字面量。这样就不容易出错了。具体实现如下：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">// ./webpack.config.js</span>
<span class="hljs-keyword">const</span> webpack = <span class="hljs-built_in">require</span>(<span class="hljs-string">'webpack'</span>)
<span class="hljs-built_in">module</span>.exports = &#123;
  <span class="hljs-comment">// ... 其他配置</span>
  <span class="hljs-attr">plugins</span>: [
    <span class="hljs-keyword">new</span> webpack.DefinePlugin(&#123;
      <span class="hljs-comment">// 值要求的是一个代码片段</span>
      <span class="hljs-attr">API_BASE_URL</span>: <span class="hljs-built_in">JSON</span>.stringify(<span class="hljs-string">'https://api.example.com'</span>)
    &#125;)
  ]
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-57">Mini CSS Extract Plugin</h4>
<p>对于 CSS 文件的打包，一般我们会使用 style-loader 进行处理，这种处理方式最终的打包结果就是 CSS 代码会内嵌到 JS 代码中。</p>
<p>mini-css-extract-plugin 是一个可以将 CSS 代码从打包结果中提取出来的插件，它的使用非常简单，同样也需要先通过 npm 安装一下这个插件。具体命令如下：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript">npm i mini-css-extract-plugin --save-dev
<span class="copy-code-btn">复制代码</span></code></pre>
<p>Webpack 的配置文件。具体配置如下：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">// ./webpack.config.js</span>
<span class="hljs-keyword">const</span> MiniCssExtractPlugin = <span class="hljs-built_in">require</span>(<span class="hljs-string">'mini-css-extract-plugin'</span>)
<span class="hljs-built_in">module</span>.exports = &#123;
  <span class="hljs-attr">mode</span>: <span class="hljs-string">'none'</span>,
  <span class="hljs-attr">entry</span>: &#123;
    <span class="hljs-attr">main</span>: <span class="hljs-string">'./src/index.js'</span>
  &#125;,
  <span class="hljs-attr">output</span>: &#123;
    <span class="hljs-attr">filename</span>: <span class="hljs-string">'[name].bundle.js'</span>
  &#125;,
  <span class="hljs-attr">module</span>: &#123;
    <span class="hljs-attr">rules</span>: [
      &#123;
        <span class="hljs-attr">test</span>: <span class="hljs-regexp">/\.css$/</span>,
        use: [
          <span class="hljs-comment">// 'style-loader', // 将样式通过 style 标签注入</span>
          MiniCssExtractPlugin.loader,
          <span class="hljs-string">'css-loader'</span>
        ]
      &#125;
    ]
  &#125;,
  <span class="hljs-attr">plugins</span>: [
    <span class="hljs-keyword">new</span> MiniCssExtractPlugin()
  ]
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<ol>
<li>将这个插件添加到配置对象的 plugins 数组中了。这样 Mini CSS Extract Plugin 在工作时就会自动提取代码中的 CSS 了。</li>
<li>Mini CSS Extract Plugin 还需要我们使用 MiniCssExtractPlugin 中提供的 loader 去替换掉 style-loader，以此来捕获到所有的样式。</li>
</ol>
<p>打包过后，样式就会存放在独立的文件中，直接通过 link 标签引入页面
如果你的 CSS 体积不是很大的话，提取到单个文件中，效果可能适得其反，因为单独的文件就需要单独请求一次。个人经验是如果 CSS 超过 200KB 才需要考虑是否提取出来，作为单独的文件。</p>
<h4 data-id="heading-58">Optimize CSS Assets Webpack Plugin</h4>
<p>使用了 Mini CSS Extract Plugin 过后，样式就被提取到单独的 CSS 文件中了。但是js文件被压缩了, css文件没有被压缩</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/61a51eff6c694398ba879b76885d5780~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer">
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/c4cfbb5401d2471bb14d7d76debabdc0~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>生产模式下会自动压缩输出的结果，我们可以打开打包生成的 JS 文件。
Webpack 内置的压缩插件仅仅是针对 JS 文件的压缩，其他资源文件的压缩都需要额外的插件。</p>
<p>Webpack 官方推荐了一个 Optimize CSS Assets Webpack Plugin 插件。我们可以使用这个插件来压缩我们的样式文件。</p>
<pre><code class="hljs language-bash copyable" lang="bash">npm i optimize-css-assets-webpack-plugin --save-dev
<span class="copy-code-btn">复制代码</span></code></pre>
<p>具体配置代码如下:</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">// ./webpack.config.js</span>
<span class="hljs-keyword">const</span> MiniCssExtractPlugin = <span class="hljs-built_in">require</span>(<span class="hljs-string">'mini-css-extract-plugin'</span>)
<span class="hljs-keyword">const</span> OptimizeCssAssetsWebpackPlugin = <span class="hljs-built_in">require</span>(<span class="hljs-string">'optimize-css-assets-webpack-plugin'</span>)
<span class="hljs-built_in">module</span>.exports = &#123;
  <span class="hljs-attr">mode</span>: <span class="hljs-string">'none'</span>,
  <span class="hljs-attr">entry</span>: &#123;
    <span class="hljs-attr">main</span>: <span class="hljs-string">'./src/index.js'</span>
  &#125;,
  <span class="hljs-attr">output</span>: &#123;
    <span class="hljs-attr">filename</span>: <span class="hljs-string">'[name].bundle.js'</span>
  &#125;,
  <span class="hljs-attr">module</span>: &#123;
    <span class="hljs-attr">rules</span>: [
      &#123;
        <span class="hljs-attr">test</span>: <span class="hljs-regexp">/\.css$/</span>,
        use: [
          MiniCssExtractPlugin.loader,
          <span class="hljs-string">'css-loader'</span>
        ]
      &#125;
    ]
  &#125;,
  <span class="hljs-attr">plugins</span>: [
    <span class="hljs-keyword">new</span> MiniCssExtractPlugin(),
    <span class="hljs-keyword">new</span> OptimizeCssAssetsWebpackPlugin()
  ]
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这个插件的官方文档中发现，文档中的这个插件并不是配置在 plugins 数组中的，而是添加到了 optimization 对象中的 minimizer 属性中。具体如下：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">// ./webpack.config.js</span>
<span class="hljs-keyword">const</span> MiniCssExtractPlugin = <span class="hljs-built_in">require</span>(<span class="hljs-string">'mini-css-extract-plugin'</span>)
<span class="hljs-keyword">const</span> OptimizeCssAssetsWebpackPlugin = <span class="hljs-built_in">require</span>(<span class="hljs-string">'optimize-css-assets-webpack-plugin'</span>)
<span class="hljs-built_in">module</span>.exports = &#123;
  <span class="hljs-attr">mode</span>: <span class="hljs-string">'none'</span>,
  <span class="hljs-attr">entry</span>: &#123;
    <span class="hljs-attr">main</span>: <span class="hljs-string">'./src/index.js'</span>
  &#125;,
  <span class="hljs-attr">output</span>: &#123;
    <span class="hljs-attr">filename</span>: <span class="hljs-string">'[name].bundle.js'</span>
  &#125;,
  <span class="hljs-attr">optimization</span>: &#123;
    <span class="hljs-attr">minimizer</span>: [
      <span class="hljs-keyword">new</span> OptimizeCssAssetsWebpackPlugin()
    ]
  &#125;,
  <span class="hljs-attr">module</span>: &#123;
    <span class="hljs-attr">rules</span>: [
      &#123;
        <span class="hljs-attr">test</span>: <span class="hljs-regexp">/\.css$/</span>,
        use: [
          MiniCssExtractPlugin.loader,
          <span class="hljs-string">'css-loader'</span>
        ]
      &#125;
    ]
  &#125;,
  <span class="hljs-attr">plugins</span>: [
    <span class="hljs-keyword">new</span> MiniCssExtractPlugin()
  ]
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>optimize-css-assets-webpack-plugin配置到 plugins 属性中，那么这个插件在任何情况下都会工作。而配置到 minimizer 中，就只会在 minimize 特性开启时才工作。</p>
<p>所以 Webpack 建议像这种压缩插件，应该我们配置到 minimizer 中，便于 minimize 选项的统一控制。</p>
<p>但是这么配置也有个缺点，此时我们再次运行生产模式打包，打包完成后再来看一眼输出的 JS 文件，此时你会发现，原本可以自动压缩的 JS，现在却不能压缩了。具体 JS 的输出结果如下：
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/e14e402d3b1d488bb36a2e3f2a22a898~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer">
那这是因为我们设置了 minimizer，Webpack 认为我们需要使用自定义压缩器插件，那内部的 JS 压缩器就会被覆盖掉。我们必须手动再添加回来。</p>
<p>内置的 JS 压缩插件叫作 terser-webpack-plugin</p>
<pre><code class="hljs language-bash copyable" lang="bash">npm i terser-webpack-plugin --save-dev
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">// ./webpack.config.js</span>
<span class="hljs-keyword">const</span> MiniCssExtractPlugin = <span class="hljs-built_in">require</span>(<span class="hljs-string">'mini-css-extract-plugin'</span>)
<span class="hljs-keyword">const</span> OptimizeCssAssetsWebpackPlugin = <span class="hljs-built_in">require</span>(<span class="hljs-string">'optimize-css-assets-webpack-plugin'</span>)
<span class="hljs-keyword">const</span> TerserWebpackPlugin = <span class="hljs-built_in">require</span>(<span class="hljs-string">'terser-webpack-plugin'</span>)
<span class="hljs-built_in">module</span>.exports = &#123;
  <span class="hljs-attr">mode</span>: <span class="hljs-string">'none'</span>,
  <span class="hljs-attr">entry</span>: &#123;
    <span class="hljs-attr">main</span>: <span class="hljs-string">'./src/index.js'</span>
  &#125;,
  <span class="hljs-attr">output</span>: &#123;
    <span class="hljs-attr">filename</span>: <span class="hljs-string">'[name].bundle.js'</span>
  &#125;,
  <span class="hljs-attr">optimization</span>: &#123;
    <span class="hljs-attr">minimizer</span>: [
      <span class="hljs-keyword">new</span> TerserWebpackPlugin(),
      <span class="hljs-keyword">new</span> OptimizeCssAssetsWebpackPlugin()
    ]
  &#125;,
  <span class="hljs-attr">module</span>: &#123;
    <span class="hljs-attr">rules</span>: [
      &#123;
        <span class="hljs-attr">test</span>: <span class="hljs-regexp">/\.css$/</span>,
        use: [
          MiniCssExtractPlugin.loader,
          <span class="hljs-string">'css-loader'</span>
        ]
      &#125;
    ]
  &#125;,
  <span class="hljs-attr">plugins</span>: [
    <span class="hljs-keyword">new</span> MiniCssExtractPlugin()
  ]
&#125;
<span class="copy-code-btn">复制代码</span></code></pre></div>  
</div>
            