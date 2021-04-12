
---
title: '比神奇女侠还神奇的 postcss'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/c0d3efa6b4ca41a2b47619bcb9f7795c~tplv-k3u1fbpfcp-zoom-1.image'
author: 掘金
comments: false
date: Sun, 11 Apr 2021 10:10:35 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/c0d3efa6b4ca41a2b47619bcb9f7795c~tplv-k3u1fbpfcp-zoom-1.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><blockquote>
<ul>
<li>作者：陈大鱼头</li>
<li>github： <a href="https://github.com/KRISACHAN" target="_blank" rel="nofollow noopener noreferrer">KRISACHAN</a></li>
</ul>
</blockquote>
<h2 data-id="heading-0">postcss 是什么</h2>
<p>按 <a href="https://postcss.org/" target="_blank" rel="nofollow noopener noreferrer">官网</a> 上的介绍，它是一个 <strong>用 JavaScript 转换 CSS 的工具（A tool for transforming CSS with JavaScript）</strong> 。</p>
<p>与之类似的有 <strong><a href="https://sass-lang.com/" target="_blank" rel="nofollow noopener noreferrer">Sass</a></strong> 、<strong><a href="http://lesscss.org/" target="_blank" rel="nofollow noopener noreferrer">Less</a></strong> 跟 <strong><a href="https://stylus-lang.com/" target="_blank" rel="nofollow noopener noreferrer">Stylus</a></strong> 等 <strong>CSS 预处理器</strong> ，可以让我们通过更简便的方法去写 <strong>CSS</strong> 。</p>
<p>虽然利用 <strong>postcss</strong> 我们也可以写出变量 、函数、混合宏、扩展、条件语句、循环等 <strong>CSS</strong> 不支持（或者支持度）不高的语法，但是 <strong>postcss</strong> 本质还是一个 <strong>与业务无关的 CSS 工具</strong> ，而实现以上诸多功能的还是依赖于社区上的各种 <a href="https://www.postcss.parts/" target="_blank" rel="nofollow noopener noreferrer">插件</a> 。</p>
<p>它的作用就如同 <strong>JS</strong> 里的 <strong><a href="https://babeljs.io/" target="_blank" rel="nofollow noopener noreferrer">babel</a></strong> 一般。</p>
<h2 data-id="heading-1">postcss 可以做什么</h2>
<h3 data-id="heading-2">增强代码的可读性</h3>
<p>利用从 Can I Use 网站获取的数据为 CSS 规则添加特定厂商的前缀。 <a href="https://github.com/postcss/autoprefixer" target="_blank" rel="nofollow noopener noreferrer">Autoprefixer</a> 自动获取浏览器的流行度和能够支持的属性，并根据这些数据帮你自动为 CSS 规则添加前缀。</p>
<p>示例如下：</p>
<pre><code class="hljs language-css copyable" lang="css">// 输入
<span class="hljs-selector-pseudo">:fullscreen</span> &#123;
&#125;

// 输出
:-webkit-full-screen &#123;
&#125;
:-ms-fullscreen &#123;
&#125;
<span class="hljs-selector-pseudo">:fullscreen</span> &#123;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-3">将未来的 CSS 特性带到今天！</h3>
<p><a href="https://preset-env.cssdb.org/" target="_blank" rel="nofollow noopener noreferrer">PostCSS Preset Env</a> 帮你将最新的 CSS 语法转换成大多数浏览器都能理解的语法，并根据你的目标浏览器或运行时环境来确定你需要的 polyfills，此功能基于 <a href="https://cssdb.org/" target="_blank" rel="nofollow noopener noreferrer">cssdb</a> 实现。</p>
<p>示例如下：</p>
<pre><code class="hljs language-css copyable" lang="css">// 输入
<span class="hljs-selector-tag">body</span> &#123;
  <span class="hljs-attribute">color</span>: <span class="hljs-built_in">lch</span>(<span class="hljs-number">53</span> <span class="hljs-number">105</span> <span class="hljs-number">40</span>);
&#125;

// 输出
<span class="hljs-selector-tag">body</span> &#123;
  <span class="hljs-attribute">color</span>: <span class="hljs-built_in">rgb</span>(<span class="hljs-number">250</span>, <span class="hljs-number">0</span>, <span class="hljs-number">4</span>);
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-4">终结全局 CSS</h3>
<p><a href="https://github.com/css-modules/css-modules" target="_blank" rel="nofollow noopener noreferrer">CSS 模块</a> 能让你你永远不用担心命名太大众化而造成冲突，只要用最有意义的名字就行了。</p>
<p>示例如下：</p>
<pre><code class="hljs language-css copyable" lang="css">// 输入
<span class="hljs-selector-class">.name</span> &#123;
  <span class="hljs-attribute">color</span>: gray;
