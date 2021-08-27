
---
title: 'setState是异步还是同步？'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=8839'
author: 掘金
comments: false
date: Thu, 26 Aug 2021 22:18:43 GMT
thumbnail: 'https://picsum.photos/400/300?random=8839'
---

<div>   
<div class="markdown-body html cache"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p><strong>这是我参与8月更文挑战的第27天，活动详情查看：<a href="https://juejin.cn/post/6987962113788493831" title="https://juejin.cn/post/6987962113788493831" target="_blank">8月更文挑战</a></strong></p>
<p>在介绍这个问题之前，我们先来看一下一个例子：</p>
<pre><code class="hljs language-js copyable" lang="js">state = &#123;
    <span class="hljs-attr">number</span>:<span class="hljs-number">1</span>
&#125;;
<span class="hljs-function"><span class="hljs-title">componentDidMount</span>(<span class="hljs-params"></span>)</span>&#123;
    <span class="hljs-built_in">this</span>.setState(&#123;<span class="hljs-attr">number</span>:<span class="hljs-number">3</span>&#125;)
    <span class="hljs-built_in">console</span>.log(<span class="hljs-built_in">this</span>.state.number)
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>看完这个例子，也许很多小伙伴会下意识的以为setState是一个异步方法，但是其实setState并没有异步的说法，之所以会有一种异步方法的表现形式，归根结底还是因为react框架本身的性能机制所导致的。因为每次调用setState都会触发更新，异步操作是为了提高性能，将多个状态合并一起更新，减少re-render调用。</p>
<p>试想一下如果在组件中有以下这样一段代码执行：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">for</span> ( <span class="hljs-keyword">let</span> i = <span class="hljs-number">0</span>; i < <span class="hljs-number">100</span>; i++ ) &#123;
    <span class="hljs-built_in">this</span>.setState( &#123; <span class="hljs-attr">num</span>: <span class="hljs-built_in">this</span>.state.num + <span class="hljs-number">1</span> &#125; );
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>如果setState是一个同步执行的机制，那么这个组件会被重新渲染100次，这对性能是一个相当大的消耗。</p>
<p>显然，React也是想到了这个问题，因此对setState做了一些特殊的优化：</p>
<blockquote>
<p>React会将多个setState的调用合并为一个来执行，也就是说，当执行setState的时候，state中的数据并不会马上更新</p>
</blockquote>
<p>这也很好的印证了刚才提到的那个例子。我们可以看下面代码会在控制台上打印什么？
但是往往在实际的开发工作中，我们可能需要同步的获取到更新之后的数据，那么怎么获取呢？下面介绍几种常用的方法：</p>
<h3 data-id="heading-0"><strong>回调函数</strong></h3>
<p>setState提供了一个回调函数供开发者使用，在回调函数中，我们可以实时的获取到更新之后的数据。还是以刚才的例子做示范：</p>
<pre><code class="hljs language-js copyable" lang="js">state = &#123;
    <span class="hljs-attr">number</span>:<span class="hljs-number">1</span>
&#125;;
<span class="hljs-function"><span class="hljs-title">componentDidMount</span>(<span class="hljs-params"></span>)</span>&#123;
    <span class="hljs-built_in">this</span>.setState(&#123;<span class="hljs-attr">number</span>:<span class="hljs-number">3</span>&#125;,<span class="hljs-function">()=></span>&#123;
        <span class="hljs-built_in">console</span>.log(<span class="hljs-built_in">this</span>.state.number)
    &#125;)
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这个时候大家可以看到控制台打印的数据就是最新的了，我们也就实时的获取到了最新的数据。</p>
<h3 data-id="heading-1"><strong>setTimeout</strong></h3>
<p>上面我们讲到了，setState本身并不是一个异步方法，其之所以会表现出一种异步的形式，是因为react框架本身的一个性能优化机制。那么基于这一点，如果我们能够越过react的机制，是不是就可以令setState以同步的形式体现了呢？</p>
<p>说再多文字不如代码实践，实践才是检验真理的唯一标准，下面我们还是以之前的例子为基础改造一下代码：</p>
<pre><code class="hljs language-js copyable" lang="js">state = &#123;
    <span class="hljs-attr">number</span>:<span class="hljs-number">1</span>
&#125;;
<span class="hljs-function"><span class="hljs-title">componentDidMount</span>(<span class="hljs-params"></span>)</span>&#123;
    <span class="hljs-built_in">setTimeout</span>(<span class="hljs-function">()=></span>&#123;
      <span class="hljs-built_in">this</span>.setState(&#123;<span class="hljs-attr">number</span>:<span class="hljs-number">3</span>&#125;)
      <span class="hljs-built_in">console</span>.log(<span class="hljs-built_in">this</span>.state.number)
    &#125;,<span class="hljs-number">0</span>)
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-2"><strong>原生事件中修改状态</strong></h3>
<p>上面已经印证了避过react的机制，可以同步获取到更新之后的数据，那么除了setTimeout以外，还有在原生事件中也是可以的。还是看一下例子：</p>
<pre><code class="copyable">state = &#123;
    number:1
&#125;;
componentDidMount() &#123;
    document.body.addEventListener('click', this.changeVal, false);
&#125;
changeVal = () => &#123;
    this.setState(&#123;
      number: 3
    &#125;)
    console.log(this.state.number)
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-3">总结</h2>
<blockquote>
<p>setState本身并不是异步，只是因为react的性能优化机制体现为异步。在react的生命周期函数或者作用域下为异步，在原生的环境下为同步。</p>
<ul>
<li>1.setState 只在合成事件和钩子函数中是“异步”的，在原生事件和 setTimeout 中都是同步的。</li>
<li>2.setState的“异步”并不是说内部由异步代码实现，其实本身执行的过程和代码都是同步的，只是合成事件和钩子函数的调用顺序在更新之前，导致在合成事件和钩子函数中没法立马拿到更新后的值，形式了所谓的“异步”，当然可以通过第二个参数 setState(partialState, callback) 中的callback拿到更新后的结果。</li>
<li>3.setState 的批量更新优化也是建立在“异步”（合成事件、钩子函数）之上的，在原生事件和setTimeout 中不会批量更新，在“异步”中如果对同一个值进行多次 setState ， setState 的批量更新策略会对其进行覆盖，取最后一次的执行，如果是同时 setState 多个不同的值，在更新时会对其进行合并批量更新。</li>
</ul>
</blockquote>
<p><strong>通过我们上面的学习，我们看看下面的代码最终会打印什么？</strong></p>
<pre><code class="hljs language-jsx copyable" lang="jsx"><span class="hljs-keyword">import</span> React <span class="hljs-keyword">from</span> <span class="hljs-string">"react"</span>;
<span class="hljs-keyword">import</span> ReactDOM <span class="hljs-keyword">from</span> <span class="hljs-string">"react-dom"</span>;
<span class="hljs-keyword">import</span> <span class="hljs-string">"antd/dist/antd.css"</span>;
<span class="hljs-keyword">import</span> <span class="hljs-string">"./index.css"</span>;
<span class="hljs-keyword">import</span> &#123; Button &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">"antd"</span>;
<span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">App</span> <span class="hljs-keyword">extends</span> <span class="hljs-title">React</span>.<span class="hljs-title">Component</span> </span>&#123;
<span class="hljs-function"><span class="hljs-title">constructor</span>(<span class="hljs-params"></span>)</span> &#123;
    <span class="hljs-built_in">super</span>();
    <span class="hljs-built_in">this</span>.state = &#123;
        <span class="hljs-attr">count</span>: <span class="hljs-number">0</span>
    &#125;;
&#125;
<span class="hljs-function"><span class="hljs-title">componentDidMount</span>(<span class="hljs-params"></span>)</span> &#123;
    <span class="hljs-built_in">this</span>.setState(&#123;
        <span class="hljs-attr">count</span>: <span class="hljs-built_in">this</span>.state.count + <span class="hljs-number">1</span>
    &#125;);
    <span class="hljs-built_in">console</span>.log(<span class="hljs-string">"cc1"</span>, <span class="hljs-built_in">this</span>.state.count); <span class="hljs-comment">// 打印</span>
    <span class="hljs-built_in">this</span>.setState(&#123;
        <span class="hljs-attr">count</span>: <span class="hljs-built_in">this</span>.state.count + <span class="hljs-number">1</span>
    &#125;);
    <span class="hljs-built_in">console</span>.log(<span class="hljs-string">"cc2"</span>, <span class="hljs-built_in">this</span>.state.count); <span class="hljs-comment">// 打印</span>
    <span class="hljs-built_in">setTimeout</span>(<span class="hljs-function">() =></span> &#123;
        <span class="hljs-built_in">this</span>.setState(&#123;
            <span class="hljs-attr">count</span>: <span class="hljs-built_in">this</span>.state.count + <span class="hljs-number">1</span>
        &#125;);
        <span class="hljs-built_in">console</span>.log(<span class="hljs-string">"setTimeout1"</span>, <span class="hljs-built_in">this</span>.state.count); <span class="hljs-comment">// 打印</span>
    &#125;, <span class="hljs-number">0</span>);
    
    <span class="hljs-built_in">setTimeout</span>(<span class="hljs-function">() =></span> &#123;
        <span class="hljs-built_in">this</span>.setState(&#123;
            <span class="hljs-attr">count</span>: <span class="hljs-built_in">this</span>.state.count + <span class="hljs-number">1</span>
        &#125;);
        <span class="hljs-built_in">console</span>.log(<span class="hljs-string">"setTimeout2"</span>, <span class="hljs-built_in">this</span>.state.count); <span class="hljs-comment">// 打印</span>
    &#125;, <span class="hljs-number">0</span>);
    
    <span class="hljs-built_in">Promise</span>.resolve().then(<span class="hljs-function">() =></span> &#123;
        <span class="hljs-built_in">this</span>.setState(&#123;
            <span class="hljs-attr">count</span>: <span class="hljs-built_in">this</span>.state.count + <span class="hljs-number">1</span>
        &#125;);
        <span class="hljs-built_in">console</span>.log(<span class="hljs-string">"promise1"</span>, <span class="hljs-built_in">this</span>.state.count);
        <span class="hljs-built_in">this</span>.setState(&#123;
            <span class="hljs-attr">count</span>: <span class="hljs-built_in">this</span>.state.count + <span class="hljs-number">1</span>
        &#125;);
        <span class="hljs-built_in">console</span>.log(<span class="hljs-string">"promise2"</span>, <span class="hljs-built_in">this</span>.state.count);
        
    &#125;);
    <span class="hljs-built_in">this</span>.setState(&#123;
        <span class="hljs-attr">count</span>: <span class="hljs-built_in">this</span>.state.count + <span class="hljs-number">1</span>
    &#125;);
    <span class="hljs-built_in">console</span>.log(<span class="hljs-string">"cc3"</span>, <span class="hljs-built_in">this</span>.state.count); <span class="hljs-comment">// 打印</span>
&#125;

    click = <span class="hljs-function">() =></span> &#123;
        <span class="hljs-built_in">this</span>.setState(&#123;
            <span class="hljs-attr">count</span>: <span class="hljs-built_in">this</span>.state.count + <span class="hljs-number">1</span>
        &#125;);
        <span class="hljs-built_in">console</span>.log(<span class="hljs-string">"click"</span>, <span class="hljs-built_in">this</span>.state.count);
    &#125;;

    <span class="hljs-function"><span class="hljs-title">render</span>(<span class="hljs-params"></span>)</span> &#123;
        <span class="hljs-built_in">console</span>.log(<span class="hljs-string">"render"</span>, <span class="hljs-built_in">this</span>.state.count);
        <span class="hljs-keyword">return</span> (
        <span class="xml"><span class="hljs-tag"><></span>
            <span class="hljs-tag"><<span class="hljs-name">Button</span> <span class="hljs-attr">type</span>=<span class="hljs-string">"primary"</span> <span class="hljs-attr">onClick</span>=<span class="hljs-string">&#123;this.click&#125;</span>></span>
                &#123;this.state.count&#125;
            <span class="hljs-tag"></<span class="hljs-name">Button</span>></span>
        <span class="hljs-tag"></></span></span>
        );
    &#125;
&#125;
ReactDOM.render(<span class="xml"><span class="hljs-tag"><<span class="hljs-name">App</span> /></span></span>, <span class="hljs-built_in">document</span>.getElementById(<span class="hljs-string">"container"</span>));
<span class="copy-code-btn">复制代码</span></code></pre></div>  
</div>
            