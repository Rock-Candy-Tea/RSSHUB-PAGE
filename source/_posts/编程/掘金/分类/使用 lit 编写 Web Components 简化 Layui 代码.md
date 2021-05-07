
---
title: '使用 lit 编写 Web Components 简化 Layui 代码'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=3151'
author: 掘金
comments: false
date: Thu, 06 May 2021 03:34:37 GMT
thumbnail: 'https://picsum.photos/400/300?random=3151'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h1 data-id="heading-0">Layui 介绍</h1>
<p>Layui 是一套开源的 Web UI 解决方案，主要面向的是不熟悉前端开发的后端开发人员，使用这套框架可以大大提升后台系统的开发效率，这套框架也有其不足之处，其未采用现代化的前端开发方式，而使用的是原生 html、css、js 的编写方式，所以许多前端工程师认为这套框架在技术上并没有多少创新之处并且也不适用于大型项目，这些看法并没有问题，但 Layui 也有其优势，毕竟许多后台系统或个人项目用不上太过复杂的前端技术。</p>
<p>在后台系统开发的初期，只需按照 Layui 提供的文档和 demo 依葫芦画瓢即可完成功能开发，但在系统功能越来越多的情况下，会发现存在许多重复模式的代码，比如下面的一个表单 html 代码片段。</p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">form</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"layui-form"</span> <span class="hljs-attr">action</span>=<span class="hljs-string">""</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"layui-inline"</span>></span><span class="hljs-tag"></<span class="hljs-name">div</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"layui-form-item"</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">label</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"layui-form-label"</span>></span>名称:<span class="hljs-tag"></<span class="hljs-name">label</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"layui-input-block"</span> <span class="hljs-attr">style</span>=<span class="hljs-string">"width: 200px"</span>></span>
      <span class="hljs-tag"><<span class="hljs-name">input</span>
        <span class="hljs-attr">type</span>=<span class="hljs-string">"text"</span>
        <span class="hljs-attr">name</span>=<span class="hljs-string">"name"</span>
        <span class="hljs-attr">class</span>=<span class="hljs-string">"layui-input"</span>
        <span class="hljs-attr">autocomplete</span>=<span class="hljs-string">"off"</span>
        <span class="hljs-attr">lay-verify</span>=<span class="hljs-string">"required"</span>
      /></span>
    <span class="hljs-tag"></<span class="hljs-name">div</span>></span>
  <span class="hljs-tag"></<span class="hljs-name">div</span>></span>

  <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"layui-inline"</span>></span><span class="hljs-tag"></<span class="hljs-name">div</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"layui-form-item"</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">label</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"layui-form-label"</span>></span>编码:<span class="hljs-tag"></<span class="hljs-name">label</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"layui-input-block"</span> <span class="hljs-attr">style</span>=<span class="hljs-string">"width: 200px"</span>></span>
      <span class="hljs-tag"><<span class="hljs-name">input</span>
        <span class="hljs-attr">type</span>=<span class="hljs-string">"text"</span>
        <span class="hljs-attr">name</span>=<span class="hljs-string">"sourceCode"</span>
        <span class="hljs-attr">class</span>=<span class="hljs-string">"layui-input"</span>
        <span class="hljs-attr">autocomplete</span>=<span class="hljs-string">"off"</span>
        <span class="hljs-attr">lay-verify</span>=<span class="hljs-string">"required"</span>
      /></span>
    <span class="hljs-tag"></<span class="hljs-name">div</span>></span>
  <span class="hljs-tag"></<span class="hljs-name">div</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"layui-form-item"</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"layui-input-block"</span>></span>
      <span class="hljs-tag"><<span class="hljs-name">button</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"layui-btn"</span> <span class="hljs-attr">lay-submit</span>=<span class="hljs-string">""</span> <span class="hljs-attr">lay-filter</span>=<span class="hljs-string">"save"</span>></span>保存<span class="hljs-tag"></<span class="hljs-name">button</span>></span>
      <span class="hljs-tag"><<span class="hljs-name">button</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"layui-btn layui-btn-primary"</span> <span class="hljs-attr">id</span>=<span class="hljs-string">"cancel"</span> <span class="hljs-attr">type</span>=<span class="hljs-string">"button"</span>></span>
        取消
      <span class="hljs-tag"></<span class="hljs-name">button</span>></span>
    <span class="hljs-tag"></<span class="hljs-name">div</span>></span>
  <span class="hljs-tag"></<span class="hljs-name">div</span>></span>
