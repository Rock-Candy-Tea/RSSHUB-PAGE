
---
title: 'Appium 1.22.2 发布，移动应用自动化测试工具'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=217'
author: 开源中国
comments: false
date: Mon, 21 Feb 2022 07:05:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=217'
---

<div>   
<div class="content">
                                                                                            <p>Appium 是一个开源、跨平台的自动化测试工具，最初主要用于测试原生和轻量移动应用，包括 iOS 和 Android ，目前还支持对 Windows 平台上的应用的自动化测试。</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">Appium 1.22.2 已发布，这是一个补丁版本。Appium 1.x 只有在 XCTest 获得 <span style="background-color:#ffffff; color:#24292f">breaking updates </span>或在 EOL 之前出现重大 <span style="background-color:#ffffff; color:#24292f">bugs </span>时，才会收到小版本或补丁版本更新。</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">主要更新内容如下：</p> 
<p style="text-align:start"><strong>iOS(XCUITest)</strong></p> 
<ul> 
 <li>添加<code>safariTabBarPosition</code>settings api，以帮助<code>nativeWebTap</code>capability/setting 考虑设备是否在 Safari 窗口的顶部或底部具有 tab bar。可阅读 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fappium%2Fappium-xcuitest-driver%23settings-api" target="_blank">Settings API</a> 中的<code>safariTabBarPosition</code>以了解更多详细信息 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fappium%2Fappium-xcuitest-driver%2Fpull%2F1361" target="_blank">appium-xcuitest-driver#1361</a></li> 
 <li>iOS 15 环境下不显示模拟器的键盘教程 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fappium%2Fappium-ios-simulator%2Fpull%2F315" target="_blank">appium-ios-simulator#315</a></li> 
 <li>修复在 <a href="https://www.oschina.net/action/GoToLink?url=http%3A%2F%2Fappium.io%2Fdocs%2Fen%2Fcommands%2Fdevice%2Fapp%2Finstall-app%2F" target="_blank">Install App</a> 命令中 pass installation options 的问题 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fappium%2Fappium-xcuitest-driver%2Fpull%2F1357" target="_blank">appium-xcuitest-driver#1357</a></li> 
 <li>禁用 XCTest 默认的通知检查器，以避免在 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fappium%2Fappium%2Fissues%2F16025" target="_blank">iOS 15.2</a> 上出现问题 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fappium%2FWebDriverAgent%2Fpull%2F540" target="_blank">WebDriverAgent#540</a></li> 
 <li>略微提升 XML source generation 的性能 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fappium%2Fappium-xcuitest-driver%2Fpull%2F1351" target="_blank">appium-xcuitest-driver#1351 </a><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fappium%2FWebDriverAgent%2Fpull%2F544" target="_blank">WebDriverAgent#544</a></li> 
</ul> 
<p style="text-align:start">详情可查看 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fappium%2Fappium%2Fblob%2Fmaster%2FCHANGELOG.md" target="_blank">CHANGELOG</a></p>
                                        </div>
                                      
</div>
            