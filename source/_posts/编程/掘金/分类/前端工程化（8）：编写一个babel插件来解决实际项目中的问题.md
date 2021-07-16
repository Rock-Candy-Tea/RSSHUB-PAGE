
---
title: '前端工程化（8）：编写一个babel插件来解决实际项目中的问题'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/9472c376162d4b8eaad0c9ff804e5603~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Fri, 16 Jul 2021 01:28:49 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/9472c376162d4b8eaad0c9ff804e5603~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>在笔者的上一篇文章<a href="https://juejin.cn/post/6976501655302832159" target="_blank" title="https://juejin.cn/post/6976501655302832159">前端工程化（7）：你所需要知道的最新的babel兼容性实现方案</a>中剖析了在实际项目中如何使用<code>babel</code>提供的原生转译能力，得益于<code>babel</code>强大的转译能力我们无需再担心项目的兼容性问题。但是<code>babel</code>不只是一款帮助我们处理代码兼容性的工具，我们还可以借助它的插件化能力完成日常工作中一些重复、繁琐的工作。本文将笔者从在实际项目中碰到的问题而萌生用<code>babel</code>来解决的想法，到一个完整的<code>babel</code>插件的落地过程做了个总结，向大家展示在面对实际项目中的某些问题时用<code>babel</code>插件来解决有多香！！</p>
<h2 data-id="heading-0">1. 实际项目中出现的问题</h2>
<p>项目中会经常用到<code>element-ui</code>中的<a href="https://link.juejin.cn/?target=https%3A%2F%2Felement.eleme.cn%2F%23%2Fzh-CN%2Fcomponent%2Fmessage-box%23que-ren-xiao-xi" target="_blank" rel="nofollow noopener noreferrer" title="https://element.eleme.cn/#/zh-CN/component/message-box#que-ren-xiao-xi" ref="nofollow noopener noreferrer">$confirm</a>来提示用户进行二次确认，比如在进行删除操作时应当都唤出是否确认删除的提示：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript">handleDelete (row) &#123;
  <span class="hljs-built_in">this</span>.$confirm(<span class="hljs-string">'是否删除该条数据?'</span>, <span class="hljs-string">'提示'</span>, &#123;
    <span class="hljs-attr">type</span>: <span class="hljs-string">'warning'</span>
  &#125;).then(<span class="hljs-keyword">async</span> () => &#123;
    <span class="hljs-built_in">this</span>.loading = <span class="hljs-literal">true</span>
    <span class="hljs-keyword">const</span> res = <span class="hljs-keyword">await</span> <span class="hljs-built_in">this</span>.$delete(<span class="hljs-string">'/api/xx'</span>, &#123; <span class="hljs-attr">id</span>: row.id &#125;)
    <span class="hljs-keyword">if</span> (!res) <span class="hljs-keyword">return</span>
    <span class="hljs-keyword">await</span> <span class="hljs-built_in">this</span>.loadList()
    <span class="hljs-built_in">this</span>.$message(&#123;
      <span class="hljs-attr">type</span>: <span class="hljs-string">'success'</span>,
      <span class="hljs-attr">message</span>: <span class="hljs-string">'删除成功!'</span>
    &#125;)
  &#125;)
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>上面是我们团队统一约定的删除逻辑编写方式。这么写没啥大问题，但是当我们取消二次确认弹框的时候，浏览器会提示错误：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/9472c376162d4b8eaad0c9ff804e5603~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>这个错误想必大家也并不陌生，就是<code>promise</code>错误没有捕捉。是的，因为我们没有写<code>catch</code>，因为我们觉得没有什么必要的逻辑要在取消的时候触发（包括提示取消删除之类的）。</p>
<p>虽然这个错误对程序运行没有影响，<strong>但是对不熟悉的开发人员定位错误以及错误监控系统都会造成多余的困扰</strong>。我们也不好改组件源码，只好强制要求团队成员在每个<code>$confirm</code>后面手动加上<code>catch</code>逻辑：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript">handleDelete (row) &#123;
  <span class="hljs-built_in">this</span>.$confirm(<span class="hljs-string">'是否删除该条数据?'</span>, <span class="hljs-string">'提示'</span>, &#123;
    <span class="hljs-attr">type</span>: <span class="hljs-string">'warning'</span>
  &#125;).then(<span class="hljs-keyword">async</span> () => &#123;
    <span class="hljs-built_in">this</span>.loading = <span class="hljs-literal">true</span>
    <span class="hljs-keyword">const</span> res = <span class="hljs-keyword">await</span> <span class="hljs-built_in">this</span>.$delete(<span class="hljs-string">'/api/xx'</span>, &#123; <span class="hljs-attr">id</span>: row.id &#125;)
    <span class="hljs-keyword">if</span> (!res) <span class="hljs-keyword">return</span>
    <span class="hljs-keyword">await</span> <span class="hljs-built_in">this</span>.loadList()
    <span class="hljs-built_in">this</span>.$message(&#123;
      <span class="hljs-attr">type</span>: <span class="hljs-string">'success'</span>,
      <span class="hljs-attr">message</span>: <span class="hljs-string">'删除成功!'</span>
    &#125;);
  &#125;).catch(<span class="hljs-function"><span class="hljs-params">err</span> =></span> err)
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>代码中充斥着大量的使用<code>$confirm</code>的逻辑，如果靠人力去手动解决这种重复性的问题，一方面增加了工作量，另一方面不能避免会有团队成员疏忽。</p>
<p>有位大佬曾说过：当你在做着一些重复性的工作时，那一定有别的办法来帮助你快速的完成它。这时脑子里就萌生了<strong>用<code>babel</code>插件来自动添加<code>catch</code>的想法</strong>...</p>
<h2 data-id="heading-1">2. 编写插件前的准备工作</h2>
<p>之所以萌生了用<code>babel</code>插件的想法，那是因为<code>babel</code>是从底层将我们代码解析成<code>AST</code>树，然后对<code>AST</code>树的节点进行递归遍历，在遍历的过程中，如果有插件则会执行插件中的逻辑对节点进行增删改，最后将修改过的<code>AST</code>树再生成代码，从而实现代码的修改。所以，在编写插件前，我们首先要分析对应代码的<code>AST</code>树结构，以及插件的运作方式。</p>
<h3 data-id="heading-2">2.1 AST 树结构分析</h3>
<p>首先需要借助<a href="https://link.juejin.cn/?target=https%3A%2F%2Fastexplorer.net%2F" target="_blank" rel="nofollow noopener noreferrer" title="https://astexplorer.net/" ref="nofollow noopener noreferrer">astexplorer</a>来分析原代码的<code>AST</code>树结构，以及目标代码的<code>AST</code>树结构。<strong>对比两者结构的差异，从而才能找到转换的切入点</strong>。</p>
<p>原代码的主结构为：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-built_in">this</span>.$confirm().then()
<span class="copy-code-btn">复制代码</span></code></pre>
<p>解析的AST树结构（简化）：</p>
<pre><code class="hljs language-json copyable" lang="json">&#123;
  <span class="hljs-attr">"type"</span>: <span class="hljs-string">"ExpressionStatement"</span>,
  <span class="hljs-attr">"expression"</span>: &#123;
    <span class="hljs-attr">"type"</span>: <span class="hljs-string">"CallExpression"</span>,
    <span class="hljs-attr">"callee"</span>: &#123;
      <span class="hljs-attr">"type"</span>: <span class="hljs-string">"MemberExpression"</span>,
      <span class="hljs-attr">"object"</span>: &#123;
        <span class="hljs-attr">"type"</span>: <span class="hljs-string">"CallExpression"</span>,
        <span class="hljs-attr">"callee"</span>: &#123;
          <span class="hljs-attr">"type"</span>: <span class="hljs-string">"MemberExpression"</span>,
          <span class="hljs-attr">"object"</span>: &#123;
            <span class="hljs-attr">"type"</span>: <span class="hljs-string">"ThisExpression"</span>
          &#125;,
          <span class="hljs-attr">"property"</span>: &#123;
            <span class="hljs-attr">"type"</span>: <span class="hljs-string">"Identifier"</span>,
            <span class="hljs-attr">"name"</span>: <span class="hljs-string">"$confirm"</span>
          &#125;
        &#125;,
        <span class="hljs-attr">"arguments"</span>: []
      &#125;,
      <span class="hljs-attr">"property"</span>: &#123;
        <span class="hljs-attr">"type"</span>: <span class="hljs-string">"Identifier"</span>
        <span class="hljs-string">"name"</span>: <span class="hljs-string">"then"</span>
      &#125;
    &#125;,
    <span class="hljs-attr">"arguments"</span>: []
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>目标代码的主结构为：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-built_in">this</span>.$confirm().then().catch()
<span class="copy-code-btn">复制代码</span></code></pre>
<p>解析的AST树结构（简化）：</p>
<pre><code class="hljs language-json copyable" lang="json">&#123;
  <span class="hljs-attr">"type"</span>: <span class="hljs-string">"ExpressionStatement"</span>,
  <span class="hljs-attr">"expression"</span>: &#123;
    <span class="hljs-attr">"type"</span>: <span class="hljs-string">"CallExpression"</span>,
    <span class="hljs-attr">"callee"</span>: &#123;
      <span class="hljs-attr">"type"</span>: <span class="hljs-string">"MemberExpression"</span>,
      <span class="hljs-attr">"object"</span>: &#123;
        <span class="hljs-attr">"type"</span>: <span class="hljs-string">"CallExpression"</span>,
        <span class="hljs-attr">"callee"</span>: &#123;
          <span class="hljs-attr">"type"</span>: <span class="hljs-string">"MemberExpression"</span>,
          <span class="hljs-attr">"object"</span>: &#123;
            <span class="hljs-attr">"type"</span>: <span class="hljs-string">"CallExpression"</span>,
            <span class="hljs-attr">"callee"</span>: &#123;
              <span class="hljs-attr">"type"</span>: <span class="hljs-string">"MemberExpression"</span>,
              <span class="hljs-attr">"object"</span>: &#123;
                <span class="hljs-attr">"type"</span>: <span class="hljs-string">"ThisExpression"</span>,
              &#125;,
              <span class="hljs-attr">"property"</span>: &#123;
                <span class="hljs-attr">"type"</span>: <span class="hljs-string">"Identifier"</span>,
                <span class="hljs-attr">"name"</span>: <span class="hljs-string">"$confirm"</span>
              &#125;
            &#125;,
            <span class="hljs-attr">"arguments"</span>: []
          &#125;,
          <span class="hljs-attr">"property"</span>: &#123;
            <span class="hljs-attr">"type"</span>: <span class="hljs-string">"Identifier"</span>,
            <span class="hljs-attr">"name"</span>: <span class="hljs-string">"then"</span>
          &#125;
        &#125;,
        <span class="hljs-attr">"arguments"</span>: []
      &#125;,
      <span class="hljs-attr">"property"</span>: &#123;
        <span class="hljs-attr">"type"</span>: <span class="hljs-string">"Identifier"</span>
        <span class="hljs-string">"name"</span>: <span class="hljs-string">"catch"</span>
      &#125;
    &#125;,
    <span class="hljs-attr">"arguments"</span>: []
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>关于<code>babel</code>是怎么将代码转换成<code>AST</code>树结构的在这里不再阐述，这里就大概分析下代码是如何跟<code>AST</code>树对应上的：</p>
<ul>
<li>
<p>首先，这行代码被称为表达式语句，所以这行代码的顶级节点的<code>type</code>就为<code>ExpressionStatement</code>（在<code>javascript</code>中，一行代码要么是表达式要么是声明，所以<code>AST</code>树的顶级节点类型要么是<code>Statement</code>要么是<code>Declaration</code>）。</p>
</li>
<li>
<p>其次，这行代码是个调用表达式，所以次级节点的<code>type</code>为<code>CallExpression</code>。这里的调用顺序的解析要注意，是<strong>从右往左</strong>依次解析的，可以理解为<code>「「「this.$confirm()」.then()」.catch()」</code>。</p>
</li>
<li>
<p>接着，这个调用表达式的被调用者是成员表达式，所以接下来的节点的<code>type</code>为<code>MemberExpression</code>，而成员表达式的访问的对象又是一个调用表达式，调用表达式的被调用者又是成员表达式，依次类推，一直解析到<code>this.$confirm</code>为止。</p>
</li>
</ul>
<p>我们可以看到，<code>this.$confirm.then().catch()</code>的树结构在<code>this.$confirm.then()</code>树结构的基础上多了一层调用表达式节点，被调用者是个成员表达式，而成员表达式的对象就是<code>this.$confirm.then()</code>最外层的调用表达式节点。</p>
<p>知道这个特征后，我们接下来就可以利用插件来完成转换。</p>
<h3 data-id="heading-3">2.1 babel 插件结构分析</h3>
<p>一个插件的基本结构如下所示：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-built_in">module</span>.exports = <span class="hljs-function">(<span class="hljs-params">&#123; types: t &#125;</span>) =></span> &#123;
  <span class="hljs-keyword">return</span> &#123;
    <span class="hljs-attr">visitor</span>: &#123;
      ...
    &#125;
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>可以看出，<code>babel</code>插件其实就是个函数，入参是<code>babel</code>对象，其中包含了<code>babel</code>所有的工具对象。最常用的是<code>types</code>工具对象，我们在编写插件的时候基本都需要依赖它提供的创建<code>AST</code>节点、验证<code>AST</code>节点的方法。</p>
<p>创建一个节点可以通过<code>types</code>调用该节点名称对应的方法：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript">t.identifier(<span class="hljs-string">'a'</span>)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>验证一个节点可以通过<code>types</code>调用<code>is</code> + 该节点名称对应的方法：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript">t.isIdentifier(node)
<span class="copy-code-btn">复制代码</span></code></pre>
<blockquote>
<p><code>types</code>对象实际上是<code>babel-types</code>包的映射。<code>AST</code>树节点类型众多，当你需要调用某个节点的校验和创建方法时，可以查阅<a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.babeljs.cn%2Fdocs%2Fbabel-types" target="_blank" rel="nofollow noopener noreferrer" title="https://www.babeljs.cn/docs/babel-types" ref="nofollow noopener noreferrer">babel-types</a>文档。</p>
</blockquote>
<p>插件函数最后会返回一个对象，对象里面定义一个<code>visitor</code>（访问者）属性。在<code>visitor</code>中可以定义你想要访问的节点类型，节点类型以函数的形式定义，这样当<code>AST</code>遍历到你想要访问的节点类型时，则会执行你定义的节点类型方法。比如你想要访问<code>CallExpression</code>类型节点，并对这节点做一些操作：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-built_in">module</span>.exports = <span class="hljs-function">(<span class="hljs-params">&#123; types: t &#125;</span>) =></span> &#123;
  <span class="hljs-keyword">return</span> &#123;
    <span class="hljs-attr">visitor</span>: &#123;
      CallExpression (path) &#123;
        <span class="hljs-comment">// do sth</span>
      &#125;
    &#125;
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>节点类型方法接收一个<code>path</code>（路径）参数，<code>path</code>表示两个节点之间连接的对象，<code>path</code>中存储着当前<code>AST</code>节点信息以及一些节点操作方法，列举几个常用的：</p>
<ul>
<li>
<p><code>path</code>中的属性:</p>
<ul>
<li><code>node</code> - 当前遍历到的节点信息</li>
<li><code>parent</code> - 当前遍历到的节点信息的父节点信息</li>
<li><code>parentPath</code> - 当前遍历到的节点的父节点路径</li>
<li><code>scope</code> - 作用域</li>
</ul>
</li>
<li>
<p><code>path</code>中的方法:</p>
<ul>
<li><code>findParent</code> - 找寻特定的父节点</li>
<li><code>getSibling</code> - 获取同级路径</li>
<li><code>getFunctionParent</code> - 获取包含该节点最近的父函数节点</li>
<li><code>getStatementParent</code> - 获取包含该节点最近的表达式节点</li>
<li><code>relaceWith</code> - 替换一个节点</li>
<li><code>relaceWithMultiple</code> - 用多节点替换单节点</li>
<li><code>insertBefore</code> - 在之前插入兄弟节点</li>
<li><code>insertAfter</code> - 在之后插入兄弟节点</li>
<li><code>remove</code> - 删除节点</li>
<li><code>pushContainer</code> - 将节点插入到容器中</li>
<li><code>stop</code> - 停止遍历</li>
<li><code>skip</code> - 跳过此次遍历</li>
</ul>
</li>
</ul>
<blockquote>
<p>具体使用可以查阅<a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fjamiebuilds%2Fbabel-handbook%2Fblob%2Fmaster%2Ftranslations%2Fzh-Hans%2Fplugin-handbook.md%23toc-transformation-operations" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/jamiebuilds/babel-handbook/blob/master/translations/zh-Hans/plugin-handbook.md#toc-transformation-operations" ref="nofollow noopener noreferrer">babel-handbook</a> 文档，建议仔细阅读。</p>
</blockquote>
<p><strong>当有一个节点类型方法的访问者时，实际上是在访问该节点的路径而非节点本身。我们对节点的操作也都是在操作路径，而不是节点本身</strong>。</p>
<p>所以，插件都是通过修改<code>path</code>对象来修改<code>AST</code>结构。我们只要合理运用<code>path</code>提供的属性和方法，再辅以<code>babel-types</code>提供的校验、创建节点能力，就可以简单的完成<code>AST</code>树节点的增删改。</p>
<h2 data-id="heading-4">3. 开始编写插件</h2>
<h3 data-id="heading-5">3.1 环境搭建</h3>
<p>我们需要搭建一个环境来方便开发、调试以及发布<code>babel</code>插件。首先安装几个<code>babel</code>的核心包：</p>
<pre><code class="hljs language-json copyable" lang="json"><span class="hljs-string">"devDependencies"</span>: &#123;
  <span class="hljs-attr">"@babel/cli"</span>: <span class="hljs-string">"^7.14.5"</span>,
  <span class="hljs-attr">"@babel/core"</span>: <span class="hljs-string">"^7.14.6"</span>,
  <span class="hljs-attr">"@babel/preset-env"</span>: <span class="hljs-string">"^7.14.7"</span>
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<blockquote>
<p>引入<code>@babel/preset-env</code>预设的目的一是为了将插件源码在打包时进行兼容性转换，二是为了在测试的时候模拟使用了<code>@babel/preset-env</code>预设的环境。</p>
</blockquote>
<p>新建文件夹<code>src</code>和<code>test</code>，<code>src</code>中存放插件源码，<code>test</code>中存放测试用例，然后配置打包和调试命令：</p>
<pre><code class="hljs language-json copyable" lang="json"><span class="hljs-string">"scripts"</span>: &#123;
  <span class="hljs-attr">"build"</span>: <span class="hljs-string">"rm -rf lib && babel src/index.js -d lib"</span>,
  <span class="hljs-attr">"test"</span>: <span class="hljs-string">"babel test/index.js -d test/compiled --watch"</span>
&#125;,
<span class="copy-code-btn">复制代码</span></code></pre>
<p>最后新建<code>babel.config.js</code>文件并配置<code>plugins</code>，该配置项是一个数组，表示<code>babel</code>需要加载的插件列表，我们将其指向自定义插件的路径就可以：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">var</span> config = &#123;
  <span class="hljs-attr">presets</span>: [
    [<span class="hljs-string">'@babel/preset-env'</span>]
  ]
&#125;
<span class="hljs-comment">// 执行 npm run test 时才启用插件</span>
<span class="hljs-keyword">if</span> (process.argv[<span class="hljs-number">2</span>].indexOf(<span class="hljs-string">'test'</span>) >= <span class="hljs-number">0</span>) &#123;
  config.plugins = [
    [<span class="hljs-string">"./src/index.js"</span>]
  ]
&#125;

<span class="hljs-built_in">module</span>.exports = config
<span class="copy-code-btn">复制代码</span></code></pre>
<p>调试时只需要事先在<code>test/index.js</code>文件中编写好几个测试用例，然后在<code>src/index.js</code>中编写插件逻辑，重新执行<code>npm run test</code>，最后在<code>test/compiled/index.js</code>文件中查看编译的结果即可。</p>
<h3 data-id="heading-6">3.2 逻辑编写</h3>
<p>插件的逻辑编写其实不难，关键是要找准我们应该访问哪种节点类型。对于<code>this.$confirm().then()</code>代码不难看出我们要访问的节点类型是<code>CallExpression</code>，然后通过<code>CallExpression</code>节点找到<code>this.$confirm</code>所在的节点，找到则继续往下执行，没有找到则提前退出：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-built_in">module</span>.exports = <span class="hljs-function">(<span class="hljs-params">&#123; types: t &#125;</span>) =></span> &#123;
  <span class="hljs-keyword">return</span> &#123;
    <span class="hljs-attr">visitor</span>: &#123;
      CallExpression (path) &#123;
        <span class="hljs-keyword">const</span> &#123; node &#125; = path
        <span class="hljs-keyword">if</span> (!(t.isMemberExpression(node.callee) && t.ThisExpression(node.callee.object) && t.isIdentifier(node.call.property, &#123; <span class="hljs-attr">name</span>: <span class="hljs-string">'$confirm'</span> &#125;))) &#123;
          <span class="hljs-keyword">return</span>
        &#125;
      &#125;
    &#125;
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>如果找到<code>this.$confirm</code>所在的节点，则沿着当前节点路径去搜寻父节点中是否有包含<code>catch</code>的节点，没找到则继续往下执行，找到的话则不做任何操作提前退出：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-built_in">module</span>.exports = <span class="hljs-function">(<span class="hljs-params">&#123; types: t &#125;</span>) =></span> &#123;
  <span class="hljs-keyword">return</span> &#123;
    <span class="hljs-attr">visitor</span>: &#123;
      CallExpression (path) &#123;
        <span class="hljs-keyword">const</span> &#123; node &#125; = path
        <span class="hljs-keyword">if</span> (!(t.isMemberExpression(node.callee) && t.ThisExpression(node.callee.object) && t.isIdentifier(node.call.property, &#123; <span class="hljs-attr">name</span>: <span class="hljs-string">'$confirm'</span> &#125;))) &#123;
          <span class="hljs-keyword">return</span>
        &#125;
        
        <span class="hljs-keyword">const</span> catchPath = path.findParent(<span class="hljs-function">(<span class="hljs-params">&#123; node &#125;</span>) =></span> &#123;
          <span class="hljs-keyword">return</span> t.isMemberExpression(node) && isObjectProperty(node.property, <span class="hljs-string">'catch'</span>)
        &#125;)
        <span class="hljs-keyword">if</span> (catchPath) &#123;
          <span class="hljs-keyword">return</span>
        &#125;
      &#125;
    &#125;
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>如果没有在父节点路劲中找到<code>catch</code>所在的节点，先获取最外层的<code>then</code>所在的节点做好构建新节点的准备：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-built_in">module</span>.exports = <span class="hljs-function">(<span class="hljs-params">&#123; types: t &#125;</span>) =></span> &#123;
  <span class="hljs-keyword">return</span> &#123;
    <span class="hljs-attr">visitor</span>: &#123;
      CallExpression (path) &#123;
        <span class="hljs-keyword">const</span> &#123; node &#125; = path
        <span class="hljs-keyword">if</span> (!(t.isMemberExpression(node.callee) && t.ThisExpression(node.callee.object) && t.isIdentifier(node.call.property, &#123; <span class="hljs-attr">name</span>: <span class="hljs-string">'$confirm'</span> &#125;))) &#123;
          <span class="hljs-keyword">return</span>
        &#125;
        
        <span class="hljs-keyword">const</span> catchPath = path.findParent(<span class="hljs-function">(<span class="hljs-params">&#123; node &#125;</span>) =></span> &#123;
          <span class="hljs-keyword">return</span> t.isMemberExpression(node) && isObjectProperty(node.property, <span class="hljs-string">'catch'</span>)
        &#125;)
        <span class="hljs-keyword">if</span> (catchPath) &#123;
          <span class="hljs-keyword">return</span>
        &#125;
        
        <span class="hljs-keyword">const</span> mostOuterThenPath = path.findParent(<span class="hljs-function"><span class="hljs-params">pPath</span> =></span> &#123;
          <span class="hljs-keyword">const</span> node = pPath.node
          <span class="hljs-keyword">return</span> t.isCallExpression(node) && isObjectProperty(node.callee.property, <span class="hljs-string">'then'</span>) && !t.isMemberExpression(pPath.parentPath.node)
        &#125;)
      &#125;
    &#125;
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这里获取最外层<code>then</code>所在节点的办法是判断当前节点的父节点是否是<code>MemberExpression</code>，如果不是则是最外层<code>then</code>所在的节点。</p>
<p>获取到最外层<code>then</code>所在的节点以后，就用它构建一个<code>callExpression</code>新节点，并替换掉它：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-built_in">module</span>.exports = <span class="hljs-function">(<span class="hljs-params">&#123; types: t &#125;</span>) =></span> &#123;
  <span class="hljs-keyword">return</span> &#123;
    <span class="hljs-attr">visitor</span>: &#123;
      CallExpression (path) &#123;
        <span class="hljs-keyword">const</span> &#123; node &#125; = path
        <span class="hljs-keyword">if</span> (!(t.isMemberExpression(node.callee) && t.ThisExpression(node.callee.object) && t.isIdentifier(node.call.property, &#123; <span class="hljs-attr">name</span>: <span class="hljs-string">'$confirm'</span> &#125;))) &#123;
          <span class="hljs-keyword">return</span>
        &#125;
        
        <span class="hljs-keyword">const</span> catchPath = path.findParent(<span class="hljs-function">(<span class="hljs-params">&#123; node &#125;</span>) =></span> &#123;
          <span class="hljs-keyword">return</span> t.isMemberExpression(node) && isObjectProperty(node.property, <span class="hljs-string">'catch'</span>)
        &#125;)
        <span class="hljs-keyword">if</span> (catchPath) &#123;
          <span class="hljs-keyword">return</span>
        &#125;
        
        <span class="hljs-keyword">const</span> mostOuterThenPath = path.findParent(<span class="hljs-function"><span class="hljs-params">pPath</span> =></span> &#123;
          <span class="hljs-keyword">const</span> node = pPath.node
          <span class="hljs-keyword">return</span> t.isCallExpression(node) && isObjectProperty(node.callee.property, <span class="hljs-string">'then'</span>) && !t.isMemberExpression(pPath.parentPath.node)
        &#125;)
        
        <span class="hljs-keyword">const</span> arrowFunctionNode = t.arrowFunctionExpression(
          [t.identifier(<span class="hljs-string">'err'</span>)],
          t.identifier(<span class="hljs-string">'err'</span>)
        )

        <span class="hljs-keyword">const</span> newNode = t.callExpression(
          t.memberExpression(
            mostOuterThenPath.node,
            t.identifier(<span class="hljs-string">'catch'</span>)
          ),
          [arrowFunctionNode]
        )

        mostOuterThenPath.replaceWith(newNode)
      &#125;
    &#125;
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>完成上述<code>babel</code>插件逻辑（忽略了一些边界情况），就可以实现<code>this.$confim().then()</code>到<code>this.$confim().then().catch(err => err)</code>的转换了。</p>
<h2 data-id="heading-7">4. 升级成通用方案</h2>
<p>上面的<code>babel</code>实现方案只针对<code>this.$confirm</code>来做<code>catch</code>的添加，插件要是只有这个功能未免也太鸡肋了。所以决定把这个方案升级成通用方案，这个通用方案支持的场景有：</p>
<ul>
<li>
<p>不强制规定只给成员访问形式的<code>Promise</code>添加<code>catch</code>，也就是说可以给<code>this.$confirm</code>、<code>$confirm</code>、<code>this['$confirm']</code>、<code>MessageBox.confirm</code>形式的<code>Promise</code>添加<code>catch</code>；</p>
</li>
<li>
<p>用户可以选择为指定的<code>Promise</code>添加<code>catch</code>，如果不选择则给所有<code>Promise</code>都添加<code>catch</code>；</p>
</li>
</ul>
<p>借助<code>babel</code>提供的插件选项，在<code>babel.config.js</code>中修改配置：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript">config.plugins = [
  [<span class="hljs-string">"./src/index.js"</span>, &#123;
    <span class="hljs-attr">promiseNames</span>: [<span class="hljs-string">'$confirm'</span>, <span class="hljs-string">'$prompt'</span>, <span class="hljs-string">'$msgbox'</span>]
  &#125;]
]
<span class="copy-code-btn">复制代码</span></code></pre>
<p><code>promiseNames</code>中定义的选项会通过状态对象传递给插件访问者：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-built_in">module</span>.exports = <span class="hljs-function">(<span class="hljs-params">&#123; types: t &#125;</span>) =></span> &#123;
  <span class="hljs-keyword">return</span> &#123;
    <span class="hljs-attr">visitor</span>: &#123;
      CallExpression (path, &#123; opts &#125;) &#123;
        <span class="hljs-built_in">console</span>.log(opts.promiseNames) <span class="hljs-comment">// ['$confirm', '$prompt', '$msgbox']</span>
      &#125;
    &#125;
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>支持自定义<code>catch</code>的回调逻辑，如果不定义，则默认是<code>catch(err => err)</code>。</li>
</ul>
<p>也是借助<code>babel</code>提供的插件选项，在<code>babel.config.js</code>中修改配置：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript">config.plugins = [
  [<span class="hljs-string">"./src/index.js"</span>, &#123;
    <span class="hljs-attr">catchCallback</span>: <span class="hljs-string">'console.log(err)'</span>
  &#125;]
]
<span class="copy-code-btn">复制代码</span></code></pre>
<p>同时还借助<code>babel</code>提供的<code>template</code>工具，将字符串转换成<code>AST</code>节点：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-built_in">module</span>.exports = <span class="hljs-function">(<span class="hljs-params">&#123; types: t, template &#125;</span>) =></span> &#123;
  <span class="hljs-keyword">return</span> &#123;
    <span class="hljs-attr">visitor</span>: &#123;
      CallExpression (path, &#123; opts &#125;) &#123;
        <span class="hljs-built_in">console</span>.log(opts.catchCallback) <span class="hljs-comment">// console.log(err)</span>
        ...
        <span class="hljs-keyword">const</span> arrowFunctionBody = !catchCallback
          ? t.identifier(<span class="hljs-string">'err'</span>)
          : t.BlockStatement([
            template.ast(catchCallback)
          ])
        <span class="hljs-keyword">const</span> arrowFunctionNode = t.arrowFunctionExpression(
          [t.identifier(<span class="hljs-string">'err'</span>)],
          arrowFunctionBody
        )
        ...
      &#125;
    &#125;
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>完整的代码请戳这<a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fpandly%2Fbabel-plugin-promise-add-catch" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/pandly/babel-plugin-promise-add-catch" ref="nofollow noopener noreferrer">github.com/pandly/babe…</a></p>
<h2 data-id="heading-8">5. 在实际项目中调试</h2>
<p>经过上述几个步骤的操作，一个完整的<code>babel</code>插件就基本完成了。接下来，就是在实际项目中进行测试了，本地调试可以用<code>npm link</code>指令来操作：</p>
<pre><code class="hljs language-bash copyable" lang="bash">$ <span class="hljs-comment"># 先去到模块目录，把它 link 到全局</span>
$ <span class="hljs-built_in">cd</span> path/to/babel-plugin-promise-add-catch
$ npm link
$
$ <span class="hljs-comment"># 再去项目目录通过包名来 link</span>
$ <span class="hljs-built_in">cd</span> path/to/my-project
$ npm link babel-plugin-promise-add-catch
<span class="copy-code-btn">复制代码</span></code></pre>
<p>然后在实际项目的<code>babel</code>配置文件中加上：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript">plugins: [
 [
  <span class="hljs-string">'promise-add-catch'</span>,
    &#123;
      <span class="hljs-attr">promiseNames</span>: [<span class="hljs-string">'$confirm'</span>, <span class="hljs-string">'$prompt'</span>, <span class="hljs-string">'$msgbox'</span>] <span class="hljs-comment">// 如果有需要</span>
      <span class="hljs-attr">catchCallback</span>: <span class="hljs-string">'console.log(err)'</span> <span class="hljs-comment">// 如果有需要</span>
    &#125;
  ]
]
<span class="copy-code-btn">复制代码</span></code></pre>
<p>启动项目，删除代码中的<code>catch</code>，如果控制台没有报错，则说明大功告成！</p>
<h2 data-id="heading-9">6. 总结</h2>
<p>总体来说，<code>babel</code>插件的编写入门还是比较简单的，但是要想写好却不是那么简单。入门简单是因为插件化结构清晰，<code>api</code>封装的强大，文档比较健全；而要想写好一个<code>babel</code>插件，首先要熟悉代码对应的<code>AST</code>树结构，其次要去考虑很多边界情况来保证代码的健壮性，最后要熟读<code>babel</code>文档，掌握<code>babel</code>提供的<code>api</code>和属性。</p>
<p>在编写插件的时候碰到两个问题，一直没有找到答案：</p>
<ol>
<li>
<p>都说是<code>plugins</code>优先于<code>presets</code>执行，可是在测试<code>async</code>函数时很明显感受到是<code>presets</code>优先于<code>plugins</code>;</p>
</li>
<li>
<p>本地<code>demo</code>使用<code>@babel/preset-env</code>会把<code>catch</code>和<code>finally</code>方法编译成计算的形式<code>['catch']()</code>，但是在真实项目中却不会。</p>
</li>
</ol>
<p>以上两个问题有知道的大佬可以在评论区告诉我，非常感谢~~</p>
<p>个人觉得这个插件还是挺实用的，并且已经推广到团队中去了，哈哈哈哈~~</p>
<p>最后，这个插件已发布到<code>npm</code>，插件地址<a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.npmjs.com%2Fpackage%2Fbabel-plugin-promise-add-catch" target="_blank" rel="nofollow noopener noreferrer" title="https://www.npmjs.com/package/babel-plugin-promise-add-catch" ref="nofollow noopener noreferrer">babel-plugin-promise-add-catch</a>，欢迎各位使用，也欢迎各位提出意见~~</p></div>  
</div>
            