
---
title: 'Microsoft Defender再被发现造成操作系统高内存使用率、黑屏等问题'
categories: 
 - 新媒体
 - cnBeta
 - 最新
headimg: 'https://static.cnbetacdn.com/article/2022/0501/d8489fba6d11a77.png'
author: cnBeta
comments: false
date: Sun, 01 May 2022 09:01:36 GMT
thumbnail: 'https://static.cnbetacdn.com/article/2022/0501/d8489fba6d11a77.png'
---

<div>   
Microsoft Defender for Endpoint显然给Windows 10
20H2上的一些客户系统带来了一些重大问题。该报告来自Borncity，他们已经观察到这些问题将近一个月了。以下是该网站报告的Defender
for Endpoint正在导致的问题清单：<br>
<blockquote><p>非常高的内存使用率</p><p>登录后系统出现黑屏问题（延迟两分钟或更长时间）</p><p>导致Word 2016和更新版本无法打开或需要很长的时间才能打开</p><p>Windows事件查看器需要很长的时间来显示事件（包括远程以及本地）。</p></blockquote><p>高内存使用率的问题很可能是由内存泄漏的错误引起的。这个问题显然不是新问题，微软早些时候曾修复过一次该问题。</p><p><img src="https://static.cnbetacdn.com/article/2022/0501/d8489fba6d11a77.png" title alt="图片.png" referrerpolicy="no-referrer"></p><p><a href="https://static.cnbetacdn.com/article/2022/0501/8b2f1b141774b9c.png" target="_blank"><img src="https://static.cnbetacdn.com/thumb/article/2022/0501/8b2f1b141774b9c.png" title alt="FQSaovpXwAMXMx1.png" referrerpolicy="no-referrer"></a></p><p>微软公司表示，这个问题从签名版1.363.177.0开始出现。然而，在修正了这个错误以后，问题显然又回来了，看起来早些时候的解决可能只是暂时的。</p><p>Microsoft Defender的"反恶意软件服务可执行程序"（MsMpEng.exe）的高内存使用率是一个相当常见的错误，有时减少内存消耗的临时解决方法是禁用软件当中的实时保护。</p><p><strong>了解更多：</strong></p><p><a href="https://www.borncity.com/blog/2022/04/30/defender-for-endpoint-verursacht-probleme-bei-windows-10-20h2-clients-26-april-2022/" _src="https://www.borncity.com/blog/2022/04/30/defender-for-endpoint-verursacht-probleme-bei-windows-10-20h2-clients-26-april-2022/" target="_blank">https://www.borncity.com/blog/2022/04/30/defender-for-endpoint-verursacht-probleme-bei-windows-10-20h2-clients-26-april-2022/</a><br></p>   
</div>
            