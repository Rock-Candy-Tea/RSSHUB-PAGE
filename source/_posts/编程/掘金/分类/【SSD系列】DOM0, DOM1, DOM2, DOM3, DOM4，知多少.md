
---
title: '【SSD系列】DOM0, DOM1, DOM2, DOM3, DOM4，知多少'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=9110'
author: 掘金
comments: false
date: Fri, 13 Aug 2021 16:42:19 GMT
thumbnail: 'https://picsum.photos/400/300?random=9110'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>这是我参与8月更文挑战的第14天，活动详情查看：<a href="https://juejin.cn/post/6987962113788493831" title="https://juejin.cn/post/6987962113788493831" target="_blank">8月更文挑战</a>。</p>
<h2 data-id="heading-0">前言</h2>
<p>关于关于<a href="https://juejin.cn/column/6991252706941730852" target="_blank" title="https://juejin.cn/column/6991252706941730852">【SSD系列】</a>：<br>
<strong>前端一些有意思的内容，旨在3-10分钟里， 500-1500字，有所获，又不为所累。</strong></p>
<p>DOM是前端工程师必修技能，DOM到底涵盖多少东西呢？</p>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fdom.spec.whatwg.org%2F" target="_blank" rel="nofollow noopener noreferrer" title="https://dom.spec.whatwg.org/" ref="nofollow noopener noreferrer">DOM Living Standard</a> 这里有最新的DOM标准，不妨收藏一下。</p>
<h2 data-id="heading-1">什么是DOM</h2>
<p>DOM（文档对象模型）是针对 HTML和 XML文档的一个API（应用程序编程接口）。DOM描绘了一个层次化的节点树，允许开发人员添加、移除和修改页面的某一部分。DOM 脱胎于Netscape及微软公司创始的 DHTML（动态 HTML），但现在它已经成为表现和操作页面标记的真正的跨平台、语言中立的方式。</p>
<h2 data-id="heading-2">DOM0</h2>
<p><code>JavaScript</code>在早期版本中提供了查询和操作Web文档的内容API（如：图像和表单），在<code>JavaScript</code>中定义了定义了<code>'images'</code>、<code>'forms'</code>等，因此我们可以像下这样访问第一张图片或名为“user”的表单：</p>
<pre><code class="copyable">document.images[0]
document.forms['user']
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这实际上是未形成标准的试验性质的初级阶段的DOM，现在习惯上被称为<code>DOM0</code></p>
<p>还有我们所熟知的<code>onclick</code>事件，也是与<code>DOM0</code>级的事件。</p>
<p><code>DOM0</code>级别的事件优点：</p>
<ol>
<li>
<p><strong>效率高</strong></p>
</li>
<li>
<p><strong>可以被Node.clone克隆</strong></p>
</li>
<li>
<p><strong>移除事件非常简单</strong></p>
<p><code>container.onclick=null</code>即可</p>
</li>
<li>
<p>有点也是缺点，唯一性</p>
</li>
</ol>
<p>多次复制会被覆盖</p>
<p>当然其他<code>onxxx</code>事件也是，而我们熟知的<code>addEventListener</code>则属于<code>DOM2</code>级别事件。</p>
<pre><code class="hljs language-js copyable" lang="js"><div id=<span class="hljs-string">"container"</span> onclick=<span class="hljs-string">"log1();log2()"</span>>点我</div>
<span class="xml"><span class="hljs-tag"><<span class="hljs-name">script</span>></span><span class="javascript">
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">log1</span>(<span class="hljs-params"></span>) </span>&#123;
<span class="hljs-built_in">console</span>.log(<span class="hljs-string">'log1......'</span>);
&#125;
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">log2</span>(<span class="hljs-params"></span>) </span>&#123;
<span class="hljs-built_in">console</span>.log(<span class="hljs-string">'log2......'</span>);
&#125;

<span class="hljs-comment">// 移除事件</span>
container.onclick = <span class="hljs-literal">null</span>

</span><span class="hljs-tag"></<span class="hljs-name">script</span>></span></span>

