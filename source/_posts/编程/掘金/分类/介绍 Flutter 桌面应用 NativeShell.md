
---
title: '介绍 Flutter 桌面应用 NativeShell'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://ducafecat.tech/2021/06/09/translation/introducing-nativeshell/2021-06-09-08-59-44.png'
author: 掘金
comments: false
date: Tue, 08 Jun 2021 17:26:50 GMT
thumbnail: 'https://ducafecat.tech/2021/06/09/translation/introducing-nativeshell/2021-06-09-08-59-44.png'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p><img src="https://ducafecat.tech/2021/06/09/translation/introducing-nativeshell/2021-06-09-08-59-44.png" alt loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-0">猫哥说</h2>
<p>看到这张图片，我就感觉脖子酸。。。我这样摆过，虽然看起来很 cool，然后你的脖子要上下调整，这比左右调整费事。</p>
<p>今天推荐阅读的是关于 Flutter 桌面开发，下面有原文、代码 Git 链接。</p>
<p>开始前我想起 React Native 说过的一句话 《用同样的方法在多端开发》，这句话很玄妙又很正确，就是说不是让你同一套代码同时能编译成 ios android web windows linux ...，只是代码的高度复用，所以有的同学在做多端架构时就要注意拆包了。</p>
<p>比如 你的业务代码、API、Entity、功能函数 很多情况下是复用的。但是各个平台的底层、交互体验是个性化。</p>
<p>不要被在 ios android 两端平滑兼容所欺骗。</p>
<p>今天介绍 NativeShell 这个桌面程序，这个程序演示了 多窗口、模式对话框、拖拽、菜单、工具栏、文件操作、系统 API 调用的例子，如果你正在做研究，这是一个很好参考。</p>
<h2 data-id="heading-1">老铁记得 转发 ，猫哥会呈现更多 Flutter 好文~~~~</h2>
<h2 data-id="heading-2">微信群 ducafecat</h2>
<h2 data-id="heading-3">原文</h2>
<blockquote>
<p><a href="https://matejknopp.com/post/introducing-nativeshell/" target="_blank" rel="nofollow noopener noreferrer">matejknopp.com/post/introd…</a></p>
</blockquote>
<h2 data-id="heading-4">视频</h2>
<h2 data-id="heading-5">代码</h2>
<p><a href="https://github.com/nativeshell/app_template" target="_blank" rel="nofollow noopener noreferrer">github.com/nativeshell…</a></p>
<h2 data-id="heading-6">参考</h2>
<ul>
<li><a href="http://airflow.app/" target="_blank" rel="nofollow noopener noreferrer">airflow.app/</a></li>
<li><a href="https://airflow.app/remote-app/" target="_blank" rel="nofollow noopener noreferrer">airflow.app/remote-app/</a></li>
<li><a href="https://github.com/nativeshell/examples/blob/main/src/file_open_dialog.rs#L18" target="_blank" rel="nofollow noopener noreferrer">github.com/nativeshell…</a></li>
<li><a href="https://github.com/nativeshell/examples/blob/main/lib/pages/drag_drop.dart" target="_blank" rel="nofollow noopener noreferrer">github.com/nativeshell…</a></li>
<li><a href="https://github.com/nativeshell/nativeshell/blob/main/nativeshell/src/shell/platform/win32/drag_com.rs" target="_blank" rel="nofollow noopener noreferrer">github.com/nativeshell…</a></li>
</ul>
<h2 data-id="heading-7">正文</h2>
<p>自从我第一次看到 Turbo Vision，我就对桌面应用程序感兴趣。DOS 中那些文本模式可调整大小的窗口对我来说就像魔术一样。它激发了人们对用户界面框架的兴趣，这种框架在 20 多年后依然很强大。</p>
<p>在过去十年左右的时间里，人们的注意力主要转移到了网络和移动设备上，这并没有让我感到特别高兴。所以我觉得是时候从阴影中爬出来，离开我的舒适区，试着把一些聚光灯带回它应该在的地方。到桌面上去！:)</p>
<h3 data-id="heading-8">Flutter 之路</h3>
<p>我最后一个处理的桌面应用程序是(现在仍然是) Airflow。它是 Qt 和大量平台特定代码的混合体。如果我自己这么说的话，我对最终的结果非常满意，但是开发人员的经验和整体生产力还有很多需要改进的地方。</p>
<p><a href="http://airflow.app/" target="_blank" rel="nofollow noopener noreferrer">airflow.app/</a></p>
<p>大约两年前，我需要一个适用于 iOS 和安卓系统的气流应用程序。经过几个原型后，决定做出，我去 Flutter。我确实喜欢认为我有自己的 UI 开发经验，毕竟，我在不同的平台上使用过十几个 GUI 框架，所以现在没有什么能让我感到惊讶的了，对吧？错了。他们所有人中最大的惊喜就是和 Flutter 一起工作的感觉是多么的好。在我的一生中，从来没有，一次也没有，建立用户界面这么有意义。</p>
<p><a href="https://airflow.app/remote-app/" target="_blank" rel="nofollow noopener noreferrer">airflow.app/remote-app/</a></p>
<p>如果我能用这种方式构建桌面应用程序，岂不是很神奇？当然，这是可能的，但现实是一个严酷的情妇，在那个时候桌面嵌入仍然处于婴儿期。那就回到 Qt 吧。但这个念头一直在我脑海中挥之不去。</p>
<p>一两年过去了，很多事情发生了变化。还有很多工作要做，但是桌面嵌入已经成熟了很多，而且 Flutter on desktop 已经开始成为一个可行的选择。</p>
<h3 data-id="heading-9">Flutter desktop 嵌入</h3>
<p>现在你可能会问: Matt，Flutter 不是已经嵌入了桌面吗? 那么这一切都是为了什么呢？</p>
<p>是的，的确如此。NativeShell 就建立在他们之上。您可以将 Flutter 桌面嵌入程序想象为一个平台视图组件(想想 GtkWidget、 NSView 或者，恕我直言，HWND)。它处理鼠标和键盘输入，绘画，但它不尝试管理窗口，或 Flutter 引擎/隔离。或者做一些像平台菜单和拖放的事情。为了使事情更加复杂，Flutter 嵌入在每个平台上都有完全不同的 API。因此，如果您希望为一些低级代码创建引擎或注册平台通道处理程序，则需要为每个平台分别执行此操作。</p>
<p><a href="https://nativeshell.dev/" target="_blank" rel="nofollow noopener noreferrer">nativeshell.dev/</a></p>
<h3 data-id="heading-10">这就是 NativeShell 介入的地方</h3>
<p>从 Flutter 桌面嵌入结束的地方开始。它为现有的 Flutter 嵌入提供了一个一致的、与平台无关的 API。它管理引擎和窗户。它提供了拖放支持，对平台菜单的访问，以及其他超出 Flutter 嵌入范围的功能。并且它通过简单易用的 Dart API 公开了所有这些。</p>
<p>NativeShell 是用铁锈写的。锈是伟大的，因为它可以让你编写高效的低级平台特定的代码，如果你需要，但它也让你使用 NativeShell，而不必知道任何锈。简单地执行货物运输是所有需要让事情进行。Cargo 是 Rust 软件包管理器(就像 pub 是用于 Dart 的) ，它负责下载和构建所有依赖项。</p>
<h3 data-id="heading-11">开始</h3>
<ul>
<li>
<p>Install Rust
<a href="https://www.rust-lang.org/tools/install" target="_blank" rel="nofollow noopener noreferrer">www.rust-lang.org/tools/insta…</a></p>
</li>
<li>
<p>Install Flutter
<a href="https://flutter.dev/docs/get-started/install" target="_blank" rel="nofollow noopener noreferrer">flutter.dev/docs/get-st…</a></p>
</li>
<li>
<p>在 Flutter 中启用桌面支持(为您的平台选择一个)</p>
</li>
</ul>
<pre><code class="hljs language-sh copyable" lang="sh">$ flutter config --enable-windows-desktop
$ flutter config --enable-macos-desktop
$ flutter config --enable-linux-desktop
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>Switch to Flutter Master</li>
</ul>
<pre><code class="hljs language-sh copyable" lang="sh">$ flutter channel master
$ flutter upgrade
<span class="copy-code-btn">复制代码</span></code></pre>
<p>在这之后，你应该可以开始了:</p>
<pre><code class="hljs language-sh copyable" lang="sh">$ git <span class="hljs-built_in">clone</span> https://github.com/nativeshell/examples.git
$ <span class="hljs-built_in">cd</span> examples
$ cargo run
<span class="copy-code-btn">复制代码</span></code></pre>
<p>NativeShell 透明地集成了 Flutter 建立过程和货物。如果铁锈和飞镖之神在对你微笑，这就是你现在应该看到的:</p>
<p><img src="https://ducafecat.tech/2021/06/09/translation/introducing-nativeshell/2021-06-09-08-38-25.png" alt loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-12">Platform Channels</h3>
<p>如果您需要从 Flutter 应用程序调用本机代码，这两个选项是平台通道或 FFI。对于一般使用的平台通道是预先设计好的，因为它们更容易使用，并且能够在平台和 UI 线程之间适当地传递消息。</p>
<p>这就是使用 NativeShell 注册平台通道处理程序的效果(我保证，这里也是惟一的 Rust 代码)</p>
<pre><code class="hljs language-rust copyable" lang="rust"><span class="hljs-function"><span class="hljs-keyword">fn</span> <span class="hljs-title">register_example_channel</span></span>(context: Rc<Context>) &#123;
    context
        .message_manager
        .borrow_mut()
        .register_method_handler(<span class="hljs-string">"example_channel"</span>, |call, reply, engine| &#123;
            <span class="hljs-keyword">match</span> call.method.as_str() &#123;
                <span class="hljs-string">"echo"</span> => &#123;
                    reply.send_ok(call.args);
                &#125;
                _ => &#123;&#125;
            &#125;
        &#125;);
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>为了直接使用现有的平台嵌入 API 来完成这项工作，您需要使用平台特定的 API 为每个平台分别编写这些代码。然后确保每次创建新引擎时都注册处理程序(关闭引擎时可能注销)。</p>
<p>使用 NativeShell，您只需注册处理程序一次，它可以从任何引擎调用。消息可以通过 Serde 被透明地序列化和反序列化为 Rust 结构(使用 Flutter 的标准方法编解码格式)。</p>
<p><a href="https://github.com/nativeshell/examples/blob/main/src/file_open_dialog.rs#L18" target="_blank" rel="nofollow noopener noreferrer">github.com/nativeshell…</a></p>
<h3 data-id="heading-13">Window Management</h3>
<p>想必你希望你的桌面应用程序有多个窗口？NativeShell 已经掩护你了。调整窗口大小到内容或设置最小的窗口大小，使 Flutter 布局不底流？它也能做到这一点。它还确保只在内容准备好后才显示窗口，从而消除了丑陋的闪烁。</p>
<p>目前，每个窗口作为单独的独立窗体运行。NativeShell 为创建窗口、设置和调整几何形状、更新样式和窗口标题提供了 API。它还提供了便于在窗口之间进行通信的 API。</p>
<p>视频可以根据内容调整大小，也可以根据内容大小调整大小。</p>
<ul>
<li>多窗口</li>
</ul>
<p><img src="https://ducafecat.tech/2021/06/09/translation/introducing-nativeshell/2021-06-09-08-40-27.png" alt loading="lazy" referrerpolicy="no-referrer"></p>
<ul>
<li>模式对话框</li>
</ul>
<p><img src="https://ducafecat.tech/2021/06/09/translation/introducing-nativeshell/2021-06-09-08-40-59.png" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>这将是 Dart 中如何创建和管理多个窗口的最小演示:</p>
<pre><code class="hljs language-dart copyable" lang="dart"><span class="hljs-keyword">void</span> main() <span class="hljs-keyword">async</span> &#123;
  runApp(MinimalApp());
&#125;

<span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">MinimalApp</span> <span class="hljs-keyword">extends</span> <span class="hljs-title">StatelessWidget</span> </span>&#123;
  <span class="hljs-meta">@override</span>
  Widget build(BuildContext context) &#123;
    <span class="hljs-comment">// Widgets above WindowWidget will be same in all windows. The actual</span>
    <span class="hljs-comment">// window content will be determined by WindowState</span>
    <span class="hljs-keyword">return</span> MaterialApp(
      home: WindowWidget(
        onCreateState: (initData) &#123;
          WindowState? context;
          context ??= OtherWindowState.fromInitData(initData);
          <span class="hljs-comment">// possibly no init data, this is main window</span>
          context ??= MainWindowState();
          <span class="hljs-keyword">return</span> context;
        &#125;,
      ),
    );
  &#125;
&#125;

<span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">MainWindowState</span> <span class="hljs-keyword">extends</span> <span class="hljs-title">WindowState</span> </span>&#123;
  <span class="hljs-meta">@override</span>
  Widget build(BuildContext context) &#123;
    <span class="hljs-keyword">return</span> TextButton(
      onPressed: () <span class="hljs-keyword">async</span> &#123;
        <span class="hljs-comment">// This will create new isolate for a window. Whatever is given to</span>
        <span class="hljs-comment">// Window.create will be provided by WindowWidget in new isolate</span>
        <span class="hljs-keyword">final</span> <span class="hljs-built_in">window</span> = <span class="hljs-keyword">await</span> Window.create(OtherWindowState.toInitData());
        <span class="hljs-comment">// you can use the window object to communicate with newly created</span>
        <span class="hljs-comment">// window or register handlers for window events</span>
        <span class="hljs-built_in">window</span>.closeEvent.addListener(() &#123;
          <span class="hljs-built_in">print</span>(<span class="hljs-string">'Window closed'</span>);
        &#125;);
      &#125;,
      child: Text(<span class="hljs-string">'Open Another Window'</span>),
    );
  &#125;
&#125;

<span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">OtherWindowState</span> <span class="hljs-keyword">extends</span> <span class="hljs-title">WindowState</span> </span>&#123;
  <span class="hljs-meta">@override</span>
  Widget build(BuildContext context) &#123;
    <span class="hljs-keyword">return</span> Text(<span class="hljs-string">'This is Another Window!'</span>);
  &#125;

  <span class="hljs-comment">// This can be anything that fromInitData recognizes</span>
  <span class="hljs-keyword">static</span> <span class="hljs-built_in">dynamic</span> toInitData() => &#123;
        <span class="hljs-string">'class'</span>: <span class="hljs-string">'OtherWindow'</span>,
      &#125;;

  <span class="hljs-keyword">static</span> OtherWindowState? fromInitData(<span class="hljs-built_in">dynamic</span> initData) &#123;
    <span class="hljs-keyword">if</span> (initData <span class="hljs-keyword">is</span> <span class="hljs-built_in">Map</span> && initData[<span class="hljs-string">'class'</span>] == <span class="hljs-string">'OtherWindow'</span>) &#123;
      <span class="hljs-keyword">return</span> OtherWindowState();
    &#125;
    <span class="hljs-keyword">return</span> <span class="hljs-keyword">null</span>;
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-14">Drag & Drop</h3>
<p>很难想象还有哪个桌面用户界面框架不支持拖放操作。NativeShell 支持拖放文件路径、 url、自定义 Dart 数据(由 StandardMethodCodec 实现序列化) ，甚至可以扩展以处理自定义平台特定格式。</p>
<p>它应该很容易使用，而且我对它的结果很满意，尽管它确实涉及到编写一些看起来非常吓人的代码。</p>
<p><img src="https://ducafecat.tech/2021/06/09/translation/introducing-nativeshell/2021-06-09-08-43-26.png" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p><a href="https://github.com/nativeshell/examples/blob/main/lib/pages/drag_drop.dart" target="_blank" rel="nofollow noopener noreferrer">github.com/nativeshell…</a></p>
<p><a href="https://github.com/nativeshell/nativeshell/blob/main/nativeshell/src/shell/platform/win32/drag_com.rs" target="_blank" rel="nofollow noopener noreferrer">github.com/nativeshell…</a></p>
<h3 data-id="heading-15">Popup Menu</h3>
<p>很多框架和应用程序都犯了这样的错误，这常常让我感到惊讶。直到最近 Firefox 才开始在 macOS 上使用本地弹出菜单。无论你的应用程序多么精致，如果你的菜单出错了，你就会感觉不对劲。</p>
<p>允许你轻松地创建和显示上下文菜单。考虑到菜单系统的强大功能，这个菜单 API 看似简单。菜单是反应性的。你可以要求重建菜单，而可见和 NativeShell 将计算三角洲和只更新菜单项实际上已经改变。</p>
<p><img src="https://ducafecat.tech/2021/06/09/translation/introducing-nativeshell/2021-06-09-08-44-37.png" alt loading="lazy" referrerpolicy="no-referrer"></p>
<pre><code class="hljs language-dart copyable" lang="dart">  <span class="hljs-built_in">int</span> _counter = <span class="hljs-number">0</span>;

  <span class="hljs-keyword">void</span> _showContextMenu(TapDownDetails e) <span class="hljs-keyword">async</span> &#123;
    <span class="hljs-keyword">final</span> menu = Menu(_buildContextMenu);

    <span class="hljs-comment">// Menu can be updated while visible</span>
    <span class="hljs-keyword">final</span> timer = Timer.periodic(<span class="hljs-built_in">Duration</span>(milliseconds: <span class="hljs-number">500</span>), (timer) &#123;
      ++_counter;
      <span class="hljs-comment">// This will call the _buildContextMenu() function, diff the old</span>
      <span class="hljs-comment">// and new menu items and only update those platform menu items that</span>
      <span class="hljs-comment">// actually changed</span>
      menu.update();
    &#125;);

    <span class="hljs-keyword">await</span> Window.of(context).showPopupMenu(menu, e.globalPosition);

    timer.cancel();
  &#125;

  <span class="hljs-built_in">List</span><MenuItem> _buildContextMenu() => [
        MenuItem(title: <span class="hljs-string">'Context menu Item'</span>, action: () &#123;&#125;),
        MenuItem(title: <span class="hljs-string">'Menu Update Counter <span class="hljs-subst">$_counter</span>'</span>, action: <span class="hljs-keyword">null</span>),
        MenuItem.separator(),
        MenuItem.children(title: <span class="hljs-string">'Submenu'</span>, children: [
          MenuItem(title: <span class="hljs-string">'Submenu Item 1'</span>, action: () &#123;&#125;),
          MenuItem(title: <span class="hljs-string">'Submenu Item 2'</span>, action: () &#123;&#125;),
        ]),
      ];
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-16">MenuBar</h3>
<p>可能是 NativeShell 中我最喜欢的功能。在 macOS 上，它呈现为空窗口小部件，而是将菜单放在系统菜单栏(在屏幕顶部)。在 Windows 和 Linux 上，它使用 Flutter 小部件呈现顶级菜单项，然后使用本机菜单处理其余部分。这意味着菜单栏可以位于小部件层次结构中的任何位置，它不局限于窗口的顶部，也不依赖于 GDI 或 Gtk 来绘制 iself。</p>
<p>它支持鼠标跟踪和键盘导航，就像普通系统菜单栏一样，但没有任何限制。</p>
<p><img src="https://ducafecat.tech/2021/06/09/translation/introducing-nativeshell/2021-06-09-08-45-43.png" alt loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-17">现在情况如何</h3>
<p>NativeShell 正在被沉重的开发。事情很可能会破裂。迫切需要更多的文档和示例。但我认为它的形状可能对某些人有用。</p>
<p>所有三个支持的平台(macOS，Windows，Linux)都具有完全的同等功能。</p>
<p><a href="https://github.com/nativeshell/nativeshell/tree/main/nativeshell/src/shell/platform/macos" target="_blank" rel="nofollow noopener noreferrer">github.com/nativeshell…</a></p>
<p><a href="https://github.com/nativeshell/nativeshell/tree/main/nativeshell/src/shell/platform/win32" target="_blank" rel="nofollow noopener noreferrer">github.com/nativeshell…</a></p>
<p><a href="https://github.com/nativeshell/nativeshell/tree/main/nativeshell/src/shell/platform/linux" target="_blank" rel="nofollow noopener noreferrer">github.com/nativeshell…</a></p>
<p>如果你一路走到了这里，你可以继续 nativeshell.dev。</p>
<p><a href="https://nativeshell.dev/" target="_blank" rel="nofollow noopener noreferrer">nativeshell.dev/</a></p>
<p>感谢您的反馈！</p>
<p><a href="https://github.com/nativeshell/nativeshell/issues" target="_blank" rel="nofollow noopener noreferrer">github.com/nativeshell…</a></p>
<hr>
<p>© 猫哥</p>
<p><a href="https://ducafecat.tech/" target="_blank" rel="nofollow noopener noreferrer">ducafecat.tech/</a></p>
<p><a href="https://github.com/ducafecat" target="_blank" rel="nofollow noopener noreferrer">github.com/ducafecat</a></p>
<h2 data-id="heading-18">往期</h2>
<h3 data-id="heading-19">开源</h3>
<h4 data-id="heading-20">GetX Quick Start</h4>
<p><a href="https://github.com/ducafecat/getx_quick_start" target="_blank" rel="nofollow noopener noreferrer">github.com/ducafecat/g…</a></p>
<h4 data-id="heading-21">新闻客户端</h4>
<p><a href="https://github.com/ducafecat/flutter_learn_news" target="_blank" rel="nofollow noopener noreferrer">github.com/ducafecat/f…</a></p>
<h3 data-id="heading-22">strapi 手册译文</h3>
<p><a href="https://getstrapi.cn/" target="_blank" rel="nofollow noopener noreferrer">getstrapi.cn</a></p>
<h3 data-id="heading-23">微信讨论群 ducafecat</h3>
<h3 data-id="heading-24">系列集合</h3>
<h4 data-id="heading-25">译文</h4>
<p><a href="https://ducafecat.tech/categories/%E8%AF%91%E6%96%87/" target="_blank" rel="nofollow noopener noreferrer">ducafecat.tech/categories/…</a></p>
<h4 data-id="heading-26">开源项目</h4>
<p><a href="https://ducafecat.tech/categories/%E5%BC%80%E6%BA%90/" target="_blank" rel="nofollow noopener noreferrer">ducafecat.tech/categories/…</a></p>
<h4 data-id="heading-27">Dart 编程语言基础</h4>
<p><a href="https://space.bilibili.com/404904528/channel/detail?cid=111585" target="_blank" rel="nofollow noopener noreferrer">space.bilibili.com/404904528/c…</a></p>
<h4 data-id="heading-28">Flutter 零基础入门</h4>
<p><a href="https://space.bilibili.com/404904528/channel/detail?cid=123470" target="_blank" rel="nofollow noopener noreferrer">space.bilibili.com/404904528/c…</a></p>
<h4 data-id="heading-29">Flutter 实战从零开始 新闻客户端</h4>
<p><a href="https://space.bilibili.com/404904528/channel/detail?cid=106755" target="_blank" rel="nofollow noopener noreferrer">space.bilibili.com/404904528/c…</a></p>
<h4 data-id="heading-30">Flutter 组件开发</h4>
<p><a href="https://space.bilibili.com/404904528/channel/detail?cid=144262" target="_blank" rel="nofollow noopener noreferrer">space.bilibili.com/404904528/c…</a></p>
<h4 data-id="heading-31">Flutter Bloc</h4>
<p><a href="https://space.bilibili.com/404904528/channel/detail?cid=177519" target="_blank" rel="nofollow noopener noreferrer">space.bilibili.com/404904528/c…</a></p>
<h4 data-id="heading-32">Flutter Getx4</h4>
<p><a href="https://space.bilibili.com/404904528/channel/detail?cid=177514" target="_blank" rel="nofollow noopener noreferrer">space.bilibili.com/404904528/c…</a></p>
<h4 data-id="heading-33">Docker Yapi</h4>
<p><a href="https://space.bilibili.com/404904528/channel/detail?cid=130578" target="_blank" rel="nofollow noopener noreferrer">space.bilibili.com/404904528/c…</a></p></div>  
</div>
            