
---
title: '闲鱼单体应用Serverless化拆分实践'
categories: 
 - 编程
 - 掘金
 - 标签
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/3e412c559639448c8157900f652b29a9~tplv-k3u1fbpfcp-zoom-1.image'
author: 掘金
comments: false
date: Mon, 10 May 2021 19:14:48 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/3e412c559639448c8157900f652b29a9~tplv-k3u1fbpfcp-zoom-1.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>作者：闲鱼技术——柬超</p>
<h2 data-id="heading-0">背景</h2>
<p>2018，我们在实践中提出了flutter+Dart Faas的云端一体化研发解决方案，该方案借助Serverless 轻（聚焦业务）、快（单个接口单个函数，研发、部署快）、NoOps（运维平台化）的能力，降低了服务端业务组装层的研发门槛，使得客户端同学也能够有能力有机会参与到服务端业务开发中，减少了客户端服务端协作效率问题，提升了新兴业务的迭代效率。但是在闲鱼传统应用架构中，也存在着类似业务组装层，这个应用的名字叫idleapi。<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/3e412c559639448c8157900f652b29a9~tplv-k3u1fbpfcp-zoom-1.image" alt="undefined" title="null" loading="lazy" referrerpolicy="no-referrer">由于应用的垂直业务边界划分和架构分层设计不清晰，近乎所有业务都在idleapi上迭代。新的业务不断累加，老的业务不断迭代，过期的业务又得不到及时的清理，导致应用规模不断膨胀。据统计，截止2020年双十一，Idleapi对外提供了1200多个网关接口，其中有500多个是没有业务流量的（业务下线），但是代码依然还在运行，没有及时清理。 导致idleapi总共有70w+行代码，2k+个业务开关，上百个业务模块。这么多业务、代码、开发都耦合在一个应用上，引发了一些列的隔离性问题：</p>
<h3 data-id="heading-1">线上稳定性：</h3>
<p>上百个业务模块运行在一个应用进程中，相互干扰，容易引发隔离性问题。例如一个业务模块出现问题（将内存耗尽或者将线程池占满），就会导致部署在同一台机器上的其他业务模块无资源可用，拒绝服务，连累了同机部署的核心业务，就会引发故障。这样的例子每年都会有。</p>
<h3 data-id="heading-2">研发效率低：</h3>
<p>几十个研发同学开发维护上百个业务模块，每次发布都会有十几分支，每增加一个业务分支，都会面临代码冲突的风险，分支的基线版本与其他分支的基线版本差距越大，要解决的冲突也就越多，消耗的时间也就越久。据统计，Idleapi预发发布一次需要30分钟左右，其中有20分钟是在等开发同学解决冲突，开发效率低下。</p>
<h3 data-id="heading-3">业务垂直化冲突：</h3>
<p>为了更好的发展业务，关注业务指标，闲鱼按照业务域重新组合了人员结构，但是应用结构还来不及跟进。同一业务组内部虽然能够自治内聚，有效沟通，但是当所有业务耦合在一个应用中时，业务间仍然需要大量精力跨组协同</p>
<h2 data-id="heading-4">治理--拆分</h2>
<p>The structures of large systems tend to disintegrate during development, qualitatively more so than with small systems. Organizations which design systems are constrained to produce designs which are copies of the communication structures of these organizations. 根据康威定律：大的系统总是在发展中趋于分解、重组，以达到系统架构和人员结构的某种同态。为了解决idleapi存在的各种问题，我们决定对它进行拆分。拆分过程中，有几个问题必须要提前考虑清楚：<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/6535de3144db4f84b8cf223a7bac5a90~tplv-k3u1fbpfcp-zoom-1.image" alt="undefined" title="null" loading="lazy" referrerpolicy="no-referrer"></p>
<p>1. 拆分的产物是什么？是按业务域划分的传统的单体应用，还是以业务接口为单位的FaaS函数？2. 拆分过程中，业务代码是全部重写还是复用？如何处理冗余的业务代码？3. 业务的配置、监控、告警如何迁移？4. 如何快速验证？5. 如何平滑灰度？如何回滚？业务迁移过程中，新的需求如何处理？6. 应用上线后，是否有措施防止再次出现应用/Faas膨胀问题？ 上述几个问题是拆分流程的关键点，决定着拆分方案能否成功的落地执行。接下来我们逐个分析下：</p>
<h2 data-id="heading-5">传统应用 VS FaaS函数</h2>
<p>拆分要解决的第一个方向性问题: 拆分的目标产物是什么？思路大致有两个:1. 按照业务域拆分成一个一个小的传统的应用，独立研发部署运维；2. 以照网关接口为单位，拆分为一个个对应的FaaS函数。根据这几年的探索和对比：我们认为FaaS非常适合解决Idleapi遇到的问题。<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/db4285c933c44b7b9a90fd5ba4ee310b~tplv-k3u1fbpfcp-zoom-1.image" alt="undefined" title="null" loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-6">调试期</h3>
<p>首先在调试期，传统应用下，多个接口在一个应用上并行开发，不同分支代码发布时存在代码合并冲突的风险，且预发部署一次大概需要30分钟左右。 而在Faas下，一个网关接口，对应一个Faas函数，每个Faas 函数有自己独立的git仓库和部署环境。Faas之间相互独立，物理隔离，开发同学可以放心修改自己的代码和基线版本，也可以随时发起远程Debug，而不用担心妨碍其他开发同学调试。而且由于每个Faas函数只聚焦于一个业务网关接口，FaaS函数的代码量和依赖的二方服务远小于传统应用，因此预发部署一次只需要3分钟，比传统应用快近10倍。</p>
<h3 data-id="heading-7">运行期</h3>
<p>在运行期，每个Faas函数运行在不同的集群上，这种天然的物理隔离性，使得FaaS函数不会引发隔离性故障。一个Faas函数上面的业务耗尽线程池、写爆磁盘，都不会影响部署在其集群上面的函数（业务关联除外）。</p>
<h3 data-id="heading-8">编码期：</h3>
<p>虽然Faas函数在调试期，运行期，运维期都占据优势，但是传统的单体应用在编码期占据优势，例如： 代码复用性：多个业务的代码在一个工程仓库里面，底层的工具类、manager类，上层业务都可以直接调用，代码复用简单直接；而FaaS模式下，不同的网关接口分别在不同的代码仓库中，代码复用：需要代码拷贝或者公共代码下沉到二方包或者领域服务中，又会引起代码维护问题。 软件版本升级：当Pandora或者二方包必须要升级时： 传统应用只需要升级该应用依赖的软件版本，重新发布就可以解决升级问题。而在FaaS模式下：如果每个函数都需要业务开发同学逐个修改和发布，重复劳动的工作量会是传统应用的上百倍，十分影响开发效率。我们也在尝试通过一些平台化的工具或者分层的措施等方案来解决这个难题。</p>
<h2 data-id="heading-9">拆分工具</h2>
<p>拆分方案确定后，idleapi将由一个巨型单体应用，被拆分成几百个以网关接口为单位的FaaS函数。这么多的业务重新实现一份是不现实的，所以最佳方式是复用单体应用中的业务代码。<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/246be8f225384bd699f29ff1be95c07a~tplv-k3u1fbpfcp-zoom-1.image" alt="undefined" title="null" loading="lazy" referrerpolicy="no-referrer">对代码分析后，我们发现idleapi中，各业务的代码相互引用，形成了一个错综复杂的巨型网状结构。一个业务接口关联了五个甚至十个其他业务接口的代码，牵涉的源文件数近1000，占idleapi代码源文件总量的1/4，完全没有达到我们简化业务代码的目的。而且除了业务网关入口外，还存在着其他各种隐式的函数入口，比如：json序列化会自动调用类的set函数等，Bean的初始化函数等等。对人工拆分业务代码提出了很大的挑战。 为此，我们设计和实现了一个代码拆分工具，能够帮助业务在交织如麻的代码中，分析出业务入口函数所依赖的类、方法和属性，排除没有调用到的类、方法和属性。该工具能够将单个业务入口所依赖的源文件数量进一步降低到100左右，（其中70%是接口数据类型）。结合我们设计实现的Faas业务框架，业务同学迁移时，能够一键拆分出业务代码、创建Faas函数，并部署到预发环境，整个过程耗时半小时以内。 对于业务开关配置，我们也提供了迁移工具，能够一键将线上或者预发的配置批量迁移到新的函数，免去人工迁移需要逐个审批拷贝的重复劳动。</p>
<h2 data-id="heading-10">自动化回归测试</h2>
<p>测试是保障拆分出的业务代码质量的最后一道屏障。为了降低应用拆分给业务和测试同学带来的额外工作量，我们协同Faas平台和自动化回归测试平台，将录制回放等回归测试功能，适配到Faas平台的SideCar和Pod架构。开发同学只需要在FaaS函数发布后，在传统应用中录制线上流量，然后把流量导入待测FaaS函数进行自动化回归测试。 通过对接自动化测试平台，开发同学可以自助完成业务的回归测试。降低了业务迁移的风险和测试同学的测试压力，提升迁移的效率。</p>
<h2 data-id="heading-11">运维</h2>
<p>在FaaS业务的运维方面，我们尽量保留开发同学的运维习惯：拆分出的FaaS函数保留了单体应用中日志的名称、日志的组织格式、编码等等，也保留了开发同学登录远程机器的能力。同时，我们将业务个性化日志适配到Faas平台的白屏化日志功能，开发同学可以通过管控平台查看搜索任意机器上的所有日志，相比登陆机器逐个查看，提效很多。同时，基于日志的监控告警系统只需要更新下相关监控的业务日志路径就能够完成监控的迁移。<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/bfa428a228084b588158f27f9507c112~tplv-k3u1fbpfcp-zoom-1.image" alt="undefined" title="null" loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-12">架构演进</h2>
<p>对于应用拆分为细粒度Faas函数后，业务代码复用问题，解决方案大致有两种思路： 一．先治理再拆分：先对单体应用进行改造重构，把各业务复用的代码下沉（下沉到公共二方包或下沉到该业务领域服务层），然后再吧单体应用拆分为多个Faas函数。这个方案存在2个问题：1. 僵尸代码占比仅一半，会带来无效的重构工作量，2. 原有应用上进行重构，新的业务迭代和重构AB混杂在一起做开发、做灰度，复杂度高，风险大。 二．先拆分后治理：先对单体应用进行业务拆分，暂时忽略代码复用的问题，等函数拆分之后，有业务同学在后续的开发过程中，根据实际业务需要进行代码复用改造。将业务复用代码或独立为工作二方包，或下沉到领域服务中。相比第一种方案，在隔离清晰的函数代码库之间梳理复用性问题，复杂度和风险会小很多。因此，我们选择了第二种方案。<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/456d03b83a374ed29461303600de01e4~tplv-k3u1fbpfcp-zoom-1.image" alt="undefined" title="null" loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-13">收益</h2>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/a27d4919183d4bc5ab74691d54d32458~tplv-k3u1fbpfcp-zoom-1.image" alt="undefined" title="null" loading="lazy" referrerpolicy="no-referrer">目前已经有30+个网关接口从单体应用中拆分出来，并交付业务开发维护，进一步验证了该方案在单体应用的拆分治理方面是可行的。后续我们会将拆分方案提供给开发同学，由开发同学自行拆分迁移业务。拆分后，业务保留了原有的开发运维习惯。 同时，一个业务网关接口对应一个函数的规则，使得一个Faas函数只聚焦于一个业务网关接口，解决了业务不断推陈出新的场景下传统应用不断膨胀的难题。这种聚焦性，也使得函数代码量只有传统应用的3%不到（且以数据类居多），业务发布一次仅需要5分钟（Java）</p>
<h2 data-id="heading-14">总结</h2>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/d35eb69c4916422ba4a294a040fbe52f~tplv-k3u1fbpfcp-zoom-1.image" alt="undefined" title="null" loading="lazy" referrerpolicy="no-referrer"></p>
<p>总体来看，借助自动化拆分工具，业务同学能够在半小时内一键拆分出一个业务接口，并预发部署，中间过程不需要人工干预，且拆分出的函数保持了原有开发运维习惯，迁移成本低，能够被业务同学接受。而且借助函数的业务聚焦性，一个接口一个函数，各函数在开发期没有其他业务的干扰，可测性高，部署速度快。在运行期，各函数运行在不同的物理机，这种天然的物理隔离，大幅提升了运行期的稳定性，降低了业务的运维成本。</p>
<h2 data-id="heading-15">展望</h2>
<p>目前Faas函数平台还在快速发展中，还存在着一些待改进的地方： 机器成本 小流量函数机器成本高：在集团安全生产的高要求下，即使是小流量函数，也需要每个机房两台机器，浪费严重，平台正在考虑通过降低机器规格和超卖等多种措施提升机器利用率。 弹性：在业务上下游链路比较长的情况下，单点的弹性并不能解决所有问题，这需要通盘考虑和解决。 维护成本 统一升级：在集团卡口发布时，每个函数都需要修复问题重新发布，这是一个巨大的工作量，相关解决方案我们正在探索实践中。</p></div>  
</div>
            