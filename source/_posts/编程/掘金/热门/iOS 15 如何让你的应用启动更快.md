
---
title: 'iOS 15 如何让你的应用启动更快'
categories: 
 - 编程
 - 掘金
 - 热门
headimg: 'https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/e9e9e695737c4806aaeee8392cf97c82~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Sun, 27 Jun 2021 23:56:39 GMT
thumbnail: 'https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/e9e9e695737c4806aaeee8392cf97c82~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><blockquote>
<p>这是一篇来自 Noah Martin 的文章，作者发现了 WWDC2021 中没有被提及的一处改动，却能够帮助你的 App 在 iOS15 上运行的更快。</p>
</blockquote>
<p>WWDC21 上最吸引人的功能被深埋在 Xcode 13 的发布说明中。</p>
<blockquote>
<p>所有以 macOS 12 或 iOS 15 及更高部署目标构建的程序和 dylibs 现在都使用新的链式 fixups 格式。这种新的格式使用了不同的加载命令和 LINKEDIT 数据，并且不会在旧的操作系统版本上运行或加载。</p>
</blockquote>
<p>没有任何文档或会议来了解这一变化，但我们可以通过逆向工程来了解苹果在新操作系统上的不同做法，以及它是否会优化你的应用程序。</p>
<p>首先，介绍一下控制应用程序启动的程序，即 dyld 的背景。</p>
<h2 data-id="heading-0">认识dyld</h2>
<p>动态链接器（dyld）是每个应用程序的入口点。它负责让你的代码准备好运行，所以对 dyld 的任何改进都会改善应用程序的启动时间。在调用 main 、运行静态初始化方法或设置 Objective-C 运行时之前，dyld 会进行 fixups 工作。这包括 rebase 和 bind 操作，这些操作修改了应用程序二进制文件中的指针，以保证在运行时所有地址的有效性。要查看这些操作，你可以使用 dyldinfo 命令行工具。</p>
<pre><code class="hljs language-c copyable" lang="c">% xcrun dyldinfo -rebase -bind Snapchat.app/<span class="hljs-function">Snapchat
rebase <span class="hljs-title">information</span> <span class="hljs-params">(from compressed dyld info)</span>:
segment section          address     type
__DATA  __got            0x10748C0C8  pointer
...
bind information:
segment section address     type    addend dylib        symbol
__DATA  __const 0x107595A70 pointer 0      libswiftCore _$sSHMp
</span><span class="copy-code-btn">复制代码</span></code></pre>
<p>上面的结果意味着地址 <code>0x10748C0C8</code> 位于 <code>__DATA/__got</code> 中，需要移位一个常量值（被称为滑动 slide ）。而地址 <code>0x107595A70</code> 位于 <code>__DATA/__const</code> ，应该指向 libswiftCore.dylib 中的一个 Hashable[1] 的协议描述符</p>
<p>dyld 使用 <code>LC_DYLD_INFO</code> 加载命令和 <code>dyld_info_command</code> 结构来确定二进制文件中 rebase 、bind 和导出符号[2]的位置和大小。<a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.emergetools.com" target="_blank" rel="nofollow noopener noreferrer" title="https://www.emergetools.com" ref="nofollow noopener noreferrer">Emerge</a>（免责声明：是一个可以查看 App 包二进制大小和分布的软件，本文的作者就是作者😬）对这些数据进行分析，让你直观地了解它们对二进制文件大小的贡献，并能提供建议，使用链接器标志使其更小。</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/e9e9e695737c4806aaeee8392cf97c82~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-1">一个新的格式</h2>
<p>当我第一次将一个为 iOS 15 构建的应用程序导入到 Emerge 时，软件没有展示出可视化的 dyld fixups 。这是因为 <code>LC_DYLD_INFO_ONLY</code> 加载命令不见了，它被 <code>LC_DYLD_CHAINED_FIXUPS</code> 和 <code>LC_DYLD_EXPORTS_TRIE</code> 取代。</p>
<pre><code class="hljs language-c copyable" lang="c">% otool -l iOS14Example.app/iOS14Example | grep LC_DYLD
      cmd LC_DYLD_INFO_ONLY
