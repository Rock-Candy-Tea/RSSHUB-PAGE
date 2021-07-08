
---
title: 'DevOps发布策略简介'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/602dc869d5694e02b913ec77c3e383ae~tplv-k3u1fbpfcp-zoom-1.image'
author: 掘金
comments: false
date: Wed, 07 Jul 2021 17:46:42 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/602dc869d5694e02b913ec77c3e383ae~tplv-k3u1fbpfcp-zoom-1.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p><strong>简介：</strong> DevOps追求更短的迭代周期、更高频的发布。但发布的次数越多，引入故障的可能性就越大。更多的故障将会降低服务的可用性，进而影响到客户体验。所以，为了保证服务质量，守好发布这个最后一道关，阿里逐步发展出了适应DevOps要求的发布策略。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/602dc869d5694e02b913ec77c3e383ae~tplv-k3u1fbpfcp-zoom-1.image" alt="image.png" title="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>作者 | 沉银<br>
来源 | 阿里技术公众号</p>
<h3 data-id="heading-0">前言</h3>
<p>DevOps追求更短的迭代周期、更高频的发布。但发布的次数越多，引入故障的可能性就越大。更多的故障将会降低服务的可用性，进而影响到客户体验。所以，为了保证服务质量，守好发布这个最后一道关，阿里逐步发展出了适应DevOps要求的发布策略。</p>
<p>在开始讲述阿里的实践之前，我们先简单介绍下几种常见发布策略，以及它们适用的场景和优缺点。</p>
<h3 data-id="heading-1">一 常见发布策略</h3>
<h4 data-id="heading-2">1 停机发布</h4>
<p>停机发布会在发布以前关闭服务，停止用户访问，然后一次性的升级所有服务。这种发布策略的发布频率往往比较低，且需要在发布之前做好充足的测试。</p>
<p>停机发布的特点有：</p>
<ul>
<li>所有需要升级的组件被整合到一次发布中</li>
<li>一个项目中的大部分应用都会被更新</li>
<li>发布之前的研发流程和测试流程往往需要花很长的时间</li>
<li>发布时如果出现问题, 修复和回滚的成本很高</li>
<li>完成一次停机发布, 需要花费很久的时间, 且需要很多团队在一起才能完成</li>
<li>往往需要客户端和服务器端同步升级</li>
</ul>
<p>停机发布并不适合互联网公司，因为两次发布的间隔很久，从功能特性提出到进入市场的时间太长，对市场反应不敏感，会在充分竞争的市场里处于下风。每次发布因为要停机，也会带来经济损失。</p>
<p>优势：</p>
<ol>
<li>简单，不太需要考虑新旧版本共存时的兼容性问题</li>
</ol>
<p>劣势：</p>
<ol>
<li>发布过程中，服务不可用</li>
<li>只能在业务低峰期 (往往是夜间)发布，并且需要很多团队在一起工作</li>
<li>出现故障后很难回滚</li>
</ol>
<p>适合场景：</p>
<ol>
<li>开发测试环境</li>
<li>非关键应用，用户影响面小</li>
<li>兼容性比较难管控的场景</li>
</ol>
<h4 data-id="heading-3">2 金丝雀发布</h4>
<p>金丝雀发布这个术语源自20世纪初期，当时英国的煤矿工人在下井采矿之前，会把笼养的金丝雀携带到矿井中，如果矿井中一氧化碳等有毒气体的浓度过高，在影响矿工之前，金丝雀相比人类表现的更加敏感快速，金丝雀中毒之后，煤矿工人就知道该立刻撤离。金丝雀发布是在将整个软件的新版本发布给所有用户之前，先发布给部分用户，用真实的客户流量来测试，以保证软件不会出现严重问题，降低发布风险。</p>
<p>在实践中，金丝雀发布一般会先发布到一个小比例的机器，比如 2% 的服务器做流量验证，然后从中快速获得反馈，根据反馈决定是扩大发布还是回滚。金丝雀发布通常会结合监控系统，通过监控指标，观察金丝雀机器的健康状况。如果金丝雀测试通过，则把剩余的机器全部升级成新版本，否则回滚代码。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/e566ffb352c447d2a9c59d0cf581ae8b~tplv-k3u1fbpfcp-zoom-1.image" alt="image.png" title="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>优势：</p>
<ol>
<li>对用户体验影响较小，在金丝雀发布过程中，只有少量用户会受影响</li>
<li>发布安全能够得到保障</li>
</ol>
<p>劣势：</p>
<ol>
<li>金丝雀的机器数量比较少, 有一些问题并不能够暴露出来</li>
</ol>
<p>适用场景：</p>
<ol>
<li>监控比较完备且与发布系统集成</li>
</ol>
<h4 data-id="heading-4">3 灰度/滚动发布</h4>
<p>灰度发布是金丝雀发布的延伸，是将发布分成不同的阶段/批次，每个阶段/批次的用户数量逐级增加。如果新版本在当前阶段没有发现问题，就再增加用户数量进入下一个阶段，直至扩展到全部用户。</p>
<p>灰度发布可以减小发布风险，是一种零宕机时间的发布策略。它通过切换线上并存版本之间的路由权重，逐步从一个版本切换为另一个版本。整个发布过程会持续比较长的时间, 在这段时间内，新旧代码共存，所以在开发过程中，需要考虑版本之间的兼容性，新旧代码共存不能影响功能可用性和用户体验。当新版本代码出现问题时，灰度发布能够比较快的回滚到老版本的代码上。</p>
<p>结合特性开关等技术，灰度发布可以实现更复杂灵活的发布策略。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/1797a21ed7d4451d9a291a8323233c2f~tplv-k3u1fbpfcp-zoom-1.image" alt="image.png" title="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>优势：</p>
<ol>
<li>用户体验影响比较小, 不需要停机发布</li>
<li>能够控制发布风险</li>
</ol>
<p>劣势：</p>
<ol>
<li>发布时间会比较长</li>
<li>需要复杂的发布系统和负载均衡器</li>
<li>需要考虑新旧版本共存时的兼容性</li>
</ol>
<p>适用场景：</p>
<ol>
<li>适合可用性较高的生产环境发布</li>
</ol>
<h4 data-id="heading-5">4 蓝绿发布</h4>
<p>蓝绿部署是指有两个完全相同的、互相独立的生产环境，一个叫做“蓝环境”，一个叫做“绿环境”。其中，绿环境是用户正在使用的生产环境。当要部署一个新版本的时候，先把这个新版本部署到蓝环境中，然后在蓝环境中运行冒烟测试，以检查新版本是否正常工作。如果测试通过，发布系统更新路由配置，将用户流量从绿环境导向蓝环境，蓝环境就变成了生产环境。这种切换通常在一秒钟之内就能搞定。如果出了问题，把路由切回到绿环境上，再在蓝环境中调试，找到问题的原因。因此，蓝绿部署可以做到仅仅一次切换，立刻就向所有用户推出新版本，新功能对所有用户立刻生效可见。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/35ef65d6d10e43b8ba65b20f1dd0c5f6~tplv-k3u1fbpfcp-zoom-1.image" alt="image.png" title="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>优势：</p>
<ol>
<li>升级切换和回退速度非常快</li>
<li>零停机时间</li>
</ol>
<p>不足：</p>
<ol>
<li>一次性的全量切换，如果发布出现问题, 会对用户产生比较大的影响</li>
<li>需要两倍的机器资源</li>
<li>需要中间件和应用自身支持热备集群的流量切换</li>
</ol>
<p>适用场景：</p>
<ol>
<li>机器资源比较富余或者按需分配 (背靠云厂商)</li>
</ol>
<h4 data-id="heading-6">5 A/B 测试</h4>
<p>A/B 测试和灰度发布非常像，可以从发布的目的上进行区分。AB测试侧重的是根据A版本和B版本的差异进行决策，最终选择一个版本进行部署。和灰度发布相比，AB测试更倾向于去决策，和金丝雀发布相比，AB测试在权重和流量的切换上更灵活。</p>
<p>举个例子，某功能有两个实现版本 A 和 B，通过细粒度的流量控制，把 50% 的用户总是引导到 A 实现上，把剩下的 50% 用户总是引导到 B 实现上，通过比较 A 实现和 B 实现的转化率，最终选择转化率较高的 A 实现作为功能的最终版本。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/98ccbfb16b674f3094c83a2a1ef739d1~tplv-k3u1fbpfcp-zoom-1.image" alt="image.png" title="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>优势：</p>
<ol>
<li>快速实验能力</li>
<li>用户体验影响小</li>
<li>可以使用生产环境流量做测试</li>
<li>可以针对某些特定用户做测试</li>
</ol>
<p>不足：</p>
<ol>
<li>需要较为复杂的业务流量识别和控制能力</li>
<li>需要考虑较为复杂的新旧版本兼容性问题</li>
</ol>
<p>适用场景：</p>
<ol>
<li>用来做业务探索和创新测试</li>
<li>需要对多个方案进行决策</li>
</ol>
<h4 data-id="heading-7">6 流量隔离环境发布</h4>
<p>在上述的发布策略中，发布的单位都是应用，但是一个功能模块往往是由多个应用组合在一起提供的服务，即使当前发布的应用出现了异常，这个异常也未必体现在当前应用中，在复杂的情况下，异常会延迟到它的下游应用才体现出来，如何发现此类问题并且不影响用户体验是非常重要的。此外，我们有时候还希望新版本的代码上线以后，只影响到一小部分用户。而传统的灰度发布，因为无法识别业务流量，所以即使某个应用只有一台机器出现了问题，也可能会影响到所有的用户。</p>
<p>如下图左侧的灰度发布，App1 的所有机器都有一定概率会路由到出现问题的红色 App2 机器上。而右侧的隔离环境发布中，新版本的代码会先发布在全链路隔离环境中，即使发布中出现问题，也只会影响少量用户。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/633091d9854b4a2db4bc8847fdfd3b4b~tplv-k3u1fbpfcp-zoom-1.image" alt="image.png" title="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>优势：</p>
<ol>
<li>能够发现一些复杂的, 涉及到多应用的问题</li>
<li>出现故障时, 只会影响很小一部分用户</li>
</ol>
<p>不足：</p>
<ol>
<li>需要对流量隔离环境进行独立监控</li>
<li>系统设计复杂, 需要中间件和链路上的所有应用能够识别业务流量</li>
</ol>
<p>适用场景：</p>
<ol>
<li>较为核心的生产业务场景</li>
</ol>
<h3 data-id="heading-8">二 阿里巴巴发布最佳实践</h3>
<p>我们将按照发布的过程来介绍阿里巴巴发布的最佳实践。</p>
<h4 data-id="heading-9">1 发布计划</h4>
<p>发布前要对待发布功能模块做充分验证，同时要思考假如本次发布引入故障该如何止血。所以在发布之前写出本次发布的计划清单是非常重要的，一个典型的发布计划如下：</p>
<ul>
<li>
<p>本次发布参与人</p>
<ul>
<li>开发人</li>
<li>测试人</li>
<li>代码 Review 人</li>
</ul>
</li>
<li>
<p>发布内容</p>
</li>
<li>
<p>测试过程</p>
</li>
<li>
<p>风险描述</p>
</li>
<li>
<p>线上验证方案</p>
</li>
<li>
<p>线上出现问题的止血方案</p>
</li>
<li>
<p>发布步骤</p>
<ul>
<li>分 x 批发布</li>
<li>前 x 批发布后暂停 x 小时</li>
</ul>
</li>
</ul>
<h4 data-id="heading-10">2 不同环境使用不同的发布策略</h4>
<p>前面介绍的几种发布策略都有各自的优缺点，要根据自己的场景特点和需求选择合适的发布策略。</p>
<p>一般来说，测试环境是用来做初步功能测试，所以会频繁的更新代码和发布，如果采用灰度发布的方式且发布的批次设置的比较大，则开发效率会大打折扣。这个时候单机或多机的单批次停机发布其实是一个不做的选择。</p>
<p>对于预发环境，不仅要考虑自己测试的需要，还要考虑上下游其他开发者的测试需求，所以单批次停机发布就不再合适，可以设置两批发布。</p>
<p>对于线上环境，可以先发布隔离流量环境，再多批次发布线上环境。</p>
<h4 data-id="heading-11">3 发布中关注监控报警</h4>
<p>仅靠发布策略是无法避免故障的发生的，在发布中和发布后仔细的观察应用的监控数据非常重要。应用的核心指标监控数据，比如 QPS、RT、成功率和报错数，能够帮助用户尽可能早的发现故障。此外，在生产环境中，如果批次数量设置的比较小，每批发布机器数量比较少，那么即使某些监控指标出现了问题，因为数据量比较小，可能会被淹没在整体的监控数据中，所以配置已发布机器的独立监控也是非常重要的。</p>
<h4 data-id="heading-12">4 金丝雀发布和无人值守</h4>
<p>阿里内部绝大部分应用会在多机房/单元部署，可能存在一种场景，同一份代码和配置在某些机房/单元正常，在其他的的单元/机房下就会出现故障，所以有必要在分批发布的时候，把所有机房/单元的组合都在第一批发布时出现，这样问题可以及早暴露。此外研发人员往往会重点关注前几批发布，如果后面批次才出现问题，研发人员可能无法快速响应。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/c7db82307462403fa1b234735e3c7688~tplv-k3u1fbpfcp-zoom-1.image" alt="image.png" title="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<blockquote>
<p>单元化是为了解决容灾和扩展性问题，上图是阿里巴巴的单元化部署架构。</p>
</blockquote>
<p>此外，应用的监控项一般都很多，在发布周期比较长的情况下，不能要求研发人员时刻专注每一个监控项，需要一定的智能化方案帮助研发找出那些需要重点关注的监控项。</p>
<p>为了解决上面两个问题，阿里设计并实现了自己的金丝雀发布策略。金丝雀发布从应用的每个机房/单元下抽取 10% 的机器放到首批，无人值守智能监控系统会对这部分机器设置独立的监控，对于每个监控项，无人值守会对比已发布和未发布机器的监控指标数据，同时对比发布前和发布后的监控数据，如果发现异常，会推送给研发人员做进一步的判断。</p>
<p>这种金丝雀发布策略可以帮助研发尽可能早的发现问题, 并且减少研发人员的工作量，提高研发效率。</p>
<h4 data-id="heading-13">5 持续集成和发布</h4>
<p>合理的选择发布策略，按照上面所述的最佳实践来发布，发布的风险可以被控制在很小的范围内，甚至比停机发布的风险还要小。实际上，发布周期短，每次发布仅包含少量代码是一个很好的发布实践。因为部署间隔时间长，将会导致每次的部署包含更多的代码变更，结果就是出现更多缺陷和宕机的风险。这种情况下，人们为了降低发布风险，会倾向于增加更多的评审，事实上这除了大大增加部署时间外，对降低发布风险的影响微乎其微。这是一个越来越差的增强回路，我们需要通过高频的持续部署，来颠覆这个恶性循环。</p>
<h3 data-id="heading-14">三 总结</h3>
<p>敏捷开发能够缩短产品走向市场的时间，让消费者更快地获得想要的功能，也能让产品团队更快地拿到消费者的反馈并据此对产品做出迭代。为了解决敏捷开发下频繁发布带来的发布风险，本文介绍了多种发布策略，包括各个发布策略的优缺点、适用场景，在不同场景下综合应用这些模式可以在更快速地交付高质量的产品。</p>
<p><a href="https://link.juejin.cn/?target=http%3A%2F%2Fclick.aliyun.com%2Fm%2F1000282425%2F" target="_blank" rel="nofollow noopener noreferrer" title="http://click.aliyun.com/m/1000282425/" ref="nofollow noopener noreferrer">原文链接</a></p>
<p>本文为阿里云原创内容，未经允许不得转载。</p></div>  
</div>
            