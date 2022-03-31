
---
title: '再加亿点点细节！Cocos 基于平面着色的 3D 水面渲染方案'
categories: 
 - 游戏
 - GameRes 游资网
 - 列表
headimg: 'https://di.gameres.com/attachment/forum/202203/28/111924obcac71i561zkiyy.jpg'
author: GameRes 游资网
comments: false
date: Mon, 28 Mar 2022 00:00:00 GMT
thumbnail: 'https://di.gameres.com/attachment/forum/202203/28/111924obcac71i561zkiyy.jpg'
---

<div>   
<div align="center"><img aid="1034904" zoomfile="https://di.gameres.com/attachment/forum/202203/28/111924obcac71i561zkiyy.jpg" data-original="https://di.gameres.com/attachment/forum/202203/28/111924obcac71i561zkiyy.jpg" width="600" id="aimg_1034904" inpost="1" src="https://di.gameres.com/attachment/forum/202203/28/111924obcac71i561zkiyy.jpg" referrerpolicy="no-referrer">
</div><br>
<br>
但该项目基于 Cocos Creator 延迟渲染管线，对项目和设备要求较高，所以麒麟子专门准备了这个独立的水面效果分享，希望能够对大家有所帮助。<br>
<br>
<strong><font color="#de5650">二、水面渲染流程</font></strong><br>
<br>
水面渲染技术非常多，不同段位的产品，对水面的要求不同。<br>
<br>
毛星云的《真实感水体渲染技术总结》这篇文章中，通过对一些 3A 大作的水面渲染进行分析，列出了非常多的技术要点，有兴趣的朋友可以拜读。<br>
<br>
水面渲染技术从简单到复杂来排序，可以分为以下三类：<br>
<br>
<strong>平面着色</strong><br>
<br>
<div align="center">
<img aid="1034874" zoomfile="https://di.gameres.com/attachment/forum/202203/28/111827oa2bpm3ep34y22by.png" data-original="https://di.gameres.com/attachment/forum/202203/28/111827oa2bpm3ep34y22by.png" width="600" id="aimg_1034874" inpost="1" src="https://di.gameres.com/attachment/forum/202203/28/111827oa2bpm3ep34y22by.png" referrerpolicy="no-referrer">
</div><br>
<br>
<strong>顶点动画</strong><br>
<br>
<div align="center">
<img aid="1034875" zoomfile="https://di.gameres.com/attachment/forum/202203/28/111828hv3wnaskhpwvvivq.gif" data-original="https://di.gameres.com/attachment/forum/202203/28/111828hv3wnaskhpwvvivq.gif" width="480" id="aimg_1034875" inpost="1" src="https://di.gameres.com/attachment/forum/202203/28/111828hv3wnaskhpwvvivq.gif" referrerpolicy="no-referrer">
</div><br>
<br>
<strong>流体模拟</strong><br>
<br>
<div align="center">
<img aid="1034876" zoomfile="https://di.gameres.com/attachment/forum/202203/28/111829l4cx07z9hbx85x92.gif" data-original="https://di.gameres.com/attachment/forum/202203/28/111829l4cx07z9hbx85x92.gif" width="480" id="aimg_1034876" inpost="1" src="https://di.gameres.com/attachment/forum/202203/28/111829l4cx07z9hbx85x92.gif" referrerpolicy="no-referrer">
</div><br>
<br>
本文实现的是基于平面着色的水面效果，虽然它并非高端效果，但却是大部分 3D 项目中采用的方案。<br>
<br>
基于平面着色的水面渲染主要涉及以下几个部分：<br>
<br>
<strong>反射</strong><br>
<br>
<strong>折射</strong><br>
<br>
<strong>水深效果</strong><br>
<br>
<strong>水岸柔边</strong><br>
<br>
<strong>动态天空盒</strong><br>
<br>
<strong>法线图与光照</strong><br>
<br>
<strong>岸边浪花</strong><br>
<br>
由于时间关系，法线图与光照与岸边浪花暂未实现。<br>
<br>
标准的渲染流程如下所示：<br>
<br>
<div align="center">
<img aid="1034877" zoomfile="https://di.gameres.com/attachment/forum/202203/28/111830v63pjtuln7zazrji.png" data-original="https://di.gameres.com/attachment/forum/202203/28/111830v63pjtuln7zazrji.png" width="600" id="aimg_1034877" inpost="1" src="https://di.gameres.com/attachment/forum/202203/28/111830v63pjtuln7zazrji.png" referrerpolicy="no-referrer">
</div><br>
<br>
可以看出，如果要实现所有效果，至少需要绘制场景4次。<br>
<br>
由于这里的深度图只是和折射搭配使用，8位精度足够用了，我们可以考虑借用折射图中的 Alpha 通道来存储深度信息。<br>
<br>
优化后的流程图如下：<br>
<br>
<div align="center">
<img aid="1034878" zoomfile="https://di.gameres.com/attachment/forum/202203/28/111830asjasggzzgk7vcvv.png" data-original="https://di.gameres.com/attachment/forum/202203/28/111830asjasggzzgk7vcvv.png" width="600" id="aimg_1034878" inpost="1" src="https://di.gameres.com/attachment/forum/202203/28/111830asjasggzzgk7vcvv.png" referrerpolicy="no-referrer">
</div><br>
<br>
<strong><font color="#de5650">三、反射贴图渲染</font></strong><br>
<br>
麒麟子在《用实时反射 Shader 增强画面颜值》中已经完整地剖析了实时反射相关原理，在此就不再敷述，有需要了解的读者可直接点击查看。<br>
<br>
这里主要讲一讲本 DEMO 中的实现步骤。<br>
<br>
<strong>步骤1</strong>：使用代码新建一个 RenderTexture。<br>
<br>
<strong>步骤2</strong>：创建一个节点，添加摄像机组件，并将 clearFlags、clearColor、visibility 属性与主摄像机同步。<br>
<br>
<strong>步骤3</strong>：设置反射摄像机的渲染优先级，确保比主摄像机先渲染。<br>
<br>
<strong>步骤4</strong>：将新创建的 RenderTexture 赋值给此摄像机的 targetTexture 属性。<br>
<br>
以上步骤的代码在 WaterPlane.ts 中，如下图所示：<br>
<br>
<div align="center">
<img aid="1034879" zoomfile="https://di.gameres.com/attachment/forum/202203/28/111831upf2pnpy729nnjnj.png" data-original="https://di.gameres.com/attachment/forum/202203/28/111831upf2pnpy729nnjnj.png" width="600" id="aimg_1034879" inpost="1" src="https://di.gameres.com/attachment/forum/202203/28/111831upf2pnpy729nnjnj.png" referrerpolicy="no-referrer">
</div><br>
<br>
<strong>步骤5</strong>：在 lateUpdate 中同步主摄像机参数。<br>
<br>
<div align="center">
<img aid="1034880" zoomfile="https://di.gameres.com/attachment/forum/202203/28/111831jcmcsmspayzmpca1.png" data-original="https://di.gameres.com/attachment/forum/202203/28/111831jcmcsmspayzmpca1.png" width="600" id="aimg_1034880" inpost="1" src="https://di.gameres.com/attachment/forum/202203/28/111831jcmcsmspayzmpca1.png" referrerpolicy="no-referrer">
</div><br>
<br>
<strong>步骤6</strong>：在 lateUpdate 中根据实时反射原理，动态计算摄像机关于主摄像机的镜像位置和旋转。<br>
<br>
最终，渲染得到的 RenderTexture 如下：<br>
<br>
<div align="center">
<img aid="1034881" zoomfile="https://di.gameres.com/attachment/forum/202203/28/111833paspvokq0k0kqoek.jpg" data-original="https://di.gameres.com/attachment/forum/202203/28/111833paspvokq0k0kqoek.jpg" width="600" id="aimg_1034881" inpost="1" src="https://di.gameres.com/attachment/forum/202203/28/111833paspvokq0k0kqoek.jpg" referrerpolicy="no-referrer">
</div><br>
<br>
<strong>麒麟小贴士：</strong><br>
<br>
所有物体的材质，需要加入自定义裁剪面，裁剪掉水面以下的部分。<br>
<br>
可以明显看到，上图中绿色物体的倒影，水面以下的部分是被裁剪掉了的。<br>
<br>
<strong><font color="#de5650">四、折射贴图渲染</font></strong><br>
<br>
折射渲染的原理非常简单：<br>
<br>
<strong>渲染水平面以下的部分到 RenderTexture</strong><br>
<br>
<strong>在水面渲染阶段使用噪声图进行扰动，以模拟出水面折射效果</strong><br>
<br>
折射渲染的流程与反射渲染大致相同，只有两个细小的差别：<br>
<br>
<strong>用于折射渲染的摄像机所有参数均与主摄像保持一致即可</strong><br>
<br>
<strong>折射渲染阶段，物体被裁剪掉的是水面以上的部分</strong><br>
<br>
下面我们来看看，本 DEMO 中关于折射的实现步骤。<br>
<br>
<strong>步骤1</strong>：使用代码新建一个 RenderTexture。<br>
<br>
<strong>步骤2</strong>：创建一个节点，添加摄像机组件，并将 clearFlags、clearColor、visibility 属性与主摄像机同步。<br>
<br>
<strong>步骤3</strong>：设置反射摄像机的渲染优先级，确保比主摄像机先渲染。<br>
<br>
<strong>步骤4</strong>：将新创建的 RenderTexture 赋值给此摄像机的 targetTexture 属性。<br>
<br>
以上步骤的代码在 WaterPlane.ts 中，如下图所示：<br>
<br>
<div align="center">
<img aid="1034882" zoomfile="https://di.gameres.com/attachment/forum/202203/28/111834c5p8tpjaouw2xw5x.png" data-original="https://di.gameres.com/attachment/forum/202203/28/111834c5p8tpjaouw2xw5x.png" width="600" id="aimg_1034882" inpost="1" src="https://di.gameres.com/attachment/forum/202203/28/111834c5p8tpjaouw2xw5x.png" referrerpolicy="no-referrer">
</div><br>
<br>
<strong>麒麟小贴士</strong>： 注意红色线框部分，本 DEMO 中折射贴图的 Alpha 通道用于标记深度信息，所以需要确保 Alpha 通道的值为 255。<br>
<br>
<strong>步骤5</strong>：在 lateUpdate 中同步主摄像机参数、位置、旋转等信息。<br>
<br>
最终，渲染得到的 RenderTexture 如下：<br>
<br>
<div align="center">
<img aid="1034883" zoomfile="https://di.gameres.com/attachment/forum/202203/28/111834uif4sa1uuuj4uoui.png" data-original="https://di.gameres.com/attachment/forum/202203/28/111834uif4sa1uuuj4uoui.png" width="600" id="aimg_1034883" inpost="1" src="https://di.gameres.com/attachment/forum/202203/28/111834uif4sa1uuuj4uoui.png" referrerpolicy="no-referrer">
</div><br>
<br>
<strong><font color="#de5650">五、水面渲染</font></strong><br>
<br>
水面渲染主要利用了投影纹理技术，将顶点的投影坐标转化为 UV，对折射和反射贴图进行采样。<br>
<br>
由于使用了折射贴图，我们的水面材质不需要开启 Alpha 混合。<br>
<br>
<strong>折射渲染</strong><br>
<br>
<strong>步骤1</strong>：根据投影坐标计算出屏幕 UV。如下所示：<br>
<br>
<strong>vec2 screenUV = v_screenPos.xy / v_screenPos.w * 0.5 + 0.5;</strong><br>
<br>
<strong>步骤2</strong>：采样折射贴图，可以得到如下渲染效果：<br>
<br>
<div align="center">
<img aid="1034884" zoomfile="https://di.gameres.com/attachment/forum/202203/28/111834sjrpgkj1zk1k8crr.png" data-original="https://di.gameres.com/attachment/forum/202203/28/111834sjrpgkj1zk1k8crr.png" width="600" id="aimg_1034884" inpost="1" src="https://di.gameres.com/attachment/forum/202203/28/111834sjrpgkj1zk1k8crr.png" referrerpolicy="no-referrer">
</div><br>
<br>
左边为正常渲染效果，右边为标记了折射内容的效果<br>
<br>
<strong>步骤3</strong>：使用噪声图对折射进行扰动，可得到如下效果：<br>
<br>
<div align="center">
<img aid="1034885" zoomfile="https://di.gameres.com/attachment/forum/202203/28/111836nntnf8ay5538ytt8.gif" data-original="https://di.gameres.com/attachment/forum/202203/28/111836nntnf8ay5538ytt8.gif" width="600" id="aimg_1034885" inpost="1" src="https://di.gameres.com/attachment/forum/202203/28/111836nntnf8ay5538ytt8.gif" referrerpolicy="no-referrer">
</div><br>
<br>
<strong>反射渲染</strong><br>
<br>
<strong>步骤1</strong>：与折射渲染一样，根据投影坐标计算出屏幕 UV。<br>
<br>
<strong>步骤2</strong>：采样反射贴图，可以得到如下渲染效果：<br>
<br>
<div align="center">
<img aid="1034886" zoomfile="https://di.gameres.com/attachment/forum/202203/28/111836j3kf0kn0okm8jpje.png" data-original="https://di.gameres.com/attachment/forum/202203/28/111836j3kf0kn0okm8jpje.png" width="600" id="aimg_1034886" inpost="1" src="https://di.gameres.com/attachment/forum/202203/28/111836j3kf0kn0okm8jpje.png" referrerpolicy="no-referrer">
</div><br>
<br>
<strong>步骤3</strong>：使用噪声图对反射进行扰动，可得到如下效果：<br>
<br>
<div align="center">
<img aid="1034887" zoomfile="https://di.gameres.com/attachment/forum/202203/28/111838qvtv3x1vpx4bq00b.gif" data-original="https://di.gameres.com/attachment/forum/202203/28/111838qvtv3x1vpx4bq00b.gif" width="600" id="aimg_1034887" inpost="1" src="https://di.gameres.com/attachment/forum/202203/28/111838qvtv3x1vpx4bq00b.gif" referrerpolicy="no-referrer">
</div><br>
<br>
<strong>菲涅尔混合</strong><br>
<br>
菲涅尔的计算公式从玉兔的边缘光教程开始，到实时反射等场合，已经出现过很多次了。下面是核心代码：<br>
<br>
<div align="center">
<img aid="1034888" zoomfile="https://di.gameres.com/attachment/forum/202203/28/111838ynkmqw1mdwmokwwz.png" data-original="https://di.gameres.com/attachment/forum/202203/28/111838ynkmqw1mdwmokwwz.png" width="600" id="aimg_1034888" inpost="1" src="https://di.gameres.com/attachment/forum/202203/28/111838ynkmqw1mdwmokwwz.png" referrerpolicy="no-referrer">
</div><br>
<br>
折射可以视为水体本色，利用菲涅尔因子与反射内容混合，即可实现一个带折射和反射的水体效果。<br>
<br>
伪代码如下：<br>
<br>
<strong>finalColor = mix(refractionColor,reflectionColor,fresnel)</strong><br>
<br>
最终可以得到如下显示效果：<br>
<br>
<div align="center">
<img aid="1034889" zoomfile="https://di.gameres.com/attachment/forum/202203/28/111839ytdfjyidfyfddrrs.gif" data-original="https://di.gameres.com/attachment/forum/202203/28/111839ytdfjyidfyfddrrs.gif" width="600" id="aimg_1034889" inpost="1" src="https://di.gameres.com/attachment/forum/202203/28/111839ytdfjyidfyfddrrs.gif" referrerpolicy="no-referrer">
</div><br>
<br>
完整代码代码请查看项目中的 effect-water.effect 文件。<br>
<br>
<strong><font color="#de5650">六、水深效果</font></strong><br>
<br>
从上面的动画中可以看出，虽然折射和反射效果都有了。但画风有些奇怪，完全没有水面的感觉。<br>
<br>
<strong>这是水面没有深浅效果导致的。</strong><br>
<br>
我们来看看，如何获取深度信息，并根据深度信息实现水深效果。<br>
<br>
<strong>获取深度信息</strong><br>
<br>
<div align="center">
<img aid="1034905" zoomfile="https://di.gameres.com/attachment/forum/202203/28/112440boxxowgp3wxg3gl8.jpg" data-original="https://di.gameres.com/attachment/forum/202203/28/112440boxxowgp3wxg3gl8.jpg" width="600" id="aimg_1034905" inpost="1" src="https://di.gameres.com/attachment/forum/202203/28/112440boxxowgp3wxg3gl8.jpg" referrerpolicy="no-referrer">
</div><br>
<br>
从上图中，我们可以清晰地看到，靠近岸边的海水的颜色比远处海水的颜色透明得多。<br>
<br>
产生这种现象的主要原因，就是基于视线方向的水体厚度不同。<br>
<br>
什么叫基于视线方向的水体厚度，请看下图：<br>
<br>
<div align="center">
<img aid="1034890" zoomfile="https://di.gameres.com/attachment/forum/202203/28/111839l6re4qezwqaya7fw.png" data-original="https://di.gameres.com/attachment/forum/202203/28/111839l6re4qezwqaya7fw.png" width="600" id="aimg_1034890" inpost="1" src="https://di.gameres.com/attachment/forum/202203/28/111839l6re4qezwqaya7fw.png" referrerpolicy="no-referrer">
</div><br>
<br>
我们通常说的水体深度，是指在忽略视线因素的情况，水面到水底的高度差。<br>
<br>
在不追究细节的情况下，我们可以简单地使用高度差来作为水的深度。<br>
<br>
一种可能的伪代码如下：<br>
<br>
<strong>depth = clamp((g_waterLevel - v_position.y) * depthScale,0.0,1.0);</strong><br>
<br>
其中 depthScale 是我们的深度缩放因子，可以用来调节比例尺问题，以及水体能见度线性衰减速率。<br>
<br>
而基于视线方向的水体厚度，是指视线方向与水平面和水底交点的距离差。即图中 点 P1 到 点 P2 的距离。<br>
<br>
下面我们来推导一下，使用基于视线方向水体的厚度来作为深度因子的公式。<br>
<br>
许多朋友第一反应是解直线方程，但用空间向量的特性来求解会更容易。<br>
<br>
为方便对照理解，再贴一次上面的图：<br>
<br>
<div align="center">
<img aid="1034891" zoomfile="https://di.gameres.com/attachment/forum/202203/28/111839ia88rnamrtyty38s.png" data-original="https://di.gameres.com/attachment/forum/202203/28/111839ia88rnamrtyty38s.png" width="600" id="aimg_1034891" inpost="1" src="https://di.gameres.com/attachment/forum/202203/28/111839ia88rnamrtyty38s.png" referrerpolicy="no-referrer">
</div><br>
<br>
设观察方向为 viewDir，厚度为 depth 则有：<br>
<br>
<strong>P1 + viewDir * depth = P2</strong><br>
<br>
分拆为分量运算可得：<br>
<br>
P1.x + viewDir.x * depth = P2.x<br>
<br>
<strong>P1.y + viewDir.y * depth = P2.y</strong><br>
<br>
P1.z + viewDir.z * depth = P2.z<br>
<br>
可推导出：<br>
<br>
<strong>depth = (P2.y - P1.y) / viewDir.y</strong><br>
<br>
由此可得如下计算公式：<br>
<br>
<strong>vec3 viewDir = normalize(v_position.xyz - cc_cameraPos.xyz);</strong><br>
<br>
<strong>float depth = (v_position.y - g_waterLevel) / viewDir.y</strong><br>
<br>
<strong>depth = clamp(depth * depthScale,0.0,1.0);</strong><br>
<br>
比起直接使用水体深度来说，多了一次求 viewDir 单位向量的运算，以及一次除以 viewDir.y 运算。<br>
<br>
在非极端情况下，多出的这一点纯逻辑运算在 GPU 上是可以忽略不计的，可以放心使用。<br>
<br>
将上述公式添加到渲染对象的 Shader 中，并在折射渲染阶段启用，将结果存入 Alpha 通道即可。<br>
<br>
项目中的 Shader 代码如下图所示：<br>
<br>
<div align="center">
<img aid="1034892" zoomfile="https://di.gameres.com/attachment/forum/202203/28/111840ovn4j4w16ndzw3a8.png" data-original="https://di.gameres.com/attachment/forum/202203/28/111840ovn4j4w16ndzw3a8.png" width="600" id="aimg_1034892" inpost="1" src="https://di.gameres.com/attachment/forum/202203/28/111840ovn4j4w16ndzw3a8.png" referrerpolicy="no-referrer">
</div><br>
<br>
最终得到的深度信息如下：<br>
<br>
<div align="center">
<img aid="1034893" zoomfile="https://di.gameres.com/attachment/forum/202203/28/111840e4xwz33s4qqsprk4.png" data-original="https://di.gameres.com/attachment/forum/202203/28/111840e4xwz33s4qqsprk4.png" width="600" id="aimg_1034893" inpost="1" src="https://di.gameres.com/attachment/forum/202203/28/111840e4xwz33s4qqsprk4.png" referrerpolicy="no-referrer">
</div><br>
<br>
<strong>深度混合</strong><br>
<br>
有了上面的深度信息，我们只需要在计算出折射颜色后，再用深度信息与水底颜色混合即可。Shader 代码如下图所示：<br>
<br>
<div align="center">
<img aid="1034894" zoomfile="https://di.gameres.com/attachment/forum/202203/28/111840gpmaogn7ua6no46a.png" data-original="https://di.gameres.com/attachment/forum/202203/28/111840gpmaogn7ua6no46a.png" width="600" id="aimg_1034894" inpost="1" src="https://di.gameres.com/attachment/forum/202203/28/111840gpmaogn7ua6no46a.png" referrerpolicy="no-referrer">
</div><br>
<br>
由于水体的可见度是非线性的，所以对 diffDepth 使用了 pow 函数，这个 power 参数默认是 2.0。<br>
<br>
最终可以得到如下效果：<br>
<br>
<div align="center">
<img aid="1034895" zoomfile="https://di.gameres.com/attachment/forum/202203/28/111841txzqk0y0o434rlg6.gif" data-original="https://di.gameres.com/attachment/forum/202203/28/111841txzqk0y0o434rlg6.gif" width="600" id="aimg_1034895" inpost="1" src="https://di.gameres.com/attachment/forum/202203/28/111841txzqk0y0o434rlg6.gif" referrerpolicy="no-referrer">
</div><br>
<br>
<strong><font color="#de5650">六、水岸柔边</font></strong><br>
<br>
<div align="center">
<img aid="1034896" zoomfile="https://di.gameres.com/attachment/forum/202203/28/111842hpwtv1va958pw92v.png" data-original="https://di.gameres.com/attachment/forum/202203/28/111842hpwtv1va958pw92v.png" width="600" id="aimg_1034896" inpost="1" src="https://di.gameres.com/attachment/forum/202203/28/111842hpwtv1va958pw92v.png" referrerpolicy="no-referrer">
</div><br>
<br>
当我们把摄像机拉近，观察水面与物体交接处的时候，可以明显看到一条清晰的边界。<br>
<br>
这条边界在反射越强的时候越明显，使我们的水面效果大打折扣。<br>
<br>
好在我们已经有了深度信息，可以根据深度来判断出哪里靠近岸边，并修改菲涅尔因子，使反射越靠近岸边的时候越弱即可。<br>
<br>
核心代码如下：<br>
<br>
<div align="center">
<img aid="1034897" zoomfile="https://di.gameres.com/attachment/forum/202203/28/111842g2z550kkjt1f16m6.png" data-original="https://di.gameres.com/attachment/forum/202203/28/111842g2z550kkjt1f16m6.png" width="600" id="aimg_1034897" inpost="1" src="https://di.gameres.com/attachment/forum/202203/28/111842g2z550kkjt1f16m6.png" referrerpolicy="no-referrer">
</div><br>
<br>
最终可以实现在全反射的情况下，水面与岸边依然平滑过渡。效果如下图所示：<br>
<br>
<div align="center">
<img aid="1034898" zoomfile="https://di.gameres.com/attachment/forum/202203/28/111843pge0c0u78rz8z9x0.png" data-original="https://di.gameres.com/attachment/forum/202203/28/111843pge0c0u78rz8z9x0.png" width="600" id="aimg_1034898" inpost="1" src="https://di.gameres.com/attachment/forum/202203/28/111843pge0c0u78rz8z9x0.png" referrerpolicy="no-referrer">
</div><br>
<br>
再来一张远视角的图：<br>
<br>
<div align="center">
<img aid="1034899" zoomfile="https://di.gameres.com/attachment/forum/202203/28/111844p6ucbnntuuldg2z4.png" data-original="https://di.gameres.com/attachment/forum/202203/28/111844p6ucbnntuuldg2z4.png" width="600" id="aimg_1034899" inpost="1" src="https://di.gameres.com/attachment/forum/202203/28/111844p6ucbnntuuldg2z4.png" referrerpolicy="no-referrer">
</div><br>
<br>
<strong><font color="#de5650">七、动态天空盒</font></strong><br>
<br>
<div align="center">
<img aid="1034900" zoomfile="https://di.gameres.com/attachment/forum/202203/28/111849rfttq5a60gbjp6te.gif" data-original="https://di.gameres.com/attachment/forum/202203/28/111849rfttq5a60gbjp6te.gif" width="600" id="aimg_1034900" inpost="1" src="https://di.gameres.com/attachment/forum/202203/28/111849rfttq5a60gbjp6te.gif" referrerpolicy="no-referrer">
</div><br>
<br>
为了增强氛围感，DEMO 中使用了动态天空盒。<br>
<br>
这是一个特别简单的高效的动态天空盒方案，仅使用了一个双层纹理混合的半球模型，调节两张纹理的水平方向流动速度即可。<br>
<br>
<div align="center">
<img aid="1034901" zoomfile="https://di.gameres.com/attachment/forum/202203/28/111851u0kq1fbmsho8cn3m.png" data-original="https://di.gameres.com/attachment/forum/202203/28/111851u0kq1fbmsho8cn3m.png" width="600" id="aimg_1034901" inpost="1" src="https://di.gameres.com/attachment/forum/202203/28/111851u0kq1fbmsho8cn3m.png" referrerpolicy="no-referrer">
</div><br>
<br>
<div align="center">
<img aid="1034902" zoomfile="https://di.gameres.com/attachment/forum/202203/28/111853eq25psqhgdxx6pnr.png" data-original="https://di.gameres.com/attachment/forum/202203/28/111853eq25psqhgdxx6pnr.png" width="600" id="aimg_1034902" inpost="1" src="https://di.gameres.com/attachment/forum/202203/28/111853eq25psqhgdxx6pnr.png" referrerpolicy="no-referrer">
</div><br>
<br>
<strong><font color="#de5650">八、关于DEMO</font></strong><br>
<br>
所有效果参数均可调节，如下图所示：<br>
<br>
<div align="center">
<img aid="1034903" zoomfile="https://di.gameres.com/attachment/forum/202203/28/111855qflgbeyfkjyyjzjk.png" data-original="https://di.gameres.com/attachment/forum/202203/28/111855qflgbeyfkjyyjzjk.png" width="600" id="aimg_1034903" inpost="1" src="https://di.gameres.com/attachment/forum/202203/28/111855qflgbeyfkjyyjzjk.png" referrerpolicy="no-referrer">
</div><br>
<br>
<font size="2"></font><br>
<font size="2">来源：COCOS</font><br>
<font size="2">原文：https://mp.weixin.qq.com/s/yLEt3yHBj9lBNWm_xANvJw</font><br>
<br>
<br>
  
</div>
            