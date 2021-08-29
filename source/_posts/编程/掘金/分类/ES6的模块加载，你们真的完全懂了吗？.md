
---
title: 'ES6的模块加载，你们真的完全懂了吗？'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=8286'
author: 掘金
comments: false
date: Sat, 28 Aug 2021 18:24:30 GMT
thumbnail: 'https://picsum.photos/400/300?random=8286'
---

<div>   
<div class="markdown-body html cache"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>这是我参与8月更文挑战的第12天，活动详情查看：<a href="https://juejin.cn/post/6987962113788493831" title="https://juejin.cn/post/6987962113788493831" target="_blank">8月更文挑战</a></p>
<h1 data-id="heading-0">Module 的语法</h1>
<h2 data-id="heading-1">概述</h2>
<p>历史上，JavaScript 一直没有模块（module）体系，无法将一个大程序拆分成互相依赖的小文件，再用简单的方法拼装起来。其他语言都有这项功能，比如 Ruby 的<code>require</code>、Python 的<code>import</code>，甚至就连 CSS 都有<code>@import</code>，但是 JavaScript 任何这方面的支持都没有，这对开发大型的、复杂的项目形成了巨大障碍。</p>
<p>在 ES6 之前，社区制定了一些模块加载方案，最主要的有 CommonJS 和 AMD 两种。前者用于服务器，后者用于浏览器。ES6 在语言标准的层面上，实现了模块功能，而且实现得相当简单，完全可以取代 CommonJS 和 AMD 规范，成为浏览器和服务器通用的模块解决方案。</p>
<p>ES6 模块的设计思想是尽量的静态化，使得编译时就能确定模块的依赖关系，以及输入和输出的变量。CommonJS 和 AMD 模块，都只能在运行时确定这些东西。比如，CommonJS 模块就是对象，输入时必须查找对象属性。</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">// CommonJS模块</span>
<span class="hljs-keyword">let</span> &#123; stat, exists, readfile &#125; = <span class="hljs-built_in">require</span>(<span class="hljs-string">'fs'</span>);

<span class="hljs-comment">// 等同于</span>
<span class="hljs-keyword">let</span> _fs = <span class="hljs-built_in">require</span>(<span class="hljs-string">'fs'</span>);
<span class="hljs-keyword">let</span> stat = _fs.stat;
<span class="hljs-keyword">let</span> exists = _fs.exists;
<span class="hljs-keyword">let</span> readfile = _fs.readfile;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>上面代码的实质是整体加载<code>fs</code>模块（即加载<code>fs</code>的所有方法），生成一个对象（<code>_fs</code>），然后再从这个对象上面读取 3 个方法。这种加载称为“运行时加载”，因为只有运行时才能得到这个对象，导致完全没办法在编译时做“静态优化”。</p>
<p>ES6 模块不是对象，而是通过<code>export</code>命令显式指定输出的代码，再通过<code>import</code>命令输入。</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">// ES6模块</span>
<span class="hljs-keyword">import</span> &#123; stat, exists, readFile &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'fs'</span>;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>上面代码的实质是从<code>fs</code>模块加载 3 个方法，其他方法不加载。这种加载称为“编译时加载”或者静态加载，即 ES6 可以在编译时就完成模块加载，效率要比 CommonJS 模块的加载方式高。当然，这也导致了没法引用 ES6 模块本身，因为它不是对象。</p>
<p>由于 ES6 模块是编译时加载，使得静态分析成为可能。有了它，就能进一步拓宽 JavaScript 的语法，比如引入宏（macro）和类型检验（type system）这些只能靠静态分析实现的功能。</p>
<p>除了静态加载带来的各种好处，ES6 模块还有以下好处。</p>
<ul>
<li>不再需要<code>UMD</code>模块格式了，将来服务器和浏览器都会支持 ES6 模块格式。目前，通过各种工具库，其实已经做到了这一点。</li>
<li>将来浏览器的新 API 就能用模块格式提供，不再必须做成全局变量或者<code>navigator</code>对象的属性。</li>
<li>不再需要对象作为命名空间（比如<code>Math</code>对象），未来这些功能可以通过模块提供。</li>
</ul>
<p>本章介绍 ES6 模块的语法，下一章介绍如何在浏览器和 Node 之中，加载 ES6 模块。</p>
<h2 data-id="heading-2">严格模式</h2>
<p>ES6 的模块自动采用严格模式，不管你有没有在模块头部加上<code>"use strict";</code>。</p>
<p>严格模式主要有以下限制。</p>
<ul>
<li>变量必须声明后再使用</li>
<li>函数的参数不能有同名属性，否则报错</li>
<li>不能使用<code>with</code>语句</li>
<li>不能对只读属性赋值，否则报错</li>
<li>不能使用前缀 0 表示八进制数，否则报错</li>
<li>不能删除不可删除的属性，否则报错</li>
<li>不能删除变量<code>delete prop</code>，会报错，只能删除属性<code>delete global[prop]</code></li>
<li><code>eval</code>不会在它的外层作用域引入变量</li>
<li><code>eval</code>和<code>arguments</code>不能被重新赋值</li>
<li><code>arguments</code>不会自动反映函数参数的变化</li>
<li>不能使用<code>arguments.callee</code></li>
<li>不能使用<code>arguments.caller</code></li>
<li>禁止<code>this</code>指向全局对象</li>
<li>不能使用<code>fn.caller</code>和<code>fn.arguments</code>获取函数调用的堆栈</li>
<li>增加了保留字（比如<code>protected</code>、<code>static</code>和<code>interface</code>）</li>
</ul>
<p>上面这些限制，模块都必须遵守。由于严格模式是 ES5 引入的，不属于 ES6，所以请参阅相关 ES5 书籍，本书不再详细介绍了。</p>
<p>其中，尤其需要注意<code>this</code>的限制。ES6 模块之中，顶层的<code>this</code>指向<code>undefined</code>，即不应该在顶层代码使用<code>this</code>。</p>
<h2 data-id="heading-3">export 命令</h2>
<p>模块功能主要由两个命令构成：<code>export</code>和<code>import</code>。<code>export</code>命令用于规定模块的对外接口，<code>import</code>命令用于输入其他模块提供的功能。</p>
<p>一个模块就是一个独立的文件。该文件内部的所有变量，外部无法获取。如果你希望外部能够读取模块内部的某个变量，就必须使用<code>export</code>关键字输出该变量。下面是一个 JS 文件，里面使用<code>export</code>命令输出变量。</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">// profile.js</span>
<span class="hljs-keyword">export</span> <span class="hljs-keyword">var</span> firstName = <span class="hljs-string">'Michael'</span>;
<span class="hljs-keyword">export</span> <span class="hljs-keyword">var</span> lastName = <span class="hljs-string">'Jackson'</span>;
<span class="hljs-keyword">export</span> <span class="hljs-keyword">var</span> year = <span class="hljs-number">1958</span>;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>上面代码是<code>profile.js</code>文件，保存了用户信息。ES6 将其视为一个模块，里面用<code>export</code>命令对外部输出了三个变量。</p>
<p><code>export</code>的写法，除了像上面这样，还有另外一种。</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">// profile.js</span>
<span class="hljs-keyword">var</span> firstName = <span class="hljs-string">'Michael'</span>;
<span class="hljs-keyword">var</span> lastName = <span class="hljs-string">'Jackson'</span>;
<span class="hljs-keyword">var</span> year = <span class="hljs-number">1958</span>;

