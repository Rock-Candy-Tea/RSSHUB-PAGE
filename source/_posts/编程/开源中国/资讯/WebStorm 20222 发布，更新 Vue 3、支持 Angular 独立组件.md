
---
title: 'WebStorm 2022.2 发布，更新 Vue 3、支持 Angular 独立组件'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://static.oschina.net/uploads/space/2022/0726/071929_I2fz_4937141.png'
author: 开源中国
comments: false
date: Tue, 26 Jul 2022 07:20:00 GMT
thumbnail: 'https://static.oschina.net/uploads/space/2022/0726/071929_I2fz_4937141.png'
---

<div>   
<div class="content">
                                                                                            <p>WebStorm 2022.2，即今年的第二个更新已经发布了。这次更新的新功能使 WebStorm 变得更好，包括对 Angular 独立组件的支持，对 Vue 3 的更新，对 TypeScript 4.7 的支持，内置远程开发，以及对编辑器的大量改进。</p> 
<p><img alt height="328" src="https://static.oschina.net/uploads/space/2022/0726/071929_I2fz_4937141.png" width="700" referrerpolicy="no-referrer"></p> 
<h3><strong>对 Angular 独立组件的支持</strong></h3> 
<p>Jetbrains 一直在积极致力于为 WebStorm 2022.2 带来对 Angular 14 的支持。在这个版本中，所做的最重要的补充是对 Angular 独立组件的支持。WebStorm 现在可以正确地识别标记为 <code>standalone: true</code> 的组件、指令和管道。</p> 
<h3><strong>针对 Vue 3 的更新</strong></h3> 
<p>WebStorm 2022.2 对 Vue 3 提供了更好的支持。例如，它现在可以理解 <code>v-if/else</code>指令中的类型收窄。此外还支持 Vue 团队推荐的状态管理解决方案 Pinia，它可以作为全局存储使用。</p> 
<h3>支持 <strong>TypeScript 4.7</strong></h3> 
<p>WebStorm 2022.2 捆绑了 TypeScript 4.7，支持新的语言特性，如 Node.js 中的 <code>moduleSuffixes</code> 和 ESM。如果在你的 tsconfig.json 文件中 <code>module</code> 被设置为 <code>node16</code> 或 <code>nodenext</code>，它将自动在导入语句中插入 .js 扩展。此外，WebStorm 支持 package.json 文件中的 <code>typesVersions</code> 字段。</p> 
<h3><strong>对 AngularJS 的支持结束</strong></h3> 
<p>由于 AngularJS 现在已经达到了生命周期结束。WebStorm 2022.2 将不再积极维护它。AngularJS 仍然可以在其他版本的 WebStorm 和 JetBrains IDE 中使用。</p> 
<h3><strong>内置的远程开发工作流程</strong></h3> 
<p>WebStorm 2022.2 在去年引入了对远程开发工作流的支持，如今可以在 Beta 标签下开箱即用。你可以连接到一个运行着 IDE 的远程机器上，并在那里的项目上工作，就像它位于你的本地机器上一样。</p> 
<h3>改进 <strong>Docker</strong></h3> 
<p>在 WebStorm 2022.2 中，你现在可以使用新的 <em>Copy Docker Image</em> 将镜像从一个 Docker 守护进程复制到另一个。它将镜像保存到一个文件中，然后将其推送到选定的连接。新版本还加入了一个设置，在你重启 WebStorm 时自动连接到到 Docker。</p> 
<h3><strong>HTTP 客户端的新功能</strong></h3> 
<p>WebStorm 2022.2 支持 WebSocket 连接，这使得你可以创建请求，以及发送和接收消息。新版本也已经在 HTTP 客户端中引入了对 GraphQL 请求的支持。WebStorm 现在可以通过 HTTP 和 WebSocket 协议发送 GraphQL 查询。</p> 
<h3><strong>JetBrains Space 集成</strong></h3> 
<p>WebStorm 现在内置了对 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.jetbrains.com%2Fspace%2F" target="_blank">JetBrains Space</a> 的集成。你可以将 IDE 连接到 Space 中的组织，以查看和克隆项目仓库，编写使用 Space API 的复杂脚本，并审查团队成员的代码。</p> 
<h3><strong>缩放时的字体大小指示</strong></h3> 
<p>当你在编辑器中放大或缩小你的代码时，现在可以看到一个指示器来显示当前的字体大小，并可以选择将其恢复到默认大小。</p> 
<h3><strong>全局改变字体大小的捷径</strong>。</h3> 
<p>新版本引入了用键盘快捷键来改变整个编辑器的字体大小的功能。你现在可以按 ⌃⇧. / Alt+Shift+. 来增加字体大小。按 ⌃⇧, / Alt+Shift+, 来减小字体。</p> 
<h3><strong>更快地访问代码补全设置</strong></h3> 
<p>只要你需要改变自动补全的方式，你现在就可以从编辑器中的代码补全弹出窗口跳到你的代码补全设置。</p> 
<h3><strong>在 Markdown 文档中生成一个目录</strong></h3> 
<p>在这个版本中，增加了一个新的生成目录的操作，这将使为你的 Markdown 文件创建一个目录变得更加简单明了。你可以使用 ⌘N（在 Windows 和 Linux 上为 Alt+Insert），这将带来 <code>Insert...</code> 弹出窗口。然后你可以选择 Table Of Contents，它将自动为你生成目录。</p> 
<p>更多详情可查看：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fblog.jetbrains.com%2Fwebstorm%2F2022%2F07%2Fwebstorm-2022-2%2F" target="_blank">https://blog.jetbrains.com/webstorm/2022/07/webstorm-2022-2/</a></p> 
<p> </p>
                                        </div>
                                      
</div>
            