
---
title: 'Godot 4.0 alpha 10 发布，引入重磅新特性'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://oscimg.oschina.net/oscnet/up-ffabdfe4950e31f91a9afdf79edd686066f.png'
author: 开源中国
comments: false
date: Sat, 18 Jun 2022 00:13:00 GMT
thumbnail: 'https://oscimg.oschina.net/oscnet/up-ffabdfe4950e31f91a9afdf79edd686066f.png'
---

<div>   
<div class="content">
                                                                    
                                                        <p>Godot 4.0 发布了第 10 个 Alpha 版本。</p> 
<p>值得关注的变化：</p> 
<ul> 
 <li><strong>新增将 Godot 3.x 项目转换为兼容 Godot 4 的 CLI 工具</strong></li> 
</ul> 
<p>此工具旨在优化项目从 Godot 3.x 过渡到 Godot 4.0 的 API 兼容性。由于此工作仍在进行中，因此建议在尝试转换工具之前，先备份项目。</p> 
<ul> 
 <li><strong>初步实现<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgodotengine%2Fgodot%2Fpull%2F61319" target="_blank"> Temporal Anti-Aliasing (TAA)</a></strong></li> 
</ul> 
<p>先来看看分别启用和禁用 Temporal AA（时域抗锯齿）的效果。</p> 
<p><strong>启用 TAA ↓</strong></p> 
<p><img alt src="https://oscimg.oschina.net/oscnet/up-ffabdfe4950e31f91a9afdf79edd686066f.png" referrerpolicy="no-referrer"></p> 
<p><strong>禁用 TAA ↓</strong></p> 
<p><img alt src="https://oscimg.oschina.net/oscnet/up-010a2cf0f2f64b1f5f7441184acc8d7bf66.png" referrerpolicy="no-referrer"></p> 
<p>从上述的效果图来看，启用 TAA 后显著提升了画质。</p> 
<p>Temporal AA 的实现原理是基于上一帧的信息来帮助优化当前帧的抗锯齿。TAA 在游戏引擎中越来越受欢迎，因为它提供了与多采样抗锯齿相同/相近的质量，但开销更低。</p> 
<p><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdownloads.tuxfamily.org%2Fgodotengine%2F4.0%2Falpha10%2F" target="_blank">下载地址</a> & <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgodotengine.org%2Farticle%2Fdev-snapshot-godot-4-0-alpha-10" target="_blank">发布公告</a></p>
                                        </div>
                                      
</div>
            