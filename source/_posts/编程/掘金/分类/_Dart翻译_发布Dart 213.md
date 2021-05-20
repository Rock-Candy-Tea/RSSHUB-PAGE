
---
title: '_Dart翻译_发布Dart 2.13'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/d8caa1bebf6741529ef0691860e91068~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Wed, 19 May 2021 18:41:00 GMT
thumbnail: 'https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/d8caa1bebf6741529ef0691860e91068~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>新的类型别名语言功能，改进的Dart FFI</p>
<blockquote>
<p>原文地址：<a href="https://medium.com/dartlang/announcing-dart-2-13-c6d547b57067" target="_blank" rel="nofollow noopener noreferrer">medium.com/dartlang/an…</a></p>
<p>原文作者：<a href="https://medium.com/@mit.mit" target="_blank" rel="nofollow noopener noreferrer">medium.com/@mit.mit</a></p>
<p>发布时间：2021年5月20日 - 8分钟阅读</p>
</blockquote>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/d8caa1bebf6741529ef0691860e91068~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>作者：Kevin Moore和Michael Thomsen</p>
<p>今天，我们发布了Dart 2.13，其特点是类型别名--目前我们要求的第二大语言功能。Dart 2.13还包括改进的DFI和更好的性能，我们还为Dart提供了新的Docker官方图像。这篇文章给出了2.12版本中引入的空值安全功能的更新，讨论了2.13版本的新功能，有一些关于Docker和谷歌云对Dart后端支持的令人兴奋的消息，并预览了一些你可以在未来版本中看到的变化。</p>
<h1 data-id="heading-0">空值安全更新</h1>
<p>我们在3月份的<a href="https://medium.com/dartlang/announcing-dart-2-12-499a6e689c87" target="_blank" rel="nofollow noopener noreferrer">Dart 2.12</a>版本中推出了<a href="https://dart.dev/null-safety" target="_blank" rel="nofollow noopener noreferrer">完善的空值安全</a>。空值安全是Dart最新的主要生产力特性，旨在帮助你避免空值错误--一类通常难以发现的错误。随着该版本的发布，我们鼓励软件包发布者开始将pub.dev上的共享软件包迁移到null safety。</p>
<p>我们非常高兴地看到null safety被采用的速度之快 仅仅在推出几个月后，pub.dev上最受欢迎的前500个软件包中的93%已经支持null safety。我们要对所有软件包的开发者表示衷心的感谢，感谢他们这么快就完成了这项工作，并帮助整个生态系统向前发展!</p>
<p>有了这么多支持null safety的软件包，你很有可能开始将你的应用程序迁移到使用null safety。第一步是使用dart pub outdated来检查你的应用程序的依赖性。详情请见<a href="https://dart.dev/null-safety/migration-guide#step1-wait" target="_blank" rel="nofollow noopener noreferrer">null safety迁移指南</a>。我们还修改了dart创建和flutter创建模板，使它们现在在新的应用和包中默认启用null safety。</p>
<h1 data-id="heading-1">宣布类型别名</h1>
<p>类型别名是2.13语言的一个新特性。它扩展了我们早期的支持，即允许创建函数类型的类型别名，但不包括任何其他类型。这个备受追捧的功能是语言问题跟踪器中<a href="https://github.com/dart-lang/language/issues?q=is%3Aissue+is%3Aopen+sort%3Areactions-%2B1-desc" target="_blank" rel="nofollow noopener noreferrer">第二高</a>的评价。</p>
<p>使用一个类型别名，你可以为任何现有的类型创建一个新的名字，然后可以在任何可以使用原始类型的地方使用。你并没有真正定义一个新的类型，只是引入了一个简短的别名。这个别名甚至可以通过类型平等测试。</p>
<pre><code class="hljs language-dart copyable" lang="dart"><span class="hljs-keyword">typedef</span> Integer = <span class="hljs-built_in">int</span>;
<span class="hljs-keyword">void</span> main() &#123;
  <span class="hljs-built_in">print</span>(<span class="hljs-built_in">int</span> == Integer); <span class="hljs-comment">// true</span>
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>那么你可以用类型别名做什么呢？一个常见的用途是给一个类型起一个更短或更具描述性的名字，使你的代码更容易阅读和维护。</p>
<p>一个很好的例子是处理JSON（感谢GitHub用户<a href="https://github.com/Levi-Lesches" target="_blank" rel="nofollow noopener noreferrer">Levi-Lesches</a>提供这个例子）。在这里我们可以定义一个新的类型别名Json，它将JSON文档描述为一个从String键到任何值的映射（使用动态类型）。然后我们可以在定义fromJson命名的构造函数和json获取器时使用这个Json类型别名。</p>
<pre><code class="hljs language-dart copyable" lang="dart"><span class="hljs-keyword">typedef</span> Json = <span class="hljs-built_in">Map</span><<span class="hljs-built_in">String</span>, <span class="hljs-built_in">dynamic</span>>;
<span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">User</span> </span>&#123;
  <span class="hljs-keyword">final</span> <span class="hljs-built_in">String</span> name;
  <span class="hljs-keyword">final</span> <span class="hljs-built_in">int</span> age;
  User.fromJson(Json json) :
    name = json[<span class="hljs-string">'name'</span>],
    age = json[<span class="hljs-string">'age'</span>];
