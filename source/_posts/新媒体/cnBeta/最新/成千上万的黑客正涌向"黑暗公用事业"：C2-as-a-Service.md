
---
title: '成千上万的黑客正涌向"黑暗公用事业"：C2-as-a-Service'
categories: 
 - 新媒体
 - cnBeta
 - 最新
headimg: 'https://static.cnbetacdn.com/article/2022/0807/d1c4f592046ca88.webp'
author: cnBeta
comments: false
date: Sat, 06 Aug 2022 18:58:23 GMT
thumbnail: 'https://static.cnbetacdn.com/article/2022/0807/d1c4f592046ca88.webp'
---

<div>   
安全研究人员发现了一种名为"黑暗公用事业"的新服务，它为网络犯罪分子提供了一种简单而廉价的方式，为其恶意行动建立一个指挥和控制（C2）中心。Dark
Utilities服务为威胁者提供了一个支持Windows、Linux和基于Python的恶意程序载荷的平台。<br>
 <p><img src="https://static.cnbetacdn.com/article/2022/0807/d1c4f592046ca88.webp" title alt="dark-utilities-site.webp" referrerpolicy="no-referrer"></p><p>C2服务器指的是攻击者在外部控制其恶意软件的方式，发送命令、配置和新的有效载荷，并接收从被攻击系统收集的数据。</p><p>"黑暗公用事业"的运作是一种"C2即服务"（C2-as-a-Service），它对外宣称可以提供可靠、匿名的C2基础设施和所有必要的附加功能，起价仅为9.99欧元。</p><p>思科Talos的一份报告称，该服务有大约3000名活跃用户，这将为运营商带来大约3万欧元的收入。</p><p><img src="https://static.cnbetacdn.com/article/2022/0807/1b77da91e6fb6a0.webp" title alt="selecting-os.webp" referrerpolicy="no-referrer"></p><p>Dark Utilities在2022年初出现，在Tor网络和透明网络上提供全面的C2能力，并在IPFS - 一个用于存储和共享数据的分散的网络系统中托管恶意软件载荷。</p><p>所提供的恶意软件一条龙服务还支持多种架构，而且这一运营商似乎正计划扩大该列表，以提供一套更大的可能成为目标的设备选项。</p><p>思科Talos研究人员说，选择操作系统会产生一个命令字符串，"威胁者通常会将其嵌入PowerShell或Bash脚本中，以方便在受害者机器上检索和执行恶意载荷"。</p><p>所选的载荷还通过在<a data-link="1" href="https://microsoft.pvxt.net/x9Vg1" target="_blank">Windows</a>上创建一个注册表键，或在Linux上创建一个Crontab条目或一个Systemd服务，在目标系统上建立了持久存在。</p><p><img src="https://static.cnbetacdn.com/article/2022/0807/44575b33c8b97bc.webp" title alt="dashboard.webp" referrerpolicy="no-referrer"></p><p>根据研究人员的说法，客户的管理面板带有多种模块，用于各种类型的攻击，包括分布式拒绝服务（DDoS）和加密劫持。</p><p>由于数以万计的威胁者已经订阅，而且价格低廉，Dark Utilities可能会吸引更多不太熟练的对手。</p>   
</div>
            