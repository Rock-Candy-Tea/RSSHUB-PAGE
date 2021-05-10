
---
title: 'React快速暴力入门'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/b654a24918094ebc806d4a67116acafb~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Sun, 09 May 2021 04:27:27 GMT
thumbnail: 'https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/b654a24918094ebc806d4a67116acafb~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h1 data-id="heading-0">React快速暴力入门</h1>
<p>React 作为如今三大框架之一，在进行了短期的学习后，整理了一些笔记，做一下分享： （新人一个，多多包涵）</p>
<h2 data-id="heading-1">一、React简介</h2>
<h3 data-id="heading-2">1. 什么是React：</h3>
<blockquote>
<p><strong>React</strong> 是一款由 <strong>Facebook</strong>开发的用于构造用户界面的<strong>Javascript</strong>库。<br>
<strong>React</strong> 与<strong>Vue</strong>相比拥有较高的性能，但使用难度比<strong>Vue</strong>高些。<br>
<strong>React</strong> 将页面以一个个组件的方式进行拆分与组装，重复使用提高效率（可见下图）
<strong>React</strong> 对数据的处理与管理比原生更加的清晰。</p>
</blockquote>
<h3 data-id="heading-3">2. React的特点</h3>
<ol>
<li><strong>声明式设计</strong> −React的每个组件都是通过声明创建，使得页面逻辑更加清晰</li>
</ol>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/b654a24918094ebc806d4a67116acafb~tplv-k3u1fbpfcp-watermark.image" alt="582_1.png" loading="lazy" referrerpolicy="no-referrer">
2. <strong>虚拟DOM</strong> −React每次渲染页面时会创建一个虚拟DOM，与现有的DOM进行对比，有差异的才进行替换重新渲染，提高了效率。
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/fb5f0c50b5ce4716afd51258552548b8~tplv-k3u1fbpfcp-watermark.image" alt="584_1.png" loading="lazy" referrerpolicy="no-referrer">
3. <strong>JSX</strong> − <strong>JSX</strong> 是 <strong>JavaScript</strong> 语法的扩展。<strong>React</strong> 开发不一定使用 <strong>JSX</strong> ，但我们建议使用它。</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">// 在 javascript中创建元素</span>
<span class="hljs-keyword">const</span> DOM = <span class="hljs-built_in">document</span>.createElement(<span class="hljs-string">"h1"</span>); <span class="hljs-comment">// 真实DOM</span>
DOM.innerText = <span class="hljs-string">"这是h1标签"</span>;

<span class="hljs-comment">// 在 jsx中创建元素</span>
<span class="hljs-keyword">const</span> VDOM = <span class="xml"><span class="hljs-tag"><<span class="hljs-name">h1</span>></span>这是h1标签<span class="hljs-tag"></<span class="hljs-name">h1</span>></span></span> <span class="hljs-comment">// 虚拟DOM</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<ol start="4">
<li><strong>组件</strong> − 通过 React 构建组件，使得代码更加容易得到复用，能够很好的应用在大项目的开发中。</li>
</ol>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">// 不必现在就看懂，仅需要知道每个组件都是需要进行声明后才能使用</span>
<span class="hljs-keyword">import</span> React, &#123;PureCompoent&#125; <span class="hljs-keyword">from</span> <span class="hljs-string">"react"</span>;
<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> <span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Header</span> <span class="hljs-keyword">extends</span> <span class="hljs-title">PureCompoent</span></span>&#123;
    <span class="hljs-function"><span class="hljs-title">render</span>(<span class="hljs-params"></span>)</span>&#123;
        <span class="hljs-keyword">return</span> <span class="xml"><span class="hljs-tag"><<span class="hljs-name">header</span>></span>这是头部组件<span class="hljs-tag"></<span class="hljs-name">header</span>></span></span>
    &#125;
&#125;
<span class="hljs-comment">// ------------------------------------------------</span>
<span class="hljs-comment">// 在需要使用 header组件时调用即可重复使用</span>
<span class="hljs-keyword">import</span> Header <span class="hljs-keyword">from</span> <span class="hljs-string">"./Header"</span>;
<span class="xml"><span class="hljs-tag"><<span class="hljs-name">Header</span>></span><span class="hljs-tag"></<span class="hljs-name">Header</span>></span></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<ol start="5">
<li><strong>单向响应的数据流</strong> − React 实现了单向响应的数据流，从而减少了重复代码，这也是它为什么比传统数据绑定更简单。(这个在后面会了解到)</li>
</ol>
<h3 data-id="heading-4">3. 安装与使用</h3>
<ol>
<li>使用<strong>cdn</strong></li>
</ol>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">script</span> <span class="hljs-attr">crossorigin</span> <span class="hljs-attr">src</span>=<span class="hljs-string">"https://unpkg.com/react@16/umd/react.development.js"</span>></span><span class="hljs-tag"></<span class="hljs-name">script</span>></span>
<span class="hljs-tag"><<span class="hljs-name">script</span> <span class="hljs-attr">crossorigin</span> <span class="hljs-attr">src</span>=<span class="hljs-string">"https://unpkg.com/react-dom@16/umd/react-dom.development.js"</span>></span><span class="hljs-tag"></<span class="hljs-name">script</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<ol start="2">
<li>通过下载导入 React包</li>
</ol>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">script</span> <span class="hljs-attr">src</span>=<span class="hljs-string">"../js/react.development.js"</span>></span><span class="hljs-tag"></<span class="hljs-name">script</span>></span>
<span class="hljs-tag"><<span class="hljs-name">script</span> <span class="hljs-attr">src</span>=<span class="hljs-string">"../js/react-dom.development.js"</span>></span><span class="hljs-tag"></<span class="hljs-name">script</span>></span>
<span class="hljs-tag"><<span class="hljs-name">script</span> <span class="hljs-attr">src</span>=<span class="hljs-string">"../js/babel.min.js"</span>></span><span class="hljs-tag"></<span class="hljs-name">script</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<ol start="3">
<li>使用 react的脚手架<code>create-react-app</code> 创建项目文件会自带react</li>
</ol>
<pre><code class="copyable">npm i create-react-app -g
create-react-app 项目名称
<span class="copy-code-btn">复制代码</span></code></pre>
<blockquote>
<p>注意：使用 <code>react</code>必须使用 <strong>babel.js</strong> 将 <code>jsx</code>语法转为 <code> js</code>语法
<code>ReactDOM</code> 独立于 <code>React</code>（为了防止<code>React</code>太大太臃肿而拆开）</p>
</blockquote>
<h3 data-id="heading-5">4. 虚拟DOM</h3>
<h4 data-id="heading-6">(1) 关于虚拟DOM</h4>
<p><strong>虚拟DOM的本质就是一个对象</strong>，真实DOM也是个对象，但虚拟DOM的<strong>属性更少，更加轻量</strong>。</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">// 虚拟DOM  </span>
<span class="hljs-keyword">const</span> VDOM = <span class="xml"><span class="hljs-tag"><<span class="hljs-name">h1</span>></span>Hello World<span class="hljs-tag"></<span class="hljs-name">h1</span>></span></span>; <span class="hljs-comment">// 此处不需要引号，因为不是字符串</span>
<span class="hljs-comment">// 真实DOM</span>
<span class="hljs-keyword">const</span> TDOM = <span class="hljs-built_in">document</span>.querySelector(<span class="hljs-string">"#app"</span>);

