
---
title: 'AirTag_丢失模式_存安全漏洞：能引导用户跳转到恶意_钓鱼网站'
categories: 
 - 新媒体
 - cnBeta
 - 最新
headimg: 'https://static.cnbetacdn.com/article/2021/0929/a9a650812259fd8.jpg'
author: cnBeta
comments: false
date: Tue, 28 Sep 2021 23:57:32 GMT
thumbnail: 'https://static.cnbetacdn.com/article/2021/0929/a9a650812259fd8.jpg'
---

<div>   
<strong>根据 <a href="https://krebsonsecurity.com/2021/09/apple-airtag-bug-enables-good-samaritan-attack/" target="_blank">KrebsOnSecurity</a> 分享的一份最新安全报告，苹果允许任何智能手机用户扫描丢失的 AirTag 以定位所有者的联系信息，该功能可能被滥用于网络钓鱼诈骗。</strong>当一个 AirTag 被设置为丢失模式时，它会生成一个 URL“https://found.apple.com”，它让 AirTag 所有者输入联系电话或电子邮件地址。<br>
<p style="text-align: left;">任何扫描该 AirTag 的人都会被自动引导到有主人联系信息的 URL，查看所提供的联系信息不需要登录或个人信息。</p><p style="text-align:center"><img src="https://static.cnbetacdn.com/article/2021/0929/a9a650812259fd8.jpg" alt="j3l1owgy.jpg" referrerpolicy="no-referrer"></p><p style="text-align: left;">据 KrebsOnSecurity 称，丢失模式并不能防止用户在电话号码字段中注入任意的计算机代码，因此扫描 AirTag 的人可能会被转到一个虚假的 iCloud 登录页面或其他恶意网站。不知道查看 AirTag 的信息不需要个人信息的人，可能会被骗提供他们的 iCloud 登录信息或其他个人信息，或者被重定向到试图下载恶意软件。</p><p style="text-align: left;">这个 AirTag 缺陷是由安全顾问 Bobby Raunch 发现的，他告诉 KrebsOnSecurity，该漏洞使 AirTags 变得危险。他说：“我不记得还有另一个例子，像这样低成本的小型消费级追踪设备可以被武器化”。</p><p style="text-align: left;">Rauch 于 6 月 20 日联系了苹果公司，苹果公司花了几个月时间进行调查。苹果上周四告诉罗奇，它将在即将到来的更新中解决这一漏洞，并要求他不要在公开场合谈论这个问题。</p><p style="text-align: left;">苹果公司没有回答他的问题，即他是否会得到奖励，或者他是否有资格参加漏洞赏金计划，所以他决定分享这个漏洞的细节，因为苹果公司缺乏沟通。</p><p style="text-align: left;">Rauch 说：“我告诉他们，如果你们能提供一些细节，说明你们计划何时补救这个问题，以及是否会有任何表彰或漏洞赏金，我愿意与你们合作。但是他们的回应基本上都是‘如果你不泄露这个，我们会很感激’”。</p><p style="text-align: left;">上周，安全研究员丹尼斯·托卡雷夫（Denis Tokarev）在苹果公司忽视他的报告并在几个月内未能修复这些问题后，公开了几个零日的 iOS 漏洞。此后，苹果公司进行了道歉，但该公司因其漏洞赏金计划和对报告的反应迟缓而继续受到批评。</p>   
</div>
            