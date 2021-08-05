
---
title: 'iOS开发App组件化之路'
categories: 
 - 编程
 - 掘金
 - 热门
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/bd57077715304736bb1fea5754e1b015~tplv-k3u1fbpfcp-zoom-crop-mark:1280:960:0:0.image'
author: 掘金
comments: false
date: Fri, 23 Jul 2021 00:02:39 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/bd57077715304736bb1fea5754e1b015~tplv-k3u1fbpfcp-zoom-crop-mark:1280:960:0:0.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>原创：GuoJin 百度APP技术团队-资深技术专家</p>
<blockquote>
<p>组件化是一个老生常谈的涉及面很广的话题，即不是做好一件事而是做好一系列的事情才能达成；其中包含组件化框架在内的各架构层级、构建系统、依赖管理系统、以及配套的防劣化机制与规则规范。<br>
本文主要基于百度App背景、目标和组件化历程来讲述保障并行开发和组件复用的手段，尽量避免过多发散到构建系统、依赖管理系统,以及组件化框架这样的具体子方向。组件化的重要性取决于应用规模、团队规模、产品技术目标；所述内容虽然是从iOS平台出发，但方法论与实现路径适用于大部分平台。</p>
<p>干货：<a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fuzi-yyds-code" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/uzi-yyds-code" ref="nofollow noopener noreferrer">Github</a></p>
</blockquote>
<h4 data-id="heading-0">背景与目标</h4>
<p>百度App(大型App)复杂度来源</p>
<ul>
<li>业务规模大：百度App技术方向及子方向70+，单端代码量180w+；<br>
目标：隔离各组件间影响避免故障蔓延，并控制整体App的复杂度；</li>
<li>团队规模大：有代码权限的数百人;<br>
目标：保障高效并行开发；</li>
<li>公司内部接入业务多：30+,非单纯基础库，与百度App关系复杂；<br>
目标：处理接入业务与百度App架构及架构中各组件关系，保障快速高效接入与基础能力复用。</li>
<li>迭代速度快：3周一个版本，2周开发1周测试；<br>
目标：避免高速迭代情况下组件化程度劣化。</li>
<li>技术形态多：H5、NA、Hybrid、Talos、Flutter并存；<br>
目标：保障基础能力复用，构建系统支撑。</li>
</ul>
<p>另外启动速度、体积等准入流程的约束；以及目标的多样性也是大型App复杂度来源因素；由背景产生的目标是天生的技术需求，除此之外，百度App在不同阶段有不同的产品技术目标。<br>
百度App不同阶段的不同目标</p>
<ul>
<li>合作业务三方库复用;单个技术组件输出(最早的需求，2014年),对单个组件输出来讲，如何避免输出时,拔出萝卜带出"泥";</li>
<li>矩阵产品孵化（2017年~2019）；</li>
<li>小程序开源复用（2018年）：输出组件兼容不同宿主,保持部分依赖组件可替代性； 目标多样性要求在开发时考虑到各个目标的诉求，在方案设计时尽量避免和这些目标冲突。</li>
</ul>
<h4 data-id="heading-1">重要架构迭代</h4>
<p>初始态-2013(钻木取火)：<br>
这一时期，百度App浏览器角色较重，大家都在一个工程里开发，各业务和基础逻辑交错，没有边界，你中有我、我中有你；UI架构比较复杂，每个RD都要从App主入口开始看懂主流程代码，小心翼翼的开发。<br>
这一时期的架构是这样：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/bd57077715304736bb1fea5754e1b015~tplv-k3u1fbpfcp-zoom-crop-mark:1280:960:0:0.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>这一时期的主要问题有：</p>
<ul>
<li>一些基础库、甚至开源三方库都会有业务侵入；没有明确分层和防修改机制，入侵成本极低；</li>
<li>首屏各业务间没有容器隔离，牵一发而动全身，极容易互相影响；</li>
<li>对各业务共用的服务(远程配置、端能力)没有服务组件化，if else/switch case式逻辑无限蔓延；</li>
<li>逻辑、资源没有合理归属，数据没有拆分，基础组件对外输出困难；</li>
<li>插件接口层没有体系化建设，稳定性欠佳(fragile)；接入业务成为百度App里的超级模块，依赖关系难以控制。</li>
</ul>
<h4 data-id="heading-2">2014-2015(蒸汽机时代)：</h4>
<p>虽然当时团队规模只有几十人，但已经意识到了组件化的重要性；接入业务逐步变多，同时也有部分技术组件对外输出的需求；这一阶段：</p>
<ul>
<li>首先拆出三方库，粗粒度拆出基础库，归到业务组件下层；百度App和接入业务复用这部分基础库；</li>
<li>引入框架容器，对首屏各业务及栈式导航容器中的业务进行隔离；</li>
<li>对新兴的业务组件或需要重构的业务，首先采用组件化模式开发，逻辑、资源、数据各有归属，同时明确外部依赖；</li>
<li>初步制定了依赖规范，禁止层级反向依赖，这一阶段只是规范，没有工具链的强制支撑;</li>
<li>组件除基础库外的依赖通过Adapter注入来实现。</li>
</ul>
<h4 data-id="heading-3">这一时期的架构是这样：</h4>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/995e0c8016b845bd97dbe3f5f47003ff~tplv-k3u1fbpfcp-zoom-crop-mark:1280:960:0:0.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>这一时期的主要问题有：</p>
<ul>
<li>组件归属的模糊性,部分组件游离在基础库和业务组件之间，同层组件间的依赖与调用关系不够清晰；</li>
<li>组件间通过Adapter进行一对一解耦，虽然有比较明确的外部依赖关系，但解耦效率不高;</li>
<li>主App中还遗留端能力接口，与通过插件系统接入的一些SDK。</li>
</ul>
<p>2016-2017（电力时代）<br>
这一时期重点建设了组件化框架（Pyramid、SchemeRouter）与分发框架(RemoteConfig、PMS、预取分发)，及数据拆分框架（CocoaSetting）；进一步保障了各组件能做到逻辑、数据各有归属；</p>
<p>这一时期的架构是这样：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/8a351f51477d4059a64a76b9620b9a7a~tplv-k3u1fbpfcp-zoom-crop-mark:1280:960:0:0.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>image</p>
<h4 data-id="heading-4">2018-2019(理想态-核能时代)</h4>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/e2ab0b213887497784b761a589590914~tplv-k3u1fbpfcp-zoom-crop-mark:1280:960:0:0.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>这一时期，组件化框架相对完善，各组件已能做到逻辑、资源、数据各有归属。<strong>主工程进一步被弱化</strong>；</p>
<ul>
<li>层级更加明确清晰，游离与基础库层和业务组件层间的通用服务有了归属;组件可以自下而上的对外输出；</li>
<li>整个App通过中央仓库的组件列表(Central Repo Specs)，经过EasyBox组装整个工程；</li>
<li>框架容器加载及系统事件分发统一到轻量级的AppLauncher;</li>
<li>对接入SDK，按架构层级属性归属；如仅被某一个业务组件引用，则有这个业务组件负责管理，降低对外的复杂度；</li>
<li>服务层可共享服务相对完善。</li>
</ul>
<p>组件化的进阶-中台化（星际远航）<br>
中台化的大潮滚滚而来,除云端一体化复用外，对组件化也提出了其他的更高要求。共享组件库+构建系统(EasyBox)合力，已能达到矩阵产品组合输出能力。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/5f010beb8bce4d2d9f17337642ef47fb~tplv-k3u1fbpfcp-zoom-crop-mark:1280:960:0:0.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>image</p>
<h4 data-id="heading-5">组件化的实现路径</h4>
<p><strong>自下而上的组件化建设</strong></p>
<h4 data-id="heading-6">1、编译隔离、架构分层及层级访问限制机制建立</h4>
<ul>
<li>编译隔离：通过构建系统（EasyBox）提供的编译规则文件明确每个组件的对外接口，明确组件的外部依赖（这方面IDE也经常好心办坏事，让组件间可以低成本的随意访问，逐步模糊了组件的逻辑边界，加深了组件间的依赖）；</li>
<li>层间限制：通过构建系统（EasyBox）建立反向访问限制，即下层组件不可以访问上层组件；</li>
<li>同层访问：同层组件间也不能无限制调用，通信及访问限制通过组件化Pyramid框架来完成；各组件间维持较清晰的接口边界和逻辑边界。</li>
</ul>
<h4 data-id="heading-7">2、三方库规范化与基础库体系化</h4>
<p>1)基础库主要存在以下问题：</p>
<ul>
<li>没有防修改机制，业务侵入成本低；</li>
<li>交叉依赖问题:同一基础依赖的逻辑归属到同一组件里;</li>
</ul>
<p><strong>基础库要在无业务侵入的情况下经过一定程度的抽象到架构底层，二进制化实行组件负责人制度，并进行体系化建设避免上述问题。</strong></p>
<p>2)三方库主要存在以下问题：</p>
<ul>
<li>没有防修改机制，业务侵入成本低；</li>
<li>三方库在一定用户规模或业务规模下，确实存在bug，而github的push request不及时或无响应；</li>
</ul>
<p><strong>所有三方库更新到最新发布版并二进制化避免业务侵入；差异部分明确修改点，通过运行时单独打补丁；对外输出时，明确这一点。</strong></p>
<h4 data-id="heading-8">3、建立运行时分发与隔离服务</h4>
<p>为避免各组件对共有逻辑、共有数据集中式处理，建立容器及分发机制来分发事件、数据、以及逻辑调用。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/66c1005130804df1affeeef9cdfc813c~tplv-k3u1fbpfcp-zoom-crop-mark:1280:960:0:0.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>image</p>
<p>Pyramid组件化框架：</p>
<ul>
<li>这里主要讲Pyramid框架的分发作用，Pyramid将系统事件分发给各子组件；</li>
<li>除此之外，组件化框架还有另外两个作用：<br>
1)Pyramid框架组件间通信：adapter一对一方式解耦升级为一对多解耦；<br>
2)它将组件间的强依赖转变为弱依赖，这让技术组件对外输出时，被依赖的组件具有某种程度的可替代性；</li>
</ul>
<p>端能力：</p>
<ul>
<li>分离SchemeRouter与SchemeHandler逻辑，SchemeRouter归属服务层组件化框架，SchemeHandler归属各组件；</li>
<li>由于Scheme参数不够明确清晰，在百度App中Scheme主要用于和H5的通信，较少用于页面路由；</li>
</ul>
<p>配置分发服务：将集中解析并调用各业务处理逻辑改造为分发机制，并最终升级为云控服务；<br>
数据拆分服务：配合配置分发服务，将数据拆分到各组件内部管理；<br>
资源/预取分发服务：建立资源/预取分发服务；<br>
框架容器：通过Tab导航容器、栈式导航容器将各控制器UI数据拆分到各子控制器、事件分发传递给各子控制器；</p>
<h4 data-id="heading-9">分发与隔离机制、容器机制是并行开发的重要保障。</h4>
<p>4、服务层建立<br>
多业务调用的低依赖组件去业务化抽象成通用服务：账号、分享、云控、统计、性能、AI等<br>
5、建立组件模型<br>
建立组件模型，各业务模块快速组件化。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/08775de0992a4a2899b8c41bfb24381c~tplv-k3u1fbpfcp-zoom-crop-mark:1280:960:0:0.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>image</p>
<ul>
<li>通俗的讲，就是指导各业务模块明确功能范围，做到逻辑、资源、数据、私有SDK各有归属；</li>
<li>最终每个组件是一个独立的功能单元、逻辑单元、数据及资源管理单元，H5通信单元，性能量化单元，编译输出单元(1个或多个)。</li>
<li>为了更灵活的组合输出，组件的接口封装层和服务对接层可以进行不同粒度编译单元拆分；主要目的是分离依赖，满足输出灵活性；</li>
</ul>
<p>6、业务组件化 按照组件模型，确定业务的功能范围、逻辑与接口边界，快速组件化。<br>
7、劣化控制 组件接口变更、依赖变更、Warning数变化都会记录通知相关负责人，这些在Tekes平台管理；敬请继续关注后续公众号文章；没有防劣化机制，填坑速度永远比不上挖坑速度；一人填坑的速度也永远比不上多人挖坑速度。</p>
<h4 data-id="heading-10">收益总结</h4>
<p>1.研发效率的提升，主要体现在以下几个方面：</p>
<ul>
<li>复杂度控制：复杂度控制在组件内部，对外"简单可依赖"；</li>
<li>并行开发：组件化框架及各分发服务具备设计时的隔离性，保障大规模并行开发效率；以远程配置为例，原来新增一项开发时间为4+小时，现在仅需0.5小时；效率提升8倍+;</li>
<li>复用：为矩阵产品输出轮子；参考百度App矩阵产品，复用率都在50%以上；</li>
<li>编译速度提升：因为组件具有独立编译单元的属性,在编译过程中组件源码和编译产物可以等价替换，所以组件化也为后续组件二进制化打下基础，百度App编译速度也平均值从15分钟/次优化到2分钟/次；</li>
</ul>
<p>2.质量上，组件化具备设计时的隔离性，确保单个组件的故障影响范围内敛到自己内部，不会引发整体crash；<br>
3.为启动速度、体积等方向提供量化单位；</p>
<h4 data-id="heading-11">4.建立健全架构体系，分组件深度优化。</h4>
<p>吴军博士在《文明之光》一书中评价希腊人对世界文明的贡献这样写到：近代自然科学的很多体系都是在古希腊时代奠定的，希腊人在学术研究上有别于东方文明之处不在于一两项科学发明和发现，而在于他们将自然科学各学科分门别类，对每一个学科都建立起一整套系统的体系，在此基础上，演绎或归纳出普遍规律性，即定理或定律，继而成为自然科学各个学科的基石和支柱。</p>
<p>虽然没有这样的高度，但对软件开发来讲，也有异曲同工的作用。</p>
<p><strong>结语</strong></p>
<p>"自己"得来终觉浅，引用一段话作为结语，节选自《每个架构师都应该研究下康威定律》</p>
<p>架构的目标是用于管理复杂性、易变性和不确定性，以确保在长期的系统演化过程中，一部分架构的变化不会对架构的其它部分产生不必要的负面影响。这样做可以确保业务和研发效率的敏捷，让应用的易变部分能够频繁地变化，对应用的其它部分的影响尽可能的小。</p>
<p>收入于：<a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fuzi-yyds-code" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/uzi-yyds-code" ref="nofollow noopener noreferrer">Github</a></p></div>  
</div>
            