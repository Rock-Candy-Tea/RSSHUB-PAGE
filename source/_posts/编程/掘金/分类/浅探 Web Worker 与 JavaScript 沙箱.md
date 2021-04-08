
---
title: '浅探 Web Worker 与 JavaScript 沙箱'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=5967'
author: 掘金
comments: false
date: Thu, 08 Apr 2021 03:49:40 GMT
thumbnail: 'https://picsum.photos/400/300?random=5967'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h2 data-id="heading-0">一些「炒冷饭」的背景介绍</h2>
<blockquote>
<p>本文并不会从头开始介绍 Web Worker 的基础知识和基本 API 的使用等（只是部分有涉及），若还未了解过 Web Worker，可参考查阅 W3C 标准 <a href="https://w3c.github.io/workers/" target="_blank" rel="nofollow noopener noreferrer">Workers 文档</a> 中的相关介绍。</p>
</blockquote>
<p>自从 2014 年 HTML5 正式推荐标准发布以来，HTML5 增加了越来越多强大的特性和功能，而在这其中，工作线程（Web Worker）概念的推出让人眼前一亮，但未曾随之激起多大的浪花，并被在其随后工程侧的 Angular、Vue、React 等框架的「革命」浪潮所淹没。当然，我们总会偶然看过一些文章介绍，或出于学习的目的做过一些应用场景下的练习，甚或在实际项目中的涉及大量数据计算场景中真的使用过。但相信也有很多人和我一样茫然，找不到这种高大上的技术在实际项目场景中能有哪些能起到广泛作用的应用。</p>
<p>究其原因，Web Worker 独立于 UI 主线程运行的特性使其被大量考虑进行性能优化方面的尝试（比如一些图像分析、3D 计算绘制等场景），以保证在进行大量计算的同时，页面对用户能有及时的响应。而这些性能优化的需求在前端侧一方面涉及频率低，另一方面也能通过微任务或服务端侧处理来解决，它并不能像 Web Socket 这种技术为前端页面下的轮询场景的优化能带来质的改变。</p>
<p>直至 2019 年爆火的微前端架构的出现，基于微应用间 JavaScript 沙箱隔离的需求，Web Worker 才得以重新从边缘化的位置跃入到我的中心视野。根据我已经了解到的 Web Worker 的相关知识，我知道了 Web Worker 是工作在一个独立子线程下（虽然这个子线程比起 Java 等编译型语言的子线程实现得还有点弱，如无法加锁等），线程之间自带隔离的特性，那基于这种「物理」性的隔离，能不能实现 JavaScript 运行时的隔离呢？</p>
<p>本文接下来的内容，将介绍我在探索基于 Web Worker 实现 JavaScript 沙箱隔离方案过程中的一些资料收集、理解以及我的踩坑和思考的过程。虽然可能整篇文章内容都在「炒冷饭」，但还是希望我的探索方案的过程能对正在看这篇文章的你有所帮助。</p>
<h2 data-id="heading-1">JavaScript 沙箱</h2>
<p>在探索基于 Web Worker 的解决方案之前，我们先要对当前要解决的问题——JavaScript 沙箱有所了解。</p>
<p>提到沙箱，我会先想到出于兴趣玩过的沙盒游戏，但我们要探索的 JavaScript 沙箱不同于沙盒游戏，沙盒游戏注重对世界基本元素的抽象、组合以及物理力系统的实现等，而 JavaScript 沙箱则更注重在使用共享数据时对操作状态的隔离。</p>
<p>在现实与 JavaScript 相关的场景中，我们知道平时使用的浏览器就是一个沙箱，运行在浏览器中的 JavaScript 代码无法直接访问文件系统、显示器或其他任何硬件。Chrome 浏览器中每个标签页也是一个沙箱，各个标签页内的数据无法直接相互影响，接口都在独立的上下文中运行。而在同一个浏览器标签页下运行 HTML 页面，有哪些更细节的、对沙箱现象有需求的场景呢？</p>
<p>当我们作为前端开发人员较长一段时间后，我们很轻易地就能想到在同一个页面下，使用沙箱需求的诸多应用场景，譬如：</p>
<ol>
<li>执行从不受信的源获取到的第三方 JavaScript 代码时（比如引入插件、处理 jsonp 请求回来的数据等）。</li>
<li>在线代码编辑器场景（比如著名的 <a href="https://codesandbox.io/s/new" target="_blank" rel="nofollow noopener noreferrer">codesandbox</a>）。</li>
<li>使用服务端渲染方案。</li>
<li>模板字符串中的表达式的计算。</li>
<li>... ...</li>
</ol>
<p>这里我们先回到开头，先将前提假设在我正在面对的微前端架构设计下。在微前端架构（推荐文章 <a href="https://github.com/phodal/microfrontends" target="_blank" rel="nofollow noopener noreferrer">Thinking in Microfrontend</a> 、<a href="https://mp.weixin.qq.com/s/rYNsKPhw2zR84-4K62gliw" target="_blank" rel="nofollow noopener noreferrer">拥抱云时代的前端开发架构——微前端</a> 等）中，其最关键的一个设计便是各个子应用间的调度实现以及其运行态的维护，而运行时各子应用使用全局事件监听、使全局 CSS 样式生效等常见的需求在多个子应用切换时便会成为一种污染性的副作用，为了解决这些副作用，后来出现的很多微前端架构（如 <a href="https://github.com/umijs/qiankun" target="_blank" rel="nofollow noopener noreferrer">乾坤</a>）有着各种各样的实现。譬如 CSS 隔离中常见的命名空间前缀、Shadow DOM、 <a href="https://github.com/umijs/qiankun/blob/master/src/sandbox/patchers/css.ts" target="_blank" rel="nofollow noopener noreferrer">乾坤 sandbox css</a> 的运行时动态增删等，都有着确实行之有效的具体实践，而这里最麻烦棘手的，还是微应用间的 JavaScript 的沙箱隔离。</p>
<p>在微前端架构中，JavaScript 沙箱隔离需要解决如下几个问题：</p>
<ol>
<li>挂在 window 上的全局方法/变量（如 setTimeout、滚动等全局事件监听等）在子应用切换时的清理和还原。</li>
<li>Cookie、LocalStorage 等的读写安全策略限制。</li>
<li>各子应用独立路由的实现。</li>
<li>多个微应用共存时相互独立的实现。</li>
</ol>
<p>在 <a href="https://github.com/umijs/qiankun" target="_blank" rel="nofollow noopener noreferrer">乾坤</a> 架构设计中，关于沙箱有两个入口文件需要关注，一个是 <a href="https://github.com/umijs/qiankun/blob/master/src/sandbox/proxySandbox.ts" target="_blank" rel="nofollow noopener noreferrer">proxySandbox.ts</a>，另一个是 <a href="https://github.com/umijs/qiankun/blob/master/src/sandbox/snapshotSandbox.ts" target="_blank" rel="nofollow noopener noreferrer">snapshotSandbox.ts</a>，他们分别基于 Proxy 实现代理了 window 上常用的常量和方法以及不支持 Proxy 时降级通过快照实现备份还原。结合其相关开源文章分享，简单总结下其实现思路：起初版本使用了<strong>快照沙箱</strong>的概念，模拟 ES6 的 Proxy API，通过代理劫持 window ，当子应用修改或使用 window 上的属性或方法时，把对应的操作记录下来，每次子应用挂载/卸载时生成快照，当再次从外部切换到当前子应用时，再从记录的快照中恢复，而后来为了兼容多个子应用共存的情况，又基于 Proxy 实现了代理所有全局性的常量和方法接口，为每个子应用构造了独立的运行环境。</p>
<p>另外一种值得借鉴的思路是阿里云开发平台的 <a href="https://github.com/aliyun/alibabacloud-alfa/tree/master/packages/core/browser-vm" target="_blank" rel="nofollow noopener noreferrer">Browser VM</a>，其核心入口逻辑在 <a href="https://github.com/aliyun/alibabacloud-alfa/blob/master/packages/core/browser-vm/src/Context.js" target="_blank" rel="nofollow noopener noreferrer">Context.js</a> 文件中。它的具体实现思路是这样的：</p>
<ol>
<li>借鉴 <code>with</code> 的实现效果，在 webpack 编译打包阶段为每个子应用代码包裹一层代码（见其插件包 <a href="https://github.com/aliyun/alibabacloud-alfa/tree/master/packages/build-tools/breezr-plugin-os/src" target="_blank" rel="nofollow noopener noreferrer">breezr-plugin-os</a> 下相关文件），创建一个闭包，传入自己模拟的 window、document、location、history 等全局对象（见 <a href="https://github.com/aliyun/alibabacloud-alfa/blob/master/packages/core/browser-vm/src" target="_blank" rel="nofollow noopener noreferrer">根目录下</a> 相关文件）。</li>
<li>在模拟的 <a href="https://github.com/aliyun/alibabacloud-alfa/blob/master/packages/core/browser-vm/src/Context.js" target="_blank" rel="nofollow noopener noreferrer">Context</a> 中，new 一个 iframe 对象，提供一个和宿主应用空的（about:blank) 同域 URL 来作为这个 iframe 初始加载的 URL（空的 URL 不会发生资源加载，但是会产生和这个 iframe 中关联的 history 不能被操作的问题，这时路由的变换只支持 hash 模式），然后将其下的原生浏览器对象通过 <code>contentWindow</code> 取出来（因为 iframe 对象天然隔离，这里省去了自己 Mock 实现所有 API 的成本）。</li>
<li>取出对应的 iframe 中原生的对象之后，继续对特定需要隔离的对象生成对应的 Proxy，然后对一些属性获取和属性设置，做一些特定的实现（比如 window.document 需要返回特定的沙箱 document 而不是当前浏览器的document 等）。</li>
<li>为了文档内容能够被加载在同一个 DOM 树上，对于 document，大部分的 DOM 操作的属性和方法仍旧直接使用宿主浏览器中的 document 的属性和方法处理等。</li>
</ol>
<p>总的来说，在 <a href="https://github.com/aliyun/alibabacloud-alfa/tree/master/packages/core/browser-vm" target="_blank" rel="nofollow noopener noreferrer">Browser VM</a> 的实现中， 可以看出其实现部分还是借鉴了 <a href="https://github.com/umijs/qiankun" target="_blank" rel="nofollow noopener noreferrer">乾坤</a> 或者说其他微前端架构的思路，比如常见全局对象的代理和拦截。并且借助 Proxy 特性，针对 Cookie、LocalStorage 的读写同样能做一些安全策略的实现等。但其最大的亮点还是借助 iframe 做了一些取巧的实现，当这个为每个子应用创建的 iframe 被移除时，写在其下 window 上的变量和 setTimeout、全局事件监听等也会一并被移除；另外基于 Proxy，DOM 事件在沙箱中做记录，然后在宿主中生命周期中实现移除，能够以较小的开发成本实现整个 JavaScript 沙箱隔离的机制。</p>
<p>除了以上社区中现在比较火的方案，最近我也在 <a href="https://mp.weixin.qq.com/s/pIRFNpAo8WWinow_2jcGZg" target="_blank" rel="nofollow noopener noreferrer">大型 Web 应用插件化架构探索</a> 一文中了解到了 UI 设计领域的 <a href="https://www.figma.com/" target="_blank" rel="nofollow noopener noreferrer">Figma</a> 产品也基于其插件系统产出了一种隔离方案。起初 Figma 同样是将插件代码放入 iframe 中执行并通过 postMessage 与主线程通信，但由于易用性以及 postMessage 序列化带来的性能等问题，Figma 选择还是将插件放入主线程去执行。Figma 采用的方案是基于目前还在草案阶段 Realm API，并将 JavaScript 解释器的一种 C++ 实现 Duktape 编译到了 WebAssembly，然后将其嵌入到 Realm 上下文中，实现了其产品下的三方插件的独立运行。这种方案和探索的基于 Web Worker 的实现可能能够结合得更好，持续关注中。</p>
<h2 data-id="heading-2">Web Worker 与 DOM 渲染</h2>
<p>在了解了 JavaScript 沙箱的「前世今生」之后，我们将目光投回本文的主角——Web Worker 身上。</p>
<p>正如本文开头所说，Web Worker 子线程的形式也是一种天然的沙箱隔离，理想的方式，是借鉴 <a href="https://github.com/aliyun/alibabacloud-alfa/tree/master/packages/core/browser-vm" target="_blank" rel="nofollow noopener noreferrer">Browser VM</a>  的前段思路，在编译阶段通过 Webpack 插件为每个子应用包裹一层创建 Worker 对象的代码，让子应用运行在其对应的单个 Worker 实例中，比如：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript">__WRAP_WORKER__(<span class="hljs-string">`/* 打包代码 */ &#125;`</span>);

