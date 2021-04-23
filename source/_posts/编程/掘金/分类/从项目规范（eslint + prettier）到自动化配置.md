
---
title: '从项目规范（eslint + prettier）到自动化配置'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/5d62d3c81b444b76883f82d6315b49f9~tplv-k3u1fbpfcp-zoom-1.image'
author: 掘金
comments: false
date: Thu, 22 Apr 2021 16:58:45 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/5d62d3c81b444b76883f82d6315b49f9~tplv-k3u1fbpfcp-zoom-1.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h2 data-id="heading-0">前言：为什么需要项目规范</h2>
<p>我们学习编程的方式各有不同，对于知识的理解也各有不同，在一天天的编程过后，每个人都养成了自己的代码习惯和理解。</p>
<p>代码习惯和理解的差异，导致了团队中会出现各种各样的 “规范” 代码。在你查看自己的代码时，你可能会觉得自己的代码看起来比较标准，只是有点乱。但是在团队成员查看你的代码时，他心里可能会这么想：wtf，他写的代码怎么是这个样子。这种风格的代码就好像是一个公司律师用 excel 规范自动格式化的沙拉食谱，看起来一点都不靠谱。</p>
<p><img alt="image" class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/5d62d3c81b444b76883f82d6315b49f9~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p>这种差异性导致了团队协作的效率低下，也影响了项目的健壮性和可维护性。所以，我们需要对代码风格进行规范。这种规范不仅可以使代码风格保持统一，并且可以在代码运行之前就检测出一些错误和 bug，提高协作开发效率。</p>
<p>而前端开发人员最常用的 Javascript 最初设计出来是只是为了解决一些简单的网页互动，是一种弱类型、基于原型的语言。</p>
<p>Javascript 拥有其它语言所没有的灵活性，这种灵活性带来了代码效率的提升，但相应也使得代码编写具有很大的随意性。另外 Javascript 的隐式类型转换规则混乱，允许同名函数的重复定义，这就增加了代码中存在隐患的可能性。</p>
<blockquote>
<p>冷笑话：Javascript 权威指南和 Javascript 语言精粹的厚度区别。</p>
</blockquote>
<p><img alt="image" class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/9e30fa19a95940b4b55cfca24b84fb9a~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p>如果能够在代码提交测试之前发现这些潜在的错误，就能够极大地减轻测试人员的压力，减少软件项目的除错成本。可是 Javascript 作为解释型语言，解释器被内嵌在对应的客户端，对此表示无能为力，这个任务只能由专用的代码检查工具完成。</p>
<p>在接下来，我会针对上述的这些问题展开讲述，首先介绍解决这些问题的工具，然后再介绍借助这项工具来解决团队规范和错误预检问题的步骤方法，最后再用一行命令来整合这些复杂的步骤，将使用门槛降到最低。</p>
<h2 data-id="heading-1">Eslint 和 Prettier</h2>
<h3 data-id="heading-2">lint</h3>
<p>lint 是最著名的 C 语言工具之一，是由贝尔实验室 SteveJohnson 于 1979 在 PCC(PortableC Compiler) 基础上开发的静态代码分析，一般由 UNIX 系统提供。</p>
<p>lint 被用于检查 C 程序中潜在的错误，包括（但不限于）可疑的类型组合、未使用的变量、不可达的代码以及不可移植的代码。lint会产生一系列程序员有必要从头到尾仔细阅读的诊断信息。使用lint的好处是：</p>
<ol>
<li>它可以检查出被编译器漏掉的错误;</li>
<li>可以关联很多文件进行错误的检查和代码分析,具有较强大灵活性</li>
</ol>
<blockquote>
<p>lint 应该也算是 lint 界的老祖宗了。</p>
</blockquote>
<h3 data-id="heading-3">Eslint</h3>
<p>有个叫 Nicholas C. Zakas 的人在 2013 年推出了一个 Javascript 的 lint 工具，而 Javascript 也称作 ECMAScript（简称 ES），所以这个工具被叫做 ESlint。</p>
<p><img alt="image" class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/2811b3f7b58a4b2da805e355dd87b8d4~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p>ESLint 是在 ECMAScript/JavaScript 代码中识别和报告模式匹配的工具，它的目标是保证代码的一致性和避免错误。</p>
<p>Eslint 可以在运行代码前就发现一些语法错误和潜在的 bug，极大地减轻测试人员的压力，减少软件项目的除错成本。同时，Eslint 允许开发者通过 rules 定义自己的代码规范，所以非常适合用于制定团队代码规范。</p>
<h3 data-id="heading-4">Prettier</h3>
<p><img alt="image" class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/8aef0cff0c404a6d8aaec3c539445f9e~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p>Prettier 是一款代码格式化工具，用于检测代码中的格式问题，比如单行代码长度、tab长度、空格、逗号表达式等。在功能职责上，ESlint 偏向于把控项目的代码质量，而 Prettier 更偏向于统一项目的编码风格。</p>
<p>在 ESlint 推出 <code>--fix</code> 参数前，ESLint 并没有自动化格式代码的功能，要对一些格式问题做批量格式化只能用 Prettier 这样的工具。并且，Prettier 在代码风格的检测上比 ESlint 更全面，所以两者通常是结合在一起使用的。</p>
<h2 data-id="heading-5">常见的标准规范</h2>
<p>在介绍规范之前，可以先使用 <code>npm i eslint prettier -g</code> 命令全局安装 <code>eslint</code> 和 <code>prettier</code>，在后面的教程中都会使用到这两个全局包。</p>
<h3 data-id="heading-6">ESlint 推荐的规范</h3>
<p>ESlint 在默认情况下是不开启任何自定义规则校验，只对错误的 ES5 语法和标准的语法错误进行检测，比如 <code>const</code> 这种 ES6 语法，还有莫名其妙的分号（如下图）。</p>
<p><img alt="image" class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/2a96cd4a7a1d49df95f18b833343bbc4~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p>当我们在项目目录下新增 <code>eslintrc.js</code> 文件，并写入以下内容后，将会启用 ESlint 推荐的规范：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-built_in">module</span>.exports = &#123;
  <span class="hljs-attr">root</span>: <span class="hljs-literal">true</span>,
  <span class="hljs-attr">extends</span>: <span class="hljs-string">'eslint:recommended'</span>
