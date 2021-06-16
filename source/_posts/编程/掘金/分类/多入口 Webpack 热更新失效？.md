
---
title: '多入口 Webpack 热更新失效？'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/67891dc6d9f24be4a6ea475857c0f88c~tplv-k3u1fbpfcp-zoom-1.image'
author: 掘金
comments: false
date: Mon, 14 Jun 2021 17:13:05 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/67891dc6d9f24be4a6ea475857c0f88c~tplv-k3u1fbpfcp-zoom-1.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h2 data-id="heading-0">前言</h2>
<p><code>Webpack</code> 对于现代前端开发者，想必是相当熟悉了，在很多项目中，应用非常广泛，而 <code>webpack-dev-server</code>，相信大家应该也都接触过。最近，作者在配置多入口，热更新在单入口是好使的，结果到了多入口不好使？，然后通过 Google 寻找答案，找到了一篇 <code>issue</code>，<a href="https://github.com/webpack/webpack-dev-server/issues/2792" target="_blank" rel="nofollow noopener noreferrer">HMR not working with multiple entries</a>，跟我的问题类似，好像真的有 BUG？看到作者回复</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/67891dc6d9f24be4a6ea475857c0f88c~tplv-k3u1fbpfcp-zoom-1.image" alt="WechatIMG1679" loading="lazy" referrerpolicy="no-referrer"></p>
<p>v4 修复了该问题，我丢，我还在使用 v3，翻看 v4 文档</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/5297ae1360f84d288d7e93dc2e079e90~tplv-k3u1fbpfcp-zoom-1.image" alt="WechatIMG1680" loading="lazy" referrerpolicy="no-referrer"></p>
<p>此时，只有一个感觉，热更新都多久的东西了，不应该存在多入口，热更新有问题吧？升级到 v4 之后，还是不行，当时我这暴脾气就上来了，直接翻看源码。翻看源码之前，首先要对热更新是个什么，有个基础的了解。</p>
<h2 data-id="heading-1">模块热更新</h2>
<p>模块热更新(Hot Module Replacement)是指在浏览器运行过程中，替换、添加或删除模块，而无需重新加载整个页面。</p>
<ul>
<li>保留在完全重新加载页面期间丢失的应用程序状态</li>
<li>在源代码中对 <code>CSS/JS</code> 进行修改，会立刻在浏览器中进行更新，并只更新改变的内容，节省开发时间</li>
</ul>
<p>对比 <code>Live Reload</code> 方案，<code>HMR</code> 体现了其强大之处，实时模块热刷新和保存应用状态，极大的提高了开发效率和开发体验。</p>
<h2 data-id="heading-2">启用模块热更新</h2>
<p><code>HMR</code> 的启用十分简单，一个带有热更新功能的 <code>webpack.config.js</code> 文件的配置如下：</p>
<pre><code class="copyable">const path = require('path');

module.exports = &#123;
    // ...
    entry: &#123;
        app: ['./src/index.js']
    &#125;,
    devServer: &#123;
        contentBase: path.resolve(__dirname, 'dist'),
        hot: true,
        historyApiFallback: true,
        compress: true
    &#125;
