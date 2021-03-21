
---
title: 这样入门 js 抽象语法树(AST)，从此我来到了一个新世界
categories: 
    - 编程
    - 掘金 - 分类
author: 掘金 - 分类
comments: false
date: Sun, 21 Mar 2021 00:10:40 GMT
thumbnail: https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/7426fd01fe254668a36c6b369bed788b~tplv-k3u1fbpfcp-zoom-1.image
---

<div>   
<div class="markdown-body"><style>.markdown-body{word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333}.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6{line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px}.markdown-body h1{font-size:30px;margin-bottom:5px}.markdown-body h2{padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec}.markdown-body h3{font-size:18px;padding-bottom:0}.markdown-body h4{font-size:16px}.markdown-body h5{font-size:15px}.markdown-body h6{margin-top:5px}.markdown-body p{line-height:inherit;margin-top:22px;margin-bottom:22px}.markdown-body img{max-width:100%}.markdown-body hr{border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px}.markdown-body code{word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em}.markdown-body code,.markdown-body pre{font-family:Menlo,Monaco,Consolas,Courier New,monospace}.markdown-body pre{overflow:auto;position:relative;line-height:1.75}.markdown-body pre>code{font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8}.markdown-body a{text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff}.markdown-body a:active,.markdown-body a:hover{color:#275b8c}.markdown-body table{display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6}.markdown-body thead{background:#f6f6f6;color:#000;text-align:left}.markdown-body tr:nth-child(2n){background-color:#fcfcfc}.markdown-body td,.markdown-body th{padding:12px 7px;line-height:24px}.markdown-body td{min-width:120px}.markdown-body blockquote{color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8}.markdown-body blockquote:after{display:block;content:""}.markdown-body blockquote>p{margin:10px 0}.markdown-body ol,.markdown-body ul{padding-left:28px}.markdown-body ol li,.markdown-body ul li{margin-bottom:0;list-style:inherit}.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item{list-style:none}.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul{margin-top:0}.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul{margin-top:3px}.markdown-body ol li{padding-left:6px}.markdown-body .contains-task-list{padding-left:0}.markdown-body .task-list-item{list-style:none}@media (max-width:720px){.markdown-body h1{font-size:24px}.markdown-body h2{font-size:20px}.markdown-body h3{font-size:18px}}</style><blockquote>
<p>本文产出工具：<a href="https://github.com/vortesnail/tsccss" target="_blank" rel="nofollow noopener noreferrer">github/tsccss</a> ，欢迎使用，star🌟。<br>
本人博客地址：<a href="https://github.com/vortesnail/blog" target="_blank" rel="nofollow noopener noreferrer">github/blog</a> ，若此文对你有帮助，赏个 star🌟，谢谢老爷了！</p>
</blockquote>
<h2 data-id="heading-0">契机</h2>
<p>最近在搭建一个开源的项目环境时，我需要打一个 ES 模块的包，以便开发者可以直接通过 <code>npm</code>  就能安装并使用，但是这个项目注定了会有样式，而且我希望打出的包的文件目录和我开发目录是一致的，似乎 <code>Rollup</code>  是一个不错的选择，但是我（自虐般地）选择了 <code>Typescript</code>  自带的编译器 <code>tsc</code> ，然后我就开始我的填坑之旅～</p>
<h2 data-id="heading-1">tsc 遇到的坑</h2>
<p>在使用 <code>tsc</code>  编译我的代码时，对我目前来说，有<strong>三个</strong>基本的坑，下面我会对它们进行简单的阐述，在此之前看下即将被编译的目录结构。</p>
<pre><code class="copyable">|-- src
  |-- assets
    |-- test.png
  |-- util
    |-- classnames.ts
  |-- index.tsx
  |-- index.scss
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-2">简化引用路径问题</h3>
<p>首先我是在 <code>tsconfig.json</code>  中写了简化引用路径配置的，比如针对以上目录，我是这样：</p>
<pre><code class="hljs language-json copyable" lang="json">{
  <span class="hljs-attr">"compilerOptions"</span>: {
    <span class="hljs-attr">"baseUrl"</span>: <span class="hljs-string">"./"</span>,
    <span class="hljs-attr">"paths"</span>: {
      <span class="hljs-attr">"@Src/*"</span>: [<span class="hljs-string">"src/*"</span>],
      <span class="hljs-attr">"@Utils/*"</span>: [<span class="hljs-string">"src/utils/*"</span>],
      <span class="hljs-attr">"@Assets/*"</span>: [<span class="hljs-string">"src/assets/*"</span>]
    }
  }
}
<span class="copy-code-btn">复制代码</span></code></pre>
<p>那么无论我层级多深时，我要是想引用 <code>util</code>  或 <code>assets</code>  里面的文件模块、资源就会特别方便，比如我在 <code>index.tsx</code>  文件中这样引入：</p>
<p>编译前：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">import</span> classNames <span class="hljs-keyword">from</span> <span class="hljs-string">"@Utils/classnames"</span>;
<span class="hljs-keyword">import</span> testPNG <span class="hljs-keyword">from</span> <span class="hljs-string">"@Assets/test.png"</span>;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>编译后（预期 😢）：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">import</span> classNames <span class="hljs-keyword">from</span> <span class="hljs-string">"./util/classnames"</span>;
<span class="hljs-keyword">import</span> testPNG <span class="hljs-keyword">from</span> <span class="hljs-string">"./assets/test.png"</span>;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>然而实际编译后的结果令我大失所望， <code>tsc</code>  既然连这个都不支持转译！！它编译之后的代码还是老样子，于是我就去找官网查，发现也没有这个相关的配置项，于是跑到外网查了下发现有人是和我遇到了相同的问题的，它提供了一个解决方案就是，使用这个插件 <a href="https://github.com/joonhocho/tscpaths" target="_blank" rel="nofollow noopener noreferrer">tscpaths</a> 并在编译后多加一段 <code>npm</code>  命令即可：</p>
<pre><code class="hljs language-json copyable" lang="json"><span class="hljs-string">"scripts"</span>: {
  <span class="hljs-attr">"build"</span>: <span class="hljs-string">"tsc -p tsconfig.json && tscpaths -p tsconfig.json -s src -o dist,
},
</span><span class="copy-code-btn">复制代码</span></code></pre>
<p>当执行到这个命令时：</p>
<pre><code class="hljs language-bash copyable" lang="bash">tscpaths -p tsconfig.json -s src -o dist
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这个插件会去遍历每一个我们已经由 <code>tsc</code>  编译之后的 <code>.js</code>  文件，将我们<strong>简化的引用路径转为相对路径</strong>，大功告成～</p>
<h3 data-id="heading-3">静态资源未打包问题</h3>
<p>如上所示，如果我在 <code>index.tsx</code>  文件中引入一个放在 <code>assets</code>  的图片资源：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">import</span> testPNG <span class="hljs-keyword">from</span> <span class="hljs-string">"@Assets/test.png"</span>;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>在经过 <code>tsc</code>  编译之后，而且在使用我们的命令行工具之后，我们的引用路径是对了，但是一看打包出来的目录中，是不会出现 <code>assets</code>  这个资源文件夹的，其实这也正常，毕竟 <code>tsc</code>  也仅仅是个 Typescript 的编译器，要实现其它的打包功能，要靠自己动手！</p>
<p>解决问题的办法就是使用 <a href="https://github.com/calvinmetcalf/copyfiles" target="_blank" rel="nofollow noopener noreferrer">copyfiles</a> 命令行工具，它和上面我们介绍的插件一样，都是在 <code>tsc</code>  编译之后，做一些额外操作达到我们想要的目的。</p>
<p>就像它的名字一样，它就是拿来复制文件的～我们在 npm scripts 下的 build 命令后面再加上这个：</p>
<pre><code class="hljs language-bash copyable" lang="bash">copyfiles -f src/assets/* dist/assets
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这样就能把资源文件夹复制到打包之后的文件目录下了。</p>
<h3 data-id="heading-4">引入样式文件后缀名问题</h3>
<p>我们做一个项目时在所难免会用到 <code>sass</code>  或 <code>less</code> ，本项目就选择了 <code>sass</code> ，我在 <code>index.tsx</code>  中引入样式文件方式如下：</p>
<pre><code class="hljs language-jsx copyable" lang="jsx"><span class="hljs-keyword">import</span> <span class="hljs-string">"./index.scss"</span>;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>但是在 <code>tsc</code>  编译为 <code>.js</code>  文件之后，打开 <code>index.js</code>  发现引入的样式后缀还是 <code>.scss</code> 。作为给别的开发者使用的包，一定是要引入 <code>.css</code>  文件的格式的，你不可能确定别人用的都是 <code>sass</code> ，所以我又去网上找解决方案，发现很少有人提这个问题，而且也没有找到可以用的插件什么的。</p>
<p>就在一筹莫展之时，我突然想到，卧槽，这不就是类似于上面提到的 <code>tscpaths</code>  这个工具吗，也是在文件内做字符串替换，太像了！于是我赶紧下载了它的源码，看了下大概是使用 node 读取了 <code>tsconfig.json</code>  中 <code>bathUrl</code>  和 <code>paths</code>  配置，以及用户自定义的入口、出口路径来找到 <code>.js</code>  文件，分析成相对路径之后再<strong>正则匹配</strong>到对应的引用路径去替换掉！</p>
<p>立马有了思路准备实践，突然想到全局正则匹配做替换的局限性，比如在<strong>开发者代码中也写了与引用一样的代码</strong>（这种情况基本不可能发生，但是仍要考虑），那不是把人家的逻辑代码都改了吗？比如以下代码：</p>
<pre><code class="hljs language-jsx copyable" lang="jsx"><span class="hljs-keyword">import</span> React <span class="hljs-keyword">from</span> <span class="hljs-string">"react"</span>;
<span class="hljs-keyword">import</span> <span class="hljs-string">"./index.scss"</span>;

<span class="hljs-keyword">const</span> Tool = <span class="hljs-function">() =></span> {
  <span class="hljs-keyword">return</span> (
    <span class="xml"><span class="hljs-tag"><<span class="hljs-name">div</span>></span>
      <span class="hljs-tag"><<span class="hljs-name">p</span>></span>You should import style file like this:<span class="hljs-tag"></<span class="hljs-name">p</span>></span>
      <span class="hljs-tag"><<span class="hljs-name">p</span>></span>import './index.scss'<span class="hljs-tag"></<span class="hljs-name">p</span>></span>
    <span class="hljs-tag"></<span class="hljs-name">div</span>></span></span>
  );
};
<span class="copy-code-btn">复制代码</span></code></pre>
<p>怎么办，你做全局替换，是会<strong>替换掉别人逻辑源代码的</strong>。。当然，可以写更好的查找算法（或正则）来精确替换，但是无形中考虑的情况就非常多了；我们有没有更好的实现方式呢？这时候我想到了<strong>抽象语法树(AST)</strong>。</p>
<p>注意 ⚠️：另外要说一下， <code>tsc</code>  也不会编译 <code>.scss</code>  文件的，它需要 <code>node-sass</code>  来将每个 <code>.scss</code>  文件编译到对应打包目录，在 <code>tsc</code>  编译之后，再执行以下命令即可：</p>
<pre><code class="hljs language-bash copyable" lang="bash"><span class="hljs-string">"build-css"</span>: <span class="hljs-string">"node-sass -r src -o dist"</span>,
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-5">AST 是什么？</h2>
<p>如果你了解或者使用过 <code>ESLint</code> 、<code>Babel</code>  及 <code>Webpack</code>  这类工具，那么恭喜你，你已经对 AST 的强大之处有了最直观的了解了，比如 <code>ESLint</code>  是怎么修复你的代码的呢？看下面不太严谨的图：</p>
<p><img alt="1.jpg" class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/7426fd01fe254668a36c6b369bed788b~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p>不严谨的语言描述就是，eslint 将当前的 js 代码解析成了一个抽象语法树，在这棵树上做了一些修整，比如剪掉一条树枝，就是去除代码中多出的空格 <code>space</code> ；比如修整了一条树枝，就是 <code>var</code>  转换为 <code>const</code>  等。修整完之后再转换为我们的 js 代码！</p>
<p>这个树中的每条“枝”都代表了 js 代码中的某个字段的<strong>描述对象</strong>，比如以下简单的代码：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">const</span> a = <span class="hljs-number">1</span>;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>我们先自己定制一套简单的转换为 AST 语法规则，可以这样表示上面这行代码：</p>
<pre><code class="hljs language-json copyable" lang="json">{
  <span class="hljs-attr">"type"</span>: <span class="hljs-string">"VariableDeclaration"</span>,
  <span class="hljs-attr">"kind"</span>: <span class="hljs-string">"const"</span>,
  <span class="hljs-attr">"declarations"</span>: [
    {
      <span class="hljs-attr">"type"</span>: <span class="hljs-string">"VariableDeclarator"</span>,
      <span class="hljs-attr">"id"</span>: {
        <span class="hljs-attr">"type"</span>: <span class="hljs-string">"Identifier"</span>,
        <span class="hljs-attr">"name"</span>: <span class="hljs-string">"a"</span>
      },
      <span class="hljs-attr">"init"</span>: {
        <span class="hljs-attr">"type"</span>: <span class="hljs-string">"Literal"</span>,
        <span class="hljs-attr">"value"</span>: <span class="hljs-number">1</span>,
        <span class="hljs-attr">"raw"</span>: <span class="hljs-string">"1"</span>
      }
    }
  ]
}
<span class="copy-code-btn">复制代码</span></code></pre>
<p>是的，这就是一颗简易的抽象语法树了，就这么简单，它只是一种特殊的对象结构来表示我们的 js 代码而已，如果我们有一个手段，能拿到表示 <code>1</code>  这个值的节点，并将 <code>init.value</code>  改为 <code>2</code> ，再将该语法树转换为 js 源码，那就能得到：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">const</span> a = <span class="hljs-number">2</span>;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>那么上面说的“转换”规则是不用我们自己去写的，随着 JavaScript 语言的发展，由一些大佬创建的项目 <a href="https://github.com/estree/estree" target="_blank" rel="nofollow noopener noreferrer">ESTree</a> 用于更新 AST 规则，目前已成为社区标准。然后社区中一些其它项目比如 ESlint 和 Babel 就会使用 ESTree 或在此基础上做一些修改，然后衍生出自己的一套规则，并制作相应的转换工具，暴露出一些 API 给开发者使用。</p>
<h2 data-id="heading-6">搭配工具</h2>
<p>因为生成的 AST 结构上看起来是特别<strong>繁杂</strong>的，如果没有好用工具或文档，学习时或写代码时会很困扰，那么接下来就给大家介绍三个利器。</p>
<h3 data-id="heading-7">在线调试工具 <a href="https://astexplorer.net/" target="_blank" rel="nofollow noopener noreferrer">AST Explorer</a></h3>
<blockquote>
<p>这是一个非常棒的网站，只需要将你现在的 js 代码输入进去，即可查看转换后的 AST 结构。</p>
</blockquote>
<p>有了这个网站你就能实时地去查看解析之后的 AST 是什么样子的，以及它们的类型是什么，这在之后写代码去对 AST 做修改特别有用！因为你可以明确自己想要修改的地方是哪里。</p>
<p><img alt="2.gif" class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/eac7dfcdc68046f3b7f6eb7b06a96dc2~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p>比如上图中，我们想要修改 <code>1</code> 为 <code>2</code> ，我们通过某个工具去找到这个 AST 中的 <code>type</code>  为 <code>Literal</code>  这个节点，将其 <code>value</code>  设为 <code>2</code> ，再转换为 js 代码就实现了这个需求。</p>
<p>类似的工具是很多的，我们就选用 Facebook 官方的开源工具：<a href="https://github.com/facebook/jscodeshift" target="_blank" rel="nofollow noopener noreferrer">jscodeshift</a></p>
<h3 data-id="heading-8">AST 转换工具 <a href="https://github.com/facebook/jscodeshift" target="_blank" rel="nofollow noopener noreferrer">jscodeshift</a></h3>
<p>jscodeshift 是基于 <a href="https://github.com/benjamn/recast" target="_blank" rel="nofollow noopener noreferrer">recast</a> 封装的一个库，相比于 recast 不友好的 api 设计，jscodeshift 将其封装并暴露出对 js 开发者来说更为友好的 api，让我们在操作修改 AST 的时候更加方便。</p>
<p>我建议大家先知道这个工具就行，具体的 api 使用我下面会跟大家挑几个典型的说一说，有个具体的印象就行，说实话，这个库的文档写的并不好，也不适合初学者阅读，特别是英语还不好的人。当你使用过它的一些 api 后有了直观的感觉，再去阅读也不迟～</p>
<h3 data-id="heading-9">AST 类型大全 <a href="https://babeljs.io/docs/en/babel-types" target="_blank" rel="nofollow noopener noreferrer">@babel/types</a></h3>
<p>这是一本 AST 类型词典，如果我们想要生成一些新的代码，也就是要生成一些新的节点，按照语法规则，你必须将你要添加的节点类型按照规范传入，比如 <code>const</code>  的类型就为 <code>type: VariableDeclaration</code> ，当然了， <code>type</code>  只是一个节点的一个属性而已，还有其他的，你都可以在这里面查阅到。</p>
<p>下面是常用的节点类型含义对照表，更多的类型大家可以细看 <a href="https://babeljs.io/docs/en/babel-types" target="_blank" rel="nofollow noopener noreferrer">@babel/types</a>：</p>





















































































<table><thead><tr><th>类型名称</th><th>中文译名</th><th>描述</th></tr></thead><tbody><tr><td>Program</td><td>程序主体</td><td>整段代码的主体</td></tr><tr><td>VariableDeclaration</td><td>变量声明</td><td>声明变量，比如 let const var</td></tr><tr><td>FunctionDeclaration</td><td>函数声明</td><td>声明函数，比如 function</td></tr><tr><td>ExpressionStatement</td><td>表达式语句</td><td>通常为调用一个函数，比如 console.log(1)</td></tr><tr><td>BlockStatement</td><td>块语句</td><td>包裹在 {} 内的语句，比如 if (true) { console.log(1) }</td></tr><tr><td>BreakStatement</td><td>中断语句</td><td>通常指 break</td></tr><tr><td>ContinueStatement</td><td>持续语句</td><td>通常指 continue</td></tr><tr><td>ReturnStatement</td><td>返回语句</td><td>通常指 return</td></tr><tr><td>SwitchStatement</td><td>Switch 语句</td><td>通常指 switch</td></tr><tr><td>IfStatement</td><td>If 控制流语句</td><td>通常指 if (true) {} else {}</td></tr><tr><td>Identifier</td><td>标识符</td><td>标识，比如声明变量语句中 const a = 1 中的 a</td></tr><tr><td>ArrayExpression</td><td>数组表达式</td><td>通常指一个数组，比如 [1, 2, 3]</td></tr><tr><td>StringLiteral</td><td>字符型字面量</td><td>通常指字符串类型的字面量，比如 const a = '1' 中的 '1'</td></tr><tr><td>NumericLiteral</td><td>数字型字面量</td><td>通常指数字类型的字面量，比如 const a = 1 中的 1</td></tr><tr><td>ImportDeclaration</td><td>引入声明</td><td>声明引入，比如 import</td></tr></tbody></table>
<h2 data-id="heading-10">AST 节点的增删改查</h2>
<p>上面说到了 jscodeshift 的 api 设计的是比较友好的，那么我们就以一个树的增删改查来简单地带大家了解一下，不过在这之前需要先搭建一个简单的开发环境。</p>
<h3 data-id="heading-11">开发环境</h3>
<p>第一步：创建一个项目文件夹</p>
<pre><code class="hljs language-bash copyable" lang="bash">mkdir ast-demo
<span class="hljs-built_in">cd</span> ast-demo
<span class="copy-code-btn">复制代码</span></code></pre>
<p>第二步：项目初始化</p>
<pre><code class="hljs language-bash copyable" lang="bash">npm init -y
<span class="copy-code-btn">复制代码</span></code></pre>
<p>第三步：安装 jscodeshift</p>
<pre><code class="hljs language-bash copyable" lang="bash">npm install jscodeshift --save
<span class="copy-code-btn">复制代码</span></code></pre>
<p>第四步：新建 <code>4</code>  个 js 文件，分别对应增删该查。</p>
<pre><code class="hljs language-bash copyable" lang="bash">touch create.js delete.js update.js find.js
<span class="copy-code-btn">复制代码</span></code></pre>
<p>第五步：在做以下事例时，请大家打开 <a href="https://astexplorer.net/" target="_blank" rel="nofollow noopener noreferrer">AST Explorer</a> ，把要转换的 <code>value</code>  都复制进来看看它的树结构，以便更好地理解。</p>
<h3 data-id="heading-12">查找节点</h3>
<p><code>find.js</code> ：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">const</span> jf = <span class="hljs-built_in">require</span>(<span class="hljs-string">"jscodeshift"</span>);

<span class="hljs-keyword">const</span> value = <span class="hljs-string">`
import React from 'react';
import { Button } from 'antd';
`</span>;

<span class="hljs-keyword">const</span> root = jf(value);
root
  .find(jf.ImportDeclaration, { <span class="hljs-attr">source</span>: { <span class="hljs-attr">value</span>: <span class="hljs-string">"antd"</span> } })
  .forEach(<span class="hljs-function">(<span class="hljs-params">path</span>) =></span> {
    <span class="hljs-built_in">console</span>.log(path.node.source.value);
  });
<span class="copy-code-btn">复制代码</span></code></pre>
<p>在控制台执行以下命令：</p>
<pre><code class="hljs language-bash copyable" lang="bash">node find.js
<span class="copy-code-btn">复制代码</span></code></pre>
<p>然后你就能看到控制台打印了 <code>antd</code> 。</p>
<p>在此说明一下，上面代码中定义的 <code>value</code>  字符串就是我们要<strong>操作</strong>的文本内容，实际应用中我们一般都是读取文件，然后做处理。</p>
<p>在上面的 <code>.find</code>  函数中，第一个参数为要查找的类型，第二个参数为查询条件，如果你将上面的 <code>value</code>  复制到 <a href="https://astexplorer.net/" target="_blank" rel="nofollow noopener noreferrer">AST Explorer</a> 上看看，你就知道这个查询条件为什么是这种结构了。</p>
<h3 data-id="heading-13">修改节点</h3>
<p><code>update.js</code> ：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">const</span> jf = <span class="hljs-built_in">require</span>(<span class="hljs-string">"jscodeshift"</span>);

<span class="hljs-keyword">const</span> value = <span class="hljs-string">`
import React from 'react';
import { Button, Input } from 'antd';
`</span>;

<span class="hljs-keyword">const</span> root = jf(value);
root
  .find(jf.ImportDeclaration, { <span class="hljs-attr">source</span>: { <span class="hljs-attr">value</span>: <span class="hljs-string">"antd"</span> } })
  .forEach(<span class="hljs-function">(<span class="hljs-params">path</span>) =></span> {
    <span class="hljs-keyword">const</span> { specifiers } = path.node;
    specifiers.forEach(<span class="hljs-function">(<span class="hljs-params">spec</span>) =></span> {
      <span class="hljs-keyword">if</span> (spec.imported.name === <span class="hljs-string">"Button"</span>) {
        spec.imported.name = <span class="hljs-string">"Select"</span>;
      }
    });
  });

<span class="hljs-built_in">console</span>.log(root.toSource());
<span class="copy-code-btn">复制代码</span></code></pre>
<p>上面的代码目的是将从 <code>antd</code>  引入的 <code>Button</code>  改为 <code>Input</code> ，为了很精确地定位在这一行，我们先通过 <code>ImportDeclaration</code>  和条件参数去找到，在向内找到 <code>Button</code>  这个节点，简单的判断之后就可以做修改了。</p>
<p>你能看到最后一行我们执行了 <code>toSource()</code> ，该方法就是将 <code>AST</code>  转回为我们的源码，控制台打印如下：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">import</span> React <span class="hljs-keyword">from</span> <span class="hljs-string">"react"</span>;
<span class="hljs-keyword">import</span> { Select, Input } <span class="hljs-keyword">from</span> <span class="hljs-string">"antd"</span>; <span class="hljs-comment">// 可以看到 Button 已被精确地替换为了 Select</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-14">增加节点</h3>
<p><code>create.js</code> ：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">const</span> jf = <span class="hljs-built_in">require</span>(<span class="hljs-string">"jscodeshift"</span>);

<span class="hljs-keyword">const</span> value = <span class="hljs-string">`
import React from 'react';
import { Button, Input } from 'antd';
`</span>;

<span class="hljs-keyword">const</span> root = jf(value);
root
  .find(jf.ImportDeclaration, { <span class="hljs-attr">source</span>: { <span class="hljs-attr">value</span>: <span class="hljs-string">"antd"</span> } })
  .forEach(<span class="hljs-function">(<span class="hljs-params">path</span>) =></span> {
    <span class="hljs-keyword">const</span> { specifiers } = path.node;
    specifiers.push(jf.importSpecifier(jf.identifier(<span class="hljs-string">"Select"</span>)));
  });

<span class="hljs-built_in">console</span>.log(root.toSource());
<span class="copy-code-btn">复制代码</span></code></pre>
<p>上面代码首先仍然是找到 <code>antd</code>  那行，然后在 <code>specifiers</code>  这个数组的最后一位添加一个新的节点，表现在转换后的 js 代码上就是，新增了一个 <code>Select</code>  的引入：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">import</span> React <span class="hljs-keyword">from</span> <span class="hljs-string">"react"</span>;
<span class="hljs-keyword">import</span> { Button, Input, Select } <span class="hljs-keyword">from</span> <span class="hljs-string">"antd"</span>; <span class="hljs-comment">// 可以看到引入了 Select</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-15">删除节点</h3>
<p><code>delete.js</code> ：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">const</span> jf = <span class="hljs-built_in">require</span>(<span class="hljs-string">"jscodeshift"</span>);

<span class="hljs-keyword">const</span> value = <span class="hljs-string">`
import React from 'react';
import { Button, Input } from 'antd';
`</span>;

<span class="hljs-keyword">const</span> root = jf(value);
root
  .find(jf.ImportDeclaration, { <span class="hljs-attr">source</span>: { <span class="hljs-attr">value</span>: <span class="hljs-string">"antd"</span> } })
  .forEach(<span class="hljs-function">(<span class="hljs-params">path</span>) =></span> {
    jf(path).replaceWith(<span class="hljs-string">""</span>);
  });

<span class="hljs-built_in">console</span>.log(root.toSource());
<span class="copy-code-btn">复制代码</span></code></pre>
<p>删除引入 <code>antd</code>  一整行，就是这么简单。</p>
<h3 data-id="heading-16">更多 API</h3>
<p>上面所实现的<strong>增删改查</strong>其实都是多种实现方式中的一种而已，只要你对 API 很熟练，或者脑洞够大，那可就谁也拦不住了～这里我只想说，去官方的 <a href="https://github.com/facebook/jscodeshift/blob/master/src/Collection.js" target="_blank" rel="nofollow noopener noreferrer">collection</a> 及 <a href="https://github.com/facebook/jscodeshift/tree/master/src/collections" target="_blank" rel="nofollow noopener noreferrer">extensions</a> 看看你就知道有哪些 API 了，然后多尝试、多动手，总会实现你想要的效果的。</p>
<h2 data-id="heading-17">实战解析</h2>
<blockquote>
<p>技术为需求服务。</p>
</blockquote>
<h3 data-id="heading-18">明确需求</h3>
<p>在对 jscodeshift 有了初步了解之后，我们接下来做一个<strong>命令行工具</strong>来解决我在上面提出的“<strong>引入样式文件后缀名问题</strong>”，接下来会简单使用到 <a href="https://github.com/tj/commander.js" target="_blank" rel="nofollow noopener noreferrer">commander</a> ，它使 nodejs 命令行接口变得更简单～</p>
<p>我再次明确下我目前的需求：<strong>由 <code>tsc</code>  编译之后的目录，比如 <code>dist</code> ，我要将里面生成的所有 js 文件中关于样式文件的引入，比如 <code>import './style.scss'</code> ，全部转换成以 <code>.css</code>  为后缀的方式。</strong></p>
<p>该命令行工具我给它命名为：<a href="https://github.com/vortesnail/tsccss" target="_blank" rel="nofollow noopener noreferrer">tsccss</a>。</p>
<p><img alt="3.jpg" class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/df8733823d4840868a242db69cb2eeb9~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-19">搭建环境</h3>
<p>就像上面一样，我们先初始化项目，因为演示为主，所以我们就不使用 Typescript 了，就写原生 nodejs 原生模块写法，如果对项目要求较高的，也可以加上 <code>ESLint</code> 、 <code>Prettier</code>  等规范代码的工具，如果大家有兴趣，可以前往我在 github 上已经写好了的这个命令行工具 <a href="https://github.com/vortesnail/tsccss" target="_blank" rel="nofollow noopener noreferrer">tsccss</a> ，可以做个参考。</p>
<p>好的，现在我们一气呵成，按下面步骤来：</p>
<pre><code class="hljs language-bash copyable" lang="bash"><span class="hljs-comment"># 创建项目目录</span>
mkdir tsccss
<span class="hljs-built_in">cd</span> tsccss

<span class="hljs-comment"># 初始化</span>
npm init -y

<span class="hljs-comment"># 安装依赖包</span>
npm i commander globby jscodeshift --save

<span class="hljs-comment"># 创建入口文件</span>
mkdir src
<span class="hljs-built_in">cd</span> src
touch index.js
<span class="copy-code-btn">复制代码</span></code></pre>
<p>现在目录如下：</p>
<pre><code class="hljs language-bash copyable" lang="bash">|-- node_modules
|-- src
  |-- index.js
|-- package.json
<span class="copy-code-btn">复制代码</span></code></pre>
<p>接下来在 <code>package.json</code>  中找个位置加入以下代码：</p>
<pre><code class="hljs language-json copyable" lang="json">{
  <span class="hljs-attr">"main"</span>: <span class="hljs-string">"src/index.js"</span>,
  <span class="hljs-attr">"bin"</span>: {
    <span class="hljs-attr">"tsccss"</span>: <span class="hljs-string">"src/index.js"</span>
  },
  <span class="hljs-attr">"files"</span>: [<span class="hljs-string">"src"</span>]
}
<span class="copy-code-btn">复制代码</span></code></pre>
<p>其中 <code>bin</code>  字段很重要，在其他开发者下载了你这个包之后，人家在 <code>tsccss xxxxxx</code>  时就会以 node 执行后面配置的文件，即 <code>src/index.js</code> ，当然，我们的 <code>index.js</code>  还要在最顶部加上这行代码：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-meta">#! /usr/bin/env node</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这句代码解决了不同的用户 node 路径不同的问题，可以让系统动态的去查找 node 来执行你的脚本文件。</p>
<h3 data-id="heading-20">使用 commander</h3>
<p>直接在 <code>index.js</code>  中加入以下代码：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">const</span> { program } = <span class="hljs-built_in">require</span>(<span class="hljs-string">"commander"</span>);

program.version(<span class="hljs-string">"0.0.1"</span>).option(<span class="hljs-string">"-o, --out <path>"</span>, <span class="hljs-string">"output root path"</span>);

program.on(<span class="hljs-string">"--help"</span>, <span class="hljs-function">() =></span> {
  <span class="hljs-built_in">console</span>.log(<span class="hljs-string">`
  You can add the following commands to npm scripts:
 ------------------------------------------------------
  "compile": "tsccss -o dist"
 ------------------------------------------------------
`</span>);
});

program.parse(process.argv);

<span class="hljs-keyword">const</span> { out } = program.opts();
<span class="hljs-built_in">console</span>.log(out);

<span class="hljs-keyword">if</span> (!out) {
  <span class="hljs-keyword">throw</span> <span class="hljs-keyword">new</span> <span class="hljs-built_in">Error</span>(<span class="hljs-string">"--out must be specified"</span>);
}
<span class="copy-code-btn">复制代码</span></code></pre>
<p>接下来在项目根目录下，执行以下控制台命令：</p>
<pre><code class="hljs language-bash copyable" lang="bash">node src/index.js -o dist
<span class="copy-code-btn">复制代码</span></code></pre>
<p>你会发现控制台打印了 <code>dist</code> ，是的，就是 <code>-o dist</code>  的作用，简单介绍下 <code>version</code>  和 <code>option</code> 。</p>
<ul>
<li><strong>version</strong></li>
</ul>
<p><strong>作用</strong>：定义命令程序的版本号；<br>
<strong>用法示例</strong>：.version('0.0.1', '-v, --version') ；<br>
<strong>参数解析</strong>：</p>
<ol>
<li>第一个参数，版本号 <必须>；</li>
<li>第二个参数，自定义标志 <可省略>，默认为 -V 和 --version。</li>
</ol>
<ul>
<li><strong>option</strong></li>
</ul>
<p><strong>作用</strong>：用于定义命令选项；<br>
<strong>用法示例</strong>：.option('-n, --name  ', 'edit your name', 'vortesnail')；<br>
<strong>参数解析</strong>：</p>
<ol>
<li>第一个参数，自定义标志 <必须>，分为长短标识，中间用逗号、竖线或者空格分割；
（标志后面可跟参数，可以用 <> 或者 [] 修饰，前者意为必须参数，后者意为可选参数）</li>
<li>第二个参数，选项描述 <省略不报错>，在使用 --help 命令时显示标志描述；</li>
<li>第三个参数，选项参数默认值，可选。</li>
</ol>
<p>所以大家还可以试试这两个命令：</p>
<pre><code class="hljs language-bash copyable" lang="bash">node src/index.js --version
node src/index.js --<span class="hljs-built_in">help</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-21">读取 dist 下 js 文件</h3>
<p><code>dist</code>  目录是假定我们要去做样式文件后缀名替换的文件根目录，现在需要使用 <code>globby</code>  工具自动读取该目录下的所有 js 文件路径，在顶部需要引入两个函数：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">const</span> { resolve } = <span class="hljs-built_in">require</span>(<span class="hljs-string">"path"</span>);
<span class="hljs-keyword">const</span> { sync } = <span class="hljs-built_in">require</span>(<span class="hljs-string">"globby"</span>);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>然后在下面继续追加代码：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">const</span> outRoot = resolve(process.cwd(), out);

<span class="hljs-built_in">console</span>.log(<span class="hljs-string">`tsccss --out <span class="hljs-subst">${outRoot}</span>`</span>);

<span class="hljs-comment">// Read output files</span>
<span class="hljs-keyword">const</span> files = sync(<span class="hljs-string">`<span class="hljs-subst">${outRoot}</span>/**/!(*.d).{ts,tsx,js,jsx}`</span>, {
  <span class="hljs-attr">dot</span>: <span class="hljs-literal">true</span>,
}).map(<span class="hljs-function">(<span class="hljs-params">x</span>) =></span> resolve(x));
<span class="hljs-built_in">console</span>.log(files);
<span class="copy-code-btn">复制代码</span></code></pre>
<p><code>files</code>  即 <code>dist</code>  目录下所有 js 文件路径，我们故意在该目录下新建几个任意的 js 文件，再执行下 <code>node src/index.js -o dist</code> ，看看控制台是不是正确打印出了这些文件的绝对路径。</p>
<h3 data-id="heading-22">编写替换方法</h3>
<p>因为有了前面的<strong>增删改查</strong>的铺垫，其实现在这一步已经很简单了，思路就是：</p>
<ul>
<li>找到所有类型为 <code>ImportDeclaration</code>  的节点；</li>
<li>运用正则判断该节点的 <code>source.value</code>  是否以 <code>.scss</code>  或 <code>.less</code>  结尾；</li>
<li>若正则匹配到了，我们就运用正则的一些用法将其后缀替换为 <code>.css</code> 。</li>
</ul>
<p>就这么简单，我们直接引入 jscodeshift ：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">const</span> jscodeshift = <span class="hljs-built_in">require</span>(<span class="hljs-string">"jscodeshift"</span>);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>然后追加以下代码：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">transToCSS</span>(<span class="hljs-params">str</span>) </span>{
  <span class="hljs-keyword">const</span> jf = jscodeshift;
  <span class="hljs-keyword">const</span> root = jf(str);
  root.find(jf.ImportDeclaration).forEach(<span class="hljs-function">(<span class="hljs-params">path</span>) =></span> {
    <span class="hljs-keyword">let</span> value = <span class="hljs-string">""</span>;
    <span class="hljs-keyword">if</span> (path && path.node && path.node.source) {
      value = path.node.source.value;
    }
    <span class="hljs-keyword">const</span> regex = <span class="hljs-regexp">/(scss|less)('|"|`)?$/i</span>;
    <span class="hljs-keyword">if</span> (value && regex.test(value.toString())) {
      path.node.source.value = value
        .toString()
        .replace(regex, <span class="hljs-function">(<span class="hljs-params">_res, _$<span class="hljs-number">1</span>, $<span class="hljs-number">2</span></span>) =></span> ($<span class="hljs-number">2</span> ? <span class="hljs-string">`css<span class="hljs-subst">${$<span class="hljs-number">2</span>}</span>`</span> : <span class="hljs-string">"css"</span>));
    }
  });

  <span class="hljs-keyword">return</span> root.toSource();
}
<span class="copy-code-btn">复制代码</span></code></pre>
<p>可以看到，该方法直接返回了转换后的 js 代码，是可以直接写入源文件的内容。</p>
<h3 data-id="heading-23">读写文件</h3>
<p>拿到文件路径 <code>files</code>  后，需要 node 原生模块 <code>fs</code>  来帮助我们读写文件，这部分代码很简单，思路就是：<strong>读 js 文件，将文件内容转换为 AST 做节点值替换，再转为 js 代码，最后写回该文件</strong>，就 OK 了。</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">const</span> { readFileSync, writeFileSync } = <span class="hljs-built_in">require</span>(<span class="hljs-string">"fs"</span>);

