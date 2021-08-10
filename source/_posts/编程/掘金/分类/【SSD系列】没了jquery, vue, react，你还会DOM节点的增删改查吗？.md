
---
title: '【SSD系列】没了jquery, vue, react，你还会DOM节点的增删改查吗？'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/1faeb4fc6ce340c8980929c34113bd83~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Mon, 09 Aug 2021 16:14:20 GMT
thumbnail: 'https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/1faeb4fc6ce340c8980929c34113bd83~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>这是我参与8月更文挑战的第10天，活动详情查看：<a href="https://juejin.cn/post/6987962113788493831" title="https://juejin.cn/post/6987962113788493831" target="_blank">8月更文挑战</a>。</p>
<h2 data-id="heading-0">前言</h2>
<p>关于<a href="https://juejin.cn/column/6991252706941730852" target="_blank" title="https://juejin.cn/column/6991252706941730852">【SSD系列】</a>：<br>
<strong>前端一些有意思的内容，旨在3-10分钟里， 500-1500字，有所获，又不为所累。</strong></p>
<p>先提问一波：(无框架前提下)</p>
<ul>
<li>
<p><strong>常用查询节点方法有哪些</strong></p>
</li>
<li>
<p><strong>什么是空白节点</strong>？？她又到底是个什么东西</p>
</li>
<li>
<p><strong>querySelectorAll 有哪些坑</strong></p>
</li>
<li>
<p><strong>怎么查询伪元素</strong></p>
</li>
<li>
<p><strong>四种删除节点方式你都知道吗</strong></p>
</li>
<li>
<p><strong>HTMLCollection 和 NodeList的区别</strong></p>
</li>
<li>
<p><strong>怎样删除所有的孩子节点</strong></p>
</li>
</ul>
<p>我们已经先jquery, vue, react等前端框架带来的便利了：</p>
<ul>
<li>jquery就不说了，一个<code>$</code>走天下，无限连。</li>
<li>vue和react使用<code>ref</code>就能拿到对应节点。</li>
</ul>
<p>离开了这些框架，你还能666的操作Node节点吗？</p>
<h2 data-id="heading-1">本文源码</h2>
<p><strong><a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fxiangwenhu%2FjuejinBlogsCodes%2Ftree%2Fmaster%2Fcrud-doms" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/xiangwenhu/juejinBlogsCodes/tree/master/crud-doms" ref="nofollow noopener noreferrer">crud-doms</a></strong></p>
<h2 data-id="heading-2">节点查询</h2>
<p>先放一段测试的html代码</p>
<pre><code class="hljs language-html copyable" lang="html">  <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"outer"</span> <span class="hljs-attr">id</span>=<span class="hljs-string">"outer"</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">ul</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"list list-1"</span>></span>
      <span class="hljs-tag"><<span class="hljs-name">li</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"item"</span>></span>list-one<span class="hljs-tag"></<span class="hljs-name">li</span>></span>
      <span class="hljs-tag"><<span class="hljs-name">li</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"item"</span>></span>list-two<span class="hljs-tag"></<span class="hljs-name">li</span>></span>
      <span class="hljs-tag"><<span class="hljs-name">li</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"item"</span>></span>list-three<span class="hljs-tag"></<span class="hljs-name">li</span>></span>
    <span class="hljs-tag"></<span class="hljs-name">ul</span>></span>
  <span class="hljs-tag"></<span class="hljs-name">div</span>></span>

  <span class="hljs-tag"><<span class="hljs-name">input</span> <span class="hljs-attr">type</span>=<span class="hljs-string">"button"</span> <span class="hljs-attr">name</span>=<span class="hljs-string">"btnSubmit"</span> <span class="hljs-attr">value</span>=<span class="hljs-string">"刷新"</span>/></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-3">常用的节点查询方法</h3>
