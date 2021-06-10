
---
title: 'Node 最新 Module 导入导出规范'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/98d4e0b7eaf74db2b64b43628c4eaaae~tplv-k3u1fbpfcp-zoom-1.image'
author: 掘金
comments: false
date: Wed, 09 Jun 2021 19:48:54 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/98d4e0b7eaf74db2b64b43628c4eaaae~tplv-k3u1fbpfcp-zoom-1.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>作者：ademily</p>
<h3 data-id="heading-0">前言</h3>
<p>Node.js 包模块最新规范提供了避免暴露特定文件、API 的能力，利于代码规范和仓库依赖治理。大力智能前端团队同学便对 Node 包模块最新规则进行了详尽的研究。本文就为大家带来最新的 Node 包模块导入导出规则，希望大家以后在工作中能够得心应手得处理这类情况。</p>
<blockquote>
<p>原文：<a href="https://nodejs.org/api/packages.html#packages%5C_modules%5C_packages" target="_blank" rel="nofollow noopener noreferrer">nodejs.org/api/package…</a></p>
</blockquote>
<p>包模块历史变更：</p>

































<table><thead><tr><th>版本</th><th>变更</th></tr></thead><tbody><tr><td>v14.13.0</td><td>新增 <code>"exports"</code> 模式（<code>"exports"</code> patterns）</td></tr><tr><td>v14.6.0</td><td>新增 <code>"imports"</code> 字段</td></tr><tr><td>v13.7.0、v12.16.0</td><td>条件导出不再使用特殊标识（Unflag conditional exports）</td></tr><tr><td>v13.6.0、v12.16.0</td><td>通过名称自引用不再使用特殊标识（Unflag self-referencing a package using its name.）</td></tr><tr><td>v12.7.0</td><td>引入 <code>"exports"</code> 这个 <code>package.json</code> 新字段，作为经典字段 <code>"main"</code> 的更强大的代替</td></tr><tr><td>v12.0.0</td><td>新增 通过 <code>package.json</code> 中 <code>"type"</code> 字段，使得 <code>.js</code> 文件会被视为 ES模块。</td></tr></tbody></table>
<h3 data-id="heading-1">一. 介绍</h3>
<p>包（package）是一个由 <code>package.json</code> 描述的文件夹树。包由包含 <code>package.json</code> 的文件夹和所有子文件夹组成，直到下一个含另一个 <code>package.json</code> 的文件夹，或者 <code>node_modules</code> 文件夹。</p>
<p>本页为大家介绍如何书写 <code>package.json</code>。页面底部还有 Node.js 定义的 <code>package.json</code> 字段供参考。</p>
<h3 data-id="heading-2">二. 判断模块系统</h3>
<p>当作为初始输入传递给 <code>node</code>，或在ES模块代码中被 <code>import</code> 语句引用时，Node.js 会将以下内容视为 ESM 模块：</p>
<ul>
<li>
<p>以 <code>.mjs</code> 结尾的文件</p>
</li>
<li>
<p>以 <code>.js</code> 结尾的文件，且最近的父 <code>package.json</code> 的顶层 <code>"type"</code> 值为 <code>"module"</code></p>
</li>
<li>
<p>将标志为 <code>--input-type=module</code> 的字串，作为 <code>--eval</code> 的参数传入或通过 <code>STDIN</code> 传入 <code>node</code></p>
</li>
</ul>
<p>Node.js 会将所有其他形式的输入视为 CommonJS，例如 <code>.js</code> 文件们最近的父 <code>package.json</code> 没有 <code>"type"</code> 字段，或启动 <code>node</code> 时没有传入 <code>--input-type</code> 标志。之所以保留 CommonJS 模式，是为了向后兼容。虽然目前 Node.js 对 CommonJS 和 ESM 模块 都支持，但我们最好尽可能地明确使用哪种。</p>
<p>当以下情况作为初始输入启动 <code>node</code>，或在 ESM 模块代码中的使用 <code>import</code> 语句引用时，Node.js 会将其视为 CommonJS：</p>
<ul>
<li>
<p>以 <code>.cjs</code> 结尾的文件</p>
</li>
<li>
<p>以 <code>.js</code> 结尾的文件，且最近的父 <code>package.json</code> 中顶层字段 <code>"type"</code> 值为 <code>"commonjs"</code></p>
</li>
<li>
<p>将标志 <code>--input-type=commonjs</code> 作为 <code>--eval</code> 或 <code>--print</code> 的参数，或通过 <code>STDIN</code> 传递到 <code>node</code></p>
</li>
</ul>
<p>即使在所有源码都是 CommonJS 的情况下，包作者也应该在 <code>package.json</code> 中包含 <code>"type"</code> 字段。明确包的 <code>"type"</code>，可以在 Node.js 的默认类型发生变化的情况下对包进行未来的保护，而且也可以让构建工具和 loaders 更容易明确如何解析包内的文件。</p>
<h4 data-id="heading-3">1. package.json 和文件扩展名</h4>
<p>在一个包中，<code>package.json</code> 的 <code>"type"</code> 字段定义了 Node.js 应该如何解析 <code>.js</code> 文件。如果 <code>package.json</code> 没有 <code>"type"</code> 字段，那么 <code>.js</code> 文件将被视为 CommonJS 模块。</p>
<p>当 <code>package.json</code> 的 <code>"type"</code> 值为 <code>"module"</code>，则 Node.js 会将该包中的 <code>.js</code> 文件解析为使用 ESM 模块语法。</p>
<p><code>"type"</code> 字段不仅适用于初始化入口文件（<code>node my-app.js</code>），也适用于 <code>import</code> 声明和 <code>import()</code> 表达式所引用的文件。</p>
<pre><code class="copyable">// my-app.js 被当做ES模块，因为 package.json中 "type" 为 "module"

