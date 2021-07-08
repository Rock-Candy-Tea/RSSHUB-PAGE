
---
title: 'vue-cli cdn 方式引入 Vue 模块'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=767'
author: 掘金
comments: false
date: Thu, 08 Jul 2021 01:48:56 GMT
thumbnail: 'https://picsum.photos/400/300?random=767'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h2 data-id="heading-0">前言</h2>
<p>如果你只是想快速配置 cdn，可以直接看快速配置篇。</p>
<blockquote>
<p><strong>Chrome 将于不久后默认开启 <a href="https://link.juejin.cn/?target=https%3A%2F%2Fchromestatus.com%2Ffeature%2F5436853517811712" target="_blank" rel="nofollow noopener noreferrer" title="https://chromestatus.com/feature/5436853517811712" ref="nofollow noopener noreferrer">限制子资源在私有网络的分发</a> 策略，它会导致非 https 协议无法使用第三方外链，这将导致开发环境无法使用 cdn。</strong>
这个安全策略开启后，你可能会在未来遇到这个错误：
我当前是 Chrome 91，可以在 Chrome 浏览器的地址栏中输入 chrome://flags/#block-insecure-private-network-requests 来找到这个策略，在未来的版本它会被默认开启，如果你现在主动启用该策略，那么开发环境使用 cdn 你将遇到一个错误：<code>The request client is not a secure context and the resource is in more-private address space \</code>local`.`
<strong>综上，该博客于 2021-07-08 日做了非常大的改动。本来 Vue 也出 3 了，这篇模块也没还没讨论 Vue3 的 cdn 引入方式。</strong></p>
</blockquote>
<h2 data-id="heading-1">选择 Vue 的 cdn</h2>
<p>引入的 <strong>vue</strong> 文件必须是游览器版本，最少需要 ==运行时源码==，根据你的 Vue 版本不同，选择的文件也不同：</p>
<ul>
<li>Vue2 版本的用户选择： <strong>vue.runtime.min.js</strong>；</li>
<li>Vue3 版本的用户选择： <strong>vue.runtime.global.prod.js</strong>。</li>
</ul>
<blockquote>
<p><strong>运行时源码和完整版有什么不同？</strong>
运行时源码少了编译器，而完整版有，因为 vue-loader 已经编译了 <code>template</code>，所以不需要再次编译。这意味着运行时源码还要小一点，详见<a href="https://link.juejin.cn/?target=https%3A%2F%2Fcn.vuejs.org%2Fv2%2Fguide%2Finstallation.html%23%25E5%25AF%25B9%25E4%25B8%258D%25E5%2590%258C%25E6%259E%2584%25E5%25BB%25BA%25E7%2589%2588%25E6%259C%25AC%25E7%259A%2584%25E8%25A7%25A3%25E9%2587%258A" target="_blank" rel="nofollow noopener noreferrer" title="https://cn.vuejs.org/v2/guide/installation.html#%E5%AF%B9%E4%B8%8D%E5%90%8C%E6%9E%84%E5%BB%BA%E7%89%88%E6%9C%AC%E7%9A%84%E8%A7%A3%E9%87%8A" ref="nofollow noopener noreferrer">vue2 官方文档</a> 或者 <a href="https://link.juejin.cn/?target=https%3A%2F%2Fv3.cn.vuejs.org%2Fguide%2Finstallation.html%23%25E5%25AF%25B9%25E4%25B8%258D%25E5%2590%258C%25E6%259E%2584%25E5%25BB%25BA%25E7%2589%2588%25E6%259C%25AC%25E7%259A%2584%25E8%25A7%25A3%25E9%2587%258A" target="_blank" rel="nofollow noopener noreferrer" title="https://v3.cn.vuejs.org/guide/installation.html#%E5%AF%B9%E4%B8%8D%E5%90%8C%E6%9E%84%E5%BB%BA%E7%89%88%E6%9C%AC%E7%9A%84%E8%A7%A3%E9%87%8A" ref="nofollow noopener noreferrer">vue3 官方文档</a>。</p>
</blockquote>
<p>我使用的是 <a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.bootcdn.cn" target="_blank" rel="nofollow noopener noreferrer" title="https://www.bootcdn.cn" ref="nofollow noopener noreferrer">bootcdn</a> 的运行时压缩模块，体积会更小。<strong>切记，使用的 cdn 需要和你的 package.json 中依赖包的版本号相同，以免产生版本 bug。</strong></p>
<h2 data-id="heading-2">如何引入 cdn ？</h2>
<p>因为开发环境不能安全使用第三方外链，所以第三方 cdn 只能在生产环境中使用。</p>
<p>具体引入方式是在 <code>vue.config.js</code> 中注册 cdn 的模板变量，然后在 <code>public/index.html</code> 中插入。<strong>一手准备，一手插入。</strong></p>
<h3 data-id="heading-3">一手插入</h3>
<p>使用 <strong>vue-cli</strong> 构建的项目，可以在 <strong>项目/public/index.html</strong> 的 head 元素中 ==插入准备好的 cdn 模板==。</p>
<p>我的代码如下：</p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">head</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">meta</span> <span class="hljs-attr">charset</span>=<span class="hljs-string">"utf-8"</span> /></span>
  <span class="hljs-tag"><<span class="hljs-name">meta</span> <span class="hljs-attr">http-equiv</span>=<span class="hljs-string">"X-UA-Compatible"</span> <span class="hljs-attr">content</span>=<span class="hljs-string">"IE=edge"</span> /></span>
  <span class="hljs-tag"><<span class="hljs-name">meta</span> <span class="hljs-attr">name</span>=<span class="hljs-string">"viewport"</span> <span class="hljs-attr">content</span>=<span class="hljs-string">"width=device-width,initial-scale=1.0"</span> /></span>
  <span class="hljs-tag"><<span class="hljs-name">link</span> <span class="hljs-attr">rel</span>=<span class="hljs-string">"icon"</span> <span class="hljs-attr">href</span>=<span class="hljs-string">"<%= BASE_URL %>favicon.ico"</span> /></span>
  <span class="hljs-tag"><<span class="hljs-name">title</span>></span>vue-app<span class="hljs-tag"></<span class="hljs-name">title</span>></span>

  <span class="hljs-comment"><!-- 这里是插入的 CDN 位置，编写下面这行代码即可。 --></span>
  <%= htmlWebpackPlugin.options.cdns %>
