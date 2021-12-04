
---
title: '超实用！Cocos 可视化 3D 图形渲染调试工具包，精准排查和定位问题'
categories: 
 - 游戏
 - GameRes 游资网
 - 列表
headimg: 'https://di.gameres.com/attachment/forum/202111/04/101801x1jrfaweb05ggp5u.jpg'
author: GameRes 游资网
comments: false
date: Thu, 04 Nov 2021 00:00:00 GMT
thumbnail: 'https://di.gameres.com/attachment/forum/202111/04/101801x1jrfaweb05ggp5u.jpg'
---

<div>   
<table cellspacing="0" cellpadding="0"><tbody><tr><td class="t_f" id="postmessage_2517877">
<strong>引言：</strong><br><br>
减少 DrawCall 是游戏在性能优化时的常用方法之一。对 2D 项目来说这个方法十分有效，但是在 3D 项目中就不完全适用了，甚至有时候，减少 DrawCall 反而还会增加 CPU 的开销。<br><br>
Cocos 首席布道师麒麟子今天将同大家分享一个可视化 3D 图形调试工具，这个工具能让我们简单快速地定位问题，有的放矢进行图形渲染调试与优化。<br><br><div align="center">
<img id="aimg_1019541" aid="1019541" zoomfile="https://di.gameres.com/attachment/forum/202111/04/101801x1jrfaweb05ggp5u.jpg" data-original="https://di.gameres.com/attachment/forum/202111/04/101801x1jrfaweb05ggp5u.jpg" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202111/04/101801x1jrfaweb05ggp5u.jpg" referrerpolicy="no-referrer">
</div>
<br>
上面的丑图，各位可能看不出来是干嘛的。不用担心，阅读完本文后，保证解除你所有疑惑。<br><br>
在开始我们的正题之前，我想问问，大家有没有遇到过下面这些问题：<br><br>
游戏渲染性能优化，就只有 DrawCall 吗？<br><br>
材质系统中的合批(Batching)和几何体实例化(GPU Instancing)有何异同？<br><br>
Cocos Creator 3.3 赛博朋克 DEMO 中的 Overdraw 功能是什么？<br><br>
学 3D 就是学写 Shader 吗？会写 Shader 真的就可以为所欲为了吗？<br><br>
什么是引擎中台，什么是 TA？<br><br>
为什么我已熟知某 3D 引擎 API，转过来用 Cocos Creator 的 3D 还是那么难？<br><br>
为什么我用 Cocos Creator 做游戏这么多年了，用 Cocos Creator 做 3D 还是很困难？<br><br>
由于这篇文章主要是做 KylinsGraphicsDebugger 功能说明，上面的问题不会逐一回答，对上面问题有兴趣的朋友，可以关注文末麒麟子的公众号，我会在之后的文章中为大家一一解答。等不及的朋友也可以加麒麟子个人微信，麒麟子期待和大家交流探讨相关问题。<br><br>
在你成为3D大牛的路上，这几个知识点是绕不开的。在没有需求的时候，你可以不买。但请记住它的名字：KylinsGraphicsDebugger，相信你有一天一定会用得上。<br><br><strong><font color="#de5650">KylinsGraphicsDebugger</font></strong><br><strong><font color="#de5650"><br></font></strong><br><strong><font color="#de5650">适合以下两种情形：</font></strong><br><br>
想要深入研究 3D 游戏优化方案的开发者或团队；<br><br>
想要通过一套有效的工具快速解决问题的开发者或团队。<br><br><strong><font color="#de5650">KylinsGraphicsDebugger</font></strong><br><strong><font color="#de5650"><br></font></strong><br><strong><font color="#de5650">可以使你：</font></strong><br><br>
精确制定 3D 项目中相关模型使用的贴图大小规范；<br><br>
精确找到 3D 项目中贴图尺寸过大的地方，减少内存开销和包体大小；<br><br>
精确定位场景中的 3D 模型材质批次，找出 DrawCall 问题；<br><br>
快速找到 Overdraw 超负荷的位置，进一步提升中低端机渲染性能；<br><br>
配合相关文章，深入理解工具中使用的知识，成为 3D 游戏性能优化大师；<br><br>
包含生成带 Mipmap 的纹理的代码；<br><br>
包含创建 Mesh 的代码；<br><br>
包含全局替换和恢复模型材质的代码。<br><br>
在做 2D 项目的时候，我们一提到性能优化时，说得最多的就是减少 DrawCall。<br><br>
由于 2D 游戏中，GPU 很难成为瓶颈，所以解决掉 DrawCall 问题，基本上就解决了80%的渲染性能问题。但如今越来越多的 3D 项目出现，越来越多的开发者开始发现，DrawCall 并不完全适用了，甚至有时候，减少 DrawCall 反而增加了 CPU 的开销。特别对于一些从 2D 项目转到 3D 项目的开发者或者团队，这个情况尤为明显。<br><br>
那怎么办呢？KylinsGraphicsDebugger 就是采用可视化的方式，辅助大家排查和定位问题。<br><br>
注意看下图中右上角那些选项，我们将逐一展示它们的功能：<br><br><div align="center">
<img id="aimg_1019542" aid="1019542" zoomfile="https://di.gameres.com/attachment/forum/202111/04/101801nkettnuf9n202mam.jpg" data-original="https://di.gameres.com/attachment/forum/202111/04/101801nkettnuf9n202mam.jpg" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202111/04/101801nkettnuf9n202mam.jpg" referrerpolicy="no-referrer">
</div>
<br><strong><font color="#de5650">一、主要功能</font></strong><br><br>
支持原生 H5 小游戏 平台；<br><br>
无需修改引擎管线；<br><br>
对场景节点树零污染，只需复制到 resources 目录，简单调用 API 即可使用；<br><br>
支持 Mipmap Levels 查看，定制美术规范，找到分辨率过剩的纹理；<br><br>
支持材质实例 ID 显示，可配合 RenderDoc,spector.JS 等工具快速定位 DrawCall 问题；<br><br>
支持 Overdraw 经典模式和 Overdraw Pro 两种显示方式，可快速定位场景中 Overdraw 超过一定数量的地方；<br><br>
以上特性可单独对某个节点以及其子节点使用（如果要全体作用，只需要传入场景根节点即可），方便聚焦问题。<br><br><strong><font color="#de5650">二、基本信息</font></strong><br><br>
引擎版本：Cocos Creator 3.3.2<br><br>
编程语言：TypeScript<br><br>
KylinsGraphicsDebugger 资源链接、操作和开发文档，详见 Cocos Store 资源页（点击文末【阅读原文】跳转）：<br><br>
https://store.cocos.com/app/detail/3342<br><br><font color="#de5650"><strong>三、DEMO 使用</strong></font><br><br>
DEMO 面板中提供了效果切换、色卡对比等功能。DEMO 中的调节面板，不依赖于任何框架，只和 KylinsGraphicsDebugger 相关，如果有需要，开发者可以将此面板集成到自己的项目中进行参数调试。<br><br><strong><font color="#de5650">如何找到适合对象的贴图大小</font></strong><br><br><strong>1、 在常规视角下，开启 mipmaps 的显示，如下图所示：</strong><br><br><div align="center"><font size="2">
<img id="aimg_1019543" aid="1019543" zoomfile="https://di.gameres.com/attachment/forum/202111/04/101802ij5u1sts7t8soos3.jpg" data-original="https://di.gameres.com/attachment/forum/202111/04/101802ij5u1sts7t8soos3.jpg" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202111/04/101802ij5u1sts7t8soos3.jpg" referrerpolicy="no-referrer"></font></div>
<div align="center"><font size="2">常规视角是指游戏中使用最多的视角</font></div>
<br><strong>2、将对象颜色与色卡对比，找出适合的尺寸</strong><br><br><div align="center"><font size="2">
<img id="aimg_1019544" aid="1019544" zoomfile="https://di.gameres.com/attachment/forum/202111/04/101802zcrcnazxnbhh4yin.jpg" data-original="https://di.gameres.com/attachment/forum/202111/04/101802zcrcnazxnbhh4yin.jpg" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202111/04/101802zcrcnazxnbhh4yin.jpg" referrerpolicy="no-referrer"></font></div>
<div align="center"><font size="2">如图所示，三个小球的空间关系</font></div>
<br>
图中士兵和小球的颜色以黄色和绿色为主，那说明士兵的贴图最多使用256x256就够了，超过就是浪费。<br><br>
注：这个显示，只和像素大小有关，与模型是否缩放、远近无关。<br><br>
如图中的两个球体，一离得很近，一个离得很远并且有缩放。但由于两个球体在屏幕上的像素大小一致，所以他们呈现了相同的颜色。而另一个更小的球，主色为黄色，表示可以采用更低的分辨率。<br><br>
由于三个球使用了同样的材质，所以小球的纹理贴图使用256x256就可以了。但这个球的绿色已经泛黄，如果球代表的物体要求不高的话,128x128也是可以的。每降一级，可以省下75%的资源开销，还是很划得来的。<br><br><strong><font color="#de5650">如何找到 Overdraw 严重的地方</font></strong><br><br><strong>1、将半透明特效开启 Overdraw</strong><br><br>
据项目需要来决定，有时候也需要检查非透明物体。<br><br><div align="center"><font size="2">
<img id="aimg_1019545" aid="1019545" zoomfile="https://di.gameres.com/attachment/forum/202111/04/101802t111jlyflf1hn0rr.jpg" data-original="https://di.gameres.com/attachment/forum/202111/04/101802t111jlyflf1hn0rr.jpg" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202111/04/101802t111jlyflf1hn0rr.jpg" referrerpolicy="no-referrer"></font></div>
<div align="center"><font size="2">Overdraw 经典显示，颜色越红越亮，表示 Overdraw 越多</font></div>
<div align="center"><font size="2"><br></font></div>
<div align="center"><font size="2">
<img id="aimg_1019546" aid="1019546" zoomfile="https://di.gameres.com/attachment/forum/202111/04/101803jqiu83yuii9i44py.jpg" data-original="https://di.gameres.com/attachment/forum/202111/04/101803jqiu83yuii9i44py.jpg" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202111/04/101803jqiu83yuii9i44py.jpg" referrerpolicy="no-referrer"></font></div>
<div align="center"><font size="2">Overdraw Pro 显示，不同颜色代表不同的 Overdraw 次数</font></div>
<br>
本方案保留了 Overdraw 经典显示方式，以照顾 Overdraw 查看非常有经验的朋友们。但只通过颜色来对比的话，很难找出问题。比如我们如果要找到 Overdraw 大于5的地方，就很难了。<br><br><strong>2、 将各部分颜色与色卡对比</strong><br><br>
Overdraw Pro 采用了色卡对比方式，将对应区域与色卡对比，即可找出相关区域。<br><br>
比如，在本例中，如果我们要找出 Overdraw 大于等于10的区域，那么红色部分就是需要关注的。如果我们要找出 Overdraw 大于等于5的区域，那么红色、紫色、绿色、橙色、黄色、蓝色区域就是需要关注的。<br><br><strong><font color="#de5650">材质 ID 是拿来干什么的？</font></strong><br><br><div align="center"><font size="2">
<img id="aimg_1019547" aid="1019547" zoomfile="https://di.gameres.com/attachment/forum/202111/04/101803ueuauscyz7q6lzxa.jpg" data-original="https://di.gameres.com/attachment/forum/202111/04/101803ueuauscyz7q6lzxa.jpg" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202111/04/101803ueuauscyz7q6lzxa.jpg" referrerpolicy="no-referrer"></font></div>
<div align="center"><font size="2">材质 ID 显示，同一颜色，表示使用了同一个材质</font></div>
<br>
我们给每一个材质实例设置了一个颜色，在上图中，如果两个对象使用了同一个颜色，表示他们使用的是同一个材质。<br><br>
此方案可以用在以下几个地方：<br><br>
找出能够执行 Batching、GPU Instancing 的对象；<br><br>
检查材质使用规范，找出能够使用同一个材质就能做到，却使用了多个材质的地方；<br><br>
找出 Batching，GPU Instancing 失败的原因（可能是材质不小心被改到了，比如本来应该使用 .sharedMaterial 的地方，写成了 .material）。<br><br>
由于材质 ID 对应的颜色是随机的，可能出现相近难以辨别的情况，因此提供了 reset colors 按钮，重新随机所有颜色。<br><font size="2"><br></font><br><font size="2"></font><br><font size="2">来源：COCOS</font><br><font size="2">原文：https://mp.weixin.qq.com/s/g22ealeBbHhUOGGlf0oWBw</font><br><br><br>
</td></tr></tbody></table>


  
</div>
            