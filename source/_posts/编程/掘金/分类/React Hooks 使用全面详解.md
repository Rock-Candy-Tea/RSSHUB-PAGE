
---
title: 'React Hooks 使用全面详解'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=4117'
author: 掘金
comments: false
date: Sun, 13 Jun 2021 00:20:48 GMT
thumbnail: 'https://picsum.photos/400/300?random=4117'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>参考文章：</p>
<p><a href="https://juejin.cn/post/6844903985338400782" target="_blank">juejin.cn/post/684490…</a></p>
<p><a href="https://juejin.cn/post/6844903958968795149" target="_blank">juejin.cn/post/684490…</a></p>
<p><a href="https://juejin.cn/post/6844904074433789959" target="_blank">juejin.cn/post/684490…</a></p>
<h2 data-id="heading-0">1. Hooks解决的问题</h2>
<p><strong>（1）class组件的不足</strong></p>
<ul>
<li>状态逻辑难复用：</li>
</ul>
<p>在组件之间复用状态逻辑很难，可能要用到 render props （渲染属性）或者 HOC（高阶组件），但无论是渲染属性，还是高阶组件，都会在原先的组件外包裹一层父容器（一般都是 div 元素），导致层级冗余趋向复杂难以维护：</p>
<ul>
<li>在生命周期函数中混杂不相干的逻辑：</li>
</ul>
<p>在生命周期函数中混杂不相干的逻辑（如：在 componentDidMount 中注册事件以及其他的逻辑，在 componentWillUnmount 中卸载事件，这样分散不集中的写法，很容易写出 bug ）</p>
<p>类组件中到处都是对状态的访问和处理，导致组件难以拆分成更小的组件</p>
<ul>
<li>this 指向问题：</li>
</ul>
<p>父组件给子组件传递函数时，必须绑定 this</p>
<p><strong>（2）hooks的优势</strong></p>
<ul>
<li>能优化类组件的三大问题</li>
<li>能在无需修改组件结构的情况下复用状态逻辑（自定义 Hooks ）</li>
<li>能将组件中相互关联的部分拆分成更小的函数（比如设置订阅或请求数据）</li>
<li>副作用的关注点分离：副作用指那些没有发生在数据向视图转换过程中的逻辑，如 ajax 请求、访问原生dom元素、本地持久化缓存、绑定/解绑事件、添加订阅、设置定时器、记录日志等。以往这些副作用都是写在类组件生命周期函数中的。而useEffect 在全部渲染完毕后才会执行，useLayoutEffect 会在浏览器 layout 之后，painting 之前执行。</li>
</ul>
<h2 data-id="heading-1">2. Hooks使用前提</h2>
<ul>
<li>只能在函数内部的最外层调用 Hook，不要在循环、条件判断或者子函数中调用</li>
<li>只能在 React 的函数组件中调用 Hook，不要在其他 JavaScript 函数中调用</li>
</ul>
<h2 data-id="heading-2">3. useState</h2>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">import</span> &#123; useState &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'react'</span>;

<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">Example</span>(<span class="hljs-params"></span>) </span>&#123;
  <span class="hljs-keyword">const</span> [count, setCount] = useState(<span class="hljs-number">0</span>);

  <span class="hljs-keyword">return</span> (
    <span class="xml"><span class="hljs-tag"><<span class="hljs-name">div</span>></span>
      <span class="hljs-tag"><<span class="hljs-name">p</span>></span>You clicked &#123;count&#125; times<span class="hljs-tag"></<span class="hljs-name">p</span>></span>
      <span class="hljs-tag"><<span class="hljs-name">button</span> <span class="hljs-attr">onClick</span>=<span class="hljs-string">&#123;()</span> =></span> setCount(count + 1)&#125;>
        Click me
      <span class="hljs-tag"></<span class="hljs-name">button</span>></span>
    <span class="hljs-tag"></<span class="hljs-name">div</span>></span></span>
  );
&#125;

<span class="copy-code-btn">复制代码</span></code></pre>
<p>useState 会返回一个数组：一个 state，一个用于更新 state 的函数</p>
<p>useState 唯一的参数就是初始 state，在初始化渲染期间，返回的状态 (state) 与传入的第一个参数 (initialState) 值相同，</p>
<p><strong>注意事项：</strong></p>
<ul>
<li>React 假设当你多次调用 useState 的时候，你能保证每次渲染时它们的调用顺序是不变的。<strong>因为react是根据每个useState定义时的顺序来确定你在更新State值时更新的是哪个state</strong></li>
<li>你可以在事件处理函数中或其他一些地方调用这个函数。它类似 class 组件的 this.setState，但是它不会把新的 state 和旧的 state 进行合并，而是直接替换</li>
<li>initialState 参数只会在组件的初始化渲染中起作用，后续渲染时会被忽略</li>
<li>Hook 内部使用 Object.is 来比较新/旧 state 是否相等，与 class 组件中的 setState 方法不同，如果你修改状态的时候，传的状态值没有变化，则不重新渲染</li>
<li>useState不能直接存储函数或函数组件，他会调用该函数并且将函数的返回值作为最终state值进行存储或更新。如果必须这么做可以作为一个数组的元素或对象的某个属性进行存储</li>
<li>useState没有设置类似class组件中的setState的回调函数来拿到最新state然后进行后续操作；可通过useEffect并设置相应依赖来实现。因为useEffect就是在渲染完成后调用的</li>
<li></li>
</ul>
<p><strong>useState在异步操作中的状态不同步问题:</strong></p>
<p>函数的运行是独立的，每个函数都有一份独立的作用域。函数的变量是保存在运行时的作用域里面。当我们有异步操作的时候，经常会碰到异步回调的变量引用是之前的，也就是旧的（这里也可以理解成闭包）。比如下面的一个例子：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">import</span> React, &#123; useState &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">"react"</span>;
​
<span class="hljs-keyword">const</span> Counter = <span class="hljs-function">() =></span> &#123;
  <span class="hljs-keyword">const</span> [counter, setCounter] = useState(<span class="hljs-number">0</span>);
