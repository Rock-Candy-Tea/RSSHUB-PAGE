
---
title: '网络安全专家发现由微软 WHQL 签名的 FiveSys 驱动其实是伪装的恶意软件'
categories: 
 - 新媒体
 - IT 之家
 - 分类资讯
headimg: 'https://img.ithome.com/newsuploadfiles/2021/10/120fc999-1c5e-4862-a9ec-445b97bd9ec6.jpeg'
author: IT 之家
comments: false
date: Fri, 22 Oct 2021 10:08:10 GMT
thumbnail: 'https://img.ithome.com/newsuploadfiles/2021/10/120fc999-1c5e-4862-a9ec-445b97bd9ec6.jpeg'
---

<div>   
<p data-vmark="bbf1"><a class="s_tag" href="https://www.ithome.com/" target="_blank">IT之家</a> 10 月 22 日消息，近日比特梵德（Bitdefender）的安全研究人员发现了一个由微软自己进行数字签名的新型 rootkit 恶意驱动程序，名为 FiveSys。此恶意驱动程序带有“Windows 硬件质量实验室”（WHQL）认证，<span class="accentTextColor">该认证由微软通过 Windows 硬件兼容计划（WHCP）对其各合作厂商送来的驱动程序进行核查后发布。</span></p><p data-vmark="19f9"><img src="https://img.ithome.com/newsuploadfiles/2021/10/120fc999-1c5e-4862-a9ec-445b97bd9ec6.jpeg" w="1182" h="776" title="网络安全专家发现由微软 WHQL 签名的 FiveSys 驱动其实是伪装的恶意软件" width="1182" height="538" referrerpolicy="no-referrer"></p><p data-vmark="d480">比特梵德解释了 FiveSys rootkit 恶意驱动程序感染的原理以及它的功能：“rootkit 的原理相当简单，其目的是通过一个自定义代理来重定向受感染机器中的互联网流量，此代理是从一个内置 300 个域名的列表中提取出来的，这种重定向对 HTTP 和 HTTPS 都有效。Rootkit 在 HTTPS 进行重定向工作时向其安装了一个自定义的根证书，这样一来，<a class="s_tag" href="https://qiyu.ruanmei.com/" target="_blank">浏览器</a>就不会对该代理服务器的未知身份发出警告。”</p><p data-vmark="9796">IT之家了解到，到目前为止，FiveSys 恶意驱动程序的传播区域只限于中国，这可能表明其散布者主要对中国感兴趣。在其他关键特征方面，相关白皮书还提到，<span class="accentTextColor">该 rootkit 阻止用户进行注册表的修改，并试图阻止其访问受感染的系统。</span></p><p data-vmark="3297">除了重定向互联网流量，该 rootkit 还阻止其他恶意程序编写组的驱动程序在受感染电脑上进行加载，可能该恶性程序正在限制其他的恶性程序进入被感染的系统。</p><p data-vmark="9c2b"><img src="https://img.ithome.com/newsuploadfiles/2021/10/baf4592b-5548-40f6-bff3-16b78898a85e.png" w="495" h="349" title="网络安全专家发现由微软 WHQL 签名的 FiveSys 驱动其实是伪装的恶意软件" width="495" height="349" referrerpolicy="no-referrer"></p><p data-vmark="c719">比特梵德在提醒微软后，微软就将该恶性驱动程序上的签名删除了，用户可以在这篇比特梵德的<a href="https://www.bitdefender.com/blog/hotforsecurity/the-emergence-of-the-fivesys-rootkit-a-malicious-driver-signed-by-microsoft/" target="_blank">官方博客文章</a>中了解详情。</p><p data-vmark="0b5c">有趣的是，这并不是微软第一次发生这样的事情。在今年 6 月，一个名为“Netfilter”的恶性程序也通过了微软的 WHQL 签名认证，所感染电脑的方法可能与此次类似。</p>
          
</div>
            