
---
title: 'openEuler 21.03 发布'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=6984'
author: 开源中国
comments: false
date: Fri, 02 Apr 2021 23:48:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=6984'
---

<div>   
<div class="content">
                                                                    
                                                        <p>2021年3月31日， openEuler 21.03 创新版正式发布。此发行版是 openEuler 的第二个创新版，围绕 openEuler 内核发布众多创新特性，openEuler 21.03 使用的内核是 Linux Kernel 5.10 版本。</p> 
<p>下载地址：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Frepo.openeuler.org%2FopenEuler-21.03%2F" target="_blank">https://repo.openeuler.org/openEuler-21.03/</a></p> 
<p>据介绍，openEuler 21.03 主要更新内容是内核创新，其中包括内存分层扩展和内核热升级；增加桌面环境 DDE 和 Xfce；增强云原生能力。</p> 
<p>以下内容摘录自<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fmp.weixin.qq.com%2Fs%2F38QabJmiKqNnBZtmw4uKjg" target="_blank">发布公告</a>。</p> 
<h1>内核创新</h1> 
<p>openEuler 21.03 在内核上有两大创新：内存分层扩展和内核热升级。</p> 
<p>Linux Kernel 代码量快速增加，漏洞数量的也在不断增加， 目前的内核修热补丁技术只能修复 20%的漏洞，80% 的漏洞仍然需要重启才能完成修复，系统重启会影响业务正常运行，业界需要一种在不重启的情况下实现内核修复和升级的方法。</p> 
<p>openEuler 21.03 的内核热升级可以解决这个问题。在内核升级的过程中，系统对业务进程进行暂停保存操作，来保证数据的一致性，然后通过 kexec 机制快速更换新内核，让业务可以继续运行。</p> 
<p>当前内存制造工艺已经达到瓶颈，Arm 生态发展让每个 CPU 核的成本越来越低。数据库、虚拟机、大数据、人工智能、深度学习场景同时需要算力和内存的支持。内存容量成为了制约业务和算力的问题。</p> 
<p>内存分层扩展通过 DRAM 和低速内存介质，如 SCM、AEP 等形成多级内存，通过内存自动调度让热数据在 DRAM 高速内存区中运行，让冷数据交换到低速内存区，从而增加内存容量，保证核心业务高效平稳运行。该特性适用于内存使用量大，且使用相对不频繁的应用进程上，在这些场景中的效果较好，收益较大。</p> 
<p>除了上述两大创新，openEuler 21.03 通过对 qspinlock、NUMA-Aware qslinlock 等近十种锁进行优化，减少 CPU 共享数据的冲突，提升 CPU 多核的并发度。提高业务效率。</p> 
<h1>向云而生，构筑云化基座</h1> 
<p>在云原生能力上，中国联通将 OpenStack 移植到 openEuler，华为和润和软件将 Kubernetes 打包到 openEuler 的软件仓库。openEuler 21.03 初步实现云化基座。</p> 
<p>在虚拟化能力上，StratoVirt 再次升级。它针对轻量虚拟化场景进行优化，增加弹性内存、大页、系统调用过滤等增强功能，增强 IO 子系统，提升性能和稳定性。</p> 
<p>麒麟软件贡献的 HA 高可用集群方案，可以实现故障秒级切换，为用户提供业务连续性保障、数据持续保护和灾难恢复的高可用环境。</p> 
<h2>新增 DDE 和 Xfce，丰富社区桌面环境生态</h2> 
<p>openEuler 21.03 新增两款桌面环境：DDE 和 Xfce。</p> 
<p>统信桌面环境简称 DDE，是一款安全、稳定且易用的 Linux 桌面环境，采用 Qt 作为前端，Go 为后端，Gala 作为 wm，lightdm 作为 dm 。</p> 
<p>统信软件将 DDE 移植到 openEuler 中，让 openEuler 的开发者也可以享受到安全、稳定、易用的 DDE 桌面环境。</p> 
<p>Xfce 是一个轻量级的 Linux 桌面环境，其特点是快速、轻量、界面美观，在节省系统资源的同时，能够快速加载和执行应用程序。</p> 
<p>北京拓林思在 openEuler 21.03 中把 Xfce 移植到 openEuler。Xfce 所有核心组件升级到 GTK3 和 GDBus。大多数组件还获得了GObject Introspection 的支持。移植到 openEuler 后， Xfce 获得了更完善的用户体验。</p> 
<p>目前 openEuler 共支持三款桌面环境，分别是：UKUI、DDE、Xfce，供开发者进行使用。</p> 
<p>更多内容访问 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fmp.weixin.qq.com%2Fs%2F38QabJmiKqNnBZtmw4uKjg" target="_blank">https://mp.weixin.qq.com/s/38QabJmiKqNnBZtmw4uKjg</a>。</p>
                                        </div>
                                      
</div>
            