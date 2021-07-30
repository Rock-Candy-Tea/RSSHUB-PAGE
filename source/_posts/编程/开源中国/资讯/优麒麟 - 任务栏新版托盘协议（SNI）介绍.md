
---
title: '优麒麟 - 任务栏新版托盘协议（SNI）介绍'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://www.ubuntukylin.com/upload/202107/1627545300522364.png'
author: 开源中国
comments: false
date: Thu, 29 Jul 2021 18:37:00 GMT
thumbnail: 'https://www.ubuntukylin.com/upload/202107/1627545300522364.png'
---

<div>   
<div class="content">
                                                                                            <p style="text-align:center"><img alt="优麒麟（Ubuntu Kylin）" height="55" src="https://www.ubuntukylin.com/upload/202107/1627545300522364.png" width="405" referrerpolicy="no-referrer"></p> 
<p><strong>在 Linux 操作系统中，“系统托盘区域”是在给定的 X 屏幕上运行的应用程序，可以显示正在运行的应用程序提供的小图标。系统托盘是一个 X 客户端，在给定的屏幕上拥有一个特殊的管理器选择并提供了容器窗口。Windows 将此功能称为“通知区域”，旧版托盘协议就是通过 X 服务直接获取应用信息，在开发上难度很大。</strong></p> 
<p>新版托盘规范定义了可视项的管理，通常是用于向用户报告应用程序状态或提供对该应用程序执行的常见操作的快速访问的图标。它旨在作为 Freedesktop 的桌面通知规范的补充但不直接相关，旨在替代 Freedesktop 系统托盘规范，更加面向模型视图，为工作区提供更多自由，如何以图形方式表示与它的视觉风格语言，这种方式（SNI）是将 systemtray 的调用封装进 dbus 总线中，提升了开发者的开发效率。</p> 
<p>从用户角度来看新版托盘协议（SNI）从表面上看不出有什么太大的变化，在开发的角度上是将最上层的应用与下层基础库的分离。</p> 
<p style="text-align:center"><img alt="优麒麟（Ubuntu Kylin）" height="46" src="https://www.ubuntukylin.com/upload/202107/1627545341466943.png" width="285" referrerpolicy="no-referrer"></p> 
<p style="text-align:center"><img alt="优麒麟（Ubuntu Kylin）" height="63" src="https://www.ubuntukylin.com/upload/202107/1627545357674201.png" width="211" referrerpolicy="no-referrer"></p> 
<p>新版托盘协议主要是通过三个库来实现的：</p> 
<p>dbusmenu 是实现应用程序和面板（#5）之间传输协议的库。dbusmenu 已经被用于开发会话菜单，并且也是在 Lucid 中实现一些新系统菜单的构建块。</p> 
<p>indicator-applet 是将托管应用程序指示器区域的面板小程序。指示器小程序是作为消息菜单项目的一部分开发的，旨在成为面板指示器的通用容器 。libappindicator 是一个新的库，用于帮助应用程序端更改；它确实注册了图标和菜单，并在内部使用 dbusmenu 通过 dbus 发布上下文菜单。虽然它是 Gnome 桌面的新库，但它基于在 KDE 项目中设计的用于更新系统托盘协议的协议（上面的“信令协议”部分）。libappindicator 采用并扩展了该协议，并将其与 dbusmenu 连接以提供应用程序迁移其代码所需的全套服务 。</p> 
<p style="text-align:center"><img alt="优麒麟（Ubuntu Kylin）" height="63" src="https://www.ubuntukylin.com/upload/202107/1627545388432684.png" width="235" referrerpolicy="no-referrer"></p> 
<p><span style="color:#0070c0"><strong><span style="background-color:#ffffff">3.1 托盘应用托盘封装</span></strong></span></p> 
<p>通过 dbusmenu，indicator-applet，libappindicator 将托盘应用的属性，方法，以及信号注册到 dbus 总线上，在任务栏上进行 dbus 监听解析来实现与托盘应用交互。</p> 
<p style="text-align:center"><img alt="优麒麟（Ubuntu Kylin）" height="142" src="https://www.ubuntukylin.com/upload/202107/1627545524614169.png" width="645" referrerpolicy="no-referrer"></p> 
<p> </p> 
<p>注册 item 的方法有：</p> 
<p style="text-align:center"><img alt="优麒麟（Ubuntu Kylin）" height="171" src="https://www.ubuntukylin.com/upload/202107/1627545541228876.png" width="384" referrerpolicy="no-referrer"></p> 
<p>属性有：</p> 
<p style="text-align:center"><img alt="优麒麟（Ubuntu Kylin）" height="495" src="https://www.ubuntukylin.com/upload/202107/1627545559943936.png" width="685" referrerpolicy="no-referrer"></p> 
<p>信号有：</p> 
<p style="text-align:center"><img alt="优麒麟（Ubuntu Kylin）" height="236" src="https://www.ubuntukylin.com/upload/202107/1627545581579337.png" width="519" referrerpolicy="no-referrer"></p> 
<p><strong><span style="color:#0070c0">3.2 注册 dbus 服务</span></strong></p> 
<p>当拿到了托盘应用的信息然后就需要对信息进行封装通过 dbus 的方式发送给任务栏，在任务栏上会注册一个 statusnotifierWatcher 的服务用来检测托盘信息的，每当托盘应用打开的时候都会调用 statusnotifierWatcher 的 RegisterStatusNotifierItem 方法在任务栏的托盘区域进行按钮的注册，当托盘应用关闭的时候会调用任务栏 unRegisterStatusNotifierItem 方法来取消在任务栏上的注册。</p> 
<p><strong><span style="color:#0070c0">3.3 调用 dbus 的方法</span></strong></p> 
<p>当用户对托盘应用进行操作的时候，会调用相应 dbus 方法，并激活相关事件。例如左键点击会触发“激活窗口”的事件，右键单击会触发“显示右键菜单”的事件，悬浮会触发“显示提示语”的事件</p> 
<p style="text-align:center"><img alt="优麒麟（Ubuntu Kylin）" height="59" src="https://www.ubuntukylin.com/upload/202107/1627545860685131.png" width="279" referrerpolicy="no-referrer"></p> 
<p><strong><span style="color:#0070c0">4.1 注册 statusnotifierHost 的 dbus</span></strong></p> 
<p>在一个桌面上为了防止托盘应用会在多个地方注册成托盘，用一个 dbus 来让托盘应用只能注册到一个托盘来确保不会出现功能上不稳定。</p> 
<p><strong><span style="color:#0070c0">4.2 注册 statusnotifierWatch 的 dbus</span></strong></p> 
<p>用来检测托盘应用的打开和关闭，statusnotifierWatch 的 RegisterStatusNotifierItem 和 unRegisterStatusNotifierItem 是协议层与应用层来进行交互的信号，通过 RegisterStatusNotifierItem 方法来获取应用注册的 dbus 的服务名。</p> 
<p><strong><span style="color:#0070c0">4.3 对托盘应用的 dbus 进行调用</span></strong></p> 
<p>上文说的鼠标事件点击调用槽函数是一部分，还可以监听托盘应用的 signal 如图标变换，提示信息变化等。如果需要托盘应用的窗口以及其他属性，还可以通过 dbus 来获取 properties。</p> 
<p><strong><span style="color:#0070c0">4.4 在优麒麟桌面环境下使用</span></strong></p> 
<p>Qt 应用程序可以在自己的应用程序里创建一个 QSystemtrayIcon 类，并为这个类似设置图标和事件槽函数，在任务栏上会自动生成托盘图标。</p> 
<p>Gtk 程序通过</p> 
<p style="text-align:center"><img alt="优麒麟（Ubuntu Kylin）" height="84" src="https://www.ubuntukylin.com/upload/202107/1627546005190187.png" width="688" referrerpolicy="no-referrer"></p> 
<p>来注册应用为托盘应用，即可实现在任务栏上显示托盘图标。</p> 
<p style="text-align:center"><img alt="优麒麟（Ubuntu Kylin）" height="58" src="https://www.ubuntukylin.com/upload/202107/1627546021543318.png" width="194" referrerpolicy="no-referrer"></p> 
<p><strong><span style="color:#0070c0">5.1</span></strong> 在 dbus 调用的时候可能会出现延时，必要的话可以考虑多线程处理，避免界面阻塞。</p> 
<p><span style="color:#0070c0"><strong>5.2</strong></span> 由于 dbus 调用是异步调用出现响应慢问题，在读取托盘应用信息是可能会需要添加延时读取，不然会出现信息读取不到的地方。</p>
                                        </div>
                                      
</div>
            