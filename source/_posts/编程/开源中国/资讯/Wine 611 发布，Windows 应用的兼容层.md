
---
title: 'Wine 6.11 发布，Windows 应用的兼容层'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=9972'
author: 开源中国
comments: false
date: Sun, 20 Jun 2021 07:01:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=9972'
---

<div>   
<div class="content">
                                                                    
                                                        <p>Wine（Wine Is Not an Emulator）是一个能够在多种兼容 POSIX 接口的操作系统（诸如 Linux、macOS 与 BSD 等）上运行 Windows 应用的兼容层。它不是像虚拟机或者模拟器一样模仿内部的 Windows 逻辑，而是将 Windows API 调用翻译成为动态的 POSIX 调用，免除了性能和其它一些行为的内存占用，让你能够干净地整合 Windows 应用到桌面。</p> 
<p>Wine 6.11 已经正式发布，该版本的新增内容包括：</p> 
<ul> 
 <li>在所有内置程序中支持主题；</li> 
 <li>从 Musl 导入的所有剩余 CRT 数学函数；</li> 
 <li>MP3 支持在 macOS 上也需要 libmpg123；</li> 
 <li>支持代码页 720；</li> 
 <li>各种错误修复； 
  <ul> 
   <li>msvcrt/string 测试在 valgrind 下失败；</li> 
   <li>Excel 2007 需要 ICreateTypeInfo2::DeleteFuncDesc() ；</li> 
   <li>多款游戏因从 Musl 导入 logf 而导致渲染问题；</li> 
   <li>ZynAddSubFX 3.0.3 Demo 无法加载/打开/保存预设；</li> 
   <li>Otvdm 无法启动任何 Win16 应用程序；</li> 
   <li>……</li> 
  </ul> </li> 
</ul> 
<p>更多详情可查看：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.winehq.org%2Fannounce%2F6.11" target="_blank">https://www.winehq.org/announce/6.11</a></p>
                                        </div>
                                      
</div>
            