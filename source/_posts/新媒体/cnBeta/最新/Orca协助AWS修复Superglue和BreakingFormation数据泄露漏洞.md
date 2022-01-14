
---
title: 'Orca协助AWS修复Superglue和BreakingFormation数据泄露漏洞'
categories: 
 - 新媒体
 - cnBeta
 - 最新
headimg: 'https://static.cnbetacdn.com/article/2022/0114/1cee12b2a4cc6cc.gif'
author: cnBeta
comments: false
date: Fri, 14 Jan 2022 06:01:12 GMT
thumbnail: 'https://static.cnbetacdn.com/article/2022/0114/1cee12b2a4cc6cc.gif'
---

<div>   
<strong>近日，亚马逊云服务被曝正在修补所谓的“强力胶”（Superglue）漏洞。</strong>此外还有一个被称作 AWS CloudFormation 的 Bug，攻击者可利用它们摸到其他用户的敏感数据。Orca 安全研究团队率先披露了 AWS 工具中的缺陷，庆幸的是两个 Bug 都已得到完全修补。<br>
 <p><img src="https://static.cnbetacdn.com/article/2022/0114/1cee12b2a4cc6cc.gif" alt="0.gif" referrerpolicy="no-referrer"></p><p style="text-align: center;">（来自：<a href="https://orca.security/resources/blog/aws-glue-vulnerability/" target="_self">Orca Security</a>）</p><p><strong>首先聊聊 Superglue 漏洞，用户可借此访问其他 AWS Glue 用户管理的信息。</strong></p><p>AWS 官方宣称 Glue 是一项无服务器的数据集成服务，旨在轻松发现、准备和组合那些用于分析、机器学习和应用程序开发的数据。</p><p>事实上，亚马逊服务的体量着实庞大，以至于 Glue 用户能够免费存储多达百万个对象。</p><blockquote><p>Orca 指出 —— 我们能够识别 AWS Glue 中的一项功能，它可用于获取 AWS 官方服务账户中的某个角色的凭证，从而赋予了对内部服务 API 的完全访问权限。</p><p>结合内部错误配置和 Glue 内部访问 API，我们得以将帐户内的权限进一步提升至不受限的水平，包括以完全的管理权限访问某个区域的所有资源。</p></blockquote><p><img src="https://static.cnbetacdn.com/article/2022/0114/945cbe4a214af1b.png" alt="1.png" referrerpolicy="no-referrer"></p><p>在受 Glue 服务信任的 AWS 客户账户中，至少都有一个类似角色的账户。</p><p>得逞后，攻击者能够查询和修改区域内的相关资源，包括但不限于 Glue 作业、开发端点、工作流、爬虫、触发器等元数据。</p><blockquote><p>Orca 证实 —— 其已确认通过该漏洞控制众多账户、以访问其他 AWS Glue 用户管理的信息的能力。</p><p>庆幸的是，漏洞披露不久后，亚马逊在数小时内就做出了回应，并于第二日实施了部分缓解，直到数日后彻底封堵了相关问题。</p></blockquote><p><img src="https://static.cnbetacdn.com/article/2022/0114/a0fb08a3aa73357.png" alt="2-0.png" referrerpolicy="no-referrer"></p><p>第二个漏洞影响到了 AWS CloudFormation，通过将基础设施视作代码， 用户可对第一和第三方资源开展建模、预置和管理。</p><p>这种“基础设施即代码”的范式，已于近年来愈加受到客户的青睐。在迁移至云端的时候，其配置与维护的便利性也相当出众。</p><blockquote><p>然而被称作 <a href="https://orca.security/resources/blog/aws-cloudformation-vulnerability/" target="_self">BreakingFormation</a> 的第二个 Bug，却可被用于泄露在易受攻击的服务器上发现的机密文件。</p><p>此外服务器端请求（SSRF）易受未经授权披露内部 AWS 基础设施服务凭证的影响 —— 庆幸的是，该漏洞在向 AWS 披露六天内完成了彻底修复。</p></blockquote><p><img src="https://static.cnbetacdn.com/article/2022/0114/f9327daef5f0cd2.png" alt="2-1-7.png" referrerpolicy="no-referrer"></p><p>最后，Bleeping Computer 分享了 AWS 副总裁 Colm MacCárthaigh 在 Twitter 上披露的与 BreakingFormation 漏洞有关的更多细节，且一开始就承认了 Orca 能够获得对所有 AWS 账户资源的访问权限的说法。</p><p>然后 Orca 首席技术官 Yoav Alon 回应称 CloudFormation 的暴露范围，并不像最初预期的那样广泛。</p><blockquote><p>我们立即向 AWS 通报了该问题，后者迅速采取了行动来解决这个问题。</p><p>AWS 安全团队在不到 25 小时内编写了首个修复程序，并于 6 日内落实到了所有 AWS 区域。</p><p>Orca 安全研究人员帮助测试了修复补丁，以确保妥善解决相关问题，且我们能够验证其不会再遭到利用。</p></blockquote>   
</div>
            