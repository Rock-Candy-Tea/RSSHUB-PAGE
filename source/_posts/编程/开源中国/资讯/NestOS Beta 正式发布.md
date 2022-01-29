
---
title: 'NestOS Beta 正式发布'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://static.oschina.net/uploads/space/2022/0129/072415_Qr0L_4252687.png'
author: 开源中国
comments: false
date: Sat, 29 Jan 2022 07:32:00 GMT
thumbnail: 'https://static.oschina.net/uploads/space/2022/0129/072415_Qr0L_4252687.png'
---

<div>   
<div class="content">
                                                                                            <p><span style="background-color:#ffffff; color:#000000">在麒麟软件和欧拉开源社区的共同努力下，</span><span style="background-color:#ffffff; color:#000000">同时支持 x86_64 和 aarch64 架构的 NestOS beta 版本现已正式发布。与此同时，NestOS 官网也已正式上线。</span></p> 
<p style="color:black; margin-left:0px; margin-right:0px"><span style="color:#000000">NestOS 官网：</span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fnestos.org.cn%2F" target="_blank">https://nestos.org.cn/</a></p> 
<p style="color:black; margin-left:0px; margin-right:0px"><span style="background-color:#ffffff; color:#000000">在硬件适配方面，目前 NestOS 在飞腾 FT2000+、S2500 与鲲鹏 Kunpeng920 等设备上完成了适配验证，支持以裸金属与虚拟化方式安装部署。未来我们也会持续扩展支持更多平台，为 NestOS 带来更多的可能性。</span></p> 
<p style="color:black; margin-left:0; margin-right:0; text-align:center"><img align="left" height="287" src="https://static.oschina.net/uploads/space/2022/0129/072415_Qr0L_4252687.png" width="500" referrerpolicy="no-referrer"></p> 
<p> </p> 
<p style="color:black; margin-left:0; margin-right:0; text-align:center"> </p> 
<p style="color:black; margin-left:0; margin-right:0; text-align:center"> </p> 
<p style="color:black; margin-left:0; margin-right:0; text-align:center"> </p> 
<p style="color:black; margin-left:0; margin-right:0; text-align:center"> </p> 
<p style="color:black; margin-left:0; margin-right:0; text-align:center"> </p> 
<p style="color:black; margin-left:0px; margin-right:0px"><em><span style="color:#000000">NestOS beta 版本架构图</span></em></p> 
<p style="color:black; margin-left:0; margin-right:0; text-align:justify">NestOS 搭载了 docker、iSulad、podman、cri-o 等常见容器引擎，提供适配云场景下多种基础运行环境，并针对 Kubernetes 场景进行优化。同时在 IaaS 生态构建方面，开发团队将针对 openStack、oVirt 等平台提供支持；在 PaaS 生态构建方面，还将会提供 OKD(openShift)、Rancher 等平台的相关支持。</p> 
<p style="color:black; margin-left:0; margin-right:0; text-align:justify"><img height="282" src="https://static.oschina.net/uploads/space/2022/0129/072548_zTmp_4252687.png" width="500" referrerpolicy="no-referrer"></p> 
<p><em>NestOS 的 roadmap 规划图</em></p> 
<h4><strong>NestOS技术特性</strong></h4> 
<p style="color:black; margin-left:0; margin-right:0; text-align:justify"><strong>开箱即用的容器平台</strong>：容器技术克服了用户修改系统配置、用户服务对系统组件依赖冲突等导致大规模集群服务运维困难的问题，同时可以快速的安装部署、根据服务负载方便的实时扩展收缩以及节点运维时服务平滑迁移，是云原生时代最重要的基础核心。当前主流通用服务器操作系统需要安装部署后再次进行云场景适配调整，而 NestOS 集成适配了 iSulad、Docker、Podman 、cri-o 等主流容器引擎，做到开箱即用，可为用户提供一种轻量级、定制化的云场景操作系统。</p> 
<p style="color:black; margin-left:0; margin-right:0; text-align:justify"><strong>简单易用的安装配置过程</strong>：NestOS 采用了 Ignition 技术，可以以相同配置方便地完成大批量集群节点安装配置工作。Ignition 是一个与分发无关的配置实用程序，用于系统的安装和配置并初始化 NestOS。Ignition 配置文件中可以包含对网络、存储、文件系统、systemd 单元和用户鉴权及权限管理等配置。安装阶段，NestOS 既支持引导启动安装镜像后手动运行 nestos-installer 命令，加载 Ignition 配置文件，完成 NestOS 本地安装；也可通过 PXE 方式，在启动引导参数中添加远程 Ignition 配置访问地址，实现大批量集群节点网络引导方式安装。</p> 
<p><img height="261" src="https://static.oschina.net/uploads/space/2022/0129/072727_3fv6_4252687.png" width="500" referrerpolicy="no-referrer"></p> 
<p style="color:black; margin-left:0; margin-right:0; text-align:justify"><strong>安全可靠的包管理方式</strong>：NestOS 使用 rpm-ostree 进行软件包管理，rpm-ostree 可以看成是 rpm 和 ostree 的合体。Rpm-ostree 一方面提供了基于 rpm 的软件包安装管理方式，另一方面提供了基于 ostree 的操作系统更新升级。用户每次对系统更新都像是 rpm-ostree 在提交一次“Transaction”，确保更新过程全部成功或全部失败，并允许在更新系统遇到异常后回滚到更新前状态。</p> 
<p style="color:black; margin-left:0; margin-right:0; text-align:justify"><strong>友好可控的自动更新机制</strong>：NestOS 提供自动更新服务，它作为远程更新服务和 rpm-ostree 的客户端，负责检测更新服务器是否存在更新版本，实现节点自动更新与重新引导。该服务支持自动更新代理、用户自定义配置文件和多种更新策略，用户可对是否自动更新、自动更新策略等选项进行配置，也可与上层集群服务相结合，将当前节点服务负载迁移后再行更新，实现集群节点有序升级，保证集群服务不因节点升级而中断。当集群节点需统一进行配置修改或基础环境更新时，可将修改完毕充分验证后的更新版本发布至更新服务器，集群节点将通过自动更新机制完成统一升级。</p> 
<p style="color:black; margin-left:0; margin-right:0; text-align:justify"><strong>紧密配合的双系统分区</strong>：NestOS 采用双系统分区设计，两个分区分别被设置为主动模式和被动模式，并在系统运行期间各司其职。主动分区负责系统运行，被动分区负责系统升级，同时在系统运行期间主动分区被设置成只读状态，确保 NestOS 运行期间的完整性与安全性。当新版本操作系统发布时，一个完整的文件系统将被下载至被动分区，并在系统重启引导时从新版本分区启动，原来的被动分区将切换为主动分区，而之前的主动分区则被切换为被动分区，两个分区扮演的角色将相互对调，等待下一次系统更新。</p> 
<h4 style="color:black; margin-left:0px; margin-right:0px; text-align:justify"><strong>性能对比测试</strong></h4> 
<p style="color:black; margin-left:0; margin-right:0; text-align:justify">使用 NestOS beta 版本横向对比 openEuler21.09、openEuler20.03LTS、Centos8 系统运行 docker,podman,iSulad 容器引擎性能。测试结果如下。x86_64 和 aarch64 虚拟机参数如下:</p> 
<p><img height="235" src="https://static.oschina.net/uploads/space/2022/0129/072812_PeZJ_4252687.png" width="1015" referrerpolicy="no-referrer"></p> 
<p><span style="background-color:#ffffff; color:#000000">软件版本：</span></p> 
<p><img height="317" src="https://static.oschina.net/uploads/space/2022/0129/072828_pZFX_4252687.png" width="1009" referrerpolicy="no-referrer"></p> 
<p style="color:black; margin-left:0; margin-right:0; text-align:justify">Docker（x86_64）测试结果如下：</p> 
<p><img height="438" src="https://static.oschina.net/uploads/space/2022/0129/072906_3ZwG_4252687.png" width="1004" referrerpolicy="no-referrer"></p> 
<p><span style="background-color:#ffffff; color:#000000">Docker（aarch64）测试结果如下：</span></p> 
<p><img height="440" src="https://static.oschina.net/uploads/space/2022/0129/072924_zGPw_4252687.png" width="1002" referrerpolicy="no-referrer"></p> 
<p><span style="background-color:#ffffff; color:#000000">iSulad（x86_64）测试结果如下：</span></p> 
<p><img height="429" src="https://static.oschina.net/uploads/space/2022/0129/072941_tN5x_4252687.png" width="1003" referrerpolicy="no-referrer"></p> 
<p><span style="background-color:#ffffff; color:#000000">iSulad(aarch64)测试结果如下：</span></p> 
<p><img height="432" src="https://static.oschina.net/uploads/space/2022/0129/072959_6Dyq_4252687.png" width="999" referrerpolicy="no-referrer"></p> 
<p><span style="background-color:#ffffff; color:#000000">Podman(x86_64)测试结果如下：</span></p> 
<p><img height="445" src="https://static.oschina.net/uploads/space/2022/0129/073016_d1cU_4252687.png" width="1008" referrerpolicy="no-referrer"></p> 
<p><span style="background-color:#ffffff; color:#000000">Podman(aarch64)测试结果如下：</span></p> 
<p><img height="433" src="https://static.oschina.net/uploads/space/2022/0129/073039_YxcL_4252687.png" width="1002" referrerpolicy="no-referrer"></p> 
<p><span style="background-color:#ffffff; color:#000000">注：欧拉开源社区目前暂不支持podman，Nestos所使用podman将陆续合入欧拉开源社区社区。</span></p> 
<p><span style="background-color:#ffffff; color:#000000">Nestos 使用文档：</span><a href="https://gitee.com/openeuler/NestOS">https://gitee.com/openeuler/NestOS</a></p>
                                        </div>
                                      
</div>
            