
---
title: '安全研究人员利用蓝牙技术骗过COVID-19健康证书应用 篡改其结果'
categories: 
 - 新媒体
 - cnBeta
 - 最新
headimg: 'https://static.cnbetacdn.com/article/2021/1221/f27ef455dd005b9.webp'
author: cnBeta
comments: false
date: Tue, 21 Dec 2021 13:15:08 GMT
thumbnail: 'https://static.cnbetacdn.com/article/2021/1221/f27ef455dd005b9.webp'
---

<div>   
<strong>一名安全研究人员通过在设备到达应用程序之前拦截和修改来自该设备的蓝牙流量，能够改变一个家用COVID-19测试应用的结果，并使这些结果得到认证。</strong>该研究人员Ken
Gannon在Ellume的鼻拭子测试结果认证应用中发现了这个缺陷，该测试旨在分析和传输数据给一个显示和保存结果的配套应用程序。根据甘农咨询的安全公司F-Secure的新闻稿，Ellume现在已经修复了这个问题。<br>
 <p><img src="https://static.cnbetacdn.com/article/2021/1221/f27ef455dd005b9.webp" title alt="img_product_consumer02.0.webp" referrerpolicy="no-referrer"></p><p>伪造结果的过程并不简单，研究人员使用了一个被root的Android设备来窃听和分析测试者发送给应用程序的数据。从那里，Gannon能够确定结果是如何发送的，以及如何验证其真实性。然后，他写了两个脚本，能够成功地将负面结果变为正面结果。他说，当他收到Ellume发来的结果的电子邮件时，它错误地显示他的测试结果为阳性。如果你对技术细节感兴趣，你可以在这里阅读这篇报道：</p><p>Ellume说它遵循了F-Secure的建议，做了更多的分析，以确保数据的准确性，并对应用程序进行了修改，使其更难分析其数据或接管数据传输。他没有测试他的研究是否适用于iOS版本的应用程序，研究目标仅限于"判断一个'普通人'是否能伪造一个阳性/阴性的COVID测试"。他说，从理论上讲，"一个专门的威胁行为者可以利用[他的]研究来修改Ellume应用程序，使其总是报告一个阳性/阴性结果"，且这可以安装在一个没有root的<a data-link="1" href="https://c.duomai.com/track.php?site_id=242986&euid=&t=https://shouji.jd.com/" target="_blank">手机</a>上。</p><p>虽然Gannon的文章只包括将测试结果从阴性改成阳性，但他在F-Secure的新闻稿中说，"这个过程是双向的"。在Ellume的补丁之前，"有适当动机和技术能力的人可以利用这些缺陷来确保他们，或与他们合作的人，在每次测试时得到一个阴性的结果"。</p><p>从理论上讲，人们可以通过这种方法提交一个假的健康证书来满足美国的入境要求。不仅能够让一个不正确的结果得到认证，而且是在视频测试监督员无法发现的情况下做到这一点。</p><p>新闻稿称，Ellume公司现在正在开发一个"验证门户"，让当局验证其测试的真实性，并已回过头来分析其以前的所有结果的准确性。Ellume公司说，暂时没有发现任何一个结果是伪造的。</p>   
</div>
            