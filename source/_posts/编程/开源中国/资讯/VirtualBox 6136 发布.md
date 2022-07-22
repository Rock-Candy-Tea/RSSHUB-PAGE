
---
title: 'VirtualBox 6.1.36 发布'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=4'
author: 开源中国
comments: false
date: Fri, 22 Jul 2022 07:31:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=4'
---

<div>   
<div class="content">
                                                                                            <p><span style="background-color:#ffffff; color:#333333">VirtualBox 是一款功能强大的 x86 虚拟机软件，它不仅具有丰富的特色，而且性能也很优异。VirtualBox 6.1.36 是一个维护版本，修复和 / 或增加了以下内容：</span></p> 
<ul> 
 <li>VMM：修复了为单个 vCPU 虚拟机配置 Speculative Store Bypass 时可能发生的 Linux guest 内核崩溃</li> 
 <li>GUI：在虚拟机设置对话框的存储页面中，修复了在 KDE 上破坏鼠标与本机文件选择器交互的错误</li> 
 <li>NAT：防止主机解析器错误地为不受支持的查询返回 NXDOMAIN 时出现问题（bug <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.virtualbox.org%2Fticket%2F20977" target="_blank">#20977</a>）</li> 
 <li>Audio：saved state area 的一般改进</li> 
 <li>Recording：设置处理的各种修复</li> 
 <li>VGA：使用 VBE banking 时屏幕更新的性能改进</li> 
 <li>USB：修复了断开 USB 设备时罕见的崩溃问题</li> 
 <li>ATA：修复了 NT4 guests 需要一分钟才能弹出 CD 的问题</li> 
 <li>vboximg-mount：修复了损坏的写入支持（bug <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.virtualbox.org%2Fticket%2F20896" target="_blank">＃20896</a>）</li> 
 <li>SDK：修复了 Python 绑定错误地尝试将任意字节数据转换为 Python 3 的 unicode 对象，从而导致异常（bug <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.virtualbox.org%2Fticket%2F19740" target="_blank">#19740</a>）</li> 
 <li>API：修复了在 VM 未运行时添加虚拟 USB 大容量存储设备或虚拟 USB DVD 驱动器默认未标记为可热插拔的问题</li> 
 <li>API：对 Python 3.10 的初始支持</li> 
 <li>API：Solaris OS 类型清理</li> 
 <li>Windows host：修复了 6.1.32 中的回归导致使用 Hyper-V 时 guest 挂起（bug <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.virtualbox.org%2Fticket%2F20787" target="_blank">#20787</a>）</li> 
 <li>Windows host：修复了使用 Hyper-V/NEM 模式时保存和恢复 VM 状态的可能问题</li> 
 <li>Linux and Solaris hosts：如果共享文件夹在主机端表示为符号链接，则允许挂载共享文件夹（bug <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.virtualbox.org%2Fticket%2F17491" target="_blank">#17491</a>）</li> 
 <li>Linux Host and Guest drivers：引入了对内核 5.18、5.19 和 RHEL 9.1 的初始支持（bug <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.virtualbox.org%2Fticket%2F20914" target="_blank">#20914</a>、<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.virtualbox.org%2Fticket%2F20941" target="_blank">#20941</a>）</li> 
 <li>Linux Host and Guest drivers：更好地支持使用 clang 编译器构建的内核（bug <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.virtualbox.org%2Fticket%2F20425" target="_blank">#20425</a> 和 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.virtualbox.org%2Fticket%2F20998" target="_blank">#20998</a>）</li> 
 <li>Solaris Guest Additions：安装程序区域的一般改进</li> 
 <li>Solaris Guest Additions：修复了 VMSVGA 图形配置中的 guest screen resize </li> 
 <li>Linux and Solaris Guest Additions：修复了 VBoxVGA 和 VBoxSVGA 图形配置中的多屏幕处理</li> 
 <li>Linux and Solaris Guest Additions：添加了对通过 VBoxManage 设置主屏幕的支持</li> 
 <li>Linux and Solaris Guest Additions：修复了调整 guest screens 大小时 X11 资源泄漏的问题</li> 
 <li>Linux and Solaris Guest Additions：修复了使用 guest control 启动进程时的文件描述符泄漏（bug <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.virtualbox.org%2Fticket%2F20902" target="_blank">#20902</a>）</li> 
 <li>Linux and Solaris Guest Additions：修复了以 root 身份执行进程的 guest control</li> 
 <li>Linux Guest Additions：通过防止内核模块在没有必要的情况下重新构建来改进访客启动时间（bug <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.virtualbox.org%2Fticket%2F20502" target="_blank">#20502</a>）</li> 
 <li>Windows Guest Additions：修复了在极少数情况下在 NT4 guests 中启动时 VBoxTray 崩溃的问题</li> 
</ul> 
<p><span style="background-color:#ffffff; color:#333333">更多详情可查看：</span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.virtualbox.org%2Fwiki%2FChangelog" target="_blank">https://www.virtualbox.org/wiki/Changelog</a></p>
                                        </div>
                                      
</div>
            