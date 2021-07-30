
---
title: '微软发布紧急带外更新：修复Windows 10中打印机问题'
categories: 
 - 新媒体
 - cnBeta
 - 最新
headimg: 'https://static.cnbetacdn.com/thumb/article/2021/0715/e990884b7538193.jpg'
author: cnBeta
comments: false
date: Fri, 30 Jul 2021 02:11:26 GMT
thumbnail: 'https://static.cnbetacdn.com/thumb/article/2021/0715/e990884b7538193.jpg'
---

<div>   
近期，Windows 10 系统报告了多个打印相关的问题。上周微软承认在某些情况下，确实存在影响打印和扫描功能的 BUG，并会对少数设备产生影响。这些问题出现在本月补丁星期二活动日之后，除 Windows 10 之外，Windows 8.1/7 系统也受到影响。<br>
<p style="text-align:center"><a href="https://static.cnbetacdn.com/thumb/article/2021/0715/e990884b7538193.jpg" target="_blank"><img src="https://static.cnbetacdn.com/thumb/article/2021/0715/e990884b7538193.jpg" referrerpolicy="no-referrer"></a></p><p style="text-align: left;">微软现在发布了“针对 CVE-2021-33764 漏洞的加固修复”，微软表示：</p><blockquote style="text-align: left;"><p style="text-align: left;">受影响的设备主要是智能卡认证的打印机、扫描仪和多功能设备，它们不支持 DH 或在 Kerberos AS 请求中宣传支持 des-ede3-cbc（"三重DES"）。</p><p style="text-align: left;">根据 RFC 4556 规范的第 3.2.1 节，为了使这种密钥交换发挥作用，客户必须支持并通知密钥分发中心（KDC）他们对 des-ede3-cbc（"三重 DES"）的支持。</p><p style="text-align: left;">如果客户在加密模式下启动 Kerberos PKINIT，但既不支持也不告诉 KDC 他们支持 des-ede3-cbc（"三重DES"），将被拒绝。</p></blockquote><p style="text-align: left;">目前微软已经发布了适用于 <a data-link="1" href="https://microsoft.pvxt.net/x9Vg1" target="_blank">Windows</a> 10 Version 1809/1607 的紧急带外更新。而其他更新版本的 Windows 10 尚不清楚何时会获得更新。该更新写道：“修复一个可能阻止打印机、扫描仪和多功能设备工作的问题。这个问题发生在不符合某种规范并使用智能卡认证的设备上”。</p>   
</div>
            