
---
title: 'iOS摸鱼周报 第五期'
categories: 
 - 编程
 - 掘金
 - 热门
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/2f11c724288c42a694c79bfb3591ba79~tplv-k3u1fbpfcp-zoom-1.image'
author: 掘金
comments: false
date: Sun, 28 Feb 2021 18:26:40 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/2f11c724288c42a694c79bfb3591ba79~tplv-k3u1fbpfcp-zoom-1.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p><img alt class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/2f11c724288c42a694c79bfb3591ba79~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p>iOS摸鱼周报，主要分享大家开发过程遇到的经验教训及学习内容。虽说是周报，但当前内容的贡献途径还未稳定下来，如果后续的内容不足一期，可能会拖更到下一周再发。所以希望大家可以多分享自己学到的开发小技巧和解bug经历。</p>
<p>周报仓库在这里：<a href="https://github.com/zhangferry/iOSWeeklyLearning" target="_blank" rel="nofollow noopener noreferrer">github.com/zhangferry/…</a> ，可以查看README了解贡献方式；另可关注公众号：iOS成长之路，后台点击进群交流，联系我们。</p>
<h2 data-id="heading-0">开发Tips</h2>
<p>开发小技巧收录。</p>
<h3 data-id="heading-1">UML图关系</h3>
<p>UML图中的关系表达形式很容易记混，这里参照下图可以便于我们记忆：</p>
<p><img alt class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/af1c26c786134520a1a0eaef1babfcf9~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p>实现关系：描述接口和类之间的关系，对应Java里interface的实现，在Swift里就是protocol的实现。</p>
<p>泛化关系又叫继承关系：由子类指向父类</p>
<p>关联关系：指对象与对对象之间的连接，一个对象包含另一个对象的引用（一般为属性）。用实心单或者双箭头表示。有时需要表示关联一个或者多个。</p>
<p>关联关系其他几种特殊类型：</p>
<p>聚合关系：体现了整体与部分的拥有关系，汽车<code>has a</code>轮胎、发动机，发动机没有汽车无法单独存在，这里轮胎和发动机通常是封装在汽车内不可见的。</p>
<p>组合关系：体现了整体与部分的包含关系，班级<code>contains a</code>学生，学生和班级可以独立存在，学生和班级可以单独存在，学生依赖班级，这里的关系通常两者都是可见的。</p>
<p>依赖关系：是一种弱关联关系（非属性），常见的局部变量，静态方法，方法参数、返回值等都是依赖关系。</p>
<h3 data-id="heading-2">个人开发者账号的限制</h3>
<p>部门申请了一个备用的个人开发者账号，发现邀请别人加入时无法分配证书管理权限，经过调研发现不同类型的开发者账号权限是不同的。它们区别大致如下：</p>









































