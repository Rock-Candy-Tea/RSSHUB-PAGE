
---
title: 'KDE Plasma 5.23.3 发布，11 月的 Bug 修复版本'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://oscimg.oschina.net/oscnet/up-cc6aca1beee792604470a6ba99d8556645c.png'
author: 开源中国
comments: false
date: Wed, 10 Nov 2021 07:13:00 GMT
thumbnail: 'https://oscimg.oschina.net/oscnet/up-cc6aca1beee792604470a6ba99d8556645c.png'
---

<div>   
<div class="content">
                                                                                            <p><span style="background-color:#ffffff; color:#333333">KDE Plasma 5.23.3 现已发布，该版本是 KDE Plasma 5 的错误修复更新，包含许多功能改进和新模块以完善桌面体验。</span></p> 
<p><span style="background-color:#ffffff; color:#333333"><img alt height="784" src="https://oscimg.oschina.net/oscnet/up-cc6aca1beee792604470a6ba99d8556645c.png" width="1588" referrerpolicy="no-referrer"></span></p> 
<h4 style="margin-left:0; margin-right:0; text-align:left">Breeze</h4> 
<ul style="list-style-type:disc; margin-left:0; margin-right:0"> 
 <li>Kstyle：将 QFocusFrame 添加到非视图/委托交互小部件</li> 
</ul> 
<h4>kwayland-server</h4> 
<ul> 
 <li>正确应用初始 xdg-shell 双缓冲状态</li> 
 <li>修复 SlideInterface 的所有权</li> 
 <li>仅当 dnd 操作更改时才发出 DataOfferInterface::dragAndDropActionsChanged()</li> 
</ul> 
<h4 style="margin-left:0; margin-right:0; text-align:left">KWin</h4> 
<ul style="list-style-type:disc; margin-left:0; margin-right:0"> 
 <li>Wayland：当首选装饰模式更改时检查工作区位置</li> 
 <li>DecorationItem：防止崩溃</li> 
 <li> [wayland] 修复忽略的键盘 RepeatRate</li> 
 <li>RenderLoop：限制全屏窗口的重绘调度</li> 
 <li>Wayland：修复在切换装饰后产生的 Wayland 窗口</li> 
 <li>使用 QScopedPointer 来存储装饰对象</li> 
 <li>Scripts/minimizeall：尝试保留最后一个活动窗口</li> 
 <li>截屏：当平台无法提供纹理时不再崩溃</li> 
</ul> 
<h4>libksysguard</h4> 
<ul> 
 <li>修复 ksgrd_network_helper 在失败后退出时崩溃的问题</li> 
 <li>修复 ConnectionMapping 中不正确的字符串终止</li> 
</ul> 
<h4 style="margin-left:0; margin-right:0; text-align:left">Plasma Desktop</h4> 
<ul style="list-style-type:disc; margin-left:0; margin-right:0"> 
 <li>键盘布局：修复菜单中缺少的世界语标志图标</li> 
 <li>启动：在 TapHandler 中不接受手写笔</li> 
 <li>草案：修复 LayoutManager.insertAtCoordinates 的问题</li> 
 <li>开始动画时不要不必要地重置面板不透明度</li> 
 <li>Foldermodel：在 Plasma 文件夹视图中将覆盖层拖放到图标上</li> 
 <li>Plasma-desktop runner：修复显示交互式等离子/kwin 控制台</li> 
 <li>启动：修复拖放导致代理重置为 0 X 位置和重叠</li> 
</ul> 
<h4 style="margin-left:0; margin-right:0; text-align:left">Plasma 浏览器集成</h4> 
<ul style="list-style-type:disc; margin-left:0; margin-right:0"> 
 <li>[History Runner] 跳过 blob URL</li> 
</ul> 
<h4 style="margin-left:0; margin-right:0; text-align:left">Plasma Workspace</h4> 
<ul style="list-style-type:disc; margin-left:0; margin-right:0"> 
 <li>修复了对 osd 的大小提示</li> 
 <li>使用隐式大小不会导致绑定循环</li> 
 <li>Wayland：不要为占位符屏幕创建 DesktopView</li> 
 <li>[startplasma] 检测处于链接状态的 systemd 服务</li> 
 <li>断开 xdgActivationTokenArrived 的观察者</li> 
 <li>Interactiveconsole：允许从命令行参数指定模式</li> 
</ul> 
<p>详情请查看<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fkde.org%2Fannouncements%2Fchangelogs%2Fplasma%2F5%2F5.23.2-5.23.3%2F" target="_blank">更新公告</a>。</p> 
<p> </p>
                                        </div>
                                      
</div>
            