% otool -l iOS15Example.app/iOS15Example | grep LC_DYLD
      cmd LC_DYLD_CHAINED_FIXUPS
      cmd LC_DYLD_EXPORTS_TRIE
<span class="copy-code-btn">复制代码</span></code></pre>
<p>输出的数据和以前的完全一样，是一个三段式结构，每个节点代表一个符号名称的一部分。</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/96306d026caf4f87b43e732e5dbd1a08~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer">
在 iOS 15 中唯一的变化是数据现在由 <code>linkedit_data_command</code> 引用，这个结构中包含了第一个节点的偏移量。为了验证这一点，我写了一个简短的 Swift 应用程序来解析 iOS 15 的二进制文件并打印每个符号。</p>
<pre><code class="hljs language-swift copyable" lang="swift"><span class="hljs-keyword">let</span> bytes <span class="hljs-operator">=</span> (<span class="hljs-keyword">try!</span> <span class="hljs-type">Data</span>(contentsOf: url) <span class="hljs-keyword">as</span> <span class="hljs-type">NSData</span>).bytes
bytes.processLoadComands &#123; load_command, pointer <span class="hljs-keyword">in</span>
  <span class="hljs-keyword">if</span> load_command.cmd <span class="hljs-operator">==</span> <span class="hljs-type">LC_DYLD_EXPORTS_TRIE</span> &#123;
    <span class="hljs-keyword">let</span> dataCommand <span class="hljs-operator">=</span> pointer.load(as: linkedit_data_command.<span class="hljs-keyword">self</span>)
    bytes.advanced(by: <span class="hljs-type">Int</span>(dataCommand.dataoff)).readExportTrie()
  &#125;
&#125;

