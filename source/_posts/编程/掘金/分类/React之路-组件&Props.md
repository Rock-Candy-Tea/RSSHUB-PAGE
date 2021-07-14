
---
title: 'React之路-组件&Props'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=4282'
author: 掘金
comments: false
date: Tue, 13 Jul 2021 18:10:26 GMT
thumbnail: 'https://picsum.photos/400/300?random=4282'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h3 data-id="heading-0">组件</h3>
<p>组件，从概念上类似于 JavaScript 函数。它接受任意的入参（即 “props”），并返回用于描述页面展示内容的 React 元素。</p>
<h3 data-id="heading-1">函数组件和class组件</h3>
<p>函数组件(js函数)</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// 函数组件就是js函数,携带参数props,返回react对象</span>
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">Welcome</span>(<span class="hljs-params">props</span>) </span>&#123;
  <span class="hljs-keyword">return</span> <span class="xml"><span class="hljs-tag"><<span class="hljs-name">h1</span>></span>Hello, &#123;props.name&#125;<span class="hljs-tag"></<span class="hljs-name">h1</span>></span></span>;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>ES6 class组件</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Welcome</span> <span class="hljs-keyword">extends</span> <span class="hljs-title">React</span>.<span class="hljs-title">Component</span> </span>&#123;
  <span class="hljs-function"><span class="hljs-title">render</span>(<span class="hljs-params"></span>)</span> &#123;
    <span class="hljs-keyword">return</span> <span class="xml"><span class="hljs-tag"><<span class="hljs-name">h1</span>></span>Hello, &#123;this.props.name&#125;<span class="hljs-tag"></<span class="hljs-name">h1</span>></span></span>;
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-2">渲染组件</h3>
<p>React 元素也可以是用户自定义的组件</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> element = <span class="xml"><span class="hljs-tag"><<span class="hljs-name">Welcome</span> <span class="hljs-attr">name</span>=<span class="hljs-string">"Sara"</span> /></span></span>;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>当 React 元素为用户自定义组件时，它会将 JSX 所接收的属性（attributes）以及子组件（children）转换为单个对象传递给组件，这个对象被称之为 “props”</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">//声明函数组件,接收参数props并且返回react对象</span>
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">Topnav</span>(<span class="hljs-params">props</span>)</span>&#123;
  <span class="hljs-keyword">return</span> <span class="xml"><span class="hljs-tag"><<span class="hljs-name">h1</span>></span>this is &#123;props.name&#125;<span class="hljs-tag"></<span class="hljs-name">h1</span>></span></span>
&#125;

<span class="hljs-keyword">const</span> element= <span class="xml"><span class="hljs-tag"><<span class="hljs-name">Topnav</span> <span class="hljs-attr">name</span>=<span class="hljs-string">'导航'</span> /></span></span>

ReactDOM.render(
  element,
  <span class="hljs-built_in">document</span>.getElementById(<span class="hljs-string">'root'</span>)
)
<span class="hljs-comment">// 将<Topnav name='导航' />作为参数传给ReactDOM.render()</span>
<span class="hljs-comment">// React调用Topnav组件,将name=导航作为props传入</span>
<span class="hljs-comment">// topnav组件将<h1>this is 导航作为返回值返回</h1>;</span>
<span class="hljs-comment">// 页面DOM更新成this is 导航</span>

<span class="hljs-comment">//组件名开头必须是大写字母</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-3">组件组合</h3>
<p>创建一个渲染多个组件的List组件</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">Name</span>(<span class="hljs-params">props</span>) </span>&#123;
  <span class="hljs-keyword">return</span> <span class="xml"><span class="hljs-tag"><<span class="hljs-name">h1</span>></span>姓名: &#123;props.name&#125;<span class="hljs-tag"></<span class="hljs-name">h1</span>></span></span>;
&#125;
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">Age</span>(<span class="hljs-params">props</span>) </span>&#123;
  <span class="hljs-keyword">return</span> <span class="xml"><span class="hljs-tag"><<span class="hljs-name">h1</span>></span>年龄: &#123;props.age&#125;<span class="hljs-tag"></<span class="hljs-name">h1</span>></span></span>;
&#125;
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">Sex</span>(<span class="hljs-params">props</span>) </span>&#123;
  <span class="hljs-keyword">return</span> <span class="xml"><span class="hljs-tag"><<span class="hljs-name">h1</span>></span>性别: &#123;props.sex&#125;<span class="hljs-tag"></<span class="hljs-name">h1</span>></span></span>;
&#125;
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">List</span>(<span class="hljs-params"></span>) </span>&#123;
  <span class="hljs-keyword">return</span> (
    <span class="xml"><span class="hljs-tag"><<span class="hljs-name">div</span>></span>
      <span class="hljs-tag"><<span class="hljs-name">Name</span> <span class="hljs-attr">name</span>=<span class="hljs-string">"张三"</span> /></span>
      <span class="hljs-tag"><<span class="hljs-name">Age</span> <span class="hljs-attr">age</span>=<span class="hljs-string">"20"</span> /></span>
      <span class="hljs-tag"><<span class="hljs-name">Sex</span> <span class="hljs-attr">sex</span>=<span class="hljs-string">"男"</span> /></span>
    <span class="hljs-tag"></<span class="hljs-name">div</span>></span></span>
  );
&#125;
ReactDOM.render(
  <span class="xml"><span class="hljs-tag"><<span class="hljs-name">List</span> /></span></span>,
  <span class="hljs-built_in">document</span>.getElementById(<span class="hljs-string">'root'</span>)
);
<span class="copy-code-btn">复制代码</span></code></pre></div>  
</div>
            