<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-3">DOM1</h2>
<p>大家熟知的<code>Node</code>，<code>document</code>, <code>document.createElement</code>都是在DOM1级别定义的。</p>
<p>更多关于知识，详见<a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.w3.org%2FTR%2F1998%2FREC-DOM-Level-1-19981001%2F" target="_blank" rel="nofollow noopener noreferrer" title="https://www.w3.org/TR/1998/REC-DOM-Level-1-19981001/" ref="nofollow noopener noreferrer">Document Object Model (DOM) Level 1 Specification</a>。</p>
<p>1998年 10月DOM1级规范成为W3C的推荐标准，为基本的文档结构及查询提供了接口，专注于HTML文档和XML文档。</p>
<p>在<code>DOM1</code>中，DOM由两个模块组成：<code>DOM Core</code>（DOM核心）和<code>DOM HTML</code>。其中，<code>DOM Core</code>规定了基于XML的文档结构标准，通过这个标准简化了对文档中任意部分的访问和操作。<code>DOM HTML</code>则在DOM核心的基础上加以扩展，添加了针对HTML的对象和方法，如：JavaScript中的<code>Document</code>对象</p>
<p>每个节点都有nodeType属性，表示该节点的类型。</p>
<p>在Node类型上的12个数值常量表示：</p>






































































