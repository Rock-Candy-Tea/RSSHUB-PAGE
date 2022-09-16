
---
title: 'Babel 插件：30分钟从入门到实战'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/b9aafb0aa79444a49634ef2c02b66571~tplv-k3u1fbpfcp-zoom-in-crop-mark:4536:0:0:0.awebp'
author: 掘金
comments: false
date: Fri, 16 Sep 2022 02:24:37 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/b9aafb0aa79444a49634ef2c02b66571~tplv-k3u1fbpfcp-zoom-in-crop-mark:4536:0:0:0.awebp'
---

<div>   
<div class="markdown-body cache"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:16px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:24px;margin-bottom:5px&#125;.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;font-size:20px&#125;.markdown-body h2&#123;padding-bottom:12px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>Babel 是一个 source to source（源码到源码）的 JavaScript 编译器，简单来说，你为 Babel 提供一些 JavaScript 代码，Babel 可以更改这些代码，然后返回给你新生成的代码。Babel 主要用于将 ECMAScript 2015+ 代码转换为能够向后兼容的 JavaScript 版本。Babel 使用插件系统进行代码转换，因此任何人都可以为 babel 编写自己的转换插件，以支持实现广泛的功能。</p>
<h1 data-id="heading-0">Babel 编译流程</h1>
<p>Babel 的编译流程主要分为三个部分：解析（parse），转换（transform），生成（generate）。</p>
<pre><code class="hljs language-rust copyable" lang="rust">code <span class="hljs-punctuation">-></span> AST <span class="hljs-punctuation">-></span> transformed AST <span class="hljs-punctuation">-></span> transformed code
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li><strong>解析 Parse</strong></li>
</ul>
<p>将源码转换成抽象语法树（AST, Abstract Syntax Tree）。</p>
<p>比如：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">function</span> <span class="hljs-title function_">square</span>(<span class="hljs-params">n</span>) &#123;
  <span class="hljs-keyword">return</span> n * n;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>以上的程序可以被转换成类似这样的抽象语法树：</p>
<pre><code class="hljs language-less copyable" lang="less"><span class="hljs-selector-tag">-</span> <span class="hljs-selector-tag">FunctionDeclaration</span>:
  <span class="hljs-selector-tag">-</span> <span class="hljs-selector-tag">id</span>:
    <span class="hljs-selector-tag">-</span> <span class="hljs-selector-tag">Identifier</span>:
      <span class="hljs-selector-tag">-</span> <span class="hljs-selector-tag">name</span>: <span class="hljs-selector-tag">square</span>
  <span class="hljs-selector-tag">-</span> <span class="hljs-selector-tag">params</span> <span class="hljs-selector-attr">[1]</span>
    <span class="hljs-selector-tag">-</span> <span class="hljs-selector-tag">Identifier</span>
      <span class="hljs-selector-tag">-</span> <span class="hljs-selector-tag">name</span>: <span class="hljs-selector-tag">n</span>
  <span class="hljs-selector-tag">-</span> <span class="hljs-selector-tag">body</span>:
    <span class="hljs-selector-tag">-</span> <span class="hljs-selector-tag">BlockStatement</span>
      <span class="hljs-selector-tag">-</span> <span class="hljs-selector-tag">body</span> <span class="hljs-selector-attr">[1]</span>
        <span class="hljs-selector-tag">-</span> <span class="hljs-selector-tag">ReturnStatement</span>
          <span class="hljs-selector-tag">-</span> <span class="hljs-selector-tag">argument</span>
            <span class="hljs-selector-tag">-</span> <span class="hljs-selector-tag">BinaryExpression</span>
              <span class="hljs-selector-tag">-</span> <span class="hljs-selector-tag">operator</span>: *
              <span class="hljs-selector-tag">-</span> <span class="hljs-selector-tag">left</span>
                <span class="hljs-selector-tag">-</span> <span class="hljs-selector-tag">Identifier</span>
                  <span class="hljs-selector-tag">-</span> <span class="hljs-selector-tag">name</span>: <span class="hljs-selector-tag">n</span>
              <span class="hljs-selector-tag">-</span> <span class="hljs-selector-tag">right</span>
                <span class="hljs-selector-tag">-</span> <span class="hljs-selector-tag">Identifier</span>
                  <span class="hljs-selector-tag">-</span> <span class="hljs-selector-tag">name</span>: <span class="hljs-selector-tag">n</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li><strong>转换 Transform</strong></li>
