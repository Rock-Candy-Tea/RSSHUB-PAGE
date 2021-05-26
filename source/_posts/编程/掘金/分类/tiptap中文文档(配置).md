
---
title: 'tiptap中文文档(配置)'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=3336'
author: 掘金
comments: false
date: Tue, 25 May 2021 22:30:26 GMT
thumbnail: 'https://picsum.photos/400/300?random=3336'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h2 data-id="heading-0">入门指南</h2>
<h3 data-id="heading-1">配置</h3>
<h4 data-id="heading-2">介绍</h4>
<p>在初始化新编辑器时，可以控制一些事情。在大多数情况下，只需说明应在何处呈现tiptap（元素）、要启用哪些功能（扩展）以及初始文档应是什么（内容）。不过，还可以配置一些功能。让我们看一个完全配置的编辑器示例。</p>
<h4 data-id="heading-3">编辑器配置</h4>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">import</span> &#123; Editor &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'@tiptap/core'</span>
<span class="hljs-keyword">import</span> Document <span class="hljs-keyword">from</span> <span class="hljs-string">'@tiptap/extension-document'</span>
<span class="hljs-keyword">import</span> Paragraph <span class="hljs-keyword">from</span> <span class="hljs-string">'@tiptap/extension-paragraph'</span>
<span class="hljs-keyword">import</span> Text <span class="hljs-keyword">from</span> <span class="hljs-string">'@tiptap/extension-text'</span>

