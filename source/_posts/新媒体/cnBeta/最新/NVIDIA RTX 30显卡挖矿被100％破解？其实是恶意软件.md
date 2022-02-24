
---
title: 'NVIDIA RTX 30显卡挖矿被100％破解？其实是恶意软件'
categories: 
 - 新媒体
 - cnBeta
 - 最新
headimg: 'https://static.cnbetacdn.com/thumb/article/2022/0224/08a9ef504c20c12.png'
author: cnBeta
comments: false
date: Thu, 24 Feb 2022 07:36:12 GMT
thumbnail: 'https://static.cnbetacdn.com/thumb/article/2022/0224/08a9ef504c20c12.png'
---

<div>   
这两天，一个号称能破解NVIDIA RTX 30全系显卡挖矿限制的工具“RTX LHR v2 Unlocker”得到广泛关注，据说可以全自动破解、算力几乎翻番、不损坏硬件，甚至发生了<a class="f14_link" href="https://news.mydrivers.com/1/816/816552.htm" target="_blank">作者疑似跑路</a>的闹剧。那么，这个工具真的这么神？经过分析发现，这个破解工具，其实就是个病毒，或者说是个恶意软件。<br>
 <p><a href="https://img1.mydrivers.com/img/20220224/b6b66bca60d24da69f5bfed8f3f84045.png" style="text-align: -webkit-center;" target="_blank"></a><a target="_blank" href="https://static.cnbetacdn.com/article/2022/0224/08a9ef504c20c12.png"><img data-original="https://static.cnbetacdn.com/article/2022/0224/08a9ef504c20c12.png" src="https://static.cnbetacdn.com/thumb/article/2022/0224/08a9ef504c20c12.png" referrerpolicy="no-referrer"></a></p><p><strong>它的主执行文件LHRUnlocker Install.<a data-link="1" href="https://c.duomai.com/track.php?site_id=242986&euid=&t=https://msi-pc.jd.com/" target="_blank">MSI</a>不但起不到破解算力的作用，还会感染<a data-link="1" href="https://microsoft.pvxt.net/x9Vg1" target="_blank">Windows</a>命令行服务程序powershell.exe并绕过其执行策略，添加目录屏蔽Windows Defender安全服务，以挂起模式添加进程(疑似注入代码)，获取硬盘序列号等敏感信息，等等，并导致CPU占用率过高。</strong></p><p>目前来看，这个恶意软件的破坏力并不大，不会给用户系统造成致命伤害，但其威胁性还在进一步分析中，不排除有更多恶意行为。所以，对于破解类工具，一定要慎重，矿主们也不要欢呼雀跃了。</p><p><a href="https://img1.mydrivers.com/img/20220224/745389bd9cc24b4098d99712757e01c5.png" target="_blank"></a><a target="_blank" href="https://static.cnbetacdn.com/article/2022/0224/77a42eee3e3947a.png"><img data-original="https://static.cnbetacdn.com/article/2022/0224/77a42eee3e3947a.png" src="https://static.cnbetacdn.com/thumb/article/2022/0224/77a42eee3e3947a.png" referrerpolicy="no-referrer"></a></p><p><a href="https://img1.mydrivers.com/img/20220224/32d8ce23eb3c4df48591cc98c66f3289.jpg" target="_blank"></a><a target="_blank" href="https://static.cnbetacdn.com/article/2022/0224/1780511ad3c849c.jpg"><img data-original="https://static.cnbetacdn.com/article/2022/0224/1780511ad3c849c.jpg" src="https://static.cnbetacdn.com/thumb/article/2022/0224/1780511ad3c849c.jpg" referrerpolicy="no-referrer"></a></p>   
</div>
            