
---
title: 'QNAP发布勒索软件安全警告：提醒自家NAS用户屏蔽公网访问'
categories: 
 - 新媒体
 - cnBeta
 - 最新
headimg: 'https://static.cnbetacdn.com/article/2022/0127/787695f0b2e71bf.jpg'
author: cnBeta
comments: false
date: Thu, 27 Jan 2022 03:29:28 GMT
thumbnail: 'https://static.cnbetacdn.com/article/2022/0127/787695f0b2e71bf.jpg'
---

<div>   
知名网络附加存储（NAS）硬件制造商威联通（QNAP），刚刚向用户发出了一则新的预警。<strong>受 DeadBolt 勒索软件肆虐的影响，该公司已建议自家客户采取积极行动，以避免将他们的 NAS 暴露于互联网上，不然可能遭遇未经授权的远程访问。</strong><br>
 <p><img src="https://static.cnbetacdn.com/article/2022/0127/787695f0b2e71bf.jpg" alt="0.jpg" referrerpolicy="no-referrer"></p><p style="text-align: center;">（来自：QNAP <a href="https://www.qnap.com/en/security-news/2022/take-immediate-actions-to-stop-your-nas-from-exposing-to-the-internet-and-fight-against-ransomware-together" target="_self">官网</a>）</p><p>通常情况下，NAS 设备更适合在局域网（LAN）环境中使用。而公告中提到的 BeadBolt 勒索软件，其本体也没有那么复杂。但若没有及时更新系统、或存在配置失误，就很容易遭到外网攻击。</p><p><img src="https://static.cnbetacdn.com/article/2022/0127/3b605b3e4ae16d8.png" alt="1.png" referrerpolicy="no-referrer"></p><p style="text-align: center;">NAS 用户总在有意无意间开启了允许远程访问</p><p>安全研究人员指出，DeadBolt 似乎正在扫描暴露于公网上的任何不安全的 NASA 系统。若不幸中招，用户存储的文件数据将被勒索软件给加密。</p><p>目前尚不清楚攻击者会如何与受害者取得联系，但用户应该会在某块受感染的硬盘驱动器上看到一条明文的信息，比如支付 BTC 赎金以解锁他们的文件。</p><p><img src="https://static.cnbetacdn.com/article/2022/0127/1671da8ae2ec4cb.png" alt="2.png" referrerpolicy="no-referrer"></p><p style="text-align: center;">推荐设置 1：禁用不必要的端口转发（QNAP <a href="https://www.qnap.com/en/how-to/faq/article/disable-unnecessary-port-forwarding" target="_self">传送门</a>）</p><p>为避免遇到潜在的麻烦，QNAP 在安全公告中建议 NAS 用户 ——（1）关闭<a data-link="1" href="https://c.duomai.com/track.php?site_id=242986&euid=&t=https://list.jd.com/list.html?cat=670,699,700" target="_blank">路由器</a>上的端口转发功能；（2）关闭 NAS 端的 UPnP 功能。</p><p>前者可进入路由器管理界面，取消“虚拟服务器 \ NAT \ 端口转发”设置，并关闭 NAS 管理服务端口（默认转发端口的设置为 8080 和 443）。</p><p>后者可移步至 QTS 菜单上的 myQNAPcloud，点击“自动路由器配置”，然后取消“启用 UPNP 端口转发”前的勾选。</p><p><img src="https://static.cnbetacdn.com/article/2022/0127/b8f850c8a32864a.png" alt="3.png" referrerpolicy="no-referrer"></p><p style="text-align: center;">推荐设置 2：取消启用 UPNP 端口转发</p><p>如果你在 QTS 仪表板上看到了“系统管理服务可通过如下 HTTP 协议，从外部 IP 地址直接访问”的提示，则清楚地表明当前 NAS 已暴露于公网。</p><p>当然，如果你主要还是在本地局域网（LAN）使用 NAS，那大可放心地屏蔽公网访问，相关网络附加存储体验并不会受到任何影响。</p>   
</div>
            