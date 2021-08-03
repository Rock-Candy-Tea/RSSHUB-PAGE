
---
title: 'Babel 7.x 配置与使用'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=6691'
author: 掘金
comments: false
date: Mon, 02 Aug 2021 05:01:40 GMT
thumbnail: 'https://picsum.photos/400/300?random=6691'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>本文主要介绍 Babel 7 的基本使用方式与其新特性在 monorepos 类型项目中配置应用。可以从<a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fwjcj%2Fbabel-7-monorepo-demo" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/wjcj/babel-7-monorepo-demo" ref="nofollow noopener noreferrer">这里</a> <code>clone</code> 示例源码，简单的示例也可以使用 Babel 提供的<a href="https://link.juejin.cn/?target=https%3A%2F%2Fbabeljs.io%2Frepl%2F" target="_blank" rel="nofollow noopener noreferrer" title="https://babeljs.io/repl/" ref="nofollow noopener noreferrer">在线编译平台</a>。</p>
<h2 data-id="heading-0">开始</h2>
<p>Babel 是一个 JavaScript 编译器。主要用于将 ECMAScript 2015+ 代码转换成能够运行在当前或旧版本的浏览器或其他环境中的语法。</p>
<blockquote>
<p>语法转换；通过 Polyfill 方式在目标环境中添加缺失的特性（通过第三方 polyfill 模块，例如 core-js，实现）；源码转换 (codemods)。</p>
</blockquote>
<p>官网中提到 Babel 会为你做的几件事👆，这是因为 ECMAScript 2015+ 代码中除了包含新的语法，还包含一些新的特性：内置对象（如 <code>Promise</code>）、内置对象新增静态属性（如 <code>Array.from</code>）和实例属性（如 <code>[].includes</code>）。语法可以通过插件转换为 ES5 语法实现旧版浏览器兼容，而新增特性则通过注入 polyfill 实现，polyfill 新增特性到全局环境（<code>global scope</code>）、原生对象（如 <code>Array</code>）或其原型（如 <code>Array.prototype</code>）上，从而也会导致全局环境污染。Babel 使用 <code>core-js</code> 来提供的 polyfill。</p>
<p><strong><code>@babel/polyfill</code> 开始已废弃，Babel 7.4.0 版本开始不推荐使用</strong></p>
<p><code>@babel/polyfill</code> 是 Babel 提供 polyfill 独立出来的一个库。其包含 <code>core-js</code> 和一个自定义的 <code>regenerator runtime</code> 来模拟完整的 ES2015+ 环境，以前这个库本身等价于：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">import</span> <span class="hljs-string">"core-js/shim"</span>;  <span class="hljs-comment">// 包含 < Stage 4 的阶段提案</span>
<span class="hljs-keyword">import</span> <span class="hljs-string">"regenerator-runtime/runtime"</span>; <span class="hljs-comment">// 生成器函数（generator functions）</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>使用 <code>@babel/polyfill</code> 时会注入全部的 polyfill，这对于一个库/工具来说太多了，或者你无法完全控制代码的运行的环境，污染全局可能会带来一些问题。所以它仅适用于应用程序或命令行工具。现在的 <code>@babel/polyfill</code> 本身使用 <code>core-js v2</code> 中标准 ECMAScript 特性的 polyfill，即：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">import</span> <span class="hljs-string">"core-js/stable"</span>; <span class="hljs-comment">// Stage 4 的阶段提案</span>
<span class="hljs-keyword">import</span> <span class="hljs-string">"regenerator-runtime/runtime"</span>;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>如果你需要填充处于提案阶段（< Stage 4）的特性，需要安装 <code>core-js v2+</code> 并从其中导入对应的 polyfill，比如：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// for core-js v2:</span>
<span class="hljs-keyword">import</span> <span class="hljs-string">"core-js/fn/array/flat-map"</span>;
<span class="hljs-comment">// for core-js v3:</span>
<span class="hljs-keyword">import</span> <span class="hljs-string">"core-js/features/array/flat-map"</span>;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>而 <code>core-js v3</code> 也已经完全模块化，直接使用 <code>core-js</code> 可以根据需要单独引入某个 polyfill，配合 <code>@babel/preset-env</code> 可以根据目标环境智能的引入需要的 polyfill。所以 <code>@babel/polyfill</code> 的价值已经不大了。</p>
<h2 data-id="heading-1">常用命令</h2>
<pre><code class="copyable">npm install @babel/cli @babel/core --save-dev
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li><code>@babel/cli</code>：内置的 CLI 命令行工具，可通过命令行编译文件。</li>
<li><code>@babel/core</code>：Babel 核心功能模块。包含了解析、转换、生成相关 <a href="https://link.juejin.cn/?target=https%3A%2F%2Fbabeljs.io%2Fdocs%2Fen%2Fbabel-core%23transformsync" target="_blank" rel="nofollow noopener noreferrer" title="https://babeljs.io/docs/en/babel-core#transformsync" ref="nofollow noopener noreferrer">API</a>。</li>
</ul>
<p>常用命令：</p>
<pre><code class="hljs language-bash copyable" lang="bash">npx babel example.js
<span class="hljs-comment"># 指定输出文件和启动监听模式</span>
npx babel example.js --out-file compiled.js --watch
<span class="hljs-comment"># 简写</span>
npx babel example.js -o compiled.js -w

