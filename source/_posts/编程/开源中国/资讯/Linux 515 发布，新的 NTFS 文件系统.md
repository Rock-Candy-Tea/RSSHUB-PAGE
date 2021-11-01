
---
title: 'Linux 5.15 发布，新的 NTFS 文件系统'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=1282'
author: 开源中国
comments: false
date: Mon, 01 Nov 2021 06:54:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=1282'
---

<div>   
<div class="content">
                                                                                            <p>经过 7 个候选版本后，Linux 内核 5.15 现已<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Flore.kernel.org%2Flkml%2FCAHk-%3DwjfbfQobW2jygMvgfJXKmzZNB%3DUTzBrFs2vTEzVpBXA4Q%40mail.gmail.com%2FT%2F%23u" target="_blank">发布</a>，这是 GNU/Linux 发行版的最新 LTS（长期支持）内核。</p> 
<p><strong>主要更新内容</strong></p> 
<ul> 
 <li>新的 NTFS "NTFS3" 文件系统驱动程序，其最初由 Paragon Software 开发</li> 
 <li>KSMBD 被合并为内核 SMB 文件服务器，旨在实现高性能、支持 RDMA 和其他可以在内核空间中更容易实现的领域的高级功能，并且比 Samba 更轻巧 </li> 
 <li>许多新的 RDNA2 PCI ID，可能用于 AMD Radeon RDNA2 显卡更新</li> 
 <li>对 Intel Xe HP 和 DG2/Alchemist 图形硬件的初步支持</li> 
 <li>围绕 Intel Alder Lake 的各种 PCI ID 添加和其他支持工作</li> 
 <li>AMD Zen 3 APU 温度监控终于到位，而且还更具前瞻性，<span style="background-color:#ffffff; color:#121212">Yellow Carp / Rembrandt</span> APU 温度监控也出现在 k10temp 中</li> 
 <li>华硕 ACPI 平台配置文件支持</li> 
 <li>AMD Van Gogh APU音频驱动被合并，Steam Deck是受益于此的硬件之一</li> 
 <li>合并了 Realtek RTL8188EU WiFi 驱动程序以替换之前的 Realtek WiFi 驱动程序</li> 
 <li>PREEMPT_RT 锁定代码被合并为代表 Linux 内核的大量以前未完成的实时补丁</li> 
 <li>亚马逊的 DAMON 被合并为他们一直追求的数据访问监控框架，用于主动内存回收和其他目的</li> 
 <li>新的 "process_mrelease" 系统调用可以更快地释放死亡进程的内存</li> 
 <li>以安全的名义在上下文切换时选择加入 L1 数据缓存刷新，但考虑到性能影响，由系统管理员严格选择加入</li> 
 <li>添加了强化以允许在从内核函数返回之前清除调用者使用的寄存器，建立在 GCC 11+ 编译器端的支持之上</li> 
</ul> 
<p>更多详细内容，请查看<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Flore.kernel.org%2Flkml%2FCAHk-%3DwjfbfQobW2jygMvgfJXKmzZNB%3DUTzBrFs2vTEzVpBXA4Q%40mail.gmail.com%2FT%2F%23u" target="_blank">发布公告</a>。</p>
                                        </div>
                                      
</div>
            