
---
title: '写给 Vue 开发的 React 上手指南'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=5757'
author: 掘金
comments: false
date: Sun, 18 Apr 2021 09:17:20 GMT
thumbnail: 'https://picsum.photos/400/300?random=5757'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h1 data-id="heading-0">写给 Vue 开发的 React 上手指南</h1>
<h2 data-id="heading-1">前言</h2>
<p>近年来前端框架 Angular、React 和 Vue 成为前端开发的主流，他们相比于 jQuery 封装了底层 DOM 操作，使开发者能够专注于业务数据，提升了开发体验。其中 React 和 Vue 的设计思路有异曲同工之妙，作为双修玩家，想写点东西用来沉淀自己的对于单项数据流、函数式组件和虚拟 DOM 等概念。</p>
<p>本文适合以下类型的读者：</p>
<ul>
<li>被上司逼着换框架的 Vue 程序猿</li>
<li>精力旺盛想尝试 React 的 Vue 程序猿</li>
<li>Vue 、 React 浅度使用，想深入了解其中一项的程序猿</li>
</ul>
<p>阅读本文需要掌握以下知识：</p>
<ul>
<li>理解 this 指向</li>
<li>理解 ES6 的 class 、 解构赋值和箭头函数等语法</li>
</ul>
<p>另外，如果觉得看文档更加方便，这里提供传送门： <a href="https://reactjs.org/docs/getting-started.html" target="_blank" rel="nofollow noopener noreferrer">reactjs.org/docs/gettin…</a></p>
<h2 data-id="heading-2">React 简介</h2>
<p>来看看官网如何用一句话介绍 React：</p>
<blockquote>
<p>一个构建用户界面的 JavaScript 库</p>
</blockquote>
<p>官方把 React 定义为一个 “UI 库” 而非框架，意思是 React 专注于使用 JavaScript 渲染用户界面（跟 UI 无关的东西不是我的本行） 库也好，框架也罢，能实现功能就是好东西，下面开始对比</p>
<h2 data-id="heading-3">直观对比</h2>
<p><strong>Talk is cheap, show you the code</strong>
让我们分别用两种框架实现一个购物车展示列表<br>
使用 Vue 可以这么写：</p>
<pre><code class="hljs language-jsx copyable" lang="jsx"><template>
  <span class="xml"><span class="hljs-tag"><<span class="hljs-name">div</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">h3</span>></span>&#123;&#123; title &#125;&#125;<span class="hljs-tag"></<span class="hljs-name">h3</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">ul</span>></span>
      <span class="hljs-tag"><<span class="hljs-name">li</span> <span class="hljs-attr">v-for</span>=<span class="hljs-string">"i in cart"</span> <span class="hljs-attr">:key</span>=<span class="hljs-string">"i.name"</span>></span>
        <span class="hljs-tag"><<span class="hljs-name">span</span>></span>&#123;&#123; i.name &#125;&#125; - &#123;&#123; i.price &#125;&#125;<span class="hljs-tag"></<span class="hljs-name">span</span>></span>
      <span class="hljs-tag"></<span class="hljs-name">li</span>></span>
    <span class="hljs-tag"></<span class="hljs-name">ul</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">p</span>></span>总价： &#123;&#123; total &#125;&#125;<span class="hljs-tag"></<span class="hljs-name">p</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">button</span> @<span class="hljs-attr">click</span>=<span class="hljs-string">"settle"</span>></span>结账<span class="hljs-tag"></<span class="hljs-name">button</span>></span>
  <span class="hljs-tag"></<span class="hljs-name">div</span>></span></span>
</template>
<span class="xml"><span class="hljs-tag"><<span class="hljs-name">script</span>></span><span class="javascript">
<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> &#123;
  <span class="hljs-attr">props</span>: &#123;
    <span class="hljs-attr">title</span>: <span class="hljs-built_in">String</span>
  &#125;,
  <span class="hljs-function"><span class="hljs-title">data</span>(<span class="hljs-params"></span>)</span> &#123;
    <span class="hljs-keyword">return</span> &#123;
      <span class="hljs-attr">cart</span>: [
            &#123;<span class="hljs-attr">name</span>: <span class="hljs-string">'牙膏'</span>, <span class="hljs-attr">price</span>: <span class="hljs-number">6.5</span>&#125;,
            &#123;<span class="hljs-attr">name</span>: <span class="hljs-string">'香皂'</span>, <span class="hljs-attr">price</span>: <span class="hljs-number">16</span>&#125;,
            &#123;<span class="hljs-attr">name</span>: <span class="hljs-string">'洗发水'</span>, <span class="hljs-attr">price</span>: <span class="hljs-number">19.5</span>&#125;,
      ]
    &#125;
  &#125;,
  <span class="hljs-attr">computed</span>: &#123;
    <span class="hljs-function"><span class="hljs-title">total</span>(<span class="hljs-params"></span>)</span> &#123;
      <span class="hljs-keyword">return</span> <span class="hljs-built_in">this</span>.cart.reduce(<span class="hljs-function">(<span class="hljs-params"> prev, curr </span>) =></span> prev + curr.price, <span class="hljs-number">0</span>)
    &#125;
  &#125;,
  <span class="hljs-attr">methods</span>: &#123;
    <span class="hljs-function"><span class="hljs-title">settle</span>(<span class="hljs-params"></span>)</span> &#123;
      alert(<span class="hljs-string">`下单成功，总价: <span class="hljs-subst">$&#123;<span class="hljs-built_in">this</span>.total&#125;</span>`</span>)
    &#125;
  &#125;,
&#125;
</span><span class="hljs-tag"></<span class="hljs-name">script</span>></span></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>emmm，数据视图分离、data、computed ...， 多么熟悉的画面，把这段逻辑挪到 React 中，它长这样：</p>
<pre><code class="hljs language-jsx copyable" lang="jsx"><span class="hljs-keyword">import</span> React, &#123; Component &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'react'</span>;
<span class="hljs-keyword">import</span> PropTypes <span class="hljs-keyword">from</span> <span class="hljs-string">'prop-types'</span>;

