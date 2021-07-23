
---
title: 'VirtualBox 6.1.24 发布，开源虚拟机'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=3040'
author: 开源中国
comments: false
date: Fri, 23 Jul 2021 06:18:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=3040'
---

<div>   
<div class="content">
                                                                                            <p>VirtualBox 6.1.24 现已发布。VirtualBox 是一款功能强大的 x86 虚拟机软件，它不仅具有丰富的特色，而且性能也很优异。</p> 
<p>该版本是一个维护版本，修复和/或添加了以下项目：</p> 
<ul> 
 <li>Storage：修复了在设备连接到高于 30 的 VirtIO SCSI 端口时启动虚拟机的问题（bug <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.virtualbox.org%2Fticket%2F20213" target="_blank">#20213</a>）</li> 
 <li>Storage：改进 DVD medium change signaling</li> 
 <li>Serial：修复了在某些情况下 guest 丢失中断的问题（6.0 回归，bug <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.virtualbox.org%2Fticket%2F18668" target="_blank">#18668</a>）</li> 
 <li>Audio：多项修复和增强</li> 
 <li>Network：修复了在断开链接的情况下恢复 VM 后与 virtio-net 的连接问题</li> 
 <li>Network：修复了第一个片段末尾缺少 8 个字节的有效负载的 UDP GSO fragmentation 问题</li> 
 <li>API：修复了最近 Windows Server 版本的 VM 配置</li> 
 <li>Extension Pack：修复了 Linux 上 USB 网络摄像头直通的问题</li> 
 <li>Host and guest driver：修复小内存泄漏（bug <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.virtualbox.org%2Fticket%2F20280" target="_blank">#20280</a>）</li> 
 <li>Linux host and guest：支持内核版本 5.13（bug <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.virtualbox.org%2Fticket%2F20456" target="_blank">#20456</a>）</li> 
 <li>Linux host and guest：引入对 SUSE SLES/SLED 15 SP3 内核的支持（bug <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.virtualbox.org%2Fticket%2F20396" target="_blank">#20396</a>）</li> 
 <li>Linux host：如果系统已经安装了内核模块并且模块版本与当前版本匹配，则安装程序将不会尝试构建内核模块</li> 
 <li>Windows host：修复 DLL 签名验证以更好地处理无效证书</li> 
 <li>Guest Additions：修复了使用共享剪贴板时崩溃的问题（bug <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.virtualbox.org%2Fticket%2F19165" target="_blank">#19165</a>）</li> 
 <li>Linux Guest Additions：引入对 Ubuntu 特定内核的支持（bug <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.virtualbox.org%2Fticket%2F20325" target="_blank">#20325</a>）</li> 
 <li>Solaris guest：增加了默认内存和磁盘大小</li> 
 <li>EFI：支持使用 E1000 网络控制器仿真进行网络引导</li> 
 <li>EFI：稳定性改进（bug <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.virtualbox.org%2Fticket%2F20090" target="_blank">#20090</a>）</li> 
</ul> 
<p>更新说明：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.virtualbox.org%2Fwiki%2FChangelog" target="_blank">https://www.virtualbox.org/wiki/Changelog</a> </p>
                                        </div>
                                      
</div>
            