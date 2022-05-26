
---
title: 'GitLab 15 正式发布'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://oscimg.oschina.net/oscnet/up-e14005d2bdf226145b87ff814b18825507a.png'
author: 开源中国
comments: false
date: Thu, 26 May 2022 07:22:00 GMT
thumbnail: 'https://oscimg.oschina.net/oscnet/up-e14005d2bdf226145b87ff814b18825507a.png'
---

<div>   
<div class="content">
                                                                    
                                                        <p><span style="color:#000000">GitLab 15.0 现已正式发布，其中包括了所有层级的 Container Scanning、Internal notes、与外部组织和联系人的更好链接等内容。主要改进如下：</span></p> 
<p><span style="color:#000000"><strong>在 WYSIWYG 编辑器中编辑 code blocks、links 和 media inline</strong></span></p> 
<p><span style="color:#000000">GitLab 15.0 包含了加快用户在 wiki 的 WYSIWYG Markdown 编辑器中的工作流程的改进。</span></p> 
<p><span style="color:#000000">首先，将不再有无样式的单色代码块。用户可以在代码块上方的下拉列表中从 100 多种语言中进行选择，以便 CSS、YAML 和 Python 代码彼此分离，并具有准确的语法高亮显示。</span></p> 
<p><span style="color:#000000">在 WYSIWYG 编辑器中编辑链接和图像也变得更加容易。新的弹出菜单在用户选择链接或附加图像时出现。当你选择链接或附加图像时会出现一个新的弹出菜单。从菜单中，你可以快速编辑链接的目标 URL 或描述，将链接或图像复制到剪贴板，甚至从页面中删除链接或图像。</span></p> 
<p><span style="color:#000000"><img alt height="290" src="https://oscimg.oschina.net/oscnet/up-e14005d2bdf226145b87ff814b18825507a.png" width="500" referrerpolicy="no-referrer"></span></p> 
<p><span style="color:#000000"><strong>高级搜索与 OpenSearch 兼容</strong></span></p> 
<p><span style="color:#000000">OpenSearch 是一个开源的 Elasticsearch 分支。在 GitLab 15.0 之前，高级搜索与 OpenSearch 不兼容。如果你使用 AWS 托管服务，则必须使用旧版本的 Elasticsearch；现在则可以充分利用 OpenSearch 进行高级搜索。</span></p> 
<p><span style="color:#000000"><img alt height="309" src="https://oscimg.oschina.net/oscnet/up-8b68b63c9072e1d3ca573f789d5297952b3.png" width="500" referrerpolicy="no-referrer"></span></p> 
<p><span style="color:#000000"><strong>使用自动迭代节奏计划和安排问题</strong></span></p> 
<p><span style="color:#000000">增加了一个小组以迭代节奏管理多组并发迭代的能力，这将允许每个团队在其迭代节奏中控制每次迭代的开始日期和持续时间；迭代的日常管理现在也更加高效。</span></p> 
<p><span style="color:#000000">现在还可以将问题板或问题列表限定为迭代。组中的所有现有迭代都将转换为迭代节奏，而不会更改基础迭代数据。此外，为了更好地支持迭代的未来增强功能（例如迭代速度和波动性以及容量规划），开发团队已弃用手动创建和删除单个迭代的功能，并将在 16.0 中删除此功能。</span></p> 
<p><span style="color:#000000"><img alt height="266" src="https://oscimg.oschina.net/oscnet/up-87c9cbc1865031633cb79137f26e5d36f0d.png" width="500" referrerpolicy="no-referrer"></span></p> 
<p><span style="color:#000000"><strong>Internal notes</strong></span></p> 
<p><span style="color:#000000">Internal notes 功能使团队能够编辑只对某些用户可见的内部或客户数据的讨论，同时保持问题的核心细节公开。只有问题作者、受让人以及至少具有报告者角色的组或项目成员才能看到 issues 或 epics 中的 Internal notes。</span></p> 
<p><span style="color:#000000"><img alt height="258" src="https://oscimg.oschina.net/oscnet/up-f99e4feaf3a506ee23467101b06ac685c15.png" width="500" referrerpolicy="no-referrer"></span></p> 
<p><span style="color:#000000"><strong>将外部组织和联系人链接到问题</strong></span></p> 
<p><span style="color:#000000">GitLab 15.0 引入了第一个 MVC，用于管理和结算 GitLab的 外部客户。借助客户关系管理 (CRM) 功能，你可以：</span></p> 
<ul> 
 <li><span style="color:#000000">创建组织和联系人。</span></li> 
 <li><span style="color:#000000">为组织设置默认账单费率。</span></li> 
 <li><span style="color:#000000">将联系人添加到组织。</span></li> 
 <li><span style="color:#000000">通过<code>/add_contacts</code>快速操作将联系人链接到问题。</span></li> 
 <li><span style="color:#000000">查看与给定联系人或属于组织的所有联系人相关的问题。</span></li> 
</ul> 
<p><span style="color:#000000">客户关系功能在默认情况下是不启用的，只能从最高级别的组中进行管理。</span></p> 
<p><span style="color:#000000"><strong><span style="background-color:#ffffff">Container Scanning 适用于所有层</span></strong></span></p> 
<p><span style="color:#000000">Container Scanning 可帮助开发人员轻松找到安装在其容器映像中的依赖项中的已知安全漏洞。GitLab 15.0 在每个 GitLab 层中都提供了基本的 Container Scanning 功能。</span></p> 
<p><span style="color:#000000"><strong><span style="background-color:#ffffff">在管道配置中使用嵌套 CI/CD 变量和环境</span></strong></span></p> 
<p><span style="color:#000000"><span style="background-color:#ffffff">从 GitLab 15.0 开始，你可以在其他变量中嵌套变量，并让它们都以你期望的方式扩展；</span><span style="background-color:#ffffff">从而增加动态环境的灵活性。 </span></span></p> 
<p><span style="color:#000000"><span style="background-color:#ffffff"><img alt height="344" src="https://oscimg.oschina.net/oscnet/up-97cfa4bca499a7aacca63e54f8f0b3a0f31.png" width="500" referrerpolicy="no-referrer"></span></span></p> 
<p><span style="color:#000000"><span style="background-color:#ffffff">详情可<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fabout.gitlab.com%2Freleases%2F2022%2F05%2F22%2Fgitlab-15-0-released%2F" target="_blank">查看官方公告</a>。</span></span></p>
                                        </div>
                                      
</div>
            