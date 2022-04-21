
---
title: 'Microsoft Defender又一次误将Google Chrome更新视作可疑活动'
categories: 
 - 新媒体
 - cnBeta
 - 最新
headimg: 'https://static.cnbetacdn.com/article/2022/0421/bf31ec6ead628f2.png'
author: cnBeta
comments: false
date: Thu, 21 Apr 2022 02:28:55 GMT
thumbnail: 'https://static.cnbetacdn.com/article/2022/0421/bf31ec6ead628f2.png'
---

<div>   
近日，我们在 Twitter 和 Reddit 等平台上见到了不少系统管理员报告，<strong>可知问题主要集中在被 Microsoft Defender for Endpoint 安全防护软件标记为“可疑”的 Google Chrome 更新上。</strong>由于谷歌更新服务（GoogleUpdate.exe）没有给“goopdate.dll”这个动态链接库文件签名，Microsoft Defender 也突然变得严格了起来。<br>
 <p><img src="https://static.cnbetacdn.com/article/2022/0421/bf31ec6ead628f2.png" alt="1.png" referrerpolicy="no-referrer"></p><p>在运行 Google Chrome 更新时，Kevin Gary 留意到了 Microsoft Defender 安全防护软件的异常。</p><p>从他分享的日志截图来看，Defender 直接将谷歌更新标记成了恶意软件。</p><p>然后<a data-link="1" href="https://c.duomai.com/track.php?site_id=242986&euid=&t=https://www.microsoftstore.com.cn/" target="_blank">微软</a>最有价值专家 Ota Hirufumi 解释称，官方已确认该问题属于误报，并且已经实施了修复。</p><p><a href="https://static.cnbetacdn.com/article/2022/0421/4af877210679ed5.png" target="_blank"><img src="https://static.cnbetacdn.com/thumb/article/2022/0421/4af877210679ed5.png" alt="2.png" referrerpolicy="no-referrer"></a></p><p>据悉，家庭版（Microsoft Defender for Home）在最近的 AV-Comparatives 和 AV-TEST 横评中的总体表现相当不错。</p><p>尴尬的是，企业版（Microsoft 365 Defender）却总是将切实无害的文件和服务标记为恶意。</p><p><img src="https://static.cnbetacdn.com/article/2022/0421/2b5db822505f5f5.png" alt="3.png" referrerpolicy="no-referrer"></p><p>此外去年 2 月，Defender for Endpoint 就已经误报过一次 Chrome 更新，最近甚至将自家的 <a data-link="1" href="https://microsoft.pvxt.net/P0JMe" target="_blank">Office</a> 更新也打上了恶意软件的标记。</p><p>即使该公司在那次事后发布了一份指南，以减少此类误报。但从实际表现来看，相关措施并未起到实质性的帮助作用。</p>   
</div>
            