<ol>
<li>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fdeveloper.mozilla.org%2Fzh-CN%2Fdocs%2FWeb%2FAPI%2FDocument%2FgetElementById" target="_blank" rel="nofollow noopener noreferrer" title="https://developer.mozilla.org/zh-CN/docs/Web/API/Document/getElementById" ref="nofollow noopener noreferrer">getElementById</a></p>
<p>根据元素的<code>id</code>属性值进行节点查询，返回单一节点。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-built_in">document</span>.getElementById(<span class="hljs-string">"outer"</span>)  <span class="hljs-comment">// <div class="outer" id="outer">......</span>
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
<li>
<p><code>getElementsByClassName</code></p>
<p>根据元素的classname属性值就行查询。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-built_in">document</span>.getElementsByClassName(<span class="hljs-string">"item"</span>) <span class="hljs-comment">// HTMLCollection(3) [li.item, li.item, li.item]</span>
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
<li>
<p><code>getElementsByName</code></p>
<p>根源节点的name属性进行查询。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-built_in">document</span>.getElementsByName(<span class="hljs-string">"btnSubmit"</span>) <span class="hljs-comment">// NodeList [input]</span>
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
<li>
<p><code>getElementsByTagName</code></p>
<p>根据节点标签名进行查询。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-built_in">document</span>.getElementsByTagName(<span class="hljs-string">"li"</span>) <span class="hljs-comment">// HTMLCollection(3) [li.item, li.item, li.item]</span>
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
<li>
<p><code>querySelector</code></p>
<p>根绝css选择器进行节点查询，返回单个节点。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-built_in">document</span>.querySelector(<span class="hljs-string">"#outer"</span>) <span class="hljs-comment">// <div class="outer" id="outer">......</span>
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
<li>
<p><code>querySelectorAll</code></p>
<p>根绝css选择器进行节点查询，返回节点列表。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-built_in">document</span>.querySelectorAll(<span class="hljs-string">".item"</span>) <span class="hljs-comment">// NodeList(3) [li.item, li.item, li.item]</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>在没有<code>querySelector</code>和<code>querySelectorAll</code>出现之前，基本都是通过前四个查询方法配合 <code>childNodes</code>和<code>parentNode</code>方法扩展出各种方法。</p>
</li>
</ol>
<h3 data-id="heading-4">一些特殊查询属性</h3>
<ul>
<li>document.all  返回所有的节点</li>
<li>document.images 返回所有的图片</li>
<li>document.forms 返回所有的form表单</li>
<li>document.links 返回所有的链接标签</li>
<li>document.embeds 返回所有的 <code>object</code>标签元素，以前主要用于flash，pdf等等</li>
</ul>
<h3 data-id="heading-5">querySelectorAll 注意事项</h3>
<ul>
<li>
<p>其返回的<strong>静态的<code>NodeList</code></strong>， 随后对<code>DOM</code>元素的改动不会影响其集合的内容。</p>
<p>下面的代码可以看到，添加一个节后后， nodeList长度并没有变化。</p>
<pre><code class="hljs language-html copyable" lang="html">  <span class="hljs-tag"><<span class="hljs-name">ul</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"list list-1"</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">li</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"item"</span>></span>list-one<span class="hljs-tag"></<span class="hljs-name">li</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">li</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"item"</span>></span>list-two<span class="hljs-tag"></<span class="hljs-name">li</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">li</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"item"</span>></span>list-three<span class="hljs-tag"></<span class="hljs-name">li</span>></span>
  <span class="hljs-tag"></<span class="hljs-name">ul</span>></span>

  <span class="hljs-tag"><<span class="hljs-name">script</span>></span><span class="javascript">
      <span class="hljs-keyword">var</span>  nodeList = <span class="hljs-built_in">document</span>.querySelectorAll(<span class="hljs-string">".item"</span>);
      <span class="hljs-built_in">console</span>.log(<span class="hljs-string">"len："</span>, nodeList.length);  <span class="hljs-comment">// 3</span>

      <span class="hljs-keyword">var</span> liEl = <span class="hljs-built_in">document</span>.createElement(<span class="hljs-string">"li"</span>);
      liEl.className = <span class="hljs-string">"item"</span>;
      liEl.innerHTML = <span class="hljs-string">"list-for"</span>
      <span class="hljs-built_in">document</span>.querySelector(<span class="hljs-string">".list"</span>).appendChild(liEl);
      
      <span class="hljs-built_in">console</span>.log(<span class="hljs-string">"len："</span>, nodeList.length); <span class="hljs-comment">//3 </span>
  </span><span class="hljs-tag"></<span class="hljs-name">script</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
<li>
<p>querySelectorAll可能返回的不是你期望的值</p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"outer"</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"select"</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"inner"</span>></span>
    <span class="hljs-tag"></<span class="hljs-name">div</span>></span>
  <span class="hljs-tag"></<span class="hljs-name">div</span>></span>