&#125;

// 输出
<span class="hljs-selector-class">.Logo__name__SVK0g</span> &#123;
  <span class="hljs-attribute">color</span>: gray;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-5">避免 CSS 代码中的错误</h3>
<p>通过使用 <a href="https://stylelint.io/" target="_blank" rel="nofollow noopener noreferrer">stylelint</a> 强化一致性约束并避免样式表中的错误。stylelint 是一个现代化 CSS 代码检查工具。它支持最新的 CSS 语法，也包括类似 CSS 的语法，例如 SCSS 。</p>
<p>示例如下：</p>
<pre><code class="copyable">// 输入
a &#123;
  color: #d3;
&#125;

// 控制台输出
app.css
2:10 Invalid hex color
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-6">postcss 怎么用</h2>
<p>我们可以以 <strong><a href="https://webpack.js.org/" target="_blank" rel="nofollow noopener noreferrer">webpack</a></strong> 为例看看如何进行配置。</p>
<p>首先就是安装基础插件：</p>
<pre><code class="hljs language-shell copyable" lang="shell">npm install postcss-loader postcss --save-dev
or
yarn add postcss-loader postcss -D
<span class="copy-code-btn">复制代码</span></code></pre>
<p>然后在你的 <code>webpack.config.js</code> 里添加：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-built_in">module</span>.exports = &#123;
  <span class="hljs-attr">module</span>: &#123;
    <span class="hljs-attr">rules</span>: [
      &#123;
        <span class="hljs-attr">test</span>: <span class="hljs-regexp">/\.css$/</span>,
        use: [<span class="hljs-string">"style-loader"</span>, <span class="hljs-string">"css-loader"</span>, <span class="hljs-string">"postcss-loader"</span>]
      &#125;
    ]
  &#125;
&#125;;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>然后在根目录下创建文件 <code>postcss.config.js</code> ，内容如下：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-built_in">module</span>.exports = &#123;
  <span class="hljs-attr">plugins</span>: []
&#125;;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>现在就让我们为在 <strong><a href="https://juejin.cn/#postcss%E5%8F%AF%E4%BB%A5%E5%81%9A%E4%BB%80%E4%B9%88">postcss 可以做什么</a></strong> 里提到的 4 个特性来添加相应的插件。</p>
<p>4 个特性对应的插件如下：</p>
<h3 data-id="heading-7">autoprefixer（增强代码的可读性）</h3>
<p>安装方式：</p>
<pre><code class="hljs language-shell copyable" lang="shell">npm install autoprefixer --save-dev
or
yarn add autoprefixer -D
<span class="copy-code-btn">复制代码</span></code></pre>
<p>配置如下：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">// postcss.config.js</span>
<span class="hljs-keyword">const</span> autoprefixer = <span class="hljs-built_in">require</span>(<span class="hljs-string">"autoprefixer"</span>);
<span class="hljs-built_in">module</span>.exports = &#123;
  <span class="hljs-attr">plugins</span>: [autoprefixer]
&#125;;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><a href="https://www.npmjs.com/package/autoprefixer" target="_blank" rel="nofollow noopener noreferrer">autoprefixer</a> 是与 <a href="https://www.npmjs.com/package/browserslist" target="_blank" rel="nofollow noopener noreferrer">browserslist</a> 进行关联， <strong>browserslist</strong> 就是一个告知打包工具项目将会运行的浏览器以及 node 平台，以此来创建相应的兼容性代码的工具。</p>
<p>所以我们可以在 <code>package.json</code> 里添加 <code>browserslist</code> 属性，或者在根目录添加 <code>.browserslistrc</code> 文件，示例如下（具体规则可根据项目情况来进行配置）：</p>
<pre><code class="copyable">last 2 version
> 1%
IE 11
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>browserslist</strong> 的数据都是来自<a href="https://caniuse.com/" target="_blank" rel="nofollow noopener noreferrer">Can I Use</a>的。</p>
<p>我们可以通过 <a href="https://browserslist.dev/" target="_blank" rel="nofollow noopener noreferrer">browserslist.dev</a> 来查看语句匹配情况。截图如下：</p>
<p><img alt class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/c0d3efa6b4ca41a2b47619bcb9f7795c~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p>所以我们有：</p>
<pre><code class="hljs language-css copyable" lang="css">// <span class="hljs-selector-tag">input</span>
<span class="hljs-selector-class">.example</span> &#123;
  <span class="hljs-attribute">display</span>: grid;
  <span class="hljs-attribute">transition</span>: all <span class="hljs-number">0.5s</span>;
  user-select: none;
  <span class="hljs-attribute">background</span>: <span class="hljs-built_in">linear-gradient</span>(to bottom, white, black);
