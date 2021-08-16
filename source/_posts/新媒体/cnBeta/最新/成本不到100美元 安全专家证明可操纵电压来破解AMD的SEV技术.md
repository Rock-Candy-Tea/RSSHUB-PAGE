
---
title: '成本不到100美元 安全专家证明可操纵电压来破解AMD的SEV技术'
categories: 
 - 新媒体
 - cnBeta
 - 最新
headimg: 'https://static.cnbetacdn.com/thumb/article/2021/0816/00d1015d0ee2525.jpg'
author: cnBeta
comments: false
date: Mon, 16 Aug 2021 01:36:32 GMT
thumbnail: 'https://static.cnbetacdn.com/thumb/article/2021/0816/00d1015d0ee2525.jpg'
---

<div>   
<a href="https://arxiv.org/abs/2108.04575" target="_blank"><strong>来自柏林理工大学的研究团队已经证明</strong></a><strong>，可以通过操纵输入电压来破解 AMD 的安全加密虚拟化 (SEV) 技术。</strong>此前也有一些安全团队利用类似的方法攻破英特尔处理器安全技术。
AMD 的 SEV 技术主要依靠安全处理器 (SP)， 一种不起眼的 ARM Cortex-A5， 为 AMD EPYC CPU（Naples, Rome 和 Milan——Zen 1 到 3） 提供信任根。<br>
 <p style="text-align:center"><a href="https://static.cnbetacdn.com/article/2021/0816/00d1015d0ee2525.jpg" target="_blank"><img src="https://static.cnbetacdn.com/thumb/article/2021/0816/00d1015d0ee2525.jpg" referrerpolicy="no-referrer"></a></p><p style="text-align:center"><a href="https://static.cnbetacdn.com/article/2021/0816/3fb715d7393f88f.jpg" target="_blank"><img src="https://static.cnbetacdn.com/thumb/article/2021/0816/3fb715d7393f88f.jpg" referrerpolicy="no-referrer"></a></p><p style="text-align:center"><a href="https://static.cnbetacdn.com/article/2021/0816/b7cc7ba9e345d50.jpg" target="_blank"><img src="https://static.cnbetacdn.com/thumb/article/2021/0816/b7cc7ba9e345d50.jpg" referrerpolicy="no-referrer"></a></p><p style="text-align:center"><a href="https://static.cnbetacdn.com/article/2021/0816/5d682d34c236ad2.jpg" target="_blank"><img src="https://static.cnbetacdn.com/thumb/article/2021/0816/5d682d34c236ad2.jpg" referrerpolicy="no-referrer"></a></p><p style="text-align: left;">这份研究报告虽然非常冗长，但是标题非常有趣：“One Glitch to Rule Them All: Fault Injection Attacks Against <a data-link="1" href="https://c.duomai.com/track.php?site_id=242986&euid=&t=https://amd-cpu.jd.com/" target="_blank">AMD</a>’s Secure Encrypted Virtualization”（一个小故障引发的血案：针对 AMD 安全加密虚拟化的故障注入攻击”）。该报告描述了攻击者如何破坏 SP 以检索加密密钥或执行任意代码。</p><p style="text-align: left;">在报告中写道：“通过操纵芯片上 AMD 系统 (SoC) 的输入电压，我们在 AMD-SP 的只读存储器 (ROM) 引导加载程序中引入了错误，使我们能够完全控制这种信任根”。</p><p style="text-align: left;">执行这种攻击所需的位置相当严格；以允许在硬件级别访问服务器的角色访问云计算公司，并聪明地将其完成而不引起怀疑。然而，所需的设备并不那么雄心勃勃，只需要一个微控制器和一个闪存编程器，两者的价格都低于 50 美元。</p>   
</div>
            