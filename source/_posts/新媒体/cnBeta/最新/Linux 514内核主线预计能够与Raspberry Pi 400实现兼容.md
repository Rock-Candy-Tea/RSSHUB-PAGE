
---
title: 'Linux 5.14内核主线预计能够与Raspberry Pi 400实现兼容'
categories: 
 - 新媒体
 - cnBeta
 - 最新
headimg: 'https://static.cnbetacdn.com/article/2021/0614/c4b4af99151c214.jpg'
author: cnBeta
comments: false
date: Mon, 14 Jun 2021 11:45:17 GMT
thumbnail: 'https://static.cnbetacdn.com/article/2021/0614/c4b4af99151c214.jpg'
---

<div>   
<strong>去年11月推出的Raspberry Pi 400是一款Raspberry Pi键盘电脑，它实际上是将Raspberry Pi 4
SBC嵌入到键盘中，并整合到一个大铝块上。</strong>对于一贯简约的树莓派产品而言，这是一个很好的小设备，并且从Linux
5.14开始，它看起来应该可以和主线内核完美兼容。<br>
 <p><img src="https://static.cnbetacdn.com/article/2021/0614/c4b4af99151c214.jpg" title alt="1.jpg" referrerpolicy="no-referrer"></p><p>购买Raspberry Pi 400的价格需要100美元，可以得到内置Raspberry Pi的键盘，它提供4GB内存、1.8GHz四核Broadcom处理器、16GB存储空间和相关的外围设备，这一点花费便可以使买家拥有一台可以完全工作的电脑，除了一台显示器外不需要配备任何额外的东西。</p><p>使Raspberry Pi 400更有吸引力的是，主线内核支持即将到来，上周排入SoC/SoC "for-next"分支的补丁是为Raspberry Pi 400增加的DeviceTree。由于它基本上与Raspberry Pi 4非常接近，所以不需要改变内核驱动，但由于1.8GHz的时钟频率、不同的WiFi芯片、通过GPIO处理断电以及400型号上没有ACT LED，所以需要更新DTS配置。</p><p><img src="https://static.cnbetacdn.com/article/2021/0614/9c71ef7179bff0c.jpg" title alt="image.jpg" referrerpolicy="no-referrer"></p><p>这一切也要归功于现在排在Linux 5.14内核之前的SoC的下一个Git分支中开发人员的努力，Raspberry Pi 400的支持现在应该是好的。有点遗憾的是，花了这么多月的时间，这个相对简单的附加功能才准备好进入主线。</p><p><strong>访问了解更多细节：</strong></p><p><a href="https://git.kernel.org/pub/scm/linux/kernel/git/soc/soc.git/commit/?h=for-next&id=1c701accecf21932ebcbd8acacb4557af3797e77" _src="https://git.kernel.org/pub/scm/linux/kernel/git/soc/soc.git/commit/?h=for-next&id=1c701accecf21932ebcbd8acacb4557af3797e77" target="_blank">https://git.kernel.org/pub/scm/linux/kernel/git/soc/soc.git/commit/?h=for-next&id=1c701accecf21932ebcbd8acacb4557af3797e77</a><br></p>   
</div>
            