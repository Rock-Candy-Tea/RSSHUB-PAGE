
---
title: 'Babel转换流程详解'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/6a379ee6b9c84d2ba067965bc3c6921a~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Fri, 04 Jun 2021 01:46:41 GMT
thumbnail: 'https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/6a379ee6b9c84d2ba067965bc3c6921a~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h2 data-id="heading-0">Babel是什么？</h2>
<h3 data-id="heading-1">Babel 是一个 JavaScript 编译器</h3>
<p>Babel 是一个工具链，主要用于将采用 ECMAScript 2015+ 语法编写的代码转换为向后兼容的 JavaScript 语法，以便能够运行在当前和旧版本的浏览器或其他环境中。</p>
<h2 data-id="heading-2">Babel是如何编译的？</h2>
<p>编译主要分为三个阶段：</p>
<ol>
<li><strong>parse</strong>：解析--将代码字符串解析成AST</li>
<li><strong>transform</strong>：转换--对AST进行变换操作</li>
<li><strong>generate</strong>：生成--根据转换后的AST再生成代码字符串</li>
</ol>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/6a379ee6b9c84d2ba067965bc3c6921a~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>接下来对这几个阶段一一来介绍</p>
<h3 data-id="heading-3">parse：@babel/parser</h3>
<p>@babel/parser:JavaScript解析器（以前称为 Babylon）,主要使用其API--parse()对源码进行词法分析语法分析最终转换成AST</p>
<p><strong>api：babelParser.parse(code, [options])</strong></p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// @babel/parser/lib/index.js源码 parse方法如下</span>
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">parse</span>(<span class="hljs-params">input, options</span>) </span>&#123;
  <span class="hljs-keyword">var</span> _options;
  <span class="hljs-keyword">if</span> (((_options = options) == <span class="hljs-literal">null</span> ? <span class="hljs-keyword">void</span> <span class="hljs-number">0</span> : _options.sourceType) === <span class="hljs-string">"unambiguous"</span>) &#123;
    options = <span class="hljs-built_in">Object</span>.assign(&#123;&#125;, options);
    <span class="hljs-keyword">try</span> &#123;
      options.sourceType = <span class="hljs-string">"module"</span>;
      <span class="hljs-keyword">const</span> parser = getParser(options, input);
      <span class="hljs-keyword">const</span> ast = parser.parse();
      <span class="hljs-keyword">if</span> (parser.sawUnambiguousESM) &#123;
        <span class="hljs-keyword">return</span> ast;
      &#125;
      <span class="hljs-keyword">if</span> (parser.ambiguousScriptDifferentAst) &#123;
        <span class="hljs-keyword">try</span> &#123;
          options.sourceType = <span class="hljs-string">"script"</span>;
          <span class="hljs-keyword">return</span> getParser(options, input).parse();
        &#125; <span class="hljs-keyword">catch</span> (_unused) &#123;&#125;
      &#125; <span class="hljs-keyword">else</span> &#123;
        ast.program.sourceType = <span class="hljs-string">"script"</span>;
      &#125;
      <span class="hljs-keyword">return</span> ast;
    &#125; <span class="hljs-keyword">catch</span> (moduleError) &#123;
      <span class="hljs-keyword">try</span> &#123;
        options.sourceType = <span class="hljs-string">"script"</span>;
        <span class="hljs-keyword">return</span> getParser(options, input).parse();
      &#125; <span class="hljs-keyword">catch</span> (_unused2) &#123;&#125;
      <span class="hljs-keyword">throw</span> moduleError;
    &#125;
  &#125; <span class="hljs-keyword">else</span> &#123;
    <span class="hljs-keyword">return</span> getParser(options, input).parse();
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h5 data-id="heading-4">入参options</h5>
<ul>
<li>plugins:包含要启用的插件的数组。</li>
<li>sourceType:（<strong>script|module|unambiguous</strong>）代码应该被解析的模式,默认为“script”。 “unambiguous”会使@babel/parser 尝试根据 ES6 导入或导出语句的存在进行猜测。 带有 ES6 导入和导出的文件被视为“module”，否则被视为“script”。</li>
</ul>
<h5 data-id="heading-5">Output</h5>
<p>基于<strong>ESTree</strong>规范格式生成<strong>AST</strong>。</p>
<p>参考下面的代码和图：右边是入参options，左边是生成的AST</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> add = <span class="hljs-function">(<span class="hljs-params">a,b</span>)=></span>&#123;
    <span class="hljs-keyword">return</span> a + b
&#125;
add(<span class="hljs-number">1</span>,<span class="hljs-number">2</span>)
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/e390a15f21fa4477b3cce2c85c2893f5~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-6">transform：@babel/core、@babel/traverse、@babel/types</h3>
<p>对AST语法树进行替换，调用插件@babel/core下面transform相关方法，但是transform其实是使用@babel/traverse插件对AST语法进行节点的替换、增删改查等操作</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> parser = <span class="hljs-built_in">require</span>(<span class="hljs-string">"@babel/parser"</span>);
<span class="hljs-keyword">const</span> core = <span class="hljs-built_in">require</span>(<span class="hljs-string">"@babel/core"</span>);
<span class="hljs-keyword">const</span> traverse = <span class="hljs-built_in">require</span>(<span class="hljs-string">"@babel/traverse"</span>);
<span class="hljs-keyword">const</span> types = <span class="hljs-built_in">require</span>(<span class="hljs-string">"@babel/types"</span>);
<span class="hljs-keyword">const</span> code = <span class="hljs-string">`const add = (a,b)=>&#123;
    return a + b
&#125;
add(1,2)`</span>;
<span class="hljs-comment">// options参数参考链接</span>
<span class="hljs-comment">// https://www.babeljs.cn/docs/options</span>
<span class="hljs-keyword">const</span> options = &#123;
    <span class="hljs-attr">caller</span>: &#123;
      <span class="hljs-attr">name</span>: <span class="hljs-string">'babel-loader'</span>,
      <span class="hljs-attr">target</span>: <span class="hljs-string">'web'</span>,
      <span class="hljs-attr">supportsStaticESM</span>: <span class="hljs-literal">true</span>,
      <span class="hljs-attr">supportsDynamicImport</span>: <span class="hljs-literal">true</span>,
      <span class="hljs-attr">supportsTopLevelAwait</span>: <span class="hljs-literal">true</span>
    &#125;
&#125;
<span class="hljs-comment">// 1、词法分析语法分析转换成AST</span>
<span class="hljs-keyword">const</span> ast = parser.parse(code);
<span class="hljs-comment">// transform</span>
core.transformFromAst(ast, code, options, <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">err, result</span>) </span>&#123;
   <span class="hljs-comment">// result==>code, map, ast &#125;</span>
   <span class="hljs-keyword">return</span> result
&#125;);

<span class="hljs-comment">// 2、对AST节点进行增、删、改、查操作</span>
traverse.default(ast, &#123;
    <span class="hljs-function"><span class="hljs-title">enter</span>(<span class="hljs-params">path</span>)</span> &#123;
        <span class="hljs-comment">// isArrowFunctionExpression等其实是依赖babel/types插件方法</span>
        <span class="hljs-keyword">if</span> (path.isArrowFunctionExpression(path.node)) &#123;
            path.node.type = <span class="hljs-string">'FunctionExpression'</span>
        &#125;
    &#125;
&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>1. @babel/traverse：</strong>
是一个对AST进行遍历的工具。类似字符串的replace方法，指定一个正则表达式，就能对字符串进行替换。只不过babel-traverse是针对ast进行替换。</p>
<p><strong>2.@babel/types：</strong>
检查AST节点类型和生成对应的表达式，比如判断AST节点是不是箭头函数类型：type.isArrowFunctionExpression(path.node)</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/075e1b53bcca41d0a844733b782529bd~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-7">generator：@babel/generator</h3>
<p>使用插件@babel/generator将转换好的ast重新生成目标代码。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> generate = <span class="hljs-built_in">require</span>(<span class="hljs-string">"@babel/generator"</span>);

<span class="hljs-keyword">const</span> output = generate(ast,options,code)
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/bcd5bd5e3f18481394503f43109441dd~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p></div>  
</div>
            