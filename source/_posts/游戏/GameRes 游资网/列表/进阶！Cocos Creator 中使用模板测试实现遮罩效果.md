
---
title: '进阶！Cocos Creator 中使用模板测试实现遮罩效果'
categories: 
 - 游戏
 - GameRes 游资网
 - 列表
headimg: 'https://di.gameres.com/attachment/forum/202111/10/103852yyn5zyxpnw37v77v.jpg'
author: GameRes 游资网
comments: false
date: Wed, 10 Nov 2021 00:00:00 GMT
thumbnail: 'https://di.gameres.com/attachment/forum/202111/10/103852yyn5zyxpnw37v77v.jpg'
---

<div>   
<table cellspacing="0" cellpadding="0"><tbody><tr><td class="t_f" id="postmessage_2518255">
在之前的章节里，我们知道的都是平面上的渲染，直接往屏幕上画东西就可以了，绘制的内容都比较单一。但在 3D 游戏里，我们需要考虑的东西则会多很多。比如在人群中，视野方向的人物模型很多，每一个人物模型都需要绘制，如何让距离相机进的物体不被离得远的遮挡？再比如，街道两边有很多带有玻璃窗的商店，如何通过玻璃窗看到里面的景象？<br><br>
要实现这里的功能，就需要涉及到渲染流程的最后一个阶段：alpha 测试与混合。在这个阶段里 GPU 主要的工作是逐片元操作，将它们的颜色以某种形式合并，得到最终在屏幕上显示的像素颜色。主要涉及的工作有两个：对片元进行测试并进行合并。测试步骤决定了片元最终会不会被显示出来。在 WebGL 里主要的测试有裁剪测试、透明度测试、模板测试以及深度测试，这几个测试都是高度可配置的。其中，考量到裁剪测试没有模板测试来得更加灵活，因此本次就不涉及裁剪测试内容。整个测试流程如下图：<br><br><div align="center">
<img id="aimg_1020720" aid="1020720" zoomfile="https://di.gameres.com/attachment/forum/202111/10/103852yyn5zyxpnw37v77v.jpg" data-original="https://di.gameres.com/attachment/forum/202111/10/103852yyn5zyxpnw37v77v.jpg" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202111/10/103852yyn5zyxpnw37v77v.jpg" referrerpolicy="no-referrer">
</div>
<br>
从图中可以看出，片元着色器输出的颜色缓冲并不是最终屏幕上呈现的颜色缓冲，还必须经过模板、深度和混合测试影响后才能得到最终用来输出的颜色缓冲。本章重点介绍模板测试和深度测试，混合测试将在下一章中为大家介绍。<br><br>
>注意：由于这部分内容是补充知识，重点在于了解一下这部分的概念以及在 Cocos Creator 3.x 中的应用即可。<br><br><strong><font color="#de5650">模板测试（Stencil Test）</font></strong><br><br>
Stencil 的本质是镂空，通过这样的板子就可以方便的画出某个特定的形状。模板测试的核心是持有一个模板缓冲，每个像素/片段都有一个模板值，通常每个模板值是 8 位（用掩码表示），也就是可以有 256 种不同的值，这样就可以通过设置我们想要的模板值来丢弃或保留这个片段。一个简单模板测试例子如下：<br><br><div align="center"><font size="2">
<img id="aimg_1020721" aid="1020721" zoomfile="https://di.gameres.com/attachment/forum/202111/10/103852nersjmrg4mc2gpmg.jpg" data-original="https://di.gameres.com/attachment/forum/202111/10/103852nersjmrg4mc2gpmg.jpg" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202111/10/103852nersjmrg4mc2gpmg.jpg" referrerpolicy="no-referrer"></font></div>
<div align="center"><font size="2">图片摘自 OpenGL</font></div>
<br>
通常，用户在启用模板缓冲的时候，会将整个模板缓冲中的所有片段的模板值设置为 0，丢弃所有片段。然后再设置特定区域的模板值（大于 0）以及比较函数。GPU 会读取用户设置的模板值，然后将该值与模板缓冲中该位置的模板值按比较函数进行比较，最终决定是保留还是舍弃该片段，形成镂空，也就是遮罩效果。在模板测试中，有两个很重要的方法是 “stencilFunc” 和 “stencilOp”，前者用来控制 stencil 的测试方式，得出测试结果，后者根据结果决定要如何处理缓冲中的数据。<br><br>
`void stencilFunc(GLenum func, GLint ref, GLuint mask)` ：<br><br>
func：指定模板测试比较函数。默认是 Always。<br><br><div align="center">
<img id="aimg_1020722" aid="1020722" zoomfile="https://di.gameres.com/attachment/forum/202111/10/103853zozzmb7skbm7ot7k.jpg" data-original="https://di.gameres.com/attachment/forum/202111/10/103853zozzmb7skbm7ot7k.jpg" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202111/10/103853zozzmb7skbm7ot7k.jpg" referrerpolicy="no-referrer">
</div>
<br>
ref：用来做模板测试的参考值。<br><br>
mask：指定操作掩码。在测试时会先将 ref 与 mask 进行与运算，再将 ref 与模板缓冲（stencil buffer）中的值进行与运算，最后根据比较函数得出结果。<br><br>
单纯看这些描述可能还不是很理解这里的意思，在这举个例子：<br><br>
gl.stencilFunc(gl.GEQUAL, 1, 0xff); // 此处，mask 采用 16 进制的原因是因为数据在计算机中的表示最终都是以二进制形式存在，但二进制写起来太长了，因此可以采用 16 进制或者 8 进制解决。进制越大，数的表达长度也就越短。<br><br>
这个配置的意思是将值 1&0xff 与 stencil buffer&0xff 进行比较，判断是否满足 GEQUAL 的条件，满足则测试通过，否则测试不通过。因此，我们在这里只是想单纯的让 ref 和 stencil buffer 进行比较，mask 就不能成为干扰因素，因此设置为 0xff（11111111），让它每一位都为 1，“与”计算都会保持原值。如果想禁用模板，则可以设置 0x00 的值，这样模板缓冲中的值都是 0。<br><br>
模板测试通过或者不通过后要对模板缓冲进行什么操作，就需要用到 `void stencilOp(GLenum fail, GLenum zfail, GLenum zpass);`<br><br>
fail：指定当前模板测试不通过时的行为。默认为 KEEP。<br><br><div align="center">
<img id="aimg_1020723" aid="1020723" zoomfile="https://di.gameres.com/attachment/forum/202111/10/103853onu4q3h85t4nllu5.jpg" data-original="https://di.gameres.com/attachment/forum/202111/10/103853onu4q3h85t4nllu5.jpg" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202111/10/103853onu4q3h85t4nllu5.jpg" referrerpolicy="no-referrer">
</div>
<br>
zfail：指定当前模板测试通过但深度测试未通过时的行为。允许和默认的值同 fail。<br><br>
zpass：指定当前模板测试通过且深度测试也通过时的行为，或者当模板测试通过且没有开启深度测试时的行为。允许和默认的值同 fail。<br><br>
这里的内容就比较好理解，通常，我们会对测试失败时采用保持当前值的方式，测试通过时用设置值替换模板缓冲值。<br><br>
gl.stencilOp(gl.KEEP, gl.KEEP, gl.REPLACE);<br><br>
模板测试默认是处于禁用状态，使用时需要手动开启。<br><br>
// 默认情况下模板测试处于禁用状态，需要手动启用模板测试<br><br>
gl.enable(gl.STENCIL_TEST);<br><br>
// 同样需要在每次迭代之前清除模板缓冲<br><br>
gl.clear(gl.COLOR_BUFFER_BIT | gl.STENCIL_BUFFER_BIT);<br><br>
这里顺带提醒一下，如果想自己尝试在 WebGL 上写模板测试的同学，遇到模板测试没有生效的情况，可以检查一下，在请求上下文的时候是否有要求包含一个模板缓冲区。<br><br>
const gl = canvas.getContext("webgl", &#123; stencil: true &#125;);<br><br><strong><font color="#de5650">深度测试（Depth test）</font></strong><br><br>
深度测试是 3D 游戏里不可或缺的重要环节，可以帮助实现 3D 渲染上物体的遮挡效果，如果没有深度测试，可能会出现前后物体的渲染错乱或者闪烁的现象。<br><br>
深度测试的核心跟模板测试类似，也是持有一个深度缓冲，深度缓冲就像颜色缓冲(Color Buffer)（最终生成的像素颜色值的存储缓冲，最终设备上呈现的像素颜色就是从这里读取）一样存储了每个片段的深度值，以 16、24 或者 32 位 float 的形式存储，在大多数系统中默认精度是 24。当开启深度测试的时候，会将当前渲染的每一个片段的深度值与深度缓冲的内容进行对比测试。如果测试通过，深度缓冲则会更新新的深度值，如果测试失败，片段则会被丢弃。<br><br>
深度缓冲是在片段着色器运行之后（也在模板测试之后），在屏幕空间中运行的。屏幕空间坐标与 "gl.viewport" 设置有关，WebGL 会直接使用 GLSL 的内建变量 "gl_FragCoord" 从片段着色器直接访问。“gl_FragCoord” 的 x 和 y 分量代表了片段的屏幕空间坐标。同时，它也包含了一个 z 分量，这个是用来存储真正的深度值，最终用它来和深度缓冲中的内容进行对比。<br><br>
深度缓冲也有一个重要的函数 “void depthFunc(GLenum func)” 用来设置深度比较函数，比较的参数跟模板缓冲的比较函数所使用参数一样，默认参数为 LESS。深度测试默认也是禁用的，同样需要手动开启。<br><br>
const gl = canvas.getContext("webgl", &#123; stencil: true, depth: true &#125;);<br><br>
gl.clear(gl.COLOR_BUFFER_BIT | gl.STENCIL_BUFFER_BIT | gl.DEPTH_BUFFER_BIT);<br><br>
gl.enable(gl.DEPTH_TEST);<br><br>
当深度测试通过之后，会将当前片段的 z 值存入深度缓冲。当前片段的 z（深度）值是介于 0.0 到 1.0 直接的值。从观察者角度看到场景中物体的 z 值，这个值是投影矩阵作用后又经过标准设备坐标变换，最终再转换到 0.0 到 1.0 之间的值。<br><br><strong><font color="#de5650">在 3.x 中的应用</font></strong><br><br>
根据上面的内容相信大家应该基本了解了模板测试和深度测试的原理，接下来，我们试试在  Cocos Creator 如何应用这部分。Cocos Creator 底层默认对模板/深度等做了初始化处理，实现的模块是在引擎源码中的 webgl1/webgl2-device.ts 模块，由于此处我测试使用的是 WebGL1 的后端，因此，我在 Creator 版本安装目录下找到 resources->3d->engine->cocos->core->webgl->webgl-device.ts 模块，可以看到如下初始化内容：<br><br><div align="center"><font size="2">
<img id="aimg_1020724" aid="1020724" zoomfile="https://di.gameres.com/attachment/forum/202111/10/103854zwc8z4r8w4tpljtg.jpg" data-original="https://di.gameres.com/attachment/forum/202111/10/103854zwc8z4r8w4tpljtg.jpg" width="572" inpost="1" src="https://di.gameres.com/attachment/forum/202111/10/103854zwc8z4r8w4tpljtg.jpg" referrerpolicy="no-referrer"></font></div>
<div align="center"><font size="2">注：虽然 API 部分有轻微差异，这是因为 WebGL 提供了不止一种方法设置，但概念基本相同。</font></div>
<br>
这里罗列出的默认配置，主要针对 3D 对象配置，由于 2D 对象大多数包含透明像素，因此底层 2D 管线没有处理深度部分，这样就不需要进行深度测试，可以在之前像 builtin-sprite 这类 2D Effect 上看到针对深度测试部分都采用了手动关闭的形式。因此，在接下来的深度模板测试实践中，选用的是 3D 对象。尝试在场景里摆放上 2 个模型，来测试一下深度相关。人物模型为 O1，场景模型为 O2。模型与相机的摆放位置如下：<br><br><div align="center">
<img id="aimg_1020725" aid="1020725" zoomfile="https://di.gameres.com/attachment/forum/202111/10/103854etutbz8k7lt6dh86.jpg" data-original="https://di.gameres.com/attachment/forum/202111/10/103854etutbz8k7lt6dh86.jpg" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202111/10/103854etutbz8k7lt6dh86.jpg" referrerpolicy="no-referrer">
</div>
<br>
从 <a href="https://mp.weixin.qq.com/s/K2jlmFgt1HLYN-B3jtroHA" target="_blank">《Cocos Shader 系列：基础入门（五）》</a>中有关于模板深度缓冲的写法就可以看出每一个 pass 都可以对模板/深度缓冲进行配置。大致的写法如下：<br><br>
CCEffect %&#123;<br><br>
techniques:<br><br>
- name: opaque<br><br>
passes:<br><br>
- vert: ...<br><br>
frag: ...<br><br>
properties: ...<br><br>
depthStencilState:<br><br>
deprhTest: false<br><br>
...<br><br>
&#125;%<br><br>
这样的写法通常是为了设置 pass 初始化时的数据，如果需要修改，Cocos Creator 3.x 也针对 Effect 写法进行了封装。在属性检查器面板上每一个材质的 pass 下都可以看到 PipelineStates 属性，可以很方便的进行可视化配置。<br><br><div align="center">
<img id="aimg_1020726" aid="1020726" zoomfile="https://di.gameres.com/attachment/forum/202111/10/103855rg8m8mk89acm4arv.jpg" data-original="https://di.gameres.com/attachment/forum/202111/10/103855rg8m8mk89acm4arv.jpg" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202111/10/103855rg8m8mk89acm4arv.jpg" referrerpolicy="no-referrer">
</div>
<br><strong>可配置参数以及说明如下：</strong><br><br><div align="center">
<img id="aimg_1020727" aid="1020727" zoomfile="https://di.gameres.com/attachment/forum/202111/10/103855g0cbpwbflf799zcl.jpg" data-original="https://di.gameres.com/attachment/forum/202111/10/103855g0cbpwbflf799zcl.jpg" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202111/10/103855g0cbpwbflf799zcl.jpg" referrerpolicy="no-referrer">
</div>
<br>
接着，对人物模型 O1 修改一些配置：<br><br>
材质关闭 depthTest，并应用。直接在编辑器上可以观察到由于没有进行深度测试，所以 O1 的绘制内容被地面覆盖，同时自身身上的装饰物渲染顺序也出现错乱。<br><br><div align="center">
<img id="aimg_1020728" aid="1020728" zoomfile="https://di.gameres.com/attachment/forum/202111/10/103856b7zvddccyzvtlvpt.jpg" data-original="https://di.gameres.com/attachment/forum/202111/10/103856b7zvddccyzvtlvpt.jpg" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202111/10/103856b7zvddccyzvtlvpt.jpg" referrerpolicy="no-referrer">
</div>
<br>
材质开启 depthTest，调整 depthFunc 为 GREATER，并应用。此时可以发现，无论你怎么找，模型都无法被看见。正常来说被背景模型因为深度测试函数使用还是 LESS，所以会覆盖深度缓冲内容，但是不至于全部都能覆盖得到，那么覆盖不到的部分也不可能完全看不见人物模型的。这主要是因为我们每帧都会清除深度缓冲，清除的深度缓冲区默认值为 1.0，表示最大的深度值。因此，人物模型再怎么远都不可能比最大值来的远。<br><br>
将所有修改还原，接下来，进行模板测试。模板测试需要有两个基础操作，一个是将所有的片段清空，一个是设定特定区域的模板值。然后，需要绘制的物体只需要选择在特定的模板值上绘制即可。我这里准备实现一个只显示人物模型上半身的效果。准备两个面片（quad），每个面片都有自己的材质（Effect 用默认的 builtin-standard），A 面片离相机最近，做人物消失效果；B 面片只有人物上半身大小，位于人物上半身位置，相比于 A 离相机第二近，做人物只显示区域设置；最后人物在这两个面片后面。摆放位置如下：<br><br><div align="center">
<img id="aimg_1020729" aid="1020729" zoomfile="https://di.gameres.com/attachment/forum/202111/10/103858kh3r1ff66716icid.jpg" data-original="https://di.gameres.com/attachment/forum/202111/10/103858kh3r1ff66716icid.jpg" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202111/10/103858kh3r1ff66716icid.jpg" referrerpolicy="no-referrer">
</div>
<br>
接着，做如下操作：<br><br>
将材质 A（面片 A 的材质）的正反面 stencilTest 都开启，有关正反面是什么会在下一章中说到。将 stencilFunc 设置为 NEVER，stencillFailOp 设置为 ZERO，并点击应用。此处的配置让模板测试永不通过，执行 fail 函数，将所有模型绘制区域的模板缓冲都设置为 0。<br><br>
将材质 B（面片 B 的材质）的正反面 stencilTest 都开启，stencilFunc 设置为 NEVER，stencillFailOp 设置为 REPLACE，stencilRef 设置为 1，并点击应用。此处的配置让模板测试永不通过，执行 fail 函数，将所有模型绘制区域的模板缓冲都设置为 ref。<br><br>
将人物材质的正反面 stencilTest 都开启，stencilFunc 设置为 EQUAL，stencilRef 设置为 1，stencilReadMask 和 stencilWriteMask 设置值为 ref，stencillFailOp、stencilZFailOp 和 stencilPassOp 设置为 KEEP，并点击应用。此处的配置只有 ref 值和模板测试值相等的情况下才能通过模板测试，测试通过后用 stencilRef&stencilWriteMask 替换模板缓冲中的相对应片段。<br><br>
最后得出的效果如下：<br><br><div align="center">
<img id="aimg_1020730" aid="1020730" zoomfile="https://di.gameres.com/attachment/forum/202111/10/103858e0huhnd0bh0qm6uf.jpg" data-original="https://di.gameres.com/attachment/forum/202111/10/103858e0huhnd0bh0qm6uf.jpg" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202111/10/103858e0huhnd0bh0qm6uf.jpg" referrerpolicy="no-referrer">
</div>
<br>
只有模型的上半身显示了出来，大家可以尝试着从不同角度来观察效果。<br><br>
有关模板测试和深度测试的内容就到这为止，感兴趣的同学可以去增加更多不同的组合实现特别的效果。在下一个章节我们将来认识一下混合测试（BlendState）和面剔除（CullMode）。<br><br>
内容参考：<br><br>
1. 模板测试：<br><br>
https://learnopengl-cn.github.io/04%20Advanced%20OpenGL/02%20Stencil%20testing/<br><br>
2. 深度测试：<br><br>
https://learnopengl-cn.github.io/04%20Advanced%20OpenGL/01%20Depth%20testing/<br><br><font size="2"></font><br><font size="2">来源：COCOS</font><br><font size="2">原文：https://mp.weixin.qq.com/s/NGWdIZrasvXqtBI75rw9xg</font><br><br><br>
</td></tr></tbody></table>


  
</div>
            