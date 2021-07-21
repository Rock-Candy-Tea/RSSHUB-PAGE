
---
title: '黑客团伙利用SSH暴力破解器入侵远程设备 用于挖矿和DDoS攻击'
categories: 
 - 新媒体
 - cnBeta
 - 最新
headimg: 'https://static.cnbetacdn.com/thumb/article/2021/0721/3248bbf9b08aa9f.jpg'
author: cnBeta
comments: false
date: Wed, 21 Jul 2021 01:42:58 GMT
thumbnail: 'https://static.cnbetacdn.com/thumb/article/2021/0721/3248bbf9b08aa9f.jpg'
---

<div>   
疑似来自罗马尼亚、至少从 2020 年开始活跃的一个黑客团伙正使用此前从未被记录的 SSH 暴力破解器（使用 Golang 编写），对使用 Linux 的设备发起加密劫持活动。在成功入侵之后，<strong>就会部署门罗币（Monero）恶意挖矿软件。</strong><br>
 <p style="text-align:center"><a href="https://static.cnbetacdn.com/article/2021/0721/3248bbf9b08aa9f.jpg" target="_blank"><img src="https://static.cnbetacdn.com/thumb/article/2021/0721/3248bbf9b08aa9f.jpg" referrerpolicy="no-referrer"></a></p><p style="text-align: left;"><a href="https://www.bitdefender.com/blog/labs/how-we-tracked-a-threat-group-running-an-active-cryptojacking-campaign" target="_blank">来自 Bitdefender 的安全研究人员在上周发布的安全公告中表示</a>，这款称之为“Diicot brute”的密码破解工具通过软件即服务（software-as-a-service）模型进行分发，每个威胁行为者都提供自己独特的 API 密钥以促进入侵。</p><p style="text-align:center"><a href="https://static.cnbetacdn.com/article/2021/0721/3932700f9323fde.jpg" target="_blank"><img src="https://static.cnbetacdn.com/thumb/article/2021/0721/3932700f9323fde.jpg" referrerpolicy="no-referrer"></a></p><p style="text-align: left;">在远程攻击成功之后除了部署恶意程序用于挖矿之外，该团伙还连接了至少 2 个 DDoS 僵尸网络，包括一个名为 chernobyl 的 Demonbot 变体和一个 Perl IRC bot，以及 XMRig 自 2021 年 2 月起托管在名为 mexalz[.]us 的域上的挖矿负载。</p><p style="text-align:center"><a href="https://static.cnbetacdn.com/article/2021/0721/71b2334cb3dc9cc.jpg" target="_blank"><img src="https://static.cnbetacdn.com/thumb/article/2021/0721/71b2334cb3dc9cc.jpg" referrerpolicy="no-referrer"></a></p><p style="text-align: left;">Bitdefender 表示于 2021 年 5 月开始调查该组织的敌对在线活动，随后发现了对手的攻击基础设施和工具包。该组织还以依靠一袋混淆技巧而闻名，这些技巧使他们能够躲避安全软件的审查。为此，Bash 脚本使用 shell 脚本编译器 (shc) 进行编译，并且发现攻击链利用 Discord 将信息报告回其控制的渠道，这种技术在恶意行为者中变得越来越普遍用于指挥和控制通信并逃避安全。</p><p style="text-align:center"><a href="https://static.cnbetacdn.com/article/2021/0721/1e9df8d73999a94.jpg" target="_blank"><img src="https://static.cnbetacdn.com/thumb/article/2021/0721/1e9df8d73999a94.jpg" referrerpolicy="no-referrer"></a></p><p style="text-align: left;">研究人员说：“黑客窃取弱 SSH 凭据的情况并不少见。安全方面最大的问题之一是默认用户名和密码，或者弱凭据黑客可以通过蛮力轻松克服。棘手的部分不一定是蛮力强制这些凭据，而是以一种让攻击者未被发现的方式进行操作”。</p><p style="text-align: center;"><a href="https://static.cnbetacdn.com/article/2021/0721/e27527f4f23d484.jpg" target="_blank"><img src="https://static.cnbetacdn.com/thumb/article/2021/0721/e27527f4f23d484.jpg" referrerpolicy="no-referrer"></a></p>   
</div>
            