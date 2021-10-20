
---
title: 'Linux 5.16将支持2021年款苹果Magic Keyboard'
categories: 
 - 新媒体
 - cnBeta
 - 最新
headimg: 'https://static.cnbetacdn.com/article/2021/1020/4accb5aa737b3b4.jpg'
author: cnBeta
comments: false
date: Wed, 20 Oct 2021 13:55:39 GMT
thumbnail: 'https://static.cnbetacdn.com/article/2021/1020/4accb5aa737b3b4.jpg'
---

<div>   
<strong>除了所有正在进行的为Linux内核带来Apple Silicon/M1兼容性的工作外，Linux 5.16的开发周期将支持今年发布的Apple
Magic Keyboard。</strong>通过Apple-HID驱动，Linux内核已经支持早期版本的Magic
Keyboard，以处理围绕该键盘的设备差异，这些特异性需要由软件特别处理以充分利用键盘，例如功能键（Fn）。<br>
 <p><img src="https://static.cnbetacdn.com/article/2021/1020/4accb5aa737b3b4.jpg" title alt="image.jpg" referrerpolicy="no-referrer"></p><p>早在4月，<a data-link="1" href="https://apple.pvxt.net/c/1251234/435400/7639?u=https%3A%2F%2Fwww.apple.com%2Fcn%2Fmusic%2F" target="_blank">苹果</a>Magic Keyboard就推出了2021年的更新版，作为这种蓝牙连接键盘的最新版本。2021年的Magic Keyboard增加了一个Touch ID传感器，但这个指纹识别功能的Linux的兼容性并不在开发计划内。</p><p>最新补丁被HID子系统的"for-5.16"Git分支所采纳。这一驱动程序的增加使键盘与HID-Apple驱动程序一起工作。只需添加新的ID（0x029c），并向驱动说明是否有Fn键就可以了。</p><p>如果想在Linux下使用最新的苹果魔法键盘，这是一个简单但重要的补充。</p><p><strong>了解更多：</strong></p><p><a href="https://git.kernel.org/pub/scm/linux/kernel/git/hid/hid.git/commit/?h=for-5.16/apple&id=0cd3be51733febb4f8acb92bcf55b75fe824dd05" _src="https://git.kernel.org/pub/scm/linux/kernel/git/hid/hid.git/commit/?h=for-5.16/apple&id=0cd3be51733febb4f8acb92bcf55b75fe824dd05" target="_blank">https://git.kernel.org/pub/scm/linux/kernel/git/hid/hid.git/commit/?h=for-5.16/apple&id=0cd3be51733febb4f8acb92bcf55b75fe824dd05</a><br></p>   
</div>
            