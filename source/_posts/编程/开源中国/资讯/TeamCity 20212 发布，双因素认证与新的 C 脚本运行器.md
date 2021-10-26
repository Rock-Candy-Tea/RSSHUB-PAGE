
---
title: 'TeamCity 2021.2 发布，双因素认证与新的 C# 脚本运行器'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://oscimg.oschina.net/oscnet/up-91d1462a67615cdd4cf819f7b887d7104c7.png'
author: 开源中国
comments: false
date: Tue, 26 Oct 2021 04:52:00 GMT
thumbnail: 'https://oscimg.oschina.net/oscnet/up-91d1462a67615cdd4cf819f7b887d7104c7.png'
---

<div>   
<div class="content">
                                                                    
                                                        <p>TeamCity 2021.2 现已发布，该版本引入了双因素认证，进一步与 JetBrains Space 整合，并提供了新的跨平台 C# 脚本构建运行器。此外，该版本还对 Kotlin DSL 语法进行了一些改进，并对 Sakura UI 进行了多项更新。</p> 
<p><img alt height="800" src="https://oscimg.oschina.net/oscnet/up-91d1462a67615cdd4cf819f7b887d7104c7.png" width="1600" referrerpolicy="no-referrer"></p> 
<h4><span style="background-color:#ffffff; color:#182026">更加安全的方法</span></h4> 
<p><span style="background-color:#ffffff; color:#182026">CI/CD 是现代开发流程的核心要素，为了进一步加强其CI/CD服务器的安全性，TeamCity 管理员现在可以启用双因素认证，并要求用户输入额外的认证代码来登录。</span></p> 
<p><span style="background-color:#ffffff; color:#182026"><img alt height="1110" src="https://oscimg.oschina.net/oscnet/up-19e8ab01474893ce57b5fba0ff183710476.png" width="1793" referrerpolicy="no-referrer"></span></p> 
<h4><span style="background-color:#ffffff; color:#182026">进一步整合 </span>Perforce</h4> 
<p>TeamCity 2021.2 通过一系列新功能加强了 Perforce 整合，包括：</p> 
<ul> 
 <li>在变更列表上运行构建 
  <ul> 
   <li>运行自定义构建功能现在允许用户使用 Perforce 变更列表中的变更运行个人构建。用户可以在这样的变更列表上触发整个构建链，并在 TeamCity 用户界面上看到相应的文件列表。</li> 
  </ul> </li> 
 <li>Perforce Shelve 触发器 
  <ul> 
   <li>该版本增加了新的 Perforce Shelve 触发器，它可以检测新的和修改过的、描述中包含特定关键字的变更列表，并触发对它们的个人构建。</li> 
  </ul> </li> 
 <li>Perforce Helix Swarm 报告 
  <ul> 
   <li>该版本通过添加新的 Perforce Swarm 发布器扩展了提交状态发布器的构建功能。当发布者被配置后，TeamCity 会将构建的信息发送到 Perforce Helix Swarm 服务器，相应的评论会被添加到变更列表的 Swarm 评论中。</li> 
  </ul> </li> 
 <li>自动标签 
  <ul> 
   <li>VCS 的标签构建功能现在可以在 Helix 服务器中创建自动标签。这些标签作为 changelist 编号的别名。与 TeamCity 以前的版本中使用的静态标签相比，这些标签可以大大提升性能。</li> 
  </ul> </li> 
</ul> 
<h4>新的 Space 认证模块</h4> 
<p>2021.2 版本增加了新的 JetBrains Space 认证模块，允许用户使用 Space 账户登录，并且新版本的 TeamCity 还支持添加 VCS 根目录、创建项目和构建配置。</p> 
<p><img alt height="796" src="https://oscimg.oschina.net/oscnet/up-767002f8270c77e7c08dc36b32c5b997346.png" width="591" referrerpolicy="no-referrer"></p> 
<h4>为 C# 开发人员简化 CI/CD</h4> 
<p>该版本创建了新的 C# 脚本构建运行器，它提供了一种用真正的编程语言来编写构建步骤的简单方法，并且是跨平台的，可以在任何带有 Docker 的系统上运行，同时内置了对 NuGet 的支持。</p> 
<p><img alt src="https://oscimg.oschina.net/oscnet/up-ecd1b8064c2de4e04d471ca2a4c0a9dbde7.png" referrerpolicy="no-referrer"></p> 
<h2 style="margin-left:.5em; margin-right:0; text-align:start">Sakura UI</h2> 
<p>Sakura UI 可以帮助开发人员快速找到需要的东西，二 2021.2 版则增加了 Sakura 用户界面中没有的经典用户界面的两个视图：待定变更和变更细节。此外，用户名现在可以在旁边显示头像。</p> 
<p><img alt src="https://oscimg.oschina.net/oscnet/up-e68af1b080bc0f87fcdd85d5a743f3865e8.png" referrerpolicy="no-referrer"></p> 
<p>更多详细内容请查看<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fblog.jetbrains.com%2Fteamcity%2F2021%2F10%2Fteamcity-2021-2-two-factor-authentication-improved-integrations-with-perforce-products-jetbrains-space-and-azure-devops-a-new-cross-platform-c-script-runner-and-updates-to-the-sakura-ui%2F" target="_blank">官方公告</a>。</p> 
<p> </p>
                                        </div>
                                      
</div>
            