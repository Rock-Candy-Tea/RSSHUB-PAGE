
---
title: 'Atom 1.56.0 发布，GitHub 官方文本编辑器'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=211'
author: 开源中国
comments: false
date: Thu, 15 Apr 2021 07:21:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=211'
---

<div>   
<div class="content">
                                                                    
                                                        <p>Atom 是由 GitHub 开发的自由及开放源代码的文字与代码编辑器，支持 macOS、Windows 和 Linux 操作系统，支持 Node.js 所写的插件，并内置由 Github 提供的 Git 版本控制系统。多数的延伸包皆为开放源代码许可，并由社区建置与维护。Atom 基于使用 Chromium 和 Node.js 的跨平台应用框架 Electron（最初名为Atom Shell），并使用 CoffeeScript 和 Less 撰写。Atom 也可当作 IDE 使用。被它的开发者称为“21 世纪的高自定义性”文本编辑器（hackable text editor for the 21st Century）。自 2014 年 5 月 6 日起，Atom 的核心程序、包管理器以及 Atom 基于 Chromium 的桌面程序框架皆使用 MIT 许可协议发布。</p> 
<p>Atom 1.56.0 正式发布，本次更新内容如下：</p> 
<p>显著变化：</p> 
<ul> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fatom%2Fatom%2Fpull%2F21847" target="_blank">#21847</a> - 修复 macOS 上所有窗口关闭后退出的错误行为；</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fatom%2Fatom%2Fpull%2F21852" target="_blank">#21852</a> - 改进 Java 语法高亮显示；</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fatom%2Fatom%2Fpull%2F21847" target="_blank">#21847</a> - 增加禁用鼠标中键粘贴的设置；</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fatom%2Fatom%2Fpull%2F21777" target="_blank">#21777</a> - Electron 升级；</li> 
</ul> 
<p><strong>Atom Core</strong></p> 
<ul> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fatom%2Fatom%2Fpull%2F21753" target="_blank">atom/atom#21753 -</a> 修正树状结构注入时"empty"语言的处理方式；</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fatom%2Fatom%2Fpull%2F21715" target="_blank">atom/atom#21715 -</a> 检查 testRunner 是否为 es 模块；</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fatom%2Fatom%2Fpull%2F21848" target="_blank">atom/atom#21848 -</a> 添加授权；</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fatom%2Fatom%2Fpull%2F21928" target="_blank">atom/atom#21928 -</a> 修复了依赖性 bump 脚本；</li> 
</ul> 
<p><strong>GitHub</strong></p> 
<ul> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fatom%2Fgithub%2Fpull%2F2459" target="_blank">atom/github#2459 -</a> 使用 action-setup-atom 来实现；</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fatom%2Fgithub%2Fpull%2F2621" target="_blank">atom/github#2621 -</a> package.json：将@babel/core 固定为 7.12.10 以下；</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fatom%2Fgithub%2Fpull%2F2625" target="_blank">atom/github#2625 -</a> 更新 shell.openExternal 为 Promise，因为 Atom 上的 Electron 更新；</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fatom%2Fgithub%2Fpull%2F2626" target="_blank">atom/github#2626 -</a> 更新 Electron API 中一些方法的 Promise api；</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fatom%2Fgithub%2Fpull%2F2631" target="_blank">atom/github#2631 -</a> 修复 GitHub 在 Atom electron 9.4.1 升级失败的测试；</li> 
</ul> 
<p>拼写检查</p> 
<ul> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fatom%2Fspell-check%2Fpull%2F357" target="_blank">atom/spell-check#357 -</a> 在配置中加入 enableDebug；</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fatom%2Fspell-check%2Fpull%2F359" target="_blank">atom/spell-check#359 -</a> 修复了无法加载包的问题；</li> 
</ul> 
<p>更多详情可查看：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fatom%2Fatom%2Freleases%2Ftag%2Fv1.56.0" target="_blank">https://github.com/atom/atom/releases/tag/v1.56.0</a></p>
                                        </div>
                                      
</div>
            