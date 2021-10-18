
---
title: '光影的魔法！Cocos Creator 实现屏幕空间的环境光遮蔽(SSAO)'
categories: 
 - 游戏
 - GameRes 游资网
 - 热点推荐
headimg: 'https://di.gameres.com/attachment/forum/202110/12/141111u67rw62ts89z77l8.jpg'
author: GameRes 游资网
comments: false
date: Tue, 12 Oct 2021 00:00:00 GMT
thumbnail: 'https://di.gameres.com/attachment/forum/202110/12/141111u67rw62ts89z77l8.jpg'
---

<div>   
<table cellspacing="0" cellpadding="0"><tbody><tr><td class="t_f" id="postmessage_2516490">
<strong>引言：</strong><br><br>
本文作者 alpha 从事游戏前端开发已经5年，毕业后他先是入职了腾讯无线大连研发中心，而后开启了北漂生涯，在北京的这3年一直都在使用 Cocos Creator，对前端业务，包体、内存优化有很多的实践经验。最近 alpha 在学习计算机图形学相关技术，今天他将同大家分享 Cocos Creator 3.3 实现屏幕空间的环境光遮蔽(SSAO)的技术经验。<br><br><strong><font color="#de5650">什么是 AO ?</font></strong><br><br>
环境光(Ambient Lighting)是场景总体光照中的一个固定光照常量，用来模拟光的散射(Scattering)。在现实中，光线会以任意方向散射，它的强度是会改变的。<br><br>
其中一种间接光照的模拟叫做环境光遮蔽(Ambient Occlusion)，它的原理是通过将褶皱、孔洞和非常靠近的墙面变暗的方法近似模拟出间接光照。这些区域很大程度上是被周围的几何体遮挡的，所以这些地方看起来会更暗一些。<br><br>
在2007年，Crytek 公司发布了一款叫做屏幕空间环境光遮蔽(Screen Space Ambient Occlusion，SSAO)的技术，并用在了他们的看家作孤岛危机上。这一技术使用了屏幕空间场景的深度而不是真实的几何体数据来确定遮蔽量。这一做法相对于真正的环境光遮蔽（基于光线追踪）不但速度快，而且还能获得较好的效果，使得它成为近似实时环境光遮蔽的标准。<br><br>
下面这幅图展示了在使用和不使用 SSAO 时场景的不同。特别注意对比电话亭后面和墙角部分，你会发现（环境）光被遮蔽了许多：<br><br><div align="center">
<img id="aimg_1014071" aid="1014071" zoomfile="https://di.gameres.com/attachment/forum/202110/12/141111u67rw62ts89z77l8.jpg" data-original="https://di.gameres.com/attachment/forum/202110/12/141111u67rw62ts89z77l8.jpg" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202110/12/141111u67rw62ts89z77l8.jpg" referrerpolicy="no-referrer">
</div>
<br>
虽然这个效果不是非常明显，但是启用 AO 确实给我们更真实的感觉，这些小的遮蔽细节能让整个场景看起来更有立体感。<br><br><strong><font color="#de5650">SSAO 原理</font></strong><br><br>
SSAO 背后的原理很简单：对于屏幕上的每一个片段，会根据周边深度值计算一个遮蔽因子(Occlusion Factor)。这个遮蔽因子之后会被用来决定片段的环境光分量。遮蔽因子是通过采集片段周围球型核心(Kernel)的多个深度样本，并和当前片段深度值对比而得到的。高于片段深度值样本的个数就是我们想要的遮蔽因子。<br><br><div align="center">
<img id="aimg_1014072" aid="1014072" zoomfile="https://di.gameres.com/attachment/forum/202110/12/141112dizyjjjbg6b7cflo.jpg" data-original="https://di.gameres.com/attachment/forum/202110/12/141112dizyjjjbg6b7cflo.jpg" width="400" inpost="1" src="https://di.gameres.com/attachment/forum/202110/12/141112dizyjjjbg6b7cflo.jpg" referrerpolicy="no-referrer">
</div>
<br>
上图中在几何体内灰色的深度样本都是高于片段深度值的，他们会增加遮蔽因子；几何体内样本个数越多，片段获得的环境光照也就越少。<br><br>
很明显，渲染效果的质量和精度与采样的样本数量有直接关系。如果样本数量太低，渲染的精度会急剧减少，会得到一种叫做波纹(Banding)的效果；如果它太高了，会影响性能。通过引入随机性到采样核心(Sample Kernel)从而减少样本的数目。通过随机旋转采样核心，能在有限样本数量中得到高质量的结果。然而随机性引入了一个很明显的噪声图案，需要通过模糊降噪来修复这一问题。下面这幅图片展示了波纹效果还有随机性造成的效果：<br><br><div align="center">
<img id="aimg_1014073" aid="1014073" zoomfile="https://di.gameres.com/attachment/forum/202110/12/141112b1k2ct2j8t8tjjt1.jpg" data-original="https://di.gameres.com/attachment/forum/202110/12/141112b1k2ct2j8t8tjjt1.jpg" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202110/12/141112b1k2ct2j8t8tjjt1.jpg" referrerpolicy="no-referrer">
</div>
<br>
可以看到，尽管在低样本数的情况下得到了很明显的波纹效果，引入随机性之后这些波纹效果就完全消失了。最初 Crytek 的实现是用一个深度缓冲做为输入，但是这种方式存在一些问题（如自遮闭, 光环），由于这个原因，现在通常不会使用球体的采样核心，而是使用一个沿着表面法向量的半球体采样核心。<br><br><div align="center">
<img id="aimg_1014074" aid="1014074" zoomfile="https://di.gameres.com/attachment/forum/202110/12/141113xb2gs2hzg2xalpsx.jpg" data-original="https://di.gameres.com/attachment/forum/202110/12/141113xb2gs2hzg2xalpsx.jpg" width="400" inpost="1" src="https://di.gameres.com/attachment/forum/202110/12/141113xb2gs2hzg2xalpsx.jpg" referrerpolicy="no-referrer">
</div>
<br>
通过在法向半球体(Normal Oriented Hemisphere)周围采样，将不会考虑到片段背面的几何体，它消除了环境光遮蔽灰蒙蒙的感觉，从而产生更真实的结果。<br><br><strong>SSAO 特点：</strong><br><br>
独立于场景复杂性，仅和投影后最终的像素有关，和场景中的顶点数三角数无关。<br><br>
跟传统的 AO 处理方法相比，不需要预处理，无需加载时间，也无需系统内存中的内存分配，所以更加适用于动态场景。<br><br>
对屏幕上的每个像素以相同的一致方式工作。<br><br>
没有 CPU 使用 - 它可以在 GPU 上完全执行。<br><br>
可以轻松集成到任何现代图形管线中。<br><br>
在了解了 AO & SSAO 之后，我们来看看要怎么<strong>基于 Cocos Creator 3.3.1 实现 SSAO。</strong><br><br>
Demo 地址：<br><br>
https://gitee.com/yanjifa/cc-ssao-demo<br><br><strong><font color="#de5650">样本缓冲</font></strong><br><br>
SSAO 需要几何体的信息来确定一个片段的遮蔽因子，对于每个片段（像素），需要如下数据：<br><br>
逐片段位置向量<br><br>
逐片段法线向量<br><br>
逐片段反射颜色<br><br><strong>采样核心</strong><br><br>
用来旋转采样核心的随机旋转向量<br><br>
通过使用一个逐片段观察空间位置，可以将一个采样半球核心对准片段的观察空间表面法线。对于每一个核心样本会采样线性深度纹理来比较结果。采样核心会根据旋转矢量稍微偏转一点；所获得的遮蔽因子将会之后用来限制最终的环境光照分量。<br><br><div align="center">
<img id="aimg_1014075" aid="1014075" zoomfile="https://di.gameres.com/attachment/forum/202110/12/141113ek10ykdbqmabmmme.jpg" data-original="https://di.gameres.com/attachment/forum/202110/12/141113ek10ykdbqmabmmme.jpg" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202110/12/141113ek10ykdbqmabmmme.jpg" referrerpolicy="no-referrer">
</div>
<br>
通过以上发现 SSAO 所需的数据不正是延迟管线的 G-buffer，关于 G-buffer 是什么可通过文章「延迟着色法」[1]做一个简单的了解。阅读引擎代码 editor/assets/chunks/standard-surface-entry-entry.chunk 和 cocos/core/pipeline/define.ts ：<br><br>
// editor/assets/chunks/standard-surface-entry-entry.chunk 33 行附近<br><br>
#elif CC_PIPELINE_TYPE == CC_PIPELINE_TYPE_DEFERRED<br><br>
layout(location = 0) out vec4 fragColor0;<br><br>
layout(location = 1) out vec4 fragColor1;<br><br>
layout(location = 2) out vec4 fragColor2;<br><br>
layout(location = 3) out vec4 fragColor3;<br><br>
void main () &#123;<br><br>
StandardSurface s; surf(s);<br><br>
fragColor0 = s.albedo;                         // 漫反射颜色 -> 反照率纹理<br><br>
fragColor1 = vec4(s.position, s.roughness);    // 位置 -> 世界空间位置<br><br>
fragColor2 = vec4(s.normal, s.metallic);       // 法线 -> 世界空间法线<br><br>
fragColor3 = vec4(s.emissive, s.occlusion);    // 和本文无关, 不做介绍<br><br>
&#125;<br><br>
#endif<br><br><br>
// cocos/core/pipeline/define.ts  117 行 附近<br><br>
export enum PipelineGlobalBindings &#123;<br><br>
UBO_GLOBAL,<br><br>
UBO_CAMERA,<br><br>
UBO_SHADOW,<br><br>
SAMPLER_SHADOWMAP,<br><br>
SAMPLER_ENVIRONMENT,<br><br>
SAMPLER_SPOT_LIGHTING_MAP,<br><br>
SAMPLER_GBUFFER_ALBEDOMAP,   // 6<br><br>
SAMPLER_GBUFFER_POSITIONMAP, // 7<br><br>
SAMPLER_GBUFFER_NORMALMAP,   // 8<br><br>
SAMPLER_GBUFFER_EMISSIVEMAP,<br><br>
SAMPLER_LIGHTING_RESULTMAP,<br><br>
COUNT,<br><br>
&#125;<br><br>
// cocos/core/pipeline/define.ts  283 行 附近<br><br>
const UNIFORM_GBUFFER_ALBEDOMAP_NAME = 'cc_gbuffer_albedoMap';<br><br>
export const UNIFORM_GBUFFER_ALBEDOMAP_BINDING = PipelineGlobalBindings.SAMPLER_GBUFFER_ALBEDOMAP; // 6<br><br>
// ...<br><br>
const UNIFORM_GBUFFER_POSITIONMAP_NAME = 'cc_gbuffer_positionMap';<br><br>
export const UNIFORM_GBUFFER_POSITIONMAP_BINDING = PipelineGlobalBindings.SAMPLER_GBUFFER_POSITIONMAP; // 7<br><br>
// ...<br><br>
const UNIFORM_GBUFFER_NORMALMAP_NAME = 'cc_gbuffer_normalMap';<br><br>
export const UNIFORM_GBUFFER_NORMALMAP_BINDING = PipelineGlobalBindings.SAMPLER_GBUFFER_NORMALMAP; // 8<br><br>
// ...<br><br>
通过以上代码可以分析出引擎 G-buffer 的数据布局，和具体 G-buffer 数据内容，深度值后面将会使用 G-buffer 计算得出。<br><strong><font color="#de5650"><br></font></strong><br><strong><font color="#de5650">自定义渲染管线</font></strong><br><br>
通过扩展延迟渲染管线的方式，在内置渲染管线的 LightFlow 上增加 一个 SsaoStage 用来生成 AO 纹理。首先创建一个渲染管线资源，资源管理器右键->创建->Render Pipeine->Render Pipeline Asset，命名为 ssao-deferrd-pipeline，创建 ssao-material | ssao-effect 着色器用来计算 AO 纹理，完整文件如下：<br><br>
.<br><br>
├── ssao-constant.chunk            // UBO 描述<br><br>
├── ssao-deferred-pipeline.rpp     // 管线资源文件<br><br>
├── ssao-effect.effect             // ssao shader<br><br>
├── ssao-lighting.effect           // 光照 shader, 直接拷贝内置 internal/effects/pipeline/defferrd-lighting<br><br>
├── ssao-lighting.mtl<br><br>
├── ssao-material.mtl<br><br>
├── ssao-render-pipeline.ts        // 定制管线脚本<br><br>
├── ssao-stage.ts                  // stage 脚本<br><br>
└── uboDefine.ts                   // Uniform Buffer Object 定义脚本<br><br>
对应管线配置如下，在 LightingFlow 下 Stages 最前面加入 SsaoStage，并指定对应的材质，可以看到，引擎现在其实已经支持后处理(PostProcess)了，只要指定材质就可以了，可能当前版本还不完善，所以引擎组还没公开，其实 SSAO 也可以算是一种后处理效果，管线资源的属性设置如下：<br><br><div align="center">
<img id="aimg_1014076" aid="1014076" zoomfile="https://di.gameres.com/attachment/forum/202110/12/141114ytombz6obroim9ml.jpg" data-original="https://di.gameres.com/attachment/forum/202110/12/141114ytombz6obroim9ml.jpg" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202110/12/141114ytombz6obroim9ml.jpg" referrerpolicy="no-referrer">
</div>
<br>
自定义管线脚本如下：<br><br>
// uboDefine.ts<br><br>
import &#123; gfx, pipeline &#125; from "cc";<br><br>
const &#123; DescriptorSetLayoutBinding, UniformSamplerTexture, DescriptorType, ShaderStageFlagBit, Type &#125; = gfx;<br><br>
const &#123; SetIndex, PipelineGlobalBindings, globalDescriptorSetLayout &#125; = pipeline;<br><br>
let GlobalBindingStart = PipelineGlobalBindings.COUNT; // 11<br><br>
let GlobalBindingIndex = 0;<br><br>
/**<br><br>
* 定义 SSAO Frame Buffer, 布局描述<br><br>
*/<br><br>
const UNIFORM_SSAOMAP_NAME = 'cc_ssaoMap';<br><br>
export const UNIFORM_SSAOMAP_BINDING = GlobalBindingStart + GlobalBindingIndex++; // 11<br><br>
const UNIFORM_SSAOMAP_DESCRIPTOR = new DescriptorSetLayoutBinding(UNIFORM_SSAOMAP_BINDING, DescriptorType.SAMPLER_TEXTURE, 1, ShaderStageFlagBit.FRAGMENT);<br><br>
const UNIFORM_SSAOMAP_LAYOUT = new UniformSamplerTexture(SetIndex.GLOBAL, UNIFORM_SSAOMAP_BINDING, UNIFORM_SSAOMAP_NAME, Type.SAMPLER2D, 1);<br><br>
globalDescriptorSetLayout.layouts[UNIFORM_SSAOMAP_NAME] = UNIFORM_SSAOMAP_LAYOUT;<br><br>
globalDescriptorSetLayout.bindings[UNIFORM_SSAOMAP_BINDING] = UNIFORM_SSAOMAP_DESCRIPTOR;<br><br>
/**<br><br>
* 采样核心、相机远近裁剪面 near & far 等 UniformBlock 布局描述<br><br>
*/<br><br>
export class UBOSsao &#123;<br><br>
public static readonly SAMPLES_SIZE = 64; // 最大采样核心<br><br>
public static readonly CAMERA_NEAR_FAR_LINEAR_INFO_OFFSET = 0;<br><br>
public static readonly SSAO_SAMPLES_OFFSET = UBOSsao.CAMERA_NEAR_FAR_LINEAR_INFO_OFFSET + 4;<br><br>
public static readonly COUNT = (UBOSsao.SAMPLES_SIZE + 1) * 4;<br><br>
public static readonly SIZE = UBOSsao.COUNT * 4;<br><br>
public static readonly NAME = 'CCSsao';<br><br>
public static readonly BINDING = GlobalBindingStart + GlobalBindingIndex++; // 12<br><br>
public static readonly DESCRIPTOR = new gfx.DescriptorSetLayoutBinding(UBOSsao.BINDING, gfx.DescriptorType.UNIFORM_BUFFER, 1, gfx.ShaderStageFlagBit.ALL);<br><br>
public static readonly LAYOUT = new gfx.UniformBlock(SetIndex.GLOBAL, UBOSsao.BINDING, UBOSsao.NAME, [<br><br>
new gfx.Uniform('cc_cameraNFLSInfo', gfx.Type.FLOAT4, 1), // vec4<br><br>
new gfx.Uniform('ssao_samples', gfx.Type.FLOAT4, UBOSsao.SAMPLES_SIZE), // vec4[64]<br><br>
], 1);<br><br>
&#125;<br><br>
globalDescriptorSetLayout.layouts[UBOSsao.NAME] = UBOSsao.LAYOUT;<br><br>
globalDescriptorSetLayout.bindings[UBOSsao.BINDING] = UBOSsao.DESCRIPTOR;<br><br>
/**<br><br>
*  ssao-render-pipeline.ts<br><br>
*  扩展延迟渲染管线<br><br>
*/<br><br>
import &#123; _decorator, DeferredPipeline, gfx, renderer &#125; from "cc";<br><br>
import &#123; UNIFORM_SSAOMAP_BINDING &#125; from "./uboDefine";<br><br>
const &#123; ccclass &#125; = _decorator;<br><br>
const _samplerInfo = [<br><br>
gfx.Filter.POINT,<br><br>
gfx.Filter.POINT,<br><br>
gfx.Filter.NONE,<br><br>
gfx.Address.CLAMP,<br><br>
gfx.Address.CLAMP,<br><br>
gfx.Address.CLAMP,<br><br>
];<br><br>
const samplerHash = renderer.genSamplerHash(_samplerInfo);<br><br>
export class SsaoRenderData &#123;<br><br>
frameBuffer?: gfx.Framebuffer | null;<br><br>
renderTargets?: gfx.Texture[] | null;<br><br>
depthTex?: gfx.Texture | null;<br><br>
&#125;<br><br>
@ccclass("SsaoRenderPipeline")<br><br>
export class SsaoRenderPipeline extends DeferredPipeline &#123;<br><br>
private _width = 0;<br><br>
private _height = 0;<br><br>
private _ssaoRenderData: SsaoRenderData | null = null!;<br><br>
private _ssaoRenderPass: gfx.RenderPass | null = null;<br><br>
public activate(): boolean &#123;<br><br>
const result = super.activate();<br><br>
this._width = this.device.width;<br><br>
this._height = this.device.height;<br><br>
this._generateSsaoRenderData();<br><br>
return result;<br><br>
&#125;<br><br>
public resize(width: number, height: number) &#123;<br><br>
if (this._width === width && this._height === height) &#123;<br><br>
return;<br><br>
&#125;<br><br>
super.resize(width, height);<br><br>
this._width = width;<br><br>
this._height = height;<br><br>
this._destroyRenderData();<br><br>
this._generateSsaoRenderData();<br><br>
&#125;<br><br>
public getSsaoRenderData(camera: renderer.scene.Camera): SsaoRenderData &#123;<br><br>
if (!this._ssaoRenderData) &#123;<br><br>
this._generateSsaoRenderData();<br><br>
&#125;<br><br>
return this._ssaoRenderData!;<br><br>
&#125;<br><br>
/**<br><br>
* 核心代码, 创建一个 FrameBuffer 存储 SSAO 纹理<br><br>
*/<br><br>
private _generateSsaoRenderData() &#123;<br><br>
if (!this._ssaoRenderPass) &#123;<br><br>
const colorAttachment = new gfx.ColorAttachment();<br><br>
colorAttachment.format = gfx.Format.RGBA8;<br><br>
colorAttachment.loadOp = gfx.LoadOp.CLEAR;<br><br>
colorAttachment.storeOp = gfx.StoreOp.STORE;<br><br>
colorAttachment.endAccesses = [gfx.AccessType.COLOR_ATTACHMENT_WRITE];<br><br>
const depthStencilAttachment = new gfx.DepthStencilAttachment();<br><br>
depthStencilAttachment.format = this.device.depthStencilFormat;<br><br>
depthStencilAttachment.depthLoadOp = gfx.LoadOp.CLEAR;<br><br>
depthStencilAttachment.depthStoreOp = gfx.StoreOp.STORE;<br><br>
depthStencilAttachment.stencilLoadOp = gfx.LoadOp.CLEAR;<br><br>
depthStencilAttachment.stencilStoreOp = gfx.StoreOp.STORE;<br><br>
const renderPassInfo = new gfx.RenderPassInfo([colorAttachment], depthStencilAttachment);<br><br>
this._ssaoRenderPass = this.device.createRenderPass(renderPassInfo);<br><br>
&#125;<br><br>
this._ssaoRenderData = new SsaoRenderData();<br><br>
this._ssaoRenderData.renderTargets = [];<br><br>
// 因为 SSAO 纹理最终是一张灰度图, 所以使用 Format.R8 单通道纹理, 减少内存占用, 使用时只需要读取 R 通道即可<br><br>
this._ssaoRenderData.renderTargets.push(this.device.createTexture(new gfx.TextureInfo(<br><br>
gfx.TextureType.TEX2D,<br><br>
gfx.TextureUsageBit.COLOR_ATTACHMENT | gfx.TextureUsageBit.SAMPLED,<br><br>
gfx.Format.R8,<br><br>
this._width,<br><br>
this._height,<br><br>
)));<br><br>
this._ssaoRenderData.depthTex = this.device.createTexture(new gfx.TextureInfo(<br><br>
gfx.TextureType.TEX2D,<br><br>
gfx.TextureUsageBit.DEPTH_STENCIL_ATTACHMENT,<br><br>
this.device.depthStencilFormat,<br><br>
this._width,<br><br>
this._height,<br><br>
));<br><br>
this._ssaoRenderData.frameBuffer = this.device.createFramebuffer(new gfx.FramebufferInfo(<br><br>
this._ssaoRenderPass!,<br><br>
this._ssaoRenderData.renderTargets,<br><br>
this._ssaoRenderData.depthTex,<br><br>
));<br><br>
this.descriptorSet.bindTexture(UNIFORM_SSAOMAP_BINDING, this._ssaoRenderData.frameBuffer.colorTextures[0]!);<br><br>
const sampler = renderer.samplerLib.getSampler(this.device, samplerHash);<br><br>
this.descriptorSet.bindSampler(UNIFORM_SSAOMAP_BINDING, sampler);<br><br>
&#125;<br><br>
public destroy(): boolean &#123;<br><br>
this._destroyRenderData();<br><br>
return super.destroy();<br><br>
&#125;<br><br>
private _destroyRenderData() &#123;<br><br>
if (!this._ssaoRenderData) &#123;<br><br>
return;<br><br>
&#125;<br><br>
if (this._ssaoRenderData.depthTex) &#123;<br><br>
this._ssaoRenderData.depthTex.destroy();<br><br>
&#125;<br><br>
if (this._ssaoRenderData.renderTargets) &#123;<br><br>
this._ssaoRenderData.renderTargets.forEach((o) => &#123;<br><br>
o.destroy();<br><br>
&#125;)<br><br>
&#125;<br><br>
if (this._ssaoRenderData.frameBuffer) &#123;<br><br>
this._ssaoRenderData.frameBuffer.destroy();<br><br>
&#125;<br><br>
this._ssaoRenderData = null;<br><br>
&#125;<br><br>
&#125;<br><br>
通过项目设置修改渲染管线为自定义的 SSAO 管线：<br><br><div align="center">
<img id="aimg_1014077" aid="1014077" zoomfile="https://di.gameres.com/attachment/forum/202110/12/141115kz96684qv68z04vy.jpg" data-original="https://di.gameres.com/attachment/forum/202110/12/141115kz96684qv68z04vy.jpg" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202110/12/141115kz96684qv68z04vy.jpg" referrerpolicy="no-referrer">
</div>
<br><strong><font color="#de5650">采样核心</font></strong><br><br>
我们需要沿着表面法线方向生成大量的样本。就像前面介绍的那样，想要生成形成半球形的样本。由于对每个表面法线方向生成采样核心非常困难，也不合实际，所以将在切线空间(Tangent Space)内生成采样核心，法向量将指向正 z 方向。<br><br><div align="center">
<img id="aimg_1014078" aid="1014078" zoomfile="https://di.gameres.com/attachment/forum/202110/12/141115mcnf7883nu7i3msc.jpg" data-original="https://di.gameres.com/attachment/forum/202110/12/141115mcnf7883nu7i3msc.jpg" width="400" inpost="1" src="https://di.gameres.com/attachment/forum/202110/12/141115mcnf7883nu7i3msc.jpg" referrerpolicy="no-referrer">
</div>假设有一个单位半球，生成一个拥有最大64样本值的采样核心：<br><br>
// ssao-stage.ts<br><br>
activate(pipeline: DeferredPipeline, flow: RenderFlow) &#123;<br><br>
super.activate(pipeline, flow);<br><br>
const device = pipeline.device;<br><br>
this._sampleBuffer = device.createBuffer(new gfx.BufferInfo(<br><br>
gfx.BufferUsageBit.UNIFORM | gfx.BufferUsageBit.TRANSFER_DST,<br><br>
gfx.MemoryUsageBit.HOST | gfx.MemoryUsageBit.DEVICE,<br><br>
UBOSsao.SIZE,<br><br>
UBOSsao.SIZE,<br><br>
));<br><br>
this._sampleBufferData = new Float32Array(UBOSsao.COUNT);<br><br>
const sampleOffset = UBOSsao.SSAO_SAMPLES_OFFSET / 4;<br><br>
// 64 样本值采样核心, 这里写的不太详细, 可结合 LearnOpenGL CN 的教程, 加深理解<br><br>
for (let i = 0; i < UBOSsao.SAMPLES_SIZE; i++) &#123;<br><br>
let sample = new Vec3(<br><br>
Math.random() * 2.0 - 1.0,<br><br>
Math.random() * 2.0 - 1.0,<br><br>
Math.random() + 0.01, // 这里和原教程有点区别, Z 稍微增加一个很小的值, 可改善平面波纹(Banding)的效果, 可能会对精度造成影响<br><br>
);<br><br>
sample = sample.normalize();<br><br>
let scale = i / UBOSsao.SAMPLES_SIZE;<br><br>
// 通过插值, 将核心样本靠近原点分布<br><br>
scale = lerp(0.1, 1.0, scale * scale);<br><br>
sample.multiplyScalar(scale);<br><br>
const index = 4 * (i + sampleOffset);<br><br>
this._sampleBufferData[index + 0] = sample.x;<br><br>
this._sampleBufferData[index + 1] = sample.y;<br><br>
this._sampleBufferData[index + 2] = sample.z;<br><br>
&#125;<br><br>
this._pipeline.descriptorSet.bindBuffer(UBOSsao.BINDING, this._sampleBuffer);<br><br>
&#125;<br><br>
我们在切线空间中以-1.0到1.0为范围变换 x 和 y 方向，并以 0.0 和 1.0 为范围变换样本的 z 方向 (如果以-1.0到1.0为范围，取样核心就变成球型了)。由于采样核心将会沿着表面法线对齐，所得的样本矢量将会在半球里。通过权重插值，得到一个大部分样本靠近原点的核心分布。<br><br><div align="center">
<img id="aimg_1014079" aid="1014079" zoomfile="https://di.gameres.com/attachment/forum/202110/12/141116p404mrb9hchor4bo.jpg" data-original="https://di.gameres.com/attachment/forum/202110/12/141116p404mrb9hchor4bo.jpg" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202110/12/141116p404mrb9hchor4bo.jpg" referrerpolicy="no-referrer">
</div>
<br><strong><font color="#de5650">获取深度数据</font></strong><br><br>
通过 G-buffer 中的 PostionMap 获取线性深度值：<br><br>
float getDepth(vec3 worldPos) &#123;<br><br>
// 转到观察空间<br><br>
vec3 viewPos = (cc_matView * vec4(worldPos.xyz, 1.0)).xyz;<br><br>
// cc_cameraNFLSInfo.y -> 相机 Far, 通过 ssao-stage.ts 脚本更新<br><br>
float depth = -viewPos.z / cc_cameraNFLSInfo.y;<br><br>
return depth;<br><br>
&#125;<br><br>
深度图如下：<br><br><div align="center">
<img id="aimg_1014080" aid="1014080" zoomfile="https://di.gameres.com/attachment/forum/202110/12/141116axgnldggkd8lz1pg.jpg" data-original="https://di.gameres.com/attachment/forum/202110/12/141116axgnldggkd8lz1pg.jpg" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202110/12/141116axgnldggkd8lz1pg.jpg" referrerpolicy="no-referrer">
</div>
<br><strong><font color="#de5650">SSAO 着色器</font></strong><br><br>
/**<br><br>
* ssao-effect.effect<br><br>
*/<br><br>
CCProgram ssao-fs %&#123;<br><br>
precision highp float;<br><br>
#include <cc-global><br><br>
#include <cc-shadow-map-base><br><br>
#include <ssao-constant><br><br>
// 最大 64<br><br>
#define SSAO_SAMPLES_SIZE 64<br><br>
in vec2 v_uv;<br><br>
#pragma builtin(global)<br><br>
layout (set = 0, binding = 7) uniform sampler2D cc_gbuffer_positionMap;<br><br>
#pragma builtin(global)<br><br>
layout (set = 0, binding = 8) uniform sampler2D cc_gbuffer_normalMap;<br><br>
layout(location = 0) out vec4 fragColor;<br><br>
// 随机数 0.0 - 1.0<br><br>
float rand(vec2 uv, float dx, float dy)<br><br>
&#123;<br><br>
uv += vec2(dx, dy);<br><br>
return fract(sin(dot(uv,  vec2(12.9898, 78.233))) * 43758.5453);<br><br>
&#125;<br><br>
// 随机旋转采样核心向量<br><br>
vec3 getRandomVec(vec2 uv)&#123;<br><br>
return vec3(<br><br>
rand(uv, 0.0, 1.0) * 2.0 - 1.0,<br><br>
rand(uv, 1.0, 0.0) * 2.0 - 1.0,<br><br>
0.0<br><br>
);<br><br>
&#125;<br><br>
// 获取线性深度<br><br>
float getDepth(vec3 worldPos) &#123;<br><br>
vec3 viewPos = (cc_matView * vec4(worldPos.xyz, 1.0)).xyz;<br><br>
float depth = -viewPos.z / cc_cameraNFLSInfo.y;<br><br>
return depth;<br><br>
&#125;<br><br>
// 深度图<br><br>
// void main () &#123;<br><br>
//   vec3 worldPos = texture(cc_gbuffer_positionMap, v_uv).xyz;<br><br>
//   fragColor = vec4(getDepth(worldPos));<br><br>
// &#125;<br><br>
void main () &#123;<br><br>
vec3 worldPos = texture(cc_gbuffer_positionMap, v_uv).xyz;<br><br>
vec3 normal = texture(cc_gbuffer_normalMap, v_uv).xyz;<br><br>
vec3 randomVec = getRandomVec(v_uv);<br><br>
float fragDepth = -getDepth(worldPos);<br><br>
// 创建一个TBN矩阵，将向量从切线空间变换到观察空间<br><br>
vec3 tangent = normalize(randomVec - normal * dot(randomVec, normal));<br><br>
vec3 bitangent = cross(normal, tangent);<br><br>
mat3 TBN = mat3(tangent, bitangent, normal);<br><br>
// 取样半径<br><br>
float radius = 1.0;<br><br>
float occlusion = 0.0;<br><br>
for(int i = 0; i < SSAO_SAMPLES_SIZE; ++i)<br><br>
&#123;<br><br>
vec3 ssaoSample = TBN * ssao_samples<i>.xyz;<br><br>
ssaoSample = worldPos + ssaoSample * radius;<br><br>
float aoDepth = -getDepth(ssaoSample);<br><br>
vec4 offset = vec4(ssaoSample, 1.0);<br><br>
offset      = (cc_matProj * cc_matView) * offset;   // 转换到裁剪空间<br><br>
offset.xyz /= offset.w;                             // 透视除法<br><br>
offset.xyz  = offset.xyz * 0.5 + 0.5;               // 从 NDC (标准化设备坐标, -1.0 - 1.0) 变换到 0.0 - 1.0<br><br>
vec3 samplePos = texture(cc_gbuffer_positionMap, offset.xy).xyz;<br><br>
float sampleDepth = -getDepth(samplePos);<br><br>
// 范围检查<br><br>
float rangeCheck = smoothstep(0.0, 1.0, radius / abs(fragDepth - sampleDepth));<br><br>
// 检查样本的当前深度值是否大于存储的深度值，如果是，添加到最终的贡献因子上<br><br>
occlusion += (sampleDepth >= aoDepth ? 1.0 : 0.0) * rangeCheck;<br><br>
&#125;<br><br>
// 将遮蔽贡献根据核心的大小标准化，并输出结果<br><br>
occlusion = 1.0 - (occlusion / float(SSAO_SAMPLES_SIZE));<br><br>
fragColor = vec4(occlusion, 1.0, 1.0, 1.0);<br><br>
&#125;<br><br>
&#125;%<br><br>
下图展示了环境遮蔽着色器产生的纹理：<br><br><div align="center">
<img id="aimg_1014081" aid="1014081" zoomfile="https://di.gameres.com/attachment/forum/202110/12/141116pwh70op49t99uo4q.jpg" data-original="https://di.gameres.com/attachment/forum/202110/12/141116pwh70op49t99uo4q.jpg" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202110/12/141116pwh70op49t99uo4q.jpg" referrerpolicy="no-referrer">
</div>
<br>
可见，环境遮蔽产生了非常强烈的深度感。仅仅通过环境遮蔽纹理就已经能清晰地看见模型一定躺在地板上而不是浮在空中。<br><br>
现在的效果仍然看起来不是很完美，不连续的噪点清晰可见，为了创建一个光滑的环境遮蔽结果，需要模糊环境遮蔽纹理进行降噪。<br><br><div align="center">
<img id="aimg_1014082" aid="1014082" zoomfile="https://di.gameres.com/attachment/forum/202110/12/141117v1yk6j4pqvskyzqp.jpg" data-original="https://di.gameres.com/attachment/forum/202110/12/141117v1yk6j4pqvskyzqp.jpg" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202110/12/141117v1yk6j4pqvskyzqp.jpg" referrerpolicy="no-referrer">
</div>
<br><strong><font color="#de5650">应用 SSAO 纹理</font></strong><br><br>
最后将 SSAO 纹理进行模糊降噪，并逐片段将环境遮蔽因子乘到环境光照分量上，拷贝内置光照着色器(internal/effects/pipeline/deferred-lighting.effect)命名为 ssao-lighting.effect。<br><br>
/**<br><br>
* 本文改动部分添加了中文注释<br><br>
*/<br><br>
CCProgram lighting-fs %&#123;<br><br>
precision highp float;<br><br>
#include <cc-global><br><br>
#include <shading-standard-base><br><br>
#include <shading-standard-additive><br><br>
#include <output-standard><br><br>
#include <cc-fog-base><br><br>
in vec2 v_uv;<br><br>
#pragma builtin(global)<br><br>
layout (set = 0, binding = 6) uniform sampler2D cc_gbuffer_albedoMap;<br><br>
#pragma builtin(global)<br><br>
layout (set = 0, binding = 7) uniform sampler2D cc_gbuffer_positionMap;<br><br>
#pragma builtin(global)<br><br>
layout (set = 0, binding = 8) uniform sampler2D cc_gbuffer_normalMap;<br><br>
#pragma builtin(global)<br><br>
layout (set = 0, binding = 9) uniform sampler2D cc_gbuffer_emissiveMap;<br><br>
#pragma builtin(global)<br><br>
layout (set = 0, binding = 11) uniform sampler2D cc_ssaoMap;<br><br>
layout(location = 0) out vec4 fragColor;<br><br>
vec4 gaussianBlur(sampler2D Tex, vec2 UV, float Intensity)<br><br>
&#123;<br><br>
// 省略, 详见 demo 工程<br><br>
return texture(Tex, UV);<br><br>
&#125;<br><br>
// 屏幕展示 SSAO 纹理<br><br>
// void main() &#123;<br><br>
//   // 降噪<br><br>
//   vec4 color = gaussianBlur(cc_ssaoMap, v_uv, 3.0);<br><br>
//   // 不降噪<br><br>
//   vec4 color = texture(cc_ssaoMap, v_uv);<br><br>
//   fragColor = vec4(vec3(color.r), 1.0);<br><br>
// &#125;<br><br>
void main () &#123;<br><br>
StandardSurface s;<br><br>
vec4 albedoMap = texture(cc_gbuffer_albedoMap,v_uv);<br><br>
vec4 positionMap = texture(cc_gbuffer_positionMap,v_uv);<br><br>
vec4 normalMap = texture(cc_gbuffer_normalMap,v_uv);<br><br>
vec4 emissiveMap = texture(cc_gbuffer_emissiveMap,v_uv);<br><br>
// ssao 环境遮蔽因子, 单通道纹理, 所以只取 R 通道<br><br>
vec4 ssaoMap = vec4(vec3(gaussianBlur(cc_ssaoMap, v_uv, 3.0).r), 1.0);<br><br>
s.albedo = albedoMap * ssaoMap; // 乘到辐照率贴图上, 应用遮蔽纹理<br><br>
s.position = positionMap.xyz;<br><br>
s.roughness = positionMap.w;<br><br>
s.normal = normalMap.xyz;<br><br>
s.metallic = normalMap.w;<br><br>
s.emissive = emissiveMap.xyz;<br><br>
s.occlusion = emissiveMap.w;<br><br>
// fixme: default value is 0, and give black result<br><br>
float fogFactor;<br><br>
CC_TRANSFER_FOG_BASE(vec4(s.position, 1), fogFactor);<br><br>
vec4 shadowPos;<br><br>
CC_TRANSFER_SHADOW_BASE(vec4(s.position, 1), shadowPos);<br><br>
vec4 color = CCStandardShadingBase(s, shadowPos) +<br><br>
CCStandardShadingAdditive(s, shadowPos);<br><br>
CC_APPLY_FOG_BASE(color, fogFactor);<br><br>
fragColor = CCFragOutput(color);<br><br>
&#125;<br><br>
&#125;%<br><br>
最后来看下最终的渲染结果对比，首先是 SSAO 开启的效果：<br><br><div align="center">
<img id="aimg_1014083" aid="1014083" zoomfile="https://di.gameres.com/attachment/forum/202110/12/141117lgl9lllha4n89sft.jpg" data-original="https://di.gameres.com/attachment/forum/202110/12/141117lgl9lllha4n89sft.jpg" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202110/12/141117lgl9lllha4n89sft.jpg" referrerpolicy="no-referrer">
</div>
<br>
SSAO 关闭的效果：<br><br><div align="center">
<img id="aimg_1014084" aid="1014084" zoomfile="https://di.gameres.com/attachment/forum/202110/12/141118wqbjnc8i8rcs859q.jpg" data-original="https://di.gameres.com/attachment/forum/202110/12/141118wqbjnc8i8rcs859q.jpg" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202110/12/141118wqbjnc8i8rcs859q.jpg" referrerpolicy="no-referrer">
</div>
<br>
屏幕空间环境遮蔽是一个可高度自定义的效果，它的效果很大程度上依赖于我们根据场景类型调整它的参数。对所有类型的场景并不存在什么完美的参数组合方式。一些场景只在小半径情况下工作，又有些场景会需要更大的半径和更大的样本数量才能看起来更真实。当前这个演示用了64个样本，属于比较多的了，你可以调整核心大小和半径从而获得合适的效果。<br><br><strong><font color="#de5650">已知问题</font></strong><br><br>
编辑器摄像机预览会渲染不正确。<br><br>
资源管理器里面点击自定义管线资源文件，编辑器控制台会报错，可能会导致编辑器无响应 (目前建议没事别碰，碰过重启编辑器可恢复正常)。<br><br>
手机浏览器 (小米10 Pro) 下使用最大采样核心 (64) 时，帧数只有个位数，可以确定当前版本基本不能应用到实际项目中，还需优化。<br><br>
Native 下自定义渲染管线同时还需要自定义 Engine-Native[2] 引擎，所以 Native 暂时还未支持，可参考 PR 3934[3] 添加对 Native 的支持，这里要感谢 大表姐Kristine 提供的信息。<br><br><strong><font color="#de5650">相关教程</font></strong><br><br>
LearnOpenGL-CN->目录->高级光照->SSAO：<br><br>
https://learnopengl-cn.github.io/05%20Advanced%20Lighting/09%20SSAO/<br><br>
环境遮罩之 SSAO 原理：<br><br>
https://zhuanlan.zhihu.com/p/46633896<br><br>
GAMES202-高质量实时渲染（视频00:46:25开始）：<br><br>
https://www.bilibili.com/video/BV1YK4y1T7yY?p=8<br><br><strong><font color="#de5650">参考链接</font></strong><br><br>
延迟着色法[1]：<br><br>
https://learnopengl-cn.github.io/05%20Advanced%20Lighting/08%20Deferred%20Shading/<br><br>
Engine-Native[2]：<br><br>
https://github.com/cocos-creator/engine-native/tree/develop/cocos/renderer/pipeline<br><br>
PR 3934[3]：<br><br>
https://github.com/cocos-creator/engine-native/pull/3934<br><br><font size="2"></font><br><font size="2">来源：COCOS</font><br><font size="2">原文：https://mp.weixin.qq.com/s/0aNtXI7s41meJhI5M4JItQ</font><br><br><br></i>
</td></tr></tbody></table>


  
</div>
            