<span class="hljs-tag"></<span class="hljs-name">div</span>></span>

<span class="hljs-tag"><<span class="hljs-name">script</span>></span><span class="javascript">
<span class="hljs-keyword">var</span> select = <span class="hljs-built_in">document</span>.querySelector(<span class="hljs-string">'.select'</span>);
<span class="hljs-keyword">var</span> inner = select.querySelectorAll(<span class="hljs-string">'.outer .inner'</span>);
inner.length; <span class="hljs-comment">// 1, not 0!</span>
</span><span class="hljs-tag"></<span class="hljs-name">script</span>></span>

<span class="copy-code-btn">复制代码</span></code></pre>
<p>那么怎样才能返回期望的结果呢？答案是 <code>:scope</code></p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">var</span> select = <span class="hljs-built_in">document</span>.querySelector(<span class="hljs-string">'.select'</span>);
<span class="hljs-keyword">var</span> inner = select.querySelectorAll(<span class="hljs-string">':scope .outer .inner'</span>);
inner.length; <span class="hljs-comment">// 0</span>
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
<li>
<p><strong><a href="https://link.juejin.cn/?target=https%3A%2F%2Fdeveloper.mozilla.org%2Fzh-CN%2Fdocs%2FWeb%2FAPI%2FDocument%2FquerySelector%23%25E8%25BD%25AC%25E4%25B9%2589%25E7%2589%25B9%25E6%25AE%258A%25E5%25AD%2597%25E7%25AC%25A6" target="_blank" rel="nofollow noopener noreferrer" title="https://developer.mozilla.org/zh-CN/docs/Web/API/Document/querySelector#%E8%BD%AC%E4%B9%89%E7%89%B9%E6%AE%8A%E5%AD%97%E7%AC%A6" ref="nofollow noopener noreferrer">转义特殊字符</a></strong></p>
<pre><code class="hljs language-html copyable" lang="html">  <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">id</span>=<span class="hljs-string">"foo\bar"</span>></span><span class="hljs-tag"></<span class="hljs-name">div</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">id</span>=<span class="hljs-string">"foo:bar"</span>></span><span class="hljs-tag"></<span class="hljs-name">div</span>></span>

  <span class="hljs-tag"><<span class="hljs-name">script</span>></span><span class="javascript">
    <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'#foo\bar'</span>)               <span class="hljs-comment">// "#fooar"</span>
    <span class="hljs-built_in">document</span>.querySelector(<span class="hljs-string">'#foo\bar'</span>)    <span class="hljs-comment">// 不匹配任何元素</span>

    <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'#foo\\bar'</span>)              <span class="hljs-comment">// "#foo\bar"</span>
    <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'#foo\\\\bar'</span>)            <span class="hljs-comment">// "#foo\\bar"</span>
    <span class="hljs-built_in">document</span>.querySelector(<span class="hljs-string">'#foo\\\\bar'</span>) <span class="hljs-comment">// 匹配第一个div</span>

    <span class="hljs-built_in">document</span>.querySelector(<span class="hljs-string">'#foo:bar'</span>)    <span class="hljs-comment">// 不匹配任何元素</span>
    <span class="hljs-built_in">document</span>.querySelector(<span class="hljs-string">'#foo\\:bar'</span>)  <span class="hljs-comment">// 匹配第二个div</span>
  </span><span class="hljs-tag"></<span class="hljs-name">script</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
