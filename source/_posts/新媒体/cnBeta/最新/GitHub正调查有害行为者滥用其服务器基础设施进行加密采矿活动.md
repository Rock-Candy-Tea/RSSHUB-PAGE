
---
title: 'GitHub正调查有害行为者滥用其服务器基础设施进行加密采矿活动'
categories: 
 - 新媒体
 - cnBeta
 - 最新
headimg: 'https://static.cnbetacdn.com/thumb/article/2021/0404/679f0b8f90e05d2.jpg'
author: cnBeta
comments: false
date: Sun, 04 Apr 2021 07:57:24 GMT
thumbnail: 'https://static.cnbetacdn.com/thumb/article/2021/0404/679f0b8f90e05d2.jpg'
---

<div>   
<strong>代码托管服务GitHub的发言人今天表示其在积极调查一系列针对其云基础设施的攻击，这些攻击让网络犯罪分子植入并滥用该公司的服务器进行非法的加密采矿作业。</strong>这些攻击自2020年秋季以来一直在进行，其滥用了GitHub的一个名为GitHub
Actions的功能，该功能允许用户在其GitHub仓库内发生某个事件后自动执行任务和工作流程。<br>
 <p><a href="https://static.cnbetacdn.com/article/2021/0404/679f0b8f90e05d2.jpg" target="_blank"><img src="https://static.cnbetacdn.com/thumb/article/2021/0404/679f0b8f90e05d2.jpg" title alt="GitHub-attacker-job.jpg" referrerpolicy="no-referrer"></a></p><p>在今天的电话中，荷兰安全工程师Justin Perdok表示至少有一个威胁行为者正在针对可能启用GitHub Actions的GitHub仓库。</p><p>攻击涉及伪造一个合法的库，将恶意的GitHub Actions添加到原始代码中，然后向原始仓库提交Pull Request，以便将代码合并回原始仓库。但攻击并不依赖于原始项目所有者批准恶意Pull Request。Perdok说，只要提交Pull Request就足以实现攻击。</p><p><img src="https://static.cnbetacdn.com/article/2021/0404/95a71ca2f91b48b.png" title alt="GitHub-attacker-history.png" referrerpolicy="no-referrer"></p><p>这位荷兰安全工程师告诉我们，攻击者专门针对那些拥有自动化工作流程的GitHub项目所有者，这些项目所有者通过自动化作业测试传入的Pull Request。</p><p>一旦这些恶意Pull Request被提交，GitHub的系统就会读取攻击者的代码，并通过虚拟机在GitHub的设施上下载并运行加密货币挖掘软件。</p><p>攻击者仅通过一次攻击就产生了100个虚拟加密矿机，从而为GitHub的基础设施创造了巨大的计算负荷。攻击者似乎是随机发生的，而且规模很大。Perdok表示，他发现至少有一个账户创建了数百个包含恶意代码的Pull Request。</p><p>这些攻击似乎至少从2020年11月开始发生，当时第一例是由一名法国软件工程师报告的。</p><p>在今天的一封电子邮件中，GitHub表示，他们 "意识到这种活动，并正在积极调查"，他们去年对法国工程师也是这么说的。然而，现在的解决方案似乎知识在和攻击者玩猫捉老鼠的游戏，因为一旦旧账户被检测到并暂停，攻击者就会注册新账户。</p><p>目前，这次攻击似乎没有以任何方式破坏用户的项目，似乎只是专注于滥用GitHub基础设施。</p>   
</div>
            