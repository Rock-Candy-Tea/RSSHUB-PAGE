
---
title: '苹果Mozilla担忧Chrome 94空闲检测API或被滥用'
categories: 
 - 新媒体
 - cnBeta
 - 最新
headimg: 'https://static.cnbetacdn.com/thumb/article/2021/0924/4ff9da786cacb67.png'
author: cnBeta
comments: false
date: Fri, 24 Sep 2021 08:57:18 GMT
thumbnail: 'https://static.cnbetacdn.com/thumb/article/2021/0924/4ff9da786cacb67.png'
---

<div>   
<strong>随着 Chrome 94 浏览器的正式发布，苹果和 Mozilla 都对谷歌引入的一项功能感到担忧，它就是极富争议的“空闲检测”API 。</strong>顾名思义，这项功能允许站点知晓用户是否空间。意味着用户没有与设备、特定的硬件（比如键鼠）、或某些系统事件（例如屏保 / 锁定状态）进行交互。<br>
<p><a href="https://static.cnbetacdn.com/article/2021/0924/4ff9da786cacb67.png" target="_blank"><img src="https://static.cnbetacdn.com/thumb/article/2021/0924/4ff9da786cacb67.png" referrerpolicy="no-referrer"></a></p><p>在该 API 的<a href="https://web.dev/idle-detection/" target="_self">示例</a>中，谷歌介绍了它能够知晓当前联系人（或社交网络站点）是否有空。</p><p>若用户在某段时间内没有交互，即可自动重新启动 kiosk 应用程序。对于那些需要占用昂贵算力的应用程序，亦可借此来限制闲置状态下的资源开销。</p><p>不过在最新的版本中，谷歌已要求网站必须明确获得用户的许可，才能正式调用 Idle Detection API 。</p><p><img src="https://static.cnbetacdn.com/article/2021/0924/8ddf4befd712f6a.gif" referrerpolicy="no-referrer"></p><p>尽管 Chrome 94 已正式集成空闲检测 API，但苹果和 Mozilla 均表示了坚决反对，所以 Firefox 和 Safari 用户暂时不用担心这茬。Mozilla 指出，该 API 存在潜在的滥用状况，或导致基于用户使用模式的监控和操纵。</p><p>Ghacks 赞同了这一观点，即未来不排除有网站会利用粗略的模式估量算法，来秘密地最大化调用本地计算资源（比如某种工作量证明计算），从而在用户知情 / 未同意的情况下浪费电力和硬件寿命。</p><p><img src="https://static.cnbetacdn.com/article/2021/0924/9facc3913091407.png" referrerpolicy="no-referrer"></p><p>苹果 WebKit 团队亦在邮件公告中给予了正式回应，称目前并没有部署该 API 的“足够强大”的用例。</p><p>至于其它基于 Chromium 内核的第三方浏览器，除非开发团队手动剔除或禁用，不然迟早也会引发争议。</p>   
</div>
            