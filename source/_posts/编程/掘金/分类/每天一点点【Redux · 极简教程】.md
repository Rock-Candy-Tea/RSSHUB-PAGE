
---
title: '每天一点点【Redux · 极简教程】'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://cors.zfour.workers.dev/?http://cn.redux.js.org/assets/images/ReduxDataFlowDiagram-49fa8c3968371d9ef6f2a1486bd40a26.gif'
author: 掘金
comments: false
date: Mon, 16 Aug 2021 19:31:02 GMT
thumbnail: 'https://cors.zfour.workers.dev/?http://cn.redux.js.org/assets/images/ReduxDataFlowDiagram-49fa8c3968371d9ef6f2a1486bd40a26.gif'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h3 data-id="heading-0">前言:</h3>
<p><a href="https://link.juejin.cn/?target=http%3A%2F%2Fcn.redux.js.org%2Fapi%2Fapi-reference" target="_blank" rel="nofollow noopener noreferrer" title="http://cn.redux.js.org/api/api-reference" ref="nofollow noopener noreferrer">Redux</a> : JS 应用的状态容器，提供可预测的状态管理, <code>当你有数据需要全局统一管理,并且渲染时</code>, 你可以考虑她。</p>
<h3 data-id="heading-1">知识点:</h3>
<ol>
<li>createStore 创建store</li>
<li>reducer 初始化、修改状态函数</li>
<li>getState 获取状态值</li>
<li>dispatch 提交更更新</li>
<li>subscribe 变更更订阅</li>
</ol>
<h3 data-id="heading-2">使用步骤:</h3>
<h4 data-id="heading-3">1. 准备工作 (处理逻辑 和 订阅)</h4>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">import</span> &#123; createStore, combineReducers &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'redux'</span>

<span class="hljs-comment">// I. reducer</span>
<span class="hljs-keyword">const</span> counterReducer = <span class="hljs-function">(<span class="hljs-params">state = <span class="hljs-number">0</span>, action</span>) =></span> &#123;
  <span class="hljs-keyword">switch</span> (action.type) &#123;
    <span class="hljs-keyword">case</span> <span class="hljs-string">'counter/ADD'</span>:
      <span class="hljs-keyword">return</span> state + action.payload || <span class="hljs-number">1</span>
    <span class="hljs-keyword">case</span> <span class="hljs-string">'MINUS'</span>:
      <span class="hljs-keyword">return</span> state - <span class="hljs-number">1</span>
    <span class="hljs-attr">default</span>:
      <span class="hljs-keyword">return</span> state
  &#125;
&#125;

<span class="hljs-keyword">const</span> todoReducer = <span class="hljs-function">(<span class="hljs-params">state = <span class="hljs-string">'todo list'</span>, action</span>) =></span> &#123;
  <span class="hljs-keyword">switch</span> (action.type) &#123;
    <span class="hljs-keyword">case</span> <span class="hljs-string">'todo/ADD'</span>:
      <span class="hljs-keyword">return</span> state + <span class="hljs-string">'add'</span>
    <span class="hljs-attr">default</span>:
      <span class="hljs-keyword">return</span> state
  &#125;
&#125;

<span class="hljs-comment">// II. createStore</span>

<span class="hljs-keyword">const</span> rootReducer = combineReducers(&#123;
  <span class="hljs-attr">todo</span>: todoReducer,
  <span class="hljs-attr">counter</span>: counterReducer
&#125;)

<span class="hljs-keyword">const</span> store = createStore(rootReducer)

<span class="hljs-comment">// III. subscribe</span>

<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">render</span>(<span class="hljs-params"></span>) </span>&#123;
  ReactDOM.render(
    <span class="xml"><span class="hljs-tag"><<span class="hljs-name">React.StrictMode</span>></span>
      <span class="hljs-tag"><<span class="hljs-name">ReduxPage</span> /></span>
    <span class="hljs-tag"></<span class="hljs-name">React.StrictMode</span>></span></span>,
    <span class="hljs-built_in">document</span>.getElementById(<span class="hljs-string">'root'</span>)
  );
&#125;
render()

store.subscribe(render)

<span class="copy-code-btn">复制代码</span></code></pre>
<p><code>tips: combineReducers 可以合并多个 reducer , 有利于代码解耦 以及 分工合作; 入参为一个对象, 在调用 getState 时, 返回的就是这个对象的对应的reducer之后的state值.</code></p>
<h4 data-id="heading-4">2. 消费与发布</h4>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> ReduxPage = <span class="hljs-function"><span class="hljs-params">props</span> =></span> &#123;
  <span class="hljs-comment">// 获取state</span>
  
  <span class="hljs-keyword">const</span> state = store.getState()
  
  <span class="hljs-keyword">return</span> (<span class="xml"><span class="hljs-tag"><></span>
    <span class="hljs-tag"><<span class="hljs-name">p</span>></span>&#123;state.todo&#125;<span class="hljs-tag"></<span class="hljs-name">p</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">p</span>></span>&#123;state.counter&#125;<span class="hljs-tag"></<span class="hljs-name">p</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">button</span> <span class="hljs-attr">onClick</span>=<span class="hljs-string">&#123;()</span> =></span> &#123;
    
      // 更新 state
        
      store.dispatch(&#123; type: 'counter/ADD', payload: 2 &#125;)
      
    &#125;&#125;>counter add<span class="hljs-tag"></<span class="hljs-name">button</span>></span>
  <span class="hljs-tag"></></span></span>)
&#125;

<span class="copy-code-btn">复制代码</span></code></pre>
<p><code>tips: dispatch 的 type 要唯一, 不然符合条件的都会触发</code></p>
<p><code>tips: 此时你会发现在更新数据方面,用起来贼不爽, 因此 react-redux应运而生 </code></p>
<h3 data-id="heading-5">Redux模型</h3>
<p><img src="https://cors.zfour.workers.dev/?http://cn.redux.js.org/assets/images/ReduxDataFlowDiagram-49fa8c3968371d9ef6f2a1486bd40a26.gif" alt loading="lazy" referrerpolicy="no-referrer"></p></div>  
</div>
            