
---
title: '蚂蚁图形引擎 Oasis v0.6 发布'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://static.oschina.net/uploads/space/2021/1121/083635_cDWf_2720166.gif'
author: 开源中国
comments: false
date: Sun, 21 Nov 2021 08:44:00 GMT
thumbnail: 'https://static.oschina.net/uploads/space/2021/1121/083635_cDWf_2720166.gif'
---

<div>   
<div class="content">
                                                                                            <p style="color:#333333; margin-left:0; margin-right:0; text-align:justify"><span>蚂蚁图形引擎 Oasis Engine 0.6 版本已发布，</span>Oasis Engine 是一个移动优先的高性能 Web 图形引擎，被广泛应用在支付宝五福、打年兽等各种互动业务中的图形引擎。</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:justify"><strong>主要变化：</strong></p> 
<ul> 
 <li style="margin-left: 0px; margin-right: 0px;"><span>新版本增加<strong>离线烘焙工具包，</strong>使用户能够更快更好地获得高质量的 PBR 渲染效果；</span></li> 
 <li style="margin-left: 0px; margin-right: 0px;"><span>增加强大的<strong><span> </span>PhysX 物理系统</strong>，在功能和性能上相比上个版本都有明显提升；</span></li> 
 <li style="margin-left: 0px; margin-right: 0px;"><span>增加<strong>输入系统</strong>，弥补了引擎在交互功能上的短板，大幅减少编写交互功能的代码量；</span></li> 
 <li style="margin-left: 0px; margin-right: 0px;"><span>还有其他微小而美好的功能打磨和更新...</span></li> 
