
---
title: '飞猪Flutter技术演进及业务改造的实践与思考总结'
categories: 
    - 编程
    - 掘金 - 专栏
author: 掘金 - 专栏
comments: false
date: Mon, 08 Mar 2021 04:10:54 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/432b7f7911774942bda548e32d82fdf9~tplv-k3u1fbpfcp-zoom-1.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><blockquote>
<p>本文作者飞猪@旅鹤，负责飞猪安卓端 架构和大交通业务团队，在客户端工程化体系、性能优化、稳定性治理、音视频、移动安全等方向有丰富经验；</p>
</blockquote>
<blockquote>
<p>当前飞猪技术部 2022 届校园招聘开始啦，欢迎前往 <a href="https://juejin.cn/post/6937256619763826718" target="_blank">掘金详细了解</a>。</p>
</blockquote>
<p>本文结合飞猪近半年来在 Flutter 技术实践中的突破和探索，重点介绍跨端标准容器建设、组件库的沉淀、性能优化的经验，以及面对存量业务做 Flutter 改造的新思路。</p>
<h2 data-id="heading-0">一、飞猪客户端架构演进</h2>
<p><img alt class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/432b7f7911774942bda548e32d82fdf9~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-1">发展历程</h3>
<p><strong>客户端架构 1.0</strong><br>
 2013 年，随着阿里巴巴 All in Mobile，阿里旅行也有了独立的 App。最初业务比较简单，PC 页面简单改造成 H5 运行在 App 端，以信息展示为主，Native 业务承接机票交易，整个 App 的构建发布不成体系。发渠道包都在单台 Jenkis 服务器上现拉源码编译，测试验证后直接发应用市场，没有体系化的研发构建平台，也缺乏完善的灰度机制。
