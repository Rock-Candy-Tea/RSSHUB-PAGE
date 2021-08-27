
---
title: 'Cocos Creator 3.3 发布，实现 3D 技术突破，优化 2D 性能体验'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://oscimg.oschina.net/oscnet/up-e619ad3eca6561e11b0095b0082328c9638.png'
author: 开源中国
comments: false
date: Fri, 27 Aug 2021 07:34:00 GMT
thumbnail: 'https://oscimg.oschina.net/oscnet/up-e619ad3eca6561e11b0095b0082328c9638.png'
---

<div>   
<div class="content">
                                                                                            <p>Cocos Creator 3.3 正式版已发布。</p> 
<p><img alt src="https://oscimg.oschina.net/oscnet/up-e619ad3eca6561e11b0095b0082328c9638.png" referrerpolicy="no-referrer"></p> 
<p><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.cocos.com%2Fcocos-creator-3-3-%25e4%25bb%258a%25e6%2597%25a5%25e5%258f%2591%25e5%25b8%2583%25ef%25bc%258c%25e5%25ae%259e%25e7%258e%25b0-3d-%25e6%258a%2580%25e6%259c%25af%25e7%25aa%2581%25e7%25a0%25b4%25ef%25bc%258c%25e4%25bc%2598%25e5%258c%2596-2d-%25e6%2580%25a7%25e8%2583%25bd%25e4%25bd%2593%25e9%25aa%258c%239569" target="_blank">发布公告写道</a>，早在 v3.0 正式发布时，Cocos 便升级成为 2D & 3D 能力兼备的游戏引擎，不论是多后端渲染框架、还是所见即所得的编辑器，以及 PBR 物理渲染，已经让 Cocos 具备完整开发 3D 手游和小游戏的能力。当版本升级到 v3.1，延时渲染管线的出现和 PhysX 物理支持，则让 Cocos 具备更大的底气，为 Cocos 在移动端挑战次世代品质的游戏画面奠定了基础。而与华为、字节跳动的深度合作，更是为 Cocos 开拓更多可能性——v3.2.0 的更新，让 Cocos 成为全球首家支持鸿蒙系统的游戏引擎，为之后的游戏领域布局，带来深远的影响。</p> 
<p>现在 Cocos Creator 3.3 正式版的发布，基于对引擎性能提升的自信，以及之前对 3D 研发投入的厚积薄发，开发团队制作了「赛博朋克」技术演示视频。</p> 
<p><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.bilibili.com%2Fvideo%2FBV1uA411c7La" target="_blank"><img alt src="https://oscimg.oschina.net/oscnet/up-cbcdf3ddb7d2784aa6b153cb1a9d36dd55b.png" referrerpolicy="no-referrer"></a></p> 
<p>▲点击观看 DEMO 用 Cocos Creator 的实时渲染效果</p> 
<p>下面介绍一下 Cocos Creator 3.3 带来的一些全新变化：</p> 
<h2><strong>性能优化</strong></h2> 
<h3><strong>启动性能优化</strong></h3> 
<p>此次更新，Cocos Creator 3.3 认真对引擎性能做了一波优化，特别是在<strong>小游戏平台</strong>。版本更新后，小游戏的<strong>启动性能、运行性能等</strong>都有了显著提升，其中在启动性能更是提升了60%。</p> 
<p>在启动性能方面，通过升级之前发布的小游戏「快上车」，可以很明显地看出，在最新的 v3.3 里，相较之前，项目升级后微信云测启动性能分达到83分，提升了60%。</p> 
<p><img alt src="https://oscimg.oschina.net/oscnet/up-b584937da96b5da0aadccaec24bd4dbbb12.png" referrerpolicy="no-referrer"> <img alt src="https://oscimg.oschina.net/oscnet/up-3e2f0c6b6f5fc9e1625360d9f7fd9cc1f4c.png" referrerpolicy="no-referrer"></p> 
<h3><strong>运行性能优化</strong></h3> 
<p>除了启动性能升，运行性能也做出了不错的优化。以「奔跑吧小仙女」跑酷游戏为例，v3.3 的云测数据，和 v3.0 版相比，运行性能提升了34%。</p> 
<p><img alt src="https://oscimg.oschina.net/oscnet/up-b560c047149cde44446f801aea20886ae31.png" referrerpolicy="no-referrer"> <img alt src="https://oscimg.oschina.net/oscnet/up-88ef523f8d4bac2d102cf77c5853e0d87fa.png" referrerpolicy="no-referrer"></p> 
<h3><strong>物理性能优化</strong></h3> 
<p>目前，微信小游戏全面支持了 WebAssembly (简称 wasm) 的运行，<strong>而 Cocos Creator 3.3 则支持在此基础上将 Bullet 以 WASM 的方式运行，</strong>使得 Bullet 的物理性能有很大提升，开发者可以用在更多复杂的物理场景。</p> 
<p>通过和 ASMJS 版本测试对比，可以看出在 iOS 和安卓版本上，Wasm 版本的物理运行效率有了显著提升，在 iOS 上的提升尤其明显。同时，越复杂的场景提升越明显。在构建微信平台时，如果选择 Bullet 物理后端，Cocos Creator 会自动构建 WASM 包，非常方便，便于大家尝试更多复杂物理功能的游戏。</p> 
<p><img alt src="https://oscimg.oschina.net/oscnet/up-15c5598542a38fc1eec91757ceb1f978383.png" referrerpolicy="no-referrer"></p> 
<h3><strong>原生性能架构优化</strong></h3> 
<p>同时，新版本进一步提升了原生引擎的绑定层级，在渲染管线之上的渲染场景部分也完成了原生化，光源、模型等渲染对象的收集过程使用原生实现，进一步提升了原生平台的性能。</p> 
<p>还有一个附带的好处，由于绑定层级的向上迁移，一些底层的数据共享机制被解除了，比如 Pass，SubModel  等。这使得 JS 引擎上层的实现尤其是 UI 和 2D 渲染合批相关的数据更加简化，部分高频操作的数据结构从 TypedArray 还原为直接量属性，使得 Web 和小游戏平台的性能也得到了可见的提升。</p> 
<h2><strong>优化场景编辑：细节优化带来编辑体验感提升</strong></h2> 
<p>在 v3.x 的引擎功能狂飙突进中，开发团队前期更注重实际功能的开发，而忽略了不少操作细节体验。在 v3.3 中，他们对场景编辑进行了一些相对应的优化：</p> 
<ol> 
 <li>优化场景相机的漫游模式，并增加了加速开关；</li> 
 <li>增加一个场景灯光的开关（默认打开）；</li> 
 <li>增加模型的最大最小坐标显示：<br> <img alt src="https://oscimg.oschina.net/oscnet/up-e33f9d9daabf203deeb014499449aa19921.png" referrerpolicy="no-referrer"></li> 
 <li>增加 Transform Gizmo 的吸附功能（通过移动，旋转，缩放的 Gizmo 操作时，按住 Ctrl 键，就可以按设定的步长进行值的增长：<br> <img alt src="https://oscimg.oschina.net/oscnet/up-b89d93fe7927a2999727bf7624b1df2fee2.png" referrerpolicy="no-referrer"></li> 
 <li>优化大项目使用体验：降低编辑器内存使用，避免崩溃，优化卡顿。</li> 
