
---
title: 'CISA发布Apache Log4j漏洞扫描器 以筛查易受攻击的应用实例'
categories: 
 - 新媒体
 - cnBeta
 - 最新
headimg: 'https://static.cnbetacdn.com/article/2021/1225/e3615255ac2f55e.png'
author: cnBeta
comments: false
date: Sat, 25 Dec 2021 05:32:22 GMT
thumbnail: 'https://static.cnbetacdn.com/article/2021/1225/e3615255ac2f55e.png'
---

<div>   
在 Log4shell 漏洞曝光之后，美国网络安全与基础设施局（CISA）一直在密切关注事态发展。除了敦促联邦机构在圣诞假期之前完成修补，国防部下属的该机构还发起了 #HackDHS 漏洞赏金计划。<strong>最新消息是，CISA 又推出了一款名叫“log4j-scanner”的漏洞扫描器，以帮助各机构筛查易受攻击的 web 服务。</strong><br>
 <p><img src="https://static.cnbetacdn.com/article/2021/1225/e3615255ac2f55e.png" alt="0.png" referrerpolicy="no-referrer"></p><p style="text-align: center;">截图（来自：GitHub）</p><p>据悉，作为 CISA 快速行动小组与开源社区团队的一个衍生项目，log4j-scanner 能够对易受两个 Apache 远程代码执行漏洞影响的 Web 服务进行识别（分别是 CVE-2021-44228 和 CVE-2021-45046)。</p><p><a href="https://static.cnbetacdn.com/article/2021/1225/d2a5c53be232ed2.png" target="_blank"><img src="https://static.cnbetacdn.com/thumb/article/2021/1225/d2a5c53be232ed2.png" alt="1.png" referrerpolicy="no-referrer"></a></p><p>这套扫描解决方案建立在类似的工具之上，包括由网络安全公司 FullHunt 开发的针对 CVE-2021-44228 漏洞的自动扫描框架。</p><p>有需要的安全团队，可借助该工具对网络主机进行扫描，以查找 Log4j RCE 暴露和让 Web 应用程序绕过防火墙（WAF）的潜在威胁。</p><p><a href="https://static.cnbetacdn.com/article/2021/1225/5e8fc7bd29c9635.png" target="_blank"><img src="https://static.cnbetacdn.com/thumb/article/2021/1225/5e8fc7bd29c9635.png" alt="2.png" referrerpolicy="no-referrer"></a></p><p>CISA 在 log4j-scanner 项目主页上介绍了如下功能：</p><blockquote><p>● 支持统一资源定位符（URL）列表。</p><p>● 可对 60 多个 HTTP 请求标头展开模糊测试（不仅限于 3-4 个）。</p><p>● 可对 HTTP POST 数据参数开展模糊测试。</p><p>● 可对 JSON 数据参数开展模糊测试。</p><p>● 支持用于漏洞发现和验证的 DNS 回调。</p><p>● 可筛查有效载荷的防火墙（WAF）绕过。</p></blockquote><div class="article-relation"><p><strong>相关文章:</strong></p><p><a href="https://www.cnbeta.com/articles/tech/1218417.htm" target="_blank">Log4j威胁加剧 美国土安全部宣布拓展HackDHS漏洞赏金计划</a></p></div>   
</div>
            