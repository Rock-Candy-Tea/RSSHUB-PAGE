
---
title: 'Terminal.Gui v1.8.0 发布，.NET 跨平台终端 UI 工具包'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://static.oschina.net/uploads/space/2022/0920/151914_0jVc_2720166.gif'
author: 开源中国
comments: false
date: Wed, 21 Sep 2022 07:04:00 GMT
thumbnail: 'https://static.oschina.net/uploads/space/2022/0920/151914_0jVc_2720166.gif'
---

<div>   
<div class="content">
                                                                                            <p>Terminal.Gui 是适用于 .NET 的跨平台终端 UI 工具包，可在 Windows、Mac 和 Linux/Unix 平台上为 .NET、.NET Core 和 Mono 构建富控制台应用程序。</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><img src="https://static.oschina.net/uploads/space/2022/0920/151914_0jVc_2720166.gif" referrerpolicy="no-referrer"></p> 
<p><strong>特性</strong></p> 
<ul> 
 <li>跨平台：支持 Windows、Mac 和 Linux。Curses、Windows 控制台和 .NET 控制台的终端驱动程序意味着应用程序在彩色和单色终端上都能正常运行。</li> 
 <li>键盘和鼠标输入：支持键盘和鼠标输入，包括拖放支持。</li> 
 <li>灵活布局：支持绝对布局和创新的计算布局系统 (Computed Layout)。Computed Layout 使控件之间的相对布局变得容易，并支持动态终端 UI。</li> 
 <li>支持剪贴板：剪切、复制和粘贴通过<code>Clipboard</code>类提供的文本。</li> 
 <li>任意视图：所有可见的 UI 元素都是<code>View</code>类的子类，而这些子类又可以包含任意数量的 sub-views。</li> 
 <li>高级应用程序功能：主循环支持处理事件、空闲处理程序、计时器和监控文件描述符。大多数类对于 threading 是安全的。</li> 
 <li>响应式扩展 (Reactive Extensions)：使用响应式扩展并受益于提高的代码可读性，以及应用 MVVM 模式和 ReactiveUI 数据绑定的能力。</li> 
</ul> 
<p>最新发布的 1.8.0 修复了许多问题：</p> 
<ul> 
 <li><span>修复 </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgui-cs%2FTerminal.Gui%2Fissues%2F1943" target="_blank">#1943</a>：鼠标 ButtonShift 无法保留选中文本的问题</li> 
 <li>将<span> </span><code>main</code><span> 合并到</span><span> </span><code>develop</code></li> 
 <li>确保 isButtonShift flag 在所有情况下都被禁用</li> 
 <li>修复<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgui-cs%2FTerminal.Gui%2Fissues%2F1948" target="_blank">#1948</a>：Get unwrapped cursor position when word wrap is enabled on TextView</li> 
 <li>在 TextView 上启用 word wrap 功能时，获取 unwrapped 的光标位置</li> 
 <li>修复同步上下文方法 Send 目前是阻塞的问题</li> 
 <li>将 Microsoft.NET.Test.Sdk 从 17.2.0 升级到 17.3.0</li> 
 <li>修复<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgui-cs%2FTerminal.Gui%2Fissues%2F1951" target="_blank">#1951</a>：选定文本的 TextView 不会滚动到光标位置以外</li> 
 <li><span>修复 </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgui-cs%2FTerminal.Gui%2Fissues%2F1953" target="_blank">#1953</a>：TextView 光标位置无法通过鼠标更新</li> 
</ul> 
<p><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgui-cs%2FTerminal.Gui%2Freleases%2Ftag%2Fv1.8.0" target="_blank">详情查看 release note</a>。</p>
                                        </div>
                                      
</div>
            