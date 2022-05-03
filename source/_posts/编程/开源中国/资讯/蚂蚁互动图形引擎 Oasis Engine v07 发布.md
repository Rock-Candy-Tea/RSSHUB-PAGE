
---
title: '蚂蚁互动图形引擎 Oasis Engine v0.7 发布'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://oscimg.oschina.net/oscnet/up-33cd829587e17059deaf4f025579ee7cd03.png'
author: 开源中国
comments: false
date: Mon, 02 May 2022 23:56:00 GMT
thumbnail: 'https://oscimg.oschina.net/oscnet/up-33cd829587e17059deaf4f025579ee7cd03.png'
---

<div>   
<div class="content">
                                                                                            <p>蚂蚁图形引擎 Oasis Engine 0.7 版本已发布，Oasis Engine 是一个移动优先的高性能 Web 图形引擎，被广泛应用在支付宝五福、打年兽等各种互动业务中的图形引擎。</p> 
<p><span style="background-color:#ffffff; color:#000000">0.7 版本在图形方面新增了</span><strong style="color:#000000">文字渲染器</strong><span style="background-color:#ffffff; color:#000000">，完善了 2D 的基础能力，同时增强了<span> </span></span><strong style="color:#000000">PBR 材质渲染效果</strong><span style="background-color:#ffffff; color:#000000">，让真实感渲染效果更上一层楼。物理方面，深入结合 PhysX 的能力引入</span><strong style="color:#000000">动态碰撞器</strong><span style="background-color:#ffffff; color:#000000">组件，帮助开发者轻松利用几行代码实现物理类的互动。动画方面，升级了<span> </span></span><strong style="color:#000000">BlendShape 动画</strong><span style="background-color:#ffffff; color:#000000">和</span><strong style="color:#000000">动画倒播</strong><span style="background-color:#ffffff; color:#000000">能力。交互方面，针对 PC 端的互动，增加了</span><strong style="color:#000000">键盘交互</strong><span style="background-color:#ffffff; color:#000000">能力。</span></p> 
<hr> 
<h2 style="margin-left:0px; margin-right:0px; text-align:left">图形更新</h2> 
<h3 style="margin-left:0px; margin-right:0px; text-align:left">文字</h3> 
<p style="color:#000000; margin-left:0; margin-right:0; text-align:left">新增了文字渲染器，解决了文字绘制的问题，2D 基础能力方面得到进一步完善。之前开发者在项目中只能用 HTML+CSS 技术实现文字绘制，整个互动项目的开发流程比较割裂。此版本的文字系统支持基础的系统字体的渲染，包括大小、颜色、加粗、斜体等样式设置(下方左图)。另外，也支持多行显示，并支持各种对齐方式(下方右图)。</p> 
<p><img alt src="https://oscimg.oschina.net/oscnet/up-33cd829587e17059deaf4f025579ee7cd03.png" referrerpolicy="no-referrer"></p> 
<p><span style="background-color:#ffffff; color:#000000">文字系统也支持自定义 Shader，可以实现一些有意思的特效，比如官网示例中简单实现的 KTV 字幕效果：</span></p> 
<p><img alt src="https://oscimg.oschina.net/oscnet/up-a16751f186808b0b991721176c1c73d3e88.png" referrerpolicy="no-referrer"></p> 
<h3>材质</h3> 
<p style="color:#000000; margin-left:0; margin-right:0; text-align:left"><strong>新增 ClearCoat</strong></p> 
<p style="color:#000000; margin-left:0; margin-right:0; text-align:left">旧版的 PBR 材质设计是单一涂层模型，很难体现自然现实中的复杂材质表现，因此我们在材质的基础层上面增加了<strong>透明涂层</strong>（Clear Coat），用来模拟类似车子表面涂上一层透明涂层的渲染表现：</p> 
<p><img alt src="https://oscimg.oschina.net/oscnet/up-94c47cec4ea1570cc80f7ea88576dee2783.png" referrerpolicy="no-referrer"></p> 
<p>开启此功能非常便捷，只需要设置 PBR 材质的 clearCoat 属性为 0 ～ 1 的值即可：</p> 
<pre style="margin-left:0; margin-right:0; text-align:left"><code>material.clearCoat = <span style="color:#d19a66">1.0</span> ;
</code></pre> 
<p><span style="background-color:#ffffff; color:#000000">除了设置 clearCoat 作为透明涂层的强度之外，引擎还提供了透明涂层纹理、透明涂层粗糙度、透明涂层粗糙度纹理、透明涂层法线纹理，用来控制涂层的综合表现，具体效果可以参考官网示例。</span></p> 
<p><img alt src="https://oscimg.oschina.net/oscnet/up-f832886c5a8ab3a84295136146ae4296ff6.png" referrerpolicy="no-referrer"></p> 
<p><strong>新增高光抗锯齿</strong></p> 
<p style="color:#000000; margin-left:0; margin-right:0; text-align:left">旧版的材质在低粗糙度的时候，会有较强的镜面反射，且高光区域会很锐利，在一些模型边缘会表现的更加明，新版材质在 Shader 中内置了高光抗锯齿，改善了这一状况。</p> 
<p><img alt src="https://oscimg.oschina.net/oscnet/up-df0831f56beb4293812b6b69168d73f3114.png" referrerpolicy="no-referrer"></p> 
<p><strong>新增 AO 贴图 UV 通道切换</strong></p> 
<p style="color:#000000; margin-left:0; margin-right:0; text-align:left">旧版引擎不支持多 UV 通道管理，大部分 AO 贴图（occlusion Texture）在建模导出的时候采用了第二个 UV 通道，因此会导致渲染异常。新版引擎新增了 AO 贴图 UV 通道切换的功能，glTF 解析的时候会自动切换 UV 通道，也可以手动切换，但注意，引擎限制了 AO 通道只能采用 UV0 或者 UV1:</p> 
<pre><code> material.occlusionTextureCoord = TextureCoordinate.UV1;</code></pre> 
<p><img alt src="https://oscimg.oschina.net/oscnet/up-26fdb127b11a2575dd3e3d9413cc2edec0b.png" referrerpolicy="no-referrer"></p> 
<p><strong>HDR 文件加载器</strong></p> 
<p style="color:#000000; margin-left:0; margin-right:0; text-align:left">旧版引擎实现一个天空盒，必须使用立方体纹理加载器加载 6 张贴图，且结尾必须使用 px 、py、 pz 、nx 、ny 、nz。为了增加性能和易用性，新版引擎往资源加载器中增加了 HDR loader，用户可以直接加载各种分辨率的 HDR 贴图作为天空盒背景：</p> 
<pre><code>engine.resourceManager
  .load<TextureCube>(&#123;
    type: AssetType.HDR,
    url: "***.hdr"
  &#125;)
  .then((texture) => &#123;
    skyMaterial.textureCubeMap = texture;
    // HDR output is RGBM format.
    skyMaterial.textureDecodeRGBM = true;
  &#125;);</code></pre> 
<h3 style="color:#000000; margin-left:0px; margin-right:0px; text-align:left"><strong>纹理</strong></h3> 
<p style="color:#000000; margin-left:0; margin-right:0; text-align:left"><strong>新增 Texture2DArray</strong></p> 
<p style="color:#000000; margin-left:0; margin-right:0; text-align:left">新增了 Texture2DArray 纹理类, Texture2DArray 是数组的形式的 Texture2D，常作为数据纹理使用，并且不会占用多个 GPU 纹理单元，开发者可以使用该纹理作为多种用途使用。</p> 
<p style="color:#000000; margin-left:0; margin-right:0; text-align:left"><strong>优化 RenderTarget</strong></p> 
<p style="color:#000000; margin-left:0; margin-right:0; text-align:left">为了让 RenderTarget 从设计上更好的扩展任意纹理类型，精简了纹理结构，其中 RenderTarget 的 colorTexture 和 depthTexture 属性类型使用 Texture  替代旧版的 RenderColorTexture 和 RenderDepthTexture。</p> 
<h2 style="margin-left:0px; margin-right:0px; text-align:left">物理更新</h2> 
<p style="color:#000000; margin-left:0; margin-right:0; text-align:left"><strong>新增动态</strong><strong>物理碰撞器</strong></p> 
<p style="color:#000000; margin-left:0; margin-right:0; text-align:left">新版引擎正式加入了由 PhysX.js 提供后端支持的动态物理碰撞器组件，通过该组件用户可以很容易为应用添加物理反馈的效果，并且可以触发碰撞响应的事件。</p> 
<p style="color:#000000; margin-left:0; margin-right:0; text-align:left"><img src="https://static.oschina.net/uploads/space/2022/0503/075228_bdjF_2720166.gif" referrerpolicy="no-referrer"></p> 
<p><span style="background-color:#ffffff; color:#000000">由于碰撞器组件会按照物理规律驱动组件运动，因此单步模拟的时间步长就显得非常重要。新版引擎将物理场景更新的时间间隔改成</span><strong style="color:#000000">固定时间</strong><span style="background-color:#ffffff; color:#000000">，每一个主循环内，会有一次或者多次更新，并且物理场景和 Entity 的变换也会同步多次。对于物理相关的脚本逻辑，增加了 onPhysicsUpdate 脚本函数，该函数在每次物理场景更新前被调用，保证用户设置的物理更新逻辑可以被执行。因此在脚本生命周期中，单个循环中可能会多次触发相应的物理事件：</span></p> 
<p><img alt src="https://oscimg.oschina.net/oscnet/up-11997ec7849f35d65173fbf6fff84345024.png" referrerpolicy="no-referrer"></p> 
<p><strong>解耦初始化接口</strong></p> 
<p style="color:#000000; margin-left:0; margin-right:0; text-align:left">除了新功能，新版引擎优化了物理引擎的初始化方式，将物理引擎和 Engine 初始化解耦：</p> 
<pre><code>import &#123;WebGLEngine&#125; from "oasis-engine";
import &#123;PhysXPhysics&#125; from "@oasis-engine/physics-physx";

const engine = new WebGLEngine("canvas");

PhysXPhysics.initialize().then(() => &#123;
  engine.physicsManager.initialize(PhysXPhysics);
  engine.run();
&#125;);</code></pre> 
<h2 style="margin-left:0px; margin-right:0px; text-align:left">交互更新</h2> 
<p style="color:#000000; margin-left:0; margin-right:0; text-align:left"><strong>键盘交互</strong></p> 
<p style="color:#000000; margin-left:0; margin-right:0; text-align:left">新增键盘交互，开发者可以通过几个简单的接口实时获取键盘的交互情况，现在官网上的 Flappy Bird 可以用空格键玩啦！</p> 
<pre><code>class KeyScript extends Script &#123;
  onUpdate() &#123;
    const &#123; inputManager &#125; = this.engine;
    if (inputManager.isKeyHeldDown(Keys.Space)) &#123;
      // 现在还按着空格键
    &#125;
    if (inputManager.isKeyDown(Keys.Space)) &#123;
      // 这帧按下过空格键
    &#125;
    if (inputManager.isKeyUp(Keys.Space)) &#123;
      // 这帧抬起过空格键
    &#125;
  &#125;
&#125;</code></pre> 
<h2 style="margin-left:0px; margin-right:0px; text-align:left">动画更新</h2> 
<p style="margin-left:0px; margin-right:0px; text-align:left"><strong><span>B</span><span>lendShape 动画数量提升</span></strong></p> 
<p style="color:#000000; margin-left:0; margin-right:0; text-align:left">旧版本中 Mesh 存储的 BlendShape 动画数量上限最大为 4，新版引擎改进了内部实现，BlendShape 动画上限提升，通过浮点数纹理实现模式解除了数量上限的限制，几乎可以支持任意数量的 BlendShape 动画混合，下面案例为 8 个 BlendShape 的混合动画，旧版本只支持 4 根柱子有动画。</p> 
<p><img src="https://static.oschina.net/uploads/space/2022/0503/075414_lym3_2720166.gif" referrerpolicy="no-referrer"></p> 
<p><strong>动画倒播</strong></p> 
<p style="color:#000000; margin-left:0; margin-right:0; text-align:left">新增 Animator 倒播的能力,  <code>animator.speed</code><span> </span>为负值时，动画可以进行倒播，开发者可以编写个性化的播放逻辑：</p> 
<pre><code>animator.speed = -1;</code></pre> 
<p><img src="https://static.oschina.net/uploads/space/2022/0503/075432_NPeX_2720166.gif" referrerpolicy="no-referrer"></p> 
<h2 style="margin-left:0px; margin-right:0px; text-align:left">基础更新</h2> 
<p style="margin-left:0px; margin-right:0px; text-align:left"><strong>变换</strong></p> 
<p style="color:#000000; margin-left:0; margin-right:0; text-align:left">优化 Transform API 的使用方式，提升了高频 API 的使用体验，例如，过去我们想修改 position、rotation、scale 等属性的单轴分量值需要通过以下步骤完成，使用相对繁琐：</p> 
<pre><code>const transform = lightEntity.transform;
const position = transform.position;
position.y += 0.1;
transform.position = position;</code></pre> 
<p style="color:#000000; margin-left:0; margin-right:0; text-align:left">优化后开发者可以直接修改单轴分量即可，无需回设完整属性，使用方式更自然：</p> 
<pre style="margin-left:0; margin-right:0; text-align:left">const transform = lightEntity.transform;
transform.position.y += 0.1;</pre> 
<h2 style="margin-left:0px; margin-right:0px; text-align:left">文档更新</h2> 
<p style="color:#000000; margin-left:0; margin-right:0; text-align:left">文档目录结构做了较大更新，将内容以功能模块进行划分，让开发者能够更快地定位到所需功能：</p> 
<h2 style="margin-left:0px; margin-right:0px; text-align:left">示例更新</h2> 
<ul style="margin-left:0; margin-right:0"> 
 <li> <p>图形：text KTV effect、text renderer、text wrap alignment、pbr clear coat、HDR Loader</p> </li> 
 <li> <p>物理：physx attractor、physx compound、physx select</p> </li> 
</ul> 
<h2 style="margin-left:0px; margin-right:0px; text-align:left">0.7 里程碑信息</h2> 
<ul style="margin-left:0; margin-right:0"> 
 <li> <p>完整日志：https://github.com/oasis-engine/engine/releases/tag/v0.7.0-beta.2</p> </li> 
 <li> <p>迭代计划：https://github.com/oasis-engine/engine/issues/666</p> </li> 
</ul> 
<h2 style="margin-left:0px; margin-right:0px; text-align:left">0.8 里程碑预告</h2> 
<ul style="margin-left:0; margin-right:0"> 
 <li> <p>在下个里程碑当中，物理组件方面会引入角色控制器和物理约束，这些物理技术可以很容易与动画系统结合起来，可以增强开发者对于角色的控制能力。</p> </li> 
 <li> <p>文字渲染器将会持续优化内部实现，采用逐字符缓存的方式，减少文字内存占用。</p> </li> 
 <li> <p>特效相关功能的开发和规划。</p> </li> 
</ul> 
<p>来自 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fmp.weixin.qq.com%2Fs%2FeHc-Aiqxc4mGGRb7ht11Jw" target="_blank">Oasis 引擎爱好者</a></p>
                                        </div>
                                      
</div>
            