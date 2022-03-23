
---
title: 'LMDE 5'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://oscimg.oschina.net/oscnet/up-27afe2e7434eae1db44e1582ec72127fd07.png'
author: 开源中国
comments: false
date: Wed, 23 Mar 2022 07:11:00 GMT
thumbnail: 'https://oscimg.oschina.net/oscnet/up-27afe2e7434eae1db44e1582ec72127fd07.png'
---

<div>   
<div class="content">
                                                                    
                                                        <p>LMDE 5 已正式<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fblog.linuxmint.com%2F%3Fp%3D4287" target="_blank">发布</a>，代号"Elsie"。新版本基于 Debian 11 并使用了 Cinnamon 桌面环境。</p> 
<p><img alt src="https://oscimg.oschina.net/oscnet/up-27afe2e7434eae1db44e1582ec72127fd07.png" referrerpolicy="no-referrer"></p> 
<p>LMDE 是"<span style="background-color:#ffffff; color:#555555">Linux Mint Debian Edition</span>"的缩写，即基于 Debian 的 Linux Mint。其目标是在不使用 Ubuntu 的前提下，确保可提供与 Linux Mint 相同的体验，软件包仓库来自 Debian。LMDE 还有一个目标是开发兼容除 Ubuntu 之外的软件。</p> 
<p>下载地址：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fblog.linuxmint.com%2F%3Fp%3D4287" target="_blank">https://blog.linuxmint.com/?p=4287</a></p> 
<p>发布说明主要是描述了已知的问题：</p> 
<p style="margin-left:0; margin-right:0"><strong>Yumi multiboot</strong></p> 
<p style="margin-left:0; margin-right:0">LMDE 的 ISO 和 Live 安装程序使用的结构与其他发行版使用的不同，因此不要在 LMDE 中使用 Yumi 或 multiboot 技术，会导致无法正常安装</p> 
<p style="margin-left:0; margin-right:0"><strong>默认被锁定的 root 账号</strong></p> 
<p style="margin-left:0; margin-right:0">默认情况下，root 账户是被锁定的。要使用恢复控制台（来自 Grub 菜单）或以 root 身份登录，首先需要给 root 一个新密码。</p> 
<pre><code>sudo passwd root</code></pre> 
<p style="margin-left:0; margin-right:0"><strong>声音和麦克风问题</strong></p> 
<p style="margin-left:0; margin-right:0">麦克风或声音输出存在问题，需要用户安装 "pavucontrol"。</p> 
<p style="margin-left:0; margin-right:0"><strong>KDE 应用程序的问题</strong></p> 
<p style="margin-left:0; margin-right:0">如果遇到 KDE 应用程序（Okular、Gwenview 和 KStars 等）的问题，请运行以下命令。</p> 
<pre><code>apt install kdelibs-bin kdelibs5-data kdelibs5-plugins</code></pre> 
<p>此外，为了保证与非 PAE 处理器的兼容性，Linux Mint Debian 的 32 位版本默认带有 686 非 PAE 内核。要获得 PAE 支持，只需安装 686-PAE 内核并重新启动计算机。</p> 
<pre><code>apt update
apt install linux-headers-686-pae linux-image-686-pae</code></pre> 
<p><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Flinuxmint.com%2Frel_elsie.php" target="_blank">详情点此查看</a>。</p>
                                        </div>
                                      
</div>
            