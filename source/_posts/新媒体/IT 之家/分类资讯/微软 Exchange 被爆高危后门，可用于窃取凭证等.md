
---
title: '微软 Exchange 被爆高危后门，可用于窃取凭证等'
categories: 
 - 新媒体
 - IT 之家
 - 分类资讯
headimg: 'https://img.ithome.com/newsuploadfiles/2022/7/b185247e-f96e-40a0-82aa-5f204ba2baaf.png'
author: IT 之家
comments: false
date: Fri, 01 Jul 2022 23:44:55 GMT
thumbnail: 'https://img.ithome.com/newsuploadfiles/2022/7/b185247e-f96e-40a0-82aa-5f204ba2baaf.png'
---

<div>   
<p data-vmark="312f"><a class="s_tag" href="https://www.ithome.com/" target="_blank">IT之家</a> 7 月 2 日消息，卡巴斯基的安全团队本周四发布了一份令人担忧的报告。报告指出在 Exchange 服务器上发现了一个全新的、难以检测的后门，该后门可用于获取长久的、未被检测到的电子邮件访问权限，甚至接管目标组织的基础设施，而这正是曾经专注于利用 ProxyLogon Microsoft Exchange 服务器漏洞的攻击者发现的新漏洞。</p><p data-vmark="62d9">卡巴斯基的研究人员表示，现在的攻击者逐渐呈现出一种趋势，他们将恶意后门模块部署在 Windows 的互联网信息服务 (IIS) 服务器（如 Exchange 服务器）中，从而引起类似 SessionManager 的一系列高危漏洞。</p><p data-vmark="3d3e">IT之家了解到， SessionManager 恶意软件常常伪装成 Internet 信息服务 (IIS) 的合法模块，而 IIS 正是默认安装在 Exchange 服务器上的 Web 服务。组织经常部署 IIS 模块以简化其 Web 基础架构上的特定工作流程。</p><p data-vmark="5b3f">卡巴斯基报告称，目前已经有 24 个非政府组织的 34 个服务器已被 SessionManager 进行入侵。截至本月初，仍有 20 个组织受到感染。</p><p data-vmark="2b5e">研究人员补充道，SessionManager 后门于 2021 年 3 月首次发现，已被用于针对非洲、欧洲、中东和南亚的非政府组织 (ngo)。</p><p data-vmark="33e7" style="text-align: center;"><img src="https://img.ithome.com/newsuploadfiles/2022/7/b185247e-f96e-40a0-82aa-5f204ba2baaf.png" w="640" h="360" title="微软 Exchange 被爆高危后门，可用于窃取凭证等" width="640" height="360" referrerpolicy="no-referrer"></p><p data-vmark="a083">卡巴斯基高级安全研究员皮埃尔・德尔彻 (Pierre Delcher) 表示:“自 2021 年第一季度以来，利用 Exchange 服务器漏洞一直是网络罪犯想要进入目标基础设施的首选”“最近发现的 SessionManager 一年多来都没有被发现，现在仍然在被人利用。”</p><p data-vmark="6129">卡巴斯基团队建议定期对暴露在外的 ISS 服务器中的恶意模块进行筛查，重点检测网络上的横向移动部分，并密切监控数据流动，以避免数据被泄露。</p><p data-vmark="25d0">德尔彻警告说:“就 Exchange 服务器而言，值得我们多次强调：过去一年的漏洞已经让它们成为了完美的攻击目标，无论其恶意意图如何，所以它们应该被仔细审计和监控，以防被隐藏地植入设备，如果它们还没有被隐藏的话。”</p>
          
</div>
            