<span class="hljs-keyword">export</span> &#123; firstName, lastName, year &#125;;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>上面代码在<code>export</code>命令后面，使用大括号指定所要输出的一组变量。它与前一种写法（直接放置在<code>var</code>语句前）是等价的，但是应该优先考虑使用这种写法。因为这样就可以在脚本尾部，一眼看清楚输出了哪些变量。</p>
<p><code>export</code>命令除了输出变量，还可以输出函数或类（class）。</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">export</span> <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">multiply</span>(<span class="hljs-params">x, y</span>) </span>&#123;
  <span class="hljs-keyword">return</span> x * y;
&#125;;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>上面代码对外输出一个函数<code>multiply</code>。</p>
<p>通常情况下，<code>export</code>输出的变量就是本来的名字，但是可以使用<code>as</code>关键字重命名。</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">v1</span>(<span class="hljs-params"></span>) </span>&#123; ... &#125;
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">v2</span>(<span class="hljs-params"></span>) </span>&#123; ... &#125;

<span class="hljs-keyword">export</span> &#123;
  v1 <span class="hljs-keyword">as</span> streamV1,
  v2 <span class="hljs-keyword">as</span> streamV2,
  v2 <span class="hljs-keyword">as</span> streamLatestVersion
&#125;;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>上面代码使用<code>as</code>关键字，重命名了函数<code>v1</code>和<code>v2</code>的对外接口。重命名后，<code>v2</code>可以用不同的名字输出两次。</p>
<p>需要特别注意的是，<code>export</code>命令规定的是对外的接口，必须与模块内部的变量建立一一对应关系。</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">// 报错</span>
<span class="hljs-keyword">export</span> <span class="hljs-number">1</span>;

<span class="hljs-comment">// 报错</span>
<span class="hljs-keyword">var</span> m = <span class="hljs-number">1</span>;
<span class="hljs-keyword">export</span> m;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>上面两种写法都会报错，因为没有提供对外的接口。第一种写法直接输出 1，第二种写法通过变量<code>m</code>，还是直接输出 1。<code>1</code>只是一个值，不是接口。正确的写法是下面这样。</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">// 写法一</span>
<span class="hljs-keyword">export</span> <span class="hljs-keyword">var</span> m = <span class="hljs-number">1</span>;

<span class="hljs-comment">// 写法二</span>
<span class="hljs-keyword">var</span> m = <span class="hljs-number">1</span>;
<span class="hljs-keyword">export</span> &#123;m&#125;;

<span class="hljs-comment">// 写法三</span>
<span class="hljs-keyword">var</span> n = <span class="hljs-number">1</span>;
<span class="hljs-keyword">export</span> &#123;n <span class="hljs-keyword">as</span> m&#125;;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>上面三种写法都是正确的，规定了对外的接口<code>m</code>。其他脚本可以通过这个接口，取到值<code>1</code>。它们的实质是，在接口名与模块内部变量之间，建立了一一对应的关系。</p>
<p>同样的，<code>function</code>和<code>class</code>的输出，也必须遵守这样的写法。</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">// 报错</span>
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">f</span>(<span class="hljs-params"></span>) </span>&#123;&#125;
<span class="hljs-keyword">export</span> f;

<span class="hljs-comment">// 正确</span>
<span class="hljs-keyword">export</span> <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">f</span>(<span class="hljs-params"></span>) </span>&#123;&#125;;

