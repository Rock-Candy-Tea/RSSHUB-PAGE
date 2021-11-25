
---
title: '所有Windows版本均受影响 Cisco Talos发现一个高危提权漏洞'
categories: 
 - 新媒体
 - cnBeta
 - 最新
headimg: 'https://static.cnbetacdn.com/article/2021/1125/f82c91c95d86132.webp'
author: cnBeta
comments: false
date: Wed, 24 Nov 2021 23:55:13 GMT
thumbnail: 'https://static.cnbetacdn.com/article/2021/1125/f82c91c95d86132.webp'
---

<div>   
<strong>计算机安全组织 Cisco Talos 发现了一个新的漏洞，包括 Windows 11 和 Windows Server 2022 在内的所有 Windows 版本均受影响。</strong>该漏洞存在于 Windows 安装程序中，允许攻击者提升自己的权限成为管理员。<br>
 <p style="text-align:center"><img src="https://static.cnbetacdn.com/article/2021/1125/f82c91c95d86132.webp" alt="3mncqbaj.webp" referrerpolicy="no-referrer"></p><p style="text-align: left;">在发现该漏洞之后，Cisco Talos 集团升级了自己的 Snort 规则，该规则由检测针对一系列漏洞的攻击的规则组成。更新后的规则清单包括零日特权提升漏洞，以及针对浏览器、操作系统和网络协议等新兴威胁的新规则和修改后的规则。</p><p style="text-align: left;">利用该漏洞，拥有部分权限的用户可以提升自己的权限至系统管理员。这家安全公司已经在互联网上发现了恶意软件样本，这表明可能已经有黑客利用该漏洞发起攻击。</p><p style="text-align: left;">此前，微软的安全研究员 Abdelhamid Naceri 向微软报告了这个漏洞，据说在 11 月 9 日用 CVE-2021-41379 修复了该漏洞。然而，这个补丁似乎并不足以解决这个问题，因为这个问题仍然存在，导致Naceri在GitHub上发布了概念证明。</p><p style="text-align: left;">简单地说，这个概念证明显示了黑客如何利用微软Edge提升服务的酌情访问控制列表（DACL）将系统上的任何可执行文件替换为<a data-link="1" href="https://c.duomai.com/track.php?site_id=242986&euid=&t=https://msi-pc.jd.com/" target="_blank">MSI</a>文件。</p><p style="text-align: left;">微软将该漏洞评为"中等严重程度"，基本CVSS（通用漏洞评分系统）评分为5.5，时间评分为4.8。现在有了功能性的概念验证漏洞代码，其他人可以尝试进一步滥用它，可能会增加这些分数。目前，微软还没有发布一个新的更新来缓解这个漏洞。</p>   
</div>
            