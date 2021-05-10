
---
title: 'PuTTY 0.75 发布，SSH_Telnet 程序'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=7612'
author: 开源中国
comments: false
date: Sun, 09 May 2021 23:21:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=7612'
---

<div>   
<div class="content">
                                                                                            <p><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.chiark.greenend.org.uk%2F%7Esgtatham%2Fputty%2F" target="_blank">PuTTY 0.75 现已发布</a>。PuTTY 是一款集成虚拟终端、系统控制台和网络文件传输为一体的自由开源程序。它支持多种网络协议，包括 SCP，SSH，Telnet，rlogin 和原始的套接字连接，它也可以连接到串行端口。其软件名字“PuTTY”并没有特殊含义。</p> 
<p>PuTTY 0.75 中包含的一些主要新功能有：Pageant 中的延迟密钥解密、更安全的 SSH 密钥指纹和 SSH 私钥文件，以及一些用于特殊目的的新网络协议。此外，该版本还包括了对 Windows 终端模拟器中的 DoS 漏洞的修复，该漏洞允许恶意的服务器锁定所有在客户端运行的 GUI Windows 应用程序。</p> 
<p>具体更新内容如下：</p> 
<ul> 
 <li>安全修复：在 Windows上，服务器可以通过告诉 PuTTY 窗口反复高速更改其标题来对整个 Windows GUI 进行 DoS。</li> 
 <li>Pageant 现在支持加载仍加密的密钥，并在第一次使用时通过提示口令来解密它。</li> 
 <li>将默认的 SSH 密钥指纹格式升级为 OpenSSH-style SHA-256。</li> 
 <li>将私钥文件格式升级为 PPK3，改进了 passphrase hashing，不再使用 SHA-1。</li> 
 <li>终端现在支持 ESC [ 9 m 用于删除线文本。</li> 
 <li>新协议：用于已经安全的 IPC 通道的裸露 ssh 连接层，以及用于与非常老的系统（例如 PDP-10）进行通信的 SUPDUP。</li> 
 <li>PuTTYgen 现在支持用于 RSA 和 DSA 的 alternative provable-prime generation algorithm。</li> 
 <li>Unix 工具现在可以直接连接到 Unix-domain socket。</li> 
</ul> 
<p>更新日志：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.chiark.greenend.org.uk%2F%7Esgtatham%2Fputty%2Fchanges.html" target="_blank">https://www.chiark.greenend.org.uk/~sgtatham/putty/changes.html</a></p> 
<p>下载地址：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.chiark.greenend.org.uk%2F%7Esgtatham%2Fputty%2Flatest.html" target="_blank">https://www.chiark.greenend.org.uk/~sgtatham/putty/latest.html</a> </p>
                                        </div>
                                      
</div>
            