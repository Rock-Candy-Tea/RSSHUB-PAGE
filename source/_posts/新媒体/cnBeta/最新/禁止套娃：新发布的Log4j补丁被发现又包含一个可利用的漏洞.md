
---
title: '禁止套娃：新发布的Log4j补丁被发现又包含一个可利用的漏洞'
categories: 
 - 新媒体
 - cnBeta
 - 最新
headimg: 'https://static.cnbetacdn.com/article/2021/12/5c13f14a11b370e.png'
author: cnBeta
comments: false
date: Thu, 16 Dec 2021 13:40:55 GMT
thumbnail: 'https://static.cnbetacdn.com/article/2021/12/5c13f14a11b370e.png'
---

<div>   
就在我们了解到国家支持的黑客已经开始研究上周震惊网络安全界的Log4j漏洞问题时，其他研究人员发出了一个令人不安的发展信号。Log4j黑客，也被称为Log4Shell已经有一个补丁，已经可以部署到企业。<strong>但事实证明，这个补丁玩起了“套娃”：它解决原有问题的同时又产生新的安全问题，且可以被外部利用。因此，希望保护他们的系统免受Log4j攻击的公司必须部署一个新的补丁，修复之前的补丁。</strong><br>
 <p><a href="https://static.cnbetacdn.com/article/2021/12/5c13f14a11b370e.png" target="_blank"><img src="https://static.cnbetacdn.com/article/2021/12/5c13f14a11b370e.png" referrerpolicy="no-referrer"></a></p><p>正如我们在以前的报道中所解释的，Log4j黑客是非常危险的。这是因为它几乎影响到所有提供互联网服务的公司。这个安全漏洞存在于一个被广泛使用的Java日志工具中。自上周四披露以来，网络安全研究人员已经目睹了数十万次利用该漏洞的尝试。这包括来自国家支持的黑客的攻击，与大多数黑客相比，他们拥有大量可支配的资源。只要互联网公司不对他们的系统应用现有的Log4j补丁，他们就会面临风险。<br></p><p>黑客可以利用Log4j黑客技术，在没有密码的情况下进入计算机服务器。从那里，他们可以安装其他恶意程序。这些工具将让他们窃取信息，进行勒索软件攻击，或挖掘加密货币。根据最初描述安全问题的报告，有人利用了《Minecraft》里面的漏洞。<a data-link="1" href="https://c.duomai.com/track.php?site_id=242986&euid=&t=https://www.microsoftstore.com.cn/" target="_blank">微软</a>很快给Minecraft打了补丁，并不断发布关于Log4j漏洞在外部世界的安全更新。</p><p>普通的终端用户无法自己修复Log4j黑客的问题。这并不像将操作系统或应用程序更新到最新、最安全的版本那样容易。是互联网公司必须部署最新的Log4j补丁来保护服务器。</p><p>但安全研究人员已经发现，Apache基金会上周发布的Log4j 2.15.0补丁至少有两个需要修复的漏洞。报告说，已经安装了Log4j 2.15.0的企业应该尽快安装2.16.0版本。</p><p>根据一些研究人员的说法，Log4j 2.15.0的补丁"在某些非默认配置中"并不完整。反过来，这使得攻击者可以对打了补丁的系统发动攻击。来自Praetorian的安全研究人员也详细介绍了新的安全问题，他们解释说，黑客仍然可以从已经部署了Log4j 2.15.0补丁的服务器上窃取数据。</p><p>"在我们的研究中，我们已经证明2.15.0在某些情况下仍然可以实现敏感数据的渗出，"研究人员说。"我们已经把这个问题的技术细节传递给了Apache基金会，但在这期间，我们强烈建议客户尽快升级到2.16.0。"</p><p>Praetorian发布了对Log4j 2.15.0补丁的概念证明攻击，但没有披露使其成为可能的技术细节。</p><p>了解更多：</p><p><a href="https://github.com/cckuailong/Log4j_CVE-2021-45046" _src="https://github.com/cckuailong/Log4j_CVE-2021-45046" target="_blank">https://github.com/cckuailong/Log4j_CVE-2021-45046</a><br></p>   
</div>
            