<span class="hljs-comment">// ...</span>

<span class="hljs-keyword">const</span> filesLen = files.length;
<span class="hljs-keyword">for</span> (<span class="hljs-keyword">let</span> i = <span class="hljs-number">0</span>; i < filesLen; i += <span class="hljs-number">1</span>) {
  <span class="hljs-keyword">const</span> file = files[i];
  <span class="hljs-keyword">const</span> content = readFileSync(file, <span class="hljs-string">"utf-8"</span>);
  <span class="hljs-keyword">const</span> resContent = transToCSS(content);
  writeFileSync(file, resContent, <span class="hljs-string">"utf8"</span>);
}
<span class="copy-code-btn">复制代码</span></code></pre>
<p>现在你到 <code>dist</code>  目录下的 <code>index1.js</code> 、 <code>index2.js</code>  文件中，随便输入以下内容，以便查看效果：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">import</span> <span class="hljs-string">"style.scss"</span>;
<span class="hljs-keyword">import</span> <span class="hljs-string">"style.less"</span>;
<span class="hljs-keyword">import</span> <span class="hljs-string">"style.css"</span>;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>然后最后一次执行我们的命令：</p>
<pre><code class="hljs language-bash copyable" lang="bash">node src/index.js -o dist
<span class="copy-code-btn">复制代码</span></code></pre>
<p>再看刚才的 <code>index1.js</code>  或 <code>index2.js</code> ，是不是全部正确替换了：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">import</span> <span class="hljs-string">"style.css"</span>;
<span class="hljs-keyword">import</span> <span class="hljs-string">"style.css"</span>;
<span class="hljs-keyword">import</span> <span class="hljs-string">"style.css"</span>;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>舒服了～ 😊</p>
<p>上面的代码还是可以优化很多地方的，比如大家还可以写一些额外的代码来统计替换的位置、数量、文件修改数量等，这些都可以在控制台打印出来，在别人使用时也能得到较好的反馈～甚至替换的正则方法也可以再做改进，看大家的了！</p>
<h2 data-id="heading-24">最后想说的</h2>
<p>虽然上面的实战是非常简单的一种 AST 用法，但是这篇文章的主要作用就是能带大家入门，利用这种思维去解决工作或学习中遇到的一些问题，在我看来，有了对某方法的事物认知之后，你的解决问题的方式就会无形之中多了一种。其实技术在某种程度来说并不是最重要的，重要的是<strong>对技术的认知</strong>。</p>
<p>毕竟，你不知道某个东西，利用它的想法都不会产生，但是你知道了，无论技术实现再难，也总是可以攻克的！</p>
<p>最后感谢大家能认真读到这里，文章中有错误的地方，欢迎探讨。</p>
<blockquote>
<p>本文产出工具：<a href="https://github.com/vortesnail/tsccss" target="_blank" rel="nofollow noopener noreferrer">github/tsccss</a> ，欢迎使用，star🌟。<br>
本人博客地址：<a href="https://github.com/vortesnail/blog" target="_blank" rel="nofollow noopener noreferrer">github/blog</a> ，若此文对你有帮助，赏个 star🌟，谢谢老爷了！</p>
</blockquote>
<p>参考文章：<br>
<a href="https://github.com/tj/commander.js/blob/master/Readme_zh-CN.md" target="_blank" rel="nofollow noopener noreferrer">commander</a><br>
<a href="https://juejin.cn/post/6923936548027105293" target="_blank">像玩 jQuery 一样玩 AST</a><br>
<a href="https://github.com/whxaxes/blog/issues/10" target="_blank" rel="nofollow noopener noreferrer">jscodeshift 简易教程</a></p></div> <div class="image-viewer-box" data-v-78c9b824><!----></div>  
</div>
            