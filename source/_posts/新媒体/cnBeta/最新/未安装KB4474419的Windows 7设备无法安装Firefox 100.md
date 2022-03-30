
---
title: '未安装KB4474419的Windows 7设备无法安装Firefox 100'
categories: 
 - 新媒体
 - cnBeta
 - 最新
headimg: 'https://static.cnbetacdn.com/article/2022/0330/8b0aacbea2701ab.webp'
author: cnBeta
comments: false
date: Wed, 30 Mar 2022 06:34:08 GMT
thumbnail: 'https://static.cnbetacdn.com/article/2022/0330/8b0aacbea2701ab.webp'
---

<div>   
<strong>从 Firefox 100 开始，Windows 7 SP1 用户必须要安装 KB4474419 更新之后才可安装该浏览器，否则会提示安装失败。</strong>这是因为 Mozilla 对 Firefox for Windows 安装程序的签名是 SHA2-256 摘要，而不是 SHA-1。<br>
 <p style="text-align:center"><img src="https://static.cnbetacdn.com/article/2022/0330/8b0aacbea2701ab.webp" alt="8ecsfbvv.webp" referrerpolicy="no-referrer"></p><p style="text-align: left;">一些 <a data-link="1" href="https://microsoft.pvxt.net/x9Vg1" target="_blank">Windows</a> 更新，特别是安全更新是相当强制性的。如果用户不在他们的设备上安装它们，Windows 可能无法正常工作，你也无法安装某些应用程序。在传统的 Windows 操作系统上发布的 Firefox 100 就是这样的情况。</p><p style="text-align: left;">早在 2019 年，<a data-link="1" href="https://c.duomai.com/track.php?site_id=242986&euid=&t=https://www.microsoftstore.com.cn/" target="_blank">微软</a>放弃了 Sha-1，并通过 KB4474419 为 Windows 7 SP1 和 Windows Server 2008 R2 SP1，以及 Windows Server 2008 SP2 引入了 SHA2-代码签名支持。</p><p style="text-align: left;">如果你没有安装强制更新，Firefox浏览器的安装可能会失败，你可能会收到像下面这样的错误或其他错误。</p><p style="text-align: left;">Mozilla 指出：“从这个版本开始，Windows版Firefox浏览器的安装程序使用SHA-256摘要签名，而不是SHA-1。在运行微软Windows 7操作系统的计算机上成功安装KB4474419更新是必需的”。</p>   
</div>
            