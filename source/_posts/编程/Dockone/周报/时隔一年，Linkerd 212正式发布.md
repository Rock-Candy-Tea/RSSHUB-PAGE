
---
title: '时隔一年，Linkerd 2.12正式发布'
categories: 
 - 编程
 - Dockone
 - 周报
headimg: 'https://picsum.photos/400/300?random=1524'
author: Dockone
comments: false
date: 2022-09-04 09:08:58
thumbnail: 'https://picsum.photos/400/300?random=1524'
---

<div>   
<br>时隔将近一年Linkerd 2.12终于发布了。这个庞大的版本为Linkerd引入了基于路由的策略，允许用户以完全零信任的方式定义和执行基于HTTP路由的授权策略。这些策略建立在Linkerd强大的工作负载身份之上，由双向TLS保护，并使用来自Kubernetes新<a href="https://gateway-api.sigs.k8s.io/">Gateway API</a>的类型进行配置。<br>
<br>Linkerd 2.12是采用Gateway API作为核心配置机制的第一步。虽然这个API对于服务网格用例来说还不是很完美，但它为这个版本提供了一个强大的起点，我们乐观地认为它们会随着时间的推移而发展，以满足Linkerd的需求。重要的是，在Gateway API的基础上构建将使我们能够将特定于Linkerd的配置对象的数量保持在最低限度，即使我们引入了新功能——这可能是我们成为Kubernetes最简单和最轻的服务网格目标的重要组成部分。<br>
<br>新版本还引入了访问日志记录，这是一个令人期待已久的功能，允许Linkerd生成Apache样式的请求日志。它增加了对iptables-nft的支持，并引入了许多其他改进和性能提升。<br>
<br>Buoyant Cloud客户现在可以将他们的2.10+或更高版本的集群全自动升级到Linkerd 2.12，包括数据平面代理。（仅限商业和企业层。）<br>
<br>新版本的发布包含了50多名贡献者的大量辛勤工作，其中包括Timescale、Adidas、Sourcegraph、Intel、Shopify、Red Hat等的工程师。特别感谢Agrim Prasad、Ahmed Al-Hulaibi、Aleksandr Tarasov、Alexander Berger、Ao Chen、Badis Merabet、Crevil (Bjørn)、Brian Dunnigan、Christian Schlotter、Dani Baeyens、David Symons、Dmitrii Ermakov、Elvin Efendi、Eng Zer Jun、Gustavo Fernandes de Carvalho、Harry Walter、Israel Miller、Jack Gill、Jacob Henner、Jacob Lorenzen、Joakim Roubert、Josh Ault、João Soares、Kim Christensen、Krzysztof Dryś、Lior Yantovski、Martin Anker Have、Michael Lin、Michał Romanowski、Naveen Nalam、Nick Calibey、Nikola Brdaroski、Or Shachar、Pål-Magnus Slåtto、Raman Gupta、Ricardo Gândara Pinto、Roberth Strand、Sankalp Rangare、Sascha Grunert、Steve Gray、Steve Zhang、Takumi Sue、Tanmay Bhat、Táskai Dominik、Ujjwal Goyal、Weichung Shaw、Wim de Groot、Yannick Utard、Yurii Dzobak和罗泽轩，感谢你们的辛勤工作！<br>
<br><h3>Per-route策略</h3>Linkerd的新的per-route策略扩展了现有的基于端口的策略，对服务之间的通信方式进行了更细粒度的控制。这些策略是为采用零信任安全方法的组织设计的，这些方法不仅需要加密，还需要强大的工作负载身份和无处不在的明确授权Linkerd的授权策略：<br>
<ul><li>将网络视为对抗性的。它们不依赖IP地址，也不要求CNI层或底层网络的任何其他方面是安全的。</li><li>使用安全的工作负载身份。Linkerd的工作负载身份自动从ServiceAccounts派生，并在连接时通过双向TLS进行加密验证。</li><li>在Pod级别强制执行。每个连接和每个请求都经过验证。</li><li>轻松允许<em>默认拒绝</em>模式。默认情况下，具有安全意识的采用者可以轻松地禁止访问敏感资源，除非明确允许（“最小特权原则”）。</li></ul><br>
<br>由于运行状况和就绪探测需要在未经授权的情况下通过，因此在Kubernetes中完成默认拒绝设置可能会很棘手。在Linkerd 2.12中，健康和就绪探测现在默认授权，但也可以显式授权，同时仍锁定其他应用程序端点。（查看<a href="https://linkerd.io/2.12/features/server-policy/">完整的策略文档 »</a>）<br>
<br><h3>Gateway API</h3>Linkerd 2.12为支持Kubernetes Gateway API 迈出了第一步。虽然Gateway API最初被设计为Kubernetes中长期存在的Ingress资源更丰富、更灵活的替代方案，但它为描述服务网格流量提供了良好的基础，并允许Linkerd将其添加的配置机制保持在最低限度。<br>
<br>在Linkerd 2.12中，第一步是谨慎的：Linkerd提供了部分Gateway API（例如 CRD，诸如<a href="https://gateway-api.sigs.k8s.io/api-types/httproute/">HTTPRoute</a>之类的）的部分实现，以配置Linkerd的基于路由的策略。这种方法允许我们开始使用Gateway API类型，而无需实现对Linkerd没有意义的规范部分。随着Gateway API的发展以更好地满足Linkerd的需求，我们的意图能以一种最小化用户摩擦的方式切换到源类型。<br>
<br><h3>访问记录</h3>Linkerd 2.12还引入了访问日志记录，它允许代理选择性地发出Apache样式的请求日志。出于性能和资源利用率的原因，此功能默认关闭（尤其是对于高流量工作负载），但可以在需要它的情况下轻松启用。（请参阅<a href="https://linkerd.io/2.12/features/access-logging/">访问记录文档 »</a>）<br>
<br><h3>使用Buoyant Cloud进行全自动升级和回滚</h3>除了Linkerd 2.12版本之外，我们的托管Linkerd服务Buoyant Cloud现在支持（几乎）任何运行2.10.0及更高版本的集群自动升级到Linkerd 2.12。此升级过程涵盖控制平面和数据平面，你只需更改CRD即可跨任意数量的集群保持Linkerd部署的最新状态。<br>
<br>和以前一样，Buoyant Cloud与（几乎）在你的基础设施上运行的任何Linkerd集群一起运行。只需将Buoyant Cloud代理与你现有的开源Linkerd安装一起部署，并获得自动健康警报、升级和回滚、策略分析等等。<br>
<br><h3>其他更新</h3>Linkerd 2.12还有大量其他改进、性能提升和错误修复，包括：<br>
<ul><li>一个新的<code class="prettyprint">config.linkerd.io/shutdown-grace-period</code>注释，用于配置代理的最大宽限期以进行正常关闭</li><li>Linkerd的init容器中用于iptables-nft支持的新<code class="prettyprint">iptables-nft</code>模式</li><li>修复了在信任根轮换后未根据需要重新启动的某些控制平面组件</li><li>修复了在Linkerd命名空间中发现意外Pod时“linkerd check”命令崩溃的问题</li><li>更改了<code class="prettyprint">proxy.await</code> Helm值，以便用户现在可以在控制平面组件上禁用<code class="prettyprint">linkerd-await</code></li><li>允许自动缩放器在必要时驱逐Linkerd扩展部署的注释</li><li>在非链接（独立）模式下运行Linkerd CNI插件的能力</li><li>多集群扩展中的ServiceAccount令牌Secret以支持Kubernetes版本 >= v1.24</li><li>还有更多！</li></ul><br>
<br>有关详细信息，请参阅<a href="https://github.com/linkerd/linkerd2/releases/tag/stable-2.12.0">完整的发行说明</a>。<br>
<br><h3>Linkerd 的下一步是什么？</h3>2022年对于Linkerd来说又是不可思议的一年。去年，Linkerd成为第一个也是唯一一个在CNCF中毕业的服务网格，加入了Kubernetes、Prometheus和Envoy等项目所在的基金会，成为高成熟度的热门项目。今年早些时候，我们宣布了<a href="https://linkerd.io/2022/03/09/announcing-automated-multi-cluster-failover-for-kubernetes/">Linkerd 跨集群故障转移的可用性</a>；CNCF调查<a href="https://linkerd.io/2022/02/16/linkerd-istio-adoption/">结果显示，Linkerd在美国和欧盟的采用率超过了Istio ，以及</a><a href="https://linkerd.io/2022/06/27/announcing-the-completion-of-linkerds-2022-security-audit/">Linkerd 2022年安全审计</a>的竞争。<br>
<br>在接下来的几个Linkerd版本中，我们将致力于开发足以令人兴奋的客户端策略功能，例如断路和基于标头的路由，以及长期功能，例如网格扩展，以允许数据平面在Kubernetes之外运行。当然，如果你有功能要求，<a href="https://slack.linkerd.io/">我们很乐意听到</a>！<br>
<br><h3>Linkerd 适合所有人</h3>Linkerd是CNCF的毕业项目。Linkerd由Buoyant创建，100%开源。如果你有功能请求、问题或意见，我们很乐意你加入我们快速发展的社区！Linkerd托管在<a href="https://github.com/linkerd/">GitHub上</a>，我们在<a href="https://slack.linkerd.io/">Slack</a>、<a href="https://twitter.com/linkerd">Twitter</a>和<a href="https://linkerd.io/community/get-involved/">邮件列表</a>上有一个蓬勃发展的社区。快来加入乐趣吧！<br>
<br><strong>原文链接：<a href="https://buoyant.io/blog/announcing-linkerd-2-12">Announcing Linkerd 2.12: Zero-trust route-based policy, Gateway API, access logging, and more!</a></strong>
                                
                                                              
</div>
            