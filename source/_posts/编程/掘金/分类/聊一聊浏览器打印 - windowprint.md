
---
title: '聊一聊浏览器打印 - window.print'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=5898'
author: 掘金
comments: false
date: Sat, 17 Sep 2022 23:55:04 GMT
thumbnail: 'https://picsum.photos/400/300?random=5898'
---

<div>   
<div class="markdown-body cache"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:16px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:24px;margin-bottom:5px&#125;.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;font-size:20px&#125;.markdown-body h2&#123;padding-bottom:12px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h2 data-id="heading-0">前言</h2>
<p>一般信息填写类的需求页面，都会增设「预览」和「打印」功能。我们会通过编写 DOM 及样式来绘制出预览视图，而打印则是基于预览来生成 PDF 文件。</p>
<p>浏览器原生 API <code>window.print()</code> 可以用于打印当前窗口（window.document）视图内容。调用此方法会产生一个打印预览弹框，用户可以根据具体设置来得到打印结果。</p>
<p>接下来将从 code 层面带领大家熟悉「打印」的使用。</p>
<h2 data-id="heading-1">一、打印样式</h2>
<p>默认情况下，基于页面上的内容，会将元素，布局和样式都进行打印；</p>
<p>如果仅想在打印上设置特殊样式，可以通过以下方式：</p>
<ol>
<li>使用打印样式表：</li>
</ol>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">link</span> <span class="hljs-attr">href</span>=<span class="hljs-string">"print.css"</span> <span class="hljs-attr">media</span>=<span class="hljs-string">"print"</span> <span class="hljs-attr">rel</span>=<span class="hljs-string">"stylesheet"</span> /></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<ol start="2">
<li>使用媒介查询：</li>
</ol>
<pre><code class="hljs language-css copyable" lang="css"><span class="hljs-keyword">@media</span> print &#123;
  <span class="hljs-selector-tag">p</span>&#123;
    <span class="hljs-attribute">color</span>: lavender;
    <span class="hljs-attribute">background</span>: <span class="hljs-number">#ccc</span>;
  &#125;
  <span class="hljs-selector-tag">h1</span>&#123;
    <span class="hljs-attribute">color</span>: lightblue;
    <span class="hljs-attribute">background</span>: <span class="hljs-number">#ccc</span>;
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<ol start="3">
<li>使用内联 media 属性</li>
</ol>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">style</span> <span class="hljs-attr">media</span>=<span class="hljs-string">"print"</span>></span><span class="css">
  <span class="hljs-selector-tag">p</span>&#123;
    <span class="hljs-attribute">color</span>: lavender;
    <span class="hljs-attribute">background</span>: <span class="hljs-number">#ccc</span>;
  &#125;
  <span class="hljs-selector-tag">h1</span>&#123;
    <span class="hljs-attribute">color</span>: lightblue;
    <span class="hljs-attribute">background</span>: <span class="hljs-number">#ccc</span>;
  &#125;
</span><span class="hljs-tag"></<span class="hljs-name">style</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>默认情况下，元素的背景色不会被打印，可通过设置属性来支持：</p>
<pre><code class="hljs language-css copyable" lang="css"><span class="hljs-selector-tag">div</span>&#123;
  // Chrome、Safari 等 webkit 浏览器内核
  -webkit-print-<span class="hljs-attribute">color</span>-adjust: exact;
  // 火狐
  print-<span class="hljs-attribute">color</span>-adjust: exact;
  <span class="hljs-attribute">color</span>-adjust: exact;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-2">二、打印指定区域内容</h2>
