
---
title: '富文本编辑器框架 - slate.js'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/78fb882c5f0a43eb980f53641bdf70fd~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Sat, 05 Jun 2021 04:45:22 GMT
thumbnail: 'https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/78fb882c5f0a43eb980f53641bdf70fd~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/78fb882c5f0a43eb980f53641bdf70fd~tplv-k3u1fbpfcp-watermark.image" alt="preview.png" loading="lazy" referrerpolicy="no-referrer"></p>
<blockquote>
<p>图片来源：<a href="https://github.com/ianstormtaylor/slate#" target="_blank" rel="nofollow noopener noreferrer">github.com/ianstormtay…</a></p>
</blockquote>
<h2 data-id="heading-0">Slate 简介</h2>
<p><a href="https://docs.slatejs.org/" target="_blank" rel="nofollow noopener noreferrer">Slate</a> 是一个使用 TypeScript 开发的富文本编辑器开发框架，诞生于 2016 年，作者是 Ian Storm Taylor。Slate 是一个<code>完全</code>可定制的富文本编辑器框架。Slate 让你构建像 <a href="https://medium.com/" target="_blank" rel="nofollow noopener noreferrer">Medium</a>, <a href="https://www.dropbox.com/paper" target="_blank" rel="nofollow noopener noreferrer">Dropbox Paper</a> 或者是 <a href="https://www.google.com/docs/about/" target="_blank" rel="nofollow noopener noreferrer">Google Docs</a> 这样丰富，直观的编辑器。你可以认为它是基于 <code>React</code> 的一种可拔插的 <code>contenteditable</code> 实现。它的灵感来源于 <a href="https://draftjs.org/" target="_blank" rel="nofollow noopener noreferrer">Draft.js</a>，<a href="https://prosemirror.net/" target="_blank" rel="nofollow noopener noreferrer">Prosemirror</a> 和 <a href="https://quilljs.com/" target="_blank" rel="nofollow noopener noreferrer">Quill</a> 这样的库。slate 比较知名的用户有 <code>GitBook</code> 和<code>语雀</code>等。<br></p>
<p><code>Slate</code> 在线 <a href="https://www.slatejs.org/examples/richtext" target="_blank" rel="nofollow noopener noreferrer">Demo</a></p>
<h2 data-id="heading-1">特点</h2>
<ul>
<li>插件作为一等公民，能够完全修改编辑器行为；</li>
<li>数据层和渲染层分离，更新数据触发渲染；</li>
<li>文档数据类似于 DOM 树，可嵌套；</li>
<li>具有原子化操作 API，支持协同编辑；</li>
<li>使用 React 作为渲染层；</li>
</ul>
<h2 data-id="heading-2">slate 架构简介</h2>
<h3 data-id="heading-3">架构图</h3>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/fd48436d490348e78cdd02187e980458~tplv-k3u1fbpfcp-watermark.image" alt="未命名绘图 (14).png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>在 slate 代码仓库下包含四个 <code>package</code> 包：</p>
<ol>
<li><strong>Slate History</strong>: 历史插件，提供了undo/redo支持；</li>
<li><strong>slate-hyperscript</strong>: 能够使用 JSX 语法来创建 slate 的数据；</li>
<li><strong>slate-react</strong>: 视图层；</li>
<li><strong>slate</strong>: 编辑器核心抽象，定义了 Editor，Path，Node，Text，Operation 等基础类，Transforms 操作；</li>
</ol>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/adb459df9d3448aca148547668cb833c~tplv-k3u1fbpfcp-watermark.image" alt="WeChat86c41084f9e8169093c53fb1d3201919.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-4">slate (model)</h2>
<p><code>slate package</code> 是 slate 的核心，定义了编辑器的<code>数据模型</code>、操作这些模型的基本操作、以及创建编辑器实例对象的方法。</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/86179c5633c0411cbdc0e4af00d4cb02~tplv-k3u1fbpfcp-watermark.image" alt="未命名绘图 (15).png" loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-5">Interfaces</h3>
<p><code>intefaces</code> 目录下是 Slate 定义的数据模型，定义了 editor 、element、text、path、point、range、operation、location 等。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">export</span> type Node = Editor | Element | Text

<span class="hljs-keyword">export</span> interface Element &#123;
  <span class="hljs-attr">children</span>: Node[]
  [key: string]: unknown
&#125;

<span class="hljs-keyword">export</span> interface Text &#123;
  <span class="hljs-attr">text</span>: string
  [key: string]: unknown
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li><strong>Editor</strong> Slate 的顶级节点就是 <code>Editor</code> 。它封装了文档的所有富文本内容，但是对于节点来说最重要的部分是它的 <code>children</code> 属性，其中包含一个 <code>Node</code> 对象树。</li>
<li><strong>Element</strong> 类型含有 children 属性。</li>
<li><strong>Text</strong> 文本节点是树中的最低级节点，包含文档的文本内容以及任何格式。</li>
</ul>
<p>用户可以自行拓展 Node 的属性，例如通过添加 type 字段标识 Node 的类型（paragraph, ordered list, heading 等等），或者是文本的属性（italic, bold 等等），来描述富文本中的文字和段落。</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/dd0c742fb8eb421aac16365b00fc14a3~tplv-k3u1fbpfcp-watermark.image" alt="截屏2021-06-02 上午8.11.47.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h4 data-id="heading-6">路径(Path)</h4>
<p>路径是引用一个位置的最底层方式。每个路径都是一个简单的数字数组，它通过文档树中每个祖先节点的索引来引用一个节点:</p>
<pre><code class="hljs language-js copyable" lang="js">type Path = number[]
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/4504a6c5732c4a81998514ca61c1d0af~tplv-k3u1fbpfcp-watermark.image" alt="截屏2021-06-03 上午7.27.29.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h4 data-id="heading-7">点(Point)</h4>
<p><code>Point</code> 包含一个 <code>offset</code> 属性（偏移量）对于特定的文本节点:</p>
<pre><code class="hljs language-js copyable" lang="js">interface Point &#123;
  <span class="hljs-attr">path</span>: Path
  <span class="hljs-attr">offset</span>: number
  [key: string]: unknown
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-8">文档范围(Range)</h4>
<p>文档范围不仅指文档中的一个点，它是指两点之间的内容。</p>
<pre><code class="hljs language-js copyable" lang="js">interface Range &#123;
  <span class="hljs-attr">anchor</span>: Point
  <span class="hljs-attr">focus</span>: Point
  [key: string]: unknown
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><code>锚点</code>和<code>焦点</code>是通过用户交互建立的。锚点并不一定在焦点的<code> 前面</code>。就像在 DOM 一样，锚点和焦点的排序取决于选区的方向（向前或向后）。</p>
<h4 data-id="heading-9">Operation</h4>
<p><code>Operation</code> 对象是 Slate 用来更改内部状态的低级指令，作为文档的最小抽象， Slate 将所有变化表示为 Operation。你可以从 <a href="https://github.com/ianstormtaylor/slate/blob/main/packages/slate/src/interfaces/operation.ts#L140" target="_blank" rel="nofollow noopener noreferrer">这里</a> 看到源码。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">export</span> interface OperationInterface &#123;
  <span class="hljs-attr">isNodeOperation</span>: <span class="hljs-function">(<span class="hljs-params">value: any</span>) =></span> value is NodeOperation
  <span class="hljs-attr">isOperation</span>: <span class="hljs-function">(<span class="hljs-params">value: any</span>) =></span> value is Operation
  <span class="hljs-attr">isOperationList</span>: <span class="hljs-function">(<span class="hljs-params">value: any</span>) =></span> value is Operation[]
  <span class="hljs-attr">isSelectionOperation</span>: <span class="hljs-function">(<span class="hljs-params">value: any</span>) =></span> value is SelectionOperation
  <span class="hljs-attr">isTextOperation</span>: <span class="hljs-function">(<span class="hljs-params">value: any</span>) =></span> value is TextOperation
  <span class="hljs-attr">inverse</span>: <span class="hljs-function">(<span class="hljs-params">op: Operation</span>) =></span> Operation
