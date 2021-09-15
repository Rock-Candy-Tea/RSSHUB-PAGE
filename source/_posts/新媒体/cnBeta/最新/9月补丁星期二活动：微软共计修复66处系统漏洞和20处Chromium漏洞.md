
---
title: '9月补丁星期二活动：微软共计修复66处系统漏洞和20处Chromium漏洞'
categories: 
 - 新媒体
 - cnBeta
 - 最新
headimg: 'https://static.cnbetacdn.com/article/2021/06/83c0cdc0ad1bb0e.jpg'
author: cnBeta
comments: false
date: Wed, 15 Sep 2021 05:46:45 GMT
thumbnail: 'https://static.cnbetacdn.com/article/2021/06/83c0cdc0ad1bb0e.jpg'
---

<div>   
<strong>在 9 月的补丁星期二活动日中，微软共计修复了 66 处系统漏洞和 20 处 Microsoft Edge 中的 Chromium 安全漏洞。</strong>受影响的产品包括。Azure、Edge（Android、Chromium 和 iOS）、Office、SharePoint Server、Windows、Windows DNS 和 Windows Subsystem for Linux。<br>
 <p><a href="https://static.cnbetacdn.com/article/2021/06/83c0cdc0ad1bb0e.jpg" target="_blank"><img src="https://static.cnbetacdn.com/article/2021/06/83c0cdc0ad1bb0e.jpg" referrerpolicy="no-referrer"></a></p><p>在修复的这些漏洞中，其中 3 个被评为“critical”（关键）、1 个被评为“moderate”（中等），其余的被评为“important”（重要）。</p><p>其中一个已经公开披露的 CVE 解决了 MSHTML 中的一个关键零日漏洞（CVE-2021-40444），也被称为<a data-link="1" href="https://c.duomai.com/track.php?site_id=242986&euid=&t=https://www.microsoftstore.com.cn/" target="_blank">微软</a>的传统 Trident 渲染引擎。该漏洞可被滥用，以实现任意代码的执行，在承载浏览器渲染引擎的微软 <a data-link="1" href="https://microsoft.pvxt.net/P0JMe" target="_blank">Office</a> 文档中使用恶意的 ActiveX 控件。这是我们在 9 月 7 日了解到的漏洞，并被用于针对 Office 用户的攻击。利用该漏洞的代码已经在网络上和安全研究人员之间流传，所以要打好补丁。</p><p>另一项修复更新了 8 月 11 日公开披露的补丁，该补丁解决了上个月的 Print Spooler RCE（CVE-2021-36958）。IT资产管理公司 Ivanti 的产品管理副总裁 Chris Goettl 在发给 The Register 的一份声明中解释说：“这次更新已经删除了以前定义的缓解措施，因为它不再适用，并解决了研究人员在原始修复之外发现的其他问题。该漏洞已被公开披露，而且可以获得功能性的利用代码，因此这使本月的<a data-link="1" href="https://microsoft.pvxt.net/x9Vg1" target="_blank">Windows</a>操作系统更新变得更加紧迫”。</p><p>Goettl 说之前披露的第三个漏洞（CVE-2021-36968）解决了 Windows DNS 中的一个权限提升漏洞。这个 CVE 适用于传统的 Windows 操作系统。</p><p>还有另外两个关键漏洞修复：一个是 Windows WLAN 自动配置服务远程代码执行漏洞（CVE-2021-36965）和一个开放管理基础设施远程代码执行漏洞（CVE-2021-38647）。Zero-Day Initiative 的 Dustin Childs 在一份公告中说，前者允许邻近网络的攻击者，如<a data-link="1" href="https://c.duomai.com/track.php?site_id=242986&euid=&t=https%3A%2F%2Flist.jd.com%2Flist.html%3Fcat%3D737%2C752%2C761" target="_blank">咖啡</a>店的公共 Wi-Fi，接管一个有漏洞的目标系统。</p><p>后者甚至更严重。这是一个严重性（CVSS 9.8）的错误，在Linux和Unix风味的操作系统的开放管理基础设施（OMI）。它可以被利用来获得对网络上有漏洞的机器的管理控制，不需要认证或其他检查。</p><p>Childs警告说：“这个漏洞不需要用户互动或权限，所以攻击者只需向受影响的系统发送一个特制的信息，就可以在受影响的系统上运行他们的代码。OMI用户应该迅速测试和部署这个”。</p>   
</div>
            