<span class="hljs-class"><span class="hljs-keyword">extension</span> <span class="hljs-title">UnsafeRawPointer</span> </span>&#123;
  <span class="hljs-function"><span class="hljs-keyword">func</span> <span class="hljs-title">readExportTrie</span>()</span> &#123;
    <span class="hljs-keyword">var</span> frontier <span class="hljs-operator">=</span> readNode(name: <span class="hljs-string">""</span>)
    <span class="hljs-keyword">guard</span> <span class="hljs-operator">!</span>frontier.isEmpty <span class="hljs-keyword">else</span> &#123; <span class="hljs-keyword">return</span> &#125;

    <span class="hljs-keyword">repeat</span> &#123;
      <span class="hljs-keyword">let</span> (<span class="hljs-keyword">prefix</span>, offset) <span class="hljs-operator">=</span> frontier.removeFirst()
      <span class="hljs-keyword">let</span> children <span class="hljs-operator">=</span> advanced(by: <span class="hljs-type">Int</span>(offset)).readNode(name: <span class="hljs-keyword">prefix</span>)
      <span class="hljs-keyword">for</span> (suffix, offset) <span class="hljs-keyword">in</span> children &#123;
        frontier.append((<span class="hljs-keyword">prefix</span> <span class="hljs-operator">+</span> suffix, offset))
      &#125;
    &#125; <span class="hljs-keyword">while</span> <span class="hljs-operator">!</span>frontier.isEmpty
  &#125;

  <span class="hljs-comment">// Returns an array of child nodes and their offset</span>
  <span class="hljs-function"><span class="hljs-keyword">func</span> <span class="hljs-title">readNode</span>(<span class="hljs-params">name</span>: <span class="hljs-type">String</span>)</span> -> [(<span class="hljs-type">String</span>, <span class="hljs-type">UInt</span>)] &#123;
    <span class="hljs-keyword">guard</span> load(as: <span class="hljs-type">UInt8</span>.<span class="hljs-keyword">self</span>) <span class="hljs-operator">==</span> <span class="hljs-number">0</span> <span class="hljs-keyword">else</span> &#123;
      <span class="hljs-comment">// This is a terminal node</span>
      <span class="hljs-built_in">print</span>(<span class="hljs-string">"symbol name <span class="hljs-subst">\(name)</span>"</span>)
      <span class="hljs-keyword">return</span> []
    &#125;
    <span class="hljs-keyword">let</span> numberOfBranches <span class="hljs-operator">=</span> <span class="hljs-type">UInt</span>(advanced(by: <span class="hljs-number">1</span>).load(as: <span class="hljs-type">UInt8</span>.<span class="hljs-keyword">self</span>))
    <span class="hljs-keyword">var</span> mutablePointer <span class="hljs-operator">=</span> <span class="hljs-keyword">self</span>.advanced(by: <span class="hljs-number">2</span>)
    <span class="hljs-keyword">var</span> result <span class="hljs-operator">=</span> [(<span class="hljs-type">String</span>, <span class="hljs-type">UInt</span>)]()
    <span class="hljs-keyword">for</span> <span class="hljs-keyword">_</span> <span class="hljs-keyword">in</span> <span class="hljs-number">0</span><span class="hljs-operator">..<</span>numberOfBranches &#123;
      result.append(
        (mutablePointer.readNullTerminatedString(),
         mutablePointer.readULEB()))
    &#125;
    <span class="hljs-keyword">return</span> result
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-2">链式</h2>
<p>真正的变化是在 <code>LC_DYLD_CHAINED_FIXUPS</code> 。在 iOS 15 之前，rebase、bind 和lazy bind 各自存储在一个单独的表中。现在它们被合并成链，链的起点指针包含在这个新的加载命令中。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/f2976bbec69f4aedb5ab852bbdcef6a4~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer">
应用程序的二进制文件被分成几个部分，每个部分都包含一连串的 fixups ，这些 fixups 可以是bind 或 rebase（不再有 lazy binds ）。二进制文件中的每个64位 rebase[3] 位置现在都编码了它所指向的偏移量以及下一个 ccc 的偏移量，如这个结构所见。</p>
<pre><code class="hljs language-c copyable" lang="c"><span class="hljs-class"><span class="hljs-keyword">struct</span> <span class="hljs-title">dyld_chained_ptr_64_rebase</span>
&#123;</span>
<span class="hljs-keyword">uint64_t</span>    target    : <span class="hljs-number">36</span>,
            high8     :  <span class="hljs-number">8</span>,
            reserved  :  <span class="hljs-number">7</span>,    <span class="hljs-comment">// 0s</span>
            next      : <span class="hljs-number">12</span>,
            bind      :  <span class="hljs-number">1</span>;    <span class="hljs-comment">// Always 0 for a rebase</span>
