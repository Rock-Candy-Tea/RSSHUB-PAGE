
---
title: 'VirtualBox 6.1.32 发布'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=8238'
author: 开源中国
comments: false
date: Thu, 20 Jan 2022 07:30:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=8238'
---

<div>   
<div class="content">
                                                                                            <p>VirtualBox 是一款功能强大的 x86 虚拟机软件，它不仅具有丰富的特色，而且性能也很优异。VirtualBox 6.1.32 是一个维护版本，修复和/或增加了以下内容：</p> 
<ul> 
 <li>VMM: 改变了使用 Hyper-V 时的 guest RAM 管理，使其与 HVCI 更加兼容 (bug <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.virtualbox.org%2Fticket%2F20627" target="_blank">#20627</a> and <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.virtualbox.org%2Fticket%2F20694" target="_blank">#20694</a>)</li> 
 <li>VMM: 解决了由于 OS/2 中缺少 TLB 刷新，在较新的 AMD CPU 上出现 OS/2 guest 不稳定的情况 (bug <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.virtualbox.org%2Fticket%2F20625" target="_blank">#20625</a>)</li> 
 <li>GUI：修正了在全屏模式下使用迷你工具栏时，在少数情况下的键盘焦点丢失问题</li> 
 <li>音频：修正了在配置 OSS 音频后端时，意外创建空的调试日志文件的问题</li> 
 <li>E1000：修复某些 Linux 内核的链接状态报告</li> 
 <li>无人值守安装（Unattended installation）：修复了 6.1.28 版本中引入的回归问题，该问题会导致 Windows XP 到 10 的分区失败 (bug <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.virtualbox.org%2Fticket%2F20769" target="_blank">#20769</a>)</li> 
 <li>Solaris host：修正安装程序中的回归问题，该问题导致在 Solaris 10 上安装失败。</li> 
 <li>Solaris host：修复了打包方面的问题，使 <a href="https://www.oschina.net/action/GoToLink?url=http%3A%2F%2Fvboxshell.py" target="_blank">vboxshell.py</a> 可以执行。</li> 
 <li>Linux host：修复对某些 USB 设备的访问，该问题导致设备类别没有得到正确处理 (bug <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.virtualbox.org%2Fticket%2F20721" target="_blank">#20721</a>)</li> 
 <li>Guest：如果 guest 处于文本模式，修正了错误的鼠标位置</li> 
 <li>Guest 控制：修正了从 host 到 guest，以及从 guest 到 host 的文件夹复制问题</li> 
 <li>Guest 控制：修复了 UNICODE 的处理问题</li> 
 <li>共享剪贴板：改进了 X11 和 Windows guest 和 host 之间的 HTML 内容交换</li> 
 <li>OS/2 附加功能：修正了共享文件夹中扩展属性的一些问题 (bug <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.virtualbox.org%2Fticket%2F19453" target="_blank">#19453</a>)</li> 
</ul> 
<p>更多详情可查看：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.virtualbox.org%2Fwiki%2FChangelog" target="_blank">https://www.virtualbox.org/wiki/Changelog</a></p>
                                        </div>
                                      
</div>
            