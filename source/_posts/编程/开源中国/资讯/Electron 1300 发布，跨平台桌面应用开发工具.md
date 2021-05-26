
---
title: 'Electron 13.0.0 发布，跨平台桌面应用开发工具'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=5333'
author: 开源中国
comments: false
date: Wed, 26 May 2021 07:27:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=5333'
---

<div>   
<div class="content">
                                                                    
                                                        <p>Electron 13.0.0 现已发布，主要更新内容如下： </p> 
<h4><strong>Stack Upgrades</strong></h4> 
<ul> 
 <li>Chromium 91.0.4472.69. 
  <ul> 
   <li>v91 blog post</li> 
   <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdeveloper.chrome.com%2Fblog%2Fnew-in-chrome-90%2F" target="_blank">v90 blog post</a></li> 
  </ul> </li> 
 <li>Node v14.17.0 
  <ul> 
   <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fnodejs%2Fnode%2Fblob%2Fmaster%2Fdoc%2Fchangelogs%2FCHANGELOG_V14.md%2314.17.0" target="_blank">v14.17.0 release notes</a></li> 
  </ul> </li> 
 <li>V8 v9.1 
  <ul> 
   <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fv8.dev%2Fblog%2Fv8-release-91" target="_blank">v9.1 blog post</a></li> 
   <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fv8.dev%2Fblog%2Fv8-release-90" target="_blank">v9.0 blog post</a></li> 
  </ul> </li> 
</ul> 
<h4><strong>Breaking Changes</strong></h4> 
<ul> 
 <li>已修复，因此 window.open() 参数 frameName 不再被设置为 window title。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Felectron%2Felectron%2Fpull%2F27481" target="_blank">＃27481</a></li> 
 <li>更改了<code>session.setPermissionCheckHandler(handler)</code>，允许<code>handler</code>第一个参数<code>webContents</code>为<code>null</code>。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Felectron%2Felectron%2Fpull%2F19903" target="_blank">＃19903</a></li> 
</ul> 
<h4>Features</h4> 
<p><strong>Additions</strong></p> 
<ul> 
 <li>添加了<code>@electron/remote</code>使用的<code>process.contextId</code>。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Felectron%2Felectron%2Fpull%2F28251" target="_blank">＃28251</a></li> 
 <li>添加了<code>process.contextIsolated</code>属性，用于指示当前渲染器上下文是否启用了<code>contextIsolation</code>。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Felectron%2Felectron%2Fpull%2F28252" target="_blank">＃28252</a></li> 
 <li>已添加<code>process.uptime()</code>到沙盒渲染器。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Felectron%2Felectron%2Fpull%2F26684" target="_blank">＃26684</a></li> 
 <li>为<code>BrowserWindow</code>新增了<code>roundedCorners</code>选项。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Felectron%2Felectron%2Fpull%2F27572" target="_blank">＃27572</a></li> 
 <li>为作为<code>context-menu</code>事件的一部分发出的参数添加了缺失的字段。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Felectron%2Felectron%2Fpull%2F26788" target="_blank">＃26788</a></li> 
 <li>添加了新的<code>session.storagePath</code>API，以获取磁盘上特定于会话的数据的路径。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Felectron%2Felectron%2Fpull%2F28866" target="_blank">＃28866</a></li> 
 <li>添加了对通过 context bridge 的 DOM 元素的支持。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Felectron%2Felectron%2Fpull%2F26776" target="_blank">＃26776</a></li> 
 <li>添加了对注册 Manifest V3 扩展服务工作者的支持。 
  <ul> 
   <li>为<code>ServiceWorkers</code>添加了“registration-completed”事件。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Felectron%2Felectron%2Fpull%2F27562" target="_blank">＃27562</a></li> 
  </ul> </li> 
 <li>在传递给用<code>setWindowOpenHandler</code>注册的窗口打开处理程序的 details object 中添加了<code>disposition</code>、<code>referrer</code>和<code>postBody</code>。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Felectron%2Felectron%2Fpull%2F29277" target="_blank">＃29277</a></li> 