当时 Android 手机山寨机横行，主流厂商各种定制 ROM，兼容性、适配问题搞的焦头烂额，所以我们主要精力在解决稳定性问题，同时夯实基础功能，支撑业务稳定上线。这个阶段 Android、iOS 得到独立发展，只在页面跳转协议和事件总线协议上保持一致。</p>
<p><strong>客户端架构2.0</strong><br>
随着支付宝和手淘快速成长为航母级应用，无线基础设施趋于完善，飞猪也搭上了顺风车，支撑了业务快速迭代。我们在端研发框架上对接过无线研发协作平台，有力保障了多人并行开发，业务迭代最快做到按周交付。同时基本建立了完善的灰度发布体系，Crash 率从千分之 5 降低到万分之 2，其它基础功能（网路库/图片库/Push 通道）也逐步从自建方案回归到依赖中台基础能力，研发效率大幅提升。
但受限于应用渠道更新效率，在 Android 端，新版本升级覆盖慢的问题长期存在，分发效率低的问题不得不提上日程。因此我们开始投入做相关技术的改造：</p>
<ul>
<li>看 Native 自身，各种动态化技术层出不穷。飞猪也积极参与了动态更新技术共建，回归头看，在非航母级应用上，动态发布能力主要还是修 bug，真正推业务的情况并不多见。为了进一步提升业务对 Native 动态性需求，飞猪也与手淘共建了 DX 动态模板容器，通过统一动态模板 DSL，建立了完善的搭建平台和模板管理仓库，现已广泛应用于业务中，但只限于简单业务逻辑。</li>
<li>看前端，H5 因为开发效率高，且具备完备的动态化能力，开始大量承接业务。我们很早就成立了跨栈虚拟小组，通过离线包、预加载、预渲染、新SSR技术来优化 H5 性能。飞猪前端同学也积极参与了Weex业务落地，当时国际机票核心主链路也由Weex承接，实现接近原生的体验。</li>
</ul>
<h3 data-id="heading-2"><strong>挑战与新机会</strong><br></h3>
<p>随着业务需求迭代，App 变的越来越臃肿，技术改造带来研发效率/性能体验提升的同时，也增加了维护的复杂度。旅行业务域逻辑非常复杂，对有些大的需求，在需求评审上经常需要反复对焦，但在实际交付上还是存在两端开发理解偏差引发的线上问题，我们印象中就发生过几起机票交易链路因为漏测引发线上故障。
技术侧复杂度增加也容易出现纰漏，一次 H5 离线包在 Android 端由于没加好保护导致线上大面积客诉，经过超过 24 小时排查才最终定位到问题。很多基础线的改造也很难评估具体影响面，给稳定性带来新的挑战。从目前的技术方案上看，因为两端的具体实现依赖原生能力，系统平台层的差异性带来的业务表现差异问题，很大程度是需要更底层的技术方案来解决的。</p>
<p><strong>自渲染与Flutter</strong><br>
<img alt class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/474501387f964fa4b792dc844f0651cb~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer">
自渲染技术并不是新概念，从很早以前的 QT 到现在的 Flutter，它的优势在于具备非常好的跨端能力，能解决长尾问题。对比原生渲染方案，具体到 WebView，在 Android 上版本碎片化问题非常多，给前端适配带来很大的难度，我们利用12MB包大小内置U4来解决在WebView在Android端的适配问题；看 Native 原生业务，之前提到的由于沟通上理解上偏差出现交付上差异，最终由测试兜底也是不可持续的。
<img alt class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/aa3805ecdca9419b86a0a65251704f27~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer">
Flutter 在全球超过 200 万开发者，月活开发者 50 万。据 GitHub 统计，Flutter 是全球第二快增长的开源项目。Google Play 发布了超过 11 万 Flutter 应用，国内大厂基本都使用 Flutter，集团内非常多 BU 也积极参与生态建设。对比 QT，同是自渲染技术，它在开发体验上和生态建设上都有很大优势，也因此收获了很多开发者。对比其他的技术方案，Flutter 除了因为政策原因舍弃了动态性，其他方面表现都非常优秀。</p>
<h3 data-id="heading-3"><strong>客户端架构Flutter演进方向</strong></h3>
<p><img alt class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/f38b1d9176784fbf86d55af2d75ac9d4~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer">
2019 年，飞猪开始在商家版 EBK 改造项目上试水 Flutter，在研发效率和用户体验上都有不错的收益。随着 Flutter 混合技术栈的完善，我们决定 2020 年 6 月份在飞猪 C 端做 Flutter 专项改造，寄希望于推动飞猪技术架构升级，完成客户端技术体系向大前端技术体系演进，建立统一移动端研发模式，摸高 Flutter 的效能极限。具体到几个核心项目，包括跨端标准容器、研发工程体系、组件化建设、自动化测试领域寻求突破，并沉淀最佳实践。
通过引入 Flutter 技术，上层业务开发可以无缝对接 Android、iOS，中间的 Flutter 容器非常薄，平台差异性对接工作主要通过 Flutter SDK 实现，解决 Native 体验的一致性问题，提升可维护性。
正如官方描述所说，Flutter 是 UI Tool Kit，最初定位是服务全新 App 开发，在实际中很多功能满足不了存量业务开发需求。集团基础建设主要围绕完善 Flutter 混合技术栈开发、高可用监控预警、研发支撑平台，以及最核心的性能优化建设，飞猪主要聚焦在业务层面的落地，用好Flutter新技术能力。</p>
<h2 data-id="heading-4">二、飞猪 Flutter 技术沉淀</h2>
<p>经过半年的沉淀，我们在相关关键领域有了比较大的突破，希望和大家深入交流，分享不一样的 Flutter 实践经验。</p>
<h3 data-id="heading-5">1. Web on Flutter</h3>
<h4 data-id="heading-6">背景介绍</h4>
<p><img alt class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/6497484ea499498fbc2f4ea8bd3f07da~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer">
Android 端内置 UC WebView，基本解决了 WebView 碎片化问题，适配压力骤减。但在 2020 年双 11 会场页面开发中，还是存在一些 UI 展示低级缺陷问题，主要表现在字体显示上（上面暴露的问题，近期UC WebView 4.0已经解决），这些问题虽然不严重，但比较影响用户体验，拉低我们对品质的追求。另一方面，Weex 1.0 依赖原生组件，两端渲染一致性问题非常难解决，实现原理类似的 RN 也遇到类似的挑战。
随着 Flutter 技术热度兴起，前端同学在探索 Web on Flutter 的可能，对比之前 Weex 是 Web on Native。底层渲染技术用 Flutter 替换后，会带来性能上新的机会，一致性的表现将能更完美地解决。
<img alt class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/62273b88e12f4886a5326a4cb8b6a6eb~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<h4 data-id="heading-7">技术选型与落地</h4>
<p><img alt class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/9a3272057cbc459085e2560e49bdd841~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<ul>
<li>方案①：JS 封装与 Widget API 接近的接口，实现 Flutter 动态能力，该方案脱离了前端生态；</li>
<li>方案②：Web 与 Widget 对接，ROI 高，完成映射后性能基本接近 Flutter 原生，性能方面也有很高的想象空间；</li>
<li>方案③：Web 与 RenderObject 对接，需要自己写布局相关逻辑，性能上没想象的高，扩展视频、地图组件有一定改造成本，Flutter 版本升级有一定成本；</li>
<li>方案④：用 C++重写 Framework，抛弃 Dart Rumtime，开发成本非常高。</li>
</ul>
<p><img alt class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/090d09d6c5894e3c95cc1a475bed3cd2~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer">
<img alt class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/ce2c3396524749488b88d60dc4fb338e~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer">
Flugy 由飞猪自研，支持前端跨端标准子集，目前在技术层面也和其他团队共建中。
从架构图看，Flugy 是一个 Widget Plugin，可以和 Flutter 生态打通，主要代码用 Dart 开发，对接的是 Flutter Widget（不需要定制引擎），从前端视角看就是个精简的 WebView， H5 不用改造就能运行起来，近期了解到高德开发了Flutter版地图，作为扩展能力接入Flugy也是非常方便的。
<img alt class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/d24a2d632d1842ef9918b8d87067e146~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer">
渲染指令说明：对应的是 DOM API 的一些操作指令，包括 createElement，AppendChildren，removeChildren，replaceChildren，insertBefore...</p>
<h4 data-id="heading-8">Flugy 标准容器关键突破口</h4>
<p><img alt="image.png" class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/862d462d9b9644e7951e735a1676184f~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer">
基于之前的架构设计，容器要做的核心事情是要打通 Web 和 Flutter，虽然 Flutter 核心开发来自 Chrome 维护者，但从设计理念上更接近原生。前端开发只需要通过属性赋值设置想要的结果，不用具体到要用什么组件来实现，WebView 把这部分逻辑都消化掉，而原生开发需要关注更多的细节，组件的封装和组织关系，这也是 Native 页面性能更高，但开发效率不如前端的原因。</p>
<p>回到标准容器项目上看，需要 Flugy 容器把 WebView 之前处理的页面布局、样式的逻辑实现好。与 WebView 不同之处在于我们对接的是 W3C 的子集，没有历史包袱。这里列举了几个属性映射有代表性难题。比如 Overflow：display 和 Position。</p>
<ul>
<li>Position 属性的实现：
<ul>
<li>通常原生开发是从整个页面大的结构入手，然后具体到各子模块的拆分。在 Web on Flutter 上，JS 是在运行过程中创建 DOM，是以流的方式发送渲染指令到容器侧，是个实时解析的过程，我们在解析过程中构建 Widget 对象。但前端的定位属性非常灵活会有脱离常规流情况，这就需要反复修改之前构建的 Widget 对象，也是技术突破口。</li>
<li>对元素状态做了一层抽象把问题简化，首先在解析添加元素 A 时，遇到 position 为sticky/fixed/absolute 元素时，在创建元素 A 的时候会同时创建一个它的副本 A'（副本会被标记为逃逸元素，即 escape 为 true），随后 A 元素原身将会留在其父容器中占位（不做渲染展示），继续走正常的布局流，以确保其它同级元素位置的正确性。而它的副本 A'将会通过内部的通信机制向上寻找能够接纳它的更高层级的父级容器，然后在目标父级容器中按照 web 的规则做渲染展示。</li>
<li>得益于 Flutter 有状态 Widget 的设计和 Flugy 内部有效的通信机制，每一步操作都被控制到了一个最小范围内，仅进行局部更新，而不会触发整颗树的更新，使得性能得到保证。</li>
</ul>
</li>
<li>其他很多属性在 Flutter 都有具体实现，实现的复杂度基本可控。对齐标准是个比较细致的工作，也容易出现理解不到位导致实现效果不符合标准要求，前端同学正在牵头做标准容器单测事项，通过 XRay 实现各标准容器与 H5 渲染表现对齐。</li>
</ul>
<p>结果展示</p>




















