
---
title: '如何使用 DDD 指导微服务拆分？｜8月更文挑战'
categories: 
 - 编程
 - 掘金
 - 标签
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/e81fb099befe40688389e980311b6996~tplv-k3u1fbpfcp-zoom-1.image'
author: 掘金
comments: false
date: Sun, 01 Aug 2021 19:54:20 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/e81fb099befe40688389e980311b6996~tplv-k3u1fbpfcp-zoom-1.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><blockquote>
<p>我是架构精进之路，大厂架构师，CSDN 博客专家，点击上方“关注”，坚持每天为你分享技术干货，私信我回复“01”，送你一份程序员成长进阶大礼包。</p>
</blockquote>
<h2 data-id="heading-0">软件架构发展经历</h2>
<p>软件架构的发展经历了从单体架构、垂直架构、SOA 架构到微服务架构以及到现在最新的 service mesh（网格服务架构）的过程。借用 dubbo 的网站架构发展图和说明：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/e81fb099befe40688389e980311b6996~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-1">微服务存在的问题</h2>
<p>进入微服务之后 ， 解决了集中式架构的单体应用很多问题， 但是新的问题应运而生 ， 微服务的力度应该多大 ？微服务如何设计呢？微服务如何拆分 ？微服务边界在哪里 ？</p>
<p>很长时间人们都没有解决这一问题，就连 Martin Fowler 在提出微服务架构的时候也没有告诉我们这该如何拆分微服务。</p>
<p>甚至在很长的时间里人们对微服务拆分产生了一些误解， 有人认为："微服务很简单，就是将之前的单体应用拆分成多个部署包， 或者将原来的单体应用架构替换为一套支持微服务的技术架构，就算是微服务了。" 还有人认为微服务应该拆分得越小越好。</p>
<p>鉴于上述情形， 很多项目因为前期拆分过度， 导致复杂度过高， 导致后期难以运维甚至难以上线。</p>
<p>可以得出一个结论：<strong>微服务拆分困境产生的根本原因就是不知道业务或者微服务的边界到底在什么地方。换句话说，确定了业务边界和应用边界，这个困境也就迎刃而解了。</strong></p>
<h2 data-id="heading-2">DDD 的诞生</h2>
<p>而 DDD 就是解决了这个确定业务边界的问题，可见 DDD 并不是一种技术架构，而是一种划分业务领域范围的方法论。DDD 的兴起是由于很多熟悉领域驱动建模(DDD)的工程师在进行微服务设计时， 发现用 DDD 的思路进行业务梳理可以很好规划服务边界， 可以很好实现微服务内部和外部的"高内聚、低耦合"。于是越来越多的人将 DDD 作为业务划分的指导思想。</p>
<p>DDD 是一种拆解业务、划分业务、确定业务边界的方法， 是一种高度复杂的领域设计思想，将我们的问题拆分成一个个地域， 试图分离技术实现的复杂性，主要解决的是软件难以理解难以演进的问题，DDD 不是一种架构， 而是一种架构方法论， 目的就是将复杂问题领域简单化， 帮助我们设计出清晰的领域和边界， 可以很好的实现技术架构的演进。DDD 包括两部分，战略设计部分和战术设计部分。</p>
<ul>
<li>
<p><strong>战略设计</strong>主要从业务视角出发，建立业务领域模型，划分领域边界，建立通用语言的限界上下文，限界上下文可以作为微服务设计的参考边界。</p>
</li>
<li>
<p><strong>战术设计</strong>则从技术视角出发，侧重于领域模型的技术实现，完成软件开发和落地，包括：聚合根、实体、值对象、领域服务、应用服务和资源库等代码逻辑的设计和实现。</p>
</li>
</ul>
<h2 data-id="heading-3">微服务拆分难题</h2>
<p>开发者在刚开始尝试实现自己的微服务架构时，往往会产生一系列问题 ：</p>
<ul>
<li>
<p>微服务到底应该怎么划分？</p>
</li>
<li>
<p>一个典型的微服务到底应该有多微？</p>
</li>
<li>
<p>如果做了微服务设计，最后真的会有好处吗？</p>
</li>
</ul>
<p>回答上面的问题需要首先了解微服务设计的逻辑，<strong>科学的架构设计应该通过一些输入并逐步推导出结果</strong>，架构师要避免凭空设计和“拍脑门”的做法。</p>
<p>服务的划分有一些基本的方法和原则，通过这些方法能让微服务划分更有操作性。最终在微服务落地实施时也能按图索骥，无论是对遗留系统改造还是全新系统的架构都能游刃有余。</p>
<h2 data-id="heading-4">微服务拆分的几个阶段</h2>
<p>在开始划分微服务之前，架构师需要在大脑中有一个重要的认识：<strong>微服务只是手段，不是目的。</strong></p>
<p>微服务架构是为了让系统变得更容易拓展、更富有弹性。在把单体应用变成靠谱的微服务架构之前，单体系统的各个模块应该是合理、清晰地。</p>
<p>也就是说，从逻辑上单体系统和微服务没有区别，某种理想情况下微服务只是把单体系统的各个模块分开部署了而已</p>
<p>大量的实践教训告诉我们，混沌的微服务架构，比解耦良好的单体应用会带来更多麻烦。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/6af3589b038d4696ba1e9681092a810a~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>混乱的微服务VS良好的单体</p>
<p>领域驱动设计立足于面向对象思想，从业务出发，通过领域模型的方式反映系统的抽象，从而得到合理的服务划分。</p>
<p>采用 DDD 来进行业务建模和服务拆分时，可以参考下面几个阶段：</p>
<ul>
<li>
<p>使用 DDD（领域驱动建模） 进行业务建模，从业务中获取抽象的模型（例如订单、用户），根据模型的关系进行划分限界上下文。</p>
</li>
<li>
<p>检验模型是否得到合适的的抽象，并能反映系统设计和响应业务变化。</p>
</li>
<li>
<p>从 DDD 的限界上下文往微服务转化，并得到系统架构、API 列表、集成方式等产出。</p>
</li>
</ul>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/f0337f24ae9146c0a2b89943ce4df63d~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>使用DDD划分微服务的过程</p>
<h3 data-id="heading-5">如何抽象？</h3>
<p>抽象需要找到看似无关事务的内在联系，对微服务的设计尤为重要。</p>
<p>然而现实的例子比比皆是，电信或移动营业厅还需要用户分两步办理号卡业务、宽带业务。原始是不合适的抽象模型造成的，并最终影响了微服务的划分。</p>
<p>我们可以使用概念图来描述一些概念的抽象关系。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/f27eff8e72ff4dc494368c04ebdf76d3~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>商品这一概念的概念图</p>
<p>如果没有抽象出领域模型，就得不到正确的微服务划分。</p>
<h3 data-id="heading-6">使用 DDD 进行业务建模</h3>
<p>通过利用 DDD 对系统从业务的角度分析，对系统进行抽象后，得到内聚更高的业务模型集合，在 DDD 中一组概念接近、高度内聚并能找到清晰的边界的业务模型被称作限界上下文（Bounded Context）。</p>
<p>限界上下文可以视为逻辑上的微服务，或者单体应用中的一个组件。</p>
<p>在电商领域就是订单、商品以及支付等几个在电商领域最为常见的概念；在社交领域就是用户、群组、消息等。</p>
<p>DDD 的方法论中是如何找到子系统的边界的呢？</p>
<p>其中一项实践叫做事件风暴工作坊，工作坊要求业务需求提出者和技术实施者协作完成领域建模。把系统状态做出改变的事件作为关键点，从系统事件的角度触发，提取能反应系统运作的业务模型。再进一步识别模型之间的关系，划分出限界上下文，可以看做逻辑上的微服务。</p>
<p>事件是系统数据流中的关键点，类似于电影制作中的关键帧。</p>
<blockquote>
<p>例如系统管理员可以登录、创建商品、上架商品，对应的系统状态的改变是用户已登录、商品已创建、商品已经上架；相应的顾客可以登录、创建订单、支付，对应的系统状态改变是用户已登录、订单已创建、订单已支付。</p>
</blockquote>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/f8e59dae7ed14ed990a435e06916cd88~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>利用事件刺探业务黑盒并抽象出模型</p>
<p>在得到模型之后，通过分析模型之间的关系得出限界上下文。例如商品属性和商品相对于用户、用户组关系更为密切，通过这些关系作出限界上下文拆分的基本线索。</p>
<p>其次是识别模型中的二义性，让限界上下文划分更为准确。</p>
<blockquote>
<p>例如，在电商领域，另外一个不恰当设计的例子是：把订单中的订单项当做和商品同样的概念划分到了商品服务</p>
</blockquote>
<p>但订单中的商品实际上和商品库中的商品不是同一个概念。当订单需要修改订单下的商品信息时，需要访问商品服务，这势必造成了订单和商品服务的耦合。</p>
<p>合理的设计应该是：商品服务提供商品的信息给订单服务，但是订单服务没有理由修改商品信息，而是访问作为商品快照的订单项。</p>
<p>订单项应该作为一个独立的概念被划分到订单服务中，而不是和商品使用同一个概念，甚至共享同一张数据库表。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/b056c7a2974345ad853854d3ac761b25~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>典型具有”二义性“陷阱的场景</p>
<p>一组关系密切的模型形成了上下文（context），二义性的识别能帮我们找到上下文的边界（bounded）。</p>
<h3 data-id="heading-7">验证和评审领域模型</h3>
<p>前面我们说到限界上下文可以作为逻辑上的微服务，但并不意味着我们可以直接把限界上下文变成微服务。</p>
<p>限界上下文被设计出来后，验证它的方法可以从我们采用微服务的两个目的出发：降低耦合、容易扩展，可以作为限界上下文评审原则：</p>
<p>**原则 1：**设计出来的限界上下文之间的互相依赖应该越少越好，依赖的上游不应该知道下游的信息。</p>
<p>**原则 2：**使用潜在业务进行适配，如果能在一定程度上响应业务变化，则证明用它指导出来的微服务可以在相当一段时间内足以支撑应用开发。</p>
<p>但是理想的领域模型往往抽象程度、成本、复用性这几个因素中获取平衡。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/529a3d1e5101417ba15c6e7c2a400d75~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>”抽象”的成本</p>
<p>用一个简单的图来表达话，我们的领域模型设计往往在复用性和成本取得平衡的中间区域才有实用价值。</p>
<h3 data-id="heading-8">几个典型的误区</h3>
<p>在大量使用 DDD 指导微服务拆分的实践后，我们发现很多系统设计存在一些常见的误区</p>
<p>主要分为两类：未成功做出抽象、抽象程度过高、错误的抽象。</p>
<p><strong>1）未成功做出抽象</strong></p>
<p>在实际开发过程中，大家都有一个体会，设计阶段只考虑了一些常见的服务，但是发现项目中有大量可以重用的逻辑，并应该做成单独服务。</p>
<p>当我们在做服务拆分时，遗漏了服务的结果是有一些业务逻辑被分散到各个服务中，并不断重复。</p>
<p><strong>2）抽象程度过高</strong></p>
<p>抽象程度过高最典型的一个特征是得到的限界上下文极端的微小。</p>
<p>抽象程度过高带来的成本有：更多的微服务部署带来的运维压力、开发调试难度提高、服务间通信带来的性能开销、跨服务的分布式事务协调等。因此抽象不是越高越好，应根据实际业务需要和成本考虑。</p>
<p>那相应的，微服务到底应该多小呢？</p>
<p>业界流传一句话来形容，微服务应该多小：“一个微服务应该可以在二周内完成重写“。</p>
<p>这句话可能只是一句调侃，如果真的作为微服务应该多微的标准是不可取的。</p>
<p>微服务的大小应该取决于划分限界上下文时各个限界上下文内聚程度。</p>
<p><strong>3）错误抽象</strong></p>
<p>对微服务或 DDD 理解不够。模型具有二义性，被放到不同的限界上下文。</p>
<blockquote>
<p>例如，订单中的收货地址、用户配置的常用地址以及地址库中的标准地址。</p>
</blockquote>
<p>这三种地址虽然名称类似，但是在概念上完全不是一回事</p>
<p>假如架构师将”地址“划分到了标准地址库中，势必会造成用户上下文和系统配置上下文、订单上下文存在不必要的耦合。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/c52c089fb93e49bab043eb04341e2d38~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>抽象错误带来的依赖</p>
<p>上图的右边为正常的依赖关系，左边产生了不正常的依赖，会进一步产生双向依赖。</p>
<h3 data-id="heading-9">从限界上下文到系统架构</h3>
<p>在通过 DDD 得到领域模型和限界上下文后，理论上我们已经得到了微服务的拆分。但是，限界上下文到系统架构还需要完成下面几件事。</p>
<p><strong>1）设计微服务之间的依赖关系</strong></p>
<p>一个合理的分布式系统，系统之间的依赖应该是非常清晰地。依赖，在软件开发中指的是一个应用或者组件需要另外一个组件提供必要的功能才能正常工作。因此被依赖的组件是不知道依赖它的应用的，换句话说，被调用者不需要知道调用方的信息，否则这不是一个合理的依赖</p>
<p>在微服务设计时，如果 domain service 需要通过一个 from 参数，根据不同的渠道做出不同的行为，这对系统的拓展是致命的。例如，用户服务对于访问他的来源不应该知晓；用户服务应该对订单、商品、物流等访问者提供无差别的服务。</p>
<p>因此，微服务的依赖关系可以总结为：上游系统不需要知道下游系统信息，否则请重新审视系统架构。</p>
<p><strong>2）设计微服务间集成方式</strong></p>
<p>拆分微服务是为了更好的集成到一起，对于后续落地来说，还有服务集成这一重要的阶段。</p>
<p>微服务之间的集成方式会受到很多因素的制约，前面在讨论微服务到底有多微的时候就顺便提到了集成会带来成本，处于不同的目的可以采用不同的集成方式。</p>
<ul>
<li><strong>采用 RPC（远程调用） 的方式集成。</strong></li>
</ul>
<p>使用 RPC 的方式可以让开发者非常容易的切换到分布式系统开发中来，但是 RPC 的耦合性依然很高，同时需要对 RPC 平台依赖。业界优秀的 RPC 框架有 dubbo、Grpc、thrift 等</p>
<ul>
<li><strong>采用消息的方式集成。</strong></li>
</ul>
<p>使用消息的方式异步传输数据，服务之间使用发布-订阅的方式交互。另外一种思想是通过对系统事件传递，因此产生了 Event Sourcing 这种集成模式，让微服务具备天然的弹性。</p>
<ul>
<li><strong>采用 RESTful 方式集成。</strong></li>
</ul>
<p>RESTful 是一种最大化利用 HTTP 协议的 API 设计方式，服务之间通过 HTTP API 集成。这种方式让耦合变得极低，甚至稍作修改就可以暴露给外部系统使用。</p>
<p>这三种集成方式耦合程度由高到低，适用于不同的场景，需要根据实际情况选择，甚至在系统中可能同时存在。</p>
<p>服务间集成的方式还有其他方式，一般来说，上面三种微服务集成的方式可以概括目前常见系统大部分需求。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/2911d4e476164f54b519325a991d19aa~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-10">总结</h2>
<p>这篇文章主要研讨了 DDD 火起来的原因， 解决了什么业界难题， 知道 DDD 主要思路 ， 以及 DDD 大概的实现步骤等 。</p>
<p>逻辑往往比经验更为重要。写这篇文章的初衷是为了得到微服务划分的依据是什么，我该怎么有说服力的回复？</p>
<p>是具体情况具体分析？By experience？还是说，我是通过一套方法对业务逻辑进行分析得到的。</p>
<ul>
<li>
<p>当没有足够的经验直接解决问题，或问题庞大到不足以使用经验解决时，能支撑你做出决策就只有对输入问题进行有效的分析。</p>
</li>
<li>
<p>使用 DDD 指导微服务划分，能在一定程度上弥补经验的不足，做出有理有据的系统架构设计。</p>
</li>
</ul>
<blockquote>
<p>我是架构精进之路，大厂架构师，CSDN 博客专家，点击上方“关注”，坚持每天为你分享技术干货，私信我回复“01”，送你一份程序员成长进阶大礼包。</p>
</blockquote></div>  
</div>
            