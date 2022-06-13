
---
title: 'MidnightBSD 2.2.0 发布，FreeBSD 衍生版本'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=3475'
author: 开源中国
comments: false
date: Mon, 13 Jun 2022 07:23:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=3475'
---

<div>   
<div class="content">
                                                                                            <p><span style="color:#333333">MidnightBSD 是从 FreeBSD 派生出的操作系统。该项目的一个关键性目标是创建一份易于使用的桌面环境，并使用图形化的 ports 管理，以及 采用 GNUstep 的系统配置。该操作系统的主体将沿用 BSD 许可证。MidnightBSD 是 FreeBSD 6.1 beta 的分支。</span></p> 
<p>目前，适用于 amd64 和 i386 的 MidnightBSD 2.2 已经发布，此版本的重点是更新基础系统中的第三方软件，和一些较小的增强功能。</p> 
<h4 style="margin-left:0px">错误修复和新功能</h4> 
<ul> 
 <li>为 lzma 使用 md 库 sha256 实现</li> 
 <li>/bin/sh 基于 freebsd 12-stable 源更新</li> 
 <li>root shell 从 csh 更改为 tcsh。</li> 
 <li><span style="color:#444444">从 pfsense 向 dummynet 引入补丁，将最大值增加到 4Gb/s 。</span></li> 
 <li>mport 2.2.0 移除了对 libdispatch / gcd 依赖项的使用，因此可以支持静态构建的 mport。</li> 
 <li>将 desktop-file-utils 命令添加到 plist。</li> 
 <li>将@KLD 添加到 plist 处理程序（允许包定义内核模块）</li> 
 <li>在 ucl pkg 消息上引入类型（允许针对特定事件的包消息）</li> 
 <li>在存根分离上添加空检查（防止卸载包时崩溃）</li> 
 <li>将 chroot 路径添加到 libexec 命令和 mport .list</li> 
 <li><span style="color:#444444">修复了桌面启动问题，并为 GUI 安装创建了初始 .xinitrc 文件。</span></li> 
 <li>Netcat：从 FreeBSD 添加 sctp 支持</li> 
 <li>将 ptsname_r 添加到 libc。</li> 
 <li>来自 FreeBSD 的 Ipfilter 错误修复。</li> 
 <li>在首次启动脚本期间启用 dbus 和 hald</li> 
</ul> 
<p>更多内容可查看更新公告：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.midnightbsd.org%2Fnotes%2F" target="_blank">https://www.midnightbsd.org/notes/</a></p>
                                        </div>
                                      
</div>
            