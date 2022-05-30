
---
title: 'ChromeLoader恶意软件：添加恶意扩展点击在线广告谋利'
categories: 
 - 新媒体
 - cnBeta
 - 最新
headimg: 'https://static.cnbetacdn.com/article/2022/0530/086864a2b08c659.webp'
author: cnBeta
comments: false
date: Mon, 30 May 2022 03:53:40 GMT
thumbnail: 'https://static.cnbetacdn.com/article/2022/0530/086864a2b08c659.webp'
---

<div>   
近日网络安全专家发现了一个新型恶意网络病毒，通过在浏览器中添加恶意扩展程序让受害者点击在线广告，从而为不法分子带来收入。<strong>据网络安全商店 Red Canary 的安全专家分析，该病毒称之为 ChromeLoader，设备一旦感染就很难发现和删除。</strong><br>
 <p style="text-align:center"><img src="https://static.cnbetacdn.com/article/2022/0530/086864a2b08c659.webp" referrerpolicy="no-referrer"></p><p style="text-align:center"><img src="https://static.cnbetacdn.com/article/2022/0530/aa74193cc5aa30a.webp" referrerpolicy="no-referrer"></p><p style="text-align: left;">在 <a data-link="1" href="https://microsoft.pvxt.net/x9Vg1" target="_blank">Windows</a> 平台上，该恶意病毒会使用 PowerShell 向受害者的 Chrome 浏览器添加恶意扩展；在 macOS 平台上，它使用 Bash 向 Safari 发起相同的攻击。Red Canary 的检测工程师 Aedan Russell 在博文中详细介绍了该恶意程序。</p><p style="text-align: left;">ChromeLoader 注入的恶意扩展程序一旦添加到受害者的浏览器中，就会通过在线广告重定向用户，从而为不法分子带来收入。 Russell 告诉 The Register，Windows ChromeLoader 使用 PowerShell 插入更多恶意 Chrome 扩展程序的情况并不常见。</p><p style="text-align: left;">Russell 表示：</p><blockquote><p style="text-align: left;">ChromeLoader 的开发人员已经找到了一种通过使用 Chrome 的合法开发人员命令行参数来收集广告收入的有效方法。</p><p style="text-align: left;">通过 PowerShell 加载 Web 浏览器扩展程序（并且默默地这样做）显示出高于标准的隐蔽性，因为其他恶意浏览器扩展程序通常是通过诱骗用户公开安装它们来引入的，通常伪装成合法的浏览器扩展程序。</p></blockquote><p style="text-align: left;">ChromeLoader 通过以 ISO 文件的形式分发，该文件看起来像种子文件或破解的视频游戏，从而获得了对系统的初始访问权限。据 Red Canary 称，它通过按安装付费的网站和 Twitter 等社交媒体网络传播。</p>   
</div>
            