
---
title: 'Shader 之顶点着色器能做什么？Cocos Creator 实现模拟云海'
categories: 
 - 游戏
 - GameRes 游资网
 - 热点推荐
headimg: 'https://di.gameres.com/attachment/forum/202201/28/114617r98lqvmx0mggz9gi.jpg'
author: GameRes 游资网
comments: false
date: Fri, 28 Jan 2022 00:00:00 GMT
thumbnail: 'https://di.gameres.com/attachment/forum/202201/28/114617r98lqvmx0mggz9gi.jpg'
---

<div>   
今天将基于 Cocos Creator 3.3.1，通过一个模拟云海效果的 Demo，一步步编写顶点着色器，实现修改模型的形状，来一起了解一下 Mesh 模型、顶点着色器、片元着色器、噪声之间的作用。<br>
<br>
本文着重于分享顶点着色器「能做的事情」，并不是真的想模拟一个真正的云海，毕竟对比 RAYMarching 体积云之类的效果来说还是有一定差距。<br>
<br>
选用这个来作为开篇的理由很简单：<br>
<br>
<div align="center"><font size="2">
<img aid="1029806" zoomfile="https://di.gameres.com/attachment/forum/202201/28/114617r98lqvmx0mggz9gi.jpg" data-original="https://di.gameres.com/attachment/forum/202201/28/114617r98lqvmx0mggz9gi.jpg" width="600" id="aimg_1029806" inpost="1" src="https://di.gameres.com/attachment/forum/202201/28/114617r98lqvmx0mggz9gi.jpg" referrerpolicy="no-referrer">
</font></div><div align="center"><font size="2">图源网络</font></div><br>
这里用到的 <strong>Mesh</strong> 的形状是矩形。显卡只能绘制三角形，那么绘制一个矩形至少要两个三角形拼接起来。如果有非常多的小矩形，组成一个大矩形，其实就相当于有很多的小三角形，组成一个大矩形。<br>
<br>
<div align="center">
<img aid="1029807" zoomfile="https://di.gameres.com/attachment/forum/202201/28/114617yk6ls6n3j3hlu6ld.jpg" data-original="https://di.gameres.com/attachment/forum/202201/28/114617yk6ls6n3j3hlu6ld.jpg" width="600" id="aimg_1029807" inpost="1" src="https://di.gameres.com/attachment/forum/202201/28/114617yk6ls6n3j3hlu6ld.jpg" referrerpolicy="no-referrer">
</div><br>
<strong>顶点着色器</strong>只修改了模型的 Y 轴，没有做过多的改变。顶点着色器的变化只是从噪声贴图中获取该怎么变，没有使用复杂的公式计算，所以也很容易想象。<br>
<br>
<strong>片元着色器</strong>更简单，只是返回了顶点着色器输出的 v_color，顶点着色器输出的值会根据重心坐标进行差值。<br>
<br>
<strong>噪声</strong>是一个只有黑白灰的图片，所以也很容易理解。<br>
<br>
<div align="center"><font size="2">
<img aid="1029808" zoomfile="https://di.gameres.com/attachment/forum/202201/28/114617gi8sa9g017eaa79e.gif" data-original="https://di.gameres.com/attachment/forum/202201/28/114617gi8sa9g017eaa79e.gif" width="420" id="aimg_1029808" inpost="1" src="https://di.gameres.com/attachment/forum/202201/28/114617gi8sa9g017eaa79e.gif" referrerpolicy="no-referrer">
</font></div><div align="center"><font size="2">效果预览</font></div><br>
结合我们已知的知识整理一下思路：<br>
<br>
GPU 渲染的是一个一个的三角形。<br>
<br>
一个面只要顶点够多，就能生成一个平滑的曲面——因此，在低端机可以让三角形【顶点】少一些。<br>
<br>
动态生成一个 Mesh，是一个平面，并且三角形足够的多。<br>
<br>
通过一张外部图片【噪声】的信息，来存储云的凹凸信息——可以想到，一张图只有黑白灰，越白的地方，让三角形的高度越高，反之亦然。<br>
<br>
让这张贴图运动【滚动】起来，随着时间的变化，修改获取 UV 的位置信息——这样三角形就可以变化了。<br>
<br>
通过读取多张噪声，或者读取同一张噪声不同位置的地方，叠加起来，就可以获得翻涌的感觉。<br>
<br>
接下来进入正题，上手实操！<br>
<br>
限于篇幅，本文仅展示部分核心代码，完整代码及 Demo 工程请移步论坛讨论帖查看、下载：<br>
<br>
https://forum.cocos.org/t/topic/128595<br>
<strong><font color="#de5650"><br>
</font></strong><br>
<strong><font color="#de5650">1、准备</font></strong><br>
<br>
首先创建默认的场景、材质和 effect 文件。<br>
<br>
<div align="center">
<img aid="1029809" zoomfile="https://di.gameres.com/attachment/forum/202201/28/114617y634nsnwzswpmg1j.jpg" data-original="https://di.gameres.com/attachment/forum/202201/28/114617y634nsnwzswpmg1j.jpg" width="272" id="aimg_1029809" inpost="1" src="https://di.gameres.com/attachment/forum/202201/28/114617y634nsnwzswpmg1j.jpg" referrerpolicy="no-referrer">
</div><br>
<strong><font color="#de5650">2、编辑 effect 文件</font></strong><br>
<br>
双击打开 effect，获得默认的 Cocos 的 Shader 文件，可以看到一行：<br>
<br>
- vert: general-vs:vert # builtin header<br>
<br>
根据后面的注释可知，这里使用了默认的 builtin 的顶点着色器，可参考 Cocos 官方文档。<br>
<br>
Effect Syntax · Cocos Creator<br>
<br>
https://docs.cocos.com/creator/3.3/manual/zh/material-system/effect-syntax.html<br>
<br>
所以这个文件里面缺少了要编写的顶点着色器，因此需要手动补充一个。<br>
<br>
找到自带的 chunks 里面的 general-vs，将内容复制出来。<br>
<br>
<div align="center">
<img aid="1029810" zoomfile="https://di.gameres.com/attachment/forum/202201/28/114618g4b8by44b84tb4g2.jpg" data-original="https://di.gameres.com/attachment/forum/202201/28/114618g4b8by44b84tb4g2.jpg" width="600" id="aimg_1029810" inpost="1" src="https://di.gameres.com/attachment/forum/202201/28/114618g4b8by44b84tb4g2.jpg" referrerpolicy="no-referrer">
</div><br>
回到 effect 文件中，补充一个 CCProgram 块 my-vs：<br>
<br>
CCProgram my-vs %&#123;<br>
<br>
precision highp float;<br>
<br>
#include <input-standard><br>
<br>
#include <cc-global><br>
<br>
#include <cc-local-batch><br>
<br>
#include <input-standard><br>
<br>
#include <cc-fog-vs><br>
<br>
#include <cc-shadow-map-vs><br>
<br>
in vec4 a_color;<br>
<br>
#if HAS_SECOND_UV<br>
<br>
in vec2 a_texCoord1;<br>
<br>
#endif<br>
<br>
out vec3 v_position;<br>
<br>
out vec3 v_normal;<br>
<br>
out vec3 v_tangent;<br>
<br>
out vec3 v_bitangent;<br>
<br>
out vec2 v_uv;<br>
<br>
out vec2 v_uv1;<br>
<br>
out vec4 v_color;<br>
<br>
vec4 vert () &#123;<br>
<br>
StandardVertInput In;<br>
<br>
CCVertInput(In);<br>
<br>
mat4 matWorld, matWorldIT;<br>
<br>
CCGetWorldMatrixFull(matWorld, matWorldIT);<br>
<br>
vec4 pos = matWorld * In.position;<br>
<br>
v_position = pos.xyz;<br>
<br>
v_normal = normalize((matWorldIT * vec4(In.normal, 0.0)).xyz);<br>
<br>
v_tangent = normalize((matWorld * vec4(In.tangent.xyz, 0.0)).xyz);<br>
<br>
v_bitangent = cross(v_normal, v_tangent) * In.tangent.w; // note the cross order<br>
<br>
v_uv = a_texCoord;<br>
<br>
#if HAS_SECOND_UV<br>
<br>
v_uv1 = a_texCoord1;<br>
<br>
#endif<br>
<br>
v_color = a_color;<br>
<br>
CC_TRANSFER_FOG(pos);<br>
<br>
CC_TRANSFER_SHADOW(pos);<br>
<br>
return cc_matProj * (cc_matView * matWorld) * In.position;<br>
<br>
&#125;<br>
<br>
&#125;%<br>
<br>
并且将最上面的 CCEffect 的 vert 部分定义修改成：my-vs:vert<br>
<br>
CCEffect %&#123;<br>
<br>
techniques:<br>
<br>
- name: opaque<br>
<br>
passes:<br>
<br>
- vert: my-vs:vert # builtin header<br>
<br>
frag: unlit-fs:frag<br>
<br>
properties: &props<br>
<br>
mainTexture:    &#123; value: white &#125;<br>
<br>
mainColor:      &#123; value: [1, 1, 1, 1], editor: &#123; type: color &#125; &#125;<br>
<br>
- name: transparent<br>
<br>
passes:<br>
<br>
- vert: general-vs:vert # builtin header<br>
<br>
frag: unlit-fs:frag<br>
<br>
blendState:<br>
<br>
targets:<br>
<br>
- blend: true<br>
<br>
blendSrc: src_alpha<br>
<br>
blendDst: one_minus_src_alpha<br>
<br>
blendSrcAlpha: src_alpha<br>
<br>
blendDstAlpha: one_minus_src_alpha<br>
<br>
properties: *props<br>
<br>
&#125;%<br>
<br>
<strong><font color="#de5650">3、绑定 effect 到材质上</font></strong><br>
<br>
<div align="center">
<img aid="1029811" zoomfile="https://di.gameres.com/attachment/forum/202201/28/114618lfvwd3wkk6taa33f.jpg" data-original="https://di.gameres.com/attachment/forum/202201/28/114618lfvwd3wkk6taa33f.jpg" width="600" id="aimg_1029811" inpost="1" src="https://di.gameres.com/attachment/forum/202201/28/114618lfvwd3wkk6taa33f.jpg" referrerpolicy="no-referrer">
</div><br>
选中材质，选择 Effect，选中刚刚新建的 effect 文件，最后不要忘记点击右上角的箭头，保存一下。正确的话会预览出一个纯白的方块。<br>
<br>
<div align="center">
<img aid="1029812" zoomfile="https://di.gameres.com/attachment/forum/202201/28/114618y5820oenk528j5tw.jpg" data-original="https://di.gameres.com/attachment/forum/202201/28/114618y5820oenk528j5tw.jpg" width="600" id="aimg_1029812" inpost="1" src="https://di.gameres.com/attachment/forum/202201/28/114618y5820oenk528j5tw.jpg" referrerpolicy="no-referrer">
</div><br>
<strong><font color="#de5650">4、创建 Plane 并应用材质</font></strong><br>
<br>
<div align="center">
<img aid="1029813" zoomfile="https://di.gameres.com/attachment/forum/202201/28/114619pl9vgr9nzwfn8rut.jpg" data-original="https://di.gameres.com/attachment/forum/202201/28/114619pl9vgr9nzwfn8rut.jpg" width="600" id="aimg_1029813" inpost="1" src="https://di.gameres.com/attachment/forum/202201/28/114619pl9vgr9nzwfn8rut.jpg" referrerpolicy="no-referrer">
</div><br>
场景中创建 3D 对象，Plane。<br>
<br>
<div align="center">
<img aid="1029814" zoomfile="https://di.gameres.com/attachment/forum/202201/28/114619yzr3kou0ko3r3932.jpg" data-original="https://di.gameres.com/attachment/forum/202201/28/114619yzr3kou0ko3r3932.jpg" width="600" id="aimg_1029814" inpost="1" src="https://di.gameres.com/attachment/forum/202201/28/114619yzr3kou0ko3r3932.jpg" referrerpolicy="no-referrer">
</div><br>
选中 Plane 节点，将 material 拖拽覆盖原本的 default-material 材质，最终可以得到一个纯白的 Plane。<br>
<br>
<div align="center">
<img aid="1029815" zoomfile="https://di.gameres.com/attachment/forum/202201/28/114619nfhgp0yb8qhumyhm.jpg" data-original="https://di.gameres.com/attachment/forum/202201/28/114619nfhgp0yb8qhumyhm.jpg" width="600" id="aimg_1029815" inpost="1" src="https://di.gameres.com/attachment/forum/202201/28/114619nfhgp0yb8qhumyhm.jpg" referrerpolicy="no-referrer">
</div><br>
<strong><font color="#de5650">5、准备噪声贴图</font></strong><br>
<br>
<div align="center">
<img aid="1029816" zoomfile="https://di.gameres.com/attachment/forum/202201/28/114619ozccazppc4dc5rcf.jpg" data-original="https://di.gameres.com/attachment/forum/202201/28/114619ozccazppc4dc5rcf.jpg" width="256" id="aimg_1029816" inpost="1" src="https://di.gameres.com/attachment/forum/202201/28/114619ozccazppc4dc5rcf.jpg" referrerpolicy="no-referrer">
</div><br>
<div align="center">
<img aid="1029817" zoomfile="https://di.gameres.com/attachment/forum/202201/28/114620e3jv4nnr2jxyl2py.jpg" data-original="https://di.gameres.com/attachment/forum/202201/28/114620e3jv4nnr2jxyl2py.jpg" width="256" id="aimg_1029817" inpost="1" src="https://di.gameres.com/attachment/forum/202201/28/114620e3jv4nnr2jxyl2py.jpg" referrerpolicy="no-referrer">
</div><br>
这里有两张噪声，他们看上去好像并没有区别，但是如果让 UV 偏移0.5的话就会发生奇怪的问题。现在我们来测试一下。<br>
<br>
先简单修改下片元着色器，也就是 frag 块：<br>
<br>
CCProgram unlit-fs %&#123;<br>
<br>
precision highp float;<br>
<br>
#include <output><br>
<br>
#include <cc-fog-fs><br>
<br>
in vec2 v_uv;<br>
<br>
uniform sampler2D mainTexture;<br>
<br>
uniform Constant &#123;<br>
<br>
vec4 mainColor;<br>
<br>
&#125;;<br>
<br>
vec4 frag () &#123;<br>
<br>
vec4 col = mainColor * texture(mainTexture, v_uv + 0.5);<br>
<br>
CC_APPLY_FOG(col);<br>
<br>
return CCFragOutput(col);<br>
<br>
&#125;<br>
<br>
&#125;%<br>
<br>
注意：这里修改了 UV 的取值，将 v_uv 增加了0.5。<br>
<br>
回到 Cocos Creator，将两张噪声分别放进材质里，看看会发生什么。<br>
<br>
<div align="center">
<img aid="1029818" zoomfile="https://di.gameres.com/attachment/forum/202201/28/114620n15e85e01e7173me.jpg" data-original="https://di.gameres.com/attachment/forum/202201/28/114620n15e85e01e7173me.jpg" width="600" id="aimg_1029818" inpost="1" src="https://di.gameres.com/attachment/forum/202201/28/114620n15e85e01e7173me.jpg" referrerpolicy="no-referrer">
</div><br>
<div align="center">
<img aid="1029819" zoomfile="https://di.gameres.com/attachment/forum/202201/28/114620dleleehhue61ys6t.jpg" data-original="https://di.gameres.com/attachment/forum/202201/28/114620dleleehhue61ys6t.jpg" width="600" id="aimg_1029819" inpost="1" src="https://di.gameres.com/attachment/forum/202201/28/114620dleleehhue61ys6t.jpg" referrerpolicy="no-referrer">
</div><br>
可以很明显地发现噪声在偏移之后，中间并不平滑。所以这里使用的噪声贴图有一个条件：无缝噪声。<br>
<br>
测试完记得把 +0.5 删掉！！<br>
<br>
<strong><font color="#de5650">6、修改顶点着色器</font></strong><br>
<br>
定义 mainTexture。<br>
<br>
定义 p = In.position，并且用 p 代替后续代码中的 In.position。<br>
<br>
将噪声图映射在矩形上面，矩形上各个三角形对应的顶点，判断颜色是更黑还是更白，根据颜色值的深浅来决定这个顶点在 y 值上的高低。在着色器中，颜色的取值范围是 0~1，所以现在每个顶点的 y 有了高度信息，即取值范围 0~1。<br>
<br>
<div align="center">
<img aid="1029820" zoomfile="https://di.gameres.com/attachment/forum/202201/28/114620sbn1hbnlel77hli2.jpg" data-original="https://di.gameres.com/attachment/forum/202201/28/114620sbn1hbnlel77hli2.jpg" width="600" id="aimg_1029820" inpost="1" src="https://di.gameres.com/attachment/forum/202201/28/114620sbn1hbnlel77hli2.jpg" referrerpolicy="no-referrer">
</div><br>
并且，由于是黑白灰的噪声，所以 r=g=b，直接将 r 的颜色赋值给 p.y。<br>
<br>
uniform sampler2D mainTexture;<br>
<br>
vec4 vert () &#123;<br>
<br>
StandardVertInput In;<br>
<br>
CCVertInput(In);<br>
<br>
mat4 matWorld, matWorldIT;<br>
<br>
CCGetWorldMatrixFull(matWorld, matWorldIT);<br>
<br>
vec4 p = In.position;<br>
<br>
float y = texture(mainTexture, a_texCoord).x;<br>
<br>
p.y = y;<br>
<br>
vec4 pos = matWorld * p;<br>
<br>
v_position = pos.xyz;<br>
<br>
v_normal = normalize((matWorldIT * vec4(In.normal, 0.0)).xyz);<br>
<br>
v_tangent = normalize((matWorld * vec4(In.tangent.xyz, 0.0)).xyz);<br>
<br>
v_bitangent = cross(v_normal, v_tangent) * In.tangent.w; // note the cross order<br>
<br>
v_uv = a_texCoord;<br>
<br>
#if HAS_SECOND_UV<br>
<br>
v_uv1 = a_texCoord1;<br>
<br>
#endif<br>
<br>
v_color = a_color;<br>
<br>
CC_TRANSFER_FOG(pos);<br>
<br>
CC_TRANSFER_SHADOW(pos);<br>
<br>
return cc_matProj * (cc_matView * matWorld) * p;<br>
<br>
&#125;<br>
<br>
回到 Cocos Creator 就可以发现 Plane 变得凹凸不平，并且越黑的地方越低，越白的地方越高。<br>
<br>
<div align="center">
<img aid="1029821" zoomfile="https://di.gameres.com/attachment/forum/202201/28/114621q3rlbwqkrbns3giu.jpg" data-original="https://di.gameres.com/attachment/forum/202201/28/114621q3rlbwqkrbns3giu.jpg" width="600" id="aimg_1029821" inpost="1" src="https://di.gameres.com/attachment/forum/202201/28/114621q3rlbwqkrbns3giu.jpg" referrerpolicy="no-referrer">
</div><br>
<strong><font color="#de5650">7、平滑</font></strong><br>
<br>
<div align="center">
<img aid="1029822" zoomfile="https://di.gameres.com/attachment/forum/202201/28/114621kxe3xjaea11prbjz.jpg" data-original="https://di.gameres.com/attachment/forum/202201/28/114621kxe3xjaea11prbjz.jpg" width="600" id="aimg_1029822" inpost="1" src="https://di.gameres.com/attachment/forum/202201/28/114621kxe3xjaea11prbjz.jpg" referrerpolicy="no-referrer">
</div><br>
默认的 Plane 面数比较少，所以会变得比较不平滑。<br>
<br>
<div align="center">
<img aid="1029823" zoomfile="https://di.gameres.com/attachment/forum/202201/28/114621urwzqiig9l9g3vyh.jpg" data-original="https://di.gameres.com/attachment/forum/202201/28/114621urwzqiig9l9g3vyh.jpg" width="544" id="aimg_1029823" inpost="1" src="https://di.gameres.com/attachment/forum/202201/28/114621urwzqiig9l9g3vyh.jpg" referrerpolicy="no-referrer">
</div><br>
创建一个脚本，叫 my-mesh，用来替换 plane 的默认 mesh：<br>
<br>
import &#123; _decorator, Component, utils, primitives, MeshRenderer &#125; from 'cc';<br>
<br>
const &#123; ccclass, property &#125; = _decorator;<br>
<br>
@ccclass('MyMesh')<br>
<br>
export class MyMesh extends Component &#123;<br>
<br>
start () &#123;<br>
<br>
const renderer = this.node.getComponent(MeshRenderer);<br>
<br>
if(!renderer)&#123;<br>
<br>
return;<br>
<br>
&#125;<br>
<br>
const plane: primitives.IGeometry = primitives.plane(&#123;<br>
<br>
width: 10,<br>
<br>
length: 10<br>
<br>
widthSegments: 100,<br>
<br>
lengthSegments: 100,<br>
<br>
&#125;);<br>
<br>
renderer.mesh = utils.createMesh(plane);<br>
<br>
&#125;<br>
<br>
&#125;<br>
<br>
<div align="center">
<img aid="1029824" zoomfile="https://di.gameres.com/attachment/forum/202201/28/114621yn2x9wuabdbpjkuu.jpg" data-original="https://di.gameres.com/attachment/forum/202201/28/114621yn2x9wuabdbpjkuu.jpg" width="600" id="aimg_1029824" inpost="1" src="https://di.gameres.com/attachment/forum/202201/28/114621yn2x9wuabdbpjkuu.jpg" referrerpolicy="no-referrer">
</div><br>
回到 Cocos Creator，将脚本和 Node 绑定起来，并且运行。可以看到，相对编辑器中的已经平滑了许多，并且很容易的区分出高低的颜色。<br>
<br>
<div align="center">
<img aid="1029825" zoomfile="https://di.gameres.com/attachment/forum/202201/28/114621ie2eo1jrjzwbjjjo.jpg" data-original="https://di.gameres.com/attachment/forum/202201/28/114621ie2eo1jrjzwbjjjo.jpg" width="600" id="aimg_1029825" inpost="1" src="https://di.gameres.com/attachment/forum/202201/28/114621ie2eo1jrjzwbjjjo.jpg" referrerpolicy="no-referrer">
</div><br>
<strong><font color="#de5650">8、运动</font></strong><br>
<br>
引入时间戳（单位：s），根据时间的不同，获取不同位置的 UV 信息，就可以让画面滚动起来。<br>
<br>
引入 #incloud cc-global。<br>
<br>
修改 UV 的获取，a_texCoord 值加上 cc_time.x 并且 *一个速度系数0.1。<br>
<br>
uniform sampler2D mainTexture;<br>
<br>
#include <cc-global><br>
<br>
vec4 vert () &#123;<br>
<br>
StandardVertInput In;<br>
<br>
CCVertInput(In);<br>
<br>
mat4 matWorld, matWorldIT;<br>
<br>
CCGetWorldMatrixFull(matWorld, matWorldIT);<br>
<br>
vec4 p = In.position;<br>
<br>
float y = texture(mainTexture, a_texCoord + cc_time.x * 0.1).x;<br>
<br>
p.y = y;<br>
<br>
vec4 pos = matWorld * p;<br>
<br>
v_position = pos.xyz;<br>
<br>
v_normal = normalize((matWorldIT * vec4(In.normal, 0.0)).xyz);<br>
<br>
v_tangent = normalize((matWorld * vec4(In.tangent.xyz, 0.0)).xyz);<br>
<br>
v_bitangent = cross(v_normal, v_tangent) * In.tangent.w; // note the cross order<br>
<br>
v_uv = a_texCoord;<br>
<br>
#if HAS_SECOND_UV<br>
<br>
v_uv1 = a_texCoord1;<br>
<br>
#endif<br>
<br>
v_color = a_color;<br>
<br>
CC_TRANSFER_FOG(pos);<br>
<br>
CC_TRANSFER_SHADOW(pos);<br>
<br>
return cc_matProj * (cc_matView * matWorld) * p;<br>
<br>
&#125;<br>
<br>
&#125;%<br>
<br>
<div align="center">
<img aid="1029826" zoomfile="https://di.gameres.com/attachment/forum/202201/28/114622xyydeqp6udu263ud.gif" data-original="https://di.gameres.com/attachment/forum/202201/28/114622xyydeqp6udu263ud.gif" width="402" id="aimg_1029826" inpost="1" src="https://di.gameres.com/attachment/forum/202201/28/114622xyydeqp6udu263ud.gif" referrerpolicy="no-referrer">
</div><br>
<strong><font color="#de5650">9、颜色</font></strong><br>
<br>
形状改变了，但是颜色好像并没有重新发生变化。<br>
<br>
修改顶点着色器，将 texture 函数获取到的颜色直接丢给 v_color。<br>
<br>
修改片元着色器，直接将 v_color 颜色返回（记得先声明 in vec4 v_color）。<br>
<br>
CCProgram my-vs %&#123;<br>
<br>
precision highp float;<br>
<br>
#include <input-standard><br>
<br>
#include <cc-global><br>
<br>
#include <cc-local-batch><br>
<br>
#include <input-standard><br>
<br>
#include <cc-fog-vs><br>
<br>
#include <cc-shadow-map-vs><br>
<br>
in vec4 a_color;<br>
<br>
#if HAS_SECOND_UV<br>
<br>
in vec2 a_texCoord1;<br>
<br>
#endif<br>
<br>
out vec3 v_position;<br>
<br>
out vec3 v_normal;<br>
<br>
out vec3 v_tangent;<br>
<br>
out vec3 v_bitangent;<br>
<br>
out vec2 v_uv;<br>
<br>
out vec2 v_uv1;<br>
<br>
out vec4 v_color;<br>
<br>
uniform sampler2D mainTexture;<br>
<br>
#include <cc-global><br>
<br>
vec4 vert () &#123;<br>
<br>
StandardVertInput In;<br>
<br>
CCVertInput(In);<br>
<br>
mat4 matWorld, matWorldIT;<br>
<br>
CCGetWorldMatrixFull(matWorld, matWorldIT);<br>
<br>
vec4 p = In.position;<br>
<br>
vec4 baseColor0 = texture(mainTexture, a_texCoord + cc_time.x * 0.1);<br>
<br>
p.y = baseColor0.x;<br>
<br>
vec4 pos = matWorld * p;<br>
<br>
v_position = pos.xyz;<br>
<br>
v_normal = normalize((matWorldIT * vec4(In.normal, 0.0)).xyz);<br>
<br>
v_tangent = normalize((matWorld * vec4(In.tangent.xyz, 0.0)).xyz);<br>
<br>
v_bitangent = cross(v_normal, v_tangent) * In.tangent.w; // note the cross order<br>
<br>
v_uv = a_texCoord;<br>
<br>
#if HAS_SECOND_UV<br>
<br>
v_uv1 = a_texCoord1;<br>
<br>
#endif<br>
<br>
v_color = baseColor0;<br>
<br>
CC_TRANSFER_FOG(pos);<br>
<br>
CC_TRANSFER_SHADOW(pos);<br>
<br>
return cc_matProj * (cc_matView * matWorld) * p;<br>
<br>
&#125;<br>
<br>
&#125;%<br>
<br>
CCProgram unlit-fs %&#123;<br>
<br>
precision highp float;<br>
<br>
#include <output><br>
<br>
#include <cc-fog-fs><br>
<br>
in vec2 v_uv;<br>
<br>
in vec4 v_color;<br>
<br>
uniform sampler2D mainTexture;<br>
<br>
uniform Constant &#123;<br>
<br>
vec4 mainColor;<br>
<br>
&#125;;<br>
<br>
vec4 frag () &#123;<br>
<br>
return v_color;<br>
<br>
&#125;<br>
<br>
&#125;%<br>
<br>
可以发现没有刚刚的问题了，回到越白的地方越高，越黑的地方越暗了。<br>
<br>
<div align="center">
<img aid="1029827" zoomfile="https://di.gameres.com/attachment/forum/202201/28/114622hlep7jljyiixil67.gif" data-original="https://di.gameres.com/attachment/forum/202201/28/114622hlep7jljyiixil67.gif" width="420" id="aimg_1029827" inpost="1" src="https://di.gameres.com/attachment/forum/202201/28/114622hlep7jljyiixil67.gif" referrerpolicy="no-referrer">
</div><br>
<strong><font color="#de5650">10、噪声叠加-翻涌</font></strong><br>
<br>
噪声可以用多张，也可以读取多次，只要读取的位置不一样，并且叠加起来，那么就可以得到翻涌的感觉了。<br>
<br>
定义了 tiling0 和 tiling1，其中，xy 用来控制 UV 的倍率，zw 用来控制 UV 移动的方向。<br>
<br>
texture 采样两次，分别为 baseColor0 和 baseColor1，并且两个颜色的红色加起来 *0.5，赋值给 p.y。<br>
<br>
p.y 最后还 -0.5，是因为 y 的值原本在 0~1 之间，希望最后在 -0.5~0.5 之间分布，所以整体 -0.5。<br>
<br>
将 v_color = baseColor0 改成 v_color = (baseColor0 + baseColor1)* 0.5。<br>
<br>
vec4 vert () &#123;<br>
<br>
StandardVertInput In;<br>
<br>
CCVertInput(In);<br>
<br>
mat4 matWorld, matWorldIT;<br>
<br>
CCGetWorldMatrixFull(matWorld, matWorldIT);<br>
<br>
vec4 p = In.position;<br>
<br>
vec4 tiling0 = vec4(1.0, 1.0, 0.1, 0.1);<br>
<br>
vec4 tiling1 = vec4(1.0, 1.0, 0.07, 0.07);<br>
<br>
vec4 baseColor0 = texture(mainTexture, a_texCoord * tiling0.xy + cc_time.x * tiling0.zw);<br>
<br>
vec4 baseColor1 = texture(mainTexture, a_texCoord * tiling1.xy + cc_time.x * tiling1.zw);<br>
<br>
p.y = (baseColor0.x + baseColor1.x) * 0.5 - 0.5;<br>
<br>
vec4 pos = matWorld * p;<br>
<br>
v_position = pos.xyz;<br>
<br>
v_normal = normalize((matWorldIT * vec4(In.normal, 0.0)).xyz);<br>
<br>
v_tangent = normalize((matWorld * vec4(In.tangent.xyz, 0.0)).xyz);<br>
<br>
v_bitangent = cross(v_normal, v_tangent) * In.tangent.w; // note the cross order<br>
<br>
v_uv = a_texCoord;<br>
<br>
#if HAS_SECOND_UV<br>
<br>
v_uv1 = a_texCoord1;<br>
<br>
#endif<br>
<br>
v_color = (baseColor0 + baseColor1)* 0.5;<br>
<br>
CC_TRANSFER_FOG(pos);<br>
<br>
CC_TRANSFER_SHADOW(pos);<br>
<br>
return cc_matProj * (cc_matView * matWorld) * p;<br>
<br>
&#125;<br>
<br>
可以发现运动不再和上面一样只是单一运动，而是带上了起伏的感觉。<br>
<br>
<div align="center">
<img aid="1029828" zoomfile="https://di.gameres.com/attachment/forum/202201/28/114623e8zdndzeneotcfon.gif" data-original="https://di.gameres.com/attachment/forum/202201/28/114623e8zdndzeneotcfon.gif" width="420" id="aimg_1029828" inpost="1" src="https://di.gameres.com/attachment/forum/202201/28/114623e8zdndzeneotcfon.gif" referrerpolicy="no-referrer">
</div><br>
<strong><font color="#de5650">11、颜色过渡</font></strong><br>
<br>
黑白灰毕竟不好看，所以我们自定义两个颜色（c0 和 c1）来重新定义高低。<br>
<br>
vec4 c0 = vec4(1.0, 0.0, 0.0, 1.0);<br>
<br>
vec4 c1 = vec4(0.0, 1.0, 0.0, 1.0);<br>
<br>
v_color = (p.y + 0.5) * (c0 - c1) + c1;<br>
<br>
c0 表示最高处的颜色；<br>
<br>
c1 表示最低处的颜色；<br>
<br>
c0 - c1 = 两个颜色的差距；<br>
<br>
p.y + 0.5 得到一个 0~1 之间的值，用来表示当前 y 的高度；<br>
<br>
(p.y + 0.5) * (c0 - c1) 得到一个 y 高度变化中的过渡值；<br>
<br>
过渡值 +c1，表示过渡值 + 基础值 = 最终的颜色；<br>
<br>
c0 - c1 等于两个颜色分量的差，用差 *（y + 0.5）得到变化值，最后再加上 c1。<br>
<br>
这样就得到了一个自定义颜色的 Shader。<br>
<br>
<div align="center">
<img aid="1029829" zoomfile="https://di.gameres.com/attachment/forum/202201/28/114623viv5vhhi6c559fch.gif" data-original="https://di.gameres.com/attachment/forum/202201/28/114623viv5vhhi6c559fch.gif" width="420" id="aimg_1029829" inpost="1" src="https://di.gameres.com/attachment/forum/202201/28/114623viv5vhhi6c559fch.gif" referrerpolicy="no-referrer">
</div><br>
<strong><font color="#de5650">12、将定义的数据暴露给材质面板</font></strong><br>
<br>
目前位置，这里定义了两个 tiling，两个颜色 c0 和 c1：<br>
<br>
CCEffect %&#123;<br>
<br>
techniques:<br>
<br>
- name: opaque<br>
<br>
passes:<br>
<br>
- vert: my-vs:vert # builtin header<br>
<br>
frag: unlit-fs:frag<br>
<br>
properties: &props<br>
<br>
mainTexture:    &#123; value: white &#125;<br>
<br>
mainColor:      &#123; value: [1, 1, 1, 1], editor: &#123; type: color &#125; &#125;<br>
<br>
c0:      &#123; value: [1, 0, 0, 1], editor: &#123; type: color &#125; &#125;<br>
<br>
c1:      &#123; value: [0, 1, 0, 1], editor: &#123; type: color &#125; &#125;<br>
<br>
tiling0:   &#123; value: [1.0, 1.0, 0.1, 0.1] &#125;<br>
<br>
tiling1:   &#123; value: [1.0, 1.0, 0.07, 0.07] &#125;<br>
<br>
- name: transparent<br>
<br>
passes:<br>
<br>
- vert: general-vs:vert # builtin header<br>
<br>
frag: unlit-fs:frag<br>
<br>
blendState:<br>
<br>
targets:<br>
<br>
- blend: true<br>
<br>
blendSrc: src_alpha<br>
<br>
blendDst: one_minus_src_alpha<br>
<br>
blendSrcAlpha: src_alpha<br>
<br>
blendDstAlpha: one_minus_src_alpha<br>
<br>
properties: *props<br>
<br>
&#125;%<br>
<br>
将 c0，c1，tiling0，tiling1 定义到 properties 里面，原来的参数这里先不做任何删改，保留处理。<br>
<br>
给顶点着色器和片元着色器都加上 uniform 声明定义块：<br>
<br>
uniform MyVec4 &#123;<br>
<br>
vec4 c0;<br>
<br>
vec4 c1;<br>
<br>
vec4 tiling0;<br>
<br>
vec4 tiling1;<br>
<br>
&#125;;<br>
<br>
然后移除原本代码里面定义的 c0，c1，tiling0 和tiling1，用 uniform 来代替。<br>
<br>
完成后回到 Cocos Creator 中，查看材质。<br>
<br>
<div align="center">
<img aid="1029830" zoomfile="https://di.gameres.com/attachment/forum/202201/28/114623yzj1nuxuk1euk553.jpg" data-original="https://di.gameres.com/attachment/forum/202201/28/114623yzj1nuxuk1euk553.jpg" width="600" id="aimg_1029830" inpost="1" src="https://di.gameres.com/attachment/forum/202201/28/114623yzj1nuxuk1euk553.jpg" referrerpolicy="no-referrer">
</div><br>
<strong><font color="#de5650">13、成品与 Demo</font></strong><br>
<br>
最后调整一下摄像机、材质的参数，即得到成品：<br>
<br>
<div align="center">
<img aid="1029831" zoomfile="https://di.gameres.com/attachment/forum/202201/28/114624hllij6sl4jjt2o49.gif" data-original="https://di.gameres.com/attachment/forum/202201/28/114624hllij6sl4jjt2o49.gif" width="420" id="aimg_1029831" inpost="1" src="https://di.gameres.com/attachment/forum/202201/28/114624hllij6sl4jjt2o49.gif" referrerpolicy="no-referrer">
</div><br>
最终完整的 effect 文件内容这里不再赘述，大家可以点击文末【阅读原文】移步论坛专贴查看完整内容、下载 Demo 工程，欢迎一起讨论交流！<br>
<br>
Demo 工程&论坛讨论帖：<br>
<br>
https://forum.cocos.org/t/topic/128595<br>
<br>
<font size="2"></font><br>
<font size="2">来源：COCOS</font><br>
<font size="2">原文：https://mp.weixin.qq.com/s/bzfFXRzoT5_LmuhDxofGMQ</font><br>
<br>
<br>
  
</div>
            