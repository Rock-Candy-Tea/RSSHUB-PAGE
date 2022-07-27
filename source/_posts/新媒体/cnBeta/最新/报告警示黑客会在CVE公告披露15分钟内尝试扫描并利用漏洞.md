
---
title: '报告警示黑客会在CVE公告披露15分钟内尝试扫描并利用漏洞'
categories: 
 - 新媒体
 - cnBeta
 - 最新
headimg: 'https://static.cnbetacdn.com/article/2022/0727/d9a72ef62a6d221.jpg'
author: cnBeta
comments: false
date: Wed, 27 Jul 2022 09:34:36 GMT
thumbnail: 'https://static.cnbetacdn.com/article/2022/0727/d9a72ef62a6d221.jpg'
---

<div>   
由 Palo Alto Networks 最新公布的《2022 版 Unit 42 事件响应报告》可知，<strong>黑客一直在密切监视软件供应商的公告板上是否有最新的 CVE 漏洞报告，并且会在极短的 15 分钟内开始扫描易受攻击的端点。</strong>这意味着系统管理员修复已披露安全漏洞的时间，要远少于此前的预估。<br>
 <p><img src="https://static.cnbetacdn.com/article/2022/0727/d9a72ef62a6d221.jpg" alt="1.jpg" referrerpolicy="no-referrer"></p><p style="text-align: center;">漏洞利用的初始访问方式推测</p><p>Palo Alto Networks 在一篇专题博客文章中提到，随着威胁行为者竞相在漏洞修补前加以利用，系统管理员将不得不打起 12 分精神。</p><p>更糟糕的是，由于漏洞扫描的技能要求并不高，所以水平较低的攻击者也可轻松筛选互联网上易受攻击的端点，并将有价值的发现抛售到暗网市场上牟利。</p><blockquote><p>以 CVE-2022-1388 为例，Unit 42 指出这是一个严重影响 F5 BIG-IP 产品、且未经身份验证的远程命令执行漏洞。</p><p>该漏洞于 2022 年 5 月 4 日披露，但在 CVE 公告发布十小时后，他们就已记录 2552 次端点扫描和漏洞利用尝试。</p></blockquote><p>其次，报告指出“ProxyShell”是 2022 上半年被触及最多的漏洞利用链（特指 CVE-2021-34473、CVE-2021-34523 和 CVE-2021-31207），占据了利用事件总数的 55% 。</p><p>Log4Shell 以 14% 紧随其后，各种 SonicWall CVE 占据了 7%、ProxyLogon 占了 5%，而 Zoho ManageEngine ADSelfService Plus 中的远程代码执行（RCE）漏洞也有 3% 。<img src="https://static.cnbetacdn.com/article/2022/0727/f412fee41bc8a89.jpg" alt="2.jpg" referrerpolicy="no-referrer"></p><p style="text-align: center;">漏洞利用排行</p><p>统计数据表明，半旧（而不是最新）的缺陷，最容易被攻击者所利用。发生这种情况的原因有许多，包括但不限于攻击面的大小、漏洞利用的复杂性、及其能够产生的实际影响。</p><p>有鉴于此，Palo Alto Networks 建议管理员尽快部署安全更新，以更好地避免系统成为零日 / CVE 公告发布初期的漏洞利用受害者。</p><blockquote><p>此外 Unit 42 报告指出，利用软件漏洞开展初始网络破坏的方法，仅占到 1/3 左右。</p><p>在 37% 的案例中，网络钓鱼仍是许多攻击者的首选。另外在 15% 的案例中，黑客也会利用泄露凭证、或暴力破解来入侵网络。</p><p>而针对特权员工的社会工程技巧、或贿赂流氓内部人员，也占所有漏洞攻击响应事件的 10% 左右。</p></blockquote><p>鉴于系统 / 网络 / 安全管理专业人员已经面临相当大的压力，报告建议组织机构尽量让设备远离互联网。</p><p>除了通过虚拟专用网（或其它安全网关）来限制对服务器的访问以降低风险，非必要的公开端口和服务也必须尽量封堵上。</p><p>最后就是养成勤快部署安全更新的习惯，尽管快速部署关键更新会导致一定时间的业务中断，但这总比面对遭遇全面网络攻击后难以弥补的局面要好得多。</p>   
</div>
            