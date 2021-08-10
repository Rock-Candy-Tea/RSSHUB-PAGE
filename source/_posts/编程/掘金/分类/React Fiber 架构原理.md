
---
title: 'React Fiber 架构原理'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/819a921770044f188c1a29b4f2c53966~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Sun, 08 Aug 2021 00:30:15 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/819a921770044f188c1a29b4f2c53966~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h1 data-id="heading-0">Fiber 原理</h1>
<h2 data-id="heading-1">在 Fiber 出现之前 React 存在什么问题</h2>
<p>在 React 16 之前的版本对比更新 VirtualDOM 的过程是采用 Stack 架构实现的，也就是循环加递归。这种对比方式有一个问题，就是一旦任务开始进行就无法中断，如果应用中的组件数量庞大，Virtual DOM 的层级比较深，主线程被长期占用，直到整棵 VirtualDOM 树比对更新完成之后主线程才能被释放，主线程才能执行其他任务。这就会导致一些用户交互，动画等任务无法立即得到执行，页面就会产生卡顿, 非常的影响用户体验。
核心问题：递归无法中断，执行任务耗时长，JavaScript 是单线程的，和 Native GUI 互斥，比较 VirtualDOM 的过程中无法执行其他任务，导致任务延迟页面卡顿，用户体验差。</p>
<h2 data-id="heading-2">Stack 架构的简单实现</h2>
<p>我们来实现一个简单的获取 jsx，然后将 jsx 转换成 DOM ，然后添加到页面中的过程</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> jsx = (
  <span class="xml"><span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">id</span>=<span class="hljs-string">"a1"</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">id</span>=<span class="hljs-string">"b1"</span>></span>
      <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">id</span>=<span class="hljs-string">"c1"</span>></span><span class="hljs-tag"></<span class="hljs-name">div</span>></span>
      <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">id</span>=<span class="hljs-string">"c2"</span>></span><span class="hljs-tag"></<span class="hljs-name">div</span>></span>
    <span class="hljs-tag"></<span class="hljs-name">div</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">id</span>=<span class="hljs-string">"b2"</span>></span><span class="hljs-tag"></<span class="hljs-name">div</span>></span>
  <span class="hljs-tag"></<span class="hljs-name">div</span>></span></span>
)

<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">render</span>(<span class="hljs-params">vdom, container</span>) </span>&#123;
  <span class="hljs-comment">// 创建元素</span>
  <span class="hljs-keyword">const</span> element = <span class="hljs-built_in">document</span>.createElement(vdom.type)
  <span class="hljs-comment">// 为元素添加属性</span>
  <span class="hljs-built_in">Object</span>.keys(vdom.props)
    .filter(<span class="hljs-function"><span class="hljs-params">propName</span> =></span> propName !== <span class="hljs-string">"children"</span>) <span class="hljs-comment">// 过滤 children 属性</span>
    .forEach(<span class="hljs-function"><span class="hljs-params">propName</span> =></span> (element[propName] = vdom.props[propName]))
  <span class="hljs-comment">// 递归创建子元素</span>
  <span class="hljs-keyword">if</span> (<span class="hljs-built_in">Array</span>.isArray(vdom.props.children)) &#123;
    vdom.props.children.forEach(<span class="hljs-function"><span class="hljs-params">child</span> =></span> render(child, element))
  &#125;
  <span class="hljs-comment">// 将元素添加到页面中</span>
  container.appendChild(element)
&#125;