&#125;

// output
<span class="hljs-comment">/*
* Prefixed by https://autoprefixer.github.io
* PostCSS: v7.0.29,
* Autoprefixer: v9.7.6
* Browsers: last 2 version
*/</span>
<span class="hljs-selector-class">.example</span> &#123;
  <span class="hljs-attribute">display</span>: -ms-grid;
  <span class="hljs-attribute">display</span>: grid;
  -webkit-<span class="hljs-attribute">transition</span>: all <span class="hljs-number">0.5s</span>;
  <span class="hljs-attribute">transition</span>: all <span class="hljs-number">0.5s</span>;
  -webkit-user-select: none;
  -moz-user-select: none;
  -ms-user-select: none;
  user-select: none;
  <span class="hljs-attribute">background</span>: <span class="hljs-built_in">-webkit-gradient</span>(
    linear,
    left top,
    left bottom,
    <span class="hljs-built_in">from</span>(white),
    <span class="hljs-built_in">to</span>(black)
  );
  <span class="hljs-attribute">background</span>: <span class="hljs-built_in">linear-gradient</span>(to bottom, white, black);
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>我们可以通过 <a href="https://autoprefixer.github.io/" target="_blank" rel="nofollow noopener noreferrer">autoprefixer.github.io/</a> 在线看编译效果</p>
<h3 data-id="heading-8">postcss-preset-env（将未来的 CSS 特性带到今天！）</h3>
<p>安装方式：</p>
<pre><code class="hljs language-shell copyable" lang="shell">npm install postcss-preset-env --save-dev
or
yarn add postcss-preset-env -D
<span class="copy-code-btn">复制代码</span></code></pre>
<p>配置如下：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">// postcss.config.js</span>
<span class="hljs-keyword">const</span> postcssPresetEnv = <span class="hljs-built_in">require</span>(<span class="hljs-string">"postcss-preset-env"</span>);
<span class="hljs-built_in">module</span>.exports = &#123;
  <span class="hljs-attr">plugins</span>: [postcssPresetEnv(<span class="hljs-comment">/* pluginOptions */</span>)]
&#125;;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>postcss-preset-env</strong> 可以让我们用一些浏览器支持率不高或者尚未支持的 <strong>CSS 属性</strong> 。</p>
<p>示例如下：</p>
<pre><code class="hljs language-css copyable" lang="css">// <span class="hljs-selector-tag">input</span>
<span class="hljs-selector-pseudo">:root</span> &#123;
  --fontSize: <span class="hljs-number">1rem</span>;
  --mainColor: <span class="hljs-built_in">rgba</span>(<span class="hljs-number">18</span>,<span class="hljs-number">52</span>,<span class="hljs-number">86</span>,<span class="hljs-number">0.47059</span>);
  --secondaryColor: <span class="hljs-built_in">rgba</span>(<span class="hljs-number">102</span>, <span class="hljs-number">51</span>, <span class="hljs-number">153</span>, <span class="hljs-number">0.9</span>);
&#125;

<span class="hljs-keyword">@media</span> (<span class="hljs-attribute">max-width</span>: <span class="hljs-number">50rem</span>) &#123;
  <span class="hljs-selector-tag">body</span> &#123;
    <span class="hljs-attribute">color</span>: <span class="hljs-built_in">var</span>(--mainColor);
    <span class="hljs-attribute">font-family</span>: system-ui;
    <span class="hljs-attribute">font-size</span>: <span class="hljs-built_in">var</span>(--fontSize);
    <span class="hljs-attribute">line-height</span>: <span class="hljs-built_in">calc</span>(<span class="hljs-built_in">var</span>(--fontSize) * <span class="hljs-number">1.5</span>);
    <span class="hljs-attribute">overflow-wrap</span>: break-word;
    <span class="hljs-attribute">padding-left</span>: <span class="hljs-built_in">calc</span>(<span class="hljs-built_in">var</span>(--fontSize) / <span class="hljs-number">2</span> + <span class="hljs-number">1px</span>);
    <span class="hljs-attribute">padding-right</span>: <span class="hljs-built_in">calc</span>(<span class="hljs-built_in">var</span>(--fontSize) / <span class="hljs-number">2</span> + <span class="hljs-number">1px</span>);
  &#125;
