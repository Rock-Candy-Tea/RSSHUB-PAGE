
---
title: '200家企业遭遇REvil勒索软件的MSP供应链攻击'
categories: 
 - 新媒体
 - cnBeta
 - 最新
headimg: 'https://static.cnbetacdn.com/thumb/article/2021/0703/09b1412ef5738ad.png'
author: cnBeta
comments: false
date: Sat, 03 Jul 2021 05:54:55 GMT
thumbnail: 'https://static.cnbetacdn.com/thumb/article/2021/0703/09b1412ef5738ad.png'
---

<div>   
<strong>周四下午开始，REvil 勒索软件团伙（又名 Sodinokibi）似乎又盯上了拥有数千名客户的托管服务提供商（MSPs）。</strong>作为 Kaseya VSA 供应链攻击的一部分，目前已知有 8 个大型的 MSP 遭到了攻击。据悉，Kaseya VSA 是一个基于云的 MSP 平台，允许提供商为客户执行补丁管理和客户端监控任务。<br>
<p><a href="https://static.cnbetacdn.com/article/2021/0703/09b1412ef5738ad.png" target="_blank"><img src="https://static.cnbetacdn.com/thumb/article/2021/0703/09b1412ef5738ad.png" alt="1.png" referrerpolicy="no-referrer"></a></p><p>Huntress Labs 的 John Hammond 向 <a href="https://www.bleepingcomputer.com/news/security/revil-ransomware-hits-200-companies-in-msp-supply-chain-attack/" target="_self">BleepingComputer</a> 透露，所有受影响的 MSP 都在使用 Kaseya VSA，且他们有证据表明他们的客户也受到了影响，包括 3 个 Huntress 合作伙伴 / 大约 200 家企业。</p><p>截止美东时间当天下午 2 点，此类潜在攻击似乎仅限于少数内部部署客户。但 Kaseya 还是在网站上发布了安全公告，警告所有 VSA 客户立即关闭他们的服务器，以防止事态的进一步蔓延。</p><blockquote><p>目前我们正在非常谨慎地调查时间的根本原因，但在收到进一步的通知之前，建议大家立即关闭自家的 VSA 服务器。</p><p>该操作至关重要，还请立即执行，因为攻击者做的第一件事，就是关上 VSA 管理访问的大门。</p></blockquote><p><a href="https://static.cnbetacdn.com/article/2021/0703/43991a74dc08d4b.png" target="_blank"><img src="https://static.cnbetacdn.com/thumb/article/2021/0703/43991a74dc08d4b.png" alt="2.png" referrerpolicy="no-referrer"></a></p><p style="text-align: center;">执行 REvil 勒索软件的 PowerShell 命令（图 via <a href="https://www.reddit.com/r/kaseya/comments/ocf0x1/kaseya_has_been_hacked_with_randomware_that/" target="_self">Reddit</a>）</p><p>在致 BleepingComputer 的一份声明中，Kaseya 表示他们已经关闭了自家的 SaaS 服务器，并且正在与其它安全公司合作调查这一事件。</p><p>此外大多数勒索软件加密攻击都选在了周末的深夜进行，因为那时负责网络监控的人手最少。鉴于本次攻击发生在周五中午，攻击者很可能瞄准这周末发起更大范围的行动。</p><p><img src="https://static.cnbetacdn.com/article/2021/0703/1a6a32c1a769634.png" alt="3.png" referrerpolicy="no-referrer"></p><p style="text-align: center;">agent.exe 可执行文件的签名</p><p>John Hammond 与 Sophos 的 Mark Loman 都向 BleepingComputer 透露，针对 MSP 的攻击，似乎是通过 Kaseya VSA 发起的供应链攻击。</p><p>前者称，Kaseya VSA 会将 agent.crt 文件放到 c:\kworking 文件夹中，并作为“Kaseya VSA Agent Hot-fix”更新来分发。</p><p>然后借助合法的 <a data-link="1" href="https://microsoft.pvxt.net/x9Vg1" target="_blank">Windows</a> certutil.exe 这个 PowerShell 命令对 agent.crt 文件进行解码，并将 agent.exe 文件提取到同一文件夹中。</p><p>agent.exe 使用了来自“PB03 TRANSPORT LTD”的签名证书，辅以嵌入的“MsMpEng.exe”和“mpsvc.dll”（后面这个动态链接库文件又被 REvil 勒索软件的加密器所使用）。</p><p><img src="https://static.cnbetacdn.com/article/2021/0703/dddeb0f8b45bddf.png" alt="4.png" referrerpolicy="no-referrer"></p><p style="text-align: center;">agent.exe 提取并启动的嵌入式资源代码</p><p>MsMPEng.exe 是合法的 Microsoft Defender 可执行文件的旧版本，它被当做 LOLBin 以调用动态链接库（DLL）文件，并通过受信任的可执行文件进行加密。</p><p>此外一些样本还向受感染的计算机注入了带有政治色彩的 Windows 注册表项及配置更改，比如 BleepingComputer 就在 [VirusTotal] 样本中看到了 BlackLivesMatter 密钥被用于存储来自攻击者的配置信息。</p><p><img src="https://static.cnbetacdn.com/article/2021/0703/f16ea3e699d5663.png" alt="5.png" referrerpolicy="no-referrer"></p><p>若不幸中招，勒索软件团伙会向受害者索取 500 万美元的赎金，以获得针对其中一个样本的解密器。</p><p>而且通常 REvil 会在部署文件加密型勒索软件前窃取受害者的数据，但目前尚不清楚本次攻击有泄露哪些文件。</p>   
</div>
            