</ul>
<p>转换阶段接受一个 AST 并遍历它，在遍历的过程中对树的节点进行增删改。这也是运行 Babel 插件的阶段。</p>
<ul>
<li><strong>生成 Generate</strong></li>
</ul>
<p>将经过一系列转换之后的 AST 转换成字符串形式的代码，同时还会创建 sourcemap。</p>
<h1 data-id="heading-1">你会用到的一些工具库</h1>
<p>对于每一个阶段，Babel 都提供了一些工具库：</p>
<ul>
<li>Parse 阶段可以使用 <strong>@babel/parser</strong> 将源码转换成 AST。</li>
<li>Transform 阶段可以使用  <strong>@babel/traverse</strong> 调用 visitor 函数遍历 AST，期间可以使用  <strong>@babel/types</strong> 创建 AST 和检查 AST 节点的类型，批量创建 AST 的场景下可以使用  <strong>@babel/template</strong> 中途还可以使用  <strong>@babel/code-frame</strong> 打印报错信息。</li>
<li>Generate 阶段可以使用  <strong>@babel/generator</strong> 根据 AST 生成代码字符串和 sourcemap。</li>
</ul>
<p>以上提及的包都是  <strong>@babel/core</strong> 的 dependencies，所以只需要安装 @babel/core 就能访问到它们。</p>
<p>除了上面提到的工具库，以下工具库也比较常用：</p>
<ul>
<li><strong>@babel/helper-plugin-utils</strong>：如果插件使用者的 Babel 版本没有您的插件所需的 API，它能给用户提供明确的错误信息。</li>
<li><strong>babel-plugin-tester</strong>：用于帮助测试 Babel 插件的实用工具，通常配合 jest 使用。</li>
</ul>
<p>本文不会深入讨论它们的详细用法，当你在编写插件的时候，可以根据功能需求找到它们，我们后文也会涉及到部分用法。</p>
<h1 data-id="heading-2">认识 Babel 插件</h1>
<p>接下来让我们开始认识 Babel 插件吧。</p>
<p>babel 插件是一个简单的函数，它必须返回一个匹配以下接口的对象。如果 Babel 发现未知属性，它将抛出错误。</p>
<p align="center"><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/b9aafb0aa79444a49634ef2c02b66571~tplv-k3u1fbpfcp-zoom-in-crop-mark:4536:0:0:0.awebp" alt="图片" loading="lazy" referrerpolicy="no-referrer"></p>
<p>以下是一个简单的插件示例：</p>
<pre><code class="hljs language-scss copyable" lang="scss">export default <span class="hljs-built_in">function</span>(api, options, dirname) &#123;
  return &#123;
    visitor: &#123;
      <span class="hljs-built_in">StringLiteral</span>(path, state) &#123;&#125;,
    &#125;
  &#125;;
&#125;;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>Babel 插件接受 3 个参数：</p>
<ul>
<li>api：一个对象，包含了 types (@babel/types)、traverse (@babel/traverse)、template(@babel/template) 等实用方法，我们能从这个对象中访问到 @babel/core dependecies 中包含的方法。</li>
</ul>

<ul>
<li>options：插件参数。</li>
</ul>

<ul>
<li>dirname：目录名。</li>
</ul>
<p>返回的对象有 name、manipulateOptions、pre、visitor、post、inherits 等属性：</p>
<ul>
<li>name：插件名字。</li>
</ul>

<ul>
<li>inherits：指定继承某个插件，通过 Object.assign 的方式，和当前插件的 options 合并。</li>
</ul>

<ul>
<li>visitor：指定 traverse 时调用的函数。</li>
</ul>

<ul>
<li>pre 和 post 分别在遍历前后调用，可以做一些插件调用前后的逻辑，比如可以往 file（表示文件的对象，在插件里面通过 state.file 拿到）中放一些东西，在遍历的过程中取出来。</li>
</ul>

<ul>
<li>manipulateOptions：用于修改 options，是在插件里面修改配置的方式。</li>
</ul>
<p>我们上面提到了一些陌生的概念：visitor、path、state，现在让我们一起来认识它们：</p>
<ul>
<li><strong>visitor 访问者</strong></li>
</ul>
<p>这个名字来源于设计模式中的<strong>访问者模式</strong>（<a href="https://link.juejin.cn/?target=https%3A%2F%2Fen.wikipedia.org%2Fwiki%2FVisitor_pattern%25EF%25BC%2589" target="_blank" rel="nofollow noopener noreferrer" title="https://en.wikipedia.org/wiki/Visitor_pattern%EF%BC%89" ref="nofollow noopener noreferrer">en.wikipedia.org/wiki/Visito…</a> 简单的说它就是一个对象，指定了在遍历 AST 过程中，访问指定节点时应该被调用的方法。</p>
<ul>
<li>
<p>假如我们有这样一段程序：</p>
<pre><code class="hljs language-csharp copyable" lang="csharp">    <span class="hljs-function">function <span class="hljs-title">foo</span>()</span> &#123;
      <span class="hljs-keyword">return</span> <span class="hljs-string">'string'</span>
    &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
