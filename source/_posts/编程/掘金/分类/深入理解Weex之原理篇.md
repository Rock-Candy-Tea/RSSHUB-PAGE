
---
title: '深入理解Weex之原理篇'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=7090'
author: 掘金
comments: false
date: Sat, 21 Aug 2021 18:32:36 GMT
thumbnail: 'https://picsum.photos/400/300?random=7090'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>这是我参与 8 月更文挑战的第 22 天，活动详情查看： <a href="https://juejin.cn/post/6987962113788493831" target="_blank" title="https://juejin.cn/post/6987962113788493831">8月更文挑战</a></p>
<h2 data-id="heading-0">前言</h2>
<p>前端工程师们一直在探索编写一套代码，可以运行在H5、安卓、IOS平台。</p>
<p>在早期，采用Hybrid进行H5混合开发，这种模式APP就相当于一个浏览器，暴露给H5一些native的能力做通信。这种模式开发效率快，但是在性能上有一定的瓶颈。</p>
<h2 data-id="heading-1">Weex</h2>
<p>到后来，Vue、React这类前端框架开始大行其道，一个重要的概念促使了跨端的发展，那就是虚拟DOM。这是一种DSL的描述，通过不同平台的渲染API实现屏幕绘制。比如在浏览器通过<code>document</code>,在native上通过原生的API进行渲染绘制。</p>
<p>再来后来，Weex诞生了，不得不说，Weex是Vue的一种跨端实现。Weex依旧采取前端H5页面进行开发，同时app在终端的运行体验不输native app。即可以保证快速响应需求，又可以保证用户体验。</p>
<h2 data-id="heading-2">工作流程</h2>
<p>我们先来看下Weex的工作流程：</p>
<ol>
<li>开发者编写Vue文件，通过打包工具打包成多个JS文件；</li>
<li>在APP端请求JS文件，通过JS执行引擎(JSCore)运行JS文件；</li>
<li>执行输出VNode，调用WXBridge（Weex渲染引擎）</li>
<li>WXBridge继续调用原生渲染API，完成最终渲染</li>
</ol>
<p>看完工作流程，我们可以得出以下结论：</p>
<ul>
<li>把性能损耗较大的渲染工作交给native，而逻辑由JSCore解析执行</li>
</ul>
<h3 data-id="heading-3">构建渲染指令树</h3>
<p>在浏览器上它们都使用一致的 DOM API 把 Virtual DOM 转换成真实的 HTMLElement。在 Weex 里的逻辑也是类似的，只是在最后一步生成真实元素的过程中，不使用原生 DOM API，而是使用 JS Framework 里定义的一套 Weex DOM API 将操作转化成渲染指令发给客户端。</p>
<p>JS Framework 提供的 Weex DOM API 和浏览器提供的 DOM API 功能基本一致，在 Vue 和 Rax 内部对这些接口都做了适配，针对 Weex 和浏览器平台调用不同的接口就可以实现跨平台渲染。</p>
<h3 data-id="heading-4">JS-Native 通信</h3>
<p>在开发页面过程中，除了节点的渲染以外，还有原生模块的调用、事件绑定、回调等功能，这些功能都依赖于 js 和 native 之间的通信来实现。</p>
<p>首先，页面的 js 代码是运行在 js 线程上的，然而原生组件的绘制、事件的捕获都发生在 UI 线程。在这两个线程之间的通信用的是 callNative 和 callJS 这两个底层接口（现在已经扩展到了很多个），它们默认都是异步的，在 JS Framework 和原生渲染器内部都基于这两个方法做了各种封装。</p>
<p>callNative 是由客户端向 JS 执行环境中注入的接口，提供给 JS Framework 调用，界面的节点（上文提到的渲染指令树）、模块调用的方法和参数都是通过这个接口发送给客户端的。为了减少调用接口时的开销，其实现在已经开了更多更直接的通信接口，其中有些接口还支持同步调用（支持返回值），它们在原理上都和 callNative 是一样的。</p>
<p>callJS 是由 JS Framework 实现的，并且也注入到了执行环境中，提供给客户端调用。事件的派发、模块的回调函数都是通过这个接口通知到 JS Framework，然后再将其传递给上层前端框架。</p>
<h3 data-id="heading-5">JS Service</h3>
<p>Weex 是一个多页面的框架，每个页面的 js bundle 都在一个独立的环境里运行，不同的 Weex 页面对应到浏览器上就相当于不同的“标签页”，普通的 js 库没办法实现在多个页面之间实现状态共享，也很难实现跨页通信。</p>
<p>JS Framework 中实现了 JS Service 的功能，主要就是用来解决跨页面复用和状态共享的问题的，例如 BroadcastChannel 就是基于 JS Service 实现的，它可以在多个 Weex 页面之间通信。</p>
<h2 data-id="heading-6">小结</h2>
<p>Weex的本质也是一种运行时渲染，而不是编译时。这有点类似于webview容器，但是Weex的最终是由native实现的，所以在运行性能上是可以和原生APP媲美的。</p></div>  
</div>
            