
---
title: 'NetBSD 9.2 发布'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=5150'
author: 开源中国
comments: false
date: Tue, 25 May 2021 06:58:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=5150'
---

<div>   
<div class="content">
                                                                    
                                                        <p>NetBSD 9.2“Nakatomi Socrates”已发布，这是 NetBSD 9 发布分支的第二次更新。它代表了自 2020 年 10 月 <a href="https://www.oschina.net/news/119413/netbsd-9-1-released">NetBSD 9.1</a> 发布以来，由于安全或稳定性原因而被认为是重要的修正的子集，以及一些从开发分支回传的改进。它与 NetBSD 9.0 完全兼容。</p> 
<p>NetBSD 是一个免费的、安全的及高度可移植的类 UNIX 操作系统，它适合于很多种平台，从 64 位的 AlphaServers 及桌面系统到手持及嵌入式系统。它在设计上非常整洁，并拥有先进的特性，这使得它在业界和学术界都有口皆碑。用户可通过完整的源代码来获得支持。很多应用程序都可容易地从 NetBSD Packages Collection 获得。 </p> 
<p>自 NetBSD 9.1 以来的更改如下：</p> 
<p><strong>Kernel</strong></p> 
<p>netinet：避免信息泄露， <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fcdn.netbsd.org%2Fpub%2FNetBSD%2Fsecurity%2Fadvisories%2FNetBSD-SA2021-001.txt.asc" target="_blank">NetBSD-SA2021-001</a>：IPv4 和 IPv6 中可预测的 ID 泄露</p> 
<ul> 
 <li>netinet：修复了“multicast router 发送带有无效 UDP 校验和的 multicast packet”（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgnats.netbsd.org%2F55779" target="_blank"> PR 55779</a>）</li> 
 <li>xen：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fxenbits.xen.org%2Fxsa%2Fadvisory-362.html" target="_blank">XSA-362 的</a>修复-后端将授权映射错误视为 bug。恶意的 DomU 可能会触发 Dom0 内核崩溃。</li> 
 <li>xen：删除了 xennet(4) 和 xvif(4) 中对 rx-flip 模式的支持，作为 XSA-362 修正的一部分（驱动程序已经默认为更快的 rx-copy 模式）。</li> 
 <li>zfs：各种稳定性修复程序。修复了“在 NFS 提供的 ZFS 上创建目录时出现 panic”的问题。（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgnats.netbsd.org%2F55042" target="_blank"> PR 55042</a>）</li> 
 <li>coda：修复了“coda 客户端打开错误的文件而不是缓存容器”的问题。（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgnats.netbsd.org%2F55775" target="_blank"> PR 55775</a>）</li> 
 <li>hyperv：修复了“无法通过<code>hvn</code>设备进行 ifconfig(8) up/down”的问题。</li> 
 <li>msdosfs：修复了"BOOTSIG0 和 BOOTSIG1 检查阻止安装 Raspberry Pi Pico 的 USB 大容量存储器"（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgnats.netbsd.org%2F55985" target="_blank"> PR 55985</a>）</li> 
 <li>kern：修复了“在 init(8) 之前加载多个大型 firmware 文件时出现 panic”（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgnats.netbsd.org%2F55906" target="_blank"> PR 55906</a>）</li> 
 <li>fdescfs：修复了“fdescfs 创建的节点有错误的主编号”（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgnats.netbsd.org%2F56130" target="_blank"> PR 56130</a>）</li> 
 <li>procfs：更正了<code>environ</code>节点的权限。</li> 
 <li>usb：删除了中止路径中的不正确断言，并修复了<code>DIAGNOSTIC</code>启用后的错误断言失败。</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=http%3A%2F%2Fman.netbsd.org%2FNetBSD-9.2%2Fi386%2Fsysctl.7" target="_blank">sysctl(7)</a>：<code>kern.maxfiles</code>默认值现在与系统内存成正比。避免在 hungry 应用程序（例如多进程 Mozilla Firefox）中耗尽资源。</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=http%3A%2F%2Fman.netbsd.org%2FNetBSD-9.2%2Fi386%2Fcompat_netbsd32.8" target="_blank">compat_netbsd32(8)</a>：对 AArch64 的各种改进： 
  <ul> 
   <li>添加了对 ARMv6 用户空间的支持。现在在 aarch64 服务器上的沙盒中构建 ARMv6 二进制软件包。</li> 
   <li>添加了对 <a href="https://www.oschina.net/action/GoToLink?url=http%3A%2F%2Fman.netbsd.org%2FNetBSD-9.2%2Fi386%2Fptrace.2" target="_blank">ptrace(2)</a> 的支持，修复了 <a href="https://www.oschina.net/action/GoToLink?url=http%3A%2F%2Fman.netbsd.org%2FNetBSD-9.2%2Fi386%2Fclone.2" target="_blank">clone(2)</a>，修复了 core 文件格式。</li> 
   <li>模拟 ARMv7 中不推荐使用的指令。</li> 
  </ul> </li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=http%3A%2F%2Fman.netbsd.org%2FNetBSD-9.2%2Fi386%2Fcompat_linux.8" target="_blank">compat_linux(8)</a>：修复了与使用长于有效的 struct sockaddr_in * 大小的 namelen 的程序的兼容性问题。</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=http%3A%2F%2Fman.netbsd.org%2FNetBSD-9.2%2Fi386%2Fthreadpool.9" target="_blank">threadpool(9)</a>： 修复了“<code>threadpool_job_cancelthrash</code>测试随机失败”的问题（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgnats.netbsd.org%2F55948" target="_blank">PR 55948</a>）</li> 
