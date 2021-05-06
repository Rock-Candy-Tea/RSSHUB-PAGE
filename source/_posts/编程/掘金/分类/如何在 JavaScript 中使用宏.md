
---
title: '如何在 JavaScript 中使用宏'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/efc0b93928c44071b383d3037ad69b3a~tplv-k3u1fbpfcp-zoom-1.image'
author: 掘金
comments: false
date: Wed, 05 May 2021 23:16:24 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/efc0b93928c44071b383d3037ad69b3a~tplv-k3u1fbpfcp-zoom-1.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>在语言当中，宏常见用途有实现 DSL 。通过宏，开发者可以自定义一些语言的格式，比如实现 JSX 语法。在 WASM 已经实现的今天，用其他语言来写网页其实并不是没有可能。像 Rust 语言就带有强大的宏功能，这使得基于 Rust 的 Yew 框架，不需要实现类似 Babel 的东西，而是靠语言本身就能实现类似 JSX 的语法。 一个 Yew 组件的例子，支持类 JSX 的语法。</p>
<pre><code class="hljs language-rust copyable" lang="rust"><span class="hljs-keyword">impl</span> Component <span class="hljs-keyword">for</span> MyComponent &#123;
    <span class="hljs-comment">// ...</span>

    <span class="hljs-function"><span class="hljs-keyword">fn</span> <span class="hljs-title">view</span></span>(&<span class="hljs-keyword">self</span>) -> Html &#123;
        <span class="hljs-keyword">let</span> onclick = <span class="hljs-keyword">self</span>.link.callback(|_| Msg::Click);
        html! &#123;
            <button onclick=onclick>&#123; <span class="hljs-keyword">self</span>.props.button_text &#125;</button>
        &#125;
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-0">JavaScript 宏的局限性</h2>
<p>不同于 Rust ，JavaScript 本身是不支持宏的，所以整个工具链也是没有考虑宏的。因此，你是可以写个识别自定义语法的宏，但是由于配套的工具链并不支持，比如最常见的 VSCode 和 Typescript ，你会得到一个语法错误。同样对于 babel 本身所用的 parser 也是不支持扩展语法的，除非你另 Fork 出来一个 Babel 。因此 babel-plugin-macros 不支持自定义语法。 不过，借助模板字符串函数，我们可以曲线救国，至少获得部分自定义语法树的能力。 一个 GraphQL 的例子，支持在 JavaScript 中直接编写 GraphQL。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">import</span> &#123; gql &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'graphql.macro'</span>;

<span class="hljs-keyword">const</span> query = gql<span class="hljs-string">`
  query User &#123;
    user(id: 5) &#123;
      lastName
      ...UserEntry1
    &#125;
  &#125;
`</span>;

<span class="hljs-comment">//  在编译期会转换成 ↓ ↓ ↓ ↓ ↓ ↓</span>

