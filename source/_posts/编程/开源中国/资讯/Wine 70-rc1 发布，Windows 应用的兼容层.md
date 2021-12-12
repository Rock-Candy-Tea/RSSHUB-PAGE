
---
title: 'Wine 7.0-rc1 发布，Windows 应用的兼容层'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=1481'
author: 开源中国
comments: false
date: Sun, 12 Dec 2021 07:34:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=1481'
---

<div>   
<div class="content">
                                                                                            <p>Wine（Wine Is Not an Emulator）是一个能够在多种兼容 POSIX 接口的操作系统（诸如 Linux、macOS 与 BSD 等）上运行 Windows 应用的兼容层。它不是像虚拟机或者模拟器一样模仿内部的 Windows 逻辑，而是将 Windows API 调用翻译成为动态的 POSIX 调用，免除了性能和其它一些行为的内存占用，让你能够干净地整合 Windows 应用到桌面。</p> 
<p>Wine 7.0-rc1 已经发布，这是即将发布的 Wine 7.0 的第一个候选版本，该版本中值得关注的更新内容包括：</p> 
<ul> 
 <li>重新实现了 WinMM 操纵杆驱动程序。</li> 
 <li>所有 Unix 库转换为基于 syscall 的接口。</li> 
 <li>各种错误的修正： 
  <ul> 
   <li>scrrun：文件系统的 BOM 测试在韩文和中文环境下失败。</li> 
   <li>《盗贼之海》进入游戏大厅时崩溃</li> 
   <li>在 Wine 中，GetFileVersionInfoEx() 的检查在非英语区中失败。</li> 
   <li>带有多个 <code>=</code> 的 winegcc 选项没有被正确处理</li> 
   <li>NIK Dfine2 崩溃/挂起（以前可以正常工作）</li> 
   <li>winedbg 命令行参数未正确引用</li> 
   <li>cMUD 3.34 安装程序崩溃</li> 
   <li>……</li> 
  </ul> </li> 
</ul> 
<p>更多详情可查看：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.winehq.org%2Fannounce%2F7.0-rc1" target="_blank">https://www.winehq.org/announce/7.0-rc1</a></p>
                                        </div>
                                      
</div>
            