</ul> 
<p><strong>Programs and services</strong></p> 
<p><a href="https://www.oschina.net/action/GoToLink?url=http%3A%2F%2Fman.netbsd.org%2FNetBSD-9.2%2Fi386%2Fcalendar.1" target="_blank">calendar(1)</a>：将 Judaic 日历更新为 2021 年。</p> 
<ul> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=http%3A%2F%2Fman.netbsd.org%2FNetBSD-9.2%2Fi386%2Fctwm.1" target="_blank">ctwm(1)</a>：根据用户反馈，调整了默认的窗口管理器配置以提高可访问性。修复了 window focus 问题。</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=http%3A%2F%2Fman.netbsd.org%2FNetBSD-9.2%2Fi386%2Fftp.1" target="_blank">ftp(1)</a>： 修复了“<code>ftp -q</code>不起作用”的问题。（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgnats.netbsd.org%2F55857" target="_blank">PR 55857</a>）</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=http%3A%2F%2Fman.netbsd.org%2FNetBSD-9.2%2Fi386%2Fnl.1" target="_blank">nl(1)</a>： 改进的 POSIX 一致性。允许使用<code>-d</code>的一个和两个字符分隔符。（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgnats.netbsd.org%2F55891" target="_blank">PR 55891</a>）</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=http%3A%2F%2Fman.netbsd.org%2FNetBSD-9.2%2Fi386%2Fpatch.1" target="_blank">patch(1):</a>：修复了-V none的行为。</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=http%3A%2F%2Fman.netbsd.org%2FNetBSD-9.2%2Fi386%2Fprogress.1" target="_blank">progress(1)</a>：在写入时处理 EINTR。（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgnats.netbsd.org%2F55914" target="_blank">PR 55914</a>）</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=http%3A%2F%2Fman.netbsd.org%2FNetBSD-9.2%2Fi386%2Fhttpd.8" target="_blank">httpd(8) </a>：从 NetBSD HEAD 更新为 20210227。 
  <ul> 
   <li>在目录索引中添加了<code>README</code>文件支持。</li> 
   <li>为各种存档和视频格式添加了更多的 MIME 类型。</li> 
   <li>修复了在 32 位架构上提供大于 4GB 的服务文件。</li> 
   <li>各种稳定性修复程序。</li> 
  </ul> </li> 
 <li>......</li> 
</ul> 
<p><strong>系统调用和库</strong></p> 
<ul> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=http%3A%2F%2Fman.netbsd.org%2FNetBSD-9.2%2Fi386%2Fkevent.2" target="_blank">kevent(2)</a>： 修复了<code>kqueue_scan()</code>中的一场 race，它导致了事件的遗漏，以及 Go 计时器的延迟问题。（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgnats.netbsd.org%2F50094" target="_blank">PR 50094</a>）</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=http%3A%2F%2Fman.netbsd.org%2FNetBSD-9.2%2Fi386%2Fposix_spawn.3" target="_blank">posix_spawn(3)</a>：修复了对<code>POSIX_SPAWN_RESETIDS</code>的处理。</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=http%3A%2F%2Fman.netbsd.org%2FNetBSD-9.2%2Fi386%2Ffread.3" target="_blank">fread(3)</a>：优化了对非缓冲 I/O 的缓冲处理， 使该函数的速度提高了几个数量级。（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgnats.netbsd.org%2F55808" target="_blank">PR 55808</a>）</li> 
</ul> 
<p><strong>设备驱动程序</strong></p> 
<ul> 
 <li>pwm_backlight：在用户设置时保存新的亮度水平，防止 Pinebook Pro 的显示亮度在 DPMS 空白后重新设置。</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=http%3A%2F%2Fman.netbsd.org%2FNetBSD-9.2%2Fi386%2Fahcisata.4" target="_blank">ahcisata(4)</a>：各种一致性改进，在 Solidrun Honeycomb LX2K 上支持 SATA。</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=http%3A%2F%2Fman.netbsd.org%2FNetBSD-9.2%2Fi386%2Faudio.4" target="_blank">audio(4)</a>：修复了某些硬件上首选环绕声格式的问题，改为首选立体声。</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=http%3A%2F%2Fman.netbsd.org%2FNetBSD-9.2%2Fi386%2Faudio.4" target="_blank">audio(4)</a><em>:</em>: 修复了资源泄漏和锁定问题。</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=http%3A%2F%2Fman.netbsd.org%2FNetBSD-9.2%2Fi386%2Fcd.4" target="_blank">cd(4)</a>： 修复了“无法弹出以 sd(4) 连接的 USB 大容量存储器”的问题（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgnats.netbsd.org%2F55986" target="_blank">PR 55986</a>）</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=http%3A%2F%2Fman.netbsd.org%2FNetBSD-9.2%2Fi386%2Fena.4" target="_blank">ena(4)</a>： 修复了“被破坏的 ena<code>evcnts</code>引起 panic”（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgnats.netbsd.org%2F55942" target="_blank">PR 55942</a>）</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=http%3A%2F%2Fman.netbsd.org%2FNetBSD-9.2%2Fi386%2Fhilkbd.4" target="_blank">hilkbd(4)</a>：修复了控制台附件中的一个 race condition。</li> 
 <li>......</li> 