</ul>
<h3 data-id="heading-6"><strong>HTMLCollection 和 NodeList的区别</strong></h3>
<p>细心的通知可能发现了，上面的方法，有的返回的是HTMLCollection，有的返回的是NodeList。 他们有什么区别呢？</p>
<p>这里先要弄清晰继承关系：</p>
<pre><code class="hljs language-js copyable" lang="js">HTMLElement -> Element -> Node-> EventTarget
<span class="copy-code-btn">复制代码</span></code></pre>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FEventTarget" target="_blank" rel="nofollow noopener noreferrer" title="https://developer.mozilla.org/en-US/docs/Web/API/EventTarget" ref="nofollow noopener noreferrer">EventTarget</a> 前一个提供了事件分发能力，本身也是一个订阅发布中心，更多详情参见 <strong><a href="https://juejin.cn/post/6991992950876028959" target="_blank" title="https://juejin.cn/post/6991992950876028959">3行代码一个订阅发布中心，不会不知道吧</a></strong>。</p>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FNode" target="_blank" rel="nofollow noopener noreferrer" title="https://developer.mozilla.org/en-US/docs/Web/API/Node" ref="nofollow noopener noreferrer">Node</a> 有 12种节点类型，详情参见 <a href="https://link.juejin.cn/?target=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FNode%2FnodeType" target="_blank" rel="nofollow noopener noreferrer" title="https://developer.mozilla.org/en-US/docs/Web/API/Node/nodeType" ref="nofollow noopener noreferrer">NodeType</a>，我们常用的  div, span等等属于nodeType=1的节点类型。</p>
<p>所以：</p>
<p>HTMLCollection 是元素节点类型，即nodeType为1的节点。</p>
<p>NodeList 是节点集合，包含文本节点，注释节点等等其他节点。</p>
<h3 data-id="heading-7">怎么查询伪元素</h3>
<pre><code class="hljs language-html copyable" lang="html">// html代码  
<span class="hljs-tag"><<span class="hljs-name">style</span>></span><span class="css">
    <span class="hljs-selector-class">.nihao</span><span class="hljs-selector-pseudo">::before</span>&#123;
      <span class="hljs-attribute">content</span>: <span class="hljs-string">'你好，'</span>;
    &#125;
  </span><span class="hljs-tag"></<span class="hljs-name">style</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"nihao"</span> <span class="hljs-attr">id</span>=<span class="hljs-string">"nihao"</span>></span>
    Tom
  <span class="hljs-tag"></<span class="hljs-name">div</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>答案是不能，但你可以通过 <a href="https://link.juejin.cn/?target=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FWindow%2FgetComputedStyle" target="_blank" rel="nofollow noopener noreferrer" title="https://developer.mozilla.org/en-US/docs/Web/API/Window/getComputedStyle" ref="nofollow noopener noreferrer">window.getComputedStyle</a> 来获取其样式。</p>
<pre><code class="hljs language-css copyable" lang="css">window<span class="hljs-selector-class">.getComputedStyle</span>(nihao, "before")<span class="hljs-selector-attr">[<span class="hljs-string">"content"</span>]</span> // "\"你好，\""
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-8">节点删除</h2>
<p>先特出测试的html代码段</p>
<pre><code class="hljs language-html copyable" lang="html">  <span class="hljs-tag"><<span class="hljs-name">ul</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"list list-1"</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">li</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"item"</span>></span>list-one<span class="hljs-tag"></<span class="hljs-name">li</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">li</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"item"</span>></span>list-two<span class="hljs-tag"></<span class="hljs-name">li</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">li</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"item"</span>></span>list-three<span class="hljs-tag"></<span class="hljs-name">li</span>></span>
  <span class="hljs-tag"></<span class="hljs-name">ul</span>></span> 
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-9"><a href="https://link.juejin.cn/?target=https%3A%2F%2Fdeveloper.mozilla.org%2Fzh-CN%2Fdocs%2FWeb%2FAPI%2FNode%2FremoveChild" target="_blank" rel="nofollow noopener noreferrer" title="https://developer.mozilla.org/zh-CN/docs/Web/API/Node/removeChild" ref="nofollow noopener noreferrer">Node.removeNode</a></h3>
<p>这种我们用的最多的方法，前提是首先得获得要被删除元素的父节点，可以使用<code>parentNode</code>或者<code>parentElement</code>获得。</p>
<pre><code class="hljs language-js copyable" lang="js">
    <span class="hljs-keyword">var</span> ul = <span class="hljs-built_in">document</span>.querySelector(<span class="hljs-string">".list"</span>);
    <span class="hljs-built_in">console</span>.log(<span class="hljs-string">"li length"</span>, ul.children.length);  <span class="hljs-comment">// 3</span>
    ul.removeChild(ul.children[<span class="hljs-number">0</span>])  <span class="hljs-comment">// removeChild</span>
    <span class="hljs-built_in">console</span>.log(<span class="hljs-string">"li length"</span>, ul.children.length); <span class="hljs-comment">// 2</span>

