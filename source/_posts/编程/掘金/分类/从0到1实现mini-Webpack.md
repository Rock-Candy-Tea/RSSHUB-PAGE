
---
title: '从0到1实现mini-Webpack'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/6b2dd133328347438e8a1b77ea6bdf63~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Sun, 30 May 2021 02:13:01 GMT
thumbnail: 'https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/6b2dd133328347438e8a1b77ea6bdf63~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;color:#383838;font-size:15px;line-height:37.5px;letter-spacing:2px;word-break:break-word;font-family:-apple-system,BlinkMacSystemFont,Segoe UI,Roboto,Oxygen,Ubuntu,Cantarell,Open Sans,Helvetica Neue,sans-serif;scroll-behavior:smooth;background-image:linear-gradient(0deg,transparent 24%,rgba(201,195,195,.329) 25%,hsla(0,8%,80.4%,.05) 26%,transparent 27%,transparent 74%,hsla(0,5.2%,81%,.185) 75%,rgba(180,176,176,.05) 76%,transparent 77%,transparent),linear-gradient(90deg,transparent 24%,rgba(204,196,196,.226) 25%,hsla(0,4%,66.1%,.05) 26%,transparent 27%,transparent 74%,hsla(0,5.2%,81%,.185) 75%,rgba(180,176,176,.05) 76%,transparent 77%,transparent);background-color:#fff;background-size:50px 50px;padding-bottom:120px&#125;.markdown-body ::selection&#123;color:#fff;background-color:#a862ea&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;margin:30px 0 15px;color:#a862ea&#125;.markdown-body h1&#123;line-height:2;font-size:1.4em&#125;.markdown-body h1~p:first-of-type:first-letter&#123;color:#a862ea;float:left;font-size:2em;margin-right:.4em;font-weight:bolder&#125;.markdown-body h2&#123;font-size:1.2em&#125;.markdown-body h3&#123;font-size:1.1em&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:2em&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;padding-left:.2em&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:10px&#125;.markdown-body li::marker&#123;color:#a862ea&#125;.markdown-body li,.markdown-body p&#123;opacity:.9;vertical-align:baseline;transition:all .1s ease&#125;.markdown-body li:hover,.markdown-body p:hover&#123;opacity:1&#125;.markdown-body a&#123;display:inline-block;color:#a862ea;cursor:pointer;padding-bottom:2px;text-decoration:none;position:relative&#125;.markdown-body a:after&#123;content:"";position:absolute;width:98%;height:2px;bottom:0;left:0;transform:scaleX(0);background-color:#a862ea;transform-origin:bottom right;transition:transform .3s ease-in-out&#125;.markdown-body a:hover:after&#123;transform:scaleX(1);transform-origin:bottom left&#125;.markdown-body a:active,.markdown-body a:link&#123;color:#a862ea&#125;.markdown-body img&#123;max-width:100%;user-select:none;margin:1em 0;box-shadow:0 0 20px 0 #e7daff;transition:transform .2s ease 0s;background-color:#f8f5ff&#125;.markdown-body img:hover&#123;opacity:1;transform:translateY(-2px)&#125;.markdown-body blockquote&#123;padding:.5em 1em;margin:15px 0;border-top-left-radius:2px;border-bottom-left-radius:2px;border-left:4px solid #a862ea;background-color:#f8f5ff&#125;.markdown-body blockquote>p&#123;margin:0&#125;.markdown-body code&#123;padding:2px .4em;overflow-x:auto;color:#a862ea;font-weight:700;word-break:break-word;font-family:Operator Mono,Consolas,Monaco,Menlo,monospace;background-color:#f8f5ff&#125;.markdown-body pre&#123;margin:2em 0;box-shadow:0 0 20px #e7daff&#125;.markdown-body pre>code&#123;display:block;padding:1.5em;word-break:normal;font-size:.9em;font-style:normal;font-weight:400;font-family:Operator Mono,Consolas,Monaco,Menlo,monospace;line-height:22.5px;color:#383838;border-radius:3px;scroll-behavior:smooth&#125;.markdown-body pre>code::-webkit-scrollbar&#123;height:6px;background-color:#f8f5ff&#125;.markdown-body pre>code::-webkit-scrollbar-thumb&#123;background-color:#e7daff;border-bottom-left-radius:3px;border-bottom-right-radius:3px&#125;.markdown-body hr&#123;margin:2em 0;border-top:1px solid #a862ea&#125;.markdown-body table&#123;font-size:12px;max-width:100%;overflow:auto;border-collapse:collapse;border:1px solid #e7daff&#125;.markdown-body thead&#123;color:#a862ea;background:#f8f5ff&#125;.markdown-body td,.markdown-body th&#123;padding:1em .5em&#125;.markdown-body tr&#123;background-color:#fcfcfc&#125;@media (max-width:720px)&#123;.markdown-body&#123;font-size:12px&#125;&#125;</style><h2 data-id="heading-0">前言</h2>
<p>近日看了直播课里面讲的<strong>webpack</strong>实现思路，自觉受益匪浅，因此把里面的内容半搬运过来写成博客与大家一起分享，在这个过程自己也手敲一下代码加深印象，本文适用于对webpack有初步了解的人群，话不多说，开整🔧</p>
<blockquote>
<p><a href="https://www.bilibili.com/video/BV1ub4y1Z7Mx" target="_blank" rel="nofollow noopener noreferrer">www.bilibili.com/video/BV1ub…</a></p>
</blockquote>
<h2 data-id="heading-1">前置知识</h2>
<p>webpack的作用就是对模块进行打包处理，因此以下内容给对模块化概念还不了解的同学做一个简单介绍，已经对这部分内容熟悉的可直接跳过至下一章节🔨</p>
<h3 data-id="heading-2">Js中的模块概念</h3>
<blockquote>
<p>模块通常是指编程语言所提供的代码组织机制，利用此机制可将程序拆解为独立且通用的代码单元。</p>
</blockquote>
<ol>
<li>模块化的出现解决了什么问题</li>
</ol>
<p>模块化的出现解决了代码分割、作用域隔离、模块之间的依赖管理以及发布到生产环境时的自动化打包与处理等多个问题，试想一下，脱离了模块化开发方式，我们的代码组织将会非常令人头痛，使用文件同时还得考虑其内部错综复杂的依赖关系。</p>
<p>2.模块化规范🏁</p>
<p>在Es6之前,<code>AMD/CMD/CommonJs</code>是JS模块化开发的标准，对应的实现是<code>RequireJs/SeaJs/nodeJs</code>. CommonJs主要针对服务端，AMD/CMD主要针对浏览器端。最常见的在node模块中，采用的是CommonJS规范，暴露模块使用module.exports和exports，而对应有一个全局性方法require用于加载模块。</p>
<h3 data-id="heading-3">现阶段的标准ES module</h3>
<p>ES6标准发布后，module成为标准，标准使用是以export指令导出接口，以import引入模块，很好的取代了之前的commonjs和AMD规范,成为了浏览器和服务器的通用的模块解决方案。</p>
<p><strong>存在兼容性问题，需要支持es6，通常使用</strong>babel<strong>将es6编译成es5语法向下兼容。</strong></p>
<blockquote>
<p><a href="https://www.cnblogs.com/libin-1/p/7127481.html" target="_blank" rel="nofollow noopener noreferrer">彻底搞清楚javascript中的require、import和export</a></p>
</blockquote>
<h2 data-id="heading-4">webpack简介</h2>
<blockquote>
<p>本质上，webpack 是一个现代 JavaScript 应用程序的静态模块打包器(module bundler)。当 webpack 处理应用程序时，它会递归地构建一个依赖关系图(dependency graph)，其中包含应用程序需要的每个模块，然后将所有这些模块打包成一个或多个 bundle。</p>
</blockquote>
<p>先介绍一下<strong>webpack</strong>中的核心概念</p>
<ol>
<li>入口(entry)  webpack构建时的入口文件，从这里开始建立依赖关系，可以是一个或多个入口</li>
<li>输出(output) 指定webpack的打包产物bundle的纯输出目录，同样也有一个或者多个</li>
<li>loader 负责将webpack不能识别的文件类型（js除外）转换为 webpack 能够处理的有效模块</li>
<li>插件(plugins) webpack强大的根源，在构建的不同阶段会广播出对应的钩子事件，监听这些事件就可以对打包过程做高度自定义处理，包括，从打包优化和压缩，一直到重新定义环境中的变量。</li>
</ol>
<h2 data-id="heading-5">实现mini-webpack</h2>
<p>根据上文的介绍，我们梳理出一个基本的打包器应该帮我们处理哪几件事：</p>
<ol>
<li>根据配置文件找到打包入口</li>
<li>解析入口文件，收集他的依赖</li>
<li><strong>递归地寻找依赖的关系，建立文件间的依赖图</strong></li>
<li>把所有文件打包成一个文件</li>
</ol>
<h3 data-id="heading-6">基本配置</h3>
<p>先初始化一个项目：</p>
<pre><code class="hljs language-js copyable" lang="js">npm init -y
<span class="copy-code-btn">复制代码</span></code></pre>
<p>创建src目录，在src目录下新建文件module-1.js,module-2.js,module-3.js如下：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// module-1.js</span>
<span class="hljs-keyword">import</span> res <span class="hljs-keyword">from</span> <span class="hljs-string">'./module-2'</span>

