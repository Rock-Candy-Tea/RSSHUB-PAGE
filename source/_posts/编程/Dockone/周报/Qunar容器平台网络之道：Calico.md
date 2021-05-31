
---
title: 'Qunar容器平台网络之道：Calico'
categories: 
 - 编程
 - Dockone
 - 周报
headimg: 'https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210529/74007a1b29ce8a7f7c8c5e1240d31af4.jpg'
author: Dockone
comments: false
date: 2021-05-31 00:45:01
thumbnail: 'https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210529/74007a1b29ce8a7f7c8c5e1240d31af4.jpg'
---

<div>   
<br><h3>简介</h3>Calico 是一个开源的 CNI 项目，为容器化应用提供的网络解决方案，下面来为大家简单介绍一下我们是如何使用 Calico 为容器化提供网络功能的。<br>
<h3>Calico架构</h3>简单说一下 Calico 架构，Calico 是一个基于三层的数据中心网络方案，可作为 CNI 插件为运行于 Kubernetes 中的容器提供基于 TCP/IP 三层的网络通信方案，也可与 OpenStack 这种 IaaS 云架构集成，利用 BGP，IPIP 等协议为工作负载提供网络联通功能，能够提供高效可控的 VM、容器、物理机之间的通信。<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210529/74007a1b29ce8a7f7c8c5e1240d31af4.jpg" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210529/74007a1b29ce8a7f7c8c5e1240d31af4.jpg" class="img-polaroid" title="1.jpg" alt="1.jpg" referrerpolicy="no-referrer"></a>
</div>
<br>
<em>图1. 核心组件</em><br>
<br>Calico的核心组件包括：<br><br>
<ul><li>Felix，Calico Agent，运行在每个容器宿主节点上，主要负责配置路由、ACL等信息来确保容器的联通状态；  </li><li>etcd ，分布式的 Key/Value 存储，负责网络元数据一致性，确保 Calico 网络状态的准确性；  </li><li>BGP Client（Bird），主要把 Felix 写入 Kernel 的路由信息分发到 Calico 网络，保证容器间的通信有效性；  </li><li>BGP Route Reflector（简称：RR ），路由反射器，默认 Calico 工作在 node-mesh 模式，所有节点互相连接， node-mesh 模式在小规模部署时工作是没有问题的，当大规模部署时，连接数会非常大，消耗过多资源，利用 BGP RR ，可以避免这种情况的发生，通过一个或者多个 BGP RR 来完成集中式的路由分发，减少对网络资源的消耗以及提高 Calico 工作效率、稳定性。</li></ul><br>
<br>Calico 在每一个容器宿主节点上利用 Linux kernel 实现了一个高效的 vRouter 来负责数据转发 而每个 vRouter 通过 BGP 协议负责把自己上运行的 workload 的路由信息向整个 Calico 网络内传播。<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210529/791a10058b8591b26d69843943bbbb0b.jpg" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210529/791a10058b8591b26d69843943bbbb0b.jpg" class="img-polaroid" title="2.jpg" alt="2.jpg" referrerpolicy="no-referrer"></a>
</div>
<br>
<em>图2. 数据路径</em><br>
<h3>Calico 在 Qunar 的使用</h3>在 Qunar 的网络环境中，主机域名是一个较强的依赖因素，比如 Nginx/OR 就需要可以 IP 直达的 upstream 成员，而此需求容器本身或者 Kubernetes 并无法直接满足，所以在 2017 年开始测试使用 Kubernetes 作为容器编排工具时， Pod 可被直接访问就是一个必须的测试要素，经过一段时间的测试使用，从 Flannel ， Cilium ， Calico 等方案中，我们选择了 Calico 。<br>
<br>Calico 已经在我们的 ESAAS 专用集群中为 4000+ 的 Pod 提供网络功能，目前线上业务集群也选择使用 Calico 方案，选择 Calico 方案的主要因素：<br>
<ul><li>纯三层方案，因为没有 Overlay 网络，方案简单可控，并且没有解包封包，节省 CPU 计算资源的同时，提高了整个网络的性能，并且三层方案不会因为容器数量变化带来 ARP 广播风暴，也不用担心因为容器的频繁启动停止所带来的网络扰动，保证了网络的稳定性；  </li><li>Pod ip，Sevice ip 均可路由直达，没有类似 NAT 的中间环节，所有数据流量通过 IP 包的方式完成互联；  </li><li>适合大规模部署的方案</li></ul><br>
<br>总结以上就是 Calico 网络方案简单，高效，稳定，适合用于大规模的生产环境。<br>
<br>Qunar 容器云平台使用 Kubernetes 编排容器， Calico 作为 DaemonSet 部署在集群的每个宿主节点上，为了适合大规模应用，我们使用了 Calico RR 模式，将机架交换机做为路由反射器与宿主节点建立起 BGP 邻居联系，所有宿主节点都配置为同一个 AS Number，每个宿主节点都会向机架交换机宣告到本地容器IP的路由，再由交换机向同一 AS 域内的其它节点宣告。<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210529/e9e5fd97ebac3ba9acf08c1835f775f8.jpg" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210529/e9e5fd97ebac3ba9acf08c1835f775f8.jpg" class="img-polaroid" title="3.jpg" alt="3.jpg" referrerpolicy="no-referrer"></a>
</div>
<br>
*图3. 宿主的 BGP Peer 列表 * <br>
<br>通过图3 可以看到，宿主 Node1 的 BGP Peer 是两个机架交换机的 IP 地址，配置两个 Peer 也是出于冗余的考虑，当其中一个 Peer 连接失败，路由信息还可以通过另一个 Peer 进行宣告，不影响线上业务。<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210529/32bd39f8fa4b4aff26ee835ace3b6614.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210529/32bd39f8fa4b4aff26ee835ace3b6614.png" class="img-polaroid" title="4.png" alt="4.png" referrerpolicy="no-referrer"></a>
</div>
<br>
<em>图4. 整体架构</em><br>
<br>如图 4 所示，所有 Kubernetes Node 通过两块 10G 网卡做 Bonding 同时连接两台机架交换机，和机架交换机建立 IBGP 连接，机架交换机和核心交换机通过 EBGP 连接， Kubernetes 集群使用统一的 AS Number 。下面是 Calico 的 BgpPeer 配置：<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210529/559316691f838065d2446b0699ed259e.jpg" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210529/559316691f838065d2446b0699ed259e.jpg" class="img-polaroid" title="5.jpg" alt="5.jpg" referrerpolicy="no-referrer"></a>
</div>
<br>
<em>图5. BgpPeer 配置</em><br>
<h4>Calico IPAM</h4>Calico 分配 IP 地址的原则为，将整个 IPPool 分为多个地址块（Block），每个 Node 获得一个 Block ，当有 Pod 调度到某个 Node 上时，Node 优先使用 Block 内的地址。通过 BGP 学习到到其它宿主的路由条目，并且自己也会向外宣告本地的路由条目，如此集群内的宿主就可以相互学习到彼此的路由条目，并且由 Felix 添加到本地的路由表中，这样所有宿主就都知道集群内其它宿主拥有的 Block 了。<br>
<h4>同一 Kubernetes 集群内 Pod 间的通信</h4><div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210529/ac20132d11fb0bb98ec1e34b5074c6e1.jpg" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210529/ac20132d11fb0bb98ec1e34b5074c6e1.jpg" class="img-polaroid" title="6.jpg" alt="6.jpg" referrerpolicy="no-referrer"></a>
</div>
<br>
<em>图6. 同一集群内 Pod 访问流量</em><br>
<br>同一集群内的 Pod 如何相互通信呢，如上图所示，观察绿色线段， Container1 请求的访问 Container4 ，请求会先经过 veth pair calixxxx 的虚拟网卡进入到宿主网络栈，并在宿主 Node1 的路由表中会查找到 Container4 IP 所属网段的路由：10.10.1.0/26 via 10.10.5.10 dev bond0 proto bird ，这条路由就是由 Node2 在 Calico 分配了 IP Block 之后宣告出来的，意思是去往目标地址在 10.66.1.0/26 内的下一跳地址是 10.10.5.10，也就是 Node2 的 IP 地址，当数据包到达宿主 Node2 上时，会查询匹配到目标 IP 为 10.10.1.13 的路由：10.10.1.3 dev cali11239f98883 scope link ，这条路由是 Ceontainer4 被调度到 Node2 上后由 Calico 添加的，最终数据包通过 veth pair cali11239f98883 进入到 Container4 中，这个数据通路反过来也是一样，所以两个 Pod 就可以建立连接相互通信了。<br>
<h4>Kubernetes 集群内 Pod 与外部网络的通信：</h4>了解了统一集群内的 Pod 如何相互通信，容器与集群外部地址通信就好理解了。由于机架交换机与核心交换机建立的 EBGP 连接，会将集群的路由向核心交换机宣告，所有到容器网络访问，核心交换机都会将数据包转发给对应机架交换机。当某一个 Pod 要去访问外部的地址时（比如：位于集群外部网络的 gitlab ），我们通过 traceroute 的输出看到：<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210529/dafda9a6e274852d56a923bacc825a9f.jpg" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210529/dafda9a6e274852d56a923bacc825a9f.jpg" class="img-polaroid" title="7.jpg" alt="7.jpg" referrerpolicy="no-referrer"></a>
</div>
<br>
<em>图7. 访问集群外地址路径</em><br>
<br>第一跳：是容器所在宿主 IP<br>
<br>第二跳：是宿主 bond0 IP所在 VLAN 的网关<br>
<br>第三跳和第四跳：是机架交换机和核心交换机的互联地址<br>
<br>第五跳：是核心交换机地址<br>
<br>第六跳和第七跳：也是网络设备的地址，已经进入到 Qunar 的基础网络<br>
<br>第八跳：最后一跳，到达目标地址<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210529/65c1307eb0992e8c095d66752ae13fc9.jpg" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210529/65c1307eb0992e8c095d66752ae13fc9.jpg" class="img-polaroid" title="8.jpg" alt="8.jpg" referrerpolicy="no-referrer"></a>
</div>
<br>
<em>图8. 访问集群外流量</em><br>
<h3>问题</h3>在 Calico 使用过中，也发现了一些问题，比如下面这个问题， Calico IPAM 分配 IP 的时候，是按照如下逻辑进行的：<br>
<ol><li>如果节点已有绑定 IP Block ，则从此 IP Block 中分配 IP；  </li><li>如果第一步中无可用 IP 分配或者宿主没有已绑定的 IP Block，则会从 IP Pool 中查找一个未绑定的 IP Block 给宿主，再执行 IP 分配策略；  </li><li>如果第二步失败，则会从所有 IP Block 中查找一个未使用的 IP。</li></ol><br>
<br>这就会有个问题，在所有 IP Block 都分配给宿主后，当一个新宿主加入集群，那这个宿主上启动的容器就会分到一个已分配 IP Block 中的可用 IP（IP Borrowing），问题是， Calico 在利用 BIRD 进行 BGP 路由广播时，针对每个已绑定的 IP Block 会设置 blackhole 路由，而这个 IP 由于黑洞路由的存在是不能与之通信的。在 Calico 3.14 之前的版本中我们对这个问题的解决方案是在集群规划时，同时关联考虑 IP 和集群大小，同时添加 IP Block 使用监控，在 IP Block 即将耗尽时能及时添加新的 IP Pool，3.14及之后的版本，可以配置打开 strict IP affinity 来关闭 IP Borrowing。<br>
<br><h3>总结</h3>至此我们了解了容器是如何互通以及如何与集群外部地址通信。Calico 还有很多更深入的功能及用法，比如适应超大规模的 Typha 模式，可以为更大规模的容器化平台提供健壮高效的网络功能。后期我们也会根据实际使用场景，调整配置，配合业务的需求和发展。<br>
<br>原文链接：<a href="https://mp.weixin.qq.com/s/Tmx8oiC-QlcbwfJsS3dvxg" rel="nofollow" target="_blank">https://mp.weixin.qq.com/s/Tmx8oiC-QlcbwfJsS3dvxg</a>
                                                                <div class="aw-upload-img-list">
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                </div>
                                
                                                                <ul class="aw-upload-file-list">
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    </ul>
                                                              
</div>
            