<span class="hljs-comment">// 正确</span>
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">f</span>(<span class="hljs-params"></span>) </span>&#123;&#125;
<span class="hljs-keyword">export</span> &#123;f&#125;;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>另外，<code>export</code>语句输出的接口，与其对应的值是动态绑定关系，即通过该接口，可以取到模块内部实时的值。</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">export</span> <span class="hljs-keyword">var</span> foo = <span class="hljs-string">'bar'</span>;
<span class="hljs-built_in">setTimeout</span>(<span class="hljs-function">() =></span> foo = <span class="hljs-string">'baz'</span>, <span class="hljs-number">500</span>);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>上面代码输出变量<code>foo</code>，值为<code>bar</code>，500 毫秒之后变成<code>baz</code>。</p>
<p>这一点与 CommonJS 规范完全不同。CommonJS 模块输出的是值的缓存，不存在动态更新，详见下文《Module 的加载实现》一节。</p>
<p>最后，<code>export</code>命令可以出现在模块的任何位置，只要处于模块顶层就可以。如果处于块级作用域内，就会报错，下一节的<code>import</code>命令也是如此。这是因为处于条件代码块之中，就没法做静态优化了，违背了 ES6 模块的设计初衷。</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">foo</span>(<span class="hljs-params"></span>) </span>&#123;
  <span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> <span class="hljs-string">'bar'</span> <span class="hljs-comment">// SyntaxError</span>
&#125;
foo()
<span class="copy-code-btn">复制代码</span></code></pre>
<p>上面代码中，<code>export</code>语句放在函数之中，结果报错。</p>
<h2 data-id="heading-4">import 命令</h2>
<p>使用<code>export</code>命令定义了模块的对外接口以后，其他 JS 文件就可以通过<code>import</code>命令加载这个模块。</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">// main.js</span>
<span class="hljs-keyword">import</span> &#123; firstName, lastName, year &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'./profile.js'</span>;

<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">setName</span>(<span class="hljs-params">element</span>) </span>&#123;
  element.textContent = firstName + <span class="hljs-string">' '</span> + lastName;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>上面代码的<code>import</code>命令，用于加载<code>profile.js</code>文件，并从中输入变量。<code>import</code>命令接受一对大括号，里面指定要从其他模块导入的变量名。大括号里面的变量名，必须与被导入模块（<code>profile.js</code>）对外接口的名称相同。</p>
<p>如果想为输入的变量重新取一个名字，<code>import</code>命令要使用<code>as</code>关键字，将输入的变量重命名。</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">import</span> &#123; lastName <span class="hljs-keyword">as</span> surname &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'./profile.js'</span>;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><code>import</code>命令输入的变量都是只读的，因为它的本质是输入接口。也就是说，不允许在加载模块的脚本里面，改写接口。</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">import</span> &#123;a&#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'./xxx.js'</span>

a = &#123;&#125;; <span class="hljs-comment">// Syntax Error : 'a' is read-only;</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>上面代码中，脚本加载了变量<code>a</code>，对其重新赋值就会报错，因为<code>a</code>是一个只读的接口。但是，如果<code>a</code>是一个对象，改写<code>a</code>的属性是允许的。</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">import</span> &#123;a&#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'./xxx.js'</span>

a.foo = <span class="hljs-string">'hello'</span>; <span class="hljs-comment">// 合法操作</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>上面代码中，<code>a</code>的属性可以成功改写，并且其他模块也可以读到改写后的值。不过，这种写法很难查错，建议凡是输入的变量，都当作完全只读，不要轻易改变它的属性。</p>
<p><code>import</code>后面的<code>from</code>指定模块文件的位置，可以是相对路径，也可以是绝对路径。如果不带有路径，只是一个模块名，那么必须有配置文件，告诉 JavaScript 引擎该模块的位置。</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">import</span> &#123; myMethod &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'util'</span>;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>上面代码中，<code>util</code>是模块文件名，由于不带有路径，必须通过配置，告诉引擎怎么取到这个模块。</p>
<p>注意，<code>import</code>命令具有提升效果，会提升到整个模块的头部，首先执行。</p>
<pre><code class="hljs language-javascript copyable" lang="javascript">foo();

<span class="hljs-keyword">import</span> &#123; foo &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'my_module'</span>;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>上面的代码不会报错，因为<code>import</code>的执行早于<code>foo</code>的调用。这种行为的本质是，<code>import</code>命令是编译阶段执行的，在代码运行之前。</p>
<p>由于<code>import</code>是静态执行，所以不能使用表达式和变量，这些只有在运行时才能得到结果的语法结构。</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">// 报错</span>
<span class="hljs-keyword">import</span> &#123; <span class="hljs-string">'f'</span> + <span class="hljs-string">'oo'</span> &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'my_module'</span>;

<span class="hljs-comment">// 报错</span>
<span class="hljs-keyword">let</span> <span class="hljs-built_in">module</span> = <span class="hljs-string">'my_module'</span>;
<span class="hljs-keyword">import</span> &#123; foo &#125; <span class="hljs-keyword">from</span> <span class="hljs-built_in">module</span>;

<span class="hljs-comment">// 报错</span>
<span class="hljs-keyword">if</span> (x === <span class="hljs-number">1</span>) &#123;
  <span class="hljs-keyword">import</span> &#123; foo &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'module1'</span>;