<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-10"><a href="https://link.juejin.cn/?target=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FElement%2Fremove" target="_blank" rel="nofollow noopener noreferrer" title="https://developer.mozilla.org/en-US/docs/Web/API/Element/remove" ref="nofollow noopener noreferrer">Element.remove</a></h3>
<p>这个方法属于 Element对象上，也就表明，其他nodeType类型是不可以使用的, 其不需要获得副节点。</p>
<pre><code class="hljs language-js copyable" lang="js">
    <span class="hljs-keyword">var</span> ul = <span class="hljs-built_in">document</span>.querySelector(<span class="hljs-string">".list"</span>);
    <span class="hljs-built_in">console</span>.log(<span class="hljs-string">"li length"</span>, ul.children.length);  <span class="hljs-comment">// 3</span>
    ul.children[<span class="hljs-number">0</span>].remove();  <span class="hljs-comment">// remove</span>
    <span class="hljs-built_in">console</span>.log(<span class="hljs-string">"li length"</span>, ul.children.length); <span class="hljs-comment">// 2</span>

<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-11">outerHTML或者innerHTML</h3>
<pre><code class="hljs language-js copyable" lang="js">
   <span class="hljs-keyword">var</span> ul = <span class="hljs-built_in">document</span>.querySelector(<span class="hljs-string">".list"</span>);
    <span class="hljs-built_in">console</span>.log(<span class="hljs-string">"li length"</span>, ul.children.length);  <span class="hljs-comment">// 3</span>
    ul.children[<span class="hljs-number">0</span>].outerHTML = <span class="hljs-literal">null</span>   <span class="hljs-comment">// outerHTML</span>
    <span class="hljs-built_in">console</span>.log(<span class="hljs-string">"li length"</span>, ul.children.length); <span class="hljs-comment">// 2</span>


<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-12"><a href="https://link.juejin.cn/?target=https%3A%2F%2Fdeveloper.mozilla.org%2Fzh-CN%2Fdocs%2Fweb%2Fapi%2Fdocument%2Fadoptnode" target="_blank" rel="nofollow noopener noreferrer" title="https://developer.mozilla.org/zh-CN/docs/web/api/document/adoptnode" ref="nofollow noopener noreferrer">Document.adoptNode</a></h3>
<p>从其他的document文档中获取一个节点。 该节点以及它的子树上的所有节点都会从原文档删除。</p>
<pre><code class="hljs language-js copyable" lang="js">
<span class="hljs-keyword">var</span> ul = <span class="hljs-built_in">document</span>.querySelector(<span class="hljs-string">".list"</span>);
<span class="hljs-built_in">console</span>.log(<span class="hljs-string">"li length"</span>, ul.children.length);  <span class="hljs-comment">// 3</span>
<span class="hljs-built_in">document</span>.adoptNode(ul.children[<span class="hljs-number">0</span>]); <span class="hljs-comment">// adoptNode</span>
<span class="hljs-built_in">console</span>.log(<span class="hljs-string">"li length"</span>, ul.children.length); <span class="hljs-comment">// 2</span>

<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-13">批量删除节点</h3>
<p>批量删除，比如清除某个节点下的所有子节点，一般是使用<code>while</code>循环，暴力的方式是 <code>innerHTML = null</code>。</p>
<p><code>innerHTML = null</code>可能导致事件监听器没有被取消，以导致内存泄漏，具体有么有，还得看浏览器的实现。</p>
<p>我们封装一个吧：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">clearChildNodes</span>(<span class="hljs-params">node</span>)</span>&#123;
    <span class="hljs-keyword">while</span>(node.hasChildNodes())&#123;
        node.removeChild(node.firstChild);
    &#125;
