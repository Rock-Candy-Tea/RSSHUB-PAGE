
---
title: '安全人员发现新型恶意软件，文件伪装成 Windows 激活工具并可绕过系统保护'
categories: 
 - 新媒体
 - IT 之家
 - 热榜
headimg: 'https://img.ithome.com/newsuploadfiles/2022/3/84558142-4d89-4853-a9e3-1c0e5094ad56.jpg'
author: IT 之家
comments: false
date: Tue, 22 Mar 2022 03:54:31 GMT
thumbnail: 'https://img.ithome.com/newsuploadfiles/2022/3/84558142-4d89-4853-a9e3-1c0e5094ad56.jpg'
---

<div>   
<p data-vmark="a491"><a class="s_tag" href="https://www.ithome.com/" target="_blank">IT之家</a> 3 月 22 日消息，安全研究公司 ASEC 发现网络上近期出现了一种新的恶意软件大肆传播，它会伪装成以 Windows 激活工具的形式，但实际上是 BitRAT 远程访问木马。</p><p data-vmark="e2a8">IT之家了解到，ASEC 发现这种木马主要是通过 Webhards 分发（Webhards 是韩国的在线文件共享服务），但也会有通过其他渠道传播的风险。</p><p data-vmark="7293">值得一提的是，虽然破解和盗版软件通常被报毒，但许多人往往不会认真对待此类警告，而且部分用户需要 Windows 激活工具，可能在某些情况下就导致了这一问题。</p><p data-vmark="bced">ASEC 解释说，下载的 zip 文件“W10DigitalActivation.exe”虽然带有正版 Windows 激活文件，但也确实包含恶意文件。“W10DigitalActivation”msi 文件显然是真实的，而另一个“W10DigitalActivation_Temp”文件却是恶意软件（见下图）。</p><p data-vmark="af8b">当毫无戒心的用户运行压缩包中的文件时，真正的激活工具和恶意软件会同时执行，从而让用户误以为 Windows 激活工具是真的，所以这个文件没有威胁。</p><p data-vmark="fd4a" style="text-align: center;"><img src="https://img.ithome.com/newsuploadfiles/2022/3/84558142-4d89-4853-a9e3-1c0e5094ad56.jpg" w="760" h="350" alt="BitRAT伪装成Windows密钥验证工具" title="安全人员发现新型恶意软件，文件伪装成 Windows 激活工具并可绕过系统保护" width="760" height="350" referrerpolicy="no-referrer"></p><p data-vmark="0a10">当你运行木马后，W10DigitalActivation_Temp.exe 会通过命令和控制 (C&C) 服务器下载其他恶意文件，并通过 PowerShell 将它们传递到 Windows 启动程序文件夹中。</p><p data-vmark="4ed4">最后，BitRAT 会为你在 % temp% 文件夹内安装“Software_Reporter_Tool.exe”文件，从而实现在 Windows Defender 中添加了 Startup 文件夹的排除路径和 BitRAT 的排除过程。</p>
          
</div>
            