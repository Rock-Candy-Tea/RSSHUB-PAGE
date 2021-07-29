
---
title: 'openEuler 20.03 LTS SP2 发布'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=5234'
author: 开源中国
comments: false
date: Wed, 28 Jul 2021 23:34:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=5234'
---

<div>   
<div class="content">
                                                                    
                                                        <p>2021 年 7 月 14 日，openEuler 20.03 LTS SP2 正式发布，该版本合入了欧拉操作系统创新版的众多特性，这些创新特性经过用户验证和功能增强，可以以稳定的运行表现和优异的性能表现运行在生产环境中。</p> 
<p>能够合入这些特性离不开社区众多的开发者，openEuler 20.03 LTS SP2 是社区开发者共建共创的版本，社区开发者贡献的代码也都合入到该版本中。</p> 
<p>来自中国联通、中国电信、华为的开发者将 OpenStack Queen 和  Rocky 版本移植到欧拉操作系统，至此，欧拉操作系统目前支持 OpenStack 的版本如下：Victoria、Queen、Rocky 三个版本。</p> 
<p>openEuler 20.03 LTS SP2 关键特性如下：</p> 
<h4><strong>内存分级扩展 etMem</strong></h4> 
<p>支持多种内存和存储介质统一管理，系统容量平滑扩展。对于内存敏感和内热访问明显的业务，同等性能下内存成本显著降低。</p> 
<ul> 
 <li> <p><strong>冷热页面识别：</strong> 通过内核态的内存页面忙闲统计机制，精确识别进程内存页面访问冷热分布。</p> </li> 
 <li> <p><strong>淘汰策略可配置：</strong> 提供配置接口，可定制内存页面冷热分级策略。</p> </li> 
 <li> <p><strong>平滑扩展：</strong>冷页面自动换出到扩展内存，部署在其上的软件不需要改变和适配编程方式的情况下兼容的运行。</p> </li> 
 <li> <p><strong>多介质扩展支持：</strong> 支持 SCM、XL Flash、NVMe SSD 等多种介质作为扩展内存，根据介质自身访问速度指定内存冷热分层方案，达到扩展内存并减少性能损失的目的。</p> </li> 
</ul> 
<h4><strong>虚拟化功能和可维测能力增强</strong></h4> 
<p>增加热迁移 Pro 能力扩展，提升可维可测能力。</p> 
<ul> 
 <li> <p><strong>热迁移 Pro 特性：</strong> 增强热迁移 multifd 支持 TLS，保障迁移过程数据安全；支持热迁移数据并行压缩，提升迁移性能；增加数据页面访问频率统计，支撑热迁移数据提前预测。</p> </li> 
 <li> <p><strong>性能调试工具(vmtop)：</strong> 可以实时动态查看虚拟机的资源使用情况，包括 CPU 使用率，内存使用率等信息。新增扩展支持 x86_64 架构。</p> </li> 
 <li> <p><strong>IO 悬挂支持：</strong> IO 发生错误时默认自动重试，超时会上报警告。</p> </li> 
 <li> <p><strong>RISC-V 架构支持虚拟化热迁移。</strong></p> </li> 
</ul> 
<h4><strong>轻量虚拟运行时 StratoVirt</strong></h4> 
<p>增加弹性内存、大页功能、系统调用过滤功能，增强 IO 子系统提升性能和稳定性。</p> 
<ul> 
 <li> <p><strong>弹性内存支持：</strong> 根据工作负载的内存需求，实现内存的分配和回收， virtio-balloon 内存回收速度达 3GB/秒。</p> </li> 
 <li> <p><strong>大页支持：</strong> 在轻量级框架下提供大页的支持，可为轻量级虚拟机提供连续的物理内存页面，提高虚拟机内存访问效率。</p> </li> 
 <li> <p><strong>系统调用过滤：</strong> 简化设备模型，增加系统调用过滤支持，最简配置下仅需使用 35 个系统调用，有效减小系统攻击面。</p> </li> 
 <li> <p><strong>IO 子系统增强：</strong> 支持多通道并发 IO 能力，提升性能；支持 IO-QOS 能力，提升虚拟机 IO 流量管理的灵活性和稳定性。</p> </li> 
</ul> 
<h4><strong>机密计算编程框架 secGear</strong></h4> 
<p>secGear 统一机密计算编程框架，提供了易用的开发套件，包括安全区（使用 secGear 编程会将系统区分为安全区域和非安全区域） 生命周期管理、安全开发库、代码辅助生成工具、代码构建与签名工具、安全能力和安全服务组件实现方案。可用于信任环、密态数据库、多方计算、AI 安全保护等多种场景。</p> 
<ul> 
 <li> <p><strong>服务层：</strong> 提供完整的运行在安全侧的安全服务</p> </li> 
 <li> <p><strong>中间件层：</strong> 提供一套协议接口，满足用户基本安全应用</p> </li> 
 <li> <p><strong>基础层：</strong> 提供丰富的 enclave 开发接口或工具，并且在安全侧支持 C POSIX APIs 和标准 OpenSSL 接口，用户基于这些接口可以自由开发安全应用程序</p> </li> 
</ul> 
<h4><strong>OpenStack Queens/Rocky 支持</strong></h4> 
<p>OpenStack Queens/Rocky 是一款可大规模扩展、标准统一的云管理操作系统，更多特性请参考 OpenStack Queens/Rocky 官方发行说明。oepkg提供软件包下载服务。</p> 
<ul> 
 <li> <p><strong>集成 openStack Queens/Rocky 版本：</strong> 使能基础设施即服务(IaaS)解决方案。</p> </li> 
 <li> <p><strong>增强块存储服务能力：</strong> 增加容量扩展、快照和虚拟机镜像克隆等高级功能。</p> </li> 
 <li> <p><strong>增强容器化部署和网络能力：</strong> 与容器能更好的集成。</p> </li> 
 <li> <p><strong>增加扩展服务支持：</strong> 支持控制面板管理、裸机部署、云资源追踪等扩展服务。</p> </li> 
</ul> 
<p>下载地址：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fopeneuler.org%2Fzh%2Fdownload%2F" target="_blank">https://openeuler.org/zh/download/</a> </p>
                                        </div>
                                      
</div>
            