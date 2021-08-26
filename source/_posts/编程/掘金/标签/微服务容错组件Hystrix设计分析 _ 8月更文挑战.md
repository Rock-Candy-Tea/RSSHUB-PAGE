
---
title: '微服务容错组件Hystrix设计分析 _ 8月更文挑战'
categories: 
 - 编程
 - 掘金
 - 标签
headimg: 'https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/75a23c424a884d1e80cb1be35b0e81f0~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Wed, 25 Aug 2021 15:39:47 GMT
thumbnail: 'https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/75a23c424a884d1e80cb1be35b0e81f0~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;color:#595959;font-size:15px;font-family:-apple-system,system-ui,BlinkMacSystemFont,Helvetica Neue,PingFang SC,Hiragino Sans GB,Microsoft YaHei,Arial,sans-serif;background-image:linear-gradient(90deg,rgba(60,10,30,.04) 3%,transparent 0),linear-gradient(1turn,rgba(60,10,30,.04) 3%,transparent 0);background-size:20px 20px;background-position:50%&#125;.markdown-body p&#123;color:#595959;font-size:15px;line-height:2;font-weight:400&#125;.markdown-body p+p&#123;margin-top:16px&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;padding:30px 0;margin:0;color:#135ce0&#125;.markdown-body h1&#123;position:relative;text-align:center;font-size:22px;margin:50px 0&#125;.markdown-body h1:before&#123;position:absolute;content:"";top:-10px;left:50%;width:32px;height:32px;transform:translateX(-50%);background-size:100% 100%;opacity:.36;background-repeat:no-repeat;background:url(data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACAAAAAgCAMAAABEpIrGAAAABGdBTUEAALGPC/xhBQAAACBjSFJNAAB6JgAAgIQAAPoAAACA6AAAdTAAAOpgAAA6mAAAF3CculE8AAABfVBMVEX///8Ad/8AgP8AgP8AgP8Aff8AgP8Af/8AgP8AVf8Af/8Af/8AgP8AgP8Af/8Afv8AAP8Afv8Afv8Aef8AgP8AdP8Afv8AgP8AgP8Acf8Ae/8AgP8Af/8AgP8Af/8Af/8AfP8Afv8AgP8Af/8Af/8Afv8Afv8AgP8Afv8AgP8Af/8Af/8AgP8AgP8Afv8AgP8Af/8AgP8AgP8AgP8Ae/8Afv8Af/8AgP8Af/8AgP8Af/8Af/8Aff8Af/8Abf8AgP8Af/8AgP8Af/8Af/8Afv8AgP8AgP8Afv8Afv8AgP8Af/8Aff8AgP8Afv8AgP8Aff8AgP8AfP8AgP8Ae/8AgP8Af/8AgP8AgP8AgP8Afv8AgP8AgP8AgP8Afv8AgP8AgP8AgP8AgP8AgP8Af/8AgP8Af/8Af/8Aev8Af/8AgP8Aff8Afv8AgP8AgP8AgP8Af/8AgP8Af/8Af/8AgP8Afv8AgP8AgP8AgP8AgP8Af/8AeP8Af/8Af/8Af//////rzEHnAAAAfXRSTlMAD7CCAivatxIDx5EMrP19AXdLEwgLR+6iCR/M0yLRzyFF7JupSXn8cw6v60Q0QeqzKtgeG237HMne850/6Qeq7QaZ+WdydHtj+OM3qENCMRYl1B3K2U7wnlWE/mhlirjkODa9FN/BF7/iNV/2kASNZpX1Wlf03C4stRGxgUPclqoAAAABYktHRACIBR1IAAAACXBIWXMAAAsTAAALEwEAmpwYAAAAB3RJTUUH4gEaBzgZ4yeM3AAAAT9JREFUOMvNUldbwkAQvCAqsSBoABE7asSOBRUVVBQNNuy9996789+9cMFAMHnVebmdm+/bmdtbQv4dOFOW2UjPzgFyLfo6nweKfIMOBYWwFtmMPGz2Yj2pJI0JDq3udJW6VVbmKa9I192VQFV1ktXUAl5NB0cd4KpnORqsEO2ZIRpF9gJfE9Dckqq0KuZt7UAH5+8EPF3spjsRpCeQNO/tA/qDwIDA+OCQbBoKA8NOdjMySgcZGVM6jwcgRuUiSs0nlPFNSrEpJfU0jTLD6llqbvKxei7OzvkFNQohi0vAsj81+MoqsCaoPOQFgus/1LyxichW+hS2JWCHZ7VlF9jb187pIAYcHiViHAMnp5mTjJ8B5xeEXF4B1ze/fTh/C0h398DDI9HB07O8ci+vRBdvdGnfP4gBuM8vw7X/G3wDmFhFZEdxzjMAAAAldEVYdGRhdGU6Y3JlYXRlADIwMTgtMDEtMjZUMDc6NTY6MjUrMDE6MDA67pVWAAAAJXRFWHRkYXRlOm1vZGlmeQAyMDE4LTAxLTI2VDA3OjU2OjI1KzAxOjAwS7Mt6gAAABl0RVh0U29mdHdhcmUAd3d3Lmlua3NjYXBlLm9yZ5vuPBoAAAAWdEVYdFRpdGxlAGp1ZWppbl9sb2dvIGNvcHlxapmKAAAAV3pUWHRSYXcgcHJvZmlsZSB0eXBlIGlwdGMAAHic4/IMCHFWKCjKT8vMSeVSAAMjCy5jCxMjE0uTFAMTIESANMNkAyOzVCDL2NTIxMzEHMQHy4BIoEouAOoXEXTyQjWVAAAAAElFTkSuQmCC)&#125;.markdown-body h2&#123;position:relative;font-size:20px;border-left:4px solid;padding:0 0 0 10px;margin:30px 0&#125;.markdown-body h3&#123;font-size:16px&#125;.markdown-body ul&#123;list-style:disc outside;margin-left:2em;margin-top:1em&#125;.markdown-body li&#123;line-height:2;color:#595959&#125;.markdown-body img.loaded&#123;margin:0 auto;display:block&#125;.markdown-body blockquote&#123;background:#fff9f9;margin:2em 0;padding:2px 20px;border-left:4px solid #b2aec5&#125;.markdown-body blockquote p&#123;color:#666;line-height:2&#125;.markdown-body a&#123;color:#036aca;border-bottom:1px solid rgba(3,106,202,.8);font-weight:400;text-decoration:none&#125;.markdown-body em strong,.markdown-body strong&#123;color:#036aca&#125;.markdown-body hr&#123;border-top:1px solid #135ce0&#125;.markdown-body pre&#123;overflow:auto&#125;.markdown-body code,.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body table&#123;border-collapse:collapse;margin:1rem 0;overflow-x:auto&#125;.markdown-body table td,.markdown-body table th&#123;border:1px solid #dfe2e5;padding:.6em 1em&#125;.markdown-body table tr&#123;border-top:1px solid #dfe2e5&#125;.markdown-body table tr:nth-child(2n)&#123;background-color:#f6f8fa&#125;</style><p><strong>这是我参与8月更文挑战的第2天，活动详情查看：<a href="https://juejin.cn/post/6987962113788493831" title="https://juejin.cn/post/6987962113788493831" target="_blank">8月更文挑战</a></strong></p>
<h1 data-id="heading-0">引言</h1>
<p>在分布式微服务场景下，由于各个业务服务的纵向拆分，加上通常会使用集群技术来保障业务服务的可靠性，由此导致了应用服务节点的爆炸式增长，服务节点的增多会导致出故障的概率也随之增加。如之前文章所阐述的，某个应用节点的不可用可能导致最终整个平台正常运行受影响，因此我们需要一些手段去应对这种异常情况。<code>Hystrix</code>正是一种专门针对微服务容错处理的基础组件，本文主要针对容错组件<code>Hystrix</code>进行设计分析，希望对大家有所裨益。</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/75a23c424a884d1e80cb1be35b0e81f0~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h1 data-id="heading-1">Hystrix是什么？</h1>
<p>由于微服务架构的风靡于世，在微服务分布式场景中，某些服务节点既是上游业务的依赖方又是下游业务的调用方，各个服务的之间的依赖关系形成我们具体的业务处理流程。在实际的生产环境中，许多服务依赖项中在运行过程中或许由于代码问题、或许由于资源使用问题，可能会出现服务响应慢以及无法响应等问题。<code>Hystrix</code>是<code>Netflix</code>提供的一款服务容错基础组件，通过引入它可以给原有的应用添加延迟容忍和容错逻辑，以达到提升整个微服务架构的服务治理能力的目的。<code>Hystrix</code>通过隔离服务之间的访问点、阻止跨服务的级联故障以及提供降级访问机制实现以提高系统的整体弹性以及稳定性。</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/40f1dd054dfe4cf7bda141ce7c3c0067~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h1 data-id="heading-2">Hystrix解决什么问题？</h1>
<p>复杂的分布式架构中，应用程序的集群节点及其依赖项服务节点非常多，节点出现问题之后如何进行及时容错处理是微服务架构稳定性以及可靠性的重要体现，那么<code>Hystrix</code>到底可以为我们解决那些问题呢？</p>
<p>1、 阻止某个有问题调用耗尽系统的所有线程，限制线程资源消耗；</p>
<p>2、阻止异常在分布式系统之间的传播；</p>
<p>3、快速失败代替请求排队；</p>
<p>4、错误回退、优雅的服务降级；</p>
<h1 data-id="heading-3">Hystrix原理分析</h1>
<h2 data-id="heading-4">1、问题分析</h2>
<p>如下图所示，应用请求会进入所有后端服务集群。如果各个服务节点都是正常的，那么服务节点便会正常响应， 对应的依赖的服务也会正常运行，一切看起来都很美好。</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/b5f31e5ed5f4450c9c30babcb864b8cc~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>但是现实总是很残酷的，如果依赖的某个服务节点出现异常，比如此时服务正在进行<code>full GC</code>，无法响应外部请求。因此此时的用户请求会被阻塞住。如下图所示，用户请求分别调用服务A、H、I以及P服务来完成某项业务流程，但是此时服务I出现异常或者服务I集群的某个节点出现了异常，虽然两者的连接还保持着，但是所有发送过去的业务请求都出现<code>timeout</code>。那么此时调用方的工作线程就会被阻塞住，导致调用方出现线程不断被被占用的情况。</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/692d64327ccf4f93af3b7ec53d94d689~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>在流量较大的场景下，由于后端某些节点的异常，服务提供者不可用，如下图的依赖I服务不可用，请求无法正常返回，那么调用方会不断进行重试进一步加大流量，最终导致调用方线程资源耗尽，导致服务调用者不可用。服务调用者也可能是上游服务的服务提供方，由于请求资源不断被占用，同时导致上游依赖应用同步被影响，最后故障点会蔓延到整个平台中。</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/76938138f4f44491b72265a8d18b7c9d~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-5">2、问题破解</h2>
<p>既然微服务架构中某个节点的异常可能导致整个平台的不可用，有什么好的解决方案可以解决这个问题呢？如果说这个故障节点就像是病毒传播的一号病人一样，那么只要及时的发现以及隔离它，避免异常节点的进一步影响发散，是不是就可以解决微服务架构各个服务之间的依赖调用异常导致的问题。基于此的分析，我们希望借助<code>Hystrix</code>实现如下的几点核心逻辑：</p>
<p><strong>资源隔离</strong>：限制调用服务使用的资源，当某一下游服务出现问题时，不会影响整个服务调用链。</p>
<p><strong>服务熔断</strong>：当失败率达到阀值自动触发熔断，熔断器触发后原有的请求链路被切断，请求无法正常触达服务提供方。</p>
<p><strong>服务降级</strong>：超时、资源不足等异常触发熔断后，需要调用预设的降级接口返回兜底数据，提升平台容错能力。</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/74192c158ce743d496c51ce073958a50~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-6">3、实现原理</h2>
<h3 data-id="heading-7">（1）业务流程</h3>
<p>如果想要实现异常情况的熔断保护，首先我们得有个断路器，由它作为调用流量的开关。大致的运行逻辑如下图所示，服务调用时判断断路器是否打开，如果打开了则进行降级操作，果没有打开则判断信号量以及线程池是否拒绝，如果拒绝则同样执行降级流程。如果正常则上报自己的健康状态。执行正常流程看是否成功，失败了则执行降级流程。如果成功了，则上报监控数据，如果超时同样是执行降级策。</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/f86f8b8ce1cf49d3817dc15ec986fbe8~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-8">（2）断路器原理分析</h3>
<p>断路器的作用实际就是之前文章中说到的微服务架构中的保险丝一样，起到保护系统的作用。当对下游服务调用异常量达到设定阈值后，将断路器打开，触发熔断操作，避免流量继续堆积。</p>
<p>断路器涉及到的主要设计点主要包括两项，一个是断路器的控制逻辑（控制断路器开关的打开和关闭），另一个是触发断路操作的阈值判断与数据统计（统计数据作为断路器的操作判断）。对于断路器本身来说表面上看就是断路器的开关打开或者关闭来控制是否走降级逻辑，实际上核心的逻辑是如何判断什么时候该开以及什么时候该关。</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/d179a01b9442450daa75dc00707f7d06~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p><strong>断路器逻辑控制</strong></p>
<p>断路器的状态转换和注册中心的服务是否在线有点类似，都涉及到状态的变化，只不过断路器多了个半打开的状态。因此实际上还需要对服务是否恢复正常进行判断的过程。大致流程如上图所示，断路器的初始状态是关闭状态，一旦请求失败情况达到了阈值便会打开断路器。断路器打开后需要进行探测，探测什么时候异常恢复之后还是要将断路器进行关闭的。但是在打开断路器之后不会立马进行探测，而是需要经历个窗口期，不然立马重试必然还是失败，这个窗口期就相当于给别人一个恢复的时间窗口。</p>
<p>当过了窗口期之后，将一些请求进行放开，让其完成正常的下游业务调用，进行请求试探，如果成功则关闭断路器，如果失败则继续维持当前断路器的OPEN状态。当然至于探测这块不是说一次成功或者失败就改变断路器现有的状态，这里可以设置对应的状态变更策略。</p>
<p><strong>阈值统计</strong></p>
<p>阈值以及数据统计是进行开关打开的判断依据，因此如何统计数据是非常关键的设计。如果阈值统计不够准确有效，那么实际无法起到该有的作用，如果断路器过于敏感，偶尔的调用异常就打开断路器（网络抖动等），势必会严重影响正常的业务流程。如果断路器过于迟钝，该打开的时候不打开，那么可能导致异常在全平台的传播</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/4e93b914da344fdfa332a3b3003e1dc0~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>既然不能通过一次的调用成功或者失败来判断，那么我们可以把统计的周期拉长，通过几个周期来判断。同时为了保证判断的时效性，统计的周期需要不断更新。如上图所示，一开始的统计周期是0-7，过了一个时间节点后统计周期就是1-8，时间间隔不变但是统计的开始时间和结束时间是实时更新的，这就类似一个滑动窗口，随着时间的推移不断向前行进，保障统计的时效。</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/d5a200ab2a4f4156afc9cded9f2547ea~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p><strong>（3）隔离设计</strong></p>
<p><code>Hystrix</code>通过隔离的方式来限制异常节点访问对平台的影响，这个就类似于之前我文章提到的船舱内的隔板，限制异常影响范围。主要包括线程池隔离以及信号量隔离。</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/d15ead5131bd4a1487f1b8e36268a75c~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p><strong>线程隔离</strong></p>
<p>如上图所示，在线程隔离的实现方式中，通过将用户请求线程与<code>Hystrix</code>组件线程进行隔离，如果出现服务提供方不可用的情况，阻塞的线程是线程池冲分配的线程，将资源隔离的影响降到最低。组件包装依赖调用逻辑，每个调用<code>conmand</code>在单独线程池中执行，限制线程资源占用。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/db5ba4c2150f4a8ca0293677fa959eae~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>通过发送请求线程与执行请求的线程资源隔离，可有效防止发生级联故障。当线程池或请求队列饱和时，<code>Hystrix</code>将拒绝服务，使得服务请求线程可以<code>fast-fail</code>，从而避免服务节点问题导致的依赖异常扩散。</p>
<p><strong>信号量隔离</strong></p>
<p>我们都知道线程池的引入会带来一定的资源消耗，因为涉及到线程池内部的线程资源调度。因此比较适合引入线程池带来的好处多于资源调用损耗的场景。在一般的场景下，使用更加轻量级的隔离方式会更加适合，那么信号量正是这种轻量级的隔离方式，不存在线程上下文切换所带来的性能开销。从隔离设计的第一张图中我们可以看出使用线程池时，发送请求的线程和执行依赖服务的线程不是同一个，线程池的使用方式就是将它们进行了隔离。而使用信号量时，发送请求的线程和执行依赖服务的线程是同一个线程， 都是发起请求的线程，信号量隔离限制对某个资源调用的并发数。</p>
<h1 data-id="heading-9">总结</h1>
<p>本文主要对微服务架构中服务容错降级进行背景问题分析，阐述了服务容错组件Hystrix组件在服务容错、降价以及熔断方面的设计内容。相信大家对于服务容错这块内容有了更加深刻的理解。在后面的文章中，笔者将对Hystrix组件在开发的微服务应用中具体的应用进行说明，请大家敬请期待。</p>
<hr>
<p>我是慕枫，感谢各位小伙伴点赞、收藏和评论，文章持续跟新，我们下期再见！</p>
<p><em><strong>真正的大师永远怀着一颗学徒的心</strong></em></p>
<blockquote>
<p>微信搜索：慕枫技术笔记，优质文章持续更新，我们有学习打卡的群可以拉你进，一起努力冲击大厂，另外有很多学习以及面试的材料提供给大家。</p>
</blockquote>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/18ab39046c654e3d81e7d63a002c50ad~tplv-k3u1fbpfcp-watermark.image" alt="20210528220244677.gif" loading="lazy" referrerpolicy="no-referrer"></p></div>  
</div>
            