<li>
<p>这段代码对应的 AST 如下：</p>
<pre><code class="hljs language-css copyable" lang="css">     - Program
       - FunctionDeclaration (<span class="hljs-selector-tag">body</span><span class="hljs-selector-attr">[0]</span>)
         - Identifier (id)
         - BlockStatement (<span class="hljs-selector-tag">body</span>)
           - ReturnStatement (<span class="hljs-selector-tag">body</span><span class="hljs-selector-attr">[0]</span>)
           - StringLiteral (arugument)
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
<li>
<p>当我们对这颗 AST 进行深度优先遍历时，每次访问 StringLiteral 都会调用 visitor.StringLiteral。</p>
</li>
</ul>
<p>当 visitor.StringLiteral 是一个函数时，它将在向下遍历的过程中被调用（即进入阶段）。当 visitor.StringLiteral 是一个对象时（<code>&#123; enter(path, state) &#123;&#125;, exit(path, state) &#123;&#125; &#125;</code>），visitor.StringLiteral.enter 将在向下遍历的过程中被调用（进入阶段），visitor.StringLiteral.exit 将在向上遍历的过程中被调用（退出阶段）。</p>
<ul>
<li><strong>Path 路径</strong></li>
</ul>
<p>Path 用于表示两个节点之间连接的对象，这是一个可操作和访问的巨大可变对象。</p>
<p>Path 之间的关系如图所示：</p>
<p align="center"><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/974a5040d4634f4ea1f44bc0d0563ec0~tplv-k3u1fbpfcp-zoom-in-crop-mark:4536:0:0:0.awebp" alt="图片" loading="lazy" referrerpolicy="no-referrer"></p>
<p>除了能在 Path 对象上访问到当前 AST 节点、父级 AST 节点、父级 Path 对象，还能访问到添加、更新、移动和删除节点等其他方法，这些方法提高了我们对 AST 增删改的效率。</p>
<ul>
<li><strong>State 状态</strong></li>
</ul>
<p>在实际编写插件的过程中，某一类型节点的处理可能需要依赖其他类型节点的处理结果，但由于 visitor 属性之间互不关联，因此需要 state 帮助我们在不同的 visitor 之间传递状态。</p>
<p>一种处理方式是使用递归，并将状态往下层传递：</p>
<pre><code class="hljs language-scss copyable" lang="scss">const anotherVisitor = &#123;
  <span class="hljs-built_in">Identifier</span>(path) &#123;
    console<span class="hljs-selector-class">.log</span>(this.someParam) <span class="hljs-comment">// => 'xxx'</span>
  &#125;
&#125;;

