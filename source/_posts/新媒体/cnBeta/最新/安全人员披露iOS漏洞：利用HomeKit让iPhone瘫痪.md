
---
title: '安全人员披露iOS漏洞：利用HomeKit让iPhone瘫痪'
categories: 
 - 新媒体
 - cnBeta
 - 最新
headimg: 'https://static.cnbetacdn.com/article/2022/0102/8891643d2a97249.webp'
author: cnBeta
comments: false
date: Sun, 02 Jan 2022 00:54:16 GMT
thumbnail: 'https://static.cnbetacdn.com/article/2022/0102/8891643d2a97249.webp'
---

<div>   
<strong>近日安全研究人员披露了存在于 iOS 系统中的漏洞，使用 HomeKit 进行攻击，而且苹果修复该漏洞的速度非常缓慢。</strong>安全研究员 Trevor Spiniolas 称，如果 HomeKit 设备名称被改为一个“很长的字符串”，在测试中设定为 50 万个字符，加载该字符串的 iOS 和 iPadOS 设备就会被重新启动并无法使用。<br>
 <p><img src="https://static.cnbetacdn.com/article/2022/0102/8891643d2a97249.webp" alt="QQ截图20220102085225.webp" referrerpolicy="no-referrer"></p><p>此外，由于该名称存储在 iCloud 中，并在登录到同一账户的所有其他 iOS 设备中得到更新，该错误可能会反复出现。</p><p>Spiniolas 称这个漏洞为“doorLock”，并声称它影响到测试中的 iOS 14.7 以上的所有 iOS 版本，尽管它也可能存在于所有 iOS 14 版本中。</p><p>此外，虽然 iOS 15.0 /15.1 中的更新对应用程序或用户可以设置的名称长度进行了限制，但以前的 iOS 版本仍然可以更新名称。如果该错误在没有限制的 iOS 版本上被触发，并共享 HomeKit 数据，那么与之共享数据的所有设备也将受到影响，无论版本如何。</p><p>这会导致两种情况发生，在控制中心没有启用 Home 设备的设备会发现 Home 应用无法使用并崩溃。重启或更新都不能解决这个问题，恢复的设备如果签入同一个 iCloud 账户，将再次使 Home 无法使用。</p><p>对于在控制中心启用了Home设备的<a data-link="1" href="https://apple.pvxt.net/c/1251234/435400/7639?u=https%3A%2F%2Fwww.apple.com%2Fcn%2Fiphone%2F" target="_blank">iPhone</a>和<a data-link="1" href="https://apple.pvxt.net/c/1251234/435400/7639?u=https%3A%2F%2Fwww.apple.com%2Fcn%2Fipad%2F" target="_blank">iPad</a>，也就是用户访问HomeKit设备时的默认设置，iOS本身变得毫无反应。输入变得延迟或被忽略，设备没有反应，偶尔会经历重启。</p><p>在这种情况下，重启或更新设备都无法解决，而中断的USB访问基本上会迫使用户恢复设备并丢失所有本地数据。然而，恢复和签署到同一iCloud账户将再次触发该错误，其效果与之前相同。</p><p>Spiniolas认为这个问题可能被用于恶意的目的，比如通过一个可以访问家庭数据的应用程序自己引入这个错误。攻击者向其他用户发送对Home的邀请也是可行的，即使目标不拥有HomeKit设备。</p><p>据研究人员称，通过在控制中心禁用Home设备，可以避免这两种情况中最糟糕的情况。要做到这一点，打开"设置"和"控制中心"，然后将"显示家庭控制"的切换设置为关闭。用户还应该对加入其他用户的家庭网络的邀请保持警惕，特别是那些来自未知联系人的邀请。</p><p>Spiniolas声称，他最初在8月10日向<a data-link="1" href="https://apple.pvxt.net/c/1251234/435400/7639?u=https%3A%2F%2Fwww.apple.com%2Fcn%2Fmusic%2F" target="_blank">苹果</a>公司报告了这个错误，据说苹果公司计划在2022年底前发布修复该错误的安全更新。然而，据称苹果随后在12月8日将其估计改为"2022年初"。</p><p>该研究人员写道：“我认为这个bug的处理是不恰当的，因为它给用户带来了严重的风险，而且很多个月过去了，没有得到全面的修复。公众应该知道这个漏洞以及如何防止它被利用，而不是被蒙在鼓里”。</p>   
</div>
            