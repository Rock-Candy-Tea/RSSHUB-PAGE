
---
title: '新Linux补丁已实现在苹果M1_T2平台启用Wi-Fi支持'
categories: 
 - 新媒体
 - cnBeta
 - 最新
headimg: 'https://static.cnbetacdn.com/article/2021/1227/647a304e94653b4.webp'
author: cnBeta
comments: false
date: Mon, 27 Dec 2021 01:26:33 GMT
thumbnail: 'https://static.cnbetacdn.com/article/2021/1227/647a304e94653b4.webp'
---

<div>   
去年 12 月，秉承着“万物皆可 Linux”的理念，知名开发者赫克托·马丁（Hector Martin）正发起众筹 Asahi Linux 项目，计划为 Apple Silicon Mac 设备移植 Linux 系统。<strong>在今天放出的初期“征求意见”系列补丁中，大神 Martin 成功让 Broadcom “BRCMFMAC”驱动程序能够在 M1 SoC 以及苹果 T2 平台上支持无线局域网。</strong><br>
 <p style="text-align:center"><img src="https://static.cnbetacdn.com/article/2021/1227/647a304e94653b4.webp" alt="ifmddr3e.webp" referrerpolicy="no-referrer"></p><p style="text-align: left;">Asahi Linux 项目目标是在 Linux 下实现对 Apple Silicon ARM 的支持，他发出了一套 34 个 RFC 补丁，以支持 Apple T2 和 M1 平台与这个上游 Broadcom 开源网络驱动器。这些补丁已经用<a data-link="1" href="https://apple.pvxt.net/c/1251234/435400/7639?u=https%3A%2F%2Fwww.apple.com%2Fcn%2Fmusic%2F" target="_blank">苹果</a> T2/M1 平台使用的 Broadcom FullMAC 硬件进行了测试，包括 BCM4355C1、BCM4364B2/B3、BCM4377B3、BCM4378B1 和 BCM4387C2。</p><p style="text-align: left;">Martin 在补丁封面信中指出：“像苹果公司一样，这些机器上的东西与其他每一个Broadcom平台都略有不同。特别是，除了正常的设备/固件支持变化外，这一系列中的很大一部分涉及到选择和加载正确的固件。这些平台使用多个维度进行固件选择，而这些维度的值则不同程度地来自于DT或OTP”。</p><p style="text-align:center"><img src="https://static.cnbetacdn.com/article/2021/1227/3668158a5fa6393.webp" alt="lzh4jxoo.webp" referrerpolicy="no-referrer"></p><p style="text-align: left;">为使苹果 M1/T2 平台能够与现有的 Broadcom Linux 内核驱动一起工作，支持 WiFi，他编写了超过一千行的内核代码。如果感兴趣，<a href="https://lore.kernel.org/linux-acpi/20211226153624.162281-1-marcan@marcan.st/" target="_blank">请看 RFC 补丁系列的所有细节。</a></p>   
</div>
            