import './startup/init.js'。
// 由于 ./startup 不包含 package.json 文件，因此继承了上一级的 "type" 值，所以作为 ES模块加载

import 'commonjs-package';
// 由于./node_modules/commonjs-package/package.json 缺乏 "type"字段或包含 `"type":"commonjs"`，所以该文件以 CommonJS 进行加载

import './node_modules/commonjs-package/index.js'。
// 由于./node_modules/commonjs-package/package.json 缺乏 "type"字段或包含 `"type":"commonjs"`，所以该文件以 CommonJS 进行加载
<span class="copy-code-btn">复制代码</span></code></pre>
<p>以 <code>.mjs</code> 结尾的文件总是作为 ESM 模块加载，且不受最近的父 <code>package.json</code> 的影响。</p>
<p>同样的，以 <code>.cjs</code> 结尾的文件总是作为 CommonJS 加载，且不受最近的父 <code>package.json</code> 的影响。</p>
<pre><code class="copyable">import './legacy-file.cjs'。
// 以 CommonJS 的形式加载，因为 .cjs 总是以 CommonJS 的形式加载

import 'commonjs-package/src/index.mjs'; 
//以 ES模块加载，因为 .mjs 总是作为 ES 模块形式进行加载
<span class="copy-code-btn">复制代码</span></code></pre>
<p><code>.mjs</code> 和 <code>.cjs</code> 扩展名能让我们在一个包中使用两种模式：</p>
<ul>
<li>
<p>在一个 <code>"type": "module"</code> 的包中，Node.js 可以将后缀为 <code>.cjs</code> 的特定文件解释为 CommonJS（因为在 <code>"module"</code> 包中，<code>.js</code> 和 <code>.mjs</code> 文件都被视为 ES模块）。</p>
</li>
<li>
<p>在一个 <code>"type": "commonjs"</code> 的包中，Node.js 可以将后缀为 <code>.mjs</code> 的特定文件解释为 ES模块（因为在 <code>"commonjs"</code> 包中，<code>.js</code> 和 <code>.cjs</code> 文件都被视为 CommonJS）。</p>
</li>
</ul>
<h4 data-id="heading-4">2. --input-type 标志</h4>
<p>当字串作为 <code>--eval</code>（或 <code>-e</code>）参数或者通过 <code>STDIN</code> 传递到 <code>node</code> 时，一旦设置了 <code>--input-type=module</code> 标志，那么这些字串会被视为 ESM 模块。</p>
<pre><code class="copyable">node --input-type=module --eval "import &#123; sep &#125; from 'path'; console.log(sep);"

