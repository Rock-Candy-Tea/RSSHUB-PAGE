
---
title: '微软分享缓解PetitPotam NTML中继攻击的方法'
categories: 
 - 新媒体
 - cnBeta
 - 最新
headimg: 'https://static.cnbetacdn.com/article/2021/0726/b423d8873dcd84f.png'
author: cnBeta
comments: false
date: Mon, 26 Jul 2021 04:18:18 GMT
thumbnail: 'https://static.cnbetacdn.com/article/2021/0726/b423d8873dcd84f.png'
---

<div>   
<strong>几天前，法国安全研究人员 Gilles Lionel 披露了一种新式 NTLM 中继攻击。若得逞，黑客将接管域控制器或其它 Windows 服务器。</strong>随着 PetitPotam 概念验证代码的披露，这也成为了困扰企业网络管理员的一个新安全问题。<br>
<p><img src="https://static.cnbetacdn.com/article/2021/0726/b423d8873dcd84f.png" alt="1.png" referrerpolicy="no-referrer"></p><p>具体说来是，该漏洞利用了微软加密文件系统远程协议（简称 EFSRPC），以强制设备（包括域控制器）向恶意的远程 NTLM 中继进行身份验证。</p><p>基于此，攻击者便可窃取哈希证书，并获得假定设备的实际身份与特权。</p><p>庆幸的是，微软已经知晓了 PetitPotam 攻击可被用于攻击 <a data-link="1" href="https://microsoft.pvxt.net/x9Vg1" target="_blank">Windows</a> 域控制器或其它 Windows 服务。</p><p><img src="https://static.cnbetacdn.com/article/2021/0726/d9f5deb6d2b92df.png" alt="2.png" referrerpolicy="no-referrer"></p><p>作为一种经典的 NTLM 中继攻击，微软此前已记录过类似的事件，并且提供了一些用户保护客户免受威胁的缓解选项（参考 <a href="https://docs.microsoft.com/en-us/security-updates/SecurityAdvisories/2009/974926" target="_self">974926</a> 安全通报）。</p><p>为防止在启用了 NTLM 的网络上发生中继攻击，域管理员必须确保其身份验证服务已启用相应的保护措施，比如 EPA 身份验证扩展保护、或 SMB 签名功能。</p><p>据悉，PetitPotam 会利用未妥善配置 Active Directory 证书保护服务（AD CS）的服务器。有需要的客户，可参考 KB5005413 中概述的缓解措施。</p><p><img src="https://static.cnbetacdn.com/article/2021/0726/731bbbbb79beac3.png" alt="3.png" referrerpolicy="no-referrer"></p><p><a href="https://msrc.microsoft.com/update-guide/vulnerability/ADV210003" target="_self">微软</a>指出，如果企业已在域中启用了 NTLM 身份验证，并将 Active Directory 证书服务与以下任何服务一起使用，就极易受到 PetiPotam 攻击的影响：</p><blockquote><p>● Certificate Authority Web Enrollment</p><p>● Certificate Enrollment Web Service</p></blockquote><p>基于此，最简单的解决方案，就是在不需要的情况下禁用 NTLM，例如域控制器、启用身份验证机制的扩展保护、或启用 NTLM 身份验证以使用签名功能。</p><p style="text-align:center"><a href="https://static.cnbetacdn.com/article/2021/0709/3e9423ce5678d8a.gif" target="_blank"><img src="https://static.cnbetacdn.com/article/2021/0709/3e9423ce5678d8a.gif" referrerpolicy="no-referrer"></a></p><p>最后，与 PrintNightmare 一样，这很可能是 PetitPotam 系列攻击的第一章。</p><p>Gilles Lionel 在接受 BleepingComputer 采访时称，PetitPotam 还允许其它形式的攻击，例如对使用 DES 数据加密标准的 NTLMv1 进行降级攻击。</p><p>作为一种不安全的算法，其仅使用了 56 位密钥生成，因而很容易被攻击者恢复哈希后的密码，并导致本地特权提升攻击。</p>   
</div>
            