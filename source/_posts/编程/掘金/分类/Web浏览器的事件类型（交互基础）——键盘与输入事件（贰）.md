
---
title: 'Web浏览器的事件类型（交互基础）——键盘与输入事件（贰）'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=8868'
author: 掘金
comments: false
date: Wed, 30 Jun 2021 07:36:08 GMT
thumbnail: 'https://picsum.photos/400/300?random=8868'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.8;font-weight:400;font-size:16px;word-spacing:2px;letter-spacing:2px;overflow-x:hidden;color:#3e3e3e;background-image:linear-gradient(90deg,rgba(50,0,0,.05) 3%,transparent 0),linear-gradient(1turn,rgba(50,0,0,.05) 3%,transparent 0);background-size:20px 20px;background-position:50%&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:1.2em;border-bottom:2px solid #ef7060;word-spacing:0!important;letter-spacing:0!important;font-size:inherit;line-height:inherit;display:block;font-weight:400;background:#ef7060;color:#fff;padding:10px;border-top-right-radius:3px;border-top-left-radius:3px;margin-right:3px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>这是我参与更文挑战的第<code>30</code>天，活动详情查看：<a href="https://juejin.cn/post/6967194882926444557" target="_blank">更文挑战</a></p>
<h3 data-id="heading-0">4.textInput事件</h3>
<p><code>DOM3 Events</code> 规范增加了一个名为 <code>textInput</code> 的事件，它在字符被输入到可编辑区域时触发。<code>textInput</code> 和 <code>keypress</code> 有两个区别：</p>
<ol>
<li>keypress 会在任何可以获得焦点的元素上触发，而 textInput 只在可以编辑区域触发。</li>
<li>textInput 只在新字符被插入时触发， keypress 对任何影像文本的操作都触发（包括退格键）。</li>
</ol>
<p>textInput 的 event 对象上提供了一个 data 属性，包含要插入的字符。使用方法如下所示：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">let</span> textbox = <span class="hljs-built_in">document</span>.getElementById(<span class="hljs-string">"myText"</span>);
textbox.addEventListener(<span class="hljs-string">"textInput"</span>, <span class="hljs-function">(<span class="hljs-params">event</span>) =></span> &#123;
  <span class="hljs-built_in">console</span>.log(event.data);
&#125;);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>event 对象上还有一个名为 inputMethod 的属性，该属性表示向控件中输入文本的手段。可能的
值如下：</p>
<ol start="0">
<li>表示浏览器不能确定是什么输入手段；</li>
<li>表示键盘；</li>
<li>表示粘贴；</li>
<li>表示拖放操作；</li>
<li>表示IME；</li>
<li>表示表单选项；</li>
<li>表示手写；</li>
<li>表示语音；</li>
<li>表示组合方式；</li>
<li>表示脚本；</li>
</ol>
<p>可以通过上面的值判断用户是如何输入值的。</p>
<h2 data-id="heading-1">合成事件</h2>
<p>合成事件是 <code>DOM3 Events</code> 中新增的，用于处理通常使用 <code>IME</code> （<code>Input Method Editors</code>）输入时的复杂输入序列。<code>IME</code> 可以让用户输入物理键盘上没有的字符。例如我们的中文就是通过很多字符组合生成的，也就是合成事件。</p>
<p>合成事件有以下<code>3</code>中：</p>
<ul>
<li><code>compositionstart</code>: 在 <code>IME</code> 的文本合成系统打开时触发，表示输入即将开始</li>
<li><code>compositionupdate</code>: 在新字符插入输入字段时触发</li>
<li><code>compositionend</code>: 在 <code>IME</code> 的文本合成系统关闭时触发，表示恢复正常键盘输入</li>
</ul>
<p>合成事件的 <code>event</code> 会新增一个 <code>data</code> 属性，包含以下几 <code>3</code> 中情况下的值：</p>
<ul>
<li>在 <code>compositionstart</code> 事件中，包含正在编辑的文本（例如，已经选择了文本但还没替换）；</li>
<li>在 <code>compositionupdate</code> 事件中，包含要插入的新字符；</li>
<li>在 <code>compositionend</code> 事件中，包含本次合成过程中输入的全部内容。</li>
</ul>
<p>合成使用方式如下：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">let</span> textbox = <span class="hljs-built_in">document</span>.getElementById(<span class="hljs-string">"myText"</span>);
textbox.addEventListener(<span class="hljs-string">"compositionstart"</span>, <span class="hljs-function">(<span class="hljs-params">event</span>) =></span> &#123;
  <span class="hljs-built_in">console</span>.log(event.data);
&#125;);
textbox.addEventListener(<span class="hljs-string">"compositionupdate"</span>, <span class="hljs-function">(<span class="hljs-params">event</span>) =></span> &#123;
  <span class="hljs-built_in">console</span>.log(event.data);
&#125;);
textbox.addEventListener(<span class="hljs-string">"compositionend"</span>, <span class="hljs-function">(<span class="hljs-params">event</span>) =></span> &#123;
  <span class="hljs-built_in">console</span>.log(event.data);
&#125;);
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-2">HTML5事件</h2>
<p><code>HTML5</code> 详尽地列出了浏览器支持的所有事件。下面会介绍浏览器较好支持的事件，但也并不是所有浏览器支持。</p>
<ol>
<li>contextmenu 事件</li>
</ol>
<p><code>contextmenu</code> 事件，以专门用于表示何时该显示上下文菜单，从而允许开发者取消默认的上下文菜单并提供自定义菜单。<code>contextmenu</code> 事件冒泡，因此只要给 <code>document</code> 指定一个事件处理程序就可以处理页面上的所有同类事件。<code>contextmenu</code> 事件应该算一种鼠标事件，因此 <code>event</code> 对象上的很多属性都与光标位置有关。来看下面的例子:</p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-meta"><!DOCTYPE <span class="hljs-meta-keyword">html</span>></span>
<span class="hljs-tag"><<span class="hljs-name">html</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">head</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">title</span>></span>ContextMenu Event Example<span class="hljs-tag"></<span class="hljs-name">title</span>></span>
  <span class="hljs-tag"></<span class="hljs-name">head</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">body</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">id</span>=<span class="hljs-string">"myDiv"</span>></span>
      Right click or Ctrl+click me to get a custom context menu. Click anywhere else to get the default context menu.
    <span class="hljs-tag"></<span class="hljs-name">div</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">ul</span>
      <span class="hljs-attr">id</span>=<span class="hljs-string">"myMenu"</span>
      <span class="hljs-attr">style</span>=<span class="hljs-string">"position: absolute; visibility: hidden; background-color: silver"</span>
    ></span>
      <span class="hljs-tag"><<span class="hljs-name">li</span>></span><span class="hljs-tag"><<span class="hljs-name">a</span> <span class="hljs-attr">href</span>=<span class="hljs-string">"http://www.somewhere.com"</span>></span> somewhere<span class="hljs-tag"></<span class="hljs-name">a</span>></span><span class="hljs-tag"></<span class="hljs-name">li</span>></span>
      <span class="hljs-tag"><<span class="hljs-name">li</span>></span><span class="hljs-tag"><<span class="hljs-name">a</span> <span class="hljs-attr">href</span>=<span class="hljs-string">"http://www.wrox.com"</span>></span>Wrox site<span class="hljs-tag"></<span class="hljs-name">a</span>></span><span class="hljs-tag"></<span class="hljs-name">li</span>></span>
      <span class="hljs-tag"><<span class="hljs-name">li</span>></span><span class="hljs-tag"><<span class="hljs-name">a</span> <span class="hljs-attr">href</span>=<span class="hljs-string">"http://www.somewhere-else.com"</span>></span>somewhere-else<span class="hljs-tag"></<span class="hljs-name">a</span>></span><span class="hljs-tag"></<span class="hljs-name">li</span>></span>
    <span class="hljs-tag"></<span class="hljs-name">ul</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">script</span>></span><span class="javascript">
      <span class="hljs-built_in">window</span>.addEventListener(<span class="hljs-string">"load"</span>, <span class="hljs-function">(<span class="hljs-params">event</span>) =></span> &#123;
        <span class="hljs-keyword">let</span> div = <span class="hljs-built_in">document</span>.getElementById(<span class="hljs-string">"myDiv"</span>);
        div.addEventListener(<span class="hljs-string">"contextmenu"</span>, <span class="hljs-function">(<span class="hljs-params">event</span>) =></span> &#123;
          event.preventDefault(); <span class="hljs-comment">// 阻止默认菜单的展示</span>
          <span class="hljs-comment">// 展示自定义的菜单</span>
          <span class="hljs-keyword">let</span> menu = <span class="hljs-built_in">document</span>.getElementById(<span class="hljs-string">"myMenu"</span>);
          menu.style.left = event.clientX + <span class="hljs-string">"px"</span>;
          menu.style.top = event.clientY + <span class="hljs-string">"px"</span>;
          menu.style.visibility = <span class="hljs-string">"visible"</span>;
        &#125;);
        <span class="hljs-built_in">document</span>.addEventListener(<span class="hljs-string">"click"</span>, <span class="hljs-function">(<span class="hljs-params">event</span>) =></span> &#123;
          <span class="hljs-built_in">document</span>.getElementById(<span class="hljs-string">"myMenu"</span>).style.visibility = <span class="hljs-string">"hidden"</span>;
        &#125;);
      &#125;);
    </span><span class="hljs-tag"></<span class="hljs-name">script</span>></span>
  <span class="hljs-tag"></<span class="hljs-name">body</span>></span>
<span class="hljs-tag"></<span class="hljs-name">html</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-3">引用</h2>
<p>[1] <a href="https://book.douban.com/subject/35175321/" target="_blank" rel="nofollow noopener noreferrer">JavaScript高级程序设计（第4版）</a></p></div>  
</div>
            