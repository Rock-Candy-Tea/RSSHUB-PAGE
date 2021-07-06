
---
title: '中国首个 LF Edge 捐赠项目 Baetyl 2.2 正式发布'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=4789'
author: 开源中国
comments: false
date: Tue, 06 Jul 2021 14:36:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=4789'
---

<div>   
<div class="content">
                                                                    
                                                        <p style="text-align:justify"><span style="color:#3d3d3d">Baetyl 作为中国首个加入 LF Edge 基金会的边缘计算项目，自2019年由百度捐赠以来，在开放中立的社区环境中得到不断的支持与发展。如今，在众多活跃的贡献者的努力下，Baetyl 实现了更多具有挑战性的功能，正式升级为 Baetyl v2.2 版本。此次升级的新特性依然本持着云原生的理念，助力 Baetyl 向着构建开放、安全、可扩展、可控制的智能边缘计算平台的方向前进。</span></p> 
<p style="text-align:justify"><span style="color:#3d3d3d">具体来说，相较于之前发布的 Baetyl v2.0 版本，v2.2 版本的升级亮点包括：</span></p> 
<ul> 
 <li> <p><strong>新增了对 EdgeX Foundry 的支持</strong></p> </li> 
 <li> <p><strong>新增了对支持边缘集群环境的所需的 API 定义</strong></p> </li> 
 <li> <p><strong>新增了对 DaemonSet 负载类型应用的支持</strong></p> </li> 
 <li> <p><strong>新增了对已部署应用的远程调试、远程日志查看的 API 定义</strong></p> </li> 
 <li> <p><strong>新增了对 GPU 监控及共享功能的 API 定义</strong></p> </li> 
 <li> <p><strong>提供更多的官方模块</strong></p> </li> 
</ul> 
<p style="text-align:justify"><span style="color:#3d3d3d">以上的功能特性在边缘计算场景下具有较高实用价值的同时，并能满足大量急迫的需求。</span></p> 
<p style="text-align:justify"><span style="color:#1f6ed4"><strong>一、关于对 EdgeX Foundry 的支持</strong></span></p> 
<p style="text-align:justify"><span style="color:#3d3d3d">Baetyl 2.2 版本已完成对开源计算框架 EdgeX Foundry 的兼容，通过 baetyl 的云端管理套件，开发者可以向边缘侧下发完整的 EdgeX 14个服务，下发的 EdgeX 服务将由 Baetyl 提交部署并统一监测信息与云端进行信息同步。</span></p> 
<p style="text-align:justify"><span style="color:#1f6ed4"><strong>二、对边缘集群的支持</strong></span></p> 
<p style="text-align:justify"><span style="color:#3d3d3d">在工业物联网场景中，经常会有大量工控盒子构成一个边缘集群的场景。Baetyl 定义了开放的多集群管理 API，通过实现这些 API，可以把整个集群反映在云端控制台上，开发者可便捷地将应用部署到定义的集群中，更值得一提的是，还可支持开发者指定部署到某些边缘子节点上。</span></p> 
<p style="text-align:justify"><span style="color:#1f6ed4"><strong>三、对 DaemonSet 负载类型应用的支持</strong></span></p> 
<p style="text-align:justify"><span style="color:#3d3d3d">在支持集群的背景下，类似于针对集群中每个节点状态监控的功能就需要一种新的负载方式来支持部署，所以 Baetyl 2.2 也对 DaemonSet 进行了支持，通过这种负载类型，可以将服务再匹配到的每个集群中的节点上启动一个副本，并会随着新节点的增删自动调整。</span></p> 
<p style="text-align:justify"><span style="color:#1f6ed4"><strong>四、关于远程调试、远程日志查看功能</strong></span></p> 
<p style="text-align:justify"><span style="color:#3d3d3d">为方便对边缘设备进行调试或日志查看操作，Baetyl 2.2 版本建立了开放的远程调试 API，能够在未来与多种云端控制系统实现打通。</span></p> 
<p style="text-align:justify"><span style="color:#1f6ed4"><strong>五、关于对 GPU 的支持</strong></span></p> 
<p style="text-align:justify"><span style="color:#3d3d3d">对 GPU 的支持主要包括两方面，一是对 GPU 的使用监控，二是对 GPU 共享的支持。通过 GPU 监控模块，baetyl-core 可以实时获取 GPU 当前显存使用量、温度、能耗等信息。通过 GPU 共享功能，多个应用可以共享使用设备的 GPU 资源。目前已经完成了 GPU 支持接口的定义，仅需在端侧提供一个包含 GPU share 功能的模块即可使用。</span></p> 
<p style="text-align:justify"><span style="color:#1f6ed4"><strong>六、在边缘侧提供了更多的官方系统模块</strong></span></p> 
<p style="text-align:justify"><span style="color:#3d3d3d">baetyl-init：</span><span style="color:#3d3d3d">负责激活边缘节点到云端，初始化并守护 baetyl-core，任务完成后会持续上报并同步 core 状态；</span></p> 
<p><span style="color:#3d3d3d">baetyl-rule：</span><span style="color:#3d3d3d">可以实现 baetyl 框架端侧的消息流转，在 baetyl-broker（端侧消息中心）、函数服务、Iot Hub（云端 mqtt broker）进行消息交换。</span></p> 
<p style="text-align:justify"><span style="color:#3d3d3d">在这些新特性之外，此次升级还提供了很多其他功能细节上的优化和机制上的完善，比如安装过程的优化、系统应用可根据需要选择配置、定义了事务执行接口、任务队列接口等。以上所述新功能会随着6月30日 Baetyl 2.2 的正式发布立即可用，更多信息</span><span style="color:#3d3d3d">访问 GitHub 搜索 Baetyl 进行体验～</span></p>
                                        </div>
                                      
</div>
            