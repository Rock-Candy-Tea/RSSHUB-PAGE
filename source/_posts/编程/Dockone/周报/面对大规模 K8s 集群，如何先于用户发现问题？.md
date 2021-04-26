
---
title: '面对大规模 K8s 集群，如何先于用户发现问题？'
categories: 
 - 编程
 - Dockone
 - 周报
headimg: 'https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210425/36e6c61fc1f495265c24d2849b77e4a4.png'
author: Dockone
comments: false
date: 2021-04-26 04:12:02
thumbnail: 'https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210425/36e6c61fc1f495265c24d2849b77e4a4.png'
---

<div>   
<br>作者 | 彭南光（光南）<br>
来源 | <a href="https://mp.weixin.qq.com/s/EXFAywUqHq3QlaAydVuLeQ">阿里巴巴云原生公众号</a><br>
<br><blockquote><br>_千里之堤，溃于蚁穴。_</blockquote><h1>绪论</h1>不知道大家是否经历过这样的情景：突然被用户告知系统出现问题，然后一脸懵地惶惶然排查修复；或是等到自己发现系统出现故障时，实际已经对用户造成了严重的恶劣影响。<br>
<br>所谓千里之堤，溃于蚁穴。用户信任的建立是长期而艰难的，然而要摧毁这种信任却很简单。一旦出现上述问题，不仅极大影响用户使用体验，同时会给用户留下一个这个产品/团队不可靠的印象，丧失用户对产品/团队长期好不容易积累下来的信用资本，未来再想建立这样的信任关系就很难了。<br>
<br>这也是为什么我们说快速发现问题的能力如此重要的原因，只有先做到快速发现问题，才能谈怎样排查问题、如何解决问题。<br>
<br>那么怎样才能在复杂的大规模场景中，做到真正先于用户发现问题呢？下面我会带来我们在管理大规模 ASI 集群过程中对于快速发现问题的一些经验和实践，希望能对大家有所启发。<br>
<br>注：ASI 是 Alibaba Serverless infrastructure 的缩写，是阿里巴巴针对云原生应用设计的统一基础设施。有兴趣可以阅读：<a href="http://mp.weixin.qq.com/s?__biz=MzUzNzYxNjAzMg==&mid=2247498271&idx=1&sn=d18b7abf3ba14aacc7bc0e1028629023&chksm=fae6f1d0cd9178c67368b98161b289a6fb489f745992d0129dbb65edc0c027024ea777370a57&scene=21#wechat_redirect">《揭开阿里巴巴复杂任务资源混合调度技术面纱》</a>。<br>
<br><h1>背景</h1><h2>1. 复杂的场景和曾面临的困境</h2>我们所管理的大规模 ASI 集群场景非常复杂，这为我们的工作带来了极大挑战，任何一个场景处理不慎就有可能导致意料之外的伤害扩大化。<br>
<ul><li><br>从组件维度看，我们目前有几百个组件，每年有几万次的组件变更。频繁的组件变更如何在稳定性和效率之间取得权衡，怎样让变更时更稳定，怎样让灰度更确信，从而降低爆炸半径？</li><li><br>从集群维度看，目前有上千个集群和海量节点，碰到的集群/节点问题较多，监控链路覆盖比较繁复，怎样让集群运行时更加可信?</li><li><br>从二方用户和业务场景看，我们支持了大量的集团二方用户，同时业务场景也非常复杂，怎样保证各有特色的业务场景都能得到一致的细心关照?</li></ul><br>
<br><div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210425/36e6c61fc1f495265c24d2849b77e4a4.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210425/36e6c61fc1f495265c24d2849b77e4a4.png" class="img-polaroid" title="1.png" alt="1.png" referrerpolicy="no-referrer"></a>
</div>
<br>
<br><h2>2. 问题预判和解决思路</h2>基于长期的集群管理经验，我们有如下预设：<br>
<ol><li><br>数据监控作为正向链路，无法无死角覆盖所有场景。即使链路中各个节点的监控数据正常，也不能 100% 保证链路可用。<br>
<ul><li>集群状态每时每刻都在变化，各个组件也在不停地更新升级，同时链路上的每个系统也在不停的变更，监控数据的覆盖永远是正向的追赶，只能逼近 100% 全覆盖而无法完全达到。</li><li>即使整个集群链路中所有组件/节点的监控数据都正常，也不能保证集群链路 100% 可用。就如同业务系统一样，看上去都是可用的，没有问题暴露。但只有通过全链路压测实际探测过整个链路后，才能得到实际可用的结论。</li><li>你要正向证明一个东西可用，需要举证无数的例子。而如果要反向证明不可用，一个反例就够了。数据监控链路只能逼近全覆盖，而无法保证真正全覆盖。</li></ul></li><li><br>大规模场景下，数据无法达到 100% 的完全一致性。<br>
<ul><li>当集群规模足够大时，数据的一致性问题将会愈加显现。比如全局风控组件是否全集群链路覆盖？相关流控配置是否全集群链路推平？pod 主容器时区是否与上层一致？集群客户端节点证书是否有即将过期？等等问题，一旦疏忽，将有可能酿成严重的故障。</li></ul></li></ol><br>
<br>只有弥补上述两类风险点，才能有底气真正做到先于用户发现问题。我们解决上述两类风险的思路分别是：<br>
<ol><li>黑盒探测<br>
<ul>- 所谓黑盒探测，既模拟广义上的用户行为，探测链路是否正常。</ul></li><li>定向巡检<br>
<ul>- 所谓巡检，既检查集群异常指标，找到已有或可能将存在的风险点。</ul></li></ol><br>
<br>基于以上思路，我们设计并实现了 KubeProbe 探测/巡检中心，用于弥补复杂系统的正向监控的不足，帮助我们更好、更快地发现系统风险和线上问题。<br>
<br><h1>设计</h1><h2>黑盒探测和定向巡检</h2><h3><strong>1）黑盒探测</strong></h3>不知道你是否也经历过一条链路上各个系统监控数据都正常，但是实际链路流程就是跑不通。或者因为系统变化快，监控覆盖不到 100% 的场景总是会有遗漏，导致影响到了用户却没有报警，对用户没有实质影响却报警频发从而疲于奔命。<br>
<br>如果一个系统开发者自己都不使用自己的系统，那么怎么可能先于用户发现系统问题呢？所以要先于用户发现系统问题，首先我们自己就得先成为用户，而且一定是使用最多，了解最深，无时无刻不在使用和感知系统状况的用户。<br>
<br>所谓黑盒探测，就是让自己成为自己的用户，模拟广义"用户"的行为去对集群/组件/链路等待待测对象做探测。注意，这里的"用户"并不仅仅是狭义上使用系统的同学，而是广义用户。比如，etcd 的"用户"是 APIServer，而 ASI 的"用户"可能是某个通过 APIServer 操作集群的同学，也可能是 Normandy 发起的发布/扩容/缩容操作。<br>
<br><div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210425/bac6efd4eb07c1d0991cb2e22e94b03a.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210425/bac6efd4eb07c1d0991cb2e22e94b03a.png" class="img-polaroid" title="2.png" alt="2.png" referrerpolicy="no-referrer"></a>
</div>
<br>
<br>我们希望 KubeProbe 能在 变更时（监听到集群状态发生变化/组件变更/组件发布/系统升级等等事件）/运行时（周期，高频）/故障恢复时（手动），通过周期/事件触发/手动触发，执行各种不同类型的黑盒探测，第一时间感知组件/集群/链路的可用性。<br>
<br>以 etcd 集群的可用性来举例，我们可以实现一个探测用例，逻辑是对 etcd 做 create/get/delete/txn 等等操作，并记录每个操作的成功率/消耗时间，当成功率低于 100% 或消耗时间超过容忍阈值后，触发报警。我们将周期高频运行这个 etcd 的探测用例，同时对于 etcd 集群的任何变更都会发出一个事件 event 触发这个 etcd 探测立即运行，这样就能尽量确保第一时间发现 etcd 可用性故障了。同时，当 etcd 集群因为某些原因不可用了，我们也可以通过手动触发等其他方式做探活，也能第一时间得到是否恢复的信息。<br>
<br><h3><strong>2）定向巡检</strong></h3>在大规模集集群/系统场景下，数据一致性是一定会面临的难题。数据不一致，将导致一些隐患，可能会在未来引发某些确定性的故障。<br>
<br>相比于黑盒探测面对的未知故障场景，定向巡检的目标是对集群的已知风险点做扫描。<br>
<br><div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210425/fe6cfabc9aa7249d4e8c22ccbf7027d2.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210425/fe6cfabc9aa7249d4e8c22ccbf7027d2.png" class="img-polaroid" title="3.png" alt="3.png" referrerpolicy="no-referrer"></a>
</div>
<br>
<br>我们希望 KubeProbe 能够定期对整个集群/链路做定向的巡检，找出这些数据不一致的点，判断数据不一致是否可能引发风险，从而能够防患于未然，治未病。<br>
<br>比如 etcd 冷热备多集群覆盖不全，可能导致集群遇到故障无法快速恢复。那么我们就定期对 etcd 的冷热备覆盖情况做定向巡检，找出没有覆盖推平的集群，并告警。比如 集群风控系统没有全集群链路覆盖，限流配置没有全集群链路推平，可能导致某些故障场景引发集群全面崩溃，我们定期对风控配置全网扫描，判断是否可能导致故障，找出这些隐藏的已知风险点并告警。<br>
<br><h1>实现</h1><h2>1. 架构</h2><h3><strong>1）基本架构</strong></h3>KubeProbe 的基本实现架构大致如下图，KubeProbe 中心端配置集群/集群组与巡检/探测用例/用例集之间的关联关系，负责对集群做具体某次探测实例下发。某个具体的巡检/探测用例下发到具体某个集群将使用用例的镜像创建一个 pod，这个 pod 里会执行若干巡检/探测逻辑，当执行完成后会回调中心端回写本次巡检/探测结果。其具体结果在中心端统一展示/告警，并提供给其他消费者消费（如支持 ASIOps 平台的发布阻断）。<br>
<br><div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210425/8cf132179571d320490d044f7648f45c.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210425/8cf132179571d320490d044f7648f45c.png" class="img-polaroid" title="4.png" alt="4.png" referrerpolicy="no-referrer"></a>
</div>
<br>
<br><h3><strong>2）高频架构</strong></h3>除了上述的基本架构之外，我们对于高频探测用例（既探测周期短，触发频率需要非常频繁，甚至保持无缝探测的场景）设计了一套集群内的分布式常驻探测架构，该架构通过集群内的 ProbeOperator 组件 watch 自定义对象 probeConfig 的变化，在集群内创建一个常驻的探测 pod，将持续无间断的运行探测逻辑，实现接近无缝的持续探测，并将结果通过去噪/令牌桶限流等处理后，上报中心端，共给其他消费者消费。<br>
<br><div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210425/19c75ebc06f0bc8bded4234888014af6.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210425/19c75ebc06f0bc8bded4234888014af6.png" class="img-polaroid" title="5.png" alt="5.png" referrerpolicy="no-referrer"></a>
</div>
<br>
<br><h2>2. KubeProbe 探测/巡检用例管理</h2>所有的探测/巡检用例都使用统一的 git 仓库管理，由我们提供一个统一的 client 库，client 库最核心提供的方法主要有两个。<br>
<br>```<br>
KPclient "gitlab.alibaba-inc.com/&#123;sigma-inf&#125;/&#123;kubeProbe&#125;/client"<br>
<br>// 报告成功<br>
// 此方法会向KubeProbe报告本次巡检结果为成功<br>
KPclient.ReportSuccess()<br>
os.Exit(0)<br>
<br>// 报告失败<br>
// 报告方法会向KubeProbe报告本次巡检结果为失败，并且失败信息为 <code class="prettyprint">我失败啦</code><br>
KPclient.ReportFailure([]string&#123;"我失败啦!"&#125;)<br>
os.Exit(1)<br>
```<br>
<br>我们可以通过提供好的 Makefile 将这个用例打包成镜像，录入 KubeProbe 中心端就可以对集群做配置和下发了。将具体巡检/探测逻辑和 KubeProbe 中心管控端解耦，可以灵活而又简便的让更多的二方用户接入自己的特殊巡检/探测逻辑。<br>
<br>目前已经使用的探测/巡检用例包括：<br>
<ul><li>通用探测：模拟 pod / deployment / statefulset 生命周期探测集群整条管控链路。</li><li>etcd 黑盒探测：模拟 etcd 的基本操作，探测元集群中各 etcd 状态。</li><li>金丝雀探测（感谢质量技术同学的大力支持）：模拟用户使用 ASI 的部署场景，实现金丝雀应用的全链路模拟发布/扩容/缩容。</li><li>Virtual cluster 探测：探测 vc 虚拟集群的管控链路状态。</li><li>联邦链路探测：探测联邦控制器相关链路的状态。</li><li>节点通用探测：在集群每个节点上模拟调度一个探测 pod，探测节点侧链路状态。</li><li>ASI 客户端/服务端证书巡检：检查客户端/服务端证书有效性以及到期时间是否已超过告警阈值。</li><li>全局风控限流巡检：检查各 ASI 集群是否已经推平并开启 KubeDefender 全局限流风控配置。</li><li>······</li></ul><br>
<br><h2>3. KubeProbe 中心端管控</h2>编写完成探测/巡检用例，并打包上传好镜像后，就需要在 KubeProbe 中心端注册这个用例模版，即将镜像注册进 KubeProbe 中心端的数据库中。<br>
<br>我们可以通过"渲染配置"参数传入一些指定的 env 环境变量到巡检/探测 pod 中，用于执行不同的业务逻辑，实现同一个用例模版生成多个用例。<br>
<br>最后通过统一的配置管控将用例和集群做绑定，配置对应的参数，执行各种下发逻辑。<br>
<br><div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210425/b14821c921e8597bc250664297484a93.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210425/b14821c921e8597bc250664297484a93.png" class="img-polaroid" title="6.png" alt="6.png" referrerpolicy="no-referrer"></a>
</div>
<br>
<br>同时，我们还在 KubeProbe 中心端做了大量权限安全管控，脏数据资源清理以及提效增速的工作（比如采用完全以 ownerreferences 的巡检/探测用例资源自动清理能力等等），这里不再赘述。<br>
<br><h2>4. 打通发布 / 变更阻断</h2>我们打通了 KubeProbe 探测与发布变更的关联，当对应集群中有任何变更发生时（如某组件在做发布），我们会自动通过相应的事件触发此集群绑定的所有巡检/探测用例，检查集群状态是否正常。如果探测失败，则会将变更阻断，降低爆炸半径，提升集群变更时稳定性。<br>
<br><h2>5. 为什么不使用 Kuberhealthy</h2>社区有一个 Operator 叫 Kuberhealthy 也可以做类似的事情，我们曾经也考虑采用，并且深度使用过 Kuberhealthy 和参与 kuberhealthy 的社区贡献，最终得出不适合的结论，主要原因是对大规模集群的支持较弱，同时高频调用时主流程卡死问题比较严重，不支持事件/手动单次触发特性，不支持统一上报数据中心等等，最终选择了自研自建的方式，目前来看是一个比较正确的选择。<br>
<br><h1>一点小结果</h1>KubeProbe 上线以来，实现探测/巡检用例几十个，在集团数百个 ASI 集群中运行千万余次，主动发现集群故障和问题百余次，其中某些小故障一旦没有发觉很有可能升级成为大故障，有效降低了系统风险。同时打通了变更/发布系统，提升了变更稳定性。并且在特殊故障时，多次先于业务方提前发现问题，更早地推动解决问题，客观降低了故障损失。<br>
<br>下面是一个具体例子:<br>
<ul><li>我们会接收到每个集群中各个组件的发布事件，由发布事件触发我们会在对应集群中运行相关的巡检/探测，比如调度一个定向的 pod 到某个节点组件发布的节点上去。我们发现 kube-proxy 的发布会导致节点的短暂不可用，调度上去的 pod 无法创建成功，从简单的返回/日志/集群事件上看不出具体的问题，并且持续复现。经过深入排查，得知是 kube-proxy 的问题，存在 netns 泄露。运行久了会泄露，当 kube-proxy 重启的时候，内核要清理 netns，会卡一段时间来清理，导致节点一段时间链路不通，pod 可以调度上去但是运行不起来，从而后续推进了 kube-proxy 的问题修复。</li></ul><br>
<br><div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210425/569cf56902c6329238d26de71f41a3db.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210425/569cf56902c6329238d26de71f41a3db.png" class="img-polaroid" title="7.png" alt="7.png" referrerpolicy="no-referrer"></a>
</div>
<br>
<br><div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210425/7543eca418b7ea51526976e966cded25.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210425/7543eca418b7ea51526976e966cded25.png" class="img-polaroid" title="8.png" alt="8.png" referrerpolicy="no-referrer"></a>
</div>
<br>
<br><h1>发现问题之后</h1><h2>1. KubeProbe 和数据监控的告警区别</h2>KubeProbe 所面对的场景和数据监控不同，更多偏向于链路探测。<br>
<br>比如，监控告警一般的告警可能如下：<br>
<ul><li>xx容器内存使用率 99%</li><li>webhook 双副本全部挂掉了</li><li>apiserver 三副本全部宕机了</li></ul><br>
<br>这些告警，往往内容中就包含了具体的故障点，而 KubeProbe 的链路探测告警就有很多不一样，比如：<br>
<ul><li>Statefulset 链路探测失败，Failed to create pod sandbox: rpc error: code = Unknown</li><li>etcd 全流程黑盒探测失败，context deadline exceeded</li><li>CloneSet 扩容失败，connect: connection refused</li></ul><br>
<br>这些 KubeProbe 的告警往往比较难从字面看出到底这次巡检/探测是为什么失败了，我们往往需要根据相关的用例返回日志，巡检/探测 pod 日志，KubeProbe 相关集群事件综合排查，定位失败原因。<br>
<br><h2>2. 根因定位</h2>我们以比较混沌的 KubeProbe 探测失败告警作为线索，构建了一套 KubeProbe 自闭环的根因定位系统，将问题排查的专家经验下沉进系统中，实现了快速和自动的问题定位功能，一个简单的定位规则如下：<br>
<br><div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210425/de89dfd074f08e9824c58e9fef0be302.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210425/de89dfd074f08e9824c58e9fef0be302.png" class="img-polaroid" title="9.png" alt="9.png" referrerpolicy="no-referrer"></a>
</div>
<br>
<br>我们会通过普通的根因分析树以及对失败巡检探测事件/日志的机器学习分类算法（持续开发投入中），为每一个 KubeProbe 的探测失败 Case 做根因定位，并通过 KubeProbe 内统一实现的问题严重性评估系统（目前这里的规则仍比较简单），为告警的严重性做评估，从而判断应该如何做后续的处理适宜，比如是否自愈，是否电话告警等等。<br>
<br><h2>3. Oncall 和 ChatOps</h2>有了上面提到的根因定位以及告警严重性评估系统，我们使用了 nlp 告警机器人，实现了一套自动化的 Oncall 系统以及 ChatOps，展示一些使用的 case 如下，通过 ChatOps 和 Oncall 机器人，极大的降低了问题处理的复杂度，尽量用技术的手段解决重复的问题。<br>
<br><div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210425/f143f18cd0b4388f586dc9ccfa4e18aa.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210425/f143f18cd0b4388f586dc9ccfa4e18aa.png" class="img-polaroid" title="10.png" alt="10.png" referrerpolicy="no-referrer"></a>
</div>
<br>
<br><div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210425/10e1f8aeb30aa3a74ad1c561d2d6a05c.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210425/10e1f8aeb30aa3a74ad1c561d2d6a05c.png" class="img-polaroid" title="11.png" alt="11.png" referrerpolicy="no-referrer"></a>
</div>
<br>
<br><div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210425/a283cf81de6db7db5ecbe85497845068.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210425/a283cf81de6db7db5ecbe85497845068.png" class="img-polaroid" title="12.png" alt="12.png" referrerpolicy="no-referrer"></a>
</div>
<br>
<br><h1>我们仍在路上</h1>以上是我们在管理大规模 Kubernetes 集群中的一点经验，也解决了一些常见的问题，希望能对大家有所帮助。同时，这些工作在阿里云海量规模的场景下还需要持续打磨，我们仍在路上，并且将持续在路上。
                                                                <div class="aw-upload-img-list">
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                </div>
                                
                                                                <ul class="aw-upload-file-list">
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    </ul>
                                                              
</div>
            