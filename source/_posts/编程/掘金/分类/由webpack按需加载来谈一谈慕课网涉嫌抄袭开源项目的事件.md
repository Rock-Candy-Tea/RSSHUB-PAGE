
---
title: '由webpack按需加载来谈一谈慕课网涉嫌抄袭开源项目的事件'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/913ca2bb92624383b9c0054a4988f239~tplv-k3u1fbpfcp-zoom-1.image'
author: 掘金
comments: false
date: Sun, 20 Jun 2021 15:38:24 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/913ca2bb92624383b9c0054a4988f239~tplv-k3u1fbpfcp-zoom-1.image'
---

<div>   
<div class="markdown-body"><style>@charset "UTF-8";.markdown-body&#123;word-break:break-word;line-height:2;font-weight:400;font-size:15px;overflow-x:hidden;color:#333;letter-spacing:1.2px&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1:first-child,.markdown-body h2:first-child,.markdown-body h3:first-child,.markdown-body h4:first-child,.markdown-body h5:first-child,.markdown-body h6:first-child&#123;margin-top:-1.5rem;margin-bottom:1rem&#125;.markdown-body h1:before,.markdown-body h2:before,.markdown-body h3:before,.markdown-body h4:before,.markdown-body h5:before,.markdown-body h6:before&#123;content:"#";display:inline-block;color:#3eaf7c;padding-right:.23em&#125;.markdown-body h1&#123;position:relative;font-size:2.5rem;margin-bottom:5px&#125;.markdown-body h1:before&#123;font-size:2.5rem&#125;.markdown-body h2&#123;padding-bottom:.5rem;font-size:2.2rem;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:1.5rem;padding-bottom:0&#125;.markdown-body h4&#123;font-size:1.25rem&#125;.markdown-body h5&#123;font-size:1rem&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body strong&#123;color:#3eaf7c&#125;.markdown-body img&#123;max-width:100%;border-radius:2px;display:block;margin:auto&#125;.markdown-body hr&#123;border:none;border-top:1px solid #3eaf7c;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;overflow-x:auto;padding:.2rem .5rem;margin:0;color:#3eaf7c;font-size:.85em;background-color:rgba(27,31,35,.05);border-radius:3px&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75;border:.5rem solid #3eaf7c&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;font-weight:500;text-decoration:none;color:#3eaf7c;margin:0 5px&#125;.markdown-body a:active,.markdown-body a:hover&#123;text-decoration:none;border-bottom:1.5px solid #3eaf7c&#125;.markdown-body a[href^=http]:after&#123;content:url("data:image/svg+xml;base64,PHN2ZyBjbGFzcz0iaWNvbiIgdmlld0JveD0iMCAwIDEwMjQgMTAyNCIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIiB3aWR0aD0iMTQiIGhlaWdodD0iMTQiPjxkZWZzPjxzdHlsZS8+PC9kZWZzPjxwYXRoIGQ9Ik04MzIgMTI4SDY0MHY2NGgxNDYuNzUyTDUyMS4zNzYgNDU3LjM3Nmw0NS4yNDggNDUuMjQ4TDgzMiAyMzcuMjQ4VjM4NGg2NFYxMjh6IiBmaWxsPSIjM2VhZjdjIi8+PHBhdGggZD0iTTc2OCA4MzJIMTkyVjI1NmgzNTJ2LTY0SDE2MGEzMiAzMiAwIDAwLTMyIDMydjY0MGEzMiAzMiAwIDAwMzIgMzJoNjQwYTMyIDMyIDAgMDAzMi0zMlY0ODBoLTY0djM1MnoiIGZpbGw9IiMzZWFmN2MiLz48L3N2Zz4=");margin-left:2px&#125;.markdown-body a[href^="#"]:before&#123;content:"#"&#125;.markdown-body table&#123;display:inline-block!important;font-size:13px;width:auto;max-width:100%;overflow:auto;border:1px solid #3eaf7c;border-collapse:collapse&#125;.markdown-body thead&#123;background:#3eaf7c;color:#fff;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:rgba(153,255,188,.1)&#125;.markdown-body td,.markdown-body th&#123;padding:4px 8px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#7b7878;padding:1px 23px;border-left:.5rem solid;border-color:#42b983;background-color:rgba(66,184,131,.1);position:relative;margin:14px 8px 0&#125;.markdown-body blockquote:before&#123;display:inline-block;position:absolute;content:url("data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMjUiIGhlaWdodD0iMjUiIHZpZXdCb3g9IjAgMCAyNyAyNyIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj48ZyB0cmFuc2Zvcm09InRyYW5zbGF0ZSgxLjg2MiAxLjg2MikiIGZpbGwtcnVsZT0ibm9uemVybyIgZmlsbD0ibm9uZSI+PGNpcmNsZSBzdHJva2U9IiNGRkYiIHN0cm9rZS13aWR0aD0iMS43MjQiIGZpbGw9IiM0MkI5ODMiIGN4PSIxMS42MzgiIGN5PSIxMS42MzgiIHI9IjExLjYzOCIvPjxwYXRoIGQ9Ik0xNC45NzggNi4yN0E1LjAwNiA1LjAwNiAwIDAwNi42NyA5LjQ2OGE0LjkwMSA0LjkwMSAwIDAwMS43NzMgNC4zNjJjLjMyMy4yNTguNTE0LjY0Ny41MjIgMS4wNnYxLjA2YTIuNjg1IDIuNjg1IDAgMDA1LjM3IDB2LTEuMDA4Yy4wMDItLjM5OC4xNzMtLjc3Ny40Ny0xLjA0MmE1LjAyMyA1LjAyMyAwIDAwLjE3My03LjYzem0tMy4zMzcgMTAuOTY3YTEuMzA0IDEuMzA0IDAgMDEtMS4yODYtMS4yODd2LS4yNzhoMi41NzJ2LjI2MWMwIC43MTMtLjU3MyAxLjI5NC0xLjI4NiAxLjMwNHptMi4yNi00LjQxNWMtLjQ0LjM4My0uNzUuODkzLS44ODcgMS40NmgtMi43NDZhMi44NjggMi44NjggMCAwMC0uOTM4LTEuNTNoLS4wMThhMy40NzYgMy40NzYgMCAwMS0xLjI2OS0zLjE0NSAzLjYxNSAzLjYxNSAwIDAxNy4xOTYuNCAzLjY1IDMuNjUgMCAwMS0xLjMzOCAyLjgxNXoiIGZpbGw9IiNGRkYiLz48L2c+PC9zdmc+");width:25px;height:25px;left:-16px;top:12px&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body details&#123;outline:none;border:none;border-left:4px solid #3eaf7c;padding-left:10px;margin-left:4px&#125;.markdown-body details summary&#123;cursor:pointer;border:none;outline:none;background:#fff;margin:0 -17px&#125;.markdown-body details summary::-webkit-details-marker&#123;color:#3eaf7c&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body ol li::marker&#123;color:#3eaf7c&#125;.markdown-body ul li&#123;list-style:none;padding-left:10px&#125;.markdown-body ul li::marker&#123;content:"•";color:#3eaf7c&#125;.markdown-body ul li.task-list-item:before&#123;content:"";margin-right:0&#125;.markdown-body input[type=checkbox]&#123;vertical-align:text-bottom;box-shadow:inset 0 0 0 10px #fff&#125;.markdown-body input[type=checkbox]:before&#123;content:url("data:image/svg+xml;base64,PHN2ZyBjbGFzcz0iaWNvbiIgdmlld0JveD0iMCAwIDEwMjQgMTAyNCIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIiB3aWR0aD0iMTYiIGhlaWdodD0iMTYiPjxkZWZzPjxzdHlsZS8+PC9kZWZzPjxwYXRoIGQ9Ik04NzcuMDU2IDE0Ni45NDR2NzMwLjExMkgxNDYuOTQ0VjE0Ni45NDRoNzMwLjExMnptMC0xMDQuMjc3SDE0Ni45NDRjLTU3LjYyOCAwLTEwNC4yNzcgNDYuNjQ5LTEwNC4yNzcgMTA0LjI3N3Y3MzAuMTEyYzAgNTcuNjI4IDQ2LjY0OSAxMDQuMjc3IDEwNC4yNzcgMTA0LjI3N2g3MzAuMTEyYzU3LjYyOCAwIDEwNC4yNzctNDYuNjQ5IDEwNC4yNzctMTA0LjI3N1YxNDYuOTQ0YzAtNTcuNjI4LTQ2LjY0OS0xMDQuMjc3LTEwNC4yNzctMTA0LjI3N3oiIGZpbGw9IiMzZWFmN2MiLz48L3N2Zz4=");position:relative;top:-2px;right:2px&#125;.markdown-body input[type=checkbox]:checked:before&#123;content:url("data:image/svg+xml;base64,PHN2ZyBjbGFzcz0iaWNvbiIgdmlld0JveD0iMCAwIDEwMjQgMTAyNCIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIiB3aWR0aD0iMTUiIGhlaWdodD0iMTUiPjxkZWZzPjxzdHlsZS8+PC9kZWZzPjxwYXRoIGQ9Ik05MTAuMjA4IDBIMTEzLjc2QTExNC4xMTIgMTE0LjExMiAwIDAwLS4wMzIgMTEzLjc5MlY5MTAuMjRjMCA2Mi41OTIgNTEuMiAxMTMuNzkyIDExMy43OTIgMTEzLjc5Mmg3OTYuNDQ4YzYyLjU5MiAwIDExMy43OTItNTEuMiAxMTMuNzkyLTExMy43OTJWMTEzLjc5MkMxMDI0IDUxLjIgOTcyLjggMCA5MTAuMjA4IDB6bS01MTIgNzk2LjQ0OEwxMTMuNzYgNTEybDc5LjY0OC03OS42NDggMjA0LjggMjA0LjhMODMwLjU2IDIwNC44bDc5LjY0OCA3OS42NDgtNTEyIDUxMnoiIGZpbGw9IiMzZWFmN2MiLz48L3N2Zz4=");position:relative;top:-2px;right:2px&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/913ca2bb92624383b9c0054a4988f239~tplv-k3u1fbpfcp-zoom-1.image" alt="quote" loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-0">谈谈webpack的按需加载</h2>
<p>对于采用单页应用作为前端架构的网站来说，会面临着一个网页需要加载的代码量很大的问题，因为许多功能都集中的做到了一个 HTML 里。 这会导致网页加载缓慢、交互卡顿，用户体验将非常糟糕。导致这个问题的根本原因在于一次性的加载所有功能对应的代码，但其实用户每一阶段只可能使用其中一部分功能。 所以解决以上问题的方法就是用户当前需要用什么功能就只加载这个功能对应的代码，也就是所谓的按需加载。</p>
<p>在给单页应用做按需加载优化时，一般采用以下原则：</p>
<ul>
<li>把整个网站划分成一个个小功能，再按照每个功能的相关程度把它们分成几类。</li>
<li>把每一类合并为一个 Chunk，按需加载对应的 Chunk。</li>
<li>对于用户首次打开你的网站时需要看到的画面所对应的功能，不要对它们做按需加载，而是放到执行入口所在的 Chunk 中，以降低用户能感知的网页加载时间。</li>
<li>对于个别依赖大量代码的功能点，例如依赖 Chart.js 去画图表、依赖 flv.js 去播放视频的功能点，可再对其进行按需加载。</li>
</ul>
<p>被分割出去的代码的加载需要一定的时机去触发，也就是当用户操作到了或者即将操作到对应的功能时再去加载对应的代码。 被分割出去的代码的加载时机需要开发者自己去根据网页的需求去衡量和确定。</p>
<p>由于被分割出去进行按需加载的代码在加载的过程中也需要耗时，你可以预言用户接下来可能会进行的操作，并提前加载好对应的代码，从而让用户感知不到网络加载时间。</p>
<p>上述内容简单的介绍了一下webpack的按需加载，引用自文章<a href="https://www.cnblogs.com/joyco773/p/9051401.html" target="_blank" rel="nofollow noopener noreferrer">《webpack学习笔记--按需加载》</a>。</p>
<h2 data-id="heading-1">webpack打包压缩实践</h2>
<p>首先新建一个文件夹 <code>webpack-demo</code>，目录行进入文件话，通过 <code>npm init -y</code> 构建一个项目工程，安装如下几个工具包：</p>
<pre><code class="hljs language-bash copyable" lang="bash">npm i webpack webpack-cli mini-css-extract-plugin css-loader
<span class="copy-code-btn">复制代码</span></code></pre>
<p>完成过如下图所示：
​</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/e01bb5e1263e47d1af8d1b8e248e0361~tplv-k3u1fbpfcp-zoom-1.image" alt="image" loading="lazy" referrerpolicy="no-referrer"></p>
<p>然后便可在文件夹根目录新建一个 <code>webpack.config.js</code> 文件，编写 <code>webpack</code> 配置项，如下所示：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">const</span> path = <span class="hljs-built_in">require</span>(<span class="hljs-string">'path'</span>)
<span class="hljs-keyword">const</span> MiniCssExtractPlugin = <span class="hljs-built_in">require</span>(<span class="hljs-string">"mini-css-extract-plugin"</span>);

