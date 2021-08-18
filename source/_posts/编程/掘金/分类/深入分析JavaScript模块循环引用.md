
---
title: '深入分析JavaScript模块循环引用'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/535caaf3fad8437dabf54199226f2e99~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Mon, 16 Aug 2021 22:54:23 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/535caaf3fad8437dabf54199226f2e99~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h2 data-id="heading-0">背景</h2>
<p>大力教育的在线教室中台提供封装了核心能力的教室 SDK，业务方基于教室 SDK 开发面向用户的在线教室 App。最近对教室 SDK 做一次比较大的改动时，我遇到了一个懵逼的问题。这个问题耗费了我 3 天左右时间，让我压力一度大到全身发热。当时虽然解决了问题，但并没有很理解原因。直到一个多月后，才有时间做一些更深入的分析，并写下这篇文章。</p>
<p>当时的情况是，业务方 App 工程能通过 TypeScript 编译，但在运行时会报错。就不同的使用教室 SDK 的方式，报错有两种。图 1 为在业务方 App 工程里正常安装教室 SDK 后进行调试时的报错；图 2 为在业务方 App 工程里 yarn link 教室 SDK 后进行调试时的报错。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/535caaf3fad8437dabf54199226f2e99~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>图 1</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/947cafbc71b645b0a2812f59bea1c80b~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>图 2</p>
<p>在分析这个问题前，需要先分析一下 JS（JavaScript）的模块机制。</p>
<h2 data-id="heading-1">CommonJS vs ES6 模块</h2>
<p>CommonJS 与 ES6（ECMAScript 6）模块有什么区别呢？《ECMAScript 6 入门教程 》[1]一书在“Module 的加载实现”章节指出两个模块体系有三个重大差异。个人觉得这三个差异基本是错误的，给大家造成了不少误解。后面再讲质疑的理由，这里先抛出我总结的几点差异：</p>
<ul>
<li>CommonJS 模块由 JS 运行时实现，ES6 模块借助 JS 引擎实现；ES6 模块是语言层面的底层的实现，CommonJS 模块是之前缺失底层模块机制时在上层做的弥补。从报错信息可以察觉这个差异。</li>
<li>CommonJS 模块同步加载并执行模块文件，ES6 模块提前加载并执行模块文件。CommonJS 模块在执行阶段分析模块依赖，采用深度优先遍历（depth-first traversal），执行顺序是父 -> 子 -> 父；ES6 模块在预处理阶段分析模块依赖，在执行阶段执行模块，两个阶段都采用深度优先遍历，执行顺序是子 -> 父。</li>
<li>CommonJS 模块循环引用使用不当一般不会导致 JS 错误；ES6 模块循环引用使用不当一般会导致 JS 错误。</li>
<li>CommonJS 模块的导入导出语句的位置会影响模块代码执行结果；ES6 模块的导入导出语句位置不影响模块代码语句执行结果。</li>
</ul>
<p>为了方便说明，本文把 JS 代码的运行大致分为预处理和执行两个阶段，注意，官方并没有这种说法。下面进行更细致的分析。</p>
<h3 data-id="heading-2">CommonJS 模块</h3>
<p>在 Node.js 中，CommonJS 模块[2]由 cjs/loader.js[3] 实现加载逻辑。其中，模块包装器是一个比较巧妙的设计。</p>
<p>在浏览器中，CommonJS 模块一般由包管理器提供的运行时实现，整体逻辑和 Node.js 的模块运行时类似，也使用了模块包装器。以下分析都以 Node.js 为例。</p>
<h4 data-id="heading-3">模块使用报错</h4>
<p>CommonJS 模块使用不当时，由 cjs/loader.js 抛出错误。比如：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// Node.js</span>
internal/modules/cjs/loader.js:<span class="hljs-number">905</span>
  <span class="hljs-keyword">throw</span> err;

  ^

