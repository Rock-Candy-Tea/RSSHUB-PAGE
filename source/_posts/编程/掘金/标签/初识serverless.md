
---
title: '初识serverless'
categories: 
 - 编程
 - 掘金
 - 标签
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/9ddfc30102e843618cac4c7e5e19eb22~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Sun, 16 May 2021 23:26:59 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/9ddfc30102e843618cac4c7e5e19eb22~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h1 data-id="heading-0">前言</h1>
<p>serverless 也是刚兴起没多久，偶然一次机会让我在技术网站上看到serverless，觉得它的概念挺好 ，Serverless意味无维护，不是完全去除服务器，而是使用公共云资源，这样就无需对服务器运行状态进行关心和担心，它们是否在工作，应用是否跑起来正常运行等等。Serverless代表的是你不要关心运营维护问题。serverless 的内涵就是对全部底层资源和运维工作的封装，让开发者更专注于业务逻辑，显然它的技术前景非常好，所以我想我们也需要去了解和关注它，毕竟这个东西对前端来说简直是棒极了，这也是我们前端开发者一波前所未有的机遇，享受一下云开发的乐趣， 而且对于体量小的应用他基本上没什么消耗。</p>
<h1 data-id="heading-1">一、serverless的概念和特点</h1>
<p>serverless是一个比较抽象的概念，因为它蕴含的信息量很大， serverless深刻的体现了现代化的云的概念，这里我要给大家总结的含义有两种：</p>
<ol>
<li>
<p>狭义 Serverless（最常见）= Serverless computing 架构 = FaaS 架构 = Trigger（事件驱动）+ FaaS（函数即服务）+ BaaS（后端即服务，持久化或第三方服务）= FaaS + BaaS。</p>
</li>
<li>
<p>广义 Serverless = 服务端免运维 = 具备 Serverless 特性的云服务</p>
</li>
</ol>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/9ddfc30102e843618cac4c7e5e19eb22~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer">
其实简单点说，Serverless（无服务器架构）是指服务端逻辑由开发者实现，运行在无状态的计算容器中，由事件触发，完全被第三方管理，其业务层面的状态则存储在数据库或其他介质中。（相比现在传统模式的应用），它的主要特点有四点：</p>
<ol>
<li>
<p>事件驱动----函数在 FaaS 平台中，需要通过一系列的事件来驱动函数执行；</p>
</li>
<li>
<p>无状态----因为每次函数执行，可能使用的都是不同的容器，无法进行内存或数据共享。如果要共享数据，则只能通过第三方服务；</p>
</li>
<li>
<p>无运维----使用serverless我们不需要关心服务器，也不需要关心运维，这也是serverless思想的核心；</p>
</li>
<li>
<p>低成本----使用 Serverless 成本很低，因为我们只需要为每次函数的运行付费。函数不运行，则不花钱，也不会浪费服务器资源过度;</p>
</li>
<li>
<p>自动弹性伸缩---针对业务的实际事件或请求数，云函数自动弹性合适的处理实例来承载实际业务量，在没有事件或请求时，无实例运行，不占用资源。</p>
</li>
</ol>
<h2 data-id="heading-2">Serverless常见的服务商和解决方案</h2>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/682100ce0bc7446480d76a2468985571~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer">
目前这里面我只用腾讯云的serverless框架简单的构建过应用和简单操作过阿里云的fun命令行工具，还在阿里云官网简单使用了函数计算，享受了一把快速构建部署serverless的应用的快感、小程序应用层的云开发也是利用了serverless的概念，对于简单的学习这种开发模式我想大概也够了，最实用的一点就是平常自己玩点东西的话这个真的是省钱还省力。 从下图对比可以看出各个服务商提供服务的价位。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/31a7949b8e184cbd939ed49f459f6f9a~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-3">Serverless的应用场景</h2>
<p>其实讲了一些serverless的优势和特点，但是我想大家最关注的点就是它的应用场景吧，这种模式下适合的场景有哪些呢？</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/eadcadc8de7649d88ec56393c809472b~tplv-k3u1fbpfcp-watermark.image" alt="111.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>我这只是列了一些平常实用的一些场景我做了demo的场景serverless的使用场景还有很多， 后边serverless实战章节通过代码演示具体是怎么运行的。</p>
<h1 data-id="heading-4">FaaS和BaaS</h1>
<p>FaaS，函数即服务，它还有个名字叫作 Serverless Computing，它可以让我们随时随地创建、使用、销毁一个函数。</p>
<p>你可以想一下通常函数的使用过程：它需要先从代码加载到内存，也就是实例化，然后被其它函数调用时执行。在 FaaS 中也是一样的，函数需要实例化，然后被触发器 Trigger 或者被其他的函数调用。二者最大的区别就是在 Runtime，也就是函数的上下文，函数执行时的语境。</p>
<p>FaaS 的 Runtime 是预先设置好的，Runtime 里面加载的函数和资源都是云服务商提供的，我们可以使用却无法控制。你可以理解为 FaaS 的 Runtime 是临时的，函数调用完后，这个临时 Runtime 和函数一起销毁。
FaaS 的函数调用完后，云服务商会销毁实例，回收资源，所以 FaaS 推荐无状态的函数。对于前端工程师来说，这可能很好理解，就是函数不可改变 Immutable。简单解释一下，就是说一个函数只要参数固定，返回的结果也必须是固定的。</p>
<p>MVC 架构里面，一个 HTTP 的数据请求，就会对应一个 Control 函数，我们完全可以用 FaaS 函数来代替 Control 函数。在 HTTP 的数据请求量大的时候，FaaS 函数会自动扩容多实例同时运行；在 HTTP 的数据请求量小时，又会自动缩容；当没有 HTTP 数据请求时，还会缩容到 0 实例，节省开支。</p>
<h2 data-id="heading-5">FaaS 是如何运行的</h2>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/3135bccb52d94360b04f20d916f70273~tplv-k3u1fbpfcp-watermark.image" alt="22.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/3135bccb52d94360b04f20d916f70273~tplv-k3u1fbpfcp-watermark.image" alt="33.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-6">FaaS最大的优势在哪里</h2>
<p>其实，<strong>FaaS</strong> 与应用托管 PaaS 平台对比，最大的区别在于资源利用率，这也是 <strong>FaaS</strong> 最大的创新点。FaaS 的应用实例可以缩容到 0，而应用托管 <strong>PaaS</strong> 平台则至少要维持 1 台服务器或容器。就是一种新的运行代码的托管环境。
在上面“Hello World”例子中，函数在第一次调用之前，实际的服务器占用为 0。因为直到用户第一次 HTTP 数据请求过来时，函数服务才被 HTTP 事件触发，启动函数实例。也就是说没有用户请求时，函数服务没有任何的函数实例，也就不占用任何的服务器资源。而应用托管 <strong>PaaS</strong> 平台，创建应用实例的过程通常需要几十秒，为了保证你的服务可用性，必须一直维持着至少一台服务器运行你的应用实例，但是<strong>FaaS</strong>就像一个声控灯，有人时他可以很快亮起来，没人时又可以关着，最关键的一点是<strong>FaaS</strong>的极速启动的特性，冷启动是指在函数调用链路中包含了代码下载、启动函数实例容器、运行时初始化、用户代码初始化等环节</p>
<p>总结来说，<strong>FaaS</strong>的特性主要有三点：</p>
<ol>
<li>
<p>纯 <strong>FaaS</strong> 应用调用链路由函数触发器、函数服务和函数代码三部分组成，它们分别替代了传统服务端运维的负载均衡 & 反向代理，服务器 & 应用运行环境，应用代码部署</p>
</li>
<li>
<p>对比传统应用托管 <strong>PaaS</strong> 平台，FaaS 应用最大的不同就是，<strong>FaaS</strong> 应用可以缩容到 0，在事件到来时极速启动，Node.js 的函数甚至可以做到 100ms 启动并执行</p>
</li>
<li>
<p><strong>FaaS</strong> 在设计上牺牲了用户的可控性和应用场景，来简化代码模型，并且通过分层结构进一步提升资源的利用率，这也是为什么 <strong>FaaS</strong> 冷启动时间能这么短的主要原因。关于 <strong>FaaS</strong> 的 3 层结构，你可以这么想象：容器层就像是 Windows 操作系统；Runtime 就像是 Windows 里面的播放器暴风影音；你的代码就像是放在 U 盘里的电影。</p>
</li>
</ol>
<h2 data-id="heading-7">BaaS（Backend as a Service）</h2>
<p>BaaS 其实是一个集合，是指具备高可用性和弹性，而且免运维的后端服务，MVC 架构中的 Model 层，就需要我们用 BaaS 来解决。用公共服务替我们管理数据，而serverless的理念就是一切皆服务。我初步觉得就是使大家更近一步接触后端。一般是一个个的 API 调用后端或别人已经实现好的程序逻辑，比如身份验证服务 Auth0，这些 BaaS 通常会用来管理数据，云服务商提供的云数据库，还有各种其它数据库和存储服务。它有两种模式，一种是API模式，让开发者自己拓展代码；另一种是SDK模式，阿里云oss存储的官方sdk，还有高德...</p></div>  
</div>
            