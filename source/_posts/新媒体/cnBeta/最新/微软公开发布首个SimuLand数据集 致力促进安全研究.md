
---
title: '微软公开发布首个SimuLand数据集 致力促进安全研究'
categories: 
 - 新媒体
 - cnBeta
 - 最新
headimg: 'https://static.cnbetacdn.com/thumb/article/2021/0806/4a10ac7e6a94a77.png'
author: cnBeta
comments: false
date: Fri, 06 Aug 2021 10:26:53 GMT
thumbnail: 'https://static.cnbetacdn.com/thumb/article/2021/0806/4a10ac7e6a94a77.png'
---

<div>   
<strong>微软在一个月前宣布了开源 SimuLand 项目，以帮助安全研究人员轻松部署实验环境、重现攻击模式和相关技术。</strong>然后验证 Microsoft 365 Defender、Azure Defender 和 Azure Sentinel 等工具，能否检测到对抗模式。研究人员还可以从这些实验中捕获遥测数据，以扩展他们自己的研究。现在，微软又发布了首次模拟演练的公共数据集。<br>
<p><a href="https://static.cnbetacdn.com/article/2021/0806/4a10ac7e6a94a77.png" target="_blank"><img src="https://static.cnbetacdn.com/thumb/article/2021/0806/4a10ac7e6a94a77.png" referrerpolicy="no-referrer"></a></p><p style="text-align: center;">图 1 - SimuLand 安全研究方法 / 数据威胁图集（来自：Microsoft <a href="https://www.microsoft.com/security/blog/2021/08/05/sharing-the-first-simuland-dataset-to-expedite-research-and-learn-about-adversary-tradecraft/" target="_self">官网</a>）</p><p>如果你对微软如何生成这些数据集感到好奇，还请翻阅参考实验指南运行的首次模拟和遥测数据结果。</p><p>具体说来是，其模拟了攻击者是如何从本地 ADFS 服务器窃取 Azure 目录联合服务（ADFS）的令牌签名证书。</p><p>然后利用它来签署新的安全声明标记语言（SAML）令牌，并借助 Microsoft Graph API 来访问邮件数据。</p><p><img src="https://static.cnbetacdn.com/article/2021/0806/33c01936b3bc839.jpg" referrerpolicy="no-referrer"></p><p style="text-align: center;">图 2 - 映射到源数据的对抗技术</p><p>本次公布的数据集，是微软在首次模拟演练期间汇总的安全事件集合，该公司通过 Microsoft 365 Defender 高级搜索 API、以及 Azure Log Analytics 工作区 API 而开展收集工作。</p><p>微软表示，通过分享该数据集，研究人员将能够更好地分析对抗性场景、改进他们的检测规则、对事件链进行建模、自动化模拟计划，或者在组织内部规划黑客马拉松等挑战。</p><p>展望未来，微软还计划分享更多数据集、并添加新的实验指南。感兴趣的朋友，可移步至 SimuLand 的 GitHub <a href="https://github.com/Azure/SimuLand" target="_self">项目主页</a>，或查看微软安全数据集的<a href="https://securitydatasets.com/notebooks/compound/GoldenSAMLADFSMailAccess.html" target="_self">存储库</a>。</p>   
</div>
            