
---
title: 'PrintNightmare漏洞已引起CISA关注 微软表示正积极开展调查'
categories: 
 - 新媒体
 - cnBeta
 - 最新
headimg: 'https://static.cnbetacdn.com/thumb/article/2021/0702/5c654bd22c894cf.jpg'
author: cnBeta
comments: false
date: Fri, 02 Jul 2021 07:41:18 GMT
thumbnail: 'https://static.cnbetacdn.com/thumb/article/2021/0702/5c654bd22c894cf.jpg'
---

<div>   
虽然每月的补丁星期二活动微软都会发布一系列安全更新，但依然存在“漏网之鱼”。日前，国内安全公司深信服（Sangfor）发现了名为 PrintNightmare 的零日漏洞，允许黑客在补丁完善的 Windows Print Spooler 设备上获得完整的远程代码执行能力。<strong>该漏洞已引起美国网络安全和基础设施安全局（CISA）的关注，微软正在积极开展调查。</strong><br>
<p style="text-align:center"><a href="https://static.cnbetacdn.com/article/2021/0702/5c654bd22c894cf.jpg" target="_blank"><img src="https://static.cnbetacdn.com/thumb/article/2021/0702/5c654bd22c894cf.jpg" alt="842d05fk.jpg" referrerpolicy="no-referrer"></a></p><p style="text-align: left;">CISA 将 PrintNightmare 漏洞描述为“关键漏洞”（Critical），因为它可以远程执行代码。CERT 协调中心在 VU#383432 下对其进行跟踪，并解释说，问题的发生是因为 <a data-link="1" href="https://microsoft.pvxt.net/x9Vg1" target="_blank">Windows</a> Print Spooler 服务没有限制对 RpcAddPrinterDriverEx() 函数的访问，这意味着经过远程验证的攻击者可以利用它来运行任意代码。这种任意代码的执行是在SYSTEM的幌子下进行的。</p><p style="text-align: left;">作为参考，这个有问题的函数通常用于安装打印机驱动程序。然而，由于远程访问是不受限制的，这意味着有动机的攻击者可以使它指向远程服务器上的驱动程序，使受感染的机器以SYSTEM权限执行任意代码。</p><p style="text-align: left;">值得注意的是，微软在6月的 "补丁星期二 "更新中修复了CVE-2021-1675的相关问题，但最新的进展并不在修复范围内。该公司表示，它正在积极调查这个问题，并为域名管理员提出了两个解决方法。第一个是禁用 Windows Print Spooler 服务，但这意味着本地和远程的打印都将被禁用。第二种是通过组策略禁用入站远程打印。这将限制远程打印，但本地打印仍将正常工作。</p><p style="text-align: left;">微软正在以CVE-2021-34527追踪该漏洞。该公司明确表示，有问题的代码存在于所有版本的Windows中，但它仍在调查它是否也可以在所有版本中被利用。也就是说，由于该问题正在积极调查中，微软还没有给它一个漏洞评分，但也将其标记为 "关键"。</p><div class="article-relation"><p><strong>相关文章:</strong></p><p><a href="https://www.cnbeta.com/articles/tech/1147467.htm" target="_blank">零日漏洞PrintNightmare曝光：可在Windows后台执行远程代码</a></p></div>   
</div>
            