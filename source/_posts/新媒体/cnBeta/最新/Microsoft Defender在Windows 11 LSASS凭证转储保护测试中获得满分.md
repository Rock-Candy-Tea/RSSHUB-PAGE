
---
title: 'Microsoft Defender在Windows 11 LSASS凭证转储保护测试中获得满分'
categories: 
 - 新媒体
 - cnBeta
 - 最新
headimg: 'https://static.cnbetacdn.com/article/2022/0910/6d11e2156dd00c1.jpg'
author: cnBeta
comments: false
date: Fri, 09 Sep 2022 23:55:19 GMT
thumbnail: 'https://static.cnbetacdn.com/article/2022/0910/6d11e2156dd00c1.jpg'
---

<div>   
在过去几个月里，我们一直在报道AV-Comparatives关于Microsoft Defender性能的报告。微软的Windows操作系统内置安全解决方案总体上表现良好，所测试的产品主要是针对家庭用户的。<strong>然而，最近，这家安全评估公司对企业级反恶意软件解决方案进行了LSASS凭证转储保护测试，在被测试的产品中就有微软的Microsoft's Defender for Endpoint，它在评估中获得了满分。</strong><br>
 <p>本地安全授权子系统服务（LSASS）对在<a data-link="1" href="https://microsoft.pvxt.net/x9Vg1" target="_blank">Windows</a>计算机上登录的用户进行认证。威胁者经常利用这个LSASS过程，利用转储从域用户那里窃取有用的凭证，然后可以利用这些证书在目标网络中得到权限自由行动。</p><p>在这次LSASS凭证转储测试中使用了15种不同的攻击方法，Microsoft's Defender for Endpoint很好地阻止了所有这些方法，其他测试产品也同样表现良好。</p><p>下表包括以下产品的结果（启用LSASS保护设置后）：</p><p>Avast Ultimate Business Security、Bitdefender GravityZone Business Security Enterprise、Kaspersky Endpoint Detection and Response Expert和Microsoft Defender for Endpoint。</p><p style="text-align: left;"><strong>Microsoft Defender和其他产品的LSASS凭证转储测试成绩：</strong></p><p><img src="https://static.cnbetacdn.com/article/2022/0910/6d11e2156dd00c1.jpg" title alt="1662758469_lsass_2022_malware_detection_by_ms_defender_and_others_(source-_av_comparatives).jpg" referrerpolicy="no-referrer"></p><p>在Microsoft Defender for Endpoint的情形下，由于Protected Process Light（PPL）和Attack <a data-link="1" href="https://microsoft.pvxt.net/9W473" target="_blank">Surface</a> Reduction（ASR）机制被激活，因此成功地对攻击行为进行了阻断。PPL在Windows 11上被默认启用，最近，用于阻止凭证窃取的ASR规则也被默认启用。</p><p><strong>阅读测试过程全文：</strong></p><p><a href="https://www.av-comparatives.org/lsass-credential-dumping-security/" _src="https://www.av-comparatives.org/lsass-credential-dumping-security/" target="_blank">https://www.av-comparatives.org/lsass-credential-dumping-security/</a><br></p>   
</div>
            