
---
title: 'Electron 13.1.7 发布，跨平台桌面应用开发工具'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=5531'
author: 开源中国
comments: false
date: Sun, 18 Jul 2021 07:34:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=5531'
---

<div>   
<div class="content">
                                                                                            <p>Electron 13.1.7 现已发布，主要更新内容如下： </p> 
<p><strong>Fixes</strong></p> 
<ul> 
 <li>修复了 webview 中的<code>requestFullscreen</code>不会使元素全屏显示的问题。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Felectron%2Felectron%2Fpull%2F29987" target="_blank">＃29987 </a></li> 
 <li>修复了同步调用<code>webContents.on('login')</code>回调时崩溃的问题。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Felectron%2Felectron%2Fpull%2F30091" target="_blank">＃30091 </a></li> 
 <li>修复了使用<code>fsPromises.readFile</code>时可能出现的渲染器崩溃问题。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Felectron%2Felectron%2Fpull%2F29928" target="_blank">#29928</a></li> 
 <li>修复了 Electron 有时不支持用户定义的下载目录的问题。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Felectron%2Felectron%2Fpull%2F29968" target="_blank">＃29968</a></li> 
 <li>修复了在 macOS 上退出全屏并添加<code>BrowserView</code>时，traffic lights 会被重复绘制的问题。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Felectron%2Felectron%2Fpull%2F30149" target="_blank">#30149</a></li> 
 <li>修复了在 macOS 上打开多个窗口时的<code>document.focus</code>错误值 
  <ul> 
   <li>修复在 Mac 上打开面板或使用自定义窗口切换器时的关键窗口状态。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Felectron%2Felectron%2Fpull%2F29234" target="_blank">＃29234</a></li> 
  </ul> </li> 
 <li>修复了 systemPreferences.getSystemColor 返回缺少 alpha 值的颜色。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Felectron%2Felectron%2Fpull%2F30088" target="_blank">#30088</a></li> 
</ul> 
<p><strong>Other Changes</strong></p> 
<ul> 
 <li> <p>1216190 的反向移植修复。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Felectron%2Felectron%2Fpull%2F30100" target="_blank">#30100</a></p> </li> 
</ul> 
<p><strong>Documentation</strong></p> 
<ul> 
 <li> <p>Documentation changes：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Felectron%2Felectron%2Fpull%2F30057" target="_blank">#30057</a></p> </li> 
</ul> 
<p>更新说明：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Felectron%2Felectron%2Freleases%2Ftag%2Fv13.1.7" target="_blank">https://github.com/electron/electron/releases/tag/v13.1.7</a></p>
                                        </div>
                                      
</div>
            