
---
title: 'Godot 3.5 发布，多平台游戏引擎'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://static.oschina.net/uploads/space/2022/0809/071835_nG5U_4937141.gif'
author: 开源中国
comments: false
date: Tue, 09 Aug 2022 07:20:00 GMT
thumbnail: 'https://static.oschina.net/uploads/space/2022/0809/071835_nG5U_4937141.gif'
---

<div>   
<div class="content">
                                                                                            <p>Godot Engine 是一个功能丰富的跨平台游戏引擎，可以从一个统一的界面创建 2D 和 3D 游戏。它提供了一套全面的通用工具，因此用户可以专注于制作游戏。游戏可以一键导出到多个平台，包括主要的桌面平台（Linux、macOS、Windows）、移动平台（Android、iOS），以及基于 Web 的平台和游戏机。</p> 
<p>经过 9 个月的开发，Godot 3.5 已经发布，虽然大部分的开发重点都在即将发布的 Godot 4.0 上，但许多贡献者和用户都希望有一个强大而成熟的 3.x 分支来开发和发布他们的游戏，所以对我们来说，继续为 Godot 3 用户提供更好的游戏开发体验非常重要。</p> 
<h2>功能</h2> 
<h3>新的 Navigation Server</h3> 
<p><img alt height="391" src="https://static.oschina.net/uploads/space/2022/0809/071835_nG5U_4937141.gif" width="700" referrerpolicy="no-referrer"></p> 
<p>新的 NavigationServer 增加了对使用 RVO2 库的避障支持，整个 API 现在比以前灵活多了。</p> 
<h3>3D 中的物理插值</h3> 
<p>现在你可以在项目设置中找到新的 <code>physics/common/physics_interpolation</code> 选项。启用这个设置后，Godot会自动对物体进行插值，使渲染的帧变得平滑。</p> 
<h3>通过 SceneTreeTween 实现更好的 Tweening</h3> 
<p>Tomasz Chabora 对 Godot 4.0 中的 Tween 类进行了彻底的修改，使其更加强大和灵活。Haoyu Qiu 将该功能作为 SceneTreeTween 回传到 Godot 3.5，以保留原有的 Tween，从而保持兼容性。在3.5 版本更新后，现在有两个独立的 Tween 实现，你可以继续使用原来的 3.x 版本，或者采用新的 4.0 版本的 API。</p> 
<h3>Time singleton</h3> 
<p>Aaron Franke 在 4.0 中添加了一个新的 <code>Time</code> 单例。 <code>Time</code> 单例为从操作系统中读取当前时间的各种方式提供了一个更好的抽象。在 4.0 中，各种与时间有关的方法被从 <code>OS</code> 单例移到了 <code>Time</code> 单例中。在 3.5 中，这些方法并没有从 <code>OS</code> 单例中移除，因此可以使用 <code>OS</code> 或 <code>Time</code> 单例的方法。</p> 
<h3>Label3D 和 TextMesh</h3> 
<p><img alt height="391" src="https://static.oschina.net/uploads/space/2022/0809/071904_p4At_4937141.gif" width="700" referrerpolicy="no-referrer"></p> 
<p>Godot 现在提供了期待已久的 Label3D 节点，用于在 3D 场景中显示文本。</p> 
<h3>通过唯一的名字访问节点</h3> 
<p><img alt height="342" src="https://static.oschina.net/uploads/space/2022/0809/071932_3csi_4937141.gif" width="700" referrerpolicy="no-referrer"></p> 
<p>Godot 3.5 为节点增加了 "scene unique names" 的概念，以帮助完成从脚本访问特定节点的常见任务。有 “scene unique names” 的节点可以在其场景中使用新的 <code>%</code> 名称前缀轻松引用。</p> 
<h3>新的 flow 容器</h3> 
<p>两个新的 flow 容器（HFlowContainer 和 VFlowContainer）以从左到右或从上到下的流方式垂直或水平排列子控制节点。</p> 
<p><img alt="https://godotengine.org/storage/app/media/3.5/flow.gif" src="https://static.oschina.net/uploads/img/202208/09072007_QAT1.gif" referrerpolicy="no-referrer"></p> 
<h3>异步着色器编译 + 缓存</h3> 
<p>一项期待已久的改善措施即将出现在 Godot 3.5 中，以减少 OpenGL 上着色器编译的卡顿现象。</p> 
<p>这个新系统为每个材质使用一个 "ubershader"（一个支持所有可能的渲染条件的大型着色器，速度慢，但在启动时编译，并可选择为未来的运行进行缓存）。</p> 
<p>这意味着在某些条件下，如第一次使用材质时，渲染可能会慢一两秒。这个功能默认是禁用的，可以在项目设置中的 <code>rendering/GLES3</code> 部分启用。</p> 
<h3>Android 编辑器的移植和优化</h3> 
<p>两年前开始致力于 Godot 编辑器的 Android 移植。由于 Godot 编辑器是由 Godot 本身构建的，所以通过一些构建系统的改变来编译 Android 的编辑器并不难。</p> 
<p>这项工作已合并到 Godot 3.5，目前的版本没有很多针对移动设备的改动，所以它只能在带键盘和鼠标的平板电脑上使用。</p> 
<h3>材料叠加</h3> 
<p>在 3.5 和 4.0 版本的 <code>MeshInstances</code> 中同时添加了新的 <code>material_overlay</code> 属性。 <code>material_overlay</code> 属性允许你指定一个材质，这个材质将被用来重新渲染 Mesh 的所有表面，并使用该材质。它的功能与 <code>SpatialMaterial</code> 的 <code>next_pass</code> 材质相同，但它适用于网格的所有表面，而不是只适用于 <code>SpatialMaterial</code> 的表面。</p> 
<p><img alt="https://godotengine.org/storage/app/media/3.5/enemy-material-slices.png" src="https://static.oschina.net/uploads/img/202208/09072009_7a2S.png" referrerpolicy="no-referrer"></p> 
<p>更多详情可查看：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgodotengine%2Fgodot%2Freleases" target="_blank">https://github.com/godotengine/godot/releases</a></p>
                                        </div>
                                      
</div>
            