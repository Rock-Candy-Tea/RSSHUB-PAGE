
---
title: 'React 18 发布'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=9036'
author: 开源中国
comments: false
date: Wed, 30 Mar 2022 00:20:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=9036'
---

<div>   
<div class="content">
                                                                                            <p><span style="color:#000000">React 18 现已</span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Freactjs.org%2Fblog%2F2022%2F03%2F29%2Freact-v18.html" target="_blank">发布</a><span style="color:#000000">，此版本包括开箱即用的改进，如自动批处理，新的 API（如 startTransition）和支持 Suspense 的流式服务器端渲染。</span></p> 
<p><span style="color:#000000">公告指出，React 18 中的许多功能都建立在新的并发渲染器之上，这是一个解锁强大新功能的幕后更改。Concurrent React 是可选的，它仅在用户使用并发功能时启用，但开发团队认为它将会对大众构建应用程序的方式产生重大影响。</span></p> 
<p style="margin-left:0; margin-right:0; text-align:start">“<span><span><span><span style="color:#000000"><span><span><span><span><span><span><span><span><span><span><span><span><span><span>我们花了数年时间研究和开发对 React 并发的支持，并且我们特别注意为现有用户提供逐步采用的路径。去年夏天，<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Freactjs.org%2Fblog%2F2021%2F06%2F08%2Fthe-plan-for-react-18.html" target="_blank">我们成立了 React 18 工作组</a>，收集社区专家的反馈，确保整个 React 生态系统的顺利升级体验。</span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span>”</p> 
<p style="margin-left:0; margin-right:0; text-align:start"><span style="color:#000000">在 React 18 中，用户还可以开始使用 Suspense 在 Relay、Next.js、Hydrogen 或 Remix 等框架中获取数据。官方表示，使用 Suspense 获取临时数据在技术上是可行的，但仍不建议将其作为一般策略。在未来，其可能会公开更多的 primitives，使用户能够更容易用 Suspense 访问数据。</span></p> 
<p style="margin-left:0; margin-right:0"><span style="color:#000000">公告指出，其对 Suspense 的愿景始终不仅仅是加载代码——目标是扩展对 Suspense 的支持，以便最终相同的声明式 Suspense fallback 可以处理任何异步操作（加载代码、数据、图像等）。</span></p> 
<p style="margin-left:0px; margin-right:0px"><span style="color:#000000">React 18 的新功能如下：</span></p> 
<ul> 
 <li><strong><span><span><span><span style="color:#000000"><span><span><span><span><span><span><span><span><span><span><span><span><span>自动批处理。</span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></strong><span><span><span><span style="color:#000000"><span><span><span><span><span><span><span><span><span><span><span><span><span><span>批处理是 React 将多个状态更新分组到一个重新渲染中以获得更好的性能。如果没有自动批处理，我们只能在 React 事件处理程序中批处理更新。默认情况下，Promise、setTimeout、native event handlers 或任何其他事件内部的更新不会在 React 中批处理。使用自动批处理，这些更新将自动批处理：</span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></li> 
