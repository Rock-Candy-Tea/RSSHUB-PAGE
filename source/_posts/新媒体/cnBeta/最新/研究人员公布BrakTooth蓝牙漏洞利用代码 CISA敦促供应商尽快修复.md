
---
title: '研究人员公布BrakTooth蓝牙漏洞利用代码 CISA敦促供应商尽快修复'
categories: 
 - 新媒体
 - cnBeta
 - 最新
headimg: 'https://static.cnbetacdn.com/article/2021/1110/135bfee091079c3.png'
author: cnBeta
comments: false
date: Wed, 10 Nov 2021 01:40:30 GMT
thumbnail: 'https://static.cnbetacdn.com/article/2021/1110/135bfee091079c3.png'
---

<div>   
随着公开漏洞利用代码和一款概念验证工具的发布，<strong>美国网络与基础设施安全局（CISA）也及时地向供应商发去了通报，以敦促其尽快修复影响数十亿设备（手机 / PC / 玩具）的拒绝服务（DoS）和代码执行攻击漏洞。</strong>ThreatPost 指出，用于测试新曝光的蓝牙 BrakTooth 漏洞的概念验证工具的保密期已结束，相关测试套件和完整漏洞利用代码现已向公众开放访问。<br>
 <p><img src="https://static.cnbetacdn.com/article/2021/1110/135bfee091079c3.png" alt="0.png" referrerpolicy="no-referrer"></p><p style="text-align: center;">BrakTooth 漏洞检测与利用工具概念验证代码已上线 GitHub（来自：<a href="https://us-cert.cisa.gov/ncas/current-activity/2021/11/04/braktooth-proof-concept-tool-demonstrates-bluetooth" target="_self">CISA</a>）</p><p>据悉，BrakTooth 是一系列影响 1400 多款蓝牙商用产品的缺陷，数十亿受影响的设备都依赖于经典蓝牙协议来通讯。</p><p>正如原文指出的那样，攻击者只需找到现成的售价仅 14.80 美元的 ESP32 板子（AliExpress 上的同类产品甚至低到 4 美元）。</p><p>然后利用自定义链接管理协议（LMP）固件，即可在计算机上运行 BrakTooth 漏洞的概念验证攻击代码。</p><p><img src="https://static.cnbetacdn.com/article/2021/1110/3a124efd6f43bda.jpg" alt="1.jpg" referrerpolicy="no-referrer"></p><p style="text-align: center;">受影响的蓝牙 SoC 厂商与型号列表</p><p>早在 9 月发表的一篇<a href="https://asset-group.github.io/disclosures/braktooth/" target="_self">论文</a>中，新加坡大学研究人员就已经披露了最初的 16 个漏洞（现已多达 22 个），并将其统称为“BrakTooth”。</p><p>他们在 1400 多款嵌入式芯片组件中所使用的闭源商用 BT 堆栈中发现了漏洞，并详细说明了它们可能导致的一系列攻击类型。除了常见的拒绝服务（DoS），其中一个漏洞还可能导致任意代码执行（ACE）。</p><p>自论文发表以来，已有不少厂商发布了修补更新。与此同时，研究人员也曝光了更多易受攻击的设备，甚至<a data-link="1" href="https://apple.pvxt.net/c/1251234/435400/7639?u=https%3A%2F%2Fwww.apple.com%2Fcn%2Fmusic%2F" target="_blank">苹果</a> <a data-link="1" href="https://apple.pvxt.net/c/1251234/435400/7639?u=https%3A%2F%2Fwww.apple.com%2Fcn%2Fiphone%2F" target="_blank">iPhone</a> 智能机 / <a data-link="1" href="https://apple.pvxt.net/c/1251234/435400/7639?u=https%3A%2F%2Fwww.apple.com%2Fcn%2Fmac%2F" target="_blank">MacBook</a> 笔记本电脑也未能幸免。</p><p>此外 BrakTooth 漏洞还影响到了<a data-link="1" href="https://c.duomai.com/track.php?site_id=242986&euid=&t=https://www.microsoftstore.com.cn/" target="_blank">微软</a> <a data-link="1" href="https://microsoft.pvxt.net/9W473" target="_blank">Surface</a>、<a data-link="1" href="http://www.anrdoezrs.net/links/9019719/type/dlg/sid//https://www.dell.com/zh-cn/shop/deals" target="_blank">戴尔</a>台式 / 笔记本电脑、索尼 / <a data-link="1" href="https://c.duomai.com/track.php?site_id=242986&euid=&t=https://oppo.jd.com/" target="_blank">OPPO</a> 智能机、以及沃尔玛 / 松下等品牌的音频设备。</p><p><img src="https://static.cnbetacdn.com/article/2021/1110/5b36670728e4f65.jpg" alt="2.jpg" referrerpolicy="no-referrer"></p><p style="text-align: center;">受影响设备的漏洞补丁状态和 SDK / 固件版本</p><p>截止 9 月，该团队已分析 11 家供应商的 13 款 BT 硬件，并列出了 20 份通用漏洞披露（CVE）公告 —— 其中四个来自英特尔和高通。</p><p>不久后，高通发布了 V6（8.6）和 V15（8.15）的 CVE，但研究人员指出或许仍有许多其它产品未被他们统计在内，比如片上系统（SoC）、BT 模块和其它 BT 终端产品。</p><p>周一的时候，芯片组供应商 Airoha、联发科和<a data-link="1" href="https://c.duomai.com/track.php?site_id=242986&euid=&t=https://samsung.jd.com/" target="_blank">三星</a>陆续披露了旗下某些设备易受攻击的报告。</p><p>英特尔、高通和三星的部分设备仍在等待补丁，但来自高通和德州仪器（TI）的某些产品已被列入不打算修复的列表，还有不少供应商正在调查此问题。</p>   
</div>
            