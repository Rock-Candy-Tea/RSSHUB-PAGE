
---
title: '_图_这次是微软发现了Google ChromeOS中的漏洞 可导致内存严重损坏'
categories: 
 - 新媒体
 - cnBeta
 - 最新
headimg: 'https://static.cnbetacdn.com/article/2022/0825/47657f382034c42.webp'
author: cnBeta
comments: false
date: Thu, 25 Aug 2022 00:34:02 GMT
thumbnail: 'https://static.cnbetacdn.com/article/2022/0825/47657f382034c42.webp'
---

<div>   
在过去我们经常看到 Google 旗下的“Project Zero”团队曝光各种 Windows 系统漏洞，<strong>不过在几个月前微软披露了存在于 ChromeOS 系统中的一个漏洞。</strong>根据 Chromium 错误日志，微软的 365 Defender Research 团队发现了 <a href="https://bugs.chromium.org/p/chromium/issues/detail?id=1320917" target="_blank">Security: ChromeOS cras D-Bus SetPlayerIdentity</a>，<strong>会导致内存<strong>严重</strong>损坏。</strong><br>
 <p style="text-align:center"><img src="https://static.cnbetacdn.com/article/2022/0825/47657f382034c42.webp" referrerpolicy="no-referrer"></p><p style="text-align: left;">在日志中写道：“在定位到本地内存损坏问题后，我们发现该漏洞可以通过操纵音频元数据远程触发。攻击者可能会诱使用户满足这些条件，例如通过简单地在浏览器中或从配对的蓝牙设备播放一首新歌曲，或利用中间对手 (AiTM) 功能远程利用该漏洞”。</p><p style="text-align: left;"><a href="https://nvd.nist.gov/vuln/detail/CVE-2022-2587" target="_blank">用更有技术的方式来描述就是，</a>从命令行可以通过将 128 字节的字符串传递给 dbus-send 实用程序来触发基于堆的缓冲区溢出，最终结果可能是简单的拒绝服务或完整的远程代码执行。</p><p style="text-align:center"><img src="https://static.cnbetacdn.com/article/2022/0825/b0abdb498f6ea91.webp" referrerpolicy="no-referrer"></p><p style="text-align: left;">在发现该漏洞后，Microsoft 将其标记为 CVE-2022-2587，并且就关键效力而言，通用漏洞评分系统 (CVSS) 得分为 9.8 分（满分 10 分）。</p><p style="text-align: left;">幸运的是，这一切都是在 2022 年 4 月完成的，此后Google及其 ChromeOS 团队已对其进行了修补。Microsoft 365 Defender 研究团队的 Jonathan Bar Or 写道：“代码已提交，并在多次合并后向用户正式发布。我们感谢 Google 团队和 Chromium 社区为解决该问题所做的努力”。</p>   
</div>
            