&#125;

// output Stage <span class="hljs-number">0</span> > <span class="hljs-number">3%</span>
<span class="hljs-selector-pseudo">:root</span> &#123;
  --fontSize: <span class="hljs-number">1rem</span>;
  --mainColor: <span class="hljs-built_in">rgba</span>(<span class="hljs-number">18</span>, <span class="hljs-number">52</span>, <span class="hljs-number">86</span>, <span class="hljs-number">0.47059</span>);
  --secondaryColor: <span class="hljs-built_in">rgba</span>(<span class="hljs-number">102</span>, <span class="hljs-number">51</span>, <span class="hljs-number">153</span>, <span class="hljs-number">0.9</span>);
&#125;

<span class="hljs-selector-tag">html</span> &#123;
  <span class="hljs-attribute">overflow-x</span>: hidden;
  <span class="hljs-attribute">overflow-y</span>: auto;
  <span class="hljs-attribute">overflow</span>: hidden auto;
&#125;

<span class="hljs-keyword">@media</span> (<span class="hljs-attribute">max-width</span>: <span class="hljs-number">50rem</span>) &#123;
  <span class="hljs-selector-tag">body</span> &#123;
    <span class="hljs-attribute">color</span>: <span class="hljs-built_in">var</span>(--mainColor);
    <span class="hljs-attribute">font-family</span>: system-ui;
    <span class="hljs-attribute">font-size</span>: <span class="hljs-built_in">var</span>(--fontSize);
    <span class="hljs-attribute">line-height</span>: <span class="hljs-built_in">calc</span>(<span class="hljs-built_in">var</span>(--fontSize) * <span class="hljs-number">1.5</span>);
    <span class="hljs-attribute">overflow-wrap</span>: break-word;
    <span class="hljs-attribute">padding-left</span>: <span class="hljs-built_in">calc</span>(<span class="hljs-built_in">var</span>(--fontSize) / <span class="hljs-number">2</span> + <span class="hljs-number">1px</span>);
    <span class="hljs-attribute">padding-right</span>: <span class="hljs-built_in">calc</span>(<span class="hljs-built_in">var</span>(--fontSize) / <span class="hljs-number">2</span> + <span class="hljs-number">1px</span>);
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>我们可以通过 <a href="https://csstools.github.io/postcss-preset-env/" target="_blank" rel="nofollow noopener noreferrer">csstools.github.io/postcss-pre…</a> 在线看编译效果。</p>
<p>它可选的选项有 7 个，分别是：stage、features、browsers、insertBefore、insertAfter、autoprefixer、preserve、importFrom。</p>
<p>具体选项说明与示例可参考 <a href="https://github.com/csstools/postcss-preset-env" target="_blank" rel="nofollow noopener noreferrer">github.com/csstools/po…</a> 。</p>
<p>这里要着重分享两个选项：</p>
<h4 data-id="heading-9">stage</h4>
<p>在谈 <strong>stage</strong> 这个选项之前，首先我们得先知道一个概念—— <strong>cssdb</strong> 。</p>
<p><strong>cssdb</strong> 是 <code>postcss-preset-env</code> 的实现基准，主要就是 <strong>CSS</strong> 的新功能功能及这些功能从提出到成为标准时所在的进程。</p>
<p><strong>cssdb</strong> 跟 <strong>ecma</strong> 一样，对新属性分了不同的进程，具体的进程如下：</p>
<p>Stage 0：脑袋风暴阶段。高度不稳定，可能会发生变化。</p>
<p>Stage 1：实验阶段。也非常不稳定，可能会发生变化，但是该提案已得到 W3C 成员的认可。</p>
<p>Stage 2：承认阶段。高度不稳定并且可能会发生变化，但是正在积极研究中。</p>
<p>Stage3：拥抱阶段。稳定且变化不大，此功能可能会成为标准。</p>
<p>Stage4：标准阶段。最终的解决方案，所有主流浏览器都支持。</p>
<p>所以 <strong>stage</strong> 这个配置的可选项就是 <strong>1、2、3、4</strong> 了。</p>
<h4 data-id="heading-10">features</h4>
<p><strong>features</strong> 选项按 <strong>ID</strong> 启用或禁用特定的 <strong>polyfill</strong> 。启用就是 <code>true</code> 。</p>
<p>具体可参考 <a href="https://github.com/csstools/postcss-preset-env/blob/master/src/lib/plugins-by-id.js#L36" target="_blank" rel="nofollow noopener noreferrer">github.com/csstools/po…</a></p>
<h3 data-id="heading-11">css-modules（终结全局 CSS）</h3>
<p>安装方式：</p>
<pre><code class="hljs language-shell copyable" lang="shell">npm install postcss-modules --save-dev
or
yarn add postcss-modules -D
<span class="copy-code-btn">复制代码</span></code></pre>
<p>配置如下：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">// postcss.config.js</span>
<span class="hljs-keyword">const</span> postcssModules = <span class="hljs-built_in">require</span>(<span class="hljs-string">"postcss-modules"</span>);
<span class="hljs-built_in">module</span>.exports = &#123;
  <span class="hljs-attr">plugins</span>: [postcssModules(<span class="hljs-comment">/* pluginOptions */</span>)]
