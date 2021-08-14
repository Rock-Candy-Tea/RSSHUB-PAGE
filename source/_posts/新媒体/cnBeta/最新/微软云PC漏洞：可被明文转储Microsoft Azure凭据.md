
---
title: '微软云PC漏洞：可被明文转储Microsoft Azure凭据'
categories: 
 - 新媒体
 - cnBeta
 - 最新
headimg: 'https://static.cnbetacdn.com/article/2021/0814/0077d609992b0e8.png'
author: cnBeta
comments: false
date: Sat, 14 Aug 2021 06:39:03 GMT
thumbnail: 'https://static.cnbetacdn.com/article/2021/0814/0077d609992b0e8.png'
---

<div>   
一位安全研究人员，<strong>刚刚找到了一种利用 Mimikatz，从微软 Windows 365 Cloud PC 服务中转储用户未加密的明文 Microsoft Azure 凭据的方法。</strong>据悉，Mimikatz 是由 Benjamin Delpy 创建的开源网络安全项目，允许研究人员测试各种凭证窃取和模拟漏洞。<br>
 <p><img src="https://static.cnbetacdn.com/article/2021/0814/0077d609992b0e8.png" alt="1.png" referrerpolicy="no-referrer"></p><p>mimikatz 的 <a href="https://github.com/gentilkiwi/mimikatz/wiki" target="_self">GitHub</a> 项目主页写道，其具有从内存中提取明文密码、哈希、PIN 码和 kerberos 凭证等功能。</p><p>尴尬的是，尽管 mimikatz 是专为安全研究人员而创建的，但由于各种模块的功能相当强大，威胁行为者也能够利用这把双刃剑，从 LSASS 进程的内存中转储纯文本密码、或执行 NTLM 哈希传递攻击。</p><p>此外攻击者可在整个网络中横向传播，直到他们夺取并接管 <a data-link="1" href="https://microsoft.pvxt.net/x9Vg1" target="_blank">Windows</a> 域控制器的控制权。</p><p style="text-align: center;"><iframe src="//tv.sohu.com/s/sohuplayer/iplay.html?bid=280049517&autoplay=false&disablePlaylist=true" width="640" height="480" frameborder="0"></iframe></p><p style="text-align: center;">dump Windows365 Azure passwords in the Web Interface（<a href="https://tv.sohu.com/v/dXMvODIyMjQwNTMvMjgwMDQ5NTE3LnNodG1s.html" target="_self">via</a>）</p><p>8 月 2 日，<a data-link="1" href="https://c.duomai.com/track.php?site_id=242986&euid=&t=https://www.microsoftstore.com.cn/" target="_blank">微软</a>推出了基于 Windows 365 的云桌面服务，允许用户租用云 PC、并通过远程桌面客户端或浏览器进行访问。</p><p>虽然微软提供了虚拟 PC 的免费试用版，但名额很快被抢购一空。Benjamin Delpy 在接受 BleepingComputer 采访时称，自己有幸获得了一个能够测试这项新服务安全性的机会。</p><p>结果发现，Windows 365 云 PC 竟然允许恶意程序转储 Microsoft Azure 登录用户的明文邮件地址和密码。</p><p><a href="https://static.cnbetacdn.com/article/2021/0814/0d4877712106261.jpg" target="_blank"><img src="https://static.cnbetacdn.com/thumb/article/2021/0814/0d4877712106261.jpg" alt="2.jpg" referrerpolicy="no-referrer"></a></p><p>按照既有的技术设定，终端服务器进程将要求内核为其进行解密。</p><p>然而通过 2021 年 5 月发现的一个漏洞，他还是顺利完成了转储登录终端服务器用户的明文凭据的相关操作。</p><p>尽管用户的终端服务器凭据在存储于内存中时会被加密，但 Delpy 声称可以通过欺骗终端服务进程的方式来解密。</p><p><a href="https://static.cnbetacdn.com/article/2021/0814/f5d672b24ebbb04.jpg" target="_blank"><img src="https://static.cnbetacdn.com/thumb/article/2021/0814/f5d672b24ebbb04.jpg" alt="3.jpg" referrerpolicy="no-referrer"></a></p><p>此外由于使用了 RDP 远程桌面协议，这套攻击方案也适用于 Web 浏览器。</p><p>尽管需要具有管理员权限才能运行 mimikatz，普通账户的用户无需太过担心。</p><p>但若攻击者获得了 Windows PC 设备的访问权限以运行相关命令，后果就难以想象了。</p><p><img src="https://static.cnbetacdn.com/article/2021/0814/71428739ccf29b4.png" alt="4.png" referrerpolicy="no-referrer"></p><p>比如，假设你在 Windows 365 云 PC 上打开了带有恶意附件的网络钓鱼电子邮件，并且逃过了系统自带的 Microsoft Defender 安全软件的眼线。</p><p>那样一旦你启用了文档中的恶意宏，它就可以安装远程访问程序，以便攻击者对 Cloud PC 展开进一步的渗透。</p><p>在利用 PrintNightmare 等漏洞来获得管理员权限之后，借助 mimikatz 转储明文凭据等操作都将唾手可得。</p><p>更别提威胁行为者会结合多重手段，向其它 Microsoft 服务和可能的企业内部网络来横向传播。</p>   
</div>
            