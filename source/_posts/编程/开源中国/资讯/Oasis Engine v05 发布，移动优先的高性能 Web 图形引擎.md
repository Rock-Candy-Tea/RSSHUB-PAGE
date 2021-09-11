
---
title: 'Oasis Engine v0.5 发布，移动优先的高性能 Web 图形引擎'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://static.oschina.net/uploads/space/2021/0204/161444_8Kdg_2720166.jpg'
author: 开源中国
comments: false
date: Sat, 11 Sep 2021 07:23:00 GMT
thumbnail: 'https://static.oschina.net/uploads/space/2021/0204/161444_8Kdg_2720166.jpg'
---

<div>   
<div class="content">
                                                                                            <div> 
 <p>Oasis Engine v0.5 已发布。Oasis Engine 是一个移动优先的高性能 Web 图形引擎，被广泛应用在支付宝五福、打年兽等各种互动业务中的图形引擎。</p> 
 <p><img alt="161444_8Kdg_2720166.jpg" src="https://static.oschina.net/uploads/space/2021/0204/161444_8Kdg_2720166.jpg" referrerpolicy="no-referrer"></p> 
 <p><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fmp.weixin.qq.com%2Fs%2F4ryPSE0zvDuFA6AeeT7dIA" target="_blank">发布公告写道</a>：</p> 
 <blockquote> 
  <p>本次里程碑重点重新设计了<strong>动画系统</strong>，提供了全新的 <strong>Animator</strong> 组件并支持了 <strong>BlendShape</strong> 动画，动画能力得到大幅提升。<strong>渲染</strong>方面重新设计了 <strong>PBR 材质</strong>接口，环境光的漫反射部分提供了<strong>球谐</strong>模式，PBR 工作流得到提升。<strong>2D</strong> 方面增加了<strong>精灵图集</strong>功能，Spine 增强了换肤能力，Lottie 动画也集成到编辑器中。官网支持<strong>中英文</strong>双语，新增<strong> 20+</strong> 示例。</p> 
 </blockquote> 
 <p>以下内容来自发布公告：</p> 
 <h2><strong>动画</strong></h2> 
 <h3><strong>Animtor</strong></h3> 
 <p>动画是引擎必不可少的核心系统，可以让原本静态的场景生动起来。随着动画相关功能的需求越来越多，以及考虑未来引擎动画系统的健康发展，此次我们重新设计了动画系统，在功能、易用性和性能均带来不同程度的提升，同时也为动画系统未来的功能扩展打下了基础。主要升级点如下（详见文档）：</p> 
 <ul> 
  <li> <p><strong>动画过渡：</strong>不再需要目标动画和原动画严格的骨骼匹配即可进行动画的过渡，可以很大程度减少设计师的工作量。</p> </li> 
  <li> <p><strong>动画叠加：</strong>改为依照所属动画层的混合模式及权重进行叠加并支持多层的动画叠加，你可以轻松的叠加多个动作而不只是之前的两个。</p> </li> 
 </ul> 
 <ul> 
  <li> <p><strong>动画状态机能力</strong>：你可以通过动画状态机去管理你的项目动画，状态与状态的切换会自动为你加上你设置好的过渡，暂时还不支持条件切换，该功能会在下个里程碑添加。</p> </li> 
  <li> <p><strong>动画状态裁剪</strong>：你可以对已有的动画切片进行裁剪而达到复用，而不需要设计师重新制作。</p> </li> 
 </ul> 
 <ul> 
  <li> <p><strong>动画事件：</strong>改为脚本化的驱动方式，使用方式更加灵活简单。</p> </li> 
 </ul> 
 <p>新版动画系统在性能上提升了 <strong>30% </strong>左右：</p> 
 <p><img alt src="https://oscimg.oschina.net/oscnet/up-f69a42008f21d32d7d9e263283586e05849.png" referrerpolicy="no-referrer"></p> 
 <p>老版动画系统</p> 
 <p><img alt src="https://oscimg.oschina.net/oscnet/up-92b1bfb56a89ac8ed6b821dca585e3431fc.png" referrerpolicy="no-referrer"></p> 
 <p>新版动画系统</p> 
 <p><em>测试环境：机型：Mi 11 Pro  |  浏览器：Chrome 92.0.4515.131  |  系统版本：Android11</em></p> 
 <p>除了引擎功能之外，编辑器也增加了动画编辑能力。通过 Animator 编辑器，你可以在上面方便的为动画添加过渡和叠加。</p> 
 <h3><strong>BlendShape</strong></h3> 
 <p>BlendShape（MorphTarget）动画是一种常见的动画表现形式，尤其在精细动画表现方面被广泛应用，比如角色面部表情动画。我们为 <code>ModelMesh</code> 新增了 <code>BlendShape</code> 能力。此外我们还支持了 glTF 模型的 BlendShape 动画解析导入，并与新版的 <code>Animator</code> 系统进行了深度融合，和蒙皮动画一样，开发者加载带有 BlendShape 动画的 glTF 后只需调用 <code>Animator</code> 动画组件的 <code>play()</code> 接口即可播放使用，无需任何额外操作。详见文档。</p> 
 <p><img src="https://static.oschina.net/uploads/space/2021/0910/153133_S8yM_2720166.gif" referrerpolicy="no-referrer"></p> 
 <h2><strong>渲染</strong></h2> 
 <h3><strong>IBL 球谐</strong></h3> 
 <p>在 PBR 工作流中，我们可以设置环境光的漫反射和镜面反射来达到 <strong>IBL</strong>（<strong>基于图像的照明</strong>）。不同于镜面反射，漫反射因为光反射波瓣很大，得到的是比较<strong>低频</strong>的信号，即看上去像是一张高斯模糊过后的贴图。在之前的版本中，我们通过设置环境光的 diffuseMode，来切换漫反射为纯色模式或者<strong>纹理模式</strong>，也就是说我们之前需要上传一张立方体纹理（6张贴图）才能实现漫反射的低频信号，而且占用了一个着色器的宝贵纹理单元；此次我们使用3阶球谐函数，即9个不同方向上的颜色值，27个数字（9*3 RGB）代替立方体纹理模式，不仅释放了一个着色器的纹理单元，而且带来了更好的效果。详见文档。（烘焙工具见下文预告）</p> 
 <p><img alt src="https://oscimg.oschina.net/oscnet/up-a9fb473ac7a08334d7c6dd57afcb50ca7f5.png" referrerpolicy="no-referrer"></p> 
 <h3><strong>PBR 接口重构</strong></h3> 
 <p>在过往的PBR材质接口设计中，我们妥协了太多业务衍生出来的接口，比如透明度贴图，其实完全可以合并到基础纹理的透明通道中来代替实现，不够纯粹的接口不仅使开发者感到迷茫，也会使运算性能下降。因此，经过对合理性和未来扩展性的充分考虑，我们对 PBR 材质接口进行了一次合理的 BreakingChange 调整，接口变动详见 PR 讨论。</p> 
 <h3><strong>背景纹理模式</strong></h3> 
 <p>场景中背景支持纹理模式的设置，可使用一张图片作为场景背景。详见文档。</p> 
 <p><img src="https://static.oschina.net/uploads/space/2021/0910/153230_fEuA_2720166.gif" referrerpolicy="no-referrer"></p> 
 <h2><strong>2D</strong></h2> 
 <h3><strong>SpriteAtlas</strong></h3> 
 <p>精灵图集是 2D 项目常用的优化手段，它可以带来更少的绘制次数，更少的显存占用和更少的资源请求次数，从而大大提升渲染性能，在 Oasis 中我们也引入了 <code>SpriteAtlas</code> 类来增加这项能力，开发者只需要加载图集资源便可得到 <code>SpriteAtlas</code> 实例，然后根据精灵名称获取对应的精灵即可。详见文档。<br> <br> 为了帮助开发者更便捷的使用 SpriteAtlas，Oasis 为开发者提供了图集打包 Tool-Atlas 工具，可以本地快速导出 SpriteAtlas 需要的 .atlas 文件。此外，在编辑器中已集成 Tool-Atals，开发者只需要选择需要打包的精灵，即可自动完成打包，如下：</p> 
 <p><img src="https://static.oschina.net/uploads/space/2021/0910/153255_teu3_2720166.gif" referrerpolicy="no-referrer"></p> 
 <h2><strong>物理系统</strong></h2> 
 <p>在今年的 roadmap 规划中，Oasis 将物理相关功能的研发列为重点。本次里程碑对物理触发器事件的使用方式进行了改良，将其脚本化，和其他逻辑事件一样统一使用脚本回调的方式处理，在 <code>Script</code> 当中增加了对应的接口（详见文档）：</p> 
 <p><img alt src="https://oscimg.oschina.net/oscnet/up-8fa2eead9cdc7067d13d08755613bb45112.png" referrerpolicy="no-referrer"></p> 
 <p>同时，对 <code>raycast()</code> 接口也进行了重新的设计。新增了 <code>PhysicsManager</code>，将 <code>raycast()</code> 接口由场景调整至<code>PhysicsManager</code> ，同时也为后期接入更多的物理功能提供了便利。详见Raycast 文档、Collision-Detection 文档。</p> 
 <p>经过性能和功能上的权衡，Oasis 未来会首选 PhysX 作为物理底层的核心部分。本次里程碑发布了使用 EmScripten 编译的 PhysX.js 仓库，该仓库提供了非常便捷的编译脚本，以及对应的 NVIDIA PhysX Visual Debugger 联调配置。该仓库独立于 Oasis 引擎，欢迎感兴趣的朋友和同行共建并提出 Issue。</p> 
 <h2><strong>生态</strong></h2> 
 <h3><strong>Spine 组件</strong></h3> 
 <p>oasis spine在0.5里程碑优化了 buffer 数据的处理方式，一方面优化了内存，另一方面解决了顶点总数扩大时带来的渲染问题。详见文档。优化后，新版运行时能够支持 spine 以下换装能力：</p> 
 <ol> 
  <li> <p>全套皮肤更换</p> </li> 
 </ol> 
 <p><img src="https://static.oschina.net/uploads/space/2021/0910/153336_rQQo_2720166.gif" referrerpolicy="no-referrer"></p> 
 <ol start="2"> 
  <li> <p>单附件更换</p> </li> 
 </ol> 
 <p><img alt src="https://oscimg.oschina.net/oscnet/up-39522a9451706ed068290e0775a0c42f08a.png" referrerpolicy="no-referrer"></p> 
 <ol start="3"> 
  <li> <p>皮肤混搭</p> </li> 
 </ol> 
 <p>新增了<code>addSeparateSlot</code> 与 <code>hackSeparateSlotTexture</code> API。能够从动画中拆分指定名称的插槽并替换其材质，实现皮肤混搭的效果。</p> 
 <p><img alt src="https://oscimg.oschina.net/oscnet/up-2510f66da02ae1da65c4b52481ceb97caf4.png" referrerpolicy="no-referrer"></p> 
 <h3><strong>Lottie 组件</strong></h3> 
 <p>考虑到和引擎 2D 底层能力（比如 atlas、蒙版）的整合，本次对 Lottie runtime 进行了全面的重构，并且提供了命令行工具 tool-atlas-lottie 来帮助用户把原生的 lottie JSON 文档转成符合 Oasis atlas 标准的文件。详见文档。此外，也支持在编辑器中添加 Lottie 资产和组件，通过云端的转换能力代替命令行工具实现文件格式转换。详见文档。</p> 
 <h2><strong>其他更新</strong></h2> 
 <p>功能更新：</p> 
 <ul> 
  <li> <p>引擎：BlinnPhone 材质支持顶点色；</p> </li> 
  <li> <p>引擎：Color 增加常用方法；</p> </li> 
  <li> <p>编辑器：新加纹理一键生成 Sprite 资源，并自定绑定纹理；</p> </li> 
  <li> <p>编辑器：集成图集打包工具 Atlas；</p> </li> 
  <li> <p>编辑器：增加项目升级引擎版本功能；</p> </li> 
  <li> <p>编辑器：样式改版与交互优化。</p> </li> 
 </ul> 
 <p>文档进行了全面的整合优化：</p> 
 <ul> 
  <li> <p>新增 第一个游戏 ，精灵图集 等引擎文档；</p> </li> 
  <li> <p>新增 29 篇编辑器文档；</p> </li> 
 </ul> 
 <ul> 
  <li> <p>优化 33 篇文档；</p> </li> 
  <li> <p>网站支持中英文双语。</p> </li> 
 </ul> 
 <p>新增 24 个示例：</p> 
 <table style="width:553px"> 
  <tbody> 
   <tr> 
    <td> <p>分类</p> </td> 
    <td> <p>示例</p> </td> 
   </tr> 
   <tr> 
    <td> <p>2D</p> </td> 
    <td> 
     <ul> 
      <li> <p>Sprite Pivot 优化</p> </li> 
      <li> <p>Sprite SheetAnimation 优化</p> </li> 
     </ul> 
     <ul> 
      <li> <p>Sprite Material Glitch RGB Split</p> </li> 
      <li> <p>Sprite Atlas</p> </li> 
     </ul> 
     <ul> 
      <li> <p>Flappy Bird</p> </li> 
     </ul> </td> 
   </tr> 
   <tr> 
    <td> <p>Spine</p> </td> 
    <td> 
     <ul> 
      <li> <p>Spine Skin Change</p> </li> 
      <li> <p>Spine Change Attachment</p> </li> 
     </ul> 
     <ul> 
      <li> <p>Spine Hack Slot Texture</p> </li> 
     </ul> </td> 
   </tr> 
   <tr> 
    <td> <p>Lottie</p> </td> 
    <td> 
     <ul> 
      <li> <p>性能基线</p> </li> 
     </ul> </td> 
   </tr> 
   <tr> 
    <td> <p>动画</p> </td> 
    <td> 
     <ul> 
      <li> <p>动画状态播放</p> </li> 
      <li> <p>动画过渡</p> </li> 
     </ul> 
     <ul> 
      <li> <p>动画叠加</p> </li> 
      <li> <p>动画事件</p> </li> 
     </ul> 
     <ul> 
      <li> <p>BlendShape 动画</p> </li> 
     </ul> </td> 
   </tr> 
   <tr> 
    <td> <p>物理</p> </td> 
    <td> 
     <ul> 
      <li> <p>Raycast</p> </li> 
      <li> <p>Collision Detection</p> </li> 
     </ul> </td> 
   </tr> 
   <tr> 
    <td> <p>灯光</p> </td> 
    <td> 
     <ul> 
      <li> <p>Light Type</p> </li> 
      <li> <p>Ambient light</p> </li> 
     </ul> </td> 
   </tr> 
   <tr> 
    <td> <p>纹理</p> </td> 
    <td> 
     <ul> 
      <li> <p>Texture Mipmap</p> </li> 
      <li> <p>Texture Anisotropic</p> </li> 
     </ul> </td> 
   </tr> 
   <tr> 
    <td> <p>相机</p> </td> 
    <td> 
     <ul> 
      <li> <p>多相机</p> </li> 
      <li> <p>RenderTarget</p> </li> 
     </ul> 
     <ul> 
      <li> <p>多视图</p> </li> 
     </ul> </td> 
   </tr> 
   <tr> 
    <td> <p>场景</p> </td> 
    <td> 
     <ul> 
      <li> <p>纹理背景</p> </li> 
     </ul> </td> 
   </tr> 
  </tbody> 
 </table> 
 <p>整体单测覆盖率从 0.4 版本的 45% 提升到了 <strong>49%</strong>：</p> 
 <ul> 
  <li> <p>完善数学库单测。</p> </li> 
  <li> <p>补充材质单测。</p> </li> 
 </ul> 
 <p>研发详情：</p> 
 <ul> 
  <li> <p>里程碑0.5</p> <p>https://github.com/oasis-engine/engine/milestone/3?closed=1</p> </li> 
  <li> <p>Change Log</p> <p>https://github.com/oasis-engine/engine/releases/tag/v0.5.0</p> </li> 
 </ul> 
 <h2><strong>0.6 里程碑预告</strong></h2> 
 <h3><strong>IBL 烘焙</strong></h3> 
 <p>现在的 IBL 烘焙（各个 mipmap 级别的镜面反射贴图、漫反射球谐）都是交给开发者使用业界工具比如 IBL-Baker 制作，因为概念复杂以及工作流的割裂，很多开发者其实并没有充分利用 IBL 技术，使得 Oasis 的PBR 效果并不是那么有优势。因此在接下来的 0.6 里程碑中，Oasis 将推出自己的 IBL 离线烘焙工具，并集成到编辑器和官网中，使开发者能够快速接入 PBR 工作流。</p> 
 <h3><strong>物理</strong></h3> 
 <p>Oasis 将加入接入 PhysX 并重新设计物理相关的功能，除了重构现有 <code>Collider</code> 外，还将增加 <code>CapsuleCollider</code>，提供基于 PhysX 优化的<code>raycast</code> 方法，以及增加 <code>RigidBody</code> 组件等。</p> 
 <p><img height="242" src="https://static.oschina.net/uploads/space/2021/0910/153417_PaAk_2720166.gif" width="320" referrerpolicy="no-referrer"></p> 
 <p><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fmp.weixin.qq.com%2Fs%2F4ryPSE0zvDuFA6AeeT7dIA" target="_blank">详情查看发布公告</a>。</p> 
</div>
                                        </div>
                                      
</div>
            