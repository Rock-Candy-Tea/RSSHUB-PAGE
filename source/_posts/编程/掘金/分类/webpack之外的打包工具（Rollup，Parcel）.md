
---
title: 'webpack之外的打包工具（Rollup，Parcel）'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=287'
author: 掘金
comments: false
date: Fri, 07 May 2021 19:27:48 GMT
thumbnail: 'https://picsum.photos/400/300?random=287'
---

<div>   
<div class="markdown-body"><style>@charset "UTF-8";.markdown-body&#123;word-break:break-word;line-height:2;font-weight:400;font-size:15px;overflow-x:hidden;color:#333;letter-spacing:1.2px&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1:first-child,.markdown-body h2:first-child,.markdown-body h3:first-child,.markdown-body h4:first-child,.markdown-body h5:first-child,.markdown-body h6:first-child&#123;margin-top:-1.5rem;margin-bottom:1rem&#125;.markdown-body h1:before,.markdown-body h2:before,.markdown-body h3:before,.markdown-body h4:before,.markdown-body h5:before,.markdown-body h6:before&#123;content:"#";display:inline-block;color:#3eaf7c;padding-right:.23em&#125;.markdown-body h1&#123;position:relative;font-size:2.5rem;margin-bottom:5px&#125;.markdown-body h1:before&#123;font-size:2.5rem&#125;.markdown-body h2&#123;padding-bottom:.5rem;font-size:2.2rem;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:1.5rem;padding-bottom:0&#125;.markdown-body h4&#123;font-size:1.25rem&#125;.markdown-body h5&#123;font-size:1rem&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body strong&#123;color:#3eaf7c&#125;.markdown-body img&#123;max-width:100%;border-radius:2px;display:block;margin:auto&#125;.markdown-body hr&#123;border:none;border-top:1px solid #3eaf7c;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;overflow-x:auto;padding:.2rem .5rem;margin:0;color:#3eaf7c;font-size:.85em;background-color:rgba(27,31,35,.05);border-radius:3px&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75;border:.5rem solid #3eaf7c&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;font-weight:500;text-decoration:none;color:#3eaf7c;margin:0 5px&#125;.markdown-body a:active,.markdown-body a:hover&#123;text-decoration:none;border-bottom:1.5px solid #3eaf7c&#125;.markdown-body a[href^=http]:after&#123;content:url("data:image/svg+xml;base64,PHN2ZyBjbGFzcz0iaWNvbiIgdmlld0JveD0iMCAwIDEwMjQgMTAyNCIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIiB3aWR0aD0iMTQiIGhlaWdodD0iMTQiPjxkZWZzPjxzdHlsZS8+PC9kZWZzPjxwYXRoIGQ9Ik04MzIgMTI4SDY0MHY2NGgxNDYuNzUyTDUyMS4zNzYgNDU3LjM3Nmw0NS4yNDggNDUuMjQ4TDgzMiAyMzcuMjQ4VjM4NGg2NFYxMjh6IiBmaWxsPSIjM2VhZjdjIi8+PHBhdGggZD0iTTc2OCA4MzJIMTkyVjI1NmgzNTJ2LTY0SDE2MGEzMiAzMiAwIDAwLTMyIDMydjY0MGEzMiAzMiAwIDAwMzIgMzJoNjQwYTMyIDMyIDAgMDAzMi0zMlY0ODBoLTY0djM1MnoiIGZpbGw9IiMzZWFmN2MiLz48L3N2Zz4=");margin-left:2px&#125;.markdown-body a[href^="#"]:before&#123;content:"#"&#125;.markdown-body table&#123;display:inline-block!important;font-size:13px;width:auto;max-width:100%;overflow:auto;border:1px solid #3eaf7c;border-collapse:collapse&#125;.markdown-body thead&#123;background:#3eaf7c;color:#fff;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:rgba(153,255,188,.1)&#125;.markdown-body td,.markdown-body th&#123;padding:4px 8px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#7b7878;padding:1px 23px;border-left:.5rem solid;border-color:#42b983;background-color:rgba(66,184,131,.1);position:relative;margin:14px 8px 0&#125;.markdown-body blockquote:before&#123;display:inline-block;position:absolute;content:url("data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMjUiIGhlaWdodD0iMjUiIHZpZXdCb3g9IjAgMCAyNyAyNyIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj48ZyB0cmFuc2Zvcm09InRyYW5zbGF0ZSgxLjg2MiAxLjg2MikiIGZpbGwtcnVsZT0ibm9uemVybyIgZmlsbD0ibm9uZSI+PGNpcmNsZSBzdHJva2U9IiNGRkYiIHN0cm9rZS13aWR0aD0iMS43MjQiIGZpbGw9IiM0MkI5ODMiIGN4PSIxMS42MzgiIGN5PSIxMS42MzgiIHI9IjExLjYzOCIvPjxwYXRoIGQ9Ik0xNC45NzggNi4yN0E1LjAwNiA1LjAwNiAwIDAwNi42NyA5LjQ2OGE0LjkwMSA0LjkwMSAwIDAwMS43NzMgNC4zNjJjLjMyMy4yNTguNTE0LjY0Ny41MjIgMS4wNnYxLjA2YTIuNjg1IDIuNjg1IDAgMDA1LjM3IDB2LTEuMDA4Yy4wMDItLjM5OC4xNzMtLjc3Ny40Ny0xLjA0MmE1LjAyMyA1LjAyMyAwIDAwLjE3My03LjYzem0tMy4zMzcgMTAuOTY3YTEuMzA0IDEuMzA0IDAgMDEtMS4yODYtMS4yODd2LS4yNzhoMi41NzJ2LjI2MWMwIC43MTMtLjU3MyAxLjI5NC0xLjI4NiAxLjMwNHptMi4yNi00LjQxNWMtLjQ0LjM4My0uNzUuODkzLS44ODcgMS40NmgtMi43NDZhMi44NjggMi44NjggMCAwMC0uOTM4LTEuNTNoLS4wMThhMy40NzYgMy40NzYgMCAwMS0xLjI2OS0zLjE0NSAzLjYxNSAzLjYxNSAwIDAxNy4xOTYuNCAzLjY1IDMuNjUgMCAwMS0xLjMzOCAyLjgxNXoiIGZpbGw9IiNGRkYiLz48L2c+PC9zdmc+");width:25px;height:25px;left:-16px;top:12px&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body details&#123;outline:none;border:none;border-left:4px solid #3eaf7c;padding-left:10px;margin-left:4px&#125;.markdown-body details summary&#123;cursor:pointer;border:none;outline:none;background:#fff;margin:0 -17px&#125;.markdown-body details summary::-webkit-details-marker&#123;color:#3eaf7c&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body ol li::marker&#123;color:#3eaf7c&#125;.markdown-body ul li&#123;list-style:none;padding-left:10px&#125;.markdown-body ul li::marker&#123;content:"•";color:#3eaf7c&#125;.markdown-body ul li.task-list-item:before&#123;content:"";margin-right:0&#125;.markdown-body input[type=checkbox]&#123;vertical-align:text-bottom;box-shadow:inset 0 0 0 10px #fff&#125;.markdown-body input[type=checkbox]:before&#123;content:url("data:image/svg+xml;base64,PHN2ZyBjbGFzcz0iaWNvbiIgdmlld0JveD0iMCAwIDEwMjQgMTAyNCIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIiB3aWR0aD0iMTYiIGhlaWdodD0iMTYiPjxkZWZzPjxzdHlsZS8+PC9kZWZzPjxwYXRoIGQ9Ik04NzcuMDU2IDE0Ni45NDR2NzMwLjExMkgxNDYuOTQ0VjE0Ni45NDRoNzMwLjExMnptMC0xMDQuMjc3SDE0Ni45NDRjLTU3LjYyOCAwLTEwNC4yNzcgNDYuNjQ5LTEwNC4yNzcgMTA0LjI3N3Y3MzAuMTEyYzAgNTcuNjI4IDQ2LjY0OSAxMDQuMjc3IDEwNC4yNzcgMTA0LjI3N2g3MzAuMTEyYzU3LjYyOCAwIDEwNC4yNzctNDYuNjQ5IDEwNC4yNzctMTA0LjI3N1YxNDYuOTQ0YzAtNTcuNjI4LTQ2LjY0OS0xMDQuMjc3LTEwNC4yNzctMTA0LjI3N3oiIGZpbGw9IiMzZWFmN2MiLz48L3N2Zz4=");position:relative;top:-2px;right:2px&#125;.markdown-body input[type=checkbox]:checked:before&#123;content:url("data:image/svg+xml;base64,PHN2ZyBjbGFzcz0iaWNvbiIgdmlld0JveD0iMCAwIDEwMjQgMTAyNCIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIiB3aWR0aD0iMTUiIGhlaWdodD0iMTUiPjxkZWZzPjxzdHlsZS8+PC9kZWZzPjxwYXRoIGQ9Ik05MTAuMjA4IDBIMTEzLjc2QTExNC4xMTIgMTE0LjExMiAwIDAwLS4wMzIgMTEzLjc5MlY5MTAuMjRjMCA2Mi41OTIgNTEuMiAxMTMuNzkyIDExMy43OTIgMTEzLjc5Mmg3OTYuNDQ4YzYyLjU5MiAwIDExMy43OTItNTEuMiAxMTMuNzkyLTExMy43OTJWMTEzLjc5MkMxMDI0IDUxLjIgOTcyLjggMCA5MTAuMjA4IDB6bS01MTIgNzk2LjQ0OEwxMTMuNzYgNTEybDc5LjY0OC03OS42NDggMjA0LjggMjA0LjhMODMwLjU2IDIwNC44bDc5LjY0OCA3OS42NDgtNTEyIDUxMnoiIGZpbGw9IiMzZWFmN2MiLz48L3N2Zz4=");position:relative;top:-2px;right:2px&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h1 data-id="heading-0">webpack之外的打包工具（Rollup，Parcel）</h1>
<p>我们接触最多的可能是webpack，但现在其实还有很多其他的打包工具，所以在此文章做一个整理，让我们有更多的角度去认识打包工具的发展，也有助于未来工程的技术选型。</p>
<p>此文章主要讲：</p>
<ol>
<li>Rollup和Parcel各自的特点和优势</li>
<li>JavaScript打包工具发展的趋势</li>
<li>如何选择合适的打包工具</li>
</ol>
<h2 data-id="heading-1">Rollup</h2>
<p>如何用Webpack和Rollup进行比较的话</p>
<ul>
<li>webpack的优势在于他更加全面，基于”一切皆模块“的思想而衍生出丰富的loader和plugin可以满足各种使用场景</li>
<li>Rollup更像一把手术刀，它更专注于JavaScript的打包。
<ul>
<li>当然也支持其他类型的模块，但总体而言在通用性上还是不如webpack。如果当前的项目需求仅仅是打包JavaScript，比如一个JavaScript库，那么Rollup很多时候会是我们的第一选择。</li>
</ul>
</li>
</ul>
<h4 data-id="heading-2">配置</h4>
<p>简单示例看看Rollup如何工作</p>
<p>首先创建rollup.config.js以及我们打包的项目文件app.js</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// rollup.config.js</span>
<span class="hljs-built_in">module</span>.exports = &#123;
    <span class="hljs-attr">input</span>: <span class="hljs-string">'src/app.js'</span>,
    <span class="hljs-attr">output</span>: &#123;
        <span class="hljs-attr">file</span>: <span class="hljs-string">'dist/bundle.js'</span>,
        <span class="hljs-attr">format</span>: <span class="hljs-string">'cjs'</span> <span class="hljs-comment">// CommonJS</span>
    &#125;
