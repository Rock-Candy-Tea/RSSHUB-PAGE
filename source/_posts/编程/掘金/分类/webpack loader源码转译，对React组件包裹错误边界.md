
---
title: 'webpack loader源码转译，对React组件包裹错误边界'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/44f481bea98d40d59efbe5fcee49df98~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Wed, 14 Jul 2021 23:10:59 GMT
thumbnail: 'https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/44f481bea98d40d59efbe5fcee49df98~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h2 data-id="heading-0">前言</h2>
<p>React项目常常会遇到整个页面突然白屏。遇到这种问题大概率是界面渲染过程中，组件<code>render</code>方法抛出异常导致React runtime崩溃。本文介绍编写<code>webpack loader</code>在项目构建中模块编译时自动对React组件做错误边界包裹处理。</p>
<p>阅读本文，你将会了解使用<code>@babel/parser</code>，<code>@babel/traverse</code>，<code>@babel/template</code>，<code>@babel/generator</code>四个库，把JavaScript模块代码，从源码按需转化成目标代码的实践过程。</p>
<h2 data-id="heading-1">为什么使用webpack loader</h2>
<h3 data-id="heading-2">背景</h3>
<p>在<code>webpack</code>模块编译阶段，入口<code>bundle</code>用到的模块都将逐一编译，每个模块的编译过程中会根据<code>webpack</code>的<code>module</code>配置，执行每个<code>loader</code>。
<code>loader</code>默认暴露的方法，能获取到模块的<code>源码</code>,经过处理并最终返回<code>目标代码</code>完成对一个模块的一次转译过程。</p>
<h3 data-id="heading-3">结论</h3>
<p>可以使用<code>loader</code>，通过接收<code>源码</code>，分析<code>源码</code>，修改<code>源码</code>，最终返回<code>源码</code>的步骤实现对React组件模块的<code>源码</code>，增加包裹错误边界的逻辑。</p>
<h2 data-id="heading-4">步骤</h2>
<h3 data-id="heading-5">1.分析源码</h3>
<p>分析<code>jsx</code>/<code>tsx</code>模块的源码，有很多种方式。本方案主要使用<code>@babel/parser</code>对源码进行<code>AST</code>抽象语法树对象的转换。</p>
<p>源码转换成<code>AST</code>对象后，接下来要做的就是对<code>AST</code>对象的分析。本文主要介绍React的<code>ESM</code>规范模块做相关的处理，<code>ESM</code>规范下React的组件暴露主要有以下四种方式:</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> ComponentA <span class="hljs-comment">// 情况1 export default</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> &#123;ComponentA, ComponentB, ComponentC&#125; <span class="hljs-comment">// 情况2 export default &#123;&#125;</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">// 情况3 export const</span>
<span class="hljs-keyword">export</span> <span class="hljs-keyword">const</span> ComponentA = <span class="hljs-function">(<span class="hljs-params">props</span>) =></span> &#123;
 <span class="hljs-comment">// 组件代码实现</span>