</ul> 
<p><strong>Ports</strong></p> 
<ul> 
 <li>arm： 修复了“Raspberry Pi 4 上 usb_transfer_complete() 的 panic”（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgnats.netbsd.org%2F55243" target="_blank"> PR 55243</a>）</li> 
 <li>arm： sync-lock 和 atomic operations 的修复。</li> 
 <li>mac68k：添加了<code>MAC68K_MEMSIZE</code>内核选项来解决 Booter 报告大小错误的问题。</li> 
 <li>mac68k：为 Quadra/Centris 650/800 修正 DJMEMCMAX。</li> 
 <li>m68k： plugged 内核堆栈的内存泄漏。（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgnats.netbsd.org%2F55990" target="_blank"> PR 55990</a>）</li> 
 <li>sparc：从<code>GENERIC</code>内核中删除<code>DIAGNOSTIC</code>选项。（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgnats.netbsd.org%2F56077" target="_blank"> PR 56077</a>）</li> 
 <li>x68k： 修复了 <a href="https://www.oschina.net/action/GoToLink?url=http%3A%2F%2Fman.netbsd.org%2FNetBSD-9.2%2Fi386%2Fsavecore.8" target="_blank">savecore(8)</a>。（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgnats.netbsd.org%2F51663" target="_blank"> PR 51663</a>）</li> 
 <li>zaurus：使 LCD BrightnessUp 和 BrightnessDown 在 C7x0/860 上工作。</li> 
 <li>修复了在旧架构上的安装问题： 
  <ul> 
   <li>alpha：切换回 .gz sets 以避免 xz extraction 内存耗尽。</li> 
   <li>miniroot：针对阻止安装问题的各种修复程序，将缺少的设置添加到默认设置。</li> 
   <li>hp300：删除了 INSTALL 和 RAMDISK 内核中的默认选项，这些选项会导致提取程序时间过长。</li> 
  </ul> </li> 
</ul> 
<p><strong>构建系统和工具链</strong></p> 
<ul> 
 <li>build.sh：从工具中删除了通用符号，以允许与较新的编译器进行交叉编译。</li> 
 <li>build.sh：修复了从 MacOS 与最近的 Clang 交叉构建 NetBSD 的问题。</li> 
