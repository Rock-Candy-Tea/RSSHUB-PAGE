
---
title: '苹果iCloud、推特和《我的世界》均易受Log4Shell零日漏洞影响'
categories: 
 - 新媒体
 - cnBeta
 - 最新
headimg: 'https://static.cnbetacdn.com/article/2021/1211/13619f62a455b85.png'
author: cnBeta
comments: false
date: Sat, 11 Dec 2021 02:55:28 GMT
thumbnail: 'https://static.cnbetacdn.com/article/2021/1211/13619f62a455b85.png'
---

<div>   
<strong>近日有报道称，包括苹果 iCloud、推特、Cloudflare、《我的世界》、以及 Steam 等在内的诸多热门服务，均易受到一个零日漏洞的影响。</strong>Luna Sec 安全研究人员将这个存在于流行的 Java 日志库中的零日漏洞利用称作“Log4Shell”，且已在 Apache Log4j 中发现。后者是一款开源的日志实用程序，且被大量应用程序、网站和相关服务所采用。<br>
 <p><img src="https://static.cnbetacdn.com/article/2021/1211/13619f62a455b85.png" referrerpolicy="no-referrer"></p><p style="text-align: center;">（来自：<a href="https://www.lunasec.io/docs/blog/log4j-zero-day/" target="_self">Luna Sec</a>）</p><p>起初，研究人员仅在<a data-link="1" href="https://c.duomai.com/track.php?site_id=242986&euid=&t=https://www.microsoftstore.com.cn/" target="_blank">微软</a>旗下的《我的世界》中发现了“Log4Shell”。但由于 Log4j 在几乎所有基于 Java 的企业应用程序 / 服务器中“无处不在”，这一零日漏洞的影响范围还是难以估量的。</p><p><strong>Luna Sec 安全研究人员在一篇博客文章中警告称：任何使用 Apache Struts 的地方，都可能易受此类攻击。</strong></p><blockquote><p>目前已被证实易受影响的服务器，已波及<a data-link="1" href="https://apple.pvxt.net/c/1251234/435400/7639?u=https%3A%2F%2Fwww.apple.com%2Fcn%2Fmusic%2F" target="_blank">苹果</a>、亚马逊、Cloudflare、推特、Steam、百度、网易、腾讯、Elastic 等科技巨头。</p><p>庆幸的是，尽管另有成千上万的其它组织尚未列出，但在致外媒的一份声明中，Cloudflare 表示其已给系统打上了更新补丁，且尚未发现任何有被利用的证据。</p><p>此外《我的世界》游戏开发商 Mojang 工作室已通过紧急发布的安全更新而修复了该错误。</p><p>Apache 软件基金会也于今日发布了紧急安全更新，并为无法立即启用更新的客户提供了缓解方案。</p></blockquote><p>美国国家安全局网络安全主管 Robert Joyce 证实，该机构开发的免费开源逆向工程工具 GHIDRA 也受到了影响：“由于广泛包含在软件框架中，Log4j 是一个相当重大的漏洞利用威胁”。</p><p>新西兰计算机紧急响应小组（CERT）、德国电信 CERT 和 Greynoise 网络监控服务均发出警告 —— 攻击者正在积极寻找易受 Log4Shell 攻击的服务器，约有 100 台不同的主机正在对互联网展开扫描。</p><p>最后，HackerOne 高级安全技术专家 Kayla Underkoffler 指出 —— 随着开源软件在全球关键供应链中所占的比例越来越大，其遭遇此类攻击威胁的位面也在与日俱增。</p>   
</div>
            