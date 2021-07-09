
---
title: '你也可以搞懂的微服务第一篇——来自ThoughtWork的学习体验'
categories: 
 - 编程
 - 掘金
 - 标签
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/a01c971e23b24b849dde6163e77e35ec~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Thu, 08 Jul 2021 21:26:41 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/a01c971e23b24b849dde6163e77e35ec~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>「本文已参与好文召集令活动，点击查看：<a href="https://juejin.cn/post/6978685539985653767" target="_blank" title="https://juejin.cn/post/6978685539985653767">后端、大前端双赛道投稿，2万元奖池等你挑战！</a>」</p>
<blockquote>
<ul>
<li>📢欢迎点赞 ：👍 收藏 ⭐留言 📝 如有错误敬请指正，赐人玫瑰，手留余香！</li>
<li>📢本文作者：由webmote 原创，首发于 【掘金】</li>
<li>📢作者格言： 生活在于折腾，当你不折腾生活时，生活就开始折腾你，让我们一起加油！💪💪💪</li>
</ul>
</blockquote>
<h1 data-id="heading-0">🎏 序言</h1>
<p>“滚滚长江东逝水，浪花淘尽英雄。”</p>
<p>技术之路上，繁星点点，今天且来看看“微服务 ”，如何称雄。</p>
<p>“<strong>微服务</strong>” 这个词好像已经出来十年了吧，我有幸从好早之前就一直从事相关的开发实践。所以一直想写有关微服务拆分的题材，但都觉得自己理解不到位，难以下笔。</p>
<p>因为没有系统的理论知识，很难写出什么新花样。🌷🌷🌷</p>
<p>直到最近参加了ThoughtWork的系列直播课，我觉得是时候系统的整理下学习心得，也算给最近的听课以交代。</p>
<p>里面夹杂了自己的实践感悟，写的不一定能面面俱到，也不可能准确无误，欢迎大家纠正！共同📝交流探讨。</p>
<h1 data-id="heading-1">🎏 01.微服务是啥？</h1>
<p>微服务(Microservice)概念据说是在2012年出现，其一出现就对互联网行业产生了巨大影响，因为其理念刚好符合“<strong>分而治之</strong>”的思想，在日益巨大化的互联网行业内，不免逐步产生了无法把控的思绪混乱，而“<strong>微</strong>”刚好能解决这个痛点。</p>
<p>先不上定义，仅从字面意思，我们就能看出，微服务即是<strong>小服务</strong>，巨大的服务怎么看也和“<strong>微</strong>”格格不入。</p>
<p><strong>掘金牙医</strong>曾经写过一篇《我在掘金这3年 - 如何给飞行中的飞机换引擎》，在其中有段阐述，我觉得理解的很有地气。</p>
<blockquote>
<p>我们将 <strong>Wordpress</strong>(<em>一款php语言编写的个人博客系统</em>) 无限拆分, 拆分到每个 <strong>function</strong> 都构成一个服务 (因为再细分已经毫义, 把一个大小, 功能适当的 <strong>function</strong> 再拆开只会降低性能徒增复杂度). 那么以 <strong>function</strong> 为服务最小单位的 repo 组成的业务就是服务中的最小模式了.</p>
</blockquote>
<blockquote>
<p>为了讨论的简便, 我们直接把最小服务模式叫 Picoservice. 最大模式叫 Polyservice. Polyservice 的话我们刚才说的 Wordpress 就是个很好的例子, 现实中 Polyservice 有很多, 传统业务可能都是这样组织代码的, 相信大家也都见到过. 但每个 function 都拆分成服务的业务可不多见, 我粗略统计了下 Wordpress 大概有一万个 function. 可以想象将 Wordpress 拆分成 Picoservice 最后组织成业务是多么可怕的事情. 现实中只有 FAAS 平台上运行的业务可能是以单个 <strong>function</strong> 的形式组成并运行的.</p>
</blockquote>
<blockquote>
<p>依据服务大小的定义, 我们可以把现有的服务类型按照大小进行排序:</p>
</blockquote>
<blockquote>
<p><strong>Picoservice <= FAAS(or ServerLess) < Microservice < Monoservice <= Polyservice</strong></p>
</blockquote>
<blockquote>
<p><strong>注意:</strong> 服务大小跟服务部署规模没有关系, 无论是 Picoservice 还是 Polyservice, 只要设计得当都可以多机部署以提升性能.</p>
</blockquote>
<p>看过接地气的描述外，回头我们再看看微服务<strong>真正的定义</strong>是啥？</p>
<p>“微服务”是是一种架构模式，它提倡将单一的应用程序<strong>划分成一组小的服务</strong>，每个服务运行在其<strong>独立的进程</strong>中，服务间采用<strong>轻量级的通信机制</strong>互相沟通。每个服务都围绕具体业务进行构建，并且能够被<strong>独立的部署</strong>到生产环境。</p>
<p>简而言之，微服务是一种将单个应用以许多微小服务所组成的服务套件的形式来构建软件的方法，每个微服务拥有<strong>自己的轻量级数据处理模块</strong>以及<strong>通信机制</strong>（通常是 HTTP API 的形式）。 微服务围绕业务能力和各自独立的自动化部署机制构建而来。由于微服务需要极少的集中管理，因此各个服务可以使用不同的编程语言以及存储技术。</p>
<p>当年写三国的罗贯中虽然没有做过码农，编写过前后端代码，经历过内卷的996、007，承担过系统架构师，但其凭借自己敏锐的洞察力，在当时已经提出了IT界技术发展更迭的规律: <code>话说天下大势，分久必合，合久必分。周末七国分争，并入于秦。及秦灭之后，楚、汉分争，又并入于汉。汉朝自高祖斩白蛇而起义，一统天下，后来光武中兴，传至献帝，遂分为三国。</code></p>
<p>你品，你细品！中文文化的博大精深，底蕴深厚令人折服！</p>
<blockquote>
<p>“<strong>分而治之</strong>”是微服务的精髓！理解了这个精髓，就可以如庖丁解牛般设计你的系统架构。 当然以后肯定有某架构，<strong>一统江山</strong>，又是大势所趋，这是后话，按下不表。</p>
</blockquote>
<h1 data-id="heading-2">🎏 02.微服务的诞生轨迹？</h1>
<p>既然明白了“<strong>分久必合，合久必分</strong>”的理论知识，那我们来看看微服务的诞生轨迹。</p>
<p><code>沿着分分分的路</code>，越走越远。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/a01c971e23b24b849dde6163e77e35ec~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>由于把许多独立的业务拆成不同的微服务，因此带来的微服务构建的复杂度，一般表现为下列几点：</p>
<ul>
<li>微服务的注册和发现</li>
<li>微服务的部署和弹性伸缩</li>
<li>微服务间的通讯</li>
<li>微服务间通讯的效率</li>
<li>微服务间的事务性（ACID）</li>
<li>微服务的对外网关、限流熔断</li>
<li>微服务的全局配置</li>
<li>微服务的认证授权（OAuth2）</li>
<li>微服务间的异步通讯、消息</li>
<li>微服务的日志</li>
<li>微服务的监控</li>
</ul>
<p>以上难题也是大型分布式应用的难题。</p>
<p>因此在我们的应用规模没有上去之前，考虑到时间成本和其他复杂度要素，仍然可以按照<strong>单体 > SOA > 微服务</strong>的进阶步骤一步步实施。</p>
<h1 data-id="heading-3">🎏 03.微服务的打开方式？</h1>
<blockquote>
<p>从A点到B点，直线距离永远是最短的，然而往往这条路也是走的<strong>最艰难的</strong>！所以这世上多了很多的盘山公路！</p>
</blockquote>
<p>不管是旧系统的改造，还是新系统的构建，直接冲向微服务是有很大的风险的。</p>
<p>因此一般的实践建议是：</p>
<ul>
<li>单体或粗粒度服务优先，避免过度设计；</li>
<li>业务演进过程中加深对业务边界的理解；</li>
<li>避免前期因服务划分不合理带来的大量重构工作；</li>
</ul>
<p>当然如果在团队中坏味道已经肆意弥漫了，那就是时候先动手了。 是的，是我先动的手。</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/059fa83815e0403fbd9150083c14c6dd~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>有几种重要的拆分方式：</p>
<h2 data-id="heading-4">🎏 03.1  事件风暴法</h2>
<p>该方法来自传统的DDD领域建模界，DDD方式在互联网应用中被使用的很少，原因有很多了，这里指出的重要的几点供你参考：</p>
<ul>
<li>争端太大，大家对DDD的理解各不相同，并没有太好的标准说服对方；</li>
<li>慢，毕竟要理清楚各个业务边界不是那么容易的，而互联网应用一般是说好了就干；</li>
<li>事件、命令、聚合根、实体等概念诸多，理解不易。</li>
</ul>
<p>虽然有诸多缺点，但瑕不掩瑜，在微服务划分上，DDD异军突起，起到了关键的理论指导意义。</p>
<p>事件风暴法是集合业务人员、领域专家、技术人员、架构和测试人员等一起寻找事件、命令、领域模型，直到划分界限上下文和识别出问题域。</p>
<p>以下步骤略显枯燥，谨慎阅读。</p>
<h3 data-id="heading-5">03.1.1 寻找领域事件</h3>
<ul>
<li>领域事件： 捕获建模领域中所发生的事情</li>
<li>识别：    领域专家所关心的事情，业务上真实发生，有事件顺序</li>
<li>甄别：    领域事件必须是对业务有价值的，必须将导致进一步业务操作的</li>
</ul>
<p>一个例子： 在商品订单业务中。</p>
<p>领域事件：</p>
<ul>
<li>商品已创建、商品已编辑</li>
<li>商品已发布</li>
<li>订单已创建、订单已取消</li>
<li>库存已扣减</li>
<li>出库单已生成</li>
<li>出库单已配货</li>
<li>出库单已发货</li>
<li>订单已发货</li>
<li>订单已签收</li>
<li>订单已确认收货</li>
</ul>
<h3 data-id="heading-6">03.1.2 寻找命令</h3>
<ul>
<li>命令： 产生事件的领域行为或领域活动</li>
<li>识别： 用户的动作、外部系统触发、定时任务</li>
</ul>
<p>接上个例子，有可能的命令：</p>
<ul>
<li>添加商品、编辑商品</li>
<li>发布商品</li>
<li>添加订单、取消订单</li>
<li>定时生成出库单</li>
<li>配货</li>
<li>发货</li>
<li>订单签收</li>
<li>订单确认</li>
</ul>
<h3 data-id="heading-7">03.1.3 寻找领域模型</h3>
<ul>
<li>领域模型： 是对业务领域内的概念类或现实世界中对象的可视化表示</li>
<li>识别： 是否可以被独立访问（可以：就是聚合，不能：属于它依赖的聚合）</li>
<li>做法： 留下聚合即时贴，命令在左，事件在右。</li>
</ul>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/c7af22b4d33440a79701d163de5dd50d~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-8">03.1.4 划分限界上下文</h3>
<ul>
<li>限界上下文： 某<strong>场景或环境</strong>下的业务边界</li>
<li>识别： 定义<strong>业务场景</strong>，然后找寻业务边界</li>
<li>方法：识别出相邻事件的关系，确立上下游角色。一般来说，发布事件的为下游，订阅事件的为上游。</li>
</ul>
<p>例如下面：</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/a0ef81d1e0ca4ddfbc481c0a1ee8824b~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-9">03.1.5 识别问题域</h3>
<ul>
<li>问题域： 需要讨论的问题范围</li>
<li>识别： 站在业务专家的角度看待问题，只能通过与最理解该领域的人一同协作才能完成。</li>
</ul>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/985264e220d640cc9faa4a8fe27f28ae~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-10">🎏 03.2  8X Flow业务建模法</h2>
<p>8X Flow是ThoughtWorks 中国区CTO徐昊研究并设计的方法论。</p>
<p>DDD解释中最容易混淆的是领域的概念本身，通俗的认为<code>领域是问题的集合</code>，问题又是业务的抽象。</p>
<p>那么，领域和业务到底有啥区别呢？</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/1d0deaca88704b94854e9e5422f72bd3~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<blockquote>
<p>徐昊观点： Domain + operation（运维） = business， 领域比较抽象，再更进一步抽象可以变成领域专家系统， 专家可以支撑业务。</p>
</blockquote>
<p>8x Flow的分析方法步骤：</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/ee7d58c2130f4092ae49baa0d5f1b49e~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>主要思想是寻找业务合约（订单支付凭据、订单发货凭据、订单收货凭据等等），基于这些凭据，构造支付流程、发货流程、收货流程等。 甚至于演化为限界上下文。</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/16d9d73267334a23a6da5034ec808f0e~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h1 data-id="heading-11">🎏 04. 拆分微服务的原则</h1>
<p>微服务拆分应遵循的原则，描述如下：</p>
<ul>
<li>低耦合，单一职责</li>
</ul>
<p>微服务的设计和面向对象的设计原则类似，也需要符合低耦合、单一职责的设计原则。</p>
<ul>
<li>单向依赖</li>
</ul>
<p>杜绝循环和双向依赖。采用消息解耦上下游服务。</p>
<ul>
<li>定义上下游</li>
</ul>
<p>下面的图说的非常清晰，上下游服务应遵循下述调用方式。</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/7f020af2ef4242a285089c34b0e1fc1e~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<ul>
<li>数据操作独立</li>
</ul>
<p>数据隔离，让服务操作自身数据。</p>
<ul>
<li>构造BFF</li>
</ul>
<p>为前端应用构造BFF服务，整合微服务间的融合。</p>
<h1 data-id="heading-12">🎏 05. 结语</h1>
<p>微服务按照DDD拆分太烧脑了，也许正如徐昊所说，很多公司的应用应该是业务优先，而不是领域优先，也即很多的业务逻辑，很少的领域逻辑，那么我们拆分这些业务时，完全按照DDD必将陷入迷茫之中。</p>
<p>适合自己的才是最好的，我们掌握这么多方法是为了灵活解决实际的问题，而不是被困在这些武器内不可自拔，甚至发出没有DDD就不是好的微服务的谬论。</p>
<p>后续还会有很长的真实的实践，实践之后再回来总结下。</p>
<p>例行小结，理性看待！</p>
<p>结的是啥啊，结的是我想你点赞而不可得的寂寞。😳😳😳</p>
<p>👓都看到这了，还在乎点个赞吗？</p>
<p>👓都点赞了，还在乎一个收藏吗？</p>
<p>👓都收藏了，还在乎一个评论吗？</p>
<blockquote>
<p><strong>还有系列前端文章，客官，你不瞧瞧？</strong></p>
</blockquote>
<p>👉<a href="https://juejin.cn/post/6981588179539197959" target="_blank" title="https://juejin.cn/post/6981588179539197959">关于微前端(阿里QianKun)的那点事——上线一个“微前端”逼走了2位90后</a></p>
<p>👉<a href="https://juejin.cn/post/6980530046553292831" target="_blank" title="https://juejin.cn/post/6980530046553292831">前端项目，看我在这里管理全局后台初始化的数据，就问你飒不飒？</a></p>
<p>👉<a href="https://juejin.cn/post/6975870882598092830" target="_blank" title="https://juejin.cn/post/6975870882598092830">十分钟手把手教你设计简单易用的组件级考试题（单选、多选、填空、图片），建议收藏</a></p>
<p>👉<a href="https://juejin.cn/post/6972721024274006024" target="_blank" title="https://juejin.cn/post/6972721024274006024">解放前端工程师——手把手教你开发自己的自定义列表和自定义表单系列之一缘起</a></p>
<p>👉<a href="https://juejin.cn/post/6972722813585063973" target="_blank" title="https://juejin.cn/post/6972722813585063973">解放前端工程师——手把手教你开发自己的自定义列表和自定义表单系列之二接口</a></p>
<p>👉<a href="https://juejin.cn/post/6973890009023643679" target="_blank" title="https://juejin.cn/post/6973890009023643679">解放前端工程师——手把手教你开发自己的自定义列表和自定义表单系列之三表格</a></p>
<p>👉<a href="https://juejin.cn/post/6968377565585571847" target="_blank" title="https://juejin.cn/post/6968377565585571847">Vue组件定制——动态查询规则生成组件</a></p></div>  
</div>
            