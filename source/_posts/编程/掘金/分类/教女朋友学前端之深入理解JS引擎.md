
---
title: '教女朋友学前端之深入理解JS引擎'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/78c3dbcfda7442629f5187c1ea11f598~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Sun, 15 Aug 2021 16:55:51 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/78c3dbcfda7442629f5187c1ea11f598~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;color:#383838;font-size:15px;line-height:37.5px;letter-spacing:2px;word-break:break-word;font-family:-apple-system,BlinkMacSystemFont,Segoe UI,Roboto,Oxygen,Ubuntu,Cantarell,Open Sans,Helvetica Neue,sans-serif;scroll-behavior:smooth;background-image:linear-gradient(0deg,transparent 24%,rgba(201,195,195,.329) 25%,hsla(0,8%,80.4%,.05) 26%,transparent 27%,transparent 74%,hsla(0,5.2%,81%,.185) 75%,rgba(180,176,176,.05) 76%,transparent 77%,transparent),linear-gradient(90deg,transparent 24%,rgba(204,196,196,.226) 25%,hsla(0,4%,66.1%,.05) 26%,transparent 27%,transparent 74%,hsla(0,5.2%,81%,.185) 75%,rgba(180,176,176,.05) 76%,transparent 77%,transparent);background-color:#fff;background-size:50px 50px;padding-bottom:120px&#125;.markdown-body ::selection&#123;color:#fff;background-color:#a862ea&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;margin:30px 0 15px;color:#a862ea&#125;.markdown-body h1&#123;line-height:2;font-size:1.4em&#125;.markdown-body h1~p:first-of-type:first-letter&#123;color:#a862ea;float:left;font-size:2em;margin-right:.4em;font-weight:bolder&#125;.markdown-body h2&#123;font-size:1.2em&#125;.markdown-body h3&#123;font-size:1.1em&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:2em&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;padding-left:.2em&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:10px&#125;.markdown-body li::marker&#123;color:#a862ea&#125;.markdown-body li,.markdown-body p&#123;opacity:.9;vertical-align:baseline;transition:all .1s ease&#125;.markdown-body li:hover,.markdown-body p:hover&#123;opacity:1&#125;.markdown-body a&#123;display:inline-block;color:#a862ea;cursor:pointer;padding-bottom:2px;text-decoration:none;position:relative&#125;.markdown-body a:after&#123;content:"";position:absolute;width:98%;height:2px;bottom:0;left:0;transform:scaleX(0);background-color:#a862ea;transform-origin:bottom right;transition:transform .3s ease-in-out&#125;.markdown-body a:hover:after&#123;transform:scaleX(1);transform-origin:bottom left&#125;.markdown-body a:active,.markdown-body a:link&#123;color:#a862ea&#125;.markdown-body img&#123;max-width:100%;user-select:none;margin:1em 0;box-shadow:0 0 20px 0 #e7daff;transition:transform .2s ease 0s;background-color:#f8f5ff&#125;.markdown-body img:hover&#123;opacity:1;transform:translateY(-2px)&#125;.markdown-body blockquote&#123;padding:.5em 1em;margin:15px 0;border-top-left-radius:2px;border-bottom-left-radius:2px;border-left:4px solid #a862ea;background-color:#f8f5ff&#125;.markdown-body blockquote>p&#123;margin:0&#125;.markdown-body code&#123;padding:2px .4em;overflow-x:auto;color:#a862ea;font-weight:700;word-break:break-word;font-family:Operator Mono,Consolas,Monaco,Menlo,monospace;background-color:#f8f5ff&#125;.markdown-body pre&#123;margin:2em 0;box-shadow:0 0 20px #e7daff&#125;.markdown-body pre>code&#123;display:block;padding:1.5em;word-break:normal;font-size:.9em;font-style:normal;font-weight:400;font-family:Operator Mono,Consolas,Monaco,Menlo,monospace;line-height:22.5px;color:#383838;border-radius:3px;scroll-behavior:smooth&#125;.markdown-body pre>code::-webkit-scrollbar&#123;height:6px;background-color:#f8f5ff&#125;.markdown-body pre>code::-webkit-scrollbar-thumb&#123;background-color:#e7daff;border-bottom-left-radius:3px;border-bottom-right-radius:3px&#125;.markdown-body hr&#123;margin:2em 0;border-top:1px solid #a862ea&#125;.markdown-body table&#123;font-size:12px;max-width:100%;overflow:auto;border-collapse:collapse;border:1px solid #e7daff&#125;.markdown-body thead&#123;color:#a862ea;background:#f8f5ff&#125;.markdown-body td,.markdown-body th&#123;padding:1em .5em&#125;.markdown-body tr&#123;background-color:#fcfcfc&#125;@media (max-width:720px)&#123;.markdown-body&#123;font-size:12px&#125;&#125;</style><p><strong>美味值：🌟🌟🌟🌟🌟</strong></p>
<p><strong>口味：番茄肥牛</strong></p>
<blockquote>
<p>食堂老板娘：老板，Chrome V8 引擎工作原理面试会问吗？</p>
</blockquote>
<p>食堂老板：这块的知识不仅面试可能会问，学会了 JS 引擎的工作原理，可以更好的理解 JavaScript、更好的理解前端生态中 Babel 的词法分析和语法分析，ESLint 的语法检查原理以及 React、Vue 等前端框架的实现原理。总之，学习引擎原理可谓是一举多得。</p>
<blockquote>
<p>食堂老板娘：好好好，别罗嗦了，快开始吧～</p>
</blockquote>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/78c3dbcfda7442629f5187c1ea11f598~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-0">宏观视角看 V8</h2>
<p>V8 是我们前端届的网红，它用 C++ 编写，是谷歌开源的高性能 JavaScript 和 WebAssembly 引擎，主要用在 Chrome、Node.js、Electron...中。</p>
<p>在开始讲我们的主角 V8 引擎之前，先来从宏观视角展开谈谈 V8 所处的位置，建立一个世界观。</p>
<p>在信息科技高速发展的今天，这个疯狂的大世界充斥着各种电子设备，我们每天都用的手机、电脑、电子手表、智能音箱以及现在马路上跑的越来越多的电动汽车。</p>
<p>作为软件工程师，我们可以将它们统一理解为“电脑”，它们都是由<code>中央处理器(CPU)、存储以及输入、输出设备构成</code>。CPU 就像厨师，负责按照菜谱执行命令烧菜。存储如同冰箱，负责保存数据以及要执行的命令(食材)。</p>
<p>当电脑接通电源，CPU 便开始从存储的某个位置读取指令，按照指令一条一条的执行命令，开始工作。电脑还可以接入各种外部设备，比如：鼠标、键盘、屏幕、发动机等等。CPU 不需要全部搞清楚这些设备的能力，它只负责和这些设备的端口进行数据交换就好。设备厂商也会在提供设备时，附带与硬件匹配的软件，来配合 CPU 一起工作。说到这里，我们便得到了最基础的计算机，也是计算机之父冯·诺伊曼在 1945 年提出的体系结构。</p>
<p>不过由于机器指令人类读起来非常不友好，难以阅读和记忆，所以人们发明了编程语言和编译器。编译器可以把人类更容易理解的语言转换为机器指令。除此之外，我们还需要操作系统，来帮我们解决软件治理的问题。我们知道操作系统有很多，如 Windows、Mac、Linux、Android、iOS、鸿蒙等，使用这些操作系统的设备更是数不胜数。为了消除客户端的多样性，实现跨平台并提供统一的编程接口，浏览器便诞生了。</p>
<p>所以，我们可以将浏览器看作操作系统之上的操作系统，而对于我们前端工程师最熟悉的 JavaScript 代码来说，浏览器引擎(如：V8)就是它的整个世界。</p>
<h2 data-id="heading-1">星球最强 JavaScript 引擎</h2>
<p>毫无疑问，V8 是最流行、最强的 JavaScript 引擎，V8 这个名字的灵感来源于 50 年代经典的“肌肉车”的引擎。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/829d1f11a09042339bf1f07113b2abe4~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-2">Programming Languages Software Award</h3>
<p>V8 也曾获得了学术界的肯定，拿到了 ACM SIGPLAN 的 <a href="https://link.juejin.cn/?target=http%3A%2F%2Fwww.sigplan.org%2FAwards%2FSoftware%2F" target="_blank" rel="nofollow noopener noreferrer" title="http://www.sigplan.org/Awards/Software/" ref="nofollow noopener noreferrer">Programming Languages Software Award</a>。</p>
<h3 data-id="heading-3">主流 JS 引擎</h3>
<p>JavaScript 的主流引擎如下所示：</p>
<ul>
<li><a href="https://link.juejin.cn/?target=https%3A%2F%2Fv8.dev%2F" target="_blank" rel="nofollow noopener noreferrer" title="https://v8.dev/" ref="nofollow noopener noreferrer">V8 (Google) </a></li>
<li><a href="https://link.juejin.cn/?target=https%3A%2F%2Fspidermonkey.dev%2F" target="_blank" rel="nofollow noopener noreferrer" title="https://spidermonkey.dev/" ref="nofollow noopener noreferrer">SpiderMonkey (Mozilla) </a></li>
<li><a href="https://link.juejin.cn/?target=https%3A%2F%2Fdeveloper.apple.com%2Fdocumentation%2Fjavascriptcore%2F" target="_blank" rel="nofollow noopener noreferrer" title="https://developer.apple.com/documentation/javascriptcore/" ref="nofollow noopener noreferrer">JavaScriptCore (Apple) </a></li>
<li><a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fmicrosoft%2FChakraCore%2F" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/microsoft/ChakraCore/" ref="nofollow noopener noreferrer">Chakra (Microsoft) </a></li>
<li><a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fsvaarala%2Fduktape%2F" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/svaarala/duktape/" ref="nofollow noopener noreferrer">duktape(IOT)</a></li>
<li><a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fjerryscript-project%2Fjerryscript%2F" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/jerryscript-project/jerryscript/" ref="nofollow noopener noreferrer">JerryScript(IOT)</a></li>
<li><a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fbellard%2Fquickjs%2F" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/bellard/quickjs/" ref="nofollow noopener noreferrer">QuickJS</a></li>
<li><a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Ffacebook%2Fhermes%2F" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/facebook/hermes/" ref="nofollow noopener noreferrer">Hermes(Facebook-React Native)</a></li>
</ul>
<h3 data-id="heading-4">V8 发布周期</h3>
<p>V8 团队使用 4 种 Chrome 发布渠道向用户推送新版本。</p>
<ul>
<li>Canary releases 金丝雀版 (每天)</li>
<li>Dev releases 开发版 (每周)</li>
<li>Beta releases 测试版 (每 6 周)</li>
<li>Stable releases 稳定版 (每 6 周)</li>
</ul>
<p>想要了解更多，请戳 <a href="https://link.juejin.cn/?target=https%3A%2F%2Fzhuanlan.zhihu.com%2Fp%2F35038142" target="_blank" rel="nofollow noopener noreferrer" title="https://zhuanlan.zhihu.com/p/35038142" ref="nofollow noopener noreferrer">V8 引擎版本发布流程</a>。</p>
<h2 data-id="heading-5">V8 架构演进史</h2>
<p>2008 年 9 月 2 日，V8 与 Chrome 在同一天开源，最初的代码提交日期可追溯到 2008 年 6 月 30 日，你可以通过下面的链接查看 V8 代码库的可视化演化进程。</p>
<ul>
<li><a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.youtube.com%2Fwatch%3Fv%3DG0vnrPTuxZA" target="_blank" rel="nofollow noopener noreferrer" title="https://www.youtube.com/watch?v=G0vnrPTuxZA" ref="nofollow noopener noreferrer">使用 gource 创建的 V8 代码库可视化演化进程</a></li>
</ul>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/35e466dc16804a57a232dda430446ec2~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>当时的 V8 架构简单粗暴，只有一个 <code>Codegen</code> 编译器。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/50728c74592744a49b38830495eb9758~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>2010 年，V8 中加入了 <code>Crankshaft</code> 优化编译器，大大提升了运行时性能。Crankshaft 生成的机器代码比之前的 Codegen 编译器快两倍，而体积减少了 30％。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/0c14e54701a54ce29fd9c6879e6cbe50~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>2015 年，为了进一步提升性能，V8 引入了 <code>TurboFan</code> 优化编译器。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/ca32f74b65964f27ba50ae5100d689de~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>接下来到了分水岭，在此之前，V8 都是选择将源码直接编译为机器码的架构。不过随着 Chrome 在移动设备的普及，V8 团队发现了这种架构下存在的致命问题：编译时间过长、机器码的内存占用很大。</p>
<p>所以，V8 团队对引擎架构进行了重构，在 2016 年引入了 <code>Ignition 解释器和字节码</code>。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/872e7da8eca143fe9fc22025852070a4~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>2017 年，V8 默认开启全新的编译 <code>pipeline(Ignition + TurboFan)</code>，并移除了 <code>Full-codegen 和 Crankshaft</code>。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/856e739932674412818f00f3a644c4b7~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>高性能的 JS 引擎不仅需要 TurboFan 这样高度优化的编译器，在编译器有机会开始工作之前的性能，也存在着大量的优化空间。</p>
<p>于是在 2021 年，V8 引入新的编译管道 <code>Sparkplug</code>。</p>
<p>对于 Sparkplug 想要了解更多，请戳<a href="https://link.juejin.cn/?target=https%3A%2F%2Fv8.dev%2Fblog%2Fsparkplug" target="_blank" rel="nofollow noopener noreferrer" title="https://v8.dev/blog/sparkplug" ref="nofollow noopener noreferrer">Sparkplug</a></p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/61a04cd8643b4da4a3c1f123afcff05b~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<ul>
<li>关于 V8 架构演进史，想要了解更多请戳<a href="https://link.juejin.cn/?target=https%3A%2F%2Fv8.dev%2Fblog%2F10-years" target="_blank" rel="nofollow noopener noreferrer" title="https://v8.dev/blog/10-years" ref="nofollow noopener noreferrer">庆祝 V8 诞生 10 周年</a></li>
</ul>
<blockquote>
<p>食堂老板娘：原来 V8 架构经历了这么多的变化</p>
</blockquote>
<p>食堂老板：是的，V8 团队为了不断的优化引擎的性能，做了很多努力。</p>
<h2 data-id="heading-6">V8 工作机制</h2>
<p><code>敲黑板，进入本文的重点。</code></p>
<blockquote>
<p>食堂老板娘：拿出小本本记好</p>
</blockquote>
<p>V8 执行 JavaScript 代码的核心流程分为以下两个阶段：</p>
<ul>
<li>编译</li>
<li>执行</li>
</ul>
<p><code>编译阶段指 V8 将 JavaScript 转换为字节码或者二进制机器码，执行阶段指解释器解释执行字节码，或者 CPU 直接执行二进制机器码。</code></p>
<p>为了对 V8 整体的工作机制有更好的理解，我们先来搞懂下面几个概念。</p>
<h3 data-id="heading-7">机器语言、汇编语言、高级语言</h3>
<p>CPU 的指令集就是机器语言，CPU 只能识别二进制的指令。但是对人类来说，二进制难以阅读和记忆，所以人们将二进制转换为可以识别、记忆的语言，也就是汇编语言，通过汇编编译器可以将汇编指令转换为机器指令。</p>
<p>不同的 CPU 有不同的指令集，使用汇编语言编程需要兼容不同的 CPU 架构，如 ARM、MIPS 等，学习成本比较高。汇编语言这层抽象还远远不够，所以高级语言应运而生，高级语言屏蔽了计算机架构的细节，兼容多种不同的 CPU 架构。</p>
<p>CPU 同样不认识高级语言，一般有两种方式执行高级语言的代码，也就是：</p>
<ul>
<li>解释执行</li>
<li>编译执行</li>
</ul>
<h3 data-id="heading-8">解释执行、编译执行</h3>
<p>解释执行会先将输入的源码通过解析器编译成中间代码，再直接使用解释器解释执行中间代码，输出结果。</p>
<p>编译执行也会将源码转换为中间代码，然后编译器会将中间代码编译成机器码，通常编译成的机器码以二进制文件形式存储，执行二进制文件输出结果。编译后的机器码还可以保存在内存中，可以直接执行内存中的二进制代码。</p>
<h3 data-id="heading-9">JIT (Just In Time)</h3>
<p><code>解释执行启动速度快，执行速度慢，而编译执行启动速度慢，执行速度快。</code></p>
<p>V8 权衡利弊后同时采用了解释执行和编译执行这两种方式，这种混合使用的方式称为 <code>JIT (即时编译)</code>。</p>
<p>V8 在执行 JavaScript 源码时，首先解析器会将源码解析为 AST 抽象语法树，解释器 (Ignition) 会将 AST 转换为字节码，一边解释一边执行。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/8ac24fff06fe43deb12639e699e57744~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>解释器同时会记录某一代码片段的执行次数，如果执行次数超过了某个阈值，这段代码便会被标记为热代码(Hot Code)，同时将运行信息反馈给优化编译器 TurboFan，TurboFan 根据反馈信息，会优化并编译字节码，最后生成优化的机器码。</p>
<blockquote>
<p>食堂老板娘：也就是说，当这段代码再次执行时，解释器就可以直接运行优化后的机器码，不需要再次解释，这样会提升很多性能吧？</p>
</blockquote>
<p>食堂老板：对的！</p>
<p>V8 的解释器和编译器的名字寓意非常有趣，解释器 Ignition 代表点火器，编译器 TurboFan 代表涡轮增压，代码启动时通过点火器发动，TurboFan 一旦介入，执行效率会越来越高。</p>
<p>了解了 V8 的大体工作机制，接下来我们继续深入，看一下 V8 核心模块的工作原理。</p>
<h2 data-id="heading-10">V8 核心模块工作原理</h2>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/ac9aba6b08464c29be86d5a9f803afea~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>V8 的核心模块包括：</p>
<ul>
<li><a href="https://link.juejin.cn/?target=https%3A%2F%2Fv8.dev%2Fblog%2Fscanner%2F" target="_blank" rel="nofollow noopener noreferrer" title="https://v8.dev/blog/scanner/" ref="nofollow noopener noreferrer">Parser</a>：解析器负责将 JavaScript 代码转换成 AST 抽象语法树。</li>
<li><a href="https://link.juejin.cn/?target=https%3A%2F%2Fv8.dev%2Fdocs%2Fignition%2F" target="_blank" rel="nofollow noopener noreferrer" title="https://v8.dev/docs/ignition/" ref="nofollow noopener noreferrer">Ignition</a>：解释器负责将 AST 转换为字节码，并收集 TurboFan 需要的优化编译信息。</li>
<li><a href="https://link.juejin.cn/?target=https%3A%2F%2Fv8.dev%2Fdocs%2Fturbofan" target="_blank" rel="nofollow noopener noreferrer" title="https://v8.dev/docs/turbofan" ref="nofollow noopener noreferrer">TurboFan</a>：利用解释器收集到的信息，将字节码转换为优化的机器码。</li>
</ul>
<p>V8 需要等编译完成后才可以运行代码，所以解析和编译过程中的性能十分重要。</p>
<h3 data-id="heading-11">解析器 Parser</h3>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/0480d7a4005748c5b0f53a227f877b7c~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>解析器的解析过程分为两个阶段：</p>
<ul>
<li>词法分析 (Scanner 词法分析器)</li>
<li>语法分析 (Pre-Parser、Parser 语法分析器)</li>
</ul>
<h4 data-id="heading-12">词法分析</h4>
<p><code>Scanner</code> 负责接收 <code>Unicode Stream</code> 字符流，将其解析为 <code>tokens</code>，提供给解析器 <code>Parser</code>。</p>
<p>比如下面这段代码：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">let</span> myName = <span class="hljs-string">'童欧巴'</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>会被解析成 <code>let</code>，<code>myName</code>，<code>=</code>，<code>'童欧巴'</code>，它们分别是关键字、标识符、赋值运算符以及字符串。</p>
<h4 data-id="heading-13">语法分析</h4>
<p>接下来，语法分析会将上一步生成的 tokens，根据语法规则转换为 AST，如果源码存在语法错误，在这一阶段就会终止并抛出语法错误。</p>
<p>可以通过这个网站查看 AST 的结构：<a href="https://link.juejin.cn/?target=https%3A%2F%2Fastexplorer.net%2F" target="_blank" rel="nofollow noopener noreferrer" title="https://astexplorer.net/" ref="nofollow noopener noreferrer">astexplorer.net/</a></p>
<p>也可以通过这个链接<a href="https://link.juejin.cn/?target=https%3A%2F%2Fresources.jointjs.com%2Fdemos%2Fjavascript-ast" target="_blank" rel="nofollow noopener noreferrer" title="https://resources.jointjs.com/demos/javascript-ast" ref="nofollow noopener noreferrer">resources.jointjs.com/demos/javas…</a>直接生成图片，如下所示：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/b58e92e076414fee9a2aa55735c04024~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>得到了 AST，V8 便会生成该段代码的<code>执行上下文</code>。</p>
<h4 data-id="heading-14">惰性解析</h4>
<p>主流的 JavaScript 引擎都采用了<code>惰性解析(Lazy Parsing)</code>，因为源码在执行前如果全部完全解析的话，不仅会造成执行时间过长，而且会消耗更多的内存以及磁盘空间。</p>
<p>惰性解析就是指如果遇到并不是立即执行的函数，只会对其进行<code>预解析(Pre-Parser)</code>，当函数被调用时，才会对其完全解析。</p>
<p>预解析时，只会验证函数的语法是否有效、解析函数声明以及确定函数作用域，并不会生成 AST，这项工作由 <code>Pre-Parser</code> 预解析器完成。</p>
<h3 data-id="heading-15">解释器 Ignition</h3>
<p>得到了 AST 和执行上下文，接下来解释器会将 AST 转换为字节码并执行。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/a69425638c2147bc95cfb004a512d241~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<blockquote>
<p>食堂老板娘：为什么要引入字节码呢？</p>
</blockquote>
<p>引入字节码是一种工程上的权衡，从图中可以看出，仅仅是一个几 KB 的文件，生成的机器码就已经占用了大量的内存空间。</p>
<p>相比机器码，<code>字节码不仅占用内存少，而且生成字节码的时间很快，提升了启动速度</code>。虽然字节码没有机器码执行速度快，但是牺牲了一点执行效率，换来的收益还是很值得的。</p>
<p>况且，字节码与特定类型的机器码无关，通过解释器将字节码转换为机器码后才可以执行，这样也使得 V8 更加方便的移植到不同的 CPU 架构。</p>
<p>你可以通过如下命令，查看 JavaScript 代码生成的字节码。</p>
<pre><code class="hljs language-shell copyable" lang="shell">node --print-bytecode index.js
<span class="copy-code-btn">复制代码</span></code></pre>
<p>也可以通过如下链接进行查看：</p>
<ul>
<li><a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fv8%2Fv8%2Fblob%2Fmaster%2Fsrc%2Finterpreter%2Fbytecodes.h%2F" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/v8/v8/blob/master/src/interpreter/bytecodes.h/" ref="nofollow noopener noreferrer">V8 解释器的头文件，包括所有字节码</a></li>
</ul>
<p>我们来看一段代码：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// index.js</span>
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">add</span>(<span class="hljs-params">a, b</span>) </span>&#123;
    <span class="hljs-keyword">return</span> a + b
