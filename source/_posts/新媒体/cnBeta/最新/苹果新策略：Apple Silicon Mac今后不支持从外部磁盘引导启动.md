
---
title: '苹果新策略：Apple Silicon Mac今后不支持从外部磁盘引导启动'
categories: 
 - 新媒体
 - cnBeta
 - 最新
headimg: 'https://static.cnbetacdn.com/thumb/article/2021/0525/b6c2834271da99c.jpg'
author: cnBeta
comments: false
date: Tue, 25 May 2021 03:42:21 GMT
thumbnail: 'https://static.cnbetacdn.com/thumb/article/2021/0525/b6c2834271da99c.jpg'
---

<div>   
<strong>由于苹果正逐步淘汰外部磁盘的创建和使用，使用 Apple Silicon 的 Mac 设备今后将无法从外部移动磁盘启动。</strong>对于部分用户来说，为他们的 Mac 创建可引导的磁盘能够额外添加安全保障，防止 Mac 上的主磁盘损坏或者遇到其他问题。但伴随着苹果逐渐朝着 Apple Silicon 芯片过渡，这种可以让用户快速恢复运行的备份技术将不再获得支持。<br>
 <p style="text-align:center"><a href="https://static.cnbetacdn.com/article/2021/0525/b6c2834271da99c.jpg" target="_blank"><img src="https://static.cnbetacdn.com/thumb/article/2021/0525/b6c2834271da99c.jpg" alt="76ym7qj4.jpg" referrerpolicy="no-referrer"></a></p><p style="text-align: left;">知名软件 Carbon Copy Cloner（以下简称 CCC） 的开发商 Bombich 创始人 Mike Bombich 在 5 月 19 日的一篇博文中写道，该公司将会继续为<a data-link="1" href="https://c.duomai.com/track.php?site_id=242986&euid=&t=https://intel.jd.com/" target="_blank">英特尔</a>和 Apple Silicon 的 Mac 设备提供可引导启动备份，只要 macOS 支持该功能就会继续提供支持。</p><p style="text-align: left;">然而随着 Apple Silicon 的引入，Mac 的功能发生了变化，使用外部启动的能力可能受到限制，部分原因是<a data-link="1" href="https://apple.pvxt.net/c/1251234/435400/7639?u=https%3A%2F%2Fwww.apple.com%2Fcn%2Fmusic%2F" target="_blank">苹果</a>的设计决定。</p><p style="text-align: left;">第一个问题是 macOS Big Sur，因为苹果使 macOS 驻留在一个“密密封的签名系统卷”加上，这只能由苹果软件还原来复制。虽然 CCC 有使用软件还原（ASR）程序的能力，但该工具被认为是不完<a data-link="1" href="https://c.duomai.com/track.php?site_id=242986&euid=&t=https://mideajiadian.jd.com/" target="_blank">美的</a>，它的失败 "没有任何解释"，并且以 "非常单一 "的方式操作。</p><p style="text-align: left;">第二个障碍是 Apple Fabric，一个使用每个文件加密密钥的存储系统。ASR 曾几个月内没有工作，直到 macOS 11.3 的发布才恢复了它。在克隆回原来的内部存储时，内核恐慌也随之而来。</p><p style="text-align: left;">去年 12 月，Bombich 表示：“我们Mac社区的许多人都能看出这是苹果的发展方向，现在我们终于得到了确认。特别是自从引入APFS以来，苹果一直在朝着锁定macOS系统文件的方向发展，为提高安全性牺牲了一些便利性”。</p><p style="text-align: left;">在2月份的一份产品安全文件中发现了一个变化，Bombich指出，它提到Apple Silicon质Mac的启动过程总是由内部存储器上的一个卷来推动的。该卷上的轻量级操作系统会评估启动资产的完整性，并在从该卷启动之前对该外部设备上的操作系统进行认证。</p><p style="text-align: left;">他说：“从理论上讲，这意味着如果内部存储出现故障，Apple Silicon 电脑根本无法启动”。苹果公司内部的专家向 Bombich "明确地确认"，如果内部存储失效，你不能从外部启动驱动器启动 Apple Silicon Mac。</p>   
</div>
            