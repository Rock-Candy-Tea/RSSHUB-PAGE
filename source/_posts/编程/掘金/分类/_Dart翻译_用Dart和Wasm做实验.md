
---
title: '_Dart翻译_用Dart和Wasm做实验'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/42e5e650bafb4484b2eabbd2e0408007~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Tue, 27 Jul 2021 21:49:15 GMT
thumbnail: 'https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/42e5e650bafb4484b2eabbd2e0408007~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>将Dart编译为Wasm，并从Dart调用Wasm模块</p>
<blockquote>
<p>原文地址：<a href="https://link.juejin.cn/?target=https%3A%2F%2Fmedium.com%2Fdartlang%2Fexperimenting-with-dart-and-wasm-ef7f1c065577" target="_blank" rel="nofollow noopener noreferrer" title="https://medium.com/dartlang/experimenting-with-dart-and-wasm-ef7f1c065577" ref="nofollow noopener noreferrer">medium.com/dartlang/ex…</a></p>
<p>原文作者：<a href="https://link.juejin.cn/?target=https%3A%2F%2Fmedium.com%2F%40mit.mit" target="_blank" rel="nofollow noopener noreferrer" title="https://medium.com/@mit.mit" ref="nofollow noopener noreferrer">medium.com/@mit.mit</a></p>
<p>发布时间：2021年7月28日 - 8分钟阅读</p>
</blockquote>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fwebassembly.org%2F" target="_blank" rel="nofollow noopener noreferrer" title="https://webassembly.org/" ref="nofollow noopener noreferrer">WebAssembly</a>（通常缩写为Wasm）是 "一种基于堆栈的虚拟机的二进制指令格式"。虽然Wasm最初是为在网络上运行本地代码而设计的，但后来Wasm已经发展成为一种在多个平台上运行编译代码的通用技术。Dart已经是一个高度可移植和多平台的语言，所以我们对Wasm如何使我们扩展Dart的这些品质非常感兴趣。</p>
<h1 data-id="heading-0">为什么要用Wasm做实验？</h1>
<p>Wasm已经获得了浏览器供应商的<a href="https://link.juejin.cn/?target=https%3A%2F%2Fwebassembly.org%2Froadmap%2F" target="_blank" rel="nofollow noopener noreferrer" title="https://webassembly.org/roadmap/" ref="nofollow noopener noreferrer">广泛支持</a>，如Chrome, Edge, Firefox和WebKit。这使得Wasm在浏览器中运行二进制代码的前景非常有趣。然而，最初Wasm并不是为具有垃圾收集（GC）的编程语言而设计的，如Dart和Java/Kotlin，这使得有效地将基于GC的语言编译到Wasm中很困难。通过参与Wasm项目最近的<a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2FWebAssembly%2Fgc%2Fblob%2Fmaster%2FREADME.md" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/WebAssembly/gc/blob/master/README.md" ref="nofollow noopener noreferrer">GC提案</a>，我们希望既能对提案提供技术反馈，又能更多地了解我们通过Wasm代码运行基于Dart的网络应用可能获得的收益。</p>
<p>Wasm的第二个特点是，二进制Wasm模块是独立于平台的。这有可能使与现有代码的互操作性更加实用：如果现有的代码可以被编译为Wasm，那么所有平台的Dart应用程序可以依赖于一个单一的，共享的二进制Wasm模块。</p>
<p>在这篇文章的其余部分，我们将讨论我们对Wasm和Dart两种形式的实验。</p>
<ol>
<li>Dart到Wasm的编译。扩展我们的AOT编译器，支持将Dart源代码编译为Wasm二进制代码（问题<a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fdart-lang%2Fsdk%2Fissues%2F32894" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/dart-lang/sdk/issues/32894" ref="nofollow noopener noreferrer">32894</a>）。</li>
<li>Dart to Wasm interop: 支持从Dart代码到编译的Wasm模块的调用（问题<a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fdart-lang%2Fsdk%2Fissues%2F37355" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/dart-lang/sdk/issues/37355" ref="nofollow noopener noreferrer">37355</a>和<a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fdart-lang%2Fsdk%2Fissues%2F37882" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/dart-lang/sdk/issues/37882" ref="nofollow noopener noreferrer">37882</a>）。</li>
</ol>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/42e5e650bafb4484b2eabbd2e0408007~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<blockquote>
<p>说明Wasm与Dart的两种潜在用途</p>
</blockquote>
<h1 data-id="heading-1">编译Dart到Wasm</h1>
<p>如前所述，Wasm起源于一种在网络上运行本地代码的方式。传统上，网络是由JavaScript代码驱动的，这些代码在虚拟机（VM）中运行，在网络应用程序运行的同时，对JavaScript代码进行及时（JIT）编译为本地代码。在目前针对网络的Dart框架中，如<a href="https://link.juejin.cn/?target=https%3A%2F%2Fflutter.dev%2Fweb" target="_blank" rel="nofollow noopener noreferrer" title="https://flutter.dev/web" ref="nofollow noopener noreferrer">Flutter web</a>，Dart应用代码被编译为<a href="https://link.juejin.cn/?target=https%3A%2F%2Fdart.dev%2Fweb%2Fdeployment" target="_blank" rel="nofollow noopener noreferrer" title="https://dart.dev/web/deployment" ref="nofollow noopener noreferrer">优化</a>的JavaScript，用于部署，然后这些JavaScript在应用运行时被网络平台JIT编译为本地代码。</p>
<p>我们正在研究将Dart代码直接编译为Wasm原生代码，看看我们是否可以获得一个更直接的路径来在网络上运行原生代码。Wasm汇编格式是低层次的，比JavaScript更接近机器代码的抽象水平，这导致了启动时间的改善，一般来说，效率更可预测。</p>
<p>Dart对Wasm编译的支持是一个早期阶段的调查，编译器也不完整，但我们正在尝试学习。我们一直对Wasm作为Dart的编译目标感兴趣，但它的原始形式对于有垃圾收集的语言来说并不理想。Wasm缺乏内置的垃圾收集支持，所以像Dart这样的语言必须将垃圾收集的实现包含在编译的Wasm模块中。包括GC的实现将是非常复杂的，会增加编译后的Wasm代码的大小，影响启动时间，并且不能很好地与浏览器系统的其他部分进行对象级互操作。</p>
<p>幸运的是，WebAssembly社区正在进行的一项努力，即<a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2FWebAssembly%2Fgc%2Fblob%2Fmaster%2FREADME.md" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/WebAssembly/gc/blob/master/README.md" ref="nofollow noopener noreferrer">Wasm GC</a>，正在探索扩大Wasm的可能性，对垃圾收集语言提供直接和有效的支持。鉴于我们对Wasm的长期兴趣，我们看到了一个机会，通过编写一个编译器将Dart翻译成Wasm GC，来参与社区并提供真实世界的经验。</p>
<p>现在预测这可能会给我们带来什么还为时过早，但我们最初的原型设计显示了非常积极的结果，最初的基准测试显示了更快的第一帧时间和更快的平均帧时间/吞吐量。如果你有兴趣了解更多关于这个项目的信息，请看一下<a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Faskeksa-google%2Fsdk%2Fblob%2Fwasm_prototype%2Fdart2wasm.md" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/askeksa-google/sdk/blob/wasm_prototype/dart2wasm.md" ref="nofollow noopener noreferrer">wasm_prototype</a>的源代码。</p>
<h1 data-id="heading-2">与Wasm代码的互操作性(package:wasm)</h1>
<p>除了编译到Wasm，我们也有兴趣调查Wasm是否可以用来与现有的代码整合，以一种更跨平台的方式。有几种语言支持编译到遵循C语言调用惯例的模块，有了<a href="https://link.juejin.cn/?target=https%3A%2F%2Fdart.dev%2Fguides%2Flibraries%2Fc-interop" target="_blank" rel="nofollow noopener noreferrer" title="https://dart.dev/guides/libraries/c-interop" ref="nofollow noopener noreferrer">Dart FFI</a>，你就可以与这些模块进行互操作。Dart FFI可以成为利用现有源代码和库的一个好方法，而不是在Dart中重新实现代码。</p>
<p>然而，由于C模块是特定于平台的，分发带有本地C模块的共享包是很复杂的：它需要一个通用的构建系统，或者分发多个二进制模块（每个所需平台一个）。如果一个单一的Wasm二进制汇编格式可以在所有的平台上使用，分发就会容易得多。那么，与其为每个目标平台将你的库编译成特定平台的二进制代码，你可以将它编译成一个Wasm二进制模块并在任何地方运行。这将有可能为在<a href="https://link.juejin.cn/?target=https%3A%2F%2Fpub.dev%2F" target="_blank" rel="nofollow noopener noreferrer" title="https://pub.dev/" ref="nofollow noopener noreferrer">pub.dev</a>上轻松发布包含本地代码的软件包打开大门。</p>
<p>我们正在尝试在一个新的软件包中支持Wasm互操作，即<a href="https://link.juejin.cn/?target=https%3A%2F%2Fpub.dev%2Fpackages%2Fwasm" target="_blank" rel="nofollow noopener noreferrer" title="https://pub.dev/packages/wasm" ref="nofollow noopener noreferrer">package:wasm</a>。这个原型是建立在<a href="https://link.juejin.cn/?target=https%3A%2F%2Fwasmer.io%2F" target="_blank" rel="nofollow noopener noreferrer" title="https://wasmer.io/" ref="nofollow noopener noreferrer">Wasmer</a>运行时上的，它支持<a href="https://link.juejin.cn/?target=https%3A%2F%2Fwasi.dev%2F" target="_blank" rel="nofollow noopener noreferrer" title="https://wasi.dev/" ref="nofollow noopener noreferrer">WASI</a>的操作系统交互。请注意，我们目前的原型是不完整的，只支持桌面平台（Windows、Linux和macOS）。</p>
<h1 data-id="heading-3">例子。调用Brotli压缩库</h1>
<p>让我们看看一个使用package:wasm来利用<a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fgoogle%2Fbrotli" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/google/brotli" ref="nofollow noopener noreferrer">Brotli压缩库</a>的例子，它被编译成一个Wasm模块。在这个例子中，我们将读取一个输入文件，对其进行压缩，报告其压缩率，然后对其进行解压，并验证我们得到的输入。请参阅GitHub repo获取完整的<a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fdart-lang%2Fwasm%2Ftree%2Fmain%2Fexample" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/dart-lang/wasm/tree/main/example" ref="nofollow noopener noreferrer">示例源代码</a>。因为package:wasm是建立在<a href="https://link.juejin.cn/?target=https%3A%2F%2Fdart.dev%2Fguides%2Flibraries%2Fc-interop" target="_blank" rel="nofollow noopener noreferrer" title="https://dart.dev/guides/libraries/c-interop" ref="nofollow noopener noreferrer">dart:ffi</a>之上的，如果你有FFI的经验，你可能会发现这些步骤很熟悉。</p>
<p>有几种将C语言代码编译到Wasm的方法，但在本例中我们使用<a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fwasienv%2Fwasienv" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/wasienv/wasienv" ref="nofollow noopener noreferrer">wasienv</a>。完整的细节可在<a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fdart-lang%2Fwasm%2Fblob%2Fmain%2FREADME.md" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/dart-lang/wasm/blob/main/README.md" ref="nofollow noopener noreferrer">README</a>中找到。</p>
<p>对于这个例子，我们将尝试调用这些Brotli函数来压缩和解压数据。</p>
<pre><code class="hljs language-dart copyable" lang="dart"><span class="hljs-built_in">int</span> BrotliEncoderCompress(
  <span class="hljs-built_in">int</span> quality, <span class="hljs-built_in">int</span> lgwin, <span class="hljs-built_in">int</span> mode, size_t input_size,
  <span class="hljs-keyword">const</span> uint8_t* input_buffer, size_t* output_size,
  uint8_t* output_buffer);
