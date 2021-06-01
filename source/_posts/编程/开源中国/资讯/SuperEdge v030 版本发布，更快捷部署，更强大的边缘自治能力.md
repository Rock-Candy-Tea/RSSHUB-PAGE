
---
title: 'SuperEdge v0.3.0 版本发布，更快捷部署，更强大的边缘自治能力'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=1959'
author: 开源中国
comments: false
date: Tue, 01 Jun 2021 14:31:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=1959'
---

<div>   
<div class="content">
                                                                    
                                                        <h2>背景</h2> 
<p>SuperEdge 将 Kubernetes 强大的容器管理能力扩展到边缘计算场景中，把云原生能力扩展到边缘侧，不仅很好的实现了云端对边缘端资源和业务的管理和控制，而且提供了边缘增强应用管理能力，支持多区域应用部署、区域自治、灰度发布等一系列能力。SuperEdge 提供的强大的边缘自治和接入能力，显著加速用户业务向边缘计算的转型，打通云原生与边缘计算的边界，云边协同助力工业互联网、物联网、车联网、大数据、人工智能等业务更快更好的落地。</p> 
<h2>新特性及优化</h2> 
<p>本次更新主要聚焦于提升用户使用体验，简化用户安装部署边缘集群和节点的流程，继续增强边缘节点状态感知和自治能力，详情如下：</p> 
<h3>Edgeadm 支持一键安装 K8s 边缘集群和 Join 边缘节点</h3> 
<p>edgeadm 新增支持一键安装 Kubernetes 边缘集群，支持为边缘集群添加任意位置的边缘节点，便于用户快速体验 SuperEdge 的边缘能力。</p> 
<h4>edgeadm 工具提供：</h4> 
<ul> 
 <li> <p>支持一键安装 Kubernetes 边缘集群，参数与 Kubeadm 保持一致</p> </li> 
 <li> <p>支持 Join 任何位置的边缘节点，只需节点可以单向访问 Master</p> </li> 
 <li> <p>支持在线和离线两种安装方式，方便用户根据实际情况灵活选用</p> </li> 
 <li> <p>支持部署高可用集群</p> </li> 
</ul> 
<h4>只需三步就可搭建起一个 K8s 边缘集群：</h4> 
<ul> 
 <li> <p>下载安装包</p> </li> 
</ul> 
<pre><code>arch=amd64 version=v0.3.0 && rm -rf edgeadm-linux-* && wget https://superedge-1253687700.cos.ap-guangzhou.myqcloud.com/$version/$arch/edgeadm-linux-$arch-$version.tgz && tar -xzvf edgeadm-linux-* && cd edgeadm-linux-$arch-$version && ./edgeadm
</code></pre> 
<blockquote> 
 <p>注意修改"arch=amd64"参数，目前支持[amd64, arm64]</p> 
</blockquote> 
<ul> 
 <li> <p>安装边缘 Kubernetes master 节点</p> </li> 
</ul> 
<pre><code>./edgeadm init --kubernetes-version=1.18.2 --image-repository superedge.tencentcloudcr.com/superedge --service-cidr=10.96.0.0/12 --pod-network-cidr=192.168.0.0/16 --install-pkg-path ./kube-linux-*.tar.gz --apiserver-cert-extra-sans=<Master节点外网IP> --apiserver-advertise-address=<Master节点内网IP> --enable-edge=true
</code></pre> 
<ul> 
 <li> <p>Join 边缘节点</p> </li> 
</ul> 
<pre><code>./edgeadm join <Master节点外网IP/Master节点内网IP/域名>:Port --token xxxx --discovery-token-ca-cert-hash sha256:xxxxxxxxxx --install-pkg-path <edgeadm kube-*静态安装包地址> --enable-edge=true
</code></pre> 
<h3>节点智能感知技术</h3> 
<p>在原生 Kubernetes 设计中，所有节点可以从 Apiserver 更新 Endpoints数据，从而避免将流量路由到异常的节点上，以便提高服务 SLA。而在边缘计算的场景下，节点与 ApiServer 经常面临弱网断连的情况，处于断联期间的节点无法获取到更新的 Endpoints 数据，导致服务 SLA 大幅下降现象。</p> 
<p>为了解决这个问题，SuperEdge 实现了节点智能感知技术，该技术基于 SuperEdge 首创的边缘分布式健康探测技术(EdgeHealth)和服务区域自治技术(ServiceGroup)，让处于断联状态的节点也可以感知并剔除异常 Endpoints，让边缘业务更可靠。</p> 
<p>举例，集群中存在 A,B,C 三节点，一个服务 Svc 的后端实例均匀地分布在三个节点上，A 节点与云端断联后，B 节点故障，由于 A 节点上缓存的仍是断联前的 Service 的 Endpoints 列表，因此对于 Service 的访问仍旧会转发到 B 节点上，造成访问的失败；在使用 SuperEdge 的节点智能感知技术后，A 节点可以自行将属于 B 节点上的后端摘除，保证了服务访问的正常。</p> 
<p>面对更为极端的情况，集群中所有节点同云端断联，节点也依然能保证服务后端的可用，极大增强了边缘集群的自治能力。</p> 
<h3>支持 golang 1.16</h3> 
<p>支持 golang 1.16 版本，支持最新 golang 语言特性</p>
                                        </div>
                                      
</div>
            