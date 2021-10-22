
---
title: '网络安全专家发现经微软WHQL认证的FiveSys驱动实际上是款恶意程序'
categories: 
 - 新媒体
 - cnBeta
 - 最新
headimg: 'https://static.cnbetacdn.com/thumb/article/2021/1022/5872216c8f121e9.jpg'
author: cnBeta
comments: false
date: Fri, 22 Oct 2021 07:47:47 GMT
thumbnail: 'https://static.cnbetacdn.com/thumb/article/2021/1022/5872216c8f121e9.jpg'
---

<div>   
<strong>Bitdefender 的网络安全专家近日发现了一款名为“FiveSys”的新恶意程序，它是一个 rootkit，实际上是由微软自己进行数字签名的。</strong>FiveSys 恶意驱动程序带有 Windows 硬件质量实验室（WHQL）认证，该认证由微软通过 Windows 硬件兼容计划（WHCP）对其各合作厂商送来的驱动程序包进行仔细核查后提供。<br>
 <p style="text-align:center"><a href="https://static.cnbetacdn.com/article/2021/1022/5872216c8f121e9.jpg" target="_blank"><img src="https://static.cnbetacdn.com/thumb/article/2021/1022/5872216c8f121e9.jpg" alt="0v80u3aa.jpg" referrerpolicy="no-referrer"></a></p><p style="text-align: left;">下面，Bitdefender 解释了 FiveSys rootkit 存在的原因以及它的功能。</p><blockquote style="text-align: left;"><p style="text-align: left;">rootkit 的目的很简单：它的目的是通过一个自定义的代理来重定向受感染机器的互联网流量，这个代理是从一个内置的 300 个域名列表中提取的。这种重定向对 HTTP 和 HTTPS 都有效；rootkit 为 HTTPS 重定向工作安装了一个自定义的根证书。这样一来，浏览器就不会对代理服务器的未知身份发出警告。</p><p style="text-align: left;">除了重定向互联网流量外，该rootkit还阻止其他恶意软件编写组的驱动程序的加载，因为他们可能试图限制竞争对手的威胁者进入被破坏的系统。</p></blockquote><p style="text-align: left;">据观察，到目前为止，FiveSys 的传播只限于中国，这可能表明威胁者主要对该地区感兴趣。在其他关键特征方面，相关白皮书还提到，该根包阻止注册表的修改，并试图阻止其竞争对手访问受感染的系统。</p>   
</div>
            