
---
title: '安卓开发者发现华为 AppGallery 漏洞，可免费下载付费应用'
categories: 
 - 新媒体
 - IT 之家
 - 热榜
headimg: 'https://img.ithome.com/newsuploadfiles/2022/5/b570af01-0af8-4939-96a0-249912d3a95b.png'
author: IT 之家
comments: false
date: Thu, 19 May 2022 00:07:37 GMT
thumbnail: 'https://img.ithome.com/newsuploadfiles/2022/5/b570af01-0af8-4939-96a0-249912d3a95b.png'
---

<div>   
<p data-vmark="8449"><a class="s_tag" href="https://www.ithome.com/" target="_blank">IT之家</a> 5 月 19 日消息，自从美国禁令之后，华为新机便失去了对谷歌 GMS 服务的提供。因此，华为不得不投入更多资源开发自己的软件商店和配套服务 —— 华为移动服务 (HMS) 以便在其自家手机上使用，其中就包括华为 AppGallery。</p><p data-vmark="a0c8">当然，既然是对标 Play 商店，那么 AppGallery 应用商店的意义不仅仅在于推广软件，还包括为付费游戏创收等。但现在有开发者发现了一个华为 AppGallery 漏洞，用户可以藉此免费下载付费 App。</p><p data-vmark="5866">Android 开发者 @Dylan Roussel 在探索 AppGallery 商店 API 时发现了一个漏洞，华为通过这一接口返回（与数据请求对应）免费和付费应用程序的 APK 下载链接，而华为 AppGallery 的底层 API 没有为付费应用程序提供任何保护。</p><p data-vmark="8d3b" style="text-align: center;"><img src="https://img.ithome.com/newsuploadfiles/2022/5/b570af01-0af8-4939-96a0-249912d3a95b.png" w="912" h="775" title="安卓开发者发现华为 AppGallery 漏洞，可免费下载付费应用" width="912" height="697" referrerpolicy="no-referrer"></p><p data-vmark="754f">他尝试了一下，最终发现用户无需为某个特定应用付费，甚至无需登录帐户就可以获得付费应用的有效下载链接。他表示，这个漏洞可以帮助他人轻松下载盗版 App，安装和使用时也没遇到任何麻烦。</p><p data-vmark="852b">为了确保这不是一个 App 的许可证验证问题，他还对多个应用程序重复了这一过程 —— 结果表明其他 App 都是一样的反应，证实这一漏洞确实在于华为方面。</p><p data-vmark="6fbe">他最初于今年 2 月份发现了这一漏洞，随后联系华为方面进行反馈。按照业界规矩，他给了华为 5 周的时间来修复这一漏洞，华为也已经意识到该漏洞并承认了这一点。在 13 周之后，他决定公开这一发现，不过华为仍未公布该漏洞是否已经修复的报告或给出计划修复的时间安排。</p><p data-vmark="e951">IT之家提醒，华为 AppGallery 程序开发人员目前最好的解决办法是确保你的 App 拥有 DRM 保护，例如 AppGallery DRM 服务。它会在用户打开 App 时检查他们是否购买该应用，而且这也是确保应用不会被二次分发给他人的好方法。</p>
          
</div>
            