<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">__WRAP_WORKER__</span>(<span class="hljs-params">appCode</span>) </span>&#123;
    <span class="hljs-keyword">var</span> blob = <span class="hljs-keyword">new</span> Blob([appCode]);
    <span class="hljs-keyword">var</span> appWorker = <span class="hljs-keyword">new</span> Worker(<span class="hljs-built_in">window</span>.URL.createObjectURL(blob));
&#125; 
<span class="copy-code-btn">复制代码</span></code></pre>
<p>但在了解过微前端下 JavaScript 沙箱的实现过程后，我们不难发现几个在 Web Worker 下去实现微前端场景的 JavaScript 沙箱必然会遇到的几个难题：</p>
<ol>
<li>出于线程安全设计考虑，Web Worker 不支持 DOM 操作，必须通过 postMessage 通知 UI 主线程来实现。</li>
<li>Web Worker 无法访问 window、document 之类的浏览器全局对象。</li>
</ol>
<p>其他诸如 Web Worker 无法访问页面全局变量和函数、无法调用 alert、confirm 等 BOM API 等问题，相对于无法访问 window、document 全局对象已经是小问题了。不过可喜的是，Web Worker 中可以正常使用 setTimeout、setInterval 等定时器函数，也仍能发送 ajax 请求。</p>
<p>所以，当先要解决问题，便是在单个 Web Worker 实例中执行 DOM 操作的问题了。首先我们有一个大前提：<strong>Web Worker 中无法渲染 DOM</strong>，所以，我们需要基于实际的应用场景，将 DOM 操作进行拆分。</p>
<h3 data-id="heading-3">React Worker DOM</h3>
<p>因为我们微前端架构中的子应用局限在 React 技术栈下，我先将目光放在了基于 React 框架的解决方案上。</p>
<p>在 React 中，我们知道其将渲染阶段分为对 DOM 树的改变进行 Diff 和实际渲染改变页面 DOM 两个阶段这一基本事实，那能不能将 Diff 过程置于 Web Worker 中，再将渲染阶段通过 postMessage 与主线程进行通信后放在主线程进行呢？简单一搜，颇为汗颜，已经有大佬在 5、6 年前就有尝试了。这里我们可以参考下 <a href="https://github.com/web-perf/react-worker-dom" target="_blank" rel="nofollow noopener noreferrer">react-worker-dom</a> 的开源代码。</p>
<p><a href="https://github.com/web-perf/react-worker-dom" target="_blank" rel="nofollow noopener noreferrer">react-worker-dom</a> 中的实现思路很清晰。其在 <a href="https://github.com/web-perf/react-worker-dom/blob/master/src/common/channel.js" target="_blank" rel="nofollow noopener noreferrer">common/channel.js</a> 中统一封装了子线程和主线程互相通信的接口和序列化通信数据的接口，然后我们可以看到其在 Worker 下实现 DOM 逻辑处理的总入口文件在 <a href="https://github.com/web-perf/react-worker-dom/blob/master/src/worker/index.js" target="_blank" rel="nofollow noopener noreferrer">worker 目录下</a>，从该入口文件顺藤摸瓜，可以看到其实现了计算 DOM 后通过 postMessage 通知主线程进行渲染的入口文件 <a href="https://github.com/web-perf/react-worker-dom/blob/master/src/worker/WorkerBridge.js" target="_blank" rel="nofollow noopener noreferrer">WorkerBridge.js</a> 以及其他基于 React 库实现的 DOM 构造、Diff 操作、生命周期 Mock 接口等相关代码，而接受渲染事件通信的入口文件在 <a href="https://github.com/web-perf/react-worker-dom/blob/master/src/page/index.js" target="_blank" rel="nofollow noopener noreferrer">page 目录下</a>，该入口文件接受 node 操作事件后再结合 <a href="https://github.com/web-perf/react-worker-dom/blob/master/src/page/WorkerDomNodeImpl.js" target="_blank" rel="nofollow noopener noreferrer">WorkerDomNodeImpl.js</a> 中的接口代码实现了 DOM 在主线程的实际渲染更新。</p>
<p>简单做下总结。基于 React 技术栈，通过在 Web Worker 下实现 Diff 与渲染阶段的进行分离，可以做到一定程度的 DOM 沙箱，但这不是我们想要的微前端架构下的 JavaScript 沙箱。先不谈拆分 Diff 阶段与渲染阶段的成本与收益比，首先，基于技术栈框架的特殊性所做的这诸多努力，会随着这个框架本身版本的升级存在着维护升级难以掌控的问题；其次，假如各个子应用使用的技术栈框架不同，要为这些不同的框架分别封装适配的接口，扩展性和普适性弱；最后，最为重要的一点，这种方法暂时还是没有解决 window 下资源共享的问题，或者说，只是启动了解决这个问题的第一步。</p>
<p>接下来，我们先继续探讨 Worker 下实现 DOM 操作的另外一种方案。window 下资源共享的问题我们放在其后再作讨论。</p>
<h3 data-id="heading-4">AMP WorkerDOM</h3>
<p>在我开始纠结于如 <a href="https://github.com/web-perf/react-worker-dom" target="_blank" rel="nofollow noopener noreferrer">react-worker-dom</a> 这种思路实际落地开发的诸多「天堑」问题的同时，浏览过其他 DOM 框架因为同样具备插件机制偶然迸进了我的脑海，它是 Google 的 <a href="https://amp.dev/zh_cn/" target="_blank" rel="nofollow noopener noreferrer">AMP</a>。</p>
<p><a href="https://github.com/ampproject" target="_blank" rel="nofollow noopener noreferrer">AMP 开源项目</a> 中除了如 <a href="https://github.com/ampproject/amphtml" target="_blank" rel="nofollow noopener noreferrer">amphtml</a> 这种通用的 Web 组件框架，还有很多其他工程采用了 Shadow DOM、Web Component 等新技术，在项目下简单刷了一眼后，我欣喜地看到了工程 <a href="https://github.com/ampproject/worker-dom" target="_blank" rel="nofollow noopener noreferrer">worker-dom</a>。</p>
<p>粗略翻看下 <a href="https://github.com/ampproject/worker-dom" target="_blank" rel="nofollow noopener noreferrer">worker-dom</a> 源码，我们在 src 根目录下可以看到 <a href="https://github.com/ampproject/worker-dom/tree/main/src/main-thread" target="_blank" rel="nofollow noopener noreferrer">main-thread</a> 和 <a href="https://github.com/ampproject/worker-dom/tree/main/src/worker-thread" target="_blank" rel="nofollow noopener noreferrer">worker-thread</a> 两个目录，分别打开看了下后，可以发现其实现拆分 DOM 相关逻辑和 DOM 渲染的思路和上面的  <a href="https://github.com/web-perf/react-worker-dom" target="_blank" rel="nofollow noopener noreferrer">react-worker-dom</a> 基本类似，但 <a href="https://github.com/ampproject/worker-dom" target="_blank" rel="nofollow noopener noreferrer">worker-dom</a> 因为和上层框架无关，其下的实现更为贴近 DOM 底层。</p>
<p>先看 <a href="https://github.com/ampproject/worker-dom/tree/main/src/worker-thread" target="_blank" rel="nofollow noopener noreferrer">worker-thread</a>  DOM 逻辑层的相关代码，可以看到其下的 <a href="https://github.com/ampproject/worker-dom/tree/main/src/worker-thread/dom" target="_blank" rel="nofollow noopener noreferrer">dom 目录</a> 下实现了基于 DOM 标准的所有相关的节点元素、属性接口、document 对象等代码，上一层目录中也实现了 Canvas、CSS、事件、Storage 等全局属性和方法。</p>
<p>接着看 <a href="https://github.com/ampproject/worker-dom/tree/main/src/main-thread" target="_blank" rel="nofollow noopener noreferrer">main-thread</a>，其关键功能一方面是提供加载 worker 文件从主线程渲染页面的接口，另一方面可以从 <a href="https://github.com/ampproject/worker-dom/blob/main/src/main-thread/worker.ts" target="_blank" rel="nofollow noopener noreferrer">worker.ts</a> 和 <a href="https://github.com/ampproject/worker-dom/blob/main/src/main-thread/nodes.ts" target="_blank" rel="nofollow noopener noreferrer">nodes.ts</a> 两个文件的代码来理解。</p>
<p>在 <a href="https://github.com/ampproject/worker-dom/blob/main/src/main-thread/worker.ts" target="_blank" rel="nofollow noopener noreferrer">worker.ts</a> 中像我最初所设想的那样包裹了一层代码，用于自动生成 Worker 对象，并将代码中的所有 DOM 操作都代理到模拟的 WorkerDOM 对象上：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">const</span> code = <span class="hljs-string">`
      'use strict';
      (function()&#123;
        <span class="hljs-subst">$&#123;workerDOMScript&#125;</span>
        self['window'] = self;
        var workerDOM = WorkerThread.workerDOM;
        WorkerThread.hydrate(
          workerDOM.document,
          <span class="hljs-subst">$&#123;<span class="hljs-built_in">JSON</span>.stringify(strings)&#125;</span>,
          <span class="hljs-subst">$&#123;<span class="hljs-built_in">JSON</span>.stringify(skeleton)&#125;</span>,
          <span class="hljs-subst">$&#123;<span class="hljs-built_in">JSON</span>.stringify(cssKeys)&#125;</span>,
          <span class="hljs-subst">$&#123;<span class="hljs-built_in">JSON</span>.stringify(globalEventHandlerKeys)&#125;</span>,
          [<span class="hljs-subst">$&#123;<span class="hljs-built_in">window</span>.innerWidth&#125;</span>, <span class="hljs-subst">$&#123;<span class="hljs-built_in">window</span>.innerHeight&#125;</span>],
          <span class="hljs-subst">$&#123;<span class="hljs-built_in">JSON</span>.stringify(localStorageInit)&#125;</span>,
          <span class="hljs-subst">$&#123;<span class="hljs-built_in">JSON</span>.stringify(sessionStorageInit)&#125;</span>
        );
        workerDOM.document[<span class="hljs-subst">$&#123;TransferrableKeys.observe&#125;</span>](this);
        Object.keys(workerDOM).forEach(function(k)&#123;self[k]=workerDOM[k]&#125;);
&#125;).call(self);
<span class="hljs-subst">$&#123;authorScript&#125;</span>
//# sourceURL=<span class="hljs-subst">$&#123;<span class="hljs-built_in">encodeURI</span>(config.authorURL)&#125;</span>`</span>;
<span class="hljs-built_in">this</span>[TransferrableKeys.worker] = <span class="hljs-keyword">new</span> Worker(URL.createObjectURL(<span class="hljs-keyword">new</span> Blob([code])));
<span class="copy-code-btn">复制代码</span></code></pre>
<p>在 <a href="https://github.com/ampproject/worker-dom/blob/main/src/main-thread/nodes.ts" target="_blank" rel="nofollow noopener noreferrer">nodes.ts</a>  中，实现了真实元素节点的构造和存储（基于存储数据结构是否以及如何在渲染阶段有优化还需进一步研究源码）。</p>
<p>同时，在 <a href="https://github.com/ampproject/worker-dom/tree/main/src/transfer" target="_blank" rel="nofollow noopener noreferrer">transfer</a> 目录下的源码，定义了逻辑层和 UI 渲染层的消息通信的规范。</p>
<p>总的来看，AMP WorkerDOM 的方案抛弃了上层框架的约束，通过从底层构造了 DOM 所有相关 API 的方式，真正做到了与框架技术栈无关。它一方面完全可以作为上层框架的底层实现，来支持各种上层框架的二次封装迁移（如工程 <a href="https://github.com/ampproject/amp-react-prototype" target="_blank" rel="nofollow noopener noreferrer">amp-react-prototype</a>），另一方面结合了当前主流 JavaScript 沙箱方案，通过模拟 window、document 全局方法的并代理到主线程的方式实现了部分的 JavaScript 沙箱隔离（暂时没看到路由隔离的相关代码实现）。</p>
<p>当然，从我个人角度来看，AMP WorkerDOM 也有其当前在落地上一定的局限性。一个是对当前主流上层框架如 Vue、React 等的迁移成本及社区生态的适配成本，另一个是其在单页应用下的尚未看到有相关实现方案，在大型 PC 微前端应用的支持上还无法找到更优方案。</p>
<p>其实，在了解完 AMP WorkerDOM 的实现方案之后，基于 <a href="https://github.com/web-perf/react-worker-dom" target="_blank" rel="nofollow noopener noreferrer">react-worker-dom</a> 思路的后续方案也可以有个大概方向了：渲染通信的后续过程，可考虑结合 <a href="https://github.com/aliyun/alibabacloud-alfa/tree/master/packages/core/browser-vm" target="_blank" rel="nofollow noopener noreferrer">Browser VM</a> 的相关实现，在生成 Worker 对象的同时，也生成一个 iframe 对象，然后将 DOM 下的操作都通过 postMessage 发送到主线程后，以与其绑定的 iframe 兑现来执行，同时，通过代理将具体的渲染实现再转发给原 <a href="https://github.com/web-perf/react-worker-dom/blob/master/src/page/WorkerDomNodeImpl.js" target="_blank" rel="nofollow noopener noreferrer">WorkerDomNodeImpl.js</a> 逻辑来实现 DOM 的实际更新。</p>
<h2 data-id="heading-5">小结与一些个人前瞻</h2>
<p>首先聊一聊个人的一些总结。Web Worker 下实现微前端架构下的 JavaScript 沙箱最初是出于一点个人灵光的闪现，在深入调研后，虽然最终还是因为这样那样的问题导致在方案落地上无法找到最优解从而放弃采用社区通用方案，但仍不妨碍我个人对 Web Worker 技术在实现插件类沙箱应用上的持续看好。插件机制在前端领域一直是津津乐道的一种设计，从 Webpack 编译工具到 IDE 开发工具，从 Web 应用级的实体插件到应用架构设计中插件扩展设计，结合 WebAssembly 技术，Web Worker 无疑将在插件设计上占据举足轻重的地位。</p>
<p>其次是一些个人的一些前瞻思考。其实从 Web Worker 实现 DOM 渲染的调研过程中可以看到，基于逻辑与 UI 分离的思路，前端后续的架构设计有很大机会能够产生一定的变革。目前不管是盛行的 Vue 还是 React 框架，其框架设计不论是 MVVM 还是结合 Redux 之后的 Flux，其本质上仍旧还是由 View 层驱动的框架设计（个人浅见），其具备灵活性的同时也产生着性能优化、大规模项目层级升上后的协作开发困难等问题，而基于 Web Worker 的逻辑与 UI 分离，将促使数据获取、处理、消费整个流程的进一步的业务分层，从而固化出一整套的 MVX 设计思路。</p>
<p>当然，以上这些我个人还处于初步调研的阶段，不成熟之处还需多加琢磨。且听之，后续再实践之。</p>
<blockquote>
<p>作者：ES2049 / 靳志凯</p>
</blockquote>
<blockquote>
<p>文章可随意转载，但请保留此原文链接。</p>
<p>非常欢迎有激情的你加入 <a href="https://es2049.studio/" target="_blank" rel="nofollow noopener noreferrer">ES2049 Studio</a>，简历请发送至 <a href="mailto:caijun.hcj@alibaba-inc.com">caijun.hcj@alibaba-inc.com</a> 。</p>
</blockquote></div> <div class="image-viewer-box" data-v-78c9b824><!----></div>  
</div>
            