
---
title: '对苹果M1的初步支持如约在Linux 5.13内核中出现'
categories: 
 - 新媒体
 - cnBeta
 - 最新
headimg: 'https://static.cnbetacdn.com/article/2021/0317/598784650e0ec4f.png'
author: cnBeta
comments: false
date: Mon, 26 Apr 2021 23:57:44 GMT
thumbnail: 'https://static.cnbetacdn.com/article/2021/0317/598784650e0ec4f.png'
---

<div>   
<strong>正如预期的那样，早期对苹果M1 SoC支持和2020年Apple Silicon设备（Mac Mini、MacBook Pro、MacBook
Air）的支持已经加入Linux 5.13内核。</strong>在Linux 5.13合并窗口的第一天，各种ARM
SoC/平台的拉动请求被提交，并且已经被合并到主线。<br>
 <p><a href="https://static.cnbetacdn.com/article/2021/0317/598784650e0ec4f.png" target="_blank"><img src="https://static.cnbetacdn.com/article/2021/0317/598784650e0ec4f.png" referrerpolicy="no-referrer"></a></p><p>最值得注意的是Apple M1 / Apple Silicon SoC和当前设备支持。但请记住，这是非常初步的支持，在真正准备好用于日常使用之前，还有很多工作要做，例如对加速图形的支持都还不到位，希望其余的工作将在不远的将来到来，让这些新一代的<a data-link="1" href="https://apple.pvxt.net/c/1251234/435400/7639?u=https%3A%2F%2Fwww.apple.com%2Fcn%2Fmusic%2F" target="_blank">苹果</a>设备能够为Linux上的日常用户所使用。</p><p>除了对苹果的ARM工作正在加强之外，Linux 5.13还增加了对旧的ARM Nuvoton WPCM450平台的支持。WPCM450因为是被Supermicro X9服务器主板和其他一些服务器主板中的BMC运用而备受关注。</p><p>Linux 5.13的DeviceTree更新支持意法半导体STM32H750、恩智浦i.MX8QuadMax、高通SC7280和TI AM64x Sita4ra。</p><p><img src="https://static.cnbetacdn.com/article/2021/0427/06793a4451bc48b.png" title alt="0OBF)4GK0Z9FC56IL9C$HSF.png" referrerpolicy="no-referrer"></p><p><strong>新增加的硬件支持包括：</strong></p><p>- ASpeed AST2500 BMC：华擎E3C246D4I Xeon服务器主板</p><p>- 全志A10：Topwise A721平板</p><p>- Amlogic GXL。MeCool KII<a data-link="1" href="https://c.duomai.com/track.php?site_id=242986&euid=&t=https%3A%2F%2Flist.jd.com%2Flist.html%3Fcat%3D737%2C794%2C798%26ev%3D4155_76344%26sort%3Dsort_rank_asc%26trans%3D1%26JL%3D2_1_0%23J_crumbsBar" target="_blank">电视</a>盒</p><p>- 晶晨GXM：Mecool KIII, Minix Neo U9-H电视盒</p><p>- 博通BCM4908: TP-Link Archer C2300 V1<a data-link="1" href="https://c.duomai.com/track.php?site_id=242986&euid=&t=https://list.jd.com/list.html?cat=670,699,700" target="_blank">路由器</a></p><p>- MStar <a data-link="1" href="https://c.duomai.com/track.php?site_id=242986&euid=&t=https://list.jd.com/list.html?cat=670,677,11303" target="_blank">SSD</a>202D: M5Stack UnitV2摄像头</p><p>- Marvell Armada 38x: ATL-x530以太网交换机</p><p>- 联发科MT8183 Chromebooks: 联想10e，<a data-link="1" href="https://c.duomai.com/track.php?site_id=242986&euid=&t=https://acer-pc.jd.com/" target="_blank">宏碁</a>Spin 311，<a data-link="1" href="https://c.duomai.com/track.php?site_id=242986&euid=&t=https://asus.jd.com/" target="_blank">华硕</a>Flip CM3，华硕Detachable CM3</p><p>- 联发科MT8516/MT8183 OLogic Pumpkin Board</p><p>- 恩智浦i.MX7：reMarkable平板电脑</p><p>- 恩智浦i.MX8M: Kontron  pitx-imx8m, Engicam i.Core MX8M Mini</p><p>- Nuvoton NPCM730: 广达GBS BMC</p><p>- 高通X55：Telit FN980 TLB SoM，Thundercomm TurboX T55 SoM</p><p>- 高通MSM8998：OnePlus 5/5T<a data-link="1" href="https://c.duomai.com/track.php?site_id=242986&euid=&t=https://shouji.jd.com/" target="_blank">手机</a></p><p>- 高通SM8350：骁龙888移动硬件开发套件</p><p>- 瑞芯微RK3399：NanoPi R4S板</p><p>- STM32MP1：Engicam MicroGEA STM32MP1 MicroDev 2.0和SOM，EDIMM2.2入门套件，Carrier，SOM</p><p>- TI AM65：西门子SIMATIC IOT2050网关</p><p>总的来说，这是为Linux 5.13提供的一组令人兴奋的ARM硬件补充。</p><div class="article-relation"><p><strong>相关文章:</strong></p><p><a href="https://www.cnbeta.com/articles/tech/1119497.htm" target="_blank">Linux 5.13将为英特尔Alder Lake处理器添加perf支持</a></p><p><a href="https://www.cnbeta.com/articles/tech/1120257.htm" target="_blank">Linux 5.13增加来自英特尔的KCPUID组件 帮助准确识别新推出的CPU</a></p><p><a href="https://www.cnbeta.com/articles/tech/1120261.htm" target="_blank">Linux 5.13合并窗口拉开序幕：微软Surface改进、技嘉WMI驱动……</a></p></div>   
</div>
            