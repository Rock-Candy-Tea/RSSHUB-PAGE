
---
title: 'Wine 7.0-rc5 发布，Windows 应用的兼容层'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=5662'
author: 开源中国
comments: false
date: Wed, 12 Jan 2022 23:42:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=5662'
---

<div>   
<div class="content">
                                                                                            <p>Wine（Wine Is Not an Emulator）是一个能够在多种兼容 POSIX 接口的操作系统（诸如 Linux、macOS 与 BSD 等）上运行 Windows 应用的兼容层。它不是像虚拟机或者模拟器一样模仿内部的 Windows 逻辑，而是将 Windows API 调用翻译成为动态的 POSIX 调用，免除了性能和其它一些行为的内存占用，让你能够干净地整合 Windows 应用到桌面。</p> 
<p>Wine 7.0-rc5 已经发布，这是一个错误修复版本，其目前已处于代码冻结状态。</p> 
<p><strong>Bugs fixed in 7.0-rc3：</strong></p> 
<ul> 
 <li style="text-align:start"><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fbugs.winehq.org%2Fshow_bug.cgi%3Fid%3D23782" target="_blank">23782</a>  Spaceforce Rogue Universe：无法进入游戏（介绍视频循环播放）</li> 
 <li style="text-align:start"><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fbugs.winehq.org%2Fshow_bug.cgi%3Fid%3D41239" target="_blank">41239</a>  FUEL 因着色器验证失败而在启动时中止</li> 
 <li style="text-align:start"><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fbugs.winehq.org%2Fshow_bug.cgi%3Fid%3D46841" target="_blank">46841</a>  ASC Paint Shop Pro 8.x 和 9.x 启动时崩溃（msvcrt c++ 异常处理）</li> 
 <li style="text-align:start"><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fbugs.winehq.org%2Fshow_bug.cgi%3Fid%3D48084" target="_blank">48084</a>  Crouzet Soft 1.11 在启动时崩溃</li> 
 <li style="text-align:start"><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fbugs.winehq.org%2Fshow_bug.cgi%3Fid%3D49099" target="_blank">49099</a>  一次性向所有设备发送 MIDI events</li> 
 <li style="text-align:start"><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fbugs.winehq.org%2Fshow_bug.cgi%3Fid%3D49174" target="_blank">49174</a>  在 mshtml/htmlwindow.c 中重复检查 iter->parent</li> 
 <li style="text-align:start"><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fbugs.winehq.org%2Fshow_bug.cgi%3Fid%3D50100" target="_blank">50100</a>  无法登录 Bentley CONNECTION 客户端(需要'let'语句支持)</li> 
 <li style="text-align:start"><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fbugs.winehq.org%2Fshow_bug.cgi%3Fid%3D50527" target="_blank">50527</a>  Dying Light 在开始新游戏后显示黑屏</li> 
 <li style="text-align:start"><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fbugs.winehq.org%2Fshow_bug.cgi%3Fid%3D51805" target="_blank">51805</a>  Tropico 2：鼠标光标为黑色</li> 
 <li style="text-align:start"><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fbugs.winehq.org%2Fshow_bug.cgi%3Fid%3D51829" target="_blank">51829</a>  Roblox Player：在加载过程中长时间冻结</li> 
 <li style="text-align:start"><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fbugs.winehq.org%2Fshow_bug.cgi%3Fid%3D52042" target="_blank">52042</a>  Ketarin 在 WINE 6.21 THREAD 从 RUNNING 过渡到 DONE_BLOCKING 时崩溃了</li> 
 <li style="text-align:start"><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fbugs.winehq.org%2Fshow_bug.cgi%3Fid%3D52071" target="_blank">52071</a>  mshtml:script 在 Windows 的 externalDisp_InvokeEx() 中 fails</li> 
 <li style="text-align:start"><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fbugs.winehq.org%2Fshow_bug.cgi%3Fid%3D52142" target="_blank">52142</a>  在 Wine 6.22 中的 Ketarin Listview error unknown msg</li> 
 <li style="text-align:start"><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fbugs.winehq.org%2Fshow_bug.cgi%3Fid%3D52143" target="_blank">52143</a>  mscoree:parse_startup 在 Wine 上的 Ketarin 错误</li> 
 <li style="text-align:start"><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fbugs.winehq.org%2Fshow_bug.cgi%3Fid%3D52144" target="_blank">52144</a>  Ketarin stops refreshing program window on Wine 6.22</li> 
 <li style="text-align:start"> <p style="margin-left:0px; margin-right:0px; text-align:start"><span><span><span><span><span><span><span style="color:#000000"><span><span><span style="background-color:#ffffff"><span><span><span><span><span><span><span><span><span><span><span><span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fbugs.winehq.org%2Fshow_bug.cgi%3Fid%3D52157" target="_blank">52157</a>  ntdll:wow64 在 64 位 Wine 上失效</span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></p> </li> 
 <li style="text-align:start"> <p style="margin-left:0px; margin-right:0px; text-align:start"><span><span><span><span><span><span><span style="color:#000000"><span><span><span style="background-color:#ffffff"><span><span><span><span><span><span><span><span><span><span><span><span>......</span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></p> </li> 
</ul> 
<p style="margin-left:0px; margin-right:0px; text-align:start">详情可查看：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.winehq.org%2Fannounce%2F7.0-rc5" target="_blank">https://www.winehq.org/announce/7.0-rc5</a></p>
                                        </div>
                                      
</div>
            