</ul> 
<p><strong>Improvements</strong></p> 
<ul> 
 <li>Additional permission checks 现在是通过<code>session.setPermissionCheckHandler</code>进行的。其中包括<code>Notification.permission</code>和<code>permission.query</code>。请注意，检查处理程序的<code>webContents</code>参数现在可以为 null。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Felectron%2Felectron%2Fpull%2F19903" target="_blank">＃19903</a></li> 
 <li>允许在 macOS 上的 win.SetVisibleOnAllWorkspaces 中跳过进程类型转换。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Felectron%2Felectron%2Fpull%2F27200" target="_blank">＃27200</a></li> 
 <li>已还原<code>WebFrameMain.executeJavaScriptInIsolatedWorld()</code>。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Felectron%2Felectron%2Fpull%2F27926" target="_blank">＃27926</a></li> 
 <li>使<code>trafficLightPosition</code>选项适用于<code>customButtonOnHover</code>窗口。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Felectron%2Felectron%2Fpull%2F26789" target="_blank">＃26789</a></li> 
 <li>当<code>uploadToServer</code>值为 false 时，<code>crashReporter.start</code>的<code>submitURL</code>选项不再是必需的参数。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Felectron%2Felectron%2Fpull%2F28283" target="_blank">＃28283</a></li> 
 <li>改进的<code>napi_threadsafe_function</code>性能。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Felectron%2Felectron%2Fpull%2F29048" target="_blank">＃29048 </a></li> 
</ul> 
<p><strong>Removed/Deprecated</strong></p> 
<ul> 
 <li>删除了已废弃的<code>BrowserWindow</code>扩展 API。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Felectron%2Felectron%2Fpull%2F26696" target="_blank">＃26696</a></li> 
 <li>删除了已废弃的<code>shell.moveItemToTrash()</code>。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Felectron%2Felectron%2Fpull%2F26723" target="_blank">＃26723</a></li> 
 <li>删除了已废弃的<code>systemPreferences</code>方法。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Felectron%2Felectron%2Fpull%2F26849" target="_blank">＃26849</a></li> 
</ul> 
<h4>Fixes</h4> 
<ul> 
 <li>修复<code>hiddenInset</code>titleBarStyle 异常的全屏标题栏。修复了<code>hiddenInset</code>titleBarStyle 与<code>trafficLightPosition</code>option 不兼容的问题。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Felectron%2Felectron%2Fpull%2F27489" target="_blank">＃27489</a></li> 
 <li>修复了使用 off-the-record 会话时，在关机过程中的一个 use-after-free 错误。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Felectron%2Felectron%2Fpull%2F26680" target="_blank">＃26680</a></li> 
 <li>修复了<code>contextBridge</code>可能会错误地尝试序列化某些 WebAssembly 对象的问题。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Felectron%2Felectron%2Fpull%2F27518" target="_blank">＃27518</a></li> 
 <li>修复了协议模块中 302/303/307 重定向响应的行为。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Felectron%2Felectron%2Fpull%2F26297" target="_blank">＃26297</a></li> 
 <li>使<code>BrowserWindow.setWindowButtonVisibility</code>对具有<code>customButtonsOnHover</code>标题栏样式的窗口有效。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Felectron%2Felectron%2Fpull%2F27073" target="_blank">＃27073</a></li> 
 <li>修复了开机时的 rare crash。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Felectron%2Felectron%2Fpull%2F29109" target="_blank">＃29109</a></li> 
 <li>修复了导致无法显示 PDF 查看器的权限问题。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Felectron%2Felectron%2Fpull%2F29252" target="_blank">＃29252</a></li> 
 <li>修复了在 macOS 上使用 vibrancy 和使无框窗口全屏时可能出现的不正确的 visual artifacts。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Felectron%2Felectron%2Fpull%2F29099" target="_blank">＃29099</a></li> 
 <li>修复了在 macOS 上使用 vibrancy 和 titleBarStyle 一起导致奇怪的 window shadow 的问题。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Felectron%2Felectron%2Fpull%2F29165" target="_blank">＃29165</a></li> 
 <li>恢复了app.setAppUserModelId的跨平台 noop 实现。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Felectron%2Felectron%2Fpull%2F28921" target="_blank">＃28921</a></li> 
 <li>......</li> 
</ul> 
<h4>Other Changes</h4> 
<ul> 
 <li>非功能性更改；更新版本库的问题模板文件。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Felectron%2Felectron%2Fpull%2F27825" target="_blank">＃27825</a></li> 
 <li>更新了默认 Electron 菜单中的社区讨论链接。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Felectron%2Felectron%2Fpull%2F28459" target="_blank">＃28459 </a></li> 
</ul> 
<h4>End of Support for 10.x.y</h4> 
<p>根据项目的支持策略，Electron 10.x.y 已经达到了支持的终点。官方鼓励开发者和应用程序升级到更新的 Electron 版本。</p> 
<p>更多详情可查看：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Felectron%2Felectron%2Freleases%2Ftag%2Fv13.0.0" target="_blank">https://github.com/electron/electron/releases/tag/v13.0.0</a></p>
                                        </div>
                                      
</div>
            