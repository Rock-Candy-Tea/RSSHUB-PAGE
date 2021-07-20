
---
title: '☝️ webpack5 + react + typescript环境配置代码完全指南(信息密度点大，老铁来挑战不？)'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/a90327edce1c430eac2da36d80452b7e~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Mon, 19 Jul 2021 05:01:47 GMT
thumbnail: 'https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/a90327edce1c430eac2da36d80452b7e~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h2 data-id="heading-0">前言</h2>
<p>本文是对某开源的项目<code>webpack5 + react + typescript</code><a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fvortesnail%2Freact-ts-quick-starter" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/vortesnail/react-ts-quick-starter" ref="nofollow noopener noreferrer">项目地址</a>逐行代码做分析，解剖一个成熟的环境所有配置的意义，理清一些常见的问题，比如</p>
<ul>
<li>
<p>文件中的 <code>import</code> 转<code>es5</code>被 <code>webpack</code> 编译成了什么？webpack的分包配置splitChunks咋用? 你真的理解其选项值<code>chunks</code>的值<code>async</code>或者<code>initial</code>或者<code>all</code>是什么意思吗，这个可对分包优化至关重要啊！为什么<code>package.json</code>没有依赖的包，在<code>node_modules</code>下面会出现，<code>npm install</code>包是以什么结构安装npm包呢？</p>
</li>
<li>
<p><code>babel/core</code>有什么用，它跟<code>babel-loader</code>的区别, <code>babelrc</code>文件中配置项<code>presets</code>和<code>plugin</code>的区别是什么，<code>babelrc</code>常用设置项知道多少，这个不清楚？那项目代码校验和格式化用到<code>editorConfig、prettier、eslint，stylelint</code>他们的关系和区别是什么？如何配置防止它们冲突，比如<code>eslint</code>也有<code>css</code>校验，怎么让<code>stylelint</code>跟它不起冲突，这些你要晋升为前端主管怎么能心里没数？</p>
</li>
<li>
<p>如果你用的<code>vscode</code>，如何在工作区配置<code>ctrl+s</code>自动保存，让你的js和css文件自动格式化，并配置为<code>prettier</code>格式化，<code>webpack5</code>和<code>4</code>的配置中的变化、等等。。。</p>
</li>
</ul>
<p>以上提到的知识点对我们深入了解<code>项目环境搭建</code>非常重要， 你的项目你来时一般环境都是搭建好的，试过从0自己搭建不？是不是抄别人的配置，都一头雾水，完全不知道这些配置项时啥意思呢？</p>
<p>现在！本篇本章专解这个问题！废话少说，</p>
<p>我们先从<code>package.json</code>说起，里面的每一行代码是什么意思。</p>
<h2 data-id="heading-1">package.json</h2>
<p><code>package.json</code>里面有很多有趣的内容，我们先从依赖包说起，解释这个项目中，下面的依赖包分别有什么用。</p>
<pre><code class="hljs language-javascript copyable" lang="javascript">  <span class="hljs-string">"devDependencies"</span>: &#123;
    <span class="hljs-string">"@babel/core"</span>: <span class="hljs-string">"^7.13.13"</span>,
    <span class="hljs-string">"@babel/plugin-transform-runtime"</span>: <span class="hljs-string">"^7.13.10"</span>,
    <span class="hljs-string">"@babel/preset-env"</span>: <span class="hljs-string">"^7.13.12"</span>,
    <span class="hljs-string">"@babel/preset-react"</span>: <span class="hljs-string">"^7.13.13"</span>,
    <span class="hljs-string">"@babel/preset-typescript"</span>: <span class="hljs-string">"^7.13.0"</span>,
    <span class="hljs-string">"@commitlint/cli"</span>: <span class="hljs-string">"^12.0.1"</span>,
    <span class="hljs-string">"@commitlint/config-conventional"</span>: <span class="hljs-string">"^12.0.1"</span>,
    <span class="hljs-string">"@types/react"</span>: <span class="hljs-string">"^17.0.3"</span>,
    <span class="hljs-string">"@types/react-dom"</span>: <span class="hljs-string">"^17.0.3"</span>,
    <span class="hljs-string">"@types/webpack-env"</span>: <span class="hljs-string">"^1.16.0"</span>,
    <span class="hljs-string">"@typescript-eslint/eslint-plugin"</span>: <span class="hljs-string">"^4.19.0"</span>,
    <span class="hljs-string">"@typescript-eslint/parser"</span>: <span class="hljs-string">"^4.19.0"</span>,
    <span class="hljs-string">"babel-loader"</span>: <span class="hljs-string">"^8.2.2"</span>,
    <span class="hljs-string">"chalk"</span>: <span class="hljs-string">"^4.1.0"</span>,
    <span class="hljs-string">"clean-webpack-plugin"</span>: <span class="hljs-string">"^3.0.0"</span>,
    <span class="hljs-string">"conventional-changelog-cli"</span>: <span class="hljs-string">"^2.1.1"</span>,
    <span class="hljs-string">"copy-webpack-plugin"</span>: <span class="hljs-string">"^8.1.0"</span>,
    <span class="hljs-string">"cross-env"</span>: <span class="hljs-string">"^7.0.3"</span>,
    <span class="hljs-string">"css-loader"</span>: <span class="hljs-string">"^5.2.0"</span>,
    <span class="hljs-string">"css-minimizer-webpack-plugin"</span>: <span class="hljs-string">"^1.3.0"</span>,
    <span class="hljs-string">"detect-port-alt"</span>: <span class="hljs-string">"^1.1.6"</span>,
    <span class="hljs-string">"error-overlay-webpack-plugin"</span>: <span class="hljs-string">"^0.4.2"</span>,
    <span class="hljs-string">"eslint"</span>: <span class="hljs-string">"^7.22.0"</span>,
    <span class="hljs-string">"eslint-config-airbnb"</span>: <span class="hljs-string">"^18.2.1"</span>,
    <span class="hljs-string">"eslint-config-prettier"</span>: <span class="hljs-string">"^8.1.0"</span>,
    <span class="hljs-string">"eslint-import-resolver-typescript"</span>: <span class="hljs-string">"^2.4.0"</span>,
    <span class="hljs-string">"eslint-plugin-import"</span>: <span class="hljs-string">"^2.22.1"</span>,
    <span class="hljs-string">"eslint-plugin-jsx-a11y"</span>: <span class="hljs-string">"^6.4.1"</span>,
    <span class="hljs-string">"eslint-plugin-prettier"</span>: <span class="hljs-string">"^3.3.1"</span>,
    <span class="hljs-string">"eslint-plugin-promise"</span>: <span class="hljs-string">"^4.3.1"</span>,
    <span class="hljs-string">"eslint-plugin-react"</span>: <span class="hljs-string">"^7.23.1"</span>,
    <span class="hljs-string">"eslint-plugin-react-hooks"</span>: <span class="hljs-string">"^4.2.0"</span>,
    <span class="hljs-string">"eslint-plugin-unicorn"</span>: <span class="hljs-string">"^29.0.0"</span>,
    <span class="hljs-string">"fork-ts-checker-webpack-plugin"</span>: <span class="hljs-string">"^6.2.0"</span>,
    <span class="hljs-string">"html-webpack-plugin"</span>: <span class="hljs-string">"^5.3.1"</span>,
    <span class="hljs-string">"husky"</span>: <span class="hljs-string">"^4.3.8"</span>,
    <span class="hljs-string">"ip"</span>: <span class="hljs-string">"^1.1.5"</span>,
    <span class="hljs-string">"is-root"</span>: <span class="hljs-string">"^2.1.0"</span>,
    <span class="hljs-string">"lint-staged"</span>: <span class="hljs-string">"^10.5.4"</span>,
    <span class="hljs-string">"mini-css-extract-plugin"</span>: <span class="hljs-string">"^1.4.0"</span>,
    <span class="hljs-string">"node-sass"</span>: <span class="hljs-string">"^5.0.0"</span>,
    <span class="hljs-string">"postcss"</span>: <span class="hljs-string">"^8.2.8"</span>,
    <span class="hljs-string">"postcss-flexbugs-fixes"</span>: <span class="hljs-string">"^5.0.2"</span>,
    <span class="hljs-string">"postcss-loader"</span>: <span class="hljs-string">"^5.2.0"</span>,
    <span class="hljs-string">"postcss-preset-env"</span>: <span class="hljs-string">"^6.7.0"</span>,
    <span class="hljs-string">"prettier"</span>: <span class="hljs-string">"^2.2.1"</span>,
    <span class="hljs-string">"sass-loader"</span>: <span class="hljs-string">"^11.0.1"</span>,
    <span class="hljs-string">"style-loader"</span>: <span class="hljs-string">"^2.0.0"</span>,
    <span class="hljs-string">"stylelint"</span>: <span class="hljs-string">"^13.12.0"</span>,
    <span class="hljs-string">"stylelint-config-prettier"</span>: <span class="hljs-string">"^8.0.2"</span>,
    <span class="hljs-string">"stylelint-config-rational-order"</span>: <span class="hljs-string">"^0.1.2"</span>,
    <span class="hljs-string">"stylelint-config-standard"</span>: <span class="hljs-string">"^21.0.0"</span>,
    <span class="hljs-string">"stylelint-declaration-block-no-ignored-properties"</span>: <span class="hljs-string">"^2.3.0"</span>,
    <span class="hljs-string">"stylelint-order"</span>: <span class="hljs-string">"^4.1.0"</span>,
    <span class="hljs-string">"stylelint-scss"</span>: <span class="hljs-string">"^3.19.0"</span>,
    <span class="hljs-string">"terser-webpack-plugin"</span>: <span class="hljs-string">"^5.1.1"</span>,
    <span class="hljs-string">"typescript"</span>: <span class="hljs-string">"^4.2.3"</span>,
    <span class="hljs-string">"webpack"</span>: <span class="hljs-string">"^5.37.1"</span>,
    <span class="hljs-string">"webpack-bundle-analyzer"</span>: <span class="hljs-string">"^4.4.0"</span>,
    <span class="hljs-string">"webpack-cli"</span>: <span class="hljs-string">"^4.5.0"</span>,
    <span class="hljs-string">"webpack-dev-server"</span>: <span class="hljs-string">"^3.11.2"</span>,
    <span class="hljs-string">"webpack-merge"</span>: <span class="hljs-string">"^5.7.3"</span>,
    <span class="hljs-string">"webpackbar"</span>: <span class="hljs-string">"^5.0.0-3"</span>
  &#125;,
  <span class="hljs-string">"dependencies"</span>: &#123;
    <span class="hljs-string">"@babel/runtime-corejs3"</span>: <span class="hljs-string">"^7.13.10"</span>,
    <span class="hljs-string">"react"</span>: <span class="hljs-string">"^17.0.2"</span>,
    <span class="hljs-string">"react-dom"</span>: <span class="hljs-string">"^17.0.2"</span>
  &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-2">@babel/core有啥用？</h3>
<p><code>babel</code> 的功能在于<code>「代码转译」</code>，具体一点，即将目标代码转译为能够符合期望语法规范的代码。在转译的
过程中，<code>babel</code> 内部经历了<code>「解析 - 转换 - 生成」</code>三个步骤。而 <code>@babel/core</code> 这个库则负责<code>「解析」</code>，具体的<code>「转换」</code>和<code>「生成」</code>步骤则交给各种插件（plugin）和预设（preset）来完成。</p>
<p>你可以从<code>@babel/core</code>自己的依赖里看到其中有三个包，叫<code>@babel/generator</code> (将ast生成代码)、 <code>@babel/parser</code>（将源代码转换为AST）、<code>@babel/traverse</code>（转换AST）,有这三个包，就能转换你的代码，案例如下：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">import</span> &#123; parse &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'@babel/parser'</span>;
<span class="hljs-keyword">import</span> traverse <span class="hljs-keyword">from</span> <span class="hljs-string">'@babel/traverse'</span>;
<span class="hljs-keyword">import</span> generate <span class="hljs-keyword">from</span> <span class="hljs-string">'@babel/generator'</span>;

<span class="hljs-keyword">const</span> code = <span class="hljs-string">'const n = 1'</span>;

<span class="hljs-comment">// 将源代码转换为AST</span>
<span class="hljs-keyword">const</span> ast = parse(code);

