
---
title: '解放生产力，自动化生成vue组件文档'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/9bd89aaca1a54104bcde29b4386a96f4~tplv-k3u1fbpfcp-zoom-1.image'
author: 掘金
comments: false
date: Tue, 29 Jun 2021 01:21:08 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/9bd89aaca1a54104bcde29b4386a96f4~tplv-k3u1fbpfcp-zoom-1.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h1 data-id="heading-0">一、现状</h1>
<p>Vue框架在前端开发中应用广泛，当一个多人开发的Vue项目经过长期维护之后往往会沉淀出很多的公共组件，这个时候经常会出现一个人 开发了一个组件而其他维护者或新接手的人却不知道这个组件是做什么的、该怎么用，还必须得再去翻看源码，或者压根就没注意到这个组件 的存在导致重复开发。这个时候就非常需要维护对应的组件文档来保障不同开发者之间良好的协作关系了。</p>
<p><strong>但是传统的手动维护文档又会带来新问题：</strong></p>
<ul>
<li>
<p>效率低，写文档是个费时费力的体力活，好不容易抽时间把组件开发完了回头还要写文档，想想都头大。</p>
</li>
<li>
<p>易出错，文档内容容易出现差错，可能与实际组件内容不一致。</p>
</li>
<li>
<p>不智能，组件更新迭代的同时，需要手动将变更同步到文档中，消耗时间还容易遗漏。</p>
</li>
</ul>
<p><strong>而理想中的文档维护方式则是：</strong></p>
<ul>
<li>
<p>工作量小，能够结合Vue组件自动获取相关信息，减少从头开始写文档的工作量。</p>
</li>
<li>
<p>信息准确，组件的关键信息与组件内容一致，不出错。</p>
</li>
<li>
<p>智能同步，Vue组件迭代升级时，文档内容可以自动的同步更新，无需人工校验信息是否一致。</p>
</li>
</ul>
<h1 data-id="heading-1">二、社区解决方案</h1>
<h2 data-id="heading-2">2.1 业务梳理</h2>
<p>为了能实现上述理想效果，我搜索并研究了一下社区中的解决方案，目前Vue官方提供了Vue-press可以用于快速搭建Vue项目文档， 而且也已经有了可以自动从Vue组件中提取信息的库了。</p>
<p>但是已有的第三方库并不能完全满足需求，主要存在以下两个问题:</p>
<blockquote>
<p>信息不全面，一些重要内容无法获取例如不能处理v-model，不能解析属性的修饰符sync，不能获取methods中函数入参的详细信息等。</p>
<p>比如下面的例子，value属性与input事件可以合起来构成一个v-model属性，但是这个信息在生成的文档中没有体现出来，要文档读者自行理解判断。而且生成的文档中没有展示是否支持sync。</p>
</blockquote>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/9bd89aaca1a54104bcde29b4386a96f4~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<blockquote>
<p>有较多的自定义标识，而且标识的命名过于个性化，对原有的代码侵入还是比较大的。例如下图中的代码，为了标记注释，需要在原有的 业务代码中额外添加"@vuese" "@arg"等标识，使得业务代码多出了一些业务无关内容。</p>
</blockquote>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/c511274192c04aca8b09f5d2e45a3ca2~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<h1 data-id="heading-3">三、技术方案</h1>
<p>针对以上文中提到的问题以及社区方案的不足，我们团队内沉淀出了一个小工具专门用于Vue组件信息获取并输出组件文档，大致效果如下：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/f2215c617d65469a9e51239ba14a9ded~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>上图中左边是一个常见的Vue单文件组件，右边是生成的文档。我们可以看到我们从组件中成功的提取到了以下一些信息：</p>
<ul>
<li>
<p>组件的名称。</p>
</li>
<li>
<p>组件的说明。</p>
</li>
<li>
<p>props，slot，event，methods等。</p>
</li>
<li>
<p>组件的注释内容。</p>
</li>
</ul>
<p>接下来我们将详细的讲解如何从组件中提取这些信息。</p>
<h2 data-id="heading-4">3.1 Vue文件解析</h2>
<p>既然是要从Vue组件中提取信息，那么首先的问题就是如何解析Vue组件。Vue官方开发了Vue-template-compiler库专门用于Vue解析， 这里我们也可以用同样的方式来处理。通过查阅文档可知Vue-template-compiler提供了一个parseComponent方法可以对原始的Vue文件进行处理。</p>
<pre><code class="hljs language-java copyable" lang="java"><span class="hljs-keyword">import</span> &#123; parseComponent &#125; from <span class="hljs-string">'Vue-template-compiler'</span>
<span class="hljs-keyword">const</span> result = parseComponent(VueFileContent, [options])
<span class="copy-code-btn">复制代码</span></code></pre>
<p>处理后的结果如下，其中template和script分别对应Vue文件中的template和script的文本内容。</p>
<pre><code class="hljs language-java copyable" lang="java">export <span class="hljs-class"><span class="hljs-keyword">interface</span> <span class="hljs-title">SFCDescriptor</span> </span>&#123;
  template: SFCBlock | undefined;
  script: SFCBlock | undefined;
  styles: SFCBlock[];
  customBlocks: SFCBlock[];
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>当然仅仅是得到文本是不够的，还需要对文本进行更进一步的处理来获取更多的信息。得到script后，我们可以用babel把js编译成js的AST（抽象语法树），这个AST是一个普通的js对象，可以通过js进行遍历和读取 有了Ast之后我们就可以从中获取到我们想到详细的组件信息了。</p>
<pre><code class="hljs language-java copyable" lang="java"><span class="hljs-keyword">import</span> &#123; parse &#125; from <span class="hljs-string">'@babel/parser'</span>;
<span class="hljs-keyword">const</span> jsAst = parse(script, [options]);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>接着我们来看template，继续查找Vue-template-compiler的文档我们找到compile方法，compile是专门用于将template编译成AST的， 正好可以满足需求。</p>
<pre><code class="hljs language-java copyable" lang="java"><span class="hljs-keyword">import</span> &#123; compile &#125; from <span class="hljs-string">'Vue-template-compiler'</span>
<span class="hljs-keyword">const</span> templateAst = compile(template, [options]);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>得到结果中的ast则为template的编译结果。</p>
<pre><code class="hljs language-java copyable" lang="java">export <span class="hljs-class"><span class="hljs-keyword">interface</span> <span class="hljs-title">CompiledResult</span> </span>&#123;
  ast: ASTElement,
  render: string,
  staticRenderFns: Array<string>,
  errors: Array<string>
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>通过第一步的文件解析工作，我们成功获取到了Vue的模板ast和script中的js的AST，下一步我们就可以从中获取我们想要的信息了。</p>
<h2 data-id="heading-5">3.2 信息提取</h2>
<p>根据是否需要约定，信息可以分为两种：</p>
<blockquote>
<p>一种是可以直接从Vue组件中获取，例如props、events等。</p>
</blockquote>
<blockquote>
<p>另一种是需要额外约定格式的，例如：组件的说明注释，props的属性说明等，这部分可以放到注释里，通过对注释进行解析获取。</p>
</blockquote>
<p>为了方便的从ast中读取信息，这里先简单介绍一个工具@babel/traverse，这个库是babel官方提供的专门用于遍历js AST的。使用方式如下；</p>
<pre><code class="hljs language-java copyable" lang="java"><span class="hljs-keyword">import</span> traverse from <span class="hljs-string">'@babel/traverse'</span>

