
---
title: '这不是纪录片，Unity再度发布高清实时炫技短片《Lion》'
categories: 
 - 游戏
 - GameRes 游资网
 - 列表
headimg: 'https://di.gameres.com/attachment/forum/202208/12/151506mbl14zi6l49rm9o1.gif'
author: GameRes 游资网
comments: false
date: Fri, 12 Aug 2022 00:00:00 GMT
thumbnail: 'https://di.gameres.com/attachment/forum/202208/12/151506mbl14zi6l49rm9o1.gif'
---

<div>   
自去年 Unity 收购了 Wētā 和 Ziva 等艺术工具起，如何将这些前沿工具整合进 Unity 编辑器，赋能创作者的创作流程，就成为了我们工作的重点。近期，Unity 发布的全新实时 3D 炫技之作《Lion》给出了答案。<br>
<br>
《Lion》是 Unity 艺术工具又一关键里程碑，该作首次集结了 Wētā Digital、Ziva、SpeedTree、SyncSketch 和 Unity Editor 的艺术工具，让艺术家、开发者们能够实现比真实还真实的实时高清图像。<br>
<br>
<div align="center"><ignore_js_op><span id="flv_w8P"></span></ignore_js_op></div><br>
该视频展示了用 Wētā Digital、SpeedTree、Ziva、SyncSketch 和 Unity Editor 艺术工具创建的内容——项目目前已经成为实时管线演示的一部分，可在消费级硬件上体验，能够在 PlayStation 5® 上以 4K 的 30 帧运行。<br>
<br>
原离线演示的资产是由 Monster Emporium Animation School 的学生制作的，包含还原真实尺寸、使用 Ziva VFX 生物力学弹性体解算器模拟的躯体柔软的狮子。<br>
<br>
原离线演示的资产：<br>
<br>
https://www.monsteremporium.co.uk/<br>
<br>
<div align="center"><font size="2"><font color="#808080">
<img aid="1049956" zoomfile="https://di.gameres.com/attachment/forum/202208/12/151506mbl14zi6l49rm9o1.gif" data-original="https://di.gameres.com/attachment/forum/202208/12/151506mbl14zi6l49rm9o1.gif" width="480" id="aimg_1049956" inpost="1" src="https://di.gameres.com/attachment/forum/202208/12/151506mbl14zi6l49rm9o1.gif" referrerpolicy="no-referrer">
</font></font></div><div align="center"><font size="2"><font color="#808080">Ziva VFX模拟幼狮坐下的序列</font></font></div><br>
场景随后会被更新成高性能的实时体验。<br>
<br>
狮子资产使用了 Ziva RT 机器学习变形以及新的 Ziva RT Unity Player（预览版），可以动态执行动画，以提供保真度最高的形变。<br>
<br>
<div align="center"><font size="2"><font color="#808080">
<img aid="1049957" zoomfile="https://di.gameres.com/attachment/forum/202208/12/151512ya6b1r2ramfz16zt.gif" data-original="https://di.gameres.com/attachment/forum/202208/12/151512ya6b1r2ramfz16zt.gif" width="480" id="aimg_1049957" inpost="1" src="https://di.gameres.com/attachment/forum/202208/12/151512ya6b1r2ramfz16zt.gif" referrerpolicy="no-referrer">
</font></font></div><div align="center"><font size="2"><font color="#808080">Ziva RT带来的变形效果可以直接用于最终成品，它还可以加快用工具评估动画装配的速度，加快DCC迭代流程。在这个例子中，我们使用了Ziva VFX 2.0准静态积分器训练Ziva RT，它提供了准确和稳健的结果，是训练实时形变的理想选择。</font></font></div><div align="center"><font size="2"><font color="#808080"><br>
</font></font></div><div align="center"><font size="2"><font color="#808080">
<img aid="1049958" zoomfile="https://di.gameres.com/attachment/forum/202208/12/151515pz61p79ypx7l7zc2.gif" data-original="https://di.gameres.com/attachment/forum/202208/12/151515pz61p79ypx7l7zc2.gif" width="480" id="aimg_1049958" inpost="1" src="https://di.gameres.com/attachment/forum/202208/12/151515pz61p79ypx7l7zc2.gif" referrerpolicy="no-referrer">
</font></font></div><div align="center"><font size="2"><font color="#808080">将高保真变形与Ziva RT和通常在游戏中使用的更传统的剥皮动画进行比较。肌肉组织和软组织的差异在小熊的轮廓和肩胛骨下特别明显。</font></font></div><br>
为了在运行时获得最佳性能，Ziva RT Unity Player 能并行执行 SIMD 优化后的代码，并利用 Unity 的 Burst 技术实时完成动态互动的变形。<br>
<br>
新演示的环境还使用了 SpeedTree 的植被。<br>
<br>
我们先用 SpeedTree Cinema 创建资产，针对实时使用进行优化，在狮子附近添加一些尘土飞扬的草丛，并在地平线上打造了一个非洲标志性可可豆木的形状。这些数据将输出为带有高分辨率纹理的 Game FBX，让植物资产的分辨率能与制作精细的生物们相匹配。<br>
<br>
<div align="center"><font size="2"><font color="#808080">
<img aid="1049959" zoomfile="https://di.gameres.com/attachment/forum/202208/12/151515y7kxpxgxs9km9jyl.jpg" data-original="https://di.gameres.com/attachment/forum/202208/12/151515y7kxpxgxs9km9jyl.jpg" width="600" id="aimg_1049959" inpost="1" src="https://di.gameres.com/attachment/forum/202208/12/151515y7kxpxgxs9km9jyl.jpg" referrerpolicy="no-referrer">
</font></font></div><div align="center"><font size="2"><font color="#808080">一点点植被有助于构图、能让环境更生动。</font></font></div><div align="center"><font size="2"><font color="#808080"><br>
</font></font></div><div align="center"><font size="2"><font color="#808080">
<img aid="1049960" zoomfile="https://di.gameres.com/attachment/forum/202208/12/151521d4s42gp48swdl2l4.jpg" data-original="https://di.gameres.com/attachment/forum/202208/12/151521d4s42gp48swdl2l4.jpg" width="600" id="aimg_1049960" inpost="1" src="https://di.gameres.com/attachment/forum/202208/12/151521d4s42gp48swdl2l4.jpg" referrerpolicy="no-referrer">
</font></font></div><div align="center"><font size="2"><font color="#808080">SpeedTree资产</font></font></div><br>
为了增强写实感，我们用 Wētā Digital 的毛发和皮毛梳理工具 Wig（pre-alpha）作为 Ziva 形变技术的补充，并为制作“大猫咪”和幼崽的鬃毛、皮毛，提供了更高的逼真度和艺术创作空间。<br>
<br>
“Wig 是一种完全不同的工作方式——它实际上是我用过的最快的梳理工具，”Sara Hansen 说，她是《Lion》的Unity技术美术，以前曾为 Wētā FX、DNEG 和其他 VFX 公司制作过成品级毛发。<br>
<br>
“要制作高质量的毛发，用另一套梳理工具我可能得花几个月的时间，用 Wig 则要快得多，制作只需几周时间。有些毛发在其他工具中需要数周的，在 Wig 中只需要一天或几天就能完成，而且质量要好得多，艺术风格的可控性也更强......即使你要遵从详细的艺术指导进行调整，比如调整参考镜头里的某束毛发，你也能用 Wig 轻松完成。”<br>
<br>
<div align="center"><font size="2"><font color="#808080">
<img aid="1049961" zoomfile="https://di.gameres.com/attachment/forum/202208/12/151529gnd5andwt1666wma.gif" data-original="https://di.gameres.com/attachment/forum/202208/12/151529gnd5andwt1666wma.gif" width="480" id="aimg_1049961" inpost="1" src="https://di.gameres.com/attachment/forum/202208/12/151529gnd5andwt1666wma.gif" referrerpolicy="no-referrer">
</font></font></div><div align="center"><font size="2"><font color="#808080">用Wig制作的狮子鬃毛</font></font></div><br>
《Lion》背后的团队来自北美和西欧的多个国家。团队间的远程协作是利用可视化协作工具 SyncSketch 实现的，它提供了实时产品审查和直观迭代的能力。<br>
<br>
<div align="center">
<img aid="1049962" zoomfile="https://di.gameres.com/attachment/forum/202208/12/151530otrh39htcpxhclc3.gif" data-original="https://di.gameres.com/attachment/forum/202208/12/151530otrh39htcpxhclc3.gif" width="480" id="aimg_1049962" inpost="1" src="https://di.gameres.com/attachment/forum/202208/12/151530otrh39htcpxhclc3.gif" referrerpolicy="no-referrer">
</div><div align="center"><font size="2"><font color="#808080">使用SyncSketch云协作工具审查狮子的毛发</font></font></div><br>
这次创意演练验证了 Wētā Digital 的 Wig、Ziva、SpeedTree、SyncSketch 和 Unity Editor 的生产能力，使团队能够快速迭代、全面改进生物和角色制作的工作流程：从绑定到变形到毛发和毛皮附着系统、从渲染到着色等环节，让工作流成为一个连贯的系统。<br>
<br>
“我们希望保证工具能够协同作业，让创作者在每一个环节利用优秀的工作流程来创作角色和生物。因此，我们制作该演示的部分目标是在生产环境中验证 Unity 艺术工具，满足艺术家在日常工作中的种种难题，并使工具和工作流变得更好、更强大，”Unity Technologies 的杰出技术伙伴和首席建筑师、专业艺术和图形创新副总裁 Natalya Tatarchuk 说。<br>
<br>
为了在 PlayStation 5®、Xbox Series X|S® 和 PC 上实时运行高度逼真的生物和场景渲染，我们还开发了一些关键的技术创新。<br>
<br>
项目在一开始就使用了 Unity 的高清渲染管线（HDRP）。我们还使用了全局光照（GI），利用 Adaptive Probe Volumes（适应性探针体积，APV）来照亮狮子周围干旱的沙漠和植被。<br>
<br>
<div align="center">
<img aid="1049963" zoomfile="https://di.gameres.com/attachment/forum/202208/12/151531a330wtom0480mfzw.jpg" data-original="https://di.gameres.com/attachment/forum/202208/12/151531a330wtom0480mfzw.jpg" width="600" id="aimg_1049963" inpost="1" src="https://di.gameres.com/attachment/forum/202208/12/151531a330wtom0480mfzw.jpg" referrerpolicy="no-referrer">
</div><br>
我们还必须解决同时模拟和渲染几百万根发丝的挑战。为此，我们在 HDRP 上进行了一系列重大的性能和视觉清晰度改进。<br>
<br>
其中包括用 GPU 驱动头发簇模拟、使上百万根发丝能够实时地做出反应，该模拟方案已经包含在了 Unity 新发布于 GitHub 上的 Hair System。该模拟方法沿袭了令人惊叹的数字人演示《Enemies》的头发模拟方案，并做了进一步扩展，用 GPU 来更高效地处理更高数量级的发丝。<br>
<br>
Hair System：<br>
<br>
https://github.com/Unity-Technologies/com.unity.demoteam.hair<br>
<br>
对于头发和毛皮的渲染，Unity 的图形开发者们做了重大优化，改进了 HDRP 基于图块的 GPU 软件光栅化算法，转为渲染几百万根独立的头发。该方法还借助了分析式抗锯齿来提高图像流畅度，还为每条发丝添加计算排序好的透明度，还用改进后的物理性头发光照模型来实现电影质量的发丝渲染。<br>
<br>
我们现在可以渲染数百万独立的发丝，所有发丝的动作都相互独立且独特，不会出现瑕疵。新方法可以准确地还原头发的高光部分和光线在软发上的透光现象，比如阳光下的幼狮皮毛或狮子鬃毛。<br>
<br>
以上所有改进，将登陆 2023.1 Tech Stream 版，敬请期待。<br>
<br>
<div align="center">
<img aid="1049964" zoomfile="https://di.gameres.com/attachment/forum/202208/12/151617jw7t6wuuui6s49ub.gif" data-original="https://di.gameres.com/attachment/forum/202208/12/151617jw7t6wuuui6s49ub.gif" width="320" id="aimg_1049964" inpost="1" src="https://di.gameres.com/attachment/forum/202208/12/151617jw7t6wuuui6s49ub.gif" referrerpolicy="no-referrer">
</div><br>
<font size="2"><font color="#808080">来源：Unity官方平台</font></font><br>
<font size="2"><font color="#808080">原文：https://mp.weixin.qq.com/s/xGX7Gd2jAm9Rr8zn_WZ-AQ</font></font><br>
<br>
  
</div>
            