
---
title: '苹果在iOS 14.7开发者测试版本中修复了Wi-Fi功能变砖的问题'
categories: 
 - 新媒体
 - cnBeta
 - 最新
headimg: 'https://static.cnbetacdn.com/article/2021/0710/f7fe2a14047b5f5.jpg'
author: cnBeta
comments: false
date: Sat, 10 Jul 2021 02:47:35 GMT
thumbnail: 'https://static.cnbetacdn.com/article/2021/0710/f7fe2a14047b5f5.jpg'
---

<div>   
上月，安全研究员 Carl Schou 曝光了 iOS 中存在了一个无线连接功能 Bug 。当 iPhone 尝试连接到具有特殊名称的 Wi-Fi 热点时，很可能导致设备的无线连接功能出现异常。<strong>好消息是，随着 iOS 14.7 新开发者测试版（Developer beta 5）的到来，苹果终于修复了 iPhone 会被“%p%s%s%s%s%n”等特殊 Wi-Fi 热点带到沟里去的 Bug 。</strong><br>
 <p><img src="https://static.cnbetacdn.com/article/2021/0710/f7fe2a14047b5f5.jpg" referrerpolicy="no-referrer"></p><p style="text-align: center;">（图 via <a href="https://appleinsider.com/articles/21/07/09/critical-wi-fi-bug-fixed-in-ios-147-developer-beta-5" target="_self">Apple Insider</a>）</p><p>此前 Carl Schou 发现，在尝试连接那些带有百分比（%）符号的 Wi-Fi 热点名称后，会导致 iOS 设备的 Wi-Fi 功能变砖。</p><p>而从油管 Zollotech 频道发布的新视频来看，近日更新的 iOS 14.7 beta 5 不仅带来了一些直观可见变化，还修复了这个严重影响用户使用体验的 Wi-Fi 热点名称 Bug 。</p><p><img src="https://static.cnbetacdn.com/article/2021/0620/5b3e155c99f6297.gif" referrerpolicy="no-referrer"></p><p style="text-align: center;">iOS 14 无线热点名称 Bug 演示</p><p>除了 Carl Schou 演示的“%p%s%s%s%s%n”，另一种“%secretclub%power”无线热点名称也会导致 iOS 设备的 Wi-Fi 功能被彻底禁用、且无法再次连上。</p><p>显然，该 Bug 与<a data-link="1" href="https://apple.pvxt.net/c/1251234/435400/7639?u=https%3A%2F%2Fwww.apple.com%2Fcn%2Fmusic%2F" target="_blank">苹果</a>移动操作系统对特殊字符的处理方式有关。而此前不幸躺枪的用户，已被迫通过出厂重置来解决该问题。</p><p style="text-align: center;"><iframe width="640" height="480" src="//tv.sohu.com/s/sohuplayer/iplay.html?bid=270941384&autoplay=false&disablePlaylist=true" frameborder="0"></iframe></p><p style="text-align: center;">iOS 14.7 Beta 5 is Out - What's New（<a href="https://tv.sohu.com/v/dXMvODIyMjQwNTMvMjcwOTQxMzg0LnNodG1s.html" target="_self">via</a>）</p><p>Apple Insider 指出，苹果或将带有百分比符号的 SSID 名称误解为字符串格式的说明符，即符号后的字符串被理解称变量或命令、而不是纯文本。</p><p>据推测，苹果应该会将之视作一个高优先级的修复程序。如果一切顺利的话，预计 iOS 14.7 会在未来几天内向公众推送，并自动安装相应更新。</p><div class="article-relation"><p><strong>相关文章:</strong></p><p><a href="https://www.cnbeta.com/articles/tech/1142767.htm" target="_blank">iOS又一Bug：特殊Wi-Fi热点名称会导致iPhone无线连接功能异常</a></p></div>   
</div>
            