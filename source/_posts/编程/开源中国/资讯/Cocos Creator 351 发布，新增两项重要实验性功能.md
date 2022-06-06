
---
title: 'Cocos Creator 3.5.1 发布，新增两项重要实验性功能'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://oscimg.oschina.net/oscnet/up-20e3e397b7ab1021d152dc00573bd110ab9.png'
author: 开源中国
comments: false
date: Sun, 05 Jun 2022 07:42:00 GMT
thumbnail: 'https://oscimg.oschina.net/oscnet/up-20e3e397b7ab1021d152dc00573bd110ab9.png'
---

<div>   
<div class="content">
                                                                    
                                                        <p>Cocos Creator 3.5.1 已发布，此版本在不影响原有功能稳定性的前提下加入了两项影响深远的实验性功能，<strong>一是智能导入 FBX 中的 DCC 默认材质，</strong>还原美术在各类 DCC 工具中使用的材质和外观；<strong>二是内置了一系列 Surface Shader 材质资源，</strong>这将成为未来支撑材质定制的基石。</p> 
<p style="color:#3e3e3e; margin-left:0; margin-right:0; text-align:justify"><span>除此之外，还完成了一系列关键性的问题修复、体验优化和大量的文档优化，建议所有 v3.x 用户升级。</span></p> 
<h2 style="margin-left:0px; margin-right:0px"><strong>重要更新 </strong></h2> 
<h3 style="margin-left:0px; margin-right:0px"><strong>实验性：FBX 智能材质导入</strong></h3> 
<p><img alt src="https://oscimg.oschina.net/oscnet/up-20e3e397b7ab1021d152dc00573bd110ab9.png" referrerpolicy="no-referrer"></p> 
<p><span style="background-color:#ffffff; color:#3e3e3e">FBX 智能材质导入是模型导入器中辅助转换材质的一个功能，它可以将各种 DCC 工具导出到模型中的部分标准材质直接映射到 Cocos Creator 的内置材质中，尽量还原美术在 DCC 工具中看到的材质效果。我们可以对比一下 Maya 中的 Standard Surface 材质导入 Cocos Creator 后的效果：</span></p> 
<p><img alt src="https://oscimg.oschina.net/oscnet/up-52302c925650daec280a74c56dc26ea8af7.png" referrerpolicy="no-referrer"></p> 
<p>▲ Maya 工具内效果</p> 
<p><img alt src="https://oscimg.oschina.net/oscnet/up-5939a164c16301bba2817a7092e3800c441.png" referrerpolicy="no-referrer"></p> 
<p>▲ 开启 FBX 智能材质导入后 Cocos Creator 内效果</p> 
<p>此功能已支持主流 DCC 工具：3ds Max、Blender、Maya、C4D 中的部分标准材质。</p> 
<p style="margin-left:0; margin-right:0"><img alt src="https://oscimg.oschina.net/oscnet/up-b0f655defc84adb99fb5d3b9c6b5ace12bf.png" referrerpolicy="no-referrer"></p> 
<p>具体使用可以参考使用文档[1]。同时我们也将在 v3.6 中持续优化模型和材质导入体验，敬请期待。</p> 
<h3 style="margin-left:0px; margin-right:0px"><strong>实验性：新增 Surface Shader</strong></h3> 
<p style="margin-left:0; margin-right:0"><span>从 v</span><span>3.0 版本以来，不少开发者都经历过升级过程中材质无法正常使用，需要迁移的问题，为此我们也准备过不少材质系统专属的升级文档，然而手动升级过程的体验确实不尽如人意。此问题的根本原因是引擎的光照模型和表面材质的计算一直在调整，这会影响所有相关的材质 effect 代码，也会影响到用户复用这些材质时的兼容性。</span></p> 
<p style="margin-left:0; margin-right:0">为了提升材质系统的兼容性，我们新增了一系列 Surface Shader 资源，抽象了引擎内的光照模型和表面材质计算，未来开发者可以使用这些抽象好的头文件和内置函数极大简化自己书写的 effect 资源。同时由于多了一些封装，跨版本间的兼容性也会更有保障。</p> 
<p style="margin-left:0; margin-right:0">具体 Surface Shader 的使用请参考使用文档[2]。</p> 
<h2 style="margin-left:0px; margin-right:0px"><strong>文档优化 </strong></h2> 
<p style="margin-left:0; margin-right:0"><span>从 v3.5 开始我们设计了新版 API 文档页面[3]，受到了开发者比较普遍的好评和一些反馈。在 v3.5.1 我们继续做了大量的内容检查，通过近 40 个 PR 进一步补全了之前遗留的一些 API 文档，修复了部分文档错误。并且之后文档也会得到持续性的优化，希望给开发者带来越来越好的使用体验。</span></p> 
<h2 style="margin-left:0px; margin-right:0px"><strong>重要修复 </strong></h2> 
<ul style="list-style-type:disc; margin-left:0; margin-right:0"> 
 <li> <p style="margin-left:0; margin-right:0"><span>修复浏览器预览速度过慢的问题。</span></p> </li> 
 <li> <p style="margin-left:0; margin-right:0">修复 Mobile Safari 上无法预览的问题。</p> </li> 
 <li> <p style="margin-left:0; margin-right:0">修复部分材质从 v3.4.2 或更低版本不能自动升级的问题。</p> </li> 
 <li> <p style="margin-left:0; margin-right:0">修复 3D 粒子系统在状态切换时可能的报错和表现问题。</p> </li> 
 <li> <p style="margin-left:0; margin-right:0">修复延迟管线的光影计算。</p> </li> 
</ul> 
<h2 style="margin-left:0px; margin-right:0px"><strong>参考链接 </strong></h2> 
<p style="margin-left:0; margin-right:0">[1] FBX 智能材质导入使用文档</p> 
<p style="margin-left:0; margin-right:0"><em>https://docs.cocos.com/creator/manual/zh/importer/materials/fbx-materials.html</em></p> 
<p style="margin-left:0; margin-right:0">[2] Surface Shader 使用文档</p> 
<p style="margin-left:0; margin-right:0"><em>https://docs.cocos.com/creator/manual/zh/shader/surface-shader.html</em></p> 
<p style="margin-left:0; margin-right:0">[3] 新版 API 文档</p> 
<p style="margin-left:0; margin-right:0"><em>https://docs.cocos.com/creator/api/zh/#/</em></p> 
<p>下载：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.cocos.com%2Fcreator" target="_blank">https://www.cocos.com/creator</a></p> 
<hr> 
<p>Cocos Creator 是以内容创作为核心，实现了脚本化、组件化和数据驱动的游戏开发工具。 具备了易于上手的内容生产工作流，以及功能强大的开发者工具套件，可用于实现游戏逻辑和高性能游戏效果。</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><img alt src="https://oscimg.oschina.net/oscnet/up-e622ff52598dc6383c70d6d03fb9a963de8.png" referrerpolicy="no-referrer"></p> 
<p> </p>
                                        </div>
                                      
</div>
            