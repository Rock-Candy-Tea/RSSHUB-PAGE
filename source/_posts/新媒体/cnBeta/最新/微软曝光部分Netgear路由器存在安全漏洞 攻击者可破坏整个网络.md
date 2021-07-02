
---
title: '微软曝光部分Netgear路由器存在安全漏洞 攻击者可破坏整个网络'
categories: 
 - 新媒体
 - cnBeta
 - 最新
headimg: 'https://static.cnbetacdn.com/article/2021/0702/29829e3cb71c756.png'
author: cnBeta
comments: false
date: Fri, 02 Jul 2021 08:52:50 GMT
thumbnail: 'https://static.cnbetacdn.com/article/2021/0702/29829e3cb71c756.png'
---

<div>   
<strong>在调查 Microsoft Defender for Endpoint 中的设备指纹识别功能时，微软安全研究人员意外发现了 Netgear 路由器中存在的一个安全漏洞。</strong>为避免被攻击者利用来破坏整个网络，这家总部位于雷德蒙德的软件巨头选择了与 Netgear 团队密切合作，以尽可能快速有效地解决相关问题。<br>
<p><img src="https://static.cnbetacdn.com/article/2021/0702/29829e3cb71c756.png" referrerpolicy="no-referrer"></p><p style="text-align: center;">（来自：Microsoft <a href="https://www.microsoft.com/security/blog/2021/06/30/microsoft-finds-new-netgear-firmware-vulnerabilities-that-could-lead-to-identity-theft-and-full-system-compromise/" target="_self">Security Blog</a>）</p><p>据悉，该漏洞是在 DGN-2200v1 <a data-link="1" href="https://c.duomai.com/track.php?site_id=242986&euid=&t=https://list.jd.com/list.html?cat=670,699,700" target="_blank">路由器</a>的管理端口，试图被不属于 IT 员工的设备访问后被发现的。</p><p>在被机器学习算法标记为异常之后，研究人员调查了该连接是否存在任何可能被攻击者利用的潜在安全漏洞的可能。</p><p>结果发现，攻击者不仅无需身份验证即可访问路由器的管理界面，还能够获得对路由器的完整控制权。</p><p style="text-align: center;"><img src="https://static.cnbetacdn.com/article/2021/0702/e1fb539c7c5cb5e.jpg" referrerpolicy="no-referrer"></p><p style="text-align: center;"><a href="https://www.netgear.com/support/product/DGN2200v1.aspx" target="_self">DNG-2200v1</a> 资料图</p><p>此外侧信号攻击或泄露已保存的路由器的登录信息，而配置备份与恢复功能亦可用于获取保存在设备内存中的凭据。</p><p>通常情况下，数据会使用“NtgrBak”这个唯一的 DES 密钥加以保护。但对于有能力绕过 NVRAM 中的加密的攻击者来说，获取明文密码也并非难事。借助同样的手段，攻击者还可获得用户名。</p><p><a href="https://static.cnbetacdn.com/article/2021/0702/e251a1581c09e2d.png" target="_blank"><img src="https://static.cnbetacdn.com/thumb/article/2021/0702/e251a1581c09e2d.png" referrerpolicy="no-referrer"></a></p><p style="text-align: center;">Microsoft 365 Defender 中的设备列表</p><p>Microsoft 365 Defender 研究团队的 Jonathan Bar Or 指出：“安全解决方案的持续改进，迫使攻击者探索破坏系统的替代方法”。</p><blockquote><p>通过虚拟专用网设备和其它面向互联网的系统而开展的固件型与勒索软件攻击的数量不断增加，就是在操作系统层级内外发起攻击的一个典型例子。</p></blockquote><p>最后，我们强烈建议 Netgear DGN2200v1 路由器用户立即下载并安装最新版固件，以帮助设备和网络抵御任何潜在的攻击。</p>   
</div>
            