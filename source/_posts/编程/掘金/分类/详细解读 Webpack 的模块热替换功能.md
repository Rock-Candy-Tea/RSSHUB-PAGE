
---
title: '详细解读 Webpack 的模块热替换功能'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/47c1697861954aa08bd5c9d3898b068b~tplv-k3u1fbpfcp-zoom-1.image'
author: 掘金
comments: false
date: Thu, 01 Apr 2021 08:51:01 GMT
thumbnail: 'https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/47c1697861954aa08bd5c9d3898b068b~tplv-k3u1fbpfcp-zoom-1.image'
---

<div>   
<div class="markdown-body"><style>@charset "UTF-8";.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:14px;overflow-x:hidden;color:#353535&#125;.markdown-body h1&#123;padding-bottom:4px;font-size:30px&#125;.markdown-body h1,.markdown-body h2&#123;margin-top:36px;margin-bottom:10px;line-height:1.5;color:#005bb7&#125;.markdown-body h2&#123;position:relative;padding-left:16px;padding-right:10px;padding-bottom:10px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h2:before&#123;content:"「";position:absolute;top:-6px;left:-10px&#125;.markdown-body h2:after&#123;content:"」";position:absolute;top:6px;right:auto&#125;.markdown-body h3&#123;position:relative;padding-bottom:0;margin-top:30px;margin-bottom:10px;font-size:20px;line-height:1.5;color:#005bb7;padding-left:6px&#125;.markdown-body h3:before&#123;content:"»";padding-right:6px;color:#2196f3&#125;.markdown-body h4&#123;margin-top:24px;font-size:16px&#125;.markdown-body h4,.markdown-body h5&#123;padding-bottom:0;margin-bottom:10px;line-height:1.5;color:#005bb7;padding-left:6px&#125;.markdown-body h5&#123;margin-top:18px;font-size:14px&#125;.markdown-body h6&#123;padding-bottom:0;margin-top:12px;margin-bottom:10px;font-size:12px;line-height:1.5;color:#005bb7;padding-left:6px&#125;.markdown-body p&#123;line-height:inherit;margin-top:16px;margin-bottom:16px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;position:relative;width:98%;height:1px;margin-top:32px;margin-bottom:32px;background-image:linear-gradient(90deg,#007fff,rgba(255,0,0,.3),hsla(0,0%,100%,.1),rgba(255,0,0,.3),#007fff);border-width:0;overflow:visible&#125;.markdown-body hr:after&#123;content:"";position:absolute;margin:auto;left:0;right:0;bottom:0;top:0;display:inline-block;width:60px;height:20px;background:#fff;background-image:url(data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACgAAAAgCAYAAABgrToAAAADoklEQVRYR82XTYgcRRTHf2933Q1RjAa9eFO8JHoJ8RQVBQ2iBwXBET0YEUTXNVmNQtTpmeqaWV0XNRq/o4KoECSCEPSg4CF+BYUkIIiCoCJCPIhC/Ihh2Z0nVV27VnZnenumW9i6ddV7//frV69fVQurfMgq56NawFTPAU6QyomqXrw6wIZeyhCPebA5buNR+akKyGoAjd6BshthnYdSjqNcRVuOlIUsD2j0SuA94IwuMHdh5ZUykOUBXfSGbmKI54EtAeYIHSZoy5dl4JxvNYBOKdW1KE8BQ8AkVk6WhasWsAiN0TX9gveXQaPP+Aytpc4u+bMI06JNohsYYYYOR2lJWtS3OKDRfcAtQfgDoI6Vo4UCGb0OmAEuDvZvYmVbEd/igC3dzDz7gQu8sPA9kJDK27mBmjqBeLjTg90PDFOjWawFFQd06kZHEfaj3LAIpTRpSXsZ5E06zEYP9sDimnAApYaV2SLZG/wjMeqAkijwW4xQJ5Gf/ZzRC8OW3hiBTGGlURRswW55Bh/Ssxljrwew8l1PQaM14GngvGDzBUKdDsMeTtgU5o8B92PFlUf3YXUrHa7Fys6lBqcCGnX15YQ2A18FyPd7Crd1A3M8C1wdbH4DD3hWeP6IEXbQkG97ajR1HPFnuPP5jFFq1OWX7hl8WM9l1AO648uNfwLk7tytMeogty+xeQ4rO3r6bdcx1nuwOGsHmaXGtPzae4uzGnLH1kQkvpdZGrHjssBZJrL+pqS05KWc8tgITAPXRzYvYOXe/C2OV43eDcRBDtIhoS2f9wzc0Cv8Wls+zoFzUC5zF0U241h5uZtPfptp6OUM8wbK+cH5GEpCS17P3fJei0Z3+npTxryJ8CPzbKMtn/ZyWbkPGl0PuFPkmkjkcb4h4R2ZLwRq1H0ALmvjkf2HwK1Y+T1PY2XABe/sHJ6MxN5lnoSpnC/UGbsTaI5phK2R7x6s3Ffk5YoDOrWm3onwJHBmEP86bPmBrsGaenNoIdnxCH+gPEhLXi0Cl1VBvyPVLSh7gEuC62yAfOIUqabWEaaiucMIk6RyqJ+Q/QM69V26jjW86Gvov/EaoyT8zRCn+Xq7PVrbx0nuYUaO9wM3WAbjCE1NEUw09Um4UV+2OKfYfu5/S19gsAzGKqm6LE5FrShbdS0ku465DjDwKA/oQht19ejqbaEVuRbiLhuHByYLjtUAZpDutzP7cYdHsPJXWbjyNVgFwQoa1WXwf4Jd9YD/Ap80+yE7+u9aAAAAAElFTkSuQmCC);background-repeat:no-repeat;background-size:auto 100%;background-position-x:center&#125;.markdown-body code&#123;padding:.065em .4em;font-size:.87em;color:#c2185b;word-break:break-word;overflow-x:auto;background-color:#fff4f4;border-radius:2px&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;display:block;padding:16px 12px;margin:0;font-size:12px;color:#333;word-break:normal;overflow-x:auto;background:#f8f8f8&#125;.markdown-body pre>code::-webkit-scrollbar&#123;width:4px;height:4px&#125;.markdown-body pre>code::-webkit-scrollbar-track&#123;background-color:#bedcff&#125;.markdown-body pre>code::-webkit-scrollbar-thumb&#123;background-color:#2196f3;border-radius:10px&#125;.markdown-body a&#123;position:relative;text-decoration:none;color:#3da8f5;border-bottom:1px solid #bedcff&#125;.markdown-body a:hover&#123;color:#007fff;border-bottom-color:#007fff&#125;.markdown-body a:active&#123;color:#007fff&#125;.markdown-body a:after&#123;position:absolute;content:"";top:100%;left:0;width:100%;opacity:0;border-bottom:1px solid #bedcff;transition:top .3s,opacity .3s;transform:translateZ(0)&#125;.markdown-body a:hover:after&#123;top:0;opacity:1;border-bottom-color:#007fff&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #c3e0fd;border-spacing:0;border-collapse:collapse&#125;.markdown-body table thead&#123;color:#000;text-align:left;font-size:14px;background:#f6f6f6&#125;.markdown-body table tr:nth-child(2n)&#123;background-color:#f7fbff&#125;.markdown-body table tr:hover&#123;background-color:#e0edf7&#125;.markdown-body table td,.markdown-body table th&#123;padding:12px 8px;line-height:24px;border:1px solid #c3e0fd&#125;.markdown-body table th&#123;color:#005bb7;background-color:#dff0ff&#125;.markdown-body table td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#8c8c8c;border-left:4px solid #2196f3;background-color:#f0fdff;padding:1px 20px;margin:22px 0&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body b,.markdown-body blockquote>b,.markdown-body blockquote>strong,.markdown-body strong&#123;color:#2196f3&#125;.markdown-body em,.markdown-body i&#123;color:#4fc3f7&#125;.markdown-body del&#123;color:#ccc&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:4px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body details>summary&#123;outline:none;color:#005bb7;font-size:20px;font-weight:bolder;border-bottom:1px solid #bedcff;cursor:pointer&#125;.markdown-body details>p&#123;padding:10px 20px;margin:10px 0 0;color:#666;background-color:#f0fdff;border:2px dashed #2196f3&#125;.markdown-body h1::selection,.markdown-body h2::selection,.markdown-body h3::selection,.markdown-body h4::selection,.markdown-body h5::selection,.markdown-body h6::selection&#123;color:#005bb7;background-color:rgba(160,200,255,.15)&#125;.markdown-body p::selection&#123;color:#c80000&#125;.markdown-body a::selection,.markdown-body b::selection,.markdown-body del::selection,.markdown-body em::selection,.markdown-body i::selection,.markdown-body strong::selection&#123;background-color:transparent&#125;.markdown-body code::selection&#123;background-color:#ffeaeb&#125;.markdown-body pre>code::selection&#123;background-color:rgba(160,200,255,.25)&#125;.markdown-body ol ::selection,.markdown-body ul ::selection&#123;background-color:rgba(160,200,255,.15)&#125;.markdown-body .contains-task-list&#123;padding-left:14px;list-style:none&#125;.markdown-body .contains-task-list input[type=checkbox]&#123;position:relative&#125;.markdown-body .contains-task-list input[type=checkbox]:before&#123;content:"";position:absolute;top:0;left:0;right:0;bottom:0;width:inherit;height:inherit;background:#f0f8ff;border:1px solid #add6ff;border-radius:2px;box-sizing:border-box;z-index:1&#125;.markdown-body .contains-task-list input[type=checkbox]:checked:after&#123;content:"✓";position:absolute;top:-12px;left:0;right:0;bottom:0;width:0;height:0;color:#f55;font-size:20px;font-weight:700;z-index:2&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><blockquote>
<ul>
<li>原文地址：<a href="https://blog.bitsrc.io/webpacks-hot-module-replacement-feature-explained-43c13b169986" target="_blank" rel="nofollow noopener noreferrer">Webpack’s Hot Module Replacement Feature Explained</a></li>
<li>原文作者：<a href="https://medium.com/@nathansebhastian" target="_blank" rel="nofollow noopener noreferrer">Nathan Sebhastian</a></li>
<li>译文出自：<a href="https://github.com/xitu/gold-miner" target="_blank" rel="nofollow noopener noreferrer">掘金翻译计划</a></li>
<li>本文永久链接：<a href="https://github.com/xitu/gold-miner/blob/master/article/2021/webpacks-hot-module-replacement-feature-explained.md" target="_blank" rel="nofollow noopener noreferrer">github.com/xitu/gold-m…</a></li>
<li>译者：<a href="https://github.com/PassionPenguin" target="_blank" rel="nofollow noopener noreferrer">霜羽 Hoarfroster</a></li>
<li>校对者：<a href="https://github.com/5Reasons" target="_blank" rel="nofollow noopener noreferrer">5Reasons</a>、<a href="https://github.com/nia3y" target="_blank" rel="nofollow noopener noreferrer">nia3y</a></li>
</ul>
</blockquote>
<p><img alt class="lazyload" src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/47c1697861954aa08bd5c9d3898b068b~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p>在开发 JavaScript 应用程序时，每次我们保存代码更改后，我们都需要重新加载浏览器以刷新用户界面。</p>
<p>像 Webpack 之类的开发者工具可以通过<strong>监视模式</strong>来监听项目文件的更改。一旦检测到更改，Webpack 就会自动地重新构建应用程序并重新加载浏览器。</p>
<p>但是很快，开发者们就开始思考，有没有一种方法可以在不重新加载浏览器的情况下保存和更新页面的更改？毕竟，重新加载意味着会丢失在 UI 上的任何执行的状态：</p>
<ul>
<li>我们正在使用的所有模态框或对话框都将消失。我们需要从头开始，重复步骤，以使它们再次出现。</li>
<li>我们的应用程序的状态将被重置。如果我们使用的是 React 或 Vue 之类的库，我们需要重新执行状态更改，或者通过本地存储持久化状态。</li>
<li>想要将状态持久保存到本地存储，我们需要额外多写一些代码。除非我们的在生产环境下也有这种需求，否则每次开发时都需要为了调试而添加和删除代码，着实非常不方便。</li>
<li>即便我们仅仅只对 CSS 代码做出了很小的更改，也会触发浏览器的刷新。</li>
</ul>
<p>而<a href="https://webpack.js.org/concepts/hot-module-replacement/" target="_blank" rel="nofollow noopener noreferrer">模块热替换（Hot Module Replacement，HMR）</a>功能就是为了解决这种问题，并且现在已经成为了为前端开发提速的有力助手。</p>
<h2 data-id="heading-0">HMR 功能是怎么工作的？</h2>
<p>HMR 让我们可以在应用程序运行时交换、添加或删除 JavaScript 模块，而无需重新加载浏览器。在 Webpack 中是通过在 Webpack 开发服务器（<a href="https://github.com/webpack/webpack-dev-server" target="_blank" rel="nofollow noopener noreferrer">webpack-dev-server</a>）中创建一个 <strong>HMR 服务器</strong>实现的，而该服务器会通过 Websocket 与浏览器中的 <strong>HMR 运行时</strong>进行通信。</p>
<p><img alt="简述 HMR 工作的方式" class="lazyload" src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/c86a61859a904a98b1a986c7e645323b~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p>交换模块的过程如下：</p>
<ul>
<li>首次构建应用程序时，Webpack 会生成一份清单文件，包含编译的哈希和所有模块的列表。Webpack 会将 <strong>HMR 运行时</strong>注入到生成的 <code>bundle.js</code> 文件中。</li>
<li>Webpack 会在保存文件时检测文件的更改。</li>
<li>Webpack 编译器会用我们所做的更改来构建我们的应用程序，创建一个新的清单文件并将其与旧的清单文件进行比较。此过程也称为“热更新”。</li>
<li><strong>热更新</strong>数据将被发送到 <strong>HMR 服务器</strong>，后者则会把更新发送至 <strong>HMR 运行时</strong>。</li>
<li><strong>HMR 运行时</strong>将解包<strong>热更新</strong>数据，并使用适当的加载器来处理更改。如果我们有 CSS 更改，则将调用 css-loader 或 style-loader。如果我们对 JavaScript 代码进行了更改，则通常会调用 babel-loader。</li>
</ul>
<p>通过启用 HMR 功能，我们无需刷新浏览器即可让浏览器下载新的软件包并解包应用更改。HMR 运行时将接受来自 HMR 服务器的传入请求，包含清单文件和代码块，替换浏览器中的当前文件。</p>
<p>在运行启用了 HMR 的应用程序时保存代码更改时，我们实际上可以在 “Network” 选项卡上看到从 HMR 服务器发送的热更新文件：</p>
<p><img alt="网络选项卡下的热更新文件" class="lazyload" src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/9ceb93c48e31461bb109b434fb903ed2~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p>当“热更新”无法替换浏览器中的代码时，HMR 运行时将通知 webpack-dev-server。然后，webpack-dev-server 将刷新浏览器以下载新的 <code>bundle.js</code> 文件。我们可以通过在 Webpack 配置中添加 <code>hotOnly：true</code> 来禁用此行为。</p>
<h2 data-id="heading-1">如何启用 HMR 功能</h2>
<p>为了在项目中启用 HMR，我们需要让我们的应用程序知道如何处理<strong>热更新</strong>。我们可以通过实例化 Webpack 公开的 <code>module.hot</code> API 来实现：</p>
<p>首先，我们需要向 Webpack 配置文件中添加 <code>hot: true</code> 来启用 HMR，如下所示：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// webpack.config.js</span>

