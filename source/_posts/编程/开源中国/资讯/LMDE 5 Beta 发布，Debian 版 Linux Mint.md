
---
title: 'LMDE 5 Beta 发布，Debian 版 Linux Mint'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://oscimg.oschina.net/oscnet/up-75f3faa6c40ca45006d9ef88b883c7ab1c7.png'
author: 开源中国
comments: false
date: Wed, 02 Mar 2022 07:28:00 GMT
thumbnail: 'https://oscimg.oschina.net/oscnet/up-75f3faa6c40ca45006d9ef88b883c7ab1c7.png'
---

<div>   
<div class="content">
                                                                                            <p>LMDE 是一个 Linux Mint 项目，代表 "Linux Mint Debian Edition"。它的目标是确保 Linux Mint（基于 Ubuntu） 能够在 Debian 的基础上也继续提供相同的用户体验，并保证 Linux Mint 开发的软件在 Ubuntu 之外也能兼容。</p> 
<p>一句话总结就是，LMDE 的目标是尽可能地与 Linux Mint 相似，但不使用 Ubuntu，其软件包基础是由 Debian 提供的。</p> 
<p><img alt height="451" src="https://oscimg.oschina.net/oscnet/up-75f3faa6c40ca45006d9ef88b883c7ab1c7.png" width="700" referrerpolicy="no-referrer"></p> 
<p>Linux Mint 近日发布了 LMDE 5 "Elsie" 的 Beta 版本，官方目前公布的信息不算多，并表示<strong>更多内容将在稳定版公布后发布</strong>。</p> 
<ul> 
 <li>LMDE 5 基于 Debian 11 Bullseye</li> 
 <li>使用 Linux 5.10 内核</li> 
 <li>Cinnamon 5.2 桌面环境</li> 
</ul> 
<h3>系统要求：</h3> 
<ul> 
 <li>2GB 内存（建议使用 4GB 的内存）</li> 
 <li>20GB 的磁盘空间（推荐 100GB）</li> 
</ul> 
<h3>已知问题：</h3> 
<ul> 
 <li> <p>Yumi multiboot</p> <p>LMDE 的 ISO 和 Live 安装程序使用的结构与其他发行版使用的不同，因此不要在 LMDE 中使用 Yumi 或 multiboot 技术，会导致无法正常安装</p> </li> 
 <li> <p>锁定的 root 账号</p> <p>默认情况下，root 账户是被锁定的。要使用恢复控制台（来自 Grub 菜单）或以 root 身份登录，你首先需要给 root 一个新密码。</p> </li> 
 <li> <p>声音和麦克风问题</p> <p>麦克风或声音输出存在问题，需要用户安装 "pavucontrol"。</p> </li> 
 <li> <p>KDE 应用程序的问题</p> <p>如果遇到 KDE 应用程序（Okular、Gwenview 和 KStars 等）的问题，请运行以下命令。</p> <p><code>apt install kdelibs-bin kdelibs5-data kdelibs5-plugins</code></p> </li> 
</ul> 
<h3>下载地址：</h3> 
<ul> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fmirror.sjtu.edu.cn%2Flinuxmint-cd%2Ftesting%2Flmde-5-cinnamon-64bit-beta.iso" target="_blank">链接</a></li> 
</ul> 
<p>更多详情可查看：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Flinuxmint.com%2Frel_elsie.php" target="_blank">https://linuxmint.com/rel_elsie.php</a></p>
                                        </div>
                                      
</div>
            