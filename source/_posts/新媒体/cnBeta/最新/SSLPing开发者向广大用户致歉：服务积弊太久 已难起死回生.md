
---
title: 'SSLPing开发者向广大用户致歉：服务积弊太久 已难起死回生'
categories: 
 - 新媒体
 - cnBeta
 - 最新
headimg: 'https://static.cnbetacdn.com/article/2022/0413/d71502c2ef3ef87.png'
author: cnBeta
comments: false
date: Wed, 13 Apr 2022 10:19:28 GMT
thumbnail: 'https://static.cnbetacdn.com/article/2022/0413/d71502c2ef3ef87.png'
---

<div>   
<strong>SSLPing 是一款相当实用的工具，在注册并添加了你的服务器后，它就会帮助检查证书、协议、密码和已知漏洞。</strong>从 SSL v3 到 TLS 1.2，对于一些大型服务提供商来说，如果未能在证书到期前妥善处理，后续的影响还是相当难以规避的。然而近日，这款免费工具的创作者正在发出寻求帮助的讯号。<br>
<p><img src="https://static.cnbetacdn.com/article/2022/0413/d71502c2ef3ef87.png" referrerpolicy="no-referrer"></p><p style="text-align: center;">（来自：SSLPing <a href="https://sslping.com/about" target="_self">官网</a>）</p><p>据悉，作为一项没有广告支撑的免费服务，其有为超过 500 名注册用户提供对 12500 台 TLS 服务器的监测。</p><p>作为一个顺兴而为的项目，Chris Hartwig 认为 SSLPing 还是相当成功的。这是一次极佳的体验，他很高兴能够为所有人提供一项实用的服务。</p><p>然而由于 Patreon 赞助仅能覆盖 1/4 左右的成本，他已对此感到难以为继。更糟糕的是，SSLPing 在五天前遇到了问题。</p><p>Docker 容器在系统更新破坏了大量事务后拒绝运行（涉及 upstart / system / FS 驱动等），且他暂不清楚如何让它起死回生。</p><p>显然，SSLPing 的消亡，归咎于自 2016 年 3 月以来的一系列积弊。</p><blockquote><p>● 首先，SSLPing 使用了较旧的操作系统，且 Chris Hartwig 尝试更新无果。由于从 OpenSSL 中删除了一些旧内容，导致 SSLPing 的功能发生了改变。</p><p>● 其次，SSLPing 使用了较旧的 nodejs 版本，结果升级会剔除 SSL v3 检测。</p><p>● 第三，SSLPing 使用了现已失宠的 Docker Swarm 容器（最终的赢家是 Kubernetes），且物理服务器（其中 3 台）也年事已高 —— 上周挂掉了一台，另外两台已正常运行 1400 多天。</p><p>● 第四，SSLPing 依赖于现已弃用的 UI 库。</p><p>● ……（以及其它拖欠已久的技术债）</p></blockquote><p>好消息是，如果 Chris Hartwig 能够顺利发布 sslbot.io（旨在取代老旧的 SSLPing 服务），他也将在第一时间向外界公布。</p><p>对于在此期间引发的麻烦（但愿不会太严重），他还是深表歉意。</p>   
</div>
            