Json <span class="hljs-keyword">get</span> json => &#123;
    <span class="hljs-string">'name'</span>: name,
    <span class="hljs-string">'age'</span>: age,
  &#125;;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>你也可以在一个命名为类的类型别名上调用构造函数，所以下面的做法是完全合法的。</p>
<pre><code class="hljs language-dart copyable" lang="dart">main() &#123;
  <span class="hljs-keyword">var</span> j = Json();
  j[<span class="hljs-string">'name'</span>] = <span class="hljs-string">'Michael'</span>;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>通过使用类型别名来给复杂的类型命名，你可以让读者更容易理解你的代码的不变性。例如，下面的代码定义了一个类型别名来描述包含通用类型X的键和<code>List<X></code>类型的值的地图。通过给类型一个带有单个类型参数的名称，地图的规则结构对代码的读者来说变得更加明显。</p>
<pre><code class="hljs language-dart copyable" lang="dart"><span class="hljs-keyword">typedef</span> MapToList<X> = <span class="hljs-built_in">Map</span><X, <span class="hljs-built_in">List</span><X>>;
<span class="hljs-keyword">void</span> main() &#123;
  MapToList<<span class="hljs-built_in">int</span>> m = &#123;&#125;;
  m[<span class="hljs-number">7</span>] = [<span class="hljs-number">7</span>]; <span class="hljs-comment">// OK</span>
  m[<span class="hljs-number">8</span>] = [<span class="hljs-number">2</span>, <span class="hljs-number">2</span>, <span class="hljs-number">2</span>]; <span class="hljs-comment">// OK</span>
  <span class="hljs-keyword">for</span> (<span class="hljs-keyword">var</span> x <span class="hljs-keyword">in</span> m.keys) &#123;
    <span class="hljs-built_in">print</span>(<span class="hljs-string">'<span class="hljs-subst">$x</span> --> <span class="hljs-subst">$&#123;m[x]&#125;</span>'</span>);
  &#125;
&#125;

=>

<span class="hljs-number">7</span> --> [<span class="hljs-number">7</span>]
<span class="hljs-number">8</span> --> [<span class="hljs-number">2</span>, <span class="hljs-number">2</span>, <span class="hljs-number">2</span>]
<span class="copy-code-btn">复制代码</span></code></pre>
<p>如果你试图使用不匹配的类型，你会得到一个分析错误。</p>
<pre><code class="copyable">m[42] = ['The', 'meaning', 'of', 'life'];

=>

The element type 'String' can't be assigned to the list type 'int'.
<span class="copy-code-btn">复制代码</span></code></pre>
<p>你甚至可以在公共库中重命名类时使用类型别名。想象一下，你在公共图书馆中有一个现有的类PoorlyNamedClass，你想把它重命名为BetterNamedClass。如果你简单地重命名这个类，那么你的API客户会突然出现编译错误。通过类型别名，你可以继续做重命名，但是要为旧的类名定义一个新的类型别名，然后为旧名添加@Deprecated注释。在使用PoorlyNamedClass时，会引起警告，但会继续编译并像以前一样工作，给用户时间来升级他们的代码。
下面是你如何实现BetterNamedClass并废除PoorlyNamedClass的方法（在一个名为mylibrary.dart的文件中）。</p>
<pre><code class="hljs language-dart copyable" lang="dart"><span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">BetterNamedClass</span> </span>&#123;...&#125;

<span class="hljs-meta">@Deprecated</span>(<span class="hljs-string">'Use BetterNamedClass instead'</span>)
<span class="hljs-keyword">typedef</span> PoorlyNamedClass = BetterNamedClass;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>下面是有人试图使用PoorlyNamedClass时的情况。</p>
<pre><code class="hljs language-dart copyable" lang="dart"><span class="hljs-keyword">import</span> <span class="hljs-string">'mylibrary.dart'</span>;
<span class="hljs-keyword">void</span> main() &#123;
  PoorlyNamedClass p;
&#125;

=>