echo "import &#123; sep &#125; from 'path'; console.log(sep);" | node --input-type=module
<span class="copy-code-btn">复制代码</span></code></pre>
<p>同样的，我们还有 <code>--input-type=commonjs</code> 用于显式地将字符串输入作为 CommonJS 运行。如果 <code>--input-type</code> 没有被指定，默认为 CommonJS 模式。</p>
<h3 data-id="heading-5">三. 包入口（Package entry points）</h3>
<p>在 <code>package.json</code> 文件中，有两个字段可以定义包入口：<code>"main"</code> 和 <code>"exports"</code>。所有版本的 Node.js 都支持 <code>"main"</code> 字段，但它的功能是有限的：它只定义包的主入口。</p>
<p><code>"exports"</code> 字段算是 <code>"main"</code> 的替代品，它既可以定义包的主入口，又封闭了包，<strong>防止其他未被定义的内容被访问</strong>。这种封闭允许模块作者为他们的包定义公共接口。</p>
<p>如果同时定义了 <code>"exports"</code> 和 <code>"main"</code>，<code>"exports"</code> 字段优先于 <code>"main"</code>。<code>"exports"</code> 并不是 ESM 模块 或 CommonJS 所特有的；<code>"exports"</code> 如果存在的话，就会覆盖 <code>"main"</code> 。因此， <code>**"main"**</code> <strong>不能作为 CommonJS 的降级回落，但它可以作为不支持</strong> <code>**"exports"**</code> <strong>字段的 Node.js 旧版本的降级回落</strong>。</p>
<p>在 <code>"exports"</code> 中使用“条件导出”（Conditional exports）可以为每个环境定义不同入口，包括包是通过 <code>require</code> 还是 <code>import</code> 来引用。关于如何在一个包中同时支持 CommonJS 和 ESM 模块，请参考 “双 CommonJS/ESM 模块包”部分。</p>
<p><strong>注意</strong>：使用 <code>"exports"</code> 字段可以防止包的使用者使用其他未定义的入口点，包括 <code>package.json</code>（例如：<code>require('your-package/package.json')</code>。<strong>这很可能是一个重大变更</strong>。</p>
<p>为了使 <code>"exports"</code> 的引入不具有破坏性，请确保之前支持的每个入口都被导出。最好明确指定各个入口，这样包的就有了明确的公共API定义。例如，一个项目如果之前导出了<code>main</code>、<code>lib</code>、<code>feature</code> 和 <code>package.json</code>，那么 <code>package.exports</code> 可以使用如下写法：</p>
<pre><code class="copyable">&#123;
  "name": "my-mod",
  "exports": &#123;
    ".": "./lib/index.js",
    "./lib": "./lib/index.js",
    "./lib/index": "./lib/index.js",
    "./lib/index.js": "./lib/index.js",
    "./feature": "./feature/index.js",
    "./feature/index.js": "./feature/index.js",
    "./package.json": "./package.json"
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>另外，一个项目可以选择导出整个文件夹：</p>
<pre><code class="copyable">&#123;
  "name": "my-mod",
  "exports": &#123;
    ".": "./lib/index.js",
    "./lib": "./lib/index.js",
    "./lib/*": "./lib/*.js",
    "./feature": "./feature/index.js",
    "./feature/*": "./feature/*.js",
    "./package.json": "./package.json"
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>在万不得已时，可以通过 <code>"./*": "./*"</code> 来导出整个包的根目录，此时“封闭”功能也就不起作用了 <em>。</em> 这种将包内的所有文件暴露出去的方式，以禁用封闭为代价的同时，也提供了潜在的工具便利。由于<strong>Node.js 中的 ES</strong> <strong>M</strong> <strong>模块加载器强制使用完整路径</strong>，因此导出根目录而不是显式的定义入口，前者的表现力比我们之前的例子要差很多。这不仅失去了封闭，而且调用模块的人也无法直接使用 <code>import feature from 'my-mod/feature'</code>，因为他们需要写下完整路径 <code>import feature from 'my-mod/feature/index.js</code>。</p>
<h4 data-id="heading-6">1. 主入口的导出（Main entry point export）</h4>
<p>要设置包的主入口，最好在 <code>package.json</code> 中同时定义 <code>"exports"</code> 和 <code>"main"</code>。</p>
<pre><code class="copyable">&#123;
  "main": "./main.js",
  "exports": "./main.js"
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>当定义了 <code>"exports"</code> 字段，所有子路径都会被封闭，不再对使用者开放。例如，<code>require('pkg/subpath.js')</code> 会抛出 <a href="https://nodejs.org/api/errors.html#errors_err_package_path_not_exported" target="_blank" rel="nofollow noopener noreferrer">ERR_PACKAGE_PATH_NOT_EXPORTED</a> 错误。</p>
<p>这种对导出的封闭不仅为工具提供了更可靠的接口保证，也为处理包的升级提供了保证。这不是一个严格意义上的封闭，因为直接 require 任何绝对路径，如 <code>require('/path/to/node_modules/pkg/subpath.js')</code> 仍然会加载 <code>subpath.js</code>。</p>
<h4 data-id="heading-7">2. 子路径的导出（Subpath exports）</h4>
<p>当使用 <code>"exports"</code> 字段时，可以将主入口视为 <code>"."</code> 路径，然后构造自定义路径：</p>
<pre><code class="copyable">&#123;
  "main": "./main.js",
  "exports": &#123;
    ".": "./main.js",
    "./submodule": "./src/submodule.js"
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>目前只有在 <code>"exports"</code> 中定义的子路径才能被导入：</p>
<pre><code class="copyable">import submodule from 'es-module-package/submodule';
//加载./node_modules/es-module-package/src/submodule.js。
<span class="copy-code-btn">复制代码</span></code></pre>
<p>导入其他子路径就会报错：</p>
<pre><code class="copyable">import submodule from 'es-module-package/private-module.js';
// 抛错 ERR_PACKAGE_PATH_NOT_EXPORTED
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-8">3. 子路径的导入（Subpath imports）</h4>
<p>除了 <code>"exports"</code> 字段之外，还可以定义内部包导入映射，这些映射只适用于在包内部导入指定内容。<code>imports</code> 字段中定义的入口必须一直以 <code>#</code> 开头，以确保它们与包的对外指定内容相区别。例如，<code>imports</code> 字段也可以做内部模块的条件导出：</p>
<pre><code class="copyable">// package.json
&#123;
  "imports": &#123;
    "#dep": &#123;
      "node": "dep-node-native",
      "default": "./dep-polyfill.js"
    &#125;
  &#125;,
  "dependencies": &#123;
    "dep-node-native": "^1.0.0"
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>上述例子展示了，当处于非 node 环境中时，<code>import '#dep'</code> 并不能获取到外部包<code>dep-node-native</code>，而会获取本地文件 <code>./dep-polyfill.js</code>。与 <code>"exports"</code> 字段不同，<code>"imports"</code> 字段允许映射外部包。<code>imports</code> 字段的解析规则与 <code>exports</code> 字段类似。</p>
<h4 data-id="heading-9">4. 子路径模式（Subpath patterns）</h4>
<p>对于 <code>exports</code> 或 <code>imports</code> 数量较少的包，我们建议明确列出每个子路径入口。但对于有大量子路径的包来说，这可能会导致 <code>package.json</code> 出现臃肿和维护问题。对于这种有大量路径的情况，我们可以用子路径导出模式来代替：</p>
<pre><code class="copyable">// ./node_modules/es-module-package/package.json
&#123;
  "exports": &#123;
    "./features/*": "./src/features/*.js"
  &#125;,
  "imports": &#123;
    "#internal/*": "./src/internal/*.js"
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>左侧匹配模式必须都以 <code>*</code> 结尾。右侧所有的 <code>*</code> 实例都将被替换成左侧的值，包括它是否包含/分隔符。</p>
<pre><code class="copyable">import featureX from 'es-module-package/features/x';
//加载./node_modules/es-module-package/src/features/x.js。

import featureY from 'es-module-package/features/y/y';
//加载./node_modules/es-module-package/src/features/y/y.js。

