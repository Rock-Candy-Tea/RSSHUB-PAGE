
---
title: 'Alpine Linux 已发布，注重安全的轻量级 Linux 发行版'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=5032'
author: 开源中国
comments: false
date: Tue, 24 May 2022 07:46:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=5032'
---

<div>   
<div class="content">
                                                                    
                                                        <p style="margin-left:0px">Alpine Linux 是一个面向安全的轻量级 Linux 发行版，该发行版以安全为理念，面向 x86 路由器、防火墙、虚拟专用网、IP 电话盒及服务器而设计。</p> 
<p style="margin-left:0px">另外，不同于常见的 Linux 发行版，Alpine Linux 采用 <a href="https://www.oschina.net/action/GoToLink?url=http%3A%2F%2Fmusl-libc.org%2F">musl libc</a> 和 <a href="https://www.oschina.net/action/GoToLink?url=http%3A%2F%2Fbusybox.net%2F">busybox</a> 以减小系统的体积和运行时资源消耗。在保持瘦身的同时，Alpine Linux 还提供了自己的包管理工具 apk，可以在其网站上<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fpkgs.alpinelinux.org%2Fpackages">查询软件包</a>，或直接通过 apk 命令进行查询和安装。</p> 
<p style="margin-left:0px">Alpine Linux 3.16 更新内容如下：</p> 
<h3><strong>/tmp 挂载为 tmpfs</strong></h3> 
<p style="margin-left:0px">以前<code>/tmp</code>是根文件系统的一部分，并在启动时通过 bootmisc openrc 服务脚本进行清理。在 v3.16 中，新安装将<code>/tmp</code>作为 tmpfs 挂载。</p> 
<h3 style="margin-left:0px"><strong>ICU 数据拆分</strong></h3> 
<p style="margin-left:0px">icu 包已拆分为：</p> 
<ul> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fpkgs.alpinelinux.org%2Fpackages%3Fname%3Dicu-data-en%26branch%3Dedge%26repo%3D%26arch%3Dx86_64%26maintainer%3D" target="_blank">icu-data-en</a> (2.6 MiB) - 仅使用 en_US/GB 区域设置且没有遗留字符集转换器的 ICU 数据。</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fpkgs.alpinelinux.org%2Fpackages%3Fname%3Dicu-data-full%26branch%3Dedge%26repo%3D%26arch%3Dx86_64%26maintainer%3D" target="_blank">icu-data-full</a> (29 MiB) - 完整的 ICU 数据。</li> 
</ul> 
<p style="margin-left:0px"><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fpkgs.alpinelinux.org%2Fpackages%3Fname%3Dicu-libs%26branch%3Dedge%26repo%3D%26arch%3Dx86_64%26maintainer%3D" target="_blank">icu-libs</a> 只安装 icu-data-en。如果需要额外的语言支持，则需要手动安装 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fpkgs.alpinelinux.org%2Fpackages%3Fname%3Dicu-data-full%26branch%3Dedge%26repo%3D%26arch%3Dx86_64%26maintainer%3D" target="_blank">icu-data-full 。</a></p> 
<p style="margin-left:0px">nodejs 现在使用系统 ICU 编译。</p> 
<h3><strong>网络管理器插件</strong></h3> 
<p>NetworkManager 插件（例如 WiFi 或 ADSL 支持）已被移动到子包中，默认情况下不安装。如果需要，请安装相应的软件包：</p> 
<ul> 
 <li>WiFi：网络<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fpkgs.alpinelinux.org%2Fpackages%3Fname%3Dnetworkmanager-wifi%26branch%3Dedge%26repo%3D%26arch%3Dx86_64%26maintainer%3D" target="_blank">管理器-wifi</a></li> 
 <li>ADSL：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fpkgs.alpinelinux.org%2Fpackages%3Fname%3Dnetworkmanager-adsl%26branch%3Dedge%26repo%3D%26arch%3Dx86_64%26maintainer%3D" target="_blank">网络管理器-adsl</a></li> 
 <li>移动宽带：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fpkgs.alpinelinux.org%2Fpackages%3Fname%3Dnetworkmanager-wwan%26branch%3Dedge%26repo%3D%26arch%3Dx86_64%26maintainer%3D" target="_blank">networkmanager-wwan</a></li> 
 <li>蓝牙：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fpkgs.alpinelinux.org%2Fpackages%3Fname%3Dnetworkmanager-bluetooth%26branch%3Dedge%26repo%3D%26arch%3Dx86_64%26maintainer%3D" target="_blank">networkmanager-蓝牙</a></li> 
 <li>PPP：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fpkgs.alpinelinux.org%2Fpackages%3Fname%3Dnetworkmanager-ppp%26branch%3Dedge%26repo%3D%26arch%3Dx86_64%26maintainer%3D" target="_blank">网络管理器-ppp</a></li> 
 <li>打开 vSwitch：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fpkgs.alpinelinux.org%2Fpackages%3Fname%3Dnetworkmanager-ovs%26branch%3Dedge%26repo%3D%26arch%3Dx86_64%26maintainer%3D" target="_blank">networkmanager-ovs</a></li> 
