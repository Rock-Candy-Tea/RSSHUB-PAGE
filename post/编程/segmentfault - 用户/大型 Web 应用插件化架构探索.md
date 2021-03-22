
---
title: 大型 Web 应用插件化架构探索
categories: 
    - 编程
    - segmentfault - 用户
author: segmentfault - 用户
comments: false
date: 2021-03-22 03:14:56
thumbnail: 'https://segmentfault.com/img/remote/1460000039652040'
---

<div>   
<blockquote>简介： 随着 Web 技术的逐渐成熟，越来越多的应用架构趋向于复杂，例如阿里云等巨型控制台项目，每个产品下都有各自的团队来负责维护和迭代。不论是维护还是发布以及管控成本都随着业务体量的增长而逐渐不可控。在这个背景下微前端应用而生，微前端在阿里内部已经有许多成熟的实践，这里不再赘述。本文以微前端为引子(蹭热度)，探讨一些另类的 Web 应用所面临的类似问题。</blockquote><p><span class="img-wrap"><img class="lazy" src="https://segmentfault.com/img/remote/1460000039652040" alt title referrerpolicy="no-referrer"></span></p><h1>前言</h1><p>随着 Web 技术的逐渐成熟，越来越多的应用架构趋向于复杂，例如阿里云等巨型控制台项目，每个产品下都有各自的团队来负责维护和迭代。不论是维护还是发布以及管控成本都随着业务体量的增长而逐渐不可控。在这个背景下<strong>微前端</strong>应用而生，微前端在阿里内部已经有许多成熟的实践，这里不再赘述。本文以微前端为引子，探讨一些另类的 Web 应用所面临的类似问题。</p><h1>现代文本编辑器沉浮</h1><p>2018年微软 GitHub 后，<strong>Atom</strong>便经常被拿来调侃，所谓一山不容二虎。在 VS Code 已经成为一众前端工程师编辑器首选的当下，Atom 的地位显得很尴尬，论性能被同为 Electron 的 VS Code 秒杀，论插件，VS Code 去年插件总数就已经突破 1w 大关，而早发布一年多的 Atom 至今还停留在 8k +。再加上微软官方主导的 LSP/DAP 等重量级协议的普及，时至今日 Atom 作为曾经 Web/Electron 技术标杆应用的地位早已被 VS Code 斩落马下。</p><p><span class="img-wrap"><img class="lazy" src="https://segmentfault.com/img/remote/1460000039652044" alt title referrerpolicy="no-referrer"></span></p><p>网上关于 Atom 的日渐衰落的讨论，始终离不开性能。Atom 的确太慢了，究其原因很大程度上是被其插件架构所拖累的。尤其是 Atom 在 UI 层面开放过多的权限给插件开发者定制，插件质量良萎不齐以及 UI 完全开放给插件后带来的安全隐患都成为 Atom 的阿喀琉斯之踵。甚至其主界面的 FileTree、Tab 栏、Setting Views 等重要组件都是通过插件实现的。相比之下 VS Code 则封闭很多，VS Code 插件完全运行在 Node.js 端，对于 UI 的定制性只有极个别被封装为纯方法调用的 API。</p><p><span class="img-wrap"><img class="lazy" src="https://segmentfault.com/img/remote/1460000039652043" alt title referrerpolicy="no-referrer"></span></p><p>但另一方面，VS Code 这种相对封闭的插件 UI 方案，一些需要更强定制性的功能便无法满足，更多插件开发者开始魔改 VS Code 底层甚至源码来实现定制。例如社区很火的 VS Code Background，这款插件通过强行修改 VS Code 安装文件中的 CSS 来实现编辑器区域的背景图。而另一款 VSC Netease Music 则更激进，因为 VS Code 捆绑包中的 Electron 剔除了 FFmpeg 导致在 Webview 视图下无法播放音视频，使用此插件需要自行替换 FFmpeg 的动态链接库。而这些插件不免会对 VS Code 安装包造成一定程度的破坏，导致用户需要卸载重装。</p><h1>不止编辑器 - 飞个马</h1><p>Figma 是一个在线协作式 UI 设计工具， 相比 Sketch 它具有跨平台、实时协作等优点，近年来逐渐受到 UI 设计师们的青睐。而近期 Figma 也正式上线了其插件系统。</p><p><span class="img-wrap"><img class="lazy" src="https://segmentfault.com/img/remote/1460000039652039" alt title referrerpolicy="no-referrer"></span></p><p>作为一个 Web 应用，Figma 的插件系统自然也是基于 JavaScript 构建的，这一定程度上降低了开发门槛。自去年6月份 Figma 官方宣布开放插件系统测试以来，已经有越来越多的 Designner/Developer 开发了300+ 插件，其中包括图形资源、文件归档、甚至是导入 3D 模型等。</p><p><span class="img-wrap"><img class="lazy" src="https://segmentfault.com/img/remote/1460000039652038" alt title referrerpolicy="no-referrer"></span></p><h1>Figma 的插件系统是如何工作的？</h1><p>这是一个基于 TypeScript + React 技术栈，使用 Webpack 构建的 Figma 插件目录结构</p><pre><code>.
├── README.md
├── figma.d.ts
├── manifest.json
├── package-lock.json
├── package.json
├── src
│   ├── code.ts
│   ├── logo.svg
│   ├── ui.css
│   ├── ui.html
│   └── ui.tsx
├── tsconfig.json
└── webpack.config.js</code></pre><p>在其 manifest.json 文件中包含了一些简单的信息。</p><pre><code>&#123;
  "name": "React Sample",
  "id": "738168449509241862",
  "api": "1.0.0",
  "main": "dist/code.js",
  "ui": "dist/ui.html"