<span class="hljs-built_in">Error</span>: Cannot find <span class="hljs-built_in">module</span> <span class="hljs-string">'./none_existed.js'</span>
Require stack:
- <span class="hljs-regexp">/Users/</span>wuliang/Documents/code/demo_module/index.js
<span class="copy-code-btn">复制代码</span></code></pre>
<p>可以看到，错误是通过 throw 语句抛出的。</p>
<h4 data-id="heading-4">模块执行顺序</h4>
<p>CommonJS 模块是顺序执行的，遇到 require 时，加载并执行对应模块的代码，然后再回来执行当前模块的代码。</p>
<p>如图 3 所示，模块 A 依赖模块 B 和 C，模块 A 被 2 个 require 语句从上往下分为 3 段，记为 A1、A2、A3。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/7a2d4bf5f848432482221cb2384e27b7~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>图 3</p>
<p>如图 4 所示，代码块执行顺序为：A1 -> B -> A2 -> C -> A3。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/01633bc3880141898faf7d25b28ce1d7~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>图 4</p>
<h4 data-id="heading-5">模块循环引用</h4>
<p>从 cjs/loader.js 的 L765、L772 和 L784 行代码可以看到，在模块执行前就会创建好对应的模块对象，并进行缓存。模块执行的过程实际是在给该模块对象计算需要导出的变量属性。因此，CommonJS 模块在启动执行时，就已经处于可以被获取的状态，这个特点可以很好地解决模块循环引用的问题。</p>
<p>如图 5 所示，模块 A 依赖模块 B，模块 B 又依赖模块 A，模块 A 和 B 分别被 require 语句从上往下分为 2 段，记为 A1、A2、B1、B2。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/b0a857ced5a04f9f846ff57a791e8c06~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>图 5</p>
<p>如图 6 所示，代码块的执行顺序为：A1 -> B1 -> B2 -> A2。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/1288730470d34e148dc26b4afe30bc05~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>图 6</p>
<h5 data-id="heading-6">使用不当的问题</h5>
<p>如果 B2 使用了 A2 导出的变量会怎么样呢？模块 A 的模块对象上不存在该变量对应的属性，获取的值为 undefined。获得 undefined 虽然不符合预期，但一般不会造成 JS 错误。</p>
<p>可以看到，由于 require 语句直接分割了执行的代码块，CommonJS 模块的导入导出语句的位置会影响模块代码语句的执行结果。</p>
<h3 data-id="heading-7">ES6 模块</h3>
<p>ES6 模块[4]借助 JS 引擎实现。JS 引擎实现了 ES6 模块的底层核心逻辑，JS 运行时需要在上层做适配。适配工作量还不小，比如实现文件的加载，具体可以看一下我发起的一个讨论[5]。</p>
<h4 data-id="heading-8">模块使用报错</h4>
<p>ES6 模块使用不当时，由 JS 引擎或 JS 运行时的适配层抛出错误。比如：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// Node.js 中报错</span>
internal/process/esm_loader.js:<span class="hljs-number">74</span>
    internalBinding(<span class="hljs-string">'errors'</span>).triggerUncaughtException

                              ^

<span class="hljs-built_in">Error</span> [ERR_MODULE_NOT_FOUND]: Cannot find <span class="hljs-built_in">module</span>