</ul> 
<p style="margin-left:0px; margin-right:0px"><strong><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fmp.weixin.qq.com%2Fs%2FDkFzJYmjeA4jC9d3W5IwDQ" target="_blank"><span style="background-color:#ffffff; color:#333333">以下内容来自发布公告：</span></a></strong></p> 
<h2><strong style="color:#4b2911">渲染系统</strong></h2> 
<p><span style="background-color:#ffffff; color:#333333"><strong>新增离线烘焙工具包。</strong><span>在之前的 PBR 美术工作流中，不管是开发者还是美术开发者，都会因为 PBR 的复杂概念和 IBL 烘焙、漫反射球谐烘焙等美术资源的割裂，很难上手整个渲染流程。</span></span></p> 
<p><span style="background-color:#ffffff; color:#333333"><span>因此，我们开发了离线烘焙工具包，并集成到了</span><strong>编辑器</strong><span>和<span> </span></span><strong>glTF Viewer </strong></span><span style="background-color:#ffffff; color:#333333"><span>中，用户只需要从网上选择满意的<span> </span></span><strong>HDRI 贴图</strong></span><span style="background-color:#ffffff; color:#333333"><span>，然后上传到编辑器中，即可绑定环境贴图，其中的 IBL 离线烘焙、漫反射球谐烘焙等过程都会</span><strong>自动处理</strong><span>，就算您是零基础的用户，也能轻易上手。除此之外，我们在渲染侧实现了离线烘焙、HDR 渲染、色彩空间校正，PBR 的渲染效果也比之前更加逼真。</span></span></p> 
<p><img src="https://static.oschina.net/uploads/space/2021/1121/083635_cDWf_2720166.gif" referrerpolicy="no-referrer"></p> 
<p><span>由于编辑器暂未开放，直接使用引擎的开发者可以使用<span> </span><strong>glTF Viewe</strong>r ，将 HDRI 贴图拖入到<span> </span><strong>glTF Viewe</strong>r 中得到烘焙产物。使用详见教程：</span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Foasisengine.cn%2F0.6%2Fdocs%2Flight-cn%23ibl-%25E6%25A8%25A1%25E5%25BC%258F" target="_blank"><span>https://oasisengine.cn/0.6/docs/light-cn#ibl-%E6%A8%A1%E5%BC%8F</span></a></p> 
<p><img alt src="https://oscimg.oschina.net/oscnet/up-70eb3135d38eab515cf525a2cc4bafee12d.png" referrerpolicy="no-referrer"></p> 
<h2><strong style="color:#4b2911">物理系统</strong></h2> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:justify"><span><strong>新增物理系统</strong><span>。引入了由 WebAssembly 编译的</span><strong><span> </span></strong></span><span><strong>PhysX</strong></span><span><span> 作为物理系统的底层，并且设计了多后端架构。因此，我们对物理组件进行了一次合理的<span> </span></span><strong><span style="color:#f5222d">BreakingChange</span></strong><span>调整。在一套接口下，我们实现了<span> </span></span><strong><em>Physics-Lite</em></strong><strong>（轻量版，不依赖 PhysX，功能简单）</strong><span><span> </span>和</span><em><span> </span></em><strong><em>Physics-PhysX</em></strong><strong>（高级版，可以实现复杂的物理效果）</strong><span>两个物理包，前者基于0.5 版本中遗留的物理系统，后者基于 PhysX 4.1，兼容重度轻度物理场景与物理场景。开发者只需要在引擎初始化时进行配置，后续的开发过程中无需关心到底使用了哪种后端物理包。</span></span></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:justify"><span><span>除了接口的重构，</span><em>Physics-Lite</em><span><span> </span>在功能上也做了同步升级，支持多<span> </span></span></span><code><span>ColliderShape</span></code><span><span><span> </span>的组合。未来我们主要会开发<span> </span></span><em>Physics-PhysX</em><span>，并且适度增强<span> </span></span><em>Physics-Lite</em><span><span> </span>的功能以支持轻量级应用。使用详见文档：</span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Foasisengine.cn%2F0.6%2Fdocs%2Fcollider-cn" target="_blank">https://oasisengine.cn/0.6/docs/collider-cn</a></span></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:justify"><span>编辑器也全面适配最新的物理组件，添加UI列表功能，使得在同一个碰撞器中添加多种<span> </span></span><code><span>ColliderShape</span></code><span><span> </span>：</span></p> 
<p><img alt src="https://oscimg.oschina.net/oscnet/up-e3835ac868a970a02700d91565c18b8d98f.png" referrerpolicy="no-referrer"></p> 
<p><span style="background-color:#ffffff; color:#333333">详细接口设计与架构可以参考<span> </span></span><span style="background-color:#ffffff; color:#333333">Wiki</span><span style="background-color:#ffffff; color:#333333">，后续会在公众号等平台推出《<span style="color:#262626">Oasis 物理第二弹：物理多后端与组件架构设计</span>》，《Oasis 物理第三弹：实现轻量级碰撞检测算法包》等一系列介绍 PhysX 以及物理组件架构的技术文章。</span></p> 
<h2><strong style="color:#4b2911">输入系统</strong></h2> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:justify"><span><strong>新增输入系统</strong>。该系统是引擎功能长期缺失的部分，之前开发者反馈实现点击等交互需求的代码比较繁琐，v0.6 全新的输入系统将大幅减少编写交互功能的代码量。支持了<span> </span><strong>Pointer</strong><span> </span>类型的事件，<strong>抹平了鼠标和触屏事件的差异</strong>，能够满足常用的点击、拖拽等交互需求，并且在<strong>脚本组件的生命周期函数</strong>中增加对交互事件的响应，简化了注册输入事件的成本。鼠标滚轮（Wheel）、键盘（Keyborad）等事件会在以后的版本中支持。</span></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:justify"><span>使用详见文档：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Foasisengine.cn%2F0.6%2Fdocs%2Finput-cn" target="_blank">https://oasisengine.cn/0.6/docs/input-cn</a></span></p> 
<p><img src="https://static.oschina.net/uploads/space/2021/1121/083921_hhSm_2720166.gif" referrerpolicy="no-referrer"></p> 
<h2><strong style="color:#4b2911">其他更新</strong></h2> 
<h3 style="color:#333333; margin-left:0px; margin-right:0px; text-align:justify"><span><strong><span>引擎功能</span></strong></span></h3> 
<ul style="margin-left:0; margin-right:0"> 
 <li style="margin-left: 0px; margin-right: 0px;"><span>动画系统增加了状态机脚本</span><span>，开发者可以方便的在动画状态开始/更新/结束处编写自己的业务逻辑。</span></li> 
 <li style="margin-left: 0px; margin-right: 0px;"><code><span>PrimitiveMesh</span></code><span><span> </span>新增<span> </span></span><code><span>createCapsule()</span></code><span><span> </span>方法，可快速方便的创建圆柱体。</span></li> 
 <li style="margin-left: 0px; margin-right: 0px;"><code><span>Texture2D</span></code><span>、</span><code><span>RenderColorTexture</span></code><span><span> </span>和<span> </span></span><code><span>RenderColorTexture</span></code><span><span> </span>的读取像素接口<span> </span></span><code><span>getPixelBuffer()</span></code><span><span> </span>增加<span> </span></span><code><span>miplevel</span></code><span><span> </span>参数，可以指定读取像素的纹理等级。</span></li> 
 <li style="margin-left: 0px; margin-right: 0px;"><span>Camera.render() 方法增加<span> </span></span><code><span>miplevel</span></code><span><span> </span>参数，可指定渲染的纹理等级。</span></li> 
 <li style="margin-left: 0px; margin-right: 0px;"><span>glTF 解析<span> </span></span><code><span>ModelMesh</span></code><span><span> </span>时支持更多 UV 通道和顶点色。</span></li> 
 <li style="margin-left: 0px; margin-right: 0px;"><span>Animator 增加<span> </span></span><code><span>getCurrentAnimatorState()</span></code><span>，可以获取当前播放的动画状态。</span></li> 
 <li style="margin-left: 0px; margin-right: 0px;"><span>精灵 Sprite 增加克隆功能。</span></li> 
 <li style="margin-left: 0px; margin-right: 0px;"><span>四元数 Quaternion 增加<span> </span></span><code><span>rotateAxisAngle()</span></code><span><span> </span>方法。</span></li> 
 <li style="margin-left: 0px; margin-right: 0px;"><span>SkyBox 材质增加 RGBM HDR 编码格式支持。</span></li> 
 <li style="margin-left: 0px; margin-right: 0px;"><span>引擎入参增加色彩空间配置，默认线性空间。</span></li> 
 <li> <p style="margin-left:0; margin-right:0"><span>直接光照改为物理单位，即除以 PI。如果觉得之前的场景变暗，属于正常现象，可以尝试添加HDR环境贴图。</span></p> </li> 
