
---
title: '【学习笔记📒】webpack_手写loader — 模板编译 tpl-loader'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=1608'
author: 掘金
comments: false
date: Tue, 04 May 2021 06:00:56 GMT
thumbnail: 'https://picsum.photos/400/300?random=1608'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.8;font-weight:400;font-size:16px;word-spacing:2px;letter-spacing:2px;overflow-x:hidden;color:#3e3e3e;background-image:linear-gradient(90deg,rgba(50,0,0,.05) 3%,transparent 0),linear-gradient(1turn,rgba(50,0,0,.05) 3%,transparent 0);background-size:20px 20px;background-position:50%&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:1.2em;border-bottom:2px solid #ef7060;word-spacing:0!important;letter-spacing:0!important;font-size:inherit;line-height:inherit;display:block;font-weight:400;background:#ef7060;color:#fff;padding:10px;border-top-right-radius:3px;border-top-left-radius:3px;margin-right:3px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h1 data-id="heading-0">Webpack 基础知识点</h1>
<h2 data-id="heading-1">Webpack 三大件</h2>
<pre><code class="hljs language-json copyable" lang="json"><span class="hljs-string">"devDependencies"</span>: &#123;
  <span class="hljs-attr">"webpack"</span>: <span class="hljs-string">"^4.30.0"</span>,
  <span class="hljs-attr">"webpack-cli"</span>: <span class="hljs-string">"^3.3.0"</span>,
  <span class="hljs-attr">"webpack-dev-server"</span>: <span class="hljs-string">"^3.7.2"</span>
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-2">核心概念</h2>
<ul>
<li>mode</li>
<li>entry</li>
<li>output</li>
<li>loader</li>
<li>plugin</li>
<li>devServer</li>
</ul>
<h2 data-id="heading-3">Loader</h2>
<h3 data-id="heading-4">什么是Loader</h3>
<ul>
<li>loader 用于对模块的源代码进行转换：<strong>把源模块转换成通用模块</strong>。</li>
<li>loader 让 webpack 能够去<strong>处理那些非 JavaScript 文件</strong>（<strong>webpack 自身只理解 JavaScript</strong>）。loader 可以将所有类型的文件转换为 webpack 能够处理的有效模块，然后你就可以利用 webpack 的打包能力，对它们进行处理。</li>
</ul>
<blockquote>
<p>注意，loader 能够 <code>import</code> 导入<strong>任何类型的模块</strong>（例如 <code>.css</code> 文件），这是 webpack 特有的功能，其他打包程序或任务执行器的可能并不支持。我们认为这种语言扩展是有很必要的，因为这可以使开发人员创建出更准确的依赖关系图。</p>
</blockquote>
<ul>
<li>webpack loader的顺序是 <code>从下到上</code>，<code>从右到左</code>。</li>
</ul>
<p>当<strong>链式调用</strong>多个 loader 的时候，请记住它们会以<code>相反的顺序</code>执行。取决于<strong>数组写法格式</strong>，<code>从右向左</code>或者<code>从下向上</code>执行。</p>
<h3 data-id="heading-5">在 webpack.config.js 中的配置</h3>
<p>在更高层面，在 <code>webpack</code> 的配置中 <code>loader</code> 有两个目标：</p>
<ol>
<li><code>test</code> 属性，用于标识出应该被对应的 loader 进行转换的<strong>某个或某些文件</strong>。</li>
<li><code>use</code> 属性，表示进行转换时，应该使用哪个 loader。</li>
</ol>
<p>webpack.config.js:</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> path = <span class="hljs-built_in">require</span>(<span class="hljs-string">'path'</span>);

<span class="hljs-keyword">const</span> config = &#123;
  <span class="hljs-attr">output</span>: &#123;
    <span class="hljs-attr">filename</span>: <span class="hljs-string">'my-first-webpack.bundle.js'</span>
  &#125;,
  <span class="hljs-attr">module</span>: &#123;
    <span class="hljs-attr">rules</span>: [
      &#123; <span class="hljs-attr">test</span>: <span class="hljs-regexp">/\.txt$/</span>, use: <span class="hljs-string">'raw-loader'</span> &#125;
    ]
  &#125;
