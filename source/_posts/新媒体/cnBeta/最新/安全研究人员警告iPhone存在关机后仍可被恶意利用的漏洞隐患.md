
---
title: '安全研究人员警告iPhone存在关机后仍可被恶意利用的漏洞隐患'
categories: 
 - 新媒体
 - cnBeta
 - 最新
headimg: 'https://static.cnbetacdn.com/article/2022/0517/cc0e959020146b8.png'
author: cnBeta
comments: false
date: Tue, 17 May 2022 06:40:54 GMT
thumbnail: 'https://static.cnbetacdn.com/article/2022/0517/cc0e959020146b8.png'
---

<div>   
<strong>德国达姆施塔特工业大学的一支研究团队，刚刚披露了一种可将恶意软件加载到 iPhone 上的新手段。更糟糕的是，攻击者甚至可在设备处于关机状态时得逞。</strong>虽然尚无证据表明该漏洞已被野外利用、甚至可能需要搭配其它攻击手段，但对于设备制造商苹果来说，这依然是个相当烫手的山芋。<br>
<p><img src="https://static.cnbetacdn.com/article/2022/0517/cc0e959020146b8.png" referrerpolicy="no-referrer"></p><p style="text-align: center;">研究配图 - 1：<a data-link="1" href="https://apple.pvxt.net/c/1251234/435400/7639?u=https%3A%2F%2Fwww.apple.com%2Fcn%2Fiphone%2F" target="_blank">iPhone</a> 的“储备电量模式”（Power Reserve Mode）</p><p><a href="https://www.techspot.com/news/94611-researchers-claim-malware-can-loaded-onto-iphones-have.html" target="_self">TechSpot</a> 指出：这项漏洞利用与 iOS 15 中的一项功能有关，允许 Find My 在设备关机后仍持续工作数小时。</p><p>具体说来是，用于蓝牙、近场通讯（NFC）和超宽带（UWB）的芯片，即使在用户关机后、仍会已低功耗（LPM）模式继续运行。</p><p><img src="https://static.cnbetacdn.com/article/2022/0517/1a624b099f87c33.png" referrerpolicy="no-referrer"></p><p style="text-align: center;">研究配图 - 2：<a data-link="1" href="https://apple.pvxt.net/c/1251234/435400/7639?u=https%3A%2F%2Fwww.apple.com%2Fcn%2Fmusic%2F" target="_blank">苹果</a>官方文档中的 Secure Element 与 SEP 安全飞地处理器示意</p><p>这种特殊的模式，与您在正常使用 iPhone 时、于“低电量”状态下开启的“黄色电池指示图标”并不是一码事。</p><p>可知在评估 LPM 功能时，该校研究团队发现蓝牙 LPM 固件既无签名、也未加密。</p><p><img src="https://static.cnbetacdn.com/article/2022/0517/5f9c4bcb9015b1f.png" referrerpolicy="no-referrer"></p><p style="text-align: center;">研究配图 - 3：iOS 15 的关机滑动对话框</p><p>然而在适当的触发条件下，研究团队声称可修改此固件以运行恶意软件 —— 有利于攻击者的条件包括对 iPhone 进行越狱、且最好获得系统级访问权限。</p><p>如果你已经已经放权，那这里提到的蓝牙芯片漏洞利用可能就是多此一举了。即便如此，研究人员还是及时地向苹果通报了相关问题，但这家库比蒂诺科技巨头没有立即回应 <a href="https://www.vice.com/en/article/g5q4vj/malware-can-be-loaded-even-onto-phones-that-are-turned-off-researchers-show" target="_self">Motherboard</a> 的置评请求。</p><p><img src="https://static.cnbetacdn.com/article/2022/0517/928fcf9c40b6add.png" referrerpolicy="no-referrer"></p><p style="text-align: center;">研究配图 - 4：iPhone 11-13 机型上的新 Secure Element 与芯片内接口</p><p>庆幸的是，安全研究员 Ryan Duff 表示：“在缺乏额外漏洞利用的情况下，攻击者难以单独借此发起攻击”。</p><p>但若攻击者有机会直接利用到蓝牙芯片并修改固件（目前尚不知晓有类似的漏洞利用），事情就会变得相当棘手。</p><p><img src="https://static.cnbetacdn.com/article/2022/0517/cff892e35e15f36.png" referrerpolicy="no-referrer"></p><p style="text-align: center;">即使 iPhone 处于关机状态，黑客仍可利用该漏洞来定位用户设备。</p><p>最后，在 2022 年 5 月的 Arxiv 预印版（<a href="https://arxiv.org/pdf/2205.06114.pdf" target="_self">PDF</a>）报告中，研究团队警告称 LPM 是一个必须保持高度警惕的攻击面。</p><p>若被别有用心的人染指，以在关机后的 iPhone 上部署无线型的恶意软件，后果将不堪设想。</p>   
</div>
            