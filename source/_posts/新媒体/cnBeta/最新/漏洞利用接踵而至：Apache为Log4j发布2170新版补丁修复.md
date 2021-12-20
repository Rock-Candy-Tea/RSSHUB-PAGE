
---
title: '漏洞利用接踵而至：Apache为Log4j发布2.17.0新版补丁修复'
categories: 
 - 新媒体
 - cnBeta
 - 最新
headimg: 'https://static.cnbetacdn.com/thumb/article/2021/1220/887fd460af17f78.jpg'
author: cnBeta
comments: false
date: Mon, 20 Dec 2021 10:47:43 GMT
thumbnail: 'https://static.cnbetacdn.com/thumb/article/2021/1220/887fd460af17f78.jpg'
---

<div>   
在 Log4j 漏洞曝光之后，Apache 软件基金会于上周二发布了修补后的 2.17.0 新版本，并于周五晚些发布了一个新补丁。<strong>官方承认 2.16 版本无法在查找评估中妥善防止无限递归，因而易受 CVE-2021-45105 攻击的影响。</strong>据悉，这个拒绝服务（DoS）攻击的威胁级别相当之高，CVSS 评分达到了 7.5 / 10 。<br>
 <p><a href="https://static.cnbetacdn.com/article/2021/1220/887fd460af17f78.jpg" target="_blank"><img src="https://static.cnbetacdn.com/thumb/article/2021/1220/887fd460af17f78.jpg" referrerpolicy="no-referrer"></a></p><p style="text-align: center;">截图（via <a href="https://www.bleepingcomputer.com/news/security/upgraded-to-log4j-216-surprise-theres-a-217-fixing-dos/" target="_self">Bleeping Computer</a>）</p><p>具体说来是，Apache Log4j2 的 2.0-alpha1 到 2.16.0 版本，均未能防止自引用查找的不受控递归。</p><p>当日志配置使用了带有上下文查找的非默认模式布局时（例如 <strong>$$&#123;ctx:loginId&#125;</strong>），控制线程上下文映射（MDC）数据输入的攻击者，便可制作一份包含递归查找的恶意输入数据，从而导致进程因堆栈溢出报错而被终止。</p><p>时隔三天冒出的新问题，是由 Akamai Technologies 的 Hideki Okamoto 和另一位匿名漏洞研究人员所发现的 —— 此类攻击又被称作 DoS（拒绝服务）。</p><p>缓解措施包括部署 2.17.0 补丁，并将诸如 <strong>$&#123;ctx:loginId&#125;</strong> 或 <strong>$$&#123;ctx:loginId&#125;</strong> 之类的上下文查找，替换为日志记录配置中 PatternLayout 线程的上下文映射模式（如 <strong>%X</strong>、<strong>%mdc</strong> 或 <strong>%MDC</strong>）。</p><p>Apache 还建议在 <strong>$&#123;ctx:loginId&#125;</strong> 或 <strong>$$&#123;ctx:loginId&#125;</strong> 等配置中，删除对上下文查找的引用 —— 它们源于应用程序的外部，比如 HTTP 标头或用户输入。</p><p>庆幸的是，只有 Log4j 的核心 JAR 文件，受到了 CVE-2021-45105 漏洞的的影响。</p><p><a href="https://static.cnbetacdn.com/article/2021/1220/0d47a16badc1ece.png" target="_blank"><img src="https://static.cnbetacdn.com/thumb/article/2021/1220/0d47a16badc1ece.png" referrerpolicy="no-referrer"></a></p><p style="text-align: center;">（图 via <a href="https://security.googleblog.com/2021/12/understanding-impact-of-apache-log4j.html" target="_self">Google Security Blog</a>）</p><p>周五的时候，网络安全研究人员开始发布有关 2.16.0 潜在问题的推文，且其中一些人确定了拒绝服务（DoS）漏洞。</p><p>美国网络安全和基础设施安全局（CISA）提出了多项紧急建议，要求联邦机构尽快在圣诞节前落实补丁修复。</p><p>与此同时，IBM、思科、VMware 等科技巨头，也在争分夺秒地修复自家产品中的 Log4j 漏洞。</p><p>第二波惶恐源于安全公司 Blumira 发现的另一种 Log4j 攻击，其能够利用机器或本地网络上的侦听服务器来发起攻击。</p><p>在此之前，许多人误以为 Log4j 漏洞仅限于暴露的易受攻击的服务器。而 Conti 之类的勒索软件组织，也在积极探索此类漏洞利用方法。</p><div class="article-relation"><p><strong>相关文章:</strong></p><p><a href="https://www.cnbeta.com/articles/tech/1216701.htm" target="_blank">谷歌开源洞察团队详解Apache Log4j漏洞造成的广泛影响</a></p></div>   
</div>
            