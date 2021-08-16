
---
title: 'Debian 11'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://static.oschina.net/uploads/space/2021/0816/072808_orA7_4937141.png'
author: 开源中国
comments: false
date: Sun, 15 Aug 2021 23:32:00 GMT
thumbnail: 'https://static.oschina.net/uploads/space/2021/0816/072808_orA7_4937141.png'
---

<div>   
<div class="content">
                                                                                            <p>经过 2 年 1 个月零 9 天的开发，Debian 11.0 "bullseye" 正式发布了。该版本包括许多重大的变化，并将在未来 5 年内得到支持。</p> 
<h3>Debian 11 支持的计算机架构包括：</h3> 
<ul> 
 <li>32 位 PC（<strong><code>i386</code></strong>）和 64 位 PC（<strong><code>amd64</code></strong>）</li> 
 <li>64 位 ARM（<strong><code>arm64</code></strong>）</li> 
 <li>ARM EABI（<strong><code>armel</code></strong>）</li> 
 <li>ARMv7（EABI 硬浮点 ABI，<strong><code>armhf</code></strong>）</li> 
 <li>MIPS（<strong><code>mipsel</code></strong>）</li> 
 <li>64 位 MIPS（<strong><code>mips64el</code></strong>）</li> 
 <li>PowerPC（<strong><code>ppc64el</code></strong>）</li> 
 <li>IBM System z（<strong><code>s390x</code></strong>）</li> 
</ul> 
<h3>这次发布中有什么新变化</h3> 
<p>Debian 的这次发行再次带来了比上一版本 buster 更多的软件；本次发行包括 11294 个新软件包，软件包的总数达到了 59551 个。这个发行版的多数软件包得到了更新：更新了 42821 个软件包（占 buster 软件包总数的 72%）。而且，由于各种原因，有相当数量的软件包（9519 个，占 buster 软件包总数的 16%）从这次发行中被删除了。您将不会看到这些包有任何更新，而且在包管理软件中它们会被标记为“过时的”；</p> 
<h4><strong>桌面程序和软件包</strong></h4> 
<p>如往常一样，Debian 也提供了多个桌面程序和环境。提供的桌面环境包括 GNOME 3.38，KDE Plasma 5.20，LXDE 11，LXQt 0.16，MATE 1.24，以及 Xfce 4.16。</p> 
<p>生产力应用也得到了升级，包括办公套件：</p> 
<ul> 
 <li>LibreOffice 已升级到 7.0 版；</li> 
 <li>Calligra 已升级到 3.2 版；</li> 
 <li>GNUcash 已升级到 4.4 版；</li> 
</ul> 
<p>这次发行包含了许多软件的更新，其中包括：</p> 
<p><img alt height="633" src="https://static.oschina.net/uploads/space/2021/0816/072808_orA7_4937141.png" width="700" referrerpolicy="no-referrer"></p> 
<h4><strong>无驱动扫描和打印</strong></h4> 
<p>使用 <strong><code>CUPS</code></strong> 打印以及使用 <strong><code>SANE</code></strong> 扫描对于越来越多的硬件型号已经可以实现无需任何驱动程序（通常是非自由驱动程序）即可正常操作，尤其是过去五年以来出现在市场上的新设备。</p> 
<ul> 
 <li><strong>CUPS 和无驱动打印</strong></li> 
</ul> 
<p>使用以太网或无线网络连接的现代打印机已经可以使用<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwiki.debian.org%2FCUPSQuickPrintQueues" target="_blank">无驱动打印功能</a>，由 <strong><code>CUPS</code></strong> 和 <strong><code>cups-filters</code></strong> 软件包提供支持，此功能已在 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.debian.org%2Freleases%2Fbuster%2Famd64%2Frelease-notes%2Fch-whats-new.html%23driverless-printing" target="_blank">Debian buster 发行注记</a>中描述。Debian 11 “bullseye” 提供了新软件包 <strong><code>ipp-usb</code></strong>；它使用许多现代打印机所支持的、供应商中立的 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwiki.debian.org%2FCUPSDriverlessPrinting%23ippoverusb" target="_blank">IPP-over-USB</a> 协议，且 <strong><code>cups-daemon</code></strong> 推荐安装该软件包。它使得 USB 设备可被视作网络设备，以将无驱动打印扩展至包括 USB 连接的打印机。</p> 
<p>在 <strong><code>ipp-usb</code></strong> 软件包中包含的 systemd 服务文件将在使用 USB 的打印机连接到系统时启动 <strong><code>ipp-usb</code></strong> 守护程序，以使其可用于打印任务。默认情况下 <strong><code>cups-browsed</code></strong> 软件包应当可以自动完成配置，或者可以<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwiki.debian.org%2FSystemPrinting" target="_blank">手动设置本地无驱动打印队列</a>。</p> 
<ul> 
 <li><strong>SANE 和无驱动扫描</strong></li> 