<span class="hljs-built_in">int</span> BrotliDecoderDecompress(
  size_t encoded_size, <span class="hljs-keyword">const</span> uint8_t* encoded_buffer,
  size_t* output_size, uint8_t* output_buffer);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>质量、lgwin和模式参数是编码器的调整参数。细节与本例无关，所以我们只使用这些参数的默认值。另一件要注意的事情是，output_size是一个输入输出参数。当我们调用这些函数时，output_size必须被初始化为我们分配的output_buffer的大小，之后它将被设置为实际使用的缓冲区的数量。</p>
<p>第一步是使用我们编译的Wasm二进制文件来构建一个WasmModule对象。二进制数据应该是一个Uint8List，我们可以通过使用file.readAsBytesSync()从文件中读取它来获得。</p>
<pre><code class="hljs language-dart copyable" lang="dart"><span class="hljs-keyword">var</span> brotliPath = Platform.script.resolve(‘libbrotli.wasm’);
<span class="hljs-keyword">var</span> moduleData = File(brotliPath.path).readAsBytesSync();
<span class="hljs-keyword">var</span> module = WasmModule(moduleData);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>一个非常有用的调试工具是module.describe()，它可以确保我们的Wasm模块具有我们期望的API。这将返回一个字符串，列出模块的所有进口和出口。</p>
<pre><code class="hljs language-dart copyable" lang="dart"><span class="hljs-built_in">print</span>(module.describe());
<span class="copy-code-btn">复制代码</span></code></pre>
<p>对于我们的Brotli库，这就是输出。</p>
<pre><code class="copyable">import function: int32 wasi_unstable::fd_close(int32)
import function: int32 wasi_unstable::fd_write(int32, int32, int32, int32)
import function: int32 wasi_unstable::fd_fdstat_get(int32, int32)
import function: int32 wasi_unstable::fd_seek(int32, int64, int32, int32)
import function: void wasi_unstable::proc_exit(int32)
export memory: memory
export function: int32 BrotliDecoderSetParameter(int32, int32, int32)
export function: int32 BrotliDecoderCreateInstance(int32, int32, int32)
export function: void BrotliDecoderDestroyInstance(int32)
export function: int32 BrotliDecoderDecompress(int32, int32, int32, int32)
…
export function: int32 BrotliEncoderSetParameter(int32, int32, int32)
export function: int32 BrotliEncoderCreateInstance(int32, int32, int32)
export function: void BrotliEncoderDestroyInstance(int32)
export function: int32 BrotliEncoderMaxCompressedSize(int32)
export function: int32 BrotliEncoderCompress(int32, int32, int32, int32, int32, int32, int32)
…
<span class="copy-code-btn">复制代码</span></code></pre>
<p>我们可以看到，该模块导入了一些WASI函数，并导出了它的内存和一堆Brotli函数。我们感兴趣的两个函数是导出的，但它们的签名看起来有点不同。这是因为Wasm只支持32位和64位的ints和floats。指针已经变成int32索引，进入导出的内存。</p>
<p>下一步是对模块进行实例化。在实例化过程中，我们必须填充模块所期望的每一个导入。实例化使用了构建器模式（module.instantiate(). initialization... .build()）。我们的库只导入WASI函数，所以我们可以直接调用enableWasi()。</p>
<pre><code class="hljs language-dart copyable" lang="dart"><span class="hljs-keyword">var</span> instance = module.instantiate().enableWasi().build();
<span class="copy-code-btn">复制代码</span></code></pre>
<p>如果我们有额外的非WASI函数导入，我们可以使用addFunction()将一个Dart函数导入wasm库中。
现在我们有了一个WasmInstance，我们可以查询它的任何一个导出的函数，或者检查它的内存。</p>
<pre><code class="hljs language-dart copyable" lang="dart"><span class="hljs-keyword">var</span> memory = instance.memory;
<span class="hljs-keyword">var</span> compress = instance.lookupFunction(“BrotliEncoderCompress”);
<span class="hljs-keyword">var</span> decompress = instance.lookupFunction(“BrotliDecoderDecompress”);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>接下来我们要做的是对我们的输入文件使用压缩和解压函数。但是我们不能直接将数据传递给这些函数。C函数采取的是uint8_t的数据指针，但在Wasm代码中，这些指针成为实例内存的int32索引。Brotli还使用size_t指针报告压缩和解压缩数据的大小，这些指针也变成了int32。</p>
<p>因此，为了将我们的数据传递给函数，我们必须将其复制到实例的内存中，并将其索引传递给函数。我们需要5个区域的内存：输入数据、压缩数据、压缩大小、解压缩数据和解压缩大小。为了简单起见，我们只是要抓取一些未使用的内存区域，但你也可以在你的库中导出malloc()和free()。</p>
<p>为了确保我们把数据放在未使用的内存中，我们要增长实例内存，并使用新的区域来存放我们的数据。</p>
<pre><code class="hljs language-dart copyable" lang="dart"><span class="hljs-keyword">var</span> inputPtr = memory.lengthInBytes;
memory.grow((<span class="hljs-number">3</span> * inputData.length /
    WasmMemory.kPageSizeInBytes).ceil());
