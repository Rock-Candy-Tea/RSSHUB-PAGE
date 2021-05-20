
---
title: 'React 数据管理之 Flux'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/0b5322fa35d54d88a7141005f31f87f8~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Wed, 19 May 2021 18:44:20 GMT
thumbnail: 'https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/0b5322fa35d54d88a7141005f31f87f8~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style>
<h1 data-id="heading-0">背景</h1>
<p>在 2014 年的<a href="https://www.youtube.com/watch?v=nYkdrAPrdcw&t=18s" target="_blank" rel="nofollow noopener noreferrer">Rethinking Web App Development at Facebook</a>会议上，Facebook 首次公开了 Flux 和 React。当时 Facebook 团队需要解决问题：“如何在产品的快速迭代中，保证产品的高质量？”。
<img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/0b5322fa35d54d88a7141005f31f87f8~tplv-k3u1fbpfcp-watermark.image" alt="少时间但是高质量.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>因此，Facebook 团队使用了 Flux 和 React 两套技术架构。通过 Flux 和 React，Facebook 团队提升了项目代码的可预测性，以便新来的工程师可以快速跟上节奏、完成功能开发和问题修复。
<img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/9e0b1717aa8840848c97f2314621ec27~tplv-k3u1fbpfcp-watermark.image" alt="flux-result.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h1 data-id="heading-1">MVC 问题</h1>
<p>在使用 Flux 之前，Facebook 团队使用的 MVC 架构。在 MVC 架构下，Facebook 项目的数据流转过程如下所示：
<img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/985c520a595f49b0b7372dfcfe2bf717~tplv-k3u1fbpfcp-watermark.image" alt="MVC-view和model交互.png" loading="lazy" referrerpolicy="no-referrer">
在该数据流中，View 会直接更新 Model。</p>
<p>看到这个架构图时，总感觉它不是常规的 MVC 架构，于是用 Google 查了下。在 wikipedia 中 MVC 架构是这样的：</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/9a92a2d4d92440f88e885b90e1641f22~tplv-k3u1fbpfcp-watermark.image" alt="MVC-wikipedia.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>在常规的 MVC 架构中，View 并不会直接更新 Model。那为什么 Facebook 给出的数据流如此不同呢？</p>
<h2 data-id="heading-2">为什么 View 会直接更新 Model</h2>
<p>考虑如下 React 组件，线上 Demo <a href="https://codesandbox.io/s/react-mvc-data-flow-02x4c" target="_blank" rel="nofollow noopener noreferrer">请戳这里</a>。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// list 和 total 是两个 Model 层</span>
<span class="hljs-comment">// 当数据发生更改时，通过 forceUpdate 通知组件进行更新</span>
<span class="hljs-keyword">let</span> list = []
<span class="hljs-keyword">let</span> total = <span class="hljs-number">0</span>

