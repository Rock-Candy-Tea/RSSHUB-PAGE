
---
title: 'Wine 7.14 发布，Windows 应用的兼容层'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=3113'
author: 开源中国
comments: false
date: Sun, 31 Jul 2022 07:08:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=3113'
---

<div>   
<div class="content">
                                                                    
                                                        <p>Wine（Wine Is Not an Emulator）是一个能够在多种兼容 POSIX 接口的操作系统（诸如 Linux、macOS 与 BSD 等）上运行 Windows 应用的兼容层。它不是像虚拟机或者模拟器一样模仿内部的 Windows 逻辑，而是将 Windows API 调用翻译成为动态的 POSIX 调用，免除了性能和其它一些行为的内存占用，让你能够干净地整合 Windows 应用到桌面。</p> 
<p>Wine 7.14 已经正式发布，该版本中值得关注的更新内容包括：</p> 
<ul> 
 <li>在 USER32 的系统调用接口方面取得了更多进展</li> 
 <li>改进了 DirectWrite 中的字体回退</li> 
 <li>一些关于套接字关闭的修复</li> 
 <li>各种错误的修复 
  <ul> 
   <li>修复《文明 4》在加载保存的游戏时崩溃</li> 
   <li>修复《毛线小精灵 2》中的崩溃</li> 
   <li>修复某些特定对话框永久全屏的问题</li> 
   <li>修复图标无法在窗口标题栏中正确呈现的问题</li> 
   <li>修复无法使用 CJK 输入法输入任何内容的问题</li> 
   <li>修复在 NtUserDrawCaptionTemp() 中使用了错误字体的问题</li> 
   <li>……</li> 
  </ul> </li> 
</ul> 
<p>更多详情可查看：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.winehq.org%2Fannounce%2F7.14" target="_blank">https://www.winehq.org/announce/7.14</a></p>
                                        </div>
                                      
</div>
            