</ul> 
<h2 style="margin-left:0px">新功能和值得注意的新软件包</h2> 
<ul> 
 <li>修复了使用控制台将驱动程序编译为模块时不显示引导输出的问题</li> 
 <li>OpenRC 输出会显示在 VirtIO 串行控制台上。</li> 
</ul> 
<h3 style="margin-left:0px"><strong>SDL 1.2 迁移到 SDL 1.2 兼容</strong></h3> 
<p style="margin-left:0px">旧的 sdl 包 (SDL 1.2) 已从社区转移到测试，因此不会成为 Alpine 3.16 的一部分。</p> 
<h2>其他软件更新</h2> 
<ul style="list-style-type:disc"> 
 <li>GNOME 42</li> 
 <li>LLVM 13</li> 
 <li>PHP 8.0 and 8.1 both shipped</li> 
 <li>Python 3.10</li> 
 <li>QEMU 7</li> 
 <li>R 4.2</li> 
 <li>Ruby 3.1</li> 
 <li>Rust 1.60</li> 
 <li>Sway 1.7</li> 
 <li>Xen 4.16.1</li> 
</ul> 
<h3 style="margin-left:0; margin-right:.3em; text-align:start"><span><span><span style="color:#000000"><strong><span><span><span><span><span><span><span><span><span><span><span><span><span><span><span>KDE</span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></strong></span></span></span></h3> 
<p><span><span><span style="color:#222222"><span><span><span><span><span><span><span><span><span><span><span><span style="background-color:#ffffff"><span><span><span>Plasma 已从 5.23 升级到 5.24。</span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></p> 
<p><span><span><span style="color:#222222"><span><span><span><span><span><span><span><span><span><span><span><span style="background-color:#ffffff"><span><span><span>KDE 应用程序（发布服务）已从 21.08 升级到 22.04，KDE 框架已从 5.88 升级到 5.93。</span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></p> 
<p><span><span><span style="color:#222222"><span><span><span><span><span><span><span><span><span><span><span><span style="background-color:#ffffff"><span><span><span>Plasma Mobile Gear 已从 21.12 升级到 22.04。</span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></p> 
<h3><span><span><span style="color:#000000"><strong><span><span><span><span><span><span><span><span><span><span><span><span><span><span><span>Python 升级到 3.10</span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></strong></span></span></span></h3> 
<p><span><span><span style="color:#222222"><span><span><span><span><span><span><span><span><span><span><span><span style="background-color:#ffffff"><span><span><span>Python 已经升级到 3.10 版本，所有模块都针对 python 3.10 进行了重建。</span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></p> 
<p><span><span><span style="color:#222222"><span><span><span><span><span><span><span><span><span><span><span><span style="background-color:#ffffff"><span><span><span>手动安装的 Python 模块必须针对 3.10 重新编译。</span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></p> 
<h2><span><span><span style="color:#000000"><span><span><span><span><span><span><span><span><span><span><span><span><span><span><span><span>弃用/删除</span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></h2> 
<p><span><span><span style="color:#222222"><span><span><span><span><span><span><span><span><span><span><span><span style="background-color:#ffffff"><span><span><span>PHP 7 包已移至测试，因为它很快将 EOL ，取而代之的是 PHP 8</span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></p>
                                        </div>
                                      
</div>
            