</ul> 
<p><strong>第三方组件</strong></p> 
<p>对 NetBSD 基本系统中的各种第三方组件进行了更新：</p> 
<ul> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=http%3A%2F%2Fman.netbsd.org%2FNetBSD-9.2%2Fi386%2Fopenssl.1" target="_blank">openssl(1)</a>：更新至 1.1.1k 
  <ul> 
   <li>修复了 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fnvd.nist.gov%2Fvuln%2Fdetail%2FCVE-2021-3450" target="_blank">CVE-2021-3450</a>， <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fnvd.nist.gov%2Fvuln%2Fdetail%2FCVE-2021-3449" target="_blank">CVE-2021-3449</a></li> 
  </ul> </li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=http%3A%2F%2Fman.netbsd.org%2FNetBSD-9.2%2Fi386%2Ftmux.1" target="_blank">tmux(1)</a>：更新到 3.1c</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=http%3A%2F%2Fman.netbsd.org%2FNetBSD-9.2%2Fi386%2FXorg.1" target="_blank">Xorg(1)</a>：对以下内容应用了上游修复程序： 
  <ul> 
   <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fnvd.nist.gov%2Fvuln%2Fdetail%2FCVE-2021-3472" target="_blank">CVE-2021-3472</a>（本地特权升级）。</li> 
  </ul> </li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=http%3A%2F%2Fman.netbsd.org%2FNetBSD-9.2%2Fi386%2Fxdpyinfo.1" target="_blank">xdpyinfo(1)</a>：修复了“重定向或管道上无<code>xdpyinfo</code>输出”</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=http%3A%2F%2Fman.netbsd.org%2FNetBSD-9.2%2Fi386%2Fxterm.1" target="_blank">xterm(1)</a>：更新至 366 
  <ul> 
   <li>已修复 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fnvd.nist.gov%2Fvuln%2Fdetail%2FCVE-2021-27135" target="_blank">CVE-2021-27135</a>：纠正了选择缓冲区的上限，考虑到了组合字符。注意，目前还不清楚这个错误是否适用于 NetBSD。</li> 
  </ul> </li> 
 <li>freetype：更新至 2.10.4 
  <ul> 
   <li>已修复 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fnvd.nist.gov%2Fvuln%2Fdetail%2FCVE-2020-15999" target="_blank">CVE-2020-15999</a>：处理嵌入式 PNG 位图时的堆缓冲区溢出。注意，这个 bug 不适用于默认配置下的 NetBSD。</li> 
  </ul> </li> 
 <li>tzdata：更新至 2021a</li> 
 <li>libX11： 修复了 X Input Method 中的 off by one。（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgnats.netbsd.org%2F55640" target="_blank"> PR 55640</a>）</li> 
 <li>xkb：为以下应用了上游修复程序： 
  <ul> 
   <li>CVE-2020-14360 / ZDI-CAN-11572: XkbSetMap 越界访问</li> 
   <li>CVE-2020-25712 / ZDI-CAN-11839: XkbSetDeviceInfo 基于堆的缓冲区溢出</li> 
  </ul> </li> 
</ul> 
<p><strong>获取 NetBSD 9.2：</strong><strong> ​​​​​</strong></p> 
<ul> 
 <li>USB stick installation images: <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fcdn.netbsd.org%2Fpub%2FNetBSD%2FNetBSD-9.2%2Fimages%2FNetBSD-9.2-amd64-install.img.gz" target="_blank">64-bit x86</a>, <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fcdn.netbsd.org%2Fpub%2FNetBSD%2FNetBSD-9.2%2Fimages%2FNetBSD-9.2-i386-install.img.gz" target="_blank">32-bit x86</a></li> 
 <li>SD card live images: <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fcdn.netbsd.org%2Fpub%2FNetBSD%2FNetBSD-9.2%2Fevbarm-aarch64%2Fbinary%2Fgzimg%2Farm64.img.gz" target="_blank">64-bit ARM</a>, <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fcdn.netbsd.org%2Fpub%2FNetBSD%2FNetBSD-9.2%2Fevbarm-earmv7hf%2Fbinary%2Fgzimg%2Farmv7.img.gz" target="_blank">ARMv7</a> (most 32-bit boards), <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fcdn.netbsd.org%2Fpub%2FNetBSD%2FNetBSD-9.2%2Fevbarm-earmv6hf%2Fbinary%2Fgzimg%2Frpi.img.gz" target="_blank">ARMv6</a> (Raspberry Pi 1 only)</li> 
 <li>CD installation images: <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fcdn.netbsd.org%2Fpub%2FNetBSD%2FNetBSD-9.2%2Fimages%2FNetBSD-9.2-amd64.iso" target="_blank">64-bit x86</a>, <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fcdn.netbsd.org%2Fpub%2FNetBSD%2FNetBSD-9.2%2Fimages%2FNetBSD-9.2-i386.iso" target="_blank">32-bit x86</a>, <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fcdn.netbsd.org%2Fpub%2FNetBSD%2FNetBSD-9.2%2Fimages%2FNetBSD-9.2-sparc64.iso" target="_blank">64-bit SPARC</a></li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fcdn.netbsd.org%2Fpub%2FNetBSD%2FNetBSD-9.2%2Fimages%2F" target="_blank">Other images</a> and <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fcdn.netbsd.org%2Fpub%2FNetBSD%2FNetBSD-9.2%2F" target="_blank">distribution files</a></li> 
</ul> 
<p>更多详情可查看发布公告：<a href="https://www.oschina.net/action/GoToLink?url=http%3A%2F%2Fnetbsd.org%2Freleases%2Fformal-9%2FNetBSD-9.2.html" target="_blank">http://netbsd.org/releases/formal-9/NetBSD-9.2.html</a></p>
                                        </div>
                                      
</div>
            