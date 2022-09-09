
---
title: 'Godot 4.0 alpha 16 发布'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://oscimg.oschina.net/oscnet/up-ffabdfe4950e31f91a9afdf79edd686066f.png'
author: 开源中国
comments: false
date: Fri, 09 Sep 2022 07:19:00 GMT
thumbnail: 'https://oscimg.oschina.net/oscnet/up-ffabdfe4950e31f91a9afdf79edd686066f.png'
---

<div>   
<div class="content">
                                                                                            <div style="margin-left:0; margin-right:0; text-align:start"> 
 <p>Godot 4.0 发布了第 16 个 Alpha 版本。</p> 
</div> 
<p>自上个版本以来的主要变化：</p> 
<ul> 
 <li>使用 OpenGL 3 / WebGL 2 渲染器来重启对 Web 导出的支持</li> 
 <li>使用 Vulkan API 支持 2D 的多采样抗锯齿 (MSAA)</li> 
 <li>Godot 4 的新 Vulkan 渲染器引入物理光单元 (Physical light units)</li> 
 <li>在 Linux、macOS 和 Windows 中重新启用 per-pixel 透明度支持</li> 
 <li>针对编辑器的多项改进</li> 
 <li>修复在 Linux 上使用 X11 的最小化/最大化行为</li> 
 <li>GUI：改进 SplitContainer 行为</li> 
 <li>GUI：添加对换行时修剪边缘空间的支持</li> 
 <li>GUI：添加<code>ThemeOwner</code>类型用于管理 theme propagation 和查找</li> 
 <li>GUI：使 AcceptDialog 和衍生工具充分利用 StyleBox</li> 
 <li>……</li> 
</ul> 
<hr> 
<p>Godot 4 其他值得关注的变化：</p> 
<ul style="list-style-type:disc; margin-left:0; margin-right:0"> 
 <li><strong>新增将 Godot 3.x 项目转换为兼容 Godot 4 的 CLI 工具</strong></li> 
</ul> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">此工具旨在优化项目从 Godot 3.x 过渡到 Godot 4.0 的 API 兼容性。由于此工作仍在进行中，因此建议在尝试转换工具之前，先备份项目。</p> 
<ul style="list-style-type:disc; margin-left:0; margin-right:0"> 
 <li><strong>初步实现<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgodotengine%2Fgodot%2Fpull%2F61319" target="_blank"><span> </span>Temporal Anti-Aliasing (TAA)</a></strong></li> 
</ul> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">先来看看分别启用和禁用 Temporal AA（时域抗锯齿）的效果。</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><strong>启用 TAA ↓</strong></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><img alt src="https://oscimg.oschina.net/oscnet/up-ffabdfe4950e31f91a9afdf79edd686066f.png" referrerpolicy="no-referrer"></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><strong>禁用 TAA ↓</strong></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><img alt src="https://oscimg.oschina.net/oscnet/up-010a2cf0f2f64b1f5f7441184acc8d7bf66.png" referrerpolicy="no-referrer"></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">从上述的效果图来看，启用 TAA 后显著提升了画质。</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">Temporal AA 的实现原理是基于上一帧的信息来帮助优化当前帧的抗锯齿。TAA 在游戏引擎中越来越受欢迎，因为它提供了与多采样抗锯齿相同 / 相近的质量，但开销更低。</p> 
<p><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdownloads.tuxfamily.org%2Fgodotengine%2F4.0%2Falpha16%2F" target="_blank">下载地址</a> & <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgodotengine.org%2Farticle%2Fdev-snapshot-godot-4-0-alpha-16" target="_blank">发布公告</a></p>
                                        </div>
                                      
</div>
            