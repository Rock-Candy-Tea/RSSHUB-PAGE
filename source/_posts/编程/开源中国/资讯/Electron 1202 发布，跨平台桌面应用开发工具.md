
---
title: 'Electron 12.0.2 发布，跨平台桌面应用开发工具'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=4982'
author: 开源中国
comments: false
date: Fri, 26 Mar 2021 07:04:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=4982'
---

<div>   
<div class="content">
                                                                                            <p>Electron 12.0.2 现已发布，主要更新内容如下： </p> 
<p><strong>Fixes</strong> </p> 
<ul> 
 <li>从 systemPreferences.getAccentColor()、getSystemColor 和 getColor 返回的颜色现在可以正确地转换到设备的颜色空间。之前的颜色会有微妙的错误。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Felectron%2Felectron%2Fpull%2F28172" target="_blank">＃28172</a></li> 
 <li>修复了<code>desktopCapturer.getSources()</code>promise result 有时无法解析的问题。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Felectron%2Felectron%2Fpull%2F28281" target="_blank">＃28281</a></li> 
 <li>修复了 Windows 上罕见的崩溃，该崩溃可能在发出某些 Tray events 时发生。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Felectron%2Felectron%2Fpull%2F28111" target="_blank">＃28111</a></li> 
 <li>修复了一个问题，在 Windows 下，一些 Node.js 模块会在页面重新加载时挂起。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Felectron%2Felectron%2Fpull%2F28337" target="_blank">＃28337</a></li> 
 <li>修复了 macOS 上 BrowserViews 中的拖动区域可能偏离其 y 轴的问题。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Felectron%2Felectron%2Fpull%2F28296" target="_blank">＃28296</a></li> 
 <li>修复了上下文菜单靠近屏幕边缘时无法正确定位的问题。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Felectron%2Felectron%2Fpull%2F28277" target="_blank">＃28277</a></li> 
 <li>修复了在没有指定背景色的透明窗口上调用<code>getBackgroundColor</code>时的崩溃。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Felectron%2Felectron%2Fpull%2F28188" target="_blank">＃28188 </a></li> 
 <li>修复了从 asar 文件中密集 I/O，导致一段时间后出现 ERR_FILE_NOT_FOUND 的问题。 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Felectron%2Felectron%2Fpull%2F28202" target="_blank">＃28202 </a></li> 
 <li>在 Windows 上传递给<code>shell.openExternal</code>的 URL 现在可以正确地进行 URI 编码。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Felectron%2Felectron%2Fpull%2F28341" target="_blank">＃28341</a></li> 
</ul> 
<p><strong>Other Changes</strong></p> 
<ul> 
 <li> <p>修复了在 Windows 上使用 AsyncCleanupHooks 进行本机模块编译的问题。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Felectron%2Felectron%2Fpull%2F28109" target="_blank">＃28109 </a></p> </li> 
 <li>将 Chromium 更新为 89.0.4389.90。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Felectron%2Felectron%2Fpull%2F28174" target="_blank">＃28174</a></li> 
</ul> 
<p><strong>Documentation</strong></p> 
<ul> 
 <li>文档更改：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Felectron%2Felectron%2Fpull%2F28214" target="_blank">＃28214</a></li> 
</ul> 
<p>更新说明： <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Felectron%2Felectron%2Freleases%2Ftag%2Fv12.0.2" target="_blank">https://github.com/electron/electron/releases/tag/v12.0.2</a></p>
                                        </div>
                                      
</div>
            