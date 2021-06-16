
---
title: '盘点那些 React Hooks 里常见的问题'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/c8f5177f715d465f9eb0cc7e4b935e4a~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Thu, 10 Jun 2021 23:47:04 GMT
thumbnail: 'https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/c8f5177f715d465f9eb0cc7e4b935e4a~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>原文：<a href="https://juejin.cn/post/6972439516703358990" target="_blank">juejin.cn/post/697243…</a><br>
作者：Tonychen</p>
<h2 data-id="heading-0">Infinite Chain Of  Update</h2>
<p>实际使用中有时候会碰到 <code>Infinite Chain Of Update</code> 这个报错，其实就是你的一段代码引发了「死循环更新」。下面我们来看几个例子👇</p>
<h3 data-id="heading-1">依赖数组问题</h3>
<p>比如说在使用 <code>useEffect</code> 时没有传入依赖数组👇</p>
<pre><code class="hljs language-jsx copyable" lang="jsx"><span class="hljs-comment">// count 会无限 + 1</span>
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">App</span>(<span class="hljs-params"></span>) </span>&#123;
    <span class="hljs-keyword">const</span> [count, setCount] = useState(<span class="hljs-number">0</span>)

    useEffect(<span class="hljs-function">() =></span> &#123;
        setCount(count + <span class="hljs-number">1</span>)
    &#125;)
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>为什么说 <code>count</code> 会无限更新？这里的逻辑是这样的👇</p>
<ul>
<li>组件更新</li>
<li>执行 <code>useEffect</code></li>
<li>更新 <code>count</code> 并触发组件更新</li>
<li>执行 <code>useEffect</code></li>
<li>……</li>
</ul>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/c8f5177f715d465f9eb0cc7e4b935e4a~tplv-k3u1fbpfcp-watermark.image" alt="2021-06-09-1053-4.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>解决方法很简单，只要给 <code>useEffect</code> 传一个空数组作为第三个参数，下次更新时  <code>useEffect</code>  便不会执行。</p>
<pre><code class="hljs language-jsx copyable" lang="jsx"><span class="hljs-comment">// 正常渲染</span>
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">App</span>(<span class="hljs-params"></span>) </span>&#123;
    <span class="hljs-keyword">const</span> [count, setCount] = useState(<span class="hljs-number">0</span>)

    useEffect(<span class="hljs-function">() =></span> &#123;
        setCount(count + <span class="hljs-number">1</span>)
    &#125;, [])
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-2">监听了被更新的值</h3>
<p>这个算是新手 <code>hooks</code> 玩家经常会遇到、老手也有些头疼的问题。</p>
<ul>
<li>案例1</li>
</ul>
<p><code>useEeffect</code> 中更新的 <code>state</code> 间接影响了被监听的变量，举个例子🌰</p>
<pre><code class="hljs language-jsx copyable" lang="jsx"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">App</span>(<span class="hljs-params"></span>) </span>&#123;
    <span class="hljs-keyword">const</span> [obj, setObj] = useState(&#123;<span class="hljs-attr">a</span>: <span class="hljs-number">0</span>&#125;)
    <span class="hljs-keyword">const</span> &#123;a&#125; = obj
    useEffect(<span class="hljs-function">() =></span> &#123;
        setObj(&#123;
            ...obj,
            <span class="hljs-attr">a</span>: <span class="hljs-number">1</span>
        &#125;)
    &#125;, [a, obj])
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>上面这段代码在实际运行的时候就会导致死循环，为什么呢？因为在 <code>setObj</code> 的时候改变的是 <code>obj</code> 这个值，而 <code>useEffect</code> 监听了这个值，从而 导致了死循环……</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/4a5d842312254132ae68afdf6f16ce41~tplv-k3u1fbpfcp-watermark.image" alt="2021-06-09-1053-3.svg" loading="lazy" referrerpolicy="no-referrer"></p>
<p>怎么解决呢？由于是 <code>obj</code> 变化引起的 <code>infinite loop</code> ，那么其实只要不监听 <code>obj</code> 就没有这回事了</p>
<p>🤪，这里可以利用一下 <code>setState</code> 的「回调函数」用法👇</p>
<pre><code class="hljs language-jsx copyable" lang="jsx"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">App</span>(<span class="hljs-params"></span>) </span>&#123;
    <span class="hljs-keyword">const</span> [obj, setObj] = useState(&#123;<span class="hljs-attr">a</span>: <span class="hljs-number">0</span>&#125;)
    <span class="hljs-keyword">const</span> &#123;a&#125; = obj;
    useEffect(<span class="hljs-function">() =></span> &#123;
        setObj(<span class="hljs-function">(<span class="hljs-params">state</span>) =></span> (&#123;
            ...state,
            <span class="hljs-attr">a</span>: <span class="hljs-number">1</span>
        &#125;))
    &#125;, [a])
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>案例2</li>
</ul>
<p>有时候你需要根据不同的「状态」来决定组件显示什么，那么通常就需要利用一个 <code>state</code> 来控制若干种「状态」的显示，从状态 1 到状态 2 的转化是异步的。一个简单的做法就是用 <code>useEffect</code> 来监听它。</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/823a3226b78048c3b7fa36558996cd39~tplv-k3u1fbpfcp-watermark.image" alt="2021-06-09-1053-2.svg" loading="lazy" referrerpolicy="no-referrer"></p>
<p>如果说这个状态有一部分依赖外部传入，另外一部分根据这个外部传入的状态的变化来进行对应的处理。举个例子👇</p>
<pre><code class="hljs language-jsx copyable" lang="jsx"><span class="hljs-keyword">export</span> <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">App</span>(<span class="hljs-params">&#123;outsider, wait&#125;</span>) </span>&#123;
    <span class="hljs-keyword">const</span> [state, setState] = useState(<span class="hljs-string">'INIT'</span>)
    useEffect(<span class="hljs-function">() =></span> &#123;
        <span class="hljs-comment">// 根据 ousider 处理 state 的值</span>
        <span class="hljs-keyword">if</span> (outsider === <span class="hljs-literal">true</span>) &#123;
                setState(<span class="hljs-string">'PENDING'</span>)
        &#125; <span class="hljs-keyword">else</span> &#123;
            <span class="hljs-keyword">if</span> (state === <span class="hljs-string">'PENDING'</span>) &#123;
                <span class="hljs-built_in">setTimeout</span>(<span class="hljs-function">() =></span> &#123;
                    setState(<span class="hljs-string">'RESOLVED'</span>)
                &#125;, wait)
            &#125;
        &#125;
    &#125;, [outsider, state])
    <span class="hljs-keyword">return</span> (
        <span class="hljs-comment">// 根据 state 来渲染不同的组件/样式</span>
    )
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>实际运行起来的话又是 <code>infinite loop</code> 了，可能你第一时间我想的一样，就是采用「案例1」的解法。但是注意，这里是有异步处理的，所以这里只能说是利用 <code>useRef</code> 来做一下简单的处理。</p>
<pre><code class="hljs language-jsx copyable" lang="jsx"><span class="hljs-keyword">export</span> <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">App</span>(<span class="hljs-params">&#123;outsider, wait&#125;</span>) </span>&#123;
    <span class="hljs-keyword">const</span> [state, setState] = useState(<span class="hljs-string">'INIT'</span>)
    <span class="hljs-keyword">const</span> stateRef = useRef(state)
    useEffect(<span class="hljs-function">() =></span> &#123;
        <span class="hljs-comment">// 根据 ousider 处理 state 的值</span>
        <span class="hljs-keyword">if</span> (outsider === <span class="hljs-literal">true</span>) &#123;
            setState(<span class="hljs-string">'PENDING'</span>)
            stateRef.current = <span class="hljs-string">'PENDING'</span>
        &#125; <span class="hljs-keyword">else</span> &#123;
            <span class="hljs-keyword">if</span> (stateRef.current === <span class="hljs-string">'PENDING'</span>) &#123;
                <span class="hljs-built_in">setTimeout</span>(<span class="hljs-function">() =></span> &#123;
                    setState(<span class="hljs-string">'RESOLVED'</span>)
                    stateRef.current = <span class="hljs-string">'RESOLVED'</span>
                &#125;, wait)
            &#125;
        &#125;
    &#125;, [outsider])
    <span class="hljs-keyword">return</span> (
        <span class="hljs-comment">// 根据 state 来渲染不同的组件/样式</span>
    )
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这样一来在 <code>useEffect</code> 中就不需要依赖 <code>state</code> ，而且能够根据 <code>state</code> 当前的值做出一些操作😄</p>
<h3 data-id="heading-3">小结</h3>
<p>在写 <code>hooks</code> 的时候，需要经常注意代码中是否有依赖 <code>state</code> 且 <code>setState</code> 的地方，通常直觉上的写法是会带来 <code>infinite loop</code> 的。</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/5acacc788b6b482f92d6ae7b80b471b2~tplv-k3u1fbpfcp-watermark.image" alt="2021-06-09-1053.svg" loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-4">获取不到最新的值</h2>
<p>新手 <code>hooks</code> 经常会碰到这类问题，下面是一个简单的例子👇</p>
<pre><code class="hljs language-jsx copyable" lang="jsx"><span class="hljs-keyword">import</span> &#123; useCallback, useEffect, useState &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">"react"</span>;

<span class="hljs-keyword">let</span> timeout = <span class="hljs-literal">null</span>;
<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">App</span>(<span class="hljs-params"></span>) </span>&#123;
  <span class="hljs-keyword">const</span> [count, setCount] = useState(<span class="hljs-number">0</span>);

  <span class="hljs-keyword">const</span> handleClick = useCallback(<span class="hljs-function">() =></span> &#123;
    setCount(count + <span class="hljs-number">1</span>);
    timeout = <span class="hljs-built_in">setTimeout</span>(<span class="hljs-function">() =></span> &#123;
      <span class="hljs-built_in">console</span>.log(<span class="hljs-string">"timeout"</span>, count);
      setCount(count + <span class="hljs-number">1</span>);
    &#125;, <span class="hljs-number">1000</span>);
  &#125;, [count]);

  useEffect(<span class="hljs-function">() =></span> &#123;
    <span class="hljs-keyword">return</span> <span class="hljs-function">() =></span> &#123;
      <span class="hljs-built_in">clearTimeout</span>(timeout);
    &#125;;
  &#125;, []);

  <span class="hljs-keyword">return</span> (
    <span class="xml"><span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">className</span>=<span class="hljs-string">"App"</span>></span>
      <span class="hljs-tag"><<span class="hljs-name">p</span>></span>&#123;count&#125;<span class="hljs-tag"></<span class="hljs-name">p</span>></span>
      <span class="hljs-tag"><<span class="hljs-name">button</span> <span class="hljs-attr">onClick</span>=<span class="hljs-string">&#123;handleClick&#125;</span>></span>click me<span class="hljs-tag"></<span class="hljs-name">button</span>></span>
    <span class="hljs-tag"></<span class="hljs-name">div</span>></span></span>
  );
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>运行之后你会发现，每次 <code>console.log</code> 打印出来的都是上一次 <code>count + 1</code> 前的结果，而这其实就和 <code>useState</code> 实现有关系了，这里仅截取源码中的一小部分实现👇</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/857024e2b5b54c86a3ed03a6e5d6f433~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>可以看出，从 <code>useState</code> 中解构出来的是原数据的值而非引用，所以在上面的例子中，在 <code>setTimeout</code> 里拿不到最新的 <code>count</code> 值。</p>
<h2 data-id="heading-5">参考资料</h2>
<p><a href="https://www.seangroff.dev/useeffect-state-trap/" target="_blank" rel="nofollow noopener noreferrer">Setting State based on Previous State in useEffect - Its a trap!</a></p></div>  
</div>
            