render(jsx, <span class="hljs-built_in">document</span>.getElementById(<span class="hljs-string">"root"</span>))
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/819a921770044f188c1a29b4f2c53966~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>可以看到，jsx 代码被转换成了真实的 DOM 添加到了页面中</p>
<h2 data-id="heading-3">Fiber 如何解决性能问题的思路</h2>
<ol>
<li>在 Fiber 架构中 React 放弃了递归调用，采用循环来模拟递归，因为循环可以随时被中断。</li>
<li>Fiber 将大的渲染任务拆分成一个个小任务</li>
<li>React 使用 requestIdleCallback 去利用浏览器的空闲时间去执行小任务，React 在执行一个任务单元后，查看是否有其他高优先级的任务，如果有，放弃占用线程，先执行优先级高的任务。</li>
</ol>
<h2 data-id="heading-4">requestIdleCallback</h2>
<p>我们先来看看 requestIdleCallback 在 <a href="https://link.juejin.cn/?target=https%3A%2F%2Fdeveloper.mozilla.org%2Fzh-CN%2Fdocs%2FWeb%2FAPI%2FWindow%2FrequestIdleCallback" target="_blank" rel="nofollow noopener noreferrer" title="https://developer.mozilla.org/zh-CN/docs/Web/API/Window/requestIdleCallback" ref="nofollow noopener noreferrer">MDN</a> 上的解释</p>
<blockquote>
<p>window.requestIdleCallback()方法将在浏览器的空闲时段内调用的函数排队。这使开发者能够在主事件循环上执行后台和低优先级工作，而不会影响延迟关键事件，如动画和输入响应。函数一般会按先进先调用的顺序执行，然而，如果回调函数指定了执行超时时间timeout，则有可能为了在超时前执行函数而打乱执行顺序。</p>
</blockquote>
<h3 data-id="heading-5">requestIdleCallback 的语法</h3>
<p>requestIdleCallback 接收两个参数，一个名为 IdleDeadline 的回调函数，一个是可选参数</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/deab1f93b03b419282de9f58ddabc8c1~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>IdleDeadline 参数上有一个 timeRemaining() 的方法，返回一个时间 <a href="https://link.juejin.cn/?target=https%3A%2F%2Fdeveloper.mozilla.org%2Fzh-CN%2Fdocs%2FWeb%2FAPI%2FDOMHighResTimeStamp" target="_blank" rel="nofollow noopener noreferrer" title="https://developer.mozilla.org/zh-CN/docs/Web/API/DOMHighResTimeStamp" ref="nofollow noopener noreferrer">DOMHighResTimeStamp</a>, 并且是浮点类型的数值，它用来表示当前闲置周期的预估剩余毫秒数。如果idle period已经结束，则它的值是0。你的回调函数(传给requestIdleCallback的函数)可以重复的访问这个属性用来判断当前线程的闲置时间是否可以在结束前执行更多的任务。</p>
<h3 data-id="heading-6">requestIdleCallback 的作用</h3>
<p>浏览器的页面都是通过引擎一帧一帧绘制出来的，当每秒绘制的帧数达到 60 的时候，页面就是流畅的，玩过 fps 游戏的都知道，当这个帧数小于 60 的时候，人的肉眼就能感知出来卡顿。一秒 60 帧，每一帧分到的时间就是 1000/60 ≈ 16 ms，如果每一帧执行的时间小于 16 ms，就说明浏览器有空余时间，那么能不能通过浏览器的空余时间去处理任务呢，这样就不用一直等待主任务执行完了，requestIdleCallback 就是利用浏览器的空余时间去执行任务的。</p>
<p>上面说了一堆，有的人可能已经懵了，你别废话，直接上代码给我一个示例就行了。诶，那我们就用下面的例子看看 requestIdleCallback 到底有什么神奇之处</p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">style</span>></span><span class="css">
  <span class="hljs-selector-id">#box</span> &#123;
    <span class="hljs-attribute">padding</span>: <span class="hljs-number">20px</span>;
    <span class="hljs-attribute">background</span>: palegoldenrod;
  &#125;
</span><span class="hljs-tag"></<span class="hljs-name">style</span>></span>

