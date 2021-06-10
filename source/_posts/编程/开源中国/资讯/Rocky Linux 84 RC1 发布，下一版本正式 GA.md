
---
title: 'Rocky Linux 8.4 RC1 发布，下一版本正式 GA'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=2884'
author: 开源中国
comments: false
date: Thu, 10 Jun 2021 06:50:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=2884'
---

<div>   
<div class="content">
                                                                    
                                                        <p>Rocky Linux 8.4 RC1 已于上周五<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Frockylinux.org%2Fnews%2Frocky-linux-8-4-rc1-release%2F" target="_blank">发布</a>，开发团队建议不要在生产环境使用 RC 版本，只能将此用于测试，并且表示不支持从 Rocky Linux 8.3 RC1 升级到 Rocky Linux 8.4 RC1，也不支持从 RC 版本升级到稳定版本。</p> 
<p>此外，他们计划解决 Rocky Linux 8.4 RC1 中所有反馈的错误后，直接发布 GA 版本。</p> 
<p>Rocky Linux 8.4 RC1 下载地址：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Frockylinux.org%2Fdownload" target="_blank">https://rockylinux.org/download</a></p> 
<hr> 
<h1>新模块</h1> 
<p>Rocky Linux 8.4 中全新的 module streams 包括以下内容：</p> 
<ul> 
 <li>Python 3.9</li> 
 <li>SWIG 4.0</li> 
 <li>Subversion 1.14</li> 
 <li>Redis 6</li> 
 <li>PostgreSQL 13</li> 
 <li>MariaDB 10.5</li> 
</ul> 
<h1>主要变化</h1> 
<p>Rocky Linux 8.4 的主要变化体现在安全、网络、内核和高可用以及集群等方面。</p> 
<h2>安全</h2> 
<ul> 
 <li>Libreswan 提供的 IPsec VPN 现在支持 IKEv2 的 TCP 封装和安全标签</li> 
 <li>scap-security-guide 已更新到到 0.1.54 ，OpenSCAP 已更新到 1.3.4。这些更新提供了实质性的改进，包括优化内存管理</li> 
 <li>fapolicyd 框架现在提供完整性检查，并且 RPM 插件注册由 YUM 包管理器或 RPM 包管理器更新</li> 
</ul> 
<h2>网络</h2> 
<ul> 
 <li> <p>完全支持 Nmstate（主机的网络 API），这些 nmstate 包提供了一个库和 nmstatectl 命令行，以声明方式管理主机网络设置</p> </li> 
 <li> <p>支持 MPLS（多协议标签交换）</p> </li> 
 <li> <p>iproute2 引入了三个新的流量控制 (tc) 操作：<code>mac_push</code>, <code>push_eth</code>, 和<code>pop_eth</code>，并添加 MPLS 标签</p> </li> 
</ul> 
<h2>内核</h2> 
<ul> 
 <li> <p>主动压缩功能：在发出分配请求之前定期启动内存压缩工作。因此，降低了特定内存分配请求的延迟。</p> </li> 
 <li> <p>提供了用于控制组技术的平板内存控制器。Slab 内存控制器优化了内存的利用率，并且能够将内存记帐从页面级别转移到对象级别。因此，可以观察到总内核内存占用量显著下降，并改善了内存碎片情况。</p> </li> 
 <li> <p>时间命名空间功能：此功能适用于更改 Linux 容器内的日期和时间。现在也可以在检查点恢复后进行容器内时钟的调整。</p> </li> 
 <li> <p>支持第 8、 9 代英特尔酷睿处理器中设置的错误检测和纠正 (EDAC) 内核模块。</p> </li> 
</ul> 
<h2>高可用和集群</h2> 
<ul> 
 <li>维护状态数据的持久性： Pacemaker 资源代理可以异步检测故障并立即将故障注入 Pacemaker，而无需等待下一个监控间隔。持久性资源代理还可以加快具有高状态开销的服务的集群响应时间，因为维护状态数据可以通过不为每个操作单独调用状态来减少集群操作（例如启动、停止和监控）的状态开销。</li> 
</ul> 
<h2>编译器和开发工具</h2> 
<p>以下编译器工具集已更新：</p> 
<ul> 
 <li>GCC Toolset 10</li> 
 <li>LLVM Toolset 11.0.0</li> 
 <li>Rust Toolset 1.49.0</li> 
 <li>Go Toolset 1.15.7</li> 
</ul> 
<p>最后，Rocky Linux 团队提供了 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Frocky-linux%2Frocky-tools%2F" target="_blank">migrate2rocky</a> 工具用于帮助使用者从Rocky Linux 8.3、Centos 8.3 或 8.4、RHEL 8.3 或 8.4 以及 Alma 8.3 或 8.4 迁移到 Rocky Linux 8.4。此工具已经过测试并且可以正常运行，但使用时需自担风险。</p> 
<p><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdocs.rockylinux.org%2Fen%2Frocky%2F8%2Frelease_notes%2Frocky_linux_8-4_release" target="_blank">详情查看 release note</a>。</p>
                                        </div>
                                      
</div>
            