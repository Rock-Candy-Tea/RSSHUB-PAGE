
---
title: '企业级Flutter项目-走出第一步'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://ducafecat.tech/2021/05/14/translation/flutter-in-business-first-steps/2021-05-14-11-08-00.png'
author: 掘金
comments: false
date: Thu, 13 May 2021 19:22:32 GMT
thumbnail: 'https://ducafecat.tech/2021/05/14/translation/flutter-in-business-first-steps/2021-05-14-11-08-00.png'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p><img src="https://ducafecat.tech/2021/05/14/translation/flutter-in-business-first-steps/2021-05-14-11-08-00.png" alt loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-0">老铁记得 转发 ，猫哥会呈现更多 Flutter 好文~~~~</h2>
<h2 data-id="heading-1">微信 flutter 研修群 ducafecat</h2>
<h2 data-id="heading-2">原文</h2>
<blockquote>
<p><a href="https://matteozajac.medium.com/flutter-in-business-first-steps-d8d0648c913b" target="_blank" rel="nofollow noopener noreferrer">matteozajac.medium.com/flutter-in-…</a></p>
</blockquote>
<h2 data-id="heading-3">参考</h2>
<ul>
<li><a href="https://pub.dev/packages/flutter_bloc" target="_blank" rel="nofollow noopener noreferrer">pub.dev/packages/fl…</a></li>
<li><a href="https://pub.dev/packages/chopper" target="_blank" rel="nofollow noopener noreferrer">pub.dev/packages/ch…</a></li>
<li><a href="https://pub.dev/packages/json_serializable" target="_blank" rel="nofollow noopener noreferrer">pub.dev/packages/js…</a></li>
<li><a href="https://dart.dev/guides/language/effective-dart" target="_blank" rel="nofollow noopener noreferrer">dart.dev/guides/lang…</a></li>
<li><a href="https://plugins.jetbrains.com/plugin/12400-flutter-pub-version-checker" target="_blank" rel="nofollow noopener noreferrer">plugins.jetbrains.com/plugin/1240…</a></li>
</ul>
<h2 data-id="heading-4">正文</h2>
<p>大多数时候你必须为你的应用程序的技术债务付款。如果你在 MVP 之后没有良好的体系结构，那么现在是时候停下来，重构一下，让你的未来变得更加容易。事实上，在没有架构的情况下编写较小的应用程序更容易---- 很难不同意这一点---- 但是作为一个成熟的技术专家来考虑。</p>
<p>测试覆盖率，设计模式，代码分析，这些都是我正在考虑的。本文将介绍我们如何在提高代码质量和团队愉悦感的同时，交付出色的应用程序。</p>
<h3 data-id="heading-5">从架构开始</h3>
<p>Provider, BLoC, Redux ーー如果这些词听起来不熟悉，请在继续前进之前对它们有基本的了解。</p>
<p>它们都有优点和缺点，你可以自己选择。</p>
<p>拥有 Flutter 的知识和如何人们已经适应项目结构 BLoC 似乎是最简单的方式开始。</p>
<p>恕我直言，展示和理解 BLoC 如何工作的最好方式是看下面的图表。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/c2196c2e58994dd0b3c321f97fcc6cba~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<ul>
<li>表示层将事件发送到 BLoC</li>
<li>数据层异步执行较长的操作，例如从 API 或数据库获取数据</li>
<li>对用户界面产生返回值</li>
</ul>
<p>就这么简单。</p>
<p>自己实现 BLoC 模式这真的是很好的锻炼，你应该一次性完全理解它背后的流程。如果你已经这样做了</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/461119f135f2420a96b156b211c0de14~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>然后使用..。</p>
<h3 data-id="heading-6">BLoC 库</h3>
<p>幸运的是，社区没有让人失望。你不必每次都写 BLoC，只需使用这个方便的 library ー FlutterBloc。</p>
<p>我想指出几个关键特征:</p>
<ul>
<li>Event — 没有样板的事件-状态通信,</li>
<li>Dependency 依赖注入通过 BlocProvider,</li>
<li>BlocBuilder 根据接收的状态构建小部件,</li>
<li>BlocDelegate 使全局处理错误更加容易,</li>
<li>BLoC 可以(也应该)进行测试</li>
</ul>
<p><a href="https://pub.dev/packages/flutter_bloc" target="_blank" rel="nofollow noopener noreferrer">pub.dev/packages/fl…</a></p>
<h3 data-id="heading-7">采用 REST API</h3>
<p><img src="https://ducafecat.tech/2021/05/14/translation/flutter-in-business-first-steps/2021-05-14-10-52-06.png" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>如果你创建了一个移动应用程序，你将连接到一个远程数据源。最常用的方法是 REST api 和 JSON。当然，你已经这样做了很多次，所以没有更多的解释。</p>
<p>来自 Android world 的消息表明你已经使用过 Retrofit、 GSON 或莫希 JSON 转换器。这些真的是非常棒的工具。</p>
<p>Flutter 中使用 chopper 库</p>
<p><a href="https://pub.dev/packages/chopper" target="_blank" rel="nofollow noopener noreferrer">pub.dev/packages/ch…</a></p>
<p>在这两种情况下，您都需要为您的 API 定义抽象类，并使用 <code>flutter pub run build_runner build</code> 生成它。</p>
<p>接下来，没有类似 GSON 的库可以将 JSON 转换为 POJO。您需要编写自己的映射器函数，或者使用 <code>json_serializable</code>，它通过注释 Dart 类自动生成转换到 JSON 和从 JSON 转换的代码。这个过程本身非常简单，你肯定会习惯的。</p>
<p><a href="https://pub.dev/packages/json_serializable" target="_blank" rel="nofollow noopener noreferrer">pub.dev/packages/js…</a></p>
<h3 data-id="heading-8">本地持久化</h3>
<p><img src="https://ducafecat.tech/2021/05/14/translation/flutter-in-business-first-steps/2021-05-14-10-55-34.png" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>在大多数情况下，当需要缓存我们的数据时，Sqflite 是我们的首选。它只是一个 SQLite Dart 实现，支持:</p>
<ul>
<li>原始 SQL 查询,</li>
<li>插入/查询/更新/删除的方便助手,</li>
<li>批次ー避免性能问题。</li>
</ul>
<h3 data-id="heading-9">分析代码</h3>
<p>在项目中拥有并保持代码样式对于团队来说可能是至关重要的。与体系结构一样，它也是维护项目和团队成员之间的质量、一致性的关键因素。</p>
<p>默认情况下，ide 集成了默认的静态分析，您可以根据需要扩展和调整这些分析。在他们的文档中很好地描述了 Effective 有自己的线头规则ーー Effective Dart。如果您喜欢这种风格(我确实喜欢) ，来自 Google 的开发团队就创建了一个带有这种规则集的包(pedantic | Dart 包)</p>
<ul>
<li>
<p>Effective Dart
<a href="https://dart.dev/guides/language/effective-dart" target="_blank" rel="nofollow noopener noreferrer">dart.dev/guides/lang…</a></p>
</li>
<li>
<p>pedantic
<a href="https://pub.dev/packages/pedantic" target="_blank" rel="nofollow noopener noreferrer">pub.dev/packages/pe…</a></p>
</li>
</ul>
<h3 data-id="heading-10">值得一提</h3>
<p>手动检查每个包的版本可能有点烦人。对于 Android Studio 用户，你可以查看这个插件 Flutter Pub Version Checker ー For IntelliJ IDEA，Android Studio 为你提供。突出显示带有新版本的软件包非常方便。</p>
<p><a href="https://plugins.jetbrains.com/plugin/12400-flutter-pub-version-checker" target="_blank" rel="nofollow noopener noreferrer">plugins.jetbrains.com/plugin/1240…</a></p>
<h3 data-id="heading-11">待续</h3>
<p>这是一个关于我们公司内部使用的库和方法的快速总结。如果你正在寻找一些开始点，它也应该有助于你的项目，但作为 Flutter 已经演变，我们有许多可行的解决方案，共同的问题，这只是其中之一。在下一篇文章中，我将展示体系结构图，解释特定的层，并实现一个列表屏幕(从远程、本地持久化获取)。</p>
<hr>
<p>© 猫哥</p>
<p><a href="https://ducafecat.tech/" target="_blank" rel="nofollow noopener noreferrer">ducafecat.tech/</a></p>
<p><a href="https://github.com/ducafecat" target="_blank" rel="nofollow noopener noreferrer">github.com/ducafecat</a></p>
<h2 data-id="heading-12">往期</h2>
<h3 data-id="heading-13">开源</h3>
<h4 data-id="heading-14">GetX Quick Start</h4>
<p><a href="https://github.com/ducafecat/getx_quick_start" target="_blank" rel="nofollow noopener noreferrer">github.com/ducafecat/g…</a></p>
<h4 data-id="heading-15">新闻客户端</h4>
<p><a href="https://github.com/ducafecat/flutter_learn_news" target="_blank" rel="nofollow noopener noreferrer">github.com/ducafecat/f…</a></p>
<h3 data-id="heading-16">strapi 手册译文</h3>
<p><a href="https://getstrapi.cn/" target="_blank" rel="nofollow noopener noreferrer">getstrapi.cn</a></p>
<h3 data-id="heading-17">微信讨论群 ducafecat</h3>
<h3 data-id="heading-18">系列集合</h3>
<h4 data-id="heading-19">译文</h4>
<p><a href="https://ducafecat.tech/categories/%E8%AF%91%E6%96%87/" target="_blank" rel="nofollow noopener noreferrer">ducafecat.tech/categories/…</a></p>
<h4 data-id="heading-20">开源</h4>
<p><a href="https://ducafecat.tech/categories/%E5%BC%80%E6%BA%90/" target="_blank" rel="nofollow noopener noreferrer">ducafecat.tech/categories/…</a></p>
<h4 data-id="heading-21">Dart 编程语言基础</h4>
<p><a href="https://space.bilibili.com/404904528/channel/detail?cid=111585" target="_blank" rel="nofollow noopener noreferrer">space.bilibili.com/404904528/c…</a></p>
<h4 data-id="heading-22">Flutter 零基础入门</h4>
<p><a href="https://space.bilibili.com/404904528/channel/detail?cid=123470" target="_blank" rel="nofollow noopener noreferrer">space.bilibili.com/404904528/c…</a></p>
<h4 data-id="heading-23">Flutter 实战从零开始 新闻客户端</h4>
<p><a href="https://space.bilibili.com/404904528/channel/detail?cid=106755" target="_blank" rel="nofollow noopener noreferrer">space.bilibili.com/404904528/c…</a></p>
<h4 data-id="heading-24">Flutter 组件开发</h4>
<p><a href="https://space.bilibili.com/404904528/channel/detail?cid=144262" target="_blank" rel="nofollow noopener noreferrer">space.bilibili.com/404904528/c…</a></p>
<h4 data-id="heading-25">Flutter Bloc</h4>
<p><a href="https://space.bilibili.com/404904528/channel/detail?cid=177519" target="_blank" rel="nofollow noopener noreferrer">space.bilibili.com/404904528/c…</a></p>
<h4 data-id="heading-26">Flutter Getx4</h4>
<p><a href="https://space.bilibili.com/404904528/channel/detail?cid=177514" target="_blank" rel="nofollow noopener noreferrer">space.bilibili.com/404904528/c…</a></p>
<h4 data-id="heading-27">Docker Yapi</h4>
<p><a href="https://space.bilibili.com/404904528/channel/detail?cid=130578" target="_blank" rel="nofollow noopener noreferrer">space.bilibili.com/404904528/c…</a></p></div>  
</div>
            