<p>默认情况下，调用 window.print() 会对整个 document.body 进行打印，当需要打印指定容器内容时，可以通过以下几种方式：</p>
<h3 data-id="heading-3">1. 对容器进行打印</h3>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">body</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">id</span>=<span class="hljs-string">"container"</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">p</span>></span>这是一个段落<span class="hljs-tag"></<span class="hljs-name">p</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">h1</span>></span>这是一个标题<span class="hljs-tag"></<span class="hljs-name">h1</span>></span>
  <span class="hljs-tag"></<span class="hljs-name">div</span>></span>
  
  <span class="hljs-tag"><<span class="hljs-name">input</span> <span class="hljs-attr">type</span>=<span class="hljs-string">"button"</span> <span class="hljs-attr">value</span>=<span class="hljs-string">"打印此页面"</span> <span class="hljs-attr">onclick</span>=<span class="hljs-string">"printpage()"</span> /></span>

  <span class="hljs-tag"><<span class="hljs-name">script</span>></span><span class="javascript">
    <span class="hljs-keyword">const</span> <span class="hljs-title function_">printpage</span> = (<span class="hljs-params"></span>) => &#123;
      <span class="hljs-keyword">let</span> newstr = <span class="hljs-variable language_">document</span>.<span class="hljs-title function_">getElementById</span>(<span class="hljs-string">"container"</span>).<span class="hljs-property">innerHTML</span>;
      <span class="hljs-keyword">let</span> oldstr = <span class="hljs-variable language_">document</span>.<span class="hljs-property">body</span>.<span class="hljs-property">innerHTML</span>;
      <span class="hljs-variable language_">document</span>.<span class="hljs-property">body</span>.<span class="hljs-property">innerHTML</span> = newstr;
      <span class="hljs-variable language_">window</span>.<span class="hljs-title function_">print</span>();
      <span class="hljs-variable language_">document</span>.<span class="hljs-property">body</span>.<span class="hljs-property">innerHTML</span> = oldstr;
    &#125;
  </span><span class="hljs-tag"></<span class="hljs-name">script</span>></span>
<span class="hljs-tag"></<span class="hljs-name">body</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-4">2. 对容器内的部分内容进行打印</h3>
<p>当只需要打印容器内某一部分内容时，可以通过注释标识进行截取。</p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">body</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">id</span>=<span class="hljs-string">"container"</span>></span>
    <span class="hljs-comment"><!--startprint--></span>
    <span class="hljs-tag"><<span class="hljs-name">p</span>></span>这是一个段落<span class="hljs-tag"></<span class="hljs-name">p</span>></span>
    <span class="hljs-comment"><!--endprint--></span>
    <span class="hljs-tag"><<span class="hljs-name">h1</span>></span>这是一个标题<span class="hljs-tag"></<span class="hljs-name">h1</span>></span>
  <span class="hljs-tag"></<span class="hljs-name">div</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">input</span> <span class="hljs-attr">type</span>=<span class="hljs-string">"button"</span> <span class="hljs-attr">value</span>=<span class="hljs-string">"打印此页面"</span> <span class="hljs-attr">onclick</span>=<span class="hljs-string">"printpage()"</span> /></span>

  <span class="hljs-tag"><<span class="hljs-name">script</span>></span><span class="javascript">
    <span class="hljs-keyword">const</span> <span class="hljs-title function_">printpage</span> = (<span class="hljs-params"></span>) => &#123;
      <span class="hljs-keyword">let</span> oldStr = <span class="hljs-variable language_">window</span>.<span class="hljs-property">document</span>.<span class="hljs-property">body</span>.<span class="hljs-property">innerHTML</span>; <span class="hljs-comment">// 获取body的内容</span>
      <span class="hljs-keyword">let</span> start = <span class="hljs-string">"<!--startprint-->"</span>; <span class="hljs-comment">// 开始打印标识, 17个字符</span>
      <span class="hljs-keyword">let</span> end = <span class="hljs-string">"<!--endprint-->"</span>; <span class="hljs-comment">// 结束打印标识</span>
      <span class="hljs-keyword">let</span> newStr = oldStr.<span class="hljs-title function_">substr</span>(oldStr.<span class="hljs-title function_">indexOf</span>(start) + <span class="hljs-number">17</span>); <span class="hljs-comment">// 截取开始打印标识之后的内容</span>
      newStr = newStr.<span class="hljs-title function_">substring</span>(<span class="hljs-number">0</span>, newStr.<span class="hljs-title function_">indexOf</span>(end)); <span class="hljs-comment">// 截取开始打印标识和结束打印标识之间的内容</span>
      <span class="hljs-variable language_">window</span>.<span class="hljs-property">document</span>.<span class="hljs-property">body</span>.<span class="hljs-property">innerHTML</span> = newStr; <span class="hljs-comment">// 把需要打印的指定内容赋给body</span>
      <span class="hljs-variable language_">window</span>.<span class="hljs-title function_">print</span>(); <span class="hljs-comment">// 调用浏览器的打印功能打印指定区域</span>
      <span class="hljs-variable language_">window</span>.<span class="hljs-property">document</span>.<span class="hljs-property">body</span>.<span class="hljs-property">innerHTML</span> = oldStr; <span class="hljs-comment">// body替换为原来的内容</span>
    &#125;
  </span><span class="hljs-tag"></<span class="hljs-name">script</span>></span>
