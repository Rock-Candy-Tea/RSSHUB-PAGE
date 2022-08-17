
---
title: 'Monterey前macOS旧版本仍存高危漏洞 黑客可绕过安全机制修改核心文件'
categories: 
 - 新媒体
 - cnBeta
 - 最新
headimg: 'https://static.cnbetacdn.com/article/2022/0817/47bbda2999634d2.webp'
author: cnBeta
comments: false
date: Wed, 17 Aug 2022 00:29:35 GMT
thumbnail: 'https://static.cnbetacdn.com/article/2022/0817/47bbda2999634d2.webp'
---

<div>   
一名安全专家于去年发现了存在于 macOS 系统中的漏洞，可以浏览系统上的任意文件。<strong>利用这个漏洞，黑客可以绕过所有的 Mac 安全防护层、更改核心系统文件、访问网络摄像头。</strong>苹果虽然在去年发布了修复补丁，不过在旧版 macOS 系统中依然存在。<br>
 <p style="text-align:center"><img src="https://static.cnbetacdn.com/article/2022/0817/47bbda2999634d2.webp" referrerpolicy="no-referrer"></p><p style="text-align: left;">去年 10 月，<a data-link="1" href="https://apple.pvxt.net/c/1251234/435400/7639?u=https%3A%2F%2Fwww.apple.com%2Fcn%2Fmusic%2F" target="_blank">苹果</a>在 macOS Monterey 中修复了这个高危漏洞，不过此前旧版本依然可以通过代码注入的方式破坏 Mac 设备。虽然目前并没有证据表明已经有黑客利用该漏洞，但是存在敏感信息泄露以及被黑客完全掌控的风险。</p><p style="text-align: left;">该漏洞可以绕过苹果防止恶意代码传播的 2 个安全审查机制：其一是 macOS Sandbox，理论上可以将恶意代码限制在已感染的应用程序中;其二是System Integrity Protection (SIP)，阻止合法的文件接触敏感文件。但在尚未打补丁的旧系统上，这两个安全机制都无法阻止该漏洞。</p><p style="text-align:center"><img src="https://static.cnbetacdn.com/article/2022/0817/22890f5fe344d59.webp" referrerpolicy="no-referrer"></p><p style="text-align: left;">在用户设备处于闲置状态或者关机的时候，该漏洞可以通过劫持的方式暂停 macOS 程序。在应用需要唤醒的时候，该系统可以在不记录保存状态的情况下读取某些文件。该保存状态不如应用在正常运行期间的安全性。</p><p style="text-align: left;">网络安全专家 Thijs Alkemade 在重新激活已经停止的应用之后，找到了修改 macOS 读取文件的方式，这让他以系统不希望的方式运行代码。Alkemade 重申这个漏洞可以跳转不同的应用，最终绕过 SIP 来更改某系系统文件。</p>   
</div>
            