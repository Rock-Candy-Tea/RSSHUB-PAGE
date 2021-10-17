
---
title: 'KaOS 2021.10 发布，KDE 桌面 Linux 发行版'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://kaosx.us/img/2021/bootloader.png'
author: 开源中国
comments: false
date: Sun, 17 Oct 2021 07:28:00 GMT
thumbnail: 'https://kaosx.us/img/2021/bootloader.png'
---

<div>   
<div class="content">
                                                                    
                                                        <p>KDE 成立 25 周年，为了纪念这一日子，KaOS 发布了 2021.10 的 ISO，其中包括最新的 Plasma 5.23.0。</p> 
<p>另一个最大的变化是增加了一个引导程序选择模块。对于 UEFI 安装，现在可以在 systemd-boot、rEFInd 或 No Bootloader 之间进行选择，所有这些都在一个基于 QML 的 GUI 中呈现。</p> 
<p><img alt="https://kaosx.us/img/2021/bootloader.png" src="https://kaosx.us/img/2021/bootloader.png" referrerpolicy="no-referrer"></p> 
<p>Plasma 5.23 的亮点包括：Kickoff 接受了大量代码修改，提高了性能和可访问性，并且可以选择所有应用程序的列表或网格视图，Systemsettings 有更容易的查找选项，以及一个计时器来恢复可能不想要的显示设置。</p> 
<p>对于其他 KDE 部分，包括最新的框架 5.85.0 和 KDE 应用程序 21.08.2。所有这些都建立在 Qt 5.15.2+。</p> 
<p><img alt="https://kaosx.us/img/2021/plasma_5.23.png" src="https://kaosx.us/img/2021/plasma_5.23.png" referrerpolicy="no-referrer"></p> 
<p>这个发行版的基础软件包更新包括 Systemd 249.4、Curl 7.79.1、Coreutils 9.0、NetworkManager 1.32.12、Mesa 21.2.3、Bison 3.8.2、Vulkan packages 1.2.195、Udisks 2.9.4、Sudo 1.9.8p2 和 Pacman 6.0.1。</p> 
<p><img alt="https://kaosx.us/img/2021/pmanager.png" src="https://kaosx.us/img/2021/pmanager.png" referrerpolicy="no-referrer"></p> 
<p>pmanager，KaOS 使用的软件包查看器，在其后端部分大部分被重写了。这是由于基于 json 的旧数据库迁移到更一致的 SQLite 系统。</p> 
<p>KaOS 使用 Systemd 提供的 Systemd-boot 进行 UEFI 安装。包括用于将 ISO 文件写入 USB 的 KaOS 特定工具 —— IsoWriter，它不仅可以写入 USB，它还提供了在将 U 盘用于 ISO 后复原 U 盘的选项，这是以前使用的 Imagewriter 无法做到的。这个版本的新功能还可以验证写入的 U 盘与下载的 ISO 文件相比是否完整。</p> 
<p>LibreOffice 如今已取代了 Calligra 成为 KaOS 的默认办公应用程序。</p> 
<h3>已知的问题：</h3> 
<ul> 
 <li>目前无法在 RAID 上安装</li> 
</ul> 
<p>更多详情可查看：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fkaosx.us%2Fnews%2F2021%2Fkaos10%2F" target="_blank">https://kaosx.us/news/2021/kaos10/</a></p>
                                        </div>
                                      
</div>
            