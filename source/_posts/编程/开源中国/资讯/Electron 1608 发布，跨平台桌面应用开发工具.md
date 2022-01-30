
---
title: 'Electron 16.0.8 发布，跨平台桌面应用开发工具'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=3783'
author: 开源中国
comments: false
date: Sun, 30 Jan 2022 07:05:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=3783'
---

<div>   
<div class="content">
                                                                                            <p>Electron 16.0.8 现已发布，具体更新内容如下：</p> 
<p style="text-align:start"><strong>Fixes</strong></p> 
<ul> 
 <li>修复了用户尝试下载已编辑的 PDF 时发生的崩溃。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Felectron%2Felectron%2Fpull%2F32538" target="_blank">#32538 </a></li> 
 <li>修复了<code>alert()</code>对话框标题损坏的问题。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Felectron%2Felectron%2Fpull%2F32470" target="_blank">#32470</a></li> 
 <li>修复了<code>ipcRenderer.postMessage</code>未传递<code>transfer</code>参数时会引发错误的问题。<span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Felectron%2Felectron%2Fpull%2F32459" target="_blank">#</a></span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Felectron%2Felectron%2Fpull%2F32460" target="_blank"> 32460</a></li> 
 <li>修复了在 macOS 上 frameless vibrant windows 无法正确显示透明度的问题。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Felectron%2Felectron%2Fpull%2F32648" target="_blank">#32648</a></li> 
 <li>修复了 'maximize' 和 'unmaximize' 事件在 linux 上没有正确触发的问题。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Felectron%2Felectron%2Fpull%2F32497" target="_blank">#32497</a></li> 
 <li>修复了 macOS 上无框窗口的纵横比调整。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Felectron%2Felectron%2Fpull%2F32446" target="_blank">#32446</a></li> 
 <li>修复了调用<code>webContents.setZoomFactor(1.0)</code>时的崩溃。<span># </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Felectron%2Felectron%2Fpull%2F32620" target="_blank">32620</a></li> 
 <li>修复了最小化 的BrowserWindow 被 BrowserWindow.unmaximize() 恢复的问题。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Felectron%2Felectron%2Fpull%2F32495" target="_blank">#32495</a></li> 
 <li>修复了无法关闭的<code>roundedCorners: false</code>窗口。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Felectron%2Felectron%2Fpull%2F32611" target="_blank">#32611</a></li> 
 <li>从 Linux 上的 crashpad_handler 二进制文件中剥离符号，减少包大小。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Felectron%2Felectron%2Fpull%2F32554" target="_blank">#32554</a></li> 
 <li>使得<code>&lt;webview&gt</code>的实现更加 robust，当<code>will-attach-webview</code>处理程序修改<code>params.instanceId</code>内部时，它不再中断。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Felectron%2Felectron%2Fpull%2F32429" target="_blank">#32429</a></li> 
</ul> 
<p style="text-align:start"><strong>Documentation</strong></p> 
<ul> 
 <li><span style="background-color:#ffffff; color:#24292f">Documentation changes</span>：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Felectron%2Felectron%2Fpull%2F32645" target="_blank">#32645</a></li> 
</ul> 
<p>更新说明：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Felectron%2Felectron%2Freleases%2Ftag%2Fv16.0.8" target="_blank">https://github.com/electron/electron/releases/tag/v16.0.8</a></p>
                                        </div>
                                      
</div>
            