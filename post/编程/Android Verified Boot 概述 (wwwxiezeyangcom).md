
---
title: Android Verified Boot 概述 (www.xiezeyang.com)
categories: 
    - 编程
    - 技术头条 - 最新分享
author: 技术头条 - 最新分享
comments: false
date: 2021-03-21 16:41:04
thumbnail: 
---

<div>   
Verified Boot是Google为Android启动定义的一种安全机制。它建立了一条从受硬件保护的Root of trust到booloader，再到boot和其它验证分区（包括system、vendor、product、odm等）的完整信任链。在设备启动的过程中，无论处于哪个阶段，都会在进入下一个阶段前先验证下一个阶段的完整性和真实性。除了确保设备运行的是安全的Android系统以外，verified boot还支持回滚保护（anti-roll back），它可以保证设备只会更新到更高版本，以避免可能的漏洞持续存在。另外，verified boot还允许设备将其完整性传到给终端用户。

要想使能verified boot，需要在编译系统中启用dm-verity功能。Android 4.4就增加了对验证启动和 dm-verity 内核功能的支持。以前的Android版本会在发现设备损坏时向用户发出警告，但仍允许他们启动设备。从Android 7.0 开始，系统会严格强制执行verified boot，从而使得遭到入侵的设备无法启动，与此同时还增加了对向前纠错功能的支持，能更可靠地防范非恶意数据损坏。Android 8.0及更高版本包含了 Android Verified Boot (AVB)功能。其实AVB就是验证启动的一个参考实现，可与 Project Treble 配合使用。除此之外，AVB 还对分区脚本格式进行了标准化处理，并增添了回滚保护功能。为了便于区分，我们一般将此之前的verified boot称为1.0版，而AVB专指verified boot 2.0版。
    
</div>
            