&#125;;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>36位用于指针 target ，足以满足 2³⁶ = 64GB 的二进制，12位用于提供下一个 fixup 的偏移量（stride = 4）。因此，它可以指向 2¹² * 4 = 16kb 内的任何地方--正好是 iOS 上的 page 大小。</p>
<p>这种非常紧凑的编码意味着遍历链的整个过程就可以覆盖整个二进制文件。在我的测试中，超过 50% 的 dyld 都能够被新的格式系统优化并最终减少二进制包的大小，只有少量的元数据被保留下来以引导每个 page 的第一次 fixup 。最终的结果是，大型 Swift 应用程序的大小减少了 1mb 以上。</p>
<p>这个过程的源代码在 MachOLoaded.cpp 中，二进制布局在 /usr/include/macho-o/fixup-chains.h 中。</p>
<h2 data-id="heading-3">顺序问题</h2>
<p>为了理解新 fixup 格式背后的动机，我们必须了解应用程序启动期间最昂贵的操作之一： page fault 。当应用程序启动过程中访问文件系统中的代码时，需要通过一个 page fault 将其从磁盘文件中带入内存。应用程序二进制文件中的每个 16kb 范围都被映射到内存中的一个页面。一旦页面被修改，只要应用程序不停止，它就需要留在 RAM 中（称为 dirty page）。iOS 通过压缩最近没有使用的页面来优化 dirty page。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/1e2d2dafe8a74e7b9bdcb8d304e84149~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer">
应用程序启动时的 fixup 需要改变应用程序二进制中的地址，因此整个 page 都不可避免被标记为 dirty。让我们看看在应用启动时有多少页面被 fixups。</p>
<pre><code class="hljs language-c copyable" lang="c">% xcrun dyldinfo -rebase Snapchat.app/Snapchat > rebases
% ruby -e <span class="hljs-string">'puts IO.read("rebases").split("\n").drop(2).map &#123; |a| a.split(" ")[2].to_i(16) / 16384 &#125;.uniq.count'</span>
<span class="hljs-number">1554</span>
% xcrun dyldinfo -bind Snapchat.app/Snapchat > binds
<span class="hljs-number">450</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>当使用表结构存储 fixup 数据时，首先需要解决 rebase ，然后是 bind 。这意味着 rebase 需要很多 page fault ，并且最终大部分是 IO 绑定[4]。另一方面，bind 所访问的 page 是 rebase 所使用的 page 的 30%。</p>
<p>而现在，在 iOS 15 中，链式 fixups 将每个内存 page 的所有变化合并在一起。 Dyld 现在可以更快地处理它们，只需调整一次内存，就可以同时完成 rebase 和 bind 。这使得像内存压缩器这样的操作系统功能可以利用链式 fixups 中的信息，不需要在 bind 过程中回去解压旧 page 。由于这些变化，dyld 中的 rebase 功能变成了一个无用的功能。
<img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/f8e858d87bc148278ebd413f9dcb2488~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer">
总的来说，这一变化主要影响到的是 iOS 应用程序的逆向工程和探索动态链接器的细节，但它很好地提醒了影响你的应用程序性能的低层次内存管理。虽然这一变化只在你以 iOS 15 为目标时生效，但请记住，你仍然可以做很多事情来优化应用程序的启动时间。</p>
<ul>
<li>减少动态框架的数量</li>
<li>减少应用程序的大小，以减少内存页的使用（这就是作者制作 Emerge 的原因！）。</li>
<li>将代码从 <code>+load</code> 和静态初始化器中移出</li>
<li>使用更少的类</li>
<li>将工作推迟到绘制第一帧之后</li>
</ul>
<blockquote>
<p>[1] dyldinfo 的符号被篡改了，你可以用 xcrun swift-demangle '_$sSHMp' 获得人类可读的名称。</p>
<p>[2] 导出是 bind 的第二部分。一个二进制文件会与从其依赖关系中导出的符号绑定。</p>
<p>[3] bind 也是如此，一个指针实际上是 rebase 和 bind（ <code>dyld_chained_ptr_64_bind</code> ）的联合体，用一个位来区分这两者。bind 也需要导入符号名，这里不作讨论。</p>
<p>[4] <a href="https://link.juejin.cn/?target=https%3A%2F%2Fasciiwwdc.com%2F2016%2Fsessions%2F406" target="_blank" rel="nofollow noopener noreferrer" title="https://asciiwwdc.com/2016/sessions/406" ref="nofollow noopener noreferrer">asciiwwdc.com/2016/sessio…</a></p>
</blockquote>
<blockquote>
<p>原文： <a href="https://link.juejin.cn/?target=https%3A%2F%2Fmedium.com%2Fgeekculture%2Fhow-ios-15-makes-your-app-launch-faster-51cf0aa6c520" target="_blank" rel="nofollow noopener noreferrer" title="https://medium.com/geekculture/how-ios-15-makes-your-app-launch-faster-51cf0aa6c520" ref="nofollow noopener noreferrer">How iOS 15 makes your app launch faster</a></p>
</blockquote></div>  
</div>
            