&#125;;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>css-modules</strong> 支持我们以模块化的形式来编写代码。示例如下：</p>
<pre><code class="hljs language-css copyable" lang="css">// <span class="hljs-selector-tag">input</span>
<span class="hljs-selector-class">.grid</span> &#123;
  <span class="hljs-attribute">display</span>: grid;
  grid: <span class="hljs-built_in">repeat</span>(<span class="hljs-number">2</span>, <span class="hljs-number">240px</span>) / auto-flow <span class="hljs-number">320px</span>;
  & > <span class="hljs-selector-tag">div</span> &#123;
    <span class="hljs-attribute">background-color</span>: <span class="hljs-number">#8ca0ff</span>;
    <span class="hljs-attribute">width</span>: <span class="hljs-number">200px</span>;
    <span class="hljs-attribute">height</span>: <span class="hljs-number">200px</span>;
    <span class="hljs-attribute">transition</span>: <span class="hljs-number">1s</span>;
  &#125;
&#125;

// output
<span class="hljs-selector-class">.demo__grid___2lKm5</span> &#123;
  <span class="hljs-attribute">display</span>: -ms-grid;
  <span class="hljs-attribute">display</span>: grid;
  grid: <span class="hljs-built_in">repeat</span>(<span class="hljs-number">2</span>, <span class="hljs-number">32vw</span>) / auto-flow <span class="hljs-number">42.667vw</span>;
&#125;
<span class="hljs-selector-class">.demo__grid___2lKm5</span> > <span class="hljs-selector-tag">div</span> &#123;
  <span class="hljs-attribute">background-color</span>: <span class="hljs-number">#8ca0ff</span>;
  <span class="hljs-attribute">width</span>: <span class="hljs-number">26.667vw</span>;
  <span class="hljs-attribute">height</span>: <span class="hljs-number">26.667vw</span>;
  -webkit-<span class="hljs-attribute">transition</span>: <span class="hljs-number">1s</span>;
  <span class="hljs-attribute">transition</span>: <span class="hljs-number">1s</span>;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>其实在这里，如果不使用 <code>postcss-modules</code> ，也可以直接利用 <code>css-loader</code> 开启 css 模块化，具体配置如下：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">// webpack.config.js</span>
<span class="hljs-built_in">module</span>.exports = &#123;
  <span class="hljs-attr">module</span>: &#123;
    <span class="hljs-attr">rules</span>: [
      &#123;
        <span class="hljs-attr">test</span>: <span class="hljs-regexp">/\.css$/i</span>,
        use: [
          &#123;
            <span class="hljs-attr">loader</span>: <span class="hljs-string">"css-loader"</span>,
            <span class="hljs-attr">options</span>: &#123;
              <span class="hljs-attr">modules</span>: <span class="hljs-literal">true</span>,
              <span class="hljs-attr">importLoaders</span>: <span class="hljs-literal">true</span>,
              <span class="hljs-attr">localIdentName</span>: <span class="hljs-string">"[name]__[local]___[hash:base64:5]"</span>
            &#125;
          &#125;
        ]
      &#125;
    ]
  &#125;
