
---
title: 'GitLab 14.1 发布：新增 Helm 图表支持'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://static.oschina.net/uploads/space/2021/0726/172235_If0q_2720166.png'
author: 开源中国
comments: false
date: Mon, 26 Jul 2021 23:34:00 GMT
thumbnail: 'https://static.oschina.net/uploads/space/2021/0726/172235_If0q_2720166.png'
---

<div>   
<div class="content">
                                                                    
                                                        <p>GitLab 14.1 已正式<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fabout.gitlab.com%2Freleases%2F2021%2F07%2F22%2Fgitlab-14-1-released%2F" target="_blank">发布</a>，主要更新内容包括：新增 Helm 图表支持、支持将 GitLab Runner 连接到 Kubernetes 集群、支持在 VS Code 中查看 MR 的分支等。</p> 
<p><img src="https://static.oschina.net/uploads/space/2021/0726/172235_If0q_2720166.png" referrerpolicy="no-referrer"></p> 
<h3>构建、发布和共享 Helm 图表</h3> 
<p>Helm 是 Kubernetes 的包管理工具，用于将图表 (Charts) 定义为 Helm 包，其中包含在 Kubernetes 集群内运行应用程序、工具或服务所需的所有资源定义。对于创建和管理自己的 Helm 图表的组织来说，拥有一个中央仓库来收集和共享它们非常重要。</p> 
<p>GitLab 此前已支持多种包管理器格式，但没有支持 Helm。不过从这个版本开始，用户可以使用 GitLab 项目来发布和共享打包的 Helm 图表。只需将项目添加为远程项目，使用个人访问、部署或 CI/CD 作业令牌进行身份验证。完成后，可以使用 Helm 客户端或 GitLab CI/CD 来管理 Helm 图表，还可以使用 API 或用户界面下载图表。</p> 
<p><img src="https://static.oschina.net/uploads/space/2021/0727/062147_Pl4J_2720166.png" referrerpolicy="no-referrer"></p> 
<h3>Kubernetes 集群的 CI/CD 隧道</h3> 
<p>GitLab 现在附带一个 CI/CD 隧道 (CI/CD Tunnel)，它使用 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdocs.gitlab.com%2Fee%2Fuser%2Fclusters%2Fagent%2F" target="_blank">GitLab Kubernetes 代理</a>将 GitLab Runners 与 Kubernetes 集群连接起来，这样操作可支持通用的 GitOps 工作流，其中可以在管道中对部署逻辑进行编码。</p> 
<h3>代码覆盖合并请求批准规则</h3> 
<p>为了保持高代码测试覆盖率，需要确保对代码库的合并请求永远不会降低测试覆盖率。以前，强制执行此操作的唯一方法是要求用户批准，他们将检查测试覆盖率是否降低作为其审查的一部分。现在，可以使用新的 Coverage check 批准规则强制执行此组织策略。</p> 
<p><img alt src="https://oscimg.oschina.net/oscnet/up-c0e73c2107a565a6331f8748df36de2ab05.png" referrerpolicy="no-referrer"></p> 
<h3>支持在 Wiki 内容编辑器中创建表格并上传图像</h3> 
<p>现在可以将图像直接上传到编辑器中，还可以插入和编辑表格，包括从流行的电子表格应用程序复制和粘贴内容，以将其他来源的表格引入 wiki。</p> 
<p><img alt src="https://oscimg.oschina.net/oscnet/up-cace0eaead988d3940e976bcb0bccfa3811.png" referrerpolicy="no-referrer"></p> 
<h3>在 Visual Studio Code 中查看合并请求的分支</h3> 
<p>现在，在使用 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fmarketplace.visualstudio.com%2Fitems%3FitemName%3DGitLab.gitlab-workflow" target="_blank">GitLab Workflow</a> for Visual Studio Code <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgitlab.com%2Fgitlab-org%2Fgitlab-vscode-extension%2F-%2Fblob%2Fmain%2FREADME.md%23merge-request-reviews" target="_blank">查看合并请求时</a>，可以右键单击 MR 标题以查看其源分支。这使得在更大的上下文中查看提议的更改、在本地测试项目以及在源分支上执行其他操作变得更加容易。</p> 
<p><img alt src="https://oscimg.oschina.net/oscnet/up-8f2b2a269fcea685e50950413a28f9238ff.png" referrerpolicy="no-referrer"></p> 
<p>更多内容查看<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fabout.gitlab.com%2Freleases%2F2021%2F07%2F22%2Fgitlab-14-1-released%2F" target="_blank">发布公告</a>。</p>
                                        </div>
                                      
</div>
            