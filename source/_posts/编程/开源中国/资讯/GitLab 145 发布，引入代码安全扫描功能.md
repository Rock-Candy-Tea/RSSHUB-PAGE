
---
title: 'GitLab 14.5 发布，引入代码安全扫描功能'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://oscimg.oschina.net/oscnet/up-5091a5144f1b67f8438c6c874ecb905a690.png'
author: 开源中国
comments: false
date: Sun, 28 Nov 2021 08:14:00 GMT
thumbnail: 'https://oscimg.oschina.net/oscnet/up-5091a5144f1b67f8438c6c874ecb905a690.png'
---

<div>   
<div class="content">
                                                                                            <p>GitLab 14.5 已正式<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fabout.gitlab.com%2Freleases%2F2021%2F11%2F22%2Fgitlab-14-5-released%2F" target="_blank">发布</a>，主要更新内容包括引入代码安全扫描、使用 CI/CD 隧道进行细粒度的权限控制、合并 PR 批准的 Group 层级设置、免费 K8s 代理、项目专题 (project topics) 等多项功能和改进。</p> 
<p><img alt src="https://oscimg.oschina.net/oscnet/up-5091a5144f1b67f8438c6c874ecb905a690.png" referrerpolicy="no-referrer"></p> 
<h3>引入代码安全扫描</h3> 
<p>Gitlab 14.5 引入了对基础设施即代码 (IaC) 配置文件的安全扫描。与所有的 SAST 扫描器一样，该功能也是免费开放。</p> 
<p>IaC 安全扫描器的初始版本支持 Terraform、Ansible、AWS CloudFormation 和 Kubernetes 配置文件扫描，并基于开源保持基础设施即代码安全 (KICS) 项目。新的 IaC 扫描功能加入了现有的 Kubernetes 清单 SAST 扫描器。</p> 
<p>如果熟悉 GitLab SAST，IaC 扫描的工作原理完全相同，包括独立的 IaC 扫描 CI 配置文件、安全配置页面上基于 UI 的启用工具以及对所有终端漏洞管理功能的支持，包括安全仪表板和合并请求小部件。使用 IaC 扫描模板可轻松地使用其他扫描器扩展 IaC 扫描。</p> 
<p><img alt src="https://oscimg.oschina.net/oscnet/up-b2e2431ed5f0f906370218b762ca89e8c0a.png" referrerpolicy="no-referrer"></p> 
<h3>使用 CI/CD 隧道进行细粒度的权限控制</h3> 
<p>GitLab 14.5 发布了通用访问模拟和 CI/CD 作业模拟。这些模拟可以在 Agent 配置文件中进行指定，并且可以使用 Kubernetes RBAC 规则管理模拟的帐户权限。</p> 
<p><img alt src="https://oscimg.oschina.net/oscnet/up-2150373d641b9fb1f81c55efebedd12116d.png" referrerpolicy="no-referrer"></p> 
<h3>项目专题 (project topics)</h3> 
<p>此版本在项目中增加了一个新的探索主题 (Explore topics) 选项卡。</p> 
<ul> 
 <li>主题可按受欢迎程度（具有此主题的项目数）进行排序</li> 
 <li>主题可以按名称搜索，然后按相似度和流行度排序</li> 
</ul> 
<p><img alt src="https://oscimg.oschina.net/oscnet/up-768b5a4c2c8a08e031db596afea536e3f48.png" referrerpolicy="no-referrer"></p> 
<p><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fabout.gitlab.com%2Freleases%2F2021%2F11%2F22%2Fgitlab-14-5-released%2F" target="_blank">详情查看发布公告</a>。</p>
                                        </div>
                                      
</div>
            