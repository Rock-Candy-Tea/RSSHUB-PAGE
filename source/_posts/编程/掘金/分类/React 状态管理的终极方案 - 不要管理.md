
---
title: 'React 状态管理的终极方案 - 不要管理'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=3722'
author: 掘金
comments: false
date: Thu, 03 Jun 2021 04:48:16 GMT
thumbnail: 'https://picsum.photos/400/300?random=3722'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>开发者普遍认为状态是组件的一部分, 但是同时却又在剥离状态上不停的造轮子, 这不是很矛盾么?</p>
<p>对于一个最简单的文本组件而言</p>
<pre><code class="hljs language-js copyable" lang="js">
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">Text</span>(<span class="hljs-params"></span>)</span>&#123;
  <span class="hljs-keyword">const</span> [text, setText] = useState(<span class="hljs-string">'载入'</span>)
  <span class="hljs-keyword">return</span> ()&#123;
    <span class="xml"><span class="hljs-tag"><<span class="hljs-name">p</span>></span>&#123;text&#125;<span class="hljs-tag"></<span class="hljs-name">p</span>></span></span>
  &#125;
&#125;

<span class="copy-code-btn">复制代码</span></code></pre>
<p>你觉得应该把 text 从 Text 组件中剥离么? 如果你的直觉告诉你不应该这么做, 那为何要使用 redux mobx jotai 等等一系列稀奇古怪的状态管理库来让我们的代码变得更复杂?</p>
<p>所以 why?</p>
<p>还不是 React 自己的锅!!!</p>
<p>因为 React 在组件状态上给出了双重定义, 内敛的 state 和开放的 props.
同时因为 jsx 的限制导致组件通信只能依赖 props.</p>
<p>有人会说还有 context, 但如果你为组件通信单独增加一层 provide, 那随着应用膨胀, 你的状态会被 xml 结构割得四分五裂, 最后只剩下单一 store 这颗有毒药丸.</p>
<p>因为 React 天生状态同步上的缺陷, 才让状态管理这件事在 React 社区如此发达, 这其实是病态的.</p>
<p>想想战国时期群雄逐鹿吧. 还不是周天子失仪, 看看 Vue 就没有这么多狗屁倒灶的事.</p>
<p>状态管理生态的病态繁荣让整个 React 生态变得混乱.</p>
<p>不同状态管理库之间潜在的集成成本, 以及围绕这些状态管理打造的组件库又需要考虑集成. 看看 Route5 吧, 我觉得官网的 React 和 Redux 集成方案根本不够. 毕竟还有好几个库在那等着呢...</p>
<p>从 React 自身角度来看, 只要解决两个问题, 就没有所谓的状态管理了.</p>
<h3 data-id="heading-0">组件内部通信</h3>
<p>jsx 下的组件结构无非两种, 包含和平级, 对于包含嵌套的结构, 单一 store 是可行的, 要解决的无非是内部的 jsx 片段之间如何共享和同步状态. 其实很简单只要给这些 jsx 片段绑定上一个共同的 context 就行了</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">import</span> &#123;createComponent&#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'structured-react-hook'</span>

