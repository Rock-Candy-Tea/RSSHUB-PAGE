
---
title: '【JS】简简单单的一次babel大扫盲！'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=6049'
author: 掘金
comments: false
date: Sun, 04 Apr 2021 19:39:58 GMT
thumbnail: 'https://picsum.photos/400/300?random=6049'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h2 data-id="heading-0">祖传开头</h2>
<blockquote>
<p>早睡早起保平安</p>
</blockquote>
<p>这篇文章算是一次关于babel的一次扫盲。整理出一份babel的基础概念扫盲，写给自己，也写需要这种基础梳理的小伙伴吧。希望大家都不要因为非常基础的问题，比如babel版本之类的小问题绊住了手脚哈哈哈！另外babel也是一个非常好的学习工具，可以把es6的代码转化成es5，抛开各种语法糖，探究js的本质。总而言之，希望这篇文章能对各位有所助益吧~</p>
<h2 data-id="heading-1">一、Babel基本概念</h2>
<blockquote>
<p>Babel 是一个通用的多功能的 JavaScript 编译器。将ECMAScript 2015+ 的代码转化成能适配各种低端游览器或者其他环境（Node）的代码。</p>
</blockquote>
<p><strong>特点：</strong></p>
<ul>
<li>静态分析，在不需要执行代码的情况下，对代码分析处理。</li>
<li>通过组合各种模块，生一个能实现特定功能的集合。</li>
<li>@babel/core 包含了所有babel的 核心功能，使用babel前必须先引入。</li>
</ul>
<h2 data-id="heading-2">🌰一个简单的例子</h2>
<p><br><strong>第一步：在 <code>.babelrc</code> 文件中进行babel的配置。</strong></p>
<blockquote>
<p>当然还有其他的配置方式，比如创建一个babel.config.js文件或者直接在package.json中的babel字段下进行配置。</p>
</blockquote>
<pre><code class="hljs language-json copyable" lang="json">&#123;
    <span class="hljs-attr">"presets"</span>: [
        [
            <span class="hljs-string">"@babel/preset-env"</span>
        ]
    ]
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>**第二步：安装 <code>@babel/core</code> 、 <code>@babel/cli</code> 和 **<code>**@babel/preset-env**</code> <strong>。</strong><br>@babel/core是babel的和核心库。@babel/cli是babel能在终端环境中可以运行的工具库。<br>
<br><strong>第三步：创建源代码文件和babel运行命令。</strong><br>
<br>src/index.js</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">const</span> newArys = [<span class="hljs-number">1</span>, <span class="hljs-number">2</span>, <span class="hljs-number">3</span>, <span class="hljs-number">4</span>, <span class="hljs-number">5</span>].map(<span class="hljs-function">(<span class="hljs-params">n</span>) =></span> n * n);
<span class="copy-code-btn">复制代码</span></code></pre>
<p><br>package.json</p>
<pre><code class="hljs language-json copyable" lang="json"><span class="hljs-string">"scripts"</span>: &#123;
    <span class="hljs-attr">"compiler"</span>: <span class="hljs-string">"babel src --out-dir lib"</span>,
    <span class="hljs-attr">"watch"</span>: <span class="hljs-string">"npm run compiler -- --watch"</span>
 &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>命令 <code>compiler</code> 的作用就是将 <code>src</code> 目录下所有的JavaScript文件都进行解析，最后输出到 <code>lib</code> 目录下。<br>命令 <code>watch</code> 的作用就是监听 <code>src</code> 目录下是否有进行改动，若有就重新进行编译。</p>
<blockquote>
<p>tips：向 npm 脚本传入参数，要使用--标明。</p>
</blockquote>
<p>**<br><strong>更多babel-cli命令</strong><br>以下列举了几个比较常见的配置命令。</p>



































