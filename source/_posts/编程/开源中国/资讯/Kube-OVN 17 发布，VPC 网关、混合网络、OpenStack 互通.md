
---
title: 'Kube-OVN 1.7 发布，VPC 网关、混合网络、OpenStack 互通'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=1758'
author: 开源中国
comments: false
date: Thu, 03 Jun 2021 14:39:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=1758'
---

<div>   
<div class="content">
                                                                    
                                                        <p>Kube-OVN 1.7.0  发布，本版本对 VPC 功能进行强化增加了VPC内的网关功能，并对 underlay/overlay 以及多网卡混合部署模式提供了更好的支持，此外还通过 OVN-IC 实现了 OpenStack 和 Kubenretes 网络进行互通的方案</p> 
<p>主要更新：<br> 1. 用户自定 VPC 支持 NAT 网关<br> 2. 支持单个 Pod 内多块 kube-ovn 网卡<br> 3. 集中式网关支持多活模式高可用<br> 4. 支持 overlay/underlay 混合部署模式<br> 5. 支持宿主机单网卡下的 underlay 网络<br> 6. 通过 ovn-ic 联通 Kubernetes 和 Openstack 网络<br> 7. 支持 BGP 对外发布 Service IP<br> 8. 支持使用 internal port 替换 veth pair 提升网络性能</p>
                                        </div>
                                      
</div>
            