<span class="hljs-comment">// 浏览器中报错</span>
Uncaught <span class="hljs-built_in">SyntaxError</span>: The requested <span class="hljs-built_in">module</span> <span class="hljs-string">'./child.js'</span> does not provide an <span class="hljs-keyword">export</span> named <span class="hljs-string">'b'</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>第一个是 Node.js 适配层触发的内部错误（不是通过 throw 抛出的），第二个是浏览器抛出的 JS 引擎级别的语法错误。</p>
<h4 data-id="heading-9">模块执行顺序</h4>
<p>ES6 模块有 5 种状态，分别为 unlinked、linking、linked、evaluating 和 evaluated，用循环模块记录（Module Environment Records）[6]的 Status 字段表示。ES6 模块的处理包括连接（link）和评估（evaluate）两步。连接成功之后才能进行评估。</p>
<p>连接主要由函数 InnerModuleLinking[7] 实现。函数 InnerModuleLinking 会调用函数 InitializeEnvironment[8]，该函数会初始化模块的环境记录（Environment Records）[9]，主要包括创建模块的执行上下文（Execution Contexts）[10]、给导入模块变量创建绑定[11]并初始化[12]为子模块的对应变量，给 var 变量创建绑定并初始化为 undefined、给函数声明变量创建绑定并初始化为函数体的实例化[13]值、给其他变量创建绑定但不进行初始化。</p>
<p>对于图 3 的模块关系，连接过程如图 7 所示。连接阶段采用深度优先遍历，通过函数 HostResolveImportedModule[14] 获取子模块。完成核心操作的函数 InitializeEnvironment 是后置执行的，所以从效果上看，子模块先于父模块被初始化。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/88a96a1faa8d48059a2464af3ced22b0~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>图 7</p>
<p>评估主要由函数 InnerModuleEvaluation[15] 实现。函数 InnerModuleEvaluation 会调用函数 ExecuteModule[16]，该函数会评估模块代码（evaluating module.[[ECMAScriptCode]]）。ES6 规范并没有明确说明这里的评估模块代码具体指什么。我把 ES6 规范的相关部分反复看了至少十余遍，才得出一个比较合理的解释。这里的评估模块代码应该指根据代码语句顺序执行条款 13[17]、条款 14[18] 和 条款 15[19] 内的对应小节的“运行时语义：评估（Runtime Semantics: Evaluation）”。ScriptEvaluation[20] 中的评估脚本（evaluating scriptBody）应该也是这个意思。可以看到，ES6 规范虽然做了很多设计并且逻辑清晰和自洽，但仍有一些模棱两可的地方，没有达到一种绝对完善和无懈可击的状态。</p>
<p>对于图 3 的模块关系，评估过程如图 8 所示。和连接阶段类似，评估阶段也采用深度优先遍历，通过函数 HostResolveImportedModule 获取子模块。完成核心操作的函数 ExecuteModule 是后置执行的，所以从效果上看，子模块先于父模块被执行。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/e87afe78db564513ba60d183a0b1b457~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>图 8</p>
<p>由于连接阶段会给导入模块变量创建绑定并初始化为子模块的对应变量，子模块的对应变量在评估阶段会先被赋值，所以导入模块变量获得了和函数声明变量一样的提升效果。例如，代码 1 是能正常运行的。因此，ES6 模块的导入导出语句的位置不影响模块代码语句的执行结果。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-built_in">console</span>.log(a) <span class="hljs-comment">// 正常打印 a 的值</span>
<span class="hljs-keyword">import</span> &#123; a &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'./child.js'</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>代码 1</p>
<h4 data-id="heading-10">模块循环引用</h4>
<p>对于循环引用的场景，会先对子模块进行预处理和执行。连接阶段除了分析模块依赖关系，还会创建执行上下文和初始化变量，所以连接阶段主要包括分析模块依赖关系和对模块进行预处理。如图 9 所示，对于图 5 的模块关系，处理顺序为：预处理 B -> 预处理 A -> 执行 B -> 执行 A。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/eb435d7f409e4a078168809ad61488e2~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>图 9</p>
<h5 data-id="heading-11">使用不当的问题</h5>
<p>由于子模块先于父模块被执行，子模块直接执行从父模块导入的变量会导致 JS 错误。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// 文件 parent.js</span>
<span class="hljs-keyword">import</span> &#123;&#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'./child.js'</span>;
<span class="hljs-keyword">export</span> <span class="hljs-keyword">const</span> parent = <span class="hljs-string">'parent'</span>;

<span class="hljs-comment">// 文件 child.js</span>
<span class="hljs-keyword">import</span> &#123; parent &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'./parent.js'</span>;
<span class="hljs-built_in">console</span>.log(parent); <span class="hljs-comment">// 报错</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>代码 2</p>
<p>如代码 2 所示，child.js 中的导入变量 parent 被绑定为 parent.js 的导出变量 parent，当执行 child.js 的最后一行代码时，parent.js 还没有被执行，parent.js 的导出变量 parent 未被初始化，所以 child.js 中的导入变量 parent 也就没有被初始化，会导致 JS 错误。注意，本文说的变量是统称，包含 var、let、const、function 等关键字声明的变量。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-built_in">console</span>.log(parent)
            ^
<span class="hljs-built_in">ReferenceError</span>: Cannot access <span class="hljs-string">'parent'</span> before initialization
<span class="copy-code-btn">复制代码</span></code></pre>
<p>如果是异步执行，则没问题，因为异步执行的时候父模块已经被执行了。例如，代码 3 是能正常运行的。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// parent.js</span>
<span class="hljs-keyword">import</span> &#123;&#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'./child.js'</span>;
<span class="hljs-keyword">export</span> <span class="hljs-keyword">const</span> parent = <span class="hljs-string">'parent'</span>;

<span class="hljs-comment">// child.js</span>

