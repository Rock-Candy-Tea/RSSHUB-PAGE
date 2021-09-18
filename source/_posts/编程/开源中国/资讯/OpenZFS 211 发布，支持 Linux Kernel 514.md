
---
title: 'OpenZFS 2.1.1 发布，支持 Linux Kernel 5.14'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=9072'
author: 开源中国
comments: false
date: Sat, 18 Sep 2021 07:00:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=9072'
---

<div>   
<div class="content">
                                                                                            <div> 
 <p>OpenZFS 2.1.1 现已发布，该版本大约包含了 90 个 fix。OpenZFS 2.1.1 增加了对 <span style="color:#333333">Linux Kernel</span> 5.14 的正式支持，以及对仍在开发中的 Linux 5.15 的早期兼容。还包括数据完整性修复、各种 ZTS 修复，<span style="color:#121212">持久性</span> L2ARC 修复、各种 FreeBSD 特有的问题、几种不同的优化，以及其他几十个随机修复。</p> 
 <p>主要更新内容如下：</p> 
 <p><strong>支持的平台</strong></p> 
 <ul> 
  <li><strong>Linux：</strong>兼容 3.10 - 5.14 内核</li> 
  <li><strong>FreeBSD：</strong><span style="color:#24292f">兼容从 12.2-RELEASE 开始的版本</span></li> 
 </ul> 
 <h4><span style="color:#24292f"><strong>变化</strong></span></h4> 
 <ul> 
  <li>修复底层磁盘返回错误时的数据完整性问题 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fopenzfs%2Fzfs%2Fissues%2F12391" target="_blank">#12391 </a><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fopenzfs%2Fzfs%2Fpull%2F12443" target="_blank">#12443</a></li> 
  <li>ZTS：等待 zvols 可用 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fopenzfs%2Fzfs%2Fpull%2F12553" target="_blank">#12553</a></li> 
  <li>验证 arc_read() 中的嵌入式 blkptr <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fopenzfs%2Fzfs%2Fpull%2F12535" target="_blank">#12535</a></li> 
  <li>Linux 5.15 兼容：get_acl() <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fopenzfs%2Fzfs%2Fpull%2F12548" target="_blank">#12548</a></li> 
  <li>即使元数据损坏，也允许发送损坏的快照<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fopenzfs%2Fzfs%2Fpull%2F12541" target="_blank">#12541</a></li> 
  <li>arc：删除错误的断言 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fopenzfs%2Fzfs%2Fissues%2F9897" target="_blank">#9897 </a><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fopenzfs%2Fzfs%2Fissues%2F12020" target="_blank">#12020 </a><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fopenzfs%2Fzfs%2Fpull%2F12246" target="_blank">#12246</a></li> 
  <li>具有不同 ashift 的压缩接收可能会导致磁盘上的 PSIZE 不正确<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fopenzfs%2Fzfs%2Fpull%2F12522" target="_blank">#12522 </a><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fopenzfs%2Fzfs%2Fissues%2F8462" target="_blank">#8462</a></li> 
  <li>Linux 5.15 兼容：独立 <linux/stdarg.h> <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fopenzfs%2Fzfs%2Fpull%2F12531" target="_blank">#12531</a></li> 
  <li>Linux 5.15 兼容：<span style="color:#24292f">block device readahead </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fopenzfs%2Fzfs%2Fpull%2F12532" target="_blank">12532</a></li> 
  <li>在 zpool cmd vdev media 脚本中检测 iSCSI <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fopenzfs%2Fzfs%2Fpull%2F12206" target="_blank">#12206</a></li> 
  <li>CI：不要安装 abigail-tools <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fopenzfs%2Fzfs%2Fpull%2F12529" target="_blank">#12529</a></li> 
  <li>通过新的 libabigail 版本更新 ABI 文件<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fopenzfs%2Fzfs%2Fpull%2F12529" target="_blank">#12529</a></li> 
  <li>Libabigail：使 .abi 文件更加一致<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fopenzfs%2Fzfs%2Fpull%2F12529" target="_blank">#12529</a></li> 
  <li>CI：通过 docker 镜像使用新的 libabigail <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fopenzfs%2Fzfs%2Fpull%2F12529" target="_blank">#12529</a></li> 
  <li>检查 libabigail 版本<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fopenzfs%2Fzfs%2Fpull%2F12529" target="_blank">#12529</a></li> 
  <li>ZTS：移除 FreeBSD 上的 flaky zhack 异常 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fopenzfs%2Fzfs%2Fpull%2F12527" target="_blank">#12527</a></li> 
  <li>FreeBSD：如果不是 SA znode，则不要删除 SA xattr <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fopenzfs%2Fzfs%2Fpull%2F12514" target="_blank">#12514</a></li> 
  <li>修复 zstd 的跨端互操作性<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fopenzfs%2Fzfs%2Fissues%2F12008" target="_blank">#12008 </a><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fopenzfs%2Fzfs%2Fpull%2F12022" target="_blank">#12022</a></li> 
  <li>ZTS：等待 zvols 可用 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fopenzfs%2Fzfs%2Fpull%2F12515" target="_blank">#12515</a></li> 
  <li>......</li> 
 </ul> 
 <p>更多详情可查看：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fopenzfs%2Fzfs%2Freleases%2Ftag%2Fzfs-2.1.1" target="_blank">https://github.com/openzfs/zfs/releases/tag/zfs-2.1.1</a></p> 
</div>
                                        </div>
                                      
</div>
            