&#125;</code></pre><p>可以看出 Figma 将插件入口分为了 main 与 ui 两部分， main 中包含了插件实际运行时的逻辑，而 ui 则是一个插件的 HTML 片段。即 UI 与逻辑分离。安装一个Color Search 插件后观察页面结构可以发现 main 中的 js 文件被包裹在一个 iframe 里加载到页面上，关于 main 入口的沙箱机制后文中有详细的阐述。而 ui 中的 HTML 最终也被包裹在一个 iframe 里渲染出来，这将有效的避免插件 UI 层 CSS 代码导致全局样式污染。</p><p><span class="img-wrap"><img class="lazy" src="https://segmentfault.com/img/remote/1460000039652041" alt title referrerpolicy="no-referrer"></span></p><p>Figma Developers 文档中 有一章节 <strong>How Plugins Run</strong> 对其插件系统运行机制进行了简单的介绍，简单来说 Figma 为插件中逻辑层的 main 入口创建了一个最小的 JavaScript 执行环境，它运行在浏览器主线程上，在这个执行环境中插件代码无法访问到一些浏览器全局的 API，从而也就无法在代码层面对 Figma 本身运行造成影响。而 UI 层有且仅有一份 HTML 代码片段，在插件被激活后被渲染到一个弹窗中。</p><p><span class="img-wrap"><img class="lazy" src="https://segmentfault.com/img/remote/1460000039652048" alt title referrerpolicy="no-referrer"></span></p><p>Figma 官方博客中对其插件的沙箱机制做了详细的阐述。起初他们尝试的方案是 iframe，一个浏览器自带的沙箱环境。将插件代码由 iframe 包裹起来，由于 iframe 天然的限制，这将确保插件代码无法操作 Figma 主界面上下文，同时也可以只开放一份白名单 API 供插件调用。乍一看似乎解决了问题，但由于 iframe 中的插件脚本只能通过 postMessage 与主线程通信，这导致插件中的任何 API 调用都必须被包装为一个异步 async/await 的方法，这无疑对 Figma 的目标用户<strong>非专业前端开发者的设计师</strong>不够友好。其次对于较大的文档，postMessage 通信序列化的性能成本过高，甚至会导致内存泄漏。</p><p>Figma 团队选择回到浏览器主线程，但直接将第三方代码运行在主线程，由此引发的安全问题是不可避免的。最终他们发现了一个尚在 stage2 阶段的草案 Realm API。Realm 旨在创建一个领域对象，用于隔离第三方 JavaScript 作用域的 API。</p><pre><code>let g = window; // outer global
let r = new Realm(); // root realm

