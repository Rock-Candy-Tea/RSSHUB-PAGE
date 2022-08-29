
---
title: 'Wine 7.16 发布，Windows 应用的兼容层'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=78'
author: 开源中国
comments: false
date: Mon, 29 Aug 2022 07:18:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=78'
---

<div>   
<div class="content">
                                                                                            <p>Wine（Wine Is Not an Emulator）是一个能够在多种兼容 POSIX 接口的操作系统（诸如 Linux、macOS 与 BSD 等）上运行 Windows 应用的兼容层。它不是像虚拟机或者模拟器一样模仿内部的 Windows 逻辑，而是将 Windows API 调用翻译成为动态的 POSIX 调用，免除了性能和其它一些行为的内存占用，让你能够干净地整合 Windows 应用到桌面。</p> 
<p>Wine 7.16 已经正式发布，该版本中值得关注的更新内容包括：</p> 
<ul> 
 <li>X11 驱动中的 Wow64 支持</li> 
 <li>MSHTML 中的会话存储</li> 
 <li>MSXML 中的 Unicode 正则表达式修复</li> 
 <li>编辑控件中的 IME 改进</li> 
 <li>各种错误修复 
  <ul> 
   <li>Wine 卸载程序无法启动</li> 
   <li>postgresql installer 9.3 需要从 fso.GetTempName 返回正确的字符串长度</li> 
   <li>postgresql installer 9.3 需要支持 WshShell.Run 中的默认样式参数</li> 
   <li>amazon games app 在 wine 7.0 rc-3 (winsock?) 中崩溃</li> 
   <li>……</li> 
  </ul> </li> 
</ul> 
<p>更多详情可查看：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.winehq.org%2Fnews%2F2022082801" target="_blank">https://www.winehq.org/news/2022082801</a></p>
                                        </div>
                                      
</div>
            