<table><thead><tr><th> </th><th>Flugy纯渲染性能</th><th>Flugy完整业务展示</th></tr></thead><tbody><tr><td>描述</td><td>直接加载（把 JS Bundle执行过程的DOM/CSS指令缓存到本地）缓存的指令，图片加载走线上请求，页面展示直出</td><td>加载缓存到本地的JS Bundle，看不到白屏，直接显示蓝色背景图片，网络加载后更新数据，Tab切换和滑动都非常流畅</td></tr><tr><td>结果展示</td><td><a href="https://qpluspicture.oss-cn-beijing.aliyuncs.com/2cGyw8.mp4" target="_blank" rel="nofollow noopener noreferrer">视频点击查看>>></a></td><td><a href="https://qpluspicture.oss-cn-beijing.aliyuncs.com/FcN0Kk.mp4" target="_blank" rel="nofollow noopener noreferrer">视频点击查看>>></a></td></tr></tbody></table>
<h3 data-id="heading-9">2. 单工程构建优化</h3>
<p><img alt class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/5dd396d5440047f4899e9d2410d7483f~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-10">3. 组件库建设</h3>
<h4 data-id="heading-11">多屏适配组件</h4>
<p><img alt class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/aa001f8b222c4ee08d71b106e338e3e6~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer">
我们自己计算 <em><strong>1dp</strong></em> 到底应该占设备屏幕上的多少像素，而不是使用系统预设好的值。将计算好的这个比例设置到项目的环境中，这样就可以以很低的成本达到按照实际分辨率适配出同样的视觉效果，在开发时也会免去很多换算单位的麻烦。最近我们还支持 Flutter 字体大小不受系统设置影响的方案。UI 一致性完美支持后，UI 自动化测试也能从中受益，只需要维护一套测试代码，就可以在多设备下运行，降低适配成本。</p>
<h4 data-id="heading-12"> 开源UI通用组件</h4>
<p><img alt class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/6a08b742e7d745539962395d95ded718~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer">
我们开源了 11 个 UI 组件（<a href="https://github.com/Fliggy-Mobile" target="_blank" rel="nofollow noopener noreferrer">链接地址</a>），都是比较贴合业务场景的组件，上面列举了几个在社区受欢迎的组件。最近团队主要精力在开发 Flugy，后面会加强组件库维护更新工作。
<img alt class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/4c7f02334ef64fcbae2d778c0782e176~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-13">4. XRay 自动化测试框架</h3>
<p><img alt class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/bb94851edf744598af0ef3c4de2a1fb4~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer">
我们做自动化测试框架的初衷，是要解决端渲染技术多样性带来的可测性难题。因为原有的测试框架是基于原生方案的，满足不了未来测试要求。所以我们想设计面向未来的自动化测试方案。
我们从手动测试操作过程找到灵感，基于图像处理算法定位元素，通过驱动能力操控元素，然后再通过图像处理算法验证结果。整个链路是零侵入的，所以具备非常强的适应性。目前能非常好地支持 Native、WebView、Flutter、小程序、动态模板等技术，并且也可以支持鸿蒙，以及 FusionOS。
为了提升测试代码开发效率，我们基于 IntelliJ 开发了插件，只要熟悉 Python 就能熟练掌握，2020 年为了方便外包写 case，还提供了录制回放功能。
<img alt class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/f50232054c034c588a5dbcfab506d489~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer">
这是整个测试 case 编辑、case 执行情况的流程图，最核心的部分是元素定位，用到了我们自研的图像结构相识度识别算法，以及阿里达摩院的读光 OCR 能力，在元素驱动技术上 Android 使用 adb，iOS 使用自研的方案 Dwarf。
<img alt class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/872b7dd0510249edbeafefd91f04dcc2~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer">
列举酒店列表和首页测试执行情况，通过我们自研的图像算法可识别出列表，测试代码编辑只需要 recognize_list，然后操作具体的 item 就可以。实际在 XRay 执行过程看是基于酒店列表生成了个类似 Dom Tree 的结构，在运行过程中操作的不是简单的坐标映射，而是对应到具体的元素模块中，提升了可维护性和执行成功率。
<img alt class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/6bbaf459b7d445c38360546018251f45~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer">
除了 XRay 框架的建设，在实际业务使用场景上还涉及到设备调度，我们基于手机墙调度系统做简单改造支持自动化测试设备调度，支持按系统、品牌、机型维度调配。广泛应用于持续交付的验证，为无线质量保驾护航，目前也在和无线测试团队做智能 monkey（已经覆盖80+页面的自动巡检）。
<img alt class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/4c01e81879c443d2a4dafaec5aa2a452~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer">
<img alt class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/31453ca8e63649cd90925e6386160ead~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer">
<img alt class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/7feb2d9e36384eb9aaacbc96d40cafb5~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer">
Can I Use：为了能更好地支持容器同学和前端同学的研发，便于一目了然地了解各标准在容器层落地支持的情况，前端提供了 CanIUse 检索平台，查看标准在各容器侧的支持情况，通过在真机上自动运行单测脚本做对比测试，确定容器的支持情况。</p>
<h2 data-id="heading-14">三、Flutter性能优化</h2>
<h3 data-id="heading-15"><strong>1. 圆角对性能影响</strong></h3>
<p><img alt class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/b8110201cb694ed4af362afd36d2ff6e~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer">
 </p>
