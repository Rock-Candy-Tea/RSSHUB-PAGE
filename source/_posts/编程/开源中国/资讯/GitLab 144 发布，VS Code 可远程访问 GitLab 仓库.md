
---
title: 'GitLab 14.4 发布，VS Code 可远程访问 GitLab 仓库'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://oscimg.oschina.net/oscnet/up-ea53d9bd52f8f8bff1b5a26f4ef44ca57d9.png'
author: 开源中国
comments: false
date: Sun, 31 Oct 2021 08:44:00 GMT
thumbnail: 'https://oscimg.oschina.net/oscnet/up-ea53d9bd52f8f8bff1b5a26f4ef44ca57d9.png'
---

<div>   
<div class="content">
                                                                                            <p>GitLab 14.4 月度更新已于上周发布，主要更新内容包括：新增定时 DAST 扫描、不使用 Sentry 实例的情况下集成错误跟踪、Visual Studio Code 支持远程访问 GitLab 仓库和 DevOps Adoption 趋势图等。</p> 
<p><img alt src="https://oscimg.oschina.net/oscnet/up-ea53d9bd52f8f8bff1b5a26f4ef44ca57d9.png" referrerpolicy="no-referrer"></p> 
<h3>VS Code 远程访问 GitLab 仓库</h3> 
<p>在编辑器中工作时，可能需要参考另一个项目或上游仓库来获取更多信息。如果没有在本地克隆该项目，则需要离开编辑器并在 GitLab Web 界面浏览项目，或者找到并克隆该项目以便在编辑器中进行浏览。然而这两个操作都会破坏当前的上下文，引入延迟，并且将开发者带到一个不太熟悉的界面来处理代码。</p> 
<p>GitLab Workflow 3.33.0 提供了打开远程仓库的选项。打开命令面板，使用<code>GitLab: Open Remote Repository</code>命令查找并打开一个项目。</p> 
<p>此功能让开发者可以在熟悉的 VS Code 环境中浏览项目的只读版本。然后快速找到要查找的信息、比较功能的实现或复制需要的代码片段。</p> 
<p><img src="https://static.oschina.net/uploads/space/2021/1031/083447_fMRs_2720166.png" referrerpolicy="no-referrer"></p> 
<h3><span style="background-color:#ffffff; color:#222222">DevOps Adoption</span></h3> 
<p>GitLab 14.4 为群组级别的<span style="background-color:#ffffff; color:#222222"><span> </span>DevOps Adoption</span> 增加了新图表，可了解随时间变化的趋势。</p> 
<p><img alt src="https://oscimg.oschina.net/oscnet/up-788f6c9b9600f8f5d96156d2a11f1fc40c6.png" referrerpolicy="no-referrer"></p> 
<h3>在 GitLab 内部集成错误跟踪功能（不使用 Sentry 实例）</h3> 
<p>在 GitLab 14.4 之前，可通过提供一个 Sentry 后端（自行部署或在他们的云服务中使用）的端点来与 Sentry 错误跟踪集成。而在 Gitlab 14.4 中，现在可以访问内置于 GitLab 实例的兼容 Sentry 的后端。此功能让开发者可以快速检测应用程序，使错误直接显示在 GitLab 中，而不需要一个单独的 Sentry 实例。</p> 
<p><img alt src="https://oscimg.oschina.net/oscnet/up-711ee2e79fdff3364494b4671797b838da4.png" referrerpolicy="no-referrer"></p> 
<p><span style="background-color:#ffffff; color:#333333">更多内容查看</span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fabout.gitlab.com%2Freleases%2F2021%2F10%2F22%2Fgitlab-14-4-released%2F" target="_blank">发布公告</a><span style="background-color:#ffffff; color:#333333">。</span></p>
                                        </div>
                                      
</div>
            