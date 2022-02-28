
---
title: 'Cocos Creator 实时渲染的超写实汽车！堪比真车的车漆材质表现'
categories: 
 - 游戏
 - GameRes 游资网
 - 热点推荐
headimg: 'https://di.gameres.com/attachment/forum/202202/21/110738kew9psbnieealrli.jpg'
author: GameRes 游资网
comments: false
date: Mon, 21 Feb 2022 00:00:00 GMT
thumbnail: 'https://di.gameres.com/attachment/forum/202202/21/110738kew9psbnieealrli.jpg'
---

<div>   
<div align="center">
<img aid="1031296" zoomfile="https://di.gameres.com/attachment/forum/202202/21/110738kew9psbnieealrli.jpg" data-original="https://di.gameres.com/attachment/forum/202202/21/110738kew9psbnieealrli.jpg" width="600" id="aimg_1031296" inpost="1" src="https://di.gameres.com/attachment/forum/202202/21/110738kew9psbnieealrli.jpg" referrerpolicy="no-referrer">
</div><br>
如今，许多曾经应用在游戏开发中的技术开始愈发频繁地在工业和商业领域出现。无论是在建筑、医疗、工业制造等高技术密度的行业，还是在零售、导航、人机互动等与普罗大众人间烟火息息相关的领域，即时渲染技术都在快速普及化。<br>
<br>
汽车行业毫无疑问是游戏技术商业化的先驱者之一，大至模拟真实驾驶体验的 3A 游戏大作，小至一个手机即开即用的 HTML5 展示，即时渲染总是能够给汽车带来各式各样的新鲜感。那么，在「万物皆可元宇宙」的现在，我们如何在 Cocos Creator 中，制作一个漂亮的 3D 汽车渲染呢？<br>
<br>
无论是用于游戏还是工业或商业用途，汽车渲染所需的美术资源与其他物件都没有本质的区别，我们可以：<br>
<br>
使用硬表面建模技术，还原各种车辆的结构形态；<br>
<br>
利用 PBR 渲染工作流程，表现汽车的金属、皮革、玻璃等材质效果；<br>
<br>
使用法线贴图，将精细的结构和材质细节还原在多边形数量较小的模型上，在不损失视觉展现的前提下让更多的受众无障碍获得相同的体验。<br>
<br>
然而，要达到令人满意的汽车渲染效果，首当其冲的是车漆效果的表现。本次我们将分析车漆的结构、类型等，在 Cocos Creator 3.4 中实现写实风格的车漆表现（Demo 请点击文末【阅读原文】下载）。<br>
<br>
<strong><font color="#de5650">车漆的结构</font></strong><br>
<br>
<div align="center">
<img aid="1031297" zoomfile="https://di.gameres.com/attachment/forum/202202/21/110739vyxfz7pckddo9czp.jpg" data-original="https://di.gameres.com/attachment/forum/202202/21/110739vyxfz7pckddo9czp.jpg" width="600" id="aimg_1031297" inpost="1" src="https://di.gameres.com/attachment/forum/202202/21/110739vyxfz7pckddo9czp.jpg" referrerpolicy="no-referrer">
</div><br>
传统的车漆一般分为电泳（Electrocoat）、中涂（Primer）、色漆（Basecoat）和清漆（Clearcoat）四层。<br>
<br>
电泳和中涂的作用主要是保护车身免受外界化学和紫外线侵蚀，它们位于色漆下层，被色漆层完全遮盖，因此我们不需要考虑它们在渲染中的效果。<br>
<br>
色漆是主要表现车漆颜色和质感的部分。<br>
<br>
清漆无色透明，位于色漆上层，包裹着色漆。<br>
<br>
<div align="center">
<img aid="1031298" zoomfile="https://di.gameres.com/attachment/forum/202202/21/110739yhgkzqnxgo7ztc00.jpg" data-original="https://di.gameres.com/attachment/forum/202202/21/110739yhgkzqnxgo7ztc00.jpg" width="600" id="aimg_1031298" inpost="1" src="https://di.gameres.com/attachment/forum/202202/21/110739yhgkzqnxgo7ztc00.jpg" referrerpolicy="no-referrer">
</div><br>
色漆分为不同的材质和种类，有不同的颜色和高光表现。我们可以看到，在没有喷涂清漆，色漆暴露在外的境况下，车漆的表现完全由色漆层决定，我们只需要使用 PBR 流程表现色漆的颜色、高光、金属度即可。这与其他普通材质的表现方法并无差别。<br>
<br>
<div align="center">
<img aid="1031299" zoomfile="https://di.gameres.com/attachment/forum/202202/21/110739fww1qqa1twz1tqad.jpg" data-original="https://di.gameres.com/attachment/forum/202202/21/110739fww1qqa1twz1tqad.jpg" width="600" id="aimg_1031299" inpost="1" src="https://di.gameres.com/attachment/forum/202202/21/110739fww1qqa1twz1tqad.jpg" referrerpolicy="no-referrer">
</div><br>
当喷涂上清漆层后，车漆的整体表现就不同了：清漆层无色透明，表面经过抛光非常光滑，因此在车身上出现了强烈的反射，同时又保持色漆层的颜色。<br>
<br>
<div align="center">
<img aid="1031300" zoomfile="https://di.gameres.com/attachment/forum/202202/21/110739jcojcjjvvdvdj4nw.jpg" data-original="https://di.gameres.com/attachment/forum/202202/21/110739jcojcjjvvdvdj4nw.jpg" width="600" id="aimg_1031300" inpost="1" src="https://di.gameres.com/attachment/forum/202202/21/110739jcojcjjvvdvdj4nw.jpg" referrerpolicy="no-referrer">
</div><br>
不仅如此，当我们靠近观察的时候，会发现车身上出现了细微的凹凸不平的条纹。这是油漆在干燥的过程中自然会出现的现象，称为橘皮纹。橘皮纹会在清漆层出现，是因为油漆层越厚越容易出现橘皮纹。而色漆层是车漆结构中最薄的一层，通常不会出现橘皮纹。<br>
<br>
了解了车漆的结构，我们已经有了大概的思路：我们需要在一个标准的 PBR 材质层上面，再制作一层有较强烈的反射效果，同时又有细微的条纹结构的材质。这层清漆材质独立于底层的色漆材质，并且无论底层的色漆材质如何表现都会一直存在。<br>
<br>
既然车漆的主要效果由色漆层决定，那么我们如何表现色漆层呢？<br>
<br>
<strong><font color="#de5650">色漆的分类</font></strong><br>
<br>
<div align="center">
<img aid="1031301" zoomfile="https://di.gameres.com/attachment/forum/202202/21/110740k8tam2e280dxye6m.jpg" data-original="https://di.gameres.com/attachment/forum/202202/21/110740k8tam2e280dxye6m.jpg" width="600" id="aimg_1031301" inpost="1" src="https://di.gameres.com/attachment/forum/202202/21/110740k8tam2e280dxye6m.jpg" referrerpolicy="no-referrer">
</div><br>
我们常见的色漆有三种类型：普通漆（Solid，又称素色漆、非金属漆）、金属漆（Metallic）和珠光漆（Pearlescent，又称云母漆）。<br>
<br>
普通漆的效果，与我们熟悉的非金属材质基本一致：高光的颜色一致，固有色颜色鲜明。<br>
<br>
金属漆与我们熟悉的金属材质也很类似，固有色较暗，高光有溢出的颜色。不仅如此，由于金属漆在制作的过程中，会掺入细小的金属颗粒，因此当我们靠近观察时，可以在金属漆上看到密集的金属点，在高光的区域尤其明显。<br>
<br>
珠光漆最大的特点是有次表面散射造成的颜色变化，并且它的高光也更柔和，和金属漆类似，它也有密集的金属点。<br>
<br>
无论是普通漆、金属漆还是珠光漆，我们都能在参考图中看到较为强烈的反射，这当然是色漆层上面的清漆层造成的。除此之外，在 PBR 流程中，金属度较高时固有色的明度会降低，金属漆也有同样的特性，无法表现非常鲜亮的颜色。因此在现实生活中，黑、白、黄、红四种颜色的色漆，通常是普通漆。<br>
<br>
那么，我们制作色漆的思路也有了：标准的 PBR 流程基本能满足制作色漆的要求，在此基础上，我们需要叠加一层法线效果，这将帮助我们表现金属漆的金属颗粒感。<br>
<br>
除了这三种最常见的类型之外，色漆的类型中还包括像珠光漆一样圆润，但有更鲜明的颜色和高光的糖果漆（Candy），颜色变化非常丰富的变色龙漆（Chameleon），高光非常微弱的哑光漆（Matte）等。这些效果都可以通过 PBR 参数的调节，或者一些简单的技巧（如使用 N ? V 调节 UV，用一张渐变贴图作为 albedo 等）来实现，就不多赘述了。<br>
<br>
<strong><font color="#de5650">着色器的准备工作</font></strong><br>
<br>
首先，我们需要在顶点着色器中把我们需要的顶点数据处理好：<br>
<br>
out vec3 v_normal;<br>
<br>
out vec3 v_tangent;<br>
<br>
out vec3 v_bitangent;<br>
<br>
out vec4 viewWorld;<br>
<br>
out vec4 p_position;<br>
<br>
v_normal = normalize((matWorldIT * vec4(In.normal, 0.0)).xyz);<br>
<br>
v_tangent = normalize((matWorld * vec4(In.tangent.xyz, 0.0)).xyz);<br>
<br>
v_bitangent = cross(v_normal, v_tangent) * In.tangent.w;<br>
<br>
viewWorld = normalize(cc_cameraPos - (matWorld * In.position));<br>
<br>
我们需要顶点着色器传递的数据包括顶点法线、顶点切线、顶点双切线和世界空间的观察向量。其中顶点法线和顶点切线可以直接从输入的模型获取，顶点双切线可以通过顶点法线和顶点切线的叉积计算得出，世界空间的观察向量可以使用返回摄像机世界空间位置的内置参数 cc_cameraPos 和世界空间的顶点位置计算得出。<br>
<br>
除此之外，既然我们需要进行法线功能的实现，也需要创建一个 3×3 矩阵：<br>
<br>
out mat3 matTBN;<br>
<br>
matTBN = mat3(normalize(v_tangent), normalize(v_bitangent), normalize(v_normal));<br>
<br>
我们在「真实人物渲染：头发篇」中已经聊到过切线空间的概念，把顶点法线的方向看作 Z 轴的正方向，由此建立的坐标系空间即是切线空间，它可以用于表达物体表面垂直方向不同的空间位置。而与顶点法线垂直的两个向量（切线和双切线）我们已经获得了，因此直接使用它们创建一个新的矩阵即可。这个切线空间转换矩阵，又称之为 TBN 矩阵。<br>
<br>
下面我们可以在片元着色器中着手实现效果了。<br>
<br>
<strong><font color="#de5650">色漆层的实现</font></strong><br>
<br>
既然反射是我们制作的一个重点效果，我们可以先从一个菲涅尔反射效果入手：<br>
<br>
in vec3 v_normal;<br>
<br>
in vec3 v_tangent;<br>
<br>
in vec3 v_bitangent;<br>
<br>
in vec4 viewWorld;<br>
<br>
in vec4 p_position;<br>
<br>
in mat3 matTBN;<br>
<br>
float NdotV = dot(normalize(v_normal), normalize(viewWorld.xyz));<br>
<br>
float baseMask = mix(0.0, 1.0, 1.0 - fresnelScale * pow(clamp(1.0 - NdotV, 0.0, 1.0), fresnelHard));<br>
<br>
vec4 baseBlend = mix(secondPaintColor, s.albedo, baseMask);<br>
<br>
s.albedo = baseBlend;<br>
<br>
菲涅尔当然缺不了我们已经非常熟悉的 N ? V，我们在 N ? V 的基础上分别用自定义参数做一次乘积（fresnelScale）和指数幂（fresnelHard）计算，这将分别让我们通过自定义参数调节菲涅尔的强度和范围硬度，这与我们在「头发篇」中聊到的 Specular 的实现逻辑是一样的。随后，我们再声明一个自定义颜色参数，使用菲涅尔计算的结果与固有色进行混合，这将帮助我们实现珠光漆的颜色变化效果。<br>
<br>
<div align="center">
<img aid="1031302" zoomfile="https://di.gameres.com/attachment/forum/202202/21/110740ldo2a9o3b8oogjg5.jpg" data-original="https://di.gameres.com/attachment/forum/202202/21/110740ldo2a9o3b8oogjg5.jpg" width="600" id="aimg_1031302" inpost="1" src="https://di.gameres.com/attachment/forum/202202/21/110740ldo2a9o3b8oogjg5.jpg" referrerpolicy="no-referrer">
</div><br>
下一步我们将使用一张法线实现色漆层的金属颗粒效果：<br>
<br>
vec2 flakeUV = v_uv * flakeTiling.xy + flakeTiling.zw;<br>
<br>
vec4 flakeMask = texture(flakeMask, flakeUV);<br>
<br>
vec4 flakeNormal = texture(flakeNormal, flakeUV);<br>
<br>
首先是贴图的基本操作，我们声明一个 vec4（flakeTiling）利用它的四个 float 实现 UV 的缩放和偏转，再利用这套 UV 投射两张贴图。这两张贴图，一张是金属颗粒的法线贴图，一张是与之相应的灰度图，灰度图的主要作用是为我们提供一个深度的遮罩，制作颗粒纵深的效果。<br>
<br>
<div align="center">
<img aid="1031303" zoomfile="https://di.gameres.com/attachment/forum/202202/21/110740ra6zkkqqc8oaqq88.jpg" data-original="https://di.gameres.com/attachment/forum/202202/21/110740ra6zkkqqc8oaqq88.jpg" width="512" id="aimg_1031303" inpost="1" src="https://di.gameres.com/attachment/forum/202202/21/110740ra6zkkqqc8oaqq88.jpg" referrerpolicy="no-referrer">
</div><br>
下面我们就可以将法线混合了：<br>
<br>
flakeNormal = flakeNormal * 2.0 - 1.0;<br>
<br>
vec3 fn = vec3( flakeNormal.x * flakeMask.r * flakeNormalScale,<br>
<br>
flakeNormal.y * flakeMask.r * flakeNormalScale,<br>
<br>
flakeNormal.z );<br>
<br>
vec3 flake = matTBN * normalize(fn);<br>
<br>
s.normal = normalize(vec3(s.normal.rg + flake.rg, s.normal.b * flake.b));<br>
<br>
图片当然不能存储负的数值，而法线需要能够表达负的数值，因此我们的第一步是把图片中像素点的数值归一化：从 [0, 1] 的区间，转换到 [-1, 1] 的区间。我们需要使用自定义参数对法线的表达进行控制，因此我们可以把法线贴图的数据依据维度打散，分别乘以用灰度图表达的深度遮罩和我们自定义的强度参数（flakeNormalScale），再重新组合成新的向量。使用我们准备好的 TBN 矩阵，即可将法线贴图中切线空间的数据转换为世界空间的数据。最后，将转换后的金属颗粒数据叠加到标准 PBR 材质的法线通道上。<br>
<br>
<div align="center">
<img aid="1031304" zoomfile="https://di.gameres.com/attachment/forum/202202/21/110740qbvqvvtopdb1zvvc.jpg" data-original="https://di.gameres.com/attachment/forum/202202/21/110740qbvqvvtopdb1zvvc.jpg" width="600" id="aimg_1031304" inpost="1" src="https://di.gameres.com/attachment/forum/202202/21/110740qbvqvvtopdb1zvvc.jpg" referrerpolicy="no-referrer">
</div><br>
<strong><font color="#de5650">清漆层的实现</font></strong><br>
<br>
下面我们可以处理清漆层了。首先如法炮制，使用一张法线贴图制作清漆层的橘皮效果：<br>
<br>
vec2 coatUV = v_uv * coatTiling.xy + coatTiling.zw;<br>
<br>
vec3 coatNormal = texture(coatNormal, coatUV).xyz;<br>
<br>
coatNormal = coatNormal * 2.0 - 1.0;<br>
<br>
vec3 cn = vec3( coatNormal.x * coatNormalScale,<br>
<br>
coatNormal.y * coatNormalScale,<br>
<br>
coatNormal.z );<br>
<br>
vec3 coat = matTBN * normalize(cn);<br>
<br>
s.normal = normalize(vec3(s.normal.rg + coat.rg, s.normal.b * coat.b));<br>
<br>
对于清漆层来说，最重要的是鲜明的反射效果。需要说明的是，我们的目标并不是制作一个能够忠实还原外部一切变化的反射效果。因为在目前的即时渲染领域中，除了光线追踪之外的绝大多数反射的实现手段都要求以某种形式将反射中的场景按照一般的渲染流程先构建出来。比如一个有镜面反射地板的房间，要实现地板中房间的倒影，就需要把房间里所有能在倒影中看见的物件全部单独渲染一遍，这毫无疑问会造成渲染压力的成倍增加。况且，车漆上的反射是一种视觉效果，我们并不需要它像镜子一样执行忠实反馈外部变化的功能。所以，我们只需要用一张环境的全景 HDR 贴图，叠加在片元输出上，就可以达到环境倒映在材质上的效果。<br>
<br>
全景贴图的投射方式与一般贴图并不一样，那么问题是，我们需要为全景贴图提供怎样的 UV 呢？<br>
<br>
uniform samplerCube reflEnvMap;<br>
<br>
vec3 worldRefl = reflect(normalize(-viewWorld.xyz), normalize(v_normal));<br>
<br>
vec3 reflUV = normalize(worldRefl);<br>
<br>
vec4 reflMap = texture(reflEnvMap, reflUV, s.roughness);<br>
<br>
首先我们声明一个 samplerCube 类别的 uniform，它与我们日常使用的 sampler2D 没有本质的区别，不同的是使用了全景贴图的采样器。我们可以使用 OpenGL 的 reflect 函数，获得反射光线的向量。reflect 函数要求两个参数：入射光线的向量和法线向量。我们的目的是看见反射的镜像，因此入射光线即观察向量的负向量。<br>
<br>
有了反射向量，我们就可以绘制全景贴图了。在 Cocos Creator 中，texture 函数接口对应的是 OpenGL 中 texture2D 和 textureCube 两个函数，因此在绘制一般的贴图时，调用 texture 函数，输入 sampler2D 和 UV 两个参数即可，而绘制全景贴图时，同样调用 texture 函数，输入 samplerCube、UV 和一个 float 参数即可，这个 float 参数控制 OpenGL 为全景贴图设计的一个简单模糊效果，因此我们直接把 PBR 管线中的 roughness 值赋予它。最后需要注意的是，绘制全景贴图需要的 UV 不是 vec2，而是 vec3，因此我们直接使用求得的反射向量即可。<br>
<br>
<div align="center">
<img aid="1031305" zoomfile="https://di.gameres.com/attachment/forum/202202/21/110740jv88sz3s8qvnzp3w.jpg" data-original="https://di.gameres.com/attachment/forum/202202/21/110740jv88sz3s8qvnzp3w.jpg" width="600" id="aimg_1031305" inpost="1" src="https://di.gameres.com/attachment/forum/202202/21/110740jv88sz3s8qvnzp3w.jpg" referrerpolicy="no-referrer">
</div><br>
然而，我们的反射效果并不是非常理想，反射的图像似乎颜色并不正确，这是因为全景贴图是以 RGBE 的格式以线性颜色空间存储的。在引擎中使用时，我们需要将它先转换为 RGB 格式的颜色数据。我们可以参考 Cocos Creator 中内置的 unpackRGBE 函数，用如下算法进行转换：<br>
<br>
vec4 reflMap = texture(reflEnvMap, reflUV, s.roughness);<br>
<br>
vec4 reflRGB = (reflMap * pow(1.1, reflMap.a * 255.0 - 128.0) * 5.0; //See unpack.chunk<br>
<br>
现在我们的反射环境贴图看上去正常了，然而车漆上的反射并不只有来自环境中的颜色，车漆本身的颜色同样会有影响。我们可以创建一个自定义参数（reflEnvMapScale），用它表达车漆在自身固有色和白色（相当于数值 1.0）之间的权重，再将加权后的结果乘以反射环境贴图的颜色。当权重较高时，加权的结果接近于 1.0，相当于 100% 输出环境贴图的颜色；相应的在权重较低时，输出的是环境贴图颜色与固有色相乘之后的颜色：<br>
<br>
vec3 reflShift = mix(s.albedo, vec3(1.0, 1.0, 1.0), reflEnvMapScale);<br>
<br>
vec4 reflColor = reflRGB * vec4(reflShift, 0.0);<br>
<br>
最后，使用我们之前求得的 N ? V 计算菲涅尔反射的范围，再依据菲涅尔的范围对固有色和反射颜色进行混合，车身的高反光效果就出来了：<br>
<br>
float reflMask = mix(0.0, 1.0, (reflScale * pow((1.0 - NdotV), reflHard));<br>
<br>
vec4 coatRef = mix(s.albedo, reflColor, reflMask);<br>
<br>
s.albedo = coatRef;<br>
<br>
<div align="center">
<img aid="1031306" zoomfile="https://di.gameres.com/attachment/forum/202202/21/110741vzcc9z09rcxocev2.jpg" data-original="https://di.gameres.com/attachment/forum/202202/21/110741vzcc9z09rcxocev2.jpg" width="600" id="aimg_1031306" inpost="1" src="https://di.gameres.com/attachment/forum/202202/21/110741vzcc9z09rcxocev2.jpg" referrerpolicy="no-referrer">
</div><br>
做到这里，我们对现实中车漆效果的还原就基本完毕了。然而从项目执行的角度考虑，我们仍然有一个问题需要稍加注意。<br>
<br>
<strong><font color="#de5650">一些关于美术的思考</font></strong><br>
<br>
<div align="center">
<img aid="1031307" zoomfile="https://di.gameres.com/attachment/forum/202202/21/110741hlhw5mahhtcim1at.jpg" data-original="https://di.gameres.com/attachment/forum/202202/21/110741hlhw5mahhtcim1at.jpg" width="600" id="aimg_1031307" inpost="1" src="https://di.gameres.com/attachment/forum/202202/21/110741hlhw5mahhtcim1at.jpg" referrerpolicy="no-referrer">
</div><br>
我们在日常生活中经常能看到各种产品的商业广告，在这些产品的照片或渲染当中，经常能够观察到一种边缘锋利，范围较大的白色高亮，无论是电子消费品、汽车，还是快消品的各种塑料包装，都能看到这种效果的呈现，即便从这些广告渲染中的环境来看根本找不到这些高亮的来源。<br>
<br>
这些高亮是从何而来的呢？商业光照中的照片通常是专业的摄影工作室中拍摄的，在拍摄的过程中需要使用多个灯箱和反光伞对照片上的光照进行精确的把控，而灯箱和反光伞的反射镜像恰好是边缘锋利的白色几何图形，所以在反射强度较高的材质上，这些白色高亮就频繁出现了。<br>
<br>
<div align="center">
<img aid="1031308" zoomfile="https://di.gameres.com/attachment/forum/202202/21/110741fxm08tp67rfhtvd9.jpg" data-original="https://di.gameres.com/attachment/forum/202202/21/110741fxm08tp67rfhtvd9.jpg" width="600" id="aimg_1031308" inpost="1" src="https://di.gameres.com/attachment/forum/202202/21/110741fxm08tp67rfhtvd9.jpg" referrerpolicy="no-referrer">
</div><br>
在商用的计算机渲染当中，也追求同样的效果。目前主流的各种 DCC 和插件都推出了模拟灯箱和反光伞在现实摄影棚的效果，通过生成和输出 HDR 贴图，精确控制白色高亮的位置、范围和整体形态的功能，比如 Blender 的 HDRI Maker、Cinema 4D 的 HDRI Pro Studio 等。<br>
<br>
在即时渲染中，我们不会把模型固定在一个摄影机角度进行展示，因此也通常不会精确地控制这些白色高亮在画面中的呈现。但是我们在上面着色器编写的过程中，已经实现了用 HDR 贴图制作反射效果的功能。同理，我们可以使用这些专门生产 HDR 贴图的 DCC，生成一张模拟摄影工作室光照效果的 HDR 贴图，并使用在我们的即时渲染模型上。这种工作流使我们能够在即时渲染的环境里，也能够达到商业渲染追求的效果。或者，我们也可以借鉴这种方法，为我们的游戏增色——即便我们在环境里根本没有制作灯箱和反光伞。<br>
<br>
<div align="center">
<img aid="1031309" zoomfile="https://di.gameres.com/attachment/forum/202202/21/110741vnrx82riz68o2zjw.jpg" data-original="https://di.gameres.com/attachment/forum/202202/21/110741vnrx82riz68o2zjw.jpg" width="600" id="aimg_1031309" inpost="1" src="https://di.gameres.com/attachment/forum/202202/21/110741vnrx82riz68o2zjw.jpg" referrerpolicy="no-referrer">
</div><br>
增加了白色高亮之后，汽车是不是显得更加「高级」了呢？<br>
<br>
<font size="2"></font><br>
<font size="2">来源：COCOS</font><br>
<font size="2">原文：https://mp.weixin.qq.com/s/WauJTMcXD85R3IXEL5Vv9w</font><br>
<br>
<br>
  
</div>
            