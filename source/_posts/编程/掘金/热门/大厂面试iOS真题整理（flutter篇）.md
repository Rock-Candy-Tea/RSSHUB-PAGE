
---
title: '大厂面试iOS真题整理（flutter篇）'
categories: 
 - 编程
 - 掘金
 - 热门
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/fdbb8aadca104c41b1ad5e31a58e496d~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Sat, 07 Aug 2021 02:39:04 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/fdbb8aadca104c41b1ad5e31a58e496d~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p><strong>Flutter 的面试其实和 Android 面试的套路差不多，也是分两个部分：</strong></p>
<p><strong>1.Dart</strong></p>
<p><strong>2.Flutter</strong></p>
<p>毕竟 Flutter 要使用 Dart 来写，那也就必须了解 Dart 的一些相关知识点。</p>
<hr>
<h1 data-id="heading-0">Dart 相关面试题</h1>
<h2 data-id="heading-1">1. Dart 当中的 「..」表示什么意思？</h2>
<p>Dart 当中的 「..」意思是 「级联操作符」，为了方便配置而使用。</p>
<p>「..」和「.」不同的是 调用「..」后返回的相当于是 this，而「.」返回的则是该方法返回的值 。</p>
<h2 data-id="heading-2">2. Dart 的作用域</h2>
<p>Dart 没有 「public」「private」等关键字，默认就是公开的，私有变量使用 下划线 <code>_</code>开头。</p>
<h2 data-id="heading-3">3. Dart 是不是单线程模型？是如何运行的？</h2>
<p>Dart 是单线程模型，如何运行的看这张图：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/fdbb8aadca104c41b1ad5e31a58e496d~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>引用《Flutter中文网》里的话：</p>
<blockquote>
<p>Dart 在单线程中是以消息循环机制来运行的，其中包含两个任务队列，一个是“微任务队列” <strong>microtask queue</strong>，另一个叫做“事件队列” <strong>event queue</strong>。</p>
<p>入口函数 main() 执行完后，消息循环机制便启动了。首先会按照先进先出的顺序逐个执行微任务队列中的任务，当所有微任务队列执行完后便开始执行事件队列中的任务，事件任务执行完毕后再去执行微任务，如此循环往复，生生不息。</p>
</blockquote>
<hr>
<blockquote>
<p><strong><a href="https://link.juejin.cn/?target=https%3A%2F%2Fdocs.qq.com%2Fdoc%2FDY1FKZ2pOYXhKWlJH" target="_blank" rel="nofollow noopener noreferrer" title="https://docs.qq.com/doc/DY1FKZ2pOYXhKWlJH" ref="nofollow noopener noreferrer">更多面试资料</a></strong></p>
</blockquote>
<h2 data-id="heading-4">4. Dart 多任务如何并行的？</h2>
<p>刚才也说了，既然 Dart 不存在多线程，那如何进行多任务并行？</p>
<p>Dart 当中提供了一个 <strong>类似于新线程，但是不共享内存的独立运行的 worker - isolate</strong>。</p>
<p>那他们是如何交互的？</p>
<p>这里引用 flutter入门之dart中的并发编程、异步和事件驱动详解 中的一部分答案：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/5538663c63164192a1e833e384927110~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<blockquote>
<p>在dart中，一个Isolate对象其实就是一个isolate执行环境的引用，一般来说我们都是通过当前的isolate去控制其他的isolate完成彼此之间的交互，而当我们想要创建一个新的Isolate可以使用<strong>Isolate.spawn</strong>方法获取返回的一个新的isolate对象，两个isolate之间使用SendPort相互发送消息，而isolate中也存在了一个与之对应的ReceivePort接受消息用来处理，但是我们需要注意的是，ReceivePort和SendPort在每个isolate都有一对，只有同一个isolate中的ReceivePort才能接受到当前类的SendPort发送的消息并且处理。</p>
</blockquote>
<h2 data-id="heading-5">5. 说一下 Future？</h2>
<p>Future，字面意思「未来」，是用来处理异步的工具。</p>
<p>刚才也说过：</p>
<blockquote>
<p>Dart 在单线程中是以消息循环机制来运行的，其中包含两个任务队列，一个是“微任务队列” <strong>microtask queue</strong>，另一个叫做“事件队列” <strong>event queue</strong>。</p>
</blockquote>
<p>Future 默认情况下其实就是往「事件队列」里插入一个事件，当有空余时间的时候就去执行，当执行完毕后会回调 <code>Future.then(v)</code> 方法。</p>
<p>而我们也可以通过使用 <code>Future.microtask</code> 方法来向 「微任务队列」中插入一个任务，这样就会提高他执行的效率。</p>
<p>因为在 Dart 每一个 isolate 当中，执行优先级为 ：Main > MicroTask > EventQueue</p>
<h2 data-id="heading-6">6. 说一下 Stream？</h2>
<p>Stream 和 Feature 一样，都是用来处理异步的工具。</p>
<p>但是 Stream 和 Feature 不同的地方是 Stream 可以接收多个异步结果，而Feature 只有一个。</p>
<p>Stream 的创建可以使用 <code>Stream.fromFuture</code>，也可以使用 <code>StreamController</code> 来创建和控制。</p>
<p>还有一个注意点是：普通的 Stream 只可以有一个订阅者，如果想要多订阅的话，要使用 <code>asBroadcastStream()</code>。</p>
<h2 data-id="heading-7">7. 说一下 mixin？</h2>
<p>关于什么是 mixin，引用 <strong>张风捷特烈</strong> 文章中的：</p>
<blockquote>
<p>首先mixin是一个定义类的关键字。直译出来是混入，混合的意思 Dart为了支持多重继承，引入了mixin关键字，它最大的特殊处在于： <code>mixin定义的类不能有构造方法</code>，这样可以避免继承多个类而产生的父类构造方法冲突</p>
</blockquote>
<p>Flutter 相关面试题</p>
<h3 data-id="heading-8">1. StatefulWidget 的生命周期</h3>
<p>•<code>initState()</code>：Widget 初始化当前 State，在当前方法中是不能获取到 Context 的，如想获取，可以试试 <code>Future.delayed()</code>•<code>didChangeDependencies()</code>：在 <code>initState()</code> 后调用，<code>State</code>对象依赖关系发生变化的时候也会调用。•<code>deactivate()</code>：当 <code>State</code> 被暂时从视图树中移除时会调用这个方法，页面切换时也会调用该方法，和Android里的 <code>onPause</code> 差不多。•<code>dispose()</code>：Widget 销毁时调用。•<code>didUpdateWidget</code>：Widget 状态发生变化的时候调用。</p>
<p>借用 CoorChice 文章 里的一张图：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/c2fe670c6e954b4db4b02e478a8b5128~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-9">2. Flutter 如何与 Android iOS 通信？</h3>
<p>Flutter 通过 <code>PlatformChannel</code> 与原生进行交互，其中 <code>PlatformChannel</code> 分为三种：</p>
<p>1.BasicMessageChannel：用于传递字符串和半结构化的信息。2.MethodChannel：用于传递方法调用。Flutter主动调用Native的方法，并获取相应的返回值。3.EventChannel：用于数据流（event streams）的通信。</p>
<p>具体可以查看 闲鱼技术：深入理解 Flutter Platform Channel<sup>[4]</sup>。</p>
<h3 data-id="heading-10">3. 什么是 Widgets、RenderObjects 和 Elements？</h3>
<p>•<code>Widget</code> 仅用于存储渲染所需要的信息。•<code>RenderObject</code> 负责管理布局、绘制等操作。•<code>Element</code> 才是这颗巨大的控件树上的实体。</p>
<p>具体可以查看 [译] Flutter，什么是 Widgets、RenderObjects 和 Elements？<sup>[5]</sup></p>
<h3 data-id="heading-11">4. 说一下什么是状态管理，为什么需要它？</h3>
<p>首先状态其实是一个概念上的东西，区分全局状态和局部状态。</p>
<p>局部状态比如说一个控件中输入的信息，全局状态比如是登陆后从后台请求回来的 userId。</p>
<p>当全局状态越来越多，多个页面共享一个状态时，我们就需要管理它。</p>
<p>常用的状态管理有：</p>
<p>•ScopedModel•BLoC•Redux / FishRedux•Provider</p>
<h3 data-id="heading-12">5. 说一下 BLoC 模式？</h3>
<p>这里引用一部分：</p>
<blockquote>
<p>BLoC是一种利用reactive programming方式构建应用的方法，这是一个由流构成的完全异步的世界。</p>
</blockquote>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/32c0bc00401c4abaa91e2092f1c5df88~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-13">6. 如何统一管理错误页面？</h3>
<p>我们都知道，如果在 Flutter 当中出错的话，那就是一片红。</p>
<p>可以使用 <code>ErrorWidget.builder</code> 来自定义一个 Widget 就 ok 了。</p>
<h1 data-id="heading-14">总结</h1>
<p>暂时就写到这，写了这么多，自己对 Flutter & Dart 的基础认识也更深了，也欢迎各路大佬交流。</p></div>  
</div>
            