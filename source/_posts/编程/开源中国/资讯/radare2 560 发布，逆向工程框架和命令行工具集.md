
---
title: 'radare2 5.6.0 发布，逆向工程框架和命令行工具集'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=715'
author: 开源中国
comments: false
date: Tue, 15 Feb 2022 07:42:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=715'
---

<div>   
<div class="content">
                                                                                            <p>radare2 是 radare 的一个重写版本，是一个逆向工程框架和命令行工具集，可以用来简化逆向工程任务。</p> 
<p style="color:#000000; margin-left:0; margin-right:0; text-align:start">radare2 5.6.0 现已发布，主要更新内容包括：</p> 
<p style="text-align:start"><strong>Highlights</strong></p> 
<div> 
 <div> 
  <ul> 
   <li><span style="background-color:#ffffff; color:#24292f">ABI breaks</span><span><span><span><span><span><span><span style="background-color:var(--color-canvas-default)"><span><span><span><span><span><span> - RAnal api 是 RAsm 插件的 new home，减少安装大小</span></span></span></span></span></span></span></span></span></span></span></span></span></li> 
   <li><span><span><span><span><span><span><span style="background-color:var(--color-canvas-default)"><span><span><span><span><span><span>在纯 C 中添加一个初始的、可运行的本地 r2pm 的重新实现（不需要 posix shell）</span></span></span></span></span></span></span></span></span></span></span></span></span> 
    <ul> 
     <li><span><span><span><span><span><span><span style="background-color:var(--color-canvas-default)"><span><span><span><span><span><span>Windows 支持将在以后提供，需要更多测试和用户反馈。</span></span></span></span></span></span></span></span></span></span></span></span></span></li> 
    </ul> </li> 
   <li><span><span><span><span><span><span><span style="background-color:var(--color-canvas-default)"><span><span><span><span><span><span>支持线程的初始版本（目前支持每个线程一个 RCore）</span></span></span></span></span></span></span></span></span></span></span></span></span> 
    <ul> 
     <li><span><span><span><span><span><span><span style="background-color:var(--color-canvas-default)"><span><span><span><span><span><span>删除或制作 TLS 全局变量、添加 atomic 支持、修复互斥和线程</span></span></span></span></span></span></span></span></span></span></span></span></span></li> 
     <li><span><span><span><span><span><span><span style="background-color:var(--color-canvas-default)"><span><span><span><span><span><span>r2r 测试套件现在可以在启用线程清理器的情况下运行构建</span></span></span></span></span></span></span></span></span></span></span></span></span></li> 
     <li><span><span><span><span><span><span><span style="background-color:var(--color-canvas-default)"><span><span><span><span><span><span>删除所有<code>sdb_fmt</code>使用以换取线程安全的<code>r_strf</code></span></span></span></span></span></span></span></span></span></span></span></span></span></li> 
    </ul> </li> 
   <li><span><span><span><span><span><span><span style="background-color:var(--color-canvas-default)"><span><span><span><span><span><span>更多 ESIL 测试并提高 x86、arm64、riscv、v850 等的质量！</span></span></span></span></span></span></span></span></span></span></span></span></span></li> 
   <li><span><span><span><span><span><span><span style="background-color:var(--color-canvas-default)"><span><span><span><span><span><span>改进了可用性并修复了面板中的一些错误交互，更好的帮助消息和改进的颜色主题。</span></span></span></span></span></span></span></span></span></span></span></span></span></li> 
   <li><span><span><span><span><span><span><span style="background-color:var(--color-canvas-default)"><span><span><span><span><span><span>支持最新的 capstone，并倾向于系统范围的安装以获得更好的离线构建</span></span></span></span></span></span></span></span></span></span></span></span></span></li> 
   <li><span><span><span><span><span><span><span style="background-color:var(--color-canvas-default)"><span><span><span><span><span><span>在沙盒模式下添加项目加载并添加<code>dirty</code>bit 以避免在没有任何更改时保存内容。</span></span></span></span></span></span></span></span></span></span></span></span></span></li> 
   <li><span><span><span><span><span><span><span style="background-color:var(--color-canvas-default)"><span><span><span><span><span><span>新命令：</span></span></span></span></span></span></span></span></span></span></span></span></span><span style="background-color:#ffffff; color:#24292f">pdu, r-/r+, fc, aafs, pcc, /aF, isqq.<span> </span></span><code>iS,</code><span style="background-color:#ffffff; color:#24292f">,<span> </span></span><code>axl</code><span style="background-color:#ffffff; color:#24292f">,<span> </span></span><code>/e</code><span style="background-color:#ffffff; color:#24292f">,<span> </span></span><code>pFB</code><span style="background-color:#ffffff; color:#24292f">,<span> </span></span><code>ws#</code><span><span><span><span><span><span><span style="background-color:var(--color-canvas-default)"><span><span><span><span><span><span>以支持更多的 pascal 字符串类型</span></span></span></span></span></span></span></span></span></span></span></span></span></li> 
   <li><span><span><span><span><span><span><span style="background-color:var(--color-canvas-default)"><span><span><span><span><span><span>二进制 PLIST printing (pFB) 与 (pFA - for android binary xml) 结合得很好</span></span></span></span></span></span></span></span></span></span></span></span></span></li> 
   <li><span><span><span><span><span><span><span style="background-color:var(--color-canvas-default)"><span><span><span><span><span><span>使用<code>aafs</code>和<code>sixref</code>将分析速度提高几个数量级</span></span></span></span></span></span></span></span></span></span></span></span></span></li> 
   <li><span><span><span><span><span><span><span style="background-color:var(--color-canvas-default)"><span><span><span><span><span><span>在 hexdump 和 disasm 中的指令标记化中使用 Honor flag colors</span></span></span></span></span></span></span></span></span></span></span></span></span></li> 
   <li><span><span><span><span><span><span><span style="background-color:var(--color-canvas-default)"><span><span><span><span><span><span>修复自 5.5.4 以来的 3 个 CVE、大量内存泄漏和所有覆盖性的关键问题</span></span></span></span></span></span></span></span></span></span></span></span></span> 
    <ul> 
     <li><span><span><span><span><span><span><span style="background-color:var(--color-canvas-default)"><span><span><span><span><span><span>通过使用新工具和 stdint 基本类型提高代码质量</span></span></span></span></span></span></span></span></span></span></span></span></span></li> 
    </ul> </li> 
   <li><span><span><span><span><span><span><span style="background-color:var(--color-canvas-default)"><span><span><span><span><span><span>支持原生 arm64 linux 主机上的 arm32 调试</span></span></span></span></span></span></span></span></span></span></span></span></span></li> 
   <li><span><span><span><span><span><span><span style="background-color:var(--color-canvas-default)"><span><span><span><span><span><span>将脚本支持扩展到 quickjs 和 wren 编程语言</span></span></span></span></span></span></span></span></span></span></span></span></span></li> 
   <li><span><span><span><span><span><span><span style="background-color:var(--color-canvas-default)"><span><span><span><span><span><span>将<code>time</code>测量指令添加到<code>rarun2</code></span></span></span></span></span></span></span></span></span></span></span></span></span></li> 
   <li><span><span><span><span><span><span><span style="background-color:var(--color-canvas-default)"><span><span><span><span><span><span>添加 Rabin Karp 更快的搜索算法 (/e) 并修复搜索循环中的一些错误</span></span></span></span></span></span></span></span></span></span></span></span></span></li> 
   <li><span><span><span><span><span><span><span style="background-color:var(--color-canvas-default)"><span><span><span><span><span><span>添加新的 Arch 插件：loongarch、evm.cs、v850.np 和 chip8</span></span></span></span></span></span></span></span></span></span></span></span></span></li> 
  </ul> 
 </div> 
</div> 
<p>更新说明：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fradareorg%2Fradare2%2Freleases%2Ftag%2F5.6.0" target="_blank">https://github.com/radareorg/radare2/releases/tag/5.6.0</a> </p>
                                        </div>
                                      
</div>
            