<span class="hljs-string">'PoorlyNamedClass'</span> <span class="hljs-keyword">is</span> deprecated and shouldn<span class="hljs-string">'t be used. Use BetterNamedClass instead.
</span><span class="copy-code-btn">复制代码</span></code></pre>
<p>类型别名功能从Dart 2.13开始可用。要启用它，请在你的pubspec中把Dart SDK的下级约束设置为至少2.13。</p>
<pre><code class="hljs language-yaml copyable" lang="yaml"><span class="hljs-attr">environment:</span>
  <span class="hljs-attr">sdk:</span> <span class="hljs-string">">=2.13.0 <3.0.0"</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这个功能是向后兼容的，这要归功于<a href="https://dart.dev/guides/language/evolution#language-versioning" target="_blank" rel="nofollow noopener noreferrer">语言版本划分</a>。2.13版本下SDK约束较低的包可以安全地引用2.13版本包中定义的类型别名，尽管2.13之前的包不能定义自己的类型别名。</p>
<h1 data-id="heading-2">Dart 2.13 FFI的变化</h1>
<p>我们在Dart FFI中也有一些新功能，这是我们调用C代码的互操作机制。</p>
<p>首先，FFI现在支持有内联数组的结构（<a href="https://github.com/dart-lang/sdk/issues/35763" target="_blank" rel="nofollow noopener noreferrer">#35763</a>）。考虑一个带有内联数组的C结构，像这样。</p>
<pre><code class="hljs language-dart copyable" lang="dart">struct MyStruct &#123;
  uint8_t arr[<span class="hljs-number">8</span>];
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>现在你可以直接用Dart包装，用Array的类型参数来指定元素类型。</p>
<pre><code class="hljs language-dart copyable" lang="dart"><span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">StructInlineArray</span> <span class="hljs-keyword">extends</span> <span class="hljs-title">Struct</span> </span>&#123;
  <span class="hljs-meta">@Array</span>(<span class="hljs-number">8</span>)
  <span class="hljs-keyword">external</span> Array<Uint8> arr;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>第二，FFI现在支持打包结构（<a href="https://github.com/dart-lang/sdk/issues/38158" target="_blank" rel="nofollow noopener noreferrer">#38158</a>）。通常情况下，结构体在内存中的布局是为了让成员落在CPU更容易访问的地址边界上。在<a href="http://www.catb.org/esr/structure-packing/" target="_blank" rel="nofollow noopener noreferrer">打包结构</a>中，部分填充被省略，以降低整体内存消耗，通常是以特定平台的方式。通过新的<code>@Packed(<alignment>)</code>注解，你可以轻松地指定填充。例如，下面的代码创建了一个在内存中具有4字节对齐的结构。</p>
