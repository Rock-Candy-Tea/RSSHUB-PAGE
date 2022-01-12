
---
title: '黑客组织Patchwork感染自己开发的恶意程序 导致内部系统被曝光'
categories: 
 - 新媒体
 - cnBeta
 - 最新
headimg: 'https://static.cnbetacdn.com/article/2022/0112/6b12d3f85a1ff2b.webp'
author: cnBeta
comments: false
date: Wed, 12 Jan 2022 03:01:25 GMT
thumbnail: 'https://static.cnbetacdn.com/article/2022/0112/6b12d3f85a1ff2b.webp'
---

<div>   
印度相关的黑客组织 Patchwork 自 2015 年 12 月以来一直很活跃，主要通过鱼叉式网络钓鱼攻击针对巴基斯坦。在 2021 年 11 月底至 12 月初的最新活动中，Patchwork 利用恶意 RTF 文件投放了 BADNEWS（Ragnatela）远程管理木马（RAT）的一个变种。<a href="https://blog.malwarebytes.com/threat-intelligence/2022/01/patchwork-apt-caught-in-its-own-web/" target="_blank">但有趣的是这次活动却误伤了他们自己，使得安全研究人员得以一窥它的基础架构。</a><br>
  <p style="text-align:center"><img src="https://static.cnbetacdn.com/article/2022/0112/6b12d3f85a1ff2b.webp" referrerpolicy="no-referrer"></p><p style="text-align: left;">本次活动首次将目标锁定在研究重点为分子医学和生物科学的几位教员身上。令人讽刺的是，攻击者利用自己的 RAT 感染了自己的电脑，从而让安全公司 Malwarebytes 收集到了他们电脑和虚拟机的按键和屏幕截图。</p><p style="text-align: left;">通过分析，Malwarebytes 认为本次活动是 BADNEWS RAT 的一个新的变种，叫做 Ragnatela，通过鱼叉式网络钓鱼邮件传播给巴基斯坦的相关目标。Ragnatela 在意大利语中意为蜘蛛网，也是 Patchwork APT 使用的项目名称和面板。</p><p style="text-align:center"><img src="https://static.cnbetacdn.com/article/2022/0112/7c698c52b60799d.webp" referrerpolicy="no-referrer"></p><p style="text-align: left;">在本次活动，当用户点击这些恶意 RTF 文档之后，就可以利用 Microsoft Equation Editor 中的漏洞植入 RAT 程序，它会以 OLE 对象存储在 RTF 文件中。在设备感染之后，它会和外部的 C&C 服务器建立连接，具备执行远程命令、截取屏幕、记录按键、收集设备上所有档案清单、在特定时间里执行指定程序、上传或者下载恶意程序等等。</p><p style="text-align: left;">Ragnatela RAT 是在 11 月下旬开发的，如其程序数据库 (PDB) 路径 “E:\new_ops\jlitest __change_ops -29no – Copy\Release\jlitest.pdb” 所示，并被用于网络间谍活动。</p><p style="text-align: left;">Ragnatela RAT 允许威胁参与者执行恶意操作，例如：</p><blockquote style="text-align: left;"><p style="text-align: left;">● 通过 cmd 执行命令</p><p style="text-align: left;">● 屏幕截图</p><p style="text-align: left;">● 记录键盘按键</p><p style="text-align: left;">● 收集受害者机器中所有文件的列表</p><p style="text-align: left;">● 在特定时间段收集受害者机器中正在运行的应用程序列表</p><p style="text-align: left;">● 下载附加有效载荷</p><p style="text-align: left;">● 上传文件</p></blockquote><p style="text-align: left;">为了向受害者分发RAT，Patchwork用冒充巴基斯坦当局的文件引诱他们。例如，一个名为 EOIForm.rtf 的文件被威胁者上传到他们自己的服务器 karachidha[.]org/docs/。该文件包含一个漏洞（Microsoft Equation Editor），其目的是破坏受害者的计算机并执行最终的有效载荷（RAT）。</p><p style="text-align:center"><img src="https://static.cnbetacdn.com/article/2022/0112/03e7a4e44ef02a2.webp" referrerpolicy="no-referrer"></p><p style="text-align:center"><img src="https://static.cnbetacdn.com/article/2022/0112/0c6e174ae4235c0.webp" referrerpolicy="no-referrer"></p><p style="text-align:center"><img src="https://static.cnbetacdn.com/article/2022/0112/0b5ac00c27d717a.webp" referrerpolicy="no-referrer"></p><p style="text-align: left;">不过，Malwarebytes 发现 Patchwork 自己也感染了 Ragnatela。通过 RAT，研究人员发现了该组织开发的基础框架，包括跑Virtual Box、VMware作为Web开发及测试环境，其主机有英文及印度文双键盘配置、以及尚未更新Java程式等。此外他们使用VPN Secure及CyberGhost来隐藏其IP位址，并透过VPN登入以RAT窃得的受害者电子邮件及其他帐号。</p>   
</div>
            