<span class="hljs-tag"></<span class="hljs-name">body</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-5">3. 监听打印前后事件</h3>
<p>通过监听打印前后事件，对不需要进行打印的元素进行隐藏和放开隐藏。</p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">body</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">id</span>=<span class="hljs-string">"container"</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">p</span>></span>这是一个段落<span class="hljs-tag"></<span class="hljs-name">p</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">h1</span> <span class="hljs-attr">id</span>=<span class="hljs-string">"title"</span>></span>这是一个标题<span class="hljs-tag"></<span class="hljs-name">h1</span>></span>
  <span class="hljs-tag"></<span class="hljs-name">div</span>></span>
  
  <span class="hljs-tag"><<span class="hljs-name">input</span> <span class="hljs-attr">type</span>=<span class="hljs-string">"button"</span> <span class="hljs-attr">value</span>=<span class="hljs-string">"打印此页面"</span> <span class="hljs-attr">onclick</span>=<span class="hljs-string">"printpage()"</span> /></span>

  <span class="hljs-tag"><<span class="hljs-name">script</span>></span><span class="javascript">
    <span class="hljs-keyword">const</span> <span class="hljs-title function_">printpage</span> = (<span class="hljs-params"></span>) => &#123;
      <span class="hljs-variable language_">window</span>.<span class="hljs-title function_">print</span>();
    &#125;

    <span class="hljs-variable language_">window</span>.<span class="hljs-property">onbeforeprint</span> = <span class="hljs-keyword">function</span>(<span class="hljs-params"></span>) &#123;
      <span class="hljs-comment">// 将一些不需要被打印的元素隐藏</span>
      <span class="hljs-variable language_">document</span>.<span class="hljs-title function_">getElementById</span>(<span class="hljs-string">'title'</span>).<span class="hljs-property">style</span>.<span class="hljs-property">display</span> = <span class="hljs-string">'none'</span>;
    &#125;
    <span class="hljs-variable language_">window</span>.<span class="hljs-property">onafterprint</span> = <span class="hljs-keyword">function</span>(<span class="hljs-params"></span>) &#123;
      <span class="hljs-comment">// 放开隐藏的元素</span>
      <span class="hljs-variable language_">document</span>.<span class="hljs-title function_">getElementById</span>(<span class="hljs-string">'title'</span>).<span class="hljs-property">style</span>.<span class="hljs-property">display</span> = <span class="hljs-string">'block'</span>;
    &#125;
  </span><span class="hljs-tag"></<span class="hljs-name">script</span>></span>