</ul> 
<p>官方的 <strong><code>SANE</code></strong> 无驱动后端在 <strong><code>libsane1</code></strong> 软件包中由 <strong><code>sane-escl</code></strong> 提供。另有一独立开发的无驱动后端 <strong><code>sane-airscan</code></strong>。两个后端均可使用 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwiki.debian.org%2FSaneOverNetwork%23escl" target="_blank">eSCL 协议</a>，但 <strong><code>sane-airscan</code></strong> 另外也可使用 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwiki.debian.org%2FSaneOverNetwork%23wsd" target="_blank">WSD</a> 协议。用户应该考虑在系统上同时安装两个后端。</p> 
<p><strong><code>eSCL</code></strong> 和 <strong><code>WSD</code></strong> 均为网络协议。因此，它们在设备是 <strong><code>IPP-over-USB</code></strong> 设备的情况下也可经由 USB 连接生效（参见上文）。请注意 <strong><code>libsane1</code></strong> 推荐安装 <strong><code>ipp-usb</code></strong> 软件包。在软件包已安装的情况下，合适的设备可以在使用 USB 端口连接到系统的同时自动设置使用无驱动后端。</p> 
<h4><strong>新的通用 open 命令</strong></h4> 
<p>新增加的 <strong>open</strong> 命令将作为 <strong>xdg-open</strong>（默认）或者 <strong>run-mailcap</strong> 的别名出现，具体实现则由 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fmanpages.debian.org%2F%2Fbullseye%2Fdpkg%2Fupdate-alternatives.1.html" target="_blank">update-alternatives</a> 系统管理。它旨在作为命令行交互工具，帮助用户使用默认的应用程序打开文件；所使用的程序按照具体情况可以是图形界面程序。</p> 
<h4><strong>控制组 v2</strong></h4> 
<p>在 bullseye 中，systemd 默认使用控制组 v2（cgroupv2），它提供了统一的资源控制层级架构。如果有需要，可以使用内核命令行参数重新启用旧有的 cgroups；</p> 
<h4><strong>持久化 systemd 日志</strong></h4> 
<p>在 bullseye 中的 systemd 默认启用了持久日志的功能，日志文件存放于 <strong><code>/var/log/journal/</code></strong>。请参见 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fmanpages.debian.org%2F%2Fbullseye%2Fsystemd%2Fsystemd-journald.service.8.html" target="_blank">systemd-journald.service(8)</a> 以了解细节；请注意 Debian 中的日志除了默认的 <strong><code>systemd-journal</code></strong> 组外，还可以被 <strong><code>adm</code></strong> 用户组内的成员阅读。</p> 
<p>这项改动应该不会对任何已有的传统日志守护程序（例如 <strong><code>rsyslog</code></strong>）产生任何干扰，但是不依赖这些守护程序所提供的特别功能的用户应当考虑将传统日志程序卸载并切换到仅使用新的 systemd 日志工具。</p> 
<h4><strong>新的 Fcitx 5 输入法</strong></h4> 
<p>Fcitx 5 是用于中文、日语、韩语和其它许多语言的一个输入法。它是 buster 提供的 Fcitx 4 的后续版本。新版本增加了对 Wayland 的支持并改进了扩展支持。</p> 
<h4><strong>内核 exFAT 支持</strong></h4> 
<p>bullseye 是第一个提供支持 exFAT 文件系统的 Linux 内核的发行版本，且它默认使用该实现挂载 exFAT 文件系统。因此，用户不再需要使用 <strong><code>exfat-fuse</code></strong> 软件包所提供的用户空间文件系统实现。如果您要继续使用用户空间文件系统的实现，您需要在挂载 exFAT 文件系统时直接调用 <strong>mount.exfat-fuse</strong> 命令。</p> 
<p>创建和检查 exFAT 文件系统的工具位于 <strong><code>exfatprogs</code></strong> 软件包，它由 Linux 内核 exFAT 实现的作者编写。由已有的 <strong><code>exfat-utils</code></strong> 软件包提供的独立实现仍然可用，但它不能与新的实现共同安装在系统上。我们推荐您迁移到使用 <strong><code>exfatprogs</code></strong> 软件包，尽管您需要注意并处理两者可能不互相兼容的命令行选项。</p> 
<h4><strong>改进的 man page 翻译</strong></h4> 
<p>部分项目，例如 systemd、 util-linux、 OpenSSH 和 Mutt 的部分语言的手册页，例如法语、西班牙语和马其顿语，得到了明显改进。欲获得此项改进，请安装 <strong><code>manpages-*xx*</code></strong>（其中 <strong><em><code>xx</code></em></strong> 是您所需的自然语言的代码）。</p> 
<p>在 bullseye 的生命周期中，进一步的翻译改进将会通过 <strong><code>backports</code></strong> 仓库提供。</p> 
<p>更多详情可查看：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.debian.org%2FNews%2F2021%2F20210814" target="_blank">https://www.debian.org/News/2021/20210814</a></p>
                                        </div>
                                      
</div>
            