&#125;

add(<span class="hljs-number">2</span>, <span class="hljs-number">4</span>)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>上面的代码在执行命令后，会生成如下的字节码：</p>
<pre><code class="hljs language-shell copyable" lang="shell">[generated bytecode for function: add (0x1d3fb97c7da1 <SharedFunctionInfo add>)]
Parameter count 3
Register count 0
Frame size 0
   25 S> 0x1d3fb97c8686 @    0 : 25 02             Ldar a1
   34 E> 0x1d3fb97c8688 @    2 : 34 03 00          Add a0, [0]
   37 S> 0x1d3fb97c868b @    5 : aa                Return
Constant pool (size = 0)
Handler Table (size = 0)
Source Position Table (size = 8)
0x1d3fb97c8691 <ByteArray[8]>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>其中，Parameter count 3 表示三个参数，包括传入的 a，b 以及 this。字节码的详细信息如下：</p>
<pre><code class="hljs language-js copyable" lang="js">Ldar a1 <span class="hljs-comment">// 表示将寄存器中的值加载到累加器中</span>
Add a0, [<span class="hljs-number">0</span>] <span class="hljs-comment">// 从 a0 寄存器加载值并且将其与累加器中的值相加，然后将结果再次放入累加器</span>
Return <span class="hljs-comment">// 结束当前函数的执行，并把控制权传给调用方，将累加器中的值作为返回值</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>每行字节码都对应着特定的功能，一行行字节码就如同搭乐高积木一样，组装到一起就构成了完整的程序。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/771e6e55cb124545a9a0039ab913c26e~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>解释器通常有两种类型，<code>基于栈</code>和<code>基于寄存器的解释器</code>，早期的 V8 解释器也是基于栈的，现在的 V8 解释器采用了基于寄存器的设计，支持寄存器的指令操作，使用寄存器来保存参数和中间计算结果。</p>
<p>Ignition 解释器在执行字节码时，主要使用了<code>通用寄存器</code>和<code>累加寄存器</code>，相关的函数参数和局部变量会保存在通用寄存器中，累加寄存器会保存中间结果。</p>
<p>在执行指令的过程中，CPU 需要对数据进行读写，如果直接在内存中读写的话，会严重影响程序的执行性能。所以 CPU 就引入了寄存器，将一些中间数据存放到寄存器中，提升 CPU 的执行速度。</p>
<h3 data-id="heading-16">编译器 TurboFan</h3>
<p>在编译方面，V8 团队同样做了很多优化，我们来看下内联和逃逸分析。</p>
<h4 data-id="heading-17">内联 inlining</h4>
<p>关于内联，我们先来看一段代码：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">add</span>(<span class="hljs-params">a, b</span>) </span>&#123;
  <span class="hljs-keyword">return</span> a + b