&#125;;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-12">stylelint（避免 CSS 代码中的错误）</h3>
<p>如果在 <strong>JS</strong> 中我们可以使用 <a href="https://eslint.org/" target="_blank" rel="nofollow noopener noreferrer">eslint</a> 进行代码检查一样，在 <strong>CSS</strong> 中我们也可以通过 <a href="https://stylelint.io/" target="_blank" rel="nofollow noopener noreferrer">stylelint</a> 来进行代码检查。</p>
<p>安装方法：</p>
<pre><code class="hljs language-shell copyable" lang="shell">npm install stylelint stylelint-config-standard --save-dev
or
yarn add stylelint stylelint-config-standard -D
<span class="copy-code-btn">复制代码</span></code></pre>
<p>配置如下：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">// webpack.config.js</span>
<span class="hljs-keyword">const</span> StyleLintPlugin = <span class="hljs-built_in">require</span>(<span class="hljs-string">"stylelint-webpack-plugin"</span>);

<span class="hljs-built_in">module</span>.exports = &#123;
  <span class="hljs-attr">plugins</span>: [<span class="hljs-keyword">new</span> StyleLintPlugin <span class="hljs-comment">/* pluginOptions */</span>()]
&#125;;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>然后在根目录上创建 <code>.stylelintrc</code> 或者 <code>stylelint.config.js</code> 文件（具体文件可在 StyleLintPlugin 中配置），其内容如下：</p>
<pre><code class="hljs language-shell copyable" lang="shell">&#123;
    "extends": "stylelint-config-standard",
    "rules": &#123;/* pluginOptions */&#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>所以当我们代码不规范时，就可以在命令行里看到类似的报错：</p>
<p><img alt class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/d3b397057b1846d7ae4659131b7b8e71~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p>我们也可以在 编辑器 里找到对应的 <strong>stylelint</strong> 插件，从而进行 CSS 代码自动格式化。</p>
<h2 data-id="heading-13">ying-template</h2>
<p><a href="https://github.com/KRISACHAN/ying-template" target="_blank" rel="nofollow noopener noreferrer">ying-template</a> 是鱼头在 GitHub 上开源的一个基于 webpack5 + typeScript4 + postcss8 的一个多页面脚手架，在最开始的版本中也引入了 sass、less ，不过后来因为 postcss 太香，就直接去除了 sass、less ，只留下 postcss 。</p>
<p>ying-template 目前已经在鱼头老东家的一个专利项目中投入了生产，而鱼头另一个开源库 <a href="https://github.com/KRISACHAN/ying-datastructures-algorithms" target="_blank" rel="nofollow noopener noreferrer">ying-datastructures-algorithms</a> （一个算法与数据结构 typescript 描述库）也在使用中，另外社区中也有一些小伙伴在项目中使用或借鉴了，各位有兴趣也可以 clone 下来看一下，可以感受下在 postcss 下的 css 是多么有魅力。</p>
<p>另外值得一提的是，除了上面介绍的几个基础插件之外，postcss 社区上也有许多有意思的插件，各位可以通过 <a href="https://www.postcss.parts/" target="_blank" rel="nofollow noopener noreferrer">www.postcss.parts/</a> 来选择自己所需要的插件进行使用。</p>
<h2 data-id="heading-14">参考资料</h2>
<ol>
<li><a href="https://github.com/KRISACHAN/ying-template" target="_blank" rel="nofollow noopener noreferrer">ying-template</a></li>
<li><a href="https://www.postcss.com.cn/" target="_blank" rel="nofollow noopener noreferrer">PostCSS</a></li>
<li><a href="https://mp.weixin.qq.com/s/Zqw8f5jX6MmeURRzc44C6Q" target="_blank" rel="nofollow noopener noreferrer">CSS 的未来已来</a></li>
<li><a href="https://github.com/postcss/autoprefixer" target="_blank" rel="nofollow noopener noreferrer">Autoprefixer</a></li>
<li><a href="https://autoprefixer.github.io/" target="_blank" rel="nofollow noopener noreferrer">Autoprefixer CSS online</a></li>
<li><a href="https://browserslist.dev/" target="_blank" rel="nofollow noopener noreferrer">browserslist</a></li>
<li><a href="https://github.com/csstools/postcss-preset-env" target="_blank" rel="nofollow noopener noreferrer">PostCSS Preset Env</a></li>
<li><a href="https://www.postcss.parts/" target="_blank" rel="nofollow noopener noreferrer">postcss.parts</a></li>
</ol></div> <div class="image-viewer-box" data-v-78c9b824><!----></div>  
</div>
            