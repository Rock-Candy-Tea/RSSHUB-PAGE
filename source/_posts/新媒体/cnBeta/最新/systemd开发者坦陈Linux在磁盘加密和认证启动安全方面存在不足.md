
---
title: 'systemd开发者坦陈Linux在磁盘加密和认证启动安全方面存在不足'
categories: 
 - 新媒体
 - cnBeta
 - 最新
headimg: 'https://static.cnbetacdn.com/thumb/article/2021/0923/299cc1110963e82.png'
author: cnBeta
comments: false
date: Thu, 23 Sep 2021 13:03:08 GMT
thumbnail: 'https://static.cnbetacdn.com/thumb/article/2021/0923/299cc1110963e82.png'
---

<div>   
目前，大多数Linux发行版在全盘加密和认证启动方面都没有提供足够的安全性。知名的Linux开发者Lennart Poettering甚至认为，你当前的的数据"如果存储在ChromeOS、Android、Windows或macOS设备上可能更安全。"<br>
<p>首席systemd开发者Lennart Poettering今天围绕Linux上的认证启动和磁盘加密状况写了一篇长篇博文。虽然许多Linux发行版提供全盘加密，提供UEFI SecureBoot，并开始接受TPM，但许多技术还没有发挥其最佳潜力，特别是在购买设备后没有经过人工安全性加强的的默认情况下。</p><p>Lennart对这种情况的简短总结是：</p><blockquote><p>Linux支持全盘加密（FDE）和诸如UEFI安全启动和TPM的技术已经有很长一段时间了。然而，大多数发行版对它们的设置方式并不像它们应该有的那样安全，而且在某些方面相当坦率地说是很奇怪。事实上，现在，如果你的数据存储在目前的ChromeOS、Android、<a data-link="1" href="https://microsoft.pvxt.net/x9Vg1" target="_blank">Windows</a>或MacOS设备上，可能比存储在典型的Linux发行版上更安全。</p></blockquote><p>在他的博文中，他概述了目前的技术，手头的问题，以及在改善认证和提供更好的安全方面需要改进的地方。</p><p><a href="https://static.cnbetacdn.com/article/2021/0923/299cc1110963e82.png" target="_blank"><img src="https://static.cnbetacdn.com/thumb/article/2021/0923/299cc1110963e82.png" title alt="图片.png" referrerpolicy="no-referrer"></a></p><p><a href="https://static.cnbetacdn.com/article/2021/0923/ca12e170549473f.png" target="_blank"><img src="https://static.cnbetacdn.com/thumb/article/2021/0923/ca12e170549473f.png" title alt="图片.png" referrerpolicy="no-referrer"></a></p><p>为了更好地提高安全性，有一些Linux内核拉动请求正在等待systemd的处理，所以这项工作仍然需要时间向上游推进，但这也将取决于Linux发行商在可用时也开始使用这些功能。</p><p>您可以阅读Lennart的博客，了解所有有趣的技术细节和当前Linux还存在的亟待改进的缺点：</p><p><a href="http://0pointer.net/blog/authenticated-boot-and-disk-encryption-on-linux.html" _src="http://0pointer.net/blog/authenticated-boot-and-disk-encryption-on-linux.html" target="_blank">http://0pointer.net/blog/authenticated-boot-and-disk-encryption-on-linux.html</a><br></p>   
</div>
            