&#125;;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>在 ESlint 的推荐规范中，会有一些内置的规则，比如定义后未使用的变量将会抛出错误，使用常量作为循环条件也会抛出错误（如下图）。</p>
<p><img alt="image" class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/677ede6a9ea34d8ebdd7f19c0811fe33~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p>ESlint 的推荐规范可以避免掉一些错误，比如上述两个错误就可以在运行前被检查到并解决，更多详细规范请参考 <a href="https://eslint.org/docs/rules/" target="_blank" rel="nofollow noopener noreferrer">ESlint Recommend</a>。</p>
<h3 data-id="heading-7">standard</h3>
<p>standard 是基于 ESlint Recommend 衍生出来的更严格的规范。这个规范和 recommended 大概有 88 处不同，主要是 recommended 很多都是 off, standard 是 error, 比如 <code>单行代码块两边加空格</code>、<code>禁止使用分号结尾</code>。</p>
<p>下面的代码在 <code>recommended</code> 规范下不会报错，而在 <code>standard</code> 规范中会报错。</p>
<blockquote>
<p>recommended 规范</p>
</blockquote>
<p><img alt="image" class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/eebd983c9fd1448499a36a1401d001d2~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<blockquote>
<p>standard 规范</p>
</blockquote>
<p><img alt="image" class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/d24dbefa409047af94c8bee7fd04112e~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p>先使用 <code>npm i standard eslint-plugin-standard eslint-config-standard -D</code> 命令安装 <code>standard</code> 插件，然后在 <code>eslintrc.js</code> 文件中写入以下内容后，将会启用 standard 规范：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-built_in">module</span>.exports = &#123;
  <span class="hljs-attr">root</span>: <span class="hljs-literal">true</span>,
  <span class="hljs-attr">extends</span>: [<span class="hljs-string">'standard'</span>]