<table><thead><tr><th>NodeType常量</th><th>NodeType常量值</th><th>说明</th></tr></thead><tbody><tr><td>Node.ELEMENT_NODE</td><td>1</td><td>我们常量的div,san,input等等</td></tr><tr><td>Node.ATTRIBUTE_NODE</td><td>2</td><td>属性。</td></tr><tr><td>Node.TEXT_NODE</td><td>3</td><td>包含按字面解释的纯文本，也可能包含转义后的HTML字符</td></tr><tr><td>Node.CDATA_SECTION_NODE</td><td>4</td><td>CDATA区块</td></tr><tr><td>Node.ENTITY_REFERENCE_NODE</td><td>5</td><td>在 <a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.w3.org%2FTR%2Fdom%2F" target="_blank" rel="nofollow noopener noreferrer" title="https://www.w3.org/TR/dom/" ref="nofollow noopener noreferrer">DOM4</a> 规范中被移除</td></tr><tr><td>Node.ENTITY_NODE</td><td>6</td><td>在 <a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.w3.org%2FTR%2Fdom%2F" target="_blank" rel="nofollow noopener noreferrer" title="https://www.w3.org/TR/dom/" ref="nofollow noopener noreferrer">DOM4</a> 规范里被移除</td></tr><tr><td>Node.PROCESSING_INSTRUCTION_NODE</td><td>7</td><td>用于XML文档的 <a href="https://link.juejin.cn/?target=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FProcessingInstruction" target="_blank" rel="nofollow noopener noreferrer" title="https://developer.mozilla.org/en-US/docs/Web/API/ProcessingInstruction" ref="nofollow noopener noreferrer">ProcessingInstruction (en-US)</a> ，例如 <code><?xml-stylesheet ... ?></code> 声明</td></tr><tr><td>Node.COMMENT_NODE</td><td>8</td><td>注释</td></tr><tr><td>Node.DOCUMENT_NODE</td><td>9</td><td>表示整个HTML页面</td></tr><tr><td>Node.DOCUMENT_TYPE_NODE</td><td>10</td><td>文档类型（doctype）信息。</td></tr><tr><td>Node.DOCUMENT_FRAGMENT_NODE</td><td>11</td><td>文档片段。性能优化常用。</td></tr><tr><td>Node.NOTATION_NODE</td><td>12</td><td>在 <a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.w3.org%2FTR%2Fdom%2F" target="_blank" rel="nofollow noopener noreferrer" title="https://www.w3.org/TR/dom/" ref="nofollow noopener noreferrer">DOM4</a> 规范中被移除</td></tr></tbody></table>
<h2 data-id="heading-4">DOM2</h2>
<p>我们熟知的·<code>addEventListner</code>, <code>document.body.style</code>， <code>getElementById</code>这些都是DOM2级别的东西。</p>
<ul>
<li>
<p>DOM2级核心（DOMLevel2 Core）</p>
<p>详情参见 <a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.w3.org%2FTR%2FDOM-Level-2-Core%2FOverview.html" target="_blank" rel="nofollow noopener noreferrer" title="https://www.w3.org/TR/DOM-Level-2-Core/Overview.html" ref="nofollow noopener noreferrer">DOM-Level-2-Core Overview</a> , <a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.w3.org%2FTR%2FDOM-Level-2-Core%2Fcore.html" target="_blank" rel="nofollow noopener noreferrer" title="https://www.w3.org/TR/DOM-Level-2-Core/core.html" ref="nofollow noopener noreferrer">DOM-Level-2-Core</a> 和 <a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.w3.org%2FTR%2FDOM-Level-2-Core%2Fchanges.html" target="_blank" rel="nofollow noopener noreferrer" title="https://www.w3.org/TR/DOM-Level-2-Core/changes.html" ref="nofollow noopener noreferrer">DOM-Level-2-Core Changes</a></p>
<p>在 1级核心基础上构建，为节点添加了更多方法和属性。</p>
<p>例如 <code>importNode</code>, <code>createElementNS</code>, <code>createAttributeNS</code>, <code>getElementsByTagNameNS</code> and <code>getElementById</code>等等</p>
</li>
<li>
<p>DOM2级视图（DOM Level2 Views）</p>
<p>详情参见 <a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.w3.org%2FTR%2FDOM-Level-2-Views%2FOverview.html" target="_blank" rel="nofollow noopener noreferrer" title="https://www.w3.org/TR/DOM-Level-2-Views/Overview.html" ref="nofollow noopener noreferrer">DOM-Level-2-Views Overview</a></p>
<p>为文档定义了基于样式信息的不同视图。</p>
<p>我们常用的就是<code>document.defaultView</code>，其返回文档所在的<code>Window</code>。</p>
</li>
<li>
<p>DOM2 级事件（DOM Level2 Events）</p>
<p>详情参见 <a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.w3.org%2FTR%2FDOM-Level-2-Events%2FOverview.html" target="_blank" rel="nofollow noopener noreferrer" title="https://www.w3.org/TR/DOM-Level-2-Events/Overview.html" ref="nofollow noopener noreferrer">DOM-Level-2-Events Overview</a></p>
<p>说明了如何使用事件与 DOM文档交互。</p>
<p>我们比较熟悉的就是 <code>addEventListner</code>， 基于<code>EventTarget</code>的整个事件系统都是DOM2定义的。</p>
</li>
<li>
<p>DOM2级样式（DOM Level 2 Style）</p>
<p>详情参见 <a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.w3.org%2FTR%2FDOM-Level-2-Style%2FOverview.html" target="_blank" rel="nofollow noopener noreferrer" title="https://www.w3.org/TR/DOM-Level-2-Style/Overview.html" ref="nofollow noopener noreferrer">DOM-Level-2-Style Overview</a></p>
<p>定义了如何以编程方式来访问和改变 CSS 样式信息。</p>
</li>
</ul>
<p>比如我们常见 <code>CSSStyleDeclaration </code>和<code>CSSStyleSheet</code> 这些重要的对象，<strong>别说你没用过？</strong> <code>document.body.style</code>其返回的就是<code>CSSStyleDeclaration</code>.</p>
<ul>
<li>
<p>DOM2级遍历和范围（DOM Level2Traversal and Range）</p>
<p>​    详情参见<a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.w3.org%2FTR%2FDOM-Level-2-Traversal-Range%2FOverview.html" target="_blank" rel="nofollow noopener noreferrer" title="https://www.w3.org/TR/DOM-Level-2-Traversal-Range/Overview.html" ref="nofollow noopener noreferrer">DOM-Level-2-Traversal-Range Overview</a></p>
<p>​引入了遍历 DOM文档和选择其特定部分的新接口。</p>
<p>比如： <strong><a href="https://link.juejin.cn/?target=https%3A%2F%2Fdeveloper.mozilla.org%2Fzh-CN%2Fdocs%2FWeb%2FAPI%2FDocument%2FcreateTreeWalker" target="_blank" rel="nofollow noopener noreferrer" title="https://developer.mozilla.org/zh-CN/docs/Web/API/Document/createTreeWalker" ref="nofollow noopener noreferrer">createTreeWalker</a></strong> 与 <strong><a href="https://link.juejin.cn/?target=https%3A%2F%2Fdeveloper.mozilla.org%2Fzh-CN%2Fdocs%2FWeb%2FAPI%2FDocument%2FcreateNodeIterator" target="_blank" rel="nofollow noopener noreferrer" title="https://developer.mozilla.org/zh-CN/docs/Web/API/Document/createNodeIterator" ref="nofollow noopener noreferrer">createNodeIterator</a></strong> 这两个节点遍历方法，大家可能比较陌生：</p>
</li>
</ul>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> nodeIterator = <span class="hljs-built_in">document</span>.createNodeIterator(
    <span class="hljs-built_in">document</span>.body,
    NodeFilter.SHOW_ELEMENT,
    &#123;
      <span class="hljs-function"><span class="hljs-title">acceptNode</span>(<span class="hljs-params">node</span>)</span> &#123;
       <span class="hljs-keyword">return</span> node.nodeName.toLowerCase() === <span class="hljs-string">'p'</span> ? NodeFilter.FILTER_ACCEPT : NodeFilter.FILTER_REJECT;
     &#125;
   &#125;
);
<span class="hljs-keyword">const</span> pars = [];
<span class="hljs-keyword">let</span> currentNode;