<span class="hljs-built_in">console</span>.log(<span class="hljs-string">`mini-webpack: <span class="hljs-subst">$&#123;res&#125;</span>`</span>);
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// module-2.js</span>
<span class="hljs-keyword">import</span> module3 <span class="hljs-keyword">from</span> <span class="hljs-string">'./module3'</span>
<span class="hljs-keyword">let</span> res = <span class="hljs-string">`module2 import <span class="hljs-subst">$&#123;module3&#125;</span> from module-3.js`</span>
<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> res
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// module-3.js</span>
<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> <span class="hljs-string">'hello world
</span><span class="copy-code-btn">复制代码</span></code></pre>
<p>可以很轻易地看出依赖关系如下：
<code>module1 -> module2 -> module3</code></p>
<p>新建文件<code>mini-webpack-config.js</code>作为我们mini-webpack的配置文件，结构就借鉴正版webpack：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> path = <span class="hljs-built_in">require</span>(<span class="hljs-string">"path"</span>);
<span class="hljs-built_in">module</span>.exports = &#123;
  <span class="hljs-attr">entry</span>: <span class="hljs-string">"./src/module-1.js"</span>,
  <span class="hljs-attr">output</span>: &#123;
    <span class="hljs-attr">path</span>: path.join(__dirname, <span class="hljs-string">"./dist"</span>),
    <span class="hljs-attr">filename</span>: <span class="hljs-string">"bundle.js"</span>,
  &#125;,
