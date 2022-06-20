
---
title: 'Tauri 1.0 正式发布，Rust 编写的桌面 UI 框架'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://static.oschina.net/uploads/space/2022/0620/073538_9p8L_2720166.png'
author: 开源中国
comments: false
date: Mon, 20 Jun 2022 08:06:00 GMT
thumbnail: 'https://static.oschina.net/uploads/space/2022/0620/073538_9p8L_2720166.png'
---

<div>   
<div class="content">
                                                                    
                                                        <p>Tauri 1.0 已正式发布。</p> 
<blockquote> 
 <p>Tauri 是一个桌面 UI 框架，<span><span><span style="color:#1c1e21"><span><span><span><span><span><span><span><span><span><span><span><span><span><span>可让开发者使用每个平台的 Webview 技术栈为所有主要桌面操作系统构建应用程序，目前支持 Windows/macOS/Linux 等平台。开发者通过 Tauri 几乎可以使用任何</span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span>编译为 HTML、JS 和 CSS 的<span><span><span style="color:#1c1e21"><span><span><span><span><span><span><span><span><span><span><span><span><span><span>前端框架来构建桌面 UI。</span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></p> 
 <p><span><span><span style="color:#1c1e21"><span><span><span><span><span><span><span><span><span><span><span><span><span><span>Tauri 核心库采用 Rust 编写，</span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span>使用 Tauri 开发的应用程序的后端是一个基于 Rust 的二进制文件，带有一个前端可以与之交互的 API，通过 JS Api 调用后台接口。</p> 
