
---
title: '微软紧急发布带外更新 修复PrintNightmare高危打印漏洞'
categories: 
 - 新媒体
 - cnBeta
 - 最新
headimg: 'https://static.cnbetacdn.com/thumb/article/2021/0707/e73488bdb44e5b3.jpg'
author: cnBeta
comments: false
date: Wed, 07 Jul 2021 02:07:28 GMT
thumbnail: 'https://static.cnbetacdn.com/thumb/article/2021/0707/e73488bdb44e5b3.jpg'
---

<div>   
<strong>微软今天推出了一个紧急 Windows 修复补丁，以修复存在于 Windows Print Spooler 服务中的一个关键缺陷。</strong>该漏洞被称之为“PrintNightmare”，在安全研究人员无意中公布了概念验证（PoC）的利用代码后，于上周被曝光。<br>
<p style="text-align: left;">访问：<a href="https://msrc.microsoft.com/update-guide/vulnerability/CVE-2021-34527" target="_blank">微软更新</a><br style="text-align: left;"></p><p style="text-align: left;">微软已经发布了带外安全更新以解决该漏洞，并将其评为关键漏洞，因为攻击者可以在受影响机器上以系统级权限远程执行代码。由于 <a data-link="1" href="https://microsoft.pvxt.net/x9Vg1" target="_blank">Windows</a> Print Spooler 服务在Windows上默认运行，微软不得不为 Windows Server 2019、Windows Server 2012 R2、Windows Server 2008、Windows 8.1、Windows RT 8.1 以及 Windows 10 的各种支持版本发布补丁。</p><p style="text-align:center"><a href="https://static.cnbetacdn.com/article/2021/0707/e73488bdb44e5b3.jpg" target="_blank"><img src="https://static.cnbetacdn.com/thumb/article/2021/0707/e73488bdb44e5b3.jpg" alt="QQ截图20210707100357.jpg" referrerpolicy="no-referrer"></a></p><p style="text-align: left;">微软甚至采取了不寻常的措施，为去年正式停止支持的 Windows 7 发布了补丁。不过，微软还没有为 Windows Server 2012、Windows Server 2016 和 Windows 10 Version 1607 发布补丁。微软表示，"这些版本的Windows的安全更新将很快发布"。</p><p style="text-align: left;">PrintNightmare，在漏洞代号CVE-2021-34527下被追踪，现在已被授予通用漏洞评分系统（CVSS）基本评级为8.8。值得注意的是，CVSS v3.0规范文件将其定义为 "高严重性"漏洞，但它非常接近从9.0开始的"危急"评级。目前的时间紧迫性得分是8.2，时间分是根据一些因素来衡量一个漏洞的当前可利用性。</p><p style="text-align: left;">基础分被定为8.8分是因为微软已经确定该攻击载体是在网络层面，需要较低的攻击复杂性和权限，不涉及用户互动，并可能导致组织资源的保密性、完整性和可用性 "完全丧失"。同时，时间分是8.2分是因为功能上的漏洞代码在互联网上很容易获得，并且适用于所有版本的Windows，存在关于它的详细报告，并且有一些官方的补救方法被建议。</p><div class="article-relation"><p><strong>相关文章:</strong></p><p><a href="https://www.cnbeta.com/articles/tech/1148199.htm" target="_blank">0patch发布拯救Windows PrintNightmare漏洞的免费微补丁</a></p><p><a href="https://www.cnbeta.com/articles/tech/1148301.htm" target="_blank">微软警告攻击者正肆意利用Windows PrintNightmare漏洞</a></p><p><a href="https://www.cnbeta.com/articles/tech/1148659.htm" target="_blank">微软为PrintNightmare漏洞提供进一步的缓解措施 将其评级为 "高严重性"</a></p></div>   
</div>
            