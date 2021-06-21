
---
title: '写一个Babel插件'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/bdcfd63a338446d6a5c1aa6b00ec4cfc~tplv-k3u1fbpfcp-zoom-1.image'
author: 掘金
comments: false
date: Mon, 21 Jun 2021 00:34:42 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/bdcfd63a338446d6a5c1aa6b00ec4cfc~tplv-k3u1fbpfcp-zoom-1.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h2 data-id="heading-0">写一个Babel插件</h2>
<h3 data-id="heading-1">什么是Babel？</h3>
<p>来看一下官方解释：</p>
<blockquote>
<p>Babel 是一个 JavaScript 编译器。</p>
<p>Babel 是一个工具链，主要用于将采用 ECMAScript 2015+ 语法编写的代码转换为向后兼容的 JavaScript 语法，
以便能够运行在当前和旧版本的浏览器或其他环境中。</p>
</blockquote>
<blockquote>
<p>作为一种语言，JavaScript 在不断发展，新的标准／提案和新的特性层出不穷。 在得到广泛普及之前，Babel 能够让你提前（甚至数年）使用它们。</p>
</blockquote>
<h3 data-id="heading-2">Babel的原理是什么？</h3>
<p>一图胜千言</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/bdcfd63a338446d6a5c1aa6b00ec4cfc~tplv-k3u1fbpfcp-zoom-1.image" alt="在这里插入图片描述" loading="lazy" referrerpolicy="no-referrer"></p>
<p>可以看到Babel主要做了三件事：解析 parse 、转换 transform 、生成 generate 。</p>
<h4 data-id="heading-3">1. 解析 parse</h4>
<p>解析阶段的产物是 abstract syntax tree ，AST抽象语法树。</p>
<p>解析有词法分析和语法分析两个步骤。</p>
<ol>
<li>词法分析</li>
</ol>
<blockquote>
<p>词法分析（英语：lexical analysis）是计算机科学中将字符序列转换为标记（token）序列的过程。</p>
</blockquote>
<p>语法分析阶段，把字符串形式的代码转换为tokens，可以理解为一组标记数组。</p>
<p>词法分析类似于我们的分词过程，“我 想吃 火锅”，名词、动词、名词。</p>
<p>比如<code>sum = 2 + 3</code>，标识符、操作符、数字、操作符、数字。</p>
<pre><code class="hljs language-js copyable" lang="js">[
  &#123; <span class="hljs-attr">type</span>: &#123; ... &#125;, <span class="hljs-attr">value</span>: <span class="hljs-string">"sum"</span>, <span class="hljs-attr">start</span>: <span class="hljs-number">0</span>, <span class="hljs-attr">end</span>: <span class="hljs-number">2</span> &#125;,
  &#123; <span class="hljs-attr">type</span>: &#123; ... &#125;, <span class="hljs-attr">value</span>: <span class="hljs-string">"="</span>, <span class="hljs-attr">start</span>: <span class="hljs-number">3</span>, <span class="hljs-attr">end</span>: <span class="hljs-number">4</span> &#125;,
  &#123; <span class="hljs-attr">type</span>: &#123; ... &#125;, <span class="hljs-attr">value</span>: <span class="hljs-string">"2"</span>, <span class="hljs-attr">start</span>: <span class="hljs-number">4</span>, <span class="hljs-attr">end</span>: <span class="hljs-number">5</span> &#125;,
  ...
]
<span class="copy-code-btn">复制代码</span></code></pre>
<p><a href="https://en.wikipedia.org/wiki/Lexical_analysis" target="_blank" rel="nofollow noopener noreferrer">Lexical_analysis</a></p>
<p><a href="https://zh.wikipedia.org/wiki/%E8%AF%8D%E6%B3%95%E5%88%86%E6%9E%90" target="_blank" rel="nofollow noopener noreferrer">词法分析</a></p>
<ol start="2">
<li>语法分析</li>
</ol>
<blockquote>
<p>进行语法检查、并构建由输入的单词组成的数据结构</p>
</blockquote>
<p><a href="https://zh.wikipedia.org/wiki/%E8%AF%AD%E6%B3%95%E5%88%86%E6%9E%90" target="_blank" rel="nofollow noopener noreferrer">语法分析</a></p>
<p>简单点，说话的方式简单点，就是把 tokens 转换成 AST抽象语法树。</p>
<p><a href="https://astexplorer.net/" target="_blank" rel="nofollow noopener noreferrer">AST抽象语法树</a></p>
<h4 data-id="heading-4">2. 转换 transform</h4>
<p>转换阶段接收一棵AST抽象语法树，对其进行遍历，做一些添加节点、删除节点、修改节点的操作，并输出转换后的AST抽象语法树。</p>
<h4 data-id="heading-5">3. 生成 generate</h4>
<p>这一阶段也很好理解，接收转换好的AST抽象语法树，生成字符串形式的代码，并创建源码映射。</p>
<p><a href="https://www.html5rocks.com/en/tutorials/developertools/sourcemaps/" target="_blank" rel="nofollow noopener noreferrer">Introduction to JavaScript Source Maps</a></p>
<p><a href="http://www.ruanyifeng.com/blog/2013/01/javascript_source_map.html" target="_blank" rel="nofollow noopener noreferrer">JavaScript Source Map 详解</a></p>
<hr>
<blockquote>
<p>Babel 实际上是一组模块的集合。</p>
</blockquote>
<ul>
<li>
<p>babylon 是 Babel 的解析器。</p>
</li>
<li>
<p>babel-traverse（遍历）模块维护了整棵树的状态，并且负责替换、移除和添加节点。</p>
</li>
<li>
<p>babel-generator 模块是 Babel 的代码生成器，它读取AST并将其转换为代码和源码映射（sourcemaps）。</p>
</li>
<li>
<p>babel-types 模块是一个用于 AST 节点的 Lodash 式工具库，它包含了构造、验证以及变换 AST 节点的方法。</p>
</li>
</ul>
<h3 data-id="heading-6">Babel插件是做什么的？</h3>
<blockquote>
<p>Babel's code transformations are enabled by applying plugins (or presets) to your configuration file.</p>
</blockquote>
<p><a href="https://www.babeljs.cn/docs/plugins" target="_blank" rel="nofollow noopener noreferrer">Babel插件</a></p>
<p>插件是干什么的呢？</p>
<p>直译一下，Babel的代码转换得益于在配置文件中设置的插件和预设的应用。</p>
<h3 data-id="heading-7">Visitors（访问者）和 Paths（路径）</h3>
<p>开始写plugin之前，我们还需要了解一下如何访问语法树的节点，节点与节点之间又是怎样关联的。</p>
<h4 data-id="heading-8">Visitors（访问者）</h4>
<p><a href="https://www.jianshu.com/p/1f1049d0a0f4" target="_blank" rel="nofollow noopener noreferrer">访问者模式</a>是一种将数据操作和数据结构分离的设计模式。</p>
<p>简单的说，访问者就是一个对象，定义了用于在一个树状结构中获取具体节点的方法。</p>
<p>看一下官方例子：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> MyVisitor = &#123;
  <span class="hljs-function"><span class="hljs-title">Identifier</span>(<span class="hljs-params"></span>)</span> &#123;
    <span class="hljs-built_in">console</span>.log(<span class="hljs-string">"Called!"</span>);
  &#125;