&#125; 
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">export</span> &#123;ComponentA, ComponentB, ComponentC&#125; <span class="hljs-comment">// 情况4 export &#123;&#125;</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>假定前置开发好错误边界组件，为高阶函数<code>HOC</code>:<code>ErrorBoundaryWrap</code>,目前需要做的是对以上四种方式的React模块<code>export</code>时，进行<code>HOC</code>的包裹，上文代码对应的转换如下：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> ErrorBoundaryWrap(ComponentA) <span class="hljs-comment">// 情况1</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">// 情况2</span>
<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> &#123;
  <span class="hljs-attr">ComponentA</span>: ErrorBoundaryWrap(ComponentA), 
  <span class="hljs-attr">ComponentB</span>: ErrorBoundaryWrap(ComponentB), 
  <span class="hljs-attr">ComponentC</span>: ErrorBoundaryWrap(ComponentC)
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">// 情况3</span>
<span class="hljs-keyword">export</span> <span class="hljs-keyword">const</span> ComponentA = ErrorBoundaryWrap(<span class="hljs-function">(<span class="hljs-params">props</span>) =></span> &#123;
 <span class="hljs-comment">// 组件代码实现</span>
&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">// 情况4</span>
<span class="hljs-keyword">const</span> ComponentAerrorBoundary = ErrorBoundaryWrap(ComponentA)
<span class="hljs-keyword">const</span> ComponentBerrorBoundary = ErrorBoundaryWrap(ComponentB)
<span class="hljs-keyword">const</span> ComponentCerrorBoundary = ErrorBoundaryWrap(ComponentC)
<span class="hljs-keyword">export</span> &#123;
  ComponentAerrorBoundary <span class="hljs-keyword">as</span> ComponentA, 
  ComponentBerrorBoundary <span class="hljs-keyword">as</span> ComponentB, 
  ComponentCerrorBoundary <span class="hljs-keyword">as</span> ComponentC
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<blockquote>
<p>目标转移：实现使用webpack loader对react组件包裹错误边界，可以理解为对上述四种情况的代码做转换，在webpack构建中，模块编译时，对源码进行转换，利用工程化手段。</p>
</blockquote>
<h3 data-id="heading-6">2.修改源码</h3>
<p>根据上述的四种情况，拟定一份源码，作为我们用例的编写：<code>origin.jsx</code></p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">import</span> React <span class="hljs-keyword">from</span> <span class="hljs-string">'react'</span>

<span class="hljs-keyword">const</span> Hello1 = <span class="hljs-function">() =></span> &#123;
  <span class="hljs-keyword">return</span> (
    <span class="xml"><span class="hljs-tag"><></span>
      <span class="hljs-tag"><<span class="hljs-name">h1</span>></span>Hello1 is here<span class="hljs-tag"></<span class="hljs-name">h1</span>></span>
    <span class="hljs-tag"></></span></span>
  )
&#125;
<span class="hljs-keyword">const</span> Hello2 = <span class="hljs-function">() =></span> &#123;
  <span class="hljs-keyword">return</span> (
    <span class="xml"><span class="hljs-tag"><></span>
      <span class="hljs-tag"><<span class="hljs-name">h1</span>></span>Hello2 is here<span class="hljs-tag"></<span class="hljs-name">h1</span>></span>
    <span class="hljs-tag"></></span></span>
  )
&#125;
<span class="hljs-keyword">export</span> <span class="hljs-keyword">const</span> Hello3 = <span class="hljs-function">() =></span> &#123;
  <span class="hljs-keyword">return</span> (
    <span class="xml"><span class="hljs-tag"><></span>
      <span class="hljs-tag"><<span class="hljs-name">h1</span>></span>Hello3 is here<span class="hljs-tag"></<span class="hljs-name">h1</span>></span>
    <span class="hljs-tag"></></span></span>
  )
&#125;
<span class="hljs-keyword">const</span> Hello5 = <span class="hljs-function">() =></span> &#123;
  <span class="hljs-keyword">return</span> (
    <span class="xml"><span class="hljs-tag"><></span>
      <span class="hljs-tag"><<span class="hljs-name">h1</span>></span>Hello5 is here<span class="hljs-tag"></<span class="hljs-name">h1</span>></span>
    <span class="hljs-tag"></></span></span>
  )
&#125;
<span class="hljs-keyword">const</span> Hello6 = <span class="hljs-function">() =></span> &#123;
  <span class="hljs-keyword">return</span> (
    <span class="xml"><span class="hljs-tag"><></span>
      <span class="hljs-tag"><<span class="hljs-name">h1</span>></span>Hello6 is here<span class="hljs-tag"></<span class="hljs-name">h1</span>></span>
    <span class="hljs-tag"></></span></span>
  )
&#125;
<span class="hljs-keyword">export</span> &#123;Hello1, Hello2&#125;

<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span>  &#123;
  Hello5, Hello6
&#125;

<span class="hljs-comment">// export default Hello1</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>或许这里有同学会有疑问，为什么不用<code>tsx</code>作为源码？</p>
<p>其实在使用<code>@babel/parser</code>把源码转换<code>AST</code>对象过程中，可以通过配置引入<code>typescript</code>插件，对<code>tsx</code>进行转译为<code>js</code>语法，所以在实际处理<code>AST</code>对象的过程中无需考虑<code>typescript</code>语法相关的节点。同理<code>jsx</code>插件会把源码中的<code>jsx</code>语法转换成React Element对象。</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">const</span> sourceAst = parser.parse(source, &#123;
    <span class="hljs-attr">sourceType</span>: <span class="hljs-string">'unambiguous'</span>,
    <span class="hljs-attr">plugins</span>: [<span class="hljs-string">'jsx'</span>, <span class="hljs-string">'typescript'</span>]
 &#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-7">AST对象分析</h3>
<p>不了解<code>AST</code>相关类型对象同学，可以到<code>https://astexplorer.net/</code>或相同功能的网站，粘贴源码直观查看<code>源码</code>转换成<code>AST</code>对象后的结构。</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/44f481bea98d40d59efbe5fcee49df98~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>接下来细说，上述四种情况中<code>情况2</code>具体处理流程:</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span>  &#123;
  Hello5, Hello6
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>转换为</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> &#123;
  <span class="hljs-attr">Hello5</span>: ErrorBoundaryWrap(Hello5), 
  <span class="hljs-attr">Hello6</span>: ErrorBoundaryWrap(Hello6), 
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/03267447eb5c49e795c4b8a057550b0e~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>通过工具或者对源码parse后<code>sourceAst</code>对象进行打印，可以看出<code>export default</code>是一个类型为<code>ExportDefaultDeclaration</code>的节点。</p>
<p>确定类型后，该怎么在<code>sourceAst</code>中寻找节点呢？接下来引出第二个库<code>@babel/traverse</code>。</p>
<pre><code class="hljs language-javascript copyable" lang="javascript">traverse(sourceAst, &#123;
    <span class="hljs-function"><span class="hljs-title">Program</span>(<span class="hljs-params">path</span>)</span>&#123;
        <span class="hljs-comment">// type 为'Program'节点处理</span>
    &#125;
    <span class="hljs-function"><span class="hljs-title">ImportDeclaration</span>(<span class="hljs-params">path</span>)</span>&#123;
        <span class="hljs-comment">// type 为'ImportDeclaration'节点处理</span>
    &#125;
    <span class="hljs-function"><span class="hljs-title">ArrowFunctionExpression</span>(<span class="hljs-params">path</span>)</span>&#123;
        <span class="hljs-comment">// type 为'ArrowFunctionExpression'节点处理</span>
    &#125;
    <span class="hljs-function"><span class="hljs-title">ExportSpecifier</span>(<span class="hljs-params">path</span>)</span>&#123;
        <span class="hljs-comment">// type 为'ExportSpecifier'节点处理</span>
    &#125;
    <span class="hljs-function"><span class="hljs-title">ExportDefaultDeclaration</span>(<span class="hljs-params">path</span>)</span>&#123;
        <span class="hljs-comment">// type 为'ExportDefaultDeclaration'节点处理</span>
    &#125;
&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<p><code>@babel/traverse</code>默认返回<code>traverse</code>方法，<code>traverse</code>主要接收两个参数，<code>AST</code>对象，和针对各种<code>类型</code>节点的处理回调函数。</p>
<p><code>traverse</code>方法会遍历传入的<code>AST</code>对象的每个<code>节点</code>，根据当前<code>节点</code>的类型执行对应的回调函数，回调函数会接收到<code>path</code>对象入参，<code>path</code>对象包含当前<code>节点</code>信息及该<code>节点</code>的<code>父节点</code>、<code>子节点</code>、<code>兄弟节点</code>相关对象的<code>引用</code>。</p>
<p>由于<code>// export default Hello1</code>被注释，当前<code>AST</code>中仅有一个类型为<code>ExportDefaultDeclaration</code>的<code>节点</code>，通过执行以下代码，能看到<code>ExportDefaultDeclaration</code>只会执行一次。</p>
<pre><code class="hljs language-javascript copyable" lang="javascript">traverse(sourceAst, &#123;
    <span class="hljs-comment">// 其他节点类型处理</span>
    <span class="hljs-function"><span class="hljs-title">ExportDefaultDeclaration</span>(<span class="hljs-params">path</span>)</span>&#123;
        <span class="hljs-built_in">console</span>.log(<span class="hljs-string">`#ExportDefaultDeclaration`</span>, path)
        <span class="hljs-comment">// type 为'ExportDefaultDeclaration'节点处理</span>
    &#125;
&#125;)
<span class="hljs-comment">// 输出一次 #ExportDefaultDeclaratio</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>完整代码请见 <a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2FefoxTeam%2Freact-boundary-loader" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/efoxTeam/react-boundary-loader" ref="nofollow noopener noreferrer">github.com/efoxTeam/re…</a> 执行<code>yarn && yarn test</code>运行代码。</p>
<p>接下来分析上述代码打印出来的<code>path</code>对象：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">// path对象的方法属性不完全展示</span>
NodePath &#123;
  <span class="hljs-attr">parentPath</span>: <span class="xml"><span class="hljs-tag"><<span class="hljs-name">ref</span> *<span class="hljs-attr">1</span>></span> NodePath &#123;  // 父节点path对象引用
  &#125;,
  node: Node &#123;  // 当前节点
    type: 'ExportDefaultDeclaration', // 节点类型
    declaration: Node &#123; // 子节点类型 ObjectExpression 相对于代码 &#123;Hello5, Hello6&#125; 部分
      type: 'ObjectExpression',
      properties: [Array] // 子节点属性， 下文会再展开
    &#125;
  &#125;,
  type: 'ExportDefaultDeclaration',  //当前节点类型
  parent: Node &#123; // 父节点
  &#125;,
&#125;
</span><span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-8">源AST转换为目标AST</h3>
<p>得到要操作的<code>节点</code>对象，接下来再确认一下需要做的事情：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span>  &#123;
  Hello5, Hello6
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>上述代码片段需要转换为下面的目标代码：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> &#123;
  <span class="hljs-attr">Hello5</span>: ErrorBoundaryWrap(Hello5), 
  <span class="hljs-attr">Hello6</span>: ErrorBoundaryWrap(Hello6), 
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>接下来打印<code>ExportDefaultDeclaration</code>类型的子节点<code>properties</code>属性值<code>path.node.declaration.properties</code>，对应代码<code>&#123;Hello5, Hello6&#125;</code>部分</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-built_in">console</span>.log(path.node.declaration.properties)
<span class="hljs-comment">// 保留关键部分的输出</span>
ExportDefaultDeclaration [
  &#123;
    <span class="hljs-attr">type</span>: <span class="hljs-string">'ObjectProperty'</span>,
    <span class="hljs-attr">computed</span>: <span class="hljs-literal">false</span>,
    <span class="hljs-attr">key</span>: &#123;
      <span class="hljs-attr">type</span>: <span class="hljs-string">'Identifier'</span>,
      <span class="hljs-attr">name</span>: <span class="hljs-string">'Hello5'</span>, <span class="hljs-comment">// 能获取到Hello5 Key值</span>
      <span class="hljs-attr">loc</span>: <span class="hljs-literal">undefined</span>,
      <span class="hljs-attr">leadingComments</span>: <span class="hljs-literal">undefined</span>,
      <span class="hljs-attr">innerComments</span>: <span class="hljs-literal">undefined</span>,
      <span class="hljs-attr">trailingComments</span>: <span class="hljs-literal">undefined</span>,
      <span class="hljs-attr">extra</span>: &#123;&#125;
    &#125;,
  &#125;,
  &#123;
    <span class="hljs-attr">type</span>: <span class="hljs-string">'ObjectProperty'</span>,
    <span class="hljs-attr">computed</span>: <span class="hljs-literal">false</span>,
    <span class="hljs-attr">key</span>: &#123;
      <span class="hljs-attr">type</span>: <span class="hljs-string">'Identifier'</span>,
      <span class="hljs-attr">name</span>: <span class="hljs-string">'Hello6'</span>, <span class="hljs-comment">// 能获取到Hello6 Key值</span>
      <span class="hljs-attr">loc</span>: <span class="hljs-literal">undefined</span>,
      <span class="hljs-attr">leadingComments</span>: <span class="hljs-literal">undefined</span>,
      <span class="hljs-attr">innerComments</span>: <span class="hljs-literal">undefined</span>,
      <span class="hljs-attr">trailingComments</span>: <span class="hljs-literal">undefined</span>,
      <span class="hljs-attr">extra</span>: &#123;&#125;
    &#125;,
  &#125;
]
<span class="copy-code-btn">复制代码</span></code></pre>
<p>拿到<code>Hello5</code>,<code>Hello6</code>两个Key值之后，可以构造出我们需要的代码片段，接下来介绍<code>@babel/template</code>库，使用<code>template</code>API可以把源码转换为<code>AST</code>节点。生成新的<code>AST</code>节点后，可以对原<code>AST</code>进行<code>节点</code>插入或替换。代码如下：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">let</span> replaceNodeString = <span class="hljs-string">'export default &#123;'</span>
<span class="hljs-keyword">let</span> adot = <span class="hljs-string">''</span>
path.node.declaration.properties.forEach(<span class="hljs-function"><span class="hljs-params">item</span> =></span> &#123;
  <span class="hljs-keyword">if</span> (item?.value?.name) &#123;
    replaceNodeString += <span class="hljs-string">` <span class="hljs-subst">$&#123;adot&#125;</span> <span class="hljs-subst">$&#123;item.value.name&#125;</span>: ErrorBoundary(<span class="hljs-subst">$&#123;item.value.name&#125;</span>)`</span>
    adot = <span class="hljs-string">','</span>
  &#125;
&#125;)
replaceNodeString += <span class="hljs-string">'&#125;'</span>
<span class="hljs-keyword">const</span> newNode = template.statement(replaceNodeString)()
newNode.isdeal = <span class="hljs-literal">true</span>
path.replaceWithMultiple([newNode])
<span class="copy-code-btn">复制代码</span></code></pre>
<p>上述代码通过遍历<code>path.node.declaration.properties</code>生成如下代码片段：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> &#123;
  <span class="hljs-attr">Hello5</span>: ErrorBoundaryWrap(Hello5), 
  <span class="hljs-attr">Hello6</span>: ErrorBoundaryWrap(Hello6), 
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>再把代码片段通过<code>template.statement(replaceNodeString)()</code>转换成目标<code>节点</code>对象，再使用<code>path.replaceWithMultiple</code>方法替换掉原本属于：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span>  &#123;
  Hello5, Hello6
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>的<code>节点</code>。</p>
<p>以上就完成了对<code>情况4</code>的React暴露组件代码的错误边界包裹。另外三种情况的处理和避免重复处理相同的<code>AST</code>节点、误处理相同类型的<code>AST</code>节点、以及引入<code>ErrorBoundaryWrap</code>高阶组件的实现请见 <a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2FefoxTeam%2Freact-boundary-loader" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/efoxTeam/react-boundary-loader" ref="nofollow noopener noreferrer">github.com/efoxTeam/re…</a></p>
<h3 data-id="heading-9">3.生成目标代码</h3>
<p>最后，当源<code>AST</code>经过处理，达到目标<code>AST</code>后，通过使用<code>@babel/generator</code>把目标<code>AST</code>转化为目标代码，作为loader露出方法的返回值返回。</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">const</span> &#123; code &#125; = generate(sourceAst)
<span class="hljs-keyword">return</span> code
<span class="copy-code-btn">复制代码</span></code></pre>
<p>到此，一个特定功能的模块转译loader完成。</p>
<h2 data-id="heading-10">结语</h2>
<p>本方案主要通过webpack loader的实现，对jsx/tsx后缀的JavaScript模块，进行暴露引用的4种情况，进行错误边界的包裹。用工程化手段自动化对React组件做容错处理，避免组件渲染异常导致react runtime render的崩溃。</p>
<p>推荐相关读物</p>
<ul>
<li>babel 官网 <a href="https://link.juejin.cn/?target=https%3A%2F%2Fbabeljs.io%2F" target="_blank" rel="nofollow noopener noreferrer" title="https://babeljs.io/" ref="nofollow noopener noreferrer">babeljs.io/</a></li>
<li>掘金小册子《babel 插件通关秘籍》 <a href="https://juejin.cn/book/6946117847848321055" target="_blank" title="https://juejin.cn/book/6946117847848321055">juejin.cn/book/694611…</a></li>
</ul></div>  
</div>
            