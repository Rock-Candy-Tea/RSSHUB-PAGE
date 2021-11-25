
---
title: 'Alpine Linux 3.15 发布，基于 Linux 5.15 内核'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=7765'
author: 开源中国
comments: false
date: Thu, 25 Nov 2021 07:39:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=7765'
---

<div>   
<div class="content">
                                                                    
                                                        <p>Alpine Linux 是一个面向安全的轻量级 Linux 发行版，该发行版以安全为理念，面向 x86 路由器、防火墙、虚拟专用网、IP 电话盒及服务器而设计。另外，不同于常见的 Linux 发行版，Alpine Linux 采用 <a href="https://www.oschina.net/action/GoToLink?url=http%3A%2F%2Fmusl-libc.org%2F">musl libc</a> 和 <a href="https://www.oschina.net/action/GoToLink?url=http%3A%2F%2Fbusybox.net%2F">busybox</a> 以减小系统的体积和运行时资源消耗。在保持瘦身的同时，Alpine Linux 还提供了自己的包管理工具 apk，可以在其网站上<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fpkgs.alpinelinux.org%2Fpackages">查询软件包</a>，或直接通过 apk 命令进行查询和安装。</p> 
<p>Alpine Linux 3.15 更新内容如下：</p> 
<h3><strong>HIGHLIGHTS</strong>：</h3> 
<ul> 
 <li>在安装程序中支持磁盘加密</li> 
 <li>通过 AKMS 支持树外的内核模块</li> 
 <li>在 x86_64 上初步支持 UEFI 安全启动</li> 
 <li>Linux Kernels 5.15 (LTS)</li> 
 <li>llvm 12</li> 
 <li>nodejs 16.13 (LTS) / nodejs-current 17.0</li> 
 <li>postgresql 14</li> 
 <li>openldap 2.6</li> 
 <li>ruby 3.0</li> 
 <li>rust 1.56</li> 
 <li>openjdk 17</li> 
 <li>kea 2.0</li> 
 <li>xorg-server 21.1</li> 
 <li>GNOME 41</li> 
 <li>KDE Plasma 5.23 / KDE Applications 21.08 / Plasma Mobile Gear 21.10</li> 
</ul> 
<h3><strong>SIGNIFICANT CHANGES</strong></h3> 
<ul> 
 <li>内核模块现在是用 gzip 压缩的</li> 
 <li>内核中的 Framebuffer 驱动已被禁用，由 simpledrm 取代</li> 
 <li>由于缺乏上游支持，qt5-qtwebkit 及相关软件包已被删除</li> 
 <li>MIPS64 移植已经停止了。该架构已经终止， 将不会有新的版本</li> 
</ul> 
<h3><strong>DEPRECATION NOTES</strong></h3> 
<ul> 
 <li><code>sudo</code> 将在 Alpine Linux 3.16 中被移至 community。建议替换为 <code>doas</code>，它在 main 中可用。</li> 
 <li><code>php7</code> 正在被淘汰，作为最后一个版本，7.4 将只剩下一年的安全支持。 变化</li> 
</ul> 
<p>更多详情可查看：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Falpinelinux.org%2Fposts%2FAlpine-3.15.0-released.html" target="_blank">https://alpinelinux.org/posts/Alpine-3.15.0-released.html</a></p>
                                        </div>
                                      
</div>
            