<span class="hljs-comment"><!-- body --></span>
<span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">id</span>=<span class="hljs-string">"box"</span>></span><span class="hljs-tag"></<span class="hljs-name">div</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">button</span> <span class="hljs-attr">id</span>=<span class="hljs-string">"btn1"</span>></span>执行计算任务<span class="hljs-tag"></<span class="hljs-name">button</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">button</span> <span class="hljs-attr">id</span>=<span class="hljs-string">"btn2"</span>></span>更改背景颜色<span class="hljs-tag"></<span class="hljs-name">button</span>></span>
<span class="hljs-tag"><<span class="hljs-name">script</span>></span><span class="javascript">
  <span class="hljs-keyword">const</span> box = <span class="hljs-built_in">document</span>.getElementById(<span class="hljs-string">'box'</span>)
  <span class="hljs-keyword">const</span> btn1 = <span class="hljs-built_in">document</span>.getElementById(<span class="hljs-string">'btn1'</span>)
  <span class="hljs-keyword">const</span> btn2 = <span class="hljs-built_in">document</span>.getElementById(<span class="hljs-string">'btn2'</span>)

  <span class="hljs-keyword">let</span> number = <span class="hljs-number">999999</span>
  <span class="hljs-keyword">let</span> value = <span class="hljs-number">0</span>

  <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">calc</span>(<span class="hljs-params"></span>) </span>&#123;
    <span class="hljs-keyword">while</span> (number > <span class="hljs-number">0</span>) &#123;
      value = <span class="hljs-built_in">Math</span>.random() < <span class="hljs-number">0.5</span> ? <span class="hljs-built_in">Math</span>.random() : <span class="hljs-built_in">Math</span>.random()
      <span class="hljs-built_in">console</span>.log(value)
      number--
    &#125;
  &#125;

  btn1.onclick = <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params"></span>) </span>&#123;
    calc()
  &#125;

  btn2.onclick = <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params"></span>) </span>&#123;
    box.style.background = <span class="hljs-string">'green'</span>
  &#125;
</span><span class="hljs-tag"></<span class="hljs-name">script</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>上面的代码，我们通过一个很长的循环创建随机数，增加浏览器的计算量，你可以通过本地的 ide 试试这个 demo，就会发现当你点击 执行计算任务 后，再点击 更改背景颜色 按钮后，box 的颜色不会立马改变，而是会等待几秒后才发生改变（如果电脑性能差，可能会更慢）。这时因为 native GUI 和 v8引擎的渲染是互斥的，所以页面渲染会有一些延迟。</p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">style</span>></span><span class="css">
  <span class="hljs-selector-id">#box</span> &#123;
    <span class="hljs-attribute">padding</span>: <span class="hljs-number">20px</span>;
    <span class="hljs-attribute">background</span>: palegoldenrod;
  &#125;
</span><span class="hljs-tag"></<span class="hljs-name">style</span>></span>
<span class="hljs-comment"><!-- body --></span>
<span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">id</span>=<span class="hljs-string">"box"</span>></span><span class="hljs-tag"></<span class="hljs-name">div</span>></span>
<span class="hljs-tag"><<span class="hljs-name">button</span> <span class="hljs-attr">id</span>=<span class="hljs-string">"btn1"</span>></span>执行计算任务<span class="hljs-tag"></<span class="hljs-name">button</span>></span>
<span class="hljs-tag"><<span class="hljs-name">button</span> <span class="hljs-attr">id</span>=<span class="hljs-string">"btn2"</span>></span>更改背景颜色<span class="hljs-tag"></<span class="hljs-name">button</span>></span>
<span class="hljs-tag"><<span class="hljs-name">script</span>></span><span class="javascript">
  <span class="hljs-keyword">const</span> box = <span class="hljs-built_in">document</span>.getElementById(<span class="hljs-string">'box'</span>)
  <span class="hljs-keyword">const</span> btn1 = <span class="hljs-built_in">document</span>.getElementById(<span class="hljs-string">'btn1'</span>)
  <span class="hljs-keyword">const</span> btn2 = <span class="hljs-built_in">document</span>.getElementById(<span class="hljs-string">'btn2'</span>)

  <span class="hljs-keyword">let</span> number = <span class="hljs-number">999999</span>
  <span class="hljs-keyword">let</span> value = <span class="hljs-number">0</span>

  <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">calc</span>(<span class="hljs-params">deadline</span>) </span>&#123;
    <span class="hljs-keyword">while</span> (number > <span class="hljs-number">0</span> && deadline.timeRemaining() > <span class="hljs-number">0</span>) &#123;
      value = <span class="hljs-built_in">Math</span>.random() < <span class="hljs-number">0.5</span> ? <span class="hljs-built_in">Math</span>.random() : <span class="hljs-built_in">Math</span>.random()
      <span class="hljs-built_in">console</span>.log(value)
      number--
    &#125;
    requestIdleCallback(calc)
  &#125;

  btn1.onclick = <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params"></span>) </span>&#123;
    requestIdleCallback(calc)
  &#125;

  btn2.onclick = <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params"></span>) </span>&#123;
    box.style.background = <span class="hljs-string">'green'</span>
  &#125;
