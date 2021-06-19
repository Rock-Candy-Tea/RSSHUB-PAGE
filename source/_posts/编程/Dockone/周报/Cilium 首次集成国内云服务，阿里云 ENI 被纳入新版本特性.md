
---
title: 'Cilium 首次集成国内云服务，阿里云 ENI 被纳入新版本特性'
categories: 
 - 编程
 - Dockone
 - 周报
headimg: 'https://ucc.alicdn.com/pic/developer-ecology/438994a432db4a289bb98a571eb3c22c.png'
author: Dockone
comments: false
date: 2021-06-19 02:38:30
thumbnail: 'https://ucc.alicdn.com/pic/developer-ecology/438994a432db4a289bb98a571eb3c22c.png'
---

<div>   
<br>作者：清弦<br>
阿里云技术专家，主要负责 ACK 容器网络设计与研发，阿里云开源 CNI 项目 Terway  主要维护者，Cilium Alibaba IPAM 负责人<br>
​<br>
<h1>背景</h1>​<br>
近期 Cilium 社区发布了 Cilium 1.10 正式版本，在这个版本中正式支持阿里云 ENI 模式，阿里云也是国内首家支持 Cilium 的云厂商。<br>
<br><img src="https://ucc.alicdn.com/pic/developer-ecology/438994a432db4a289bb98a571eb3c22c.png" alt="1.png" referrerpolicy="no-referrer"><br>
<br>Cilium 是一个基于 eBPF 的高性能容器网络项目，提供网络、可观测性、安全三方面的解决方案。<br>
<br><img src="https://ucc.alicdn.com/pic/developer-ecology/4d2409a15936482d9afd391341b990b7.png" alt="2.png" referrerpolicy="no-referrer"><br>
<br>Cilium 本身支持 Overlay 网络模式部署在各种云平台或者自建的集群上，但是这种非云原生的网络模式会带来不小的性能损耗。阿里巴巴云原生容器服务团队向 Cilium 社区贡献了阿里云 ENI 模式，使得在阿里云上可以以云原生方式运行 Cilium 。<br>
​<br>
云原生容器服务团队贡献 PR<br>
_<a href="https://github.com/cilium/cilium/pull/15160_" rel="nofollow" target="_blank">https://github.com/cilium/cilium/pull/15160_</a><br>
_<a href="https://github.com/cilium/cilium/pull/15512_" rel="nofollow" target="_blank">https://github.com/cilium/cilium/pull/15512_</a><br>
​<br>
<h1>架构</h1>​<br>
AlibabaCloud Operator 是集群内的网络资源控制器，承担对网络资源（ENI、ENIIP）统一管理、分配工作。<br>
​<br>
<img src="https://ucc.alicdn.com/pic/developer-ecology/007939beeab2499e820a6b418f9010b8.png" alt="3.png" referrerpolicy="no-referrer"><br>
<br>Cilium agent 通过 list-watch 机制、CNI 请求对 Operator 分配的地址资源进行配置、管理。<br>
​<br>
这种架构将所有阿里云 OpenAPI  调用集中到 Operator 中，可以有效的进行 API 请求管理，避免大规模集群下 API 流控问题。<br>
​<br>
<img src="https://ucc.alicdn.com/pic/developer-ecology/ac2b304e821e481f8c6e1831d381181a.png" alt="4.png" referrerpolicy="no-referrer"><br>
<br><h1>基于 Cilium 1.10 + 阿里云 ENI 的高性能云原生网络</h1>​<br>
Cilium 使用了 EBPF 内核技术对传统数据链路进行了优化，绕过了Conntrack 模块，对容器场景下网络性能有了非常大的提高。在阿里云上使用 Cilium 1.10 + 阿里云 ENI 模式有多种按照方式，请阅读 Cilium 社区的安装文档[1]。<br>
​<br>
为了使云上用户享受到更加出色的网络性能，阿里云自研的开源 CNI 插件 Terway [2] 与 Cilium 实现了更好的结合。Terway 支持使用阿里云的弹性网卡来实现的容器网络。使得容器网络和虚拟机网络在同一个网络平面，在不同主机之间容器网络通信时不会有封包等损失，不依赖于分布式路由也能让集群规模不受限于路由条目限制。目前，Terway IPvlan 模式已经深度集成 Cilium 。<br>
<br><h3>使用 Terway IPvlan</h3>使用 Terway 模式非常简单，在阿里云容器服务控制台，创建集群中选择网络插件  Terway ，并勾选 IPvlan 即可启用。<br>
​<br>
<img src="https://ucc.alicdn.com/pic/developer-ecology/0a12cb5f08624fdfb7de11b463a145af.png" alt="5.png" referrerpolicy="no-referrer"><br>
<br><h3><strong>IPvlan + eBPF 性能对比：</strong></h3>​<br>
测试环境：<br>
<ul><li>2 节点 ecs . g5ne . 4xlarge 机型</li><li>对比测试</li></ul><br>
<br>Terway 独占 ENI ( ipvs )<br>
Terway 共享 ENI IPvlan ( ebpf )<br>
Terway 共享 ENI veth ( ipvs )<br>
Flanne l vxlan ( ipvs )<br>
<br><h4><strong>Netperf 性能对比 TCP_CRR</strong></h4>测试场景：使用 netperf 测试 Pod 间通讯<br>
​<br>
<img src="https://ucc.alicdn.com/pic/developer-ecology/150a6a80ca2d44acaac7d8aea105608c.png" alt="6.png" referrerpolicy="no-referrer"><br>
<br>上图数字越大性能越好<br>
​<br>
通过测试，可以看到基于 IPvlan 的 Pod 网络延迟较低，在 TCP_CRR 的测试中性能指标和独占 ENI 模式相当。<br>
​<br>
<h4><strong>wrk + nginx 性能对比</strong></h4>测试场景：采用 wrk 压测 nginx 的 Service 的方式，采用 100 字节的小页面模拟常见的集群中微服务通信。<br>
<br>​<img src="https://ucc.alicdn.com/pic/developer-ecology/26258a3547ac41b68187576c2a84ecd8.png" alt="7.png" referrerpolicy="no-referrer"><br>
<br>上图数字越小性能越好<br>
<br><img src="https://ucc.alicdn.com/pic/developer-ecology/0384bfd01bd14d4eae523b165ace6cf2.png" alt="8.png" referrerpolicy="no-referrer"><br>
<br>上图数字越大性能越好<br>
<br>Terway IPvlan 模式在 wrk- nginx 的短连接测试中相对于传统的 Terway veth 策略路由方式：<br>
<ul><li>ClusterIP 吞吐增加 277% , 延迟降低 50%。</li></ul><br>
<br><h1>总结</h1>​<br>
随着 Kubernetes 已经成为容器调度的事实标准，企业上云的首选。容器网络做为应用的底层基础资源，得到越来越多的关注。<br>
​<br>
在阿里云上我们默认提供高性能的 Terway 网络插件 [3] 帮助用户充分使用云原生的网络资源。Cilium 作为社区新兴的容器网络方案，在可观测性、安全性上有许多出色的特性，本次增加的阿里云ENI模式，可以帮助 Cilium 的用户充分使用阿里云上的网络资源。我们也将继续与社区同行，推动高性能的云原生网络实现规模化落地。<br>
​<br>
安装文档：_<a href="https://docs.cilium.io/en/v1.10/gettingstarted/alibabacloud-eni/#k8s-alibabacloud-eni_" rel="nofollow" target="_blank">https://docs.cilium.io/en/v1.1 ... -eni_</a><br>
<br>Terway:  _<a href="https://www.alibabacloud.com/help/zh/doc-detail/97467.htm_" rel="nofollow" target="_blank">https://www.alibabacloud.com/h ... .htm_</a><br>
Terway 网络插件:_  <a href="https://help.aliyun.com/document_detail/86500.html_" rel="nofollow" target="_blank">https://help.aliyun.com/docume ... html_</a>
                                
                                                              
</div>
            