
---
title: 'Google SMTP服务被利用来发送欺诈邮件'
categories: 
 - 新媒体
 - cnBeta
 - 最新
headimg: 'https://static.cnbetacdn.com/article/2022/05/4499e616cc5ee57.jpg'
author: cnBeta
comments: false
date: Mon, 02 May 2022 13:12:16 GMT
thumbnail: 'https://static.cnbetacdn.com/article/2022/05/4499e616cc5ee57.jpg'
---

<div>   
我们中的大多数人不会过多地考虑我们的电子邮件上的"发件人"地址栏，它通常是由邮件程序或网络服务填写的。在收件人的一端，安全工具可以对照发送服务器检查这个地址，以验证邮件是否合法。<strong>但服务器和收件箱之间的SMTP中转服务器会允许邮件通过，即使地址不匹配，这就是为什么一些营销组织可以在不被阻止的情况下发送群发邮件。</strong><br>
<p><a href="https://static.cnbetacdn.com/article/2022/05/4499e616cc5ee57.jpg" target="_blank"><img src="https://static.cnbetacdn.com/article/2022/05/4499e616cc5ee57.jpg" referrerpolicy="no-referrer"></a></p><p><a href="https://static.cnbetacdn.com/article/2022/05/0662eb12ce969bc.jpg" target="_blank"><img src="https://static.cnbetacdn.com/article/2022/05/0662eb12ce969bc.jpg" referrerpolicy="no-referrer"></a></p><p>而Gmail恰好有SMTP中转设施，使得通过Google服务器发送非Gmail邮件成为可能。Avanan公司的研究人员发现，黑客正在操纵Google的服务，伪装成有信誉的品牌，发送成千上万的电子邮件，绕过安全工具，直接进入用户的收件箱。黑客正在利用GoogleSMTP中继服务的一个缺陷来发送钓鱼邮件，这些邮件更有可能不受干扰的情况下到达被骚扰者的收件箱中。Avanan公司观察到此类攻击的数量大量增加，在4月的短短两周内就有超过27000封此类邮件经由这种方式发送。<br></p><p>Google于4月23日被告知该漏洞。为了防范攻击，安全研究人员建议在与任何电子邮件互动之前检查发件人地址，使用电子邮件安全解决方案，使用多种指标来确定邮件是否是恶意的，并且在点击任何链接之前，总是将鼠标悬停在其上，以查看目标URL。</p><p>了解更多：</p><p><a href="https://www.avanan.com/blog/the-gmail-smtp-relay-service-exploit" _src="https://www.avanan.com/blog/the-gmail-smtp-relay-service-exploit" target="_blank">https://www.avanan.com/blog/the-gmail-smtp-relay-service-exploit</a><br></p>   
</div>
            