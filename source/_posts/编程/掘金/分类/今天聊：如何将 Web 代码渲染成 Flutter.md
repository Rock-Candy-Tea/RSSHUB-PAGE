
---
title: '今天聊：如何将 Web 代码渲染成 Flutter'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/ef9e1525937d4d3daaf051d5ce4d46d0~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Wed, 26 May 2021 15:04:38 GMT
thumbnail: 'https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/ef9e1525937d4d3daaf051d5ce4d46d0~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>@charset "UTF-8";.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:14px;overflow-x:hidden;color:#353535&#125;.markdown-body h1&#123;padding-bottom:4px;font-size:30px&#125;.markdown-body h1,.markdown-body h2&#123;margin-top:36px;margin-bottom:10px;line-height:1.5;color:#005bb7&#125;.markdown-body h2&#123;position:relative;padding-left:16px;padding-right:10px;padding-bottom:10px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h2:before&#123;content:"「";position:absolute;top:-6px;left:-10px&#125;.markdown-body h2:after&#123;content:"」";position:absolute;top:6px;right:auto&#125;.markdown-body h3&#123;position:relative;padding-bottom:0;margin-top:30px;margin-bottom:10px;font-size:20px;line-height:1.5;color:#005bb7;padding-left:6px&#125;.markdown-body h3:before&#123;content:"»";padding-right:6px;color:#2196f3&#125;.markdown-body h4&#123;margin-top:24px;font-size:16px&#125;.markdown-body h4,.markdown-body h5&#123;padding-bottom:0;margin-bottom:10px;line-height:1.5;color:#005bb7;padding-left:6px&#125;.markdown-body h5&#123;margin-top:18px;font-size:14px&#125;.markdown-body h6&#123;padding-bottom:0;margin-top:12px;margin-bottom:10px;font-size:12px;line-height:1.5;color:#005bb7;padding-left:6px&#125;.markdown-body p&#123;line-height:inherit;margin-top:16px;margin-bottom:16px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;position:relative;width:98%;height:1px;margin-top:32px;margin-bottom:32px;background-image:linear-gradient(90deg,#007fff,rgba(255,0,0,.3),hsla(0,0%,100%,.1),rgba(255,0,0,.3),#007fff);border-width:0;overflow:visible&#125;.markdown-body hr:after&#123;content:"";position:absolute;margin:auto;left:0;right:0;bottom:0;top:0;display:inline-block;width:60px;height:20px;background:#fff;background-image:url(data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACgAAAAgCAYAAABgrToAAAADoklEQVRYR82XTYgcRRTHf2933Q1RjAa9eFO8JHoJ8RQVBQ2iBwXBET0YEUTXNVmNQtTpmeqaWV0XNRq/o4KoECSCEPSg4CF+BYUkIIiCoCJCPIhC/Ihh2Z0nVV27VnZnenumW9i6ddV7//frV69fVQurfMgq56NawFTPAU6QyomqXrw6wIZeyhCPebA5buNR+akKyGoAjd6BshthnYdSjqNcRVuOlIUsD2j0SuA94IwuMHdh5ZUykOUBXfSGbmKI54EtAeYIHSZoy5dl4JxvNYBOKdW1KE8BQ8AkVk6WhasWsAiN0TX9gveXQaPP+Aytpc4u+bMI06JNohsYYYYOR2lJWtS3OKDRfcAtQfgDoI6Vo4UCGb0OmAEuDvZvYmVbEd/igC3dzDz7gQu8sPA9kJDK27mBmjqBeLjTg90PDFOjWawFFQd06kZHEfaj3LAIpTRpSXsZ5E06zEYP9sDimnAApYaV2SLZG/wjMeqAkijwW4xQJ5Gf/ZzRC8OW3hiBTGGlURRswW55Bh/Ssxljrwew8l1PQaM14GngvGDzBUKdDsMeTtgU5o8B92PFlUf3YXUrHa7Fys6lBqcCGnX15YQ2A18FyPd7Crd1A3M8C1wdbH4DD3hWeP6IEXbQkG97ajR1HPFnuPP5jFFq1OWX7hl8WM9l1AO648uNfwLk7tytMeogty+xeQ4rO3r6bdcx1nuwOGsHmaXGtPzae4uzGnLH1kQkvpdZGrHjssBZJrL+pqS05KWc8tgITAPXRzYvYOXe/C2OV43eDcRBDtIhoS2f9wzc0Cv8Wls+zoFzUC5zF0U241h5uZtPfptp6OUM8wbK+cH5GEpCS17P3fJei0Z3+npTxryJ8CPzbKMtn/ZyWbkPGl0PuFPkmkjkcb4h4R2ZLwRq1H0ALmvjkf2HwK1Y+T1PY2XABe/sHJ6MxN5lnoSpnC/UGbsTaI5phK2R7x6s3Ffk5YoDOrWm3onwJHBmEP86bPmBrsGaenNoIdnxCH+gPEhLXi0Cl1VBvyPVLSh7gEuC62yAfOIUqabWEaaiucMIk6RyqJ+Q/QM69V26jjW86Gvov/EaoyT8zRCn+Xq7PVrbx0nuYUaO9wM3WAbjCE1NEUw09Um4UV+2OKfYfu5/S19gsAzGKqm6LE5FrShbdS0ku465DjDwKA/oQht19ejqbaEVuRbiLhuHByYLjtUAZpDutzP7cYdHsPJXWbjyNVgFwQoa1WXwf4Jd9YD/Ap80+yE7+u9aAAAAAElFTkSuQmCC);background-repeat:no-repeat;background-size:auto 100%;background-position-x:center&#125;.markdown-body code&#123;padding:.065em .4em;font-size:.87em;color:#c2185b;word-break:break-word;overflow-x:auto;background-color:#fff4f4;border-radius:2px&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;display:block;padding:16px 12px;margin:0;font-size:12px;color:#333;word-break:normal;overflow-x:auto;background:#f8f8f8&#125;.markdown-body pre>code::-webkit-scrollbar&#123;width:4px;height:4px&#125;.markdown-body pre>code::-webkit-scrollbar-track&#123;background-color:#bedcff&#125;.markdown-body pre>code::-webkit-scrollbar-thumb&#123;background-color:#2196f3;border-radius:10px&#125;.markdown-body a&#123;position:relative;text-decoration:none;color:#3da8f5;border-bottom:1px solid #bedcff&#125;.markdown-body a:hover&#123;color:#007fff;border-bottom-color:#007fff&#125;.markdown-body a:active&#123;color:#007fff&#125;.markdown-body a:after&#123;position:absolute;content:"";top:100%;left:0;width:100%;opacity:0;border-bottom:1px solid #bedcff;transition:top .3s,opacity .3s;transform:translateZ(0)&#125;.markdown-body a:hover:after&#123;top:0;opacity:1;border-bottom-color:#007fff&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #c3e0fd;border-spacing:0;border-collapse:collapse&#125;.markdown-body table thead&#123;color:#000;text-align:left;font-size:14px;background:#f6f6f6&#125;.markdown-body table tr:nth-child(2n)&#123;background-color:#f7fbff&#125;.markdown-body table tr:hover&#123;background-color:#e0edf7&#125;.markdown-body table td,.markdown-body table th&#123;padding:12px 8px;line-height:24px;border:1px solid #c3e0fd&#125;.markdown-body table th&#123;color:#005bb7;background-color:#dff0ff&#125;.markdown-body table td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#8c8c8c;border-left:4px solid #2196f3;background-color:#f0fdff;padding:1px 20px;margin:22px 0&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body b,.markdown-body blockquote>b,.markdown-body blockquote>strong,.markdown-body strong&#123;color:#2196f3&#125;.markdown-body em,.markdown-body i&#123;color:#4fc3f7&#125;.markdown-body del&#123;color:#ccc&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:4px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body details>summary&#123;outline:none;color:#005bb7;font-size:20px;font-weight:bolder;border-bottom:1px solid #bedcff;cursor:pointer&#125;.markdown-body details>p&#123;padding:10px 20px;margin:10px 0 0;color:#666;background-color:#f0fdff;border:2px dashed #2196f3&#125;.markdown-body h1::selection,.markdown-body h2::selection,.markdown-body h3::selection,.markdown-body h4::selection,.markdown-body h5::selection,.markdown-body h6::selection&#123;color:#005bb7;background-color:rgba(160,200,255,.15)&#125;.markdown-body p::selection&#123;color:#c80000&#125;.markdown-body a::selection,.markdown-body b::selection,.markdown-body del::selection,.markdown-body em::selection,.markdown-body i::selection,.markdown-body strong::selection&#123;background-color:transparent&#125;.markdown-body code::selection&#123;background-color:#ffeaeb&#125;.markdown-body pre>code::selection&#123;background-color:rgba(160,200,255,.25)&#125;.markdown-body ol ::selection,.markdown-body ul ::selection&#123;background-color:rgba(160,200,255,.15)&#125;.markdown-body .contains-task-list&#123;padding-left:14px;list-style:none&#125;.markdown-body .contains-task-list input[type=checkbox]&#123;position:relative&#125;.markdown-body .contains-task-list input[type=checkbox]:before&#123;content:"";position:absolute;top:0;left:0;right:0;bottom:0;width:inherit;height:inherit;background:#f0f8ff;border:1px solid #add6ff;border-radius:2px;box-sizing:border-box;z-index:1&#125;.markdown-body .contains-task-list input[type=checkbox]:checked:after&#123;content:"✓";position:absolute;top:-12px;left:0;right:0;bottom:0;width:0;height:0;color:#f55;font-size:20px;font-weight:700;z-index:2&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>前端早早聊大会，与掘金联合举办。加 codingdreamer 进大会技术群，赢在新的起跑线。</p>
<hr>
<p>第二十七届|前端 Flutter 专场，了解 Web 渲染引擎|UI 框架|性能优化，6-5 下午直播，6 位讲师(淘宝/京东/闲鱼等)，<a href="https://www.huodongxing.com/go/tl27" target="_blank" rel="nofollow noopener noreferrer">点我上车👉 (报名地址)：</a></p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/ef9e1525937d4d3daaf051d5ce4d46d0~tplv-k3u1fbpfcp-watermark.image" alt="大会海报.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>所有往期都有全程录播，<strong><a href="https://www.huodongxing.com/go/2021" target="_blank" rel="nofollow noopener noreferrer">上手年票一次性解锁全部</a></strong></p>
<hr>
<h2 data-id="heading-0">正文如下</h2>
<blockquote>
<p>本文是第十七届 - 前端早早聊框架专场，也是早早聊第 117 场，来自飞猪-南麓 的分享</p>
</blockquote>
<h2 data-id="heading-1">前言</h2>
<p>当前，前端技术日新月异，仅看移动端上的渲染方案。从早期的 H5 Wap，到借助客户端能力通过离线包、prefetch、JSBridge 提升性能和扩展功能的 Hybrid 方案，再到前几年大火的以 Weex/ReactNative 为代表的的大前端融合渲染方案，以及最近几年各大厂商陆续推出的商业价值大于技术价值的小程序方案。前端技术的选型已由纯粹的性能追求，演变到性能与效能、甚至业务价值的博弈，而每个新技术的诞生，也都有其背后的场景价值。</p>
<p>本文作者将就 Flutter 这一新的客户端渲染方案和读者分享一下对下一代高性能前端渲染思路 Web On Flutter 的思考。看看 Flutter 之于 Web 能碰撞出什么样的火花。</p>
<h2 data-id="heading-2">初识 Flutter</h2>
<p>这里先给不太了解 Flutter 的读者做一下简单介绍：Flutter 是由 Google 于2017年推出并开源的一个移动应用开发框架。其一大特点是基于 Skia 实现了一套自绘引擎，可以同时运行在移动端、 IOT 等多种平台。Flutter 使用 Dart 开发，Dart 语言的一个特点是既支持 JIT（即时编译）又支持 AOT（提前编译），如此便可在开发阶段采用 JIT 模式进行高效开发，同时在发布阶段享受 AOT 模式的高性能。</p>
<p>作为 Google 出品的拳头级产品，Flutter 一经推出便大受欢迎，目前在 Github 中有超过 10W的 star，平均每月1.8次（2020年数据）的 Stable 版本迭代也足见维护力度。此外，Flutter 也备受大厂青睐，阿里、腾讯、字节、美团等都在开展相关布局建设，而在阿里内部，也有淘宝、闲鱼、飞猪、盒马等多个 BU 落地了实际业务。</p>
<h4 data-id="heading-3">Flutter 的优势</h4>
<p>那么是什么原因让 Flutter 如此受追捧呢，我们对比一下当前移动端主流的渲染方案：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/a2c1b67e8a044560a1e352214a7c08da~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>可以看到 Flutter 兼具 Native 的高性能和 WebView 的低开发成本，同时又因为自绘而具备极佳的渲染一致性，因此也就不难解释为何大家都对 Flutter 抱有如此大的想象和期待。</p>
<h4 data-id="heading-4">Flutter 的技术特点</h4>
<p>我们再简单介绍一下 Flutter 的技术特点：</p>
<ul>
<li><strong>自绘引擎</strong></li>
</ul>
<p>Flutter 基于 Skia 这一跨平台图形库自建了一套渲染管线，而不是使用系统（Android、iOS）的原生控件或者 WebView 的渲染管线。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/27e8ec949acc469a8cd690efc3682cfe~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>自绘带来的好处显而易见，根本上解决了跨端一致性问题（这里可以对比 Weex，Weex 是将渲染一致性问题转移到容器层解决，但这也导致了容器的愈加难以维护）。</p>
<ul>
<li><strong>响应式框架</strong></li>
</ul>
<p>前面提到 Flutter 本质是一个开发框架，而从开发模式上说，它是一个响应式框架，这也是 Flutter 开发高效的一个原因（这里我们暂且忘记它的组件地狱嵌套吧~）。我们看个示例，一个简单的“数字增加”组件，在 Flutter 里可以这么实现：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/196bf412323645d782c08c7b69d34142~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>对于前端同学来说是否有种熟悉感，没错，这个写法和 JSX 非常相似！包括组件嵌套和状态更新。</p>
<ul>
<li><strong>一切皆widgets</strong></li>
</ul>
<p>“Widget 是 Flutter 应用程序用户界面的基本构建块。每个 Widget 都是用户界面一部分的不可变声明。与其他将视图、控制器、布局和其他属性分离的框架不同，Flutter 具有一致的统一对象模型：Widget。”上面这段是 Flutter 官网的原话，翻译到前端语境，Widget 既可以是 div、span 这种结构组件，也可以是 padding、opacity 这种样式组件，同时也可以是 dialog 这种功能组件......</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/139078022dbf4997b8d21ffe69ab19cc~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>而这些 Widgets 会根据布局形成一个层次结构，也就是一棵 Widgets 树，这点读者可以先留个印象，在后面的介绍中会有用到。</p>
<h2 data-id="heading-5">Flutter 与 Web</h2>
<p>前文中，我们对 Flutter 有了初步了解，也简单对比了它和其他主流移动端渲染方案的优劣势。在本节中，我们将重点看一下 Flutter 对 Web（或者说前端）的冲击，及可能碰撞的火花。</p>
<h4 data-id="heading-6">Flutter 对前端的冲击与结合</h4>
<p>一直以来，前端相较于客户端，比较大的优势体现在以下4个方面：</p>
<ul>
<li>人力成本： 1 vs 2（iOS + Android）</li>
<li>开发效率：JIT vs AOT</li>
<li>投放场景：跨端 vs 单端</li>
<li>迭代频次：随时 vs 发版</li>
</ul>
<p>但是与 Flutter 相比，前端的“人力成本”和“开放效率”优势将极大减弱，不过依然保留着跨端投放和高频迭代的优势，那么我们是否可以将二者的优势结合起来呢？答案便是 Web On Flutter。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/6cd8534bc58a41eba538fd614e60dada~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<h4 data-id="heading-7">Web On Flutter 技术思路</h4>
<p>既然是以 Web 的方式开发，用 Flutter 引擎渲染，那就意味着渲染流程的前半段是 Web，而后半段是 Flutter。如何桥接二者的渲染管线便成了破题的重点，这里可以有3个切入点：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/d1fe59e46576405e8acabf2b12212ed9~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<ul>
<li>切入点A：用 Web 的 DOM 模拟 Flutter 的 Widget。这个方案对前端开发有很强的约束，需要遵循 Flutter 的组件思维来开发页面。目前社区里的 MXFlutter 便是这个思路。</li>
<li>切入点B：用 Flutter 的 Widget 模拟 Web 的 DOM。这个方案的难点在于精准的样式映射，比较适合限定（W3C标准子集）的前端场景。目前飞猪的 Flugy 方案采用的正是这个思路。</li>
<li>切入点C：将 Web 的 DOM 树直接映射到 Flutter 的 RenderObject 树上。这个方案的好处是，相比和 Widgets 树的桥接，将 DOM 树直接桥接到 RenderObject 树可以更细力度的操作，理论上样式还原的上限会更高点。但因其是在 Flutter 内部的 RenderObject 上进行了扩展，所以也会对 Flutter 版本有更大的敏感度。目前手淘的 Kraken 便是这个思路。</li>
<li>切入点C Plus：这个切入点在图中没有表现，其实是对 Flutter 的更深入改造，既重写 Flutter Rendering 层，好处是不用担心 DOM 树和 RenderObject 树的不对齐，但相应的开发成本也是巨大的。目前手淘的 Unicorn 在尝试这方面的探索。</li>
</ul>
<p>通过下图，读者可以进一步理解这 4 种思路的区别：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/4836a237d796469c88971414a7975edb~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<h4 data-id="heading-8">Web On Flutter 实现原理</h4>
<p>本节将以 Widget 模拟 DOM 的思路为例，分析一下可行的实现原理。我们先通览一下该思路下的整体渲染链路：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/dcee6b2cbdc34eb5bc12f4e099dd635f~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>前面提到整条链路的关键点就是将 Web 渲染链路和 Flutter 渲染链路桥接起来，那桥接的第一步就是可以双向通信，这里涉及的关键技术点就是 JS Binding；而后就是用 Widget 来模拟 DOM，生成最后用来绘制的 Widgets 树，这里需要关注的技术关键点包括 <strong>DOM 树映射及 CSS 样式映射</strong> ；同时我们也需要关注到如何进行事件绑定。接下来我就以上述 4 个技术关键点分别进行介绍。</p>
<ul>
<li><strong>JS Binding</strong></li>
</ul>
<p>在 WebView 中，我们常采用重写 Alert / Prompt、拦截 URL 或 API 注入等方案来进行 JS 和 Native 的通信。在 Web On Flutter 中，JS 和 Flutter 的通信也可以采用类似 API 注入的方案。也就是 Flutter 通过 JS 引擎 向 JS 全局上下文挂载变量，比如一个 function，而后 JS 便可以通过该 function 调到 Flutter 的方法，反过来，Flutter 也可以直接通过 JS 引擎访问到 JS 全局上下文中的变量。如此双向通信便可建立起来，下面用张图来直观的展示一下这个过程：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/c0fba43fbd1c4db889207839e1130bb6~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>这里扩展补充一下上图的 C++ 胶水层的含义。Dart 代码可以通过 dart:ffi<a href="https://flutter.cn/docs/development/platform-integration/c-interop" target="_blank" rel="nofollow noopener noreferrer"> </a>库来调用本地的 C API，但 JS 引擎又只能被 C++ 调用，所以我们需要编写一层 C++ 胶水层来封装所需使用的 JS 引擎 API，再通过 extern C 标记来编译成 C 产物给到 Dart 来调用。</p>
<p>再进一步分析整条通信链路，可以看到一大瓶颈是跨语言通信（JS <=> C/C++ <=> Dart），作者曾做过实验，JS 无参调 Dart 单次耗时在 0.05ms 左右，Dart 无参调 JS 则需要 0.08ms 左右，只看单次确实很快，但是考虑到一个真实的页面的渲染指令数可能在 1000 量级，并且携带大量参数，所以最终耗时会很容易超过 100ms，所以我们还需要进一步优化，可行的方案如缓存渲染指令进行批量调用等，这里就不做展开了。</p>
<ul>
<li><strong>DOM 树映射</strong></li>
</ul>
<p>我们再来看一下 Web 中的 DOM 树如何转成 Flutter 中的 Widgets 树。我们知道 Dom 树在前端是通过createElement、appendChild 等 DOM API 来进行创建的，整个创建过程实质就是一条条渲染指令。</p>
<p>对于createElement 指令，Flutter 在接收到后，会根据所要创建的 Element 的特性，用多个 Widget 组合出来。比如 body 元素，最外层需要一个 Container Widget 来包裹以便设置一些通用样式，body 的子节点是纵向排布的，所以还需要一个 Column Widget，最后考虑到它是可滚动的，还需要一个SingleChildScrollView 来支持。注意这里模拟 body 的 Widgets 组合只是简单示例一下，实际实现要考虑到多种情况会复杂的多。</p>
<p>对于 appendChild 指令，还记得前面提到 Flutter 是响应式框架吗，我们可以类比在 React 中增删组件，用 setState 的方式来维护一个节点的子节点。</p>
<p>整体的流程可以参看下图：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/8259cd78b3ec4a0eb64491d69126517e~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<ul>
<li><strong>CSS 样式映射</strong></li>
</ul>
<p>在完成 DOM 树到 Widgets 树转换之后，我们需要考虑如何将 CSS 样式在 Flutter 中还原，还记得前面提到的渲染指令吗，除了告知 Flutter 需要创建什么类型的 Element，它还会携带这个元素的属性，其中就包括了样式（通过 Webpack 等工具将 CSS 转成内联样式）。我们所需要做的就是将这些样式用一个或多个 Wdiget 来还原实现，这里我们举两个例子，一个是绝对定位，一个是底部对齐（比如价格和￥符）：</p>
<p>Flutter 提供了一个 Stack Widget，允许子组件堆叠，而 Positioned Widget 可以根据 Stack 的四个角来确定自身位置，如此便可以模拟 Web 中的绝对定位。</p>
<p>底部对齐的方案有很多，我们这里说一下 Flex 方案，幸运的是 Flutter 提供了 Flex 组件，可以通过属性设置很容易模拟 flex-direction、align-items 样式。至于弹性空间的分配（flex: 1），也有Expanded Widget 可以模拟。</p>
<p>另外一些通用样式，比如宽、高、背景色、边框、圆角可以在 Container Widget 中设置；文本颜色、字体大小可以在 Text Widget 中设置；图片填充模式可以在 DecorationImage Widget 中设置等等。</p>
<p>我们再通过下图的一个常见商品卡片示例看下在 Flutter 中如何进行样式还原：
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/cbb9fea116704b21aa2edd96127816ab~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<ul>
<li><strong>事件绑定</strong></li>
</ul>
<p>最后再看一下事件绑定如何来做：</p>
<ol>
<li>在 Web 代码中，我们通过 Node.addEventListener(event, callback) 来监听 DOM 交互事件，而这个监听 API 会转成 addEvent(nodeId, event) 指令调到 Flutter；</li>
<li>Flutter 在捕获到用户的交互事件后，通过 nodeId 找到并触发绑定在 Web 层 Node 上的事件回调；</li>
</ol>
<p>该过程用一张图展示如下：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/f6219a4990664beeaf61fbe9b9e472f4~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>另外，Flutter 有着和 Web 类似的从内向外的事件冒泡机制，这也让 Flutter 和 Web 之间的事件绑定更贴合，但可惜的 是 Flutter 没有停止冒泡的机制，所以这块还需我们自己去编码模拟。</p>
<h2 data-id="heading-9">总结</h2>
<p>我们做个简单的回顾：</p>
<ol>
<li>Flutter 因其高性能、渲染一致的特性（自绘引擎），加之较高的开发效率（Dart 的 JIT 模式 + 响应式框架）和更低的人力成本（相比客户端），广受大家追捧；</li>
<li>面对 Flutter，前端的一些传统优势变得微弱，但我们可以尝试将两者的优点结合起来，也就是 Web On Flutter；</li>
<li>Web On Flutter 的技术思路有多种，主要是看如何将 Web 的渲染流程和 Flutter 的渲染流程桥接起来；</li>
<li>这其中的技术关键点包括：JS Binding、Dom 树映射、CSS 样式映射、事件绑定；</li>
</ol>
<p>顺便打个广告，作者所在的“飞猪-用户前端和数字化经营团队”HC多多，欢迎各位对旅行感兴趣，或者对 Flutter、Serverless 、微前端、一体化开发、端渲染、互动营销、招选投搭、智能化、体验技术、数据度量等等感兴趣的同学加入我们。投递邮箱：<a href="mailto:haonan.whn@ailbaba-inc.com">haonan.whn@ailbaba-inc.com</a>。也欢迎关注我们的飞猪技术公众号：Fliggy F2E，定期有高质量文章更新喔。</p>
<hr>
<p>别忘了6-5 下午直播哦，<a href="https://www.huodongxing.com/go/tl27" target="_blank" rel="nofollow noopener noreferrer">点我上车👉 (报名地址)：</a></p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/ef9e1525937d4d3daaf051d5ce4d46d0~tplv-k3u1fbpfcp-watermark.image" alt="大会海报.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>所有往期都有全程录播，<strong><a href="https://www.huodongxing.com/go/2021" target="_blank" rel="nofollow noopener noreferrer">上手年票一次性解锁全部</a></strong></p>
<hr>
<p>期待更多文章，点个赞</p></div>  
</div>
            