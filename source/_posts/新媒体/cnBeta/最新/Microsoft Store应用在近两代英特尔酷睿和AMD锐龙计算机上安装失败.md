
---
title: 'Microsoft Store应用在近两代英特尔酷睿和AMD锐龙计算机上安装失败'
categories: 
 - 新媒体
 - cnBeta
 - 最新
headimg: 'https://static.cnbetacdn.com/thumb/article/2022/0520/376e55c82ba5ff5.png'
author: cnBeta
comments: false
date: Fri, 20 May 2022 06:30:11 GMT
thumbnail: 'https://static.cnbetacdn.com/thumb/article/2022/0520/376e55c82ba5ff5.png'
---

<div>   
Microsoft Store应用在英特尔第11、12代酷睿和AMD Ryzen 5000、6000计算机上安装失败。微软已经发布了一个重要的带外（OOB）更新，解决了一个导致应用程序从微软商店安装失败的问题，错误代码为"0xC002001B"。<br>
<p><a href="https://static.cnbetacdn.com/article/2022/0520/376e55c82ba5ff5.png" target="_blank"><img src="https://static.cnbetacdn.com/thumb/article/2022/0520/376e55c82ba5ff5.png" title alt="72caeaa2-069f-43f8-a752-7972f252c94d.png" referrerpolicy="no-referrer"></a></p><p>这个问题是在安装KB5011831 <a data-link="1" href="https://microsoft.pvxt.net/x9Vg1" target="_blank">Windows</a> 10版本后出现的。已经确定，这个问题困扰着现代<a data-link="1" href="https://c.duomai.com/track.php?site_id=242986&euid=&t=https://intel.jd.com/" target="_blank">英特尔</a>和<a data-link="1" href="https://c.duomai.com/track.php?site_id=242986&euid=&t=https://amd-cpu.jd.com/" target="_blank">AMD</a>的CPU系统，这些系统支持英特尔控制流执行技术（CET）或AMD同等的Shadow Stack技术。CET有助于缓解面向返回的编程（ROP）漏洞或面向CALL/JMP的编程（COP/JOP）漏洞。</p><p>受影响的CPU包括英特尔第11代 Tiger Lake 芯片，以及第12代 Alder Lake CPU。在AMD方面，Zen 3 锐龙 5000和最新的Zen 3+ Ryzen 6000系列CPU受到影响。</p><p>微软的公告说：</p><blockquote><p>安装KB5011831或以后的更新后，你可能会收到一个错误代码。0xC002001B，当试图从微软商店安装时，一些应用程序也可能无法打开。受影响的Windows设备使用支持控制流执行技术（CET）的处理器（CPU），如如11代及以后的英特尔酷睿处理器或更新的处理器和某些AMD处理器。这个问题已在带外更新KB5015020中得到解决。</p></blockquote><p>要下载修复这个问题的带外更新KB5015020，请到微软更新目录页面，点击这个链接直接到达：</p><p><a href="https://www.catalog.update.microsoft.com/Search.aspx?q=KB5015020" _src="https://www.catalog.update.microsoft.com/Search.aspx?q=KB5015020" target="_blank">https://www.catalog.update.microsoft.com/Search.aspx?q=KB5015020</a><br></p>   
</div>
            