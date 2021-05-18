
---
title: '基于 babel 和 postcss 查找项目中的无用模块'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/a5bd20cb8290451c9c49e15be67d6a2e~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Mon, 17 May 2021 07:07:05 GMT
thumbnail: 'https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/a5bd20cb8290451c9c49e15be67d6a2e~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h2 data-id="heading-0">背景</h2>
<p>昊昊是业务线前端工程师（专业页面仔），我是架构组工具链工程师（专业工具人），有一天昊昊和说我他维护的项目中没用到的模块太多了，其实可以删掉的，但是现在不知道哪些没用，就不敢删，问我是不是可以做一个工具来找出所有没有被引用的模块。毕竟是专业的工具人，这种需求难不倒我，于是花了半天多实现了这个工具。</p>
<p>这个工具是一个通用的工具，node 项目、前端项目都可以用它来查找没有用到的模块，而且其中模块遍历器的思路可以应用到很多别的地方。所以我整理了实现思路，写了这篇文章。</p>
<h2 data-id="heading-1">思路分析</h2>
<p>目标是找到项目中所有没用到的模块。项目中总有几个入口模块，代码会从这些模块开始打包或者运行。我们首先要知道所有的入口模块。</p>
<p>有了入口模块之后，分析入口模块的用到（依赖）了哪些模块，然后再从用到的模块分析依赖，这样递归的进行分析，直到没有新的依赖。这个过程中，所有遍历到的模块就是用到的，而没有被遍历到的就是没有用到的，就是我们要找的可以删除的模块。</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/a5bd20cb8290451c9c49e15be67d6a2e~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>我们可以在遍历的过程中把模块信息和模块之间的关系以对象和对象的关系保存，构造成一个依赖图（因为可能有一个模块被两个模块依赖，甚至循环依赖，所以是图）。之后对这个依赖图的数据结构的分析就是对模块之间依赖关系的分析。我们这个需求只需要保存遍历到的模块路径就可以，可以不生成依赖图。</p>
<p>遍历到不同的模块要找到它依赖的哪些模块，对于不同的模块有不同的分析依赖的方式：</p>
<ul>
<li>js、ts、jsx、tsx 模块根据 es module 的 import 或者 commonjs 的 require 来确定依赖</li>
<li>css、less、scss 模块根据 @import 和 url() 的语法来确定依赖</li>
</ul>
<p>而且拿到了依赖的路径也可能还要做一层处理，因为比如 webpack 可以配置 alias，typescript 可以配置 paths，还有 monorepo 的路径也有自己的特点，这些路径解析规则是我们要处理的，处理之后才能找到模块真实路径是啥。</p>
<p>经过从入口模块开始的依赖分析，对模块图完成遍历，把用到的模块路径保存下来，然后用所有模块路径过滤掉用到的，剩下的就是没有使用的模块。</p>
<p>思路大概这样，我们来实现一下：</p>
<h2 data-id="heading-2">代码实现</h2>
<h3 data-id="heading-3">模块遍历</h3>
<p>我们要写一个模块遍历器，传入当前模块的路径和处理模块内容的回调函数，处理过程如下：</p>
<ul>
<li>尝试补全路径，因为 .js、.json、.tsx 等可以省略后缀名</li>
<li>根据路径获得模块的类型</li>
<li>如果是 js 模块，用遍历 js 的方式进行处理</li>
<li>如果是 css 模块，用遍历 css 的方式进行处理</li>
</ul>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">const</span> MODULE_TYPES = &#123;
    <span class="hljs-attr">JS</span>: <span class="hljs-number">1</span> << <span class="hljs-number">0</span>,
    <span class="hljs-attr">CSS</span>: <span class="hljs-number">1</span> << <span class="hljs-number">1</span>,
    <span class="hljs-attr">JSON</span>: <span class="hljs-number">1</span> << <span class="hljs-number">2</span>
&#125;;

