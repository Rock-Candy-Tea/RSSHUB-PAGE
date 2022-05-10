
---
title: '黑客正积极利用BIG-IP设备漏洞 配置错误引发危险等级9.8安全隐患'
categories: 
 - 新媒体
 - cnBeta
 - 最新
headimg: 'https://static.cnbetacdn.com/article/2022/0510/fd61178a7cd1ad6.png'
author: cnBeta
comments: false
date: Tue, 10 May 2022 11:44:59 GMT
thumbnail: 'https://static.cnbetacdn.com/article/2022/0510/fd61178a7cd1ad6.png'
---

<div>   
<strong>上周，F5 披露并修补了一个严重等级达到 9.8 / 10 分的 BIG-IP 漏洞。由于 iControl REST 身份验证配置错误，黑客可借此以 root 权限运行系统命令。</strong>据悉，iControl REST 是一组用于配置和管理 BIG-IP 设备的基于 Web 的编程接口，而 BIG-IP 则是该组织用于负载均衡、防火墙、以及检查和加密进出网络数据的一系列设备。<br>
<p><img src="https://static.cnbetacdn.com/article/2022/0510/fd61178a7cd1ad6.png" alt="1.png" referrerpolicy="no-referrer"></p><p><a href="https://arstechnica.com/information-technology/2022/05/hackers-are-actively-exploiting-big-ip-vulnerability-with-a-9-8-severity-rating/" target="_self">ArsTechnica</a> 指出：BIG-IP 涵盖了超过 16000 个可在线发现的设备实例，且官方宣称有被财富 50 强中的 48 家所采用。</p><p><strong><a href="https://static.cnbetacdn.com/article/2022/0510/e6f916a0db15888.png" target="_blank"><img src="https://static.cnbetacdn.com/thumb/article/2022/0510/e6f916a0db15888.png" alt="2.png" referrerpolicy="no-referrer"></a></strong></p><p><strong>然而让 Randori 安全研究主管 Aaron Portnoy 感到震惊的是：</strong></p><blockquote><p>由于身份验证的设施方法存在缺陷，该问题竟使得能够访问管理界面的攻击者伪装系统管理员身份，之后便可与应用程序提供的所有端点进行交互、甚至执行任意代码。</p></blockquote><p><img src="https://static.cnbetacdn.com/article/2022/0510/9349a865593e059.png" alt="3.png" referrerpolicy="no-referrer"></p><p>鉴于 BIG-IP 靠近网络边缘、且作为管理 Web 服务器流量的设备功能，它们通常处于查看受 HTTPS 保护的流量 / 解密内容的有利位置。</p><p><img src="https://static.cnbetacdn.com/article/2022/0510/0c507553ec63303.png" alt="4.png" referrerpolicy="no-referrer"></p><p>过去一整天，Twitter 上流传的大量图片，揭示了黑客是如何积极在野外利用 CVE-2022-1388 漏洞，来访问名为 bash 的 F5 应用程序端点的。</p><p><a href="https://static.cnbetacdn.com/article/2022/0510/31e2eb77c5caa47.jpg" target="_blank"><img src="https://static.cnbetacdn.com/thumb/article/2022/0510/31e2eb77c5caa47.jpg" alt="5.jpg" referrerpolicy="no-referrer"></a></p><p>其功能是提供一个接口，用于将用户提供的输入，作为具有 root 权限的 bash 命令来运行。更让人感到震惊的是，虽然不少概念验证（PoC）用到了密码，但也有一些案例甚至可在不提供密码的情况下运作。</p><p><img src="https://static.cnbetacdn.com/article/2022/0510/f9af2a0f0415cd4.png" alt="6.png" referrerpolicy="no-referrer"></p><p>对于如此重要的设备命令竟然被这样松散地处置，许多业内人士都感到大为不解，此外有报告提到攻击者可利用 webshell 后门来维持对 BIG-IP 设备的控制（即便修补后也是如此）。</p><p><img src="https://static.cnbetacdn.com/article/2022/0510/df47f72af15b090.png" alt="7.png" referrerpolicy="no-referrer"></p><p>在其中一个案例中，有 IP 地址为 216.162.206.213 和 209.127.252.207 的攻击者将有效载荷置入了 /tmp/f5.sh 的文件路径、从而在 /usr/local/www/xui/common/css/ 中部署基于 PHP 的 webshell 后门。</p><p><img src="https://static.cnbetacdn.com/article/2022/0510/0539f505e24ae97.png" alt="8.png" referrerpolicy="no-referrer"></p><p>当然，这并不是安全研究人员被如此离谱严重的漏洞给惊到。比如不少人都提到，这种情况与两年前的 CVE-2020-5902 实在太过相似。</p><p>不过随着大家对于 CVE-2022-1388（RCE）漏洞的易得性、强大功能、以及广泛性有了更深入的了解，相关风险也正笼罩到更多人的头上。</p><p><img src="https://static.cnbetacdn.com/article/2022/0510/d83783112df8e7a.png" alt="9.png" referrerpolicy="no-referrer"></p><p>如果你所在的组织机构正在使用 F5 的 BIG-IP 设备，还请着重检查并修补该漏洞、以减轻任何可能遇到的潜在风险。</p><p>有需要的话，可参考 <a href="https://www.randori.com/blog/vulnerability-analysis-cve-2022-1388/" target="_self">Randori</a> 热心提供的漏洞详情分析 / 单行 bash 脚本，并抽空详阅 F5 给出的其它建议与指导（<a href="https://support.f5.com/csp/article/K23605346" target="_self">KB23605346</a>）。</p>   
</div>
            