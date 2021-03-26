
---
title: 'TeamCity 2021.1 EAP2 发布，持续集成工具'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://static.oschina.net/uploads/space/2021/0326/071210_kFfC_4937141.png'
author: 开源中国
comments: false
date: Fri, 26 Mar 2021 07:24:00 GMT
thumbnail: 'https://static.oschina.net/uploads/space/2021/0326/071210_kFfC_4937141.png'
---

<div>   
<div class="content">
                                                                                            <p>TeamCity 2021.1 EAP2 发布了。TeamCity 是一款功能强大的持续集成工具，覆盖服务器端和客户端。它提供一系列特性可以让团队快速实现持续集成：IDE 工具集成、各种消息通知、各种报表、项目的管理、分布式编译等等。该版本是  2021.1 的第二个早期访问版，带来了40多项改进和修复。</p> 
<p><img alt height="394" src="https://static.oschina.net/uploads/space/2021/0326/071210_kFfC_4937141.png" width="700" referrerpolicy="no-referrer"></p> 
<h4>新的 Kotlin 脚本构建运行器</h4> 
<p>Kotlin by JetBrains 是一种被广泛采用的简洁的编程语言，因此该 EAP 引入了一个新的构建运行器 Kotlin Script。通过输入一个 Kotlin 脚本或提供一个路径，TeamCity 将在构建过程中编译并执行它。</p> 
<p><img alt height="534" src="https://static.oschina.net/uploads/space/2021/0326/071235_AXbq_4937141.png" width="700" referrerpolicy="no-referrer"></p> 
<h4>在运行时将节点从辅助节点切换到主节点</h4> 
<p>现在在使用多节点 TeamCity 设置时，支持在运行时将一个节点的角色从次要节点切换到主节点。默认情况下，"TeamCity 主节点" 为当前主服务器，但如果这个服务器变得不可用，用户可以将其分配给管理中的任何辅助服务器。即使先前的主服务器重启，它也将成为辅助接点。</p> 
<p><img alt height="547" src="https://static.oschina.net/uploads/space/2021/0326/071259_7TIz_4937141.png" width="700" referrerpolicy="no-referrer"></p> 
<h4>可自定义将大型构建工件的分段上传到 Amazon S3</h4> 
<p>用户将构建工件存储在 Amazon S3 中时，可以直接在 TeamCity UI 中配置大文件的多段上传参数。这有助于更有效地使用网络带宽，提高吞吐量。</p> 
<p><img alt height="244" src="https://static.oschina.net/uploads/space/2021/0326/071320_P2lL_4937141.png" width="700" referrerpolicy="no-referrer"></p> 
<h4>简化了 Perforce 中 post-commit 钩子的设置</h4> 
<p>TeamCity 会定期轮询 VCS 仓库，以及时检测项目代码的变化。而该版本提供了在 VCS 服务器上设置 post-commit 钩子的功能。这样一来，只要有新的变化，VCS 服务器本身就会通知 TeamCity，从而减少了轮询操作的次数，减轻了服务器的负担。</p> 
<h4>用户界面优化</h4> 
<p>该版本对用户界面进行了优化，并且引入了 UI 助手。可通过打开屏幕右上角的 "帮助 "菜单，点击 "显示提示" 来启用此功能。</p> 
<p>详情请查看<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fblog.jetbrains.com%2Fteamcity%2F2021%2F03%2Fteamcity-2021-1-eap2-is-here%2F" target="_blank">更新公告</a>。</p>
                                        </div>
                                      
</div>
            