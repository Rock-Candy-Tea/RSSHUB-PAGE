
---
title: 'PrintNightmare漏洞的技术拉锯战仍在进行 计算机管理员权限再度失守'
categories: 
 - 新媒体
 - cnBeta
 - 最新
headimg: 'https://static.cnbetacdn.com/article/2021/0801/4beff89f5803177.webp'
author: cnBeta
comments: false
date: Sun, 01 Aug 2021 00:09:47 GMT
thumbnail: 'https://static.cnbetacdn.com/article/2021/0801/4beff89f5803177.webp'
---

<div>   
影响广泛的微软Windows的PrintNightmare漏洞事件拒绝结束，另一个版本的黑客攻击手法意味着任何用户都可以在他们的PC上绕过验证措施直接获得管理权限，甚至从一个级别很低的账户中也是如此。这一入侵方法是由Benjamin Delpy开发的。<br>
<p>他利用了<a data-link="1" href="https://microsoft.pvxt.net/x9Vg1" target="_blank">Windows</a>从远程打印服务器安装驱动程序并在系统权限级别运行这些驱动程序这一事实实现（即使是有限用户也可以安装远程打印机）。</p><p>他在\\printnightmare[.]gentilkiwi[.]com建立了一个远程打印机服务器，并精心制作了一个用于概念验证的黑客驱动，只要在各个版本的Windows操作系统中连接这台远程打印机，高权限的命令提示符就会显示出来，这意味着企业用户或黑客只要有权限进入有限账户，现在就可以轻松提升权限，获得对电脑的完全控制。</p><p><img src="https://static.cnbetacdn.com/article/2021/0801/4beff89f5803177.webp" title alt="printnightmare-revenge.webp" referrerpolicy="no-referrer"></p><p><a href="https://static.cnbetacdn.com/article/2021/0801/9d1edd6adcc7a77.jpg" target="_blank"><img src="https://static.cnbetacdn.com/thumb/article/2021/0801/9d1edd6adcc7a77.jpg" title alt="E7kxZ_XWQAEHVYA.jpg" referrerpolicy="no-referrer"></a></p><p>BleepingComputer在运行Windows 10 21H1的完全打过补丁的电脑上进行了概念验证，结果发现恶意驱动程序会被Windows Defender检测到，但这个漏洞依旧按计划顺利运行。</p><p>在<a data-link="1" href="https://c.duomai.com/track.php?site_id=242986&euid=&t=https://www.microsoftstore.com.cn/" target="_blank">微软</a>修复这个问题之前，提出缓解措施相当困难，禁用Printer Spooler是一个方法，或者系统管理员需要创建一个允许用户安装的远程打印机的自定义列表。</p><p><img src="https://static.cnbetacdn.com/article/2021/0801/751146096adcfa7.png" title alt="M`~&#123;%]WU3KCU74Z&#125;_))F(I1.png" referrerpolicy="no-referrer"></p>   
</div>
            