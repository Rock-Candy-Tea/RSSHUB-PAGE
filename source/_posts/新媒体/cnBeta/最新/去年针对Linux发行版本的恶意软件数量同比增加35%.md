
---
title: '去年针对Linux发行版本的恶意软件数量同比增加35%'
categories: 
 - 新媒体
 - cnBeta
 - 最新
headimg: 'https://static.cnbetacdn.com/article/2022/0117/9d69a44786e04ea.webp'
author: cnBeta
comments: false
date: Mon, 17 Jan 2022 04:36:25 GMT
thumbnail: 'https://static.cnbetacdn.com/article/2022/0117/9d69a44786e04ea.webp'
---

<div>   
<a href="https://www.crowdstrike.com/blog/linux-targeted-malware-increased-by-35-percent-in-2021/" target="_blank">根据 CrowdStrike 的威胁遥测数据</a>，在 2021 年针对 Linux 发行版本（被物联网设备广泛部署）的恶意软件数量比 2020 年增加了 35%。其中 XorDDoS、Mirai 和 Mozi 这前三个恶意软件家族在 2021 年占所有基于 Linux 的 IoT 恶意软件的 22%。<br>
 <p><img src="https://static.cnbetacdn.com/article/2022/0117/9d69a44786e04ea.webp" alt="v51dvxnl.webp" referrerpolicy="no-referrer"></p><p style="text-align: left;">与 2020 年相比，Mozi 在 2021 年的野外样本数量大幅增加了 10 倍。这些恶意软件家族的主要目的是破坏脆弱的互联网连接设备，将它们聚集成僵尸网络，并利用它们来进行分布式拒绝服务（DDoS）攻击。</p><p style="text-align: left;">当今大多数的云基础设施和网络服务器都运行 Linux，但它也为移动和物联网设备提供动力。它之所以受欢迎，是因为它提供了可扩展性、安全功能和广泛的发行版，以支持多种硬件设计和在任何硬件要求上的巨大性能。</p><p style="text-align: left;">随着各种 Linux 构建和分布在云基础设施、移动和物联网的核心，它为威胁者提供了一个巨大的机会。例如，无论是使用硬编码凭证、开放端口还是未修补的漏洞，运行Linux的物联网设备对威胁者来说都是一个低风险的果实--它们的大规模破坏会威胁到关键互联网服务的完整性。预计到2025年底，将有超过300亿台物联网设备连接到互联网，为威胁和网络犯罪分子创造一个潜在的巨大攻击面，以创建大规模的僵尸网络。</p><p style="text-align: left;">僵尸网络是一个连接到远程指挥和控制（C2）中心的受损设备网络。它在更大的网络中发挥着小齿轮的作用，并能感染其他设备。僵尸网络经常被用于DDoS攻击，向目标发送垃圾邮件，获得远程控制，并进行加密等CPU密集型活动。DDoS攻击使用多个连接互联网的设备来访问一个特定的服务或网关，通过消耗整个带宽来阻止合法流量的通过，导致其崩溃。</p><p style="text-align: left;"><strong>● XorDDoS</strong></p><p style="text-align: left;">XorDDoS是一个为多种Linux架构编译的Linux木马，范围从ARM到x86和x64。它的名字来自于在恶意软件和网络通信中使用XOR加密到C2基础设施。当针对物联网设备时，该木马已知会使用SSH暴力攻击来获得对脆弱设备的远程控制。</p><p style="text-align:center"><img src="https://static.cnbetacdn.com/article/2022/0117/138aebc08f361db.webp" referrerpolicy="no-referrer"></p><p style="text-align: left;">在 Linux 机器上，XorDDoS 的一些变种显示，其操作者扫描和搜索Docker服务器，并打开2375端口。这个端口提供了一个未加密的Docker套接字和对主机的远程root无密码访问，攻击者可以滥用它来获得对机器的root访问。</p><p style="text-align:center"><img src="https://static.cnbetacdn.com/article/2022/0117/ad3ec74f4aec850.webp" referrerpolicy="no-referrer"></p><p style="text-align: left;"><strong>● Mozi</strong></p><p style="text-align:center"><img src="https://static.cnbetacdn.com/article/2022/0117/c18a8d52ba4c94e.webp" referrerpolicy="no-referrer"></p><p style="text-align: left;">Mozi 是一个点对点（P2P）僵尸网络，利用分布式哈希表（DHT）系统，实施自己的扩展DHT。DHT提供的分布式和去中心化的查找机制使Mozi能够将C2通信隐藏在大量合法的DHT流量后面。Mozi通过强加SSH和Telnet端口来感染系统。然后它封锁这些端口，以便不被其他恶意行为者或恶意软件覆盖。</p><p style="text-align:center"><img src="https://static.cnbetacdn.com/article/2022/0117/928abde4af538ec.webp" referrerpolicy="no-referrer"></p><p style="text-align: left;"><strong>● Mirai</strong></p><p style="text-align: left;">Mirai 恶意软件在过去几年中声名鹊起，特别是在其开发者公布了 Mirai 的源代码之后。与Mozi类似，Mirai滥用弱协议和弱密码，如Telnet，利用暴力攻击入侵设备。</p><p style="text-align:center"><img src="https://static.cnbetacdn.com/article/2022/0117/5ac625fc63dad03.webp" referrerpolicy="no-referrer"></p><p style="text-align: left;">自从Mirai的源代码公开后，出现了多个Mirai变种，这个Linux木马可以被认为是当今许多Linux DDoS恶意软件的共同祖先。虽然大多数变种在现有的Mirai功能上进行了补充，或实现了不同的通信协议，但在其核心部分，它们共享相同的Mirai DNA。</p>   
</div>
            