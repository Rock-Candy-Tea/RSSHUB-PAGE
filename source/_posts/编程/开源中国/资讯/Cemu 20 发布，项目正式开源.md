
---
title: 'Cemu 2.0 发布，项目正式开源'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=6203'
author: 开源中国
comments: false
date: Fri, 26 Aug 2022 07:10:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=6203'
---

<div>   
<div class="content">
                                                                                            <p>Cemu 是一个任天堂 Wii U 模拟器，能够运行大多数 Wii U 游戏和自制软件。它是用 C/C++ 编写的，并且正在积极开发新功能和修复，以提高兼容性、便利性和可用性。</p> 
<p>Cemu 目前仅适用于 64 位 Windows 和 Linux 设备。</p> 
<p><strong>正是从 2.0 版本开始，Cemu 在 GitHub 上正式开源。</strong></p> 
<h3>主要变化</h3> 
<ul> 
 <li>Cemu 现在正式开源</li> 
 <li>初步的 Linux 版本已经可以使用，但请注意，它现在仍然非常初步</li> 
 <li>展望未来，我们通过使用较短的版本号（2.0、2.1、2.2、2.3......）来简化版本号</li> 
 <li>更新了所有的依赖性。最明显的是 SDL（输入和运动）和 wxWidgets（用户界面）</li> 
</ul> 
<h3>其他变化</h3> 
<ul> 
 <li>修正了 H264 视频解码器中的一个崩溃</li> 
 <li>使 nsysnet 的崩溃率降低了一些，修复了《使命召唤：黑色行动 II》中的崩溃问题</li> 
 <li>修正了在非常特殊的情况下可能发生的与日志相关的崩溃。在 Wind Waker 中，如果让游戏在标题屏幕上闲置 2 分钟，就会出现这种情况。</li> 
 <li>修正了一个当 Cemu.exe 的路径包含 unicode 字符时可能发生的崩溃</li> 
 <li>修正了一个在加载 .elf homebrew 时可能发生的崩溃</li> 
 <li>标题管理器保存导出器中的账户列表不再是空的</li> 
 <li>wiimotes 的延迟现在应该会好一点了</li> 
 <li>为调试器添加了符号/函数列表+其他小型调试器/汇编器的改进。</li> 
 <li>实现了 API： <code>coreinit.FSOpenFileExAsync</code></li> 
 <li>更多的内在变化和修复</li> 
 <li>为实现停止和重启模拟功能做了一些工作。还没有准备好，但我们正在努力</li> 
</ul> 
<p>更多详情可查看：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fcemu-project%2FCemu%2Freleases%2Ftag%2Fv2.0" target="_blank">https://github.com/cemu-project/Cemu/releases/tag/v2.0</a></p> 
<p> </p>
                                        </div>
                                      
</div>
            