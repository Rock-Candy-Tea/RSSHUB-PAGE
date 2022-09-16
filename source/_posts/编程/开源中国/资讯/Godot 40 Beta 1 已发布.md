
---
title: 'Godot 4.0 Beta 1 已发布'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://static.oschina.net/uploads/space/2022/0916/075646_Qdkf_5430600.png'
author: 开源中国
comments: false
date: Fri, 16 Sep 2022 07:58:00 GMT
thumbnail: 'https://static.oschina.net/uploads/space/2022/0916/075646_Qdkf_5430600.png'
---

<div>   
<div class="content">
                                                                                            <p>Godot 4.0 版本的第一个 beta 版本现已发布并<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgodotengine.org%2Farticle%2Fdev-snapshot-godot-4-0-beta-1" target="_blank">可供下载</a>，这意味着 Godot 4.0 的功能集已冻结，剩下的是修复错误和优化性能。</p> 
<p>一些新功能：</p> 
<h2><strong>渲染</strong></h2> 
<p>在过去的几年里， Godot 渲染被彻底改造，现在默认以 Vulkan 为目标，同时考虑了未来对 Direct3D 12 和其他渲染 API 的支持。</p> 
<p>此外，Godot 还创建了一个基于 OpenGL 的兼容性渲染器，对那些不支持 Vulkan 或其他现代 GPU API 的旧设备和低端设备进行支持。</p> 
<p><strong>新的渲染效果</strong></p> 
<p><strong>体积雾</strong>首次出现在 Godot 4 中，体积雾效果使用了时间重投影，在逼真的外观和性能之间取得了平衡。可以全局配置效果，或使用 FogVolume 节点定义特定区域。甚至可以通过编写在 FogVolume 节点上运行的自定义着色器来创建复杂的动态效果。</p> 
<p>对于其他大气效果，Godot 4.0 引入了天空着色器，允许用户创建实时更新的动态天空（包括反射）。有关更多信息，请参阅介绍<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgodotengine.org%2Farticle%2Fcustom-sky-shaders-godot-4-0" target="_blank">天空着色器</a>的文章。</p> 
<p><img height="350" src="https://static.oschina.net/uploads/space/2022/0916/075646_Qdkf_5430600.png" width="700" referrerpolicy="no-referrer"></p> 
<p><strong>重写全局光照渲染器</strong></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">在新版本中，GIProbe 已经被 VoxelGI node 所取代，这是一个适合中小型环境的实时解决方案。有史以来第一次，Godot 还提供了一种可用于大型开放世界的 GI 技术 —— 有向距离场全局光照 (SDFGI)，这项技术由 Godot 首席开发者 Juan Linietsky 创建和实现，支持实时 (real-time) 运行，<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgodotengine.org%2Farticle%2Fgodot-40-gets-sdf-based-real-time-global-illumination" target="_blank">点此了解更多信息</a>。</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><img alt src="https://oscimg.oschina.net/oscnet/up-dd51010b991aa40eb2696cd73cc5893b77f.png" referrerpolicy="no-referrer"></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><strong>Godot Physics</strong></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">Godot 4 标志着 Godot 内部 3D 物理引擎 <strong>Godot Physics </strong>的重大回归。多年来，Godot 一直使用 <strong>Bullet </strong>引擎为 3D 项目提供坚实的基础。不过团队认为在实现新功能和解决问题方面，定制解决方案可带来更大的灵活性。</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><img src="https://static.oschina.net/uploads/space/2022/0126/002858_RWbg_2720166.gif" referrerpolicy="no-referrer"></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">许多以前特定身体类型独有的属性现在可用于所有 <strong>PhysicsBody </strong>节点。因此可以引入新的 <strong>CharacterBody </strong>节点来替换旧的运动体，并使角色的配置更加简单。</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><strong>脚本</strong></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">此版本为 GDScript 增加了一些最受欢迎和期待已久的语言特性来真正优化 Godot 4 中的编码体验。例如一等公民的函数支持、lambdas、新的属性语法、await 和 super 关键字，以及类型化数组。此外，新的内置注释使语言更清晰，并改进了导出属性的语法。最重要的是，脚本现在可以自动生成文档，可以通过内置帮助和 Inspector dock 工具提示进行学习。</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><img alt src="https://oscimg.oschina.net/oscnet/up-a693c6736eb1a8d74bfb43d1aa67fb5ff47.png" referrerpolicy="no-referrer"></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"> </p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">更多新特性介绍，请查看<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgodotengine.org%2Farticle%2Fdev-snapshot-godot-4-0-beta-1" target="_blank">发布公告</a>。</p>
                                        </div>
                                      
</div>
            