&#125;


<span class="hljs-keyword">export</span> <span class="hljs-keyword">const</span> Operation: OperationInterface = &#123;

  .....
  
  isOperation(value: any): value is Operation &#123;
    <span class="hljs-keyword">if</span> (!isPlainObject(value)) &#123;
      <span class="hljs-keyword">return</span> <span class="hljs-literal">false</span>
    &#125;

    <span class="hljs-keyword">switch</span> (value.type) &#123;
      <span class="hljs-keyword">case</span> <span class="hljs-string">'insert_node'</span>:
        <span class="hljs-keyword">return</span> Path.isPath(value.path) && Node.isNode(value.node)
      <span class="hljs-keyword">case</span> <span class="hljs-string">'insert_text'</span>:
        <span class="hljs-keyword">return</span> (
          <span class="hljs-keyword">typeof</span> value.offset === <span class="hljs-string">'number'</span> &&
          <span class="hljs-keyword">typeof</span> value.text === <span class="hljs-string">'string'</span> &&
          Path.isPath(value.path)
        )
      <span class="hljs-keyword">case</span> <span class="hljs-string">'merge_node'</span>:
        <span class="hljs-keyword">return</span> (
          <span class="hljs-keyword">typeof</span> value.position === <span class="hljs-string">'number'</span> &&
          Path.isPath(value.path) &&
          isPlainObject(value.properties)
        )
      <span class="hljs-keyword">case</span> <span class="hljs-string">'move_node'</span>:
        <span class="hljs-keyword">return</span> Path.isPath(value.path) && Path.isPath(value.newPath)
      <span class="hljs-keyword">case</span> <span class="hljs-string">'remove_node'</span>:
        <span class="hljs-keyword">return</span> Path.isPath(value.path) && Node.isNode(value.node)
      <span class="hljs-keyword">case</span> <span class="hljs-string">'remove_text'</span>:
        <span class="hljs-keyword">return</span> (
          <span class="hljs-keyword">typeof</span> value.offset === <span class="hljs-string">'number'</span> &&
          <span class="hljs-keyword">typeof</span> value.text === <span class="hljs-string">'string'</span> &&
          Path.isPath(value.path)
        )
      <span class="hljs-keyword">case</span> <span class="hljs-string">'set_node'</span>:
        <span class="hljs-keyword">return</span> (
          Path.isPath(value.path) &&
          isPlainObject(value.properties) &&
          isPlainObject(value.newProperties)
        )
      <span class="hljs-keyword">case</span> <span class="hljs-string">'set_selection'</span>:
        <span class="hljs-keyword">return</span> (
          (value.properties === <span class="hljs-literal">null</span> && Range.isRange(value.newProperties)) ||
          (value.newProperties === <span class="hljs-literal">null</span> && Range.isRange(value.properties)) ||
          (isPlainObject(value.properties) &&
            isPlainObject(value.newProperties))
        )
      <span class="hljs-keyword">case</span> <span class="hljs-string">'split_node'</span>:
        <span class="hljs-keyword">return</span> (
          Path.isPath(value.path) &&
          <span class="hljs-keyword">typeof</span> value.position === <span class="hljs-string">'number'</span> &&
          isPlainObject(value.properties)
        )
      <span class="hljs-attr">default</span>:
        <span class="hljs-keyword">return</span> <span class="hljs-literal">false</span>
    &#125;
  &#125;,
  
  ......
  
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>从上面的代码中可以看出，Operation 类型有 <code>9</code> 个：</p>
<ul>
<li>insert_node：插入一个 Node。 包含 <code>插入位置</code>（path），<code>插入节点</code>（node）信息</li>
</ul>
<pre><code class="hljs language-js copyable" lang="js"> <span class="hljs-keyword">case</span> <span class="hljs-string">'insert_node'</span>:
        <span class="hljs-keyword">return</span> Path.isPath(value.path) && Node.isNode(value.node)
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>insert_text：插入一段文本，所在 <code>节点</code>（path），<code>插入内容</code>（text），<code>偏移量</code>（offset）</li>
</ul>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">case</span> <span class="hljs-string">'insert_text'</span>:
        <span class="hljs-keyword">return</span> (
          <span class="hljs-keyword">typeof</span> value.offset === <span class="hljs-string">'number'</span> &&
          <span class="hljs-keyword">typeof</span> value.text === <span class="hljs-string">'string'</span> &&
          Path.isPath(value.path)
        )
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>merge_node：将两个 Node 组合成一个，包含待合并的 <code>节点</code>（path），合并目的地位置（position），合并后节点属性（properties）信息。</li>
</ul>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">case</span> <span class="hljs-string">'merge_node'</span>:
        <span class="hljs-keyword">return</span> (
          <span class="hljs-keyword">typeof</span> value.position === <span class="hljs-string">'number'</span> &&
          Path.isPath(value.path) &&
          isPlainObject(value.properties)
        )
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>move_node：移动 Node，包含 移动位置（path），移动目的地（newPath）信息</li>
</ul>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">case</span> <span class="hljs-string">'move_node'</span>:
 <span class="hljs-keyword">return</span> Path.isPath(value.path) && Path.isPath(value.newPath)
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>remove_node：移除 Node，包含 删除位置（path），删除节点（node）信息</li>
</ul>
<pre><code class="hljs language-js copyable" lang="js"> <span class="hljs-keyword">case</span> <span class="hljs-string">'remove_node'</span>:
  <span class="hljs-keyword">return</span> Path.isPath(value.path) && Node.isNode(value.node)
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>remove_text：移除文本，包含 所在节点（path），删除内容（text），偏移量（offset）信息</li>
</ul>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">case</span> <span class="hljs-string">'remove_text'</span>:
        <span class="hljs-keyword">return</span> (
          <span class="hljs-keyword">typeof</span> value.offset === <span class="hljs-string">'number'</span> &&
          <span class="hljs-keyword">typeof</span> value.text === <span class="hljs-string">'string'</span> &&
          Path.isPath(value.path)
        )
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>set_node：设置 Node 属性，包含 所在节点（path），被设置节点（node），节点属性（properties）信息</li>
</ul>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">case</span> <span class="hljs-string">'set_node'</span>:
        <span class="hljs-keyword">return</span> (
          Path.isPath(value.path) &&
          isPlainObject(value.properties) &&
          isPlainObject(value.newProperties)
        )
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>set_selection：设置选区位置，包含 新旧节点属性（properties，newProperties）信息</li>
</ul>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">case</span> <span class="hljs-string">'set_selection'</span>:
        <span class="hljs-keyword">return</span> (
          (value.properties === <span class="hljs-literal">null</span> && Range.isRange(value.newProperties)) ||
          (value.newProperties === <span class="hljs-literal">null</span> && Range.isRange(value.properties)) ||
          (isPlainObject(value.properties) &&
            isPlainObject(value.newProperties))
        )
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>split_node：拆分 Node ，包含 所在节点（path），节点位置（position），节点属性（properties）信息</li>
</ul>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">case</span> <span class="hljs-string">'split_node'</span>:
        <span class="hljs-keyword">return</span> (
          Path.isPath(value.path) &&
          <span class="hljs-keyword">typeof</span> value.position === <span class="hljs-string">'number'</span> &&
          isPlainObject(value.properties)
        )
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-10">Transforms</h3>
<p><code>Transforms</code> 是对文档进行操作的辅助函数，包括<code>选区转换</code>，<code>节点转换</code>，<code>文本转换</code>和<code>通用转换</code>。你可以从 <a href="https://github.com/ianstormtaylor/slate/blob/main/packages/slate/src/transforms/index.ts#L6" target="_blank" rel="nofollow noopener noreferrer">这里</a> 看到源码。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">export</span> <span class="hljs-keyword">const</span> Transforms: GeneralTransforms &
  NodeTransforms &
  SelectionTransforms &
  TextTransforms = &#123;
  ...GeneralTransforms,<span class="hljs-comment">// 操作 Operation 指令</span>
  ...NodeTransforms,<span class="hljs-comment">// 操作节点指令</span>
  ...SelectionTransforms,<span class="hljs-comment">// 操作选区指令</span>
  ...TextTransforms,<span class="hljs-comment">// 操作文本指令</span>
