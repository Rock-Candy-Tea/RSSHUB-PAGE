
---
title: 'ReactNative在游戏营销场景中的实践和探索-Hermes引擎'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/f76d00c14fb74cd58973144d0025e8f9~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Wed, 25 Aug 2021 23:09:13 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/f76d00c14fb74cd58973144d0025e8f9~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p><strong>作者：字节游戏中台客户端团队 - 熊文源</strong></p>
<p>客户端跨端框架已经发展了很多年了，最近比较流行的小程序、Flutter、ReactNative，都算是比较成功、成熟的框架，面向的开发者也不一样，很多大型App都广泛的使用了，笔者有幸很早就参与学习使用了这些优秀的跨端方案，在这几年的开发和架构设计中，除了在App中支撑了千万级DAU，也慢慢将ReactNative跨端方案运用到了游戏，来提升开发、迭代效率。本次文章我们会分5个章节介绍我们在游戏中的一些探索和实践，相信大家也能从中有所收获：</p>
<ul>
<li><strong><a href="https://juejin.cn/post/7000628820814331918" target="_blank" title="https://juejin.cn/post/7000628820814331918">第一篇：游戏中使用ReactNative的背景介绍</a></strong></li>
<li><strong><a href="https://juejin.cn/post/7000630849402044453" target="_blank" title="https://juejin.cn/post/7000630849402044453">第二篇：简介游戏中怎么集成ReactNative</a></strong></li>
<li><strong><a href="https://juejin.cn/post/7000631869628743688" target="_blank" title="https://juejin.cn/post/7000631869628743688">第三篇：简介游戏中的ReactNative性能优化</a></strong></li>
<li><strong><a href="https://juejin.cn/post/7000632245824258079" target="_blank" title="https://juejin.cn/post/7000632245824258079">第四篇：ReactNative Hermes引擎简介</a></strong></li>
<li><strong><a href="https://juejin.cn/post/7000634295668703246" target="_blank" title="https://juejin.cn/post/7000634295668703246">第五篇：ReactNative 新架构介绍</a></strong></li>
</ul>
<p>（本篇为系列第四篇）</p>
<p>上面章节我们介绍了针对ReactNative做的大量的性能优化，ReactNative在手机端设备上优化很明显，但之前我们介绍了游戏相比于原生App，还多一个模拟器环境，与手机设备相差很大，运行在pc上，所以采用的的是x86架构，有32位与64位两类模拟器。ReactNative目前也已经支持了x86架构，所以在带有x86架构的游戏中，性能基本和手机设备旗鼓相当，但在海外一些游戏中，因只能支持v7、v8，不管是启动性能、内存、兼容性都相比x86版本很远，在某些复杂活动下启动性能能会超过3s以上，相信到这里，你们一定会问为什么海外不支持x86呢？主要原因是：Google Player对上架的App的架构有限制，要求v7和v8、x86和x86_64必须同时存在，换句话说游戏app如果要支持x86，就必须支持x86_64，而很多游戏引擎是不具备x86_64架构的，典型的如Unity，导致上架的App只有v7、v8，而x86模拟器也对v7、v8做了兼容，所以大部分的应用在模拟器上还是能用的，原理是采用了intel提供的转指令库，所以性能和兼容性会偏差，这里就不细述了。</p>
<p>另外还有其他一些限制，在设计整个框架时，考虑Androidx的问题（很多app没有升级），我们采用了0.59.9的ReactNative引擎，js引擎在Android端使用的是JavaScriptCore，由于JavaScriptCore最初是为桌面浏览器端设计，相较于桌面端，移动端能力有太多的限制。Facebook团队发现JavaScript 引擎是影响启动性能和应用包体积的重要因素，为了能从底层对移动端进行性能优化，2019 年推出一个强大的JS运行引擎，Facebook团队自建的JavaScrip引擎Hermes，目前ReactNative 0.60.2版本上已经支持了Android端，iOS在0.64版本也支持，新的引擎有几个特点：</p>
<ol>
<li>Hermes支持执行纯文本的js</li>
<li>支持动态加载纯文本js、bytecode</li>
<li>支持bytecode和纯文本js混合使用</li>
</ol>
<p>同样我们也集成Hermes引擎到框架中，并做了大量的性能数据测试，大致的数据如下：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/f76d00c14fb74cd58973144d0025e8f9~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>无论是在内存峰值、稳定值、启动性能上，Hermes相比于JSCore有了很多优化，Hermes业务包因为采用字节码，相对js混淆包增大了，但去掉source map后，整体大小是下降的。因ReactNative支持了JSI，所Hermes、JSCore在目前的ReactNative版本是共存的，大家可以使用0.60.2后的ReactNative版本体验：</p>
<ol>
<li>配置android/app/build.gradle ，enableHermes: true 打包hermes引擎版本</li>
<li>配置chrome debug环境<a href="https://link.juejin.cn/?target=https%3A%2F%2Freactnative.dev%2Fdocs%2Fhermes" target="_blank" rel="nofollow noopener noreferrer" title="https://reactnative.dev/docs/hermes" ref="nofollow noopener noreferrer">reactnative.dev/docs/hermes</a></li>
<li>其他开发方式不变</li>
</ol>
<p>相信有不少App采用的Module方式集成的，升级Hermes也比较简单，只需将Hermes的aar库集成到工程中， Facebook已经将Hermes引擎托管到npm端，以下是参考代码：</p>
<pre><code class="copyable">   if (enableHermes) &#123;

       def hermesPath = "../../node_modules/hermes-engine/android/";

       debugImplementation files(hermesPath + "hermes-debug.aar")

       releaseImplementation files(hermesPath + "hermes-release.aar")

   &#125; else &#123;

       implementation "org.webkit:android-jsc:+"

   &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>另外要注意在ReactNative SDK中，如果JSCore和Hermes同时存在的情况下，会优先选择JSCore，当然这边逻辑是可以调整的，开发者可以将JSCore做了Hermes的backup方案，线上出现Hermes稳定稳定问题，可以降级到JSCore版本，毕竟JSCore版本已经稳定了很多版本了。</p>
