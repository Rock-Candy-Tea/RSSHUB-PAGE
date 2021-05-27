
---
title: 'Cilium 1.10版本特性解读：支持 Wireguard、BGP、Egress IP 网关、XDP、阿里云集成'
categories: 
 - 编程
 - Dockone
 - 周报
headimg: 'https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210526/c25a8428476d1559ac682483e10dd4ed.png'
author: Dockone
comments: false
date: 2021-05-27 08:31:45
thumbnail: 'https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210526/c25a8428476d1559ac682483e10dd4ed.png'
---

<div>   
<br>Cilium 团队宣布 Cilium 1.10 版本正式发布。此版本总共包含了 2042 个新的提交。280位贡献者来自不同的企业包括：阿里巴巴、Datadog、Google、 Isovalent、 SuSE、Palantir 等。无论是自建数据中心，还是云上使用Cilium的用户，对更好、更广泛的网络集成提出了很多反馈。此版本的主要重点是确保Kubernetes网络与企业内部部署基础结构之间的无缝集成。<br>
<ul><li><strong>Egress IP gateway</strong>：当将云原生应用程序与在集群之外运行的传统应用程序集成时，由于Pod IP比传统网络更具弹性，因此IP地址管理可能会成为一个难题。通过新的Kubernetes CRD，可以在数据包离开Kubernetes集群时将静态IP与流量相关联。这使外部防火墙可以识别固定IP，并且过滤特定pod的流量。</li><li><strong>Integrated BGP Support</strong>：我们简化了通过BGP公告 Kubernetes service IP的功能，以允许外部负载轻松和集群内云原生应用程序进行通信。在1.10版本中，我们在Cilium中集成了 BGP 服务公告，因而无需任何其他外部组件就能暴露这些 service。</li><li><br><strong>独立 Load Balancer</strong>：Cilium的高性能、强大的负载平衡实现针对云原生环境的规模和客户需求进行了调整。现在，您可以使用Cilium作为独立的负载平衡器来替换网络中昂贵的硬件负载均衡。无需Kubernets，也可使用DSR和Maglev在本地环境中处理南北流量。<br>
<ul><li><strong>PCAP Recorder</strong> 通过全部或部分抓包，在独立负载均衡器模式下提供可观测性能力。</li></ul></li></ul><br>
<br>除了着眼于与更广泛的网络集成外，我们还致力于简化Cilium安装部署，进一步提升网络性能，并添加了一系列急需的功能：<br>
<ul><li><strong>支持 Wireguard</strong>：作为最受人追捧的功能之一，Cilium现在支持使用Wireguard协议替代现有IPsec实现对集群中Pod之间的流量进行加密。</li><li><strong>集群管理 CLI（New）</strong>：增加了实验性的Cilium CLI 工具，通过自动检测您的环境限制并使用最佳选项集来配置Cilium，从而简化了安装、故障排除和功能启用。</li><li><strong>更好的性能</strong>：Cilium现在具有跳过 Netfilter 连接跟踪的功能，改进了北/南服务处理，并且通过改进的Linux隧道将吞吐量性能提高了一倍。    </li><li><strong>更多增强</strong>：该版本带来了对<a href="https://cilium.io/blog/2021/05/20/cilium-110#dualstack">Kubernetes双栈</a>，<a href="https://cilium.io/blog/2021/05/20/cilium-110#alibaba">阿里云原生IPAM</a>，并发布<a href="https://cilium.io/blog/2021/05/20/cilium-110#arm64">ARM64的第一个官方版本</a>。新的 Rancher 、Rancher Kubernetes Engine 指南使得在本地Kubernetes环境中部署Cilium更容易。</li></ul><br>
<br><h3>Egress IP Gateway</h3>主要贡献：Yongkun Gui（Google）and Bolun Zhao（Google）<br>
<br>随着Kubernetes成为应用容器化的标准平台，将这些新服务连接到遗留环境变得很痛苦。传统工作负载具有可以被防火墙识别的固定且唯一的IP。当容器根据需要伸缩时，来自容器应用程序的流量将来自许多不同的IP，通常会以每个容器所在节点的IP的形式出现。这使得很难为应用程序设置安全边界并审核其行为。<br>
<br>1.10版本将出口网关功能引入了Cilium。现在，Cilium允许用户指定出口NAT策略，以便将所选的Pod的出口流量伪装成用户定义的IP地址。如下图所示，来自工作节点中运行的Pod的流量不是通过eth0直接流出，而是通过网关节点从群集中流出。在此节点上，将应用SNAT为出站流量提供一致的外部IP。从那里，可以将网络组件配置为根据源IP地址不同地处理流量。例如，传统防火墙能够通过完全匹配入站流量的源IP地址来过滤源自具有特定标签的Pod的流量。<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210526/c25a8428476d1559ac682483e10dd4ed.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210526/c25a8428476d1559ac682483e10dd4ed.png" class="img-polaroid" title="1.png" alt="1.png" referrerpolicy="no-referrer"></a>
</div>
<br>
例下面策略，Cilium 会把 default 命名空间下，发到外部地址 192.168.33.13/32的 Pod的流量，重定向到 192.168.33.100的（网关）节点。可在<a href="https://docs.cilium.io/en/v1.10/intro/">入门指南</a>中找到有关出口网关的更多信息。<br>
<pre class="prettyprint">apiVersion: cilium.io/v2alpha1  <br>
kind: CiliumEgressNATPolicy  <br>
metadata:  <br>
name: egress-sample  <br>
spec:  <br>
egress:  <br>
- podSelector:  <br>
  matchLabels:  <br>
    # The following label selects default namespace  <br>
    io.kubernetes.pod.namespace: default  <br>