<table><thead><tr><th></th><th>说明</th><th>使用</th></tr></thead><tbody><tr><td>--out-file/-o</td><td>指定输出文件</td><td>babel src --out-file index.js</td></tr><tr><td>--out-dir/-o</td><td>指定输出目录</td><td>babel src --out-dir lib</td></tr><tr><td>--watch/-w</td><td>监听文件改动并且进行重新编译</td><td>babel src --out-dir lib --watch</td></tr><tr><td>--source-maps/-s</td><td>生成映射代码</td><td>babel src --out-file script-compiled.js --source-maps</td></tr><tr><td>--ignore</td><td>指定不需要转换的文件</td><td>babel src --out-dir lib ---ignore "src/**/*.spec.js",</td></tr></tbody></table>
<p><a href="https://www.babeljs.cn/docs/babel-cli" target="_blank" rel="nofollow noopener noreferrer">www.babeljs.cn/docs/babel-…</a></p>
<h2 data-id="heading-3">二、Babel原理</h2>
<h4 data-id="heading-4">三个步骤</h4>
<p>babel的处理步骤主要分为以下步骤：</p>
<h4 data-id="heading-5">第一步：解析（parse）</h4>
<p>将原代码转换成AST树，也就是抽象语法树。这个步骤分为两个阶段：</p>
<ul>
<li>词法分析</li>
<li>语法分析</li>
</ul>
<p><br><code>词法分析</code> 简单的来理解，就是把原代码（字符串形式）进行分割，生成一个个最小单位——令牌（token），方便后续的组装。<br>一个简单的表达式：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript">a * b
<span class="copy-code-btn">复制代码</span></code></pre>
<p>经过词法分析后，以上表达式分割成3个部分。变成一组 <code>令牌流（tokens）</code> 。形式如下：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript">[
  &#123; <span class="hljs-attr">type</span>: &#123; ... &#125;, <span class="hljs-attr">value</span>: <span class="hljs-string">"a"</span>, <span class="hljs-attr">start</span>: <span class="hljs-number">0</span>, <span class="hljs-attr">end</span>: <span class="hljs-number">1</span>, <span class="hljs-attr">loc</span>: &#123; ... &#125; &#125;,
  &#123; <span class="hljs-attr">type</span>: &#123; ... &#125;, <span class="hljs-attr">value</span>: <span class="hljs-string">"*"</span>, <span class="hljs-attr">start</span>: <span class="hljs-number">2</span>, <span class="hljs-attr">end</span>: <span class="hljs-number">3</span>, <span class="hljs-attr">loc</span>: &#123; ... &#125; &#125;,
  &#123; <span class="hljs-attr">type</span>: &#123; ... &#125;, <span class="hljs-attr">value</span>: <span class="hljs-string">"b"</span>, <span class="hljs-attr">start</span>: <span class="hljs-number">4</span>, <span class="hljs-attr">end</span>: <span class="hljs-number">5</span>, <span class="hljs-attr">loc</span>: &#123; ... &#125; &#125;,
  ...
]
<span class="copy-code-btn">复制代码</span></code></pre>
<p><code>词法分析</code> ，就是把每个token的关系描述清楚，把有关系的token组合在一起。比如上述三个token组合起来就是个获取乘积的表达式。经过词法分析后，就会生成AST树。<br>
<br>🎄先来看一个具体的AST树：（通过<a href="https://astexplorer.net/" target="_blank" rel="nofollow noopener noreferrer">AST Explorer</a>模拟AST树的生成）<br>源码：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">add</span>(<span class="hljs-params">a, b</span>) </span>&#123;
  <span class="hljs-keyword">return</span> a + b
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="hljs language-json copyable" lang="json">&#123;
  <span class="hljs-attr">"type"</span>: <span class="hljs-string">"Program"</span>,
  <span class="hljs-attr">"start"</span>: <span class="hljs-number">0</span>,
  <span class="hljs-attr">"end"</span>: <span class="hljs-number">37</span>,
  <span class="hljs-attr">"body"</span>: [
    &#123;
      <span class="hljs-attr">"type"</span>: <span class="hljs-string">"FunctionDeclaration"</span>,
      <span class="hljs-attr">"start"</span>: <span class="hljs-number">0</span>,
      <span class="hljs-attr">"end"</span>: <span class="hljs-number">37</span>,
      <span class="hljs-attr">"id"</span>: &#123;
        <span class="hljs-attr">"type"</span>: <span class="hljs-string">"Identifier"</span>,
        <span class="hljs-attr">"start"</span>: <span class="hljs-number">9</span>,
        <span class="hljs-attr">"end"</span>: <span class="hljs-number">12</span>,
        <span class="hljs-attr">"name"</span>: <span class="hljs-string">"add"</span>
      &#125;,
      <span class="hljs-attr">"expression"</span>: <span class="hljs-literal">false</span>,
      <span class="hljs-attr">"generator"</span>: <span class="hljs-literal">false</span>,
      <span class="hljs-attr">"async"</span>: <span class="hljs-literal">false</span>,
      <span class="hljs-attr">"params"</span>: [
        &#123;
          <span class="hljs-attr">"type"</span>: <span class="hljs-string">"Identifier"</span>,
          <span class="hljs-attr">"start"</span>: <span class="hljs-number">13</span>,
          <span class="hljs-attr">"end"</span>: <span class="hljs-number">14</span>,
          <span class="hljs-attr">"name"</span>: <span class="hljs-string">"a"</span>
        &#125;,
        &#123;
          <span class="hljs-attr">"type"</span>: <span class="hljs-string">"Identifier"</span>,
          <span class="hljs-attr">"start"</span>: <span class="hljs-number">16</span>,
          <span class="hljs-attr">"end"</span>: <span class="hljs-number">17</span>,
          <span class="hljs-attr">"name"</span>: <span class="hljs-string">"b"</span>
        &#125;
      ],
      <span class="hljs-attr">"body"</span>: &#123;
        <span class="hljs-attr">"type"</span>: <span class="hljs-string">"BlockStatement"</span>,
        <span class="hljs-attr">"start"</span>: <span class="hljs-number">19</span>,
        <span class="hljs-attr">"end"</span>: <span class="hljs-number">37</span>,
        <span class="hljs-attr">"body"</span>: [
          &#123;
            <span class="hljs-attr">"type"</span>: <span class="hljs-string">"ReturnStatement"</span>,
            <span class="hljs-attr">"start"</span>: <span class="hljs-number">23</span>,
            <span class="hljs-attr">"end"</span>: <span class="hljs-number">35</span>,
            <span class="hljs-attr">"argument"</span>: &#123;
              <span class="hljs-attr">"type"</span>: <span class="hljs-string">"BinaryExpression"</span>,
              <span class="hljs-attr">"start"</span>: <span class="hljs-number">30</span>,
              <span class="hljs-attr">"end"</span>: <span class="hljs-number">35</span>,
              <span class="hljs-attr">"left"</span>: &#123;
                <span class="hljs-attr">"type"</span>: <span class="hljs-string">"Identifier"</span>,
                <span class="hljs-attr">"start"</span>: <span class="hljs-number">30</span>,
                <span class="hljs-attr">"end"</span>: <span class="hljs-number">31</span>,
                <span class="hljs-attr">"name"</span>: <span class="hljs-string">"a"</span>
              &#125;,
              <span class="hljs-attr">"operator"</span>: <span class="hljs-string">"+"</span>,
              <span class="hljs-attr">"right"</span>: &#123;
                <span class="hljs-attr">"type"</span>: <span class="hljs-string">"Identifier"</span>,
                <span class="hljs-attr">"start"</span>: <span class="hljs-number">34</span>,
                <span class="hljs-attr">"end"</span>: <span class="hljs-number">35</span>,
                <span class="hljs-attr">"name"</span>: <span class="hljs-string">"b"</span>
              &#125;
            &#125;
          &#125;
        ]
      &#125;
    &#125;
  ],
  <span class="hljs-attr">"sourceType"</span>: <span class="hljs-string">"module"</span>
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>AST树的每一层结构都比较相似，每一层树都会由一个个节点（<strong>Node</strong>）构成。每个节点的type都会对这个节点的类型进行说明：</p>
<ul>
<li><code>Program</code> ：一个程序的根节点类型</li>
<li><code>FunctionDeclaration</code> ：函数声明</li>
<li><code>Identifier</code> ：变量声明</li>
<li><code>BinaryExpression</code> ：表达式</li>
<li>...</li>
</ul>
<pre><code class="hljs language-json copyable" lang="json">&#123;
   type:<span class="hljs-string">""</span>,
   id:<span class="hljs-string">""</span>,
   params:&#123;&#125;,
   body:&#123;&#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<blockquote>
