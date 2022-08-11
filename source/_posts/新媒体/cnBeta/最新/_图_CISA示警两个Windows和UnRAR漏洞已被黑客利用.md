
---
title: '_图_CISA示警两个Windows和UnRAR漏洞已被黑客利用'
categories: 
 - 新媒体
 - cnBeta
 - 最新
headimg: 'https://static.cnbetacdn.com/article/2022/0811/4b75c5bbb84307f.webp'
author: cnBeta
comments: false
date: Thu, 11 Aug 2022 08:50:17 GMT
thumbnail: 'https://static.cnbetacdn.com/article/2022/0811/4b75c5bbb84307f.webp'
---

<div>   
<strong>美国网络安全和基础设施安全局 (CISA)基于目前掌握的证据，在已知可利用漏洞（Known Exploited Vulnerabilities）目录下新增了 2 个新的漏洞。</strong>其中 1 个漏洞存在于 Windows Support Diagnostic Tool (MSDT)，并以零日（0-Day）的形式存在 2 年多时间，有充足的证据表明被黑客利用。<br>
 <p style="text-align:center"><img src="https://static.cnbetacdn.com/article/2022/0811/4b75c5bbb84307f.webp" referrerpolicy="no-referrer"></p><p style="text-align: left;">这两个安全漏洞都被标记为高严重性评分，并且是目录遍历漏洞，可以帮助攻击者在目标系统上植入恶意软件。官方跟踪为 CVE-2022-34713，非正式地称为 DogWalk，MSDT 中的安全漏洞允许攻击者将恶意可执行文件放入 <a data-link="1" href="https://microsoft.pvxt.net/x9Vg1" target="_blank">Windows</a> 启动文件夹。</p><p style="text-align: left;">该问题最初是由研究员 Imre Rad 于 2020 年 1 月向<a data-link="1" href="https://c.duomai.com/track.php?site_id=242986&euid=&t=https://www.microsoftstore.com.cn/" target="_blank">微软</a>报告的，但他的报告被错误地归类为未描述安全风险，因此被驳回。今年，安全研究员 j00sean 再次引起了公众的关注，他总结了攻击者可以通过利用它实现的目标，并提供了视频证明：</p><p style="text-align:center"><img src="https://static.cnbetacdn.com/article/2022/0811/61267630854273d.webp" alt="ezgif.com-gif-maker-1.webp" referrerpolicy="no-referrer"></p><p style="text-align:center"><img src="https://static.cnbetacdn.com/article/2022/0811/17beb118911052d.webp" referrerpolicy="no-referrer"></p><p style="text-align: left;">不过要利用该漏洞需要和用户进行交互，这是一个很容易通过社会工程克服的障碍，尤其是在电子邮件和基于 Web 的攻击中，微软在今天的一份咨询中表示：</p><p style="text-align: left;">● 在电子邮件攻击场景中，攻击者可以通过向用户发送特制文件并诱使用户打开文件来利用该漏洞。</p><p style="text-align: left;">● 在基于 Web 的攻击情形中，攻击者可能拥有一个网站（或利用接受或托管用户提供的内容的受感染网站），其中包含旨在利用该漏洞的特制文件。</p><p style="text-align: left;">自 6 月初以来，0patch 微补丁服务提供了一个非官方补丁，适用于大多数受影响的 Windows 版本（Windows 7/10/11 和 Server 2008 至 2022）。作为 2022 年 8 月 Windows 安全更新的一部分，微软今天解决了 CVE-2022-34713。该公司指出，该问题已在攻击中被利用。</p><p style="text-align: left;">添加到 CISA 的 Known Exploited Vulnerabilities 目录的第二个漏洞被跟踪为 CVE-2022-30333，它是 Linux 和 Unix 系统的 UnRAR 实用程序中的路径遍历错误。攻击者可以利用它在解压操作期间将恶意文件提取到任意位置，从而在目标系统上植入恶意文件。</p><p style="text-align: left;">瑞士公司 SonarSource 于 6 月下旬在一份报告中披露了该安全问题，该报告描述了如何将其用于远程执行代码，从而在未经身份验证的情况下破坏 Zimbra 电子邮件服务器。</p>   
</div>
            