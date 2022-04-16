
---
title: 'Google发布紧急更新 修复Chromium浏览器的2个漏洞'
categories: 
 - 新媒体
 - cnBeta
 - 最新
headimg: 'https://static.cnbetacdn.com/article/2022/0416/9f60f3779b90798.webp'
author: cnBeta
comments: false
date: Sat, 16 Apr 2022 01:01:48 GMT
thumbnail: 'https://static.cnbetacdn.com/article/2022/0416/9f60f3779b90798.webp'
---

<div>   
<strong>在最新发布的紧急更新中，Google 修复了 Chrome 浏览器的 2 个漏洞，其中 1 个漏洞已经被证明被黑客利用。</strong>本周发布的紧急更新不仅适用于拥有 30 亿活跃用户的 Chrome 浏览器，还同样适用于 Edge、Brave 和 Vivaldi 等基于 Chromium 的浏览器。<br>
 <p style="text-align:center"><img src="https://static.cnbetacdn.com/article/2022/0416/9f60f3779b90798.webp" referrerpolicy="no-referrer"></p><p style="text-align:center"><img src="https://static.cnbetacdn.com/article/2022/0416/b2cd6e992a9de41.webp" referrerpolicy="no-referrer"></p><p style="text-align: left;">其中 1 个漏洞被追踪为 CVE-2022-1364，是类型混淆漏洞，这是一个高严重性的零日漏洞，正被攻击者积极滥用。Google在其警报中指出，该漏洞是Chromium V8的类型混乱，影响到浏览器中使用的JavaScript引擎。</p><p style="text-align: left;">在类型混淆漏洞中，程序将使用一种类型分配资源，如指针或对象，但随后将使用另一种不兼容的类型访问该资源。在某些语言中，如 C 和 C++，该漏洞会导致越界内存访问。</p><p style="text-align: left;">这种不兼容会导致浏览器崩溃或引发逻辑错误。它有可能被利用来执行任意代码。</p><p style="text-align: left;">互联网安全中心称：“根据与该应用程序相关的权限，攻击者可以查看、改变或删除数据。如果这个应用程序被配置为在系统上有较少的用户权限，利用这个漏洞最严重的影响可能比它被配置为管理权限的影响要小”。</p><p style="text-align: left;">隶属于Google威胁分析小组（TAG）的克莱门特·勒西涅（Clement Lecigne）于4月13日报告了该漏洞，该公司在同一天宣布了修复措施。Google 在警报中写道：“Google 知道 CVE-2022-1364 的漏洞已经被黑客利用”。</p><p style="text-align: left;">Google官员没有公布有关该漏洞的许多细节，他们说有关该漏洞的信息和链接被限制，直到大多数用户更新了修复程序，这将使Chrome浏览器在<a data-link="1" href="https://microsoft.pvxt.net/x9Vg1" target="_blank">Windows</a>、Linux和Mac平台上达到100.0.4896.127版本。他们还说，"如果该错误存在于其他项目同样依赖的第三方库中，但尚未修复，他们将保留限制。"</p>   
</div>
            