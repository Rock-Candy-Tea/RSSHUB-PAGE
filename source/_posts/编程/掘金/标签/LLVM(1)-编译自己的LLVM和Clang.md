
---
title: 'LLVM(1)-编译自己的LLVM和Clang'
categories: 
 - 编程
 - 掘金
 - 标签
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/e3cde1aad300405495ea3db6b5681492~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Thu, 26 Aug 2021 15:46:11 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/e3cde1aad300405495ea3db6b5681492~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h1 data-id="heading-0">1、引言</h1>
<p>作为一名iOS开发，很难不从各种渠道听说关于LLVM的消息，如早年编译器从GCC过度到LLVM-GCC，然后由于GCC的开源协议改变，让Apple彻底抛弃GCC转而投向目前正在使用的Clang。比如之前微信团队分享的编译优化。再如之后业内影响颇大的字节团队分享的二进制重排提及的插装所知的也是clang。在安全方面，对LLVM pass的开发也是主力军等等。。。</p>
<p>所以适当的了解LLVM对自己的知识广度是有非常大的帮助的，最少在读一篇有深度的文章的时候，不至于摸不到门槛。</p>
<h1 data-id="heading-1">2、什么是LLVM，什么是Clang</h1>
<p>LLVM 最早是底层虚拟机（Low Level Virtual Machine）的缩写，但由于项目发展过快，底层虚拟机已经不足以介绍项目本身，而它已经发展成为一个包含前端，优化器和后端的完整编译框架，并且全称就叫LLVM，并非任何英文的简称了。其主要由<code>C++</code>编写而成。</p>
<h3 data-id="heading-2">一、什么是LLVM</h3>
<h5 data-id="heading-3">传统编译器架构</h5>
<p>传统编译器架构（如GCC）将前端，优化器，后端耦合在一起，优化难度大，对多架构兼容的也不太友好，需要做大量重复的工作。
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/e3cde1aad300405495ea3db6b5681492~tplv-k3u1fbpfcp-watermark.image" alt="传统的编译器架构.jpg" loading="lazy" referrerpolicy="no-referrer"></p>
<h5 data-id="heading-4">LLVM架构</h5>
<p>LLVM架构三端（前端，优化器，后端）清晰
1、前端面向源码，将源码转化为同样的LLVM Intermediate Representation (LLVM IR)，
2、优化器则针对LLVM IR进行一系列优化，如：无用代码消除，内存优化，甚至是代码混淆等等。。。
3、后端则将IR转化为对应的机器码。
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/bf6cf895b0284e23951d4ccfc7722243~tplv-k3u1fbpfcp-watermark.image" alt="LLVM架构.jpg" loading="lazy" referrerpolicy="no-referrer"></p>
<p>从两种架构的设计可以看得出来，LLVM最大的优势就在于三端分离，所以如果我们想编写一门独立的语言，只需要编写相应的前端就可以兼容各大终端设备。如果以后多了一种终端设备，我们也只需要编写一次后端，就可以兼容各大语言。</p>
<h3 data-id="heading-5">二、什么是Clang</h3>
<p>Clang是LLVM项目的一个子项目，基于LLVM架构的C/C++/Objective-C编译器前端（Swift的前端是Swift）。</p>
<p>Apple早年从GCC切换到LLVM的时候，开始用的是基于GCC库写的一套LLVM前端，但由于Apple对代码优化的要求更高，而GCC官方又迟迟不肯对针对性的更新，所以衍生出GCC的一套分支LLVM-GCC，由Apple自己维护，导致Apple使用的GCC版本远低于官方版本，最后由于GCC的开源协议改变，让Apple彻底抛弃GCC转而投向自研的Clang。</p>
<p>相比于GCC，Clang具有如下优点：
· 编译速度快:在某些平台上，Clang的编译速度显著的快过GCC(Debug模式下编译OC速度比GGC快3倍)
· 占用内存小:Clang生成的AST所占用的内存是GCC的五分之一左右
· 模块化设计:Clang采用基于库的模块化设计，易于 IDE 集成及其他用途的重用
· 诊断信息可读性强:在编译过程中，Clang 创建并保留了大量详细的元数据 (metadata)，有利于调试和错误报告
· 设计清晰简单，容易理解，易于扩展增强</p>
<h1 data-id="heading-6">3、编译过程</h1>
<h3 data-id="heading-7">① 下载</h3>
<p>找到一个自己方便的目录，直接在github上下载（耗时根据网络情况而定，包括git文件总大小大概3G）:
<img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/a7dce269694449bca6fb0841c83d0792~tplv-k3u1fbpfcp-watermark.image" alt="3.png" loading="lazy" referrerpolicy="no-referrer"></p>
<pre><code class="copyable">> mkdir llvm_all && cd llvm_all   
> git clone https://github.com/llvm/llvm-project.git
<span class="copy-code-btn">复制代码</span></code></pre>
<p>完成后你将会看到这样一个目录：
<img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/f4bb5287b6b0402f897bc224aac80eb1~tplv-k3u1fbpfcp-watermark.image" alt="4.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>目前我们只需要关注其中两个文件<code>clang</code>和<code>llvm</code>分别是<code>clang</code>的源码和<code>llvm</code>的源码</p>
<h3 data-id="heading-8">② 编译</h3>
<pre><code class="copyable">cmake -S llvm -B build -G <generator> [options]
<span class="copy-code-btn">复制代码</span></code></pre>
<p>官方介绍了4种编译工具：</p>
<ul>
<li><code>Ninja</code> --- for generating <a href="https://link.juejin.cn/?target=https%3A%2F%2Fninja-build.org%2F" target="_blank" rel="nofollow noopener noreferrer" title="https://ninja-build.org/" ref="nofollow noopener noreferrer">Ninja</a> build files. Most llvm developers use Ninja.</li>
<li><code>Unix Makefiles</code> --- for generating make-compatible parallel makefiles.</li>
<li><code>Visual Studio</code> --- for generating Visual Studio projects and solutions.</li>
<li><code>Xcode</code> --- for generating Xcode projects.</li>
</ul>
<p>官方推荐使用<code>Ninja</code>编译，因为其速度最快，笔者也亲试，整个过程只需20分钟左右即可完成。但作为一名iOS开发，还是习惯使用Xcode编译，毕竟界面看起来亲切，而且可在之后我们编写插件的或者<code>IR Pass</code>的时候也能或得良好的代码提示，缺点就是慢一点。笔者使用Xcode编译花了40分钟左右，这根据个人电脑配置而定，配置稍微差一点，一个小时多也是正常的。</p>
<p>另外还有一些可选参数：</p>
<ul>
<li><code>-DLLVM_ENABLE_PROJECTS='...'</code> --- 可选一些LLVM的子项目共同编译，如 <code>clang</code>, <code>clang-tools-extra</code>, <code>libcxx</code>, <code>libcxxabi</code>, <code>libunwind</code>, <code>lldb</code>, <code>compiler-rt</code>, <code>lld</code>, <code>polly</code>, 或者 <code>cross-project-tests</code>
例如，如果要编译包括  <code>Clang</code>, <code>libcxx</code>, 和 <code>libcxxabi</code> 的<code>LLVM</code>, 可以增加 <code>-DLLVM_ENABLE_PROJECTS="clang;libcxx;libcxxabi"</code></li>
<li><code>-DCMAKE_INSTALL_PREFIX=directory</code> --- 指定一个绝对地址来存放编译的结果，默认存放在<code> /usr/local</code>.</li>
<li><code>-DCMAKE_BUILD_TYPE=type</code> --- 这是编译的类型，如<code>Debug</code>, <code>Release</code>, <code>RelWithDebInfo</code>, 和 <code>MinSizeRel</code>. 默认的是<code>Debug</code>.</li>
<li><code>-DLLVM_ENABLE_ASSERTIONS=On</code> --- 在启用断言检查的情况下编译（对于Debug构建，默认值为Yes，对于所有其他构建类型，默认值为No）.</li>
</ul>
<h5 data-id="heading-9">Ninja编译</h5>
<p>所以如果需要使用<code>Ninja</code>编译的话命令，需要先创建<code>Ninja</code>模板（大概5分钟），然后再编译：</p>
<pre><code class="copyable">// 创建ninja的目录，并且进入其中
mkdir llvm_ninja && cd llvm_ninja   
// 指定llvm源码目录，新建build目录，创建ninja模板，增加子项目clang，并且模板之后编译的结果放在llvm_release目录下
cmake -S ../llvm-project/llvm -B build -G Ninja -DLLVM_ENABLE_PROJECTS="clang" -DCMAKE_INSTALL_PREFIX=/Volumes/ExDisk/LLVM/llvm_all/llvm_release
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/d6d7b73b8f5e43d185305990ecce2e98~tplv-k3u1fbpfcp-watermark.image" alt="5.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>从上图中可以看到，我们增加的<code>clang</code>参与了编译，而<code>clang-tools-extra</code>没有参与编译。</p>
<p>如果你看到下面这样的结果，那么恭喜<code>ninja</code>模板已经建好
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/2071c92676814009a2e0ab555d4329e0~tplv-k3u1fbpfcp-watermark.image" alt="15.png" loading="lazy" referrerpolicy="no-referrer">
<img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/07df3e5a7d5b4663957b4c0f3c53b81e~tplv-k3u1fbpfcp-watermark.image" alt="6.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>然后进入模板目录，输入命令开始编译</p>
<pre><code class="copyable">cd build
ninja && ninja install
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/3a52f3d264d5493eaa296638f117e1ef~tplv-k3u1fbpfcp-watermark.image" alt="7.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>完成后可以在指定的release目录下看到所有的命令了
<img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/ef6cb88840974fc7b2a1bcf0aa93b98e~tplv-k3u1fbpfcp-watermark.image" alt="8.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h5 data-id="heading-10">Xcode编译</h5>
<p>同样的先在对应的目录下，生成Xcode模板，但xcode就不指定对应的release目录了，因为做iOS开发的应该都知道，Xcode的编译产物有对应的product文件（大概10分钟）</p>
<pre><code class="copyable">mkdir llvm_xcode && cd llvm_xcode
cmake -S ../llvm-project/llvm -B build -G Xcode -DLLVM_ENABLE_PROJECTS="clang" 
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/7e589a5a7eae4224a181eb525fde19b0~tplv-k3u1fbpfcp-watermark.image" alt="9.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>同样，结束后可以看到这样的目录</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/862c88ff15344f6a83f99750ea1e503a~tplv-k3u1fbpfcp-watermark.image" alt="16.png" loading="lazy" referrerpolicy="no-referrer">
<img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/0851e271233f4bfdbcb6b501ce281b9c~tplv-k3u1fbpfcp-watermark.image" alt="10.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>打开LLVM工程，回到了熟悉的画面
<img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/77a0105116bc40e4988f4bd88723c460~tplv-k3u1fbpfcp-watermark.image" alt="11.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>选中Automatically Creat Schemes后，在选择al_build，cmd+b即可开始编译（大概40分钟）。
<img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/7e9b8fca789f4b65a37078e8e1789d3a~tplv-k3u1fbpfcp-watermark.image" alt="12.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>在熟悉的地方可以看到对应的编译产物
<img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/b60eb898dd2048c78c4897073c37e293~tplv-k3u1fbpfcp-watermark.image" alt="13.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>在同级目录下，可以看到对应的命令行工具，比如我们下章需要讲到的clang。
<img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/c66deebafab04d4ebe88960d407b29c9~tplv-k3u1fbpfcp-watermark.image" alt="14.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h1 data-id="heading-11">4、总结</h1>
<p>为什么编译单独拿出来？LLVM就想一个含羞的蒙面女子，大多数人都是只可远观，而不敢亵玩，其实蒙面女子本身也是及其渴望有个勇士来揭开其面纱，而编译自己的LLVM就像是这么一步，只要自己迈出了这一步，那么就是个崭新的世界。</p>
<p>下一章，就会开始聊一些好玩的事情，比如如何编译自己的插件，如何开发自己混淆器，如何开发自己的一门开发语言。</p>
<h1 data-id="heading-12">参考</h1>
<p>1、 <a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.cnblogs.com%2Fqoakzmxncb%2Farchive%2F2013%2F04%2F18%2F3029105.html" target="_blank" rel="nofollow noopener noreferrer" title="https://www.cnblogs.com/qoakzmxncb/archive/2013/04/18/3029105.html" ref="nofollow noopener noreferrer">GCC，LLVM，Clang编译器对比</a><br>
2、 <a href="https://link.juejin.cn/?target=https%3A%2F%2Fzhuanlan.zhihu.com%2Fp%2F98350643" target="_blank" rel="nofollow noopener noreferrer" title="https://zhuanlan.zhihu.com/p/98350643" ref="nofollow noopener noreferrer">微信团队分享的编译优化</a><br>
3、 <a href="https://link.juejin.cn/?target=https%3A%2F%2Flinks.jianshu.com%2Fgo%3Fto%3Dhttps%253A%252F%252Fgithub.com%252Fming1016%252Fstudy%252Fwiki%252F%2525E6%2525B7%2525B1%2525E5%252585%2525A5%2525E5%252589%252596%2525E6%25259E%252590-iOS-%2525E7%2525BC%252596%2525E8%2525AF%252591-Clang---LLVM" target="_blank" rel="nofollow noopener noreferrer" title="https://links.jianshu.com/go?to=https%3A%2F%2Fgithub.com%2Fming1016%2Fstudy%2Fwiki%2F%25E6%25B7%25B1%25E5%2585%25A5%25E5%2589%2596%25E6%259E%2590-iOS-%25E7%25BC%2596%25E8%25AF%2591-Clang---LLVM" ref="nofollow noopener noreferrer">深入剖析 iOS 编译 Clang LLVM</a> <br>
4、 <a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fllvm%2Fllvm-project" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/llvm/llvm-project" ref="nofollow noopener noreferrer">LLVM Github地址</a></p></div>  
</div>
            