<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">getModuleType</span>(<span class="hljs-params">modulePath</span>) </span>&#123;
    <span class="hljs-keyword">const</span> moduleExt = extname(modulePath);
     <span class="hljs-keyword">if</span> (JS_EXTS.some(<span class="hljs-function"><span class="hljs-params">ext</span> =></span> ext === moduleExt)) &#123;
         <span class="hljs-keyword">return</span> MODULE_TYPES.JS;
     &#125; <span class="hljs-keyword">else</span> <span class="hljs-keyword">if</span> (CSS_EXTS.some(<span class="hljs-function"><span class="hljs-params">ext</span> =></span> ext === moduleExt)) &#123;
         <span class="hljs-keyword">return</span> MODULE_TYPES.CSS;
     &#125; <span class="hljs-keyword">else</span> <span class="hljs-keyword">if</span> (JSON_EXTS.some(<span class="hljs-function"><span class="hljs-params">ext</span> =></span> ext === moduleExt)) &#123;
         <span class="hljs-keyword">return</span> MODULE_TYPES.JSON;
     &#125;
&#125;

<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">traverseModule</span> (<span class="hljs-params">curModulePath, callback</span>) </span>&#123;
    curModulePath = completeModulePath(curModulePath);

    <span class="hljs-keyword">const</span> moduleType = getModuleType(curModulePath);

    <span class="hljs-keyword">if</span> (moduleType & MODULE_TYPES.JS) &#123;
        traverseJsModule(curModulePath, callback);
    &#125; <span class="hljs-keyword">else</span> <span class="hljs-keyword">if</span> (moduleType & MODULE_TYPES.CSS) &#123;
        traverseCssModule(curModulePath, callback);
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-4">js 模块遍历</h4>
<p>遍历 js 模块需要分析其中的 import 和 require 依赖。我们使用 babel 来做：</p>
<ul>
<li>读取文件内容</li>
<li>根据后缀名是 .jsx、.tsx 等来决定是否启用 typescript、jsx 的 parse 插件</li>
<li>使用 babel parser 把代码转成 AST</li>
<li>使用 babel traverse 对 AST 进行遍历</li>
<li>处理 ImportDeclaration 和 CallExpression 的 AST，从中提取依赖路径</li>
<li>对依赖路径进行处理，变成真实路径之后，继续遍历该路径的模块</li>
</ul>
<p>代码如下：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">traverseJsModule</span>(<span class="hljs-params">curModulePath, callback</span>) </span>&#123;
    <span class="hljs-keyword">const</span> moduleFileContent = fs.readFileSync(curModulePath, &#123;
        <span class="hljs-attr">encoding</span>: <span class="hljs-string">'utf-8'</span>
    &#125;);

    <span class="hljs-keyword">const</span> ast = parser.parse(moduleFileContent, &#123;
        <span class="hljs-attr">sourceType</span>: <span class="hljs-string">'unambiguous'</span>,
        <span class="hljs-attr">plugins</span>: resolveBabelSyntaxtPlugins(curModulePath)
    &#125;);

    traverse(ast, &#123;
        <span class="hljs-function"><span class="hljs-title">ImportDeclaration</span>(<span class="hljs-params">path</span>)</span> &#123;
            <span class="hljs-keyword">const</span> subModulePath = moduleResolver(curModulePath, path.get(<span class="hljs-string">'source.value'</span>).node);
            <span class="hljs-keyword">if</span> (!subModulePath) &#123;
                <span class="hljs-keyword">return</span>;
            &#125;
            callback && callback(subModulePath);
            traverseModule(subModulePath, callback);
        &#125;,
        <span class="hljs-function"><span class="hljs-title">CallExpression</span>(<span class="hljs-params">path</span>)</span> &#123;
            <span class="hljs-keyword">if</span> (path.get(<span class="hljs-string">'callee'</span>).toString() === <span class="hljs-string">'require'</span>) &#123;
                <span class="hljs-keyword">const</span> subModulePath = moduleResolver(curModulePath, path.get(<span class="hljs-string">'arguments.0'</span>).toString().replace(<span class="hljs-regexp">/['"]/g</span>, <span class="hljs-string">''</span>));
                <span class="hljs-keyword">if</span> (!subModulePath) &#123;
                    <span class="hljs-keyword">return</span>;
                &#125;
                callback && callback(subModulePath);
                traverseModule(subModulePath, callback);
            &#125;
        &#125;
    &#125;)
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-5">css 模块遍历</h4>
<p>遍历 css 模块需要分析 @import 和 url()。我们使用 postcss 来做：</p>
<ul>
<li>读取文件内容</li>
<li>根据文件路径是 .less、.scss 来决定是否启用 less、scss 的语法插件</li>
<li>使用 postcss.parse 把文件内容转成 AST</li>
<li>遍历 @import 节点，提取依赖路径</li>
<li>遍历样式声明（declaration），过滤出 url() 的值，提取依赖路径</li>
<li>对依赖路径进行处理，变成真实路径之后，继续遍历该路径的模块</li>
</ul>
<p>代码如下：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">traverseCssModule</span>(<span class="hljs-params">curModulePath, callback</span>) </span>&#123;
    <span class="hljs-keyword">const</span> moduleFileConent = fs.readFileSync(curModulePath, &#123;
        <span class="hljs-attr">encoding</span>: <span class="hljs-string">'utf-8'</span>
    &#125;);

    <span class="hljs-keyword">const</span> ast = postcss.parse(moduleFileConent, &#123;
        <span class="hljs-attr">syntaxt</span>: resolvePostcssSyntaxtPlugin(curModulePath)
    &#125;);
    ast.walkAtRules(<span class="hljs-string">'import'</span>, <span class="hljs-function"><span class="hljs-params">rule</span> =></span> &#123;
        <span class="hljs-keyword">const</span> subModulePath = moduleResolver(curModulePath, rule.params.replace(<span class="hljs-regexp">/['"]/g</span>, <span class="hljs-string">''</span>));
        <span class="hljs-keyword">if</span> (!subModulePath) &#123;
            <span class="hljs-keyword">return</span>;
        &#125;
        callback && callback(subModulePath);
        traverseModule(subModulePath, callback);
    &#125;);
    ast.walkDecls(<span class="hljs-function"><span class="hljs-params">decl</span> =></span> &#123;
        <span class="hljs-keyword">if</span> (decl.value.includes(<span class="hljs-string">'url('</span>)) &#123;
            <span class="hljs-keyword">const</span> url = <span class="hljs-regexp">/.*url\((.+)\).*/</span>.exec(decl.value)[<span class="hljs-number">1</span>].replace(<span class="hljs-regexp">/['"]/g</span>, <span class="hljs-string">''</span>);
            <span class="hljs-keyword">const</span> subModulePath = moduleResolver(curModulePath, url);
            <span class="hljs-keyword">if</span> (!subModulePath) &#123;
                <span class="hljs-keyword">return</span>;
            &#125;
            callback && callback(subModulePath);
        &#125;
    &#125; )
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-6">模块路径处理</h4>
<p>不管是 css 还是 js 模块都要在提取了路径之后进行处理：</p>
<ul>
<li>支持自定义路径解析逻辑，让用户可以根据需要定制路径解析的规则</li>
<li>过滤掉 node_modules 下的模块，不需要分析</li>
<li>补全路径的后缀名</li>
<li>如果遍历过的模块则跳过遍历，避免循环依赖</li>
</ul>
<p>代码如下：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">const</span> visitedModules = <span class="hljs-keyword">new</span> <span class="hljs-built_in">Set</span>();

<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">moduleResolver</span> (<span class="hljs-params">curModulePath, requirePath</span>) </span>&#123;
    <span class="hljs-keyword">if</span> (<span class="hljs-keyword">typeof</span> requirePathResolver === <span class="hljs-string">'function'</span>) &#123;<span class="hljs-comment">// requirePathResolver 是用户自定义的路径解析逻辑</span>
        <span class="hljs-keyword">const</span> res = requirePathResolver(dirname(curModulePath), requirePath);
        <span class="hljs-keyword">if</span> (<span class="hljs-keyword">typeof</span> res === <span class="hljs-string">'string'</span>) &#123;
            requirePath = res;
        &#125;
    &#125;

    requirePath = resolve(dirname(curModulePath), requirePath);

    <span class="hljs-comment">// 过滤掉第三方模块</span>
    <span class="hljs-keyword">if</span> (requirePath.includes(<span class="hljs-string">'node_modules'</span>)) &#123;
        <span class="hljs-keyword">return</span> <span class="hljs-string">''</span>;
    &#125;

    requirePath =  completeModulePath(requirePath);

    <span class="hljs-keyword">if</span> (visitedModules.has(requirePath)) &#123;
        <span class="hljs-keyword">return</span> <span class="hljs-string">''</span>;
    &#125; <span class="hljs-keyword">else</span> &#123;
        visitedModules.add(requirePath);
    &#125;
    <span class="hljs-keyword">return</span> requirePath;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这样我们就完成了分析出的依赖路径到它真实的路径的转换。</p>
<h4 data-id="heading-7">路径补全</h4>
<p>写代码的时候是可以省略掉一些文件的后缀(.js、.tsx、.json 等)的，我们要实现补全的逻辑：</p>
<ul>
<li>如果已经有后缀名了，则跳过</li>
<li>如果是目录，则尝试查找 index.xxx 的文件，找到了则返回该路径</li>
<li>如果是文件，则尝试补全 .xxx 的后缀，找到了则返回该路径</li>
<li>没有找到则报错：module not found</li>
</ul>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">const</span> JS_EXTS = [<span class="hljs-string">'.js'</span>, <span class="hljs-string">'.jsx'</span>, <span class="hljs-string">'.ts'</span>, <span class="hljs-string">'.tsx'</span>];
<span class="hljs-keyword">const</span> JSON_EXTS = [<span class="hljs-string">'.json'</span>];

<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">completeModulePath</span> (<span class="hljs-params">modulePath</span>) </span>&#123;
    <span class="hljs-keyword">const</span> EXTS = [...JSON_EXTS, ...JS_EXTS];
    <span class="hljs-keyword">if</span> (modulePath.match(<span class="hljs-regexp">/\.[a-zA-Z]+$/</span>)) &#123;
        <span class="hljs-keyword">return</span> modulePath;
    &#125;

    <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">tryCompletePath</span> (<span class="hljs-params">resolvePath</span>) </span>&#123;
        <span class="hljs-keyword">for</span> (<span class="hljs-keyword">let</span> i = <span class="hljs-number">0</span>; i < EXTS.length; i ++) &#123;
            <span class="hljs-keyword">let</span> tryPath = resolvePath(EXTS[i]);
            <span class="hljs-keyword">if</span> (fs.existsSync(tryPath)) &#123;
                <span class="hljs-keyword">return</span> tryPath;
            &#125;
        &#125;
    &#125;

    <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">reportModuleNotFoundError</span> (<span class="hljs-params">modulePath</span>) </span>&#123;
        <span class="hljs-keyword">throw</span> chalk.red(<span class="hljs-string">'module not found: '</span> + modulePath);
    &#125;

    <span class="hljs-keyword">if</span> (isDirectory(modulePath)) &#123;
        <span class="hljs-keyword">const</span> tryModulePath = tryCompletePath(<span class="hljs-function">(<span class="hljs-params">ext</span>) =></span> join(modulePath, <span class="hljs-string">'index'</span> + ext));
        <span class="hljs-keyword">if</span> (!tryModulePath) &#123;
            reportModuleNotFoundError(modulePath);
        &#125; <span class="hljs-keyword">else</span> &#123;
            <span class="hljs-keyword">return</span> tryModulePath;
        &#125;
    &#125; <span class="hljs-keyword">else</span> <span class="hljs-keyword">if</span> (!EXTS.some(<span class="hljs-function"><span class="hljs-params">ext</span> =></span> modulePath.endsWith(ext))) &#123;
        <span class="hljs-keyword">const</span> tryModulePath = tryCompletePath(<span class="hljs-function">(<span class="hljs-params">ext</span>) =></span> modulePath + ext);
        <span class="hljs-keyword">if</span> (!tryModulePath) &#123;
            reportModuleNotFoundError(modulePath);
        &#125; <span class="hljs-keyword">else</span> &#123;
            <span class="hljs-keyword">return</span> tryModulePath;
        &#125;
    &#125;
    <span class="hljs-keyword">return</span> modulePath;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>按照上面的思路，我们实现了模块的遍历，找到了所有的用到的模块。</p>
<h3 data-id="heading-8">过滤出无用模块</h3>
<p>上面我们找到了所有用到的模块，接下来只要用所有的模块过滤掉用到的模块，就是没有用到的模块。</p>
<p>我们封装一个 findUnusedModule 的方法。</p>
<p>传入参数：</p>
<ul>
<li>entries（入口模块数组）</li>
<li>includes（所有模块的 glob 表达式）</li>
<li>resolveRequirePath（自定义路径解析逻辑）</li>
<li>cwd（解析模块的根路径）</li>
</ul>
<p>返回一个对象，包含：</p>
<ul>
<li>all (所有模块)</li>
<li>used（用到的模块）</li>
<li>unused（没用到的模块）</li>
</ul>
<p>处理过程:</p>
<ul>
<li>合并参数和默认参数</li>
<li>基于 cwd 处理 includes 的模块路径</li>
<li>根据 includes 的 glob 表达式找出所有的模块</li>
<li>以所有 entires 为入口进行遍历，记录用到的模块</li>
<li>过滤掉用到的模块，求出没有用到的模块</li>
</ul>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">const</span> defaultOptions = &#123;
    <span class="hljs-attr">cwd</span>: <span class="hljs-string">''</span>,
    <span class="hljs-attr">entries</span>: [],
    <span class="hljs-attr">includes</span>: [<span class="hljs-string">'**/*'</span>, <span class="hljs-string">'!node_modules'</span>],
    <span class="hljs-attr">resolveRequirePath</span>: <span class="hljs-function">() =></span> &#123;&#125;
&#125;

<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">findUnusedModule</span> (<span class="hljs-params">options</span>) </span>&#123;
    <span class="hljs-keyword">let</span> &#123;
        cwd,
        entries,
        includes,
        resolveRequirePath
    &#125; = <span class="hljs-built_in">Object</span>.assign(defaultOptions, options);

    includes = includes.map(<span class="hljs-function"><span class="hljs-params">includePath</span> =></span> (cwd ? <span class="hljs-string">`<span class="hljs-subst">$&#123;cwd&#125;</span>/<span class="hljs-subst">$&#123;includePath&#125;</span>`</span> : includePath));

    <span class="hljs-keyword">const</span> allFiles = fastGlob.sync(includes).map(<span class="hljs-function"><span class="hljs-params">item</span> =></span> normalize(item));
    <span class="hljs-keyword">const</span> entryModules = [];
    <span class="hljs-keyword">const</span> usedModules = [];

    setRequirePathResolver(resolveRequirePath);
    entries.forEach(<span class="hljs-function"><span class="hljs-params">entry</span> =></span> &#123;
        <span class="hljs-keyword">const</span> entryPath = resolve(cwd, entry);
        entryModules.push(entryPath);
        traverseModule(entryPath, <span class="hljs-function">(<span class="hljs-params">modulePath</span>) =></span> &#123;
            usedModules.push(modulePath);
        &#125;);
    &#125;);

    <span class="hljs-keyword">const</span> unusedModules = allFiles.filter(<span class="hljs-function"><span class="hljs-params">filePath</span> =></span> &#123;
        <span class="hljs-keyword">const</span> resolvedFilePath = resolve(filePath);
        <span class="hljs-keyword">return</span> !entryModules.includes(resolvedFilePath) && !usedModules.includes(resolvedFilePath);
    &#125;);
    <span class="hljs-keyword">return</span> &#123;
        <span class="hljs-attr">all</span>: allFiles,
        <span class="hljs-attr">used</span>: usedModules,
        <span class="hljs-attr">unused</span>: unusedModules
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这样，我们封装的 findUnusedModule 能够完成最初的需求：查找项目下没有用到的模块。</p>
<h2 data-id="heading-9">测试功能</h2>
<p>我们来测试一下效果，用<a href="https://github.com/QuarkGluonPlasma/find-unused-module/tree/master/demo-project" target="_blank" rel="nofollow noopener noreferrer">这个目录</a>作为测试项目：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">const</span> &#123; all, used, unused &#125; = findUnusedModule(&#123;
    <span class="hljs-attr">cwd</span>: process.cwd(),
    <span class="hljs-attr">entries</span>: [<span class="hljs-string">'./demo-project/fre.js'</span>, <span class="hljs-string">'./demo-project/suzhe2.js'</span>],
    <span class="hljs-attr">includes</span>: [<span class="hljs-string">'./demo-project/**/*'</span>],
    resolveRequirePath (curDir, requirePath) &#123;
        <span class="hljs-keyword">if</span> (requirePath === <span class="hljs-string">'b'</span>) &#123;
            <span class="hljs-keyword">return</span> path.resolve(curDir, <span class="hljs-string">'./lib/ssh.js'</span>);
        &#125;
        <span class="hljs-keyword">return</span> requirePath;
    &#125;
&#125;);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>结果如下：</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/183f68407d854cb3975025f05e642651~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>成功的找出了没有用到的模块！（可以把<a href="https://github.com/QuarkGluonPlasma/find-unused-module" target="_blank" rel="nofollow noopener noreferrer">代码</a>拉下来跑一下试试）</p>
<h2 data-id="heading-10">思考</h2>
<p>我们实现了一个模块遍历器，它可以对从某一个模块开始遍历。基于这个遍历器我们实现了查找无用模块的需求，其实也可以用它来做别的分析需求，这个遍历的方式是通用的。</p>
<p>我们知道 babel 可以用来做两件事情：</p>
<ul>
<li>代码的转译： 从 es next、typescript 等代码转译成目标环境支持的 js</li>
<li>静态分析： 对代码内容做分析，比如类型检查、lint 等，不生成代码</li>
</ul>
<p>这个模块遍历器也可以做同样的事情：</p>
<ul>
<li>静态分析：分析模块间的依赖关系，构造依赖图，完成一些分析功能</li>
<li>打包：把依赖图中每一个模块用相应的代码模版打印成目标代码</li>
</ul>
<h2 data-id="heading-11">总结</h2>
<p>我们先分析了需求：找出项目中没用到的模块。这需要实现一个模块遍历器。</p>
<p>模块遍历要对 js 模块和 css 模块做不同的处理：js 模块分析 import 和 require，css 分析 url() 和 @import。</p>
<p>之后要对分析出的路径做处理，变成真实路径。要处理 node_modules、webpack alias、typescript 的 types 等情况，我们暴露了一个回调函数给开发者自己去扩展。</p>
<p>实现了模块遍历之后，只要指定所有的模块、入口模块，那么我们就可以找出用到了哪些模块，没用到哪些模块。</p>
<p>经过测试，符合我们的需求。</p>
<p>这个模块遍历器是通用的，可以用来做各种静态分析，也可以做后续的代码打印做成一个打包器。</p>
<p><a href="https://github.com/QuarkGluonPlasma/find-unused-module" target="_blank" rel="nofollow noopener noreferrer">代码的 github 地址</a>在这，感兴趣可以拉下来跑跑，学会写模块遍历器还是挺有帮助的。</p>
<h2 data-id="heading-12">彩蛋</h2>
<p>当时给昊昊介绍这个功能的时候，写了一份实现思路的文档，也贴在这里吧：</p>
<p><strong>昊昊</strong>: 光哥，整体的思路是什么样的啊，一上来就看代码比较乱</p>
<p><strong>我</strong>： 模块是一个图的结构，指定从某个入口开始遍历，其实这是一个 dfs 的过程，但是有循环引用，要通过记录处理过的模块来解决。递归遍历这个图，处理到的模块就是用到的。</p>
<p><strong>昊昊</strong>： dfs 一个模块，怎么确定子模块呢？</p>
<p><strong>我</strong>： 不同的模块有不同的处理方式，比如 js 模块，就要通过 import 或者 require 来确定子模块，而 css 则要通过 @import 和 url() 来确定。 但是这些只是提取路径，这个路径还是不可用的，还需要转换成真实路径，要有一个 resolve path 的过程。</p>
<p><strong>昊昊</strong>： resolve path 都做啥啊？</p>
<p><strong>我</strong>： 就是处理 alias、过滤 node_modules 下的模块，因为我们这里用不到，然后根据当前模块的路径确定子模块的绝对路径。还要暴露出一个钩子函数去让用户能够自定义 require path 的 resolve 逻辑。</p>
<p><strong>昊昊</strong>： 就是那个 requireRequirePath 么？</p>
<p><strong>我</strong>： 对的，那个就是暴露出去让用户自定义 path resolve 逻辑的钩子。</p>
<p><strong>昊昊</strong>： 我大体明白流程了？</p>
<p><strong>我</strong>： 说说看</p>
<p><strong>昊昊</strong>： 项目的模块构成依赖图，我们要确定没有用到的模块，那就要先找出用到的模块，之后把它们过滤掉。用到的模块要用几个入口模块开始做 dfs，遍历不同的模块有不同的提取 require path 的方式，提取出来以后还要对 path 进行 resolve，得到真实路径，然后递归进行子模块的处理。这样遍历完一遍就能确定用到了哪些。同时还要处理循环引用问题，因为毕竟模块是一个图，进行 dfs 会有环在。</p>
<p><strong>我</strong>： 对的，棒棒的。</p></div>  
</div>
            