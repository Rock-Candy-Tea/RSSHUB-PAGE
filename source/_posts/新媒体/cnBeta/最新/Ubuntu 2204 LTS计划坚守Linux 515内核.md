
---
title: 'Ubuntu 22.04 LTS计划坚守Linux 5.15内核'
categories: 
 - 新媒体
 - cnBeta
 - 最新
headimg: 'https://static.cnbetacdn.com/article/2022/0114/3137145082db236.webp'
author: cnBeta
comments: false
date: Fri, 14 Jan 2022 12:45:08 GMT
thumbnail: 'https://static.cnbetacdn.com/article/2022/0114/3137145082db236.webp'
---

<div>   
事实证明，Ubuntu 22.04 LTS计划使用Linux 5.15内核作为其默认内核。这是有道理的，因为Linux
5.15也是一个长期支持的内核，但不幸的是，Ubuntu LTS版本并不总是使用LTS内核版本，当"Jammy
Jellyfish"在四月发布时，v5.15已经公布有半年时间了。这对那些拥有最新硬件的人来说是一个特别不幸的选择，但至少还有Ubuntu主线内核PPA和其他非默认选项可用。<br>
 <p><a href="https://static.cnbetacdn.com/article/2022/0114/3137145082db236.webp" target="_blank"><img src="https://static.cnbetacdn.com/article/2022/0114/3137145082db236.webp" referrerpolicy="no-referrer"></a></p><p>在关于Ubuntu 22.04的GNOME计划的讨论中，Canonical的Sebastien Bacher提到，"计划是在LTS中使用5.15，但是oem和hwe版本将在某个时候升级到5.17"。</p><p>因此，如果这个计划坚持下去，默认情况下，Ubuntu 22.04 LTS将使用Linux 5.15，而在2023年，Ubuntu 22.04.2 LTS将使用Ubuntu 22.10的新硬件启用内核，一方面Ubuntu的OEM合作伙伴如<a data-link="1" href="http://www.anrdoezrs.net/links/9019719/type/dlg/sid//https://www.dell.com/zh-cn/shop/deals" target="_blank">戴尔</a>也有能力为他们最新的Linux预装系统运送更新的内核。</p><p>Linux 5.15对Ubuntu 22.04来说确实有意义，因为两者都是长期支持（LTS）版本。Linux 5.15 LTS是在10月底发布的，Linux 5.16是在上周发布的，然后Linux 5.17应该在3月底左右发布，因此Linux 5.17无论如何都不会在Ubuntu的22.04版本中默认出现。</p><p>Linux 5.16带来了默认启用的Alder Lake S图形支持，FUTEX2 futex_waitv系统调用，这对Wine / Steam Play游戏的发展非常重要，I/O优化，更充分的<a data-link="1" href="https://c.duomai.com/track.php?site_id=242986&euid=&t=https://amd-cpu.jd.com/" target="_blank">AMD</a> Ryzen 6000移动系列支持，Intel AMX支持，这对Ubuntu LTS版本中的Xeon Sapphire Rapids服务器也非常重要，还有许多其他硬件支持的增加和改进。一些修复/PCI ID的增加可能会被回传到Linux 5.15或由Ubuntu的内核构建来进行，但后续可能不会有任何大的项目出现。</p><p>因此，虽然从后勤角度来看，Linux 5.15 LTS对Ubuntu 22.04 LTS是有意义的，但特别是Linux爱好者和那些想在最新的Intel/AMD硬件上运行Ubuntu的人最好使用第三方/非官方的内核构建，直到未来Jammy Jellyfish版本中引入HWE内核。值得庆幸的是，Ubuntu主线内核PPA在Ubuntu 22.04正式发布时提供了方便的Linux 5.16或Linux 5.17的主线内核构建，以及其他第三方内核构建/PPA。随着Canonical想让Ubuntu成为"最适合游戏的Linux桌面"，也许他们会想出一个更加认可/用户友好的方式，例如在Ubuntu上运行更多最新的Linux主线稳定版本。</p>   
</div>
            