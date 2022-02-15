
---
title: '数千开发者的npm账户在使用域名已过期的电子邮件地址'
categories: 
 - 新媒体
 - cnBeta
 - 最新
headimg: 'https://static.cnbetacdn.com/article/2022/0215/f40d6d96534927f.png'
author: cnBeta
comments: false
date: Tue, 15 Feb 2022 10:33:56 GMT
thumbnail: 'https://static.cnbetacdn.com/article/2022/0215/f40d6d96534927f.png'
---

<div>   
去年，微软和北卡罗莱纳州立大学的研究人员，分析了上传到 npm 上的 1630101 个库的元数据。<strong>结果发现，数以千计的 JavaScript 开发者账户，正在使用域名已过期的电子邮件地址，意味着他们的项目很容易被劫持。</strong>在 2818 名项目维护者使用的电子邮件地址中，某些已过期的域名已挂在 GoDaddy 等网站上待售。<br>
 <p><img src="https://static.cnbetacdn.com/article/2022/0215/f40d6d96534927f.png" referrerpolicy="no-referrer"></p><p style="text-align: center;">NPM 是“节点包管理器”（<a href="https://www.npmjs.com/" target="_self">Node Package Manager</a>）的缩写</p><p>研究人员指出，别有用心的攻击者可购买这些域名，在其电子邮件服务器上重新注册维护者的地址，然后重置维护者的账户密码、以接管受害者的 npm 包。</p><p>这类攻击得逞的隐患很大，因为 npm 门户不会对账户所有者强制执行 2FA 双因素身份验证。意味着一旦被攻击者重置密码，他们就可肆意篡改相关软件包。</p><blockquote><p>共计 2818 个维护者账户在管理 8494 个包，其中平均有 2.43 个直接依赖项，表明特定攻击可波及数以万计的其它下游项目。</p><p>所有者可能会觉察到其账户被劫持，但考虑到许多 npm 库和账户要么长期被冷落（高达 58.7% 未得到维护）、要么就是已被遗弃（44.3%），情况并不容乐观。</p></blockquote><p>研究团队将它们的发现通报给了 npm 安全团队，但并未说明对方给出了怎样的回应。</p><p>截止 The Record 发稿时，发给 npm 上属的 GitHub 的电子邮件，暂未看到退件回执。</p><blockquote><p>庆幸的是，在研究结果于 2021 年 12 月发布的前几天，npm 已宣布一项新计划，声称要逐渐让开发者账户强制执行双因素身份验证。</p><p>该过程将分多个阶段进行，且本月初注册的前百名维护者账户都已落实 2FA 方案。欲知详情，还请翻阅《<a href="https://arxiv.org/abs/2112.10165" target="_self">npm 供应链中的薄弱环节</a>》一文。</p></blockquote><p><strong>以下是研究团队的一些其它发现：</strong></p><blockquote><p>● 33249 个软件包（2.2%）使用了安装脚本，或被滥用于执行恶意命令、且违反 npm 的最佳安全实践。</p><p>● 排名前 1% 的软件包（14941 个），平均有 32.4 名维护者 —— 这为针对不活跃 / 疏于照顾的开发者账户进行的攻击敞开了大门。</p><p>● 389 个软件包，平均有 40 名贡献者 —— 这为意外植入的安全漏洞、或让项目充斥潜在恶意代码而留下了隐患。</p><p>● 前 1% 维护者，平均管理着 180.3 个软件包；而直接依赖的包数量，平均为 4010 个 —— 意味着某些开发者可能可能过劳，或没有太多精力来彻底维护或审查软件包的变更。</p></blockquote>   
</div>
            