</span><span class="hljs-tag"></<span class="hljs-name">script</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>上面的代码是使用了 requestIdleCallback 去优化的，运行之后，在点击 更改背景颜色 的按钮后，立马就能看到颜色的变化，这就是 requestIdleCallback 的作用。</p>
<h2 data-id="heading-7">Fiber 原理分析</h2>
<p>下面我们通过实现一个简易版本的 Fiber 来了解一下 Fiber 的原理</p>
<h3 data-id="heading-8">什么是 Fiber</h3>
<p>我们闲扯了这么多，那么 Fiber 到底是什么呢？
Fiber 是 React 的一个执行单元，在 React 16 之后，React 将整个渲染任务拆分成了一个个的小任务进行处理，每一个小任务指的就是 Fiber 节点的构建。
拆分的小任务会在浏览器的空闲时间被执行，每个任务单元执行完成后，React 都会检查是否还有空余时间，如果有就交换主线程的控制权。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/212287f875e7489fbd33808cca298aea~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>Fiber 是一种数据结构，支撑 Fiber 构建任务的运转。当某一个 Fiber 任务执行完成后，怎样去找下一个要执行的 Fiber 任务呢？React 通过链表结构找到下一个要执行的任务单元。
Fiber 其实就是 JavaScript 对象，在这个对象中有 child 属性表示节点的子节点，有 sibling 属性表示节点的下一个兄弟节点，有 return 属性表示节点的父级节点。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// 简易版 Fiber 对象</span>
type Fiber = &#123;
  <span class="hljs-comment">// 组件类型 div、span、组件构造函数</span>
  <span class="hljs-attr">type</span>: any,
  <span class="hljs-comment">// DOM 对象</span>
  <span class="hljs-attr">stateNode</span>: any,  
  <span class="hljs-comment">// 指向自己的父级 Fiber 对象</span>
  <span class="hljs-attr">return</span>: Fiber | <span class="hljs-literal">null</span>,
  <span class="hljs-comment">// 指向自己的第一个子级 Fiber 对象</span>
  <span class="hljs-attr">child</span>: Fiber | <span class="hljs-literal">null</span>,
  <span class="hljs-comment">// 指向自己的下一个兄弟 iber 对象</span>
  <span class="hljs-attr">sibling</span>: Fiber | <span class="hljs-literal">null</span>,
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-9">实现一个简易版 Fiber</h3>
<p>Fiber 的工作分为两个阶段：render 阶段和 commit 阶段。</p>
<ul>
<li>render 阶段：构建 Fiber 对象，构建链表，在链表中标记要执行的 DOM 操作 ，可中断。</li>
<li>commit 阶段：根据构建好的链表进行 DOM 操作，不可中断。</li>
</ul>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> jsx = (
  <span class="xml"><span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">id</span>=<span class="hljs-string">"a1"</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">id</span>=<span class="hljs-string">"b1"</span>></span>
      <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">id</span>=<span class="hljs-string">"c1"</span>></span><span class="hljs-tag"></<span class="hljs-name">div</span>></span>
      <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">id</span>=<span class="hljs-string">"c2"</span>></span><span class="hljs-tag"></<span class="hljs-name">div</span>></span>
    <span class="hljs-tag"></<span class="hljs-name">div</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">id</span>=<span class="hljs-string">"b2"</span>></span><span class="hljs-tag"></<span class="hljs-name">div</span>></span>
  <span class="hljs-tag"></<span class="hljs-name">div</span>></span></span>
)

<span class="hljs-keyword">const</span> container = <span class="hljs-built_in">document</span>.getElementById(<span class="hljs-string">"root"</span>)

<span class="hljs-comment">// 构建根元素的 Fiber 对象</span>
<span class="hljs-keyword">const</span> workInProgressRoot = &#123;
  <span class="hljs-attr">stateNode</span>: container,
  <span class="hljs-attr">props</span>: &#123;
    <span class="hljs-attr">children</span>: [jsx]
  &#125;
&#125;

<span class="hljs-comment">// 下一个要执行的任务</span>
<span class="hljs-keyword">let</span> nextUnitOfWork = workInProgressRoot