&#125;

<span class="hljs-comment">// app.js</span>
<span class="hljs-built_in">console</span>.log(<span class="hljs-number">123</span>)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>与webpack一般装在项目内部不同，rollup直接全局安装即可</p>
<p><code>(sudo) npm i rollup -g</code></p>
<p>然后使用rollup命令打包</p>
<p><code>rollup -c rollup.config.js</code></p>
<ul>
<li>-c参数是告诉Rollup使用该配置文件。</li>
</ul>
<p>打包结果如下：（非常干净）</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-meta">'use strict'</span>
<span class="hljs-built_in">console</span>.log(<span class="hljs-number">123</span>)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>使用webpack的话，大概有50行左右（webpack自身代码注入）。显然rollup打包出来的体积要小，不包含无关代码</p>
<h4 data-id="heading-3">tree shaking</h4>
<p>虽然webpack也有，但最早开始于rollup，后面被webpack所借鉴</p>
<ul>
<li>（类似的还有，输出格式）在webpack的早期，Rollup有一项webpack不具有的功能：通过配置output.format开发者可以选择输出资源的模块形式（cjs（CommonJS），esm（ES6 Modules），amd，umd，iife，system等），此特性对于打包JavaScript库特别有用，因为往往一个库需要支持多种不同的模块形式，而通过rollup几个命令就可以把一份源代码打包为多份</li>
</ul>
<p>rollup的tree shaking也是基于ES6 Mudules 的静态分析，找出没有被引用过的模块，将其从最后生成的bundle中去除。</p>
<p>举个例子</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// app.js</span>
<span class="hljs-keyword">import</span> &#123; add &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'./util.js'</span>
<span class="hljs-built_in">console</span>.log(add(<span class="hljs-number">2</span>, <span class="hljs-number">3</span>))

