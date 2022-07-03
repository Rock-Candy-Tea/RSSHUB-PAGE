
---
title: '微软警告：高危蠕虫"树莓知更鸟"感染了大量的Windows企业网络'
categories: 
 - 新媒体
 - cnBeta
 - 最新
headimg: 'https://static.cnbetacdn.com/article/2022/0703/8dc8cf1ffbe6f49.png'
author: cnBeta
comments: false
date: Sun, 03 Jul 2022 06:23:38 GMT
thumbnail: 'https://static.cnbetacdn.com/article/2022/0703/8dc8cf1ffbe6f49.png'
---

<div>   
在网络安全领域，善与恶之间的斗争是一场持久战。我们经常听到恶意行为者利用新的漏洞，以及在被动和主动的基础上对它们建立的防御措施。<strong>现在，微软已经发布了关于一种高风险蠕虫的私人建议，这种蠕虫正在感染数百个Windows企业网络。</strong><br>
 <p><img src="https://static.cnbetacdn.com/article/2022/0703/8dc8cf1ffbe6f49.png" title alt="图片.png" referrerpolicy="no-referrer"></p><p>被称为"树莓知更鸟"(Raspberry Robin)的恶意软件是通过含有一个经过特殊处理后的.lnk快捷方式文件的受感染USB设备传播的。一旦用户点击这个文件，该蠕虫就会通过命令提示程序创建一个<a data-link="1" href="https://c.duomai.com/track.php?site_id=242986&euid=&t=https://msi-pc.jd.com/" target="_blank">MSI</a>exec.exe进程，并启动另一个恶意文件。然后，它通过一个简短的URL与命令和控制服务器进行通信。如果连接成功，它就会下载并安装一堆其他的恶意DLLs，然后试图与Tor节点进行通信。</p><p>值得注意的是，树莓知更鸟并不是一个新的恶意软件。它在2021年首次被多个安全专家发现，<a data-link="1" href="https://c.duomai.com/track.php?site_id=242986&euid=&t=https://www.microsoftstore.com.cn/" target="_blank">微软</a>甚至在2019年就看到了它被使用的证据。</p><p><a href="https://static.cnbetacdn.com/article/2022/0703/6e613a26ec4a15b.png" target="_blank"><img src="https://static.cnbetacdn.com/thumb/article/2022/0703/6e613a26ec4a15b.png" title alt="图片.png" referrerpolicy="no-referrer"></a></p><p>据Bleeping Computer报道，微软现在正在私下通知Defender for Endpoint的企业用户关于Raspberry Robin带来的潜在危险。它还指出，它已经在多个部门的数百个<a data-link="1" href="https://microsoft.pvxt.net/x9Vg1" target="_blank">Windows</a>网络中发现了这种蠕虫。</p><p>尽管如此，非常有趣的是，虽然受感染的机器正在与Tor网络进行通信，但Raspberry Robin背后的威胁者还没有利用这个漏洞来获取敏感信息或部署勒索软件。考虑到他们下载的初始有效载荷可以通过滥用Windows工具来绕过用户账户控制（UAC），他们可以轻松做到这一点。</p><p><a href="https://static.cnbetacdn.com/article/2022/0703/90e9d6213d50a03.png" target="_blank"><img src="https://static.cnbetacdn.com/thumb/article/2022/0703/90e9d6213d50a03.png" title alt="图片.png" referrerpolicy="no-referrer"></a></p><p>因此，目前还不知道哪个威胁集团在利用树莓知更鸟，以及他们的最终目标是什么。然而，考虑到这种威胁升级的可能性，以及它的传播速度相当快的事实，微软暂时将其标记为高风险活动。</p>   
</div>
            