<pre><code class="hljs language-dart copyable" lang="dart"><span class="hljs-meta">@Packed</span>(<span class="hljs-number">4</span>)
<span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">TASKDIALOGCONFIG</span> <span class="hljs-keyword">extends</span> <span class="hljs-title">Struct</span> </span>&#123;
  <span class="hljs-meta">@Uint</span>32()
  <span class="hljs-keyword">external</span> <span class="hljs-built_in">int</span> cbSize;
  <span class="hljs-meta">@IntPtr</span>()
  <span class="hljs-keyword">external</span> <span class="hljs-built_in">int</span> hwndParent;
  <span class="hljs-meta">@IntPtr</span>()
  <span class="hljs-keyword">external</span> <span class="hljs-built_in">int</span> hInstance;
  <span class="hljs-meta">@Uint</span>32()
  <span class="hljs-keyword">external</span> <span class="hljs-built_in">int</span> dwFlags;
  ...
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h1 data-id="heading-3">Dart 2.13的性能变化</h1>
<p>我们正在继续努力减少Dart代码的应用大小和内存占用。在大型Flutter应用程序中，代表AOT编译的Dart程序元数据的内部结构可能会占据相当大的内存块。这些元数据的存在是为了实现热重载、交互式调试和人类可读堆栈痕迹的格式化等功能，这些功能在部署的应用程序中从未使用过。在过去的一年里，我们一直在重组Dart本地运行时，以尽可能地消除这种开销。其中一些改进适用于在发布模式下构建的所有Flutter应用程序，但也有一些需要你通过使用<a href="https://flutter.dev/docs/perf/app-size#reducing-app-size" target="_blank" rel="nofollow noopener noreferrer">--split-debug-info</a>标志将调试信息从AOT编译的应用程序中分割出来，从而放弃人类可读的堆栈跟踪。</p>
<p>Dart 2.13包括一些变化，在使用--split-debug-info时，大大减少了程序元数据占用的空间。以Flutter Gallery应用程序为例。在Android上，发布的APK是112.4MB，包含调试信息，而不包含106.7MB（总体减少5%）。这个APK包含大量的资产。仅看APK内的代码元数据，它从Dart 2.12的5.7MB减少到Dart 2.13的只有3.7MB（减少35%）。</p>
<p>如果应用程序的大小和内存占用对你来说很重要，可以考虑使用--split-debug-info标志来省略调试信息。请注意，这样做的时候，你需要使用<a href="https://flutter.dev/docs/deployment/obfuscate#reading-an-obfuscated-stack-trace" target="_blank" rel="nofollow noopener noreferrer">symbolize</a>命令，使堆栈痕迹重新成为可读的人类。</p>
<h1 data-id="heading-4">官方Docker支持和谷歌云上的Dart</h1>
<p>Dart现在可以作为<a href="https://docs.docker.com/docker-hub/official_images/" target="_blank" rel="nofollow noopener noreferrer">Docker官方图像</a>使用。虽然Dart已经提供了多年的Docker镜像，但这些<a href="https://hub.docker.com/_/dart" target="_blank" rel="nofollow noopener noreferrer">新的Dart镜像</a>是由Docker测试和验证的，遵循最佳实践。它们还支持提前编译（AOT），这可以大大减少构建的容器的大小，并可以提高容器环境中的部署速度--比如<a href="https://cloud.google.com/run" target="_blank" rel="nofollow noopener noreferrer">Cloud Run</a>。</p>
<p>虽然Dart仍然专注于使Flutter等应用框架能够在每个屏幕上驱动美丽的像素，但我们意识到，大多数用户体验的背后至少有一个托管服务。通过让Dart轻松构建后端服务，我们支持全栈体验，让开发者使用与前端小部件相同的语言和业务逻辑，将他们的应用扩展到云端。</p>
<p>一般来说，将Dart用于Flutter应用程序的后端，特别适合谷歌管理的无服务器平台Cloud Run的简单性和可扩展性。这包括零扩展，这意味着当你的后端不处理任何请求时，你不会产生成本。我们与谷歌云团队合作，提供<a href="https://pub.dev/packages/functions_framework" target="_blank" rel="nofollow noopener noreferrer">Dart的函数框架</a>，这是一个软件包、工具和例子的集合，可以轻松地编写Dart函数来部署，而不是处理HTTP请求和CloudEvents的完整服务器。</p>
<p>请查看我们的<a href="https://dart.dev/server/google-cloud" target="_blank" rel="nofollow noopener noreferrer">谷歌云文档</a>以开始使用。</p>
<h1 data-id="heading-5">关于下一步的工作，请说几句</h1>
<p>我们已经在为即将发布的版本做一些令人兴奋的改变。一如既往，你可以使用<a href="https://github.com/dart-lang/language/projects/1" target="_blank" rel="nofollow noopener noreferrer">语言漏斗跟踪器</a>来关注我们的进展。</p>
<p>我们正在努力的一个领域是为Dart和Flutter提供一套新的规范线。Lints是配置Dart<a href="https://dart.dev/guides/language/analysis-options" target="_blank" rel="nofollow noopener noreferrer">静态分析</a>的一种强大方式，但由于有数百种可能的lints可以开启或关闭，很难决定选择什么。我们目前正在努力定义两套典型的衬垫，我们将在Dart和Flutter项目中默认应用。我们希望在下一个稳定版中默认启用。如果你想预览一下，请查看<a href="https://pub.dev/packages/lints" target="_blank" rel="nofollow noopener noreferrer">lints</a>和<a href="https://pub.dev/packages/flutter_lints" target="_blank" rel="nofollow noopener noreferrer">flutter_lints</a>这两个包。</p>
<p>最后，如果你对Dart VM运行时进行深度嵌入，请注意，我们正计划废除现有的机制。我们将用一个基于Dart FFI的更快、更灵活的模型来取代它（见追踪问题<a href="https://github.com/dart-lang/sdk/issues/45451" target="_blank" rel="nofollow noopener noreferrer">#45451</a>）。</p>
<h1 data-id="heading-6">Dart 2.13现在已经推出</h1>
<p>带有类型别名和改进的FFI的Dart 2.13今天可以在<a href="https://dart.dev/get-dart" target="_blank" rel="nofollow noopener noreferrer">Dart 2.13</a>和<a href="https://flutter.dev/docs/get-started/" target="_blank" rel="nofollow noopener noreferrer">Flutter 2.2</a> SDKs中使用。
如果你一直在等待你的依赖关系迁移到null safety，你可能想再次检查，使用dart pub outdated。在前500个最受欢迎的软件包中，有93%已经迁移了，所以你很有可能已经解禁了。我们也要向已经迁移的开发者表示感谢！我们很想听听你们的意见。
我们很想听听你对这篇博文中讨论的新功能和变化的体验。请在下面留言或发推特<a href="https://twitter.com/dart_lang" target="_blank" rel="nofollow noopener noreferrer">@dart_lang</a>。</p>
<hr>
<p>通过www.DeepL.com/Translator（免费版）翻译</p></div>  
</div>
            