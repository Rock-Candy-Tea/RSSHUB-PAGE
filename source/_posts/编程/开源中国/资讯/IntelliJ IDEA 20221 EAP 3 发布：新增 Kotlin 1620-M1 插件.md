
---
title: 'IntelliJ IDEA 2022.1 EAP 3 发布：新增 Kotlin 1.6.20-M1 插件'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://oscimg.oschina.net/oscnet/up-9b1784dc1fa37c39baa445d3cb057e9ab9c.gif'
author: 开源中国
comments: false
date: Sun, 20 Feb 2022 07:49:00 GMT
thumbnail: 'https://oscimg.oschina.net/oscnet/up-9b1784dc1fa37c39baa445d3cb057e9ab9c.gif'
---

<div>   
<div class="content">
                                                                                            <p style="margin-left:0px">IntelliJ IDEA 2022.1 EAP 3 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fblog.jetbrains.com%2Fidea%2F2022%2F02%2Fintellij-idea-2022-1-eap-3%2F" target="_blank">已发布</a>，第三个 EAP 版本带来了捆绑的 Kotlin 1.6.20-M1 插件、调试器的 UI 增强、Markdown 编辑器的改进等等内容，下面摘录一部分新功能作介绍：</p> 
<h3>Kotlin 1.6.20-M1 插件捆绑</h3> 
<p style="margin-left:0px"><span style="color:#27282c">IntelliJ IDEA 2022.1 的新 EAP 版本捆绑了 Kotlin 1.6.20-M1 插件，这意味着 IDE 预览版本支持最新的语言功能。 </span></p> 
<p style="margin-left:0px"><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fblog.jetbrains.com%2Fkotlin%2F2022%2F02%2Fkotlin-1-6-20-m1-released%2F" target="_blank">第一个 Kotlin 1.6.20 预览版</a>引入了许多值得注意的更新，例如对并行编译的支持、上下文接收器的原型、所有 Kotlin 目标之间更好的代码共享等等</p> 
<h3>调试器 UI 改进</h3> 
<ul> 
 <li> <h3>重置<span style="background-color:#ffffff; color:#2e3033">框架<em>（</em></span><em>Reset Frame</em><span style="background-color:#ffffff; color:#2e3033"><em>）</em>功能</span></h3> </li> 
</ul> 
<p style="margin-left:0px">在 <em>Frames </em>视图中，有一个新的内联 <em>Reset Frame </em>图标，可<span style="background-color:#ffffff; color:#27282c">用于删除选定的框架和所有嵌套的框架。（此操作以前可从工具栏中获得）</span></p> 
<p style="margin-left:0px"><img alt src="https://oscimg.oschina.net/oscnet/up-9b1784dc1fa37c39baa445d3cb057e9ab9c.gif" width="700" referrerpolicy="no-referrer"></p> 
<ul> 
 <li> <h3>默认隐藏选项卡标签</h3> </li> 
</ul> 
<p style="margin-left:0px">为了最大化 <em>调试器 </em>工具窗口中的可用空间，IntelliJ IDEA 2022.1 EAP 3 默认隐藏了选项卡标签。</p> 
<p style="margin-left:0px"><img alt height="280" src="https://oscimg.oschina.net/oscnet/up-d8361cc5cf4529bb65fa7c5cff213c5f396.gif" width="700" referrerpolicy="no-referrer"></p> 
<p style="margin-left:0px">如果需要重新显示或自定义它们的位置，请使用布局设置中的 <em>Show Tab Labels </em>选项，或通过 <em>Search Everywhere</em>（<em>macOS 上的 ⇧⇧ /Windows/Linux 上</em>的 Shift+Shift ）调用它，并聚焦<em>调试 </em>工具窗口。</p> 
<h2>更新了 Markdown 编辑器浮动工具栏</h2> 
<p>为了更容易格式化 Markdown 文件，IntelliJ IDEA 2022.1 EAP 3 重新设计了出现在文本选择上方的浮动工具栏。除了新设计之外，工具栏现在还提供<strong>创建列表</strong>功能和一个允许<strong>选择标题样式</strong>的下拉菜单。</p> 
<p><img alt height="280" src="https://oscimg.oschina.net/oscnet/up-e4f3f37c86d17e2d34af095f7af4936e9d1.gif" width="700" referrerpolicy="no-referrer"></p> 
<p><span style="background-color:#ffffff; color:#27282c">该浮动工具栏是可自定义的，可以使用所需的选项去填充它，在 <em>设置 | 首选项 | 外观与行为 | 菜单和工具栏 | Markdown 编辑器浮动工具栏</em> 中进行设置：</span></p> 
<p><span style="background-color:#ffffff; color:#27282c"><img alt height="280" src="https://oscimg.oschina.net/oscnet/up-bff72a383f74abe5957b82bb35a209059c1.png" width="700" referrerpolicy="no-referrer"></span></p> 
<h2>新建项目向导中的 Maven Archetype 优化</h2> 
<p>作为新建项目向导的 UI 改造的一部分，IntelliJ IDEA 重新设计了 Maven Archetype 项目生成器，该  2022.1 EAP 3 版本在浏览原型时引入了“键入时搜索”功能，以及在模块创建期间管理原型目录的能力。</p> 
<p><img alt height="280" src="https://oscimg.oschina.net/oscnet/up-420b6f0066a16eccf25377cd223407dbf79.gif" width="700" referrerpolicy="no-referrer"></p> 
<p><span style="background-color:#ffffff; color:#27282c">此外，还可以按原型输入所需的属性：</span></p> 
<p><span style="background-color:#ffffff; color:#27282c"><img alt height="280" src="https://oscimg.oschina.net/oscnet/up-b1426130c021697657318452915797cf939.png" width="700" referrerpolicy="no-referrer"></span></p> 
<p> </p> 
<p>以上是 IntelliJ IDEA 2022.1 EAP 3 版本提供的较显著的改进，可以在<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fyoutrack.jetbrains.com%2Farticles%2FIDEA-A-99%2FIntelliJ-IDEA-2022.1-EAP-3-%28221.4501.155-build%29-Release-Notes" target="_blank">发行说明</a>中找到完整的更新列表。 </p>
                                        </div>
                                      
</div>
            