<table><thead><tr><th></th><th>注册是否需要邓白氏码</th><th>费用</th><th>是否可以上架App Store</th><th>支持证书类型</th><th>测试设备</th><th>协作人数</th></tr></thead><tbody><tr><td>个人账号</td><td>否</td><td>$99</td><td>可以</td><td>Ad Hoc + App Store</td><td>100</td><td>开发者自己</td></tr><tr><td>公司账号</td><td>是</td><td>$99</td><td>可以</td><td>Ad Hoc + App Store</td><td>100</td><td>多人</td></tr><tr><td>企业账号</td><td>是</td><td>$299</td><td>不可以</td><td>In-Hourse & Ad Hoc</td><td>无限制</td><td>多人</td></tr></tbody></table>
<p>个人账号和公司账号功能基本一样，不同之处就在于协作人数，这里协作人数可以理解为证书的管理权限。在个人开发者账号下，我们可以在AppStoreConnect里邀请开发者，并可以选择提供给他们管理者、开发者等身份，但是在开发者资源一栏的选项却是置灰不可选的。</p>
<p><img alt class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/afe4cc9f533d4ecfacec1571cdaca532~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p>也就是说个人开发者只能由账号购买者单独管理证书。</p>
<h3 data-id="heading-3">Swift类型的Framework合并</h3>
<p>对于使用Objective-C开发的Framework，在真机和模拟器两种类型下，他们的区别就在于编译出的执行文件是适合于何种CPU架构。而对于Swift开发的Framework，区别则不仅限于执行文件。比如我们用真机（arm64 & armv7）编译出SnapKit这个Framework，它的目录是这样的：</p>
<pre><code class="copyable">├── Headers
│   └── SnapKit-Swift.h
├── Info.plist
├── Modules
│   ├── SnapKit.swiftmodule
│   │   ├── Project
│   │   │   ├── arm.swiftsourceinfo
│   │   │   ├── arm64-apple-ios.swiftsourceinfo
│   │   │   ├── arm64.swiftsourceinfo
│   │   │   ├── armv7-apple-ios.swiftsourceinfo
│   │   │   └── armv7.swiftsourceinfo
│   │   ├── arm.swiftdoc
│   │   ├── arm.swiftmodule
│   │   ├── arm64-apple-ios.swiftdoc
│   │   ├── arm64-apple-ios.swiftmodule
│   │   ├── arm64.swiftdoc
│   │   ├── arm64.swiftmodule
│   │   ├── armv7-apple-ios.swiftdoc
│   │   ├── armv7-apple-ios.swiftmodule
│   │   ├── armv7.swiftdoc
│   │   └── armv7.swiftmodule
│   └── module.modulemap
└── SnapKit
<span class="copy-code-btn">复制代码</span></code></pre>
<p>再用模拟器编译一个x86版本的SnapKit.framework。它跟上面真机版本的目录结构一样，两者除了可执行文件的区别还有Modules文件内容的区别。</p>
<p><code>modulemap</code>文件是对Framework的描述，只要是Framework就必须配套一个<code>module.modulemap</code>文件。</p>
<p><code>swiftmodule</code>文件用于描述Swift内部的方法声明，它是二进制格式的，会根据不同的架构生成不同的版本。该文件用于方法查找，如果缺少对应架构的swiftmodule文件，会被编译器直接识别出来。</p>
<p><code>swiftdoc</code>文件是一种描述Swift注释的二进制文件，也会根据架构生成。</p>
<p><code>swiftsourceinfo</code>文件是作为Swift源码的补充信息存在的，它的作用是用于定位Swift代码的行和列信息。同样，他也是二进制格式存在的。参考：<a href="https://forums.swift.org/t/proposal-emitting-source-information-file-during-compilation/28794" target="_blank" rel="nofollow noopener noreferrer">forums.swift.org/t/proposal-…</a></p>
<p>由此可知对于，对于多架构的合并除了目标执行文件，还至少需要合入swiftmodule，而另外两种文件可以根据需要决定是否合入。</p>
<h2 data-id="heading-4">编程概念</h2>
<h3 data-id="heading-5">什么是DevOps</h3>
<p>DevOps[/de'vɒps/]是Development（开发） + Operations（运维）的组合，其实它还包含了测试的环节。DevOps是一组过程，方法和系统的统称，突出重视软件开发人员和运维人员的沟通合作，通过自动化流程来使得软件构建、测试、发布更加快捷、频繁和可靠。</p>
<p>DevOps 希望做到的是软件产品交付过程中IT工具链的打通，使得各个团队减少时间损耗，更加高效地协同工作。</p>
<p>DevOps 通常需要很多工具的介入，Jira、GitLab、Jenkins、Docker、fastlane等。它是CI/CD的延伸，CI/CD是实现DevOps的基础核心。DevOps的实践可以用于增强敏捷开发。</p>
<p><img alt class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/30eab362353c40c7901bf6103a41f325~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-6">什么是敏捷开发</h3>
<p>敏捷开发（Agile software development）是一种应对快速变化的需求的一种软件开发能力。相对于“非敏捷”，更强调程序员团队与业务专家之间的紧密协作、面对面的沟通（认为比书面的文档更有效）、频繁交付新的软件版本、紧凑而自我组织型的团队、能够很好地适应需求变化的代码编写和团队组织方法，也更注重软件开发过程中人的作用。</p>
<p>其描述的是整体软件开发的过程，包含以下几个关键点：</p>
<p>• 迭代、渐进和进化：周期控制在一到四周，迭代的目标要达到一个可用的发行版</p>
<p>• 工作软件是进化的主要手段：合适的工程管理软件Jira、Tower等</p>
<p>• 高效率的面对面沟通：明确一个产品负责人；消息发布，包含最新产品信息，通常依托于大屏显示器，路人可以看到</p>
<p>• 非常短的反馈回路和适应周期：每日立会</p>
<p>• 质量焦点：推荐使用TDD方式开发，使用CI提速开发流程</p>
<h3 data-id="heading-7">什么是Scrum</h3>
<p>Scrum是敏捷开发中的一种方法学。它是用于开发、交付和持续支持复杂产品的一个框架，是一个增量的、迭代的开发过程。</p>
<p>在这个框架中，整个开发过程由若干个短的迭代周期组成，一个短的迭代周期称为一个Sprint，每个Sprint的建议长度是一至四周。在Scrum中，使用产品Backlog来管理产品的需求，产品backlog是一个按照商业价值排序的需求列表，列表条目的体现形式通常为用户故事。Scrum团队总是先开发对客户具有较高价值的需求。在Sprint中，Scrum团队从产品Backlog中挑选最高优先级的需求进行开发。挑选的需求在Sprint计划会议上经过讨论、分析和估算得到相应的任务列表，我们称它为Sprint backlog。在每个迭代结束时，Scrum团队将递交潜在可交付的产品增量。 Scrum起源于软件开发项目，但它适用于任何复杂的或是创新性的项目。Scrum 目前已被用于开发软件、硬件、嵌入式软件、交互功能网络、自动驾驶、学校、政府、市场、管理组织运营，以及几乎我们（作为个体和群体）日常生活中所使用的一切。</p>
<p>Scrum中有三个重要角色：</p>
<ol>
<li>Scrum Master是Scrum教练和团队带头人，确保团队合理的运作Scrum，并帮助团队扫除实施中的障碍；</li>
<li>产品负责人，确定产品的方向和愿景，定义产品发布的内容、优先级及交付时间，为产品投资报酬率负责；</li>
<li>开发团队，一个跨职能的小团队，人数5-9人，团队拥有交付可用软件需要的各种技能。</li>
</ol>
<p><img alt class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/e2b6ba8884e04f8caec8917a3e1831e7~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-8">什么是极限编程</h3>
<p>极限编程（英语：Extreme programming，缩写为XP），是一种软件工程方法学，是敏捷软件开发中应用最为广泛和最富有成效的几种方法学之一。如同其他敏捷方法学，极限编程和传统方法学的本质不同在于它更强调可适应性而不是可预测性。</p>
<p>极限编程的支持者认为软件需求的不断变化是很自然的现象，是软件项目开发中不可避免的、也是应该欣然接受的现象；他们相信，和传统的在项目起始阶段定义好所有需求再费尽心思的控制变化的方法相比，有能力在项目周期的任何阶段去适应变化，将是更加现实更加有效的方法。</p>
<p>极限编程包含几个重要的实践：结对编程、编码规范、TDD、重构、持续集成等。</p>
<p>极限编程有5个重要原则：快速反馈、假设简单、增量变化、拥抱变化、高质量工作。</p>
<h3 data-id="heading-9">什么是结对编程</h3>
<p>结对编程（英语：Pair programming）是一种敏捷软件开发的方法，两个程序员在一个计算机上共同工作。一个人输入代码，而另一个人审查他输入的每一行代码。输入代码的人称作驾驶员，审查代码的人称作观察员（或导航员）。两个程序员经常互换角色。</p>
<p>结对编程的理想情况是：在结对编程中，观察员同时考虑工作的战略性方向，提出改进的意见，或将来可能出现的问题以便处理。这样使得驾驶者可以集中全部注意力在完成当前任务的“战术”方面。观察员当作安全网和指南。</p>
<p>但为什么结对编程没有流行开来？这是因为它的优点不好发挥，缺点有着诸多不可控因素。</p>
<p>结对编程中希望达成的：驾驶者可以集中全部注意力在完成当前任务的“战术”方面，观察员当作安全网和指南，这需要很高的配合度才能达成。而合作所产生的交流成本和个性差异也不可忽略。</p>
<p>我想到的结对编程可以发挥的场景有这么两个：</p>
<p>1、对于一些复杂问题的攻坚，两人合作，利用不同思路可能快速解决问题。</p>
<p>2、适合帮助开发者快速熟悉自己所不熟悉的领域，类似老人带新人的模式，它有利于知识的分享和传递。</p>
<p>参考资料：<a href="https://blog.csdn.net/csdnnews/article/details/105259918" target="_blank" rel="nofollow noopener noreferrer">blog.csdn.net/csdnnews/ar…</a></p>
<h3 data-id="heading-10">什么是元编程</h3>
<p>元编程（Metaprogramming）是计算机编程里一个非常重要、有趣的概念，维基百科中的定义是将元编程描述成一种计算机程序可以将代码看待成数据的能力。简单理解就是，其表达的是一种使用代码生成代码的能力。</p>
<p>现代的编程语言大都会为我们提供不同的元编程能力，从总体来看，根据『生成代码』的时机不同，我们将元编程能力分为两种类型，其中一种是编译期间的元编程，例如：宏和模板；另一种是运行期间的元编程，也就是运行时，它赋予了编程语言在运行期间修改行为的能力，当然也有一些特性既可以在编译期实现，也可以在运行期间实现。</p>
<p>元编程可用于解决通用型的问题，减少样板代码，比如常见的字典和模型的互转问题，它存在很多固定样式，我们期望编写一个方法让它实现自动匹配，即编写一个可以自调整的方法，这个行为就是元编程，而用到的方案是反射。</p>
<p>跟元编程相关的还有一个概念是元类（Metaclass），它是代表构建类对象的类，在这些语言中例如OC，Ruby，Java，Python等都有元类的概念。</p>
<p>还有个为了保持继承关系闭环的概念叫根元类（Root metaclass），这个在OC和Ruby中都要对应概念。</p>
<p>扩展文章：<a href="https://onevcat.com/2018/03/swift-meta/" target="_blank" rel="nofollow noopener noreferrer">onevcat.com/2018/03/swi…</a></p>
<h2 data-id="heading-11">优秀博客</h2>
<p>来自字节跳动技术团队的三篇包体优化文章，涵盖了几乎所有可行且有效的包体优化方案：</p>
<p><a href="https://juejin.cn/post/6916317500992913421" title="抖音品质建设 - iOS安装包大小优化实践篇" target="_blank">抖音品质建设 - iOS安装包大小优化实践篇</a> -- 来自掘金：字节跳动技术团队</p>
<p><a href="https://juejin.cn/post/6924107853141655565" title="今日头条iOS安装包大小优化-新阶段、新实践" target="_blank">今日头条iOS安装包大小优化-新阶段、新实践</a> -- 来自掘金：字节跳动技术团队</p>
<p><a href="https://juejin.cn/post/6911121493573402638" title="今日头条优化实践：iOS包大小二进制优化，一行代码减少60MB下载大小" target="_blank">今日头条优化实践：iOS包大小二进制优化，一行代码减少60MB下载大小</a> -- 来自掘金：字节跳动技术团队</p>
<p>启动优化：</p>
<p><a href="https://juejin.cn/post/6921508850684133390" title="抖音品质建设 - iOS启动优化《实战篇》" target="_blank">抖音品质建设 - iOS启动优化《实战篇》</a> -- 来自掘金：字节跳动技术团队</p>
<p><a href="https://mp.weixin.qq.com/s/h3vB_zEJBAHCfGmD5EkMcw" title="iOS 性能优化：优化App启动速度" target="_blank" rel="nofollow noopener noreferrer">iOS 性能优化：优化App启动速度</a> -- 来自公众号：老司机技术周报</p>
<p>iOS签名及证书的几篇文章：</p>
<p><a href="http://chuquan.me/2020/03/22/ios-certificate-principle/" title="iOS证书幕后原理" target="_blank" rel="nofollow noopener noreferrer">iOS证书幕后原理</a> -- 来自博客：楚权的世界</p>
<p><a href="http://blog.cnbang.net/tech/3386/" title="iOS App 签名的原理" target="_blank" rel="nofollow noopener noreferrer">iOS App 签名的原理</a> -- 来自博客：bang's blog</p>
<p>介绍Swift与OC混编机制的文章：</p>
<p><a href="https://mp.weixin.qq.com/s/gI9vL1KlHuMzMoWWf2tnIw" title="从预编译的角度理解Swift与Objective-C及混编机制" target="_blank" rel="nofollow noopener noreferrer">从预编译的角度理解Swift与Objective-C及混编机制</a> -- 来自公众号：美团技术团队</p>
<h2 data-id="heading-12">学习资料</h2>
<h3 data-id="heading-13"><a href="https://github.com/Asabeneh/30-Days-Of-Python" title="30-Days-Of-Python" target="_blank" rel="nofollow noopener noreferrer">30-Days-Of-Python</a></h3>
<p>简介：英文仓库、Star数5k</p>
<p>教程按照天数分为30天，每天都会介绍一些Python概念，伴有示例和练习。正如该仓库的介绍说的那样，真要30天完成这些内容的学习对很多人来说都是一个挑战，我们可以根据自己的节奏去学习，即使100天才学完他们都是可以的。</p>
<p><img alt class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/9804fff3f4d34e518fb581bae307c36a~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-14"><a href="https://github.com/jackfrued/Python-100-Days" title="Python-100-Days" target="_blank" rel="nofollow noopener noreferrer">Python-100-Days</a></h3>
<p>简介：中文仓库、Star数99.9k</p>
<p>这个是国人写的教程，应该是Python类教程里Star数最高的了。更符合国人的学习习惯，伴有教程介绍和示例代码，而且内容更详尽，不单是Python内容，还会扩展一些前端、后端、深度学习等跟Python相关的知识。</p>
<h3 data-id="heading-15">斯坦福iOS开发教程</h3>
<p>推荐来源：<a href="https://github.com/tzqiang" target="_blank" rel="nofollow noopener noreferrer">tzqiang</a></p>
<p>地址：<a href="https://cs193p.sites.stanford.edu/" target="_blank" rel="nofollow noopener noreferrer">cs193p.sites.stanford.edu/</a></p>
<p>这个斯坦福的iOS开发系列教程每年都会更新，最早之前还是OC语言，还是再讲MVC。现在已经更新到Swift和MVVM了，并使用SwiftUI 进行视图搭建。除视频需要到Youtube观看外，其他内容可以在国内网络环境访问。</p>
<p><img alt class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/8f2ccfc2e4c345ff8e86455f563d63f6~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-16">开发利器</h2>
<p>推荐好用的开发工具。</p>
<h3 data-id="heading-17">Diagrams.net</h3>
<p><strong>推荐来源</strong>：<a href="https://juejin.cn/post/zhangferry.com">zhangferry</a></p>
<p><strong>地址</strong>：<a href="https://www.diagrams.net/" target="_blank" rel="nofollow noopener noreferrer">www.diagrams.net/</a></p>
<p><strong>软件状态</strong>：免费，<a href="https://github.com/jgraph/drawio" target="_blank" rel="nofollow noopener noreferrer">开源</a></p>
<p><strong>使用介绍</strong></p>
<p>强大且方便的流程图绘制软件，同时支持Web端和桌面端。和<a href="https://www.processon.com/" target="_blank" rel="nofollow noopener noreferrer">Processon的</a>免费版只能添加9个文件的限制，Diagrams.net的文件数量是无限制的，而且它支持的流程图控件比Processon还要更多。</p>
<p><img alt class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/5b1e9f7cd0f5493fa2c565f3121c0382~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<ul>
<li>支持几乎所有的主流流程图元素</li>
<li>远程存储，文件数量不限，可以存储至Github、Google Drive、Dropbox等地方</li>
<li>支持本地桌面端，可以离线绘制，本地存储</li>
<li>支持链接共享，通过链接查看我们当前绘制的流程图</li>
<li>可以导出为图片、HTML、PDF等多种格式</li>
</ul>
<h3 data-id="heading-18">Github1s.com</h3>
<p><strong>推荐来源</strong>：<a href="https://juejin.cn/post/zhangferry.com">zhangferry</a></p>
<p><strong>地址</strong>：<a href="https://github.com/conwnet/github1s" target="_blank" rel="nofollow noopener noreferrer">github.com/conwnet/git…</a></p>
<p>这个工具可以使我们访问github的仓库就像直接在VSCode中打开一样，使用方法非常简单，就是将网站域名换成github1s，以Swift仓库为例，访问：<a href="https://github1s.com/apple/swift%EF%BC%8C%E5%BE%97%E5%88%B0%E7%9A%84%E7%BB%93%E6%9E%9C%E5%A6%82%E4%B8%8B%E3%80%82" target="_blank" rel="nofollow noopener noreferrer">github1s.com/apple/swift…</a></p>
<p><img alt class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/6139af2495b341b58672f5dbdd3697a1~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p>我们可以像在VSCode里一样，直接在浏览器里查看仓库代码。</p>
<h2 data-id="heading-19">联系我们</h2>
<p><a href="https://zhangferry.com/2020/12/20/iOSWeeklyLearning_1/" target="_blank" rel="nofollow noopener noreferrer">摸鱼周报第一期</a></p>
<p><a href="https://zhangferry.com/2021/01/03/iOSWeeklyLearning_2/" target="_blank" rel="nofollow noopener noreferrer">摸鱼周报第二期</a></p>
<p><a href="https://zhangferry.com/2021/01/10/iOSWeeklyLearning_3/" target="_blank" rel="nofollow noopener noreferrer">摸鱼周报第三期</a></p>
<p><a href="https://zhangferry.com/2021/01/24/iOSWeeklyLearning_4/" target="_blank" rel="nofollow noopener noreferrer">摸鱼周报第四期</a></p></div> <div class="image-viewer-box" data-v-78c9b824><!----></div>  
</div>
            