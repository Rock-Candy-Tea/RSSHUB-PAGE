
---
title: 'Wine 7.17 发布，Windows 应用的兼容层'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=6058'
author: 开源中国
comments: false
date: Sun, 11 Sep 2022 07:11:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=6058'
---

<div>   
<div class="content">
                                                                                            <p>Wine（Wine Is Not an Emulator）是一个能够在多种兼容 POSIX 接口的操作系统（诸如 Linux、macOS 与 BSD 等）上运行 Windows 应用的兼容层。它不是像虚拟机或者模拟器一样模仿内部的 Windows 逻辑，而是将 Windows API 调用翻译成为动态的 POSIX 调用，免除了性能和其它一些行为的内存占用，让你能够干净地整合 Windows 应用到桌面。</p> 
<p>Wine 7.17 已经正式发布，该版本中值得关注的更新内容包括：</p> 
<ul> 
 <li>DirectWrite 中对 High Unicode 字符平面映射的支持</li> 
 <li>在 Vulkan 驱动中支持 Wow64 的一些工作</li> 
 <li>各种错误修复 
  <ul> 
   <li>在 Wine 7.16 中，多个应用程序（7-Zip、WinRAR、foobar2000、内置应用程序）在非默认 DPI 下的 UI 渲染失效。</li> 
   <li>msys2 安装程序无法检查磁盘空间</li> 
   <li>Visual Studio Community 2022 安装程序在试图打开时崩溃了</li> 
   <li>当使用 GCC 构建时，winedevice.exe 退出时发生故障</li> 
   <li>Wizard101 在 7.15 中无法加载</li> 
  </ul> </li> 
</ul> 
<p>更多详情可查看：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.winehq.org%2Fnews%2F2022090901" target="_blank">https://www.winehq.org/news/2022090901</a></p>
                                        </div>
                                      
</div>
            