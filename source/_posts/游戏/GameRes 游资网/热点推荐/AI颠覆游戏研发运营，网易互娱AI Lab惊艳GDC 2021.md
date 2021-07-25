
---
title: 'AI颠覆游戏研发运营，网易互娱AI Lab惊艳GDC 2021'
categories: 
 - 游戏
 - GameRes 游资网
 - 热点推荐
headimg: 'https://di.gameres.com/attachment/forum/202107/23/112324irepeeol4pdpoxxr.png'
author: GameRes 游资网
comments: false
date: Fri, 23 Jul 2021 00:00:00 GMT
thumbnail: 'https://di.gameres.com/attachment/forum/202107/23/112324irepeeol4pdpoxxr.png'
---

<div>   
<table cellspacing="0" cellpadding="0"><tbody><tr><td class="t_f" id="postmessage_2506257">
近日，游戏界的年度盛会GDC 2021于线上召开，网易互娱AI Lab在大会上向来自世界各地的数万名开发者们分享了其在游戏研发运营领域的两项研究成果——“3D Parametric Face Model and its Applications in Games（三维参数化人头模型及其在游戏中的应用）”和“Game Environment Guardian（游戏环境卫士）”。这两项成果分别入选了GDC 2021 Summit和GDC 2021 Core，前者更是唯一入选本届大会的3D人头重建方向的提案，彰显了网易互娱AI Lab在 AI与游戏领域的综合技术实力，也印证了其近年来在游戏领域的技术探索和突破获得了业界权威的认可。<br>
<br>
<strong><font color="#de5650">三维参数化人脸模型：研制创新工具，提升美术效率</font></strong><br>
<br>
画面是玩家对游戏的第一印象，因此精美的游戏画面一直是各大游戏厂商凸显游戏品质的竞技场，其中角色面部表现更是该竞技场上最能体现实力和拉开差距的环节。在精美的角色面部效果背后，暗藏着高质量模型、绑定、动画等一系列面部美术资产，且随着游戏体量的迅速增长，为游戏内每个角色都制作高质量的面部资产需要投入极高的成本。近年来三维参数化人脸模型（3DMM）快速发展，被广泛应用于人脸重建、表情回归等问题。理论上，一套高质量的参数化人脸模型、配合相关AI和图形算法，可以极大提升游戏角色面部资源的生产效率。<br>
<br>
遗憾的是，当前业界主流的三维参数化人脸模型（如Basel Face Model、FLAME、Surrey Morphable Face Model等）都以学术应用为主，主要作为某种中间表征为算法提供关于人脸的三维形状先验信息，在其参数空间中采样出的人头模型本身的质量（精度、完整度、布线质量等）远远达不到游戏行业的美术资源标准。为了解决这一问题，网易互娱AI Lab结合当前游戏工业界的实际需求，通过高精度三维扫描设备采集了涵盖不同性别、不同年龄段的500个亚洲人头数据，结合自研算法和专业扫描建模流程对数据进行修复和重拓扑，从而构建了一套针对东亚人脸的、符合游戏资源标准的高质量三维参数化人脸模型。该模型包含四个维度的参数空间：能够生成不同形状人头的形状参数空间、能够调整局部五官特征的面部属性参数空间、可以改变面部表情的表情参数空间，以及可以修改面部纹理和几何细节的外观参数化空间。<br>
<br>
但让AI深入游戏的研发与制作，关键还在于AI技术的工具化。围绕这套三维参数化人脸模型，针对不同的应用场景，网易互娱AI Lab打造了一系列用于提升面部资源生产效率的美术工具：<br>
<br>
1．人头重建：基于单视角或多视角照片生成高精度三维头部模型，并且美术模型师还可以从形状、表情、面部属性和外观四个维度对自动生成的模型进行二次编辑。利用该工具，传统上需要7-20人/天的工作可以在1分钟内快速完成。<br>
<br>
<div align="center">
<img id="aimg_994903" aid="994903" zoomfile="https://di.gameres.com/attachment/forum/202107/23/112324irepeeol4pdpoxxr.png" data-original="https://di.gameres.com/attachment/forum/202107/23/112324irepeeol4pdpoxxr.png" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202107/23/112324irepeeol4pdpoxxr.png" referrerpolicy="no-referrer">
</div><br>
2. 形状/表情迁移：给定任意游戏角色的头部模型，既可以批量生成与该模型风格相近、脸型/五官存在一定变化的模型（形状迁移），也可以批量生成该模型的各种表情Blendshape（表情迁移）。游戏项目组只需要制作一个基础人头模型，就能以极低的成本快速实现千人千面的效果，有效避免大世界游戏中NPC样貌的千篇一律。<br>
<br>
<div align="center">
<img id="aimg_994904" aid="994904" zoomfile="https://di.gameres.com/attachment/forum/202107/23/112324p2xr7gkmopecazrn.png" data-original="https://di.gameres.com/attachment/forum/202107/23/112324p2xr7gkmopecazrn.png" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202107/23/112324p2xr7gkmopecazrn.png" referrerpolicy="no-referrer">
</div><br>
3. 面部表情捕捉：网易互娱AI Lab还打造了一套完全自研、全平台单核单线程实时的轻量级面部表情捕捉套件，仅需一个普通摄像头，就可以完成从真人到游戏角色的表情精准迁移。该技术不仅能大幅提升面部动画资源的制作效率，还可以为虚拟偶像直播和游戏内玩法提供支持。<br>
<br>
<div align="center">
<img id="aimg_994905" aid="994905" zoomfile="https://di.gameres.com/attachment/forum/202107/23/112325odda1bgu2u1aebad.png" data-original="https://di.gameres.com/attachment/forum/202107/23/112325odda1bgu2u1aebad.png" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202107/23/112325odda1bgu2u1aebad.png" referrerpolicy="no-referrer">
</div><div align="center"><font size="2"><font color="#808080">《一梦江湖》颜艺系统（表情包玩法）</font></font></div><br>
<strong><font color="#de5650">游戏敏感信息过滤与舆情平台：打造和谐环境，赋能长线运营</font></strong><br>
<br>
游戏内外，玩家社交将产生大量的信息：一方面，游戏内的聊天公屏、对局语音等交流渠道内，违禁信息屡禁不止，这将给游戏营收、口碑和玩家体验造成难以估量的损失；另一方面，游戏外的论坛、社群等交流平台的内容是玩家反馈的一手资料，对于实时掌握游戏舆情和危机预警而言具有重大价值。那么，如何有效打击敏感信息，深入玩家群体，赋能长线运营？网易互娱AI Lab在大会上分享了其在违规信息过滤和舆情分析方面的最新进展。<br>
<br>
精准打击游戏内的敏感内容存在多重挑战：这些信息不仅覆盖种类甚广、形式多样，还一直在不断迭代变化，并且不同游戏的用词也存在着差异。过去，针对文本信息一般采用的是关键词识别，但这种方式难以应对变体、谐音等形式。网易互娱AI Lab基于机器学习的方法，采用卷积神经网络和BERT预训练语言模型有效识别文字变体，并构建了一套半自动新词挖掘系统，能够随着黑话的变化自动迭代。而针对语音形式的信息，以往采用的是自动语音识别（ASR）技术，该技术需要将语音解码后对文本进行分类，会耗费大量计算资源，实时性也较差。为了提升效率，网易互娱AI Lab以端到端模型在音素层面直接进行分类，该方法能在准确识别的同时大幅提高速度。此外，网易互娱AI Lab还可通过识别账号异常行为排查灰黑产账户，帮助及时减少游戏损失。目前，该系统已经成功应用于多款网易游戏，日均请求次数超过2000万，准确率超过95%。<br>
<br>
<div align="center">
<img id="aimg_994906" aid="994906" zoomfile="https://di.gameres.com/attachment/forum/202107/23/112328jzycca9c4r99udjt.png" data-original="https://di.gameres.com/attachment/forum/202107/23/112328jzycca9c4r99udjt.png" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202107/23/112328jzycca9c4r99udjt.png" referrerpolicy="no-referrer">
</div><br>
敏感信息的实时高效过滤帮助游戏长线运营打造了更加和谐的游戏环境，改善了玩家的游戏体验，而网易互娱AI Lab的舆情管理平台则为游戏运营提供了及时了解玩家的可视化数据平台，以便及时应对和防范舆情风险。该舆情平台不仅能够自动抓取游戏内所有频道和自营社区的内容，实现自动分类聚类，其情绪分析模块还可进行文本细粒度情感分析，辨别评论的正负面倾向。此外，系统还内置了舆情实时预警功能和热点分析功能，能够帮助游戏工作室及时应对舆情风险、一键掌握热点话题。目前，该舆情平台已为20多款网易热门游戏提供支持。<br>
<br>
<div align="center">
<img id="aimg_994907" aid="994907" zoomfile="https://di.gameres.com/attachment/forum/202107/23/112329nzndd4994qzhvyvv.png" data-original="https://di.gameres.com/attachment/forum/202107/23/112329nzndd4994qzhvyvv.png" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202107/23/112329nzndd4994qzhvyvv.png" referrerpolicy="no-referrer">
</div><br>
网易互娱AI Lab成立于2017年，是游戏行业领先的人工智能实验室，致力于计算机视觉、语音和自然语言处理，以及强化学习等技术在游戏场景下的研究、应用和落地，实验室旨在通过AI技术助力互娱旗下热门游戏及产品的技术升级。正如在本届GDC大会上展示的一样，网易互娱AI Lab近年来不断探索学术的边界，仰望星空亦脚踏实地，将AI成果落地于游戏研发运营的各个环节，帮助解决业务痛点，提升制作效率。目前，其研发成果已经应用于《大话西游》、《一梦江湖》、《第五人格》等多款网易热门游戏之中。未来，网易互娱AI Lab将继续突破技术壁垒，为更多游戏提供支持，助力游戏产业革新。<br>
<br>
</td></tr></tbody></table>



  
</div>
            