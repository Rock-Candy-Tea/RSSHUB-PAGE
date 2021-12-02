
---
title: 'NixOS 21.11（代号_豪猪_) 发布，大量新工具和软件升级'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=9718'
author: 开源中国
comments: false
date: Thu, 02 Dec 2021 07:14:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=9718'
---

<div>   
<div class="content">
                                                                    
                                                        <p style="color:#000000; margin-left:0; margin-right:0; text-align:start">NixOS 是独立开发的 GNU/Linux 发行版，旨在提高系统配置管理的最新水平。在 NixOS 中，整个操作系统，包括内核、应用程序、系统包和配置文件，都是由 Nix 包管理器构建的。该项目的最新版本是 NixOS 21.11，代号“豪猪”（<strong>Porcupine</strong>）其中包括以下亮点：</p> 
<h3 style="margin-left:.6em; margin-right:0; text-align:start">软件大升级</h3> 
<ul style="margin-left:0; margin-right:0"> 
 <li>默认的 Nix 版本仍为 2.3.16。<strong>由于非实验行为的回归，Nix 包管理器尚未更新到 2.4 版。</strong></li> 
 <li><code>iptables</code>现在使用<span> </span><code>nf_tables</code><span> </span>后端</li> 
 <li>PHP 默认为 PHP 8.0，从 7.4 更新</li> 
 <li>kops 默认为 1.21.1，它使用 containerd 作为默认运行时</li> 
 <li>Python3 默认为 Python 3.9，从 Python 3.8 更新</li> 
 <li>PostgreSQL 现在默认为主要版本 13</li> 
 <li>spark 默认为 spark 3，从 2 更新</li> 
 <li>bash 现在默认为主要版本 5。</li> 
 <li>Systemd 已更新到版本 249</li> 
 <li>Pantheon 桌面已更新至第 6 版</li> 
 <li><code>kubernetes-helm</code><span> </span>现在默认为 3.7.0</li> 
 <li>GNOME 已升级到 41</li> 
 <li>OpenSSH 已更新至 8.8p1 版本</li> 
 <li>ORY Kratos 更新至 0.8.0-alpha.3 版本</li> 
</ul> 
<h3 style="margin-left:.6em; margin-right:0; text-align:start">其他变更</h3> 
<ul style="margin-left:0; margin-right:0"> 
 <li>从<span> </span><code>all-packages.nix</code><span> </span>移除 Linux 内核包基础设施，将 .Linux 相关的函数和属性放在 pkgs.linuxKernel 属性集下面。</li> 
 <li>在 NixOS 虚拟机 (QEMU) 中，该<span> </span><code>virtualisation</code>模块已更新为新选项：</li> 
</ul> 
<ol style="margin-left:0; margin-right:0"> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fnixos.org%2Fmanual%2Fnixos%2Fstable%2Foptions.html%23opt-virtualisation.forwardPorts" target="_blank"><code>forwardPorts</code></a><span> </span>配置 IPv4 端口转发</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fnixos.org%2Fmanual%2Fnixos%2Fstable%2Foptions.html%23opt-virtualisation.sharedDirectories" target="_blank"><code>sharedDirectories</code></a><span> </span>设置共享主机目录</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fnixos.org%2Fmanual%2Fnixos%2Fstable%2Foptions.html%23opt-virtualisation.resolution" target="_blank"><code>resolution</code></a><span> </span>设置屏幕分辨率</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fnixos.org%2Fmanual%2Fnixos%2Fstable%2Foptions.html%23opt-virtualisation.useNixStoreImage" target="_blank"><code>useNixStoreImage</code></a><span> </span>为 Nix 存储使用磁盘映像，而不是 9P</li> 
 <li>此外，<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fnixos.org%2Fmanual%2Fnixos%2Fstable%2Foptions.html%23opt-virtualisation.msize" target="_blank"><code>msize</code></a><span> </span>9P 文件系统（包括 /nix/store 和所有共享目录）中的默认参数已增加到 16K ，以提高性能。</li> 
