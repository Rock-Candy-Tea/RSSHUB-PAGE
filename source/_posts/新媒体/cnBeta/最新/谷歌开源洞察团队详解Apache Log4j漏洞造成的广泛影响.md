
---
title: '谷歌开源洞察团队详解Apache Log4j漏洞造成的广泛影响'
categories: 
 - 新媒体
 - cnBeta
 - 最新
headimg: 'https://static.cnbetacdn.com/thumb/article/2021/1220/b12596609773f19.png'
author: cnBeta
comments: false
date: Mon, 20 Dec 2021 09:18:02 GMT
thumbnail: 'https://static.cnbetacdn.com/thumb/article/2021/1220/b12596609773f19.png'
---

<div>   
<strong>上周五，谷歌开源洞察团队在官方安全博客上发表了一篇文章，详细介绍了 Apache Log4j 漏洞对行业造成的广泛影响。</strong>James Wetter 和 Nicky Ringland 指出，超过 35000 个 Java 包、占总数 8% 以上的 Maven 中央存储库，尤其让我们对其留下的隐患感到担忧。<br>
 <p><a href="https://static.cnbetacdn.com/article/2021/1220/b12596609773f19.png" target="_blank"><img src="https://static.cnbetacdn.com/thumb/article/2021/1220/b12596609773f19.png" alt="1.png" referrerpolicy="no-referrer"></a></p><p style="text-align: center;">（来自：<a href="https://security.googleblog.com/2021/12/understanding-impact-of-apache-log4j.html" target="_self">Google Security Blog</a>）</p><p>据悉，这些漏洞允许攻击者利用 Log4j 日志库已被广为人知的不安全 JNDI 查找功能来执行远程代码。糟糕的是，这项功能在许多版本中都被默认启用。</p><p>自 12 月 9 日披露以来，Log4j 漏洞因其严重性和广泛影响，而引起了信息安全生态系统的高度关注。毕竟作为一款流行的日志工具，它已被数以万计的软件包（Java 里的 Artifacts）和项目所使用。</p><p>由于用户对 Log4j 的传递依赖项缺乏足够的远见，这不仅使得我们很难确定零日漏洞的影响范围、相关修复工作也变得相当困难。</p><p><a href="https://static.cnbetacdn.com/article/2021/1220/4551e9844d6d34b.png" target="_blank"><img src="https://static.cnbetacdn.com/thumb/article/2021/1220/4551e9844d6d34b.png" alt="2.png" referrerpolicy="no-referrer"></a></p><p>期间，Google 开源洞察团队调查了 Maven 中央存储库中的 Java 工件的所有版本，最终将范围缩小到了基于 JVM 语言的开源生态系统，同时密切追踪事态的发展。</p><p>截至 2021 年 12 月 16 日，该团队发现来自 Maven Central 的 35863 个可用 Java 工件，有依赖于受影响的 log4j 代码。</p><p>这意味着，仅 Maven Central 平台上超过 8% 的软件包，都至少有一个版本受此漏洞的影响。</p><p>若放眼整个生态系统，漏洞威力更是不容小觑（Maven Central 的平均影响为 2% / 中位数低于 0.1%）。</p><p>直接受影响的依赖项，约占这部分工件中的 7000 个，意味着它们的任何版本都被 Log4j-core 或 Log4j-api 所波及（完整列表可见 CVE 漏洞披露公告）。</p><p>此外大多数受影响的工件，都来自间接的依赖项，即它们是作为传递依赖项而被牵扯进来的。</p><p><img src="https://static.cnbetacdn.com/article/2021/1220/c34060a72d7d8b3.png" alt="3.png" referrerpolicy="no-referrer"></p><p>至于当前开源 JVM 生态系统的修复进展，若工件中至少有一个版本受到了影响，且发布了一个不受漏洞波及的更稳定版本，谷歌开源洞察团队就将之视作已修复。</p><p>比如受 Log4j 漏洞影响的工件已更新到 2.16.0、或完全剔除了对 Log4j 的依赖。庆幸的是，Log4j 维护者和更广泛的开源社区对此问题的响应是相当迅速的，并且付出了切实的巨大努力。</p><p>截止博客发表时，团队统计到了将近 5000 个已被修复的项目。至于剩余的那 30000 个工件，其中许多依赖于另一个工件。在传递依赖被修复前，暂时只有一刀切来阻止。</p><p><a href="https://static.cnbetacdn.com/article/2021/1220/0d47a16badc1ece.png" target="_blank"><img src="https://static.cnbetacdn.com/thumb/article/2021/1220/0d47a16badc1ece.png" alt="4.png" referrerpolicy="no-referrer"></a></p><p>对于 Java 生态系统来说，修复难度主要体现在工件的互相连接。首先，依赖链越深，漏洞修复所需的步骤就越繁杂（超过 80% 软件包的深度都超过了一级）。</p><p>其次，依赖算法和需求规范中的生态系统级选择约定，也为事件埋下了较大的伏笔。在 Java 生态系统中，开发者的通常做法是指定软件版本方面的“软”要求（假设没有其它版本的相同包出现在依赖关系图中）。</p><p>此类修复通常需要维护人员采取更加明确的行动，以将依赖需求更新为修补后的版本。这种做法与其它生态系统形成了鲜明的对比，例如在 npm 软件包上，开发者通常会为依赖项指定敞开的范围。</p><p>最后，对于整个生态系统需要耗费多少时间来完成漏洞修复，目前也很难评估。在查看了所有公开披露的影响 Maven 包的关键建议中，我们发现只有不到一半（48%）得到了修复。</p><p>不过在 Log4j 方面，事情还算是相当积极的。不到一周后，就有 4620 个受影响的工件（约 13%）得到了修复。剩下的工作，仍需全球开源维护者、信息安全团队和广大用户付出巨大的努力。</p>   
</div>
            