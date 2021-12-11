
---
title: 'Kali Linux 2021.4 发布，Xfce、GNOME 和 KDE 均获得更新'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://static.oschina.net/uploads/img/202112/11074022_oA5Q.png'
author: 开源中国
comments: false
date: Sat, 11 Dec 2021 07:40:00 GMT
thumbnail: 'https://static.oschina.net/uploads/img/202112/11074022_oA5Q.png'
---

<div>   
<div class="content">
                                                                                            <p>Kali Linux 2021.4 正式发布，该版本也是 Kali Linux 今年的最后一个版本。自 2021 年 9 月的 2021.3 版本以来的主要更新内容包括：</p> 
<h3>改进了对 Apple M1 的支持</h3> 
<p>在 Kali Linux 2021.1 中支持在使用 Apple Silicon 芯片的 Mac 上通过 Parallels 安装 Kali Linux。现在在 2021.4 中，已支持在 VMware Fusion 上安装，这要归功于 5.14 内核具有所使用的虚拟 GPU 的模块。</p> 
<h3>对 Samba 的广泛兼容</h3> 
<p>从 Kali Linux 2021.4 开始，Samba 客户端现在被配置为广泛的兼容性，因此无论使用的协议版本如何，它可以连接到几乎所有的 Samba 服务器。这一变化应该使它更容易发现 Samba 服务器，而不需要配置 Kali。</p> 
<h3>切换软件包管理器的镜像</h3> 
<p>默认情况下，当 Kali 系统被更新时，软件包管理器（APT）会从附近的社区镜像下载软件包。但你也可以将 Kali 配置为从 CloudFlare CDN 获取软件包。现在可以通过使用 <code>kali-tweaks</code> 来快速配置 APT 是否应该使用社区镜像或 CloudFlare CDN。</p> 
<h3>Kaboxer 主题支持</h3> 
<p>随着 Kaboxer 工具的最新更新，它带来了对窗口主题和图标主题的支持（分别放在 <code>/usr/share/themes</code> 和 <code>/usr/share/icons</code> 里面）。这使得该程序能够与桌面的其他部分适当地整合，并避免使用丑陋的主题。</p> 
<p><img alt="https://www.kali.org/blog/kali-linux-2021-4-release/images/kaboxer-theme-support.png" height="269" src="https://static.oschina.net/uploads/img/202112/11074022_oA5Q.png" width="700" referrerpolicy="no-referrer"></p> 
<h3>桌面和主题的增强</h3> 
<p>这个版本为所有 3 个主要的桌面（Xfce、GNOME 和 KDE）带来了更新，但其中一个共同点是新的窗口按钮设计。以前的按钮是为了适应 Xfce 的窗口主题而设计的，但在其他桌面上却不能很好地工作，而且缺乏个性。新的设计适用于任何桌面。</p> 
<p><img alt="https://www.kali.org/blog/kali-linux-2021-4-release/images/new-window-buttons.png" height="254" src="https://static.oschina.net/uploads/img/202112/11074023_d9rz.png" width="700" referrerpolicy="no-referrer"></p> 
<ul> 
 <li> <p><strong>Xfce</strong></p> <p>面板布局已经被调整，以优化水平空间，并为两个新的小组件腾出空间：CPU 使用率小组件和 VPN IP 小组件，除非建立了 VPN 连接，否则该组件将被隐藏。</p> <p><img alt="https://www.kali.org/blog/kali-linux-2021-4-release/images/xfce-layout-updates.png" height="408" src="https://static.oschina.net/uploads/img/202112/11074024_9Erw.png" width="700" referrerpolicy="no-referrer"></p> </li> 
 <li> <p><strong>GNOME 41</strong></p> <p>在这次更新中，GNOME Desktop 获得了两个版本的提升。自 Kali 中的 GNOME Desktop 上一次重大更新（GNOME 3.38）已经过去了一年，从那时起，GNOME 已推出了 40 和 41 两个版本，Kali Linux 现已更新至最新的 GNOME 41。</p> <p><img alt="https://www.kali.org/blog/kali-linux-2021-4-release/images/gnome41.png" height="394" src="https://static.oschina.net/uploads/img/202112/11074024_eAgb.png" width="700" referrerpolicy="no-referrer"></p> </li> 
 <li> <p><strong>KDE 5.23</strong></p> <p>KDE 团队为庆祝其 25 周年，发布了 Plasma 的 5.23 更新。这个更新现在可以在 Kali 中使用，它带来了 Breeze 主题的新设计，它用细节改善了 Plasma 的外观。</p> <p>KDE 的新窗口主题现在是基于 breeze，而不是 Aurorae。这修复了之前在 HiDPI 显示器上窗口缩放的问题。</p> </li> 
</ul> 
<h3>Kali ARM 更新</h3> 
<ul> 
 <li>所有的镜像现在都使用 ext4 作为其根文件系统，并在第一次启动时调整根文件系统的大小。这带来了比之前使用的 ext3 更快的速度，并且在第一次重启时减少了调整大小的启动时间。</li> 
 <li>Raspberry Pi Zero 2 W 的支持已经被添加，但和 Raspberry Pi 400 一样，没有 Nexmon 支持。</li> 
 <li>Pinebook Pro 现在可以超频了。大核心得到 2GHz，小核心得到 1.5GHz 的加成。 
  <ul> 
   <li><code>echo 1 | sudo tee /sys/devices/system/cpu/cpufreq/boost</code> 启用</li> 
   <li><code>echo 0 | sudo tee /sys/devices/system/cpu/cpufreq/boost</code> 禁用</li> 
  </ul> </li> 
 <li>USBArmory MkII 镜像已被添加。</li> 
</ul> 
<p>更多详情可查看：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.kali.org%2Fblog%2Fkali-linux-2021-4-release%2F" target="_blank">https://www.kali.org/blog/kali-linux-2021-4-release/</a></p>
                                        </div>
                                      
</div>
            