
---
title: 'Wine 6.0.1 发布，Windows 应用的兼容层'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=5930'
author: 开源中国
comments: false
date: Tue, 08 Jun 2021 06:16:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=5930'
---

<div>   
<div class="content">
                                                                    
                                                        <p>Wine（Wine Is Not an Emulator）是一个能够在多种兼容 POSIX 接口的操作系统（诸如 Linux、macOS 与 BSD 等）上运行 Windows 应用的兼容层。它不是像虚拟机或者模拟器一样模仿内部的 Windows 逻辑，而是将 Windows API 调用翻译成为动态的 POSIX 调用，免除了性能和其它一些行为的内存占用，让你能够干净地整合 Windows 应用到桌面。</p> 
<p>Wine 6.0.1 已经正式发布，该版本的新增内容包括：</p> 
<ul> 
 <li>py2exe 需要部分 imagehlp.BindImageEx 实现</li> 
 <li>修复 RTG Bills 2.x （VB6 应用程序）在启动时报告 "ADO error 1BD Object doesn't support this action"（msado15 'connection_GetIDsOfNames' 是一个存根）的问题</li> 
 <li>黑暗地带没有声音</li> 
 <li>Earth 2160 (GOG.com) 无法识别序列号</li> 
 <li>Wine File Explorer 的树在点击加 '+' 号时不能展开</li> 
 <li>猎鹿人演示：无法启动新游戏（地图视图无法使用）</li> 
 <li>影子武士2：地板没有被渲染出来</li> 
 <li>RPCS3 模拟器由于 'kernel32.SetFileInformationByHandle' 缺乏对 'FileEndOfFileInfo' 信息类的支持而崩溃</li> 
 <li>Process Hacker 不能列举手柄</li> 
 <li>来自 Google sandbox-attacksurface-analysis-tools v1.1.x 的 CommonObjects 工具（.NET应用）需要 'ntdll.NtQuerySystemInformation' 以支持 'SystemExtendedHandleInformation'</li> 
 <li>VarFormatCurrency 不能处理已经格式化的字符串</li> 
 <li>基于 Macromedia Director Player 4.x 的游戏（16 位 NE）无法运行</li> 
 <li>多个应用程序在启动时显示黑色客户端区域（Wargaming.net Game Center，基于 Electron 的应用程序）</li> 
 <li>Aldi (Buhl) Steuer 2019/2020 安装程序崩溃</li> 
 <li>在虚拟机中使用 winemac.drv 时找不到显示器</li> 
</ul> 
<p>详情请查看<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.winehq.org%2Fannounce%2F6.0.1" target="_blank">更新公告</a>。</p> 
<p> </p>
                                        </div>
                                      
</div>
            