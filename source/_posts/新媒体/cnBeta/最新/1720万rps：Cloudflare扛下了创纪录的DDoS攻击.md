
---
title: '1720万rps：Cloudflare扛下了创纪录的DDoS攻击'
categories: 
 - 新媒体
 - cnBeta
 - 最新
headimg: 'https://static.cnbetacdn.com/thumb/article/2021/0821/ce8dfd6a7a61b9a.png'
author: cnBeta
comments: false
date: Sat, 21 Aug 2021 03:24:13 GMT
thumbnail: 'https://static.cnbetacdn.com/thumb/article/2021/0821/ce8dfd6a7a61b9a.png'
---

<div>   
<strong>互联网基础设施服务提供商 Cloudflare 今天披露 ，其已减轻了迄今为止最夸张的分布式拒绝服务攻击（简称 DDoS）。</strong>上月，Cloudflare 发现了针对金融行业客户的大规模 DDoS 攻击。可知攻击者利用了由 20000 多台受感染设备组成的僵尸网络，以通过向目标网络发送巨量 HTTP 请求的方式，来耗尽其服务器资源。<br>
 <p><a href="https://static.cnbetacdn.com/article/2021/0821/ce8dfd6a7a61b9a.png" target="_blank"><img src="https://static.cnbetacdn.com/thumb/article/2021/0821/ce8dfd6a7a61b9a.png" alt="1.png" referrerpolicy="no-referrer"></a></p><p style="text-align: center;">（来自：<a href="https://blog.cloudflare.com/cloudflare-thwarts-17-2m-rps-ddos-attack-the-largest-ever-reported/" target="_self">Cloudflare</a>）</p><p>与经典的“带宽 DDoS 攻击”不同，这类攻击又被称作“容量 DDoS”。在前一种情况下，攻击者会试图耗尽并阻塞受害者的互联网连接。</p><p>但在后一种情况下，攻击者会向受害者服务器发送竟可能多的垃圾 HTTP 请求，以耗尽宝贵的服务器 CPU / 内存资源，从而阻止合法用户访问目标站点。</p><p>Cloudflare 指出，在本次攻击的高峰，其记录下了每秒 1720 万次的请求（rps），规模也达到了以往针对公共领域发起的容量 DDoS 攻击的三倍。</p><p><img src="https://static.cnbetacdn.com/article/2021/0821/a38c5e26e6029bf.png" alt="2.png" referrerpolicy="no-referrer"></p><p>庆幸的是，尽管通过僵尸网络发起的攻击持续了数小时，Cloudflare 还是相当扎实地帮助客户扛下了超过 3.3 亿的垃圾 HTTP 请求。</p><p>不过僵尸网络幕后的攻击者也未就此收手，而是在随后几周内发起了另外两次大规模 DDoS 攻击。其中一次攻击达到了 800 万 rps，并且瞄准了网络托管服务提供商。</p><p>据悉，本次攻击的 1720 万 rps 记录，约占该公司在 2021 年 2 季度处理的合法 HTTP 流量的 68%（2500 万 rps）。</p><p><a href="https://static.cnbetacdn.com/article/2021/0821/acc4d7f4f76282c.png" target="_blank"><img src="https://static.cnbetacdn.com/thumb/article/2021/0821/acc4d7f4f76282c.png" alt="3.png" referrerpolicy="no-referrer"></a></p><p>目前 Cloudflare 正在对这个僵尸网络保持密切关注，可知其似乎利用了著名的 Mirai  IoT 恶意软件的修改版本来构建。</p><p>根据受感染设备的 IP 地址分布，Cloudflare 指出 15% 的攻击流量来自印度尼西亚，另有 17% 的攻击流量来自印度和巴西。</p><p>此前，亚马逊网络服务（AWS）曾于 2020 年 2 月记录了有史以来最大的带宽 DDoS 攻击，峰值达到了每秒 2.3 Tbps 。</p>   
</div>
            