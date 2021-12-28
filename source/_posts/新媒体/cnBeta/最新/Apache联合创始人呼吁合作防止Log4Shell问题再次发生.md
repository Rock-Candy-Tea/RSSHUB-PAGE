
---
title: 'Apache联合创始人呼吁合作防止Log4Shell问题再次发生'
categories: 
 - 新媒体
 - cnBeta
 - 最新
headimg: 'https://static.cnbetacdn.com/article/2021/1228/21cc0cf39bdde99.webp'
author: cnBeta
comments: false
date: Tue, 28 Dec 2021 08:41:59 GMT
thumbnail: 'https://static.cnbetacdn.com/article/2021/1228/21cc0cf39bdde99.webp'
---

<div>   
<strong>Apache Web 服务器的主要开发人员布莱恩·贝伦多夫（Brian Behlendorf）近日发布文章，呼吁多个开源基金会紧密合作，防止 Log4Shell 此类问题再次发生。</strong>文章中提及了目前开源领域安全工作资源不足，在制定标准和要求以减少重大漏洞的机会方面受到束缚，并提出了几个建议来减轻安全风险。<br>
 <p style="text-align:center"><img src="https://static.cnbetacdn.com/article/2021/1228/21cc0cf39bdde99.webp" alt="x5o7enpn.webp" referrerpolicy="no-referrer"></p><p style="text-align: center;">图片来自于 Flickr</p><p style="text-align: left;">为防止 Log4Shell 此类问题再次发生，Brian Behlendorf 倡议开源软件基金会们可以做以下几件事，以减轻安全风险：</p><p style="text-align: left;">● 建立一个组织范围内的安全团队，接收和分流漏洞报告，以及协调对其他受影响项目和组织的回应和披露。</p><p style="text-align: left;">● 通过CI工具执行频繁的安全扫描，以检测软件中的未知漏洞并识别依赖关系中的已知漏洞。</p><p style="text-align: left;">● 对关键代码进行不定期的外部安全审计，特别是在新的重大发布之前。</p><p style="text-align: left;">● 要求项目使用测试框架，并确保较高的代码覆盖率，这样就可以阻止没有测试的功能，并主动淘汰未被使用的功能。</p><p style="text-align: left;">● 要求项目删除已废弃或易受影响的依赖关系。(一些Apache项目没有受到Log4j v2 CVE的影响，因为他们仍在使用Log4j v1，该版本有已知的弱点，并且自2015年以来没有得到更新！)</p><p style="text-align: left;">● 鼓励并最终要求使用SBOM格式，如SPDX，以帮助每个人更容易和快速地跟踪依赖关系，从而使漏洞更容易被发现和修复。</p><p style="text-align: left;">● 鼓励并最终要求维护者展示对安全软件开发实践基础知识的熟悉程度。</p><p style="text-align: left;">其中的许多内容都被纳入了CII最佳实践徽章中，这是将这些内容编入客观可比的指标的首次尝试之一，这项工作现在已经转移到OpenSSF。OpenSSF还为开发者发布了一个关于如何开发安全软件的免费课程，而SPDX最近也被公布为ISO标准。</p>   
</div>
            