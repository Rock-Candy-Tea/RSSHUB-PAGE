
---
title: 'Atom 1.60 发布，GitHub 官方文本编辑器'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=9129'
author: 开源中国
comments: false
date: Wed, 09 Mar 2022 07:26:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=9129'
---

<div>   
<div class="content">
                                                                                            <p>Atom 是由 GitHub 开发的开源文本编辑器，支持 macOS、Windows 和 Linux 操作系统，支持 Node.js 所写的插件，并内置由 Github 提供的 Git 版本控制系统。</p> 
<p>Atom 基于使用 Chromium 和 Node.js 的跨平台应用框架 Electron（最初名为 Atom Shell），自 2014 年 5 月 6 日起，Atom 的核心程序、包管理器以及 Atom 桌面程序框架皆使用 MIT 许可协议发布。</p> 
<p>Atom 1.60 正式发布，本次更新内容如下：</p> 
<h3>重要变化</h3> 
<ul> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fatom%2Ftabs%2Fpull%2F531" target="_blank">atom/tabs#531</a> - 在鼠标任何点击下都可以激活窗格，而不仅仅是左键点击</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fatom%2Fatom%2Fpull%2F13414" target="_blank">#13414</a> - 为 Cinnamon 桌面环境添加上下文菜单（Linux）</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fatom%2Fatom%2Fpull%2F19016" target="_blank">#19016</a> - 允许在复制和粘贴时转换行尾</li> 
</ul> 
<h3>Atom Core</h3> 
<ul> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fatom%2Fatom%2Fpull%2F22769" target="_blank">atom/atom#22769 -</a> 在 TestPanelContainerItemElement 上使用自定义元素</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fatom%2Fatom%2Fpull%2F22578" target="_blank">atom/atom#22578 -</a> 在 async isValidGitDirectory 中加入 await</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fatom%2Fatom%2Fpull%2F22781" target="_blank">atom/atom#22781 -</a> 删除冗余的 await</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fatom%2Fatom%2Fpull%2F22780" target="_blank">atom/atom#22780 -</a> 在窗格容器元素上使用自定义元素</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fatom%2Fatom%2Fpull%2F22800" target="_blank">atom/atom#22800 -</a> 更新 tree-view 软件包至 v0.229.0</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fatom%2Fatom%2Fpull%2F22814" target="_blank">atom/atom#22814 -</a> 更新 notifications 至 v0.72.1</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fatom%2Fatom%2Fpull%2F22840" target="_blank">atom/atom#22840 -</a> 将 path-parse 从 1.0.6 升级到 1.0.7</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fatom%2Fatom%2Fpull%2F17107" target="_blank">atom/atom#17107 -</a> 将参数转换为绝对路径</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fatom%2Fatom%2Fpull%2F23001" target="_blank">atom/atom#23001 -</a> bootstrap: 在系统需求检查器中更新 Node 的需求为 10.12+。</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fatom%2Fatom%2Fpull%2F22979" target="_blank">atom/atom#22979 -</a> bootstrap: 使用传统兼容的 <code>catch</code> 语法（支持旧版 Node）。</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fatom%2Fatom%2Fpull%2F23031" target="_blank">atom/atom#23031 -</a> 记住最后打开的状态</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fatom%2Fatom%2Fpull%2F23132" target="_blank">atom/atom#23132 -</a> 从 <code>crashed</code> 改为 <code>render-process-gone</code></li> 
 <li>……</li> 
</ul> 
<h3>notifications</h3> 
<ul> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fatom%2Fnotifications%2Fpull%2F204" target="_blank">atom/notifications#204 -</a> 迁移至 Github Actions</li> 
</ul> 
<h3>tree-view</h3> 
<ul> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fatom%2Ftree-view%2Fpull%2F1389" target="_blank">atom/tree-view#1389 -</a> 实现启动时隐藏树形面板的选项</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fatom%2Ftree-view%2Fpull%2F1392" target="_blank">atom/tree-view#1392 -</a> 将元素附加到 jasmine DOM 上</li> 
</ul> 
<h3>language-css</h3> 
<ul> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fatom%2Flanguage-css%2Fpull%2F169" target="_blank">atom/language-css#169 -</a> 添加通用系统字体系列</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fatom%2Flanguage-css%2Fpull%2F129" target="_blank">atom/language-css#129 -</a> 支持媒体查询 "hover”</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fatom%2Flanguage-css%2Fpull%2F144" target="_blank">atom/language-css#144 -</a> 增加对 display: flow-root 的支持</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fatom%2Flanguage-css%2Fpull%2F151" target="_blank">atom/language-css#151 -</a> 添加缺失的 scroll-snap-type 值</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fatom%2Flanguage-css%2Fpull%2F143" target="_blank">atom/language-css#143 -</a> 增加 justify-self 和 justify-items 网格属性</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fatom%2Flanguage-css%2Fpull%2F182" target="_blank">atom/language-css#182 -</a> 在 CSS 语法中加入 @-ms-viewport 和 @-o-viewport</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fatom%2Flanguage-css%2Fpull%2F173" target="_blank">atom/language-css#173 -</a> 更新 CSS 属性列表</li> 
 <li>……</li> 
</ul> 
<p>更多详情可查看：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fatom%2Fatom%2Freleases%2Ftag%2Fv1.60.0" target="_blank">https://github.com/atom/atom/releases/tag/v1.60.0</a></p>
                                        </div>
                                      
</div>
            