</ul> 
<ul style="margin-left:0; margin-right:0"> 
</ul> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:justify"><span>详见 Change Log：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Foasis-engine%2Fengine%2Freleases%2Ftag%2Fv0.6.0" target="_blank">https://github.com/oasis-engine/engine/releases/tag/v0.6.0</a></span></p> 
<h3 style="margin-left:0; margin-right:0; text-align:justify"><span><strong>编辑器功能</strong></span></h3> 
<ul style="margin-left:0; margin-right:0"> 
 <li style="margin-left: 0px; margin-right: 0px;"><span>资产面板新增目录树功能，支持资产拖拽移动。</span></li> 
</ul> 
<p style="margin-left:0px; margin-right:0px"><img src="https://static.oschina.net/uploads/space/2021/1121/084056_rFoQ_2720166.gif" referrerpolicy="no-referrer"></p> 
<ul style="margin-left:0; margin-right:0"> 
 <li style="margin-left: 0px; margin-right: 0px;"><span>优化 Gizmo 用户体验。</span></li> 
 <li style="margin-left: 0px; margin-right: 0px;"><span>新增脚本组件名字优化。</span></li> 
 <li style="margin-left: 0px; margin-right: 0px;"><span>完成雨燕工程的打通。</span></li> 
 <li style="margin-left: 0px; margin-right: 0px;"><span>修复若干 Bug，优化体验。</span></li> 