<span class="hljs-built_in">module</span>.exports = &#123;
  <span class="hljs-attr">mode</span>: <span class="hljs-string">'development'</span>, <span class="hljs-comment">// 环境模式</span>
  <span class="hljs-attr">devtool</span>: <span class="hljs-string">"source-map"</span>,
  <span class="hljs-attr">entry</span>: path.resolve(__dirname, <span class="hljs-string">'./main.js'</span>), <span class="hljs-comment">// 打包入口</span>
  <span class="hljs-attr">output</span>: &#123;
    <span class="hljs-attr">path</span>: path.resolve(__dirname, <span class="hljs-string">'dist'</span>), <span class="hljs-comment">// 打包出口</span>
    <span class="hljs-attr">filename</span>: <span class="hljs-string">'js/[name].js'</span> <span class="hljs-comment">// 打包完的静态资源文件名</span>
  &#125;,
  <span class="hljs-attr">module</span>: &#123;
    <span class="hljs-attr">rules</span>: [
      &#123;
        <span class="hljs-attr">test</span>: <span class="hljs-regexp">/\.css$/</span>,
        use: [
          MiniCssExtractPlugin.loader,
          <span class="hljs-string">"css-loader"</span>
        ]
      &#125;
    ]
  &#125;,
  <span class="hljs-attr">plugins</span>: [
    <span class="hljs-keyword">new</span> MiniCssExtractPlugin(&#123;
      <span class="hljs-attr">filename</span>: <span class="hljs-string">"[name].css"</span>,
    &#125;)
  ]
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>目前我们还没有编写入口，同样在根目录下新建一个 <code>main.js</code>，并且引入四个 <code>css</code> 文件，如下所示：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/45b6bc23162841b0b57913ec6bd5d04a~tplv-k3u1fbpfcp-zoom-1.image" alt="image (2)" loading="lazy" referrerpolicy="no-referrer"></p>
<p><code>css</code> 文件的内容我们分别给一个象征性的样式：</p>
<pre><code class="hljs language-css copyable" lang="css"><span class="hljs-selector-class">.a</span> &#123;
  <span class="hljs-attribute">font-size</span>: <span class="hljs-number">12px</span>;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="hljs language-css copyable" lang="css"><span class="hljs-selector-class">.b</span> &#123;
  <span class="hljs-attribute">color</span>: <span class="hljs-number">#fff</span>;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="hljs language-css copyable" lang="css"><span class="hljs-selector-class">.c</span> &#123;
  <span class="hljs-attribute">background-color</span>: red;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="hljs language-css copyable" lang="css"><span class="hljs-selector-class">.d</span> &#123;
  <span class="hljs-attribute">padding</span>: <span class="hljs-number">10px</span>;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>最后一步便是在 <code>package.json</code> 添加 <code>script</code> 指令，如下所示：</p>
<pre><code class="hljs language-json copyable" lang="json">&#123;
  <span class="hljs-attr">"name"</span>: <span class="hljs-string">"webpack-demo"</span>,
  <span class="hljs-attr">"version"</span>: <span class="hljs-string">"1.0.0"</span>,
  <span class="hljs-attr">"description"</span>: <span class="hljs-string">""</span>,
  <span class="hljs-attr">"main"</span>: <span class="hljs-string">"index.js"</span>,
  <span class="hljs-attr">"scripts"</span>: &#123;
    <span class="hljs-attr">"dev"</span>: <span class="hljs-string">"webpack --config ./webpack.config.js"</span>
  &#125;,
  <span class="hljs-attr">"keywords"</span>: [],
  <span class="hljs-attr">"author"</span>: <span class="hljs-string">""</span>,
  <span class="hljs-attr">"license"</span>: <span class="hljs-string">"ISC"</span>,
  <span class="hljs-attr">"dependencies"</span>: &#123;
    <span class="hljs-attr">"css-loader"</span>: <span class="hljs-string">"^5.2.6"</span>,
    <span class="hljs-attr">"mini-css-extract-plugin"</span>: <span class="hljs-string">"^1.6.0"</span>,
    <span class="hljs-attr">"webpack"</span>: <span class="hljs-string">"^5.39.1"</span>,
    <span class="hljs-attr">"webpack-cli"</span>: <span class="hljs-string">"^4.7.2"</span>
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>运行指令 <code>npm run dev</code>，<code>wepback</code> 会在根目录新建一个 <code>dist</code> 目录，凡是在 <code>main.js</code> 入口文件中引入的 <code>css</code> 文件，都将会被打包成一个 <code>css</code> 文件，不信你看：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/2269780b9d304714abc4a650294a7acc~tplv-k3u1fbpfcp-zoom-1.image" alt="image-20210619225624130" loading="lazy" referrerpolicy="no-referrer"></p>
<p>此时 <code>main.css</code> 文件中，同时包含了 <code>a.css</code>、<code>b.css</code>、<code>c.css</code>、<code>d.css</code> 四个文件的内容，只要命名不冲突，你可以在你需要的地方，直接引入 <code>main.css</code> 文件。映射文件也保存在main.css.map文件中，如下图所示：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/052de82c5852461694c9e8c689abaf28~tplv-k3u1fbpfcp-zoom-1.image" alt="image-20210619225704661" loading="lazy" referrerpolicy="no-referrer"></p>
<p>本demo的下载地址：<code>https://s.yezgea02.com/1624090152147/webpack-demo.zip</code>，感兴趣的可以下载看一下。</p>
<h2 data-id="heading-2">慕课网涉嫌抄袭和webpack按需加载有什么关系？</h2>
<p>慕课网涉嫌抄袭我的开源项目，这件事情我之前已经发布了多篇文章。最近，也一直在整理起诉的材料，我主要是根据公证材料中的内容来搜集证据。</p>
<ul>
<li><a href="https://juejin.cn/post/6970407663859400718" target="_blank">《newbee-mall开源项目被慕课网拿去做课程，然而我毫不知情，这又是什么骚操作？》</a></li>
<li><a href="https://juejin.cn/post/6970407668716404773" target="_blank">《newbee-mall开源项目被慕课网拿去做课程，项目详细对比记录，更多实锤看这里》</a></li>
<li><a href="https://juejin.cn/post/6970407667198066724" target="_blank">《一个被慕课网拿去做Java就业班终极项目的开源商城项目，推荐给大家》</a></li>
<li><a href="https://juejin.cn/post/6970840573624680484" target="_blank">《花费3680元买了一个慕课网的Java就业班课程，里面竟然有自己写的开源项目！》</a></li>
<li><a href="https://juejin.cn/post/6971891892455899150" target="_blank">《newbee-mall开源项目被慕课网拿去做课程，讲师已道歉，课程却还在售卖》</a></li>
<li><a href="https://juejin.cn/post/6972228181151449102" target="_blank">《可笑！慕课网涉嫌抄袭开源项目至今没有道歉，而且在偷偷的“毁尸灭迹”》</a></li>
</ul>
<p>之前已经比对了项目页面、项目设计等等内容。<strong>律师告诉我，这些证据能够使用，不过最好加上代码的比对。通过项目的视觉效果和代码的重复比例来证明存在抄袭行为，因为我国著作权法对侵犯著作权的判定规则是“接触+实质性相似”，“侵权=接触＋实质性相似”是被普遍接受并在司法实务中执行的规则，属于一般著作权侵权认定的通用标准。</strong></p>
<p><strong>项目的视觉效果和代码的重复比例，如果在这两个方面都有很直接的证据，那么证明慕课网涉嫌抄袭的项目和newbee-mall项目二者存在“实质性相似”就更为有利。所以，我不仅仅在写文章和回复评论，近期主要的精力花在了代码的比对上面，而比对的结果也让人哭笑不得，因为代码的重复度实在太高太高了，很多代码都是直接复制过去的。</strong></p>
<p>而比对代码的时候，就牵涉到了webpack的按需加载技术。</p>
<p>慕课网涉嫌抄袭的课程名称是《Java工程师》，我已经在公证处购买了该课程，购买过程已被公证。同时该课程中涉嫌抄袭的项目代码我也已经下载了，下载过程也被公证。整理证据时用到的就是这份公证后的代码压缩包，在解压后，可以看到项目源码，如下图所示：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/dc75898f70a440899c30f379f2c609b3~tplv-k3u1fbpfcp-zoom-1.image" alt="image-20210619232736460" loading="lazy" referrerpolicy="no-referrer"></p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/a98f07032dc44d7d958f4908044f4819~tplv-k3u1fbpfcp-zoom-1.image" alt="image-20210619232723710" loading="lazy" referrerpolicy="no-referrer"></p>
<p>分别是样式文件和页面文件。我们可以看到，代码都是被处理过的，如果直接打开的话，是很难进行代码比对的。但是通过代码的命名方式和文件大小能够看出，其实这些代码都是被压缩过了，最有可能的方式就是webpack的压缩，命名方式是<code>[name].[hash].chunk.js</code>，也就是在前一小节中的实践代码配置中，加上一个<code>chunkFilename</code>的配置即可。这样的话，首页、搜索页、商品详情页、购物车页面、订单页面等等页面的样式文件和页面代码文件都可以压缩到一个文件中。作为一个开发人员，锤人的方式就比较朴素而直接，直接把原理简单的分析一遍，然后再分析代码。</p>
<p>好的，来。</p>
<h2 data-id="heading-3">慕课网涉嫌抄袭开源项目newbee-mal的代码对比</h2>
<p><strong>之前虽然也发布了不少文章，不过并没有把项目的源码比对发出来。所以，有很多网友在质疑我是炒作、说我是祥林嫂、说这次事件一定会有反转、还说慕课网肯定会拿出证据打我的脸。好吧，我一直在等着反转，一直在等着慕课网打我的脸，但是直到今天也没等到，那我就继续把证据放出来吧。这次的证据比较直接，慕课网上《Java工程师》课程终极项目的代码涉嫌大面积的抄袭newbee-mall。通过项目视觉对比、代码对比可知，页面展示效果相似度达到95%以上，代码重复度达到90%以上，展示效果的比对在之前一篇文章里，这篇文章中的内容主要是代码比对。</strong></p>
<p>好的，大家来长长眼吧！</p>
<p>进入<code>imooc-mall/src/main/resources/static</code>文件夹下，使用浏览器打开该文件夹下的<code>index.html</code>文件，效果如下图所示：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/6543015bdc4948c38c06638eb0262622~tplv-k3u1fbpfcp-zoom-1.image" alt="image-20210618172530962" loading="lazy" referrerpolicy="no-referrer"></p>
<p>在页面上右键点击“检查”或者按住f12键，进入浏览器的控制台。进入<code>Sources</code>面板，并依次点开文件夹至<code>css</code>目录，如下图所示，可以看到慕慕生鲜项目的页面源代码：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/f000e812130c4122aa3e639fde1208ef~tplv-k3u1fbpfcp-zoom-1.image" alt="image-20210618175145712" loading="lazy" referrerpolicy="no-referrer"></p>
<p>上述<code>static/static/css</code>目录中的文件在源代码中是看不到的，不过，这不代表这些文件不存在，而是代码被压缩了。源代码文件中的<code>main.9a3b9d8e.chunk.css</code>文件就是这些文件压缩后的文件，浏览器在渲染页面时将通过<code>main.9a3b9d8e.chunk.css.map</code>文件对源代码进行按需加载。所以这些源代码并不是不存在，而是被压缩了。<code>main.9a3b9d8e.chunk.css.map</code>文件就维护了文件的映射关系，打开文件可以看到映射配置：</p>
<pre><code class="hljs language-js copyable" lang="js">&#123;<span class="hljs-string">"version"</span>:<span class="hljs-number">3</span>,<span class="hljs-string">"sources"</span>:[<span class="hljs-string">"index.css"</span>,<span class="hljs-string">"App.css"</span>,<span class="hljs-string">"login.css"</span>,<span class="hljs-string">"header.css"</span>,<span class="hljs-string">"pay.css"</span>,<span class="hljs-string">"main.9a3b9d8e.chunk.css"</span>,<span class="hljs-string">"iconfont.css"</span>,<span class="hljs-string">"common.css"</span>,<span class="hljs-string">"cart.css"</span>,<span class="hljs-string">"sweetalert.css"</span>,<span class="hljs-string">"detail.css"</span>,<span class="hljs-string">"index.scss"</span>,<span class="hljs-string">"header.scss"</span>,<span class="hljs-string">"detail.scss"</span>,<span class="hljs-string">"personal.css"</span>,<span class="hljs-string">"my-orders.css"</span>,<span class="hljs-string">"bootstrap-modal.css"</span>,<span class="hljs-string">"order-detail.css"</span>,<span class="hljs-string">"order-settle.css"</span>,<span class="hljs-string">"order-detail.scss"</span>,<span class="hljs-string">"pay-select.css"</span>,<span class="hljs-string">"personal.scss"</span>,<span class="hljs-string">"search.css"</span>],<span class="hljs-string">"names"</span>:[]
<span class="copy-code-btn">复制代码</span></code></pre>
<p>所有这些源文件的代码都被压缩进<code>main.9a3b9d8e.chunk.css</code>文件中。</p>
<p>好的，接下来，依次通过浏览器点开这些文件，并与newbee-mall项目中的文件对比：</p>
<h4 data-id="heading-4">index.css代码比对</h4>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/738361a911194dbfb914e46dd3ce01f9~tplv-k3u1fbpfcp-zoom-1.image" alt="image-20210618180340678" loading="lazy" referrerpolicy="no-referrer"></p>
<p>上图中是慕慕生鲜项目中的<code>index.css</code>源文件，下方为newbee-mall项目中的<code>index.css</code>源文件：</p>
<pre><code class="hljs language-css copyable" lang="css"><span class="hljs-selector-class">.all-sort-list</span> &#123;
    <span class="hljs-attribute">position</span>: relative;
    <span class="hljs-attribute">float</span>: left;
    <span class="hljs-attribute">width</span>: <span class="hljs-number">228px</span>;
    <span class="hljs-attribute">border-top</span>: none;
    <span class="hljs-attribute">background</span>: <span class="hljs-number">#000</span>;
    <span class="hljs-attribute">height</span>: <span class="hljs-number">100%</span>;
&#125;

<span class="hljs-selector-class">.all-sort-list</span> <span class="hljs-selector-class">.item</span> &#123;
    <span class="hljs-attribute">height</span>: <span class="hljs-number">49px</span>;
    <span class="hljs-attribute">border-top</span>: <span class="hljs-number">1px</span> solid <span class="hljs-number">#FFFFFF</span>;
&#125;

<span class="hljs-selector-class">.all-sort-list</span> <span class="hljs-selector-class">.item</span><span class="hljs-selector-class">.bo</span> &#123;
    <span class="hljs-attribute">border-top</span>: none;
&#125;

<span class="hljs-selector-class">.all-sort-list</span> <span class="hljs-selector-class">.item</span> <span class="hljs-selector-tag">h3</span> &#123;
    <span class="hljs-attribute">height</span>: <span class="hljs-number">30px</span>;
    <span class="hljs-attribute">line-height</span>: <span class="hljs-number">45px</span>;
    <span class="hljs-attribute">font-size</span>: <span class="hljs-number">15px</span>;
    <span class="hljs-attribute">font-weight</span>: normal;
    <span class="hljs-attribute">width</span>: <span class="hljs-number">199px</span>;
    <span class="hljs-attribute">overflow</span>: hidden;
&#125;

<span class="hljs-selector-class">.all-sort-list</span> <span class="hljs-selector-class">.item</span> <span class="hljs-selector-tag">span</span> &#123;
    <span class="hljs-attribute">padding</span>: <span class="hljs-number">0px</span> <span class="hljs-number">5px</span>;
    <span class="hljs-attribute">color</span>: <span class="hljs-number">#1baeae</span>;
    <span class="hljs-attribute">font-family</span>: <span class="hljs-string">"\5B8B\4F53"</span>;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这里只提供了前50行的代码对比，完整的源码对比将整理在另外的附件中，作为证据材料。</p>
<p>最终的比对结论：文件名称一模一样，代码重复度为98%，完完全全的抄袭行为！</p>
<h4 data-id="heading-5">header.css代码比对</h4>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/e7dcdf33ef1f485fb984fbdbb5df4dab~tplv-k3u1fbpfcp-zoom-1.image" alt="image-20210618181016359" loading="lazy" referrerpolicy="no-referrer"></p>
<p>上图中是慕慕生鲜项目中的<code>header.css</code>源文件，下方为newbee-mall项目中的<code>header.css</code>源文件：</p>
<pre><code class="hljs language-css copyable" lang="css"><span class="hljs-selector-id">#header</span> &#123;
    <span class="hljs-attribute">display</span>: flex;
    <span class="hljs-attribute">justify-content</span>: center;
    <span class="hljs-attribute">width</span>: <span class="hljs-number">100%</span>;
    <span class="hljs-attribute">height</span>: <span class="hljs-number">40px</span>;
    <span class="hljs-attribute">background-color</span>: <span class="hljs-number">#333</span>;
&#125;

<span class="hljs-selector-id">#header</span> <span class="hljs-selector-class">.center</span> &#123;
    <span class="hljs-attribute">width</span>: <span class="hljs-number">1226px</span>;
    <span class="hljs-attribute">height</span>: <span class="hljs-number">40px</span>;
    <span class="hljs-attribute">flex-shrink</span>: <span class="hljs-number">0</span>;
    <span class="hljs-attribute">display</span>: flex;
    <span class="hljs-attribute">justify-content</span>: space-between;
    <span class="hljs-attribute">align-items</span>: center;
&#125;

<span class="hljs-selector-id">#header</span> <span class="hljs-selector-class">.center</span> <span class="hljs-selector-tag">ul</span> <span class="hljs-selector-tag">li</span> <span class="hljs-selector-tag">a</span> &#123;
    <span class="hljs-attribute">display</span>: flex;
    <span class="hljs-attribute">align-items</span>: center;
    <span class="hljs-attribute">height</span>: <span class="hljs-number">12px</span>;
    <span class="hljs-attribute">font-size</span>: <span class="hljs-number">14px</span>;
    <span class="hljs-attribute">color</span>: <span class="hljs-number">#b0b0b0</span>;
    <span class="hljs-attribute">padding</span>: <span class="hljs-number">0</span> <span class="hljs-number">8px</span>;
    <span class="hljs-attribute">border-right</span>: <span class="hljs-number">1px</span> solid <span class="hljs-number">#b0b0b0</span>;
&#125;

<span class="hljs-selector-id">#header</span> <span class="hljs-selector-class">.center</span> <span class="hljs-selector-tag">ul</span> <span class="hljs-selector-tag">li</span><span class="hljs-selector-pseudo">:last-of-type</span> <span class="hljs-selector-tag">a</span> &#123;
    <span class="hljs-attribute">border-right</span>: none;
&#125;

<span class="hljs-selector-id">#header</span> <span class="hljs-selector-class">.center</span> <span class="hljs-selector-class">.fl</span> &#123;
    <span class="hljs-attribute">flex-shrink</span>: <span class="hljs-number">0</span>;
    <span class="hljs-attribute">display</span>: flex;
    <span class="hljs-attribute">width</span>: <span class="hljs-number">680px</span>;
&#125;

<span class="hljs-selector-id">#header</span> <span class="hljs-selector-class">.center</span> <span class="hljs-selector-class">.fr</span> &#123;
    <span class="hljs-attribute">display</span>: flex;
    <span class="hljs-attribute">height</span>: <span class="hljs-number">40px</span>;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这里只提供了前40行的代码对比，完整的源码对比将整理在另外的附件中，作为证据材料。</p>
<p>最终的比对结论：文件名称一模一样，代码重复度为99%，完完全全的抄袭行为！</p>
<h4 data-id="heading-6">login.css代码比对</h4>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/6881a2a914884f26a09661622c8d1ae2~tplv-k3u1fbpfcp-zoom-1.image" alt="image-20210618181016359" loading="lazy" referrerpolicy="no-referrer"></p>
<p>上图中是慕慕生鲜项目中的<code>login.css</code>源文件，下方为newbee-mall项目中的<code>login.css</code>源文件：</p>
<pre><code class="hljs language-css copyable" lang="css"><span class="hljs-selector-tag">body</span> &#123;
    <span class="hljs-attribute">background</span>: <span class="hljs-number">#14212a</span>;
&#125;

<span class="hljs-selector-class">.top</span> &#123;
    <span class="hljs-attribute">width</span>: <span class="hljs-number">100%</span>;
    <span class="hljs-attribute">height</span>: <span class="hljs-number">100px</span>;
    <span class="hljs-attribute">background</span>: <span class="hljs-number">#fff</span>;
&#125;

<span class="hljs-selector-class">.top</span> <span class="hljs-selector-class">.logo</span> &#123;
    <span class="hljs-attribute">width</span>: <span class="hljs-number">1130px</span>;
    <span class="hljs-attribute">height</span>: <span class="hljs-number">160px</span>;
&#125;

<span class="hljs-selector-class">.top</span> <span class="hljs-selector-class">.logo</span> <span class="hljs-selector-tag">img</span> &#123;
    <span class="hljs-attribute">border</span>: none;
    <span class="hljs-attribute">margin-top</span>: -<span class="hljs-number">15px</span>;
&#125;

<span class="hljs-selector-class">.form</span> &#123;
    <span class="hljs-attribute">width</span>: <span class="hljs-number">1130px</span>;
    <span class="hljs-attribute">height</span>: <span class="hljs-number">588px</span>;
    <span class="hljs-attribute">background</span>: <span class="hljs-built_in">url</span>(<span class="hljs-string">"../image/login_bg.png"</span>) no-repeat center center;
&#125;

<span class="hljs-selector-class">.form</span> <span class="hljs-selector-class">.login</span> &#123;
    <span class="hljs-attribute">width</span>: <span class="hljs-number">400px</span>;
    <span class="hljs-attribute">height</span>: <span class="hljs-number">470px</span>;
    <span class="hljs-attribute">margin</span>: <span class="hljs-number">30px</span> auto;
    <span class="hljs-attribute">background</span>: <span class="hljs-number">#444</span>;
    <span class="hljs-attribute">color</span>: <span class="hljs-number">#fff</span>;
    <span class="hljs-attribute">margin-right</span>: <span class="hljs-number">0px</span>;
    <span class="hljs-attribute">border-radius</span>: <span class="hljs-number">4px</span>;
    <span class="hljs-attribute">font</span>: <span class="hljs-number">12px</span> <span class="hljs-string">"宋体"</span>, Times New Roman;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这里只提供了前36行的代码对比，完整的源码对比将整理在另外的附件中，作为证据材料。</p>
<p>最终的比对结论：文件名称一模一样，代码重复度为99%，完完全全的抄袭行为！</p>
<p>除以上列举的代码抄袭外，还有<code>detail.css</code>文件、<code>cart.css</code>文件、<code>personal.css</code>文件、<code>common.css</code>文件、<code>search.css</code>文件、<code>my-orders.css</code>文件、<code>order-detail.css</code>文件、<code>order-settle.css</code>文件、<code>pay.css</code>文件、<code>pay-select.css</code>文件，这些文件的代码重复度也基本都达到了100%，完整的源码对比将整理在另外的附件中，作为证据材料。</p>
<p>页面的样式代码是完全的抄袭，newbee-mall项目的页面代码也被大面积的抄袭。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/17e22d65822b4378a82a16c8065d889c~tplv-k3u1fbpfcp-zoom-1.image" alt="image-20210619002311717" loading="lazy" referrerpolicy="no-referrer"></p>
<p>上图中<code>static/static/js/pages</code>目录中的文件就是慕慕生鲜各个页面的源代码，这部分代码在源文件中也是无法直接看到的，同样进行了压缩处理。源代码文件中的<code>main.ed04a20c.chunk.js</code>文件就是这些文件压缩后的文件，浏览器在渲染页面时将通过<code>main.ed04a20c.chunk.js.map</code>文件对源代码进行按需加载。所以这些源代码并不是不存在，而是被压缩了。<code>main.ed04a20c.chunk.js.map</code>文件就维护了文件的映射关系，打开文件可以看到映射配置：</p>
<pre><code class="hljs language-js copyable" lang="js">&#123;<span class="hljs-string">"version"</span>:<span class="hljs-number">3</span>,<span class="hljs-string">"sources"</span>:[<span class="hljs-string">"assets/image/login-logo-2.png"</span>,<span class="hljs-string">"assets/logo2.png"</span>,<span class="hljs-string">"assets/image/pay/payOnline_zsyh.png"</span>,<span class="hljs-string">"assets/image/pay/payOnline_gsyh.png"</span>,<span class="hljs-string">"assets/image/pay/payOnline_jsyh.png"</span>,<span class="hljs-string">"assets/image/pay/payOnline_jtyh.png"</span>,<span class="hljs-string">"assets/image/pay/payOnline_zgyh.png"</span>,<span class="hljs-string">"assets/image/pay/payOnline_gdyh.png"</span>,<span class="hljs-string">"assets/image/pay/payOnline_xyyh.png"</span>,<span class="hljs-string">"assets/logogif.gif"</span>,<span class="hljs-string">"assets/11.jpg"</span>,<span class="hljs-string">"assets/image/7d.jpg"</span>,<span class="hljs-string">"assets/image/hua.png"</span>,<span class="hljs-string">"assets/image/card.png"</span>,<span class="hljs-string">"assets/image/ji.png"</span>,<span class="hljs-string">"assets/banner10.jpg"</span>,<span class="hljs-string">"assets/banner11.jpg"</span>,<span class="hljs-string">"assets/banner12.jpg"</span>,<span class="hljs-string">"assets/image/pay/payOnline_zfb.png"</span>,<span class="hljs-string">"assets/image/pay/weixinpay.png"</span>,<span class="hljs-string">"assets/image/pay/unionpay.png"</span>,<span class="hljs-string">"assets/image/pay/payOnline_nyyh.png"</span>,<span class="hljs-string">"assets/image/pay/payOnline_youzheng.png"</span>,<span class="hljs-string">"assets/image/pay/payOnline_gfyh.png"</span>,<span class="hljs-string">"assets/image/pay/payOnline_pufa.png"</span>,<span class="hljs-string">"assets/image/pay/payOnline_zxyh.png"</span>,<span class="hljs-string">"assets/image/pay/payOnline_shncsyyh.png"</span>,<span class="hljs-string">"assets/image/pay/payOnline_jiangsshuyh.png"</span>,<span class="hljs-string">"assets/image/pay/wxpay_qrcode.png"</span>,<span class="hljs-string">"logo.svg"</span>,<span class="hljs-string">"assets/image/pay/alipay_qrcode.png"</span>,<span class="hljs-string">"assets/image/sub_banner/r4.jpg"</span>,<span class="hljs-string">"assets/image/sub_banner/hot2.jpg"</span>,<span class="hljs-string">"assets/image/sub_banner/hot3.jpg"</span>,<span class="hljs-string">"assets/image/sub_banner/hot4.jpg"</span>,<span class="hljs-string">"assets/image/sub_banner/m6.jpg"</span>,<span class="hljs-string">"assets/image/sub_banner/headphones.jpg"</span>,<span class="hljs-string">"assets/image/sub_banner/pc.jpg"</span>,<span class="hljs-string">"assets/image/sub_banner/air.jpg"</span>,<span class="hljs-string">"assets/image/sub_banner/baby-car.jpg"</span>,<span class="hljs-string">"assets/image/sub_banner/r1.jpg"</span>,<span class="hljs-string">"assets/image/sub_banner/r2.jpg"</span>,<span class="hljs-string">"assets/image/sub_banner/r3.jpg"</span>,<span class="hljs-string">"assets/image/sub_banner/r5.jpg"</span>,<span class="hljs-string">"assets/image/sub_banner/r6.jpg"</span>,<span class="hljs-string">"../node_modules/moment-mini/locale sync /^/.//.*$"</span>,<span class="hljs-string">"assets/image/search/right-@1x.png"</span>,<span class="hljs-string">"http.js"</span>,<span class="hljs-string">"api.js"</span>,<span class="hljs-string">"pages/login.js"</span>,<span class="hljs-string">"pages/alipay.js"</span>,<span class="hljs-string">"pages/footer.js"</span>,<span class="hljs-string">"pages/cart.js"</span>,<span class="hljs-string">"pages/components/header-fragment.js"</span>,<span class="hljs-string">"pages/components/nav-fragment.js"</span>,<span class="hljs-string">"pages/detail.js"</span>,<span class="hljs-string">"pages/header.js"</span>,<span class="hljs-string">"pages/index.js"</span>,<span class="hljs-string">"pages/personal-sidebar.js"</span>,<span class="hljs-string">"pages/my-orders.js"</span>,<span class="hljs-string">"pages/order-detail.js"</span>,<span class="hljs-string">"http2.js"</span>,<span class="hljs-string">"pages/order-settle.js"</span>,<span class="hljs-string">"pages/pay-select.js"</span>,<span class="hljs-string">"pages/personal.js"</span>,<span class="hljs-string">"pages/register.js"</span>,<span class="hljs-string">"pages/search.js"</span>,<span class="hljs-string">"pages/wxpay.js"</span>,<span class="hljs-string">"App.js"</span>,<span class="hljs-string">"serviceWorker.js"</span>,<span class="hljs-string">"index.js"</span>]
<span class="copy-code-btn">复制代码</span></code></pre>
<p>慕慕生鲜所有页面源文件的代码都被压缩进<code>main.ed04a20c.chunk.js.map</code>文件中。</p>
<p>好的，接下来，依次通过浏览器点开这些文件，并与newbee-mall项目中的文件对比。</p>
<h4 data-id="heading-7">首页代码比对</h4>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/ea48ca1586304ec790a4a76141a54c6f~tplv-k3u1fbpfcp-zoom-1.image" alt="image-20210619002811496" loading="lazy" referrerpolicy="no-referrer"></p>
<p>上图中是慕慕生鲜项目中index页面的源文件，下方为newbee-mall项目中index页面的源文件：</p>
<pre><code class="hljs language-css copyable" lang="css">    <<span class="hljs-selector-tag">div</span> id="banner">
        <<span class="hljs-selector-tag">div</span> class="all-sort-list">
            <<span class="hljs-selector-tag">th</span>:block th:each=<span class="hljs-string">"category : $&#123;categories&#125;"</span>>
            <div class=<span class="hljs-string">"item"</span>>
                <h3><span>·</span><a href=<span class="hljs-string">"##"</span>><th:block th:text=<span class="hljs-string">"$&#123;category.categoryName&#125;"</span>></th:block></a></h3>
                <div class=<span class="hljs-string">"item-list clearfix"</span>>
                    <div class=<span class="hljs-string">"subitem"</span>>
                        <th:block th:each=<span class="hljs-string">"secondLevelCategory : $&#123;category.secondLevelCategoryVOS&#125;"</span>>
                        <dl class=<span class="hljs-string">"fore1"</span>>
                            <dt><a href=<span class="hljs-string">"#"</span>><th:block th:text=<span class="hljs-string">"$&#123;secondLevelCategory.categoryName&#125;"</span>></th:block></a></dt>
                            <dd>
                                <th:block th:each=<span class="hljs-string">"thirdLevelCategory : $&#123;secondLevelCategory.thirdLevelCategoryVOS&#125;"</span>>
                                <em><a href=<span class="hljs-string">"#"</span>th:href=<span class="hljs-string">"@&#123;'/search?goodsCategoryId='+$&#123;thirdLevelCategory.categoryId&#125;&#125;"</span>>
                                    <th:block th:text=<span class="hljs-string">"$&#123;thirdLevelCategory.categoryName&#125;"</span>></th:block>
                                </a></em>
                                </th:block>
                            </dd>
                        </dl>
                        </th:block>
                    </div>
                </div>
            </div>
            </th:block>
        </div>
        <div class=<span class="hljs-string">"swiper-container fl"</span>>
            <div class=<span class="hljs-string">"swiper-wrapper"</span>>
                <!-- 配置了轮播图则显示后台配置的轮播图 -->
                <th:block th:unless=<span class="hljs-string">"$&#123;#lists.isEmpty(carousels)&#125;"</span>>
                    <th:block th:each=<span class="hljs-string">"carousel : $&#123;carousels&#125;"</span>>
                        <div class=<span class="hljs-string">"swiper-slide"</span>>
                            <a th:href=<span class="hljs-string">"@&#123;$&#123;carousel.redirectUrl&#125;&#125;"</span>>
                                <img th:src=<span class="hljs-string">"@&#123;$&#123;carousel.carouselUrl&#125;&#125;"</span> alt=<span class="hljs-string">""</span>>
                            </a>
                        </div>
                    </th:block>
                </th:block>
                <!-- 未配置轮播图则显示默认的三张轮播图 -->
                <th:block th:if=<span class="hljs-string">"$&#123;#lists.isEmpty(carousels)&#125;"</span>>
                    <div class=<span class="hljs-string">"swiper-slide"</span>>
                        <img src=<span class="hljs-string">"./mall/image/swiper/banner01.jpg"</span> alt=<span class="hljs-string">""</span>>
                    </div>
                    <div class=<span class="hljs-string">"swiper-slide"</span>>
                        <img src=<span class="hljs-string">"./mall/image/swiper/banner02.jpg"</span> alt=<span class="hljs-string">""</span>>
                    </div>
                    <div class=<span class="hljs-string">"swiper-slide"</span>>
                        <img src=<span class="hljs-string">"./mall/image/swiper/banner03.jpg"</span> alt=<span class="hljs-string">""</span>>
                    </div>
                </th:block>
            </div>
            <div class=<span class="hljs-string">"swiper-pagination"</span>></div>
            <div class=<span class="hljs-string">"swiper-button-prev"</span>></div>
            <div class=<span class="hljs-string">"swiper-button-next"</span>></div>
        </div>
    </div>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这里只提供了前63行的代码对比，完整的源码对比将整理在另外的附件中，作为证据材料。</p>
<p>最终的比对结论：代码重复度为80%以上，不仅仅抄袭页面代码，连开发时写的注释也都复制过来，这是完完全全的抄袭行为！</p>
<h4 data-id="heading-8">商品详情页代码比对</h4>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/4920cb5262dd4c748d0257cae87054d5~tplv-k3u1fbpfcp-zoom-1.image" alt="image-20210619003159322" loading="lazy" referrerpolicy="no-referrer"></p>
<p>上图中是慕慕生鲜项目中商品页面的源文件，下方为newbee-mall项目中商品详情页面的源文件：</p>
<pre><code class="hljs language-css copyable" lang="css"><<span class="hljs-selector-tag">div</span> id="detail">
    <!-- <span class="hljs-selector-tag">nav</span> -->
    <<span class="hljs-selector-tag">nav</span> <span class="hljs-selector-tag">th</span>:replace=<span class="hljs-string">"mall/header::nav-fragment"</span>></nav>

    <div class=<span class="hljs-string">"dc"</span>>
        <div class=<span class="hljs-string">"content w"</span>>
            <div class=<span class="hljs-string">"title fl"</span>>商品详情</div>
            <div class=<span class="hljs-string">"clear"</span>></div>
        </div>
    </div>

    <div class=<span class="hljs-string">"intro mt20 w clearfix"</span>>
        <div class=<span class="hljs-string">"left fl"</span> style=<span class="hljs-string">"position: relative;"</span>>
            <div class=<span class="hljs-string">"swiper-container fl"</span>>
                <img th:src=<span class="hljs-string">"@&#123;$&#123;goodsDetail.goodsCoverImg&#125;&#125;"</span>>
            </div>
        </div>
        <div class=<span class="hljs-string">"right fr"</span>>
            <div class=<span class="hljs-string">"h3 ml20 mt20"</span> th:text=<span class="hljs-string">"$&#123;goodsDetail.goodsName&#125;"</span>>NewBeeMall</div>
            <div class=<span class="hljs-string">"sub_title mr40 ml20 mt10"</span> th:text=<span class="hljs-string">"$&#123;goodsDetail.goodsIntro&#125;"</span>>NewBeeMall</div>
            <div class=<span class="hljs-string">"item_price mr40 ml20 mt10"</span>>
                <th:block th:text=<span class="hljs-string">"$&#123;goodsDetail.sellingPrice&#125;+'.00 元'"</span>></th:block>
                <del>
                    <th:block th:text=<span class="hljs-string">"$&#123;goodsDetail.originalPrice&#125;+'.00 元'"</span>></th:block>
                </del>
            </div>

            <div class=<span class="hljs-string">"order"</span>>
                <input class=<span class="hljs-string">"car"</span> type=<span class="hljs-string">"button"</span> th:onclick=<span class="hljs-string">"'saveAndGoCart('+$&#123;goodsDetail.goodsId&#125;+')'"</span> value=<span class="hljs-string">"立即选购"</span>/>
                <input class=<span class="hljs-string">"car"</span> type=<span class="hljs-string">"button"</span> th:onclick=<span class="hljs-string">"'saveToCart('+$&#123;goodsDetail.goodsId&#125;+')'"</span> value=<span class="hljs-string">"加入购物车"</span>/>
            </div>
            <div class=<span class="hljs-string">"tb-extra ml20"</span> id=<span class="hljs-string">"J_tbExtra"</span>>
                <dl>
                    <dt>承诺</dt>
                    <dd><a class=<span class="hljs-string">"J_Cont"</span> title=<span class="hljs-string">"满足7天无理由退换货申请的前提下，包邮商品需要买家承担退货邮费，非包邮商品需要买家承担发货和退货邮费。"</span> href=<span class="hljs-string">"#"</span>
                           target=<span class="hljs-string">"_blank"</span>><img th:src=<span class="hljs-string">"@&#123;/mall/image/7d.jpg&#125;"</span>><span class="hljs-number">7</span>天无理由</a></dd>
                </dl>
                <dl>
                    <dt>支付</dt>
                    <dd><a href=<span class="hljs-string">"##"</span> target=<span class="hljs-string">"_blank"</span>><img th:src=<span class="hljs-string">"@&#123;/mall/image/hua.png&#125;"</span>>蚂蚁花呗</a><a href=<span class="hljs-string">"##"</span>
                                                                                                     target=<span class="hljs-string">"_blank"</span>><img
                            th:src=<span class="hljs-string">"@&#123;/mall/image/card.png&#125;"</span>>信用卡支付</a><a href=<span class="hljs-string">"##"</span> target=<span class="hljs-string">"_blank"</span>><img
                            th:src=<span class="hljs-string">"@&#123;/mall/image/ji.png&#125;"</span>>集分宝</a></dd>
                </dl>
                <dl>
                    <dt>支持</dt>
                    <dd>折旧变现，买新更省钱。<a style=<span class="hljs-string">"float:none;text-decoration: underline;"</span> href=<span class="hljs-string">"##"</span>>详情</a></dd>
                </dl>

            </div>
        </div>
        <div class=<span class="hljs-string">"clear"</span>></div>
    </div>
    <!-- 这里使用的是 th:utext 标签，用 th:text 不会解析 html，用 th:utext 会解析 html -->
    <div class=<span class="hljs-string">"goods mt20 w clearfix"</span> th:utext=<span class="hljs-string">"$&#123;goodsDetail.goodsDetailContent&#125;"</span>>
    </div>
</div>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这里只提供了前65行的代码对比，完整的源码对比将整理在另外的附件中，作为证据材料。</p>
<p>最终的比对结论：代码重复度为90%以上，不仅仅抄袭页面代码，连文案也完完整整的抄袭，这是赤裸裸的抄袭行为！</p>
<p>除以上列举的代码抄袭外，还有<code>login.js</code>文件、<code>register.js</code>文件、<code>header.js</code>文件、<code>search.js</code>文件、<code>cart.js</code>文件、<code>personal.js</code>文件、<code>personal-sidebar.js</code>文件、<code>pay-select.js</code>文件、<code>order-settle.js</code>文件、<code>my-orders.js</code>文件、<code>order-detail.js</code>文件、<code>order-settle.js</code>文件、<code>alipay.js</code>文件、<code>weixin-pay.js</code>文件，这些文件的代码重复度也基本都达到了90%以上，完整的源码对比将整理在另外的附件中，作为证据材料。</p>
<h2 data-id="heading-9">大家关心的问题，统一答疑</h2>
<h4 data-id="heading-10">开源项目不是谁都能用的吗？</h4>
<p>这个问题还真的有不少人问。</p>
<p>话这么说没错，开源项目本身就是把所有的代码都开放了出去，所以所有人都能够拿去用是没错的。包括newbee-mall这个项目也是如此，你可以下载所有的代码、源文件，可以用来学习，也可以用来做东西。</p>
<p>但是，项目开源了，不代表作者把所有权利都放弃了。无规矩不成方圆，改个logo，改个名字，说是自己的项目，这就不行了。慕慕生鲜这次涉嫌抄袭的行为就是绝对有问题的，源码拿去改掉、项目名称改掉、项目LOGO改掉、原作者的所有版权信息删除、声称是自己的原创项目，这就是犯法的行为。拿起筷子吃饭，放下筷子骂娘，这种行为是要鄙视的。</p>
<p><strong>换一个角度来说，如果newbee-mall项目的作者是你，遇到这种行为，你该怎么做呢？</strong></p>
<h4 data-id="heading-11">为什么一直在发文章？发文章有用吗？</h4>
<p>有用啊！</p>
<p>不发文章，被抄袭和剽窃的痛无处抒发，我只能被人白白的欺负。</p>
<p>不发文章，技术圈内的人会知道这件事吗？现在 ，很多人都知道这件事的前因后果了，也得到了大多数人的支持，谢谢你们。</p>
<p>不发文章，慕课网会删改课程内容吗？现在，他们怕了，已经把课程内容中涉嫌侵权的内容全部“毁尸灭迹”了。</p>
<p>不发文章，我会收到道歉吗？现在，我只收到了一份疑似讲师的道歉，慕课网的道歉，我等你哦！</p>
<p>不发文章，慕课网的法务会联系我的律师吗？现在，双方已经在沟通了，不过对方还是那么的傲娇，涉嫌犯法的是你，好不好？！！搞不清楚状况吗？</p>
<h4 data-id="heading-12">怎么天天看到你发的文章，就只会抱怨，怎么像祥林嫂一样的？</h4>
<p>并没有天天发文章，现在还是一周一篇文章的节奏，和之前一样，顺带着会提一下这个事情。</p>
<p>我和祥林嫂不同的，虽然我们面对的情况都是被“恶狼”抢走了孩子，但是我一直在行动，一直在发声。而且，并没有抱怨，我一直在讲解前因后果和过程中发生的事情，就事论事而已。另外，我从一开始就做了很多的维权行动，搜集证据、公证、证据保全、找律师、准备起诉材料。所以，这并不是被抄袭和剽窃后的抱怨，大家也不能这样理解。我的一切行为都是为了维权，而且我也一直在实实在在的做维权的事情。预计在7月份之前就会起诉了，这周或者下周吧。</p>
<h4 data-id="heading-13">就只会天天发文章，你就不能直接起诉吗？</h4>
<p><strong>路要一步一步走。</strong></p>
<p>你们是不是觉得所有事情都能在瞬间就可以做完啊？起诉像是喘口气那么简单的吗？</p>
<p>从我知道这件事情到今天也就一个月时间，前面半个月是在确认抄袭行为存不存在和找律师。实际的曝光和整理证据材料都是从六月份中旬开始做的，而且已经做了很多诉前准备，只是这些材料和证据的整理要花时间啊。整理完成后，就会实际的去法院起诉了。</p>
<h4 data-id="heading-14">就只看到你一个人说，慕课网一句话都不说，你肯定有鬼！</h4>
<p>哈哈哈哈哈哈哈哈。</p>
<p>这种话，虽然说的人少，但是还真的有几个人这么给我留言了！还是统一回复下吧，我没办法让慕课网说话，因为我也在等着他们的回复呢！但是他们就一直不回复啊，就硬挺着啊。</p>
<p><strong>不过，我肯定会一直发声的，他们要是能挺就一直挺着好了。我会尽我所能，让越来越多人知道这件事，看清楚某些平台的嘴脸。还有，他们不可能一直都不发声的，后面起诉了，就法庭上见咯。他们在法庭上一句话也不说？不可能吧。</strong></p>
<h4 data-id="heading-15">就你一个人在叭叭的说，肯定会反转，等你啪啪打脸！</h4>
<p>正常人都能够看出来我发声的目的就是维权，而不是撕逼。我只是把维权的事情记录下来，从发现被侵权，到开始维权，再到维权的准备工作和维权的实际做法，还有维权的过程，最后是维权的结果和总结。我不想和任何人撕逼，我只是记录发生在我身上的事情而已，没有违反任何技术社区的发文规范，完全符合各个技术社区的要求，我想发多少就发多少。</p>
<p>其实，过程中我也有过胡思乱想的时候，就是这件事情会有反转吗？</p>
<p>目前来看，概率极小。首先是证据方面，从我自身掌握的证据以及我发布的文章中可以看出，这次慕课网涉嫌抄袭的证据越来越完整和完善。包括但不限于页面设计抄袭、创意抄袭、代码抄袭、文案抄袭。通过项目视觉对比、代码对比可知，页面展示效果相似度达到95%以上，代码重复度达到90%以上，涉嫌抄袭的行为是蓄意且主动的，而且还删除了该项目中关于我的版权信息并说是自己的原创项目。以上这些都是公证材料中整理出来的证据。</p>
<p><strong>其次，是慕课网这段时间的行为和态度。自从我曝光这件事情后，慕课网已经连夜“升级”了《Java工程师》课程，我提到的能够看出来的地方已经被全部删除了。对，在我眼皮子底下做的“毁尸灭迹”，看到这种掩耳盗铃的行为，我也是笑了挺久的。双方行为和态度的差别，大家应该也能够很直观的看出来。</strong></p>
<p>我会让这件事情笔直且顺利的进展下去，不会让它发生反转的。</p>
<h2 data-id="heading-16">总结</h2>
<p>证据、材料都快整理好了，起诉书也让律师开始准备了。期待事件反转的人啊，让你们失望了。</p>
<p><strong>慕课网作为国内IT教育平台的执牛耳者，应该高高地扛起保护知识产权的大旗，应该维护原创者的合法权益，应该严厉地打击抄袭、剽窃、盗版等行为，应该给同行们做好表率。千万不要试图以高高在上的姿态侵犯一个开发者的合法知识产权，决不能助长这种不正之风。慕课网，你手中的剑应该指向“恶龙”啊！</strong></p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/5ecd46c40b0a4e2c82e688b47b0d0074~tplv-k3u1fbpfcp-zoom-1.image" alt="img" loading="lazy" referrerpolicy="no-referrer"></p>
<p>我是程序员十三。关于慕课网无通知无授权的情况下改造我的开源项目newbee-mall并进行上线售卖的事件，我不止写了这一篇文章，也不止在一个平台上发布。这些文章我已经在十三个平台上同步发表，包括今日头条、微信公众号、微博、知乎、哔哩哔哩、掘金、博客园、CSDN、InfoQ写作平台、思否、51CTO、开源中国OSCHINA、腾讯云+社区，账号名称都是“程序员十三”。</p>
<p>后续我会一直在我的微信公众号里发声，关注我即可查看事件详情和最新进展，毕竟在其它平台可能文章会莫名其妙的就“没”了。也希望各位看到文章的朋友能帮忙转发，再次感谢大家。</p>
<p><strong>如果有需要转载的朋友，注明来源即可转载，或者可以联系我进行文章授权。</strong></p>
<p>一直在发文章，也有很多朋友建议我做视频发到各个视频平台。我只会录屏，剪辑和视频处理并不会，如果对这件事情有兴趣且具有剪辑能力的朋友可以联系我，我提供所有素材，对这件事进行曝光和维权记录，发布到各个视频平台。</p>
<p>2021年6月6日，是我第一次针对这次事件的发声，之后陆陆续续共发布了六篇文章：</p>
<ul>
<li><a href="https://juejin.cn/post/6970407663859400718" target="_blank">《newbee-mall开源项目被慕课网拿去做课程，然而我毫不知情，这又是什么骚操作？》</a></li>
<li><a href="https://juejin.cn/post/6970407668716404773" target="_blank">《newbee-mall开源项目被慕课网拿去做课程，项目详细对比记录，更多实锤看这里》</a></li>
<li><a href="https://juejin.cn/post/6970407667198066724" target="_blank">《一个被慕课网拿去做Java就业班终极项目的开源商城项目，推荐给大家》</a></li>
<li><a href="https://juejin.cn/post/6970840573624680484" target="_blank">《花费3680元买了一个慕课网的Java就业班课程，里面竟然有自己写的开源项目！》</a></li>
<li><a href="https://juejin.cn/post/6971891892455899150" target="_blank">《newbee-mall开源项目被慕课网拿去做课程，讲师已道歉，课程却还在售卖》</a></li>
<li><a href="https://juejin.cn/post/6972228181151449102" target="_blank">《可笑！慕课网涉嫌抄袭开源项目至今没有道歉，而且在偷偷的“毁尸灭迹”》</a></li>
</ul>
<p>2021年6月21日，是我第五次针对这次事件的发声，也就是当前各位朋友在看到这篇文章。后续我也会继续更新这次维权事件。</p>
<blockquote>
<p>除注明转载/出处外，皆为作者原创，欢迎转载，但未经作者同意必须保留此段声明，且在文章页面明显位置给出原文链接，否则保留追究法律责任的权利。</p>
</blockquote></div>  
</div>
            