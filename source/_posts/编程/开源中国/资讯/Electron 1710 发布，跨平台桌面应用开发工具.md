
---
title: 'Electron 17.1.0 发布，跨平台桌面应用开发工具'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=424'
author: 开源中国
comments: false
date: Tue, 01 Mar 2022 07:43:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=424'
---

<div>   
<div class="content">
                                                                                            <p>Electron 17.1.0 现已发布，具体更新内容如下：</p> 
<p style="text-align:start"><strong>Features</strong></p> 
<ul> 
 <li>为 Windows  Control Overlay 添加了<code>height</code>选项。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Felectron%2Felectron%2Fpull%2F32939" target="_blank">#32939</a></li> 
</ul> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:start"><strong>Fixes</strong></p> 
<ul> 
 <li>修复了 BrowserWindow.showInactive 在 Windows 上将最大化的窗口恢复为非最大化的问题。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Felectron%2Felectron%2Fpull%2F33021" target="_blank">#33021 </a></li> 
 <li>修复了当用户尝试使用<code>window.print()</code>、PDF viewer 中的 print 按钮或使用<code>BrowserWindow.webContents()</code>打印文档，并在产生的打印对话框中点击取消时发生的崩溃。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Felectron%2Felectron%2Fpull%2F33015" target="_blank">#33015</a></li> 
 <li>修复了<code>webContents.openDevTools(&#123; mode &#125;)</code>不适用于某些 dock positions 的问题。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Felectron%2Felectron%2Fpull%2F32945" target="_blank">#32945</a></li> 
 <li>修复了<code>webContents.savePage</code>传递相对路径而不是绝对路径时失败的问题。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Felectron%2Felectron%2Fpull%2F33016" target="_blank">#33016 </a></li> 
 <li>修复了通过 Windows 上的 setAsDefaultProtocolClient 注册的命令字符串。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Felectron%2Felectron%2Fpull%2F33012" target="_blank">#33012</a></li> 
 <li>修复了在渲染器忙碌时退出应用程序的过时渲染器进程。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Felectron%2Felectron%2Fpull%2F32970" target="_blank">#32970 </a></li> 
</ul> 
<p style="text-align:start"><strong><span><span><span><span><span style="color:#24292f"><span><span><span><span><span><span><span><span><span><span><span style="background-color:#ffffff"><span><span><span>Other Changes</span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></strong></p> 
<ul> 
 <li>Chore：从 libuv 向后移植 EPROTOTYPE 修复。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Felectron%2Felectron%2Fpull%2F32943" target="_blank">#32943 </a></li> 
 <li>将 Chromium 更新为 98.0.4758.102。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Felectron%2Felectron%2Fpull%2F32906" target="_blank">#32906</a></li> 
</ul> 
<p>更新说明：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Felectron%2Felectron%2Freleases%2Ftag%2Fv17.1.0" target="_blank">https://github.com/electron/electron/releases/tag/v17.1.0</a></p>
                                        </div>
                                      
</div>
            