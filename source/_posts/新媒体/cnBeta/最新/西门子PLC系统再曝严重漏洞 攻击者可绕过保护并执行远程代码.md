
---
title: '西门子PLC系统再曝严重漏洞 攻击者可绕过保护并执行远程代码'
categories: 
 - 新媒体
 - cnBeta
 - 最新
headimg: 'https://static.cnbetacdn.com/article/2021/0601/dfcdf4152380dd1.png'
author: cnBeta
comments: false
date: Tue, 01 Jun 2021 05:18:28 GMT
thumbnail: 'https://static.cnbetacdn.com/article/2021/0601/dfcdf4152380dd1.png'
---

<div>   
<strong>上周五，西门子发布了一个更新，以修复近日曝出的又一个可编程逻辑控制器（PLC）的严重漏洞。</strong>受影响的 PLC 型号包括了 SIMATIC S7-1200 和 S7-1500，两者都可能被恶意行为者用来远程访问受保护的内存区域，以实现不受限制和难以被发现的代码执行。<br>
 <p><img src="https://static.cnbetacdn.com/article/2021/0601/dfcdf4152380dd1.png" alt="1.png" referrerpolicy="no-referrer"></p><p style="text-align: center;">（来自：<a href="https://claroty.com/2021/05/28/blog-research-race-to-native-code-execution-in-plcs/" target="_self">Claroty</a>）</p><p>通过对用于在微处理器中执行 PLC 指令的 MC7 / MC7+ 字节码语言进行逆向工程，Claroty 证实了西门子 PLC 中存在的这个内存保护绕过漏洞（CVE-2020-15782）。</p><p>该漏洞的 CVSS 严重性评分为 8.1，庆幸的是目前尚无证据表明其已在野外被利用。西门子在警报（<a href="https://cert-portal.siemens.com/productcert/pdf/ssa-434534.pdf" target="_self">PDF</a>）中提到，未经身份验证的远程攻击者可通过网络访问 102 号 TCP 端口。</p><p>在将任意数据或代码写入受保护的内存区域、或读取敏感区域的数据之后，黑客就能够对设备发起进一步的攻击。</p><p><img src="https://static.cnbetacdn.com/article/2021/0601/8c37ad380a45b9d.png" alt="2.png" referrerpolicy="no-referrer"></p><p>Claroty 研究员 Tal Keren 补充道：想要在可编程逻辑控制器等工业控制系统上实现本机代码执行，显然不是普通攻击者能够轻易达成的目标。</p><p>在具有诸多复杂的内存保护机制的系统中，攻击者不仅达成了运行其选择的代码的目的，还必须确保自己不会被发现，意味着只有资深经验的少数高级黑客能够做到这一点。</p><p>具体说来是，新漏洞不仅允许攻击者在西门子 S7 控制器上执行本机代码，还可绕过底层操作系统或任何诊断软件的监测，从而让用户沙箱将任意数据和代码直接注入受保护的内存区域。</p><p><img src="https://static.cnbetacdn.com/article/2021/0601/5519e770ac5e0e2.png" alt="3.png" referrerpolicy="no-referrer"></p><p>另一方面，Claroty 指出攻击需要获取 PLC 的网络访问和下载权限。通过对 PLC 的原生沙箱进行越狱，攻击者将能够把内核级的恶意软件植入操作系统，从而实现远程代码执行。</p><p>当然，这并不是西门子首次遭遇针对 PLC 的未经授权代码执行漏洞。早在 2010 年，臭名昭著的震网（Stuxnet）蠕虫就曾利用各种 <a data-link="1" href="https://microsoft.pvxt.net/x9Vg1" target="_blank">Windows</a> 漏洞，通过修改西门子 PLC 上的代码来对工控系统进行重编程，从而实施了秘密破坏和网络间谍活动。</p><p>为降低风险，西门子强烈建议客户将软件更新到最新版本。同时该公司正在酝酿额外的更新，并让用户在等待更新到来的空窗期内采取相应的对策和落实缓解措施。</p>   
</div>
            