const MyVisitor = &#123;
  <span class="hljs-built_in">FunctionDeclaration</span>(path, state) &#123;
    <span class="hljs-comment">// state.cwd: 当前执行目录</span>
    <span class="hljs-comment">// state.opts: 插件 options</span>
    <span class="hljs-comment">// state.filename: 当前文件名(绝对路径)</span>
    <span class="hljs-comment">// state.file: BabelFile 对象，包含当前整个 ast，当前文件内容 code，etc.</span>
    <span class="hljs-comment">// state.key: 当前插件名字</span>
    path<span class="hljs-selector-class">.traverse</span>(anotherVisitor, &#123; someParam: 'xxx' &#125;);
  &#125;
&#125;;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>另外一种传递状态的办法是将状态直接设置到 this 上，Babel 会给 visitor 上的每个方法绑定 this。在 Babel 插件中，this 通常会被用于传递状态：从 pre 到 visitor 再到 post。</p>
<pre><code class="hljs language-javascript copyable" lang="javascript">   <span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> <span class="hljs-keyword">function</span>(<span class="hljs-params">&#123; types: t &#125;</span>) &#123;
     <span class="hljs-keyword">return</span> &#123;
       <span class="hljs-title function_">pre</span>(<span class="hljs-params">state</span>) &#123;
         <span class="hljs-variable language_">this</span>.<span class="hljs-property">cache</span> = <span class="hljs-keyword">new</span> <span class="hljs-title class_">Map</span>();
       &#125;,
       <span class="hljs-attr">visitor</span>: &#123;
         <span class="hljs-title class_">StringLiteral</span>(path) &#123;
           <span class="hljs-variable language_">this</span>.<span class="hljs-property">cache</span>.<span class="hljs-title function_">set</span>(path.<span class="hljs-property">node</span>.<span class="hljs-property">value</span>, <span class="hljs-number">1</span>);
         &#125;
       &#125;,
       <span class="hljs-title function_">post</span>(<span class="hljs-params">state</span>) &#123;
         <span class="hljs-variable language_">console</span>.<span class="hljs-title function_">log</span>(<span class="hljs-variable language_">this</span>.<span class="hljs-property">cache</span>);
       &#125;
     &#125;;
   &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h1 data-id="heading-3">常用的 API</h1>
<p>Babel 没有完整的文档讲解所有的 api，因此下面会列举一些可能还算常用的 api（并不是所有，主要是 path 和 types 上的方法或属性），我们并不需要全部背下来，在你需要用的时候，能找到对应的方法即可。</p>
<p>你可以通过 babel 的 typescript 类型定义找到以下列举的属性和方法，还可以通过 <strong>Babel Handbook</strong> 找到它们的具体使用方法。</p>
<blockquote>
<p>Babel Handbook：<a href="https://link.juejin.cn/?target=https%3A%2F%2Fastexplorer.net%2F" target="_blank" rel="nofollow noopener noreferrer" title="https://astexplorer.net/" ref="nofollow noopener noreferrer">astexplorer.net/</a></p>
</blockquote>
<ul>
<li>查询</li>
<li>
<ul>
<li>path.node：访问当前节点</li>
<li>path.get()：获取属性内部的 path</li>
<li>path.inList：判断路径是否有同级节点</li>
<li>path.key：获取路径所在容器的索引</li>
<li>path.container：获取路径的容器（包含所有同级节点的数组）</li>
<li>path.listKey：获取容器的key</li>
<li>path.getSibling()：获得同级路径</li>
<li>path.findParent()：对于每一个父路径调用 callback 并将其 NodePath 当作参数，当 callback 返回真值时，则将其 NodePath 返回</li>
<li>path.find()：与 path.findParent 的区别是，该方法会遍历当前节点</li>
</ul>
</li>
<li>遍历</li>
<li>
<ul>
<li>path.stop()：跳过遍历当前路径的子路径</li>
<li>path.skip()：完全停止遍历</li>
</ul>
</li>
<li>判断</li>
<li>
<ul>
<li>types.isXxx()：检查节点的类型，如 types.isStringLiteral(path.node)</li>
<li>path.isReferencedIdentifier()：检查标识符（Identifier）是否被引用</li>
</ul>
</li>
<li>增删改</li>
<li>
<ul>
<li>path.replaceWith()：替换单个节点</li>
<li>path.replaceWithMultiple()：用多节点替换单节点</li>
<li>path.replaceWithSourceString()：用字符串源码替换节点</li>
<li>path.insertBefore() / path.insertAfter()：插入兄弟节点</li>
<li>path.get('listKey').unshiftContainer() / path.get('listKey').pushContainer()：插入一个节点到数组中，如 body</li>
<li>path.remove()：删除一个节点</li>
</ul>
</li>
<li>作用域</li>
<li>
<ul>
<li>path.scope.hasBinding(): 从当前作用域开始向上查找变量</li>
<li>path.scope.hasOwnBinding()：仅在当前作用域中查找变量</li>
<li>path.scope.generateUidIdentifier()：生成一个唯一的标识符，不会与任何本地定义的变量相冲突</li>
<li>path.scope.generateUidIdentifierBasedOnNode()：基于某个节点创建唯一的标识符</li>
<li>path.scope.rename()：重命名绑定及其引用</li>
</ul>
</li>
</ul>
<h1 data-id="heading-4">AST Explorer</h1>
<p>在 @babel/types 的类型定义中，可以找到所有 AST 节点类型。我们不需要记住所有节点类型，社区内有一个 AST 可视化工具能够帮助我们分析 AST：axtexplorer.net。</p>
<p>在这个网站的左侧，可以输入我们想要分析的代码，在右侧会自动生成对应的 AST。当我们在左侧代码区域点击某一个节点，比如函数名 foo，右侧 AST 会自动跳转到对应的 Identifier AST 节点，并高亮展示。</p>
<p align="center"><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/91c05e3745a745d497e6f08ef2daa1b2~tplv-k3u1fbpfcp-zoom-in-crop-mark:4536:0:0:0.awebp" alt="图片" loading="lazy" referrerpolicy="no-referrer">我们还可以修改要 parse 的语言、使用的 parser、parser 参数等。</p>
<h1 data-id="heading-5">自己实现一个插件吧</h1>
<p>现在让我们来实现一个简单的插件吧！以下是插件需要实现的功能：</p>
<ol>
<li>将代码里重复的字符串字面量(StringLiteral)提升到顶层作用域。</li>
</ol>

<ol start="2">
<li>接受一个参数 minCount，它是 number 类型，如果某个字符串字面量重复次数大于等于 minCount 的值，则将它提升到顶层作用域，否则不做任何处理。</li>
</ol>
<p>因此，对于以下输入：</p>
<pre><code class="hljs language-ini copyable" lang="ini">const <span class="hljs-attr">s1</span> = <span class="hljs-string">"foo"</span><span class="hljs-comment">;</span>
const <span class="hljs-attr">s2</span> = <span class="hljs-string">"foo"</span><span class="hljs-comment">;</span>

const <span class="hljs-attr">s3</span> = <span class="hljs-string">"bar"</span><span class="hljs-comment">;</span>

function f1() &#123;
  const <span class="hljs-attr">s4</span> = <span class="hljs-string">"baz"</span><span class="hljs-comment">;</span>
  if (true) &#123;
    const <span class="hljs-attr">s5</span> = <span class="hljs-string">"baz"</span><span class="hljs-comment">;</span>
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>应该输出以下代码：</p>
<pre><code class="hljs language-ini copyable" lang="ini">var <span class="hljs-attr">_foo</span> = <span class="hljs-string">"foo"</span>,
  <span class="hljs-attr">_baz</span> = <span class="hljs-string">"baz"</span><span class="hljs-comment">;</span>
const <span class="hljs-attr">s1</span> = _foo<span class="hljs-comment">;</span>
const <span class="hljs-attr">s2</span> = _foo<span class="hljs-comment">;</span>
const <span class="hljs-attr">s3</span> = <span class="hljs-string">"bar"</span><span class="hljs-comment">;</span>

function f1() &#123;
  const <span class="hljs-attr">s4</span> = _baz<span class="hljs-comment">;</span>

  if (true) &#123;
    const <span class="hljs-attr">s5</span> = _baz<span class="hljs-comment">;</span>
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>通过 <a href="https://link.juejin.cn/?target=https%3A%2F%2Fastexplorer.net%2F%25EF%25BC%258C%25E6%2588%2591%25E4%25BB%25AC%25E5%258F%2591%25E7%258E%25B0%25E4%25BB%25A3%25E7%25A0%2581%25E9%2587%258C%25E7%259A%2584%25E5%25AD%2597%25E7%25AC%25A6%25E4%25B8%25B2%25E5%259C%25A8" target="_blank" rel="nofollow noopener noreferrer" title="https://astexplorer.net/%EF%BC%8C%E6%88%91%E4%BB%AC%E5%8F%91%E7%8E%B0%E4%BB%A3%E7%A0%81%E9%87%8C%E7%9A%84%E5%AD%97%E7%AC%A6%E4%B8%B2%E5%9C%A8" ref="nofollow noopener noreferrer">astexplorer.net/，我们发现代码里的字符…</a> AST 上对应的节点叫做 StringLiteral，如果想要拿到代码里所有的字符串并且统计每种字符串的数量，就需要遍历 StringLiteral 节点。</p>
<p align="center"><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/a27259194891448db7100044ec91d543~tplv-k3u1fbpfcp-zoom-in-crop-mark:4536:0:0:0.awebp" alt="图片" width="70%" loading="lazy" referrerpolicy="no-referrer"></p>
<p>我们需要一个对象用于存储所有 StringLiteral，key 是 StringLiteral 节点的 value 属性值，value 是一个数组，用于存储拥有相同 path.node.value 的所有 path 对象，最后把这个对象存到 state 对象上，以便于在遍历结束时能统计相同字符串的重复次数，从而可以判断哪些节点需要被替换为一个标识符。</p>
<pre><code class="hljs language-ini copyable" lang="ini">export default function() &#123;
  return &#123;
    visitor: &#123;
      StringLiteral(path, state) &#123;
        <span class="hljs-attr">state.stringPathMap</span> = state.stringPathMap || &#123;&#125;<span class="hljs-comment">;</span>
        const <span class="hljs-attr">nodes</span> = state.stringPathMap[path.node.value] || []<span class="hljs-comment">;</span>
        nodes.push(path)<span class="hljs-comment">;</span>
        state.stringPathMap<span class="hljs-section">[path.node.value]</span> = nodes<span class="hljs-comment">;</span>
      &#125;
    &#125;
  &#125;<span class="hljs-comment">;</span>
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>通过 <a href="https://link.juejin.cn/?target=https%3A%2F%2Fastexplorer.net%2F" target="_blank" rel="nofollow noopener noreferrer" title="https://astexplorer.net/" ref="nofollow noopener noreferrer">astexplorer.net/</a>  我们发现如果想要往顶层作用域中插入一个变量，其实就是往 Program 节点的 body 上插入 AST 节点。Program 节点也是 AST 的顶层节点，在遍历过程的退出阶段，Program 节点是最后一个被处理的，因此我们需要做的事情是：根据收集到的字符串字面量，分别创建一个位于顶层作用域的变量，并将它们统一插入到 Program 的 body 中，同时将代码中的字符串替换为对应的变量。</p>
<p align="center"><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/69130b7230354bc5ad667df5e2c226fc~tplv-k3u1fbpfcp-zoom-in-crop-mark:4536:0:0:0.awebp" alt="图片" width="70%" loading="lazy" referrerpolicy="no-referrer"></p>
<pre><code class="hljs language-scss copyable" lang="scss">export default <span class="hljs-built_in">function</span>() &#123;
  return &#123;
    visitor: &#123;
      <span class="hljs-built_in">StringLiteral</span>(path, state) &#123; <span class="hljs-comment">/** ... */</span> &#125;,
      Program: &#123;
        <span class="hljs-built_in">exit</span>(path, state) &#123;
          const &#123; minCount = <span class="hljs-number">2</span> &#125; = state<span class="hljs-selector-class">.opts</span> || &#123;&#125;;
      
          for (const [string, paths] of Object.entries(state.stringPathMap || &#123;&#125;)) &#123;
            if (paths.length < minCount) &#123;
              continue;
            &#125;
      
            const id = path<span class="hljs-selector-class">.scope</span><span class="hljs-selector-class">.generateUidIdentifier</span>(string);
      
            paths<span class="hljs-selector-class">.forEach</span>(p => &#123;
              p.replaceWith(id);
            &#125;);
      
            path<span class="hljs-selector-class">.scope</span><span class="hljs-selector-class">.push</span>(&#123; id, init: types.stringLiteral(string) &#125;);
          &#125;
        &#125;,
      &#125;,
    &#125;
  &#125;;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h1 data-id="heading-6">完整代码</h1>
<pre><code class="hljs language-typescript copyable" lang="typescript"><span class="hljs-keyword">import</span> &#123; <span class="hljs-title class_">PluginPass</span>, <span class="hljs-title class_">NodePath</span> &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'@babel/core'</span>;
<span class="hljs-keyword">import</span> &#123; <span class="hljs-keyword">declare</span> &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'@babel/helper-plugin-utils'</span>;

<span class="hljs-keyword">interface</span> <span class="hljs-title class_">Options</span> &#123;
  <span class="hljs-comment">/**
   * 当字符串字面量的重复次数大于或小于 minCount，将会被提升到顶层作用域
   */</span>
  minCount?: <span class="hljs-built_in">number</span>;
&#125;

<span class="hljs-keyword">type</span> <span class="hljs-title class_">State</span> = <span class="hljs-title class_">PluginPass</span> & &#123;
  <span class="hljs-comment">// 以 StringLiteral 节点的 value 属性值为 key，存放所有 StringLiteral 的 Path 对象</span>
  stringPathMap?: <span class="hljs-title class_">Record</span><<span class="hljs-built_in">string</span>, <span class="hljs-title class_">NodePath</span>[]>;
&#125;;

<span class="hljs-keyword">const</span> <span class="hljs-title class_">HoistCommonString</span> = <span class="hljs-keyword">declare</span><<span class="hljs-title class_">Options</span>>(<span class="hljs-function">(<span class="hljs-params">&#123; assertVersion, types &#125;, options</span>) =></span> &#123;
  <span class="hljs-comment">// 判断当前 Babel 版本是否为 7</span>
  <span class="hljs-title function_">assertVersion</span>(<span class="hljs-number">7</span>);

  <span class="hljs-keyword">return</span> &#123;
    <span class="hljs-comment">// 插件名字</span>
    <span class="hljs-attr">name</span>: <span class="hljs-string">'hoist-common-string'</span>,

    <span class="hljs-attr">visitor</span>: &#123;
      <span class="hljs-title class_">StringLiteral</span>(path, <span class="hljs-attr">state</span>: <span class="hljs-title class_">State</span>) &#123;
        <span class="hljs-comment">// 将所有 StringLiteral 节点对应的 path 对象收集起来，存到 state 对象里，</span>
        <span class="hljs-comment">// 以便于在遍历结束时能统计相同字符串的重复次数</span>
        state.<span class="hljs-property">stringPathMap</span> = state.<span class="hljs-property">stringPathMap</span> || &#123;&#125;;

        <span class="hljs-keyword">const</span> nodes = state.<span class="hljs-property">stringPathMap</span>[path.<span class="hljs-property">node</span>.<span class="hljs-property">value</span>] || [];
        nodes.<span class="hljs-title function_">push</span>(path);

        state.<span class="hljs-property">stringPathMap</span>[path.<span class="hljs-property">node</span>.<span class="hljs-property">value</span>] = nodes;
      &#125;,

      <span class="hljs-title class_">Program</span>: &#123;
        <span class="hljs-comment">// 将在遍历过程的退出阶段被调用</span>
        <span class="hljs-comment">// Program 节点是顶层 AST 节点，可以认为 Program.exit 是最后一个执行的 visitor 函数</span>
        <span class="hljs-title function_">exit</span>(<span class="hljs-params">path, state: State</span>) &#123;
          <span class="hljs-comment">// 插件参数。还可以通过 state.opts 拿到插件参数</span>
          <span class="hljs-keyword">const</span> &#123; minCount = <span class="hljs-number">2</span> &#125; = options || &#123;&#125;;

          <span class="hljs-keyword">for</span> (<span class="hljs-keyword">const</span> [<span class="hljs-built_in">string</span>, paths] <span class="hljs-keyword">of</span> <span class="hljs-title class_">Object</span>.<span class="hljs-title function_">entries</span>(state.<span class="hljs-property">stringPathMap</span> || &#123;&#125;)) &#123;
            <span class="hljs-comment">// 对于重复次数少于 minCount 的 Path，不做处理</span>
            <span class="hljs-keyword">if</span> (paths.<span class="hljs-property">length</span> < minCount) &#123;
              <span class="hljs-keyword">continue</span>;
            &#125;

            <span class="hljs-comment">// 基于给定的字符串创建一个唯一的标识符</span>
            <span class="hljs-keyword">const</span> id = path.<span class="hljs-property">scope</span>.<span class="hljs-title function_">generateUidIdentifier</span>(<span class="hljs-built_in">string</span>);

            <span class="hljs-comment">// 将所有相同的字符串字面量替换为上面生成的标识符</span>
            paths.<span class="hljs-title function_">forEach</span>(<span class="hljs-function"><span class="hljs-params">p</span> =></span> &#123;
              p.<span class="hljs-title function_">replaceWith</span>(id);
            &#125;);

            <span class="hljs-comment">// 将标识符添加到顶层作用域中</span>
            path.<span class="hljs-property">scope</span>.<span class="hljs-title function_">push</span>(&#123; id, <span class="hljs-attr">init</span>: types.<span class="hljs-title function_">stringLiteral</span>(<span class="hljs-built_in">string</span>) &#125;);
          &#125;
        &#125;,
      &#125;,
    &#125;,
  &#125;;
&#125;);
<span class="copy-code-btn">复制代码</span></code></pre>
<h1 data-id="heading-7">测试插件</h1>
<p>测试 Babel 插件有三种常用的方法：</p>
<ul>
<li>测试转换后的 AST 结果，检查是否符合预期</li>
</ul>

<ul>
<li>测试转换后的代码字符串，检查是否符合预期（通常使用快照测试）</li>
</ul>

<ul>
<li>执行转换后的代码，检查执行结果是否符合预期</li>
</ul>
<p>我们一般使用第二种方法，配合 <strong>babel-plugin-tester</strong> 可以很好地帮助我们完成测试工作。配合 babel-plugin-tester，我们可以对比输入输出的字符串、文件、快照。</p>
<pre><code class="hljs language-php copyable" lang="php">import pluginTester <span class="hljs-keyword">from</span> <span class="hljs-string">'babel-plugin-tester'</span>;
import xxxPlugin <span class="hljs-keyword">from</span> <span class="hljs-string">'./xxxPlugin'</span>;

<span class="hljs-title function_ invoke__">pluginTester</span>(&#123;
<span class="hljs-attr">  plugin</span>: xxxPlugin,
<span class="hljs-attr">  fixtures</span>: path.<span class="hljs-title function_ invoke__">join</span>(__dirname, <span class="hljs-string">'__fixtures__'</span>),
<span class="hljs-attr">  tests</span>: &#123;
    // <span class="hljs-number">1</span>. 对比转换前后的字符串
    // <span class="hljs-number">1.1</span> 输入输出完全一致时，可以简写
    <span class="hljs-string">'does not change code with no identifiers'</span>: <span class="hljs-string">'"hello";'</span>,
    // <span class="hljs-number">1.2</span> 输入输出不一致
    <span class="hljs-string">'changes this code'</span>: &#123;
<span class="hljs-attr">      code</span>: <span class="hljs-string">'var hello = "hi";'</span>,
<span class="hljs-attr">      output</span>: <span class="hljs-string">'var olleh = "hi";'</span>,
    &#125;,
    // <span class="hljs-number">2</span>. 对比转换前后的文件
    <span class="hljs-string">'using fixtures files'</span>: &#123;
<span class="hljs-attr">      fixture</span>: <span class="hljs-string">'changed.js'</span>,
<span class="hljs-attr">      outputFixture</span>: <span class="hljs-string">'changed-output.js'</span>,
    &#125;,
    // <span class="hljs-number">3</span>. 与上一次生成的快照做对比
    <span class="hljs-string">'using jest snapshots'</span>: &#123;
<span class="hljs-attr">      code</span>: `
        function<span class="hljs-title function_ invoke__"> sayHi</span>(person) &#123;
          <span class="hljs-keyword">return</span> <span class="hljs-string">'Hello '</span> + person + <span class="hljs-string">'!'</span>
        &#125;
      `,
<span class="hljs-attr">      snapshot</span>: <span class="hljs-literal">true</span>,
    &#125;,
  &#125;,
&#125;);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>本文将以快照测试为例，以下是测试我们插件的示例代码：</p>
<pre><code class="hljs language-csharp copyable" lang="csharp">import pluginTester <span class="hljs-keyword">from</span> <span class="hljs-string">'babel-plugin-tester'</span>;
import HoistCommonString <span class="hljs-keyword">from</span> <span class="hljs-string">'../index'</span>;

pluginTester(&#123;
  <span class="hljs-comment">// 插件</span>
  plugin: HoistCommonString,
  <span class="hljs-comment">// 插件名，可选</span>
  pluginName: <span class="hljs-string">'hoist-common-string'</span>,
  <span class="hljs-comment">// 插件参数，可选</span>
  pluginOptions: &#123;
    minCount: <span class="hljs-number">2</span>,
  &#125;,
  tests: &#123;
    <span class="hljs-string">'using jest snapshots'</span>: &#123;
      <span class="hljs-comment">// 输入</span>
      code: `<span class="hljs-keyword">const</span> s1 = <span class="hljs-string">"foo"</span>;
      <span class="hljs-keyword">const</span> s2 = <span class="hljs-string">"foo"</span>;

      <span class="hljs-keyword">const</span> s3 = <span class="hljs-string">"bar"</span>;

      <span class="hljs-function">function <span class="hljs-title">f1</span>()</span> &#123;
        <span class="hljs-keyword">const</span> s4 = <span class="hljs-string">"baz"</span>;
        <span class="hljs-keyword">if</span> (<span class="hljs-literal">true</span>) &#123;
          <span class="hljs-keyword">const</span> s5 = <span class="hljs-string">"baz"</span>;
        &#125;
      &#125;`,
      <span class="hljs-comment">// 使用快照测试</span>
      snapshot: <span class="hljs-literal">true</span>,
    &#125;,
  &#125;,
&#125;);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>当我们运行 jest 后（更多关于 jest 的介绍，可以查看 <strong>jest 官方文档</strong><a href="https://link.juejin.cn/?target=https%3A%2F%2Fjestjs.io%2Fdocs%2Fgetting-started%25EF%25BC%2589" target="_blank" rel="nofollow noopener noreferrer" title="https://jestjs.io/docs/getting-started%EF%BC%89" ref="nofollow noopener noreferrer">jestjs.io/docs/gettin…</a> 会生成一个 snapshots 目录：</p>
<p align="center"><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/5b9b20f304fb489984a5097deacffccd~tplv-k3u1fbpfcp-zoom-in-crop-mark:4536:0:0:0.awebp" alt="图片" width="50%" loading="lazy" referrerpolicy="no-referrer"></p>
<p>有了快照以后，每次迭代插件都可以跑一下单测以快速检查功能是否正常。快照的更新也很简单，只需要执行 <code>jest --updateSnapshot</code>。</p>
<h1 data-id="heading-8">使用插件</h1>
<p>如果想要使用 Babel 插件，需要在配置文件里添加 plugins 选项，plugins 选项接受一个数组，值为字符串或者数组。以下是一些例子：</p>
<pre><code class="hljs language-json copyable" lang="json"><span class="hljs-comment">// .babelrc</span>
<span class="hljs-punctuation">&#123;</span>
    <span class="hljs-attr">"plugins"</span><span class="hljs-punctuation">:</span> <span class="hljs-punctuation">[</span>
        <span class="hljs-string">"babel-plugin-myPlugin1"</span><span class="hljs-punctuation">,</span>
        <span class="hljs-punctuation">[</span><span class="hljs-string">"babel-plugin-myPlugin2"</span><span class="hljs-punctuation">]</span><span class="hljs-punctuation">,</span>
        <span class="hljs-punctuation">[</span><span class="hljs-string">"babel-plugin-myPlugin3"</span><span class="hljs-punctuation">,</span> <span class="hljs-punctuation">&#123;</span> <span class="hljs-comment">/** 插件 options */</span> <span class="hljs-punctuation">&#125;</span><span class="hljs-punctuation">]</span><span class="hljs-punctuation">,</span>
        <span class="hljs-string">"./node_modules/asdf/plugin"</span>
    <span class="hljs-punctuation">]</span>
<span class="hljs-punctuation">&#125;</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>Babel 对插件名字的格式有一定的要求，比如最好包含 babel-plugin，如果不包含的话也会自动补充。以下是 Babel 插件名字的自动补全规则：</p>
<p align="center"><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/5624334ef75b4438aed3dfec6da0b0a9~tplv-k3u1fbpfcp-zoom-in-crop-mark:4536:0:0:0.awebp" alt="图片" width="70%" loading="lazy" referrerpolicy="no-referrer"></p>
<p>到这里，Babel 插件的学习就告一段落了，如果大家想继续深入学习 Babel 插件，可以访问 <strong>Babel 的仓库</strong>（<a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fbabel%2Fbabel%2Ftree%2Fmain%2Fpackages%25EF%25BC%2589" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/babel/babel/tree/main/packages%EF%BC%89" ref="nofollow noopener noreferrer">github.com/babel/babel…</a> 这是一个 monorepo，里面包含了很多真实的插件，通过阅读这些插件，相信你一定能对 Babel 插件有更深入的理解！</p>
<h1 data-id="heading-9">参考文档</h1>
<p><strong>Babel plugin handbook</strong>：<a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fjamiebuilds%2Fbabel-handbook%2Fblob%2Fmaster%2Ftranslations%2Fen%2Fplugin-handbook.md" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/jamiebuilds/babel-handbook/blob/master/translations/en/plugin-handbook.md" ref="nofollow noopener noreferrer">github.com/jamiebuilds…</a></p>
<p><strong>Babel 官方文档</strong>：<a href="https://link.juejin.cn/?target=https%3A%2F%2Fbabeljs.io%2Fdocs%2Fen%2F" target="_blank" rel="nofollow noopener noreferrer" title="https://babeljs.io/docs/en/" ref="nofollow noopener noreferrer">babeljs.io/docs/en/</a></p>
<p><strong>Babel 插件通关秘籍</strong>：<a href="https://juejin.cn/book/6946117847848321055" target="_blank" title="https://juejin.cn/book/6946117847848321055">juejin.cn/book/694611…</a></p>
<h1 data-id="heading-10">🙋 <strong>加入我们</strong></h1>
<p>我们来自字节跳动飞书商业应用研发部(Lark Business Applications)，目前我们在北京、深圳、上海、武汉、杭州、成都、广州、三亚都设立了办公区域。我们关注的产品领域主要在企业经验管理软件上，包括飞书 OKR、飞书绩效、飞书招聘、飞书人事等 HCM 领域系统，也包括飞书审批、OA、法务、财务、采购、差旅与报销等系统。欢迎各位加入我们。</p>
<p>扫码发现职位&投递简历</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/eec2e60f24874cbe8dbd974682781bd5~tplv-k3u1fbpfcp-zoom-in-crop-mark:4536:0:0:0.awebp" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>官网投递：<a href="https://link.juejin.cn/?target=https%3A%2F%2Fjob.toutiao.com%2Fs%2FFyL7DRg" target="_blank" rel="nofollow noopener noreferrer" title="https://job.toutiao.com/s/FyL7DRg" ref="nofollow noopener noreferrer">job.toutiao.com/s/FyL7DRg</a></p></div>  
</div>
            