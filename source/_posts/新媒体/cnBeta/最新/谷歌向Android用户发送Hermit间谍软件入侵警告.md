
---
title: '谷歌向Android用户发送Hermit间谍软件入侵警告'
categories: 
 - 新媒体
 - cnBeta
 - 最新
headimg: 'https://static.cnbetacdn.com/article/2022/0624/a7a2a0039aba7e1.png'
author: cnBeta
comments: false
date: Fri, 24 Jun 2022 02:31:49 GMT
thumbnail: 'https://static.cnbetacdn.com/article/2022/0624/a7a2a0039aba7e1.png'
---

<div>   
<strong>早些时候，Lookout 安全研究人员将一款名为 Hermit 的 Android 间谍软件，与意大利 RCS Lab 软件公司联系了起来。</strong>现在，Google 威胁研究人员已经证实了 Lookout 的大部分发现，并且正在向遭到 Hermit 移动间谍软件入侵的 Android 用户发去警告。<br>
 <p style="text-align: center;"><img src="https://static.cnbetacdn.com/article/2022/0624/a7a2a0039aba7e1.png" alt="1.png" referrerpolicy="no-referrer"></p><p style="text-align: center;">被攻击者控制的一个站点截图</p><p>Lookout 与 <a href="https://blog.google/threat-analysis-group/italian-spyware-vendor-targets-users-in-italy-and-kazakhstan/" target="_self">Google</a> 指出，Hermit 被证实为有官方背景的商业间谍软件，受害者主要出现在哈萨克斯坦和意大利、但叙利亚北部也有被发现。</p><p style="text-align: center;"><img src="https://static.cnbetacdn.com/article/2022/0624/c62b43d1514d520.png" alt="2.png" referrerpolicy="no-referrer"></p><p>该间谍软件拥有各种模块，可根据需要从其命令与控制服务器（C&C）获取相关功能，比如收集通话记录、记录环境音频、重定向电话，以及受害者的设备上窃取照片、消息、电子邮件和精确定位。</p><p style="text-align: center;"><img src="https://static.cnbetacdn.com/article/2022/0624/57b3985b0364550.png" alt="3.png" referrerpolicy="no-referrer"></p><p>Lookout 分析发现，Hermit 间谍软件可在所有 Android 版本上运行，并试图在受感染的 Android 设备上扎根。</p><p>攻击者通过短信发送的恶意链接，引诱受害者从外部应用商店下载并安装恶意软件。通常情况下，Hermit 会将自己伪装成各大通讯品牌或消息传递类应用。</p><p style="text-align: center;"><img src="https://static.cnbetacdn.com/article/2022/0624/796bfcec99858ee.png" alt="4.png" referrerpolicy="no-referrer"></p><p>此外在周四的一篇博客文章中，Google 找到了幕后行为者与目标 ISP 联手切断移动数据连接的证据。推测是以恢复连接为幌子，引诱受害者去下载 App 。</p><p>Google 进一步分析了针对 <a data-link="1" href="https://apple.pvxt.net/c/1251234/435400/7639?u=https%3A%2F%2Fwww.apple.com%2Fcn%2Fiphone%2F" target="_blank">iPhone</a> 的间谍软件样本，调查发现 Hermit 的 iOS App 滥用了苹果企业开发者证书，以允许间谍软件从外部应用商店加载。</p><p><img src="https://static.cnbetacdn.com/article/2022/0624/afacf35b9ba2370.png" alt="5.png" referrerpolicy="no-referrer"></p><p>间谍软件利用了六个不同的漏洞，其中两个属于未曝出过的零日漏洞。更糟糕的是，苹果知悉其中一个 0-Day 漏洞已在修复完成前被积极利用。</p><p>庆幸的是，两家科技巨头都表示未在官方应用商店里发现 Android / iOS 版的 Hermit 间谍软件。</p><p><img src="https://static.cnbetacdn.com/article/2022/0624/5123ea1b461258b.png" alt="6.png" referrerpolicy="no-referrer"></p><p>目前 Google 已向受感染的 Android 设备用户发去警告通知，并更新了系统内置的 Google Play Protect 安全扫描程序，以阻止该间谍软件的运行。</p><p>此外 Google 关闭了间谍软件用于和服务器通讯的 Firebase 帐户，但并未透露到底有多少 Android 设备收到了 Hermit 间谍软件的影响。</p><p><img src="https://static.cnbetacdn.com/article/2022/0624/4022966e2bf6ff0.png" alt="7.png" referrerpolicy="no-referrer"></p><p>苹果发言人 Trevor Kincaid 则表示，该公司已吊销与本轮间谍软件活动相关的所有已知账户和证书。</p><p>目前尚不清楚 Hermit 间谍软件的确切针对目标，但有 NSO Group 和 Candiru 等臭名昭著的案例在前，此事也并不难推测。</p>   
</div>
            