&#125;;

<span class="hljs-built_in">module</span>.exports = config;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>以上配置中，对一个<strong>单独的 module 对象</strong>定义了 <code>rules</code> 属性，里面包含两个<strong>必须属性</strong>：<code>test</code> 和 <code>use</code>。这告诉 webpack 编译器(compiler) 如下信息：</p>
<blockquote>
<p>“嘿，webpack 编译器，当你碰到「在 require()/import 语句中被解析为 '.txt' 的路径」时，在你对它打包之前，先使用 raw-loader 转换一下。”</p>
</blockquote>
<h3 data-id="heading-6">简单用法</h3>
<h5 data-id="heading-7">🌟🌟 只能传入一个参数</h5>
<p>当一个 loader 在资源中使用，这个 loader 只能传入<code>一个参数</code> - 这个参数是一个<strong>包含资源文件内容的</strong><code>字符串</code>。</p>
<h5 data-id="heading-8">🌟🌟 返回值</h5>
<p><strong>同步</strong> loader 可以简单的返回<strong>一个代表模块转化后的值</strong>。<br><br>
在更复杂的情况下，loader 也可以通过使用 <code>this.callback(err, values...)</code> 函数，返回<strong>任意数量的值</strong>。错误要么传递给这个 this.callback 函数，要么扔进同步 loader 中。<br><br>
🌟🌟 loader 会返回<strong>一个或者两个值</strong>。第一个值的类型是 <code>JavaScript 代码的字符串</code>或者 <code>buffer</code>。第二个参数值是 SourceMap，它是个 JavaScript 对象。</p>
<h3 data-id="heading-9">复杂用法</h3>
<p>当<code>链式调用</code>多个 loader 的时候，请记住它们会以<code>相反的顺序</code>执行。取决于<strong>数组写法格式</strong>，<code>从右向左</code>或者<code>从下向上</code>执行。</p>
<ul>
<li>最后的 loader 最早调用，将会传入原始资源内容。</li>
<li>第一个 loader 最后调用，期望值是传出 JavaScript 和 source map（可选）。</li>
<li>中间的 loader 执行时，会传入前一个 loader 传出的结果。</li>
</ul>
<p>所以，在接下来的例子，foo-loader 被传入原始资源，bar-loader 将接收 foo-loader 的产出，返回最终转化后的模块和一个 source map（可选）
<br><br>
webpack.config.js</p>
<pre><code class="hljs language-js copyable" lang="js">&#123;
  <span class="hljs-attr">test</span>: <span class="hljs-regexp">/\.js/</span>,
  use: [
    <span class="hljs-string">'bar-loader'</span>,
    <span class="hljs-string">'foo-loader'</span>
  ]
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-10">用法准则</h3>
<p>编写 loader 时应该遵循以下准则。它们<strong>按重要程度排序</strong>，有些仅适用于某些场景。</p>
<ul>
<li>简单易用</li>
</ul>
<blockquote>
<p>每个 loader 只做单一任务。</p>
</blockquote>
<ul>
<li>使用链式传递。</li>
</ul>
<blockquote>
<p>loader 可以被链式调用意味着不一定要输出 JavaScript。只要<strong>下一个 loader 可以处理这个输出</strong>，这个 loader 就可以返回任意类型的模块。</p>
</blockquote>
<ul>
<li>模块化的输出。</li>
</ul>
<blockquote>
<p>保证输出模块化。loader 生成的模块与普通模块遵循相同的设计原则。</p>
</blockquote>
<ul>
<li>
<p>确保无状态。</p>
</li>
<li>
<p>使用 loader utilities。</p>
</li>
</ul>
<blockquote>
<p>充分利用 <a href="https://github.com/webpack/loader-utils" target="_blank" rel="nofollow noopener noreferrer">loader-utils</a> 包。它提供了许多有用的工具，但最常用的一种工具是<strong>获取传递给 loader 的选项</strong>。<a href="https://github.com/webpack/schema-utils" target="_blank" rel="nofollow noopener noreferrer">schema-utils</a> 包配合 loader-utils，用于保证 loader 选项，进行与 JSON Schema 结构一致的<strong>校验</strong>。</p>
</blockquote>
<p>loader.js</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">import</span> &#123; getOptions &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'loader-utils'</span>;
<span class="hljs-keyword">import</span> validateOptions <span class="hljs-keyword">from</span> <span class="hljs-string">'schema-utils'</span>;