<h2 data-id="heading-0"><strong>主要优化点</strong></h2>
<p>那facebook设计的<a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Ffacebook%2Fhermes" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/facebook/hermes" ref="nofollow noopener noreferrer">Hermes</a>引擎相对于JScore做了哪些优化？可以理解Hermes就是为ReactNative 而生的用于替换JScore的，ES6规范，采用AOT编译，将解释和编译过程前置到编译阶段，运行时只完成机器码的执行，大大提高了运行效率：</p>
<ol>
<li>相比JSCore，做了简化，将一些ReactNative中不常用的语法做了删除，更加聚焦、精简，具体可以参考<a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Ffacebook%2Fhermes%2Fblob%2Fmain%2Fdoc%2FFeatures.md" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/facebook/hermes/blob/main/doc/Features.md" ref="nofollow noopener noreferrer">Features</a>，以下是一些例子：</li>
</ol>
<ul>
<li>Realms</li>
<li>with statements</li>
<li>Local mode eval() (use and introduce local variables)</li>
<li>Symbol.species and its interactions with JS library functions</li>
<li>use of constructor property when creating new Arrays in Array.prototype methods</li>
<li>Symbol.unscopables (Hermes does not support with)</li>
<li>Other features added to ECMAScript after ES6 not listed under "Supported"</li>
</ul>
<ol start="2">
<li>最新版本Hermes 采用了Hades垃圾收集器，目的是要对比genGC的暂停时间提升一个数量级，大部分垃圾收集工作是在后台线程中运行，与运行JavaScript代码的解释器是同时发生的，而genGC是与解释器共享的单个线程运行</li>
<li>无JIT, 为了加快执行速度，流行的 JavaScript 引擎可以地将频繁解释的代码编译为机器码，这项工作由即时（JIT）编译器执行, 但JIT 必须在应用程序启动时预热，所以对TTI影响较大，另外JIT 会增加原生代码体积和内存消耗，这些在内存比较吃紧的手持设备、游戏中，显得很致命，影响了我们最关注的指标，因此Hermes没有实现JIT，而是更关注Hermes 的解释器执行效率</li>
<li>Hermes预编译器，在移动应用构建过程中运行，或者是打包前端业务包时，原有的方式，会将前端代码打包成混淆的jsbunlde文件，而Hermes提供了转换器，将jsbundle文件转换成字节码文件，因为是在打包过程中，所以给到我们程序优化成字节码的时间可以更长，使字节码更小、效率更高，而且现在还可以针对整个程序做优化，例如删除重复数据和打包字符串表等。另外字节码的设计使其在运行时可以映射到内存中并解释，而无需一次读取整个文件，以下是具体的执行命令：</li>
</ol>
<pre><code class="copyable">./node_modules/hermes-engine/osx-bin/hermes -emit-binary
<span class="copy-code-btn">复制代码</span></code></pre>
<ol start="5">
<li>上面介绍了JSCore和Hermes在ReactNative中是可以随时切换的，新的引擎支持了JSI架构，抹平了JS引擎的差异，切换到其他引擎更方便了，例如v8等</li>
</ol>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/50705659f4704302beeef3b77a904700~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<ol start="6">
<li>Hermes是为移动设备设计的JS引擎，稳定性更好，在x86架构上，TTI表现相比JScore提升较少，但x86的整体性能已经很好了</li>
<li>对于文章前面提到的JSCore v7、v8在x86模拟器中中存在的兼容问题，Hermes引擎也有了很好的改善，基本兼容主流模拟器</li>
</ol>
<p>数据来看，新的引擎无论是在TTI上，还是执行效率、兼容性上，都相比旧的JSCore有了飞的提升，到这里大家会有一个疑问，如果是打包成字节码运行，那怎么调试的，其实Hermes在调试过程中，采用的是懒编译，它在设备上懒惰地生成字节码。这样开发者就可以使用 Metro 或其他纯 JavaScript 代码源进行快速迭代，但代价是懒惰编译的字节码不包括生产构建的所有优化特性，性能上会偏差，这也是为什么非字节码的jsbundle能运行到Hermes的原因，但整体性能偏差。</p>
<h2 data-id="heading-1"><strong>如何升级</strong></h2>
<p>上面说了很多Hermes的新特性，相信大家也一定也想在自己的项目中体验体验，那就涉及升级的问题了，可以有三种思路：</p>
<ul>
<li>升级ReactNative版本到0.60.2及以后版本，当然考虑稳定性，版本越高越好，具体升级版本，大家根据实际需求来升级，Facebook也提供了升级工具：<a href="https://link.juejin.cn/?target=https%3A%2F%2Freact-native-community.github.io%2Fupgrade-helper%2F%3Ffrom%3D0.63.4%26to%3D0.64.0" target="_blank" rel="nofollow noopener noreferrer" title="https://react-native-community.github.io/upgrade-helper/?from=0.63.4&to=0.64.0" ref="nofollow noopener noreferrer">react-native-community.github.io/upgrade-hel…</a></li>
<li>如项目使用的ReactNative已经包含了JSI的设计，也可以考虑通过适配JSI和Hermes的excute环境来完成适配，因JSI可以支持灵活替换JS引擎，但相对适配的难度相较大</li>
<li>对于一些已经集成Hermes的项目，单独升级Hermes版本的难度较低，兼容适配JSI接口即可。笔者也尝试在0.62.2的ReactNative版本中完成了Hermes从0.40升级到0.72</li>
</ul>
<p><strong>Hermes版本的修改记录</strong>：<a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Ffacebook%2Fhermes%2Freleases" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/facebook/hermes/releases" ref="nofollow noopener noreferrer">github.com/facebook/he…</a></p>
<h2 data-id="heading-2">总结</h2>
<p>我们在游戏中完成Hermes升级后，将ReactNative版本到Hermes版本，通过真实的线上业务来验证、灰度，整体数据基本超过了预期的，对用户体验来说收益很高：</p>
<ol>
<li>整体崩溃率是远低于JSCore版本</li>
<li>模拟器TTI时间有几倍以上的优化</li>
</ol></div>  
</div>
            