<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">workLoop</span>(<span class="hljs-params">deadline</span>) </span>&#123;
  <span class="hljs-comment">// 1. 是否有空余时间</span>
  <span class="hljs-comment">// 2. 是否有要执行的任务</span>
  <span class="hljs-keyword">while</span> (nextUnitOfWork && deadline.timeRemaining() > <span class="hljs-number">0</span>) &#123;
    nextUnitOfWork = performUnitOfWork(nextUnitOfWork)
  &#125;
  <span class="hljs-comment">// 表示所有的任务都已经执行完成了</span>
  <span class="hljs-keyword">if</span> (!nextUnitOfWork) &#123;
    <span class="hljs-comment">// 进入到第二阶段 执行DOM</span>
    commitRoot()
  &#125;
&#125;

<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">performUnitOfWork</span>(<span class="hljs-params">workInProgressFiber</span>) </span>&#123;
  <span class="hljs-comment">// 1. 创建 DOM 对象并将它存储在 stateNode 属性</span>
  <span class="hljs-comment">// 2. 构建当前 Fiber 的子级 Fiber</span>
  <span class="hljs-comment">// 向下走的过程</span>
  beginWork(workInProgressFiber)
  <span class="hljs-comment">// 如果当前Fiber有子级</span>
  <span class="hljs-keyword">if</span> (workInProgressFiber.child) &#123;
    <span class="hljs-comment">// 返回子级 构建子级的子级</span>
    <span class="hljs-keyword">return</span> workInProgressFiber.child
  &#125;

  <span class="hljs-keyword">while</span> (workInProgressFiber) &#123;
    <span class="hljs-comment">// 向上走，构建链表</span>
    completeUnitOfWork(workInProgressFiber)

    <span class="hljs-comment">// 如果有同级</span>
    <span class="hljs-keyword">if</span> (workInProgressFiber.sibling) &#123;
      <span class="hljs-comment">// 返回同级 构建同级的子级</span>
      <span class="hljs-keyword">return</span> workInProgressFiber.sibling
    &#125;
    <span class="hljs-comment">// 更新父级</span>
    workInProgressFiber = workInProgressFiber.return
  &#125;
&#125;

