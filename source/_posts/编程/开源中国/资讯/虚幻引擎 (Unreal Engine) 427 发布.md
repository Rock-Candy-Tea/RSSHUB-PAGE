
---
title: '虚幻引擎 (Unreal Engine) 4.27 发布'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://oscimg.oschina.net/oscnet/up-3a3cfcc682991832bd508d8f3c184a2dc4c.png'
author: 开源中国
comments: false
date: Fri, 20 Aug 2021 23:55:00 GMT
thumbnail: 'https://oscimg.oschina.net/oscnet/up-3a3cfcc682991832bd508d8f3c184a2dc4c.png'
---

<div>   
<div class="content">
                                                                    
                                                        <p>虚幻引擎 (Unreal Engine) 4.27<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.unrealengine.com%2Fzh-CN%2Fblog%2Funreal-engine-4-27-released" target="_blank"> 已正式发布</a>。此版本通过在效率、质量和易用性方面对虚拟制片工具集的一系列改进，令摄像机内视效上升到了新高度，其他亮点包括通过路径追踪实现精美的最终图片，开箱即用的 Oodle 和 Bink，可用于生产的像素流送等诸多功能。</p> 
<p><img alt src="https://oscimg.oschina.net/oscnet/up-3a3cfcc682991832bd508d8f3c184a2dc4c.png" referrerpolicy="no-referrer"></p> 
<h2>主要新功能</h2> 
<h3>nDisplay改良</h3> 
<p>通过3D配置编辑器和集成了所有nDisplay相关功能和设置的单个UAsset文件，使用多显示器渲染的应用（包括摄像机内视效）现在将更容易设置。我们还提供了对OpenColorIO的支持，以实现精确的颜色校准，对多GPU渲染的支持也已进入测试阶段。同时，多摄像机的配置也得到了简化。</p> 
<p><img alt src="https://oscimg.oschina.net/oscnet/up-0c62cb9b6fae4a1260469770b0ee6ad9b1a.png" referrerpolicy="no-referrer"></p> 
<h3>可用于生产的像素流送</h3> 
<p>像素流送的质量大幅提升，并配备WebRTC的升级版本，现已可用于生产。此外，我们还添加了对Linux的支持。这项强大的技术使虚幻引擎和构建在其上的应用程序能够在高性能云端虚拟机上运行，最终用户无论身处何地，都可在任何设备上通过普通网络浏览器享受其提供的高质量体验。</p> 
<p><img alt src="https://oscimg.oschina.net/oscnet/up-9dda7329ce382a4ba919bcc1d8fbb536927.png" referrerpolicy="no-referrer"></p> 
<h3>扩展的虚拟制片工具集</h3> 
<p>用于支持摄像机内视效和其他现场虚拟制片工作流程的改良包括：全新的拖放式远程控制网页UI构建器，以及得到显著改进并可用于生产的虚拟摄像机系统。同时，对关卡快照的支持也已进入测试阶段，使你能够保存和恢复给定关卡的状态，并为运动镜头生成正确的动态模糊。</p> 
<p><img alt src="https://oscimg.oschina.net/oscnet/up-953406a98a172cae131c755615972d54e3b.png" referrerpolicy="no-referrer"></p> 
<h3>Oodle和Bink加入</h3> 
<p>RAD Game Tools成为Epic Games大家庭的一员后，Oodle压缩套件和Bink Video编解码器现已成为虚幻引擎中开箱即用的内置工具，将业内最快、最高效、最流行的一些压缩和编码工具免费送到了虚幻引擎开发者的手中。这些工具可在虚幻引擎支持的所有平台上运行。 </p> 
<p><img alt src="https://oscimg.oschina.net/oscnet/up-6a24e45b00b4a80355efd8eea8f63b9c539.png" referrerpolicy="no-referrer"></p> 
<h3>GPU Lightmass改良（测试版）</h3> 
<p>GPU Lightmass是一种光源烘焙解决方案，它使用GPU（而非CPU）以明显更快的速度逐步渲染预计算的光照贴图，并在这一过程中利用了通过DirectX 12（DX12）和微软DXR框架所实现的最新光线追踪功能。在这个发行版中，GPU Lightmass提供了对更多功能的支持，同时也提高了稳定性和可靠性。</p> 
<p><img alt src="https://oscimg.oschina.net/oscnet/up-09c5f321bd2fe29a439c376a1011600691b.png" referrerpolicy="no-referrer"></p> 
<h3>用于最终像素的路径追踪器（测试版）</h3> 
<p>路径追踪器是一个由DXR加速、并且物理精确的渐进式渲染模式，可一键启用。通过这个发行版中提供的众多改进，你现在可以使用它创建与离线渲染相媲美的最终像素图片，并在其中实现无损全局光照、物理正确的折射和超采样抗锯齿等。</p> 
<p><img alt src="https://oscimg.oschina.net/oscnet/up-b55c7a68f2ba02e3e82a1d425e60136467b.png" referrerpolicy="no-referrer"></p> 
<h3>Datasmith改良</h3> 
<p>我们大幅扩展了Datasmith运行环境，允许用户将.udatasmith数据导入在虚幻引擎上构建的封装应用中。我们还为全新的Archicad Exporter插件以及现有的Rhino和SketchUp Pro插件添加了Direct Link功能，使用户能够在源DCC工具和基于虚幻引擎的应用之间保持实时连接。</p> 
<p><img alt src="https://oscimg.oschina.net/oscnet/up-76c21160f1e15576bed90966de599c5cd8e.png" referrerpolicy="no-referrer"></p> 
<h3>对USD和Alembic的支持改良（测试版）</h3> 
<p>在这个虚幻引擎4.27中，现在可以将更多元素导出到USD，其中包括关卡、子关卡、地形、植被和动画序列，也可以将材质作为MDL节点导入。你现在也可以在USD舞台编辑器中（包括通过多用户编辑的形式）编辑USD属性。此外，现在可以将头发和毛发Groom绑定至从Alembic导入的GeometryCache数据。</p> 
<p><img alt src="https://oscimg.oschina.net/oscnet/up-9c241221597051e421d03804b663032c90e.png" referrerpolicy="no-referrer"></p> 
<h3>用于扩展现实的工作流程改良</h3> 
<p>在虚幻引擎中创建XR（VR、AR和MR）内容变得更容易了。通过我们的OpenXR插件，你可以用相同的API锁定多台目标XR设备，该插件现已可用于生产，并为其他功能提供了支持。我们还重新设计了VR和AR模板，提供更多内置功能和更简单的设置，让你以更快的方式启动项目。</p> 
<p><img alt src="https://oscimg.oschina.net/oscnet/up-5342469cedcc9a3412b9466912da0dbd0ce.png" referrerpolicy="no-referrer"></p> 
<h3>简化的静态图像渲染（测试版）</h3> 
<p>新增了使用影片渲染队列实现多个相机的批量渲染的功能，无需经过复杂的Sequencer设置。因此，在使用变体或进行迭代时，从不同视点重复创建一系列大型静态图片将变得容易，是创建建筑、汽车、产品设计可交付成果的理想之选。</p> 
<p><img alt src="https://oscimg.oschina.net/oscnet/up-1ff8e6db9c2c187a9f8ee30c74b77f40827.png" referrerpolicy="no-referrer"></p> 
<h3>Visual Dataprep改良</h3> 
<p>我们继续扩展了Visual Dataprep的功能，提供了新操作符和过滤器，添加了对Actor组件的支持，增强了用户体验。Visual Dataprep可帮助你轻松地自动完成导入与3D数据准备流程，只需使用直观的可视化拖放UI、各种操作符和选择过滤器构建“配方”即可。 </p> 
<p><img alt src="https://oscimg.oschina.net/oscnet/up-1b0f1144d0daa8bd744d149a2b13f2d8466.png" referrerpolicy="no-referrer"></p> 
<h3>对虚幻引擎容器的支持（测试版）</h3> 
<p>通过对Windows和Linux上的容器提供支持，虚幻引擎将可充当一个强大的自足式基础技术层，为像素流送、CI/CD、AI/ML训练、批量处理和渲染以及微服务等基于云端的新型开发工作流程、部署策略以及增强的产品管线铺平了道路。 </p> 
<p><img alt src="https://oscimg.oschina.net/oscnet/up-56a84000d8d1203f10a9a54deaf83f7f01a.png" referrerpolicy="no-referrer"></p> 
<ul> 
 <li>下载地址：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.unrealengine.com%2Fzh-CN%2Fdownload" target="_blank">https://www.unrealengine.com/zh-CN/download</a></li> 
 <li>版本说明：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdocs.unrealengine.com%2F4.27%2Fzh-CN%2FWhatsNew%2FBuilds%2FReleaseNotes%2F4_27%2F" target="_blank">https://docs.unrealengine.com/4.27/zh-CN/WhatsNew/Builds/ReleaseNotes/4_27/</a></li> 
</ul>
                                        </div>
                                      
</div>
            