<p>每个节点都可以是一个树形结构，成千上万的节点组成的一个AST树。这样就完成了一次对代码的静态分析。</p>
</blockquote>
<h4 data-id="heading-6"></h4>
<h4 data-id="heading-7">第二步：转换（transform）</h4>
<p>这个步骤就是接收到第一步生成的AST树后进行<strong>遍历</strong>，对AST的节点进行更新、添加、删除等操作。也是整个编译过程中最复杂的部分，也是babel插件介入工作并完成一些特定功能的过程。<br>
<br><strong>babel插件原理：</strong></p>
<ul>
<li>创建一个访问者，这个访问者对象会提供具体的获取树节点信息的方法</li>
<li>实际访问的是一个<strong>路径</strong></li>
</ul>
<p>**<br>🌰看一个简单的babel插件例子</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">// babel-plugins-mm</span>
<span class="hljs-built_in">module</span>.exports = <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params"></span>) </span>&#123;
    <span class="hljs-keyword">return</span> &#123;
        <span class="hljs-attr">visitor</span>:&#123;
            <span class="hljs-attr">Identifier</span>: &#123;
                <span class="hljs-function"><span class="hljs-title">enter</span>(<span class="hljs-params">path</span>)</span> &#123;
                    <span class="hljs-built_in">console</span>.log(<span class="hljs-string">"Entered!"</span>+ path.node.name);
                &#125;,
                <span class="hljs-function"><span class="hljs-title">exit</span>(<span class="hljs-params">path</span>)</span> &#123;
                    <span class="hljs-built_in">console</span>.log(<span class="hljs-string">"Exited!"</span>+ path.node.name);
                &#125;
            &#125;
        &#125;
    &#125;;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>使用插件：（只写插件名称，默认会从node-modules里查找）<br><code>mm</code> 是 <code>babel-plugins-mm</code> 的简写。</p>