let f = r.evaluate("(function() &#123; return 17 &#125;)");

f() === 17 // true

Reflect.getPrototypeOf(f) === g.Function.prototype // false
Reflect.getPrototypeOf(f) === r.globalThis.Function.prototype // true</code></pre><p>值得注意的是，Realm 同样可以使用 JavaScript 目前已有的特性来实现，即 with 与 Proxy。这也是目前社区比较流行的沙箱方案。</p><pre><code>const whitelist = &#123;
  windiw: undefined,
  document: undefined,
  console: window.console,
&#125;;

const scopeProxy = new Proxy(whitelist, &#123;
  get(target, prop) &#123;
    if (prop in target) &#123;
      return target[prop]
    &#125;
    return undefined
  &#125;
&#125;);

with (scopeProxy) &#123;
  eval("console.log(document.write)") // Cannot read property 'write' of undefined!
  eval("console.log('hello')")        // hello
&#125;</code></pre><p>前文中 Figma 插件被 iframe 所包裹的插件 main 入口即包含了一个被 Realm 接管的作用域，你可以认为是类似这段示例代码中的一份 白名单 API，毕竟维护一份白名单比屏蔽黑名单实现起来更简洁。但事实上由于 JavaScript 的原型式继承，插件仍然可以通过 console.log 方法的原型链访问到外部对象，理想的解决方案是将这些白名单 API 在 Realm 上下文中包装一次，从而彻底隔离原型链。</p><pre><code>const safeLogFactory = realm.evaluate(`
  (function safeLogFactory(unsafeLog) &#123; 
    return function safeLog(...args) &#123;
      unsafeLog(...args);
    &#125;
  &#125;)
`);

const safeLog = safeLogFactory(console.log);

const outerIntrinsics = safeLog instanceOf Function;
const innerIntrinsics = realm.evaluate(`log instanceOf Function`, &#123; log: safeLog &#125;);
if (outerIntrinsics || !innerIntrinsics) throw new TypeError(); 

realm.evaluate(`log("Hello outside world!")`, &#123; log: safeLog &#125;);</code></pre><p><span class="img-wrap"><img class="lazy" src="https://segmentfault.com/img/remote/1460000039652046" alt title referrerpolicy="no-referrer"></span></p><p>显然为每一个白名单中的 API 做这样操作的工作是非常繁杂且容易出错的。那么如何构建一个安全且易于添加 API 的沙箱环境呢？</p><p>Duktape 是一个由 C++ 实现的用于嵌入式设备的 JavaScript 解释器，它不支持任何浏览器 API，自然地它可以被编译到 WebAssembly，Figma 团队将 Duktape 嵌入到 Realm 上下文中，插件最终通过 Duktape 解释执行。这样可以安全的实现插件所需 API，且不用担心插件会通过原型链访问到沙箱外部。</p><p><span class="img-wrap"><img class="lazy" src="https://segmentfault.com/img/remote/1460000039652042" alt title referrerpolicy="no-referrer"></span></p><p>这是一种被称为 Membrane Pattern 的防御性的编程模式，用于在程序中与子组件(广义上)实现一层中介。简单来说就是代理(Proxy)，为一个对象创建一个可控的访问边界，使得它可以保留一部分特性给第三方嵌入脚本，而屏蔽一部分不希望被访问到的特性。关于 Membrane 的详细论述可以查看 Isolating application sub-components with membranes 与 Membranes in JavaScript 这两篇文章。</p><p><span class="img-wrap"><img class="lazy" src="https://segmentfault.com/img/remote/1460000039652047" alt title referrerpolicy="no-referrer"></span></p><p>这是最终 Figma 的插件方案，它运行在主线程，不需要担心 postMessage 通信带来的传输损耗。多了一次 Duktape 解释执行的消耗，但得益于 WebAssembly 出色的性能，这部分消耗并不是很大。</p><p>另外 Figma 还保留了最初的 iframe ，允许插件可以自行创建 iframe ，并在其中插入任意 JavaScript ，同时它可以与沙箱中的 JavaScript 脚本通过 postMessage 相互通信。</p><h1>鱼和熊掌如何兼得？</h1><p>我们把这类插件的需求总结为<strong>在 Web 应用中运行第三方代码及其自定义控件</strong>，它有与开头提到的<strong>微前端</strong>架构非常相似的一些问题。</p><ol><li>一定程度上的 JavaScript 代码沙箱隔离机制，应用主体对第三方代码(或子应用)有一定的管控能力</li><li>样式强隔离，第三方代码样式不对应用主体产生 CSS 污染</li></ol><h1>JavaScript 沙箱</h1><p>JavaScript 沙箱隔离在社区是个经久不衰的话题，最简单的 iframe 标签 Sandbox 属性就已经能做到 JavaScript 运行时的隔离，社区较为流行的是利用一些语言特性(with、realm、Proxy 等 API )屏蔽(或代理) Window、Document 等全局对象，建立白名单机制，对可能潜在危险操作的 API 重写(如阿里云 Console OS - Browser VM)。另外还有 Figma 这种尝试嵌入平台无关的 JavaScript 解释器，所有第三方代码都通过嵌入的解释器来执行。以及利用 Web Worker 做 DOM Diff 计算，并将计算结果发送回 UI 线程来进行渲染，这个方案早在 2013 年就已经有人进行了实践，这篇论文中作者将 JSDOM 这一 Node.js 平台广泛流行的测试库运行在 Web Worker。而近些年来也有 preact-worker-demo 、react-worker-dom 等项目基于 Web Worker 的 DOM Renderer 尝试将 DOM API 代理到 Worker 线程。而 Google AMP Project 在JSCONF 2018 US 对外公布的 worker-dom 则将 DOM API 在 Web Worker 端实现了 DOM API，虽然实践下来还存在一些问题（例如同步方法无法模拟），但 WorkerDOM 在性能和隔离性上都取得了一定成果。</p><p><span class="img-wrap"><img class="lazy" src="https://segmentfault.com/img/remote/1460000039652049" alt title referrerpolicy="no-referrer"></span></p><p>以上这些解决方案被广泛的应用在各种插件化架构的 Web 应用中，但大多都是 Case By Case，每种解决方案都有各自的成本与取舍。</p><h1>CSS 作用域</h1><p>CSS 样式隔离方案中，如上文中 Figma 使用 iframe 渲染插件界面，牺牲一部分性能换来了相对完美的样式隔离。而在现代前端工程化体系下，可以通过 CSS Module 在转译时对 class 添加 hash 或 namespace 等方式实现，这类方案较为依赖插件代码编译过程。而更新潮的是利用 Web Component 的 Shadow DOM，将插件元素用 Web Component 包裹起来，Shadow Root 外部样式无法作用于内部，同样 Shadow Root 内部的样式也无法影响到外部。</p><p><span class="img-wrap"><img class="lazy" src="https://segmentfault.com/img/remote/1460000039652045" alt title referrerpolicy="no-referrer"></span></p><h1>最后</h1><p>本文列举了目前编辑器、设计工具这类大型 Web 应用插件化架构下所面临的的一些问题，以及社区实践的解决方案。不论是让人又爱又恨的 iframe ，还是 Realm、Web Worker 、 Shadow DOM 等，目前来说每种方案都有各自的优势与不足。但随着 Web 应用的复杂度增长，插件化这一需求也逐渐被各大标准化组织所重视起来。下一篇将着重介绍 KAITIAN IDE 中插件架构的探索与实践，包括 JavaScript 沙箱、CSS 隔离、Web Worker 等。</p><p>作者：开发者小助手_LS<br><a href="https://developer.aliyun.com/article/782744?utm_content=g_1000252784" rel="nofollow">原文链接</a><br>本文为阿里云原创内容，未经允许不得转载</p>  
</div>
            