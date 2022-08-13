
---
title: '利用macOS端Zoom安装器漏洞 黑客可以接管你的Mac'
categories: 
 - 新媒体
 - cnBeta
 - 最新
headimg: 'https://static.cnbetacdn.com/article/2022/0813/068f1c0449d1879.webp'
author: cnBeta
comments: false
date: Sat, 13 Aug 2022 02:28:05 GMT
thumbnail: 'https://static.cnbetacdn.com/article/2022/0813/068f1c0449d1879.webp'
---

<div>   
<strong>一名安全专家近日发现利用 macOS 端 Zoom 应用程序，掌控整个系统权限的攻击方式。</strong>本周五在拉斯维加斯召开的 Def Con 黑客大会上，Mac 安全专家帕特里克·沃德尔（Patrick Wardle）在演讲中详细介绍了这个漏洞细节。<br>
 <p style="text-align:center"><img src="https://static.cnbetacdn.com/article/2022/0813/068f1c0449d1879.webp" referrerpolicy="no-referrer"></p><p style="text-align: left;">虽然 Zoom 已经修复了演示中的部分 BUG，但是沃德尔还演示了一个尚未修复、依然可以影响 macOS 系统的漏洞。该漏洞通过 Zoom 应用的安装器进行入侵，虽然在首次添加到 macOS 的时候需要用户输入系统密码，不过沃德尔表示可以通过超级用户权限在后台执行自动升级功能。</p><p style="text-align: left;">在 Zoom 发布修复更新之后，在安装新的安装包的时候都需要审查是否经过 Zoom 加密签署。不过这种审查方式依然存在缺陷，任意文件只需要修改为和 Zoom 签署认证相同的文件名称就可以通过测试，因此攻击者可以伪装任意恶意程序，并通过提权来掌控系统、</p><p style="text-align: left;">其结果是一种权限提升攻击方式，需要攻击者已经获得了对目标系统的初始访问权限，然后利用漏洞来获得更高级别的访问权限。 在这种情况下，攻击者从受限用户帐户开始，但升级为最强大的用户类型——称为“superuser”或“root”——允许他们添加、删除或修改机器上的任何文件。</p><p style="text-align:center"><img src="https://static.cnbetacdn.com/article/2022/0813/e255965be18b276.webp" referrerpolicy="no-referrer"></p><p style="text-align: left;">沃德尔在去年 12 月向 Zoom 报告了这个问题。虽然 Zoom 随后发布了一个修复补丁，但是令他沮丧的这个修复补丁包含另一个错误，这意味着该漏洞仍然可以以稍微更迂回的方式利用，因此他向 Zoom 披露了第二个错误，并等待了八个月才发布研究。</p><p style="text-align: left;">沃德尔表示：“对我来说，我不仅向 Zoom 报告了错误，还报告了错误以及如何修复代码，所以等了六、七、八个月，知道所有 Mac 版本的 Zoom 都在用户的计算机上仍然易受攻击，真是令人沮丧”。</p>   
</div>
            