<span class="hljs-keyword">import</span> &#123; parent &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'./parent.js'</span>;
<span class="hljs-built_in">setTimeout</span>(<span class="hljs-function">() =></span> &#123;
  <span class="hljs-built_in">console</span>.log(parent) <span class="hljs-comment">// 输出 'parent'</span>
&#125;, <span class="hljs-number">0</span>);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>代码 3</p>
<h3 data-id="heading-12">纠正教程观点</h3>
<p>《ECMAScript 6 入门教程》一书说的三个重大差异如下：</p>
<ol>
<li>CommonJS 模块输出的是一个值的拷贝，ES6 模块输出的是值的引用。</li>
<li>CommonJS 模块是运行时加载，ES6 模块是编译时输出接口。</li>
<li>CommonJS 模块的 require() 是同步加载模块，ES6 模块的 import 命令是异步加载，有一个独立的模块依赖的解析阶段。</li>
</ol>
<p>对于第 1 点，CommonJS 和 ES6 模块输出的都是变量，变量都是值的引用。该章节的评论中也有人质疑这个点。对于第 2 点，前半句基本正确，后半句基本错误。CommonJS 模块在执行阶段加载子模块文件，ES6 模块在预处理阶段加载子模块文件，当然 ES6 模块在执行阶段也会加载子模块文件，不过会使用预处理阶段的缓存。从形式上看，CommonJS 模块整体导出一个包含若干个变量的对象，ES6 模块分开导出单个变量，如果只看父模块，ES6 模块的父模块确实在预处理阶段就绑定了子模块的导出变量，但是预处理阶段的子模块的导出变量是还没有被赋最终值的，所以并不能算真正输出。对于第 3 点，CommonJS 模块同步加载并执行模块文件，ES6 模块提前加载并执行模块文件。异步通常被理解为延后一个时间节点执行，所以说成异步加载是错误的。</p>
<h2 data-id="heading-13">分析问题</h2>
<p>对 JS 模块机制有了更深刻的理解后，我们回来分析我遇到的问题。</p>
<h3 data-id="heading-14">问题一</h3>
<p>首先分析图 1 的报错。业务方 App 的工程代码用 webpack 打包，所以实际运行的是 CommonJS 模块。上面讲过 CommonJS 模块循环引用使用不当一般不会导致 JS 错误，为啥这里会出现 JS 报错呢？这是因为，循环引用使用不当导致变量的值为 undefined，我们的代码使用了 extends[21]，而 extends 不支持 undefined。由于使用了 Bable[22] 进行转码，所以由垫片 _inherits[23] 报错。另外一个典型的不支持的 undefined 的 case 是 Object.create(undefined)。</p>
<h3 data-id="heading-15">问题二</h3>
<p>然后分析图 2 的报错。在业务方 App 工程里 yarn link 教室 SDK，使用 webpack 打包后，运行的仍然是 CommonJS 模块，为什么会出现 JS 引擎级别的错误呢？这不是 ES6 模块才会出现的报错么？这里有两个原因。</p>
<p>教室 SDK 使用 <a href="https://link.juejin.cn/?target=https%3A%2F%2Frollupjs.org%2Fguide%2Fen%2F" target="_blank" rel="nofollow noopener noreferrer" title="https://rollupjs.org/guide/en/" ref="nofollow noopener noreferrer">Rollup</a>[24] 进行打包。Rollup 会把多个文件打包成一个文件，子模块的代码会被放到父模块前面。比如，代码 2 经过 Rollup 打包后变成了代码 4。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-built_in">console</span>.log(parent); <span class="hljs-comment">// 报错</span>

<span class="hljs-keyword">const</span> parent = <span class="hljs-string">'parent'</span>;
<span class="hljs-keyword">export</span> &#123; parent &#125;;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>代码 4</p>
<p>本地 yarn link 教室 SDK 后，引用的教室 SDK 包路径为软连接，而软连接在 Babel 转码时会被忽略。因此，业务 App 直接引用了 Rollup 打包的 ES6+ 语法的教室 SDK。如果在子模块中直接执行了父模块导出的变量，就会报错。如代码 4 所示，执行第一行代码时，变量 parent 有被创建绑定但没有被初始化。</p>
<h2 data-id="heading-16">解决问题</h2>
<p>明确了问题由模块循环引用导致，并分析了具体原因。那怎么在复杂的代码工程中找到出现循环引用的模块呢？</p>
<h3 data-id="heading-17">webpack plugin</h3>
<p>circular-dependency-plugin[25] 是一个分析模块循环引用的 webpack 插件。它的源码只有 100 行左右，原理也比较简单。在 optimizeModules[26] 钩子中，从本模块开始递归寻找依赖模块，并比较依赖模块与本模块的 debugId，如果相同，就判定为循环引用，并返回循环引用链。</p>
<h3 data-id="heading-18">定位并解决循环引用</h3>
<p>在业务 App 工程中引入 circular-dependency-plugin 后做一些配置，就可以看到教室 SDK 相关的循环引用模块。输出的模块循环引用链比较多，有 112 个。如何进一步定位到几个导致问题的循环引用呢？根据报错的堆栈找到报错的文件，然后找出和这个文件相关的循环引用，用 hack 的方式逐个切断这些循环引用后验证报错是否解决。最后，我在切断两个循环引用后解决了问题。其中一个循环引用链如下：</p>
<pre><code class="hljs language-js copyable" lang="js">Circular dependency detected:

node_modules/@byted-classroom/room/lib/service/assist/stream-validator.js ->

node_modules/@byted-classroom/room/lib/service/rtc/engine.js ->

node_modules/@byted-classroom/room/lib/service/rtc/definitions.js ->

node_modules/@byted-classroom/room/lib/service/rtc/base.js ->

node_modules/@byted-classroom/room/lib/service/monitor/index.js ->

node_modules/@byted-classroom/room/lib/service/monitor/monitors.js ->

node_modules/@byted-classroom/room/lib/service/monitor/room.js ->

node_modules/@byted-classroom/room/lib/service/npy-courseware/student-courseware.js ->

node_modules/@byted-classroom/room/lib/service/index.js ->

node_modules/@byted-classroom/room/lib/service/audio-mixing/index.js ->

node_modules/@byted-classroom/room/lib/service/audio-mixing/mixing-player.js ->

node_modules/@byted-classroom/room/lib/index.js ->

node_modules/@byted-classroom/room/lib/room/base.js ->

node_modules/@byted-classroom/room/lib/service/rtc/manager.js ->

node_modules/@byted-classroom/room/lib/service/assist/stream-validator.js
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-19">建议</h2>
<p>TypeScript 工程的循环引用问题是比较普遍的，常常会因为需要使用一个类型而增加一个文件依赖。建议在工程中引入模块循环引用检测机制，比如 webpack 插件 circular-dependency-plugin 和 eslint 规则 import/no-cycle，以便及时调整文件或代码结构来切断循环引用。</p>
<h2 data-id="heading-20">总结</h2>
<p>本文从开发时遇到的一个报错出发，对 JS 模块机制和循环引用进行了深度分析，并提供了定位和解决模块循环引用问题的方法。根据对 ES 规范的解读，本文纠正了《ECMAScript 6 入门教程》一书中的几个错误观点。</p>
<h2 data-id="heading-21">参考文献</h2>
<ol>
<li>ES6 入门教程，<a href="https://link.juejin.cn/?target=https%3A%2F%2Fes6.ruanyifeng.com%2F" target="_blank" rel="nofollow noopener noreferrer" title="https://es6.ruanyifeng.com/" ref="nofollow noopener noreferrer">es6.ruanyifeng.com/</a></li>
<li>Modules: CommonJS modules，<a href="https://link.juejin.cn/?target=https%3A%2F%2Fnodejs.org%2Fdist%2Flatest-v14.x%2Fdocs%2Fapi%2Fmodules.html%23modules_modules_commonjs_modules" target="_blank" rel="nofollow noopener noreferrer" title="https://nodejs.org/dist/latest-v14.x/docs/api/modules.html#modules_modules_commonjs_modules" ref="nofollow noopener noreferrer">nodejs.org/dist/latest…</a></li>
<li>cjs/loader.js，<a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fnodejs%2Fnode%2Fblob%2Fv14.x-staging%2Flib%2Finternal%2Fmodules%2Fcjs%2Floader.js" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/nodejs/node/blob/v14.x-staging/lib/internal/modules/cjs/loader.js" ref="nofollow noopener noreferrer">github.com/nodejs/node…</a></li>
<li>ECMAScript Language: Scripts and Modules，<a href="https://link.juejin.cn/?target=https%3A%2F%2Ftc39.es%2Fecma262%2F%23sec-ecmascript-language-scripts-and-modules" target="_blank" rel="nofollow noopener noreferrer" title="https://tc39.es/ecma262/#sec-ecmascript-language-scripts-and-modules" ref="nofollow noopener noreferrer">tc39.es/ecma262/#se…</a></li>
<li>What features of V8 engine dose Node.js use when implementing ECMAScript modules，<a href="https://link.juejin.cn/?target=https%3A%2F%2Fapp.slack.com%2Fclient%2FT0K2RM7F0%2FC0K2NFFV1%2Fthread%2FC0K2NFFV1-1626762465.203500" target="_blank" rel="nofollow noopener noreferrer" title="https://app.slack.com/client/T0K2RM7F0/C0K2NFFV1/thread/C0K2NFFV1-1626762465.203500" ref="nofollow noopener noreferrer">app.slack.com/client/T0K2…</a></li>
<li>Cyclic Module Records，<a href="https://link.juejin.cn/?target=https%3A%2F%2Ftc39.es%2Fecma262%2F%23sec-cyclic-module-records" target="_blank" rel="nofollow noopener noreferrer" title="https://tc39.es/ecma262/#sec-cyclic-module-records" ref="nofollow noopener noreferrer">tc39.es/ecma262/#se…</a></li>
<li>InnerModuleLinking，<a href="https://link.juejin.cn/?target=https%3A%2F%2Ftc39.es%2Fecma262%2F%23sec-InnerModuleLinking" target="_blank" rel="nofollow noopener noreferrer" title="https://tc39.es/ecma262/#sec-InnerModuleLinking" ref="nofollow noopener noreferrer">tc39.es/ecma262/#se…</a></li>
<li>InitializeEnvironment，<a href="https://link.juejin.cn/?target=https%3A%2F%2Ftc39.es%2Fecma262%2F%23sec-source-text-module-record-initialize-environment" target="_blank" rel="nofollow noopener noreferrer" title="https://tc39.es/ecma262/#sec-source-text-module-record-initialize-environment" ref="nofollow noopener noreferrer">tc39.es/ecma262/#se…</a></li>
<li>Environment Records，<a href="https://link.juejin.cn/?target=https%3A%2F%2Ftc39.es%2Fecma262%2F%23sec-environment-records" target="_blank" rel="nofollow noopener noreferrer" title="https://tc39.es/ecma262/#sec-environment-records" ref="nofollow noopener noreferrer">tc39.es/ecma262/#se…</a></li>
<li>Execution Contexts，<a href="https://link.juejin.cn/?target=https%3A%2F%2Ftc39.es%2Fecma262%2F%23sec-execution-contexts" target="_blank" rel="nofollow noopener noreferrer" title="https://tc39.es/ecma262/#sec-execution-contexts" ref="nofollow noopener noreferrer">tc39.es/ecma262/#se…</a></li>
<li>CreateMutableBinding，<a href="https://link.juejin.cn/?target=https%3A%2F%2Ftc39.es%2Fecma262%2F%23sec-declarative-environment-records-createmutablebinding-n-d" target="_blank" rel="nofollow noopener noreferrer" title="https://tc39.es/ecma262/#sec-declarative-environment-records-createmutablebinding-n-d" ref="nofollow noopener noreferrer">tc39.es/ecma262/#se…</a></li>
<li>InitializeBinding，<a href="https://link.juejin.cn/?target=https%3A%2F%2Ftc39.es%2Fecma262%2F%23sec-declarative-environment-records-initializebinding-n-v" target="_blank" rel="nofollow noopener noreferrer" title="https://tc39.es/ecma262/#sec-declarative-environment-records-initializebinding-n-v" ref="nofollow noopener noreferrer">tc39.es/ecma262/#se…</a></li>
<li>Runtime Semantics: InstantiateFunctionObject，<a href="https://link.juejin.cn/?target=https%3A%2F%2Ftc39.es%2Fecma262%2F%23sec-runtime-semantics-instantiatefunctionobject" target="_blank" rel="nofollow noopener noreferrer" title="https://tc39.es/ecma262/#sec-runtime-semantics-instantiatefunctionobject" ref="nofollow noopener noreferrer">tc39.es/ecma262/#se…</a></li>
<li>HostResolveImportedModule，<a href="https://link.juejin.cn/?target=https%3A%2F%2Ftc39.es%2Fecma262%2F%23sec-hostresolveimportedmodule" target="_blank" rel="nofollow noopener noreferrer" title="https://tc39.es/ecma262/#sec-hostresolveimportedmodule" ref="nofollow noopener noreferrer">tc39.es/ecma262/#se…</a></li>
<li>InnerModuleEvaluation，<a href="https://link.juejin.cn/?target=https%3A%2F%2Ftc39.es%2Fecma262%2F%23sec-innermoduleevaluation" target="_blank" rel="nofollow noopener noreferrer" title="https://tc39.es/ecma262/#sec-innermoduleevaluation" ref="nofollow noopener noreferrer">tc39.es/ecma262/#se…</a></li>
<li>ExecuteModule，<a href="https://link.juejin.cn/?target=https%3A%2F%2Ftc39.es%2Fecma262%2F%23sec-source-text-module-record-execute-module" target="_blank" rel="nofollow noopener noreferrer" title="https://tc39.es/ecma262/#sec-source-text-module-record-execute-module" ref="nofollow noopener noreferrer">tc39.es/ecma262/#se…</a></li>
<li>ECMAScript Language: Expressions，<a href="https://link.juejin.cn/?target=https%3A%2F%2Ftc39.es%2Fecma262%2F%23sec-ecmascript-language-expressions" target="_blank" rel="nofollow noopener noreferrer" title="https://tc39.es/ecma262/#sec-ecmascript-language-expressions" ref="nofollow noopener noreferrer">tc39.es/ecma262/#se…</a></li>
<li>ECMAScript Language: Statements and Declarations，<a href="https://link.juejin.cn/?target=https%3A%2F%2Ftc39.es%2Fecma262%2F%23sec-ecmascript-language-statements-and-declarations" target="_blank" rel="nofollow noopener noreferrer" title="https://tc39.es/ecma262/#sec-ecmascript-language-statements-and-declarations" ref="nofollow noopener noreferrer">tc39.es/ecma262/#se…</a></li>
<li>ECMAScript Language: Functions and Classes，<a href="https://link.juejin.cn/?target=https%3A%2F%2Ftc39.es%2Fecma262%2F%23sec-ecmascript-language-functions-and-classes" target="_blank" rel="nofollow noopener noreferrer" title="https://tc39.es/ecma262/#sec-ecmascript-language-functions-and-classes" ref="nofollow noopener noreferrer">tc39.es/ecma262/#se…</a></li>
<li>ScriptEvaluation，<a href="https://link.juejin.cn/?target=https%3A%2F%2Ftc39.es%2Fecma262%2F%23sec-runtime-semantics-scriptevaluation" target="_blank" rel="nofollow noopener noreferrer" title="https://tc39.es/ecma262/#sec-runtime-semantics-scriptevaluation" ref="nofollow noopener noreferrer">tc39.es/ecma262/#se…</a></li>
<li>extends，<a href="https://link.juejin.cn/?target=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FJavaScript%2FReference%2FClasses%2Fextends" target="_blank" rel="nofollow noopener noreferrer" title="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Classes/extends" ref="nofollow noopener noreferrer">developer.mozilla.org/en-US/docs/…</a></li>
<li>babeljs，<a href="https://link.juejin.cn/?target=https%3A%2F%2Fbabeljs.io%2F" target="_blank" rel="nofollow noopener noreferrer" title="https://babeljs.io/" ref="nofollow noopener noreferrer">babeljs.io/</a></li>
<li>_inherits，<a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fbabel%2Fbabel%2Fblob%2Fmain%2Fpackages%2Fbabel-helpers%2Fsrc%2Fhelpers.js%23L344-L346" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/babel/babel/blob/main/packages/babel-helpers/src/helpers.js#L344-L346" ref="nofollow noopener noreferrer">github.com/babel/babel…</a></li>
<li>rollup.js，<a href="https://link.juejin.cn/?target=https%3A%2F%2Frollupjs.org%2Fguide%2Fen%2F" target="_blank" rel="nofollow noopener noreferrer" title="https://rollupjs.org/guide/en/" ref="nofollow noopener noreferrer">rollupjs.org/guide/en/</a></li>
<li>circular-dependency-plugin，<a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Faackerman%2Fcircular-dependency-plugin" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/aackerman/circular-dependency-plugin" ref="nofollow noopener noreferrer">github.com/aackerman/c…</a></li>
<li>optimizeModules，<a href="https://link.juejin.cn/?target=https%3A%2F%2Fv4.webpack.js.org%2Fapi%2Fcompilation-hooks%2F%23optimizemodules" target="_blank" rel="nofollow noopener noreferrer" title="https://v4.webpack.js.org/api/compilation-hooks/#optimizemodules" ref="nofollow noopener noreferrer">v4.webpack.js.org/api/compila…</a></li>
</ol></div>  
</div>
            