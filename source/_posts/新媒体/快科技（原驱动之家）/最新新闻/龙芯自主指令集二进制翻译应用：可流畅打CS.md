
---
title: '龙芯自主指令集二进制翻译应用：可流畅打CS'
categories: 
 - 新媒体
 - 快科技（原驱动之家）
 - 最新新闻
headimg: 'https://img1.mydrivers.com/img/20211109/54aff372-08d6-4ec1-bc9b-3da54ce02d9b.jpg'
author: 快科技（原驱动之家）
comments: false
date: Tue, 09 Nov 2021 20:35:49 GMT
thumbnail: 'https://img1.mydrivers.com/img/20211109/54aff372-08d6-4ec1-bc9b-3da54ce02d9b.jpg'
---

<div>   
<p>龙芯中科宣布，推出基于自主指令系统LoongArch的二进制翻译应用解决方案，二进制翻译为核心技术，旨在消除指令壁垒，实现不同平台软件的兼容运行。</p>
<p><strong>支持场景包括MIPS、x86、ARM平台上厂商已停止支持的老旧软硬件，以及厂商无法提供充分技术支持的商业闭源软件。</strong></p>
<p style="text-align: center;"><img alt="龙芯自主指令集二进制翻译应用：可流畅打CS" h="512" src="https://img1.mydrivers.com/img/20211109/54aff372-08d6-4ec1-bc9b-3da54ce02d9b.jpg" style="text-align: center; border: 1px solid black;" w="600" referrerpolicy="no-referrer"></p>
<p>官方称，龙芯架构具有完全自主、技术先进、兼容生态三方面特点，<strong>LoongArch指令集也在设计之初就充分考虑了生态兼容需求</strong>，把实现将异构平台现有应用软件平滑迁移到龙芯平台作为设计目标。</p>
<p>除了基础指令、虚拟机扩展指令等指令外，LoongArch还包含二进制翻译扩展指令，以支持龙芯二进制翻译系统对其他架构下二进制指令的高效翻译。</p>
<p>龙芯二进制翻译系统基于LoongArch二进制翻译扩展指令实现，利用软硬件结合的翻译优化技术，实现跨指令集、跨操作系统间的应用兼容、高效运行。</p>
<p><strong><span style="color:#ff0000;">龙芯二进制翻译应用解决方案通过三个龙芯二进制翻译系统LATM（LAT from MIPS）、LATA（LAT from ARM）、LATX（LAT from X86），分别支持MIPS、ARM、x86平台的应用在龙芯平台的安装运行。</span></strong></p>
<p>龙芯二进制翻译系统作为中间层，通过架构层支持与软硬协同算法优化，充分利用本地硬件，最大化提升模拟效率，为上层应用软件提供目标指令集的良好虚拟运行环境。</p>
<p style="text-align: center"><a href="https://img1.mydrivers.com/img/20211109/0173c1d5-5e41-45bf-9447-eb63897913e4.png" target="_blank"><img alt="龙芯自主指令集二进制翻译应用：可流畅打CS" h="123" src="https://img1.mydrivers.com/img/20211109/S0173c1d5-5e41-45bf-9447-eb63897913e4.png" style="border: black 1px solid" w="600" referrerpolicy="no-referrer"></a></p>
<p>二进制翻译技术是实现跨指令系统兼容的重要手段，通过在宿主机（host）上用软件模拟目标机/客户机（guest）指令系统兼容的CPU，从而在宿主机上执行客户机的二进制代码，达到兼容的目的。</p>
<p>该方案的最大问题是效率，因为纯软件模拟的CPU，要比硬件直接实现的CPU慢很多，运行速度往往都是数量级的差异。</p>
<p><strong>龙芯二进制翻译系统利用动态二进制翻译技术，使用了多种软硬件结合的翻译优化技术，利用LoongArch指令集二进制翻译扩展提供的EFLAGS运算标志指令与浮点特殊寻址模式支持，大幅减少翻译代价，提升二进制翻译程序的运行效率。</strong></p>
<p>龙芯二进制翻译解决方案的三大优势：</p>
<p><strong>－ 高效</strong></p>
<p>基于软硬件结合的高效二进制翻译技术，比传统软件模拟方式有数量级的性能提升。应用级翻译实现对3D加速、视频编解码等功能的硬件支持。</p>
<p><strong>－ 兼容</strong></p>
<p>跨指令集应用兼容运行，通过wine中间件可实现Windows到Linux的操作系统级别兼容，支持多平台应用在龙芯平台的运行。</p>
<p><strong>－ 自主</strong></p>
<p>与龙芯自主指令集设计深度协同，通过持续优化改进翻译器和指令集，实现更高效的翻译与更广泛的兼容性。</p>
<p><strong>通过龙芯二进制翻译系统，基于wine中间件技术，可以在龙芯平台上流畅运行常用桌面应用，如微信、Photoshop等等。</strong></p>
<p style="text-align: center;"><a href="https://img1.mydrivers.com/img/20211109/be6e2da9-62e3-49b0-be11-9cec5cf46e99.jpg" style="text-align: center;" target="_blank"><img alt="龙芯自主指令集二进制翻译应用：可流畅打CS" h="337" src="https://img1.mydrivers.com/img/20211109/Sbe6e2da9-62e3-49b0-be11-9cec5cf46e99.jpg" style="border: black 1px solid" w="600" referrerpolicy="no-referrer"></a></p>
<p><strong>它还支持硬件加速，可加速音视频、3D等应用场景，比如流畅运行CS等3D游戏</strong>，后续还将不断适配更多x86应用。</p>
<p style="text-align: center"><a href="https://img1.mydrivers.com/img/20211109/8ca81a3f-d417-46ab-9076-713c2be118da.png" target="_blank"><img alt="龙芯自主指令集二进制翻译应用：可流畅打CS" h="450" src="https://img1.mydrivers.com/img/20211109/S8ca81a3f-d417-46ab-9076-713c2be118da.png" style="border: black 1px solid" w="600" referrerpolicy="no-referrer"></a></p>
<p>目前，龙芯二进制翻译技术已经落地多个解决方案场景，比如龙芯办公外设利旧通用解决方案（虚拟打印）。</p>
<p style="text-align: center"><a href="https://img1.mydrivers.com/img/20211109/60e44a52-54bf-4e95-ae8b-ca0da756b367.jpg" target="_blank"><img alt="龙芯自主指令集二进制翻译应用：可流畅打CS" h="254" src="https://img1.mydrivers.com/img/20211109/S60e44a52-54bf-4e95-ae8b-ca0da756b367.jpg" style="border: black 1px solid" w="600" referrerpolicy="no-referrer"></a></p>

           
           
<p class="end"> - THE END -</p> 
          <p class="zhuanzai">转载请注明出处：快科技</p>  
 <p class="bqian"><a href="https://news.mydrivers.com/tag/cpuchuliqi.htm"><i>#</i>CPU处理器</a><a href="https://news.mydrivers.com/tag/longxin.htm"><i>#</i>龙芯</a></p>
<p class="url">
     
<span>责任编辑：上方文Q</span>
</p>
        
</div>
            