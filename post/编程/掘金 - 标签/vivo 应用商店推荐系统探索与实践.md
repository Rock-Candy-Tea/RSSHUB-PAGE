
---
title: vivo 应用商店推荐系统探索与实践
categories: 
    - 编程
    - 掘金 - 标签
author: 掘金 - 标签
comments: false
date: Sun, 21 Mar 2021 18:18:19 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/270c875552474849b8d14e6e3158c5bf~tplv-k3u1fbpfcp-zoom-1.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>介绍 vivo 应用商店推荐系统如何高效支撑个性化的推荐需求。</p>
<h1 data-id="heading-0">一、前言</h1>
<p>商店的应用数据主要来源于运营排期、CPD、游戏、算法等渠道，成立推荐项目之后也没有变化，发生变化的是由推荐系统负责和数据源进行对接，商店服务端只需要和应用推荐系统进行对接即可。</p>
<p>如果读者以为我们单纯是把商店服务端代码给照搬到推荐系统这边来了那就真的是too young too simple 了，不做优化或者升级直接copy一个系统是不可能的，这辈子都不可能。以下我将介绍我们如何去设计和规划应用推荐系统的。</p>
<h1 data-id="heading-1">二、面临的挑战</h1>
<p>在笔者眼中，商店应用推荐系统除了要具备高性能、高可用性及核心指标的监控能力之外，还有一个核心的能力就是高效支撑商店流量场景接入个性化推荐。</p>
<p>如何定义高效支撑？</p>
<ul>
<li>最起码能支撑三四个并行的需求同时进行吧。</li>
<li>一个需求开发周期最起码不能超过2天吧。</li>
<li>bug少一点吧，平均下来每个场景不应该超过2个吧。</li>
<li>产品同学的常态性的需求基本都能快速支持吧。</li>
</ul>
<p>分享我们一个应用推荐的策划case看看：</p>
<p><strong>在xx场景下，</strong></p>
<p><strong>如果主应用A属于应用类，</strong></p>
<blockquote>
<ul>
<li>则首先从从x1数据源去取Q1队列。</li>
<li>然后从x2数据源去取Q2队列。</li>
<li>然后用Q2队列去截断Q1队列，交集之后进行同开发者过滤和一级分类过滤。</li>
<li>如果交集为空则用Q2去兜底，然后取交集队列的n1和n2 位置上的元素作为返回队列。</li>
<li>如果前面都没有取到数据的话从大数据xxx表中按照主应用下应用点击的概率取点击率最高的分类下的n个，同时需要对这些数据进行队列内的同开发者过滤。</li>
</ul>
</blockquote>
<p><strong>如果主应用A属于游戏类，</strong></p>
<blockquote>
<ul>
<li>则xxxx</li>
<li>进行二级分类过滤</li>
<li>如果量不足的话，则从x(n)取数据然后进行处理，</li>
<li>如果数据不足3个的话，需要从周榜单中取同一级分类下的应用按照下载排行进行兜底。</li>
</ul>
</blockquote>
<p>没错，读者朋友不要怀疑自己，为了不把各位读者大大绕晕，我们这里只是挑选了一个简单的需求。实现这么一个功能也没有什么大不了的，但是当这种个性化推荐需求有几十个，后面还可能一致扩展下去的时候会不会心里发慌？来，简单看下我们现在个性化推荐的一部分需求，如图（一）所示：</p>
<p><img alt class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/270c875552474849b8d14e6e3158c5bf~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p>图（一）</p>
<p>使用商店服务端之前的case by case的开发方案，无论如何都无法实现上文中描述的要支撑商店高效接入推荐场景了，接着就是我们如何去实现优化的过程了。</p>
<h1 data-id="heading-2">三、如何解决</h1>
<p>为了更好的说明解决思路，我们从实际思考过程出发，一步步讲解问题的解决过程。</p>
<h2 data-id="heading-3">3.1 业务流程抽象</h2>
<p>单纯从策划上面来说，我们每个场景都需要至少做如图（二）中的几件事情：</p>
<p><img alt class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/484b902a41fc4e9fae4c0bac247ab68e~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p>图（二）</p>
<ul>
<li>**获取推荐列表：**调用各个数据源获取的推荐队列（需要注意的是不同场景下调用的接口并不一致，此外接口返回的字段和结构可能也不一样）。</li>
<li>**队列融合：**将1中提到的进行交集或者并集并等操作。</li>
<li>**数据过滤（队列内/队列间）：**在队列中进行各项过滤，过滤操作主要是为了提升相关性。</li>
<li>**数据兜底：**指在队列数据不够的时候，用榜单兜底，可能取周榜单数据的同一级分类数据，同二级分类数据。</li>
</ul>
<p>笔者从开发便捷性出发，对模型进行了进一步的调整，调整后为图（三）</p>
<p><img alt class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/49835aa55be34479bb05130fb3c8b753~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p>图（三）</p>
<p>获取队列后对队列进行安装过滤和队列内过滤(如主应用同开发者过滤等)可以进行流程合并，主要有如下的原因</p>
<ul>
<li>方便定义每一个数据源的过滤策略，实际需求中不同的队列也会使用不同的过滤策略。</li>
<li>这种方式非常匹配模板设计模式，能确保我们获取推荐列表过程是一致和稳定的。</li>
</ul>
<h2 data-id="heading-4">3.2 抽象流程延伸</h2>
<p>到图（三）这里，读者会发现我们依然没有能够解决我们前面提到的各种推荐场景里面的差异化过程。</p>
<p>其实在接触几个需求以后，我们会发现，想要在一套代码里面去解决这么大的差异性，几乎不可能，或者即使实现了，那么也会让代码变得无比复杂。与其这样子，我们还不如正视这种差异性，让差异在场景插件里面去实现，我们花更多的精力去打理主干。</p>
<p>那么为了支持让场景能够具备灵活的扩展能力，笔者在基于图（三）的基础上增加了四个环节：</p>
<ul>
<li>**队列结果线程内共享：**使用ThreadLocal来实现。存储各推荐队列的结果主要是为了便于后续使用某推荐队列做填充的需求，另外就是避免需要再重复请求三方数据接口，减少接口重复调用。</li>
<li>**插件队列兜底：**主要目的是在过滤后在数量不足需求的情况下，使用指定的队列完成填充，场景插件亦可按需填写实现填充逻辑，实现队列内容的补充。</li>
<li>**插件接口回调：**该环节主要是对前面的队列做个性化的处理，如对队列进行干预等，没有将插件接口回调和插件队列兜底融合在一起主要原因是插件队列融合可以实现可配置化的设置。</li>
<li>**周榜单兜底：**提供通用的周榜单数据查询能力，支持按照各种维度进行查询，此部分数据作为队列的最后兜底。</li>
</ul>
<p>拓展后的流程图如图（四）所示</p>
<p><img alt class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/6edf28fabd7544a8833745c3137fd47e~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p>图（四）</p>
<h2 data-id="heading-5">3.3 整体逻辑框图</h2>
<p>经过上述的分析可知，我们可以尽可能的把个性化的场景内容放在插件层实现，框架层负责加载按场景加载场景插件的具体个性化推荐逻辑。</p>
<p>系统从分层思路上讲从上至下共分为：插件层，框架层，协议适配层，数据源服务层，原子服务层，基础服务层，上层通过 SDK 依赖下层的服务（接口），各层次职责为：</p>
<ul>
<li>**插件层：**各个场景对应的插件，框架层对插件回调或者扩展接口提供默认实现，插件层按需实现具体的逻辑。</li>
<li>**框架层：**定义推荐数据的核心流程和执行逻辑，回调插件层的实现的扩展和回调接口。</li>
<li>**协议适配层：**负责按照场景找到场景对应的数据源服务，并封装转换协议和进行数据转换。</li>
<li>**数据源服务层：**与各个队列提供方提供的RPC服务封装层。</li>
<li>**原子服务层：**过滤类型的相关服务，主要是依赖于商店的 RPC 服务，使用组合的设计模式，服务可以进行组合。</li>
<li>**基础服务层：**支持从开发者、一级分类、二级分类、应用类型等纬度进行相关性的判断或者过滤，同原子服务层一样，此层服务也是原子粒度，支持进行组合控制。</li>
</ul>
<p><img alt class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/330cab19e2c3488f8e5a2087120d9b4d~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p>至此，相信大家都知晓了，针对于个性化的推荐，我们的开发工作最终将聚焦于开发场景插件，不需要再额外开发每一个业务流程了。</p>
<p>应用推荐系统架构</p>
<p><img alt class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/ffc3b24c66c8400e905489e1f9e3e170~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-6">3.4 关键实现</h2>
<p>在完成第三步整体逻辑框图设计之后，我们从场景参数定义，服务设计原则，设计模式使用，场景热插拔等方面进行了相关的方案研究并最终实现了方案的落地。</p>
<h3 data-id="heading-7">3.4.1 场景服务参数定义</h3>
<p>为实现推荐场景足够通用，我们将数据源层，原子服务层，基础服务层的内容进行了服务配置的映射，通过在配置中定义对应的配置项来实现服务的映射和组合，针对于差异性的内容在插件层进行实现。以如下的配置项示意图来说明：</p>
<ul>
<li>**sourceMap：**场景服务定义为map用于支持场景下多个模块或者实验组的情形，其中key为模块ID，商店服务端请求推荐的时候，需要携带此参数。</li>
<li>**cpdRequest 、algorithmRequest 、gameRequest：**用于定义对应的RPC调用的请求参数。</li>
<li>**filterRequest：**用于定义队列内的过滤请求，如主应用同开发者过滤等。</li>
<li>**unionStrategy：**定义队列合并和融合及队列间的合并规则。</li>
<li>**supplement：**兜底策略；</li>
<li>**sourceList：**使用的数据源，如上图中定义了两个数据源，则表示在此场景下需要从两个数据源获取数据，然后进行队列合并及后处理。</li>
</ul>
<p><img alt class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/96ce182e9c6e4dacba825564dfb78529~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-8">3.4.2 服务原子化与唯一化</h3>
<p>实现服务原子化与服务唯一化对本系统至关重要，在实现过程中是严格遵照如下两点来：</p>
<p>应用推荐依赖的三方RPC服务及内部的一些过滤逻辑都封装成了细粒度的原子服务（方法）的SDK。SDK中的内容不包含个性化推荐场景的具体业务性的能力，体现的重点是基础功能项，业务内容需要在场景插件中进行实现，统一类型的服务尽可能支持组合。</p>
<p>服务唯一化在对于实现系统的收敛和代码规模可控至关重要，我们也是不断的在朝着这个努力。各服务层都是以SDK的形式对外提供相关的功能，在SDK中实现服务调用入口的唯一性。</p>
<h3 data-id="heading-9">3.4.3 合理使用设计模式</h3>
<p>系统中使用了较多的设计模式来优化整体架构，如下重点来介绍使用的模板设计模式、策略模式及组合模式：</p>
<p>在获取推荐原始队列中使用了模板设计模式和策略模式来实现此过程。</p>
<blockquote>
<p>使用模板设计模式的好处显而易见，能够容易促进此部分处理逻辑流程化。</p>
<p>针对不同的数据源，需要使用不同的数据源服务和方法，使用策略模式的好处是便于定义在不同场景下对不同的接口的调用。</p>
</blockquote>
<p>同类型的原子服务或者方法尽可能支持组合模式，这种会为后续的扩展提供很大的便利性。</p>
<blockquote>
<p>以实际的实现方法来说明，在我们定义过滤类型的时候，支持传入多个过滤类型，上层业务在使用的时候按需传入即可。使用组合的设计模式在提升扩展性方面起到了巨大的作用。</p>
</blockquote>
<h3 data-id="heading-10">3.4.4 场景的热插拔</h3>
<p>系统中为实现场景之间的隔离和互不干扰，笔者使用了Java SPI的方式，在框架层定义了场景接口，接口实现类则在各个场景在独自的Jar中实现。这种方式有助于插件程序对框架层和基础服务层的侵入性降到最低。</p>
<h1 data-id="heading-11">四、带来的改变</h1>
<p>以前商店服务端在各个接口的service层写完整的推荐队列获取、融合、组装、过滤逻辑，有大量的重复内容，且随着版本的不断迭代，有很多版本不同的处理逻辑夹杂在一起，导致改造难升级难，牵一发动全身。目前应用推荐系统在两个方向带来较大改善：</p>
<ol>
<li>流程框架的逻辑完全抽象并独立，各个业务场景只需要按需写很少的插件回调逻辑即可，(不涉及十分特殊的场景可完全不用写插件回调扩展，通过配置对应的场景规则配置即可，可完全实现免开发，目前有30%左右的场景免开发)。</li>
<li>场景之间完全隔离和独立， 涉及复杂的功能升级可通过升级对应的场景id或者模块id来做增量实现，不影响现有逻辑。</li>
</ol>
<h1 data-id="heading-12">五、写在最后</h1>
<p>通过上述相关的方案落地，针对于各个推荐场景，我们大概减少了75%的开发工作量，同时bug率也得到大幅度的降低。</p>
<blockquote>
<p>作者：vivo-Huang Xiaoqun</p>
</blockquote></div> <div class="image-viewer-box" data-v-78c9b824><!----></div>  
</div>
            