</ul> 
<pre style="margin-left:1rem; margin-right:1rem; text-align:start"><code><span style="color:#b2b2b2">// Before: only React events were batched.</span>
<span style="color:#79b6f2">setTimeout</span><span style="color:#88c6be">(</span><span style="color:#88c6be">(</span><span style="color:#88c6be">)</span> <span style="color:#d7deea">=></span> <span style="color:#88c6be">&#123;</span>
  <span style="color:#79b6f2">setCount</span><span style="color:#88c6be">(</span><span>c</span> <span style="color:#d7deea">=></span> c <span style="color:#d7deea">+</span> <span style="color:#5a9bcf">1</span><span style="color:#88c6be">)</span><span style="color:#88c6be">;</span>
  <span style="color:#79b6f2">setFlag</span><span style="color:#88c6be">(</span><span>f</span> <span style="color:#d7deea">=></span> <span style="color:#d7deea">!</span>f<span style="color:#88c6be">)</span><span style="color:#88c6be">;</span>
  <span style="color:#b2b2b2">// React will render twice, once for each state update (no batching)</span>
<span style="color:#88c6be">&#125;</span><span style="color:#88c6be">,</span> <span style="color:#5a9bcf">1000</span><span style="color:#88c6be">)</span><span style="color:#88c6be">;</span>

<span style="color:#b2b2b2">// After: updates inside of timeouts, promises,</span>
<span style="color:#b2b2b2">// native event handlers or any other event are batched.`</span>
<span style="color:#79b6f2">setTimeout</span><span style="color:#88c6be">(</span><span style="color:#88c6be">(</span><span style="color:#88c6be">)</span> <span style="color:#d7deea">=></span> <span style="color:#88c6be">&#123;</span>
  <span style="color:#79b6f2">setCount</span><span style="color:#88c6be">(</span><span>c</span> <span style="color:#d7deea">=></span> c <span style="color:#d7deea">+</span> <span style="color:#5a9bcf">1</span><span style="color:#88c6be">)</span><span style="color:#88c6be">;</span>
  <span style="color:#79b6f2">setFlag</span><span style="color:#88c6be">(</span><span>f</span> <span style="color:#d7deea">=></span> <span style="color:#d7deea">!</span>f<span style="color:#88c6be">)</span><span style="color:#88c6be">;</span>
  <span style="color:#b2b2b2">// React will only re-render once at the end (that's batching!)</span>
<span style="color:#88c6be">&#125;</span><span style="color:#88c6be">,</span> <span style="color:#5a9bcf">1000</span><span style="color:#88c6be">)</span><span style="color:#88c6be">;</span></code></pre> 
<ul style="margin-left:0; margin-right:0"> 
 <li style="text-align:start">Transitions 是<span><span><span><span style="color:#000000"><span><span><span><span><span><span><span><span><span><span><span><span><span><span> React 中的一个新概念，用于区分 urgent 和 non-urgent updates。</span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span> <pre><code><ul>
<li><strong>Urgent updates </strong>反映了直接交互，例如 typing、clicking、pressing等。</li>
<li><strong>Transition updates </strong>将 UI 从一个视图转换到另一个视图。</li>
</ul>
</li>
</code></pre> </li> 
</ul> 
<pre style="margin-left:1rem; margin-right:1rem; text-align:start"><code><span style="color:#c5a5c5">import</span> <span style="color:#88c6be">&#123;</span>startTransition<span style="color:#88c6be">&#125;</span> <span style="color:#c5a5c5">from</span> <span style="color:#8dc891">'react'</span><span style="color:#88c6be">;</span>

<span style="color:#b2b2b2">// Urgent: Show what was typed</span>
<span style="color:#79b6f2">setInputValue</span><span style="color:#88c6be">(</span>input<span style="color:#88c6be">)</span><span style="color:#88c6be">;</span>

<span style="color:#b2b2b2">// Mark any state updates inside as transitions</span>
<span style="color:#79b6f2">startTransition</span><span style="color:#88c6be">(</span><span style="color:#88c6be">(</span><span style="color:#88c6be">)</span> <span style="color:#d7deea">=></span> <span style="color:#88c6be">&#123;</span>
  <span style="color:#b2b2b2">// Transition: Show the results</span>
  <span style="color:#79b6f2">setSearchQuery</span><span style="color:#88c6be">(</span>input<span style="color:#88c6be">)</span><span style="color:#88c6be">;</span>
<span style="color:#88c6be">&#125;</span><span style="color:#88c6be">)</span><span style="color:#88c6be">;</span></code></pre> 
<ul> 
 <li> <p style="margin-left:0px; margin-right:0px; text-align:start"><strong><span><span><span><span style="color:#000000"><span><span><span><span><span><span><span><span><span><span><span><span><span>新的 </span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span>Suspense <span><span><span><span style="color:#000000"><span><span><span><span><span><span><span><span><span><span><span><span><span>功能。</span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></strong><span><span><span><span style="color:#000000"><span><span><span><span><span><span><span><span><span><span><span><span><span><span>如果组件树的一部分尚未准备好显示，Suspense 允许你以声明方式指定组件树的加载状态：</span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></p> </li> 
</ul> 
<pre style="margin-left:1rem; margin-right:1rem; text-align:start"><code><span style="color:#fc929e"><span style="color:#fc929e"><span style="color:#88c6be"><</span><span style="color:#fac863">Suspense</span></span> <span style="color:#c5a5c5">fallback</span><span><span style="color:#88c6be">=</span><span style="color:#88c6be">&#123;</span><span style="color:#fc929e"><span style="color:#fc929e"><span style="color:#88c6be"><</span><span style="color:#fac863">Spinner</span></span> <span style="color:#88c6be">/></span></span><span style="color:#88c6be">&#125;</span></span><span style="color:#88c6be">></span></span><span>
  </span><span style="color:#fc929e"><span style="color:#fc929e"><span style="color:#88c6be"><</span><span style="color:#fac863">Comments</span></span> <span style="color:#88c6be">/></span></span><span>
</span><span style="color:#fc929e"><span style="color:#fc929e"><span style="color:#88c6be">
     <!--</span--><span style="color:#fac863">Suspense</span></span><span style="color:#88c6be">></span></span></span></code></pre> 
<p style="margin-left:0; margin-right:0; text-align:start"><span><span><span><span style="color:#000000"><span><span><span><span><span><span><span><span><span><span><span><span><span><span>Suspense 使“UI loading state”成为 React 编程模型中的 first-class 声明性概念。这让我们可以在它之上构建更高级别的功能。</span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></p> 
<p style="margin-left:0; margin-right:0; text-align:start"><span><span><span><span style="color:#000000"><span><span><span><span><span><span><span><span><span><span><span><span><span><span>React 18 中在服务器上添加了对 Suspense 的支持，并使用并发渲染特性扩展了它的功能。React 18 中的 Suspense 与 transition API 结合使用时效果最佳。如果你在 transition 期间 suspend，React 将防止已经可见的内容被 fallback 所取代。相反，React 会延迟渲染，直到加载了足够的数据以防止出现错误的加载状态。</span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></p> 
<ul> 
 <li style="text-align:start"><span><span><span><span style="color:#000000"><span><span><span><span><span><span><span><span><span><span><span><span><span><span><strong>新的客户端和服务器渲染 API。</strong></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span>这些更改允许用户在升级到 React 18 中的新 API 时继续使用 React 17 模式下的旧 API。</li> 
 <li style="text-align:start"><strong><span style="background-color:#ffffff; color:#333333">新的严格模式行为 (Strict Mode </span>Behaviors<span style="background-color:#ffffff; color:#333333">)。</span></strong><span style="background-color:#ffffff; color:#333333">此功能将为 React 应用程序提供更好的开箱即用性能，但要求组件能够对多次挂载和销毁的效果具有弹性。大多数效果无需任何更改即可工作，但有些效果假定它们只挂载或销毁一次。为了帮助解决这些问题，React 18 为严格模式引入了一个新的仅限开发的检查。每当第一次安装组件时，此新检查将自动卸载并重新挂载每个组件，并在第二次挂载时恢复先前的状态。</span>​​​​​</li> 
</ul> 
<pre style="margin-left:1rem; margin-right:1rem; text-align:start"><code>* React mounts the component.
  * Layout effects are created.
  * Effects are created.
* React simulates unmounting the component.
  * Layout effects are destroyed.
  * Effects are destroyed.
* React simulates mounting the component with the previous state.
  * Layout effects are created.
  * Effects are created.</code></pre> 
<p style="margin-left:0px; margin-right:0px; text-align:start">更多详情可查看：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Freactjs.org%2Fblog%2F2022%2F03%2F29%2Freact-v18.html" target="_blank">https://reactjs.org/blog/2022/03/29/react-v18.html</a></p>
                                        </div>
                                      
</div>
            