<span class="hljs-keyword">const</span> Component = createComponent(&#123;
  <span class="hljs-attr">initState</span>:&#123;
    <span class="hljs-attr">A</span>:<span class="hljs-string">'A'</span>,
    <span class="hljs-attr">B</span>:<span class="hljs-string">'B'</span>,
    <span class="hljs-attr">M</span>:<span class="hljs-string">'M'</span>,
  &#125;,
  <span class="hljs-attr">view</span>:&#123;
    <span class="hljs-function"><span class="hljs-title">renderB</span>(<span class="hljs-params"></span>)</span>&#123;
      <span class="hljs-keyword">return</span>(
        <span class="xml"><span class="hljs-tag"><></span>
          <span class="hljs-tag"><<span class="hljs-name">div</span>></span>&#123;this.state.M&#125;<span class="hljs-tag"></<span class="hljs-name">div</span>></span>
          <span class="hljs-tag"><<span class="hljs-name">div</span>></span>&#123;this.state.B&#125;<span class="hljs-tag"></<span class="hljs-name">div</span>></span>
        <span class="hljs-tag"></></span></span>
      )
    &#125;,
    <span class="hljs-function"><span class="hljs-title">renderA</span>(<span class="hljs-params"></span>)</span>&#123;
      <span class="hljs-keyword">return</span>(
        <span class="xml"><span class="hljs-tag"><></span>
          <span class="hljs-tag"><<span class="hljs-name">div</span>></span>&#123;this.state.M&#125;<span class="hljs-tag"></<span class="hljs-name">div</span>></span>
          <span class="hljs-tag"><<span class="hljs-name">div</span>></span>&#123;this.state.A&#125;<span class="hljs-tag"></<span class="hljs-name">div</span>></span>
        <span class="hljs-tag"></></span></span>
      )
    &#125;,
    <span class="hljs-function"><span class="hljs-title">render</span>(<span class="hljs-params"></span>)</span>&#123;
      <span class="hljs-keyword">return</span>(
        <span class="xml"><span class="hljs-tag"><></span>
          <span class="hljs-tag"><<span class="hljs-name">div</span>></span>&#123;this.state.M&#125;<span class="hljs-tag"></<span class="hljs-name">div</span>></span>
          <span class="hljs-tag"><<span class="hljs-name">div</span>></span>&#123;this.view.renderB()&#125;<span class="hljs-tag"></<span class="hljs-name">div</span>></span>
          <span class="hljs-tag"><<span class="hljs-name">div</span>></span>&#123;this.view.renderA()&#125;<span class="hljs-tag"></<span class="hljs-name">div</span>></span>
        <span class="hljs-tag"></></span></span>
      )
    &#125;
  &#125;
&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>一个组件可以切分任一的 jsx 片段到 view 里, 同时将状态放在 initState 里管理, 在运行时让 render 函数的 this.state 指向 initState 就行了, 当然内部有些魔法, 这就不提了.</p>
<p>当然组件大了一定需要平行切割, 不然会遇到性能和维护上的问题. 对于平行组件如何让他们彼此共享和同步状态呢?</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> ComponentA = createComponent(&#123;
  <span class="hljs-attr">name</span>:<span class="hljs-string">'ComponentA'</span>,
  <span class="hljs-attr">initState</span>:&#123;
    <span class="hljs-attr">A</span>:<span class="hljs-string">'A'</span>
  &#125;,
  <span class="hljs-attr">view</span>:&#123;
    <span class="hljs-function"><span class="hljs-title">render</span>(<span class="hljs-params"></span>)</span>&#123;
      <span class="hljs-keyword">return</span>(
        <span class="xml"><span class="hljs-tag"><<span class="hljs-name">div</span>></span>&#123;this.combination.ComponentB.state.B&#125;<span class="hljs-tag"></<span class="hljs-name">div</span>></span></span>
      )
    &#125;
  &#125;
&#125;)

<span class="hljs-keyword">const</span> ComponentB = createComponent(&#123;
  <span class="hljs-attr">name</span>:<span class="hljs-string">'ComponentB'</span>,
  <span class="hljs-attr">initState</span>:&#123;
    <span class="hljs-attr">B</span>:<span class="hljs-string">'B'</span>
  &#125;,
  <span class="hljs-attr">view</span>:&#123;
    <span class="hljs-function"><span class="hljs-title">render</span>(<span class="hljs-params"></span>)</span>&#123;
      <span class="hljs-keyword">return</span>(
        <span class="xml"><span class="hljs-tag"><<span class="hljs-name">div</span>></span>&#123;this.combination.ComponentA.state.A&#125;<span class="hljs-tag"></<span class="hljs-name">div</span>></span></span>
      )
    &#125;
  &#125;
&#125;)

<span class="copy-code-btn">复制代码</span></code></pre>
<p>就这么简单, 只要让每个组件的实例能在彼此的 this 上互相感知, 操作和共享状态并不是难事.</p>
<p>这样对于 jsx 内平行的组件来说再也不需要为了通信而烦恼了. 无论跨越多少层, 最终我都会找到你.</p>
<p>所以解决这两个问题, 还需要额外的状态管理么?</p>
<p>至少在我看来状态管理是个伪命题, 组件和状态本身就是不可分割的一部分, 把状态视为组件的核心, 只要解决了组件的问题, 状态管理自然也就不是问题了</p>
<p>但是只要 React 官方不作为, 状态管理社区的病态繁荣还将继续持续下去...┓( ´∀` )┏</p></div>  
</div>
            