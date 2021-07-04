
---
title: 'OpenZFS 2.1.0 发布，dRAID 兼容，性能更佳'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=7697'
author: 开源中国
comments: false
date: Sat, 03 Jul 2021 23:26:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=7697'
---

<div>   
<div class="content">
                                                                    
                                                        <p>OpenZFS 2.1.0 现已发布，该版本主要更新内容如下：</p> 
<h4>支持的平台</h4> 
<ul> 
 <li><strong>Linux</strong>：兼容 3.10 - 5.13 内核</li> 
 <li><strong>FreeBSD</strong>：兼容从 12.2-RELEASE 开始的版本</li> 
</ul> 
<h4>主要新功能</h4> 
<ul> 
 <li> <p><strong>Distributed Spare RAID</strong><strong> ( <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fopenzfs.github.io%2Fopenzfs-docs%2FBasic%2520Concepts%2FdRAID%2520Howto.html" target="_blank">dRAID</a> )</strong> - 允许使用 RAIDZ 的新分布式变体创建 pools，从而使用集成热备件加快重新同步时间。dRAID 的实施允许在进行 full disk 时，在 "一小部分时间 "内恢复完全冗余。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fopenzfs%2Fzfs%2Fpull%2F10102" target="_blank">#10102</a></p> </li> 
 <li> <p><strong>兼容性属性</strong>- 新的兼容性属性允许管理员可以指定应该在 pool 中启用的功能集。这种精细的控制使创建可移植 pool 和维护 OpenZFS 版本之间和跨平台的 pool 兼容性变得容易。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fopenzfs%2Fzfs%2Fpull%2F11468" target="_blank">#11468 </a><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fopenzfs%2Fzfs%2Fpull%2F11861" target="_blank">#11861</a></p> </li> 
 <li> <p><strong>InfluxDB 支持</strong>- 使用<code>zpool influxdb</code>命令在 InfluxDB 时间序列数据库中收集 pool 的统计信息以进行分析和监控。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fopenzfs%2Fzfs%2Fpull%2F10786" target="_blank">#10786</a></p> </li> 
</ul> 
<h4><code>zpool</code>/<code>zfs</code>命令的更改</h4> 
<ul> 
 <li> <p><strong><code>zpool create -u</code></strong>- 防止文件系统被自动挂载。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fopenzfs%2Fzfs%2Fpull%2F11254" target="_blank">#11254</a></p> </li> 
 <li> <p><strong><code>zpool history -i</code></strong>- pool 历史现在包括每个命令进行性能分析所用的时间。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fopenzfs%2Fzfs%2Fpull%2F11440" target="_blank">#11440</a></p> </li> 
 <li> <p><strong><code>zpool status</code></strong>- 通知用户任何正在使用非最佳块大小的磁盘。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fopenzfs%2Fzfs%2Fpull%2F11088" target="_blank">#11088</a></p> </li> 
 <li> <p><strong><code>zfs send --skip-missing|-s</code></strong>- 发送复制流时跳过丢失的快照。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fopenzfs%2Fzfs%2Fpull%2F11710" target="_blank">#11710</a></p> </li> 
 <li> <p><strong><code>zfs rename -u</code></strong>- 无需重新安装即可重命名文件系统。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fopenzfs%2Fzfs%2Fpull%2F10839" target="_blank">#10839</a></p> </li> 
</ul> 
<h4>Notable Changes</h4> 
<ul> 
 <li> <p>手册页的广泛现代化。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fopenzfs%2Fzfs%2Fpull%2F12125" target="_blank">#12125 </a><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fopenzfs%2Fzfs%2Fpull%2F12129" target="_blank">#12129 </a><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fopenzfs%2Fzfs%2Fpull%2F12149" target="_blank">#12149 </a><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fopenzfs%2Fzfs%2Fpull%2F12169" target="_blank">#12169 </a><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fopenzfs%2Fzfs%2Fpull%2F12212" target="_blank">#12212</a></p> </li> 
 <li> <p>更新<code>vdev_id</code>以支持多路径模式下的 daisy-chained JBOD。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fopenzfs%2Fzfs%2Fpull%2F11526" target="_blank">#11526</a></p> </li> 
 <li> <p>用新的 L2ARC 统计数据更新了<code>arcstat</code>，并添加了<code>-a</code> (all) 和<code>-p</code> (parsable)  命令行选项。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fopenzfs%2Fzfs%2Fpull%2F10743" target="_blank">#10743</a></p> </li> 
 <li> <p>支持内存和 CPU hotplugging。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fopenzfs%2Fzfs%2Fpull%2F11212" target="_blank">#11212</a></p> </li> 
 <li> <p>将<code>acltype=posixacl</code>重命名为<code>acltype=posix</code>，为兼容性添加了别名。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fopenzfs%2Fzfs%2Fpull%2F10918" target="_blank">#10918</a></p> </li> 
 <li> <p>为公共库接口添加了自动 ABI 验证。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fopenzfs%2Fzfs%2Fpull%2F11287" target="_blank">#11287</a></p> </li> 
 <li> <p>在 FreeBSD 上为 fletcher4 添加了 sysctl <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fopenzfs%2Fzfs%2Fpull%2F11270" target="_blank">#11270</a></p> </li> 
</ul> 
<h4>Performance</h4> 
<ul> 
 <li> <p>改进了交互式 I/O 的性能。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fopenzfs%2Fzfs%2Fpull%2F11166" target="_blank">#11166 </a><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fopenzfs%2Fzfs%2Fpull%2F11116" target="_blank">#11116</a></p> </li> 
 <li> <p>针对并行工作负载优化预取。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fopenzfs%2Fzfs%2Fpull%2F11652" target="_blank">#11652</a></p> </li> 
 <li> <p>通过减少对 locks 和 atomics 的争用来提高可扩展性。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fopenzfs%2Fzfs%2Fpull%2F11288" target="_blank">#11288 </a><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fopenzfs%2Fzfs%2Fpull%2F12172" target="_blank">#12172 </a><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fopenzfs%2Fzfs%2Fpull%2F12145" target="_blank">#12145 </a><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fopenzfs%2Fzfs%2Fpull%2F11904" target="_blank">#11904</a></p> </li> 
 <li> <p>减少 pool import time。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fopenzfs%2Fzfs%2Fpull%2F11470" target="_blank">#11470 </a><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fopenzfs%2Fzfs%2Fpull%2F11502" target="_blank">#11502 </a><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fopenzfs%2Fzfs%2Fpull%2F11469" target="_blank">#11469 </a><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fopenzfs%2Fzfs%2Fpull%2F11467" target="_blank">#11467 </a><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fopenzfs%2Fzfs%2Fpull%2F11467" target="_blank">#11467</a></p> </li> 
 <li> <p>减少了 ZIL 块的碎片化。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fopenzfs%2Fzfs%2Fpull%2F11389" target="_blank">#11389</a></p> </li> 
 <li> <p>通过轻量级写入提高<code>zfs receive</code>性能。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fopenzfs%2Fzfs%2Fpull%2F11105" target="_blank">#11105</a></p> </li> 
 <li> <p>改进的内存管理。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fopenzfs%2Fzfs%2Fpull%2F12152" target="_blank">#12152 </a><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fopenzfs%2Fzfs%2Fissues%2F11429" target="_blank">#11429 </a><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fopenzfs%2Fzfs%2Fissues%2F11574" target="_blank">#11574 </a><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fopenzfs%2Fzfs%2Fissues%2F12150" target="_blank">#12150</a></p> </li> 
 <li> <p>改进了模块加载时间。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fopenzfs%2Fzfs%2Fpull%2F11282" target="_blank">#11282</a></p> </li> 
</ul> 
<p>更多详情可查看：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fopenzfs%2Fzfs%2Freleases%2Ftag%2Fzfs-2.1.0" target="_blank">https://github.com/openzfs/zfs/releases/tag/zfs-2.1.0</a></p>
                                        </div>
                                      
</div>
            