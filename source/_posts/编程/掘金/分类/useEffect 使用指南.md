
---
title: 'useEffect 使用指南'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/6dcb5ea27a64437b824a714378a8de45~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Wed, 30 Jun 2021 18:55:54 GMT
thumbnail: 'https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/6dcb5ea27a64437b824a714378a8de45~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>本文已参与好文召集令活动，点击查看：<a href="https://juejin.cn/post/6978685539985653767" target="_blank">后端、大前端双赛道投稿，2万元奖池等你挑战！</a></p>
<h2 data-id="heading-0">引言</h2>
<p>Hooks 是 React 16.8 的新增特性，至今经历两年的时间，它可以让你在不编写 Class 组件的情况下使用 state 以及其他 React 特性。 <code>useEffect</code> 是基础 Hooks 之一，我在项目中使用较为频繁，但总有些疑惑 ，比如：</p>
<ul>
<li>如何正确使用 <code>useEffect</code> ？</li>
<li><code>useEffect</code> 的执行时机 ？</li>
<li><code>useEffect</code> 和生命周期的区别 ？</li>
</ul>
<p>本文主要从以上几个方面分析 <code>useEffect</code> ，以及与另外一个看起来和 <code>useEffect</code> 很像的 Hook <code>useLayoutEffect</code> 的使用和它们之间的区别。</p>
<h2 data-id="heading-1">useEffect 简介</h2>
<p>首先介绍两个概念，纯函数和副作用函数。</p>
<ul>
<li>纯函数（ Pure Function ）：对于相同的输入，永远会得到相同的输出，而且没有任何可观察的副作用，这样的函数被称为纯函数。</li>
<li>副作用函数（ Side effect Function ）：如果一个函数在运行的过程中，除了返回函数值，还对主调用函数产生附加的影响，这样的函数被称为副作用函数。</li>
</ul>
<p><code>useEffect</code> 就是在 React 更新 DOM 之后运行一些额外的代码，也就是执行副作用操作，比如请求数据，设置订阅以及手动更改 React 组件中的 DOM 等。</p>
<h2 data-id="heading-2">正确使用 useEffect</h2>
<p>基本使用方法：<code>useEffect(effect) </code></p>
<p>根据传参个数和传参类型，<code>useEffect(effect)</code> 的执行次数和执行结果是不同的，下面一一介绍。</p>
<ul>
<li>默认情况下，<code>effect</code> 会在每次渲染之后执行。示例如下：</li>
</ul>
<pre><code class="hljs language-js copyable" lang="js">useEffect(<span class="hljs-function">() =></span> &#123;
  <span class="hljs-keyword">const</span> subscription = props.source.subscribe();
  <span class="hljs-keyword">return</span> <span class="hljs-function">() =></span> &#123;
    <span class="hljs-comment">// 清除订阅</span>
    subscription.unsubscribe();
  &#125;;
&#125;);
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>也可以通过设置第二个参数，依赖项组成的数组 <code> useEffect(effect,[])</code> ，让它在数组中的值发生变化的时候执行，数组中可以设置多个依赖项，其中的任意一项发生变化，<code>effect</code> 都会重新执行。示例如下：</li>
</ul>
<pre><code class="hljs language-js copyable" lang="js">useEffect(
  <span class="hljs-function">() =></span> &#123;
    <span class="hljs-keyword">const</span> subscription = props.source.subscribe();
    <span class="hljs-keyword">return</span> <span class="hljs-function">() =></span> &#123;
      subscription.unsubscribe();
    &#125;;
  &#125;,
  [props.source],
);
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>需要注意的是</strong>：当依赖项是引用类型时，React 会对比当前渲染下的依赖项和上次渲染下的依赖项的内存地址是否一致，如果一致，<code>effect</code> 不会执行，只有当对比结果不一致时，<code>effect</code> 才会执行。<a href="https://codesandbox.io/s/gracious-dew-yr3gb?file=/src/App.js" target="_blank" rel="nofollow noopener noreferrer">示例如下 (点击在线测试)</a>：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">Child</span>(<span class="hljs-params">props</span>) </span>&#123;
  
  useEffect(<span class="hljs-function">() =></span> &#123;
    <span class="hljs-built_in">console</span>.log(<span class="hljs-string">"useEffect"</span>);
  &#125;, [props.data]);
  
  <span class="hljs-keyword">return</span> <span class="xml"><span class="hljs-tag"><<span class="hljs-name">div</span>></span>&#123;props.data.x&#125;<span class="hljs-tag"></<span class="hljs-name">div</span>></span></span>;
&#125;

<span class="hljs-keyword">let</span> b = &#123; <span class="hljs-attr">x</span>: <span class="hljs-number">1</span> &#125;;

<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">Parent</span>(<span class="hljs-params"></span>) </span>&#123;
  <span class="hljs-keyword">const</span> [count, setCount] = useState(<span class="hljs-number">0</span>);
  <span class="hljs-built_in">console</span>.log(<span class="hljs-string">"render"</span>);
  <span class="hljs-keyword">return</span> (
    <span class="xml"><span class="hljs-tag"><<span class="hljs-name">div</span>></span>
      <span class="hljs-tag"><<span class="hljs-name">button</span>
        <span class="hljs-attr">onClick</span>=<span class="hljs-string">&#123;()</span> =></span> &#123;
          b.x = b.x + 1;
          setCount(count + 1);
        &#125;&#125;
      >
        Click me
      <span class="hljs-tag"></<span class="hljs-name">button</span>></span>
      <span class="hljs-tag"><<span class="hljs-name">Child</span> <span class="hljs-attr">data</span>=<span class="hljs-string">&#123;b&#125;</span> /></span>
    <span class="hljs-tag"></<span class="hljs-name">div</span>></span></span>
  );
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>结果如下：</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/6dcb5ea27a64437b824a714378a8de45~tplv-k3u1fbpfcp-watermark.image" alt="useEffect1.gif" loading="lazy" referrerpolicy="no-referrer"></p>
<p>上面实例中，组件 <code><Child/></code> 中的 <code>useEffect</code> 函数中的依赖项是一个对象，当点击按钮对象中的值发生变化，但是传入 <code><Child/> </code> 组件的内存地址没有变化，所以 <code>console.log("useEffect") </code>不会执行，useEffect 不会被打印。为了解决这个问题，我们可以使用对象中的属性作为依赖，而不是整个对象。把上面示例中组件 <code><Child/></code> 修改如下：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">Child</span>(<span class="hljs-params">props</span>) </span>&#123;
  
  useEffect(<span class="hljs-function">() =></span> &#123;
    <span class="hljs-built_in">console</span>.log(<span class="hljs-string">"useEffect"</span>);
  &#125;, [props.data.x]);
  
  <span class="hljs-keyword">return</span> <span class="xml"><span class="hljs-tag"><<span class="hljs-name">div</span>></span>&#123;props.data.x&#125;<span class="hljs-tag"></<span class="hljs-name">div</span>></span></span>;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>修改后结果如下：</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/b1b985512b644cc098de1ff032217de4~tplv-k3u1fbpfcp-watermark.image" alt="useEffect2.gif" loading="lazy" referrerpolicy="no-referrer"></p>
<p>可见 <code>useEffect</code> 函数中的 <code>console.log("useEffect")</code> 被执行，打印出 useEffect。</p>
<ul>
<li>当依赖项是一个空数组 [] 时 , <code>effect</code> 只在第一次渲染的时候执行。</li>
</ul>
<h2 data-id="heading-3">useEffect 的执行时机</h2>
<p>默认情况下，<code>effect</code> 在第一次渲染之后和每次更新之后都会执行，也可以是只有某些值发生变化之后执行，重点在于是<strong>每轮渲染结束后延迟调用（ 异步执行 ）</strong>，这是 <code>useEffect</code> 的好处，保证执行 <code>effect </code>的时候，DOM 都已经更新完毕，不会阻碍 DOM 渲染，造成视觉阻塞。</p>
<h2 data-id="heading-4">useEffect 和 useLayoutEffect 的区别</h2>
<p><code>useLayoutEffect</code> 的使用方法和 <code>useEffect</code> 相同，区别是他们的执行时机。</p>
<p>如上面所说，<code>effect</code> 的内容是会在渲染 DOM 之后执行，然而并非所有的操作都能被放在 <code>effect</code> 都延迟执行的，例如，在浏览器执行下一次绘制前，需要操作 DOM 改变页面样式，如果放在 <code>useEffect</code> 中执行，会出现闪屏问题。而 <code>useLayoutEffect</code> 是在<strong>浏览器执行绘制之前被同步执行</strong>，放在 <code>useLayoutEffect</code> 中就会避免这个问题。</p>
<p>这篇文章中可以清楚的看到上述例子的具体实现：<a href="https://www.jianshu.com/p/412c874c5add" target="_blank" rel="nofollow noopener noreferrer">useEffect 和 useLayoutEffect 的区别</a></p>
<h2 data-id="heading-5">对比 useEffect 和生命周期</h2>
<p>如果你熟悉生命周期函数，你可能会用生命周期的思路去类比思考 <code>useEffect</code> 的执行过程，但其实并不建议这么做，因为 <code>useEffect</code> 的心智模型和 <code>componentDidMount</code> 等其他生命周期是不同的。</p>
<p>Function 组件中不存在生命周期，React 会根据我们当前的 props 和 state 同步 DOM ，每次渲染都会被固化，包括 state、props、side effects 以及写在 Function 组件中的所有函数。</p>
<p>另外，大多数 <code>useEffect</code> 函数不需要同步执行，不会像 <code>componentDidMount</code> 或 <code>componentDidUpdate</code> 那样阻塞浏览器更新屏幕。</p>
<p>所以 <code>useEffect</code> 可以被看作是每一次渲染之后的一个独立的函数 ，可以接收 props 和 state ，并且接收的 props 和 state 是当次 render 的数据，是独立的 。相对于生命周期 <code>componentDidMount</code> 中的 this.state 始终指向最新数据， <code>useEffect</code> 中不一定是最新的数据，更像是渲染结果的一部分 —— 每个 <code>useEffect</code> 属于一次特定的渲染。对比示例如下：</p>
<ul>
<li>在 Function 组件中使用  <code>useEffect</code> ，<a href="https://codesandbox.io/s/fervent-kowalevski-f54ok?file=/src/App.js" target="_blank" rel="nofollow noopener noreferrer">代码示例 (点击在线测试)</a>：</li>
</ul>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">Counter</span>(<span class="hljs-params"></span>) </span>&#123;
  <span class="hljs-keyword">const</span> [count, setCount] = useState(<span class="hljs-number">0</span>);

  useEffect(<span class="hljs-function">() =></span> &#123;
    <span class="hljs-built_in">setTimeout</span>(<span class="hljs-function">() =></span> &#123;
      <span class="hljs-built_in">console</span>.log(<span class="hljs-string">`You clicked <span class="hljs-subst">$&#123;count&#125;</span> times`</span>);
    &#125;, <span class="hljs-number">3000</span>);
  &#125;);

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
<p>结果如下：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/c4de346327714bf78dfe9023aa926ccf~tplv-k3u1fbpfcp-watermark.image" alt="useEffect3.gif" loading="lazy" referrerpolicy="no-referrer"></p>
<ul>
<li>在 Class 组件中的使用生命周期，代码示例如下：</li>
</ul>
<pre><code class="hljs language-js copyable" lang="js"> <span class="hljs-function"><span class="hljs-title">componentDidUpdate</span>(<span class="hljs-params"></span>)</span> &#123;
    <span class="hljs-built_in">setTimeout</span>(<span class="hljs-function">() =></span> &#123;
      <span class="hljs-built_in">console</span>.log(<span class="hljs-string">`You clicked <span class="hljs-subst">$&#123;<span class="hljs-built_in">this</span>.state.count&#125;</span> times`</span>);
    &#125;, <span class="hljs-number">3000</span>);
  &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>结果如下：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/9ef14171481d4958961ee78e0c6c634a~tplv-k3u1fbpfcp-watermark.image" alt="useEffect4.gif" loading="lazy" referrerpolicy="no-referrer"></p>
<p>但是每次渲染之后都去执行 <code>effect</code> 并不高效。所以怎么解决呢 ？这就需要我们告诉 React 对比依赖来决定是否执行 <code>effect</code> 。</p>
<h2 data-id="heading-6">如何准确绑定依赖</h2>
<p>在 <code>effect</code> 中用到了哪些外部变量，都需要如实告诉 React ，那如果没有正确设置依赖项会怎么样呢 ？示例如下 ：</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/5d10b3ef8c5f468da2e6ed059bdee17f~tplv-k3u1fbpfcp-watermark.image" alt="useEffect5.gif" loading="lazy" referrerpolicy="no-referrer"></p>
<p>上面例子中， <code>useEffect</code> 中用到的依赖项 <code>count</code>，却没有声明在卸载依赖项数组中，<code>useEffect</code> 不会再重新运行（只打印了一次 useEffect ）， <code>effect</code> 中 <code>setInterVal</code> 拿的 <code>count</code> 始终是初始化的 0 ，它后面每一秒都会调用 <code>setCount(0 + 1)</code> ，得到的结果始终是 1 。下面有两种可以正确解决依赖的方法：</p>
<h3 data-id="heading-7">1.在依赖项数组中包含所有在 effect 中用到的值</h3>
<p>将 <code>effect</code> 中用到的外部变量 <code>count</code> 如实添加到依赖项数组中，结果如下：</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/2318ce39eb3a4050b1b7e47b2fe72a66~tplv-k3u1fbpfcp-watermark.image" alt="useEffect6.gif" loading="lazy" referrerpolicy="no-referrer"></p>
<p>可以看到依赖项数组是正确的，并且解决了上面的问题，但是也可以发现，随之带来的问题是：定时器会在每一次 <code>count</code> 改变后清除和重新设定，重复创建/销毁，这不是我们想要的结果。</p>
<h3 data-id="heading-8">2.第二种方法是修改 effect 中的代码来减少依赖项</h3>
<p>即修改 <code>effect</code> 内部的代码让 <code>useEffect</code> 使得依赖更少，需要一些移除依赖常用的技巧，如： <code>setCount</code> 还有一种函数回调模式，你不需要关心当前值是什么，只要对 “旧的值” 进行修改即可，这样就不需要通过把 <code>count</code> 写到依赖项数组这种方式来告诉 React 了，因为 React 已经知道了。</p>
<h2 data-id="heading-9">是否需要清除副作用</h2>
<p>若只是在 React 更新 DOM 之后运行一些额外的代码，比如发送网络请求，手动变更 DOM，记录日志，无需清除操作，因为执行之后就可以被忽略。</p>
<p>需要清除的是指那些执行之后还有后续的操作，比如说监听鼠标的点击事件，为防止内存泄漏清除函数将在组件卸载之前调用，可以通过 <code>useEffect</code> 的返回值销毁通过 <code>useEffect</code> 注册的监听。</p>
<p>清除函数执行时机是在新的渲染之后进行的，<a href="https://codesandbox.io/s/quizzical-paper-3frj2?file=/src/App.js" target="_blank" rel="nofollow noopener noreferrer">示例如下（点击在线测试）</a>：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> Example = <span class="hljs-function">() =></span> &#123;
  <span class="hljs-keyword">const</span> [count, setCount] = useState(<span class="hljs-number">0</span>);

  useEffect(<span class="hljs-function">() =></span> &#123;
    <span class="hljs-built_in">console</span>.log(<span class="hljs-string">"useEffect"</span>);
    <span class="hljs-keyword">return</span> <span class="hljs-function">() =></span> &#123;
      <span class="hljs-built_in">console</span>.log(<span class="hljs-string">"return"</span>);
    &#125;;
  &#125;, [count]);

  <span class="hljs-keyword">return</span> (
    <span class="xml"><span class="hljs-tag"><<span class="hljs-name">div</span>></span>
      <span class="hljs-tag"><<span class="hljs-name">p</span>></span>You Click &#123;count&#125; times <span class="hljs-tag"></<span class="hljs-name">p</span>></span>
      &#123;console.log("dom")&#125;
      <span class="hljs-tag"><<span class="hljs-name">button</span>
        <span class="hljs-attr">onClick</span>=<span class="hljs-string">&#123;()</span> =></span> &#123;
          setCount(count + 1);
        &#125;&#125;
      >
        Click me
      <span class="hljs-tag"></<span class="hljs-name">button</span>></span>
    <span class="hljs-tag"></<span class="hljs-name">div</span>></span></span>
  );
&#125;;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>结果如下：</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/528c4b0432c04f95be02b144e4b02f8a~tplv-k3u1fbpfcp-watermark.image" alt="useEffect8.gif" loading="lazy" referrerpolicy="no-referrer"></p>
<p><strong>需要注意的是</strong>：<code>useEffect</code> 的清除函数在每次重新渲染时都会执行，而不是只在卸载组件的时候执行 。</p>
<h2 data-id="heading-10">参考文档</h2>
<p>Dan 对 <code>useEffect</code> 的完全解读  ---  <a href="https://overreacted.io/a-complete-guide-to-useeffect/" target="_blank" rel="nofollow noopener noreferrer">A Complete Guide to useEffect</a></p></div>  
</div>
            