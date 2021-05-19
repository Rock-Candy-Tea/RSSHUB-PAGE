
---
title: 'ZStack源码剖析：如何在百万行代码中快速迭代'
categories: 
 - 编程
 - 掘金
 - 标签
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/ff68d12016ae4160908647efa8aef39e~tplv-k3u1fbpfcp-zoom-1.image'
author: 掘金
comments: false
date: Tue, 18 May 2021 07:01:43 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/ff68d12016ae4160908647efa8aef39e~tplv-k3u1fbpfcp-zoom-1.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><blockquote>
<p>本文首发于泊浮目的专栏：<a href="https://segmentfault.com/blog/camile" target="_blank" rel="nofollow noopener noreferrer">segmentfault.com/blog/camile</a></p>
</blockquote>
<h1 data-id="heading-0">前言</h1>
<p>ZStack是下一代开源的云计算IaaS（基础架构即服务）软件。它主要面向的是未来的智能数据中心，通过提供的API来管理包括计算、存储和网络在内的数据中心的各种资源。跟OpenStack相比，ZStack具有易用、稳定、灵活、超高性能等特点。其单管理节点可以管理1万台物理机规模集群，多个管理节点构建的集群可以做到使用一个数据库、一套消息总线管理10万台物理机、数百万个虚拟机节点、并发处理数万个API。</p>
<blockquote>
<p>以下是ZStackV2.2的服务架构图</p>
</blockquote>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/ff68d12016ae4160908647efa8aef39e~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<blockquote>
<p>官网地址：<a href="http://www.zstack.io/" target="_blank" rel="nofollow noopener noreferrer">www.zstack.io/</a></p>
</blockquote>
<blockquote>
<p>核心开源引擎ZStack GitHub：<a href="https://github.com/zstackio/zstack" target="_blank" rel="nofollow noopener noreferrer">github.com/zstackio/zs…</a></p>
</blockquote>
<blockquote>
<p>ZStack-Utility GitHub：<a href="https://github.com/zstackio/zstack-utility" target="_blank" rel="nofollow noopener noreferrer">github.com/zstackio/zs…</a></p>
</blockquote>
<blockquote>
<p>阅读源码如果不想使用IDE，建议配合<a href="https://github.com/buunguyen/octotree%E6%9B%B4%E4%BD%B3%E3%80%82" target="_blank" rel="nofollow noopener noreferrer">github.com/buunguyen/o…</a></p>
</blockquote>
<p>本文将对核心引擎-ZStack的源码进行剖析。在ZStack官网上我们可以看到其每个版本的发布都是携带了许多的新特性。在笔者看来，能够快速迭代的原因首先是来自于每位工程师的辛勤付出。除此之外，因其还有些软件工程领域中沉淀下来的最佳实践：</p>
<ul>
<li>良好的架构设计</li>
<li>覆盖较为全面的测试</li>
<li>恰当好处的使用设计模式</li>
</ul>
<h1 data-id="heading-1">良好的架构设计</h1>
<h2 data-id="heading-2">异步架构</h2>
<p>Iaas的核心应该做的是管控层，而不是数据层。故ZStack仅仅也是做出一些“决策”而已——在设计系统的时候，应不考虑在这些决策的执行上消耗大量的资源。在面对大量请求或者“决策”的时候，如果使用多线程来处理阻塞式IO模型时会遇到一些问题：</p>
<ul>
<li>阻塞模型的吞吐量受到线程池大小的限制；</li>
<li>创建并使用许多线程会耗费额外的时间用于上下文切换，影响系统性能。</li>
</ul>
<p>而非阻塞、异步的消息驱动系统可以只运行少量的线程，并且不阻塞这些线程，只在需要计算资源时才使用它们。这大大提高了系统的响应速度，并且能够更高效地利用系统资源。</p>
<p>故，ZStack采用了异步架构，分别由三个部分组成：</p>
<ul>
<li>异步消息</li>
<li>异步方法</li>
<li>异步HTTP 请求</li>
</ul>
<p>如果在系统中的一部分采用异步设计，是不行的。这样还是会因为同步而没法享受异步带来的“福利”。故此整个系统都得采用异步架构。</p>
<ul>
<li><strong>相对的，开发者们在编写异步代码的时候得格外小心。</strong></li>
<li><strong>在系统设计中，异步调用可以减少系统在IO上出现瓶颈的可能性。</strong></li>
</ul>
<blockquote>
<p>扩展链接 : <a href="https://mp.weixin.qq.com/s?__biz=MzI0NTc4MzE4Mw==&mid=100000033&idx=1&sn=1a0389051572055b7bb9a23f2acb5e21&chksm=69480ec15e3f87d77287374f53c2dc090583267886d61890cc55f390584e052b8b916e4610d1&scene=18#rd" target="_blank" rel="nofollow noopener noreferrer">ZStack--可拓展性的秘密武器1：异步架构</a></p>
</blockquote>
<h2 data-id="heading-3">无状态服务</h2>
<p>在<code>ZStack</code>中，每一个服务都是独立存在的。为了方便的管理更多的物理机，<code>ZStack</code>推荐采用集群部署MN。但这样就会遇到一个问题，不同MN下面有着不同的几个服务存在，在这里我们设其为X个服务。在10个MN部署的情况下，可能就是10X个服务。那么在一个资源需要操作时，我需要发送向对应的MN。那么如何找到那个MN呢？最直观的想法就是在各个MN中保存相应的“服务表”，这即是一种状态。那么在分布式系统中，采用有状态的服务绝对不是一个好的选择，它会严重影响系统的扩展性。<code>ZStack</code>巧妙的采用了一致性哈希算法+MQ解决了这个问题。</p>
<ul>
<li><strong>这在系统设计中实为是一种使用一致性hash技术的负载均衡</strong></li>
</ul>
<blockquote>
<p>扩展链接：<a href="https://mp.weixin.qq.com/s?__biz=MzI0NTc4MzE4Mw==&mid=100000033&idx=2&sn=18c269f0108b0d39d46cd89e48fdf5a1&chksm=69480ec15e3f87d7f2964a5e1c2d8fc54a094a677794bfd3c50783d83556d66ab57e75040877&scene=18#rd" target="_blank" rel="nofollow noopener noreferrer">ZStack—可拓展性秘密武器2：无状态的服务</a></p>
</blockquote>
<h2 data-id="heading-4">无锁架构</h2>
<p>解决并发的问题不一定要用显式的锁，也可以对同一资源做操作的任务做成队列使其串行执行。</p>
<blockquote>
<p>注意：并发 != 并行
扩展链接：<a href="https://mp.weixin.qq.com/s?__biz=MzI0NTc4MzE4Mw==&mid=100000033&idx=3&sn=9006182bc8c8992e4771a48061d4481b&chksm=69480ec15e3f87d71612f560c258fc8bb6f092d142bd72cdf38d11d0c10b0a682a9a637b2fcf&scene=18#rd" target="_blank" rel="nofollow noopener noreferrer">ZStack--可拓展性秘密武器3：无锁架构</a></p>
</blockquote>
<h2 data-id="heading-5">松耦合架构</h2>
<h3 data-id="heading-6">项目模块化</h3>
<p>在<code>Intellij</code>中打开ZStack的代码，会发现大多数目录底下都会有一个<code>pom.xml</code>文件，ZStack采用了模块化项目。模块化的好处在工程实践中不言而喻的，比如：</p>
<ul>
<li>可以在不影响整个系统的情况下替换某个模块</li>
<li>开发者只要专心的在自己的模块中工作即可</li>
<li>减少系统耦合度，提高内聚，减少资源循环依赖，增强系统框架设计</li>
<li>...</li>
</ul>
<p>下面来看一下<code>ZStack</code>中代码的结构：</p>
<h4 data-id="heading-7">代码结构</h4>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/9cc1e6b922764353926f9cce5b6c8845~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<blockquote>
<p>截图于2017.9.22</p>
</blockquote>





























