<span class="hljs-comment">// 构建子集</span>
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">beginWork</span>(<span class="hljs-params">workInProgressFiber</span>) </span>&#123;
  <span class="hljs-comment">// 1. 创建 DOM 对象并将它存储在 stateNode 属性</span>
  <span class="hljs-keyword">if</span> (!workInProgressFiber.stateNode) &#123;
    <span class="hljs-comment">// 创建 DOM</span>
    workInProgressFiber.stateNode = <span class="hljs-built_in">document</span>.createElement(
      workInProgressFiber.type
    )
    <span class="hljs-comment">// 为 DOM 添加属性</span>
    <span class="hljs-keyword">for</span> (<span class="hljs-keyword">let</span> attr <span class="hljs-keyword">in</span> workInProgressFiber.props) &#123;
      <span class="hljs-keyword">if</span> (attr !== <span class="hljs-string">"children"</span>) &#123;
        workInProgressFiber.stateNode[attr] = workInProgressFiber.props[attr]
      &#125;
    &#125;
  &#125;
  <span class="hljs-comment">// 2. 构建当前 Fiber 的子级 Fiber</span>
  <span class="hljs-keyword">if</span> (<span class="hljs-built_in">Array</span>.isArray(workInProgressFiber.props.children)) &#123;
    <span class="hljs-keyword">let</span> previousFiber = <span class="hljs-literal">null</span>
    workInProgressFiber.props.children.forEach(<span class="hljs-function">(<span class="hljs-params">child, index</span>) =></span> &#123;
      <span class="hljs-keyword">let</span> childFiber = &#123;
        <span class="hljs-attr">type</span>: child.type,
        <span class="hljs-attr">props</span>: child.props,
        <span class="hljs-attr">effectTag</span>: <span class="hljs-string">"PLACEMENT"</span>,
        <span class="hljs-attr">return</span>: workInProgressFiber
      &#125;
      <span class="hljs-keyword">if</span> (index === <span class="hljs-number">0</span>) &#123;
        <span class="hljs-comment">// 构建子集，只有第一个子元素是子集</span>
        workInProgressFiber.child = childFiber
      &#125; <span class="hljs-keyword">else</span> &#123;
        <span class="hljs-comment">// 不是第一个，则构建子集的 兄弟级</span>
        previousFiber.sibling = childFiber
      &#125;
      previousFiber = childFiber
    &#125;)
  &#125;
  <span class="hljs-comment">// console.log(workInProgressFiber)</span>
&#125;

<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">completeUnitOfWork</span>(<span class="hljs-params">workInProgressFiber</span>) </span>&#123;
  <span class="hljs-comment">// 获取当前 Fiber 的父级</span>
  <span class="hljs-keyword">const</span> returnFiber = workInProgressFiber.return
  <span class="hljs-comment">// 父级是否存在</span>
  <span class="hljs-keyword">if</span> (returnFiber) &#123;
    <span class="hljs-comment">// 需要执行 DOM 操作的 Fiber</span>
    <span class="hljs-keyword">if</span> (workInProgressFiber.effectTag) &#123;
      <span class="hljs-keyword">if</span> (!returnFiber.lastEffect) &#123;
        returnFiber.lastEffect = workInProgressFiber.lastEffect
      &#125;

      <span class="hljs-keyword">if</span> (!returnFiber.firstEffect) &#123;
        returnFiber.firstEffect = workInProgressFiber.firstEffect
      &#125;

      <span class="hljs-keyword">if</span> (returnFiber.lastEffect) &#123;
        returnFiber.lastEffect.nextEffect = workInProgressFiber
      &#125; <span class="hljs-keyword">else</span> &#123;
        returnFiber.firstEffect = workInProgressFiber
      &#125;
      returnFiber.lastEffect = workInProgressFiber
    &#125;
  &#125;
&#125;

<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">commitRoot</span>(<span class="hljs-params"></span>) </span>&#123;
  <span class="hljs-keyword">let</span> currentFiber = workInProgressRoot.firstEffect
  <span class="hljs-keyword">while</span> (currentFiber) &#123;
    currentFiber.return.stateNode.appendChild(currentFiber.stateNode)
    currentFiber = currentFiber.nextEffect
  &#125;
&#125;

<span class="hljs-comment">// 在浏览器空闲的时候执行任务</span>
requestIdleCallback(workLoop)
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-10">构建 Fiber 链表</h3>
<p>上面的 completeUnitOfWork 函数就是用来构建 Fiber 链表的，只在在链表中的才会渲染</p>
<ol>
<li>链表的构建顺序是怎么样的 ？</li>
</ol>
<p>链表的顺序是由 DOM 操作的顺序决定的，c1 是第一个要执行 DOM 操作的所以它是链的开始，A1 是最后一个被添加到 Root 中的元素，所以它是链的最后。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/3ebeb5a18e4c4c6382e63285ee56aad3~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<ol start="2">
<li>如何向链的尾部添加新元素？</li>
</ol>
<p>在链表结构中通过 nextEffect 存储链中的下一项。</p>
<p>在构建链表的过程中，需要通过一个变量存储链表中的最新项，每次添加新项时都使用这个变量，每次操作完成后都需要更新它。这个变量在源码中叫做 lastEffect。</p>
<p>lastEffect 是存储在当前 Fiber 对象的父级上的，当父级发生变化时，为避免链接顺序发生错乱，lastEffect 要先上移然后再追加nextEffect</p>
<ol start="3">
<li>将链表保存在什么位置？</li>
</ol>
<p>链表需要被保存在 Root 中，因为在进入到第二阶段时，也就是 commitRoot 方法中，是将 Root 提交到第二阶段的。
在源码中，Root Fiber 下有一个叫 firstEffect 的属性，用于存储链表。
在构建链表的遍历过程中，C1 开始，Root 是结尾，如何才能将 C1 存储到 Root 中呢？
其实是链头的不断上移做到的。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/d84688affe0f40cb8fa886a72a2622eb~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-11">总结</h2>
<p>其实 Fiber 的总体思路就是利用循环和链表代替递归去优化性能，Fiber 架构有两个阶段，render 阶段就是负责构架 Fiber 对象和链表，而 commit 阶段就是负责去构建 DOM，上面简单的实现了 Fiber ，只是为了理解方便
下面是实现 Fiber 的完整版
<a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fmaoxiaoxing%2Freact-study%2Ftree%2Fmaster%2FFiber" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/maoxiaoxing/react-study/tree/master/Fiber" ref="nofollow noopener noreferrer">github.com/maoxiaoxing…</a></p></div>  
</div>
            