
---
title: 'Linux 5.13确认将引入WWAN框架'
categories: 
 - 新媒体
 - cnBeta
 - 最新
headimg: 'https://static.cnbetacdn.com/article/2021/0417/1b002b49551fee7.jpg'
author: cnBeta
comments: false
date: Sat, 17 Apr 2021 11:33:44 GMT
thumbnail: 'https://static.cnbetacdn.com/article/2021/0417/1b002b49551fee7.jpg'
---

<div>   
<strong>周五登陆Linux网络子系统“Net-Next”分支的是开发已久的WWAN子系统/框架，</strong>这一框架现在正排队等待着与即将到来的Linux 5.13合并窗口，这套代码是一个无线广域网（WWAN）框架，主要用来处理不同厂商的无线广域网硬件带来的复杂性和异构性。<br>
<p><strong>了解更多：</strong></p><p><a href="https://git.kernel.org/pub/scm/linux/kernel/git/netdev/net-next.git/commit/?id=fa588eba632df14d296436995e6bbea0c146ae77" _src="https://git.kernel.org/pub/scm/linux/kernel/git/netdev/net-next.git/commit/?id=fa588eba632df14d296436995e6bbea0c146ae77" target="_blank">https://git.kernel.org/pub/scm/linux/kernel/git/netdev/net-next.git/commit/?id=fa588eba632df14d296436995e6bbea0c146ae77</a></p><p><a href="https://git.kernel.org/pub/scm/linux/kernel/git/netdev/net-next.git/commit/?id=9a44c1cc63887627284ae232a9626a9f1cd066fc" _src="https://git.kernel.org/pub/scm/linux/kernel/git/netdev/net-next.git/commit/?id=9a44c1cc63887627284ae232a9626a9f1cd066fc" target="_blank">https://git.kernel.org/pub/scm/linux/kernel/git/netdev/net-next.git/commit/?id=9a44c1cc63887627284ae232a9626a9f1cd066fc</a><br></p><p>作为主创人员，Linaro带头进行了这项工作，这个内核补丁在内核的网络区域内引入了新的WWAN子系统，并进一步阐述了Linux实现无线WAN支持中的一些挑战。</p><p>WWAN框架的初始组成部分是一个高通控制驱动，用于通过这个框架暴露不同的调制解调器控制协议/端口，然后可以被ModemManager等用户空间软件所利用。</p><p><img src="https://static.cnbetacdn.com/article/2021/0417/1b002b49551fee7.jpg" title alt="Sierra-Wireless-Em9190-5g-Modules.jpg" referrerpolicy="no-referrer"></p>   
</div>
            