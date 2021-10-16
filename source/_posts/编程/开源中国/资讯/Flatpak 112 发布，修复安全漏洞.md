
---
title: 'Flatpak 1.12 发布，修复安全漏洞'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=7275'
author: 开源中国
comments: false
date: Sat, 16 Oct 2021 08:06:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=7275'
---

<div>   
<div class="content">
                                                                    
                                                        <p>Flatpak 1.12 和 1.10.4 已发布。</p> 
<p>Flatpak 1.10.4 修复了入口代码 (portal code) 中的安全漏洞，由于一些新的 Linux 内核系统调用没有被 SECCOMP 规则阻止，应用程序可能会创建子沙箱来混淆入口的沙箱验证机制。</p> 
<p>漏洞披露<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fflatpak%2Fflatpak%2Fsecurity%2Fadvisories%2FGHSA-67h7-w3jq-vh4q" target="_blank">解释称</a>：“一位匿名记者发现，可以直接访问 AF_UNIX 套接字的 Flatpak 应用程序（例如 Wayland、Pipewire 或 pipewire-pulse 使用的套接字），可以欺骗入口和其他主机操作系统服务，将 Flatpak 应用程序视为普通的非沙盒主机-OS 进程，通过使用最近未被 Flatpak 的拒绝列表 seccomp 过滤器阻止的与挂载相关的系统调用来操纵 VFS，以替换精心制作的 /.flatpak-info 或使该文件完全消失。“</p> 
<p>Flatpak 1.12 作为该系列的最新稳定版，值得关注的更新是对子沙盒的更好控制——主要被应用于 Steam Flatpak。</p> 
<p><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fflatpak%2Fflatpak%2Freleases%2Ftag%2F1.12.0" target="_blank">详情查看 release notes</a>。</p>
                                        </div>
                                      
</div>
            