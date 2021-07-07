
---
title: '简单的 hooks'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=1356'
author: 掘金
comments: false
date: Tue, 06 Jul 2021 02:04:56 GMT
thumbnail: 'https://picsum.photos/400/300?random=1356'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p><strong>1，为什么 react 要搞 hooks？</strong></p>
<p>想要复用一个有状态组件太麻烦，
react 的核心思想是将一个页面拆成多个可复用的组件，并且用由上而下的单项数据流形式将这些组件都串联起来。如果在大型项目中用 react，就会有很多react 组件冗长而难用，尤其是有状态的 class 组件。他们本身就包含了状态 state。所以就很难复用。</p>
<p>还有 class 函数生命周期和 this 指向问题，以及尽可能将组件写成无状态组件，但后期要获取状态是又要将 function 改成 class 就比较麻烦</p>
<p>如此 hooks 出现了
先看 demo</p>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-keyword">import</span> React, &#123; useState, useEffect &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'react'</span>;

<span class="hljs-comment">// 一个简单的hooks </span>
<span class="hljs-comment">/***
 * hooks 让一个函数变成了一个有状态函数。他有自己的状态（count），还可以更新自己的状态（setCount）,这就是注入的 hook---useState
 * hook 除了 useState 之外还有很多其他 hook 例如 useEffect 类似 componentDidMount 声明周期，useContext 提供上下文功能等
 *  只能在最顶层使用 hook，不能在条件，循环或者嵌套函数中使用 hook
 */</span>
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">Catalog</span> (<span class="hljs-params"></span>) </span>&#123;
    <span class="hljs-comment">// 由中括号解构</span>
    <span class="hljs-keyword">const</span> [count, setCount] = useState(<span class="hljs-number">0</span>) <span class="hljs-comment">//括号内为初始值</span>
    <span class="hljs-keyword">const</span> [fruit, setFruit] = useState(<span class="hljs-string">'banana'</span>)
    <span class="hljs-comment">//类似于 class 有状态组件内的 componentDidMount 和 componentDidUpDate</span>
    useEffect(<span class="hljs-function">()=></span>&#123;
        <span class="hljs-built_in">document</span>.title=<span class="hljs-string">`you click <span class="hljs-subst">$&#123;count&#125;</span> times`</span>
    &#125;)
    <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">content</span>(<span class="hljs-params"></span>)</span>&#123;
        setCount(count+<span class="hljs-number">1</span>)
        setFruit(<span class="hljs-string">"orange"</span>)
    &#125;
    <span class="hljs-keyword">return</span> (
        <span class="xml"><span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">className</span>=<span class="hljs-string">'content'</span>></span>
            <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">className</span>=<span class="hljs-string">'count'</span>></span>caltlog点击第&#123;count&#125;次<span class="hljs-tag"></<span class="hljs-name">div</span>></span>
            <span class="hljs-tag"><<span class="hljs-name">hr</span>/></span>
            <span class="hljs-tag"><<span class="hljs-name">div</span>></span>what is your like &#123;fruit&#125;<span class="hljs-tag"></<span class="hljs-name">div</span>></span>

            <span class="hljs-tag"><<span class="hljs-name">button</span> <span class="hljs-attr">className</span>=<span class="hljs-string">'button'</span> <span class="hljs-attr">onClick</span>=<span class="hljs-string">&#123;content&#125;</span>></span>catalogclick<span class="hljs-tag"></<span class="hljs-name">button</span>></span>
        <span class="hljs-tag"></<span class="hljs-name">div</span>></span></span>
    )
&#125;
<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> Catalog;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>如上useState 可以多次调用，而在多次调用中如何保证useState 是相互独立的？
他是根据 state 出现的顺序来定的</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">//第一次初始化</span>
useState(<span class="hljs-number">0</span>) <span class="hljs-comment">//初始化的 count 值</span>
useState(<span class="hljs-string">'banana'</span>) <span class="hljs-comment">//将 fruit 初始化值为 banana</span>

<span class="hljs-comment">//第二次渲染</span>
useState(<span class="hljs-number">0</span>) <span class="hljs-comment">//读取状态变量 count 值 （初始化的值被忽略）</span>
useState(<span class="hljs-string">' orange'</span>) <span class="hljs-comment">//读取状态变量 fruit （初始化值 banana被忽略）</span>


<span class="copy-code-btn">复制代码</span></code></pre>
<p>react 规定必须将 hooks 写在最外层，确保 hooks 按照顺序运行，否则就会报错</p>
<p><strong>2，什么是 Effect hooks</strong></p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-keyword">function</span>  <span class="hljs-title">count</span>(<span class="hljs-params"></span>) </span>&#123;
  <span class="hljs-keyword">const</span> [count, setCount] = useState(<span class="hljs-number">0</span>);

  useEffect(<span class="hljs-function">() =></span> &#123;
    <span class="hljs-built_in">document</span>.title = <span class="hljs-string">`You clicked <span class="hljs-subst">$&#123;count&#125;</span> times`</span>;
  &#125;);
  
<span class="copy-code-btn">复制代码</span></code></pre>
<p>例如上述代码中,useEffect 相当与 class 有状态组件中 componentDidMount，componentDidUpdate，componentWillUnmount 三个钩子函数。 我们给 useEffect 传入了一个匿名函数</p>
<p><strong>注意</strong> 1，react 首次渲染和之后的每次渲染都会调用 useEffect 函数。2，useEffect 中定义的副作用函数不会阻碍浏览器视图更新，也就是说他是异步执行的。</p>
<p>跳过一些副作用函数，只需要在 useEffect 中添加第二个参数，只有当第一个参数发生改变时才更新视图</p>
<pre><code class="hljs language-js copyable" lang="js">useEffect(<span class="hljs-function">() =></span> &#123;
    <span class="hljs-built_in">document</span>.title = <span class="hljs-string">`You clicked <span class="hljs-subst">$&#123;count&#125;</span> times`</span>;
  &#125;,[count]); <span class="hljs-comment">//只有count 发生变化时 title 这句才会发生变化</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>当第二个参数为空[]时，相当与仅在首次渲染时更新 count 未执行完毕，所以要减少这样使用可能会有 bug</p>
<p><strong>3.其他hooks，查阅<a href="https://zh-hans.reactjs.org/docs/hooks-custom.html" target="_blank" rel="nofollow noopener noreferrer">官方文档</a></strong></p></div>  
</div>
            