<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> <span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Cart</span> <span class="hljs-keyword">extends</span> <span class="hljs-title">Component</span> </span>&#123;
  <span class="hljs-comment">// 属性类型检查</span>
  <span class="hljs-keyword">static</span> propTypes = &#123;
    <span class="hljs-attr">title</span>: PropTypes.string;
  &#125;
  <span class="hljs-comment">// 组件的状态</span>
  state = &#123;
    <span class="hljs-attr">cart</span>: [
      &#123; <span class="hljs-attr">name</span>: <span class="hljs-string">'牙膏'</span>, <span class="hljs-attr">price</span>: <span class="hljs-number">6.5</span> &#125;,
      &#123; <span class="hljs-attr">name</span>: <span class="hljs-string">'香皂'</span>, <span class="hljs-attr">price</span>: <span class="hljs-number">16</span> &#125;,
      &#123; <span class="hljs-attr">name</span>: <span class="hljs-string">'洗发水'</span>, <span class="hljs-attr">price</span>: <span class="hljs-number">19.5</span> &#125;,
    ]
  &#125;
  <span class="hljs-comment">// 计算总价</span>
  total = <span class="hljs-function">() =></span> <span class="hljs-built_in">this</span>.state.cart.reduce(<span class="hljs-function">(<span class="hljs-params">prev, curr</span>) =></span> prev + curr.price, <span class="hljs-number">0</span>)
  <span class="hljs-comment">// 结账回调</span>
  settle = <span class="hljs-function">() =></span> &#123;
    alert(<span class="hljs-string">`下单成功，总价: <span class="hljs-subst">$&#123;<span class="hljs-built_in">this</span>.total()&#125;</span>`</span>)
  &#125;

  <span class="hljs-comment">// 渲染视图</span>
  <span class="hljs-function"><span class="hljs-title">render</span>(<span class="hljs-params"></span>)</span> &#123;
    <span class="hljs-keyword">const</span> &#123;
      <span class="hljs-attr">props</span>: &#123; title &#125;,
      <span class="hljs-attr">state</span>: &#123; cart &#125;,
      total,
      settle
    &#125; = <span class="hljs-built_in">this</span>;

    <span class="hljs-comment">// JSX 模板</span>
    <span class="hljs-keyword">return</span> (
      <span class="xml"><span class="hljs-tag"><<span class="hljs-name">div</span>></span>
        <span class="hljs-tag"><<span class="hljs-name">h3</span>></span>&#123;title&#125;<span class="hljs-tag"></<span class="hljs-name">h3</span>></span>
        <span class="hljs-tag"><<span class="hljs-name">ul</span>></span>
          &#123;
            cart.map((i) => (
              <span class="hljs-tag"><<span class="hljs-name">li</span> <span class="hljs-attr">key</span>=<span class="hljs-string">&#123;i.name&#125;</span>></span>
                <span class="hljs-tag"><<span class="hljs-name">span</span>></span>&#123;i.name&#125; - &#123;i.price&#125;<span class="hljs-tag"></<span class="hljs-name">span</span>></span>
              <span class="hljs-tag"></<span class="hljs-name">li</span>></span>
            ))
          &#125;
        <span class="hljs-tag"></<span class="hljs-name">ul</span>></span>
        <span class="hljs-tag"><<span class="hljs-name">p</span>></span>总价： &#123;total&#125;<span class="hljs-tag"></<span class="hljs-name">p</span>></span>
        <span class="hljs-tag"><<span class="hljs-name">button</span> <span class="hljs-attr">onClick</span>=<span class="hljs-string">&#123;settle&#125;</span>></span>结账<span class="hljs-tag"></<span class="hljs-name">button</span>></span>
      <span class="hljs-tag"></<span class="hljs-name">div</span>></span></span>
    )
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>hmmm, 除了 JSX （见下文），其他都是纯粹的 JavaScript，通过以上代码的对比，我们发现了几个信息：</p>
<ol>
<li>两个框架中模板、数据和回调这几个要素非常相似： <code>render</code> 函数对应 Vue 的 Template （提一嘴， Vue 也可以使用 JSX 编写 render 函数）； <code>state</code> 对应 Vue 中的 <code>data</code> 表示组件的状态； 而 <code>props</code> 意思相同，为父组件传下来的数据。</li>
<li>从写法上来说，React 偏 JavaScript ，Vue 则是 HTML 与 JavaScript 的结合，内置许多指令属性。</li>
<li>React 使用了 JSX 作为模板， JSX 语法相对比较简单，基本就是元素<code></></code> + 表达式<code>&#123;&#125;</code>，相比 Vue 中 Template 集中编写，JSX 可以写得比较松散。</li>
</ol>
<p>如果你倾向于 All in JavaScript ，追求代码的灵活度，那么 React 可能和你更有缘分。</p>
<h2 data-id="heading-4">详细对比</h2>
<p>上文说到 React 相对灵活，但灵活是把双刃剑，使用不当容易掉进坑里。尽管 React 社区生态非常丰富，可以帮你解决绝大部分问题，但有些东西和 Vue 不太一样，刚上手的人要留意。下面我将罗列几个与 Vue 不相同的地方：</p>
<h3 data-id="heading-5">创建虚拟 DOM —— JSX vs Template</h3>
<p>虚拟 DOM 的本质是 JavaScript 对象，使用 JavaScript 对象来描述真实 DOM，在数据变化更新时可以进行一定程度得优化，避免真实 DOM 的冗余更新。我们创建 React 的虚拟 DOM ，如果使用原生 JavaScript 会写成：</p>
<pre><code class="copyable">const myButton = React.createElement(
    'button', 
    &#123; onClick: () => doSth() &#125;, 
    'Hello World'
)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这么写很难让人看出来是在创建一个 HTML 元素。<br>
<strong>JSX</strong> 是一种 JavaScript 的语法扩展，借助 JSX 我们可以把上面的 button 元素写得更像 HTML：</p>
<pre><code class="hljs language-jsx copyable" lang="jsx"><span class="hljs-keyword">const</span> myButton = (
    <span class="xml"><span class="hljs-tag"><<span class="hljs-name">button</span> <span class="hljs-attr">onClick</span>=<span class="hljs-string">&#123;()</span> =></span> doSth()&#125;>
        Hello World
    <span class="hljs-tag"></<span class="hljs-name">button</span>></span></span>
)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>相比于 Template ，JSX 就显得比较简单纯粹了，在 Template 中可以使用各种便利的指令，而在 JSX 中只有属性 prop，没有指令这个概念，来看看具体有何不同：</p>
<h4 data-id="heading-6">表单绑定</h4>
<p>Tempalte 中一条 v-model 搞定</p>
<pre><code class="hljs language-jsx copyable" lang="jsx"><input v-model=<span class="hljs-string">"value"</span>/>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>JSX 中，老老实实展开来写吧</p>
<pre><code class="hljs language-jsx copyable" lang="jsx"><input value=&#123;value&#125; onChange=&#123;onChange&#125;/>
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-7">条件渲染</h4>
<pre><code class="hljs language-jsx copyable" lang="jsx"><div v-<span class="hljs-keyword">if</span>=<span class="hljs-string">"show"</span>>Should I render?</div>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>JSX 中花括号 <code>&#123;&#125;</code> 内可以写三目表达式，用它来替代条件渲染</p>
<pre><code class="hljs language-jsx copyable" lang="jsx">&#123;
  show ? <span class="xml"><span class="hljs-tag"><<span class="hljs-name">div</span>></span>Should I render?<span class="hljs-tag"></<span class="hljs-name">div</span>></span></span> : <span class="hljs-literal">null</span>
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>或者封装一个 <code><If /></code> 高阶函数（似乎这么做的人不多）：</p>
<pre><code class="hljs language-jsx copyable" lang="jsx"><span class="hljs-keyword">const</span> If = <span class="hljs-function">(<span class="hljs-params">props</span>) =></span> props.condition ? props.children : <span class="hljs-literal">null</span>;

