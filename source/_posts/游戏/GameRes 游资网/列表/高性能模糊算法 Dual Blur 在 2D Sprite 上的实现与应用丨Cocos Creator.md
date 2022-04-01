
---
title: '高性能模糊算法 Dual Blur 在 2D Sprite 上的实现与应用丨Cocos Creator'
categories: 
 - 游戏
 - GameRes 游资网
 - 列表
headimg: 'https://di.gameres.com/attachment/forum/202203/16/112205j3fapwigwfy8w3z4.jpg'
author: GameRes 游资网
comments: false
date: Wed, 16 Mar 2022 00:00:00 GMT
thumbnail: 'https://di.gameres.com/attachment/forum/202203/16/112205j3fapwigwfy8w3z4.jpg'
---

<div>   
<div class="quote"><blockquote>引言：在游戏开发中，很多效果的实现都离不开图像模糊算法的运用。今天，一起来看看社区开发者「詠恆の承諾」是如何基于 RenderTexture 实现多 Pass Kawase Blur。</blockquote></div><br>
屏幕后处理效果（Screen Post Processing Effects）是游戏中实现屏幕特效的方法，有助于提升画面效果。图像模糊算法在后处理渲染领域占据着重要地位，泛光（Bloom）、镜头眩光光晕（Glare Lens Flare）、景深（Depth of Field）、体积光（Volume Ray）等许多效果都用到了图像模糊算法。所以说，后处理中所采用模糊算法的优劣，决定了后处理管线最终的渲染品质和消耗性能的多少。<br>
<br>
<div align="center"><font size="2">
<img aid="1033796" zoomfile="https://di.gameres.com/attachment/forum/202203/16/112205j3fapwigwfy8w3z4.jpg" data-original="https://di.gameres.com/attachment/forum/202203/16/112205j3fapwigwfy8w3z4.jpg" width="600" id="aimg_1033796" inpost="1" src="https://di.gameres.com/attachment/forum/202203/16/112205j3fapwigwfy8w3z4.jpg" referrerpolicy="no-referrer">
</font></div><div align="center"><font size="2">后处理管线中会使用到十种模糊算法总结</font></div><br>
前段时间，由于项目需要做一个背景模糊的功能，正巧之前看到了大城小胖在《如何重绘<江南百景图>》中对比了几种模糊算法，本着学习的态度，我决定尝试在 Cocos Creator 2.4.x 中实现 Dual Blur（双重模糊）。<br>
<br>
<div align="center">
<img aid="1033797" zoomfile="https://di.gameres.com/attachment/forum/202203/16/112205t0qx2a2j2xbuyl3b.png" data-original="https://di.gameres.com/attachment/forum/202203/16/112205t0qx2a2j2xbuyl3b.png" width="600" id="aimg_1033797" inpost="1" src="https://di.gameres.com/attachment/forum/202203/16/112205t0qx2a2j2xbuyl3b.png" referrerpolicy="no-referrer">
</div><div align="center"><font size="2">最终效果</font></div><br>
<strong><font color="#de5650">实现多 Pass</font></strong><br>
<br>
首先要解决的问题是：如何在 v2.4.x 中实现多 pass？<br>
<br>
参考陈皮皮大佬的实现方案[2]，基于 RenderTexture 实现多 Pass Kawase Blur。先将纹理渲染到 RenderTexture（下文简称 RT）上，再对得到的 RT 做单次模糊处理并得到新的 RT，重复此操作，将最后一个 RT 渲染到需要的 Sprite 中即可。<br>
<br>
<strong>注意：每次渲染得到的 RT 是倒置的，渲染前的纹理 Y 轴相反。</strong><br>
<br>
protected renderWithMaterial(srcRT: cc.RenderTexture, dstRT: cc.RenderTexture | cc.Material, material?: cc.Material, size?: cc.Size) &#123;<br>
<br>
// 检查参数<br>
<br>
if (dstRT instanceof cc.Material) &#123;<br>
<br>
material = dstRT;<br>
<br>
dstRT = new cc.RenderTexture();<br>
<br>
&#125;<br>
<br>
// 创建临时节点（用于渲染 RenderTexture）<br>
<br>
const tempNode = new cc.Node();<br>
<br>
tempNode.setParent(cc.Canvas.instance.node);<br>
<br>
const tempSprite = tempNode.addComponent(cc.Sprite);<br>
<br>
tempSprite.sizeMode = cc.Sprite.SizeMode.RAW;<br>
<br>
tempSprite.trim = false;<br>
<br>
tempSprite.spriteFrame = new cc.SpriteFrame(srcRT);<br>
<br>
// 获取图像宽高<br>
<br>
const &#123; width, height &#125; = size ?? &#123; width: srcRT.width, height: srcRT.height &#125;;<br>
<br>
// 初始化 RenderTexture<br>
<br>
// 如果截图内容中不包含 Mask 组件，可以不用传递第三个参数<br>
<br>
dstRT.initWithSize(width, height, cc.gfx.RB_FMT_S8);<br>
<br>
// 更新材质<br>
<br>
if (material instanceof cc.Material) &#123;<br>
<br>
tempSprite.setMaterial(0, material);<br>
<br>
&#125;<br>
<br>
// 创建临时摄像机（用于渲染临时节点）<br>
<br>
const cameraNode = new cc.Node();<br>
<br>
cameraNode.setParent(tempNode);<br>
<br>
const camera = cameraNode.addComponent(cc.Camera);<br>
<br>
camera.clearFlags |= cc.Camera.ClearFlags.COLOR;<br>
<br>
camera.backgroundColor = cc.color(0, 0, 0, 0);<br>
<br>
// 根据屏幕适配方案，决定摄像机缩放比<br>
<br>
// 还原sizeScale，zoomRatio取屏幕与RT宽高比<br>
<br>
camera.zoomRatio = cc.winSize.height / srcRT.height;<br>
<br>
// 将临时节点渲染到 RenderTexture 中<br>
<br>
camera.targetTexture = dstRT;<br>
<br>
camera.render(tempNode);<br>
<br>
// 销毁临时对象<br>
<br>
cameraNode.destroy();<br>
<br>
tempNode.destroy();<br>
<br>
// 返回 RenderTexture<br>
<br>
return dstRT;<br>
<br>
&#125;<br>
<br>
提示！需要留意 cc.RenderTexture.initWithSize(width, height, depthStencilFormat) 中的第3个参数，之前使用时我忽略了第3个参数，加上场景比较复杂，需要截图的结点中带有 Mask 组件，导致截图丢失了 Mask 组件所在结点之前的所有图片。<br>
<br>
查看源码可知道，initWithSize 默认会清除深度缓冲区、模版缓冲区，depthStencilFormat 传入 gfx.RB_FMT_D16、gfx.RB_FMT_S8、gfx.RB_FMT_D24S8 时，则可以保留对应缓冲区。感谢鸦哥（渡鸦）的文章《实现单个 Node 截图的两种方式》[3]，代码+注释太香了！<br>
<br>
/**<br>
<br>
* !#en<br>
<br>
* Init the render texture with size.<br>
<br>
* !#zh<br>
<br>
* 初始化 render texture<br>
<br>
* @param &#123;Number&#125; [width]<br>
<br>
* @param &#123;Number&#125; [height]<br>
<br>
* @param &#123;Number&#125; [depthStencilFormat]<br>
<br>
* @method initWithSize<br>
<br>
*/<br>
<br>
initWithSize (width, height, depthStencilFormat) &#123;<br>
<br>
this.width = Math.floor(width || cc.visibleRect.width);<br>
<br>
this.height = Math.floor(height || cc.visibleRect.height);<br>
<br>
this._resetUnderlyingMipmaps();<br>
<br>
let opts = &#123;<br>
<br>
colors: [ this._texture ],<br>
<br>
&#125;;<br>
<br>
if (this._depthStencilBuffer) this._depthStencilBuffer.destroy();<br>
<br>
let depthStencilBuffer;<br>
<br>
if (depthStencilFormat) &#123;<br>
<br>
depthStencilBuffer = new gfx.RenderBuffer(renderer.device, depthStencilFormat, width, height);<br>
<br>
if (depthStencilFormat === gfx.RB_FMT_D24S8) &#123;<br>
<br>
opts.depthStencil = depthStencilBuffer;<br>
<br>
&#125;<br>
<br>
else if (depthStencilFormat === gfx.RB_FMT_S8) &#123;<br>
<br>
opts.stencil = depthStencilBuffer;<br>
<br>
&#125;<br>
<br>
else if (depthStencilFormat === gfx.RB_FMT_D16) &#123;<br>
<br>
opts.depth = depthStencilBuffer;<br>
<br>
&#125;<br>
<br>
&#125;<br>
<br>
this._depthStencilBuffer = depthStencilBuffer;<br>
<br>
if (this._framebuffer) this._framebuffer.destroy();<br>
<br>
this._framebuffer = new gfx.FrameBuffer(renderer.device, width, height, opts);<br>
<br>
this._packable = false;<br>
<br>
this.loaded = true;<br>
<br>
this.emit("load");<br>
<br>
&#125;,<br>
<br>
<strong><font color="#de5650">Dual Blur（双重模糊）</font></strong><br>
<br>
接下来只需实现 Dual Blur 算法即可。首先简单了解一下 Dual Blur，此处引用《高品质后处理：十种图像模糊算法的总结与实现》[4]一文。<br>
<br>
Dual Kawase Blur，简称 Dual Blur，是一种衍生自 Kawase Blur 的模糊算法，其由两种不同的 Blur Kernel 构成。相较于 Kawase Blur 在两个大小相等的纹理之间进行乒乓 blit 的的思路，Dual Kawase Blur 的核心思路在于 blit 过程中进行降采样和升采样，即对 RT 进行了降采样以及升采样。<br>
<br>
<div align="center">
<img aid="1033798" zoomfile="https://di.gameres.com/attachment/forum/202203/16/112206zmcxssxsmns1m1bp.jpg" data-original="https://di.gameres.com/attachment/forum/202203/16/112206zmcxssxsmns1m1bp.jpg" width="600" id="aimg_1033798" inpost="1" src="https://di.gameres.com/attachment/forum/202203/16/112206zmcxssxsmns1m1bp.jpg" referrerpolicy="no-referrer">
</div><br>
由于灵活的升降采样带来了 blit RT 所需计算量的减少等原因，Dual Kawase Blur 相对而言有更好的性能。下图是相同条件下几种模糊算法的性能对比，可以看到，Dual Kawase Blur 在其中具有最佳的性能表现。<br>
<br>
<div align="center">
<img aid="1033799" zoomfile="https://di.gameres.com/attachment/forum/202203/16/112206jcc63m18mz818igh.png" data-original="https://di.gameres.com/attachment/forum/202203/16/112206jcc63m18mz818igh.png" width="600" id="aimg_1033799" inpost="1" src="https://di.gameres.com/attachment/forum/202203/16/112206jcc63m18mz818igh.png" referrerpolicy="no-referrer">
</div><br>
为了带来更好的性能表现，可以将 uv 的偏移放在 Vert Shader 中进行，而 Fragment Shader 中基本上仅进行采样即可。<br>
<br>
<strong>此外，为了支持合图也能使用，这里我修改了顶点数据。</strong><br>
<br>
// Dual Kawase Blur （双重模糊）<br>
<br>
// 教程地址：https://github.com/QianMo/X-PostProcessing-Library/tree/master/Assets/X-PostProcessing/Effects/DualKawaseBlur<br>
<br>
CCEffect %&#123;<br>
<br>
techniques:<br>
<br>
- name: Down<br>
<br>
passes:<br>
<br>
- name: Down<br>
<br>
vert: vs<img src="https://www.gameres.com/static/image/smiley/default/biggrin.gif" smilieid="3" border="0" alt referrerpolicy="no-referrer">own<br>
<br>
frag: fs:Down<br>
<br>
blendState:<br>
<br>
targets:<br>
<br>
- blend: true<br>
<br>
rasterizerState:<br>
<br>
cullMode: none<br>
<br>
properties: &prop<br>
<br>
texture: &#123; value: white &#125;<br>
<br>
resolution: &#123; value: [1920, 1080] &#125;<br>
<br>
offset: &#123; value: 1, editor: &#123; range: [0, 100] &#125;&#125;<br>
<br>
alphaThreshold: &#123; value: 0.5 &#125;<br>
<br>
- name: Up<br>
<br>
passes:<br>
<br>
- name: Up<br>
<br>
vert: vs:Up<br>
<br>
frag: fs:Up<br>
<br>
blendState:<br>
<br>
targets:<br>
<br>
- blend: true<br>
<br>
rasterizerState:<br>
<br>
cullMode: none<br>
<br>
properties: *prop<br>
<br>
&#125;%<br>
<br>
CCProgram vs %&#123;<br>
<br>
precision highp float;<br>
<br>
#include <cc-global><br>
<br>
#include <cc-local><br>
<br>
in vec3 a_position;<br>
<br>
in vec4 a_color;<br>
<br>
out vec4 v_color;<br>
<br>
#if USE_TEXTURE<br>
<br>
in vec2 a_uv0;<br>
<br>
out vec2 v_uv0;<br>
<br>
out vec4 v_uv1;<br>
<br>
out vec4 v_uv2;<br>
<br>
out vec4 v_uv3;<br>
<br>
out vec4 v_uv4;<br>
<br>
#endif<br>
<br>
uniform Properties &#123;<br>
<br>
vec2 resolution;<br>
<br>
float offset;<br>
<br>
&#125;;<br>
<br>
vec4 Down () &#123;<br>
<br>
vec4 pos = vec4(a_position, 1);<br>
<br>
#if CC_USE_MODEL<br>
<br>
pos = cc_matViewProj * cc_matWorld * pos;<br>
<br>
#else<br>
<br>
pos = cc_matViewProj * pos;<br>
<br>
#endif<br>
<br>
#if USE_TEXTURE<br>
<br>
vec2 uv = a_uv0;<br>
<br>
vec2 texelSize = 0.5 / resolution;<br>
<br>
v_uv0 = uv;<br>
<br>
v_uv1.xy = uv - texelSize * vec2(offset); //top right<br>
<br>
v_uv1.zw = uv + texelSize * vec2(offset); //bottom left<br>
<br>
v_uv2.xy = uv - vec2(texelSize.x, -texelSize.y) * vec2(offset); //top right<br>
<br>
v_uv2.zw = uv + vec2(texelSize.x, -texelSize.y) * vec2(offset); //bottom left<br>
<br>
#endif<br>
<br>
v_color = a_color;<br>
<br>
return pos;<br>
<br>
&#125;<br>
<br>
vec4 Up () &#123;<br>
<br>
vec4 pos = vec4(a_position, 1);<br>
<br>
#if CC_USE_MODEL<br>
<br>
pos = cc_matViewProj * cc_matWorld * pos;<br>
<br>
#else<br>
<br>
pos = cc_matViewProj * pos;<br>
<br>
#endif<br>
<br>
#if USE_TEXTURE<br>
<br>
vec2 uv = a_uv0;<br>
<br>
vec2 texelSize = 0.5 / resolution;<br>
<br>
v_uv0 = uv;<br>
<br>
v_uv1.xy = uv + vec2(-texelSize.x * 2., 0) * offset;<br>
<br>
v_uv1.zw = uv + vec2(-texelSize.x, texelSize.y) * offset;<br>
<br>
v_uv2.xy = uv + vec2(0, texelSize.y * 2.) * offset;<br>
<br>
v_uv2.zw = uv + texelSize * offset;<br>
<br>
v_uv3.xy = uv + vec2(texelSize.x * 2., 0) * offset;<br>
<br>
v_uv3.zw = uv + vec2(texelSize.x, -texelSize.y) * offset;<br>
<br>
v_uv4.xy = uv + vec2(0, -texelSize.y * 2.) * offset;<br>
<br>
v_uv4.zw = uv - texelSize * offset;<br>
<br>
#endif<br>
<br>
v_color = a_color;<br>
<br>
return pos;<br>
<br>
&#125;<br>
<br>
&#125;%<br>
<br>
CCProgram fs %&#123;<br>
<br>
precision highp float;<br>
<br>
#include <alpha-test><br>
<br>
#include <texture><br>
<br>
#include <output><br>
<br>
in vec4 v_color;<br>
<br>
#if USE_TEXTURE<br>
<br>
in vec2 v_uv0;<br>
<br>
in vec4 v_uv1;<br>
<br>
in vec4 v_uv2;<br>
<br>
in vec4 v_uv3;<br>
<br>
in vec4 v_uv4;<br>
<br>
uniform sampler2D texture;<br>
<br>
#endif<br>
<br>
uniform Properties &#123;<br>
<br>
vec2 resolution;<br>
<br>
float offset;<br>
<br>
&#125;;<br>
<br>
vec4 Down () &#123;<br>
<br>
vec4 sum = vec4(1);<br>
<br>
#if USE_TEXTURE<br>
<br>
sum = texture2D(texture, v_uv0) * 4.;<br>
<br>
sum += texture2D(texture, v_uv1.xy);<br>
<br>
sum += texture2D(texture, v_uv1.zw);<br>
<br>
sum += texture2D(texture, v_uv2.xy);<br>
<br>
sum += texture2D(texture, v_uv2.zw);<br>
<br>
sum *= 0.125;<br>
<br>
#endif<br>
<br>
sum *= v_color;<br>
<br>
ALPHA_TEST(sum);<br>
<br>
return CCFragOutput(sum);<br>
<br>
&#125;<br>
<br>
vec4 Up () &#123;<br>
<br>
vec4 sum = vec4(1);<br>
<br>
#if USE_TEXTURE<br>
<br>
CCTexture(texture, v_uv1.xy, sum);<br>
<br>
sum += texture2D(texture, v_uv1.zw) * 2.;<br>
<br>
sum += texture2D(texture, v_uv2.xy);<br>
<br>
sum += texture2D(texture, v_uv2.zw) * 2.;<br>
<br>
sum += texture2D(texture, v_uv3.xy);<br>
<br>
sum += texture2D(texture, v_uv3.zw) * 2.;<br>
<br>
sum += texture2D(texture, v_uv4.xy);<br>
<br>
sum += texture2D(texture, v_uv4.zw) * 2.;<br>
<br>
sum *= 0.0833;<br>
<br>
#endif<br>
<br>
sum *= v_color;<br>
<br>
ALPHA_TEST(sum);<br>
<br>
return CCFragOutput(sum);<br>
<br>
&#125;<br>
<br>
&#125;%<br>
<br>
有了 effect 后，需要创建2个材质分别对应 techniques 中的 Down 与 Up，示例代码中用 materialDown、materialUp 来表示2个材质。<br>
<br>
通过摄像机截图，得到初始 RT 后（纹理倒置），对初始 RT 进行降采样和模糊得到新的 RT，重复若干次后，对最后的 RT 进行相同次数的升采样和模糊，得到最终满足效果的 RT。当降采样 scale 不为1时，设置 RT 尺寸时会自动向下取整，倒置最终效果会有黑边，iteration 次数越大越明显，且 iteration 存在上限，实际使用时可自行取舍。<br>
<br>
/**<br>
<br>
* 模糊渲染<br>
<br>
* @param offset 模糊半径<br>
<br>
* @param iteration 模糊迭代次数<br>
<br>
* @param scale 降采样缩放比例<br>
<br>
*/<br>
<br>
blur(offset: number, iteration: number, scale: number = 0.5) &#123;<br>
<br>
// 设置源结点、目标sprite<br>
<br>
const spriteDst = this.spriteDst,<br>
<br>
nodeSrc = this.spriteSrc.node;<br>
<br>
// 设置材质<br>
<br>
const material = this.materialDown;<br>
<br>
this.materialDown.setProperty('resolution', cc.v2(nodeSrc.width, nodeSrc.height));<br>
<br>
this.materialDown.setProperty('offset', offset);<br>
<br>
this.materialUp.setProperty('resolution', cc.v2(nodeSrc.width, nodeSrc.height));<br>
<br>
this.materialUp.setProperty('offset', offset);<br>
<br>
// 创建临时 RenderTexture<br>
<br>
let srcRT = new cc.RenderTexture(),<br>
<br>
lastRT = new cc.RenderTexture();<br>
<br>
// 获取初始 RenderTexture<br>
<br>
this.getRenderTexture(nodeSrc, lastRT);<br>
<br>
// 多 Pass 处理<br>
<br>
// 注：由于 OpenGL 中的纹理是倒置的，所以双数 Pass 的出的图像是颠倒的<br>
<br>
// 记录升降纹理时纹理尺寸<br>
<br>
let pyramid: [number, number][] = [], tw: number = lastRT.width, th: number = lastRT.height;<br>
<br>
//Downsample<br>
<br>
for (let i = 0; i < iteration; i++) &#123;<br>
<br>
pyramid.push([tw, th]);<br>
<br>
[lastRT, srcRT] = [srcRT, lastRT];<br>
<br>
// 缩小截图尺寸，提高效率<br>
<br>
// 缩小尺寸时，RT会自动向下取整，导致黑边<br>
<br>
tw = Math.max(tw * scale, 1), th = Math.max(th * scale, 1);<br>
<br>
this.renderWithMaterial(srcRT, lastRT, this.materialDown, cc.size(tw, th));<br>
<br>
&#125;<br>
<br>
// Upsample<br>
<br>
for (let i = iteration - 1; i >= 0; i--) &#123;<br>
<br>
[lastRT, srcRT] = [srcRT, lastRT];<br>
<br>
this.renderWithMaterial(srcRT, lastRT, this.materialUp, cc.size(pyramid<i>[0], pyramid<i>[1]));<br>
<br>
&#125;<br>
<br>
// 使用经过处理的 RenderTexture<br>
<br>
this.renderTexture = lastRT;<br>
<br>
spriteDst.spriteFrame = new cc.SpriteFrame(this.renderTexture);<br>
<br>
// 翻转纹理y轴<br>
<br>
spriteDst.spriteFrame.setFlipY(true);<br>
<br>
// 销毁不用的临时 RenderTexture<br>
<br>
srcRT.destroy();<br>
<br>
&#125;<br>
<br>
以上是本次的分享，希望可以给大家一点启发和帮助！欢迎点击【阅读原文】前往论坛专贴一起讨论交流，完整代码见代码仓库：<br>
<br>
https://github.com/RicardoZhou/CreatorStudy/tree/master/assets/Menu/Shader/DualBlur<br>
<br>
<strong>参考资料</strong><br>
<br>
<font size="2">[1]如何重绘《江南百景图》，大城小胖</font><font size="2"><br>
</font><br>
<font size="2">[2]基于 RenderTexture 实现多 Pass 的 Kawase Blur，陈皮皮</font><br>
<font size="2">https://forum.cocos.org/t/topic/126481</font><font size="2"><br>
</font><br>
<font size="2">[3]Creator丨实现单个 Node 截图的两种方式，渡鸦</font><font size="2"><br>
</font><br>
<font size="2">[4]高品质后处理：十种图像模糊算法的总结与实现，毛星云</font><br>
<font size="2">https://zhuanlan.zhihu.com/p/125744132</font><font size="2"><br>
</font><br>
<font size="2">[5]自定义顶点格式，GT</font><br>
<font size="2">https://forum.cocos.org/t/topic/95087</font><font size="2"><br>
</font><br>
<font size="2"></font><br>
<font size="2">来源：COCOS</font><br>
<font size="2">原文：https://mp.weixin.qq.com/s/qwndpZo1QdR9icoBGXdyOg</font><br>
<br>
</i></i>  
</div>
            