import internalZ from '#internal/z';
// 加载 ./node_modules/es-module-package/src/internal/z.js。
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这是一个直接的静态替换，没有对文件扩展名进行任何特殊处理。在上述例子中，<code>pkg/features/x.json</code> 将在映射中被解析为 <code>./src/features/x.json.js</code>。<code>exports</code> 的属性是否能维持为静态可枚举，取决于导出模式如何设置，比如导出模式的右侧匹配写为 <code>**</code> 还是列出一大串文件列表。由于 <code>exports</code> 的目标中禁止写 <code>node_moduels</code> 路径，所以模式匹配只能写包本身的文件。</p>
<h4 data-id="heading-10">5. 子路径文件夹映射（Subpath folder mappings）</h4>
<blockquote>
<p>稳定性：0 - 已废弃。使用子路径模式代替。 <br>
由于已废弃，此处就不放译文了。</p>
</blockquote>
<h4 data-id="heading-11">6. Exports 语法糖（Exports sugar）</h4>
<p>当 <code>"."</code> 是唯一的导出，<code>"exports"</code> 字段为这种情况提供了语法糖。当 <code>"."</code> 导出有降级回落的数组或字符串值，那么 <code>"exports"</code> 字段可以直接设置为这个值。</p>
<pre><code class="copyable">&#123;
  "exports": &#123;
    ".": "./main.js"
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>可改写为：</p>
<pre><code class="copyable">&#123;
  "exports": "./main.js"
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-12">7. 条件导出（Conditional exports）</h4>
<p>条件导出提供了一种根据特定条件映射到不同路径的方法。CommonJS 和 ES模块导入都支持条件导出。例如，一个包如果想为 <code>require()</code> 和 <code>import</code> 提供不同的 ES模块导出，可以写为：</p>
<pre><code class="copyable">// package.json
&#123;
  "main": "./main-require.cjs",
  "exports": &#123;
    "import": "./main-module.js",
    "require": "./main-require.cjs"
  &#125;,
  "type": "module"
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>Node.js开箱即支持以下情况：</p>
<ul>
<li>
<p><code>"import"</code> - 当包通过 <code>import</code> 或 <code>import()</code> 加载，或通过 ECMAScript 模块加载器的任何顶层导入或解析操作加载时，该条件就会匹配。无论目标文件的模块格式如何，都适用。 <code>_"import"_</code> 总是与 <code>_"require"_</code> 互斥。</p>
</li>
<li>
<p><code>"require"</code> - 当包通过 <code>require()</code> 加载时匹配。被引用的文件应该可以用 <code>require()</code> 加载，尽管该条件与目标文件的模块格式无关。预期的格式包括 CommonJS、JSON 和本地插件，但不包括 ES模块，因为 <code>require()</code> 并不支持它们。 <code>_"require"_</code> 总是与 <code>_"import"_</code> 互斥。</p>
</li>
<li>
<p><code>"node"</code> - 匹配任何 Node.js 环境。可以是 CommonJS 或 ESM 模块文件。这个条件应该总是在 <code>_"import"_</code> 或 <code>_"require"_</code> 之后。</p>
</li>
<li>
<p><code>"default"</code> - 默认的降级条件。可以是一个 CommonJS 或 ESM 模块文件。这个条件应该总是排在最后。</p>
</li>
</ul>
<p>在 <code>"exports"</code> 对象中，键序很重要。在条件匹配过程中，排序靠前的入口具有较高的优先级。通常规则是，这些条件应该从最特殊到最不特殊来排序。</p>
<p>其他条件如 <code>"browser"</code>、<code>"electron"</code>、<code>"deno"</code>、<code>"react-native"</code> 等，对 Node.js 来说是不可用的，因此会被忽略。Node.js 以外的运行时或工具可以酌情使用它们。未来可能会出现更多关于条件名称的限制、定义或引导。</p>
<p>使用 <code>"import"</code> 和 <code>"require"</code> 条件可能会导致一些危害，这将在“CommonJS/ES 双模块包部分”进一步解释。子路径也可以使用条件导出，如下：</p>
<pre><code class="copyable">&#123;
  "main": "./main.js",
  "exports": &#123;
    ".": "./main.js",
    "./feature": &#123;
      "node": "./feature-node.js",
      "default": "./feature.js"
    &#125;
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>上面这段代码就展示了：在 Node.js 和其他 JS环境 使用 <code>require('pkg/feature')</code> 和 <code>import('pkg/feature')</code> 还有不同的实现。</p>
<p>当使用环境分支时，需尽量包含 <code>"default"</code> 进行兜底。提供 <code>"default"</code> 可以确保任何未知的 JS 环境都能够使用这个通用的实现，这也避免未知的 JS 环境为了支持条件导出而不得不假装成现有环境。也因为如此，使用 <code>"node"</code> 和 <code>"default"</code> 条件分支通常比使用 <code>"node"</code> 和 <code>"browser"</code> 条件分支更可取。</p>
<h4 data-id="heading-13">8. 嵌套条件（Nested conditions）</h4>
<p>除了直接映射，Node.js 还支持嵌套条件对象。例如：定义一个只供 Node.js 使用双模式入口，而浏览器端无法使用这个双模式入口</p>
<pre><code class="copyable">&#123;
  "main": "./main.js",
  "exports": &#123;
    "node": &#123;
      "import": "./feature-node.mjs",
      "require": "./feature-node.cjs"
    &#125;,
    "default": "./feature.mjs",
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>条件继续按次序匹配扁平化后的条件。如果一个嵌套条件没有任何映射，它将继续检查父条件的剩余条件。在这种方式下，嵌套条件的行为类似于嵌套的 JavaScript <code>if</code> 语句。</p>
<h4 data-id="heading-14">9. 处理用户条件（Resolving user conditions）</h4>
<p>在运行 Node.js 时，使用 <code>--conditions</code> 标志可以添加自定义条件：</p>
<pre><code class="copyable">node --conditions=development main.js
<span class="copy-code-btn">复制代码</span></code></pre>
<p>当恰当地解析现有的 <code>"node"</code>、 <code>"default"</code>、<code>"import"</code> 和 <code>"require"</code> 条件时，上面这段代码会在包的导入和导出中解析 <code>"development"</code> 条件。可以添加任意多的自定义条件，只需要一直添加重复的 <code>--conditions</code> 即可。</p>
<h4 data-id="heading-15">10. 使用包名称进行自我引用（Self-referencing a package using its name）</h4>
<p>在包内部，<code>package.json</code> 中 <code>"exports"</code> 定义的值可以被用作包内引用的名称。假设 <code>package.json</code> 如下：</p>
<pre><code class="copyable">// package.json
&#123;
  "name": "a-package",
  "exports": &#123;
    ".": "./main.mjs",
    "./foo": "./foo.js"
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>然后，_该包中_的任何模块都可以在包内被引用：</p>
<pre><code class="copyable">// ./a-module.mjs
import &#123; something &#125; from 'a-package'; // Imports "something" from ./main.mjs.
<span class="copy-code-btn">复制代码</span></code></pre>
<p>自引用只在 <code>package.json</code> 有 <code>"exports"</code> 的情况下才能使用，并且只允许导入该 <code>"exports"</code>（在 <code>package.json</code> 中）允许的内容。所以按照上例中 <code>package.json</code> 的定义，下面的代码会产生一个运行时错误：</p>
<pre><code class="copyable">// ./another-module.mjs。

