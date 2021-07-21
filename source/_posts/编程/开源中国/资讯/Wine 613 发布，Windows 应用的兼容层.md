
---
title: 'Wine 6.13 发布，Windows 应用的兼容层'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=5687'
author: 开源中国
comments: false
date: Wed, 21 Jul 2021 07:00:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=5687'
---

<div>   
<div class="content">
                                                                    
                                                        <p>Wine 6.13 现已发布。Wine（Wine Is Not an Emulator）是一个能够在多种兼容 POSIX 接口的操作系统（诸如 Linux、macOS 与 BSD 等）上运行 Windows 应用的兼容层。它不是像虚拟机或者模拟器一样模仿内部的 Windows 逻辑，而是将 Windows API 调用翻译成为动态的 POSIX 调用，免除了性能和其它一些行为的内存占用，让你能够干净地整合 Windows 应用到桌面。</p> 
<p><strong>主要更新内容</strong></p> 
<ul> 
 <li>修复了 CoFreeUnusedLibraries 使 COM 服务器崩溃或导致 0x800703E6/I_RpcReceive error 0x3e6 的问题</li> 
 <li>修复了 QQMusic 8.6 安装程序挂起的问题</li> 
 <li>Academagia 的对话窗口不可见，直到 alt-tabed out</li> 
 <li>修复了许多 user32:msg 测试在日语语言环境中失败的问题</li> 
 <li>多个游戏和应用程序通过 DXVA2CreateVideoService 需要 IDirectXVideoProcessorService（DXVA Checker 3.x/4.x，完美世界，Kodi）</li> 
 <li>在静态文本控件中增加对 msidbControlAttributesFormatSize 的支持，以格式化和标注 PrimaryVolumeSpaceRequired 等属性（SkySaga 安装程序）</li> 
 <li>不支持 dlclose() 函数的 C 库的解决方法 LdrUnloadDll()</li> 
 <li>Dishonored 2 Demo 在发布时崩溃</li> 
 <li>启用视觉主题时 MFC 应用程序中的工具栏背景不正确</li> 
 <li>Wine 中的 64 位 ntdll:exception 测试失败</li> 
 <li>适当的滚动条主题设计</li> 
 <li>更多关于WinSock PE转换的工作</li> 
 <li>GDI syscall接口的准备工作</li> 
 <li>IPHLPAPI PE 转换的一些进展</li> 
</ul> 
<p>详情请查看<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.winehq.org%2Fannounce%2F6.13" target="_blank">更新公告</a>。</p>
                                        </div>
                                      
</div>
            