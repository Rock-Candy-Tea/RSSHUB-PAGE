
---
title: 'CISA发布AA22-103A新警报：警惕针对ICS_SCADA设备的APT网络攻击'
categories: 
 - 新媒体
 - cnBeta
 - 最新
headimg: 'https://static.cnbetacdn.com/article/2022/0414/eb4a52f27664126.png'
author: cnBeta
comments: false
date: Thu, 14 Apr 2022 03:45:42 GMT
thumbnail: 'https://static.cnbetacdn.com/article/2022/0414/eb4a52f27664126.png'
---

<div>   
<strong>本周三，包括美国能源部（DOE）、网络安全和基础设施安全局（CISA）和联邦调查局（FBI）在内的多个机构，向关键基础设施运营商发出了严重的潜在攻击警报。</strong>近年来，某些持续威胁（APT）参与者创建了许多定制工具，并在针对工业控制系统（ICS）、监控和数据采集设备（SCADA）等关键基础设施的攻击事件中发挥了相当大的威力。<br>
<p style="text-align: center;"><img src="https://static.cnbetacdn.com/article/2022/0414/eb4a52f27664126.png" alt="0.png" referrerpolicy="no-referrer"></p><p style="text-align: center;">（来自：<a href="https://www.cisa.gov/uscert/ncas/alerts/aa22-103a" target="_self">CISA</a>）</p><p>具体说来是，此类攻击多针对施耐德电气的 PLC（通用控制器）、欧姆龙 Sysmac N PLC 和开放平台统一通信架构（OPC UA）服务器而发起。</p><p>鉴于上述产品亦在美国诸多重要的工业设施中得到了广泛的使用，美国多个联邦部门在警报中发出了严厉的提醒：</p><blockquote><p>一旦被攻击者获得对相关运营技术（OT）的最终访问权限，特定工具将能够对内网进行扫描、破坏和建立远程控制能力。</p><p>此外针对工控主板驱动漏洞的利用，也潜在于基于 <a data-link="1" href="https://microsoft.pvxt.net/x9Vg1" target="_blank">Windows</a> 操作系统的工程信息技术（IT）或 OT 环境的工作站中。</p><p>通过制定和维护对 ICS / SCADA 设备的访问权限，APT 参与者可顺利提权、在 OT 环境中四处游荡，进而破坏关键设备或系统功能。</p></blockquote><p>正因如此，有关部门才不厌其烦地在每一份馆建设施实施警报中给出相关检测和缓解建议。</p><blockquote><p>本轮攻击波及施耐德电气的 MODICON 和 MODICON Nano PLC，影响 TM251、TM241、M258、M23、LMC058 和 LMC078 等型号。</p><p>欧姆龙 Sysmac NJ NX8 PLC 亦有在列，受影响的产品涵盖了 NEX NX1P2、NX-SL3300、NX-ECC203、NJ501- 1300、S8VK 和 R88D-1SN10F-ECT 等型号。</p></blockquote><p>ICS 网络安全软件公司 aDolus Technology 首席技术官 Eric Byres 在接受 <a href="https://therecord.media/us-agencies-warn-of-custom-made-hacking-tools-targeting-energy-sector-systems/" target="_self">The Record</a> 采访时指出：基于通用的“共同合作协议”，OPC UA 的大多数供应商系统都允许配合多方的产品使用。</p><p>安全公司 Dragos 首席执行官 Robert Lee 补充道，他们一直在追踪此类针对 ICS 的恶意软件。可知其最初以施耐德电气和欧姆龙等厂家的产品为目标，且会利用本机功能来逃避安全检测。</p><p>庆幸的是，大部分此类恶意软件尚未在目标网络中被激活，意味着广大基础设施运营商仍有机会在灾难发生前迅速落实防御措施。</p><p>据悉，此类恶意软件最初似乎特别针对液化天然气和电力等能源基础设施。但从本质上来剖析，可知其亦可在各种各样的工业控制器和系统上运行。</p><div class="article-relation"><p><strong>相关文章:</strong></p><p><a href="https://www.cnbeta.com/articles/tech/1257619.htm" target="_blank">乌克兰宣称挫败了Sandworm黑客组织想要攻击该国能源供应商的企图</a></p></div>   
</div>
            