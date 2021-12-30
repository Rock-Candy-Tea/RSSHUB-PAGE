
---
title: '微软解释在Windows 11上为何部分驱动可追溯到1968年'
categories: 
 - 新媒体
 - cnBeta
 - 最新
headimg: 'https://static.cnbetacdn.com/article/2021/1230/95a93aab296db42.webp'
author: cnBeta
comments: false
date: Thu, 30 Dec 2021 02:08:21 GMT
thumbnail: 'https://static.cnbetacdn.com/article/2021/1230/95a93aab296db42.webp'
---

<div>   
<strong>如果你经常检查 Windows 10/11 的更新，那么你可能已经注意到可选更新提供的部分驱动是陈旧或者失效的。</strong>在过去几年里，用户收到的驱动程序更新被列为“INTEL - System”，尽管在升级到 Windows 11 之后就已经交付，但它的日期却追溯到 1968 年。<br>
 <p style="text-align:center"><img src="https://static.cnbetacdn.com/article/2021/1230/95a93aab296db42.webp" alt="1wvmol6v.webp" referrerpolicy="no-referrer"></p><p style="text-align: left;">由于奇怪的规格，这些驱动程序大多数看起来很有问题。<a href="https://devblogs.microsoft.com/oldnewthing/20211221-00/?p=106046" target="_blank">在一篇新的博客文章中，</a>微软已经解释了为什么以及如何在 Windows 上对这些驱动程序进行追溯。目前，在 Windows 平台上发布的驱动程序有三大来源，其一是由 Windows/Microsoft 发布的，其二是由 Intel/NVIDIA 等公司发布的，还有就是由 PC 制造商发布的定制驱动程序。</p><p style="text-align: left;">微软表示所有 Windows 驱动程序的日期都被设定为 2006 年 6 月 21 日，以减少兼容性问题。Windows Update 根据包括日期在内的各种因素对驱动程序进行排名。例如，如果微软的驱动程序库中的一个驱动程序与设备的硬件 ID 完全匹配，那么它将成为最重要的候选者，用户将能够下载它。</p><p style="text-align: left;">然而，如果有一个以上的驱动程序与硬件 ID 相匹配，则会自动选择一个具有最新时间戳的驱动程序。如果在这种情况下，多个驱动程序之间也存在平局，微软将看与构建发布日期相匹配的最高文件版本号。</p><p style="text-align: left;">但是有一个问题--<strong>当你安装一个新的 Windows 版本时，Windows 驱动将自动拥有比制造商提供的时间戳更新的时间戳。因此，你的制造商驱动将被 Windows 驱动取代，这可能会破坏你设备上的特定功能。</strong>Windows 驱动显然是为了避免上面强调的情况而被追溯的。</p><p style="text-align: left;"><strong>通过追溯Windows驱动，微软允许制造商的驱动保留比Windows提供的驱动更优先的地位。</strong>在另一份文件中，微软表示，英特尔的驱动程序被追溯到 1968 年（英特尔成立的那一年），也是出于同样的原因--<strong>当制造商的驱动程序可用时，降低英特尔的驱动程序的等级。</strong></p><p style="text-align: left;">英特尔在一篇现已删除的博文中指出：“这是必要的，因为它是一个支持性的工具，不应该覆盖任何其他的驱动程序。更新英特尔(R)芯片组设备软件是不需要的--如果你没有最新的版本，请不要担心”。</p>   
</div>
            