<span class="hljs-keyword">const</span> schema = &#123;
  <span class="hljs-attr">type</span>: <span class="hljs-string">'object'</span>,
  <span class="hljs-attr">properties</span>: &#123;
    <span class="hljs-attr">test</span>: &#123;
      <span class="hljs-attr">type</span>: <span class="hljs-string">'string'</span>
    &#125;
  &#125;
&#125;

<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">source</span>) </span>&#123;
  <span class="hljs-keyword">const</span> options = getOptions(<span class="hljs-built_in">this</span>);

  validateOptions(schema, options, <span class="hljs-string">'Example Loader'</span>);

  <span class="hljs-comment">// 对资源应用一些转换……</span>

  <span class="hljs-keyword">return</span> <span class="hljs-string">`export default <span class="hljs-subst">$&#123; <span class="hljs-built_in">JSON</span>.stringify(source) &#125;</span>`</span>;
&#125;;
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>
<p>记录 loader 的依赖。</p>
</li>
<li>
<p>解析模块依赖关系。</p>
</li>
<li>
<p>提取通用代码。</p>
</li>
</ul>
<blockquote>
<p>不要在模块代码中插入绝对路径，因为当项目根路径变化时，文件绝对路径也会变化。loader-utils 中的 <a href="https://github.com/webpack/loader-utils#stringifyrequest" target="_blank" rel="nofollow noopener noreferrer">stringifyRequest</a> 方法，可以将绝对路径转化为相对路径。</p>
</blockquote>
<ul>
<li>避免绝对路径。</li>
<li>使用 peer dependencies。</li>
</ul>
<h1 data-id="heading-11">手写 模板编译 tpl-loader</h1>
<h3 data-id="heading-12">package.json</h3>
<p>按照这里的版本安装依赖，否则会因为版本问题报错。</p>
<pre><code class="hljs language-json copyable" lang="json">&#123;
  <span class="hljs-attr">"name"</span>: <span class="hljs-string">"tpl-loader-creator"</span>,
  <span class="hljs-attr">"version"</span>: <span class="hljs-string">"1.0.0"</span>,
  <span class="hljs-attr">"description"</span>: <span class="hljs-string">""</span>,
  <span class="hljs-attr">"main"</span>: <span class="hljs-string">"index.js"</span>,
  <span class="hljs-attr">"scripts"</span>: &#123;
    <span class="hljs-attr">"dev"</span>: <span class="hljs-string">"webpack-dev-server"</span>
  &#125;,
  <span class="hljs-attr">"keywords"</span>: [],
  <span class="hljs-attr">"author"</span>: <span class="hljs-string">""</span>,
  <span class="hljs-attr">"license"</span>: <span class="hljs-string">"ISC"</span>,
  <span class="hljs-attr">"devDependencies"</span>: &#123;
    <span class="hljs-attr">"@babel/core"</span>: <span class="hljs-string">"^7.14.0"</span>,
    <span class="hljs-attr">"babel-loader"</span>: <span class="hljs-string">"^8.2.2"</span>,
    <span class="hljs-attr">"html-webpack-plugin"</span>: <span class="hljs-string">"^4.5.0"</span>,
    <span class="hljs-attr">"webpack"</span>: <span class="hljs-string">"^4.30.0"</span>,
    <span class="hljs-attr">"webpack-cli"</span>: <span class="hljs-string">"^3.3.0"</span>,
    <span class="hljs-attr">"webpack-dev-server"</span>: <span class="hljs-string">"^3.7.2"</span>
  &#125;
&#125;

<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-13">webpack.config.js</h3>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> &#123; resolve &#125; = <span class="hljs-built_in">require</span>(<span class="hljs-string">'path'</span>)
<span class="hljs-keyword">const</span> HtmlWebpackPlugin = <span class="hljs-built_in">require</span>(<span class="hljs-string">'html-webpack-plugin'</span>) <span class="hljs-comment">// 是一个构造函数</span>