destinationCIDRs:  <br>
- 192.168.33.13/32  <br>
egressSourceIP: "192.168.33.100"  <br>
</pre><br>
<h3>BGP for LoadBalancer VIP</h3>主要贡献：Chris Tarazi（Isovalent）<br>
<br>随着Kubernetes在本地环境中变得越来越普遍，用户在其环境中越来越多地同时使用传统应用程序和Cloud Native应用程序。为了将它们连接在一起并允许外部访问，需要一种机制来集成Kubernetes和运行BGP的现有网络基础结构。<br>
<br>Cilium 1.10版本带来了对BGP的集成支持，将Kubernetes暴露于外部，同时简化了用户的部署。集成通过<a href="https://metallb.universe.tf/">MetalLB</a>进行，利用了service IP和BGP的L3协议支持。现在Cilium可为LoadBalancer的service分配IP，并通过BGP向其BGP路由器通告它们。现在无需其他组件就可以把serivce暴露到集群外部。<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210526/3bae3fc2653d7043dfc03dff66615473.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210526/3bae3fc2653d7043dfc03dff66615473.png" class="img-polaroid" title="2.png" alt="2.png" referrerpolicy="no-referrer"></a>
</div>
<br>
将来，我们计划也支持通过BGP发布Pod CIDR和出口IP网关。这将进一步改善Cloud Native与传统环境之间的桥梁。以下是用于配置Cilium的BGP功能的ConfigMap示例。配置的两个主要方面是对等方和地址池。前者用于与网络中现有的BGP路由器连接，因此需要IP地址和ASN。后者是Cilium将为LoadBalancer服务分配IP的池。<br>
<pre class="prettyprint">apiVersion: v1  <br>
kind: ConfigMap  <br>
metadata:  <br>
name: bgp-config  <br>
namespace: kube-system  <br>
data:  <br>
config.yaml: |  <br>
peers:  <br>
- peer-address: 10.0.0.1  <br>
  peer-asn: 64512  <br>
  my-asn: 64512  <br>
address-pools:  <br>
- name: default  <br>
  protocol: bgp  <br>
  addresses:  <br>
  - 192.0.2.0/24 <br>