// Imports "another" from ./m.mjs。失败的原因是
// "package.json" 中的 "exports" 字段
// 没有提供名为 "./m.mjs" 的导出。
import &#123; another &#125; from 'a-package/m.mjs';
<span class="copy-code-btn">复制代码</span></code></pre>
<p>当使用 <code>require</code> 时自引用也是可行的，无论是在 ES模块 还是在 CommonJS 模块中。例如：</p>
<pre><code class="copyable">// ./a-module.js
const &#123; something &#125; = require('a-package/foo'); // Loads from ./foo.js.
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-16">四. 双 CommonJS/ESM 模块包（Dual CommonJS/ES Module packages）</h3>
<p>在 Node.js 支持 ESM 模块之前，包作者在包内同时放入 CommonJS 和 ESM 模块源码是一种常见的模式，方式为：在 <code>package.json</code> 的 <code>"main"</code> 字段指定 CommonJS 入口，在 <code>"module"</code> 字段指定ES模块入口。这使得 Node.js 能够正常运行 CommonJS 入口，而其他打包构建工具等则使用 ES模块入口，因为 Node.js 会忽略（并且仍然忽略）顶层的 <code>"module"</code> 字段。</p>
<p>Node.js 现在可以运行 ESM 模块 入口，一个包可以同时包含 CommonJS 和 ESM 模块 入口（可以通过单独的指定内容如 <code>"pkg"</code> 和 <code>"pkg/es-module"</code>，也可以通过“条件导出”将两者放在同一个指定内容上）。与 <code>"module"</code> 只被打包程序使用，或是在 Node.js 执行前 ESM 模块文件被转化为 CommonJS 的情况不同，ESM 模块入口 引用的文件是直接作为 ESM 模块 使用的。</p>
<h4 data-id="heading-17">双包危害（Dual package hazard）</h4>
<p>当一个应用使用一个同时提供 CommonJS 和 ES模块源 的包时，如果这两个版本的包都被加载，那么就有可能出现某些bug。这种潜在的风险来自这样一个事实：由 <code>const pkgInstance = require('pkg')</code> 创建的 <code>pkgInstance</code> 与由 <code>import pkgInstance from 'pkg'</code> （或像 <code>'pkg/module'</code> 这样的替代主路径）创建的 <code>pkgInstance</code> 并不相同。同一个包的两个版本在同一运行时环境中被加载产生的影响，被称为 "双包危险"。虽然应用程序或包不太可能故意直接加载两个版本，但常见的情况是：应用程序加载一个版本，而该应用程序的依赖加载了另一个版本。因为 Node.js 支持 CommonJS 和 ES模块 的相互混合，所以这种危害可能会发生，并导致意外行为。</p>
<p>如果包主要导出的是一个构造函数，那么两个版本创建的实例的 <code>instanceof</code> 的比较会返回 <code>false</code>。另外，如果导出的是一个对象，为一个版本的对象添加的属性（比如 <code>pkgInstance.foo = 3</code>）在另一个版本上是不存在的。这与 <code>import</code> 和 <code>require</code> 语句分别在全 CommonJS 或全 ESM 模块环境中的作用方式不同，因此会让使用者感到惊讶。这也与大家通过 Babel 或 esm 等工具编译时熟悉的行为不同。</p>
<h4 data-id="heading-18">当编写双包时避免或减少危害（Writing dual packages while avoiding or minimizing hazards）</h4>
<p>首先，当一个包同时包含 CommonJS 和 ESM 模块源，并且这两个源都给 Node.js 使用时就会发生上一节中描述的危险，不论是通过单独的主入口或导出的路径。相反，如果编写一个包，任何版本的 Node.js 都只接收 CommonJS 源，而包中任何单独的 ESM 模块源只用于其他环境，比如只作用于浏览器。这样的包就可以被任何版本的 Node.js 使用，因为 <code>import</code> 可以引用 CommonJS 文件，只是它不会提供使用 ES 模块语法的任何优势。</p>
<p>一个包也可能会在一次大版本更新中从 CommonJS 切换到 ESM 模块语法。这会有一个缺点，即包的最新版本只能在支持 ESM 模块的 Node.js 版本中使用。</p>
<p>每种模式都需要权衡，但有两种方法可以满足以下情况：</p>
<ol>
<li>包可以通过 <code>require</code> 和 <code>import</code> 两种方式使用</li>
<li>包既可以在当前的 Node.js中 使用，也可以在缺乏 ESM 模块 支持的旧版本 Node.js 中使用</li>
<li>包的主入口，例如 <code>'pkg'</code> 既可以通过 <code>require</code> 解析到 CommonJS 文件，也可以通过 <code>import</code> 解析到 ESM 模块文件。(同样，导出的路径也是如此，例如 <code>'pkg/feature'</code> )</li>
<li>包提供了命名导出，例如 <code>import &#123; name &#125; from 'pkg'</code>，而不是 <code>import pkg from 'pkg'; pkg.name</code></li>
<li>包有可能在其他 ESM 模块环境中使用，例如浏览器环境</li>
<li>上一节中描述的双包危害应被避免或最小化了</li>
</ol>
<h5 data-id="heading-19">方法#1：使用 ESM 模块封装器（Approach #1: Use an ES module wrapper）</h5>
<p>用 CommonJS 编写包或将 ESM 模块源码 转译为 CommonJS 的方式编写包，并创建一个带有命名导出的 ESM 模块封装文件。使用“条件导出”，将 ESM 模块封装器用于 <code>import</code>，CommonJS 入口用于 <code>require</code>。</p>
<pre><code class="copyable">// ./node_modules/pkg/package.json
&#123;
  "type": "module",
  "main": "./index.cjs",
  "exports": &#123;
    "import": "./wrapper.mjs",
    "require": "./index.cjs"
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>上面的例子使用了显式扩展名 <code>.mjs</code> 和 <code>.cjs</code>。<code>"type": "module"</code> 将把 <code>.js</code> 文件视为 ES模块，就像 <code>"type": "commonjs"</code> 会把 <code>.js</code> 文件视为 CommonJS 一样。</p>
<pre><code class="copyable">// ./node_modules/pkg/index.cjs
exports.name = 'value';


