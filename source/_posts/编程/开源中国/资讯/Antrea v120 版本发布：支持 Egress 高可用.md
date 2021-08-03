
---
title: 'Antrea v1.2.0 版本发布：支持 Egress 高可用'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://oscimg.oschina.net/oscnet/d5de9464-eab1-4b63-96b9-c8591f8abe0b.png'
author: 开源中国
comments: false
date: Tue, 03 Aug 2021 07:35:00 GMT
thumbnail: 'https://oscimg.oschina.net/oscnet/d5de9464-eab1-4b63-96b9-c8591f8abe0b.png'
---

<div>   
<div class="content">
                                                                                            <p><img src="https://oscimg.oschina.net/oscnet/d5de9464-eab1-4b63-96b9-c8591f8abe0b.png" referrerpolicy="no-referrer"></p> 
<p><strong>引言</strong></p> 
<p>Antrea 项目是一个基于 Open vSwitch（OVS）的开源 Kubernetes CNI 网络解决方案，旨在为 Kubernetes 集群提供更高效、更安全的跨平台网络和安全策略。Antrea Github 地址：https://github.com/antrea-io/antrea</p> 
<p>北京时间2021年07月16日，Antrea发布了新版本v1.2.0。NetworkPolicyStats 功能从 Alpha 升级到 Beta，因此默认启用。Antrea v1.2.0 Release文档：https://github.com/antrea-io/antrea/releases/tag/v1.2.0</p> 
<p><img src="https://oscimg.oschina.net/oscnet/990533d9-1fe8-4365-9a05-1dda7482b936.png" referrerpolicy="no-referrer"></p> 
<p><strong>新增特性</strong></p> 
<p>本次发布的1.2.0版本新特性包括：</p> 
<ul> 
 <li> <p>添加新的 ExternalIPPool API 以定义可用作出口 SNAT IP 的 IP 地址范围；这些 IP 根据 nodeSelector 分配给节点，并在节点出现故障时自动故障转移；(#2236 #2237 #2186 #2358 #2345 #2371 , @tnqn @wenqiq ) 有关更多信息，请参阅 Antrea Egress 用户指南</p> </li> 
 <li> <p>在 Linux 上基于OpenFlow meters对OVS 数据面发送到 Antrea Agent的 PacketIn 消息进行限速；（ #2215，@GraysonWu @antoninbas ）</p> </li> 
 <li> <p>从 FlowAggregator 导出流记录时，为源和目标 Pod（如果适用）添加 K8s 标签作为 IPFIX 信息元素；（ #2240，@dreamtalen ）</p> </li> 
 <li> <p>使用antctl命令（antctl get featuregates）查看 Antrea Agent或Antrea Controller FeatureGates信息；(  #2082 , @luolanzone  )</p> </li> 
 <li> <p>Antrea Octant 插件支持重新运行最近一次 Traceflow 请求；（ #2202，@Dhruv-J ）</p> </li> 
 <li> <p>支持为 Pod 配置额外的SR-IOV网络接口（这些接口没有连接到 OVS 网桥），相应的用户API将在接下来的版本中提供。（ #2151，@ramay1 ）</p> </li> 
</ul> 
<p><strong>亮点一：更灵活的Egress IP 配置，支持Egress节点故障转移</strong></p> 
<p>添加新的 ExternalIPPool API 以定义可用作出口SNAT IP 的 IP地址范围；这些 IP 根据 nodeSelector 分配给节点，并在节点出现故障时支持故障转移；</p> 
<p>Egress资源是用来管理集群内Pods的出口流量的CRD API。它支持为Pod访问外部网络的流量指定出口IP（SNAT IP）和出口节点。当Egress应用于某个Pod时，它的出口流量将通过隧道传输到配置有对应Egress IP的节点（如果Egress IP所在的节点不同于Pod运行的节点的话），并经过SNAT将数据包源地址转换为Egress IP。</p> 
<p>示例：</p> 
<p>创建一个external IP Pool，命名为external-ip-pool，指定其可用IP范围，且nodeSelector只选定“kind-worker2”：</p> 
<pre><code>- apiVersion: crd.antrea.io/v1alpha2</code><code>  kind: ExternalIPPool</code><code>  metadata:</code><code>    name: external-ip-pool</code><code>  spec:</code><code>    ipRanges:</code><code>    - start: 10.10.0.11  # 10.10.0.11-10.10.0.20 can be used as Egress IPs</code><code>      end: 10.10.0.20</code><code>    nodeSelector: </code><code>      matchExpressions:</code><code>      - key: kubernetes.io/hostname</code><code>        operator: In</code><code>        values: ["kind-worker2"]</code></pre> 
<p>创建Egress，命名为egress-prod-web，指定其external IPPool为刚创建的external-ip-pool：</p> 
<pre><code>apiVersion: crd.antrea.io/v1alpha2</code><code>kind: Egress</code><code>metadata:</code><code>  name: egress-prod-web</code><code>spec:</code><code>  appliedTo:</code><code>    namespaceSelector:</code><code>      matchLabels:</code><code>        kubernetes.io/metadata.name: prod</code><code>    podSelector:</code><code>      matchLabels:</code><code>        app: web</code><code>  externalIPPool: external-ip-pool</code></pre> 
<p>查看Egress列表，看到系统在external-ip-pool指定的IP范围内自动为Egress分配了IP，并且将IP自动配置到了指定的节点“kind-worker2”：</p> 
<pre><code># kubectl get egress</code><code>NAME                 EGRESSIP       AGE   NODE</code><code>egress-prod-web      10.10.0.11     1m    kind-worker2</code></pre> 
<p>更详细的指导文档请参考：https://github.com/antrea-io/antrea/blob/v1.2.0/docs/egress.md</p> 
<p><strong>亮点二：在 Linux 上使用 OpenFlow 计量器实现packet-in报文限速</strong></p> 
<p>在Linux上使用OpenFlow计量器， OVS 数据路径发送到Antrea agent的PacketIn消息进行速率限制。</p> 
<p><strong>亮点三：在流记录中添加 Pod 标签信息 </strong></p> 
<p>从FlowAggregator导出流记录时，为源和目标Pod（如果适用）添加 K8s 标签作为IPFIX信息元素；标签信息是网络策略推荐应用所必需的，还可以增强Kibana 仪表板上的可用性。</p> 
<p><strong>亮点四：使用“antctl get featuregates”命令查看特性启用</strong></p> 
<p>使用 antctl 命令（“antctl get featuregates”）打印 Antrea Agent 和/或 Antrea Controller FeatureGates信息；</p> 
<p>示例：</p> 
<pre><code># antctl get featuregates</code><code>Antrea Agent Feature Gates</code><code>FEATUREGATE              STATUS         VERSION</code><code>AntreaProxy              Enabled        BETA</code><code>Egress                   Disabled       ALPHA</code><code>EndpointSlice            Disabled       ALPHA</code><code>Traceflow                Enabled        BETA</code><code>FlowExporter             Disabled       ALPHA</code><code>NetworkPolicyStats       Disabled       ALPHA</code><code>NodePortLocal            Disabled       ALPHA</code><code>AntreaPolicy             Enabled        BETA</code>
<code>Antrea Controller Feature Gates</code><code>FEATUREGATE              STATUS         VERSION</code><code>NetworkPolicyStats       Disabled       ALPHA</code><code>AntreaPolicy             Enabled        BETA</code><code>Egress                   Disabled       ALPHA</code><code>Traceflow                Enabled        BETA</code></pre> 
<p> </p> 
<p><img src="https://oscimg.oschina.net/oscnet/7234bf07-ee84-4c8a-84ca-4295eb72f4fe.png" referrerpolicy="no-referrer"></p> 
<p><strong>其他修改</strong></p> 
<p>新版本除了以上新特性外，还包括以下修改：</p> 
<ul> 
 <li> <p>在 Service 上启用 NodePortLocal 时，使用 Service 的目标端口而不是所选 Pod 的（可选）容器端口来确定如何为 Pod 配置端口转发。（#2222，@monotosh-avi）</p> </li> 
 <li> <p>更新go-ipfix依赖项的版本以提高 FlowExporter 性能。（#2129，@zyiou）</p> </li> 
 <li> <p>根据我们的 API 弃用策略删除弃用的API版本networking.antrea.tanzu.vmware.com/v1beta1。( #2265 , @hangyan )</p> </li> 
 <li> <p>当 Antrea 在 OVS 中执行 SNAT 时，在Traceflow observations中显示转换的源 IP 地址。( #2227 , @luolanzone )</p> </li> 
 <li> <p>从 FlowAggregator 导出的流记录中删除不必要的 IPFIX 信息元素：“originalExporterIPv4Address”、“originalExporterIPv6Address”和“originalObservationDomainId”。（#2361，@zyiou）</p> </li> 
 <li> <p>NodePortLocal 忽略非 TCP 服务端口，更新文档中关于支持协议的限制。（#2396，@antoninbas）</p> </li> 
 <li> <p>使用 OVS 用户空间数据路径（KinD集群）时，在 PREROUTING（使用 iptables）中丢弃上行链路接收到的数据包，以防止节点的TCP/IP协议栈处理这些数据包。（#2143，@antoninbas）</p> </li> 
 <li> <p>改进Antrea原生网络策略文档，添加关于 Antrea v1.1 ClusterNetworkPolicy API 引入的“namespace”字段的介绍。（#2271，@abhiraut）</p> </li> 
</ul> 
<p><img src="https://oscimg.oschina.net/oscnet/0d88a3f4-abbb-4467-814d-067fac33fc90.png" referrerpolicy="no-referrer"></p> 
<p><strong>问题修复</strong></p> 
<p>新版本还包括以下问题修复：</p> 
<ul> 
 <li> <p>修复禁用 AntreaProxy 时的节点间 ClusterIP 服务访问问题。（#2318，@tnqn）</p> </li> 
 <li> <p>修复在双栈集群中使用 IPv4 和 IPv6 Service组合时 AntreaProxy 中重复的组 ID 分配，这导致了Service连接问题。( #2317 , @hongliangl )</p> </li> 
 <li> <p>修复同时启用AntreaProxy和Egress 时节点内 ClusterIP 服务访问问题。（#2332，@tnqn）</p> </li> 
 <li> <p>修复大规模集群中GroupEntityIndex（在 Antrea Controller 中）初始化时的死锁；这导致了 NetworkPolicies不能正确分发和执行。（#2376，@tnqn）</p> </li> 
 <li> <p>修复包含空“From”字段（对于入口规则）或空“To”字段（对于出口规则）的ClusterNetworkPolicy的处理。（#2383，@Dyanngg）</p> </li> 
 <li> <p>在 Windows 上使用“os/exec”包替换第三方库来运行 PowerShell 命令配置主机网络，以解决第三方库存在的goroutine卡住的问题。( #2363 , @lzhecheng ) [Windows]</p> </li> 
 <li> <p>修复 Docker作为Windows节点的runtime时HNS Endpoint 在Pod被删除时没有被清理的问题。( #2306 , @wenyingd ) [Windows]</p> </li> 
 <li> <p>修复Windows节点上为Pod创建网络时访问HNS Network存在的race condition。（#2253，@tnqn）[Windows]</p> </li> 
 <li> <p>修复了向 OVS 发送 PacketOut 消息时的校验和计算错误。（#2273，@Dyanngg）</p> </li> 
 <li> <p>修复了 controlplane API 的内部和版本化类型之间的无效转换函数，这会导致JSON编码错误。（#2302，@tnqn）</p> </li> 
 <li> <p>修复了旧版“controlplane.antrea.tanzu.vmware.com”API 的 v1beta1 版本的实现：API 错误地使用了一些 v1beta2 类型，并且缺少一些字段选择器。（#2305，@tnqn）</p> </li> 
 <li> <p>验证创建HNSNetwork时自动发现的上行链路网卡不是虚拟网卡，并在验证失败时输出更友好的错误日志。（#2246，@tnqn）[Windows]</p> </li> 
 <li> <p>为 NodePortLocal 分配主机端口时，首先确保该端口可用并通过监听该端口来保留它。（#2385，@antoninbas）</p> </li> 
 <li> <p>将 NodePortLocal 的默认端口范围更改为 61000-62000，以避免与 Linux 上的默认ip_local_port_range 冲突。（#2382，@antoninbas）</p> </li> 
 <li> <p>将NamespaceIndex 添加到 NodePortLocal Controller 的PodInformer以避免错误日志提示和慢查询。（#2377，@tnqn）</p> </li> 
 <li> <p>当mutating webhook处理Antrea原生网络策略时，仅在“Patch”内容不为空时设置响应内容中的“PatchType”字段，否则响应会被认为无效。（#2295，@Dyanngg）</p> </li> 
 <li> <p>修复 FlowAggregator 中的“egressNetworkPolicyRuleAction”IPFIX 信息元素。（#2228，@zyiou）</p> </li> 
 <li> <p>修复Antrea Octant 插件中访问Traceflow 状态存在的race condition（在多个浏览器会话的情况下）。（#2261，@antoninbas）</p> </li> 
 <li> <p>删除从 Antrea agent调用ovs-appctl时只存在单个ovs-vswitchd.ctl 文件的假设。（#2260，@antoninbas）</p> </li> 
 <li> <p>修复antrea/antrea-ubuntu Docker镜像中whereabouts二进制文件权限问题。（#2353，@antoninbas）</p> </li> 
</ul> 
<p> </p> 
<p><img src="https://oscimg.oschina.net/oscnet/aa18987f-8b19-4b01-ad58-a3192d8b10fc.png" referrerpolicy="no-referrer"></p> 
<p><strong>致谢</strong></p> 
<p>随着v1.2.0版本的发布，Antrea提供了更完备的Egress功能，更加友好便捷的用户体验。</p> 
<p>社区的繁荣离不开贡献者的支持，感谢每一位社区贡献者！</p> 
<ul> 
 <li> <p>https://github.com/abhiraut</p> </li> 
 <li> <p>https://github.com/antoninbas</p> </li> 
 <li> <p>https://github.com/Dhruv-J</p> </li> 
 <li> <p>https://github.com/dreamtalen</p> </li> 
 <li> <p>https://github.com/Dyanngg</p> </li> 
 <li> <p>https://github.com/hangyan</p> </li> 
 <li> <p>https://github.com/hongliangl</p> </li> 
 <li> <p>https://github.com/luolanzone</p> </li> 
 <li> <p>https://github.com/lzhecheng</p> </li> 
 <li> <p>https://github.com/monotosh-avi</p> </li> 
 <li> <p>https://github.com/ramay1</p> </li> 
 <li> <p>https://github.com/tnqn</p> </li> 
 <li> <p>https://github.com/wenyingd</p> </li> 
 <li> <p>https://github.com/wenqiq</p> </li> 
 <li> <p>https://github.com/zyiou</p> </li> 
</ul> 
<p><img src="https://oscimg.oschina.net/oscnet/f11e701d-4085-4d7b-8831-e3c4827839fe.png" referrerpolicy="no-referrer"></p> 
<p><strong>关于 Antrea</strong></p> 
<p>Antrea项目是一个基于 Open vSwitch（OVS）的开源 Kubernetes CNI 网络解决方案，旨在为 Kubernetes 集群提供更高效、更安全的跨平台网络和安全策略。</p> 
<p>2021年4月28日，经云原生计算基金会（CNCF）技术监督委员会（TOC）投票决议，Antrea成为CNCF沙箱级项目（Sandbox Project）。</p> 
<p>GitHub：https://github.com/antrea-io/antrea</p> 
<p>官网：https://antrea.io</p>
                                        </div>
                                      
</div>
            