
---
title: 'CNI 这么多，怎么选？_ 容器网络系列第1期'
categories: 
 - 编程
 - Dockone
 - 周报
headimg: 'https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20220311/b2021bbd9b86e372dd2e32eb7cc0b4a3.jpg'
author: Dockone
comments: false
date: 2022-03-15 14:09:31
thumbnail: 'https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20220311/b2021bbd9b86e372dd2e32eb7cc0b4a3.jpg'
---

<div>   
<br>伴随云原生技术的落地应用，Kubernetes 正在成为云原生时代的操作系统，围绕 Kubernetes 的技术创新点也是层出不穷。其中，以容器网络举例，现在 Kubernetes 官网登记在册的 CNI 已经有近 30 种，可以算得上百家争鸣、各有所长了。<br>
<br>但随着企业开始使用 Kubernetes 承载越来越多的业务，企业对容器网络的要求越来越高，有些甚至已经超出了 CNI 的范畴。如何缓解企业在落地私有容器云平台时遇到的网络阻力，已经发展成了一个非常重要又急迫的问题。<br>
<br>本期我们将重点探讨 CNI 的典型场景有哪些？以及如何进行 CNI 选型？<br>
<br><h2>1. CNI 简介</h2>CNI (Container Network Interface) 定义了一组用于实现容器网络接口的配置以及 IP 地址的分配的规范。CNI 只关注容器的网络连接以及当容器删除时移除被分配的网络资源，因此 CNI 得到了广泛的支持，并且规范也易于实现。<br>
<br><div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20220311/b2021bbd9b86e372dd2e32eb7cc0b4a3.jpg" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20220311/b2021bbd9b86e372dd2e32eb7cc0b4a3.jpg" class="img-polaroid" title="3.10_图1_.jpg" alt="3.10_图1_.jpg" referrerpolicy="no-referrer"></a>
</div>
<br>
<br>随着 kuberntes 飞速发展，如今涌现出很多优秀的开源 CNI，如 calico，flannel，cilium。每个 CNI 都有各自的特点以及应用场景，但是也有各自的不足之处。因此，针对不同的场景使用合适的 CNI 就变得尤为重要。有时为了满足更复杂的网络需求，甚至于需要多种 CNI 联合使用，这样会使网络模型变得更为复杂，大大增加维护难度。<br>
<br>更详细的 CNI 讲解请参考:<br>
<br>Introduction to CNI（<a href="https://www.youtube.com/watch..." rel="nofollow" target="_blank">https://www.youtube.com/watch...</a>）<br>
<br>CNI deep dive（<a href="https://www.youtube.com/watch..." rel="nofollow" target="_blank">https://www.youtube.com/watch...</a>）<br>
<br><strong>1.1 主流 CNI 对比</strong><br>
<br><div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20220311/8d55865c8b0febfa354391e88648dadf.jpg" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20220311/8d55865c8b0febfa354391e88648dadf.jpg" class="img-polaroid" title="CNI_这么多，怎么选？_表格长图.jpg" alt="CNI_这么多，怎么选？_表格长图.jpg" referrerpolicy="no-referrer"></a>
</div>
<br>
<br>综上， 在开源 CNI 的领域中 calico, flannel, cilium 都有各自的优势，但是针对企业功能还略显不足。比如 calico， flannel 基本功能都有，社区也比较活跃，同时二者可以组合使用达到取长补短，但是组合使用维护成本也会增加。cilium 则是通过 eBPF 实现的独立的数据面，在网络安全，服务转发方面研究较深，但是运维起来比较困难。而 Fabric 则在功能方面比较全面，性能出色且稳定性强，运维也相对简单。<br>
<br><h2>2. Fabric 简介</h2>Fabric 是博云自研的 CNI 插件，旨在提供一个能适应多种场景，功能强大，性能卓越，稳定可靠以及简单易用的容器网络管理平台。<br>
<br>Fabric 支持 underlay/overlay 模式，同时支持 IPV4/IPV6 单栈和双栈，支持容器多网络/多网卡以及集群联邦，EIP，Qos，NetworkPolicy，PodSecurity，Windows 等特色功能。<br>
<br>并且，为了提升运维效率， 开发了对应的 debug 工具，拥有流量追踪，缓存分析等能力。支持 Linux/Windows 操作系统、支持 ARM/X86 等 CPU 架构。<br>
<br>从 Fabric 2.5  以后的版本还将集成 eBPF、智能网卡、流量分析、无感升级等功能，从而提升数据面性能，提升业务稳定性，以及更细粒度的运维调试能力。<br>
<br><strong>2.1 整体架构</strong><br>
<br><div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20220311/4412c13e33bc6c73096411631073a7a0.jpg" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20220311/4412c13e33bc6c73096411631073a7a0.jpg" class="img-polaroid" title="3.10_图4_.jpg" alt="3.10_图4_.jpg" referrerpolicy="no-referrer"></a>
</div>
<br>
图 1 Fabric Underlay 架构<br>
<br><div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20220311/8cd941e3521172091e8879dc061350a1.jpg" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20220311/8cd941e3521172091e8879dc061350a1.jpg" class="img-polaroid" title="3.10_图5_.jpg" alt="3.10_图5_.jpg" referrerpolicy="no-referrer"></a>
</div>
<br>
图 2 Fabric overlay 架构<br>
<br>Fabric 由四大核心组件组成:<br>
<ol><li>ovs：成熟且稳定的软件交换机，用于接入容器接口，以及数据面转发和安全策略控制 </li><li>ovs-controller：负责 ovs数据面的控制，默认流表生成，动态流表下发 </li><li>fabric-ctl：负责集群中 pod 信息的采集，缓存，以及其他核心功能的控制 </li><li>fabric二进制文件：标准的 k8s CNI，用于容器网络接口的配置</li></ol><br>
<br><strong>2.2 设计理念</strong><br>
Fabric 一直遵循着四大设计原则:<br>
<ol><li>微分段设计: 控制面高稳定性、快速收敛、高性能、低延迟 </li><li>简单即稳定: 全分布式部署、扩展性强、分布式控制、无单点故障、自动运维 </li><li>安全隔离: 租户隔离、NetworkPolicy、PodSecurity、隧道加密 </li><li>功能丰富: IP/MAC固定、Qos、egressIP、集群联邦、网络监控</li></ol><br>
<br><strong>2.3 发展历程</strong><br>
Fabric 自 2018 年底开始至今，已累计发布 6 个稳定版本，在十余个金融客户生产环境中稳定运行多年。<br>
<br><div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20220311/b732da03b127b384f8be9a66e4b8a1e1.jpg" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20220311/b732da03b127b384f8be9a66e4b8a1e1.jpg" class="img-polaroid" title="3.10_图7_.jpg" alt="3.10_图7_.jpg" referrerpolicy="no-referrer"></a>
</div>
<br>
图 3 fabric 发展历程<br>
<br><h2>3. 通用场景及选型建议</h2>k8s 是支持混合部署的，在很多生产环境下为了最大化利用集群资源，可以将 k8s master 节点部署在小规格虚拟机上，同时将计算节点部署在物理机或者大规格虚拟机上。甚至于， 一个集群中可以同时存在异构 CPU 节点或者不同操作系统 (Linux/Windows) 节点。不管是选用 Fabric 哪种模式，其核心功能都是完美支持的，如多网络、多 IP、QoS、租户隔离、Network Policy 等。<br>
<br><strong>3.1 Underlay 双网卡模式</strong><br>
该模式用最简单的方式打通了集群内外主机访问集群内业务的需求， 同时集群内的所有流量都能在外部交换机、路由器、防火墙等其他网络设备上追踪，方便了网络运维人员对集群内流量的控制以及其他审计能力。在该模式下也能最大程度保证业务网络的性能几乎等于业务网所提供的最大带宽。但是，该模式消耗的是业务网真实的 IP 地址，这在一定程度上限制了集群规模。<br>
<br><strong>3.1.1 环境要求</strong><br>
<ol><li>每个节点至少包含两张网卡，分别用于管理网和业务网 </li><li>管理网和业务网不能重合，业务网 IP 不能被集群外的其他机器占用</li><li>业务网卡根据需要将上联口配置成 access/trunk，且开启混杂模式</li></ol><br>
<br><strong>3.1.2 适用场景</strong><br>
（一） 集群外的机器有直接访问集群内业务的需求，如注册中心在集群外部<br>
<br>（二） 集群内业务对网络性能有较高的要求<br>
<br>（三） 集群内的业务流量能够被防火墙等安全设备控制<br>
<br>（四） 中小规模集群，因为集群里的 pod 消耗的是真实的 IP 地址，该场景下 IP 地址都是较为珍贵的，集群规模过大可能导致业务网 IP 地址池被用尽<br>
<br><strong>3.1.3 业务网规划建议</strong><br>
由于 underlay 消耗的是现有 IP 资源，所以业务网的规划就显得十分重要。如果单个业务网过大，可能导致广播域过大从而使交换机性能下降，所以在规划业务网络时我们可以划分为多个 C 类网络，不同的 C 类网络可以给不同的租户使用这样也能保证租户间的隔离性。<br>
<br><strong>3.2 Overlay 模式</strong><br>
该模式部署简单，环境依赖少。甚至于不关心节点所处位置，只要集群内节点间能相互访问理论上就能使用 overlay 模式。另外，该模式消耗的是虚拟的 IP 地址，能支持大规模的业务集群。<br>
<br><strong>3.2.1 环境要求</strong><br>
（一） 节点至少一张网卡，且每个节点之间能进行通信<br>
<br>（二） 如果节点上多张网卡需要保证管理网卡索引最小<br>
<br>（三） 节点之间放行对应的隧道协议端口，如 vxlan 需放行 UDP 4789 端口，geneve 需放行 UDP 6081 端口<br>
<br><strong>3.2.2 适用场景</strong><br>
（一） 集群外集群没有直接访问集群业务的需求<br>
<br>（二） 集群业务对网络性能要求不是很高<br>
<br>（三） 私有地址池，支持大规模集群<br>
<br>（四） 外部网络依赖少，除了放开对应的隧道协议策略之外，无需其他配置<br>
<br><strong>3.2.3 Overlay 联邦</strong><br>
为了打通 Fabric 集群间业务 Pod 的通信，Fabric 从 2.3 开始就支持了集群联邦能力。相较于开源社区提供的网络联邦方案，Fabric 联邦无需建立多重隧道，跨集群的 Pod 通信和同集群跨节点的 Pod 通信原理相同，不需要额外网关转发，直接使用一层隧道打通，无多余网络损耗。<br>
<br><h2>4. VPC 场景及选型建议</h2>从网络视角，基础设施可以分布到三个层级，大部分业务系统处于第二层和第三层，层级之间或层级之内的网络策略需要配置。<br>
<br><div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20220311/c44689de7a3bbff4ed8778085fc424fe.jpg" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20220311/c44689de7a3bbff4ed8778085fc424fe.jpg" class="img-polaroid" title="3.10_图8_.jpg" alt="3.10_图8_.jpg" referrerpolicy="no-referrer"></a>
</div>
<br>
<br><strong>4.1 基于 VPC 的多集群管理</strong><br>
根据不同的业务需求，我们可以构建多个集群，按需包含 underlay 和 overlay 等部署模式, 虚拟机可以跟 underlay 集群中的 Pod 直接通信，同一个 VPC 内的 overlay 集群之间可以利用联邦进行跨集群间业务通信。<br>
<br><div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20220311/ff3f6aa227650f78993e9181543614ad.jpg" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20220311/ff3f6aa227650f78993e9181543614ad.jpg" class="img-polaroid" title="3.10_图9_.jpg" alt="3.10_图9_.jpg" referrerpolicy="no-referrer"></a>
</div>
<br>
<br><h2>5. 未来展望</h2>现如今 Fabric 已经拥有丰富且强大的功能，并且能适用于各种环境。在未来我们将在控制面和数据面上不断进行性能优化，同时会提供更加丰富的网络能力、监控分析能力以及运维能力， 旨在打造一个更稳定，更强大的企业级容器网络平台。<br>
<br><a href="https://www.bocloud.com.cnhttp//">点击BoCloud博云了解更多解决方案</a>
                                
                                                              
</div>
            