// ./node_modules/pkg/wrapper.mjs
import cjsModule from './index.cjs';
export const name = cjsModule.name;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>在上面的例子中，<code>import &#123; name &#125; from 'pkg'</code> 中的 <code>name</code> 和 <code>const &#123; name &#125; = require('pkg')</code> 中的 <code>name</code> 是同一个东西。因此 <code>===</code> 在比较两个 <code>name</code> 时返回 <code>true</code>，避免了不同指定符造成的危害。</p>
<p>如果模块不是简单的命名导出列表，而是包含了独特的函数或对象导出，比如 <code>module.exports = function () &#123; … &#125;</code>，或如果希望在封装器中支持 <code>import pkg from 'pkg'</code>，那么封装器将被写成导出默认的同时也导出其他命名值：</p>
<pre><code class="copyable">import cjsModule from './index.cjs';
export const name = cjsModule.name;
export default cjsModule;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这种方法适合于以下任何一种用例：</p>
<ul>
<li>
<p>包目前是用 CommonJS 编写的，作者不希望将其重构为 ESM 模块语法，但希望为 ESM 模块使用者提供命名导出</p>
</li>
<li>
<p>这个包还有其他依赖它的包，终端用户可能会同时安装这个包和一些依赖它的包。例如 <code>utilities</code> 包直接被使用在应用程序中，而 <code>utilities-plus</code> 包则为 <code>utilities</code> 增加了一些功能。因为封装器导出了底层的 CommonJS 文件，所以不管 <code>utilities-plus</code> 是用 CommonJS 还是 ES模块语法写的，这都可以正常使用。</p>
</li>
<li>
<p>包中存储了内部状态，包作者不打算重构包来隔离其状态管理。参见下一节“方法#2”。</p>
</li>
</ul>
<p>这种不要求使用者进行条件导出的另一个方式是添加一个导出，例如：<code>"./module"</code>，指向一个全 ES模块语法版本的包。如果使用者确信 CommonJS 版本不会在应用程序中的任何地方被加载，比如通过依赖关系；或者 CommonJS 版本可以被加载但不影响 ES模块版本（举个例子，因为包是无状态的），那么就可以通过 <code>import 'pkg/module'</code> 来使用。</p>
<pre><code class="copyable">// ./node_modules/pkg/package.json
&#123;
  "type": "module",
  "main": "./index.cjs",
  "exports": &#123;
    ".": "./index.cjs",
    "./module": "./wrapper.mjs"
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h5 data-id="heading-20">方法#2：隔离状态（Approach #2: Isolate state）</h5>
<p><code>package.json</code> 文件可以直接定义 CommonJS 和 ESM 模块的独立入口：</p>
<pre><code class="copyable">// ./node_modules/pkg/package.json
&#123;
  "type": "module",
  "main": "./index.cjs",
  "exports": &#123;
    "import": "./index.mjs",
    "require": "./index.cjs"
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>如果包的 CommonJS 和 ESM 模块版本是等价的，例如因为一个是另一个的转译过来的；并且包的状态管理被仔细隔离（或者包是无状态的），就可以做到这一点。</p>
<p>之所以状态是一个问题，是因为包的 CommonJS 和 ESM 模块版本都可能在应用程序内被使用；例如，用户的应用程序代码可能 <code>import</code> ESM 模块版本，而应用中的一个依赖 <code>require</code> 了 CommonJS 版本。如果发生这种情况，内存中会加载这两个版本，因此会出现两种不同的状态。这很可能会产生难以解决的 bug。</p>
<p>除了编写一个无状态的包（假如 JavaScript 的 <code>Math</code> 是一个包，由于它所有方法都是静态的，那么它就是无状态的），还有一些方法可以隔离状态，使得状态在可能加载的 CommonJS 和 ESM 模块实例之间被共享：</p>
<p>1. 如果可能的话，将所有的状态都包在一个实例化的对象中。例如，JavaScript 的 <code>Date</code> 需要被实例化来包含状态；如果它是一个包，就会被这样使用：</p>
<pre><code class="copyable">import Date from 'date';
const someDate = new Date();
// someDate 包含状态; Date 无状态
<span class="copy-code-btn">复制代码</span></code></pre>
<p><code>new</code> 关键字并不是必须的，包的函数也可以返回一个新的对象，或者修改一个传入的对象，以保持包的外部状态。</p>
<p>2. 将在 CommonJS 和 ESM 模块版本的包中共享的一个或多个 CommonJS 文件，做状态隔离。例如，如果 CommonJS 和 ESM 模块 的入口分别是 <code>index.cjs</code> 和 <code>index.mjs</code>：</p>
<pre><code class="copyable">// ./node_modules/pkg/index.cjs
const state = require('./state.cjs');
module.exports.state = state;


