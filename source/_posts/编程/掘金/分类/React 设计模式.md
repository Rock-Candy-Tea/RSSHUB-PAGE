
---
title: 'React 设计模式'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/a4b11ac2a5084370833ff3e681e3b7c3~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Wed, 11 Aug 2021 23:07:11 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/a4b11ac2a5084370833ff3e681e3b7c3~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h2 data-id="heading-0">三大模块</h2>
<p>我们创建一个Holle World，看一下浏览器的调用栈。你会发现react执行了一大堆函数，我们将这些函数分成调度、协调、渲染三大模块，这三大模块就是接下来要研究的。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/a4b11ac2a5084370833ff3e681e3b7c3~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-1">设计理念</h2>
<p>在学习之前我们要将思路转变，我们作为开发者总是会去关心API上的事情，但是作为一个框架的开发人员，应该是重点关心设计理念。</p>
<p>如何设计，决定着这个框架的最终走向，这是十分重要的。</p>
<p>引用官网说的一句话：React是用 JavaScript 构建 <strong>快速响应</strong> 的大型应用程序。</p>
<p>那他是如何做到快速响应的？开发中是什么导致我们的应用不流畅呢？</p>
<p>可能来源于：大量的计算或者网络请求的延迟。总结起来就是：计算能力与网络延迟。</p>
<p>计算能力关乎到我们的CPU。网络延迟关乎到IO。这两个是我们的瓶颈。</p>
<h4 data-id="heading-2">React 解决CPU瓶颈的办法</h4>
<p>主流浏览器的刷新频率是60HZ（也就是一帧），也就是16.6ms刷新一次。在这16.6ms中浏览器会依次执行：JavaScript脚本、样式布局、样式绘制。</p>
<p>我们想一下，如果JavaScript脚本执行时间超过16.6ms（也就是一帧），会发生什么情况？</p>
<p>答案是：在当前这一帧中就没有时间进行样式布局、样式绘制。会出现掉帧的情况，从而导致卡顿。比如，浏览器滚动不流畅，输入框输入的字符不能及时响应在页面上。</p>
<p>前端的解决办法大部分是使用防抖或节流的方式，进而限制一定时间内浏览器的响应变化。这种方式是治标不治本的办法。</p>
<p>React给出的方案：将 <strong>同步的更新</strong> 转变成 <strong>异步可中断的更新</strong>。</p>
<h4 data-id="heading-3">异步可中断的更新</h4>
<p>如果某一部分的执行时间特别长，React 会中断自己的工作，并将控制权交给浏览器。等待下一帧自己预留的那部分时间到来之后，React 会继续之前被中断的工作。</p>
<p>这样，浏览器就会有时间进行样式布局、样式绘制。从而达到减少掉帧的可能性。</p>
<h4 data-id="heading-4">React 解决IO瓶颈的办法</h4>
<p>文档上给出的是：将人机交互研究的结果整合到真实的UI中。比如，在屏幕之间切换时显示过多的中间加载状态会使切换的速度变慢。</p>
<h2 data-id="heading-5">新旧的架构对比</h2>
<p>新的架构解决了老架构什么问题？新架构相对于老架构的优点是什么？</p>
<h4 data-id="heading-6">老的架构</h4>
<p>老架构是分成两个部分：</p>
<ul>
<li>决定渲染什么组件    ----   Reconclier（协调器）</li>
<li>将组件渲染到视图中  ----   Renderer（渲染器）</li>
</ul>
<p>Reconclier(协调器)作用：负责本次更新哪些组件被渲染。Diff算法就是发生在Reconclier(协调器)中。</p>
<p>Diff算法中会将上次更新的组件与本次更新的组件做一个对比，最终只有变化的部分被渲染到视图中。</p>
<p>经过Diff算法决定渲染的组件会被交给Renderer(渲染器)，渲染到视图中。</p>
<p>不同的Renderer(渲染器)会将组件渲染到不同的数组环境的视图中。比如：</p>
<ul>
<li>ReactDom渲染器，会将组件渲染到DOM/SSR中。</li>
<li>ReactNative渲染器，会将组件渲染为APP原生组件。</li>
<li>ReactTest渲染器，会将组件渲染为纯JS对象，用于测试。</li>
<li>ReactArt渲染器，会将组件渲染到canvas/svg上。</li>
</ul>
<p>在React老的架构里，如果页面上的UI发生改变，首先会去执行Reconclier(协调器)，然后再去执行Renderer(渲染器)。这两个是交替且同步执行的。</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/7f448f4663814cb4afccbd0685ac1191~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>上面这张图，我希望点击button按钮，左页面每个li变为2、4、6。同时不希望Renconclier(协调器)与Renderer(渲染器)同步执行。渲染器在渲染1变为2之后，去中断发生。</p>
<p>显然老的架构是无法支持的。</p>
<h4 data-id="heading-7">新的架构</h4>
<p>由于老的架构无法中断发生，React16重写了架构。将原先的 <strong>同步更新</strong> 改为 <strong>异步可中断更新</strong></p>
<p>由于新的架构是可中断的，React加入了一个模块对这些异步更新进行管理。如下三部分：</p>
<ul>
<li>调度更新             ----  Scheduler(调度器)</li>
<li>决定需要更新什么组件   ----  Reconclier(协调器)</li>
<li>将组件更新到视图中    ----   Renderer(渲染器)</li>
</ul>
<p>老的架构中，UI发生更新之后直接会交给Reconclier(协调器)处理。</p>
<p>新的架构中，UI发生更新会先交给Scheduler(调度器)进行优先级比较，优先级高的会交给Reconclier(协调器)进行处理。</p>
<p>在协调器采用Diff算法时，产生了更高优先级的更新 Reconclier(协调器)会中断，然后执行更高优先级的更新。</p>
<p>由于Scheduler(调度器)与Reconclier(协调器)都是在内存中，用户并不会感知到被中断的操作过程。</p>
<p>当某次更新完成了在协调器中的工作时，Reconclier(协调器)会通知Renderer(渲染器)，本次更新中有哪些组件需要进行UI渲染操作。最后会由Renderer(渲染器)来分别执行视图的渲染操作。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/a2153c438b464880b86500ab72980a6f~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>上面这张图是产生更新时，三部分是如何相互工作的。</p>
<p>Scheduler(调度器)：评定优先级，将当前评定的高优先级交给Reconclier(协调器)。</p>
<p>Reconclier(协调器)：接收到更新之后创建虚拟DOM，然后给要更新的虚拟DOM打上updata标记，最后交给Renderer(渲染器)。</p>
<p>Renderer(渲染器)：接收到通知，查看哪些虚拟DOM被标记了updata。对应的执行更新DOM操作。</p>
<h2 data-id="heading-8">总结</h2>
<ul>
<li>老架构如何运行的？有什么缺点？</li>
<li>新架构如何解决快速响应问题？</li>
<li>新架构的Scheduler(调度器)、Reconclier(协调器)、Renderer(渲染器)三部分如何配合完成可中断的异步更新的？</li>
<li>Diff算法做了什么？</li>
</ul>
<p>最后，感谢大家支持啦～～～～～～～～～</p></div>  
</div>
            