
---
title: 'immutable data 是如何优化 React 性能的'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/f16fd580451a42d8bcd0c04b8ba2a12b~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Fri, 11 Jun 2021 00:27:02 GMT
thumbnail: 'https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/f16fd580451a42d8bcd0c04b8ba2a12b~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>今天我们解决以下几个问题，什么是<code>immutable data</code>，<code>mutable data</code>带来了哪些问题，immutable data优化了哪些性能？</p>
<h1 data-id="heading-0">mutable data 数据的可变性</h1>
<p>数据的可变性用一段代码就可以描述清楚</p>
<pre><code class="copyable">const a = [&#123; todo: 'Learn js'&#125;, &#123;todo: 'Learn react'&#125;];
const b = [...a];
b[1].todo = 'Learn vue';
console.log(a[1].todo); //Learn vue
<span class="copy-code-btn">复制代码</span></code></pre>
<p>其实可以一眼看出这是<code>浅copy</code>导致的问题。内层的对象指向<code>堆内存</code>地址相同，所以修改b数组中的对象，a数组也会发生变化。平时大伙在项目中操作比较复杂的数据结构时，都习惯性<code>deepCopy</code>,否则就会出现一些不易察觉的bug。</p>
<blockquote>
<p>那我们只要遇到需要操作多层数据结构的情况使用deepCopy不就解决了么。<br>然而事实是随着数据层数的增加，deepCopy性能的消耗还是十分明显的，并且在React中deepCopy会对渲染造成很大的开销，这与react的渲染机制有关。</p>
</blockquote>
<h1 data-id="heading-1">immutable数据优化了哪些性能</h1>
<p>首先我们要看一下React 是如何渲染的。</p>
<h2 data-id="heading-2">React 渲染机制解析</h2>
<pre><code class="hljs language-mermaid" lang="mermaid">graph LR
setState或者props改变 --> shouldComponentUpdate --true --> 递归render 
递归render --> componentDidUpdate 
</code></pre>
<p>在React中，render函数返回虚拟dom树，并经过Diff算法计算出与上次虚拟dom的区别，针对差异的部分做更新，渲染出真实dom。</p>
<p>递归render的过程是性能消耗的大头，如果shouldComponentUpdate返回false，更新的过程就会被打住，所以我们要好好的利用这个shouldComponentUpdate。</p>
<h2 data-id="heading-3">shouldComponentUpdate</h2>
<p>这是一个组件的子树。每个节点中，SCU 代表 shouldComponentUpdate 返回的值，而 vDOMEq 代表返回的 React 元素是否相同。最后，圆圈的颜色代表了该组件是否需要被调停，红色代表shouldComponentUpdate返回true，进行render，绿色代表返回false，不进行render。</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/f16fd580451a42d8bcd0c04b8ba2a12b~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>c1是红色节点，<code>shouldComponentUpdate</code>返回 <code>true</code>,进入diff算法比对新旧VDom树，如果新旧VDom树中<code>节点类型不同</code>，则<code>全部替换</code>，包括下面子组件，图中展示的是<code>节点类型相同</code>的情况，则<code>递归子组件</code>。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">//什么是节点类型不同</span>
<A>
  <span class="xml"><span class="hljs-tag"><<span class="hljs-name">C</span>/></span></span>
</A>
<span class="hljs-comment">// A与B是不同节点类型</span>
<span class="xml"><span class="hljs-tag"><<span class="hljs-name">B</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">C</span>/></span>
<span class="hljs-tag"></<span class="hljs-name">B</span>></span></span>
React会直接删掉A节点（包括它所有的子节点）,然后新建一个B节点插入。
<span class="copy-code-btn">复制代码</span></code></pre>
<p>节点 C2 的 <code>shouldComponentUpdate</code> 返回了 <code>false</code>，React 因而不会调用 C2 的 <code>render</code>，也因此 C4 和 C5 的 <code>shouldComponentUpdate</code> 不会被调用到。</p>
<p>C3，<code>shouldComponentUpdate</code> 返回了 <code>true</code>，所以 React 需要继续向下查询子节点。这里 C6 的 <code>shouldComponentUpdate</code> 返回了 <code>true</code>，同时由于<code>渲染的元素与之前的不同</code>使得 React 更新了该 DOM。</p>
<p>最后一个有趣的例子是 C8。React 需要渲染这个组件，但是由于其返回的 React 元素和之前渲染的相同，所以不需要更新 DOM。</p>
<p>显而易见，你看到 React 只改变了 C6 的 DOM。对于 C8，通过对比了渲染的 React 元素跳过了渲染。而对于 C2 的子节点和 C7，由于 shouldComponentUpdate 使得 render 并没有被调用。因此它们也不需要对比元素了。</p>
<h2 data-id="heading-4">类组件React.PureComponent与函数组件memo</h2>
<p>通过shouldComponentUpdate可以避免不必要的渲染过程，从而达到性能上的优化。但是如果需要我们挨个对比props和state中的每个属性的话就太麻烦了，React提供了两种方式自动帮我们完成shouldComponentUpdate中的工作，类组件只要<code>继承React.PureComponent</code>就可以，函数组件提供了<code>memo</code>方法。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">//三种方式</span>
<span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">CounterButton</span> <span class="hljs-keyword">extends</span> <span class="hljs-title">React</span>.<span class="hljs-title">Component</span> </span>&#123;
  <span class="hljs-function"><span class="hljs-title">constructor</span>(<span class="hljs-params">props</span>)</span> &#123;
    <span class="hljs-built_in">super</span>(props);
    <span class="hljs-built_in">this</span>.state = &#123;<span class="hljs-attr">count</span>: <span class="hljs-number">1</span>&#125;;
  &#125;

  <span class="hljs-function"><span class="hljs-title">shouldComponentUpdate</span>(<span class="hljs-params">nextProps, nextState</span>)</span> &#123;
    <span class="hljs-keyword">if</span> (<span class="hljs-built_in">this</span>.props.color !== nextProps.color) &#123;
      <span class="hljs-keyword">return</span> <span class="hljs-literal">true</span>;
    &#125;
    <span class="hljs-keyword">if</span> (<span class="hljs-built_in">this</span>.state.count !== nextState.count) &#123;
      <span class="hljs-keyword">return</span> <span class="hljs-literal">true</span>;
    &#125;
    <span class="hljs-keyword">return</span> <span class="hljs-literal">false</span>;
  &#125;

  <span class="hljs-function"><span class="hljs-title">render</span>(<span class="hljs-params"></span>)</span> &#123;
    <span class="hljs-keyword">return</span> (
      <span class="xml"><span class="hljs-tag"><<span class="hljs-name">button</span>
        <span class="hljs-attr">color</span>=<span class="hljs-string">&#123;this.props.color&#125;</span>
        <span class="hljs-attr">onClick</span>=<span class="hljs-string">&#123;()</span> =></span> this.setState(state => (&#123;count: state.count + 1&#125;))&#125;>
        Count: &#123;this.state.count&#125;
      <span class="hljs-tag"></<span class="hljs-name">button</span>></span></span>
    );
  &#125;
&#125;


<span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">CounterButton</span> <span class="hljs-keyword">extends</span> <span class="hljs-title">React</span>.<span class="hljs-title">PureComponent</span> </span>&#123;
  <span class="hljs-function"><span class="hljs-title">constructor</span>(<span class="hljs-params">props</span>)</span> &#123;
    <span class="hljs-built_in">super</span>(props);
    <span class="hljs-built_in">this</span>.state = &#123;<span class="hljs-attr">count</span>: <span class="hljs-number">1</span>&#125;;
  &#125;

  <span class="hljs-function"><span class="hljs-title">render</span>(<span class="hljs-params"></span>)</span> &#123;
    <span class="hljs-keyword">return</span> (
      <span class="xml"><span class="hljs-tag"><<span class="hljs-name">button</span>
        <span class="hljs-attr">color</span>=<span class="hljs-string">&#123;this.props.color&#125;</span>
        <span class="hljs-attr">onClick</span>=<span class="hljs-string">&#123;()</span> =></span> this.setState(state => (&#123;count: state.count + 1&#125;))&#125;>
        Count: &#123;this.state.count&#125;
      <span class="hljs-tag"></<span class="hljs-name">button</span>></span></span>
    );
  &#125;
&#125;


<span class="hljs-keyword">const</span> CounterButton = <span class="hljs-function"><span class="hljs-params">props</span> =></span> &#123;
  <span class="hljs-keyword">const</span> [count, setCount] = useState(<span class="hljs-number">1</span>);

  <span class="hljs-keyword">return</span> (
    <span class="xml"><span class="hljs-tag"><<span class="hljs-name">button</span> <span class="hljs-attr">color</span>=<span class="hljs-string">&#123;props.color&#125;</span> <span class="hljs-attr">onClick</span>=<span class="hljs-string">&#123;()</span> =></span> setCount(count => count + 1)&#125;>
      Count: &#123;count&#125;
    <span class="hljs-tag"></<span class="hljs-name">button</span>></span></span>
  );
&#125;;

<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> React.memo(CounterButton);

<span class="copy-code-btn">复制代码</span></code></pre>
<blockquote>
<p>注意：无论是React.PureComponent还是memo都只会进行浅比较，一旦属性值为引用类型，浅比较会失效，原因为上面解释的数据可变性。如果使用deepCopy，那所有shouldComponentUpdate都会返回true，都进入了diff运算，就没有了意义。</p>
</blockquote>
<p>那有没有一种方式，使用浅比较就可以得出哪部分是改变的数据节点呢？</p>
<h2 data-id="heading-5">immutable 数据结构</h2>
<p>我们还是通过一小段代码来认识什么是immutable数据，这里使用的是<a href="https://github.com/immerjs/immer" target="_blank" rel="nofollow noopener noreferrer">Immer</a>这个库。</p>
<pre><code class="hljs language-js copyable" lang="js">  <span class="hljs-keyword">import</span> produce <span class="hljs-keyword">from</span> <span class="hljs-string">'immer'</span>;
  
  <span class="hljs-keyword">const</span> a = [&#123; <span class="hljs-attr">todo</span>: <span class="hljs-string">'Learn js'</span> &#125;, &#123; <span class="hljs-attr">todo</span>: <span class="hljs-string">'Learn react'</span> &#125;];
  <span class="hljs-keyword">const</span> b = produce(a, <span class="hljs-function"><span class="hljs-params">draftState</span> =></span> &#123;
    draftState[<span class="hljs-number">1</span>].todo = <span class="hljs-string">'Learn vue'</span>;
  &#125;);

  <span class="hljs-built_in">console</span>.log(a === b); <span class="hljs-comment">//false</span>
  <span class="hljs-built_in">console</span>.log(a[<span class="hljs-number">0</span>] === b[<span class="hljs-number">0</span>]); <span class="hljs-comment">//true</span>
  <span class="hljs-built_in">console</span>.log(a[<span class="hljs-number">1</span>] === b[<span class="hljs-number">1</span>]); <span class="hljs-comment">//false</span>
  <span class="hljs-built_in">console</span>.log(a[<span class="hljs-number">1</span>].todo === b[<span class="hljs-number">1</span>].todo); <span class="hljs-comment">//false</span>

<span class="copy-code-btn">复制代码</span></code></pre>
<p>这里可以看到未改变的引用类型内存地址未发生改变，保证了旧节点的可用且不变，而改变了的节点，它和与它相关的所有上级节点都更新。如图所示：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/3343fca60d4949c0a2cb325cfaad58ab~tplv-k3u1fbpfcp-watermark.image" alt="5518628-61c587b3466654e9.webp" loading="lazy" referrerpolicy="no-referrer"></p>
<p>这样就避免了深拷贝带来的极大的性能开销问题，并且更新后返回了一个全新的引用，即使是浅比对也能感知到哪一部分数据需要更新。</p>
<h3 data-id="heading-6">immer应用示例</h3>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> [state, setState] = useState(&#123;
    <span class="hljs-attr">id</span>: <span class="hljs-number">14</span>,
    <span class="hljs-attr">email</span>: <span class="hljs-string">"stewie@familyguy.com"</span>,
    <span class="hljs-attr">profile</span>: &#123;
      <span class="hljs-attr">name</span>: <span class="hljs-string">"Stewie Griffin"</span>,
      <span class="hljs-attr">bio</span>: <span class="hljs-string">"You know, the... the novel you've been working on"</span>,
      <span class="hljs-attr">age</span>:<span class="hljs-number">1</span>
    &#125;
  &#125;);

<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">changeBio</span>(<span class="hljs-params">newBio</span>) </span>&#123;
    setState(<span class="hljs-function"><span class="hljs-params">current</span> =></span> (&#123;
      ...current,
      <span class="hljs-attr">profile</span>: &#123;
        ...current.profile,
        <span class="hljs-attr">bio</span>: newBio
      &#125;
    &#125;));
  &#125;



<span class="hljs-comment">//使用 immer</span>
<span class="hljs-keyword">import</span> &#123; useImmer &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'use-immer'</span>;

<span class="hljs-keyword">const</span> [state, setState] = useImmer(&#123;
    <span class="hljs-attr">id</span>: <span class="hljs-number">14</span>,
    <span class="hljs-attr">email</span>: <span class="hljs-string">"stewie@familyguy.com"</span>,
    <span class="hljs-attr">profile</span>: &#123;
      <span class="hljs-attr">name</span>: <span class="hljs-string">"Stewie Griffin"</span>,
      <span class="hljs-attr">bio</span>: <span class="hljs-string">"You know, the... the novel you've been working on"</span>,
      <span class="hljs-attr">age</span>:<span class="hljs-number">1</span>
    &#125;
 &#125;);

<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">changeBio</span>(<span class="hljs-params">newBio</span>) </span>&#123;
   setState(<span class="hljs-function"><span class="hljs-params">draft</span> =></span> &#123;
      draft.profile.bio = newBio;
    &#125;);
  &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>减少了解构语法是不是清爽了很多，当然随着数据结构进一步复杂，immer优势也会进一步体现。</p>
<p>感谢大家的阅读。</p></div>  
</div>
            