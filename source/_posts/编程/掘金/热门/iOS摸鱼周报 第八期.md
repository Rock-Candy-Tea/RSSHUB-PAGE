
---
title: 'iOS摸鱼周报 第八期'
categories: 
 - 编程
 - 掘金
 - 热门
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/628a6de178474c3e90c087744b2b33e4~tplv-k3u1fbpfcp-zoom-1.image'
author: 掘金
comments: false
date: Sun, 11 Apr 2021 18:02:26 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/628a6de178474c3e90c087744b2b33e4~tplv-k3u1fbpfcp-zoom-1.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p><img alt class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/628a6de178474c3e90c087744b2b33e4~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p>iOS摸鱼周报，主要分享大家开发过程遇到的经验教训及学习内容。虽说是周报，但当前内容的贡献途径还未稳定下来，如果后续的内容不足一期，可能会拖更到下一周再发。所以希望大家可以多分享自己学到的开发小技巧和解bug经历。</p>
<p>周报仓库在这里：<a href="https://github.com/zhangferry/iOSWeeklyLearning" target="_blank" rel="nofollow noopener noreferrer">github.com/zhangferry/…</a> ，可以查看README了解贡献方式；另可关注公众号：iOS成长之路，后台点击进群交流，联系我们。</p>
<h2 data-id="heading-0">开发Tips</h2>
<p>开发小技巧收录。</p>
<h3 data-id="heading-1">Github的仓库操作需求token验证</h3>
<p>今天使用一个旧仓库访问Github时，收到一个Deprecation Notice的邮件，说是基于用户名密码的登录方式之后将不再支持，<a href="https://github.blog/2020-12-15-token-authentication-requirements-for-git-operations/" title="2020-12-15-token-authentication-requirements-for-git-operations" target="_blank" rel="nofollow noopener noreferrer">官方通告</a>可以看这里。</p>
<p>当前对于放在github的仓库有两种访问方式：用户名密码、Token。</p>
<p>用户名密码就是使用https访问git仓库。</p>
<p>Token是指私有访问（SSH）、OAuth、GitHub App这三种情况。</p>
<p>在<strong>2021年8月13号</strong>之后，github将不再接受用户名密码的访问形式。受影响的流程包含：</p>
<ul>
<li>命令行访问</li>
<li>桌面应用访问（Github Desktop不受影响）</li>
<li>其他App或者服务使用用户名密码访问直接访问github的情况</li>
</ul>
<p>不受影响的情况：</p>
<ul>
<li>账号具有双重验证功能、SSH访问</li>
<li>使用GitHub Enterprise Server，没有收到Github的更改通知。</li>
<li>其他不支持用户名密码访问的Github App</li>
</ul>
<h3 data-id="heading-2">配置Entitlements</h3>
<p>entitlements是一种授权文件，用于配置相应的操作是否被允许。这个文件会在我们增加Capability的时候自动生成，它的实体是一个plist文件，用于记录我们增加的Capability。打包时entitlements会被放置到MachO文件的Code Signature段中，系统会根据这里的值判断当前应用的权限。</p>
<p>通常一个Target只会有一个entitlements，当如果我们想要根据不同configuration对应不同bundleId时，可能由于某些限制，他们之间的权限能力不同，这时就需要他们拥有不同的entitlements。</p>
<p>我们可以Copy原来的授权文件，重命名，然后在<code>Build Setting > Signing > Code Signing Entitlements </code>中配置刚才新增的entitlements文件。</p>
<p><img alt class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/c4aabfaf50d947cea52c44d16fb91e16~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-3">would clobber existing tag</h3>
<p>在拉取远程tag时会报这种错误，含义是远程tag跟本地有tag冲突。解决方案是找出这个冲突的本地tag，删除掉。</p>
<p>可以通过<code>git ls-remote -t </code>和<code>git tag -l</code>结果进行比对，也可以直接删除本地仓库，重新拉取。</p>
<h2 data-id="heading-4">那些Bug</h2>
<h3 data-id="heading-5">Swift与OC block的差异</h3>
<p>推荐来源：<a href="https://github.com/weiminghuaa" target="_blank" rel="nofollow noopener noreferrer">weiminghuaa</a></p>
<p><strong>Bug现象</strong></p>
<p>原生和web、小程序、flutter等等交互时，传递给原生的是方法名和数据，所以经常需要写方法转发函数，用到performSelector。在OC时，传递block没问题，Swift就不行，可能在performSelector闪退，也可能在block执行的地方闪退</p>
<p><img alt="21617687306_ pic_hd" class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/7a2a88f757ec4e9ab78e70a552178c16~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p><img alt="271617690340_ pic_hd" class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/a368ed191d3e4b4a9ac274deee101c9a~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p><strong>解决方案</strong></p>
<p>swift调用performSelector传参之前，将swift的clourse，显示的转换为oc的block</p>
<pre><code class="hljs language-swift copyable" lang="swift"><span class="hljs-keyword">let</span> block : <span class="hljs-keyword">@convention(block)</span> (<span class="hljs-keyword">Any</span>, <span class="hljs-type">Bool</span>) -> () <span class="hljs-operator">=</span> callback
<span class="copy-code-btn">复制代码</span></code></pre>
<p><a href="https://stackoverflow.com/questions/26374792/difference-between-block-objective-c-and-closure-swift-in-ios" target="_blank" rel="nofollow noopener noreferrer">stackoverflow.com/questions/2…</a></p>
<p><strong>Bug解释</strong></p>
<p>知识点太偏了，难搞。</p>
<p>解题思路记一下：（真正的技术群很关键，讨论才有灵感）
1、刚开始，完全不知所措</p>
<p>2、在开发者群里好友的建议下，分别写了oc和swift的demo，确认oc没问题，swift有问题</p>
<p>3、基于第二点的结果，猜测，swift的closure和oc的block，虽然都是闭包，但毕竟是不同语言，应该是不同实现，大多数情况在项目中通用，但是具体到这里，swift调oc的runtime去传参，把closure传过去，就出问题，无法copy，closure直接在函数结束时销毁了</p>
<p>4、尝试了解block的底层，并了解closure和block的差异，最终找到了可以显示转换的方法</p>
<h2 data-id="heading-6">编程概念</h2>
<h3 data-id="heading-7">什么是VPS</h3>
<p>VPS是Virtual Private Server （虚拟专用服务器）的缩写，它可以将一台物理服务器分割成多个虚拟专享服务器，每个虚拟服务器相互隔离，都有各自的操作系统，磁盘空间及IP地址。使用时VPS就像一台真正的实体服务器，并可以根据用户喜好进行定制。</p>
<p>云服务器跟VPS的概念很像，很多时候他们被混用，但其实还是有区别的。云服务器是VPS的升级版，它不再局限于从一台服务器分离出多个虚拟服务器而是，依托于更先进的集群技术，在一组服务器上虚拟出独立服务器，集群中每个服务器都有云服务器的一个镜像，所以云服务器能保证虚拟服务器的安全与稳定。但如果是VPS，你使用的那台主机发生宕机，你的VPS就无法访问了。</p>
<h3 data-id="heading-8">什么是Ajax</h3>
<p><img alt="image.png" class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/6d63d3ac466947408081267cef25316c~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p>Ajax是Asynchronous Javascript And XML 的缩写，即异步JavaScript和XML，它是一种提高web应用技术交互性的技术方案。</p>
<p>Ajax可以实现在浏览器和服务器之间的异步（不阻塞用户交互）数据传输，并在数据回传至浏览器时局部更新该内容（页面并没有刷新）。这样的好处是即提高了对用户动作的响应又避免了发送多余无用的信息。</p>
<p>第一个著名的Ajax应用是Gmail。</p>
<h3 data-id="heading-9">什么是UTF-8</h3>
<p>UTF-8（8-bit Unicode Transformation Format）是一种Unicode编码形式。Unicode编码是ISO组织制定的包含全球所有文字，符号的编码规范，它规定所有的字符都使用两个字节表示。这样虽然可以包含全球所有文字，但对于仅处于低字节的英文字符也使用两个字节表示，其实是造成了一定程度的空间浪费，于是就有了UTF-8的编码形式。它是动态的使用1-4个字符表示Unicode编码内容的，英文字符占一个字节，此时同ASCII码，中文字符占三个字节。</p>
<p>UTF-8的编码规则总结如下：</p>
<pre><code class="copyable">Unicode符号范围      |        UTF-8编码方式
(十六进制)           |            （二进制）
--------------------+-------------------------------------
0000 0000-0000 007F | 0xxxxxxx
0000 0080-0000 07FF | 110xxxxx 10xxxxxx
0000 0800-0000 FFFF | 1110xxxx 10xxxxxx 10xxxxxx
0001 0000-0010 FFFF | 11110xxx 10xxxxxx 10xxxxxx 10xxxxxx
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这里再强调一下Unicode和UTF-8的区别：<strong>前者是字符集，后者是编码规则</strong>。</p>
<p>UTF-8编码使用非常广泛，在Cocoa编程环境中其作为官方推荐编码方式，在网页端的展示，UTF-8的应用范围也达到了95%左右。</p>
<p>另外两种编码规则UTF-16和UTF-32的最短长度分别为16位和32位，也会造成一部分的字节浪费，所以都没有UTF-8使用更广。</p>
<h3 data-id="heading-10">什么是响应式</h3>
<p>响应式编程（英语：Reactive programming）是一种专注于数据流和变化传递的异步编程范式。面向对象、面向流程都是一种编程范式，他们的区别在于，响应式编程提高了代码的抽象层级，所以你可以只需关注定义了业务逻辑的那些相互依赖的事件，而非纠缠于大量的实现细节。</p>
<p>很多语言都与对应的响应式实现框架，OC：ReactiveCocoa，Swift：RxSwift/Combine，JavaScript：RxJS，Java：RxJava</p>
<p>响应式的关键在于这几点：</p>
<p>数据流：任何东西都可以看做数据流，一次网络请求、一次Click事件、用户输入、变量等。</p>
<p>变化传递：以上这些数据流单独或者组合作用产生了变化，对别的流有了影响，即为变化传递。</p>
<p>异步编程：非阻塞式的，数据流之间互不干涉。</p>
<p>应用示例：假设一个拥有计时器的场景，当用户关闭该页面和退到后台时暂停定时器，当应用回到前台时开启定时器，另外需要有一个地方展示定时器时间。
以下是用RxSwift实现的代码逻辑：</p>
<p><img alt="image.png" class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/25cf00e7e1274de286bf252e552e8006~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-11">什么是Catalyst</h3>
<p><img alt="image.png" class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/ea7a60c8b0e8445c9fd67940515248c3~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p>背景：苹果生态中，长期以来，移端和电脑端的App并不通用，开发者必须写两次代码，设计两套UI界面，才能分别为两个平台制作对应的App。这也直接导致了iOS应用百花齐放，macOS应用却凄凄惨惨戚戚。</p>
<p>Mac Catalyst 正是解决这一问题的技术方案，苹果在19年WWDC上发布它，开发者可以将iPad 应用移植到macOS上，之后也会支持iOS应用的移植。它的意义在于我们可以直接使用UIKit开发macOS应用，BigSur上的短信和地图均使用Mac Catalyst重写过。<code>Write once，run anywhere</code>是苹果的最终目标。</p>
<p>Mac Catalyst已被集成进了Xcode（11.0版本及之后），在平台选择选项框中找到mac选项，选中即可，Catalyst功能只有在Catalina及之后的系统版本才能使用。</p>
<h3 data-id="heading-12">什么是DSL</h3>
<p>DSL（Domain Specific Language）即特定领域语言，与DSL相对的就是GPL，这里的 GPL 并不是我们知道的开源许可证，而是 General Purpose Language 的简称，即通用编程语言，也就是我们非常熟悉的 Objective-C、Swift、Python 以及 C 语言等等。</p>
<p>DSL是为了解决某一类任务而专门设计的计算机语言，其通过在表达能力上做的妥协换取在某一领域内的高效。</p>
<p>DSL包含外部DSL和内部DSL，外部DSL包括：Regex、SQL、HTML&CSS</p>
<p>内部DSL包括：基于Ruby构建的项目配置，Podfile、Gemfile、Fastfile文件里的语法</p>
<p>参考资料：<a href="https://draveness.me/dsl/" target="_blank" rel="nofollow noopener noreferrer">draveness.me/dsl/</a></p>
<h2 data-id="heading-13">优秀博客</h2>
<p>1、<a href="https://juejin.cn/post/6943384976909942815" title="我离职了" target="_blank">我离职了</a> -- 来自掘金：敖丙</p>
<p>敖丙还在B站录了<a href="https://www.bilibili.com/video/BV1cp4y1a7DW" title="我离职了 B站" target="_blank" rel="nofollow noopener noreferrer">视频</a>，看视频可能更有感染力。</p>
<p>2、<a href="http://xelz.info/blog/2017/02/18/lego-cube-solver/" title="我的玩具——乐高魔方机器人" target="_blank" rel="nofollow noopener noreferrer">我的玩具——乐高魔方机器人</a> -- 来自博客：xelz's blog</p>
<p>这个真的非常有意思，有理工科思维做一件具体有趣的事情非常酷。大概思路是这样的;</p>
<ul>
<li>手机与LEGO通过蓝牙连接</li>
<li>LEGO检测到魔方放入之后通知手机开始扫描</li>
<li>手机扫描完一个面之后，通知LEGO将魔方翻转到下一个面</li>
<li>扫描完毕后，手机开始计算还原步骤</li>
<li>手机通过蓝牙将还原公式发送给LEGO</li>
<li>LEGO按照公式将魔方还原</li>
</ul>
<p>3、<a href="http://xelz.info/blog/2018/11/24/all-you-need-to-know-about-bitcode/" title="关于bitcode, 知道这些就够了" target="_blank" rel="nofollow noopener noreferrer">关于bitcode, 知道这些就够了</a> -- 来自博客：xelz's blog</p>
<p>4、<a href="https://mp.weixin.qq.com/s/5Ez2BrsyBgQ8aHZqlYtAjg" title="哈啰出行iOS App首屏秒开优化" target="_blank" rel="nofollow noopener noreferrer">哈啰出行iOS App首屏秒开优化</a> -- 来自公众号：哈罗技术团队</p>
<p>5、<a href="https://mp.weixin.qq.com/s/PX8bXSFXgJWMgHqien85jQ" title="SwiftUI: Text 中的插值" target="_blank" rel="nofollow noopener noreferrer">SwiftUI: Text 中的插值</a> -- 来自公众号：老司机技术周报</p>
<p>6、<a href="https://mp.weixin.qq.com/s/z8s4urq_KCf2ny5kKOYMHA" target="_blank" rel="nofollow noopener noreferrer">深入理解MachO数据解析规则</a> -- 来自公众号：iOS成长之路</p>
<p>7、<a href="https://mp.weixin.qq.com/s/LMeO6chdac65JQu1Yy2-Iw" target="_blank" rel="nofollow noopener noreferrer">MacBook 升级 SSD 硬盘指北</a> -- 来自公众号：iOS成长之路</p>
<p>8、<a href="https://mp.weixin.qq.com/s/s8iwQLNtla5nxF_Tmj2wJg" title="DWARF文件初探——提取轻量符号表" target="_blank" rel="nofollow noopener noreferrer">DWARF文件初探——提取轻量符号表</a> -- 来自公众号：皮拉夫大王在此</p>
<h2 data-id="heading-14">学习资料</h2>
<h3 data-id="heading-15">Can Balkaya</h3>
<p>Can Balkaya是WWDC20的学生挑战赛冠军，当前在Medium开了<a href="https://canbalkaya.blog/" title="Can Balkaya" target="_blank" rel="nofollow noopener noreferrer">专栏</a>，经常发布一些介绍Swift特性相关的文章，质量都很高。我在别的地方看到有人翻译过里面部分文章，说明它还是有一定关注度的，如果英文稍微好些的可以直接订阅这个专栏来看。</p>
<p><img alt class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/9a051146413b4cb3aad15072de8af995~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-16">工具推荐</h2>
<p>推荐好用的工具。</p>
<h3 data-id="heading-17">Cleaner for Xcode</h3>
<p><strong>推荐来源</strong>：zhangferry</p>
<p><strong>地址</strong>：<a href="https://github.com/waylybaye/XcodeCleaner-SwiftUI" target="_blank" rel="nofollow noopener noreferrer">github.com/waylybaye/X…</a></p>
<p><strong>软件状态</strong>：开源版本免费，AppStore版本$0.99</p>
<p><strong>使用介绍</strong></p>
<p>这个应用可以帮助你清除遗留以及废弃文件，从而极大的节省硬盘空间。 你可以每月或者每周运行一次进行清理。</p>
<p><img alt class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/9690e877a3ee497d911497e3fb9289d0~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-18">JSONExport</h2>
<p><strong>推荐来源</strong>：春起梨花开</p>
<p><strong>地址</strong>：<a href="https://github.com/Ahmed-Ali/JSONExport" target="_blank" rel="nofollow noopener noreferrer">github.com/Ahmed-Ali/J…</a></p>
<p><strong>软件状态</strong>：免费，开源</p>
<p><strong>使用介绍</strong></p>
<p>支持JSON文件直接导出为开发中使用的Model类型。支持Java，Objective-C，Swift等语言的数据模型。</p>
<p>对于一些适配CoreData、Realm的特殊格式也可以完整适配。</p>
<p><img alt class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/69852333e5994c11bd2dd26b2fb9121c~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-19">联系我们</h2>
<p><a href="https://zhangferry.com/2021/01/10/iOSWeeklyLearning_3/" target="_blank" rel="nofollow noopener noreferrer">摸鱼周报第三期</a></p>
<p><a href="https://zhangferry.com/2021/01/24/iOSWeeklyLearning_4/" target="_blank" rel="nofollow noopener noreferrer">摸鱼周报第四期</a></p>
<p><a href="https://zhangferry.com/2021/02/28/iOSWeeklyLearning_5/" target="_blank" rel="nofollow noopener noreferrer">摸鱼周报第五期</a></p>
<p><a href="https://zhangferry.com/2021/03/14/iOSWeeklyLearning_6/" target="_blank" rel="nofollow noopener noreferrer">摸鱼周报第六期</a></p>
<p><a href="https://zhangferry.com/2021/03/28/iOSWeeklyLearning_7/" target="_blank" rel="nofollow noopener noreferrer">摸鱼周报第七期</a></p></div> <div class="image-viewer-box" data-v-78c9b824><!----></div>  
</div>
            