&#125;;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这是一个简单的访问者，把它用于遍历中时，每当在树中遇见一个 Identifier 的时候会调用 Identifier() 方法。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">square</span>(<span class="hljs-params">n</span>) </span>&#123;
  <span class="hljs-keyword">return</span> n * n;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这段代码会触发几次"Called!"打印？</p>
<p>可以看一下这段代码解析出来的<a href="https://astexplorer.net/" target="_blank" rel="nofollow noopener noreferrer">AST抽象语法树</a>。</p>
<p>有四个Identifier，所以触发四次。</p>
<p>实际上，<code>Identifier() &#123; ... &#125;</code> 是 <code>Identifier: &#123; enter() &#123; ... &#125; &#125;</code> 的简写形式，一个访问者有两次机会访问节点：进入节点，退出节点。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> MyVisitor = &#123;
  <span class="hljs-string">"Identifier|FunctionDeclaration|BlockStatement|ReturnStatement|BinaryExpression"</span>: &#123;
        <span class="hljs-function"><span class="hljs-title">enter</span>(<span class="hljs-params">path</span>)</span> &#123;
            <span class="hljs-built_in">console</span>.log(<span class="hljs-string">"Entered!"</span>,path.node.type,path.node.name || <span class="hljs-string">''</span>);
        &#125;,
        <span class="hljs-function"><span class="hljs-title">exit</span>(<span class="hljs-params">path</span>)</span> &#123;
            <span class="hljs-built_in">console</span>.log(<span class="hljs-string">"Exited!"</span>,path.node.type,path.node.name || <span class="hljs-string">''</span>);
        &#125;
    &#125;