&#125;;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>standard 会比 recommended 更加严格，在代码风格上也做了一些限制。不过它的用户群体也是比较多的，也不乏一些大家耳熟能详的。（如下图）</p>
<p><img alt="image" class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/d1dec999597a4f6dafdcc50ab6ff5224~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p>详细规范请参考 <a href="https://standardjs.com/rules-zhcn.html" target="_blank" rel="nofollow noopener noreferrer">ESlint Standard</a>。</p>
<h3 data-id="heading-8">airbnb</h3>
<p>airbnb 规范是最严格的 ESlint 规范，列出下面几点比较明显的区别：</p>
<ol>
<li>默认必须要分号，而eslint默认不添加分号</li>
<li>不能使用for循环，推荐使用数组自带的 API 完成遍历工作。</li>
<li>当你必须使用函数表达式（或传递一个匿名函数）时，使用箭头函数符号。</li>
</ol>
<p>除了这些以外，还有更多严格的规则，可以查看 <a href="https://github.com/yuche/javascript" target="_blank" rel="nofollow noopener noreferrer">Airbnb 规范</a>。</p>
<h2 data-id="heading-9">在项目中配置 Eslint + Prettier</h2>
<p>由于 Eslint 和 Prettier 存在一些相同的规则，当同一个规则设置不同时，就会出现很诡异的现象：使用 prettier 格式化的代码，无法通过 eslint 校验。</p>
<p>下面，我们就以一份 <code>前端代码规范</code> 为例，为一个项目配置一套完整的 <code>ESlint + Prettier</code> 规范。</p>
<h3 data-id="heading-10">配置 .eslintrc.js</h3>
<p>我们新建一个 <code>eslintrc.js</code> 文件，写入以下内容，作为我们的初始化配置。（如下）</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-built_in">module</span>.exports = &#123;
  <span class="hljs-attr">root</span>: <span class="hljs-literal">true</span> <span class="hljs-comment">// 表示该文件为根配置文件</span>
&#125;;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>在上一章的示例代码中，我们发现 eslint 默认只能识别 <code>es5</code> 的语法，所以我们先配置 <code>env</code> 属性，让 <code>eslint</code> 支持到 <code>es6</code> 语法，并且我们设置环境为 <code>browser</code>（浏览器） 或 <code>node</code>（如下）。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-built_in">module</span>.exports = &#123;
  <span class="hljs-attr">root</span>: <span class="hljs-literal">true</span>,

  <span class="hljs-attr">env</span>: &#123;
    <span class="hljs-attr">browser</span>: <span class="hljs-literal">true</span>,
    <span class="hljs-attr">node</span>: <span class="hljs-literal">true</span>,
    <span class="hljs-attr">es6</span>: <span class="hljs-literal">true</span>,
  &#125;,

  <span class="hljs-attr">extends</span>: <span class="hljs-string">'eslint:recommended'</span>
&#125;;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>如果使用 <code>standard</code> 标准则不需要额外设置，<code>standard</code> 支持最新的 ECMAScript 特性。而实验性的特性，则需要添加 <code>babel-eslint</code> 解析器。</p>
<p>所以，这里我们直接配置 <code>standard</code> 标准和 <code>babel-eslint</code> 解析器，再加上一些自定义规则后，最后配置的规则如下：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-built_in">module</span>.exports = &#123;
  <span class="hljs-attr">root</span>: <span class="hljs-literal">true</span>,

  <span class="hljs-attr">parserOptions</span>: &#123;
    <span class="hljs-attr">parser</span>: <span class="hljs-string">'babel-eslint'</span>, <span class="hljs-comment">// 解析一些最新的 es 语法</span>
    <span class="hljs-attr">sourceType</span>: <span class="hljs-string">'module'</span>  <span class="hljs-comment">// 模块为 ECMAScript 模块</span>
  &#125;,

  <span class="hljs-attr">extends</span>: [<span class="hljs-string">'standard'</span>], <span class="hljs-comment">// 使用 standard 标准</span>

  <span class="hljs-attr">rules</span>: &#123;
    <span class="hljs-string">'no-debugger'</span>: <span class="hljs-string">'error'</span>, <span class="hljs-comment">// 禁止在代码中使用 debugger</span>
    <span class="hljs-attr">quotes</span>: [<span class="hljs-string">'error'</span>, <span class="hljs-string">'single'</span>], <span class="hljs-comment">// 单引号</span>
    <span class="hljs-attr">semi</span>: [<span class="hljs-string">'error'</span>, <span class="hljs-string">'always'</span>] <span class="hljs-comment">// 代码需要以分号结尾</span>
  &#125;