&#125;
<span class="hljs-keyword">const</span> ul = <span class="hljs-built_in">document</span>.querySelector(<span class="hljs-string">".list"</span>);
<span class="hljs-built_in">console</span>.log(<span class="hljs-string">"nodes:"</span>, ul.childNodes.length);  <span class="hljs-comment">// 7</span>
clearChildNodes(ul);   
<span class="hljs-built_in">console</span>.log(<span class="hljs-string">"nodes:"</span>, ul.childNodes.length);  <span class="hljs-comment">// 0</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-14">空白节点</h3>
<p>为什么是7个节点呢？ 看图上的空白节点，有4个， 4+3 =7楼。</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/1faeb4fc6ce340c8980929c34113bd83~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>我们调整一下代码,  删除空白，再看输出</p>
<pre><code class="hljs language-html copyable" lang="html">  <span class="hljs-tag"><<span class="hljs-name">ul</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"list list-1"</span>></span><span class="hljs-tag"><<span class="hljs-name">li</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"item"</span>></span>list-one<span class="hljs-tag"></<span class="hljs-name">li</span>></span><span class="hljs-tag"><<span class="hljs-name">li</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"item"</span>></span>list-two<span class="hljs-tag"></<span class="hljs-name">li</span>></span><span class="hljs-tag"><<span class="hljs-name">li</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"item"</span>></span>list-three<span class="hljs-tag"></<span class="hljs-name">li</span>></span><span class="hljs-tag"></<span class="hljs-name">ul</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/8b040d1e33ff472b834c93129d27517b~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>那空白节点，究竟是个什么东西？？</p>
<p>看代码，其实就是<strong>nodeType为3的文本节点</strong>。进行输出的时候其textConent为空。</p>
<pre><code class="hljs language-js copyable" lang="js">   <span class="hljs-keyword">var</span> ul = <span class="hljs-built_in">document</span>.querySelector(<span class="hljs-string">".list"</span>);
    <span class="hljs-built_in">console</span>.log(<span class="hljs-string">"li length"</span>, ul.childNodes.length);  <span class="hljs-comment">// 7</span>

    <span class="hljs-keyword">var</span> firstNode = ul.childNodes[<span class="hljs-number">0</span>];
    <span class="hljs-built_in">console</span>.log(<span class="hljs-string">"nodeType"</span>, firstNode.nodeType);  <span class="hljs-comment">// 3 </span>
    <span class="hljs-built_in">console</span>.log(<span class="hljs-string">"content"</span>, firstNode.textContent); <span class="hljs-comment">// </span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>我们不妨添加一点内容,  你就能清晰的知道了， 其childNodes长度依旧是7，第一个文本节点的内容是 <code>text content</code></p>
<pre><code class="hljs language-html copyable" lang="html">  <span class="hljs-tag"><<span class="hljs-name">ul</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"list list-1"</span>></span>text content
    <span class="hljs-tag"><<span class="hljs-name">li</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"item"</span>></span>list-one<span class="hljs-tag"></<span class="hljs-name">li</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">li</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"item"</span>></span>list-two<span class="hljs-tag"></<span class="hljs-name">li</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">li</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"item"</span>></span>list-three<span class="hljs-tag"></<span class="hljs-name">li</span>></span>
  <span class="hljs-tag"></<span class="hljs-name">ul</span>></span> 
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/83bde55b6eeb4097aeac2d274db14685~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-15">小结</h2>
<p>是不是很简单，一切都看起来没那么难，这样，你才容易入坑啊。</p>
<p><strong>篇幅优先，如果star超过 100， 再写一篇节点增加和更新的文章。</strong></p>
<h2 data-id="heading-16">写在最后</h2>
<p>写作不易，你的一赞一评就是我前行的最大动力。<br>
技术交流群，请加微信 dirge-cloud。</p>
<blockquote>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fdeveloper.mozilla.org%2Fzh-CN%2Fdocs%2FWeb%2FAPI%2FNode" target="_blank" rel="nofollow noopener noreferrer" title="https://developer.mozilla.org/zh-CN/docs/Web/API/Node" ref="nofollow noopener noreferrer">Node</a><br>
<a href="https://link.juejin.cn/?target=https%3A%2F%2Fdeveloper.mozilla.org%2Fzh-CN%2Fdocs%2FWeb%2FAPI%2FHTMLElement" target="_blank" rel="nofollow noopener noreferrer" title="https://developer.mozilla.org/zh-CN/docs/Web/API/HTMLElement" ref="nofollow noopener noreferrer">HTMLElement</a><br>
<a href="https://link.juejin.cn/?target=https%3A%2F%2Fdeveloper.mozilla.org%2Fzh-CN%2Fdocs%2FWeb%2FAPI%2FDocument%2FquerySelectorAll" target="_blank" rel="nofollow noopener noreferrer" title="https://developer.mozilla.org/zh-CN/docs/Web/API/Document/querySelectorAll" ref="nofollow noopener noreferrer">querySelectorAll</a></p>
</blockquote></div>  
</div>
            