&#125;;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/6d2cb3dea6524b03ad48a991cc340647~tplv-k3u1fbpfcp-zoom-1.image" alt="在这里插入图片描述" loading="lazy" referrerpolicy="no-referrer"></p>
<blockquote>
<p>可以把方法名用"|"分割成"Idenfifier|MemberExpression"形式的字符串，把同一个函数应用到多种访问节点。</p>
</blockquote>
<h4 data-id="heading-9">Paths（路径）</h4>
<blockquote>
<p>Path 是表示两个节点之间连接的对象。</p>
</blockquote>
<p>当我们通过Visitor来访问节点时，实际访问当不是节点，而是路径。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> MyVisitor = &#123;
    <span class="hljs-string">"Identifier"</span>: &#123;
        <span class="hljs-function"><span class="hljs-title">enter</span>(<span class="hljs-params">path</span>)</span> &#123;
            <span class="hljs-keyword">if</span>(path.node.name === <span class="hljs-string">'a'</span>) <span class="hljs-built_in">console</span>.log(path);
        &#125;,
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>用上面这个访问者访问<code>var a = 1</code>的AST抽象语法树，我们可以看到此时的path：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/21e85b4c31b04cf49f9382783b321390~tplv-k3u1fbpfcp-zoom-1.image" alt="在这里插入图片描述" loading="lazy" referrerpolicy="no-referrer"></p>
<p>路径对象还包含添加、更新、移动和删除节点有关的其他很多方法。</p>
<hr>
<p>当然path中还有很多其他信息，有兴趣可以去了解一下</p>
<pre><code class="hljs language-js copyable" lang="js">&#123;
  <span class="hljs-string">"parent"</span>: &#123;...&#125;,
  <span class="hljs-string">"node"</span>: &#123;...&#125;,
  <span class="hljs-string">"hub"</span>: &#123;...&#125;,
  <span class="hljs-string">"contexts"</span>: [],
  <span class="hljs-string">"data"</span>: &#123;&#125;,
  <span class="hljs-string">"shouldSkip"</span>: <span class="hljs-literal">false</span>,
  <span class="hljs-string">"shouldStop"</span>: <span class="hljs-literal">false</span>,
  <span class="hljs-string">"removed"</span>: <span class="hljs-literal">false</span>,
  <span class="hljs-string">"state"</span>: <span class="hljs-literal">null</span>,
  <span class="hljs-string">"opts"</span>: <span class="hljs-literal">null</span>,
  <span class="hljs-string">"skipKeys"</span>: <span class="hljs-literal">null</span>,
  <span class="hljs-string">"parentPath"</span>: <span class="hljs-literal">null</span>,
  <span class="hljs-string">"context"</span>: <span class="hljs-literal">null</span>,
  <span class="hljs-string">"container"</span>: <span class="hljs-literal">null</span>,
  <span class="hljs-string">"listKey"</span>: <span class="hljs-literal">null</span>,
  <span class="hljs-string">"inList"</span>: <span class="hljs-literal">false</span>,
  <span class="hljs-string">"parentKey"</span>: <span class="hljs-literal">null</span>,
  <span class="hljs-string">"key"</span>: <span class="hljs-literal">null</span>,
  <span class="hljs-string">"scope"</span>: <span class="hljs-literal">null</span>,
  <span class="hljs-string">"type"</span>: <span class="hljs-literal">null</span>,
  <span class="hljs-string">"typeAnnotation"</span>: <span class="hljs-literal">null</span>
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-10">写一个Babel插件吧</h3>
<p>来写一个删除<code>console.log(...)</code>的插件吧。</p>
<p>plugin 是一个接收了当前babel对象作为参数的 function，我们先把<code>babel.types</code>取出来，我们将用到它的一些验证节点类型的方法。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-built_in">module</span>.exports = <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">&#123; types: t &#125;</span>) </span>&#123;
    <span class="hljs-keyword">return</span> &#123;
        <span class="hljs-attr">visitor</span>: &#123;
            <span class="hljs-comment">// ...</span>
        &#125;
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>来看看一条<code>console.log(...)</code>语句的<a href="https://astexplorer.net/" target="_blank" rel="nofollow noopener noreferrer">AST抽象语法树</a>吧。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/cb32d2975ec24ecebc7cd784f21052c3~tplv-k3u1fbpfcp-zoom-1.image" alt="在这里插入图片描述" loading="lazy" referrerpolicy="no-referrer"></p>
<p>然后就可以完成这个插件了！</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-title">CallExpression</span>(<span class="hljs-params">path, state</span>)</span> &#123;
    <span class="hljs-keyword">let</span> node = path.node.callee
    <span class="hljs-keyword">if</span>(t.isMemberExpression(node) 
        && t.isIdentifier(node.object) 
        && node.object.name === <span class="hljs-string">'console'</span> 
        && t.isIdentifier(node.property) 
        && node.property.name === <span class="hljs-string">'log'</span> )&#123;
            path.parentPath.remove();
    &#125;
&#125;,
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/a19917a7f7eb42c8b56970323de9c748~tplv-k3u1fbpfcp-zoom-1.image" alt="在这里插入图片描述" loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-11">一个小知识</h3>
<ol>
<li>插件的执行顺序是怎样的？</li>
</ol>
<p>插件顺序从前往后排列。</p>
<ol start="2">
<li>预设的执行顺序是怎样的？</li>
</ol>
<p>Preset 顺序是颠倒的（从后往前）。</p>
<ol start="3">
<li>插件和预设的执行顺序是怎样的？</li>
</ol>
<p>插件在 Presets 前运行。</p>
<h3 data-id="heading-12">相关文档</h3>
<p><a href="https://github.com/jamiebuilds/babel-handbook/blob/master/translations/zh-Hans/plugin-handbook.md#toc-introduction" target="_blank" rel="nofollow noopener noreferrer">Babel插件手册</a></p></div>  
</div>
            