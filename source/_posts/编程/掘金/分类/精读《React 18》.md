
---
title: '精读《React 18》'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/414933a6d87e46c0990f30e6b7048bb9~tplv-k3u1fbpfcp-zoom-1.image'
author: 掘金
comments: false
date: Sun, 11 Jul 2021 21:47:45 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/414933a6d87e46c0990f30e6b7048bb9~tplv-k3u1fbpfcp-zoom-1.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>React 18 带来了几个非常实用的新特性，同时也没有额外的升级成本，值得仔细看一看。</p>
<p>下面是几个关键信息：</p>
<ul>
<li><a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Freactwg%2Freact-18" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/reactwg/react-18" ref="nofollow noopener noreferrer">React 18 工作小组</a>。利用社区讨论 React 18 发布节奏与新特性。</li>
<li><a href="https://link.juejin.cn/?target=https%3A%2F%2Freactjs.org%2Fblog%2F2021%2F06%2F08%2Fthe-plan-for-react-18.html" target="_blank" rel="nofollow noopener noreferrer" title="https://reactjs.org/blog/2021/06/08/the-plan-for-react-18.html" ref="nofollow noopener noreferrer">发布计划</a>。目前还没有正式发布，不过 <code>@alpha</code> 版已经可用了，<a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Freactwg%2Freact-18%2Fdiscussions%2F9" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/reactwg/react-18/discussions/9" ref="nofollow noopener noreferrer">安装 alpha 版</a>。</li>
<li><a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Freactwg%2Freact-18%2Fdiscussions%2F4" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/reactwg/react-18/discussions/4" ref="nofollow noopener noreferrer">React 18 新特性介绍</a>。虽然还未正式发布，但特性介绍可以先行，本周精读主要就是解读这篇文档。</li>
</ul>
<h2 data-id="heading-0">精读</h2>
<p>总的来说，React 18 带来了 3 大新特性：</p>
<ul>
<li>Automatic batching。</li>
<li>Concurrent APIS。</li>
<li>SSR for Suspense。</li>
</ul>
<p>同时为了开启新的特性，需要进行简单的 <code>render</code> 函数升级。</p>
<h3 data-id="heading-1">Automatic batching</h3>
<p>batching 是指，React 可以将回调函数中多个 <code>setState</code> 事件合并为一次渲染。</p>
<p>也就是说，<code>setState</code> 并不是实时修改 State 的，而将多次 <code>setState</code> 调用合并起来仅触发一次渲染，既可以减少程序数据状态存在中间值导致的不稳定性，也可以提升渲染性能。可以理解为如下代码所示：</p>
<pre><code class="hljs language-typescript copyable" lang="typescript"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">handleClick</span>(<span class="hljs-params"></span>) </span>&#123;
  setCount(<span class="hljs-function">(<span class="hljs-params">c</span>) =></span> c + <span class="hljs-number">1</span>);
  setFlag(<span class="hljs-function">(<span class="hljs-params">f</span>) =></span> !f);
  <span class="hljs-comment">// 仅触发一次渲染</span>
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>但可惜的是，React 18 以前，如果在回调函数的异步调用中执行 <code>setState</code>，由于丢失了上下文，无法做合并处理，所以每次 <code>setState</code> 调用都会立即触发一次重渲染：</p>
<pre><code class="hljs language-typescript copyable" lang="typescript"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">handleClick</span>(<span class="hljs-params"></span>) </span>&#123;
  <span class="hljs-comment">// React 18 以前的版本</span>
  fetch(<span class="hljs-comment">/*...*/</span>).then(<span class="hljs-function">() =></span> &#123;
    setCount(<span class="hljs-function">(<span class="hljs-params">c</span>) =></span> c + <span class="hljs-number">1</span>); <span class="hljs-comment">// 立刻重渲染</span>
    setFlag(<span class="hljs-function">(<span class="hljs-params">f</span>) =></span> !f); <span class="hljs-comment">// 立刻重渲染</span>
  &#125;);
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>而 React 18 带来的优化便是，任何情况都可以合并渲染了！即使在 <code>promise</code>、<code>timeout</code> 或者 <code>event</code> 回调中调用多次 <code>setState</code>，也都会合并为一次渲染：</p>
<pre><code class="hljs language-typescript copyable" lang="typescript"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">handleClick</span>(<span class="hljs-params"></span>) </span>&#123;
  <span class="hljs-comment">// React 18+</span>
  fetch(<span class="hljs-comment">/*...*/</span>).then(<span class="hljs-function">() =></span> &#123;
    setCount(<span class="hljs-function">(<span class="hljs-params">c</span>) =></span> c + <span class="hljs-number">1</span>);
    setFlag(<span class="hljs-function">(<span class="hljs-params">f</span>) =></span> !f);
    <span class="hljs-comment">// 仅触发一次渲染</span>
  &#125;);
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>当然如果你非要 <code>setState</code> 调用后立即重渲染也行，只需要用 <code>flushSync</code> 包裹：</p>
<pre><code class="hljs language-typescript copyable" lang="typescript"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">handleClick</span>(<span class="hljs-params"></span>) </span>&#123;
  <span class="hljs-comment">// React 18+</span>
  fetch(<span class="hljs-comment">/*...*/</span>).then(<span class="hljs-function">() =></span> &#123;
    ReactDOM.flushSync(<span class="hljs-function">() =></span> &#123;
      setCount(<span class="hljs-function">(<span class="hljs-params">c</span>) =></span> c + <span class="hljs-number">1</span>); <span class="hljs-comment">// 立刻重渲染</span>
      setFlag(<span class="hljs-function">(<span class="hljs-params">f</span>) =></span> !f); <span class="hljs-comment">// 立刻重渲染</span>
    &#125;);
  &#125;);
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>开启这个特性的前提是，将 <code>ReactDOM.render</code> 替换为 <code>ReactDOM.createRoot</code> 调用方式。</p>
<h3 data-id="heading-2">新的 ReactDOM Render API</h3>
<p>升级方式很简单：</p>
<pre><code class="hljs language-typescript copyable" lang="typescript"><span class="hljs-keyword">const</span> container = <span class="hljs-built_in">document</span>.getElementById(<span class="hljs-string">"app"</span>);

<span class="hljs-comment">// 旧 render API</span>
ReactDOM.render(<span class="xml"><span class="hljs-tag"><<span class="hljs-name">App</span> <span class="hljs-attr">tab</span>=<span class="hljs-string">"home"</span> /></span></span>, container);

<span class="hljs-comment">// 新 createRoot API</span>
<span class="hljs-keyword">const</span> root = ReactDOM.createRoot(container);
root.render(<span class="xml"><span class="hljs-tag"><<span class="hljs-name">App</span> <span class="hljs-attr">tab</span>=<span class="hljs-string">"home"</span> /></span></span>);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>API 修改的主要原因还是语义化，即当我们多次调用 <code>render</code> 时，不再需要重复传入 <code>container</code> 参数，因为在新的 API 中，<code>container</code> 已经提前绑定到 <code>root</code> 了。</p>
<p><code>ReactDOM.hydrate</code> 也被 <code>ReactDOM.hydrateRoot</code> 代替：</p>
<pre><code class="hljs language-typescript copyable" lang="typescript"><span class="hljs-keyword">const</span> root = ReactDOM.hydrateRoot(container, <span class="xml"><span class="hljs-tag"><<span class="hljs-name">App</span> <span class="hljs-attr">tab</span>=<span class="hljs-string">"home"</span> /></span></span>);
<span class="hljs-comment">// 注意这里不用调用 root.render()</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这样的好处是，后续如果再调用 <code>root.render(<Appx />)</code> 进行重渲染，我们不用关心这个 <code>root</code> 来自 <code>createRoot</code> 或者 <code>hydrateRoot</code>，因为后续 API 行为表现都一样，减少了理解成本。</p>
<h3 data-id="heading-3">Concurrent APIS</h3>
<p>首先要了解 Concurrent Mode 是什么。</p>
<p>简单来说，Concurrent Mode 就是一种可中断渲染的设计架构。什么时候中断渲染呢？当一个更高优先级渲染到来时，通过放弃当前的渲染，立即执行更高优先级的渲染，换来视觉上更快的响应速度。</p>
<p>有人可能会说，不对啊，中断渲染后，之前渲染的 CPU 执行不就浪费了吗，换句话说，整体执行时常增加了。这句话是对的，但实际上用户对页面交互及时性的感知是分为两种的，第一种是即时输入反馈，第二种是这个输入带来的副作用反馈，比如更新列表。其中，即使输入反馈只要能优先满足，即便副作用反馈更慢一些，也会带来更好的体验，更不用说副作用反馈大部分情况会因为即使输入反馈的变化而作废。</p>
<p>由于 React 将渲染 DOM 树机制改为两个双向链表，并且渲染树指针只有一个，指向其中一个链表，因此可以在更新完全发生后再切换指针指向，而在指针切换之前，随时可以放弃对另一颗树的修改。</p>
<p>以上是背景输入。React 18 提供了三个新的 API 支持这一模式，分别是：</p>
<ul>
<li>startTransition。</li>
<li>useDeferredValue。</li>
<li>。</li>
</ul>
<p>后两个文档还未放出，所以本文只介绍第一个 API：startTransition。首先看一下用法：</p>
<pre><code class="hljs language-typescript copyable" lang="typescript"><span class="hljs-keyword">import</span> &#123; startTransition &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">"react"</span>;

<span class="hljs-comment">// 紧急更新：</span>
setInputValue(input);

<span class="hljs-comment">// 标记回调函数内的更新为非紧急更新：</span>
startTransition(<span class="hljs-function">() =></span> &#123;
  setSearchQuery(input);
&#125;);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>简单来说，就是被 <code>startTransition</code> 回调包裹的 <code>setState</code> <strong>触发的渲染</strong> 被标记为不紧急的渲染，这些渲染可能被其他紧急渲染所抢占。</p>
<p>比如这个例子，当 <code>setSearchQuery</code> 更新的列表内容很多，导致渲染时 CPU 占用 100% 时，此时用户又进行了一个输入，即触发了由 <code>setInputValue</code> 引起的渲染，此时由 <code>setSearchQuery</code> 引发的渲染会立刻停止，转而对 <code>setInputValue</code> 渲染进行支持，这样用户的输入就能快速反映在 UI 上，代价是搜索列表响应稍慢了一些。而一个 <code>transition</code> 被打断的状态可以通过 <code>isPending</code> 访问到：</p>
<pre><code class="hljs language-typescript copyable" lang="typescript"><span class="hljs-keyword">import</span> &#123; useTransition &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">"react"</span>;
<span class="hljs-keyword">const</span> [isPending, startTransition] = useTransition();
<span class="copy-code-btn">复制代码</span></code></pre>
<p>其实这比较符合操作系统的设计理念，我们知道在操作系统是通过中断响应底层硬件事件的，中断都非常紧急（因为硬件能存储的消息队列非常有限，操作系统不能即使响应，硬件的输入可能就丢失了），因此要支持抢占式内核，并在中断到来时立刻执行中断（可能把不太紧急的操作放到下半部执行）。</p>
<p>对前端交互来说，用户角度发出的 “中断” 一般来自键盘或鼠标的操作，但不幸的是，前端框架甚至是 JS 都过于上层，它们无法自动识别：</p>
<ol>
<li>哪些代码是紧急中断产生的。比如 <code>onClick</code> 就一定是用户鼠标点击产生的吗？不一定，可能是 <code>xxx.onClick</code> 主动触发的，而非用户触发。</li>
<li>用户触发的就一定是紧急中断吗？不一定，比如键盘输入后，<code>setInputValue</code> 是紧急的，而更新查询列表的 <code>setSearchQuery</code> 就是非紧急的。</li>
</ol>
<p>我们要理解到前端场景对用户操作感知的局限性，才能理解为什么必须手动指定更新的紧急程度，而不能像操作系统一样，上层程序无需感知中断的存在。</p>
<h3 data-id="heading-4">SSR for Suspense</h3>
<p>完整名称是：Streaming SSR with selective hydration。</p>
<p>即像水流一样，打造一个从服务端到客户端持续不断的渲染管线，而不是 <code>renderToString</code> 那样一次性渲染机制。selective hydration 表示选择性水合，水合指的是后端内容打到前端后，JS 需要将事件绑定其上，才能响应用户交互或者 DOM 更新行为，而在 React 18 之前，这个操作必须是整体性的，而水合过程可能比较慢，会引起全局的卡顿，所以选择性水合可以按需优先进行水合。</p>
<p>所以这个特性其实是转为 SSR 准备的，而功能启用载体就是 Suspense（所以以后不要再认为 Suspense 只是一个 loading 作用）。其实在 Suspense 设计之初，就是为了解决服务端渲染问题，只是一开始只实装了客户端测的按需加载功能，后面你会逐渐发现 React 团地逐渐赋予了 Suspense 更多强大能力。</p>
<p>SSR for Suspense 解决三个主要问题：</p>
<ul>
<li>SSR 模式下，如果不同模块取数效率不同，会因为最慢的一个模块拖慢整体 HTML 吞吐时间，这可能导致体验还不如非 SSR 来的好。举一个极端情况，假设报表中一个组件依赖了慢查询，需要五分钟数据才能出来，那么 SSR 的后果就是白屏时间拉长到 5 分钟。</li>
<li>即便 SSR 内容打到了页面上，由于 JS 没有加载完毕，所以根本无法进行 hydration，整个页面处于无法交互状态。</li>
<li>即便 JS 加载完了，由于 React 18 之前只能进行整体 hydration，可能导致卡顿，导致首次交互响应不及时。</li>
</ul>
<p>在 React 18 的 server render 中，只要使用 <code>pipeToNodeWritable</code> 代替 <code>renderToString</code> 并配合 <code>Suspense</code> 就能解决上面三个问题。</p>
<p>使用 <code>pipeToNodeWriteable</code> 可以看 <a href="https://link.juejin.cn/?target=https%3A%2F%2Fcodesandbox.io%2Fs%2Ffestive-star-9hfqt%3Ffile%3D%2Fserver%2Frender.js%3A1043-1575" target="_blank" rel="nofollow noopener noreferrer" title="https://codesandbox.io/s/festive-star-9hfqt?file=/server/render.js:1043-1575" ref="nofollow noopener noreferrer">这个例子</a>。</p>
<p>最大的区别在于，服务端渲染由简单的 <code>res.send</code> 改成了 <code>res.socket</code>，这样渲染就从单次行为变成了持续性的行为。</p>
<p>那么 React 18 的 SSR 到底有怎样的效果呢？<a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Freactwg%2Freact-18%2Fdiscussions%2F37" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/reactwg/react-18/discussions/37" ref="nofollow noopener noreferrer">这篇介绍文档</a> 的图建议看一看，非常直观，这里我简要描述一下：</p>
<ol>
<li>被 <code><Suspense></code> 包裹的区块，在服务端渲染时不会阻塞首次吞吐，而且在这个区块准备完毕后（包括异步取数）再实时打到页面中（以 HTML 模式，此时还没有 hydration），在此之前返回的是 <code>fallback</code> 的内容。</li>
<li>hydration 的过程也是逐步的，这样不会导致一下执行所有完整的 js 导致页面卡顿（hydration 其实就是 React 里写的回调注册、各类 Hooks，整个应用的量非常庞大）。</li>
<li>hydration 因为被拆成多部，React 还会提前监听鼠标点击，并提前对点击区域优先级进行 hydration，甚至能抢占已经在其他区域正在进行中的 hydration。</li>
</ol>
<p>那么总结一下，新版 SSR 性能提高的秘诀在于两个字：按需。</p>
<p>而这个难点在于，SSR 需要后端到前端的配合，在 React 18 之前，后端到前端的过程完全没有优化，而现在将 SSR HTML 的吞吐改成多次，按需，并且水合过程中还支持抢占，因此性能得到进一步提升。</p>
<h2 data-id="heading-5">总结</h2>
<p>结合起来看，React 18 关注点在于更快的性能以及用户交互响应效率，其设计理念处处包含了中断与抢占概念。</p>
<p>以后提起前端性能优化，我们就多了一些应用侧的视角（而不仅仅是工程化视角），从以下两个应用优化视角有效提升交互反馈速度：</p>
<ol>
<li>随时中断的框架设计，第一优先级渲染用户最关注的 UI 交互模块。</li>
<li>从后端到前端 “顺滑” 的管道式 SSR，并将 hydration 过程按需化，且支持被更高优先级用户交互行为打断，第一优先水合用户正在交互的部分。</li>
</ol>
<blockquote>
<p>讨论地址是：<a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fdt-fe%2Fweekly%2Fissues%2F336" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/dt-fe/weekly/issues/336" ref="nofollow noopener noreferrer">精读《React 18》· Issue #336 · dt-fe/weekly</a></p>
</blockquote>
<p><strong>如果你想参与讨论，请 <a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fdt-fe%2Fweekly" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/dt-fe/weekly" ref="nofollow noopener noreferrer">点击这里</a>，每周都有新的主题，周末或周一发布。前端精读 - 帮你筛选靠谱的内容。</strong></p>
<blockquote>
<p>关注 <strong>前端精读微信公众号</strong></p>
</blockquote>
<img width="200" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/414933a6d87e46c0990f30e6b7048bb9~tplv-k3u1fbpfcp-zoom-1.image" loading="lazy" referrerpolicy="no-referrer">
<blockquote>
<p>版权声明：自由转载-非商用-非衍生-保持署名（<a href="https://link.juejin.cn/?target=https%3A%2F%2Fcreativecommons.org%2Flicenses%2Fby-nc-nd%2F3.0%2Fdeed.zh" target="_blank" rel="nofollow noopener noreferrer" title="https://creativecommons.org/licenses/by-nc-nd/3.0/deed.zh" ref="nofollow noopener noreferrer">创意共享 3.0 许可证</a>）</p>
</blockquote></div>  
</div>
            