
---
title: 'Qt 6.4 Beta 发布，新增 HTTP Server & 3D Physics 模块'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://oscimg.oschina.net/oscnet/up-3a2bc58d11315ad8c2f11c7fef0144d8f5a.png'
author: 开源中国
comments: false
date: Sun, 19 Jun 2022 07:43:00 GMT
thumbnail: 'https://oscimg.oschina.net/oscnet/up-3a2bc58d11315ad8c2f11c7fef0144d8f5a.png'
---

<div>   
<div class="content">
                                                                    
                                                        <p>Qt 6.4<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.qt.io%2Fblog%2Fqt-6.4-beta-released" target="_blank"> 发布</a>了首个 Beta 版本，正式版预计于 9 月底推出。</p> 
<p>与 Qt 6.3 相比，Qt 6.4 增加了三个模块，分别是：</p> 
<ul> 
 <li><strong><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdoc-snapshots.qt.io%2Fqt6-6.4%2Fqthttpserver-index.html" target="_blank">Qt HTTP Server</a></strong></li> 
 <li><strong><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdoc-snapshots.qt.io%2Fqt6-6.4%2Fqtquick3dphysics-index.html" target="_blank">Qt Quick 3D Physics</a></strong></li> 
 <li><strong><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdoc-snapshots.qt.io%2Fqtvncserver%2Findex.html" target="_blank">Qt VNC Server</a></strong></li> 
</ul> 
<p>Qt HTTP Server 和 Qt Quick 3D Physics 目前处于技术预览产品阶段。Qt HTTP Server 模块通过可选的 TLS 支持轻松地将 HTTP 服务器嵌入到应用程序中。但其文档提到，它不具备用作面向互联网的 Web 服务器的稳健性和安全性，而是专注于较小的本地/基于 LAN 的 Web 服务需求。</p> 
<p>Qt Quick 3D Physics 提供了一个高级物理模拟 API，用于与刚体和静态网格进行交互。下图是 Qt 6.4 文档包含的 Qt 3D Physics 可视化的示例：</p> 
<p><img alt src="https://oscimg.oschina.net/oscnet/up-3a2bc58d11315ad8c2f11c7fef0144d8f5a.png" referrerpolicy="no-referrer"></p> 
<p>Qt VNC Server <span><span><span><span><span style="color:#09102b"><span><span><span><span><span><span><span><span><span><span><span><span style="background-color:#ffffff"><span><span><span><span><span><span>为 Qt 6.4 提供远程 UI 功能，不过仅限于在商业许可证下的版本中使用。</span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></p> 
<p style="margin-left:0; margin-right:0; text-align:start"><span><span><span><span><span style="color:#09102b"><span><span><span><span><span><span><span><span><span><span><span><span style="background-color:#ffffff"><span><span><span><span><span><span>Qt 6.4 现有模块中也有许多重要且令人兴奋的功能，例如：</span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></p> 
<ul> 
 <li style="margin-left: 0px; margin-right: 0px; text-align: start;"><span><span><span><span><span style="color:#09102b"><span><span><span><span><span><span><span><span><span><span><span><span style="background-color:#ffffff"><span><span><span><span><span><span>用于 Qt Quick Controls 的 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdoc-snapshots.qt.io%2Fqt6-6.4%2Fqtquickcontrols2-styles.html%23ios-style" target="_blank">iOS 样式</a></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></li> 
 <li style="margin-left: 0px; margin-right: 0px; text-align: start;"><span><span><span><span><span style="color:#09102b"><span><span><span><span><span><span><span><span><span><span><span><span style="background-color:#ffffff"><span><span><span><span><span><span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdoc-snapshots.qt.io%2Fqt6-6.4%2Fqtquickcontrols2-styles.html%23ios-style" target="_blank">对 Qt Multimedia 的</a><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdoc-snapshots.qt.io%2Fqt6-6.4%2Fspatialaudiooverview.html" target="_blank">空间音频</a>支持</span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></li> 
 <li style="margin-left: 0px; margin-right: 0px; text-align: start;"><span><span><span><span><span style="color:#09102b"><span><span><span><span><span><span><span><span><span><span><span><span style="background-color:#ffffff"><span><span><span>Qt for WebAssembly 已升级为稳定版。在 Qt 6.4 中，完全支持 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdoc-snapshots.qt.io%2Fqt6-6.4%2Fwasm.html" target="_blank">Qt for WebAssembly</a> 作为一个新平台</span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></li> 
 <li style="margin-left: 0px; margin-right: 0px; text-align: start;"><span><span><span><span><span><span><span><span><span><span><span><span style="color:#121212"><span><span><span><span><span><span><span style="background-color:#ffffff"><span><span><span>其他各种改进</span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></li> 
</ul> 
<p style="margin-left:0px; margin-right:0px; text-align:start"><span><span><span><span><span><span><span><span><span><span><span><span style="color:#121212"><span><span><span><span><span><span><span style="background-color:#ffffff"><span><span><span>Qt 6.4 的目标是在 9 月底之前发布稳定版，<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.qt.io%2Fblog%2Fqt-6.4-beta-released" target="_blank">详情</a>。</span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></p>
                                        </div>
                                      
</div>
            