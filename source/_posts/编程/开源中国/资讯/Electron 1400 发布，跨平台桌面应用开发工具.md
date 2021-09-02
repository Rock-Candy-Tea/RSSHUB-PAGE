
---
title: 'Electron 14.0.0 发布，跨平台桌面应用开发工具'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=7717'
author: 开源中国
comments: false
date: Thu, 02 Sep 2021 06:32:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=7717'
---

<div>   
<div class="content">
                                                                                            <p>Electron 14.0.0 现已发布，主要更新内容如下：</p> 
<h4>Stack Upgrades</h4> 
<ul> 
 <li>Chromium 93.0.4577.58. 
  <ul> 
   <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdeveloper.chrome.com%2Fblog%2Fnew-in-chrome-93%2F" target="_blank">New in 93</a></li> 
   <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.chromestatus.com%2Ffeatures%23milestone%253D92" target="_blank">New in 92</a></li> 
  </ul> </li> 
 <li>Node v14.17.0. 
  <ul> 
   <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fnodejs%2Fnode%2Fblob%2Fmaster%2Fdoc%2Fchangelogs%2FCHANGELOG_V14.md%2314.17.0" target="_blank">v14.17.0 release notes</a></li> 
  </ul> </li> 
 <li>V8 
  <ul> 
   <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fv8.dev%2Fblog%2Fv8-release-93" target="_blank">v9.3 blog post</a></li> 
   <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fv8.dev%2Fblog%2Fv8-release-92" target="_blank">v9.2 blog post</a></li> 
  </ul> </li> 
</ul> 
<h4>Breaking Changes</h4> 
<ul> 
 <li>子窗口不再从其父窗口继承 BrowserWindow 构造选项。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Felectron%2Felectron%2Fpull%2F28550" target="_blank">#28550</a></li> 
 <li>不推荐使用的<code>worldSafeExecuteJavaScript</code>选项已从<code>webPreferences</code>中移除。 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Felectron%2Felectron%2Fpull%2F28456" target="_blank">#28456</a></li> 
 <li>从<code>new-window</code>和<code>did-create-window</code>WebContents 事件中删除了已被废弃的<code>additionalFeatures</code>属性。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Felectron%2Felectron%2Fpull%2F28548" target="_blank">#28548</a></li> 
 <li>删除了已废弃的<code>app.allowRendererProcessReuse</code>和 BrowserWindow<code>affinity</code>选项。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Felectron%2Felectron%2Fpull%2F26874" target="_blank">#26874</a></li> 
</ul> 
<h4>Features</h4> 
<p><strong>Additions</strong></p> 
<ul> 
 <li>添加<code>BrowserWindow.isFocusable()</code>用于确定窗口是否可聚焦。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Felectron%2Felectron%2Fpull%2F28642" target="_blank">#28642</a></li> 
 <li>添加了<code>WebFrameMain.visibilityState</code>实例属性。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Felectron%2Felectron%2Fpull%2F28706" target="_blank">#28706</a></li> 
 <li>在传递给用<code>setWindowOpenHandler</code>注册的窗口打开处理程序的细节对象中添加了<code>disposition</code>,<code>referrer</code>和<code>postBody</code>。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Felectron%2Felectron%2Fpull%2F28518" target="_blank">#28518</a></li> 
 <li>添加了<code>@electron/remote</code>使用的<code>process.contextId</code>。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Felectron%2Felectron%2Fpull%2F28007" target="_blank">#28007</a></li> 
 <li>在 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.electronjs.org%2Fdocs%2Ftutorial%2Ffuses" target="_blank">Electron Fuse</a> 后面添加了实验性 cookie 加密支持。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Felectron%2Felectron%2Fpull%2F29492" target="_blank">#29492</a></li> 
 <li>为<code>webRequest</code>listener details 添加了缺失的<code>resourceType</code>转换：<code>font</code>、<code>ping</code>、<code>cspReport</code>、<code>media</code>、<code>webSocket</code>。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Felectron%2Felectron%2Fpull%2F30050" target="_blank">#30050</a></li> 
 <li>添加了新的<code>session.storagePath</code>API 以获取磁盘上会话特定数据的路径。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Felectron%2Felectron%2Fpull%2F28665" target="_blank">28665</a></li> 
 <li>添加<code>webContents.fromDevToolsTargetId(targetId)</code>以从关联的 Chrome DevTools 协议 TargetID 中查找 WebContents 实例。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Felectron%2Felectron%2Fpull%2F30732" target="_blank">#30732</a></li> 
 <li>在 macOS 上增加了对 Windows Control Overlay 的支持。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Felectron%2Felectron%2Fpull%2F29986" target="_blank">#29986</a></li> 
 <li>在 Windows 上添加了对 Windows Control Overlay 的支持。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Felectron%2Felectron%2Fpull%2F30678" target="_blank">#30678</a></li> 
 <li>添加了对调试 URL 的支持，如<code>chrome://gpucrash</code>. <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Felectron%2Felectron%2Fpull%2F29466" target="_blank">#29466</a></li> 
 <li>添加了对将 Chromium 日志记录到带有. 此外，现在可以通过在第一个 JS 滴答期间附加命令行开关来启用 JavaScript 的日志记录。增加了对 Chromium 日志的支持，即用<code>--log-file=.../path/to/file.log</code>来引导 Chromium 的日志。另外，现在也可以通过在第一个 JS tick 期间添加命令行开关来启用 JavaScript 的日志记录。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Felectron%2Felectron%2Fpull%2F29963" target="_blank">#29963</a></li> 
 <li>在节点加密中添加了对 des-ede3 密码的支持。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Felectron%2Felectron%2Fpull%2F27897" target="_blank">#27897</a></li> 
 <li>增加了<code>ContextBridgeMutability</code>功能，在暴露值时跳过了 Context Bridge DeepFreeze 和 SetReadOnlyNonConfigurable。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Felectron%2Felectron%2Fpull%2F27348" target="_blank">#27348</a></li> 