&#125;;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>在 <code>ESlint</code> 规范文件配置完成后，我们再来添加 <code>Prettier</code> 配置文件，新建 <code>.prettierrc.js</code> 文件，添加以下内容：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-built_in">module</span>.exports = &#123;
  <span class="hljs-attr">printWidth</span>: <span class="hljs-number">800</span>, <span class="hljs-comment">// 单行宽度限制</span>
  <span class="hljs-attr">tabWidth</span>: <span class="hljs-number">2</span>, <span class="hljs-comment">// tab 使用两个空格</span>
  <span class="hljs-attr">useTabs</span>: <span class="hljs-literal">false</span>, <span class="hljs-comment">// 不使用制表符缩进，使用空格缩进</span>
  <span class="hljs-attr">semi</span>: <span class="hljs-literal">true</span>, <span class="hljs-comment">// 代码需要分号结尾</span>
  <span class="hljs-attr">singleQuote</span>: <span class="hljs-literal">true</span>, <span class="hljs-comment">// 单引号</span>
  <span class="hljs-attr">bracketSpacing</span>: <span class="hljs-literal">true</span>, <span class="hljs-comment">// 对象左右两侧需要空格</span>
  <span class="hljs-attr">jsxBracketSameLine</span>: <span class="hljs-literal">false</span>, <span class="hljs-comment">// html 关闭标签换行</span>
  <span class="hljs-attr">arrowParens</span>: <span class="hljs-string">'avoid'</span>, <span class="hljs-comment">// 单参数的箭头函数参数不需要括号</span>
  <span class="hljs-attr">proseWrap</span>: <span class="hljs-string">'never'</span>, <span class="hljs-comment">// 参考 https://prettier.io/docs/en/options.html#prose-wrap</span>
  <span class="hljs-attr">trailingComma</span>: <span class="hljs-string">'none'</span> <span class="hljs-comment">// 参考 https://prettier.io/docs/en/options.html#trailing-commas</span>