&#125;

<span class="copy-code-btn">复制代码</span></code></pre>
<p><code>GeneralTransforms</code> 比较特殊，它并不生成 Operation ，而是对 Operation 进行处理，只有它能<code>直接修改 model</code>，其他 transforms 最终都会转换成 GeneralTransforms 中的一种。</p>
<h3 data-id="heading-11">createEditor</h3>
<p>创建编辑器实例的方法，返回一个实现了 Editor 接口的编辑器实例对象。你可以从 <a href="https://github.com/ianstormtaylor/slate/blob/main/packages/slate/src/create-editor.ts#L22" target="_blank" rel="nofollow noopener noreferrer">这里</a> 看到源码。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">export</span> <span class="hljs-keyword">const</span> createEditor = (): <span class="hljs-function"><span class="hljs-params">Editor</span> =></span> &#123;
  <span class="hljs-keyword">const</span> editor: Editor = &#123;
    .....
  &#125;
 
  <span class="hljs-keyword">return</span> editor
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-12">更新 model</h3>
<p>对 model 进行变更的过程主要分为以下两步：</p>
<ol>
<li>通过 Transforms 提供的一系列方法生成 Operation</li>
<li>Operation 进入 apply 流程</li>
</ol>
<p>在 Operation apply 流程中有4 个主要步骤：</p>
<ol>
<li>记录变更脏区</li>
<li>对 Operation 进行 transform</li>
<li>对 model 正确性进行校验</li>
<li>触发变更回调</li>
</ol>
<p>以 <code>Transforms.insertText</code> 为例，你可以从 <a href="https://github.com/ianstormtaylor/slate/blob/main/packages/slate/src/transforms/text.ts#L446" target="_blank" rel="nofollow noopener noreferrer">这里</a> 看到源码。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">export</span> <span class="hljs-keyword">const</span> TextTransforms: TextTransforms = &#123;
  .....
  
   insertText(
    editor: Editor,
    <span class="hljs-attr">text</span>: string,
    <span class="hljs-attr">options</span>: &#123;
      at?: Location
      voids?: boolean
    &#125; = &#123;&#125;
  ): <span class="hljs-keyword">void</span> &#123;
     Editor.withoutNormalizing(editor, <span class="hljs-function">() =></span> &#123;
       <span class="hljs-keyword">const</span> &#123; voids = <span class="hljs-literal">false</span> &#125; = options
      <span class="hljs-keyword">let</span> &#123; at = editor.selection &#125; = options
      .....
      
      <span class="hljs-keyword">const</span> &#123; path, offset &#125; = at
      <span class="hljs-keyword">if</span> (text.length > <span class="hljs-number">0</span>)
        editor.apply(&#123; <span class="hljs-attr">type</span>: <span class="hljs-string">'insert_text'</span>, path, offset, text &#125;)
     &#125;)
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>Transforms.insertText 的最后生成了一个 type 为 <code>insert_text</code> 的 Operation 并调用 Editor 实例的 <code>apply</code> 方法。</p>
<h4 data-id="heading-13">editor.apply 方法</h4>
<p>你可以从 <a href="https://github.com/ianstormtaylor/slate/blob/main/packages/slate/src/create-editor.ts#L22" target="_blank" rel="nofollow noopener noreferrer">这里</a> 看到源码。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">export</span> <span class="hljs-keyword">const</span> createEditor = (): <span class="hljs-function"><span class="hljs-params">Editor</span> =></span> &#123;
  <span class="hljs-keyword">const</span> editor: Editor =&#123;
    <span class="hljs-attr">children</span>: [],
    <span class="hljs-attr">operations</span>: [],
    <span class="hljs-attr">selection</span>: <span class="hljs-literal">null</span>,
    <span class="hljs-attr">marks</span>: <span class="hljs-literal">null</span>,
    <span class="hljs-attr">isInline</span>: <span class="hljs-function">() =></span> <span class="hljs-literal">false</span>,
    <span class="hljs-attr">isVoid</span>: <span class="hljs-function">() =></span> <span class="hljs-literal">false</span>,
    <span class="hljs-attr">onChange</span>: <span class="hljs-function">() =></span> &#123;&#125;,
     <span class="hljs-attr">apply</span>: <span class="hljs-function">(<span class="hljs-params">op: Operation</span>) =></span> &#123;
      <span class="hljs-keyword">for</span> (<span class="hljs-keyword">const</span> ref <span class="hljs-keyword">of</span> Editor.pathRefs(editor)) &#123;
        PathRef.transform(ref, op)
      &#125;

      <span class="hljs-keyword">for</span> (<span class="hljs-keyword">const</span> ref <span class="hljs-keyword">of</span> Editor.pointRefs(editor)) &#123;
        PointRef.transform(ref, op)
      &#125;

      <span class="hljs-keyword">for</span> (<span class="hljs-keyword">const</span> ref <span class="hljs-keyword">of</span> Editor.rangeRefs(editor)) &#123;
        RangeRef.transform(ref, op)
      &#125;

      <span class="hljs-keyword">const</span> set = <span class="hljs-keyword">new</span> <span class="hljs-built_in">Set</span>()
      <span class="hljs-keyword">const</span> dirtyPaths: Path[] = []

      <span class="hljs-keyword">const</span> add = <span class="hljs-function">(<span class="hljs-params">path: Path | <span class="hljs-literal">null</span></span>) =></span> &#123;
        <span class="hljs-keyword">if</span> (path) &#123;
          <span class="hljs-keyword">const</span> key = path.join(<span class="hljs-string">','</span>)

          <span class="hljs-keyword">if</span> (!set.has(key)) &#123;
            set.add(key)
            dirtyPaths.push(path)
          &#125;
        &#125;
      &#125;

      <span class="hljs-keyword">const</span> oldDirtyPaths = DIRTY_PATHS.get(editor) || []
      <span class="hljs-keyword">const</span> newDirtyPaths = getDirtyPaths(op)

      <span class="hljs-keyword">for</span> (<span class="hljs-keyword">const</span> path <span class="hljs-keyword">of</span> oldDirtyPaths) &#123;
        <span class="hljs-keyword">const</span> newPath = Path.transform(path, op)
        add(newPath)
      &#125;

      <span class="hljs-keyword">for</span> (<span class="hljs-keyword">const</span> path <span class="hljs-keyword">of</span> newDirtyPaths) &#123;
        add(path)
      &#125;

      DIRTY_PATHS.set(editor, dirtyPaths)
      Transforms.transform(editor, op)
      editor.operations.push(op)
      Editor.normalize(editor)

      <span class="hljs-comment">// Clear any formats applied to the cursor if the selection changes.</span>
      <span class="hljs-keyword">if</span> (op.type === <span class="hljs-string">'set_selection'</span>) &#123;
        editor.marks = <span class="hljs-literal">null</span>
      &#125;

      <span class="hljs-keyword">if</span> (!FLUSHING.get(editor)) &#123;
        FLUSHING.set(editor, <span class="hljs-literal">true</span>)

        <span class="hljs-built_in">Promise</span>.resolve().then(<span class="hljs-function">() =></span> &#123;
          FLUSHING.set(editor, <span class="hljs-literal">false</span>)
          editor.onChange()
          editor.operations = []
        &#125;)
      &#125;
    &#125;,
    ......
  &#125;
  <span class="hljs-keyword">return</span> editor
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h5 data-id="heading-14">转换坐标</h5>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">for</span> (<span class="hljs-keyword">const</span> ref <span class="hljs-keyword">of</span> Editor.pathRefs(editor)) &#123;
    PathRef.transform(ref, op)
  &#125;

  <span class="hljs-keyword">for</span> (<span class="hljs-keyword">const</span> ref <span class="hljs-keyword">of</span> Editor.pointRefs(editor)) &#123;
    PointRef.transform(ref, op)
  &#125;

  <span class="hljs-keyword">for</span> (<span class="hljs-keyword">const</span> ref <span class="hljs-keyword">of</span> Editor.rangeRefs(editor)) &#123;
    RangeRef.transform(ref, op)
  &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h5 data-id="heading-15">dirtyPaths</h5>
<p>dirtyPaths 一共有以下两种生成机制:</p>
<ol>
<li>一种是在 operation apply 之前的 <code>oldDirtypath</code></li>
<li>一种由 <code>getDirthPaths</code> 方法获取</li>
</ol>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> set = <span class="hljs-keyword">new</span> <span class="hljs-built_in">Set</span>()
<span class="hljs-keyword">const</span> dirtyPaths: Path[] = []
<span class="hljs-keyword">const</span> add = <span class="hljs-function">(<span class="hljs-params">path: Path | <span class="hljs-literal">null</span></span>) =></span> &#123;
        <span class="hljs-keyword">if</span> (path) &#123;
          <span class="hljs-keyword">const</span> key = path.join(<span class="hljs-string">','</span>)

          <span class="hljs-keyword">if</span> (!set.has(key)) &#123;
            set.add(key)
            dirtyPaths.push(path)
          &#125;
        &#125;
      &#125;
<span class="hljs-keyword">const</span> oldDirtyPaths = DIRTY_PATHS.get(editor) || []
<span class="hljs-keyword">const</span> newDirtyPaths = getDirtyPaths(op)

<span class="hljs-keyword">for</span> (<span class="hljs-keyword">const</span> path <span class="hljs-keyword">of</span> oldDirtyPaths) &#123;
        <span class="hljs-keyword">const</span> newPath = Path.transform(path, op)
        add(newPath)
&#125;

<span class="hljs-keyword">for</span> (<span class="hljs-keyword">const</span> path <span class="hljs-keyword">of</span> newDirtyPaths) &#123;
        add(path)
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h5 data-id="heading-16">执行变更操作</h5>
<pre><code class="hljs language-js copyable" lang="js">Transforms.transform(editor, op)
<span class="copy-code-btn">复制代码</span></code></pre>
<p><code>Transforms.transform(editor, op)</code> 就是在调用 GeneralTransforms 处理 Operation。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> applyToDraft = <span class="hljs-function">(<span class="hljs-params">editor: Editor, selection: Selection, op: Operation</span>) =></span> &#123;
 <span class="hljs-keyword">switch</span> (op.type) &#123;
  ...
  <span class="hljs-keyword">case</span> <span class="hljs-string">'insert_text'</span>: &#123;
      <span class="hljs-keyword">const</span> &#123; path, offset, text &#125; = op
      <span class="hljs-keyword">if</span> (text.length === <span class="hljs-number">0</span>) <span class="hljs-keyword">break</span>
      <span class="hljs-keyword">const</span> node = Node.leaf(editor, path)
      <span class="hljs-keyword">const</span> before = node.text.slice(<span class="hljs-number">0</span>, offset)
      <span class="hljs-keyword">const</span> after = node.text.slice(offset)
      node.text = before + text + after

      <span class="hljs-keyword">if</span> (selection) &#123;
        <span class="hljs-keyword">for</span> (<span class="hljs-keyword">const</span> [point, key] <span class="hljs-keyword">of</span> Range.points(selection)) &#123;
          selection[key] = Point.transform(point, op)!
        &#125;
      &#125;

      <span class="hljs-keyword">break</span>
    &#125;
   ....
 &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h5 data-id="heading-17">记录 operation</h5>
<pre><code class="hljs language-js copyable" lang="js">editor.operations.push(op)
<span class="copy-code-btn">复制代码</span></code></pre>
<h5 data-id="heading-18">数据校验</h5>
<pre><code class="hljs language-js copyable" lang="js">Editor.normalize(editor)
<span class="copy-code-btn">复制代码</span></code></pre>
<h5 data-id="heading-19">触发变更回调</h5>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">if</span> (!FLUSHING.get(editor)) &#123;
        <span class="hljs-comment">// 表示需要清空 operations</span>
        FLUSHING.set(editor, <span class="hljs-literal">true</span>)

        <span class="hljs-built_in">Promise</span>.resolve().then(<span class="hljs-function">() =></span> &#123;
           <span class="hljs-comment">// 清空完毕</span>
          FLUSHING.set(editor, <span class="hljs-literal">false</span>)
          <span class="hljs-comment">// 通知变更回调函数</span>
          editor.onChange()
          <span class="hljs-comment">// 清空 operations</span>
          editor.operations = []
        &#125;)
      &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-20">model 数据校验</h4>
<p>对 model 进行变更之后还需要对 model 进行数据校验，避免内容出错。数据校验的机制有两个重点，一是对 <code>dirtyPaths</code> 的管理，一个是 <code>withoutNormalizing</code> 机制。</p>
<h5 data-id="heading-21">withoutNormalizing</h5>
<p>你可以从 <a href="https://github.com/ianstormtaylor/slate/blob/main/packages/slate/src/interfaces/editor.ts#L1670" target="_blank" rel="nofollow noopener noreferrer">这里</a> 看到源码。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">export</span> <span class="hljs-keyword">const</span> Editor: EditorInterface = &#123;
  .....
  withoutNormalizing(editor: Editor, <span class="hljs-attr">fn</span>: <span class="hljs-function">() =></span> <span class="hljs-keyword">void</span>): <span class="hljs-keyword">void</span> &#123;
    <span class="hljs-keyword">const</span> value = Editor.isNormalizing(editor)
    NORMALIZING.set(editor, <span class="hljs-literal">false</span>)
    <span class="hljs-keyword">try</span> &#123;
      fn()
    &#125; <span class="hljs-keyword">finally</span> &#123;
      NORMALIZING.set(editor, value)
    &#125;
    Editor.normalize(editor)
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">export</span> <span class="hljs-keyword">const</span> NORMALIZING: <span class="hljs-built_in">WeakMap</span><Editor, boolean> = <span class="hljs-keyword">new</span> <span class="hljs-built_in">WeakMap</span>()
<span class="copy-code-btn">复制代码</span></code></pre>
<p>可以看到这段代码通过 <code>WeakMap</code> 保存了是否需要数据校验的状态。</p>
<h5 data-id="heading-22">dirtyPaths</h5>
<p>dirtyPaths 通过 editor.apply 方法形成</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> set = <span class="hljs-keyword">new</span> <span class="hljs-built_in">Set</span>()
<span class="hljs-keyword">const</span> dirtyPaths: Path[] = []
<span class="hljs-keyword">const</span> add = <span class="hljs-function">(<span class="hljs-params">path: Path | <span class="hljs-literal">null</span></span>) =></span> &#123;
        <span class="hljs-keyword">if</span> (path) &#123;
          <span class="hljs-keyword">const</span> key = path.join(<span class="hljs-string">','</span>)

          <span class="hljs-keyword">if</span> (!set.has(key)) &#123;
            set.add(key)
            dirtyPaths.push(path)
          &#125;
        &#125;
      &#125;
<span class="hljs-keyword">const</span> oldDirtyPaths = DIRTY_PATHS.get(editor) || []
<span class="hljs-keyword">const</span> newDirtyPaths = getDirtyPaths(op)

<span class="hljs-keyword">for</span> (<span class="hljs-keyword">const</span> path <span class="hljs-keyword">of</span> oldDirtyPaths) &#123;
        <span class="hljs-keyword">const</span> newPath = Path.transform(path, op)
        add(newPath)
&#125;

<span class="hljs-keyword">for</span> (<span class="hljs-keyword">const</span> path <span class="hljs-keyword">of</span> newDirtyPaths) &#123;
        add(path)
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><code>Editor.normalize(editor)</code> 的 normalize 方法，它创建一个循环，从 model 树的叶节点自底向上地不断获取<code>脏路径</code>并调用 nomalizeNode 检验路径所对应的节点是否合法。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">export</span> <span class="hljs-keyword">const</span> Editor: EditorInterface = &#123;
  .....
  
  normalize(
    editor: Editor,
    <span class="hljs-attr">options</span>: &#123;
      force?: boolean
    &#125; = &#123;&#125;
  ): <span class="hljs-keyword">void</span> &#123;
    ....

    Editor.withoutNormalizing(editor, <span class="hljs-function">() =></span> &#123;
      
      .....

      <span class="hljs-keyword">const</span> max = getDirtyPaths(editor).length * <span class="hljs-number">42</span> <span class="hljs-comment">// <span class="hljs-doctag">HACK:</span> better way?</span>
      <span class="hljs-keyword">let</span> m = <span class="hljs-number">0</span>

      <span class="hljs-keyword">while</span> (getDirtyPaths(editor).length !== <span class="hljs-number">0</span>) &#123;
        <span class="hljs-keyword">if</span> (m > max) &#123;
          <span class="hljs-keyword">throw</span> <span class="hljs-keyword">new</span> <span class="hljs-built_in">Error</span>(<span class="hljs-string">`
            Could not completely normalize the editor after <span class="hljs-subst">$&#123;max&#125;</span> iterations! This is usually due to incorrect normalization logic that leaves a node in an invalid state.
          `</span>)
        &#125;

        <span class="hljs-keyword">const</span> dirtyPath = getDirtyPaths(editor).pop()!

        <span class="hljs-comment">// If the node doesn't exist in the tree, it does not need to be normalized.</span>
        <span class="hljs-keyword">if</span> (Node.has(editor, dirtyPath)) &#123;
          <span class="hljs-keyword">const</span> entry = Editor.node(editor, dirtyPath)
          editor.normalizeNode(entry)
        &#125;
        m++
      &#125;
    &#125;)
  &#125;,
  .....
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>简图</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/c608c7b6c1b345a49d76a7d13082f3de~tplv-k3u1fbpfcp-watermark.image" alt="未命名绘图 (18).png" loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-23">Slate.js 插件体系</h2>
<p>Slate 的插件只是一个返回 editor 实例的函数，在这个函数中通过重写编辑器实例方法，修改编辑器行为。 在创建编辑器实例的时候调用插件函数即可。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> withImages = <span class="hljs-function"><span class="hljs-params">editor</span> =></span> &#123;
  <span class="hljs-keyword">const</span> &#123; isVoid &#125; = editor

  editor.isVoid = <span class="hljs-function"><span class="hljs-params">element</span> =></span> &#123;
    <span class="hljs-keyword">return</span> element.type === <span class="hljs-string">'image'</span> ? <span class="hljs-literal">true</span> : isVoid(element)
  &#125;

  <span class="hljs-keyword">return</span> editor
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>然后可以这样使用它:</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">import</span> &#123; createEditor &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'slate'</span>

<span class="hljs-keyword">const</span> editor = withImages(createEditor())
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-24">slate-history</h2>
<p><code>slate-history</code> 踪随着时间推移对 Slate 值状态的更改，并启用撤消和重做功能。</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/3a3da3614c74448d871862cb95527889~tplv-k3u1fbpfcp-watermark.image" alt="截屏2021-06-05 下午6.12.00.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-25">withHistory</h3>
<p>你可以从 <a href="https://github.com/ianstormtaylor/slate/blob/main/packages/slate-history/src/with-history.ts#L15" target="_blank" rel="nofollow noopener noreferrer">这里</a> 看到源码。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">export</span> <span class="hljs-keyword">const</span> withHistory = <span class="xml"><span class="hljs-tag"><<span class="hljs-name">T</span> <span class="hljs-attr">extends</span> <span class="hljs-attr">Editor</span>></span>(editor: T) => &#123;
  const e = editor as T & HistoryEditor
  const &#123; apply &#125; = e
  e.history = &#123; undos: [], redos: [] &#125;

  e.redo = () => &#123;
    const &#123; history &#125; = e
    const &#123; redos &#125; = history

    if (redos.length > 0) &#123;
      const batch = redos[redos.length - 1]

      HistoryEditor.withoutSaving(e, () => &#123;
        Editor.withoutNormalizing(e, () => &#123;
          for (const op of batch) &#123;
            e.apply(op)
          &#125;
        &#125;)
      &#125;)

      history.redos.pop()
      history.undos.push(batch)
    &#125;
  &#125;

  e.undo = () => &#123;
    const &#123; history &#125; = e
    const &#123; undos &#125; = history

    if (undos.length > 0) &#123;
      const batch = undos[undos.length - 1]

      HistoryEditor.withoutSaving(e, () => &#123;
        Editor.withoutNormalizing(e, () => &#123;
          const inverseOps = batch.map(Operation.inverse).reverse()

          for (const op of inverseOps) &#123;
            e.apply(op)
          &#125;
        &#125;)
      &#125;)

      history.redos.push(batch)
      history.undos.pop()
    &#125;
  &#125;

  e.apply = (op: Operation) => &#123;
    const &#123; operations, history &#125; = e
    const &#123; undos &#125; = history
    const lastBatch = undos[undos.length - 1]
    const lastOp = lastBatch && lastBatch[lastBatch.length - 1]
    const overwrite = shouldOverwrite(op, lastOp)
    let save = HistoryEditor.isSaving(e)
    let merge = HistoryEditor.isMerging(e)

    if (save == null) &#123;
      save = shouldSave(op, lastOp)
    &#125;

    if (save) &#123;
      if (merge == null) &#123;
        if (lastBatch == null) &#123;
          merge = false
        &#125; else if (operations.length !== 0) &#123;
          merge = true
        &#125; else &#123;
          merge = shouldMerge(op, lastOp) || overwrite
        &#125;
      &#125;

      if (lastBatch && merge) &#123;
        if (overwrite) &#123;
          lastBatch.pop()
        &#125;

        lastBatch.push(op)
      &#125; else &#123;
        const batch = [op]
        undos.push(batch)
      &#125;

      while (undos.length > 100) &#123;
        undos.shift()
      &#125;

      if (shouldClear(op)) &#123;
        history.redos = []
      &#125;
    &#125;

    apply(op)
  &#125;

  return e
&#125;
</span><span class="copy-code-btn">复制代码</span></code></pre>
<p>在 <code>withHistory</code> 方法中，slate-history 在 editor 上创建了两个数组用来存储历史操作：</p>
<pre><code class="hljs language-js copyable" lang="js">e.history = &#123; <span class="hljs-attr">undos</span>: [], <span class="hljs-attr">redos</span>: [] &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>它们的类型都是 Operation[][]，即 Operation 的二维数组，其中的每一项代表了一批操作（在代码上称作 batch）， <code>batch</code> 可含有多个 Operation。</p>
<p>slate-history 通过覆写 apply 方法来在 Operation 的 apply 流程之前插入 undo/redo 的相关逻辑，最后调用原来的 apply 方法。</p>
<pre><code class="hljs language-js copyable" lang="js"> e.apply = <span class="hljs-function">(<span class="hljs-params">op: Operation</span>) =></span> &#123;
    <span class="hljs-keyword">const</span> &#123; operations, history &#125; = e
    <span class="hljs-keyword">const</span> &#123; undos &#125; = history
    <span class="hljs-keyword">const</span> lastBatch = undos[undos.length - <span class="hljs-number">1</span>]
    <span class="hljs-keyword">const</span> lastOp = lastBatch && lastBatch[lastBatch.length - <span class="hljs-number">1</span>]
    <span class="hljs-keyword">const</span> overwrite = shouldOverwrite(op, lastOp)
    <span class="hljs-keyword">let</span> save = HistoryEditor.isSaving(e)
    <span class="hljs-keyword">let</span> merge = HistoryEditor.isMerging(e)

    <span class="hljs-keyword">if</span> (save == <span class="hljs-literal">null</span>) &#123;
      save = shouldSave(op, lastOp)
    &#125;

    <span class="hljs-keyword">if</span> (save) &#123;
      <span class="hljs-keyword">if</span> (merge == <span class="hljs-literal">null</span>) &#123;
        <span class="hljs-keyword">if</span> (lastBatch == <span class="hljs-literal">null</span>) &#123;
          merge = <span class="hljs-literal">false</span>
        &#125; <span class="hljs-keyword">else</span> <span class="hljs-keyword">if</span> (operations.length !== <span class="hljs-number">0</span>) &#123;
          merge = <span class="hljs-literal">true</span>
        &#125; <span class="hljs-keyword">else</span> &#123;
          merge = shouldMerge(op, lastOp) || overwrite
        &#125;
      &#125;

      <span class="hljs-keyword">if</span> (lastBatch && merge) &#123;
        <span class="hljs-keyword">if</span> (overwrite) &#123;
          lastBatch.pop()
        &#125;

        lastBatch.push(op)
      &#125; <span class="hljs-keyword">else</span> &#123;
        <span class="hljs-keyword">const</span> batch = [op]
        undos.push(batch)
      &#125;

      <span class="hljs-keyword">while</span> (undos.length > <span class="hljs-number">100</span>) &#123;
        undos.shift()
      &#125;

      <span class="hljs-keyword">if</span> (shouldClear(op)) &#123;
        history.redos = []
      &#125;
    &#125;

    apply(op)
  &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-26">undo 方法</h3>
<pre><code class="hljs language-js copyable" lang="js">e.undo = <span class="hljs-function">() =></span> &#123;
  <span class="hljs-keyword">const</span> &#123; history &#125; = e
  <span class="hljs-keyword">const</span> &#123; undos &#125; = history

  <span class="hljs-keyword">if</span> (undos.length > <span class="hljs-number">0</span>) &#123;
    <span class="hljs-keyword">const</span> batch = undos[undos.length - <span class="hljs-number">1</span>]

    HistoryEditor.withoutSaving(e, <span class="hljs-function">() =></span> &#123;
      Editor.withoutNormalizing(e, <span class="hljs-function">() =></span> &#123;
        <span class="hljs-keyword">const</span> inverseOps = batch.map(Operation.inverse).reverse()

        <span class="hljs-keyword">for</span> (<span class="hljs-keyword">const</span> op <span class="hljs-keyword">of</span> inverseOps) &#123;
          <span class="hljs-comment">// If the final operation is deselecting the editor, skip it. This is</span>
          <span class="hljs-keyword">if</span> (
            op === inverseOps[inverseOps.length - <span class="hljs-number">1</span>] &&
            op.type === <span class="hljs-string">'set_selection'</span> &&
            op.newProperties == <span class="hljs-literal">null</span>
          ) &#123;
            <span class="hljs-keyword">continue</span>
          &#125; <span class="hljs-keyword">else</span> &#123;
            e.apply(op)
          &#125;
        &#125;
      &#125;)
    &#125;)

    history.redos.push(batch)
    history.undos.pop()
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-27">redo 方法</h3>
<pre><code class="hljs language-js copyable" lang="js">e.redo = <span class="hljs-function">() =></span> &#123;
    <span class="hljs-keyword">const</span> &#123; history &#125; = e
    <span class="hljs-keyword">const</span> &#123; redos &#125; = history

    <span class="hljs-keyword">if</span> (redos.length > <span class="hljs-number">0</span>) &#123;
      <span class="hljs-keyword">const</span> batch = redos[redos.length - <span class="hljs-number">1</span>]

      HistoryEditor.withoutSaving(e, <span class="hljs-function">() =></span> &#123;
        Editor.withoutNormalizing(e, <span class="hljs-function">() =></span> &#123;
          <span class="hljs-keyword">for</span> (<span class="hljs-keyword">const</span> op <span class="hljs-keyword">of</span> batch) &#123;
            e.apply(op)
          &#125;
        &#125;)
      &#125;)

      history.redos.pop()
      history.undos.push(batch)
    &#125;
  &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-28">slate-react</h2>
<p><code>slate-react</code> 编辑器的 React 组件，渲染文档数据。</p>
<h3 data-id="heading-29">渲染原理</h3>
<p>Slate 的文档数据是一颗类似 DOM 的节点树结构，slate-react 通过递归这颗树生成 children 数组 ， 最终 react 将 children 数组中的组件渲染到页面上。</p>
<ul>
<li>设置编辑器实例的 children 属性</li>
</ul>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// https://github.com/ianstormtaylor/slate/blob/main/packages/slate-react/src/components/slate.tsx#L17</span>

<span class="hljs-keyword">export</span> <span class="hljs-keyword">const</span> Slate = <span class="hljs-function">(<span class="hljs-params">props: &#123;
  editor: ReactEditor
  value: Descendant[]
  children: React.ReactNode
  onChange: (value: Descendant[]) => <span class="hljs-keyword">void</span>
&#125;</span>) =></span> &#123;
  ....
  <span class="hljs-keyword">const</span> context: [ReactEditor] = useMemo(<span class="hljs-function">() =></span> &#123;
    <span class="hljs-comment">// 设置 editor 实例的 children 属性为 value</span>
    editor.children = value
    .....
  &#125;, [key, value, ...Object.values(rest)])
  
  .....
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>Editable 组件传递 editor 实例给 useChildren Hooks 组件。</li>
</ul>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// https://github.com/ianstormtaylor/slate/blob/main/packages/slate-react/src/components/editable.tsx#L100</span>

<span class="hljs-keyword">export</span> <span class="hljs-keyword">const</span> Editable = <span class="hljs-function">(<span class="hljs-params">props: EditableProps</span>) =></span> &#123;
 <span class="hljs-keyword">const</span> editor = useSlate()
 ....
 <span class="hljs-keyword">return</span> (
  <span class="xml"><span class="hljs-tag"><<span class="hljs-name">ReadOnlyContext.Provider</span> <span class="hljs-attr">value</span>=<span class="hljs-string">&#123;readOnly&#125;</span>></span>
   <span class="hljs-tag"><<span class="hljs-name">DecorateContext.Provider</span> <span class="hljs-attr">value</span>=<span class="hljs-string">&#123;decorate&#125;</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">Component</span>
    <span class="hljs-attr">....</span>
    ></span>
    &#123;useChildren(&#123;
            decorations,
            node: editor,
            renderElement,
            renderPlaceholder,
            renderLeaf,
            selection: editor.selection,
          &#125;)&#125;
     <span class="hljs-tag"></<span class="hljs-name">Component</span>></span>
    <span class="hljs-tag"></<span class="hljs-name">DecorateContext.Provider</span>></span>
   <span class="hljs-tag"></<span class="hljs-name">ReadOnlyContext.Provider</span>></span></span>
 )
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>useChildren 生成渲染数组，交给 React 渲染组件。</li>
</ul>
<p><code>useChildren</code> 组件会根据 children 中各个 Node 的类型，生成对应的 <code>ElementComponent</code> 或者 <code>TextComponent</code>。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> useChildren = <span class="hljs-function">(<span class="hljs-params">props: &#123;
  decorations: Range[]
  node: Ancestor
  renderElement?: (props: RenderElementProps) => JSX.Element
  renderPlaceholder: (props: RenderPlaceholderProps) => JSX.Element
  renderLeaf?: (props: RenderLeafProps) => JSX.Element
  selection: Range | <span class="hljs-literal">null</span>
&#125;</span>) =></span> &#123;
  <span class="hljs-keyword">const</span> decorate = useDecorate()
  <span class="hljs-keyword">const</span> editor = useSlateStatic()
  <span class="hljs-keyword">const</span> path = ReactEditor.findPath(editor, node)
  <span class="hljs-keyword">const</span> children = []
  <span class="hljs-keyword">const</span> isLeafBlock =
    Element.isElement(node) &&
    !editor.isInline(node) &&
    Editor.hasInlines(editor, node)

  <span class="hljs-keyword">for</span> (<span class="hljs-keyword">let</span> i = <span class="hljs-number">0</span>; i < node.children.length; i++) &#123;
    <span class="hljs-keyword">const</span> p = path.concat(i)
    <span class="hljs-keyword">const</span> n = node.children[i] <span class="hljs-keyword">as</span> Descendant
    <span class="hljs-keyword">const</span> key = ReactEditor.findKey(editor, n)
    <span class="hljs-keyword">const</span> range = Editor.range(editor, p)
    <span class="hljs-keyword">const</span> sel = selection && Range.intersection(range, selection)
    <span class="hljs-keyword">const</span> ds = decorate([n, p])

    <span class="hljs-keyword">for</span> (<span class="hljs-keyword">const</span> dec <span class="hljs-keyword">of</span> decorations) &#123;
      <span class="hljs-keyword">const</span> d = Range.intersection(dec, range)

      <span class="hljs-keyword">if</span> (d) &#123;
        ds.push(d)
      &#125;
    &#125;

    <span class="hljs-keyword">if</span> (Element.isElement(n)) &#123;
      children.push(
        <span class="xml"><span class="hljs-tag"><<span class="hljs-name">ElementComponent</span>
          <span class="hljs-attr">decorations</span>=<span class="hljs-string">&#123;ds&#125;</span>
          <span class="hljs-attr">element</span>=<span class="hljs-string">&#123;n&#125;</span>
          <span class="hljs-attr">key</span>=<span class="hljs-string">&#123;key.id&#125;</span>
          <span class="hljs-attr">renderElement</span>=<span class="hljs-string">&#123;renderElement&#125;</span>
          <span class="hljs-attr">renderPlaceholder</span>=<span class="hljs-string">&#123;renderPlaceholder&#125;</span>
          <span class="hljs-attr">renderLeaf</span>=<span class="hljs-string">&#123;renderLeaf&#125;</span>
          <span class="hljs-attr">selection</span>=<span class="hljs-string">&#123;sel&#125;</span>
        /></span></span>
      )
    &#125; <span class="hljs-keyword">else</span> &#123;
      children.push(
        <span class="xml"><span class="hljs-tag"><<span class="hljs-name">TextComponent</span>
          <span class="hljs-attr">decorations</span>=<span class="hljs-string">&#123;ds&#125;</span>
          <span class="hljs-attr">key</span>=<span class="hljs-string">&#123;key.id&#125;</span>
          <span class="hljs-attr">isLast</span>=<span class="hljs-string">&#123;isLeafBlock</span> && <span class="hljs-attr">i</span> === <span class="hljs-string">node.children.length</span> <span class="hljs-attr">-</span> <span class="hljs-attr">1</span>&#125;
          <span class="hljs-attr">parent</span>=<span class="hljs-string">&#123;node&#125;</span>
          <span class="hljs-attr">renderPlaceholder</span>=<span class="hljs-string">&#123;renderPlaceholder&#125;</span>
          <span class="hljs-attr">renderLeaf</span>=<span class="hljs-string">&#123;renderLeaf&#125;</span>
          <span class="hljs-attr">text</span>=<span class="hljs-string">&#123;n&#125;</span>
        /></span></span>
      )
    &#125;

    NODE_TO_INDEX.set(n, i)
    NODE_TO_PARENT.set(n, node)
  &#125;

  <span class="hljs-keyword">return</span> children
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/bd977034381f4041938c27b172851925~tplv-k3u1fbpfcp-watermark.image" alt="未命名绘图 (19).png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>官网例子</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/aa7c9be977784babbb596500dfaf5c41~tplv-k3u1fbpfcp-watermark.image" alt="截屏2021-06-05 下午7.58.40.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-30">自定义渲染</h3>
<p>传递渲染函数 <code>renderElement</code> 和 <code>renderLeaf</code> 给 Editable 组件，用户可以通过提供这两个参数来自行决定如何渲染 model 中的一个 Node。我们以官网 <a href="https://github.com/ianstormtaylor/slate/blob/main/site/examples/richtext.tsx#L44" target="_blank" rel="nofollow noopener noreferrer">richtext demo</a> 为例。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> RichTextExample = <span class="hljs-function">() =></span> &#123;
  ...
  <span class="hljs-keyword">const</span> renderElement = useCallback(<span class="hljs-function"><span class="hljs-params">props</span> =></span> <span class="xml"><span class="hljs-tag"><<span class="hljs-name">Element</span> &#123;<span class="hljs-attr">...props</span>&#125; /></span></span>, [])
  <span class="hljs-keyword">const</span> renderLeaf = useCallback(<span class="hljs-function"><span class="hljs-params">props</span> =></span> <span class="xml"><span class="hljs-tag"><<span class="hljs-name">Leaf</span> &#123;<span class="hljs-attr">...props</span>&#125; /></span></span>, [])
  
    <span class="hljs-keyword">return</span> (
    <span class="xml"><span class="hljs-tag"><<span class="hljs-name">Slate</span> <span class="hljs-attr">editor</span>=<span class="hljs-string">&#123;editor&#125;</span> <span class="hljs-attr">value</span>=<span class="hljs-string">&#123;value&#125;</span> <span class="hljs-attr">onChange</span>=<span class="hljs-string">&#123;value</span> =></span> setValue(value)&#125;>
       ....
      <span class="hljs-tag"><<span class="hljs-name">Editable</span>
        <span class="hljs-attr">renderElement</span>=<span class="hljs-string">&#123;renderElement&#125;</span>
        <span class="hljs-attr">renderLeaf</span>=<span class="hljs-string">&#123;renderLeaf&#125;</span>
        <span class="hljs-attr">.....</span>
      /></span>
    <span class="hljs-tag"></<span class="hljs-name">Slate</span>></span></span>
  )
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="hljs language-js copyable" lang="js"> <span class="hljs-keyword">const</span> Element = <span class="hljs-function">(<span class="hljs-params">&#123; attributes, children, element &#125;</span>) =></span> &#123;
  <span class="hljs-keyword">switch</span> (element.type) &#123;
    <span class="hljs-keyword">case</span> <span class="hljs-string">'block-quote'</span>:
      <span class="hljs-keyword">return</span> <span class="xml"><span class="hljs-tag"><<span class="hljs-name">blockquote</span> &#123;<span class="hljs-attr">...attributes</span>&#125;></span>&#123;children&#125;<span class="hljs-tag"></<span class="hljs-name">blockquote</span>></span></span>
    <span class="hljs-keyword">case</span> <span class="hljs-string">'bulleted-list'</span>:
      <span class="hljs-keyword">return</span> <span class="xml"><span class="hljs-tag"><<span class="hljs-name">ul</span> &#123;<span class="hljs-attr">...attributes</span>&#125;></span>&#123;children&#125;<span class="hljs-tag"></<span class="hljs-name">ul</span>></span></span>
    <span class="hljs-keyword">case</span> <span class="hljs-string">'heading-one'</span>:
      <span class="hljs-keyword">return</span> <span class="xml"><span class="hljs-tag"><<span class="hljs-name">h1</span> &#123;<span class="hljs-attr">...attributes</span>&#125;></span>&#123;children&#125;<span class="hljs-tag"></<span class="hljs-name">h1</span>></span></span>
    <span class="hljs-keyword">case</span> <span class="hljs-string">'heading-two'</span>:
      <span class="hljs-keyword">return</span> <span class="xml"><span class="hljs-tag"><<span class="hljs-name">h2</span> &#123;<span class="hljs-attr">...attributes</span>&#125;></span>&#123;children&#125;<span class="hljs-tag"></<span class="hljs-name">h2</span>></span></span>
    <span class="hljs-keyword">case</span> <span class="hljs-string">'list-item'</span>:
      <span class="hljs-keyword">return</span> <span class="xml"><span class="hljs-tag"><<span class="hljs-name">li</span> &#123;<span class="hljs-attr">...attributes</span>&#125;></span>&#123;children&#125;<span class="hljs-tag"></<span class="hljs-name">li</span>></span></span>
    <span class="hljs-keyword">case</span> <span class="hljs-string">'numbered-list'</span>:
      <span class="hljs-keyword">return</span> <span class="xml"><span class="hljs-tag"><<span class="hljs-name">ol</span> &#123;<span class="hljs-attr">...attributes</span>&#125;></span>&#123;children&#125;<span class="hljs-tag"></<span class="hljs-name">ol</span>></span></span>
    <span class="hljs-keyword">default</span>:
      <span class="hljs-keyword">return</span> <span class="xml"><span class="hljs-tag"><<span class="hljs-name">p</span> &#123;<span class="hljs-attr">...attributes</span>&#125;></span>&#123;children&#125;<span class="hljs-tag"></<span class="hljs-name">p</span>></span></span>
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这个 demo 就拓展了 Element 节点的 <code>type</code> 属性，让 <code>Element</code> 能够渲染为不同的标签。</p>
<h2 data-id="heading-31">slate-hyperscript</h2>
<p><code>slate-hyperscript</code> 使用 JSX 编写 Slate 文档的 hyperscript 工具。</p>
<h2 data-id="heading-32">总结</h2>
<ol>
<li>Slate 目前处于测试状态，它的一些 APIs 还没有 "最终确定"；</li>
<li>使用了 contenteditable 导致无法处理部分选区和输入事件；</li>
</ol>
<h2 data-id="heading-33">参考资料</h2>
<p><a href="https://rain120.github.io/athena/zh/slate/SlateStart.html" target="_blank" rel="nofollow noopener noreferrer">Slate 中文文档</a></p>
<p><a href="https://zhuanlan.zhihu.com/p/262209236" target="_blank" rel="nofollow noopener noreferrer">slate 架构设计分析</a></p></div>  
</div>
            