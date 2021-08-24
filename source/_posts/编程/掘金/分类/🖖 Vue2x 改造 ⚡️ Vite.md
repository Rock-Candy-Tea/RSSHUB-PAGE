
---
title: '🖖 Vue2.x 改造 ⚡️ Vite'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=1372'
author: 掘金
comments: false
date: Sun, 22 Aug 2021 19:47:30 GMT
thumbnail: 'https://picsum.photos/400/300?random=1372'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h4 data-id="heading-0">前言</h4>
<ul>
<li><code>vite</code> 已经发布大半年了势头很猛，github 活跃度非常高</li>
<li>从 <code>2.x</code> 开始加入了预编译，能够很好的兼容 <code>CommonJs</code> 模式，预编译后有着相当快的冷启动速度</li>
<li><strong>当系统维护越来越大启动速度就会越慢</strong> <code>@vue/cli</code> 创建的项目(vue2.x)使用的 <code>webpack@4.x</code> 版本，这个问题愈发严重
是时候集成到“年迈” <code>vue2</code> 的老项目中了</li>
</ul>
<blockquote>
<p>📢 注意: 本次改造只推荐在开发模式下运行 vite 生产环境依然用之前的方式；毕竟 webpack 在打包方面更加成熟</p>
</blockquote>
<h4 data-id="heading-1">项目背景</h4>
<ul>
<li>本次改造的工程是公司一个很重要，迭代又很频繁的系统；现在已经有 100+ 张页面了</li>
<li>工程模板由 <code>@vue/cli</code> 创建的 <code>vue2.x</code> 版本，内部使用 <code>webpack4.x</code> 构建</li>
<li>随着项目越来越大(一年50增加张页面左右)，对项目冷启动速度的追求就越显得迫切</li>
</ul>
<h4 data-id="heading-2">技术分析</h4>
<ul>
<li>
<p>虽然 <code>vite</code> 发展很快，npm 上面关于 vite 的插件也跟进的很快；但是总有一些鞭长莫及的情况出现在我们的老项目中</p>
</li>
<li>
<p>这里我主要以我实际改造中碰到的问题做下技术总结，如果你在使用过程中还有碰到其他的问题，本文的解决问题思路也有一定的参考价值</p>
</li>
<li>
<p>以下是我碰到的改造问题点</p>
<ol>
<li>需要将 <code>public/index.html</code> 生成软链接到根目录 ---- <code>vite</code> 启动入口</li>
<li>转换 <code>@import '~normalize.css/normalize.css</code> 中的 <code>~</code> 别名 ---- <code>vite</code> 报错</li>
<li>转换 <code>import('@/pages/xxxx')</code> ---- <code>vite</code> 警告、报错</li>
<li>转换 <code>require</code> 为 <code>import</code> 形式 ---- <code>vite</code> 报错</li>
</ol>
</li>
</ul>
<h4 data-id="heading-3">vite-plugins</h4>
<ul>
<li>我们对于 vite 工程的改造都是基于插件的，可以理解为就是写了好多插件解决对应问题</li>
<li>你可能需要先了解下如何写一个 <a href="https://link.juejin.cn/?target=https%3A%2F%2Fvitejs.dev%2Fplugins%2F" target="_blank" rel="nofollow noopener noreferrer" title="https://vitejs.dev/plugins/" ref="nofollow noopener noreferrer">vite 插件</a></li>
<li>这次几个关于<strong>转换</strong>的插件都是用的插件中的 <code>transform</code> 钩子，相对比较简单容易理解</li>
</ul>
<h4 data-id="heading-4">public/index.html -> index.html</h4>
<ul>
<li>
<p><code>vite</code> 专注于前端开发，所以入口文件为 html；<code>webpack</code> 则是以 js 为入口</p>
</li>
<li>
<p>由于打包期间还是要用 <code>webpack</code>，而我们只是开发期用 <code>vite</code>，
考虑到两个点兼容我们将 public/index.html 生成一个“软链接”放在项目根目录下
这样能同时兼顾 vite、webpack 两者
当然有人可能会问为啥不使用 vite 提供的 <code>root</code> 配置方式；其实那样可能会带来更多的问题，比如 src="xxx" 的指向就会变得很麻烦
使用软链接的而不是 copy 文件的形式，就是为了修改 public/index.html 能够同时影响 index.html 软链接</p>
</li>
<li>
<p>symlink-index-html.ts</p>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-keyword">import</span> fs <span class="hljs-keyword">from</span> <span class="hljs-string">'fs'</span>
<span class="hljs-keyword">import</span> path <span class="hljs-keyword">from</span> <span class="hljs-string">'path'</span>
<span class="hljs-keyword">import</span> &#123; Plugin &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'vite'</span>
<span class="hljs-keyword">import</span> template <span class="hljs-keyword">from</span> <span class="hljs-string">'lodash.template'</span>

