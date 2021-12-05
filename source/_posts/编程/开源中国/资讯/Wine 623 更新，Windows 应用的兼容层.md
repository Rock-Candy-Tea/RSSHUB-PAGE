
---
title: 'Wine 6.23 更新，Windows 应用的兼容层'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=7052'
author: 开源中国
comments: false
date: Sun, 05 Dec 2021 07:38:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=7052'
---

<div>   
<div class="content">
                                                                    
                                                        <p style="color:#000000; margin-left:0; margin-right:0; text-align:start">Wine 是一个能够在多种兼容 POSIX 接口的操作系统（诸如 Linux、macOS 与 BSD 等）上运行 Windows 应用的兼容层。它不是像虚拟机或者模拟器一样模仿内部的 Windows 逻辑，而是将 Windows API 调用翻译成为动态的 POSIX 调用，免除了性能和其它一些行为的内存占用，让你能够干净地整合 Windows 应用到桌面。</p> 
<p style="color:#000000; margin-left:0; margin-right:0; text-align:start">Wine 6.23 已发布，可用于在 Linux、macOS 和 BSD 上运行 Windows 应用程序和游戏。接下来将是<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.phoronix.com%2Fscan.php%3Fpage%3Dsearch%26q%3DWine%2B7.0" target="_blank">Wine 7.0</a><span> </span>的候选版本，这也标志着下一个年度 Wine 稳定版本的功能冻结，在 Wine 7.0 即将到来之时，Wine 6.23 版本并没有多么令人兴奋。</p> 
<p style="color:#000000; margin-left:0; margin-right:0; text-align:start">Wine 6.23 继续将更多代码转换为 PE（可移植可执行文件）格式的低级工作，今年许多库和其他 Wine 组件都已迁移到 PE 格式， Wine 6.23 进行了一些额外的转换。此外，Wine 可以选择使用发行版的 PE 库。<br> 此版本更新如下：</p> 
<p style="color:#000000; margin-left:0; margin-right:0; text-align:start"><em>-<span> </span></em>将挂载管理器 (<span style="color:#121212"><em>Mount manager</em></span>) 和 CoreAudio 驱动程序转换为 PE。<br> - 支持 Wow64 模式下的异常处理<br> - 可以选择使用发行版的 PE 库<br> - WineDbg 中的一些 UI 改进。<br> - 各种错误修复。</p> 
<p style="color:#000000; margin-left:0; margin-right:0; text-align:start">Wine 6.23 中有 48 个已知错误修复，影响 Rockstar Game Launcher、GIMP、GTA 1997、Windows PowerShell Core 6.2 和各种其他软件，在<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.winehq.org%2F%2Fannounce%2F6.23" target="_blank">WineHQ.org 上</a><span> </span>可查看完整的 Wine 6.23 公告。Wine 7.0 第一个候选版本已计划好，并标记了代码冻结，接下来每周都会发布 Wine 7.0 的候选版本，据外媒 phoronix 预测，Wine 7.0.0 稳定版应该在 2022 年 1 月份发布。</p>
                                        </div>
                                      
</div>
            