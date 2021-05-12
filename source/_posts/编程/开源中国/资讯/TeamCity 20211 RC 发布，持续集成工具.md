
---
title: 'TeamCity 2021.1 RC 发布，持续集成工具'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://oscimg.oschina.net/oscnet/up-b490120f92ede9fbef77e77e9460b9e1a1d.png'
author: 开源中国
comments: false
date: Wed, 12 May 2021 06:41:00 GMT
thumbnail: 'https://oscimg.oschina.net/oscnet/up-b490120f92ede9fbef77e77e9460b9e1a1d.png'
---

<div>   
<div class="content">
                                                                    
                                                        <p>TeamCity 2021.1 RC 现已发布，本 RC 是 TeamCity Early Access Program 2021.1 的最后阶段，用户已经可以在早期访问模式下试用该版本的最新功能。以下是主要更新内容。</p> 
<p><img alt src="https://oscimg.oschina.net/oscnet/up-b490120f92ede9fbef77e77e9460b9e1a1d.png" referrerpolicy="no-referrer"></p> 
<h4>自定义自动触发的构建</h4> 
<p>构建触发器现在支持自定义参数。在构建触发器的设置中，用户可以找到新的构建定制标签。与 "运行自定义构建 "对话框类似，它可以让用户覆盖构建参数的值，并定义是否应在构建前清理检查目录。</p> 
<h4><img alt src="https://oscimg.oschina.net/oscnet/up-bae60275d41cc8d49858c9e8719e31628db.png" referrerpolicy="no-referrer"></h4> 
<h4>清理 Perforce 服务器上的流工作空间</h4> 
<p>为了更好地地收集和处理作为功能分支的 Perforce 流中的变化，TeamCity 需要在 Perforce 服务器上创建和维护专用工作空间。随着时间的推移，这些工作空间可能会在 Perforce 服务器的机器上消耗大量的资源。此外，用户无法关闭一个与工作空间相关的任务流。</p> 
<p>这两个问题都可以通过清理不再需要的工作空间来解决。以前，任何手动清理都需要 Perforce 服务器管理员的参与。现在项目开发者可以在 TeamCity 用户界面上完成这项工作。</p> 
<p><img alt src="https://oscimg.oschina.net/oscnet/up-dd30c4a66b1ca523f65d5b02bc841162e82.png" referrerpolicy="no-referrer"></p> 
<p>在每次清理过程中，TeamCity 会检测并删除超过 7 天不活动的工作空间。用户也可以通过点击连接设置中的删除工作空间来随时删除它们。工作空间只在服务器上被删除，而不会在构建代理上。此外，该功能也支持删除与特定流相关的工作空间。</p> 
<p><img alt src="https://oscimg.oschina.net/oscnet/up-b686c6e8ac7906a8c7ad795c29a79d6ed05.png" referrerpolicy="no-referrer"></p> 
<h4>Sakura UI：在 “构建概览” 中以树模式显示测试</h4> 
<p>现在，Sakura UI 支持在构建概览中展示测试树视图，并且，用户可以根据当前的任务，随时在树形和扁平结构之间切换。</p> 
<p><img alt src="https://oscimg.oschina.net/oscnet/up-6a9c2e4eb100b9f1b835e54a49d9fc683ce.png" referrerpolicy="no-referrer"></p> 
<p>更多详细内容，请查看<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fblog.jetbrains.com%2Fteamcity%2F2021%2F05%2Fteamcity-2021-1-rc-is-here%2F" target="_blank">更新公告</a>。</p>
                                        </div>
                                      
</div>
            