<pre><code class="hljs language-json copyable" lang="json">&#123;
    <span class="hljs-attr">"presets"</span>: [
        [<span class="hljs-string">"@babel/preset-env"</span>]
    ],
    <span class="hljs-attr">"plugins"</span>: [
        [<span class="hljs-string">"mm"</span>]
    ]
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-8">第三步：生成（generate）</h4>
<p>最后一步就是就是将处理过后的AST再次转化后字符串形式的代码。（深度优先的遍历AST树，并生成字符串形式的代码。）</p>
<h2 data-id="heading-9">三、Babel配置</h2>
<pre><code class="hljs language-json copyable" lang="json">&#123;
  <span class="hljs-comment">// 预设</span>
  <span class="hljs-attr">"presets"</span>:[...],
  <span class="hljs-comment">// 插件</span>
  <span class="hljs-attr">"plugins"</span>:[...],
  <span class="hljs-comment">// 环境配置</span>
  <span class="hljs-attr">"env"</span>: &#123;
     <span class="hljs-attr">"development"</span>: &#123;
       <span class="hljs-attr">"plugins"</span>: [...]
     &#125;,
     <span class="hljs-attr">"production"</span>: &#123;
       <span class="hljs-attr">"plugins"</span>: [...]
     &#125;
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-10">4、Babel预设</h2>
<blockquote>
<p>就是把零零散散的babel插件组合起来，只要简单的引入一个babel预设。
每个预设都会有自己对应的配置项，具体可以查阅babel官网。</p>
</blockquote>
<p><br>目前官方的推荐的一些预设：</p>
<pre><code class="copyable">@babel/preset-env
@babel/preset-flow
@babel/preset-react
@babel/preset-typescript
...
<span class="copy-code-btn">复制代码</span></code></pre>
<p><br>注意：babel @7.0.0之后对标准阶段提案的一些预设都会废弃，比如以下预设不推荐使用了。</p>
<pre><code class="copyable">@babel/preset-stage-0
@babel/preset-stage-1
@babel/preset-stage-2
@babel/preset-stage-3
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-11">@babel/preset-env</h3>
<p>对ES2015和ES2016进行转换，并且处理polyfill。<br>
<br>preset-env有以下配置，具体可以访问官网查看。</p>
<pre><code class="copyable">targets
spec
loose
modules
debug
include
exclude
useBuiltIns
corejs
forceAllTransforms
configPath
ignoreBrowserslistConfig
shippedProposals
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-12">tagets</h4>
<p>指定适配游览器范围，如果设置了该参数，优先级会比<code>.browserslist</code> 或者 <code>package.json/browserslist</code>设置的高。如果不设置，则默认会获取 <code>.browserslist</code> 或者 <code>package.json/browserslist</code>指定的游览器适配范围。<br>但是在项目中，还是建议使用 <code>.browserslistrc</code>  或者 <code>package.json/browserslist</code>指定目标。<br></p>
<h4 data-id="heading-13">useBuiltIns</h4>
<p><code>"usage"</code> | <code>"entry"</code> | <code>false</code>, defaults to <code>false</code>.<br>这个配置参数主要的作用是明确如何处理polyfill。<br>
<br>**polyfill<br>先简单的了解一下 <code>polyfill</code> ，中文成为垫片，形象一点描述用一个个垫片铺平低端游览器的坑，使代码运行的和在高端游览器中一样。对ES2015+的一些语法进行转化适配（除了一些实验性的Js特性），比如一些新的内置对象和实例方法等（Promise、Array.from、Object.assign...）</p>
<blockquote>
<p>需要注意的是，@babel/polyfill在babel v7.4.0之后版本会被废弃，官方建议直接引入corejs，并且在options中指定corejs版本。</p>
</blockquote>
<p><code>@babel/polyfill</code>  其实就是由 <code>core-js/stable</code>  和 <code>regenerator-runtime/runtime</code>  组合而成。</p>
<ul>
<li><strong>core-js：</strong>@babel/polyfill的底层依赖库，为ES2015+的JS特性提供编译转化功能。</li>
<li>**regenerator-runtime : **专门为 <code>Generator</code> 函数提供编译转化功能，比如在项目中使用了async/await就需要引入这个插件。</li>
</ul>
<p><br>以下两种写法其实是一样，而且只能两种方式取一种，否则会报重复引入的报错。</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">import</span> <span class="hljs-string">"@babel/polyfill"</span>;
<span class="hljs-comment">// ====等同于====</span>
<span class="hljs-keyword">import</span> <span class="hljs-string">"core-js/stable"</span>;
<span class="hljs-keyword">import</span> <span class="hljs-string">"regenerator-runtime/runtime"</span>;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>但是由于polyfill的体积比较大，通常情况下我们不需要引入完成的polyfill，而且全部引入也会导致打包后体积变大。所以此处useBuiltIns就开始发挥作用。</p>
<p><code>useBuiltIns:usage</code><br>不需要在文件入口处引入polyfill，env会提供一个插件，根据每个文件的需求进行特殊引入垫片。<br>
<br>此时需要你在babel配置中指定corejs的版本的版本。</p>
<pre><code class="hljs language-javascript copyable" lang="javascript">&#123;
    <span class="hljs-string">"presets"</span>: [
        [
            <span class="hljs-string">"@babel/preset-env"</span>,
            &#123;
                <span class="hljs-string">"useBuiltIns"</span>: <span class="hljs-string">"usage"</span>,
                <span class="hljs-string">"corejs"</span>: <span class="hljs-number">3</span>
            &#125;
        ]
    ]
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>比如promise-a.js文件只使用到promise，就只会在该文件入口引入promise相关的垫片。<br> src/promise-a.js</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">// src/promise-a.js</span>
<span class="hljs-keyword">new</span> <span class="hljs-built_in">Promise</span>(<span class="hljs-function">(<span class="hljs-params">resolve</span>)=></span>&#123;
    <span class="hljs-built_in">console</span>.log(<span class="hljs-string">"promise A"</span>);
    resolve()
&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>lib/promise-a.js</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-meta">"use strict"</span>;

<span class="hljs-built_in">require</span>(<span class="hljs-string">"core-js/modules/es.object.to-string"</span>);

<span class="hljs-built_in">require</span>(<span class="hljs-string">"core-js/modules/es.promise"</span>);

<span class="hljs-keyword">new</span> <span class="hljs-built_in">Promise</span>(<span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params">resolve</span>) </span>&#123;
  <span class="hljs-built_in">console</span>.log(<span class="hljs-string">"promise A"</span>);
  resolve();
&#125;);
<span class="copy-code-btn">复制代码</span></code></pre>
<p><code>useBuiltIns: 'entry'</code><br>需要在文件入口处手动引入polyfill，然后根据当前的环境尽可能的引入需要的功能。<br>比如引入一个array相关的垫片。<br>src/entry.js</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">import</span> <span class="hljs-string">"core-js/es/array"</span>;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>lib/entry.js</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-meta">"use strict"</span>;
<span class="hljs-built_in">require</span>(<span class="hljs-string">"core-js/modules/es.array.concat"</span>);
<span class="hljs-built_in">require</span>(<span class="hljs-string">"core-js/modules/es.array.copy-within"</span>);
<span class="hljs-built_in">require</span>(<span class="hljs-string">"core-js/modules/es.array.every"</span>);
<span class="hljs-built_in">require</span>(<span class="hljs-string">"core-js/modules/es.array.fill"</span>);
<span class="hljs-built_in">require</span>(<span class="hljs-string">"core-js/modules/es.array.filter"</span>);
<span class="hljs-built_in">require</span>(<span class="hljs-string">"core-js/modules/es.array.find"</span>);
<span class="hljs-built_in">require</span>(<span class="hljs-string">"core-js/modules/es.array.find-index"</span>);
<span class="hljs-built_in">require</span>(<span class="hljs-string">"core-js/modules/es.array.flat"</span>);
<span class="hljs-built_in">require</span>(<span class="hljs-string">"core-js/modules/es.array.flat-map"</span>);
...
<span class="copy-code-btn">复制代码</span></code></pre>
<p><br><code>useBuiltIns: false</code><br>不为文件自动添加垫片，也不会对于自行引入的core-js或者@babel/polyfill有任何转化。</p>
<h4 data-id="heading-14">corejs</h4>
<p><code>2</code>, <code>3</code> or <code>&#123; version: 2 | 3, proposals: boolean &#125;</code>, defaults to <code>2</code>.<br>
<br>这个选项需要和useBuiltIns结合起来使用。当useBuiltIns: usage或者useBuiltIns: entry时才会起效。<br>core-js目前存在两个版本，分别是coreJs2和coreJs3。coreJs2目前已经不再更新，所以对于一些特别新的特性只会在coreJs3去更新。</p>
<p>如果使用coreJs3时只想注入稳定的ECMAScript功能，有以下两种方式：<br><code>1.对于useBuiltIns: usage</code> <br>corejs:  <code>&#123; version: 3, proposals: true &#125;<br /></code><br><code>2.对于useBuiltIns: entry</code><br>corejs配置为 <code>3</code> ，另外在项目引入<code>import "core-js/proposals/string-replace-all"</code></p>
<h2 data-id="heading-15">✍其他小知识点：</h2>
<p><strong><br>1.插件名称简写</strong></p>
<pre><code class="copyable">@babel/plugin-XXX 等同于 @babel/XXX
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>2.babel命名</strong><br>@7.0.0以上的包都是以@开头命名，用于区分6.x版本<br>
<br><strong>3.执行顺序</strong></p>
<ul>
<li>插件在 Presets 前运行。</li>
<li>插件顺序从前往后排列。</li>
<li>Preset 顺序是颠倒的（从后往前）。</li>
</ul>
<p><br>参考文档<br><a href="https://github.com/jamiebuilds/babel-handbook/blob/master/translations/zh-Hans/README.md" target="_blank" rel="nofollow noopener noreferrer">Babel用户手册</a><br></p></div> <div class="image-viewer-box" data-v-78c9b824><!----></div>  
</div>
            