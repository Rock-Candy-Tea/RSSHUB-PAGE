
---
title: '苹果 iPhone 再现 Wi-Fi 漏洞，中招就只能恢复出厂设置'
categories: 
 - 新媒体
 - IT 之家
 - 热榜
headimg: 'https://img.ithome.com/newsuploadfiles/2021/6/965c9cf0-039a-476b-8cc9-4f79232bf644.png'
author: IT 之家
comments: false
date: Mon, 05 Jul 2021 10:29:37 GMT
thumbnail: 'https://img.ithome.com/newsuploadfiles/2021/6/965c9cf0-039a-476b-8cc9-4f79232bf644.png'
---

<div>   
<p><a class="s_tag" href="https://www.ithome.com/" target="_blank">IT之家</a> 7 月 5 日消息 上个月底，安全人员 @Carl Schou 发现了一个苹果 iPhone 的奇特 Bug，连接特定 SSID“% p% s% s% s% s% n”的 WiFi 后会使手机无线连接功能作废，需要在设置中重置网络才能恢复。</p><p><img src="https://img.ithome.com/newsuploadfiles/2021/6/965c9cf0-039a-476b-8cc9-4f79232bf644.png" w="660" h="732" title="苹果 iPhone 再现 Wi-Fi 漏洞，中招就只能恢复出厂设置" width="660" height="732" referrerpolicy="no-referrer"></p><p>现在他又发现了一个更严重的漏洞。</p><p>IT之家了解到，如果你的 iPhone 连接了名为“% SecretClub% power”的 Wi-Fi，那么这部 iPhone 之后可能无法再正常使用 Wi-Fi 功能，甚至你就算恢复网络设置也不一定能解决，只能彻底抹除手机所有数据。</p><p><img src="https://img.ithome.com/newsuploadfiles/2021/7/5b760d96-b948-4893-9ddc-745ba7865c28.png" w="600" h="1139" title="苹果 iPhone 再现 Wi-Fi 漏洞，中招就只能恢复出厂设置" width="600" height="1139" referrerpolicy="no-referrer"></p><p>这一 bug 最初被认为是 iOS 输入解析的问题，其中百分比符号可能被 iOS 误解为字符串格式说明符，即符号后面的字符可能被视为变量或命令而非纯文本，因此会导致 iPhone Wi-Fi 功能出错。</p><p>新的 SSID bug 表明，字符 S 和 P 之后使用百分比符号极有可能是该 bug 的问题所在之处。对该 bug 的分析确认其本质是利用了底层 iOS 网络堆栈中某处字符串格式编码错误导致的，尽管它不一定会被恶意利用。</p><p>不过，Carl Schou 并未具体说明触发此 bug 的 iOS 版本和 iPhone 设备，目前受影响的设备具体情况还不得而知。</p>
          
</div>
            