<h3 data-id="heading-16"><strong>2. 合理减少重绘</strong></h3>
<p><img alt class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/0cbd8fbbbe084b7eaecd038a0a10d699~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-17"><strong>3. 开启 SurfaceView</strong></h3>
<p><img alt class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/3e5eabb99ce245a3bfdad37cba1aeb18~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer">
<img alt class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/43213999ca65428784d9bce94a877854~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer">
<img alt class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/ece425ca2fd24589afa7e81c43526518~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer">
 
<img alt="image.png" class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/cfdc0813c40d43faa5ad33cda0a5e066~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer">
注：SurfaceView开启对低端手机性能提升明显，高端手机上优势不大。</p>
<h2 data-id="heading-18">四、业务落地</h2>
<p><img alt="image.png" class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/bfac20f81fa94b95b6cbd4c1a47dadac~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<ul>
<li>2020 年伊始，飞猪 Android 端在机票航变和酒店相关简单业务做了 Flutter 试水，我们对接的首个版本是 1.12，稳定性和性能都符合预期。对于这种简单的纯展示页面，是非常适合用 Flutter 的。像机票航班详情页最近的新需求完全靠 1 人开发就可以。</li>
<li>经过简单业务试点，稳定性和性能都符合预期，也建立了对 Flutter 信任感，后面开始在比较复杂的业务上试点，用到了非常多的基础功能，包括视频播放功能对接，为后面全面开始 Flutter 建设打好基础。</li>
</ul>
<p>结果：从性能表现上看，低端机性能上加载耗时优于 iOS，帧率接近原生，CPU 负载、内存消耗接近原生，整体的稳定性非常不错。</p>
<p><img alt class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/7fbd58e81c7349d8b3a642031161a5df~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<ul>
<li>纯 Flutter 业务试点同时，我们也在做 Web on Flutter 业务试点，H5 代码基本不用改造就能运行在 Flutter 上。3月底的版本我们有次大的性能优化，同时也会上线iOS。</li>
</ul>
<h2 data-id="heading-19">五、面临挑战与未来规划</h2>
<p><img alt class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/065ea9502d544404a3ca49413d221982~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer">
近期更新：飞猪9.7.2.105版本升级到Hummer Flutter 1.22 版本，在poi详情页，平均帧率从 53 提升到 56。
3月4号Flutter 2.0 重要发布，亮点很多，优化多引擎实例支持，对混合栈应用开发更友好。
<img alt class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/4940f7e2195c4c9480a01f4fc1ebf175~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p></div> <div class="image-viewer-box" data-v-78c9b824><!----></div>  
</div>
            