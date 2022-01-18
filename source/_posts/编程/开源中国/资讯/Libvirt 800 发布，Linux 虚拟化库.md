
---
title: 'Libvirt 8.0.0 发布，Linux 虚拟化库'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=6566'
author: 开源中国
comments: false
date: Tue, 18 Jan 2022 07:01:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=6566'
---

<div>   
<div class="content">
                                                                                            <div> 
 <div> 
  <p><span style="color:#333333">Libvirt 库是一种实现 Linux 虚拟化功能的 Linux API，它支持各种虚拟机监控程序，包括 Xen 和 KVM，以及 QEMU 和用于其他操作系统的一些虚拟产品。</span></p> 
  <p><span style="color:#333333">目前 </span>Libvirt 8.0.0 发布了，带来大量更新项：</p> 
  <h3><strong>安全</strong></h3> 
  <ul> 
   <li>libxl：修复潜在的死锁和崩溃  (CVE-2021-4147)</li> 
  </ul> 
  <p>恶意访客可能会不断地重新启动自身，导致主机上的 libvirtd 死锁或崩溃，从而制造拒绝服务攻击（DOS）的条件。</p> 
  <h3><strong>删除功能</strong></h3> 
  <ul> 
   <li>qemu：为严格模式的 numatune 明确禁止实时更改节点集</li> 
  </ul> 
  <p>对于 <numatune/> 的严格模式，不能保证内存完全移动到新的节点集（例如 QEMU 可能已经锁定了内存），从而违反了严格模式的条件。如果需要在 NUMA 节点之间实时迁移 QEMU 内存，建议改用限制模式。</p> 
  <h3><strong>新特性</strong></h3> 
  <ul> 
   <li>qemu：磁盘复制操作的同步写入模式</li> 
  </ul> 
  <p><span style="color:#2e3033"><code>blockdev-mirror</code> 块作业支持将虚拟机的写操作同步传播到副本的目的地，确保任务在繁重的 I/O 下收敛。</span></p> 
  <ul> 
   <li><span style="color:#2e3033">TCG 域特性</span></li> 
  </ul> 
  <p><span style="color:#000000">Libvirt 现在可以为 TCG 域设置翻译块（translation block ）缓存大小 (tb-size)。</span></p> 
  <ul> 
   <li><span style="color:#000000">qemu：添加用于在域中注入启动密钥的新 API </span></li> 
  </ul> 
  <p>添加了新的 API <code>virDomainSetLaunchSecurityState()</code> 和 virsh 命令 <code>domsetlaunchsecstate</code> ，以支持在域的内存中注入启动密钥。</p> 
  <h3><strong>改进</strong></h3> 
  <ul> 
   <li>libxl：实现 <code>virDomainGetMessages</code> API</li> 
   <li>qemu：在外部快照和块复制后，保留 qcow2 子集群的分配状态</li> 
  </ul> 
  <p>除此之外，Libvirt 8.0.0 还包含一些 Bug 修复，详细内容可在<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Flibvirt.org%2Fnews.html" target="_blank">更新公告</a>中阅览。</p> 
 </div> 
</div>
                                        </div>
                                      
</div>
            