
---
title: 'TeamCity 2021.1 EAP3 发布，持续集成工具'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://oscimg.oschina.net/oscnet/up-84115267e02c46a8bcea72abba07a3e935f.png'
author: 开源中国
comments: false
date: Thu, 29 Apr 2021 00:02:00 GMT
thumbnail: 'https://oscimg.oschina.net/oscnet/up-84115267e02c46a8bcea72abba07a3e935f.png'
---

<div>   
<div class="content">
                                                                    
                                                        <p>TeamCity 2021.1 EAP3 发布了。TeamCity 是一款功能强大的持续集成工具，覆盖服务器端和客户端。它提供一系列特性可以让团队快速实现持续集成：IDE 工具集成、各种消息通知、各种报表、项目的管理、分布式编译等等。该版本是  2021.1 的第三个早期访问版，带来了70多项改进和修复。</p> 
<p><img alt src="https://oscimg.oschina.net/oscnet/up-84115267e02c46a8bcea72abba07a3e935f.png" referrerpolicy="no-referrer"></p> 
<h4>Node.js 构建运行器</h4> 
<p>现在为 Node.js 提供了一个专门的构建运行器，支持 npm 和 yarn 命令。如果你的资源库包含package.json文件，TeamCity会自动检测使用的框架并建议添加相应的构建步骤。目前，所有的 Node.js 步骤只能在 Docker 容器内运行，这意味着这个运行器的唯一前提条件是在构建代理上安装 Docker。TeamCity 默认使用 node:lts 容器。</p> 
<h4><img alt src="https://oscimg.oschina.net/oscnet/up-b84ce03e4bcd3b37f2e9a98d9c0fe15d179.png" referrerpolicy="no-referrer"></h4> 
<h4>基于 Elastic 的新搜索模式</h4> 
<p>从这个 EAP 开始，TeamCity提供了一个基于 Elastic 的替代搜索模式，这种模式允许在用户的 Elastic 主机上存储一个全局搜索索引。在本地搜索模式下，每个节点都要花费其磁盘空间和资源来存储和维护搜索索引。而在新的模式下，所有节点都有一个单一的索引，这大大减轻了它们的索引操作，节省了它们的磁盘空间。用户可以在项目设置中的根项目层面切换到这种模式。</p> 
<p><img alt src="https://oscimg.oschina.net/oscnet/up-bcaae3246044103c3fd03b7eccc2b00d336.png" referrerpolicy="no-referrer"></p> 
<h4>只读项目设置</h4> 
<p>EAP3 引入了一个新的选项：允许通过用户界面编辑项目。它在默认情况下是启用的，这与常规行为相一致。但如果用户在项目中禁用它，这将使项目的设置在用户界面中成为只读，并阻止 TeamCity 提交到设置的存储库。</p> 
<p><img alt src="https://oscimg.oschina.net/oscnet/up-5b24fd6130d780e703cc7f95d75a8693320.png" referrerpolicy="no-referrer"></p> 
<h4>每个构建配置允许多个 VCS 触发器</h4> 
<p>现在，用户可以为一个构建配置添加一个以上的 VCS 触发器。这允许用户为所有分支的构建设置一个静默期，除了一个分支，一旦有新的修改提交，就开始构建。或者可以配置一个触发器，只在一个给定的分支的每个签入上开始构建。在下一次 EAP 更新中，VCS 触发器将更加灵活，并在其设置中支持自定义构建参数。</p> 
<h4>限制用个人补丁定制构建的权限</h4> 
<p>EAP3 创建了一个新的用户权限：用自定义补丁改变构建源代码。有了这个权限，用户现在可以完全控制谁可以给构建打补丁，或者在必要时完全限制重要项目的这个功能。在升级到 2021.1 EAP3 时，它将自动为默认的项目开发人员角色和其他具有自定义构建权限的角色启用。</p> 
<p>更多详细内容，请查看官方公告。</p>
                                        </div>
                                      
</div>
            