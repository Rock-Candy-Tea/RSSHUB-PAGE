
---
title: 'Design for failure常见的12种设计思想｜8月更文挑战'
categories: 
 - 编程
 - 掘金
 - 标签
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/f11efdd95f6b444593c485c85ae61e08~tplv-k3u1fbpfcp-zoom-1.image'
author: 掘金
comments: false
date: Mon, 02 Aug 2021 18:22:42 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/f11efdd95f6b444593c485c85ae61e08~tplv-k3u1fbpfcp-zoom-1.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>通常情况下，我们的一个请求会经过三个服务来处理。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/f11efdd95f6b444593c485c85ae61e08~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>请 求从客户端发出，到达 Proxy Layer（执行一些公共的逻辑，如逻辑、流控、审计等），完成后，发往 App Layer（执行具体业务逻辑），执行完毕后，发向 Data Laye（进行数据持久化）。</p>
<p>事情看起来很简单，然而，在一个分布式系统中：<strong>出错是常态</strong>。</p>
<p>因此，我们需要：<strong>Design For Failure</strong>。即当你的系统将错误当作正常流时，系统便已经对错误免疫了。</p>
<p>在此，跟大家介绍常见的 12 种设计思想。</p>
<h3 data-id="heading-0">1、防御性设计（Defensive Design）</h3>
<p>所谓的防御性设计实际上就是“防呆”，英文叫 Idiot Proofing。说白了就是用户有时候会不自觉的做一些蠢事，我们在设计的时候要尽量考虑到一些不规范的交互行为，如果你的用户是一只猴子，你要写包单保证系统不被玩坏。</p>
<blockquote>
<p>例如，在 Android 开发中使用到的 Monkey Test 就是用于这样的目的。</p>
</blockquote>
<h3 data-id="heading-1">2、边界情况（Edge Case）</h3>
<p>这个设计思想在测试领域比较常见，就是我们在设计我们的设计案例的时候有没有充分考虑在边界情况下的系统行为。</p>
<blockquote>
<p>比较常见的例如，闰年情况、跨日情况等边界。</p>
</blockquote>
<h3 data-id="heading-2">3、防误措施（Mistake Proofing）</h3>
<p>怎么保证不会发生错误。例如在人机交互环节，能不能进行输入校验？</p>
<h3 data-id="heading-3">4、解耦（Decoupling）</h3>
<p>设计的时候，哪怕是最基础的代码也应该符合开闭原则。</p>
<p>Spring 的 IOC 就是为了把对象创建及维护从原来的由引用类负责这种强耦合模式转成通过 spring 容器负责。且解耦一般的做法是通过把内部逻辑封装起来，暴露对外统一 API 接口，调用方不需要了解被调用方的内部逻辑实现，只需要知道提供什么功能即可。</p>
<blockquote>
<p>再引申一下，解耦的作用就在于复用，把所有的高内聚功能独立成一个个模块，然后就可以像乐高积木一样根据调用方的实际需求进行组装。</p>
</blockquote>
<h3 data-id="heading-4">5、冗余（Redundancy）</h3>
<p>所谓的冗余指的通过重复配置关键组件或部件，保证在关键组件失效的情况下还有备份组件运作以便保证系统可以继续提供服务。生活中的例子请参与飞机的双引擎设计。</p>
<p>主从模式就是冗余的体现。在正常情况下，主实例负责提供全部的服务，从实例在主实例整体或部分不可用的情况下，完全替代主实例整体或局部而对外提供服务。</p>
<h3 data-id="heading-5">6、重试（Retry）</h3>
<p>重试是在分布式系统下处理瞬态故障的一个基本手段，简单有效（当然重试的前提是要求幂等）。但是重试也是可以很危险的，它能够引起把一个局部小时间迅速升级为一个系统重大故障，严重者导致系统假死。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/f8de065d332a4d5f92aa2289e8e67e77~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>举个简单例子：如果我们的链路类似上图，这里会发生什么问题？</p>
<p>在极端情况下，重试次数达到 5*5*5*5=625 次。</p>
<blockquote>
<p>当链路中的其中一个服务故障率异常的时候，那重试风暴便开启了，因为重试为服务器带来额外的开销和线程的占用，然后其他新来的请求又形成排队，这样的话就形成了类似的 DDos 恶性事件。</p>
</blockquote>
<h3 data-id="heading-6">7、冷备（Cold Standby）</h3>
<p>冷备实际上也是冗余设计的其中一种体现，只是它会更侧重于“冷”，意思是当系统发生宕机时，这个系统是需要手动启动用于替换下线的主实例，它是跟热备是不一样，热备更多体现在自动切换。</p>
<h3 data-id="heading-7">8、熔断（Derating）</h3>
<p>熔断本质上就是一种防御性设计或者策略。假设一个微服务体系下的系统，其中 A 服务调用 B 服务。系统的 QPS 是千级别，当时如果 B 服务挂掉的话 A 的线程绝对在短时间内占满耗尽而导致假死，从而形成大量 A 请求积压而导致情况恶化，最终形成雪崩。</p>
<h3 data-id="heading-8">9、容错（Error Tolerance）</h3>
<p>狭义的容错泛指人机交互界面的时候需要对用户输入进行输入校验，保证数据准确性。</p>
<p>广义的容错应该是两个具有明确边界的事物（如服务间，系统间）交互时候针对可能发生的一切主客观异常情况的防御性手段。常见的容错机制有 failsafe、failback、failover、failfast。</p>
<ul>
<li>
<p>failfast 更多指的是快速失败，避免线程积压导致系统滚雪球式崩溃。</p>
</li>
<li>
<p>failover 指的是失效转移。</p>
</li>
<li>
<p>failsafe 指的是失效安全。</p>
</li>
<li>
<p>failback 指的是失效自动恢复，将故障实例切换到备实例。</p>
</li>
</ul>
<h3 data-id="heading-9">10、失效安全（Fail safe）</h3>
<p>所谓的失效安全，就是指在特定失效的情况下，一个系统或者服务也不会对业务造成损害。</p>
<blockquote>
<p>例如：我们使用 token 进行安全登录也是一种失效安全的体现，如果 token 失效了（如时间过期），用户是无法登录的，因为正常登录需要 token 有一种约束因素，这种因素就是时间。如果时间过了，代表这种约束因素不存在或者不再有效了，登录功能就不能正常工作了。</p>
</blockquote>
<h3 data-id="heading-10">11、优雅降级（Graceful Degradation）</h3>
<p>服务降级跟熔断还是挺像的，只是降级来得更加温和和优雅一点。熔断是直接断掉防止异常进一步扩大而导致雪崩，但是我们的终极目标是提供尽可能多的服务，这个就是优雅降级的理念。在一些异常情况或者秒杀场景下，为了保证核心服务（如商品下单、支付）的正常可用，会放弃掉一些非核心服务（如历史账单查询），这就是所谓的服务降级。</p>
<blockquote>
<p>在微服务框架中，一般会使用 Hystrix 的 @HystrixCommand 或 Feign 的 @FeignClient 对服务进行声明，然后为每个服务配置相应的 fallback 类，最终结合起来进行服务降级。</p>
</blockquote>
<h3 data-id="heading-11">12、耐用性（Durability）</h3>
<p>这里我理解的是系统或数据的耐受性。</p>
<blockquote>
<p>例如数据，为什么我们一定要持久化到数据库，因为就是要借助数据库硬件各种维度的耐受性。</p>
</blockquote>
<h3 data-id="heading-12">补充</h3>
<p>作为一名 designer 或者 developer，应该要对墨菲定律心存敬畏。</p>
<p>另外，需要额外补充一点的就是：<strong>监控（Monitoring）</strong>。</p>
<p>我们的系统有哪几个纬度的监控，估计最多就是常规的硬件状态监控。当然这里的监控我理解除了技术指标监控，还更应该有业务指标监控，否则我们都在裸泳，等海水退下去后就一览无遗。</p>
<blockquote>
<p>监控实际上是为了更好的主动防御，一套完善的告警监控系统，能够快速通知开发与运维，开发侧能够完成紧急修复并能够协同运维进行快速部署。</p>
</blockquote>
<blockquote>
<p>作者：架构精进之路，十年研发风雨路，大厂架构师，CSDN 博客专家，专注架构技术沉淀学习及分享，职业与认知升级，坚持分享接地气儿的干货文章，期待与你一起成长</p>
<p>关注并私信我回复“01”，送你一份程序员成长进阶大礼包，欢迎勾搭。</p>
</blockquote>
<p>Thanks for reading!</p></div>  
</div>
            