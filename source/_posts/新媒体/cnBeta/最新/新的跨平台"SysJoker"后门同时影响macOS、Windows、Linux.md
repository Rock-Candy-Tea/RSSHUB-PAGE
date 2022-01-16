
---
title: '新的跨平台"SysJoker"后门同时影响macOS、Windows、Linux'
categories: 
 - 新媒体
 - cnBeta
 - 最新
headimg: 'https://static.cnbetacdn.com/thumb/article/2022/0116/6d7f4f008fdb33b.png'
author: cnBeta
comments: false
date: Sun, 16 Jan 2022 00:17:05 GMT
thumbnail: 'https://static.cnbetacdn.com/thumb/article/2022/0116/6d7f4f008fdb33b.png'
---

<div>   
据报道，新的"SysJoker"后门可以攻击多个操作系统，包括macOS、Windows和Linux。<strong>来自Intezer的研究人员透露，他们发现了SysJoker，这个后门最初被发现是攻击Linux的。不久之后，同一后门的变种被发现，它们可以扩展出对Windows和macOS进行攻击。</strong><br>
 <p><a href="https://static.cnbetacdn.com/article/2022/0116/6d7f4f008fdb33b.png" target="_blank"><img src="https://static.cnbetacdn.com/thumb/article/2022/0116/6d7f4f008fdb33b.png" title alt="Untitled-22.png" referrerpolicy="no-referrer"></a></p><p>这一发现是不寻常的，因为发现可以同时攻击多个平台的恶意代码是很罕见的。通常情况下，恶意软件只为攻击一个平台的特定漏洞而生成，而不是以类似的方式同时为多个平台开发。根据研究人员的技术分析，SysJoker被认为是在2021年下半年的一次攻击中启动的。安全研究员Patrick Wardle对其macOS变种进行了分析。该代码被发现是一个涵盖<a data-link="1" href="https://c.duomai.com/track.php?site_id=242986&euid=&t=https://intel.jd.com/" target="_blank">英特尔</a>和arm64构建的通用二进制文件，这意味着它可以在Apple Silicon以及带有英特尔芯片的旧Mac上运行。该代码有签名，尽管是临时性的签名。</p><p>最初运行时，该软件将自己复制到用户的库中，作为macOS的更新，用于在受感染的系统上持续存在。</p><p>运行后，该恶意软件随后试图下载一个文件，形成一个Google Drice账户，并能够下载和运行一个可执行文件，这取决于来自指定控制服务器的命令。其他命令包括解压缩下载的可执行文件，以及改变解压缩的可执行文件的权限以允许其运行。</p><p>而<a data-link="1" href="https://microsoft.pvxt.net/x9Vg1" target="_blank">Windows</a>下的分析表明，它的操作方式实际上是一样的，即假装是一个更新，联系远程服务器下载一个载荷并接收其他命令，并在目标系统上执行代码。在被研究人员发现后，该后门开始被反病毒引擎标记出来。</p><p>至于它的目的，Intezer还没有看到攻击者发送的第二阶段或命令，这表明它有一个非常具体的目的，因此很可能是来自一个"高级行为者"。人们认为其目的是"间谍活动"，尽管有可能作为后续阶段进行勒索软件攻击。</p><p><strong>如何检测SysJoker</strong></p><p>Intezer公布了一份系统被攻击的指标清单，包括创建哪些文件和允许代码持续存在的LaunchAgent。</p><p>SysJoker创建的文件和目录包括。</p><p>/Library/MacOsServices</p><p>/Library/MacOsServices/updateMacOs</p><p>/Library/SystemNetwork</p><p>/Library/LaunchAgents/com.apple.update.plist</p><p>持久性代码在LibraryLaunchAgents/com.apple.update.plist这个路径下。如果在Mac上发现这些文件，建议关闭所有相关进程并删除这些文件。</p><p>目前还不清楚用户如何成为SysJoker的受害者。</p>   
</div>
            