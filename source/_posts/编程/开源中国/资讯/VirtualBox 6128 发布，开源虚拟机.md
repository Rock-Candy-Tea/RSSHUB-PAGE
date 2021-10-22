
---
title: 'VirtualBox 6.1.28 发布，开源虚拟机'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=2209'
author: 开源中国
comments: false
date: Fri, 22 Oct 2021 07:10:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=2209'
---

<div>   
<div class="content">
                                                                    
                                                        <p>VirtualBox 6.1.28 现已发布。VirtualBox 是一款功能强大的 x86 虚拟机软件，它不仅具有丰富的特色，而且性能也很优异。</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">该版本是一个维护版本，修复和/或添加了以下项目：</p> 
<ul> 
 <li>VMM：修复了在某些条件下 booting nested-guests 访问 debug registers 时的 guru meditation</li> 
 <li>UI：基于触摸板滚动的错误修复</li> 
 <li>VMSVGA：修复了从保存状态恢复后第一次调整大小时的 VM 黑屏问题（错误<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.virtualbox.org%2Fticket%2F20067" target="_blank">#20067</a>）</li> 
 <li>VMSVGA：修复了 Linux Mint 上的显示损坏（错误<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.virtualbox.org%2Fticket%2F20513" target="_blank">#20513</a>）</li> 
 <li>Storage：修复了在某些情况下使用 VHD 图像时可能出现的写入错误（错误<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.virtualbox.org%2Fticket%2F20512" target="_blank">#20512</a>）</li> 
 <li>Network：virtio-net 设备支持中的多项更新</li> 
 <li>Network：现在 virtio-net 可以正确处理在保存的 VM state 下断开 cable 的问题。</li> 
 <li>Network：对网络范围的更多管理控制，请参阅用户手册</li> 
 <li>NAT：修复了不拒绝具有绝对路径名的 TFTP 请求（错误<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.virtualbox.org%2Fticket%2F20589" target="_blank">#20589</a>）</li> 
 <li>Audio：修复了 PC 休眠后 VM 会话中止的问题（错误<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.virtualbox.org%2Fticket%2F20516" target="_blank">#20516</a>）</li> 
 <li>Audio：修复了在现代 Linux 客户机上设置 HDA 模拟的线路输入音量</li> 
 <li>Audio：修复了在拍摄快照时恢复播放 AC'97 emulation 的问题</li> 
 <li>API：添加了对 Python 3.9 的绑定支持（错误<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.virtualbox.org%2Fticket%2F20252" target="_blank">#20252</a>）</li> 
 <li>API：修复了在运行时更改设置时罕见的 VM 挂起</li> 
 <li>Linux host：改进了内核模块安装检测，可防止不必要的模块重建</li> 
 <li>Windows host：在 Windows 8 及更高版本上加速大页面分配</li> 
 <li>Windows host：修复了 VM 关闭后 VBoxHeadless 进程仍然存在的问题（错误<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.virtualbox.org%2Fticket%2F20574" target="_blank">#20574</a>）</li> 
 <li>Host Services：Shared Clipboard：当 clipboard sharing 被禁用时，防止 guest clipboard 重置（错误<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.virtualbox.org%2Fticket%2F20487" target="_blank">＃20487</a>）</li> 
 <li>Host Services：Shared Clipboard over VRDP：修复了当 guest service 重新连接到主机时继续工作的问题（错误<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.virtualbox.org%2Fticket%2F20366" target="_blank">＃20366</a>）</li> 
 <li>Host Services：Shared Clipboard over VRDP：修复了当 guest 没有剪贴板数据要报告时防止远程 RDP 客户端挂起的问题</li> 
 <li>Linux Host 和 Guest：引入了对内核 5.14 和 5.15 的初始支持</li> 
 <li>Linux Host 和 Guest：引入了对 RHEL 8.5 内核的初始支持</li> 
 <li>Windows Guest：引入了 Windows 11 Guest 支持，包括无人值守安装</li> 
</ul> 
<p>更新说明：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.virtualbox.org%2Fwiki%2FChangelog" target="_blank">https://www.virtualbox.org/wiki/Changelog</a></p>
                                        </div>
                                      
</div>
            