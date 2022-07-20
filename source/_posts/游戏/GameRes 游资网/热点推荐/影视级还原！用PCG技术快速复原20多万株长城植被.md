
---
title: '影视级还原！用PCG技术快速复原20多万株长城植被'
categories: 
 - 游戏
 - GameRes 游资网
 - 热点推荐
headimg: 'https://di.gameres.com/attachment/forum/202207/11/094721pm7apgus7b7wswgb.gif'
author: GameRes 游资网
comments: false
date: Mon, 11 Jul 2022 00:00:00 GMT
thumbnail: 'https://di.gameres.com/attachment/forum/202207/11/094721pm7apgus7b7wswgb.gif'
---

<div>   
<font color="#808080"><i>以下文章来源于腾讯游戏学堂 ，作者腾讯游戏学堂</i></font><br>
<br>
2022年6月11日，由中国文物保护基金会指导，腾讯公益慈善基金会等众多长城保护研究专业机构及社会团体共同参与，由 腾讯IEG CROS研发效能部数字文化实验室 打造的“云游长城”正式上线。这是全球首次通过云游戏技术，实现大规模的文化遗产毫米级高精度、沉浸交互式的数字还原，成为前沿科技和数字技术在文保领域实现创新应用的又一标志性范例。本期将详细为大家揭秘超大规模文化遗产数字背后的PCG技术。<br>
<br>
<strong><font color="#de5650">一、项目背景</font></strong><br>
<br>
《云游长城》是一个结合Photogrammerty、超大场景渲染、云游虚拟化等技术，将长城数字化并快速应用落地的项目，用卫星云图来做地形参考的广袤场景。植被生成的规模以数十万计，在不同高低落差、不同种类的植被错落有致的情况下，要还原度极高的覆盖在写实地貌当中。这在PCG出现之前，是每个3D地形编辑美术的噩梦。<br>
<br>
不仅如此，为了让用户有更加极致的影视级体验，除了毫米级别精度的长城主体外，还加入了随时清晨、中午、傍晚、深夜光影实时调节，动态的植被，以及鸟虫云雾等特效。这导致每个模块的算力非常紧张。要保证影视级的效果，而且要稳定流畅的运行这对整个技术团队都是不小的挑战。<br>
<br>
<strong><font color="#de5650">二、最终上线的效果</font></strong><br>
<br>
只要信念够大办法总比困难多，经过团队的不断努力，技术与美术的不断磨合，最终于今年6月11日“文化和自然遗产日”正式上线。这是最终上线的效果，下面将详细介绍技术和思路。<br>
<br>
<strong><font color="#de5650">三、技术详解</font></strong><br>
<br>
腾讯游戏CROS积累了多年的游戏研发能力，包括PCG（Procedural Content Generation）程序化内容生成技术，《云游长城》的植被分布就是运用了PCG实现的，因为PCG可以更好的处理巨量的数据，加快版本迭代速度。这次搭建的植被生成工具是一个高度整合型的。将植被分布区域的计算、植被生态组合设定、还有最后的散布和优化整合到一起里。<br>
<br>
下面从植被的分布区域、植被组合、植被模型处理这三方面来介绍长城植被的制作细节。<br>
<br>
<strong><font color="#de5650">植被分布区域</font></strong><br>
<br>
根据输入的地形，通过算法可以得到一些比较基础的层，如坡度、高度、曲率、朝向、距离、噪声等。然后可以通过简单的加减乘除得到新的层（自定义层），自定义层同样也可以加入到创建新层的计算中。整个设置的过程只需通过调参即可完成。<br>
<br>
<div align="center"><font size="2"><font color="#808080">
<img aid="1045618" zoomfile="https://di.gameres.com/attachment/forum/202207/11/094721pm7apgus7b7wswgb.gif" data-original="https://di.gameres.com/attachment/forum/202207/11/094721pm7apgus7b7wswgb.gif" width="600" id="aimg_1045618" inpost="1" src="https://di.gameres.com/attachment/forum/202207/11/094721pm7apgus7b7wswgb.gif" referrerpolicy="no-referrer">
</font></font></div><div align="center"><font size="2"><font color="#808080">[ 基础层 ]</font></font></div><div align="center"><font size="2"><font color="#808080"><br>
</font></font></div><div align="center"><font size="2"><font color="#808080">
<img aid="1045619" zoomfile="https://di.gameres.com/attachment/forum/202207/11/094722rbqk7rb3bgguhp1q.gif" data-original="https://di.gameres.com/attachment/forum/202207/11/094722rbqk7rb3bgguhp1q.gif" width="600" id="aimg_1045619" inpost="1" src="https://di.gameres.com/attachment/forum/202207/11/094722rbqk7rb3bgguhp1q.gif" referrerpolicy="no-referrer">
</font></font></div><div align="center"><font size="2"><font color="#808080">[ 自定义层 ]</font></font></div><br>
我们通过这种方式划分出峡谷、山峰、悬崖、岸边、长城周围等区域用于植被分布，这些层同样可以应用到地形的材质上。<br>
<br>
<strong><font color="#de5650">植被生态组合</font></strong><br>
<br>
首先我们拍摄了很多长城现场的照片，通过照片我们可以知道长城周围都有什么类型的植物，分析它们的分布规律，然后将这些分布规律通过程序实现。<br>
<br>
<div align="center"><font size="2"><font color="#808080">
<img aid="1045620" zoomfile="https://di.gameres.com/attachment/forum/202207/11/094722wagz29kig2028bkh.jpg" data-original="https://di.gameres.com/attachment/forum/202207/11/094722wagz29kig2028bkh.jpg" width="600" id="aimg_1045620" inpost="1" src="https://di.gameres.com/attachment/forum/202207/11/094722wagz29kig2028bkh.jpg" referrerpolicy="no-referrer">
</font></font></div><div align="center"><font size="2"><font color="#808080">[ 长城周围树木 ]</font></font></div><div align="center"><font size="2"><font color="#808080"><br>
</font></font></div><div align="center"><font size="2"><font color="#808080">
<img aid="1045621" zoomfile="https://di.gameres.com/attachment/forum/202207/11/094722uoudqa2a2bucoezv.jpg" data-original="https://di.gameres.com/attachment/forum/202207/11/094722uoudqa2a2bucoezv.jpg" width="600" id="aimg_1045621" inpost="1" src="https://di.gameres.com/attachment/forum/202207/11/094722uoudqa2a2bucoezv.jpg" referrerpolicy="no-referrer">
</font></font></div><div align="center"><font size="2"><font color="#808080">[ 长城植被模型 ]</font></font></div><br>
通过定义这些植被的大小、比率、密度可以组合不同的植被组合。另外还可以设置植被之间的依赖关系，例如大树周围有小树，大树底下灌木，灌木周围有杂草等。<br>
<br>
<div align="center"><font size="2"><font color="#808080">
<img aid="1045622" zoomfile="https://di.gameres.com/attachment/forum/202207/11/094723cnajedjce5d55grj.jpg" data-original="https://di.gameres.com/attachment/forum/202207/11/094723cnajedjce5d55grj.jpg" width="600" id="aimg_1045622" inpost="1" src="https://di.gameres.com/attachment/forum/202207/11/094723cnajedjce5d55grj.jpg" referrerpolicy="no-referrer">
</font></font></div><div align="center"><font size="2"><font color="#808080">[ 长城植被组合1 ]</font></font></div><div align="center"><font size="2"><font color="#808080"><br>
</font></font></div><div align="center"><font size="2"><font color="#808080">
<img aid="1045623" zoomfile="https://di.gameres.com/attachment/forum/202207/11/094723fkk7kkz998yo98l7.jpg" data-original="https://di.gameres.com/attachment/forum/202207/11/094723fkk7kkz998yo98l7.jpg" width="600" id="aimg_1045623" inpost="1" src="https://di.gameres.com/attachment/forum/202207/11/094723fkk7kkz998yo98l7.jpg" referrerpolicy="no-referrer">
</font></font></div><div align="center"><font size="2"><font color="#808080">[ 长城植被组合2 ]</font></font></div><div align="center"><font size="2"><font color="#808080"><br>
</font></font></div><div align="center"><font size="2"><font color="#808080">
<img aid="1045624" zoomfile="https://di.gameres.com/attachment/forum/202207/11/094723erzyh7h427hzv272.jpg" data-original="https://di.gameres.com/attachment/forum/202207/11/094723erzyh7h427hzv272.jpg" width="600" id="aimg_1045624" inpost="1" src="https://di.gameres.com/attachment/forum/202207/11/094723erzyh7h427hzv272.jpg" referrerpolicy="no-referrer">
</font></font></div><div align="center"><font size="2"><font color="#808080">[ 长城植被组合3 ]</font></font></div><br>
最后可以将设定好的植被组合应用到之前生成好的植被分布区域，下面的视频演示了植被组合的设置，和快速加载之前保存好的参数设定。<br>
<br>
整套生成规则是通过算法和参数控制的，即使是地形有变动或植被需要替换，只需要让电脑重新计算就好，加快版本迭代的速度。这次场景里大概散布了20万棵植被，整个计算时间在一分钟内。另外配置的好植被组合也可以通过预设文件保存，方便效果复用。<br>
<br>
<strong><font color="#de5650">植被模型处理</font></strong><br>
<br>
LOD减面工具：我们同样将植被减面和LOD生成做成了工具，可以对输入的植被模型进行减面，并创建输出LOD组，设置LOD的screansize，生成簇信息和高度ramp等。<br>
<br>
树叶的减面思路是将uv转pos，然后重新算一2D凸包，或直接用bbox面片，只要能包住之前的点就可以，然后再将pos给到uv，最后extracttransform节点恢复树叶面片的位置。<br>
<br>
<div align="center"><font size="2"><font color="#808080">
<img aid="1045625" zoomfile="https://di.gameres.com/attachment/forum/202207/11/094724mb3e3gfpyq2wyc4k.gif" data-original="https://di.gameres.com/attachment/forum/202207/11/094724mb3e3gfpyq2wyc4k.gif" width="600" id="aimg_1045625" inpost="1" src="https://di.gameres.com/attachment/forum/202207/11/094724mb3e3gfpyq2wyc4k.gif" referrerpolicy="no-referrer">
</font></font></div><div align="center"><font size="2"><font color="#808080">[ 植被减面过程演示 ]</font></font></div><br>
工具包含了减面、删面、缩放叶片、剔除细小叶片和树枝等处理，根据不同的lod等级配置不同的减面设置。另外还可以将树分簇，将簇信息存储在顶点颜色上，可以用于动态偏移。<br>
<br>
<div align="center"><font size="2"><font color="#808080">
<img aid="1045626" zoomfile="https://di.gameres.com/attachment/forum/202207/11/094724n4y40wjc64wcwy57.gif" data-original="https://di.gameres.com/attachment/forum/202207/11/094724n4y40wjc64wcwy57.gif" width="600" id="aimg_1045626" inpost="1" src="https://di.gameres.com/attachment/forum/202207/11/094724n4y40wjc64wcwy57.gif" referrerpolicy="no-referrer">
</font></font></div><div align="center"><font size="2"><font color="#808080">[ 植被簇信息生成演示 ]</font></font></div><div align="center"><font size="2"><font color="#808080"><br>
</font></font></div><div align="center"><font size="2"><font color="#808080">
<img aid="1045627" zoomfile="https://di.gameres.com/attachment/forum/202207/11/094724e402zjqyk49k2j3a.gif" data-original="https://di.gameres.com/attachment/forum/202207/11/094724e402zjqyk49k2j3a.gif" width="320" id="aimg_1045627" inpost="1" src="https://di.gameres.com/attachment/forum/202207/11/094724e402zjqyk49k2j3a.gif" referrerpolicy="no-referrer">
</font></font></div><div align="center"><font size="2"><font color="#808080">[ 结合了簇信息的动态效果 ]</font></font></div><br>
最后一级LOD：长城植被的LOD分了5级，Lod0-Lod4，植被的最后一级LOD是使用Octahedral Impostors。<br>
<br>
<div align="center"><font size="2"><font color="#808080">
<img aid="1045628" zoomfile="https://di.gameres.com/attachment/forum/202207/11/094725z400400uqnyffqny.jpg" data-original="https://di.gameres.com/attachment/forum/202207/11/094725z400400uqnyffqny.jpg" width="384" id="aimg_1045628" inpost="1" src="https://di.gameres.com/attachment/forum/202207/11/094725z400400uqnyffqny.jpg" referrerpolicy="no-referrer">
</font></font></div><div align="center"><font size="2"><font color="#808080">[ 长城植被LOD ]</font></font></div><br>
Octahedral Impostors是从各个方向进行捕捉植被，通过shader在简单的quad模型上绘制采样类似flipbook贴图的不同区间图像来匹配摄像机的视角。<br>
<br>
<div align="center">
<img aid="1045629" zoomfile="https://di.gameres.com/attachment/forum/202207/11/094725tq98u3sef8fqqmdq.jpg" data-original="https://di.gameres.com/attachment/forum/202207/11/094725tq98u3sef8fqqmdq.jpg" width="533" id="aimg_1045629" inpost="1" src="https://di.gameres.com/attachment/forum/202207/11/094725tq98u3sef8fqqmdq.jpg" referrerpolicy="no-referrer">
</div><div align="center"><font size="2"><font color="#808080">[ Ryan Brucks 的impostor捕获示意图 ]</font></font></div><br>
<div align="center">
<img aid="1045630" zoomfile="https://di.gameres.com/attachment/forum/202207/11/094725n2wdqnesd12fw4je.jpg" data-original="https://di.gameres.com/attachment/forum/202207/11/094725n2wdqnesd12fw4je.jpg" width="600" id="aimg_1045630" inpost="1" src="https://di.gameres.com/attachment/forum/202207/11/094725n2wdqnesd12fw4je.jpg" referrerpolicy="no-referrer">
</div><div align="center"><font size="2"><font color="#808080">[ 云游长城的植被impostor贴图 ]</font></font></div><br>
<div align="center">
<img aid="1045631" zoomfile="https://di.gameres.com/attachment/forum/202207/11/094726akkm6u84wnw26w8p.gif" data-original="https://di.gameres.com/attachment/forum/202207/11/094726akkm6u84wnw26w8p.gif" width="320" id="aimg_1045631" inpost="1" src="https://di.gameres.com/attachment/forum/202207/11/094726akkm6u84wnw26w8p.gif" referrerpolicy="no-referrer">
</div><div align="center"><font size="2"><font color="#808080">[ 长城植被的impostor ]</font></font></div><br>
效果和性能往往不能两全，为了能实现最大化在算力与视效上的平衡，在云游戏上实机运行的正式版植被，团队做了大量调优。欣喜的是，最终我们在有限的算力下，实现了较好的图像呈现。<br>
<br>
以上就是在云游长城项目当中植树造林的一次实践历程。长城是第一步，后面还有中轴线、藏经洞...... 我们将继续探索PCG技术在更多的文保项目中的运用。最后，很荣幸能参与云游长城项目，为文保事业尽绵薄之力。<br>
<br>
<font size="2"><font color="#808080">引用&参考</font></font><br>
<font size="2"><font color="#808080">[1]Octahedral Impostors烘培插件Ryan Brucks’impostor: https://shaderbits.com/blog/octahedral-impostors</font></font><br>
<font size="2"><font color="#808080">[2]The Vegetation of Horizon Zero Dawn: https://www.youtube.com/watch?v=wavnKZNSYqU</font></font><br>
<font size="2"><font color="#808080">[3]Procedural World Generation of Far Cry 5: https://www.youtube.com/watch?v=JBp8zvLVsgg</font></font><br>
<br>
<font size="2"><font color="#808080">来源：腾讯游戏学堂</font></font><br>
<br>
  
</div>
            