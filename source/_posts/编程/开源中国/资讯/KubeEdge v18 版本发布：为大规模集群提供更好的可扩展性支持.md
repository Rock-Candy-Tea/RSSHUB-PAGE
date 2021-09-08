
---
title: 'KubeEdge v1.8 版本发布：为大规模集群提供更好的可扩展性支持'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=7172'
author: 开源中国
comments: false
date: Wed, 08 Sep 2021 17:35:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=7172'
---

<div>   
<div class="content">
                                                                                            <p>北京时间 8 月 31 日，KubeEdge 发布了新的特性版本 v1.8.0，为大规模集群提供更好的可扩展性支持。本次发布的1.8版本新特性包括：CloudCore 对大规模集群的 Active-Active HA 支持、EdgeMesh 架构修改、EdgeMesh 跨局域网通信、提供了Golang 实现的mapper、升级Kubernetes依赖到v1.21.4，并修复了9处问题。</p> 
<h3>新功能</h3> 
<p><strong>1. CloudCore 对大规模集群的 Active-Active HA 支持 [Beta]</strong></p> 
<p>CloudCore 现在支持 Active-Active HA 模式部署，为大规模集群提供更好的可扩展性支持。Cloud-Edge 隧道还可以与多个 CloudCore 实例配合使用。CloudCore 现在可以自动为 Cloud-Edge 隧道添加 iptable 规则。</p> 
<p><strong>2. EdgeMesh 架构修改</strong></p> 
<p>EdgeMesh 现在有两个部分：edgemesh-server 和 edgemesh-agent。edgemesh-server需要一个公网IP地址，当用户使用跨局域网通信时，它可以作为LibP2P模式下的中继服务器或协助agent建立p2p打洞。edgemesh-agent 用于代理用户节点的所有应用流量，充当不同位置 Pod 之间通信的代理。</p> 
<p><strong>3. EdgeMesh 跨局域网通信</strong></p> 
<p>用户可以使用跨局域网通信功能，实现跨局域网边缘到边缘应用通信和跨局域网边缘到云应用通信。</p> 
<p><strong>4. Onvif Mapper</strong></p> 
<p>基于新的设备映射器标准，提供了带有 Golang 实现的 Onvif Mapper。用户现在可以使用 Onvif Mapper 来管理 ONVIF IP 摄像机。</p> 
<p><strong>5. Kubernetes 依赖升级</strong></p> 
<p>将发布的Kubernetes版本升级到v1.21.4，用户现在可以在云端和边缘使用新版本的功能。</p> 
<h3>升级前的重要步骤</h3> 
<p>注意： 在 v1.8 EdgeMesh 已经与 EdgeCore 解耦并移至EdgeMesh repo，如果您使用的是 EdgeMesh，请安装最新版本的 EdgeMesh。</p> 
<h3>其他显着变化</h3> 
<ul> 
 <li> <p>重构边缘站点：导入函数和结构而不是复制代码</p> </li> 
 <li> <p>创建新 cm 后避免更新 cm </p> </li> 
 <li> <p>解决离线安装ke时校验和文件下载问题</p> </li> 
 <li> <p>当容器的 env 从 configmap 或 secret 注入时，cloudcore 支持 configmap 动态更新</p> </li> 
 <li> <p>从 edgecore 中删除 edgemesh </p> </li> 
 <li> <p>keadm：使用 join 命令时支持自定义标签</p> </li> 
 <li> <p>支持 k8s v1.21.X</p> </li> 
 <li> <p>处理 node/*/membership/detail </p> </li> 
 <li> <p>无条件同步响应消息</p> </li> 
 <li> <p>支持默认的 NVIDIA SMI 命令</p> </li> 
</ul> 
<h3>Bug修复</h3> 
<ul> 
 <li> <p>修改隧道端口的值</p> </li> 
 <li> <p>修复 apiserver 的消息</p> </li> 
 <li> <p>修复 TrimLeft 或 TrimRight 的错误使用</p> </li> 
 <li> <p>cloudhub：修复 signEdgeCert nil 指针</p> </li> 
 <li> <p>使用 UpdateDeviceStatusWorkers 作为 updateDeviceStatus 例程</p> </li> 
 <li> <p>解决 metaserver handler.go 的并发映射写入</p> </li> 
 <li> <p>修复 modbus 配置参数空值无效的问题 </p> </li> 
 <li> <p>入场：修复 pod 容忍替换</p> </li> 
 <li> <p>修复指标请求中的目标 kubeletendpoint 端口</p> </li> 
</ul> 
<p><strong>附：KubeEdge社区贡献和技术交流地址</strong></p> 
<p><strong>网站:</strong> https://kubeedge.io</p> 
<p><strong>Github地址</strong>: https://github.com/kubeedge/kubeedge</p> 
<p><strong>Slack地址</strong>: https://kubeedge.slack.com</p> 
<p><strong>邮件列表</strong>: https://groups.google.com/forum/#!forum/kubeedge</p> 
<p><strong>每周社区例会</strong>: https://zoom.us/j/4167237304</p> 
<p><strong>Twitter</strong>: https://twitter.com/KubeEdge</p> 
<p><strong>文档地址</strong>: https://docs.kubeedge.io/en/latest/</p>
                                        </div>
                                      
</div>
            