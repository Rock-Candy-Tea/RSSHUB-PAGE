
---
title: 'Google Chrome迎来第100个版本 改进Cookie及多显示器表现'
categories: 
 - 新媒体
 - cnBeta
 - 最新
headimg: 'https://static.cnbetacdn.com/thumb/article/2022/0329/0a1aa4b814d1d5c.png'
author: cnBeta
comments: false
date: Tue, 29 Mar 2022 09:12:01 GMT
thumbnail: 'https://static.cnbetacdn.com/thumb/article/2022/0329/0a1aa4b814d1d5c.png'
---

<div>   
自Chrome 99发布以来已经过去了四个星期，这意味着Chrome
100是时候进入稳定通道了。除了本身是一个重要的里程碑之外，这也是一个关键的更新，因为它在解析用户代理字符串时可能会破坏一些网站的访问体验。虽然Google已经实施了一些保障措施，但三位数的版本号带来的技术问题依然值得关注。<br>
 <p><strong><a href="https://static.cnbetacdn.com/article/2022/0329/0a1aa4b814d1d5c.png" target="_blank"><img src="https://static.cnbetacdn.com/thumb/article/2022/0329/0a1aa4b814d1d5c.png" title alt="aa6b18410c7832e.png" referrerpolicy="no-referrer"></a></strong></p><p><strong>除此之外，Chrome 100也包含了大量的其他变化，你可以在下面阅读它们：</strong></p><p>首先，Chrome 100正在更新解析cookie字符串的方式，允许将域名属性设置为空字符串。这一修改将使Chrome与标准规范保持一致，也提高了与Safari和Firefox的互操作性，后者已经正确处理了空字符串。</p><p>多屏幕窗口放置API正在得到增强，以迎合现代的使用情况，提供更多关于次要屏幕的信息，而不是仅仅与主要显示器联系在一起。</p><p>Google表示，这将在准确的窗口放置方面解锁以下场景：</p><blockquote><p>一个在投影仪上演示的幻灯片应用程序，同时在笔记本电脑屏幕上显示演讲者的笔记。</p><p>一个金融应用程序在多个显示器上打开一个窗口的仪表板。</p><p>一个医疗应用在高分辨率灰度显示器上打开图像（例如，X射线）。</p><p>一个创意应用在一个单独的屏幕上显示二级窗口（例如调色板）。</p><p>游戏、标牌、艺术和其他类型的应用程序中的多屏幕布局。</p></blockquote><p>Chrome 100中另一个有趣的功能是，网站现在可以使用一种新的方法来自愿忘记链接的人类接口设备（HID）。这意味着，使用网络蓝牙和WebUSB标准连接外设的网站如果不再需要，可以撤销这一权限许可。</p><p>Chrome 100还引入了一个数字商品API。这将使Play Store中的网络应用能够接受数字购买。这实质上是对Android Play Billing API的打包，并使提供数字购买的网络应用可以从Play Store中安装。</p><p>其他相对较小的功能包括能力委托，这样一个框架就可以将调用受限API的能力转移给受信任的子框架，增强混合混合模式属性，更好地处理AbortSignal对象的错误，通过哈希而不是依赖公钥基础设施（PKI）来认证WebTransport服务器，以及一个Web NFC方法，使开发者能够永久地使NFC标签只读。</p><p>最后，Chrome还在AbortSignal和SerialPort对象之间进行了整合，对WebSockets进行了小幅调整，并对减少用户代理字符串进行了一些兼容性修改。</p><p>Chrome 100是支持未减少的用户代理字符串的最后一个版本的浏览器。开发人员可以在2022年4月19日之前通过Origin进行试用。需要更多时间的网站开发者可以让他们的网站参加从Chrome 100到Chrome 113（含）的试验。这意味着他们在2023年5月之前可以继续使用传统的用户代理字符串，然后再迁移到用户代理客户端提示API。你可以在这里找到更多细节，并且还可以在这里阅读更多关于Chrome 100 DevTools的所有新内容：</p><p><a href="https://blog.chromium.org/2021/09/user-agent-reduction-origin-trial-and-dates.html" _src="https://blog.chromium.org/2021/09/user-agent-reduction-origin-trial-and-dates.html" target="_blank">https://blog.chromium.org/2021/09/user-agent-reduction-origin-trial-and-dates.html</a><br></p><p><a href="https://developer.chrome.com/blog/new-in-devtools-100/" _src="https://developer.chrome.com/blog/new-in-devtools-100/" target="_blank">https://developer.chrome.com/blog/new-in-devtools-100/</a><br></p><p>Chrome 100将在今天晚些时候开始推出。如果没有自动更新到100版本，请前往"帮助">"关于Google浏览器"，以便在更新可用时触发该更新。接下来是Chrome 101，它将于3月31日进入测试频道，并将于4月26日登陆稳定版。</p>   
</div>
            