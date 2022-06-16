
---
title: 'PanSift实测：IPv6互联网访问延迟优于IPv4'
categories: 
 - 新媒体
 - cnBeta
 - 最新
headimg: 'https://static.cnbetacdn.com/article/2022/0616/6bea93298cb85fd.jpg'
author: cnBeta
comments: false
date: Thu, 16 Jun 2022 09:22:27 GMT
thumbnail: 'https://static.cnbetacdn.com/article/2022/0616/6bea93298cb85fd.jpg'
---

<div>   
随着 IPv4 公网 IP 走向枯竭，IPv6 开始被人们寄予更多的期望。<strong>不过除了某些尚未搞定的兼容性问题，许多人也对 IPv6 相较于 IPv4 的访问速度变化充满了好奇。</strong>有鉴于此，PanSift 特地回顾了过去 30 天时间里的一系列监控代理收集的匿名数据，并耐心整理出了一系列图表。<br>
 <p><img src="https://static.cnbetacdn.com/article/2022/0616/6bea93298cb85fd.jpg" alt="0.jpg" referrerpolicy="no-referrer"></p><p style="text-align: center;">（来自：Pansift <a href="https://pansift.com/blog/is-ipv6-faster-than-ipv4/" target="_self">Blog</a>）</p><p>需要指出的是，网络通信受到诸多因素的影响，包括但不限于数据集大小、设备差异、操作系统版本、传输介质、协议、CoS 类型等。</p><p><img src="https://static.cnbetacdn.com/article/2022/0616/ea1c09830b7ff8a.png" alt="1.png" referrerpolicy="no-referrer"></p><p style="text-align: center;">表 - 1：IPv4 与 IPv6 总延迟对比</p><p>为了给出简洁明了的回答，PanSift 首先使用了所谓的 Wi-Fi 保证和远程故障排除工具（<a href="https://app.pansift.com/" target="_self">传送门</a>），涉及 240 万个网络相关的网关数据点。</p><p><a href="https://static.cnbetacdn.com/article/2022/0616/b4077d2ae1ca542.png" target="_blank"><img src="https://static.cnbetacdn.com/thumb/article/2022/0616/b4077d2ae1ca542.png" alt="2.png" referrerpolicy="no-referrer"></a></p><p style="text-align: center;">图 - 1：IPv4 总延迟分布</p><p>测量从 16 个随机选择的 macOS 代理中、并且每隔 30 秒执行一次（指定最长 30 天的数据保留期）。</p><p><a href="https://static.cnbetacdn.com/article/2022/0616/d24f186581258bb.png" target="_blank"><img src="https://static.cnbetacdn.com/thumb/article/2022/0616/d24f186581258bb.png" alt="3.png" referrerpolicy="no-referrer"></a></p><p style="text-align: center;">图 - 2：IPv6 总延迟分布</p><p>随后使用数据点的双栈连接代理、而不仅仅是本地连接，以使得任何比较都更加公平（这样就有了潜在持续的穿越连接和网关的流量）。</p><p><img src="https://static.cnbetacdn.com/article/2022/0616/cf16617de69cf2a.png" alt="4.png" referrerpolicy="no-referrer"></p><p style="text-align: center;">表 - 2：IPv4 与 IPv6 的 WLAN 延迟评估</p><p>此外需要注意的是，PanSift 不会对数据进行规范化、并保留完整的保真度指标，以允许开展更具细粒度的分析、甚至在故障排除时进行追溯。</p><p><img src="https://static.cnbetacdn.com/article/2022/0616/5885a9a181d0563.png" alt="5.png" referrerpolicy="no-referrer"></p><p style="text-align: center;">表 - 3：IPv4 与 IPv6 的有线延迟评估</p><p>在过滤了具有 IPv4 和 IPv6 并发互联网连接的可达性代理数据后，PanSift 最终得到了 34 万 2980 个有效数据点，并汇总出了如上结果。</p>   
</div>
            