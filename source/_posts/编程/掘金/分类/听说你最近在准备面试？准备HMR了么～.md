
---
title: '听说你最近在准备面试？准备HMR了么～'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=9681'
author: 掘金
comments: false
date: Sun, 11 Jul 2021 06:37:23 GMT
thumbnail: 'https://picsum.photos/400/300?random=9681'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>  之前面试的时候，很多次面试官都有提到过HMR的原理，正好最近的react项目当中需要调试这一块，就做一个总结。</p>
<p>  在开发过程中，我们经常会用到webpack-dev-server，它有一个默认自带的功能就是live reloading（实时重新加载）功能。在命令行中运行 webpack serve，如果你更改任何源文件并保存它们，webpack-dev-server将在编译代码后自动刷新浏览器。</p>
<p>  但是这样有一个缺点，就是如果我们需要先进行一些操作，比如打开一个对话框，再调试对话框的样式。或者经过一些特定的查询后，来调试一个列表的样式。如果浏览器在改完代码后直接刷新了，那么我们还需要去通过打开对话框或者再去做特定的查询来验证刚才的修改效果。HMR即hot module replacement（模块热更新）就解决了这个问题，它保留了在完全重新加载页面期间丢失的应用程序状态，允许在运行时只更新被修改的模块，而无需完全刷新。webpack-dev-server 支持 hot 模式，在试图重新加载整个页面之前，hot 模式会尝试使用 HMR 来更新。</p>
<p>  本文将从配置原理和实现原理两个方面来讲解模块热更新。</p>
<p><strong>配置原理</strong></p>
<p>从官方文档《指南》的 <a href="https://link.juejin.cn/?target=https%3A%2F%2Fwebpack.docschina.org%2Fguides%2Fhot-module-replacement%2F%23enabling-hmr" target="_blank" rel="nofollow noopener noreferrer" title="https://webpack.docschina.org/guides/hot-module-replacement/#enabling-hmr" ref="nofollow noopener noreferrer">热模块更新</a> 部分中我们可以看出想要应用webpack的热模块更新能力，总共分两步：</p>
<p>  1.在devServer的配置中，加上 hot: true。</p>
<pre><code class="copyable">devServer: &#123;
  contentBase: './dist',
+ hot: true,
&#125;,
<span class="copy-code-btn">复制代码</span></code></pre>
<p>  2.引入模块时，通过 module.hot.accept 检查更新。</p>
<pre><code class="copyable">  if (module.hot) &#123;
    module.hot.accept('./print.js', function() &#123;
     document.body.removeChild(element);
     element = component(); // 重新渲染 "component"，以便更新 click 事件处理函数
     document.body.appendChild(element);
    &#125;)
  &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>  但是像style-loader、css-loader之中，其实在内部调用了module.hot.accept这样的HMR API来检查样式更新，所以就不用我们再额外加代码来加载更新后的代码。在css依赖模块更新之后，会将其patch到<style>标签中。</p>
<p>  同样原理，社区还提供许多其他loader和示例，可以使HMR与各种框架和库平滑地进行交互，包括：React Hot Loader、Vue loader、Angular HMR。</p>
<p>  Vue loader实现了在引入vue文件更新的时候，自动加载vue文件的更新。这里再来重点讲一下React框架中的HMR应用方式。React框架一开始用的React Hot Loader在官方声明中已经宣布将要被<a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fpmmmwh%2Freact-refresh-webpack-plugin" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/pmmmwh/react-refresh-webpack-plugin" ref="nofollow noopener noreferrer">react-refresh-webpack-plugin</a>所取代。在它的官网中我们可以看到他的引入方式，这里需要强调的有两点：</p>
<p>  1.启动命令中的--hot 和 webpack配置中的 new webpack.HotModuleReplacementPlugin()不能同时使用。（<a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fwebpack%2Fwebpack-dev-server%2Fissues%2F87%25EF%25BC%2589" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/webpack/webpack-dev-server/issues/87%EF%BC%89" ref="nofollow noopener noreferrer">github.com/webpack/web…</a></p>
<p>  2.在webpack调试环境的配置中不能使用externals配置。不然会让react-refresh-webpack-plugin失效。</p>
<p><strong>实现原理</strong></p>
<p>  这里我们首先通过一张网图来总览：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/ae8c3fa22d3840bfafc58aa2dfbcf9ed~tplv-k3u1fbpfcp-watermark.image" alt="HMR全过程.png" loading="lazy" referrerpolicy="no-referrer"></p>
<ol>
<li>编辑器中修改和保存代码。</li>
<li>HotModuleReplacementPlugin会产生相应的更新代码的patch文件。</li>
<li>通过Webpack传给webpack-dev-server有文件更新的信息和更新后的相应patch文件。</li>
<li>webpack-dev-server通过ws协议接口，向运行在浏览器中的webpack-dev-server/client发送消息，告诉浏览器有文件更新。</li>
<li>webpack-dev-server/client将之前打包的hash值传给hot/dev-server，hot/dev-server相当于所有打包后js文件的主接口。</li>
<li>hot/dev-server告知webpack引入的JSONP请求库来向webpack-dev-server请求manifest文件和chunk文件。</li>
<li>HMR runtime将请求到的文件传送给相应的React-loader hmr或者Style-loader hmr来更新运行时App的相应的模块。</li>
<li>如果更新失败，降级为刷新页面。</li>
</ol>
<p>  下面我们来举个例子看一下具体的请求，首先我们用create-react-app脚手架来初始化一个react项目：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/eae3d74c129847cdb9124b76123a5167~tplv-k3u1fbpfcp-watermark.image" alt="启动.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>  在初始化的过程中，webpack-dev-server与webpack-dev-server/client建立了ws连接，并且在连接中向webpack-dev-server/client传送了初始化的消息，其中比较重要的是画红框的这个hash值，表示下次HotModuleReplacementPlugin在打包patch文件的时候，会用到的hash。</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/4aa995bac82a4a24ae920a380f1921fc~tplv-k3u1fbpfcp-watermark.image" alt="截屏2021-07-11 下午10.07.30.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>  当编辑器中的代码改变的时候，webpack-dev-server会发送给webpack-dev-server/client两个invalid消息，并且再传一个下次打包用的hash值。</p>
<p>  之后webpack-dev-server/client会触发hot/dev-server调用JSONP发送请求，来请求初始化时传来的hash值组成的本次代码更新的patch文件。patch文件一共有两个：hash.hot-update.json、chunk名.hash.hot-update.js。从下面两个图可以看出hash.hot-update.json文件中也是包含了下次打包会用到的hash值，而chunk名.hash.hot-update.js这个文件就包含了已经更新的包组成的webpackHotUpdate函数，这个函数将会传递给相应的loader来更新相应的包。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/cbba6a61d8334098b2519a7c576b5b1a~tplv-k3u1fbpfcp-watermark.image" alt="截屏2021-07-11 下午10.09.31.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/f23449a5f12f47219f43d6393db83747~tplv-k3u1fbpfcp-watermark.image" alt="截屏2021-07-11 下午10.09.48.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>至此，就大概分析完了HMR的流程。</p>
<p>参考：<a href="https://link.juejin.cn/?target=https%3A%2F%2Frajaraodv.medium.com%2Fwebpack-hot-module-replacement-hmr-e756a726a07%23.y667mx4lg" target="_blank" rel="nofollow noopener noreferrer" title="https://rajaraodv.medium.com/webpack-hot-module-replacement-hmr-e756a726a07#.y667mx4lg" ref="nofollow noopener noreferrer">rajaraodv.medium.com/webpack-hot…</a></p>
<hr></div>  
</div>
            