<span class="xml"><span class="hljs-tag"><<span class="hljs-name">If</span> <span class="hljs-attr">condition</span>=<span class="hljs-string">&#123;show&#125;</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">div</span>></span>Should I render ?<span class="hljs-tag"></<span class="hljs-name">div</span>></span>
<span class="hljs-tag"></<span class="hljs-name">If</span>></span></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p><code>props.children</code> 为子节点渲染，参考下文</p>
<h4 data-id="heading-8">子节点渲染</h4>
<p>Template 中需要使用 slot 作为占位：</p>
<pre><code class="hljs language-jsx copyable" lang="jsx"><div> <span class="hljs-built_in">this</span> is <span class="hljs-keyword">default</span> <slot><<span class="hljs-regexp">/slot> </</span>div>
<div> <span class="hljs-built_in">this</span> is named <slot name=<span class="hljs-string">"bar"</span>></slot><div>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>父节点传入：</p>
<pre><code class="hljs language-jsx copyable" lang="jsx"><Foo>
    <span class="xml"><span class="hljs-tag"><<span class="hljs-name">span</span>></span> child node <span class="hljs-tag"></<span class="hljs-name">span</span>></span></span>
</Foo>

<span class="xml"><span class="hljs-tag"><<span class="hljs-name">Foo</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">span</span> <span class="hljs-attr">slot</span>=<span class="hljs-string">"bar"</span>></span> bar node <span class="hljs-tag"></<span class="hljs-name">span</span>></span>
<span class="hljs-tag"></<span class="hljs-name">Foo</span>></span></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>JSX 中直接将节点当作 prop 传入即可，默认子节点会被转换成 <code>children</code> prop</p>
<pre><code class="hljs language-jsx copyable" lang="jsx"><div> <span class="hljs-built_in">this</span> will render &#123; props.children &#125; </div>
<span class="xml"><span class="hljs-tag"><<span class="hljs-name">div</span>></span> this will render &#123; props.whatever &#125; <span class="hljs-tag"></<span class="hljs-name">div</span>></span></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>父节点传入</p>
<pre><code class="hljs language-jsx copyable" lang="jsx"><Foo>
    <span class="xml"><span class="hljs-tag"><<span class="hljs-name">span</span>></span> child node <span class="hljs-tag"></<span class="hljs-name">span</span>></span></span>
</Foo>

<span class="xml"><span class="hljs-tag"><<span class="hljs-name">Foo</span> <span class="hljs-attr">whatever</span>=<span class="hljs-string">&#123;</span><<span class="hljs-attr">div</span>></span>text, nodes or any valid element<span class="hljs-tag"></<span class="hljs-name">div</span>></span>&#125; /></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-9">列表渲染</h4>
<p>为了优化列表更新的性能，我们在每个元素上声明一个 <code>key</code> 属性，这一点两家都一样：</p>
<pre><code class="hljs language-jsx copyable" lang="jsx"><ul>
    <span class="xml"><span class="hljs-tag"><<span class="hljs-name">li</span> <span class="hljs-attr">v-for</span>=<span class="hljs-string">"i in list"</span> <span class="hljs-attr">:key</span>=<span class="hljs-string">"i.id"</span>></span>&#123;i.name&#125;<span class="hljs-tag"></<span class="hljs-name">li</span>></span></span>
</ul>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>JSX 中因为不能使用 <code>for</code> 语句，得利用 Array map 进行渲染:</p>
<pre><code class="hljs language-jsx copyable" lang="jsx"><ul>
    &#123; list.map(<span class="hljs-function"><span class="hljs-params">i</span> =></span> <span class="xml"><span class="hljs-tag"><<span class="hljs-name">li</span> <span class="hljs-attr">key</span>=<span class="hljs-string">&#123;i.id&#125;</span>></span>&#123;i.name&#125;<span class="hljs-tag"></<span class="hljs-name">li</span>></span></span>) &#125;
</ul>
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-10">碎片渲染</h4>
<p>声明 JSX 节点，根元素必须唯一，像以下的写法是不行的：</p>
<pre><code class="copyable">const badNode = (
    <div>1</div>
    <div>2</div>
)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>如果不希望添加多余的 DOM 元素，可以使用 React 碎片</p>
<pre><code class="copyable">const frag = (
  <React.Fragment>
    <div>1</div>
    <div>2</div>
  </React.Fragment>
)

//  或者简写成：
const frag = (
  <>
    <div>1</div>
    <div>2</div>
  </>
)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>在 Vue 中 Template 的使用相对集中，碰到碎片化渲染的场景不多，但也有类似的场景，比如对一组元素做循环：</p>
<pre><code class="copyable"><template v-for="i in item" :key="i.id">
  <h3>&#123;&#123;i.title&#125;&#125;</h3>
  <p>&#123;&#123;i.name&#125;&#125;</p>