&#125; <span class="hljs-keyword">else</span> &#123;
  <span class="hljs-keyword">import</span> &#123; foo &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'module2'</span>;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>上面三种写法都会报错，因为它们用到了表达式、变量和<code>if</code>结构。在静态分析阶段，这些语法都是没法得到值的。</p>
<p>最后，<code>import</code>语句会执行所加载的模块，因此可以有下面的写法。</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">import</span> <span class="hljs-string">'lodash'</span>;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>上面代码仅仅执行<code>lodash</code>模块，但是不输入任何值。</p>
<p>如果多次重复执行同一句<code>import</code>语句，那么只会执行一次，而不会执行多次。</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">import</span> <span class="hljs-string">'lodash'</span>;
<span class="hljs-keyword">import</span> <span class="hljs-string">'lodash'</span>;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>上面代码加载了两次<code>lodash</code>，但是只会执行一次。</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">import</span> &#123; foo &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'my_module'</span>;
<span class="hljs-keyword">import</span> &#123; bar &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'my_module'</span>;

<span class="hljs-comment">// 等同于</span>
<span class="hljs-keyword">import</span> &#123; foo, bar &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'my_module'</span>;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>上面代码中，虽然<code>foo</code>和<code>bar</code>在两个语句中加载，但是它们对应的是同一个<code>my_module</code>模块。也就是说，<code>import</code>语句是 Singleton 模式。</p>
<p>目前阶段，通过 Babel 转码，CommonJS 模块的<code>require</code>命令和 ES6 模块的<code>import</code>命令，可以写在同一个模块里面，但是最好不要这样做。因为<code>import</code>在静态解析阶段执行，所以它是一个模块之中最早执行的。下面的代码可能不会得到预期结果。</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-built_in">require</span>(<span class="hljs-string">'core-js/modules/es6.symbol'</span>);
<span class="hljs-built_in">require</span>(<span class="hljs-string">'core-js/modules/es6.promise'</span>);
<span class="hljs-keyword">import</span> React <span class="hljs-keyword">from</span> <span class="hljs-string">'React'</span>;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-5">模块的整体加载</h2>
<p>除了指定加载某个输出值，还可以使用整体加载，即用星号（<code>*</code>）指定一个对象，所有输出值都加载在这个对象上面。</p>
<p>下面是一个<code>circle.js</code>文件，它输出两个方法<code>area</code>和<code>circumference</code>。</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">// circle.js</span>

<span class="hljs-keyword">export</span> <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">area</span>(<span class="hljs-params">radius</span>) </span>&#123;
  <span class="hljs-keyword">return</span> <span class="hljs-built_in">Math</span>.PI * radius * radius;
&#125;

<span class="hljs-keyword">export</span> <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">circumference</span>(<span class="hljs-params">radius</span>) </span>&#123;
  <span class="hljs-keyword">return</span> <span class="hljs-number">2</span> * <span class="hljs-built_in">Math</span>.PI * radius;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>现在，加载这个模块。</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">// main.js</span>

<span class="hljs-keyword">import</span> &#123; area, circumference &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'./circle'</span>;

<span class="hljs-built_in">console</span>.log(<span class="hljs-string">'圆面积：'</span> + area(<span class="hljs-number">4</span>));
<span class="hljs-built_in">console</span>.log(<span class="hljs-string">'圆周长：'</span> + circumference(<span class="hljs-number">14</span>));
<span class="copy-code-btn">复制代码</span></code></pre>
<p>上面写法是逐一指定要加载的方法，整体加载的写法如下。</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">import</span> * <span class="hljs-keyword">as</span> circle <span class="hljs-keyword">from</span> <span class="hljs-string">'./circle'</span>;

<span class="hljs-built_in">console</span>.log(<span class="hljs-string">'圆面积：'</span> + circle.area(<span class="hljs-number">4</span>));
<span class="hljs-built_in">console</span>.log(<span class="hljs-string">'圆周长：'</span> + circle.circumference(<span class="hljs-number">14</span>));
<span class="copy-code-btn">复制代码</span></code></pre>
<p>注意，模块整体加载所在的那个对象（上例是<code>circle</code>），应该是可以静态分析的，所以不允许运行时改变。下面的写法都是不允许的。</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">import</span> * <span class="hljs-keyword">as</span> circle <span class="hljs-keyword">from</span> <span class="hljs-string">'./circle'</span>;

<span class="hljs-comment">// 下面两行都是不允许的</span>
circle.foo = <span class="hljs-string">'hello'</span>;
circle.area = <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params"></span>) </span>&#123;&#125;;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-6">export default 命令</h2>
<p>从前面的例子可以看出，使用<code>import</code>命令的时候，用户需要知道所要加载的变量名或函数名，否则无法加载。但是，用户肯定希望快速上手，未必愿意阅读文档，去了解模块有哪些属性和方法。</p>
<p>为了给用户提供方便，让他们不用阅读文档就能加载模块，就要用到<code>export default</code>命令，为模块指定默认输出。</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">// export-default.js</span>
<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params"></span>) </span>&#123;
  <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'foo'</span>);
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>上面代码是一个模块文件<code>export-default.js</code>，它的默认输出是一个函数。</p>
<p>其他模块加载该模块时，<code>import</code>命令可以为该匿名函数指定任意名字。</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">// import-default.js</span>
<span class="hljs-keyword">import</span> customName <span class="hljs-keyword">from</span> <span class="hljs-string">'./export-default'</span>;
customName(); <span class="hljs-comment">// 'foo'</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>上面代码的<code>import</code>命令，可以用任意名称指向<code>export-default.js</code>输出的方法，这时就不需要知道原模块输出的函数名。需要注意的是，这时<code>import</code>命令后面，不使用大括号。</p>
<p><code>export default</code>命令用在非匿名函数前，也是可以的。</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">// export-default.js</span>
<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">foo</span>(<span class="hljs-params"></span>) </span>&#123;
  <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'foo'</span>);
