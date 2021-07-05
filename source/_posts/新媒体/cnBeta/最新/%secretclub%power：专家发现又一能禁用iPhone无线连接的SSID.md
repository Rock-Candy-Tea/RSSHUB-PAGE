
---
title: '%secretclub%power：专家发现又一能禁用iPhone无线连接的SSID'
categories: 
 - 新媒体
 - cnBeta
 - 最新
headimg: 'https://static.cnbetacdn.com/article/2021/0705/1c6e26eb76f4342.jpg'
author: cnBeta
comments: false
date: Mon, 05 Jul 2021 01:50:43 GMT
thumbnail: 'https://static.cnbetacdn.com/article/2021/0705/1c6e26eb76f4342.jpg'
---

<div>   
在处理 Wi-Fi 热点名称上，iOS 系统中存在的漏洞要比之前预想的更加严重。<strong>iPhone 在发现畸形的 SSID 无线网络之后就会完全禁用 iPhone 的 Wi-Fi 接入，需要重置出厂才能修复这个问题。</strong><br>
<p style="text-align:center"><img src="https://static.cnbetacdn.com/article/2021/0705/1c6e26eb76f4342.jpg" alt="QQ截图20210705094808.jpg" referrerpolicy="no-referrer"></p><p style="text-align: left;">今年 6 月，网络安全专家 Carl Schou 发现，只要 <a data-link="1" href="https://apple.pvxt.net/c/1251234/435400/7639?u=https%3A%2F%2Fwww.apple.com%2Fcn%2Fiphone%2F" target="_blank">iPhone</a> 用户连接 SSID 名为“%p%s%s%s%n”的无线热点，iOS 设备就会禁用 Wi-Fi 连接。虽然这个问题可以通过重置 iOS 系统内的网络设置来解决，不过 Schou 发现了一个后续问题，在设备发现 SSID 为“%secretclub%power” 的热点之后，iOS 设备就会禁用 Wi-Fi 连接，而且即便重置可能也无法解决。</p><p style="text-align: left;">Schou 称，用于测试的 iPhone 在反复重置网络设置和强制重启 iPhone 后仍然没有 Wi-Fi。该研究人员还就此事联系了<a data-link="1" href="https://apple.pvxt.net/c/1251234/435400/7639?u=https%3A%2F%2Fwww.apple.com%2Fcn%2Fmusic%2F" target="_blank">苹果</a>的设备安全团队，但尚未收到任何回复。</p><p style="text-align: left;">最初的错误被认为是输入解析的问题，百分比符号可能被 iOS 误解为字符串格式的指定符，即符号后面的字符可能被认为是一个变量或命令，而不是纯文本。虽然新的SSID确实是在开玩笑地宣传 Schou 参与的一个技术探索小组 Secret Club，但使用百分比符号后的字符 S 和 P 很可能是热点名称错误的问题所在。对该问题的分析证实了其背后是一个格式化字符串的漏洞，尽管它对于一个坏的行为者来说似乎不是一个高度可利用的漏洞。</p>   
</div>
            