<span class="hljs-keyword">const</span> query = &#123;
  <span class="hljs-string">"kind"</span>: <span class="hljs-string">"Document"</span>,
  <span class="hljs-string">"definitions"</span>: [&#123;
    ...
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-1">为什么要用宏而非 Babel 插件</h2>
<p>Babel 插件的能力确实远大于宏，而且有些情况下确实是不得不用插件。宏比起 Babel 插件好的一点在于，宏的理念在于开箱即用。使用 React 的开发者，相信都听过的大名鼎鼎的 Create-React-App ，帮你封装好了各种底层细节，开发者专注于编写代码即可。但是 CRA 的问题在于其封装的太严了，但凡你有一点需要自定义 Babel 插件的需求，基本上就需要执行<code>yarn react-script eject</code>，将所有底层细节暴露出来。 而对于宏来说，你只需要在项目的 Babel 配置内添加一个 babel-plugin-macros 插件，那么对于任何自定义的 Babel 宏都可以完美支持，而不是像插件一样，需要下载各种各样的插件。 CRA 已经内置了 babel-plugin-macros ，你可以在 CRA 项目中使用任意的 Babel 宏。</p>
<h1 data-id="heading-2">如何写一个宏？</h1>
<h2 data-id="heading-3">介绍</h2>
<p>一个宏非常像一个 Babel 插件，因此事先了解如何编写 Babel 插件是非常有帮助的，对于如何编写 Babel 插件， Babel 官方有一本<a href="https://github.com/jamiebuilds/babel-handbook/blob/master/translations/zh-Hans/README.md" title="手册" target="_blank" rel="nofollow noopener noreferrer">手册</a>，专门介绍了如何从零编写一个 Babel 插件。 在知道如何编写 Babel 插件之后，我们首先通过一个使用宏的例子，来介绍下， Babel 是如何识别文件中的宏的。是某种的特殊的语法，还是用烂的 $ 符号？</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">import</span> preval <span class="hljs-keyword">from</span> <span class="hljs-string">'preval.macro'</span>

<span class="hljs-keyword">const</span> one = preval<span class="hljs-string">`module.exports = 1 + 2 - 1 - 1`</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这是非常常见的一个宏，其作用是在编译期间执行字符串中的 JavaScript 代码，然后将执行的结果替换到相应的地方，如上的代码在编译期会被展开为：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">import</span> preval <span class="hljs-keyword">from</span> <span class="hljs-string">'preval.macro'</span>

<span class="hljs-keyword">const</span> one = <span class="hljs-number">1</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>从使用来方式来看，唯一与识别宏沾点关系的就是<code>*.macro</code>字符，这也确实就是 Babel 如何识别宏的方式，实际上不仅对于<code>*.macro</code>的形式， Babel 认为库名匹配正则<code>/[./]macro(\.c?js)?$/</code>表达式的库就是 Babel 宏，这些匹配表达式的一些例子：</p>
<pre><code class="copyable">'my.macro'
'my.macro.js'
'my.macro.cjs'
'my/macro'
'my/macro.js'
'my/macro.cjs'
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-4">编写</h2>
<p>接下来，我们将简单编写一个<code>importURL</code>宏，其作用是通过 url 来引入一些库，并在编译期间将这些库的代码预先拉取下来，处理一下然后引入到文件中。我知道有些 Webpack 插件已经支持 从 url 来引入库，不过这同样是一个很好的例子来学习如何编写宏，为了有趣！以及如何在 NodeJS 中发起同步请求! :)</p>
<h3 data-id="heading-5">准备</h3>
<p>首先创建一个名为 importURL 的文件夹，执行<code>npm init -y</code>，来快速创建一个项目。在项目使用宏的人需要安装<code>babel-plugin-macros</code>，同样的，编写宏的同样需要安装这个插件，在写之前，我们也需要提前安装一些其他的库来辅助我们编写宏，在开发之前，需要事先：</p>
<ul>
<li>在<code>package.json</code>将<code>name</code>改为<code>import-url.macro</code>，符合 Babel 识别宏的格式</li>
<li>我们需要用 Babel 提供的辅助方法来创建宏。执行<code>yarn add babel-plugin-macros</code></li>
<li><code>yarn add fs-extra</code>，一个更容易使用的代替 Node<code>fs</code>模块的库</li>
<li><code>yarn add find-root</code>，编写宏的过程我们需要根据所处理文件的路径找到其所在的工作目录，从而写入缓存，这是一个已经封装好的库</li>
</ul>
<h3 data-id="heading-6">示例</h3>
<p>我们的目标就是将如下代码转换成</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">import</span> importURL <span class="hljs-keyword">from</span> <span class="hljs-string">'importurl.macros'</span>;

<span class="hljs-keyword">const</span> React = importURL(<span class="hljs-string">'https://unpkg.com/react@17.0.1/umd/react.development.js'</span>);

<span class="hljs-comment">// 编译成</span>

<span class="hljs-keyword">import</span> importURL <span class="hljs-keyword">from</span> <span class="hljs-string">'importurl.macros'</span>;

<span class="hljs-keyword">const</span> React = <span class="hljs-built_in">require</span>(<span class="hljs-string">'../cache/pkg1.js'</span>);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>我们会解析代码 importURL 函数的第一个参数，当做远程库的地址，然后在编译期间同步的通过 Get 请求拉取代码内容。然后写入项目顶层文件夹下<code>.chache</code>下，并替换相应的 importURL 语句成<code>require(...)</code>语句，路径<code>...</code>则是使用<code>importURL</code>的文件相对<code>.cache</code>文件中的相对路径，使得 webpack 在最终打包的时候能够找到对应的代码。</p>
<h3 data-id="heading-7">开始</h3>
<p>我们先看看最终的代码长什么样子</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">import</span> &#123; execSync &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'child_process'</span>;
<span class="hljs-keyword">import</span> findRoot <span class="hljs-keyword">from</span> <span class="hljs-string">'find-root'</span>;
<span class="hljs-keyword">import</span> path <span class="hljs-keyword">from</span> <span class="hljs-string">'path'</span>;
<span class="hljs-keyword">import</span> fse <span class="hljs-keyword">from</span> <span class="hljs-string">'fs-extra'</span>;

