
---
title: 'Windows Terminal Preview 1.14 发布，支持窗口背景图功能'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://static.oschina.net/uploads/space/2022/0525/073258_Bwts_5430600.gif'
author: 开源中国
comments: false
date: Wed, 25 May 2022 07:29:00 GMT
thumbnail: 'https://static.oschina.net/uploads/space/2022/0525/073258_Bwts_5430600.gif'
---

<div>   
<div class="content">
                                                                    
                                                        <p>Windows Terminal Preview 1.14 已发布，该版本专注于修复错误和提高质量，带来如下内容：</p> 
<h3>窗口背景图功能（实验性）</h3> 
<p>现在可以让所有窗格在一个背景图上拆分，而不是每个窗格都有自己的背景图像。使用全局设置</p> 
<pre style="text-align:left"><code><span style="color:#0c6d22"><span style="color:#0c6d22">"experimental.useBackgroundImageForWindow"</span></span><span style="color:#666600"><span style="color:#666600">:</span></span><span style="color:#000000"><span style="color:#000000"> </span></span><span style="color:#000088"><span style="color:#000088">true</span></span></code></pre> 
<p>即可完成将焦点配置文件的背景图应用到整个窗口。</p> 
<p><img alt height="427" src="https://static.oschina.net/uploads/space/2022/0525/073258_Bwts_5430600.gif" width="700" referrerpolicy="no-referrer"></p> 
<h2>新行为</h2> 
<p>现在可以使用 selectAll 操作选择缓冲区中的所有文本，默认按键 Ctrl+Shift+A  。</p> 
<h2 style="text-align:left">其他改进</h2> 
<ul> 
 <li>对选项卡、滚动条、新选项卡按钮、标题按钮、颜色选择器、设置 UI、命令调色板和搜索框进行了视觉更改，以使终端更接近 Windows 11 设计语言</li> 
 <li>终端现在知道 Caps Lock、Scroll Lock 和 Num Lock 的切换状态。</li> 
 <li>改进了 Atlas 渲染器的稳定性和性能。</li> 
</ul> 
<h2>Bug 修复</h2> 
<ul> 
 <li>profile.defaults 中的命令行不再覆盖配置文件中指定 cmd.exe 或 powershell.exe 的命令行。</li> 
 <li>屏幕阅读器可以更好地阅读 UI 中的一些设置。</li> 
 <li>在设置 UI 中删除最后一个配置文件时，终端不再崩溃。</li> 
</ul> 
<p> </p> 
<p>更多内容可在<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdevblogs.microsoft.com%2Fcommandline%2Fwindows-terminal-preview-1-14-release%2F" target="_blank">发布博客</a>中阅读。</p> 
<p> </p> 
<p> </p> 
<div> 
 <div> 
  <ul> 
  </ul> 
 </div> 
</div> 
<p style="color:#000000; margin-left:0; margin-right:0; text-align:start"> </p> 
<p> </p>
                                        </div>
                                      
</div>
            