&#125;;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>在配置完成后，我们新建一个文件，测试一下效果。在 <code>src</code> 目录下新建文件 <code>test.js</code>，填入以下内容：</p>
<p><img alt="image" class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/53ec1660449c4383b7e1786ea14b8ed3~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-11">使用自动格式化</h3>
<p>从上面可以看出，文件并不符合我们制定的 eslint 规范，我们下面分别使用 eslint 格式化和 prettier 格式化功能来尝试修正。</p>
<p>首先，我们在命令行输入 <code>eslint --fix src/test.js</code>，然后看看效果（如下图）</p>
<p><img alt="image" class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/31fcc158f334407282da76d0872672e4~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p>我们可以看到，多余的空格被删除了，双引号被换成了双引号，赋值运算符的左右两侧也被加上了空格。</p>
<p>接下来，我们先把文件还原，然后使用 <code>prettier -w src/test.js</code> 命令进行格式化，效果如下图：</p>
<p><img alt="image" class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/11c73e2f9f7a416e8b84911524b66804~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p>从上图可以看出，由于我们设置的 <code>eslint</code> 和 <code>prettier</code> 的规则一致，所以格式化后的文件也是高度相似的。</p>
<p>这样一来，我们就完成了代码规范格式的统一。</p>
<h2 data-id="heading-12">vscode 插件</h2>
<p>大家从上面的示例代码中可以看出，编写不合规范的代码会直接在编辑器中报出错误，这是因为上面的示例代码使用 <code>vscode</code> 展示，并安装了一些插件来辅助开发。</p>
<p>下面，我们就来介绍一下这些插件。</p>
<p>我们先通过 <code>vscode</code> 安装 <code>ESLint</code> 插件（如下图）</p>
<p><img alt="image" class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/c9666bde38a74701a1d19939209df183~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p>在安装了 <code>ESLint</code> 插件后，插件会读取目录下的 <code>eslint</code> 配置文件，然后对代码中的错误进行检查后提示出来（如下图）。</p>
<p><img alt="image" class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/db6e9d345cf740b3964008303dc1d54e~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p>如果我们在 <code>vscode</code> 中设置了下面这个属性的话，在保存文件的时候将会自动格式化代码。（如下图）</p>
<p><img alt="image" class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/8ae29e987fe14f148484e6a3cc015de2~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p>下面，我们可以再安装 <code>Prettier</code> 插件（如下图）。</p>
<p><img alt="image" class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/ce0dc767c98b4c0290df1a074aa03728~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p>在安装好插件后，使用键盘组合键 <code>shift + command/ctrl + p</code> 唤起设置，然后输入 <code>Format Selection With...</code> 后，按回车键，在选项中选择 <code>Prettier</code> 即可（如下图）。</p>
<p><img alt="image" class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/290a826895c0437b9d048a688dc32db7~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p>在设置完成后，使用组合键 <code>shift + option/alt + f</code> 即可完成对文件的格式化。</p>
<p>这两个插件还有更多的功能，大家可以自行探索一下。</p>
<h3 data-id="heading-13">插件的三两事</h3>
<blockquote>
<p>如果你对 vscode 的插件比较熟悉，可以跳过本章节内容。</p>
</blockquote>
<p>在 <code>vscode</code> 的插件安装过程中，有很多童鞋反馈过问题，这里给出一些常见问题的解决方案。</p>
<h4 data-id="heading-14">插件不工作</h4>
<ol>
<li>全局安装 <code>npm i eslint prettier -g</code></li>
<li>安装好 <code>vscode</code> 插件后，重启 <code>vscode</code></li>
<li>如果还是不行的话，升级 <code>vscode</code></li>
</ol>
<h4 data-id="heading-15">插件未启用</h4>
<p>新版 <code>vscode</code> 需要手动启用 <code>eslint</code> 插件，在右下角查看 eslint 工作状态，可以点击开启。（如下图）</p>
<p><img alt="image" class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/5d941c36a84d46df93aa6da7332fb14d~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<h4 data-id="heading-16">启用后不工作</h4>
<p>右下角查看 eslint 工作状态，点击会输出日志。（如下图）</p>
<p><img alt="image" class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/3a0759a7902c45d8875804c25b860f40~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p>根据输出日志，进行修复，比如上图就是缺少对应插件，安装即可。</p>
<h4 data-id="heading-17">保存没有按照 eslint 的规则修复</h4>
<p>这可能是因为你的 <code>vscode</code> 开启了保存自动格式化（代码格式化），先打开 <code>首选项 > 设置</code>，搜索 <code>format on save</code>，然后关闭这个选项（如下图）</p>
<p><img alt="image" class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/0df6ce7c4fae4cd6ac954b0c90c8d0bb~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<h4 data-id="heading-18">正常工作</h4>
<p>正常工作的 <code>eslint</code> 和 <code>prettier</code> 插件状态如下图所示。</p>
<p><img alt="image" class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/b1fe2b7c93c74049a5b910e3a1168ec3~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-19">在提交时自动检测和格式化代码</h2>
<p>在项目开发过程中，自动格式化并不总是让人安心的，因为并不是项目组的所有成员都会使用 <code>vscode</code> 插件来做自动格式化。</p>
<p>这样的情况会导致有一些不规范的代码被提交到服务端，依然会造成团队规范不一致的问题，这个时候就需要用到提交时自动检测和格式化代码的功能。</p>
<p>接下来，我们将使用 <code>husky</code> 来进行代码提交时的自动检测工作。</p>
<p>先使用 <code>npm i husky -D</code> 安装依赖，在依赖完成完成后，我们需要使用下面这条命令初始化 <code>husky</code>（如下）</p>
<pre><code class="hljs language-bash copyable" lang="bash">npx husky install && npx husky <span class="hljs-built_in">set</span> .husky/pre-commit <span class="hljs-string">"npm run pre-commit"</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>上面的命令是初始化 <code>git hook</code>，在 <code>git commit</code> 之前会先执行 <code>pre-commit</code> 命令。</p>
<p>所以，我们还需要在项目的 <code>package.json</code> 中，添加 <code>pre-commit</code>，这个命令运行时进行 <code>eslint</code> 检测（如下）。</p>
<pre><code class="hljs language-json copyable" lang="json"><span class="hljs-string">"scripts"</span>: &#123;
  <span class="hljs-attr">"pre-commit"</span>: <span class="hljs-string">"eslint src"</span>
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>接下来，我们运行 <code>git add .</code> 和 <code>git commit -m 'test'</code> 命令，尝试提交代码，会发现提交失败，命令行输出如下图。</p>
<p><img alt="image" class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/48694e3da7c942478ef7cd5ebccf6ec5~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p>如上图所示，在提交时检测到代码不符合 <code>eslint</code> 规范，提交失败了。</p>
<p>如果我们希望在检测错误的同时，自动修复 <code>eslint</code> 语法错误，则需要用到 <code>lint-staged</code>，使用 <code>npm i lint-staged -D</code> 先进行安装，然后在 <code>package.json</code> 中修改 <code>pre-commit</code> 命令，再添加以下内容。</p>
<pre><code class="hljs language-json copyable" lang="json"><span class="hljs-string">"scripts"</span>: &#123;
  <span class="hljs-attr">"pre-commit"</span>: <span class="hljs-string">"lint-staged"</span>