</ol> 
<ul style="margin-left:0; margin-right:0"> 
 <li>引入设置项<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fnixos.org%2Fmanual%2Fnixos%2Fstable%2Foptions.html%23opt-services.openssh.logLevel" target="_blank"><code>services.openssh.logLevel</code></a><span> </span>（<code>"VERBOSE"</code><span> </span>/<span> </span><code>"INFO"</code>.），让 NixOS 与上游其他 Linux 发行版保持一致，减少了由于暴力破解僵尸网络而导致的服务器日志垃圾邮件。</li> 
 <li>添加或修改布局时，<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fnixos.org%2Fmanual%2Fnixos%2Fstable%2Foptions.html%23opt-services.xserver.extraLayouts" target="_blank"><code>services.xserver.extraLayouts</code></a><span> </span>不再引起额外的重新构建。</li> 
 <li><code>claws-mail</code><span> </span>软件包现在引用了新的 GTK+ 3 发行版分支，主要版本： 4。</li> 
 <li>wordpress 模块提供了一个新的接口，允许通过<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fnixos.org%2Fmanual%2Fnixos%2Fstable%2Foptions.html%23opt-services.wordpress.webserver" target="_blank"><code>services.wordpress.webserver</code></a><span> </span>选项使用不同的网络服务器，</li> 
 <li>dokuwiki 模块提供了一个新的接口，允许通过<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fnixos.org%2Fmanual%2Fnixos%2Fstable%2Foptions.html%23opt-services.dokuwiki.webserver" target="_blank"><code>services.dokuwiki.webserver</code></a><span> </span>选项使用不同的网络服务器，</li> 
 <li><code>lib.formats.yaml</code><span> </span>的<span> </span><code>generate</code><span> </span>不再生成 JSON，而是使用更多特定于 YAML 的语法</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fnixos.org%2Fmanual%2Fnixos%2Fstable%2Foptions.html%23opt-networking.wireless.enable" target="_blank">networking.wireless</a><span> </span>模块（基于 wpa_supplicant）解决了一些问题：</li> 
</ul> 
<ol style="margin-left:0; margin-right:0"> 
 <li>启动时无线接口的自动搜寻变得可靠（issues<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FNixOS%2Fnixpkgs%2Fissues%2F101963" target="_blank">#101963</a><span> </span>,<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FNixOS%2Fnixpkgs%2Fissues%2F23196" target="_blank">#23196</a>）。</li> 
 <li>WPA3 和快速 BSS 转换 (802.11r) 现在默认为所有网络启用。</li> 
 <li>现在可以安全地处理像预共享密钥和密码之类的机密问题，无需将它们包含在可读的文件中（ /nix/store 下 的<span> </span><code>wpa_supplicant.conf</code>）。</li> 
 <li>声明多个接口，将启动独立的 wpa_supplicant 守护进程，每个接口都有一个守护进程(这些服务被命名为wpa_supplicant-wlan0、wpa_supplicant-wlan1等)。</li> 
 <li>生成的<span> </span><code>wpa_supplicant.conf</code><span> </span>文件已被格式化以便于阅读。</li> 
 <li>添加了新的  <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fnixos.org%2Fmanual%2Fnixos%2Fstable%2Foptions.html%23opt-networking.wireless.scanOnLowSignal" target="_blank">scanOnLowSignal</a><span> </span>选项，以促进接入点之间的快速漫游（默认启用）。</li> 
 <li>添加了新的<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fnixos.org%2Fmanual%2Fnixos%2Fstable%2Foptions.html%23opt-networking.wireless.networks._name_.authProtocols" target="_blank">networks.<name>.authProtocols</a><span> </span>选项，以更改连接到网络时使用的身份验证协议。</li> 
</ol> 
<ul style="margin-left:0; margin-right:0"> 
 <li>ipfs 现在默认不监听本地网络。</li> 
 <li><code>systemd.network</code><span> </span>模块已获得对 FooOverUDP 链接类型的支持</li> 
 <li><code>networking</code><span> </span>模块有一个新<span> </span><code>networking.fooOverUDP</code><span> </span>选项来配置 Foo-over-UDP 封装。</li> 
</ul> 
<p style="color:#000000; margin-left:0; margin-right:0; text-align:start">22.11 是一个大版本更新，除了上述更新项外还包含<strong>大量新的工具和服务</strong>，详尽信息可在<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fnixos.org%2Fmanual%2Fnixos%2Fstable%2Frelease-notes.html%23sec-release-21.11" target="_blank">官方公告中</a>查阅。</p> 
<p> </p>
                                        </div>
                                      
</div>
            