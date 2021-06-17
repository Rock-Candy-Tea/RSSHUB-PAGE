
---
title: 'Paint 3D曝出远程代码执行漏洞 微软已发补丁修复'
categories: 
 - 新媒体
 - cnBeta
 - 最新
headimg: 'https://static.cnbetacdn.com/thumb/article/2021/0617/f3720c84e1e5044.jpg'
author: cnBeta
comments: false
date: Wed, 16 Jun 2021 23:56:24 GMT
thumbnail: 'https://static.cnbetacdn.com/thumb/article/2021/0617/f3720c84e1e5044.jpg'
---

<div>   
<strong>微软的 Paint 3D 应用程序自推出以来并不受消费者的欢迎，而且 ZDI 研究人员还发现这款 3D 建模软件存在远程代码执行漏洞，可能会对你的系统健康产生负面影响。</strong>该漏洞是通过搜索发现，需要用户加载一个被破坏的文件。在本月的补丁星期二活动日中已经修复了这个问题。<br>
 <p style="text-align:center"><a href="https://static.cnbetacdn.com/article/2021/0617/f3720c84e1e5044.jpg" target="_blank"><img src="https://static.cnbetacdn.com/thumb/article/2021/0617/f3720c84e1e5044.jpg" referrerpolicy="no-referrer"></a></p><p style="text-align:center"><a href="https://static.cnbetacdn.com/article/2021/0617/d23669827c7b688.jpg" target="_blank"><img src="https://static.cnbetacdn.com/thumb/article/2021/0617/d23669827c7b688.jpg" referrerpolicy="no-referrer"></a></p><p style="text-align: left;">该漏洞编号为 <a href="https://www.zerodayinitiative.com/advisories/ZDI-21-671/" target="_blank">CVE-2021-31946</a>，相关描述如下</p><blockquote style="text-align: left;"><p style="text-align: left;">Microsoft Paint 3D GLB File Parsing Out-Of-Bounds Read Remote Code Execution Vulnerability</p><p style="text-align: left;">该漏洞允许远程攻击者在受影响的Microsoft Paint 3D安装中执行任意代码。利用该漏洞需要用户互动，目标必须访问一个恶意网页或打开一个恶意文件。</p><p style="text-align: left;">具体的缺陷存在于 GLB 文件的解析过程中。该问题是由于缺乏对用户提供的数据的正确验证，这可能导致读取超过分配的数据结构的末端。攻击者可以利用这个漏洞，在当前进程的上下文中以低完整性执行代码。</p></blockquote><p style="text-align:center"><a href="https://static.cnbetacdn.com/article/2021/0617/360c86778c34910.jpg" target="_blank"><img src="https://static.cnbetacdn.com/thumb/article/2021/0617/360c86778c34910.jpg" referrerpolicy="no-referrer"></a></p><p style="text-align: left;">微软已经发布了该软件的更新，修复了这个问题，但<a data-link="1" href="https://microsoft.pvxt.net/x9Vg1" target="_blank">Windows</a> 11用户不必担心，因为该软件已经不再预装在该操作系统中。</p>   
</div>
            