// ./node_modules/pkg/index.mjs
import state from './state.cjs';
export &#123;
  state
&#125;;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>即使 <code>pkg</code> 在应用程序中分别通过 <code>require</code> 和 <code>import</code> 两种方式使用 (例如，在应用程序代码中使用 <code>import</code> 和在其他依赖模块中使用 <code>require</code>)，<code>pkg</code> 的每个引用都将包含相同的状态；并且从任一模块系统中修改该状态都将应用于这两个模块。</p>
<p>任何与包的单例相关的插件都需要分别应用于 CommonJS 和 ESM 模块的单例上。这种方法适用于以下任意一种用例：</p>
<ul>
<li>
<p>包目前是用 ESM 模块语法编写的，而且包作者希望在支持该语法的地方使用该版本</p>
</li>
<li>
<p>包是无状态的，或它的状态可以比较容易得被隔离</p>
</li>
<li>
<p>包不太可能被其他公共包所依赖；或者如果有被依赖的话，这个包是无状态的，或它的状态不需要在依赖者之间或在整个应用程序中被共享。</p>
</li>
</ul>
<p>即使是隔离状态，在包的 CommonJS 和 ESM 版本之间可能仍需要执行额外代码。与前一种方法相同，这种不要求使用者做条件导出的另一个方法是：添加一个导出。例如 <code>"./module"</code>，以指向包的全 ESM 版本：</p>
<pre><code class="copyable">// ./node_modules/pkg/package.json
&#123;
  "type": "module",
  "main": "./index.cjs",
  "exports": &#123;
    ".": "./index.cjs",
    "./module": "./index.mjs"
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-21">五. Node.js <code>package.json</code> 字段定义</h3>
<p>本节描述 Node.js 运行时使用的字段。其他工具（如 npm）使用了额外的字段，这些字段被 Node.js 忽略了，在此不做说明。<code>package.json</code> 中的以下字段是被 Node.js 使用的：</p>
<ul>
<li>
<p>"name" - 当在包内使用命名导入时相关。也被包管理器用作包的名称。</p>
</li>
<li>
<p>"main" - 如果没有指定 <code>exports</code>，或在无法使用 <code>exports</code> 的老 Node.js 版本中，<code>"main"</code> 就是加载包时的默认模块。</p>
</li>
<li>
<p>"type" - 这个字段决定了将 <code>.js</code> 文件作为 CommonJS 还是 ES模块 进行加载。</p>
</li>
<li>
<p>"exports" - 包导出和条件导出。当 <code>"exports"</code> 有值时，会限制可以被加载的子模块为哪些。</p>
</li>
<li>
<p>"imports" - 包的导入，供包内模块本身使用。</p>
</li>
</ul>
<h4 data-id="heading-22">1. "name"</h4>
<p>历史变更：</p>

















<table><thead><tr><th>版本</th><th>变更</th></tr></thead><tbody><tr><td>v13.1.0、v12.16.0</td><td>在 v13.1.0、v12.16.0 版本中新增该属性</td></tr><tr><td>v13.6.0、v12.16.0</td><td>移除 <code>--experimental-resolve-self</code> 选项</td></tr></tbody></table>
<ul>
<li>Type: <code><string></code></li>
</ul>
<pre><code class="copyable">&#123; "name": "package-name" &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><code>"name"</code> 字段定义了包的名称。发布到 <em>npm</em> 上需要一个满足特定要求的名字。</p>
<p><code>"name"</code> 可以搭配 <code>"exports"</code> 字段，来实现自引用。</p>
<h4 data-id="heading-23">2. "main"</h4>
<p>在 v0.4.0 新增该属性</p>
<ul>
<li>Type: <code><string></code></li>
</ul>
<pre><code class="copyable">&#123; "main": "./main.js" &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>当通过 <code>require()</code> 加载包目录时, 就是使用 <code>"main"</code> 字段定义的内容。<code>"main"</code> 的值是一个路径。</p>
<pre><code class="copyable">require('./path/to/directory'); // 这将被解析为 ./path/to/directory/main.js.
<span class="copy-code-btn">复制代码</span></code></pre>
<p>一个包有 <code>"exports"</code> 字段时，当按名称引入包，<code>"exports"</code> 将优先于 <code>"main"</code> 字段。</p>
<h4 data-id="heading-24">3. "type"</h4>
<p>历史变更：</p>

