<span class="hljs-keyword">import</span> &#123; createMacro &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'babel-plugin-macros'</span>;

<span class="hljs-keyword">const</span> syncGet = <span class="hljs-function">(<span class="hljs-params">url</span>) =></span> &#123;
  <span class="hljs-keyword">const</span> data = execSync(<span class="hljs-string">`curl -L <span class="hljs-subst">$&#123;url&#125;</span>`</span>).toString();
  <span class="hljs-keyword">if</span> (data === <span class="hljs-string">''</span>) &#123;
    <span class="hljs-keyword">throw</span> <span class="hljs-keyword">new</span> <span class="hljs-built_in">Error</span>(<span class="hljs-string">'empty data'</span>);
  &#125;
  <span class="hljs-keyword">return</span> data;
&#125;

<span class="hljs-keyword">let</span> count = <span class="hljs-number">0</span>;
<span class="hljs-keyword">export</span> <span class="hljs-keyword">const</span> genUniqueName = <span class="hljs-function">() =></span> <span class="hljs-string">`pkg<span class="hljs-subst">$&#123;++count&#125;</span>.js`</span>;

<span class="hljs-built_in">module</span>.exports = createMacro(<span class="hljs-function">(<span class="hljs-params">ctx</span>) =></span> &#123;
  <span class="hljs-keyword">const</span> &#123;
    references, <span class="hljs-comment">// 文件中所有对宏的引用</span>
    <span class="hljs-attr">babel</span>: &#123;
      <span class="hljs-attr">types</span>: t,
    &#125;
  &#125; = ctx;
  <span class="hljs-comment">// babel 会把当前处理的文件路径设置到 ctx.state.filename</span>
  <span class="hljs-keyword">const</span> workspacePath = findRoot(ctx.state.filename);
  <span class="hljs-comment">// 计算出缓存文件夹</span>
  <span class="hljs-keyword">const</span> cacheDirPath = path.join(workspacePath, <span class="hljs-string">'.cache'</span>);
  <span class="hljs-comment">//</span>
  <span class="hljs-keyword">const</span> calls = references.default.map(<span class="hljs-function"><span class="hljs-params">path</span> =></span> path.findParent(<span class="hljs-function"><span class="hljs-params">path</span> =></span> path.node.type === <span class="hljs-string">'CallExpression'</span> ));
  calls.forEach(<span class="hljs-function"><span class="hljs-params">nodePath</span> =></span> &#123;
    <span class="hljs-comment">// 确定 astNode 的类型</span>
    <span class="hljs-keyword">if</span> (nodePath.node.type === <span class="hljs-string">'CallExpression'</span>) &#123;
      <span class="hljs-comment">// 确定函数的第一个参数是纯字符串</span>
      <span class="hljs-keyword">if</span> (nodePath.node.arguments[<span class="hljs-number">0</span>]?.type === <span class="hljs-string">'StringLiteral'</span>) &#123;
        <span class="hljs-comment">// 获取一个参数，当做远程库的地址</span>
        <span class="hljs-keyword">const</span> url = nodePath.node.arguments[<span class="hljs-number">0</span>].value;
        <span class="hljs-comment">// 根据 url 拉取代码</span>
        <span class="hljs-keyword">const</span> codes = syncGet(url);
        <span class="hljs-comment">// 生成一个唯一包名，防止冲突</span>
        <span class="hljs-keyword">const</span> pkgName = genUniqueName();
        <span class="hljs-comment">// 确定最终要写入的文件路径</span>
        <span class="hljs-keyword">const</span> cahceFilename = path.join(cacheDirPath, pkgName);
        <span class="hljs-comment">// 通过 fse 库，将内容写入， outputFileSync 会自动创建不存在的文件夹</span>
        fse.outputFileSync(cahceFilename, codes);
        <span class="hljs-comment">// 计算出相对路径</span>
        <span class="hljs-keyword">const</span> relativeFilename = path.relative(ctx.state.filename, cahceFilename);
        <span class="hljs-comment">// 最终计算替换 importURL 语句</span>
        nodePath.replaceWith(t.stringLiteral(<span class="hljs-string">`require('<span class="hljs-subst">$&#123;relativeFilename&#125;</span>')`</span>))
      &#125;
    &#125;
  &#125;);
&#125;);
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>创建一个宏</li>
</ul>
<p>我们通过<code>createMacro</code>函数来创建一个宏，<code>createMacro</code>接受我们编写的函数当做参数来生成一个宏，但实际上我们并不关心<code>createMacro</code>的返回时值是什么，因为我们的代码最终都将会被自己替换掉，不会在运行期间执行到。 我们编写的函数的第一个参数是 Babel 传递给我们的一些状态，我们可以大概看下其类型都有什么。</p>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">createMacro</span>(<span class="hljs-params">handler: MacroHandler, options?: Options</span>): <span class="hljs-title">any</span></span>;
<span class="hljs-keyword">interface</span> MacroParams &#123;
      <span class="hljs-attr">references</span>: &#123; <span class="hljs-attr">default</span>: Babel.NodePath[] &#125; & References;
      state: Babel.PluginPass;
      babel: <span class="hljs-keyword">typeof</span> Babel;
      config?: &#123; [key: <span class="hljs-built_in">string</span>]: <span class="hljs-built_in">any</span> &#125;;
  &#125;
<span class="hljs-keyword">export</span> <span class="hljs-keyword">interface</span> PluginPass &#123;
    <span class="hljs-attr">file</span>: BabelFile;
    key: <span class="hljs-built_in">string</span>;
    opts: PluginOptions;
    cwd: <span class="hljs-built_in">string</span>;
    filename: <span class="hljs-built_in">string</span>;
    [key: <span class="hljs-built_in">string</span>]: unknown;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>可视化 AST</li>
</ul>
<p>我们可以通过<a href="https://astexplorer.net/" title="astexplorer" target="_blank" rel="nofollow noopener noreferrer">astexplorer</a>来观察我们将要处理代码的语法树，对于如下代码</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">import</span> importURL <span class="hljs-keyword">from</span> <span class="hljs-string">'importurl.macros'</span>;

<span class="hljs-keyword">const</span> React = importURL(<span class="hljs-string">'https://unpkg.com/react@17.0.1/umd/react.development.js'</span>);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>会生成如下语法树<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/efc0b93928c44071b383d3037ad69b3a~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer">红色标红的语法树节点，就是 Babel 会通过<code>ctx.references</code>传递给我们的，因此我们需要通过<code>.findParent()</code>方法来向上找到父节点<code>CallExpresstion</code>，才能去获取<code>arguments</code>属性下的参数，拿到远程库的 URL 地址。</p>
<ul>
<li>同步请求</li>
</ul>
<p>这里的一个难点在于， Babel 不支持异步转换，所有的转换操作都是同步的，因此在发起请求时也必须是同步的请求。我本来以为这是一件很简单的事情， Node 会提供一个类似<code>sync: true</code>的选项。但是并没有的， Node 确实不支持任何同步请求，除非你选择用下面这种很怪异的方式</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> syncGet = <span class="hljs-function">(<span class="hljs-params">url</span>) =></span> &#123;
  <span class="hljs-keyword">const</span> data = execSync(<span class="hljs-string">`curl -L <span class="hljs-subst">$&#123;url&#125;</span>`</span>).toString();
  <span class="hljs-keyword">if</span> (data === <span class="hljs-string">''</span>) &#123;
    <span class="hljs-keyword">throw</span> <span class="hljs-keyword">new</span> <span class="hljs-built_in">Error</span>(<span class="hljs-string">'empty data'</span>);
  &#125;
  <span class="hljs-keyword">return</span> data;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>收尾</li>
</ul>
<p>在拿到代码后，我们将代码写入到开始计算出的文件路径中，这里我们使用<code>fs-extra</code>的目的在于，<code>fs-extra</code>在写入的时候如果遇到不存在文件夹，不会像<code>fs</code>一样直接抛出错误，而是自动创建相应的文件件。在写入完成后，我们通过 Babel 提供的辅助方法<code>stringLiteral</code>创字符串节点，随后替换掉我们的<code>importURL(...)</code>，自此我们的整个转换流程就结束了。</p>
<h3 data-id="heading-8">最后</h3>
<p>这个宏存在一些缺陷，有兴趣的同学可以继续完善：</p>
<ul>
<li>没有识别同一 URL 的库，进行复用，不过我想这些已经满足如何编写一个宏的目的了。</li>
<li><code>genUniqueName</code>在跨文件是会计算出重复包名，正确的算法应该是根据 url 计算哈希值来当做唯一包名</li>
</ul></div>  
</div>
            