</ol> 
<h2><strong>新版动画编辑器和动画数据升级</strong></h2> 
<p>目前动画编辑器已在动画编辑器内置曲线编辑，与时间轴匹配，并支持任意关键帧之间的时间曲线编辑。</p> 
<p>同时，在 v3.3 中，动画数据已完成升级：引入了新的基础曲线类，重构了 AnimationClip，统一了动画和粒子系统使用的曲线数据。这些工作都是为了后续的完善动画系统而准备的，后续版本将支持动画状态机编辑、Blend Tree 动画融合等高级功能。</p> 
<h2><strong>阴影效果和设置优化</strong></h2> 
<p>针对大家比较关注的阴影的配置，开发团队称已经有完整的规划，并正在逐步完善。3.3 版本就首先简化阴影的配置，优化软阴影算法，修复阴影的部分效果问题。配置上的调整包含：</p> 
<ul> 
 <li>Shadow color 被迁移为 Shadow saturation 的灰度调节选项，会自动迁移老版本的 alpha 通道</li> 
 <li>软阴影选项从之前的 X9，X25 等改为 Soft 和 Soft2X</li> 
 <li>简化阴影贴图的尺寸设置为 High，Medium，Low</li> 
 <li>去除 SelfShadow 选项，现在都会默认开启自阴影计算</li> 
</ul> 
<p><img alt src="https://oscimg.oschina.net/oscnet/up-ed78c696dc2a4e828de718d49bce6e3dadf.png" referrerpolicy="no-referrer"></p> 
<p><img alt src="https://oscimg.oschina.net/oscnet/up-752efde06c0a51653346a39d4d4f48a4cff.png" referrerpolicy="no-referrer"></p> 
<h2><strong>物理系统完善</strong></h2> 
<p>在 v3.1 支持 PhysX 物理后端以来，多套物理引擎的选择和使用也成为了重点关注的使用体验，v3.3 试图尽可能统一不同物理后端的物理表现。并且，还添加了对射击类和赛车类游戏非常关键的 CCD 持续碰撞检测能力。</p> 
<hr> 
<p>更多更新请查看 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fforum.cocos.org%2Ft%2Ftopic%2F119306" target="_blank">Cocos Creator 3.3 完整更新文档</a>，也可<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.cocos.com%2Fcreator" target="_blank">前往官网浏览文档、下载最新版本</a>。</p>
                                        </div>
                                      
</div>
            