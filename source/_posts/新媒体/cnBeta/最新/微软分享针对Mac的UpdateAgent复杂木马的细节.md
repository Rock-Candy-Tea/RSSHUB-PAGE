
---
title: '微软分享针对Mac的UpdateAgent复杂木马的细节'
categories: 
 - 新媒体
 - cnBeta
 - 最新
headimg: 'https://static.cnbetacdn.com/thumb/article/2022/0203/7f0872bc25e2a08.png'
author: cnBeta
comments: false
date: Thu, 03 Feb 2022 08:24:03 GMT
thumbnail: 'https://static.cnbetacdn.com/thumb/article/2022/0203/7f0872bc25e2a08.png'
---

<div>   
网络安全仍然是一个不断发展的领域，对威胁者和安全专家来说都是如此。尽管如此，最近产生的一个积极因素是，公司更愿意与合作伙伴、专家和更大的社区分享信息，共同应对威胁。<strong>这方面的一个例子是，微软与苹果合作修补macOS设备中的"Shrootless"漏洞。微软已经提供了有关一个针对Mac的复杂木马的详细信息。</strong><br>
 <p><a href="https://static.cnbetacdn.com/article/2022/0203/7f0872bc25e2a08.png" target="_blank"><img src="https://static.cnbetacdn.com/thumb/article/2022/0203/7f0872bc25e2a08.png" title alt="UpdateAgent-Timeline-1024x593.png" referrerpolicy="no-referrer"></a></p><p>该木马被称为"UpdateAgent"，早在2020年9月就出现了，是一个相对基本的信息窃取者。然而，从那时起发展到现在，它已经进化了很多，其最近的升级版本实际上已经开始对外"承揽生意"，分发二级有效载荷，如Adload广告软件。微软提醒说，UpdateAgent不断发展的持续渗透方法意味着它在未来的活动中可能会进一步发展，并分发更危险的载荷。</p><p>UpdateAgent通常会伪装成用户在其Mac上下载的合法软件。然后，它绕过几个macOS控件，在设备中持续存在。这方面的一个例子是绕过Gatekeeper，原本这一机制是为了确保只有受信任的应用程序可以在计算机硬件上运行。然后，该木马程序利用现有的用户权限来执行恶意活动，之后就会掩盖其踪迹。</p><p>微软还指出，UpdateAgent从S3和AWS的Cloudfront下载其恶意的载荷。因此，该公司已与亚马逊合作，删除了一些已知的问题URL。从UpdateAgent在2020年9月首次出现到2021年10月的最新活动，可以从下面的图中看到它的演变。</p><p>微软表示，2021年10月的UpdateAgent活动是其迄今为止最复杂的活动之一。该木马以.zip和.pkg格式打包，并通过驱动下载进行传播，但最终结果也包括对Sudoer列表的修改。微软的调查还显示，最新攻击的基础设施是在2021年9月创建的，同时还发现了其他恶意域名。这表明，UpdateAgent正在积极开发，并可能在接下来继续变得更加复杂和危险。</p><p><a href="https://static.cnbetacdn.com/article/2022/0203/e344e0f22f5fc2c.png" target="_blank"><img src="https://static.cnbetacdn.com/thumb/article/2022/0203/e344e0f22f5fc2c.png" title alt="UpdateAgent-Attack-Chain-1024x445.png" referrerpolicy="no-referrer"></a></p><p><strong>该公司对现有的Adload Adware载荷提供了以下细节分享：</strong></p><p>一旦广告软件被安装，它就会使用广告注入软件和技术来拦截设备的在线通信，并通过广告软件运营商的服务器重定向用户的流量，将广告和促销活动注入到网页和搜索结果。更具体地说，Adload利用中间人（PiTM）攻击，通过安装一个网络代理来劫持搜索引擎结果，并将广告注入网页，从而将广告收入从官方网站持有人那里抽走，转给广告软件运营商。</p><p>Adload也是一种异常持久的广告软件。它能够打开一个后门，下载和安装其他广告软件载荷，此外还能收集系统信息，并将其发送到攻击者的C2服务器。考虑到UpdateAgent和Adload都有能力安装额外的有效载荷，攻击者可以利用这些载体中的任何一个或两个，在未来的活动中可能向目标系统提供更危险的威胁。</p><p>就目前而言，微软有一些针对UpdateAgent的保护建议。对于公众来说，这些建议包括限制对特权资源的访问，只从受信任的来源安装应用程序，部署最新的软件安全更新，以及使用能自动阻止恶意网站的浏览器。</p><p>微软希望通过分享所有这些信息，强调不断演变的恶意软件的威胁，以及供应商必须提供的安全解决方案的类型，以保护<a data-link="1" href="https://microsoft.pvxt.net/x9Vg1" target="_blank">Windows</a>和非Windows机器。</p><p><strong>微软还分享了一些高级技术细节，您可以在这里阅读更多信息：</strong></p><p><a href="https://www.microsoft.com/security/blog/2022/02/02/the-evolution-of-a-mac-trojan-updateagents-progression/" _src="https://www.microsoft.com/security/blog/2022/02/02/the-evolution-of-a-mac-trojan-updateagents-progression/" target="_blank">https://www.microsoft.com/security/blog/2022/02/02/the-evolution-of-a-mac-trojan-updateagents-progression/</a><br></p>   
</div>
            