&#125;,
<span class="hljs-string">"lint-staged"</span>: &#123;
  <span class="hljs-attr">"src/**"</span>: [
    <span class="hljs-string">"eslint --fix"</span>
  ]
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>接下来，我们再次运行 <code>git add .</code> 和 <code>git commit -m 'test'</code> 命令，尝试提交代码，输出如下图。</p>
<p><img alt="image" class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/4b4a40545cf54703a74ae196aca9a9e0~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p>从上图可以看出，在运行 <code>lint-staged</code> 命令后，会通过 <code>eslint --fix</code> 自动将不符合规格的代码正确格式化。</p>
<p>这样一来，代码提交时的自动检测和格式化代码工作就完成了。</p>
<h2 data-id="heading-20">使用脚手架，将配置自动化</h2>
<h3 data-id="heading-21">手动配置的问题</h3>
<p>在完成上述配置后，似乎已经大功告成，马上可以走在规范编码的愉快道路上，但是并没有。</p>
<p>我们仔细梳理一下会发现，我们需要在某个新项目中配置代码规范时，需要进行以下繁琐的步骤。</p>
<ol>
<li>安装 Eslint。</li>
<li>根据项目类型安装对应的 ESLint 规则配置 npm 包。</li>
<li>根据项目类型安装相关的插件、解析器等。</li>
<li>根据项目类型配置 .eslintrc .prettierrc 文件。</li>
<li>安装代码提交检查 + 自动格式化工具。 husky + lint-staged</li>
<li>配置 package.json。</li>
<li>测试及修复问题。</li>
</ol>
<p>这些繁琐的步骤会耗费大量的时间，并且可能还会出现一些错误需要额外花时间去排查。这样的流程对于个人来说可能是个比较好的学习机会，但是对于团队来说确实是个低效的协作方式。</p>
<p>所以，我们可以借助一些工具来帮忙完成上述工作，这个工具可以根据配置选择，生成对应的规范配置，并安装可以互相兼容的依赖包。</p>
<h3 data-id="heading-22">使用脚手架进行自动配置</h3>
<p>我们先使用 <code>npm i standard-config-cli -g</code> 命令全局安装脚手架工具，然后在对应的目录下运行 <code>jgxl standard</code> 命令。</p>
<p>这里我们以 <code>vue + typescript</code> 命令为例，选择的配置如下图。</p>
<p><img alt="image" class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/06befdc8cb1644509287cb587766267c~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p>在初始化完成后，对应的几个配置文件内容如下：</p>
<blockquote>
<p>.eslintrc.js</p>
</blockquote>
<p><img alt="image" class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/e3893857b0884a358706e67e882c89cc~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<blockquote>
<p>.prettierrc.js</p>
</blockquote>
<p><img alt="image" class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/4ffd0e309d8447fdaa155ab4c199c8ce~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<blockquote>
<p>package.json</p>
</blockquote>
<p><img alt="image" class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/a78c8eb96f734054986ca5f4e7069724~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p>从上面可以看出，我们的规范配置会根据所选配置，生成对应的规范配置文件，并且已经安装了相关版本的依赖。</p>
<p>作为团队成员，不需要关心这些规范的细枝末节，只需要进行核心业务开发即可。</p>
<blockquote>
<p>TIPS：<code>自动修正</code> 功能只能修正部分代码风格规范，对于一些可能产生隐患的代码问题不会自动修正（例如：定义而未使用的变量）。</p>
</blockquote>
<h2 data-id="heading-23">小结</h2>
<p>在代码风格规范的争论上，每个人都有自己的理解，永远没有正确的答案。把时间用于细枝末节上争论，不如多把关注点聚焦在核心业务上。</p>
<p>而不管怎样争论，总归会选择一种风格。在这个方面，也需要在个人语义和普适价值上做一个权衡。</p>
<p>所以，选择一份前端规范标准（如 <code>standard</code>），然后保持吧。把时间留下来解决其他有意义的问题！(^____^)/</p>
<p>参考资料：</p>
<ul>
<li><a href="http://www.ruanyifeng.com/blog/2011/06/10_design_defects_in_javascript.html" target="_blank" rel="nofollow noopener noreferrer">Javascript的10个设计缺陷</a></li>
<li><a href="https://eslint.org/" target="_blank" rel="nofollow noopener noreferrer">eslint</a></li>
<li><a href="https://standardjs.com/" target="_blank" rel="nofollow noopener noreferrer">standard</a></li>
<li><a href="https://prettier.io/" target="_blank" rel="nofollow noopener noreferrer">prettier</a></li>
<li><a href="https://juejin.cn/post/6844903621805473800" target="_blank">使用ESLint+Prettier来统一前端代码风格</a></li>
<li><a href="https://tech.meituan.com/2019/08/01/eslint-application-practice-in-medium-and-large-teams.html" target="_blank" rel="nofollow noopener noreferrer">ESLint 在中大型团队(美团)的应用实践</a></li>
<li><a href="https://medium.com/the-node-js-collection/why-and-how-to-use-eslint-in-your-project-742d0bc61ed7" target="_blank" rel="nofollow noopener noreferrer">Why (and how) to use eslint in your project</a></li>
<li><a href="https://97-things-every-x-should-know.gitbooks.io/97-things-every-programmer-should-know/content/en/thing_04/" target="_blank" rel="nofollow noopener noreferrer">Automate Your Coding Standard</a></li>
</ul>
<h2 data-id="heading-24">最后一件事</h2>
<p>如果您已经看到这里了，希望您还是点个赞再走吧~</p>
<p>您的点赞是对作者的最大鼓励，也可以让更多人看到本篇文章！</p>
<p>如果觉得本文对您有帮助，请帮忙在 <a href="https://github.com/a1029563229/Blogs" target="_blank" rel="nofollow noopener noreferrer">github</a> 上点亮 <code>star</code> 鼓励一下吧！</p></div> <div class="image-viewer-box" data-v-78c9b824><!----></div>  
</div>
            