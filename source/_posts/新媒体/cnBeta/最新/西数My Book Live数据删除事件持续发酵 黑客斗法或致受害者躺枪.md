
---
title: '西数My Book Live数据删除事件持续发酵 黑客斗法或致受害者躺枪'
categories: 
 - 新媒体
 - cnBeta
 - 最新
headimg: 'https://static.cnbetacdn.com/article/2021/0630/fd7be89cf5ba241.jpeg'
author: cnBeta
comments: false
date: Wed, 30 Jun 2021 04:27:59 GMT
thumbnail: 'https://static.cnbetacdn.com/article/2021/0630/fd7be89cf5ba241.jpeg'
---

<div>   
Ars Technica 报道称：<strong>上周西部数据（WD）My Book Live 网络附加存储（NAS）用户遭遇的大量数据被删除事件，或涉及不止一个严重的安全漏洞。</strong>起初包括西数在内的许多人，都将问题指向了一个 2018 年的已知漏洞，可知其允许对设备进行 root 访问。然而随着时间的推移，我们不禁产生了更多的疑问。<br>
 <p style="text-align: center;"><img src="https://static.cnbetacdn.com/article/2021/0630/fd7be89cf5ba241.jpeg" referrerpolicy="no-referrer"></p><p>ArsTechnica 曝光的第二个漏洞，并没有向其它漏洞一样可让攻击者完全控制用户的设备。可即便如此，攻击者仍可在无需知道密码的情况下，抹除 My Book Live 上的用户数据。</p><p>有鉴于此，在西数官方完成个人 NAS 设备的安全漏洞修复之前，还请尽量让 My Book Live 和 My Book Live Duo 等机型保持与外网隔离的状态。</p><p>对于那些不幸丢失了数据的人们来说，更可气的是，西数其实本已预料到了这种状况。然而在 WD My Book Live 软件中，相关代码似乎被官方给注释掉（或停用）了。</p><p>受此影响，当被要求恢复出厂设置时，软件竟然不会先执行一遍身份验证。</p><p style="text-align: center;"><img src="https://static.cnbetacdn.com/article/2021/0630/9c3f48e9baed173.jpg" referrerpolicy="no-referrer"></p><p>考虑到西数已于 2015 年停止支持这些设备，相关漏洞或从那时起一直存在。然而最让人感到不解的是，为何黑客坏到非要将 My Book Live 用户的设备恢复至出厂状态？</p><p>根据安全公司 Censys 的分析，Ars Technica 提出了一个疯狂的猜想 —— 数据删除或是不同黑客之间发生争斗的结果！</p><p>比如某个僵尸网络掌控者试图接管或破坏另一个，于是决定利用已知的漏洞来控制设备以达到恶意目的，然后另一黑客又利用了位置的远程擦除漏洞来重置这些受害设备。</p><p>最终在黑客斗法期间，无辜用户的数据就不幸被丢进了火葬场。不过截止发稿时，西数方面尚未回应外媒的置评请求。</p>   
</div>
            