<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">useForceUpdate</span>(<span class="hljs-params"></span>) </span>&#123;
  <span class="hljs-keyword">const</span> setV = useState(&#123;&#125;)[<span class="hljs-number">1</span>]
  <span class="hljs-keyword">return</span> <span class="hljs-function">() =></span> setV(&#123;&#125;)
&#125;

<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">App</span>(<span class="hljs-params"></span>) </span>&#123;
  <span class="hljs-keyword">const</span> forceUpdate = useForceUpdate()
  <span class="hljs-keyword">const</span> handleClick = useCallback(<span class="hljs-function">() =></span> &#123;
    <span class="hljs-comment">// 使用 setTimeout，跳过 React 的批量更新机制</span>
    <span class="hljs-built_in">setTimeout</span>(<span class="hljs-function">() =></span> &#123;
      <span class="hljs-comment">// 更新 list Model，更新后框架自动触发 forceUpdate</span>
      <span class="hljs-comment">// 这里手动触发进行模拟</span>
      <span class="hljs-comment">// order 1</span>
      list.push(<span class="hljs-built_in">Math</span>.random() >= <span class="hljs-number">0.5</span> ? <span class="hljs-string">"item"</span> : <span class="hljs-string">"moon"</span>)
      forceUpdate()

      <span class="hljs-comment">// 更新 total Model，更新后框架自动触发 forceUpdate</span>
      <span class="hljs-comment">// 这里手动触发进行模拟</span>
      <span class="hljs-comment">// order 4</span>
      total = total + <span class="hljs-number">1</span>
      forceUpdate()
    &#125;, <span class="hljs-number">0</span>)
  &#125;, [forceUpdate])

  useLayoutEffect(<span class="hljs-function">() =></span> &#123;
    <span class="hljs-comment">// 删除 list Model 中的存在 moon 数据项</span>
    <span class="hljs-keyword">if</span> (list.includes(<span class="hljs-string">"moon"</span>)) &#123;
      <span class="hljs-comment">// order 2</span>
      list = list.filter(<span class="hljs-function"><span class="hljs-params">it</span> =></span> it !== <span class="hljs-string">"moon"</span>)
      forceUpdate()

      <span class="hljs-comment">// order 3</span>
      total = list.length
      forceUpdate()
    &#125;
  &#125;, [list, total, forceUpdate])

  <span class="hljs-keyword">return</span> (
    <span class="xml"><span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">className</span>=<span class="hljs-string">"App"</span>></span>
      <span class="hljs-tag"><<span class="hljs-name">button</span> <span class="hljs-attr">onClick</span>=<span class="hljs-string">&#123;handleClick&#125;</span>></span>添加一项数据<span class="hljs-tag"></<span class="hljs-name">button</span>></span>
      <span class="hljs-tag"><<span class="hljs-name">div</span>></span>共&#123;total&#125;项数据<span class="hljs-tag"></<span class="hljs-name">div</span>></span>
      <span class="hljs-tag"><<span class="hljs-name">div</span>></span>
        &#123;list.map(it => (
          <span class="hljs-tag"><<span class="hljs-name">div</span>></span>&#123;it&#125;<span class="hljs-tag"></<span class="hljs-name">div</span>></span>
        ))&#125;
      <span class="hljs-tag"></<span class="hljs-name">div</span>></span>
    <span class="hljs-tag"></<span class="hljs-name">div</span>></span></span>
  )
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>如果点击按钮后生成的数据是 <code>"moon"</code>，那么页面就会出现数据不一致的现象。
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/b1c419fc03504289811f793aebdf3914~tplv-k3u1fbpfcp-watermark.image" alt="flux-mvc-demo.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>引起数据不一致的原因是：</p>
<ol>
<li>向 list Model 中添加数据项 "moon"，触发组件重新 Render。</li>
<li>在 <code>useLayoutEffect</code> 更新了 list Model 和 total Model。</li>
<li>回到 <code>handleClick</code> 函数中执行 <code>total = total + 1</code>，此时 <code>total</code> 比 <code>list.length</code> 大 1。</li>
</ol>
<p>这就是 Facebook 使用 MVC 框架时的数据流。在 <code>handleClick</code> 回调中，期望 <code>list.push(...)</code> 和 <code>total = total + 1</code> 一起执行。但万万没想到，中间被插了一脚，导致 Model 值已经不符合预期了。</p>
<p>上述例子中没有 MVC 中的 Controller。即使我们把更新 Model 的代码封装成函数，并封装到 Controller 对象中，让它完全符合 MVC 架构，它和上述例子仍然没有本质区别。只是通过 Action 通知 Controller 对 Model 进行更新罢了。</p>
<h2 data-id="heading-3">层叠更新（Cascading Updates）</h2>
<p>在 Action1 中更新 Model 后（参考例子中的 handleClick 回调），引起页面重新渲染，同时又触发 Action2（参考例子中 useLayoutEffect 的回调）。<strong>在 Action2 执行时，Action1 并没有结束。即同时存在两个 Action 被处理。</strong> 这就是 Facebook 团队所说的层叠更新（Cascading Updates）。也可以理解为更新一个 Model 引起了另一个 Model 发生更新。
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/ff0e1d979c744d6c859b3f169724b1f5~tplv-k3u1fbpfcp-watermark.image" alt="MVC-jing-多-View.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h1 data-id="heading-4">Flux</h1>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/dab2258b183c477b9abaf6cbe1aa8484~tplv-k3u1fbpfcp-watermark.image" alt="flux-data-flow.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>与 MVC 对比，Flux 将 Controller 命名为 Dispatcher，将 Model 命名为 Store。View 中不会直接更新 Model，而是通过向 Dispatcher 发起 Action 通知 Store 更新。</p>
<p>只看图的话，Flux 数据流和 MVC 数据流只有命名上的区别。我们还是看看 Flux 架构更多的设计思想吧。</p>
<h2 data-id="heading-5">避免层叠更新</h2>
<p>Flux 通过 Dispatcher 避免层叠更新问题。<strong>一个 Action 必须被所有 Store 处理完之后，才能发起下一个 Action，否则 Dispatcher 将报错。</strong></p>
<p>在上面的例子中，需要将 <code>handleClick</code> 定义为一个 Action <code>"addItem"</code>。list Store 和 total Store 都需要对该 Action 进行处理。当点击按钮后，如果添加的数据项是 <code>"moon"</code>，代码执行的流程如下：</p>
<ol>
<li>发起 <code>"addItem"</code> Action，item 为 "moon"。</li>
<li>执行 list.push("moon")` 更新了 list Store，触发 React 组件重新渲染。</li>
<li>在 <code>useLayoutEffect</code> 中向 Dispatcher 发起另一个 Action <code>"removeMoon"</code>。</li>
<li>Dispatcher 检查到前一个 Action <code>"addItem"</code> 没有结束，报错。</li>
</ol>
<p>从上述流程中可以看出，Flux 是在运行时避免层叠更新的。如果开发过程中没有发现层叠更新问题，那么该问题就会在线上环境暴露出来。</p>
<h2 data-id="heading-6">单向数据流</h2>
<p>单向数据流是指状态更新由 Action 到 Dispatcher，再到 Store，最后到 Container View 和 View 组件。通过单向数据流，我们将轻松地由 Action 推理出 Store 数据，最后得出 View 界面。</p>
<p>单向数据流的另一面是双向绑定，即更新一个 Store 将引起另一个 Store 发生更新（也是层叠更新）。在 Flux 中，多个 Store 可以存在依赖关系，但它们必须有严格的层级，并且通过 Dispatcher 同步更新它们。</p>
<blockquote>
<p>参考<a href="https://facebook.github.io/flux/docs/in-depth-overview/" target="_blank" rel="nofollow noopener noreferrer">原文</a>。
We found that two-way data bindings led to cascading updates, where changing one object led to another object changing, which could also trigger more updates. As applications grew, these cascading updates made it very difficult to predict what would change as the result of one user interaction. When updates can only change data within a single round, the system as a whole becomes more predictable.</p>
</blockquote>
<h2 data-id="heading-7">Dispatcher API</h2>
<p>本节代码出自<a href="https://facebook.github.io/flux/docs/dispatcher" target="_blank" rel="nofollow noopener noreferrer">Flux Dispatcher</a>。</p>
<h3 data-id="heading-8">register(fn)</h3>
<p><code>register(fn)</code> 是将更新 Store 的代码都塞进 <code>fn</code> 中。其返回值可用于 <code>unregister(id)</code> 和 <code>waitFor(id[])</code>。</p>
<pre><code class="hljs language-js copyable" lang="js">CountryStore.dispatchToken = flightDispatcher.register(<span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">payload</span>) </span>&#123;
  <span class="hljs-keyword">if</span> (payload.actionType === <span class="hljs-string">"country-update"</span>) &#123;
    CountryStore.country = payload.selectedCountry
  &#125;
&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-9">unregister(id)</h3>
<p>取消注册。</p>
<h3 data-id="heading-10">waitFor(id[])</h3>
<p>当 Action 触发后，Store1 和 Store2 都要更新状态，并且 Store1 依赖 Store2 最新的状态。此时，需要在 Store1 的更新方法中调用 <code>waitFor</code>，让 Store2 先进行更新。<code>waitFor</code> 是按照 Action 粒度划分的，不同的 Action，Store 之间的依赖关系可能不同。如果 <code>waitFor</code> 存在循环依赖，则 Dispatcher 将报错。</p>
<pre><code class="hljs language-js copyable" lang="js">CityStore.dispatchToken = flightDispatcher.register(<span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">payload</span>) </span>&#123;
  <span class="hljs-keyword">if</span> (payload.actionType === <span class="hljs-string">"country-update"</span>) &#123;
    <span class="hljs-comment">// `CountryStore.country` may not be updated.</span>
    flightDispatcher.waitFor([CountryStore.dispatchToken])
    <span class="hljs-comment">// `CountryStore.country` is now guaranteed to be updated.</span>

    <span class="hljs-comment">// Select the default city for the new country</span>
    CityStore.city = getDefaultCityForCountry(CountryStore.country)
  &#125;
&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-11">dispatch(...)</h3>
<p>派发事件。如果在 <code>isDispatching()</code> 返回 true 时，执行 <code>dispatch()</code> 将报错。这种机制是为了避免层叠更新。</p>
<h3 data-id="heading-12">isDispatching()</h3>
<p>判断当前是否在派发事件的过程中。</p>
<h1 data-id="heading-13">总结</h1>
<p>从 Facebook 在 14 年提出 Flux 到现在，已经有 7 年了。本文考古了 Flux 架构的背景、解决的问题以及解决方式，同时也解释了单向数据流和层叠更新。Flux 是 React 数据管理的鼻祖，Redux 就是基于它而生的，理解它对数据管理的发展非常有帮助。</p>
<h1 data-id="heading-14">推荐更多 React 文章</h1>
<ol>
<li><a href="https://juejin.cn/post/6935584878071119885" target="_blank">React 性能优化 | 包括原理、技巧、Demo、工具使用</a></li>
<li><a href="https://juejin.cn/post/6943397563114455048" target="_blank">聊聊 useSWR，为开发提效 - 包括 useSWR 设计思想、优缺点和最佳实践</a></li>
<li><a href="https://juejin.cn/post/6951206227418284063" target="_blank">React 为什么使用 Lane 技术方案</a></li>
<li><a href="https://juejin.cn/post/6953804914715803678" target="_blank">React Scheduler 为什么使用 MessageChannel 实现</a></li>
<li><a href="https://juejin.cn/post/6956397155363848228" target="_blank">为什么「不变的虚拟 DOM」可以避免组件重新 Render</a></li>
<li><a href="https://juejin.cn/post/6959372766114119688" target="_blank">深入理解 useEffect 和 useLayoutEffect 中回调函数的执行时机</a></li>
</ol>
<hr>
<blockquote>
<p><strong>招贤纳士</strong></p>
<p>笔者在<strong>成都</strong>-<strong>字节跳动</strong>-<strong>私有云方向</strong>，主要技术栈为 React + Node.js。
团队扩张速度快，组内技术氛围活跃。公有云私有云刚刚起步，有很多技术挑战，未来可期。</p>
<p>有意愿者可通过该链接投递简历：<a href="https://job.toutiao.com/s/e69g1rQ" target="_blank" rel="nofollow noopener noreferrer">job.toutiao.com/s/e69g1rQ</a></p>
<p>也可以添加我的微信 <code>moonball_cxy</code>，一起聊聊，交个朋友。</p>
</blockquote>
<p><strong>原创不易，别忘了点赞鼓励哦 ❤️</strong></p></div>  
</div>
            