<span class="hljs-tag"></<span class="hljs-name">form</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这种写法相比组件化开发的 React 或 Vue 确实差了许多，我们可以在 Layui 后台中引入 React 或 Vue 来混合使用，但这样一来增加了复杂性和学习成本，毕竟选用 Layui 作为后台框架的开发人员大多数是不熟悉前端开发的，那么在这种情况下，有没有一种方式在不增加多少复杂性和学习成本的前提下使得项目能应用上组件开发呢？答案是有的，Web Components 就是其中一个，其比 React 简单，且受浏览器原生支持。</p>
<h1 data-id="heading-1">Web Components 介绍</h1>
<p>随着 React 等技术的流行，前端工程化的发展越来越快，浏览器也在不断适应这种发展并且逐步开始原生支持一些优秀的技术，比如组件化开发，谷歌作为 Chrome 浏览器的拥有者，一直在推进 Web Components 技术的发展，目前许多主流浏览器已经支持 Web Components 技术。关于 Web Components 的简介可参考 <a href="http://www.ruanyifeng.com/blog/2019/08/web_components.html" target="_blank" rel="nofollow noopener noreferrer">www.ruanyifeng.com/blog/2019/0…</a> 这篇博客。</p>
<p>我们通过一个 hello world 示例来直观的看看 Web Components 的写法。</p>
<pre><code class="hljs language-js copyable" lang="js"><html>
<span class="xml"><span class="hljs-tag"><<span class="hljs-name">head</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">script</span>></span><span class="javascript">
  <span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">HelloWorld</span> <span class="hljs-keyword">extends</span> <span class="hljs-title">HTMLElement</span> </span>&#123;
    <span class="hljs-function"><span class="hljs-title">constructor</span>(<span class="hljs-params"></span>)</span> &#123;
      <span class="hljs-built_in">super</span>();
      <span class="hljs-comment">// Attach a shadow root to the element.</span>
      <span class="hljs-keyword">let</span> shadowRoot = <span class="hljs-built_in">this</span>.attachShadow(&#123;<span class="hljs-attr">mode</span>: <span class="hljs-string">'open'</span>&#125;);
      shadowRoot.innerHTML = <span class="hljs-string">`<p>hello world</p>`</span>;
    &#125;
  &#125;
  customElements.define(<span class="hljs-string">'hello-world'</span>, HelloWorld);
  </span><span class="hljs-tag"></<span class="hljs-name">script</span>></span>
<span class="hljs-tag"></<span class="hljs-name">head</span>></span></span>
<span class="xml"><span class="hljs-tag"><<span class="hljs-name">body</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">hello-world</span>></span><span class="hljs-tag"></<span class="hljs-name">hello-world</span>></span>
<span class="hljs-tag"></<span class="hljs-name">body</span>></span></span>
</html>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这个示例很简单，但是细心的朋友还是会发现一些问题，比如上图中的 innerHTML 写的是字符串，这对于复杂组件的开发必然是不利的，虽然可以通过 template 标记来解决但仍然不是很好的方式，为了解决这类问题，谷歌开源了 <a href="https://github.com/lit/lit" target="_blank" rel="nofollow noopener noreferrer">lit</a> 项目，使用这个组件可以让开发 Web 组件更加简便，当然其学习成本是很低的。</p>
<h1 data-id="heading-2">lit 介绍</h1>
<p>使用 lit 可以简化 Web 组件的开发，我们直接看一个示例代码。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">import</span> &#123;html, css, LitElement&#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'lit'</span>;
​
<span class="hljs-keyword">export</span> <span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">SimpleGreeting</span> <span class="hljs-keyword">extends</span> <span class="hljs-title">LitElement</span> </span>&#123;
  <span class="hljs-keyword">static</span> <span class="hljs-keyword">get</span> <span class="hljs-title">styles</span>() &#123;
    <span class="hljs-keyword">return</span> css`<span class="css"><span class="hljs-selector-tag">p</span> &#123; <span class="hljs-attribute">color</span>: blue &#125;`</span>;
  &#125;
​
  <span class="hljs-keyword">static</span> <span class="hljs-keyword">get</span> <span class="hljs-title">properties</span>() &#123;
    <span class="hljs-keyword">return</span> &#123;
      <span class="hljs-attr">name</span>: &#123;<span class="hljs-attr">type</span>: <span class="hljs-built_in">String</span>&#125;
    &#125;
  &#125;
​
  <span class="hljs-function"><span class="hljs-title">constructor</span>(<span class="hljs-params"></span>)</span> &#123;
    <span class="hljs-built_in">super</span>();
    <span class="hljs-built_in">this</span>.name = <span class="hljs-string">'Somebody'</span>;
  &#125;
​
  <span class="hljs-function"><span class="hljs-title">render</span>(<span class="hljs-params"></span>)</span> &#123;
    <span class="hljs-keyword">return</span> html`<span class="xml"><span class="hljs-tag"><<span class="hljs-name">p</span>></span>Hello, </span><span class="hljs-subst">$&#123;<span class="hljs-built_in">this</span>.name&#125;</span><span class="xml">!<span class="hljs-tag"></<span class="hljs-name">p</span>></span>`</span>;
  &#125;
&#125;
​
customElements.define(<span class="hljs-string">'simple-greeting'</span>, SimpleGreeting);
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">simple-greeting</span> <span class="hljs-attr">name</span>=<span class="hljs-string">"World"</span>></span><span class="hljs-tag"></<span class="hljs-name">simple-greeting</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这个示例相比前面的略微复杂一些，但增加了属性、样式和表达式的用法，这个简单的例子让我们已经有了大部分组件化开发的能力，下面就让我们使用 lit 编写 Web Components 来封装 Layui 代码。</p>
<h1 data-id="heading-3">lit 结合 Layui</h1>
<p>在后台系统中，列表页是最常见的功能之一，列表页上多数情况下也有搜索表单，我们先看使用 Layui 时的一个普遍写法，下面的代码包含列表查询、打开增加或修改窗口的代码。</p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"layui-fluid"</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"layui-row layui-col-space10"</span> <span class="hljs-attr">style</span>=<span class="hljs-string">"margin-top: 5px"</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">form</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"layui-form"</span> <span class="hljs-attr">action</span>=<span class="hljs-string">""</span>></span>
      <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"layui-input-inline"</span>></span>名称<span class="hljs-tag"></<span class="hljs-name">div</span>></span>
      <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"layui-input-inline"</span> <span class="hljs-attr">style</span>=<span class="hljs-string">"width: 120px"</span>></span>
        <span class="hljs-tag"><<span class="hljs-name">input</span>
          <span class="hljs-attr">type</span>=<span class="hljs-string">"text"</span>
          <span class="hljs-attr">class</span>=<span class="hljs-string">"layui-input"</span>
          <span class="hljs-attr">name</span>=<span class="hljs-string">"name"</span>
          <span class="hljs-attr">placeholder</span>=<span class="hljs-string">"请输入名称"</span>
          <span class="hljs-attr">value</span>=<span class="hljs-string">""</span>
        /></span>
      <span class="hljs-tag"></<span class="hljs-name">div</span>></span>
      <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"layui-input-inline"</span>></span>
        <span class="hljs-tag"><<span class="hljs-name">button</span>
          <span class="hljs-attr">class</span>=<span class="hljs-string">"layui-btn"</span>
          <span class="hljs-attr">id</span>=<span class="hljs-string">"searchBtn"</span>
          <span class="hljs-attr">lay-submit</span>=<span class="hljs-string">""</span>
          <span class="hljs-attr">lay-filter</span>=<span class="hljs-string">"search"</span>
        ></span>
          搜索
        <span class="hljs-tag"></<span class="hljs-name">button</span>></span>
      <span class="hljs-tag"></<span class="hljs-name">div</span>></span>
    <span class="hljs-tag"></<span class="hljs-name">form</span>></span>
  <span class="hljs-tag"></<span class="hljs-name">div</span>></span>

  <span class="hljs-comment"><!--定义表格--></span>
  <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"layui-row"</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">table</span> <span class="hljs-attr">id</span>=<span class="hljs-string">"tb"</span> <span class="hljs-attr">lay-filter</span>=<span class="hljs-string">"Lay"</span>></span><span class="hljs-tag"></<span class="hljs-name">table</span>></span>
  <span class="hljs-tag"></<span class="hljs-name">div</span>></span>
<span class="hljs-tag"></<span class="hljs-name">div</span>></span>

<span class="hljs-tag"><<span class="hljs-name">script</span> <span class="hljs-attr">type</span>=<span class="hljs-string">"text/html"</span> <span class="hljs-attr">id</span>=<span class="hljs-string">"toolbar"</span>></span><span class="handlebars"><span class="xml">
  <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"layui-btn-container"</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">button</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"layui-btn layui-btn-sm"</span> <span class="hljs-attr">lay-event</span>=<span class="hljs-string">"addBtn"</span>></span>添加<span class="hljs-tag"></<span class="hljs-name">button</span>></span>
  <span class="hljs-tag"></<span class="hljs-name">div</span>></span>
</span></span><span class="hljs-tag"></<span class="hljs-name">script</span>></span>
<span class="hljs-tag"><<span class="hljs-name">script</span> <span class="hljs-attr">type</span>=<span class="hljs-string">"text/html"</span> <span class="hljs-attr">id</span>=<span class="hljs-string">"bar"</span>></span><span class="handlebars"><span class="xml">
  <span class="hljs-tag"><<span class="hljs-name">a</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"layui-btn layui-btn-xs"</span> <span class="hljs-attr">lay-event</span>=<span class="hljs-string">"edit"</span>></span>修改<span class="hljs-tag"></<span class="hljs-name">a</span>></span>
</span></span><span class="hljs-tag"></<span class="hljs-name">script</span>></span>

<span class="hljs-tag"><<span class="hljs-name">script</span>></span><span class="javascript">
  layui.use([<span class="hljs-string">"form"</span>, <span class="hljs-string">"table"</span>, <span class="hljs-string">"laytpl"</span>], <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params"></span>) </span>&#123;
    <span class="hljs-keyword">var</span> form = layui.form,
      table = layui.table,
      layer = parent.layer === <span class="hljs-literal">undefined</span> ? layui.layer : parent.layer,
      $ = layui.jquery;

    <span class="hljs-keyword">var</span> tableIns = table.render(&#123;
      <span class="hljs-attr">elem</span>: <span class="hljs-string">"#tb"</span>,
      <span class="hljs-attr">toolbar</span>: <span class="hljs-string">"#toolbar"</span>,
      <span class="hljs-attr">defaultToolbar</span>: [],
      <span class="hljs-attr">even</span>: <span class="hljs-literal">true</span>,
      <span class="hljs-attr">url</span>: <span class="hljs-string">"/getList"</span>, <span class="hljs-comment">//数据接口</span>
      <span class="hljs-attr">page</span>: &#123;
        <span class="hljs-attr">limit</span>: <span class="hljs-number">20</span>,
      &#125;,
      <span class="hljs-attr">method</span>: <span class="hljs-string">"post"</span>,
      <span class="hljs-attr">height</span>: <span class="hljs-string">"full-40"</span>,
      <span class="hljs-attr">request</span>: &#123;
        <span class="hljs-attr">pageName</span>: <span class="hljs-string">"page"</span>, <span class="hljs-comment">//页码的参数名称，默认：page</span>
        <span class="hljs-attr">limitName</span>: <span class="hljs-string">"pageSize"</span>, <span class="hljs-comment">//每页数据量的参数名，默认：limit</span>
      &#125;,
      <span class="hljs-attr">contentType</span>: <span class="hljs-string">"application/json"</span>,
      <span class="hljs-attr">parseData</span>: <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params">res</span>) </span>&#123;
        <span class="hljs-keyword">var</span> data = &#123;
          <span class="hljs-attr">code</span>: res.code, <span class="hljs-comment">//解析接口状态</span>
          <span class="hljs-attr">msg</span>: res.message, <span class="hljs-comment">//解析提示文本</span>
          <span class="hljs-attr">count</span>: <span class="hljs-number">0</span>, <span class="hljs-comment">//解析数据长度</span>
          <span class="hljs-attr">data</span>: <span class="hljs-literal">null</span>, <span class="hljs-comment">//解析数据列表</span>
        &#125;;
        <span class="hljs-keyword">if</span> (res.code == <span class="hljs-number">200</span>) &#123;
          data = &#123;
            <span class="hljs-attr">code</span>: <span class="hljs-number">0</span>, <span class="hljs-comment">//解析接口状态</span>
            <span class="hljs-attr">msg</span>: res.message, <span class="hljs-comment">//解析提示文本</span>
            <span class="hljs-attr">count</span>: res.data.total, <span class="hljs-comment">//解析数据长度</span>
            <span class="hljs-attr">data</span>: res.data.list, <span class="hljs-comment">//解析数据列表</span>
          &#125;;
        &#125;
        <span class="hljs-keyword">return</span> data;
      &#125;,
      <span class="hljs-attr">cols</span>: [
        [
          &#123; <span class="hljs-attr">field</span>: <span class="hljs-string">"name"</span>, <span class="hljs-attr">title</span>: <span class="hljs-string">"名称"</span>, <span class="hljs-attr">align</span>: <span class="hljs-string">"center"</span> &#125;,
          &#123; <span class="hljs-attr">field</span>: <span class="hljs-string">"code"</span>, <span class="hljs-attr">title</span>: <span class="hljs-string">"编码"</span>, <span class="hljs-attr">align</span>: <span class="hljs-string">"center"</span> &#125;,
        ],
      ],
      <span class="hljs-attr">done</span>: <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params">res</span>) </span>&#123;
        <span class="hljs-keyword">if</span> (res.code != <span class="hljs-number">0</span>) &#123;
          alert(res.msg);
        &#125;
      &#125;,
    &#125;);

    <span class="hljs-comment">//对表格工具栏的操作</span>
    table.on(<span class="hljs-string">"tool(Lay)"</span>, <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params">obj</span>) </span>&#123;
      <span class="hljs-keyword">var</span> data = obj.data, <span class="hljs-comment">//获得当前行数据</span>
        layEvent = obj.event; <span class="hljs-comment">//获得 lay-event 对应的值</span>
      <span class="hljs-keyword">if</span> (layEvent === <span class="hljs-string">"edit"</span>) &#123;
        layer.open(&#123;
          <span class="hljs-attr">title</span>: <span class="hljs-string">"编辑"</span>,
          <span class="hljs-attr">type</span>: <span class="hljs-number">2</span>,
          <span class="hljs-attr">shadeClose</span>: <span class="hljs-literal">false</span>,
          <span class="hljs-attr">maxmin</span>: <span class="hljs-literal">false</span>,
          <span class="hljs-attr">area</span>: [<span class="hljs-string">"450px"</span>, <span class="hljs-string">"550px"</span>],
          <span class="hljs-attr">shift</span>: <span class="hljs-number">0</span>,
          <span class="hljs-attr">content</span>: <span class="hljs-string">"edit.html?id="</span> + data.id,
          <span class="hljs-attr">end</span>: <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params"></span>) </span>&#123;
            tableIns.reload();
          &#125;,
        &#125;);
      &#125;
    &#125;);
    <span class="hljs-comment">//查询</span>
    form.on(<span class="hljs-string">"submit(search)"</span>, <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params">data</span>) </span>&#123;
      <span class="hljs-keyword">var</span> options = &#123;
        <span class="hljs-attr">where</span>: &#123;
          <span class="hljs-attr">params</span>: &#123;
            <span class="hljs-attr">name</span>: data.field.name,
          &#125;,
        &#125;,
      &#125;;
      tableIns.reload(options);
      <span class="hljs-keyword">return</span> <span class="hljs-literal">false</span>;
    &#125;);

    <span class="hljs-comment">//头工具栏事件</span>
    table.on(<span class="hljs-string">"toolbar(Lay)"</span>, <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params">obj</span>) </span>&#123;
      <span class="hljs-keyword">if</span> (obj.event == <span class="hljs-string">"addBtn"</span>) &#123;
        layer.open(&#123;
          <span class="hljs-attr">title</span>: <span class="hljs-string">"添加"</span>,
          <span class="hljs-attr">type</span>: <span class="hljs-number">2</span>,
          <span class="hljs-attr">shadeClose</span>: <span class="hljs-literal">false</span>,
          <span class="hljs-attr">maxmin</span>: <span class="hljs-literal">false</span>,
          <span class="hljs-attr">area</span>: [<span class="hljs-string">"450px"</span>, <span class="hljs-string">"550px"</span>],
          <span class="hljs-attr">shift</span>: <span class="hljs-number">0</span>,
          <span class="hljs-attr">content</span>: <span class="hljs-string">"add.html"</span>,
          <span class="hljs-attr">end</span>: <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params"></span>) </span>&#123;
            tableIns.reload();
          &#125;,
        &#125;);
      &#125;
    &#125;);
  &#125;);
</span><span class="hljs-tag"></<span class="hljs-name">script</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>几乎每个列表页都要按照以下样板代码进行编写，新增一个列表页时必然是复制以下代码进行修改，导致整个系统到处充斥着重复代码。使用 Web Components 可以解决这些问题，下面我们看看使用 lit 如何将这些样板代码进行封装。</p>
<p>下面的代码定义了一个 <strong>search-table</strong> 组件，这个组件比原有的表格在功能上更加丰富，能够根据设置自动渲染搜索的表单和工具栏。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">import</span> &#123; html, LitElement &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">"./lit-element/lit-element.js"</span>;
<span class="hljs-keyword">import</span> <span class="hljs-string">"./search-form.js"</span>;

<span class="hljs-keyword">export</span> <span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">SearchTable</span> <span class="hljs-keyword">extends</span> <span class="hljs-title">LitElement</span> </span>&#123;
  <span class="hljs-keyword">static</span> <span class="hljs-keyword">get</span> <span class="hljs-title">properties</span>() &#123;
    <span class="hljs-keyword">return</span> &#123;
      <span class="hljs-attr">renderSetting</span>: &#123; <span class="hljs-attr">type</span>: <span class="hljs-built_in">Object</span> &#125;,
      <span class="hljs-attr">toolbars</span>: &#123; <span class="hljs-attr">type</span>: <span class="hljs-built_in">Array</span> &#125;,
    &#125;;
  &#125;

  <span class="hljs-function"><span class="hljs-title">constructor</span>(<span class="hljs-params"></span>)</span> &#123;
    <span class="hljs-built_in">super</span>();
  &#125;

  <span class="hljs-function"><span class="hljs-title">createRenderRoot</span>(<span class="hljs-params"></span>)</span> &#123;
    <span class="hljs-keyword">return</span> <span class="hljs-built_in">this</span>;
  &#125;

  <span class="hljs-function"><span class="hljs-title">render</span>(<span class="hljs-params"></span>)</span> &#123;
    <span class="hljs-keyword">return</span> html`<span class="xml">
      <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"layui-fluid"</span>></span>
        </span><span class="hljs-subst">$&#123;<span class="hljs-built_in">this</span>.renderSearchForm()&#125;</span><span class="xml">

        <span class="hljs-comment"><!--定义表格--></span>
        <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"layui-row"</span>></span>
          <span class="hljs-tag"><<span class="hljs-name">table</span> <span class="hljs-attr">id</span>=<span class="hljs-string">"Table"</span> <span class="hljs-attr">lay-filter</span>=<span class="hljs-string">"Lay"</span>></span><span class="hljs-tag"></<span class="hljs-name">table</span>></span>
        <span class="hljs-tag"></<span class="hljs-name">div</span>></span>

        </span><span class="hljs-subst">$&#123;<span class="hljs-built_in">this</span>.renderTableToolbar()&#125;</span><span class="xml"> </span><span class="hljs-subst">$&#123;<span class="hljs-built_in">this</span>.renderFieldToolbar()&#125;</span><span class="xml">
      <span class="hljs-tag"></<span class="hljs-name">div</span>></span>
    `</span>;
  &#125;

  <span class="hljs-function"><span class="hljs-title">renderSearchForm</span>(<span class="hljs-params"></span>)</span> &#123;
    <span class="hljs-keyword">const</span> searchSettings = <span class="hljs-built_in">this</span>.searchSettings();
    <span class="hljs-keyword">if</span> (searchSettings.length > <span class="hljs-number">0</span>) &#123;
      <span class="hljs-keyword">return</span> html`<span class="xml">
        <span class="hljs-tag"><<span class="hljs-name">search-form</span>
          <span class="hljs-attr">searchSettings</span>=</span></span><span class="hljs-subst">$&#123;<span class="hljs-built_in">JSON</span>.stringify(searchSettings)&#125;</span><span class="xml"><span class="hljs-tag">
        ></span><span class="hljs-tag"></<span class="hljs-name">search-form</span>></span>
      `</span>;
    &#125;
  &#125;

  <span class="hljs-function"><span class="hljs-title">searchSettings</span>(<span class="hljs-params"></span>)</span> &#123;
    <span class="hljs-keyword">const</span> searchSettings = [];
    <span class="hljs-built_in">this</span>.renderSetting.cols[<span class="hljs-number">0</span>].forEach(<span class="hljs-function">(<span class="hljs-params">col</span>) =></span> &#123;
      <span class="hljs-keyword">if</span> (col.search) &#123;
        <span class="hljs-keyword">const</span> searchSetting = &#123;
          <span class="hljs-attr">field</span>: col.field,
          <span class="hljs-attr">label</span>: col.label || col.title,
          <span class="hljs-attr">valueType</span>: col.valueType,
          <span class="hljs-attr">valueEnum</span>: col.valueEnum,
          <span class="hljs-attr">tooltip</span>: col.tooltip,
        &#125;;
        searchSettings.push(searchSetting);
      &#125;
    &#125;);
    <span class="hljs-keyword">return</span> searchSettings;
  &#125;

  <span class="hljs-function"><span class="hljs-title">renderTableToolbar</span>(<span class="hljs-params"></span>)</span> &#123;
    <span class="hljs-keyword">if</span> (!!<span class="hljs-built_in">this</span>.toolbars && <span class="hljs-built_in">this</span>.toolbars.length > <span class="hljs-number">0</span>) &#123;
      <span class="hljs-keyword">return</span> <span class="hljs-built_in">this</span>.renderToolbar(<span class="hljs-string">"toolbar"</span>, <span class="hljs-built_in">this</span>.toolbars);
    &#125;
  &#125;

  <span class="hljs-function"><span class="hljs-title">renderToolbar</span>(<span class="hljs-params">id, toolbars</span>)</span> &#123;
    <span class="hljs-keyword">if</span> (!!toolbars && toolbars.length > <span class="hljs-number">0</span>) &#123;
      <span class="hljs-keyword">return</span> html`<span class="xml">
        <span class="hljs-tag"><<span class="hljs-name">script</span> <span class="hljs-attr">type</span>=<span class="hljs-string">"text/html"</span> <span class="hljs-attr">id</span>=<span class="hljs-string">"</span></span></span><span class="hljs-subst">$&#123;id&#125;</span><span class="xml"><span class="hljs-tag"><span class="hljs-string">"</span>></span><span class="javascript">
          <div <span class="hljs-class"><span class="hljs-keyword">class</span></span>=<span class="hljs-string">"layui-btn-container"</span>>
            </span></span><span class="hljs-subst">$&#123;toolbars.map(
              (bar) => html`<span class="xml"><span class="javascript">
                <button <span class="hljs-class"><span class="hljs-keyword">class</span></span>=<span class="hljs-string">"layui-btn layui-btn-sm"</span> lay-event=<span class="hljs-string">"</span></span></span><span class="hljs-subst">$&#123;bar.event&#125;</span><span class="xml">">
                  </span><span class="hljs-subst">$&#123;bar.text&#125;</span><span class="xml"><span class="handlebars"><span class="xml">
                <span class="hljs-tag"></<span class="hljs-name">button</span>></span>
              `</span></span></span>
            )&#125;</span><span class="xml"><span class="handlebars"><span class="xml">
          <span class="hljs-tag"></<span class="hljs-name">div</span>></span>
        </span></span><span class="hljs-tag"></<span class="hljs-name">script</span>></span>
      `</span>;
    &#125;
  &#125;

  <span class="hljs-function"><span class="hljs-title">renderFieldToolbar</span>(<span class="hljs-params"></span>)</span> &#123;
    <span class="hljs-keyword">const</span> fieldBars = [];
    <span class="hljs-built_in">this</span>.renderSetting.cols[<span class="hljs-number">0</span>].forEach(<span class="hljs-function">(<span class="hljs-params">col</span>) =></span> &#123;
      <span class="hljs-keyword">if</span> (col.toolbar && col.toolbars) &#123;
        <span class="hljs-keyword">const</span> bar = &#123;
          <span class="hljs-attr">toolbars</span>: col.toolbars,
          <span class="hljs-attr">id</span>: col.toolbar.replace(<span class="hljs-string">"#"</span>, <span class="hljs-string">""</span>),
        &#125;;
        fieldBars.push(bar);
      &#125;
    &#125;);

    <span class="hljs-keyword">return</span> html`<span class="xml">
      </span><span class="hljs-subst">$&#123;fieldBars.map(
        (bar) => html`<span class="xml"> </span><span class="hljs-subst">$&#123;<span class="hljs-built_in">this</span>.renderToolbar(bar.id, bar.toolbars)&#125;</span><span class="xml"> `</span>
      )&#125;</span><span class="xml">
    `</span>;
  &#125;
&#125;

customElements.define(<span class="hljs-string">"search-table"</span>, SearchTable);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>由于 search-table 的属性是对象，而 html 标记上的属性只能设置字符串，因此在赋值时需要将 json 序列化后写在属性上，写法上并不方便，我们可再增加一个工具方法来优化组件的编写方式。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">renderComponent</span>(<span class="hljs-params">tagName, attrs</span>) </span>&#123;
  <span class="hljs-keyword">const</span> element = <span class="hljs-built_in">document</span>.createElement(tagName);
  <span class="hljs-keyword">if</span> (!!attrs) &#123;
    <span class="hljs-keyword">for</span> (<span class="hljs-keyword">const</span> key <span class="hljs-keyword">in</span> attrs) &#123;
      <span class="hljs-keyword">const</span> value = attrs[key];
      element.setAttribute(key, <span class="hljs-built_in">JSON</span>.stringify(value));
    &#125;
  &#125;
  <span class="hljs-built_in">document</span>.write(element.outerHTML);
&#125;

<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">renderTable</span>(<span class="hljs-params">attrs, callback</span>) </span>&#123;
  renderComponent(<span class="hljs-string">"search-table"</span>, attrs);
  applyTableSetting(attrs, callback);
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>renderTable</strong> 方法中包含 <strong>search-table</strong> 组件的输出，并应用表格相关的设置。封装完成后我们看看最终的写法。</p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">script</span>></span><span class="javascript">
  renderTable(
    &#123;
      <span class="hljs-attr">toolbars</span>: [
        &#123;
          <span class="hljs-attr">text</span>: <span class="hljs-string">"添加"</span>,
          <span class="hljs-attr">event</span>: <span class="hljs-string">"addBtn"</span>,
          <span class="hljs-attr">onEvent</span>: <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params">data, tableIns</span>) </span>&#123;
            <span class="hljs-keyword">return</span> &#123;
              <span class="hljs-attr">title</span>: <span class="hljs-string">"添加"</span>,
              <span class="hljs-attr">area</span>: [<span class="hljs-string">"450px"</span>, <span class="hljs-string">"550px"</span>],
              <span class="hljs-attr">content</span>: <span class="hljs-string">"add.html"</span>,
            &#125;;
          &#125;,
        &#125;
      ],
      <span class="hljs-attr">renderSetting</span>: &#123;
        <span class="hljs-attr">url</span>: <span class="hljs-string">"/getList"</span>,
        <span class="hljs-attr">cols</span>: [
          [
            &#123; <span class="hljs-attr">field</span>: <span class="hljs-string">"name"</span>, <span class="hljs-attr">title</span>: <span class="hljs-string">"名称"</span>, <span class="hljs-attr">search</span>:<span class="hljs-literal">true</span>, <span class="hljs-attr">align</span>: <span class="hljs-string">"center"</span> &#125;,
            &#123; <span class="hljs-attr">field</span>: <span class="hljs-string">"code"</span>, <span class="hljs-attr">title</span>: <span class="hljs-string">"编码"</span>, <span class="hljs-attr">align</span>: <span class="hljs-string">"center"</span> &#125;,
            &#125;,
            &#123;
              <span class="hljs-attr">field</span>: <span class="hljs-string">""</span>,
              <span class="hljs-attr">title</span>: <span class="hljs-string">"操作"</span>,
              <span class="hljs-attr">align</span>: <span class="hljs-string">"center"</span>,
              <span class="hljs-attr">toolbar</span>: <span class="hljs-string">"#bar"</span>,
              <span class="hljs-attr">fixed</span>: <span class="hljs-string">"right"</span>,
              <span class="hljs-attr">width</span>: <span class="hljs-string">"10%"</span>,
              <span class="hljs-attr">toolbars</span>: [
                &#123;
                  <span class="hljs-attr">text</span>: <span class="hljs-string">"修改"</span>,
                  <span class="hljs-attr">event</span>: <span class="hljs-string">"edit"</span>,
                  <span class="hljs-attr">onEvent</span>: <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params">data</span>) </span>&#123;
                    <span class="hljs-keyword">return</span> &#123;
                      <span class="hljs-attr">title</span>: <span class="hljs-string">"编辑"</span>,
                      <span class="hljs-attr">area</span>: [<span class="hljs-string">"450px"</span>, <span class="hljs-string">"550px"</span>],
                      <span class="hljs-attr">content</span>:
                        <span class="hljs-string">"edit.html?id="</span> + data.id,
                    &#125;;
                  &#125;,
                &#125;,
              ],
            &#125;,
          ],
        ],
      &#125;,
    &#125;);
</span><span class="hljs-tag"></<span class="hljs-name">script</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>只需要这么一点代码就完成了最初 Layui 版本所实现的一样的功能，在封装时沿用并扩展了 Layui 表格的属性，使得兼容原有 Layui 的 api，注意在名称一列新增了 search 扩展属性，设置为 true 即将该字段自动加入到搜索表单中。</p>
<p>文章中仅包含部分代码，上文中涉及的 Web Components 的全部代码请查看 <a href="https://github.com/lcomplete/TechShare/tree/master/docs/js/web_components" target="_blank" rel="nofollow noopener noreferrer">github.com/lcomplete/T…</a> 。注意这里面许多代码是根据项目实际情况进行封装的，为进行简化，全部组件的封装代码也并未给出，希望读者朋友能够领会组件化开发和 DRY 的编程思想。</p></div>  
</div>
            