</ul> 
<h3 style="margin-left:0; margin-right:0; text-align:justify"><strong>示例</strong></h3> 
<table cellspacing="0"> 
 <tbody> 
  <tr> 
   <td style="border-color:#d9d9d9; border-style:solid; border-width:1px; height:33px"> <p style="margin-left:0; margin-right:0">分类</p> </td> 
   <td style="border-color:#d9d9d9; border-style:solid; border-width:1px; height:33px"> <p style="margin-left:0; margin-right:0">示例</p> </td> 
  </tr> 
  <tr> 
   <td style="border-color:#d9d9d9; border-style:solid; border-width:1px; height:43px"> <p style="margin-left:0; margin-right:0">Mesh</p> </td> 
   <td style="border-color:#d9d9d9; border-style:solid; border-width:1px; height:43px"> 
    <ul style="margin-left:0; margin-right:0"> 
     <li> <p style="margin-left:0; margin-right:0">More Primitive Mesh</p> </li> 
    </ul> </td> 
  </tr> 
  <tr> 
   <td style="border-color:#d9d9d9; border-style:solid; border-width:1px; height:34px"> <p style="margin-left:0; margin-right:0">动画</p> </td> 
   <td style="border-color:#d9d9d9; border-style:solid; border-width:1px; height:34px"> 
    <ul style="margin-left:0; margin-right:0"> 
     <li> <p style="margin-left:0; margin-right:0">Animation State Machine Script</p> </li> 
    </ul> </td> 
  </tr> 
  <tr> 
   <td style="border-color:#d9d9d9; border-style:solid; border-width:1px; height:34px"> <p style="margin-left:0; margin-right:0">物理</p> </td> 
   <td style="border-color:#d9d9d9; border-style:solid; border-width:1px; height:34px"> 
    <ul style="margin-left:0; margin-right:0"> 
     <li> <p style="margin-left:0; margin-right:0">Lite Collision Detection</p> </li> 
     <li> <p style="margin-left:0; margin-right:0">Lite Raycast</p> </li> 
    </ul> 
    <ul style="margin-left:0; margin-right:0"> 
     <li> <p style="margin-left:0; margin-right:0">PhysX Collision Detection</p> </li> 
     <li> <p style="margin-left:0; margin-right:0">PhysX Raycast</p> </li> 
    </ul> </td> 
  </tr> 
  <tr> 
   <td style="border-color:#d9d9d9; border-style:solid; border-width:1px; height:34px"> <p style="margin-left:0; margin-right:0">材质</p> </td> 
   <td style="border-color:#d9d9d9; border-style:solid; border-width:1px; height:34px"> 
    <ul style="margin-left:0; margin-right:0"> 
     <li> <p style="margin-left:0; margin-right:0">PBR Helmet</p> </li> 
     <li> <p style="margin-left:0; margin-right:0">PBR Base</p> </li> 
    </ul> 
    <ul style="margin-left:0; margin-right:0"> 
     <li> <p style="margin-left:0; margin-right:0">IBL Baker && HDR/LDR</p> </li> 
     <li> <p style="margin-left:0; margin-right:0">glTF Viewer</p> </li> 
    </ul> </td> 
  </tr> 
  <tr> 
   <td style="border-color:#d9d9d9; border-style:solid; border-width:1px; height:33px"> <p style="margin-left:0; margin-right:0">交互</p> </td> 
   <td style="border-color:#d9d9d9; border-style:solid; border-width:1px; height:33px"> 
    <ul style="margin-left:0; margin-right:0"> 
     <li> <p style="margin-left:0; margin-right:0">Input Manager</p> </li> 
    </ul> </td> 
  </tr> 
  <tr> 
   <td style="border-color:#d9d9d9; border-style:solid; border-width:1px; height:33px"> <p style="margin-left:0; margin-right:0">场景</p> </td> 
   <td style="border-color:#d9d9d9; border-style:solid; border-width:1px; height:33px"> 
    <ul style="margin-left:0; margin-right:0"> 
     <li> <p style="margin-left:0; margin-right:0">Video Background</p> </li> 
    </ul> </td> 
  </tr> 
 </tbody> 
</table> 
<h2>0.7 版本预告</h2> 
<ul> 
 <li style="margin-left: 0px; margin-right: 0px;"><strong>物理</strong>：进一步挖掘 PhysX 物理引擎特性，扩充 DynamicCollider 的方法以支持刚体运动，并且增加刚体约束，角色控制器等组件。</li> 
 <li style="margin-left: 0px; margin-right: 0px;"><strong>纹理：</strong>对纹理的结构进行整合重构，并新增 Texture 纹理数组等功能。</li> 
 <li style="margin-left: 0px; margin-right: 0px;"><strong>文字：</strong>增加 2D 文字系统，进一步完善功能闭环和 2D 能力。</li> 
</ul> 
<p style="margin-left:0px; margin-right:0px"><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Foasis-engine%2Fengine%2Freleases%2Ftag%2Fv0.6.0" target="_blank">详情查看 release note</a>。</p>
                                        </div>
                                      
</div>
            