<span class="hljs-tag"></<span class="hljs-name">head</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这里使用了 <a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fjantimon%2Fhtml-webpack-plugin" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/jantimon/html-webpack-plugin" ref="nofollow noopener noreferrer">html-webpack-plugin</a> 插件的模板参数，你可以通过此插件准备一些参数插入到这个模板中。</p>
<p>可以看到，我们插入了 <code><%= htmlWebpackPlugin.options.cdns %></code> 参数，这就是我们需要准备的 cdn 模板。</p>
<blockquote>
<p>诸如 <code><%= %></code> 这类语法是 <a href="https://link.juejin.cn/?target=https%3A%2F%2Fejs.co%2F" target="_blank" rel="nofollow noopener noreferrer" title="https://ejs.co/" ref="nofollow noopener noreferrer">EJS</a> 模板语法，想要详细了解可以看看它的 <a href="https://link.juejin.cn/?target=https%3A%2F%2Fejs.bootcss.com%2F" target="_blank" rel="nofollow noopener noreferrer" title="https://ejs.bootcss.com/" ref="nofollow noopener noreferrer">中文文档</a>。</p>
</blockquote>
<h3 data-id="heading-4">一手准备</h3>
<p>来到 <code>项目/vue.config.js</code> 文件，如果没有就创建。</p>
<p>准备分两步：</p>
<ul>
<li>
<p><strong>设置外部依赖</strong>：在打包时忽略已经用 cdn 引入的模块。</p>
</li>
<li>
<p><strong>添加模板参数</strong>：准备插入的 cdn 资源元素。</p>
</li>
</ul>
<p>以下代码中，Moment.js 和 Vue3 就是用了 cdn 来引入，并且在打包时忽略这两个模块：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">/** <span class="hljs-doctag">@file </span>vue.config.js */</span>