<span class="hljs-comment">// util.js</span>
<span class="hljs-keyword">export</span> <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">add</span>(<span class="hljs-params">a, b</span>) </span>&#123;
    <span class="hljs-keyword">return</span> a + b
&#125;
<span class="hljs-keyword">export</span> <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">sub</span>(<span class="hljs-params">a, b</span>) </span>&#123;
    <span class="hljs-keyword">return</span> a - b
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>Rollup的打包结果如下：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-meta">'use strict'</span>

<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">add</span>(<span class="hljs-params">a, b</span>) </span>&#123;
    <span class="hljs-keyword">return</span> a + b
&#125;

<span class="hljs-built_in">console</span>.log(add(<span class="hljs-number">2</span>, <span class="hljs-number">3</span>))
<span class="copy-code-btn">复制代码</span></code></pre>
<p>可以看到util.js中的sub函数没有被引用过，因此也没有出现在最终的bundle.js中。与之前一样，输出的内容非常清晰简洁，没有附加代码</p>
<h4 data-id="heading-4">实际应用</h4>
<p>在实际应用中，rollup经常被用于打包一些库或框架（vue，react）</p>
<ul>
<li>react团队在一篇博文中提到，他们将react原有的打包工具从Browserify迁移到rollup，获得了以下几项收益：
<ol>
<li>最低限度的附加代码</li>
<li>对ES6 Modules的良好支持</li>
<li>通过 tree shaking去除开发环境代码</li>
<li>通过自定义插件在实现一些react特性化的打包逻辑</li>
</ol>
</li>
</ul>
<p>Rollup没有webpack对于应用开发那样强大的支持（支持各种loader和plugin，HMR等），因为他设计之初，就是主要偏向于JavaScript库的构建</p>
<p>总结：Rollup更像一把手术刀，它更专注于JavaScript的打包。</p>
<ul>
<li>当然也支持其他类型的模块，但总体而言在通用性上还是不如webpack。如果当前的项目需求仅仅是打包JavaScript，比如一个JavaScript库，那么Rollup很多时候会是我们的第一选择。</li>
</ul>
<h2 data-id="heading-5">Parcel</h2>
<p>Parcel在js打包工具中属于相对后来者（根据npm版本上传显示最早上传于 2017.8，webpack是2021.3，rollup是2015.5）</p>
<h4 data-id="heading-6">打包速度</h4>
<p>在Parcel官网的Benchmark测试中，在有缓存的情况下其打包速度比webpack快近8倍，且宣称自己是零配置。他的出现正好契合当时开发者们对于webpack打包慢和配置复杂的抱怨，从而吸引了很多用户</p>
<p>Parcel在打包速度上主要做了3件事情：</p>
<ol>
<li>利用worker来并行执行任务</li>
<li>文件系统缓存</li>
<li>资源编译处理流程优化</li>
</ol>
<p>上面3点的前两个webpack已经在做了。比如webpack在资源压缩时可用利用多核同时压缩多个资源（但资源编译过程中还没实现）；本地缓存则更多的是在loader层面，像babel-loader就会把编译结果缓存在项目中的一个隐藏目录里，并通过本地文件的修改时间和状态来判断是否使用上次编译的缓存。第三点是Parcel最大的优势：因为webpack的每个loader都要生成一遍AST，Parcel则不用，只需生成一次AST（相当于Parcel内置了loader，才能做此优化）</p>
<h4 data-id="heading-7">零配置</h4>
<p>非常方便和快速</p>
<p>具体操作可以参考官网：<a href="https://www.parceljs.cn/getting_started.html" target="_blank" rel="nofollow noopener noreferrer">www.parceljs.cn/getting_sta…</a></p>
<p>总结：Parcel相比于webpack来说，优势在于快速和灵巧。假如我们需要在很短的时间内搭建一个原型，或者不需要进行深度定制的工程，那么使用Parcel的话前期开发速度会很快。</p>
<ul>
<li>以前即便做一个小工程使用Webpack也要先写一堆配置，现在我们多了另外一种选择</li>
</ul>
<h2 data-id="heading-8">打包工具的发展趋势</h2>
<ol>
<li>性能与通用性
<ul>
<li>打包速度趋向越来越快，但越通用就必须会牺牲掉一些性能。如Parcel对比webpack，Parcel牺牲的通用性去提升打包性能</li>
</ul>
</li>
<li>配置极小化与工程标准化
<ul>
<li>极小化配置甚至零配置逐渐成为一个重要的特性。Parcel让大家知道，打包工具并不一定非要写一大堆配置，很多东西可以被简化。Parcel出现不久后，webpack也在4.0的版本中宣称自己是零配置</li>
<li>极小化配置的背后体现出来的就是js工程的标准化。最简单的就是源码目录（比如src）和产出资源目录（比如dist）。成为默认项之后，对整个社区的发展是一件好事</li>
</ul>
</li>
<li>WebAssembly
<ul>
<li>未来说不定通过loader就能加载c代码模块</li>
</ul>
</li>
</ol>
<hr>
<p>参考《Webpack实战：入门、进阶与调优》（居玉皓）</p></div>  
</div>
            