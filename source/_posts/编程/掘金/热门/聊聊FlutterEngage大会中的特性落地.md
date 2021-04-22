
---
title: '聊聊FlutterEngage大会中的特性落地'
categories: 
 - 编程
 - 掘金
 - 热门
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/cce2476b4cf949c4bd973f831233faa2~tplv-k3u1fbpfcp-zoom-1.image'
author: 掘金
comments: false
date: Mon, 12 Apr 2021 19:32:39 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/cce2476b4cf949c4bd973f831233faa2~tplv-k3u1fbpfcp-zoom-1.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>作者：闲鱼技术——萧湘</p>
<p>flutter engage大会已经过去一段时间，闲鱼团队作为国内较早大规模使用flutter的团队，对flutter的每一次升级都感到兴奋无比，网上已经有很多介绍大会的flutte 2特性的介绍文章，就不会赘述具体特性，今天会从开发者的角度如何看待以及评论这些新特性，评估这些特性在业务场景应用，最后对flutter未来的展望，将来还有哪些值得期待的功能。</p>
<h2 data-id="heading-0">flutter2新特性</h2>
<h3 data-id="heading-1">全面支持Windows、MacOS、Linux、Web、iOS、Android六大平台</h3>
<p>本次flutter engage大会最大的亮点莫过于支持更多平台，在原有移动端的基础上，新增桌面、web端，从此flutter往真正的多平台迈向了更加坚实的一步，flutter2看起来更像全新的引擎。<img alt title="null" class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/cce2476b4cf949c4bd973f831233faa2~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-2">桌面平台</h3>
<p>flutter2全面支持目前主流的Windows、MacOS、Linux桌面平台，其实对于fluttre架构而言，因底层使用skia本身就跨多平台的缘故，从移动端扩展到桌面端是非常顺畅。</p>
<p><strong>优点：</strong></p>
<p>开发者编写一份Dart渲染代码，便可以部署到多个平台，是一个非常流畅的开发方式。</p>
<p><strong>目前存在的问题</strong></p>
<p>除了编写Dart渲染代码外，还需要关注工程所依赖的库是否都完美的支持了桌面版平台。谷歌声称其官方维护所有pub库已经全部支持web/macos/windows等平台，除此外社区其他的库还需要等待作者们升级，要想流畅升级的开发者们可能还需要尚待时日。</p>
<p>想要迁移至桌面平台的开发者们可以自行评估自己的工程所依赖的库。如果依赖的库大部分来自谷歌官方，且都支持了桌面平台，较少平台相关库，升级过程应该是非常顺畅的。</p>
<p><strong>闲鱼观点</strong></p>
<p>相比于业内其他成熟的跨平台桌面开发框架，学习成本比Qt偏小（Dart语言），性能比electron好，但现成的组件没有electron成熟，非常适合工具类的应用从移动端平滑的迁移到桌面端。</p>
<h3 data-id="heading-3">flutter web</h3>
<p>flutter web最开始的设计思路时使用Dart代码操作css或者Dom接口进行渲染，而到flutter2后已升级为framework和渲染层完全隔离，使用同一份Dart代码可以编译成多个平台。下面两图是基于操作系统的flutter架构和基于浏览器的flutter架构。</p>
<p><img alt="Windows/MacOS/Linux/iOS/Android" title="null" class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/15ca76f0ea684ea09541bf4783a7a0a4~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p>Windows/MacOS/Linux/iOS/Android架构</p>
<p><img alt title="null" class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/b4f35bb5fa14452ea53e4318af918939~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer">web架构</p>
<h3 data-id="heading-4">flutter web推荐场景</h3>
<p>相同一份Dart代码如今能跑在各种平台下了，部署到服务器上也能跑在web端了，那么在上面常见下使用flutter web是最合适的呢?</p>
<p>谷歌推荐使用flutter web的场景有</p>
<p>•Progressive Web Apps(PWA)•Single Page Apps（SPA）•现有app迁移</p>
<p>PWA和SPA是相对于传统web应用而言，传统web网页遵循请求-应答协议，网页内容的刷新和加载伴随着多次的网络请求。而PWA和SPA相对则会请求少，或者请求时回包的数据。 比如PWA，可以简单理解为这是一种期望运行在各种设备，接近Native应用保持一致体验的使用web应用。简单而言这是在用web技术模拟原生应用，这个应用渲染大部分代码无需网络请求，即开即用，可以无网络时离线运行，和普通原生功能一致，只是这是使用web技术编写，运行在浏览器的应用。常见的例子是安装在android设备的web twitter应用。</p>
<p>而SPA和PWA界限在于，SPA的界面代码第一次需要网络请求，而后每次的请求都是纯数据的请求。<img alt title="null" class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/190fa56de667489c804fc1cb1d4a999e~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer">PWA应用原理</p>
<p><img alt title="null" class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/ca465ce240a649289fdadde1687d08e5~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer">SPA应用原理</p>
<p>这三种场景使用flutter web的初衷是充分利用它相比传统web网页优越的渲染性能。如果使用flutter web来编写非常经典的web应用则既失去了利用flutter web优越渲染性能，又没法和传统web一样充分利用其成熟的生态。</p>
<h3 data-id="heading-5">如何迁移flutter web？</h3>
<p>无需配置特别的设置，直接使用IDE（VSCode或者Android Studio）编写flutter 工程后，使用<code>flutter build web</code>即可体验。</p>
<p>但有以下几点需要重点关注：</p>
<p>1、依赖的Flutter plugin需支持web 对于跨平台的plugin，需要重新支持web</p>
<p>2、响应式布局 相对于原有移动设备屏幕小，web端可能会运行在各种屏幕下，各种交互方式需要进行优化。</p>
<p>3、页面跳转/导航 页面的跳转从移动设备的单窗口，变成浏览器下的多窗口，多tab</p>
<p>4、桌面设备交互风格(鼠标、键盘) 支持浏览器下更加常用的鼠标键盘等的交互方式</p>
<p>5、渲染模式（HTML/CanvasKit） 需要根据业务需求选择flutter web的渲染方式（HTML渲染方式安装包小，性能较差，CanvasKit渲染方式安装包大，性能好）</p>
<p><strong>目前存在的问题</strong></p>
<p>因为浏览器的特性存在决定了，如要对一些于操作系统强相关的plugin库进行web的特性支持时，会存在困难，比如文件系统，各种社交媒体登录分享sdk等。因此进一步缩小了其使用的场景。</p>
<p><strong>闲鱼观点：</strong></p>
<p>flutter web的渲染性能虽不如基于操作系统架构的原生flutter应用，但优于能部署在服务器，但又比一般的web渲染性能稍好，所以非常适合对性能在有要求的web活动业务场景中使用。或作为原生flutter界面崩溃时的一种业务降级兜底方案，在紧急场景业务充当救火队员的角色。</p>
<h3 data-id="heading-6">支持嵌入式</h3>
<p>大会中介绍了丰田公司把flutter迁移到了嵌入式场景，但大会中也没有贴出详细的进展以及相关特性。只能继续期待了。<img alt title="null" class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/b2e2bbb6694b497597dd877211fe24d3~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p><strong>支持多屏设备</strong></p>
<p>这是微软为将自家设备surface duo设备，开辟一个独立的分支给flutter支持多屏特性。</p>
<p><img alt title="null" class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/8836aa56e46d417d94069f86670f80cd~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p>支持的特性能很好的支持多屏设备的特点，比如：</p>
<p>1.Extended Canvas: 双屏共享一个大canvas2.List-Detail: 左列表，右详情3.Two Page:多页，看书应用4.Dual View:双屏，相同内容不同角度的双屏5.Companion Pane:左显示，右配置</p>
<p>代码样例：</p>
<p>比如TwoPanel是新增的Widget，panel1、panel2传入两个不同屏幕的widget</p>
<pre><code class="copyable">Widget build(BuildContext context) &#123;
   return TwoPane(
      pane1: _widgetA(),
      pane2: _widgetB(),
      paneProportion: 0.3,
      panePriority: MediaQuery.of(context).size.width > 500 ? TwoPanePriority.both : TwoPanePriority.pane1,
   );
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img alt title="null" class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/eabe4e2d638c4714a1f5fc8e00c41d6d~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p>但目前这个分支由微软维护，暂未合入到flutter的主分支中 flutter github中开辟的两个issue在专门跟进 （issue77156[1] ，issue24756[2]） ，感兴趣的可以去到下方链接了解概况 <a href="https://devblogs.microsoft.com/surface-duo/flutter-dual-screen-foldable/" target="_blank" rel="nofollow noopener noreferrer">devblogs.microsoft.com/surface-duo…</a> [3]</p>
<h3 data-id="heading-7">Dart语言新特性</h3>
<p>flutter2中除了新增平台等新特性外，配套的Dart语言也推出新特性</p>
<h3 data-id="heading-8">Sound null safety</h3>
<p>Sound null safety我们暂且称为空安全声明，目的是通过显式声明可能为null的变量，增加Dart语言的鲁棒性。 因为Dart语言变量可以存null或者具体的值，因此在日常的开发中可能因为忘记赋值或者变量延迟赋值，导致访问某个变量时为null，导致程序运行时抛出exception。 这个功能推出后，可以从源码级解决null异常导致的错误。 简单的操作是在类型声明后添加？以标识这个变量是可以为null的。<img alt title="null" class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/c22b2e4f095f4b8eb7c4e20164b6ef1a~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p>•如何迁移？ 为Dart了这个语法糖，对于已有的项目如何升级?谷歌对此也提供了配套的升级工具，只需要在工程目录下使用<code>dart migrate</code>，就可以帮助你扫描整个工程中潜在的待替换的变量</p>
<p><img alt title="null" class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/764a817ff62a43a7b29ea55d4e8261c1~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p><strong>优点</strong></p>
<p>缓解因变量为null而抛出exception而引发的白屏，用户无法操作等体验问题。</p>
<p><strong>目前存在的问题</strong></p>
<p>但是开发者对于现存工程，一旦Dart代码一下子全部改造，无疑会增加系统风险，而且对于测试范围也会是非常繁重的任务。</p>
<p><strong>闲鱼观点：</strong></p>
<p>这个特性很好的将风险提前暴露在了编码阶段，又能顺带解决神出鬼没的null问题，性价比很高。但大规模改造也会引来问题，但这个特性非强制性的原因，为解决大规模改造可能导致的系统性风险，可以采取分批改造的方法进行。</p>
<h3 data-id="heading-9">FFI(Foreign Function Interface)</h3>
<p>动态库函数调用特性。特性的目的是让开发者更加方便的调用操作系统的动态库。 这个特性其实很早就已经有了，如今正式转正stable，开发者们可以放心使用了。</p>
<p>使用的方式也非常直观</p>
<p>1.编译某个平台下的动态库2.Dart代码中加载动态库，将Dart的函数和动态库的函数绑定3.Dart调用已绑好的函数即可</p>
<p><img alt title="null" class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/d7f15273088a4891961d2c63f1482778~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p>FFI更多详细看这里<a href="https://pub.dev/packages/ffigen" target="_blank" rel="nofollow noopener noreferrer">pub.dev/packages/ff…</a></p>
<p><strong>优点</strong></p>
<p>由静态库迁移到动态库后，可以减少安装包大小</p>
<p>相比于注入plugin模式去调用操作系统的接口，FFI更加友好，真正的按需加载，建议对于不常用频次少的的系统调用可使用FFI，对于优化整个engine初始化的加载速度有很好益处。</p>
<p><strong>闲鱼观点</strong>： 相对于旧的platform channel这种与C交互而言，FFI因需要动态库加载和符号绑定，性能不占优势，开发者们在选择这两种技术方案时是要权衡的。</p>
<h2 data-id="heading-10">社区其他</h2>
<p><strong>混合栈的跳转有官方支持了吗？</strong></p>
<p>对于众多团队而言，最初都是由原生的应用引入flutter，所以如何在原生界面和flutter界面跳转变成开发者非常强需求的功能点，flutter boost的推出是为解决混合栈界面跳转而提出的解决方案，但该方案也并非完美，最大问题在于多个flutter界面跳转时需要多开engine，无法共享engine中相同内存。针对这个问题flutter2中已经支持了engine多实例[4]，但官方也说了，这是一个正式实验中有风险的功能，但官方未提供不同技术栈之间的跳转方案（iOS/Android->flutter，flutter->iOS/Android），但在官方对于这个问题的技术路线图中也说到，以后这个特性是需要需要继续开发的，但目前还是建议使用futter boost方案。</p>
<p>多flutter界面技术路线：<a href="https://docs.google.com/document/d/1fdKRufqUzQvERcqNIUSq-GdabXc4k8VIsClzRElJ6KY/edit#" target="_blank" rel="nofollow noopener noreferrer">docs.google.com/document/d/…</a></p>
<h2 data-id="heading-11">细枝末节</h2>
<p>除了以上的一些比较大的功能点外，还有一些提升效率小工具</p>
<p>•flutter fix[5]:dart代码分析工具，能高亮废弃代码等•dartPad2.0[6]: 浏览器运行flutter小工程，所见即所得，验证小问题神器•FFI Gen[7]FFI Dart代码生成器，根据C接口批量生产FFI的Dart接口</p>
<h2 data-id="heading-12">展望</h2>
<p>从作为开发者的角度而言，flutter2扩展了更多的平台，让它在跨平台的路上越走越远。但与此同时，众多平台推出的同时，也会带来更多细枝末节的小问题，小issues，同时从官方的下一步的动作看，接下来将会聚集在支持一个社区中响应度比较大的好几个问题中</p>
<p>•为解决混合栈中内存过大而开发的多引擎实例特性•为解决开发时出现的性能UI调试难的问题，在着力开发devtools工具•dart语言因缺少命名空间，正在开发的类似特性等等</p>
<p>这些问题我们也在持续跟进中，如有进一步的进展，我们也会和大家持续的探讨。 更多flutter相关技术热点，欢迎大家持续关注闲鱼技术。</p>
<h3 data-id="heading-13">References</h3>
<p><code>[1]</code> issue77156: <em><a href="https://github.com/flutter/flutter/pull/77156" target="_blank" rel="nofollow noopener noreferrer">github.com/flutter/flu…</a></em><br>
<code>[2]</code> issue24756: <em><a href="https://github.com/flutter/engine/pull/24756" target="_blank" rel="nofollow noopener noreferrer">github.com/flutter/eng…</a></em><br>
<code>[3]</code> <a href="https://devblogs.microsoft.com/surface-duo/flutter-dual-screen-foldable/" target="_blank" rel="nofollow noopener noreferrer">devblogs.microsoft.com/surface-duo…</a> : <em><a href="https://devblogs.microsoft.com/surface-duo/flutter-dual-screen-foldable/" target="_blank" rel="nofollow noopener noreferrer">devblogs.microsoft.com/surface-duo…</a></em><br>
<code>[4]</code> engine多实例: <em><a href="https://flutter.dev/docs/development/add-to-app/multiple-flutters" target="_blank" rel="nofollow noopener noreferrer">flutter.dev/docs/develo…</a></em><br>
<code>[5]</code> flutter fix: <em><a href="https://flutter.dev/docs/development/tools/flutter-fix" target="_blank" rel="nofollow noopener noreferrer">flutter.dev/docs/develo…</a></em><br>
<code>[6]</code> dartPad2.0: <em><a href="https://dartpad.dev/flutter" target="_blank" rel="nofollow noopener noreferrer">dartpad.dev/flutter</a></em><br>
<code>[7]</code> FFI Gen: <em><a href="https://pub.dev/packages/ffigen" target="_blank" rel="nofollow noopener noreferrer">pub.dev/packages/ff…</a></em></p></div> <div class="image-viewer-box" data-v-78c9b824><!----></div>  
</div>
            