<span class="hljs-tag"></<span class="hljs-name">body</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-6">4. iframe</h3>
<p>上面几种方式都在当前窗口进行打印，并且都需要更改 document.body 内容，这会出现视图切换，带来的体验不是太好。</p>
<p>下面我们借助 iframe 来实现打印，并且不影响当前视窗的内容展示。</p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">body</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">id</span>=<span class="hljs-string">"container"</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">p</span>></span>这是一个段落<span class="hljs-tag"></<span class="hljs-name">p</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">h1</span> <span class="hljs-attr">id</span>=<span class="hljs-string">"title"</span>></span>这是一个标题<span class="hljs-tag"></<span class="hljs-name">h1</span>></span>
  <span class="hljs-tag"></<span class="hljs-name">div</span>></span>
  
  <span class="hljs-tag"><<span class="hljs-name">input</span> <span class="hljs-attr">type</span>=<span class="hljs-string">"button"</span> <span class="hljs-attr">value</span>=<span class="hljs-string">"打印此页面"</span> <span class="hljs-attr">onclick</span>=<span class="hljs-string">"printpage()"</span> /></span>

  <span class="hljs-tag"><<span class="hljs-name">script</span>></span><span class="javascript">
    <span class="hljs-keyword">const</span> <span class="hljs-title function_">printpage</span> = (<span class="hljs-params"></span>) => &#123;
      <span class="hljs-keyword">const</span> printContent = <span class="hljs-variable language_">document</span>.<span class="hljs-title function_">querySelector</span>(<span class="hljs-string">'#container'</span>).<span class="hljs-property">innerHTML</span>;
      <span class="hljs-keyword">const</span> iframe = <span class="hljs-variable language_">document</span>.<span class="hljs-title function_">createElement</span>(<span class="hljs-string">'iframe'</span>);
      iframe.<span class="hljs-title function_">setAttribute</span>(<span class="hljs-string">'style'</span>, <span class="hljs-string">'position: absolute; width: 0; height: 0;'</span>);
      <span class="hljs-variable language_">document</span>.<span class="hljs-property">body</span>.<span class="hljs-title function_">appendChild</span>(iframe);
      <span class="hljs-keyword">const</span> iframeDoc = iframe.<span class="hljs-property">contentWindow</span>.<span class="hljs-property">document</span>;
      <span class="hljs-comment">// 设置打印展示方式 - 横向展示</span>
      iframeDoc.<span class="hljs-title function_">write</span>(<span class="hljs-string">'<style media="print">@page &#123;size: landscape;&#125;</style>'</span>);
      <span class="hljs-comment">// 向 iframe 中注入 printContent 样式</span>
      iframeDoc.<span class="hljs-title function_">write</span>(<span class="hljs-string">`<link href="./print.css" media="print" rel="stylesheet" />`</span>);
      <span class="hljs-comment">// 写入内容</span>
      iframeDoc.<span class="hljs-title function_">write</span>(<span class="hljs-string">'<div>'</span> + printContent + <span class="hljs-string">'</div>'</span>);
      <span class="hljs-built_in">setTimeout</span>(<span class="hljs-keyword">function</span>(<span class="hljs-params"></span>)&#123;
        iframe.<span class="hljs-property">contentWindow</span>?.<span class="hljs-title function_">print</span>();
        <span class="hljs-variable language_">document</span>.<span class="hljs-property">body</span>.<span class="hljs-title function_">removeChild</span>(iframe);
      &#125;, <span class="hljs-number">50</span>);
    &#125;
  </span><span class="hljs-tag"></<span class="hljs-name">script</span>></span>
<span class="hljs-tag"></<span class="hljs-name">body</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<blockquote>
<p>值得注意的是，iframe 是一个新的 window 窗口，不会复用当前窗口的样式，需要为 iframe 注入打印内容所需的样式。</p>
</blockquote>
<h2 data-id="heading-7">三、强行插入分页</h2>
<p>当需要自定义打印分页时机时，可通过如下方式将指定 DOM 设为分割点。</p>
<ol>
<li>在指定元素前添加分页符</li>
</ol>
<pre><code class="hljs language-css copyable" lang="css"><span class="hljs-keyword">@media</span> print &#123;
  <span class="hljs-selector-tag">h1</span> &#123;
    <span class="hljs-attribute">page-break-before</span>: always;
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<ol start="2">
<li>在指定元素后添加分页符</li>
</ol>
<pre><code class="hljs language-css copyable" lang="css"><span class="hljs-keyword">@media</span> print &#123;
  <span class="hljs-selector-tag">h1</span> &#123;
    <span class="hljs-attribute">page-break-after</span>: always;
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-8">四、打印设置</h2>
<ol>
<li>设置打印布局</li>
</ol>
<pre><code class="hljs language-css copyable" lang="css"><span class="hljs-keyword">@media</span> print &#123;
  <span class="hljs-keyword">@page</span> &#123;
    <span class="hljs-comment">/* 纵向展示（高度展示内容更多） */</span>
    <span class="hljs-comment">/* size: portrait;  */</span>

    <span class="hljs-comment">/* 横向（宽度展示内容更大） */</span>
    size: landscape;

    <span class="hljs-comment">/* 打印的边距 上右下左 */</span>
    <span class="hljs-attribute">margin</span>: <span class="hljs-number">1cm</span> <span class="hljs-number">2cm</span> <span class="hljs-number">1cm</span> <span class="hljs-number">2cm</span>;
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-9">五、最佳实践（React）</h2>
<h3 data-id="heading-10">1. 背景：</h3>
<p>有一个信息填写页面，支持进行预览和打印，预览是一个 Dialog 弹框，打印取自于预览的内容。因此，在打印前，需要将预览内容呈现在 DOM 树上。</p>
<h3 data-id="heading-11">2. 思路：</h3>
<ul>
<li>点击打印，将预览 Dialog open state 设置为 true，Dialog 渲染到 DOM 树上；</li>
<li>执行 setTimeout 延迟任务，在 Dialog 渲染在 DOM 树上后对其隐藏（disabled: none），目的是实现视图上不展示 Dialog；</li>
<li>创建 iframe，并将 Dialog 内容及其样式，写入 iframe.document 中；</li>
<li>执行 iframe.contentWindow.print() 进行打印；</li>
<li>打印完成后做一些重置处理：移除 iframe、将 Dialog 隐藏逻辑去掉、将 Dialog open state 置为 false；</li>
<li>这样，在不影响现有页面内容的展示，同时实现了打印 Dialog 内容。</li>
</ul>
<h3 data-id="heading-12">3. 实现：</h3>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> <span class="hljs-title function_">printFocus</span> = (<span class="hljs-params"></span>) => &#123; <span class="hljs-comment">// 打印事件</span>
  <span class="hljs-comment">// 1. 挂载要打印的内容</span>
  <span class="hljs-title function_">setPreviewOpen</span>(<span class="hljs-literal">true</span>);

  <span class="hljs-built_in">setTimeout</span>(<span class="hljs-function">() =></span> &#123; <span class="hljs-comment">// 延迟，等待 Dialog 渲染在 DOM 树上</span>
    <span class="hljs-comment">// 2. 隐藏要打印的内容</span>
    <span class="hljs-keyword">const</span> container = <span class="hljs-variable language_">document</span>.<span class="hljs-title function_">querySelector</span>(<span class="hljs-string">'.preview-wrapper'</span>);
    container.<span class="hljs-title function_">setAttribute</span>(<span class="hljs-string">'style'</span>, <span class="hljs-string">'display: none;'</span>);

    <span class="hljs-comment">// 3. 创建 iframe</span>
    <span class="hljs-keyword">const</span> iframe = <span class="hljs-variable language_">document</span>.<span class="hljs-title function_">createElement</span>(<span class="hljs-string">'iframe'</span>);
    <span class="hljs-keyword">const</span> printContent = container.<span class="hljs-property">innerHTML</span>;
    iframe.<span class="hljs-title function_">setAttribute</span>(<span class="hljs-string">'style'</span>, <span class="hljs-string">'position: absolute; width: 0; height: 0;'</span>);
    <span class="hljs-variable language_">document</span>.<span class="hljs-property">body</span>.<span class="hljs-title function_">appendChild</span>(iframe);
    <span class="hljs-keyword">const</span> doc = iframe.<span class="hljs-property">contentWindow</span>.<span class="hljs-property">document</span>;

    <span class="hljs-comment">// 4. 写入内容</span>
    doc.<span class="hljs-title function_">write</span>(<span class="hljs-string">'<style media="print">@page &#123;size: landscape;&#125;</style>'</span>);
    doc.<span class="hljs-title function_">write</span>(<span class="hljs-string">`<link href="./preview-focus.css" media="print" rel="stylesheet" />`</span>);
    doc.<span class="hljs-title function_">write</span>(<span class="hljs-string">'<div>'</span> + printContent + <span class="hljs-string">'</div>'</span>);

    <span class="hljs-built_in">setTimeout</span>(<span class="hljs-keyword">function</span>(<span class="hljs-params"></span>)&#123;
      <span class="hljs-comment">// 5. 执行打印</span>
      iframe.<span class="hljs-property">contentWindow</span>.<span class="hljs-title function_">print</span>();
      <span class="hljs-comment">// 6. 重置工作</span>
      <span class="hljs-variable language_">document</span>.<span class="hljs-property">body</span>.<span class="hljs-title function_">removeChild</span>(iframe);
      <span class="hljs-title function_">setPreviewOpen</span>(<span class="hljs-literal">false</span>);
      container.<span class="hljs-title function_">removeAttribute</span>(<span class="hljs-string">'style'</span>);
    &#125;, <span class="hljs-number">50</span>);
  &#125;, <span class="hljs-number">0</span>);
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-13">参考：</h2>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fblog.csdn.net%2Fwunengneng%2Farticle%2Fdetails%2F109853361" target="_blank" rel="nofollow noopener noreferrer" title="https://blog.csdn.net/wunengneng/article/details/109853361" ref="nofollow noopener noreferrer">1. 打印背景色丢失解决方案</a><br>
<a href="https://juejin.cn/post/6844904009271083021" target="_blank" title="https://juejin.cn/post/6844904009271083021">2. window.print() 前端实现网页打印详解</a></p></div>  
</div>
            