&#125;
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">foo</span>(<span class="hljs-params"></span>) </span>&#123;
  <span class="hljs-keyword">return</span> add(<span class="hljs-number">2</span>, <span class="hljs-number">4</span>)
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>如上代码所示，我们在 foo 函数中调用了函数 add，add 函数接收 a，b 两个参数，返回他们的和。如果不经过编译器优化，则会分别生成这两个函数所对应的机器码。</p>
<p>为了提升性能，TurboFan 优化编译器会将上面两个函数进行内联，然后再进行编译。内联后的函数如下所示：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">fooAddInlined</span>(<span class="hljs-params"></span>) </span>&#123;
  <span class="hljs-keyword">var</span> a = <span class="hljs-number">2</span>
  <span class="hljs-keyword">var</span> b = <span class="hljs-number">4</span>
  <span class="hljs-keyword">var</span> addReturnValue = a + b
  <span class="hljs-keyword">return</span> addReturnValue
&#125;

<span class="hljs-comment">// 因为 fooAddInlined 中 a 和 b 的值都是确定的，所以可以进一步优化</span>
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">fooAddInlined</span>(<span class="hljs-params"></span>) </span>&#123;
  <span class="hljs-keyword">return</span> <span class="hljs-number">6</span>
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>内联优化后，编译生成的机器码会精简很多，执行效率也有很大的提升。</p>
<h4 data-id="heading-18">逃逸分析 Escape Analysis</h4>
<p>逃逸分析也不难理解，它的意思就是<code>分析对象的生命周期是否仅限于当前函数</code>，我们来看一段代码：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">add</span>(<span class="hljs-params">a, b</span>)</span>&#123;
  <span class="hljs-keyword">const</span> obj = &#123; <span class="hljs-attr">x</span>: a, <span class="hljs-attr">y</span>: b &#125;
  <span class="hljs-keyword">return</span> obj.x + obj.y
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><code>如果对象只在函数内部定义，并且对象只作用于函数内部的话，就会被认为是“未逃逸”的</code>，我们可以将上面代码进行优化：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">add</span>(<span class="hljs-params">a, b</span>)</span>&#123;
  <span class="hljs-keyword">const</span> obj_x = a
  <span class="hljs-keyword">const</span> obj_y = b
  <span class="hljs-keyword">return</span> obj_x + obj_y
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>优化后，无需再有对象定义，而且我们可以直接将变量加载到寄存器上，不再需要从内存中访问对象属性。不仅减少了内存消耗，而且提升了执行效率。</p>
<p>关于逃逸分析，Chrome 曾经也爆出过安全漏洞，使整个互联网变慢，感兴趣请戳<a href="https://link.juejin.cn/?target=https%3A%2F%2Fsegmentfault.com%2Fa%2F1190000011413430" target="_blank" rel="nofollow noopener noreferrer" title="https://segmentfault.com/a/1190000011413430" ref="nofollow noopener noreferrer">V8 团队的一个错误，使得整个互联网变慢</a></p>
<p>除了上述提到的各种优化方案和模块，V8 还有很多优化手段和核心模块，如：使用隐藏类快速获取对象属性、使用内联缓存提升函数执行效率、<a href="https://link.juejin.cn/?target=https%3A%2F%2Fv8.dev%2Fblog%2Ftrash-talk%2F" target="_blank" rel="nofollow noopener noreferrer" title="https://v8.dev/blog/trash-talk/" ref="nofollow noopener noreferrer">Orinoco</a> 垃圾回收器、<a href="https://link.juejin.cn/?target=https%3A%2F%2Fv8.dev%2Fblog%2Fliftoff%2F" target="_blank" rel="nofollow noopener noreferrer" title="https://v8.dev/blog/liftoff/" ref="nofollow noopener noreferrer">Liftoff</a> WebAssembly 编译器等等，本文不再过多介绍，大家感兴趣可以自行学习。</p>
<h2 data-id="heading-19">小结</h2>
<p>本文从宏观视角看 V8、V8 架构演进史、V8 的工作机制以及 V8 核心模块的工作原理几个方面进行了介绍和总结，我们可以发现，无论是 Chrome 还是 Node.js，它们只是一个桥梁，负责把我们前端工程师编写的 JavaScript 代码运输到最终的目的地，转换成对应机器的机器码并执行。在这段旅程中，V8 团队做了很大的努力，给他们最大的 respect。</p>
<p>虽然 CPU 的指令集是有限的，但是我们软件工程师编写的程序不是固定的，正是这些程序最终被 CPU 执行，才有了改变世界的可能。</p>
<p>你们是最棒的，改变世界的程序们！</p>
<blockquote>
<p>食堂老板娘：童童，你是最胖的！^_^</p>
</blockquote>
<h2 data-id="heading-20">站在巨人的肩膀上</h2>
<ul>
<li>V8是如何执行 JavaScript 代码的？-老蒋</li>
<li>图解 Google V8 -李兵</li>
<li>许式伟的架构课</li>
<li><a href="https://link.juejin.cn/?target=https%3A%2F%2Fv8.dev%2Fblog" target="_blank" rel="nofollow noopener noreferrer" title="https://v8.dev/blog" ref="nofollow noopener noreferrer">v8.dev/blog</a></li>
</ul>
<h2 data-id="heading-21">❤️爱心三连击</h2>
<p>1.如果你觉得食堂酒菜还合胃口，就点个赞支持下吧，你的<strong>赞</strong>是我最大的动力。</p>
<p>2.关注公众号<code>前端食堂</code>，<strong>吃好每一顿饭！</strong></p>
<p>3.点赞、评论、转发 === 催更！</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/795ce56b905f4fcaaff6694244e1f84d~tplv-k3u1fbpfcp-watermark.image" alt="透明的footer.png" loading="lazy" referrerpolicy="no-referrer"></p></div>  
</div>
            