​
  <span class="hljs-keyword">const</span> onAlertButtonClick = <span class="hljs-function">() =></span> &#123;
    <span class="hljs-built_in">setTimeout</span>(<span class="hljs-function">() =></span> &#123;
      alert(<span class="hljs-string">"Value: "</span> + counter);
    &#125;, <span class="hljs-number">3000</span>);
  &#125;;
​
  <span class="hljs-keyword">return</span> (
    <span class="xml"><span class="hljs-tag"><<span class="hljs-name">div</span>></span>
      <span class="hljs-tag"><<span class="hljs-name">p</span>></span>You clicked &#123;counter&#125; times.<span class="hljs-tag"></<span class="hljs-name">p</span>></span>
      <span class="hljs-tag"><<span class="hljs-name">button</span> <span class="hljs-attr">onClick</span>=<span class="hljs-string">&#123;()</span> =></span> setCounter(counter + 1)&#125;>Click me<span class="hljs-tag"></<span class="hljs-name">button</span>></span>
      <span class="hljs-tag"><<span class="hljs-name">button</span> <span class="hljs-attr">onClick</span>=<span class="hljs-string">&#123;onAlertButtonClick&#125;</span>></span>
        Show me the value in 3 seconds
      <span class="hljs-tag"></<span class="hljs-name">button</span>></span>
    <span class="hljs-tag"></<span class="hljs-name">div</span>></span></span>
  );
&#125;;
​
<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> Counter;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>当你点击Show me the value in 3 seconds的后，紧接着点击Click me使得counter的值从0变成1。三秒后，定时器触发，但alert出来的是0（旧值），但我们希望的结果是当前的状态1。</p>
<p>这个问题在class component不会出现，因为class component的属性和方法都存放在一个instance上，调用方式是：this.state.xxx和this.method()。因为每次都是从一个不变的instance上进行取值，所以不存在引用是旧的问题。</p>
<p>除了setTimout这种异步，还有类似事件监听函数（比如滚动监听的回调函数）中访问State也会是旧的</p>
<p>这个问题目前的普遍解决方案是使用<code>useRef</code>（见下方）</p>
<h2 data-id="heading-3">4. useEffect</h2>
<p>什么是React中的副作用操作？</p>
<blockquote>
<p>指那些没有发生在数据向视图转换过程中的逻辑，如 ajax 请求、访问原生dom 元素、本地持久化缓存、绑定/解绑事件、添加订阅、设置定时器、记录日志等。</p>
</blockquote>
<p>副作用操作可以分两类：<strong>需要清除的（例如事件绑定/解绑）和不需要清除的</strong>。</p>
<p>原先在函数组件内（这里指在 React 渲染阶段）改变 dom 、发送 ajax 请求以及执行其他包含副作用的操作都是不被允许的，因为这可能会产生莫名其妙的 bug 并破坏 UI 的一致性</p>
<p>一个需求实现：<strong>需要实时让document.title显示你最新的点击次数(coutnt)</strong></p>
<p>class组件实现：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Counter</span> <span class="hljs-keyword">extends</span> <span class="hljs-title">React</span>.<span class="hljs-title">Component</span></span>&#123;
    state = &#123;<span class="hljs-attr">number</span>:<span class="hljs-number">0</span>&#125;;
    add = <span class="hljs-function">()=></span>&#123;
        <span class="hljs-built_in">this</span>.setState(&#123;<span class="hljs-attr">number</span>:<span class="hljs-built_in">this</span>.state.number+<span class="hljs-number">1</span>&#125;);
    &#125;;
    <span class="hljs-function"><span class="hljs-title">componentDidMount</span>(<span class="hljs-params"></span>)</span>&#123;
        <span class="hljs-built_in">this</span>.changeTitle();
    &#125;
    <span class="hljs-function"><span class="hljs-title">componentDidUpdate</span>(<span class="hljs-params"></span>)</span>&#123;
        <span class="hljs-built_in">this</span>.changeTitle();
    &#125;
    changeTitle = <span class="hljs-function">()=></span>&#123;
        <span class="hljs-built_in">document</span>.title = <span class="hljs-string">`你已经点击了<span class="hljs-subst">$&#123;<span class="hljs-built_in">this</span>.state.number&#125;</span>次`</span>;
    &#125;;
    <span class="hljs-function"><span class="hljs-title">render</span>(<span class="hljs-params"></span>)</span>&#123;
        <span class="hljs-keyword">return</span> (
            <span class="xml"><span class="hljs-tag"><></span>
              <span class="hljs-tag"><<span class="hljs-name">p</span>></span>&#123;this.state.number&#125;<span class="hljs-tag"></<span class="hljs-name">p</span>></span>
              <span class="hljs-tag"><<span class="hljs-name">button</span> <span class="hljs-attr">onClick</span>=<span class="hljs-string">&#123;this.add&#125;</span>></span>+<span class="hljs-tag"></<span class="hljs-name">button</span>></span>
            <span class="hljs-tag"></></span></span>
        )
    &#125;
&#125;

<span class="copy-code-btn">复制代码</span></code></pre>
<p>因为需要实时让document.title显示你最新的点击次数(coutnt)，所以就必须在componentDidMount 或 componentDidUpdate中编写重复的代码来重新设置document.title</p>
<p>hooks实现：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">import</span> React,&#123;Component,useState,useEffect&#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'react'</span>;
<span class="hljs-keyword">import</span> ReactDOM <span class="hljs-keyword">from</span> <span class="hljs-string">'react-dom'</span>;
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">Counter</span>(<span class="hljs-params"></span>)</span>&#123;
    <span class="hljs-keyword">const</span> [number,setNumber] = useState(<span class="hljs-number">0</span>);
    <span class="hljs-comment">// useEffect里面的这个函数会在第一次渲染之后和更新完成后执行</span>
    <span class="hljs-comment">// 相当于 componentDidMount 和 componentDidUpdate:</span>
    useEffect(<span class="hljs-function">() =></span> &#123;
        <span class="hljs-built_in">document</span>.title = <span class="hljs-string">`你点击了<span class="hljs-subst">$&#123;number&#125;</span>次`</span>;
    &#125;);
    <span class="hljs-keyword">return</span> (
        <span class="xml"><span class="hljs-tag"><></span>
            <span class="hljs-tag"><<span class="hljs-name">p</span>></span>&#123;number&#125;<span class="hljs-tag"></<span class="hljs-name">p</span>></span>
            <span class="hljs-tag"><<span class="hljs-name">button</span> <span class="hljs-attr">onClick</span>=<span class="hljs-string">&#123;()</span>=></span>setNumber(number+1)&#125;>+<span class="hljs-tag"></<span class="hljs-name">button</span>></span>
        <span class="hljs-tag"></></span></span>
    )
&#125;
ReactDOM.render(<span class="xml"><span class="hljs-tag"><<span class="hljs-name">Counter</span> /></span></span>, <span class="hljs-built_in">document</span>.getElementById(<span class="hljs-string">'root'</span>));

<span class="copy-code-btn">复制代码</span></code></pre>
<p>useEffect 就是一个 Effect Hook，给函数组件增加了操作副作用的能力。它跟 class 组件中的 <code>componentDidMount</code>、<code>componentDidUpdate</code> 和 <code>componentWillUnmount</code> 具有相同的用途，只不过被合并成了一个 API</p>
<p>与 componentDidMount 或 componentDidUpdate 不同，使用 useEffect 调度的 effect 不会阻塞浏览器更新屏幕，这让你的应用看起来响应更快。大多数情况下，effect 不需要同步地执行。在个别情况下（例如测量布局），有单独的 useLayoutEffect Hook 供你使用，其 API 与 useEffect 相同。</p>
<h3 data-id="heading-4">4.1 清除副作用</h3>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">Counter</span>(<span class="hljs-params"></span>)</span>&#123;
    <span class="hljs-keyword">let</span> [number,setNumber] = useState(<span class="hljs-number">0</span>);
    <span class="hljs-keyword">let</span> [text,setText] = useState(<span class="hljs-string">''</span>);
    <span class="hljs-comment">// 相当于componentDidMount 和 componentDidUpdate</span>
    useEffect(<span class="hljs-function">()=></span>&#123;
        <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'开启一个新的定时器'</span>)
        <span class="hljs-keyword">let</span> $timer = <span class="hljs-built_in">setInterval</span>(<span class="hljs-function">()=></span>&#123;
            setNumber(<span class="hljs-function"><span class="hljs-params">number</span>=></span>number+<span class="hljs-number">1</span>);
        &#125;,<span class="hljs-number">1000</span>);
        <span class="hljs-comment">// useEffect 如果返回一个函数的话，该函数会在组件卸载和更新时调用</span>
        <span class="hljs-comment">// useEffect 在执行副作用函数之前，会先调用上一次返回的函数</span>
        <span class="hljs-comment">// 如果要清除副作用，要么返回一个清除副作用的函数</span>
       <span class="hljs-keyword">return</span> <span class="hljs-function">()=></span>&#123;
            <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'destroy effect'</span>);
            <span class="hljs-built_in">clearInterval</span>($timer);
        &#125; 
    &#125;);
    <span class="hljs-comment">// &#125;,[]);//要么在这里传入一个空的依赖项数组，这样就不会去重复执行</span>
    <span class="hljs-keyword">return</span> (
        <span class="xml"><span class="hljs-tag"><></span>
          <span class="hljs-tag"><<span class="hljs-name">input</span> <span class="hljs-attr">value</span>=<span class="hljs-string">&#123;text&#125;</span> <span class="hljs-attr">onChange</span>=<span class="hljs-string">&#123;(event)</span>=></span>setText(event.target.value)&#125;/>
          <span class="hljs-tag"><<span class="hljs-name">p</span>></span>&#123;number&#125;<span class="hljs-tag"></<span class="hljs-name">p</span>></span>
          <span class="hljs-tag"><<span class="hljs-name">button</span>></span>+<span class="hljs-tag"></<span class="hljs-name">button</span>></span>
        <span class="hljs-tag"></></span></span>
    )
&#125;

<span class="copy-code-btn">复制代码</span></code></pre>
<p>useEffect 接收一个函数，该函数会在组件渲染到屏幕之后才执行，该函数有要求：<strong>要么返回一个能清除副作用的函数，要么就不返回任何内容</strong></p>
<p>默认情况下，useEffect在第一次渲染之后和每次更新之后都会执行。而useEffect 接收的函数参数所返回的清除副作用的函数则会在组件更新和卸载前执行，然后更新后执行useEffect 接收的函数。然后等待下一次组件更新或卸载，执行清除副作用的函数......如此循环往复</p>
<h3 data-id="heading-5">4.2  跳过 effect 进行性能优化</h3>
<p>默认情况下，useEffect在每次更新之后都会执行</p>
<p>有时候，我们只想useEffect只在组件挂载时执行，然后卸载时执行清除副作用函数，不想更新时也执行useEffect（比如原生事件的绑定/解绑）或者只想让指定state发生更新时才执行useEffect（比如某些state更新后拿到最新state进行后续操作）</p>
<p>此时，你可以通知 React 跳过对 effect 的调用，只要传递数组作为 useEffect 的第二个可选参数即可：</p>
<ul>
<li>如果想执行只运行一次的 effect（仅在组件挂载和卸载时执行），可以传递一个空数组（[]）作为第二个参数。这就告诉 React 你的effect 不依赖于 props 或 state 中的任何值，所以它永远都不需要重复执行</li>
<li>如果指定state发生更新时才执行useEffect，可以传递一个包含指定state元素的的数组作为第二个参数</li>
</ul>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">Counter</span>(<span class="hljs-params"></span>)</span>&#123;
    <span class="hljs-keyword">let</span> [number,setNumber] = useState(<span class="hljs-number">0</span>);
    <span class="hljs-keyword">let</span> [text,setText] = useState(<span class="hljs-string">''</span>);
    <span class="hljs-comment">// 相当于componentDidMount 和 componentDidUpdate</span>
    useEffect(<span class="hljs-function">()=></span>&#123;
        <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'useEffect'</span>);
        <span class="hljs-keyword">let</span> $timer = <span class="hljs-built_in">setInterval</span>(<span class="hljs-function">()=></span>&#123;
            setNumber(<span class="hljs-function"><span class="hljs-params">number</span>=></span>number+<span class="hljs-number">1</span>);
        &#125;,<span class="hljs-number">1000</span>);
    &#125;,[text]);<span class="hljs-comment">// 数组表示 effect 依赖的变量，只有当这个变量发生改变之后才会重新执行 efffect 函数</span>
    <span class="hljs-keyword">return</span> (
        <span class="xml"><span class="hljs-tag"><></span>
          <span class="hljs-tag"><<span class="hljs-name">input</span> <span class="hljs-attr">value</span>=<span class="hljs-string">&#123;text&#125;</span> <span class="hljs-attr">onChange</span>=<span class="hljs-string">&#123;(event)</span>=></span>setText(event.target.value)&#125;/>
          <span class="hljs-tag"><<span class="hljs-name">p</span>></span>&#123;number&#125;<span class="hljs-tag"></<span class="hljs-name">p</span>></span>
          <span class="hljs-tag"><<span class="hljs-name">button</span>></span>+<span class="hljs-tag"></<span class="hljs-name">button</span>></span>
        <span class="hljs-tag"></></span></span>
    )
&#125;

<span class="copy-code-btn">复制代码</span></code></pre>
<blockquote>
<p>注意：无论你是否指定了useEffct的第二个参数，useEffect永远都会在组件挂载时执行一次</p>
</blockquote>
<h3 data-id="heading-6">4.3  使用多个useEffect</h3>
<p>useEffect可以声明多个，React 将按照 effect 声明的顺序依次调用组件中的每一个 effect</p>
<p>我们可以根据具体副作用操作的性质分类将不同种类的操作放到多个useEffect中</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// Hooks 版</span>
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">FriendStatusWithCounter</span>(<span class="hljs-params">props</span>) </span>&#123;
  <span class="hljs-keyword">const</span> [count, setCount] = useState(<span class="hljs-number">0</span>);
<span class="hljs-comment">//dom操作相关的effect</span>
  useEffect(<span class="hljs-function">() =></span> &#123;
    <span class="hljs-built_in">document</span>.title = <span class="hljs-string">`You clicked <span class="hljs-subst">$&#123;count&#125;</span> times`</span>;
  &#125;);

  <span class="hljs-keyword">const</span> [isOnline, setIsOnline] = useState(<span class="hljs-literal">null</span>);
<span class="hljs-comment">//订阅/取消订阅的相关effect</span>
  useEffect(<span class="hljs-function">() =></span> &#123;
    <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">handleStatusChange</span>(<span class="hljs-params">status</span>) </span>&#123;
      setIsOnline(status.isOnline);
    &#125;

    ChatAPI.subscribeToFriendStatus(props.friend.id, handleStatusChange);
    <span class="hljs-keyword">return</span> <span class="hljs-function">() =></span> &#123;
      ChatAPI.unsubscribeFromFriendStatus(props.friend.id, handleStatusChange);
    &#125;;
  &#125;);
  <span class="hljs-comment">// ...</span>
&#125;

<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-7">4.4  useEffect 不能接收 async 作为回调函数</h3>
<p>在useEffect中发起异步请求是很常见的场景，由于异步请求通常都是封装好的异步方法，所以新手很容易写成下面这样：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">App</span>(<span class="hljs-params"></span>) </span>&#123;
  <span class="hljs-keyword">const</span> [data, setData] = useState(&#123; <span class="hljs-attr">hits</span>: [] &#125;);
  <span class="hljs-comment">// 注意 async 的位置</span>
  <span class="hljs-comment">// 这种写法，虽然可以运行，但是会发出警告</span>
  <span class="hljs-comment">// 每个带有 async 修饰的函数都返回一个隐含的 promise</span>
  <span class="hljs-comment">// 但是 useEffect 函数有要求：要么返回清除副作用函数，要么就不返回任何内容</span>
  useEffect(<span class="hljs-keyword">async</span> () => &#123;
    <span class="hljs-keyword">const</span> result = <span class="hljs-keyword">await</span> axios(
      <span class="hljs-string">'https://hn.algolia.com/api/v1/search?query=redux'</span>,
    );
    setData(result.data);
  &#125;, []);
  <span class="hljs-keyword">return</span> (
    <span class="xml"><span class="hljs-tag"><<span class="hljs-name">ul</span>></span>
      &#123;data.hits.map(item => (
        <span class="hljs-tag"><<span class="hljs-name">li</span> <span class="hljs-attr">key</span>=<span class="hljs-string">&#123;item.objectID&#125;</span>></span>
          <span class="hljs-tag"><<span class="hljs-name">a</span> <span class="hljs-attr">href</span>=<span class="hljs-string">&#123;item.url&#125;</span>></span>&#123;item.title&#125;<span class="hljs-tag"></<span class="hljs-name">a</span>></span>
        <span class="hljs-tag"></<span class="hljs-name">li</span>></span>
      ))&#125;
    <span class="hljs-tag"></<span class="hljs-name">ul</span>></span></span>
  );
&#125;

<span class="copy-code-btn">复制代码</span></code></pre>
<p>更优雅的写法：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">App</span>(<span class="hljs-params"></span>) </span>&#123;
  <span class="hljs-keyword">const</span> [data, setData] = useState(&#123; <span class="hljs-attr">hits</span>: [] &#125;);
  useEffect(<span class="hljs-function">() =></span> &#123;
    <span class="hljs-comment">// 更优雅的方式</span>
    <span class="hljs-comment">//将异步请求封成一个独立async函数然后在useEffect中调用</span>
    <span class="hljs-keyword">const</span> fetchData = <span class="hljs-keyword">async</span> () => &#123;
      <span class="hljs-keyword">const</span> result = <span class="hljs-keyword">await</span> axios(
        <span class="hljs-string">'https://hn.algolia.com/api/v1/search?query=redux'</span>,
      );
      setData(result.data);
    &#125;;
    fetchData();
  &#125;, []);
  <span class="hljs-keyword">return</span> (
    <span class="xml"><span class="hljs-tag"><<span class="hljs-name">ul</span>></span>
      &#123;data.hits.map(item => (
        <span class="hljs-tag"><<span class="hljs-name">li</span> <span class="hljs-attr">key</span>=<span class="hljs-string">&#123;item.objectID&#125;</span>></span>
          <span class="hljs-tag"><<span class="hljs-name">a</span> <span class="hljs-attr">href</span>=<span class="hljs-string">&#123;item.url&#125;</span>></span>&#123;item.title&#125;<span class="hljs-tag"></<span class="hljs-name">a</span>></span>
        <span class="hljs-tag"></<span class="hljs-name">li</span>></span>
      ))&#125;
    <span class="hljs-tag"></<span class="hljs-name">ul</span>></span></span>
  );
&#125;

<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-8">5. useReducer</h2>
<p>useReducer 和 redux 中 reducer 很像。useState 内部就是靠 useReducer 来实现的</p>
<p>useReducer接收两个参数：reducer函数（含preState和action两个参数）和初始化的state。</p>
<p>useReducer返回值为一个数组，包含最新的state和dispatch函数（用来触发reducer函数，计算对应的state）。</p>
<pre><code class="hljs language-js copyable" lang="js">    <span class="hljs-comment">// 官方 useReducer Demo</span>
    <span class="hljs-comment">// 第一个参数：应用的初始化</span>
    <span class="hljs-keyword">const</span> initialState = &#123;<span class="hljs-attr">count</span>: <span class="hljs-number">0</span>&#125;;

    <span class="hljs-comment">// 第二个参数：state的reducer处理函数</span>
    <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">reducer</span>(<span class="hljs-params">state, action</span>) </span>&#123;
        <span class="hljs-keyword">switch</span> (action.type) &#123;
            <span class="hljs-keyword">case</span> <span class="hljs-string">'increment'</span>:
              <span class="hljs-keyword">return</span> &#123;<span class="hljs-attr">count</span>: state.count + <span class="hljs-number">1</span>&#125;;
            <span class="hljs-keyword">case</span> <span class="hljs-string">'decrement'</span>:
               <span class="hljs-keyword">return</span> &#123;<span class="hljs-attr">count</span>: state.count - <span class="hljs-number">1</span>&#125;;
            <span class="hljs-keyword">default</span>:
                <span class="hljs-keyword">throw</span> <span class="hljs-keyword">new</span> <span class="hljs-built_in">Error</span>();
        &#125;
    &#125;

    <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">Counter</span>(<span class="hljs-params"></span>) </span>&#123;
        <span class="hljs-comment">// 返回值：最新的state和dispatch函数</span>
        <span class="hljs-keyword">const</span> [state, dispatch] = useReducer(reducer, initialState);
        <span class="hljs-keyword">return</span> (
            <span class="xml"><span class="hljs-tag"><></span>
                // useReducer会根据dispatch的action，返回最终的state，并触发rerender
                Count: &#123;state.count&#125;
                // dispatch 用来接收一个 action参数「reducer中的action」，用来触发reducer函数，更新最新的状态
                <span class="hljs-tag"><<span class="hljs-name">button</span> <span class="hljs-attr">onClick</span>=<span class="hljs-string">&#123;()</span> =></span> dispatch(&#123;type: 'increment'&#125;)&#125;>+<span class="hljs-tag"></<span class="hljs-name">button</span>></span>
                <span class="hljs-tag"><<span class="hljs-name">button</span> <span class="hljs-attr">onClick</span>=<span class="hljs-string">&#123;()</span> =></span> dispatch(&#123;type: 'decrement'&#125;)&#125;>-<span class="hljs-tag"></<span class="hljs-name">button</span>></span>
            <span class="hljs-tag"></></span></span>
        );
    &#125;

<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>选择useReducer还是useState：</strong></p>
<ul>
<li>如果你的页面state很简单，可以直接使用useState</li>
<li>如果你的页面state比较复杂（state是一个对象或者state非常多散落在各处）请使用userReducer</li>
<li>对于复杂的state操作逻辑（比如某项操作同时需要操作或更新多个state值），嵌套的state的对象，推荐使用useReducer</li>
<li>如果你的页面组件层级比较深，并且需要子组件触发state的变化，可以考虑useReducer + useContext</li>
</ul>
<h2 data-id="heading-9">6. useContext</h2>
<p>接收一个 context 对象（React.createContext 的返回值）并返回该 context 的当前值。当前的 context 值由上层组件中距离当前组件最近的 <MyContext.Provider> 的 value prop 决定</p>
<p>当组件上层最近的 <MyContext.Provider> 更新时，该 Hook 会触发重渲染，并使用最新传递给 MyContext provider 的 context value 值</p>
<p><strong>useContext(MyContext) 相当于 class 组件中的 <code>static contextType = MyContext </code>或者<code> <MyContext.Consumer></code></strong></p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> themes = &#123;
  <span class="hljs-attr">light</span>: &#123;
    <span class="hljs-attr">foreground</span>: <span class="hljs-string">"#000000"</span>,
    <span class="hljs-attr">background</span>: <span class="hljs-string">"#eeeeee"</span>
  &#125;,
  <span class="hljs-attr">dark</span>: &#123;
    <span class="hljs-attr">foreground</span>: <span class="hljs-string">"#ffffff"</span>,
    <span class="hljs-attr">background</span>: <span class="hljs-string">"#222222"</span>
  &#125;
&#125;;

<span class="hljs-keyword">const</span> ThemeContext = React.createContext(themes.light);

<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">App</span>(<span class="hljs-params"></span>) </span>&#123;
  <span class="hljs-keyword">return</span> (
    <span class="xml"><span class="hljs-tag"><<span class="hljs-name">ThemeContext.Provider</span> <span class="hljs-attr">value</span>=<span class="hljs-string">&#123;themes.dark&#125;</span>></span>
      <span class="hljs-tag"><<span class="hljs-name">Toolbar</span> /></span>
    <span class="hljs-tag"></<span class="hljs-name">ThemeContext.Provider</span>></span></span>
  );
&#125;

<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">Toolbar</span>(<span class="hljs-params">props</span>) </span>&#123;
  <span class="hljs-keyword">return</span> (
    <span class="xml"><span class="hljs-tag"><<span class="hljs-name">div</span>></span>
      <span class="hljs-tag"><<span class="hljs-name">ThemedButton</span> /></span>
    <span class="hljs-tag"></<span class="hljs-name">div</span>></span></span>
  );
&#125;

<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">ThemedButton</span>(<span class="hljs-params"></span>) </span>&#123;
  <span class="hljs-keyword">const</span> theme = useContext(ThemeContext);
  <span class="hljs-keyword">return</span> (
    <span class="xml"><span class="hljs-tag"><<span class="hljs-name">button</span> <span class="hljs-attr">style</span>=<span class="hljs-string">&#123;&#123;</span> <span class="hljs-attr">background:</span> <span class="hljs-attr">theme.background</span>, <span class="hljs-attr">color:</span> <span class="hljs-attr">theme.foreground</span> &#125;&#125;></span>
      I am styled by theme context!
    <span class="hljs-tag"></<span class="hljs-name">button</span>></span></span>
  );
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>使用useContext和useReducer模拟实现简易Redux：</strong></p>
<p>Provider组件：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">import</span> React, &#123; useReducer &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'react'</span>
<span class="hljs-keyword">import</span> <span class="hljs-string">'./App.css'</span>
<span class="hljs-keyword">import</span> ComponentA <span class="hljs-keyword">from</span> <span class="hljs-string">'./components/ComponentA'</span>
<span class="hljs-keyword">import</span> ComponentB <span class="hljs-keyword">from</span> <span class="hljs-string">'./components/ComponentB'</span>
<span class="hljs-keyword">import</span> ComponentC <span class="hljs-keyword">from</span> <span class="hljs-string">'./components/ComponentC'</span>
<span class="hljs-keyword">const</span> initialState = <span class="hljs-number">0</span>
<span class="hljs-keyword">const</span> reducer = <span class="hljs-function">(<span class="hljs-params">state, action</span>) =></span> &#123;
    <span class="hljs-keyword">switch</span> (action) &#123;
        <span class="hljs-keyword">case</span> <span class="hljs-string">'increment'</span>:
            <span class="hljs-keyword">return</span> state + <span class="hljs-number">1</span>
        <span class="hljs-keyword">case</span> <span class="hljs-string">'decrement'</span>:
            <span class="hljs-keyword">return</span> state - <span class="hljs-number">1</span>
        <span class="hljs-keyword">case</span> <span class="hljs-string">'reset'</span>:
            <span class="hljs-keyword">return</span> initialState
        <span class="hljs-attr">default</span>:
            <span class="hljs-keyword">return</span> state
    &#125;
&#125;

<span class="hljs-keyword">export</span> <span class="hljs-keyword">const</span> CountContext = React.createContext()

<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">App</span>(<span class="hljs-params"></span>) </span>&#123;
    <span class="hljs-keyword">const</span> [count, dispatch] = useReducer(reducer, initialState)
    <span class="hljs-keyword">return</span> (
        <span class="xml"><span class="hljs-tag"><<span class="hljs-name">CountContext.Provider</span>
            <span class="hljs-attr">value</span>=<span class="hljs-string">&#123;&#123;</span> <span class="hljs-attr">countState:</span> <span class="hljs-attr">count</span>, <span class="hljs-attr">countDispatch:</span> <span class="hljs-attr">dispatch</span> &#125;&#125;
        ></span>
            <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">className</span>=<span class="hljs-string">"App"</span>></span>
                &#123;count&#125;
                <span class="hljs-tag"><<span class="hljs-name">ComponentA</span> /></span>
                <span class="hljs-tag"><<span class="hljs-name">ComponentB</span> /></span>
                                <span class="hljs-tag"><<span class="hljs-name">ComponentC</span> /></span>
            <span class="hljs-tag"></<span class="hljs-name">div</span>></span>
        <span class="hljs-tag"></<span class="hljs-name">CountContext.Provider</span>></span></span>
    )
&#125;

<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> App    
<span class="copy-code-btn">复制代码</span></code></pre>
<p>Component A：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">//组件A</span>
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">ComponentA</span>(<span class="hljs-params"></span>) </span>&#123;
  <span class="hljs-keyword">const</span> countContext = useContext(CountContext)
  <span class="hljs-keyword">return</span> (
    <span class="xml"><span class="hljs-tag"><<span class="hljs-name">div</span>></span>
      Component A &#123;countContext.countState&#125;
      <span class="hljs-tag"><<span class="hljs-name">button</span> <span class="hljs-attr">onClick</span>=<span class="hljs-string">&#123;()</span> =></span> countContext.countDispatch('increment')&#125;>Increment<span class="hljs-tag"></<span class="hljs-name">button</span>></span>
            <span class="hljs-tag"><<span class="hljs-name">button</span> <span class="hljs-attr">onClick</span>=<span class="hljs-string">&#123;()</span> =></span> countContext.countDispatch('decrement')&#125;>Decrement<span class="hljs-tag"></<span class="hljs-name">button</span>></span>
            <span class="hljs-tag"><<span class="hljs-name">button</span> <span class="hljs-attr">onClick</span>=<span class="hljs-string">&#123;()</span> =></span> countContext.countDispatch('reset')&#125;>Reset<span class="hljs-tag"></<span class="hljs-name">button</span>></span>
    <span class="hljs-tag"></<span class="hljs-name">div</span>></span></span>
  )
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>Component B:</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">ComponentB</span>(<span class="hljs-params"></span>) </span>&#123;
  <span class="hljs-keyword">const</span> countContext = useContext(CountContext)
  <span class="hljs-keyword">return</span> (
    <span class="xml"><span class="hljs-tag"><<span class="hljs-name">div</span>></span>
      Component B &#123;countContext.countState&#125;
      <span class="hljs-tag"><<span class="hljs-name">button</span> <span class="hljs-attr">onClick</span>=<span class="hljs-string">&#123;()</span> =></span> countContext.countDispatch('increment')&#125;>Increment<span class="hljs-tag"></<span class="hljs-name">button</span>></span>
            <span class="hljs-tag"><<span class="hljs-name">button</span> <span class="hljs-attr">onClick</span>=<span class="hljs-string">&#123;()</span> =></span> countContext.countDispatch('decrement')&#125;>Decrement<span class="hljs-tag"></<span class="hljs-name">button</span>></span>
            <span class="hljs-tag"><<span class="hljs-name">button</span> <span class="hljs-attr">onClick</span>=<span class="hljs-string">&#123;()</span> =></span> countContext.countDispatch('reset')&#125;>Reset<span class="hljs-tag"></<span class="hljs-name">button</span>></span>
    <span class="hljs-tag"></<span class="hljs-name">div</span>></span></span>
  )
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-10">7. useRef</h2>
<p>useRef 返回一个可变的 ref 对象，其 .current 属性被初始化为传入的参数（initialValue）。返回的 ref 对象在组件的整个生命周期内保持不变</p>
<p>useRef 返回的 ref 对象在组件的整个生命周期内保持不变，也就是说每次重新渲染函数组件时，返回的ref 对象都是同一个。</p>
<p>但使用 React.createRef ，每次重新渲染组件都会重新创建 ref</p>
<p>示例：用useRef存储dom节点</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">Child</span>(<span class="hljs-params"></span>) </span>&#123;
    <span class="hljs-keyword">const</span> inputRef = useRef();
    <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'input===inputRef'</span>, input === inputRef);
    input = inputRef;
    <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">getFocus</span>(<span class="hljs-params"></span>) </span>&#123;
        inputRef.current.focus();
    &#125;
    <span class="hljs-keyword">return</span> (
        <span class="xml"><span class="hljs-tag"><></span>
            <span class="hljs-tag"><<span class="hljs-name">input</span> <span class="hljs-attr">type</span>=<span class="hljs-string">"text"</span> <span class="hljs-attr">ref</span>=<span class="hljs-string">&#123;inputRef&#125;</span> /></span>
            <span class="hljs-tag"><<span class="hljs-name">button</span> <span class="hljs-attr">onClick</span>=<span class="hljs-string">&#123;getFocus&#125;</span>></span>获得焦点<span class="hljs-tag"></<span class="hljs-name">button</span>></span>
        <span class="hljs-tag"></></span></span>
    )
&#125;

<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>用useRef解决useState异步更新不同步的问题：</strong></p>
<p>针对上面useState谈到的异步更新不同步的问题，用useRef返回的immutable RefObject（把值保存在current属性上）来保存state，<code>你可以把useRef存储的值看成class组件实例中通过this存储的属性</code>。然后取值方式从counter变成了： counterRef.current。如下：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">import</span> React, &#123; useState, useRef, useEffect &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">"react"</span>;
​
<span class="hljs-keyword">const</span> Counter = <span class="hljs-function">() =></span> &#123;
  <span class="hljs-keyword">const</span> [counter, setCounter] = useState(<span class="hljs-number">0</span>);
  <span class="hljs-keyword">const</span> counterRef = useRef(counter);
​
  <span class="hljs-keyword">const</span> onAlertButtonClick = <span class="hljs-function">() =></span> &#123;
    <span class="hljs-built_in">setTimeout</span>(<span class="hljs-function">() =></span> &#123;
      alert(<span class="hljs-string">"Value: "</span> + counterRef.current);
    &#125;, <span class="hljs-number">3000</span>);
  &#125;;
​
  useEffect(<span class="hljs-function">() =></span> &#123;
    counterRef.current = counter;
  &#125;);
​
  <span class="hljs-keyword">return</span> (
    <span class="xml"><span class="hljs-tag"><<span class="hljs-name">div</span>></span>
      <span class="hljs-tag"><<span class="hljs-name">p</span>></span>You clicked &#123;counter&#125; times.<span class="hljs-tag"></<span class="hljs-name">p</span>></span>
      <span class="hljs-tag"><<span class="hljs-name">button</span> <span class="hljs-attr">onClick</span>=<span class="hljs-string">&#123;()</span> =></span> setCounter(counter + 1)&#125;>Click me<span class="hljs-tag"></<span class="hljs-name">button</span>></span>
      <span class="hljs-tag"><<span class="hljs-name">button</span> <span class="hljs-attr">onClick</span>=<span class="hljs-string">&#123;onAlertButtonClick&#125;</span>></span>
        Show me the value in 3 seconds
      <span class="hljs-tag"></<span class="hljs-name">button</span>></span>
    <span class="hljs-tag"></<span class="hljs-name">div</span>></span></span>
  );
&#125;;
​
<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> Counter;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>React.forwardRef</strong></p>
<p>在useRef出来之前，由于函数组件是没有实例的，所以函数组件无法使用ref属性来获取dom引用，而对应的解决方法就是React.forwardRef：</p>
<p>TextInput函数组件：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> TextInput =  forwardRef(<span class="hljs-function">(<span class="hljs-params">props,ref</span>) =></span> &#123;
<span class="hljs-comment">//设置input标签node节点作为TextInput组件的ref引用</span>
  <span class="hljs-keyword">return</span> <span class="xml"><span class="hljs-tag"><<span class="hljs-name">input</span> <span class="hljs-attr">ref</span>=<span class="hljs-string">&#123;ref&#125;</span>></span><span class="hljs-tag"></<span class="hljs-name">input</span>></span></span>
&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">TextInputWithFocusButton</span>(<span class="hljs-params"></span>) </span>&#123;
  <span class="hljs-comment">// 关键代码</span>
  <span class="hljs-keyword">const</span> inputEl = useRef(<span class="hljs-literal">null</span>);
  <span class="hljs-keyword">const</span> onButtonClick = <span class="hljs-function">() =></span> &#123;
    <span class="hljs-comment">// 关键代码，`current` 指向已挂载到 DOM 上的文本输入元素</span>
    inputEl.current.focus();
  &#125;;
  <span class="hljs-keyword">return</span> (
    <span class="xml"><span class="hljs-tag"><></span>
      // 用useRef存储TextInput设置的ref引用
     
      <span class="hljs-tag"><<span class="hljs-name">TextInput</span> <span class="hljs-attr">ref</span>=<span class="hljs-string">&#123;inputEl&#125;</span>></span><span class="hljs-tag"></<span class="hljs-name">TextInput</span>></span>
      <span class="hljs-tag"><<span class="hljs-name">button</span> <span class="hljs-attr">onClick</span>=<span class="hljs-string">&#123;onButtonClick&#125;</span>></span>Focus the input<span class="hljs-tag"></<span class="hljs-name">button</span>></span>
    <span class="hljs-tag"></></span></span>
  );
<span class="copy-code-btn">复制代码</span></code></pre>
<p>上面例子说明<strong>forwardRef和useRef配合 可以在父组件中操作子组件的 ref 对象</strong></p>
<h2 data-id="heading-11">8. useCallback</h2>
<p>useCallback缓存一个函数，这个函数如果是由父组件作为props传递给子组件，或者自定义hooks里面的函数【通常自定义hooks里面的函数不会依赖于引用它的组件里面的数据】，这时候我们可以考虑缓存这个函数，好处:</p>
<ul>
<li>不用每次重新声明新的函数，避免释放内存、分配内存的计算资源浪费</li>
<li>子组件不会因为这个函数的变动重新渲染。【和React.memo搭配使用】</li>
</ul>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">Example</span>(<span class="hljs-params"></span>)</span>&#123;

    <span class="hljs-keyword">const</span> [count, setCount]= useState(<span class="hljs-number">1</span>);


    <span class="hljs-keyword">const</span> getNum = useCallback(<span class="hljs-function">() =></span> &#123;
        <span class="hljs-keyword">return</span> (<span class="hljs-number">555</span> * <span class="hljs-number">666666</span> )+count
        <span class="hljs-comment">//只有count值改变时，才会重新计算</span>
    &#125;,[count])

    <span class="hljs-keyword">const</span> Child = React.memo(<span class="hljs-function">(<span class="hljs-params">&#123;getNum&#125;</span>) =></span>&#123;
        <span class="hljs-keyword">return</span> <span class="xml"><span class="hljs-tag"><<span class="hljs-name">h4</span>></span>总和&#123;getNum()&#125;<span class="hljs-tag"></<span class="hljs-name">h4</span>></span></span>
    &#125;)

    <span class="hljs-keyword">return</span> <span class="xml"><span class="hljs-tag"><<span class="hljs-name">div</span>></span>
           <span class="hljs-tag"><<span class="hljs-name">Child</span> <span class="hljs-attr">getNum</span>=<span class="hljs-string">&#123;getNum&#125;/</span>></span>
        <span class="hljs-tag"><<span class="hljs-name">button</span> <span class="hljs-attr">onClick</span>=<span class="hljs-string">&#123;()</span> =></span> setCount(count + 1)&#125;>+1<span class="hljs-tag"></<span class="hljs-name">button</span>></span>
        <span class="hljs-tag"></<span class="hljs-name">div</span>></span></span>

&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>上面例子，将一个函数交给useCallBack处理并且作为props传递给memo包裹的子组件并子组件调用该方法，定义只有当coutn变化时才会触发子组件重新渲染</p>
<p>因为通过useCallBack包裹后的函数通过props传递给子组件的永远是该函数的引用</p>
<h2 data-id="heading-12">9. useMemo</h2>
<p>useMemo 主要用于渲染过程优化，两个参数依次是计算函数（通常是组件函数）和依赖状态列表，当依赖的状态发生改变时，才会触发计算函数的执行。如果没有指定依赖，则每一次渲染过程都会执行该计算函数。</p>
<p><strong>useMemo的返回值就是计算函数的返回值</strong></p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">Example</span>(<span class="hljs-params"></span>)</span>&#123;

    <span class="hljs-keyword">const</span> [count, setCount]= useState(<span class="hljs-number">1</span>);


    <span class="hljs-keyword">const</span> getNum = useMemo(<span class="hljs-function">() =></span> &#123;
        <span class="hljs-keyword">return</span> (<span class="hljs-number">555</span> * <span class="hljs-number">666666</span> )+count
        
        <span class="hljs-comment">//只有count值改变时，才会重新计算</span>
    &#125;,[count])

    <span class="hljs-keyword">return</span> <span class="xml"><span class="hljs-tag"><<span class="hljs-name">div</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">h4</span>></span>总和:&#123;getNum&#125;<span class="hljs-tag"></<span class="hljs-name">h4</span>></span>
        <span class="hljs-tag"><<span class="hljs-name">button</span> <span class="hljs-attr">onClick</span>=<span class="hljs-string">&#123;()</span> =></span> setCount(count + 1)&#125;>+1<span class="hljs-tag"></<span class="hljs-name">button</span>></span>
        <span class="hljs-tag"></<span class="hljs-name">div</span>></span></span>

&#125;

<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> Example;


<span class="copy-code-btn">复制代码</span></code></pre>
<p>上面例子只有当count变化时才会触发getNum函数的重新计算和渲染；如果不使用useMemo则任何一个state发生变化都会导致组件重新渲染进而导致getNum重新计算，耗费性能</p>
<p>注意：</p>
<blockquote>
<p>如果useMemo的返回值是作为props传给子组件的，当该值的类型是原始值时（string,number等），不需要使用useMemo。因为只要该值不变，react本身是不会重新渲染函数子组件的。如果是引用类型值，则可以使用useMemo，因为即使它的内容不变，但是引用会变。所以用useMemo来缓存它的引用</p>
</blockquote>
<p><strong>useMemo和useCallback的区别</strong>
useMemo 和  useCallback 接收的参数都是一样,第一个参数为回调 第二个参数为要依赖的数据</p>
<p><strong>共同作用:</strong></p>
<ul>
<li>仅仅 依赖数据 发生变化,才会重新计算结果，也就是起到缓存的作用。</li>
</ul>
<p><strong>两者区别:</strong></p>
<ul>
<li>useMemo 计算结果是<strong>计算函数返回来的值</strong>,主要用于 缓存计算结果的值，应用场景如: 需要计算的状态</li>
<li>useCallback计算结果是<strong>计算函数</strong>，主要用于 缓存函数，应用场景如:需要缓存的函数，因为函数式组件每次任何一个 state 的变化
整个组件 都会被重新刷新，一些函数是没有必要被重新刷新的，此时就应该缓存起来，提高性能，和减少资源浪费。</li>
</ul>
<h2 data-id="heading-13">10. 自定义Hook</h2>
<p><code>自定义 Hook 必须以 use 开头吗？</code></p>
<blockquote>
<p>必须如此。这个约定非常重要。不遵循的话，由于无法判断某个函数是否包含对其内部 Hook 的调用，React 将无法自动检查你的 Hook 是否违反了 Hook 的规则。</p>
</blockquote>
<p><strong>（1）useDidMount</strong></p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">import</span> &#123; useEffect &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'react'</span>;

<span class="hljs-keyword">const</span> useDidMount = <span class="hljs-function"><span class="hljs-params">fn</span> =></span> useEffect(<span class="hljs-function">() =></span> fn && fn(), []);

<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> useDidMount;

<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>（2）useWillUnmount</strong></p>
<p>useEffect 时已经提及过，其允许返回一个 清除副作用的 函数，当依赖项为[]时，其相当于componentWillUnMount</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">import</span> &#123; useEffect &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'react'</span>;

<span class="hljs-keyword">const</span> useWillUnmount = <span class="hljs-function"><span class="hljs-params">fn</span> =></span> useEffect(<span class="hljs-function">() =></span> <span class="hljs-function">() =></span> fn && fn(), []);

<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> useWillUnmount;

<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>（3）实现类似class组件可支持回调的setState方法</strong></p>
<p>class组件更新状态时，setState可以通过第二个参数拿到更新完毕后的回调函数。很遗憾，<strong>虽然hooks函数的useState第二个参数回调支持类似class组件的setState的第一个参数的用法（通过传入一个函数并将函数的返回值作为新的state进行更新），但不支持第二个参数回调</strong>，但是很多业务场景中我们又希望hooks组件能支持更新后的回调这一方法。</p>
<p>借助useRef和useEffect配合useState来实现这一功能:</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> useXState = <span class="hljs-function">(<span class="hljs-params">initState</span>) =></span> &#123;
    <span class="hljs-keyword">const</span> [state, setState] = useState(initState)
    <span class="hljs-comment">//表示有state值更新了</span>
    <span class="hljs-keyword">let</span> isUpdate = useRef()
    <span class="hljs-keyword">const</span> setXState = <span class="hljs-function">(<span class="hljs-params">state, cb</span>) =></span> &#123;
        <span class="hljs-comment">//这里setState是使用了函数参数的方式更新useState的值，而不是直接更新成指定的参数值</span>
        setState(<span class="hljs-function"><span class="hljs-params">prev</span> =></span> &#123;
            isUpdate.current = cb
            <span class="hljs-keyword">return</span> <span class="hljs-keyword">typeof</span> state === <span class="hljs-string">'function'</span> ? state(prev) : state
        &#125;)
    &#125;
    useEffect(<span class="hljs-function">() =></span> &#123;
        <span class="hljs-keyword">if</span>(isUpdate.current) &#123;
        <span class="hljs-comment">//存在更新state，则执行回调</span>
            isUpdate.current()
        &#125;
    &#125;)

    <span class="hljs-keyword">return</span> [state, setXState]
&#125;

<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> useXState
<span class="copy-code-btn">复制代码</span></code></pre>
<p>说明：</p>
<p>利用useRef的特性来作为标识区分是挂载还是更新，当执行setXstate时，会传入和setState一模一样的参数，并且将回调赋值给useRef的current属性，这样在更新完成时，我们手动调用current即可实现更新后的回调这一功能</p>
<h2 data-id="heading-14">11. Hooks vs Render Props vs HOC</h2>
<p>没有 Hooks 之前，高阶组件和 Render Props 本质上都是将复用逻辑提升到父组件中。而 Hooks 出现之后，我们将复用逻辑提取到组件顶层，而不是强行提升到父组件中。这样就能够避免 HOC 和 Render Props 带来的「嵌套地狱」。但是，像 Context 的  和  这样有父子层级关系（树状结构关系）的，还是只能使用 Render Props 或者 HOC。</p>
<p>对于 Hooks、Render Props 和高阶组件来说，它们都有各自的使用场景：</p>
<p>Hooks：</p>
<blockquote>
<p>替代 Class 的大部分用例，除了 getSnapshotBeforeUpdate 和 componentDidCatch 还不支持。
可提取复用逻辑。除了有明确父子关系的，其他场景都可以使用 Hooks。</p>
</blockquote>
<p>Render Props：</p>
<blockquote>
<p>在组件渲染上拥有更高的自由度，可以根据父组件提供的数据进行动态渲染。适合有明确父子关系的场景。</p>
</blockquote>
<p>高阶组件：</p>
<blockquote>
<p>适合用来做注入，并且生成一个新的可复用组件。适合用来写插件。</p>
</blockquote>
<p>不过，能使用 Hooks 的场景还是应该优先使用 Hooks，其次才是 Render Props 和 HOC。当然，Hooks、Render Props 和 HOC 不是对立的关系。我们既可以用 Hook 来写 Render Props 和 HOC，也可以在 HOC 中使用 Render Props 和 Hooks。</p></div>  
</div>
            