<span class="hljs-comment"># 编译目录</span>
npx babel src --out-dir lib
<span class="hljs-comment"># 简写</span>
npx babel src -d lib
<span class="copy-code-btn">复制代码</span></code></pre>
<p>更多 <code>babel</code> 命令查看<a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.babeljs.cn%2Fdocs%2Fbabel-cli" target="_blank" rel="nofollow noopener noreferrer" title="https://www.babeljs.cn/docs/babel-cli" ref="nofollow noopener noreferrer">这里</a>。</p>
<p><em>执行 npx babel 之前首先要安装 <code>@babel/cli</code> 和 <code>@babel/core</code>，否则 npx 将安装老旧的 <code>babel 6.x</code> 版本。</em></p>
<p>如果不想每次都需要输入 <code>npx</code> 和如此长的指令，可以将命令写入 npm 运行脚本，<code>npm run build</code> 编译 <code>src</code> 目录中的所有文件：</p>
<pre><code class="hljs language-json_ copyable" lang="json_">&#123;
  "scripts": &#123;
    "build": "babel src --out-dir lib --watch"
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>区别于 webpack、rollup 的编译方式，Babel 是文件到文件的编译，不需要指定从某个入口文件开始。</p>
<h2 data-id="heading-2">配置文件</h2>
<p>执行上面的 <code>babel</code> 命令，你会发生它什么都不会做，只是将代码拷贝到另一处。只有为 Babel 指定了插件（plugins）或预设（presets，一组插件），Babel 才会对代码进行转换。</p>
<p>通常通过创建配置文件实现 Babel 配置，Babel 7.x 中存在两种配置文件格式：</p>
<ul>
<li>
<p><code>项目范围配置</code>（Project-wide configuration）：使用 <code>babel.config.json</code> 文件，支持 <code>.js</code>, <code>.cjs</code>, <code>.mjs</code> 扩展名。后文中将称呼其为**<code>babel.config.json</code>**。</p>
</li>
<li>
<p><code>相对文件配置</code>（File-relative configuration）：使用 <code>.babelrc.json</code> 文件（<code>.babelrc</code> 是 <code>.babelrc.json</code> 的别名），同样支持不同的扩展名 <code>.js</code>, <code>.cjs</code>, <code>.mjs</code>。后文中将称呼其为**<code>.babelrc.json</code>**。</p>
</li>
</ul>
<p>这两种配置文件可以一起使用，也可以独立使用。如果你想对某文件或某目录的子集上运行某些转换插件，使用 <code>.babelrc.json</code>。
如果您的项目中有多个包（即多个 <code>package.json</code>）目录且需要独立的 Babel 配置，那么加入 <code>babel.config.json</code> 会很有用，这种情况通常在 <code>monorepo</code> 项目中（一个项目中多个子包，且子包间存在互相依赖的。后文中有专门针对此场景的 Babel 使用介绍）。如果只是常规项目（一个项目即一个包），使用 <code>.babelrc.json</code> 即可。</p>
<p><code>babel.config.json</code> 对整个项目生效，包括 <code>node_modules</code>，<code>babel.config.json</code> 作为通用配置在子包共享，同时每个子包也可以做个性配置项。</p>
<h2 data-id="heading-3">配置选项</h2>
<p>这里先介绍常规项目中常用的配置项，所有配置选项查看<a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.babeljs.cn%2Fdocs%2Foptions" target="_blank" rel="nofollow noopener noreferrer" title="https://www.babeljs.cn/docs/options" ref="nofollow noopener noreferrer">这里</a>。</p>
<pre><code class="hljs language-json_ copyable" lang="json_">// .babelrc.json
&#123;
  // 插件列表。详见👇
  "plugins": [], 
   // 预设列表。详见👇
  "presets": [],
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>配置项详解：</strong></p>
<h3 data-id="heading-4"><code>plugins</code>（插件）</h3>
<p>插件是小型的 JavaScript 程序，用于告诉 Babel 如何对代码进行转换。</p>
<p>Babel 的代码转换功能通过将插件（或预设）应用到配置文件来启动。<br></p>
<p>Babel 编译代码的过程分为三个阶段：</p>
<ol>
<li>解析（parse）：将代码字符串解析成 AST（抽象语法树）；</li>
<li>转换（transform：对 AST 进行转换，转换后依然还是 AST；</li>
<li>生成（generate）：将转换后的 AST 生成代码字符串。</li>
</ol>
<p>而插件分为 <code>语法插件</code>（Syntax Plugins）和 <code>转换插件</code>（Transform Plugins）两种。官方语法插件和转换插件的名称分别以 <code>@babel/plugin-syntax</code>、<code>@babel/plugin-transform</code> 开头。<br>
语法插件在解析阶段作用于解析器（<code>@babel/parser</code>），扩展其语法解析能力，通过转换插件来实现代码转换。如果已经配置相应的转换插件，则不需要指定语法插件，因为会自动启用它，所以提到 Babel 插件通常指的是转换插件。</p>
<p>例如添加 <code>@babel/plugin-transform-arrow-functions</code> 插件后可解析并转换箭头函数：</p>
<pre><code class="hljs language-json_ copyable" lang="json_">&#123;
  "plugins": [
    "@babel/plugin-transform-arrow-functions"
  ]
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>源码：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">var</span> a = <span class="hljs-function"><span class="hljs-params">b</span> =></span> b;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>转换后：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">var</span> a = <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params">b</span>) </span>&#123;
  <span class="hljs-keyword">return</span> b;
