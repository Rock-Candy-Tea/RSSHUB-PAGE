
---
title: 'Kube-OVN 1.7.1 Overlay_Underlay 混合网络'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=6546'
author: 开源中国
comments: false
date: Mon, 19 Jul 2021 12:00:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=6546'
---

<div>   
<div class="content">
                                                                    
                                                        <p>Kube-OVN 是一款运行在 Kubernetes 上的 SDN 网络管理系统，为企业用户提供丰富完善的网络能力。</p> 
<p>Kube-OVN 1.7.1 版本更新内容如下：</p> 
<p><strong>功能更新：</strong></p> 
<ul> 
 <li>Underlay/Vlan 模式重构，支持更丰富和灵活的网络映射配置</li> 
 <li>kubectl ko trace 命令支持 underlay/vlan 模式网络</li> 
 <li>kubectl ko 新增 ovn 集群相关操作 status/kick/backup</li> 
 <li>支持根据主机网卡名指定隧道端口</li> 
</ul> 
<p><strong>性能：</strong></p> 
<ul> 
 <li>使用新版本 ovs，开启 tx offloading </li> 
</ul> 
<p><strong>安全：</strong></p> 
<ul> 
 <li>增加 go build 安全选项</li> 
 <li>修复 CVE-2021-3121</li> 
</ul> 
<p>更多详情可查看：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fkubeovn%2Fkube-ovn%2Freleases%2Ftag%2Fv1.7.1" target="_blank">https://github.com/kubeovn/kube-ovn/releases/tag/v1.7.1</a></p>
                                        </div>
                                      
</div>
            