<span class="hljs-keyword">export</span> <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">symlinkIndexHtml</span>(<span class="hljs-params">options: &#123;
  <span class="hljs-regexp">//</span> index.html 读取路径，一般为 <span class="hljs-keyword">public</span>/index.html
  template: <span class="hljs-built_in">string</span>
  <span class="hljs-regexp">//</span> 兼容 html-webpack-plugin 中的编译注入
  templateDate?: Record<<span class="hljs-built_in">string</span>, unknown>
  <span class="hljs-regexp">//</span> index.html 中的 js 文件入口
  entry?: <span class="hljs-built_in">string</span>
&#125;</span>): <span class="hljs-title">Plugin</span> </span>&#123;
  <span class="hljs-keyword">const</span> rootIndexHtml = path.join(process.cwd(), <span class="hljs-string">'index.html'</span>)

  <span class="hljs-keyword">try</span> &#123;
    fs.unlinkSync(rootIndexHtml)
  &#125; <span class="hljs-keyword">catch</span> (error) &#123; &#125;

  <span class="hljs-keyword">if</span> (!fs.existsSync(rootIndexHtml)) &#123;
    <span class="hljs-comment">// 生成 index.html 软链接</span>
    fs.symlinkSync(options.template, rootIndexHtml)
  &#125;

  <span class="hljs-keyword">return</span> &#123;
    <span class="hljs-attr">name</span>: <span class="hljs-string">'vite-plugin-vue2-compatible:symlinkIndexHtml'</span>,
    <span class="hljs-function"><span class="hljs-title">transformIndexHtml</span>(<span class="hljs-params">html</span>)</span> &#123;
      <span class="hljs-keyword">let</span> indexHtml = html
      <span class="hljs-keyword">const</span> entry = options.entry || <span class="hljs-string">'/src/main.js'</span>

      <span class="hljs-keyword">try</span> &#123;
        <span class="hljs-keyword">const</span> compiled = template(indexHtml, &#123; <span class="hljs-attr">interpolate</span>: <span class="hljs-regexp">/<%=([\s\S]+?)%>/g</span> &#125;)
        <span class="hljs-comment">// 注入 html-webpack-plugin 变量</span>
        indexHtml = compiled(options.templateDate)
        <span class="hljs-comment">// 指定 src 入口</span>
        indexHtml = indexHtml.split(<span class="hljs-string">'\n'</span>)
          .map(<span class="hljs-function"><span class="hljs-params">line</span> =></span> line.includes(<span class="hljs-string">'</body>'</span>)
            ? <span class="hljs-string">`    <script type="module" src="<span class="hljs-subst">$&#123;entry&#125;</span>"></script>
      <span class="hljs-subst">$&#123;line&#125;</span>`</span>
            : line
          )
          .join(<span class="hljs-string">'\n'</span>)
      &#125; <span class="hljs-keyword">catch</span> (error) &#123;
        indexHtml = <span class="hljs-string">`<h2><span class="hljs-subst">$&#123;error&#125;</span></h2>`</span>
      &#125;

      <span class="hljs-keyword">return</span> indexHtml
    &#125;,
  &#125;
&#125;

<span class="copy-code-btn">复制代码</span></code></pre>
</li>
</ul>
<h4 data-id="heading-5">转换 @import ~ 别名</h4>
<ul>
<li><code>gonzales-pe</code> css <code>AST</code> 工具</li>
<li><code>node-source-walk</code> css <code>AST</code> 遍历工具</li>
<li>style-import.ts
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-keyword">import</span> path <span class="hljs-keyword">from</span> <span class="hljs-string">'path'</span>
<span class="hljs-keyword">import</span> &#123; Plugin &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'vite'</span>
<span class="hljs-keyword">import</span> &#123; convertVueFile &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'./utils'</span>
<span class="hljs-keyword">import</span> Walker <span class="hljs-keyword">from</span> <span class="hljs-string">'node-source-walk'</span>
<span class="hljs-keyword">import</span> gonzales <span class="hljs-keyword">from</span> <span class="hljs-string">'gonzales-pe'</span>

<span class="hljs-keyword">export</span> <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">styleImport</span>(<span class="hljs-params">options?: Record<<span class="hljs-built_in">string</span>, unknown></span>): <span class="hljs-title">Plugin</span> </span>&#123;
  <span class="hljs-keyword">const</span> walker = <span class="hljs-keyword">new</span> Walker <span class="hljs-keyword">as</span> <span class="hljs-built_in">any</span>
  <span class="hljs-comment">// 判断是否为 @import 语句</span>
  <span class="hljs-keyword">const</span> isImportStatement = <span class="hljs-function">(<span class="hljs-params">node</span>) =></span> &#123;
    <span class="hljs-keyword">if</span> (node.type !== <span class="hljs-string">'atrule'</span>) &#123; <span class="hljs-keyword">return</span> <span class="hljs-literal">false</span> &#125;
    <span class="hljs-keyword">if</span> (!node.content.length || node.content[<span class="hljs-number">0</span>].type !== <span class="hljs-string">'atkeyword'</span>) &#123; <span class="hljs-keyword">return</span> <span class="hljs-literal">false</span> &#125;
    <span class="hljs-keyword">const</span> atKeyword = node.content[<span class="hljs-number">0</span>]
    <span class="hljs-keyword">if</span> (!atKeyword.content.length) &#123; <span class="hljs-keyword">return</span> <span class="hljs-literal">false</span> &#125;
    <span class="hljs-keyword">const</span> importKeyword = atKeyword.content[<span class="hljs-number">0</span>]
    <span class="hljs-keyword">if</span> (importKeyword.type !== <span class="hljs-string">'ident'</span> || importKeyword.content !== <span class="hljs-string">'import'</span>) &#123; <span class="hljs-keyword">return</span> <span class="hljs-literal">false</span> &#125;
    <span class="hljs-keyword">return</span> <span class="hljs-literal">true</span>
  &#125;
  <span class="hljs-comment">// 去掉字符串两边的引号部分</span>
  <span class="hljs-keyword">const</span> extractDependencies = <span class="hljs-function">(<span class="hljs-params">importStatementNode</span>) =></span> &#123;
    <span class="hljs-keyword">return</span> importStatementNode.content
      .filter(<span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params">innerNode</span>) </span>&#123;
        <span class="hljs-keyword">return</span> innerNode.type === <span class="hljs-string">'string'</span> || innerNode.type === <span class="hljs-string">'ident'</span>
      &#125;)
      .map(<span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params">identifierNode</span>) </span>&#123;
        <span class="hljs-keyword">return</span> identifierNode.content.replace(<span class="hljs-regexp">/["']/g</span>, <span class="hljs-string">''</span>)
      &#125;)
  &#125;

  <span class="hljs-keyword">return</span> &#123;
    <span class="hljs-attr">enforce</span>: <span class="hljs-string">'pre'</span>,
    <span class="hljs-attr">name</span>: <span class="hljs-string">'vite-plugin-vue2-compatible:styleImport'</span>,
    <span class="hljs-function"><span class="hljs-title">transform</span>(<span class="hljs-params">code, id</span>)</span> &#123;
      <span class="hljs-keyword">if</span> (!id.endsWith(<span class="hljs-string">'.vue'</span>)) <span class="hljs-keyword">return</span>
      <span class="hljs-keyword">let</span> _code = code

      <span class="hljs-keyword">try</span> &#123;
        <span class="hljs-comment">// 提出所有的 @import 语句</span>
        <span class="hljs-keyword">const</span> imports = convertVueFile(code).styles.reduce(<span class="hljs-function">(<span class="hljs-params">dependencies, cur</span>) =></span> &#123;
          <span class="hljs-keyword">const</span> ast = (gonzales <span class="hljs-keyword">as</span> <span class="hljs-built_in">any</span>).parse(cur.content, &#123; <span class="hljs-attr">syntax</span>: cur.lang &#125;)
          <span class="hljs-keyword">let</span> deps = dependencies
          walker.walk(ast, <span class="hljs-function">(<span class="hljs-params">node: <span class="hljs-built_in">any</span></span>) =></span> &#123;
            <span class="hljs-keyword">if</span> (!isImportStatement(node)) <span class="hljs-keyword">return</span>
            deps = deps.concat(extractDependencies(node))
          &#125;)
          <span class="hljs-keyword">return</span> deps
        &#125;, [])

        <span class="hljs-comment">// 转换 @import 语句中的 ~ 别名</span>
        <span class="hljs-keyword">for</span> (<span class="hljs-keyword">const</span> importPath <span class="hljs-keyword">of</span> imports) &#123;
          <span class="hljs-keyword">if</span> (importPath.startsWith(<span class="hljs-string">'~'</span>)) &#123;
            <span class="hljs-keyword">const</span> node_modules = path.join(process.cwd(), <span class="hljs-string">'node_modules'</span>)
            <span class="hljs-keyword">const</span> targetPath = path.join(
              path.relative(path.parse(id).dir, node_modules),
              importPath.slice(<span class="hljs-number">1</span>),
            )
            <span class="hljs-comment">// Replace alias '~' to 'node_modules'</span>
            _code = _code.replace(importPath, targetPath)
          &#125;
        &#125;
        <span class="hljs-keyword">return</span> _code
      &#125; <span class="hljs-keyword">catch</span> (error) &#123;
        <span class="hljs-keyword">throw</span> error
      &#125;
    &#125;,
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
</ul>
<h4 data-id="heading-6">转换 <code>import('@/pages/xxxx')</code></h4>
<ul>
<li>
<p>这个还是挺麻烦的，需要考虑两个点</p>
<ol>
<li><code>@</code> 这种别名替换 ---- vite 报错</li>
<li><code>xxxx</code> 动态路径分析 ---- vite 警告</li>
</ol>
</li>
<li>
<p>实现原理</p>
<ol>
<li><code>impot('@/pages/' + path)</code> 本质上是将 pages 下的所有文件列举处理，然后生成一个 <code>switch</code> 提供匹配</li>
</ol>
<p>如有目录结构如下:</p>
<pre><code class="hljs language-tree copyable" lang="tree">src
  pages
    foo.vue
    bar/index.vue
<span class="copy-code-btn">复制代码</span></code></pre>
<p>将会生成:</p>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">__variableDynamicImportRuntime__</span>(<span class="hljs-params">path</span>) </span>&#123;
  <span class="hljs-keyword">switch</span> (path) &#123;
    <span class="hljs-keyword">case</span> <span class="hljs-string">'../pages/foo'</span>: <span class="hljs-keyword">return</span> <span class="hljs-keyword">import</span>(<span class="hljs-string">'../pages/foo.vue'</span>);
    <span class="hljs-keyword">case</span> <span class="hljs-string">'../pages/foo.vue'</span>: <span class="hljs-keyword">return</span> <span class="hljs-keyword">import</span>(<span class="hljs-string">'../pages/foo.vue'</span>);
      <span class="hljs-keyword">break</span>;
    <span class="hljs-keyword">case</span> <span class="hljs-string">'../pages/bar'</span>: <span class="hljs-keyword">return</span> <span class="hljs-keyword">import</span>(<span class="hljs-string">'../pages/bar/index.vue'</span>);
    <span class="hljs-keyword">case</span> <span class="hljs-string">'../pages/bar/index'</span>: <span class="hljs-keyword">return</span> <span class="hljs-keyword">import</span>(<span class="hljs-string">'../pages/bar/index.vue'</span>);
    <span class="hljs-keyword">case</span> <span class="hljs-string">'../pages/bar/index.vue'</span>: <span class="hljs-keyword">return</span> <span class="hljs-keyword">import</span>(<span class="hljs-string">'../pages/bar/index.vue'</span>);
      <span class="hljs-keyword">break</span>;
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<ol start="2">
<li>参考链接</li>
</ol>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Frollup%2Fplugins%2Ftree%2Fmaster%2Fpackages%2Fdynamic-import-vars" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/rollup/plugins/tree/master/packages/dynamic-import-vars" ref="nofollow noopener noreferrer">dynamic-import-vars</a></p>
</li>
<li>
<p>dynamic-import 代码有点长，<a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fcaoxiemeihao%2Fvite-plugin-vue2-compatible%2Ftree%2Fmain%2Fsrc%2Fdynamic-import" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/caoxiemeihao/vite-plugin-vue2-compatible/tree/main/src/dynamic-import" ref="nofollow noopener noreferrer">完整代码 github 链接</a></p>
</li>
</ul>
<h4 data-id="heading-7"><code>require</code> to <code>import</code></h4>
<ul>
<li>
<p>这个问题就是 CommonJs to ESModule 方案，npm 上面找了好几个包都没实现我的功能(要么不转化，要么注入环境变量报错)；
索性自己写了一个简化版的，也算给自己拓宽下技术线路(不能吃现成的，得会自己做不是)</p>
</li>
<li>
<p>技术选型</p>
<ol>
<li><code>acorn</code> js 抽象语法树(AST)工具</li>
<li><code>acorn-walk</code> 语法树 遍历工具</li>
</ol>
</li>
<li>
<p>实现原理</p>
<ol>
<li>先用 acorn 将代码转化为 <code>AST</code></li>
<li>在使用 acorn-walk 遍历 <code>AST</code> 分析出 require 加载得文件，然后转换成 import 格式即可</li>
</ol>
</li>
<li>
<p><code>cjs-esm</code> 代码有点长，<a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fcaoxiemeihao%2Fcjs-esm" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/caoxiemeihao/cjs-esm" ref="nofollow noopener noreferrer">完整代码 github 链接</a></p>
</li>
<li>
<p>基于 cjs-esm 写一个 <a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fcaoxiemeihao%2Fvite-plugins%2Ftree%2Fmain%2Fcommonjs" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/caoxiemeihao/vite-plugins/tree/main/commonjs" ref="nofollow noopener noreferrer">vite-plugin-commonjs</a></p>
<p>如果有代码如下</p>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-keyword">const</span> pkg = <span class="hljs-built_in">require</span>(<span class="hljs-string">'../package.json'</span>);

<span class="hljs-keyword">const</span> routers = [&#123;
  <span class="hljs-attr">path</span>: <span class="hljs-string">'/foo'</span>,
  <span class="hljs-attr">component</span>: <span class="hljs-built_in">require</span>(<span class="hljs-string">'@/pages/foo.vue'</span>).default;
&#125;];
<span class="copy-code-btn">复制代码</span></code></pre>
<p>将会生成:</p>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-keyword">import</span> pkg  <span class="hljs-keyword">from</span> <span class="hljs-string">"../package.json"</span>;
<span class="hljs-keyword">import</span> _MODULE_default___EXPRESSION_object__ <span class="hljs-keyword">from</span> <span class="hljs-string">"@/pages/foo.vue"</span>;

<span class="hljs-keyword">const</span> routers = [&#123;
  <span class="hljs-attr">path</span>: <span class="hljs-string">'/foo'</span>,
  <span class="hljs-attr">component</span>: _MODULE_default___EXPRESSION_object__;
&#125;];
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
</ul>
<h4 data-id="heading-8">最后我们将所有插件打包到一个 npm 包中</h4>
<ul>
<li><a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fcaoxiemeihao%2Fvite-plugin-vue2-compatible" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/caoxiemeihao/vite-plugin-vue2-compatible" ref="nofollow noopener noreferrer">完整代码 github 链接</a></li>
<li>在项目根目录添加 <code>vite.config.ts</code></li>
</ul>
<blockquote>
<p>注意：下面的配置可能需要结合你项目的情况做一些调整</p>
</blockquote>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-keyword">import</span> path <span class="hljs-keyword">from</span> <span class="hljs-string">'path'</span>
<span class="hljs-keyword">import</span> &#123; defineConfig &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'vite'</span>
<span class="hljs-keyword">import</span> &#123; createVuePlugin &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'vite-plugin-vue2'</span>
<span class="hljs-keyword">import</span> &#123;
  vitePluginCommonjs,
  dynamicImport,
  styleImport,
  symlinkIndexHtml,
&#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'vite-plugin-vue2-compatible'</span>
<span class="hljs-keyword">import</span> pkg <span class="hljs-keyword">from</span> <span class="hljs-string">'./package.json'</span>

<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> defineConfig(&#123;
  <span class="hljs-attr">plugins</span>: [
    <span class="hljs-comment">/**
     * <span class="hljs-doctag">@Repository </span>https://github.com/underfin/vite-plugin-vue2
     */</span>
    createVuePlugin(&#123;
      <span class="hljs-attr">jsx</span>: <span class="hljs-literal">true</span>,
      <span class="hljs-attr">jsxOptions</span>: &#123;
        <span class="hljs-attr">compositionAPI</span>: <span class="hljs-literal">true</span>,
      &#125;,
    &#125;),
    <span class="hljs-comment">/**
     * 处理 webpack 项目中 require 写法
     */</span>
    vitePluginCommonjs(),
    <span class="hljs-comment">/**
     * 兼容 import('<span class="hljs-doctag">@xxxx</span>') 写法别名
     */</span>
    dynamicImport(),
    <span class="hljs-comment">/**
     * 兼容 <span class="hljs-doctag">@import <span class="hljs-variable">alias</span></span>
     *   <span class="hljs-doctag">@import </span>'~normalize.css/normalize.css'
     *            ↓
     *   <span class="hljs-doctag">@import </span>'node_modules/normalize.css/normalize.css'
     */</span>
    styleImport(),
    <span class="hljs-comment">/**
     * <span class="hljs-doctag">@vue</span>/cli 项目中静态文件入口是 public/index.html
     * vite 项目是根目录下的 index.html 作为一切的入口
     * symlinkIndexHtml 将 public/index.html 文件在根目录下创建一个 index.html 的软连接
     */</span>
    symlinkIndexHtml(&#123;
      <span class="hljs-comment">// 指向 @vue/cli 创建项目的 public/index.html 文件</span>
      <span class="hljs-attr">template</span>: path.join(__dirname, <span class="hljs-string">'public/index.html'</span>),
      <span class="hljs-comment">// 告诉 vite 的入口文件 index.html 加载哪个 js；既 webpack 配置中的 entry</span>
      <span class="hljs-attr">entry</span>: <span class="hljs-string">'/src/main.js'</span>,
      <span class="hljs-comment">// 兼容 html-webpack-plugin 中的编译注入</span>
      <span class="hljs-attr">templateDate</span>: &#123;
        <span class="hljs-attr">BASE_URL</span>: <span class="hljs-string">'/'</span>,
        <span class="hljs-attr">htmlWebpackPlugin</span>: &#123;
          <span class="hljs-attr">options</span>: &#123;
            <span class="hljs-attr">title</span>: pkg.name,
          &#125;,
        &#125;,
      &#125;,
    &#125;),
  ],
  <span class="hljs-attr">resolve</span>: &#123;
    <span class="hljs-attr">alias</span>: &#123;
      <span class="hljs-comment">// 同 webpack 中的 alias</span>
      <span class="hljs-string">'@'</span>: path.join(__dirname, <span class="hljs-string">'./src'</span>),
    &#125;,
    <span class="hljs-comment">// 同 webpack 中的 extensions</span>
    <span class="hljs-attr">extensions</span>: [<span class="hljs-string">'.vue'</span>, <span class="hljs-string">'.ts'</span>, <span class="hljs-string">'.tsx'</span>, <span class="hljs-string">'.js'</span>, <span class="hljs-string">'.jsx'</span>, <span class="hljs-string">'.mjs'</span>],
  &#125;,
  <span class="hljs-attr">define</span>: &#123;
    <span class="hljs-comment">// 同 webpack.DefinePlugin</span>
    <span class="hljs-string">'process.env'</span>: process.env,
  &#125;
&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-9">运行</h4>
<ol>
<li><code>npm i -D vite vite-plugin-vue2 vite-plugin-vue2-compatible</code></li>
<li>添加 packge.json 中 scripts 命令</li>
</ol>
<pre><code class="hljs language-diff copyable" lang="diff">&#123;
  "scripts": &#123;
<span class="hljs-addition">+    "vite": "export NODE_ENV=development; vite"</span>
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<ol start="3">
<li><code>npm run vite</code></li>
</ol>
<p>🎉 Boom shakalaka!</p></div>  
</div>
            