<table><thead><tr><th align="left">名称</th><th align="left">简介</th></tr></thead><tbody><tr><td align="left">build</td><td align="left">用于Java部分的编译、打包、部署等</td></tr><tr><td align="left">conf</td><td align="left">配置文件及SQL文件的放置;Spring Service配置存放;持久化文件配置</td></tr><tr><td align="left">core</td><td align="left">核心模块。实现系统的核心功能——包括数据库、消息总线、工作流实现等等</td></tr><tr><td align="left">coregroovy</td><td align="left">ZStack的最新测试采用了Groovy，这里是对测试库做的支持</td></tr><tr><td align="left">header</td><td align="left">消息以及Entity的定义</td></tr><tr><td align="left">plugin</td><td align="left">顾名思义。其中不少组件都以插件化开发，提供较高的灵活性</td></tr><tr><td align="left">sdk</td><td align="left">测试库使用的SDK</td></tr><tr><td align="left">simulator</td><td align="left">对于测试库支持的又一模块，主要用户simulator agent的行为</td></tr><tr><td align="left">testlib</td><td align="left">测试库</td></tr><tr><td align="left">test</td><td align="left">测试模块</td></tr><tr><td align="left">工具类</td><td align="left">工具包。目前仅仅支持了doc生成</td></tr><tr><td align="left">utils</td><td align="left">代码中使用的工具类</td></tr><tr><td align="left">其他</td><td align="left">功能实现模块</td></tr></tbody></table>
<h3 data-id="heading-8">通过MQ来解耦合</h3>
<p>在<code>ZStack</code>中，每个功能实现模块都会被称为<strong>服务</strong>——一个独立的服务。各个服务之间的通信由MQ来承担。这就像是传统的CSE，C和E是不耦合的，通过S来交互。同样的，一个服务需要向另一个服务发起调用，只需往消息总线发送消息，并指定这个服务ID（Service ID）即可。如果某个服务的代码需要大量重构或者做成<strong>微服务</strong>，只要提供相同的服务并注册到MQ上就可以了。这就是事件驱动架构（Event Driven Architecture）的一种典型实现。</p>
<blockquote>
<p>CSE：Controller、Service、Entity。注：称作Domain或者Model都是不专业的。Domain是一个领域对象，往往我们再做传统Java软件web开发中，这些Domain都是贫血模型，是没有行为的，或是没有足够的领域模型的行为的，所以，以这个理论来讲，这些Domain都应该是一个普通的entity对象，并非领域对象，所以请把包名改为:com.xxx.entity。</p>
</blockquote>
<p>**举个简单明了的例子。**如果每个对象的行为都是通过消息来决定的（比如一个方法需要message得到回复后才能do something...），那么这个对象仅仅对消息总线产生了依赖。在测试中，将会发挥巨大的威力——我们只需要改变handle message处的行为，就可以使一个对象行为做出相应的变化。这样可以使mock的单位变得更小，同时也可以变得更加灵活。</p>
<p>试想如果通过函数调用：</p>
<pre><code class="hljs language-java copyable" lang="java"><span class="hljs-comment">//方法a中的代码</span>
xxService.method1();
xx2Service.method2();
<span class="copy-code-btn">复制代码</span></code></pre>
<p>在测试中该如何解耦？但如果通过MQ——即一个消息来调用<code>xxService.method1()</code>，那么方法a对xxService就没有了直接的依赖。</p>
<h3 data-id="heading-9">使用Spring</h3>
<blockquote>
<p>不了解Spring的人可以看：<a href="https://segmentfault.com/a/1190000008834535" target="_blank" rel="nofollow noopener noreferrer">看起来很长但还是有用的Spring学习笔记</a></p>
</blockquote>
<p>在代码中，每当我们New出一个对象时，这个模块便对这个对象产生了依赖。当我们需要测试的时候就不得不去Mock它。当依赖的对象or Field 有成千上万个的时候，这就是一场灾难了。代码变得愈发不可测，坑就越多，开发者在扩展or维护项目的时候就会愈发的乏力。这就像是我们之前提到的MQ，<code>服务1->MQ->服务2</code>，由于中间隔了一个MQ，于是服务1和服务2没有必然的关系。同样的，从<code>对象1->调用->对象2</code>到<code>对象1->调用->Spring提供的IOC容器->对象2</code>，这样使对象与对象之间也没有了直接调用关系，对象1只要知道它要调用的对象实现了其需要的<code>Interface</code>就是可以调用的。</p>
<p>除了<code>Autowired</code>的正确使用姿势。在ZStack中，还有一类很有意思的代码，一般称之为<code>xxxExtensionPoint</code>。其本质就是定义一个接口，然后其实现类作为Bean通过XML注册到IOC中。在需要使用的时候，通过Spring获取到所有实现该接口的对象，调用其函数。这样就会使代码变得非常的灵活。</p>
<p>例如，<code>ZStack</code>分为多个版本——开源版、企业版、混合云版等。如果一个服务在不同版本中的处理逻辑需要稍许不同，那么就可以在开源版的代码中注册一个接口，在另一个版本的服务中实现该接口。这样也不会影响到开源版的原有逻辑。从模块上看我们代码的是松耦合并且无法直接调用的，但是在内存中，却是可以调用得到的。</p>
<h1 data-id="heading-10">覆盖较为全面的测试</h1>
<p>在<code>ZStack</code>中</p>
<ul>
<li>开发者Fix每一个Bug都是需要补充相应的Case；</li>
<li>每一个Feature在进去之前更会由开发工程师与QA工程师同时制定测试场景并Cover；</li>
<li>每一个PR（pull request）进去之前都会通过PR系统跑过所有的Case，以防止Bug的Regression；</li>
</ul>
<p>由于<code>ZStack</code>源码做到了一定的解耦合（上述提到）与无状态，使得集成测试得以进行。</p>
<blockquote>
<p>其首席架构师Frank.Zhang曾说过：我们开发者在写代码的时候往往就应该考虑该怎么写测试了。</p>
</blockquote>
<blockquote>
<p>想了解ZStack的测试框架，可以看： <a href="https://github.com/zstackio/zstack/wiki/%E7%AE%A1%E7%90%86%E8%8A%82%E7%82%B9%E5%9F%BA%E4%BA%8E%E6%A8%A1%E6%8B%9F%E5%99%A8%E7%9A%84Integration-Test%E6%A1%86%E6%9E%B6" target="_blank" rel="nofollow noopener noreferrer">ZStack WiKi ：管理节点基于模拟器的Integration Test框架</a></p>
</blockquote>
<h1 data-id="heading-11">恰当好处的使用设计模式</h1>
<p>在<code>ZStack</code>中，设计模式有较为良好的实践。笔者有机会将会在之后的<a href="https://segmentfault.com/bookmark/1230000011444285" target="_blank" rel="nofollow noopener noreferrer">系列文章</a>分析其中的典型案例以及在代码中使用极其频繁的核心工具。</p></div>  
</div>
            