</pre><br>
<br>更多请参阅文档中的<a href="https://docs.cilium.io/en/v1.10/gettingstarted/bgp/">BGP指南</a>。<br>
<h3>阿里云集成</h3>主要贡献：Bokang Li（Alibaba）<br>
<br>Cilium 支持从公有云上分配IP给Pod，之前已经支持的有 AWS ENI （v1.6）、Azure （v1.8）模式。在1.10版本里增加了阿里云的支持，使得 Cilium 可以直接为Pod 分配 ENI （Elastic Network Interface）上的IP。<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210526/1d8c4dbb7be49efdd6bf0c3e14412544.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210526/1d8c4dbb7be49efdd6bf0c3e14412544.png" class="img-polaroid" title="3.png" alt="3.png" referrerpolicy="no-referrer"></a>
</div>
<br>
这种模式下，Cilium 为Pod 直接分配 ENI 的IP，这个地址在阿里云的 VPC 上可以被直接路由。这种模式简化了 Pod 间流量模型避免了封装、SNAT。作为云原生的网络解决方案，用户可以轻易使用云企业网（CEN）、VPN网关将自建集群接入到阿里云上。<br>
<br>更多信息参考<a href="https://docs.cilium.io/en/v1.10/gettingstarted/alibabacloud-eni/">阿里云使用文档</a>。<br>
<h3>Wireguard 透明加密</h3>主要贡献：Martynas Pumputis（Isovalent）and Sebastian Wicki（Isovalent）<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210526/6d50b9b5482ac35e77eb1ed50b9a8cbc.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210526/6d50b9b5482ac35e77eb1ed50b9a8cbc.png" class="img-polaroid" title="4.png" alt="4.png" referrerpolicy="no-referrer"></a>
</div>
<br>
在1.10版本中，我们加入Wireguard协议进行透明加密。透明加密是一项功能，可确保Pod之间的流量通过安全隧道传输，从而允许用户在不受信任的网络中运行Kubernetes。自1.4版开始，Cilium就已经支持通过IPSec进行透明加密。现在，我们也引入了 Wireguard。Wireguard 协议不允许对诸如密钥大小和密码套件之类的参数进行调整，这使其非常易于使用并简化了部署和操作。每个节点的加密密钥对由Cilium自动生成，并且密钥旋转由Wireguard内核模块透明地执行。<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210526/e78ea3f098324be154db6aa39d4e132c.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210526/e78ea3f098324be154db6aa39d4e132c.png" class="img-polaroid" title="5.png" alt="5.png" referrerpolicy="no-referrer"></a>
</div>
<br>
对于某些工作负载，Wireguard还具有优于IPSec的性能优势。在我们最近的<a href="https://cilium.io/blog/2021/05/11/cni-benchmark#encryption">CNI性能分析</a>博客文章中，我们对这两种协议进行了评估，发现Wireguard可以为流工作负载实现非常高的吞吐量，但是IPSec仍可以实现更好的延迟，并且在某些情况下可以将加密算法卸载到CPU。上图显示了我们实验的简短摘录，请阅读完整的博客以获取更多详细信息。<br>
<br>Wireguard的另一个技术优势是，它可以很好地集成到Cilium datapath 体系中。由于安全隧道是作为Linux网络接口公开的，因此Wireguard可以非常轻松地标记来自容器的数据包以进行加密，然后将其转发到安全隧道设备。下面的动画显示了Cilium中Wireguard加密数据包的路径：<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210526/6c9df1df450a2f1e00d8e250641e8aca.gif" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210526/6c9df1df450a2f1e00d8e250641e8aca.gif" class="img-polaroid" title="6.gif" alt="6.gif" referrerpolicy="no-referrer"></a>
</div>
<br>
Cilium 1.10中直接路由和隧道模式均支持的Wireguard加密，如果基础Linux内核支持的话，也可以在托管Kubernetes环境中启用Wireguard加密。当前缺少对主机级别加密以及Cilium L7 策略和可观测性的支持，并将在后面Cilium版本中添加。如果您想了解有关Cilium中的Wireguard集成的更多信息，请确保观看<a href="https://www.youtube.com/watch?v=-awkPi3D60E">eCHO第3集直播的录制</a>，并阅读Cilium文档中的<a href="https://docs.cilium.io/en/v1.10/gettingstarted/encryption-wireguard/">入门指南</a>。<br>
<h3>Kubernetes 双栈</h3>主要贡献：Deepesh Pathak（Microsoft），André Martins（Isovalent）<br>
<br>Cilium 创建之初就支持 IPv4 / v6双栈。在Cilium的早期原型中也支持 IPv6 单栈模式。鉴于Kubernetes一直缺乏双栈支持，Cilium 对Pods、 Services的 IPv6 支持有点麻烦。在最新的Kubernetes 稳定版本中IP双栈已经默认开启：<a href="https://kubernetes.io/docs/concepts/services-networking/dual-stack/">Kubernetes 1.21默认开启IP双栈（beta）</a>。Cilium IPv4/v6 双栈功能可以通过 helm 部署时开启，设置 <code class="prettyprint">ipv6.enabled</code>：<br>
<pre class="prettyprint">$ helm install cilium cilium/cilium --version 1.10.0 \  <br>
--namespace kube-system \  <br>
--set ipv4.enabled=true \  <br>
--set ipv6.enabled=true  <br>
$ kubectl get cep -n kube-system  <br>
NAME                       ENDPOINT ID   IDENTITY ID   ENDPOINT STATE   IPV4            IPV6  <br>
coredns-755cd654d4-msqgm   2205          11023         ready            10.16.115.242   fd02::71cf<br>
</pre><br>
<h3>Cilium ARM64 镜像</h3>主要贡献：André Martins（Isovalent）<br>
<br>在以前的版本中，Cilium核心团队已在ARM64平台上提供了快照以用于初始测试。但是没发布到Cilium的官方镜像。在个迭代中我们对镜像构建进行了一些改进，以允许自动构建多架构镜像docker镜像。从Cilium 1.10开始，Docker Hub和Quay.io上的官方Cilium存储库将托管这些多架构镜像。在ARM64上安装Cilium与在其他平台上安装类似，使用与AMD64 docker镜像相同的映像标签。这让Cilium 具备在AWS Graviton 实例、Azure Linux/ARM64 Pipelines 等一系列新硬件上运行的能力。Cilium甚至可以在智能手机上运行！<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210526/328790673a8f03c3da9ba058902ecd66.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210526/328790673a8f03c3da9ba058902ecd66.png" class="img-polaroid" title="14.png" alt="14.png" referrerpolicy="no-referrer"></a>
</div>
<br>
<h3>Cilium CLI</h3>提供了一个新的<a href="https://github.com/cilium/cilium-cli">CLI</a>，可用于安装和管理Cilium群集。CLI直接连接Kubernetes API，并提供各种功能来管理Cilium。该CLI 兼容Cilium的旧版本。<br>
<ul><li>检查Cilium安装状态，并快速显示故障状态。</li><li>自动检测特定Kubernetes环境（datapath，IPAM等）的理想配置选项。</li><li>启用Hubble观测性和Relay组件。</li><li>管理多集群连接和状态。</li><li>执行连接性和一致性测试，以验证集群中的网络功能。</li></ul><br>
<br><h4>集群范围 Cilium Status</h4><code class="prettyprint">cilium status</code> 命令可以快速检查 Cilium 安装状态。可显示不正常组件数量、节点故障的状态。<br>
<pre class="prettyprint">$ cilium status  <br>
/¯¯\  <br>
/¯¯\__/¯¯\    Cilium:         OK  <br>
\__/¯¯\__/    Operator:       OK  <br>
/¯¯\__/¯¯\    Hubble:         disabled  <br>
\__/¯¯\__/    ClusterMesh:    disabled  <br>
\__/  <br>
Deployment        cilium-operator    Desired: 2, Ready: 2/2, Available: 2/2  <br>
DaemonSet         cilium             Desired: 2, Ready: 2/2, Available: 2/2  <br>
Containers:       cilium             Running: 2  <br>
              cilium-operator    Running: 2  <br>
