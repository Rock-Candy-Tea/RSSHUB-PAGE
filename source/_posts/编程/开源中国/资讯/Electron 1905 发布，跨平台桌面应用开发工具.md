
---
title: 'Electron 19.0.5 发布，跨平台桌面应用开发工具'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=1945'
author: 开源中国
comments: false
date: Wed, 22 Jun 2022 07:38:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=1945'
---

<div>   
<div class="content">
                                                                                            <p><span style="background-color:#ffffff; color:#333333">Electron 19.0.5 现已发布，具体更新内容如下：</span></p> 
<p><strong><span><span><span><span><span style="color:#24292f"><span><span><span><span><span><span><span><span><span><span><span style="background-color:#ffffff"><span><span><span>Fixes</span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></strong></p> 
<ul> 
 <li>修复了 macOS 上<code>crashReporter.start()</code>的性能问题。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Felectron%2Felectron%2Fpull%2F34638" target="_blank">#34638 </a></li> 
 <li>修复了<code>setWindowOpenHandler()</code>在回调出错的情况下会崩溃的错误。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Felectron%2Felectron%2Fpull%2F34546" target="_blank">#34546 </a></li> 
 <li>修复了在 Windows 上更改 BrowserView bounds 时未重新计算可拖动区域的问题。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Felectron%2Felectron%2Fpull%2F34611" target="_blank">#34611</a></li> 
 <li>修复了在 Windows 上无论哪个窗口 in focus，media keys 都会被发送到 Electron 的问题。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Felectron%2Felectron%2Fpull%2F34646" target="_blank">#34646</a></li> 
 <li>修复了如果用户使用最小化按钮最小化，normal bounds 将不会适当更新的问题。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Felectron%2Felectron%2Fpull%2F34484" target="_blank">#34484</a></li> 
 <li>修复了在 Linux 上打开或保存对话框的过滤器参数中 <span style="background-color:#ffffff; color:#24292f">passing</span> &#123; name: 'All Files', extensions: ['*'] &#125; 将不允许选择没有扩展名的文件的问题。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Felectron%2Felectron%2Fpull%2F34517" target="_blank">#34517 </a></li> 
 <li>修复了 linux arm64 构建不需要 glibc 2.29+。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Felectron%2Felectron%2Fpull%2F34502" target="_blank">#34502</a></li> 
</ul> 
<p style="text-align:start"><strong><span><span><span><span><span style="color:#24292f"><span><span><span><span><span><span><span><span><span><span><span style="background-color:#ffffff"><span><span><span>Other Changes</span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></strong></p> 
<ul> 
 <li>修复了 BrowserViews 在调用 setBounds 后并不总是在视觉上更新的问题。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Felectron%2Felectron%2Fpull%2F34642" target="_blank">#34642</a></li> 
 <li>在 Linux 上，将 libgdk-pixbuf 依赖项更改为动态链接而不是静态链接。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Felectron%2Felectron%2Fpull%2F34602" target="_blank">#34602</a></li> 
 <li>将 Chromium 更新为 102.0.5005.115。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Felectron%2Felectron%2Fpull%2F34498" target="_blank">#34498</a></li> 
</ul> 
<p>更新说明：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Felectron%2Felectron%2Freleases%2Ftag%2Fv19.0.5" target="_blank">https://github.com/electron/electron/releases/tag/v19.0.5</a></p>
                                        </div>
                                      
</div>
            