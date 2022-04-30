
---
title: '四大功能！带你初识 Fabric _ 容器网络系列第2期'
categories: 
 - 编程
 - Dockone
 - 周报
headimg: 'https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20220329/9fbb11442efa1f0f50e1b81e6d8da923.png'
author: Dockone
comments: false
date: 2022-04-30 11:08:19
thumbnail: 'https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20220329/9fbb11442efa1f0f50e1b81e6d8da923.png'
---

<div>   
<br><h2>容器网络系列：第二期</h2>随着 Kubernetes 社区的发展，实际生产环境中使用 Kubernetes 越来越多，用户对 CNI (Container Network Interface) 的要求也越来越多。Fabric 作为博云自研的一款成熟的 CNI 产品，旨在提供能适应多种场景，功能丰富易用且性能卓越的容器网络管理平台，从而有效的回应用户对于 CNI 的期待。<br>
<br>本期我们将着重介绍 Fabric 的一些常用基础功能。<br>
<br><h2>一、IP/MAC 固定</h2><strong>1.1 使用场景</strong><br>
- 保证 Pod IP/MAC 不变<br>
<br>Kubernetes 具有很高的容错性，例如，当集群中的某一节点发生故障时，pod 会自动漂移到其它正常的节点，这样就保证了业务的可用性，不再需要手动到对应的节点启动容器。但是 pod 在其它节点启动的过程中会重新申请 IP/MAC 地址，如果不支持 IP/MAC 固定的 CNI, pod 的 IP 地址很容易发生改变，这对很多强依赖 IP/MAC 的业务（如: 数据库服务, 微服务网关等）来说是不可接受的。<br>
<br>固定 IP/MAC 使漂移后的 pod 可以保持原有的身份发生网络访问，提高了业务可用性，保证了关联业务都能正常与之发生访问。<br>
<ul><li>简化相关网络策略的配置</li></ul><br>
<br>在一些安全策略把控严格的企业中，针对特定的业务 pod 开通外围的网络策略就变得稍显复杂。此时，如果业务 pod 的身份信息无法固定，则意味着 pod 重建或者发生漂移后对应的网络策略都要发生变更， 这对于运维工程师来说无疑是极为头疼的。因此，固定 IP/MAC 应运而生，这大大简化了网络策略的配置，并降低了维护成本。<br>
<br><strong>1.2 产品特点</strong><br>
Fabric 固定 IP/MAC 的功能有如下特点：<br>
<br>(1) 更灵活的 IP/MAC 预约池，只要 IP/MAC 未被使用就能加入预约池。<br>
<br>(2) CRD 设计，更符合 Kubernetes 的设计原则。<br>
<br>(3) 支持常见的 Kubernetes Workload。<br>
<br>(4) Namespace 级别的安全隔离，不同的租户可以使用不同的 IP/MAC 预约池。<br>
<br>(5) 预约池可以根据使用需求动态扩缩容。<br>
<br>(6) 对于无状态服务，每次分配会从 IP 池中随机分配；对于有状态的 Statefulset 类型应用，每个 Pod 实例会获取整个生命周期固定的 IP 地址。<br>
<br><strong>1.3 实现原理</strong><br>
集群中的 Pod 在某一节点被创建时，Kubelet 都会通过 CNI 去请求分配 IP，Fabric CNI 会通过 http 请求的方式向 fabric api-server 发送申请 IP 的请求。当 fabric api-server 收到申请 IP 的请求之后，首先会根据请求中的 pod 信息去查看 pod 对应的 annotation，判断 annotation 是否绑定 IP/MAC 预约池（即判断是否需要固定 IP/MAC）。如果没有绑定 IP/MAC 预约池则正常分配 IP，如果存在 IP/MAC 预约池，则使用 IP/MAC 预约池中的 IP/MAC，即完成固定 IP/MAC。<br>
<br>基本固定 IP/MAC 流程如图 1 所示：<br>
<br><div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20220329/9fbb11442efa1f0f50e1b81e6d8da923.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20220329/9fbb11442efa1f0f50e1b81e6d8da923.png" class="img-polaroid" title="3.28-1_.png" alt="3.28-1_.png" referrerpolicy="no-referrer"></a>
</div>
<br>
<br>图 1：fabric 固定 IP/MAC 流程<br>
<br><h2>二、流量出口 - EgressIp</h2><strong>2.1 使用场景</strong><br>
<ul><li>集群流量审计</li></ul><br>
<br>当在集群中想要做流量审计工作时，统计集群中每条对外的流量是一件十分麻烦的事情，因为集群中的每个节点都能成为对外流量的出口。当集群的节点数量较多时，工作量更是会成倍的上涨。但是，通过 Fabric，我们可以借助配置 EgressIP 来完美解决这个问题，所有的对外流量均从一组节点流出，工作人员从之前对集群的每个节点都进行统计，到只需要统计一组节点的流量记录，这大大降低了工作量。<br>
<ul><li>安全运维</li></ul><br>
<br>在实际生产环境中，基于安全生产的原则，集群中只有个别的节点可以连接外网，集群管理员只需要为个别节点开通对外策略。Pod 如果想要访问外网，可以通过配置 EgressIP 来实现。<br>
<ul><li>固定出口 IP</li></ul><br>
<br>某些应用（如数据库）只能接受指定源 IP 地址的流量，其它地址的连接均不予接受。如果集群中所有需要访问应用的流量都需要集群管理人员手动配置的话，这明显是一个巨大的工作量。对此我们可以通过配置 EgressIP，来配置专门的流量出口，大大减轻工作人员的运维压力。<br>
<br><strong>2.2 特点</strong><br>
Fabric EgressIP 功能的设计有如下特点：<br>
<br>(1) 配置灵活：EgressIP 可以配置为 namespace 级别，也可以设置为 pod 级别，满足不同级别的配置需求。<br>
<br>(2) 高可用性：当 fabric 重启之后，会自动重新分配 EgressIP。当正在使用的 EgressIP 挂掉之后，fabric 会自动在配置列表中选择一个最优且可用的 EgressIP 进行替换。<br>
<br>(3) EgressIP 优选，在 EgressIP 可用列表中优先会选择 pod 所在节点做为 EgressIP，从而减少网络损耗。<br>
<br><strong>2.3 实现原理</strong><br>
<ul><li>Egress IP 选择原理</li></ul><br>
<br>(1) 获取可用 EgressIP 列表。<br>
<br>(2) 判断可用 EgressIP 中是否有当前 pod 所在节点，如果存在则选择当前节点 IP 为 EgressIP。<br>
<br>(3) 如果不存在则选择当前 pod 之前被分配过的 EgressIP。<br>
<br>(4) 如果 pod 之前使用的 EgressIP 也不存在，则使用可用 EgerssIP 列表的最后一位。<br>
<ul><li>网络传输原理</li></ul><br>
<br>当 pod 数据访问目的地址被判定为外部网络时，数据会发往 EgressIP 所在的节点，然后从 EgressIP 所在节点传输到外部网络。<br>
<br>具体网络传输过程如图 2 所示：<br>
<br><div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20220329/e30eab3b1fcc50076b721f5469e40878.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20220329/e30eab3b1fcc50076b721f5469e40878.png" class="img-polaroid" title="3.28-2_.png" alt="3.28-2_.png" referrerpolicy="no-referrer"></a>
</div>
<br>
<br>图 2：设置 pod 通过 EgressIP 访问外部网络数据传输流程<br>
<br>注：Fabric overlay 网络支持多种封装协议(vxlan、gre、geneve)，图 2 仅以 vxlan 作为示例，不代表仅支持 vxlan。<br>
<br>三、QoS (Quality of Service) 服务质量<br>
<br><strong>3.1 使用场景</strong><br>
<ul><li>业务 Pod 双向限速</li></ul><br>
<br>当集群网络资源有限时，某一时刻发生的大文件传输过程，或者其它需要占用大规模网络资源的情况，极易造成集群网络的崩溃。通过 QoS 配置，可以限制某些容易发生大规模传输的网络资源配额，给予其正常的网络带宽，从而保证集群整体网络的正常。<br>
<br><strong>3.2 特点</strong><br>
(1) 使用简单，直接通过的注解（annotation）进行双向的 Qos 配置。<br>
<br>(2) 支持双栈，IPV4 和 IPV6 都有很好的支持。<br>
<br>(3) 支持多网络，在多网络的环境下，支持对每个网卡分别进行 QoS 配置。<br>
<br><strong>3.3 实现原理</strong><br>
Fabric 的容器网络架构基于 OpenvSwitch，pod 通过 veth peer 连接在 ovs bridge 的 port 上，主机侧的 veth 等同于 ovs 的 interface (网卡)，interface 插在 ovs port 里，所以我们控制 pod 的 QoS 就等同于控制对应 ovs interface/port 的 QoS。因此，配置 pod 出栈的 Qos 实际上是配置主机侧 veth 对应的 interface 的 ingress 属性，配置 pod 入栈的 QoS 实际是配置主机侧 veth 对应的 port (interface 插入的地方) 的 QoS 属性。<br>
<br>Fabric 配置 QoS 的原理如图 3 所示：<br>
<br><div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20220329/7a64f44a29176042a55d0b5117d2f5cd.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20220329/7a64f44a29176042a55d0b5117d2f5cd.png" class="img-polaroid" title="3.28-3_.png" alt="3.28-3_.png" referrerpolicy="no-referrer"></a>
</div>
<br>
<br>图 3：Fabric 配置 QoS 原理<br>
<br><h2>四、租户隔离</h2><strong>4.1 使用场景</strong><br>
<ul><li>多租户之间的网络隔离</li></ul><br>
<br>多租户是一种软件设计架构，指的是单个软件实例可以为不同的用户提供服务。多租户架构在云计算领域也有广泛的应用，在云计算领域多租户除了指共享软件服务之外，也可以指服务器资源，服务器资源在不同的租户之间进行分配。多租户的特性就是要解决租户间的隔离问题，不同的租户之间不能互相访问数据，以此达到安全隔离的效果。<br>
<br><strong>4.2 特点</strong><br>
Fabric 租户隔离功能设计有如下特点：<br>
<br>(1) 使用方便，直接添加注解（annotation）信息，即可为容器配置多租户隔离。<br>
<br>(2) 配置灵活，除了基本的租户之间的隔离之外，同时还可以配置兄弟租户之间的互通，可以适应多种使用场景。<br>
<br>(3) 租户白名单设计，几个系统级别的 namespace (kube-system, kube-public, default, kube-node-lease, monitoring, ingerss-nginx) 是任意租户可达的。<br>
<br><strong>4.3 实现原理</strong><br>
当集群中已经配置多租户时，pod 如果访问集群网络会首先进行网络策略验证，即验证网络访问源地址和目的地址网络是否符合多租户网络隔离策略。主要判断的是否在同一 namespace 下、源地址或目的地址是否在白名单内、租户是否存在、是否配置了兄弟租户（租户之间互通）。<br>
<br>简要的多租户网络隔离验证策略如图 4 所示：<br>
<br><div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20220329/415217d30ffe26d6269932528b7e1a74.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20220329/415217d30ffe26d6269932528b7e1a74.png" class="img-polaroid" title="3.28-4_.png" alt="3.28-4_.png" referrerpolicy="no-referrer"></a>
</div>
<br>
<br>图 4：多租户网络隔离验证策略<br>
<br><h2>五、总结与展望</h2>目前，Fabric 有着非常丰富且强大的功能，但由于篇幅所限，本文只能介绍一些常用且基础的功能。后续 Fabric 会持续优化已有的功能，并积极开发更多实用的新功能。在此之后，我们还会分享一些 Fabric 的进阶的功能的设计方案和相关特性。<br>
<br><a href="https://www.bocloud.com.cn/?source=baidu&plan=ppc&unit=ppc&keyword=boyun&bd_vid=9080245679410335436">点击BoCloud博云了解更多解决方案</a>
                                
                                                              
</div>
            