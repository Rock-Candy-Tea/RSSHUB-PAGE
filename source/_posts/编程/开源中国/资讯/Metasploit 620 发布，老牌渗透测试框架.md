
---
title: 'Metasploit 6.2.0 发布，老牌渗透测试框架'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=9397'
author: 开源中国
comments: false
date: Wed, 15 Jun 2022 07:01:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=9397'
---

<div>   
<div class="content">
                                                                                            <p>Metasploit 项目是一个提供安全漏洞信息服务的计算机安全项目，可以协助安全工程师进行渗透测试 (penetration testing) 及入侵检测系统签名开发。</p> 
<p>目前 Metasploit 6.2.0 版本<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.rapid7.com%2Fblog%2Fpost%2F2022%2F06%2F09%2Fannouncing-metasploit-6-2%2F" target="_blank">发布</a>了，此版本包含 138 个新模块、148 个新改进/功能和 156 个错误修复。其中有 6 个较重要的新功能，增强了现有的漏洞利用模块，添加了协议支持，并提供了额外的调试机制。</p> 
<p><strong>Capture 插件</strong></p> 
<p>引入了一个新的“Capture”插件，它提供了一种更简化的在网络上窃取凭据的方法。启动插件时将自动启动 13 个不同的服务，四个以 SSL 模式运行，以捕获网络上的凭据。</p> 
<p><strong>SMB v3 服务器支持</strong> </p> 
<p>Metasploit 扩展了对 SMB v3 的支持，可以快速启动共享只读文件夹的 SMB v3 服务器。</p> 
<p><strong>增强的 smb_relay 支持</strong></p> 
<p><strong>smb_relay</strong> 模块已支持通过 SMB 版本 2 和 3 进行中继。该模块还可以配置为在一个会话中以多个设备为目标，在目标之间智能循环。</p> 
<p><strong>改进的旋转/NATed 服务支持</strong></p> 
<p>Metasploit 向提供侦听服务（如 HTTP、FTP、LDAP 等）的库添加了功能，允许它们绑定到独立于普通 IP 地址和端口组合的显式 IP 地址和端口组合。</p> 
<p><strong>调试 Meterpreter 会话</strong></p> 
<p>可以通过记录 msfconsole 和 Meterpreter 之间的网络请求和响应（TLV 数据包），或生成自定义 Meterpreter 调试版本来调试 Meterpreter 会话。</p> 
<p style="margin-left:0px"><strong>本地漏洞利用工具改进</strong> </p> 
<p style="margin-left:0px">为 <code>local_exploit_suggester</code>模块修复 Bug 并改进用户界面。该模块将启动多个 Metasploit 模块，以尝试在目标主机上获得本地权限提升。</p> 
<p> </p> 
<p>更多内容可查看<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.rapid7.com%2Fblog%2Fpost%2F2022%2F06%2F09%2Fannouncing-metasploit-6-2%2F" target="_blank">更新公告博客</a>。</p>
                                        </div>
                                      
</div>
            