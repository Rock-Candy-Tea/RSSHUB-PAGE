
---
title: 'Nmap 7.92 发布，网络安全审计工具'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=3833'
author: 开源中国
comments: false
date: Mon, 09 Aug 2021 06:57:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=3833'
---

<div>   
<div class="content">
                                                                                            <p>Nmap 7.92 现已发布。Nmap 是一个网络连接端扫描软件，用来扫描网上电脑开放的网络连接端。此次更新包括数十个优化、加强和 bug 修复。</p> 
<p><strong>主要更新内容</strong></p> 
<ul> 
 <li>将 Npcap（Windows 原始数据包捕获和传输驱动程序）从 1.00 版升级到最新的 1.50 版</li> 
 <li>由于 Npcap 1.50 升级，Nmap 现在可以在 Windows ARM 架构上运行</li> 
 <li>将 Windows 版本要求更新为 Visual Studio 2019、Windows 10 SDK 和 UCRT</li> 
 <li>新的 Nmap 选项：unique 将防止 Nmap 扫描同一个 IP 地址两次，当不同的名称解析为相同的地址时会发生这种情况</li> 
 <li>TLS 1.3 现在被大多数与其相关的脚本支持，例如 ssl-enum-ciphers。某些功能（如 ssl 隧道连接和证书解析）需要 OpenSSL 1.1.1 或更高版本才能完全支持 </li> 
 <li>添加了 3 个 NSE 脚本，使总数达到 604 个</li> 
 <li>将 OpenSSL 升级到版本 1.1.1k。这解决了一些不会以实质性方式影响 Nmap 的 CVE</li> 
 <li>如果 excludefile 列出的 CIDR 范围包含较早的较小 CIDR 范围，则该地址集匹配中会排除所有目标</li> 
 <li>防止 ssl-* NSE 脚本探测从版本扫描中排除的端口，通常是 9100-9107，因为 JetDirect 将打印发送到这些端口的任何内容</li> 
 <li>当无法找到到目标的可用路由时，Nmap 不再产生 “无法将源地址转换为表示格式” 的消息</li> 
 <li>如果连接数超过 FD_SETSIZE，则使用 FD_* 宏的安全检查版本提前中止</li> 
 <li>通过 SOCKS4/SOCKS5 代理的连接，在连接建立后会间歇性地丢掉服务器发送的数据</li> 
</ul> 
<p>详情请查看<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fseclists.org%2Fnmap-announce%2F2021%2F3" target="_blank">更新公告</a>。</p>
                                        </div>
                                      
</div>
            