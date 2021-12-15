
---
title: 'CISA敦促美国联邦机构在圣诞节前完成Log4Shell漏洞修补'
categories: 
 - 新媒体
 - cnBeta
 - 最新
headimg: 'https://static.cnbetacdn.com/article/2021/1215/6f3e6dca04741ba.jpg'
author: cnBeta
comments: false
date: Wed, 15 Dec 2021 08:24:11 GMT
thumbnail: 'https://static.cnbetacdn.com/article/2021/1215/6f3e6dca04741ba.jpg'
---

<div>   
<strong>美国网络安全和基础设施安全局（CISA）已经向各联邦机构发去警示，敦促其在平安夜前修补受 Log4Shell 漏洞影响的系统。</strong>昨日，该机构已将 CVE-2021-44228 和其它 12 个安全漏洞列入“主动漏洞利用目录”。基于此，相关联邦机构将有十天时间来测试有哪些内部应用程序 / 服务器使用了 Log4j Java 库、检查系统是否易受 Log4Shell 攻击、并及时修补受影响的服务器。<br>
 <p style="text-align: center;"><img src="https://static.cnbetacdn.com/article/2021/1215/6f3e6dca04741ba.jpg" alt="CISA Log4j.jpg" referrerpolicy="no-referrer"></p><p style="text-align: center;">由目录时间表可知，上述工作需在 12 月 24 日之前完成。</p><p>此外，CISA 于昨日提出了一个<a href="https://github.com/cisagov/log4j-affected-db" target="_self">专门的网页</a>，旨在为美国公共和私营部门提供有关 Log4Shell 漏洞缓解措施的指导。</p><p>该机构计划在该页列出所有易受 Log4Shell 漏洞影响的软件供应商，以便大家即使获取最新且全面的补丁信息。</p><p>尽管自上周以来，厂商已经陆续推出了紧急补丁，但要等到正式融合于相关软件，显然还需要再等待一段时间。</p><p><a href="https://static.cnbetacdn.com/article/2021/1215/434926ff44ebd85.png" target="_blank"><img src="https://static.cnbetacdn.com/thumb/article/2021/1215/434926ff44ebd85.png" alt="CISA Log4j.png" referrerpolicy="no-referrer"></a></p><p>虽然 CISA 工作人员仍在通过 GitHub 收集项目信息，但安全研究员 Royce Williams 已经编制了哪些产品易受 Log4Shell 漏洞攻击影响的<a href="https://www.techsolvency.com/story-so-far/cve-2021-44228-log4j-log4shell/#affected-products" target="_self">一份列表</a>（其中涵盖了 300 多家供应商），此外还有一份由<a href="https://github.com/NCSC-NL/log4shell/tree/main/software" target="_self">荷兰国家网络安全中心</a>维护的名录。</p><p>至于造成本次风波的罪魁祸首，其源于 Log4j 这个 Java 库中的一个 bug 。Log4j 为许多 Java 桌面应用程序 / 服务器软件提供了日志创建和管理功能，但几乎无处不在的大规模漏洞利用，已将各个行业逼到了相当危险的境地。</p><p>另一个需要考虑的是，思科与 Cloudflare 均表示，他们曾于漏洞公开两周前首次看到 Log4Shell 被利用的迹象 —— 确切说法是 12 月 1 日发生了首次攻击（而不是上周）—— 意味着安全团队需要扩大相关响应事件的调查。</p><div class="article-relation"><p><strong>相关文章:</strong></p><p><a href="https://www.cnbeta.com/articles/tech/1214303.htm" target="_blank">CISA示警Log4j破坏力惊人 数亿台设备受到影响</a></p><p><a href="https://www.cnbeta.com/articles/tech/1215009.htm" target="_blank">Log4j漏洞大流行：72小时内发生超84万起攻击</a></p></div>   
</div>
            