
---
title: 浅谈 Android 的安全启动和完整性保护 (evilpan.com)
categories: 
    - 编程
    - 技术头条 - 最新分享
author: 技术头条 - 最新分享
comments: false
date: 2021-03-21 16:41:04
thumbnail: 
---

<div>   
在 IoT 中保证设备安全性的重要一环就是保证代码的完整性，不让恶意代码影响业务的正常逻辑。一般而言是及时修复现有攻击面所面临的漏洞，比如浏览器、蓝牙、调试接口；另一方面需要确保的是即便恶意代码获取了执行权限，也无法修改系统镜像进行持久化。针对这点所构造的安全方案通常称为 Secure Boot，对于不同的厂商，实现上可能会引入不同的名字，比如 Verified Boot、High Assurance Boot 等等，但本质上都是类似的。
    
</div>
            