&#125;

<span class="hljs-comment">// 或者写成</span>

<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">foo</span>(<span class="hljs-params"></span>) </span>&#123;
  <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'foo'</span>);
&#125;

<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> foo;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>上面代码中，<code>foo</code>函数的函数名<code>foo</code>，在模块外部是无效的。加载的时候，视同匿名函数加载。</p>
<p>下面比较一下默认输出和正常输出。</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">// 第一组</span>
<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">crc32</span>(<span class="hljs-params"></span>) </span>&#123; <span class="hljs-comment">// 输出</span>
  <span class="hljs-comment">// ...</span>
&#125;

<span class="hljs-keyword">import</span> crc32 <span class="hljs-keyword">from</span> <span class="hljs-string">'crc32'</span>; <span class="hljs-comment">// 输入</span>

<span class="hljs-comment">// 第二组</span>
<span class="hljs-keyword">export</span> <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">crc32</span>(<span class="hljs-params"></span>) </span>&#123; <span class="hljs-comment">// 输出</span>
  <span class="hljs-comment">// ...</span>
&#125;;

<span class="hljs-keyword">import</span> &#123;crc32&#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'crc32'</span>; <span class="hljs-comment">// 输入</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>上面代码的两组写法，第一组是使用<code>export default</code>时，对应的<code>import</code>语句不需要使用大括号；第二组是不使用<code>export default</code>时，对应的<code>import</code>语句需要使用大括号。</p>
<p><code>export default</code>命令用于指定模块的默认输出。显然，一个模块只能有一个默认输出，因此<code>export default</code>命令只能使用一次。所以，import命令后面才不用加大括号，因为只可能唯一对应<code>export default</code>命令。</p>
<p>本质上，<code>export default</code>就是输出一个叫做<code>default</code>的变量或方法，然后系统允许你为它取任意名字。所以，下面的写法是有效的。</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">// modules.js</span>
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">add</span>(<span class="hljs-params">x, y</span>) </span>&#123;
  <span class="hljs-keyword">return</span> x * y;
&#125;
<span class="hljs-keyword">export</span> &#123;add <span class="hljs-keyword">as</span> <span class="hljs-keyword">default</span>&#125;;
<span class="hljs-comment">// 等同于</span>
<span class="hljs-comment">// export default add;</span>

<span class="hljs-comment">// app.js</span>
<span class="hljs-keyword">import</span> &#123; <span class="hljs-keyword">default</span> <span class="hljs-keyword">as</span> foo &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'modules'</span>;
<span class="hljs-comment">// 等同于</span>
<span class="hljs-comment">// import foo from 'modules';</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>正是因为<code>export default</code>命令其实只是输出一个叫做<code>default</code>的变量，所以它后面不能跟变量声明语句。</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">// 正确</span>
<span class="hljs-keyword">export</span> <span class="hljs-keyword">var</span> a = <span class="hljs-number">1</span>;

<span class="hljs-comment">// 正确</span>
<span class="hljs-keyword">var</span> a = <span class="hljs-number">1</span>;
<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> a;

<span class="hljs-comment">// 错误</span>
<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> <span class="hljs-keyword">var</span> a = <span class="hljs-number">1</span>;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>上面代码中，<code>export default a</code>的含义是将变量<code>a</code>的值赋给变量<code>default</code>。所以，最后一种写法会报错。</p>
<p>同样地，因为<code>export default</code>命令的本质是将后面的值，赋给<code>default</code>变量，所以可以直接将一个值写在<code>export default</code>之后。</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">// 正确</span>
<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> <span class="hljs-number">42</span>;

<span class="hljs-comment">// 报错</span>
<span class="hljs-keyword">export</span> <span class="hljs-number">42</span>;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>上面代码中，后一句报错是因为没有指定对外的接口，而前一句指定对外接口为<code>default</code>。</p>
<p>有了<code>export default</code>命令，输入模块时就非常直观了，以输入 lodash 模块为例。</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">import</span> _ <span class="hljs-keyword">from</span> <span class="hljs-string">'lodash'</span>;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>如果想在一条<code>import</code>语句中，同时输入默认方法和其他接口，可以写成下面这样。</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">import</span> _, &#123; each, forEach &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'lodash'</span>;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>对应上面代码的<code>export</code>语句如下。</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params">obj</span>) </span>&#123;
  <span class="hljs-comment">// ···</span>
&#125;

<span class="hljs-keyword">export</span> <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">each</span>(<span class="hljs-params">obj, iterator, context</span>) </span>&#123;
  <span class="hljs-comment">// ···</span>
&#125;

<span class="hljs-keyword">export</span> &#123; each <span class="hljs-keyword">as</span> forEach &#125;;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>上面代码的最后一行的意思是，暴露出<code>forEach</code>接口，默认指向<code>each</code>接口，即<code>forEach</code>和<code>each</code>指向同一个方法。</p>
<p><code>export default</code>也可以用来输出类。</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">// MyClass.js</span>
<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> <span class="hljs-class"><span class="hljs-keyword">class</span> </span>&#123; ... &#125;