<span class="hljs-built_in">module</span>.exports = &#123;
    <span class="hljs-attr">entry</span>: &#123;
        <span class="hljs-attr">app</span>: <span class="hljs-string">'./src/index.js'</span>,
    &#125;,
    <span class="hljs-attr">devtool</span>: <span class="hljs-string">'inline-source-map'</span>,
    <span class="hljs-attr">devServer</span>: &#123;
        <span class="hljs-attr">hot</span>: <span class="hljs-literal">true</span>,
        <span class="hljs-comment">// ... 忽略掉其他配置</span>
    &#125;,
    <span class="hljs-attr">plugins</span>: [
        <span class="hljs-comment">// 开启这个插件</span>
        <span class="hljs-keyword">new</span> webpack.HotModuleReplacementPlugin(),
    ],
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>之后，我们必须使用 <code>module.hot</code> API 处理传入的 HMR 请求。这是一个普通的 JS 项目的实现示例：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// index.js</span>

<span class="hljs-keyword">import</span> component <span class="hljs-keyword">from</span> <span class="hljs-string">"./component"</span>;

<span class="hljs-built_in">document</span>.body.appendChild(component);

<span class="hljs-comment">// 检查是否支持 HMR 接口</span>
<span class="hljs-keyword">if</span> (<span class="hljs-built_in">module</span>.hot) &#123;
    <span class="hljs-comment">// 支持热更新</span>
    <span class="hljs-built_in">module</span>.hot.accept();
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>一旦告诉 Webpack 我们支持 HMR，HMR 运行时和加载程序就会接管处理更新。</p>
<p>但是，为复杂的应用程序实现 HMR 可能会很棘手，因为我们可能会遇到不希望的副作用，例如<a href="https://webpack.js.org/guides/hot-module-replacement/%EF%BC%83enabling-hmr" target="_blank" rel="nofollow noopener noreferrer">仍然绑定到旧函数的事件处理程序</a>，尤其是当你使用 React 或 Vue 之类的库。此外，我们还需要确保<a href="https://webpack.js.org/guides/production/" target="_blank" rel="nofollow noopener noreferrer">仅在开发中启用 HMR</a>。</p>
<p>不过在我们尝试自己实施 HMR 之前，建议你先为我们的项目寻找一下可用的解决方案，因为 HMR 已经集成到许多流行的 JavaScript 应用程序生成器中。</p>
<p>Create React App 和 Next.js 都内置了 React Fast Refresh，React 特定的热重载实现。而 Vue CLI 3 的 HMR 则是通过 <a href="https://github.com/vuejs/vue-loader" target="_blank" rel="nofollow noopener noreferrer">vue-loader</a> 实现的。<a href="https://github.com/sveltejs/svelte-loader" target="_blank" rel="nofollow noopener noreferrer">Svelte</a> 和 <a href="https://github.com/PatrickJS/angular-hmr" target="_blank" rel="nofollow noopener noreferrer">Angular</a> 也有自己的 HMR 集成，因此我们没有必要从头开始编写集成。</p>
<h2 data-id="heading-2">小结</h2>
<p>热模块替换能让我们无需刷新浏览器即可在浏览器中查看代码更改所带来的效果，从而可以保留前端应用程序的状态。</p>
<p>但是实现 HMR 可能很棘手，因为它会产生一些副作用。幸运的是，HMR 已在许多 JavaScript 应用程序生成器中实现。因此我们可以直接享受此功能，而不必自己实现。</p>
<blockquote>
<p>如果发现译文存在错误或其他需要改进的地方，欢迎到 <a href="https://github.com/xitu/gold-miner" target="_blank" rel="nofollow noopener noreferrer">掘金翻译计划</a> 对译文进行修改并 PR，也可获得相应奖励积分。文章开头的 <strong>本文永久链接</strong> 即为本文在 GitHub 上的 MarkDown 链接。</p>
</blockquote>
<hr>
<blockquote>
<p><a href="https://github.com/xitu/gold-miner" target="_blank" rel="nofollow noopener noreferrer">掘金翻译计划</a> 是一个翻译优质互联网技术文章的社区，文章来源为 <a href="https://juejin.im/" target="_blank" rel="nofollow noopener noreferrer">掘金</a> 上的英文分享文章。内容覆盖 <a href="https://github.com/xitu/gold-miner#android" target="_blank" rel="nofollow noopener noreferrer">Android</a>、<a href="https://github.com/xitu/gold-miner#ios" target="_blank" rel="nofollow noopener noreferrer">iOS</a>、<a href="https://github.com/xitu/gold-miner#%E5%89%8D%E7%AB%AF" target="_blank" rel="nofollow noopener noreferrer">前端</a>、<a href="https://github.com/xitu/gold-miner#%E5%90%8E%E7%AB%AF" target="_blank" rel="nofollow noopener noreferrer">后端</a>、<a href="https://github.com/xitu/gold-miner#%E5%8C%BA%E5%9D%97%E9%93%BE" target="_blank" rel="nofollow noopener noreferrer">区块链</a>、<a href="https://github.com/xitu/gold-miner#%E4%BA%A7%E5%93%81" target="_blank" rel="nofollow noopener noreferrer">产品</a>、<a href="https://github.com/xitu/gold-miner#%E8%AE%BE%E8%AE%A1" target="_blank" rel="nofollow noopener noreferrer">设计</a>、<a href="https://github.com/xitu/gold-miner#%E4%BA%BA%E5%B7%A5%E6%99%BA%E8%83%BD" target="_blank" rel="nofollow noopener noreferrer">人工智能</a>等领域，想要查看更多优质译文请持续关注 <a href="https://github.com/xitu/gold-miner" target="_blank" rel="nofollow noopener noreferrer">掘金翻译计划</a>、<a href="http://weibo.com/juejinfanyi" target="_blank" rel="nofollow noopener noreferrer">官方微博</a>、<a href="https://zhuanlan.zhihu.com/juejinfanyi" target="_blank" rel="nofollow noopener noreferrer">知乎专栏</a>。</p>
</blockquote></div> <div class="image-viewer-box" data-v-78c9b824><!----></div>  
</div>
            