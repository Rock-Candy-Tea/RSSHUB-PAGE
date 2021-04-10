
---
title: 'GoLand 2021.1 稳定版发布'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://static.oschina.net/uploads/space/2021/0409/162657_V8jA_2720166.png'
author: 开源中国
comments: false
date: Sat, 10 Apr 2021 07:52:00 GMT
thumbnail: 'https://static.oschina.net/uploads/space/2021/0409/162657_V8jA_2720166.png'
---

<div>   
<div class="content">
                                                                                            <p>GoLand 2021.1 稳定版<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fblog.jetbrains.com%2Fgo%2F2021%2F04%2F08%2Fmeet-goland-2021-1%2F" target="_blank">已发布</a>，作为今年首个大版本，此次更新带来了不少变化，例如：使用 Go 1.16 新支持的功能（包括<code>//go:embed</code>）、支持通过 Docker, SSH 和 WSL 2 远程构建和运行应用程序、从 JSON 生成代码，以及优化错误处理功能。</p> 
<p><img src="https://static.oschina.net/uploads/space/2021/0409/162657_V8jA_2720166.png" referrerpolicy="no-referrer"></p> 
<h1>支持 Go 1.16</h1> 
<p>从 Go 1.16 开始，开发者可以在构建时将文件和目录嵌入 Go 二进制文件。嵌入适用的几类变量：<code>string</code>、<code>[]byte</code> 和 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Ftip.golang.org%2Fpkg%2Fembed%2F%23FS" target="_blank">embed.FS</a>。您需要在软件包的顶层声明这些变量。 最后，您需要添加 <code>//go:embed</code> 指令使嵌入生效。</p> 
<p><img src="https://static.oschina.net/uploads/space/2021/0410/070300_dBOZ_2720166.png" referrerpolicy="no-referrer"></p> 
<p>GoLand 提供了代码高亮显示、从 embed 指令内的引用到项目中的文件和文件夹的导航、<em>Rename</em> 重构、<em>Find Usages</em>、代码补全和一些代码检查。 例如，如果您试图将文件嵌入类型错误的变量，GoLand 会发出通知。</p> 
<h1>改进错误处理</h1> 
<p>从此版本开始， <em>Unhandled Error</em> 代码检查功能已获得一系列快速修复：</p> 
<ul> 
 <li>Handle error 快速修复将调用结果分配给变量并生成<code>if error not nil</code>检查</li> 
 <li>Wrap error handling in a closure 快速修复可用于<code>defer</code>和<code>go</code>语句，生成的代码与 Handle error 类似，但会将所有内容封装在闭包中</li> 
 <li>Ignore explicitly 应用范围得到扩展，涵盖了<code>defer</code>和<code>go</code>语句。 快速修复将调用结果分配给空白变量，并将所有内容封装在闭包中</li> 
</ul> 
<p><img src="https://static.oschina.net/uploads/space/2021/0410/070237_FDJY_2720166.gif" referrerpolicy="no-referrer"></p> 
<h1>改进 Run/Debug Configurations</h1> 
<p>新版本以多种方式改进了 Run/Debug Configuration 对话框：</p> 
<ul> 
 <li>要添加所有必要的构建选项，点击 Modify options；要添加运行选项，点击 Modify。 IDE 现在会验证每个选项以确保其兼容</li> 
 <li>对于 Docker-compose，支持所有现有的选项，包括声明环境变量文件 (.env) 的选项</li> 
 <li>对于 Dockerfile，不必记住所有的运行命令，因为代码补全可在 Run Options 字段中运行</li> 
 <li>对于 Docker 镜像，可以使用代码补全在 Image ID 或 name 字段中输入映像的名称</li> 
</ul> 
<p><img src="https://static.oschina.net/uploads/space/2021/0410/070507_T04Y_2720166.png" referrerpolicy="no-referrer"></p> 
<h3>在 Windows 上通过“开始”菜单快速访问最近的项目</h3> 
<p>现在可以在 Windows 中右键点击任务栏或开始菜单上的 GoLand 图标访问最近打开的项目。</p> 
<p><img src="https://static.oschina.net/uploads/space/2021/0410/070628_Oa4G_2720166.png" referrerpolicy="no-referrer"></p> 
<p><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.jetbrains.com%2Fgo%2Fwhatsnew%2F" target="_blank">更多新特性介绍点此查看</a>。</p> 
<p>下载地址：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.jetbrains.com%2Fgo%2Fdownload%2F" target="_blank">https://www.jetbrains.com/go/download/</a></p>
                                        </div>
                                      
</div>
            