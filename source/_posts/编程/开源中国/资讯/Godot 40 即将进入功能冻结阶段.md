
---
title: 'Godot 4.0 即将进入功能冻结阶段'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://oscimg.oschina.net/oscnet/up-cf3b9a52d66b5533b57161108f41b0a7bd5.png'
author: 开源中国
comments: false
date: Sat, 30 Jul 2022 07:27:00 GMT
thumbnail: 'https://oscimg.oschina.net/oscnet/up-cf3b9a52d66b5533b57161108f41b0a7bd5.png'
---

<div>   
<div class="content">
                                                                    
                                                        <p>根据 Godot 官方博客<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgodotengine.org%2Farticle%2Fgodot-4-0-development-enters-feature-freeze" target="_blank">公布</a>的开发进度，从 8 月 3 日开始，Godot 4.0 将进入功能冻结阶段，预计在未来五到六周内发布 4.0 Beta 1。</p> 
<p>具体进度：</p> 
<ul> 
 <li><strong>8 月 3 日：</strong>4.0 进入功能冻结阶段；开发者最好在此之前提交重要变更代码</li> 
 <li><strong>8 月 17 日</strong>：确定 beta 1 的时间窗口；继续审查和评估 PR</li> 
 <li><strong>9 月初：</strong>发布<strong> </strong>beta 1</li> 
</ul> 
<p><img alt src="https://oscimg.oschina.net/oscnet/up-cf3b9a52d66b5533b57161108f41b0a7bd5.png" referrerpolicy="no-referrer"></p> 
<p>Godot 4.0 新增功能：</p> 
<ul> 
 <li>备受期待的 Vulkan 渲染器和其他渲染器增强功能</li> 
 <li>支持 Temporal AA</li> 
 <li>支持 OpenXR</li> 
 <li>支持 text-to-speech</li> 
 <li>改进图形渲染系统</li> 
 <li>改进 OpenGL</li> 
 <li>添加新的 Physics 特性</li> 
 <li>增强 GDScript 脚本</li> 
 <li>改进多人游戏模式</li> 
 <li>编辑器功能增强</li> 
 <li>优化文档</li> 
 <li>……</li> 
</ul> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">下面介绍 4.0 的部分亮点。</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><strong>重写全局光照渲染器</strong></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">在新版本中，GIProbe 已经被 VoxelGI node 所取代，这是一个适合中小型环境的实时解决方案。有史以来第一次，Godot 还提供了一种可用于大型开放世界的 GI 技术 —— 有向距离场全局光照 (SDFGI)，这项技术由 Godot 首席开发者 Juan Linietsky 创建和实现，支持实时 (real-time) 运行，<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgodotengine.org%2Farticle%2Fgodot-40-gets-sdf-based-real-time-global-illumination" target="_blank">点此了解更多信息</a>。</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><img alt src="https://oscimg.oschina.net/oscnet/up-dd51010b991aa40eb2696cd73cc5893b77f.png" referrerpolicy="no-referrer"></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><strong>Godot Physics</strong></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">Godot 4 标志着 Godot 内部 3D 物理引擎 <strong>Godot Physics </strong>的重大回归。多年来，Godot 一直使用 <strong>Bullet </strong>引擎为 3D 项目提供坚实的基础。不过团队认为在实现新功能和解决问题方面，定制解决方案可带来更大的灵活性。</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><img src="https://static.oschina.net/uploads/space/2022/0126/002858_RWbg_2720166.gif" referrerpolicy="no-referrer"></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">许多以前特定身体类型独有的属性现在可用于所有 <strong>PhysicsBody </strong>节点。因此可以引入新的 <strong>CharacterBody </strong>节点来替换旧的运动体，并使角色的配置更加简单。</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><strong>脚本</strong></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">此版本为 GDScript 增加了一些最受欢迎和期待已久的语言特性来真正优化 Godot 4 中的编码体验。例如一等公民的函数支持、lambdas、新的属性语法、await 和 super 关键字，以及类型化数组。此外，新的内置注释使语言更清晰，并改进了导出属性的语法。最重要的是，脚本现在可以自动生成文档，可以通过内置帮助和 Inspector dock 工具提示进行学习。</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><img alt src="https://oscimg.oschina.net/oscnet/up-a693c6736eb1a8d74bfb43d1aa67fb5ff47.png" referrerpolicy="no-referrer"></p> 
<p><strong>初步实现<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgodotengine%2Fgodot%2Fpull%2F61319" target="_blank"><span> </span>Temporal Anti-Aliasing (TAA)</a></strong></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">先来看看分别启用和禁用 Temporal AA（时域抗锯齿）的效果。</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><strong>启用 TAA ↓</strong></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><img alt src="https://oscimg.oschina.net/oscnet/up-ffabdfe4950e31f91a9afdf79edd686066f.png" referrerpolicy="no-referrer"></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><strong>禁用 TAA ↓</strong></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><img alt src="https://oscimg.oschina.net/oscnet/up-010a2cf0f2f64b1f5f7441184acc8d7bf66.png" referrerpolicy="no-referrer"></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">从上述的效果图来看，启用 TAA 后显著提升了画质。</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">Temporal AA 的实现原理是基于上一帧的信息来帮助优化当前帧的抗锯齿。TAA 在游戏引擎中越来越受欢迎，因为它提供了与多采样抗锯齿相同 / 相近的质量，但开销更低。</p> 
<hr> 
<p style="margin-left:0px; margin-right:0px; text-align:left"><strong>关于 Godot 引擎</strong></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">游戏引擎是一个复杂的工具，因此很难用三言两语来概括 Godot。这是一个快速概要，如果需要快速撰写关于 Godot 引擎的文章，可以自由复用该概要。</p> 
<blockquote> 
 <p style="margin-left:0; margin-right:0">Godot 引擎是一款功能丰富的跨平台游戏引擎，可通过统一界面创建 2D 和 3D 游戏。 它提供了一套全面的通用工具，因此用户可以专注于制作游戏，而无需重新发明轮子。 游戏可以一键导出到多个平台，包括主要的桌面平台 (Linux、macOS、Windows) 以及移动平台 (Android、iOS) 和基于 Web 的 (HTML5) 平台。</p> 
 <p style="margin-left:0; margin-right:0">Godot 在宽松的 MIT 许可证下完全自由且开源。没有附加条文，没有特许权使用费，没有任何要求。用户的游戏乃至引擎的每一行代码，都是他们的。Godot 的开发完全独立且由社区驱动，允许用户以帮助塑造他们的引擎来满足他们的期望。它受到 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fsfconservancy.org%2F" target="_blank">软件自由保护</a> 非营利组织的支持。</p> 
 <p style="margin-left:0; margin-right:0">摘自 Godot 中文文档：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdocs.godotengine.org%2Fzh_CN%2Flatest%2F" target="_blank">https://docs.godotengine.org/zh_CN/latest/</a></p> 
</blockquote> 
<p> </p>
                                        </div>
                                      
</div>
            