
---
title: '任天堂Switch、索尼PS5手柄驱动等HID更新已经抵达Linux 5.16'
categories: 
 - 新媒体
 - cnBeta
 - 最新
headimg: 'https://static.cnbetacdn.com/article/2021/1105/f366838f179afdf.jpg'
author: cnBeta
comments: false
date: Fri, 05 Nov 2021 13:35:32 GMT
thumbnail: 'https://static.cnbetacdn.com/article/2021/1105/f366838f179afdf.jpg'
---

<div>   
<strong>HID子系统的更新已经被送入正在进行的Linux
5.16合并窗口，对Linux游戏玩家来说会有一些明显的改进。</strong>最令人兴奋的消息是任天堂Switch手柄驱动终于出现了！这个内核驱动可以让任天堂Switch的用户能够与主线内核一起工作，并且无论是USB有线和蓝牙连接下都被支持，像触感震动模式、LED和其他功能都可以正常工作。<br>
 <p><img src="https://static.cnbetacdn.com/article/2021/1105/f366838f179afdf.jpg" title alt="1.jpg" referrerpolicy="no-referrer"></p><p>需要注意的是，这个开源的<a data-link="1" href="https://c.duomai.com/track.php?site_id=242986&euid=&t=https://www.jd.com/pinpai/14671.html" target="_blank">任天堂</a>Switch手柄驱动程序不是来自任天堂，而是通过逆向工程的自由软件社区。</p><p><img src="https://static.cnbetacdn.com/article/2021/1105/f30db3194d06803.jpg" title alt="2.jpg" referrerpolicy="no-referrer"></p><p>同时，索尼官方对他们支持PlayStation 5 DualSense手柄的HID内核驱动做出了改进。</p><p>去年年底，索尼发布了一个用于Linux的官方PS5手柄驱动程序。该驱动程序被添加到Linux 5.12中，他们现在可以继续工作。对于Linux 5.16而言，索尼的Roderick Colenbrander提交的PlayStation 5手柄支持驱动的最新版带来了LED处理方面的改进。</p><p><img src="https://static.cnbetacdn.com/article/2021/1105/7f52a6a63cce178.jpg" title alt="3.jpg" referrerpolicy="no-referrer"></p><p>本周期另一个值得注意的HID新增内容是对<a data-link="1" href="https://apple.pvxt.net/c/1251234/435400/7639?u=https%3A%2F%2Fwww.apple.com%2Fcn%2Fmusic%2F" target="_blank">苹果</a>Magic Keyboard 2021型号的支持，不过与Switch一样，开源HID驱动没有得到苹果官方支持。Linux 5.16 HID还增加了对NitroKey FIDO U2F的支持。</p><p><img src="https://static.cnbetacdn.com/article/2021/1105/edfd0afc134ce18.jpg" title alt="image.jpg" referrerpolicy="no-referrer"></p><p><strong>今天上午Linux 5.16版HID的这一系列重大变化是通过这个拉动请求提交的：</strong></p><p><a href="https://lore.kernel.org/lkml/nycvar.YFH.7.76.2111051220020.12554@cbobk.fhfr.pm/T/#u" _src="https://lore.kernel.org/lkml/nycvar.YFH.7.76.2111051220020.12554@cbobk.fhfr.pm/T/#u" target="_blank">https://lore.kernel.org/lkml/<span class="__cf_email__" data-cfemail="f09e8993869182dea9b6b8dec7dec7c6dec2c1c1c1c0c5c1c2c2c0c0c2c0dec1c2c5c5c4b093929f929bde96989682de809d">[email protected]</span>/T/#u</a><br></p>   
</div>
            