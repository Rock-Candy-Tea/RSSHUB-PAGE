
---
title: 'Antrea v1.3.0 版本发布：支持 WireGuard 传输加密和基于 FQDN 的网络策略'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=7973'
author: 开源中国
comments: false
date: Mon, 13 Sep 2021 17:59:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=7973'
---

<div>   
<div class="content">
                                                                                            <p><strong>引言</strong></p> 
<p>Antrea 项目是一个基于 Open vSwitch（OVS）的开源 Kubernetes CNI 网络解决方案，旨在为 Kubernetes 集群提供更高效、更安全的跨平台网络和安全策略。2021 年 4 月，Antrea 正式成为 CNCF 沙箱级项目（Sandbox Project）。</p> 
<p>Antrea Github 地址：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fantrea-io%2Fantrea" target="_blank">https://github.com/antrea-io/antrea</a></p> 
<p>北京时间 2021 年 09 月 03 日，Antrea 发布了新版本 v1.3.0。主要包括对基于 DNS/FQDN 名称的网络安全策略的支持，和支持 WireGuard 加密跨主机 Pod 流量，以及其他更新和修改。</p> 
<p>Antrea v1.3.0 Release 文档：</p> 
<p><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fantrea-io%2Fantrea%2Freleases%2Ftag%2Fv1.3.0" target="_blank">https://github.com/antrea-io/antrea/releases/tag/v1.3.0</a></p> 
<p><strong>新增特性</strong></p> 
<p>本次发布的 1.3.0 版本新特性包括：</p> 
<ul> 
 <li>Antrea 原生网络策略增加对全限定域名（FQDNs）的支持。FQDN 过滤规则可以使用通配符。(#2613 #2634 #2667 #2623 #2691, @Dyanngg @antoninbas @GraysonWu @madhukark @lzhecheng)</li> 
 <li>对使用 WireGuard 加密跨主机 Pod 流量的支持。目前对此类流量加密可以选择 IPsec 或者 WireGuard。如果需要启用 WireGuard，流量封装模式必须指定为 encap。同时隧道类型选项将被忽略。(#2297 #2697, @xliuxu @tnqn)</li> 
 <li>增加可配置的网卡接口用于传输 Pod 流量。(#2370, @wenyingd)</li> 
</ul> 
<ol start="2"> 
 <li>在 Windows 节点中，SNAT 现在将在主机端执行，不再由 OVS 执行。 <pre><code><ol>
<li>增加了一个配置项 transportInterface 用于指定哪个网卡将被 Antrea Agent 用于传输 Pod 流量。默认行为保持不变，即默认会使用包含 Kubernetes 节点 IP 的网卡。</li>
</ol>
</li>
</code></pre> </li> 
</ol> 
<ul> 
 <li>对双协议栈网卡（网卡同时配置了 IPv4 和 IPv6 地址）的支持，因此目前可以在双协议栈集群中启用 noEncap 流量封装模式。 (#2436, @lzhecheng)</li> 
 <li>在 ExternalIPPool CRD 中增加状态字段，可以显示 ExternalIPPool 已用 IP 数量以及总的 IP 数量。(#2490, @wenqiq)</li> 
 <li>Egress 新增对 IPv6 以及 IPv4/IPv6 双协议栈集群的支持。(#2196 #2655, @wenqiq)</li> 
 <li>antctl supportbundle 命令增加了时间戳参数，可以对收集到的日志进行过滤。(#2389, @hangyan@weiqiangt)</li> 
 <li>增加对 IPv6 以及 IPv4/IPv6 双协议栈 Kind 集群的支持。(#2415, @adobley @christianang @gwang550)</li> 
 <li>在 Flow Aggregator 中增加对 JSON 格式日志的支持以便在使用 Logstash 时提供更好的性能，目前 IPFIX 仍为默认的日志格式。(#2559, @zyiou)</li> 
 <li>“antctl get networkpolicy” 命令增加 “–sort-by” 选项。(#2604, @antoninbas)</li> 
</ul> 
<p><strong>亮点一：Antrea 原生网络策略增加对全限定域名（FQDNs）的支持。</strong></p> 
<p>Antrea 原生网络策略配置于出口流量时可以指定域名作为筛选条件。域名可以支持通配符，支持的动作包括 Allow, Drop 和 Reject。一个简单的例子如下：</p> 
<pre><code>apiVersion: crd.antrea.io/v1alpha1
kind: ClusterNetworkPolicy
metadata:
  name: acnp-fqdn-all-foobar
spec:
  priority: 1
  appliedTo:
  - podSelector:
      matchLabels:
        app: client
  egress:
  - action: Drop
    to:
      - fqdn: "*foobar.com"
</code></pre> 
<p>上面的例子会丢弃所有标签中包含 app: client 的 Pod 发送到*<a href="https://www.oschina.net/action/GoToLink?url=http%3A%2F%2Ffoobar.com" target="_blank">foobar.com</a> 域名的流量。</p> 
<p>注意这个特性只工作在三层或四层，此外此项功能无法作用于 Kubernetes 为 Service 创建的 DNS 域名（例如 kubernetes.default.svc 或者 antrea.kube-system.svc，Headless Service 不受此限制影响）。</p> 
<p><strong>亮点二：支持使用 WireGuard 加密跨主机 Pod 流量。</strong></p> 
<p>WireGuard 可以用于加密跨主机的 Pod 间流量，在特定场景下 WireGuard 相较于 IPsec 提供更好的吞吐量。</p> 
<p>要启用此功能只需要修改 Antrea 的 Configmap 将 trafficEncryptionMode 指定为 WireGuard，此时跨主机流量将被 WireGuard 加密封装，Antrea 的流量封装模式（trafficEncapMode）必须指定为 encap。此外，隧道类型的选项将被忽略。</p> 
<p><strong>其他修改</strong></p> 
<ul> 
 <li>移除 ClusterGroup 必须存在才可以作为其他 ClusterGroup 的子组的限制。(#2443, @Dyanngg)</li> 
 <li>移除 ClusterGroup 必须存在才可以被 Antrea ClusterNetworkPolicy 引用的限制。(#2478, @Dyanngg @abhiraut)</li> 
 <li>依据 API 弃用规则移除了 “<a href="https://www.oschina.net/action/GoToLink?url=http%3A%2F%2Fcontrolplane.antrea.tanzu.vmware.com%2Fv1beta1%25E2%2580%259D" target="_blank">controlplane.antrea.tanzu.vmware.com/v1beta1”</a> API。(#2528 #2631, @luolanzone)</li> 
 <li>Controller 对 ClusterGroup 成员的查询接口 (“/clustergroupmembers” API) 的返回中将包含 IPBlocks 列表。(#2577, @Dyanngg @abhiraut)</li> 
 <li>对所有属于同一个 Service 的 Endpoint 安装一条 Openflow bundle 以减少 Agent 启动时安装流规则的时间。(#2476, @tnqn)</li> 
 <li>优化 Agent 启动时 NetworkPolicy 规则的批量安装，仅依据最终的状态生成流规则而非增量安装。(#2479, @tnqn @Dyanngg)</li> 
 <li>用 GroupMemberSet.Merge 代替 GroupMemberSet.Union 以降低 Agent 中 policy controller 的 CPU 和内存占用。(#2467, @tnqn)</li> 
 <li>优化 iptables 规则查询，避免枚举所有规则链以减少 Agent 的内存消耗。(#2458, @tnqn)</li> 
 <li>考虑在特定场景下 Agent 会在较长时间内无法连接到 Controller，优化 Agent 的就绪探针，可以容忍更多次的失败。(#2535, @tnqn)</li> 
 <li>去掉了在启用 IPsec 加密时只能选择 GRE 隧道的限制，目前 VXLAN 和 GENEVE 都可以被支持（需要较新 Kernel 支持）。 (#2489, @luolanzone)</li> 
 <li>对 NetworkPolicy 审计日志中的拒绝连接日志进行自动去重，在 1 秒种之内的所有被拒绝的连接将被合并成一条日志，该日志将包含拒绝连接的次数。(#2294 #2578, @qiyueyao)</li> 
 <li>当部分节点无响应时支持返回部分 supportbundle 的结果。(#2399, @hangyan)</li> 
 <li>当 NetworkPolicyStats Feature Gate 未被开启时如果从 Controller API 中获取 NetworkPolicyStats 时将返回空的列表而非错误。(#2386, @PeterEltgroth)</li> 
 <li>将 OVS 从 2.14.2 更新到 2.15.1 ，新版本修复了 userspace datapath 中对 Geneve 隧道的支持，此功能用于 Kind 集群。(#2515, @antoninbas)</li> 
 <li>更新 go-ipfix 到 v0.5.7，以对 FlowExporter 功能特别是 Flow Aggregator 模块提供更好的性能支持。(#2574, @srikartati @zyiou)</li> 
 <li>对 AntreaAgentInfo 和 AntreaControllerInfo CRD 添加格式化输出。(#2572, @antoninbas)</li> 
 <li>优化了 Egress 状态更新，当 Egress IP 为用户手动配置时，系统匹配到 IP 对应的节点将自动更新 Egress 状态为对应节点名称。(#2444, @wenqiq)</li> 
 <li>将 ClusterGroup CRD 的单数名称由 “group” 更新为 “clustergroup”。(#2484, @abhiraut)</li> 
 <li>将官方支持的 Go 版本由 1.15 更新为 1.17，此更新中需要注意的是 “net” 包中 “ParseIP” 和 “ParseCIDR” 的实现的变化。Antrea 用户不受影响。[参考<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fantrea-io%2Fantrea%2Fissues%2F2606%23issuecomment-901502141%255C%255C" target="_blank">https://github.com/antrea-io/antrea/issues/2606#issuecomment-901502141\\\\</a>] (#2609 #2640, @antoninbas)</li> 
 <li>将保留 OVS 寄存器范围和定义常量的过程标准化，OVS 寄存器将被用于存储单个数据包的信息以用来实现特定的功能。(#2455, @wenyingd)</li> 
 <li>更新 ELK 相关参考配置以支持 TCP 传输。(#2387, @zyiou)</li> 
 <li>更新 Windows 安装指引。(#2456, @lzheheng)</li> 
 <li>更新 Antrea 原生规则相关文档以同步 Kubernetes 上游对 “<a href="https://www.oschina.net/action/GoToLink?url=http%3A%2F%2Fkubernetes.io%2Fmetadata.name%25E2%2580%259D" target="_blank">kubernetes.io/metadata.name”</a> 标签的支持。(#2596, @abhiraut)</li> 
 <li>在 Vagrant 配置的测试集群中使用 containerd 作为容器运行时。(#2583, @stanleywbwong)</li> 
 <li>更新了 Antrea 原生规则文档中 AllowToCoreDNS 的例子。(#2605, @btrieger)</li> 
 <li>将 Github 工作流中的 “actions/setup-go” 更新至 v2 版本。(#2517, @MysteryBlokHed)</li> 
</ul> 
<p><strong>问题修复</strong></p> 
<ul> 
 <li>修复了计算 NetworkPolicy 中新增规则的统计数据时的空指针异常。(#2495, @tnqn)</li> 
 <li>修复了在双协议栈集群中安装 iptables 规则时，如果其中只有一个协议栈的规则已被安装，则安装过程可能被跳过的错误。(#2469, @lzhecheng)</li> 
 <li>修复了 Agent 由 FlowExporter 中的导出协程和 conntrack 池协程导致的死锁问题。(#2429, @srikartati)</li> 
 <li>将 Windows 节点的 OVS 版本更新到 2.14.2-antrea.1，此版本基于上游 2.14.2 正式版并修复了使用 DNAT 时计算 TCP 校验和的问题。(#2549, @lzhecheng)</li> 
 <li>修复了在 NodePortLocal 初始化时，恢复 iptables 规则时暂时性的错误（由 xtables 锁竞争引起）。(#2555, @antoninbas)</li> 
 <li>在 Agent 启动时检查 OVS datapath 所支持的特性列表，如果缺失 Antrea 必须的特性则 Agent 会输出错误日志并退出，而非继续尝试运行。(#2571, @tnqn)</li> 
 <li>在 Linux 节点在运行 ovs-apptcl 命令之前等待 ovs-vswitchd 的 PID 文件变为就绪。(#2695, @tnqn)</li> 
 <li>在 Flow Exporter 中周期性删除无法被导出的过期连接，以避免内存溢出错误。(#2516, @srikartati)</li> 
 <li>修复了由 Antrea Agent 流表中产生的拒绝数据包可能在两个被 network policies 拒绝的端点中无限循环的问题。(#2579, @GraysonWu)</li> 
 <li>修复了 Linux 内核版本号解析的问题以适应更多的发行版，如 RHEL / CentOS。(#2450, @Jexf)</li> 
 <li>修复了 IPsec 隧道设备命名时，由于节点名称中可能包含 “-”，当用于设备名的首字符时不合法的问题。(#2486, @luolanzone)</li> 
 <li>当创建到远端节点的 IPsec OVS 隧道端口时，优雅处理端口已经存在但是配置已经过期的问题。(#2582, @luolanzone)</li> 
 <li>修复了当 Baseline 层 Antrea 原生网络策略应用于流时 Flow Exporter 报告的策略信息。(#2542, @zyiou)</li> 
 <li>周期性清除 Flow Aggregator 产生的日志文件，此前 “–log_file_max_size”和“–log_file_max_num” 被错误地忽略。(#2522, @srikartati)</li> 
 <li>修复了当 FlowAggregator 发送第一条流日志时缺失的模版 ID。(#2546, @zyiou)</li> 
 <li>确保从环境变量或者主机名读取的 Windows 节点名称被转换为小写。(#2672, @shettyg)</li> 
 <li>修复了 Windows 中 Antrea 清理网络的脚本，移除了 Hyper-V 对用于 OVS uplink 网卡的绑定以使之可以正确恢复其 IP 地址。(#2550, @wenyingd)</li> 
 <li>修复了 Logstash 的参考配置以避免在计算吞吐量时 0 作为除数的问题 (#2432, @zyiou)</li> 
 <li>修复了在收集 support bundle 时，由于 antrea-agent 镜像没有包含 iproute2 时可能产生的空指针异常问题。此问题不涉及 antrea-ubuntu 镜像。(#2598, @liu4480)</li> 
</ul> 
<p><strong>致谢</strong></p> 
<p>随着 v1.3.0 版本的发布，Antrea 提供了 NetworkPolicy 全限定域名（FQDNs）的功能支持，同时支持 WireGuard 加密跨主机 Pod 流量，对集群网络安全性和性能将有很大提升。</p> 
<p>社区的繁荣离不开贡献者的支持，感谢每一位社区贡献者！</p> 
<ul> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fabhiraut" target="_blank">https://github.com/abhiraut</a></li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fadobley" target="_blank">https://github.com/adobley</a></li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fantoninbas" target="_blank">https://github.com/antoninbas</a></li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fbtrieger" target="_blank">https://github.com/btrieger</a></li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fchristianang" target="_blank">https://github.com/christianang</a></li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FDyanngg" target="_blank">https://github.com/Dyanngg</a></li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FGraysonWu" target="_blank">https://github.com/GraysonWu</a></li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgwang550" target="_blank">https://github.com/gwang550</a></li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fhangyan" target="_blank">https://github.com/hangyan</a></li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fhongliangl" target="_blank">https://github.com/hongliangl</a></li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FJexf" target="_blank">https://github.com/Jexf</a></li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fluolanzone" target="_blank">https://github.com/luolanzone</a></li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Flzhecheng" target="_blank">https://github.com/lzhecheng</a></li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fliu4480" target="_blank">https://github.com/liu4480</a></li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fmadhukark" target="_blank">https://github.com/madhukark</a></li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FMysteryBlokHed" target="_blank">https://github.com/MysteryBlokHed</a></li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FPeterEltgroth" target="_blank">https://github.com/PeterEltgroth</a></li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fqiyueyao" target="_blank">https://github.com/qiyueyao</a></li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fshettyg" target="_blank">https://github.com/shettyg</a></li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fsrikartati" target="_blank">https://github.com/srikartati</a></li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fstanleywbwong" target="_blank">https://github.com/stanleywbwong</a></li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Ftnqn" target="_blank">https://github.com/tnqn</a></li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fweiqiangt" target="_blank">https://github.com/weiqiangt</a></li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fwenyingd" target="_blank">https://github.com/wenyingd</a></li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fwenqiq" target="_blank">https://github.com/wenqiq</a></li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fxliuxu" target="_blank">https://github.com/xliuxu</a></li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fzyiou" target="_blank">https://github.com/zyiou</a></li> 
</ul> 
<p><strong>Antrea 中文社区</strong></p> 
<p>欢迎加入 Antrea 中文社区。</p> 
<p>GitHub：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fantrea-io%2Fantrea" target="_blank">https://github.com/antrea-io/antrea</a></p> 
<p>官网：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fantrea.io" target="_blank">https://antrea.io</a></p> 
<p>微信群：请搜索添加 “Antrea” 微信官方公众号进群</p> 
<p><strong>参考链接</strong></p> 
<p><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fantrea-io%2Fantrea" target="_blank">https://github.com/antrea-io/antrea</a></p> 
<p><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fantrea-io%2Fantrea%2Freleases%2Ftag%2Fv1.3.0" target="_blank">https://github.com/antrea-io/antrea/releases/tag/v1.3.0</a></p>
                                        </div>
                                      
</div>
            