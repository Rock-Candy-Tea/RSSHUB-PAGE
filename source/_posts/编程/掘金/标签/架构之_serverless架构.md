
---
title: '架构之_serverless架构'
categories: 
 - 编程
 - 掘金
 - 标签
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/e17d29e0647e4df3b5197a2a05f8f924~tplv-k3u1fbpfcp-zoom-1.image'
author: 掘金
comments: false
date: Mon, 12 Jul 2021 17:12:50 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/e17d29e0647e4df3b5197a2a05f8f924~tplv-k3u1fbpfcp-zoom-1.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h1 data-id="heading-0">简介</h1>
<p>不知道什么时候，出现了一个叫做Serverless架构的模式，看这个英语单词Serverless，也就是没有服务的意思。没有服务怎么搭建应用程序呢？</p>
<p>后来仔细研究了一下，发现Serverless并不是说不需要服务，而是将服务搭建在BaaS或者FaaS平台上的。通常适用于单页应用程序或者业务逻辑并不负责的程序。</p>
<p>很明显这个serverless架构是云厂商想出来的，目的就是要让你用他们的服务。这个跟最近比较流行的cloud native有异曲同工之妙。</p>
<p>此类架构虽然消除了对传统架构中搭建服务的需求，可能会受益于显着降低的运营成本、复杂性和工程交付时间，但代价是增加对供应商的依赖和相对不成熟的支持服务。</p>
<p>本文将会详细讨论一下serverless和它背后的故事。</p>
<h1 data-id="heading-1">什么是serverless</h1>
<p>serverless的概念毫无疑问是云厂商提出来的，诸如微软，谷歌，亚马逊都是serverless的推崇者，并且在他们提供的服务中进行深度绑定和推荐。</p>
<p>那么什么是serverless呢？</p>
<p>serverless其实可以描述两种状态。第一种状态就是那些富客户端，对于富客户端来说业务逻辑都可以在客户端完成，在云端只需要用到数据库服务或者身份验证服务即可，这些类型的服务被称为BaaS。</p>
<p>还有一种就是服务器端逻辑仍由应用程序开发人员编写，但与传统架构不同，它运行在无状态计算容器中，这些容器是事件触发的、短暂的（可能只持续一次调用），并完全由第三方来调用。这种服务被称为功能即服务或FaaS。最有名的就是现在比较火的云上的Lambda服务了。</p>
<h1 data-id="heading-2">serverless的例子</h1>
<h2 data-id="heading-3">简单的三层服务</h2>
<p>接下来我们来举几个具体可以使用到serverless的例子，方便大家的理解。</p>
<p>考虑一个最最常见的web项目，提供了增删改查的功能。很明显，我们需要一个客户端，一个服务器端和一个数据库，如下图所示：</p>
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/e17d29e0647e4df3b5197a2a05f8f924~tplv-k3u1fbpfcp-zoom-1.image" loading="lazy" referrerpolicy="no-referrer">
<p>上图是一个最简单的服务的例子，我们有一个客户端用来展示对应的UI界面，一般来说这个客户端就是浏览器。还有一个服务端用来接收所有的客户端请求和业务逻辑处理。最后有一个数据库用来存储对应的数据。</p>
<p>如果将上面的服务转换成为serverless架构，该如何修改呢？</p>
<p>在serverless架构中，服务端没有了，转而被各种FaaS所替代。然后客户端的功能会被增强，变成富客户端，大部分的业务逻辑都会在客户端进行，甚至在某些情况下可以直接从客户端读取数据库。</p>
<p>必须使用到FaaS服务的业务逻辑需要被拆分，如下图所示：</p>
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/1549a5e7b6fd4c8db4e2e4a8d5c6cbe3~tplv-k3u1fbpfcp-zoom-1.image" loading="lazy" referrerpolicy="no-referrer">
<p>上图中，我们使用了第三方的云认证服务来进行安全认证。同时对于不重要的数据可以直接授权客户端进行数据库的查询。</p>
<p>对于更新服务，还是需要借助于FaaS提供的更新API来对数据库进行更新。</p>
<p>可以看到，Serverless的架构已经和原来的架构完全不同了。带来的好处就是系统变得更加灵活，并且对功能重新做了划分，减少了服务端的业务逻辑，有点分布式的效果，对应的服务器成本更低。</p>
<p>缺点就是原来的一个服务被拆分成为了多个服务，需要对多个服务进行监控，然后基本上所有的数据都存放在云端，那么对服务提供商的安全能力提出了更高的要求。最后，这种灵活性和成本的减少会带来系统的复杂性，增加了维护的难度。</p>
<h2 data-id="heading-4">消息驱动</h2>
<p>一个常见的消息驱动的例子就是前端的点击流上报。当用户在客户端点击某个按钮之后，会去调用服务端的某个接口。这个接口会将点击消息发送到消息队列中，然后再启用异步的后端服务从消息队列中拿取消息，最后更新数据库。</p>
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/c9ded9f37a9345488e8d26c942b9fe8e~tplv-k3u1fbpfcp-zoom-1.image" loading="lazy" referrerpolicy="no-referrer">
<p>那么上面的例子如果用Serverless该怎么实现呢？</p>
<p>我们需要将服务端替换成FaaS，并且将异步服务也替换成对应的FaaS：</p>
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/7470559f5926411193df057c925992ea~tplv-k3u1fbpfcp-zoom-1.image" loading="lazy" referrerpolicy="no-referrer">
<p>这里的好处是可以借助FaaS的快速拓展功能，在消息数量比较多的情况下，可以动态扩展消息处理函数，从而提升系统的处理速度。</p>
<h1 data-id="heading-5">FaaS</h1>
<p>上面我们提到了很多次FaaS，那么FaaS到底是什么呢？</p>
<p>按照它的英文原意，FaaS就是函数作为服务。或者你可以看做是亚马逊的  AWS Lambda 服务。</p>
<p>AWS Lambda 可以不需要任何服务器就可以运行，只需要上传你的业务代码，就可以自动生成一个Lambda服务。然后这个服务就可以供外部调用。</p>
<blockquote>
<p>当然，这里的不需要服务器是指客户不需要自己购买服务器和在上面搭建服务，事实上lambda也是需要在服务器上运行的。</p>
</blockquote>
<p>FaaS 基本上可以兼容Javascript、Python、Go和任何jvm语言编写的代码，只需要做少许更改即可重新生成为FaaS服务。</p>
<p>FaaS的另外一个优点就是可以水平扩展，并且这个水平扩展是完全自动的。这个水平扩展自动管理是由运营商来控制的，用户不需要考虑到实现的底层细节。这种水平扩展能力对于服务在某个时刻的峰值应用是非常有效的。</p>
<p>我们只需要设计好FaaS函数，剩下的一切都交给云厂商去做即可。</p>
<h2 data-id="heading-6">FaaS的缺点</h2>
<p>FaaS是无状态的，也就是说你不能够使用本地内存变量或者本地磁盘的数据，因为FaaS不能保证这些数据的有效性和持久性。</p>
<p>所以需要对要存储的数据进行外部持久化。</p>
<p>另外，由于云服务器的限制，每次FaaS的调用都有一个最长超时时间，所以FaaS只适合那些能够快速响应的程序。</p>
<p>另外，FaaS在启动的时候可能需要初始化，这种函数的实例化可能会带来请求的延迟。所以需要考虑云提供商的启动策略，并作出相应的调整。</p>
<p>当我们决定使用任何外包策略时，您都将部分系统的控制权交给第三方供应商。这种缺乏控制可能表现为系统停机、意外限制、成本变化、功能丢失、强制 API 升级等。</p>
<ul>
<li>多租户问题</li>
</ul>
<p>多租户是指多个不同客户（或租户）的多个软件实例在同一台机器上运行的情况，并且可能在同一托管应用程序中运行。这是一种云服务商实现规模经济效益的策略。服务供应商尽最大努力让客户觉得他们每个人都是唯一使用他们系统的人，但是，没有一个完美的方案能够同时解决多租户的安全性（一个客户能够看到另一个客户的数据）、健壮性（一个客户的软件中的错误导致另一个客户的软件出现故障）和性能（一个高负载的客户）等方面的问题。</p>
<ul>
<li>供应商绑定</li>
</ul>
<p>如果你在一个服务商使用了serverless,那么将其切换到另外一个供应商的成本是巨大的。可能需要更新对应的运营工具，还可能需要更新代码。</p>
<h2 data-id="heading-7">FaaS的优点</h2>
<p>我们可以把Serverless看做是最简单的外包解决方案，你不需要自己管理服务器和数据库，这些都可以托管给云厂商。</p>
<p>一方面，基础设施服务的投入变少了，另外一方面，可以节约维护这些基础设施的人力成本。</p>
<p>另外，您对代码进行的任何性能优化不仅会提高应用程序的速度，而且它们将与降低运营成本有直接或者间接的联系，具体取决于服务供应商的收费方案。例如，假设一个应用程序最初需要一秒钟来处理一个事件。如果通过代码优化将这一时间减少到 200 毫秒，将立即看到计算成本节省 80%，而无需进行任何基础架构更改。</p>
<p>与部署整个服务器相比，打包和部署 FaaS 功能很简单。您所做的就是将所有代码打包成一个 zip 文件，然后上传。</p>
<h1 data-id="heading-8">总结</h1>
<p>serverless架构是目前比较热门的一种架构方式，我们可以去尝试使用这种新的架构方式，来看看能否给我们的业务带来不同的变化。但是也需要看到并不是所有的服务都可以使用serverless架构。我们需要对其进行权衡。</p>
<blockquote>
<p>本文已收录于 <a href="https://link.juejin.cn/?target=http%3A%2F%2Fwww.flydean.com%2F11-serverless-architecture%2F" target="_blank" rel="nofollow noopener noreferrer" title="http://www.flydean.com/11-serverless-architecture/" ref="nofollow noopener noreferrer">www.flydean.com/11-serverle…</a></p>
<p>最通俗的解读，最深刻的干货，最简洁的教程，众多你不知道的小技巧等你来发现！</p>
</blockquote></div>  
</div>
            