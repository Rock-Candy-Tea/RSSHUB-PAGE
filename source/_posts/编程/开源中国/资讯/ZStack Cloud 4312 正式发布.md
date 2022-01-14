
---
title: 'ZStack Cloud 4.3.12 正式发布'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://oscimg.oschina.net/oscnet/up-28370cc795da7185fa6de113a142e556241.png'
author: 开源中国
comments: false
date: Fri, 14 Jan 2022 03:01:00 GMT
thumbnail: 'https://oscimg.oschina.net/oscnet/up-28370cc795da7185fa6de113a142e556241.png'
---

<div>   
<div class="content">
                                                                                            <p>2022年1月7日，ZStack Cloud正式发布最新版本——<strong>ZStack Cloud 4.3.12</strong>，涵盖一系列重要功能，以下为您进行详细介绍。</p> 
<p><span style="color:#2980b9"><strong>ZStack Cloud 4.3.12新功能概览</strong></span></p> 
<p>1.许可证新增USB Key授权方式<br> 2.弹性裸金属管理增强：支持本地部署<br> 3.云主机性能增强：支持配置vNUMA以及Emulator绑定<br> 4.新增SharedBlock存储分配策略<br> 5.存储迁移至Ceph主存储支持指定存储池<br> 6.VMware纳管新增支持7.0版本<br> 7.QEMU升级至4.2<br> 8.其它功能和优化</p> 
<p><br> <span style="color:#2980b9"><strong>1.许可证新增USB Key授权方式</strong></span></p> 
<p>从ZStack Cloud 4.3.12开始，许可证新增支持USB Key授权方式（面向付费用户）。用户只需将一个U盾（内含加密保护的授权文件）插到一个管理节点上即可完成授权，安全便捷。</p> 
<p style="margin-left:0.0001pt; margin-right:0px; text-align:center"><img alt height="451" src="https://oscimg.oschina.net/oscnet/up-28370cc795da7185fa6de113a142e556241.png" width="600" referrerpolicy="no-referrer"></p> 
<p style="margin-left:.0001pt; margin-right:0; text-align:center"><span> </span><span style="color:#7f8c8d">USB Key授权</span><span> </span></p> 
<p><span style="color:#2980b9"><strong>2.弹性裸金属管理增强：支持本地部署</strong></span></p> 
<p>在之前版本中，弹性裸金属实例仅支持云盘部署，ZStack Cloud 4.3.12新增支持本地部署。用户不仅可将系统镜像直接部署至弹性裸金属实例的本地磁盘，充分利用本地磁盘的稳定性和高性能优势，也可将已部署系统的实例直接纳管，无需中断业务重装系统，有效保障业务连续性。</p> 
<p style="text-align:center"><img alt height="397" src="https://oscimg.oschina.net/oscnet/up-714d342e1702dd54bb5d139817c3dc2b0be.png" width="600" referrerpolicy="no-referrer"><br> <span style="color:#7f8c8d">本地部署</span></p> 
<p><span style="color:#2980b9"><strong>3.云主机性能增强：支持配置vNUMA以及Emulator绑定</strong></span></p> 
<p><span><span><span><span>ZStack Cloud 4.3.12提供以下策略配置，实现云主机性能增强。</span></span></span></span></p> 
<p><span style="color:#2980b9">1)    支持配置vNUMA</span></p> 
<p><span><span><span><span>云主机支持配置vNUMA，通过CPU绑定方式为云主机透传关联的物理机NUMA节点 (pNUMA Node) ，实现云主机CPU优先访问所在vNUMA节点的本地内存，从而增强云主机性能。</span></span></span></span></p> 
<p><span><span><span><span>配置vNUMA时，云平台提供三种CPU绑定方式：按NUMA结构手动绑定、智能绑定、输入绑定。用户可根据实际场景需求灵活选择。</span></span></span></span></p> 
<p><span><span><span><span>配置vNUMA完成后，用户可直观查看云主机vNUMA拓扑及其关联的物理机pNUMA节点拓扑。</span></span></span></span></p> 
<p style="text-align:center"><img alt height="581" src="https://oscimg.oschina.net/oscnet/up-209cf08df6918a38cf0028c73967dba0704.png" width="800" referrerpolicy="no-referrer"></p> 
<p style="margin-left:0.0001pt; margin-right:0px; text-align:center"><span style="color:#7f8c8d">云主机配置vNUMA</span></p> 
<p style="text-align:center"><img alt height="505" src="https://oscimg.oschina.net/oscnet/up-6d6a5e84c31739a95c4e903d2722a5e723e.png" width="800" referrerpolicy="no-referrer"></p> 
<p style="text-align:center"><span style="color:#7f8c8d">云主机vNUMA拓扑</span></p> 
<p style="text-align:center"><img alt height="536" src="https://oscimg.oschina.net/oscnet/up-ce5f0c3eeb7034332f821089c18d0dbd951.png" width="800" referrerpolicy="no-referrer"></p> 
<p style="text-align:center"><span> </span><span style="color:#7f8c8d">物理机pNUMA拓扑</span></p> 
<p style="margin-left:.0001pt; margin-right:0"><span style="color:#2980b9"><strong><strong>2)<strong> </strong>支持配置</strong></strong><strong><strong>Emulator绑定</strong></strong></span></p> 
<p style="margin-left:.0001pt; margin-right:0"><span><span><span><span>云主机支持配置</span></span><span><span>Emulator</span></span><span><span>绑定，通过</span></span><span><span>将云主机</span></span><span><span>相关线程（</span></span><span><span>除vCPU和IO线程</span></span><span><span>以外的</span></span><span><span>其他线程</span></span><span><span>）</span></span><span><span>与物理机CPU进行绑定</span></span><span><span>，实现云主机相关线程独占特定物理</span></span><span><span>CPU</span></span><span><span>运行，从而增强云主机性能。</span></span></span></span></p> 
<p style="text-align:center"><img alt height="451" src="https://oscimg.oschina.net/oscnet/up-c437c1b63fdeb2b7f4fb98aca99b5df7640.png" width="800" referrerpolicy="no-referrer"></p> 
<p style="margin-left:.0001pt; margin-right:0; text-align:center"><span> </span><span style="color:#7f8c8d">云主机配置Emulator绑定</span><span> </span></p> 
<p><span style="color:#2980b9"><strong>4.新增SharedBlock存储分配策略</strong></span></p> 
<p>ZStack Cloud 4.3.12针对SharedBlock主存储多LUN场景提供存储分配策略优化。在全局设置中，新增 “SharedBlock存储分配策略”，用于设置云盘和快照在SharedBlock主存储 LUN上的落盘策略。策略主要包括三种：根据系统分配、创建在容量剩余最多的LUN中、创建在 LV（快照+云盘）数量最少的LUN中。<br> 该全局设置同时支持细粒度至单个SharedBlock主存储。</p> 
<p style="text-align:center"><img alt height="274" src="https://oscimg.oschina.net/oscnet/up-ccd24d083f8337e3034d042697f61ee2a60.png" width="800" referrerpolicy="no-referrer"></p> 
<p style="margin-left:.0001pt; margin-right:0; text-align:center"><span style="color:#7f8c8d">SharedBlock存储分配策略</span></p> 
<p><span style="color:#2980b9"><strong>5.存储迁移至Ceph主存储支持指定存储池</strong></span></p> 
<p>从ZStack Cloud 4.3.12开始，对云主机/云盘执行存储迁移操作时，若目标主存储为Ceph主存储，支持指定目标存储池（根云盘存储池、数据云盘存储池），满足用户对存储池的灵活分配需求。</p> 
<p style="text-align:center"><img alt height="417" src="https://oscimg.oschina.net/oscnet/up-675d714c6afc21e12bf270a926be5140108.png" width="500" referrerpolicy="no-referrer"></p> 
<p style="margin-left:.0001pt; margin-right:0; text-align:center"><span style="color:#7f8c8d">云主机存储迁移</span></p> 
<p style="margin-left:0.0001pt; margin-right:0px; text-align:center"><span style="color:#7f8c8d"><img alt height="247" src="https://oscimg.oschina.net/oscnet/up-67695553fed2eeda227d5755ed85454d5e4.png" width="500" referrerpolicy="no-referrer"></span></p> 
<p style="margin-left:0.0001pt; margin-right:0px; text-align:center"><span style="color:#7f8c8d">云盘存储迁移</span></p> 
<p><span style="color:#2980b9"><strong>6.VMware纳管新增支持7.0版本</strong></span></p> 
<p>在之前版本中，ZStack Cloud已支持纳管VMware vCenter 5.0、5.1、5.5、6.0、6.5、6.7，从ZStack Cloud 4.3.12开始，VMware纳管新增支持7.0版本。</p> 
<p><br> <span style="color:#2980b9"><strong>7.QEMU升级至4.2</strong></span></p> 
<p>从ZStack Cloud 4.3.12开始，QEMU版本默认从2.12自动升级至4.2。</p> 
<p>若使用4.3.12（及后续版本）ISO全新部署云平台，将默认安装QEMU 4.2版本，若升级至4.3.12（及后续版本）环境，将默认继续沿用QEMU 2.12版本。</p> 
<p>云平台要求同一集群内所有物理机必须使用相同的QEMU版本，因此，若升级至4.3.12（及后续版本）环境，将不支持在已有集群内使用4.3.12（及后续版本）ISO安装物理机进行扩容。如需扩容，请使用新集群。</p> 
<p><br> <span style="color:#2980b9"><strong>8.其它功能和优化</strong></span></p> 
<ul> 
 <li>使用已开启Virtio的Windows镜像（ISO格式）创建云主机时，支持自动加载Virtio驱动。</li> 
 <li>创建云主机检测到计算资源不足的提示优化。</li> 
 <li>云主机控制台交互优化。</li> 
 <li>创建二层网络支持自动展示备选网卡名供用户选择。</li> 
 <li>创建VPC网络支持按需指定DNS。</li> 
 <li>企业管理增强：部门运营管理员角色权限优化、项目详情页新增“关联资源”展示页。</li> 
 <li>持续数据保护（CDP）增强：CDP任务支持查看实时进度。</li> 
 <li>全局设置新增 “云主机时间同步”。</li> 
 <li>新增3条默认事件报警条目：“负载均衡实例未连接”、“ 载均衡实例已连接”、“路由器的启用状态变为已暂停”。</li> 
 <li>新增3条自定义资源报警条目“检查到不健康的后端服务器”、“Ceph存储池可用容量百分比”、“Ceph存储池已用容量百分比”。</li> 
 <li>审计详情页支持对API 请求UUID一键复制。</li> 
</ul>
                                        </div>
                                      
</div>
            