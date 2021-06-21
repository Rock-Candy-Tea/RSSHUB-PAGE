
---
title: '在 esbuild 中实现 babel 超人气爆款插件'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/1a95c06d7c8040e395c6309a7f9fa2ea~tplv-k3u1fbpfcp-zoom-1.image'
author: 掘金
comments: false
date: Mon, 21 Jun 2021 00:00:49 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/1a95c06d7c8040e395c6309a7f9fa2ea~tplv-k3u1fbpfcp-zoom-1.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h1 data-id="heading-0">前言</h1>
<p><a href="https://esbuild.github.io/" target="_blank" rel="nofollow noopener noreferrer">esbuild</a> 是近些天来非常火的一个全新的工具，年前霸屏掘金前端板块，被称作第三代构建方案，它最与众不同之处就是它独特的使用 go 语言构建。得益于此，它的打包速度非常的惊人。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/1a95c06d7c8040e395c6309a7f9fa2ea~tplv-k3u1fbpfcp-zoom-1.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>构建十次 threejs 副本竟然只需要 0.37s，它被作为 vite 的打包工具的构建底层方案从而一战成名。</p>
<p>令人遗憾的是 esbuild 本身是不支持 babel 插件，所以本次文章，将带大家编写一个插件，该插件对标 babel-plugin-import，将赋予 esbuild 一个 babel 中非常通用的插件功能——动态引入。</p>
<h1 data-id="heading-1">why</h1>
<p>动态 import 的想法其实非常简单，即通过改变 ast 的方式将代码强行改为仅引入单文件，即：</p>
<pre><code class="hljs language-jsx copyable" lang="jsx"><span class="hljs-keyword">import</span> &#123; Button, Select &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'antd'</span>
<span class="hljs-comment">// ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓</span>
<span class="hljs-keyword">import</span> Button <span class="hljs-keyword">from</span> <span class="hljs-string">'antd/lib/button'</span>
<span class="hljs-keyword">import</span> Select <span class="hljs-keyword">from</span> <span class="hljs-string">'antd/lib/select'</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>为什么要这样做？</p>
<p>我们知道，引入模块时，如果引入形如 <code>import &#123; Button &#125; from 'antd'</code> 是会将包全部模块都引进来的。</p>
<p>我们在看一个库时，首先要读这个库的 <code>pacakge.json</code> 文件：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/50f3ce09f4634bcc907a955109ec7cb0~tplv-k3u1fbpfcp-zoom-1.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>其中的 <code>main</code> 和 <code>module</code> 字段标记着用户在使用 import 语句是具体引入的文件是哪个，<code>main</code> 字段代表 commonjs 引入形式默认查找的文件，<code>module</code> 字段为 es 形式默认查找的文件。这是 commonjs 时期遗留下的规定，因此你在使用不带 <code>module</code> 字段的库时，形如 <code>import &#123; Button &#125; from 'antd'</code> 总是会引入 <code>main</code> 所标记的文件，丢失了 esm 的 tree-shaking 特性。</p>
<p>在本例中我们需要查看 <code>main</code> 中指向的文件，即 <code>lib/index.js</code>。</p>
<p>这是一个 commonjs 形式的文件，你会发现，所有的组件都通过 <code>require</code> 的形式引入，我们知道 commonjs 的 <code>require</code> 是动态依赖的，这意味着只要引入了 <code>import &#123; Button &#125; from 'antd'</code>（即便你只使用 Button 组件），就会将全量组件引入，导致打包结果增大。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/fc681109ff784e5a9e40c27d41f3f1d1~tplv-k3u1fbpfcp-zoom-1.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>尝试仅引入 antd 的 Button 组件，将 antd 的 package.json 中的 <code>module</code> 字段删除后打包：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/6bec10fac5f9462697df5f5f39ab8a80~tplv-k3u1fbpfcp-zoom-1.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>然后再用动态引入的方式：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/fa4cbe91b02d40e88a0f2f0650bfda23~tplv-k3u1fbpfcp-zoom-1.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>OMG！竟足足少了 80%！</p>
<p>我们通过 import 指定路径的文件，绕过了 <code>lib/index.js</code> 文件，自然也就不会将所有组件打包。社区中一般将此行为称作「动态引入」(dynamic import) 或者「按需引入」(import on demand)。</p>
<h1 data-id="heading-2">how</h1>
<p>在最流行的 webpack 中我们可以利用<a href="https://www.npmjs.com/package/babel-plugin-import" target="_blank" rel="nofollow noopener noreferrer"> babel-plugin-import </a>插件来解决这一问题。该插件由 antd 团队开发，周均下载超 30 万次，可谓是前端界的超级网红，为的正是解决这一情形：</p>
<pre><code class="hljs language-jsx copyable" lang="jsx"><span class="hljs-comment">// .babelrc</span>
<span class="hljs-string">"plugins"</span>: [
  [<span class="hljs-string">"import"</span>, &#123; <span class="hljs-string">"libraryName"</span>: <span class="hljs-string">"antd"</span> &#125;]
]
<span class="copy-code-btn">复制代码</span></code></pre>
<p>如此设置，babel 仅针对 antd 库做按需引入，且引入形式默认是 <code><libraryName>/lib/<componentName></code>。但其他的类库路径不一定如此，比如 lodash，lodash 的函数路径就是 <code>lodash/<functionName></code> 的，因此它允许你配置 <code>libraryDirectory</code> 更改引入包路径：</p>
<pre><code class="hljs language-jsx copyable" lang="jsx"><span class="hljs-comment">// .babelrc</span>
<span class="hljs-string">"plugins"</span>: [
  [<span class="hljs-string">"import"</span>, &#123; <span class="hljs-string">"libraryName"</span>: <span class="hljs-string">"lodash"</span>, <span class="hljs-attr">libraryDirectory</span>: <span class="hljs-string">''</span> &#125;]
]
<span class="copy-code-btn">复制代码</span></code></pre>
<p>看来 babel-plugin-import 早有准备。继续翻看文档我们会看到如下配置项，能够覆盖所有的引入情形：</p>





































<table><thead><tr><th><strong>配置项</strong></th><th><strong>意义</strong></th></tr></thead><tbody><tr><td><code>libraryName</code></td><td>包名</td></tr><tr><td><code>libraryDirectory</code></td><td>模块引入路径</td></tr><tr><td><code>styleLibraryDirectory</code></td><td>样式引入路径</td></tr><tr><td><code>camel2DashComponentName</code></td><td>是否将 camelCase 转为 kebabCase，默认为 true</td></tr><tr><td><code>style</code></td><td>是否默认引入样式，支持函数形式</td></tr><tr><td><code>customName</code></td><td>改变模块引用路径的函数</td></tr><tr><td><code>customStyleName</code></td><td>改变样式引入路径的函数</td></tr></tbody></table>
<p>那么，让我们开始 esbuild 插件的开发，首先我们要了解一下 esbuild 的插件机制。</p>
<h1 data-id="heading-3">esbuild 插件机制</h1>
<p>esbuild 插件的机制相比 webpack 可谓是极简，对程序仅有 onStart、onEnd 两个环节，对文件仅影响 onResolve、onLoad 两个环节。</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/44783404eb39437a803d09d255b4ea99~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>esbuild 的规范要求插件必须是有 name、setup 的对象，其中 setup 是一个接收 build 流程的函数，你可以在 build 上注册周期钩子，在 build 流程开始时会统一挂载，并在相应环节触发。</p>
<pre><code class="hljs language-jsx copyable" lang="jsx"><span class="hljs-keyword">const</span> plugin = &#123;
<span class="hljs-attr">name</span>: <span class="hljs-string">'myPlugin'</span>,
  <span class="hljs-attr">setup</span>: <span class="hljs-function"><span class="hljs-params">build</span> =></span> &#123;
  build.onLoad(&#123;&#125;, <span class="hljs-function"><span class="hljs-params">args</span> =></span> &#123;
      <span class="hljs-keyword">const</span> contents = fs.readFileSync(args.path, <span class="hljs-string">'utf-8'</span>)
      <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'content: '</span>, contents)
      <span class="hljs-keyword">return</span> &#123;
        <span class="hljs-attr">cotnents</span>: contents + <span class="hljs-string">'\n'</span>,
      &#125;
    &#125;)
&#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>具体的周期钩子的接受值和返回值可以<a href="https://esbuild.github.io/plugins/#using-plugins" target="_blank" rel="nofollow noopener noreferrer">参阅 esbuild 官方 using plugins 一栏</a>。</p>
<h1 data-id="heading-4">开始开发</h1>
<p>我们可以借助最近非常火的一个 AST 分析框架 <a href="https://gogocode.io/" target="_blank" rel="nofollow noopener noreferrer">gogocode</a> 的能力，快速将我们的想法变现。</p>
<p>我们要干的事情事实上就两种情况：</p>
<p>情况一：<code>ImportDefaultSpecifier</code> 类型</p>
<pre><code class="hljs language-jsx copyable" lang="jsx"><span class="hljs-keyword">import</span> Antd <span class="hljs-keyword">from</span> <span class="hljs-string">'antd'</span>

<span class="hljs-keyword">const</span> Button = Antd.Button
<span class="hljs-keyword">const</span> &#123; Select &#125; = Antd
<span class="hljs-comment">// ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓</span>
<span class="hljs-keyword">import</span> Button <span class="hljs-keyword">from</span> <span class="hljs-string">'antd/lib/button'</span>
<span class="hljs-keyword">import</span> Select <span class="hljs-keyword">from</span> <span class="hljs-string">'antd/lib/select'</span>

ReactDOM.render(
  <span class="xml"><span class="hljs-tag"><></span>
    <span class="hljs-tag"><<span class="hljs-name">Button</span> /></span>
    <span class="hljs-tag"><<span class="hljs-name">Select</span> /></span>
    <span class="hljs-tag"><<span class="hljs-name">Antd.Table</span> /></span>
<span class="hljs-tag"></></span></span>,
  <span class="hljs-built_in">document</span>.querySelector(<span class="hljs-string">'#root'</span>)
)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>情况二：<code>ImportSepecifier</code> 类型</p>
<pre><code class="hljs language-jsx copyable" lang="jsx"><span class="hljs-keyword">import</span> &#123; Button, Select &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'antd'</span>
<span class="hljs-comment">// ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓</span>
<span class="hljs-keyword">import</span> Button <span class="hljs-keyword">from</span> <span class="hljs-string">'antd/lib/button'</span>
<span class="hljs-keyword">import</span> Select <span class="hljs-keyword">from</span> <span class="hljs-string">'antd/lib/select'</span>

ReactDOM.render(
  <span class="xml"><span class="hljs-tag"><></span>
    <span class="hljs-tag"><<span class="hljs-name">Button</span> /></span>
    <span class="hljs-tag"><<span class="hljs-name">Select</span> /></span>
  <span class="hljs-tag"></></span></span>,
  <span class="hljs-built_in">document</span>.querySelector(<span class="hljs-string">'#root'</span>)
)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>情况二处理起来相对比较简单，我们分析它所有的 <code>ImportDeclaration</code> 的 <code>ImportSepecifier</code>，只要分析到了，就向原 ast 下方 push 几个 <code>DefaultImportSepecifier</code> ，并将原 <code>ImportDeclaration</code> 删除。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/ad1c13f545f4410b8a1b4aed0970a1dd~tplv-k3u1fbpfcp-zoom-1.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<blockquote>
<p>……：省略号用以省略与本需求无关的 ast 声明</p>
</blockquote>
<p>需要注意的是这个声明有一特殊情况：<code>import &#123; Button as MyButton &#125; from 'antd'</code>，我们需要记录它的「引入名称」（<code>importSepecifier.imported</code>）和「开发者想要使用的新名称」（<code>importSepecifier.local</code>），在替换时将其赋值即可。</p>
<p>​</p>
<p>对于情况一，我们又可以分成三种情况：</p>
<ul>
<li>直接使用：<code><Antd.Select /></code></li>
<li>间接引用：<code>const Button = Antd.Button</code></li>
<li>间接的列表引用：<code>const &#123; Button: MyButton, Select &#125; = Antd</code></li>
</ul>
<p>对于后两者，我们得在脑内将 <code>VariableDeclaration</code> 转变为 <code>ImportDeclaration</code>。</p>
<p>由于 <a href="https://gogocode.io/zh" target="_blank" rel="nofollow noopener noreferrer">gogocode</a> 使用的是直接匹配的模式，所以可以选择性地跳过无关环节，非常方便。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/bc6cd0e6165d493e9e2699019229d5b1~tplv-k3u1fbpfcp-zoom-1.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h1 data-id="heading-5">上代码！</h1>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/2862e813447f4063bcae544811b6de0e~tplv-k3u1fbpfcp-zoom-1.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>回过头来看看 <code>getUsedComponents</code> 干了什么：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/64c3352981b246b28d06d226bb0fdb6c~tplv-k3u1fbpfcp-zoom-1.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>就是这样喵！</p>
<h1 data-id="heading-6">测试用例</h1>
<p>对于测试用例，<code>babel-plugin-import</code> 已经帮我们写好了，我们直接使用即可。</p>
<p>esbuild 处理文件<a href="https://juejin.cn/post/6976153834758340621">使用何种 loader</a> 与 webpack 不同，它是直接根据后缀名来判断的，所以我们要将所有用到 js 的文件后缀名改成 jsx。例如：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/4e3b32852c774952a7161a326ed050b9~tplv-k3u1fbpfcp-zoom-1.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>然后，让我们写好测试逻辑：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/3ec2299cde4c4d4cb7d9b30ad2d7c0be~tplv-k3u1fbpfcp-zoom-1.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>跑下试试：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/02890abc3dd845e0b0a6f5d22cea03fa~tplv-k3u1fbpfcp-zoom-1.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>芜湖！比预计的还要顺利，还就那个全部通过！</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/93f5c6aad239461f953acc58759f1cf5~tplv-k3u1fbpfcp-zoom-1.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>这个库已经发布到了 npm，名字叫 <a href="https://www.npmjs.com/package/esbuild-dynamic-import-plugin" target="_blank" rel="nofollow noopener noreferrer">esbuild-dynamic-import-plugin</a>，并且已经加入到<a href="https://github.com/egoist/awesome-esbuild" target="_blank" rel="nofollow noopener noreferrer"> awesome esbuild </a>全家桶。在 awesome esbuild 中还有大量插件没有被覆盖，欢迎大家使用 <a href="https://gogocode.io/zh" target="_blank" rel="nofollow noopener noreferrer">gogocode</a> 进行开发！</p>
<h1 data-id="heading-7">写在后面</h1>
<p>我们在《webpack、babel、vite、rollup 中完美融入 gogocode》的那次文章中，对 webpack 的插件系统做了一个小剖析，它的确更可控，但是实在太很重了：webpack 竟然有 28 个生命周期钩子，而 esbuild 只有 4 个；webpack 的 tapable 的规范容易让开发者陷入无所适从的境地，esbuild 就相对来说清爽得很。</p>
<p>其次 <a href="https://gogocode.io/zh" target="_blank" rel="nofollow noopener noreferrer">gogocode</a> 匹配和替换 ast 的方案非常的高效，能够节省大量的代码，比如刚刚我们要匹配 <code>ImportDeclaration</code> 如果使用 babel 的 visitor 模式，那将至少编写十倍不止的代码，而 <a href="https://gogocode.io/zh" target="_blank" rel="nofollow noopener noreferrer">gogocode</a> 只有一行简单的字符串就解决了。让开发着把注意力放在对代码转换的思路上，不仅节省时间，还节省了程序猿的掉的头发。真正做到了以「猿」(¿) 为本，赞一个！</p>
<blockquote>
<p>为什么会变成这样呢~！第一次写 esbuild 构建框架的插件；第一次用 <a href="https://gogocode.io/zh" target="_blank" rel="nofollow noopener noreferrer">gogocode</a> 搞出如此复杂的插件。这两件愉快的事情交织在了一起。本应该是双倍的快乐，但为什么会这样呢~！（指变成了四倍快乐）
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/a60c166467734a82be3ab71ee1d168d6~tplv-k3u1fbpfcp-zoom-1.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
</blockquote>
<h2 data-id="heading-8">GoGoCode 相关链接</h2>
<p>GoGoCode的Github仓库（新项目求star ^_^）
<a href="https://github.com/thx/gogocode" target="_blank" rel="nofollow noopener noreferrer">github.com/thx/gogocod…</a></p>
<p>GoGoCode的官网
<a href="https://gogocode.io/" target="_blank" rel="nofollow noopener noreferrer">gogocode.io/</a></p>
<p>可以来 playground 快速体验一下
<a href="https://play.gogocode.io/" target="_blank" rel="nofollow noopener noreferrer">play.gogocode.io/</a></p>
<p><a href="https://juejin.cn/post/6938601548192677918" target="_blank">阿里妈妈出的新工具，给批量修改项目代码减轻了痛苦</a><br><a href="https://juejin.cn/post/6943114726175932452" target="_blank">「GoGoCode 实战」一口气学会 30 个 AST 代码替换小诀窍</a><br><a href="https://juejin.cn/post/6948635226453049374" target="_blank">0成本上手AST，用GoGoCode解决Vue2迁移Vue3难题</a><br><a href="https://juejin.cn/post/6953160272496295943" target="_blank">GoGoCode协助清理代码中的「垃圾」</a></p>
<p>本文作者：冰块</p></div>  
</div>
            