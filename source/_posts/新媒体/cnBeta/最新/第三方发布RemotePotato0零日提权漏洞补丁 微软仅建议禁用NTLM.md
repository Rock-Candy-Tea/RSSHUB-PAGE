
---
title: '第三方发布RemotePotato0零日提权漏洞补丁 微软仅建议禁用NTLM'
categories: 
 - 新媒体
 - cnBeta
 - 最新
headimg: 'https://static.cnbetacdn.com/article/2022/0114/70508d401cfa2f9.jpg'
author: cnBeta
comments: false
date: Fri, 14 Jan 2022 05:22:35 GMT
thumbnail: 'https://static.cnbetacdn.com/article/2022/0114/70508d401cfa2f9.jpg'
---

<div>   
<strong>近日曝光的一个影响所有流行 Windows 操作系统版本的零日漏洞，已收到多个非官方补丁。</strong>SentinelOne 研究人员 Antonio Cocomazzi 和 Andrea Pierini 最早发现了这个名为“RemotePotato0”的提权漏洞，并于 2021 年 4 月就向微软进行了通报。<br>
 <p style="text-align: center;"><img src="https://static.cnbetacdn.com/article/2022/0114/70508d401cfa2f9.jpg" alt="1.jpg" referrerpolicy="no-referrer"></p><p style="text-align: center;">截图（via 0patch by ACROS Security）</p><p>然而让人不解的是，尽管<a data-link="1" href="https://c.duomai.com/track.php?site_id=242986&euid=&t=https://www.microsoftstore.com.cn/" target="_blank">微软</a>承认了这个零日漏洞的存在，却迟迟未给它分配一个通用漏洞披露（CVE ID）编号，据说是官方拒绝修复。</p><p>至于 RemotePotato0 的攻击原理，其实依赖于 NTLM 中继，以触发经过身份验证的 RPC / DCOM 调用。</p><p>通过成功地将 NTLM 身份验证中继到其它协议，攻击者便可在目标系统上为自己提升权限，从而获得域管理员的相应能力。</p><p style="text-align: center;"><iframe src="//tv.sohu.com/s/sohuplayer/iplay.html?bid=318406755&autoplay=false&disablePlaylist=true" width="640" height="480" frameborder="0"></iframe></p><p style="text-align: center;">0patching the Remote Potato0 Local Privilege Escalation（<a href="https://tv.sohu.com/v/dXMvODIyMjQwNTMvMzE4NDA2NzU1LnNodG1s.html" target="_self">via</a>）</p><p>0patch 联合创始人Mitja Kolsek 对这个漏洞给出了详细的解释，甚至分享了非官方补丁，以阻止在受影响的服务器上的利用。</p><blockquote><p>其允许以低权限登录的攻击者，利用同一台计算机上其他用户会话的 NTLM 哈希，发送 IP 攻击者指定的地址。</p><p>在从域管理员那里截获 NTLM 哈希后，攻击者可通过伪造请求，假装该管理员身份并执行某些管理操作 —— 比如特权提升。</p></blockquote><p><a href="https://static.cnbetacdn.com/article/2022/0114/4c2175cc9d4fabf.jpg" target="_blank"><img src="https://static.cnbetacdn.com/thumb/article/2022/0114/4c2175cc9d4fabf.jpg" alt="2.jpg" referrerpolicy="no-referrer"></a></p><p>NTLM 全称为 <a data-link="1" href="https://microsoft.pvxt.net/x9Vg1" target="_blank">Windows</a> NT LAN Manager，作为一个过时的身份验证协议，其仍被大量 Windows 服务器所采用。</p><p>或许正因如此，微软才懒得为其专门分配一个 CVE 漏洞编号和提供修复，而是建议直接禁用 NTLM、或重新配置 Windows 服务器以阻止此类中继攻击。</p><p>不过微软这项决定的风险依然很大，毕竟 RemotePotato0 可在无需与目标交互的情况下被利用。</p><p>有鉴于此，第三方强烈建议为从 Windows 7 ~ 10、以及 Server 2008 ~ 2019 的操作系统积极落实漏洞封堵措施。</p>   
</div>
            