</ul> 
<p><strong>Improvements</strong></p> 
<ul> 
 <li> <p>改进了通过 contextBridge 来回发送的函数的性能特征。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Felectron%2Felectron%2Fpull%2F28285" target="_blank">#28285</a></p> </li> 
 <li>改进了<code>napi_threadsafe_function</code>的性能。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Felectron%2Felectron%2Fpull%2F29021" target="_blank">＃29021 </a></li> 
</ul> 
<p><strong>Removed/Deprecated</strong></p> 
<ul> 
 <li> <p>当<code>uploadToServer</code>为false时，<code>crashReporter.start</code>的<code>submitURL</code>选项不再是一个必要的参数。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Felectron%2Felectron%2Fpull%2F28105" target="_blank">#28105</a></p> </li> 
</ul> 
<h4>Fixes</h4> 
<ul> 
 <li>允许 Node.js 在调用<code>uv_run()</code>之前使用显式微任务策略管理微任务队列。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Felectron%2Felectron%2Fpull%2F28957" target="_blank">#28957</a></li> 
 <li>允许从自定义协议和 asar 包加载 source maps。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Felectron%2Felectron%2Fpull%2F28573" target="_blank">＃28573 </a></li> 
 <li>具有指定背景颜色或透明度的子窗口现在可以按预期工作。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Felectron%2Felectron%2Fpull%2F28054" target="_blank">＃28054</a></li> 
 <li>从<code>systemPreferences.getAccentColor()</code>、<code>getSystemColor</code>和<code>getColor</code>返回的颜色现在被正确地转换成设备的色彩空间。之前的颜色会有细微的不正确。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Felectron%2Felectron%2Fpull%2F28121" target="_blank">#28121</a></li> 
 <li>Electron Fuses 现在跨平台的顺序一致。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Felectron%2Felectron%2Fpull%2F29616" target="_blank">#29616</a></li> 
 <li>修复了<code>fs.promises.readFile</code>在向路径参数传递一个<code>FileHandle</code>时会出现不恰当的错误的问题。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Felectron%2Felectron%2Fpull%2F29577" target="_blank">＃29577 </a></li> 
 <li>修复了当通过需要认证的代理连接已注册 WebRequest 监听器的应用程序时，CORS 预检请求总是被取消。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Felectron%2Felectron%2Fpull%2F29812" target="_blank">＃29812 </a></li> 
 <li>......</li> 
</ul> 
<h4>终止对 11.xy 的支持</h4> 
<p>根据项目的<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.electronjs.org%2Fdocs%2Ftutorial%2Fsupport%23supported-versions" target="_blank">支持政策，</a> Electron 11.xy 已终止<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.electronjs.org%2Fdocs%2Ftutorial%2Fsupport%23supported-versions" target="_blank">支持</a>。鼓励开发人员和应用程序升级到较新版本的 Electron。</p> 
<p>更新说明：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Felectron%2Felectron%2Freleases%2Ftag%2Fv14.0.0" target="_blank">https://github.com/electron/electron/releases/tag/v14.0.0</a></p>
                                        </div>
                                      
</div>
            