&#125;;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-5"><code>presets</code>（预设）</h3>
<p>表示一组插件的集合。<br></p>
<p>如果希望使用 Babel 将 ES2015（ES6）代码编译成 ES5，需要配置<a href="https://link.juejin.cn/?target=https%3A%2F%2Fbabeljs.io%2Fdocs%2Fen%2Fplugins-list%23es2015" target="_blank" rel="nofollow noopener noreferrer" title="https://babeljs.io/docs/en/plugins-list#es2015" ref="nofollow noopener noreferrer">很多插件</a>，一个一个插件进行安装配置十分不便。<br>
如果使用Babel 预设 <code>@babel/preset-es2015</code> 则特别简单，因为其包含了 ES2015 特性的所有插件。</p>
<pre><code class="hljs language-bash copyable" lang="bash">npm install @babel/preset-es2015 --save-dev 
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="hljs language-json_ copyable" lang="json_">// .babelrc.json
&#123;
  "plugins": [],
  "presets": [
    "@babel/preset-es2015"
  ],
  // 此选项即将被废弃。
  "env": &#123;
    "development": &#123;
      "presets": [["@babel/preset-react", &#123; "development": true &#125;]]
    &#125;
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>在 Babel 7 中，所有 <code>Stage-x</code> 预设（<code>babel-preset-es2015</code> 、<code>babel-preset-es2016</code> ~ <code>babel-preset-latest</code>）都已经废弃，使用 <code>@babel/preset-env</code>（详见👇） 替代。</p>
<h3 data-id="heading-6">插件顺序、传递参数</h3>
<p><strong>插件顺序</strong></p>
<p>插件的排列顺序很重要，如果两个转换插件都将处理某一段代码将根据下面规则执行：</p>
<ul>
<li>插件在预设前运行；</li>
<li>插件顺序从前往后排列；</li>
<li>预设顺序是颠倒的（从后往前）。</li>
</ul>
<pre><code class="hljs language-json_ copyable" lang="json_">&#123;
  "plugins": ["pluginA", "pluginB"],
  "presets": ["presetA", "presetB"]
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>执行顺序：pluginA => pluginB => presetB => presetA</p>
<p><strong>传递参数</strong></p>
<p>插件参数和预设参数的传递方式一样，将 <code>插件名/预设名</code> 和 <code>参数对象</code> 组成一个数组在配置中设置：</p>
<pre><code class="hljs language-json_ copyable" lang="json_">&#123;
  "plugins": [
    "pluginA",
    ["pluginA", &#123; "option1": value &#125;] // 传递参数
  ],
  "presets": [
    "presetA",
    ["presetA", &#123; "option1": value &#125;]
  ]
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-7">monorepos 项目</h2>
<p>monorepos 项目中存在多个子包，<code>babel.config.json</code> 和 <code>.babelrc.json</code> 可以配合使用。下面是 monorepos 场景一些常用到的配置选项：</p>
<pre><code class="hljs language-js copyable" lang="js">&#123;
  <span class="hljs-comment">// 继承其他配置文件中的配置，当前配置文件中的配置字段将合并到扩展文件的配置之上。</span>
  <span class="hljs-string">"extends"</span>: <span class="hljs-built_in">String</span>,
  <span class="hljs-comment">// 指定仅适用于存储库中某些子目录的配置</span>
  <span class="hljs-string">"overrides"</span>: [],
  <span class="hljs-comment">// 匹配目录或文件。通常与 overrides 一起使用</span>
  <span class="hljs-string">"test"</span>: MatchPattern | <span class="hljs-built_in">Array</span><MatchPattern>,
  <span class="hljs-comment">// babel 默认情况下不会加载任何子包中的 .babelrc.json，除非 babel.config.js 中配置了 babelrcRoots 选项。</span>
  <span class="hljs-comment">// 例如 ['.', './packages/*'] 表示对当前根目录和所有子包开启 .babelrc.json 的加载，根目录可同时存在 babel.config.js 和 .babelrc.json。</span>
  <span class="hljs-string">"babelrcRoots"</span>: [],
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>下面👇选项仅允许作为 Babel 程序选项使用。例如 <code>babel-loader</code> 的 <code>options</code> 选项中（下面有示例）、命令行选项中（<code>babel --rootMode=upward</code>）等：</p>
<pre><code class="hljs language-json_ copyable" lang="json_">&#123;
  // “根”目录初始路径，默认为 opts.cwd
  "root": string,
  // 项目最终 'root' 值的不同方式，有三个选项：
    // - 'root'：传递 root 值不变
    // - 'upward'：自动向上找 babel.config.json 做为根目录位置，没找到就抛错；
    // - upward-optional：类似 upward，没找到回退。
  "rootMode": string,
  // Babel 默认在“根”目录自动搜索 babel.config.json 作为项目范围配置，此选项可以指定 项目范围配置文件，从而覆盖默认的搜索行为。
  "configFile": string | boolean,
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>结合一个 monorepos 项目（如下目录结构）对上面的配置选项进行使用说明：</p>
<pre><code class="copyable">.
├── packages
│   ├── package-a 
│   │    ├── src
│   │    │    └── index.js
│   │    ├── .babelrc.json
│   │    └── package.json
│   │
│   └── package-b
│        ├── src
│        │    └── index.js
│        ├── .babelrc.json
│        └── package.json
│
├── babel.config.json
└── package.json
<span class="copy-code-btn">复制代码</span></code></pre>
<p>Babel 7 中引入了一个 <code>root</code>（根）的概念，默认为当前工作目录（<code>process.cwd()</code>）。Babel 将在此根目录中自动搜索 <code>babel.config.json</code> 文件，指定 <code>"configFile"</code> 选项可以指定项目范围配置文件，从而覆盖此行为。</p>
<p>通常可以将所有子包的 Babel 配置放在“根”目录的 <code>babel.config.json</code> 中，通过 <code>"overrides"</code> 选项可以对项目中某些子目录文件进行独立配置。
比如下面👇 <code>babel.config.json</code> 中 <code>"@babel/preset-env"</code> 预设是共享的，但对 <code>package-a</code> 中的 JSX 元素进行了 <code>automatic</code> 模式转换（引入了 <code>react/jsx-runtime</code> 模块），其他包中的文件则使用经典的 <code>classic</code> 转换（将 jsx 转换为 <code>React.createElement</code> 调用）。</p>
<pre><code class="hljs language-json_ copyable" lang="json_">// babel.config.json
&#123;
  "presets": [
    "@babel/preset-env",
    ["@babel/preset-react", &#123; "runtime": "classic" &#125;]
  ],
  "overrides": [&#123;
    "test": "./packages/package-a",
    "presets": [
      ["@babel/preset-react", &#123; "runtime": "automatic" &#125;]
    ]
  &#125;]
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><em><code>@babel/preset-env</code> 和 <code>@babel/preset-react</code> 的详细使用可查看<a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fwjcj%2Fblog%2Fissues%2F39" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/wjcj/blog/issues/39" ref="nofollow noopener noreferrer">Babel 常用插件、预设详解</a>。</em></p>
<p>如果你想在特定子包中运行 Babel（当前工作目录与 Babel “根”目录不一致时），上面的配置将会出现问题。比如你 <code>cd ./packages/package-a</code> 目录下后执行 <code>webpack</code> 打包将报错。</p>
<p>在 <code>babel-loader</code> 配置选项中添加 <code>rootMode: 'upward'</code> 就可以恢复正常👇，<code>rootMode: 'upward'</code> 表示 Babel 会自动向上找 <code>babel.config.json</code> 做为“根”目录位置（即<code>root</code> 选项的值）。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-built_in">module</span>.exports = &#123;
  <span class="hljs-attr">mode</span>: <span class="hljs-string">'development'</span>,
  <span class="hljs-attr">module</span>: &#123;
    <span class="hljs-attr">rules</span>: [
      &#123;
        <span class="hljs-attr">test</span>: <span class="hljs-regexp">/\.(js|jsx)$/</span>,
        loader: <span class="hljs-built_in">require</span>.resolve(<span class="hljs-string">'babel-loader'</span>),
        <span class="hljs-attr">options</span>: &#123;
          <span class="hljs-attr">rootMode</span>: <span class="hljs-string">'upward'</span>,
        &#125;
      &#125;
    ]
  &#125;
&#125;;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>Babel 默认情况下不会加载任何子包中的 <code>.babelrc.json</code>。<code>babel.config.json</code> 设置 <code>babelrcRoots</code> 后才会启用。下面配置表示启用所有子包的 <code>.babelrc.json</code> 文件配置。
此选项通常用于替代 <code>overrides</code> 选项来实现子包的个性配置。</p>
<pre><code class="hljs language-json_ copyable" lang="json_">&#123;
  "babelrcRoots": ["./packages/*"]
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>Babel 配置选项非常多，查看更多选项请查看<a href="https://link.juejin.cn/?target=https%3A%2F%2Fbabeljs.io%2Fdocs%2Fen%2Foptions" target="_blank" rel="nofollow noopener noreferrer" title="https://babeljs.io/docs/en/options" ref="nofollow noopener noreferrer">官网文档</a>。</p>
<h2 data-id="heading-8">参考</h2>
<ul>
<li><a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.babeljs.cn%2Fdocs%2F" target="_blank" rel="nofollow noopener noreferrer" title="https://www.babeljs.cn/docs/" ref="nofollow noopener noreferrer">Babel</a></li>
<li><a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fjamiebuilds%2Fbabel-handbook%2Fblob%2Fmaster%2Ftranslations%2Fzh-Hans%2Fuser-handbook.md%23toc-babel-core" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/jamiebuilds/babel-handbook/blob/master/translations/zh-Hans/user-handbook.md#toc-babel-core" ref="nofollow noopener noreferrer">Babel 用户手册</a></li>
</ul></div>  
</div>
            