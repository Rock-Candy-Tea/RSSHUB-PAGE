
---
title: '戴尔发布BIOSConnect安全漏洞修补程序 影响3000多万台设备'
categories: 
 - 新媒体
 - cnBeta
 - 最新
headimg: 'https://static.cnbetacdn.com/article/2021/0630/037c90e5f8c00c4.jpg'
author: cnBeta
comments: false
date: Wed, 30 Jun 2021 07:58:34 GMT
thumbnail: 'https://static.cnbetacdn.com/article/2021/0630/037c90e5f8c00c4.jpg'
---

<div>   
<strong>上周，MSPU 报道了戴尔远程 BIOS 更新软件正存在的一个漏洞，或导致多达 129 款不同型号的电脑遭遇中间人攻击。</strong>Eclypsium 研究人员解释称，该漏洞使得远程攻击者能够执行多款戴尔笔记本电脑的 BIOS 代码，进而控制设备的启动过程、并打破操作系统和更高层级的安全机制。<br>
 <p><img src="https://static.cnbetacdn.com/article/2021/0630/037c90e5f8c00c4.jpg" referrerpolicy="no-referrer"></p><p>此外 <a href="http://www.eclypsium.com/2021/06/24/biosdisconnect/" target="_self">Eclypsium</a> 指出，受影响的设备数量超过了 3000 万台，并且涵盖了<a data-link="1" href="http://www.anrdoezrs.net/links/9019719/type/dlg/sid//https://www.dell.com/zh-cn/shop/deals" target="_blank">戴尔</a>的消费级 / 商务本、台式机、以及平板电脑产品线。</p><p>至于问题的根源，其实出在戴尔 BIOS 更新软件 —— BIOSConnect 的身上。作为戴尔支持帮助（SupportAssistant）服务的一部分，该公司在大多数 <a data-link="1" href="https://microsoft.pvxt.net/x9Vg1" target="_blank">Windows</a> 设备上都预装了它。</p><blockquote><p>然而在客户机到服务器端的连接过程中，BIOSConnect 使用了不安全的 TLS 连接。结合三个溢出漏洞，使得攻击者能够将特定的软件传送到用户设备上。</p><p>其中两个溢出型的安全漏洞会对操作系统的恢复过程产生影响，而另一个则影响固件的更新过程。但这三个漏洞都是相互独立存在的，最终都可能导致 BIOS 中的任意代码执行。</p></blockquote><p>研究人员建议所有受影响的设备用户手动执行 BIOS 更新，且戴尔官方也应该主动砍掉 BIOSConnect 软件中用不到的功能。</p><p><strong>庆幸的是，目前戴尔已经承认了相关问题，并于今日发布了修补程序。</strong>该公司在支持页面上写道：</p><blockquote><p>DSA-2021-106：这是一项针对戴尔客户端平台的安全更新，旨在修复 BIOSConnect 和 HTTPS 引导功能中的多个漏洞。</p></blockquote><p><strong>下载地址：</strong></p><blockquote><p><a href="https://www.dell.com/support/kbdoc/en-hk/000188682/dsa-2021-106-dell-client-platform-security-update-for-multiple-vulnerabilities-in-the-supportassist-biosconnect-feature-and-https-boot-feature" _src="https://www.dell.com/support/kbdoc/en-hk/000188682/dsa-2021-106-dell-client-platform-security-update-for-multiple-vulnerabilities-in-the-supportassist-biosconnect-feature-and-https-boot-feature" target="_blank">https://www.</a><a data-link="1" href="http://www.anrdoezrs.net/links/9019719/type/dlg/sid//https://www.dell.com/zh-cn/shop/deals" target="_blank">DELL</a>.com/support/kbdoc/en-hk/000188682/dsa-2021-106-dell-client-platform-security-update-for-multiple-vulnerabilities-in-the-supportassist-biosconnect-feature-and-https-boot-feature</p></blockquote>   
</div>
            