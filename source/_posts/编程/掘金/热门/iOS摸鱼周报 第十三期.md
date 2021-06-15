
---
title: 'iOS摸鱼周报 第十三期'
categories: 
 - 编程
 - 掘金
 - 热门
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/7b2ddf8438884b7b91881b704b742cb3~tplv-k3u1fbpfcp-zoom-1.image'
author: 掘金
comments: false
date: Sun, 30 May 2021 18:26:18 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/7b2ddf8438884b7b91881b704b742cb3~tplv-k3u1fbpfcp-zoom-1.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/7b2ddf8438884b7b91881b704b742cb3~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>iOS摸鱼周报，主要分享开发过程中遇到的经验教训、优质的博客、高质量的学习资料、实用的开发工具等。周报仓库在这里：<a href="https://github.com/zhangferry/iOSWeeklyLearning" target="_blank" rel="nofollow noopener noreferrer">github.com/zhangferry/…</a> ，如果你有好的的内容推荐可以通过 issue 的方式进行提交。另外也可以申请成为我们的常驻编辑，一起维护这份周报。另可关注公众号：iOS成长之路，后台点击进群交流，联系我们，获取更多内容。</p>
<h2 data-id="heading-0">开发Tips</h2>
<p>整理编辑：<a href="https://github.com/renmoqiqi" target="_blank" rel="nofollow noopener noreferrer">人魔七七</a></p>
<h3 data-id="heading-1">CocoaPods 常见操作</h3>
<h4 data-id="heading-2">pod install</h4>
<p>当我们的工程首次使用 Cocoapods 管理第三方库的时候或者当我们每次编辑 Podfile 文件的时候比如：添加，删除或者编辑一个 pod 库的时候，都需要执行该命令。</p>
<ul>
<li>首次执行 <code>pod install</code> 命令，会下载安装新的 pod，并把每个 pod 的版本写到 Podfile.lock 文件里。这个文件跟踪所有的 pod 库及其依赖的版本并锁定他们的版本号。</li>
<li>在存在 Podfile.lock 的情况下执行 <code>pod install</code> 的时候，只解析 Podfile.lock 中没有列出的pod依赖项。1. 对于Podfile.lock 列出的版本，不需要检查 pods 是否有更新直接使用既有的版本安装。2. 对于Podfile.lock 未列出的版本，会根据Podfile 描述的版本安装。</li>
</ul>
<p>Podfile 文件是 pod 执行的核心文件，它的解析逻辑推荐看这篇：<a href="https://www.desgard.com/2020/09/16/cocoapods-story-4.html" title="Podfile 的解析逻辑" target="_blank" rel="nofollow noopener noreferrer">Podfile 的解析逻辑</a>。</p>
<h4 data-id="heading-3">pod update</h4>
<p>pod update 可以全局升级，也可以指定 podName 单个升级。当我们执行 <code>pod update podName</code> 的时候，会忽略 Podfile.lock 文件的版本，根据 Podfile 的定义尽可能更新到最新的版本，并更新 Podfile.lock 文件。该命令会同样适配于 pod 库 podspec文件内部定义的依赖。 可以通过<code>pod outdated</code> 检测出过期的依赖版本和可升级版本。</p>
<p>对于 install 和 update 有两个常用参数：</p>
<ul>
<li>--repo-update：该参数会更新所有的 repo，例如该更新了一个私有库版本，直接 install 是找不到对应版本的，我们不想更新所有的依赖库，只想更新 对应的 repo，就可以使用该指令。该参数还对应一个特有命令：<code>pod repo update</code>。</li>
<li>--no-repo-update：update 操作会默认更新所有 repo，有时这并不是必须的，且该步骤会同步 pod 公有 repo，导致比较耗时，这时就可以增加该参数，用于关闭该更新操作。</li>
</ul>
<h3 data-id="heading-4">CocoaPods 使用建议</h3>
<ul>
<li>
<p>推荐使用 Gemfile 管理 pod 版本，每次执行 pod 通过 bundle 进行，例如： <code>bundle exec pod install</code> 。</p>
</li>
<li>
<p>工程持有管理者对项目进行 CocoaPods 初始化的时候会有一个 Podfile.lock 这个文件我们需要纳入版本控制里。</p>
</li>
<li>
<p>如果需要更新某个库到某一个版本，由项目持有管理者采用 <code>pod update podName</code> 的方式更新某个库到一定的版本。然后提交 Podfile.lock 和 Podfile 文件。</p>
</li>
</ul>
<h2 data-id="heading-5">那些Bug</h2>
<p>整理编辑：<a href="https://zhangferry.com/" target="_blank" rel="nofollow noopener noreferrer">zhangferry</a></p>
<h3 data-id="heading-6">module compiled with Swift 5.3.2 cannot be imported by the Swift 5.3 compiler: **.swiftmodule</h3>
<p><strong>问题背景</strong></p>
<p>通过某个版本的 Xcode 生成的 Swift 库（Framework），在另一台机器（不同版本 Xcode）无法识别，报上述错误。</p>
<p><strong>问题分析</strong></p>
<p>该错误是由于编译器不兼容导致的，错误含义是由 Swift 5.3.2 编译器（编译器版本可以通过 <code>swift --version</code>查看）编译的module，特指 <code>swiftmodule</code> 文件，无法被 Swift 5.3 的编译器所识别。<code>swiftmodule</code>文件用于描述Swift内部的方法声明，它是二进制格式的，会根据不同的架构生成不同的版本。但也正因为其二进制格式的特性，无法跟随编译器的升级进行调整。这个问题对应的就是 ABI 稳定中的 module stability。这里引用喵神的一段<a href="https://onevcat.com/2019/02/swift-abi/" title="Swift ABI 稳定对我们到底意味着什么" target="_blank" rel="nofollow noopener noreferrer">博客</a>内容：</p>
<blockquote>
<p>ABI 稳定是使用 binary 发布框架的必要非充分条件。框架的 binary 在不同的 runtime 是兼容了，但是作为框架，现在是依靠一个 <code>.swiftmodule</code> 的二进制文件来描述 API Interface 的，这个二进制文件中包含了序列化后的 AST (更准确说，是 interface 的 SIL)，以及编译这个 module 时的平台环境 (Swift 编译器版本等)。</p>
<p>ABI 稳定并不意味着编译工具链的稳定，对于框架来说，想要用 binary 的方式提供框架，除了 binary 本身稳定以外，还需要描述 binary 的方式 (也就是现在的 swiftmodule) 也稳定，而这正在开发中。将来，Swift 将为 module 提供文本形式的 <code>.swiftinterface</code> 作为框架 API 描述，然后让未来的编译器根据这个描述去“编译”出对应的 <code>.swiftmodule</code> 作为缓存并使用。</p>
<p>这一目标被称为 module stability，当达到 module stability 后，你就可以使用 binary 来发布框架了。</p>
</blockquote>
<p><strong>问题解决</strong></p>
<p>上面说的 module stability 已经实现了，就是可以通过 <code>.swiftinterface</code> 文件描述二进制包。它的实现对应一个编译参数<code>-enable-library-evolution</code>，在 Build Setting 里就是 <code>Build Libraries for Distribution</code>，我们将其设置为 YES ，生成的 Framework 里就会包含对应的 <code>.swiftinterface</code> 文件，就能实现不同版本编译器之间的兼容问题。</p>
<p>但到这里还没完全结束，遇到了另一个问题：</p>
<pre><code class="copyable">/*.framework/Modules/*.swiftmodule/arm64-apple-ios.swiftinterface:5:8: cannot load underlying module for 'SnapKit'

failed to build module '*' from its module interface; the compiler that produced it, 'Apple Swift version 5.3.2 (swiftlang-1200.0.45 clang-1200.0.32.28)', may have used features that aren't supported by this compiler, 'Apple Swift version 5.3 (swiftlang-1200.0.29.2 clang-1200.0.30.1)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>按理说有了 <code>swiftinterface</code> 应该不会出现编译不兼容问题了，但还是出现了，虽然提示内容有些不太一样，这里会多出一个内部依赖库的问题。这里查看对应版本的 <code>swiftinterface</code> 文件：</p>
<pre><code class="copyable">// swift-interface-format-version: 1.0
// swift-compiler-version: Apple Swift version 5.3.2 (swiftlang-1200.0.45 clang-1200.0.32.28)
// swift-module-flags: -target arm64-apple-ios10.0 -enable-objc-interop -enable-library-evolution -swift-version 5 -enforce-exclusivity=checked -Onone -module-name ZYModule
import Foundation
import SnapKit
import Swift
import UIKit
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这里除了声明编译器信息外，还把依赖库 SnapKit 也写入了进去，所以这里猜测的隐含逻辑就是二进制库做了 <code>Build Libraries for Distribution</code> ，其依赖的其他库也绑定了对应的编译器版本信息，在工程里使用源码编译的 SnapKit 对于了其当前编译版本（5.3），与二进制库所生成的版本（5.3.2）不一致，所以才导致了该问题。我尝试修改项目里 Pod库 的 <code>Build Libraries for Distribution</code> 选项：</p>
<pre><code class="hljs language-ruby copyable" lang="ruby">post_install <span class="hljs-keyword">do</span> <span class="hljs-params">|installer|</span>
  installer.pods_project.targets.each <span class="hljs-keyword">do</span> <span class="hljs-params">|target|</span>
   target.build_configurations.each <span class="hljs-keyword">do</span> <span class="hljs-params">|config|</span>
    config.build_settings[<span class="hljs-string">'BUILD_LIBRARY_FOR_DISTRIBUTION'</span>] = <span class="hljs-string">'YES'</span>
   <span class="hljs-keyword">end</span>
  <span class="hljs-keyword">end</span>
<span class="hljs-keyword">end</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>问题得到解决，编译通过！</p>
<h2 data-id="heading-7">编程概念</h2>
<p>整理编辑：<a href="https://juejin.cn/user/782508012091645" target="_blank">师大小海腾</a>，<a href="https://zhangferry.com/" target="_blank" rel="nofollow noopener noreferrer">zhangferry</a></p>
<h3 data-id="heading-8">什么是 BIOS</h3>
<p>BIOS 全称为 Basic Input Output System，即基本输入输出系统。BIOS 是预先内置在计算机主机内部的程序，也是计算机开机后加载的第一个程序。BIOS 保存着计算机最重要的基本输入输出的程序、开机后自检程序和系统自启动程序，它可从 CMOS（是电脑主板上的一块可读写的 RAM 芯片）中读写系统设置的具体信息。</p>
<p>BIOS 除了键盘，磁盘，显卡等基本控制程序外，还有<code>引导程序</code>的功能。引导程序是存储在启动驱动器起始区域的小程序，操作系统的启动驱动器一般是硬盘。不过有时也可能是 CD-ROM 或软盘。</p>
<p>电脑开机后，BIOS 会确认硬件是否正常运行，没有异常的话就会直接启动引导程序，引导程序的功能就是把在硬盘等记录的 OS 加载到内存中运行，虽然启动应用是 OS 的功能，但 OS 不可以自己启动自己，而是通过引导程序来启动。</p>
<p>制作黑苹果的时候安装的 Clover 就是一个启动程序，它通过修改 BIOS 配置，让 BIOS 首先执行它，然后由它来引导至 MacOS 的启动。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/040e5fb61546468a99feb3a23ed2c5b0~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>严格意义来说 BIOS 是 IBM PC架构上的一种设计规范，Mac电脑，包括一些新型的主板都没有 BIOS 这一概念，取而代之的是 EFI/UEFI。</p>
<h3 data-id="heading-9">什么是汇编</h3>
<p>汇编语言（Assembly Language）是任何一种用于电子计算机、微处理器、微控制器或其他可编程器件的低级语言，亦称为符号语言。在汇编语言中，用助记符代替机器指令的操作码，用地址符号或标号代替指令或操作数的地址。在不同的设备中，汇编语言对应着不同的机器语言指令集，通过汇编过程转换成机器指令。特定的汇编语言和特定的机器语言指令集是一一对应的，不同平台之间不可直接移植。</p>
<p>汇编语言比机器语言的可读性要好，但跟高级语言比较而言，可读性还是较差。不过采用它编写的程序具有存储空间占用少、执行速度快的特点，这些是高级语言所无法取代的。在实际应用中，是否使用汇编语言，取决于具体应用要求、开发时间和质量等方面作权衡。汇编常用的指令如下：</p>








































<table><thead><tr><th>操作码</th><th>操作数</th><th>功能</th></tr></thead><tbody><tr><td>mov</td><td>A, B</td><td>把B的值赋给A</td></tr><tr><td>and</td><td>A, B</td><td>把A和B同时相加，并把结果赋给A</td></tr><tr><td>push</td><td>A</td><td>把A的值存储在栈中</td></tr><tr><td>pop</td><td>A</td><td>从栈中读出值，并将其赋值给A</td></tr><tr><td>call</td><td>A</td><td>调用函数A</td></tr><tr><td>ret</td><td>无</td><td>处理返回给调用源函数</td></tr></tbody></table>
<h3 data-id="heading-10">什么是虚拟机</h3>
<p>虚拟机（Virtual Machine）是指通过软件模拟的具有完整硬件系统功能的、运行在一个完全隔离环境中的完整计算机系统。在实体计算机中能够完成的工作在虚拟机中都能够实现。在计算机中创建虚拟机时，需要将实体机的部分硬盘和内存容量作为虚拟机的硬盘和内存容量。每个虚拟机都有独立的 CMOS、硬盘和操作系统，可以像使用实体机一样对虚拟机进行操作。</p>
<p>虚拟机的主要用处有：</p>
<ol>
<li>演示环境，可以安装各种演示环境，便于做各种例子</li>
<li>保证主机的快速运行，减少不必要的垃圾安装程序，偶尔使用的程序，或者测试用的程序在虚拟机上运行</li>
<li>避免每次重新安装，银行等常用工具，不经常使用，而且要求保密比较好的，单独在一个环境下面运行</li>
<li>想测试一下不熟悉或者有风险的应用，在虚拟机中随便安装和彻底删除</li>
<li>体验不同版本的操作系统，如 Linux、Mac 等。</li>
</ol>
<p>虚拟机目前可分为三类：</p>
<ul>
<li>系统虚拟机，例如：VMware</li>
<li>程序虚拟机，例如：JVM（Java Virtual Machine）</li>
<li>操作系统层虚拟化，例如：Docker</li>
</ul>
<h3 data-id="heading-11">什么是外围中断</h3>
<p>IRQ（Interrupt Request）代表的就是中断请求。IRQ 是用来暂停当前正在运行的程序，并跳转到其他程序运行的必要机制。该机制被称为处理中断。中断处理在硬件控制中担当着重要的角色。因为如果没有中断处理，就有可能无法顺畅进行处理的情况。</p>
<p>从中断处理开始到请求中断的程序（中断处理程序）运行结束之前，被中断的程序（主程序）的处理是停止的。这种情况就类似于在处理文档的过程中有电话打进来，电话就相当于是中断处理。假如没有中断处理的发生，就必须等到文档处理完成后才能够接听电话。由此可见，中断处理有着巨大的价值，就像是接听完电话后会返回原来的文档作业一样，中断程序处理完成后，也会返回到主程序中继续。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/6872f3f34f964db9922c0ccaeedba81e~tplv-k3u1fbpfcp-zoom-1.image" alt="中断请求示意图" loading="lazy" referrerpolicy="no-referrer"></p>
<p><strong>实施中断请求的是连接外围设备的 I/O 控制器，负责实施中断处理的是 CPU。</strong></p>
<p>假如有多个外围设备进行中断请求的话， CPU 需要做出选择进行处理，为此，我们可以在 I/O 控制器和 CPU 中间加入名为中断控制器的 IC 来进行缓冲。中断控制器会把从多个外围设备发出的中断请求有序的传递给 CPU。中断控制器的功能相当于就是缓冲。下面是中断控制器功能的示意图</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/59d32c87764641a8b3f15e033d981101~tplv-k3u1fbpfcp-zoom-1.image" alt="中断控制器的功能" loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-12">什么是 DMA</h3>
<p>DMA 全称为 Direct Memory Access，即直接存储器访问。DMA 是一种内存访问机制，它是指在不通过 CPU 的情况下，外围设备直接和主存进行数据传输。磁盘等硬件设备都用到了 DMA 机制，通过 DMA，大量数据就可以在短时间内实现传输，之所以这么快，是因为 CPU 作为中介的时间被节省了，下面是 DMA 的传输过程</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/aec6eab2189f4f759772990f42dfc982~tplv-k3u1fbpfcp-zoom-1.image" alt="使用 DMA 的外部设备和不使用 DMA 的外部设备" loading="lazy" referrerpolicy="no-referrer"></p>
<p>I/O 端口号、IRQ、DMA 通道可以说是识别外围设备的 3 点组合。不过，IRQ、DMA 通道并不是所有外围设备都具备的。计算机主机通过软件控制硬件时所需要的信息的最低限，是外围设备的 I/O 端口号。IRQ 只对需要中断处理的外围设备来说是必须的，DMA 通道则只对需要 DMA 机制的外围设备来说必须的。</p>
<h2 data-id="heading-13">优秀博客</h2>
<p>整理编辑：<a href="https://www.jianshu.com/u/739b677928f7" target="_blank" rel="nofollow noopener noreferrer">皮拉夫大王在此</a></p>
<p>本期博客汇总的主题是 <code>watchdog</code></p>
<p>1、<a href="https://www.jianshu.com/p/6cf4aeced795" title="iOS watchdog (看门狗机制)" target="_blank" rel="nofollow noopener noreferrer">iOS watchdog (看门狗机制)</a> -- 来自简书：Mr_Xie</p>
<p>先来简单了解什么是 watchdog。</p>
<p>2、<a href="http://www.cocoachina.com/articles/27303" title="iOS App 后台任务的坑" target="_blank" rel="nofollow noopener noreferrer">iOS App 后台任务的坑</a> -- 来自cocoachina ：米米狗</p>
<p>后台任务泄漏是导致触发 watchdog 常见情况之一，还有一种情况就是主线程卡死，文章中有介绍如何区分。</p>
<p>3、<a href="https://developer.apple.com/documentation/xcode/addressing-watchdog-terminations" title="Addressing Watchdog Terminations" target="_blank" rel="nofollow noopener noreferrer">Addressing Watchdog Terminations</a></p>
<p>苹果的官方文档。对我个人而言，了解 scene-create 和 scene-update 的含义在排查问题过程中起到了一定的作用。</p>
<p>4、<a href="https://zhuanlan.zhihu.com/p/99232749" title="你的 App 在 iOS 13 上被卡死了吗" target="_blank" rel="nofollow noopener noreferrer">你的 App 在 iOS 13 上被卡死了吗</a></p>
<p>进入实践阶段，其实我们很少真的在主线程做大量耗时操作如网络请求等。触发 watchdog 往往是不经意的，甚至你不会怀疑你的代码有任何问题。这篇文章介绍的是 58 同城团队如何定位到剪切板造成的启动卡死。</p>
<p>5、<a href="https://juejin.cn/post/6937091641656721438" title="iOS 稳定性问题治理：卡死崩溃监控原理及最佳实践" target="_blank">iOS 稳定性问题治理：卡死崩溃监控原理及最佳实践</a></p>
<p>这篇文章是字节跳动 APM 团队早些时候发表的，是业界少有的公开介绍卡死崩溃的原因的文章，具有很强的借鉴意义。我们在做启动卡死优化的过程中，文中提到的相关问题基本都有遇到，只不过在此之前并不知道什么原因以及如何解决。所以说如果你想做卡死治理，可以参考下这篇文章。</p>
<p>6、<a href="https://mp.weixin.qq.com/s/kv-_oZObp7QRHeAbrkdfsA" title="面试过500+位候选人之后，想谈谈面试官视角的一些期待" target="_blank" rel="nofollow noopener noreferrer">面试过 500+ 位候选人之后，想谈谈面试官视角的一些期待</a></p>
<p>《iOS 稳定性问题治理：卡死崩溃监控原理及最佳实践》的作者在面试了 500+ 候选人后写的文章，有需要的同学可以针对性的做些准备。</p>
<p>7、<a href="https://juejin.cn/post/6967199105541996575" title="论证：iOS安全性，为什么需要审核？" target="_blank">论证：iOS安全性，为什么需要审核？</a></p>
<p><a href="https://github.com/iHTCboy" target="_blank" rel="nofollow noopener noreferrer">@iHTCboy</a>：从辩论的视角分析 iOS 安全性，同时与 macOS 安全性进行对比，提出了让 iOS 更加安全的建议，文中同时也总结了非常多 iOS 和 macOS 安全技术小知识，可以让大家在短时间里快速入门和重温 Apple OS 安全性知识点。</p>
<h2 data-id="heading-14">学习资料</h2>
<p>整理编辑：<a href="https://juejin.cn/user/1433418892590136" target="_blank">Mimosa</a></p>
<h3 data-id="heading-15">喵神预告：新书，开工！</h3>
<p><a href="https://weibo.com/onevcat" target="_blank" rel="nofollow noopener noreferrer">喵神</a>关于 <code>async-swift</code> 的书开工了。是关于Swift5.5的新特性<strong>协程</strong>，待书籍完工的第一时间我们会通过周报再通知到大家。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/ce977d61f5dc4a00ba4e8fccbc6480cc~tplv-k3u1fbpfcp-zoom-1.image" alt="New Book! Go!" loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-16">30 seconds of code</h3>
<p>地址：<a href="https://www.30secondsofcode.org/" target="_blank" rel="nofollow noopener noreferrer">www.30secondsofcode.org/</a></p>
<p>该网站的口号是：「能找到满足你所有开发需求的代码片段！」，他有许多语言的常用代码片段（Code Snippets），例如排序算法、hex 转 rgb、时间转换等等，能让你轻松地找到各个语言的这些常用代码，让你的开发效率大大提升！（可惜目前还没有 <code>Swift</code> 的板块🥲</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/0acdd3847e4e4f41a34f00aac2d9c331~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-17">工具推荐</h2>
<p>整理编辑：<a href="https://zhangferry.com/" target="_blank" rel="nofollow noopener noreferrer">zhangferry</a></p>
<h3 data-id="heading-18">Whatpulse</h3>
<p><strong>地址</strong>：<a href="https://whatpulse.org/" target="_blank" rel="nofollow noopener noreferrer">whatpulse.org/</a></p>
<p><strong>软件状态</strong>：基础功能免费，高级功能付费</p>
<p><strong>使用介绍</strong></p>
<p>Whatpulse是一个电脑使用检测统计软件，它可以统计你每天的键盘、鼠标、网络等情况的使用详情并将其做成简单的统计表格，用于分析每天的电脑使用情况。</p>
<p>翻到一张之前公司电脑使用该软件将近一年的留存成果，100万+ 按键次数，使用最多的竟然是删除键。。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/c6f223e7ac5f4967bdf175c7172188ea~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<h1 data-id="heading-19">OctoMouse</h1>
<p><strong>地址</strong>：<a href="https://konsomejona.github.io/OctoMouse/index.html" target="_blank" rel="nofollow noopener noreferrer">konsomejona.github.io/OctoMouse/i…</a></p>
<p><strong>软件状态</strong>：免费，<a href="https://github.com/KonsomeJona/OctoMouse" target="_blank" rel="nofollow noopener noreferrer">开源</a></p>
<p><strong>使用介绍</strong></p>
<p>该软件主要用于统计键盘及鼠标的行为信息，比较有意思的是，它对鼠标的统计会包含移动距离参数。可以试试看多久才能让鼠标移动 5km。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/afd8229563f541b7955ab0da2c82fc9e~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-20">联系我们</h2>
<p><a href="https://zhangferry.com/2021/04/11/iOSWeeklyLearning_8/" target="_blank" rel="nofollow noopener noreferrer">iOS摸鱼周报 第八期</a></p>
<p><a href="https://zhangferry.com/2021/04/24/iOSWeeklyLearning_9/" target="_blank" rel="nofollow noopener noreferrer">iOS摸鱼周报 第九期</a></p>
<p><a href="https://zhangferry.com/2021/05/05/iOSWeeklyLearning_10/" target="_blank" rel="nofollow noopener noreferrer">iOS摸鱼周报 第十期</a></p>
<p><a href="https://zhangferry.com/2021/05/16/iOSWeeklyLearning_11/" target="_blank" rel="nofollow noopener noreferrer">iOS摸鱼周报 第十一期</a></p>
<p><a href="https://zhangferry.com/2021/05/22/iOSWeeklyLearning_12/" target="_blank" rel="nofollow noopener noreferrer">iOS摸鱼周报 第十二期</a></p></div>  
</div>
            