
---
title: 'iOS又一Bug：特殊Wi-Fi热点名称会导致iPhone无线连接功能异常'
categories: 
 - 新媒体
 - cnBeta
 - 最新
headimg: 'https://static.cnbetacdn.com/article/2021/0620/1818eee00391f56.jpg'
author: cnBeta
comments: false
date: Sun, 20 Jun 2021 01:05:48 GMT
thumbnail: 'https://static.cnbetacdn.com/article/2021/0620/1818eee00391f56.jpg'
---

<div>   
<strong>安全研究员 Carl Schou 刚刚发现了 iOS 中的又一个 Bug，如果 iPhone 尝试连接到具有特殊名称的 Wi-Fi 热点，很可能导致设备的无线连接功能异常。</strong>首先，他建立了一个名叫“%p%s%s%s%s%n”的无线热点名称。但在初次尝试连接时，Carl Schou 发现根本无法连上。然后通过进一步的尝试，设备上的 Wi-Fi 连接功能干脆被彻底禁用了。<br>
 <p><img src="https://static.cnbetacdn.com/article/2021/0620/1818eee00391f56.jpg" referrerpolicy="no-referrer"></p><p>据 Bleeping Computer 所述，即便后续尝试连接其它 Wi-Fi 热点，这一“传染病”也无法被治愈。更糟糕的是，在变更热点 SSID 名称并重启 <a data-link="1" href="https://apple.pvxt.net/c/1251234/435400/7639?u=https%3A%2F%2Fwww.apple.com%2Fcn%2Fiphone%2F" target="_blank">iPhone</a> 之后，问题也依然存在。</p><p>接着一群人分别测试了相同的故障 SSID 名称，结果也纷纷以躺枪姿态证实了该问题。作为对比，Android 移动设备能够毫无问题地连接到“名称异常”的无线接入点。</p><p><img src="https://static.cnbetacdn.com/article/2021/0620/f77a229e68b29d4.png" referrerpolicy="no-referrer"></p><p>一些研究人员认为，该问题或与 iOS 对 Wi-Fi 热点名称的“输入解析”bug 有关。因为 SSID 开头的百分比符号，可能被操作系统误认为是字符串格式的说明符。</p><p>结果就是 % 之后的这串字符被当做了所谓的变量，而不是纯文本格式。<strong>对于已经不幸中招的用户来说，只能在重置网络设置后，才能让 iOS 设备的 Wi-Fi 连接功能恢复正常，方法如下：</strong></p><blockquote><p>● 打开‘设置’；</p><p>● 进入‘通用’；</p><p>● 选择‘重置网络设置’；</p><p>● 确认请求；</p><p>● 待 iPhone 重启后，再尝试照常设置 Wi-Fi 。</p></blockquote><p><img src="https://static.cnbetacdn.com/article/2021/0620/5b3e155c99f6297.gif" referrerpolicy="no-referrer"></p><p>当然，这并不是我们首次见到<a data-link="1" href="https://apple.pvxt.net/c/1251234/435400/7639?u=https%3A%2F%2Fwww.apple.com%2Fcn%2Fmusic%2F" target="_blank">苹果</a>设备因为遇到特殊字符串而出现功能异常。比如几年前，iPhone / <a data-link="1" href="https://apple.pvxt.net/c/1251234/435400/7639?u=https%3A%2F%2Fwww.apple.com%2Fcn%2Fipad%2F" target="_blank">iPad</a> 就被某些基于特殊表情符号或特定德语字符的传入通知（又称“文本炸弹”）而导致设备崩溃。</p><p>此外更早的时候，一些有心的用户也可能发现，某些移动设备是无法正确检索或识别纯中文格式的无线热点 SSID 名称的。</p>   
</div>
            