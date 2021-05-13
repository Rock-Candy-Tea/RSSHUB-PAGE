
---
title: 'Atom 1.57.0 发布，GitHub 官方文本编辑器'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=9528'
author: 开源中国
comments: false
date: Thu, 13 May 2021 06:31:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=9528'
---

<div>   
<div class="content">
                                                                    
                                                        <p>Atom 是由 GitHub 开发的自由及开放源代码的文字与代码编辑器，支持 macOS、Windows 和 Linux 操作系统，支持 Node.js 所写的插件，并内置由 Github 提供的 Git 版本控制系统。多数的延伸包皆为开放源代码许可，并由社区建置与维护。Atom 基于使用 Chromium 和 Node.js 的跨平台应用框架 Electron（最初名为Atom Shell），并使用 CoffeeScript 和 Less 撰写。Atom 也可当作 IDE 使用。被它的开发者称为“21 世纪的高自定义性”文本编辑器（hackable text editor for the 21st Century）。自 2014 年 5 月 6 日起，Atom 的核心程序、包管理器以及 Atom 基于 Chromium 的桌面程序框架皆使用 MIT 许可协议发布。</p> 
<p>Atom 1.57.0 正式发布，本次更新内容如下：</p> 
<p>值得注意的变化：</p> 
<ul> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fatom%2Fatom%2Fpull%2F21847" target="_blank">#21847</a> - 改进对不兼容的本地模块的检测</li> 
</ul> 
<p><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fatom%2Fatom" target="_blank"><strong>Atom Core</strong></a><strong>:</strong></p> 
<ul> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fatom%2Fatom%2Fpull%2F22019" target="_blank">atom/atom#22019 -</a> 修复依赖性 Bump 脚本失败的问题</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fatom%2Fatom%2Fpull%2F21927" target="_blank">atom/atom#21927 -</a> 修复：直接要求 .node 文件以检测不兼容的本地模块</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fatom%2Fatom%2Fpull%2F22046" target="_blank">atom/atom#22046 -</a> 修复上下文菜单不工作的问题</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fatom%2Fatom%2Fpull%2F22050" target="_blank">atom/atom#22050 -</a> 修复上下文菜单右键不起作用的问题</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fatom%2Fatom%2Fpull%2F22106" target="_blank">atom/atom#22106 -</a> 将 y18n 从 3.2.1 升级到 3.2.2</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fatom%2Fatom%2Fpull%2F22061" target="_blank">atom/atom#22061 -</a> focus-trap 升级至 6.3.0</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fatom%2Fatom%2Fpull%2F22060" target="_blank">atom/atom#22060 -</a> chai 升级至 4.3.4</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fatom%2Fatom%2Fpull%2F22063" target="_blank">atom/atom#22063 -</a> git-utils 升级至 5.7.1</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fatom%2Fatom%2Fpull%2F22068" target="_blank">atom/atom#22068 -</a> normalize-package-data 升级至 3.0.2</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fatom%2Fatom%2Fpull%2F22152" target="_blank">atom/atom#22152 -</a> settings-view 升级至 0.261.8</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fatom%2Fatom%2Fpull%2F22159" target="_blank">atom/atom#22159 -</a> tree-view 升级至 0.228.3</li> 
</ul> 
<p>setting-view:</p> 
<ul> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fatom%2Fsettings-view%2Fpull%2F1176" target="_blank">atom/settings-view#1176 -</a> 修复：更新异步依赖性</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fatom%2Fsettings-view%2Fpull%2F1182" target="_blank">atom/settings-view#1182 -</a> 捕获 README 文件未找到的错误</li> 
</ul> 
<p><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fatom%2Ftree-view" target="_blank"><strong>tree-view</strong></a><strong>:</strong></p> 
<ul> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fatom%2Ftree-view%2Fpull%2F1377" target="_blank">atom/tree-view#1377 -</a> 将 fs.realpathSync 包在 try-catch 中</li> 
</ul> 
<p>更多详情可查看：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fatom%2Fatom%2Freleases%2Ftag%2Fv1.57.0" target="_blank">https://github.com/atom/atom/releases/tag/v1.57.0</a></p>
                                        </div>
                                      
</div>
            