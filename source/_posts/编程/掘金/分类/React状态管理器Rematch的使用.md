
---
title: 'React状态管理器Rematch的使用'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=510'
author: 掘金
comments: false
date: Wed, 07 Sep 2022 19:33:23 GMT
thumbnail: 'https://picsum.photos/400/300?random=510'
---

<div>   
<div class="markdown-body cache"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:16px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:24px;margin-bottom:5px&#125;.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;font-size:20px&#125;.markdown-body h2&#123;padding-bottom:12px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h2 data-id="heading-0"><code>Rematch</code>使用</h2>
<h3 data-id="heading-1">1. <code>Rematch</code>介绍</h3>
<p><code>Rematch</code>是没有样板文件的<code>Redux</code>的最佳实践，没有<code>action types</code>、 <code>action creators</code>, 状态转换或<code>thunks</code>。</p>
<h3 data-id="heading-2">2. <code>Rematch</code>特性</h3>
<p><code>Redux</code> 是一个了不起的状态管理工具，由良好的中间件生态系统和优秀的开发工具支持。<code>Rematch</code> 以 <code>Redux</code> 为基础，减少样板文件并强制执行最佳实践。</p>
<ul>
<li>小于 2kb 的大小</li>
<li>无需配置</li>
<li>减少 <code>Redux</code> 样板</li>
<li><code>React</code> 开发工具支持</li>
<li>支持动态添加<code>reducer</code></li>
<li><code>Typesctipt</code>支持</li>
<li>允许创建多个<code>store</code></li>
<li>支持<code>React Native</code></li>
<li>可通过插件扩展</li>
</ul>
<h3 data-id="heading-3">3. 基本使用</h3>
<p>以一个计数器(<code>count</code>)应用为例子：</p>
<p>a. 定义模型(<code>Model</code>)
<code>Model</code>集合了<code>state</code>、<code>reducers</code>、<code>async actions</code>,它是描述<code>Redux store</code>的一部分以及它是如何变化的,定义一个模型只需回答三个小问题：</p>
<pre><code class="hljs language-markdown copyable" lang="markdown"><span class="hljs-bullet">-</span> 如何初始化<span class="hljs-code">`state`</span>？ <span class="hljs-strong">**state**</span>
<span class="hljs-bullet">-</span> 如何改变<span class="hljs-code">`state`</span>？ <span class="hljs-strong">**reducers**</span>
<span class="hljs-bullet">-</span> 如何处理异步<span class="hljs-code">`actions`</span>？ <span class="hljs-strong">**effect**</span> with async/await
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// ./models/countModel.js</span>
<span class="hljs-keyword">export</span> <span class="hljs-keyword">const</span> count = &#123;
  <span class="hljs-attr">state</span>: <span class="hljs-number">0</span>, <span class="hljs-comment">// 初始化状态</span>
  <span class="hljs-attr">reducers</span>: &#123;
    <span class="hljs-comment">// reducers中使用纯函数来处理状态的变化</span>
    <span class="hljs-title function_">increment</span>(<span class="hljs-params">state, payload</span>) &#123;
      <span class="hljs-keyword">return</span> state = payload
    &#125;,
  &#125;,
  <span class="hljs-attr">effects</span>: <span class="hljs-function"><span class="hljs-params">dispatch</span> =></span> (&#123;
    <span class="hljs-comment">// effects中使用非纯函数处理状态变化</span>
    <span class="hljs-comment">// 使用async/await处理异步的actions</span>
    <span class="hljs-keyword">async</span> <span class="hljs-title function_">incrementAsync</span>(<span class="hljs-params">payload, rootState</span>) &#123;
      <span class="hljs-keyword">await</span> <span class="hljs-keyword">new</span> <span class="hljs-title class_">Promise</span>(<span class="hljs-function"><span class="hljs-params">resolve</span> =></span> <span class="hljs-built_in">setTimeout</span>(resolve, <span class="hljs-number">1000</span>))
      dispatch.<span class="hljs-property">count</span>.<span class="hljs-title function_">increment</span>(payload)
    &#125;
  &#125;)
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// ./models/index.js</span>
<span class="hljs-keyword">import</span> &#123; count &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'./count'</span>

<span class="hljs-keyword">export</span> <span class="hljs-keyword">const</span> models = &#123;
  count
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>b. 初始化<code>store</code>
使用<code>init</code>方法初始化<code>store</code>, <code>init</code>是构建配置的<code>Redux</code>存储所需的唯一方法。<code>init</code>的其他参数可以访问<a href="https://link.juejin.cn/?target=https%3A%2F%2Frematchjs.bootcss.com%2Fdocs%2Fapi-reference" target="_blank" rel="nofollow noopener noreferrer" title="https://rematchjs.bootcss.com/docs/api-reference" ref="nofollow noopener noreferrer">api</a>了解。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// store.js</span>
<span class="hljs-keyword">import</span> &#123; init &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'@rematch/core'</span>
<span class="hljs-keyword">import</span> * <span class="hljs-keyword">as</span> models <span class="hljs-keyword">from</span> <span class="hljs-string">'./models'</span>

<span class="hljs-keyword">const</span> store = <span class="hljs-title function_">init</span>(&#123;models&#125;)

<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> store
<span class="copy-code-btn">复制代码</span></code></pre>
<p>c. <code>Dispatch actions</code>
可以通过使用<code>dispatch</code>来改变你的<code>store</code>中的<code>reducer</code>和<code>effects</code>，而不需要使用<code>action types</code> 或 <code>action creators</code>; <code>Dispatch</code>可以直接被调用，也可以使用简写<code>dispatch[model][action](payload)</code>。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> &#123; dispatch &#125; = store
<span class="hljs-comment">// state = &#123; count: 0 &#125;</span>

<span class="hljs-comment">// reducers</span>
<span class="hljs-title function_">dispatch</span>(&#123; <span class="hljs-attr">type</span>: <span class="hljs-string">'count/increment'</span>, <span class="hljs-attr">payload</span>: <span class="hljs-number">1</span> &#125;) <span class="hljs-comment">// state = &#123; count: 1 &#125;</span>
dispatch.<span class="hljs-property">count</span>.<span class="hljs-title function_">increment</span>(<span class="hljs-number">1</span>) <span class="hljs-comment">// state = &#123; count: 2 &#125;</span>

<span class="hljs-comment">// effects</span>
<span class="hljs-title function_">dispatch</span>(&#123; <span class="hljs-attr">type</span>: <span class="hljs-string">'count/incrementAsync'</span>, <span class="hljs-attr">payload</span>: <span class="hljs-number">1</span> &#125;) <span class="hljs-comment">// 延时1秒后 state = &#123; count: 3 &#125;</span>
dispatch.<span class="hljs-property">count</span>.<span class="hljs-title function_">incrementAsync</span>(<span class="hljs-number">1</span>) <span class="hljs-comment">// 延时1秒后 state = &#123; count: 4 &#125;</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>d. <code>Rematch</code>和<code>Redux</code>一起使用
<code>Rematch</code>可以和原生<code>Redux</code>集成一起使用，看下边这个例子：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// App.js</span>
<span class="hljs-keyword">import</span> <span class="hljs-title class_">React</span> <span class="hljs-keyword">from</span> <span class="hljs-string">'react'</span>
<span class="hljs-keyword">import</span> <span class="hljs-title class_">ReactDOM</span> <span class="hljs-keyword">from</span> <span class="hljs-string">'react-dom'</span>
<span class="hljs-keyword">import</span> &#123; <span class="hljs-title class_">Provider</span>, connect &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'react-redux'</span>
<span class="hljs-keyword">import</span> store <span class="hljs-keyword">from</span> <span class="hljs-string">'./store'</span>

<span class="hljs-keyword">const</span> <span class="hljs-title function_">Count</span> = (<span class="hljs-params">props</span>) => (
    <span class="xml"><span class="hljs-tag"><<span class="hljs-name">div</span>></span>
        The count is &#123;props.count&#125;
        <span class="hljs-tag"><<span class="hljs-name">button</span> <span class="hljs-attr">onClick</span>=<span class="hljs-string">&#123;props.increment&#125;</span>></span>increment<span class="hljs-tag"></<span class="hljs-name">button</span>></span>
        <span class="hljs-tag"><<span class="hljs-name">button</span> <span class="hljs-attr">onClick</span>=<span class="hljs-string">&#123;props.incrementAsync&#125;</span>></span>incrementAsync<span class="hljs-tag"></<span class="hljs-name">button</span>></span>
    <span class="hljs-tag"></<span class="hljs-name">div</span>></span></span>
)

<span class="hljs-keyword">const</span> <span class="hljs-title function_">mapState</span> = (<span class="hljs-params">state</span>) => (&#123;
    <span class="hljs-attr">count</span>: state.<span class="hljs-property">count</span>,
&#125;)

<span class="hljs-keyword">const</span> <span class="hljs-title function_">mapDispatch</span> = (<span class="hljs-params">dispatch</span>) => (&#123;
    <span class="hljs-attr">increment</span>: <span class="hljs-function">() =></span> dispatch.<span class="hljs-property">count</span>.<span class="hljs-title function_">increment</span>(<span class="hljs-number">1</span>),
    <span class="hljs-attr">incrementAsync</span>: <span class="hljs-function">() =></span> dispatch.<span class="hljs-property">count</span>.<span class="hljs-title function_">incrementAsync</span>(<span class="hljs-number">1</span>),
&#125;)

<span class="hljs-keyword">const</span> <span class="hljs-title class_">CountContainer</span> = <span class="hljs-title function_">connect</span>(
    mapState,
    mapDispatch
)(<span class="hljs-title class_">Count</span>)

<span class="hljs-title class_">ReactDOM</span>.<span class="hljs-title function_">render</span>(
    <span class="xml"><span class="hljs-tag"><<span class="hljs-name">Provider</span> <span class="hljs-attr">store</span>=<span class="hljs-string">&#123;store&#125;</span>></span>
        <span class="hljs-tag"><<span class="hljs-name">CountContainer</span> /></span>
    <span class="hljs-tag"></<span class="hljs-name">Provider</span>></span></span>,
    <span class="hljs-variable language_">document</span>.<span class="hljs-title function_">getElementById</span>(<span class="hljs-string">'root'</span>)
)

<span class="copy-code-btn">复制代码</span></code></pre></div>  
</div>
            