&#125;;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-7">解析配置，得到entry入口</h3>
<p>新建文件<code>mini-webpack.js</code></p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// mini-webpack.js</span>
<span class="hljs-keyword">const</span> fs = <span class="hljs-built_in">require</span>(<span class="hljs-string">"fs"</span>);
<span class="hljs-keyword">const</span> path = <span class="hljs-built_in">require</span>(<span class="hljs-string">"path"</span>);
<span class="hljs-comment">// 读取配置</span>
<span class="hljs-keyword">const</span> config = <span class="hljs-built_in">require</span>(<span class="hljs-string">"./mini-webpack-config.js"</span>);

<span class="hljs-comment">// 主函数</span>
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">main</span>(<span class="hljs-params"></span>) </span>&#123;
  <span class="hljs-keyword">let</span> absPath = path.resolve(__dirname, config.entry);
  <span class="hljs-keyword">let</span> entry = fs.readFileSync(absPath, <span class="hljs-string">"utf-8"</span>);
  <span class="hljs-built_in">console</span>.log(entry);
&#125;
main();
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这一步比较简单，用node文件模块帮我们读取entry入口内容</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/6b2dd133328347438e8a1b77ea6bdf63~tplv-k3u1fbpfcp-watermark.image" alt="~F_)Y054CSSIAFTN8EHZIZ6.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-8">分析ast，抽离依赖</h3>
<p>第一步，如何从文件内容中知道我们引用了哪些模块？</p>
<p>这里用了解析ast tree的方法, 是源代码语法结构的一种抽象表示。它以树状的形式表现编程语言的语法结构，树上的每个节点都表示源代码中的一种结构。（其实用正则是否也可行呢 🙋）
<img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/f6e2585fe4e84524a9ac9a2b18b8f245~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>可以看到： ImportDeclaration对象的source属性的value就是我们要找的依赖。</p>
<p>我们可以借助<code>@babel/parser</code>将代码编译成ast</p>
<pre><code class="hljs language-js copyable" lang="js">npm i @babel/parser
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> babelParser = <span class="hljs-built_in">require</span>(<span class="hljs-string">"@babel/parser"</span>);
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">main</span>(<span class="hljs-params"></span>) </span>&#123;
  <span class="hljs-keyword">let</span> absPath = path.resolve(__dirname, config.entry);
  <span class="hljs-keyword">let</span> content = fs.readFileSync(absPath, <span class="hljs-string">"utf-8"</span>);
  <span class="hljs-built_in">console</span>.log(
    babelParser.parse(content, &#123;
      <span class="hljs-comment">// 指示解析代码的模式，默认是script 需要指定为模块module</span>
      <span class="hljs-attr">sourceType</span>: <span class="hljs-string">"module
    &#125;)
  );
&#125;
</span><span class="copy-code-btn">复制代码</span></code></pre>
<p>这样便能得到代码在ast树上的结构：</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/9e3b984d1c2b467caa395a80df8cc544~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>第二步，需要对节点的body内容进行遍历，找到上文所说的<code>ImportDeclaration</code>对象，从而拿到文件依赖关系，可借助babel为我们提供的工具<code>@babel/traverse</code></p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// 安装</span>
npm i @babel/traverse
-------------------------------
<span class="hljs-keyword">const</span> traverse = <span class="hljs-built_in">require</span>(<span class="hljs-string">"@babel/traverse"</span>).default;
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">main</span>(<span class="hljs-params"></span>) </span>&#123;
  <span class="hljs-keyword">let</span> entry = config.entry;
  <span class="hljs-keyword">let</span> content = fs.readFileSync(entry, <span class="hljs-string">"utf-8"</span>);
  <span class="hljs-comment">// 依赖存储  </span>
  <span class="hljs-keyword">let</span> dependecies = []
  <span class="hljs-keyword">let</span> ast = babelParser.parse(content, &#123;
    <span class="hljs-attr">sourceType</span>: <span class="hljs-string">"module"</span>, <span class="hljs-comment">//指示应该在其中解析代码的模式。带有ES6导入和导出的文件被认为是“模块”，否则就是“脚本”。</span>
  &#125;);
  traverse(ast, &#123;
    <span class="hljs-attr">ImportDeclaration</span>: <span class="hljs-function">(<span class="hljs-params">&#123; node &#125;</span>) =></span> &#123;
      dependecies.push(node.source.value)
    &#125;,
  &#125;);


  <span class="hljs-comment">// --> ['./module-2.js']</span>
  <span class="hljs-built_in">console</span>.log(dependecies); 
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>考虑到复用性，我们把主函数内容封装一下，函数<code>collectDependencies</code>根据传入文件名返回依赖对象，增加一个递增的id属性.</p>
<pre><code class="copyable">// 主函数
function main() &#123;
  let entry = config.entry;
  collectDependencies(entry)
  
&#125;
/**
 * 根据传入文件找到依赖
 * @param &#123;*&#125; filename 
 * @returns 
 */
function collectDependencies(filename) &#123;
  let code = fs.readFileSync(filename, "utf-8");
  let dependecies = [];
  let ast = babelParser.parse(code, &#123;
    sourceType: "module", //指示应该在其中解析代码的模式。带有ES6导入和导出的文件被认为是“模块”，否则就是“脚本”。
  &#125;);
  traverse(ast, &#123;
    ImportDeclaration: (&#123; node &#125;) => &#123;
      // console.log(node);
      dependecies.push(node.source.value);
    &#125;,
  &#125;);
  let id = ID++
  return &#123;
  id,
  filename,
  dependecies
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-9">构建依赖图</h3>
<p>当前我们已经获取了module1的依赖（module2），所以接下来要做的事情是：寻找依赖(module2)的依赖（module3），构建依赖图，用<code>allAsset</code>表示依赖图，遍历<code>allAsset</code>，并且将每次循环找出来的依赖推入<code>allAsset</code>，这样获得的就是完整的依赖关系</p>
<ul>
<li>需要注意因为我们import使用的是相对路径，dependecies里的路径是相对于module-1的路径，和我们当前的文件mini-webpack.js不在一个目录下的,需要一层路径转换处理。</li>
<li><strong>新增一个属性mapping存储路径与依赖的id之间的映射关系，后续打包生成bundle有用</strong></li>
</ul>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// 主函数</span>
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">main</span>(<span class="hljs-params"></span>) </span>&#123;
  <span class="hljs-keyword">let</span> entry = config.entry;
  <span class="hljs-keyword">let</span> mainAsset = collectDependencies(entry);
  <span class="hljs-comment">//构建依赖图</span>
  <span class="hljs-keyword">let</span> graph = createDependGraph(mainAsset);
&#125;

<span class="hljs-comment">/**
 * 入口的依赖
 * <span class="hljs-doctag">@param <span class="hljs-type">&#123;*&#125;</span> </span>mainAsset 
 * <span class="hljs-doctag">@returns </span>
 */</span>
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">createDependGraph</span>(<span class="hljs-params">mainAsset</span>) </span>&#123;
  <span class="hljs-keyword">let</span> allAsset = [mainAsset];
  <span class="hljs-keyword">let</span> i = <span class="hljs-number">0</span>;
  <span class="hljs-keyword">while</span> (i < allAsset.length) &#123;
    <span class="hljs-keyword">let</span> asset = allAsset[i];
    <span class="hljs-keyword">let</span> dirname = path.dirname(asset.filename);
    asset.mapping = &#123;&#125;;
    asset.dependecies.forEach(<span class="hljs-function">(<span class="hljs-params">relativePath</span>) =></span> &#123;
      <span class="hljs-keyword">let</span> absPath = path.join(dirname, relativePath);
      <span class="hljs-keyword">let</span> childAsset = collectDependencies(absPath);
      asset.mapping[relativePath] = childAsset.id;
      allAsset.push(childAsset);
    &#125;);
    i++;
  &#125;
  <span class="hljs-keyword">return</span> allAsset;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>获得输出如下：
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/981ebf83335645e59ffefccd77965077~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-10">ast转换es5</h3>
<p>最终我们的目标是要把多个文件打包成一个文件，所以需要先获得文件里面的内容。而前文已经提到了，我们代码里面的import要被浏览器识别需要经过babel转译，它可以帮你将 ECMAScript 2015+ 版本的代码转换为向后兼容的 JavaScript 语法，这个过程是通过修改<strong>ast</strong>实现的。</p>
<p>需要安装两个工具包<code>babel-core</code>和<code>babel-preset-env</code>,对<code>collectDependencies</code>函数稍作修改：</p>
<pre><code class="hljs language-js copyable" lang="js">npm i babel-core babel-preset-env
-------------------------------------------分割线
<span class="hljs-keyword">const</span> core = <span class="hljs-built_in">require</span>(<span class="hljs-string">"babel-core"</span>);

<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">collectDependencies</span>(<span class="hljs-params">filename</span>) </span>&#123;
  <span class="hljs-keyword">let</span> content = fs.readFileSync(filename, <span class="hljs-string">"utf-8"</span>);
  <span class="hljs-keyword">let</span> dependecies = [];
  <span class="hljs-keyword">const</span> ast = babaylon.parse(content, &#123;
    <span class="hljs-comment">//指定解析代码的模式，默认‘script’，带有ES6导入和导出的文件被认为是“模块”</span>
    <span class="hljs-attr">sourceType</span>: <span class="hljs-string">"module"</span>, 
  &#125;);
  traverse(ast, &#123;
    <span class="hljs-attr">ImportDeclaration</span>: <span class="hljs-function">(<span class="hljs-params">&#123; node &#125;</span>) =></span> &#123;
      dependecies.push(node.source.value);
    &#125;,
  &#125;);
  <span class="hljs-comment">// ast -->  es5</span>
  <span class="hljs-keyword">let</span> &#123; code &#125; = core.transformFromAst(ast, <span class="hljs-literal">null</span>, &#123;
    <span class="hljs-attr">presets</span>: [<span class="hljs-string">"env"</span>],
  &#125;);

  <span class="hljs-keyword">let</span> id = ID++;
  <span class="hljs-keyword">return</span> &#123;
    id,
    filename,
    dependecies,
    code,
  &#125;;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>看看当前返回的是个啥：</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/347f82aa302b442e99e338ba081b0955~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>似曾相识的感觉，有require，有module，exports...是不是很像commonjs模块化规范？其实项目中本质就是使用babel将es6转码为es5再执行，import会被转码为require。</p>
<h3 data-id="heading-11">打包成bundle</h3>
<p>这一步不是特别很好理解，我是对照着原版webpack打包后的bundle反推回来的。
先思考一下bundle函数需要做到的事情：</p>
<ol>
<li>首先我们需要返回一个字符串代码块</li>
<li>代码块要需要可以自动执行</li>
<li>需要运行每个依赖模块的code</li>
</ol>
<p>上文提到将import转码为require，但是浏览器端本身不会提供<strong>require，exports，module</strong>,所以我们需要一个函数提供入参，将编译后的代码代码作为模块对应这个函数的函数体执行，外部提供这三个参数传入。</p>
<p>此时需要构造模块与这个函数间的对应关系,上面的模块id可以作为标识。</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/41f5a13899094f4d9ba60e65a97b722d~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer">
（webpack使用了文件路径做标识，key为模块路径，value为模块的可执行函数，用文件路径就不需要mapping和localRequire，更加直观，不过要统一路径格式，只要能通过require找到可执行函数就行）</p>
<p>代码如下：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// 主函数</span>
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">main</span>(<span class="hljs-params"></span>) </span>&#123;
  <span class="hljs-keyword">let</span> entry = config.entry;
  <span class="hljs-keyword">let</span> mainAsset = collectDependencies(entry);

  <span class="hljs-comment">//构建依赖图</span>
  <span class="hljs-keyword">let</span> graph = createDependGraph(mainAsset);
  <span class="hljs-comment">//输出</span>
  <span class="hljs-keyword">let</span> res = bundle(graph);  
  
  
  <span class="hljs-comment">//输出目录</span>
  <span class="hljs-keyword">if</span> (!fs.existsSync(config.output.path)) &#123;
    fs.mkdirSync(config.output.path);
  &#125;
  <span class="hljs-comment">// 输出文件</span>
  <span class="hljs-keyword">let</span> opath = path.join(config.output.path, config.output.filename);

  <span class="hljs-keyword">if</span> (fs.existsSync(opath)) &#123;
    fs.unlinkSync(opath);
  &#125;
  <span class="hljs-keyword">let</span> ws = fs.createWriteStream(opath, &#123;
    <span class="hljs-attr">encoding</span>: <span class="hljs-string">"utf-8"</span>,
  &#125;);
  
  ws.write(res);
&#125;

<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">bundle</span>(<span class="hljs-params">graph</span>) </span>&#123;
  <span class="hljs-keyword">let</span> modules = <span class="hljs-string">""</span>;
  
  graph.forEach(<span class="hljs-function">(<span class="hljs-params"><span class="hljs-built_in">module</span></span>) =></span> &#123;
    <span class="hljs-comment">// 遍历依赖图，构造模块与这个函数间的对应关系</span>
    modules += <span class="hljs-string">`
    <span class="hljs-subst">$&#123;<span class="hljs-built_in">module</span>.id&#125;</span>: [
      function(require,module,exports)&#123;
        <span class="hljs-subst">$&#123;<span class="hljs-built_in">module</span>.code&#125;</span>
      &#125;,
      <span class="hljs-subst">$&#123;<span class="hljs-built_in">JSON</span>.stringify(<span class="hljs-built_in">module</span>.mapping)&#125;</span>
    ],
    `</span>;
  &#125;);
 
  <span class="hljs-keyword">let</span> res = <span class="hljs-string">`
  (function(modules)&#123;
    function require(id) &#123;
    
      // fn：执行模块代码 给exports赋值
      // mapping： &#123;相对路径：依赖id &#125; 映射
      let [fn,mapping] = modules[id]
      
      // 作用：相对路径转成模块id 
      // 原因：代码内是require('相对路径')的形式
      function localRequire(relativePath) &#123;
        return require(mapping[relativePath])
      &#125;
      let module = &#123;exports:&#123;&#125;&#125;
      // 在fn内部modul.exports被重新赋值了
      fn(localRequire,module,module.exports)
      // 这就是模块的导出
      return module.exports
    &#125;
    // id-0对应entry
    return require(0)
  &#125;)(&#123;<span class="hljs-subst">$&#123;modules&#125;</span>&#125;)
  `</span>;

  <span class="hljs-keyword">return</span> res;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>最终成功在dist目录下生成bundle.js,在html中引入bundles.js执行测试，输出了预期的结果。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/4b45effbb773403783d9279d86719ade~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/7aae4a554d924925bc1b54f60ac8bbfd~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-12">打包优化</h3>
<p>引入uglify-js对打包文件压缩，新增build命令方便打包</p>
<pre><code class="hljs language-js copyable" lang="js">npm i uglify-js -g
-------------------------------
<span class="hljs-comment">// package.json</span>

<span class="hljs-string">"scripts"</span>: &#123;
    <span class="hljs-string">"build"</span>: <span class="hljs-string">"node mini-webpack.js && uglifyjs ./dist/bundle.js -m -o ./dist/bundle.js"</span>
  &#125;,
<span class="copy-code-btn">复制代码</span></code></pre>
<p>可以看到代码压缩成一行，减小了体积，并且隐藏了变量名，增强了源码安全性。webpack还考虑到了模块的缓存和按需加载等场景，这是我们可以学习优化的地方</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/5d38058332fd4161a9d5a062c23ee7df~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-13">后记</h2>
<p>本文介绍了webpack对模块进行打包的原理，从0到1地完成了一个最小化的mini-webpack，虽然功能上还有许多不完善，但是重在学习分析解决问题的思路，在这个过程也对babel是如何转译我们的代码的有了更直观的认识。代码中有疑问或者不对的地方欢迎各位批评指正，共同进步。求点赞三连QAQ🔥🔥</p>
<p>链接：</p>
<blockquote>
<ul>
<li><a href="https://www.jianshu.com/p/32db2f258986" target="_blank" rel="nofollow noopener noreferrer">聊一聊 Javascript 中的 AST</a></li>
<li><a href="https://juejin.cn/post/6859569958742196237" target="_blank">你的 import 被 webpack 编译成了什么？</a></li>
<li><a href="https://astexplorer.net/" target="_blank" rel="nofollow noopener noreferrer">astexplorer在线</a></li>
</ul>
</blockquote></div>  
</div>
            