<span class="hljs-built_in">module</span>.exports = &#123;
  <span class="hljs-attr">chainWebpack</span>: <span class="hljs-function">(<span class="hljs-params">config</span>) =></span> &#123;
    <span class="hljs-comment">// 只在生产环境使用 cdn</span>
    <span class="hljs-keyword">if</span> (process.env.NODE_ENV === <span class="hljs-string">"production"</span>) &#123;
      <span class="hljs-comment">// 忽略 vue 和 moment 这两个模块</span>
      config.externals(&#123;
        <span class="hljs-attr">vue</span>: <span class="hljs-string">"Vue"</span>,
        <span class="hljs-attr">moment</span>: <span class="hljs-string">"moment"</span>,
      &#125;);

      <span class="hljs-comment">// 修改 HtmlWebpackPlugin 插件参数，植入 cdns 这个模板参数，值为 Vue3 和 Moment.js 的 cdn 链接</span>
      config.plugin(<span class="hljs-string">"html"</span>).tap(<span class="hljs-function">(<span class="hljs-params">args</span>) =></span> &#123;
        args[<span class="hljs-number">0</span>].cdns = <span class="hljs-string">`
<script src="https://cdn.bootcdn.net/ajax/libs/vue/3.1.2/vue.runtime.global.prod.min.js" crossorigin="anonymous"></script>
<script src="https://cdn.bootcdn.net/ajax/libs/moment.js/2.29.1/moment.min.js" crossorigin="anonymous"></script>
`</span>;
        <span class="hljs-keyword">return</span> args;
      &#125;);
    &#125;
  &#125;,
&#125;;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>其中：</p>
<ul>
<li>
<p><code>config.externals</code> 用于配置 <a href="https://link.juejin.cn/?target=https%3A%2F%2Fwebpack.docschina.org%2Fconfiguration%2Fexternals%2F%23externals" target="_blank" rel="nofollow noopener noreferrer" title="https://webpack.docschina.org/configuration/externals/#externals" ref="nofollow noopener noreferrer">外部扩展</a>，其作用是不打包使用外部引入的扩展，也就是 build 的时候不打包这也模块。</p>
<ul>
<li>
<p><strong>键名：键名为使用外部扩展的模块。</strong> 比如 <code>import VueLib123 from "vue"</code> 这句话，模块 <code>"Vue"</code> 是不变的，这个就是键名。</p>
</li>
<li>
<p><strong>值：值就是使用 cdn 后，这个模块在全局上的引用。</strong> 比如 Vue 使用 cdn 引入后，全局上使用 <code>Vue</code> 变量来访问，那么外部扩展的值就是 Vue。</p>
</li>
</ul>
</li>
<li>
<p><code>config.plugin("html").tap</code> 用于修改 <a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.webpackjs.com%2Fplugins%2Fhtml-webpack-plugin%2F" target="_blank" rel="nofollow noopener noreferrer" title="https://www.webpackjs.com/plugins/html-webpack-plugin/" ref="nofollow noopener noreferrer">HtmlWebpackPlugin</a> 这个插件的参数，这里插入一个 <code>cdns</code> 参数，所以在 <code>public/index.html</code> 中可以使用 <code><%= htmlWebpackPlugin.options.cdns %></code> 来访问这个参数。</p>
</li>
</ul>
<blockquote>
<ul>
<li>上述代码使用的 Webpack 配置方式是 <a href="https://link.juejin.cn/?target=https%3A%2F%2Fcli.vuejs.org%2Fzh%2Fguide%2Fwebpack.html%23%25E9%2593%25BE%25E5%25BC%258F%25E6%2593%258D%25E4%25BD%259C-%25E9%25AB%2598%25E7%25BA%25A7" target="_blank" rel="nofollow noopener noreferrer" title="https://cli.vuejs.org/zh/guide/webpack.html#%E9%93%BE%E5%BC%8F%E6%93%8D%E4%BD%9C-%E9%AB%98%E7%BA%A7" ref="nofollow noopener noreferrer">链式调用</a>，因为涉及修改插件参数，无法使用 <a href="https://link.juejin.cn/?target=https%3A%2F%2Fcli.vuejs.org%2Fzh%2Fguide%2Fwebpack.html%23%25E7%25AE%2580%25E5%258D%2595%25E7%259A%2584%25E9%2585%258D%25E7%25BD%25AE%25E6%2596%25B9%25E5%25BC%258F" target="_blank" rel="nofollow noopener noreferrer" title="https://cli.vuejs.org/zh/guide/webpack.html#%E7%AE%80%E5%8D%95%E7%9A%84%E9%85%8D%E7%BD%AE%E6%96%B9%E5%BC%8F" ref="nofollow noopener noreferrer">简单配置</a>。</li>
<li>我在 script 元素中设置了 <strong>crossorigin</strong> 属性，取消了用户凭证传递，详见 <a href="https://link.juejin.cn/?target=https%3A%2F%2Fdeveloper.mozilla.org%2Fzh-CN%2Fdocs%2FWeb%2FHTML%2FCORS_settings_attributes" target="_blank" rel="nofollow noopener noreferrer" title="https://developer.mozilla.org/zh-CN/docs/Web/HTML/CORS_settings_attributes" ref="nofollow noopener noreferrer">CORS settings attributes</a> 。</li>
<li>如果你想更安全的使用第三方 cdn ，那么推荐你使用 <a href="https://link.juejin.cn/?target=https%3A%2F%2Fdeveloper.mozilla.org%2Fzh-CN%2Fdocs%2FWeb%2FSecurity%2FSubresource_Integrity" target="_blank" rel="nofollow noopener noreferrer" title="https://developer.mozilla.org/zh-CN/docs/Web/Security/Subresource_Integrity" ref="nofollow noopener noreferrer">SRI</a>。</li>
</ul>
</blockquote>
<h2 data-id="heading-5">小结 + 打包测试</h2>
<p><strong>注意：源代码只是改了 “项目/public/index.html” 文件和配置了 vue.config.js，没有修改其他代码。此方法并不会在开发环境中使用 cdn，具体原因参考第一节前言。</strong></p>
<p>测试代码的 <code>package.json</code> 依赖为：</p>
<pre><code class="hljs language-json copyable" lang="json">&#123;
  <span class="hljs-attr">"dependencies"</span>: &#123;
    <span class="hljs-attr">"core-js"</span>: <span class="hljs-string">"^3.6.5"</span>,
    <span class="hljs-attr">"moment"</span>: <span class="hljs-string">"^2.29.1"</span>,
    <span class="hljs-attr">"vue"</span>: <span class="hljs-string">"^3.0.0"</span>
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>其中 <code>moment</code> 和 <code>vue</code> 使用了 cdn 引入。</p>
<p><strong>不使用 cdn 的打包情况</strong>（注释掉 vue.config.js 添加的代码就可测试）：</p>
<pre><code class="hljs language-bash copyable" lang="bash">warning

webpack performance recommendations:
You can <span class="hljs-built_in">limit</span> the size of your bundles by using import() or require.ensure to lazy load some parts of your application.
For more info visit https://webpack.js.org/guides/code-splitting/

  File                                 Size                                            Gzipped

  dist\js\chunk-vendors.50f67bb1.js    379.14 KiB                                      110.63 KiB
  dist\js\app.d4b48aed.js              6.54 KiB                                        2.45 KiB

  Images and other types of assets omitted.

 DONE  Build complete. The dist directory is ready to be deployed.
 INFO  Check out deployment instructions at https://cli.vuejs.org/guide/deployment.html

Done <span class="hljs-keyword">in</span> 5.03s.
<span class="copy-code-btn">复制代码</span></code></pre>
<p>上来直接报一个包太大警告，这项目还什么都没写，就是在 <code>App.vue</code> 里面引入了 Moment.js。</p>
<p>其中 <code>chunk-vendors</code> 为 379.14 KB，包含了 <code>core-js</code>、<code>moment</code> 和 <code>vue</code> 三个模块。</p>
<p><strong>使用 cdn 的打包情况：</strong></p>
<pre><code class="hljs language-bash copyable" lang="bash"> DONE  Compiled successfully <span class="hljs-keyword">in</span> 720ms                                                                                         下午2:52:47
  File                                 Size                                            Gzipped

  dist\js\chunk-vendors.20dbb2c7.js    24.82 KiB                                       9.06 KiB
  dist\js\app.08fbc8da.js              2.02 KiB                                        0.99 KiB

  Images and other types of assets omitted.

 DONE  Build complete. The dist directory is ready to be deployed.
 INFO  Check out deployment instructions at https://cli.vuejs.org/guide/deployment.html

Done <span class="hljs-keyword">in</span> 3.49s.
<span class="copy-code-btn">复制代码</span></code></pre>
<p>此时 <strong>chunk-venders 降到 24KB</strong>，只剩一些关于 <code>core-js</code> 的依赖了。</p>
<p><strong>小结：</strong></p>
<p>这种打包方式只是阐述基本实现方式，如果你觉得比较麻烦，可以看最后一节快速配置篇。</p>
<p>如果想继续优化打包，建议了解异步路由，异步加载等，谨慎使用 <code>require.context</code>。</p>
<h2 data-id="heading-6">快速配置篇</h2>
<p>我自己也没那么多时间每次去查怎么配置，所以直接封装了一个函数。</p>
<ul>
<li>首先，在 <code>public/index.html</code> 的 <code>head</code> 元素里面添加下面这行代码用来插入 cdn。</li>
</ul>
<pre><code class="hljs language-ejs copyable" lang="ejs"><%= htmlWebpackPlugin.options.cdns %>
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>接着新建一个文件 <code>useCDNs.js</code> 在任意位置，我放到了 <code>根路径/webpack/useCDNs.js</code> 中。新建后复制以下代码粘贴进去即可，注释不想要可以删掉。</li>
</ul>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">/** <span class="hljs-doctag">@file </span>useCDNs.js */</span>

<span class="hljs-comment">/** <span class="hljs-doctag">@typedef <span class="hljs-type">&#123;string&#125;</span> </span>ModuleName 模块名   */</span>
<span class="hljs-comment">/** <span class="hljs-doctag">@typedef <span class="hljs-type">&#123;string&#125;</span> </span>ModuleRefer 模块在全局的引用   */</span>
<span class="hljs-comment">/** <span class="hljs-doctag">@typedef <span class="hljs-type">&#123;string&#125;</span> </span>ElementTem 元素模板   */</span>
<span class="hljs-comment">/** <span class="hljs-doctag">@typedef <span class="hljs-type">&#123;&#123;mod:ModuleName;refer:ModuleRefer;el:ElementTem&#125;</span></span>&#125; CDNItem  cdn 项目 */</span>

<span class="hljs-comment">/**
 * cdn 使用函数。
 *
 * 此函数可以在指定开发环境中，指定某些模块作为外部依赖出现，并把准备好的第三方 cdn 模板以 `cdns` 参数通过 HtmlWebpackPlugin 插件插入到 `public/index.html` 文件中。
 * 你可以在 `public/index.html` 中使用 ejs 语法 <%= htmlWebpackPlugin.options.cdns %> 来插入准备好的 cdn。
 *
 * <span class="hljs-doctag">@param <span class="hljs-type">&#123;import('webpack-chain')&#125;</span> </span>config webpack-chain 实例
 * <span class="hljs-doctag">@param <span class="hljs-type">&#123;CDNItem[]&#125;</span> </span>cdns 传入需要使用的 cdn 数组
 * <span class="hljs-doctag">@param <span class="hljs-type">&#123;string&#125;</span> </span>env 什么环境下使用 cdn ，默认生产环境
 */</span>
<span class="hljs-built_in">module</span>.exports = <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">useCDNs</span>(<span class="hljs-params">config, cdns = [], env = <span class="hljs-string">"production"</span></span>) </span>&#123;
  <span class="hljs-keyword">if</span> (process.env.NODE_ENV !== env) <span class="hljs-keyword">return</span>;

  config.externals(
    cdns.reduce(<span class="hljs-function">(<span class="hljs-params">prev, v</span>) =></span> &#123;
      prev[v.mod] = v.refer;
      <span class="hljs-keyword">return</span> prev;
    &#125;, &#123;&#125;)
  );

  config.plugin(<span class="hljs-string">"html"</span>).tap(<span class="hljs-function">(<span class="hljs-params">args</span>) =></span> &#123;
    args[<span class="hljs-number">0</span>].cdns = cdns.map(<span class="hljs-function">(<span class="hljs-params">v</span>) =></span> v.el).join(<span class="hljs-string">""</span>);
    <span class="hljs-keyword">return</span> args;
  &#125;);
&#125;;
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>最后在 <code>vue.config.js</code> 中使用如下方式调用：</li>
</ul>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">/** <span class="hljs-doctag">@file </span>vue.config.js */</span>

<span class="hljs-keyword">const</span> useCDNs = <span class="hljs-built_in">require</span>(<span class="hljs-string">"./webpack/useCDNs"</span>);

<span class="hljs-built_in">module</span>.exports = &#123;
  <span class="hljs-attr">chainWebpack</span>: <span class="hljs-function">(<span class="hljs-params">config</span>) =></span> &#123;
    useCDNs(config, [
      &#123;
        <span class="hljs-attr">mod</span>: <span class="hljs-string">"vue"</span>,
        <span class="hljs-attr">refer</span>: <span class="hljs-string">"Vue"</span>,
        <span class="hljs-attr">el</span>: <span class="hljs-string">`<script src="https://cdn.bootcdn.net/ajax/libs/vue/3.1.2/vue.runtime.global.prod.min.js"></script>`</span>,
      &#125;,
      &#123;
        <span class="hljs-attr">mod</span>: <span class="hljs-string">"moment"</span>,
        <span class="hljs-attr">refer</span>: <span class="hljs-string">"moment"</span>,
        <span class="hljs-attr">el</span>: <span class="hljs-string">`<script src="https://cdn.bootcdn.net/ajax/libs/moment.js/2.29.1/moment.min.js" crossorigin="anonymous"></script>`</span>,
      &#125;,
    ]);
  &#125;,
&#125;;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>其中，<code>mod</code> 和 <code>refer</code> 对应了外部扩展的模块名和引用名，<code>el</code> 为 cdn 元素。</p>
<p>关于 <code>useCDNs</code> 详细使用参考原文件，注释已经写满了。</p>
<h2 data-id="heading-7">FAQ</h2>
<h3 data-id="heading-8">是否需要删除 import Vue 语句？</h3>
<p>==不用删除，也不能删除。==</p>
<p>因为本文方法只是配置了生成环境使用 cdn，开发环境使用的还是 <code>node_moduels</code> 中的本地包，删了开发环境就 GG。</p>
<h3 data-id="heading-9">cdn 哪里找？</h3>
<p>以前我使用的是 <a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.bootcdn.cn" target="_blank" rel="nofollow noopener noreferrer" title="https://www.bootcdn.cn" ref="nofollow noopener noreferrer">bootcdn</a>，但这家前年过年前后崩过一次，后来没怎么使用。</p>
<p>你可以使用 <a href="https://link.juejin.cn/?target=https%3A%2F%2Funpkg.com%2F" target="_blank" rel="nofollow noopener noreferrer" title="https://unpkg.com/" ref="nofollow noopener noreferrer">UNPKG</a>，这个是和 npm 库直接关联的。</p>
<p>或者 <a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.jsdelivr.com%2F" target="_blank" rel="nofollow noopener noreferrer" title="https://www.jsdelivr.com/" ref="nofollow noopener noreferrer">JSDELIVR</a>，老牌 cdn 有保障，还支持 <a href="https://link.juejin.cn/?target=https%3A%2F%2Fdeveloper.mozilla.org%2Fzh-CN%2Fdocs%2FWeb%2FSecurity%2FSubresource_Integrity" target="_blank" rel="nofollow noopener noreferrer" title="https://developer.mozilla.org/zh-CN/docs/Web/Security/Subresource_Integrity" ref="nofollow noopener noreferrer">SRI</a>。</p>
<h3 data-id="heading-10">兼容性</h3>
<p>vue-cli3 和 vue-cli4 都兼容这种配置方式。</p></div>  
</div>
            