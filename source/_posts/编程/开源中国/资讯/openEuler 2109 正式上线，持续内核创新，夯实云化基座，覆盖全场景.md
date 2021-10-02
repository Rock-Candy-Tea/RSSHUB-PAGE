
---
title: 'openEuler 21.09 正式上线，持续内核创新，夯实云化基座，覆盖全场景'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://oscimg.oschina.net/oscnet/up-fc23e55c2f1ec8c987e52347202c6f2e832.png'
author: 开源中国
comments: false
date: Sat, 02 Oct 2021 07:54:00 GMT
thumbnail: 'https://oscimg.oschina.net/oscnet/up-fc23e55c2f1ec8c987e52347202c6f2e832.png'
---

<div>   
<div class="content">
                                                                    
                                                        <p><img alt src="https://oscimg.oschina.net/oscnet/up-fc23e55c2f1ec8c987e52347202c6f2e832.png" referrerpolicy="no-referrer"></p> 
<p style="color:#000000; margin-left:0; margin-right:0; text-align:justify"><span>2021 年 9 月 30 日，全新 openEuler 21.09 创新版如期而至。</span></p> 
<p style="color:#000000; margin-left:0; margin-right:0; text-align:justify"><span>openEuler 21.09 是欧拉正式升级面向数字基础设施的开源操作系统后的第一个社区创新版本。</span><span>伴随社区的快速发展，面向场景化的 SIG 不断组建，openEuler 的应用边界从最初的服务器场景，逐步拓展到云计算、边缘计算、嵌入式等更多场景。</span></p> 
<p style="color:#000000; margin-left:0; margin-right:0; text-align:justify"><span>openEuler 21.09 推出面向新型介质的文件系统 EulerFS，持续内核创新，新增容器操作系统 KubeOS和安全容器等大颗粒特性，夯实云化基座；同时发布了 openEuler 21.09 Edge 和 openEuler 21.09 Embedded 版本，探索全场景能力。</span></p> 
<blockquote> 
 <p style="margin-left:0px; margin-right:0px"><strong>感谢</strong></p> 
 <p style="margin-left:0; margin-right:0"><span style="color:#000000"><strong><em>由衷对来自社区的 869 名参与 openEuler 21.09 版本贡献的开发者表示感谢。</em></strong></span></p> 
 <p style="margin-left:0; margin-right:0"><span style="color:#000000"><strong><em>同样感谢积极参与该版本贡献的华为、联通数科、中国电信、青云科技、麒麟软件、统信软件、中科院软件所、上海交通大学等公司、研究机构和高校。</em></strong></span></p> 