traverse(jsAst, options);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>通过在options中配置对应内容的回调函数，可以获得想要的ast节点。具体的使用可以参考<a href="https://babeljs.io/docs/en/babel-traverse" target="_blank" rel="nofollow noopener noreferrer">官方文档</a></p>
<h3 data-id="heading-6">3.2.1 可直接获取的信息</h3>
<p>可以从代码中直接获取的信息可以有效的解决信息同步问题，无论代码怎么变动，文档的关键信息都可以自动同步，省去了人工校对的麻烦。</p>
<p>可以直接获取的信息有：</p>
<ul>
<li>
<p>组件属性props</p>
</li>
<li>
<p>提供外部调用的方法methods</p>
</li>
<li>
<p>事件events</p>
</li>
<li>
<p>插槽slots</p>
</li>
</ul>
<p>1、2都可以利用traverse在js AST上直接遍历名称为props和methods的对象节点获取。</p>
<p>事件的获取稍微麻烦一点，可以通过查找<span class="math math-inline"><span class="katex"><span class="katex-mathml"><math xmlns="http://www.w3.org/1998/Math/MathML"><semantics><mrow><mi>e</mi><mi>m</mi><mi>i</mi><mi>t</mi><mtext>函数来定位到事件的位置，而</mtext></mrow><annotation encoding="application/x-tex">emit函数来定位到事件的位置，而</annotation></semantics></math></span><span class="katex-html" aria-hidden="true"><span class="base"><span class="strut" style="height:0.68333em;vertical-align:0em;"></span><span class="mord mathnormal">e</span><span class="mord mathnormal">m</span><span class="mord mathnormal">i</span><span class="mord mathnormal">t</span><span class="mord cjk_fallback">函</span><span class="mord cjk_fallback">数</span><span class="mord cjk_fallback">来</span><span class="mord cjk_fallback">定</span><span class="mord cjk_fallback">位</span><span class="mord cjk_fallback">到</span><span class="mord cjk_fallback">事</span><span class="mord cjk_fallback">件</span><span class="mord cjk_fallback">的</span><span class="mord cjk_fallback">位</span><span class="mord cjk_fallback">置</span><span class="mord cjk_fallback">，</span><span class="mord cjk_fallback">而</span></span></span></span></span>emit函数可以在traverse中监听MemberExpress(复杂类型节点)， 然后通过节点上的属性名是否是'<span class="math math-inline"><span class="katex"><span class="katex-mathml"><math xmlns="http://www.w3.org/1998/Math/MathML"><semantics><mrow><mi>e</mi><mi>m</mi><mi>i</mi><msup><mi>t</mi><mo mathvariant="normal" lspace="0em" rspace="0em">′</mo></msup><mtext>判断是否是事件。如果是事件，那么在</mtext></mrow><annotation encoding="application/x-tex">emit'判断是否是事件。如果是事件，那么在</annotation></semantics></math></span><span class="katex-html" aria-hidden="true"><span class="base"><span class="strut" style="height:0.751892em;vertical-align:0em;"></span><span class="mord mathnormal">e</span><span class="mord mathnormal">m</span><span class="mord mathnormal">i</span><span class="mord"><span class="mord mathnormal">t</span><span class="msupsub"><span class="vlist-t"><span class="vlist-r"><span class="vlist" style="height:0.751892em;"><span style="top:-3.063em;margin-right:0.05em;"><span class="pstrut" style="height:2.7em;"></span><span class="sizing reset-size6 size3 mtight"><span class="mord mtight"><span class="mord mtight">′</span></span></span></span></span></span></span></span></span><span class="mord cjk_fallback">判</span><span class="mord cjk_fallback">断</span><span class="mord cjk_fallback">是</span><span class="mord cjk_fallback">否</span><span class="mord cjk_fallback">是</span><span class="mord cjk_fallback">事</span><span class="mord cjk_fallback">件</span><span class="mord cjk_fallback">。</span><span class="mord cjk_fallback">如</span><span class="mord cjk_fallback">果</span><span class="mord cjk_fallback">是</span><span class="mord cjk_fallback">事</span><span class="mord cjk_fallback">件</span><span class="mord cjk_fallback">，</span><span class="mord cjk_fallback">那</span><span class="mord cjk_fallback">么</span><span class="mord cjk_fallback">在</span></span></span></span></span>emit父级中读取arguments字段， arguments的第一个元素就是事件名称，后面的元素为事件传参。</p>
<pre><code class="hljs language-java copyable" lang="java"><span class="hljs-keyword">this</span>.$emit(<span class="hljs-string">'event'</span>, arg);
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="hljs language-java copyable" lang="java">traverse(jsAst, &#123;
 MemberExpression(Node) &#123;
  <span class="hljs-comment">// 判断是不是event</span>
  <span class="hljs-keyword">if</span> (Node.node.property.name === <span class="hljs-string">'$emit'</span>) &#123;
  <span class="hljs-comment">// 第一个元素是事件名称</span>
    <span class="hljs-keyword">const</span> eventName = Node.parent.arguments[<span class="hljs-number">0</span>];
  &#125;
 &#125;
&#125;);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>在成功获取到Events后，那么结合Events和props，就可以进一步的判断出props中的两个特殊属性：</p>
<blockquote>
<p>是否存在v-model：查找props中是否存在value属性并且Events中是否存在input事件来确定。</p>
</blockquote>
<blockquote>
<p>props的某个属性是否支持sync：判断Events的时间名中是否存在有update开头的事件，并且事件名称与属性名相同。</p>
</blockquote>
<p>插槽slots的信息保存在上文的template的AST中，递归遍历template AST找到名为slots的节点，进而还可以在节点上查找到name。</p>
<h3 data-id="heading-7">3.2.2 需要约定的信息</h3>
<p>为什么除了可直接获取的组件信息之外,还会需要额外的约定一部分内容呢？其一是因为可直接获取的信息内容比较单薄，还不足以支撑起一个相对完善的组件文档；其二是我们日常开发组件时本身就会写很多的注释，如果能直接将部分注释提取出来放到文档中，可以大大降低文档维护的工作量；</p>
<p>整理一下可以约定的内容有以下几条：</p>
<ul>
<li>
<p>组件名称。</p>
</li>
<li>
<p>组件的整体介绍。</p>
</li>
<li>
<p>props、Events、methods、slots文字说明。</p>
</li>
<li>
<p>Methods标记和入参的详细说明。这些内容都可以放在注释中进行维护，之所以放在注释中进行维护是因为注释可以很容易从上文提到的js AST以及template AST中获取到， 在我们解析Vue组件信息的同时就可以把这部分针对性的说明一起解析到。</p>
</li>
</ul>
<p>接下来我们着重讲解如何将提取注释和注释与被注释的内容是如何对应起来的。</p>
<p>js中的注释根据位置不同可以分为头部注释(leadingComments)和尾部注释(trailingComments)，不同位置的注释会存放在对应的字段中， 代码展示如下:</p>
<pre><code class="hljs language-java copyable" lang="java"><span class="hljs-comment">// 头部注释export default &#123;&#125; // 尾部注释</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>解析结果</strong></p>
<pre><code class="hljs language-java copyable" lang="java"><span class="hljs-keyword">const</span> exportNode = &#123;
  type: <span class="hljs-string">"ExportDefaultDeclaration"</span>,
  leadingComments: [&#123;
    type: <span class="hljs-string">'CommentLine'</span>,
    value: <span class="hljs-string">'头部注释'</span>
  &#125;],
  trailingComments: [&#123;
    type: <span class="hljs-string">'CommentLine'</span>,
    value: <span class="hljs-string">'尾部注释'</span>
  &#125;]
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>在同一个位置上，根据注释格式的不同又分为单行注释(CommentLine)和块级注释(CommentBlock)，两种注释的区别会反应在注释节点的type字段中：</p>
<pre><code class="hljs language-java copyable" lang="java">
<span class="hljs-comment">/**
 * 块级注释
 */</span>
<span class="hljs-comment">// 单行注释</span>
export <span class="hljs-keyword">default</span> &#123;&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>解析结果</strong></p>
<pre><code class="hljs language-java copyable" lang="java"><span class="hljs-keyword">const</span> exportNode = &#123;
  type: <span class="hljs-string">"ExportDefaultDeclaration"</span>,
  leadingComments: [
    &#123;
      type: <span class="hljs-string">'CommentBlock'</span>,
      value: <span class="hljs-string">'块级注释'</span>
    &#125;,
    &#123;
      type: <span class="hljs-string">'CommentLine'</span>,
      value: <span class="hljs-string">'单行注释'</span>
    &#125;
  ]
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>另外，从上面的解析结果我们也可以看到，注释节点是挂载在被注释的export节点里面的，这也解决我们上面提到的另一个问题：注释与被注释的关联关系怎么获取的--其实babel在编译代码的时候已经替我们做好了。</p>
<p>template查找注释与被注释内容的方法不同。template中注释节点与其他节点一样是作为dom节点存在的， 在遍历节点的时候通过判断isComment字段的值是否为true来确定是否是注释节点。而被注释的内容的位置在兄弟节点的后一位：</p>
<pre><code class="hljs language-java copyable" lang="java"><!--template的注释-->
<slot>被注释的节点</slot>
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>解析结果</strong></p>
<pre><code class="hljs language-java copyable" lang="java"><span class="hljs-keyword">const</span> templateAst = [
  &#123;
    isComment: <span class="hljs-keyword">true</span>,
    text: <span class="hljs-string">"template的注释"</span>,
    type: <span class="hljs-number">3</span>
  &#125;,
  &#123;
    tag: <span class="hljs-string">"slot"</span>,
    type: <span class="hljs-number">1</span>
  &#125;
]
<span class="copy-code-btn">复制代码</span></code></pre>
<p>知道了如何处理注释内容，那么我们还可以利用注释做更多的事情。例如可以通过在methods的方法的注释中约定一个标记@public来区分是私有方法还是公共方法，如果更细节一点的话， 还可以参考另一个专门用于解析js注释的库js-doc的格式，对方法的入参进行更进一步的说明，丰富文档的内容。</p>
<p>我们只需要在获取到注释内容之后对文本进行切割读取即可，例如：</p>
<pre><code class="hljs language-java copyable" lang="java">export <span class="hljs-keyword">default</span> &#123;
  methods: &#123;
    <span class="hljs-comment">/**
     * <span class="hljs-doctag">@public</span>
     * <span class="hljs-doctag">@param</span> &#123;boolean&#125; value 入参说明
     */</span>
    show(value) &#123;&#125;
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>当然了为了避免对代码侵入过多，我们还是需要尽量少的添加额外的标识。而入参说明采用了与js-doc相同的格式，主要还是因为这套方案 使用比较普遍，而且代码编辑器都自动支持方便编辑。</p>
<h1 data-id="heading-8">四、总结</h1>
<p>编写组件文档是一个可以很好的提升项目内各个前端开发成员之间协作的事情，一份维护良好的文档会极大的改善开发体验。而如果能进一步的使用工具把维护文档的过程自动化的话，那开发的幸福感还能得到再次提升。</p>
<p>经过一系列的摸索和尝试，我们成功的找到了 自动化提取Vue组件信息的方案，大大减轻了维护Vue组件文档的工作量，提升了文档信息的准确度。具体实现上，先用vue-template-compiler对Vue文件进行处理，获得template的AST和js的AST，有了这两个AST后就可以去获取更加详细的信息了， 梳理一下到目前为止我们生成的文档里可以获取到的内容及获取方式：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/b809c2cd48dc491db62fe34f9e686228~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>至于获取到内容之后是以Markdown的形式输出还是json文件的形式输出，就取决于实际的开发情况了。</p>
<h1 data-id="heading-9">五、展望</h1>
<p>这里我们所讨论的是直接从单个Vue文件去获取信息并输出，但是像很多第三方组件库里例如elementUI的文档，不仅有组件信息还有展示实例。如果一个组件库维护的相对完善的话，一个组件应该会有对应的测试用例，那么是否可以将组件的测试用例也提取出来， 实现组件文件中示例部分的自动提取呢？这也是值得研究的问题。</p>
<blockquote>
<p>作者：vivo互联网前端团队-Feng Di</p>
</blockquote></div>  
</div>
            