
---
title: 'Cocos 实用渲染实战（一）：高性价比的人物皮肤渲染'
categories: 
 - 游戏
 - GameRes 游资网
 - 热点推荐
headimg: 'https://di.gameres.com/attachment/forum/202110/14/143048v305r25t5t3555fi.gif'
author: GameRes 游资网
comments: false
date: Thu, 14 Oct 2021 00:00:00 GMT
thumbnail: 'https://di.gameres.com/attachment/forum/202110/14/143048v305r25t5t3555fi.gif'
---

<div>   
<table cellspacing="0" cellpadding="0"><tbody><tr><td class="t_f" id="postmessage_2516679">
无论何等类型或规模，人物渲染都是项目中难以替代的重要组成部分。<br><br>
有趣的是，对比世间万物，我们理应对自己的身体更加熟悉，然而远自文艺复兴以来，无论在美术层面还是技术层面，人物渲染一直是一个令人挠头的痒点——即便是从真人模特身上以尖端仪器扫描，并赋予极高贴图精度的加持下，我们依然时常难以摆脱“恐怖谷”的困扰。<br><br>
那么，有什么“奇技淫巧”，能够让我们在 Cocos Creator 中更容易地产出可信的人物渲染效果呢？Cocos 布道师葡萄干将从皮肤、头发、眼睛三个方面，同大家分享一套 Cocos 「次世代」人物渲染方案。<br><br><div align="center">
<img id="aimg_1014710" aid="1014710" zoomfile="https://di.gameres.com/attachment/forum/202110/14/143048v305r25t5t3555fi.gif" data-original="https://di.gameres.com/attachment/forum/202110/14/143048v305r25t5t3555fi.gif" width="550" inpost="1" src="https://di.gameres.com/attachment/forum/202110/14/143048v305r25t5t3555fi.gif" referrerpolicy="no-referrer">
</div>
<br>
今天先从皮肤说起。<br><br><strong><font color="#de5650">确立目标</font></strong><br><br>
我们将在 Cocos Effect 中编写一个次表面散射着色器，用于表现人物渲染中的皮肤材质效果。Cocos Creator 已经自带了标准 Metal/Roughness 流程的 PBR 着色器，我们将在此基础上增加新的 GLSL 代码，这样既可以使用所有 Metal/Roughness 流程的 PBR 功能和特性，同时也兼备次表面散射的效果呈现。<br><br>
所谓次表面散射，最直观的视觉观感是：物体内部自发光由内而外把物体照亮了，因此使用我们的着色器除了可以配合环境制作写实的次表面散射效果之外，在特定数值的配合下，还可以产生更特别、更戏剧化的效果：<br><br><div align="center">
<img id="aimg_1014711" aid="1014711" zoomfile="https://di.gameres.com/attachment/forum/202110/14/143051vaeanb3bbvab88r3.gif" data-original="https://di.gameres.com/attachment/forum/202110/14/143051vaeanb3bbvab88r3.gif" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202110/14/143051vaeanb3bbvab88r3.gif" referrerpolicy="no-referrer">
</div>
<br>
我们的着色器将配合两张新贴图 Thickness 和 Curvature 使用。这两个名词对于美术，尤其是角色美术的同学，想必是不陌生了。同时，我们会附加上菲涅尔反射的功能，在 PBR 反射算法的基础上赋予更灵活的调节选项。最后，我们会赋予一个 Diffuse Profile 功能，其细节会在后文详说。目前我们只需要知道它是一个随数值调节颜色输出的功能。<br><br>
那么，Cocos Effect 又如何使用呢？<br><br><strong><font color="#de5650">快速上手</font></strong><br><br>
Cocos Effect 是 Cocos Creator 存储着色器的一种格式，它使用 YAML 编写。Cocos Effect 将顶点着色器、片元着色器和编辑器中的参数整合在一个文件中，并且会根据目标平台不同转换为不同版本的 OpenGL ES Shader。YAML 只传输数据，它本身不包含逻辑，毕竟 YAML 的全称是“YAML Ain't a Markup Language” （YAML 不是一种标记语言），真正表达逻辑的还是 GLSL 顶点和片元着色器。<br><br>
Cocos Effect 的详细信息何以从官方文档「Effect 语法」[1]中获得，以Cocos Creator 内置的标准 PBR 着色器为例，我们可以参考以下的信息，快速开始编写自己的着色器：<br><br>
所有顶点着色器代码需要在“CCProgram standard-vs”标签下用 GLSL 编写，同时也可以使用 Cocos Creator 内置的 Shader 参数，具体的列表可以在「常用 shader 内置 Uniform」[2]获得；<br><br><div align="center">
<img id="aimg_1014712" aid="1014712" zoomfile="https://di.gameres.com/attachment/forum/202110/14/143051hy7020qn7y007a06.jpg" data-original="https://di.gameres.com/attachment/forum/202110/14/143051hy7020qn7y007a06.jpg" width="344" inpost="1" src="https://di.gameres.com/attachment/forum/202110/14/143051hy7020qn7y007a06.jpg" referrerpolicy="no-referrer">
</div>
<br>
类似的，所有的片元着色器代码需要在“CCProgram standard-fs”标签下用 GLSL 编写；<br><br><div align="center">
<img id="aimg_1014713" aid="1014713" zoomfile="https://di.gameres.com/attachment/forum/202110/14/143052ohwgc3ojqo4hc49h.jpg" data-original="https://di.gameres.com/attachment/forum/202110/14/143052ohwgc3ojqo4hc49h.jpg" width="344" inpost="1" src="https://di.gameres.com/attachment/forum/202110/14/143052ohwgc3ojqo4hc49h.jpg" referrerpolicy="no-referrer">
</div>
<br>
自定义参数需要在“properties”标签下声明，在“properties”标签下声明的变量都会在 Cocos Creator 内的编辑面板中出现；<br><br><div align="center">
<img id="aimg_1014714" aid="1014714" zoomfile="https://di.gameres.com/attachment/forum/202110/14/143052g10qxclcc0f4ddfd.jpg" data-original="https://di.gameres.com/attachment/forum/202110/14/143052g10qxclcc0f4ddfd.jpg" width="388" inpost="1" src="https://di.gameres.com/attachment/forum/202110/14/143052g10qxclcc0f4ddfd.jpg" referrerpolicy="no-referrer">
</div>
<br>
我们需要为新声明的参数声明一个相应的 uniform，这需要在“CCProgram shared-ubo”标签下实现，声明的 uniform 无论顶点着色器还是片元着色器都可以访问；<br><br><div align="center">
<img id="aimg_1014715" aid="1014715" zoomfile="https://di.gameres.com/attachment/forum/202110/14/143053q9958ys1uvy2h2gu.jpg" data-original="https://di.gameres.com/attachment/forum/202110/14/143053q9958ys1uvy2h2gu.jpg" width="388" inpost="1" src="https://di.gameres.com/attachment/forum/202110/14/143053q9958ys1uvy2h2gu.jpg" referrerpolicy="no-referrer">
</div>
<br>
我们也可以声明自定义函数，但是记得：YAML 是不包含逻辑的。所以自定义函数应该放在顶点着色器（“CCProgram standard-vs”）或者片元着色器（“CCProgram standard-fs”）之内。<br><br><strong><font color="#de5650">奠定理论</font></strong><br><br>
首先，我们需要解答一个问题：什么样的效果能够让皮肤更真实？<br><br>
我们可以从现实生活中找到一些参考：<br><br><div align="center">
<img id="aimg_1014716" aid="1014716" zoomfile="https://di.gameres.com/attachment/forum/202110/14/143054uamfrr4ao7lc5o4s.jpg" data-original="https://di.gameres.com/attachment/forum/202110/14/143054uamfrr4ao7lc5o4s.jpg" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202110/14/143054uamfrr4ao7lc5o4s.jpg" referrerpolicy="no-referrer">
</div>
<br>
观察上图，首先你可能会注意到的是：他的耳朵是红色的。而且在结构越陡峭、线条越坚硬的部分，红色显得更加浓艳。另外，在他的鼻梁明暗交界线的部分，也可以看到一条红色聚集的色带。<br><br><div align="center">
<img id="aimg_1014717" aid="1014717" zoomfile="https://di.gameres.com/attachment/forum/202110/14/143055ctbqtn7blnl7sinf.jpg" data-original="https://di.gameres.com/attachment/forum/202110/14/143055ctbqtn7blnl7sinf.jpg" width="460" inpost="1" src="https://di.gameres.com/attachment/forum/202110/14/143055ctbqtn7blnl7sinf.jpg" referrerpolicy="no-referrer">
</div>
<br>
在上图中，我们同样能够在鼻梁的明暗交界线上观察到红色的色带，她的鼻梁的线条并不是特别陡峭，因此色带似乎也比上一个例子更宽一些。<br><br><div align="center">
<img id="aimg_1014718" aid="1014718" zoomfile="https://di.gameres.com/attachment/forum/202110/14/143056s21xgirzrrie0t1x.jpg" data-original="https://di.gameres.com/attachment/forum/202110/14/143056s21xgirzrrie0t1x.jpg" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202110/14/143056s21xgirzrrie0t1x.jpg" referrerpolicy="no-referrer">
</div>
<br>
在这个例子中，我们同样可以观察到红色聚集的部分，不过在她的脸上，红色聚集在鼻翼和鼻尖的位置。<br><br><div align="center">
<img id="aimg_1014719" aid="1014719" zoomfile="https://di.gameres.com/attachment/forum/202110/14/143056i22ygekeesy43dkd.jpg" data-original="https://di.gameres.com/attachment/forum/202110/14/143056i22ygekeesy43dkd.jpg" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202110/14/143056i22ygekeesy43dkd.jpg" referrerpolicy="no-referrer">
</div>
<br>
而在这个例子当中，我们可以在他的脸颊明暗交界线的位置看到大面积的粉红色聚集（至于为什么是粉红色，是因为这张照片在后期调色中混入了冷色调的缘故）。而这种粉红色在他鼻梁线条锋利的部分同样可以看到。<br><br>
综合起来，我们似乎可以观察到一定的规律：<br><br>
人的皮肤在明暗交接线的部分，会出现红色聚集；<br><br>
红色聚集在人脸结构陡峭，线条锋利的部分，会更明显和鲜艳；<br><br>
耳朵、鼻尖、鼻翼等区域是红色聚集常见的地方。<br><br>
那么，为什么会出现这种现象？这些红色是从何而来的？<br><br><div align="center">
<img id="aimg_1014720" aid="1014720" zoomfile="https://di.gameres.com/attachment/forum/202110/14/143057dxfas0xs5p50fs30.jpg" data-original="https://di.gameres.com/attachment/forum/202110/14/143057dxfas0xs5p50fs30.jpg" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202110/14/143057dxfas0xs5p50fs30.jpg" referrerpolicy="no-referrer">
</div>
<br>
我们知道，当光线从一种介质 A 射入另一种介质 B 时，一部分光线被介质 B 吸收，另一部分在介质 B 中经过多次反射和折射，最终一部分光线从介质 B 折返重新射入介质 A 中。而这些在介质 B 中经过反复反射折射而重新回到介质 A 的光线被人眼所捕捉到，所以人眼可以观察到介质 B 的颜色。这些光线虽然原理上属于反射光线（Specular），但实际表现的是散射（Diffuse）的特质，所以被称为漫反射（Diffuse Reflectance）光线。<br><br>
你大概已经注意到：当漫反射光线经过在介质 B 中的种种流程，重新射入介质 A 时，距离原来射入介质 B 的入射点已经有了一段距离。对于绝大多数材质来说，这个距离非常微小，完全可以忽略不记，所以我们可以理解为漫反射光线是由原入射点射出的。<br><br><div align="center">
<img id="aimg_1014721" aid="1014721" zoomfile="https://di.gameres.com/attachment/forum/202110/14/143057uvfqnntfacvkcrn8.jpg" data-original="https://di.gameres.com/attachment/forum/202110/14/143057uvfqnntfacvkcrn8.jpg" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202110/14/143057uvfqnntfacvkcrn8.jpg" referrerpolicy="no-referrer">
</div>
<br>
然而对一小部分材质来说，这个距离就不能忽略了。当光线射入时，这类材质会表现一种透光的特质，仿佛物体内部自带光源，把物体从内部照亮了。自然界中有很多有机材质会表现这种特质，比如蜂蜡、树叶、果蔬等，当然也包括人的皮肤。<br><br>
这种特别的散射特质，即被称为次表面散射（Sub-surface Scattering）。<br><br><div align="center">
<img id="aimg_1014722" aid="1014722" zoomfile="https://di.gameres.com/attachment/forum/202110/14/143058ji69499l8bzd9ibd.jpg" data-original="https://di.gameres.com/attachment/forum/202110/14/143058ji69499l8bzd9ibd.jpg" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202110/14/143058ji69499l8bzd9ibd.jpg" referrerpolicy="no-referrer">
</div>
<br>
原理似乎挺简单，但我们应该如何实现呢？<br><br>
在计算机图形学的历史上，我们可以找到多种多样表现次表面散射的技巧和手法。其中一个较早的例子来自与电影《黑客帝国》（The Matrix）。特效人员发现，可以简单地对皮肤的 Diffuse 贴图做一次模糊，再叠加到原贴图上，就可以有效降低贴图的人工质感，做出光线在表皮下散射的效果。<br><br>
而对于明暗交界线上的红色堆积，你大概已经想到可以轻松利用“N·L”方法，通过光照方向和物体表面法线计算得明暗交界线的位置，再叠加以一个颜色即可。这种方法也被称为 Wrap Lighting 方法，在经典游戏《半衰期2》（Half-life 2）中广泛应用。<br><br>
而与“N·L”非常类似的“N·V”方法，可以通过摄像机方向和物体表面法线得到物体正对摄像机观察角度的部分，这可以帮助我们轻松获得菲涅尔（Fresnel）反射的效果。<br><br>
讲到这里，我们的目标已经比较明确了：<br><br>
我们需要一个模糊，用于达到 Diffuse 贴图的漫反射效果；<br><br>
我们需要一张 Thickness 贴图和一张 Curvature 贴图，帮助我们识别物体那些部位容易出现次表面散射；<br><br>
我们需要一个菲涅尔反射效果，这将帮助我们实现皮肤的 Specular 部分；<br><br>
最后，我们需要一个 Diffuse Profile，这将帮助我们确定次表面散射的强度和颜色。<br><br><strong><font color="#de5650">实现模糊效果</font></strong><br><br>
如何实现模糊的效果？其背后的逻辑其实很简单：我们只要把需要被模糊的图像的 UV 向各个方向偏移一点距离，把所有偏移的结果相加，求一个平均值即可：<br><br>
vec3 boxBlur( sampler2D diffuseMap, float blurAmt )&#123;<br><br>
vec2 uv01 = vec2(v_uv.x - blurAmt * 0.01, v_uv.y - blurAmt * 0.01);<br><br>
vec2 uv02 = vec2(v_uv.x + blurAmt * 0.01, v_uv.y - blurAmt * 0.01);<br><br>
vec2 uv03 = vec2(v_uv.x + blurAmt * 0.01, v_uv.y + blurAmt * 0.01);<br><br>
vec2 uv04 = vec2(v_uv.x - blurAmt * 0.01, v_uv.y + blurAmt * 0.01);<br><br>
vec3 blurredDiffuse = (SRGBToLinear(texture(diffuseMap, uv01).rgb) + SRGBToLinear(texture(diffuseMap, uv02).rgb) + SRGBToLinear(texture(diffuseMap, uv03).rgb) + SRGBToLinear(texture(diffuseMap, uv04).rgb)) / 4.0;<br><br>
return blurredDiffuse;<br><br>
&#125;<br><br>
在上面的示例代码中，“v_uv”是 Vertex Shader 传递的 UV 数据，我们基于 Cocos Creator 的内置 PBR 着色器编写我们的 Shader，所以有很多准备工作已经做好了，我们直接拿来用即可。“SRGBToLinear”是 Cocos Creator 内置函数，将 sRGB 空间的颜色数据转换为线性空间，在 PBR 流程当中，所有的颜色计算需要在线性空间中进行。<br><br>
当然，仅仅做一次平均值的计算，最终效果可能不是特别好。你也可以用同样的方法循环2-3次，以获得更细腻的效果：<br><br>
vec3 blurPass = vec3( 0.0, 0.0, 0.0 );<br><br>
for( float i = 1.0; i < 4.0; i++ )&#123;<br><br>
blurPass += boxBlur(diffuseMap, blurAmt * i);<br><br>
&#125;<br><br>
blurPass = blurPass / 3.0;<br><br>
这种单刀直入的模糊方式，称之为方形模糊（Box Blur），其特点就是所有像素一视同仁，被处于同样等级的模糊处理。虽然简洁明了效率高，但视觉上不一定是我们想要的。<br><br>
如果你用过 Adobe 系列的图像处理工具，你一定很熟悉最常用的模糊工具高斯模糊（Gaussian Blur）。高斯模糊的逻辑与方形模糊一脉相承，不同的是：像素偏移的距离越大，模糊的程度越高，反之则越小，而模糊程度的权重则呈正态分布排列。这样我们得到的结果中间模糊程度低，四周模糊程度高，并且呈现出一种从中间向四周自然衰减的效果。<br><br>
用代码从头实现一个正态分布函数，似乎还是太麻烦了。所幸的是，我们只需要几个呈正态分布的数值作为我们模糊的权重，直接代入我们的方形模糊函数当中即可，网上有诸多正态分布数值生成器可供挑选。<br><br>
vec3 gaussianBlur( sampler2D diffuseMap, float blurAmt ) &#123;<br><br>
float gOffset[5];<br><br>
gOffset[0] = 0.0;<br><br>
gOffset[1] = 1.0;<br><br>
gOffset[2] = 2.0;<br><br>
gOffset[3] = 3.0;<br><br>
gOffset[4] = 4.0;<br><br>
float gWeight[5];<br><br>
gWeight[0] = 0.2270270270;<br><br>
gWeight[1] = 0.1945945946;<br><br>
gWeight[2] = 0.1216216216;<br><br>
gWeight[3] = 0.0540540541;<br><br>
gWeight[4] = 0.0162162162;<br><br>
vec3 baseDiffuse = SRGBToLinear(texture(diffuseMap, v_uv).rgb);<br><br>
for( int i = 0; i < 5; i++ )&#123;<br><br>
baseDiffuse += SRGBToLinear(texture(diffuseMap, v_uv + vec2(gOffset<i> * 0.01 * blurAmt, 0.0)).rgb) * gWeight<i>;<br><br>
baseDiffuse += SRGBToLinear(texture(diffuseMap, v_uv - vec2(gOffset<i> * 0.01 * blurAmt, 0.0)).rgb) * gWeight<i>;<br><br>
baseDiffuse += SRGBToLinear(texture(diffuseMap, v_uv + vec2(0.0, gOffset<i> * 0.01 * blurAmt)).rgb) * gWeight<i>;<br><br>
baseDiffuse += SRGBToLinear(texture(diffuseMap, v_uv - vec2(0.0, gOffset<i> * 0.01 * blurAmt)).rgb) * gWeight<i>;<br><br>
&#125;<br><br>
return baseDiffuse / 5.0;<br><br>
&#125;<br><br><strong><font color="#de5650">探索 Diffuse Profile</font></strong><br><br>
让我们回到之前观察到的明暗交界线上的红色聚集上面。我们已经想到可以用“N·L”+ 颜色叠加的方法实现这种效果，但这里有一个问题：这里的红色是常量的红色吗？<br><br>
让我们来看一个实验：有一个呈现次表面散射的球体，被单一光源照射。光源的位置和强度不变，放大和缩小球体的大小，观察次表面散射颜色的变化。<br><br><div align="center">
<img id="aimg_1014723" aid="1014723" zoomfile="https://di.gameres.com/attachment/forum/202110/14/143058coaa25a80a3znao8.jpg" data-original="https://di.gameres.com/attachment/forum/202110/14/143058coaa25a80a3znao8.jpg" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202110/14/143058coaa25a80a3znao8.jpg" referrerpolicy="no-referrer">
</div>
<br>
结果略微出乎意料：在球体极大和极小的情况下，散射颜色较深，近乎于纯黑色；随着球体的缩放接近于极大和极小之间的一个范围，散射的颜色逐渐变得明亮和鲜艳，直到达到一个峰值。<br><br>
这似乎告诉我们：次表面散射的颜色变化也遵循一条钟形曲线（正态分布曲线），在某个临界点达到峰值，向两边递减。<br><br>
那么，这个临界点是由什么决定的呢？这就取决于我们如何理解实验中球体大小的变化。<br><br>
首先，在光源位置不变的情况下，球体的大小变化，意味着光线到达球体表面传播的距离变化，也就是说，光线传播的距离是因素之一。<br><br>
另外，一个半径较大的球体，可以看作其表面的曲率（Curvature）也更大，反之则更小。一个半径无限小的球体，表面的曲率也无限小，可以看作是一个平面。也就是说，物体表面的曲率，即弯曲的程度，也是因素之一。这也与我们之前在观察参考图中得到的结论相契合。<br><br>
理论很美好，但是我们如何实现呢？<br><br>
所幸的是，我们已经有基于现实观测的皮肤次表面散射数据供我们使用：<br><br><div align="center">
<img id="aimg_1014724" aid="1014724" zoomfile="https://di.gameres.com/attachment/forum/202110/14/143058ufkfqy9ru55qom52.jpg" data-original="https://di.gameres.com/attachment/forum/202110/14/143058ufkfqy9ru55qom52.jpg" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202110/14/143058ufkfqy9ru55qom52.jpg" referrerpolicy="no-referrer">
</div>
<br><div align="center">
<img id="aimg_1014725" aid="1014725" zoomfile="https://di.gameres.com/attachment/forum/202110/14/143058et6v6ov6e4nnso16.jpg" data-original="https://di.gameres.com/attachment/forum/202110/14/143058et6v6ov6e4nnso16.jpg" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202110/14/143058et6v6ov6e4nnso16.jpg" referrerpolicy="no-referrer">
</div>
<br>
这张表看上去有点不明觉厉，简单地说：我们所观察到的皮肤上的红色，其实是皮肤的不同截层以不同的颜色和强度曲线分别进行散射，再叠加而成。这张表列举了六层不同的颜色和曲线。而所有截层的散射强度都以正态分布排列，所以我们可以在右图看到自然衰减的晕染。<br><br>
既然数据已经给到我们了，我们就可以根据正态分布公式，计算出散射强度，再叠加以颜色，散射的最终输出就解决了。<br><br><div align="center">
<img id="aimg_1014726" aid="1014726" zoomfile="https://di.gameres.com/attachment/forum/202110/14/143059j2thhcfceecdhwbt.jpg" data-original="https://di.gameres.com/attachment/forum/202110/14/143059j2thhcfceecdhwbt.jpg" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202110/14/143059j2thhcfceecdhwbt.jpg" referrerpolicy="no-referrer">
</div>
<br>
上图即是正态分布（高斯分布）公式，简单地说：μ 为中位数，在我们的计算中也就是散射颜色变化的峰值，我们知道它由光线传播的距离和物体表面的曲度相关，目前可以取0；σ^2为方差，它决定了钟形曲线的陡峭程度，这个数值已经为我们提供了。由此，我们可以直接带入公式：<br><br>
#define M_PI 3.1415926535897932384626433832795<br><br>
vec3 Profile( float dis )&#123;<br><br>
return  vec3(0.233, 0.455, 0.649) * 1.0 / (abs(sqrt(0.0064)) * abs(sqrt(2.0 * M_PI))) * exp(-dis * dis / (2.0 * 0.0064)) +<br><br>
vec3(0.1, 0.366, 0.344) * 1.0 / (abs(sqrt(0.0484)) * abs(sqrt(2.0 * M_PI))) * exp(-dis * dis / (2.0 * 0.0484)) +<br><br>
vec3(0.118, 0.198, 0.0) * 1.0 / (abs(sqrt(0.187)) * abs(sqrt(2.0 * M_PI))) * exp(-dis * dis / (2.0 * 0.187)) +<br><br>
vec3(0.113, 0.007, 0.007) * 1.0 / (abs(sqrt(0.567)) * abs(sqrt(2.0 * M_PI))) * exp(-dis * dis / (2.0 * 0.567)) +<br><br>
vec3(0.358, 0.004, 0.0) * 1.0 / (abs(sqrt(1.99)) * abs(sqrt(2.0 * M_PI))) * exp(-dis * dis / (2.0 * 1.99)) +<br><br>
vec3(0.078, 0.0, 0.0) * 1.0 / (abs(sqrt(7.41)) * abs(sqrt(2.0 * M_PI))) * exp(-dis * dis / (2.0 * 7.41));<br><br>
&#125;<br><br>
到目前为止，我们已经得到了实现 Diffuse 散射效果的模糊，得到了解决次表面散射颜色和强度的 Diffuse Profile，现在的问题是：次表面散射应该出现在哪里？<br><br>
在这里我们需要引入两张贴图：Thickness 和 Curvature。Thickness 通过以法线反方向发射射线的方式计算物体的厚度，Curvature 表现的是物体表面的曲率。这两张图，我们无需考虑如何在引擎中计算和生成，因为我们可以在第三方软件，比如 Substance Painter 中离线渲染他们。<br><br><div align="center">
<img id="aimg_1014727" aid="1014727" zoomfile="https://di.gameres.com/attachment/forum/202110/14/143059a2ig585im8rvp8rv.jpg" data-original="https://di.gameres.com/attachment/forum/202110/14/143059a2ig585im8rvp8rv.jpg" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202110/14/143059a2ig585im8rvp8rv.jpg" referrerpolicy="no-referrer">
</div>
<br>
获得烘焙完成的贴图之后，我们把 Curvature 放在一边，先处理 Thickness。<br><br>
vec4 bDepth = gaussianBlur(thicknessMap, 0.0);<br><br>
float deltaDepth = abs(SRGBToLinear(texture(thicknessMap, v_uv).rgb).x - bDepth.x);<br><br>
我们先用之前的高斯模糊处理 Thickness，再用原贴图减去被模糊后的 Thickness 贴图。回忆一下高斯模糊的原理，我们得到的结果是：模糊后偏离较小的像素被减去了，留下的是偏离较大的像素。这些Δ值可以作为我们次表面散射的遮罩。<br><br>
我们仍缺的一环是菲涅尔反射。如上所述，我们可以使用“N·V”方法实现这一效果。<br><br>
vec4 v_normal_cam = normalize(cc_matView * vec4(v_normal, 0.0));<br><br>
float NVdot = dot(vec3(0.0, 0.0, 1.0), normalize(v_normal_cam).xyz);<br><br>
在上面的示例代码中，“cc_matView”是Cocos Creator自带参数，返回的是试图矩阵。“v_normal”是从 Vertex Shader 传递的法线数据。<br><br>
所有组件已经基本就绪了，下面是让他们联动起来的环节。<br><br><strong><font color="#de5650">完成 Shader</font></strong><br><br>
漫反射效果，用我们的模糊处理一下 Diffuse 贴图，叠加到 Albedo 通道即可。<br><br>
vec4 bDiffuse = gaussianBlur(diffuseMap, blurAmt);<br><br>
s.albedo += bDiffuse;<br><br>
菲涅尔反射的效果，用我们“N·V”计算得出的权重，乘以一个自定义参数，叠加到 roughness 通道即可。<br><br>
pbr.y += NVdot * roughnessGain;<br><br>
s.roughness = clamp(pbr.y, 0.04, 1.0);<br><br>
漫反射的颜色，我们已经得到了 Diffuse Profile 的函数，问题是：用什么参数带入这个函数？<br><br>
我们已经知道光线传播的距离和物体表面的曲率是影响次表面散射的因素。光传播的距离似乎比较难把控，但我们至少知道物体本身的前后关系也算在光传播的距离当中，因此代入顶点位置数据（v_position）是顺理成章的。<br><br>
至于物体表面的曲率，我们并不知道曲率与次表面散射的直接数值关系，但我们通过观察实验得知：曲率与次表面散射强度大致呈线性关系，因此我们姑且把曲率（由 Curvature 贴图提供）当作一般的数值权重，再辅以我们自定义的权重加以调节。<br><br>
除了 Diffuse Profile 的输出之外，我们还可以利用 Cocos Creator 内置的 cc_mainLitColor 参数，在散射中加入光源颜色和强度的影响。<br><br>
最后，在颜色输出上再叠加上物体自身的 Diffuse 颜色，就基本确立了次表面散射的颜色和强度。<br><br>
vec3 curvatureMap = SRGBToLinear(texture(curvatureMap, v_uv).rgb);<br><br>
vec3 sssColor = Profile(length(v_position) * curvatureMap.x) *<br><br>
cc_mainLitColor.rgb *<br><br>
cc_mainLitColor.w *<br><br>
s.albedo.rgb;<br><br>
然而，问题又出现了：次表面散射该从哪个通道输出？<br><br>
Cocos Creator 遵循标准 PBR 的 Metal/Roughness 流程，因而默认 Pipeline 中并没有 Translucency 通道，但这并不会对我们造成太大影响：我们可以利用 Emissive 通道达到相同的效果。<br><br>
下一个问题是：次表面散射应该在哪里出现？<br><br>
我们知道次表面散射的成因是入射光线在物体内部反射和折射而产生内部发光现象，所以我们的第一步是计算“N·L”，利用我们已得到的 Thickness Δ值，我们可以得到一个明面为0，暗面为 Thickness 的遮罩。这也符合次表面散射的原理：光线从明面射入，所以我们可以从暗面观察到次表面散射现象。<br><br>
最后，利用遮罩将次表面散射颜色叠加到暗面上，我们的效果就已经出来了。<br><br>
float sssMask = mix(deltaDepth, 0.0, NLdot);<br><br>
vec3 sssGain = mix(vec3(0.0, 0.0, 0.0), sssColor, sssMask);<br><br>
s.emissive += sssGain;<br><br>
次表面散射确实是一个经久不衰的话题。毫无疑问，我们今天的成果还有许多可以纠正、改进和继续发掘的地方。希望你读到这里，已经激发了一些奇思妙想，开始动手制作属于自己的 Cocos Creator 着色器了。<br><br>
下一章，我们将看看如何在 Cocos Creator 中渲染出逼真的人物头发。<br><br><font size="2"></font><br><font size="2">来源：COCOS</font><br><font size="2">原文：https://mp.weixin.qq.com/s/WniBIH5QN4PXKJYOYoajPw</font><br><br><br></i></i></i></i></i></i></i></i>
</td></tr></tbody></table>


  
</div>
            