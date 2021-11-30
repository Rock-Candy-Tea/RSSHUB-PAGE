
---
title: '一批Android网银木马躲过官方应用商店检测 清理前下载量已达30万'
categories: 
 - 新媒体
 - cnBeta
 - 最新
headimg: 'https://static.cnbetacdn.com/thumb/article/2021/1130/f6b0d259d8a71c8.png'
author: cnBeta
comments: false
date: Tue, 30 Nov 2021 04:57:27 GMT
thumbnail: 'https://static.cnbetacdn.com/thumb/article/2021/1130/f6b0d259d8a71c8.png'
---

<div>   
<strong>Threat Fabric 安全研究人员刚刚公布了一批 Android 网银木马，而且在被 Google Play 清理之前，其下载量就已经超过了 30 万次。</strong>在二维码扫描仪、PDF 扫描仪、加密货币钱包等表象的掩饰下，这些恶意应用会在暗中窃取用户登录凭证、双因素身份验证码、记录按键、以及屏幕截图。<br>
 <p><a href="https://static.cnbetacdn.com/article/2021/1130/f6b0d259d8a71c8.png" target="_blank"><img src="https://static.cnbetacdn.com/thumb/article/2021/1130/f6b0d259d8a71c8.png" alt="0.png" referrerpolicy="no-referrer"></a></p><p style="text-align: center;">（来自：<a href="https://www.threatfabric.com/blogs/deceive-the-heavens-to-cross-the-sea.html" target="_self">Threat Fabric</a>）</p><p>通过持续四个月的追踪，Threat Fabric 发现了四个独立的 Android 恶意软件系列。可知其利用了多种技巧，来规避 Google Play 应用商店的检测机制</p><p>安全研究人员指出，之所以从 Google Play 的自动化（安全沙箱）和机器学习审核流程中逃逸，正是该平台试试权限限制的直接后果。</p><p><a href="https://static.cnbetacdn.com/article/2021/1130/32fcd36089caca6.png" target="_blank"><img src="https://static.cnbetacdn.com/thumb/article/2021/1130/32fcd36089caca6.png" alt="1.png" referrerpolicy="no-referrer"></a></p><p>通常情况下，这些恶意软件会先以一款良性 App 的面目示人。所以在早期的 VirusTotal 恶意软件检测过程中，它们并不会在第一时间被揪出。</p><p>但在用户安装后，它们就会开始诱骗用户下载并安装带有“附加功能”的更新包。此时这些恶意应用会通过第三方来源来获取，但此时它们已经骗取了用户的普遍信任。</p><p><a href="https://static.cnbetacdn.com/article/2021/1130/bd2035ac6738433.png" target="_blank"><img src="https://static.cnbetacdn.com/thumb/article/2021/1130/bd2035ac6738433.png" alt="2.png" referrerpolicy="no-referrer"></a></p><p>为了躲避雷达追踪，这些恶意程序还利用了其它手段。在许多情况下，幕后操纵者只有在检查受感染的设备的地理位置、或通过增量更新后，才会手动部署恶意内容。</p><p>这种致力于躲过不必要关注的手段，实在让人难以置信。然而现实表明，基于自动化流程的传统恶意软件检测方案，正在变得不那么可靠。</p><p><a href="https://static.cnbetacdn.com/article/2021/1130/60fd26added3cb7.png" target="_blank"><img src="https://static.cnbetacdn.com/thumb/article/2021/1130/60fd26added3cb7.png" alt="3.png" referrerpolicy="no-referrer"></a></p><p>在近日发表的一篇博客文章中，Threat Fabric 详细阐述了被调查的 9 款 dropper 恶意软件。其中造成最多感染的，被称作 Anatsa 家族。</p><p>这款“相当先进”的 Android 网银木马内置了许多功能，包括远程访问和自动转账系统。受害者将被无情地清空账户，将资金转移到幕后黑手控制的账户中。</p><p><a href="https://static.cnbetacdn.com/article/2021/1130/cf166612c137a6e.png" target="_blank"><img src="https://static.cnbetacdn.com/thumb/article/2021/1130/cf166612c137a6e.png" alt="4.png" referrerpolicy="no-referrer"></a></p><p>感染 Anatsa 恶意软件的过程，是从 Google Play 下载看似人畜无害的初始安装包后开始的。之后相关 App 会强制用户更新，以继续使用该应用程序。</p><p>但现实是，幕后黑手在远程更新服务器上托管了夹带私货的恶意内容，并通过骗取信任的方式，将之安装在了毫无戒备的受害者设备上。</p><p><a href="https://static.cnbetacdn.com/article/2021/1130/098dae7119fb176.png" target="_blank"><img src="https://static.cnbetacdn.com/thumb/article/2021/1130/098dae7119fb176.png" alt="5.png" referrerpolicy="no-referrer"></a></p><p>为了装得更像一些，幕后团伙甚至会雇人在 Google Play 应用商店刷好评，以引诱更多无辜者上当受骗。</p><p>最后，研究人员还发现了另外三大恶意软件家族（分别称之为 Alien、Hydra 和 Ermac）。</p><p>其特点是植入了 Gymdrop 恶意负载，并利用基于受感染设备模型的过滤规则，来躲过安全研究人员的搜捕。</p>   
</div>
            