</blockquote> 
<p><img src="https://static.oschina.net/uploads/space/2022/0620/073538_9p8L_2720166.png" referrerpolicy="no-referrer"></p> 
<p>可以看到，Tauri 对标的正是 Electron。与 Electron 相比，Tauri 更加轻量、性能更好。</p> 
<p>Tauri v.s Electron</p> 
<table cellspacing="0" style="-webkit-text-stroke-width:0px; background-color:#ffffff; border-collapse:collapse; border-spacing:0px; box-sizing:border-box; color:#24292f; display:block; font-family:-apple-system,BlinkMacSystemFont,"Segoe UI",Helvetica,Arial,sans-serif,"Apple Color Emoji","Segoe UI Emoji"; font-size:16px; font-style:normal; font-variant-caps:normal; font-variant-ligatures:normal; font-weight:400; letter-spacing:normal; margin-bottom:16px; margin-top:0px; max-width:100%; orphans:2; overflow:auto; text-align:start; text-decoration-color:initial; text-decoration-style:initial; text-decoration-thickness:initial; text-transform:none; white-space:normal; widows:2; width:max-content; word-spacing:0px"> 
 <thead> 
  <tr> 
   <th>Detail</th> 
   <th>Tauri</th> 
   <th>Electron</th> 
  </tr> 
 </thead> 
 <tbody> 
  <tr> 
   <td style="border-style:solid; border-width:1px">Installer Size Linux</td> 
   <td style="border-style:solid; border-width:1px">3.1 MB</td> 
   <td style="border-style:solid; border-width:1px">52.1 MB</td> 
  </tr> 
  <tr> 
   <td style="border-style:solid; border-width:1px">Memory Consumption Linux</td> 
   <td style="border-style:solid; border-width:1px">180 MB</td> 
   <td style="border-style:solid; border-width:1px">462 MB</td> 
  </tr> 
  <tr> 
   <td style="border-style:solid; border-width:1px">Launch Time Linux</td> 
   <td style="border-style:solid; border-width:1px">0.39s</td> 
   <td style="border-style:solid; border-width:1px">0.80s</td> 
  </tr> 
  <tr> 
   <td style="border-style:solid; border-width:1px">Interface Service Provider</td> 
   <td style="border-style:solid; border-width:1px">WRY</td> 
   <td style="border-style:solid; border-width:1px">Chromium</td> 
  </tr> 
  <tr> 
   <td style="border-style:solid; border-width:1px">Backend Binding</td> 
   <td style="border-style:solid; border-width:1px">Rust</td> 
   <td style="border-style:solid; border-width:1px">Node.js (ECMAScript)</td> 
  </tr> 
  <tr> 
   <td style="border-style:solid; border-width:1px">Underlying Engine</td> 
   <td style="border-style:solid; border-width:1px">Rust</td> 
   <td style="border-style:solid; border-width:1px">V8 (C/C++)</td> 
  </tr> 
  <tr> 
   <td style="border-style:solid; border-width:1px">FLOSS</td> 
   <td style="border-style:solid; border-width:1px">Yes</td> 
   <td style="border-style:solid; border-width:1px">No</td> 
  </tr> 
  <tr> 
   <td style="border-style:solid; border-width:1px">Multithreading</td> 
   <td style="border-style:solid; border-width:1px">Yes</td> 
   <td style="border-style:solid; border-width:1px">Yes</td> 
  </tr> 
  <tr> 
   <td style="border-style:solid; border-width:1px">Bytecode Delivery</td> 
   <td style="border-style:solid; border-width:1px">Yes</td> 
   <td style="border-style:solid; border-width:1px">No</td> 
  </tr> 
  <tr> 
   <td style="border-style:solid; border-width:1px">Multiple Windows</td> 
   <td style="border-style:solid; border-width:1px">Yes</td> 
   <td style="border-style:solid; border-width:1px">Yes</td> 
  </tr> 
  <tr> 
   <td style="border-style:solid; border-width:1px">Auto Updater</td> 
   <td style="border-style:solid; border-width:1px">Yes</td> 
   <td style="border-style:solid; border-width:1px">Yes1</td> 
  </tr> 
  <tr> 
   <td style="border-style:solid; border-width:1px">Custom App Icon</td> 
   <td style="border-style:solid; border-width:1px">Yes</td> 
   <td style="border-style:solid; border-width:1px">Yes</td> 
  </tr> 
  <tr> 
   <td style="border-style:solid; border-width:1px">Windows Binary</td> 
   <td style="border-style:solid; border-width:1px">Yes</td> 
   <td style="border-style:solid; border-width:1px">Yes</td> 
  </tr> 
  <tr> 
   <td style="border-style:solid; border-width:1px">macOS Binary</td> 
   <td style="border-style:solid; border-width:1px">Yes</td> 
   <td style="border-style:solid; border-width:1px">Yes</td> 
  </tr> 
  <tr> 
   <td style="border-style:solid; border-width:1px">Linux Binary</td> 
   <td style="border-style:solid; border-width:1px">Yes</td> 
   <td style="border-style:solid; border-width:1px">Yes</td> 
  </tr> 
  <tr> 
   <td style="border-style:solid; border-width:1px">iOS Binary</td> 
   <td style="border-style:solid; border-width:1px">Soon</td> 
   <td style="border-style:solid; border-width:1px">No</td> 
  </tr> 
  <tr> 
   <td style="border-style:solid; border-width:1px">Android Binary</td> 
   <td style="border-style:solid; border-width:1px">Soon</td> 
   <td style="border-style:solid; border-width:1px">No</td> 
  </tr> 
  <tr> 
   <td style="border-style:solid; border-width:1px">Desktop Tray</td> 
   <td style="border-style:solid; border-width:1px">Yes</td> 
   <td style="border-style:solid; border-width:1px">Yes</td> 
  </tr> 
  <tr> 
   <td style="border-style:solid; border-width:1px">Sidecar Binaries</td> 
   <td style="border-style:solid; border-width:1px">Yes</td> 
   <td style="border-style:solid; border-width:1px">No</td> 
  </tr> 
 </tbody> 
</table> 
<p style="text-align:start"><span><span><span style="color:#1c1e21"><span><span><span><span><span><span><span><span><span><span><span><span><span><span>在 1.0 版本发布之后，开发团队已经开始计划 Tauri 的下一步。除了要继续优化文档，还包括以下计划：</span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></p> 
<ul> 
 <li>对移动端 iOS 和 Android 的支持</li> 
 <li>引入替代渲染器</li> 
 <li>IPC 功能增强，以​​实现改进的调试</li> 
 <li>引入 runtime 插件</li> 
 <li>支持对其他语言的附加绑定</li> 
</ul> 
<p><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Ftauri.app%2Fblog%2Ftauri_1_0%2F" target="_blank">详情查看发布公告</a>。</p>
                                        </div>
                                      
</div>
            