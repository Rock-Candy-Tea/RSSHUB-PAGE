
---
title: '谈谈代码：降低复杂度，从放弃三层架构到DDD入门'
categories: 
 - 编程
 - 掘金
 - 标签
headimg: 'https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/7420601af47f493daf64f74a3f6873fb~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Fri, 30 Jul 2021 20:12:41 GMT
thumbnail: 'https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/7420601af47f493daf64f74a3f6873fb~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><blockquote>
<p>本文首发于<a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.jianshu.com%2Fu%2F204b8aaab8ba" target="_blank" rel="nofollow noopener noreferrer" title="https://www.jianshu.com/u/204b8aaab8ba" ref="nofollow noopener noreferrer">泊浮目的简书</a>:<a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.jianshu.com%2Fu%2F204b8aaab8ba" target="_blank" rel="nofollow noopener noreferrer" title="https://www.jianshu.com/u/204b8aaab8ba" ref="nofollow noopener noreferrer">www.jianshu.com/u/204b8aaab…</a></p>
</blockquote>















<table><thead><tr><th align="left">版本</th><th align="left">日期</th><th align="left">备注</th></tr></thead><tbody><tr><td align="left">1.0</td><td align="left">2021.8.1</td><td align="left">文章首发</td></tr></tbody></table>
<h1 data-id="heading-0">1.前言</h1>
<p>最近我发现团队项目中的某个应用复杂度越来越高，具体表现为：</p>
<ul>
<li>代码可读性较差：各个服务之间调用复杂，流程不清晰</li>
<li>修改部分业务导致大量测试用例失败，但很难快速的寻找出这些测试用例失败的根因</li>
</ul>
<p>基于这些情况，我开始寻找降低复杂度的方案，于是就有了这篇再谈DDD的文章。</p>
<h2 data-id="heading-1">1.1 具体问题</h2>
<h3 data-id="heading-2">1.1.1 宏观角度</h3>
<p>从宏观来说，软件架构模式演进经历了三个阶段。</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/7420601af47f493daf64f74a3f6873fb~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<ul>
<li>第一阶段是单机架构：采用面向过程的设计方法，系统包括客户端 UI 层和数据库两层，采用 C/S 架构模式，整个系统围绕数据库驱动设计和开发，并且总是从设计数据库和字段开始。</li>
<li>第二阶段是集中式架构：采用面向对象的设计方法，系统包括业务接入层、业务逻辑层和数据库层，采用经典的三层架构，也有部分应用采用传统的 SOA 架构。这种架构容易使系统变得臃肿，可扩展性和弹性伸缩性差。</li>
<li>第三阶段是分布式微服务架构：随着微服务架构理念的提出，集中式架构正向分布式微服务架构演进。微服务架构可以很好地实现应用之间的解耦，解决单体应用扩展性和弹性伸缩能力不足的问题。我们知道，在单机和集中式架构时代，系统分析、设计和开发往往是独立、分阶段割裂进行的。</li>
</ul>
<p>比如，在系统建设过程中，我们经常会看到这样的情形：A 负责提出需求，B 负责需求分析，C 负责系统设计，D 负责代码实现，这样的流程很长，经手的人也很多，很容易导致信息丢失。最后，就很容易导致需求、设计与代码实现的不一致，往往到了软件上线后，我们才发现很多功能并不是自己想要的，或者做出来的功能跟自己提出的需求偏差太大。</p>
<p>而且在单机和集中式架构这两种模式下，软件无法快速响应需求和业务的迅速变化，最终错失发展良机。此时，分布式微服务的出现就有点恰逢其时的意思了。</p>
<p>上面这部分来自于极客时间，这里面指出一般DDD是使用在微服务设计与拆分上，但我认为在单体应用中做模块的拆分也是可以并推荐的，这可以让你的模块在需要时可以即刻拆分出去——变成一个独立的微服务。相关可以参考<a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.jianshu.com%2Fp%2F85a42b1c145c" target="_blank" rel="nofollow noopener noreferrer" title="https://www.jianshu.com/p/85a42b1c145c" ref="nofollow noopener noreferrer">【ZStack】4.进程内服务</a>，这是一个开源，并实施于生产中很好的一个案例。</p>
<h3 data-id="heading-3">1.1.2 微观角度</h3>
<p>这个问题很简单，service的代码必然会越堆越多，而且聚拢越来越多的业务。</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/0ff55054463945708f16cce25ebe9c83~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<h1 data-id="heading-4">2.DDD入门</h1>
<p>我们先来看一张图：</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/b46525d17e244475930114caf33d725d~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer">
从最外层开始——什么是领域？大白话来说就是一系列问题的聚合。举个例子：</p>
<ul>
<li>电商平台中的电商域，你要解决的一系列问题有：
<ul>
<li>用户认证</li>
<li>移动收付</li>
<li>订单</li>
<li>报价</li>
<li>...</li>
</ul>
</li>
</ul>
<p>可以看到，域是呈现出来的是一系列的业务领域问题。</p>
<p>在不同域中，同一个数据实体的抽象形态往往是不同的。比如，Bookstore 应用中的书本，在销售领域中关注的是价格，在仓储领域中关注的是库存数量，在商品展示领域中关注的是书籍的介绍信息。</p>
<h2 data-id="heading-5">2.1 上下文边界</h2>
<p>往里面，我们应该看到的是限界上下文。其实这个翻译并不好，原文叫<code>bounded context</code>，叫做<strong>上下文边界</strong>更为妥当。本质上来说，它定义了边界。再具体点，即：用来封装通用语言和领域对象，提供上下文环境，保证在领域之内的一些术语、业务相关对象等（通用语言）有一个确切的含义，没有二义性。</p>
<h2 data-id="heading-6">2.2 聚合</h2>
<p>接下来，我们看到了聚合。<strong>聚合</strong>就是由业务和逻辑紧密关联的实体和值对象组合而成的，聚合是数据修改和持久化的基本单元，每一个聚合对应一个仓储，实现数据的持久化。</p>
<p>聚合有一个聚合根和上下文边界，这个边界根据业务单一职责和高内聚原则，定义了聚合内部应该包含哪些实体和值对象，而聚合之间的边界是松耦合的。按照这种方式设计出来的微服务很自然就是“高内聚、低耦合”的。</p>
<p>那聚合根是什么呢？</p>
<p>聚合根的主要目的是为了避免由于复杂数据模型缺少统一的业务规则控制，而导致聚合、实体之间数据不一致性的问题。</p>
<p>传统数据模型中的每一个实体都是对等的，如果任由实体进行无控制地调用和数据修改，很可能会导致实体之间数据逻辑的不一致。而如果采用锁的方式则会增加软件的复杂度，也会降低系统的性能。</p>
<p>如果把聚合比作组织，那聚合根就是这个组织的负责人。聚合根也称为根实体，它不仅是实体，还是聚合的管理者。</p>
<p>首先它作为实体本身，拥有实体的属性和业务行为，实现自身的业务逻辑。</p>
<p>其次它作为聚合的管理者，在聚合内部负责协调实体和值对象按照固定的业务规则协同完成共同的业务逻辑。</p>
<p>最后在聚合之间，它还是聚合对外的接口人，以聚合根 ID 关联的方式接受外部任务和请求，在上下文内实现聚合之间的业务协同。也就是说，聚合之间通过聚合根 ID 关联引用，如果需要访问其它聚合的实体，就要先访问聚合根，再导航到聚合内部实体，外部对象不能直接访问聚合内实体。</p>
<h2 data-id="heading-7">2.3 实体与值对象</h2>
<p>在 DDD 中有这样一类对象，它们拥有唯一标识符，且标识符在历经各种状态变更后仍能保持一致。对这些对象而言，重要的不是其属性，而是其延续性和标识，对象的延续性和标识会跨越甚至超出软件的生命周期。我们把这样的对象称为<strong>实体</strong>。其实很像数据库里自带不变id的一行行业务数据。</p>
<p>值对象相对不是那么重要，因为它是用来描述实体的一组属性集。很多系统中的实现会以json来实现，比如<a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.jianshu.com%2Fp%2F6b315deed5d4" target="_blank" rel="nofollow noopener noreferrer" title="https://www.jianshu.com/p/6b315deed5d4" ref="nofollow noopener noreferrer">【ZStack】7.标签系统</a>。</p>
<p>为了方便理解，这边做个小结。实体和值对象的目的都是抽象聚合若干属性以简化设计和沟通，有了这一层抽象，我们在使用人员实体时，不会产生歧义，在引用地址值对象时，不用列举其全部属性，在同一个限界上下文中，大幅降低误解、缩小偏差，两者的区别如下：</p>
<ol>
<li>两者都经过属性聚类形成，实体有唯一性，值对象没有。在本文案例的限界上下文中，人员有唯一性，一旦某个人员被系统纳入管理，它就被赋予了在事件、流程和操作中被唯一识别的能力，而值对象没有也不必具备唯一性。</li>
<li>实体着重唯一性和延续性，不在意属性的变化，属性全变了，它还是原来那个它；值对象着重描述性，对属性的变化很敏感，属性变了，它就不是那个它了（意味着不可变性，它可能是从外部查询来的）。</li>
<li>战略上的思考框架稳定不变，战术上的模型设计却灵活多变，实体和值对象也有可能随着系统业务关注点的不同而更换位置。比如，如果换一个特殊的限界上下文，这个上下文更关注地址，而不那么关注与这个地址产生联系的人员，那么就应该把地址设计成实体，而把人员设计成值对象。</li>
</ol>
<h1 data-id="heading-8">3. DDD上手</h1>
<h2 data-id="heading-9">3.1 从三层模型到DDD</h2>
<p>这里先简单介绍一下三层模型到DDD对应的一个变化。</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/212d6206e6544cffa6ce71361449f1d1~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer">
可以的看得出来，主要是对service进行了拆分。一般可以拆成三层：</p>
<ul>
<li>应用服务层：多个领域服务或外部应用服务进行封装、编排和组合，对外提供粗粒度的服务。应用服务主要实现服务组合和编排，是一段独立的业务逻辑。</li>
<li>领域服务层：由多个实体组合而成，一个方法可能会跨实体进行调用。在代码过于复杂的时候，可以将每个领域服务拆分为一个领域服务类，而不是将所有领域服务代码放到一个领域服务类中。</li>
<li>实体：是一个充血模型。同一个实体相关的逻辑都在实体类代码中实现。</li>
</ul>
<h2 data-id="heading-10">3.2 建模简介</h2>
<p>我们可以用三步来划定领域模型和微服务的边界。</p>
<ul>
<li>第一步：在事件风暴中梳理业务过程中的用户操作、事件以及外部依赖关系等，根据这些要素梳理出领域实体等领域对象。</li>
<li>第二步：根据领域实体之间的业务关联性，将业务紧密相关的实体进行组合形成聚合，同时确定聚合中的聚合根、值对象和实体。在第二章的图里，聚合之间的边界是第一层边界，它们在同一个微服务实例中运行，这个边界是逻辑边界，所以用虚线表示。</li>
<li>第三步：根据业务及语义边界等因素，将一个或者多个聚合划定在一个限界上下文内，形成领域模型。在上面的图里，限界上下文之间的边界是第二层边界，这一层边界可能就是未来微服务的边界，不同限界上下文内的领域逻辑被隔离在不同的微服务实例中运行，物理上相互隔离，所以是物理边界，边界之间用实线来表示。</li>
</ul>
<h2 data-id="heading-11">3.3 实践：设计一个MiniStack</h2>
<p>为了便于大家理解，我在这里会设计一个很简单的Iaas平台，并在里面代入最基本的DDD概念。</p>
<h3 data-id="heading-12">3.3.1 产品愿景</h3>
<ul>
<li>为了：企业的内部的开发者、运维人员</li>
<li>他们的：计算、存储、网络资源管理</li>
<li>这个：MiniStack</li>
<li>是一个：私有云平台</li>
<li>它可以：管理计算、存储、网络资源管理，帮用户简单快速的创建虚拟机</li>
<li>而不像：OpenStack</li>
<li>我们的产品：简单、健壮、智能</li>
</ul>
<p>串起来就是：为了满足企业的内部的开发者和运维人员，他们的硬件资源管理，我们建设里这个MiniStack，它是一个私有云平台，它可以管理计算、存储、网络资源管理，帮用户简单快速的创建虚拟机，而不像OpenStack，我们的产品简单、健壮、弹性。</p>
<h3 data-id="heading-13">3.3.2 场景分析</h3>
<p>因篇幅原因，我们来聊个最典型的场景——创建虚拟机，以便理出相关的领域模型。</p>
<p>在这里我们需要注意，我们要尽可能的梳理整个系统发生的操作、命令、领域时间以及依赖变化等。</p>
<h4 data-id="heading-14">3.3.2.1 创建虚拟机</h4>
<ol>
<li>用户登陆系统：从数据库中对信息进行校验，完成登陆认证</li>
<li>创建虚拟机：填写虚拟机名、集群、计算规格、L3网络以及镜像。如果需要的话（简单的体现），可以指定所在的物理机、以及网段。
<ul>
<li>VM服务需要提供创建虚拟机接口</li>
</ul>
</li>
<li>提交至MiniStack引擎，引起开始做相关调度：
<ol>
<li>寻找符合计算、存储资源的低负载物理机，并更新vm所属的物理机
<ul>
<li>物理机服务需要提供查询接口</li>
</ul>
</li>
<li>分配L3网络中的空闲IP，并更新vm相关的网络信息
<ul>
<li>网络服务需要提供IP分配接口</li>
</ul>
</li>
<li>告诉物理机agent：从镜像服务器拉取镜像到第1步寻找出的物理机
<ul>
<li>物理机服务需要提供拉取镜像接口</li>
</ul>
</li>
<li>告诉物理机agent启动参数，拉起vm
<ul>
<li>VM服务需要提供启动接口</li>
</ul>
</li>
</ol>
</li>
<li>界面上返回创建成功，用户可以看到vm</li>
</ol>
<p>但创建完虚拟机以后并不是就这么完事了，万一哪天这台物理机carsh了呢？哪天CPU因为奇怪的进程而打满了呢？因此为了我们的目标——智能，创建vm后，MiniStack每5分钟收集一系列的监控信息:</p>
<ol>
<li>向物理机agent发送心跳包，确保物理机状态正常</li>
<li>向虚拟机agent发送心跳包，并会返回：计算、存储、网络的相关状态</li>
</ol>
<h3 data-id="heading-15">3.3.3 宏观设计：领域建模</h3>
<p>在这一步，我们需要对业务进行分析，建立领域模型。一般步骤为：</p>
<ol>
<li>找出领域实体和值对象等领域对象</li>
<li>找出聚合根，根据实体、值对象与聚合根的依赖关系，建立聚合</li>
<li>第三步根据业务及语义边界等因素，定义限界上下文</li>
</ol>
<h4 data-id="heading-16">3.3.3.1 定义实体</h4>
<p>我们大致可以找出几个实体：</p>
<ul>
<li>虚拟机
<ul>
<li>启动</li>
<li>停止</li>
</ul>
</li>
<li>物理机的存储资源
<ul>
<li>查询</li>
<li>分配</li>
<li>释放</li>
</ul>
</li>
<li>物理机的计算资源
<ul>
<li>查询</li>
<li>分配</li>
<li>释放</li>
</ul>
</li>
<li>L3网络
<ul>
<li>分配IP</li>
</ul>
</li>
<li>镜像服务器
<ul>
<li>查询镜像</li>
<li>添加镜像</li>
<li>发布镜像</li>
</ul>
</li>
</ul>
<h4 data-id="heading-17">3.3.3.2 定义聚合与限界上下文</h4>
<p>在找聚合前，我们先要找出聚合根。可以分为物理机、网络、镜像服务器、虚拟机。而他们彼此都是独立的上下文，在需要的情况下，也可以拆成一个个微服务，如果是单体应用，则建议用模块手段进行逻辑隔离。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/8358eb44c66249a197ad76160daf40a5~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-18">3.3.4 微观：领域对象与代码结构分析</h3>
<p>当我们完成宏观上的建模后，便可以开始做微观的事：梳理微服务内的领域对象，梳理领域对象之间的关系，确定它们在代码模型和分层架构中的位置，建立领域模型与微服务模型的映射关系，以及服务之间的依赖关系。</p>
<p>大致上，分位两步：</p>
<ol>
<li>分析领域对象</li>
<li>设计代码结构</li>
</ol>
<h4 data-id="heading-19">3.3.4.1  分析领域对象</h4>
<p>在这一步，我们需要确认：</p>
<ul>
<li>服务的分层</li>
<li>应用服务由哪些服务组成</li>
<li>领域服务包含哪些实体和实体方法</li>
<li>哪个实体是聚合根</li>
<li>实体有哪些属性和方法</li>
<li>哪些对象为值对象</li>
</ul>
<p>由于我们的用例比较简单，整理如下：</p>
<ul>
<li>应用服务：
<ul>
<li>VM创建服务：负责创建VM，会调度大量的底层领域服务</li>
</ul>
</li>
<li>领域服务：VM服务、物理机服务、网络服务、镜像服务
<ul>
<li>VM服务：管理VM的生命周期，如创建、删除、启动、停止等</li>
<li>物理机服务：物理机相关服务，如添加、删除、状态变更、心跳感知、资源RUD等</li>
<li>网络服务：网络相关服务，如创建删除L2、L3网络，IP管理等</li>
<li>镜像服务：镜像服务器相关服务，如添加、删除、状态变更、增加镜像等</li>
</ul>
</li>
<li>实体：VM实体、物理机实体、本地存储实体（物理机存储）
<ul>
<li>VM实体：启动、停止等</li>
<li>物理机实体：状态变更、心跳感知等</li>
<li>L3实体：IP段添加、删除、IP分配、释放等</li>
<li>本地存储实体：存储的占用与释放</li>
</ul>
</li>
</ul>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/bf8995682af14349ad858ebe7976f6f2~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>接下来看一下聚合中的对象，我们把及格聚合根识别出来：</p>
<ul>
<li>物理机聚合的中的聚合根是物理机</li>
<li>网络聚合中的聚合根是L2网络</li>
<li>镜像聚合中的聚合根是镜像服务器</li>
<li>虚拟机聚合中的聚合根是虚拟机实体</li>
</ul>
<p>而上面提到的实体属性与方法我们已经在图中呈现出来了。</p>
<p>关于值对象，可以参考<a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.jianshu.com%2Fp%2F6b315deed5d4" target="_blank" rel="nofollow noopener noreferrer" title="https://www.jianshu.com/p/6b315deed5d4" ref="nofollow noopener noreferrer">【ZStack】7.标签系统</a>。该设计用于真实生产中。</p>
<h4 data-id="heading-20">3.3.4.2  设计代码结构</h4>
<p>当我们完成领域对象的分析后，我们便开始设计各领域对象在代码模型中的呈现方式了——即建立领域对象与代码对象的映射关系。根据这种映射关系，服务人员可以快速定位到业务逻辑所在的代码位置。</p>
<p>宏观上，我们可以参考以下分层模型：</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/e63ebaed28614876b62ec88e80e57f3d~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>微观实施上，我们可以参考<a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Falibaba%2FCOLA" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/alibaba/COLA" ref="nofollow noopener noreferrer">COLA</a>。</p>
<h1 data-id="heading-21">4.小结</h1>
<p>本文和大家一起捋了一遍DDD，并在文里“凭空的”设计了一个项目。其实这个项目并非凭空，我参考了以前参与的开源项目ZStack并对它做出了简化——该项目目前跑在大量的企业用户的私有云中，迭代已有6年多。因此无论从设计还是落地来说，都有一定的参考经验。</p>
<p>为了大家方便将文中的例子结合ZStack代码理解，我这边做了一个映射。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/f477c60411ba45ee86413c7215e2cb2d~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>当然，本篇的内容仅仅只能作为入门。并未深入相关概念，如：<code>子域</code>、<code>核心域</code>、<code>通用域</code>、<code>支撑域</code>、<code>领域事件</code>等；对于实战篇也仅仅设计了一个较为简单例子，并没有深究设计原则与架构演进路线。之后有机会的话，我会继续深入相关方向。</p>
<h2 data-id="heading-22">4.1 参考资料</h2>
<ul>
<li>关于ZStack的资料
<ul>
<li><a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.jianshu.com%2Fp%2F85a42b1c145c" target="_blank" rel="nofollow noopener noreferrer" title="https://www.jianshu.com/p/85a42b1c145c" ref="nofollow noopener noreferrer">【ZStack】4.进程内服务</a></li>
<li><a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.jianshu.com%2Fp%2F6b315deed5d4" target="_blank" rel="nofollow noopener noreferrer" title="https://www.jianshu.com/p/6b315deed5d4" ref="nofollow noopener noreferrer">【ZStack】7.标签系统</a></li>
<li><a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.jianshu.com%2Fp%2Fb83e469089f1" target="_blank" rel="nofollow noopener noreferrer" title="https://www.jianshu.com/p/b83e469089f1" ref="nofollow noopener noreferrer">【ZStack】9.查询API</a></li>
<li><a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.jianshu.com%2Fp%2Fffceecd2f990" target="_blank" rel="nofollow noopener noreferrer" title="https://www.jianshu.com/p/ffceecd2f990" ref="nofollow noopener noreferrer">ZStack源码剖析：如何在百万行代码中快速迭代</a></li>
<li><a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.jianshu.com%2Fp%2Ffa983d5b3f83" target="_blank" rel="nofollow noopener noreferrer" title="https://www.jianshu.com/p/fa983d5b3f83" ref="nofollow noopener noreferrer">ZStack源码剖析之设计模式鉴赏——三驾马车</a></li>
<li><a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fzstackio%2Fzstack" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/zstackio/zstack" ref="nofollow noopener noreferrer">ZStack Github Repo</a></li>
</ul>
</li>
<li>虽然ZStack是个值得参考的项目，但其DDD的设计并不是特别明显。因此在项目分层上也可以参考<a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Falibaba%2FCOLA" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/alibaba/COLA" ref="nofollow noopener noreferrer">COLA</a></li>
<li>《领域驱动设计》</li>
<li>极客时间——DDD实战课</li>
</ul></div>  
</div>
            