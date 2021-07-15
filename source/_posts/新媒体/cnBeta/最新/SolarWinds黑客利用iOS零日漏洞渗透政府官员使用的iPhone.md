
---
title: 'SolarWinds黑客利用iOS零日漏洞渗透政府官员使用的iPhone'
categories: 
 - 新媒体
 - cnBeta
 - 最新
headimg: 'https://static.cnbetacdn.com/article/2021/0715/ba4917056f62ecf.png'
author: cnBeta
comments: false
date: Thu, 15 Jul 2021 04:36:41 GMT
thumbnail: 'https://static.cnbetacdn.com/article/2021/0715/ba4917056f62ecf.png'
---

<div>   
<strong>谷歌威胁分析团队指出，在针对西欧政府官员的渗透活动中，SolarWinds 黑客利用了在旧版 iOS 系统中新发现的一个零日漏洞。</strong>周三的这份报告，披露本次攻击还利用了通过领英（LinkedIn）向政府官员发送的信息。若受害者在 iPhone 上访问了特定的链接，就会被重定向至带有初始恶意负载的域名。<br>
 <p><img src="https://static.cnbetacdn.com/article/2021/0715/ba4917056f62ecf.png" referrerpolicy="no-referrer"></p><p>在满足多项“验证检查”后，SolarWinds 黑客会利用 CVE-2021-1879 漏洞来下载最终的有效载荷，并将之用于绕过某些安全防护措施。</p><p>比如关闭同源防护策略（Same-Origin-Policy）、或其它能够防止恶意脚本在本地网络上搜集数据的安全功能。</p><p>如此一来，攻击者便能够利用收集自谷歌、<a data-link="1" href="https://c.duomai.com/track.php?site_id=242986&euid=&t=https://www.microsoftstore.com.cn/" target="_blank">微软</a>、领英、脸书、雅虎等网站<a data-link="1" href="https://c.duomai.com/track.php?site_id=242986&euid=&t=https://shouji.jd.com/" target="_blank">手机</a>的身份验证信息，并将之发送到受黑客控制的 IP 地址。</p><p>不过 Maddie Stone 和 Clement Lecigne 写道：“受害者需要通过 Safari 访问精心制作的网站，才会被黑客成功渗透其 cookie ”。</p><p>庆幸的是，<a data-link="1" href="https://apple.pvxt.net/c/1251234/435400/7639?u=https%3A%2F%2Fwww.apple.com%2Fcn%2Fmusic%2F" target="_blank">苹果</a>已于今年 3 月修复了该漏洞。如果你运行受影响的 iOS 12.4 - 13.7 版本，还请及时为设备打上补丁。</p><p>此外通过使用支持站点隔离功能的浏览器（比如 Chrome 或 Firefox），亦可避免此类“同源策略”攻击。</p><p>最后，尽管谷歌没有披露幕后黑手的真实身份，但 ArsTechnica 已将攻击者确定为 Nobelium（与 2019 年 SolarWinds 黑客攻击事件背后是同一团队）。</p>   
</div>
            