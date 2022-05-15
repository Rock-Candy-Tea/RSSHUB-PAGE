
---
title: 'ALT Linux 10.0 已发布'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://static.oschina.net/uploads/space/2022/0515/074939_Jk8o_5430600.png'
author: 开源中国
comments: false
date: Sat, 14 May 2022 23:56:00 GMT
thumbnail: 'https://static.oschina.net/uploads/space/2022/0515/074939_Jk8o_5430600.png'
---

<div>   
<div class="content">
                                                                    
                                                        <p style="margin-left:0; margin-right:0; text-align:start">ALT Linux 是俄罗斯的一款 Linux 操作系统，基于 KDE Plasma 图形环境构建，在风格上最接近 Windows 操作系统。</p> 
<p style="margin-left:0; margin-right:0; text-align:start"><img alt height="394" src="https://static.oschina.net/uploads/space/2022/0515/074939_Jk8o_5430600.png" width="700" referrerpolicy="no-referrer"></p> 
<p style="margin-left:0; margin-right:0; text-align:start">目前 ALT Linux 的第十个版本 “Alt Workstation K 10” <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.basealt.ru%2Fabout%2Fnews%2Farchive%2Fview%2Fnovaja-versija-os-alt-rabochaja-stancija-k-10-svobodno-integriruetsja-v-ljubuju-it-infrastrukturu-i-usilivaet-ejo-zashchitu" target="_blank">发布了</a>，<span><span><span><span><span style="color:#333333"><span><span><span><span><span><span><span><span><span><span><span><span><span><span>以下是该版本的主要变化。</span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></p> 
<ul style="margin-left:0; margin-right:0"> 
 <li>操作系统基于当前的 Linux 5.15 LTS 内核（长期支持）。向新内核的过渡提供了许多<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.opennet.ru%2Fopennews%2Fart.shtml%3Fnum%3D56079" target="_blank">新功能</a>。特别是与 Intel 12 代 Alder Lake 处理器的配合得到了改进，增加了对基于 RDNA 2 架构的 AMD 显卡的支持，包括了一个新的 NTFS 文件系统驱动程序（提高了数据传输速度）。文件系统）。优化了适用于 Linux 的经典 ext4 文件系统，提高了 Btrfs 文件系统的性能。</li> 
 <li>更改了<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.altlinux.org%2FUEFI" target="_blank">安全启动</a>签名方案。该发行版仍会在不禁用安全启动的情况下安装。</li> 
 <li>扩展组策略功能，添加新模板。使用<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.altlinux.org%2F%25D0%2593%25D1%2580%25D1%2583%25D0%25BF%25D0%25BF%25D0%25BE%25D0%25B2%25D1%258B%25D0%25B5_%25D0%25BF%25D0%25BE%25D0%25BB%25D0%25B8%25D1%2582%25D0%25B8%25D0%25BA%25D0%25B8%2FADMC" target="_blank">ADMC</a>开发工具“Basalt SPO”，您可以管理 Active Directory 域和组策略。</li> 
 <li>增加了一个带有<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fpackages.altlinux.org%2Fru%2Fsisyphus%2Fsrpms%2Fca-certificates-digital.gov.ru" target="_blank">加密根证书</a>的包。</li> 
 <li>包含软件包以支持通过硬件令牌（Rutoken、JaCarta、ESMART）进行的两因素身份验证。</li> 
 <li>新增安装兼容俄罗斯国产软件的包：ViPNet、1C:Enterprise、Yandex.Browser等。</li> 
 <li>改进了对 OKI、Brother、Epson 打印机和扫描仪的支持。</li> 
 <li>对 Flathub 存储库的支持已添加到 OS 应用程序中心，用于以 flatpak 格式安装第三方应用程序。</li> 
 <li>添加了对 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fsnapcraft.io%2F" target="_blank">SNAP 应用程序</a>的支持。</li> 
 <li>有用的实用程序包括：clinfo（获取有关 OpenCL 加速状态的信息）、glxinfo、vulkan-tools（用于检查 3D 加速设置）等等。</li> 
 <li>现在可以在安装过程中截屏。</li> 
 <li>实施安全系统更新。出现更新时，建议重新启动，在此期间系统会更新。</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdoc.qt.io%2Fqt-5%2Fwhatsnew515.html" target="_blank">包括 Qt 5.15</a> 跨平台长期支持 (LTS) 框架。它有许多新功能，特别是对 3D 图形的支持。</li> 
</ul> 
<p style="margin-left:0; margin-right:0; text-align:start"><span><span><span><span><span style="color:#333333"><span><span><span><span><span><span><span><span><span><span><span><span><span><span>操作系统“ Alt Workstation K ”10 和以前一样配备了美观方便的图形化 Plasma 外壳，新版本 KDE Plasma 5.23 包括对 Wayland 图形子系统的支持，这使得它可以在平板电脑上工作。另外，此版本支持NVIDIA 340、390和470、510系列GPU的四代驱动，在带有NVIDIA显卡的电脑上安装操作系统时，会自动安装正确的驱动版本。</span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></p> 
<p style="margin-left:0; margin-right:0; text-align:start"><span><span><span><span><span style="color:#333333"><span><span><span><span><span><span><span><span><span><span><span><span><span><span>更多内容可在<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.basealt.ru%2Fabout%2Fnews%2Farchive%2Fview%2Fnovaja-versija-os-alt-rabochaja-stancija-k-10-svobodno-integriruetsja-v-ljubuju-it-infrastrukturu-i-usilivaet-ejo-zashchitu" target="_blank">官方公告</a>中查看。</span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></p>
                                        </div>
                                      
</div>
            