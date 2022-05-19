
---
title: '用AI技术促进美术工业化，制作效率普遍比传统方案提高5-10倍 _ N.GAME'
categories: 
 - 游戏
 - GameRes 游资网
 - 热点推荐
headimg: 'https://di.gameres.com/attachment/forum/202205/06/093404izq2lc96c66dql23.jpg'
author: GameRes 游资网
comments: false
date: Fri, 06 May 2022 00:00:00 GMT
thumbnail: 'https://di.gameres.com/attachment/forum/202205/06/093404izq2lc96c66dql23.jpg'
---

<div>   
2022N.GAME网易游戏开发者峰会于「4月18日-4月21日」举办，本届峰会围绕全新主题“未来已来 The Future is Now”，共设置创意趋势场、技术驱动场、艺术打磨场以及价值探索场四个场次，邀请了20位海内外重磅嘉宾共享行业研发经验、前沿研究成果和未来发展趋势。<br>
<br>
本篇干货来自技术驱动场的嘉宾陈康，他是网易互娱AI Lab的技术经理。<br>
<br>
<div align="center"><font size="2"><font color="#808080">
<img aid="1038504" zoomfile="https://di.gameres.com/attachment/forum/202205/06/093404izq2lc96c66dql23.jpg" data-original="https://di.gameres.com/attachment/forum/202205/06/093404izq2lc96c66dql23.jpg" width="600" id="aimg_1038504" inpost="1" src="https://di.gameres.com/attachment/forum/202205/06/093404izq2lc96c66dql23.jpg" referrerpolicy="no-referrer">
</font></font></div><div align="center"><font size="2"><font color="#808080">嘉宾分享实录（有部分删减与调整）</font></font></div><br>
大家好，我是来自网易互娱AI Lab的陈康，目前负责互娱AI Lab沪杭团队，以及图形学、3D视觉和语音方向的技术研发和落地。<br>
<br>
很高兴有这个机会给大家分享一下我们部门从17年底成立到现在，基于AI的美术资源生产方面做过的尝试。<br>
<br>
<strong><font color="#de5650">常见美术资产的生产过程</font></strong><br>
<br>
首先，什么是美术资源呢？在游戏行业，其专有名词叫“美术资产”。<br>
<br>
<div align="center">
<img aid="1038505" zoomfile="https://di.gameres.com/attachment/forum/202205/06/093405g3ncq1q1n691clt8.jpg" data-original="https://di.gameres.com/attachment/forum/202205/06/093405g3ncq1q1n691clt8.jpg" width="600" id="aimg_1038505" inpost="1" src="https://di.gameres.com/attachment/forum/202205/06/093405g3ncq1q1n691clt8.jpg" referrerpolicy="no-referrer">
</div><br>
以《一梦江湖》和《王牌竞速》两款游戏为例。在艺术风格上有着明显差异，前者偏古风，后者偏现代。但共同点是，你在画面里看到的所有东西，比如人物、衣服、建筑、植被、甚至车辆、以及界面上的按钮图标。<br>
<br>
这些都是美术同学在DCC软件或者游戏引擎中制作出来的，所以都属于美术资产。<br>
<br>
游戏行业发展到今天，在美术资产制作方面，已经形成了一套非常成熟的工业化、流水线生产的解决方案。<br>
<br>
接下来，以我们部门的虚拟技术代言人，同时也是峰会的虚拟主持人i.F.为例。给大家简单介绍一下常见美术资产的制作过程。<br>
<br>
假设你作为一名策划同学，想要美术帮你制作一个这样的角色，你会怎么跟他表达需求呢？你可能会说想要活泼可爱的二次元妹子，处于青春期的年龄段、可能性格有点呆萌。<br>
<br>
但这种描述其实都是很主观、抽象的。比如都是二次元，《阴阳师》和《原神》的二次元就有很大差异。基于这种模糊的描述，美术是没法直接制作三维模型的。<br>
<br>
因为在这过程中肯定需要不停地迭代需求，甚至有可能推翻重做。在三维模型环节进行这种角色设计层面的迭代，成本是非常高的。<br>
<br>
所以，策划的需求一般会先给到原画师，原画师会把这些抽象的描述转化成具体的形象。所有形象设计层面的修改和迭代都是在原画阶段完成的。<br>
<br>
<div align="center">
<img aid="1038506" zoomfile="https://di.gameres.com/attachment/forum/202205/06/093405dcch3h6lvlgchzjc.jpg" data-original="https://di.gameres.com/attachment/forum/202205/06/093405dcch3h6lvlgchzjc.jpg" width="600" id="aimg_1038506" inpost="1" src="https://di.gameres.com/attachment/forum/202205/06/093405dcch3h6lvlgchzjc.jpg" referrerpolicy="no-referrer">
</div><br>
这边展示的就是i.F.的角色原画。在设计过程中，原画师肯定会融入的自己理解，提出修改方案。因为在这个领域美术要比策划专业的多。<br>
<br>
比如i.F.这个形象，头上像兔子耳朵一样的耳机，就是原画同学自己设计出来的。因为我们需要一个青春可爱的技术代言人，这就可以在保持角色可爱风格的同时，体现出一定科技元素。<br>
<br>
角色原画设定图完善后，就会进入模型环节。模型师会参考这个形象制作三维模型和对应的材质贴图。<br>
<br>
<div align="center">
<img aid="1038507" zoomfile="https://di.gameres.com/attachment/forum/202205/06/093405x4hdxh94c0nc01v9.jpg" data-original="https://di.gameres.com/attachment/forum/202205/06/093405x4hdxh94c0nc01v9.jpg" width="600" id="aimg_1038507" inpost="1" src="https://di.gameres.com/attachment/forum/202205/06/093405x4hdxh94c0nc01v9.jpg" referrerpolicy="no-referrer">
</div><br>
对模型师的要求是，制作完成的模型和贴图放到游戏引擎之后，能最大程度还原原画设计的形象。<br>
<br>
如果是静态物体，一般到这一步做完就结束了。后面直接交给场景编辑师在游戏引擎中搭建游戏场景即可。但实际上，游戏角色是要能动起来的。<br>
<br>
所以模型制作完成后还要交给绑定师架设骨骼、蒙皮、以及一些变形体，然后制作绑定控制器。即角色身上的这些奇怪的线圈和右边的面板。通过操纵这些东西，便可驱动角色做出对应的动作。<br>
<br>
绑定好的角色会交给动画师，他们会采用动作捕捉，或者手动设定关键帧的方式制作动画资源。<br>
<br>
<div align="center">
<img aid="1038508" zoomfile="https://di.gameres.com/attachment/forum/202205/06/093406zysms7u4qimsgmf1.jpg" data-original="https://di.gameres.com/attachment/forum/202205/06/093406zysms7u4qimsgmf1.jpg" width="600" id="aimg_1038508" inpost="1" src="https://di.gameres.com/attachment/forum/202205/06/093406zysms7u4qimsgmf1.jpg" referrerpolicy="no-referrer">
</div><br>
整个生产过程其实非常类似一条工业流水线，一环套一环。每一款成品游戏的美术资源都是由大量美术劳动力堆起来的。这块的开销也一直是整个游戏研发成本的大头。<br>
<br>
现在的玩家越来越挑剔，游戏行业竞争也越来越激烈。比如现在的3A大作，如果不支持开放世界已经不好意思说自己是本世代游戏了。<br>
<br>
开放世界是怎么让你觉得有开放感的呢？其实简单来说就是尽量多的生产内容，你就会觉得这款游戏非常开放。<br>
<br>
比如说《刺客信条》《孤岛惊魂》这种级别的经典的开放世界沙盒游戏，地图动不动就几十平方公里。这种规模的地图如果按照传统制作方式已经不现实。<br>
<br>
所以目前大量的程序化手段被应用到游戏开发过程中，像程序化地形、建筑、植物等都已经是很常见的做法了。<br>
<br>
目前游戏行业的整个趋势是最大程度地利用程序化制作美术资源。那怎么来理解基于AI的美术资源生产呢？<br>
<br>
其实简单说AI就是一种程序，所以我们做的工作本质上是在程序化生产主线下，引入AI的技术手段，从而实现一些传统方案无法做到的效果。<br>
<br>
下面我就给大家介绍一下，我们部门在原画、模型和动画三个方面做过的一些尝试。<br>
<br>
<strong><font color="#de5650">AI在原画方面的应用</font></strong><br>
<br>
首先是原画方面，我们做了两个辅助创作的工具。<br>
<br>
第一个应用是对二次元角色线稿进行自动上色的工具，并且可生成多套不同的上色方案。主要作用是给美术在设计二次元形象时，提供色彩搭配上的灵感。<br>
<br>
第二个工具是人脸的生成和编辑工具。该工具可基于美术绘制的人脸线稿生成真实的人脸照片，并且允许对生成人脸的属性进行编辑，这里展示的是对人脸的年龄进行修改后的结果。<br>
<br>
<div align="center">
<img aid="1038509" zoomfile="https://di.gameres.com/attachment/forum/202205/06/093406zkbxbthhbnt6bobb.jpg" data-original="https://di.gameres.com/attachment/forum/202205/06/093406zkbxbthhbnt6bobb.jpg" width="600" id="aimg_1038509" inpost="1" src="https://di.gameres.com/attachment/forum/202205/06/093406zkbxbthhbnt6bobb.jpg" referrerpolicy="no-referrer">
</div><br>
由于互联网上人脸是数据非常丰富的，人脸的结构相对也比较简单。所以目前这个工具可以生成非常高清的人脸照片。美术在设计写实类角色时，可以参考AI合成的人脸进行二次创作。<br>
<br>
当然，我知道很多同学对AI在原画方面是有更高的期待的。比如说，利用GAN或风格迁移等技术直接生成游戏的场景原画。因为这也是AI技术最早出圈被大家知道的一批应用。<br>
<br>
不过目前想要实际落地还稍微有点困难，不是说技术本身有问题。主要是因为游戏原画设计追求的不一定是真实，更多是一种特定艺术风格下的视觉表达。<br>
<br>
我们随便找一幅游戏画面对比一下，这种图片跟日常照片是有明显区别的。在当前的数据条件下，想生成一个这种级别的AI模型还比较困难，所以，如何让AI在原画设计方面发挥更多的作用，也是我们未来的重点努力方向之一。<br>
<br>
<div align="center">
<img aid="1038510" zoomfile="https://di.gameres.com/attachment/forum/202205/06/093406a7djvrrisqes6dcj.jpg" data-original="https://di.gameres.com/attachment/forum/202205/06/093406a7djvrrisqes6dcj.jpg" width="600" id="aimg_1038510" inpost="1" src="https://di.gameres.com/attachment/forum/202205/06/093406a7djvrrisqes6dcj.jpg" referrerpolicy="no-referrer">
</div><br>
<strong><font color="#de5650">用AI制作模型</font></strong><br>
<br>
在这一块我们的主要工作围绕在人脸模型。<br>
<br>
首先，简单介绍一个基础设施叫三维参数化人脸模型。这是一个双线性模型，基于大量三维扫描得到的三维人脸数据制作出来的，有脸型和表情两个维度。简单说就是任意给定一组脸型参数和表情参数，就会得到对应参数下的三维人头模型。<br>
<br>
<div align="center">
<img aid="1038511" zoomfile="https://di.gameres.com/attachment/forum/202205/06/093406vs6ezhjrxkekk6kx.jpg" data-original="https://di.gameres.com/attachment/forum/202205/06/093406vs6ezhjrxkekk6kx.jpg" width="600" id="aimg_1038511" inpost="1" src="https://di.gameres.com/attachment/forum/202205/06/093406vs6ezhjrxkekk6kx.jpg" referrerpolicy="no-referrer">
</div><br>
在2018年，我们自己扫描并制作了一套高质量的三维参数化人脸。当时一共采集了500名中国人，男女各占一半；从10-60岁，每人扫描了7套表情，共3500套。<br>
<br>
<div align="center">
<img aid="1038512" zoomfile="https://di.gameres.com/attachment/forum/202205/06/093407ayicbhyc33mmzyiy.jpg" data-original="https://di.gameres.com/attachment/forum/202205/06/093407ayicbhyc33mmzyiy.jpg" width="600" id="aimg_1038512" inpost="1" src="https://di.gameres.com/attachment/forum/202205/06/093407ayicbhyc33mmzyiy.jpg" referrerpolicy="no-referrer">
</div><br>
我们在这块投入了不小的成本，去年的游戏开发者大会GDC上也做过一次分享。我相信很多从事三维人脸相关研究的同学会对这个模型概念非常熟悉。<br>
<br>
这是由一篇1999年的SIGGRAPH论文提出来的概念，专业名称叫3DMM。目前学术界其实是有很出名的开源3DMM数据，我们为什么不直接用这种开源模型呢？主要有三方面原因：<br>
<br>
首先是版权问题，因为我们希望这套技术是真的能够在游戏产品中用起来。<br>
<br>
其次是精度问题，这些开源模型的精度距离实际游戏的标准还是有不小差距。我们早期做实验用的也是这些模型，但是美术同学对开源模型的人和质量非常嫌弃。<br>
<br>
所以我们自己采集时，每一个人头后续都是发包人工精修，质量很高。<br>
<br>
最后是人种问题，因为这种开源模型一般都是欧美机构发布的。他们采集的对象主要是有明显的高鼻梁、深眼窝特点的欧美高加索人种，而不是亚洲人。<br>
<br>
基于这些原因，我们果断决定自己制作一套这样的模型。<br>
<br>
<div align="center">
<img aid="1038513" zoomfile="https://di.gameres.com/attachment/forum/202205/06/093407q94i64949iqw6cbw.jpg" data-original="https://di.gameres.com/attachment/forum/202205/06/093407q94i64949iqw6cbw.jpg" width="600" id="aimg_1038513" inpost="1" src="https://di.gameres.com/attachment/forum/202205/06/093407q94i64949iqw6cbw.jpg" referrerpolicy="no-referrer">
</div><br>
在AI领域，参数化人脸的主要作用是提供关于人脸的三维形状先验。制作好的参数化三维人脸模型，可以用于从二维照片中重建三维人脸模型。这套参数化人脸模型，在东亚人脸照片上取得了非常好的重建效果。<br>
<br>
<div align="center">
<img aid="1038514" zoomfile="https://di.gameres.com/attachment/forum/202205/06/093407r3gdcgm0gwg7l0lz.jpg" data-original="https://di.gameres.com/attachment/forum/202205/06/093407r3gdcgm0gwg7l0lz.jpg" width="600" id="aimg_1038514" inpost="1" src="https://di.gameres.com/attachment/forum/202205/06/093407r3gdcgm0gwg7l0lz.jpg" referrerpolicy="no-referrer">
</div><br>
当然，由于单视角照片存在一些深度方面的缺失，很难还原类似鼻梁高度，眼窝这方面的特征。<br>
<br>
所以我们也开发了一套多视角的重建算法，如果条件允许的话，可拍摄演员的多张照片进行重建。这边大家可以对比一下，右边多视角重建结果对演员鼻子形状的还原程度，比单视角高非常多。<br>
<br>
<div align="center">
<img aid="1038515" zoomfile="https://di.gameres.com/attachment/forum/202205/06/093407x7pz59zgpofxf0nn.jpg" data-original="https://di.gameres.com/attachment/forum/202205/06/093407x7pz59zgpofxf0nn.jpg" width="600" id="aimg_1038515" inpost="1" src="https://di.gameres.com/attachment/forum/202205/06/093407x7pz59zgpofxf0nn.jpg" referrerpolicy="no-referrer">
</div><br>
除了从照片中重建三维模型，这套参数化人脸还有一个更重要的应用，批量给游戏生成人头模型。<br>
<br>
如果游戏的人头资源标准跟库里的人头标准一致，那就很简单了。可以直接在参数化人脸模型的参数空间采样，把采样模型给到游戏项目使用。但这种情况一般不多，因为每个游戏都有自己特定的需求。<br>
<br>
所以，一个更常见的生成方式是对项目组的模型进行自动批量变形。简单说就是把生成的模型相对于平均脸的变化，迁移到项目组的模型上，可以是表情和脸型的迁移变化。并且，所有变形都可以用项目规定的骨骼蒙皮进行表达。<br>
<br>
<div align="center">
<img aid="1038516" zoomfile="https://di.gameres.com/attachment/forum/202205/06/093407ktkq5f5y51krdkzd.jpg" data-original="https://di.gameres.com/attachment/forum/202205/06/093407ktkq5f5y51krdkzd.jpg" width="600" id="aimg_1038516" inpost="1" src="https://di.gameres.com/attachment/forum/202205/06/093407ktkq5f5y51krdkzd.jpg" referrerpolicy="no-referrer">
</div><br>
这是一组我们生成的结果，最左边是项目组提供给我们的角色模型。我们以此自动批量生成同风格，但脸型和五官有明显区别的模型，且每个模型都可生成一套表情。<br>
<br>
即项目组只需做一个静态模型便能自动批量生成许多绑定好的模型。这对于追求千人千面的开放世界游戏非常有价值，能够以级低成本让游戏中每个NPC看起来都不同。<br>
<br>
<div align="center">
<img aid="1038517" zoomfile="https://di.gameres.com/attachment/forum/202205/06/093408zvbbqzdszcpbilcc.jpg" data-original="https://di.gameres.com/attachment/forum/202205/06/093408zvbbqzdszcpbilcc.jpg" width="600" id="aimg_1038517" inpost="1" src="https://di.gameres.com/attachment/forum/202205/06/093408zvbbqzdszcpbilcc.jpg" referrerpolicy="no-referrer">
</div><br>
这是我们对两个Metahuman模型变形后的效果，可以看到生成的人头模型跟原始的资源标准完全兼容，且变形质量生成的模型作为实际游戏的头模是绰绰有余的。<br>
<br>
大家要知道，像Metahuman这种级别模型，一个头的成本，保守计算都要小几十万人民币，所以该技术是非常有价值的。<br>
<br>
为了进一步丰富我们的三维人头数据，我们搭建了自己的三维扫描实验室，目前在杭州园区搭建了专门扫描人头的设备。左边是设计图，右边是搭建完成后的实物。<br>
<br>
是一个正20面体，一共包含53台单反和150组定制LED灯光。整套系统都是我们自己设计和搭建的。后续还将会在网易广州和上海园区分别搭建更大的全身扫描装备。<br>
<br>
<div align="center">
<img aid="1038518" zoomfile="https://di.gameres.com/attachment/forum/202205/06/093408l383durdyjhx0zmd.jpg" data-original="https://di.gameres.com/attachment/forum/202205/06/093408l383durdyjhx0zmd.jpg" width="600" id="aimg_1038518" inpost="1" src="https://di.gameres.com/attachment/forum/202205/06/093408l383durdyjhx0zmd.jpg" referrerpolicy="no-referrer">
</div><br>
三维扫描的原理其实非常简单。摄影测量算法，从多视角照片中计算人头的三维点云。这是我们系统扫描的一组样例，精度可对标国内外一线扫描服务供应商。<br>
<br>
<div align="center">
<img aid="1038519" zoomfile="https://di.gameres.com/attachment/forum/202205/06/093408zqzut7qhqnesuxvt.gif" data-original="https://di.gameres.com/attachment/forum/202205/06/093408zqzut7qhqnesuxvt.gif" width="400" id="aimg_1038519" inpost="1" src="https://di.gameres.com/attachment/forum/202205/06/093408zqzut7qhqnesuxvt.gif" referrerpolicy="no-referrer">
</div><br>
这是基于我们的扫描流程制作的一组表情基的效果，扫描模型对演员面部细节还原程度非常高。<br>
<br>
之前有说该设备具有150组定制LED灯光，这组灯光花了很高的成本。每一盏灯的开关和亮度可独立控制。一组灯光包含三个灯头，分别安装了一个普通无偏振的uv镜和两个偏振镜。相对于相机上安装的偏振镜方向，两个偏振镜一个平行、一个垂直。<br>
<br>
<div align="center">
<img aid="1038520" zoomfile="https://di.gameres.com/attachment/forum/202205/06/093408y16z4iuss13i36a3.jpg" data-original="https://di.gameres.com/attachment/forum/202205/06/093408y16z4iuss13i36a3.jpg" width="341" id="aimg_1038520" inpost="1" src="https://di.gameres.com/attachment/forum/202205/06/093408y16z4iuss13i36a3.jpg" referrerpolicy="no-referrer">
</div><br>
对摄影比较熟悉的同学应该很熟悉偏振镜的用法，是一种常用的uv镜。主要用于非金属物体表面的一些不必要的反射光，还可还原物体本身颜色。<br>
<br>
<div align="center">
<img aid="1038521" zoomfile="https://di.gameres.com/attachment/forum/202205/06/093408eztl6lvatt6tttxt.jpg" data-original="https://di.gameres.com/attachment/forum/202205/06/093408eztl6lvatt6tttxt.jpg" width="600" id="aimg_1038521" inpost="1" src="https://di.gameres.com/attachment/forum/202205/06/093408eztl6lvatt6tttxt.jpg" referrerpolicy="no-referrer">
</div><br>
偏振镜的原理是什么？光具备波粒二象性，既是粒子、也是一种电磁波。它的振动方向与传播方向垂直，类型的波叫横波，所有的横波都具有偏振现象。<br>
<br>
若光的偏振方向与偏振镜方向平行，那所有能量都会通过；若是垂直的，则所有能量会被过滤。<br>
<br>
基于这个原理，我们可以给扫描物体一次性拍摄8组灯光下照片，然后利用这8张照片就能算出物体表面的材质，也就是漫反射、高光和法线的信息。<br>
<br>
这8组灯光分别是4组平行偏振光和4组交叉偏振光，对每一组而言，首先打开所有灯光，然后灯光亮度按照灯光在三维空间的坐标值递减。最后在XYZ三个方向分别可产生一组灯光。<br>
<br>
<div align="center">
<img aid="1038522" zoomfile="https://di.gameres.com/attachment/forum/202205/06/093409o1t75p1tpcftdaad.jpg" data-original="https://di.gameres.com/attachment/forum/202205/06/093409o1t75p1tpcftdaad.jpg" width="600" id="aimg_1038522" inpost="1" src="https://di.gameres.com/attachment/forum/202205/06/093409o1t75p1tpcftdaad.jpg" referrerpolicy="no-referrer">
</div><br>
目前这套设备刚搭建完成，在人脸材质扫描方面我们刚刚起步，后续会逐渐加大这块的投入。<br>
<br>
<strong><font color="#de5650">将AI应用于动画制作</font></strong><br>
<br>
这块是我们这几年工作的重心。美术资产一般占整个游戏研发总成本里最大的部分，但在其中，动画一般又会占整个美术资产最大的一块。<br>
<br>
虽然原画和模型也很贵，但大部分属于一次性开销，而动画需要配合剧情持续性产出，高质量的动画，一分钟的制作成本就可以很轻松过万。<br>
<br>
在动画这块首先是在光学动捕数据的清洗方面做了些工作。光学动捕的原理其实很简单，就是在紧身动捕服表面设置很多标记点。通过多视角红外相机跟踪标记点在三维空间中的坐标，并根据坐标算来人体骨骼的旋转和平移信息。<br>
<br>
自动算出的这些信息不可避免有一些错误，进而会导致解算出来的骨骼动画可能存在异常。所以在实际的动捕过程流程中，会有专门的美术负责对动捕出来的标记点进行清洗。<br>
<br>
资深的动捕美术通过直接看标记点的轨迹曲线，便知道出错类型及如何修改。这块也是目前动捕工作流中主要的人工工作量。<br>
<br>
18年育碧提出一种算法，通过AI模型来取代上面的过程，当时发表在了SIGGRAPH上。<br>
<br>
我们在19年时候投资了一家法国3A游戏工作室Quantic Dream（《底特律：变人》的制作公司），因此当时开始有技术合作。他们提出了上面的要求，我们对此进行了跟进。在做了一年多以后，我们找到了精度更高的解决方案，也发表在了SIGGRAPH上。<br>
<br>
<div align="center">
<img aid="1038523" zoomfile="https://di.gameres.com/attachment/forum/202205/06/093409qy0z8yedquy860yh.gif" data-original="https://di.gameres.com/attachment/forum/202205/06/093409qy0z8yedquy860yh.gif" width="400" id="aimg_1038523" inpost="1" src="https://di.gameres.com/attachment/forum/202205/06/093409qy0z8yedquy860yh.gif" referrerpolicy="no-referrer">
</div><br>
目前这套算法已经以Vicon软件的插件形式，部署在网易互娱和Quantic Dream的动捕工作流中。这里是一个例子。这是原始含噪音的标记点，闪来闪去的就是局部噪音，留在原地的那些点就是跟丢的点。<br>
<br>
接下来要介绍的几个工作是我们部门落地最多的项目，首先是一套基于普通单目摄像头的轻量级面部动捕系统。<br>
<br>
<div align="center">
<img aid="1038524" zoomfile="https://di.gameres.com/attachment/forum/202205/06/093409p5vuq0u5qnc3zqbz.gif" data-original="https://di.gameres.com/attachment/forum/202205/06/093409p5vuq0u5qnc3zqbz.gif" width="400" id="aimg_1038524" inpost="1" src="https://di.gameres.com/attachment/forum/202205/06/093409p5vuq0u5qnc3zqbz.gif" referrerpolicy="no-referrer">
</div><br>
基本原理是利用前面介绍的那套三维参数化人脸模型，对视频中演员的脸型、表情头部姿态进行回归，把回归得到的系数重定向到游戏角色上。也会配合CV检测和识别模型，加强算法对眨眼、视线、舌头和整体情绪的捕捉精度。<br>
<br>
这个项目从18年开始做，前前后后差不多有10位同事参与，里面的算法模块都是我们自己开发的。打磨到现在，已经是一套非常成熟的in-house面部动捕解决方案。<br>
<br>
围绕这套算法，我们还打造了一整套的工具链。有实时动捕预览工具、有针对动捕结果进行离线调整和编辑的工具、还有Maya/Max里的动捕数据重定向插件。<br>
<br>
<div align="center">
<img aid="1038525" zoomfile="https://di.gameres.com/attachment/forum/202205/06/093409dnozxbn3uuzobx7r.jpg" data-original="https://di.gameres.com/attachment/forum/202205/06/093409dnozxbn3uuzobx7r.jpg" width="600" id="aimg_1038525" inpost="1" src="https://di.gameres.com/attachment/forum/202205/06/093409dnozxbn3uuzobx7r.jpg" referrerpolicy="no-referrer">
</div><br>
另外为了方便项目组接入面部动捕系统，还专门开发了一套适配算法的面部自动绑定插件。此外，核心算法还打包了全平台SDK，在iPhone 6s以上的机器可以做到实时单核单线程。<br>
<br>
这套系统在游戏里有着非常多的应用场景。<br>
<br>
首先是辅助动画师制作正式的游戏动画资源。相比于传统一帧一帧手Key，采用动捕方案的制作效率有明显优势，且只要演员表演到位，效果跟美术手Key几乎无差别。<br>
<br>
其次，可以给营销同学快速产出一些面部动画素材。虽然该方面对精度要求没那么高，但对时效性要求却很高，慢了就蹭不上热点。因此这种轻量级的方案非常适合营销场景。比如某段视频火了，用这套工具可以非常快速地产出面部动画素材。<br>
<br>
另外，因为整套算法提供全平台的SDK，因此可打包在游戏里给玩家提供UGC玩法。例如在《一梦江湖》中上线的颜艺系统，可让玩家录制自己的表情动画。<br>
<br>
<div align="center">
<img aid="1038526" zoomfile="https://di.gameres.com/attachment/forum/202205/06/093410njqyzzxboqphhpbx.gif" data-original="https://di.gameres.com/attachment/forum/202205/06/093410njqyzzxboqphhpbx.gif" width="400" id="aimg_1038526" inpost="1" src="https://di.gameres.com/attachment/forum/202205/06/093410njqyzzxboqphhpbx.gif" referrerpolicy="no-referrer">
</div><br>
右边是我在B站上找到的视频，是玩家系统录制的一段打哈欠的动画，上传到B站后传播效果非常好。<br>
<br>
最后，这套算法还可以支持一些虚拟主播的场景。比如《第五人格》秃秃杯电竞比赛的虚拟解说、云音乐look直播的虚拟主播等等，用的都是这套技术。<br>
<br>
另外，我们还配合高精度三维扫描设备，测试了面部动捕算法在超写实模型上的效果。用模特自己的视频来驱动他自己的角色，样可以更好的对比表情的还原度。<br>
<br>
<div align="center">
<img aid="1038527" zoomfile="https://di.gameres.com/attachment/forum/202205/06/093410mor13508xqrlzfa3.gif" data-original="https://di.gameres.com/attachment/forum/202205/06/093410mor13508xqrlzfa3.gif" width="400" id="aimg_1038527" inpost="1" src="https://di.gameres.com/attachment/forum/202205/06/093410mor13508xqrlzfa3.gif" referrerpolicy="no-referrer">
</div><br>
这是另外一组效果，从效果上可见不管是扫描重建还是面部捕捉，技术都足以支持这种高精度场景。<br>
<br>
跟面部动捕类似，们也做了一套轻量级基于普通摄像头的身体动捕系统。单视角和多视角输入都支持，原理跟面捕类似，利用一套参数化人体模型，对各关节参数进行拟合。同样会配合CV模型提升优化结果的合理性。<br>
<br>
该项目打磨了两年时间，效果和稳定性相当不错。<br>
<br>
<div align="center">
<img aid="1038528" zoomfile="https://di.gameres.com/attachment/forum/202205/06/093410wgjrffen5kerqree.gif" data-original="https://di.gameres.com/attachment/forum/202205/06/093410wgjrffen5kerqree.gif" width="400" id="aimg_1038528" inpost="1" src="https://di.gameres.com/attachment/forum/202205/06/093410wgjrffen5kerqree.gif" referrerpolicy="no-referrer">
</div><br>
这是在冬奥之后，我们用该技术项目制作视频。按传统制作方式，这种营销策划案不太可能实现，因为难以找到能还原动作的演员。一套下来没有6位数的开销和1个多月的制作周期很难完成。但用这套AI的方案，成本可以忽略不计。<br>
<br>
<div align="center">
<img aid="1038529" zoomfile="https://di.gameres.com/attachment/forum/202205/06/093410bzptedlif3hp5yhf.gif" data-original="https://di.gameres.com/attachment/forum/202205/06/093410bzptedlif3hp5yhf.gif" width="400" id="aimg_1038529" inpost="1" src="https://di.gameres.com/attachment/forum/202205/06/093410bzptedlif3hp5yhf.gif" referrerpolicy="no-referrer">
</div><br>
这个是更早时候，跟《大话西游》项目组合作的一段视频，官网和B站上都能搜到。当时请了B站舞蹈区的知名UP主，用三部手机录了这套动作。用动捕算法得出动作后，重定向到游戏角色上，整体效果非常精美。<br>
<br>
<div align="center">
<img aid="1038530" zoomfile="https://di.gameres.com/attachment/forum/202205/06/093410rqpnvxbxoxv8hxt9.jpg" data-original="https://di.gameres.com/attachment/forum/202205/06/093410rqpnvxbxoxv8hxt9.jpg" width="600" id="aimg_1038530" inpost="1" src="https://di.gameres.com/attachment/forum/202205/06/093410rqpnvxbxoxv8hxt9.jpg" referrerpolicy="no-referrer">
</div><br>
另外，在给《明日之后》项目组制作的动画素材中，只用了一个单目摄像头，捕捉了身体和面部动作。只要拍得足够清晰，手指动作也是可以精准捕捉的。<br>
<br>
<div align="center">
<img aid="1038531" zoomfile="https://di.gameres.com/attachment/forum/202205/06/093411npvhrpvpphrn6zn1.gif" data-original="https://di.gameres.com/attachment/forum/202205/06/093411npvhrpvpphrn6zn1.gif" width="400" id="aimg_1038531" inpost="1" src="https://di.gameres.com/attachment/forum/202205/06/093411npvhrpvpphrn6zn1.gif" referrerpolicy="no-referrer">
</div><br>
除了视频输出，我们还做了基于音频输入生成动画的技术。比如从语音输入生成角色的面部和肢体动画，围绕这个技术做了一整套的工具链。启动时间也非常早，18年就在不少游戏上落地实装。<br>
<br>
当时做得还比较简单，只支持口型和几种简单的基础情绪。后来我们做了持续的基础升级和迭代，增加了语音驱动头动、眼动、手动、面部微表情，还有肢体动作等等。<br>
<br>
另一个从音频输入生成动画的工作，是基于音乐生成舞蹈动作。这项工作我们从2018年开始研究，经过几年迭代最终形成了一套方案，详细的技术方案在论文里有介绍，这里主要展示实际落地效果：首先是二次元女团舞；<br>
<br>
<div align="center">
<img aid="1038532" zoomfile="https://di.gameres.com/attachment/forum/202205/06/093411d19b7s4dgob2c194.gif" data-original="https://di.gameres.com/attachment/forum/202205/06/093411d19b7s4dgob2c194.gif" width="400" id="aimg_1038532" inpost="1" src="https://di.gameres.com/attachment/forum/202205/06/093411d19b7s4dgob2c194.gif" referrerpolicy="no-referrer">
</div><br>
这是一段韩舞的动画，也是网易CC直播年度盛典的开场舞蹈。<br>
<br>
<div align="center">
<img aid="1038533" zoomfile="https://di.gameres.com/attachment/forum/202205/06/093411dg2fqlkyq35c5553.jpg" data-original="https://di.gameres.com/attachment/forum/202205/06/093411dg2fqlkyq35c5553.jpg" width="600" id="aimg_1038533" inpost="1" src="https://di.gameres.com/attachment/forum/202205/06/093411dg2fqlkyq35c5553.jpg" referrerpolicy="no-referrer">
</div><br>
另外，我们也会用一些网络热门歌曲合成舞蹈。去年圣诞节时，我们用虚拟偶像I.F.制作的B站互动视频，其中所有动画都是通过AI技术生成的。目前这套AI动画的解决方案已经相当成熟，在内部经过了大量项目的验证，目前也在持续为网易的各个项目组输出动作资源。<br>
<br>
目前这套AI动画解决方案相当成熟，在内部经过大量项目验证后给网易各个项目持续不断输出动作资源。<br>
<br>
<strong><font color="#de5650">技术总结</font></strong><br>
<br>
最后简单总结一下，AI技术对程序化美术资源生成能产生明显的促进作用。根据我们的实践经验，在人脸、人体的模型和动画方面，它甚至可以在一定程度上取代一些初级执行向美术的工作。利用我们的AI方案，普遍可以比传统方案提升5-10倍的制作效率。<br>
<br>
但目前向让AI从事一些更高级的动作仍然比较困难，这也是我们未来努力的方向。<br>
<br>
数据是AI的核心，AI模型有多少能力其实很大程度上取决于能给模型提供多少价值的数据。因此，难点便是高质量的数据比较稀缺。<br>
<br>
跟照片、语音、文字这种日常生产的数据不太一样，游戏资产获取门槛比较高。比如在某个景点看到一个很有特色的雕塑，绝大部分人的反应可能是掏出手机，拍张照记录下来，但几乎不会有人掏出电脑现场建个模。<br>
<br>
当然随着技术的进步，游戏资源的制作门槛肯定是越来越低的。而且像元宇宙这样的热门应用场景，游戏厂商自身会让广大玩家参与到虚拟世界的内容创造过程中来。<br>
<br>
所以我相信随着数据的持续积累，未来AI技术也是可以能从事一些更高级工作，这也是我们的努力方向。<br>
<br>
以上就是本次分享的全部内容，谢谢大家！<br>
<br>
<font size="2"><font color="#808080"></font></font><br>
<br>
  
</div>
            