<span class="hljs-comment">// 转换AST</span>
traverse(ast, &#123;
  <span class="hljs-function"><span class="hljs-title">enter</span>(<span class="hljs-params">path</span>)</span> &#123;
    <span class="hljs-comment">// in this example change all the variable `n` to `x`</span>
    <span class="hljs-keyword">if</span> (path.isIdentifier(&#123; <span class="hljs-attr">name</span>: <span class="hljs-string">'n'</span> &#125;)) &#123;
      path.node.name = <span class="hljs-string">'x'</span>;
    &#125;
  &#125;,
&#125;);

<span class="hljs-comment">// 生成代码 <- ast</span>
<span class="hljs-keyword">const</span> output = generate(ast, code);
<span class="hljs-built_in">console</span>.log(output.code); <span class="hljs-comment">// 'const x = 1;'</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这应该非常清楚的了解<code>babel／core</code>有什么用了吧，至于说怎么在<code>traverse</code>阶段改变代码，就要用到其他的插件了，我们马上说一下<code>babel-loader</code>，让你明白它跟<code>babel／core</code>的区别</p>
<h3 data-id="heading-3">babel-loader</h3>
<p>我们知道<code>webpack</code>需要各种<code>loader</code>，这些<code>loader</code>的作用就是把文件做转化，比如<code>babel-loader</code>是用来转化<code>js</code>，<code>jsx</code>，<code>ts</code>，<code>tsx</code>文件的。</p>
<p>比如我们写的<code>js</code>代码是<code>es6</code>，<code>import xx模块 from ‘xx模块’</code>，为了浏览器兼容性，我们需要转化为<code>es5</code>的写法，转译<code>import</code>，那么这个时候就需要<code>babel-loader</code>来帮忙了。</p>
<p>比如说一个简单的<code>loader</code>怎么写呢，我们就知道<code>babel-loader</code>大概是个什么东西了，</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-built_in">module</span>.exports = <span class="hljs-function"><span class="hljs-params">source</span> =></span> &#123;
<span class="hljs-comment">// source 就是加载到的文件内容</span>
<span class="hljs-built_in">console</span>.log(source)
<span class="hljs-keyword">return</span> <span class="hljs-string">"hello ~"</span> <span class="hljs-comment">// 返回一个字符串</span>
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>上面我们把任何加载到的文件内容转化为一个字符串，也就是<code>loader</code>无非是加工读到的文件，所以<code>babel-loader</code>就是读取对应的<code>jsx?|tsx?</code>文件,然后加工后返回而已</p>
<h3 data-id="heading-4">prest家族：@babel/preset-env、@babel/preset-react、@babel/preset-typescript、</h3>
<ul>
<li>@babel/preset-typescript: 主要是用来编译<code>ts</code>文件的。</li>
</ul>
<p>目前<code> TypeScript</code> 的编译有两种方式。一种是使用 <code>TypeScript</code> 自家的编译器 <code>typescript</code> 编译（简称 TS 编译器），一种就是使用<code> Babel + @babel/preset-typescript</code> 编译。</p>
<p>其中最好的选择就是使用<code>Babel + @babel/preset-typescript</code>，主要原因是：</p>
<ul>
<li><code>Babel</code> 能够指定需要编译的浏览器环境。这一点 TS 编译器是不支持的。在<code>babelrc</code>文件里可以设置编译的<code>target</code>属性（在<code>preset-env</code>插件上设置）为比如</li>
</ul>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-string">"targets"</span>: &#123;
  <span class="hljs-string">"browsers"</span>: [<span class="hljs-string">"last 2 versions"</span>, <span class="hljs-string">"safari >= 7"</span>], <span class="hljs-comment">// 配置safari的版本大于7的语法才转译</span>
  <span class="hljs-string">"node"</span>: <span class="hljs-string">"6.10"</span> <span class="hljs-comment">// node版本支持到6.10</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li><code>TS</code> 编译器在编译过程中进行类型检查，类型检查是需要时间的，而 <code>babel</code> 不做类型检查，编译速度就更快</li>
</ul>
<p>@babel/preset-react: 主要是编译<code>jsx</code>文件的，也就是解析<code>jsx语</code>法的，比如说<code>react</code>生成div，我们举一个例子，在jsx里面是这样的，转换成什么了呢？</p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">div</span>></span><span class="hljs-tag"></<span class="hljs-name">div</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>转化后的<code>react</code>的<code>api</code></p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">const</span> reactElement = ReactElement.createElement(
  ... <span class="hljs-comment">// 标签名称字符串/ReactClass,</span>
  ... <span class="hljs-comment">// [元素的属性值对对象],</span>
  ... <span class="hljs-comment">// [元素的子节点]</span>
)
reactElement(<span class="hljs-string">'div'</span>, <span class="hljs-literal">null</span>, <span class="hljs-string">''</span>)
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>@babel/preset-env:</li>
</ul>
<p><code>@babel/preset-env</code>将基于你的实际浏览器及运行环境，自动的确定<code>babel</code>插件及<code>polyfill</code>，在不进行任何配置的情况下，<code>@babel/preset-env</code>所包含的插件将支持所有最新的JS特性(<code>ES2015</code>,<code>ES2016</code>等，不包含 <code>stage</code> 阶段)，将其转换成<code>ES5</code>代码。例，那么只配置 <code>@babel/preset-env</code>，转换时会抛出错误，需要另外安装相应的插件。</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">//.babelrc</span>

&#123;

<span class="hljs-string">"presets"</span>: [<span class="hljs-string">"@babel/preset-env"</span>]

&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>注意：<code>@babel/preset-env</code>会根据你配置的目标环境，生成插件列表来编译。<code>Babel</code> 官方建议我们把 <code>targets </code>的内容保存到 <code>.browserslistrc</code>文件中 或者 <code>package.json</code> 里增加一个<code>browserslit</code>节点，不然除了<code>babel</code>外，其他的工具，例如<code>browserslist</code>、<code>post-css</code>等无法从 <code>babel</code> 配置文件里读取配置</p>
<p>如果你不是要兼容所有的浏览器和环境，推荐你指定目标环境，这样你的编译代码能够保持最小。</p>
<p>具体用法我们会在将<code>babelrc</code>文件配置（<code>babel</code>的配置文件）的时候详细说明。</p>
<h3 data-id="heading-5">@babel/plugin-transform-runtime、@babel/runtime-corejs</h3>
<p>为什么我们需要它，我们来看看<code>@babel/prest-env</code>编译完js文件后，会有哪些问题</p>
<ul>
<li>
<p>比如我们使用字符串的inclues语法（es5中并不支持它，需要转译）, 例如<code> Array.from</code> 等静态方法，直接在 <code>global.Array</code> 上添加；对于例如 includes 等实例方法，直接在<code>global.Array.prototype</code>上添加。这样直接修改了全局变量的原型。</p>
</li>
<li>
<p><code>babel</code> 转译 syntax 时，有时候会使用一些辅助的函数来帮忙转，比如：</p>
</li>
</ul>
<p>class 语法中，babel 自定义了 <code>_classCallCheck</code>这个函数来辅助；<code>typeof</code> 则是直接重写了一遍，自定义了 <code>_typeof 这个函数来辅助</code>。这些函数叫做 helpers。每个项目文件都写无意是不合理的。</p>
<p>作用是将 <code>helper</code>(辅助函数) 和 <code>polyfill</code>（不修改全局变量原型的静态方法等） 都改为从一个统一的地方引入，并且引入的对象和全局变量是完全隔离的。</p>
<p>具体配置不详细说明了，到后面讲<code>babelrc</code>文件的的时候说。</p>
<ul>
<li>@babel/runtime-corejs：</li>
</ul>
<p>上面我们看到了<code>@babel/prest-env</code>带来的问题，这两个问题@babel/plugin-transform-runtime可以解决，那<code>@babel/runtime-corejs</code>又是个什么东西呢？</p>
<p>其中 <code>@babel/plugin-transform-runtime</code> 的作用是转译代码，转译后的代码中可能会引入 <code>@babel/runtime-corejs</code> 里面的模块，也就是说具体转译代码的函数是单独在另一个包里，就是<code>@babel/runtime-corejs</code>里面</p>
<h3 data-id="heading-6">types家族：@types/react @types/react-dom @types/webpack-env</h3>
<ul>
<li>
<p><code>@types/react、@types/react-dom</code>这两个是react的typescript类型定义</p>
</li>
<li>
<p><code>@types/webpack-env</code> 是webpack的typescript类型定义</p>
</li>
</ul>
<h3 data-id="heading-7">eslint家族：eslint、eslint-config-airbnb、eslint-config-prettier...</h3>
<ul>
<li>
<p>eslint：是一个插件化并且可配置的 <code>JavaScript</code> 语法规则和代码风格的检查工具。这个就不多说了，大家都知道吧，不用<code>eslint</code>的前端项目应该很少。</p>
</li>
<li>
<p>eslint-config-airbnb：<code>Airbnb</code>的eslint规则的标准,它依赖<code>eslint, eslint-plugin-import, eslint-plugin-react, and eslint-plugin-jsx-a11y</code>等插件，并且对各个插件的版本有所要求。</p>
</li>
<li>
<p>eslint-config-prettier：<code>prettier</code>是一个代码格式化工具，比如说规范项目都使用单引号，还是双引号。而且，<code>Prettier</code> 还给予了一部分配置项，可以通过 <code>.prettierrc</code> 文件修改。</p>
</li>
<li>
<p>所以相当于 <code>Prettier</code> 接管代码格式的问题，而使用 <code>Prettier + ESLint</code> 就完完全全解决了代码格式和代码语法规则校验的问题。</p>
</li>
</ul>
<p>但实际上使用起来配置有些小麻烦，但也不是什么大问题。因为 <code>Prettier</code> 和 <code>ESLint</code> 一起使用的时候会有冲突，我们需要使用 <code>eslint-config-prettier</code> 来关掉 (disable) 所有和 <code>Prettier</code> 冲突的 ESLint 的配置,</p>
<p><code>eslint-plugin-prettier</code> 将 prettier 的 rules 以插件的形式加入到 ESLint 里面方法就是在 .eslintrc 里面将 prettier 设为最后一个 extends</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">// .eslintrc    </span>
&#123;      
    <span class="hljs-string">"plugins"</span>: [<span class="hljs-string">"prettier"</span>],      
    <span class="hljs-string">"rules"</span>: &#123;        
        <span class="hljs-string">"prettier/prettier"</span>: <span class="hljs-string">"error"</span>      
    &#125;    
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>将上面两个步骤和在一起就是下面的配置，也是官方的推荐配置</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">// .eslintrc</span>
&#123;
  <span class="hljs-string">"extends"</span>: [<span class="hljs-string">"plugin:prettier/recommended"</span>]
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>eslint-plugin-import：用于校验<code>es6</code>的<code>import</code>规则，如果增加<code>import plugin</code>，在我们使用<code>webpack</code>的时候，如果你配置了<code>resolve.config.js</code>的<code>alias</code>，那么我们希望import plugin的校验规则会从这里取模块的路径，此时需要配置,注意，此时同时要下载<code>eslint-import-resolver-webpack</code>插件才能像下面一样设置</li>
</ul>
<pre><code class="hljs language-javascript copyable" lang="javascript">“rules”: &#123;&#125;,
       <span class="hljs-comment">/** 这里传入webpack并不是import插件能识别webpack，
       * 而且通过npm安装了「eslint-import-resolver-webpack」，
       * 「import」插件通过「eslint-import-resolver-」+「webpack」找到该插件并使用，
       * 就能解析webpack配置项。使用里面的参数。
       **/</span>
<span class="hljs-string">"settings"</span>: &#123;
        <span class="hljs-comment">// 使用webpack中配置的resolve路径</span>
        <span class="hljs-string">"import/resolver"</span>: <span class="hljs-string">"webpack"</span> 
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>eslint-import-resolver-typescript：它也是<code>「eslint-import-resolver-」</code>家族的一员，它的作用是</p>
<ul>
<li><code>import/require</code> 扩展名为 .ts/.tsx 的文件</li>
<li>使用<code> tsconfig.json</code> 中定义的paths路径</li>
<li>优先解析<code>@types/* </code>定义而不是普通的 .js</li>
</ul>
<p>eslint-plugin-jsx-a11y： 该插件为你的 <code>JSX</code> 中的无障碍问题提供了 <code>AST</code> 的语法检测反馈。</p>
<p>eslint-plugin-react: 一些 <code>react</code> 的 <code>eslint</code> 的 <code>rules</code> 规范</p>
<p>eslint-plugin-react-hooks:检测react hooks的一些语法规范，并提供相应的<code>rules</code></p>
<h3 data-id="heading-8">postcss家族：postcss、postcss-flexbugs-fixes、postcss-loaderpostcss-preset-env，autoprefixer</h3>
<p>postcss: 是一个使用JavaScript插件来转换<code>CSS</code>的工具。</p>
<p><code>PostCSS</code>本身很小，其只包含<code>CSS</code>解析器，操作<code>CSS</code>节点树的<code>API</code>，<code>source map</code>，以及一个节点树字符串化工具,其它功能都是通过插件来实现的，比如说插件有</p>
<p>1、添加浏览器内核前缀的</p>
<p>2、有检测<code>css</code>代码的工具等等</p>
<p>postcss-flexbugs-fixes： 修复在一些浏览器上flex布局的bug，比如说</p>
<ul>
<li>在ie10和标准的区别</li>
</ul>
<p>----|标准|
flex: 1flex: 1 1 0%flex: 1 0 0px
flex: autoflex: 1 1 autoflex: 1 0 auto</p>

























<table><thead><tr><th>缩写声明</th><th>标准转义</th><th>IE10转义</th></tr></thead><tbody><tr><td>(no flex declaration)</td><td>flex: 0 1 auto</td><td>flex: 0 0 auto</td></tr><tr><td>flex: 1</td><td>flex: 1 1 0%</td><td>flex: 1 0 0px</td></tr><tr><td>flex: auto</td><td>flex: 1 1 auto</td><td>flex: 1 0 auto</td></tr></tbody></table>
<p>postcss-loader：<code>loader</code>的功能在上面已经说明，这个<code>loader</code>是<code>postcss</code>用来改变<code>css</code>代码的<code>loader</code></p>
<p>postcss-preset-env：这个插件主要是集成了（有了它不用下载autoprefixer插件）</p>
<p>autoprefixer：用于解析 <code>CSS</code> 并使用 <code>Can I Use</code> 中的值向 <code>CSS</code> 规则添加供应商前缀</p>
<p>style-resoures-loader：这个插件比较重要，即使这个项目没有用，我也建议大家项目用上。它的作用就是避免重复在每个样式文件中<code>@import</code>导入，在各个<code>css</code> 文件中能够直接使用变量和公共的样式。</p>
<h3 data-id="heading-9">webpack家族：webpack、webpack-bundle-analyzer、webpack-cli、webpack-dev-server、webpack-merge、webpackbar</h3>
<p>webpack：这个不用描述了吧。。。</p>
<p>webpack-cli：</p>
<ul>
<li>是使用 <code>webpack</code>的命令行工具，在 <code>4.x</code> 版本之后不再作为 <code>webpack</code> 的依赖了，我们使用时需要单独安装这个工具。</li>
</ul>
<p>webpack-bundle-analyzer: <code>webpack</code>打包体积分析工具，会让我们知道打包后的文件分别是由哪些文件组成，并且体积是多少，是一款优化分析打包文件的工具</p>
<p>webpack-dev-server：是一个小型的<code>Node.js Express</code>服务器,它使用<code>webpack-dev-middleware</code>来服务于webpack的包,除此自外，它还有一个通过<code>Sock.js</code>来连接到服务器的微型运行时</p>
<p>webpack-merge：</p>
<ul>
<li>一般情况，我们会把webpack文件分为，<code>webpack.common.js</code>（后面两个js文件共同的内容抽离出来）,<code>webpack.pro.js</code>（生产环境独有的内容）,<code>webpack.dev.js</code>（开发环境独有的内容）。</li>
<li>此时，我们需要一个方法来合并<code>webpack.common.js</code>和<code>webpack.pro.js</code>变为生产环境的内容，同理<code>common</code>和<code>dev</code>也是如此。我们就需要<code>webpack-merge</code>方法了。它的作用如下</li>
</ul>
<pre><code class="copyable">const merge = require("webpack-merge");
merge(
    &#123;a : [1],b:5,c:20&#125;,
    &#123;a : [2],b:10, d: 421&#125;
)
//合并后的结果
&#123;a : [1,2] ,b :10 , c : 20, d : 421&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>从上面的案例，我们可以看出来, 数组内容会合并，基础类型的值会被覆盖，这比较符合我们<code>webpack.common.js</code>有一些plugins：[],<code>webpack.pro.js</code> 也有一些plugins是合并的需要，而不是覆盖。</p>
<h3 data-id="heading-10">stylelint 家族： stylelint、、stylelint-config-rational-order...</h3>
<p>stylelint：<code>stylelint</code> 用于样式规范检查与修复，支持 <code>.css .scss .less .sss</code></p>
<p>stylelint-config-prettier：关闭所有不必要的或可能与 <code>Prettier</code> 冲突的规则。</p>
<p>stylelint-config-rational-order：它对你的<code>css</code>样式排序会有要求，具体为</p>
<pre><code class="hljs language-css copyable" lang="css">Positioning -- 定位
Box Model -- 盒模型
Typography -- 版式
Visual -- 可见性（显示和隐藏）
<span class="hljs-attribute">Animation</span> -- 动画
Misc -- 其它杂项

<span class="hljs-selector-class">.declaration-order</span> &#123;
  <span class="hljs-comment">/* 1.Positioning 位置属性 */</span> 
  <span class="hljs-attribute">position</span>: absolute;
  <span class="hljs-attribute">top</span>: <span class="hljs-number">0</span>;
  <span class="hljs-attribute">right</span>: <span class="hljs-number">0</span>;
  <span class="hljs-attribute">bottom</span>: <span class="hljs-number">0</span>;
  <span class="hljs-attribute">left</span>: <span class="hljs-number">0</span>;
  <span class="hljs-attribute">z-index</span>: <span class="hljs-number">10</span>;

  <span class="hljs-comment">/* 2.Box Model 盒子属性 */</span>
  <span class="hljs-attribute">display</span>: block;
  <span class="hljs-attribute">float</span>: right;
  <span class="hljs-attribute">width</span>: <span class="hljs-number">100px</span>;
  <span class="hljs-attribute">height</span>: <span class="hljs-number">100px</span>;
  <span class="hljs-attribute">margin</span>: <span class="hljs-number">10px</span>;
  <span class="hljs-attribute">padding</span>: <span class="hljs-number">10px</span>;

  <span class="hljs-comment">/* 3.Typography 文字属性 */</span>
  <span class="hljs-attribute">color</span>: <span class="hljs-number">#888</span>;
  <span class="hljs-attribute">font</span>: normal <span class="hljs-number">16px</span> Helvetica, sans-serif;
  <span class="hljs-attribute">line-height</span>: <span class="hljs-number">1.3</span>;
  <span class="hljs-attribute">text-align</span>: center;

  <span class="hljs-comment">/* 4.Visual 视觉属性 */</span>
  <span class="hljs-attribute">background-color</span>: <span class="hljs-number">#eee</span>;
  <span class="hljs-attribute">border</span>: <span class="hljs-number">1px</span> solid <span class="hljs-number">#888</span>;
  <span class="hljs-attribute">border-radius</span>: <span class="hljs-number">4px</span>;
  <span class="hljs-attribute">opacity</span>: <span class="hljs-number">1</span>;

  <span class="hljs-comment">/* 5.Animation Misc 其他 */</span>
  <span class="hljs-attribute">transition</span>: all <span class="hljs-number">1s</span>;
  user-select: none;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>你不按上面的顺序写<code>css</code>的话，会警告或者报错。</p>
<p>stylelint-order：这个实现的功能也是排序，不过它跟上面的插件的区别是，它按照字母（英文是<code>alpha sort</code>）排序，所以两个插件要配合使用。</p>
<p>stylelint-config-standard：该风格是 <code>Stylelint</code> 的维护者汲取了<code> GitHub、Google、Airbnb</code> 多家之长生成的一套css风格规则。</p>
<p>stylelint-declaration-block-no-ignored-properties：这个插件的作用是警告那些不起作用的属性。比如说你设置了<code>display：inline，width： 200px</code>，其实这里的<code>width</code>是不起作用的，此时这个插件就会发出警告</p>
<h3 data-id="heading-11">chalk</h3>
<p>打印有颜色文字的插件：用法比如说</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">// 控制台打印红色的hello</span>
<span class="hljs-built_in">require</span>(<span class="hljs-string">'chalk'</span>).red(<span class="hljs-string">'hello'</span>)
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-12">clean-webpack-plugin</h3>
<p>webpack使用的插件，一般用在production环境，用来清除文件夹用的，就是类似<code>rm -rf ./dist</code></p>
<h3 data-id="heading-13">conventional-changelog-cli、@commitlint/cli、@commitlint/config-conventional</h3>
<p><code>commitlint</code> 可以帮助我们进行 <code>git commit</code> 时的 message 格式是否符合规范，<code>conventional-changelog</code> 可以帮助我们快速生成 <code>changelog</code></p>
<p><code>@commitlint/config-conventional</code> 类似 eslint 配置文件中的 extends ，它是官方推荐的 <code>angular</code> 风格的 commitlint 配置</p>
<h3 data-id="heading-14">copy-webpack-plugin</h3>
<p>在webpack中拷贝文件和文件夹</p>
<h3 data-id="heading-15">cross-env</h3>
<p>它是运行跨平台设置和使用环境变量(Node中的环境变量)的脚本。因为在windows和linux|mac里设置环境变量的方法不一致，比如说</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">// 在windows系统上，我们使用：</span>
<span class="hljs-string">"SET NODE_ENV=production && webpack --config build/webpack.config.js"</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">// 在Lunix系统和安装并使用了bash的windows的系统上，我们会使用:</span>
<span class="hljs-string">"EXPORT  NODE_ENV=production && webpack --config build/webpack.config.js"</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-16">mini-css-extract-plugin、css-minimizer-webpack-plugin</h3>
<p><code>webpack 4.0</code>以后，官方推荐使用<code>mini-css-extract-plugin</code>插件来打包css文件（从css文件中提取css代码到单独的文件中，对<code>css</code>代码进行代码压缩等）</p>
<p>相对的，如果你不想提取<code>css</code>，可以使用<code>style-loader</code>，将<code>css</code>内嵌到<code>html</code>文件里。</p>
<p>使用方法和效果如下：（后面会在webpack配置文件分析里看到），</p>
<p>先举一个基础配置的例子。 <code>webpack.config.js</code>：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">const</span> MiniCssExtractPlugin = <span class="hljs-built_in">require</span>(<span class="hljs-string">'mini-css-extract-plugin'</span>);
<span class="hljs-built_in">module</span>.exports = &#123;
  <span class="hljs-attr">plugins</span>: [
    <span class="hljs-keyword">new</span> MiniCssExtractPlugin(&#123;
      <span class="hljs-attr">filename</span>: <span class="hljs-string">'[name].css'</span>
    &#125;),
  ],
  <span class="hljs-attr">module</span>: &#123;
    <span class="hljs-attr">rules</span>: [
      &#123;
        <span class="hljs-attr">test</span>: <span class="hljs-regexp">/\.css$/</span>,
        use: [
          MiniCssExtractPlugin.loader, <span class="hljs-string">'css-loader'</span>,<span class="hljs-string">'postcss-loader'</span> <span class="hljs-comment">// postcss-loader 可选</span>
        ],
      &#125;,&#123;
        <span class="hljs-attr">test</span>: <span class="hljs-regexp">/\.less$/</span>,
        use: [
          MiniCssExtractPlugin.loader, <span class="hljs-string">'css-loader'</span>,<span class="hljs-string">'postcss-loader'</span>,<span class="hljs-string">'less-loader'</span> <span class="hljs-comment">// postcss-loader 可选</span>
        ],
      &#125;
    ],
  &#125;,
&#125;;
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>实战案例</li>
</ul>
<p>基于以上配置</p>
<ul>
<li>如果入口 <code>app.js</code> 中引用了 <code>Root,js</code></li>
<li><code>Root</code>引入了 <code>Topics.js</code></li>
<li>而 <code>Root.js</code> 中引用样式 <code>main.css</code></li>
<li><code>Topics.js</code> 中引用了 <code>topics.css</code>。</li>
</ul>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">// 入口文件 app.js</span>
<span class="hljs-keyword">import</span> Root <span class="hljs-keyword">from</span> <span class="hljs-string">'./components/Root'</span>

<span class="hljs-comment">// Root.js</span>
<span class="hljs-keyword">import</span> <span class="hljs-string">'../styles/main.less'</span>
<span class="hljs-keyword">import</span> Topics <span class="hljs-keyword">from</span> <span class="hljs-string">'./Topics'</span>

<span class="hljs-comment">// Topics.js</span>
<span class="hljs-keyword">import</span> <span class="hljs-string">"../styles/topics.less"</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这种情况下，<code>Topics</code> 会和 <code>Root</code> 同属一个 <code>chunk</code>，所以会一起都打包到 <code>app.js</code> 中， 结果就是 main.less 和 topics.less 会被提取到一个文件中：<code>app.css</code>。而不是生成两个 <code>css</code> 文件。</p>
<pre><code class="hljs language-javascript copyable" lang="javascript">            Asset       Size  Chunks                    Chunk Names
          app.css  <span class="hljs-number">332</span> bytes       <span class="hljs-number">1</span>  [emitted]         app
           app.js    <span class="hljs-number">283</span> KiB       <span class="hljs-number">1</span>  [emitted]  [big]  app
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>代码情景二</li>
</ul>
<p>但是，如果 <code>Root.js</code> 中并没有直接引入 <code>Topics</code> 组件，而是配置了代码分割 ，比如模块的动态引入(也就是说你的topics模块，是impot()动态引入的)，那么结果就不一样了：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript">            Asset       Size  Chunks                    Chunk Names
          app.css  <span class="hljs-number">260</span> bytes       <span class="hljs-number">1</span>  [emitted]         app
           app.js    <span class="hljs-number">281</span> KiB       <span class="hljs-number">1</span>  [emitted]  [big]  app
 topics.bundle.js   <span class="hljs-number">2.55</span> KiB       <span class="hljs-number">4</span>  [emitted]         topics
       topics.css   <span class="hljs-number">72</span> bytes       <span class="hljs-number">4</span>  [emitted]         topics
<span class="copy-code-btn">复制代码</span></code></pre>
<p>因为这个时候有两个 chunk，对应了两个 JS 文件，所以会提取这两个 JS 文件中的 CSS 生成对应的文件。这才是<code>“为每个包含 CSS 的 JS 文件创建一个单独的 CSS 文件”</code>的真正含义。</p>
<ul>
<li>情景三</li>
</ul>
<p>但是，如果分割了 <code>chunk</code>，还是只希望只生成一个 <code>CSS</code> 文件怎么办呢？也是可以做到的。但需要借助 Webpack 的配置 <code>optimization.splitChunks.cacheGroups</code>。</p>
<p>先来看看配置怎么写的：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript">optimization: &#123;
  <span class="hljs-attr">splitChunks</span>: &#123;
    <span class="hljs-attr">cacheGroups</span>: &#123;
      <span class="hljs-comment">// Extracting all CSS/less in a single file</span>
      <span class="hljs-attr">styles</span>: &#123;
      <span class="hljs-attr">name</span>: <span class="hljs-string">'styles'</span>,
        <span class="hljs-attr">test</span>: <span class="hljs-regexp">/\.(c|le)ss$/</span>,
        chunks: <span class="hljs-string">'all'</span>,
        <span class="hljs-attr">enforce</span>: <span class="hljs-literal">true</span>,
      &#125;,
    &#125;
  &#125;
&#125;,
<span class="copy-code-btn">复制代码</span></code></pre>
<p>打包结果：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript">            Asset       Size  Chunks                    Chunk Names
           app.js    <span class="hljs-number">281</span> KiB       <span class="hljs-number">2</span>  [emitted]  [big]  app
 styles.bundle.js  <span class="hljs-number">402</span> bytes       <span class="hljs-number">0</span>  [emitted]         styles
       styles.css  <span class="hljs-number">332</span> bytes       <span class="hljs-number">0</span>  [emitted]         styles
 topics.bundle.js   <span class="hljs-number">2.38</span> KiB       <span class="hljs-number">5</span>  [emitted]         topics
<span class="copy-code-btn">复制代码</span></code></pre>
<p>继续加强上面的配置,压缩上面分理处的代码，
<code>css-minimizer-webpack-plugin</code>是用来压缩分离出来的css的。使用方法如下：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">const</span> MiniCssExtractPlugin = <span class="hljs-built_in">require</span>(<span class="hljs-string">'mini-css-extract-plugin'</span>);
<span class="hljs-keyword">const</span> CssMinimizerPlugin = <span class="hljs-built_in">require</span>(<span class="hljs-string">'css-minimizer-webpack-plugin'</span>);

<span class="hljs-built_in">module</span>.exports = &#123;
  <span class="hljs-attr">module</span>: &#123;
    <span class="hljs-attr">rules</span>: [
      &#123;
        <span class="hljs-attr">test</span>: <span class="hljs-regexp">/.s?css$/</span>,
        use: [MiniCssExtractPlugin.loader, <span class="hljs-string">'css-loader'</span>, <span class="hljs-string">'sass-loader'</span>],
      &#125;,
    ],
  &#125;,
  <span class="hljs-attr">optimization</span>: &#123;
    <span class="hljs-attr">minimizer</span>: [
      <span class="hljs-comment">// For webpack@5 you can use the `...` syntax to extend existing minimizers (i.e. `terser-webpack-plugin`), uncomment the next line</span>
      <span class="hljs-comment">// `...`,</span>
      <span class="hljs-keyword">new</span> CssMinimizerPlugin(),
    ],
  &#125;,
&#125;;
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-17">detect-port-alt</h4>
<p>这个包用来检测对应端口是否被占用，比如项目里发现启动3000端口被占用的话就+1，直到选择一个不被占用的端口（端口上限是65535）。</p>
<h4 data-id="heading-18">error-overlay-webpack-plugin</h4>
<p>它提供了和 create-react-app 一样的错误遮罩：</p>
<p>用法如下：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">const</span> ErrorOverlayPlugin = <span class="hljs-built_in">require</span>(<span class="hljs-string">'error-overlay-webpack-plugin'</span>)

<span class="hljs-built_in">module</span>.exports = &#123;
  <span class="hljs-attr">plugins</span>: [<span class="hljs-keyword">new</span> ErrorOverlayPlugin()],
  <span class="hljs-attr">devtool</span>: <span class="hljs-string">'cheap-module-source-map'</span>, <span class="hljs-comment">// 'eval' is not supported by error-overlay-webpack-plugin</span>
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/a90327edce1c430eac2da36d80452b7e~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h4 data-id="heading-19">@typescript-eslint/eslint-plugin、@typescript-eslint/parser</h4>
<p>@typescript-eslint/parser：ESLint的解析器，用于解析typescript，从而检查和规范Typescript代码</p>
<p>@typescript-eslint/eslint-plugin：这是一个ESLint插件，包含了各类定义好的检测Typescript代码的规范</p>
<p>配置如下所示：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-built_in">module</span>.exports = &#123;
    <span class="hljs-attr">parser</span>:  <span class="hljs-string">'@typescript-eslint/parser'</span>, <span class="hljs-comment">// 定义ESLint的解析器</span>
    <span class="hljs-attr">extends</span>: [<span class="hljs-string">'plugin:@typescript-eslint/recommended'</span>],<span class="hljs-comment">// 定义文件继承的子规范</span>
    <span class="hljs-attr">plugins</span>: [<span class="hljs-string">'@typescript-eslint'</span>],<span class="hljs-comment">// 定义了该eslint文件所依赖的插件</span>
    <span class="hljs-attr">env</span>:&#123;                          <span class="hljs-comment">// 指定代码的运行环境</span>
        <span class="hljs-attr">browser</span>: <span class="hljs-literal">true</span>,
        <span class="hljs-attr">node</span>: <span class="hljs-literal">true</span>,
    &#125;                               
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-20">fork-ts-checker-webpack-plugin</h4>
<p>它在一个单独的进程上运行类型检查器，该插件在编译之间重用抽象语法树，并与TSLint共享这些树。可以通过多进程模式进行扩展，以利用最大的CPU能力。</p>
<h4 data-id="heading-21">html-webpack-plugin</h4>
<p>这个插件非常常用，几乎是必备的。</p>
<p>它的作用是：当使用 <code>webpack</code>打包时，创建一个 <code>html</code> 文件，并把 <code>webpack</code> 打包后的静态文件自动插入到这个 html 文件当中。简单实用如下（讲webpack文件时会更详细介绍api）：</p>
<pre><code class="hljs language-JAVASCRIPT copyable" lang="JAVASCRIPT">&#123;
  <span class="hljs-attr">entry</span>: <span class="hljs-string">'index.js'</span>,
  <span class="hljs-attr">output</span>: &#123;
    <span class="hljs-attr">path</span>: __dirname + <span class="hljs-string">'/dist'</span>, 
    <span class="hljs-attr">filename</span>: <span class="hljs-string">'bundle.js'</span>
  &#125;,
  <span class="hljs-attr">plugins</span>: [
    <span class="hljs-keyword">new</span> HtmlWebpackPlugin(&#123;
      <span class="hljs-attr">title</span>: <span class="hljs-string">'My App'</span>, 
      <span class="hljs-attr">filename</span>: <span class="hljs-string">'assets/admin.html'</span>  <span class="hljs-comment">// 在  output.path 目录下生成 assets/admin.html 文件</span>
    &#125;)
  ]
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-22">husky、lint-staged</h4>
<p>husky是一个npm包，安装后，可以很方便的在package.json配置git hook 脚本 。</p>
<p>比如，在 package.json 内配置如</p>
<pre><code class="hljs language-JAVASCRIPT copyable" lang="JAVASCRIPT"> <span class="hljs-string">"scripts"</span>: &#123;
    <span class="hljs-string">"lint"</span>: <span class="hljs-string">"eslint src"</span>
  &#125;,
  <span class="hljs-string">"husky"</span>: &#123;
    <span class="hljs-string">"hooks"</span>: &#123;
      <span class="hljs-string">"pre-commit"</span>: <span class="hljs-string">"npm run lint"</span>
    &#125;
  &#125;,
<span class="copy-code-btn">复制代码</span></code></pre>
<p>那么，在后续的每一次<code>git commit</code> 之前，都会执行一次对应的 hook 脚本<code>npm run lint</code> 。其他hook同理.</p>
<ul>
<li>lint-staged</li>
</ul>
<p>如果我们 想对git 缓存区最新改动过的文件进行以上的格式化和 <code>lint</code> 规则校验，这就需要 <code>lint-staged</code>了 。</p>
<p>如下：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript">&#123;
    <span class="hljs-string">"husky"</span>: &#123;
    <span class="hljs-string">"hooks"</span>: &#123;
      <span class="hljs-string">"pre-commit"</span>: <span class="hljs-string">"lint-staged"</span>,
    &#125;
  &#125;,
  <span class="hljs-string">"lint-staged"</span>: &#123;
    <span class="hljs-comment">// 首先，我们会对暂存区后缀为 `.ts .tsx .js` 的文件进行 eslint 校验，</span>
    <span class="hljs-comment">// --config 的作用是指定配置文件。</span>
    <span class="hljs-string">"*.&#123;ts,tsx,js&#125;"</span>: [
      <span class="hljs-string">"eslint --config .eslintrc.js"</span>
    ],
    <span class="hljs-comment">// 同理 是stylelint的校验</span>
    <span class="hljs-string">"*.&#123;css,less,scss&#125;"</span>: [
      <span class="hljs-string">"stylelint --config .stylelintrc.js"</span>
    ],
    <span class="hljs-comment">// prettier格式化</span>
    <span class="hljs-string">"*.&#123;ts,tsx,js,json,html,yml,css,less,scss,md&#125;"</span>: [
      <span class="hljs-string">"prettier --write"</span>
    ]
  &#125;,
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这里没有添加 <code>--fix</code> 来自动修复不符合规则的代码，因为自动修复的内容对我们不透明，这样不太好。</p>
<h3 data-id="heading-23">terser-webpack-plugin</h3>
<p>是一个使用 <code>terser</code> 压缩<code>js</code>的<code>webpack</code> 插件。</p>
<p>如果你使用的是 <code>webpack v5</code> 或以上版本，你不需要安装这个插件。<code>webpack v5</code> 自带最新的 <code>terser-webpack-plugin</code>。如果使用 <code>webpack v4</code>，则必须安装 <code>terser-webpack-plugin v4</code> 的版本。</p>
<p>简易用法如下，详细介绍留到后面webpack配置文件详解</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">const</span> TerserPlugin = <span class="hljs-built_in">require</span>(<span class="hljs-string">'terser-webpack-plugin'</span>);

<span class="hljs-built_in">module</span>.exports = &#123;
  <span class="hljs-attr">optimization</span>: &#123;
    <span class="hljs-attr">minimizer</span>: [<span class="hljs-keyword">new</span> TerserPlugin(
      parallel: <span class="hljs-literal">true</span>   <span class="hljs-comment">// 多线程</span>
    )],
  &#125;,
&#125;;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-24">package.json里的其它比较重要的字段</h3>
<pre><code class="hljs language-javascript copyable" lang="javascript">&#123;
  <span class="hljs-string">"main"</span>: <span class="hljs-string">"index.js"</span>,
  <span class="hljs-string">"scripts"</span>: &#123;
    <span class="hljs-string">"start"</span>: <span class="hljs-string">"cross-env NODE_ENV=development node scripts/server"</span>,
    <span class="hljs-string">"build"</span>: <span class="hljs-string">"cross-env NODE_ENV=production webpack --config ./scripts/config/webpack.prod.js"</span>,
    <span class="hljs-string">"changelog"</span>: <span class="hljs-string">"conventional-changelog -p angular -i CHANGELOG.md -s"</span>,
    <span class="hljs-string">"lint"</span>: <span class="hljs-string">"npm run lint-eslint && npm run lint-stylelint"</span>,
    <span class="hljs-string">"lint-eslint"</span>: <span class="hljs-string">"eslint -c .eslintrc.js --ext .ts,.tsx,.js src"</span>,
    <span class="hljs-string">"lint-stylelint"</span>: <span class="hljs-string">"stylelint --config .stylelintrc.js src/**/*.&#123;less,css,scss&#125;"</span>
  &#125;,
  <span class="hljs-string">"browserslist"</span>: [<span class="hljs-string">">0.2%"</span>, <span class="hljs-string">"not dead"</span>, <span class="hljs-string">"ie >= 9"</span>, <span class="hljs-string">"not op_mini all"</span>],
  <span class="hljs-string">"husky"</span>: &#123;
    <span class="hljs-string">"hooks"</span>: &#123;
      <span class="hljs-string">"pre-commit"</span>: <span class="hljs-string">"lint-staged"</span>,
      <span class="hljs-string">"commit-msg"</span>: <span class="hljs-string">"commitlint --config .commitlintrc.js -E HUSKY_GIT_PARAMS"</span>
    &#125;
  &#125;,
  <span class="hljs-string">"lint-staged"</span>: &#123;
    <span class="hljs-string">"*.&#123;ts,tsx,js&#125;"</span>: [<span class="hljs-string">"eslint --config .eslintrc.js"</span>],
    <span class="hljs-string">"*.&#123;css,less,scss&#125;"</span>: [<span class="hljs-string">"stylelint --config .stylelintrc.js"</span>],
    <span class="hljs-string">"*.&#123;ts,tsx,js,json,html,yml,css,less,scss,md&#125;"</span>: [<span class="hljs-string">"prettier --write"</span>]
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这里的<code>main</code>需要跟一些其它字段来一起比较。比如<code>browser，module，main</code>三个字段都可以出现在<code>package.json</code>中，它们有什么区别呢？</p>
<p>我们直接说结论，具体详细分析，详情参考这篇文章<a href="https://link.juejin.cn/?target=https%3A%2F%2Fzhuanlan.zhihu.com%2Fp%2F129310389" target="_blank" rel="nofollow noopener noreferrer" title="https://zhuanlan.zhihu.com/p/129310389" ref="nofollow noopener noreferrer">开发插件package.json在webpack构建中的表现</a></p>
<h3 data-id="heading-25">结论</h3>
<ul>
<li>webpack 选择 web 浏览器环境</li>
<li>插件的 package.json 是否配置了 browser 字段
<ul>
<li>存在：选择 browser 作为入口</li>
<li>不存在：</li>
<li>插件的 package.json 是否配置了 module 字段
<ul>
<li>存在：选择 module 作为入口</li>
<li>不存在：以 main 作为入口</li>
</ul>
</li>
</ul>
</li>
<li>webapack 选择 node环境
<ul>
<li>插件的 package.json 是否配置了 module 字段
<ul>
<li>存在：选择 module 作为入口</li>
<li>不存在：以 main 作为入口</li>
</ul>
</li>
</ul>
</li>
</ul>
<p>根据上面的行为总结，我们在开发插件的时候，需要考虑插件是提供给<code>web</code>环境还是<code>node</code>环境，如果都涉及到且存在区别，就要明确指出 <code>browser、module</code> 字段。如果没有任何区别的话，使用 <code>main</code> 入口足以</p>
<h3 data-id="heading-26">.vscode中settings文件</h3>
<p>这个文件对于使用vscode的用户比较重要，有一些设置非常棒，比如点击ctrl+s自动格式化你的文件，设置如下：</p>
<pre><code class="hljs language-JAVASCRIPT copyable" lang="JAVASCRIPT">   <span class="hljs-string">"editor.formatOnSave"</span>: <span class="hljs-literal">true</span>, <span class="hljs-comment">// 自动格式化代码，我们使用的是prettier</span>
   <span class="hljs-string">"editor.codeActionsOnSave"</span>: &#123;
    <span class="hljs-string">"source.fixAll.eslint"</span>: <span class="hljs-literal">true</span>, <span class="hljs-comment">// 保存自动修复 eslint报错（有些报错必须手动修复）</span>
    <span class="hljs-string">"source.fixAll.stylelint"</span>: <span class="hljs-literal">true</span> <span class="hljs-comment">// 保存自动修复 stylelint报错，也就是css报错</span>
  &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>下图是具体的settings文件，逐一注释其中的作用</p>
<pre><code class="hljs language-javascript copyable" lang="javascript">&#123;
  <span class="hljs-string">"css.validate"</span>: <span class="hljs-literal">false</span>, <span class="hljs-comment">// 禁用vscode本身的css校验功能</span>
  <span class="hljs-string">"less.validate"</span>: <span class="hljs-literal">false</span>, <span class="hljs-comment">// 禁用vscode本身的less校验功能</span>
  <span class="hljs-string">"scss.validate"</span>: <span class="hljs-literal">false</span>, <span class="hljs-comment">// 禁用vscode本身的scss校验功能</span>

  <span class="hljs-string">"eslint.validate"</span>: [<span class="hljs-string">"javascript"</span>, <span class="hljs-string">"javascriptreact"</span>, <span class="hljs-string">"typescript"</span>, <span class="hljs-string">"typescriptreact"</span>], <span class="hljs-comment">// eslint 校验的文件格式</span>
  <span class="hljs-string">"search.exclude"</span>: &#123; <span class="hljs-comment">// 搜索文件时排除的文件夹</span>
    <span class="hljs-string">"**/node_modules"</span>: <span class="hljs-literal">true</span>,
    <span class="hljs-string">"dist"</span>: <span class="hljs-literal">true</span>,
    <span class="hljs-string">"build"</span>: <span class="hljs-literal">true</span>
  &#125;,
  <span class="hljs-string">"editor.formatOnSave"</span>: <span class="hljs-literal">true</span>,  <span class="hljs-comment">// 保存时，自动格式化</span>
  <span class="hljs-string">"editor.codeActionsOnSave"</span>: &#123; <span class="hljs-comment">// 保存时自动格式化eslint的规则和stylint的规则</span>
    <span class="hljs-string">"source.fixAll.eslint"</span>: <span class="hljs-literal">true</span>,
    <span class="hljs-string">"source.fixAll.stylelint"</span>: <span class="hljs-literal">true</span>
  &#125;,
  <span class="hljs-string">"[javascript]"</span>: &#123; <span class="hljs-comment">// 底下类似是指校验js，jsx，ts，tsx的校验器是prettier，而不是vscode默认的</span>
    <span class="hljs-string">"editor.defaultFormatter"</span>: <span class="hljs-string">"esbenp.prettier-vscode"</span>
  &#125;,
  <span class="hljs-string">"[javascriptreact]"</span>: &#123;
    <span class="hljs-string">"editor.defaultFormatter"</span>: <span class="hljs-string">"esbenp.prettier-vscode"</span>
  &#125;,
  <span class="hljs-string">"[typescript]"</span>: &#123;
    <span class="hljs-string">"editor.defaultFormatter"</span>: <span class="hljs-string">"esbenp.prettier-vscode"</span>
  &#125;,
  <span class="hljs-string">"[typescriptreact]"</span>: &#123;
    <span class="hljs-string">"editor.defaultFormatter"</span>: <span class="hljs-string">"esbenp.prettier-vscode"</span>
  &#125;,
  <span class="hljs-string">"[json]"</span>: &#123;
    <span class="hljs-string">"editor.defaultFormatter"</span>: <span class="hljs-string">"esbenp.prettier-vscode"</span>
  &#125;
&#125;

<span class="copy-code-btn">复制代码</span></code></pre>
<p>上面的保存时自动格式化eslint的规则和stylint的规则，需要注意的是，有些规则是必须手动修改的，不会自动保存格式化。</p>
<h3 data-id="heading-27">babelrc文件解析</h3>
<p>下面的presets和plugins的区别是，</p>
<ul>
<li>
<p>presets是一些预设，插件的对应名字是<code>babel-preset-xxx</code>。<code>Babel</code>插件一般尽可能拆成小的力度，开发者可以按需引进。但是一个一个引进有时候很麻烦，能不能把一些常用的插件打成一个包给我们用呢，这就是<code>presets</code>的作用和。</p>
</li>
<li>
<p><code>plugins</code>就是一个一个的插件集合，你要配特定的功能就可以加入到plugins中</p>
</li>
</ul>
<p>以下的所有插件之前都介绍过，可以试着回忆一下哦</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-built_in">module</span>.exports = &#123;
  <span class="hljs-attr">presets</span>: [
    [
      <span class="hljs-string">'@babel/preset-env'</span>,  <span class="hljs-comment">// 将基于你的实际浏览器及运行环境，自动的确定babel插件及polyfill</span>
      &#123;
        <span class="hljs-attr">useBuiltIns</span>: <span class="hljs-string">'usage'</span>, <span class="hljs-comment">// 按需使用</span>
        <span class="hljs-attr">modules</span>: <span class="hljs-literal">false</span>, <span class="hljs-comment">// 意思是不转义import语法，主要是为了tree-shaking</span>
      &#125;,
    ],
    <span class="hljs-string">'@babel/preset-react'</span>, <span class="hljs-comment">// 转化js、jsx文件的插件集合</span>
    <span class="hljs-string">'@babel/preset-typescript'</span>, <span class="hljs-comment">// 转化ts，tsx文件的插件集合</span>
  ],
  <span class="hljs-attr">plugins</span>: [
    [
      <span class="hljs-string">'@babel/plugin-transform-runtime'</span>,<span class="hljs-comment">// 优化polyfill的插件</span>
      &#123;
        <span class="hljs-attr">corejs</span>: &#123;
          <span class="hljs-attr">version</span>: <span class="hljs-number">3</span>,
          <span class="hljs-attr">proposals</span>: <span class="hljs-literal">true</span>,
        &#125;,
      &#125;,
    ],
  ],
&#125;;

<span class="copy-code-btn">复制代码</span></code></pre>
<p>这里详细解释一下<code>@babel/preset-env</code>这个插件的详细的常见使用参数，因为它很重要，是<code>babel</code>转义我们代码的关键插件:</p>
<ul>
<li>targets属性，最常见的是
<ul>
<li>targets.node ： 它可以指定编译当前node版本，或者 "node": true 或者 "node": "current", 它与 "node": process.versions.node 相同。</li>
<li>targets.browsers：可以利用 browserslist 查询选择的浏览器 (例如: last 2 versions, > 5%)</li>
</ul>
</li>
</ul>
<p>但是这里不建议把<code>browsers</code>信息写在<code>eslinttc</code>里面，因为可能其他的插件也需要浏览器信息，最好写在<code>package.json</code>中。
例如：</p>
<pre><code class="hljs language-JAVASCRIPT copyable" lang="JAVASCRIPT"><span class="hljs-string">"browserslist"</span>: [<span class="hljs-string">">0.2%"</span>, <span class="hljs-string">"not dead"</span>, <span class="hljs-string">"ie >= 9"</span>, <span class="hljs-string">"not op_mini all"</span>],
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>
<p>modules属性，如果是false，就是说导出方式是按es6 module，默认是commonjs规范</p>
</li>
<li>
<p>useBuiltIns：规定如何引入polyfill，比如说有些浏览器不支持promise，我们需要引入polyfill去兼容这些不支持promise的浏览器环境</p>
<ul>
<li>值为usage 会根据配置的浏览器兼容，以及你代码中用到的 API 来进行 polyfill，实现了按需添加，并且使用了<code>useBuiltIns: 'usage'之后，就不必手动在入口文件中</code>import '@babel/polyfill'`</li>
<li>值为 <code>entry</code> 配置项时, 根据<code>target</code>中浏览器版本的支持，将<code>polyfills</code>拆分引入，仅引入有浏览器不支持的<code>polyfill</code></li>
<li>corejs选项， 这个选项只会在与<code>useBuiltIns: usage</code>或者<code>useBuiltIns: entry</code>一起使用时才会生效, 确保<code>@babel/preset-env</code>为你的<code>core-js</code>版本注入了正确的引入</li>
</ul>
</li>
</ul>
<p>接着，我们解释一下在'@babel/plugin-transform-runtime'插件的配置：</p>
<ul>
<li>corejs： 比如<code>['@babel/plugin-transform-runtime', &#123; corejs: 2 &#125;]</code>，指定一个数字将引入<code>corejs</code>来重写需要<code>polyfillAPI</code> 的<code>helpers</code>，这需要使用<code>@babel/runtime-corejs2</code>作为依赖</li>
</ul>
<p>技术细节：<code>transform-runtime</code>转换器插件会做三件事：</p>
<ul>
<li>当你使用<code>generators/async</code>函数时，自动引入<code>@babel/runtime/regenerator</code>（可通过regenerator选项切换）</li>
<li>若是需要，将使用<code>core-js</code>作为<code>helpers</code>，而不是假定用户已经使用了<code>polyfill</code>（可通过corejs选项切换）</li>
<li>自动移除内联的 Babel helpers并取而代之使用<code>@babel/runtime/helpers</code>模块（可通过helpers选项切换）</li>
</ul>
<p>最后，我们要提一个问题，就是import 通过webpack转义之后，变成了什么样子，我们用案例来说。</p>
<p>如下是一个非常简单的webpack编译的模块。</p>
<pre><code class="copyable">import &#123; tmpPrint &#125; from './tmp.js'
export function print () &#123;
  tmpPrint() 
  console.log('我是 num.js 的 print 方法')
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>会被webpack编译为以路径为key，以函数为value的对象。</p>
<pre><code class="hljs language-javascript copyable" lang="javascript">&#123;
<span class="hljs-string">"./src/num.js"</span>:
      (<span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params"><span class="hljs-built_in">module</span>, __webpack_exports__, __webpack_require__</span>) </span>&#123;
<span class="hljs-meta">        "use strict"</span>;
        __webpack_require__.r(__webpack_exports__);
        __webpack_require__.d(__webpack_exports__, <span class="hljs-string">"print"</span>, <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params"></span>) </span>&#123; <span class="hljs-keyword">return</span> print; &#125;);
        <span class="hljs-comment">// 加载 ./src/tmp.js 模块</span>
        <span class="hljs-keyword">var</span> _tmp_js__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(<span class="hljs-string">"./src/tmp.js"</span>);
        <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">print</span>(<span class="hljs-params"></span>) </span>&#123;
          <span class="hljs-built_in">Object</span>(_tmp_js__WEBPACK_IMPORTED_MODULE_0__[<span class="hljs-string">"tmpPrint"</span>])()
          <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'我是 num.js 的 print 方法'</span>)
        &#125;
        <span class="hljs-comment">//# sourceURL=webpack:///./src/num.js?");</span>
      &#125;),
&#125;

<span class="copy-code-btn">复制代码</span></code></pre>
<p>我们接着看一下__webpack_require__.r，<strong>webpack_require</strong>.d，__webpack_require__分别是什么：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">__webpack_require__</span>(<span class="hljs-params">moduleId</span>) </span>&#123;
    <span class="hljs-comment">// 所有模块都会被缓存，如果在缓存里就直接从缓存里拿</span>
    <span class="hljs-keyword">if</span> (installedModules[moduleId]) &#123;
      <span class="hljs-keyword">return</span> installedModules[moduleId].exports;
    &#125;
    <span class="hljs-comment">// 这里是缓存的定义，i是id的意思，l是load的意思，exports是导出的内容</span>
    <span class="hljs-keyword">var</span> <span class="hljs-built_in">module</span> = installedModules[moduleId] = &#123;
      <span class="hljs-attr">i</span>: moduleId,
      <span class="hljs-attr">l</span>: <span class="hljs-literal">false</span>,
      <span class="hljs-attr">exports</span>: &#123;&#125;
    &#125;;

    <span class="hljs-comment">// 如果不是在缓存里，取出模块把module, module.exports, __webpack_require__作为参数放入到模块里</span>
    <span class="hljs-comment">// 如下的modules[moduleId]中保存的内容就相当于这块内容：</span>
    <span class="hljs-comment">// (function (module, __webpack_exports__, __webpack_require__) &#123;</span>
    <span class="hljs-comment">//    "use strict";</span>
    <span class="hljs-comment">//    __webpack_require__.r(__webpack_exports__);</span>
    <span class="hljs-comment">//    __webpack_require__.d(__webpack_exports__, "print", function () &#123; return // print; &#125;);</span>
        <span class="hljs-comment">// 加载 ./src/tmp.js 模块</span>
       <span class="hljs-comment">// var _tmp_js__WEBPACK_IMPORTED_MODULE_0__ = // __webpack_require__("./src/tmp.js");</span>
        <span class="hljs-comment">// function print() &#123;</span>
         <span class="hljs-comment">//  Object(_tmp_js__WEBPACK_IMPORTED_MODULE_0__["tmpPrint"])()</span>
         <span class="hljs-comment">// console.log('我是 num.js 的 print 方法')</span>
       <span class="hljs-comment">// &#125;</span>
        <span class="hljs-comment">//# sourceURL=webpack:///./src/num.js?");</span>
     <span class="hljs-comment">// &#125;),</span>
<span class="hljs-comment">// &#125;</span>

    
    modules[moduleId].call(<span class="hljs-built_in">module</span>.exports, <span class="hljs-built_in">module</span>, <span class="hljs-built_in">module</span>.exports, __webpack_require__);

    这下是不是懂了，很简单啊这个函数！就是加载和暴露模块用的
    <span class="hljs-comment">// Flag the module as loaded</span>
    <span class="hljs-built_in">module</span>.l = <span class="hljs-literal">true</span>;

    <span class="hljs-comment">// Return the exports of the module</span>
    <span class="hljs-keyword">return</span> <span class="hljs-built_in">module</span>.exports;
  &#125;
  
  
 __webpack_require__.d = <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params"><span class="hljs-built_in">exports</span>, name, getter</span>) </span>&#123;
     <span class="hljs-comment">// __webpack_require__.o这个函数的意思是检查name是否是exports的属性</span>
    <span class="hljs-keyword">if</span> (!__webpack_require__.o(<span class="hljs-built_in">exports</span>, name)) &#123;
      <span class="hljs-comment">// 如果exports原本没有name属性，就用defineProperty去定义name属性</span>
      <span class="hljs-built_in">Object</span>.defineProperty(<span class="hljs-built_in">exports</span>, name, &#123; <span class="hljs-attr">enumerable</span>: <span class="hljs-literal">true</span>, <span class="hljs-attr">get</span>: getter &#125;);
    &#125;
  &#125;;

   <span class="hljs-comment">// 这个函数就是用来标识是否是es模块的</span>
  __webpack_require__.r = <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params"><span class="hljs-built_in">exports</span></span>) </span>&#123;
    <span class="hljs-keyword">if</span> (<span class="hljs-keyword">typeof</span> <span class="hljs-built_in">Symbol</span> !== <span class="hljs-string">'undefined'</span> && <span class="hljs-built_in">Symbol</span>.toStringTag) &#123;
      <span class="hljs-built_in">Object</span>.defineProperty(<span class="hljs-built_in">exports</span>, <span class="hljs-built_in">Symbol</span>.toStringTag, &#123; <span class="hljs-attr">value</span>: <span class="hljs-string">'Module'</span> &#125;);
    &#125;
    <span class="hljs-built_in">Object</span>.defineProperty(<span class="hljs-built_in">exports</span>, <span class="hljs-string">'__esModule'</span>, &#123; <span class="hljs-attr">value</span>: <span class="hljs-literal">true</span> &#125;);
  &#125;;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>好了，我们接着回头接续分析那个src/sum.js的模块</p>
<pre><code class="hljs language-javascript copyable" lang="javascript">&#123;
<span class="hljs-string">"./src/num.js"</span>:
<span class="hljs-comment">// 大家还记得上面讲require有一句</span>
<span class="hljs-comment">// modules[moduleId].call(module.exports, module, module.exports, __webpack_require__);</span>
<span class="hljs-comment">// 我们可以看到 module就等于下面函数的 module，代表这个模块对象</span>
<span class="hljs-comment">// module.exports对应__webpack_exports__，也就是__webpack_exports__代表module导出的对象</span>
<span class="hljs-comment">// __webpack_require__对应function的 __webpack_require__参数，也就是导入模块函数</span>
      (<span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params"><span class="hljs-built_in">module</span>, __webpack_exports__, __webpack_require__</span>) </span>&#123;
<span class="hljs-meta">        "use strict"</span>;
        <span class="hljs-comment">// 这句话的意思把导出的exports对象标记为esmodule</span>
        __webpack_require__.r(__webpack_exports__);
        <span class="hljs-comment">// 这句话的意思是把模块下面的print函数，放入exports导出对象</span>
        __webpack_require__.d(__webpack_exports__, <span class="hljs-string">"print"</span>, <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params"></span>) </span>&#123; <span class="hljs-keyword">return</span> print; &#125;);
        <span class="hljs-comment">// 加载 ./src/tmp.js </span>
        <span class="hljs-keyword">var</span> _tmp_js__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(<span class="hljs-string">"./src/tmp.js"</span>);
        <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">print</span>(<span class="hljs-params"></span>) </span>&#123;
          <span class="hljs-built_in">Object</span>(_tmp_js__WEBPACK_IMPORTED_MODULE_0__[<span class="hljs-string">"tmpPrint"</span>])()
          <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'我是 num.js 的 print 方法'</span>)
        &#125;
        <span class="hljs-comment">//# sourceURL=webpack:///./src/num.js?");</span>
      &#125;),
&#125;

<span class="copy-code-btn">复制代码</span></code></pre>
<p>经过上面分析，发现最关键的一句就是__webpack_require__.r(<strong>webpack_exports</strong>)，把导出对象标记为esModule，如果你没有用import，而是用commonjs的require，那么就不会有这一句</p>
<p>那问题又来了，如果是表示esmodule了，有啥用啊！这部分我就不写了，要不就是一篇专门讲import和require区别的文章了。</p>
<p>我直接说结论了</p>
<ul>
<li>如果是import Header form './Header'，在webpack里会转译为类似</li>
</ul>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-built_in">require</span>(<span class="hljs-string">'./Header'</span>).default
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>如果是import * as Header form './Header'，在webpack里会转译为类似</li>
</ul>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">const</span> Header = <span class="hljs-built_in">require</span>(<span class="hljs-string">'./Header'</span>)
Header.default 表示导出的Header组件
Header.A代表导出的A

<span class="hljs-comment">// Header.js</span>
<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> Header;
<span class="hljs-keyword">export</span> <span class="hljs-keyword">const</span> A=<span class="hljs-number">1</span>；
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>如果是import &#123; A &#125; form './Header'，在webpack里会转译为类似</li>
</ul>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-built_in">require</span>(<span class="hljs-string">'./Header'</span>).A
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li><code>export default Header</code> 会被挂在exports的default属性上</li>
<li><code>export const A=1</code>,会被挂在exports的A属性上</li>
</ul>
<p>意思是es6模块实际上被<code>webpack</code>的一套规则还是变味了<code>commonjs</code>规范而已。</p>
<p>上面没看懂？没关系的，更具体更清晰的推论，在<code>tsconfig.js</code>文件的esModuleInterop参数讲解中会有更清晰的解释（这个是站在webpack编译的角度，下面esModuleInterop参数是在ts编译的角度，其实原理都是一样的）。</p>
<p>以下比较简单的文件，我就在文件注释中解释参数了</p>
<h3 data-id="heading-28">.commitlintrc文件解析</h3>
<p>如下的rules的规范如下：<code>rule</code>由<code>name</code>和配置数组组成，如：<code>'name:[0, 'always', 72]'</code>，数组中第一位为<code>level</code>，可选<code>0,1,2</code>，<code>0</code>为<code>disable</code>，<code>1</code>为<code>warning</code>，<code>2</code>为<code>error</code>，第二位为应用与否，可选<code>always|never</code>，第三位该rule的值,下面的值代表你的commit开头必须是这些字段</p>
<pre><code class="hljs language-JAVASCRIPT copyable" lang="JAVASCRIPT"><span class="hljs-built_in">module</span>.exports = &#123;
  <span class="hljs-attr">extends</span>: [<span class="hljs-string">'@commitlint/config-conventional'</span>], <span class="hljs-comment">// 这个插件继承的是angular团队的提交规范</span>
  <span class="hljs-attr">rules</span>: &#123;
    <span class="hljs-string">'type-enum'</span>: [ <span class="hljs-comment">// 解释上面已经提过数组每一位的意思</span>
      <span class="hljs-number">2</span>,
      <span class="hljs-string">'always'</span>,
      [<span class="hljs-string">'build'</span>, <span class="hljs-string">'ci'</span>, <span class="hljs-string">'chore'</span>, <span class="hljs-string">'docs'</span>, <span class="hljs-string">'feat'</span>, <span class="hljs-string">'fix'</span>, <span class="hljs-string">'perf'</span>, <span class="hljs-string">'refactor'</span>, <span class="hljs-string">'revert'</span>, <span class="hljs-string">'style'</span>, <span class="hljs-string">'test'</span>],
    ],
  &#125;,
&#125;;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-29">.editorconfig文件分析</h3>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">// 表明是最顶层的配置文件，发现设为 true 时，才会停止查找.editorconfig 文件</span>
root = <span class="hljs-literal">true</span>

[*]
<span class="hljs-comment">// tab 为 hard-tabs，space 为 soft-tabs 表示缩进符号，我们选的空格</span>
indent_style = space
<span class="hljs-comment">// 设置整数表示规定每级缩进的列数和 soft-tabs 的空格数。</span>
<span class="hljs-comment">// 如果设定为 tab，则会使用 tab_width 的值（如果已指定）</span>
indent_size = <span class="hljs-number">2</span>
<span class="hljs-comment">// 定义换行符，支持 lf、cr 和 crlf</span>
end_of_line = lf
<span class="hljs-comment">// 编码格式，支持 latin1、utf-8、utf-8-bom、utf-16be 和 utf-16le，不建议使用 uft-8-bom</span>
charset = utf-<span class="hljs-number">8</span>
<span class="hljs-comment">// 设为 true 表示会除去换行行首的任意空白字符，false 反之</span>
trim_trailing_whitespace = <span class="hljs-literal">true</span>
<span class="hljs-comment">// 设为 true 表明使文件以一个空白行结尾，false 反之</span>
insert_final_newline = <span class="hljs-literal">true</span>

[*.md]
trim_trailing_whitespace = <span class="hljs-literal">false</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-30">.eslintrc文件分析</h3>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">const</span> OFF = <span class="hljs-number">0</span>;
<span class="hljs-keyword">const</span> WARN = <span class="hljs-number">1</span>;
<span class="hljs-keyword">const</span> ERROR = <span class="hljs-number">2</span>;

<span class="hljs-built_in">module</span>.exports = &#123;
  <span class="hljs-comment">// 要在配置文件中指定环境，请使用env键并通过将每个设置为来指定要启用的环境true。</span>
  <span class="hljs-comment">// 例如，以下启用浏览器和Node.js环境：</span>
  <span class="hljs-comment">// es6表示对于新的ES6全局变量，比如Set的支持，注意跟下面parserOptions的ecmaVersion对比一下</span>
  <span class="hljs-comment">// ecmaVersion: 6 表示启用对于ES6语法的校验</span>
  <span class="hljs-comment">//</span>
  <span class="hljs-attr">env</span>: &#123;
    <span class="hljs-attr">browser</span>: <span class="hljs-literal">true</span>,
    <span class="hljs-attr">es6</span>: <span class="hljs-literal">true</span>,
    <span class="hljs-attr">node</span>: <span class="hljs-literal">true</span>,
  &#125;,
  <span class="hljs-comment">// </span>
  <span class="hljs-attr">extends</span>: [
    <span class="hljs-string">'airbnb'</span>,
    <span class="hljs-string">'airbnb/hooks'</span>,
    <span class="hljs-string">'plugin:react/recommended'</span>,
    <span class="hljs-string">'plugin:unicorn/recommended'</span>,
    <span class="hljs-string">'plugin:promise/recommended'</span>,
    <span class="hljs-string">'plugin:@typescript-eslint/recommended'</span>,
    <span class="hljs-string">'plugin:prettier/recommended'</span>,
  ],
  <span class="hljs-comment">// 指定解析器</span>
  <span class="hljs-comment">// 默认情况下，ESLint使用Espree作为其解析器。您可以选择指定在配置文件中使用其他解析器</span>
  <span class="hljs-attr">parser</span>: <span class="hljs-string">'@typescript-eslint/parser'</span>,
  <span class="hljs-comment">// parserOptions属性在文件中设置解析器选项</span>
  <span class="hljs-comment">// ecmaVersion-设置为3、5（默认），6、7、8、9、10或11，以指定要使用的ECMAScript语法的版本。</span>
  <span class="hljs-comment">// sourceType-设置为"script"（默认），或者"module"代码在ECMAScript模块中。</span>
  <span class="hljs-comment">// ecmaFeatures -一个对象，指示您要使用哪些其他语言功能,参数如下</span>
  <span class="hljs-comment">//   globalReturn-允许return在全局声明</span>
  <span class="hljs-comment">//   impliedStrict-启用全局严格模式（如果ecmaVersion大于等于5）</span>
  <span class="hljs-comment">//   jsx-启用JSX</span>
  <span class="hljs-attr">parserOptions</span>: &#123;
    <span class="hljs-attr">ecmaFeatures</span>: &#123;
      <span class="hljs-attr">impliedStrict</span>: <span class="hljs-literal">true</span>,
      <span class="hljs-attr">jsx</span>: <span class="hljs-literal">true</span>,
    &#125;,
    <span class="hljs-attr">ecmaVersion</span>: <span class="hljs-number">12</span>,
    <span class="hljs-attr">sourceType</span>: <span class="hljs-string">'module'</span>,
  &#125;,
  <span class="hljs-attr">plugins</span>: [<span class="hljs-string">'react'</span>, <span class="hljs-string">'unicorn'</span>, <span class="hljs-string">'promise'</span>, <span class="hljs-string">'@typescript-eslint'</span>, <span class="hljs-string">'prettier'</span>],
  <span class="hljs-attr">settings</span>: &#123;
     <span class="hljs-comment">// 这里的improt/resolver针对插件是eslint-import-resolver-xxx</span>
     <span class="hljs-comment">// 比如下面的typescript里的规则，针对的就是插件eslint-import-resolver-typescript</span>
     <span class="hljs-comment">// 再下面的node就是配置eslint-import-resolver-node</span>
     <span class="hljs-comment">// 有人说我们没依赖eslint-import-resolver-node，哪里来的呢，是因为</span>
     <span class="hljs-comment">// eslint-import-plugin插件依赖，所以也安装了它，这就要涉及到npm依赖包平铺的规则了，下面会讲</span>
    <span class="hljs-string">'import/resolver'</span>: &#123;
      <span class="hljs-attr">typescript</span>: &#123;
        <span class="hljs-attr">directory</span>: <span class="hljs-string">'./tsconfig.json'</span>, <span class="hljs-comment">// 这里主要解决的是别名的问题，tsconfig.json里有别名设置</span>
      &#125;,
      <span class="hljs-attr">node</span>: &#123;
        <span class="hljs-attr">extensions</span>: [<span class="hljs-string">'.tsx'</span>, <span class="hljs-string">'.jsx'</span>, <span class="hljs-string">'.ts'</span>, <span class="hljs-string">'.js'</span>],
      &#125;,
    &#125;,
  &#125;,
  <span class="hljs-attr">rules</span>: &#123;
    <span class="hljs-comment">// 以下规则就不详细讲了，因为很多都是因为typescript插件bug跟eslint冲突不得不关闭一些规则</span>
    <span class="hljs-string">'import/extensions'</span>: [
      ERROR,
      <span class="hljs-string">'ignorePackages'</span>,
      &#123;
        <span class="hljs-attr">ts</span>: <span class="hljs-string">'never'</span>,
        <span class="hljs-attr">tsx</span>: <span class="hljs-string">'never'</span>,
        <span class="hljs-attr">js</span>: <span class="hljs-string">'never'</span>,
      &#125;,
    ],
    <span class="hljs-string">'import/no-extraneous-dependencies'</span>: [ERROR, &#123; <span class="hljs-attr">devDependencies</span>: <span class="hljs-literal">true</span> &#125;],
    <span class="hljs-string">'import/prefer-default-export'</span>: OFF,
    <span class="hljs-string">'import/no-unresolved'</span>: ERROR,
    <span class="hljs-string">'import/no-dynamic-require'</span>: OFF,

    <span class="hljs-string">'unicorn/better-regex'</span>: ERROR,
    <span class="hljs-string">'unicorn/prevent-abbreviations'</span>: OFF,
    <span class="hljs-string">'unicorn/filename-case'</span>: [
      ERROR,
      &#123;
        <span class="hljs-attr">cases</span>: &#123;
          <span class="hljs-comment">// 中划线</span>
          <span class="hljs-attr">kebabCase</span>: <span class="hljs-literal">true</span>,
          <span class="hljs-comment">// 小驼峰</span>
          <span class="hljs-attr">camelCase</span>: <span class="hljs-literal">true</span>,
          <span class="hljs-comment">// 下划线</span>
          <span class="hljs-attr">snakeCase</span>: <span class="hljs-literal">false</span>,
          <span class="hljs-comment">// 大驼峰</span>
          <span class="hljs-attr">pascalCase</span>: <span class="hljs-literal">true</span>,
        &#125;,
      &#125;,
    ],
    <span class="hljs-string">'unicorn/no-array-instanceof'</span>: WARN,
    <span class="hljs-string">'unicorn/no-for-loop'</span>: WARN,
    <span class="hljs-string">'unicorn/prefer-add-event-listener'</span>: [
      ERROR,
      &#123;
        <span class="hljs-attr">excludedPackages</span>: [<span class="hljs-string">'koa'</span>, <span class="hljs-string">'sax'</span>],
      &#125;,
    ],
    <span class="hljs-string">'unicorn/prefer-query-selector'</span>: ERROR,
    <span class="hljs-string">'unicorn/no-null'</span>: OFF,
    <span class="hljs-string">'unicorn/no-array-reduce'</span>: OFF,

    <span class="hljs-string">'@typescript-eslint/no-useless-constructor'</span>: ERROR,
    <span class="hljs-string">'@typescript-eslint/no-empty-function'</span>: WARN,
    <span class="hljs-string">'@typescript-eslint/no-var-requires'</span>: OFF,
    <span class="hljs-string">'@typescript-eslint/explicit-function-return-type'</span>: OFF,
    <span class="hljs-string">'@typescript-eslint/explicit-module-boundary-types'</span>: OFF,
    <span class="hljs-string">'@typescript-eslint/no-explicit-any'</span>: OFF,
    <span class="hljs-string">'@typescript-eslint/no-use-before-define'</span>: ERROR,
    <span class="hljs-string">'@typescript-eslint/no-unused-vars'</span>: WARN,
    <span class="hljs-string">'no-unused-vars'</span>: OFF,

    <span class="hljs-string">'react/jsx-filename-extension'</span>: [ERROR, &#123; <span class="hljs-attr">extensions</span>: [<span class="hljs-string">'.tsx'</span>, <span class="hljs-string">'ts'</span>, <span class="hljs-string">'.jsx'</span>, <span class="hljs-string">'js'</span>] &#125;],
    <span class="hljs-string">'react/jsx-indent-props'</span>: [ERROR, <span class="hljs-number">2</span>],
    <span class="hljs-string">'react/jsx-indent'</span>: [ERROR, <span class="hljs-number">2</span>],
    <span class="hljs-string">'react/jsx-one-expression-per-line'</span>: OFF,
    <span class="hljs-string">'react/destructuring-assignment'</span>: OFF,
    <span class="hljs-string">'react/state-in-constructor'</span>: OFF,
    <span class="hljs-string">'react/jsx-props-no-spreading'</span>: OFF,
    <span class="hljs-string">'react/prop-types'</span>: OFF,

    <span class="hljs-string">'jsx-a11y/click-events-have-key-events'</span>: OFF,
    <span class="hljs-string">'jsx-a11y/no-noninteractive-element-interactions'</span>: OFF,
    <span class="hljs-string">'jsx-a11y/no-static-element-interactions'</span>: OFF,

    <span class="hljs-string">'lines-between-class-members'</span>: [ERROR, <span class="hljs-string">'always'</span>],
    <span class="hljs-comment">// indent: [ERROR, 2, &#123; SwitchCase: 1 &#125;],</span>
    <span class="hljs-string">'linebreak-style'</span>: [ERROR, <span class="hljs-string">'unix'</span>],
    <span class="hljs-attr">quotes</span>: [ERROR, <span class="hljs-string">'single'</span>],
    <span class="hljs-attr">semi</span>: [ERROR, <span class="hljs-string">'always'</span>],
    <span class="hljs-string">'no-unused-expressions'</span>: WARN,
    <span class="hljs-string">'no-plusplus'</span>: OFF,
    <span class="hljs-string">'no-console'</span>: OFF,
    <span class="hljs-string">'class-methods-use-this'</span>: ERROR,
    <span class="hljs-string">'jsx-quotes'</span>: [ERROR, <span class="hljs-string">'prefer-single'</span>],
    <span class="hljs-string">'global-require'</span>: OFF,
    <span class="hljs-string">'no-use-before-define'</span>: OFF,
    <span class="hljs-string">'no-restricted-syntax'</span>: OFF,
    <span class="hljs-string">'no-continue'</span>: OFF,
  &#125;,
&#125;;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>上面提到一个重要的点，就是<code>eslint-import-resolver-node</code>,我们并没有在<code>package.json</code>声明，咋node_modules里面就有它了呢？入下</p>
<pre><code class="copyable">- node_modules
 - eslint-import-resolver-node // 为啥没有安装它，它确在第一层
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这就涉及到npm安装依赖包的规则了，因为<code>eslint-import-plugin</code>依赖<code>eslint-import-resolver-node</code>,所以，<code>node_modules</code>里面就会有，我们就简单讲一下<code>npm</code>包安装(install)规则。</p>
<p>这问题曾经我面试的时候也遇到过，接下来我们简单了解一下：</p>
<h2 data-id="heading-31">嵌套结构</h2>
<p>我们都知道，执行 <code>npm install</code> 后，依赖包被安装到了 <code>node_modules</code>，在 <code>npm</code> 的早期版本， npm 处理依赖的方式简单粗暴，以递归的形式，严格按照 <code>package.json</code> 结构以及子依赖包的 <code>package.json</code> 结构将依赖安装到他们各自的 <code>node_modules</code> 中。直到有子依赖包不在依赖其他模块。也就是说，假如你的package.json如下</p>
<pre><code class="copyable">&#123;
     A模块："1.0.0",
     B模块："1.0.0"
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>然后B模块有依赖C模块，B模块的package.json如下</p>
<pre><code class="copyable">&#123;
    C模块："1.0.0"
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>那么整个项目依赖就是嵌套的，如下：</p>
<pre><code class="copyable">node_modules
 - A模块
 - B模块
  - C模块
<span class="copy-code-btn">复制代码</span></code></pre>
<p>在 Windows 系统中，文件路径最大长度为260个字符，嵌套层级过深可能导致不可预知的问题。</p>
<h2 data-id="heading-32">扁平结构</h2>
<p>为了解决以上问题，NPM 在 3.x 版本做了一次较大更新。其将早期的嵌套结构改为扁平结构：</p>
<p>安装模块时，不管其是直接依赖还是子依赖的依赖，优先将其安装在 <code>node_modules</code> 根目录。</p>
<p>还是上面的依赖结构，我们在执行 <code>npm install</code> 后将得到下面的目录结构：</p>
<pre><code class="copyable">node_modules
 - A模块
 - B模块
 - C模块
<span class="copy-code-btn">复制代码</span></code></pre>
<p>当安装到相同模块时，判断已安装的模块版本是否符合新模块的版本范围，如果符合则跳过，不符合则在当前模块的 node_modules 下安装该模块。</p>
<p>就是说假如C模块依赖A模块的2.0.0版本，依赖图如下：</p>
<pre><code class="copyable">node_modules
 - A模块 1.0.0
 - B模块
 - C模块
    - A模块 2.0.0
<span class="copy-code-btn">复制代码</span></code></pre>
<p>其实铺平的结构也会有问题，我们这里就不详述了，上面提到的那篇文章真的不错，推荐详细看，里面设置npm相关知识的点比这里谈到的多得多。</p>
<h3 data-id="heading-33">.npmrc文件分析</h3>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/0b4bce02e7db4d2282766027e3b2ae01~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-34">.prettierrc文件分析</h3>
<pre><code class="hljs language-javascript copyable" lang="javascript">&#123;
  <span class="hljs-comment">// tab缩进大小,默认为2</span>
  <span class="hljs-attr">tabWidth</span>: <span class="hljs-number">2</span>,
  <span class="hljs-comment">// 使用tab缩进，默认false</span>
  <span class="hljs-attr">useTabs</span>: <span class="hljs-literal">true</span>,
  <span class="hljs-comment">// 使用分号, 默认true</span>
  <span class="hljs-attr">semi</span>: <span class="hljs-literal">false</span>,
  <span class="hljs-comment">// 使用单引号, 默认false(在jsx中配置无效, 默认都是双引号)</span>
  <span class="hljs-attr">singleQuote</span>: <span class="hljs-literal">true</span>,
  <span class="hljs-comment">// 行尾逗号,默认none,可选 none|es5|all</span>
  <span class="hljs-comment">// es5 包括es5中的数组、对象</span>
  <span class="hljs-comment">// all 包括函数对象等所有可选</span>
  <span class="hljs-attr">TrailingCooma</span>: <span class="hljs-string">"none"</span>,
  <span class="hljs-comment">// 对象中的空格 默认true</span>
  <span class="hljs-comment">// true: &#123; foo: bar &#125;</span>
  <span class="hljs-comment">// false: &#123;foo: bar&#125;</span>
  <span class="hljs-attr">bracketSpacing</span>: <span class="hljs-literal">true</span>,
  <span class="hljs-comment">// JSX标签闭合位置 默认false</span>
  <span class="hljs-comment">// false: <div</span>
  <span class="hljs-comment">//          className=""</span>
  <span class="hljs-comment">//          style=&#123;&#123;&#125;&#125;</span>
  <span class="hljs-comment">//       ></span>
  <span class="hljs-comment">// true: <div</span>
  <span class="hljs-comment">//          className=""</span>
  <span class="hljs-comment">//          style=&#123;&#123;&#125;&#125; ></span>
  jsxBracketSameLine：<span class="hljs-literal">false</span>,
  <span class="hljs-comment">// 箭头函数参数括号 默认avoid 可选 avoid| always</span>
  <span class="hljs-comment">// avoid 能省略括号的时候就省略 例如x => x</span>
  <span class="hljs-comment">// always 总是有括号</span>
  <span class="hljs-attr">arrowParens</span>: <span class="hljs-string">'always'</span>, 
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-35">.stylelintrc文件分析</h3>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-built_in">module</span>.exports = &#123;
<span class="hljs-comment">// stylelint的配置可以在已有配置的基础上进行扩展，之后你自己书写的配置项将覆盖已有的配置。</span>
<span class="hljs-comment">// 配置的含义，我们前面已经讲过简单提一下stylelint-config-rational-order是配置书写顺序的</span>
  <span class="hljs-attr">extends</span>: [<span class="hljs-string">'stylelint-config-standard'</span>, <span class="hljs-string">'stylelint-config-rational-order'</span>, <span class="hljs-string">'stylelint-config-prettier'</span>],
  <span class="hljs-comment">// plugins一般是由社区提供的，对stylelint已有规则进行扩展</span>
  <span class="hljs-comment">// 也就说有些规则原本stylelint没有，就要插件自定义规则了</span>
  <span class="hljs-comment">// 'stylelint-declaration-block-no-ignored-properties'这个插件的作用是警告那些不起作用的属性</span>
  <span class="hljs-attr">plugins</span>: [<span class="hljs-string">'stylelint-order'</span>, <span class="hljs-string">'stylelint-declaration-block-no-ignored-properties'</span>, <span class="hljs-string">'stylelint-scss'</span>],
  <span class="hljs-attr">rules</span>: &#123;
  <span class="hljs-comment">// rules不详述了，可以访问这个网站搜寻，https://stylelint.docschina.org/user-guide/plugins/</span>
    <span class="hljs-string">'plugin/declaration-block-no-ignored-properties'</span>: <span class="hljs-literal">true</span>,
    <span class="hljs-string">'comment-empty-line-before'</span>: <span class="hljs-literal">null</span>,
    <span class="hljs-string">'declaration-empty-line-before'</span>: <span class="hljs-literal">null</span>,
    <span class="hljs-string">'function-name-case'</span>: <span class="hljs-string">'lower'</span>,
    <span class="hljs-string">'no-descending-specificity'</span>: <span class="hljs-literal">null</span>,
    <span class="hljs-string">'no-invalid-double-slash-comments'</span>: <span class="hljs-literal">null</span>,
    <span class="hljs-string">'block-no-empty'</span>: <span class="hljs-literal">null</span>,
    <span class="hljs-string">'value-keyword-case'</span>: <span class="hljs-literal">null</span>,
    <span class="hljs-string">'rule-empty-line-before'</span>: [<span class="hljs-string">'always'</span>, &#123; <span class="hljs-attr">except</span>: [<span class="hljs-string">'after-single-line-comment'</span>, <span class="hljs-string">'first-nested'</span>] &#125;],
    <span class="hljs-string">'at-rule-no-unknown'</span>: <span class="hljs-literal">null</span>,
    <span class="hljs-string">'scss/at-rule-no-unknown'</span>: <span class="hljs-literal">true</span>,
  &#125;,
  <span class="hljs-comment">// 忽略校验的文件，其中/**/*是glob语法，指的是所有文件和文件夹</span>
  <span class="hljs-attr">ignoreFiles</span>: [<span class="hljs-string">'node_modules/**/*'</span>, <span class="hljs-string">'build/**/*'</span>, <span class="hljs-string">'dist/**/*'</span>],
&#125;;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-36">tsconfig.json文件分析</h3>
<p>为什么使用 tsconfig.json？</p>
<p>通常我们可以使用 tsc 命令来编译少量 TypeScript 文件, 但如果实际开发的项目，很少是只有单个文件，当我们需要编译整个项目时，就可以使用 tsconfig.json 文件，将需要使用到的配置都写进 tsconfig.json 文件</p>
<pre><code class="hljs language-javascript copyable" lang="javascript">&#123;
   <span class="hljs-comment">// 编译选项，跟编译ts相关</span>
  <span class="hljs-string">"compilerOptions"</span>: &#123;
    <span class="hljs-comment">// 指定编译的ECMAScript目标版本。</span>
    <span class="hljs-comment">// 枚举值："ES3"， "ES5"， "ES6"/ "ES2015"， "ES2016"， "ES2017"，"ESNext"。</span>
    <span class="hljs-comment">// 默认值： “ES3”,ESNext包含提案的内容</span>
    <span class="hljs-string">"target"</span>: <span class="hljs-string">"ES5"</span>,
    <span class="hljs-comment">// 指定生成哪个模块系统代码。枚举值："None"， "CommonJS"， "AMD"， "System"， "UMD"，</span>
    <span class="hljs-comment">// "ES6"， "ES2015"，"ESNext"。默认值根据--target选项不同而不同，当target设置为ES6时，</span>
    <span class="hljs-comment">// 默认module为“ES6”，否则为“commonjs”</span>
    <span class="hljs-string">"module"</span>: <span class="hljs-string">"ESNext"</span>,
    <span class="hljs-comment">// 编译过程中需要引入的库文件的列表。比如没有esnext，Set、Reflect等api会被ts报错</span>
    <span class="hljs-string">"lib"</span>: [<span class="hljs-string">"dom"</span>, <span class="hljs-string">"dom.iterable"</span>, <span class="hljs-string">"esnext"</span>],
    <span class="hljs-comment">// 是否允许编译javascript文件。如果设置为true，js后缀的文件也会被typescript进行编译</span>
    <span class="hljs-string">"allowJs"</span>: <span class="hljs-literal">true</span>,
    <span class="hljs-comment">// 指定 jsx 代码的生成: 'preserve', 'react-native', or 'react'</span>
    <span class="hljs-string">"jsx"</span>: <span class="hljs-string">"react"</span>,
    <span class="hljs-comment">// 下面详解 </span>
    <span class="hljs-string">"isolatedModules"</span>: <span class="hljs-literal">true</span>,
    <span class="hljs-comment">// 用于指定是否启用严格的类型检查，不过到底具体怎么严格我也不知道</span>
    <span class="hljs-string">"strict"</span>: <span class="hljs-literal">true</span>,
    <span class="hljs-comment">// 下面详解</span>
    <span class="hljs-string">"moduleResolution"</span>: <span class="hljs-string">"node"</span>,
    <span class="hljs-comment">// 下面详解</span>
    <span class="hljs-string">"esModuleInterop"</span>: <span class="hljs-literal">true</span>,
    <span class="hljs-string">"resolveJsonModule"</span>: <span class="hljs-literal">true</span>,
    <span class="hljs-comment">// 下面详解</span>
    <span class="hljs-string">"baseUrl"</span>: <span class="hljs-string">"./"</span>,
    <span class="hljs-comment">// 路径别名，跟webpack alias一样，注意你是ts的话，必须webpack和ts都配</span>
    <span class="hljs-string">"paths"</span>: &#123;
      <span class="hljs-string">"Src/*"</span>: [<span class="hljs-string">"src/*"</span>],
      <span class="hljs-string">"Components/*"</span>: [<span class="hljs-string">"src/components/*"</span>],
      <span class="hljs-string">"Utils/*"</span>: [<span class="hljs-string">"src/utils/*"</span>]
    &#125;,
    
    <span class="hljs-comment">// 以下两个是跟装饰器功能有关，experimentalDecorators是 是否开启装饰器</span>
    <span class="hljs-comment">// emitDecoratorMetadata是装饰器里的一个功能，如果你使用依赖注入，有可能需要开启它</span>
    <span class="hljs-comment">// 依赖注入不懂的同学可以略过，后面会写一篇关于学习nestjs前置知识的文章</span>
    <span class="hljs-comment">// 会讲怎么使用emitDecoratorMetadata实现依赖注入</span>
    <span class="hljs-string">"experimentalDecorators"</span>: <span class="hljs-literal">true</span>,
    <span class="hljs-string">"emitDecoratorMetadata"</span>: <span class="hljs-literal">true</span>,

    <span class="hljs-comment">// 禁止对同一个文件的不一致的引用。主要是文件大小写必须一致，比如引用a.js和A.js是不一样的</span>
    <span class="hljs-string">"forceConsistentCasingInFileNames"</span>: <span class="hljs-literal">true</span>,
    <span class="hljs-comment">// 忽略所有的声明文件（ `*.d.ts`）的类型检查</span>
    <span class="hljs-string">"skipLibCheck"</span>: <span class="hljs-literal">true</span>,
    <span class="hljs-comment">// 下面详解</span>
    <span class="hljs-string">"allowSyntheticDefaultImports"</span>: <span class="hljs-literal">true</span>,
    <span class="hljs-comment">// 不生成输出文件</span>
    <span class="hljs-string">"noEmit"</span>: <span class="hljs-literal">true</span>
  &#125;,
  <span class="hljs-string">"exclude"</span>: [<span class="hljs-string">"node_modules"</span>]
&#125;

<span class="copy-code-btn">复制代码</span></code></pre>
<p>上面的jsx选项可以有三个值选择，我们详细解释一下：</p>
<p>jsx可选项包括：preserve, react 和 react-native。</p>
<p>这些模式仅影响编译阶段 - 类型检查不受影响。</p>
<ul>
<li><code>preserve</code>模式将保持<code>JSX</code>作为输出的一部分，又后面的编译器继续编译（例如Babel）。 此外，输出将具有.jsx文件扩展名。</li>
<li>react模式将编译<code>React.createElement</code>，在使用之前不需要经过<code>JSX</code>转换，输出将具有.js文件扩展名。</li>
<li>react-native模式相当于保留，因为它保留了所有<code>JSX</code>，但输出将具有.js文件扩展名</li>
</ul>
<p>isolatedModules，这个选项有点复杂，查阅了不少资料。。。下面详细讲一下：</p>
<ul>
<li>导出非值标识符</li>
</ul>
<p>在 TypeScript 中，你可以引入一个类型，然后再将其导出：</p>
<pre><code class="copyable">import &#123; someType, someFunction &#125; from "someModule";


someFunction();


export &#123; someType, someFunction &#125;;
Try
<span class="copy-code-btn">复制代码</span></code></pre>
<p>由于 <code>someType</code> 并没有值，所以生成的 <code>export</code> 将不会导出它（否则将导致 JavaScript 运行时的错误）：</p>
<pre><code class="copyable">export &#123; someFunction &#125;;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>单文件转译器并不知道 <code>someType</code> 是否会产生一个值，所以导出一个只指向类型的名称会是一个错误。</p>
<ul>
<li>非模块文件</li>
</ul>
<p>如果设置了 <code>isolatedModules</code>，则所有的实现文件必须是模块 （也就是它有某种形式的 <code>import</code>/<code>export</code>）。如果任意文件不是模块就会发生错误：</p>
<pre><code class="copyable">function fn() &#123;&#125;
'index.ts' cannot be compiled under '--isolatedModules' because it is considered a global script file. Add an import, export, or an empty 'export &#123;&#125;' statement to make it a module.'index.ts' cannot be compiled under '--isolatedModules' because it is considered a global script file. Add an import, export, or an empty 'export &#123;&#125;' statement to make it a module.Try
<span class="copy-code-btn">复制代码</span></code></pre>
<p>此限制不适用于 <code>.d.ts</code> 文件</p>
<ul>
<li>指向 <code>const enum</code> 成员</li>
</ul>
<p>在 TypeScript 中，当你引用一个 <code>const enum</code> 的成员时，该引用在生成的 JavaScript 中将会被其实际值所代替。这会将这样的 TypeScript 代码：</p>
<pre><code class="copyable">declare const enum Numbers &#123;
  Zero = 0,
  One = 1,
&#125;
console.log(Numbers.Zero + Numbers.One);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>转换为这样的 JavaScript：</p>
<pre><code class="copyable">"use strict";
console.log(0 + 1);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>在不知道这些成员值的情况下，其他转译器不能替换对 <code>Numbers</code> 的引用。如果无视的话则会导致运行时错误（运行时没有 <code>Numbers</code>） 对象。 正因如此，当启用 <code>isolatedModules</code> 时，引用环境中的 <code>const enum</code> 成员将会是一个错误</p>
<ul>
<li>moduleResolution (参考《tsconfig详细配资》，详见文章底部)</li>
</ul>
<p>可选值： classic | node</p>
<p>我们举一个例子，看看两种模式的工作机制，假设用户主目录下有一个ts-test的项目，里面有一个src目录，src目录下有一个a.ts文件，即<code>/Users/**/ts-test/src/a.ts</code></p>
<ul>
<li><strong>classic模块解析规则</strong>:
<ul>
<li>
<p>对于<strong>相对路径模块</strong>: 只会在当前相对路径下查找是否存在该文件(.ts文件)，<strong>不会作进一步的解析</strong>，如"./src/a.ts"文件中，有一行<code>import &#123; b &#125; from "./b"</code>，那么其只会检测是否存在<code>"./src/b.ts"</code>，没有就算找不到。</p>
</li>
<li>
<p>对于<strong>非相对路径模块</strong>: 编译器则会<strong>从包含导入文件的目录开始依次向上级目录遍历</strong>，<strong>尝试定位匹配的ts文件或者d.ts类型声明文件</strong>，如果<code>/Users/**/ts-test/src/a.ts</code>文件中有一行<code>import &#123; b &#125; from "b"</code>，那么其查找过程如下:</p>
</li>
</ul>
</li>
</ul>
<pre><code class="hljs language-javascript copyable" lang="javascript">/Users<span class="hljs-comment">/**/</span>ts-test/src/b.ts
/Users<span class="hljs-comment">/**/</span>ts-test/src/b.d.ts
/Users<span class="hljs-comment">/**/</span>ts-test/b.ts
/Users<span class="hljs-comment">/**/</span>ts-test/b.d.ts
/Users<span class="hljs-comment">/**/</span>b.ts
/Users<span class="hljs-comment">/**/</span>b.d.ts
/Users/b.ts
/Users/b.d.ts
/b.ts
/b.d.ts
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li><strong>node模块解析规则</strong>:
<ul>
<li>对于<strong>相对路径模块</strong>:除了会在当前相对路径下查找是否存在该文件(.ts文件)外，<strong>还会作进一步的解析</strong>，如果在相对目录下没有找到对应的.ts文件，那么就会看一下是否存在同名的目录</li>
<li>如果有，那么再看一下里面是否有package.json文件，然后看里面有没有配置，main属性</li>
<li>如果配置了，则加载main所指向的文件(.ts或者.d.ts),如果没有配置main属性，那么就会看一下目录里有没有index.ts或者index.d.ts，有则加载。</li>
<li>对于<strong>非相对路径模块</strong>: 对于非相对路径模块，那么会直接到a.ts所在目录下的node_modules目录下去查找，也是遵循逐层遍历的规则，查找规则同上，同上node模块解析规则查找如下（一般情况下是找）:</li>
</ul>
</li>
</ul>
<pre><code class="copyable">/Users/**/ts-test/src/node_modules/b.ts
/Users/**/ts-test/src/node_modules/b.d.ts
/Users/**/ts-test/src/node_modules/b/package.json(如果指定了main)
/Users/**/ts-test/src/node_modules/b/index.ts
/Users/**/ts-test/src/node_modules/b/index.d.ts

/Users/**/ts-test/node_modules/b.ts
/Users/**/ts-test/node_modules/b.d.ts
/Users/**/ts-test/node_modules/b/package.json(如果指定了main)
/Users/**/ts-test/node_modules/index.ts
/Users/**/ts-test/node_modules/index.d.ts

/Users/**/node_modules/b.ts
/Users/**/node_modules/b.d.ts
/Users/**/node_modules/b/package.json(如果指定了main)
/Users/**/node_modules/index.ts
/Users/**/node_modules/index.d.ts

/Users/node_modules/b.ts
/Users/node_modules/b.d.ts
/Users/node_modules/b/package.json(如果指定了main)
/Users/node_modules/index.ts
/Users/node_modules/index.d.ts

/node_modules/b.ts
/node_modules/b.d.ts
/node_modules/b/package.json(如果指定了main)
/node_modules/index.ts
/node_modules/index.d.ts
<span class="copy-code-btn">复制代码</span></code></pre>
<p>以上需要注意一点的是，还有一个typeRoots属性，默认是node_modules/@types，并且<strong>不管是classic解析还是node解析，都会到node_modules/@types目录下查找类型声明文件</strong>，即<strong>typeRoots和模块的解析规则无关</strong></p>
<ul>
<li>baseUrl</li>
</ul>
<p>这个是用于<strong>拓宽引入非相对模块时的查找路径的</strong>。其<strong>默认值就是"./"</strong> ，比如当<code>moduleResolution</code>属性值为node的时候，如果我们引入了一个非相对模块，那么<strong>编译器只会到node_modules目录下去查找</strong>，但是如果配置了<code>baseUrl</code>，那么编译器在<code>node_modules</code>中没有找到的情况下，还会到baseUrl中指定的目录下查找；</p>
<p>同样<code>moduleResolution</code>属性值为<code>classic</code>的时候也是一样，除了到当前目录下找之外(逐层)，如果没有找到还会到<code>baseUrl</code>中指定的目录下查找；就是相当于拓宽了非相对模块的查找路径范围</p>
<ul>
<li>allowSyntheticDefaultImports</li>
</ul>
<p>当设置为 true， 并且模块<strong>没有</strong>显式指定默认导出时，<code>allowSyntheticDefaultImports</code> 可以让你这样写导入：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">import</span> React <span class="hljs-keyword">from</span> <span class="hljs-string">"react"</span>;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>而不是：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">import</span> * <span class="hljs-keyword">as</span> React <span class="hljs-keyword">from</span> <span class="hljs-string">"react"</span>;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>例如：<code>allowSyntheticDefaultImports</code> 不为 true 时：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">// @filename: utilFunctions.js</span>
Module <span class="hljs-string">'"/home/runner/work/TypeScript-Website/TypeScript-Website/packages/typescriptlang-org/utilFunctions"'</span> has no <span class="hljs-keyword">default</span> <span class="hljs-keyword">export</span>.Module <span class="hljs-string">'"/home/runner/work/TypeScript-Website/TypeScript-Website/packages/typescriptlang-org/utilFunctions"'</span> has no <span class="hljs-keyword">default</span> <span class="hljs-keyword">export</span>.
<span class="hljs-keyword">const</span> getStringLength = <span class="hljs-function">(<span class="hljs-params">str</span>) =></span> str.length;


<span class="hljs-built_in">module</span>.exports = &#123;
  getStringLength,
&#125;;


<span class="hljs-comment">// @filename: index.ts</span>
<span class="hljs-keyword">import</span> utils <span class="hljs-keyword">from</span> <span class="hljs-string">"./utilFunctions"</span>;


<span class="hljs-keyword">const</span> count = utils.getStringLength(<span class="hljs-string">"Check JS"</span>);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这段代码会引发一个错误，因为没有“default”对象可以导入，即使你认为应该有。 为了使用方便，Babel 这样的转译器会在没有默认导出时自动为其创建，使模块看起来更像：</p>
<pre><code class="copyable">// @filename: utilFunctions.js
const getStringLength = (str) => str.length;
const allFunctions = &#123;
  getStringLength,
&#125;;
module.exports = allFunctions;
module.exports.default = allFunctions;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>本选项不会影响 TypeScript 生成的 JavaScript，它仅对类型检查起作用。</p>
<ul>
<li>esModuleInterop</li>
</ul>
<p>这个参数涉及到es6模块和commonjs模块互相转换知识点了。具体参考这篇文章（这一参数就是一篇文章<a href="https://link.juejin.cn/?target=https%3A%2F%2Fzhuanlan.zhihu.com%2Fp%2F148081795" target="_blank" rel="nofollow noopener noreferrer" title="https://zhuanlan.zhihu.com/p/148081795" ref="nofollow noopener noreferrer"> esModuleInterop 到底做了什么？</a>, 我这里简引用一下这篇文章的关键点。</p>
<p>首先我们看一下<code>import</code>语法在ts中是如何被转译的！</p>
<ul>
<li>TS 默认编译规则</li>
</ul>
<p>TS 对于 import 变量的转译规则为：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"> <span class="hljs-comment">// before</span>
 <span class="hljs-keyword">import</span> React <span class="hljs-keyword">from</span> <span class="hljs-string">'react'</span>;
 <span class="hljs-built_in">console</span>.log(React)
 <span class="hljs-comment">// after</span>
 <span class="hljs-keyword">var</span> React = <span class="hljs-built_in">require</span>(<span class="hljs-string">'react'</span>);
 <span class="hljs-built_in">console</span>.log(React[<span class="hljs-string">'default'</span>])


 <span class="hljs-comment">// before</span>
 <span class="hljs-keyword">import</span> &#123;Component&#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'react'</span>;
 <span class="hljs-built_in">console</span>.log(Component);
 <span class="hljs-comment">// after</span>
 <span class="hljs-keyword">var</span> React = <span class="hljs-built_in">require</span>(<span class="hljs-string">'react'</span>);
 <span class="hljs-built_in">console</span>.log(React.Component)
 

 <span class="hljs-comment">// before </span>
 <span class="hljs-keyword">import</span> * <span class="hljs-keyword">as</span> React <span class="hljs-keyword">from</span> <span class="hljs-string">'react'</span>;
 <span class="hljs-built_in">console</span>.log(React);
 <span class="hljs-comment">// after</span>
 <span class="hljs-keyword">var</span> React = <span class="hljs-built_in">require</span>(<span class="hljs-string">'react'</span>);
 <span class="hljs-built_in">console</span>.log(React);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>结论，可以看到：</p>
<ul>
<li>对于 <code>import</code> 导入默认导出的模块，<code>TS</code> 在读这个模块的时候会去读取上面的 <code>default</code> 属性</li>
<li>对于 <code>import</code> 导入非默认导出的变量，<code>TS</code> 会去读这个模块上面对应的属性</li>
<li>对于 <code>import *，TS</code> 会直接读该模块</li>
</ul>
<p><code>TS、babel</code> 对 export` 变量的转译规则为：（代码经过简化）</p>
<pre><code class="copyable"> // before
 export const name = "esm";
 export default &#123;
   name: "esm default",
 &#125;;

 // after
 exports.__esModule = true;
 exports.name = "esm";
 exports["default"] = &#123;
   name: "esm default"
 &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>可以看到：</p>
<ul>
<li>对于 <code>export default</code> 的变量，<code>TS</code> 会将其放在 <code>module.exports</code> 的 default 属性上</li>
<li>对于 <code>export</code> 的变量，<code>TS </code>会将其放在 <code>module.exports</code> 对应变量名的属性上</li>
<li>额外给 <code>module.exports</code> 增加一个<code> __esModule: true 的属性，用来告诉编译器，这本来是一个 esm 模块</code></li>
</ul>
<h3 data-id="heading-37">TS 开启 esModuleInterop 后的编译规则</h3>
<p>回到标题上，<code>esModuleInterop</code> 这个属性默认为 false。改成 true 之后，TS 对于 import 的转译规则会发生一些变化（export 的规则不会变）：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"> <span class="hljs-comment">// before</span>
 <span class="hljs-keyword">import</span> React <span class="hljs-keyword">from</span> <span class="hljs-string">'react'</span>;
 <span class="hljs-built_in">console</span>.log(React);
 <span class="hljs-comment">// after 代码经过简化</span>
 <span class="hljs-comment">// __importDefault规则如下：</span>
 <span class="hljs-comment">// 如果目标模块是 esm，就直接返回目标模块；否则将目标模块挂在一个对象的 defalut 上，返回该对象</span>
 <span class="hljs-keyword">var</span> react = __importDefault(<span class="hljs-built_in">require</span>(<span class="hljs-string">'react'</span>));
 <span class="hljs-built_in">console</span>.log(react[<span class="hljs-string">'default'</span>]);


 <span class="hljs-comment">// before</span>
 <span class="hljs-keyword">import</span> &#123;Component&#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'react'</span>;
 <span class="hljs-built_in">console</span>.log(Component);
 <span class="hljs-comment">// after 代码经过简化</span>
 <span class="hljs-keyword">var</span> react = <span class="hljs-built_in">require</span>(<span class="hljs-string">'react'</span>);
 <span class="hljs-built_in">console</span>.log(react.Component);
 
 
 <span class="hljs-comment">// before</span>
 <span class="hljs-keyword">import</span> * <span class="hljs-keyword">as</span> React <span class="hljs-keyword">from</span> <span class="hljs-string">'react'</span>;
 <span class="hljs-built_in">console</span>.log(React);
 <span class="hljs-comment">// after 代码经过简化</span>
 <span class="hljs-comment">// _importStar 规则如下</span>
 <span class="hljs-comment">// 如果目标模块是 esm，就直接返回目标模块。否则</span>
 <span class="hljs-comment">// 将目标模块上所有的除了 default 以外的属性挪到 result 上</span>
 <span class="hljs-comment">// 将目标模块自己挂到 result.default 上</span>
 <span class="hljs-keyword">var</span> react = _importStar(<span class="hljs-built_in">require</span>(<span class="hljs-string">'react'</span>));
 <span class="hljs-built_in">console</span>.log(react);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>可以看到，对于默认导入和 namespace（*）导入，TS 使用了两个 helper 函数来帮忙</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">// 代码经过简化</span>
<span class="hljs-keyword">var</span> __importDefault = <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params">mod</span>) </span>&#123;
  <span class="hljs-keyword">return</span> mod && mod.__esModule ? mod : &#123; <span class="hljs-attr">default</span>: mod &#125;;
&#125;;

<span class="hljs-keyword">var</span> __importStar = <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params">mod</span>) </span>&#123;
  <span class="hljs-keyword">if</span> (mod && mod.__esModule) &#123;
    <span class="hljs-keyword">return</span> mod;
  &#125;

  <span class="hljs-keyword">var</span> result = &#123;&#125;;
  <span class="hljs-keyword">for</span> (<span class="hljs-keyword">var</span> k <span class="hljs-keyword">in</span> mod) &#123;
    <span class="hljs-keyword">if</span> (k !== <span class="hljs-string">"default"</span> && mod.hasOwnProperty(k)) &#123;
      result[k] = mod[k]
    &#125;
  &#125;
  result[<span class="hljs-string">"default"</span>] = mod;

  <span class="hljs-keyword">return</span> result;
&#125;;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>其实这个参数对于我们项目而言没有用，因为<code>@babel/preset-typescript</code>会把类型清除掉，<code>webpack</code> 不会调用 <code>tsc</code>，<code>tsconfig.json</code> 也会被忽略掉。</p>
<p>但是可以帮助我们拓宽视野，这样面试官让你聊<code>es6</code>模块和<code>commonjs</code>模块转换的话题（cjs 导入 esm （一般不会这样使用，除开这种情况），就会游刃有余</p>
<h3 data-id="heading-38">webpack相关配置</h3>
<p>首先是工具文件：</p>
<h3 data-id="heading-39">env.js</h3>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">// 判读是否是生产环境，这里这个项目的作者取了一个巧，判断非develop环境是这样的</span>
<span class="hljs-comment">// process.env.NODE_ENV !== 'production'</span>
<span class="hljs-comment">// 这样写不要好，有可能你们公司有很多环境，比如还有预发、灰度环境等等</span>
<span class="hljs-keyword">const</span> isDevelopment = process.env.NODE_ENV !== <span class="hljs-string">'production'</span>;
<span class="hljs-keyword">const</span> isProduction = process.env.NODE_ENV === <span class="hljs-string">'production'</span>;

<span class="hljs-built_in">module</span>.exports = &#123;
  isDevelopment,
  isProduction,
&#125;;

<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-40">path.js</h3>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">// 以下是两个node模块</span>
<span class="hljs-keyword">const</span> path = <span class="hljs-built_in">require</span>(<span class="hljs-string">'path'</span>);
<span class="hljs-keyword">const</span> fs = <span class="hljs-built_in">require</span>(<span class="hljs-string">'fs'</span>);

<span class="hljs-comment">// 同步获取node执行的文件的工作目录, 我们的工作目录一般都是项目的根目录，这里就表示根目录</span>
<span class="hljs-comment">// 为啥这么说呢，因为package.json写着webpack --config ./scripts/config/webpack.prod.js</span>
<span class="hljs-comment">// webpack就是借助node的能力，它的 ./scripts就暴露是以项目目录为根目录</span>
<span class="hljs-comment">// 这里需要注意process.cwd和__dirname的区别</span>
<span class="hljs-comment">// process.cwd()返回当前工作目录。如：调用node命令执行脚本时的目录。</span>
<span class="hljs-comment">// __dirname返回源代码所在的目录</span>
<span class="hljs-keyword">const</span> appDirectory = fs.realpathSync(process.cwd());

<span class="hljs-comment">// 获取绝对路径的方法函数</span>
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">resolveApp</span>(<span class="hljs-params">relativePath</span>) </span>&#123;
  <span class="hljs-keyword">return</span> path.resolve(appDirectory, relativePath);
&#125;

<span class="hljs-comment">// 默认extentions</span>
<span class="hljs-keyword">const</span> moduleFileExtensions = [<span class="hljs-string">'ts'</span>, <span class="hljs-string">'tsx'</span>, <span class="hljs-string">'js'</span>, <span class="hljs-string">'jsx'</span>];

<span class="hljs-comment">/**
 * Resolve module path
 * <span class="hljs-doctag">@param <span class="hljs-type">&#123;function&#125;</span> </span>resolveFn resolve function
 * <span class="hljs-doctag">@param <span class="hljs-type">&#123;string&#125;</span> </span>filePath file path
 */</span>
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">resolveModule</span>(<span class="hljs-params">resolveFn, filePath</span>) </span>&#123;
  <span class="hljs-comment">// Check if the file exists</span>
  <span class="hljs-keyword">const</span> extension = moduleFileExtensions.find(<span class="hljs-function">(<span class="hljs-params">ex</span>) =></span> fs.existsSync(resolveFn(<span class="hljs-string">`<span class="hljs-subst">$&#123;filePath&#125;</span>.<span class="hljs-subst">$&#123;ex&#125;</span>`</span>)));

  <span class="hljs-keyword">if</span> (extension) &#123;
    <span class="hljs-keyword">return</span> resolveFn(<span class="hljs-string">`<span class="hljs-subst">$&#123;filePath&#125;</span>.<span class="hljs-subst">$&#123;extension&#125;</span>`</span>);
  &#125;
  <span class="hljs-keyword">return</span> resolveFn(<span class="hljs-string">`<span class="hljs-subst">$&#123;filePath&#125;</span>.ts`</span>); <span class="hljs-comment">// default is .ts</span>
&#125;

<span class="hljs-built_in">module</span>.exports = &#123;
  <span class="hljs-attr">appBuild</span>: resolveApp(<span class="hljs-string">'build'</span>),
  <span class="hljs-attr">appPublic</span>: resolveApp(<span class="hljs-string">'public'</span>),
  <span class="hljs-attr">appIndex</span>: resolveModule(resolveApp, <span class="hljs-string">'src/index'</span>), <span class="hljs-comment">// Package entry path</span>
  <span class="hljs-attr">appHtml</span>: resolveApp(<span class="hljs-string">'public/index.html'</span>),
  <span class="hljs-attr">appNodeModules</span>: resolveApp(<span class="hljs-string">'node_modules'</span>), <span class="hljs-comment">// node_modules path</span>
  <span class="hljs-attr">appSrc</span>: resolveApp(<span class="hljs-string">'src'</span>),
  <span class="hljs-attr">appSrcComponents</span>: resolveApp(<span class="hljs-string">'src/components'</span>),
  <span class="hljs-attr">appSrcUtils</span>: resolveApp(<span class="hljs-string">'src/utils'</span>),
  <span class="hljs-attr">appProxySetup</span>: resolveModule(resolveApp, <span class="hljs-string">'src/setProxy'</span>),
  <span class="hljs-attr">appPackageJson</span>: resolveApp(<span class="hljs-string">'package.json'</span>),
  <span class="hljs-attr">appTsConfig</span>: resolveApp(<span class="hljs-string">'tsconfig.json'</span>),
  moduleFileExtensions,
&#125;;

<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-41">webpack.common.js</h3>
<p>这是<code>webpack</code>生产环境和开发环境共同的配置文件
以下需要特别注意的参数是'css-loader'里有个importLoaders的参数，它的意思是需要举一个例子就明白了，</p>
<p>如下图：importLoader是1
<img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/a4a251ff5a4d408eb4d63ca746df1b36~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<ul>
<li>
<p>我们在写<code>sass</code>或者<code>less</code>的时候可以<code>@import</code>去引入其他的<code>sass</code>或<code>less</code>文件，此时引用的文件如何被loader处理就跟这个参数有关了。</p>
</li>
<li>
<p>当<code>css-loader</code>处理<code>index.scss</code>文件，读取到<code>@import</code>语句的时候， 因为将<code>importLoaders</code>设置为<code>1</code>，那么<code>a.scss</code>和<code>b.scss</code>会被<code>postcss-loader</code>给处理</p>
</li>
<li>
<p>如果将<code>importLoaders</code>设置为<code>2</code>，那么 <code>a.scss</code>和<code>b.scss</code>就会被<code>postcss-loader</code>和<code>sass-loader</code>给处理</p>
</li>
</ul>
<p>下面的<code>externals</code>属性是一个常见<code>webpack</code>优化点，比如你会把<code>react，react-dom</code>放入<code>cdn</code>，这样就不用打包他们</p>
<p>这里还有一些<code>webpack5</code>和<code>webpack4</code>相同功能但配置有些区别的点：</p>
<ul>
<li>之前使用 <code>file-loader</code> ，但是<code> webpack5</code> 现在已默认内置资源模块，根据官方配置，现在可以改为以下配置方式，不再需要安装额外插件：</li>
</ul>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-built_in">module</span>.exports = &#123;
  <span class="hljs-attr">output</span>: &#123;
    <span class="hljs-comment">// ...</span>
    <span class="hljs-attr">assetModuleFilename</span>: <span class="hljs-string">'images/[name].[contenthash:8].[ext]'</span>,
  &#125;,
  <span class="hljs-comment">// other...</span>
  <span class="hljs-attr">module</span>: &#123;
    <span class="hljs-attr">rules</span>: [
      <span class="hljs-comment">// other...</span>
      &#123;
        <span class="hljs-attr">test</span>: [<span class="hljs-regexp">/\.bmp$/</span>, <span class="hljs-regexp">/\.gif$/</span>, <span class="hljs-regexp">/\.jpe?g$/</span>, <span class="hljs-regexp">/\.png$/</span>],
        <span class="hljs-attr">type</span>: <span class="hljs-string">'asset'</span>,
        <span class="hljs-attr">parser</span>: &#123;
          <span class="hljs-attr">dataUrlCondition</span>: &#123;
            <span class="hljs-attr">maxSize</span>: <span class="hljs-number">4</span> * <span class="hljs-number">1024</span>,
          &#125;,
        &#125;,
      &#125;,
      &#123;
        <span class="hljs-attr">test</span>: <span class="hljs-regexp">/\.(eot|svg|ttf|woff|woff2?)$/</span>,
        type: <span class="hljs-string">'asset/resource'</span>,
      &#125;,
    ]
  &#125;,
  <span class="hljs-attr">plugins</span>: [<span class="hljs-comment">//...],</span>
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-42">缓存</h4>
<p>这里提一个醒<code>dll</code>在<code>webpack</code>里已经过时了！过时了！以后谁给你推荐这个webpack优化就别理他就行了！因为配置hard-source-webpack-plugin都比配置dll容易的多，这还是webpack4的配置。都过时了</p>
<p>之前可以使用插件 <code>hard-source-webpack-plugin</code> 实现缓存，大大加快二次编译速度，现在<code>webpack5</code>现在默认支持缓存，我们只需要以下配置即可：</p>
<pre><code class="hljs language-JAVASCRIPT copyable" lang="JAVASCRIPT"><span class="hljs-built_in">module</span>.exports = &#123;
  <span class="hljs-comment">//...</span>
  <span class="hljs-attr">cache</span>: &#123;
   <span class="hljs-comment">// 默认type是memory也就是缓存放到内存中</span>
    <span class="hljs-attr">type</span>: <span class="hljs-string">'filesystem'</span>,
    <span class="hljs-attr">buildDependencies</span>: &#123;
      <span class="hljs-attr">config</span>: [__filename],
    &#125;,
  &#125;,
  <span class="hljs-comment">//...</span>
&#125;;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><code>cache.buildDependencies</code>，它可以指定构建过程中的代码依赖。它的值类型有两种：文件和目录。</p>
<ul>
<li>目录类型必须以斜杠（/）结尾。其他所有内容都解析为文件类型。</li>
<li>对于目录类型来说，会解析其最近的 package.json 中的 dependencies。</li>
<li>对于文件类型来说，我们将查看 node.js 模块缓存以寻找其依赖。</li>
</ul>
<p>如下示例的意思是：
<code>__filename</code> 变量指向 <code>node.js</code> 中的当前文件。</p>
<pre><code class="hljs language-javascript copyable" lang="javascript">cache.buildDependencies: &#123;
    <span class="hljs-comment">// 它的作用是当配置文件内容或配置文件依赖的模块文件发生变化时，当前的构建缓存即失效</span>
    <span class="hljs-attr">config</span>: [__filename]
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>注意：当设置 <code>cache.type: "filesystem"</code> 时，<code>webpack</code> 会在内部以分层方式启用文件系统缓存和内存缓存。 从缓存读取时，会先查看内存缓存，如果内存缓存未找到，则降级到文件系统缓存。 写入缓存将同时写入内存缓存和文件系统缓存。也就是说它比<code>memory</code>模式更好</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">// 插件把 webpack 打包后的静态文件自动插入到 html 文件当中</span>
<span class="hljs-keyword">const</span> HtmlWebpackPlugin = <span class="hljs-built_in">require</span>(<span class="hljs-string">'html-webpack-plugin'</span>);
<span class="hljs-comment">// 用来分离css为单独的文件</span>
<span class="hljs-keyword">const</span> MiniCssExtractPlugin = <span class="hljs-built_in">require</span>(<span class="hljs-string">'mini-css-extract-plugin'</span>);
<span class="hljs-comment">// 添加打包进度条插件</span>
<span class="hljs-keyword">const</span> WebpackBar = <span class="hljs-built_in">require</span>(<span class="hljs-string">'webpackbar'</span>);
<span class="hljs-comment">// 它在一个单独的进程上运行类型检查器，该插件在编译之间重用抽象语法树，并与TSLint共享这些树。</span>
<span class="hljs-comment">// 可以通过多进程模式进行扩展，以利用最大的CPU能力。</span>
<span class="hljs-keyword">const</span> ForkTsCheckerWebpackPlugin = <span class="hljs-built_in">require</span>(<span class="hljs-string">'fork-ts-checker-webpack-plugin'</span>);
<span class="hljs-comment">// 在webpack中拷贝文件和文件夹</span>
<span class="hljs-keyword">const</span> CopyPlugin = <span class="hljs-built_in">require</span>(<span class="hljs-string">'copy-webpack-plugin'</span>);
<span class="hljs-comment">// 引入路径工具，上文已讲</span>
<span class="hljs-keyword">const</span> paths = <span class="hljs-built_in">require</span>(<span class="hljs-string">'../paths'</span>);
<span class="hljs-comment">// 引入环境判断工具，上文已讲</span>
<span class="hljs-keyword">const</span> &#123; isDevelopment, isProduction &#125; = <span class="hljs-built_in">require</span>(<span class="hljs-string">'../env'</span>);
<span class="hljs-comment">// 引入配置文件，上文已讲</span>
<span class="hljs-keyword">const</span> &#123; imageInlineSizeLimit &#125; = <span class="hljs-built_in">require</span>(<span class="hljs-string">'../conf'</span>);

<span class="hljs-comment">// 这个函数是用来加载css相关loader的函数</span>
<span class="hljs-comment">// 如果是开发环境用style-loader，将css内嵌到html中，反之css单独打包</span>
<span class="hljs-keyword">const</span> getCssLoaders = <span class="hljs-function">(<span class="hljs-params">importLoaders</span>) =></span> [
  isDevelopment ? <span class="hljs-string">'style-loader'</span> : MiniCssExtractPlugin.loader,
  &#123;
    <span class="hljs-attr">loader</span>: <span class="hljs-string">'css-loader'</span>,
    <span class="hljs-attr">options</span>: &#123;
      <span class="hljs-attr">modules</span>: <span class="hljs-literal">false</span>,
      <span class="hljs-attr">sourceMap</span>: isDevelopment,
      importLoaders,
    &#125;,
  &#125;,
  &#123;
    <span class="hljs-attr">loader</span>: <span class="hljs-string">'postcss-loader'</span>,
    <span class="hljs-attr">options</span>: &#123;
      <span class="hljs-attr">postcssOptions</span>: &#123;
        <span class="hljs-attr">plugins</span>: [
          <span class="hljs-built_in">require</span>(<span class="hljs-string">'postcss-flexbugs-fixes'</span>),
          isProduction && [   <span class="hljs-comment">// 开发环境不使用postcss-preset-env加浏览器前缀，加快打包时间</span>
            <span class="hljs-string">'postcss-preset-env'</span>,
            &#123;
              <span class="hljs-attr">autoprefixer</span>: &#123;
                <span class="hljs-attr">grid</span>: <span class="hljs-literal">true</span>,
                <span class="hljs-attr">flexbox</span>: <span class="hljs-string">'no-2009'</span>,
              &#125;,
              <span class="hljs-attr">stage</span>: <span class="hljs-number">3</span>,
            &#125;,
          ],
        ].filter(<span class="hljs-built_in">Boolean</span>),
      &#125;,
    &#125;,
  &#125;,
];

<span class="hljs-built_in">module</span>.exports = &#123;
  <span class="hljs-comment">// 入口信息</span>
  <span class="hljs-attr">entry</span>: &#123;
    <span class="hljs-attr">app</span>: paths.appIndex,
  &#125;,
  <span class="hljs-attr">cache</span>: &#123;
    <span class="hljs-attr">type</span>: <span class="hljs-string">'filesystem'</span>,
    <span class="hljs-attr">buildDependencies</span>: &#123;
      <span class="hljs-attr">config</span>: [__filename],
    &#125;,
  &#125;,
  <span class="hljs-comment">// 这里可以设置extensions和别名</span>
  <span class="hljs-comment">// extensions就是webpack会识别的文件后缀的顺序，</span>
  <span class="hljs-comment">// 如果你是tsx建议放到第一位，否则你写成['ts','tsx']会先检测是否是ts文件，不是才接着看是不是tsx</span>
  <span class="hljs-attr">resolve</span>: &#123;
    <span class="hljs-attr">extensions</span>: [<span class="hljs-string">'.tsx'</span>, <span class="hljs-string">'.ts'</span>, <span class="hljs-string">'.js'</span>, <span class="hljs-string">'.json'</span>],
    <span class="hljs-attr">alias</span>: &#123;
      <span class="hljs-attr">Src</span>: paths.appSrc,
      <span class="hljs-attr">Components</span>: paths.appSrcComponents,
      <span class="hljs-attr">Utils</span>: paths.appSrcUtils,
    &#125;,
  &#125;,
  <span class="hljs-attr">externals</span>: &#123;
    <span class="hljs-attr">react</span>: <span class="hljs-string">'React'</span>,
    <span class="hljs-string">'react-dom'</span>: <span class="hljs-string">'ReactDOM'</span>,
    <span class="hljs-attr">axios</span>: <span class="hljs-string">'axios'</span>,
  &#125;,
  <span class="hljs-attr">module</span>: &#123;
    <span class="hljs-attr">rules</span>: [
      &#123;
        <span class="hljs-attr">test</span>: <span class="hljs-regexp">/\.(tsx?|js)$/</span>,
        loader: <span class="hljs-string">'babel-loader'</span>,
        <span class="hljs-attr">options</span>: &#123; <span class="hljs-attr">cacheDirectory</span>: <span class="hljs-literal">true</span> &#125;, <span class="hljs-comment">// 这是一个webpack优化点，使用缓存</span>
        <span class="hljs-attr">exclude</span>: <span class="hljs-regexp">/node_modules/</span>, <span class="hljs-comment">// 这个也是webpack优化的点 exclude排除不需要编译的文件夹</span>
      &#125;,
      &#123;
        <span class="hljs-attr">test</span>: <span class="hljs-regexp">/\.css$/</span>,
        use: getCssLoaders(<span class="hljs-number">1</span>),  <span class="hljs-comment">// 这个讲得就是importLoaders属性运用，上面已经讲了</span>
      &#125;,
      &#123;
        <span class="hljs-attr">test</span>: <span class="hljs-regexp">/\.scss$/</span>,
        use: [
          ...getCssLoaders(<span class="hljs-number">2</span>),
          &#123;
            <span class="hljs-attr">loader</span>: <span class="hljs-string">'sass-loader'</span>,
            <span class="hljs-attr">options</span>: &#123;
              <span class="hljs-attr">sourceMap</span>: isDevelopment,
            &#125;,
          &#125;,
        ],
      &#125;,
      &#123;
        <span class="hljs-attr">test</span>: [<span class="hljs-regexp">/\.bmp$/</span>, <span class="hljs-regexp">/\.gif$/</span>, <span class="hljs-regexp">/\.jpe?g$/</span>, <span class="hljs-regexp">/\.png$/</span>], 
        <span class="hljs-attr">type</span>: <span class="hljs-string">'asset'</span>, <span class="hljs-comment">// webpack5自带的loader，webpack4依赖file-loader</span>
        <span class="hljs-attr">parser</span>: &#123;
          <span class="hljs-attr">dataUrlCondition</span>: &#123;
            <span class="hljs-attr">maxSize</span>: imageInlineSizeLimit,
          &#125;,
        &#125;,
      &#125;,
      &#123;
        <span class="hljs-attr">test</span>: <span class="hljs-regexp">/\.(eot|svg|ttf|woff|woff2?)$/</span>,
        type: <span class="hljs-string">'asset/resource'</span>, <span class="hljs-comment">// webpack5自带的loader，webpack4依赖file-loader</span>
      &#125;,
    ],
  &#125;,
  <span class="hljs-attr">plugins</span>: [
    <span class="hljs-keyword">new</span> HtmlWebpackPlugin(&#123; <span class="hljs-comment">// 这个模块是重点，下面详细讲</span>
      <span class="hljs-attr">template</span>: paths.appHtml,
      <span class="hljs-attr">cache</span>: <span class="hljs-literal">true</span>,
    &#125;),
    <span class="hljs-keyword">new</span> CopyPlugin(&#123; <span class="hljs-comment">// 这个是复制文件或者目录的插件</span>
      <span class="hljs-attr">patterns</span>: [
        &#123;
          <span class="hljs-attr">context</span>: paths.appPublic,
          <span class="hljs-attr">from</span>: <span class="hljs-string">'*'</span>,
          <span class="hljs-attr">to</span>: paths.appBuild,
          <span class="hljs-attr">toType</span>: <span class="hljs-string">'dir'</span>,
          <span class="hljs-attr">globOptions</span>: &#123;
            <span class="hljs-attr">dot</span>: <span class="hljs-literal">true</span>,
            <span class="hljs-attr">gitignore</span>: <span class="hljs-literal">true</span>,
            <span class="hljs-attr">ignore</span>: [<span class="hljs-string">'**/index.html'</span>],
          &#125;,
        &#125;,
      ],
    &#125;),
    <span class="hljs-comment">// 打包进度条插件</span>
    <span class="hljs-keyword">new</span> WebpackBar(&#123;
      <span class="hljs-attr">name</span>: isDevelopment ? <span class="hljs-string">'RUNNING'</span> : <span class="hljs-string">'BUNDLING'</span>,
      <span class="hljs-attr">color</span>: isDevelopment ? <span class="hljs-string">'#52c41a'</span> : <span class="hljs-string">'#722ed1'</span>,
    &#125;),
    <span class="hljs-comment">// 插件功能上面已写</span>
    <span class="hljs-keyword">new</span> ForkTsCheckerWebpackPlugin(&#123;
      <span class="hljs-attr">typescript</span>: &#123;
        <span class="hljs-attr">configFile</span>: paths.appTsConfig,
      &#125;,
    &#125;),
  ],
&#125;;

<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>
<p>HtmlWebpackPlugin</p>
<ul>
<li>title</li>
</ul>
<p>生成html文件的标题</p>
<ul>
<li>filename</li>
</ul>
<p>就是html文件的文件名，默认是index.html</p>
<ul>
<li>template</li>
</ul>
<p>指定你生成的文件所依赖哪一个html文件模板，模板类型可以是html、ejs</p>
<p>如果你设置的 <code>title</code> 和 <code>filename</code>于模板中发生了冲突，那么以你的<code>title</code> 和 <code>filename</code> 的配置值为准。</p>
<ul>
<li>
<p>inject**</p>
<p>inject有四个值： <code>true</code> <code>body</code> <code>head</code> <code>false</code></p>
<ul>
<li><code>true</code> 默认值，script标签位于html文件的 body 底部</li>
<li><code>body</code> script标签位于html文件的 body 底部</li>
<li><code>head</code> script标签位于html文件的 head中</li>
<li><code>false</code> 不插入生成的js文件，这个几乎不会用到的</li>
</ul>
</li>
<li>
<p>favicon</p>
</li>
</ul>
<p>给你生成的html文件生成一个 <code>favicon</code> ,值是一个路径</p>
<pre><code class="hljs language-javascript copyable" lang="javascript">plugins: [
    <span class="hljs-keyword">new</span> HtmlWebpackPlugin(&#123;
        ...
        <span class="hljs-attr">favicon</span>: <span class="hljs-string">'path/to/my_favicon.ico'</span>
    &#125;) 
<span class="copy-code-btn">复制代码</span></code></pre>
<p>然后再生成的html中就有了一个 <code>link</code> 标签</p>
<ul>
<li>minify</li>
</ul>
<p>使用minify会对生成的html文件进行压缩。注意,不能直接这样写：<code>minify: true</code> ,  使用时候必须给定一个 <code>&#123; &#125; </code>对象 ）</p>
<pre><code class="hljs language-javascript copyable" lang="javascript">plugins: [
    <span class="hljs-keyword">new</span> HtmlWebpackPlugin(&#123;
        ...
        <span class="hljs-attr">minify</span>: &#123;
            <span class="hljs-attr">removeAttributeQuotes</span>: <span class="hljs-literal">true</span> <span class="hljs-comment">// 移除属性的引号</span>
        &#125;
    &#125;)
]
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>chunks</li>
</ul>
<p>chunks主要用于多入口文件，当你有多个入口文件，那就回编译后生成多个打包后的文件，那么<code>chunks</code> 就能选择你要使用那些js文件</p>
<pre><code class="hljs language-javascript copyable" lang="javascript">entry: &#123;
    <span class="hljs-attr">index</span>: path.resolve(__dirname, <span class="hljs-string">'./src/index.js'</span>),
    <span class="hljs-attr">devor</span>: path.resolve(__dirname, <span class="hljs-string">'./src/devor.js'</span>),
    <span class="hljs-attr">main</span>: path.resolve(__dirname, <span class="hljs-string">'./src/main.js'</span>)
&#125;

<span class="hljs-attr">plugins</span>: [
    <span class="hljs-keyword">new</span> httpWebpackPlugin(&#123;
        <span class="hljs-attr">chunks</span>: [<span class="hljs-string">'index'</span>,<span class="hljs-string">'main'</span>]
    &#125;)
]
<span class="copy-code-btn">复制代码</span></code></pre>
<p>那么编译后：</p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">script</span> <span class="hljs-attr">type</span>=<span class="hljs-string">text/javascript</span> <span class="hljs-attr">src</span>=<span class="hljs-string">"index.js"</span>></span><span class="hljs-tag"></<span class="hljs-name">script</span>></span>
<span class="hljs-tag"><<span class="hljs-name">script</span> <span class="hljs-attr">type</span>=<span class="hljs-string">text/javascript</span> <span class="hljs-attr">src</span>=<span class="hljs-string">"main.js"</span>></span><span class="hljs-tag"></<span class="hljs-name">script</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>
<p>如果你没有设置chunks选项，那么默认是全部显示</p>
</li>
<li>
<p>chunksSortMode</p>
</li>
</ul>
</li>
</ul>
<p>script的顺序，默认四个选项： <code>none</code> <code>auto</code> <code>dependency</code> <code>&#123;function&#125;</code></p>
<p>'dependency' 不用说，按照不同文件的依赖关系来排序。</p>
<p>这里重点讲解一下<code>function</code>的用法</p>
<p>如何配置出我们想要的顺序</p>
<pre><code class="hljs language-javascript copyable" lang="javascript">    <span class="hljs-keyword">new</span> HtmlWebpackPlugin(&#123;
        ...
        <span class="hljs-attr">chunksSortMode</span>: <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params">chunk1, chunk2</span>) </span>&#123;
            <span class="hljs-keyword">var</span> order = [<span class="hljs-string">'common'</span>, <span class="hljs-string">'public'</span>, <span class="hljs-string">'index'</span>];
            <span class="hljs-keyword">var</span> order1 = order.indexOf(chunk1.names[<span class="hljs-number">0</span>]);
            <span class="hljs-keyword">var</span> order2 = order.indexOf(chunk2.names[<span class="hljs-number">0</span>]);
            <span class="hljs-keyword">return</span> order1 - order2;  
        &#125;
    &#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>以上配置的顺序就是['common', 'public', 'index']，为什么呢，因为chunksSortMode这个函数就是数组的sort方法里的自定义函数，这里说白了就是数组[0， 1， 2]按升序排列。</p>
<p>接下来还有webpack.dev.js和webpack.prod.js两个文件（有点写不下去了，这篇文章查了n多资料，搞得现在脑袋有点昏啊）</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/d7f934f0a2db4b4ca236cd44bf0f9837~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>我就快速写重点内容了，不贴代码了</p>
<ul>
<li>
<p>webpack.dev.js里面的重点是devServer属性的配置</p>
</li>
<li>
<p>devServer配置详解：</p>
</li>
</ul>
<pre><code class="hljs language-javascript copyable" lang="javascript">devServer: &#123;
    <span class="hljs-comment">// 提供静态文件目录地址</span>
    <span class="hljs-comment">// 基于express.static实现, 所以这里你如果不请求静态文件，这个属性没啥用</span>
    <span class="hljs-attr">contentBase</span>: path.join(__dirname, <span class="hljs-string">'dist'</span>),
    <span class="hljs-comment">// 任意的 404 响应都被替代为 index.html</span>
    <span class="hljs-comment">// 基于node connect-history-api-fallback包实现</span>
    <span class="hljs-comment">// 我们知道vue和react有hash路由和history路由</span>
    <span class="hljs-comment">// history路由需要设置这个参数为true，要不你刷新页面会空白屏</span>
    <span class="hljs-attr">historyApiFallback</span>: <span class="hljs-literal">true</span>,
    <span class="hljs-comment">// 是否一切服务都启用 gzip 压缩</span>
    <span class="hljs-comment">// 基于node compression包实现</span>
    <span class="hljs-attr">compress</span>: <span class="hljs-literal">true</span>,
    <span class="hljs-comment">// 是否隐藏bundle信息</span>
    <span class="hljs-attr">noInfo</span>: <span class="hljs-literal">true</span>,
    <span class="hljs-comment">// 发生错误是否覆盖在页面上</span>
    <span class="hljs-attr">overlay</span>: <span class="hljs-literal">true</span>,
    <span class="hljs-comment">// 是否开启热加载</span>
    <span class="hljs-comment">// 必须搭配webpack.HotModuleReplacementPlugin 才能完全启用 HMR。</span>
    <span class="hljs-comment">// 如果 webpack 或 webpack-dev-server 是通过 --hot 选项启动的，那么这个插件会被自动添加</span>
    <span class="hljs-attr">hot</span>: <span class="hljs-literal">true</span>,
    <span class="hljs-comment">// 热加载模式</span>
    <span class="hljs-comment">// true代表inline模式，false代表iframe模式</span>
    <span class="hljs-attr">inline</span>: <span class="hljs-literal">true</span>, <span class="hljs-comment">// 默认是true</span>
    <span class="hljs-comment">// 是否自动打开</span>
    <span class="hljs-attr">open</span>: <span class="hljs-literal">true</span>,
    <span class="hljs-comment">// 设置本地url和端口号</span>
    <span class="hljs-attr">host</span>: <span class="hljs-string">'localhost'</span>,
    <span class="hljs-attr">port</span>: <span class="hljs-number">8080</span>,
    <span class="hljs-comment">// 代理</span>
    <span class="hljs-comment">// 基于node http-proxy-middleware包实现</span>
    <span class="hljs-attr">proxy</span>: &#123;
        <span class="hljs-comment">// 匹配api前缀时，则代理到3001端口</span>
        <span class="hljs-comment">// 即http://localhost:8080/api/123 = http://localhost:3001/api/123</span>
        <span class="hljs-comment">// 注意:这里是把当前server8080代理到3001，而不是任意端口的api代理到3001</span>
        <span class="hljs-string">'/api'</span>: <span class="hljs-string">'http://localhost:3001'</span>,
        <span class="hljs-comment">// 设置为true, 本地就会虚拟一个服务器接收你的请求并代你发送该请求</span>
        <span class="hljs-comment">// 主要解决跨域问题</span>
        <span class="hljs-attr">changeOrigin</span>: <span class="hljs-literal">true</span>,
        <span class="hljs-comment">// 针对代理https</span>
        <span class="hljs-attr">secure</span>: <span class="hljs-literal">false</span>,
        <span class="hljs-comment">// 覆写路径：http://localhost:8080/api/123 = http://localhost:3001/123</span>
        <span class="hljs-attr">pathRewrite</span>: &#123;<span class="hljs-string">'^/api'</span> : <span class="hljs-string">''</span>&#125;
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>webpack.prod.js的重点是配置TerserPlugin，和optimization配置其中splitChunks是重点中的重点）</li>
</ul>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">// 这个插件最开始讲了，一下的插件就略过都讲过了</span>
<span class="hljs-keyword">const</span> &#123; merge &#125; = <span class="hljs-built_in">require</span>(<span class="hljs-string">'webpack-merge'</span>);
<span class="hljs-keyword">const</span> MiniCssExtractPlugin = <span class="hljs-built_in">require</span>(<span class="hljs-string">'mini-css-extract-plugin'</span>);
<span class="hljs-keyword">const</span> CssMinimizerPlugin = <span class="hljs-built_in">require</span>(<span class="hljs-string">'css-minimizer-webpack-plugin'</span>);
<span class="hljs-keyword">const</span> TerserPlugin = <span class="hljs-built_in">require</span>(<span class="hljs-string">'terser-webpack-plugin'</span>);
<span class="hljs-keyword">const</span> &#123; CleanWebpackPlugin &#125; = <span class="hljs-built_in">require</span>(<span class="hljs-string">'clean-webpack-plugin'</span>);
<span class="hljs-keyword">const</span> &#123; BundleAnalyzerPlugin &#125; = <span class="hljs-built_in">require</span>(<span class="hljs-string">'webpack-bundle-analyzer'</span>);
<span class="hljs-keyword">const</span> common = <span class="hljs-built_in">require</span>(<span class="hljs-string">'./webpack.common.js'</span>);
<span class="hljs-keyword">const</span> paths = <span class="hljs-built_in">require</span>(<span class="hljs-string">'../paths'</span>);
<span class="hljs-keyword">const</span> &#123; shouldOpenAnalyzer, ANALYZER_HOST, ANALYZER_PORT &#125; = <span class="hljs-built_in">require</span>(<span class="hljs-string">'../conf'</span>);

<span class="hljs-built_in">module</span>.exports = merge(common, &#123;
  <span class="hljs-attr">mode</span>: <span class="hljs-string">'production'</span>, 这个需要细讲，下面说
  <span class="hljs-attr">output</span>: &#123;
    <span class="hljs-attr">filename</span>: <span class="hljs-string">'js/[name].[contenthash:8].js'</span>,
    <span class="hljs-attr">path</span>: paths.appBuild,
    <span class="hljs-attr">assetModuleFilename</span>: <span class="hljs-string">'images/[name].[contenthash:8].[ext]'</span>,
  &#125;,
  <span class="hljs-attr">plugins</span>: [
     <span class="hljs-comment">// 打包后会有dist（或者build，名字在output里设置）目录</span>
     <span class="hljs-comment">// 再次打包时需要把之前的dist删掉后，再次生成dist</span>
     <span class="hljs-comment">// 这个插件就是其删掉作用的</span>
    <span class="hljs-keyword">new</span> CleanWebpackPlugin(),
    <span class="hljs-comment">// 提取css的插件</span>
    <span class="hljs-keyword">new</span> MiniCssExtractPlugin(&#123;
      <span class="hljs-attr">filename</span>: <span class="hljs-string">'css/[name].[contenthash:8].css'</span>,
      <span class="hljs-attr">chunkFilename</span>: <span class="hljs-string">'css/[name].[contenthash:8].chunk.css'</span>,
    &#125;),
    <span class="hljs-comment">// 开启分析工具的插件，分析包的体积</span>
    shouldOpenAnalyzer &&
      <span class="hljs-keyword">new</span> BundleAnalyzerPlugin(&#123;
        <span class="hljs-attr">analyzerMode</span>: <span class="hljs-string">'server'</span>,
        <span class="hljs-attr">analyzerHost</span>: ANALYZER_HOST,
        <span class="hljs-attr">analyzerPort</span>: ANALYZER_PORT,
      &#125;),
  ].filter(<span class="hljs-built_in">Boolean</span>),
  <span class="hljs-comment">// 这个重点下面讲</span>
  <span class="hljs-attr">optimization</span>: &#123;
    <span class="hljs-attr">concatenateModules</span>: <span class="hljs-literal">false</span>,
    <span class="hljs-attr">minimize</span>: <span class="hljs-literal">true</span>,
    <span class="hljs-attr">minimizer</span>: [
      <span class="hljs-comment">// new TerserPlugin(&#123; // 这个常用配置后面下面讲</span>
      <span class="hljs-comment">//   extractComments: false,</span>
      <span class="hljs-comment">//   terserOptions: &#123;</span>
      <span class="hljs-comment">//     compress: &#123; pure_funcs: ['console.log'] &#125;,</span>
      <span class="hljs-comment">//   &#125;,</span>
      <span class="hljs-comment">// &#125;),</span>
      <span class="hljs-keyword">new</span> CssMinimizerPlugin(), <span class="hljs-comment">// css压缩插件</span>
    ],
    <span class="hljs-attr">splitChunks</span>: &#123; <span class="hljs-comment">// 这个是重点下面讲</span>
      <span class="hljs-attr">chunks</span>: <span class="hljs-string">'all'</span>,
      <span class="hljs-attr">minSize</span>: <span class="hljs-number">0</span>,
    &#125;,
  &#125;,
&#125;);

<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>
<p>TerserPlugin</p>
<ul>
<li>test</li>
</ul>
<p>默认值：<code>/.m?js(?.*)?$/i</code>, 用来匹配需要压缩的文件。</p>
<ul>
<li>include</li>
</ul>
<p>默认值： <code>undefined</code>, 匹配参与压缩的文件</p>
<ul>
<li>exclude</li>
</ul>
<p>默认值： <code>undefined</code>, 匹配参与压缩的文件</p>
<ul>
<li><code>parallel</code></li>
</ul>
<p>类型： <code>Boolean|Number</code> 默认值： <code>true</code></p>
<p>这个参数很重要，启用多进程构建，可以大大提高打包速度，强烈建议开启</p>
<pre><code class="hljs language-javascript copyable" lang="javascript">  terserOptions: &#123;
      <span class="hljs-attr">format</span>: &#123;
        <span class="hljs-comment">// 删除所有的注释</span>
        <span class="hljs-attr">comments</span>: <span class="hljs-literal">true</span>,
      &#125;
      <span class="hljs-attr">compress</span>: &#123;
          <span class="hljs-comment">// 删除未引用的函数和变量</span>
          <span class="hljs-attr">unused</span>: <span class="hljs-literal">true</span>,
          <span class="hljs-comment">// 删掉 debugger</span>
          <span class="hljs-attr">drop_debugger</span>: <span class="hljs-literal">true</span>, 
          <span class="hljs-comment">// 移除 console</span>
          <span class="hljs-attr">drop_console</span>: <span class="hljs-literal">true</span>, 
          <span class="hljs-comment">// 删除无法访问的代码</span>
          <span class="hljs-attr">dead_code</span>: <span class="hljs-literal">true</span>,
          <span class="hljs-attr">unsafe_undefined</span>: <span class="hljs-literal">true</span>,
        &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
<li>
<p>mode</p>
</li>
</ul>
<p>mode有三个参数<code>production</code>，<code>development</code>，<code>none</code>，前两个参数会默认安装一堆插件，用来区分是开发环境还是生产环境。而<code>none</code>的话，webpack就是最初的样子，无任何预设，需要从无到有开始配置。</p>
<p>所以我们了解是哪些插件，有啥用是理解webpack进化到现在的比较重要的知识点。</p>
<h2 data-id="heading-43">development模式下，webpack做了那些打包工作</h2>
<p>在此mode下，就做了以下插件的事（还有其它配置，重点介绍下面的），其他都没做，所以这些插件可以省略,webpack默认就给你加上了，而且会将 <code>DefinePlugin</code> 中 <code>process.env.NODE_ENV</code> 的值设置为 <code>development</code></p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">// webpack.development.config.js</span>
<span class="hljs-built_in">module</span>.exports = &#123;
+ mode: <span class="hljs-string">'development'</span>
- devtool: <span class="hljs-string">'eval'</span>,
 <span class="hljs-attr">optimization</span>: &#123;
    <span class="hljs-attr">moduleIds</span>: <span class="hljs-string">'named'</span>,
    <span class="hljs-attr">chunkIds</span>: <span class="hljs-string">'named'</span>
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>我们看看<code>moduleIds</code>和<code>chunkIds</code>这两个配置都做了啥，简而言之，就是帮助缓存生效的插件。</p>
<p>我们知道webpack最开始的版本并不会给模块加上名字，模块名都是数字，<code>0，1，2，3</code>，但是对于我们人来说数字不好认，要是名字多好，便于开发的时候查找。</p>
<p>而且，你想想，如果我们在<code>0</code>和<code>1</code>模块之间，再加一个模块，那么顺序就是<code>0</code>、新模块（现在是<code>1</code>）、老的1模块（现在是<code>2</code>），老的<code>2</code>模块（现在是<code>3</code>），这时候新模块就是<code>1</code>，其它老模块数字依次<code>+1</code>，这个时候缓存就失效了，虽然老的模块代码没变，但是这种缓存下标的方式，让缓存很容易失效，这就是为啥加上这个配置的原因</p>
<p>有了<code>moduleIds</code>，模块都拥有了姓名，而且都是独一无二的key，不管新增减多少模块，模块的key都是固定的。</p>
<p>除了<code>moduleIds</code>，还有一个<code>chunkIds</code>，这个是给配置的每个chunks命名，原本的chunks也是数组，没有姓名。</p>
<h2 data-id="heading-44">production</h2>
<p>在正式版本中，所省略的插件们，如下所示，我们会一个个分析。</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">// webpack.production.config.js</span>
<span class="hljs-built_in">module</span>.exports = &#123;
  + mode: <span class="hljs-string">'production'</span>
  - plugins: [
  -   <span class="hljs-keyword">new</span> webpack.DefinePlugin(&#123; <span class="hljs-string">"process.env.NODE_ENV"</span>: <span class="hljs-string">'"production"'</span> &#125;),
  -   <span class="hljs-keyword">new</span> webpack.optimize.ModuleConcatenationPlugin(),
  -   <span class="hljs-keyword">new</span> webpack.NoEmitOnErrorsPlugin(),
  -   <span class="hljs-keyword">new</span> TerserPlugin(<span class="hljs-comment">/* ... */</span>),
  - ]
  &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-45">terser-webpack-plugin</h3>
<p>用于js代码压缩。在以前版本中，我们需要引入npm包<code>terser-webpack-plugin</code>来进行压缩，现在我们可以在<code>optimize</code>中进行配置达到同样的效果</p>
<p>配置之前已讲</p>
<h3 data-id="heading-46">ModuleConcatenationPlugin</h3>
<p>这个是用来帮助作用域提升的，我们之前看了webpack打包出来的是类似</p>
<pre><code class="hljs language-javascript copyable" lang="javascript">&#123;
   文件路径<span class="hljs-number">1</span>：<span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params"></span>)<span class="hljs-title">xx</span>,
   文件路径2：<span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params"></span>)<span class="hljs-title">xx</span>,
   文件路径3：<span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params"></span>)<span class="hljs-title">xx</span>,
&#125;
</span></span></span><span class="copy-code-btn">复制代码</span></code></pre>
<p>这样每个模块都在自己的function里面，都有自己的作用域，我们知道作用域链访问是有性能代价的，如果大家都提到一个作用域，对性能提升是有帮助的，这个插件就做这样的事。</p>
<h3 data-id="heading-47">NoEmitOnErrorsPlugin</h3>
<p>这个就是用于防止程序报错，就算有错误也给我继续编译。</p>
<h3 data-id="heading-48">others</h3>
<p>还有一些默认的插件配置，也就是可以不在plugins中引用的配置：</p>
<h3 data-id="heading-49">SideEffectsFlagPlugin</h3>
<p><code>webpack.optimization.sideEffects</code>用于实现<code>treeshaking</code>形式的死码删除。而为了实现<code>treeshaking</code>，需要满足几个条件:</p>
<ul>
<li>导入的模块已经标记了sideEffect，即package.json中的sideEffects这个属性为false。</li>
<li>当前模块引用了无副作用的模块，且没有被使用</li>
</ul>
<p>这样，经过<code>SideEffectsFlagPlugin</code>处理后，没有副作用且没有被使用的模块都会被打上<code>sideEffectFree</code>标记。 在<code>ModuleConcatenationPlugin</code>中，带着<code>sideEffectFree</code>标记的模块将不会被打包。</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">// webpack.pord.config.js</span>
<span class="hljs-built_in">module</span>.exports = &#123;
  <span class="hljs-attr">optimization</span>: &#123;
    <span class="hljs-attr">sideEffects</span>: <span class="hljs-literal">true</span>
  &#125;
&#125;;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-50">FlagIncludedChunksPlugin</h3>
<p>即配置<code>optimization.flagIncludedChunks</code>。该配置项会使webpack确认，若当前标记的<code>chunk</code>a是另外一个<code>chunk</code>A的子集并且已经A加载完成，则a将不会再次加载（包含关系）。</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">// webpack.pord.config.js</span>
<span class="hljs-built_in">module</span>.exports = &#123;
  <span class="hljs-attr">optimization</span>: &#123;
    <span class="hljs-attr">flagIncludedChunks</span>: <span class="hljs-literal">true</span>
  &#125;
&#125;;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-51">FlagDependencyUsagePlugin</h3>
<p>标记没有用到的依赖。</p>
<h2 data-id="heading-52">splitChunks</h2>
<p>最后1个知识点来了哦！</p>
<p>这个配置对象中，其它都好说，最令人困惑的是chunks属性，我们来看看是个什么东西。</p>
<ul>
<li><code>chunks</code>选项，决定要提取那些模块。
<ul>
<li>
<p>默认是<code>async</code>：只提取异步加载的模块出来打包到一个文件中。</p>
<ul>
<li>异步加载的模块：通过<code>import('xxx')</code>或<code>require(['xxx'],() =>&#123;&#125;)</code>加载的模块。</li>
</ul>
</li>
<li>
<p><code>initial</code>：提取同步加载和异步加载模块，如果xxx在项目中异步加载了，也同步加载了，那么xxx这个模块会被提取两次，分别打包到不同的文件中。</p>
<ul>
<li>同步加载的模块：通过 <code>import xxx</code>或<code>require('xxx')</code>加载的模块。</li>
</ul>
</li>
<li>
<p><code>all</code>：不管异步加载还是同步加载的模块都提取出来，打包到一个文件中。</p>
</li>
</ul>
</li>
</ul>
<p>兄弟们，但是我遇到了问题，就是上面说的这些根本不管用，下面的案例摘自<code>stockOverFolw</code>的高票回答，但是我用<code>webpack5</code>同样的配置，根本得不到跟这个回答一致的答案，百思不得其解，后面我改进了一下，就可以了，后面再介绍，大家先看案例</p>
<p>app.js 如下，有一个静态模块导入叫<code>my-static-module</code>，还有一个动态模块导入叫<code>my-dynamic-module</code></p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">//app.js</span>
<span class="hljs-keyword">import</span> <span class="hljs-string">"my-static-module"</span>;

<span class="hljs-keyword">if</span>(some_condition_is_true)&#123;
  <span class="hljs-keyword">import</span> (<span class="hljs-string">"my-dynamic-module"</span>)
&#125;
<span class="hljs-built_in">console</span>.log(<span class="hljs-string">"My app is running"</span>)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>``</p>
<p>来看看chunks参数不一样，得到的结果会是多么不一样(配置如下)</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-built_in">module</span>.exports = &#123;
  <span class="hljs-attr">optimization</span>: &#123;
    <span class="hljs-attr">chunks</span>: <span class="hljs-keyword">async</span> | initial | all
  &#125;
&#125;;
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>async (default)</li>
</ul>
<p>会生成以下两个文件</p>
<ol>
<li><code>bundle.js</code> (包括 app.js + my-static-module)</li>
<li><code>chunk.js</code> (仅仅包括 my-dynamic-module)</li>
</ol>
<ul>
<li>initial</li>
</ul>
<p>会生成以下两个文件</p>
<ol>
<li><code>app.js</code> (仅仅包括 app.js)</li>
<li><code>bundle.js</code> (仅仅包括 my-static-module)</li>
<li><code>chunk.js</code> (仅仅包括 my-dynamic-module)</li>
</ol>
<ul>
<li>all</li>
</ul>
<p>会生成以下两个文件</p>
<ol>
<li><code>app.js</code> (仅仅包括 app.js only)</li>
<li><code>bundle.js</code> (仅仅包括 my-static-module + my-dynamic-module)</li>
</ol>
<p>可以看出，<code>all</code>是比较极限的压缩</p>
<p>我无论怎么尝试，得出来的结果都是默认的<code>async</code>导出的结果，可能是我配错了吧，希望有熟悉这项配置的大哥评论区留个言。</p>
<p>我后来是怎么改，就可以符合上面的答案了呢，我把chunks配置在<code>cacheGroups</code>参数里，如下:</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-built_in">module</span>.exports = &#123;
   <span class="hljs-attr">splitChunks</span>: &#123;
      <span class="hljs-attr">cacheGroups</span>: &#123;
        <span class="hljs-attr">common</span>: &#123;
          <span class="hljs-attr">chunks</span>: <span class="hljs-string">'async'</span> | <span class="hljs-string">'all'</span> | <span class="hljs-string">'initial'</span>,
          <span class="hljs-attr">minSize</span>: <span class="hljs-number">0</span>,
          <span class="hljs-attr">minChunks</span>: <span class="hljs-number">1</span>,
        &#125;,
      &#125;,
    &#125;,
&#125;;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这里顺便介绍一下minChunks是什么意思，意思是至少引用多少次才分离公共代码，我这里是1次，只要引用过模块都分离出去。</p>
<p><code>minSize</code>是规定被提取的模块在压缩前的大小最小值，单位为字节，默认为30000，只有超过了30000字节才会被提取，我们这里设置为0，是为了自己做实验，保证能被分离就分离出去。</p>
<p>接下来，介绍一下其他参数：</p>
<ul>
<li><code>maxSize</code>选项：把提取出来的模块打包生成的文件大小不能超过maxSize值，如果超过了，要对其进行分割并打包生成新的文件。单位为字节，默认为0，表示不限制大小。</li>
<li><code>maxAsyncRequests</code>选项：最大的按需(异步)加载次数，默认为 6。</li>
<li><code>maxInitialRequests</code>选项：打包后的入口文件加载时，还能同时加载js文件的数量（包括入口文件），默认为4。</li>
<li>先说一下优先级 <code>maxInitialRequests</code> / <code>maxAsyncRequests</code> <<code>maxSize</code><<code>minSize</code>。</li>
<li><code>automaticNameDelimiter</code>选项：打包生成的js文件名的分割符，默认为<code>~</code>。</li>
<li><code>name</code>选项：打包生成js文件的名称。</li>
<li><code>cacheGroups</code>选项，核心重点，<strong>配置提取模块的方案</strong>。里面每一项代表一个提取模块的方案。下面是<code>cacheGroups</code>每项中特有的选项，其余选项和外面一致，若<code>cacheGroups</code>每项中有，就按配置的，没有就使用外面配置的。</li>
<li>
<ul>
<li><code>test</code>选项：用来匹配要提取的模块的资源路径或名称。值是正则或函数。</li>
<li><code>priority</code>选项：方案的优先级，值越大表示提取模块时优先采用此方案。默认值为0。</li>
<li><code>reuseExistingChunk</code>选项：<code>true</code>/<code>false</code>。为<code>true</code>时，如果当前要提取的模块，在已经在打包生成的<em>js</em>文件中存在，则将重用该模块，而不是把当前要提取的模块打包生成新的<em>js</em>文件。</li>
<li><code>enforce</code>选项：<code>true</code>/<code>false</code>。为<code>true</code>时，忽略<code>minSize</code>，<code>minChunks</code>，<code>maxAsyncRequests</code>和<code>maxInitialRequests</code>外面选项</li>
</ul>
</li>
</ul>
<p>能看到最后一定很不容易，欢迎点赞，后面会接着出文章，目前3篇正在写，也是自己最近学习完的知识</p>
<ul>
<li>form表单低代码平台之渲染器实现（渲染器就是schema => 表单）</li>
<li>jest单元测试教程</li>
<li>leetcode官方面试最常见150题之简单题</li>
</ul>
<p>参考：</p>
<p><a href="https://juejin.cn/post/6844903826630115335#heading-2" target="_blank" title="https://juejin.cn/post/6844903826630115335#heading-2">mini-css-extract-plugin插件快速入门</a></p>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fsegmentfault.com%2Fa%2F1190000019661168" target="_blank" rel="nofollow noopener noreferrer" title="https://segmentfault.com/a/1190000019661168" ref="nofollow noopener noreferrer">在Typescript项目中，如何优雅的使用ESLint和Prettier</a></p>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fzhuanlan.zhihu.com%2Fp%2F35913229" target="_blank" rel="nofollow noopener noreferrer" title="https://zhuanlan.zhihu.com/p/35913229" ref="nofollow noopener noreferrer">实用husky介绍</a></p>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fzhuanlan.zhihu.com%2Fp%2F180491533" target="_blank" rel="nofollow noopener noreferrer" title="https://zhuanlan.zhihu.com/p/180491533" ref="nofollow noopener noreferrer">我是这样搭建typescript+react</a></p>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fwebpack.docschina.org%2F" target="_blank" rel="nofollow noopener noreferrer" title="https://webpack.docschina.org/" ref="nofollow noopener noreferrer">webpack官网</a></p>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fblog.csdn.net%2Fyuse6262%2Farticle%2Fdetails%2F97824093" target="_blank" rel="nofollow noopener noreferrer" title="https://blog.csdn.net/yuse6262/article/details/97824093" ref="nofollow noopener noreferrer">webpack import和export</a></p>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fsegmentfault.com%2Fa%2F1190000021421461" target="_blank" rel="nofollow noopener noreferrer" title="https://segmentfault.com/a/1190000021421461" ref="nofollow noopener noreferrer">tsconfig常用配置</a></p>
<p><a href="https://juejin.cn/post/6844904022080667661#heading-51" target="_blank" title="https://juejin.cn/post/6844904022080667661#heading-51">前端工程化 - 剖析npm的包管理机制</a></p></div>  
</div>
            