</template>
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-11">一言难尽的 this</h3>
<p>这个是 JavaScript 的问题，框架不背锅。Vue 中，不管是在 <code>data</code> 、 <code>computed / watch</code> 还是 <code>methods</code> 中，<code>this</code> 始终指向当前组件，这是因为 Vue 在创建组件的时候帮你做了一次绑定。 而 React 就没那么贴心了（灵活嘛），这里有一段代码：</p>
<pre><code class="hljs language-jsx copyable" lang="jsx"><span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Comp</span> <span class="hljs-keyword">extends</span> <span class="hljs-title">Component</span> </span>&#123;
  state = &#123;
    <span class="hljs-attr">a</span>: <span class="hljs-number">1</span>
  &#125;

  <span class="hljs-function"><span class="hljs-title">printA</span>(<span class="hljs-params"></span>)</span> &#123;
    <span class="hljs-built_in">console</span>.log(<span class="hljs-built_in">this</span>.state.a); <span class="hljs-comment">// "this" is undefined</span>
  &#125;

  <span class="hljs-function"><span class="hljs-title">render</span>(<span class="hljs-params"></span>)</span> &#123;
    <span class="hljs-keyword">return</span> (
      <span class="xml"><span class="hljs-tag"><<span class="hljs-name">button</span> <span class="hljs-attr">onClick</span>=<span class="hljs-string">&#123;this.printA&#125;</span>></span>Click<span class="hljs-tag"></<span class="hljs-name">button</span>></span></span>
    )
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>React 的行家一眼就能发现问题： 当点击 button 的时候，<code>printA</code> 方法中的 <code>this</code> 并不是指向当前组件，所以执行 <code>printA</code> 会报错。为了保证 <code>this</code> 指向，你可以从以下三个选项中挑一个来解决：</p>
<ul>
<li>解法一：使用箭头函数（推荐） 利用箭头函数绑定上一层 this 的原理，可以将成员函数转成箭头函数：</li>
</ul>
<pre><code class="hljs language-jsx copyable" lang="jsx"><span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Comp</span> <span class="hljs-keyword">extends</span> <span class="hljs-title">Component</span> </span>&#123;
  printA = <span class="hljs-function">() =></span> &#123;
    <span class="hljs-built_in">console</span>.log(<span class="hljs-built_in">this</span>.state.a);
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>或者在 render 函数一头处理，不过每次重渲染都会创建一个新的箭头函数：</p>
<pre><code class="hljs language-jsx copyable" lang="jsx"><button onClick=<span class="hljs-string">"() => this.printA()"</span>>Click</button>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这种解法在编写 class 组件时心智负担相对比较小。</p>
<ul>
<li>解法二： 使用 bind 改变 this 指向，和上面的问题一样：每次重渲染都会创建一个新的函数：</li>
</ul>
<pre><code class="hljs language-jsx copyable" lang="jsx"><button onClick=<span class="hljs-string">"this.printA.bind(this)"</span>>Click</button>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>或者在 <code>constructor</code> 中处理，保证每次引用一样</p>
<pre><code class="hljs language-jsx copyable" lang="jsx"><span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Comp</span> <span class="hljs-keyword">extends</span> <span class="hljs-title">Component</span> </span>&#123;
  <span class="hljs-function"><span class="hljs-title">constructor</span>(<span class="hljs-params">props</span>)</span> &#123;
    <span class="hljs-built_in">super</span>(props);
    <span class="hljs-built_in">this</span>.printA = <span class="hljs-built_in">this</span>.printA.bind(<span class="hljs-built_in">this</span>);
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>解法三：使用函数组件（推荐）</li>
</ul>
<p>既然 this 这么麻烦，咱不用 class 组件了可好？答案是可行的，React 16.8 之后开始支持 <strong>React Hooks</strong> ，可以使用函数组件替代 class 组件，不用再纠结 this 了！参见下文 <strong>React Hooks</strong></p>
<h3 data-id="heading-12">Immutable 不可变特性</h3>
<p>第一次看到这个概念，本人也很懵：状态时刻都在变化，为什么说不可变呢？ 这里的不可变，是函数式编程的一个理念（过于深入，不做讲解）：假设把 React 组件比作函数，那么每次更新组件都不要直接修改 state 里的数据，而是生成一个新的 state 来替换。我们在 Vue 中习惯了响应式更新，修改状态时直接赋值：</p>
<pre><code class="hljs language-jsx copyable" lang="jsx"><span class="hljs-built_in">this</span>.state.cart[<span class="hljs-number">1</span>].price = <span class="hljs-number">5.5</span>;
<span class="hljs-built_in">this</span>.state.cart.push(&#123; <span class="hljs-attr">name</span>: <span class="hljs-string">'毛巾'</span>, <span class="hljs-attr">price</span>: <span class="hljs-number">32.9</span> &#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>React 告诉你： Don't do that! 我为你提供了 <code>setState</code> 方法，调了我的 <code>setState</code> ，并且新值和旧值不相等（<code>Object.is(oldVal, newVal)</code>）我才认为你修改了状态：</p>
<pre><code class="hljs language-jsx copyable" lang="jsx"><span class="hljs-comment">// 修改第一项的 price</span>
<span class="hljs-built_in">this</span>.setState(&#123;
  <span class="hljs-attr">cart</span>: <span class="hljs-built_in">this</span>.state.cart.map(<span class="hljs-function">(<span class="hljs-params">item, index</span>) =></span> index === <span class="hljs-number">1</span> ? &#123; ...item, <span class="hljs-attr">price</span>: <span class="hljs-number">5.5</span> &#125; : item)
&#125;)

<span class="hljs-comment">// 添加一个商品</span>
<span class="hljs-built_in">this</span>.setState(&#123;
  <span class="hljs-attr">cart</span>: [...this.state.cart, &#123; <span class="hljs-attr">name</span>: <span class="hljs-string">'毛巾'</span>, <span class="hljs-attr">price</span>: <span class="hljs-number">32.9</span> &#125;]
&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>可以看到，除了调用 <code>setState</code> 方法，新数据与原数据的引用是不一样的，为的是让 React 比对旧值是发现数据的变化，从而触发更新。</p>
<blockquote>
<p>会不会有性能问题?</p>
</blockquote>
<p>比起 JS 引擎创建对象这种开销，不如关心一下你的 JS 文件体积过大影响加载以及 DOM 更新的粒度？</p>
<h3 data-id="heading-13">单向数据流</h3>
<p>这个简单，子组件不要直接修改父组件的状态：</p>
<pre><code class="hljs language-jsx copyable" lang="jsx"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">MyInput</span>(<span class="hljs-params">&#123; value, onChange &#125;</span>) </span>&#123;
  <span class="hljs-keyword">return</span> (
    <span class="xml"><span class="hljs-tag"><<span class="hljs-name">input</span>
      <span class="hljs-attr">placeHolder</span>=<span class="hljs-string">"type something"</span>
      <span class="hljs-attr">value</span>=<span class="hljs-string">&#123;value&#125;</span>
      <span class="hljs-attr">onChange</span>=<span class="hljs-string">&#123;e</span> =></span> onChange(e.target.value)&#125;/></span>
  )
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这一点上， Vue 的一个折中的办法是：把 value 和 onChange 封装成 v-model （抱歉，template 编译就是可以为所欲为），但原理是一样的：</p>
<pre><code class="hljs language-jsx copyable" lang="jsx"><template>
  <span class="xml"><span class="hljs-tag"><<span class="hljs-name">input</span> <span class="hljs-attr">placeholder</span>=<span class="hljs-string">"type something"</span> <span class="hljs-attr">value</span>=<span class="hljs-string">"value"</span> @<span class="hljs-attr">change</span>=<span class="hljs-string">"e => onChange(e.target.value)"</span> /></span></span>
</template>
<span class="xml"><span class="hljs-tag"><<span class="hljs-name">script</span>></span><span class="javascript">
  <span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> &#123;
    <span class="hljs-attr">model</span>: &#123;
      <span class="hljs-attr">value</span>: <span class="hljs-string">'value'</span>,
      <span class="hljs-attr">event</span>: <span class="hljs-string">'change'</span>
  &#125;
&#125;
</span><span class="hljs-tag"></<span class="hljs-name">script</span>></span></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-14">生命周期钩子</h3>
<p>组件不是一个持久化的东西，从创建、更新到销毁，每一个 timing 都可以处理一些逻辑：</p>
<ul>
<li><code>constructor</code>: 对应 Vue 中的 <code>data</code> 函数（想必你们都知道 Vue 的 data 得写成一个函数吧），我想来想去，把它与 <code>data</code> 对比最合适，因为在 <code>constructor</code> 中可以初始化组件的
state 。</li>
<li><code>componentDidMount</code>: 对应 Vue 中的 <code>mounted</code>，第一次渲染时调用，可以在该函数内发起初始化异步请求什么的。</li>
<li><code>componentDidUpdate</code>: 对应 Vue 中的 <code>updated</code>，组件更新（除了第一次渲染）时调用，处理 state 和 props 更新后的逻辑。</li>
<li><code>componentWillUnmount</code>: 对应 Vue 中的 <code>beforeDestroy</code>，组件卸载之前调用，一般用来取消定时器、退订事件等。</li>
<li><code>shouldComponentUpdate</code>: React 独有，根据传入的 props、state 的变化，返回 <code>true</code> 或者 <code>false</code> 来决定组件是否更新，有利于减少重渲染带来的性能开销和副作用。</li>
</ul>
<p>剩下一些不常用的，可以移步文档 <a href="https://reactjs.org/docs/react-component.html#rarely-used-lifecycle-methods" target="_blank" rel="nofollow noopener noreferrer">reactjs.org/docs/react-…</a></p>
<p>React 生命周期函数名称都比较长，不是什么技术原因，主要是为了保持一个提醒的作用：哦，原来这里用了这么个钩子。</p>
<h2 data-id="heading-15">特性</h2>
<p>讲完了对比，接下来介绍一些 React 的优势项</p>
<h3 data-id="heading-16">Typescript 支持</h3>
<p>由于 React 偏 JavaScript ，对 TypeScript 的支持是强于 Vue2.x 的（Vue 在 3.x 以上版本对 TS 支持有所改进），如果你理解静态类型检查对于复杂前端工程的意义，那么 React 是一个非常合适的选择。让我们使用 TypeScript 对 React Class 组件进行类型标注：</p>
<pre><code class="hljs language-typescript copyable" lang="typescript"><span class="hljs-keyword">import</span> React, &#123; Component &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'react'</span>;

<span class="hljs-keyword">interface</span> IProp &#123;
  <span class="hljs-attr">title</span>: <span class="hljs-built_in">string</span>;
&#125;

<span class="hljs-keyword">interface</span> IState &#123;
  <span class="hljs-attr">foo</span>: <span class="hljs-built_in">number</span>;
  bar: <span class="hljs-built_in">string</span>;
  baz: <span class="hljs-built_in">string</span>[];
&#125;

<span class="hljs-comment">// 第一个泛型表示组件中有哪些 Props ， 第二个表示组件的 State</span>
<span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Comp</span> <span class="hljs-keyword">extends</span> <span class="hljs-title">Component</span><<span class="hljs-title">IProp</span>, <span class="hljs-title">IState</span>> </span>&#123;
    state = &#123;
        <span class="hljs-attr">foo</span>: <span class="hljs-number">0</span>,
        <span class="hljs-attr">bar</span>: <span class="hljs-string">'bar'</span>,
        <span class="hljs-attr">baz</span>: [<span class="hljs-string">'ak'</span>, <span class="hljs-string">'m16'</span>, <span class="hljs-string">'famas'</span>]
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>有了静态类型除了能够对代码加强约束，还能让 IDE 放心地推导类型，给予合适的代码补全，可谓一次编写，处处受益。有关 TypeScript 支持请参考 <a href="https://zh-hans.reactjs.org/docs/static-type-checking.html#typescript" target="_blank" rel="nofollow noopener noreferrer">zh-hans.reactjs.org/docs/static…</a> 。</p>
<h3 data-id="heading-17">React Hooks —— 函数式组件补完计划</h3>
<p>事实上，除了上文使用 class 创建组件，也可以使用函数创建，并且 React 团队鼓励大家使用函数编写组件，继续折腾购物车，这回使用函数来组织代码：</p>
<pre><code class="hljs language-jsx copyable" lang="jsx"><span class="hljs-keyword">import</span> React <span class="hljs-keyword">from</span> <span class="hljs-string">'react'</span>;

<span class="hljs-keyword">const</span> defaultCart = [
  &#123; <span class="hljs-attr">name</span>: <span class="hljs-string">'牙膏'</span>, <span class="hljs-attr">price</span>: <span class="hljs-number">6.5</span> &#125;,
  &#123; <span class="hljs-attr">name</span>: <span class="hljs-string">'香皂'</span>, <span class="hljs-attr">price</span>: <span class="hljs-number">16</span> &#125;,
  &#123; <span class="hljs-attr">name</span>: <span class="hljs-string">'洗发水'</span>, <span class="hljs-attr">price</span>: <span class="hljs-number">19.5</span> &#125;,
]

<span class="hljs-comment">// 第一个参数为函数组件的 prop</span>
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">Cart</span>(<span class="hljs-params">&#123; title, cart = defaultCart &#125;</span>) </span>&#123;

  <span class="hljs-keyword">const</span> total = cart.reduce(<span class="hljs-function">(<span class="hljs-params">prev, curr</span>) =></span> prev + curr.price, <span class="hljs-number">0</span>);

  <span class="hljs-keyword">const</span> settle = <span class="hljs-function">() =></span> &#123;
    alert(<span class="hljs-string">`下单成功，总价: <span class="hljs-subst">$&#123;total&#125;</span>`</span>)
  &#125;

  <span class="hljs-keyword">return</span> (
    <span class="xml"><span class="hljs-tag"><<span class="hljs-name">div</span>></span>
      <span class="hljs-tag"><<span class="hljs-name">h3</span>></span>&#123;title&#125;<span class="hljs-tag"></<span class="hljs-name">h3</span>></span>
      <span class="hljs-tag"><<span class="hljs-name">ul</span>></span>
        &#123;
          cart.map((i) => (
            <span class="hljs-tag"><<span class="hljs-name">li</span> <span class="hljs-attr">key</span>=<span class="hljs-string">&#123;i.name&#125;</span>></span>
              <span class="hljs-tag"><<span class="hljs-name">span</span>></span>&#123;i.name&#125; - &#123;i.price&#125;<span class="hljs-tag"></<span class="hljs-name">span</span>></span>
            <span class="hljs-tag"></<span class="hljs-name">li</span>></span>
          ))
        &#125;
      <span class="hljs-tag"></<span class="hljs-name">ul</span>></span>
      <span class="hljs-tag"><<span class="hljs-name">p</span>></span>总价： &#123;total&#125;<span class="hljs-tag"></<span class="hljs-name">p</span>></span>
      <span class="hljs-tag"><<span class="hljs-name">button</span> <span class="hljs-attr">onClick</span>=<span class="hljs-string">&#123;settle&#125;</span>></span>结账<span class="hljs-tag"></<span class="hljs-name">button</span>></span>
    <span class="hljs-tag"></<span class="hljs-name">div</span>></span></span>
  );
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>函数组件当中，第一个参数为父组件传入的 <code>props</code>， 问题来了：<strong>state 怎么办</strong>？目前我们的函数组件仅支持静态渲染，如果需要修改购物车的状态，不得不再引入一个 onChange 的 prop ，由父组件修改。有没有方法能让函数拥有自己的 state 呢？</p>
<p>答案是使用 <strong>React Hooks</strong>，它们是 React 内置的一组钩子函数（跟生命周期钩子有所区别，可以从零开始理解），函数名称以 <code>use</code> 起头。能够将状态与当前渲染的函数组件“关联”起来，且看：</p>
<pre><code class="hljs language-jsx copyable" lang="jsx"><span class="hljs-keyword">import</span> React, &#123; useState &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'react'</span>;

<span class="hljs-keyword">const</span> Cart = <span class="hljs-function">(<span class="hljs-params">&#123; title &#125;</span>) =></span> &#123;
  <span class="hljs-comment">// 状态：购物车清单</span>
  <span class="hljs-keyword">const</span> [cart, setCart] = useState([
    &#123; <span class="hljs-attr">name</span>: <span class="hljs-string">"牙膏"</span>, <span class="hljs-attr">price</span>: <span class="hljs-number">6.5</span> &#125;,
    &#123; <span class="hljs-attr">name</span>: <span class="hljs-string">"香皂"</span>, <span class="hljs-attr">price</span>: <span class="hljs-number">16</span> &#125;,
    &#123; <span class="hljs-attr">name</span>: <span class="hljs-string">"洗发水"</span>, <span class="hljs-attr">price</span>: <span class="hljs-number">19.5</span> &#125;
  ]);
  <span class="hljs-comment">// 状态：新增货品名称</span>
  <span class="hljs-keyword">const</span> [name, setName] = useState(<span class="hljs-string">""</span>);
  <span class="hljs-comment">// 状态：新增货品价格</span>
  <span class="hljs-keyword">const</span> [price, setPrice] = useState();

  <span class="hljs-keyword">const</span> addItem = <span class="hljs-function">() =></span> &#123;
    setCart([...cart, &#123; name, price &#125;]);
  &#125;;

  <span class="hljs-keyword">const</span> clearAll = <span class="hljs-function">() =></span> &#123;
    <span class="hljs-keyword">if</span> (confirm(<span class="hljs-string">"是否删除购物车里的商品?"</span>)) &#123;
      setCart([]);
    &#125;
  &#125;;

  <span class="hljs-keyword">const</span> total = cart.reduce(<span class="hljs-function">(<span class="hljs-params">prev, curr</span>) =></span> +prev + +curr.price, <span class="hljs-number">0</span>);

  <span class="hljs-keyword">const</span> settle = <span class="hljs-function">() =></span> &#123;
    alert(<span class="hljs-string">`下单成功，总价: <span class="hljs-subst">$&#123;total&#125;</span>`</span>);
  &#125;;

  <span class="hljs-keyword">return</span> (
    <span class="xml"><span class="hljs-tag"><<span class="hljs-name">div</span>></span>
      <span class="hljs-tag"><<span class="hljs-name">h3</span>></span>&#123;title&#125;<span class="hljs-tag"></<span class="hljs-name">h3</span>></span>
      <span class="hljs-tag"><<span class="hljs-name">ul</span>></span>
        &#123;cart.map((i) => (
          <span class="hljs-tag"><<span class="hljs-name">li</span> <span class="hljs-attr">key</span>=<span class="hljs-string">&#123;i.name&#125;</span>></span>
            <span class="hljs-tag"><<span class="hljs-name">span</span>></span>
              &#123;i.name&#125; - &#123;i.price&#125;
            <span class="hljs-tag"></<span class="hljs-name">span</span>></span>
          <span class="hljs-tag"></<span class="hljs-name">li</span>></span>
        ))&#125;
      <span class="hljs-tag"></<span class="hljs-name">ul</span>></span>
      <span class="hljs-tag"><<span class="hljs-name">div</span>></span>
        <span class="hljs-tag"><<span class="hljs-name">span</span>></span>
          商品名称：
          <span class="hljs-tag"><<span class="hljs-name">input</span>
            <span class="hljs-attr">type</span>=<span class="hljs-string">"text"</span>
            <span class="hljs-attr">value</span>=<span class="hljs-string">&#123;name&#125;</span>
            <span class="hljs-attr">onChange</span>=<span class="hljs-string">&#123;(e)</span> =></span> setName(e.target.value)&#125;
          />
        <span class="hljs-tag"></<span class="hljs-name">span</span>></span>
        <span class="hljs-tag"><<span class="hljs-name">span</span>></span>
          价格：
          <span class="hljs-tag"><<span class="hljs-name">input</span>
            <span class="hljs-attr">type</span>=<span class="hljs-string">"number"</span>
            <span class="hljs-attr">value</span>=<span class="hljs-string">&#123;price&#125;</span>
            <span class="hljs-attr">onChange</span>=<span class="hljs-string">&#123;(e)</span> =></span> setPrice(+e.target.value)&#125;
          />
        <span class="hljs-tag"></<span class="hljs-name">span</span>></span>
        <span class="hljs-tag"><<span class="hljs-name">button</span> <span class="hljs-attr">onClick</span>=<span class="hljs-string">&#123;addItem&#125;</span>></span>添加商品<span class="hljs-tag"></<span class="hljs-name">button</span>></span>
      <span class="hljs-tag"></<span class="hljs-name">div</span>></span>
      <span class="hljs-tag"><<span class="hljs-name">p</span>></span>总价： &#123;total&#125;<span class="hljs-tag"></<span class="hljs-name">p</span>></span>
      <span class="hljs-tag"><<span class="hljs-name">button</span> <span class="hljs-attr">onClick</span>=<span class="hljs-string">&#123;settle&#125;</span>></span>结账<span class="hljs-tag"></<span class="hljs-name">button</span>></span>
      <span class="hljs-tag"><<span class="hljs-name">button</span> <span class="hljs-attr">onClick</span>=<span class="hljs-string">&#123;clearAll&#125;</span>></span>删除<span class="hljs-tag"></<span class="hljs-name">button</span>></span>
    <span class="hljs-tag"></<span class="hljs-name">div</span>></span></span>
  );
&#125;;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>我们从 <code>react</code> 中引入了 <code>useState</code> 钩子，这可能是编写函数组件最常用的钩子了——它的参数接受一个默认值，返回 <code>[value, setValue]</code> 的元组（就是约定好值的 JavaScript 数组啦），来帮助我们读取和修改数据。 有了 <code>useState</code>，我们终于让函数组件发挥出 class 组件的功能。</p>
<h4 data-id="heading-18">React Hooks 注意事项</h4>
<p>为了保证函数组件知道它自己调用了什么钩子，React Hooks 被设计成执行顺序和组件渲染顺序<strong>一致</strong>（有兴趣的可以找专门的 React Hooks 文章了解），数据结构可以看作是一个链表：</p>
<blockquote>
<p>组件A ->  组件B -> 组件C<br>
(useStateA1; useStateA2) -> (useStateB) -> (useStateC1; useStateC2)</p>
</blockquote>
<p>为了保证 Hooks 调用顺序一致，下面几个用法都应该避免：</p>
<ul>
<li>不要在 <code>if / while / for</code> 等流程语句中使用 Hooks</li>
</ul>
<pre><code class="hljs language-jsx copyable" lang="jsx"><span class="hljs-comment">// bad </span>
<span class="hljs-keyword">if</span> (someThing) &#123;
  useState(a)
&#125; <span class="hljs-keyword">else</span> &#123;
  useState(b)
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>不要在函数组件执行域之外调用 Hooks</li>
</ul>
<pre><code class="hljs language-jsx copyable" lang="jsx"><span class="hljs-comment">// bad, do not use outside the functional component</span>
<span class="hljs-keyword">const</span> [outer, setOuter] = useState()

<span class="hljs-comment">// bad, do not use inside class component</span>
<span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">A</span> <span class="hljs-keyword">extends</span> <span class="hljs-title">Component</span> </span>&#123;
  <span class="hljs-title">constructor</span> (<span class="hljs-params"></span>) &#123;
    <span class="hljs-built_in">this</span>.state = useState()
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-19">其他 Hooks</h4>
<p>除了 <code>useState</code> ， React 还内置了如 <code>useEffect</code> 、 <code>useLayoutEffect</code> 、 <code>useRef</code> <code>useMemo</code> 等钩子。这里介绍 <code>useEffect</code> 、 <code>useMemo</code>
和 <code>useCallback</code> 这三个带<strong>依赖项</strong>（参考下文 QA 解释）的钩子，剩下的参考文档 <a href="https://reactjs.org/docs/hooks-reference.html#gatsby-focus-wrapper" target="_blank" rel="nofollow noopener noreferrer">reactjs.org/docs/hooks-…</a></p>
<h5 data-id="heading-20">useEffect</h5>
<p>这是个多面手，处理组件更新后副作用的回调，当 state 或者 props 改变引发函数重新渲染时，根据参数和返回值的定义<strong>选择性执行</strong>。大致可以驾驭以下场景：</p>
<ul>
<li><code>componentDidMount</code> 和 <code>componentDidUpdate</code> 的合体，只要重新渲染始终会执行：</li>
</ul>
<pre><code class="copyable">// 只传一个回调，函数重新渲染就执行
useEffect(() => &#123; console.log('updated') &#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>指定某些<strong>依赖</strong>作为数组传入第二个参数，只要有一项依赖发生变化就执行，类似 Vue 中的 <code>watch</code>：</li>
</ul>
<pre><code class="copyable">function Comp(&#123; title &#125;) &#123;
  const [count, setCount] = useState(0);
  // 第二个参数指定一个数组，放入你想监听的依赖：
  useEffect(() => &#123;
    console.log('title or count has changed.')
  &#125;, [title, count])
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>原则上，函数中用到的所有依赖都应该放进数组里。</p>
<ul>
<li>处理组件第一次渲染时的回调，类似 Vue 中的 <code>mounted</code></li>
</ul>
<pre><code class="copyable">// 第二个参数传一个空数组，表示没有依赖，只会在第一次渲染时执行
useEffect(() => &#123;
  alert('mounted');
&#125;, [])
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>处理首次渲染和销毁，类似 Vue 中 <code>mounted</code> 和 <code>beforeDestroy</code> 组合</li>
</ul>
<pre><code class="copyable">useEffect(() => &#123;
    const onKeyPress = e => console.log(`You've press $&#123;e.key&#125; .`);
    document.addEventListener('keyPress', onKeyPress);
    // 如果返回值是函数，组件销毁之前 React 会调用这个函数来清理副作用
    return () => document.removeEventListener('keyPress', onKeyPress);
&#125;, [])
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>注意：Effect 钩子的依赖使用不当会导致组件无限更新（死循环）：</li>
</ul>
<pre><code class="hljs language-jsx copyable" lang="jsx"><span class="hljs-comment">// 1. 依赖一个 state 又在 effect 中更新这个 state</span>
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">Bad1</span>(<span class="hljs-params"></span>) </span>&#123;
  <span class="hljs-keyword">const</span> [count, setCount] = useState(<span class="hljs-number">0</span>);
  useEffect(<span class="hljs-function">() =></span> &#123;
    setCount(count++);
  &#125;, [count])
&#125;

<span class="hljs-comment">// 2. 每次依赖对象引用不一致</span>
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">Bad2</span>(<span class="hljs-params"></span>) </span>&#123;
  <span class="hljs-comment">// 组件重新渲染时 data 都是一个新对象。</span>
  <span class="hljs-keyword">const</span> data = &#123; <span class="hljs-attr">a</span>: <span class="hljs-number">1</span>, <span class="hljs-attr">b</span>: <span class="hljs-number">2</span> &#125;
  useEffect(<span class="hljs-function">() =></span> &#123;
    <span class="hljs-built_in">console</span>.log(data);
  &#125;, [data])
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h5 data-id="heading-21">useMemo/useCallback</h5>
<p>useMemo 类似于 Vue 的 <code>computed</code>，表示一个记忆状态 接受一个求值函数和一串依赖数组：</p>
<blockquote>
<p>useMemo(getterFn, [dep1, dep2 ...])</p>
</blockquote>
<p>用法</p>
<pre><code class="copyable">const [name, setName] = useState('John Smith');
const [age, setAge] = useState(17);

const getData = () => (&#123; name, age &#125;);
const data = useMemo(getData, [name, age])
<span class="copy-code-btn">复制代码</span></code></pre>
<p>第一次渲染时调用 <code>getData</code> 取值不必多说。当组件重新渲染时，如果元组中 name、age 其中一项变化，则仍会调用<code>getData</code>函数重新求值。如果二者都没变化，直接返回上一次渲染的数据给 data，避免了引用类型变化问题。</p>
<p>useCallback 是 useMemo 的函数版，防止组件重渲染时回调引用被覆盖：</p>
<pre><code class="copyable">const [count, setCount] = useState(0);
const setCount = useCallback(() => setCount(count + 1) , [count]);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>由于函数闭包特性，依赖项<code>count</code>必须传入，如果不传则每次都只会得到初次渲染的值<code>0</code>。</p>
<p>一句话概括 <code>useEffect</code>, <code>useMemo</code> 和 <code>useCallback</code>:</p>
<blockquote>
<p>只要依赖数组中的每一项和上次相同，那么 Hooks 的结果就相同</p>
</blockquote>
<h5 data-id="heading-22">自己封装</h5>
<p>将多个 hooks 封装进一个函数，再在函数组件中调用是允许的，因为这样不会破坏执行顺序：</p>
<pre><code class="copyable">const useCount = () => &#123;
  const [count, setCount] = useState(0);
  const text = useMemo(() => `You've click $&#123;count&#125; times!`);
  const add = useCallback(() => setCount(count + 1));
  const reset = useCallback(() => setCount(0));
  return &#123;
    text,
    add,
    reset
  &#125;
&#125;

const Comp = () => &#123;
  const &#123; text, add, reset &#125; = useCount();
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>不过也要注意：封装的钩子函数名称也要用 <code>use</code> 开头（这是一个约束）。</p>
<h2 data-id="heading-23">小结</h2>
<p>React 和 Vue 是目前前端流行的三大框架之二。本文以对比的视角，通过单文件组件、JSX 和 Template 声明周期等各自特性的对比，介绍了 React 的基本写法和注意事项。为的是让大家更清晰地认识两者之间的区别和相似点，加深对这两者的理解。</p>
<h2 data-id="heading-24">问答环节</h2>
<h3 data-id="heading-25">刚才在 React Hooks 中提到的依赖是啥</h3>
<p>函数式组件，每一次更新都会重新执行一遍函数，所以将 <code>prop</code>、<code>state</code>、<code>memo</code> 、 <code>context</code> 和 <code>callback</code> 等<strong>可能</strong>会随着函数重新渲染而变的值叫做依赖。而 <code>ref</code> 、 <code>useState</code>
中返回的 <code>setXXX</code> 函数，不会随着组件重新渲染而改变，所以不算做依赖。</p>
<h3 data-id="heading-26">setState 到底是同步还是异步</h3>
<p>我觉得不应该过多关心这个问题，但鉴于许多面试都会问到这个，在此梳理一下：</p>
<ol>
<li>首先 setState 更新是同步的，但是调用完成后不会直接赋值给 state ，所以造成了调用后 state 没有立即变化的情况，但不是异步逻辑造成的。</li>
<li>在同步的回调、componentDidMount 等钩子中，因为批处理机制的存在，必须要等到所有 setState 调用完毕，才会一次性更新：</li>
</ol>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">A</span> <span class="hljs-keyword">extends</span> <span class="hljs-title">Component</span> </span>&#123;
  state = &#123; <span class="hljs-attr">a</span>: <span class="hljs-number">1</span> &#125;

  <span class="hljs-function"><span class="hljs-title">callSync</span>(<span class="hljs-params"></span>)</span> &#123;
    <span class="hljs-built_in">this</span>.setState(&#123; <span class="hljs-attr">a</span>: <span class="hljs-number">100</span> &#125;);
    <span class="hljs-built_in">console</span>.log(<span class="hljs-built_in">this</span>.state.a); <span class="hljs-comment">// 1</span>
    <span class="hljs-built_in">this</span>.setState(&#123; <span class="hljs-attr">a</span>: <span class="hljs-number">200</span> &#125;);
    <span class="hljs-built_in">console</span>.log(<span class="hljs-built_in">this</span>.state.a); <span class="hljs-comment">// 1</span>
    <span class="hljs-built_in">this</span>.setState(&#123; <span class="hljs-attr">a</span>: <span class="hljs-number">300</span> &#125;, <span class="hljs-function">() =></span> <span class="hljs-built_in">console</span>.log(<span class="hljs-built_in">this</span>.state.a)); <span class="hljs-comment">// 300</span>
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<ol start="3">
<li>在 setTimeout 、 Promise 等异步代码中，由于批处理流程已经结束了，所以 setState 会立即更新</li>
</ol>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">A</span> <span class="hljs-keyword">extends</span> <span class="hljs-title">Component</span> </span>&#123;
  callAfterTimeout = <span class="hljs-function">() =></span> &#123;
    <span class="hljs-built_in">setTimeout</span>(<span class="hljs-function">() =></span> &#123;
      <span class="hljs-built_in">this</span>.setState(&#123; <span class="hljs-attr">a</span>: <span class="hljs-number">100</span> &#125;);
      <span class="hljs-built_in">console</span>.log(<span class="hljs-built_in">this</span>.state.a) <span class="hljs-comment">// 100</span>
    &#125;, <span class="hljs-number">0</span>)
  &#125;

  callAfterPromise = <span class="hljs-function">() =></span> &#123;
    <span class="hljs-built_in">Promise</span>
      .resolve()
      .then(<span class="hljs-function">() =></span> &#123;
        <span class="hljs-built_in">this</span>.setState(&#123; <span class="hljs-attr">a</span>: <span class="hljs-number">100</span> &#125;);
        <span class="hljs-built_in">console</span>.log(<span class="hljs-built_in">this</span>.state.a) <span class="hljs-comment">// 100</span>
      &#125;)
  &#125;

  callAfterAwait = <span class="hljs-keyword">async</span> () => &#123;
    <span class="hljs-keyword">await</span> <span class="hljs-built_in">Promise</span>.resolve();
    <span class="hljs-built_in">this</span>.setState(&#123; <span class="hljs-attr">a</span>: <span class="hljs-number">100</span> &#125;);
    <span class="hljs-built_in">console</span>.log(<span class="hljs-built_in">this</span>.state.a) <span class="hljs-comment">// 100</span>
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-27">能不能封装一个 v-model</h3>
<p>借助 React Hooks 来做一层封装（花里胡哨的玩意，似乎这么做的人不多）：</p>
<pre><code class="hljs language-jsx copyable" lang="jsx"><span class="hljs-keyword">const</span> useModel = <span class="hljs-function">(<span class="hljs-params">&#123; value = <span class="hljs-string">'value'</span>, event = <span class="hljs-string">'onChange'</span> &#125;, defaultValue</span>) =></span> &#123;
  <span class="hljs-keyword">const</span> [val, setVal] = useState(defaultValue);
  <span class="hljs-keyword">return</span> &#123;
    [value]: val,
    [event]: useCallback(<span class="hljs-function"><span class="hljs-params">e</span> =></span> setVal(e.target[value]), [])
  &#125;
&#125;

<span class="hljs-keyword">const</span> MyInput = <span class="hljs-function">() =></span> &#123;
  <span class="hljs-keyword">const</span> inputModel = useModel(); <span class="hljs-comment">// &#123; value: '', onChange: f &#125;</span>
  <span class="hljs-keyword">const</span> checkboxModel = useModel(&#123; <span class="hljs-attr">value</span>: <span class="hljs-string">'checked'</span> &#125;, <span class="hljs-literal">true</span>); <span class="hljs-comment">// &#123; checked: true, onChange: f &#125;</span>

  <span class="hljs-keyword">return</span> (
    <span class="xml"><span class="hljs-tag"><<span class="hljs-name">form</span>></span>
      <span class="hljs-tag"><<span class="hljs-name">input</span> &#123;<span class="hljs-attr">...inputModel</span>&#125; /></span>
      <span class="hljs-tag"><<span class="hljs-name">input</span> <span class="hljs-attr">type</span>=<span class="hljs-string">"checkbox"</span> &#123;<span class="hljs-attr">...checkboxModel</span>&#125; /></span>
    <span class="hljs-tag"></<span class="hljs-name">form</span>></span></span>
  )
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-28">JSX 不是 React 专用吗？ Vue 也能写 JSX ？</h3>
<ol>
<li>不是，2. 能 <a href="https://cn.vuejs.org/v2/guide/render-function.html#JSX" target="_blank" rel="nofollow noopener noreferrer">cn.vuejs.org/v2/guide/re…</a></li>
</ol>
<h3 data-id="heading-29">有计划出镜像文章：写给 React 开发的 Vue 上手指南吗？</h3>
<p>你好，有的</p>
<h3 data-id="heading-30">有计划带上 Angular 吗？</h3>
<p>抱歉，Angular 用的不多，暂不编写。</p></div> <div class="image-viewer-box" data-v-78c9b824><!----></div>  
</div>
            