<span class="hljs-comment">// main.js</span>
<span class="hljs-keyword">import</span> MyClass <span class="hljs-keyword">from</span> <span class="hljs-string">'MyClass'</span>;
<span class="hljs-keyword">let</span> o = <span class="hljs-keyword">new</span> MyClass();
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-7">export 与 import 的复合写法</h2>
<p>如果在一个模块之中，先输入后输出同一个模块，<code>import</code>语句可以与<code>export</code>语句写在一起。</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">export</span> &#123; foo, bar &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'my_module'</span>;

<span class="hljs-comment">// 可以简单理解为</span>
<span class="hljs-keyword">import</span> &#123; foo, bar &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'my_module'</span>;
<span class="hljs-keyword">export</span> &#123; foo, bar &#125;;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>上面代码中，<code>export</code>和<code>import</code>语句可以结合在一起，写成一行。但需要注意的是，写成一行以后，<code>foo</code>和<code>bar</code>实际上并没有被导入当前模块，只是相当于对外转发了这两个接口，导致当前模块不能直接使用<code>foo</code>和<code>bar</code>。</p>
<p>模块的接口改名和整体输出，也可以采用这种写法。</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">// 接口改名</span>
<span class="hljs-keyword">export</span> &#123; foo <span class="hljs-keyword">as</span> myFoo &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'my_module'</span>;

<span class="hljs-comment">// 整体输出</span>
<span class="hljs-keyword">export</span> * <span class="hljs-keyword">from</span> <span class="hljs-string">'my_module'</span>;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>默认接口的写法如下。</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">export</span> &#123; <span class="hljs-keyword">default</span> &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'foo'</span>;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>具名接口改为默认接口的写法如下。</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">export</span> &#123; es6 <span class="hljs-keyword">as</span> <span class="hljs-keyword">default</span> &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'./someModule'</span>;

<span class="hljs-comment">// 等同于</span>
<span class="hljs-keyword">import</span> &#123; es6 &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'./someModule'</span>;
<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> es6;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>同样地，默认接口也可以改名为具名接口。</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">export</span> &#123; <span class="hljs-keyword">default</span> <span class="hljs-keyword">as</span> es6 &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'./someModule'</span>;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>ES2020 之前，有一种<code>import</code>语句，没有对应的复合写法。</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">import</span> * <span class="hljs-keyword">as</span> someIdentifier <span class="hljs-keyword">from</span> <span class="hljs-string">"someModule"</span>;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Ftc39%2Fproposal-export-ns-from" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/tc39/proposal-export-ns-from" ref="nofollow noopener noreferrer">ES2020</a>补上了这个写法。</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">export</span> * <span class="hljs-keyword">as</span> ns <span class="hljs-keyword">from</span> <span class="hljs-string">"mod"</span>;

<span class="hljs-comment">// 等同于</span>
<span class="hljs-keyword">import</span> * <span class="hljs-keyword">as</span> ns <span class="hljs-keyword">from</span> <span class="hljs-string">"mod"</span>;
<span class="hljs-keyword">export</span> &#123;ns&#125;;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-8">模块的继承</h2>
<p>模块之间也可以继承。</p>
<p>假设有一个<code>circleplus</code>模块，继承了<code>circle</code>模块。</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">// circleplus.js</span>

<span class="hljs-keyword">export</span> * <span class="hljs-keyword">from</span> <span class="hljs-string">'circle'</span>;
<span class="hljs-keyword">export</span> <span class="hljs-keyword">var</span> e = <span class="hljs-number">2.71828182846</span>;
<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">x</span>) </span>&#123;
  <span class="hljs-keyword">return</span> <span class="hljs-built_in">Math</span>.exp(x);
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>上面代码中的<code>export *</code>，表示再输出<code>circle</code>模块的所有属性和方法。注意，<code>export *</code>命令会忽略<code>circle</code>模块的<code>default</code>方法。然后，上面代码又输出了自定义的<code>e</code>变量和默认方法。</p>
<p>这时，也可以将<code>circle</code>的属性或方法，改名后再输出。</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">// circleplus.js</span>

<span class="hljs-keyword">export</span> &#123; area <span class="hljs-keyword">as</span> circleArea &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'circle'</span>;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>上面代码表示，只输出<code>circle</code>模块的<code>area</code>方法，且将其改名为<code>circleArea</code>。</p>
<p>加载上面模块的写法如下。</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">// main.js</span>

<span class="hljs-keyword">import</span> * <span class="hljs-keyword">as</span> math <span class="hljs-keyword">from</span> <span class="hljs-string">'circleplus'</span>;
<span class="hljs-keyword">import</span> exp <span class="hljs-keyword">from</span> <span class="hljs-string">'circleplus'</span>;
<span class="hljs-built_in">console</span>.log(exp(math.e));
<span class="copy-code-btn">复制代码</span></code></pre>
<p>上面代码中的<code>import exp</code>表示，将<code>circleplus</code>模块的默认方法加载为<code>exp</code>方法。</p>
<h2 data-id="heading-9">跨模块常量</h2>
<p>本书介绍<code>const</code>命令的时候说过，<code>const</code>声明的常量只在当前代码块有效。如果想设置跨模块的常量（即跨多个文件），或者说一个值要被多个模块共享，可以采用下面的写法。</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">// constants.js 模块</span>
<span class="hljs-keyword">export</span> <span class="hljs-keyword">const</span> A = <span class="hljs-number">1</span>;
<span class="hljs-keyword">export</span> <span class="hljs-keyword">const</span> B = <span class="hljs-number">3</span>;
<span class="hljs-keyword">export</span> <span class="hljs-keyword">const</span> C = <span class="hljs-number">4</span>;

