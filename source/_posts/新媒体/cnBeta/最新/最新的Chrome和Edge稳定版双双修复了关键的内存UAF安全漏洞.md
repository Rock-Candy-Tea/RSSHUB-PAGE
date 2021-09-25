
---
title: '最新的Chrome和Edge稳定版双双修复了关键的内存UAF安全漏洞'
categories: 
 - 新媒体
 - cnBeta
 - 最新
headimg: 'https://static.cnbetacdn.com/thumb/article/2021/0925/d4bc1a888130bd9.jpg'
author: cnBeta
comments: false
date: Sat, 25 Sep 2021 07:46:53 GMT
thumbnail: 'https://static.cnbetacdn.com/thumb/article/2021/0925/d4bc1a888130bd9.jpg'
---

<div>   
微软和Google都发布了新的稳定通道版本，修补了一个基于Chromium的Use-After-Free（UAF）的关键漏洞，该漏洞可能允许攻击者在成功利用后执行任意代码。Edge的版本是94.0.992.31，而Google浏览器的版本是94.0.4606.61。新的构建版本是基于Chromium版本94.0.4606.54。<br>
<p><a href="https://static.cnbetacdn.com/article/2021/0925/d4bc1a888130bd9.jpg" target="_blank"><img src="https://static.cnbetacdn.com/thumb/article/2021/0925/d4bc1a888130bd9.jpg" title alt="1632236565_google_chrome_94.jpg" referrerpolicy="no-referrer"></a></p><p>该漏洞的ID为"CVE-2021-37973"，该漏洞是由Google安全工程师Clément Lecigne在Sergei Glazunov和Mark Brand等人的协助下发现的。</p><p>Google表示在其Portals门户功能中发现了UAF漏洞，根据CERT的说法，"远程攻击者可以利用这个漏洞执行任意代码或导致系统出现拒绝服务情况"。当程序或应用在释放动态内存部分后未能正确管理内存指针，这反过来会导致攻击者执行代码。</p><p>指针存储了与应用程序正在使用的内存的某个地址有关的数据。但动态内存会不断被刷新和重新分配，供不同的应用程序使用。然而，如果该指针在其对应的内存空间被释放或未分配时没有被设置为空，攻击者就可以成功地利用该指针数据获得对同一内存部分的访问，从而传递任意的恶意代码。这就是为什么该漏洞被命名为Use-After-Free。</p><p>然而，<a href="https://docs.microsoft.com/en-us/DeployEdge/microsoft-edge-relnotes-security">Edge 94.0.992.31</a>以及<a href="https://chromereleases.googleblog.com/2021/09/stable-channel-update-for-desktop_24.html">Chrome 94.0.4606.61</a>都已经修补了这个基于内存的关键安全漏洞，建议用户将其浏览器更新到这些版本。</p><div class="article-relation"><p><strong>相关文章:</strong></p><p><a href="https://www.cnbeta.com/articles/tech/1183037.htm" target="_blank">Chrome安全团队希望将指针错误消灭在编译阶段</a></p></div>   
</div>
            