&#125;;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>src/index.js</p>
<pre><code class="copyable">if (module.hot) &#123;
    module.hot.accept();
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-3">原理</h2>
<p>网上关于 <code>Webpack</code> 热更新原理文章很多，这里就不详细描述了，推荐几个。</p>
<ul>
<li>
<p><a href="https://tsejx.github.io/webpack-guidebook/principle-analysis/operational-principle/hot-module-replacement" target="_blank" rel="nofollow noopener noreferrer">模块热更新</a></p>
</li>
<li>
<p><a href="https://juejin.cn/post/6844904008432222215" target="_blank">轻松理解 webpack 热更新原理</a></p>
</li>
<li>
<p><a href="https://juejin.cn/post/6844904008432222215" target="_blank">Webpack HMR 原理解析</a></p>
</li>
</ul>
<h2 data-id="heading-4">调试</h2>
<h3 data-id="heading-5">npm link</h3>
<pre><code class="copyable">$ git clone https://github.com/webpack/webpack-dev-server.git
<span class="copy-code-btn">复制代码</span></code></pre>
<p>一定要找到你项目中对应的版本包，对号入座噢，否则会报错，把 <code>webpack-dev-server</code> 项目拉下来之后，尝试在 <code>webpack-dev-server/lib/Server.js</code> 该文件增加一行 <code>console.log</code></p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/01496038bbb049aab4cab8ba3d7e7c4a~tplv-k3u1fbpfcp-zoom-1.image" alt="carbon" loading="lazy" referrerpolicy="no-referrer"></p>
<p>然后进入根目录</p>
<pre><code class="copyable">$ cd webpack-dev-server
$ npm link
<span class="copy-code-btn">复制代码</span></code></pre>
<p>生成软链</p>
<pre><code class="copyable">cd 项目地址
npm link webpack-dev-server
<span class="copy-code-btn">复制代码</span></code></pre>
<p>link 成功之后，会提示下面，更换了 webpack-dev-server 地址</p>
<pre><code class="copyable">jiang@JiangdeMacBook-Pro-3 commonVideoClient % cnpm link webpack-dev-server
/Users/jiang/Desktop/commonVideoClient/node_modules/webpack-dev-server -> /usr/local/lib/node_modules/webpack-dev-server -> /Users/jiang/Desktop/webpack-dev-server
<span class="copy-code-btn">复制代码</span></code></pre>
<p>然后在项目跑 <code>webpack-dev-server</code>，在控制台应该就会看到对应的输出了，调试源码非常方便。</p>
<p><code>npm link</code> 方案，第三方库和项目属于不同的项目，它们有自己的 <code>node_modules</code>，如果第三方库和项目都使用了同一个依赖，它们会在各自的 <code>node_modules</code> 去查
找，如果这个依赖不支持多例，应用就会异常。</p>
<h3 data-id="heading-6">yalc</h3>
<p>在开发和创作多个包（私有或公共）时，您经常发现自己需要在本地环境中正在处理的其他项目中使用最新/WIP 版本，而无需将这些包发布到远程注册中心。NPM 和 Yarn 使用类似的符号链接包( npm/yarn link)方法解决了这个问题。虽然这在许多情况下可能有效，但它经常带来令人讨厌的约束和依赖解析、文件系统之间的符号链接互操作性等问题。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/895d28b5d6974241aaccfc4f111b36d7~tplv-k3u1fbpfcp-zoom-1.image" alt="yalc" loading="lazy" referrerpolicy="no-referrer"></p>
<p>全局安装 yalc</p>
<pre><code class="copyable">npm install -g yalc
<span class="copy-code-btn">复制代码</span></code></pre>
<p>生成 yalc 包</p>
<pre><code class="copyable">$ cd webpack-dev-server
$ yalc publish
<span class="copy-code-btn">复制代码</span></code></pre>
<p>可以在自己本地 <code>/Users/jiang/.yalc/packages/webpack-dev-server</code>，找到对应的包</p>
<pre><code class="copyable">cd 项目地址
yalc link webpack-dev-server
<span class="copy-code-btn">复制代码</span></code></pre>
<p>link 后，可以在自己项目下，找到 <code>.yalc</code></p>
<p>每次手动修改第三方库的代码，都需要手动 link，就很麻烦，对不对？ok，神器来了，<code>nodemon</code>，</p>
<pre><code class="copyable">npm install -g nodemon

nodemon
--ignore dist/
--ignore node_modules/
--watch lib # 观察目录
-C # 只在变更后执行，首次启动不执行命令
-e js,ts,html,less,scss 监控指定后缀名的文件
--debug # 调试
-x "yalc publish" 自定义命令
<span class="copy-code-btn">复制代码</span></code></pre>
<p>然后，我们来试试这个工具，在 <code>webpack-dev-server</code>，新增三行可执行命令</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/7ae53353165c42809312bf5e4db073c5~tplv-k3u1fbpfcp-zoom-1.image" alt="carbon2" loading="lazy" referrerpolicy="no-referrer"></p>
<p>运行下 <code>npm run watch</code>，然后每次修改，都会自动更新，是不是很舒服？</p>
<img width="119" alt="WeChat7c8e2813667093e82dc47a836e6d5cdb" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/6fcceba8aa0543799b4e897141912f13~tplv-k3u1fbpfcp-zoom-1.image" loading="lazy" referrerpolicy="no-referrer">
<h3 data-id="heading-7">网页调试</h3>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/c577a52742e44d37a1ec995109b656d1~tplv-k3u1fbpfcp-zoom-1.image" alt="WechatIMG1776" loading="lazy" referrerpolicy="no-referrer"></p>
<p>找到对应的文件位置和代码行数，通过浏览器进行断点调试，这个就不展开讲了。</p>
<h2 data-id="heading-8">找到问题</h2>
<p>经过一番折腾，升级 <code>webpack-dev-server@v4</code>，原理分析，源码调试，与之前正常的单页应用进行对比，发现都是正常的，还是不行，我就郁闷了，为何呢？突然之间，我悟了，好像多页应用没有在入口进行 <code>module.hot</code></p>
<p>之前在 <code>app.jsx</code> 中写的 <code>module.hot</code></p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/24bc52910e5c4873901d7de1c81cfe6c~tplv-k3u1fbpfcp-zoom-1.image" alt="carbon3" loading="lazy" referrerpolicy="no-referrer"></p>
<p>改在入口文件 进行 <code>module.hot</code></p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/187139bca30d4ed6b6b3bfd39fb9416a~tplv-k3u1fbpfcp-zoom-1.image" alt="carbon4" loading="lazy" referrerpolicy="no-referrer"></p>
<p>ok，成功，喜大普奔。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/8afab4272ac946b6984f28507fe923b0~tplv-k3u1fbpfcp-zoom-1.image" alt="WechatIMG1780" loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-9">总结</h2>
<p>带着问题，阅读源码是最高效的，这样你在阅读源码的过程中也不会感到无聊，因为你是要解决问题，才会去看源码，对于不懂的代码，一点一点调试，一步一步走下去，再结合现有的一些原理文章（站在巨人的肩膀上）就会找到答案。这次的经历，也算很有意思，感谢小伙伴们的阅读，喜欢的可以点个赞噢 🌟 ～</p></div>  
</div>
            