</blockquote> 
<h2 style="margin-left:0px; margin-right:0px; text-align:justify"><span><span>openEuler 21.09 创新版正式推出</span></span></h2> 
<p><span><span style="color:#000000">openEuler 21.09 作为第一个覆盖全场景的社区创新版正式推出。</span></span></p> 
<p><img alt src="https://oscimg.oschina.net/oscnet/up-de2994362902a1605caaf7695f29422590c.png" referrerpolicy="no-referrer"></p> 
<p>openEuler 21.09 系统架构和新特性如下：</p> 
<p style="color:#000000; margin-left:0; margin-right:0; text-align:justify"><img alt src="https://oscimg.oschina.net/oscnet/up-718e3398db2b15bd7155557e7f22d93e9f7.png" referrerpolicy="no-referrer"></p> 
<h3><span><span>引领内核创新</span></span></h3> 
<p><span>openEuler 21.09 对云原生调度的相关功能进行了增强。对于云场景在线和离线业务</span><span>混合部署场景，创新 CPU 调度算法和 OOM 内存回收算法，保障在线业务对 CPU 的实时抢占及抖动抑制，支撑在线业务安全可靠运行。</span></p> 
<p style="color:#000000; margin-left:0; margin-right:0; text-align:justify">在文件系统方面，openEuler 21.09 新增 EulerFS 文件系统。EulerFS 是华为开发并贡献到社区的全新文件系统，针对 SCM 新型介质，采用了软更新和双视图技术，减少文件系统元数据同步时延，相比 EXT4 文件系统，性能倍级提升。</p> 
<p style="color:#000000; margin-left:0; margin-right:0; text-align:justify">在内存管理方面，内存分级扩展 etMem 新增用户态 swap 功能。实现策略配置淘汰的冷内存交换到用户态存储，性能优于内核态 swap 且业务无感知。</p> 
<h3 style="margin-left:0px; margin-right:0px; text-align:justify"><span>夯实云化基座</span></h3> 
<p>K8S 已经成为事实上的云原生基础设施底座，业界主流操作系统厂商均基于 K8S，推出云原生场景专用容器 OS（如 Redhat RCHOS，AWS BottleRocket 等），提供与业务容器一致的管理和运维体验。</p> 
<p style="color:#000000; margin-left:0; margin-right:0; text-align:justify">openEuler 21.09 紧跟业界的最新技术趋势，华为将原创的容器化操作系统 KubeOS 贡献到社区，具备运行内存消耗<150M，重启时间<15 秒的优势。</p> 
<p style="color:#000000; margin-left:0; margin-right:0; text-align:justify">openEuler 21.09 结合 StratoVirt、iSulad、ShimV2 形成了安全容器方案，为应用提供一个轻量、安全的执行环境，隔离容器和宿主机操作系统间、容器间的安全风险。该方案由华为贡献到社区，较传统 Docker+QEMU 方案，底噪和启动时间优化 40%以上。</p> 
<p style="color:#000000; margin-left:0; margin-right:0; text-align:justify">KubeSphere是在K8S之上构建的以应用为中心的容器平台，由青云科技发起，并欧拉开源社区的 KubeSphere SIG 提供支持和维护。</p> 
<p style="color:#000000; margin-left:0; margin-right:0; text-align:justify">OpenStack 版本更新到 Wallaby。Wallaby 是 2021 年 4 月份发布的最新稳定版本，包含 nova、kolla、cyborg、tacker 等核心项目的重要更新。由联通数科、中国电信、华为共同发起，并由欧拉开源社区 OpenStack SIG 提供支持和维护。</p> 
<p style="color:#000000; margin-left:0; margin-right:0; text-align:justify">Eggo 是基于 K8S 的双平面集群部署工具，提供高效稳定的集群部署能力，支持单集群多架构、在线和离线等多种部署模式。Eggo 结合 GitOps 管理能力、感知集群配置变化，驱动集群 OS 统一高效部署，百节点部署时间从几个小时降为 15 分钟之内。Eggo 由华为主导研发，未来将由 Cloud Native SIG 负责开发维护。</p> 
<h3 style="margin-left:0px; margin-right:0px; text-align:justify"><span><span>探索全场景创新</span></span></h3> 
<p>openEuler 21.09 针对边缘计算场景发布了 openEuler 21.09 Edge。该版本集成了 KubeEdge和边云协同框架，具备边云应用统一管理和发放等基础能力，未来将通过增强智能协同提升 AI 易用性和场景适应性，增强服务协同实现跨边云服务发现和流量转发，增强数据协同提升南向服务能力。</p> 
<p style="color:#000000; margin-left:0; margin-right:0; text-align:justify">openEuler 21.09 针对嵌入式场景发布了超轻量级嵌入式版本 openEuler 21.09 Embedded。该版本镜像小于 5M，启动时间小于 5 秒，提供轻量化、安全和轻量容器等基础能力，支持 ARM32、ARM64 芯片架构，未来将协同欧拉开源社区生态伙伴、用户、开发者，逐步扩展支持 PowerPC、RISC-V 等芯片架构，增加确定性时延、工业中间件、仿真系统等能力，打造嵌入式领域操作系统解决方案。</p> 
<p style="color:#000000; margin-left:0; margin-right:0; text-align:justify">openEuler 21.09 Edge和openEuler 21.09 Embedded是欧拉开源操作系统场景的探索和拓展，提供预览性质的技术创新体验，社区将持续丰富边缘计算和嵌入式场景的能力。</p> 
<h3 style="margin-left:0px; margin-right:0px; text-align:justify"><span><span>中间件&桌面环境</span></span></h3> 
<p>OpenResty 目前已经移植到 openEuler 21.09 版本中。OpenResty 是一个基于 Nginx 与 Lua 的高性能 Web 平台。用于方便地搭建能够处理超高并发、扩展性极高的动态 Web 应用、Web 服务和动态网关。感谢来自 Apache APISIX 社区的罗泽轩、温铭在本次 OpenResty 迁移工作中的贡献，让 OpenResty 可以在欧拉开源操作系统上平稳高效的运行。</p> 
<p style="color:#000000; margin-left:0; margin-right:0; text-align:justify">UKUI 是由麒麟团队开发的基于 Linux 发行版的轻量级桌面环境，在 openEuler 21.09 中，UKUI 新增中文输入法和多媒体支持。</p> 
<p style="color:#000000; margin-left:0; margin-right:0; text-align:justify">统信桌面环境简称 DDE，是一款安全、稳定且易用的 Linux 桌面环境，由统信软件开发。在 openEuler 21.09 中， DDE 新增支持画板、音乐和影院应用。</p> 
<hr> 
<p style="color:#000000; margin-left:0; margin-right:0; text-align:justify">汇聚操作系统的创新力量，闪耀数字时代的星辰大海。再次感谢参与 openEuler 21.09 版本贡献的 869 名开发者，百家厂商，和来自全球的几十万用户，对欧拉开源社区的贡献和信任。欧拉开源社区的每一步成长离不开大家的努力，在未来社区将持续在服务器、云计算、边缘计算和嵌入式场景推动创新和发展。</p> 
<p style="color:#000000; margin-left:0; margin-right:0; text-align:justify">欢迎下载和体验最新版本，<span style="background-color:#ffffff; color:#000000"><strong style="color:#002fa7"><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Frepo.openeuler.org%2FopenEuler-21.09%2FISO%2F" target="_blank">点击链接即刻下载 openEuler 21.09</a>。</strong></span></p>
                                        </div>
                                      
</div>
            