<span class="hljs-keyword">var</span> memoryView = memory.view;
<span class="hljs-keyword">var</span> outputPtr = inputPtr + inputData.length;
<span class="hljs-keyword">var</span> outSizePtr = outputPtr + inputData.length;
<span class="hljs-keyword">var</span> decodedPtr = outSizePtr + <span class="hljs-number">4</span>;
<span class="hljs-keyword">var</span> decSizePtr = decodedPtr + inputData.length;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>我们的内存区域看起来像这样。</p>
<pre><code class="copyable">[initial instance memory][input][output][output size][decoded][decoded size]
<span class="copy-code-btn">复制代码</span></code></pre>
<p>接下来，我们在内存中加载输入数据，并调用我们的压缩函数。</p>
<pre><code class="hljs language-dart copyable" lang="dart">memoryView.setRange(
    inputPtr, inputPtr + inputData.length, inputData);
<span class="hljs-keyword">var</span> status = compress(kDefaultQuality, kDefaultWindow, kDefaultMode,
    inputData.length, inputPtr, outSizePtr, outputPtr);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这个例子的其余部分也是这样工作的。这就是结果。</p>
<pre><code class="copyable">Loading lipsum.txt
Input size: 3210 bytes
Compressing…
Compression status: 1
Compressed size: 1198 bytes
Space saving: 62.68%
Decompressing…
Decompression status: 1
Decompressed size: 3210 bytes
Verifying decompression…
Decompression succeeded :)
<span class="copy-code-btn">复制代码</span></code></pre>
<h1 data-id="heading-4">尝试package:wasm</h1>
<p>如果你对尝试Wasm互操作感兴趣，请查看package:wasm的<a href="https://link.juejin.cn/?target=https%3A%2F%2Fpub.dev%2Fpackages%2Fwasm" target="_blank" rel="nofollow noopener noreferrer" title="https://pub.dev/packages/wasm" ref="nofollow noopener noreferrer">README</a>说明。</p>
<h1 data-id="heading-5">路线图</h1>
<p>Wasm编译和Wasm互操作都是实验性的。如果这些实验被证明是有成效的，我们计划继续开发它们，并最终将其产品化为稳定的、支持的版本。然而，如果我们了解到有些东西不能按预期工作，或看到缺乏兴趣，我们将停止实验。</p>
<p>我们做这些实验是为了学习，有两个主要部分。首先，我们想了解在技术上支持Wasm的可行性，以及这种支持的特点可能是什么。它可以使Dart代码更快，更小，或更可预测吗？其次，我们有兴趣探索Wasm可能释放哪些新的技术能力，以及这些可能为Dart开发者带来哪些新的用例。我们可以使与本地代码的互操作更加便携吗？</p>
<p>您认为Wasm如何适用于您的需求？你认为你会用它来做什么？我们很想听听您的想法。请让我们知道在<a href="https://link.juejin.cn/?target=https%3A%2F%2Fgroups.google.com%2Fa%2Fdartlang.org%2Fg%2Fmisc%2F" target="_blank" rel="nofollow noopener noreferrer" title="https://groups.google.com/a/dartlang.org/g/misc/" ref="nofollow noopener noreferrer">Dart misc讨论组</a>。</p>
<hr>
<p><a href="https://link.juejin.cn/?target=http%3A%2F%2Fwww.deepl.com" target="_blank" rel="nofollow noopener noreferrer" title="http://www.deepl.com" ref="nofollow noopener noreferrer">www.deepl.com</a></p></div>  
</div>
            