Image versions    cilium             quay.io/cilium/cilium:v1.10.0: 2  <br>
              cilium-operator    quay.io/cilium/operator-generic:v1.10.0: 2 <br>
</pre><br>
<h4>连通性和一致性测试</h4>新增 <code class="prettyprint">cilium connectivity test</code> 命令，可以快速验证网络、 kubernets service、network policy 是否按预期工作，是验证 Cilium 正常工作的理想工具。<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210526/62469e16d06b84c26dba83ea6836bcef.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210526/62469e16d06b84c26dba83ea6836bcef.png" class="img-polaroid" title="13.png" alt="13.png" referrerpolicy="no-referrer"></a>
</div>
<br>
<h3>Cilium网络性能改进</h3>主要贡献：Gilberto Bertin（Isovalent），Kornilios Kourtis（Isovalent）and Daniel Borkmann（Isovalent）<br>
<br>接<a href="https://cilium.io/blog/2020/11/10/cilium-19#performance-testing-framework">之前版本工作</a>，我们继续严格评估Cilium的网络性能。我们在<a href="https://cilium.io/blog/2021/05/11/cni-benchmark">博文</a>中总结了我们的最新发现，并将其整合到<a href="https://docs.cilium.io/en/v1.10/operations/performance/benchmark/">Cilium的文档</a>中。我们对比不同场景，展示了 eBPF 带来的低延迟、高吞吐的 CNI ，以及 Wireguard 和 IPsec 的对比。<br>
<br>在我们深入的性能评估的指导下，Cilium 1.10包括许多 datapath 改进，这次主要集中在VXLAN / Geneve隧道性能以及减少Netfilter开销上。最为显着地：<br>
<ul><li><a href="https://cilium.io/blog/2020/11/10/cilium-19#virtual-ethernet-device-optimization-with-ebpf">BPF host routing</a>已扩展为支持封装。这意味着在直接路由和隧道模式下均可以使用eBPF最大化性能。由于不再需要上主机堆栈处理网络流量，因此可以将南北服务处理与直接路由模式相提并论。</li><li>我们定位并<a href="https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git/commit/?id=89e5c58fc1e2857ccdaae506fb8bc5fed57ee063">解决</a>了Linux内核中的性能问题，该问题导致VXLAN和Geneve的UDP封装数据包的GRO聚合被延迟，导致与Cilium封装一起使用时性能欠佳。该修复程序已回合到所有稳定的内核（例如4.9），并已集成到下游发行版（如Ubuntu LTS变体）中。在我们的测试环境中，这使VXLAN和Geneve封装的 Gbit/s 级流量TCP单流吞吐速率提高了一倍以上。</li><li>最后，现在可以将Cilium配置为跳过Netfilter conntrack：我们引入了一个新的配置项  <code class="prettyprint">--install-no-conntrack-iptables-rules</code> ，该选项允许在任何可能的情况下跳过Netfilter连接跟踪。您可以在<a href="https://docs.cilium.io/en/v1.10/operations/performance/tuning/#bypass-iptables-connection-tracking">调优指南</a>中阅读更多内容。</li></ul><br>
<br><h4>Case 1：Pod到Pod隧道模式</h4>对Pod 间使用VXLAN/Geneve隧道互访场景，吞吐性能有显著提升（通过netperf TCP_STREAM 测试）。我们对Linux内核的GRO引擎进行了小幅改进，该引擎通过将MTU大小的数据包聚合到64k个超级数据包来优化Linux的堆栈遍历，从而降低了每个数据包的堆栈处理成本。<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210526/b5ab1b4fba7a1cf8c9a34d86e61a836f.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210526/b5ab1b4fba7a1cf8c9a34d86e61a836f.png" class="img-polaroid" title="7.png" alt="7.png" referrerpolicy="no-referrer"></a>
</div>
<br>
<h4>Case 2：主机到 Service/Pod 隧道模式</h4>对于外部客户端（例如NodePort service）访问Pod 情况，可以应用与<a href="https://cilium.io/blog/2020/11/10/cilium-19#virtual-ethernet-device-optimization-with-ebpf">之前</a>直接路由情况相同的改进。转发可以直接在tc eBPF层中执行，而不必将数据包推入主机栈。这将显着提高单流吞吐量（TCP_STREAM），并显着减少延迟（TCP_RR TCP_CRR）。当数据包必须走隧道时（例如Pod 到Pod），这时收益不明显，因为这要求通过上层UDP堆栈。但对后端在本地节点的收益明显。一个典型的例子是NodePort 服务并且指定了 <code class="prettyprint">externalTrafficPolicy=Local</code>。<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210526/9be3f56c107d58e0ddc360ed2b24601d.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210526/9be3f56c107d58e0ddc360ed2b24601d.png" class="img-polaroid" title="8.png" alt="8.png" referrerpolicy="no-referrer"></a>
</div>
<br>
<h4>Case 3：Pod 到 Pod 直接路由模式</h4>对于最后一种情况，我们研究了流量通过 Netfilter 子系统时的性能影响。发现特别是Netfilter 连接跟踪模块会给 fast-path 增加大量成本。由于我们实现了基于eBPF 的源地址转换，我们可以跳过连接跟踪。改进后连接/请求/响应类型的工作负载（TCP_CRR）性能几乎提升了一倍。<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210526/9257502009ba1bbacf48ba695d2914de.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210526/9257502009ba1bbacf48ba695d2914de.png" class="img-polaroid" title="9.png" alt="9.png" referrerpolicy="no-referrer"></a>
</div>
<br>
<h3>XDP-based Standalone Load Balancer</h3>主要贡献：Daniel Borkmann（Isovalent），Martynas Pumputis（Isovalent），Chris Tarazi（Isovalent）and Sebastian Wicki（Isovalent）<br>
<br>Cilium基于eBPF的负载均衡器最新增加了对Maglev一致性哈希的支持以及eXpress数据路径（XDP）层的转发平面加速，从而显着提高了鲁棒性和负载均衡效率。这些功能目标是替代kube-proxy，同时也为可编程的高性能第4层负载均衡器（L4LB）框架铺平了道路，我们在1.10版本中添加了该框架。Cilium XDP L4LB 带有完整的IPv4/v6 双栈支持，可以独立于Kubernetes进行部署。我们共同维护的Linux内核中的XDP层提供了接近于DPDK的性能，同时通过在驱动程序层中运行eBPF程序，搭载Linux的NAPI机制来更有效地利用CPU资源。绝大部分的10G，40G和100G NIC驱动程序，LTS内核均支持XDP。为了更好地理解Cilium XDP L4LB的功能和架构，可见下图：<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210526/420d18f76f2b15bbe29548887a4302e3.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210526/420d18f76f2b15bbe29548887a4302e3.png" class="img-polaroid" title="10.png" alt="10.png" referrerpolicy="no-referrer"></a>
</div>
<br>
Cilium 基于XDP 的L4 负载均衡由下面两部分组成：<br>
<ul><li>高性能转发平面，eBPF 程序运行在驱动层，以便Maglev一致哈希以L4 DNAT从服务表中选择后端，然后将数据包尽快回出节点尽可能possible,</li><li>Cilium编排API，以便对主要服务表和通配的n元组PCAP记录器进行编程和利用，该记录器可用于过滤和观察L4LB的入站和相应出站流量。</li></ul><br>
<br>通过集成到XDP层和Maglev 后端状态保持，L4LB可以随着NIC接收队列的CPU的数量线性扩展。鉴于负载均衡器设计的效率和较低的CPU开销，Cilium XDP L4LB也可以与常规工作负载并置。尽管Cilium的XDP L4LB入门指南尚在开发中，但请参阅<a href="https://github.com/cilium/cilium-l4lb-test/blob/master/cilium-lb-example.yaml">示例DaemonSet</a>以了解如何部署负载平衡器。入门指南发布后，我们将更新。<br>
<h4>DSR with IPIP Encapsulation and L4 DNAT</h4>Cilium的XDP L4LB实现了直接服务器返回（DSR），用于将请求转发到后端节点，这是通过将客户端请求封装到 IPIP/IP6IP6 数据包中来实现的。内层 IP 头包含原始请求，因此后端节点具有完整的上下文，可以直接向客户端发送答复，从而节省了反向路径的额外跳数。L4LB DNAT 后端可以配置为 service 或者 pod ip。对于即将发布的版本，我们计划将其扩展到其他封装机制。<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210526/e696ab06335194303f7940a38164fd91.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210526/e696ab06335194303f7940a38164fd91.png" class="img-polaroid" title="11.png" alt="11.png" referrerpolicy="no-referrer"></a>
</div>
<br>
<h4>n-Tuple PCAP Recorder</h4>在一组不断处理每秒数亿个数据包的Cilium XDP L4LB中，如何才能有效地找到来排除故障或观察一小部分网络流量呢？由于XDP在常规网络堆栈以下运行，现有工具（例如tcpdump）并不可用。在Cilium XDP L4LB的数据路径中，设置有两个观察点，以便过滤并记录LB入站流量及其对应的出站流量。这就使得我们可以观测流量通过负载均衡后下一跳路径。L4LB 过滤器支持通配符和n元组表达式，当然也支持 IPv4/v6，这意味着允许匹配源和目标前缀，端口和协议的任意组合。支持导出为PCAP文件，以通过Wireshark，tcpdump或其他熟悉的工具进行检查。<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210526/1198352fcdcebff3889b1aa992b26ebc.gif" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210526/1198352fcdcebff3889b1aa992b26ebc.gif" class="img-polaroid" title="12.gif" alt="12.gif" referrerpolicy="no-referrer"></a>
</div>
<br>
PCAP记录器对XDP datapath 里面大流量进行优化，可通过新的Hubble Recorder API 调用。为了方便起见，我们还为Hubble CLI添加了支持，作为Hubble Recorder API 用法的一个示例。上面的示例演示如何通过在Hubble CLI中指定5元组过滤器来捕获从任何源到目标  <code class="prettyprint">192.168.33.11:80</code>  L4LB转发的TCP服务流量。PCAP记录器目前仅在Cilium的新XDP L4LB模式下可用，未来计划支持分析集群内东西向流量。<br>
<br>译文链接：<a href="https://mp.weixin.qq.com/s/FaLtC6j3zhf9W3wKbfQX0g" rel="nofollow" target="_blank">https://mp.weixin.qq.com/s/FaLtC6j3zhf9W3wKbfQX0g</a>
                                                                <div class="aw-upload-img-list">
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                </div>
                                
                                                                <ul class="aw-upload-file-list">
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    </ul>
                                                              
</div>
            