<span class="hljs-built_in">module</span>.exports = &#123;
  <span class="hljs-attr">mode</span>: <span class="hljs-string">'development'</span>,
  <span class="hljs-attr">entry</span>: resolve(__dirname, <span class="hljs-string">'src/app.js'</span>),
  <span class="hljs-attr">output</span>: &#123;
    <span class="hljs-attr">path</span>: resolve(__dirname, <span class="hljs-string">'build'</span>),
    <span class="hljs-attr">filename</span>: <span class="hljs-string">'app.js'</span>
  &#125;,
  <span class="hljs-attr">devtool</span>: <span class="hljs-string">'source-map'</span>,
  <span class="hljs-attr">module</span>: &#123;
    <span class="hljs-attr">rules</span>: [
      <span class="hljs-comment">// 模块规则（配置 loader、解析器等选项）</span>

      &#123;
        <span class="hljs-attr">test</span>: <span class="hljs-regexp">/\.tpl$/</span>,
        <span class="hljs-comment">// 这里是匹配条件，每个选项都接收一个正则表达式或字符串</span>
        <span class="hljs-comment">// test 和 include 具有相同的作用，都是必须匹配选项</span>
        <span class="hljs-comment">// exclude 是必不匹配选项（优先于 test 和 include）</span>
        <span class="hljs-comment">// 最佳实践：</span>
        <span class="hljs-comment">// - 只在 test 和 文件名匹配 中使用正则表达式</span>
        <span class="hljs-comment">// - 在 include 和 exclude 中使用绝对路径数组</span>
        <span class="hljs-comment">// - 尽量避免 exclude，更倾向于使用 include</span>
        use: [
          <span class="hljs-comment">// 应用多个 loader 和选项</span>
          <span class="hljs-comment">// loader的顺序是 `从下到上`，`从右到左`。</span>
          <span class="hljs-string">'babel-loader'</span>,
          &#123;
            <span class="hljs-attr">loader</span>: <span class="hljs-string">'./loaders/tpl-loader'</span>,
            <span class="hljs-attr">options</span>: &#123;
              <span class="hljs-attr">log</span>: <span class="hljs-literal">true</span>
            &#125;
          &#125;
        ]
      &#125;
    ]
  &#125;,
  <span class="hljs-attr">plugins</span>: [
    <span class="hljs-keyword">new</span> HtmlWebpackPlugin(&#123;
      <span class="hljs-attr">template</span>: resolve(__dirname, <span class="hljs-string">'index.html'</span>)
    &#125;)
  ],
  <span class="hljs-attr">devServer</span>: &#123;
    <span class="hljs-attr">port</span>: <span class="hljs-string">'3333'</span>
  &#125;
&#125;

<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-14">info.tpl</h3>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">div</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">h1</span>></span>&#123;&#123; name &#125;&#125;<span class="hljs-tag"></<span class="hljs-name">h1</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">p</span>></span>&#123;&#123; age &#125;&#125;<span class="hljs-tag"></<span class="hljs-name">p</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">p</span>></span>&#123;&#123; career &#125;&#125;<span class="hljs-tag"></<span class="hljs-name">p</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">p</span>></span>&#123;&#123; hobby &#125;&#125;<span class="hljs-tag"></<span class="hljs-name">p</span>></span>
<span class="hljs-tag"></<span class="hljs-name">div</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-15">app.js</h3>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">import</span> tpl <span class="hljs-keyword">from</span> <span class="hljs-string">'./info.tpl'</span>

<span class="hljs-keyword">const</span> oApp = <span class="hljs-built_in">document</span>.querySelector(<span class="hljs-string">'#app'</span>)

<span class="hljs-keyword">const</span> info = tpl(&#123;
<span class="hljs-attr">name</span>: <span class="hljs-string">'小朝'</span>,
<span class="hljs-attr">age</span>: <span class="hljs-number">18</span>,
<span class="hljs-attr">career</span>: <span class="hljs-string">'前端开发工程师'</span>,
<span class="hljs-attr">hobby</span>: <span class="hljs-string">'美食'</span>
&#125;)

oApp.innerHTML = info
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-16">tpl-loader/index.js</h3>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> &#123; tplReplace &#125; = <span class="hljs-built_in">require</span>(<span class="hljs-string">'../util'</span>)
<span class="hljs-keyword">const</span> &#123; getOptions &#125; = <span class="hljs-built_in">require</span>(<span class="hljs-string">'loader-utils'</span>)

<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">tplLoader</span>(<span class="hljs-params">source</span>) </span>&#123;
source = source.replace(<span class="hljs-regexp">/\s+/g</span>, <span class="hljs-string">''</span>)
<span class="hljs-keyword">const</span> &#123; log &#125; = getOptions(<span class="hljs-built_in">this</span>)
<span class="hljs-keyword">const</span> _log = log
? <span class="hljs-string">`console.log('compiled the file which is from <span class="hljs-subst">$&#123;<span class="hljs-built_in">this</span>.resourcePath&#125;</span>')`</span>
: <span class="hljs-string">''</span>

<span class="hljs-comment">/**
 * source
 * <div><h1>&#123;&#123;name&#125;&#125;</h1><p>&#123;&#123;age&#125;&#125;</p><p>&#123;&#123;career&#125;&#125;</p><p>&#123;&#123;hobby&#125;&#125;</p></div>
 */</span>

<span class="hljs-comment">/**
 * options
 * &#123;name: "小朝", age: 18, career: "前端开发工程师", hobby: "美食"&#125;
 */</span>

<span class="hljs-keyword">return</span> <span class="hljs-string">`
    export default options => &#123;
      // 需要被 babel-loader 转成 js程序
      <span class="hljs-subst">$&#123;tplReplace.toString()&#125;</span>
      <span class="hljs-subst">$&#123;_log.toString()&#125;</span>
      console.log('*******')
      console.log('<span class="hljs-subst">$&#123;source&#125;</span>')
      console.log(options)
      return tplReplace('<span class="hljs-subst">$&#123;source&#125;</span>', options)
    &#125;
  `</span>
&#125;

<span class="hljs-built_in">module</span>.exports = tplLoader

<span class="copy-code-btn">复制代码</span></code></pre>
<h5 data-id="heading-17">🌟🌟 loader 返回的结果</h5>
<blockquote>
<p>注意：如果是处理顺序排在最后一个的 loader，那么它的返回值将最终交给 webpack 的 require，换句话说，它一定是一段<strong>可执行的 JS 脚本</strong> （用<code>字符串</code>来存储），更准确来说，是一个 node 模块的 JS 脚本</p>
</blockquote>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// 处理顺序排在最后的 loader</span>
<span class="hljs-built_in">module</span>.exports = <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params">source</span>) </span>&#123;
    <span class="hljs-comment">// 这个 loader 的功能是把源模块转化为字符串交给 require 的调用方</span>
    <span class="hljs-keyword">return</span> <span class="hljs-string">`module.exports = <span class="hljs-subst">$&#123;<span class="hljs-built_in">JSON</span>.stringify(source)&#125;</span>`</span>
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>util.js:</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">tplReplace</span> (<span class="hljs-params">template, replaceObject</span>) </span>&#123;
  <span class="hljs-keyword">return</span> template.replace(<span class="hljs-regexp">/\&#123;\&#123;(.*?)\&#125;\&#125;/g</span>, <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">node, key</span>) </span>&#123;
    <span class="hljs-keyword">return</span> replaceObject[key]
  &#125;)
&#125;

<span class="hljs-built_in">module</span>.exports = &#123;
  tplReplace
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h1 data-id="heading-18">参考资料</h1>
<ul>
<li><a href="https://www.webpackjs.com/contribute/writing-a-loader/" target="_blank" rel="nofollow noopener noreferrer">编写一个 loader|webpack</a></li>
<li><a href="https://juejin.cn/post/6844903555673882632" target="_blank">手把手教你撸一个 Webpack Loader</a></li>
<li><a href="https://segmentfault.com/a/1190000021205134" target="_blank" rel="nofollow noopener noreferrer">手把手用代码教你实现一个 webpack loader</a></li>
</ul></div>  
</div>
            