<table><thead><tr><th>版本</th><th>变更</th></tr></thead><tbody><tr><td>v13.2.0、v12.17.0</td><td>不再使用 <code>--experimental-modules</code> 标志</td></tr><tr><td>v12.0.0</td><td>在 v12.0.0 版本中新增该属性</td></tr></tbody></table>
<ul>
<li>Type: <code><string></code></li>
</ul>
<p><code>"type"</code> 字段定义了 Node.js 对所有以该 <code>package.json</code> 为最近的父文件的 <code>.js</code> 文件所使用的模块格式。</p>
<p>当最近的父 <code>package.json</code> 的顶层字段 <code>"type"</code> 为 <code>"module"</code> 时，以 <code>.js</code> 结尾的文件将作为 ES模块加载。</p>
<p>最近的父 <code>package.json</code> ：被定义为在当前文件夹中搜索时找到的第一个 <code>package.json</code>，或在该文件夹的父包找到的第一个 <code>package.json</code> 以此类推，直到到达 <code>node_modules</code> 文件夹或根目录。</p>
<pre><code class="copyable">// package.json
&#123;
  "type": "module"
&#125;
复制代码
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="copyable"># 与上面的 package.json 在同一文件夹中
node my-app.js # 以 ESM 模块的形式运行，因为 package.json里定义了 "module" type
复制代码
<span class="copy-code-btn">复制代码</span></code></pre>
<p>如果最近的父 <code>package.json</code> 缺少 <code>"type"</code> 字段，或包含 <code>"type": "commonjs"</code>，则 <code>.js</code> 文件将被视为 CommonJS。如果直到根目录也没找到 <code>package.json</code>，<code>.js</code> 文件将被视为 CommonJS。</p>
<p>如果最近的父 <code>package.json</code> 中包含 <code>"type": "module"</code>，那么在 <code>.js</code> 文件被 <code>import</code> 时会被作为ES模块处理：</p>
<pre><code class="copyable">// my-app.js，这是上例的一部分内容
import './startup.js'; // 由于package.json，这会作为ES模块被加载。
复制代码
<span class="copy-code-btn">复制代码</span></code></pre>
<p>无论 <code>"type"</code> 字段的值是什么，<code>.mjs</code> 文件总是被视为 ES模块，而 <code>.cjs</code> 文件总是被视为 CommonJS。</p>
<h4 data-id="heading-25">4. "exports"</h4>
<p>历史变更：</p>





























<table><thead><tr><th>版本</th><th>变更</th></tr></thead><tbody><tr><td>v14.13.0</td><td>新增支持 <code>exports</code> 模式</td></tr><tr><td>v13.7.0、v12.16.0</td><td>实现条件导出的逻辑顺序</td></tr><tr><td>v13.7.0、v12.16.0</td><td>移除 <code>--experimental-conditional-exports</code> 选项</td></tr><tr><td>v13.2.0、v12.16.0</td><td>实现条件导出</td></tr><tr><td>v12.7.0</td><td>在 v12.7.0 版本中新增该属性</td></tr></tbody></table>
<ul>
<li>Type: <code><Object> | <string> | <string[]></code></li>
</ul>
<pre><code class="copyable">&#123; "exports": "./index.js" &#125;
复制代码
<span class="copy-code-btn">复制代码</span></code></pre>
<p><code>"exports"</code> 字段可以定义包的入口，而包则可以通过 <code>node_modules</code> 查找或自引用导入。Node.js 12+ 开始支持 <code>"exports"</code>，作为 <code>"main"</code> 的替代，它既支持定义子路径导出和条件导出，又封闭了内部未导出的模块。</p>
<p>条件导出也可以在 <code>"exports"</code> 中使用，以定义每个环境中不同的包入口，包括这个包是通过 <code>require</code> 还是通过 <code>import</code> 引入。</p>
<p>所有在 <code>"exports"</code> 中定义的路径必须是以 <code>./</code> 开头的相对路径URL。</p>
<h4 data-id="heading-26">5. "imports"</h4>
<p>在 v14.6.0 版本中新增该属性</p>
<ul>
<li>Type: <code><Object></code></li>
</ul>
<pre><code class="copyable">// package.json &#123; "imports": &#123; "#dep": &#123; "node": "dep-node-native", "default": "./dep-polyfill.js" &#125; &#125;, "dependencies": &#123; "dep-node-native": "^1.0.0" &#125; &#125;
复制代码
<span class="copy-code-btn">复制代码</span></code></pre>
<p><code>imports</code> 字段中的入口必须是以 <code>#</code> 开头的字符串。</p>
<p>导入映射允许映射外部包。这个字段定义了当前包的子路径导入。</p>
<h3 data-id="heading-27">六. 附录：webpack 功能校验</h3>
<p>以上 Node.js 支持的功能，用 webpack 也检测了一下：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/98d4e0b7eaf74db2b64b43628c4eaaae~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>下图为使用 webpack 在浏览器端的验证：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/069e9f3d5fb84a20aae5c4cf0c6706d4~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>上述<strong>测试用例的 repo</strong> 请访问：<a href="https://github.com/zEmily/webpack-demo" target="_blank" rel="nofollow noopener noreferrer">github.com/zEmily/webp…</a></p>
<h3 data-id="heading-28">七. 总结</h3>
<p>查看了几个常用的库，发现它们并没有在使用 <code>exports</code> 新特性。或许包作者目前不想做破坏性的更新迭代，但未来预计新特性都会慢慢更新上去。</p>
<p>虽然外部的包没有在使用 <code>exports</code>，但是我们可以在内部先使用起来。比如书写通用 lib 包时，使用 <code>exports</code> 仅暴露预期内的接口，而不是将所有包内容都让外部随意访问；如果这个包仅在 node 环境下使用的话，可以使用上面提到的 <strong>“条件导出”</strong> 来做限制，避免出现不必要的 bug。</p></div>  
</div>
            