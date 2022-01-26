
---
title: 'Godot 4.0 首个 Alpha 版本发布'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://oscimg.oschina.net/oscnet/up-65427e7fc7c52db73b6a7e32a75ffb9bd6a.png'
author: 开源中国
comments: false
date: Wed, 26 Jan 2022 07:18:00 GMT
thumbnail: 'https://oscimg.oschina.net/oscnet/up-65427e7fc7c52db73b6a7e32a75ffb9bd6a.png'
---

<div>   
<div class="content">
                                                                                            <p>Godot 4.0 发布了首个 Alpha 版本。4.0 作为重大版本更新，其开发工作于 2020 年<a href="https://www.oschina.net/news/112685/godot-decade-in-retrospective-and-future">启动</a>，在两年多的开发过程中，Godot 4.0 带来的新特性包括：支持 Vulkan API、改进图形渲染系统、改进 OpenGL、添加新的 Physics 特性、增强 GDScript 脚本、更好地支持音频、改进多人游戏模式，以及许多其他的变化。</p> 
<p><img alt src="https://oscimg.oschina.net/oscnet/up-65427e7fc7c52db73b6a7e32a75ffb9bd6a.png" referrerpolicy="no-referrer"></p> 
<p>4.0 Alpha 下载地址：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdownloads.tuxfamily.org%2Fgodotengine%2F4.0%2Falpha1%2F" target="_blank">https://downloads.tuxfamily.org/godotengine/4.0/alpha1/</a>（在 Alpha 阶段的引擎仍然不完整也不够稳定，且与后续的 beta 版本会有较大的变化，建议谨慎使用）</p> 
<p>下面介绍 4.0 的部分亮点。</p> 
<p><strong>重写全局光照渲染器</strong></p> 
<p>在新版本中，GIProbe 已经被 VoxelGI node 所取代，这是一个适合中小型环境的实时解决方案。有史以来第一次，Godot 还提供了一种可用于大型开放世界的 GI 技术 —— 有向距离场全局光照 (SDFGI)，这项技术由 Godot 首席开发者 Juan Linietsky 创建和实现，支持实时 (real-time) 运行，<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgodotengine.org%2Farticle%2Fgodot-40-gets-sdf-based-real-time-global-illumination" target="_blank">点此了解更多信息</a>。</p> 
<p><img alt src="https://oscimg.oschina.net/oscnet/up-dd51010b991aa40eb2696cd73cc5893b77f.png" referrerpolicy="no-referrer"></p> 
<p><strong>Godot Physics</strong></p> 
<p>Godot 4 标志着 Godot 内部 3D 物理引擎 <strong>Godot Physics </strong>的重大回归。多年来，Godot 一直使用 <strong>Bullet </strong>引擎为 3D 项目提供坚实的基础。不过团队认为在实现新功能和解决问题方面，定制解决方案可带来更大的灵活性。</p> 
<p><img src="https://static.oschina.net/uploads/space/2022/0126/002858_RWbg_2720166.gif" referrerpolicy="no-referrer"></p> 
<p>许多以前特定身体类型独有的属性现在可用于所有 <strong>PhysicsBody </strong>节点。因此可以引入新的 <strong>CharacterBody </strong>节点来替换旧的运动体，并使角色的配置更加简单。</p> 
<p><strong>脚本</strong></p> 
<p>此版本为 GDScript 增加了一些最受欢迎和期待已久的语言特性来真正优化 Godot 4 中的编码体验。例如一等公民的函数支持、lambdas、新的属性语法、await 和 super 关键字，以及类型化数组。此外，新的内置注释使语言更清晰，并改进了导出属性的语法。最重要的是，脚本现在可以自动生成文档，可以通过内置帮助和 Inspector dock 工具提示进行学习。</p> 
<p><img alt src="https://oscimg.oschina.net/oscnet/up-a693c6736eb1a8d74bfb43d1aa67fb5ff47.png" referrerpolicy="no-referrer"></p> 
<p><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgodotengine.org%2Farticle%2Fdev-snapshot-godot-4-0-alpha-1" target="_blank">更多新特性介绍和已知问题查看发布公告</a>。</p> 
<h3><strong>关于 Godot 引擎</strong></h3> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">游戏引擎是一个复杂的工具，因此很难用三言两语来概括 Godot。这是一个快速概要，如果需要快速撰写关于 Godot 引擎的文章，可以自由复用该概要。</p> 
<blockquote> 
 <p style="margin-left:0; margin-right:0">Godot引擎是一款功能丰富的跨平台游戏引擎，可通过统一界面创建2D和3D游戏。 它提供了一套全面的通用工具，因此用户可以专注于制作游戏，而无需重新发明轮子。 游戏可以一键导出到多个平台，包括主要的桌面平台(Linux、macOS、Windows)以及移动平台(Android、iOS)和基于Web的(HTML5)平台。</p> 
 <p style="margin-left:0; margin-right:0">Godot在宽松的MIT许可证下完全自由且开源。没有附加条文，没有特许权使用费，没有任何要求。用户的游戏乃至引擎的每一行代码，都是他们的。Godot的开发完全独立且由社区驱动，允许用户以帮助塑造他们的引擎来满足他们的期望。它受到 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fsfconservancy.org%2F" target="_blank">软件自由保护</a> 非营利组织的支持。</p> 
 <p style="margin-left:0; margin-right:0">摘自 Godot 中文文档：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdocs.godotengine.org%2Fzh_CN%2Flatest%2F" target="_blank">https://docs.godotengine.org/zh_CN/latest/</a></p> 
</blockquote>
                                        </div>
                                      
</div>
            