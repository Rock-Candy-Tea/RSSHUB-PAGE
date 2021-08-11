
---
title: 'Dart 代码的组件集合Dart VM3'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/7a1efb33fe1548dd9707e3ff0f2c1f61~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Tue, 10 Aug 2021 17:23:59 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/7a1efb33fe1548dd9707e3ff0f2c1f61~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>这是我参与8月更文挑战的第 8 天，活动详情查看：<a href="https://juejin.cn/post/6987962113788493831" title="https://juejin.cn/post/6987962113788493831" target="_blank">8月更文挑战</a>。为应掘金的<code>八月更文挑战</code>，</p>
<h2 data-id="heading-0">通过 JIT 运行源代码</h2>
<p>本节将介绍当从命令行执行 Dart 时会发生什么：</p>
<pre><code class="copyable">// hello.dart
main() => print('Hello, World!');
​
$ dart hello.dart
Hello, World!
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>「Dart 2 VM 开始不再具有从原始代码直接执行 Dart 的能力，相反 VM 希望获得包含序列化内核 AST 的内核二进制文件（也称为 dill 文件）」</strong>。将 Dart 源代码翻译成 Kernel AST 的任务是由通用前端 (CFE)处理的，CFE 是用 Dart 编写并在不同 Dart 工具上共享（例如 VM、dart2js、Dart Dev Compiler）。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/7a1efb33fe1548dd9707e3ff0f2c1f61~tplv-k3u1fbpfcp-watermark.image" alt="图片" loading="lazy" referrerpolicy="no-referrer"></p>
<p>为了保持直接从源代码执行 Dart ，这里托管一个名为 kernel service 的辅助 <code>isolate</code>，它处理将 Dart 源代码编译到内核中，然后 VM 运行生成的内核二进制文件。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/b037e582d04e401b8a23ee7cb742f0e8~tplv-k3u1fbpfcp-watermark.image" alt="图片" loading="lazy" referrerpolicy="no-referrer"></p>
<p>然而这种设置并不是 CFE 和 VM 运行 Dart 代码的唯一方法，例如 <strong>「Flutter 是将编译到 Kernel 的过程和从 Kernel 执行的过程完全分离」</strong>，并将它们放在不同的设备上实现：编译发生在开发者机器（主机）上，执行在目标移动设备上处理，目标移动设备接收由 flutter 工具发送给它的内核二进制文件。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/d54e167c90dc42f7856ef81bb8546696~tplv-k3u1fbpfcp-watermark.image" alt="图片" loading="lazy" referrerpolicy="no-referrer"></p>
<p>这里需要注意，该 Flutter 工具不处理 Dart 本身的解析， 相反它会生成另一个持久进程 <code>frontend_server</code>，它本质上是围绕 CFE 和一些 Flutter 特定的 Kernel-to-Kernel 转换的封装。</p>
<p><code>frontend_server</code> 将 Dart 源代码编译为内核文件， 然后 flutter 将其发送到设备， 当开发人员请求热重载时 <code>frontend_server</code> 开始发挥作用：在这种情况下 <code>frontend_server</code> 可以重用先前编译中的 CFE 状态，并重新编译实际更改的库。</p>
<p><strong>「一旦内核二进制文件加载到 VM 中，它就会被解析以创建代表各种程序实体的对象，然而这个过程是惰性完成的」</strong>：首先只加载关于库和类的基本信息，源自内核二进制文件的每个实体都保留一个指向二进制文件的指针，以便以后可以根据需要加载更多信息。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/1cfbcb81f22c41819debf73dd675a8f4~tplv-k3u1fbpfcp-watermark.image" alt="图片" loading="lazy" referrerpolicy="no-referrer"></p>
<blockquote>
<p>❝</p>
<p>每当我们引用 VM 内部分配的对象时，我们都会使用 Untagged 前缀，因为这遵循了 VM 自己的命名约定：内部 VM 对象的布局由 C++ 类定义，名称以 Untagged头文件 <code>runtime/vm/raw_object.h</code> 开头。例如 <code>dart::UntaggedClass</code> 是描述一个 Dart 类 VM 对象， <code>dart::UntaggedField</code> 是一个 VM 对象</p>
<p>❞</p>
</blockquote>
<p><strong>「只有在运行时需要它时（例如查找类成员、分配实例等），有关类的信息才会完全反序列化」</strong>，在这个阶段，类成员会从内核二进制文件中读取，然而在此阶段不会反序列化完整的函数体，只会反序列化它们的签名。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/809a775ffec349159be323cb3aa16def~tplv-k3u1fbpfcp-watermark.image" alt="图片" loading="lazy" referrerpolicy="no-referrer"></p>
<p>此时 methods 在运行时可以被成功解析和调用，因为已经从内核二进制文件加载了足够的信息，例如它可以解析和调用 <code>main</code> 库中的函数。</p>
<blockquote>
<p>❝</p>
<p><code>package:kernel/ast.dart</code> 定义了描述内核 AST 的类； <code>package:front_end</code>处理解析 Dart 源代码并从中构建内核 AST。<code>dart::kernel::KernelLoader::LoadEntireProgram是</code> 将内核 AST 反序列化为相应 VM 对象的入口点；<code>pkg/vm/bin/kernel_service.dart</code> 实现了内核服务隔离，<code>runtime/vm/kernel_isolate.cc</code> 将 Dart 实现粘合到 VM 的其余部分； <code>package:vm</code> 承载大多数基于内核的 VM 特定功能，例如各种内核到内核的转换；由于历史原因一些特定于 VM 的转换仍然存在于 <code>package:kernel</code> 中。</p>
<p>❞</p>
</blockquote>
<p>最初所有的函数都会有一个占位符，而不是它们的主体的实际可执行代码：它们指向 <code>LazyCompileStub</code>，它只是要求运行时系统为当前函数生成可执行代码，然后 <code>tail-calls</code> 这个新生成的代码。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/1abb6b1a0dee4daab82cd437370d2f94~tplv-k3u1fbpfcp-watermark.image" alt="图片" loading="lazy" referrerpolicy="no-referrer"></p>
<p>第一次编译函数时，是通过未优化编译器完成的。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/8f38112d09094d5db3620d2c9e35cb8e~tplv-k3u1fbpfcp-watermark.image" alt="图片" loading="lazy" referrerpolicy="no-referrer"></p></div>  
</div>
            