<span class="hljs-comment">// test1.js 模块</span>
<span class="hljs-keyword">import</span> * <span class="hljs-keyword">as</span> constants <span class="hljs-keyword">from</span> <span class="hljs-string">'./constants'</span>;
<span class="hljs-built_in">console</span>.log(constants.A); <span class="hljs-comment">// 1</span>
<span class="hljs-built_in">console</span>.log(constants.B); <span class="hljs-comment">// 3</span>

<span class="hljs-comment">// test2.js 模块</span>
<span class="hljs-keyword">import</span> &#123;A, B&#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'./constants'</span>;
<span class="hljs-built_in">console</span>.log(A); <span class="hljs-comment">// 1</span>
<span class="hljs-built_in">console</span>.log(B); <span class="hljs-comment">// 3</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>如果要使用的常量非常多，可以建一个专门的<code>constants</code>目录，将各种常量写在不同的文件里面，保存在该目录下。</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">// constants/db.js</span>
<span class="hljs-keyword">export</span> <span class="hljs-keyword">const</span> db = &#123;
  <span class="hljs-attr">url</span>: <span class="hljs-string">'http://my.couchdbserver.local:5984'</span>,
  <span class="hljs-attr">admin_username</span>: <span class="hljs-string">'admin'</span>,
  <span class="hljs-attr">admin_password</span>: <span class="hljs-string">'admin password'</span>
&#125;;

<span class="hljs-comment">// constants/user.js</span>
<span class="hljs-keyword">export</span> <span class="hljs-keyword">const</span> users = [<span class="hljs-string">'root'</span>, <span class="hljs-string">'admin'</span>, <span class="hljs-string">'staff'</span>, <span class="hljs-string">'ceo'</span>, <span class="hljs-string">'chief'</span>, <span class="hljs-string">'moderator'</span>];
<span class="copy-code-btn">复制代码</span></code></pre>
<p>然后，将这些文件输出的常量，合并在<code>index.js</code>里面。</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">// constants/index.js</span>
<span class="hljs-keyword">export</span> &#123;db&#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'./db'</span>;
<span class="hljs-keyword">export</span> &#123;users&#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'./users'</span>;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>使用的时候，直接加载<code>index.js</code>就可以了。</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">// script.js</span>
<span class="hljs-keyword">import</span> &#123;db, users&#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'./constants/index'</span>;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-10">import()</h2>
<h3 data-id="heading-11">简介</h3>
<p>前面介绍过，<code>import</code>命令会被 JavaScript 引擎静态分析，先于模块内的其他语句执行（<code>import</code>命令叫做“连接” binding 其实更合适）。所以，下面的代码会报错。</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">// 报错</span>
<span class="hljs-keyword">if</span> (x === <span class="hljs-number">2</span>) &#123;
  <span class="hljs-keyword">import</span> MyModual <span class="hljs-keyword">from</span> <span class="hljs-string">'./myModual'</span>;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>上面代码中，引擎处理<code>import</code>语句是在编译时，这时不会去分析或执行<code>if</code>语句，所以<code>import</code>语句放在<code>if</code>代码块之中毫无意义，因此会报句法错误，而不是执行时错误。也就是说，<code>import</code>和<code>export</code>命令只能在模块的顶层，不能在代码块之中（比如，在<code>if</code>代码块之中，或在函数之中）。</p>
<p>这样的设计，固然有利于编译器提高效率，但也导致无法在运行时加载模块。在语法上，条件加载就不可能实现。如果<code>import</code>命令要取代 Node 的<code>require</code>方法，这就形成了一个障碍。因为<code>require</code>是运行时加载模块，<code>import</code>命令无法取代<code>require</code>的动态加载功能。</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">const</span> path = <span class="hljs-string">'./'</span> + fileName;
<span class="hljs-keyword">const</span> myModual = <span class="hljs-built_in">require</span>(path);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>上面的语句就是动态加载，<code>require</code>到底加载哪一个模块，只有运行时才知道。<code>import</code>命令做不到这一点。</p>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Ftc39%2Fproposal-dynamic-import" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/tc39/proposal-dynamic-import" ref="nofollow noopener noreferrer">ES2020提案</a> 引入<code>import()</code>函数，支持动态加载模块。</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">import</span>(specifier)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>上面代码中，<code>import</code>函数的参数<code>specifier</code>，指定所要加载的模块的位置。<code>import</code>命令能够接受什么参数，<code>import()</code>函数就能接受什么参数，两者区别主要是后者为动态加载。</p>
<p><code>import()</code>返回一个 Promise 对象。下面是一个例子。</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">const</span> main = <span class="hljs-built_in">document</span>.querySelector(<span class="hljs-string">'main'</span>);

