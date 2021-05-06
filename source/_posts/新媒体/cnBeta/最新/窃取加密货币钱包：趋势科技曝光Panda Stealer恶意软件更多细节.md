
---
title: '窃取加密货币钱包：趋势科技曝光Panda Stealer恶意软件更多细节'
categories: 
 - 新媒体
 - cnBeta
 - 最新
headimg: 'https://static.cnbetacdn.com/article/2021/0506/d805b7552fb45a8.png'
author: cnBeta
comments: false
date: Thu, 06 May 2021 08:01:32 GMT
thumbnail: 'https://static.cnbetacdn.com/article/2021/0506/d805b7552fb45a8.png'
---

<div>   
本周，趋势科技（Trend Micro）安全研究人员分享了有关“Panda Stealer”恶意软件的详情。<strong>可知除了垃圾邮件、攻击者还选择了将它放入 Excel 文档并通过 Discord 渠道进行传播，以窃取用户的加密货币。</strong>由目前上传至 VirusTotal 的样本和调查分析可知，该恶意软件以波及美国、澳大利亚、日本和德国等地，且感染链条通常可追溯到一封网络钓鱼邮件。<br>
<p><img src="https://static.cnbetacdn.com/article/2021/0506/d805b7552fb45a8.png" referrerpolicy="no-referrer"></p><p style="text-align: center;">已有受害者通过 Discord 链接，从恶意网站下载了可执行文件。</p><p>安全研究人员指出，Panda Stealer 会在钓鱼邮件中将自身伪装成企业询价。在欺骗受害者打开了 .XLSM 后缀的文件并启用宏操作后，恶意软件就会尝试下载并执行主窃取程序。</p><p>此外 Panda Stealer 还有另一种感染途径，通过在 .XLS 格式的附件中插入一个隐藏了 PowerShell 命令 Excel 公式，恶意软件会在触发后尝试访问 paste.ee 这个网址，以将 PowerShell 脚本引入受害者的系统。</p><p><img src="https://static.cnbetacdn.com/article/2021/0506/026edbd8f8bb552.png" referrerpolicy="no-referrer"></p><p style="text-align: center;">恶意网址与文件（来自：<a href="https://www.trendmicro.com/en_us/research/21/e/new-panda-stealer-targets-cryptocurrency-wallets-.html" target="_self">Trend Micro</a>）</p><p>Trend Micro 表示，Visual Basic 中的 CallByName 导出功能，被攻击者用于从 paste.ee 网址调用内存中的 .NET 程序集。</p><p>通过 Agile.NET 混淆器加载的程序集，将把合法的 MSBuild.exe 进程掏空，然后用攻击者的有效负载替换（来自另一个 paste.ee 网址的十六进制编码的 Panda Stealer 二进制文件）。</p><p><a href="https://static.cnbetacdn.com/article/2021/0506/66a93c2cdd611a1.png" target="_blank"><img src="https://static.cnbetacdn.com/thumb/article/2021/0506/66a93c2cdd611a1.png" referrerpolicy="no-referrer"></a></p><p style="text-align: center;">Panda Stealer 的屏幕截图</p><p>下载完成后，Panda Stealer 将检测与以太坊（ETH）、莱特币（LTC）、字节币（BCN）、达世币（DASH）等加密货币有关的钱包密钥和地址。</p><p>此外该恶意软件能够屏幕截图、泄露系统数据、以及窃取信息，包括浏览器 Cookie、NordVPN、Telegram、Discord、以及 Steam 账户的凭据。</p><p><img src="https://static.cnbetacdn.com/article/2021/0506/9e1f3b25148454e.png" referrerpolicy="no-referrer"></p><p style="text-align: center;">叫卖收集来的数据的 Telegram 频道</p><p>通过对攻击链条和恶意软件分发方式的分析，Trend Micro 认为 Panda Stealer 与 Phobos 勒索软件（以及 4 月份报告中提到的 LockBit）存在许多相似之处。</p><p>尽管未将该活动归因于特定的网络攻击者，但 Trend Micro 还是顺着命令与控制服务器，反向找到了幕后黑手的 IP 地址、以及从 Shock Hosting 租用的 VPS 服务器（后者已处于被挂起的状态）。</p>   
</div>
            