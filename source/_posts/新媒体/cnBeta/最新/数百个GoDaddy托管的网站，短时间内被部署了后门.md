
---
title: '数百个GoDaddy托管的网站，短时间内被部署了后门'
categories: 
 - 新媒体
 - cnBeta
 - 最新
headimg: 'https://static.cnbetacdn.com/article/2022/0317/843c27544458986.jpg'
author: cnBeta
comments: false
date: Thu, 17 Mar 2022 07:00:15 GMT
thumbnail: 'https://static.cnbetacdn.com/article/2022/0317/843c27544458986.jpg'
---

<div>   
Bleeping Computer 网站披露，网络安全分析师发现 GoDaddy 管理服务器上托管的部分 WordPress 网站，被部署了大量后门，所有网站都具有相同的后门有效载荷。<br>
 <p style="text-align:center"><img src="https://static.cnbetacdn.com/article/2022/0317/843c27544458986.jpg" referrerpolicy="no-referrer"></p><p style="text-align: left;">据悉，这次网络攻击可能影响到许多互联网服务经销商，已知的包括 MediaTemple、tsoHost、123Reg、Domain Factory、Heart Internet和Host Europe Managed WordPress 等。</p><p style="text-align: left;">2022 年 2 月 11 日，Wordfenc 安全团队首次观察到此次恶意活动。经过一段时间追踪，发现 24 小时内约有 298 个网站感染后门，其中 281 个网站托管在 GoDaddy。</p><p style="text-align:center"><img src="https://static.cnbetacdn.com/article/2022/0317/75d127699e49643.jpg" referrerpolicy="no-referrer"></p><p style="text-align: left;">网络安全研究员透漏，感染后门的网站允许攻击者从 C2 中获取垃圾邮件链接模板，用于将恶意网页注入到用户搜索结果中，进行虚假宣传，诱导受害者购买假冒产品。</p><p style="text-align: left;">此外，攻击者还能够通过更改网站内容等明显违规行为，损害网站声誉，但这些似乎都不是威胁者最终目的。</p><p style="text-align: left;">糟糕的是，这种模式的网络攻击发生在服务器上而不是浏览器上，很难从用户端检测到和阻止，因此本地网络安全工具不会检测到任何可疑的东西。</p><p style="text-align: left;"><strong><strong>供应链攻击</strong></strong></p><p style="text-align: left;">此次网络攻击的入侵载体还没有得到确定，虽然看起来很接近供应链攻击，但目前不能证实。</p><p style="text-align: left;">无论如何，如果用户的网站托管在GoDaddy的WordPress管理平台上，请务必尽快扫描wp-config.php文件，查找潜在的后门注入。</p><p style="text-align:center"><img src="https://static.cnbetacdn.com/article/2022/0317/24f36be8ca3ea0f.jpg" referrerpolicy="no-referrer"></p><p style="text-align: left;">值得注意的是，2021 年 11 月，GoDaddy 披露一起数据泄露事件，影响范围涵盖 120 万客户和多个WordPress 管理服务经销商，包含上文提到的六个。</p><p style="text-align: left;">Bleeping Computer 已经联系了 GoDaddy，期望获取更多关于攻击活动的信息，但没有收到回复。</p><p style="text-align: left;"><strong>参考文章：</strong></p><blockquote style="text-align: left;"><p style="text-align: left;">https://www.bleepingcomputer.com/news/security/hundreds-of-godaddy-hosted-sites-backdoored-in-a-single-day/</p></blockquote>   
</div>
            