<span class="hljs-built_in">console</span>.log(<span class="hljs-string">"虚拟DOM: "</span>, VDOM);   <span class="hljs-comment">// Object</span>
<span class="hljs-built_in">console</span>.log(<span class="hljs-string">"真实DOM: "</span>, TDOM);   <span class="hljs-comment">// <div id="app"></div></span>
<span class="hljs-built_in">console</span>.log(<span class="hljs-string">"虚拟DOM类型: "</span>, <span class="hljs-keyword">typeof</span> VDOM);  <span class="hljs-comment">// object</span>
<span class="hljs-built_in">console</span>.log(<span class="hljs-string">"真实DOM类型: "</span>, <span class="hljs-keyword">typeof</span> TDOM);  <span class="hljs-comment">// object</span>
<span class="hljs-built_in">console</span>.log(VDOM <span class="hljs-keyword">instanceof</span> <span class="hljs-built_in">Object</span>);    <span class="hljs-comment">// true</span>
<span class="hljs-built_in">console</span>.log(TDOM <span class="hljs-keyword">instanceof</span> <span class="hljs-built_in">Object</span>);    <span class="hljs-comment">// true</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<blockquote>
<p>虚拟DOM 最终会被 React转为 真实DOM呈现在页面上</p>
</blockquote>
<h4 data-id="heading-7">(2) 创建虚拟DOM</h4>
<ol>
<li>通过 <code>React</code>的方法 <code>createElement()</code>方法创建虚拟DOM</li>
</ol>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">// React.createElement(标签名称, 标签属性, 标签内容)</span>
<span class="hljs-keyword">const</span> VDOM1 = React.createElement(<span class="hljs-string">"h1"</span>, &#123;<span class="hljs-attr">id</span>: <span class="hljs-string">"title"</span>&#125;, <span class="hljs-string">"This is Title"</span>);
<span class="copy-code-btn">复制代码</span></code></pre>
<ol start="2">
<li>使用方法一的<strong>语法糖</strong>创建虚拟DOM</li>
</ol>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">const</span> VDOM2 = <span class="xml"><span class="hljs-tag"><<span class="hljs-name">h1</span> <span class="hljs-attr">id</span>=<span class="hljs-string">"title"</span>></span>This is Title<span class="hljs-tag"></<span class="hljs-name">h1</span>></span></span>;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-8">5. 关于<code>JSX</code></h3>
<p><code>jsx</code>语法与<code>javascript</code>语法非常相似，只有一些需要注意的地方</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">// 虚拟DOM  </span>
<span class="hljs-keyword">const</span> VDOM = (  <span class="hljs-comment">// 使用括号框住 jsx标签表示层级会更加美观些。</span>
    <span class="xml"><span class="hljs-tag"><<span class="hljs-name">h1</span>></span>
        <span class="hljs-tag"><<span class="hljs-name">span</span>></span>Hello World<span class="hljs-tag"></<span class="hljs-name">span</span>></span>
    <span class="hljs-tag"></<span class="hljs-name">h1</span>></span></span>
)
<span class="hljs-keyword">const</span> myid = <span class="hljs-string">"HeLlO"</span>;
<span class="hljs-keyword">const</span> content = <span class="hljs-string">"Happy New Year"</span>
<span class="hljs-keyword">const</span> students = [
&#123;<span class="hljs-attr">id</span>: <span class="hljs-string">"001"</span>, <span class="hljs-attr">name</span>: <span class="hljs-string">"Tom"</span>, <span class="hljs-attr">age</span>: <span class="hljs-number">18</span>&#125;,
&#123;<span class="hljs-attr">id</span>: <span class="hljs-string">"002"</span>, <span class="hljs-attr">name</span>: <span class="hljs-string">"Tim"</span>, <span class="hljs-attr">age</span>: <span class="hljs-number">19</span>&#125;,
&#123;<span class="hljs-attr">id</span>: <span class="hljs-string">"003"</span>, <span class="hljs-attr">name</span>: <span class="hljs-string">"Jerry"</span>, <span class="hljs-attr">age</span>: <span class="hljs-number">20</span>&#125;,
];
<span class="hljs-keyword">const</span> VDOM2 = (
    <span class="xml"><span class="hljs-tag"><<span class="hljs-name">div</span>></span>
        <span class="hljs-tag"><<span class="hljs-name">h2</span> <span class="hljs-attr">className</span>=<span class="hljs-string">"title"</span> <span class="hljs-attr">id</span>=<span class="hljs-string">&#123;myid.toLowerCase()&#125;</span>></span>
            <span class="hljs-tag"><<span class="hljs-name">span</span> <span class="hljs-attr">style</span>=<span class="hljs-string">&#123;&#123;color:</span> '<span class="hljs-attr">pink</span>'&#125;&#125;></span>&#123;content&#125;<span class="hljs-tag"></<span class="hljs-name">span</span>></span>
        <span class="hljs-tag"></<span class="hljs-name">h2</span>></span>
        <span class="hljs-tag"><<span class="hljs-name">ul</span>></span>&#123;/* 使用 ES6的 map() 函数进行列表渲染（将数据批量渲染到页面上） */&#125;
        &#123;
            students.map(student=>&#123;
                return <span class="hljs-tag"><<span class="hljs-name">li</span> <span class="hljs-attr">key</span>=<span class="hljs-string">&#123;student.id&#125;</span>></span>&#123;student.name&#125;---&#123;student.age&#125;<span class="hljs-tag"></<span class="hljs-name">li</span>></span>
            &#125;
        &#125;
        <span class="hljs-tag"></<span class="hljs-name">ul</span>></span>
        <span class="hljs-tag"><<span class="hljs-name">input</span> <span class="hljs-attr">type</span>=<span class="hljs-string">"text"</span>/></span>    
    <span class="hljs-tag"></<span class="hljs-name">div</span>></span></span>
)
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-9">jsx语法规则：</h4>
<ol>
<li>定义虚拟DOM时不要写引号</li>
<li>标签中混入 js表达式时要用 <strong>&#123;&#125;</strong>
<ul>
<li>表达式会产生一个值，可以放在任何需要值的地方</li>
<li>语句时一串代码，用于处理逻辑用的</li>
</ul>
</li>
<li>标签中类名指定不用 class，要用 className</li>
<li>标签中使用内联样式时，要用双括号写法（使用小驼峰写法写css样式）</li>
<li>添加事件属性时（如<code>onclick</code>)，<strong>on</strong>后面的单词首字母要大写（如<code>onClick</code>）</li>
<li>虚拟DOM必须只有一个根标签</li>
<li>标签必须闭合</li>
<li>标签开头
<ul>
<li>标签开头为小写时，会被 jsx编译为 html标签，若 html没有对应同名元素则报错</li>
<li>标签开头为大写时，会被 jsx识别为组件，若没找到对应组件则</li>
</ul>
</li>
</ol>
<h3 data-id="heading-10">6. 渲染到页面上</h3>
<p>使用 <code>ReactDOM</code>的 <code>render()</code>方法进行渲染</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">const</span> VDOM = <span class="xml"><span class="hljs-tag"><<span class="hljs-name">h1</span> <span class="hljs-attr">id</span>=<span class="hljs-string">"title"</span>></span>This is a Title<span class="hljs-tag"></<span class="hljs-name">h1</span>></span></span>;    <span class="hljs-comment">// 创建虚拟DOM</span>
<span class="hljs-comment">// ReactDOM.render( 组件(虚拟DOM),  要绑定到哪个元素上 );</span>
ReactDOM.render(VDOM, <span class="hljs-built_in">document</span>.querySelector(<span class="hljs-string">"#root"</span>));
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-11">二、组件的使用</h2>
<p>在 <strong>React</strong>中，有两种组件的创建方式，分别为<strong>函数式组件</strong>和<strong>类式组件</strong>。其中 <strong>类式组件</strong>使用频率较高（React 16.8出现 <code>Hook</code>后函数式组件也多了起来）</p>
<h3 data-id="heading-12">函数式组件</h3>
<p>顾名思义，该组件是由函数来写的</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">Demo</span>(<span class="hljs-params">props</span>)</span>&#123;    <span class="hljs-comment">// 定义一个组件，名为 Demo</span>
    <span class="hljs-keyword">return</span> <span class="xml"><span class="hljs-tag"><<span class="hljs-name">h2</span>></span>This is a component<span class="hljs-tag"></<span class="hljs-name">h2</span>></span></span>;    <span class="hljs-comment">// 返回值为组件的DOM内容</span>
&#125;
ReactDOM.render(<span class="xml"><span class="hljs-tag"><<span class="hljs-name">Demo</span>/></span></span>, <span class="hljs-built_in">document</span>.querySelector(<span class="hljs-string">"#root"</span>))
<span class="copy-code-btn">复制代码</span></code></pre>
<p>函数式组件定义：</p>
<ul>
<li>函数名称必须大写</li>
<li>调用时以标签方式调用且开头大写</li>
<li>函数式组件的参数为 <code>props</code>（后面会讲）</li>
</ul>
<h3 data-id="heading-13">类式组件</h3>
<p>该组件通过类来构建，但需要继承<strong>React</strong>自带的一个类<code>Component</code>。</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">// 使用 ES6写法创建类式组件，并继承于 React.Component</span>
<span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Demo</span> <span class="hljs-keyword">extends</span> <span class="hljs-title">React</span>.<span class="hljs-title">Component</span></span>&#123;
    
    <span class="hljs-comment">// 添加render() 函数（必须），返回值为组件的虚拟DOM</span>
    <span class="hljs-function"><span class="hljs-title">render</span>(<span class="hljs-params"></span>)</span>&#123;
        <span class="hljs-built_in">console</span>.log(<span class="hljs-built_in">this</span>);      <span class="hljs-comment">// render() 函数的 this 指向组件的实例对象</span>
        <span class="hljs-keyword">return</span> <span class="xml"><span class="hljs-tag"><<span class="hljs-name">h1</span>></span>This is a Title!<span class="hljs-tag"></<span class="hljs-name">h1</span>></span></span>
    &#125;
&#125;
ReactDOM.render(<span class="xml"><span class="hljs-tag"><<span class="hljs-name">Demo</span>/></span></span>, <span class="hljs-built_in">document</span>.querySelector(<span class="hljs-string">"#root"</span>));
<span class="copy-code-btn">复制代码</span></code></pre>
<p>类式组件的定义：</p>
<ul>
<li>必须继承 <strong>React</strong>的内置类<code>Component</code></li>
<li>必须包含方法 <code>render()</code></li>
<li>构造函数 <code>constructor()</code>的参数为 <code>props</code>（后面会讲），如果需要使用<code>constructor</code>则必须调用父类的构造函数 <code>super(props)</code></li>
</ul>
<p>类式组件挂载时的执行情况：</p>
<ol>
<li><strong>React</strong>解析组件标签，发现了 <code>Demo</code>组件</li>
<li>发现为类式组件，随后 <code>new</code>出该类的实例对象，通过实例调用原型对象上的<code>render</code>方法</li>
<li>将 <code>render</code>方法返回的<strong>虚拟DOM</strong>转为<strong>真实DOM</strong>，随后呈现到页面中</li>
</ol>
<hr>
<p>组件定义的注意事项：</p>
<ol>
<li>类式组件的<code>render()</code> 返回的组件标签与函数式组件返回的组件标签一定要有一个<strong>根标签</strong></li>
<li>都必须以<strong>大写字母开头</strong></li>
</ol>
<h3 data-id="heading-14">组件的挂载与卸载</h3>
<p>挂载已经看了很多个了，直接上代码：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">// ReactDOM.render( 组件, 要绑定在哪个元素上 );</span>
ReactDOM.render( <span class="xml"><span class="hljs-tag"><<span class="hljs-name">Demo</span>/></span></span>, <span class="hljs-built_in">document</span>.querySelector(<span class="hljs-string">"#app"</span>) );
<span class="copy-code-btn">复制代码</span></code></pre>
<p>卸载的代码长点，我也直接放上来了：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">// ReactDOM.unmountComponentAtNode( 要卸载哪个元素上的组件 );</span>
ReactDOM.unmountComponentAtNode( <span class="hljs-built_in">document</span>.querySelector(<span class="hljs-string">"#app"</span>) );
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-15">其他小知识</h3>
<ol>
<li>包含表单元素的组件分为<strong>非受控租价</strong>与<strong>受控组件</strong>
<ul>
<li><strong>受控组件</strong>：表单组件的输入组件随着输入并将内容存储到状态中（随时更新）</li>
<li><strong>非受控组件</strong>：表单组件的输入组件的内容在有需求的时候才存储到状态中（即用即取）</li>
</ul>
</li>
</ol>
<h2 data-id="heading-16">三、组件的三大属性</h2>
<p>组件的实质就是个对象，而对象自然有属性，在组件里最常用的三个属性分别是 <code>state</code>、<code>props</code>和 <code>refs</code></p>
<h3 data-id="heading-17">1. state</h3>
<p><code>state</code>即组件的<strong>状态</strong>，说的明白点就是该组件所存储的（所需要使用的）数据</p>
<h4 data-id="heading-18">类式组件中的使用：</h4>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Weather</span> <span class="hljs-keyword">extends</span> <span class="hljs-title">React</span>.<span class="hljs-title">Component</span></span>&#123;
    <span class="hljs-function"><span class="hljs-title">constructor</span>(<span class="hljs-params">props</span>)</span>&#123;
        <span class="hljs-built_in">super</span>(props);
        <span class="hljs-comment">// this.state = &#123;weather: "Spring"&#125;     // 也可以在构造函数中定义 state</span>
    &#125;
    
    state = &#123;   <span class="hljs-comment">// 定义 state</span>
        <span class="hljs-attr">weather</span>: <span class="hljs-string">"summer"</span>,
    &#125;
    
    <span class="hljs-function"><span class="hljs-title">render</span>(<span class="hljs-params"></span>)</span>&#123;
        <span class="hljs-comment">// 当前季节为：summer</span>
        <span class="hljs-keyword">return</span> <span class="xml"><span class="hljs-tag"><<span class="hljs-name">h2</span>></span>当前季节为：&#123; this.state.weather &#125;<span class="hljs-tag"></<span class="hljs-name">h2</span>></span></span>
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>使用的时候通过 <code>this.state</code>调用 <code>state</code>里的值
类式组件定义 <code>state</code>:</p>
<ul>
<li>可以在构造函数中初始化 <code>state</code></li>
<li>可以在类中添加属性 <code>state</code>来初始化</li>
</ul>
<h4 data-id="heading-19">函数式组件中的使用</h4>
<ul>
<li>在 <strong>React16.8</strong> 前，函数式组件并不能有自己的 <code>state</code>（因为会重复初始化数据）</li>
<li>到 <strong>React16.8</strong> 后，出现了 <code>Hook</code>方法，使得函数式组件也可以使用 <code>state</code>特性，先了解即可，后面会教学。</li>
</ul>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">Demo</span>(<span class="hljs-params"></span>)</span>&#123;
    <span class="hljs-keyword">const</span> [weather, setWeather] = React.useState(<span class="hljs-string">"Winter"</span>);
    <span class="hljs-keyword">return</span> <span class="xml"><span class="hljs-tag"><<span class="hljs-name">h2</span>></span>当前季节为：&#123;weather&#125;<span class="hljs-tag"></<span class="hljs-name">h2</span>></span></span>     <span class="hljs-comment">// 当前季节为：Winter</span>
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-20">修改 state</h4>
<p>在<strong>类式组件</strong>的函数中，你会发现直接修改 <code>state</code>的值，如：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-built_in">this</span>.state.count = <span class="hljs-number">1</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>如果你在页面中使用了 <code>count</code>这个值，你会发现，这页面咋没变呢？<br>
梳理一下页面渲染靠的是哪个函数呢？不是靠的 <code>render()</code>函数吗？<br>
如果你每次直接修改 <code>state</code>后在调用 <code>render()</code>函数的话，不会显得太麻烦了吗？<br>
其实<strong>React</strong>也不建议 <code>state</code>不允许直接修改，而是通过<strong>特定的渠道</strong>来修改，便是使用在<strong>类的原型对象上</strong>的方法 <code>setState()</code></p>
<h5 data-id="heading-21">setState</h5>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-built_in">this</span>.setState(partialState, [callback]);
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li><code>partialState</code>: 需要更新的状态的部分对象</li>
<li><code>callback</code>: 更新完状态后的回调函数</li>
</ul>
<p><code>setState</code> 有两种写法：
写法1：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-built_in">this</span>.setState(&#123;
    <span class="hljs-attr">count</span>: <span class="hljs-number">1</span>,
&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>写法2：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">// 传入一个函数，返回x需要修改成的对象，参数为当前的 state</span>
<span class="hljs-built_in">this</span>.setState(<span class="hljs-function"><span class="hljs-params">state</span> =></span> (&#123;<span class="hljs-attr">count</span>: state.count+<span class="hljs-number">1</span>&#125;);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>使用那种写法，取决于<strong>修改的状态是否需要动用到当前的状态</strong></p>
<h5 data-id="heading-22">forceUpdate</h5>
<p>还有一种修改状态的方法，就是 <code>forceUpdate</code>，意思是<strong>强制更新</strong>，即强制更新状态。<br>
参数为更新状态完成后的回调函数</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-built_in">this</span>.forceUpdate([callback]);
<span class="copy-code-btn">复制代码</span></code></pre>
<p><em><code>setState</code>更新与<code>forceUpdate</code>更新都是一种合并操作，而不是替换操作</em></p>
<hr>
<ul>
<li>在执行 <code>setState</code>操作后，<strong>React</strong>会自动帮我们调用一次 <code>render()</code></li>
<li><code>render()</code> 的执行次数便是 <strong>1+n</strong> (1 为初始化时的自动调用，n 为状态更新的次数（即调用 <code>setState</code>或<code>forceUpdate</code>的次数）)</li>
<li>尽量少用或不用 <code>forceUpdate</code></li>
</ul>
<h3 data-id="heading-23">2. props</h3>
<p>与 <code>state</code>不同，<code>state</code>是组件自身的状态（数据），而 <code>props</code>则是外部传入给自己的状态（数据）</p>
<p><em><code>props</code>在组件内修改，必须由谁传入的即由谁修改</em></p>
<h4 data-id="heading-24">类式组件中使用</h4>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Person</span> <span class="hljs-keyword">extends</span> <span class="hljs-title">React</span>.<span class="hljs-title">component</span></span>&#123;

    <span class="hljs-function"><span class="hljs-title">constructor</span>(<span class="hljs-params">props</span>)</span>&#123;     <span class="hljs-comment">// 还记得构造函数的参数吗，也能够获取 props</span>
        <span class="hljs-built_in">super</span>(props);
    &#125;

    <span class="hljs-comment">// 可以使用静态属性 propTyps 来限制props</span>
    <span class="hljs-keyword">static</span> propTypes = &#123;
         <span class="hljs-comment">// 在 16版本前，通过使用React自带的PropTypess属性传递值</span>
        <span class="hljs-comment">// name: React.PropTypes.string.isRequired,</span>
        
        <span class="hljs-comment">// 16版本后，PropTypes被单独移出 React作为单独的个体，需要另外导入</span>
        <span class="hljs-attr">name</span>: PropTypes.string.isRequired, <span class="hljs-comment">// 字符串类型，且必须传值</span>
        <span class="hljs-attr">sex</span>: PropTypes.string,  <span class="hljs-comment">// 字符串类型</span>
        <span class="hljs-attr">age</span>: PropTypes.number,  <span class="hljs-comment">// 数字类型</span>
        <span class="hljs-attr">speak</span>: PropTypes.func,  <span class="hljs-comment">// 函数类型</span>
    &#125;
    
    <span class="hljs-comment">// 可以使用静态属性 defaultProps 来设置某些 prop 的默认值</span>
    <span class="hljs-keyword">static</span> defaultProps = &#123;
        <span class="hljs-attr">sex</span>: <span class="hljs-string">"男"</span>,   <span class="hljs-comment">// 设置 sex 的 prop 默认值为 “男”</span>
    &#125;

    <span class="hljs-function"><span class="hljs-title">render</span>(<span class="hljs-params"></span>)</span>&#123;
        <span class="hljs-keyword">const</span> &#123;name, sex, age&#125; = <span class="hljs-built_in">this</span>.props;    <span class="hljs-comment">// 从 props中获取值</span>
        <span class="hljs-keyword">return</span> (
            <span class="xml"><span class="hljs-tag"><<span class="hljs-name">ul</span>></span>
                <span class="hljs-tag"><<span class="hljs-name">li</span>></span>姓名：&#123;name&#125;&#125;<span class="hljs-tag"></<span class="hljs-name">li</span>></span>
                <span class="hljs-tag"><<span class="hljs-name">li</span>></span>性别：&#123;sex&#125;<span class="hljs-tag"></<span class="hljs-name">li</span>></span>
                <span class="hljs-tag"><<span class="hljs-name">li</span>></span>年龄：&#123;age&#125;<span class="hljs-tag"></<span class="hljs-name">li</span>></span>
            <span class="hljs-tag"></<span class="hljs-name">ul</span>></span></span>
        )
    &#125;
&#125;

<span class="hljs-comment">// ReactDOM.render( <Person name="Tom" sex="男" age="16"/>, document.querySelector("#root"));    // 以类似属性的方式传递 props值</span>

ReactDOM.render(<span class="xml"><span class="hljs-tag"><<span class="hljs-name">Person</span> &#123;<span class="hljs-attr">...p</span>&#125; /></span></span>, <span class="hljs-built_in">document</span>.querySelector(<span class="hljs-string">"#root"</span>))；  
<span class="hljs-comment">// 可以用扩展运算符来传递 props值</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>在使用的时候可以通过 <code>this.props</code>来获取值
类式组件的 <code>props</code>:</p>
<ol>
<li>通过在组件标签上传递值，在组件中就可以获取到所传递的值</li>
<li>在构造函数的参数里可以获取到 <code>props</code></li>
<li>可以分别设置 <code>propTypes</code> 和 <code>defaultProps</code> 两个属性来分别操作 <code>props</code>的规范和默认值，两者都是直接添加在类式组件的<strong>原型对象</strong>上的（所以需要添加 <code>static</code>）</li>
</ol>
<h4 data-id="heading-25">函数式组件中使用</h4>
<p>还记得说函数式组件的参数是什么吗？便是 <code>props</code>。<br>
传入的方式与类式组件相同，都是在组件标签中传递值</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">Person</span>(<span class="hljs-params">props</span>)</span>&#123;   <span class="hljs-comment">// 参数为 props</span>
    <span class="hljs-keyword">const</span> &#123;name, sex, age&#125; = props;     <span class="hljs-comment">// 使用占位符获取 props的值</span>
    <span class="hljs-keyword">return</span> (
        <span class="xml"><span class="hljs-tag"><<span class="hljs-name">ul</span>></span>
            <span class="hljs-tag"><<span class="hljs-name">li</span>></span>姓名：&#123;name&#125;&#125;<span class="hljs-tag"></<span class="hljs-name">li</span>></span>
            <span class="hljs-tag"><<span class="hljs-name">li</span>></span>性别：&#123;sex&#125;<span class="hljs-tag"></<span class="hljs-name">li</span>></span>
            <span class="hljs-tag"><<span class="hljs-name">li</span>></span>年龄：&#123;age&#125;<span class="hljs-tag"></<span class="hljs-name">li</span>></span>
        <span class="hljs-tag"></<span class="hljs-name">ul</span>></span></span>
    )
&#125;

Person.defaultProps = &#123;     <span class="hljs-comment">// 设置 props默认值</span>
    <span class="hljs-attr">sex</span>: <span class="hljs-string">"男"</span>,
    <span class="hljs-attr">age</span>: <span class="hljs-number">18</span>,
&#125;
Person.propTypes = &#123;    <span class="hljs-comment">// 设置 props限制</span>
    <span class="hljs-attr">name</span>: PropTypes.string.isRequired,
    <span class="hljs-attr">sex</span>: PropTypes.string,
    <span class="hljs-attr">age</span>: PropTypes.number,
&#125;

<span class="hljs-keyword">const</span> p = &#123;<span class="hljs-attr">name</span>:<span class="hljs-string">"Jerry"</span>, <span class="hljs-attr">sex</span>:<span class="hljs-string">"女"</span>, <span class="hljs-attr">age</span>:<span class="hljs-number">16</span>&#125;
ReactDOM.render(<span class="xml"><span class="hljs-tag"><<span class="hljs-name">Person</span> &#123;<span class="hljs-attr">...p</span>&#125;/></span></span>,<span class="hljs-built_in">document</span>.querySelector(<span class="hljs-string">"#app"</span>));
<span class="copy-code-btn">复制代码</span></code></pre>
<p>函数组件的 <code>props</code>定义:</p>
<ol>
<li>同样也是在组件标签中传递 <code>props</code>的值</li>
<li>组件函数的参数为 <code>props</code></li>
<li>对 <code>props</code>的限制和设置默认值也同样实在原型对象上</li>
</ol>
<h3 data-id="heading-26">3. refs</h3>
<p>假设在你的组件里有着表单元素，然后你需要获取到其中的值，该怎么获取呢？有的人可能想给元素绑定 <code>id</code>后用 <code>document.querySelector</code>来查找元素，但这样就违背了 <strong>React</strong>的想法，又开始操作起了DOM元素，所有<strong>React</strong>提供了第三种特性 <code>refs</code></p>
<p>在<strong>React</strong>的历史中，共有三种操作<code>refs</code>的方法，分别为：</p>
<ul>
<li>字符串形式</li>
<li>回调形式</li>
<li><code>createRef</code>形式</li>
</ul>
<p>让我们一一来了解一下：</p>
<h4 data-id="heading-27">类式组件中使用 <code>refs</code></h4>
<h5 data-id="heading-28">(1) 字符串形式的 <code>refs</code></h5>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Demo</span> <span class="hljs-keyword">extends</span> <span class="hljs-title">React</span>.<span class="hljs-title">Component</span></span>&#123;
    
    <span class="hljs-function"><span class="hljs-title">showData</span>(<span class="hljs-params"></span>)</span>&#123;
         <span class="hljs-comment">// 通过自己设定的 refs名称获取对应的元素</span>
        <span class="hljs-keyword">const</span> &#123;myInput&#125; = <span class="hljs-built_in">this</span>.refs;   <span class="hljs-comment">// 返回该元素</span>
        alert(myInput.value)
    &#125;
    
    <span class="hljs-function"><span class="hljs-title">render</span>(<span class="hljs-params"></span>)</span>&#123;
        <span class="hljs-keyword">return</span> (
            <span class="xml"><span class="hljs-tag"><<span class="hljs-name">div</span>></span>
                &#123; /* 通过 ref属性绑定这个 input标签 */ &#125;
                <span class="hljs-tag"><<span class="hljs-name">input</span> <span class="hljs-attr">type</span>=<span class="hljs-string">"text"</span> <span class="hljs-attr">ref</span>=<span class="hljs-string">"myInput"</span> <span class="hljs-attr">placeholder</span>=<span class="hljs-string">"search something"</span> /></span>
                &#123;/* 事件绑定会在下面讲 */&#125;
                <span class="hljs-tag"><<span class="hljs-name">button</span> <span class="hljs-attr">onClick</span>=<span class="hljs-string">&#123;this.showData&#125;</span>></span>Show Data<span class="hljs-tag"></<span class="hljs-name">button</span>></span>
            <span class="hljs-tag"></<span class="hljs-name">div</span>></span></span>
        )
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h5 data-id="heading-29">(2) 回调形式的 <code>refs</code></h5>
<p>其实很简单，但在后来的版本中，官方觉得这样做有问题，于是推出了全新的版本：使用回调函数来操作 <code>refs</code></p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Demo</span> <span class="hljs-keyword">extends</span> <span class="hljs-title">React</span>.<span class="hljs-title">Component</span></span>&#123;
    
    <span class="hljs-function"><span class="hljs-title">showData</span>(<span class="hljs-params"></span>)</span>&#123;
        <span class="hljs-keyword">const</span> &#123;myInput&#125; = <span class="hljs-built_in">this</span>;   <span class="hljs-comment">// 返回该元素</span>
        alert(myInput.value)
    &#125;
    <span class="hljs-function"><span class="hljs-title">render</span>(<span class="hljs-params"></span>)</span>&#123;
        <span class="hljs-keyword">return</span> (
            <span class="xml"><span class="hljs-tag"><<span class="hljs-name">div</span>></span>
                &#123;/* 回调函数的参数为该元素本身，通过函数绑定在 this上 */&#125;
                <span class="hljs-tag"><<span class="hljs-name">input</span> <span class="hljs-attr">type</span>=<span class="hljs-string">"text"</span> <span class="hljs-attr">ref</span>=<span class="hljs-string">&#123;</span> <span class="hljs-attr">e</span> =></span> this.myInput = e &#125; placeholder="search something" />
                <span class="hljs-tag"><<span class="hljs-name">button</span> <span class="hljs-attr">onClick</span>=<span class="hljs-string">&#123;this.showData&#125;</span>></span>Show Data<span class="hljs-tag"></<span class="hljs-name">button</span>></span>
            <span class="hljs-tag"></<span class="hljs-name">div</span>></span></span>
        )
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h5 data-id="heading-30">(3) createRef形式（推荐）</h5>
<p>后来的<strong>React</strong>发现，使用回调函数的形式还是会出现一些不可言喻的问题，所以，又一次推出了全新的的方法来使用 <code>refs</code>，便是使用 <strong>React</strong>身上的方法 <code>createRef()</code></p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Demo</span> <span class="hljs-keyword">extends</span> <span class="hljs-title">React</span>.<span class="hljs-title">Component</span></span>&#123;

    <span class="hljs-comment">// 使用 React.createRef() 创建一个 ref容器</span>
    myRef = React.createRef();

    showData = <span class="hljs-function">()=></span>&#123;
        <span class="hljs-comment">// 在容器中获取 DOM元素</span>
        <span class="hljs-keyword">const</span> &#123;current&#125; = <span class="hljs-built_in">this</span>.myRef;
        alter(current.value);
    &#125;

    <span class="hljs-function"><span class="hljs-title">render</span>(<span class="hljs-params"></span>)</span>&#123;
        <span class="hljs-keyword">return</span> (
            <span class="xml"><span class="hljs-tag"><<span class="hljs-name">div</span>></span>
                &#123;/* 将DOM元素绑定在容器中 */&#125;
                <span class="hljs-tag"><<span class="hljs-name">input</span> <span class="hljs-attr">ref</span>=<span class="hljs-string">&#123;this.myRef&#125;</span> <span class="hljs-attr">placeholder</span>=<span class="hljs-string">"点击提示数据"</span> <span class="hljs-attr">type</span>=<span class="hljs-string">"text"</span>/></span>
                <span class="hljs-tag"><<span class="hljs-name">button</span> <span class="hljs-attr">onClick</span>=<span class="hljs-string">&#123;this.showData&#125;</span>></span>ShowData<span class="hljs-tag"></<span class="hljs-name">button</span>></span>    
            <span class="hljs-tag"></<span class="hljs-name">div</span>></span></span>
        )
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>注意：一个 <code>ref</code>容器，只能存储一个元素（专人专用），后加入的会把前一个顶出去</p>
<h4 data-id="heading-31">函数式组件中使用 <code>refs</code></h4>
<ul>
<li>在<strong>React16.8</strong>前，与 <code>state</code>相同，函数式组件也无法使用 <code>refs</code>特性</li>
<li>在<strong>React16.8</strong>后，出现了 <code>Hook</code>函数，使得函数式组件也有了使用 <code>refs</code>特性的能力</li>
</ul>
<p>以下代码现阶段无需看懂先，了解即可。</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">Demo</span>(<span class="hljs-params"></span>) </span>&#123;
    <span class="hljs-keyword">const</span> [count, setCount] = React.useState(<span class="hljs-number">0</span>);
    <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">add</span>(<span class="hljs-params"></span>)</span>&#123;
        setCount(<span class="hljs-function"><span class="hljs-params">count</span>=></span> count+<span class="hljs-number">1</span>);
    &#125;
    <span class="hljs-keyword">return</span> (
        <span class="xml"><span class="hljs-tag"><<span class="hljs-name">div</span>></span>
            <span class="hljs-tag"><<span class="hljs-name">h2</span>></span>当前求和：&#123;count&#125;<span class="hljs-tag"></<span class="hljs-name">h2</span>></span>
            <span class="hljs-tag"><<span class="hljs-name">button</span> <span class="hljs-attr">onClick</span>=<span class="hljs-string">&#123;add&#125;</span>></span>点击加一<span class="hljs-tag"></<span class="hljs-name">button</span>></span>
        <span class="hljs-tag"></<span class="hljs-name">div</span>></span></span>
    )
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-32">四、组件的事件绑定</h2>
<h3 data-id="heading-33">1. 在函数式组件中进行事件绑定</h3>
<p>可以在函数中定义另外一个函数（内置函数）然后进行调用即可</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">Demo</span>(<span class="hljs-params">props</span>)</span>&#123;
    <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">showData</span>(<span class="hljs-params"></span>)</span>&#123;
        <span class="hljs-built_in">console</span>.log(props);
        alert(<span class="hljs-string">"触发了事件"</span>);
    &#125;
    <span class="hljs-keyword">return</span> (
        <span class="xml"><span class="hljs-tag"><<span class="hljs-name">div</span>></span>
            <span class="hljs-tag"><<span class="hljs-name">button</span> <span class="hljs-attr">onClick</span>=<span class="hljs-string">&#123;showData&#125;</span>></span>点击触发<span class="hljs-tag"></<span class="hljs-name">button</span>></span>
        <span class="hljs-tag"></<span class="hljs-name">div</span>></span></span>
    )
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-34">2. 在类式组件中进行事件绑定</h3>
<p>在类式组件中可以通过类本身的方法来调用</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Demo</span> <span class="hljs-keyword">extends</span> <span class="hljs-title">React</span>.<span class="hljs-title">Component</span></span>&#123;
    state = &#123; <span class="hljs-attr">count</span>: <span class="hljs-number">0</span> &#125;    <span class="hljs-comment">// 定义 state</span>
    <span class="hljs-function"><span class="hljs-title">showData</span>(<span class="hljs-params"></span>)</span>&#123;
        alert(<span class="hljs-string">"触发了事件"</span>)
        <span class="hljs-built_in">console</span>.log(<span class="hljs-built_in">this</span>.state.count);; 报错
    &#125;
    <span class="hljs-function"><span class="hljs-title">render</span>(<span class="hljs-params"></span>)</span>&#123;
        <span class="hljs-keyword">return</span> (
            <span class="xml"><span class="hljs-tag"><<span class="hljs-name">div</span>></span>
                <span class="hljs-tag"><<span class="hljs-name">button</span> <span class="hljs-attr">onClick</span>=<span class="hljs-string">&#123;this.showData&#125;</span>></span><span class="hljs-tag"></<span class="hljs-name">button</span>></span>
            <span class="hljs-tag"></<span class="hljs-name">div</span>></span></span>
        )
        <span class="hljs-comment">// 成功弹出弹窗，但是输出报错</span>
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><em>这里你会发现，虽然成功 <code>alter</code>，但是输出 <code>state</code>会报错，这是为什么呢？</em></p>
<p>平时在组件内使用 <code>this.state</code>的时候，此时 <code>this</code>的指向都是作用于类的<strong>原型对象</strong>，即类本身。<br>
而在函数中，因为使用了 <code>babel.js</code>的缘故，<code>js</code>默认开启了<strong>严格模式</strong>，所以函数体的 <code>this</code>为 <code>undefined</code>，自然找不到在原型对象上的 <code>state</code>。<br>
此时有两种解决方法：</p>
<ul>
<li>使用 <code>bind</code>、<code>apply</code>等方法改变 <code>this</code>指向</li>
<li>使用<strong>箭头函数</strong>，改变 <code>this</code>指向（推荐）</li>
</ul>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Demo</span> <span class="hljs-keyword">extends</span> <span class="hljs-title">React</span>.<span class="hljs-title">Component</span></span>&#123;
    <span class="hljs-function"><span class="hljs-title">constractor</span>(<span class="hljs-params">props</span>)</span>&#123;
        <span class="hljs-built_in">super</span>(props);
        <span class="hljs-comment">// this.showData = this.showData.bind(this);   // 方法1</span>
    &#125;
    
    state = &#123; <span class="hljs-attr">count</span>: <span class="hljs-number">0</span> &#125;    <span class="hljs-comment">// 定义 state</span>
    showData = <span class="hljs-function">()=></span>&#123;    <span class="hljs-comment">// 方法2</span>
        alert(<span class="hljs-string">"触发了事件"</span>)
        <span class="hljs-built_in">console</span>.log(<span class="hljs-built_in">this</span>.state.count);; 报错
    &#125;
    <span class="hljs-function"><span class="hljs-title">render</span>(<span class="hljs-params"></span>)</span>&#123;
        <span class="hljs-keyword">return</span> (
            <span class="xml"><span class="hljs-tag"><<span class="hljs-name">div</span>></span>
                <span class="hljs-tag"><<span class="hljs-name">button</span> <span class="hljs-attr">onClick</span>=<span class="hljs-string">&#123;this.showData&#125;</span>></span><span class="hljs-tag"></<span class="hljs-name">button</span>></span>
            <span class="hljs-tag"></<span class="hljs-name">div</span>></span></span>
        )
        <span class="hljs-comment">// 成功弹出弹窗，但是输出报错</span>
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-35">3. React的事件处理方法</h3>
<ul>
<li>通过 <code>onXxx</code>属性指定事件处理函数（注意大小写
<ul>
<li>
<p><strong>React</strong>使用的是<strong>自定义（合成）事件</strong>，而不是原生的 DOM事件（为了更好的兼容性）</p>
</li>
<li>
<p><strong>React</strong>的事件是通过事件委托方式处理的（委托给组件最外层的元素）（为了更加的高效）</p>
</li>
<li>
<p>可以通过事件的 <code>event.target</code>获取发生的DOM元素对象，可以尽量减少 <code>refs</code>的使用</p>
</li>
<li>
<p>在绑定事件的时候<strong>不要加括号</strong>，这会被 <code>jsx</code>识别为执行函数</p>
</li>
<li>
<p>在类式组件中绑定函数注意 <code>this</code>的指向问题（推荐绑定的函数都使用<strong>箭头函数</strong>）</p>
</li>
</ul>
</li>
</ul>
<h2 data-id="heading-36">五、组件的生命周期</h2>
<p>对 <code>Vue</code>熟悉的应该对<strong>生命周期</strong>并不陌生。<br>
组件在挂载到页面上的过程中，期间发生了许多的事情，而生命周期，可以看作是<strong>一个组件的执行流程</strong>，我们可以通过在某个流程节点中进行一些操作，而这就是 <strong>生命周期钩子（函数）</strong><br>
<em>注：生命周期函数只适用于类式组件，并不适用于函数式组件，但是在<strong>React16.8</strong>之后的 <code>Hook</code>，也可以让函数式组件实现类似于生命周期钩子的功能</em></p>
<h3 data-id="heading-37">1. React 16之前</h3>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/2aa6b5432ea54b8ca286823714e3e5bc~tplv-k3u1fbpfcp-watermark.image" alt="592_1.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>以下是流程：</p>
<ul>
<li>自身组件挂载
<ol>
<li><code>constructor</code>: 构造函数（初始化）</li>
<li><code>componentWillMount</code>: 组件挂载前</li>
<li><code>render</code>: 组件挂载中</li>
<li><code>componentDidMount</code>: 组件挂载完成后</li>
</ol>
</li>
<li>拥有父组件且父组件状态进行更新（<code>setState</code>）：
<ol>
<li>父组件 <code>shouldComponentUpdate</code>: 父组件是否进行状态更新</li>
<li>父组件 <code>componentWillUpdate</code>: 父组件状态更新前</li>
<li>父组件 <code>render</code>: 父组件更新挂载中</li>
<li>子组件 <code>componentWillReceiveProps</code>: 子组件将收到新的<code>Props</code></li>
<li>子组件 <code>shouldComponentUpdate</code>: 子组件是否进行状态更新</li>
<li>子组件 <code>componentWillUpdate</code>: 子组件状态更新前</li>
<li>子组件 <code>render</code>: 子组件更新挂载中</li>
<li>子组件 <code>componentDidMount</code>: 子组件挂载完成</li>
<li>父组件 <code>componentDidMount</code>: 父组件挂载完成</li>
</ol>
</li>
<li>当组件要进行卸载时：
<ol>
<li><code>componentWillUnmount</code>: 组件卸载前</li>
</ol>
</li>
</ul>
<p>有几个需要注意的地方：</p>
<ul>
<li><code>shouldComponentUpdate</code>的意思是是否更新状态，所以他应该有个<strong>布尔</strong>类型返回值，而且默认为 <code>true</code>（不写的时候），当你写了这个钩子时别忘了写个返回值，这个横眉周期一般用于进行更新值的一些判断。</li>
<li><code>shouldComponentUpdate</code>有两个参数，分别是 <code>nextProps</code>：新的<code>props</code> 与 <code>nextState</code>： 新的<code>state</code>，此时他们都还没更新到组件上。</li>
<li>使用 <code>setState</code>时会经过生命周期 <code>shouldComponentUpdate</code>，但是使用 <code>forceUpdate</code>时则不会，而是直接到 <code>componentWillUpdate</code>生命周期</li>
</ul>
<h3 data-id="heading-38">2. React 16之后</h3>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/fa947c75a4cb42d796845385adf7888f~tplv-k3u1fbpfcp-watermark.image" alt="594_1.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>新旧生命周期对比：</p>
<ol>
<li>在新的生命周期中，舍弃了（即将舍弃）三个生命周期函数：
<ul>
<li><code>componentWillMount</code></li>
<li><code>componentWillReceiveProps</code></li>
<li><code>componentWillUpdate</code></li>
</ul>
</li>
<li>新增了两个生命周期函数：
<ul>
<li>
<p><code>getDerivedStateFromProps</code></p>
</li>
<li>
<p><code>getSnapshotBeforeUpdate</code></p>
</li>
</ul>
</li>
</ol>
<p>以下是流程：</p>
<ul>
<li>自身组件挂载：
<ol>
<li><code>constructor</code>: 构造函数（初始化）</li>
<li><code>getDerivedStateFromProps</code>: 从<code>props</code>中获取派生的<code>state</code></li>
<li><code>render</code>: 组件挂载中</li>
<li><code>componentDidMount</code>: 组件完成挂载</li>
</ol>
</li>
<li>父组件更新时
<ol>
<li>父组件 <code>getDerivedStateFromProps</code>: 从 <code>props</code>中获取派生的<code>state</code></li>
<li>父组件 <code>shouldComponentUpdate</code>: 判断是否进行状态更新</li>
<li>父组件 <code>render</code>: 父组件挂载中</li>
<li>子组件 <code>getDerivedStateFromProps</code>: 从 <code>props</code>中获取派生的<code>state</code></li>
<li>子组件 <code>shouldComponentUpdate</code>: 判断是否进行状态更新</li>
<li>子组件 <code>render</code>: 子组件挂载中</li>
<li>子组件 <code>getSnapshotBeforeUpdate</code>: 子组件获取状态更新前的快照</li>
<li>子组件 <code>componentDidUpdate</code>: 子组件完成更新</li>
<li>父组件 <code>getSnapshotBeforeUpdate</code>: 父组件获取状态更新前的快照</li>
<li>父组件 <code>componentDidUpdate</code>: 父组件完成更新</li>
</ol>
</li>
<li>组件卸载时
<ol>
<li><code>componentWillUnmount</code>: 组件卸载前</li>
</ol>
</li>
</ul>
<p>也有几个需要注意的地方：</p>
<ul>
<li><code>getDerivedStateFromProps</code> 需要定义个实例本身，所以是静态方法</li>
<li><code>getDerivedStateFromProps</code> 有两个参数，分别是当前的 <code>props</code>和 <code>state</code></li>
<li>若需要组件的状态任何时候都取决于 <code>props</code>则可以使用 <code>getDerivedStateFromProps</code>，但是使用场景比较罕见，可以在其中定义 <code>state</code></li>
<li><code>getSnapshotBeforeUpdate</code> 有两个参数，分别为状态更新前的 <code>props</code> 和<code>state</code>，并且有一个返回值（快照），一般用作本次更新情况的说明情况。</li>
<li><code>componentDidUpdate</code> 有三个参数，分别为状态更新前的 <code>props</code> 和 <code>state</code>，以及先前 <code>getSnapshotBeforeUpdate</code>返回的快照。</li>
<li>其他的与旧的生命周期没有什么差别</li>
</ul>
<h2 data-id="heading-39">六、组件列表渲染、条件渲染与DOM的<code>Diffing</code>算法</h2>
<h3 data-id="heading-40">1. 组件列表渲染</h3>
<p>在有时候我们需要批量的去创建一些DOM元素或组件，比如页面上的：新闻列表、推文列表、好友列表等等，你会发现在开发的过程中经常会使用到列表，但是自己一个个的去写DOM回十分繁琐。<br>
我们可以通过数组存储数据，也可以使用数组来循环渲染数据。<br>
举个例子：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Demo</span> <span class="hljs-keyword">extends</span> <span class="hljs-title">React</span>.<span class="hljs-title">Component</span></span>&#123;
    state = &#123;
        <span class="hljs-attr">arr</span>: [a, b, c],
    &#125;
    <span class="hljs-function"><span class="hljs-title">render</span>(<span class="hljs-params"></span>)</span>&#123;
        <span class="hljs-comment">// 输出 abc</span>
        <span class="hljs-keyword">return</span> (
            <span class="xml"><span class="hljs-tag"><<span class="hljs-name">div</span>></span>
                <span class="hljs-tag"><<span class="hljs-name">ul</span>></span> &#123;stus&#125; <span class="hljs-tag"></<span class="hljs-name">ul</span>></span>
            <span class="hljs-tag"></<span class="hljs-name">div</span>></span></span>
        )
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>你会发现，<strong>React</strong>输出数组会把所有的元素直接循环输出出来，那么我们只要在每个元素左右添加上标签，那不就构成了列表渲染吗？<br>
这里我们可以通过 <code>jsx</code>语法配合<code>ES6</code>语句来实现列表渲染。<br>
直接上代码：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Demo</span> <span class="hljs-keyword">extends</span> <span class="hljs-title">React</span>.<span class="hljs-title">Component</span></span>&#123;
    state = &#123;
        <span class="hljs-attr">stus</span>: [
            &#123;<span class="hljs-attr">id</span>: <span class="hljs-string">"001"</span>, <span class="hljs-attr">name</span>: <span class="hljs-string">"小明"</span>, <span class="hljs-attr">age</span>: <span class="hljs-string">"28"</span>&#125;,
            &#123;<span class="hljs-attr">id</span>: <span class="hljs-string">"002"</span>, <span class="hljs-attr">name</span>: <span class="hljs-string">"小红"</span>, <span class="hljs-attr">age</span>: <span class="hljs-string">"26"</span>&#125;,
        ],
    &#125;
    <span class="hljs-function"><span class="hljs-title">render</span>(<span class="hljs-params"></span>)</span>&#123;
        <span class="hljs-keyword">return</span> (
            <span class="xml"><span class="hljs-tag"><<span class="hljs-name">div</span>></span>
                <span class="hljs-tag"><<span class="hljs-name">ul</span>></span>
                    &#123;
                        this.state.stus.map(item =>&#123;
                            return <span class="hljs-tag"><<span class="hljs-name">li</span> <span class="hljs-attr">key</span>=<span class="hljs-string">&#123;item.id&#125;</span>></span>&#123;item.name&#125;---&#123;item.age&#125;<span class="hljs-tag"></<span class="hljs-name">li</span>></span>
                        &#125;)
                    &#125;
                <span class="hljs-tag"></<span class="hljs-name">ul</span>></span>
            <span class="hljs-tag"></<span class="hljs-name">div</span>></span></span>
        )
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/d7829a545c36492f92d60db73bb55a35~tplv-k3u1fbpfcp-watermark.image" alt="598_1.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-41">2. key 的使用</h3>
<p>有的人发现了写列表渲染的时候，我都会给每个标签加上一个 <code>key</code>属性，这是为什么呢？<br>
其实 <code>key</code>的作用是给当前的标签添加一个<strong>唯一的标识</strong>，用于给<strong>React</strong>进行 <strong>diffing算法</strong>计算的时候使用</p>
<h3 data-id="heading-42">3. diffing 算法</h3>
<p>当状态发生改变时，react会根据【新的状态】生成【新的虚拟DOM】<br>
然后将新旧虚拟DOM进行 diff比较，比较规则如下：</p>
<ol>
<li>旧虚拟DOM 中<strong>找到了</strong>与 新虚拟DOM 相同的 key
<ul>
<li>若虚拟DOM中的内容没变，则直接使用之前的真实DOM</li>
<li>若虚拟DOM中的内容变了，则生成新的真实DOM并进行替换           </li>
</ul>
</li>
<li>旧虚拟DOM 中<strong>未找到</strong>与 新虚拟DOM 相同的 key，则根据数据创建新的真实DOM，然后渲染到页面</li>
</ol>
<hr>
<p><em>用index作为key可能引发的问题</em></p>
<ul>
<li>对数据进行 逆序添加、逆序删除 邓破坏顺序的操作
会产生没有必要的真实DOM更新，影响效率</li>
<li>对结构中包含输入类的DOM
会产生错误的 DOM更新，同时界面渲染有问题</li>
<li>若仅用于展示数据，那用 index作为 key则没有问题 </li>
</ul>
<h2 data-id="heading-43">七、React脚手架</h2>
<p>恭喜，终于熬到了脚手架这里了，终于可以一键生成所有东西而不是自己一个个引用了。<br>
什么是脚手架呢？  脚手架可以说是建房子时的构架，其他人已经帮你吧房子的架构搭好了，不需要自己动手。<br>
而<strong>React</strong>就有自己的脚手架，开发团队通过 <code>webpack</code>，<code>babel</code>、<code>npm</code>等方法，帮你搭建好了一个使用<strong>React</strong>开发软件的环境，不再需要自己去创建文件夹，导入<strong>React</strong>等重复的操作，更加利于我们编写 <code>SPA</code>应用（单页面富应用）。</p>
<h3 data-id="heading-44">1. 安装React脚手架</h3>
<p>在自己的命令行窗口中输入（需要现有 <code>node</code>环境）：</p>
<pre><code class="hljs language-node copyable" lang="node">npm i create-react-app -g
<span class="copy-code-btn">复制代码</span></code></pre>
<p>全局安装 <code>create-react-app</code>脚手架</p>
<h3 data-id="heading-45">2. 创建React应用</h3>
<pre><code class="hljs language-node copyable" lang="node">create-create-app 应用名称
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>应用名称不应该出现大写字母和特殊字符</li>
<li>使用英文命名而不是中文命名</li>
</ul>
<h3 data-id="heading-46">3. 文件解析</h3>
<p>项目文件中比较常用的文件就以下这些：</p>
<ul>
<li><strong>node_modules</strong> ------ npm包的存放位置</li>
<li><strong>public</strong> ------ 用于存放静态文件</li>
<li><strong>src</strong> ------ 项目的代码存放位置
<ul>
<li><strong>components</strong> ------ 用于存放公用组件的文件夹</li>
<li><strong>page</strong> ------ 用于存放页面的文件夹</li>
<li><code>App.js</code> ------ 根组件</li>
<li><code>App.css</code> ------ 根组件的样式</li>
<li><code>index.js</code> ------ 项目入口文件</li>
<li><code>index.css</code> ------ 项目的公用样式</li>
</ul>
</li>
<li><code>.gitgnore</code> ------ 编写<code>git</code>的配置文件</li>
<li><code>package.json</code> ------ 项目配置文件</li>
<li><code>README.md</code> ------ 项目信息</li>
</ul>
<p>还记得我们的讲组件化的图片吗</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/b654a24918094ebc806d4a67116acafb~tplv-k3u1fbpfcp-watermark.image" alt="582_1.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>其中的 <code>APP</code>就是根组件，通过我们编写其他的组件如 <code>Header</code>、<code>Aside</code>等组件，都加装在根组件上。</p>
<h3 data-id="heading-47">4. npm 指令</h3>
<pre><code class="hljs language-node copyable" lang="node">npm start       // 使用 webpack-dev-server 启动服务查看应用
npm build       // 打包生成生产文件
npm test        // 进行软件测试（不常用）
npm eject       // 将所有的配置文件暴漏出来（不常用且不建议用）
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-48">八、react-router的使用</h2>
<h3 data-id="heading-49">1. 什么是 react-router</h3>
<p><code>react-router</code> 是为了<strong>React</strong>编写<code>SPA</code>应用操作<strong>前端路由</strong>而诞生的。</p>
<h4 data-id="heading-50">(1) 前端路由（可能有点直白）</h4>
<p><strong>前端路由</strong>是通过<code>HTML5</code>的新API <code>History</code>来操作的，其原理就是url地址的地址发生改变，但是并不会触发重新加载，同时<code>javascript</code>可以监听到改变。<br>
有两种类型：</p>
<ul>
<li><code>HashRouter</code>: 利用<strong>url地址栏</strong>的 <strong>#</strong> 后面的<strong>哈希值</strong></li>
</ul>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/b0562d1234ff4e87a86660b7707cf994~tplv-k3u1fbpfcp-watermark.image" alt="606_2.png" loading="lazy" referrerpolicy="no-referrer"></p>
<ul>
<li><code>BrowserRouter</code>: 利用浏览器的<strong>History API</strong>，地址栏中不包含 <strong>#</strong> ，显得更加美观</li>
</ul>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/4eff153c596141bab8e4936d8c672aab~tplv-k3u1fbpfcp-watermark.image" alt="604_1.png" loading="lazy" referrerpolicy="no-referrer"></p>
<blockquote>
<p>以上两种情况都不会触发 url的跳转功能</p>
</blockquote>
<h4 data-id="heading-51">(2) SPA 应用</h4>
<p><code>SPA</code> 全称 <strong>Single Page web Application</strong>，顾名思义是只有<strong>一个页面的应用</strong>，通过<code>javascript</code>进行实时的渲染来更新页面。<br>
即通过当前的路由来判断页面应该加载什么组件，从而呈现不同的页面与效果。</p>
<h3 data-id="heading-52">2. 使用 react-router</h3>
<h4 data-id="heading-53">(1) 安装与使用</h4>
<p>在项目文件夹中打开命令行窗口进行 <code>npm</code>下载</p>
<pre><code class="hljs language-node copyable" lang="node">npm i react-router-dom -S
<span class="copy-code-btn">复制代码</span></code></pre>
<p><em>注意：我们下载的是 <code>react-router-dom</code> 而不是 <code>react-router</code></em>
两者区别：</p>
<ul>
<li><code>react-router</code>：提供了<code>router</code>的核心 API。如<code>Router</code>、<code>Route</code>、<code>Switch</code>等，但<strong>没有提供有关dom操作进行路由跳转的API</strong>；</li>
<li><code>react-router-dom</code>：提供了<code>BrowserRouter</code>、<code>Route</code>、<code>Link</code>等api，<strong>可以通过dom操作触发事件控制路由</strong>。</li>
</ul>
<blockquote>
<p><code>react-router-dom</code>中包含了<code>react-router</code>，所以我们选择下 <code>react-router-dom</code>。</p>
</blockquote>
<h4 data-id="heading-54">(2) 常用组件</h4>
<h5 data-id="heading-55">a. 路由跳转</h5>
<p>在多页面应用中，通常都是使用 <code>a</code>标签进行页面跳转</p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">a</span> <span class="hljs-attr">href</span>=<span class="hljs-string">"http://localhost:3000"</span>></span>跳转页面<span class="hljs-tag"></<span class="hljs-name">a</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>使用单页面富应用中使用<code>react-router</code>则使用路由跳转组件</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">import</span> &#123;Link, NavLink&#125; <span class="hljs-keyword">from</span> <span class="hljs-string">"react-router"</span>;
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">Link</span> <span class="hljs-attr">activeClassName</span>=<span class="hljs-string">"nav-active"</span> <span class="hljs-attr">className</span>=<span class="hljs-string">"nav"</span> <span class="hljs-attr">to</span>=<span class="hljs-string">"/about"</span>></span>About<span class="hljs-tag"></<span class="hljs-name">Link</span>></span>
<span class="hljs-tag"><<span class="hljs-name">NavLink</span> <span class="hljs-attr">activeClassName</span>=<span class="hljs-string">"nav-active"</span> <span class="hljs-attr">className</span>=<span class="hljs-string">"nav"</span> <span class="hljs-attr">to</span>=<span class="hljs-string">"/home"</span>></span>Home<span class="hljs-tag"></<span class="hljs-name">NavLink</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li><code>activeClassName</code>: 处于当前路由时，对应的组件会自动添加该类</li>
<li><code>className</code>: 当前组件类名</li>
<li><code>to</code>: 当前组件所对应的路由</li>
</ul>
<p><code>Link</code>组件与 <code>NavLink</code>组件都可以进行路由的跳转，区别在于：当前路由对应的<code>NavLink</code>会自动添加<code>class</code>: <code>active</code>，而 <code>Link</code>不会。</p>
<h5 data-id="heading-56">b. 注册路由</h5>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">import</span> &#123;Route&#125; <span class="hljs-keyword">from</span> <span class="hljs-string">"react-router"</span>;
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">Route</span> <span class="hljs-attr">path</span>=<span class="hljs-string">"/home"</span> <span class="hljs-attr">component</span>=<span class="hljs-string">&#123;Home&#125;</span>></span><span class="hljs-tag"></<span class="hljs-name">Route</span>></span>
<span class="hljs-tag"><<span class="hljs-name">Route</span> <span class="hljs-attr">exact</span> <span class="hljs-attr">path</span>=<span class="hljs-string">"/about"</span> <span class="hljs-attr">component</span>=<span class="hljs-string">&#123;About&#125;</span>></span><span class="hljs-tag"></<span class="hljs-name">Route</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li><code>path</code>: 所要监听的路由</li>
<li><code>component</code>: 该路由要绑定的组件</li>
<li><code>exact</code>: 可选，不写时为 <code>false</code>，是否选择严格匹配</li>
</ul>
<p>当当前路由对应上了路由组件所绑定的路由时，则会展示所绑定的组件。</p>
<h6 data-id="heading-57">(a) 路由严格匹配与模糊匹配</h6>
<p>路由不仅仅只有一级，有的时候是有多级嵌套的，比如以下这张：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/b0562d1234ff4e87a86660b7707cf994~tplv-k3u1fbpfcp-watermark.image" alt="606_2.png" loading="lazy" referrerpolicy="no-referrer"><br>
<strong>模糊匹配</strong>和<strong>严格匹配</strong>，都是指当前的组件对当前路由的匹配模式：</p>
<ul>
<li><strong>模糊匹配</strong>: 如果当前路由与匹配的路由成相等或包含（注意层级）的情况，则启用该组件
<ul>
<li><code>http://localhost:3000/home/a/b/c</code> 则为包含路由 <code>/home</code></li>
<li><code>http://localhost:3000/a/b/home/c</code> 则为不包含路由 <code>/home</code>（<em>层级不对</em>）</li>
</ul>
</li>
<li><strong>严格匹配</strong>: 如果当前路由与匹配的路由相等的话，才启用该组件
<ul>
<li><code>http://localhost:3000/home</code> 则为与路由 <code>/home</code> 相等</li>
<li><code>http://localhost:3000/home/a</code> 则为与路由 <code>/home</code> 不相等</li>
</ul>
</li>
</ul>
<h5 data-id="heading-58">c. 重定向路由</h5>
<p>你明明设置好了路由 <code>/home</code>，但是有的用户就喜欢对着干，在地址栏输入了 <code>/nothing</code>，而你没有注册这个路由，那该怎么办呢？<br>
这个时候你就可以东涌道<strong>重定向路由</strong>了，对于没有注册过的路由，都会被跳转到你指定的某个路由去，这就是<strong>重定向路由</strong>。<br>
经常可以用作一些<strong>404</strong>，<strong>页面丢失</strong>等情况的路由跳转方式。</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">import</span> &#123;Redirect, Route&#125; <span class="hljs-keyword">from</span> <span class="hljs-string">"react-router"</span>;
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">Route</span> <span class="hljs-attr">......</span>/></span>
<span class="hljs-tag"><<span class="hljs-name">Route</span> <span class="hljs-attr">......</span>/></span>
<span class="hljs-tag"><<span class="hljs-name">Redirect</span> <span class="hljs-attr">to</span>=<span class="hljs-string">"/home"</span>/></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li><code>to</code>: 需要重定向到哪个路由？</li>
</ul>
<p><code>Redirect</code>需放在所有<code>Route</code>下面，当上面的 <code>Route</code>都没有匹配到时，则路由将重定向到指定的路由。</p>
<h5 data-id="heading-59">d. Switch 路由</h5>
<p>你想想，如果你的路由中，出现了 <code>/home</code> 与 <code>/home/abc</code> 和 <code>/home/a/b/c</code> 等这样的路由，当路由为 <code>/home</code>时则会三个路由都同时渲染，但是你又只想要渲染其中的一条，这个时候我们就可以使用 <code>Switch</code>组件。<br>
使用 <code>Switch</code>组件包裹住所有的 <code>Route</code> 和 <code>Redirect</code>，当出现多个匹配的路由时，只会渲染第一个匹配的组件。</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">import</span> &#123;Switch, Route, Redirect&#125; <span class="hljs-keyword">from</span> <span class="hljs-string">"react-router"</span>;
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">Switch</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">Route</span> <span class="hljs-attr">....</span>/></span>
    <span class="hljs-tag"><<span class="hljs-name">Route</span> <span class="hljs-attr">....</span>/></span>
    <span class="hljs-tag"><<span class="hljs-name">Redirect</span> <span class="hljs-attr">to</span>=<span class="hljs-string">"..."</span>/></span>
<span class="hljs-tag"></<span class="hljs-name">Switch</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h5 data-id="heading-60">e. 路由器</h5>
<p>你想要使用路由跳转组件和路由组件，还差一个路由器组件，同时路由器组件必须包裹着这两个组件。</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">import</span> &#123;HashRouter, BrowserRouter&#125; <span class="hljs-keyword">from</span> <span class="hljs-string">"react-router"</span>;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>一般为了使整个<strong>React应用</strong>都可以使用到路由组件，所以一般我们都是把路由器包裹在根组件上的。</p>
<pre><code class="hljs language-javascript copyable" lang="javascript">ReactDOM.render( 
    <span class="xml"><span class="hljs-tag"><<span class="hljs-name">BrowserRouter</span>></span>
        <span class="hljs-tag"><<span class="hljs-name">App</span>/></span>
    <span class="hljs-tag"></<span class="hljs-name">BrowserRouter</span>></span></span>,
    <span class="hljs-built_in">document</span>.querySelector(<span class="hljs-string">"#root"</span>)
);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>有两种路由器组件，分别是<code>HashRouter</code> 与 <code>BrowserRouter</code>，分别对应者两种路由方式。</p>
<h4 data-id="heading-61">(3) 路由组件</h4>
<p>路由组件与一般组件</p>
<ol>
<li>写法不同
<ul>
<li>一般组件：<code><Demo></Demo></code></li>
<li>路由组件：<code><Route path="/demo" component=&#123;Demo&#125;/></code></li>
</ul>
</li>
<li>存放位置不同
<ul>
<li>一般组件：<strong>components文件夹</strong></li>
<li>路由组件：<strong>page 文件夹</strong></li>
</ul>
</li>
<li>接受到的 <code>props</code> 不同
<ul>
<li>一般组件：根据组件标签传递了上面，就收到了什么</li>
<li>路由标签：会收到三个固定的属性</li>
</ul>
</li>
</ol>
<pre><code class="hljs language-json copyable" lang="json">&#123;
  <span class="hljs-attr">"history"</span>: &#123;
    <span class="hljs-attr">"length"</span>: <span class="hljs-number">18</span>,
    <span class="hljs-attr">"action"</span>: <span class="hljs-string">"PUSH"</span>,
    <span class="hljs-attr">"location"</span>: &#123;
      <span class="hljs-attr">"pathname"</span>: <span class="hljs-string">"/home"</span>,
      <span class="hljs-attr">"search"</span>: <span class="hljs-string">""</span>,
      <span class="hljs-attr">"hash"</span>: <span class="hljs-string">""</span>,
      <span class="hljs-attr">"key"</span>: <span class="hljs-string">"tvfyve"</span>
    &#125;
  &#125;,
  <span class="hljs-attr">"location"</span>: &#123;
    <span class="hljs-attr">"pathname"</span>: <span class="hljs-string">"/home"</span>,
    <span class="hljs-attr">"search"</span>: <span class="hljs-string">""</span>,
    <span class="hljs-attr">"hash"</span>: <span class="hljs-string">""</span>,
    <span class="hljs-attr">"key"</span>: <span class="hljs-string">"tvfyve"</span>
  &#125;,
  <span class="hljs-attr">"match"</span>: &#123;
    <span class="hljs-attr">"path"</span>: <span class="hljs-string">"/home"</span>,
    <span class="hljs-attr">"url"</span>: <span class="hljs-string">"/home"</span>,
    <span class="hljs-attr">"isExact"</span>: <span class="hljs-literal">true</span>,
    <span class="hljs-attr">"params"</span>: &#123;&#125;
  &#125;
&#125; 
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-62">3.嵌套路由</h3>
<p>假设我们有个路由组件为 <code>Home</code>，在根组件中使用 <code>Link</code>跳转到了该路由，当前路由为 <code>/home</code>，可在组件 <code>Home</code> 中还有两个 <code>Link</code>，分别导向路由 <code>/home/message</code> 与 <code>/home/news</code> 然后在组件中还有其他的路由组件。这就时嵌套路由的使用。<br>
如下面的代码：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Home</span> <span class="hljs-keyword">extends</span> <span class="hljs-title">Component</span></span>&#123;
    <span class="hljs-function"><span class="hljs-title">render</span>(<span class="hljs-params"></span>)</span>&#123;
        <span class="hljs-keyword">return</span> (
            <span class="xml"><span class="hljs-tag"><<span class="hljs-name">div</span>></span>
                <span class="hljs-tag"><<span class="hljs-name">Link</span> <span class="hljs-attr">to</span>=<span class="hljs-string">"/home/message"</span>></span>Message<span class="hljs-tag"></<span class="hljs-name">Link</span>></span>
                <span class="hljs-tag"><<span class="hljs-name">Link</span> <span class="hljs-attr">to</span>=<span class="hljs-string">"/home/news"</span>></span>News<span class="hljs-tag"></<span class="hljs-name">Link</span>></span>
                <span class="hljs-tag"><<span class="hljs-name">hr</span>/></span>
                <span class="hljs-tag"><<span class="hljs-name">Route</span> <span class="hljs-attr">path</span>=<span class="hljs-string">"/home/message"</span> <span class="hljs-attr">component</span>=<span class="hljs-string">&#123;Message&#125;</span> /></span>
                <span class="hljs-tag"><<span class="hljs-name">Route</span> <span class="hljs-attr">path</span> =<span class="hljs-string">"/home/news"</span> <span class="hljs-attr">component</span>=<span class="hljs-string">&#123;News&#125;</span> /></span>
            <span class="hljs-tag"></<span class="hljs-name">div</span>></span></span>
        )
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-63">4. 编程式路由</h3>
<p>如果说，我们想要做用户点击按钮登陆后，如果他是老师就去老师页面，如果是学生就去学生页面，这个显然单靠 <code>Ljnk</code> 无法完成，我们可以通过 <code>js</code>进行路由的跳转（也是 <code>react-router</code> 基于 <code>History API</code> 编写的）</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Message</span> <span class="hljs-keyword">extends</span> <span class="hljs-title">Component</span> </span>&#123;
    state = &#123;
        <span class="hljs-attr">messageArr</span>:[
            &#123;<span class="hljs-attr">id</span>:<span class="hljs-string">"01"</span>, <span class="hljs-attr">title</span>: <span class="hljs-string">"消息1"</span>&#125;,
            &#123;<span class="hljs-attr">id</span>:<span class="hljs-string">"02"</span>, <span class="hljs-attr">title</span>: <span class="hljs-string">"消息2"</span>&#125;,
            &#123;<span class="hljs-attr">id</span>:<span class="hljs-string">"03"</span>, <span class="hljs-attr">title</span>: <span class="hljs-string">"消息3"</span>&#125;,
        ]
    &#125;
    <span class="hljs-comment">// 编程式路由导航</span>
    pushShow = <span class="hljs-function">(<span class="hljs-params">id, title</span>)=></span>&#123;
        <span class="hljs-comment">// push跳转 + 携带 params参数</span>
        <span class="hljs-built_in">this</span>.props.history.push(<span class="hljs-string">`/home/message/detail/<span class="hljs-subst">$&#123;id&#125;</span>/<span class="hljs-subst">$&#123;title&#125;</span>`</span>);
        
        <span class="hljs-comment">// push跳转 + 携带 search参数</span>
        <span class="hljs-comment">// this.props.history.push(`/home/message/detail?id=$&#123;id&#125;&title=$&#123;title&#125;`);</span>
        
        <span class="hljs-comment">// push跳转 + 携带 state参数</span>
        <span class="hljs-comment">// this.props.history.push(`/home/message/detail`, &#123;id,title&#125;);</span>
    &#125;
    replaceShow = <span class="hljs-function">(<span class="hljs-params">id, title</span>)=></span>&#123;
        <span class="hljs-comment">// replace跳转 + 携带 params参数</span>
        <span class="hljs-built_in">this</span>.props.history.replace(<span class="hljs-string">`/home/message/detail/<span class="hljs-subst">$&#123;id&#125;</span>/<span class="hljs-subst">$&#123;title&#125;</span>`</span>);
        
        <span class="hljs-comment">// replace跳转 + 携带 search参数</span>
        <span class="hljs-comment">// this.props.history.replace(`/home/message/detail?id=$&#123;id&#125;&title=$&#123;title&#125;`);</span>
        
        <span class="hljs-comment">// replace跳转 + 携带 state参数</span>
        <span class="hljs-comment">// this.props.history.replace(`/home/message/detail`, &#123;id, title&#125;);</span>
    &#125;
    <span class="hljs-comment">// 后退</span>
    goBack = <span class="hljs-function">()=></span>&#123;
        <span class="hljs-built_in">this</span>.props.history.goBack();
    &#125;
    <span class="hljs-comment">// 前进</span>
    goForward = <span class="hljs-function">()=></span>&#123;
        <span class="hljs-built_in">this</span>.props.history.goForward();
    &#125;
    <span class="hljs-comment">// 跳转指定位置</span>
    go = <span class="hljs-function">()=></span>&#123;
        <span class="hljs-comment">// 向前两步</span>
        <span class="hljs-built_in">this</span>.props.history.go(<span class="hljs-number">2</span>);
        
        <span class="hljs-comment">// 后退两步</span>
        <span class="hljs-built_in">this</span>.props.history.go(-<span class="hljs-number">2</span>);
    &#125;
    <span class="hljs-function"><span class="hljs-title">render</span>(<span class="hljs-params"></span>)</span> &#123;
        <span class="hljs-keyword">const</span> &#123;messageArr&#125; = <span class="hljs-built_in">this</span>.state;
        <span class="hljs-keyword">return</span> (
            <span class="xml"><span class="hljs-tag"><<span class="hljs-name">div</span>></span>
                <span class="hljs-tag"><<span class="hljs-name">ul</span>></span>
                    &#123;
                        messageArr.map(item=>&#123;
                            return (
                            <span class="hljs-tag"><<span class="hljs-name">li</span> <span class="hljs-attr">key</span>=<span class="hljs-string">&#123;item.id&#125;</span>></span>
                                <span class="hljs-tag"><<span class="hljs-name">Link</span> <span class="hljs-attr">to</span>=<span class="hljs-string">&#123;</span>`/<span class="hljs-attr">home</span>/<span class="hljs-attr">message</span>/<span class="hljs-attr">detail</span>/$&#123;<span class="hljs-attr">item.id</span>&#125;/$&#123;<span class="hljs-attr">item.title</span>&#125;`&#125;></span>&#123;item.title&#125;<span class="hljs-tag"></<span class="hljs-name">Link</span>></span>
                                <span class="hljs-symbol">&nbsp;</span><span class="hljs-tag"><<span class="hljs-name">button</span> <span class="hljs-attr">onClick</span>=<span class="hljs-string">&#123;()</span> =></span> this.pushShow(item.id, item.title)&#125;>push查看<span class="hljs-tag"></<span class="hljs-name">button</span>></span>
                                <span class="hljs-symbol">&nbsp;</span><span class="hljs-tag"><<span class="hljs-name">button</span> <span class="hljs-attr">onClick</span>=<span class="hljs-string">&#123;()</span> =></span> this.replaceShow(item.id, item.title)&#125;>replace查看<span class="hljs-tag"></<span class="hljs-name">button</span>></span>
                            <span class="hljs-tag"></<span class="hljs-name">li</span>></span>
                            )
                        &#125;)
                    &#125;
                <span class="hljs-tag"></<span class="hljs-name">ul</span>></span>
                <span class="hljs-tag"><<span class="hljs-name">hr</span>/></span>
                <span class="hljs-tag"><<span class="hljs-name">Route</span> <span class="hljs-attr">path</span>=<span class="hljs-string">"/home/message/detail/:id/:title"</span> <span class="hljs-attr">component</span>=<span class="hljs-string">&#123;Detail&#125;</span> /></span>
                <span class="hljs-tag"><<span class="hljs-name">button</span> <span class="hljs-attr">onClick</span>=<span class="hljs-string">&#123;this.goBack&#125;</span>></span>goBack<span class="hljs-tag"></<span class="hljs-name">button</span>></span>
                <span class="hljs-symbol">&nbsp;</span>
                <span class="hljs-tag"><<span class="hljs-name">button</span> <span class="hljs-attr">onClick</span>=<span class="hljs-string">&#123;this.goForward&#125;</span>></span>goForward<span class="hljs-tag"></<span class="hljs-name">button</span>></span>
                <span class="hljs-symbol">&nbsp;</span>
                <span class="hljs-tag"><<span class="hljs-name">button</span> <span class="hljs-attr">onClick</span>=<span class="hljs-string">&#123;this.go&#125;</span>></span>go<span class="hljs-tag"></<span class="hljs-name">button</span>></span>
            <span class="hljs-tag"></<span class="hljs-name">div</span>></span></span>
        )
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>总结一下上面的代码：</p>
<ol>
<li>编程式路由都是通过 <code>props</code>中的 <code>history</code>对象进行操作（都是该对象身上的方法，调用方式为：<code>this.props.history.xxx</code>）</li>
<li>常用方法：
<ul>
<li>
<p><code>push(route[, state])</code>: 跳转到指定路由（带有历史记录）</p>
</li>
<li>
<p><code>replace(route[, state])</code>: 跳转到指定路由（不带有历史记录）</p>
</li>
<li>
<p><code>goBack()</code>: 后退一个</p>
</li>
<li>
<p><code>goForward()</code>: 前进一个</p>
</li>
<li>
<p><code>go(num)</code>: 前往指定步数，当 <code>num</code>为正数时，为前进，当 <code>num</code>为负数时则为后退。</p>
</li>
</ul>
</li>
</ol>
<h3 data-id="heading-64">5. withRouter 组件</h3>
<p>有的时候，我们想要在其他组件中也使用路由组件的功能，比如导航栏，应该属于公用组件，但是里面的导航链接的功能却是路由组件的功能，我们应该怎么解决呢？<br>
在 <code>react-router</code> 中，提供了这么一种方法，可以让一般组件具有路由组件的功能，则就是 <code>withRouter()</code> 方法。<br>
看看演示：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">import</span> &#123;withRouter&#125; <span class="hljs-keyword">from</span> <span class="hljs-string">"react-router-dom"</span>;

<span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Header</span> <span class="hljs-keyword">extends</span> <span class="hljs-title">Component</span> </span>&#123;
    <span class="hljs-comment">// withRouter后该组件也有了路由组件的功能</span>
    goBack = <span class="hljs-function">()=></span>&#123;
        <span class="hljs-built_in">this</span>.props.history.goBack();
    &#125;
    go = <span class="hljs-function">()=></span>&#123;
        <span class="hljs-built_in">this</span>.props.history.go(<span class="hljs-number">2</span>);
    &#125;
    goForward = <span class="hljs-function">()=></span>&#123;
        <span class="hljs-built_in">this</span>.props.history.goForward();
    &#125;
    <span class="hljs-function"><span class="hljs-title">render</span>(<span class="hljs-params"></span>)</span> &#123;
        <span class="hljs-keyword">return</span> (
            <span class="xml"><span class="hljs-tag"><<span class="hljs-name">div</span>></span>
                <span class="hljs-tag"><<span class="hljs-name">h1</span>></span>This is a React-router-dom Test!<span class="hljs-tag"></<span class="hljs-name">h1</span>></span>
                <span class="hljs-tag"><<span class="hljs-name">button</span> <span class="hljs-attr">onClick</span>=<span class="hljs-string">&#123;this.goBack&#125;</span>></span>goBack<span class="hljs-tag"></<span class="hljs-name">button</span>></span>
                <span class="hljs-symbol">&nbsp;</span>
                <span class="hljs-tag"><<span class="hljs-name">button</span> <span class="hljs-attr">onClick</span>=<span class="hljs-string">&#123;this.goForward&#125;</span>></span>goForward<span class="hljs-tag"></<span class="hljs-name">button</span>></span>
                <span class="hljs-symbol">&nbsp;</span>
                <span class="hljs-tag"><<span class="hljs-name">button</span> <span class="hljs-attr">onClick</span>=<span class="hljs-string">&#123;this.go&#125;</span>></span>go<span class="hljs-tag"></<span class="hljs-name">button</span>></span>
            <span class="hljs-tag"></<span class="hljs-name">div</span>></span></span>
        )
    &#125;
&#125;

<span class="hljs-comment">// withRouter 用于给一般组件添加上路由组件特有的功能，返回一个新组件</span>
<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> withRouter(Header);
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-65">九、路由组件之间的参数传递</h2>
<p>父子组件之间的内容传递，可以通过 <code>props</code>来进行参数传递，但是路由组件却没有自己的标签，那么该如何进行参数的传递呢？<br>
还记得路由组件特有的 <code>props</code>吗，我们可以利用 <code>History API</code>的一些特性来进行路由组件之间的参数传递，有三种方法。</p>
<ul>
<li><code>params</code></li>
<li><code>search</code></li>
<li><code>state</code></li>
</ul>
<h3 data-id="heading-66">1. 传递 params 参数</h3>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">// 父组件</span>
<span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Parent</span> <span class="hljs-keyword">extends</span> <span class="hljs-title">Component</span> </span>&#123;
    state = &#123;
        <span class="hljs-attr">messageArr</span>:[
            &#123;<span class="hljs-attr">id</span>:<span class="hljs-string">"01"</span>, <span class="hljs-attr">title</span>: <span class="hljs-string">"消息1"</span>&#125;,
            &#123;<span class="hljs-attr">id</span>:<span class="hljs-string">"02"</span>, <span class="hljs-attr">title</span>: <span class="hljs-string">"消息2"</span>&#125;,
            &#123;<span class="hljs-attr">id</span>:<span class="hljs-string">"03"</span>, <span class="hljs-attr">title</span>: <span class="hljs-string">"消息3"</span>&#125;,
        ]
    &#125;
    <span class="hljs-function"><span class="hljs-title">render</span>(<span class="hljs-params"></span>)</span> &#123;
        <span class="hljs-keyword">const</span> &#123;messageArr&#125; = <span class="hljs-built_in">this</span>.state;
        <span class="hljs-keyword">return</span> (
            <span class="xml"><span class="hljs-tag"><<span class="hljs-name">div</span>></span>
                <span class="hljs-tag"><<span class="hljs-name">ul</span>></span>&#123;
                 messageArr.map(item=>&#123;
                    // 向路由组件传递 params参数
                    return <span class="hljs-tag"><<span class="hljs-name">li</span> <span class="hljs-attr">key</span>=<span class="hljs-string">&#123;item.id&#125;</span>></span><span class="hljs-tag"><<span class="hljs-name">Link</span> <span class="hljs-attr">to</span>=<span class="hljs-string">&#123;</span>`/<span class="hljs-attr">home</span>/<span class="hljs-attr">message</span>/<span class="hljs-attr">detail</span>/$&#123;<span class="hljs-attr">item.id</span>&#125;/$&#123;<span class="hljs-attr">item.title</span>&#125;`&#125;></span>&#123;item.title&#125;<span class="hljs-tag"></<span class="hljs-name">Link</span>></span><span class="hljs-tag"></<span class="hljs-name">li</span>></span>
                    &#125;)
                &#125;<span class="hljs-tag"></<span class="hljs-name">ul</span>></span>
                <span class="hljs-tag"><<span class="hljs-name">hr</span>/></span>
                &#123;/* 声明接受 params参数，可以在 props中的 match属性的 params属性里获得 */&#125;
                <span class="hljs-tag"><<span class="hljs-name">Route</span> <span class="hljs-attr">path</span>=<span class="hljs-string">"/home/message/detail/:id/:title"</span> <span class="hljs-attr">component</span>=<span class="hljs-string">&#123;Child&#125;</span> /></span>
            <span class="hljs-tag"></<span class="hljs-name">div</span>></span></span>
        )
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">// 子组件</span>
<span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Child</span> <span class="hljs-keyword">extends</span> <span class="hljs-title">Component</span> </span>&#123;
    state = &#123;
        <span class="hljs-attr">contentArr</span>:[
            &#123;<span class="hljs-attr">id</span>:<span class="hljs-string">"01"</span>, <span class="hljs-attr">content</span>: <span class="hljs-string">"你好中国"</span>&#125;,
            &#123;<span class="hljs-attr">id</span>:<span class="hljs-string">"02"</span>, <span class="hljs-attr">content</span>: <span class="hljs-string">"你好世界"</span>&#125;,
            &#123;<span class="hljs-attr">id</span>:<span class="hljs-string">"03"</span>, <span class="hljs-attr">content</span>: <span class="hljs-string">"你好帅哥"</span>&#125;,
        ]
    &#125;
    <span class="hljs-function"><span class="hljs-title">render</span>(<span class="hljs-params"></span>)</span> &#123;
        <span class="hljs-built_in">console</span>.log(<span class="hljs-built_in">this</span>.props);
        <span class="hljs-comment">// 获取 params参数</span>
        <span class="hljs-keyword">const</span> &#123;id, title&#125; = <span class="hljs-built_in">this</span>.props.match.params
        <span class="hljs-keyword">const</span> findResult = <span class="hljs-built_in">this</span>.state.contentArr.find(<span class="hljs-function"><span class="hljs-params">obj</span>=></span>obj.id == id).content;
        <span class="hljs-keyword">return</span> (
            <span class="xml"><span class="hljs-tag"><<span class="hljs-name">div</span>></span>
                <span class="hljs-tag"><<span class="hljs-name">ul</span>></span>
                    <span class="hljs-tag"><<span class="hljs-name">li</span>></span>ID: &#123;id&#125;<span class="hljs-tag"></<span class="hljs-name">li</span>></span>
                    <span class="hljs-tag"><<span class="hljs-name">li</span>></span>TITLE: &#123;title&#125;<span class="hljs-tag"></<span class="hljs-name">li</span>></span>
                    <span class="hljs-tag"><<span class="hljs-name">li</span>></span>CONTENT: &#123;findResult&#125;<span class="hljs-tag"></<span class="hljs-name">li</span>></span>
                <span class="hljs-tag"></<span class="hljs-name">ul</span>></span>
            <span class="hljs-tag"></<span class="hljs-name">div</span>></span></span>
        )
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>在使用 <code>params</code>传递参数时，你会清楚的看到参数以路由的形式展现了出来，例如：</p>
<ul>
<li><code>http://localhost:3000/home/message/用户1/文章32</code></li>
</ul>
<p>类式上面的<strong>用户1</strong>和<strong>文章32</strong>，这就是传递的参数。<br>
以<code>params</code>方式传递的参数，在路由中需要声明接受才可以使用。</p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">Route</span> <span class="hljs-attr">path</span>=<span class="hljs-string">"/home/message/detail/:id/:title"</span> <span class="hljs-attr">component</span>=<span class="hljs-string">&#123;Child&#125;</span> /></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>后面的 <code>:id</code> 与 <code>:title</code> 就是可变路由，可以通过<code>props</code>的<code>match</code>接受接收这里的内容.</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">const</span> &#123;id, title&#125; = <span class="hljs-built_in">this</span>.props.match.params
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-67">2. 传递 search 参数</h3>
<p>这个就是依赖 <code>get</code>的请求方式。</p>
<ul>
<li><code>http://localhost/home/message?id=1&title=abc</code></li>
</ul>
<p>即 <code>javascript</code> 可以获取到 <code>url</code> 中 <strong>?</strong> 后面的请求体。
所以我们可以吧上面的 <code>map</code> 中返回的标签修改以下</p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">li</span> <span class="hljs-attr">key</span>=<span class="hljs-string">&#123;item.id&#125;</span>></span><span class="hljs-tag"><<span class="hljs-name">Link</span> <span class="hljs-attr">to</span>=<span class="hljs-string">&#123;</span>`/<span class="hljs-attr">home</span>/<span class="hljs-attr">message</span>/<span class="hljs-attr">detail</span>?<span class="hljs-attr">id</span>=<span class="hljs-string">$&#123;item.id&#125;&title</span>=<span class="hljs-string">$&#123;item.title&#125;</span>`&#125;></span>&#123;item.title&#125;<span class="hljs-tag"></<span class="hljs-name">Link</span>></span><span class="hljs-tag"></<span class="hljs-name">li</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>且这种方式不需要在路由中声明接收。<br>
通过 <code>props</code> 中的 <code>location</code> 进行接收</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">const</span> search = <span class="hljs-built_in">this</span>.props.location.search;
<span class="hljs-comment">// 获取到的格式时： ?id=xxx&title=xxx 所以还需要加工一下</span>
<span class="hljs-keyword">const</span> &#123;id, title&#125; = qs.parse(search.slice(<span class="hljs-number">1</span>));
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-68">3. 传递 state 参数</h3>
<p>通过 <code>HistoryAPI</code>来进行数据传输：</p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">li</span> <span class="hljs-attr">key</span>=<span class="hljs-string">&#123;item.id&#125;</span>></span><span class="hljs-tag"><<span class="hljs-name">Link</span> <span class="hljs-attr">to</span>=<span class="hljs-string">&#123;&#123;pathname:</span> `/<span class="hljs-attr">home</span>/<span class="hljs-attr">message</span>/<span class="hljs-attr">detail</span>`, <span class="hljs-attr">state:</span>&#123;<span class="hljs-attr">id:item.id</span>, <span class="hljs-attr">title:item.title</span>&#125;&#125;&#125;></span>&#123;item.title&#125;<span class="hljs-tag"></<span class="hljs-name">Link</span>></span><span class="hljs-tag"></<span class="hljs-name">li</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>不需要在路由链接中添加任何东西，也不需要路由进行声明接收。更加的美观。<br>
在 <code>props</code>中的 <code>location</code> 里获取 <code>state</code>属性</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">const</span> &#123;id, title&#125; = <span class="hljs-built_in">this</span>.props.location.state;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-69">4. 三者对比</h3>
<p>路由组件传参其实用的较少，因为他们都有对某些东西的依赖：</p>
<ul>
<li><code>params</code>: 依赖于路由链接，链接不美观</li>
<li><code>search</code>: 依赖于路由链接，链接不美观</li>
<li><code>state</code>: 依赖于历史记录 (<code>HistoryAPI</code>)，链接美观，但是当直接输入链接时则会报错（没有历史记录）</li>
</ul>
<p>所以尽量使用其他的传参方式，如果非要使用的话，有限度比较为：</p>
<ol>
<li><code>params</code> (最为常用)</li>
<li><code>search</code> (较为常用)</li>
<li><code>state</code> (比较少用)</li>
</ol>
<h2 data-id="heading-70">十、redux 的使用</h2>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/ea94394679ea4e35b31b9ec6fc983297~tplv-k3u1fbpfcp-watermark.image" alt="614_1.png" loading="lazy" referrerpolicy="no-referrer"></p>
<blockquote>
<p>假设我们的组件如同这张图一般，组件之间相互嵌套着。<br>
这时候提出一个要求，在<strong>组件E</strong>中的数据，要给<strong>组件A</strong>和<strong>组件F</strong>使用，要怎么处理呢？</p>
</blockquote>
<ul>
<li>方法1：通过不断的 <code>props</code>进行传参，但是这非常的费时费力</li>
<li>方法2：使用 <code>Pubsub.js</code>等进行消息发布/订阅功能</li>
<li>方法3：使用 <code>react-redux</code>进行数据集中式管理</li>
</ul>
<p>即 <code>redux</code>可以看作一个管家，负责帮忙存储公共的数据。</p>
<h3 data-id="heading-71">1. 安装 redux</h3>
<pre><code class="hljs language-node copyable" lang="node">npm i redux -S
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-72">2. 核心概念</h3>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/7d046fcb589740f98ee51387b7cffbbc~tplv-k3u1fbpfcp-watermark.image" alt="616_1.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p><code>redux</code> 有着三个核心概念</p>
<ol>
<li><code>action</code>:
<ul>
<li>动作的对象（操作内容）</li>
<li>包含两个属性：
a. <code>type</code>: 表示属性，值为<strong>字符串</strong>，唯一，必要属性（要干嘛）
b. <code>data</code>: 数据属性，值为<strong>任意类型</strong>，可选属性（怎么干）</li>
<li>例如：<code>&#123; type: "ADD_STUDENT", data: &#123; name: "tom", age: 18 &#125; &#125;</code></li>
</ul>
</li>
<li><code>reducer</code>:
<ul>
<li>用于初始化状态和加工状态（对数据进行初始化和操作数据的）</li>
<li>加工时，根据旧的 <code>state</code>和 <code>action</code>，产生新的 <code>state</code>的纯函数</li>
<li>有两个参数，一个为之前的状态（<code>prevstate</code>）与动作对象（<code>action</code>）</li>
</ul>
</li>
<li><code>store</code>:
<ul>
<li>将 <code>state</code>、<code>action</code>、<code>reducer</code>联系在一起的对象（大脑）</li>
</ul>
</li>
</ol>
<blockquote>
<p>我们大致可以把 <code>redux</code>的想象成一家<strong>餐厅</strong>，而我们就是<strong>顾客</strong>( <code>component</code>)，我们通过叫<strong>服务员</strong>( <code>action</code>)进行点餐等操作，服务员转达<strong>经理</strong>( <code>store</code>)后，经理吩咐<strong>后厨</strong>( <code>reducer</code>)进行做菜，然后把菜做好后由经理传递给顾客</p>
</blockquote>
<h3 data-id="heading-73">3. 基本使用</h3>
<h4 data-id="heading-74">(1) 创建文件夹</h4>
<p>在 <code>src</code>文件夹中创建 <code>redux</code>文件夹，用于存放 <code>redux</code>的相关内容</p>
<ul>
<li><strong>Compnoent</strong> ------ 存放组件相关的文件夹</li>
<li><strong>redux</strong> ------ 存放 <code>redux</code>相关内容的文件夹
<ul>
<li><strong>actions</strong> ------ 存放 <code>action</code>相关内容的文件夹</li>
<li><strong>reducers</strong> ------ 存放 <code>reducer</code>相关内容的文件夹</li>
<li><code>constant.js</code> ------ 存放规范命名的文件</li>
<li><code>store.js</code> ------ 编写 <code>store</code>的文件</li>
</ul>
</li>
</ul>
<p>由我来一个个带你们解析。先写一个最简单的 <code>redux</code></p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">/**
 * store.js
 * 该文件专门用于暴漏一个 store对象，整个应用只有一个 store对象
 */</span>
<span class="hljs-comment">// 引入 createStore，专门用于创建 redux中最为核心的 store</span>
<span class="hljs-keyword">import</span> &#123;createStore&#125; <span class="hljs-keyword">from</span> <span class="hljs-string">"redux"</span>;
<span class="hljs-comment">// 引入为 Count组件服务的 reducer</span>
<span class="hljs-keyword">import</span> countReducer <span class="hljs-keyword">from</span> <span class="hljs-string">"./count_reducer"</span>;
<span class="hljs-keyword">const</span> store = createStore(countReducer)
<span class="hljs-comment">// 暴露 store对象</span>
<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> store;
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">/**
 * / reducer / count.js
 * 1. 该文件是用于创建一个为 Count组件服务的 reducer，reducer的本质就是一个函数
 * 
 * 2. reducer函数会收到两个参数，分别为：之前的状态（preState），动作对象（action）
 * 
 * 3. 会自动调用一次 reducer(初始化)
 */</span>
<span class="hljs-comment">// 初始化的状态</span>
<span class="hljs-keyword">const</span> initState = <span class="hljs-number">0</span>;
<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">countReducer</span>(<span class="hljs-params">preState = initState, action</span>)</span>&#123;
    <span class="hljs-keyword">if</span>(preState === <span class="hljs-literal">undefined</span>) preState = <span class="hljs-number">0</span>; 
    <span class="hljs-comment">// 从 action对象中获取 type，data</span>
    <span class="hljs-keyword">const</span> &#123;type, data&#125; = action;
    <span class="hljs-comment">// 根据 type觉得如何加工数据</span>
    <span class="hljs-keyword">switch</span> (type) &#123;
        <span class="hljs-keyword">case</span> <span class="hljs-string">'increment'</span>: <span class="hljs-comment">// data</span>
            <span class="hljs-keyword">return</span> preState + data;
        <span class="hljs-keyword">case</span> <span class="hljs-string">'decrement'</span>: <span class="hljs-comment">// 如果是减</span>
            <span class="hljs-keyword">return</span> preState - data;
        <span class="hljs-keyword">default</span>:
            <span class="hljs-keyword">return</span> preState;
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">// / Component / Count.js </span>
<span class="hljs-keyword">import</span> React, &#123; Component &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'react'</span>
<span class="hljs-comment">// 引入store</span>
<span class="hljs-keyword">import</span> store <span class="hljs-keyword">from</span> <span class="hljs-string">"../../redux/store"</span>;
<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> <span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Count</span> <span class="hljs-keyword">extends</span> <span class="hljs-title">Component</span> </span>&#123;
    <span class="hljs-comment">// 加法</span>
    increment = <span class="hljs-function">()=></span>&#123;
        <span class="hljs-keyword">const</span> &#123;value&#125; = <span class="hljs-built_in">this</span>.selectNumber;
        <span class="hljs-comment">// 发送动作对象给 store</span>
        store.dispatch(&#123;
            <span class="hljs-attr">type</span>: <span class="hljs-string">"increment"</span>,
            <span class="hljs-attr">data</span>: value*<span class="hljs-number">1</span>
        &#125;)
    &#125;
    <span class="hljs-function"><span class="hljs-title">render</span>(<span class="hljs-params"></span>)</span> &#123;
        <span class="hljs-keyword">return</span> (
            <span class="xml"><span class="hljs-tag"><<span class="hljs-name">div</span>></span>
                <span class="hljs-tag"><<span class="hljs-name">h1</span>></span>当前求和为：&#123;store.getState()&#125;<span class="hljs-tag"></<span class="hljs-name">h1</span>></span>
                <span class="hljs-tag"><<span class="hljs-name">select</span> <span class="hljs-attr">ref</span>=<span class="hljs-string">&#123;c</span>=></span>this.selectNumber = c&#125;>
                    <span class="hljs-tag"><<span class="hljs-name">option</span> <span class="hljs-attr">value</span>=<span class="hljs-string">"1"</span>></span>1<span class="hljs-tag"></<span class="hljs-name">option</span>></span>
                    <span class="hljs-tag"><<span class="hljs-name">option</span> <span class="hljs-attr">value</span>=<span class="hljs-string">"2"</span>></span>2<span class="hljs-tag"></<span class="hljs-name">option</span>></span>
                    <span class="hljs-tag"><<span class="hljs-name">option</span> <span class="hljs-attr">value</span>=<span class="hljs-string">"3"</span>></span>3<span class="hljs-tag"></<span class="hljs-name">option</span>></span>
                <span class="hljs-tag"></<span class="hljs-name">select</span>></span>
                <span class="hljs-tag"><<span class="hljs-name">button</span> <span class="hljs-attr">onClick</span>=<span class="hljs-string">&#123;this.increment&#125;</span>></span>+<span class="hljs-tag"></<span class="hljs-name">button</span>></span>
            <span class="hljs-tag"></<span class="hljs-name">div</span>></span></span>
        )
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>以上就是最精简的 <code>redux</code>，让我们分析一下流程：</p>
<ol>
<li>编写 <code>Count</code>组件，创建 <code>Count</code>组件对应的 <code>Reducer</code>文件</li>
<li>编写 <code>Reducer</code>的代码并抛出：:
<ul>
<li><code>Reducer</code>是个纯函数</li>
<li>通常使用 <code>Switch</code>进行 <code>action</code>中的 <code>type</code>的判断</li>
<li>函数返回值为修改后的值</li>
</ul>
</li>
<li>创建 <code>store</code>并编写代码：
<ul>
<li>使用方法 <code>createStore()</code>方法来创建一个 <code>store</code>，参数是一个 <code>reducer</code></li>
<li>把编写好的 <code>Count</code>组件的 <code>reducer</code>导入</li>
</ul>
</li>
<li>在组件中引入 <code>store</code>并进行调用：
<ul>
<li>在方法中通过使用 <code>dspatch()</code>方法向 <code>store</code>传递 <code>action</code></li>
<li><code>dispatch</code>的参数时一个对象（即 <code>action</code>动作对象）</li>
</ul>
</li>
</ol>
<h4 data-id="heading-75">(2) 使用流程</h4>
<p>以上使创建的大致流程，而使用的大致流程是这样的：</p>
<blockquote>
<ol>
<li><code>store</code> 初始化时自动调用了一次 <code>reducer</code>进行了值的初始化</li>
<li>组件发出动 <code>action</code> 给 <code>store</code>，<code>store</code>进行判断后分发给对应的 <code>reducer</code></li>
<li><code>reducer</code>根据 <code>action</code>里的 <code>type</code>对数据进行相应的处理后返回新的值</li>
<li><code>store</code>接收返回的新的值，并将旧的值替换掉</li>
<li>通过方法 <code>store.getState()</code> 获取当前 <code>store</code>身上的值</li>
</ol>
</blockquote>
<h4 data-id="heading-76">(3) 使用异步redux</h4>
<p>如果我们需要使用异步的 <code>redux</code>的话，还需要借助另一款插件： <code>redux-thunk</code></p>
<pre><code class="hljs language-node copyable" lang="node">npm i redux-thunk -S
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这是一个<strong>中间件</strong>，用于帮忙处理异步的 <code>redux</code>，<br>
异步的 <code>action</code>的值为一个函数
在函数中进行普通的 <code>dispatch()</code> 操作</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">export</span> <span class="hljs-keyword">const</span> createIncrementAsyncAction = <span class="hljs-function">(<span class="hljs-params">data, time=<span class="hljs-number">500</span></span>)=></span>&#123;
    <span class="hljs-comment">// 返回一个 action</span>
    <span class="hljs-keyword">return</span> <span class="hljs-function">()=></span>&#123;
        <span class="hljs-built_in">setTimeout</span>(<span class="hljs-function">()=></span>&#123;
            store.dispatch(createIncrementAction(data));
        &#125;, time);
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>同时我们要在 <code>store</code>处设置让他<strong>支持执行中间件</strong>，通过 <code>redux</code>的 <code>applyMiddleware()</code> 方法就可以加载中间件，他的参数就是中间件，然后 <code>applyMiddleware()</code> 将作为 <code>createStore()</code> 的第二个参数引入。</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">// store.js</span>
<span class="hljs-comment">// 引入 applyMiddleware，专门用于执行中间件</span>
<span class="hljs-keyword">import</span> &#123;createStore, applyMiddleware&#125; <span class="hljs-keyword">from</span> <span class="hljs-string">"redux"</span>;
<span class="hljs-comment">// 引入为 Count组件服务的 reducer</span>
<span class="hljs-keyword">import</span> countReducer <span class="hljs-keyword">from</span> <span class="hljs-string">"./count_reducer"</span>;
<span class="hljs-comment">// 引入 redux-thunk，用于支持异步 action</span>
<span class="hljs-keyword">import</span> thunk <span class="hljs-keyword">from</span> <span class="hljs-string">"redux-thunk"</span>;
<span class="hljs-comment">// 暴露 store对象</span>
<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> createStore(countReducer, applyMiddleware(thunk));
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-77">(4) 监听状态变化</h4>
<p>你写着写着有没有发现，虽然 <code>redux</code>里面的状态确实更新了，但是页面并没有变化啊？<br>
还记得页面渲染使用的是哪个函数吗？<code>render()</code>函数。可是在 <code>redux</code>状态发生变化时，并不会帮助我们调用 <code>render()</code>函数，所以我们需要手动实现实时渲染页面。<br>
在这里我们使用到了 <code>redux</code>的 <code>store</code>上的 <code>subscribe()</code> 方法，用于监听 <code>redux</code>上状态的变化，参数是一个函数，便于我们进行操作。<br>
一般我们都写在根标签上（精简些，不用再每个使用 <code>redux</code>的组件中都写一遍）</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">import</span> React <span class="hljs-keyword">from</span> <span class="hljs-string">'react'</span>;
<span class="hljs-keyword">import</span> ReactDOM <span class="hljs-keyword">from</span> <span class="hljs-string">'react-dom'</span>;
<span class="hljs-keyword">import</span> <span class="hljs-string">'./index.css'</span>;
<span class="hljs-keyword">import</span> App <span class="hljs-keyword">from</span> <span class="hljs-string">'./App'</span>;
<span class="hljs-keyword">import</span> store <span class="hljs-keyword">from</span> <span class="hljs-string">"./redux/store"</span>
ReactDOM.render(
    <span class="xml"><span class="hljs-tag"><<span class="hljs-name">App</span> /></span></span>,
  <span class="hljs-built_in">document</span>.getElementById(<span class="hljs-string">'root'</span>)
);
<span class="hljs-comment">// 精简写法</span>
store.subscribe(<span class="hljs-function">()=></span>&#123;
  ReactDOM.render(
      <span class="xml"><span class="hljs-tag"><<span class="hljs-name">App</span> /></span></span>,
    <span class="hljs-built_in">document</span>.getElementById(<span class="hljs-string">'root'</span>)
  );
&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-78">4. 注意事项</h3>
<ol>
<li>一般使用到 <code>redux</code>的话，需要使用的组件肯定不止一个，所以创建 <strong>actions</strong>和<strong>reducers</strong>用来存储多个 <code>action</code> 和 <code>reducer</code></li>
<li>同上，<code>store</code>肯定不止加载一个 <code>reducer</code>，所以我们使用 <code>redux</code>的 <code>combineReducers()</code>方法来整合所有的 <code>reducer</code>
<ul>
<li><code>combineReducers()</code>方法的参数是一个对象，里面存放着所有的 <code>reducer</code></li>
</ul>
</li>
</ol>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">import</span> &#123;createStore, applyMiddleware, combineReducers&#125; <span class="hljs-keyword">from</span> <span class="hljs-string">"redux"</span>;
<span class="hljs-keyword">import</span> countReducer <span class="hljs-keyword">from</span> <span class="hljs-string">"./reducers/count"</span>;
<span class="hljs-keyword">import</span> personReducer <span class="hljs-keyword">from</span> <span class="hljs-string">"./reducers/person"</span>;
<span class="hljs-keyword">import</span> thunk <span class="hljs-keyword">from</span> <span class="hljs-string">"redux-thunk"</span>;
<span class="hljs-comment">// 汇总所有的 reducer</span>
<span class="hljs-keyword">const</span> allReducer = combineReducers(&#123;
    <span class="hljs-attr">count</span>: countReducer,
    <span class="hljs-attr">persons</span>: personReducer,
&#125;);
<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> createStore(allReducer, applyMiddleware(thunk));


<span class="copy-code-btn">复制代码</span></code></pre>
<ol start="3">
<li>因为 <code>redux</code>在设计上还有许多的问题，例如：
<ul>
<li>单个组件需要做：与 <code>store</code>打交道，获取数据，监听数据变化，派发 <code>action</code>对象等，一个组件负责的事情太多了。</li>
<li>需要另外监听 <code>redux</code>的状态变化来更新状态并渲染页面。</li>
<li>所以有人对 <code>redux</code>进行了优化，推出了另一个库 <code>react-redux</code>（放心，没啥不同，就是多了点优化，后面会讲）</li>
</ul>
</li>
<li><strong>能不使用 <code>redux</code>，就不要使用 <code>redux</code>（不管是 <code>redux</code> 还是 <code>react-redux</code>）</strong></li>
<li><strong>能不使用 <code>redux</code>，就不要使用 <code>redux</code>（不管是 <code>redux</code> 还是 <code>react-redux</code>）</strong></li>
<li><strong>能不使用 <code>redux</code>，就不要使用 <code>redux</code>（不管是 <code>redux</code> 还是 <code>react-redux</code>）</strong></li>
</ol>
<h2 data-id="heading-79">十一、了解与使用 <code>react-redux</code></h2>
<p>前面也说了，<code>react-redux</code> 其实就是 <code>redux</code>的升级版，对许多地方进行了优化，但在学习他之前，需要我们进行一些对 <code>redux</code>的优化知识。</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/03bdf7830cfa405d8ba86900b49f606b~tplv-k3u1fbpfcp-watermark.image" alt="620_1.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-80">1. 使用容器组件和UI组件</h3>
<p>其目的就是为了把组件身上太多的活进行拆分，分为<strong>UI组件（内组件）<strong>和</strong>容器组件（外组件）</strong>，两个组件之间使用 <code>props</code>进行通信，对 <code>store</code>那边的请求状态，更改状态的活交给容器组件来干，而通过状态来编写页面，更新渲染等活，就交给 UI组件来干。</p>
<p>了解了这个后，就可以开始使用 <code>react-redux</code>了</p>
<h3 data-id="heading-81">2. 安装 react-redux</h3>
<pre><code class="hljs language-node copyable" lang="node">npm i react-redux -S
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这个就不多说了。</p>
<h3 data-id="heading-82">3. 创建文件夹</h3>
<p>对于容器组件，我们都是使用 <strong>containers</strong>文件夹进行存储。</p>
<ul>
<li><strong>containers</strong> ------ 用于存储容器组件的文件夹</li>
<li><strong>redux</strong> ------ 用于存储 <code>react-redux</code>相关的文件夹</li>
</ul>
<h3 data-id="heading-83">4. 创建容器组件</h3>
<p>容器组件通过 <code>react-redux</code>的 <code>connect()</code> 方法进行创建。</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">// 引入 Count的 UI组件</span>
<span class="hljs-keyword">import</span> Count <span class="hljs-keyword">from</span> <span class="hljs-string">"../../components/Count"</span>;
<span class="hljs-comment">// 引入 connect用于连接 UI组件与 redux</span>
<span class="hljs-keyword">import</span> &#123; connect &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'react-redux'</span>

<span class="hljs-comment">// 该函数的返回值作为状态传递给 UI组件</span>
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">mapStateToProps</span>(<span class="hljs-params">state</span>)</span>&#123;
    <span class="hljs-keyword">return</span> &#123;
        <span class="hljs-attr">count</span>: state,
    &#125;
&#125;
<span class="hljs-comment">// 该函数的返回值作为操作状态的方法传递给 UI组件</span>
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">mapDispatchToProps</span>(<span class="hljs-params">dispatch</span>)</span>&#123;
    <span class="hljs-keyword">return</span> &#123;
        <span class="hljs-attr">add</span>: <span class="hljs-function"><span class="hljs-params">data</span>=></span>&#123;
            <span class="hljs-built_in">console</span>.log(<span class="hljs-number">1234</span>);
        &#125;
    &#125;
&#125;

<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> connect(mapStateToProps, mapDispatchToProps)(Count);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>使用 <code>connect( )( )</code>创建并暴露一个 <code>Count</code>组件的容器组件。<br>
调用 <code>connect</code>时有两个参数，且必须时函数。</p>
<ul>
<li><code>mapStateToProps( state )</code>: 该函数的返回值会作为 <strong>状态</strong> 传递给 UI组件
<ul>
<li><code>state</code>: 参数 <code>state</code> 为 <code>react-redux</code> 默认操作好的 <code>store.getState()</code></li>
</ul>
</li>
<li><code>mapDispatchToProps( dispatch )</code>: 该函数的返回值会作为 <strong>操作状态的方法</strong> 传递给 UI组件，有语法糖写法，传入个对象即可（看下面代码）。
<ul>
<li><code>dispatch</code>: 参数 <code>dispatch</code> 为 <code>react-redux</code> 默认给的 <code>store.dispatch</code> 方法</li>
</ul>
</li>
</ul>
<p>这里只是为了讲解方便，使用时可以使用语法糖的。</p>
<p>注意的几个地方：</p>
<ol>
<li>一般都是把 <strong>UI组件</strong> 与 <strong>容器组件</strong> 写在一个文件中，至于存在哪个文件夹中看公司需求（一般都是 <strong>containers</strong>）</li>
<li>容器组件里的 <code>store</code>不是通过引入使用，而是作为 <code>props</code>传递给容器组件的标签的。<code><Count store=&#123;store&#125; /></code></li>
<li>语法糖写法：</li>
</ol>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">// 引入 Count的 UI组件</span>
<span class="hljs-keyword">import</span> Count <span class="hljs-keyword">from</span> <span class="hljs-string">"../../components/Count"</span>;
<span class="hljs-comment">// 引入 connect用于连接 UI组件与 redux</span>
<span class="hljs-keyword">import</span> &#123; connect &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'react-redux'</span>

<span class="hljs-comment">// 精简写法</span>
<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> connect(
    <span class="hljs-function"><span class="hljs-params">state</span> =></span> (&#123;<span class="hljs-attr">count</span>: state&#125;),
    &#123;
        <span class="hljs-attr">add</span>: <span class="hljs-function"><span class="hljs-params">data</span>=></span> <span class="hljs-built_in">console</span>.log(<span class="hljs-number">1234</span>, data)
    &#125;
)(Count);
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-84">5. Provider 组件</h3>
<p>如果你有许多个容器组件，那么每个容器组件都要传入 <code>store</code>，那么是不是觉得太繁琐了呢？所以 <code>react-redux</code> 提供了 <code>Provider</code>组件用于处理这个问题，只需要在根标签处使用并把 <code>store</code>传递进去，他就可以自动判断哪些组件需要使用 <code>store</code>并自动传递给它。</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">import</span> React <span class="hljs-keyword">from</span> <span class="hljs-string">'react'</span>;
<span class="hljs-keyword">import</span> ReactDOM <span class="hljs-keyword">from</span> <span class="hljs-string">'react-dom'</span>;
<span class="hljs-keyword">import</span> <span class="hljs-string">'./index.css'</span>;
<span class="hljs-keyword">import</span> App <span class="hljs-keyword">from</span> <span class="hljs-string">'./App'</span>;
<span class="hljs-keyword">import</span> store <span class="hljs-keyword">from</span> <span class="hljs-string">"./redux/store"</span>
<span class="hljs-comment">// 优化3: 使用自带的 Provider自动判断哪些组件需要使用 store，从而自动导入</span>
<span class="hljs-keyword">import</span> &#123; Provider &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">"react-redux"</span>;
ReactDOM.render(
  <span class="xml"><span class="hljs-tag"><<span class="hljs-name">Provider</span> <span class="hljs-attr">store</span>=<span class="hljs-string">&#123;store&#125;</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">App</span> /></span>
  <span class="hljs-tag"></<span class="hljs-name">Provider</span>></span></span>,
  <span class="hljs-built_in">document</span>.getElementById(<span class="hljs-string">'root'</span>)
);
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-85">6. 监听状态变化</h3>
<p>有没有发现，我上面的代码已经没有再写 <code>store.subscribe()</code> 监听状态变化了，是因为我们创建容器组件的 <code>connect</code>已经帮我们进行监听了。</p>
<h3 data-id="heading-86">7. 容器组件之间通信</h3>
<p>其实这个很简单，还记的 <code>connect</code>的第一个函数的第一个参数吗？传递给 UI组件的是 <code>props</code>，他的参数是 <code>state</code>，这个 <code>state</code>是 <code>store.getState()</code>。<br>
可是此时你的 <code>store.getState()</code> 不再是一个单纯的值，而是所有 <code>reducer</code>的对象，所以我们可以在里面获取到其他容器组件的值。</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> connect(
    <span class="hljs-function"><span class="hljs-params">state</span> =></span> (&#123;<span class="hljs-attr">count</span>: state.count, <span class="hljs-attr">personLength</span>: state.persons.length&#125;),
    &#123;
        <span class="hljs-attr">increment</span>: createIncrementAction,
        <span class="hljs-attr">decrement</span>: createDecrementAction,
        <span class="hljs-attr">asyncIncrement</span>: createIncrementAsyncAction,
    &#125;
)(Count);
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-87">8. 文件规范</h3>
<p>创建了那么多东西，有的可以整合一下的，让我们来修整修整：</p>
<ul>
<li><strong>containers</strong> ------ 用于存放容器组件的文件夹（UI组件与容器组件写在一起）
<ul>
<li><code>Count.js</code> ------ <code>Count</code> 的容器组件</li>
<li><code>Person.js</code> ------ <code>Person</code> 的容器组件</li>
</ul>
</li>
<li><strong>redux</strong> ------ 用于存放 <code>react-redux</code>相关的文件夹
<ul>
<li>
<p><strong>actions</strong> ------ 用于存放所有 <code>action</code>的文件夹</p>
<ul>
<li><code>count.js</code> ------ 用于存储 <code>Count</code>组件的 <code>action</code></li>
<li><code>person.js</code> ------ 用于存储 <code>Person</code>组件的 <code>action</code></li>
</ul>
</li>
<li>
<p><strong>reducers</strong> ------ 用于存放所有 <code>reducer</code>的文件夹</p>
<ul>
<li><code>count.js</code> ------ 用于存储 <code>Count</code>组件的 <code>reducer</code></li>
<li><code>person.js</code> ------ 用于存储 <code>Person</code>组件的 <code>reducer</code></li>
<li><code>index.js</code> ------ 用于存储汇总的 <code>reducer</code>的文件（<code>combineReducers()</code>方法）</li>
</ul>
</li>
<li>
<p><code>constant.js</code> ------ 用于存储一些公用的命名的文件</p>
</li>
<li>
<p><code>store.js</code> ------ <code>react-redux</code>的 <code>store</code>文件</p>
</li>
</ul>
</li>
</ul>
<h3 data-id="heading-88">9. 再说一遍，能不用就别用这东西！！</h3>
<h2 data-id="heading-89">十二、React16.8 与一些扩展</h2>
<h3 data-id="heading-90">1. lazy() 与 Suspense</h3>
<p>之前的组件，都是一并加载的，这样会给服务器带来较大的负担，所以 <code>react</code>推出了 <code>lazy()</code>懒加载，进行组件的按需加载。<br>
与之一起出来的是 <code>Suspense</code>，他解决的是组件在加载过程中还没加载出来时的白屏，用于展示其他的内容。</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">import</span> React, &#123; Component, lazy, Suspense &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'react'</span>
<span class="hljs-keyword">import</span> &#123;Route, Link&#125; <span class="hljs-keyword">from</span> <span class="hljs-string">"react-router-dom"</span>

<span class="hljs-comment">// import Home from "./Home";</span>
<span class="hljs-comment">// import About from "./About";</span>
<span class="hljs-keyword">import</span> Loading <span class="hljs-keyword">from</span> <span class="hljs-string">"./Loading"</span>;
<span class="hljs-comment">// lazy() 方法的参数是一个函数，返回需要加载的组件</span>
<span class="hljs-keyword">const</span> Home = lazy(<span class="hljs-function">()=></span><span class="hljs-keyword">import</span>(<span class="hljs-string">"./Home"</span>))
<span class="hljs-keyword">const</span> About = lazy(<span class="hljs-function">()=></span><span class="hljs-keyword">import</span>(<span class="hljs-string">"./About"</span>))
<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> <span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">index</span> <span class="hljs-keyword">extends</span> <span class="hljs-title">Component</span> </span>&#123;
    <span class="hljs-function"><span class="hljs-title">render</span>(<span class="hljs-params"></span>)</span> &#123;
        <span class="hljs-keyword">return</span> (
            <span class="xml"><span class="hljs-tag"><<span class="hljs-name">div</span>></span>
                <span class="hljs-tag"><<span class="hljs-name">Link</span> <span class="hljs-attr">to</span>=<span class="hljs-string">"/home"</span>></span>Home<span class="hljs-tag"></<span class="hljs-name">Link</span>></span>
                <span class="hljs-tag"><<span class="hljs-name">Link</span> <span class="hljs-attr">to</span>=<span class="hljs-string">"/about"</span>></span>About<span class="hljs-tag"></<span class="hljs-name">Link</span>></span>
                <span class="hljs-tag"><<span class="hljs-name">hr</span>/></span>
                &#123;/* Suspense 用于解决加载组件时的白屏，可以显示其他的内容，而其他内容不允许使用 lazy加载 */&#125;
                <span class="hljs-tag"><<span class="hljs-name">Suspense</span> <span class="hljs-attr">fallback</span>=<span class="hljs-string">&#123;</span><<span class="hljs-attr">Loading</span>/></span>&#125;>
                    <span class="hljs-tag"><<span class="hljs-name">Route</span> <span class="hljs-attr">path</span>=<span class="hljs-string">"/home"</span> <span class="hljs-attr">component</span>=<span class="hljs-string">&#123;Home&#125;</span>></span><span class="hljs-tag"></<span class="hljs-name">Route</span>></span>
                    <span class="hljs-tag"><<span class="hljs-name">Route</span> <span class="hljs-attr">path</span>=<span class="hljs-string">"/about"</span> <span class="hljs-attr">component</span>=<span class="hljs-string">&#123;About&#125;</span>></span><span class="hljs-tag"></<span class="hljs-name">Route</span>></span>
                <span class="hljs-tag"></<span class="hljs-name">Suspense</span>></span>
            <span class="hljs-tag"></<span class="hljs-name">div</span>></span></span>
        )
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li><code>lazy</code> 的参数是一个函数，使用 <code>import</code> 导入一个组件并返回</li>
<li><code>Suspense</code> 的属性 <code>fallback</code>属性的属性值是 <strong>组件标签</strong> 而不是组件</li>
<li><code>Suspense</code>所使用的组件不能使用 <code>lazy</code>进行懒加载。</li>
</ul>
<h3 data-id="heading-91">2. Hook</h3>
<p><strong>React16.8</strong>可以说是给函数式组件一次春天，因为他有了<code>Hook</code>，可以实现一些 <code>state</code>、生命周期函数，<code>refs</code>等特性。<br>
让我们一个个来看：</p>
<h4 data-id="heading-92">(1) stateHook</h4>
<p>可以让函数式组件实现使用 <code>state</code>的特性：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript">
<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">Demo</span>(<span class="hljs-params"></span>) </span>&#123;
    <span class="hljs-comment">// useState返回一个数组，只有两个元素（只有两个元素）</span>
    <span class="hljs-comment">// 元素1 为状态，元素2 为更新状态的方法</span>
    <span class="hljs-comment">// 第一次调用时以及将count进行底层存储，所以 Demo重复渲染不会重置count数据</span>
    <span class="hljs-keyword">const</span> [count, setCount] = React.useState(<span class="hljs-number">0</span>); <span class="hljs-comment">// 初始值赋为 0</span>
    <span class="hljs-keyword">const</span> [name, setName] = React.useState(<span class="hljs-string">"Tom"</span>);
    <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">add</span>(<span class="hljs-params"></span>)</span>&#123;
        <span class="hljs-comment">// 进行状态赋值</span>
        <span class="hljs-comment">// setCount(count + 1); // 写法1，直接将原来的状态值覆盖</span>
        setCount(<span class="hljs-function"><span class="hljs-params">count</span>=></span> count+<span class="hljs-number">1</span>); <span class="hljs-comment">// 写法2，参数为函数，接受原本的状态值，返回新的状态值，覆盖原来的状态</span>
    &#125;
    <span class="hljs-keyword">return</span> (
        <span class="xml"><span class="hljs-tag"><<span class="hljs-name">div</span>></span>
            <span class="hljs-tag"><<span class="hljs-name">h3</span>></span>名字：&#123;name&#125;<span class="hljs-tag"></<span class="hljs-name">h3</span>></span>
            <span class="hljs-tag"><<span class="hljs-name">h2</span>></span>当前求和：&#123;count&#125;<span class="hljs-tag"></<span class="hljs-name">h2</span>></span>
            <span class="hljs-tag"><<span class="hljs-name">button</span> <span class="hljs-attr">onClick</span>=<span class="hljs-string">&#123;add&#125;</span>></span>点击加一<span class="hljs-tag"></<span class="hljs-name">button</span>></span>    
        <span class="hljs-tag"></<span class="hljs-name">div</span>></span></span>
    )
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-93">(2) EffectHook</h4>
<p>可以让函数式组件实现类似<strong>生命周期钩子</strong>的特性：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">Demo</span>(<span class="hljs-params"></span>) </span>&#123;
    <span class="hljs-keyword">const</span> [count, setCount] = React.useState(<span class="hljs-number">0</span>);
    <span class="hljs-keyword">const</span> [name, setName] = React.useState(<span class="hljs-string">"Tom"</span>);
    <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">add</span>(<span class="hljs-params"></span>)</span>&#123;
        setCount(<span class="hljs-function"><span class="hljs-params">count</span>=></span> count+<span class="hljs-number">1</span>);
    &#125;
    <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">updName</span>(<span class="hljs-params"></span>)</span>&#123;
        setName(<span class="hljs-function"><span class="hljs-params">name</span>=></span><span class="hljs-string">"Jerry"</span>);
    &#125;
    <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">unmount</span>(<span class="hljs-params"></span>)</span>&#123;
        ReactDOM.unmountComponentAtNode(<span class="hljs-built_in">document</span>.querySelector(<span class="hljs-string">"#root"</span>));
    &#125;
    <span class="hljs-comment">// useEffect接收两个参数，第一个为函数体，第二个为检测的对象(数组)，当检测的对象状态发生改变，就会触发函数</span>
    <span class="hljs-comment">// 不填写第二参数时，检测所有元素，相当于 componentDidUpdate生命周期函数</span>
    React.useEffect(<span class="hljs-function">()=></span>&#123;
        <span class="hljs-comment">// console.log("asdf")</span>
        <span class="hljs-keyword">let</span> timer = <span class="hljs-built_in">setInterval</span>(<span class="hljs-function">()=></span>&#123;
            setCount(<span class="hljs-function"><span class="hljs-params">count</span>=></span>count+<span class="hljs-number">1</span>);
        &#125;,<span class="hljs-number">1000</span>);
        <span class="hljs-keyword">return</span> <span class="hljs-function">()=></span>&#123;        <span class="hljs-comment">// 在 useEffect中的函数体里返回的函数，相当于 componentWillUnmount生命周期函数</span>
            <span class="hljs-built_in">console</span>.log(<span class="hljs-string">"unmount"</span>)
            <span class="hljs-built_in">clearInterval</span>(timer);
;        &#125;
    &#125;,[]) <span class="hljs-comment">// 数组为空是谁也不检测，只执行一次函数，相当于生命周期函数的 componentDidMount</span>
    <span class="hljs-keyword">return</span> (
        <span class="xml"><span class="hljs-tag"><<span class="hljs-name">div</span>></span>
            <span class="hljs-tag"><<span class="hljs-name">h2</span>></span>当前求和：&#123;count&#125;<span class="hljs-tag"></<span class="hljs-name">h2</span>></span>
            <span class="hljs-tag"><<span class="hljs-name">button</span> <span class="hljs-attr">onClick</span>=<span class="hljs-string">&#123;add&#125;</span>></span>点击加一<span class="hljs-tag"></<span class="hljs-name">button</span>></span>
            <span class="hljs-tag"><<span class="hljs-name">h2</span>></span>当前名字：&#123;name&#125;<span class="hljs-tag"></<span class="hljs-name">h2</span>></span>
            <span class="hljs-tag"><<span class="hljs-name">button</span> <span class="hljs-attr">onClick</span>=<span class="hljs-string">&#123;updName&#125;</span>></span>修改名字为Jerry<span class="hljs-tag"></<span class="hljs-name">button</span>></span>
            <span class="hljs-tag"><<span class="hljs-name">button</span> <span class="hljs-attr">onClick</span>=<span class="hljs-string">&#123;unmount&#125;</span>></span>卸载组件<span class="hljs-tag"></<span class="hljs-name">button</span>></span>
        <span class="hljs-tag"></<span class="hljs-name">div</span>></span></span>
    )
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>可以把 <code>useEffect Hook</code> 看作三个函数的结合：</p>
<ul>
<li><code>componentDidMount</code></li>
<li><code>componentDidUpdate</code></li>
<li><code>componentWillUnmount</code></li>
</ul>
<h4 data-id="heading-94">(3) refHook</h4>
<p><code>refHook</code> 可以让函数式组件实现类似 <code>ref</code>的特性</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">Demo</span>(<span class="hljs-params"></span>) </span>&#123;
    <span class="hljs-keyword">const</span> [count, setCount] = React.useState(<span class="hljs-number">0</span>);
    <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">add</span>(<span class="hljs-params"></span>)</span>&#123;
        setCount(<span class="hljs-function"><span class="hljs-params">count</span>=></span> count+<span class="hljs-number">1</span>);
    &#125;
    <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">show</span>(<span class="hljs-params"></span>)</span>&#123;
        <span class="hljs-comment">// 获取文本框内容</span>
        alert(myInput.current.value);
    &#125;
    <span class="hljs-comment">// 生成一个容器</span>
    <span class="hljs-keyword">const</span> myInput = React.useRef();
    <span class="hljs-keyword">return</span> (
        <span class="xml"><span class="hljs-tag"><<span class="hljs-name">div</span>></span>
            <span class="hljs-tag"><<span class="hljs-name">h2</span>></span>当前求和：&#123;count&#125;<span class="hljs-tag"></<span class="hljs-name">h2</span>></span>
            &#123;/* 绑定容器 */&#125;
            <span class="hljs-tag"><<span class="hljs-name">input</span> <span class="hljs-attr">type</span>=<span class="hljs-string">"text"</span> <span class="hljs-attr">ref</span>=<span class="hljs-string">&#123;myInput&#125;/</span>></span>
            <span class="hljs-tag"><<span class="hljs-name">button</span> <span class="hljs-attr">onClick</span>=<span class="hljs-string">&#123;add&#125;</span>></span>点击加一<span class="hljs-tag"></<span class="hljs-name">button</span>></span>
            <span class="hljs-tag"><<span class="hljs-name">button</span> <span class="hljs-attr">onClick</span>=<span class="hljs-string">&#123;show&#125;</span>></span>点击展示数据<span class="hljs-tag"></<span class="hljs-name">button</span>></span>
        <span class="hljs-tag"></<span class="hljs-name">div</span>></span></span>
    )
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这个就没啥难度。</p>
<h3 data-id="heading-95">3. Fragment</h3>
<p>在 <code>react</code>渲染组件的时候，当你的组件越来越多时，你有没有发现你的 DOM层级越来越多，有些不美观，所以就出现了 <code>Fragment</code>。<br>
可以使用 <code>Fragment</code>标签代替组件的根标签，在 <strong>React</strong>解析的时候会被处理掉，
从而让生成出来的代码的层级更加简洁。</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> <span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Demo</span> <span class="hljs-keyword">extends</span> <span class="hljs-title">Component</span> </span>&#123;
    <span class="hljs-function"><span class="hljs-title">render</span>(<span class="hljs-params"></span>)</span> &#123;
        <span class="hljs-keyword">return</span> (
            <span class="hljs-comment">// 使用空标签可以达到一样的效果，但是空标签不允许包含任何的属性</span>
            <span class="xml"><span class="hljs-tag"><<span class="hljs-name">Fragment</span> <span class="hljs-attr">key</span>=<span class="hljs-string">&#123;1&#125;</span>></span>
                <span class="hljs-tag"><<span class="hljs-name">input</span> <span class="hljs-attr">type</span>=<span class="hljs-string">"text"</span>/></span>
                <span class="hljs-tag"><<span class="hljs-name">input</span> <span class="hljs-attr">type</span>=<span class="hljs-string">"text"</span>/></span>
            <span class="hljs-tag"></<span class="hljs-name">Fragment</span>></span></span>
        )
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-96">4. Context</h3>
<p><code>Context</code>是一种新的组件通信方式，常用于【祖组件】和【后代组件】之间通信。</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">// 1. 创建一个 Context容器对象</span>
<span class="hljs-keyword">const</span> UserNameContext = React.createContext();
<span class="hljs-comment">// 1.1 拿到 Provider与 Consumer属性</span>
<span class="hljs-keyword">const</span> &#123;Provider, Consumer&#125; = UserNameContext;
<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> <span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">A</span> <span class="hljs-keyword">extends</span> <span class="hljs-title">Component</span> </span>&#123;
    state=&#123;<span class="hljs-attr">username</span>: <span class="hljs-string">"Tom"</span>&#125;
    <span class="hljs-function"><span class="hljs-title">render</span>(<span class="hljs-params"></span>)</span> &#123;
        <span class="hljs-keyword">return</span> (
            <span class="xml"><span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">className</span>=<span class="hljs-string">"a"</span>></span>
                <span class="hljs-tag"><<span class="hljs-name">h1</span>></span>我是A组件<span class="hljs-tag"></<span class="hljs-name">h1</span>></span>
                <span class="hljs-tag"><<span class="hljs-name">p</span>></span>我的用户名是：&#123;this.state.username&#125;<span class="hljs-tag"></<span class="hljs-name">p</span>></span>
                &#123;/* 2 使用组件，后代组件都能收到来自 value的值，就在 this上的 context属性上（需提前声明）  */&#125;
                <span class="hljs-tag"><<span class="hljs-name">Provider</span> <span class="hljs-attr">value</span>=<span class="hljs-string">&#123;this.state.username&#125;</span>></span>
                    <span class="hljs-tag"><<span class="hljs-name">B</span>/></span>
                <span class="hljs-tag"></<span class="hljs-name">Provider</span>></span>
            <span class="hljs-tag"></<span class="hljs-name">div</span>></span></span>
        )
    &#125;
&#125;
<span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">B</span> <span class="hljs-keyword">extends</span> <span class="hljs-title">Component</span> </span>&#123;
    <span class="hljs-comment">// 3. 声明接受 Context</span>
    <span class="hljs-keyword">static</span> contextType = UserNameContext;   <span class="hljs-comment">// 此方法只适用于 类组件</span>
    <span class="hljs-function"><span class="hljs-title">render</span>(<span class="hljs-params"></span>)</span> &#123;
        <span class="hljs-built_in">console</span>.log(<span class="hljs-built_in">this</span>.context);  <span class="hljs-comment">// Tom</span>
        <span class="hljs-keyword">return</span> (
            <span class="xml"><span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">className</span>=<span class="hljs-string">"b"</span>></span>
                <span class="hljs-tag"><<span class="hljs-name">h2</span>></span>我是B组件<span class="hljs-tag"></<span class="hljs-name">h2</span>></span>
                <span class="hljs-tag"><<span class="hljs-name">p</span>></span>A的用户名是：&#123;this.context&#125;<span class="hljs-tag"></<span class="hljs-name">p</span>></span>
                <span class="hljs-tag"><<span class="hljs-name">C</span>/></span>
            <span class="hljs-tag"></<span class="hljs-name">div</span>></span></span>
        )
    &#125;
&#125;
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">C</span>(<span class="hljs-params"></span>) </span>&#123;
    <span class="hljs-keyword">return</span> (
        <span class="xml"><span class="hljs-tag"><<span class="hljs-name">div</span>></span>
             <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">className</span>=<span class="hljs-string">"c"</span>></span>
                <span class="hljs-tag"><<span class="hljs-name">h3</span>></span>我是C组件<span class="hljs-tag"></<span class="hljs-name">h3</span>></span>         
                &#123;/* 3.2 使用 Consumer组件进行声明接受（类组件和函数式组件都可以）  */&#125;
                <span class="hljs-tag"><<span class="hljs-name">Consumer</span>></span>
                    &#123;value=> ("A的用户名是：" + value)&#125;
                <span class="hljs-tag"></<span class="hljs-name">Consumer</span>></span>
             <span class="hljs-tag"></<span class="hljs-name">div</span>></span>
        <span class="hljs-tag"></<span class="hljs-name">div</span>></span></span>
    )
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-97">5. PureComponent</h3>
<p>在组件中，只要执行了 <code>setState()</code>，即使没更新状态数据，组件也会重新 <code>render()</code>。<br>
只要组件重新 <code>render()</code>，就会自动重新 <code>render()</code>子组件，纵使子组件没有使用到父组件任何数据。<br>
这两种情况都会导致重复渲染，使得效率低下。</p>
<p>效率高的做法：只有组件的<code>state</code>或<code>props</code>发生变化时菜重新<code>render()</code>。</p>
<ul>
<li>解决方法1：通过生命周期函数 <code>shouldComponentUpdate()</code> 进行数据判断在进行重新渲染</li>
<li>解决方法2：类组件通过继承 <code>PureComponent</code>组件，自动进行数据判断（浅对比---判断地址值）（常用）</li>
</ul>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">import</span> React, &#123; Component, PureComponent &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'react'</span>
<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> <span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Parent</span> <span class="hljs-keyword">extends</span> <span class="hljs-title">PureComponent</span> </span>&#123;
    state = &#123;<span class="hljs-attr">carName</span>: <span class="hljs-string">"奔驰"</span>&#125;
    changeCar = <span class="hljs-function">()=></span>&#123;
        <span class="hljs-built_in">this</span>.setState(<span class="hljs-function"><span class="hljs-params">state</span>=></span>(&#123;<span class="hljs-attr">carName</span>:<span class="hljs-string">"迈巴赫"</span>&#125;));
    &#125;
    <span class="hljs-comment">// shouldComponentUpdate有两个参数，分别是准备修改的 props和 state</span>
    <span class="hljs-comment">// shouldComponentUp date(nextProps, nextState)&#123;</span>
    <span class="hljs-comment">//     console.log(nextProps, nextState);  // 目标要修改的props和state</span>
    <span class="hljs-comment">//     console.log(this.props, this.state);   // 还未修改原本的props和state</span>
    <span class="hljs-comment">//     return !this.state.carName === nextState.carName;</span>
    <span class="hljs-comment">// &#125;</span>
    <span class="hljs-function"><span class="hljs-title">render</span>(<span class="hljs-params"></span>)</span> &#123;
        <span class="hljs-built_in">console</span>.log(<span class="hljs-string">"parent render"</span>);
        <span class="hljs-keyword">return</span> (
            <span class="xml"><span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">className</span>=<span class="hljs-string">"parent"</span>></span>
                <span class="hljs-tag"><<span class="hljs-name">h1</span>></span>Parent<span class="hljs-tag"></<span class="hljs-name">h1</span>></span>
                <span class="hljs-tag"><<span class="hljs-name">p</span>></span>我的车是：&#123;this.state.carName&#125;<span class="hljs-tag"></<span class="hljs-name">p</span>></span>
                <span class="hljs-tag"><<span class="hljs-name">button</span> <span class="hljs-attr">onClick</span>=<span class="hljs-string">&#123;this.changeCar&#125;</span>></span>点击换车<span class="hljs-tag"></<span class="hljs-name">button</span>></span>
                <span class="hljs-tag"><<span class="hljs-name">Child</span>/></span>
            <span class="hljs-tag"></<span class="hljs-name">div</span>></span></span>
        )
    &#125;
&#125;
<span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Child</span> <span class="hljs-keyword">extends</span> <span class="hljs-title">PureComponent</span> </span>&#123;
    
    <span class="hljs-comment">// shouldComponentUpdate(nextProps)&#123;</span>
    <span class="hljs-comment">//     return !this.props.carName === nextProps.carName</span>
    <span class="hljs-comment">// &#125;</span>
    <span class="hljs-function"><span class="hljs-title">render</span>(<span class="hljs-params"></span>)</span> &#123;
        <span class="hljs-built_in">console</span>.log(<span class="hljs-string">"child render"</span>);
        <span class="hljs-keyword">return</span> (
            <span class="xml"><span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">className</span>=<span class="hljs-string">"child"</span>></span>
                <span class="hljs-tag"><<span class="hljs-name">h2</span>></span>Child<span class="hljs-tag"></<span class="hljs-name">h2</span>></span>
                &#123;/* <span class="hljs-tag"><<span class="hljs-name">p</span>></span>父亲的车是：&#123;this.props.carName&#125;<span class="hljs-tag"></<span class="hljs-name">p</span>></span> */&#125;
            <span class="hljs-tag"></<span class="hljs-name">div</span>></span></span>
        )
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-98">6. 父子组件</h3>
<p>不多说，直接上代码：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">import</span> React, &#123; Component, PureComponent &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'react'</span>
<span class="hljs-keyword">import</span> <span class="hljs-string">"./index.css"</span>

<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> <span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Parent</span> <span class="hljs-keyword">extends</span> <span class="hljs-title">PureComponent</span> </span>&#123;
    state = &#123;<span class="hljs-attr">carName</span>: <span class="hljs-string">"奔驰"</span>&#125;
    changeCar = <span class="hljs-function">()=></span>&#123;
        <span class="hljs-built_in">this</span>.setState(<span class="hljs-function"><span class="hljs-params">state</span>=></span>(&#123;<span class="hljs-attr">carName</span>:<span class="hljs-string">"迈巴赫"</span>&#125;));
    &#125;
    <span class="hljs-function"><span class="hljs-title">render</span>(<span class="hljs-params"></span>)</span> &#123;
        <span class="hljs-built_in">console</span>.log(<span class="hljs-string">"parent render"</span>);
        <span class="hljs-keyword">return</span> (
            <span class="xml"><span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">className</span>=<span class="hljs-string">"parent"</span>></span>
                <span class="hljs-tag"><<span class="hljs-name">h1</span>></span>Parent<span class="hljs-tag"></<span class="hljs-name">h1</span>></span>
                <span class="hljs-tag"><<span class="hljs-name">p</span>></span>我的车是：&#123;this.state.carName&#125;<span class="hljs-tag"></<span class="hljs-name">p</span>></span>
                &#123;/* A组件 与 B组件 形成父子组件的第二种方法 */&#125;
                &#123;/* <span class="hljs-tag"><<span class="hljs-name">A</span>></span>
                    <span class="hljs-tag"><<span class="hljs-name">B</span>/></span>
                <span class="hljs-tag"></<span class="hljs-name">A</span>></span> */&#125;
                &#123;/* 类似于 Vue的插槽 */&#125;
                <span class="hljs-tag"><<span class="hljs-name">A</span> <span class="hljs-attr">render</span>=<span class="hljs-string">&#123;(name)</span>=></span><span class="hljs-tag"><<span class="hljs-name">B</span> <span class="hljs-attr">name</span>=<span class="hljs-string">&#123;name&#125;/</span>></span>&#125;/>  
            <span class="hljs-tag"></<span class="hljs-name">div</span>></span></span>
        )
    &#125;
&#125;

<span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">A</span> <span class="hljs-keyword">extends</span> <span class="hljs-title">PureComponent</span> </span>&#123;
    <span class="hljs-function"><span class="hljs-title">render</span>(<span class="hljs-params"></span>)</span> &#123;
        <span class="hljs-built_in">console</span>.log(<span class="hljs-string">"A render"</span>);
        <span class="hljs-keyword">return</span> (
            <span class="xml"><span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">className</span>=<span class="hljs-string">"a"</span>></span>
                <span class="hljs-tag"><<span class="hljs-name">h2</span>></span>A<span class="hljs-tag"></<span class="hljs-name">h2</span>></span>
                &#123;/* A组件 与 B组件 形成父子组件的第一种方式 */&#125;
                &#123;/* <span class="hljs-tag"><<span class="hljs-name">B</span>/></span> */&#125;
                &#123;/* &#123;this.props.children&#125; */&#125;
                &#123;this.props.render("Tom")&#125;
            <span class="hljs-tag"></<span class="hljs-name">div</span>></span></span>
        )
    &#125;
&#125;
<span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">B</span> <span class="hljs-keyword">extends</span> <span class="hljs-title">PureComponent</span> </span>&#123;
    <span class="hljs-function"><span class="hljs-title">render</span>(<span class="hljs-params"></span>)</span> &#123;
        <span class="hljs-built_in">console</span>.log(<span class="hljs-string">"B render"</span>);
        <span class="hljs-keyword">return</span> (
            <span class="xml"><span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">className</span>=<span class="hljs-string">"b"</span>></span>
                <span class="hljs-tag"><<span class="hljs-name">h2</span>></span>B<span class="hljs-tag"></<span class="hljs-name">h2</span>></span>
                <span class="hljs-tag"><<span class="hljs-name">p</span>></span>&#123;this.props.name&#125;<span class="hljs-tag"></<span class="hljs-name">p</span>></span>
            <span class="hljs-tag"></<span class="hljs-name">div</span>></span></span>
        )
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-99">7. ErrorBoundary</h3>
<p>当你的组件存在父子组件关系时，如果说你的子组件出现了错误，那么会导致父组件一并崩掉，那有没有什么办法，可以把错误控制在一个组件里，不让他扩散呢？<br>
答案是有的，有两个函数：</p>
<ul>
<li><code>getDerivedStateFromError(error)</code></li>
<li><code>componentDidCatch(error, info)</code></li>
</ul>
<p>上代码：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">import</span> React, &#123; Component, Fragment &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'react'</span>
<span class="hljs-keyword">import</span> Child <span class="hljs-keyword">from</span> <span class="hljs-string">"./Child"</span>;
<span class="hljs-comment">// 错误边界即把组件的错误信息控制在一个组件中，不使他扩散而导致程序崩溃</span>
<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> <span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Person</span> <span class="hljs-keyword">extends</span> <span class="hljs-title">Component</span> </span>&#123;
    state = &#123;
        <span class="hljs-attr">hasError</span>: <span class="hljs-string">""</span>,   <span class="hljs-comment">// 用于标识子组件是否产生错误</span>
    &#125;
    <span class="hljs-comment">// 当子组件发生错误时会触发该生命周期函数，且参数为错误信息</span>
    <span class="hljs-comment">// 只适用于生产环境，只能捕获后代组件生命周期产生的错误</span>
    <span class="hljs-keyword">static</span> <span class="hljs-function"><span class="hljs-title">getDerivedStateFromError</span>(<span class="hljs-params">error</span>)</span>&#123;
        <span class="hljs-comment">// 一般用于处理错误出现时返回给用户展示的东西</span>
        <span class="hljs-built_in">console</span>.log(<span class="hljs-string">"出错了"</span>);
        <span class="hljs-built_in">console</span>.log(error);
    &#125;
    <span class="hljs-comment">// 组件渲染过程中出错就会触发该生命周期函数</span>
    <span class="hljs-function"><span class="hljs-title">componentDidCatch</span>(<span class="hljs-params">error, info</span>)</span>&#123;
        <span class="hljs-comment">// 一般用于统计错误，反馈给雾浮起，用于通知程序员进行bug修改</span>
        <span class="hljs-built_in">console</span>.log(<span class="hljs-string">"渲染组件出错"</span>);
        <span class="hljs-built_in">console</span>.log(error, info)
    &#125;
    <span class="hljs-function"><span class="hljs-title">render</span>(<span class="hljs-params"></span>)</span> &#123;
        <span class="hljs-keyword">return</span> (
            <span class="xml"><span class="hljs-tag"><<span class="hljs-name">Fragment</span>></span>
                <span class="hljs-tag"><<span class="hljs-name">h2</span>></span>我是Parent组件<span class="hljs-tag"></<span class="hljs-name">h2</span>></span>
                &#123;
                    this.state.hasError ? 
                        <span class="hljs-tag"><<span class="hljs-name">h2</span>></span>当前网络不大行，建议买高级网络套餐好吧<span class="hljs-tag"></<span class="hljs-name">h2</span>></span> :
                        <span class="hljs-tag"><<span class="hljs-name">Child</span>/></span>                
                &#125;
            <span class="hljs-tag"></<span class="hljs-name">Fragment</span>></span></span>
        )
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-100">8. 组件通信方式总结</h3>
<ul>
<li>组件之间的关系：
<ol>
<li>父子组件</li>
<li>兄弟组件</li>
<li>祖孙组件（跨级组件）</li>
</ol>
</li>
<li>几种通信方式：
<ol>
<li><code>props</code>
<ol>
<li>children props</li>
<li>render props</li>
</ol>
</li>
<li>消息订阅
<code>pubsub</code>,<code> event</code></li>
<li>集中式管理
<code>redux</code>, <code>dva</code>, <code>react-redux</code></li>
<li>conText
生产者， 消费者模式</li>
</ol>
</li>
<li>较好的搭配方式：
<ul>
<li>父子组件：<code>props</code></li>
<li>兄弟组件： 消息订阅发布，集中式管理</li>
<li>祖孙组件：消息订阅发布，集中式管理，<code>conText</code></li>
</ul>
</li>
</ul>
<h2 data-id="heading-101">十三、最后</h2>
<p>这些就是我学习React的一些学习笔记了，日后如果还有其他的内容的话应该会深究后写成单独的文章了。</p>
<blockquote>
<p>新人上路，还请多多包含。<br>
我是MoonLight，一个初出茅庐的小前端。</p>
</blockquote></div>  
</div>
            