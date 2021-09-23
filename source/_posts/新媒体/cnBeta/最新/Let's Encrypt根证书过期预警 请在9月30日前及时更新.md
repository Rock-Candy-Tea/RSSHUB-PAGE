
---
title: "Let's Encrypt根证书过期预警 请在9月30日前及时更新"
categories: 
 - 新媒体
 - cnBeta
 - 最新
headimg: 'https://static.cnbetacdn.com/article/2021/0923/dcfc55c329b236c.png'
author: cnBeta
comments: false
date: Thu, 23 Sep 2021 08:55:29 GMT
thumbnail: 'https://static.cnbetacdn.com/article/2021/0923/dcfc55c329b236c.png'
---

<div>   
安全研究员 Scott Helme 警告称：作为全球最大 HTTPs 证书提供商之一的 Let's Encrypt，即将于下周停用旧版根证书（Root CA）。<strong>这意味着数百万计依赖它的网站必须在 9 月 30 日前及时更新，不然将面临不受计算机、设备或 Web 浏览器信任的困扰。</strong><br>
<p style="text-align: center;"><img src="https://static.cnbetacdn.com/article/2021/0923/dcfc55c329b236c.png" referrerpolicy="no-referrer"></p><p style="text-align: center;">（图自：<a href="https://scotthelme.co.uk/lets-encrypt-old-root-expiration/" target="_self">Scott Helme</a>）</p><p>据悉，作为一家非盈利组织，Let's Encrypt 致力于通过颁发证书来推动设备和互联网数据通信的加密，确保不被第三方拦截并窃取信息。</p><p>然而 Let's Encrypt 当前使用的 IdentTrust DST Root CA X3 根证书，也即将于下周过期。对于大部分网站的访客来说，9 月 30 日可能是个波澜不惊的一天。</p><p>但是对于较旧的设备来说，可能还是会遇到一些问题 ——正如 AddTrust External CA Root 在今年 5 月遭遇的根证书过期中断那样，造成Stripe、Red Hat 和 Roku 都受到了影响。</p><p>Scott Helme 在一篇博文中写道：“考虑到 Let's Encrypt 和 AddTrust 之间的体量差异，我有预感 IdenTrust 根证书到期时又会让历史重演，甚至可能引发更多的问题”。</p><p>当然，潜在易受影响的，主要是那些不怎么定期更新的设备 —— 比如嵌入式系统、或运行多年前软件版本的智能<a data-link="1" href="https://c.duomai.com/track.php?site_id=242986&euid=&t=https://shouji.jd.com/" target="_blank">手机</a>。</p><p><a href="https://static.cnbetacdn.com/article/2021/0923/41fb5ddeb745e28.png" target="_blank"><img src="https://static.cnbetacdn.com/thumb/article/2021/0923/41fb5ddeb745e28.png" referrerpolicy="no-referrer"></a></p><p style="text-align: center;">（图自：<a href="https://letsencrypt.org/2020/11/06/own-two-feet.html" target="_self">Let's Encrypt</a>）</p><p>举个例子，运行 macOS 2016 和 <a data-link="1" href="https://microsoft.pvxt.net/x9Vg1" target="_blank">Windows</a> XP SP3 的设备用户可能在月底之后遇到麻烦。依赖 OpenSSL 1.0.2 或更早版本的客户端平台也可能受到影响，此外还有尚未升级到新版固件的 PlayStation 老游戏机。</p><p>鉴于 Android 生态有着长期存在且众所周知的问题，为了防止大多数智能机受到本次事件的影响，Let's Encrypt 已于今年早些时候未雨绸缪地过渡到了自家的 ISRG Root X1 证书（到期时间为 2035 年）。</p><p>虽然包括 Android 7.1.1（Nougat）及更早版本的设备并不信任它，但 Let's Encrypt 还是能够通过对自颁证书进行交叉签名的方式，让大多数 Android 设备可在未来三年内避免受到波及。</p><p>但若你还想在 Android 5.0（Lollipop）上安装 Firefox，最好还是尽早为迁移至新平台做打算。</p><p>最后，自 2014 年成立以来，截止 2021 年 9 月初，Let's Encrypt 总计已经颁发了超过 20 亿份证书。</p>   
</div>
            