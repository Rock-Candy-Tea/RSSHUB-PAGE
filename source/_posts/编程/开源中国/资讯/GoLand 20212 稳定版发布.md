
---
title: 'GoLand 2021.2 稳定版发布'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://oscimg.oschina.net/oscnet/up-46eca466eb4a0416335e86d44286fb12618.png'
author: 开源中国
comments: false
date: Wed, 04 Aug 2021 07:06:00 GMT
thumbnail: 'https://oscimg.oschina.net/oscnet/up-46eca466eb4a0416335e86d44286fb12618.png'
---

<div>   
<div class="content">
                                                                    
                                                        <p>GoLand 2021.2 稳定版<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fblog.jetbrains.com%2Fgo%2F2021%2F07%2F29%2Fgoland-2021-2-has-been-released%2F" target="_blank">已发布</a>。</p> 
<p>GoLand 2021.2 引入了新的 <strong>Go modules </strong>功能、新的<strong>格式设置</strong>选项以及对 <strong>Go 1.17</strong> 功能的支持。此外还添加了新的快速修复，包括帮助开发者正确使用新的 <code>//go:build</code> 语法的修正。</p> 
<p>在此版本中，版本控制功能已经更新，改进包括使用 <strong>GPG 密钥签署提交</strong>的功能。对于 Web 开发者，增加了保存代码时在浏览器中自动重新加载页面的功能，并且为 MongoDB 字段和运算符提供了补全。</p> 
<p>下载地址：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.jetbrains.com%2Fzh-cn%2Fgo%2Fdownload%2F" target="_blank">https://www.jetbrains.com/zh-cn/go/download/</a></p> 
<p><img alt src="https://oscimg.oschina.net/oscnet/up-46eca466eb4a0416335e86d44286fb12618.png" referrerpolicy="no-referrer"></p> 
<h2>Go modules</h2> 
<h3>手动加载 go.mod 变更</h3> 
<p>在 GoLand 2021.2 中，开发者可以在编辑 <code>go.mod</code> 时控制 IDE 如何调用 <code>go list</code>，也可以手动加载 <code>go.mod</code> 文件变更。</p> 
<p><img alt src="https://oscimg.oschina.net/oscnet/up-d636f1ddd90e5286dae303529368a9f9fba.png" referrerpolicy="no-referrer"></p> 
<p>转到 <em>Settings | Build, Execution, Deployment | Build Tools</em>，然后选择 <em>External changes</em> 选项。当使用者在 IDE 中编辑文件时，GoLand 将自动停止调用 <code>go list</code>。</p> 
<h3>更好地支持不同的 Go 版本</h3> 
<p>如果所使用的 Go 语言版本中的功能比 go.mod 文件中指定的版本更加新，那么将会收到错误消息。此时 GoLand 会提示出问题的地方。</p> 
<p><img src="https://static.oschina.net/uploads/space/2021/0710/075519_1SJS_2720166.gif" referrerpolicy="no-referrer"></p> 
<h3>欢迎界面的默认 Go 选项</h3> 
<p>欢迎界面的 Go 选项现在是 Go modules 项目的默认选项，官方还将基于 GOPATH 的项目重命名为 Go (GOPATH)。</p> 
<p><img alt src="https://oscimg.oschina.net/oscnet/up-3effc46c2abad45f988c6757e570d75d02b.png" referrerpolicy="no-referrer"></p> 
<h2>格式化程序</h2> 
<p>此版本引入了 <em>Run gofmt on code reformat</em> 选项。 这是使 <code>gofmt</code> 在 GoLand 中更容易被发现的第一步，GoLand 具有自己的格式化程序。选中此选项后，开发者可以使用快捷键 Ctrl+Alt+L 调用两个格式化程序，<code>gofmt</code> 将在 GoLand 的格式化程序之后运行。</p> 
<p><img alt src="https://oscimg.oschina.net/oscnet/up-23766139bb1e58416db73fa0979c80be115.png" referrerpolicy="no-referrer"></p> 
<p>此选项默认启用，可在 <em>Settings | Editor | Code Style | Go</em> 中切换。</p> 
<h2>Go 1.17</h2> 
<p>在 Go 1.17 中，可以将切片转换为数组指针。GoLang 不会把这些转换标记为错误。要试用 Go 1.17 功能，请将 <em>Settings | Go</em> 中的 GOROOT 更改为“Go 1.17beta1”或“Go 1.17rc1”。</p> 
<p><img src="https://static.oschina.net/uploads/space/2021/0804/063421_rVpm_2720166.gif" referrerpolicy="no-referrer"></p> 
<h2>UI 改进</h2> 
<h3>Toolbox App 的更新通知</h3> 
<p>GoLand 会在有新版本时发出通知，并为用户提供直接从 IDE 更新到新版本的选项。要使用此功能，需要 Toolbox App 1.20.8804 或更高版本。</p> 
<p><img alt src="https://oscimg.oschina.net/oscnet/up-ae5c44529898906f0d64ac390b8c7533f61.png" referrerpolicy="no-referrer"></p> 
<h3>新的终端选项</h3> 
<p>现在可以转到 <em>Settings | Tools | Terminal</em> 将内置终端中的光标形状更改为下划线或垂直。</p> 
<p><img alt src="https://oscimg.oschina.net/oscnet/up-d8b6dcf685dd0ea5c6e9d008c56b26e0513.png" referrerpolicy="no-referrer"></p> 
<h3>新的 Change 项目图标窗口</h3> 
<p>简化了对话框，允许用户在欢迎界面上的项目列表中自定义项目图标。要上传自定义图标，只需右键点击项目并从上下文菜单中选择 <em>Choose project icon</em>。</p> 
<p><img alt src="https://oscimg.oschina.net/oscnet/up-24693544323a68d0a754e166eaefa2ce4ad.png" referrerpolicy="no-referrer"></p> 
<h2>Web 开发</h2> 
<h3>保存代码时在浏览器中重新加载页面</h3> 
<p>当开发者编辑和保存 HTML、CSS 和 JavaScript 文件时，GoLand 现已能够更新浏览器中的页面。</p> 
<p><img src="https://static.oschina.net/uploads/space/2021/0804/063920_TonR_2720166.gif" referrerpolicy="no-referrer"></p> 
<p>默认情况下，保存时重新加载页面处于开启状态。可以在 <em>Settings | Build, Execution, Deployment | Debugger | Built-in Server</em> 中切换。</p> 
<p>更多内容查看 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.jetbrains.com%2Fgo%2Fwhatsnew%2F" target="_blank">https://www.jetbrains.com/go/whatsnew/</a>。</p>
                                        </div>
                                      
</div>
            