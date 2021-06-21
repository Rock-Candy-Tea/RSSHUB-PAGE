
---
title: 'SuperEdge v0.4.0 发布，大幅提升使用和运维效率'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=9754'
author: 开源中国
comments: false
date: Mon, 21 Jun 2021 18:34:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=9754'
---

<div>   
<div class="content">
                                                                    
                                                        <p>SuperEdge 提供了一套基于原生 Kubernetes 的边缘容器管理系统，该开源项目是由腾讯云联合英特尔、VMware 威睿、虎牙、寒武纪、美团、首都在线，多家公司共同发布。SuperEdge 把云原生能力扩展到边缘侧，不仅很好的实现了云端对边缘端资源和业务的管理和控制，而且提供了边缘应用管理能力，支持多区域应用部署、区域自治、灰度发布等一系列能力，为应用实现边缘原生化提供了强有力的支持。</p> 
<p>SuperEdge 在2021-06-18发布了 v0.4.0 版本。</p> 
<p>经过社区技术讨论，本次更新主要聚焦于提升从云端批量将边缘节点添加到集群、从云端 ssh 登录到边缘节点进行运维、将 ServiceGroup 多地域应用分能力进一步扩展到支持跨集群多地域场景，详情如下：</p> 
<h3>支持从云端批量将边缘节点添加到集群中</h3> 
<ol> 
 <li> <p>版本引入了一种名为 NodeTask 的 CRD，用户只需提交 NodeTask 资源即可实现批量添加和重装边缘节点的效果，SuperEdge 以一种云原生的使用方式大幅提升添加和重装边缘节点效率；</p> </li> 
 <li> <p>该功能具备内网穿透能力，不要求被添加的节点可以被 master 节点或者外部访问，有针对性地应对边缘场景下 node 节点只能单向连接 master 的情形。</p> </li> 
</ol> 
<h3>支持从云端 ssh 登录到边缘节点进行运维</h3> 
<ol> 
 <li> <p>版本升级了 tunnel 组件，云端的 tunnel-cloud 支持代理 ssh 协议，用户可以直接在云端甚至本地使用 ssh-client 借助 SuperEdge 的 tunnel 登录到指定边缘节点效果；</p> </li> 
 <li> <p>该功能有针对性地应对边缘场景下 node 节点只能单向连接 master，用户不方便从云端直接登录边缘节点运维的情形。</p> </li> 
</ol> 
<h3>将 ServiceGroup 边缘应用分发和管理能力扩展到跨集群多地域</h3> 
<ol> 
 <li> <p>v0.4.0 版本之前，ServiceGroup 的应用分发和管理能力是针对单个集群有效，之后可以支持同时管理多个集群下多个地域的应用；</p> </li> 
 <li> <p>该功能需要配合另一个项目 [<strong>clusternet</strong>] 一起使用。https://github.com/clusternet/clusternet</p> </li> 
</ol> 
<h3>支持以 Addon 方式在原生 K8s 集群中管理边缘应用和边缘节点</h3> 
<ol> 
 <li> <p>v0.4.0版本升级了 edgeadm 工具，用户可以在已有的中心 Kubernetes 集群中 Join 边缘节点，实现在一个集群中即可以管理云端节点和应用又能管理边缘节点和应用。</p> </li> 
</ol> 
<p>更新说明：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fsuperedge%2Fsuperedge%2Freleases%2Ftag%2Fv0.4.0" target="_blank">https://github.com/superedge/superedge/releases/tag/v0.4.0</a></p>
                                        </div>
                                      
</div>
            