
---
title: 'TeslaMate漏洞致数十辆特斯拉电动汽车可被远程访问'
categories: 
 - 新媒体
 - cnBeta
 - 最新
headimg: 'https://static.cnbetacdn.com/article/2022/0125/5773e30223c5a88.png'
author: cnBeta
comments: false
date: Tue, 25 Jan 2022 04:31:25 GMT
thumbnail: 'https://static.cnbetacdn.com/article/2022/0125/5773e30223c5a88.png'
---

<div>   
本月早些时候，德国安全研究员 David Colombo 在一条推文中，首次披露了影响特斯拉电动汽车的一个严重隐患。<strong>由于流行的第三方开源日志工具中的一个安全漏洞，车子竟然被直接暴露于互联网上。</strong>若被攻击者闯入，该漏洞或导致远程解锁车门、鸣喇叭、甚至启动汽车。<br>
 <p><img src="https://static.cnbetacdn.com/article/2022/0125/5773e30223c5a88.png" alt="1.png" referrerpolicy="no-referrer"></p><p>在一连串相关推文之后，David Colombo 于周一的一篇博客文章中，介绍了他是如何在偶然情况下发现该漏洞、并“完全远程控制”了超过 25 辆特斯拉电动汽车的。</p><p>庆幸的是，他一直在努力向受影响的车主披露这个问题、且没有向别有用心的黑客公开详细信息。目前漏洞已得到正式修复，无法再被公开利用。</p><p><img src="https://static.cnbetacdn.com/article/2022/0125/e50682d136c6e93.png" alt="2.png" referrerpolicy="no-referrer"></p><p>David Colombo 在接受采访时称，他是在 TeslaMate 中发现的这个远程漏洞。作为一款免费的日志软件，许多特斯拉车主都用它来连接车载系统。</p><p>你可借此来轻松访问被默认隐藏的相关数据，包括电耗、位置历史记录、驾驶统计，以及用于故障排除和问题诊断的各种细粒度的信息。</p><p><img src="https://static.cnbetacdn.com/article/2022/0125/e21fed96254528a.png" alt="3.png" referrerpolicy="no-referrer"></p><p>作为一款“自托管”形式的网络仪表板，TeslaMate 通常在爱好者的家用电脑上运行，并依靠特斯拉 API 来访问与车主账户相关的车载数据。</p><p>然而由于网络仪表板中的一个安全漏洞 —— 比如允许匿名访问和使用一些用户从未修改过的默认密码、再加上车主的错误配置 —— 结果就导致至少数百个 TeslaMate 仪表板被直接暴露于互联网上。</p><p><img src="https://static.cnbetacdn.com/article/2022/0125/2621588a5a9aec1.png" alt="4.png" referrerpolicy="no-referrer"></p><p>API 暴露的风险，还涉及远程控制特斯拉汽车的密钥。此外 Colombo 在接受外媒电话采访时称，受影响的汽车数量可能更高。</p><p>从去年偶然发现暴露在公网上的仪表板之后，Colombo 发现 TeslaMate 没有在默认情况下施加防护。</p><p><img src="https://static.cnbetacdn.com/article/2022/0125/2bc22ac474d0a22.png" alt="5.png" referrerpolicy="no-referrer"></p><p>在网络上展开一番搜索后，可知受影响的车主遍布英美、欧洲、中国、加拿大等市场，甚至扒出了某人近期穿越过的一条加州旅行路线。</p><p>更糟糕的情况，就是被攻击者提取了用户的 API 密钥，那样别有用心者就可在车主不知情的情况下，保持对特斯拉电动汽车的长期隐匿访问。</p><p><img src="https://static.cnbetacdn.com/article/2022/0125/75e75787a1a34c7.png" alt="6.png" referrerpolicy="no-referrer"></p><p>据悉，在私下通报了漏洞后，TeslaMate 已推送了新版软件，但需用户手动安装才能彻底封堵访问漏洞。</p><p>万幸的是，特斯拉已经撤销了数千个 API 密钥。此外即使想要切实利用该漏洞，仍需要相当高深且繁琐的操作。且在许多情况下，都无法准确地与车主取得联系。</p>   
</div>
            