<span class="hljs-keyword">while</span> (currentNode = nodeIterator.nextNode()) &#123;
  pars.push(currentNode);
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>
<p>DOM2级HTML（DOMLevel2HTML）</p>
<p>​详情参见 <a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.w3.org%2FTR%2FDOM-Level-2-HTML%2FOverview.html" target="_blank" rel="nofollow noopener noreferrer" title="https://www.w3.org/TR/DOM-Level-2-HTML/Overview.html" ref="nofollow noopener noreferrer">DOM-Level-2-HTML Overview</a></p>
<p>其扩展了 DOM Level 2 Core API [ DOM Level 2 Core ] ，以描述特定于 HTML 文档[ HTML 4.01]和 XHTML 文档[ XHTML 1.0]的对象和方法。</p>
<p><strong>一般来说，操作层次化文档结构、元素和属性所需的功能将在核心部分中找到; 依赖于 HTML 中定义的特定元素的功能将在本部分中找到。</strong></p>
</li>
</ul>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.w3.org%2FTR%2FDOM-Level-2-HTML%2FOverview.html%23html-HTMLOptionsCollection" target="_blank" rel="nofollow noopener noreferrer" title="https://www.w3.org/TR/DOM-Level-2-HTML/Overview.html#html-HTMLOptionsCollection" ref="nofollow noopener noreferrer">HTMLOptionsCollection</a>就是新增的， 你别说不知道，其就是<code><option></code>节点的集合。DOMImplementation 接口的 <code>hasFeature</code>可还记得，也是哦。</p>
<h2 data-id="heading-5">DOM3</h2>
<p>详情可参见 <a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.w3.org%2FTR%2FDOM-Level-3-Core%2FOverview.html" target="_blank" rel="nofollow noopener noreferrer" title="https://www.w3.org/TR/DOM-Level-3-Core/Overview.html" ref="nofollow noopener noreferrer">DOM-Level-3-Core Overview</a>， <a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.w3.org%2FTR%2FDOM-Level-3-Core%2Fcore.html" target="_blank" rel="nofollow noopener noreferrer" title="https://www.w3.org/TR/DOM-Level-3-Core/core.html" ref="nofollow noopener noreferrer">DOM-Level-3-Core</a> 和 <a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.w3.org%2FTR%2FDOM-Level-3-Core%2Fchanges.html" target="_blank" rel="nofollow noopener noreferrer" title="https://www.w3.org/TR/DOM-Level-3-Core/changes.html" ref="nofollow noopener noreferrer">DOM-Level-3-Core Changes</a>。</p>
<p>它完成了 DOM 和 XML信息集文档之间的映射，包括对 XML Base [ XML Base ]的支持，增加了向 DOM Nodes 附加用户信息，提供了解析名称空间前缀或操作“ ID”属性的机制等等。</p>
<ul>
<li><code>DOM加载和保存模块</code>（DOM Load and Save）：引入了以统一方式加载和保存文档的方法</li>
<li><code>DOM验证模块</code>（DOM Validation）：定义了验证文档的方法</li>
<li><code>DOM核心的扩展</code>（DOM Style）：支持XML 1.0规范，涉及XML Infoset、XPath和XML Base</li>
</ul>
<h2 data-id="heading-6">DOM4</h2>
<p>2015年11月19日， DOM4发布，详情可参见 <a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.w3.org%2FTR%2F2015%2FREC-dom-20151119%2F" target="_blank" rel="nofollow noopener noreferrer" title="https://www.w3.org/TR/2015/REC-dom-20151119/" ref="nofollow noopener noreferrer">W3C DOM4</a>。</p>
<p>DOM4增加了 Mutation Observers ，作为原来 Mutation Events的替代。</p>
<h2 data-id="heading-7">小结</h2>
<p>先提个问题，我们常说的<code>HTML5</code>是 2008年发布的，他应该和DOM几对应你？</p>
<ol>
<li><code>onclick</code> 系列是DOM0级别的事件，只能有一个函数，一定条件下可以被复制</li>
<li><code>addEventListener</code>系列是DOM2级别的事件</li>
<li><code>XPath</code> 属于DOM3级别的东西，平时并不常见，其也可用于遍历节点。</li>
<li>DOM4，增加了观察节点变化的能力。</li>
</ol>
<p>综上可见，DOM1, DOM2是核心，其余的我们使用并不多。</p>
<h2 data-id="heading-8">写在最后</h2>
<p>不忘初衷，【SSD系列】，3-5分钟，500-1000字，有所得，而不为所累，如果你觉得不错，你的一赞一评就是我前行的最大动力。</p>
<p>技术交流群请到 <a href="https://juejin.cn/pin/6994350401550024741" title="https://juejin.cn/pin/6994350401550024741" target="_blank">这里来</a>。
或者添加我的微信 dirge-cloud，一起学习。</p>
<blockquote>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fhtml.spec.whatwg.org%2F" target="_blank" rel="nofollow noopener noreferrer" title="https://html.spec.whatwg.org/" ref="nofollow noopener noreferrer">HTML Living Standard</a><br>
<a href="https://link.juejin.cn/?target=https%3A%2F%2Fdom.spec.whatwg.org%2F" target="_blank" rel="nofollow noopener noreferrer" title="https://dom.spec.whatwg.org/" ref="nofollow noopener noreferrer">DOM Living Standard</a><br>
<a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.w3.org%2FTR%2F1998%2FREC-DOM-Level-1-19981001%2F" target="_blank" rel="nofollow noopener noreferrer" title="https://www.w3.org/TR/1998/REC-DOM-Level-1-19981001/" ref="nofollow noopener noreferrer">Document Object Model (DOM) Level 1 Specification</a><br>
<a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.w3.org%2FTR%2FDOM-Level-2-Core%2Fcore.html" target="_blank" rel="nofollow noopener noreferrer" title="https://www.w3.org/TR/DOM-Level-2-Core/core.html" ref="nofollow noopener noreferrer">DOM-Level-2-Core</a><br>
<a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.w3.org%2FTR%2FDOM-Level-3-Core%2Fcore.html" target="_blank" rel="nofollow noopener noreferrer" title="https://www.w3.org/TR/DOM-Level-3-Core/core.html" ref="nofollow noopener noreferrer">DOM-Level-3-Core</a><br>
<a href="https://link.juejin.cn/?target=https%3A%2F%2Fdom.spec.whatwg.org%2F" target="_blank" rel="nofollow noopener noreferrer" title="https://dom.spec.whatwg.org/" ref="nofollow noopener noreferrer">DOM Living Standard </a><br>
<a href="https://link.juejin.cn/?target=https%3A%2F%2Fitbilu.com%2Fjavascript%2Fjs%2FVyxodm_1g.html" target="_blank" rel="nofollow noopener noreferrer" title="https://itbilu.com/javascript/js/Vyxodm_1g.html" ref="nofollow noopener noreferrer">JavaScript和DOM的产生与发展</a><br>
<a href="https://link.juejin.cn/?target=https%3A%2F%2Fblog.csdn.net%2Fweixin_41054156%2Farticle%2Fdetails%2F88850585" target="_blank" rel="nofollow noopener noreferrer" title="https://blog.csdn.net/weixin_41054156/article/details/88850585" ref="nofollow noopener noreferrer">DOM0、DOM1、DOM2、DOM3事件区别</a><br>
JavaScript高级程序设计（第三版）<br>
JavaScript高级程序设计（第四版）<br>
<a href="https://link.juejin.cn/?target=https%3A%2F%2Fzhuanlan.zhihu.com%2Fp%2F107171488" target="_blank" rel="nofollow noopener noreferrer" title="https://zhuanlan.zhihu.com/p/107171488" ref="nofollow noopener noreferrer">DOM ：DOM0 DOM1 DOM2 DOM3</a><br>
<a href="https://link.juejin.cn/?target=https%3A%2F%2Fitbilu.com%2Fjavascript%2Fjs%2FVyxodm_1g.html" target="_blank" rel="nofollow noopener noreferrer" title="https://itbilu.com/javascript/js/Vyxodm_1g.html" ref="nofollow noopener noreferrer"># JavaScript和DOM的产生与发展</a></p>
</blockquote></div>  
</div>
            