<span class="hljs-keyword">import</span>(<span class="hljs-string">`./section-modules/<span class="hljs-subst">$&#123;someVariable&#125;</span>.js`</span>)
  .then(<span class="hljs-function"><span class="hljs-params">module</span> =></span> &#123;
    <span class="hljs-built_in">module</span>.loadPageInto(main);
  &#125;)
  .catch(<span class="hljs-function"><span class="hljs-params">err</span> =></span> &#123;
    main.textContent = err.message;
  &#125;);
<span class="copy-code-btn">复制代码</span></code></pre>
<p><code>import()</code>函数可以用在任何地方，不仅仅是模块，非模块的脚本也可以使用。它是运行时执行，也就是说，什么时候运行到这一句，就会加载指定的模块。另外，<code>import()</code>函数与所加载的模块没有静态连接关系，这点也是与<code>import</code>语句不相同。<code>import()</code>类似于 Node 的<code>require</code>方法，区别主要是前者是异步加载，后者是同步加载。</p>
<h3 data-id="heading-12">适用场合</h3>
<p>下面是<code>import()</code>的一些适用场合。</p>
<p>（1）按需加载。</p>
<p><code>import()</code>可以在需要的时候，再加载某个模块。</p>
<pre><code class="hljs language-javascript copyable" lang="javascript">button.addEventListener(<span class="hljs-string">'click'</span>, <span class="hljs-function"><span class="hljs-params">event</span> =></span> &#123;
  <span class="hljs-keyword">import</span>(<span class="hljs-string">'./dialogBox.js'</span>)
  .then(<span class="hljs-function"><span class="hljs-params">dialogBox</span> =></span> &#123;
    dialogBox.open();
  &#125;)
  .catch(<span class="hljs-function"><span class="hljs-params">error</span> =></span> &#123;
    <span class="hljs-comment">/* Error handling */</span>
  &#125;)
&#125;);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>上面代码中，<code>import()</code>方法放在<code>click</code>事件的监听函数之中，只有用户点击了按钮，才会加载这个模块。</p>
<p>（2）条件加载</p>
<p><code>import()</code>可以放在<code>if</code>代码块，根据不同的情况，加载不同的模块。</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">if</span> (condition) &#123;
  <span class="hljs-keyword">import</span>(<span class="hljs-string">'moduleA'</span>).then(...);
&#125; <span class="hljs-keyword">else</span> &#123;
  <span class="hljs-keyword">import</span>(<span class="hljs-string">'moduleB'</span>).then(...);
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>上面代码中，如果满足条件，就加载模块 A，否则加载模块 B。</p>
<p>（3）动态的模块路径</p>
<p><code>import()</code>允许模块路径动态生成。</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">import</span>(f())
.then(...);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>上面代码中，根据函数<code>f</code>的返回结果，加载不同的模块。</p>
<h3 data-id="heading-13">注意点</h3>
<p><code>import()</code>加载模块成功以后，这个模块会作为一个对象，当作<code>then</code>方法的参数。因此，可以使用对象解构赋值的语法，获取输出接口。</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">import</span>(<span class="hljs-string">'./myModule.js'</span>)
.then(<span class="hljs-function">(<span class="hljs-params">&#123;export1, export2&#125;</span>) =></span> &#123;
  <span class="hljs-comment">// ...·</span>
&#125;);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>上面代码中，<code>export1</code>和<code>export2</code>都是<code>myModule.js</code>的输出接口，可以解构获得。</p>
<p>如果模块有<code>default</code>输出接口，可以用参数直接获得。</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">import</span>(<span class="hljs-string">'./myModule.js'</span>)
.then(<span class="hljs-function"><span class="hljs-params">myModule</span> =></span> &#123;
  <span class="hljs-built_in">console</span>.log(myModule.default);
&#125;);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>上面的代码也可以使用具名输入的形式。</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">import</span>(<span class="hljs-string">'./myModule.js'</span>)
.then(<span class="hljs-function">(<span class="hljs-params">&#123;<span class="hljs-keyword">default</span>: theDefault&#125;</span>) =></span> &#123;
  <span class="hljs-built_in">console</span>.log(theDefault);
&#125;);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>如果想同时加载多个模块，可以采用下面的写法。</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-built_in">Promise</span>.all([
  <span class="hljs-keyword">import</span>(<span class="hljs-string">'./module1.js'</span>),
  <span class="hljs-keyword">import</span>(<span class="hljs-string">'./module2.js'</span>),
  <span class="hljs-keyword">import</span>(<span class="hljs-string">'./module3.js'</span>),
])
.then(<span class="hljs-function">(<span class="hljs-params">[module1, module2, module3]</span>) =></span> &#123;
   ···
&#125;);
<span class="copy-code-btn">复制代码</span></code></pre>
<p><code>import()</code>也可以用在 async 函数之中。</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">async</span> <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">main</span>(<span class="hljs-params"></span>) </span>&#123;
  <span class="hljs-keyword">const</span> myModule = <span class="hljs-keyword">await</span> <span class="hljs-keyword">import</span>(<span class="hljs-string">'./myModule.js'</span>);
  <span class="hljs-keyword">const</span> &#123;export1, export2&#125; = <span class="hljs-keyword">await</span> <span class="hljs-keyword">import</span>(<span class="hljs-string">'./myModule.js'</span>);
  <span class="hljs-keyword">const</span> [module1, module2, module3] =
    <span class="hljs-keyword">await</span> <span class="hljs-built_in">Promise</span>.all([
      <span class="hljs-keyword">import</span>(<span class="hljs-string">'./module1.js'</span>),
      <span class="hljs-keyword">import</span>(<span class="hljs-string">'./module2.js'</span>),
      <span class="hljs-keyword">import</span>(<span class="hljs-string">'./module3.js'</span>),
    ]);
&#125;
main();
<span class="copy-code-btn">复制代码</span></code></pre></div>  
</div>
            