<span class="hljs-keyword">new</span> Editor(&#123;
  <span class="hljs-attr">element</span>: <span class="hljs-built_in">document</span>.querySelector(<span class="hljs-string">'.element'</span>),
  <span class="hljs-attr">extensions</span>: [
    Document,
    Paragraph,
    Text,
  ],
  <span class="hljs-attr">content</span>: <span class="hljs-string">'<p>Example Text</p>'</span>,
  <span class="hljs-attr">autofocus</span>: <span class="hljs-literal">true</span>,
  <span class="hljs-attr">editable</span>: <span class="hljs-literal">true</span>,
  <span class="hljs-attr">injectCSS</span>: <span class="hljs-literal">false</span>,
&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>初始化：</p>
<ul>
<li>绑定HTML元素</li>
<li>加载扩展，如Document、Paragraph、Text</li>
<li>初始化content</li>
<li>初始化之后光标聚焦设置</li>
<li>使文本可编辑(默认可编辑),禁用默认的CSS加载</li>
</ul>
<h4 data-id="heading-4">节点、标记和扩展</h4>
<p>大多数功能都打包到节点、标记和扩展中。导入所需内容并将它们作为数组传递给编辑器，就可以开始了。以下是只有三个扩展名的最小设置：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">import</span> &#123; Editor &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'@tiptap/core'</span>
<span class="hljs-keyword">import</span> Document <span class="hljs-keyword">from</span> <span class="hljs-string">'@tiptap/extension-document'</span>
<span class="hljs-keyword">import</span> Paragraph <span class="hljs-keyword">from</span> <span class="hljs-string">'@tiptap/extension-paragraph'</span>
<span class="hljs-keyword">import</span> Text <span class="hljs-keyword">from</span> <span class="hljs-string">'@tiptap/extension-text'</span>

<span class="hljs-keyword">new</span> Editor(&#123;
  <span class="hljs-attr">element</span>: <span class="hljs-built_in">document</span>.querySelector(<span class="hljs-string">'.element'</span>),
  <span class="hljs-attr">extensions</span>: [
    Document,
    Paragraph,
    Text,
  ],
&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-5">扩展配置</h4>
<p>大多数扩展都可以配置。添加一个configure方法将对象传递给它。以下示例将禁用默认的标题级别4、5和6：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">import</span> &#123; Editor &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'@tiptap/core'</span>
<span class="hljs-keyword">import</span> Document <span class="hljs-keyword">from</span> <span class="hljs-string">'@tiptap/extension-document'</span>
<span class="hljs-keyword">import</span> Paragraph <span class="hljs-keyword">from</span> <span class="hljs-string">'@tiptap/extension-paragraph'</span>
<span class="hljs-keyword">import</span> Text <span class="hljs-keyword">from</span> <span class="hljs-string">'@tiptap/extension-text'</span>
<span class="hljs-keyword">import</span> Heading <span class="hljs-keyword">from</span> <span class="hljs-string">'@tiptap/extension-heading'</span>

<span class="hljs-keyword">new</span> Editor(&#123;
  <span class="hljs-attr">element</span>: <span class="hljs-built_in">document</span>.querySelector(<span class="hljs-string">'.element'</span>),
  <span class="hljs-attr">extensions</span>: [
    Document,
    Paragraph,
    Text,
    Heading.configure(&#123;
      <span class="hljs-attr">levels</span>: [<span class="hljs-number">1</span>, <span class="hljs-number">2</span>, <span class="hljs-number">3</span>],
    &#125;),
  ],
&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-6">默认扩展</h4>
<p>我们已经组合了一些最常见的扩展，并提供了一个StarterKit扩展来加载它们。下面是如何使用它：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">import</span> StarterKit <span class="hljs-keyword">from</span> <span class="hljs-string">'@tiptap/starter-kit'</span>

<span class="hljs-keyword">new</span> Editor(&#123;
  <span class="hljs-attr">extensions</span>: [
    StarterKit,
  ],
&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>甚至可以将所有默认扩展的配置作为对象传递。只需在配置前面加上扩展名：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">import</span> StarterKit <span class="hljs-keyword">from</span> <span class="hljs-string">'@tiptap/starter-kit'</span>

<span class="hljs-keyword">new</span> Editor(&#123;
  <span class="hljs-attr">extensions</span>: StarterKit.configure(&#123;
    <span class="hljs-attr">heading</span>: &#123;
      <span class="hljs-attr">levels</span>: [<span class="hljs-number">1</span>, <span class="hljs-number">2</span>, <span class="hljs-number">3</span>],
    &#125;,
  &#125;),
&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>StarterKit扩展包含扩展列表。如果要加载它们并添加一些自定义扩展，可以这样编写：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">import</span> StarterKit <span class="hljs-keyword">from</span> <span class="hljs-string">'@tiptap/starter-kit'</span>
<span class="hljs-keyword">import</span> Strike <span class="hljs-keyword">from</span> <span class="hljs-string">'@tiptap/extension-strike'</span>

<span class="hljs-keyword">new</span> Editor(&#123;
  <span class="hljs-attr">extensions</span>: [
    StarterKit,
    Strike,
  ],
&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>过滤特定扩展</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">import</span> StarterKit <span class="hljs-keyword">from</span> <span class="hljs-string">'@tiptap/starter-kit'</span>

<span class="hljs-keyword">new</span> Editor(&#123;
  <span class="hljs-attr">extensions</span>: [
    StarterKit.configure(&#123;
      <span class="hljs-attr">history</span>: <span class="hljs-literal">false</span>,
    &#125;),
  ],
&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>您可能会在协作编辑示例中看到类似的内容。协作有自己的历史扩展，您需要删除默认的历史扩展以避免冲突。</p>
<h3 data-id="heading-7">创建菜单</h3>
<h4 data-id="heading-8">菜单</h4>
<p>编辑器提供了一个流畅的API来触发命令和添加活动状态。你可以使用任何你喜欢的标记。为了使行菜单的定位更容易，我们提供了一些实用程序和组件。让我们逐一介绍最典型的用例。</p>
<h4 data-id="heading-9">固定菜单</h4>
<p>一个固定的菜单，例如在编辑器的顶部，可以是任何东西。我们不提供这样的菜单。只需添加一个<div>和几个<button>。下面将解释这些按钮如何触发命令。</p>
<h4 data-id="heading-10">气泡菜单</h4>
<p>选择文本时出现气泡菜单。标记和样式完全由您决定。</p></div>  
</div>
            