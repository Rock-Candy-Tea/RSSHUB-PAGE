
---
title: 'Arduino IDE 1.8.15 发布'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=4880'
author: 开源中国
comments: false
date: Mon, 17 May 2021 23:29:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=4880'
---

<div>   
<div class="content">
                                                                    
                                                        <p>Arduino 是一个开源的物理计算平台，基于一个简单的 I/O 板和一个实现处理/连接语言的开发环境。Arduino 可以用来开发独立的交互式对象，也可以连接到计算机上的软件（如 Flash、Processing 和 MaxMSP）。</p> 
<p>Arduino IDE 是一个跨平台的应用程序（适用于 Windows、macOS、Linux），是用 C 和 C++ 编写的。它被用来编写和上传程序到 Arduino 兼容板，而且在第三方内核的帮助下，也可用于其他厂商的开发板。</p> 
<p>Arduino IDE 1.8.15 正式发布，自 1.8.13 版本以来的变化包括：</p> 
<p><strong>修补程序：</strong></p> 
<ul> 
 <li>修复了库发现中的回归问题（在某些平台上未能编译捆绑的库）</li> 
</ul> 
<p><strong>IDE：</strong></p> 
<ul> 
 <li>修复了状态栏自定义板（status bar custom board）偏好设置消失的问题；</li> 
 <li>Boards 管理器错误修正：有时在输入搜索词后出现 "安装" 按钮而不是 "更新"；</li> 
 <li>Libraries/Boards 管理器：安装/卸载后，类型和类别过滤器被保留；</li> 
 <li>在 Board 管理器中增加了 "过时" 标签支持，标记为过时的平台将显示在列表底部；</li> 
 <li>Serial Plotter：行尾的下拉菜单现会遵循全局偏好的设置；</li> 
 <li>Libraries 管理器：显示维护者而不是作者；</li> 
 <li>Firmware 更新程序：增加了新的固件和对 Nano RP2040 Connect 的支持；</li> 
 <li>Boards 管理器：如果从首选项中删除了原始 URL，缓存的第三方 package_index.json 不再被删除，这使得其他工具（如arduino-cli）在不同的 URL 配置下都可以正常工作；</li> 
 <li>board 配置子菜单现在可以滚动了；</li> 
 <li>新的快捷方式：在 Serial Monitor 按钮上 Shift+click 将打开 Serial Plotter；</li> 
 <li>修正了没有选择 board 时的 NPE；</li> 
</ul> 
<p><strong>arduino-builder：</strong></p> 
<ul> 
 <li>改进了 lib 检测：检查 <a href="https://www.oschina.net/action/GoToLink?url=http%3A%2F%2Flibrary.properties" target="_blank">library.properties</a> 中是否有匹配的名字；</li> 
 <li>修复了发现无效的 build.options.json 时的编译问题；</li> 
 <li>改进了 sketch 中 .cpp/.h 文件的错误信息；</li> 
</ul> 
<p>更多详情可查看：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Farduino%2FArduino%2Freleases" target="_blank">https://github.com/arduino/Arduino/releases</a></p>
                                        </div>
                                      
</div>
            