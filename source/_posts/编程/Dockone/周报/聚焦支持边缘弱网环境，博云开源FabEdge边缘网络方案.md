
---
title: '聚焦支持边缘弱网环境，博云开源FabEdge边缘网络方案'
categories: 
 - 编程
 - Dockone
 - 周报
headimg: 'https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210804/a077968413f8ce099a262effe5252516.jpg'
author: Dockone
comments: false
date: 2021-08-07 02:22:05
thumbnail: 'https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210804/a077968413f8ce099a262effe5252516.jpg'
---

<div>   
<br>2021 年 8 月 2 日，博云正式开源 FabEdge 边缘网络方案。FabEdge 是一款基于 kubernetes 和 kubeedge 构建的开源网络方案，解决边缘计算场景下，容器网络配置管理复杂、网络割裂互不通信、缺少服务发现、缺少拓扑感知能力、无法提供就近访问等难题。<br>
并且，Fabedge 支持弱网环境，如4/5G，WiFi，LoRa 等；支持边缘节点动态 IP 地址，适用于物联网，车联网等场景。<br>
<br>目前，FabEdge 项目代码已在Github上开源，项目地址为：<a href="https://github.com/FabEdge/fabedge" rel="nofollow" target="_blank">https://github.com/FabEdge/fabedge</a>。项目使用 Apache 2.0 协议，欢迎更多技术开发者和爱好者前去试用和使用。<br>
<br>01<br>
Features  五大特性<br>
• Kubernetes 原生支持：完全兼容的 Kubernetes API ，无需额外开发，依赖较少的通用开源组件，即插即用。<br>
• 边缘容器网络管理：为边缘节点实现网络地址段管理，以及边缘容器网络地址分配。<br>
• 边云协同/边边协同：通过隧道技术打通边缘容器与云端容器，以及边缘节点间容器的相互安全通信，实现边云协同和边边协同。<br>
• 边缘 “ 社区 ”：使用“社区” CRD 自定义资源控制哪些边缘节点可以互相通讯。<br>
• 就近访问：优先使用本地服务，其次使用云端服务。<br>
<br>02<br>
Advantages  三大优势<br>
标准 —— 完全兼容 k8s api, 即插即用支持任何标准 k8s 集群；<br>
<br>安全  —— 所有通讯使用基于证书的 IPSEC 隧道；<br>
<br>易用  —— 使用 Operator 机制，最少化的人工运维代价。<br>
<br>03<br>
How it works?<br><br>
云端是标准 Kubernete 集群，可以使用任何 CNI 网络插件，比如 Calico。在集群里运行 KubeEdge 云端组件 cloudcore，在边缘节点运行 KubeEdge 边缘组件 edgecore ，边缘节点注册到云端集群，<br>
Fabedge有三个组件组成，分别是：Operator、 Connector 和 Agent。<br>
Operator 运行在云端集群，监控节点，服务等资源变化，动态为边缘节点维护configmap ，同时为每个边缘节点生成 Agent ；Connector 运行在云端，负责云端网络配置管理，并在云端和边缘节点转发流量；而 Agent 消费 configmap 信息，动态维护本节点隧道、路由、iptables 等网络配置。<br>
<br><div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210804/a077968413f8ce099a262effe5252516.jpg" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210804/a077968413f8ce099a262effe5252516.jpg" class="img-polaroid" title="微信图片_20210804170321.jpg" alt="微信图片_20210804170321.jpg" referrerpolicy="no-referrer"></a>
</div>
<br>
<br>FabEdge 架构图<br>
<br>FabEdge利用两个通道实现云边数据交换，一个是kubeedge管理的websock/quic 通道，用于控制信令；另一个是 FabEdge 自身管理的加密隧道，用于应用之间的数据传输。<br>
Operator 在云端监听 node、service、endpoint 等 k8s 资源，为每个边缘节点生成一个 configmap，包含本节点的子网、隧道、负载均衡等相关配置信息。同时 operator 负责为每个边缘节点生成相应的 pod，用于启动本节点上的agent。<br>
Connector 负责终结到边缘节点加密隧道，在云和边缘节点进行流量转发。它依赖云端CNI插件将流量转发到 connector 以外的节点，目前支持的云端 CNI 插件是 callico 。<br>
边缘节点使用社区 CNI 插件 bridge 和 host-local，是使用社区 node-local-dns 地址解析功能，负责本节点的域名解析和缓存。<br>
每个边缘节点运行一个 agent ，消费本节点对应 configmap，包括以下功能：<br>
管理本节点 CNI 插件的配置文件<br>
管理本节点安全隧道<br>
管理本节点的负载均衡信息，会优先使用本地服务后端，其次是用云端后端<br>
<br>04<br>
FabEdge vs Calico/Flannel<br>
Fabedge 不同与 Calico，Flannel 等标准 Kubernetes 网络插件。这些插件主要应用在数据中心，解决 kubernetes 集群内部网络问题，而 Fabedge 解决的是边缘计算场景下，使用 Kubeedge 将边缘节点接入云端 Kubernetes 集群后，不同边缘节点上 POD 之间， 边缘节点 POD 和云端 POD 之间如何通讯的问题。目前 Fabedge 支持无缝集成云端 Calico 插件，以后会扩展到其它插件。<br>
<br>关注“博云”公众号加入FabEdge微信交流群
                                                                <div class="aw-upload-img-list">
                                                                                                                                </div>
                                
                                                                <ul class="aw-upload-file-list">
                                                                                                                                            </ul>
                                                              
</div>
            