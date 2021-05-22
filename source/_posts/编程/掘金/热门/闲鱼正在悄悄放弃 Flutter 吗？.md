
---
title: '闲鱼正在悄悄放弃 Flutter 吗？'
categories: 
 - 编程
 - 掘金
 - 热门
headimg: 'https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/18e8a33915e24fcb8dc97b4ae3d6ef35~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Sun, 25 Apr 2021 19:34:47 GMT
thumbnail: 'https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/18e8a33915e24fcb8dc97b4ae3d6ef35~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>采访嘉宾 | 于佳（宗心）</p>
<p>编辑 | Tina</p>
<p>闲鱼在 2017 年引入 Flutter，当时的 Flutter 还远未成熟，行业内也没有把 Flutter 放入已有工程体系进行开发的先例。</p>
<p>之后这支不到 15 人的闲鱼团队从工程架构、混合栈调用、打包构建、协同模式上都做了一些创新，保证了 Flutter 能融入到闲鱼已有的客户端工程体系内。在 2017 年到 2019 年期间，闲鱼也不断的修正 Bug 提高 Flutter 的稳定性并同步给 Google，并在实践中沉淀出一套自己的混合技术方案，开源了 Flutter Boost 引擎。</p>
<p>2019 年，闲鱼开始大规模落地，推进 Flutter 在闲鱼的应用。2020 年，闲鱼线上的主链路几乎已经完全拥抱 Flutter。这两年，Flutter 也逐渐在其他企业里落地，但同时也不断有质疑的声音发出。甚至有传言表示“闲鱼的新业务已经放弃 Flutter”、“相信闲鱼遇到了很大的难题”......</p>
<p>那么，作为 Flutter 先驱和探路者，闲鱼在过去几年的摸索过程中是否有走弯路？闲鱼现在到底面临着什么样的挑战？是否会放弃 Flutter？新业务选择了什么技术？对应的技术选型原则是什么？针对这些疑问，闲鱼技术团队客户端负责人于佳（宗心）逐一给了我们解答。</p>
<h2 data-id="heading-0">国内第一个引进 Flutter 的团队</h2>
<p><strong>InfoQ：闲鱼当时引进 Flutter 时主要是为了解决什么问题？</strong></p>
<p><strong>于佳（宗心）</strong>：闲鱼在 17 年调研的时候，客户端团队只有不到 15 人，而闲鱼的业务场景可以称得上是一个 <strong>“小淘宝”</strong>，相对比较复杂。这种场景下我们首先需要解决的是多端人力共享的问题。多端人力带来的好处不只是可以一人开发双端，也代表着更好的研发资源调配灵活性（这意味着团队的 iOS：Android 的比例不再需要 1:1，而市面上 Android 的工程师基数远大于 iOS）。</p>
<p>另外我们希望这个技术是贴合移动端研发技术栈的，而非前端技术栈，本身对于 RN 和 Weex 来说，工具链和研发习惯还是有比较大的差异的。最后我们希望这个技术的体验可以做到接近原生，AOT 下的 Flutter 基本满足我们当时的要求，在实际测试过程中，同样未深度优化的详情页面，Flutter 在低端机的表现比 Native 更好。因此当时基于这三个条件选择了 Flutter。</p>
<p>2018 年的尝试投入过程中，整个基建和探索带来了一定的成本。2019 年，团队开始正式大量使用 Flutter 进行研发，目前整个团队 70% 的 commit 来自 Dart，可以说基本完成了我们当初的期望。在实际的研发过程中，基本可以完成一个需求一个客户端投入的目标。</p>
<p><strong>InfoQ：很多人质疑 Dart 语言，认为这个语言独特小众，还存在比如说多层嵌套的问题，您们怎么看待新语言的应用？</strong></p>
<p><strong>于佳（宗心）</strong>：语言是我们选择技术方案的其中一个因素，但是相对比较弱的因素。</p>
<p>我们会从几个角度去看：</p>
<ul>
<li>
<p>语言的背景，从我们的角度来看 Dart 是大厂研发的，也有比较久的历史。</p>
</li>
<li>
<p>语言的学习成本，从语法糖和学习曲线上来看，Dart 成本都比较低，首先 Android 同学的上手率很快。另外熟悉 swift 的 iOS 同学，上手也很快。现代语言的特性有很多是相通的。这部分是它的优势。</p>
</li>
<li>
<p>语言带来的其他优势，如编译产物支持 AOT 和 JIT，比较灵活。AOT 有明显的性能优势。</p>
</li>
<li>
<p>语言的未来的趋势。Dart 在 2020 年第四季度 Github Pull Request 的排名已经到了全网第 13 位，超过了 Kotlin（15 位），Swift（16 位），Objective-C（18 位）。作为移动技术领域的新语言成长性还是非常不错的。</p>
</li>
</ul>
<p>对于像多层嵌套的问题，可以通过进一步抽象一些控件类或方法解决，并不是特别大的问题。</p>
<p><strong>InfoQ：闲鱼引入 Flutter 之后做了哪些关键创新？在使用 Flutter 上有哪些收益？</strong></p>
<p><strong>于佳（宗心）</strong>：闲鱼在这部分创新非常多，并在内部申请了非常多专利。</p>
<ul>
<li>
<p>我们的开源项目 Flutter Boost 彻底改变了 Flutter 官方的一些 RoadMap。目前 Add2ExistApp 是行业最主流的研发方式。混合开发一方面帮助了业务更平滑的迁移到了新的技术栈，另一方面可以更好的利用已有的 Native 能力，大幅减少了重复开发的工作。</p>
</li>
<li>
<p>针对音视频的外接纹理方案，也是目前行业大厂常见的解决方案，在外接纹理方案下，Native 和 Flutter 侧的缓存管理得到了统一，在性能上也有一定的提升。</p>
</li>
<li>
<p>Flutter APM，基于 Flutter 技术栈的性能稳定性数据采集和加工方案，目前在集团内部也是跟多个 BU 一起共建，为大的 AliFlutter 组织提供服务。</p>
</li>
<li>
<p>Flutter 相关的动态模版方案，Flutter DX，兼容集团的已有的 Native 模版，保证了业务的平滑迁移，并为 Flutter 提供了部分业务动态性。</p>
</li>
<li>
<p>其他还有很多，包括内部的高性能长列表容器 PowerScrollView，动画框架 Fish-Lottie，游戏引擎 Candy，我们现在还有一些新的方向在沉淀，在基于 Flutter 的研发流程和研发工具上也有投入，未来大家如果感兴趣可以去 InfoQ 组织的行业大会与我们交流。</p>
</li>
</ul>
<h2 data-id="heading-1">闲鱼有想过放弃 Flutter 吗？</h2>
<p><strong>InfoQ：最近一两年，您们在 Flutter 开发上，遇到的最大挑战是什么？跟最初使用 Flutter 时的挑战一样吗？</strong></p>
<p><strong>于佳（宗心）</strong>：早先几年闲鱼作为整个行业的先驱，主要的挑战是整个技术生态太差，都需要自己做。另外就是前期引擎的稳定性有比较大的问题。</p>
<p>最近几年随着整个技术的深度使用，以及闲鱼这两年业务快速发展背后，越来越多的体验问题被大家提及，因此我们从去年开始进行了整个产品的大改版，同时客户端的目标就是全面优化，打造更好的用户端产品体验。</p>
<p>因此在生态逐渐完善后，<strong>我们的挑战是，怎么通过 Flutter 来实现更加精细化的用户体验</strong>。去年，这部分确实花了我们比较多的精力。基于这个命题，我们在内存和卡顿上内部也开发了较多的基于 Flutter 的检测工具，在内存优化和卡顿优化上也有一些比较具体的方法，但不得不说，所有的细节优化都是比较耗人力的，不管是 Native 还是 Flutter 都要投入相当的精力，所以我们目前也面向全行业进行客户端的招聘，希望有志在 Flutter 领域进行探索的同学联系我。</p>
<p><strong>InfoQ：在混合研发体系下，闲鱼还进行了引擎定制，那么官方提供的方案主要问题是什么？对于一般小企业来说，混合开发复杂度会不会太高？</strong></p>
<p><strong>于佳（宗心）</strong>：闲鱼在前期有不少修改引擎的动作，我针对当时有一些 <strong>自己的反思</strong>，一方面是确实因为 Flutter 不太完善，另一方面在 18 年左右，我们自己引擎的理解也不够深刻，很多时候可以通过更上层的方案解决，这也间接导致了我们的很多引擎定制修改难以合入主干。</p>
<p>所以这部分我想说的是，目前官方的方案可以解决 90% 的问题，如果一定要说定制，目前在性能侧还是有一些问题的。比如闲鱼目前首页还是 native 没有使用 Flutter，就是因为替换以后启动加载体验不佳，另外在长列表侧大家一直诟病的卡顿问题，我们有尝试通过上层框架解决了一部分，接下来可能还需要底层引擎帮忙优化。另外一些包括双端字体不一致的问题，还有输入框体验不一致的问题，都需要官方进行长期的优化。</p>
<p><strong>目前我们主要还是希望跟随主干分支，尽量不修改 Flutter 的代码</strong>，闲鱼团队会储备一些引擎侧的专家，同时也会依靠集团 AliFlutter 的生态做事情。在整个 AliFlutter 的组织里不同的 BU 擅长的也不同，如 UC 同学更擅长引擎定制，闲鱼团队有大量的上层应用框架，淘宝团队提供基于构建相关的基础设施。这样在大型公司中通过内部开源社区的方式就可以解决大部分的问题，放心开发了。</p>
<p>对于中小企业来说，要明确下大家面临的场景，如果前期快速迭代跑起来，对细节问题可以有一部分妥协，选择 Flutter 是一个比较明确的路径。今天大家所处的环境比闲鱼当年所处的环境要完善的多。推荐使用 Flutter Boost 进行混合开发，在部分场景下遇到问题无法快速响应时，也可以通过混合工程使用 native 进行兜底。复杂度方面，单纯引入混合栈能力，整体复杂度一般。</p>
<p><strong>InfoQ：有传言，闲鱼有新业务没采用 Flutter，这给很多人造成了闲鱼放弃 Flutter 的观念，那么您们在新业务的技术选型上，考虑了哪些因素？</strong></p>
<p><strong>于佳（宗心）</strong>：作为技术决策者，是应该避免自己被某一个技术绑架而在落地过程中产生谬误的。Flutter 和其他技术一样，最终是为了帮助团队实现业务价值，同时它也只是移动端的一种技术，捧杀和谩骂都是不合适的。这也是我特别不想在公众面前回应这个事情的原因，因为 <strong>技术本身要看适用场景。</strong></p>
<p>从目前闲鱼的人员规模和业务规模来看。对于架构设计，我的理念是尽量追求一致性和架构的简洁。</p>
<p>整个客户端组织未来从语言的方向来看是 Dart First，尽量减少双端的研发投入。而对其他容器的选择，主要以 H5 为主，在未来的路径上尽量减少其他容器的接入，让前端开发也回归到标准路线来。</p>
<p>这里有两个好处：</p>
<ol>
<li>
<p>组织成本最低，组织成本包括了同学们的学习成本、协同成本等等，多技术栈和容器多会带来额外的成本，这是我不愿意看到的。</p>
</li>
<li>
<p>架构的一致性对研发效能和质量都有帮助。举个例子，随着业务复杂性加大，多容器带来的内存飙升和包大小的问题是非常致命的，而且几乎是无解的，这就需要架构师作出决策，干掉什么留下什么。回到研发效能上，配套的工具，流程一定是围绕一类容器和语言来扩展的，如果方案特别多，每个方向都需要做额外的配套设施，成本收益很低，研发的幸福感也很低。</p>
</li>
</ol>
<p>从这个设计的角度出发，<strong>我们会有几个明确的选择</strong>：</p>
<ul>
<li>
<p>在默认场景下使用 Flutter 作为首选的方案；</p>
</li>
<li>
<p>在投放活动、前台导购、非常不确定的新业务、以及管理后台等使用 H5 作为首选实现方案；</p>
</li>
<li>
<p>在极少场景下，比如已有完整的 SDK 附带 UI 的支持如直播，以及未来中台的拍摄功能 SDK 也是自带 UI 的部分，如要切换，Native 成本最低，选择 Native。另外目前 Flutter 在首页加载还有一定的性能问题，因此还在使用 Native。从长远发展来看，未来到一定程度可能随改版直接改为 Flutter。</p>
</li>
</ul>
<h2 data-id="heading-2">关于未来发展</h2>
<p><strong>InfoQ：使用 Flutter 多年后，现在回过头去看，您认为哪些公司哪些场景适合 Flutter？</strong></p>
<p><strong>于佳（宗心）</strong>：目前看起来有几个典型场景比较适合：</p>
<ul>
<li>
<p>中台战略下的小前台产品，从大公司的组织里看阿里、头条、美团都有相对完善的 Flutter 组织或内部技术社区可以提供一些基础服务，保证了基于 Flutter 基础设施在前期投入过程中的成本均摊，在未来落地过程中，业务团队可以更加专注于业务研发，而更少的担心过程中填坑的成本。</p>
</li>
<li>
<p>中小型企业的初创 App，在人力成本资源都不够的情况下，希望先跑通流程上线验证的团队，可以尝试使用 Flutter 进行研发，在我自己实际的面试和行业交流过程中，这一类情况也比较典型。这种方式可以避免前期成本过度投入，在人员调配上也更加灵活。</p>
</li>
<li>
<p>另外这个观点还没有验证，但是逻辑上应该可行。未来面向企业内部流程工具，政府部门的部分工具属性较强的 App，可以尝试使用 Flutter。因为目前我了解的情况来看，在企业这边的应用来看，整体 ToB（美团商家端）和 ToD（比如饿了么骑手端）的场景的 App 特别多。横向比较来看，场景比较类似，也就是说更多中长尾应用有可能是 Flutter 技术的主要场景。</p>
</li>
</ul>
<p><strong>InfoQ：您认为未来 Flutter 急需改善的地方是什么？</strong></p>
<p><strong>于佳（宗心）</strong>：从 Flutter 2.0 发布后我跟一些一线开发者交流的感受来看，Flutter 还是需要推进跨端性能和细节体验的优化。去年一年在大的战略方向上（跨终端），Flutter 做的不错，在 PC 和 Web 侧都有建树，跟车企以及操作系统厂商合作都有一定进展。但回归到产品体验和开发者体验上，还有不少路要走，很多时候对于一个严苛的业务方来说，小到字体和控件的体验都会成为最后不选择这门技术的原因。这部分希望整个开源社区在新的一年能有一些进步。我们 AliFlutter 组织内部，以 UC 内核团队为首的同学们，在这方面就有非常多的沉淀以及 PR，在内部引擎制定上有很多体验的提升。未来在 AliFlutter 组织内，我们也会除了完善整个公司的基建外，进一步关注细节体验，沉淀一些最佳实践给到其他的开发同学。大家会在2个月内看到我们最新出版的书籍，欢迎交流。</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/18e8a33915e24fcb8dc97b4ae3d6ef35~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p><strong>InfoQ：Flutter2.0 来了，那么 Flutter 会成为主流选择吗？</strong></p>
<p><strong>于佳（宗心）</strong>：可以讲一下我对 Flutter 未来的判断。一方面在未来操作系统有可能走向分裂，多终端的场景下，Flutter 会有比较不错的发展，跨平台本身的对企业来说在成本侧是有很大的诉求的，尤其是互联网公司。但是从历史的经验来看，Flutter 只是渲染引擎，即使今天的游戏开发，在游戏引擎和配套工具完善的情况下，有部分的功能模块（比如社区 / 直播的功能）依然还是混合的框架，所以混合开发最后一定是一直存在的。能不能成为未来整个移动研发的主流这件事情上看，我无法给出答案，但可以肯定的是，在生态更加完善后，会在一定的历史阶段成为客户端研发的另一种常见的技术选择。</p>
<p>嘉宾介绍：</p>
<p><strong>于佳</strong>，花名 <strong>宗心</strong>，闲鱼技术团队客户端负责人。2012 年应届毕业加入阿里巴巴，经历集团无线化转型的重要时期，参与过集团多款重量级 App 以及移动中间件的设计与开发，多年客户端老兵。2014 年参与了手机淘宝的 iOS 客户端的架构升级，该架构首次完成了对百人团队并行开发的支持，同年主导了手机天猫客户端基础架构以及交易链路向手淘架构的归一，为手机淘宝作为未来集团无线中台奠定了坚实的基础。2015 年加入闲鱼客户端团队负责端架构和团队建设，工作期间完成了基于 Flutter 混合架构的闲鱼客户端的整体架构设计，在工程体系上完善了针对 Flutter 的持续集成以及高可用体系的支撑，同时推进了闲鱼主链路业务的 Flutter 化。未来将持续关注终端技术的演变及发展趋势。</p></div>  
</div>
            